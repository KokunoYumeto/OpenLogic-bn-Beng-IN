"""Check actual imported modules, chapter order, glossary and reference state."""
from argparse import ArgumentParser
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess


PROJECT = Path(__file__).resolve().parent
parser = ArgumentParser(description=__doc__)
parser.add_argument("book", type=Path)
parser.add_argument("--cumulative", action="store_true")
args = parser.parse_args()
book = args.book.resolve()
locale = book.parent.parent


def read(name):
    return (book / name).read_text(encoding="utf-8-sig")


fls = read("slc-screen.fls")
imports = set()
summaries = set()
for line in fls.splitlines():
    if not line.startswith("INPUT "):
        continue
    path = (book / line[6:]).resolve()
    if path.is_relative_to(locale / "content") and path.suffix == ".tex":
        imports.add(path.relative_to(locale).as_posix())
    if path.is_relative_to(book / "include") and re.fullmatch(r"summary-\d+\.tex", path.name):
        summaries.add(int(path.stem.split("-")[1]))
    if args.cumulative and path.parent == book and re.fullmatch(r"slc-embedded-summary-\d+\.tex", path.name):
        summaries.add(int(path.stem.split("-")[-1]))
expected = set((PROJECT / "scope.txt").read_text(encoding="utf-8").splitlines())
if not args.cumulative:
    assert expected == imports, {"missing": sorted(expected - imports), "extra": sorted(imports - expected)}
else:
    assert not imports, "The cumulative editable file must not import separate content modules"
    generated = {Path(line[6:]).name for line in fls.splitlines()
                 if line.startswith("INPUT ") and re.fullmatch(r"slc-module-\d{3}\.tex", Path(line[6:]).name)}
    assert generated == {f"slc-module-{i:03d}.tex" for i in range(1, 177)}, sorted(generated)
assert summaries == {1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15}, sorted(summaries)

toc = read("slc-screen.toc")
chapter_numbers = re.findall(r"\\contentsline\s*\{(?:chapter|appendix)\}\s*\{\\(?:chapter)?numberline\s*\{([0-9]+|[A-Z])\}", toc)
assert chapter_numbers == [str(n) for n in range(1, 16)] + list("ABCD"), chapter_numbers
assert len(re.findall(r"\\contentsline\s*\{section\}\s*\{সারাংশ\}", toc)) == 12
glossary_order = json.loads((PROJECT / "GLOSSARY-ORDER.json").read_text(encoding="utf-8"))
rendered = re.findall(r"(?m)\\glossentry\{([^}]+)\}", read("slc-screen.gls"))
assert len(rendered) == len(set(rendered)) == 79
assert rendered == glossary_order["keys"], rendered
log = read("slc-screen.log")
assert not re.search(r"Missing character:|multiply defined|undefined (?:references|citations)|(?:Reference|Citation) [^\n]* undefined|requested but not marked bn", log, re.I)
aux = read("slc-screen.aux")
labels = re.findall(r"(?m)^\\newlabel\{([^}]+)\}", aux)
assert len(labels) == len(set(labels)), "duplicate labels"
conditional = []
for relative in sorted(expected):
    source_text = (locale / relative).read_text(encoding="utf-8")
    calls = re.findall(r"\\olfileid\[bn\]\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", source_text)
    if len(calls) != 2 or {call[0] for call in calls} != {"fol", "pl"}:
        continue
    # The chapter imports these modules in first-order mode. Opening a
    # file and then silently skipping it is not an adequate import check.
    if not re.search(r"(?m)^[ \t]*\\olsection\b", source_text):
        continue
    label = ":".join(next(c for c in calls if c[0] == "fol")) + ":sec"
    assert label in labels, (relative, label)
    conditional.append(label)
assert len(conditional) >= 25
for chapter in json.loads((PROJECT / "OUTLINE.json").read_text(encoding="utf-8")):
    identifier = chapter["olchapter_id"]
    if identifier:
        expected_chapter = rf"\newlabel{{{identifier}::chap}}{{{{{chapter['id']}}}"
        assert expected_chapter in aux, expected_chapter
assert r"\bibcite" in aux and read("slc-screen.bbl").strip()
info = subprocess.check_output(["pdfinfo", str(book / "slc-screen.pdf")], text=True, encoding="utf-8")
pages = int(re.search(r"(?m)^Pages:\s*(\d+)", info)[1])
assert pages > 300
result = {"status": "passed", "native_imports": len(imports), "summaries": sorted(summaries),
          "numbered_outline": chapter_numbers, "glossary_entries": len(rendered), "labels": len(labels), "pages": pages,
          "conditional_section_labels": len(conditional),
          "pdf_sha256": sha256((book / "slc-screen.pdf").read_bytes()).hexdigest()}
(book / "inventory.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
