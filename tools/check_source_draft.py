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
    sequent_index_fix = (
        row["unit_id"] == "OLP-0065"
        and source_math - target_math
        == collections.Counter({"!A_1,\\dots,!A_m\\Sequent!B_1,\\dots,!B_m,": 1})
        and target_math - source_math
        == collections.Counter({"!A_1,\\dots,!A_m\\Sequent!B_1,\\dots,!B_n,": 1})
        and "BN-SRC-021" in documented
    )
    tableau_false_and_fix = (
        row["unit_id"] == "OLP-0067"
        and source_math - target_math
        == collections.Counter({"\\TRule{\\False}{!A\\land!B}": 1})
        and target_math - source_math
        == collections.Counter({"\\TRule{\\False}{\\land}": 1})
        and "BN-SRC-022" in documented
    )
    tableau_tree_label_fix = (
        row["unit_id"] == "OLP-0067"
        and source.count("\\TRule{\\True}{\\lif}[2]") == 2
        and checked_target.count("\\TRule{\\True}{\\lif}[2]") == 0
        and source.count("\\TRule{\\True}{\\land}[2]") == 0
        and checked_target.count("\\TRule{\\True}{\\land}[2]") == 2
        and "BN-SRC-023" in documented
    )
    tableau_consistency_scope_fix = (
        row["unit_id"] == "OLP-0067"
        and source.count("for some $!B_i \\in \\Gamma$.") == 1
        and re.search(
            r"প্রত্যেক সূচকের জন্য\s+\$!B_i \\in \\Gamma\$ হয়",
            checked_target,
        )
        is not None
        and "BN-SRC-024" in documented
    )
    sequent_exchange_side_fix = (
        row["unit_id"] == "OLP-0075"
        and source.count("\\RightLabel{\\RightR{\\Exchange}}") == 6
        and checked_target.count("\\RightLabel{\\RightR{\\Exchange}}") == 2
        and source.count("\\RightLabel{\\LeftR{\\Exchange}}") == 6
        and checked_target.count("\\RightLabel{\\LeftR{\\Exchange}}") == 10
        and "BN-SRC-025" in documented
    )
    de_morgan_prose_fix = (
        row["unit_id"] == "OLP-0075"
        and source_math - target_math
        == collections.Counter(
            {
                "!A,\\lnot!A\\lor!B\\Sequent\\quad": 1,
                "!B,\\lnot!A\\lor!B\\Sequent\\quad": 1,
            }
        )
        and target_math - source_math
        == collections.Counter(
            {
                "!A,\\lnot!A\\lor\\lnot!B\\Sequent\\quad": 1,
                "!B,\\lnot!A\\lor\\lnot!B\\Sequent\\quad": 1,
            }
        )
        and "BN-SRC-026" in documented
    )
    sequent_editorial_scope_fix = (
        row["unit_id"] == "OLP-0077"
        and source.count(
            "This section collects the definitions of the provability relation and\n"
            "  consistency for natural deduction."
        )
        == 1
        and re.search(
            r"এই অংশে সিকোয়েন্ট কলনের প্রমাণযোগ্যতা-সম্পর্ক ও সঙ্গতির সংজ্ঞাগুলি\s+একত্র করা হয়েছে",
            checked_target,
        )
        is not None
        and "BN-SRC-027" in documented
    )
    conjunction_context_fix = (
        row["unit_id"] == "OLP-0079"
        and not (source_math - target_math)
        and target_math - source_math
        == collections.Counter(
            {
                "!A,!B\\fCenter!A": 1,
                "!A,!B\\fCenter!B": 1,
            }
        )
        and source.count("\\doubleLine") == 2
        and checked_target.count("\\doubleLine") == 4
        and "BN-SRC-028" in documented
    )
    soundness_formula_fixes = (
        row["unit_id"] == "OLP-0081"
        and source_math - target_math
        == collections.Counter(
            {
                "\\Gamma\\Sequent\\Delta": 1,
                "\\Pi\\setminus\\Lambda": 1,
            }
        )
        and target_math - source_math
        == collections.Counter(
            {
                "!A\\land!B,\\Gamma\\Sequent\\Delta": 1,
                "\\Pi\\Sequent\\Lambda": 1,
            }
        )
        and "BN-SRC-029" in documented
        and "BN-SRC-030" in documented
    )
    weakening_branch_scope_fix = (
        row["unit_id"] == "OLP-0081"
        and source.count(
            "then $!C \\in \\Theta$ as well since $\\Theta = !A, \\Gamma$, and so"
        )
        == 1
        and re.search(
            r"বাঁ দুর্বলীকরণের ক্ষেত্রে\s+\$\\Theta = !A, \\Gamma\$; ডান\s+দুর্বলীকরণের ক্ষেত্রেও \$!C \\in \\Theta\$",
            checked_target,
        )
        is not None
        and "BN-SRC-031" in documented
    )
    identity_reverse_case_fix = (
        row["unit_id"] == "OLP-0083"
        and source.count("Suppose the last inference in !!a{derivation} is $=$.") == 1
        and source.count(
            "the premise\nis $\\eq[t_1][t_2], \\Gamma \\Sequent \\Delta, !A(t_1)$ and the conclusion"
        )
        == 1
        and re.search(
            r"অভিন্নতার দ্বিতীয় বিধির ক্ষেত্রটি পদদুটির ভূমিকা অদলবদল করে একইভাবে\s+প্রমাণিত হয়",
            checked_target,
        )
        is not None
        and "BN-SRC-032" in documented
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
    elif row["unit_id"] == "OLP-0067":
        assert tableau_tree_label_fix and tableau_consistency_scope_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-023",
            "source_true_conditional_rule_labels": 2,
            "target_true_conditional_rule_labels": 0,
            "source_true_conjunction_rule_labels": 0,
            "target_true_conjunction_rule_labels": 2,
            "documented_prose_correction": "BN-SRC-024",
            "all_displayed_assumptions_required_in_gamma": True,
        }
    elif row["unit_id"] == "OLP-0075":
        assert sequent_exchange_side_fix and de_morgan_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-025",
            "source_right_exchange_labels": 6,
            "target_right_exchange_labels": 2,
            "source_left_exchange_labels": 6,
            "target_left_exchange_labels": 10,
            "documented_math_correction": "BN-SRC-026",
            "restored_negated_second_disjuncts": 2,
        }
    elif row["unit_id"] == "OLP-0077":
        assert sequent_editorial_scope_fix
        tex_command_check = {
            "documented_prose_correction": "BN-SRC-027",
            "source_misidentified_system": "natural deduction",
            "target_contextual_system": "sequent calculus",
        }
    elif row["unit_id"] == "OLP-0079":
        assert conjunction_context_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-028",
            "added_shared_context_premises": 2,
            "source_double_inference_lines": 2,
            "target_double_inference_lines": 4,
        }
    elif row["unit_id"] == "OLP-0081":
        assert soundness_formula_fixes and weakening_branch_scope_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-029", "BN-SRC-030", "BN-SRC-031"],
            "restored_left_conjunction_conclusion": "!A\\land!B,\\Gamma\\Sequent\\Delta",
            "restored_cut_right_residual_sequent": "\\Pi\\Sequent\\Lambda",
            "weakening_antecedent_equality_restricted_to_left_branch": True,
        }
    elif row["unit_id"] == "OLP-0083":
        assert identity_reverse_case_fix
        tex_command_check = {
            "documented_prose_correction": "BN-SRC-032",
            "reverse_identity_rule_case_supplied": True,
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
            sequent_index_fix,
            tableau_false_and_fix,
            de_morgan_prose_fix,
            conjunction_context_fix,
            soundness_formula_fixes,
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
