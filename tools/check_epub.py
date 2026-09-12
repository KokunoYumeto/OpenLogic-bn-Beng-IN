from __future__ import annotations

import argparse
import copy
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from lxml import etree


REPO = Path(__file__).resolve().parents[1]
OUTPUT = REPO / "build" / "epub"
DEFAULT_EPUB = OUTPUT / "openlogic-bn-Beng-IN-sets-relations.epub"
COLD_EPUB = OUTPUT / "openlogic-bn-Beng-IN-sets-relations-cold.epub"
BUILD_RECEIPT = OUTPUT / "BUILD_RECEIPT.json"
PACKAGE_MANIFEST = OUTPUT / "PACKAGE_MANIFEST.json"
DEFAULT_EPUBCHECK_REPORT = OUTPUT / "EPUBCHECK.json"
DEFAULT_EVIDENCE = REPO / "evidence" / "EPUB_0_2_0_QA.json"
VISUAL_EVIDENCE = REPO / "evidence" / "EPUB_0_2_0_VISUAL_QA.json"
INPUT_HTML = REPO / "build" / "reader" / "openlogic-bn-reader.html"
HTML_RECEIPT = REPO / "build" / "reader" / "html-receipt.json"
STATUS = REPO / "evidence" / "STATUS.json"
SOURCE_MANIFEST = REPO / "evidence" / "FULL_SOURCE_MANIFEST.jsonl"

XHTML_NS = "http://www.w3.org/1999/xhtml"
MATHML_NS = "http://www.w3.org/1998/Math/MathML"
SVG_NS = "http://www.w3.org/2000/svg"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"
DC_NS = "http://purl.org/dc/elements/1.1/"
CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"
XML_NS = "http://www.w3.org/XML/1998/namespace"

LANGUAGE = "bn-Beng-IN"
EXPECTED_HTML_BYTES = 4_105_887
EXPECTED_HTML_SHA256 = "3d2c1df0ba2f8d91ddf8de832744a70f8e2ba4b179a6ea2a533fed4a273d9346"
EXPECTED_SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
EXPECTED_EPUBCHECK_VERSION = "5.3.0"
EXPECTED_EPUBCHECK_JAR_SHA256 = "f7f96617c929371821609b88c8484d6dc9f24fe916499863c46094c5fb778a65"
EXPECTED_MATHML = 909
EXPECTED_SECTIONS = 15
EXPECTED_ENVIRONMENTS = 88
EXPECTED_FIGURES = 6
EXPECTED_UNITS = [
    *(f"OLP-{number:04d}" for number in range(4, 20)),
    "OLP-0719",
    "OLP-0721",
]
FIGURE_FILENAMES = [
    "union.svg",
    "intersection.svg",
    "difference.svg",
    "graph-one.svg",
    "graph-two.svg",
    "tree.svg",
]
FONT_HASHES = {
    "NotoSerifBengali-Regular.ttf": "04935aea18655c451d05b1d4bb5bdc835226a221663f89a2ecfbcfdc4483e399",
    "NotoSerifBengali-Bold.ttf": "f752131cd292f3e0fd7a25c8fc86f5424062bc06e29f6dfadcb3c09ff4881dd0",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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
    root = OUTPUT.resolve()
    require(resolved != root and resolved.is_relative_to(root), f"unsafe audit path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


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


def element_signature(element: etree._Element) -> object:
    if not isinstance(element.tag, str):
        return ("#node", str(element.text or ""), str(element.tail or ""))
    attributes = tuple(sorted((str(name), value) for name, value in element.attrib.items()))
    children = tuple((element_signature(child), child.tail or "") for child in element)
    return (str(element.tag), attributes, element.text or "", children)


def signature_sha256(value: object) -> str:
    return sha256(json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def extract_epub(epub: Path, destination: Path) -> dict:
    safe_clear(destination)
    with zipfile.ZipFile(epub) as archive:
        infos = archive.infolist()
        require(infos, "empty EPUB archive")
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)), "duplicate ZIP entry")
        require(names[0] == "mimetype", "mimetype is not first")
        require(infos[0].compress_type == zipfile.ZIP_STORED, "mimetype is compressed")
        require(archive.read("mimetype") == b"application/epub+zip", "wrong mimetype payload")
        require(names[1:] == sorted(names[1:]), "ZIP entries are not sorted deterministically")
        for info in infos:
            name = info.filename
            pure = PurePosixPath(name)
            require(not pure.is_absolute(), f"absolute archive path: {name}")
            require(".." not in pure.parts and "\\" not in name, f"unsafe archive path: {name}")
            mode = (info.external_attr >> 16) & 0o170000
            require(mode != 0o120000, f"symbolic link in archive: {name}")
            if info.is_dir():
                continue
            target = destination / Path(*pure.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))
    return {
        "entries": len(infos),
        "mimetype_first": True,
        "mimetype_stored": True,
        "deterministic_order": True,
        "safe_paths": True,
    }


def normalize_source_body() -> etree._Element:
    source_root = parse_xml(INPUT_HTML).getroot()
    namespace = {"x": XHTML_NS}
    body = copy.deepcopy(source_root.xpath("/x:html/x:body", namespaces=namespace)[0])
    headings = body.xpath(".//x:h1 | .//x:h2", namespaces=namespace)
    require(headings, "source headings missing")
    headings[0].set("id", "book-title")
    images = body.xpath(".//x:img", namespaces=namespace)
    require(len(images) == len(FIGURE_FILENAMES), "source figure count drift")
    for image, filename in zip(images, FIGURE_FILENAMES, strict=True):
        image.set("src", f"images/{filename}")
    return body


def validate_content(unpacked: Path, html_receipt: dict) -> dict:
    content = parse_xml(unpacked / "OEBPS" / "content.xhtml").getroot()
    namespace = {"x": XHTML_NS, "m": MATHML_NS}
    require(content.tag == f"{{{XHTML_NS}}}html", "content is not XHTML")
    require(content.get("lang") == LANGUAGE, "content lang drift")
    require(content.get(f"{{{XML_NS}}}lang") == LANGUAGE, "content xml:lang drift")
    require(content.get("dir") == "ltr", "content direction drift")
    body = content.xpath("/x:html/x:body", namespaces=namespace)[0]
    expected_body = normalize_source_body()
    expected_signature = element_signature(expected_body)
    actual_signature = element_signature(body)
    require(actual_signature == expected_signature, "EPUB content body differs from the sealed semantic HTML")

    source_root = parse_xml(INPUT_HTML).getroot()
    source_math = source_root.xpath("//m:math", namespaces=namespace)
    packaged_math = content.xpath("//m:math", namespaces=namespace)
    source_math_signatures = [element_signature(node) for node in source_math]
    packaged_math_signatures = [element_signature(node) for node in packaged_math]
    require(len(packaged_math) == len(source_math) == EXPECTED_MATHML, "native MathML count drift")
    require(packaged_math_signatures == source_math_signatures, "MathML structure or content drift")
    annotations = content.xpath(
        '//m:math/m:semantics/m:annotation[@encoding="application/x-tex"]',
        namespaces=namespace,
    )
    require(len(annotations) == EXPECTED_MATHML, "MathML TeX annotation coverage drift")

    headings = content.xpath("//x:h1 | //x:h2", namespaces=namespace)
    sections = content.xpath("//x:h2", namespaces=namespace)
    environments = sum(
        len(
            content.xpath(
                f'//x:div[contains(concat(" ", normalize-space(@class), " "), " {name} ")]',
                namespaces=namespace,
            )
        )
        for name in ("defn", "ex", "prop", "thm", "prob")
    )
    require(len(sections) == html_receipt["sections"] == EXPECTED_SECTIONS, "section coverage drift")
    require(environments == html_receipt["numbered_environments"] == EXPECTED_ENVIRONMENTS, "environment coverage drift")

    images = content.xpath("//x:img", namespaces=namespace)
    require(len(images) == EXPECTED_FIGURES, "image count drift")
    require(all((image.get("alt") or "").strip() for image in images), "empty image alternative text")
    require(not content.xpath("//x:script", namespaces=namespace), "script found in content")
    ids = [element.get("id") for element in content.xpath("//*[@id]")]
    require(len(ids) == len(set(ids)), "duplicate content IDs")

    return {
        "source_body_semantic_signature_sha256": signature_sha256(expected_signature),
        "packaged_body_semantic_signature_sha256": signature_sha256(actual_signature),
        "body_semantically_identical": True,
        "mathml_expressions": len(packaged_math),
        "mathml_semantically_identical": True,
        "mathml_tex_annotations": len(annotations),
        "h1_h2_headings": len(headings),
        "sections": len(sections),
        "numbered_environments": environments,
        "svg_images": len(images),
        "svg_images_with_nonempty_alt": len(images),
        "scripts": 0,
    }


def resolve_local(base: PurePosixPath, reference: str) -> tuple[PurePosixPath, str]:
    parsed = urlsplit(reference)
    path = unquote(parsed.path)
    target = PurePosixPath(posixpath.normpath((base.parent / path).as_posix())) if path else base
    return target, unquote(parsed.fragment)


def validate_links(unpacked: Path) -> dict:
    xhtml_paths = sorted((unpacked / "OEBPS").glob("*.xhtml"))
    roots: dict[PurePosixPath, etree._Element] = {}
    ids: dict[PurePosixPath, set[str]] = {}
    for path in xhtml_paths:
        relative = PurePosixPath(path.relative_to(unpacked).as_posix())
        root = parse_xml(path).getroot()
        roots[relative] = root
        values = [element.get("id") for element in root.xpath("//*[@id]")]
        require(len(values) == len(set(values)), f"duplicate IDs in {relative}")
        ids[relative] = set(values)

    checked = 0
    external = 0
    fragments = 0
    for base, root in roots.items():
        for element in root.xpath("//*[@href or @src]"):
            for attribute in ("href", "src"):
                reference = element.get(attribute)
                if not reference:
                    continue
                parsed = urlsplit(reference)
                require(parsed.scheme != "data", f"data URI remains in {base}: {reference[:40]}")
                if parsed.scheme:
                    require(parsed.scheme in {"http", "https"}, f"unsupported URI scheme in {base}: {parsed.scheme}")
                    external += 1
                    continue
                target, fragment = resolve_local(base, reference)
                physical = unpacked / Path(*target.parts)
                require(physical.is_file(), f"missing linked resource: {base} -> {target}")
                if fragment:
                    require(target in ids, f"fragment target is not XHTML: {target}#{fragment}")
                    require(fragment in ids[target], f"missing fragment: {target}#{fragment}")
                    fragments += 1
                checked += 1

    css_path = unpacked / "OEBPS" / "styles" / "reader.css"
    css = css_path.read_text(encoding="utf-8")
    css_references = []
    for match in re.finditer(r"url\(([^)]+)\)", css):
        reference = match.group(1).strip().strip("\"'")
        require(not reference.startswith("data:"), "data URI remains in CSS")
        target, _ = resolve_local(PurePosixPath("OEBPS/styles/reader.css"), reference)
        require((unpacked / Path(*target.parts)).is_file(), f"missing CSS resource: {target}")
        css_references.append(target.as_posix())
    require(len(css_references) == 2, "embedded font reference count drift")
    require("position:fixed" not in re.sub(r"\s+", "", css).lower(), "fixed-position CSS found")
    return {
        "local_resource_links_checked": checked,
        "fragment_links_checked": fragments,
        "external_http_links": external,
        "css_resource_links_checked": len(css_references),
        "broken_links": [],
        "data_uris_remaining": 0,
        "fixed_position_css": 0,
    }


def validate_package(unpacked: Path, package_manifest: dict) -> dict:
    container = parse_xml(unpacked / "META-INF" / "container.xml").getroot()
    rootfiles = container.xpath("//c:rootfile", namespaces={"c": CONTAINER_NS})
    require(len(rootfiles) == 1, "container rootfile count drift")
    require(rootfiles[0].get("full-path") == "OEBPS/package.opf", "container package path drift")
    package = parse_xml(unpacked / "OEBPS" / "package.opf").getroot()
    namespace = {"opf": OPF_NS, "dc": DC_NS}
    require(package.get("version") == "3.0", "package EPUB version drift")
    require(package.get(f"{{{XML_NS}}}lang") == LANGUAGE, "package language drift")
    require(package.get("unique-identifier") == "pub-id", "package identifier pointer drift")
    languages = package.xpath("/opf:package/opf:metadata/dc:language/text()", namespaces=namespace)
    require(languages == [LANGUAGE], "dc:language drift")
    layout = package.xpath(
        '/opf:package/opf:metadata/opf:meta[@property="rendition:layout"]/text()',
        namespaces=namespace,
    )
    require(layout == ["reflowable"], "rendition layout is not reflowable")
    description = package.xpath("/opf:package/opf:metadata/dc:description/text()", namespaces=namespace)
    require(description and "18 of 722" in description[0] and "704" in description[0], "partial scope missing from metadata")

    items = package.xpath("/opf:package/opf:manifest/opf:item", namespaces=namespace)
    item_ids = [item.get("id") for item in items]
    require(len(item_ids) == len(set(item_ids)), "duplicate manifest item IDs")
    href_by_id = {item.get("id"): PurePosixPath("OEBPS") / PurePosixPath(item.get("href")) for item in items}
    for target in href_by_id.values():
        require((unpacked / Path(*target.parts)).is_file(), f"manifest resource missing: {target}")
    package_files = {
        PurePosixPath(row["path"])
        for row in package_manifest["records"]
        if row["path"] not in {"mimetype", "META-INF/container.xml", "OEBPS/package.opf"}
    }
    require(set(href_by_id.values()) == package_files, "manifest coverage differs from package inventory")
    content_items = [item for item in items if item.get("href") == "content.xhtml"]
    require(len(content_items) == 1 and "mathml" in (content_items[0].get("properties") or "").split(), "MathML manifest property missing")
    nav_items = [item for item in items if "nav" in (item.get("properties") or "").split()]
    require(len(nav_items) == 1 and nav_items[0].get("href") == "nav.xhtml", "navigation manifest property drift")

    spine = package.xpath("/opf:package/opf:spine/opf:itemref", namespaces=namespace)
    linear = [href_by_id[item.get("idref")] for item in spine if item.get("linear", "yes") != "no"]
    require(linear and linear[0] == PurePosixPath("OEBPS/about.xhtml"), "about page is not first linear spine item")
    require(linear == [PurePosixPath("OEBPS/about.xhtml"), PurePosixPath("OEBPS/content.xhtml")], "linear reading order drift")

    nav = parse_xml(unpacked / "OEBPS" / "nav.xhtml").getroot()
    nav_namespace = {"x": XHTML_NS, "epub": EPUB_NS}
    toc = nav.xpath('//x:nav[@epub:type="toc"]', namespaces=nav_namespace)
    require(len(toc) == 1, "EPUB navigation TOC missing")
    toc_links = toc[0].xpath(".//x:a", namespaces=nav_namespace)
    require(len(toc_links) == 20, "TOC coverage drift")
    landmarks = nav.xpath('//x:nav[@epub:type="landmarks"]//x:a', namespaces=nav_namespace)
    require(len(landmarks) == 3, "landmark coverage drift")

    about = parse_xml(unpacked / "OEBPS" / "about.xhtml").getroot()
    about_text = " ".join("".join(about.itertext()).split())
    require("৭২২টি উৎস ফাইলের মধ্যে ১৮টি" in about_text, "Bengali partial scope missing")
    require("৭০৪টি ফাইল এখনও অনূদিত নয়" in about_text, "Bengali remaining scope missing")
    require("18 of 722 source units" in about_text, "English partial scope note missing")
    require("704 units remain untranslated" in about_text, "English remaining scope note missing")

    return {
        "epub_package_version": package.get("version"),
        "language": languages[0],
        "layout": layout[0],
        "manifest_items": len(items),
        "manifest_covers_all_publication_resources": True,
        "spine_items": len(spine),
        "linear_spine": [path.as_posix() for path in linear],
        "toc_links": len(toc_links),
        "landmarks": len(landmarks),
        "partial_scope_in_bengali_and_english": True,
    }


def validate_binary_resources(unpacked: Path, html_receipt: dict) -> dict:
    figures = []
    for filename, receipt in zip(FIGURE_FILENAMES, html_receipt["figures"], strict=True):
        path = unpacked / "OEBPS" / "images" / filename
        payload = path.read_bytes()
        digest = sha256(payload)
        require(digest == receipt["svg_sha256"], f"SVG hash drift: {filename}")
        root = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True))
        require(root.tag == f"{{{SVG_NS}}}svg", f"resource is not native SVG: {filename}")
        figures.append({"filename": filename, "bytes": len(payload), "sha256": digest})
    fonts = []
    for filename, expected in FONT_HASHES.items():
        path = unpacked / "OEBPS" / "fonts" / filename
        digest = sha256(path.read_bytes())
        require(digest == expected, f"font hash drift: {filename}")
        fonts.append({"filename": filename, "bytes": path.stat().st_size, "sha256": digest})
    legal = parse_xml(unpacked / "OEBPS" / "legal.xhtml").getroot()
    legal_text = " ".join("".join(legal.itertext()).split())
    require("SIL OPEN FONT LICENSE Version 1.1" in legal_text, "font license text missing")
    return {"svg_figures": figures, "fonts": fonts, "font_license_included": True}


def validate_source_coverage() -> dict:
    status = load_json(STATUS)
    require(status["release_scope"] == "Sets and Relations; 18 of 722 source files", "release status scope drift")
    require(status["complete"] is False, "partial release incorrectly marked complete")
    require(status["translated_units"] == EXPECTED_UNITS, "release unit roster drift")
    require(status["untranslated_units"] == 704, "remaining unit count drift")
    require(len(status["unit_checks"]) == 18, "unit check coverage drift")
    require(all(row["unit_id"] in EXPECTED_UNITS for row in status["unit_checks"]), "unexpected unit check")
    require(all(row["math_parity"] and row["controls_parity"] and row["env_parity"] for row in status["unit_checks"]), "source parity failure")
    manifest = [json.loads(line) for line in SOURCE_MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip()]
    require(len(manifest) == 722, "full source manifest count drift")
    require(len({row["unit_id"] for row in manifest}) == 722, "duplicate full source manifest units")
    require(all(row["source_commit"] == EXPECTED_SOURCE_REVISION for row in manifest), "source revision drift")
    input_payload = INPUT_HTML.read_bytes()
    require(len(input_payload) == EXPECTED_HTML_BYTES, "sealed HTML byte count drift")
    require(sha256(input_payload) == EXPECTED_HTML_SHA256, "sealed HTML hash drift")
    return {
        "full_source_manifest_units": len(manifest),
        "included_units": EXPECTED_UNITS,
        "included_unit_count": len(EXPECTED_UNITS),
        "untranslated_unit_count": status["untranslated_units"],
        "complete": status["complete"],
        "unit_parity_checks_passed": len(status["unit_checks"]),
        "sealed_html_bytes": len(input_payload),
        "sealed_html_sha256": sha256(input_payload),
        "source_revision": EXPECTED_SOURCE_REVISION,
    }


def run_epubcheck(epub: Path, jar: Path, report: Path) -> dict:
    require(jar.is_file(), f"EPUBCheck jar not found: {jar}")
    jar_digest = sha256(jar.read_bytes())
    require(jar_digest == EXPECTED_EPUBCHECK_JAR_SHA256, "EPUBCheck distribution hash drift")
    if report.exists():
        report.unlink()
    completed = subprocess.run(
        ["java", "-jar", str(jar), str(epub), "--json", str(report), "--failonwarnings"],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    require(report.is_file(), "EPUBCheck did not create its JSON report")
    result = load_json(report)
    checker = result.get("checker", {})
    require(checker.get("checkerVersion") == EXPECTED_EPUBCHECK_VERSION, "EPUBCheck version drift")
    require(completed.returncode == 0, f"EPUBCheck failed: {completed.stdout}\n{completed.stderr}")
    require(not result.get("messages"), "EPUBCheck emitted messages")
    require(
        all(checker.get(key) == 0 for key in ("nFatal", "nError", "nWarning", "nUsage")),
        "EPUBCheck severity counts are nonzero",
    )
    return {
        "version": checker["checkerVersion"],
        "jar_sha256": jar_digest,
        "exit_code": completed.returncode,
        "fatal": checker["nFatal"],
        "errors": checker["nError"],
        "warnings": checker["nWarning"],
        "usage": checker["nUsage"],
        "messages": len(result["messages"]),
        "report": report.relative_to(REPO).as_posix() if report.is_relative_to(REPO) else report.name,
        "report_sha256": sha256(report.read_bytes()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit the partial Bengali reflowable EPUB3 release artifact.")
    parser.add_argument("--epub", type=Path, default=DEFAULT_EPUB)
    parser.add_argument("--epubcheck-jar", type=Path, required=True)
    parser.add_argument("--epubcheck-report", type=Path, default=DEFAULT_EPUBCHECK_REPORT)
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    epub = args.epub.resolve()
    require(epub.is_file(), f"EPUB not found: {epub}")
    build = load_json(BUILD_RECEIPT)
    package_manifest = load_json(PACKAGE_MANIFEST)
    html_receipt = load_json(HTML_RECEIPT)
    epub_payload = epub.read_bytes()
    expected_epub = build["canonical"]["epub"]
    require(len(epub_payload) == expected_epub["bytes"], "EPUB byte count differs from build receipt")
    require(sha256(epub_payload) == expected_epub["sha256"], "EPUB hash differs from build receipt")
    require(build["canonical_cold_byte_identical"] is True, "cold-build identity is not recorded")
    require(DEFAULT_EPUB.read_bytes() == COLD_EPUB.read_bytes(), "local canonical and cold EPUBs differ")

    audit_root = OUTPUT / "audit-unpacked"
    archive = extract_epub(epub, audit_root)
    extracted_inventory = inventory(audit_root)
    require(extracted_inventory == package_manifest["records"], "archive inventory differs from package manifest")
    require(tree_sha256(extracted_inventory) == package_manifest["tree_sha256"], "archive tree digest drift")
    package = validate_package(audit_root, package_manifest)
    content = validate_content(audit_root, html_receipt)
    links = validate_links(audit_root)
    binary = validate_binary_resources(audit_root, html_receipt)
    coverage = validate_source_coverage()
    epubcheck = run_epubcheck(epub, args.epubcheck_jar.resolve(), args.epubcheck_report.resolve())

    visual = {
        "status": "PENDING_SEPARATE_SILENT_BROWSER_INSPECTION",
        "claim": "No visual result is claimed by this automated audit.",
    }
    final_status = "PASS_STRUCTURAL_CONTENT_MATH_LINK_EPUBCHECK_VISUAL_PENDING"
    if VISUAL_EVIDENCE.is_file():
        visual_evidence = load_json(VISUAL_EVIDENCE)
        require(visual_evidence["status"] == "PASS_REPRESENTATIVE_SILENT_RENDERING", "visual evidence is not a pass")
        require(visual_evidence["epub"]["sha256"] == sha256(epub_payload), "visual evidence belongs to another EPUB")
        capture_receipt = REPO / visual_evidence["method"]["capture_receipt"]["path"]
        require(capture_receipt.is_file(), "visual capture receipt missing")
        require(
            sha256(capture_receipt.read_bytes()) == visual_evidence["method"]["capture_receipt"]["sha256"],
            "visual capture receipt hash drift",
        )
        visual = {
            "status": visual_evidence["status"],
            "evidence": "evidence/EPUB_0_2_0_VISUAL_QA.json",
            "evidence_sha256": sha256(VISUAL_EVIDENCE.read_bytes()),
            "samples_inspected": visual_evidence["summary"]["samples_inspected"],
            "visible_clipping_or_overlap": visual_evidence["summary"]["visible_clipping_or_overlap"],
            "limitations": visual_evidence["limitations"],
        }
        final_status = "PASS_ALL_REQUIRED_CHECKS"

    evidence = {
        "schema": "openlogic-bn-epub-qa/1",
        "date": "2026-09-13",
        "status": final_status,
        "epub": {
            "filename": epub.name,
            "bytes": len(epub_payload),
            "sha256": sha256(epub_payload),
        },
        "build_receipt": {
            "path": "build/epub/BUILD_RECEIPT.json",
            "sha256": sha256(BUILD_RECEIPT.read_bytes()),
            "canonical_cold_byte_identical": True,
        },
        "archive": archive,
        "package": package,
        "source_coverage": coverage,
        "content_equivalence": content,
        "links": links,
        "binary_resources": binary,
        "epubcheck": epubcheck,
        "visual_rendering": visual,
        "checker": {"path": "tools/check_epub.py", "sha256": sha256(Path(__file__).read_bytes())},
    }
    write_json(args.evidence.resolve(), evidence)
    print(
        json.dumps(
            {
                "status": evidence["status"],
                "epub": evidence["epub"],
                "epubcheck": epubcheck,
                "source_units": coverage["included_unit_count"],
                "mathml": content["mathml_expressions"],
                "links_checked": links["local_resource_links_checked"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
