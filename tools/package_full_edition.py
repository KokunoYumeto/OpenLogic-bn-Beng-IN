"""Build the exact, deterministic 722-source release archive from named inputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


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
    assert preparation["tex"]["sha256"] == digest(TEX)
    assert qa["source"]["prepared_tex_sha256"] == digest(TEX)
    assert qa["html"]["html_sha256"] == digest(HTML)
    assert qa["html"]["unit_markers"] == 722
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
        "README.md", ".gitattributes", "upstream/LICENSE.md", "upstream/README.md",
        "upstream/open-logic-config.sty", "upstream/open-logic-complete-config.sty",
        "upstream/open-logic-locale.sty", "upstream/open-logic-envs.sty",
        "upstream/open-logic-complete.tex", "upstream/bib/open-logic.bib",
        "upstream/bib/natbib-oup.bst",
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
        "tools/build_full_epub.py",
        "tools/build_full_edition_windows.ps1", "tools/create_reader_visual_probes.py",
        "tools/package_full_edition.py", "tools/check_source_draft.py",
        "build/full-edition/openlogic-bn-Beng-IN-complete.tex",
        "build/full-edition/PREPARATION.json", "build/full-edition/SEMANTIC_READER_QA.json",
        "build/full-edition/EPUB_QA.json", "build/full-edition/EPUBCHECK.json",
        "build/full-edition/OPERATOR_FONT.json", "build/full-edition/PANDOC_INPUT.json",
        "build/full-edition/SEMANTIC_INPUT.json", "build/full-edition/environment-markers.json",
        "build/full-edition/proof-graphs.json", "build/full-edition/math-link-targets.json",
    ):
        add_exact(files, relative)
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
            info = ZipInfo(name, date_time=(2026, 9, 28, 0, 0, 0))
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
    epub = BUILD / "openlogic-bn-Beng-IN-complete.epub"
    epub_qa = BUILD / "EPUB_QA.json"
    epub_included = False
    if epub_qa.exists():
        epub_check = json.loads(epub_qa.read_text(encoding="utf-8"))
        assert epub_check["status"] == "passed" and epub_check["source_units"] == 722
        assert epub_check["html_sha256"] == digest(HTML)
        assert epub_check["epub"]["sha256"] == digest(epub)
        assert epub_check["epubcheck"]["messages"] == 0
        target = DIST / epub.name
        target.write_bytes(epub.read_bytes())
        outputs.append(target)
        epub_included = True
    pdf = BUILD / "openlogic-bn-Beng-IN-complete.pdf"
    # Include the PDF only after a separate passing final PDF QA receipt exists.
    pdf_qa = BUILD / "PDF_QA.json"
    pdf_included = False
    if pdf_qa.exists():
        pdf_check = json.loads(pdf_qa.read_text(encoding="utf-8"))
        assert pdf_check["status"] == "passed" and pdf_check["pdf_sha256"] == digest(pdf)
        target = DIST / pdf.name
        target.write_bytes(pdf.read_bytes())
        outputs.append(target)
        pdf_included = True
    rows = [{"filename": path.name, "bytes": path.stat().st_size, "sha256": digest(path)}
            for path in outputs]
    (DIST / "SHA256SUMS-complete.txt").write_text(
        "".join(row["sha256"] + "  " + row["filename"] + "\n" for row in rows), encoding="ascii")
    (DIST / "FULL_RELEASE_ASSETS.json").write_text(
        json.dumps({"schema": "openlogic-bn-full-release-assets/1", "source_units": 722,
                    "archive_members": len(files), "pdf_included": pdf_included,
                    "epub_included": epub_included,
                    "assets": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"archive_members": len(files), "assets": rows}, ensure_ascii=False))


if __name__ == "__main__":
    main()
