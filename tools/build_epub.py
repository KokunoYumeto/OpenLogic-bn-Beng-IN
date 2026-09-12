from __future__ import annotations

import base64
import copy
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from lxml import etree


REPO = Path(__file__).resolve().parents[1]
INPUT_HTML = REPO / "build" / "reader" / "openlogic-bn-reader.html"
HTML_RECEIPT = REPO / "build" / "reader" / "html-receipt.json"
STATUS = REPO / "evidence" / "STATUS.json"
FONT_LICENSE = REPO / "fonts" / "Noto-fonts-LICENSE.txt"
OUTPUT = REPO / "build" / "epub"
CANONICAL = OUTPUT / "unpacked"
COLD = OUTPUT / "cold-unpacked"
EPUB = OUTPUT / "openlogic-bn-Beng-IN-sets-relations.epub"
COLD_EPUB = OUTPUT / "openlogic-bn-Beng-IN-sets-relations-cold.epub"
PACKAGE_MANIFEST = OUTPUT / "PACKAGE_MANIFEST.json"
BUILD_RECEIPT = OUTPUT / "BUILD_RECEIPT.json"
EVIDENCE = REPO / "evidence" / "EPUB_0_2_0_BUILD.json"

XHTML_NS = "http://www.w3.org/1999/xhtml"
MATHML_NS = "http://www.w3.org/1998/Math/MathML"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"
DC_NS = "http://purl.org/dc/elements/1.1/"
CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"
XML_NS = "http://www.w3.org/XML/1998/namespace"

LANGUAGE = "bn-Beng-IN"
RELEASE_TAG = "v0.2.0-sets-relations"
RELEASE_URL = (
    "https://github.com/KokunoYumeto/OpenLogic-bn-Beng-IN/"
    "releases/tag/v0.2.0-sets-relations"
)
HTML_URL = (
    "https://github.com/KokunoYumeto/OpenLogic-bn-Beng-IN/releases/download/"
    "v0.2.0-sets-relations/openlogic-bn-Beng-IN-sets-relations.html"
)
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
EXPECTED_HTML_BYTES = 4_105_887
EXPECTED_HTML_SHA256 = "3d2c1df0ba2f8d91ddf8de832744a70f8e2ba4b179a6ea2a533fed4a273d9346"
EXPECTED_MATHML = 909
EXPECTED_SECTIONS = 15
EXPECTED_ENVIRONMENTS = 88
EXPECTED_FIGURES = 6
MODIFIED = "2026-09-13T00:00:00Z"
FIXED_ZIP_TIME = (2026, 9, 13, 0, 0, 0)

FIGURE_FILENAMES = {
    "UNION": "union.svg",
    "INTERSECTION": "intersection.svg",
    "DIFFERENCE": "difference.svg",
    "GRAPHONE": "graph-one.svg",
    "GRAPHTWO": "graph-two.svg",
    "TREE": "tree.svg",
}
FONT_FILENAMES = {
    "04935aea18655c451d05b1d4bb5bdc835226a221663f89a2ecfbcfdc4483e399": "NotoSerifBengali-Regular.ttf",
    "f752131cd292f3e0fd7a25c8fc86f5424062bc06e29f6dfadcb3c09ff4881dd0": "NotoSerifBengali-Bold.ttf",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def parse_xml(path: Path) -> etree._ElementTree:
    return etree.parse(
        str(path),
        etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True),
    )


def safe_clear(path: Path) -> None:
    resolved = path.resolve()
    output = OUTPUT.resolve()
    require(resolved != output and resolved.is_relative_to(output), f"unsafe build path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def local_name(element: etree._Element) -> str:
    return etree.QName(element).localname


def add_text_element(parent: etree._Element, name: str, text: str, **attributes: str) -> etree._Element:
    element = etree.SubElement(parent, f"{{{XHTML_NS}}}{name}")
    for key, value in attributes.items():
        element.set(key, value)
    element.text = text
    return element


def add_link(parent: etree._Element, text: str, href: str) -> etree._Element:
    link = etree.SubElement(parent, f"{{{XHTML_NS}}}a")
    link.set("href", href)
    link.text = text
    return link


def document_shell(title: str) -> tuple[etree._Element, etree._Element]:
    root = etree.Element(
        f"{{{XHTML_NS}}}html",
        nsmap={None: XHTML_NS, "epub": EPUB_NS},
    )
    root.set("lang", LANGUAGE)
    root.set(f"{{{XML_NS}}}lang", LANGUAGE)
    root.set("dir", "ltr")
    head = etree.SubElement(root, f"{{{XHTML_NS}}}head")
    meta = etree.SubElement(head, f"{{{XHTML_NS}}}meta")
    meta.set("charset", "utf-8")
    add_text_element(head, "title", title)
    stylesheet = etree.SubElement(head, f"{{{XHTML_NS}}}link")
    stylesheet.set("rel", "stylesheet")
    stylesheet.set("type", "text/css")
    stylesheet.set("href", "styles/reader.css")
    body = etree.SubElement(root, f"{{{XHTML_NS}}}body")
    return root, body


def serialize_xhtml(root: etree._Element) -> bytes:
    return etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True,
        method="xml",
        pretty_print=False,
    )


def extract_styles_and_fonts(root: etree._Element, destination: Path) -> dict:
    namespace = {"x": XHTML_NS}
    styles = root.xpath("/x:html/x:head/x:style", namespaces=namespace)
    require(len(styles) == 2, f"expected two embedded style blocks, found {len(styles)}")
    css = "\n\n".join(element.text or "" for element in styles)
    pattern = re.compile(r"data:font/ttf;base64,([A-Za-z0-9+/=]+)")
    extracted: list[dict] = []

    def replace_font(match: re.Match[str]) -> str:
        payload = base64.b64decode(match.group(1), validate=True)
        digest = sha256(payload)
        require(digest in FONT_FILENAMES, f"unexpected embedded font: {digest}")
        filename = FONT_FILENAMES[digest]
        target = destination / "OEBPS" / "fonts" / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        extracted.append({"filename": filename, "bytes": len(payload), "sha256": digest})
        return f"../fonts/{filename}"

    css = pattern.sub(replace_font, css)
    require(len(extracted) == 2, f"expected two embedded fonts, found {len(extracted)}")
    require("data:font" not in css, "embedded font data URI remains in CSS")
    require("position:fixed" not in re.sub(r"\s+", "", css).lower(), "fixed-position CSS is not reflowable")
    css += (
        "\n\n/* EPUB additions: preserve reflow and readable auxiliary pages. */\n"
        "img.diagram{height:auto;}\n"
        ".scope-note{border:2px solid #9a6b00;padding:1rem;background:#fff8dc;}\n"
        ".metadata{font-size:.92em;color:#39434a;}\n"
        "pre.license{white-space:pre-wrap;overflow-wrap:anywhere;font-family:monospace;font-size:.82em;}\n"
    )
    css_path = destination / "OEBPS" / "styles" / "reader.css"
    css_path.parent.mkdir(parents=True, exist_ok=True)
    css_path.write_text(css, encoding="utf-8", newline="\n")

    head = root.xpath("/x:html/x:head", namespaces=namespace)[0]
    for style in styles:
        head.remove(style)
    link = etree.SubElement(head, f"{{{XHTML_NS}}}link")
    link.set("rel", "stylesheet")
    link.set("type", "text/css")
    link.set("href", "styles/reader.css")
    return {
        "css_bytes": css_path.stat().st_size,
        "css_sha256": sha256(css_path.read_bytes()),
        "fonts": sorted(extracted, key=lambda row: row["filename"]),
    }


def extract_figures(root: etree._Element, destination: Path, html_receipt: dict) -> list[dict]:
    namespace = {"x": XHTML_NS}
    images = root.xpath("//x:img", namespaces=namespace)
    receipts = html_receipt["figures"]
    require(len(images) == len(receipts) == EXPECTED_FIGURES, "figure count drift")
    records: list[dict] = []
    for image, receipt in zip(images, receipts, strict=True):
        source = image.get("src") or ""
        prefix = "data:image/svg+xml;base64,"
        require(source.startswith(prefix), "reader figure is not an embedded SVG data URI")
        payload = base64.b64decode(source[len(prefix) :], validate=True)
        digest = sha256(payload)
        require(digest == receipt["svg_sha256"], f"figure hash drift: {receipt['name']}")
        filename = FIGURE_FILENAMES[receipt["name"]]
        target = destination / "OEBPS" / "images" / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        image.set("src", f"images/{filename}")
        require(bool((image.get("alt") or "").strip()), f"missing alternative text: {filename}")
        records.append(
            {
                "name": receipt["name"],
                "filename": filename,
                "bytes": len(payload),
                "sha256": digest,
                "alt": image.get("alt"),
            }
        )
    return records


def prepare_content(destination: Path, html_receipt: dict) -> tuple[dict, list[dict]]:
    tree = parse_xml(INPUT_HTML)
    root = tree.getroot()
    require(root.tag == f"{{{XHTML_NS}}}html", "input reader is not XHTML")
    root.set("lang", LANGUAGE)
    root.set(f"{{{XML_NS}}}lang", LANGUAGE)
    root.set("dir", "ltr")
    style_record = extract_styles_and_fonts(root, destination)
    figures = extract_figures(root, destination, html_receipt)
    namespace = {"x": XHTML_NS, "m": MATHML_NS}
    headings = root.xpath("//x:h1 | //x:h2", namespaces=namespace)
    require(headings and local_name(headings[0]) == "h1", "reader title heading missing")
    if headings[0].get("id") is None:
        headings[0].set("id", "book-title")
    ids = [element.get("id") for element in root.xpath("//*[@id]")]
    require(len(ids) == len(set(ids)), "duplicate IDs in content document")
    math_count = len(root.xpath("//m:math", namespaces=namespace))
    section_count = len(root.xpath("//x:h2", namespaces=namespace))
    environment_count = sum(
        len(
            root.xpath(
                f'//x:div[contains(concat(" ", normalize-space(@class), " "), " {name} ")]',
                namespaces=namespace,
            )
        )
        for name in ("defn", "ex", "prop", "thm", "prob")
    )
    require(math_count == EXPECTED_MATHML, "MathML count drift")
    require(section_count == EXPECTED_SECTIONS, "section count drift")
    require(environment_count == EXPECTED_ENVIRONMENTS, "numbered environment count drift")
    content_path = destination / "OEBPS" / "content.xhtml"
    content_path.parent.mkdir(parents=True, exist_ok=True)
    payload = serialize_xhtml(root)
    content_path.write_bytes(payload)
    heading_records = [
        {
            "level": int(local_name(heading)[1]),
            "id": heading.get("id"),
            "title": " ".join("".join(heading.itertext()).split()),
        }
        for heading in headings
    ]
    return (
        {
            "path": "OEBPS/content.xhtml",
            "bytes": len(payload),
            "sha256": sha256(payload),
            "mathml_expressions": math_count,
            "sections": section_count,
            "numbered_environments": environment_count,
            "headings": len(heading_records),
            "style": style_record,
        },
        heading_records,
    )


def prepare_about(destination: Path) -> dict:
    title = "এই EPUB সংস্করণ সম্পর্কে"
    root, body = document_shell(title)
    main = etree.SubElement(body, f"{{{XHTML_NS}}}main")
    main.set("id", "about")
    main.set(f"{{{EPUB_NS}}}type", "frontmatter")
    add_text_element(main, "h1", title)
    scope = add_text_element(
        main,
        "p",
        (
            "এটি ওপেন লজিক-এর বাংলা (ভারত) অনুবাদের একটি আংশিক, "
            "পুনঃপ্রবাহযোগ্য EPUB3 প্রকাশ। এতে ৭২২টি উৎস ফাইলের মধ্যে ১৮টি "
            "অনূদিত ফাইল রয়েছে; ৭০৪টি ফাইল এখনও অনূদিত নয়। এটি পূর্ণাঙ্গ সংস্করণ নয়।"
        ),
    )
    scope.set("class", "scope-note")
    add_text_element(main, "h2", "অন্তর্ভুক্ত বিষয়")
    add_text_element(main, "p", "সেট ও সম্পর্ক।")
    add_text_element(main, "h2", "অন্তর্ভুক্ত একক")
    units = add_text_element(
        main,
        "p",
        "OLP-0004–OLP-0019, OLP-0719 এবং OLP-0721 (মোট ১৮টি)।",
    )
    units.set("class", "metadata")
    add_text_element(main, "h2", "বিন্যাস ও প্রবেশযোগ্যতা")
    add_text_element(
        main,
        "p",
        (
            "বইটি পুনঃপ্রবাহযোগ্য পাঠ্য, নেটিভ MathML-এ ৯০৯টি গাণিতিক প্রকাশ, "
            "বর্ণনাসহ ছয়টি SVG চিত্র এবং নেভিগেশন সূচি ব্যবহার করে। "
            "MathML সমর্থন পাঠযন্ত্রভেদে ভিন্ন হতে পারে।"
        ),
    )
    add_text_element(main, "h2", "উৎস ও প্রকাশ")
    p = add_text_element(
        main,
        "p",
        f"উৎস কর্তৃত্ব: OpenLogicProject/OpenLogic revision {SOURCE_REVISION}. প্রকাশ: ",
    )
    release_link = add_link(p, RELEASE_TAG, RELEASE_URL)
    release_link.tail = "."
    add_text_element(main, "h2", "লাইসেন্স")
    p = add_text_element(
        main,
        "p",
        "মূল ও অনূদিত পাঠ্য CC BY 4.0-এর অধীন। অন্তর্ভুক্ত Noto ফন্ট SIL Open Font License 1.1-এর অধীন; ",
    )
    license_link = add_link(p, "ফন্টের পূর্ণ লাইসেন্স পড়ুন", "legal.xhtml")
    license_link.tail = "."
    english = add_text_element(
        main,
        "p",
        (
            "Scope note (English): This reflowable EPUB3 is a partial Bengali (India) "
            "edition containing 18 of 722 source units. The other 704 units remain untranslated."
        ),
    )
    english.set("lang", "en")
    english.set(f"{{{XML_NS}}}lang", "en")
    path = destination / "OEBPS" / "about.xhtml"
    payload = serialize_xhtml(root)
    path.write_bytes(payload)
    return {"path": "OEBPS/about.xhtml", "bytes": len(payload), "sha256": sha256(payload)}


def prepare_license(destination: Path) -> dict:
    license_text = FONT_LICENSE.read_text(encoding="utf-8")
    root, body = document_shell("Noto ফন্টের লাইসেন্স")
    main = etree.SubElement(body, f"{{{XHTML_NS}}}main")
    main.set("id", "font-license")
    main.set(f"{{{EPUB_NS}}}type", "copyright-page")
    add_text_element(main, "h1", "Noto ফন্টের লাইসেন্স")
    pre = add_text_element(main, "pre", license_text)
    pre.set("class", "license")
    path = destination / "OEBPS" / "legal.xhtml"
    payload = serialize_xhtml(root)
    path.write_bytes(payload)
    return {"path": "OEBPS/legal.xhtml", "bytes": len(payload), "sha256": sha256(payload)}


def prepare_navigation(destination: Path, headings: list[dict]) -> dict:
    root, body = document_shell("সূচি")
    nav = etree.SubElement(body, f"{{{XHTML_NS}}}nav")
    nav.set(f"{{{EPUB_NS}}}type", "toc")
    nav.set("id", "toc")
    nav.set("role", "doc-toc")
    add_text_element(nav, "h1", "সূচি")
    toc = etree.SubElement(nav, f"{{{XHTML_NS}}}ol")
    item = etree.SubElement(toc, f"{{{XHTML_NS}}}li")
    add_link(item, "এই EPUB সংস্করণ সম্পর্কে", "about.xhtml#about")

    current_nested: etree._Element | None = None
    for heading in headings:
        if heading["level"] == 1:
            item = etree.SubElement(toc, f"{{{XHTML_NS}}}li")
            add_link(item, heading["title"], f"content.xhtml#{heading['id']}")
            current_nested = None
        else:
            require(item is not None, "level-two heading precedes a level-one heading")
            if current_nested is None:
                current_nested = etree.SubElement(item, f"{{{XHTML_NS}}}ol")
            child = etree.SubElement(current_nested, f"{{{XHTML_NS}}}li")
            add_link(child, heading["title"], f"content.xhtml#{heading['id']}")

    landmarks = etree.SubElement(body, f"{{{XHTML_NS}}}nav")
    landmarks.set(f"{{{EPUB_NS}}}type", "landmarks")
    landmarks.set("id", "landmarks")
    add_text_element(landmarks, "h2", "পথনির্দেশ")
    landmark_list = etree.SubElement(landmarks, f"{{{XHTML_NS}}}ol")
    for label, href, epub_type in (
        ("সংস্করণ সম্পর্কে", "about.xhtml#about", "frontmatter"),
        ("মূল পাঠ্য", "content.xhtml#book-title", "bodymatter"),
        ("ফন্টের লাইসেন্স", "legal.xhtml#font-license", "copyright-page"),
    ):
        li = etree.SubElement(landmark_list, f"{{{XHTML_NS}}}li")
        link = add_link(li, label, href)
        link.set(f"{{{EPUB_NS}}}type", epub_type)

    path = destination / "OEBPS" / "nav.xhtml"
    payload = serialize_xhtml(root)
    path.write_bytes(payload)
    return {
        "path": "OEBPS/nav.xhtml",
        "bytes": len(payload),
        "sha256": sha256(payload),
        "toc_links": len(headings) + 1,
        "landmarks": 3,
    }


def prepare_package(destination: Path) -> dict:
    package = etree.Element(
        f"{{{OPF_NS}}}package",
        nsmap={None: OPF_NS, "dc": DC_NS},
    )
    package.set("version", "3.0")
    package.set("unique-identifier", "pub-id")
    package.set(f"{{{XML_NS}}}lang", LANGUAGE)
    package.set("prefix", "schema: http://schema.org/")
    metadata = etree.SubElement(package, f"{{{OPF_NS}}}metadata")

    def dc(name: str, text: str, identifier: str | None = None) -> etree._Element:
        element = etree.SubElement(metadata, f"{{{DC_NS}}}{name}")
        if identifier:
            element.set("id", identifier)
        element.text = text
        return element

    def meta(property_name: str, text: str, refines: str | None = None) -> etree._Element:
        element = etree.SubElement(metadata, f"{{{OPF_NS}}}meta")
        element.set("property", property_name)
        if refines:
            element.set("refines", refines)
        element.text = text
        return element

    dc("identifier", f"urn:sha256:{EXPECTED_HTML_SHA256}:epub3-{RELEASE_TAG}", "pub-id")
    dc("title", "ওপেন লজিক: সেট ও সম্পর্ক", "title")
    meta("title-type", "main", "#title")
    dc("language", LANGUAGE)
    dc("creator", "Open Logic Project and credited contributors", "creator")
    meta("role", "aut", "#creator").set("scheme", "marc:relators")
    dc("contributor", "Bengali (India) translation edition", "contributor")
    meta("role", "trl", "#contributor").set("scheme", "marc:relators")
    dc("publisher", "OpenLogic Bengali (India) translation programme")
    dc("subject", "Mathematical logic")
    dc("subject", "Set theory")
    dc("subject", "Relations")
    dc(
        "description",
        "Partial Bengali (India) reflowable EPUB3 edition: Sets and Relations, 18 of 722 source units; 704 units remain untranslated.",
    )
    dc("date", MODIFIED[:10])
    dc(
        "rights",
        "Creative Commons Attribution 4.0 International (CC BY 4.0); embedded Noto fonts use SIL Open Font License 1.1.",
    )
    meta("dcterms:modified", MODIFIED)
    meta(
        "dcterms:provenance",
        f"OpenLogicProject/OpenLogic revision {SOURCE_REVISION}; partial release {RELEASE_TAG}; sealed semantic HTML {EXPECTED_HTML_SHA256}.",
    )
    meta("rendition:layout", "reflowable")
    meta("rendition:orientation", "auto")
    meta("rendition:spread", "auto")
    meta("schema:accessMode", "textual")
    meta("schema:accessMode", "visual")
    meta("schema:accessModeSufficient", "textual")
    for feature in (
        "MathML",
        "alternativeText",
        "displayTransformability",
        "readingOrder",
        "structuralNavigation",
        "tableOfContents",
    ):
        meta("schema:accessibilityFeature", feature)
    for hazard in ("noFlashingHazard", "noMotionSimulationHazard", "noSoundHazard"):
        meta("schema:accessibilityHazard", hazard)
    meta(
        "schema:accessibilitySummary",
        (
            "Partial reflowable Bengali (India) edition with semantic headings, native presentation MathML, "
            "a navigation document, and alternative text for six vector diagrams. The package is script-free "
            "and contains no audio, flashing, or motion. Reading-system support for MathML varies. Automated "
            "validation is not a human accessibility certification."
        ),
    )

    manifest = etree.SubElement(package, f"{{{OPF_NS}}}manifest")
    resources = [
        ("nav", "nav.xhtml", "nav", "nav.xhtml", "application/xhtml+xml"),
        ("about", "about.xhtml", "", "about.xhtml", "application/xhtml+xml"),
        ("content", "content.xhtml", "mathml", "content.xhtml", "application/xhtml+xml"),
        ("legal", "legal.xhtml", "", "legal.xhtml", "application/xhtml+xml"),
        ("css", "styles/reader.css", "", "styles/reader.css", "text/css"),
        ("font-regular", "fonts/NotoSerifBengali-Regular.ttf", "", "fonts/NotoSerifBengali-Regular.ttf", "font/ttf"),
        ("font-bold", "fonts/NotoSerifBengali-Bold.ttf", "", "fonts/NotoSerifBengali-Bold.ttf", "font/ttf"),
    ]
    for name, filename in FIGURE_FILENAMES.items():
        resources.append((f"image-{name.lower()}", f"images/{filename}", "", f"images/{filename}", "image/svg+xml"))
    for identifier, _, properties, href, media_type in resources:
        item = etree.SubElement(manifest, f"{{{OPF_NS}}}item")
        item.set("id", identifier)
        item.set("href", href)
        item.set("media-type", media_type)
        if properties:
            item.set("properties", properties)

    spine = etree.SubElement(package, f"{{{OPF_NS}}}spine")
    spine.set("page-progression-direction", "ltr")
    for identifier, linear in (("about", "yes"), ("content", "yes"), ("legal", "no")):
        itemref = etree.SubElement(spine, f"{{{OPF_NS}}}itemref")
        itemref.set("idref", identifier)
        itemref.set("linear", linear)

    path = destination / "OEBPS" / "package.opf"
    payload = etree.tostring(package, encoding="utf-8", xml_declaration=True, pretty_print=True)
    path.write_bytes(payload)
    return {
        "path": "OEBPS/package.opf",
        "bytes": len(payload),
        "sha256": sha256(payload),
        "manifest_items": len(resources),
        "spine_items": 3,
    }


def prepare_container(destination: Path) -> dict:
    mimetype = destination / "mimetype"
    mimetype.write_bytes(b"application/epub+zip")
    container = etree.Element(f"{{{CONTAINER_NS}}}container", nsmap={None: CONTAINER_NS})
    container.set("version", "1.0")
    rootfiles = etree.SubElement(container, f"{{{CONTAINER_NS}}}rootfiles")
    rootfile = etree.SubElement(rootfiles, f"{{{CONTAINER_NS}}}rootfile")
    rootfile.set("full-path", "OEBPS/package.opf")
    rootfile.set("media-type", "application/oebps-package+xml")
    path = destination / "META-INF" / "container.xml"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = etree.tostring(container, encoding="utf-8", xml_declaration=True, pretty_print=True)
    path.write_bytes(payload)
    return {
        "mimetype_sha256": sha256(mimetype.read_bytes()),
        "container_sha256": sha256(payload),
    }


def inventory(root: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            payload = path.read_bytes()
            records.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "bytes": len(payload),
                    "sha256": sha256(payload),
                }
            )
    return records


def tree_sha256(records: list[dict]) -> str:
    payload = json.dumps(records, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return sha256(payload)


def create_zip(unpacked: Path, epub: Path) -> dict:
    if epub.exists():
        epub.unlink()

    def zip_info(name: str, compression: int) -> zipfile.ZipInfo:
        info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
        info.compress_type = compression
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        info.flag_bits |= 0x800
        return info

    with zipfile.ZipFile(epub, "w", allowZip64=True) as archive:
        archive.writestr(zip_info("mimetype", zipfile.ZIP_STORED), b"application/epub+zip")
        for path in sorted(unpacked.rglob("*")):
            if not path.is_file() or path == unpacked / "mimetype":
                continue
            name = path.relative_to(unpacked).as_posix()
            archive.writestr(
                zip_info(name, zipfile.ZIP_DEFLATED),
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    payload = epub.read_bytes()
    with zipfile.ZipFile(epub) as archive:
        entries = archive.infolist()
        require(entries[0].filename == "mimetype", "mimetype is not the first ZIP entry")
        require(entries[0].compress_type == zipfile.ZIP_STORED, "mimetype is compressed")
        require(archive.read("mimetype") == b"application/epub+zip", "wrong mimetype payload")
        require([row.filename for row in entries[1:]] == sorted(row.filename for row in entries[1:]), "ZIP order drift")
    return {"path": epub.name, "bytes": len(payload), "sha256": sha256(payload), "entries": len(entries)}


def build_one(destination: Path, epub: Path, html_receipt: dict) -> dict:
    safe_clear(destination)
    content, headings = prepare_content(destination, html_receipt)
    about = prepare_about(destination)
    legal = prepare_license(destination)
    navigation = prepare_navigation(destination, headings)
    package = prepare_package(destination)
    container = prepare_container(destination)
    files = inventory(destination)
    archive = create_zip(destination, epub)
    return {
        "unpacked": destination.relative_to(REPO).as_posix(),
        "files": len(files),
        "bytes": sum(row["bytes"] for row in files),
        "tree_sha256": tree_sha256(files),
        "epub": archive,
        "content": content,
        "about": about,
        "license": legal,
        "navigation": navigation,
        "package": package,
        "container": container,
        "figures": html_receipt["figures"],
    }


def main() -> None:
    input_payload = INPUT_HTML.read_bytes()
    require(len(input_payload) == EXPECTED_HTML_BYTES, "sealed HTML byte count drift")
    require(sha256(input_payload) == EXPECTED_HTML_SHA256, "sealed HTML SHA-256 drift")
    html_receipt = json.loads(HTML_RECEIPT.read_text(encoding="utf-8"))
    require(html_receipt["html_sha256"] == EXPECTED_HTML_SHA256, "HTML receipt hash drift")
    require(html_receipt["mathml_expressions"] == EXPECTED_MATHML, "HTML receipt MathML drift")
    require(html_receipt["sections"] == EXPECTED_SECTIONS, "HTML receipt section drift")
    require(html_receipt["numbered_environments"] == EXPECTED_ENVIRONMENTS, "HTML receipt environment drift")
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    require(len(status["translated_units"]) == 18 and status["untranslated_units"] == 704, "release scope drift")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    canonical = build_one(CANONICAL, EPUB, html_receipt)
    cold = build_one(COLD, COLD_EPUB, html_receipt)
    require(canonical["tree_sha256"] == cold["tree_sha256"], "cold unpacked tree differs")
    require(EPUB.read_bytes() == COLD_EPUB.read_bytes(), "cold EPUB differs byte-for-byte")

    manifest = inventory(CANONICAL)
    manifest_record = {
        "schema": "openlogic-bn-epub-package-manifest/1",
        "tree_sha256": tree_sha256(manifest),
        "files": len(manifest),
        "bytes": sum(row["bytes"] for row in manifest),
        "records": manifest,
    }
    write_json(PACKAGE_MANIFEST, manifest_record)
    receipt = {
        "schema": "openlogic-bn-epub-build/1",
        "date": MODIFIED[:10],
        "status": "BUILT_DETERMINISTIC_REFLOWABLE_EPUB3_EXTERNAL_VALIDATION_PENDING",
        "release": {
            "tag": RELEASE_TAG,
            "url": RELEASE_URL,
            "scope": "Sets and Relations; 18 of 722 source units",
            "complete": False,
            "translated_units": status["translated_units"],
            "untranslated_units": status["untranslated_units"],
        },
        "input": {
            "path": "build/reader/openlogic-bn-reader.html",
            "public_url": HTML_URL,
            "bytes": len(input_payload),
            "sha256": sha256(input_payload),
            "source_revision": SOURCE_REVISION,
            "html_receipt_sha256": sha256(HTML_RECEIPT.read_bytes()),
        },
        "format": {
            "standard": "EPUB 3",
            "language": LANGUAGE,
            "page_progression": "ltr",
            "layout": "reflowable",
            "scripts": 0,
            "mathml_expressions": EXPECTED_MATHML,
            "svg_figures": EXPECTED_FIGURES,
            "numbered_environments": EXPECTED_ENVIRONMENTS,
            "sections": EXPECTED_SECTIONS,
            "first_linear_spine_item": "OEBPS/about.xhtml",
        },
        "builder": {
            "path": "tools/build_epub.py",
            "sha256": sha256(Path(__file__).read_bytes()),
            "reference_pipeline": {
                "english_builder_sha256": "eabd909079b09094d50164ef5027818f9db25415106f89e42bb9e03f4cc6f2c8",
                "english_auditor_sha256": "64ff600f8db6330bbdb142947aa52198cdb2e303149517321d02366ef17b8f0c",
            },
        },
        "canonical": canonical,
        "cold": {
            "unpacked": cold["unpacked"],
            "files": cold["files"],
            "bytes": cold["bytes"],
            "tree_sha256": cold["tree_sha256"],
            "epub": cold["epub"],
        },
        "canonical_cold_byte_identical": True,
        "package_manifest": {
            "path": "build/epub/PACKAGE_MANIFEST.json",
            "sha256": sha256(PACKAGE_MANIFEST.read_bytes()),
        },
        "font_license": {
            "name": "SIL Open Font License 1.1",
            "source_sha256": sha256(FONT_LICENSE.read_bytes()),
            "included_as": "OEBPS/legal.xhtml",
        },
    }
    write_json(BUILD_RECEIPT, receipt)
    write_json(EVIDENCE, receipt)
    print(
        json.dumps(
            {
                "epub": str(EPUB),
                "bytes": canonical["epub"]["bytes"],
                "sha256": canonical["epub"]["sha256"],
                "files": canonical["files"],
                "mathml": EXPECTED_MATHML,
                "figures": EXPECTED_FIGURES,
                "cold_identical": True,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
