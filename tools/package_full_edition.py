"""Build the exact, deterministic 722-source release archive from named inputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
from edition_metadata import FIXED_ZIP_TIME, metadata


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build/full-edition"
DIST = REPO / "dist"
MANIFEST = REPO / "evidence/FULL_SOURCE_MANIFEST.jsonl"
ARCHIVE = DIST / "openlogic-bn-Beng-IN-complete-sources.zip"
TEX = BUILD / "openlogic-bn-Beng-IN-complete.tex"
HTML = BUILD / "openlogic-bn-Beng-IN-complete.html"
PREFIX = "OpenLogic-bn-Beng-IN/"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_exact(files: set[Path], relative: str) -> None:
    path = (REPO / relative).resolve(strict=True)
    assert path.is_relative_to(REPO.resolve()), relative
    assert path.is_file(), relative
    files.add(path)


def main() -> None:
    DIST.mkdir(exist_ok=True)
    manifest = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]
    assert len(manifest) == len({row["unit_id"] for row in manifest}) == 722
    preparation = json.loads((BUILD / "PREPARATION.json").read_text(encoding="utf-8"))
    qa = json.loads((BUILD / "SEMANTIC_READER_QA.json").read_text(encoding="utf-8"))
    status = json.loads((REPO / "evidence/DRAFT_STATUS.json").read_text(encoding="utf-8"))
    checks = {row["unit_id"]: row for row in status["current_checks"]["unit_checks"]}
    assert status["current_checks"]["segment_index_sha256"] == digest(
        REPO / "evidence/SEGMENT_CANON_USE.jsonl")
    assert preparation["tex"]["sha256"] == digest(TEX)
    assert qa["source"]["prepared_tex_sha256"] == digest(TEX)
    assert qa["html"]["html_sha256"] == digest(HTML)
    assert qa["html"]["unit_markers"] == 722
    assert preparation["edition_identity"] == qa["edition_identity"] == metadata()
    html_visual = json.loads((BUILD / "HTML_VISUAL_QA.json").read_text(encoding="utf-8"))
    assert html_visual["status"] == "passed" and html_visual["html_sha256"] == digest(HTML)
    assert html_visual["source_units"] == 722 and html_visual["manually_inspected_screenshots"]
    capture_path = BUILD / "BROWSER_CAPTURES.json"
    assert html_visual["browser_captures_sha256"] == digest(capture_path)
    capture_record = json.loads(capture_path.read_text(encoding="utf-8"))
    assert capture_record["reader_sha256"] == digest(HTML)
    inspected = {item["file"]: item for item in html_visual["manually_inspected_screenshots"]}
    captured = {item["file"]: item for row in capture_record["captures"] for item in row["screenshots"]}
    for relative, item in inspected.items():
        visual_file = (BUILD / relative).resolve(strict=True)
        assert visual_file.is_relative_to(BUILD.resolve())
        assert item["sha256"] == captured[relative]["sha256"] == digest(visual_file)
    pdf = BUILD / "openlogic-bn-Beng-IN-complete.pdf"
    epub = BUILD / "openlogic-bn-Beng-IN-complete.epub"
    pdf_check = json.loads((BUILD / "PDF_QA.json").read_text(encoding="utf-8"))
    epub_check = json.loads((BUILD / "EPUB_QA.json").read_text(encoding="utf-8"))
    assert pdf_check["status"] == "passed" and pdf_check["source_units"] == 722
    assert pdf_check["tex_input_sha256"] == digest(TEX) and pdf_check["pdf_sha256"] == digest(pdf)
    visual_path = (REPO / pdf_check["visual_qa_path"]).resolve(strict=True)
    assert visual_path.is_relative_to(REPO.resolve())
    assert pdf_check["visual_qa_sha256"] == digest(visual_path)
    pdf_visual = json.loads(visual_path.read_text(encoding="utf-8"))
    pdf_captures_path = BUILD / "CURRENT_PDF_CAPTURES.json"
    assert pdf_visual["pdf_captures_sha256"] == digest(pdf_captures_path)
    pdf_captures = json.loads(pdf_captures_path.read_text(encoding="utf-8"))
    assert pdf_captures["pdf_sha256"] == digest(pdf)
    for item in pdf_visual["manually_inspected_pages"]:
        assert item in pdf_captures["captures"]
        image_path = (REPO / item["file"]).resolve(strict=True)
        assert image_path.is_relative_to(BUILD.resolve()) and digest(image_path) == item["sha256"]
    assert epub_check["status"] == "passed" and epub_check["source_units"] == 722
    assert epub_check["edition_identity"] == metadata()
    assert epub_check["html_sha256"] == digest(HTML) and epub_check["epub"]["sha256"] == digest(epub)
    assert epub_check["epubcheck"]["messages"] == 0
    assert epub_check["epubcheck"]["report_sha256"] == digest(BUILD / "EPUBCHECK.json")
    files: set[Path] = set()
    for row in manifest:
        source_path = row["source_path"]
        assert source_path.startswith("content/") and ".." not in Path(source_path).parts
        original = REPO / "upstream" / source_path
        target = REPO / "bn-Beng-IN" / source_path
        assert original.stat().st_size == row["source_bytes"] and digest(original) == row["source_sha256"]
        assert digest(target) == checks[row["unit_id"]]["target_sha256"]
        add_exact(files, original.relative_to(REPO).as_posix())
        add_exact(files, target.relative_to(REPO).as_posix())
    for relative in (
        "README.md", "RELEASE_NOTES_1_0_1.md", ".gitattributes", "upstream/LICENSE.md", "upstream/README.md",
        "upstream/open-logic-config.sty", "upstream/open-logic-complete-config.sty",
        "upstream/open-logic-locale.sty", "upstream/open-logic-envs.sty",
        "upstream/open-logic-complete.tex", "upstream/bib/open-logic.bib",
        "upstream/bib/natbib-oup.bst", "bn-Beng-IN/bib/open-logic.bib",
        "evidence/BIBLIOGRAPHY_CORRECTIONS.json",
        "evidence/BIBLIOGRAPHY_OPTIONAL_URL_DISPOSITION_2026-10-01.md",
        "evidence/SOURCE_NORMALIZATIONS.jsonl",
        "evidence/GPT6_SOL_REDO_UNIT_REVIEWS.jsonl",
        "evidence/GPT6_SOL_REDO_SUPPORT_REVIEWS.jsonl",
        "evidence/GPT6_SOL_REDO_LINDSTROM_SUPPORT_CHECK.json",
        "evidence/GPT6_SOL_REDO_TRANSLATION_DECISION_EXPORT_CHECK.json",
        "evidence/TRANSLATION_DECISION_LOG.jsonl", "evidence/TRANSLATION_DECISION_LOG.md",
        "evidence/TRANSLATION_DECISION_INDEX.json", "evidence/TRANSLATION_DECISION_PRIORITY.md",
        "evidence/TRANSLATION_DECISION_OCCURRENCES.csv",
        "fonts/NotoSerifBengali-Regular.ttf", "fonts/NotoSerifBengali-Bold.ttf",
        "fonts/Noto-fonts-LICENSE.txt",
        "evidence/FULL_SOURCE_MANIFEST.jsonl", "evidence/DRAFT_STATUS.json",
        "evidence/SOURCE_MODEL_PROVENANCE_722.json", "evidence/SEMANTIC_REVIEW_FINAL_SOURCE_UNITS.md",
        "evidence/SEMANTIC_REVIEW_LINDSTROM.md",
        "evidence/CANON_SOURCES.jsonl", "evidence/CANON_PASSAGES.jsonl",
        "evidence/SEGMENT_CANON_USE.jsonl", "evidence/TERM_DECISIONS.jsonl",
        "evidence/SOURCE_CORRECTIONS.jsonl", "evidence/RECOVERED_CANON_VERIFICATION.json",
        "tools/prepare_full_edition.py", "tools/build_cumulative_semantic_reader.py",
        "tools/build_full_semantic_reader.py", "tools/build_reader_operator_font.py",
        "tools/build_full_epub.py", "tools/edition_metadata.py", "tools/reader_tableau.py", "tools/reader_diagrams.py",
        "tools/build_full_edition_windows.ps1", "tools/create_reader_visual_probes.py",
        "tools/render_reader_visual_probes.cjs",
        "tools/package_full_edition.py", "tools/check_source_draft.py",
        "tools/verify_segment_canon.py", "tools/verify_full_pdf.py",
        "evidence/PDF_PREPARATION_CHECKPOINT_2026-09-28.json",
        "evidence/PDF_LAYOUT_CHECKPOINT_2026-09-28.json",
        "evidence/PDF_TABLEAU_CHECKPOINT_2026-09-28.json",
        "evidence/PDF_BOOKMARK_PREFLIGHT_2026-09-28.json",
        "evidence/PDF_LIST_BREAK_CHECKPOINT_2026-09-28.json",
        "evidence/PDF_JOINER_PREFLIGHT_2026-09-28.json",
        "evidence/PDF_FINAL_QA_2026-09-28.json",
        "evidence/READER_VISIBLE_TOKEN_AUDIT_2026-09-28.json",
        "evidence/ZENODO_LINEAGE_AUDIT_2026-09-28.json",
        "build/full-edition/openlogic-bn-Beng-IN-complete.tex",
        "build/full-edition/PREPARATION.json", "build/full-edition/SEMANTIC_READER_QA.json",
        "build/full-edition/EPUB_QA.json", "build/full-edition/EPUBCHECK.json",
        "build/full-edition/OPERATOR_FONT.json", "build/full-edition/PANDOC_INPUT.json",
        "build/full-edition/SEMANTIC_INPUT.json", "build/full-edition/environment-markers.json",
        "build/full-edition/proof-graphs.json", "build/full-edition/tableau-graphs.json", "build/full-edition/diagram-graphs.json",
        "build/full-edition/HTML_VISUAL_QA.json", "build/full-edition/BROWSER_CAPTURES.json",
        "build/full-edition/VISUAL_PROBES.json",
        "build/full-edition/SOURCE_FRAGMENT_SCOPES.json", "build/full-edition/READER_BUILD_ATTEMPT.json",
        "build/full-edition/math-link-targets.json",
    ):
        add_exact(files, relative)
    # Current redo records are separate from explicitly dated historical checkpoints.
    for pattern in ("REDO_GPT6_SOL_*.md", "GPT6_SOL_REDO_*_CHECK.json", "REDO_GPT6_SOL_*_AUDITED_ENGLISH.tex"):
        for path in (REPO / "evidence").glob(pattern):
            add_exact(files, path.relative_to(REPO).as_posix())
    for relative in inspected:
        add_exact(files, (BUILD / relative).relative_to(REPO).as_posix())
    add_exact(files, "build/full-edition/PDF_QA.json")
    add_exact(files, "build/full-edition/CURRENT_PDF_CAPTURES.json")
    for item in pdf_visual["manually_inspected_pages"]:
        add_exact(files, item["file"])
    add_exact(files, pdf_check["visual_qa_path"])
    add_exact(files, "build/full-edition/latest-attempt.json")
    for directory, patterns in (
        ("upstream/sty", ("*.sty", "*.cls")),
        ("upstream/include", ("*.tex",)),
        ("upstream/assets/logos", ("*.png",)),
        ("build/full-edition/font-sources", ("*.pfb", "*.vf", "*.tfm", "*.txt", "*.pdf")),
    ):
        root = REPO / directory
        assert root.is_dir(), directory
        for pattern in patterns:
            for path in root.glob(pattern):
                add_exact(files, path.relative_to(REPO).as_posix())
    assert len(files) >= 1444
    names = [path.relative_to(REPO).as_posix() for path in files]
    assert len(names) == len(set(names))
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED, compresslevel=9) as output:
        for path in sorted(files, key=lambda path: path.relative_to(REPO).as_posix()):
            name = PREFIX + path.relative_to(REPO).as_posix()
            info = ZipInfo(name, date_time=FIXED_ZIP_TIME)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            output.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    with ZipFile(ARCHIVE) as inp:
        assert len(inp.namelist()) == len(files)
        assert inp.testzip() is None
        for path in files:
            relative = path.relative_to(REPO).as_posix()
            assert hashlib.sha256(inp.read(PREFIX + relative)).hexdigest() == digest(path), relative
    outputs = [ARCHIVE]
    for source, suffix in ((TEX, "tex"), (HTML, "html")):
        target = DIST / ("openlogic-bn-Beng-IN-complete." + suffix)
        target.write_bytes(source.read_bytes())
        outputs.append(target)
    for source in (epub, pdf):
        target = DIST / source.name
        target.write_bytes(source.read_bytes())
        outputs.append(target)
    rows = [{"filename": path.name, "bytes": path.stat().st_size, "sha256": digest(path)}
            for path in outputs]
    (DIST / "SHA256SUMS-complete.txt").write_text(
        "".join(row["sha256"] + "  " + row["filename"] + "\n" for row in rows), encoding="ascii")
    (DIST / "FULL_RELEASE_ASSETS.json").write_text(
        json.dumps({"schema": "openlogic-bn-full-release-assets/1", "source_units": 722,
                    "archive_members": len(files), "pdf_included": True,
                    "epub_included": True, "edition_identity": metadata(),
                    "assets": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"archive_members": len(files), "assets": rows}, ensure_ascii=False))


if __name__ == "__main__":
    main()
