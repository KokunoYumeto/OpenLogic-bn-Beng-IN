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
    nd_node_type_fix = (
        row["unit_id"] == "OLP-0085"
        and source.count("stands below one, two, or three other sequents") == 1
        and re.search(r"ওপরে এক, দুই বা তিনটি অন্য বাক্য থাকলে", checked_target)
        is not None
        and "BN-SRC-033" in documented
    )
    nd_eigencondition_fix = (
        row["unit_id"] == "OLP-0087"
        and source.count(
            "The condition that an eigenvariable neither occur in the premises nor\n"
            "in any assumption that is !!{undischarged}"
        )
        == 1
        and re.search(
            r"\\Intro\{\\lforall\} অনুমানে আইগেনচলটি সিদ্ধান্তে.*?"
            r"\\Elim\{\\lexists\} অনুমানে সেটি প্রধান অস্তিত্বসূচক পূর্বধারণা, সিদ্ধান্ত",
            checked_target,
            re.S,
        )
        is not None
        and "BN-SRC-034" in documented
    )
    nd_end_sequent_fix = (
        row["unit_id"] == "OLP-0089"
        and source.count("!!{sentence} in the end-sequent") == 1
        and re.search(r"অন্তিম সিদ্ধান্তের\s+!!\{sentence\}", checked_target)
        is not None
        and "BN-SRC-035" in documented
    )
    nd_negation_elim_label_fix = (
        row["unit_id"] == "OLP-0089"
        and source.count("\\RightLabel{\\Intro{\\lfalse}}") == 1
        and checked_target.count("\\RightLabel{\\Intro{\\lfalse}}") == 0
        and source.count("\\RightLabel{\\Elim{\\lnot}}") == 9
        and checked_target.count("\\RightLabel{\\Elim{\\lnot}}") == 10
        and "BN-SRC-042" in documented
    )
    nd_existential_premise_fix = (
        row["unit_id"] == "OLP-0090"
        and source_math - target_math == collections.Counter({"\\lexists[x][!A(x)]": 1})
        and target_math - source_math
        == collections.Counter({"\\lexists[x][\\lnot!A(x)]": 1})
        and "BN-SRC-036" in documented
    )
    nd_existential_macro_fix = (
        row["unit_id"] == "OLP-0090"
        and source.count("\\Elim{\\exists}") == 1
        and checked_target.count("\\Elim{\\exists}") == 0
        and source.count("\\Elim{\\lexists}") == 10
        and checked_target.count("\\Elim{\\lexists}") == 11
        and "BN-SRC-037" in documented
    )
    nd_falsecl_label_fix = (
        row["unit_id"] == "OLP-0092"
        and source.count("\\RightLabel{\\FalseCl}") == 1
        and checked_target.count("\\RightLabel{\\FalseCl}") == 0
        and source.count("\\DischargeRule{\\FalseCl}{1}") == 1
        and checked_target.count("\\DischargeRule{\\FalseCl}{1}") == 1
        and "BN-SRC-038" in documented
    )
    nd_pl_semantic_object_fix = (
        row["unit_id"] == "OLP-0095"
        and source.count("!!a{structure}~\\iftag{FOL}{$\\Struct{M}$}{$\\pAssign{v}$}") == 1
        and re.search(
            r"\\iftag\{FOL\}\{কোনো !!a\{structure\}~\$\\Struct\{M\}\$\}"
            r"\{কোনো মূল্যায়ন~\$\\pAssign\{v\}\$\}",
            checked_target,
        )
        is not None
        and "BN-SRC-039" in documented
    )
    nd_forall_macro_fix = (
        row["unit_id"] == "OLP-0095"
        and source.count("\\Elim{\\forall}") == 1
        and checked_target.count("\\Elim{\\forall}") == 0
        and source.count("\\Elim{\\lforall}") == 0
        and checked_target.count("\\Elim{\\lforall}") == 1
        and "BN-SRC-040" in documented
    )
    nd_identity_reverse_case_fix = (
        row["unit_id"] == "OLP-0097"
        and source.count("Suppose the last inference in !!a{derivation} is \\Elim{\\eq}") == 1
        and re.search(
            r"দ্বিতীয় অভিন্নতা-অপসারণ বিধির ক্ষেত্রটি পদদুটির ভূমিকা অদলবদল করে\s+"
            r"একইভাবে প্রমাণিত হয়",
            checked_target,
        )
        is not None
        and "BN-SRC-041" in documented
    )
    tableau_editorial_scope_fix = (
        row["unit_id"] == "OLP-0098"
        and source.count("material relevant to natural deduction as a\nproof system, use the ``prfTab'' tag.") == 1
        and re.search(r"প্রমাণ-পদ্ধতি হিসেবে ট্যাবলো-সংক্রান্ত উপাদান অন্তর্ভুক্ত বা বাদ দিতে\s+“prfTab” ট্যাগটি ব্যবহার করো", checked_target) is not None
        and "BN-SRC-043" in documented
    )
    tableau_forall_macro_fix = (
        row["unit_id"] == "OLP-0101"
        and source.count("\\TRule{\\True}{\\forall}") == 1
        and checked_target.count("\\TRule{\\True}{\\forall}") == 0
        and source.count("\\TRule{\\False}{\\forall}") == 1
        and checked_target.count("\\TRule{\\False}{\\forall}") == 0
        and checked_target.count("\\TRule{\\True}{\\lforall}") == source.count("\\TRule{\\True}{\\lforall}") + 1
        and checked_target.count("\\TRule{\\False}{\\lforall}") == source.count("\\TRule{\\False}{\\lforall}") + 1
        and "BN-SRC-044" in documented
    )
    tableau_term_restriction_fix = (
        row["unit_id"] == "OLP-0101"
        and source.count("there are no\nrestrictions on the term~$t$.") == 1
        and re.search(r"\\TRule\{\\True\}\{\\lforall\} ও \\TRule\{\\False\}\{\\lexists\}-এ \$t\$-কে বদ্ধ\s+পদ হতে হয়, তবে তার ওপর আর কোনো নতুনত্ব-শর্ত নেই", checked_target) is not None
        and "BN-SRC-045" in documented
    )
    tableau_exercise_signed_fix = (
        row["unit_id"] == "OLP-0103"
        and source_math - target_math == collections.Counter({"\\sFmla{\\True}{!A\\lor!B,\\lnot!B},\\sFmla{\\False}{!A}": 1})
        and target_math - source_math == collections.Counter({"\\sFmla{\\True}{!A\\lor!B},\\sFmla{\\True}{\\lnot!B},\\sFmla{\\False}{!A}": 1})
        and "BN-SRC-046" in documented
    )
    tableau_closed_term_fix = (
        row["unit_id"] == "OLP-0104"
        and source.count("we can pick any term we like.") == 1
        and re.search(r"পছন্দমতো যেকোনো বদ্ধ পদ নেওয়া যায়", checked_target) is not None
        and "BN-SRC-047" in documented
    )
    tableau_reusable_line_fix = (
        row["unit_id"] == "OLP-0104"
        and source_math - target_math == collections.Counter({"3": 1})
        and target_math - source_math == collections.Counter({"4": 1})
        and "BN-SRC-048" in documented
    )
    tableau_subset_braces_fix = (
        row["unit_id"] == "OLP-0105"
        and source_math - target_math == collections.Counter({"!D_1": 1, "!D_m\\subseteq\\Gamma": 1})
        and target_math - source_math == collections.Counter({"\\{!D_1,\\dots,!D_m\\}\\subseteq\\Gamma": 1})
        and "BN-SRC-049" in documented
    )
    tableau_gamma_index_fix = (
        row["unit_id"] == "OLP-0106"
        and source_math - target_math == collections.Counter({"\\Gamma_1=\\{!C_1,\\dots,!C_n\\}\\subseteq\\Gamma": 1})
        and target_math - source_math == collections.Counter({"\\Gamma_1=\\{!C_1,\\dots,!C_m\\}\\subseteq\\Gamma": 1})
        and "BN-SRC-050" in documented
    )
    tableau_negation_premise_fix = (
        row["unit_id"] == "OLP-0106"
        and source.count("\\TRule{\\True}{\\lnot} applied to \\sFmla{\\False}{!A} after the") == 1
        and re.search(r"\\sFmla\{\\True\}\{\\lnot !A\}-তে \\TRule\{\\True\}\{\\lnot\} প্রয়োগের সিদ্ধান্ত", checked_target) is not None
        and "BN-SRC-051" in documented
    )
    tableau_left_typo_fix = (
        row["unit_id"] == "OLP-0106"
        and source.count("On the left left side, add the part of the first") == 1
        and checked_target.count("বাঁ দিকে প্রথম !!{tableau}-টির অনুমিতির নিচের অংশ যোগ করি") == 1
        and "BN-SRC-052" in documented
    )
    tableau_signed_macro_fix = (
        row["unit_id"] == "OLP-0107"
        and source.count("\\sFmla{\\True{\\formula") == 4
        and source.count("\\sFmla{\\False{\\formula") == 4
        and checked_target.count("\\sFmla{\\True{\\formula") == 0
        and checked_target.count("\\sFmla{\\False{\\formula") == 0
        and all(checked_target.count(value) == source.count(value) + 2 for value in ("\\sFmla{\\True}{\\formula{A}}", "\\sFmla{\\True}{\\formula{B}}", "\\sFmla{\\False}{\\formula{A}}", "\\sFmla{\\False}{\\formula{B}}"))
        and "BN-SRC-053" in documented
    )
    tableau_trailing_comma_fix = (
        row["unit_id"] == "OLP-0108"
        and source_math - target_math == collections.Counter({"\\sFmla{\\False}{\\formula{A}(t)},\\sFmla{\\True}{\\lforall[x][!A(x)]},": 1})
        and target_math - source_math == collections.Counter({"\\sFmla{\\False}{\\formula{A}(t)},\\sFmla{\\True}{\\lforall[x][!A(x)]}": 1})
        and "BN-SRC-054" in documented
    )
    tableau_quantifier_soundness_fix = (
        row["unit_id"] == "OLP-0109"
        and source_math - target_math == collections.Counter({"\\sFmla{\\True}{\\lforall[x][!B(x)]}\\in\\Gamma": 1, "\\sFmla{\\False}{\\lforall[x][!B(x)]}\\in\\Gamma": 1, "\\Sat/{M}{\\lforall[x][!B(x)]}": 2, "\\Sat/{M}{!B(x)}[s]": 1})
        and target_math - source_math == collections.Counter({"\\sFmla{\\True}{\\lforall[x][!A(x)]}\\in\\Gamma": 1, "\\sFmla{\\False}{\\lforall[x][!A(x)]}\\in\\Gamma": 1, "\\Sat/{M}{\\lforall[x][!A(x)]}": 2, "\\Sat/{M}{!A(x)}[s]": 1})
        and "BN-SRC-055" in documented
    )
    tableau_identity_substitution_fix = (
        row["unit_id"] == "OLP-0110"
        and source_math - target_math == collections.Counter({"\\eq[t_1][t_2]": 1})
        and target_math - source_math == collections.Counter({"\\eq[s_1][s_2]": 1})
        and "BN-SRC-056" in documented
    )
    tableau_identity_truth_sign_fix = (
        row["unit_id"] == "OLP-0111"
        and source_math - target_math == collections.Counter({"\\sFmla{S}{!A(t_2)}": 1})
        and target_math - source_math == collections.Counter({"\\sFmla{\\True}{!A(t_2)}": 1})
        and "BN-SRC-057" in documented
    )
    axd_source = source
    axd_math_ids = []
    if row["unit_id"] == "OLP-0118":
        assert axd_source.count("$B_i = !A$") == 1
        axd_source = axd_source.replace("$B_i = !A$", "$!B_i = !A$", 1)
        axd_math_ids = ["BN-SRC-058"]
    elif row["unit_id"] == "OLP-0119":
        old = "\\lif (!A \\lif !C)$;"
        assert axd_source.count(old) == 1
        axd_source = axd_source.replace(old, "\\lif (!A \\lif !C))$;", 1)
        axd_math_ids = ["BN-SRC-060"]
    elif row["unit_id"] == "OLP-0120":
        old = "\\lforall[x][!D(x)]),\\\\"
        assert axd_source.count(old) == 1
        axd_source = axd_source.replace(old, "\\lforall[x][!D(x)])),\\\\", 1)
        old = "i.e., $\\Gamma \\Proves !B$."
        assert axd_source.count(old) == 1
        axd_source = axd_source.replace(old, "i.e., $\\Gamma \\Proves !A \\lif !B$.", 1)
        axd_math_ids = ["BN-SRC-061", "BN-SRC-062"]
    elif row["unit_id"] == "OLP-0123":
        assert axd_source.count("$\\top$") == 1
        axd_source = axd_source.replace("$\\top$", "$\\ltrue$", 1)
        axd_math_ids = ["BN-SRC-065"]
    elif row["unit_id"] == "OLP-0124":
        assert axd_source.count("\\lforall[x][B(x)]") == 2
        assert axd_source.count("\\Sat{M'}{B(c)}") == 1
        axd_source = axd_source.replace("\\lforall[x][B(x)]", "\\lforall[x][!B(x)]")
        axd_source = axd_source.replace("\\Sat{M'}{B(c)}", "\\Sat{M'}{!B(c)}", 1)
        axd_math_ids = ["BN-SRC-068", "BN-SRC-069"]
    axd_math_fix = (
        bool(axd_math_ids)
        and mathparts(axd_source) == target_math
        and all(finding_id in documented for finding_id in axd_math_ids)
    )
    axd_control_source = source
    axd_control_ids = []
    if row["unit_id"] == "OLP-0122":
        axd_control_source = axd_control_source.replace(
            "\\olref[prp]{ax:land1}", "\\olref[prp]{ax:land2}", 1
        )
        axd_control_source = axd_control_source.replace(
            "\\olref[prp]{ax:lnot1}", "\\olref[prp]{ax:lnot2}", 1
        )
        axd_control_ids = ["BN-SRC-063", "BN-SRC-064"]
    axd_control_fix = (
        bool(axd_control_ids)
        and controls(axd_control_source) == controls(checked_target)
        and all(finding_id in documented for finding_id in axd_control_ids)
    )
    axd_prose_ids = []
    if row["unit_id"] == "OLP-0118":
        assert source.count("follows from previous !!{formula}s by modus ponens.") == 1
        assert re.search(
            r"আগের !!\{formula\}s থেকে অনুমোদিত কোনো\s+অনুমান-বিধি অনুসারে অনুসৃত",
            checked_target,
        ) is not None
        assert re.search(
            r"same rule which\s+justifies~\$!A_k = !A\$", source
        ) is not None
        assert re.search(
            r"\$!A_k = !A\$-র মতো একই ভিত্তিতে\s+সমর্থিত", checked_target
        ) is not None
        axd_prose_ids = ["BN-SRC-059", "BN-SRC-070"]
    elif row["unit_id"] == "OLP-0120":
        assert source.count("i.e., $\\Gamma \\Proves !B$.") == 1
        assert re.search(
            r"অর্থাৎ,?\s*\$\\Gamma \\Proves !A \\lif !B\$", checked_target
        ) is not None
        axd_prose_ids = ["BN-SRC-062"]
    elif row["unit_id"] == "OLP-0124":
        assert source.count(
            "By induction on the length of the !!{derivation} of $!A$ from"
        ) == 1
        assert re.search(
            r"অনুমান-বিধি দিয়ে সমর্থিত\s+ধাপের সংখ্যার ওপর আরোহ", checked_target
        ) is not None
        axd_prose_ids = ["BN-SRC-067"]
    elif row["unit_id"] == "OLP-0123":
        assert source.count("By the deduction theorem again, $\\Gamma \\Proves") == 1
        assert re.search(
            r"সত্য-ধ্রুবকটি স্বতঃসিদ্ধ হওয়ায় মোডাস পোনেন্স থেকে\s+\$\\Gamma \\Proves",
            checked_target,
        ) is not None
        assert source.count(
            "\\tagitem{prvEx}{$!A(t) \\Proves \\lexists[x][!A(x)]$.}{}"
        ) == 1
        assert checked_target.count("নিচের প্রতিটি বক্তব্যে দেখানো পদটি বদ্ধ:") == 1
        axd_prose_ids = ["BN-SRC-071", "BN-SRC-072"]
    elif row["unit_id"] == "OLP-0125":
        assert source.count("for any term $t$ and set~$\\Gamma$.") == 1
        assert re.search(
            r"যেকোনো বদ্ধ পদ~\$t\$ ও সেট~\$\\Gamma\$-র জন্য", checked_target
        ) is not None
        assert re.search(
            r"বদ্ধ পদদুটির জন্য \$\\Gamma \\Proves !A\(t_1\)\$", checked_target
        ) is not None
        axd_prose_ids = ["BN-SRC-066"]
    axd_prose_fix = bool(axd_prose_ids) and all(
        finding_id in documented for finding_id in axd_prose_ids
    )
    completeness_source = source
    completeness_math_ids = []
    if row["unit_id"] == "OLP-0130":
        old = "\\lforall[x_n][\\lnot !A_n]$ is defined as"
        assert completeness_source.count(old) == 1
        completeness_source = completeness_source.replace(
            old, "\\lforall[x_n][\\lnot !A_n(x_n)]$ is defined as", 1
        )
        completeness_math_ids = ["BN-SRC-073"]
    elif row["unit_id"] == "OLP-0132":
        old = "\\lforall[x][!A(x)] \\in \\Gamma^*"
        assert completeness_source.count(old) == 1
        completeness_source = completeness_source.replace(
            old, "\\lforall[x][!B(x)] \\in \\Gamma^*", 1
        )
        completeness_math_ids = ["BN-SRC-078"]
    elif row["unit_id"] == "OLP-0133":
        old = (
            "\\eq[\\Atom{f}{t_1,\\dots,t_{i-1},t,t_{i+1},,\\dots,t_n}]"
            "[\\Atom{f}{t_1,\\dots,t_{i-1},t',t_{i+1},\\dots,t_n}]"
        )
        assert completeness_source.count(old) == 1
        completeness_source = completeness_source.replace(
            old, old.replace("t_{i+1},,\\dots", "t_{i+1},\\dots"), 1
        )
        old = "\\Sat/{M}{\\Atom{R}{t}}"
        assert completeness_source.count(old) == 1
        completeness_source = completeness_source.replace(
            old, "\\Sat/{M}{\\Atom{R}{t'}}", 1
        )
        completeness_math_ids = ["BN-SRC-079", "BN-SRC-080"]
    completeness_math_fix = (
        bool(completeness_math_ids)
        and mathparts(completeness_source) == target_math
        and all(finding_id in documented for finding_id in completeness_math_ids)
    )
    completeness_control_fix = False
    if row["unit_id"] == "OLP-0130":
        old = "{}\\iftag{defAll,defEx}{}{ and }\\iftag{prvAll}{it contains an"
        assert source.count(old) == 1
        assert checked_target.count(
            "{}\\iftag{defAll,defEx}{}{ এবং\n"
            "  }\\iftag{prvEx}{সেটটিতে কোনো অস্তিত্বমূলকভাবে"
        ) == 1
        completeness_control_fix = "BN-SRC-074" in documented
    completeness_prose_ids = []
    if row["unit_id"] == "OLP-0131":
        assert source.count("Let $n$ be the largest of these.") == 1
        assert re.search(
            r"এই সসীম সেটটি ফাঁকা হলে সেটি মূল সঙ্গত\s+"
            r"সেটের উপসেট, তাই সঙ্গত.*?নইলে.*?বৃহত্তমটিকে \$n\$ ধরি",
            checked_target,
            re.S,
        ) is not None
        completeness_prose_ids = ["BN-SRC-075"]
    elif row["unit_id"] == "OLP-0132":
        assert source.count("then $\\Value{t}{M(\\Gamma^*)} = t$.") == 1
        assert re.search(
            r"তাহলে প্রতিটি বদ্ধ পদের জন্য\s+"
            r"\$\\Value\{t\}\{M\(\\Gamma\^\*\)\} = t\$",
            checked_target,
        ) is not None
        assert source.count("for all terms~$t$") == 2
        assert source.count("for at least one term~$t$") == 2
        assert re.search(
            r"\\indcase\{!A\}\{\\lforall\[x\]\[!B\(x\)\]\}.*?"
            r"সব বদ্ধ পদ~\$t\$-এর জন্য.*?সব বদ্ধ পদ~\$t\$-এর\s+জন্য",
            checked_target,
            re.S,
        ) is not None
        assert re.search(
            r"\\indcase\{!A\}\{\\lexists\[x\]\[!B\(x\)\]\}.*?"
            r"অন্তত একটি বদ্ধ পদ~\$t\$-এর জন্য.*?অন্তত একটি বদ্ধ\s+"
            r"পদ~\$t\$-এর জন্য",
            checked_target,
            re.S,
        ) is not None
        completeness_prose_ids = ["BN-SRC-076", "BN-SRC-077"]
    elif row["unit_id"] == "OLP-0133":
        assert source.count(
            "then $\\Value{t}{\\equivclass{M}{\\approx}} = \\equivrep{t}"
        ) == 1
        assert re.search(
            r"হলে প্রতিটি বদ্ধ পদের জন্য\s+"
            r"\$\\Value\{t\}\{\\equivclass\{M\}\{\\approx\}\}",
            checked_target,
        ) is not None
        completeness_prose_ids = ["BN-SRC-081"]
    elif row["unit_id"] == "OLP-0135":
        assert source.count(
            "Let $n$ be the largest number such that $!A_{\\ge n}"
        ) == 1
        assert re.search(
            r"প্রথম উপসেট-অংশটি ফাঁকা হলে~\$n\$-কে ১, আর নইলে\s+"
            r"\$!A_\{\\ge n\} \\in \\Delta\'\$ হয় এমন বৃহত্তম সংখ্যা ধরি",
            checked_target,
        ) is not None
        completeness_prose_ids = ["BN-SRC-082"]
    completeness_prose_fix = bool(completeness_prose_ids) and all(
        finding_id in documented for finding_id in completeness_prose_ids
    )
    introduction_math_ids = []
    introduction_math_fix = False
    if row["unit_id"] == "OLP-0140":
        introduction_math_ids = ["BN-SRC-083", "BN-SRC-084"]
        introduction_math_fix = (
            source_math - target_math
            == collections.Counter(
                {
                    "\\lforall[x][(!A(x)\\lif!B(x)),\\lexists[x][!A(x)]"
                    "\\Entails\\lexists[x][!B(x)]]": 1,
                    "\\lforall[x][(!A(x)\\lif!B(x))": 2,
                    "\\lexists[x][!B(x)]]": 2,
                }
            )
            and target_math - source_math
            == collections.Counter(
                {
                    "\\lforall[x][(!A(x)\\lif!B(x))],\\lexists[x][!A(x)]"
                    "\\Entails\\lexists[x][!B(x)]": 1,
                    "\\lforall[x][(!A(x)\\lif!B(x))]": 2,
                    "\\lexists[x][!B(x)]": 2,
                }
            )
            and all(finding_id in documented for finding_id in introduction_math_ids)
        )
    elif row["unit_id"] == "OLP-0143":
        introduction_math_ids = ["BN-SRC-086"]
        introduction_math_fix = (
            source_math - target_math == collections.Counter({"3": 1})
            and target_math - source_math == collections.Counter({"0": 1})
            and "BN-SRC-086" in documented
        )
    elif row["unit_id"] == "OLP-0146":
        introduction_math_ids = ["BN-SRC-087"]
        introduction_math_fix = (
            source_math - target_math
            == collections.Counter(
                {"\\lforall[\\Objv_0][\\Atom{\\ObjP}]{\\Objv_0}": 1}
            )
            and target_math - source_math
            == collections.Counter(
                {"\\lforall[\\Objv_0][\\Atom{\\ObjP}{\\Objv_0}]": 1}
            )
            and "BN-SRC-087" in documented
        )
    introduction_prose_ids = []
    if row["unit_id"] == "OLP-0143":
        assert source.count("the !!{constant}s can have more than one place") == 1
        assert re.search(
            r"!!\{predicate\}s-এর স্থানসংখ্যা একের\s+বেশি হতে পারে",
            checked_target,
        ) is not None
        assert source.count("of $1$, $2$, or~$3$)") == 1
        assert re.search(
            r"আমাদের উদাহরণে \$0\$, \$1\$ বা~\$2\$-এর\s+কোনো একটিতে",
            checked_target,
        ) is not None
        introduction_prose_ids = ["BN-SRC-085"]
    introduction_prose_fix = bool(introduction_prose_ids) and all(
        finding_id in documented for finding_id in introduction_prose_ids
    )
    introduction_token_fix = (
        row["unit_id"] == "OLP-0143"
        and semantic_tokens(source) - semantic_tokens(checked_target)
        == collections.Counter({"!!{constant}s": 1})
        and semantic_tokens(checked_target) - semantic_tokens(source)
        == collections.Counter({"!!{predicate}s": 1})
        and "BN-SRC-085" in documented
    )
    syntax_math_ids = []
    syntax_math_fix = False
    syntax_audited_source = source
    if row["unit_id"] == "OLP-0152":
        syntax_math_ids = ["BN-SRC-088"]
        old = "$\\lnot !A \\lor !B)$"
        new = "$\\lnot !A \\lor !B$"
        assert syntax_audited_source.count(old) == 1
        syntax_audited_source = syntax_audited_source.replace(old, new, 1)
        syntax_math_fix = (
            mathparts(syntax_audited_source) == target_math
            and all(finding_id in documented for finding_id in syntax_math_ids)
        )
    elif row["unit_id"] == "OLP-0154":
        syntax_math_ids = ["BN-SRC-089"]
        old = "$(!A \\land !B$)"
        new = "$(!A \\land !B)$"
        assert syntax_audited_source.count(old) == 1
        syntax_audited_source = syntax_audited_source.replace(old, new, 1)
        syntax_math_fix = (
            mathparts(syntax_audited_source) == target_math
            and all(finding_id in documented for finding_id in syntax_math_ids)
        )
    elif row["unit_id"] == "OLP-0156":
        syntax_math_ids = ["BN-SRC-090", "BN-SRC-091", "BN-SRC-092"]
        term_repairs = [
            ("m_0,\\dotsc,m_k < i", "m_0,\\dotsc,m_{k-1} < i"),
            (
                "f(t_{m_0},\\dotsc,t_{m_k})",
                "f(t_{m_0},\\dotsc,t_{m_{k-1}})",
            ),
        ]
        for old, new in term_repairs:
            assert syntax_audited_source.count(old) == 1
            syntax_audited_source = syntax_audited_source.replace(old, new, 1)
        theorem_anchor = "\\begin{thm}\n\\ollabel{thm:fseq-frm-equiv}"
        theorem_start = syntax_audited_source.index(theorem_anchor)
        syntax_prefix = syntax_audited_source[:theorem_start]
        syntax_theorem = syntax_audited_source[theorem_start:]
        assert syntax_theorem.count("\\Frm[L_0]") == 2
        syntax_theorem = syntax_theorem.replace("\\Frm[L_0]", "\\Frm[L]")
        final_member_repairs = [
            ("$!A \\ident !A_n$ is\natomic", "$!A_n$ is\natomic"),
            ("$!A \\ident \\lnot !A_j$", "$!A_n \\ident \\lnot !A_j$"),
            ("$!A \\ident (!A_j \\land !A_k)$", "$!A_n \\ident (!A_j \\land !A_k)$"),
            ("$!A \\ident (!A_j \\lor !A_k)$", "$!A_n \\ident (!A_j \\lor !A_k)$"),
            ("$!A \\ident (!A_j \\lif !A_k)$", "$!A_n \\ident (!A_j \\lif !A_k)$"),
            ("$!A \\ident (!A_j \\liff !A_k)$", "$!A_n \\ident (!A_j \\liff !A_k)$"),
            ("$!A \\ident \\lforall[x][!A_j]$", "$!A_n \\ident \\lforall[x][!A_j]$"),
            ("$!A \\ident \\lexists[x][!A_j]$", "$!A_n \\ident \\lexists[x][!A_j]$"),
            ("$!A$ is atomic", "$!A_n$ is atomic"),
            (
                "$!A \\equiv (!A_j \\land !A_k)$",
                "$!A_n \\ident (!A_j \\land !A_k)$",
            ),
        ]
        for old, new in final_member_repairs:
            assert syntax_theorem.count(old) == 1
            syntax_theorem = syntax_theorem.replace(old, new, 1)
        syntax_audited_source = syntax_prefix + syntax_theorem
        syntax_math_fix = (
            mathparts(syntax_audited_source) == target_math
            and all(finding_id in documented for finding_id in syntax_math_ids)
        )
    semantics_math_ids = []
    semantics_math_fix = False
    semantics_prose_fix = False
    semantics_audited_source = source
    if row["unit_id"] == "OLP-0163":
        semantics_math_ids = [
            "BN-SRC-093",
            "BN-SRC-094",
            "BN-SRC-095",
            "BN-SRC-096",
            "BN-SRC-097",
            "BN-SRC-098",
            "BN-SRC-099",
        ]
        semantics_repairs = [
            ("\\Assign{R}{M}[s]$.", "\\Assign{R}{M}$.", 1),
            ("\\lnot((R(b,x)", "\\lnot(R(b,x)", 2),
            (
                "\\lexists[x][(R(b,x) \\land R(x,b))],}",
                "\\lexists[x][(R(b,x) \\land R(x,b))]}",
                1,
            ),
            (
                "\\Sat/{M}{R(a,x)}[\\Subst{s}{m}{x}]$ for $m = 2$, $3$, or~$4$",
                "\\Sat/{M}{R(x,a)}[\\Subst{s}{m}{x}]$ for $m = 2$, $3$, or~$4$",
                1,
            ),
            ("and $ = 2$.", "and $m = 2$.", 1),
            (
                "So, for all $n \\in \\Domain M$, either",
                "So, for all $m \\in \\Domain M$, either",
                1,
            ),
            (
                "namely $n = 4$, so that",
                "namely $m=1$, $n=4$, $m=2$, $n=1$, so that",
                1,
            ),
        ]
        for old, new, expected_count in semantics_repairs:
            assert semantics_audited_source.count(old) == expected_count
            semantics_audited_source = semantics_audited_source.replace(old, new)
        semantics_math_fix = (
            mathparts(semantics_audited_source) == target_math
            and all(finding_id in documented for finding_id in semantics_math_ids)
        )
        semantics_prose_fix = (
            re.search(
                r"\$m = 2\$, \$3\$ ও~\$4\$ হলে\s+"
                r"\$\\Sat/\{M\}\{R\(x,a\)\}\[\\Subst\{s\}\{m\}\{x\}\]\$,\s+"
                r"তাই পূর্ববর্তীটি মিথ্যা",
                checked_target,
            )
            is not None
            and re.search(
                r"\$m=1\$ হলে \$n=4\$ এবং \$m=2\$ হলে \$n=1\$",
                checked_target,
            )
            is not None
        )
    elif row["unit_id"] == "OLP-0164":
        semantics_math_ids = ["BN-SRC-100", "BN-SRC-101"]
        semantics_repairs = [
            (
                "\\langle \\Value{t_i}{M}[s_2], \\ldots",
                "\\langle \\Value{t_1}{M}[s_2], \\ldots",
            ),
            (
                "$s_1' = \\Subst{s}{m}{x}$",
                "$s_1' = \\Subst{s_1}{m}{x}$",
            ),
            (
                "$s_2' =\n      \\Subst{s}{m}{x}$",
                "$s_2' =\n      \\Subst{s_2}{m}{x}$",
            ),
        ]
        for old, new in semantics_repairs:
            assert semantics_audited_source.count(old) == 1
            semantics_audited_source = semantics_audited_source.replace(old, new, 1)
        semantics_math_fix = (
            mathparts(semantics_audited_source) == target_math
            and all(finding_id in documented for finding_id in semantics_math_ids)
        )
    elif row["unit_id"] == "OLP-0165":
        semantics_math_ids = ["BN-SRC-102"]
        old = "$t'$~a term, and $s$~a variable"
        new = "$t'$~a term free for~$x$ in~$!A$, and $s$~a variable"
        assert semantics_audited_source.count(old) == 1
        semantics_audited_source = semantics_audited_source.replace(old, new, 1)
        semantics_math_fix = (
            mathparts(semantics_audited_source) == target_math
            and "BN-SRC-102" in documented
        )
        semantics_prose_fix = (
            re.search(
                r"\$t'\$ এমন একটি পদ যা~\$!A\$-তে\s+"
                r"\$x\$-এর জন্য মুক্ত",
                checked_target,
            )
            is not None
        )
    models_math_ids = []
    models_math_fix = False
    models_audited_source = source
    if row["unit_id"] == "OLP-0170":
        models_math_ids = ["BN-SRC-103"]
        old = r"\lforall[z](z \in x \liff z \in y)"
        new = r"\lforall[z][(z \in x \liff z \in y)]"
        assert models_audited_source.count(old) == 1
        models_audited_source = models_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0171":
        models_math_ids = ["BN-SRC-104"]
        old = "][v_2]]"
        new = "][\\Obj v_2]]"
        assert models_audited_source.count(old) == 1
        models_audited_source = models_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0172":
        models_math_ids = ["BN-SRC-105", "BN-SRC-106", "BN-SRC-107"]
        models_repairs = [
            (
                r"""\begin{align*}
 \lforall[u][(u \in f \lif {}] & \lexists[x][\lexists[y][(x \in X \land y \in
      Y \land \tuple{x, y} = u)]]) \land {}\\
 \lforall[x][(x \in X \lif {}] &
      (\lexists[y][(y \in Y \land \mathrm{maps}(f, x, y))] \land {}\\
& (\lforall[y][\lforall[y'][((\mathrm{maps}(f, x, y) \land
    \mathrm{maps}(f, x, y')) \lif y = y')]]))
\end{align*}""",
                r"""\begin{align*}
 & \lforall[u][(u \in f \lif
      \lexists[x][\lexists[y][(x \in X \land y \in
      Y \land \tuple{x, y} = u)]])] \land {}\\
 & \lforall[x][(x \in X \lif
      (\lexists[y][(y \in Y \land \mathrm{maps}(f, x, y))] \land
      \lforall[y][\lforall[y'][((\mathrm{maps}(f, x, y) \land
      \mathrm{maps}(f, x, y')) \lif y = y')]]))]
\end{align*}""",
            ),
            (
                r"""\begin{multline*}
 f \colon X \to Y \land \lforall[x][\lforall[x'][((x \in X \land x' \in
     X \land {}]] \\
 \lexists[y][(\mathrm{maps}(f, x, y) \land \mathrm{maps}(f,
        x', y))]) \lif x = x')
\end{multline*}""",
                r"""\begin{multline*}
 f \colon X \to Y \land \lforall[x][\lforall[x'][((x \in X \land x' \in
     X \land {} \\
 \lexists[y][(\mathrm{maps}(f, x, y) \land \mathrm{maps}(f,
        x', y))]) \lif x = x')]]
\end{multline*}""",
            ),
            (
                r"""\lforall[z][\lexists[y][\lforall[x][(x \in y \liff (x \in z \land
      !A(x))]]].""",
                r"""\lforall[z][\lexists[y][\lforall[x][(x \in y \liff (x \in z \land
      !A(x)))]]].""",
            ),
        ]
        for old, new in models_repairs:
            assert models_audited_source.count(old) == 1
            models_audited_source = models_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0173":
        models_math_ids = ["BN-SRC-108"]
        old = r"\lforall[y][(\eq[y][x_1] \lor \dots \lor \eq[y][x_n]]))"
        new = r"\lforall[y][(\eq[y][x_1] \lor \dots \lor \eq[y][x_n])])"
        assert models_audited_source.count(old) == 1
        models_audited_source = models_audited_source.replace(old, new, 1)
    if models_math_ids:
        models_math_fix = (
            mathparts(models_audited_source) == target_math
            and all(finding_id in documented for finding_id in models_math_ids)
        )
    beyond_math_ids = []
    beyond_math_fix = False
    beyond_audited_source = source
    if row["unit_id"] == "OLP-0176":
        beyond_math_ids = ["BN-SRC-109"]
        old = r"\lforall[a][\lforall x][(\Atom{\Obj{MarriedTo}}{a,x} \lif"
        new = r"\lforall[a][\lforall[x][(\Atom{\Obj{MarriedTo}}{a,x} \lif"
        assert beyond_audited_source.count(old) == 1
        beyond_audited_source = beyond_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0177":
        beyond_math_ids = ["BN-SRC-110"]
        old = r"\lforall[x][\lforall[y][(s(x) = s(y) \lif x = y)]]"
        new = r"\lforall[x][\lforall[y][(x' = y' \lif x = y)]]"
        assert beyond_audited_source.count(old) == 1
        beyond_audited_source = beyond_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0178":
        beyond_math_ids = ["BN-SRC-111"]
        old = r"for any~$x$ of type~$\sigma$; so item (6)"
        new = r"for any~$x$ of type~$\tau$; so item (6)"
        assert beyond_audited_source.count(old) == 1
        beyond_audited_source = beyond_audited_source.replace(old, new, 1)
    if beyond_math_ids:
        beyond_math_fix = (
            mathparts(beyond_audited_source) == target_math
            and all(finding_id in documented for finding_id in beyond_math_ids)
        )
    basics_math_ids = []
    basics_math_fix = False
    basics_audited_source = source
    if row["unit_id"] == "OLP-0187":
        basics_math_ids = ["BN-SRC-113", "BN-SRC-114"]
        old = r"\Value{t}{M'}[h \circ s] & = \Assign{f}{M}("
        new = r"\Value{t}{M'}[h \circ s] & = \Assign{f}{M'}("
        assert basics_audited_source.count(old) == 1
        basics_audited_source = basics_audited_source.replace(old, new, 1)
        old = r"& = h(\Assign{f}{M}(\Value{t_1}{M}[s], \dots, \Value{t_n}{M}[s]) \notag\\"
        new = r"& = h(\Assign{f}{M}(\Value{t_1}{M}[s], \dots, \Value{t_n}{M}[s]))\notag\\"
        assert basics_audited_source.count(old) == 1
        basics_audited_source = basics_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0189":
        basics_math_ids = ["BN-SRC-115"]
        old = "$n+1 =2r$"
        new = "$n = 2r+1$"
        assert basics_audited_source.count(old) == 1
        basics_audited_source = basics_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0190":
        basics_math_ids = ["BN-SRC-117"]
        old = r'''Given $a \in \Domain{M_1}$, find $b \in \Domain{M_2}$ as
  follows:'''
        new = r'''Given $a \in \Domain{M_1}$, if $a$ is already in the domain of
  $p$, take $q=p$. Otherwise find $b \in \Domain{M_2}$ as follows; if
  $p$ is empty, take any $b$, and if $p$ is non-empty:'''
        assert basics_audited_source.count(old) == 1
        basics_audited_source = basics_audited_source.replace(old, new, 1)
    if basics_math_ids:
        basics_math_fix = (
            mathparts(basics_audited_source) == target_math
            and all(finding_id in documented for finding_id in basics_math_ids)
        )
    basics_prose_ids = []
    basics_prose_fix = False
    if row["unit_id"] == "OLP-0185":
        assert source.count(
            "then any $N\n\\subseteq \\Domain{M}$ determines a sub!!{structure}"
        ) == 1
        basics_prose_fix = (
            re.search(
                r"যেকোনো অশূন্য \$N\s+\\subseteq \\Domain\{M\}\$ "
                r"সেট~?\$\\Struct M\$-এর একটি\s+উপ!!\{structure\}",
                checked_target,
            )
            is not None
        )
        basics_prose_ids = ["BN-SRC-112"]
    elif row["unit_id"] == "OLP-0189":
        assert source.count(
            "$!T^a_n$ is finite, so we can\n"
            "  assume it is a single first-order !!{formula}."
        ) == 1
        basics_prose_fix = (
            re.search(
                r"\$!T\^a_n\$ যৌক্তিক সমতুল্যতা-অবধি সসীম.*?"
                r"সসীম সংযোজনকে আমরা\s+একটিমাত্র প্রথম-ক্রমের !!\{formula\}",
                checked_target,
                re.S,
            )
            is not None
        )
        basics_prose_ids = ["BN-SRC-116"]
    if 112 <= int(row["unit_id"].split("-")[1]) <= 125:
        expected_axd = {
            "OLP-0118": {"BN-SRC-058", "BN-SRC-059", "BN-SRC-070"},
            "OLP-0119": {"BN-SRC-060"},
            "OLP-0120": {"BN-SRC-061", "BN-SRC-062"},
            "OLP-0122": {"BN-SRC-063", "BN-SRC-064"},
            "OLP-0123": {"BN-SRC-065", "BN-SRC-071", "BN-SRC-072"},
            "OLP-0124": {"BN-SRC-067", "BN-SRC-068", "BN-SRC-069"},
            "OLP-0125": {"BN-SRC-066"},
        }
        assert set(documented) == expected_axd.get(row["unit_id"], set())
    if 126 <= int(row["unit_id"].split("-")[1]) <= 137:
        expected_completeness = {
            "OLP-0130": {"BN-SRC-073", "BN-SRC-074"},
            "OLP-0131": {"BN-SRC-075"},
            "OLP-0132": {"BN-SRC-076", "BN-SRC-077", "BN-SRC-078"},
            "OLP-0133": {"BN-SRC-079", "BN-SRC-080", "BN-SRC-081"},
            "OLP-0135": {"BN-SRC-082"},
        }
        assert set(documented) == expected_completeness.get(row["unit_id"], set())
    if 138 <= int(row["unit_id"].split("-")[1]) <= 148:
        expected_introduction = {
            "OLP-0140": {"BN-SRC-083", "BN-SRC-084"},
            "OLP-0143": {"BN-SRC-085", "BN-SRC-086"},
            "OLP-0146": {"BN-SRC-087"},
        }
        assert set(documented) == expected_introduction.get(row["unit_id"], set())
    if 149 <= int(row["unit_id"].split("-")[1]) <= 158:
        expected_syntax = {
            "OLP-0152": {"BN-SRC-088"},
            "OLP-0154": {"BN-SRC-089"},
            "OLP-0156": {"BN-SRC-090", "BN-SRC-091", "BN-SRC-092"},
        }
        assert set(documented) == expected_syntax.get(row["unit_id"], set())
    if 159 <= int(row["unit_id"].split("-")[1]) <= 166:
        expected_semantics = {
            "OLP-0163": {
                "BN-SRC-093",
                "BN-SRC-094",
                "BN-SRC-095",
                "BN-SRC-096",
                "BN-SRC-097",
                "BN-SRC-098",
                "BN-SRC-099",
            },
            "OLP-0164": {"BN-SRC-100", "BN-SRC-101"},
            "OLP-0165": {"BN-SRC-102"},
        }
        assert set(documented) == expected_semantics.get(row["unit_id"], set())
    if 167 <= int(row["unit_id"].split("-")[1]) <= 173:
        expected_models = {
            "OLP-0170": {"BN-SRC-103"},
            "OLP-0171": {"BN-SRC-104"},
            "OLP-0172": {"BN-SRC-105", "BN-SRC-106", "BN-SRC-107"},
            "OLP-0173": {"BN-SRC-108"},
        }
        assert set(documented) == expected_models.get(row["unit_id"], set())
    if 174 <= int(row["unit_id"].split("-")[1]) <= 181:
        expected_beyond = {
            "OLP-0176": {"BN-SRC-109"},
            "OLP-0177": {"BN-SRC-110"},
            "OLP-0178": {"BN-SRC-111"},
        }
        assert set(documented) == expected_beyond.get(row["unit_id"], set())
    if 182 <= int(row["unit_id"].split("-")[1]) <= 190:
        expected_basics = {
            "OLP-0185": {"BN-SRC-112"},
            "OLP-0187": {"BN-SRC-113", "BN-SRC-114"},
            "OLP-0189": {"BN-SRC-115", "BN-SRC-116"},
            "OLP-0190": {"BN-SRC-117"},
        }
        assert set(documented) == expected_basics.get(row["unit_id"], set())
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
    elif row["unit_id"] == "OLP-0085":
        assert nd_node_type_fix
        tex_command_check = {
            "documented_prose_correction": "BN-SRC-033",
            "natural_deduction_upper_nodes_are_sentences": True,
        }
    elif row["unit_id"] == "OLP-0087":
        assert nd_eigencondition_fix
        tex_command_check = {
            "documented_prose_correction": "BN-SRC-034",
            "rule_specific_eigenvariable_conditions_restated": True,
        }
    elif row["unit_id"] == "OLP-0089":
        assert nd_end_sequent_fix and nd_negation_elim_label_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-035", "BN-SRC-042"],
            "terminal_conclusion_terminology_restored": True,
            "negation_elimination_rule_label_restored": True,
        }
    elif row["unit_id"] == "OLP-0090":
        assert nd_existential_premise_fix and nd_existential_macro_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-036", "BN-SRC-037"],
            "negated_existential_major_premise_restored": True,
            "configurable_existential_elimination_symbol_restored": True,
        }
    elif row["unit_id"] == "OLP-0092":
        assert nd_falsecl_label_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-038",
            "duplicate_falsecl_label_removed": True,
        }
    elif row["unit_id"] == "OLP-0095":
        assert nd_pl_semantic_object_fix and nd_forall_macro_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-039", "BN-SRC-040"],
            "propositional_semantic_object_is_valuation": True,
            "configurable_universal_elimination_symbol_restored": True,
        }
    elif row["unit_id"] == "OLP-0097":
        assert nd_identity_reverse_case_fix
        tex_command_check = {
            "documented_prose_correction": "BN-SRC-041",
            "reverse_identity_elimination_case_supplied": True,
        }
    elif row["unit_id"] == "OLP-0098":
        assert tableau_editorial_scope_fix
        tex_command_check = {"documented_prose_correction": "BN-SRC-043", "prfTab_controls_tableaux": True}
    elif row["unit_id"] == "OLP-0101":
        assert tableau_forall_macro_fix and tableau_term_restriction_fix
        tex_command_check = {"documented_corrections": ["BN-SRC-044", "BN-SRC-045"], "configurable_universal_labels_restored": 2, "closed_term_restriction_retained": True}
    elif row["unit_id"] == "OLP-0103":
        assert tableau_exercise_signed_fix
        tex_command_check = {"documented_correction": "BN-SRC-046", "separated_signed_formulas": 3}
    elif row["unit_id"] == "OLP-0104":
        assert tableau_closed_term_fix and tableau_reusable_line_fix
        tex_command_check = {"documented_corrections": ["BN-SRC-047", "BN-SRC-048"], "closed_term_restriction_restored": True, "reusable_line_restored": 4}
    elif row["unit_id"] == "OLP-0105":
        assert tableau_subset_braces_fix
        tex_command_check = {"documented_correction": "BN-SRC-049", "finite_subset_braces_restored": True}
    elif row["unit_id"] == "OLP-0106":
        assert tableau_gamma_index_fix and tableau_negation_premise_fix and tableau_left_typo_fix
        tex_command_check = {"documented_corrections": ["BN-SRC-050", "BN-SRC-051", "BN-SRC-052"], "gamma_one_final_index": "m", "true_negation_premise_restored": True, "duplicated_left_removed": True}
    elif row["unit_id"] == "OLP-0107":
        assert tableau_signed_macro_fix
        tex_command_check = {"documented_correction": "BN-SRC-053", "repaired_two_argument_signed_formula_calls": 8}
    elif row["unit_id"] == "OLP-0108":
        assert tableau_trailing_comma_fix
        tex_command_check = {"documented_correction": "BN-SRC-054", "trailing_formula_list_comma_removed": True}
    elif row["unit_id"] == "OLP-0109":
        assert tableau_quantifier_soundness_fix
        tex_command_check = {"documented_correction": "BN-SRC-055", "universal_schema_metavariable_normalized": "A"}
    elif row["unit_id"] == "OLP-0110":
        assert tableau_identity_substitution_fix
        tex_command_check = {"documented_correction": "BN-SRC-056", "identity_substitution_instance": "\\eq[s_1][s_2]"}
    elif row["unit_id"] == "OLP-0111":
        assert tableau_identity_truth_sign_fix
        tex_command_check = {"documented_correction": "BN-SRC-057", "identity_rule_sign": "True"}
    elif row["unit_id"] == "OLP-0118":
        assert axd_math_fix and axd_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-058", "BN-SRC-059", "BN-SRC-070"],
            "formula_prefix_restored": True,
            "all_permitted_inference_rules_covered": True,
            "repeated_formula_uses_same_justification_basis": True,
        }
    elif row["unit_id"] == "OLP-0119":
        assert axd_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-060",
            "conditional_parenthesis_balanced": True,
        }
    elif row["unit_id"] == "OLP-0120":
        assert axd_math_fix and axd_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-061", "BN-SRC-062"],
            "quantified_conditional_parenthesis_balanced": True,
            "deduction_theorem_conclusion_restored": "\\Gamma \\Proves !A \\lif !B",
        }
    elif row["unit_id"] == "OLP-0122":
        assert axd_control_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-063", "BN-SRC-064"],
            "conjunction_projection_reference": "ax:land2",
            "negation_reference": "ax:lnot2",
        }
    elif row["unit_id"] == "OLP-0123":
        assert axd_math_fix and axd_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-065", "BN-SRC-071", "BN-SRC-072"],
            "configurable_truth_constant": "\\ltrue",
            "strong_generalization_final_step": "truth axiom plus modus ponens",
            "quantifier_instantiation_scope": "closed terms",
        }
    elif row["unit_id"] == "OLP-0124":
        assert axd_math_fix and axd_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-067", "BN-SRC-068", "BN-SRC-069"],
            "induction_measure": "inference-justified steps",
            "formula_prefixes_restored": 3,
        }
    elif row["unit_id"] == "OLP-0125":
        assert axd_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-066",
            "identity_axiom_scope": "closed terms",
        }
    elif row["unit_id"] == "OLP-0130":
        assert completeness_math_fix and completeness_control_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-073", "BN-SRC-074"],
            "formula_argument_restored": "x_n",
            "existential_configuration_tag": "prvEx",
        }
    elif row["unit_id"] == "OLP-0131":
        assert completeness_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-075",
            "empty_finite_subset_handled_before_maximum": True,
        }
    elif row["unit_id"] == "OLP-0132":
        assert completeness_math_fix and completeness_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-076", "BN-SRC-077", "BN-SRC-078"],
            "term_scope": "closed terms",
            "universal_truth_lemma_metavariable": "B",
        }
    elif row["unit_id"] == "OLP-0133":
        assert completeness_math_fix and completeness_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-079", "BN-SRC-080", "BN-SRC-081"],
            "duplicate_argument_comma_removed": True,
            "alternative_representative": "t'",
            "term_scope": "closed terms",
        }
    elif row["unit_id"] == "OLP-0135":
        assert completeness_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-082",
            "empty_delta_subfamily_index": 1,
        }
    elif row["unit_id"] == "OLP-0140":
        assert introduction_math_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-083", "BN-SRC-084"],
            "balanced_entailment_formula": True,
            "balanced_derivation_formulas": 4,
        }
    elif row["unit_id"] == "OLP-0143":
        assert introduction_math_fix and introduction_prose_fix and introduction_token_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-085", "BN-SRC-086"],
            "arity_bearer": "predicate",
            "assignment_values": [0, 1, 2],
        }
    elif row["unit_id"] == "OLP-0146":
        assert introduction_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-087",
            "restored_predicate_argument": "\\Obj v_0",
        }
    elif row["unit_id"] == "OLP-0152":
        assert syntax_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-088",
            "conditional_abbreviation_parenthesis_balanced": True,
        }
    elif row["unit_id"] == "OLP-0154":
        assert syntax_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-089",
            "conjunction_example_math_delimiters_balanced": True,
        }
    elif row["unit_id"] == "OLP-0156":
        assert syntax_math_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-090", "BN-SRC-091", "BN-SRC-092"],
            "k_ary_function_argument_count": "k",
            "theorem_language": "L",
            "formation_sequence_final_member": "!A_n",
            "syntactic_identity_relation": "\\ident",
        }
    elif row["unit_id"] == "OLP-0163":
        assert semantics_math_fix and semantics_prose_fix
        tex_command_check = {
            "documented_corrections": semantics_math_ids,
            "relation_interpretation_assignment_removed": True,
            "defined_existential_parentheses_balanced": 2,
            "defined_existential_formula_comma_removed": True,
            "universal_conditional_antecedent_restored": True,
            "missing_quantifier_variable_restored": "m",
            "universal_summary_variable": "m",
            "counterexamples": {"m=1": "n=4", "m=2": "n=1"},
        }
    elif row["unit_id"] == "OLP-0164":
        assert semantics_math_fix
        tex_command_check = {
            "documented_corrections": semantics_math_ids,
            "predicate_tuple_first_index": "t_1",
            "universal_assignment_variants": ["s_1", "s_2"],
        }
    elif row["unit_id"] == "OLP-0165":
        assert semantics_math_fix and semantics_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-102",
            "formula_substitution_free_for_hypothesis": True,
        }
    elif row["unit_id"] == "OLP-0176":
        assert beyond_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-109",
            "inner_universal_variable_delimiter_restored": True,
        }
    elif row["unit_id"] == "OLP-0177":
        assert beyond_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-110",
            "declared_successor_notation_restored": "prime",
        }
    elif row["unit_id"] == "OLP-0178":
        assert beyond_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-111",
            "lambda_domain_type_restored": "tau",
        }
    elif row["unit_id"] == "OLP-0185":
        assert basics_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-112",
            "substructure_domain_required_nonempty": True,
        }
    elif row["unit_id"] == "OLP-0187":
        assert basics_math_fix
        tex_command_check = {
            "documented_corrections": basics_math_ids,
            "recursive_term_value_structure": "M'",
            "homomorphism_function_parenthesis_balanced": True,
        }
    elif row["unit_id"] == "OLP-0189":
        assert basics_math_fix and basics_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-115", "BN-SRC-116"],
            "back_and_forth_even_step_index": "n=2r+1",
            "finite_conjunction_basis": "logical-equivalence representatives",
        }
    elif row["unit_id"] == "OLP-0190":
        assert basics_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-117",
            "forth_empty_map_case": True,
            "forth_already_mapped_case": True,
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
            nd_existential_premise_fix,
            tableau_exercise_signed_fix,
            tableau_reusable_line_fix,
            tableau_subset_braces_fix,
            tableau_gamma_index_fix,
            tableau_trailing_comma_fix,
            tableau_quantifier_soundness_fix,
            tableau_identity_substitution_fix,
            tableau_identity_truth_sign_fix,
            axd_math_fix,
            completeness_math_fix,
            introduction_math_fix,
            syntax_math_fix,
            semantics_math_fix,
            models_math_fix,
            beyond_math_fix,
            basics_math_fix,
            shared_audit_fix,
        )
    )
    controls_ok = (
        controls(source) == controls(checked_target)
        or axd_control_fix
        or completeness_control_fix
    )
    checks = {
        "unit_id": row["unit_id"],
        "source_blocks": len(source_blocks),
        "target_blocks": len(target_blocks),
        "math_parity": math_ok,
        "controls_parity": controls_ok,
        "env_parity": environments(source) == environments(checked_target),
        "token_parity": (
            semantic_tokens(source) == semantic_tokens(checked_target)
            or introduction_token_fix
        ),
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
