from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from lxml import etree
import win32api


REPO = Path(__file__).resolve().parents[1]
UNPACKED = REPO / "build" / "epub" / "audit-unpacked" / "OEBPS"
OUTPUT = REPO / "build" / "epub" / "visual"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
XML_NS = "http://www.w3.org/XML/1998/namespace"
LANGUAGE = "bn-Beng-IN"
CHROME_CANDIDATES = (
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_clear(path: Path) -> None:
    resolved = path.resolve()
    root = (REPO / "build" / "epub").resolve()
    require(resolved != root and resolved.is_relative_to(root), f"unsafe visual path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def parse(path: Path) -> etree._ElementTree:
    return etree.parse(
        str(path),
        etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True),
    )


def make_shell(title: str) -> tuple[etree._Element, etree._Element]:
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
    title_element = etree.SubElement(head, f"{{{XHTML_NS}}}title")
    title_element.text = title
    link = etree.SubElement(head, f"{{{XHTML_NS}}}link")
    link.set("rel", "stylesheet")
    link.set("type", "text/css")
    link.set("href", "styles/reader.css")
    body = etree.SubElement(root, f"{{{XHTML_NS}}}body")
    main = etree.SubElement(body, f"{{{XHTML_NS}}}main")
    main.set("id", "representative-slice")
    return root, main


def slice_document(content_root: etree._Element, target_id: str, count: int, destination: Path) -> dict:
    target = content_root.xpath(f'//*[@id="{target_id}"]')
    require(len(target) == 1, f"representative anchor missing: {target_id}")
    heading = target[0]
    parent = heading.getparent()
    index = parent.index(heading)
    selected = list(parent)[index : index + count]
    require(selected and selected[0] is heading, f"representative selection failed: {target_id}")
    title = " ".join("".join(heading.itertext()).split())
    root, main = make_shell(title)
    for element in selected:
        main.append(copy.deepcopy(element))
    payload = etree.tostring(root, encoding="utf-8", xml_declaration=True, method="xml")
    destination.write_bytes(payload)
    return {
        "path": destination.relative_to(REPO).as_posix(),
        "bytes": len(payload),
        "sha256": sha256(payload),
        "source_anchor": target_id,
        "source_sibling_count": count,
        "source_subtree_signatures": [
            sha256(etree.tostring(element, encoding="utf-8", with_tail=False)) for element in selected
        ],
    }


def capture(browser: Path, source: Path, screenshot: Path, size: str, profile: Path) -> dict:
    command = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-first-run",
        "--disable-extensions",
        "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        f"--user-data-dir={profile}",
        f"--window-size={size}",
        f"--screenshot={screenshot}",
        source.resolve().as_uri(),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    require(completed.returncode == 0, f"headless browser failed: {completed.stdout}\n{completed.stderr}")
    require(screenshot.is_file() and screenshot.stat().st_size > 1_000, f"screenshot missing: {screenshot}")
    return {
        "path": screenshot.relative_to(REPO).as_posix(),
        "bytes": screenshot.stat().st_size,
        "sha256": sha256(screenshot.read_bytes()),
        "viewport": size,
        "source": source.relative_to(REPO).as_posix(),
    }


def main() -> None:
    require((UNPACKED / "content.xhtml").is_file(), "run the EPUB audit before rendering")
    browser = next((path for path in CHROME_CANDIDATES if path.is_file()), None)
    require(browser is not None, "no supported installed Chromium browser found")
    safe_clear(OUTPUT)
    (OUTPUT / "styles").mkdir()
    (OUTPUT / "images").mkdir()
    shutil.copy2(UNPACKED / "styles" / "reader.css", OUTPUT / "styles" / "reader.css")
    for path in sorted((UNPACKED / "images").glob("*.svg")):
        shutil.copy2(path, OUTPUT / "images" / path.name)
    content_root = parse(UNPACKED / "content.xhtml").getroot()
    slices = {
        "set_math_diagram": slice_document(content_root, "sfr:set:uni:sec", 5, OUTPUT / "set-math-diagram.xhtml"),
        "relation_graph": slice_document(content_root, "sfr:rel:grp:sec", 6, OUTPUT / "relation-graph.xhtml"),
        "relation_order_narrow": slice_document(content_root, "sfr:rel:ord:sec", 7, OUTPUT / "relation-order-narrow.xhtml"),
    }
    samples = [
        ("about", UNPACKED / "about.xhtml", "1200,1000"),
        ("navigation", UNPACKED / "nav.xhtml", "1200,1000"),
        ("content_opening", UNPACKED / "content.xhtml", "1200,1000"),
        ("set_math_diagram", OUTPUT / "set-math-diagram.xhtml", "1200,1000"),
        ("relation_graph", OUTPUT / "relation-graph.xhtml", "1200,1400"),
        ("relation_order_narrow", OUTPUT / "relation-order-narrow.xhtml", "500,900"),
    ]
    screenshots = {}
    for name, source, size in samples:
        screenshots[name] = capture(
            browser,
            source,
            OUTPUT / f"{name}.png",
            size,
            OUTPUT / "profiles" / name,
        )
    version_info = win32api.GetFileVersionInfo(str(browser), "\\")
    version = ".".join(
        str(value)
        for value in (
            version_info["FileVersionMS"] >> 16,
            version_info["FileVersionMS"] & 0xFFFF,
            version_info["FileVersionLS"] >> 16,
            version_info["FileVersionLS"] & 0xFFFF,
        )
    )
    receipt = {
        "schema": "openlogic-bn-epub-visual-capture/1",
        "date": "2026-09-13",
        "status": "CAPTURED_FOR_HUMAN_VISUAL_INSPECTION",
        "method": (
            "Silent headless Chromium screenshots of the unpacked EPUB pages plus three bounded XHTML "
            "slices copied from exact content.xhtml sibling subtrees with the package CSS and SVG resources."
        ),
        "browser": {"path": str(browser), "version": version, "sha256": sha256(browser.read_bytes())},
        "slices": slices,
        "screenshots": screenshots,
        "assistive_technology_used": False,
        "audio_created": False,
    }
    receipt_path = OUTPUT / "VISUAL_CAPTURE.json"
    receipt_path.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"receipt": str(receipt_path), "screenshots": len(screenshots)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
