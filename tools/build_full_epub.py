"""Package the verified 722-unit semantic XHTML as a deterministic EPUB3.

This uses the same content and native MathML as the full HTML reader. No TeX
process is invoked, and the historical 299-unit EPUB remains untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from lxml import etree

import build_cumulative_semantic_reader as reader


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build/full-edition"
SOURCE = BUILD / "content-for-epub.html"
UNPACKED = BUILD / "epub-unpacked"
EPUB = BUILD / "openlogic-bn-Beng-IN-complete.epub"
FONT_INFO = BUILD / "OPERATOR_FONT.json"
FONT_DIR = UNPACKED / "OEBPS/fonts"
CSS_PATH = UNPACKED / "OEBPS/styles/reader.css"
QA_PATH = BUILD / "SEMANTIC_READER_QA.json"
RECEIPT_PATH = BUILD / "EPUB_QA.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def page(title: str, paragraphs: list[str], extra: list[tuple[str, str]] = ()) -> dict:
    root, body = reader.xhtml_shell(title)
    main = etree.SubElement(body, f"{{{reader.XHTML_NS}}}main")
    heading = etree.SubElement(main, f"{{{reader.XHTML_NS}}}h1")
    heading.text = title
    for value in paragraphs:
        node = etree.SubElement(main, f"{{{reader.XHTML_NS}}}p")
        node.text = value
    for tag, value in extra:
        node = etree.SubElement(main, f"{{{reader.XHTML_NS}}}{tag}")
        node.text = value
    filename = "about.xhtml" if title == "এই সংস্করণ সম্পর্কে" else "legal.xhtml"
    path = UNPACKED / "OEBPS" / filename
    reader.serialize_xml(root, path)
    return {"path": "OEBPS/" + filename, "bytes": path.stat().st_size, "sha256": digest(path)}


def configure_reader(markers: list[str]) -> None:
    reader.BUILD = BUILD
    reader.UNPACKED = UNPACKED
    reader.EPUB_OUTPUT = EPUB
    reader.EXPECTED_UNITS = markers
    reader.FIXED_ZIP_TIME = (2026, 9, 28, 0, 0, 0)


def prepare_fonts_and_css(source_root: etree._Element, font_info: dict) -> list[dict]:
    styles = source_root.xpath("/*[local-name()='html']/*[local-name()='head']/*[local-name()='style']")
    require(len(styles) == 2, "full reader CSS/operator style count changed")
    css = "\n".join(node.text or "" for node in styles)
    names = re.findall(r"url\(['\"]([^'\"]+\.ttf)['\"]\)", css)
    expected = [reader.FONT_REGULAR.name, reader.FONT_BOLD.name,
                "OpenLogicReaderStMaryOperators.ttf", "OpenLogicReaderTXOperators.ttf"]
    require(sorted(names) == sorted(expected), "EPUB font references changed")
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    CSS_PATH.parent.mkdir(parents=True, exist_ok=True)
    operator_hashes = {row["file"]: row["sha256"] for row in font_info["ttf_fonts"]}
    receipts = []
    for name in expected:
        source = REPO / "fonts" / name if name.startswith("Noto") else BUILD / name
        require(source.is_file(), "missing font: " + name)
        if name in operator_hashes:
            require(digest(source) == operator_hashes[name], "operator font drift: " + name)
        elif name in reader.FONT_HASHES:
            require(digest(source) == reader.FONT_HASHES[name], "Bengali font drift: " + name)
        target = FONT_DIR / name
        shutil.copy2(source, target)
        receipts.append({"filename": name, "bytes": target.stat().st_size, "sha256": digest(target)})
    for name in expected:
        css = css.replace("url('" + name + "')", "url('../fonts/" + name + "')")
    require(not re.search(r"url\(['\"](?!\.\./fonts/)", css), "unexpected CSS URL")
    CSS_PATH.write_text(css + "\n", encoding="utf-8", newline="\n")
    return receipts


def update_package(html_sha: str, fonts: list[dict]) -> dict:
    reader.prepare_package(html_sha)
    path = UNPACKED / "OEBPS/package.opf"
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    root = etree.parse(str(path), parser)
    ns = {"opf": reader.OPF_NS, "dc": reader.DC_NS}

    def set_dc(name: str, value: str) -> None:
        nodes = root.xpath("//dc:" + name, namespaces=ns)
        require(len(nodes) == 1, "unexpected EPUB metadata: " + name)
        nodes[0].text = value

    set_dc("identifier", "urn:sha256:" + html_sha + ":epub3-722")
    set_dc("title", "ওপেন লজিক: সম্পূর্ণ ভারতীয় বাংলা সংস্করণ")
    set_dc("description", "হিমায়িত Open Logic মূলের সব ৭২২টি বিষয়বস্তু-এককের ভারতীয় বাংলা, পুনঃপ্রবাহযোগ্য MathML EPUB3 পাঠ।")
    set_dc("date", "2026-09-28")
    set_dc("rights", "CC BY 4.0; Noto fonts OFL 1.1; TX Fonts and St Mary's Road operator-font notices are in the legal page.")
    for prop, value in (
        ("dcterms:modified", "2026-09-28T00:00:00Z"),
        ("schema:accessibilitySummary", "Complete reflowable Bengali text with native MathML, structural navigation and textual proof-tree, tableau and diagram representations; script-free."),
    ):
        nodes = root.xpath("//opf:meta[@property=$property]", namespaces=ns, property=prop)
        require(len(nodes) == 1, "unexpected EPUB meta: " + prop)
        nodes[0].text = value
    manifest = root.xpath("//opf:manifest", namespaces=ns)[0]
    for row in fonts:
        if row["filename"].startswith("Noto"):
            continue
        item = etree.SubElement(manifest, f"{{{reader.OPF_NS}}}item")
        item.set("id", "font-" + row["filename"].removesuffix(".ttf").lower())
        item.set("href", "fonts/" + row["filename"])
        item.set("media-type", "font/ttf")
    reader.serialize_xml(root.getroot(), path)
    return {"path": "OEBPS/package.opf", "bytes": path.stat().st_size,
            "sha256": digest(path), "manifest_items": len(manifest)}


def repair_math_text_links(content: dict) -> tuple[dict, int]:
    """Give HTML links in MathML text the XHTML namespace EPUB requires."""
    path = UNPACKED / "OEBPS/content.xhtml"
    parser = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True)
    document = etree.parse(str(path), parser)
    ns = {"m": reader.MATHML_NS}
    anchors = document.xpath("//m:math//m:a", namespaces=ns)
    require(anchors, "expected MathML cross-reference links are missing")
    for anchor in anchors:
        require(etree.QName(anchor.getparent()).localname == "mtext", "unexpected MathML anchor parent")
        anchor.tag = f"{{{reader.XHTML_NS}}}a"
    reader.serialize_xml(document.getroot(), path)
    return content | {"bytes": path.stat().st_size, "sha256": digest(path)}, len(anchors)


def main() -> None:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--epubcheck-jar", type=Path)
    args = args_parser.parse_args()
    qa = json.loads(QA_PATH.read_text(encoding="utf-8"))
    require(qa["source_units"] == qa["html"]["unit_markers"] == 722, "full HTML scope drift")
    require(digest(SOURCE) == qa["html"]["epub_source_sha256"], "EPUB source drift")
    require(qa["html"]["broken_internal_links"] == 0, "broken HTML link")
    font_info = json.loads(FONT_INFO.read_text(encoding="utf-8"))
    parser = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True)
    source_root = etree.parse(str(SOURCE), parser).getroot()
    markers = source_root.xpath("//*[contains(concat(' ',normalize-space(@class),' '),' unit-marker ')]/@data-source-unit")
    require(len(markers) == len(set(markers)) == 722, "duplicate/missing EPUB source marker")
    require(set(markers) == {f"OLP-{number:04d}" for number in range(1, 723)}, "EPUB source scope drift")
    configure_reader(markers)
    reader.safe_clear(UNPACKED)
    fonts = prepare_fonts_and_css(source_root, font_info)
    toc, content = reader.prepare_content(SOURCE)
    content, repaired_math_links = repair_math_text_links(content)
    require(content["mathml"] == qa["html"]["native_mathml"], "EPUB MathML count drift")
    about = page("এই সংস্করণ সম্পর্কে", [
        "এটি হিমায়িত Open Logic মূলের সব ৭২২টি বিষয়বস্তু-এককের ভারতীয় বাংলা EPUB3 পাঠ।",
        "গাণিতিক সূত্রগুলি নেটিভ MathML; প্রমাণবৃক্ষ, ট্যাবলো ও চিত্রগুলির অর্থবহ পুনঃপ্রবাহযোগ্য পাঠ্যরূপ আছে। প্যাকেজে কোনো স্ক্রিপ্ট, অডিও বা স্থির-পৃষ্ঠার বিন্যাস নেই।",
        "মূল OpenLogicProject/OpenLogic revision: " + reader.SOURCE_REVISION + ".",
    ])
    tx_notice = (BUILD / "font-sources/TXFONTS-COPYRIGHT.txt").read_text(encoding="ascii")
    legal = page("লাইসেন্স", [
        "Open Logic Project এবং এই বাংলা অনুবাদ Creative Commons Attribution 4.0 International (CC BY 4.0) লাইসেন্সে প্রকাশিত।",
        "বাংলা Noto ফন্ট SIL Open Font License 1.1-এর অধীনে।",
        "বিশেষ গাণিতিক রেখার TX Fonts-এর মূল স্বত্ব ও দলিল নিচে দেওয়া হয়েছে; নথিভুক্ত এমবেডিং ব্যতিক্রম প্রযোজ্য।",
        "St Mary's Road ফন্টের স্বত্ব Jeremy Gibbons ও Alan Jeffrey-এর; এর শর্ত LPPL 1.0 বা পরবর্তী সংস্করণ। মূল দলিল: https://tug.ctan.org/fonts/stmaryrd/stmaryrd.pdf",
    ], [("pre", reader.FONT_LICENSE.read_text(encoding="utf-8")), ("pre", tx_notice)])
    parts = {"container": reader.prepare_container(), "about": about, "content": content,
             "legal": legal, "nav": reader.prepare_nav(toc),
             "package": update_package(qa["html"]["html_sha256"], fonts)}
    canonical = reader.create_epub(EPUB)
    cold = BUILD / "cold-full.epub"
    reader.create_epub(cold)
    require(EPUB.read_bytes() == cold.read_bytes(), "full EPUB cold build differs")
    cold.unlink()
    validation = reader.validate_epub(EPUB, qa["html"])
    check = None
    if args.epubcheck_jar:
        check = reader.run_epubcheck(EPUB, args.epubcheck_jar.resolve())
    receipt = {"schema": "openlogic-bn-full-epub/1", "status": "passed" if check else "structural_pass_epubcheck_pending",
               "source_units": 722, "source_revision": reader.SOURCE_REVISION,
               "html_sha256": qa["html"]["html_sha256"], "native_mathml": content["mathml"],
               "epub": canonical, "parts": parts, "fonts": fonts, "validation": validation,
               "math_text_links_in_xhtml_namespace": repaired_math_links,
               "epubcheck": check, "deterministic_cold_build": True,
               "method": "Full semantic reader XHTML packaged directly; no TeX process."}
    RECEIPT_PATH.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": receipt["status"], "units": 722, "mathml": content["mathml"],
                      "epub_bytes": canonical["bytes"], "epub_sha256": canonical["sha256"],
                      "epubcheck_messages": check["messages"] if check else None}))


if __name__ == "__main__":
    main()
