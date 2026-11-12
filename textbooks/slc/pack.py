"""Create the exact textbook archive and reader/input manifest."""
from pathlib import Path
from hashlib import sha256
import json
import re
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED


P = Path(__file__).resolve().parent
SOURCE = P / "source"
BUILD_FILES = {"build.ps1", "check-build.py", "WindowsProcessJob.cs", "assemble.py",
               "scope.txt", "OUTLINE.json", "PINS.json", "MODULES.json", "GLOSSARY-ORDER.json",
               "README.md", "slc-screen-bn.tex"}
stem = "slc-screen-bn"
source_paths = {p.relative_to(P).as_posix() for p in SOURCE.rglob("*") if p.is_file()}
assert all(not set(Path(name).parts) & {"__pycache__", ".git", ".build"} for name in source_paths)
assert not any(re.search(r"(?:\.log$|\.fls$|\.aux$|^source/.*\.zip$)", x) for x in source_paths)
for relative in (f"{stem}.pdf", f"{stem}.tex", *BUILD_FILES, *source_paths):
    assert (P / relative).is_file(), relative


def identity(relative):
    p = P / relative
    return {"bytes": p.stat().st_size, "sha256": sha256(p.read_bytes()).hexdigest()}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


inventories = sorted(P.glob(".build/*/source/locale/bn/courses/sets-logic-computation/inventory.json"))
pdf = identity(f"{stem}.pdf")
matched = [json.loads(i.read_text(encoding="utf-8")) for i in inventories]
book = next(x for x in matched if x["pdf_sha256"] == pdf["sha256"] and x["native_imports"] == 176)
cumulative_pdf = identity(f"{stem}-cumulative.pdf")
cumulative = next(x for x in matched if x["pdf_sha256"] == cumulative_pdf["sha256"] and x["native_imports"] == 0)
assert cumulative["pages"] == book["pages"] and cumulative["labels"] == book["labels"]
assert book["conditional_section_labels"] == cumulative["conditional_section_labels"] == 30
manifest = {"title": "সেট, যুক্তি, গণনা", "language": "bn-IN", "script": "Bengali",
    "original_author": "Richard Zach", "underlying_text": "Open Logic Project",
    "sources": json.loads((P / "PINS.json").read_text(encoding="utf-8")),
    "translation": {"authorship": "AI-translated and typeset by OpenAI Codex",
                    "model": "gpt-6.1-sol", "reasoning_effort": "ultra",
                    "model_metadata_observed_utc": "2026-11-12T23:20:45.8616904Z",
                    "reused_translation_models": ["gpt-5.6-sol", "gpt-6-sol"],
                    "reused_translation_review_model": "gpt-6.1-sol", "reused_reasoning_effort": "ultra"},
    "contents": {"numbered_chapters": 15, "appendices": ["A", "B", "C", "D"],
                 "summaries": book["summaries"], "glossary_entries": 79, "native_modules": 176},
    "screen_pdf": {"engine": "XeLaTeX", "pages": book["pages"], "path": f"{stem}.pdf", **pdf},
    "cumulative_tex": {"path": f"{stem}.tex", **identity(f"{stem}.tex")},
    "source_inputs": {name: identity(name) for name in sorted(source_paths | BUILD_FILES)},
}
(P / "MANIFEST.json").write_bytes(encode(manifest))
members = sorted(source_paths | BUILD_FILES | {"MANIFEST.json"})
archive = P / f"{stem}-sources.zip"
with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as out:
    for name in members:
        info = ZipInfo(name, (2026, 11, 13, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        out.writestr(info, (P / name).read_bytes(), compresslevel=9)
with ZipFile(archive) as inp:
    assert inp.namelist() == members and inp.testzip() is None
    for name in members:
        assert inp.read(name) == (P / name).read_bytes()
names = [f"{stem}.pdf", f"{stem}.tex", archive.name, "MANIFEST.json"]
(P / "SHA256SUMS.txt").write_text("".join(f"{identity(name)['sha256']}  {name}\n" for name in names),
                                encoding="ascii", newline="\n")
print(json.dumps({"archive_members": len(members), "assets": {n: identity(n) for n in names}}))
