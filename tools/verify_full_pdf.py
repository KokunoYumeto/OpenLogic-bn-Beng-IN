"""Issue a full-edition PDF QA receipt only after build and visual evidence agree.

The guarded Windows build owns TeX/BibTeX. This verifier is read-only until all
checks pass; only then does it write the receipt consumed by the release packager.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build" / "full-edition"
BASE = "openlogic-bn-Beng-IN-complete"
PDF = BUILD / f"{BASE}.pdf"
TEX = BUILD / f"{BASE}.tex"
LOG = BUILD / f"{BASE}.log"
BBL = BUILD / f"{BASE}.bbl"
ATTEMPT = BUILD / "latest-attempt.json"
PREPARATION = BUILD / "PREPARATION.json"
OUTPUT = BUILD / "PDF_QA.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"PDF QA rejected: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command_text(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True).stdout.decode(
        "utf-8", errors="replace"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--visual-qa", type=Path, required=True,
                        help="saved manual page-inspection record for this exact PDF")
    args = parser.parse_args()

    attempt = json.loads(ATTEMPT.read_text(encoding="utf-8"))
    require(attempt.get("status") == "completed", "latest guarded build did not complete")
    require(attempt.get("acquired") is True, "latest guarded build did not acquire the TeX slot")
    require(attempt.get("mutex") == r"Global\InterlanguageTeXSlotV1", "unexpected TeX mutex")
    preparation = json.loads(PREPARATION.read_text(encoding="utf-8"))
    require(preparation["source_units"] == 722, "prepared input is not the 722-unit edition")
    tex_hash = sha256(TEX)
    require(preparation["tex"]["sha256"] == tex_hash, "prepared TeX changed after preparation")
    require(attempt["input_sha256"] == tex_hash, "guarded build used a different TeX input")
    build = attempt.get("build", {})
    passes = build.get("passes", [])
    require(len(passes) >= 3 and all(p.get("exit_code") == 0 for p in passes),
            "TeX passes did not finish successfully")
    require(build.get("stable_pdf_between_passes") is True, "PDF did not converge")
    require(passes[-1]["pdf_sha256"] == passes[-2]["pdf_sha256"],
            "last two PDF passes have different hashes")
    require(build.get("bibtex", {}).get("exit_code") == 0, "BibTeX did not finish successfully")
    pdf_hash = sha256(PDF)
    require(passes[-1]["pdf_sha256"] == pdf_hash, "PDF changed after the guarded build")

    log = LOG.read_text(encoding="utf-8", errors="replace")
    require(not re.search(r"(?m)^! ", log), "TeX log contains an error")
    require(not re.search(r"(?:Reference|Citation) `[^'\n]+' on page [^\n]*undefined", log),
            "TeX log contains an undefined reference or citation")
    require("There were undefined references" not in log, "TeX log reports undefined references")
    require("Rerun to get cross-references right" not in log,
            "cross-references still require another pass")
    info = command_text("pdfinfo", str(PDF))
    page_match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", info)
    require(page_match is not None, "pdfinfo did not report a page count")
    pages = int(page_match.group(1))
    require(pages > 0, "PDF has no pages")
    require("(A4)" in info and "Encrypted:       no" in info,
            "PDF page size or encryption differs from the edition")
    log_pages = re.search(r"Output written on [^\n]+\.pdf \((\d+) pages\)\.", log)
    require(log_pages is not None and int(log_pages.group(1)) == pages,
            "PDF page count differs from the completed TeX log")
    require(BBL.exists() and re.search(r"\\bibitem(?:\[[^]]+\])?\{", BBL.read_text(encoding="utf-8")),
            "BibTeX bibliography is absent or empty")

    fonts = command_text("pdffonts", str(PDF)).splitlines()[2:]
    font_rows = [line for line in fonts if re.search(r"\s+(?:yes|no)\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$", line)]
    require(font_rows, "pdffonts returned no font rows")
    unembedded = [line for line in font_rows if re.search(r"\s+no\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$", line)]
    require(not unembedded, "PDF contains an unembedded font")
    missing_characters = sorted(set(re.findall(r"Missing character: There is no (.*?) in font", log)))

    visual_path = args.visual_qa.resolve()
    require(visual_path.is_relative_to(REPO), "visual inspection record is outside the repository")
    visual = json.loads(visual_path.read_text(encoding="utf-8"))
    require(visual.get("schema") == "openlogic-bn-full-pdf-visual-qa/1"
            and visual.get("status") == "passed"
            and visual.get("pdf_sha256") == pdf_hash,
            "visual inspection does not attest this exact PDF")
    require(all(type(p) is int and 1 <= p <= pages for p in visual.get("pages_checked", [])),
            "visual inspection contains an invalid page number")
    checked = sorted(set(visual.get("pages_checked", [])))
    require(len(checked) >= 10 and checked[0] == 1 and checked[-1] == pages
            and any(abs(p - pages // 2) <= 10 for p in checked),
            "visual inspection needs first, middle, last and at least ten distinct pages")
    require(set(visual.get("content_types", [])) >=
            {"cover", "contents", "math", "diagram", "proof", "bibliography", "final"},
            "visual inspection is missing a required content type")
    require(set(visual.get("reviewed_missing_characters", [])) == set(missing_characters),
            "missing-glyph warnings need exact visual review")

    receipt = {
        "schema": "openlogic-bn-full-pdf-qa/1",
        "status": "passed",
        "source_units": 722,
        "pdf_bytes": PDF.stat().st_size,
        "pdf_sha256": pdf_hash,
        "pages": pages,
        "page_size": "A4",
        "embedded_fonts": len(font_rows),
        "unembedded_fonts": 0,
        "tex_input_sha256": tex_hash,
        "tex_passes": len(passes),
        "bibtex_exit_code": 0,
        "missing_character_warnings_reviewed": missing_characters,
        "visual_qa_path": visual_path.relative_to(REPO).as_posix(),
        "visual_qa_sha256": sha256(visual_path),
    }
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT)
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == "__main__":
    main()
