"""Build and audit the 299-unit Bengali semantic HTML and EPUB3 reader.

This pipeline deliberately does not invoke a TeX engine.  It evaluates the
OpenLogic full-edition selectors, linearizes proof trees and tableaux for
reflow, normalizes project math macros to ordinary TeX understood by Pandoc,
and packages the resulting native MathML in a deterministic EPUB3.
"""

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import html
import json
import re
import shutil
import subprocess
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from bs4 import BeautifulSoup, NavigableString
from lxml import etree


REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build" / "cumulative-reader"
UNPACKED = BUILD / "epub-unpacked"
HTML_OUTPUT = BUILD / "openlogic-bn-Beng-IN-through-representability.html"
EPUB_OUTPUT = BUILD / "openlogic-bn-Beng-IN-through-representability.epub"
STATUS_PATH = REPO / "evidence" / "DRAFT_STATUS.json"
MANIFEST_PATH = REPO / "evidence" / "FULL_SOURCE_MANIFEST.jsonl"
CONFIG_PATH = REPO / "upstream" / "open-logic-config.sty"
BIB_PATH = REPO / "upstream" / "bib" / "open-logic.bib"
FONT_REGULAR = REPO / "fonts" / "NotoSerifBengali-Regular.ttf"
FONT_BOLD = REPO / "fonts" / "NotoSerifBengali-Bold.ttf"
FONT_LICENSE = REPO / "fonts" / "Noto-fonts-LICENSE.txt"

LANGUAGE = "bn-Beng-IN"
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
MANIFEST_SHA256 = "5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155"
MODIFIED = "2026-09-17T00:00:00Z"
EXPECTED_UNITS = [*(f"OLP-{number:04d}" for number in range(4, 301)), "OLP-0719", "OLP-0721"]
EXPECTED_UNIT_COUNT = 299
EXPECTED_UNTRANSLATED = 423
EXPECTED_EPUBCHECK_VERSION = "5.3.0"
EXPECTED_EPUBCHECK_JAR_SHA256 = "f7f96617c929371821609b88c8484d6dc9f24fe916499863c46094c5fb778a65"
FIXED_ZIP_TIME = (2026, 9, 17, 0, 0, 0)

XHTML_NS = "http://www.w3.org/1999/xhtml"
MATHML_NS = "http://www.w3.org/1998/Math/MathML"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"
DC_NS = "http://purl.org/dc/elements/1.1/"
CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"
XML_NS = "http://www.w3.org/XML/1998/namespace"

FONT_HASHES = {
    "NotoSerifBengali-Regular.ttf": "04935aea18655c451d05b1d4bb5bdc835226a221663f89a2ecfbcfdc4483e399",
    "NotoSerifBengali-Bold.ttf": "f752131cd292f3e0fd7a25c8fc86f5424062bc06e29f6dfadcb3c09ff4881dd0",
    "Noto-fonts-LICENSE.txt": "0dab92d0544f7b233403f14b84a663bdbfa746982eda629e7f4f9ffe1b036feb",
}

TRUE_TAGS = {
    "prvNot", "prvOr", "prvAnd", "prvIf", "prvFalse", "prvEx", "prvAll",
    "prvBox", "prvDiamond", "defIff", "defTrue", "probAnd", "probIf",
    "probAll", "probDiamond", "limitClause", "tagTrue", "TMs", "lambda",
    "prfSC", "prfND", "prfAX", "prfTab", "FOL", "cmplCCS", "cmplMCS",
    "novice", "math", "compsci", "phil", "olphotos", "olphotos-lowres",
}
FALSE_TAGS = {
    "prvIff", "prvTrue", "defNot", "defOr", "defAnd", "defIf", "defFalse",
    "defEx", "defAll", "defBox", "defDiamond", "probNot", "probOr",
    "probIff", "probEx", "probBox",
}

TOKEN_TRANSLATIONS = {
    "formula": "সূত্র",
    "derivation": "নিষ্পাদন",
    "sentence": "বাক্য",
    "structure": "গঠন",
    "element": "উপাদান",
    "tableau": "ট্যাবলো",
    "constant": "ধ্রুবক সংকেত",
    "variable": "চলরাশি",
    "enumerable": "তালিকায়নযোগ্য",
    "predicate": "বিধেয় সংকেত",
    "surjective": "সমাপতিত",
    "function": "অপেক্ষক সংকেত",
    "domain": "সংজ্ঞাক্ষেত্র",
    "valuation": "সত্যমান-আরোপ",
    "signed formula": "চিহ্নিত সূত্র",
    "derive": "নিষ্পাদন",
    "nonenumerable": "অতালিকায়নযোগ্য",
    "complete": "পূর্ণ",
    "bijection": "একৈক সমাপতিত অপেক্ষক",
    "undischarged": "অনবমুক্ত",
    "injective": "একৈক",
    "language": "ভাষা",
    "derivable": "নিষ্পাদনযোগ্য",
    "decidable": "নির্ণেয়",
    "subformula": "উপসূত্র",
    "main operator": "প্রধান অপারেটর",
    "represents": "উপস্থাপন করে",
    "denumerable": "অসীম গণনীয়",
    "derivability": "নিষ্পাদনযোগ্যতা",
    "injection": "একৈক অপেক্ষক",
    "discharged": "অবমুক্ত",
    "value": "মান",
    "axiomatizable": "স্বতঃসিদ্ধযোগ্য",
    "surjection": "সমাপতিত অপেক্ষক",
    "bijective": "একৈক সমাপতিত",
    "identity": "অভিন্নতার বিধেয়",
    "propositional variable": "বচনচল",
    "operator": "যৌক্তিক অপারেটর",
    "biconditional": "দ্বিশর্তবচন",
    "conditional": "শর্তবচন",
    "free for": "মুক্তভাবে প্রতিস্থাপনযোগ্য",
    "falsity": "মিথ্যাত্ব",
    "truth": "সত্যত্ব",
    "discharge": "অবমুক্ত করা",
    "main": "প্রধান",
    "nonderivability": "অনিষ্পাদনযোগ্যতা",
    "c.e.": "c.e.",
    "computably enumerable": "গণনসাধ্যভাবে তালিকায়নযোগ্য",
    "propositional": "বচনমূলক",
    "axiomatizability": "স্বতঃসিদ্ধযোগ্যতা",
}

FORMULA_METAVARS = {
    "A": r"\varphi", "B": r"\psi", "C": r"\chi", "D": r"\theta",
    "E": r"\alpha", "F": r"\beta", "G": r"\gamma", "H": r"\delta",
    "K": r"\xi", "L": r"\zeta", "O": r"\omega", "R": r"\rho",
    "S": r"\sigma", "T": r"\tau",
}

ENV_NAMES = {
    "defn": "সংজ্ঞা", "defish": "সংজ্ঞাসদৃশ মন্তব্য", "ex": "উদাহরণ",
    "prop": "প্রতিজ্ঞা", "thm": "উপপাদ্য", "lem": "সহায়ক উপপাদ্য",
    "cor": "অনুসিদ্ধান্ত", "prob": "অনুশীলনী", "rem": "মন্তব্য",
}
NUMBERED_ENVS = set(ENV_NAMES)

ASSET_DESCRIPTIONS = {
    "union.tikz": "দুটি সেটের সংযোগ: অন্তত একটি সেটে থাকা সমগ্র অঞ্চল চিহ্নিত।",
    "intersection.tikz": "দুটি সেটের ছেদ: উভয় সেটের সাধারণ অঞ্চল চিহ্নিত।",
    "difference.tikz": "সেটের অন্তর: প্রথম সেটে আছে কিন্তু দ্বিতীয়টিতে নেই এমন অঞ্চল চিহ্নিত।",
    "function.tikz": "অপেক্ষক: সংজ্ঞাক্ষেত্রের প্রত্যেক উপাদান থেকে সহসংজ্ঞাক্ষেত্রের ঠিক একটি উপাদানে তির যায়।",
    "surjective.tikz": "সমাপতিত অপেক্ষক: সহসংজ্ঞাক্ষেত্রের প্রত্যেক উপাদানে অন্তত একটি তির পৌঁছায়।",
    "injective.tikz": "একৈক অপেক্ষক: ভিন্ন ইনপুটের তির ভিন্ন আউটপুটে পৌঁছায়।",
    "bijective.tikz": "একৈক সমাপতিত অপেক্ষক: সহসংজ্ঞাক্ষেত্রের প্রত্যেক উপাদানে ঠিক একটি তির পৌঁছায়।",
    "composition.tikz": "অপেক্ষকের মিশ্রণ: প্রথমে f দিয়ে A থেকে B-তে, পরে g দিয়ে B থেকে C-তে যাওয়া; সরাসরি মানচিত্রটি g বৃত্ত f।",
    "turing-machine.tikz": "টুরিং যন্ত্রের ধারণামূলক চিত্র: দ্বিমুখী অসীম টেপের ঘর, পাঠ-লেখ মস্তক, সসীম অবস্থা-নিয়ন্ত্রণ এবং প্রতি ধাপে লেখা, চলন ও অবস্থা-বদল।",
}

CSS = r"""
@font-face{font-family:BN;src:url('../fonts/NotoSerifBengali-Regular.ttf') format('truetype');font-weight:400;font-style:normal}
@font-face{font-family:BN;src:url('../fonts/NotoSerifBengali-Bold.ttf') format('truetype');font-weight:700;font-style:normal}
:root{color-scheme:light}
html{background:#f3f1ed;color:#17232c}
body{max-width:58rem;margin:2rem auto;padding:2.5rem;background:#fff;font-family:BN,"Noto Serif Bengali",serif;font-size:18px;line-height:1.82}
header{border-bottom:2px solid #78909c;margin-bottom:2rem;padding-bottom:1.4rem}
h1,h2,h3,h4{line-height:1.45;break-after:avoid} h1{margin-top:2.8rem} h2{margin-top:2.2rem}
a{color:#155c89} code,pre{font-family:ui-monospace,Consolas,monospace;font-size:.88em}
math{font-family:"Cambria Math","STIX Two Math",math} mtext{font-family:BN,"Noto Serif Bengali",serif;font-style:normal} math[display="block"]{display:block;overflow-x:auto;padding:.65rem 0}
table{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto} th,td{border:1px solid #bbb;padding:.35rem .55rem;vertical-align:top}
nav#TOC{border:1px solid #c8cdd0;background:#fafafa;padding:1rem 1.3rem;margin:1.5rem 0 2rem}
.scope-note,.translationnote,.editorial,.display-prose,.diagram-semantic,.proof-tree-semantic,.tableau-semantic,.derivation-semantic{background:#eef4f6;border-left:4px solid #78909c;padding:.7rem 1rem;margin:1.2rem 0}
.defn,.defish,.ex,.prop,.thm,.lem,.cor,.prob,.rem{border-left:3px solid #78909c;padding:.35rem 1rem;margin:1.25rem 0}
.proof{padding:.2rem 1rem;margin:1rem 0}.environment-title{margin:.1rem 0 .5rem}.unit-marker{color:#53636d;font-family:ui-monospace,Consolas,monospace;font-size:.76em;letter-spacing:.04em;margin:1.4rem 0 .2rem}
.proof-tree-semantic li,.tableau-semantic li,.derivation-semantic li{margin:.35rem 0}.outside-ref{color:#5a6268}.license-text{white-space:pre-wrap;font-size:.72em;line-height:1.45}
.diagram-semantic ul{margin-bottom:.2rem}.source-correction{border-left-color:#b06b36}
@media(max-width:680px){body{margin:0;padding:1rem;font-size:17px}h1{font-size:1.72em}h2{font-size:1.38em}}
@media print{html{background:#fff}body{margin:0;max-width:none;padding:0;font-size:11pt}nav#TOC{break-after:page}}
""".strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def safe_clear(path: Path) -> None:
    resolved = path.resolve()
    root = BUILD.resolve()
    require(resolved != root and resolved.is_relative_to(root), f"unsafe build path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def strip_comments(value: str) -> str:
    lines: list[str] = []
    for line in value.splitlines():
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                slashes += 1
                cursor -= 1
            if slashes % 2 == 0:
                cut = index
                break
        lines.append(line[:cut])
    return "\n".join(lines)


def skip_space(value: str, position: int) -> int:
    while position < len(value) and value[position].isspace():
        position += 1
    return position


def parse_delimited(value: str, position: int, opening: str, closing: str) -> tuple[str, int]:
    position = skip_space(value, position)
    if position >= len(value) or value[position] != opening:
        raise ValueError(f"expected {opening!r} at {position}: {value[position:position + 100]!r}")
    start = position + 1
    depth = 1
    position += 1
    while position < len(value) and depth:
        char = value[position]
        slash_count = 0
        slash_position = position - 1
        while slash_position >= 0 and value[slash_position] == "\\":
            slash_count += 1
            slash_position -= 1
        escaped = slash_count % 2 == 1
        if not escaped and char == opening:
            depth += 1
        elif not escaped and char == closing:
            depth -= 1
        position += 1
    if depth:
        raise ValueError(f"unterminated {opening}{closing} group starting at {start - 1}")
    return value[start:position - 1], position


def parse_required(value: str, position: int) -> tuple[str, int]:
    position = skip_space(value, position)
    if position >= len(value):
        raise ValueError("missing required TeX argument")
    if value[position] == "{":
        return parse_delimited(value, position, "{", "}")
    if value[position] == "$":
        delimiter = "$$" if value.startswith("$$", position) else "$"
        cursor = position + len(delimiter)
        while True:
            end = value.find(delimiter, cursor)
            if end < 0:
                raise ValueError(f"unterminated math argument starting at {position}")
            slash_count = 0
            slash_position = end - 1
            while slash_position >= 0 and value[slash_position] == "\\":
                slash_count += 1
                slash_position -= 1
            if slash_count % 2 == 0:
                end += len(delimiter)
                return value[position:end], end
            cursor = end + len(delimiter)
    if value[position] == "\\":
        match = re.match(r"\\(?:[A-Za-z@]+|.)", value[position:])
        require(match is not None, "invalid control sequence argument")
        return match.group(0), position + len(match.group(0))
    return value[position], position + 1


def parse_optional(value: str, position: int) -> tuple[str | None, int]:
    cursor = skip_space(value, position)
    if cursor < len(value) and value[cursor] == "[":
        return parse_delimited(value, cursor, "[", "]")
    return None, position


def replace_macro(value: str, name: str, callback) -> str:
    pattern = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z@])")
    output: list[str] = []
    cursor = 0
    while True:
        match = pattern.search(value, cursor)
        if not match:
            output.append(value[cursor:])
            return "".join(output)
        output.append(value[cursor:match.start()])
        replacement, end = callback(value, match.end())
        output.append(replacement)
        cursor = end


def tag_enabled(expression: str) -> bool:
    tags = [part.strip() for part in expression.split(",") if part.strip()]
    for tag in tags:
        if tag.startswith("not") and tag[3:] in TRUE_TAGS | FALSE_TAGS:
            if tag[3:] in FALSE_TAGS:
                return True
        elif tag in TRUE_TAGS:
            return True
    return False


def replace_three_argument_choice(value: str, name: str, choice) -> str:
    def callback(source: str, position: int) -> tuple[str, int]:
        first, position = parse_required(source, position)
        second, position = parse_required(source, position)
        third, position = parse_required(source, position)
        return choice(first, second, third), position

    return replace_macro(value, name, callback)


def evaluate_selectors(value: str, known_labels: set[str]) -> str:
    def iftag(source: str, position: int) -> tuple[str, int]:
        tags, position = parse_required(source, position)
        yes, position = parse_required(source, position)
        cursor = skip_space(source, position)
        if cursor < len(source) and source[cursor] == "{":
            no, position = parse_required(source, position)
        else:
            no = ""
        return (yes if tag_enabled(tags) else no), position

    previous = None
    while previous != value:
        previous = value
        value = replace_macro(value, "iftag", iftag)
        value = replace_three_argument_choice(
            value, "oliflabeldef", lambda label, yes, no: yes if label in known_labels else no
        )

    def tagitem(source: str, position: int) -> tuple[str, int]:
        tags, position = parse_required(source, position)
        yes, position = parse_required(source, position)
        no, position = parse_required(source, position)
        selected = yes if tag_enabled(tags) else no
        return ("\\item " + selected) if selected.strip() else "", position

    value = replace_macro(value, "tagitem", tagitem)

    def tagrefs(source: str, position: int) -> tuple[str, int]:
        pairs, position = parse_required(source, position)
        labels = []
        for pair in re.split(r",\s*", pairs):
            if "/" not in pair:
                continue
            tag, label = pair.split("/", 1)
            label = label.strip().strip("{}")
            if tag_enabled(tag):
                labels.append(label)
        if not labels:
            return "বর্তমান বিন্যাসের প্রাসঙ্গিক ফলাফল", position
        links = [rf"\hyperlink{{{label}}}{{প্রাসঙ্গিক ফলাফল}}" for label in labels]
        return ", ".join(links), position

    value = replace_macro(value, "tagrefs", tagrefs)
    value = re.sub(r"\\begin\{tagenumerate\}\{[^{}]*\}", r"\\begin{enumerate}", value)
    value = value.replace(r"\end{tagenumerate}", r"\end{enumerate}")

    tagblock = re.compile(r"\\begin\{tagblock\}\{([^{}]+)\}(.*?)\\end\{tagblock\}", re.S)
    while tagblock.search(value):
        value = tagblock.sub(lambda match: match.group(2) if tag_enabled(match.group(1)) else "", value)

    def tagged_problem(match: re.Match[str]) -> str:
        outer = match.group(1) or "tagTrue"
        inner = match.group(2)
        body = match.group(3)
        return body if tag_enabled(outer) and not tag_enabled(inner) else ""

    value = re.sub(
        r"\\tagprob(?:\[([^\]]+)\])?\{([^{}]+)\}(.*?)\\tagendprob",
        tagged_problem,
        value,
        flags=re.S,
    )
    value = re.sub(r"\\tag(?:true|false)\{[^{}]*\}", "", value)
    value = re.sub(r"\\begin\{probtag\}\{[^{}]*\}", r"\\begin{prob}", value)
    value = value.replace(r"\end{probtag}", r"\end{prob}")
    return value


TOKEN_SUFFIXES = (
    "x-এর", "-এরও", "-গুলিকে", "-গুলির", "-গুলি", "-কেই", "-কেও",
    "-টিকে", "-টিতে", "-টিই", "-টিও", "-টির", "-তেই", "-তেও",
    "-এও", "-এর", "-কে", "-তে", "-টি", "-ই", "-ও", "-র", "-এ",
    "ted", "d", "ের", "কে",
)


def token_genitive(term: str) -> str:
    if term[-1:] in {"া", "ি", "ী", "ু", "ূ", "ৃ", "ে", "ৈ", "ো", "ৌ"}:
        return term + "র"
    return term + "ের"


def token_locative(term: str) -> str:
    if term.endswith("া"):
        return term + "য়"
    if term[-1:] in {"ি", "ী", "ু", "ূ", "ৃ", "ে", "ৈ", "ো", "ৌ"}:
        return term + "তে"
    return term + "ে"


def inflect_token(term: str, plural: bool, suffix: str, key: str = "") -> str:
    """Join OpenLogic's English-oriented token suffixes as natural Bengali."""
    if suffix == "ted" and key == "formula":
        return "সূত্রবদ্ধ"
    if suffix == "d" and key == "derive":
        return "নিষ্পাদিত"
    if suffix == "x-এর" and key == "tableau":
        return term + "গুলির"

    if suffix.startswith("-গুলি"):
        plural = True
        suffix = suffix[len("-গুলি"):]
        suffix = {"": "", "র": "-এর", "কে": "-কে"}.get(suffix, suffix)

    stem = term + ("গুলি" if plural else "")
    if suffix in {"-এর", "-র", "ের"}:
        return term + "গুলির" if plural else token_genitive(term)
    if suffix == "-এরও":
        return (term + "গুলির" if plural else token_genitive(term)) + "ও"
    if suffix in {"-কে", "কে"}:
        return stem + "কে"
    if suffix == "-কেই":
        return stem + "কেই"
    if suffix == "-কেও":
        return stem + "কেও"
    if suffix in {"-এ", "-তে"}:
        return term + "গুলিতে" if plural else token_locative(term)
    if suffix in {"-এও", "-তেও"}:
        return (term + "গুলিতে" if plural else token_locative(term)) + "ও"
    if suffix == "-তেই":
        return (term + "গুলিতে" if plural else token_locative(term)) + "ই"
    if suffix in {"-টি", "-টির", "-টিকে", "-টিতে", "-টিই", "-টিও"}:
        return stem + suffix[1:]
    if suffix == "-ই":
        return stem + "ই"
    if suffix == "-ও":
        return stem + "ও"
    return stem + suffix


def replace_tokens(value: str) -> str:
    suffix_pattern = "|".join(re.escape(item) for item in TOKEN_SUFFIXES)
    pattern = re.compile(r"!!(\^)?(a)?\{([^{}]+)\}(s)?(" + suffix_pattern + r")?")

    def token(match: re.Match[str]) -> str:
        key = " ".join(match.group(3).split())
        require(key in TOKEN_TRANSLATIONS, f"unmapped OpenLogic text token: {key!r}")
        term = inflect_token(
            TOKEN_TRANSLATIONS[key],
            bool(match.group(4)) and key not in {"c.e."},
            match.group(5) or "",
            key,
        )
        if match.group(2):
            term = "একটি " + term
        return term

    value = pattern.sub(token, value)
    value = value.replace("নিষ্পাদিত করা", "নিষ্পাদন করা")
    require("!!" not in value, "unexpanded OpenLogic token remains")
    return value


def normalize_bengali_token_suffixes(value: str) -> str:
    r"""Normalize suffixes that follow ``\printtoken``/``\usetoken`` macros."""
    suffix_pattern = "|".join(
        re.escape(item) for item in TOKEN_SUFFIXES if item not in {"ted", "d", "x-এর", "ের", "কে"}
    )
    for term in sorted(set(TOKEN_TRANSLATIONS.values()), key=len, reverse=True):
        pattern = re.compile(re.escape(term) + r"(গুলি)?(" + suffix_pattern + r")")
        value = pattern.sub(
            lambda match: inflect_token(term, bool(match.group(1)), match.group(2)),
            value,
        )
    return value


def literalize_string_commands(value: str) -> str:
    r"""Render TeX ``\string\command`` examples without executing them."""
    delimiter = re.compile(r"(?<!\\)(?:\$\$|\$)")
    command = re.compile(r"\\string\\([A-Za-z@]+)")
    output: list[str] = []
    cursor = 0
    in_dollar_math = False
    for match in delimiter.finditer(value):
        segment = value[cursor:match.start()]
        if in_dollar_math:
            segment = command.sub(
                lambda item: r"\backslash\mathrm{" + item.group(1) + "}",
                segment,
            )
        else:
            segment = command.sub(
                lambda item: r"\textbackslash{}" + item.group(1),
                segment,
            )
        output.extend((segment, match.group(0)))
        in_dollar_math = not in_dollar_math
        cursor = match.end()
    tail = value[cursor:]
    replacement = (
        (lambda item: r"\backslash\mathrm{" + item.group(1) + "}")
        if in_dollar_math
        else (lambda item: r"\textbackslash{}" + item.group(1))
    )
    output.append(command.sub(replacement, tail))
    result = "".join(output)
    require("\\string\\" not in result, "unexpanded TeX string command remains")
    return result


def replace_formula_metavariables(value: str) -> str:
    def formula(source: str, position: int) -> tuple[str, int]:
        argument, position = parse_required(source, position)
        key = argument.strip()
        return FORMULA_METAVARS.get(key, key), position

    value = replace_macro(value, "formula", formula)
    return re.sub(r"!([A-Z])", lambda match: FORMULA_METAVARS.get(match.group(1), match.group(1)), value)


def extract_environment(value: str, start: int, name: str) -> tuple[str, int]:
    begin_pattern = re.compile(r"\\begin\{" + re.escape(name) + r"\}")
    end_pattern = re.compile(r"\\end\{" + re.escape(name) + r"\}")
    cursor = start
    depth = 1
    while depth:
        begin = begin_pattern.search(value, cursor)
        end = end_pattern.search(value, cursor)
        if end is None:
            raise ValueError(f"unterminated {name} environment")
        if begin is not None and begin.start() < end.start():
            depth += 1
            cursor = begin.end()
        else:
            depth -= 1
            if depth == 0:
                return value[start:end.start()], end.end()
            cursor = end.end()
    raise AssertionError("unreachable")


def transform_environments(value: str, name: str, callback) -> tuple[str, int]:
    pattern = re.compile(r"\\begin\{" + re.escape(name) + r"\}")
    output: list[str] = []
    cursor = 0
    count = 0
    while True:
        match = pattern.search(value, cursor)
        if not match:
            output.append(value[cursor:])
            return "".join(output), count
        output.append(value[cursor:match.start()])
        body, end = extract_environment(value, match.end(), name)
        output.append(callback(body, count))
        count += 1
        cursor = end


def ensure_math(value: str) -> str:
    stripped = value.strip()
    if stripped.startswith("$") and stripped.endswith("$"):
        return stripped
    return f"${stripped}$"


def transform_proof_trees(value: str) -> tuple[str, int]:
    command_pattern = re.compile(
        r"\\(AxiomC|Axiom|UnaryInfC|UnaryInf|BinaryInfC|BinaryInf|TrinaryInfC|TrinaryInf|DeduceC|Deduce|RightLabel|insertBetweenHyps)\b"
    )

    def convert(body: str, index: int) -> str:
        lines: list[tuple[str, str]] = []
        pending_rule = ""
        cursor = 0
        for match in command_pattern.finditer(body):
            if match.start() < cursor:
                continue
            name = match.group(1)
            try:
                argument, end = parse_required(body, match.end())
            except ValueError:
                continue
            cursor = end
            if name == "RightLabel":
                pending_rule = argument.strip().strip("$")
                continue
            if name == "insertBetweenHyps":
                lines.append(("মধ্যবর্তী টীকা", argument))
                continue
            kind = "অনুমান" if name.startswith("Axiom") else "সিদ্ধান্ত"
            if pending_rule:
                kind += f"; বিধি: ${pending_rule}$"
                pending_rule = ""
            lines.append((kind, argument))
        require(lines, f"empty proof tree {index + 1}")
        items = "\n".join(rf"\item \textbf{{{kind}:}} {ensure_math(formula)}" for kind, formula in lines)
        return (
            "\n\\begin{proof-tree-semantic}\n"
            "\\textbf{প্রমাণ-বৃক্ষের রৈখিক পাঠ}\n"
            "\\begin{enumerate}\n" + items + "\n\\end{enumerate}\n"
            "\\end{proof-tree-semantic}\n"
        )

    value, count = transform_environments(value, "prooftree", convert)
    standalone = re.compile(
        r"\\(?:AxiomC?|UnaryInfC?|BinaryInfC?|TrinaryInfC?|DeduceC?)\b.*?\\DisplayProof\b",
        re.S,
    )
    while True:
        match = standalone.search(value)
        if not match:
            break
        replacement = convert(match.group(0), count)
        value = value[: match.start()] + replacement + value[match.end() :]
        count += 1
    value = re.sub(
        r"\\\[\s*(\\begin\{proof-tree-semantic\}.*?\\end\{proof-tree-semantic\})\s*\\\]",
        r"\1",
        value,
        flags=re.S,
    )
    value = value.replace(r"\DisplayProof", "")
    return value, count


def transform_tableaux(value: str) -> tuple[str, int]:
    total = 0
    for environment in ("oltableau", "tableau"):
        def convert(body: str, index: int, environment: str = environment) -> str:
            entries: list[str] = []
            position = 0
            while True:
                match = re.search(r"\\sFmla(?![A-Za-z@])", body[position:])
                if not match:
                    break
                start = position + match.start()
                cursor = position + match.end()
                sign, cursor = parse_required(body, cursor)
                formula, cursor = parse_required(body, cursor)
                optional, cursor = parse_optional(body, cursor)
                next_match = re.search(r"\\sFmla(?![A-Za-z@])", body[cursor:])
                end = cursor + next_match.start() if next_match else len(body)
                suffix = body[cursor:end]
                prefix = body[:start]
                depth = max(1, prefix.count("[") - prefix.count("]"))
                justification = ""
                just_match = re.search(r"just\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\\[A-Za-z@]+)", suffix, re.S)
                if just_match:
                    justification = just_match.group(1).strip().strip("{}")
                closed = bool(re.search(r"\bclose\b", suffix))
                detail = rf"শাখা-স্তর {depth}: ${sign}\;{formula}$"
                if optional:
                    detail += rf" (পংক্তি ${optional}$)"
                if justification:
                    detail += rf"; কারণ ${justification}$"
                if closed:
                    detail += "; শাখা বন্ধ"
                entries.append(detail)
                position = cursor
            require(entries, f"empty {environment} environment {index + 1}")
            items = "\n".join(rf"\item {entry}" for entry in entries)
            return (
                "\n\\begin{tableau-semantic}\n"
                "\\textbf{ট্যাবলোর পুনঃপ্রবাহযোগ্য শাখা-পাঠ}\n"
                "\\begin{enumerate}\n" + items + "\n\\end{enumerate}\n"
                "\\end{tableau-semantic}\n"
            )

        value, count = transform_environments(value, environment, convert)
        total += count
    return value, total


def split_tex_rows(body: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<!\\)\\\\(?:\[[^\]]*\])?", body) if part.strip()]


def transform_derivations(value: str) -> tuple[str, int]:
    def convert(body: str, index: int) -> str:
        items = []
        for row in split_tex_rows(body):
            cells = [cell.strip() for cell in row.split("&")]
            cells = [cell for cell in cells if cell]
            if not cells:
                continue
            items.append("; ".join(cells))
        require(items, f"empty derivation environment {index + 1}")
        return (
            "\n\\begin{derivation-semantic}\n"
            "\\textbf{নিষ্পাদনের পংক্তিসমূহ}\n\\begin{enumerate}\n"
            + "\n".join(rf"\item {item}" for item in items)
            + "\n\\end{enumerate}\n\\end{derivation-semantic}\n"
        )

    return transform_environments(value, "derivation", convert)


def clean_tikz_text(value: str) -> str:
    value = re.sub(r"\\(?:node|path|draw|coordinate)\b", "", value)
    value = re.sub(r"\\(?:Large|large|small|scriptsize|tiny|normalsize)\b", "", value)
    value = re.sub(r"\[[^\]]*\]", "", value)
    value = value.replace(";", " ").replace("--", r" $\to$ ")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def transform_diagrams(value: str) -> tuple[str, int]:
    def convert(body: str, index: int) -> str:
        nodes: list[str] = []
        for match in re.finditer(
            r"\\(?:node|path\s+node)(?:\[[^\]]*\])?(?:\s+at)?\s*(?:\([^)]*\))?\s*\{",
            body,
        ):
            try:
                label, _ = parse_delimited(body, match.end() - 1, "{", "}")
            except ValueError:
                continue
            label = clean_tikz_text(label)
            if label:
                nodes.append(label)
        edges = []
        for match in re.finditer(r"\\(?:path|draw)\b(.*?);", body, re.S):
            if re.match(r"\s*node\b", match.group(1)):
                continue
            description = clean_tikz_text(match.group(1))
            if description:
                edges.append(description)
        entries = [f"শীর্ষ বা লেবেল: {entry}" for entry in nodes]
        entries.extend(f"সংযোগ বা নির্দেশ: {entry}" for entry in edges)
        if not entries:
            entries = ["উৎসচিত্রে কোনো পৃথক পাঠ্য-লেবেল নেই; পার্শ্ববর্তী অনুচ্ছেদ চিত্রটির গাণিতিক ভূমিকা ব্যাখ্যা করে।"]
        return (
            "\n\\begin{diagram-semantic}\n\\textbf{চিত্রের পুনঃপ্রবাহযোগ্য পাঠ্যরূপ}\n"
            "\\begin{itemize}\n"
            + "\n".join(rf"\item {entry}" for entry in entries)
            + "\n\\end{itemize}\n\\end{diagram-semantic}\n"
        )

    value, count = transform_environments(value, "tikzpicture", convert)

    def asset(source: str, position: int) -> tuple[str, int]:
        _, position_after_optional = parse_optional(source, position)
        path, end = parse_required(source, position_after_optional)
        filename = path.replace(r"\olpath/", "").replace("\\", "/").split("/")[-1]
        require(filename in ASSET_DESCRIPTIONS, f"unmapped diagram asset: {path}")
        description = ASSET_DESCRIPTIONS[filename]
        return (
            "\n\\begin{diagram-semantic}\n\\textbf{চিত্রের পুনঃপ্রবাহযোগ্য পাঠ্যরূপ}\n"
            f"{description}\n\\end{{diagram-semantic}}\n",
            end,
        )

    before = len(re.findall(r"\\olasset(?![A-Za-z@])", value))
    value = replace_macro(value, "olasset", asset)
    return value, count + before


def sanitize_display_math(value: str) -> str:
    def unwrap_text_macros(argument: str) -> str:
        def unwrap(source: str, position: int) -> tuple[str, int]:
            nested, position = parse_required(source, position)
            return nested, position

        for nested_name in ("text", "textnormal", "mbox", "emph"):
            while re.search(rf"\\{nested_name}(?![A-Za-z@])", argument):
                updated = replace_macro(argument, nested_name, unwrap)
                if updated == argument:
                    break
                argument = updated
        return argument

    def text_macro(source: str, position: int) -> tuple[str, int]:
        argument, position = parse_required(source, position)
        argument = re.sub(
            r"(?<!\\)\$(.*?)(?<!\\)\$",
            lambda match: "$" + re.sub(r"\s+", " ", match.group(1)).strip() + "$",
            argument,
            flags=re.S,
        )
        return r"\text{" + unwrap_text_macros(argument) + "}", position

    for name in ("text", "textnormal", "mbox", "emph"):
        value = replace_macro(value, name, text_macro)

    def hyperlink(source: str, position: int) -> tuple[str, int]:
        _, position = parse_required(source, position)
        label, position = parse_required(source, position)
        return r"\text{" + label + "}", position

    value = replace_macro(value, "hyperlink", hyperlink)
    # Cross-reference labels can introduce a text macro inside an existing
    # text argument.  Flatten that second-order nesting after link removal.
    for name in ("text", "textnormal", "mbox", "emph"):
        value = replace_macro(value, name, text_macro)
    value = re.sub(
        r"\\tag\{\$((?:[^$]|\\\$)*)\$\}",
        r"\\tag{\1}",
        value,
    )
    value = re.sub(r"\\centering(?![A-Za-z@])", "", value)
    return value


def normalize_display_environments(value: str) -> str:
    def convert(body: str, _index: int, environment: str) -> str:
        anchors = re.findall(r"\\hypertarget\{([^{}]+)\}\{\}", body)
        body = re.sub(r"\\hypertarget\{[^{}]+\}\{\}", "", body)
        output: list[str] = ["\n".join(rf"\hypertarget{{{label}}}{{}}" for label in anchors)]
        cursor = 0

        def append_math(fragment: str) -> None:
            fragment = fragment.strip()
            fragment = re.sub(r"^(?:\\\\\s*)+", "", fragment)
            fragment = re.sub(r"(?:\\\\\s*)+$", "", fragment)
            if not fragment or re.fullmatch(r"(?:&|\\\\|\s)*", fragment):
                return
            fragment = sanitize_display_math(fragment)
            display_environment = "multline*" if environment.startswith("multline") else "align*"
            output.append(
                f"\\begin{{{display_environment}}}\n{fragment}\n\\end{{{display_environment}}}"
            )

        event = re.compile(r"\\intertext(?![A-Za-z@])|\\begin\{diagram-semantic\}")
        while True:
            match = event.search(body, cursor)
            if not match:
                append_math(body[cursor:])
                break
            append_math(body[cursor:match.start()])
            if match.group(0).startswith(r"\intertext"):
                prose, cursor = parse_required(body, match.end())
                output.append(
                    "\\begin{display-prose}\n" + prose.strip() + "\n\\end{display-prose}"
                )
            else:
                diagram, cursor = extract_environment(
                    body, match.end(), "diagram-semantic"
                )
                output.append(
                    "\\begin{diagram-semantic}"
                    + diagram
                    + "\\end{diagram-semantic}"
                )
        return "\n\n".join(part for part in output if part.strip())

    for environment in ("align", "align*", "multline", "multline*"):
        value, _ = transform_environments(
            value,
            environment,
            lambda body, index, environment=environment: convert(
                body, index, environment
            ),
        )

    def display_block(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        if r"\begin{diagram-semantic}" in body:
            return re.sub(r"(?:^|\n)\s*\\\\\s*(?=\n|$)", "\n", body)
        if r"\begin{tabular}" in body:
            body = re.sub(r"\\centering(?![A-Za-z@])", "", body)
            return "\\begin{center}\n" + body + "\n\\end{center}"
        return match.group(0)

    value = re.sub(r"\\\[(.*?)\\\]", display_block, value, flags=re.S)
    return value


def special_math_macros(value: str) -> str:
    def quantifier(symbol: str, unique: bool = False):
        def callback(source: str, position: int) -> tuple[str, int]:
            if unique:
                cursor = skip_space(source, position)
                is_unique = cursor < len(source) and source[cursor] == "!"
                position = cursor + 1 if is_unique else position
            else:
                is_unique = False
            first, position = parse_optional(source, position)
            second, position = parse_optional(source, position)
            result = symbol + ("!" if is_unique else "")
            if first is not None:
                result += " " + first
            if second is not None:
                result += r"\," + second
            return result, position
        return callback

    value = replace_macro(value, "lexists", quantifier(r"\exists", True))
    value = replace_macro(value, "lforall", quantifier(r"\forall"))
    value = replace_macro(value, "lambd", quantifier(r"\lambda"))

    def equality(source: str, position: int) -> tuple[str, int]:
        cursor = skip_space(source, position)
        negated = cursor < len(source) and source[cursor] == "/"
        if negated:
            position = cursor + 1
        left, position = parse_optional(source, position)
        right, position = parse_optional(source, position)
        relation = r"\neq" if negated else "="
        if right is None:
            return relation, position
        return f"{left} {relation} {right}", position

    value = replace_macro(value, "eq", equality)

    def relation_macro(positive: str, negative: str):
        def callback(source: str, position: int) -> tuple[str, int]:
            cursor = skip_space(source, position)
            negated = cursor < len(source) and source[cursor] == "/"
            if negated:
                position = cursor + 1
            optional, position = parse_optional(source, position)
            result = negative if negated else positive
            if optional is not None:
                result += "_{" + optional + "}"
            return result, position
        return callback

    value = replace_macro(value, "Proves", relation_macro(r"\vdash", r"\nvdash"))
    value = replace_macro(value, "Entails", relation_macro(r"\vDash", r"\nvDash"))
    value = replace_macro(value, "elemequiv", relation_macro(r"\equiv", r"\not\equiv"))
    value = replace_macro(value, "iso", relation_macro(r"\simeq", r"\not\simeq"))

    def satisfaction(structure_style: str):
        def callback(source: str, position: int) -> tuple[str, int]:
            cursor = skip_space(source, position)
            negated = cursor < len(source) and source[cursor] == "/"
            if negated:
                position = cursor + 1
            cursor = skip_space(source, position)
            if cursor >= len(source) or source[cursor] != "{":
                return r"\operatorname{Sat}" + ("/" if negated else ""), position
            structure, position = parse_required(source, position)
            formula, position = parse_required(source, position)
            assignment, position = parse_optional(source, position)
            left = structure_style.format(structure)
            if assignment is not None:
                left += ", " + assignment
            return f"{left} {'\\\\nvDash' if negated else '\\\\vDash'} {formula}".replace("\\\\", "\\"), position
        return callback

    value = replace_macro(value, "Sat", satisfaction(r"\mathfrak{{{}}}"))
    value = replace_macro(value, "mSat", satisfaction(r"\mathfrak{{{}}}"))
    value = replace_macro(value, "pSat", satisfaction(r"\mathfrak{{{}}}"))

    def value_macro(source: str, position: int) -> tuple[str, int]:
        term, position = parse_required(source, position)
        structure, position = parse_required(source, position)
        assignment, position = parse_optional(source, position)
        subscript = "_{" + assignment + "}" if assignment is not None else ""
        return rf"\mathrm{{Val}}^{{\mathfrak{{{structure}}}}}{subscript}({term})", position

    value = replace_macro(value, "Value", value_macro)

    def var_assign(source: str, position: int) -> tuple[str, int]:
        first, position = parse_required(source, position)
        second, position = parse_required(source, position)
        variable, position = parse_required(source, position)
        obj, position = parse_optional(source, position)
        if obj is None:
            return rf"{first} \sim_{{{variable}}} {second}", position
        return rf"{first} = {second}[{obj}/{variable}]", position

    value = replace_macro(value, "varAssign", var_assign)

    def pvalue(source: str, position: int) -> tuple[str, int]:
        assignment, position = parse_required(source, position)
        cursor = skip_space(source, position)
        formula = None
        if cursor < len(source) and source[cursor] == "(":
            formula, position = parse_delimited(source, cursor, "(", ")")
        optional, position = parse_optional(source, position)
        result = rf"\overline{{\mathfrak{{{assignment}}}}}"
        if optional is not None:
            result += "_{" + optional + "}"
        if formula is not None:
            result += "(" + formula + ")"
        return result, position

    value = replace_macro(value, "pValue", pvalue)

    def one_required_optional(template):
        def callback(source: str, position: int) -> tuple[str, int]:
            argument, position = parse_required(source, position)
            optional, position = parse_optional(source, position)
            return template(argument, optional), position
        return callback

    value = replace_macro(value, "sFmla", lambda source, position: _signed_formula(source, position))
    value = replace_macro(value, "TRule", lambda source, position: _tableau_rule(source, position))
    value = replace_macro(value, "Intro", one_required_optional(lambda arg, opt: rf"{arg}\mathrm{{I}}" + (f"_{{{opt}}}" if opt else "")))
    value = replace_macro(value, "Elim", one_required_optional(lambda arg, opt: rf"{arg}\mathrm{{E}}" + (f"_{{{opt}}}" if opt else "")))
    value = replace_macro(value, "cfind", one_required_optional(lambda arg, opt: rf"\varphi_{{{arg}}}" + (f"^{{{opt}}}" if opt else "")))
    value = replace_macro(value, "eqc", one_required_optional(lambda arg, opt: f"[{arg}]" + (f"_{{{opt}}}" if opt else "")))
    value = replace_macro(value, "rep", one_required_optional(lambda arg, opt: rf"\underline{{{arg}}}" + (f"_{{{opt}}}" if opt else "")))
    value = replace_macro(value, "tf", one_required_optional(lambda arg, opt: rf"\widetilde{{{arg}}}" + (f"_{{{opt}}}" if opt else "")))
    value = replace_macro(value, "Log", one_required_optional(lambda arg, opt: rf"\mathbf{{{arg}}}" + (f"_{{{opt}}}" if opt else "")))

    def optional_operator(operator: str, style: str = "mathrm"):
        def callback(source: str, position: int) -> tuple[str, int]:
            optional, position = parse_optional(source, position)
            result = rf"\{style}{{{operator}}}"
            if optional is not None:
                result += "_{" + optional + "}"
            return result, position
        return callback

    for name, operator, style in (
        ("Prf", "Prf", "mathrm"), ("OPrf", "Prf", "mathsf"),
        ("Prov", "Prov", "mathrm"), ("OProv", "Prov", "mathsf"),
        ("OCon", "Con", "mathsf"), ("Trm", "Trm", "mathrm"),
        ("Frm", "Frm", "mathrm"), ("Sent", "Sent", "mathrm"),
    ):
        value = replace_macro(value, name, optional_operator(operator, style))

    def optional_arrow(source: str, position: int, double: bool = False) -> tuple[str, int]:
        optional, position = parse_optional(source, position)
        label = f"^{{{optional}}}" if optional else ""
        return (r"\Longrightarrow" if double else r"\longrightarrow") + label, position

    value = replace_macro(value, "redone", lambda source, pos: optional_arrow(source, pos))
    value = replace_macro(value, "red", lambda source, pos: optional_arrow(source, pos, True))
    value = replace_macro(value, "redpar", lambda source, pos: optional_arrow(source, pos, True))

    def complete_development(source: str, position: int) -> tuple[str, int]:
        optional, position = parse_optional(source, position)
        argument, position = parse_required(source, position)
        return "{" + argument + "}^{*" + ((" " + optional) if optional else "") + "}", position

    value = replace_macro(value, "cd", complete_development)

    def inject(source: str, position: int) -> tuple[str, int]:
        optional, position = parse_optional(source, position)
        branch, position = parse_required(source, position)
        argument, position = parse_required(source, position)
        result = rf"\iota_{{{branch}}}"
        if optional:
            result += "^{" + optional + "}"
        return result + f"({argument})", position

    value = replace_macro(value, "inj", inject)
    value = replace_macro(value, "Mod", _model_class)
    value = replace_macro(value, "indcase", _inductive_case)

    def bounded_quantifier(symbol: str):
        def callback(source: str, position: int) -> tuple[str, int]:
            cursor = skip_space(source, position)
            if cursor >= len(source) or source[cursor] != "{":
                return symbol, position
            bound, position = parse_required(source, position)
            cursor = skip_space(source, position)
            body = ""
            if cursor < len(source) and source[cursor] == "{":
                body, position = parse_required(source, position)
            return f"({symbol} {bound})" + (r"\; " + body if body else ""), position

        return callback

    value = replace_macro(value, "bexists", bounded_quantifier(r"\exists"))
    value = replace_macro(value, "bforall", bounded_quantifier(r"\forall"))

    def atom(source: str, position: int) -> tuple[str, int]:
        predicate, position = parse_required(source, position)
        cursor = skip_space(source, position)
        if cursor >= len(source) or source[cursor] != "{":
            return predicate, position
        arguments, position = parse_required(source, position)
        return rf"\mathord{{{predicate}}}({arguments})", position

    def object_style(source: str, position: int) -> tuple[str, int]:
        cursor = skip_space(source, position)
        if cursor >= len(source) or source[cursor] != "{":
            return r"\mathsf{Obj}", position
        argument, position = parse_required(source, position)
        return rf"\mathsf{{{argument}}}", position

    def apply_to_first(source: str, position: int) -> tuple[str, int]:
        style, position = parse_required(source, position)
        argument, position = parse_required(source, position)
        return style + "{" + argument + "}", position

    def proof_label(name: str):
        def callback(source: str, position: int) -> tuple[str, int]:
            argument, position = parse_required(source, position)
            argument = re.sub(r"\\scriptsize(?![A-Za-z@])", "", argument)
            return rf"\operatorname{{{name}}}({argument})", position

        return callback

    value = replace_macro(value, "Atom", atom)
    value = replace_macro(value, "Obj", object_style)
    value = replace_macro(value, "applytofirst", apply_to_first)
    value = replace_macro(value, "RightLabel", proof_label("RightLabel"))
    value = replace_macro(value, "LeftLabel", proof_label("LeftLabel"))

    def raisebox(source: str, position: int) -> tuple[str, int]:
        _, position = parse_required(source, position)
        content, position = parse_required(source, position)
        return content, position

    value = replace_macro(value, "raisebox", raisebox)
    value = value.replace(r"\string\exists", r"\exists")
    value = replace_macro(
        value,
        "shoveright",
        lambda source, position: parse_required(source, position),
    )
    value = replace_macro(
        value,
        "shoveleft",
        lambda source, position: parse_required(source, position),
    )
    value = value.replace(r"\pto", r"\rightharpoonup")
    value = value.replace(r"\nicefrac", r"\frac")
    value = value.replace(r"\iddots", r"\ddots")
    value = value.replace(r"\TAss", r"\text{অনুমান}")
    value = value.replace(r"\mathexclaim", "!")
    return value


def _signed_formula(source: str, position: int) -> tuple[str, int]:
    sign, position = parse_required(source, position)
    formula, position = parse_required(source, position)
    line, position = parse_optional(source, position)
    prefix = (line + r"\,") if line else ""
    return prefix + sign + r"\;" + formula, position


def _tableau_rule(source: str, position: int) -> tuple[str, int]:
    sign, position = parse_required(source, position)
    operator, position = parse_required(source, position)
    line, position = parse_optional(source, position)
    result = operator + sign
    if line:
        result += r"\," + line
    return result, position


def _model_class(source: str, position: int) -> tuple[str, int]:
    language, position = parse_optional(source, position)
    cursor = skip_space(source, position)
    logic = None
    if cursor < len(source) and source[cursor] == "(":
        logic, position = parse_delimited(source, cursor, "(", ")")
    theory, position = parse_required(source, position)
    result = r"\mathrm{Mod}"
    if logic:
        result += "_{" + logic + "}"
    if language:
        result += "^{\\mathcal{" + language + "}}"
    return result + "(" + theory + ")", position


def _inductive_case(source: str, position: int) -> tuple[str, int]:
    cursor = skip_space(source, position)
    starred = cursor < len(source) and source[cursor] == "*"
    exercise = cursor < len(source) and source[cursor] == "!"
    if starred or exercise:
        position = cursor + 1
    formula, position = parse_required(source, position)
    complex_formula, position = parse_required(source, position)
    body, position = parse_required(source, position)
    body = body.replace(r"\indfrmp", formula).replace(r"\indfrm", formula).replace(r"\indcomplex", complex_formula)
    if exercise:
        body = "অনুশীলনী।"
    lead = f"${formula}$ পরমাণু: " if starred else f"${formula} \\equiv {complex_formula}$: "
    return lead + body, position


def collect_known_labels(units: list[tuple[str, str]]) -> set[str]:
    labels: set[str] = set()
    for uid, raw in units:
        part = chapter = section = ""
        event = re.compile(
            r"\\olfileid\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}|"
            r"\\ollabel\{([^{}]+)\}|\\olsection\{"
        )
        for match in event.finditer(raw):
            if match.group(1) is not None:
                part, chapter, section = match.group(1), match.group(2), match.group(3)
            elif match.group(4) is not None and part:
                labels.add(f"{part}:{chapter}:{section}:{match.group(4)}")
            elif part:
                labels.add(f"{part}:{chapter}:{section}:sec")
        for match in re.finditer(r"\\olchapter\{([^{}]+)\}\{([^{}]+)\}", raw):
            labels.add(f"{match.group(1)}:{match.group(2)}:chap")
        for match in re.finditer(r"\\olpart\{([^{}]+)\}", raw):
            labels.add(f"{match.group(1)}:part")
    return labels


def normalize_cross_references(value: str, uid: str, known_labels: set[str]) -> str:
    context = ["", "", ""]

    def next_event(position: int):
        pattern = re.compile(r"\\(olfileid|olsection|ollabel|olref|Olref)(?![A-Za-z@])")
        return pattern.search(value, position)

    output: list[str] = []
    cursor = 0
    while True:
        match = next_event(cursor)
        if not match:
            output.append(value[cursor:])
            break
        output.append(value[cursor:match.start()])
        name = match.group(1)
        position = match.end()
        if name == "olfileid":
            context[0], position = parse_required(value, position)
            context[1], position = parse_required(value, position)
            context[2], position = parse_required(value, position)
            replacement = ""
        elif name == "olsection":
            title, position = parse_required(value, position)
            label = ":".join(context + ["sec"])
            replacement = rf"\section{{{title}}}\label{{{label}}}"
        elif name == "ollabel":
            local, position = parse_required(value, position)
            label = ":".join(context + [local])
            replacement = rf"\hypertarget{{{label}}}{{}}"
        else:
            options: list[str] = []
            for _ in range(3):
                optional, new_position = parse_optional(value, position)
                if optional is None:
                    break
                options.append(optional)
                position = new_position
            local, position = parse_required(value, position)
            prefix = context[: 3 - len(options)] + options
            label = ":".join(prefix + [local])
            if label in known_labels:
                replacement = rf"\hyperlink{{{label}}}{{দেখুন}}"
            else:
                safe = html.escape(label)
                replacement = rf"\textnormal{{বর্তমান পাঠের বাইরের সূত্র ({safe})}}"
        output.append(replacement)
        cursor = position
    value = "".join(output)

    def chapter(source: str, position: int) -> tuple[str, int]:
        part, position = parse_required(source, position)
        chapter_id, position = parse_required(source, position)
        title, position = parse_required(source, position)
        if uid == "OLP-0719":
            title += " (বিকল্প অধ্যায়-চালক)"
            label = f"{part}:{chapter_id}:chap-alt-olp-0719"
        else:
            label = f"{part}:{chapter_id}:chap"
        return rf"\chapter{{{title}}}\label{{{label}}}", position

    def part(source: str, position: int) -> tuple[str, int]:
        part_id, position = parse_required(source, position)
        title, position = parse_required(source, position)
        return rf"\part{{{title}}}\label{{{part_id}:part}}", position

    value = replace_macro(value, "olchapter", chapter)
    value = replace_macro(value, "olpart", part)

    def generic_ref(source: str, position: int) -> tuple[str, int]:
        labels, position = parse_required(source, position)
        rendered = []
        for label in (part.strip() for part in labels.split(",")):
            if not label:
                continue
            rendered.append(rf"\hyperlink{{{label}}}{{দেখুন}}" if label in known_labels else f"বর্তমান পাঠের বাইরের সূত্র ({label})")
        return ", ".join(rendered), position

    value = replace_macro(value, "cref", generic_ref)
    value = replace_macro(value, "Cref", generic_ref)
    return value


def normalize_structural_macros(value: str) -> str:
    value = replace_macro(value, "texorpdfstring", lambda source, position: _first_of_two(source, position))
    value = replace_macro(value, "usetoken", lambda source, position: _use_token(source, position))
    value = replace_macro(value, "printtoken", lambda source, position: _print_token(source, position))
    value = replace_macro(value, "article", lambda source, position: ("একটি", parse_required(source, position)[1]))
    value = replace_macro(value, "Article", lambda source, position: ("একটি", parse_required(source, position)[1]))
    value = re.sub(r"\\olimport(?:\[[^\]]*\])?\{[^{}]*\}", "", value)
    value = re.sub(r"\\(?:OLEndChapterHook|OLEndPartHook|startycommalist)\b", "", value)
    value = value.replace(r"\ycomma", ", ")
    value = value.replace(r"\textparagraph", "§")
    value = value.replace(r"\gitissue", "উৎসের ত্রুটি-নথি")
    value = value.replace(r"\noLine", "").replace(r"\doubleLine", "").replace(r"\bottomAlignProof", "")
    value = re.sub(r"\\small(?![A-Za-z@])", "", value)
    value = value.replace(r"\notag", "")
    value = re.sub(r"\\setcounter\{[^{}]+\}\{[^{}]+\}", "", value)
    return value


def _first_of_two(source: str, position: int) -> tuple[str, int]:
    first, position = parse_required(source, position)
    _, position = parse_required(source, position)
    return first, position


def _use_token(source: str, position: int) -> tuple[str, int]:
    _, position = parse_required(source, position)
    token, position = parse_required(source, position)
    key = " ".join(token.split())
    return TOKEN_TRANSLATIONS.get(key, token), position


def _print_token(source: str, position: int) -> tuple[str, int]:
    _, position = parse_required(source, position)
    token, position = parse_required(source, position)
    key = " ".join(token.split())
    return TOKEN_TRANSLATIONS.get(key, token), position


def mark_environment_titles(value: str, marker_start: int) -> tuple[str, dict[str, dict], int]:
    markers: dict[str, dict] = {}
    pattern = re.compile(r"\\begin\{(" + "|".join(sorted(NUMBERED_ENVS)) + r")\}(?:\[([^\]]*)\])?")
    output: list[str] = []
    cursor = 0
    counter = marker_start
    for match in pattern.finditer(value):
        output.append(value[cursor:match.start()])
        marker = f"ENVHEADING{counter:06d}"
        counter += 1
        markers[marker] = {"environment": match.group(1), "title": match.group(2) or ""}
        heading = rf"\begin{{{match.group(1)}}}\textbf{{{marker}"
        if match.group(2):
            heading += ": " + match.group(2)
        heading += r"}\par "
        output.append(heading)
        cursor = match.end()
    output.append(value[cursor:])
    return "".join(output), markers, counter


def extract_fixed_macro_preamble(used_names: set[str]) -> str:
    source = strip_comments(CONFIG_PATH.read_text(encoding="utf-8"))
    declarations: list[tuple[int, str, int, str]] = []
    excluded = {
        "lexists", "lforall", "eq", "Sat", "mSat", "pSat", "Proves", "Entails",
        "Value", "varAssign", "pValue", "sFmla", "TRule", "Intro", "Elim",
        "cfind", "eqc", "rep", "iso", "elemequiv", "tf", "Log", "Prf",
        "OPrf", "Prov", "OProv", "OCon", "Trm", "Frm", "Sent", "redone",
        "red", "redpar", "cd", "lambd", "inj", "Mod", "indcase", "formula",
    }

    command = re.compile(r"\\(DeclareDocumentMacro|DeclareDocumentCommand|newcommand)\*?")
    for match in command.finditer(source):
        cursor = skip_space(source, match.end())
        try:
            if source[cursor] == "{":
                name_token, cursor = parse_delimited(source, cursor, "{", "}")
            else:
                name_match = re.match(r"\\([A-Za-z@]+)", source[cursor:])
                if not name_match:
                    continue
                name_token = name_match.group(0)
                cursor += len(name_token)
            name = name_token.lstrip("\\").strip()
            if name not in used_names or name in excluded:
                continue
            arity = 0
            if match.group(1) == "DeclareDocumentCommand":
                spec, cursor = parse_required(source, cursor)
                compact = re.sub(r"\s+", "", spec)
                if not compact or not re.fullmatch(r"m+", compact):
                    continue
                arity = len(compact)
            elif match.group(1) == "newcommand":
                optional, cursor2 = parse_optional(source, cursor)
                if optional is not None:
                    if not optional.isdigit():
                        continue
                    arity = int(optional)
                    cursor = cursor2
                    default, _ = parse_optional(source, cursor)
                    if default is not None:
                        continue
            body, cursor = parse_required(source, cursor)
        except (ValueError, IndexError):
            continue
        body = body.replace(r"\mathexclaim", "!").replace(r"\mathsfit", r"\mathsf")
        body = body.replace(r"\varolessthan", "<").replace(r"\oldepsilon", r"\epsilon")
        body = re.sub(r"\\ensuremath\{((?:[^{}]|\{[^{}]*\})*)\}", r"{\1}", body)
        declarations.append((match.start(), name, arity, body))

    # Preserve the last project definition of a name, but retain source order.
    last: dict[str, tuple[int, str, int, str]] = {entry[1]: entry for entry in declarations}
    entries = sorted(last.values())
    manual_names = {
        "Struct", "Lang", "Obj", "pAssign", "Gn", "gn", "pto", "lcm",
        "iddots", "TAss", "formula", "DischargeRule", "mModel", "Part",
        "Subst", "SSubst",
    }
    lines = []
    for _, name, arity, body in entries:
        if name in manual_names:
            continue
        lines.append(rf"\newcommand{{\{name}}}" + (f"[{arity}]" if arity else "") + "{" + body + "}")

    manual = {
        "Struct": r"\newcommand{\Struct}[1]{\mathfrak{#1}}",
        "Lang": r"\newcommand{\Lang}[1]{\mathcal{#1}}",
        "Obj": r"\newcommand{\Obj}[1]{\mathsf{#1}}",
        "pAssign": r"\newcommand{\pAssign}[1]{\mathfrak{#1}}",
        "Gn": r"\newcommand{\Gn}[1]{\ulcorner #1\urcorner}",
        "gn": r"\newcommand{\gn}[1]{\ulcorner #1\urcorner}",
        "pto": r"\newcommand{\pto}{\rightharpoonup}",
        "lcm": r"\newcommand{\lcm}{\operatorname{lcm}}",
        "iddots": r"\newcommand{\iddots}{\ddots}",
        "TAss": r"\newcommand{\TAss}{\text{অনুমান}}",
        "formula": r"\newcommand{\formula}[1]{#1}",
        "DischargeRule": r"\newcommand{\DischargeRule}[2]{{#1}^{#2}}",
        "mModel": r"\newcommand{\mModel}[1]{\mathfrak{#1}}",
        "Part": r"\newcommand{\Part}[2]{\mathord{\mathsf{P}}(#1,#2)}",
        "Subst": r"\newcommand{\Subst}[3]{#1[#2/#3]}",
        "SSubst": r"\newcommand{\SSubst}[2]{#1[#2]}",
    }
    for name, definition in manual.items():
        if name in used_names and name not in excluded:
            lines.append(definition)
    return "\n".join(lines)


@dataclass
class UnitResult:
    unit_id: str
    source_path: str
    body: str
    proof_trees: int
    tableaux: int
    diagrams: int
    derivations: int
    environment_markers: dict[str, dict]


def extract_body(raw: str) -> str:
    require(r"\begin{document}" in raw and r"\end{document}" in raw, "source unit lacks document wrapper")
    return raw.split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]


def process_unit(uid: str, source_path: str, raw: str, known_labels: set[str], marker_start: int) -> tuple[UnitResult, int]:
    value = strip_comments(extract_body(raw))
    value = evaluate_selectors(value, known_labels)
    value = replace_tokens(value)
    value = literalize_string_commands(value)
    value = normalize_cross_references(value, uid, known_labels)
    value = normalize_structural_macros(value)
    value = normalize_bengali_token_suffixes(value)
    value, proof_trees = transform_proof_trees(value)
    value, tableaux = transform_tableaux(value)
    value, derivations = transform_derivations(value)
    value, diagrams = transform_diagrams(value)
    for _ in range(12):
        expanded = special_math_macros(value)
        if expanded == value:
            break
        value = expanded
    else:
        raise RuntimeError("special math macro expansion did not reach a fixed point")
    value = value.replace(r"\mathrel{||}\joinrel\Relbar", r"\vDash")
    value = replace_formula_metavariables(value)
    # The TeX italic-correction command has no meaning in HTML and is invalid
    # inside MathJax/Pandoc text-mode math arguments.
    value = value.replace(r"\/", "")
    value = normalize_display_environments(value)
    value, markers, marker_end = mark_environment_titles(value, marker_start)
    marker = uid.lower()
    unit_heading = (
        rf"\hypertarget{{unit-{marker}}}{{}}"
        rf"\texttt{{UNITMARKER-{uid}}}\par" + "\n"
    )
    return UnitResult(uid, source_path, unit_heading + value, proof_trees, tableaux, diagrams, derivations, markers), marker_end


def build_semantic_input() -> tuple[Path, dict, dict[str, dict]]:
    status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    require(status["source"]["revision"] == SOURCE_REVISION, "source revision drift")
    require(status["source"]["manifest_sha256"] == MANIFEST_SHA256, "manifest identity drift")
    require(status["draft_scope"]["translated_units"] == EXPECTED_UNITS, "translated unit sequence drift")
    require(status["draft_scope"]["translated_count"] == EXPECTED_UNIT_COUNT, "translated count drift")
    require(status["draft_scope"]["untranslated_count"] == EXPECTED_UNTRANSLATED, "untranslated count drift")
    require(sha256(MANIFEST_PATH.read_bytes()) == MANIFEST_SHA256, "manifest byte hash drift")

    manifest = {row["unit_id"]: row for row in map(json.loads, MANIFEST_PATH.read_text(encoding="utf-8").splitlines())}
    raw_units: list[tuple[str, str]] = []
    source_paths: dict[str, str] = {}
    for uid in EXPECTED_UNITS:
        row = manifest[uid]
        target = REPO / "bn-Beng-IN" / row["source_path"]
        require(target.is_file(), f"translated target missing: {target}")
        raw = target.read_text(encoding="utf-8")
        raw_units.append((uid, raw))
        source_paths[uid] = row["source_path"]
    known_labels = collect_known_labels(raw_units)

    results: list[UnitResult] = []
    all_markers: dict[str, dict] = {}
    marker_counter = 1
    for uid, raw in raw_units:
        try:
            result, marker_counter = process_unit(
                uid, source_paths[uid], raw, known_labels, marker_counter
            )
        except Exception as exc:
            raise RuntimeError(f"reader conversion failed for {uid} ({source_paths[uid]}): {exc}") from exc
        results.append(result)
        overlap = set(all_markers) & set(result.environment_markers)
        require(not overlap, f"duplicate environment markers: {overlap}")
        all_markers.update(result.environment_markers)

    combined_body = "\n\n".join(result.body for result in results)
    used_names = set(re.findall(r"\\([A-Za-z@]+)", combined_body))
    macro_preamble = extract_fixed_macro_preamble(used_names)
    scope_note = r"""
\begin{scope-note}
\textbf{এই পাঠের পরিসর ও রূপান্তর-পদ্ধতি।}
এই পুনঃপ্রবাহযোগ্য পাঠে হিমায়িত উৎসের ৭২২টি এককের মধ্যে অনূদিত ২৯৯টি একক আছে:
OLP-0004--OLP-0300, OLP-0719 ও OLP-0721। এখনও ৪২৩টি একক অনূদিত হয়নি।
প্রত্যেক উৎস একক এখানে একবারই আছে; অধ্যায়-চালকের আমদানি-নির্দেশগুলি পুনরাবৃত্তি এড়াতে বাদ দেওয়া হয়েছে।
পূর্ণ সংস্করণের নির্বাচন-বিধি এবং প্রথম-ক্রমের শাখা ব্যবহার করা হয়েছে। বিকল্প সম্পর্ক-চালক OLP-0719
আলাদা চালক-নোট হিসেবে রাখা হয়েছে। প্রমাণ-বৃক্ষগুলি অনুমান ও সিদ্ধান্তের ক্রমে, ট্যাবলোগুলি শাখা-স্তরসহ,
এবং টিকজ চিত্রগুলি শীর্ষ, সংযোগ ও লেবেলের পাঠ্যরূপে দেওয়া হয়েছে—যাতে ছোট পর্দা ও সহায়ক প্রযুক্তিতে
বিষয়বস্তু পুনঃপ্রবাহযোগ্য থাকে। সূত্রগুলি নেটিভ MathML। এই রূপান্তরে কোনো TeX ইঞ্জিন ব্যবহৃত হয়নি।
\end{scope-note}
"""
    preamble = rf"""
\documentclass{{book}}
\usepackage{{amsmath,amssymb}}
\newenvironment{{scope-note}}{{}}{{}}
\newenvironment{{proof-tree-semantic}}{{}}{{}}
\newenvironment{{tableau-semantic}}{{}}{{}}
\newenvironment{{derivation-semantic}}{{}}{{}}
\newenvironment{{diagram-semantic}}{{}}{{}}
\newenvironment{{display-prose}}{{}}{{}}
\newenvironment{{translationnote}}{{}}{{}}
\newenvironment{{editorial}}{{}}{{}}
\newenvironment{{intro}}{{}}{{}}
\newenvironment{{explain}}{{}}{{}}
\newenvironment{{digress}}{{}}{{}}
\newenvironment{{history}}{{}}{{}}
{macro_preamble}
\begin{{document}}
\chapter*{{ওপেন লজিক: বাংলা (ভারত)}}
{scope_note}
"""
    ending = rf"""
\chapter*{{সংস্করণ ও লাইসেন্স}}
মূল রচনা Open Logic Project। উৎস ও এই বাংলা অনুবাদ Creative Commons Attribution 4.0 International
লাইসেন্সে প্রকাশিত। উৎস সংস্করণ: \texttt{{{SOURCE_REVISION}}}।
অনুবাদটি যন্ত্রের সহায়তায় প্রস্তুত এবং উৎসের সঙ্গে সূত্র, গঠন ও অর্থের স্তরে পরীক্ষা করা হয়েছে;
স্বাধীন মানব-সম্পাদনার দাবি করা হচ্ছে না। এমবেড করা Noto Serif Bengali ফন্ট SIL Open Font License 1.1-এ প্রকাশিত।
\end{{document}}
"""
    semantic_input = BUILD / "semantic-input.tex"
    semantic_input.write_text(preamble + combined_body + ending, encoding="utf-8", newline="\n")
    stats = {
        "units": len(results),
        "proof_trees": sum(result.proof_trees for result in results),
        "tableaux": sum(result.tableaux for result in results),
        "diagrams": sum(result.diagrams for result in results),
        "derivations": sum(result.derivations for result in results),
        "numbered_environments": len(all_markers),
        "known_labels": len(known_labels),
        "semantic_input_bytes": semantic_input.stat().st_size,
        "semantic_input_sha256": sha256(semantic_input.read_bytes()),
    }
    return semantic_input, stats, all_markers


def run_pandoc(source: Path) -> tuple[Path, str]:
    destination = BUILD / "pandoc.html"
    log = BUILD / "pandoc.log"
    command = [
        "pandoc", str(source), "--from=latex", "--to=html5", "--standalone",
        "--mathml", "--toc", "--toc-depth=3", "--citeproc", f"--bibliography={BIB_PATH}",
        "--metadata", f"lang={LANGUAGE}", "--metadata", "title=ওপেন লজিক: বাংলা (ভারত)",
        "--metadata", "reference-section-title=তথ্যসূত্র", "--metadata", "link-citations=true",
        "--output", str(destination),
    ]
    completed = subprocess.run(
        command, cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False
    )
    log.write_text(completed.stdout + completed.stderr, encoding="utf-8", newline="\n")
    require(completed.returncode == 0, f"Pandoc failed:\n{completed.stderr}")
    require(destination.is_file(), "Pandoc did not create HTML")
    require("Could not convert TeX math" not in completed.stderr, "Pandoc left unconverted TeX math")
    return destination, completed.stderr


def slugify(value: str) -> str:
    value = re.sub(r"[^\w\u0980-\u09ff]+", "-", value.casefold(), flags=re.UNICODE).strip("-")
    return value or "section"


def postprocess_html(pandoc_html: Path, environment_markers: dict[str, dict]) -> tuple[Path, dict]:
    soup = BeautifulSoup(pandoc_html.read_text(encoding="utf-8"), "html.parser")
    require(soup.html is not None and soup.head is not None and soup.body is not None, "Pandoc HTML shell missing")
    soup.html["lang"] = LANGUAGE
    soup.html["xml:lang"] = LANGUAGE
    soup.html["dir"] = "ltr"
    if soup.title:
        soup.title.string = "ওপেন লজিক: বাংলা (ভারত) — OLP-0300 পর্যন্ত"

    pandoc_title = soup.select_one("header#title-block-header")
    if pandoc_title is not None:
        pandoc_title.decompose()

    for style in soup.find_all("style"):
        style.decompose()
    style = soup.new_tag("style", id="reader-style")
    style.string = CSS.replace("../fonts/NotoSerifBengali-Regular.ttf", "NotoSerifBengali-Regular.ttf").replace(
        "../fonts/NotoSerifBengali-Bold.ttf", "NotoSerifBengali-Bold.ttf"
    )
    soup.head.append(style)

    header = soup.new_tag("header")
    heading = soup.new_tag("h1", id="book-title")
    heading.string = "ওপেন লজিক: বাংলা (ভারত)"
    subtitle = soup.new_tag("p")
    subtitle.string = "২৯৯টি অনূদিত উৎস এককের পুনঃপ্রবাহযোগ্য পাঠ · OLP-0300 পর্যন্ত"
    header.extend([heading, subtitle])
    soup.body.insert(0, header)

    for text_node in list(soup.find_all(string=re.compile(r"UNITMARKER-OLP-\d{4}"))):
        match = re.search(r"UNITMARKER-(OLP-\d{4})", str(text_node))
        require(match is not None, "malformed unit marker")
        uid = match.group(1)
        parent = text_node.parent
        parent.string = uid
        parent["class"] = list(dict.fromkeys(parent.get("class", []) + ["unit-marker"]))
        parent["data-source-unit"] = uid

    chapter = 0
    section = 0
    theorem = 0
    problem = 0
    label_numbers: dict[str, str] = {}
    for element in soup.find_all(["h1", "h2", "h3", "div"]):
        if element.name == "h1" and element.get("id") != "book-title":
            chapter += 1
            section = theorem = problem = 0
        elif element.name == "h2":
            section += 1
            theorem = 0
        if element.name != "div":
            continue
        classes = set(element.get("class", []))
        environment = next((name for name in NUMBERED_ENVS if name in classes), None)
        if environment is None:
            continue
        marker_node = element.find(string=re.compile(r"ENVHEADING\d{6}"))
        require(marker_node is not None, f"environment title marker missing for {environment}")
        marker_match = re.search(r"ENVHEADING\d{6}", str(marker_node))
        require(marker_match is not None and marker_match.group(0) in environment_markers, "unknown environment marker")
        marker = marker_match.group(0)
        if environment == "prob":
            problem += 1
            number = f"{chapter}.{problem}"
        else:
            theorem += 1
            number = f"{chapter}.{section}.{theorem}"
        replacement = str(marker_node).replace(marker, f"{ENV_NAMES[environment]} {number}")
        marker_node.replace_with(NavigableString(replacement))
        strong = element.find("strong")
        if strong:
            paragraph = strong.parent
            paragraph["class"] = list(dict.fromkeys(paragraph.get("class", []) + ["environment-title"]))
        for anchor in element.find_all(id=True):
            label_numbers[anchor["id"]] = f"{ENV_NAMES[environment]} {number}"

    for div in soup.find_all("div"):
        classes = set(div.get("class", []))
        if "proof" in classes:
            first = div.find("em")
            if first and first.get_text(" ", strip=True) == "Proof.":
                first.string = "প্রমাণ।"
        if classes & {"proof-tree-semantic", "tableau-semantic", "derivation-semantic", "diagram-semantic"}:
            div["role"] = "group"

    bengali_math_text_nodes = 0
    for mtext in soup.find_all("mtext"):
        if not re.search(r"[\u0980-\u09ff]", mtext.get_text()):
            continue
        # Calibre and several WebKit-based EPUB readers ignore stylesheet
        # font declarations on MathML token elements.  An inline declaration
        # preserves Bengali conjunct/vowel shaping while retaining native
        # MathML and its TeX annotation.
        prior_style = mtext.get("style", "").strip().rstrip(";")
        font_style = "font-family:'Nirmala UI','Noto Serif Bengali',BN,serif;font-style:normal"
        mtext["style"] = (prior_style + ";" + font_style).lstrip(";")
        # ``mathvariant=normal`` forces Calibre back to its unshaped math
        # font even when an inline complex-script font is present.
        mtext.attrs.pop("mathvariant", None)
        bengali_math_text_nodes += 1

    used_ids: set[str] = set()
    for element in soup.find_all(id=True):
        identifier = element["id"]
        if identifier in used_ids:
            base = identifier
            counter = 2
            while f"{base}-{counter}" in used_ids:
                counter += 1
            element["id"] = f"{base}-{counter}"
        used_ids.add(element["id"])
    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
        if not heading.get("id"):
            base = slugify(heading.get_text(" ", strip=True))
            identifier = base
            counter = 2
            while identifier in used_ids:
                identifier = f"{base}-{counter}"
                counter += 1
            heading["id"] = identifier
            used_ids.add(identifier)

    for link in soup.select('a[href^="#"]'):
        target = link.get("href", "")[1:]
        if target in label_numbers and link.get_text(" ", strip=True) == "দেখুন":
            link.string = label_numbers[target]
        if target not in used_ids:
            replacement = soup.new_tag("span")
            replacement["class"] = "outside-ref"
            replacement.string = link.get_text(" ", strip=True) + " (বর্তমান পরিসরের বাইরে)"
            link.replace_with(replacement)

    main = soup.new_tag("main", id="reader-content")
    for child in list(soup.body.contents):
        if child is header:
            continue
        main.append(child.extract())
    soup.body.append(main)

    license_details = soup.new_tag("details", id="font-license")
    summary = soup.new_tag("summary")
    summary.string = "এম্বেড করা ফন্টের লাইসেন্স"
    pre = soup.new_tag("pre")
    pre["class"] = "license-text"
    pre.string = FONT_LICENSE.read_text(encoding="utf-8")
    license_details.extend([summary, pre])
    main.append(license_details)

    raw_math = soup.select("span.math")
    require(not raw_math, f"unconverted TeX math spans: {len(raw_math)}")
    require(not soup.find_all("script"), "script found in semantic HTML")
    unit_markers = soup.select(".unit-marker[data-source-unit]")
    require([node["data-source-unit"] for node in unit_markers] == EXPECTED_UNITS, "unit marker sequence drift")
    require(
        re.search(r"!!(?:\^)?a?\{", soup.get_text()) is None,
        "unexpanded OpenLogic text token in HTML",
    )
    ids = [tag["id"] for tag in soup.find_all(id=True)]
    require(len(ids) == len(set(ids)), "duplicate HTML IDs")
    broken = [link["href"] for link in soup.select('a[href^="#"]') if link["href"][1:] not in set(ids)]
    require(not broken, f"broken internal HTML links: {broken[:10]}")
    math_nodes = soup.find_all("math")
    require(math_nodes, "native MathML missing")
    annotations = soup.find_all("annotation", attrs={"encoding": "application/x-tex"})
    require(len(annotations) == len(math_nodes), "MathML TeX annotation coverage drift")

    epub_source = BUILD / "content-for-epub.html"
    epub_source.write_text(str(soup), encoding="utf-8", newline="\n")

    regular = base64.b64encode(FONT_REGULAR.read_bytes()).decode("ascii")
    bold = base64.b64encode(FONT_BOLD.read_bytes()).decode("ascii")
    standalone = copy.deepcopy(soup)
    standalone_style = standalone.find("style", id="reader-style")
    require(standalone_style is not None, "reader style missing")
    standalone_style.string = str(standalone_style.string).replace(
        "url('NotoSerifBengali-Regular.ttf')", f"url('data:font/ttf;base64,{regular}')"
    ).replace(
        "url('NotoSerifBengali-Bold.ttf')", f"url('data:font/ttf;base64,{bold}')"
    )
    HTML_OUTPUT.write_text(str(standalone), encoding="utf-8", newline="\n")

    counts = Counter()
    for name in NUMBERED_ENVS:
        counts[name] = len(soup.select(f"div.{name}"))
    receipt = {
        "html_bytes": HTML_OUTPUT.stat().st_size,
        "html_sha256": sha256(HTML_OUTPUT.read_bytes()),
        "epub_source_bytes": epub_source.stat().st_size,
        "epub_source_sha256": sha256(epub_source.read_bytes()),
        "unit_markers": len(unit_markers),
        "native_mathml": len(math_nodes),
        "mathml_tex_annotations": len(annotations),
        "bengali_math_text_nodes_with_inline_font": bengali_math_text_nodes,
        "numbered_environments": sum(counts.values()),
        "environment_counts": dict(sorted(counts.items())),
        "proof_tree_blocks": len(soup.select("div.proof-tree-semantic")),
        "tableau_blocks": len(soup.select("div.tableau-semantic")),
        "derivation_blocks": len(soup.select("div.derivation-semantic")),
        "diagram_blocks": len(soup.select("div.diagram-semantic")),
        "internal_links": len(soup.select('a[href^="#"]')),
        "broken_internal_links": 0,
        "scripts": 0,
        "offline_fonts_embedded": True,
    }
    return epub_source, receipt


def xhtml_shell(title: str) -> tuple[etree._Element, etree._Element]:
    root = etree.Element(f"{{{XHTML_NS}}}html", nsmap={None: XHTML_NS, "epub": EPUB_NS})
    root.set("lang", LANGUAGE)
    root.set(f"{{{XML_NS}}}lang", LANGUAGE)
    root.set("dir", "ltr")
    head = etree.SubElement(root, f"{{{XHTML_NS}}}head")
    etree.SubElement(head, f"{{{XHTML_NS}}}meta", charset="utf-8")
    title_node = etree.SubElement(head, f"{{{XHTML_NS}}}title")
    title_node.text = title
    link = etree.SubElement(head, f"{{{XHTML_NS}}}link")
    link.set("rel", "stylesheet")
    link.set("type", "text/css")
    link.set("href", "styles/reader.css")
    body = etree.SubElement(root, f"{{{XHTML_NS}}}body")
    return root, body


def serialize_xml(root: etree._Element, path: Path) -> None:
    payload = etree.tostring(root, encoding="utf-8", xml_declaration=True, pretty_print=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def prepare_content(epub_source: Path) -> tuple[list[dict], dict]:
    parser = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True)
    parsed = etree.parse(str(epub_source), parser)
    source_root = parsed.getroot()
    namespace = {"x": XHTML_NS, "m": MATHML_NS}
    require(source_root.tag == f"{{{XHTML_NS}}}html", "intermediate HTML is not XML-compatible XHTML")
    source_body = source_root.xpath("/x:html/x:body", namespaces=namespace)[0]
    content_root, content_body = xhtml_shell("ওপেন লজিক: বাংলা (ভারত)")
    for child in source_body:
        content_body.append(copy.deepcopy(child))
    content_path = UNPACKED / "OEBPS" / "content.xhtml"
    serialize_xml(content_root, content_path)
    content_parsed = etree.parse(str(content_path), parser)
    headings = content_parsed.xpath("//x:h1 | //x:h2 | //x:h3", namespaces=namespace)
    toc = [
        {
            "level": int(etree.QName(node).localname[1]),
            "id": node.get("id"),
            "title": " ".join("".join(node.itertext()).split()),
        }
        for node in headings
        if node.get("id")
    ]
    math_count = len(content_parsed.xpath("//m:math", namespaces=namespace))
    return toc, {
        "path": "OEBPS/content.xhtml",
        "bytes": content_path.stat().st_size,
        "sha256": sha256(content_path.read_bytes()),
        "headings": len(toc),
        "mathml": math_count,
    }


def prepare_about() -> dict:
    root, body = xhtml_shell("এই সংস্করণ সম্পর্কে")
    main = etree.SubElement(body, f"{{{XHTML_NS}}}main")
    main.set("id", "about")
    heading = etree.SubElement(main, f"{{{XHTML_NS}}}h1")
    heading.text = "এই সংস্করণ সম্পর্কে"
    paragraphs = [
        "এটি ওপেন লজিকের চলমান বাংলা (ভারত) অনুবাদের ২৯৯-একক পাঠ: OLP-0004 থেকে OLP-0300, সঙ্গে OLP-0719 ও OLP-0721। পূর্ণ ৭২২-একক উৎসে এখনও ৪২৩টি একক অনূদিত হয়নি।",
        "প্রমাণ-বৃক্ষ, ট্যাবলো ও উৎসচিত্রগুলি পুনঃপ্রবাহযোগ্য পাঠ্য কাঠামোয় দেওয়া হয়েছে। গাণিতিক সূত্রগুলি নেটিভ MathML; প্যাকেজে কোনো স্ক্রিপ্ট, অডিও বা স্থির-পৃষ্ঠার বিন্যাস নেই।",
        f"হিমায়িত OpenLogicProject/OpenLogic উৎস সংস্করণ: {SOURCE_REVISION}।",
    ]
    for value in paragraphs:
        paragraph = etree.SubElement(main, f"{{{XHTML_NS}}}p")
        paragraph.text = value
    path = UNPACKED / "OEBPS" / "about.xhtml"
    serialize_xml(root, path)
    return {"path": "OEBPS/about.xhtml", "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes())}


def prepare_legal() -> dict:
    root, body = xhtml_shell("লাইসেন্স")
    main = etree.SubElement(body, f"{{{XHTML_NS}}}main")
    heading = etree.SubElement(main, f"{{{XHTML_NS}}}h1")
    heading.text = "লাইসেন্স"
    paragraph = etree.SubElement(main, f"{{{XHTML_NS}}}p")
    paragraph.text = "Open Logic Project এবং এই বাংলা অনুবাদ Creative Commons Attribution 4.0 International (CC BY 4.0) লাইসেন্সে প্রকাশিত।"
    font_heading = etree.SubElement(main, f"{{{XHTML_NS}}}h2")
    font_heading.text = "Noto ফন্ট"
    pre = etree.SubElement(main, f"{{{XHTML_NS}}}pre")
    pre.text = FONT_LICENSE.read_text(encoding="utf-8")
    path = UNPACKED / "OEBPS" / "legal.xhtml"
    serialize_xml(root, path)
    return {"path": "OEBPS/legal.xhtml", "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes())}


def prepare_nav(toc: list[dict]) -> dict:
    root, body = xhtml_shell("সূচিপত্র")
    nav = etree.SubElement(body, f"{{{XHTML_NS}}}nav")
    nav.set(f"{{{EPUB_NS}}}type", "toc")
    nav.set("id", "toc")
    heading = etree.SubElement(nav, f"{{{XHTML_NS}}}h1")
    heading.text = "সূচিপত্র"
    listing = etree.SubElement(nav, f"{{{XHTML_NS}}}ol")
    for row in toc:
        item = etree.SubElement(listing, f"{{{XHTML_NS}}}li")
        item.set("class", f"toc-level-{row['level']}")
        link = etree.SubElement(item, f"{{{XHTML_NS}}}a")
        link.set("href", f"content.xhtml#{row['id']}")
        link.text = row["title"]
    landmarks = etree.SubElement(body, f"{{{XHTML_NS}}}nav")
    landmarks.set(f"{{{EPUB_NS}}}type", "landmarks")
    landmark_heading = etree.SubElement(landmarks, f"{{{XHTML_NS}}}h2")
    landmark_heading.text = "পাঠের প্রধান অংশ"
    landmark_list = etree.SubElement(landmarks, f"{{{XHTML_NS}}}ol")
    for href, epub_type, title in (
        ("about.xhtml", "frontmatter", "এই সংস্করণ সম্পর্কে"),
        ("content.xhtml#book-title", "bodymatter", "মূল পাঠ"),
        ("legal.xhtml", "copyright-page", "লাইসেন্স"),
    ):
        item = etree.SubElement(landmark_list, f"{{{XHTML_NS}}}li")
        link = etree.SubElement(item, f"{{{XHTML_NS}}}a")
        link.set("href", href)
        link.set(f"{{{EPUB_NS}}}type", epub_type)
        link.text = title
    path = UNPACKED / "OEBPS" / "nav.xhtml"
    serialize_xml(root, path)
    return {"path": "OEBPS/nav.xhtml", "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes()), "entries": len(toc)}


def prepare_package(html_sha: str) -> dict:
    package = etree.Element(f"{{{OPF_NS}}}package", nsmap={None: OPF_NS, "dc": DC_NS})
    package.set("version", "3.0")
    package.set("unique-identifier", "pub-id")
    package.set("prefix", "schema: http://schema.org/")
    metadata = etree.SubElement(package, f"{{{OPF_NS}}}metadata")

    def dc(name: str, text: str, identifier: str | None = None) -> etree._Element:
        node = etree.SubElement(metadata, f"{{{DC_NS}}}{name}")
        if identifier:
            node.set("id", identifier)
        node.text = text
        return node

    def meta(prop: str, text: str, refines: str | None = None) -> etree._Element:
        node = etree.SubElement(metadata, f"{{{OPF_NS}}}meta")
        node.set("property", prop)
        if refines:
            node.set("refines", refines)
        node.text = text
        return node

    dc("identifier", f"urn:sha256:{html_sha}:epub3-299", "pub-id")
    dc("title", "ওপেন লজিক: বাংলা (ভারত) — OLP-0300 পর্যন্ত", "title")
    meta("title-type", "main", "#title")
    dc("language", LANGUAGE)
    dc("creator", "Open Logic Project and credited contributors", "creator")
    role = meta("role", "aut", "#creator")
    role.set("scheme", "marc:relators")
    dc("contributor", "Bengali (India) translation edition", "translator")
    role = meta("role", "trl", "#translator")
    role.set("scheme", "marc:relators")
    dc("publisher", "OpenLogic Bengali (India) translation programme")
    dc("subject", "Mathematical logic")
    dc("description", "Partial Bengali (India) reflowable EPUB3: 299 of 722 source units, through Representability in Q; 423 units remain untranslated.")
    dc("date", MODIFIED[:10])
    dc("rights", "Creative Commons Attribution 4.0 International (CC BY 4.0); embedded Noto fonts use SIL Open Font License 1.1.")
    meta("dcterms:modified", MODIFIED)
    meta("dcterms:provenance", f"OpenLogicProject/OpenLogic revision {SOURCE_REVISION}; sealed semantic HTML {html_sha}.")
    meta("rendition:layout", "reflowable")
    meta("rendition:orientation", "auto")
    meta("rendition:spread", "auto")
    meta("schema:accessMode", "textual")
    meta("schema:accessMode", "visual")
    meta("schema:accessModeSufficient", "textual")
    for feature in ("MathML", "displayTransformability", "readingOrder", "structuralNavigation", "tableOfContents"):
        meta("schema:accessibilityFeature", feature)
    for hazard in ("noFlashingHazard", "noMotionSimulationHazard", "noSoundHazard"):
        meta("schema:accessibilityHazard", hazard)
    meta("schema:accessibilitySummary", "Reflowable Bengali text with native MathML, structural navigation, and textual proof-tree, tableau, and diagram representations. The package is script-free and has no audio, flashing, or motion.")

    manifest = etree.SubElement(package, f"{{{OPF_NS}}}manifest")
    resources = [
        ("nav", "nav.xhtml", "application/xhtml+xml", "nav"),
        ("about", "about.xhtml", "application/xhtml+xml", ""),
        ("content", "content.xhtml", "application/xhtml+xml", "mathml"),
        ("legal", "legal.xhtml", "application/xhtml+xml", ""),
        ("css", "styles/reader.css", "text/css", ""),
        ("font-regular", "fonts/NotoSerifBengali-Regular.ttf", "font/ttf", ""),
        ("font-bold", "fonts/NotoSerifBengali-Bold.ttf", "font/ttf", ""),
    ]
    for identifier, href, media_type, properties in resources:
        item = etree.SubElement(manifest, f"{{{OPF_NS}}}item")
        item.set("id", identifier)
        item.set("href", href)
        item.set("media-type", media_type)
        if properties:
            item.set("properties", properties)
    spine = etree.SubElement(package, f"{{{OPF_NS}}}spine")
    spine.set("page-progression-direction", "ltr")
    for identifier, linear in (("about", "yes"), ("content", "yes"), ("legal", "no")):
        itemref = etree.SubElement(spine, f"{{{OPF_NS}}}itemref")
        itemref.set("idref", identifier)
        itemref.set("linear", linear)
    path = UNPACKED / "OEBPS" / "package.opf"
    serialize_xml(package, path)
    return {"path": "OEBPS/package.opf", "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes()), "manifest_items": len(resources)}


def prepare_container() -> dict:
    (UNPACKED / "mimetype").write_bytes(b"application/epub+zip")
    root = etree.Element(f"{{{CONTAINER_NS}}}container", nsmap={None: CONTAINER_NS})
    root.set("version", "1.0")
    rootfiles = etree.SubElement(root, f"{{{CONTAINER_NS}}}rootfiles")
    rootfile = etree.SubElement(rootfiles, f"{{{CONTAINER_NS}}}rootfile")
    rootfile.set("full-path", "OEBPS/package.opf")
    rootfile.set("media-type", "application/oebps-package+xml")
    path = UNPACKED / "META-INF" / "container.xml"
    serialize_xml(root, path)
    return {"container_sha256": sha256(path.read_bytes())}


def create_epub(destination: Path) -> dict:
    def info(name: str, compression: int) -> zipfile.ZipInfo:
        row = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
        row.compress_type = compression
        row.create_system = 3
        row.external_attr = 0o100644 << 16
        row.flag_bits |= 0x800
        return row

    if destination.exists():
        destination.unlink()
    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        archive.writestr(info("mimetype", zipfile.ZIP_STORED), b"application/epub+zip")
        for path in sorted(UNPACKED.rglob("*")):
            if not path.is_file() or path == UNPACKED / "mimetype":
                continue
            name = path.relative_to(UNPACKED).as_posix()
            archive.writestr(info(name, zipfile.ZIP_DEFLATED), path.read_bytes(), compresslevel=9)
    payload = destination.read_bytes()
    with zipfile.ZipFile(destination) as archive:
        entries = archive.infolist()
        require(entries[0].filename == "mimetype", "EPUB mimetype is not first")
        require(entries[0].compress_type == zipfile.ZIP_STORED, "EPUB mimetype is compressed")
        require(archive.read("mimetype") == b"application/epub+zip", "EPUB mimetype payload drift")
        require([row.filename for row in entries[1:]] == sorted(row.filename for row in entries[1:]), "EPUB ZIP order drift")
        for row in entries:
            pure = PurePosixPath(row.filename)
            require(not pure.is_absolute() and ".." not in pure.parts and "\\" not in row.filename, f"unsafe EPUB path: {row.filename}")
    return {"path": destination.relative_to(REPO).as_posix(), "bytes": len(payload), "sha256": sha256(payload), "entries": len(entries)}


def package_epub(epub_source: Path, html_receipt: dict) -> tuple[dict, dict]:
    safe_clear(UNPACKED)
    (UNPACKED / "OEBPS" / "styles").mkdir(parents=True)
    (UNPACKED / "OEBPS" / "fonts").mkdir(parents=True)
    for filename, source in ((FONT_REGULAR.name, FONT_REGULAR), (FONT_BOLD.name, FONT_BOLD)):
        shutil.copy2(source, UNPACKED / "OEBPS" / "fonts" / filename)
    (UNPACKED / "OEBPS" / "styles" / "reader.css").write_text(CSS + "\n", encoding="utf-8", newline="\n")
    toc, content_receipt = prepare_content(epub_source)
    parts = {
        "container": prepare_container(),
        "about": prepare_about(),
        "content": content_receipt,
        "legal": prepare_legal(),
        "nav": prepare_nav(toc),
        "package": prepare_package(html_receipt["html_sha256"]),
    }
    canonical = create_epub(EPUB_OUTPUT)
    cold_path = BUILD / "cold.epub"
    cold = create_epub(cold_path)
    require(EPUB_OUTPUT.read_bytes() == cold_path.read_bytes(), "cold EPUB build is not byte-identical")
    cold_path.unlink()
    return canonical, parts


def run_epubcheck(epub: Path, jar: Path) -> dict:
    require(jar.is_file(), f"EPUBCheck jar missing: {jar}")
    jar_sha = sha256(jar.read_bytes())
    require(jar_sha == EXPECTED_EPUBCHECK_JAR_SHA256, "EPUBCheck jar hash drift")
    report = BUILD / "EPUBCHECK.json"
    if report.exists():
        report.unlink()
    completed = subprocess.run(
        ["java", "-jar", str(jar), str(epub), "--json", str(report), "--failonwarnings"],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
    )
    require(report.is_file(), "EPUBCheck report missing")
    result = json.loads(report.read_text(encoding="utf-8"))
    checker = result.get("checker", {})
    require(completed.returncode == 0, f"EPUBCheck failed:\n{completed.stdout}\n{completed.stderr}")
    require(checker.get("checkerVersion") == EXPECTED_EPUBCHECK_VERSION, "EPUBCheck version drift")
    require(not result.get("messages"), f"EPUBCheck messages: {result.get('messages', [])[:3]}")
    for key in ("nFatal", "nError", "nWarning", "nUsage"):
        require(checker.get(key) == 0, f"EPUBCheck {key} is nonzero")
    return {
        "version": checker["checkerVersion"], "jar_sha256": jar_sha,
        "fatal": checker["nFatal"], "errors": checker["nError"],
        "warnings": checker["nWarning"], "usage": checker["nUsage"],
        "messages": len(result["messages"]), "report_sha256": sha256(report.read_bytes()),
    }


def validate_epub(epub: Path, html_receipt: dict) -> dict:
    audit = BUILD / "audit-unpacked"
    safe_clear(audit)
    with zipfile.ZipFile(epub) as archive:
        archive.extractall(audit)
    parser = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True)
    container = etree.parse(str(audit / "META-INF" / "container.xml"), parser)
    rootfile = container.xpath("string(//*[local-name()='rootfile']/@full-path)")
    require(rootfile == "OEBPS/package.opf", "EPUB container rootfile drift")
    package = etree.parse(str(audit / rootfile), parser)
    language = package.xpath("string(//*[local-name()='language'])")
    require(language == LANGUAGE, "EPUB language drift")
    layout = package.xpath("string(//*[local-name()='meta'][@property='rendition:layout'])")
    require(layout == "reflowable", "EPUB layout is not reflowable")
    content = etree.parse(str(audit / "OEBPS" / "content.xhtml"), parser)
    namespace = {"x": XHTML_NS, "m": MATHML_NS}
    math_count = len(content.xpath("//m:math", namespaces=namespace))
    require(math_count == html_receipt["native_mathml"], "EPUB MathML count differs from HTML")
    unit_markers = content.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' unit-marker ')]/@data-source-unit")
    require(unit_markers == EXPECTED_UNITS, "EPUB unit scope drift")
    require(not content.xpath("//x:script", namespaces=namespace), "script found in EPUB")
    nav = etree.parse(str(audit / "OEBPS" / "nav.xhtml"), parser)
    nav_links = nav.xpath("//x:nav[@epub:type='toc']//x:a/@href", namespaces={"x": XHTML_NS, "epub": EPUB_NS})
    require(nav_links, "EPUB navigation is empty")
    for filename, expected in FONT_HASHES.items():
        if filename == FONT_LICENSE.name:
            actual = sha256(FONT_LICENSE.read_bytes())
        else:
            actual = sha256((audit / "OEBPS" / "fonts" / filename).read_bytes())
        require(actual == expected, f"font/license hash drift: {filename}")
    return {
        "language": language, "layout": layout, "mathml": math_count,
        "unit_markers": len(unit_markers), "nav_links": len(nav_links),
        "scripts": 0, "fonts_verified": 2, "font_license_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the 299-unit Bengali semantic HTML and EPUB3 reader without TeX.")
    parser.add_argument("--epubcheck-jar", type=Path, required=True)
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    for filename, expected in FONT_HASHES.items():
        path = FONT_LICENSE if filename == FONT_LICENSE.name else REPO / "fonts" / filename
        require(path.is_file() and sha256(path.read_bytes()) == expected, f"pinned font resource drift: {filename}")

    semantic_input, source_stats, environment_markers = build_semantic_input()
    pandoc_html, warnings = run_pandoc(semantic_input)
    epub_source, html_receipt = postprocess_html(pandoc_html, environment_markers)
    require(html_receipt["proof_tree_blocks"] == source_stats["proof_trees"], "proof-tree coverage drift")
    require(html_receipt["tableau_blocks"] == source_stats["tableaux"], "tableau coverage drift")
    require(html_receipt["derivation_blocks"] == source_stats["derivations"], "derivation coverage drift")
    require(html_receipt["diagram_blocks"] == source_stats["diagrams"], "diagram coverage drift")
    require(html_receipt["numbered_environments"] == source_stats["numbered_environments"], "numbered environment coverage drift")
    epub_receipt, package_parts = package_epub(epub_source, html_receipt)
    epub_validation = validate_epub(EPUB_OUTPUT, html_receipt)
    epubcheck = run_epubcheck(EPUB_OUTPUT, args.epubcheck_jar.resolve())

    pandoc_version = subprocess.run(["pandoc", "--version"], capture_output=True, text=True, encoding="utf-8", check=True).stdout.splitlines()[0]
    receipt = {
        "schema": "openlogic-bn-cumulative-semantic-reader/1",
        "date": MODIFIED[:10],
        "status": "PASSED",
        "language": LANGUAGE,
        "source_revision": SOURCE_REVISION,
        "source_manifest_sha256": MANIFEST_SHA256,
        "translated_units": EXPECTED_UNITS,
        "translated_unit_count": EXPECTED_UNIT_COUNT,
        "untranslated_unit_count": EXPECTED_UNTRANSLATED,
        "complete": False,
        "method": "Direct source-to-semantic-HTML conversion with Pandoc MathML; no TeX engine; proof trees, tableaux, derivations, and TikZ figures converted to reflowable textual structures.",
        "edition_selectors": "OpenLogic complete-edition defaults with FOL=true; every translated source unit included once and driver imports suppressed to avoid duplication.",
        "pandoc": {"version": pandoc_version, "warnings": [line for line in warnings.splitlines() if line.strip()]},
        "source": source_stats,
        "html": html_receipt,
        "epub": epub_receipt,
        "epub_package": package_parts,
        "epub_validation": epub_validation,
        "epubcheck": epubcheck,
        "deterministic_epub_cold_build": True,
        "fonts": [{"filename": path.name, "sha256": sha256(path.read_bytes())} for path in (FONT_REGULAR, FONT_BOLD)],
        "licenses": {"translation_and_source": "CC BY 4.0", "fonts": "SIL OFL 1.1"},
    }
    receipt_path = BUILD / "BUILD_QA.json"
    write_json(receipt_path, receipt)
    print(json.dumps({
        "status": receipt["status"], "units": EXPECTED_UNIT_COUNT,
        "html": {"bytes": html_receipt["html_bytes"], "sha256": html_receipt["html_sha256"]},
        "epub": {"bytes": epub_receipt["bytes"], "sha256": epub_receipt["sha256"]},
        "mathml": html_receipt["native_mathml"], "epubcheck_messages": epubcheck["messages"],
        "receipt": str(receipt_path),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
