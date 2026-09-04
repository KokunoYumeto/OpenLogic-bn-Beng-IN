"""Replay source/translation structural and mathematical checks for the public draft."""

import collections
import hashlib
import json
import pathlib
import re
import unicodedata

repo = pathlib.Path(__file__).resolve().parents[1]
rows = [
    json.loads(line)
    for line in (repo / "evidence/FULL_SOURCE_MANIFEST.jsonl").read_text(encoding="utf-8").splitlines()
]


def norm(text):
    return re.sub(r"\s+", "", text)


def without_documented_corrections(text):
    return re.sub(
        r"% (?:OLFUN-\d+|BN-SRC-\d+|OLSIZ-\d+) TARGET-CORRECTION-BEGIN.*?"
        r"% (?:OLFUN-\d+|BN-SRC-\d+|OLSIZ-\d+) TARGET-CORRECTION-END",
        "",
        text,
        flags=re.S,
    )


def body(text):
    return text.split("\\begin{document}", 1)[1].rsplit("\\end{document}", 1)[0]


def mathparts(text):
    output = []
    pattern = re.compile(
        r"(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|"
        r"\\begin\{(align\*?|multline\*?|equation\*?)\}(.*?)\\end\{\3\}",
        re.S,
    )
    for match in pattern.finditer(text):
        fragment = (
            match.group(1)
            if match.group(1) is not None
            else match.group(2)
            if match.group(2) is not None
            else match.group(4)
        )
        while "\\intertext{" in fragment:
            start = fragment.index("\\intertext{")
            content_start = start + len("\\intertext{")
            depth = 1
            end = content_start
            while depth and end < len(fragment):
                if fragment[end] in "{}" and (end == 0 or fragment[end - 1] != "\\"):
                    depth += 1 if fragment[end] == "{" else -1
                end += 1
            assert depth == 0, "Unclosed intertext"
            output.extend(mathparts(fragment[content_start : end - 1]).elements())
            fragment = fragment[:start] + fragment[end:]
        while caption := re.search(r"\\(?:text|textrm|emph)\{", fragment):
            start = caption.start()
            content_start = caption.end()
            depth = 1
            end = content_start
            while depth and end < len(fragment):
                if fragment[end] in "{}" and fragment[end - 1] != "\\":
                    depth += 1 if fragment[end] == "{" else -1
                end += 1
            assert depth == 0, "Unclosed math text caption"
            output.extend(mathparts(fragment[content_start : end - 1]).elements())
            fragment = fragment[:start] + fragment[end:]
        output.append(norm(fragment))
    return collections.Counter(output)


def controls(text):
    commands = re.findall(
        r"\\(?:ollabel|olref|oliflabeldef|olasset|olimport|cite|citep|citet|citeyear|"
        r"label|ref|cref|Cref|url)(?:\[[^\]]*\])*(?:\{[^{}]*\})",
        text,
    )
    commands += re.findall(r"\\olfileid(?:\{[^{}]*\}){3}", text)
    commands += re.findall(r"\\(?:use|print)token(?:\{[^{}]*\}){2}", text)
    commands += re.findall(r"\\olchapter(?:\[[^\]]*\])?(?:\{[^{}]*\}){2}", text)
    return collections.Counter(commands)


def environments(text):
    return re.findall(r"\\(?:begin|end)\{[^{}]+\}", text)


def semantic_tokens(text):
    return collections.Counter(re.findall(r"!!\^?a?\{[^{}]+\}s?", text))


def hline_tokenization(text):
    return {
        "rowbreak_then_hline": len(re.findall(r"(?<!\\)\\\\\\hline", text)),
        "rowbreak_then_literal_hline": len(re.findall(r"(?<!\\)\\\\hline", text)),
    }


checked_ids = []
for row in rows:
    target_path = repo / "bn-Beng-IN" / row["source_path"]
    if not target_path.exists():
        continue
    source_path = repo / "upstream" / row["source_path"]
    source = source_path.read_text(encoding="utf-8")
    target = target_path.read_text(encoding="utf-8")
    assert hashlib.sha256(source_path.read_bytes()).hexdigest() == row["source_sha256"]
    source_blocks = re.split(r"\n\s*\n", body(source).strip())
    target_blocks = re.split(r"\n\s*\n", body(target).strip())
    checked_target = without_documented_corrections(target)
    source_math = mathparts(source)
    target_math = mathparts(checked_target)
    documented = sorted(
        set(re.findall(r"(?:OLFUN-\d+|BN-SRC-\d+|OLSIZ-\d+)", target))
    )
    alpha_fix = (
        row["unit_id"] == "OLP-0021"
        and source_math - target_math == collections.Counter({"n": 1})
        and target_math - source_math == collections.Counter({"x": 1})
        and "OLFUN-003" in documented
    )
    proof_id_fix = (
        row["unit_id"] == "OLP-0035"
        and source_math - target_math == collections.Counter({"g(x)=y": 1})
        and target_math - source_math == collections.Counter({"f(x)=y": 1})
        and "BN-SRC-001" in documented
    )
    cantor_scope_fix = (
        row["unit_id"] == "OLP-0036"
        and source_math - target_math == collections.Counter({"x\\in\\overline{A}": 1})
        and target_math - source_math == collections.Counter({"x\\inA": 1})
        and "BN-SRC-002" in documented
    )
    rational_order_fix = (
        row["unit_id"] == "OLP-0043"
        and source_math - target_math == collections.Counter({"r-s": 1})
        and target_math - source_math == collections.Counter({"s-r": 1})
        and "BN-SRC-006" in documented
    )
    real_zero_fix = (
        row["unit_id"] == "OLP-0048"
        and source_math - target_math
        == collections.Counter({"\\equivrep{f}{}\\neq0_\\Rat": 1})
        and target_math - source_math
        == collections.Counter({"\\equivrep{f}{}\\neq0_\\Real": 1})
        and "BN-SRC-014" in documented
    )
    conditional_paren_fix = (
        row["unit_id"] == "OLP-0058"
        and source_math - target_math
        == collections.Counter({"\\lnot!A\\lor!B)": 1})
        and target_math - source_math
        == collections.Counter({"(\\lnot!A\\lor!B)": 1})
        and "BN-SRC-019" in documented
    )
    formation_identity_fix = (
        row["unit_id"] == "OLP-0060"
        and source_math - target_math
        == collections.Counter({"!A\\equiv(!A_j\\land!A_k)": 1})
        and target_math - source_math
        == collections.Counter({"!A_n\\ident(!A_j\\land!A_k)": 1})
        and "BN-SRC-020" in documented
    )
    tex_command_check = None
    if row["unit_id"] == "OLP-0039":
        source_hlines = hline_tokenization(source)
        target_hlines = hline_tokenization(target)
        assert source_hlines == {"rowbreak_then_hline": 5, "rowbreak_then_literal_hline": 0}
        assert target_hlines == source_hlines
        tex_command_check = {
            "retracted_alert_disposition": "retracted_false_positive_no_change_required",
            "source": source_hlines,
            "target": target_hlines,
            "token_hex": "5c5c5c686c696e65",
        }
    audited_source = source
    shared_description = None
    if row["unit_id"] == "OLP-0029":
        old = "0 & 1 & -1 & 2 & -2 & 3 & \\dots"
        assert audited_source.count(old) == 1
        audited_source = audited_source.replace(
            old, "0 & 1 & -1 & 2 & -2 & 3 & -3 & \\dots", 1
        )
        shared_description = "OLSIZ-001 omitted f(7) value -3 restored"
    elif row["unit_id"] == "OLP-0032":
        old = "$\\tuple{2,m}$, $\\tuple{2,m}$"
        assert audited_source.count(old) == 1
        audited_source = audited_source.replace(
            old, "$\\tuple{2,m}$, $\\tuple{3,m}$", 1
        )
        shared_description = "OLSIZ-003 duplicated pairing family corrected"
    elif row["unit_id"] == "OLP-0034":
        assert audited_source.count("s_{k}") == 2 and audited_source.count("s_k") == 1
        audited_source = audited_source.replace("s_{k}", "s").replace("s_k", "s")
        old = "\\underbrace{000\\dots0}_{\\text{$n$ $0$'s}}"
        assert audited_source.count(old) == 1
        audited_source = audited_source.replace(old, old + "111\\dots", 1)
        shared_description = "OLSIZ-004 and OLSIZ-005 audited corrections"
    elif row["unit_id"] == "OLP-0040":
        assert audited_source.count("s_{k}") == 2 and audited_source.count("s_k") == 1
        audited_source = audited_source.replace("s_{k}", "s").replace("s_k", "s")
        shared_description = "BN-SRC-005 / OLSIZ-010 audited correction"
    shared_audit_fix = shared_description is not None and mathparts(audited_source) == target_math
    math_ok = any(
        (
            source_math == target_math,
            alpha_fix,
            proof_id_fix,
            cantor_scope_fix,
            rational_order_fix,
            real_zero_fix,
            conditional_paren_fix,
            formation_identity_fix,
            shared_audit_fix,
        )
    )
    checks = {
        "unit_id": row["unit_id"],
        "source_blocks": len(source_blocks),
        "target_blocks": len(target_blocks),
        "math_parity": math_ok,
        "controls_parity": controls(source) == controls(checked_target),
        "env_parity": environments(source) == environments(checked_target),
        "token_parity": semantic_tokens(source) == semantic_tokens(checked_target),
        "unicode_nfc": unicodedata.is_normalized("NFC", target),
        "documented_source_corrections": documented,
        "tex_command_check": tex_command_check,
        "target_sha256": hashlib.sha256(target_path.read_bytes()).hexdigest(),
    }
    assert checks["source_blocks"] == checks["target_blocks"], row["unit_id"]
    assert all(
        checks[key]
        for key in ("math_parity", "controls_parity", "env_parity", "token_parity", "unicode_nfc")
    ), row["unit_id"]
    print(json.dumps(checks, ensure_ascii=False))
    checked_ids.append(row["unit_id"])

draft = json.loads((repo / "evidence/DRAFT_STATUS.json").read_text(encoding="utf-8"))
assert sorted(checked_ids) == sorted(draft["draft_scope"]["translated_units"]), checked_ids
