"""Preserve the verified 722-unit public HTML milestone without closing the goal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
STATE = Path(r"C:\interlanguage-task-state\openlogic-bn-Beng-IN")
BUILD = REPO / "build/full-edition"
DIST = REPO / "dist"
RECEIPT = REPO / "evidence/PUBLIC_READBACK_READER_722_2026-09-28.json"
NOTE = "PUBLIC_FULL_HTML_READER_CHECKPOINT_2026-09-28.md"
MARKER = "Workflow checkpoint, 2026-09-28 public 722-unit HTML reader:"
COMMIT = "f67e4da4d1d903a020ce6a61c689e406bf640bc9"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def update_json(path: Path, change: dict) -> None:
    value = read(path)
    value.update(change)
    temp = path.with_suffix(path.suffix + ".public-full-reader.tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def append_once(path: Path, line: str) -> None:
    old = path.read_text(encoding="utf-8")
    if MARKER not in old:
        with path.open("a", encoding="utf-8") as stream:
            stream.write(("" if old.endswith("\n") else "\n") + line + "\n")


def main() -> None:
    public = read(RECEIPT)
    qa = read(BUILD / "SEMANTIC_READER_QA.json")
    visual = read(BUILD / "VISUAL_QA.json")
    assets = read(DIST / "FULL_RELEASE_ASSETS.json")
    prep = read(BUILD / "PREPARATION.json")
    attempt = read(BUILD / "latest-attempt.json")
    assert public["status"] == "passed" and public["anonymous"] and not public["credentials_used"]
    assert public["git_commit"] == COMMIT and public["reader_units"] == 722
    assert len(public["release_assets"]) == 8 and len(public["raw_objects"]) == 3
    assert qa["source_units"] == qa["html"]["unit_markers"] == 722
    assert qa["html"]["broken_internal_links"] == 0
    assert len(prep["label_map"]) == 1718
    assert assets["archive_members"] == 1510 and not assets["pdf_included"]
    assert visual["reader_sha256"] == qa["html"]["html_sha256"]
    assert len(visual["inspected_units"]) == 7
    assert attempt["input_sha256"] == prep["tex"]["sha256"] and not attempt["acquired"]
    assert public["online_reader"]["sha256"] == qa["html"]["html_sha256"]
    assert public["online_reader"]["sha256"] == sha(REPO / "docs/index.html")
    for asset in assets["assets"]:
        assert sha(DIST / asset["filename"]) == asset["sha256"]
    checkpoint = {
        "status": "public_722_html_and_source_archive_verified_pdf_pending",
        "source_units": 722,
        "reader_units": 722,
        "source_revision": public["source_revision"],
        "manifest_sha256": public["manifest_sha256"],
        "github_commit": COMMIT,
        "github_release": public["release_url"],
        "html_url": public["online_reader"]["url"],
        "html_bytes": public["online_reader"]["bytes"],
        "html_sha256": public["online_reader"]["sha256"],
        "source_zip_sha256": next(x["sha256"] for x in assets["assets"] if x["filename"].endswith("sources.zip")),
        "native_mathml": qa["html"]["native_mathml"],
        "source_labels": len(prep["label_map"]),
        "visual_units": len(visual["inspected_units"]),
        "anonymous_assets_verified": len(public["release_assets"]),
        "anonymous_raw_objects_verified": len(public["raw_objects"]),
        "public_receipt": RECEIPT.relative_to(REPO).as_posix(),
        "public_receipt_sha256": sha(RECEIPT),
        "pdf": "pending: guarded compilation and page QA",
        "full_epub": "pending",
        "zenodo": "v0.3.0 remains latest; existing API credential returned HTTP 403 and browser authorization would expand GitHub repo-hook access, so no new Zenodo version was created",
        "latest_tex_attempt": {"acquired": attempt["acquired"], "input_sha256": attempt["input_sha256"]},
        "remaining": ["guarded PDF build and visual verification", "full EPUB if feasible",
                      "Zenodo v0.4 and final version once existing authorized access is available",
                      "final full-edition GitHub/Zenodo and anonymous readback"],
    }
    note = f"""# Public full HTML reader checkpoint — 2026-09-28

The public GitHub release is {checkpoint['github_release']} at commit `{COMMIT}`.
The GitHub Pages reader is {checkpoint['html_url']} with all 722 units,
{checkpoint['native_mathml']:,} native MathML expressions and {checkpoint['source_labels']:,}/{checkpoint['source_labels']:,}
source label targets. Its {checkpoint['html_bytes']:,} bytes have SHA-256 `{checkpoint['html_sha256']}`.
The 1,510-member exact source ZIP has SHA-256 `{checkpoint['source_zip_sha256']}`.
Anonymous HTTPS byte readback matched all eight release assets, the Pages HTML and three
immutable raw GitHub objects. The sanitized receipt is `{checkpoint['public_receipt']}`
with SHA-256 `{checkpoint['public_receipt_sha256']}`. Seven bounded browser views were inspected.

The full PDF and new EPUB are not released. The latest single bounded TeX acquisition was
unavailable; compilation did not launch. Continue non-TeX work and make one acquisition at a
later natural validated checkpoint. Zenodo remains at the public v0.3.0 record
`https://zenodo.org/records/22848705`. The existing API credential returned HTTP 403. The
browser was signed out; its GitHub OAuth login requested a new repository-webhook admin grant,
which was not granted. No duplicate Zenodo lineage was made. If an already authorized route
becomes available, publish v0.4 within the existing concept, with the online HTML reading link
as the PDF-free preview exception. The full-edition goal remains active at Ultra effort.
"""
    (STATE / NOTE).write_text(note, encoding="utf-8")
    checkpoint["note"] = NOTE
    checkpoint["note_sha256"] = sha(STATE / NOTE)
    cursor_path = STATE / "CURSOR.json"
    cursor = read(cursor_path)
    assert len(cursor["public_units"]) == len(cursor["translated_units"]) == 722
    cursor.update({
        "stage": "public_full_html_reader_722_pdf_pending",
        "published_revision": COMMIT,
        "released_artifact_revision": COMMIT,
        "released_reader_units": 722,
        "release": checkpoint["github_release"],
        "public_full_reader_checkpoint": checkpoint,
        "next_action": "Continue the same Ultra goal. Build and visually QA the full PDF under one bounded TeX slot attempt at a natural validated checkpoint; meanwhile advance non-TeX EPUB/release QA. Publish Zenodo only in the existing concept with authorized access, then complete final public byte readback. No new task, fork or lower effort.",
    })
    temp = cursor_path.with_suffix(".json.public-full-reader.tmp")
    temp.write_text(json.dumps(cursor, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(cursor_path)
    update_json(STATE / "QA.json", {"public_full_reader_release": checkpoint})
    line = (f"{MARKER} Public GitHub/Pages reader 722/722 at `{COMMIT}`; "
            f"HTML SHA-256 {checkpoint['html_sha256']}, ZIP SHA-256 {checkpoint['source_zip_sha256']}; "
            f"8 release assets, Pages bytes and 3 raw objects anonymously matched. "
            "Seven browser views checked; full PDF/EPUB and Zenodo update remain. "
            f"See {NOTE}; continue same Ultra goal.")
    for name in ("GOAL.md", "WORKLOG.md", "PUBLICATION_RECEIPTS.md"):
        append_once(STATE / name, line)
    print(json.dumps({"checkpoint": NOTE, "sha256": checkpoint["note_sha256"],
                      "public_receipt_sha256": checkpoint["public_receipt_sha256"],
                      "released_reader_units": 722}))


if __name__ == "__main__":
    main()
