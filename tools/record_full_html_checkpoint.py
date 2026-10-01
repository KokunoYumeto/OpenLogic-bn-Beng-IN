"""Record the audited local full-HTML/source-archive checkpoint without claiming PDF completion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from lxml import html as html_parser


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build/full-edition"
DIST = REPO / "dist"
STATE = Path(r"C:\interlanguage-task-state\openlogic-bn-Beng-IN")
NOTE = "FULL_HTML_SOURCE_ARCHIVE_CHECKPOINT_2026-09-28.md"
MARKER = "Workflow checkpoint, 2026-09-28 full HTML and exact source archive:"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_json(path: Path, field: str, data: dict) -> None:
    current = json.loads(path.read_text(encoding="utf-8"))
    current[field] = data
    temporary = path.with_suffix(path.suffix + ".checkpoint.tmp")
    temporary.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def append_once(path: Path, line: str) -> None:
    before = path.read_text(encoding="utf-8")
    if MARKER not in before:
        with path.open("a", encoding="utf-8") as out:
            out.write(("" if before.endswith("\n") else "\n") + line + "\n")


def main() -> None:
    raise SystemExit("Historical 2026-09-28 checkpoint is retired: its fixed visual observations and publication state must not be replayed against current artifacts. Use current hash-bound redo and QA receipts.")
    preparation = json.loads((BUILD / "PREPARATION.json").read_text(encoding="utf-8"))
    reader = json.loads((BUILD / "SEMANTIC_READER_QA.json").read_text(encoding="utf-8"))
    probes = json.loads((BUILD / "VISUAL_PROBES.json").read_text(encoding="utf-8"))
    assets = json.loads((DIST / "FULL_RELEASE_ASSETS.json").read_text(encoding="utf-8"))
    attempt = json.loads((BUILD / "latest-attempt.json").read_text(encoding="utf-8"))
    tex = REPO / preparation["tex"]["path"]
    html = BUILD / "openlogic-bn-Beng-IN-complete.html"
    zip_path = DIST / "openlogic-bn-Beng-IN-complete-sources.zip"
    assert preparation["source_units"] == reader["source"]["source_units"] == reader["html"]["unit_markers"] == 722
    assert digest(tex) == preparation["tex"]["sha256"] == reader["source"]["prepared_tex_sha256"]
    assert digest(html) == reader["html"]["html_sha256"] == probes["reader_sha256"]
    assert reader["html"]["broken_internal_links"] == 0
    assert assets["archive_members"] == 1510 and not assets["pdf_included"]
    for item in assets["assets"]:
        assert digest(DIST / item["filename"]) == item["sha256"]
    assert attempt["input_sha256"] == digest(tex) and not attempt["acquired"]
    document = html_parser.fromstring(html.read_bytes())
    labels = {item["reader_label"] for item in preparation["label_map"]}
    targets = set(document.xpath('//*[@id]/@id'))
    assert len(labels) == 1718 and labels <= targets
    assert document.xpath('//*[@id="operator-font-license"]')
    assert document.xpath('//*[contains(text(),"ভরাট ও অঙ্কিত অঞ্চল")]')
    assert len(probes["probes"]) == 12
    visual = {
        "status": "sampled_browser_visual_pass; PDF and full-release QA pending",
        "reader_sha256": digest(html),
        "inspected_units": [
            {"unit": "OLP-0066", "observation": "বাংলা চলন্ত পাঠে মূল Intro/Elim গণিতনাম দৃশ্যমান"},
            {"unit": "OLP-0409", "observation": "fishhookright-এর মূল TX রেখা ও ফন্ট-প্রয়োগ দৃশ্যমান"},
            {"unit": "OLP-0425", "observation": "S5 ও T/B/4 দৃশ্যমান; সমতুল্য-শ্রেণি চিত্রের ছাঁট ও ধূসর ভরাটের পাঠ্যবিবরণ দেখা হয়েছে"},
            {"unit": "OLP-0488", "observation": "St Mary দ্বিমুখী সমতা-তীর দৃশ্যমান"},
            {"unit": "OLP-0523", "observation": "TX boxright উৎস-সংকেত ও পাঠ বিন্যাস দৃশ্যমান"},
            {"unit": "OLP-0702", "observation": "অনুমান-সিদ্ধান্ত সংযুক্ত প্রমাণ-বৃক্ষ দৃশ্যমান"},
        ],
        "probe_receipt_sha256": digest(BUILD / "VISUAL_PROBES.json"),
        "method": "লোকাল ব্রাউজারে একই পূর্ণ HTML DOM, এম্বেড-করা ফন্ট ও CSS থেকে নির্বাচিত উৎস-একক সরাসরি দেখে নেওয়া হয়েছে; ১২টি ভিউ তৈরি, ছয়টি বিষয়ভিত্তিক ভিউ দেখা।",
    }
    (BUILD / "VISUAL_QA.json").write_text(json.dumps(visual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "status": "local_full_html_source_archive_verified_pdf_pending",
        "public_source_units": 722, "public_reader_units": 299,
        "source_revision": "9620cc73f9c8e0ad003c514a5d3748f29611c4c0",
        "manifest_sha256": "5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155",
        "cumulative_tex": {"path": preparation["tex"]["path"], "bytes": tex.stat().st_size, "sha256": digest(tex)},
        "semantic_html": {"path": html.relative_to(REPO).as_posix(), "bytes": html.stat().st_size,
                          "sha256": digest(html)},
        "source_zip": {"path": zip_path.relative_to(REPO).as_posix(), "bytes": zip_path.stat().st_size,
                       "sha256": digest(zip_path), "members": 1510},
        "native_mathml": reader["html"]["native_mathml"],
        "proof_blocks": reader["html"]["proof_tree_blocks"],
        "tableau_blocks": reader["html"]["tableau_blocks"],
        "diagram_blocks": reader["html"]["diagram_blocks"],
        "source_labels_present_in_html": 1718,
        "broken_html_links": reader["html"]["broken_internal_links"],
        "visual_qa_sha256": digest(BUILD / "VISUAL_QA.json"),
        "latest_tex_attempt": {"status": attempt["status"], "acquired": attempt["acquired"],
                               "input_sha256": attempt["input_sha256"]},
        "remaining": ["guarded full PDF with bibliography/reference convergence and page inspection",
                      "final semantic/visual review and public HTML/direct-TeX/source-ZIP release",
                      "GitHub/Zenodo and anonymous byte-level readback"],
    }
    note = f"""# Full HTML and exact source archive checkpoint — 2026-09-28

The existing public source checkpoint is 722/722; the public reader is still 299 units.
The complete editable cumulative TeX is {tex.stat().st_size:,} bytes, SHA-256 `{digest(tex)}`.
The local HTML is {html.stat().st_size:,} bytes, SHA-256 `{digest(html)}`. It has all
722 source markers, {checkpoint['native_mathml']:,} native MathML expressions,
{checkpoint['proof_blocks']} proof blocks, {checkpoint['tableau_blocks']} tableaux and
{checkpoint['diagram_blocks']} diagrams. Every one of 1,718 source labels has an HTML target,
with zero broken internal links. Source-safe math macros in headings and prose, including
S5, axiom names and inference names, were repaired. The shaded-region diagram now preserves
its clipping/fill instructions in reflowable text. Six focused browser views were inspected;
see `build/full-edition/VISUAL_QA.json` for the bounded evidence.

The exact 1,510-member source ZIP is {zip_path.stat().st_size:,} bytes, SHA-256
`{digest(zip_path)}`. Every member was reopened and SHA-compared to its local input; a repeat
build produced the same archive SHA. It includes all 722 frozen English and 722 Bengali source
files, the cumulative TeX, build tools, upstream styles/bibliography, Bengali and operator
font sources, and original operator-font license notices. Direct TeX and HTML files are in
`dist/` with hashes in `FULL_RELEASE_ASSETS.json`. No PDF is included or claimed.

A guarded TeX pass on the earlier candidate reached page 82 and exposed a source table-spacing
error; the current cumulative TeX corrects it. At this natural validated checkpoint the mutex
was occupied, so no TeX launched. Do not poll the slot or suspend HTML/source work. The next
substantive steps are final HTML QA/public interim release and the guarded full PDF when available.
The existing Ultra goal remains active until the complete edition and public readback finish.
"""
    (STATE / NOTE).write_text(note, encoding="utf-8")
    checkpoint["file"] = NOTE
    checkpoint["file_sha256"] = digest(STATE / NOTE)
    cursor_path = STATE / "CURSOR.json"
    cursor = json.loads(cursor_path.read_text(encoding="utf-8"))
    assert len(cursor["translated_units"]) == len(cursor["public_units"]) == 722
    cursor["stage"] = "full_html_722_local_zip_verified_pdf_pending"
    cursor["full_html_source_archive_checkpoint"] = checkpoint
    cursor["next_action"] = "Local full HTML, cumulative editable TeX and exact 1510-member source ZIP verified; public reader remains 299. Finish interim full-HTML release QA/public readback, guarded PDF build and visual inspection, final full release. If TeX mutex busy, continue non-TeX work without polling. Keep this goal active at Ultra."
    temporary = cursor_path.with_suffix(".json.checkpoint.tmp")
    temporary.write_text(json.dumps(cursor, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(cursor_path)
    update_json(STATE / "QA.json", "full_reader_local_candidate", checkpoint)
    line = (f"{MARKER} Local 722-unit HTML SHA-256 {digest(html)}, {checkpoint['native_mathml']} MathML, "
            f"1718/1718 label targets and zero broken links; sampled browser QA. Direct TeX SHA-256 {digest(tex)}; "
            f"1510-member deterministic ZIP SHA-256 {digest(zip_path)} with all members SHA-read back. "
            "Guarded PDF compilation remains pending after one occupied-slot check; public reader still 299. "
            f"See {NOTE}; continue the same Ultra goal.")
    append_once(STATE / "GOAL.md", line)
    append_once(STATE / "WORKLOG.md", line)
    print(json.dumps({"checkpoint": NOTE, "sha256": checkpoint["file_sha256"],
                      "html_sha256": digest(html), "zip_sha256": digest(zip_path)}))


if __name__ == "__main__":
    main()
