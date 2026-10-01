"""Write the named durable checkpoint for the local 722-unit reader candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build/full-edition"
STATE = Path(r"C:\interlanguage-task-state\openlogic-bn-Beng-IN")
NOTE = "READER_INTEGRATION_CHECKPOINT_2026-09-28.md"
MARKER = "Workflow checkpoint, 2026-09-28 local full-reader integration:"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, record: dict) -> None:
    temp = path.with_suffix(path.suffix + ".checkpoint.tmp")
    temp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def append_once(path: Path, line: str) -> None:
    content = path.read_text(encoding="utf-8")
    if MARKER not in content:
        with path.open("a", encoding="utf-8") as output:
            output.write(("" if content.endswith("\n") else "\n") + line + "\n")


def main() -> None:
    raise SystemExit("Historical 2026-09-28 checkpoint is retired: its fixed visual observations and publication state must not be replayed against current artifacts. Use current hash-bound redo and QA receipts.")
    preparation = json.loads((BUILD / "PREPARATION.json").read_text(encoding="utf-8"))
    reader = json.loads((BUILD / "SEMANTIC_READER_QA.json").read_text(encoding="utf-8"))
    source = reader["source"]
    html = reader["html"]
    tex_path = REPO / preparation["tex"]["path"]
    html_path = BUILD / "openlogic-bn-Beng-IN-complete.html"
    assert source["source_units"] == html["unit_markers"] == 722
    assert source["prepared_tex_sha256"] == preparation["tex"]["sha256"] == digest(tex_path)
    assert html["html_sha256"] == digest(html_path)
    assert html["broken_internal_links"] == html["scripts"] == 0
    assert len(source["documented_missing_source_references"]) == 4
    assert len(source["reader_adjustments"]) == 4
    assert reader["status"] == "structural checks passed; visual QA pending"
    current = {
        "status": "local_candidate_structural_pass_visual_partial_pdf_pending",
        "source_revision": "9620cc73f9c8e0ad003c514a5d3748f29611c4c0",
        "manifest_sha256": "5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155",
        "published_source_revision": "c91a129f4e7addb118c4258a20b5903c1112e274",
        "published_source_units": 722,
        "published_reader_units": 299,
        "complete_tex": preparation["tex"],
        "local_html": {"path": str(html_path.relative_to(REPO)).replace("\\", "/"),
                       "bytes": html["html_bytes"], "sha256": html["html_sha256"]},
        "native_mathml": html["native_mathml"],
        "proof_blocks": html["proof_tree_blocks"],
        "tableau_blocks": html["tableau_blocks"],
        "diagram_blocks": html["diagram_blocks"],
        "internal_links": html["internal_links"],
        "numbered_environments": html["numbered_environments"],
        "visual_inspection": ["OLP-0425: Bengali text, S5 and T/B/4", "OLP-0702: proof lines and premises",
                              "OLP-0409: fishhookright", "OLP-0488: leftrightarroweq", "OLP-0523: boxright"],
        "font_virtual_mapping": "ntxsyc.vf O200 -> txsyc O200; C J -> txsyc C J, verified using vftovp; source font licensing and archive notices still to finish",
        "known_source_gaps": [item["source_label"] for item in source["documented_missing_source_references"]],
        "remaining": ["finish semantic and visual QA across representative units and labels",
                      "complete PDF compilation and PDF visual inspection under guarded TeX slot",
                      "finalize source ZIP, font notices, Bengali metadata and public release/readback"],
    }
    note = f"""# Local full-reader integration checkpoint — 2026-09-28

The frozen 722/722 source translations remain public and anonymously read back at commit
`{current['published_source_revision']}`. The public HTML reader remains 299 units.

The integrated editable TeX candidate `{current['complete_tex']['path']}` is
{tex_path.stat().st_size:,} bytes, SHA-256 `{current['complete_tex']['sha256']}`. It inserts all
722 unique source units in the relevant subject chapters, including eight inline rule-table fragments.
The local semantic HTML candidate `{current['local_html']['path']}` is
{current['local_html']['bytes']:,} bytes, SHA-256 `{current['local_html']['sha256']}`. The structural
checks pass 722 ordered markers, {current['native_mathml']:,} native MathML expressions,
{current['proof_blocks']} proof blocks, {current['tableau_blocks']} tableaux,
{current['diagram_blocks']} reflowable diagram descriptions and {current['internal_links']:,} internal
links with zero broken targets. The HTML has no script elements or unconverted TeX math warnings.

Browser screenshots and accessibility views of five named units verify Bengali shaping, source-safe
S5/T/B/4 math in prose and headings, inference premises, and the three source-operator font faces.
The four named references absent from the frozen source remain explicitly documented; two hidden
satisfaction statements, one quoted macro and one missing source proof-display command were
adjusted only in the cumulative rendering. This is a local candidate, not a published full edition.
The font license panel, broader visual and label checks, PDF build/inspection, reproducible ZIP,
GitHub/Zenodo release and anonymous readback remain. Two earlier bounded mutex checks found the
TeX slot occupied; no TeX was launched. Occupancy does not suspend the substantive goal.

Next: finish label/visual/font audit and make one bounded TeX acquisition at a natural checkpoint;
continue non-TeX work immediately if unavailable. Keep the current goal and Ultra effort active.
"""
    (STATE / NOTE).write_text(note, encoding="utf-8")
    cursor_path = STATE / "CURSOR.json"
    cursor = json.loads(cursor_path.read_text(encoding="utf-8"))
    assert len(cursor["translated_units"]) == 722 and len(cursor["public_units"]) == 722
    cursor["stage"] = "reader_722_local_structural_pass_pdf_pending"
    cursor["reader_integration_checkpoint"] = {"file": NOTE, "sha256": digest(STATE / NOTE), **current}
    cursor["next_action"] = "Full 722-unit TeX and semantic HTML are local candidates. Finish visual/label/font QA; build and inspect the guarded PDF; publish complete reader, direct TeX and exact source ZIP with verified public readback. Public reader remains 299. TeX slot occupancy never blocks non-TeX work. Preserve Ultra and this goal."
    write_json(cursor_path, cursor)
    qa_path = STATE / "QA.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    assert qa["translated_units"] == len(qa["public_source_units"]) == 722
    qa["full_reader_local_candidate"] = {"file": NOTE, "sha256": digest(STATE / NOTE), **current}
    write_json(qa_path, qa)
    line = (f"{MARKER} Integrated all 722 unique source units. Native TeX SHA-256 "
            f"{current['complete_tex']['sha256']}; local semantic HTML SHA-256 {current['local_html']['sha256']} "
            f"({current['native_mathml']} MathML, {current['proof_blocks']} proof blocks, zero broken internal links). "
            f"Five focused browser views checked; full visual QA, guarded PDF, complete archive, release and anonymous readback remain. "
            f"Public reader stays 299; {NOTE} records exact boundaries. Continue this active Ultra goal.")
    append_once(STATE / "GOAL.md", line)
    append_once(STATE / "WORKLOG.md", line)
    reconciliation_path = STATE / "RECONCILIATION_20260928_FINAL_SOURCE.md"
    if NOTE not in reconciliation_path.read_text(encoding="utf-8"):
        with reconciliation_path.open("a", encoding="utf-8") as output:
            output.write("\nThe later model attribution was independently resolved from this task's local turn contexts: "
                         "GPT-6 Sol at Ultra effort, with earlier GPT-5.6 Sol at Ultra effort. The public source "
                         "readback is now 722/722 at c91a129; the public reader remains 299. "
                         f"The current full-reader candidate is recorded in {NOTE}.\n")
    print(json.dumps({"checkpoint": NOTE, "sha256": digest(STATE / NOTE),
                      "html_sha256": current["local_html"]["sha256"], "public_reader_units": 299}))


if __name__ == "__main__":
    main()
