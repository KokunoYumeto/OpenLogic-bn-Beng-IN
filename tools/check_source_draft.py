"""Replay source/translation structural and mathematical checks for the public draft."""

import collections
import hashlib
import json
import os
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


def formal_rule_bodies(text):
    return [
        norm(fragment)
        for fragment in re.findall(
            r"\\begin\{defish\}.*?\\end\{defish\}", text, flags=re.S
        )
    ]


def sideways_derivation_before_caption(text):
    matches = re.findall(
        r"\\begin\{sidewaysfigure\}(.*?)\\caption\{", text, flags=re.S
    )
    return [norm(fragment) for fragment in matches]


def without_documented_corrections(text):
    return re.sub(
        r"% (?:OLFUN-\d+|BN-SRC-\d+|BN-NORM-\d+|OLSIZ-\d+) TARGET-(?:CORRECTION|NORMALIZATION)-BEGIN.*?"
        r"% (?:OLFUN-\d+|BN-SRC-\d+|BN-NORM-\d+|OLSIZ-\d+) TARGET-(?:CORRECTION|NORMALIZATION)-END",
        "",
        text,
        flags=re.S,
    )


def body(text):
    return text.split("\\begin{document}", 1)[1].rsplit("\\end{document}", 1)[0]


def mathparts(text):
    output = []
    pattern = re.compile(
        r"(?<!\\)\$(.*?)(?<!\\)\$|(?<!\\)\\\[(.*?)\\\]|"
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
        while caption := re.search(r"\\(?:text|textrm|emph|mbox)\s*\{", fragment):
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


def mathparts_with_setbuilder_text_math(text, binder="x"):
    """Handle set-builder captions that contain legacy nested dollar math."""
    nested = collections.Counter()
    needle = f"$\\Setabs{{{binder}}}{{\\text{{"
    while needle in text:
        start = text.index(needle)
        content_start = start + len(needle)
        depth = 1
        end = content_start
        while depth and end < len(text):
            if text[end] in "{}" and (end == 0 or text[end - 1] != "\\"):
                depth += 1 if text[end] == "{" else -1
            end += 1
        assert depth == 0, "Unclosed set-builder text caption"
        assert text[end : end + 2] == "}$", "Unexpected set-builder caption ending"
        nested.update(mathparts(text[content_start : end - 1]))
        text = text[:start] + f"$\\Setabs{{{binder}}}{{}}$" + text[end + 2 :]
    return mathparts(text) + nested


def mathparts_with_tarski_quotation(text):
    """Handle the legacy nested-dollar quote inside Tarski's outer formula."""
    quoted = "$T(\\text{`$X$'})$"
    assert text.count(quoted) == 1, "Unexpected Tarski quotation count"
    return mathparts(text.replace(quoted, "$T(\\text{})$")) + collections.Counter({"X": 1})


def mathparts_with_modal_canonical_setbuilder(text):
    """Handle the frozen nested-dollar Sigma in the canonical-world caption."""
    nested = re.compile(r"\\text\{[^{}]*\$\\Sigma\$[^{}]*\}")
    prepared, count = nested.subn(r"\text{}", text)
    assert count <= 1
    return mathparts(prepared) + collections.Counter({r"\Sigma": count})


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
    if row["unit_id"] in {"OLP-0248", "OLP-0310"}:
        binder = "x" if row["unit_id"] == "OLP-0248" else "!A"
        source_math = mathparts_with_setbuilder_text_math(source, binder=binder)
        target_math = mathparts_with_setbuilder_text_math(checked_target, binder=binder)
    elif row["unit_id"] == "OLP-0321":
        source_math = mathparts_with_tarski_quotation(source)
        target_math = mathparts_with_tarski_quotation(checked_target)
    elif row["unit_id"] == "OLP-0446":
        source_math = mathparts_with_modal_canonical_setbuilder(source)
        target_math = mathparts_with_modal_canonical_setbuilder(checked_target)
    else:
        source_math = mathparts(source)
        target_math = mathparts(checked_target)
    documented = sorted(
        set(re.findall(r"(?:OLFUN-\d+|BN-SRC-\d+|OLSIZ-\d+)", target))
    )
    normalizations = sorted(set(re.findall(r"BN-NORM-\d+", target)))
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
    arithmetic_math_ids = []
    arithmetic_math_fix = False
    arithmetic_audited_source = source
    if row["unit_id"] == "OLP-0192":
        arithmetic_math_ids = ["BN-SRC-118", "BN-SRC-119", "BN-SRC-120"]
        old = r"\Assign{+}{M}(n, m)"
        new = r"\Assign{+}{M}(a^n, a^m)"
        assert arithmetic_audited_source.count(old) == 1
        arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
        old = r"\Assign{\times}{M}(n, m) & = a^{nm}"
        new = (
            r"\Assign{\times}{M}(a^n, a^m) & = a^{nm}\\" + "\n"
            r"  \Assign{<}{M} & = \Setabs{\tuple{a^n,a^m}}{n<m}"
        )
        assert arithmetic_audited_source.count(old) == 1
        arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
        old = r"\lexists[x][\OPrf[\Th{PA}](\gn{\lfalse})]"
        new = r"\lexists[x][\OPrf[\Th{PA}](x, \gn{\lfalse})]"
        assert arithmetic_audited_source.count(old) == 1
        arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0195":
        arithmetic_math_ids = ["BN-SRC-125", "BN-SRC-126", "BN-SRC-127"]
        arithmetic_repairs = [
            ("$y = b$", "$y = a$"),
            (r"(b \nsplus y)^\nssucc", r"(b \nsplus a)^\nssucc"),
            (r"$a \nsless n$", r"$x \nsless n$"),
        ]
        for old, new in arithmetic_repairs:
            assert arithmetic_audited_source.count(old) == 1
            arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0196":
        arithmetic_math_ids = ["BN-SRC-128", "BN-SRC-130"]
        old = r"\lforall[x][\lforall[y][((x < y \lor y < x) \lor \eq[x][y]))]]"
        new = r"\lforall[x][\lforall[y][((x < y \lor y < x) \lor \eq[x][y])]]"
        assert arithmetic_audited_source.count(old) == 1
        arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
        assert arithmetic_audited_source.count(r"\oplus") == 4
        arithmetic_audited_source = arithmetic_audited_source.replace(
            r"\oplus", r"\nsplus"
        )
    elif row["unit_id"] == "OLP-0197":
        arithmetic_math_ids = ["BN-SRC-132"]
        old = r"\Setabs{\tuple{x,a}}{n \in \Domain{K}}"
        new = r"\Setabs{\tuple{x,a}}{x \in \Domain{K}}"
        assert arithmetic_audited_source.count(old) == 1
        arithmetic_audited_source = arithmetic_audited_source.replace(old, new, 1)
    if arithmetic_math_ids:
        arithmetic_math_fix = (
            mathparts(arithmetic_audited_source) == target_math
            and all(finding_id in documented for finding_id in arithmetic_math_ids)
        )
    interpolation_math_ids = []
    interpolation_math_fix = False
    interpolation_audited_source = source
    if row["unit_id"] == "OLP-0200":
        interpolation_math_ids = ["BN-SRC-134", "BN-SRC-135"]
        interpolation_repairs = [
            (
                r"$\lforall[x][!C]" + "\n" + r"\Entails \lnot \delta$",
                r"$\lforall[x][!C]" + "\n" + r"\Entails \lnot !H$",
            ),
            (
                r"$\Gamma \cup \{\lexists[x]{!S} \}$",
                r"$\Gamma \cup \{\lexists[x][!S] \}$",
            ),
        ]
        for old, new in interpolation_repairs:
            assert interpolation_audited_source.count(old) == 1
            interpolation_audited_source = interpolation_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0201":
        interpolation_math_ids = ["BN-SRC-136"]
        old = r"$\Assign{P}{M} = h(\Assign{P}{M'_2})$"
        new = r"$\Assign{P}{M} = h(\Assign{P}{M'_1})$"
        assert interpolation_audited_source.count(old) == 1
        interpolation_audited_source = interpolation_audited_source.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0202":
        interpolation_math_ids = ["BN-SRC-137"]
        old = (
            r"$!D(P) \land" + "\n" +
            r"!D(P') \Entails \Atom{P}{c_1, \dots, c_n} \to P'c_1\dots c_n$"
        )
        new = (
            r"$!D(P) \land" + "\n" +
            r"!D(P') \Entails \Atom{P}{c_1, \dots, c_n} \to \Atom{P'}{c_1, \dots, c_n}$"
        )
        assert interpolation_audited_source.count(old) == 1
        interpolation_audited_source = interpolation_audited_source.replace(old, new, 1)
    if interpolation_math_ids:
        interpolation_math_fix = (
            mathparts(interpolation_audited_source) == target_math
            and all(finding_id in documented for finding_id in interpolation_math_ids)
        )
    interpolation_prose_ids = []
    interpolation_prose_fix = False
    if row["unit_id"] == "OLP-0202":
        assert source.count("if and only $\\Sigma(P)$") == 1
        interpolation_prose_ids = ["BN-SRC-138"]
        interpolation_prose_fix = (
            "যদি এবং কেবল যদি $\\Sigma(P)$" in checked_target
            and "$P$-কে প্রকাশ্যভাবে সংজ্ঞায়িত করে" in checked_target
        )
    arithmetic_prose_ids = []
    arithmetic_prose_fix = False
    if row["unit_id"] == "OLP-0193":
        assert source.count('not in the domain\nof~$s$') == 1
        arithmetic_prose_ids = ["BN-SRC-121"]
        arithmetic_prose_fix = "বিস্তৃতিতে নেই" in checked_target
    elif row["unit_id"] == "OLP-0194":
        assert source.count('Suppose $k$ is\nthe largest number') == 1
        arithmetic_prose_ids = ["BN-SRC-122", "BN-SRC-123"]
        arithmetic_prose_fix = (
            "একটিও বাক্য না থাকলে ধ্রুবকটির যেকোনো ব্যাখ্যা চলবে" in checked_target
            and "নিম্নগামী লোয়েনহাইম--স্কোলেম উপপাদ্যে মডেলটি গণনীয় নেওয়া যায়"
            in checked_target
        )
    elif row["unit_id"] == "OLP-0195":
        assert source.count('(the ``sum\'\'\nof $x$ and $y$ in~$\\Struct{K}$,') == 1
        arithmetic_prose_ids = ["BN-SRC-124"]
        arithmetic_prose_fix = re.search(r"``যোগফল''\) বদলে", checked_target) is not None
    elif row["unit_id"] == "OLP-0196":
        assert source.count("For any $x$, there is a unique $y$") == 1
        assert source.count(
            "The non-standard blocks are therefore ordered like the rationals"
        ) == 1
        arithmetic_prose_ids = ["BN-SRC-129", "BN-SRC-131"]
        arithmetic_prose_fix = (
            len(re.findall(r"শূন্য নয়\s+এমন", checked_target)) >= 2
            and "কোনো গণনীয় অমানক মডেলের অমানক খণ্ডগুলি" in checked_target
        )
    elif row["unit_id"] == "OLP-0197":
        assert source.count('$\\Struct{N}$ is the only computable model') == 1
        arithmetic_prose_ids = ["BN-SRC-133"]
        arithmetic_prose_fix = (
            "সমরূপতা পর্যন্ত $\\Th{PA}$-র একমাত্র গণনসাধ্য মডেল"
            in checked_target
        )
    overview_math_fix = False
    if row["unit_id"] == "OLP-0278":
        audited_overview = source
        old = r"\Prov[\Gamma](\num{n})"
        new = r"\OProv[\Gamma](\num{n})"
        assert audited_overview.count(old) == 2
        audited_overview = audited_overview.replace(old, new)
        overview_math_fix = (
            mathparts(audited_overview) == target_math
            and "BN-SRC-202" in documented
        )
    undecidability_math_fix = False
    if row["unit_id"] == "OLP-0279":
        audited_undecidability = source
        old = r"!A(\num{n})"
        new = r"!A_n(\num{n})"
        assert audited_undecidability.count(old) == 2
        audited_undecidability = audited_undecidability.replace(old, new)
        undecidability_math_fix = (
            mathparts(audited_undecidability) == target_math
            and "BN-SRC-203" in documented
        )
    arithmetization_syntax_math_fix = False
    arithmetization_syntax_expected = set()
    audited_arithmetization_syntax = source
    if row["unit_id"] == "OLP-0284":
        arithmetization_syntax_expected = {
            "BN-SRC-205",
            "BN-SRC-206",
            "BN-SRC-207",
        }
        repairs = [
            (
                "There are $n$, $j < x$, and $z < x$ such that for each $i < n$",
                "There are $n$, $j < x$, and $z < x$ such that $\\len{z}=n$, for each $i < n$",
            ),
            (
                r"\bforall{i<\len{x}}{\bforall{z<x}{}}\\" + "\n"
                r"(\bexists{j<z}{z=\Gn{\Obj v_j}} \lif \lnot\fn{FreeOcc}(x,z,i)).",
                r"\bforall{i<\len{x}}{\bforall{z<x}{(\bexists{j<z}{z=\Gn{\Obj v_j}} \\" + "\n"
                r"\lif \lnot\fn{FreeOcc}(x,z,i))}}.",
            ),
        ]
        for old, new in repairs:
            assert audited_arithmetization_syntax.count(old) == 1, old
            audited_arithmetization_syntax = audited_arithmetization_syntax.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0286":
        arithmetization_syntax_expected = {
            "BN-SRC-208",
            "BN-SRC-209",
            "BN-SRC-210",
            "BN-SRC-211",
            "BN-SRC-212",
        }
        repairs = [
            (r"\Gn{!A \Sequent !A)}", r"\Gn{!A \Sequent !A}"),
            (r"\fn{EndSeq}(p)", r"\fn{EndSequent}(p)"),
            (r"\fn{InitialSeq}", r"\fn{InitSeq}"),
            (r"$\fn{Deriv}(d)$", r"$\fn{Deriv}(p)$"),
            (
                r"\bforall{i<\len{\fn{SubtreeSeq}(p)}}{\fn{Correct}((\fn{SubtreeSeq}(p))_i}.",
                r"\bforall{i<\len{\fn{SubtreeSeq}(p)}}{\fn{Correct}((\fn{SubtreeSeq}(p))_i)}.",
            ),
            ("end-sequent of~$d$ is actually", "end-sequent of~$p$ is actually"),
            (
                r"$\len{(\fn{EndSequent}(x))_1} = 1 \land ((\fn{EndSequent}(x))_1)_0 =" + "\n" + r"x$.",
                r"$\len{(\fn{EndSequent}(x))_1} = 1 \land ((\fn{EndSequent}(x))_1)_0 = y$.",
            ),
        ]
        for old, new in repairs:
            assert audited_arithmetization_syntax.count(old) == 1, old
            audited_arithmetization_syntax = audited_arithmetization_syntax.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0287":
        arithmetization_syntax_expected = {"BN-SRC-213", "BN-SRC-214"}
        old = r"$\bexists{j<(d')_0}{d = (d')_j}$"
        new = r"$\bexists{j<(d')_0}{d = (d')_{j+1}}$"
        assert audited_arithmetization_syntax.count(old) == 1
        audited_arithmetization_syntax = audited_arithmetization_syntax.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0288":
        arithmetization_syntax_expected = {
            "BN-SRC-215",
            "BN-SRC-216",
            "BN-SRC-217",
        }
        repairs = [
            (
                r"\fn{QR}_1(d, i) \defiff \bexists{b < (d)_i}",
                r"\fn{QR}_1(d, i) \defiff \bexists{j<i}{\bexists{b < (d)_i}",
            ),
            (r"\bexists{c < (d)_j}{(}}}}", r"\bexists{c < (d)_j}{(}}}}}"),
            (
                r'and that of $a$ less than the G\"odel number of the',
                r'and that of $c$ less than the G\"odel number of the',
            ),
            (r"\concat \fn{Cond}(s, y, n) \concat", r"\concat \fn{hCond}(s, y, n) \concat"),
        ]
        for old, new in repairs:
            assert audited_arithmetization_syntax.count(old) == 1, old
            audited_arithmetization_syntax = audited_arithmetization_syntax.replace(old, new, 1)
    if arithmetization_syntax_expected:
        arithmetization_syntax_math_fix = (
            mathparts(audited_arithmetization_syntax) == target_math
            and set(documented) == arithmetization_syntax_expected
        )
    representability_q_math_fix = False
    representability_q_control_fix = False
    representability_q_expected = {
        "OLP-0291": {"BN-SRC-218", "BN-SRC-219"},
        "OLP-0293": {"BN-SRC-220", "BN-SRC-221"},
        "OLP-0294": {"BN-SRC-233"},
        "OLP-0295": {"BN-SRC-222", "BN-SRC-223"},
        "OLP-0296": {"BN-SRC-224"},
        "OLP-0297": {"BN-SRC-225"},
        "OLP-0300": {
            "BN-SRC-226",
            "BN-SRC-227",
            "BN-SRC-228",
            "BN-SRC-229",
            "BN-SRC-230",
            "BN-SRC-231",
            "BN-SRC-232",
        },
    }
    audited_representability_q = source
    if row["unit_id"] == "OLP-0291":
        repairs = [
            (
                r"!!a{formula}~$!A(x_0, \dots, x_k, y)$",
                r"!!a{formula}~$!A_f(x_0, \dots, x_k, y)$",
            ),
            (
                r"$A_f(\num{n_0}, \dots," + "\n" + r"\num{n_k}, (s)_1)$",
                r"$A_f(\num{n_0}, \dots," + "\n" + r"\num{n_k}, \num{(s)_1})$",
            ),
        ]
        for old, new in repairs:
            assert audited_representability_q.count(old) == 1, old
            audited_representability_q = audited_representability_q.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0293":
        repairs = [
            (r"$h(x,\vec" + "\n" + r"z)$", r"$h(\vec x,y)$"),
            (
                r"\bforall{i <" + "\n" + r"  y}{\beta(d,i+1) = g(\vec x, i,\beta(d,i)})}.",
                r"\bforall{i <" + "\n" + r"  y}{\beta(d,i+1) = g(\vec x, i,\beta(d,i))})}.",
            ),
        ]
        for old, new in repairs:
            assert audited_representability_q.count(old) == 1, old
            audited_representability_q = audited_representability_q.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0294":
        old = "  0 & otherwise"
        new = r"  0 & \text{otherwise}"
        assert audited_representability_q.count(old) == 1
        audited_representability_q = audited_representability_q.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0295":
        repairs = [
            (
                r"\lexists[y_0\dots][\lexists[y_{k-1}][",
                r"\lexists[y_0][\dots \lexists[y_{k-1}][",
            ),
            (r"\dots \land {}]]\\", r"\dots \land {}\\"),
            (
                r"!A_f(y_0,\dots,y_{k-1},z))" + "\n" + r"\end{multline*}",
                r"!A_f(y_0,\dots,y_{k-1},z))]]" + "\n" + r"\end{multline*}",
            ),
            (
                r"Using the proofs of \olref[inc][req][cmp]{prop:rep2} and",
                r"Using the proofs of \olref[inc][req][cmp]{prop:rep1} and",
            ),
        ]
        for old, new in repairs:
            assert audited_representability_q.count(old) == 1, old
            audited_representability_q = audited_representability_q.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0296":
        old = (
            r"  \Th{Q} & \Proves \eq[(a' + \num n')][(a' + \num n)'] \quad" + "\n"
            r"  \text{by axiom $!Q_5$} \ollabel{step5}\\" + "\n"
            r"  \Th{Q} & \Proves \eq[(a' + \num n')][(a + \num n')'] \quad" + "\n"
            r"  \text{inductive hypothesis} \ollabel{step6}\\" + "\n"
            r"  \Th{Q} & \Proves \eq[(a' + \num n)'][(a + \num n')'] \quad" + "\n"
            r"  \text{by \olref{step5} and \olref{step6}.} \notag"
        )
        new = (
            r"  \Th{Q} & \Proves \eq[(a' + \num n')][(a' + \num n)'] \quad" + "\n"
            r"  \text{by axiom $!Q_5$} \ollabel{step5}\\" + "\n"
            r"  \Th{Q} & \Proves \eq[(a' + \num n)'][(a + \num n')'] \quad" + "\n"
            r"  \text{inductive hypothesis and identity rules} \ollabel{step6}\\" + "\n"
            r"  \Th{Q} & \Proves \eq[(a' + \num n')][(a + \num n')'] \quad" + "\n"
            r"  \text{by \olref{step5} and \olref{step6}.} \notag"
        )
        assert audited_representability_q.count(old) == 1
        audited_representability_q = audited_representability_q.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0300":
        repairs = [
            (r"\olfileid{inc}{inp}{s1c}", r"\olfileid{inc}{req}{s1c}"),
            (
                r"$\Th{Q} \Proves \eq[t_2][\num n]$.",
                r"$\Th{Q} \Proves \eq[t_2][\num m]$.",
            ),
            (
                r"$\Th{Q} \Proves \eq[\num n + {\num k}'][\num m]$.",
                r"$\Th{Q} \Proves \eq[{\num k}' + \num n][\num m]$.",
            ),
            (r"via~$!Q_3$", r"via~$!Q_2$"),
            ("an empty disjunction", "an empty conjunction"),
            (r"$\lnot \bexists{x<t}!A(x)$", r"$\lnot \bexists{x<t}{!A(x)}$"),
            (r"$\lexists{x}!A(x)$", r"$\lexists[x][!A(x)]$"),
        ]
        expected_counts = [1, 1, 1, 2, 1, 1, 1]
        for (old, new), expected_count in zip(repairs, expected_counts):
            assert audited_representability_q.count(old) == expected_count, old
            audited_representability_q = audited_representability_q.replace(old, new)
    if row["unit_id"] in representability_q_expected:
        assert set(documented) == representability_q_expected[row["unit_id"]]
        representability_q_math_fix = (
            mathparts(audited_representability_q) == target_math
        )
        representability_q_control_fix = (
            controls(audited_representability_q) == controls(checked_target)
        )
    if 289 <= int(row["unit_id"].split("-")[1]) <= 300:
        assert set(documented) == representability_q_expected.get(row["unit_id"], set())
    theories_computability_math_fix = False
    theories_computability_token_fix = False
    theories_computability_expected = {
        "OLP-0303": {"BN-SRC-234", "BN-SRC-235"},
        "OLP-0305": {"BN-SRC-236", "BN-SRC-237"},
        "OLP-0306": {"BN-SRC-238"},
        "OLP-0307": {"BN-SRC-239"},
        "OLP-0308": {"BN-SRC-240"},
        "OLP-0309": {"BN-SRC-241"},
        "OLP-0311": {"BN-SRC-242", "BN-SRC-243"},
    }
    audited_theories_computability = source
    if row["unit_id"] == "OLP-0303":
        old = (
            "Conversely, if $\\Th{Q} \\Proves \\lexists[s][!A_T(\\num x, \\num x, s)]$,\n"
            "then, in fact, for some natural number $n$ the formula $!A_T(\\num x,\n"
            "\\num x, \\num n)$ must be true.  Now, if $T(x,x,n)$ were false,\n"
            "$\\Th{Q}$ would prove $\\lnot !A_T(\\num x, \\num x, \\num n)$, since\n"
            "$!A_T$ represents $T$.  But then $\\Th{Q}$ proves a false formula,\n"
            "which is a contradiction. So $T(x,x,n)$ must be true, which implies\n"
            "$!A_x(x) \\downarrow$."
        )
        new = (
            "Conversely, suppose $\\Th{Q} \\Proves \\lexists[s][!A_T(\\num x, \\num x, s)]$.\n"
            "The axioms of $\\Th{Q}$ are true in the standard model and first-order\n"
            "derivation is sound, so this existential sentence is true there. Thus,\n"
            "for some natural number $n$, $!A_T(\\num x, \\num x, \\num n)$ is true.\n"
            "If $T(x,x,n)$ were false, since $!A_T$ represents $T$, then\n"
            "$\\Th{Q} \\Proves \\lnot !A_T(\\num x, \\num x, \\num n)$. By soundness,\n"
            "that negation would also be true, a contradiction. So $T(x,x,n)$ is true,\n"
            "which implies $!A_x(x) \\downarrow$."
        )
        assert audited_theories_computability.count(old) == 1
        audited_theories_computability = audited_theories_computability.replace(old, new, 1)
        old_prefix = r"\lexists[s][T(\num x,"
        new_prefix = r"\lexists[s][!A_T(\num x,"
        assert audited_theories_computability.count(old_prefix) == 2
        audited_theories_computability = audited_theories_computability.replace(
            old_prefix, new_prefix
        )
    elif row["unit_id"] == "OLP-0305":
        meta_repairs = [(r"\lnot S(\num n) &", r"\lnot S(n) &"), (r"S(\num n) &", "S(n) &")]
        for old, new in meta_repairs:
            assert audited_theories_computability.count(old) == 1
            audited_theories_computability = audited_theories_computability.replace(old, new, 1)
        assert audited_theories_computability.count(r"\Sat{\Nat}{!A}") == 1
        audited_theories_computability = audited_theories_computability.replace(
            r"\Sat{\Nat}{!A}", r"\Sat{N}{!A}"
        )
    elif row["unit_id"] == "OLP-0307":
        old = (
            r"simultaneously search for !!a{derivation} of~$!A$ from~$\Th{T}$ and"
            + "\n"
            + r"!!a{derivation} of~$\lnot !A$."
        )
        new = (
            r"simultaneously search for !!a{derivation} of~$!A$ from~$A$ and"
            + "\n"
            + r"!!a{derivation} of~$\lnot !A$ from~$A$."
        )
        assert audited_theories_computability.count(old) == 1
        audited_theories_computability = audited_theories_computability.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0308":
        assert audited_theories_computability.count("!!{axiomatized}") == 1
        audited_theories_computability = audited_theories_computability.replace(
            "!!{axiomatized}", "!!{axiomatizable}", 1
        )
    elif row["unit_id"] == "OLP-0309":
        meta_repairs = [(r"\lnot S(\num n) &", r"\lnot S(n) &"), (r"S(\num n) &", "S(n) &")]
        for old, new in meta_repairs:
            assert audited_theories_computability.count(old) == 1
            audited_theories_computability = audited_theories_computability.replace(old, new, 1)
        old = r"R(\#(!D_S(\num u)),y)"
        new = r"R(\Gn{!D_S(u)},y)"
        assert audited_theories_computability.count(old) == 1
        audited_theories_computability = audited_theories_computability.replace(old, new, 1)
    unit_number = int(row["unit_id"].split("-")[1])
    if 301 <= unit_number <= 311:
        assert set(documented) == theories_computability_expected.get(row["unit_id"], set())
        audited_theories_math = (
            mathparts_with_setbuilder_text_math(
                audited_theories_computability, binder="!A"
            )
            if row["unit_id"] == "OLP-0310"
            else mathparts(audited_theories_computability)
        )
        theories_computability_math_fix = (
            audited_theories_math == target_math
        )
        theories_computability_token_fix = (
            semantic_tokens(audited_theories_computability)
            == semantic_tokens(checked_target)
        )
    incompleteness_provability_math_fix = False
    incompleteness_provability_token_fix = False
    incompleteness_provability_expected = {
        "OLP-0316": {"BN-SRC-250", "BN-SRC-251"},
        "OLP-0318": {"BN-SRC-244"},
        "OLP-0319": {"BN-SRC-245", "BN-SRC-246", "BN-SRC-247", "BN-SRC-248"},
        "OLP-0320": {"BN-SRC-249", "BN-SRC-252"},
    }
    audited_incompleteness_provability = source
    if row["unit_id"] == "OLP-0316":
        repairs = [
            (r"\ORProv_T(y)", r"\ORProv[\Th{T}](y)"),
            (r"from~$T$", r"from~$\Th{T}$"),
        ]
        for old, new in repairs:
            assert audited_incompleteness_provability.count(old) == 1, old
            audited_incompleteness_provability = (
                audited_incompleteness_provability.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0318":
        old = r"\lexists[x][\Prf[\Th{PA}](x,y)]"
        new = r"\lexists[x][\OPrf[\Th{PA}](x,y)]"
        assert audited_incompleteness_provability.count(old) == 1
        audited_incompleteness_provability = (
            audited_incompleteness_provability.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0319":
        repairs = [
            (r"\Prov[\Th{PA}]", r"\OProv[\Th{PA}]"),
            (r"\gn{G}", r"\gn{!G}"),
            ("!!{axiomatized}", "!!{axiomatizable}"),
            (r"\OCon[T]", r"\OCon[\Th{T}]"),
        ]
        for old, new in repairs:
            assert audited_incompleteness_provability.count(old) == 1, old
            audited_incompleteness_provability = (
                audited_incompleteness_provability.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0320":
        old = r"T \Proves"
        new = r"\Th{T} \Proves"
        assert audited_incompleteness_provability.count(old) == 6
        audited_incompleteness_provability = (
            audited_incompleteness_provability.replace(old, new)
        )
        old = "It is not !!{derivable}, because if"
        new = "If $\\Th{T}$ is consistent, it is not !!{derivable}, because if"
        assert audited_incompleteness_provability.count(old) == 1
        audited_incompleteness_provability = (
            audited_incompleteness_provability.replace(old, new, 1)
        )
    if 312 <= unit_number <= 321:
        assert set(documented) == incompleteness_provability_expected.get(
            row["unit_id"], set()
        )
        audited_incompleteness_math = (
            mathparts_with_tarski_quotation(audited_incompleteness_provability)
            if row["unit_id"] == "OLP-0321"
            else mathparts(audited_incompleteness_provability)
        )
        incompleteness_provability_math_fix = (
            audited_incompleteness_math == target_math
        )
        incompleteness_provability_token_fix = (
            semantic_tokens(audited_incompleteness_provability)
            == semantic_tokens(checked_target)
        )
    second_order_syntax_semantics_math_fix = False
    second_order_syntax_semantics_token_fix = False
    second_order_syntax_semantics_expected = {
        "OLP-0324": {"BN-SRC-253"},
        "OLP-0329": {"BN-SRC-254"},
    }
    audited_second_order_syntax_semantics = source
    if row["unit_id"] == "OLP-0324":
        repairs = [
            (r"\Obj{V^1_0}(\Obj v_0)", r"\Obj{V^1_0}(\Obj{v_0})"),
            (r"\Obj{V^1_0}(v_0)", r"\Obj{V^1_0}(\Obj{v_0})"),
        ]
        for old, new in repairs:
            assert audited_second_order_syntax_semantics.count(old) == 1, old
            audited_second_order_syntax_semantics = (
                audited_second_order_syntax_semantics.replace(old, new, 1)
            )
    if 322 <= unit_number <= 329:
        assert set(documented) == second_order_syntax_semantics_expected.get(
            row["unit_id"], set()
        )
        second_order_syntax_semantics_math_fix = (
            mathparts(audited_second_order_syntax_semantics) == target_math
        )
        second_order_syntax_semantics_token_fix = (
            semantic_tokens(audited_second_order_syntax_semantics)
            == semantic_tokens(checked_target)
        )
    second_order_metatheory_math_fix = False
    second_order_metatheory_control_fix = False
    second_order_metatheory_token_fix = False
    second_order_metatheory_expected = {
        "OLP-0332": {"BN-SRC-255"},
        "OLP-0333": {"BN-SRC-256"},
        "OLP-0334": {"BN-SRC-257", "BN-SRC-258"},
    }
    audited_second_order_metatheory = source
    if row["unit_id"] == "OLP-0332":
        old = r"\lforall[w][u(x')=u" + "\n" + r" (x)']"
        new = r"\lforall[w][u(w')=u" + "\n" + r" (w)']"
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
    elif row["unit_id"] == "OLP-0333":
        old = r"$\Sat{M}{!P \lif !A$}"
        new = r"$\Sat{M}{!P \lif !A}$"
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
    elif row["unit_id"] == "OLP-0334":
        old = r"\ollabel{thm:sol-undecidable}"
        new = r"\ollabel{thm:sol-not-compact}"
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
        old = "there is some $k$ so that "
        new = (
            "if $\\Gamma_0$ contains no $!A^{\\ge n}$, take $k=1$; "
            "otherwise there is some $k$ so that "
        )
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
        old = r"$!A^{\ge k} \in \Gamma$"
        new = r"$!A^{\ge k} \in \Gamma_0$"
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
        old = r"\in \Gamma$ for $n>k$"
        new = r"\in \Gamma_0$ for $n>k$"
        assert audited_second_order_metatheory.count(old) == 1
        audited_second_order_metatheory = audited_second_order_metatheory.replace(
            old, new, 1
        )
    if 330 <= unit_number <= 335:
        assert set(documented) == second_order_metatheory_expected.get(
            row["unit_id"], set()
        )
        second_order_metatheory_math_fix = (
            mathparts(audited_second_order_metatheory) == target_math
        )
        second_order_metatheory_control_fix = (
            controls(audited_second_order_metatheory) == controls(checked_target)
        )
        second_order_metatheory_token_fix = (
            semantic_tokens(audited_second_order_metatheory)
            == semantic_tokens(checked_target)
        )
    second_order_set_theory_math_fix = False
    second_order_set_theory_expected = {
        "OLP-0338": {"BN-SRC-259", "BN-SRC-260"},
        "OLP-0339": {"BN-SRC-261", "BN-SRC-262", "BN-SRC-263"},
        "OLP-0340": {"BN-SRC-264", "BN-SRC-265", "BN-SRC-266"},
    }
    audited_second_order_set_theory = source
    if row["unit_id"] == "OLP-0338":
        global_injectivity = re.compile(
            r"\\lforall\[x\]\[\\lforall\[y\]\[\("
            r"\\eq\[u\(x\)\]\[u\(y\)\]\s*\\lif\s*\\eq\[x\]\[y\]\)\]\]"
        )
        restricted_injectivity = (
            r"\lforall[x][\lforall[y][((X(x) \land X(y) \land "
            r"\eq[u(x)][u(y)]) \lif \eq[x][y])]]"
        )
        audited_second_order_set_theory, count = global_injectivity.subn(
            lambda _: restricted_injectivity,
            audited_second_order_set_theory,
        )
        assert count == 2
    elif row["unit_id"] == "OLP-0339":
        inf_pattern = re.compile(
            r"\\begin\{multline\*\}\n\\lexists\[u\].*?\\end\{multline\*\}",
            re.S,
        )
        corrected_inf = r"""\begin{multline*}
\lexists[u][(\lforall[x][(X(x) \lif X(u(x)))] \land {}\\
  \lforall[x][\lforall[y][((X(x) \land X(y) \land
      \eq[u(x)][u(y)]) \lif \eq[x][y])]] \land {}\\
  \lexists[y][(X(y) \land \lforall[x][(X(x)
      \lif \eq/[y][u(x)])]])]
\end{multline*}"""
        audited_second_order_set_theory, count = inf_pattern.subn(
            lambda _: corrected_inf,
            audited_second_order_set_theory,
            count=1,
        )
        assert count == 1
        count_pattern = re.compile(
            r"\\begin\{multline\*\}\n\\lexists\[z\].*?\\end\{multline\*\}",
            re.S,
        )
        corrected_count = r"""\begin{multline*}
\lnot\lexists[x][X(x)] \lor {}\\
\lexists[z][\lexists[u][(X(z) \land
    \lforall[x][(X(x) \lif X(u(x)))] \land {}\\
    \lforall[Y][(((Y \subseteq X \land Y(z)) \land
      \lforall[x][(Y(x) \lif Y(u(x)))]) \lif X = Y)])]]
\end{multline*}"""
        audited_second_order_set_theory, count = count_pattern.subn(
            lambda _: corrected_count,
            audited_second_order_set_theory,
            count=1,
        )
        assert count == 1
        old = r"\fn{Aleph_1}(X) \ident \lforall[Y]"
        new = r"\fn{Aleph_1}(X) \ident \fn{Inf}(X) \land \lforall[Y]"
        assert audited_second_order_set_theory.count(old) == 1
        audited_second_order_set_theory = audited_second_order_set_theory.replace(
            old, new, 1
        )
    elif row["unit_id"] == "OLP-0340":
        marker = r"$\cardeq{\Domain{M}}{\Real}$ iff" + "\n"
        marker_index = audited_second_order_set_theory.index(marker)
        global_injectivity = re.compile(
            r"\\lforall\[x\]\[\\lforall\[y\]\[\("
            r"\\eq\[u\(x\)\]\[u\(y\)\]\s*\\lif\s*\\eq\[x\]\[y\]\)\]\]"
        )
        restricted_injectivity = (
            r"\lforall[x][\lforall[y][((Y(x) \land Y(y) \land "
            r"\eq[u(x)][u(y)]) \lif \eq[x][y])]]"
        )
        cantor_prefix, count = global_injectivity.subn(
            lambda _: restricted_injectivity,
            audited_second_order_set_theory[:marker_index],
            count=1,
        )
        assert count == 1
        audited_second_order_set_theory = (
            cantor_prefix + audited_second_order_set_theory[marker_index:]
        )
        old = "subsets of $s(Z)$ via"
        new = "subsets of $s(X)$ via"
        assert audited_second_order_set_theory.count(old) == 1
        audited_second_order_set_theory = audited_second_order_set_theory.replace(
            old, new, 1
        )
        marker_start = audited_second_order_set_theory.index(marker) + len(marker)
        block_start = audited_second_order_set_theory.index(
            r"\begin{multline*}", marker_start
        )
        block_end = audited_second_order_set_theory.index(
            r"\end{multline*}", block_start
        ) + len(r"\end{multline*}")
        corrected_domain_continuum = r"""\begin{multline*}
  \Sat{M}{\lexists[Y][(\fn{Cont}(Y) \land {}\\
    \lexists[u][(\lforall[x][Y(u(x))] \land
      \lforall[x][\lforall[y][(\eq[u(x)][u(y)] \lif \eq[x][y])]] \land {}\\
      \lforall[y][(Y(y) \lif \lexists[x][\eq[y][u(x)]])])])]}.
\end{multline*}"""
        audited_second_order_set_theory = (
            audited_second_order_set_theory[:block_start]
            + corrected_domain_continuum
            + audited_second_order_set_theory[block_end:]
        )
    if 336 <= unit_number <= 340:
        assert set(documented) == second_order_set_theory_expected.get(
            row["unit_id"], set()
        )
        second_order_set_theory_math_fix = (
            mathparts(audited_second_order_set_theory) == target_math
        )
    lambda_introduction_completion_math_fix = False
    lambda_introduction_completion_expected = {
        "OLP-0347": {"BN-SRC-267"},
        "OLP-0348": {"BN-SRC-268", "BN-SRC-269"},
        "OLP-0349": {"BN-SRC-270"},
        "OLP-0353": {"BN-SRC-271", "BN-SRC-272", "BN-SRC-273"},
        "OLP-0355": {"BN-SRC-274"},
    }
    audited_lambda_introduction_completion = source
    if row["unit_id"] == "OLP-0347":
        old = r"\Subst{\Subst{P}{M_1}{x_1}\ldots}{M_n}{x_n}"
        new = r"\Subst{\Subst{N}{M_1}{x_1}\ldots}{M_n}{x_n}"
        assert audited_lambda_introduction_completion.count(old) == 1
        audited_lambda_introduction_completion = (
            audited_lambda_introduction_completion.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0348":
        repairs = [
            ("an $n$-ary partial function", "a $k$-ary partial function"),
            (r"$F, \num{n_0}\,", r"$F\, \num{n_0}\,"),
        ]
        for old, new in repairs:
            assert audited_lambda_introduction_completion.count(old) == 1, old
            audited_lambda_introduction_completion = (
                audited_lambda_introduction_completion.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0349":
        old = r"$X \num m_0 \ldots \num" + "\n" + r"m_{n-1}$"
        new = r"$X \num{m_0} \ldots \num{m_{n-1}}$"
        assert audited_lambda_introduction_completion.count(old) == 1
        audited_lambda_introduction_completion = (
            audited_lambda_introduction_completion.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0353":
        repairs = [
            (
                "that we already have terms $G$ and $H$ that !!{lambda define} functions",
                "that we already have terms $G'$ and $H'$ that !!{lambda define} functions",
            ),
            (
                "we want a term $H$ that !!{lambda define}s the",
                "we want a term $F$ that !!{lambda define}s the",
            ),
            (
                r"f(x+1, \vec z) & = h(z, f(x,\vec z), \vec z).",
                r"f(x+1, \vec z) & = h(x, f(x,\vec z), \vec z).",
            ),
            (
                r"F(\num{0}, \vec z) & \equiv G(\vec z)",
                r"F(\num{0}, \vec z) & \equiv G'(\vec z)",
            ),
            (
                r"F(\overline{n+1}, \vec z) & \equiv H(\num{n}, F(\num{n}, \vec z), \vec z)",
                r"F(\overline{n+1}, \vec z) & \equiv H'(\num{n}, F(\num{n}, \vec z), \vec z)",
            ),
            (
                r"H(u,v) & = \lambd[\vec z][H'(u,v(u,\vec z),\vec z)].",
                r"H(u,v) & = \lambd[\vec z][H'(u,v(\vec z),\vec z)].",
            ),
        ]
        for old, new in repairs:
            assert audited_lambda_introduction_completion.count(old) == 1, old
            audited_lambda_introduction_completion = (
                audited_lambda_introduction_completion.replace(old, new, 1)
            )
    if 347 <= unit_number <= 355:
        assert set(documented) == lambda_introduction_completion_expected.get(
            row["unit_id"], set()
        )
        lambda_introduction_completion_math_fix = (
            mathparts(audited_lambda_introduction_completion) == target_math
        )
    lambda_syntax_foundations_math_fix = False
    lambda_syntax_foundations_expected = {
        "OLP-0360": {"BN-SRC-275"},
        "OLP-0361": {"BN-SRC-276", "BN-SRC-277", "BN-SRC-282", "BN-SRC-283"},
        "OLP-0362": {"BN-SRC-278", "BN-SRC-279", "BN-SRC-280", "BN-SRC-281", "BN-SRC-284"},
        "OLP-0364": {"BN-SRC-285", "BN-SRC-286", "BN-SRC-287", "BN-SRC-288"},
        "OLP-0365": {"BN-SRC-289"},
        "OLP-0366": {"BN-SRC-290", "BN-SRC-291"},
    }
    lambda_syntax_control_fix = False
    audited_lambda_syntax_foundations = source
    if row["unit_id"] == "OLP-0360":
        old = (
            "then the corresponding\noccurrence of~$N$ is the "
            r"\emph{scope} of the~$\lambd[x]$."
        )
        new = (
            "then the corresponding\noccurrence of~$M$ is the "
            r"\emph{scope} of the~$\lambd[x]$."
        )
        assert audited_lambda_syntax_foundations.count(old) == 1
        audited_lambda_syntax_foundations = (
            audited_lambda_syntax_foundations.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0361":
        repairs = [
            (
                "    \\item $\\Subst{(\\lambd[y][P])}{N}{x} = \\lambd[y][\\Subst{P}{N}{x}]$,\n"
                "      if $x \\neq y$ and $y \\notin \\FV{N}$, otherwise undefined.",
                "    \\item $\\Subst{(\\lambd[x][P])}{N}{x} = \\lambd[x][P]$; and\n"
                "      if $x \\neq y$ and $y \\notin \\FV{N}$,\n"
                "      $\\Subst{(\\lambd[y][P])}{N}{x} = \\lambd[y][\\Subst{P}{N}{x}]$.\n"
                "      If $x \\neq y$ but $y \\in \\FV{N}$, it is undefined.",
            ),
            (r"$x \notin \FV{Q}$", r"$x \notin \FV{P}$"),
            (r"$x \in \FV{M})$", r"$x \in \FV{M}$"),
            (r"$\Subst{(PQ)}{N}{y}$", r"$\Subst{(PQ)}{N}{x}$"),
            (
                "since $y \\in\n    \\FV{\\lambd[x][P]}$, we have $y \\in \\FV{P}$ too",
                "since $x \\in\n    \\FV{\\lambd[y][P]}$, we have $x \\in \\FV{P}$ too",
            ),
            (
                "& = ((\\FV{P} \\setminus \\{y\\}) \\cup (\\FV{N} \\setminus \\{x\\})\n"
                "       && \\text{by inductive hypothesis}",
                "& = ((\\FV{P} \\setminus \\{x\\}) \\cup \\FV{N}) \\setminus \\{y\\}\n"
                "       && \\text{by inductive hypothesis}",
            ),
            (r"&& x \notin \FV{N}", r"&& y \notin \FV{N}"),
            (
                "$x \\notin \\FV{\\Subst{M}{N}{x}}$, if the right-hand side is\n"
                "  defined and $x \\notin \\FV{N}$.",
                "If $\\Subst{M}{N}{x}$ is defined and $x \\notin \\FV{N}$, then\n"
                "  $x \\notin \\FV{\\Subst{M}{N}{x}}$.",
            ),
        ]
        for old, new in repairs:
            assert audited_lambda_syntax_foundations.count(old) == 1, old
            audited_lambda_syntax_foundations = (
                audited_lambda_syntax_foundations.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0362":
        repairs = [
            (
                "contains an occurrence of $\\lambd[x][N]$, $y \\notin\n  \\FV{N}$",
                "contains an occurrence of $\\lambd[x][N]$, $x \\neq y$, $y \\notin\n  \\FV{N}$",
            ),
            (r"$x \in FV(N)$", r"$x \in \FV{N}$"),
            (r"$x \notin FV(N)$", r"$x \notin \FV{N}$"),
            (r"& = FV{\Subst{N}{y}{x}}", r"& = \FV{\Subst{N}{y}{x}}"),
            (r"$z \notin FV(N')$", r"$z \notin \FV{N'}$"),
            (r"$z \notin FV(R)$", r"$z \notin \FV{R}$"),
            (
                "      &= \\lambd[z][\\Subst{\\Subst{N''}{z}{x}}{R}{y}] && \\text{by\n"
                "        \\olref{lem:sub:R}}",
                "      &\\aeq \\lambd[z][\\Subst{\\Subst{N''}{z}{x}}{R}{y}] && \\text{by\n"
                "        \\olref{lem:sub:R}}",
            ),
            (
                "      &=\\lambd[z][\\Subst{\\Subst{N'}{z}{x}}{R}{y}]\n"
                "      && \\text{by inductive",
                "      &\\aeq\\lambd[z][\\Subst{\\Subst{N'}{z}{x}}{R}{y}]\n"
                "      && \\text{by inductive",
            ),
            (
                "if there is another pair $M'' \\aeq M$ and $R''$\n"
                "  with $\\Subst{M'}{R'}{y}$ defined",
                "if there is another pair $M'' \\aeq M$ and $R'' \\aeq R$\n"
                "  with $\\Subst{M''}{R''}{y}$ defined",
            ),
        ]
        for old, new in repairs:
            assert audited_lambda_syntax_foundations.count(old) == 1, old
            audited_lambda_syntax_foundations = (
                audited_lambda_syntax_foundations.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0364":
        repairs = [
            (
                r"and $\rep{M}[0], \rep{M}[1], etc. $ if",
                r"and $\rep{M}[0]$, $\rep{M}[1]$, etc. if",
            ),
            (r"$FV(M)$", r"$\FV{M}$"),
            (r"$FV(\rep{M})$", r"$\FV{\rep{M}}$"),
            (
                "$FV(\\rep{M}[0]) =\nFV(\\rep{M}[1])$",
                "$\\FV{\\rep{M}[0]} =\n\\FV{\\rep{M}[1]}$",
            ),
            (r"$x \notin FV(R)$", r"$x \notin \FV{R}$"),
            (
                r"  \Subst{\lambd[x][x]}{y}{x} & =\ollabel{eq:1}\\",
                r"  \Subst{\lambd[x][x]}{y}{x} & \ollabel{eq:1}\\",
            ),
        ]
        for old, new in repairs:
            assert audited_lambda_syntax_foundations.count(old) == 1, old
            audited_lambda_syntax_foundations = (
                audited_lambda_syntax_foundations.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0365":
        old = r"\olfileid{lam}{int}{bet}"
        new = r"\olfileid{lam}{syn}{bet}"
        assert audited_lambda_syntax_foundations.count(old) == 1
        audited_lambda_syntax_foundations = (
            audited_lambda_syntax_foundations.replace(old, new, 1)
        )
        lambda_syntax_control_fix = (
            controls(audited_lambda_syntax_foundations) == controls(checked_target)
        )
    elif row["unit_id"] == "OLP-0366":
        repairs = [
            (r"x \notin FV(M)", r"x \notin \FV{M}"),
            (
                r"  \lambd[x][f x] \equal f",
                r"  \lambd[x][M x] \equal M \text{ provided } x \notin \FV{M}",
            ),
            (r"$x \notin FV(MN)$", r"$x \notin \FV{MN}$"),
            (
                "$x \\notin\n  FV(M)$",
                "$x \\notin\n  \\FV{M}$",
            ),
            (r"$ext$ rule", r"\ext{} rule"),
            (r"$\equal[ext]$", r"$\equal[\ext]$"),
        ]
        for old, new in repairs:
            assert audited_lambda_syntax_foundations.count(old) == 1, old
            audited_lambda_syntax_foundations = (
                audited_lambda_syntax_foundations.replace(old, new, 1)
            )
    if 356 <= unit_number <= 366:
        assert set(documented) == lambda_syntax_foundations_expected.get(
            row["unit_id"], set()
        )
        lambda_syntax_foundations_math_fix = (
            mathparts(audited_lambda_syntax_foundations) == target_math
        )
    lambda_church_rosser_math_fix = False
    lambda_church_rosser_expected = {
        "OLP-0368": {"BN-SRC-292"},
        "OLP-0369": {"BN-SRC-293", "BN-SRC-294"},
        "OLP-0370": {"BN-SRC-295", "BN-SRC-296"},
        "OLP-0371": {"BN-SRC-297", "BN-SRC-298", "BN-SRC-299", "BN-SRC-303", "BN-SRC-304"},
        "OLP-0372": {"BN-SRC-300", "BN-SRC-301", "BN-SRC-302"},
    }
    audited_lambda_church_rosser = source
    if row["unit_id"] == "OLP-0368":
        repairs = [
            (
                "  Suppose \n  \\begin{align*}",
                "  Suppose $M \\xred P$ and $M \\xred Q$; that is,\n  \\begin{align*}",
            ),
            (r"P_m \text{ and}", r"P_m \, (=P) \text{ and}"),
            (r"Q_n.", r"Q_n \, (=Q)."),
        ]
        for old, new in repairs:
            assert audited_lambda_church_rosser.count(old) == 1, old
            audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0369":
        repairs = [
            (r"$N \xrightarrow{\beta} N'$", r"$N \bredpar N'$"),
            (r"\lambd[x][\Subst{N'}{R}{y}]", r"\lambd[x][\Subst{N'}{R'}{y}]"),
        ]
        for old, new in repairs:
            assert audited_lambda_church_rosser.count(old) == 1, old
            audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0370":
        old = "$N$, $M'$, $Q$, $Q'$, where"
        new = "$N$, $N'$, $Q$, $Q'$, where"
        assert audited_lambda_church_rosser.count(old) == 1, old
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0371":
        old = r"$N \xrightarrow{\beta} N'$"
        new = r"$N \beredpar N'$"
        assert audited_lambda_church_rosser.count(old) == 1, old
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
        old = "$M'$ is $N'$ for some $x$ and~$N'$ where"
        new = "$M'$ is $N'$ for some $x$, $N$, and~$N'$ where"
        assert audited_lambda_church_rosser.count(old) == 1, old
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
        assert audited_lambda_church_rosser.count("FV(N)") == 4
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(
            "FV(N)", r"\FV{N}"
        )
    elif row["unit_id"] == "OLP-0372":
        old = "$M \\bredone\n  M'$ by $\\eta$-conversion"
        new = "$M \\eredone M'$ by $\\eta$-conversion"
        assert audited_lambda_church_rosser.count(old) == 1, old
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(old, new, 1)
        assert audited_lambda_church_rosser.count("FV(N)") == 1
        audited_lambda_church_rosser = audited_lambda_church_rosser.replace(
            "FV(N)", r"\FV{N}"
        )
    if 367 <= unit_number <= 372:
        assert set(documented) == lambda_church_rosser_expected.get(row["unit_id"], set())
        lambda_church_rosser_math_fix = mathparts(audited_lambda_church_rosser) == target_math
    lambda_definability_opening_math_fix = False
    lambda_definability_opening_expected = {
        "OLP-0374": {"BN-SRC-305"},
        "OLP-0375": {"BN-SRC-306"},
    }
    audited_lambda_definability_opening = source
    if row["unit_id"] == "OLP-0374":
        old = r"$c(n) = k$"
        new = r"$c_k(n) = k$"
        assert audited_lambda_definability_opening.count(old) == 1, old
        audited_lambda_definability_opening = (
            audited_lambda_definability_opening.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0375":
        old = r"\fn{Mult}' \ident \lambd[ab][a (\fn{Add}\, a) \num{0}]."
        new = r"\fn{Mult}' \ident \lambd[ab][a (\fn{Add}\, b) \num{0}]."
        assert audited_lambda_definability_opening.count(old) == 1, old
        audited_lambda_definability_opening = (
            audited_lambda_definability_opening.replace(old, new, 1)
        )
    if 373 <= unit_number <= 375:
        assert set(documented) == lambda_definability_opening_expected.get(
            row["unit_id"], set()
        )
        lambda_definability_opening_math_fix = (
            mathparts(audited_lambda_definability_opening) == target_math
        )
    lambda_definability_pairs_truth_pr_math_fix = False
    lambda_definability_pairs_truth_pr_expected = {
        "OLP-0376": {"BN-SRC-307"},
        "OLP-0377": {"BN-SRC-308"},
        "OLP-0378": {"BN-SRC-309", "BN-SRC-310"},
    }
    audited_lambda_definability_pairs_truth_pr = source
    if row["unit_id"] == "OLP-0376":
        old = r"\tuple{0,0}"
        new = r"\tuple{\num{0}, \num{0}}"
        assert audited_lambda_definability_pairs_truth_pr.count(old) == 2, old
        audited_lambda_definability_pairs_truth_pr = (
            audited_lambda_definability_pairs_truth_pr.replace(old, new)
        )
    elif row["unit_id"] == "OLP-0377":
        old = r"R \subseteq \Nat^n"
        new = r"R \subseteq \Nat^k"
        assert audited_lambda_definability_pairs_truth_pr.count(old) == 1, old
        audited_lambda_definability_pairs_truth_pr = (
            audited_lambda_definability_pairs_truth_pr.replace(old, new, 1)
        )
    elif row["unit_id"] == "OLP-0378":
        repairs = [
            (r"$F$, $G_0$, \dots, $G_k$", r"$F$, $G_0$, \dots, $G_{k-1}$"),
            (r"Then $H$ is !!{lambda definable}.", r"Then $h$ is !!{lambda definable}."),
            (
                r"h(x_1, \dots, x_n, y+1) & = h(x_1, \dots, x_n, y, h(x_1, \dots, x_n, y)).",
                r"h(x_1, \dots, x_n, y+1) & = g(x_1, \dots, x_n, y, h(x_1, \dots, x_n, y)).",
            ),
            (r"application of the function $h$ $y$ times", r"application of the function $g$ $y$ times"),
        ]
        for old, new in repairs:
            assert audited_lambda_definability_pairs_truth_pr.count(old) == 1, old
            audited_lambda_definability_pairs_truth_pr = (
                audited_lambda_definability_pairs_truth_pr.replace(old, new, 1)
            )
    if 376 <= unit_number <= 378:
        assert set(documented) == lambda_definability_pairs_truth_pr_expected.get(
            row["unit_id"], set()
        )
        lambda_definability_pairs_truth_pr_math_fix = (
            mathparts(audited_lambda_definability_pairs_truth_pr) == target_math
        )
    lambda_definability_completion_math_fix = False
    lambda_definability_completion_expected = {
        "OLP-0379": {"BN-SRC-311", "BN-SRC-312"},
        "OLP-0380": {"BN-SRC-313", "BN-SRC-314", "BN-SRC-317"},
    }
    audited_lambda_definability_completion = source
    if row["unit_id"] == "OLP-0379":
        repairs = [
            (
                r"\fn{Mult} \ident \lambd[ab][a (\fn{Add}\, a) 0]",
                r"\fn{Mult} \ident \lambd[ab][a (\fn{Add}\, b) \num{0}]",
            ),
            (
                "$Yg\n\\equal[\\beta] g(Yg)$",
                "$Y_C g\n\\equal[\\beta] g(Y_C g)$",
            ),
            (r"$Yg \bred g(Yg)$", r"$Y_C g \bred g(Y_C g)$"),
        ]
        for old, new in repairs:
            assert audited_lambda_definability_completion.count(old) == 1, old
            audited_lambda_definability_completion = (
                audited_lambda_definability_completion.replace(old, new, 1)
            )
    elif row["unit_id"] == "OLP-0380":
        repairs = [
            (r"To !!{lambda define}~$h$", r"To !!{lambda define}~$g$"),
            (r"    H & \ident", r"    G & \ident"),
            (
                r"(g\, \vec{x} (\fn{Succ}\, y)]]",
                r"(g\, \vec{x} (\fn{Succ}\, y))]]",
            ),
            (
                r"(g\, \vec{x} (\fn{Succ}\, y))]]",
                r"(g\, f\, \vec{x} (\fn{Succ}\, y))]]",
            ),
            (
                r"\num{h(n_1, \dots, n_k)}",
                r"\num{g(n_1, \dots, n_k)}",
            ),
        ]
        for old, new in repairs:
            assert audited_lambda_definability_completion.count(old) == 1, old
            audited_lambda_definability_completion = (
                audited_lambda_definability_completion.replace(old, new, 1)
            )
    if 379 <= unit_number <= 382:
        assert set(documented) == lambda_definability_completion_expected.get(
            row["unit_id"], set()
        )
        lambda_definability_completion_math_fix = (
            mathparts(audited_lambda_definability_completion) == target_math
        )
    many_valued_syntax_semantics_math_fix = False
    audited_many_valued_syntax_semantics = source
    if row["unit_id"] == "OLP-0391":
        repairs = [
            (
                "$\\pAssign v\n  \\Entails[\\Log L] \\Gamma$",
                "$\\pSat{v}{\\Gamma}[\\Log L]$",
            ),
            (
                r"$\pAssign v \Entails/[\Log L] !B$",
                r"$\pSat/{v}{!B}[\Log L]$",
            ),
        ]
        for old, new in repairs:
            assert audited_many_valued_syntax_semantics.count(old) == 1, old
            audited_many_valued_syntax_semantics = (
                audited_many_valued_syntax_semantics.replace(old, new, 1)
            )
    if 383 <= unit_number <= 391:
        expected_many_valued = {
            "OLP-0391": {"BN-SRC-315", "BN-SRC-316"},
        }
        assert set(documented) == expected_many_valued.get(row["unit_id"], set())
        many_valued_syntax_semantics_math_fix = (
            mathparts(audited_many_valued_syntax_semantics) == target_math
        )
    three_valued_logics_math_fix = False
    audited_three_valued_logics = source
    if row["unit_id"] == "OLP-0394":
        repairs = [
            (
                r"\tf{\land}(\False, \Undef) =" "\n"
                r"\tf{\land}(\False, \Undef) = \False.",
                r"\tf{\land}(\False, \Undef) =" "\n"
                r"\tf{\land}(\Undef, \False) = \False.",
            ),
            (r"$(\lnot p \land p) \lif q)$", r"$(\lnot p \land p) \lif q$"),
            (
                r"$\pValue v(\lnot \Diamond(p \land \lnot p)) =" "\n"
                r"\Undef$",
                r"$\pValue v(\lnot \Diamond(p \land \lnot p)) =" "\n"
                r"\False$",
            ),
        ]
        for old, new in repairs:
            assert audited_three_valued_logics.count(old) == 1, old
            audited_three_valued_logics = audited_three_valued_logics.replace(
                old, new, 1
            )
    elif row["unit_id"] == "OLP-0397":
        old_basis = r"""\item Induction basis: $!A \ident p$. By
    \olref[syn][val]{defn:pValue}, $\pValue v(!A)[\LogKs]
    = \pAssign v(p) = \pValue {v'}(!A)[\LogCL]$, which implies both (a)
    and~(b)."""
        new_basis = r"""\item Induction basis: $!A \ident p$. By
    \olref[syn][val]{defn:pValue} and~$v'$, if
    $\pValue v(!A)[\LogKs] = \False$, then $\pAssign v(p)=\False$ and
    $\pValue {v'}(!A)[\LogCL]=\False$. If
    $\pValue v(!A)[\LogKs] = \True$, then $\pAssign v(p)=\True$ and
    $\pValue {v'}(!A)[\LogCL]=\True$."""
        assert audited_three_valued_logics.count(old_basis) == 1
        audited_three_valued_logics = audited_three_valued_logics.replace(
            old_basis, new_basis, 1
        )
        repairs = [
            (
                r"$\pValue v(!B)[\LogKs]  =" "\n"
                r"      \False$ or $\pValue v(!B)[\LogKs]  = \False$",
                r"$\pValue v(!B)[\LogKs]  =" "\n"
                r"      \False$ or $\pValue v(!C)[\LogKs]  = \False$",
            ),
            (
                r"$\pValue v(!B)[\LogKs]  =" "\n"
                r"      \True$ and $\pValue v(!B)[\LogKs]  = \True$",
                r"$\pValue v(!B)[\LogKs]  =" "\n"
                r"      \True$ and $\pValue v(!C)[\LogKs]  = \True$",
            ),
            (
                r"Truth functions are the same as \L ukasiewicz logic~$\LogLuk[3]$.",
                r"The falsum truth function is $\tf{\lfalse}=\False$; truth functions for the remaining connectives are the same as \L ukasiewicz logic~$\LogLuk[3]$.",
            ),
        ]
        for old, new in repairs:
            assert audited_three_valued_logics.count(old) == 1, old
            audited_three_valued_logics = audited_three_valued_logics.replace(
                old, new, 1
            )
    if 392 <= unit_number <= 397:
        expected_three_valued = {
            "OLP-0394": {"BN-SRC-318", "BN-SRC-319", "BN-SRC-323"},
            "OLP-0397": {"BN-SRC-320", "BN-SRC-321", "BN-SRC-322"},
        }
        assert set(documented) == expected_three_valued.get(row["unit_id"], set())
        three_valued_logics_math_fix = (
            mathparts(audited_three_valued_logics) == target_math
        )
    infinite_valued_logics_math_fix = False
    audited_infinite_valued_logics = source
    if row["unit_id"] == "OLP-0399":
        repairs = [
            (
                r"n,m \in \Nat \text{ and } n\le m",
                r"n,m \in \Nat \text{ and } 0<m \text{ and } n\le m",
            ),
            (
                r"n \in \Nat \text{ and } n\le m}",
                r"n \in \Nat \text{ and } n\le m-1}",
            ),
        ]
        for old, new in repairs:
            assert audited_infinite_valued_logics.count(old) == 1, old
            audited_infinite_valued_logics = audited_infinite_valued_logics.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0400":
        old = "In fact, the converse holds as well."
        new = "For finite $\\Gamma$, the converse holds as well."
        assert audited_infinite_valued_logics.count(old) == 1
        audited_infinite_valued_logics = audited_infinite_valued_logics.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0401":
        repairs = [
            (r"      $1$ & \text{if } x =0\\", r"      1 & \text{if } x =0\\"),
            (r"      $0$ & \text{otherwise}", r"      0 & \text{otherwise}"),
            ("In fact, the converse holds as well.", "For finite $\\Gamma$, the converse holds as well."),
        ]
        for old, new in repairs:
            assert audited_infinite_valued_logics.count(old) == 1, old
            audited_infinite_valued_logics = audited_infinite_valued_logics.replace(old, new, 1)
    if 398 <= unit_number <= 401:
        expected_infinite_valued = {
            "OLP-0399": {"BN-SRC-324", "BN-SRC-325"},
            "OLP-0400": {"BN-SRC-327"},
            "OLP-0401": {"BN-SRC-326", "BN-SRC-328"},
        }
        assert set(documented) == expected_infinite_valued.get(row["unit_id"], set())
        infinite_valued_logics_math_fix = (
            mathparts(audited_infinite_valued_logics) == target_math
        )
    many_valued_sequent_calculus_math_fix = False
    audited_many_valued_sequent_calculus = source
    if row["unit_id"] == "OLP-0403":
        repairs = [
            (
                r"!A_1, \dots, !A_n & \Sequent !B_1, \dots, !B_n",
                r"!A_1, \dots, !A_m & \Sequent !B_1, \dots, !B_n",
            ),
            (r"\pValue(!A) =", r"\pValue{v}(!A) ="),
        ]
        for old, new in repairs:
            assert audited_many_valued_sequent_calculus.count(old) == 1, old
            audited_many_valued_sequent_calculus = audited_many_valued_sequent_calculus.replace(old, new, 1)
    elif row["unit_id"] == "OLP-0404":
        old = "where each $\\Gamma_1$"
        new = "where each $\\Gamma_i$"
        assert audited_many_valued_sequent_calculus.count(old) == 1
        audited_many_valued_sequent_calculus = audited_many_valued_sequent_calculus.replace(old, new, 1)
    if 402 <= unit_number <= 406:
        expected_many_valued_sequent = {
            "OLP-0403": {"BN-SRC-329", "BN-SRC-330"},
            "OLP-0404": {"BN-SRC-331"},
        }
        assert set(documented) == expected_many_valued_sequent.get(row["unit_id"], set())
        many_valued_sequent_calculus_math_fix = (
            mathparts(audited_many_valued_sequent_calculus) == target_math
        )
        if row["unit_id"] in {"OLP-0403", "OLP-0405", "OLP-0406"}:
            assert formal_rule_bodies(source) == formal_rule_bodies(checked_target)
        if row["unit_id"] == "OLP-0406":
            assert sideways_derivation_before_caption(source) == sideways_derivation_before_caption(checked_target)
    normal_modal_opening_math_fix = False
    if 407 <= unit_number <= 412:
        expected_modal_opening = {
            "OLP-0410": {"BN-SRC-332"},
            "OLP-0411": {"BN-SRC-333", "BN-SRC-334"},
        }
        assert set(documented) == expected_modal_opening.get(row["unit_id"], set())
        audited_modal_opening = source
        if row["unit_id"] == "OLP-0410":
            old = r"$\lnot !A \lor !B)$"
            new = r"$\lnot !A \lor !B$"
            assert audited_modal_opening.count(old) == 1
            audited_modal_opening = audited_modal_opening.replace(old, new, 1)
        if row["unit_id"] == "OLP-0411":
            assert source.count(r"\tagitem{prvIf}{\indcase{!A}{(!B \liff") == 1
            assert checked_target.count(r"\tagitem{prvIff}{\indcase{!A}{(!B \liff") == 1
            assert source.count(r"\item \indcase{!A}{\Box !B}") == 1
            assert checked_target.count(r"\tagitem{prvBox}{\indcase{!A}{\Box !B}") == 1
        normal_modal_opening_math_fix = mathparts(audited_modal_opening) == target_math
    normal_modal_completion_math_fix = False
    if 413 <= unit_number <= 418:
        expected_modal_completion = {
            "OLP-0413": {"BN-SRC-335", "BN-SRC-342"},
            "OLP-0416": {"BN-SRC-336", "BN-SRC-337", "BN-SRC-338"},
            "OLP-0417": {"BN-SRC-339"},
            "OLP-0418": {"BN-SRC-340", "BN-SRC-341"},
        }
        assert set(documented) == expected_modal_completion.get(row["unit_id"], set())
        audited_modal_completion = source
        if row["unit_id"] == "OLP-0413":
            old = r"$\mSat/{M}{\Box\lnot !A}$."
            new = r"$\mSat/{M}{\Box\lnot !A}[w]$."
            assert audited_modal_completion.count(old) == 1
            audited_modal_completion = audited_modal_completion.replace(old, new, 1)
            assert source.count(r"\item\ollabel{defn:sub:mmodels-box}") == 1
            assert source.count(r"\item\ollabel{defn:sub:mmodels-diamond}") == 1
            assert checked_target.count(r"\tagitem{prvBox}{\ollabel{defn:sub:mmodels-box}") == 1
            assert checked_target.count(r"\tagitem{prvDiamond}{\ollabel{defn:sub:mmodels-diamond}") == 1
        if row["unit_id"] == "OLP-0416":
            old = r"\pSat{v}{!B \lif !C} \Leftrightarrow"
            new = r"\pSat{v}{!B \liff !C} \Leftrightarrow"
            assert audited_modal_completion.count(old) == 2
            before, found, after = audited_modal_completion.rpartition(old)
            assert found and r"\tagitem{prvIff}" in before
            audited_modal_completion = before + new + after
            old = r"\text{by definition of $\pSat{v}{}$}."
            new = r"\text{by definition of $\mSat{M}{}[w]$}."
            assert audited_modal_completion.count(old) == 1
            audited_modal_completion = audited_modal_completion.replace(old, new, 1)
            assert source.count(r"\tagitem{prvFalse}{\indcase{!A}{\lnot !B}") == 1
            assert checked_target.count(r"\tagitem{prvNot}{\indcase{!A}{\lnot !B}") == 1
        if row["unit_id"] == "OLP-0418":
            old = "\\mModel{M'} =\n  \\{W', R', V'\\}"
            new = r"\mModel{M'} = \tuple{W', R', V'}"
            assert audited_modal_completion.count(old) == 1
            audited_modal_completion = audited_modal_completion.replace(old, new, 1)
            old = r"\Entails \Box p \lif p$.}"
            new = r"\Entails/ \Box p \lif p$.}"
            assert audited_modal_completion.count(old) == 1
            audited_modal_completion = audited_modal_completion.replace(old, new, 1)
        normal_modal_completion_math_fix = mathparts(audited_modal_completion) == target_math

    frame_definability_math_fix = False
    if 419 <= unit_number <= 426:
        expected_frame_corrections = {
            "OLP-0423": {"BN-SRC-343", "BN-SRC-344"},
            "OLP-0424": {"BN-SRC-345"},
            "OLP-0426": {"BN-SRC-346", "BN-SRC-347", "BN-SRC-348"},
        }
        assert set(documented) == expected_frame_corrections.get(row["unit_id"], set())
        expected_math_delta = {
            "OLP-0423": (
                collections.Counter({r"\mSat{M}{\Box!A}": 1, r"V(q)=\emptyset)": 1}),
                collections.Counter({r"\mSat{M}{\Box!A}[w]": 1, r"V(q)=\emptyset": 1}),
            ),
            "OLP-0424": (
                collections.Counter({r"\Gamma=\{!F,!A_1,!A_2,\dots\}.": 1}),
                collections.Counter({
                    r"n\ge2": 1,
                    r"\Gamma=\{!F,!A_2,!A_3,\dots\}.": 1,
                    r"k=2": 1,
                    r"i\lek": 1,
                    r"i\ge2": 1,
                }),
            ),
            "OLP-0426": (
                collections.Counter({
                    r"\ST_x(\indfrm)=(\ST_x(!B)\liff\ST_x(!C))}": 1,
                    r"\Sat{M}{\lforall[y][(\Atom{Q}{x,y}\lif\Atom{X}{y})]\lif\Atom{X}{x}}": 1,
                }),
                collections.Counter({
                    r"\ST_x(\indfrm)=(\ST_x(!B)\liff\ST_x(!C))": 1,
                    r"\Sat{M}{\lforall[y][(\Atom{Q}{x,y}\lif\Atom{X}{y})]\lif\Atom{X}{x}}[s]": 1,
                }),
            ),
        }
        expected_removed, expected_added = expected_math_delta.get(
            row["unit_id"], (collections.Counter(), collections.Counter())
        )
        frame_definability_math_fix = (
            source_math - target_math == expected_removed
            and target_math - source_math == expected_added
        )
        if row["unit_id"] == "OLP-0426":
            assert source.count(r"\tagitem{prvTrue}{\indcase{!A}{\lfalse}") == 1
            assert checked_target.count(r"\tagitem{prvTrue}{\indcase{!A}{\ltrue}") == 1
            assert checked_target.count(r"\tagitem{prvIff}{\indcase{!A}{(!B \liff !C)}") == 1
    axioms_systems_math_fix = False
    if 427 <= unit_number <= 440:
        expected_axioms_corrections = {
            "OLP-0430": {"BN-SRC-349"},
            "OLP-0432": {"BN-SRC-350", "BN-SRC-351"},
            "OLP-0437": {"BN-SRC-352", "BN-SRC-353"},
        }
        assert set(documented) == expected_axioms_corrections.get(row["unit_id"], set())
        expected_axioms_delta = {
            "OLP-0430": (
                collections.Counter({r"K\in\Sigma": 1}),
                collections.Counter({r"\Ax{K}\in\Sigma": 1}),
            ),
            "OLP-0432": (
                collections.Counter({
                    r"\Log{K}\Proves\Box!A\lif(\Box!B\lif\Box(!A\land!B)))": 1,
                    r"\Log{K}\Proves\Subst{!C}{B}{q}": 1,
                }),
                collections.Counter({
                    r"\Log{K}\Proves\Box!A\lif(\Box!B\lif\Box(!A\land!B))": 1,
                    r"\Log{K}\Proves\Subst{!C}{!B}{q}": 1,
                }),
            ),
            "OLP-0437": (
                collections.Counter({
                    r"\Log{KT}\Proves\Log{D}": 1,
                    r"\Log{KTB}\Proves/\Log{4}": 1,
                    r"\Log{KTB}\Proves/\Log{5}": 1,
                }),
                collections.Counter({
                    r"\Log{KT}\Proves\Ax{D}": 1,
                    r"\Log{KTB}\Proves/\Ax{4}": 1,
                    r"\Log{KTB}\Proves/\Ax{5}": 1,
                }),
            ),
        }
        expected_removed, expected_added = expected_axioms_delta.get(
            row["unit_id"], (collections.Counter(), collections.Counter())
        )
        axioms_systems_math_fix = (
            source_math - target_math == expected_removed
            and target_math - source_math == expected_added
        )
    modal_completeness_math_fix = False
    if 441 <= unit_number <= 449:
        expected_modal_completeness_corrections = {
            "OLP-0443": {"BN-SRC-354", "BN-SRC-355"},
            "OLP-0445": {"BN-SRC-356", "BN-SRC-357", "BN-SRC-358"},
            "OLP-0447": {"BN-SRC-359"},
        }
        assert set(documented) == expected_modal_completeness_corrections.get(
            row["unit_id"], set()
        )
        expected_modal_completeness_delta = {
            "OLP-0443": (
                collections.Counter({
                    r"!A\in\Gamma": 1,
                    r"!A\lif!B\notin\Gamma": 1,
                }),
                collections.Counter({
                    r"\lnot!A\in\Gamma": 1,
                    r"!A\liff!B\notin\Gamma": 1,
                }),
            ),
            "OLP-0445": (
                collections.Counter({
                    r"V^\Sigma)": 1,
                    r"\Sigma\Proves!B_1\lif(!B_2\lif\cdots(!B_n\lif!A)\cdots)": 1,
                    r"\Sigma\Proves\Box!B_1\lif(\Box!B_2\lif\cdots(\Box!B_n\lif\Box!A)\cdots)": 1,
                    r"\Box\Box^{-1}\Gamma\Proves\Box!A": 1,
                }),
                collections.Counter({
                    r"V^\Sigma": 1,
                    r"\Sigma\Proves!B_1\lif(!B_2\lif\cdots(!B_k\lif!A)\cdots)": 1,
                    r"\Sigma\Proves\Box!B_1\lif(\Box!B_2\lif\cdots(\Box!B_k\lif\Box!A)\cdots)": 1,
                    r"\Box\Box^{-1}\Gamma\Proves[\Sigma]\Box!A": 1,
                }),
            ),
        }
        expected_removed, expected_added = expected_modal_completeness_delta.get(
            row["unit_id"], (collections.Counter(), collections.Counter())
        )
        modal_completeness_math_fix = (
            source_math - target_math == expected_removed
            and target_math - source_math == expected_added
        )
    modal_completeness_control_fix = (
        row["unit_id"] == "OLP-0447"
        and "BN-SRC-359" in documented
        and controls(source) - controls(checked_target)
        == collections.Counter({r"\olref[mod]{prop:diamond}": 1})
        and controls(checked_target) - controls(source)
        == collections.Counter({r"\olref[mod]{lem:box-iff-diamond}": 1})
    )
    filtrations_math_fix = False
    if 450 <= unit_number <= 459:
        expected_filtration_corrections = {
            "OLP-0451": {"BN-SRC-360", "BN-SRC-361"},
            "OLP-0456": {"BN-SRC-362"},
            "OLP-0457": {"BN-SRC-365"},
            "OLP-0459": {"BN-SRC-363", "BN-SRC-364"},
        }
        assert set(documented) == expected_filtration_corrections.get(
            row["unit_id"], set()
        )
        expected_filtration_delta = {
            "OLP-0451": (
                collections.Counter({
                    r"\mSat{M}{\Box!B}[v]": 1,
                    r"[w]\inV^*": 1,
                }),
                collections.Counter({
                    r"\mSat{M}{!B}[v]": 1,
                    r"[w]\inV^*(p)": 1,
                }),
            ),
            "OLP-0456": (
                collections.Counter({r"\mSat{M^*}{!A}[w]": 1}),
                collections.Counter({r"\mSat{M^*}{!A}[{[w]}]": 1}),
            ),
            "OLP-0459": (
                collections.Counter({r"w_2": 1, r"w_5": 1}),
                collections.Counter({r"[w_2]": 1, r"[w_5]": 1}),
            ),
        }
        expected_removed, expected_added = expected_filtration_delta.get(
            row["unit_id"], (collections.Counter(), collections.Counter())
        )
        filtrations_math_fix = (
            source_math - target_math == expected_removed
            and target_math - source_math == expected_added
        )
    modal_tableaux_math_fix = False
    temporal_math_fix = False
    if 460 <= unit_number <= 469:
        expected_modal_tableaux_corrections = {
            "OLP-0462": {"BN-SRC-371"},
            "OLP-0464": {
                "BN-SRC-366", "BN-SRC-367", "BN-SRC-368",
                "BN-SRC-369", "BN-SRC-370", "BN-SRC-372",
            },
            "OLP-0465": {"BN-SRC-373"},
            "OLP-0466": {"BN-SRC-374", "BN-SRC-375", "BN-SRC-376"},
            "OLP-0468": {
                "BN-SRC-377", "BN-SRC-378", "BN-SRC-379",
                "BN-SRC-380", "BN-SRC-381", "BN-SRC-382",
                "BN-SRC-383", "BN-SRC-384",
            },
            "OLP-0469": {"BN-SRC-385", "BN-SRC-386", "BN-SRC-387", "BN-SRC-388"},
        }
        assert set(documented) == expected_modal_tableaux_corrections.get(
            row["unit_id"], set()
        )
        expected_modal_tableaux_delta = {
            "OLP-0464": (
                collections.Counter({
                    r"\mSat{M}{!A}[w]": 1,
                    r"\sFmla{\False}{!B\lor!C}\in\Gamma": 1,
                    r"\sFmla{\False}{!A}[\sigma.n]": 1,
                    r"\Struct{M}": 2,
                    r"\Sat{M}{\Gamma}[f]": 2,
                    r"\sFmla{\True}{!A}[\sigma.n]": 1,
                    r"\Gamma\Proves!A": 1,
                }),
                collections.Counter({
                    r"\mSat/{M}{!A}[w]": 1,
                    r"\sFmla{\False}{!B\lor!C}[\sigma]\in\Gamma": 1,
                    r"\sFmla{\False}{!B}[\sigma.n]": 1,
                    r"\mModel{M}": 2,
                    r"\mSat{M}{\Gamma}[f]": 2,
                    r"\sFmla{\True}{!B}[\sigma.n]": 1,
                    r"\Gamma\Entails!A": 1,
                }),
            ),
            "OLP-0465": (
                collections.Counter({r"\Log{S5}\Proves\Ax{5}": 1}),
                collections.Counter({r"\Log{S5}\Proves\Box!A\lif\Box\Diamond!A": 1}),
            ),
            "OLP-0466": (
                collections.Counter({
                    r"\sFmla{\True}{\Box!B}[\sigma]": 1,
                    r"\mSat{M}{\Box!B}[f(\sigma).n]": 1,
                    r"\mSat/{M}{\Diamond!B}[f(\sigma).n]": 1,
                }),
                collections.Counter({
                    r"\sFmla{\False}{\Diamond!B}[\sigma]": 1,
                    r"\mSat{M}{\Box!B}[f(\sigma.n)]": 1,
                    r"\mSat/{M}{\Diamond!B}[f(\sigma.n)]": 1,
                }),
            ),
            "OLP-0468": (
                collections.Counter({
                    r"\sFmla{\True}{!B\land!C}": 1,
                    r"\sFmla{\False}{!B}[\sigma]": 1,
                    r"\sFmla{\False}{\Box}[\sigma]": 1,
                    r"\sFmla{\True}{\Diamond}[\sigma]": 1,
                    r"\sFmla{\False}{\Box}[\sigma.n]": 1,
                    r"\sFmla{\True}{\Diamond}[\sigma.n]": 1,
                    r"\sFmla{\True}{\Box}[\sigma]": 1,
                    r"\sFmla{\False}{\Diamond}[\sigma]": 1,
                    r"\sFmla{\True}{\Box}[\sigma.n]": 1,
                    r"\sFmla{\False}{\Diamond}[\sigma.n]": 1,
                    r"\mSat/{M(\Delta)}{!B}[\sigma]": 3,
                }),
                collections.Counter({
                    r"\sFmla{\True}{!B\land!C}[\sigma]": 1,
                    r"\sFmla{\True}{!B}[\sigma]": 1,
                    r"\sFmla{\False}{\Box!B}[\sigma]": 1,
                    r"\sFmla{\True}{\Diamond!B}[\sigma]": 1,
                    r"\sFmla{\False}{!B}[\sigma.n]": 2,
                    r"\sFmla{\True}{!B}[\sigma.n]": 2,
                    r"\sFmla{\True}{\Box!B}[\sigma]": 1,
                    r"\sFmla{\False}{\Diamond!B}[\sigma]": 1,
                    r"\mSat/{M(\Delta)}{!C}[\sigma]": 3,
                }),
            ),
            "OLP-0469": (
                collections.Counter({
                    r"\Entails/A": 1,
                    r"\TRule{\True}{\Diamond}": 1,
                    r"\sFmla{\True}{q}[1.1]": 1,
                    r"\sFmla{\True}{\Diamond(p\landq)}[1]": 1,
                }),
                collections.Counter({
                    r"\Entails/!A": 1,
                    r"\TRule{\False}{\Diamond}": 1,
                    r"\sFmla{\True}{q}[1.2]": 1,
                    r"\sFmla{\False}{\Diamond(p\landq)}[1]": 1,
                }),
            ),
        }
        expected_removed, expected_added = expected_modal_tableaux_delta.get(
            row["unit_id"], (collections.Counter(), collections.Counter())
        )
        modal_tableaux_math_fix = (
            source_math - target_math == expected_removed
            and target_math - source_math == expected_added
        )
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
    if 191 <= int(row["unit_id"].split("-")[1]) <= 197:
        expected_arithmetic = {
            "OLP-0192": {"BN-SRC-118", "BN-SRC-119", "BN-SRC-120"},
            "OLP-0193": {"BN-SRC-121"},
            "OLP-0194": {"BN-SRC-122", "BN-SRC-123"},
            "OLP-0195": {"BN-SRC-124", "BN-SRC-125", "BN-SRC-126", "BN-SRC-127"},
            "OLP-0196": {"BN-SRC-128", "BN-SRC-129", "BN-SRC-130", "BN-SRC-131"},
            "OLP-0197": {"BN-SRC-132", "BN-SRC-133"},
        }
        assert set(documented) == expected_arithmetic.get(row["unit_id"], set())
    if 198 <= int(row["unit_id"].split("-")[1]) <= 202:
        expected_interpolation = {
            "OLP-0200": {"BN-SRC-134", "BN-SRC-135"},
            "OLP-0201": {"BN-SRC-136"},
            "OLP-0202": {"BN-SRC-137", "BN-SRC-138"},
        }
        assert set(documented) == expected_interpolation.get(row["unit_id"], set())
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
    elif row["unit_id"] == "OLP-0192":
        assert arithmetic_math_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-118", "BN-SRC-119", "BN-SRC-120"],
            "string_model_operations_use_string_arguments": True,
            "string_model_less_than_interpretation_supplied": True,
            "proof_code_argument_restored": "x",
        }
    elif row["unit_id"] == "OLP-0193":
        assert arithmetic_prose_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-121",
            "surjectivity_failure_refers_to_range": True,
        }
    elif row["unit_id"] == "OLP-0194":
        assert arithmetic_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-122", "BN-SRC-123"],
            "empty_finite_family_case": True,
            "downward_lowenheim_skolem_invoked": True,
        }
    elif row["unit_id"] == "OLP-0195":
        assert arithmetic_math_fix and arithmetic_prose_fix
        tex_command_check = {
            "documented_corrections": [
                "BN-SRC-124",
                "BN-SRC-125",
                "BN-SRC-126",
                "BN-SRC-127",
            ],
            "sum_parenthesis_closed": True,
            "only_nonstandard_K_element_is_a": True,
            "Q5_rhs_uses_a": True,
            "general_nonstandard_element_uses_x": True,
        }
    elif row["unit_id"] == "OLP-0196":
        assert arithmetic_math_fix and arithmetic_prose_fix
        tex_command_check = {
            "documented_corrections": [
                "BN-SRC-128",
                "BN-SRC-129",
                "BN-SRC-130",
                "BN-SRC-131",
            ],
            "trichotomy_formula_balanced": True,
            "predecessor_claim_excludes_zero": True,
            "addition_notation_is_nssplus": True,
            "countability_scope_is_explicit": True,
        }
    elif row["unit_id"] == "OLP-0197":
        assert arithmetic_math_fix and arithmetic_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-132", "BN-SRC-133"],
            "set_builder_binds_x": True,
            "tennenbaum_statement_is_up_to_isomorphism": True,
        }
    elif row["unit_id"] == "OLP-0200":
        assert interpolation_math_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-134", "BN-SRC-135"],
            "universal_consequence_uses_H": True,
            "existential_formula_brackets_restored": True,
        }
    elif row["unit_id"] == "OLP-0201":
        assert interpolation_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-136",
            "predicate_transport_starts_from_M1": True,
        }
    elif row["unit_id"] == "OLP-0202":
        assert interpolation_math_fix and interpolation_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-137", "BN-SRC-138"],
            "corrected_P_prime_atom": True,
            "theorem_statement_is_biconditional": True,
        }
    bounded_minimization_math_fix = False
    s_m_n_index_fix = False
    halting_parenthetical_name_fix = False
    russell_self_membership_fix = False
    ce_equivalence_math_fixes = False
    complement_ce_index_fixes = False
    reducibility_pair_fix = False
    reduction_type_fix = False
    complete_ce_direction_fix = False
    total_partial_equality_fix = False
    rice_partial_equality_fix = False
    rice_monotonicity_prose_fix = False
    fixed_point_partial_equalities_fix = False
    fixed_point_application_scope_fixes = False
    self_reference_partial_equality_fix = False
    representing_tm_table_fix = False
    configuration_empty_input_fix = False
    unary_adder_endpoint_normalization = False
    disciplined_adder_endpoint_normalization = False
    combined_machine_fix_and_endpoint_normalization = False
    partial_undefined_output_fix = False
    variant_boundary_marker_fix = False
    standard_machine_simulation_fix = False
    universal_output_decoding_fix = False
    halting_machine_combination_notation_fix = False
    representing_fo_fixes = False
    representing_formula_classification_fix = False
    verification_representation_fixes = False
    decision_unsolvability_fixes = False
    trakhtenbrot_fixes = False
    if row["unit_id"] == "OLP-0217":
        assert source.count("The less-than relation, $x \\leq y$") == 1
        assert "অনধিক সম্বন্ধ $x \\leq y$" in checked_target
        assert "BN-SRC-139" in documented
        tex_command_check = {
            "documented_correction": "BN-SRC-139",
            "less_than_or_equal_relation_named_accurately": True,
        }
    elif row["unit_id"] == "OLP-0218":
        source_fragment = "m_R(\\vec{z},y+1)=y+1"
        target_fragment = "m_R(\\vec{x},y+1)=y+1"
        bounded_minimization_math_fix = (
            source_math - target_math == collections.Counter({source_fragment: 1})
            and target_math - source_math == collections.Counter({target_fragment: 1})
            and "BN-SRC-140" in documented
        )
        assert source.count("$m_R(\\vec{z}, y+1) = y+1$") == 1
        assert checked_target.count("$m_R(\\vec{x}, y+1) = y+1$") == 1
        assert bounded_minimization_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-140",
            "third_case_preserves_argument_vector_x": True,
        }
    elif row["unit_id"] == "OLP-0219":
        assert "remainder\nwhen dividing $x$ by $y$ is $> 0$" in source
        assert "$y$-কে $x$ দিয়ে\nভাগ করার ভাগশেষ $> 0$" in checked_target
        assert "BN-SRC-141" in documented
        tex_command_check = {
            "documented_correction": "BN-SRC-141",
            "nondivisibility_uses_y_divided_by_x": True,
        }
    elif row["unit_id"] == "OLP-0232":
        s_m_n_index_fix = (
            source_math - target_math
            == collections.Counter(
                {
                    "s^m_n(x,a_0,\\dots,a_{m-1})": 1,
                    "x": 1,
                }
            )
            and target_math - source_math
            == collections.Counter(
                {
                    "s^m_n(e,a_0,\\dots,a_{m-1})": 1,
                    "e": 1,
                }
            )
            and "BN-SRC-142" in documented
        )
        assert source.count("It you think of $x$ as the description") == 1
        assert checked_target.count("$e$-কে কোনো টুরিং যন্ত্রের বর্ণনা") == 1
        assert s_m_n_index_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-142",
            "specialized_program_index": "e",
            "turing_machine_description_index": "e",
        }
    elif row["unit_id"] == "OLP-0233":
        assert "is a\nunary recursive function" in source
        assert re.search(r"একটি একস্থানী আংশিক পুনরাবৃত্ত\s+অপেক্ষক", checked_target)
        assert "BN-SRC-143" in documented
        tex_command_check = {
            "documented_correction": "BN-SRC-143",
            "derived_unary_function_class": "partial recursive",
        }
    elif row["unit_id"] == "OLP-0234":
        assert "partial computable function that is total for the\npartial computable functions" in source
        assert "আংশিক গণনসাধ্য অপেক্ষকদের জন্য সার্বজনীন" in checked_target
        assert "BN-SRC-144" in documented
        tex_command_check = {
            "documented_correction": "BN-SRC-144",
            "partial_universal_function_property": "universal",
        }
    elif row["unit_id"] == "OLP-0235":
        halting_parenthetical_name_fix = (
            source_math - target_math == collections.Counter({"h": 1})
            and target_math - source_math == collections.Counter({"g": 1})
            and "BN-SRC-145" in documented
        )
        assert "$h$~can only take the value~$0$ if it\nis defined" in source
        assert "$g$ সংজ্ঞায়িত হলে তার একমাত্র সম্ভব মান~$0$" in checked_target
        assert halting_parenthetical_name_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-145",
            "only_defined_value_zero_applies_to": "g",
        }
    elif row["unit_id"] == "OLP-0236":
        russell_self_membership_fix = (
            source_math - target_math == collections.Counter({"X\\notinS": 1})
            and target_math - source_math == collections.Counter({"S\\notinS": 1})
            and "BN-SRC-146" in documented
        )
        assert "$S\n  \\in S$ if and only if $X \\notin S$" in source
        assert "$S \\in S$ যদি এবং কেবল যদি $S \\notin S$" in checked_target
        assert russell_self_membership_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-146",
            "russell_self_nonmembership_subject": "S",
        }
    elif row["unit_id"] == "OLP-0239":
        ce_equivalence_math_fixes = (
            source_math - target_math
            == collections.Counter(
                {
                    "\\cfind{e}(x)=U(\\umin{s}{T(e,x,s)}).": 1,
                    "\\cfind{e}(x)\\fdefined=y": 1,
                }
            )
            and target_math - source_math
            == collections.Counter(
                {
                    "\\cfind{e}(x)\\simeqU(\\umin{s}{T(e,x,s)}).": 1,
                    "\\cfind{e}((z)_0)\\fdefined=y": 1,
                }
            )
            and all(f"BN-SRC-{number}" in documented for number in range(147, 150))
        )
        assert "$S$ is the range of a computable function" in source
        assert "সর্বত্র অসংজ্ঞায়িত আংশিক গণনসাধ্য অপেক্ষকের সংজ্ঞাক্ষেত্রই সেটটি" in checked_target
        assert ce_equivalence_math_fixes
        tex_command_check = {
            "documented_corrections": ["BN-SRC-147", "BN-SRC-148", "BN-SRC-149"],
            "normal_form_equality": "simeq",
            "reverse_range_witness_input": "(z)_0",
            "empty_ce_set_domain_case_supplied": True,
        }
    elif row["unit_id"] == "OLP-0242":
        complement_ce_index_fixes = (
            source_math - target_math
            == collections.Counter({"\\cfind{e}": 2, "T(e,x,h(x))": 2, "\\cfind{f}": 1})
            and target_math - source_math
            == collections.Counter({"\\cfind{d}": 3, "T(d,x,h(x))": 2})
            and all(f"BN-SRC-{number}" in documented for number in range(150, 152))
        )
        assert "if and only if $T(e, x, h(x))$" in source
        assert "যদি এবং কেবল যদি $T(d, x, h(x))$" in checked_target
        assert "halting computations of\n$\\cfind{e}$ and $\\cfind{f}$" in source
        assert "$\\cfind{d}$ ও $\\cfind{e}$-এর থামা গণনা" in checked_target
        assert complement_ce_index_fixes
        tex_command_check = {
            "documented_corrections": ["BN-SRC-150", "BN-SRC-151"],
            "membership_test_index": "d",
            "informal_parallel_indices": ["d", "e"],
        }
    elif row["unit_id"] == "OLP-0243":
        reducibility_pair_fix = (
            source_math - target_math
            == collections.Counter({"K_0=\\Setabs{\\tuple{x,e}}{x\\inW_e}": 1})
            and target_math - source_math
            == collections.Counter({"K_0=\\Setabs{\\tuple{e,x}}{x\\inW_e}": 1})
            and "BN-SRC-152" in documented
        )
        assert reducibility_pair_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-152",
            "halting_pair_order": ["e", "x"],
        }
    elif row["unit_id"] == "OLP-0244":
        reduction_type_fix = (
            source_math - target_math == collections.Counter({"f\\colonA\\toB": 1})
            and target_math - source_math == collections.Counter({"f\\colon\\Nat\\to\\Nat": 1})
            and "BN-SRC-153" in documented
        )
        assert reduction_type_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-153",
            "many_one_reduction_type": "Nat to Nat",
        }
    elif row["unit_id"] == "OLP-0245":
        complete_ce_direction_fix = (
            "$K$ can be reduced to $K_0$ in much the same way." in source
            and "$K_0$-কে অনেকটা একইভাবে~$K$-তে হ্রাস করা যায়।" in checked_target
            and "BN-SRC-154" in documented
        )
        assert complete_ce_direction_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-154",
            "completeness_reduction_direction": "K_0 <=_m K",
        }
    elif row["unit_id"] == "OLP-0247":
        total_partial_equality_fix = (
            source_math - target_math
            == collections.Counter({"\\cfind{k(x)}(y)=\\begin{cases}0&\\\\\\fundefined&\\end{cases}": 1})
            and target_math - source_math
            == collections.Counter({"\\cfind{k(x)}(y)\\simeq\\begin{cases}0&\\\\\\fundefined&\\end{cases}": 1})
            and "BN-SRC-155" in documented
        )
        assert total_partial_equality_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-155",
            "specialized_partial_function_equality": "simeq",
        }
    elif row["unit_id"] == "OLP-0248":
        rice_partial_equality_fix = (
            source_math - target_math == collections.Counter({"\\cfind{s(e,x)}(y)=h_x(y)": 1})
            and target_math - source_math == collections.Counter({"\\cfind{s(e,x)}(y)\\simeqh_x(y)": 1})
            and "BN-SRC-156" in documented
        )
        rice_monotonicity_prose_fix = (
            "whenever $y < y'$, $\\cfind{x}(y) \\fdefined$, and\n    if $\\cfind{x}(y') \\fdefined$" in source
            and "যখনই $y < y'$, এবং $\\cfind{x}(y) \\fdefined$ ও\n    $\\cfind{x}(y') \\fdefined$, তখন" in checked_target
            and "BN-SRC-157" in documented
        )
        assert rice_partial_equality_fix and rice_monotonicity_prose_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-156", "BN-SRC-157"],
            "specialized_partial_function_equality": "simeq",
            "strict_increase_requires_both_values_defined": True,
            "nested_setbuilder_text_math_checked": True,
        }
    elif row["unit_id"] == "OLP-0249":
        fixed_point_partial_equalities_fix = (
            source_math - target_math
            == collections.Counter(
                {
                    "\\cfind{e}(y)&=\\fn{Un}(f(e),y)\\\\&=\\cfind{f(e)}(y).": 1,
                    "\\cfind{e}(y)&=\\cfind{f(e)}(y)\\\\&=g(e,y).": 1,
                }
            )
            and target_math - source_math
            == collections.Counter(
                {
                    "\\cfind{e}(y)&\\simeq\\fn{Un}(f(e),y)\\\\&\\simeq\\cfind{f(e)}(y).": 1,
                    "\\cfind{e}(y)&\\simeq\\cfind{f(e)}(y)\\\\&\\simeqg(e,y).": 1,
                }
            )
            and "BN-SRC-158" in documented
        )
        assert fixed_point_partial_equalities_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-158",
            "equivalence_proof_partial_equalities": 4,
        }
    elif row["unit_id"] == "OLP-0250":
        fixed_point_application_scope_fixes = (
            "Let $f$ be any computable function" in source
            and "$f$-কে যেকোনো আংশিক গণনসাধ্য অপেক্ষক ধরি" in checked_target
            and "প্রার্থী অপেক্ষকটি এই স্থির সূচকে অসংজ্ঞায়িত হলে" in checked_target
            and all(f"BN-SRC-{number}" in documented for number in range(159, 161))
        )
        assert fixed_point_application_scope_fixes
        tex_command_check = {
            "documented_corrections": ["BN-SRC-159", "BN-SRC-160"],
            "candidate_scope": "partial computable",
            "undefined_candidate_index_case_supplied": True,
        }
    elif row["unit_id"] == "OLP-0251":
        self_reference_partial_equality_fix = (
            source_math - target_math == collections.Counter({"\\cfind{e}(y)=g(e,y)": 1})
            and target_math - source_math == collections.Counter({"\\cfind{e}(y)\\simeqg(e,y)": 1})
            and "BN-SRC-161" in documented
        )
        assert self_reference_partial_equality_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-161",
            "self_reference_partial_equality": "simeq",
        }
    elif row["unit_id"] == "OLP-0254":
        initial_head_position_fix = (
            "At the outset, the head scans the leftmost square\nand in a specified" in source
            and "শুরুতে হেডটি নিবেশের জন্য নির্ধারিত বাঁদিকের প্রথম ঘরটি পড়ে" in checked_target
            and "BN-SRC-162" in documented
        )
        assert initial_head_position_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-162",
            "initial_head_position": "first input square right of end marker",
        }
    elif row["unit_id"] == "OLP-0255":
        state_one_fix = (
            "machine starts in state one, scanning the leftmost" in source
            and "যন্ত্রটি দশা~$q_0$-তে বাঁদিকের" in checked_target
            and "BN-SRC-163" in documented
        )
        audited_table = source
        old_q0_stroke = r"\TMtrans{\TMstroke}{q_1}{\TMright}"
        old_q1_blank = r"\TMtrans{\TMblank}{q_1}{\TMright}"
        old_q1_stroke = r"\TMtrans{\TMstroke}{q_0}{\TMright}"
        assert audited_table.count(old_q0_stroke) == 3
        assert audited_table.count(old_q1_blank) == 1
        assert audited_table.count(old_q1_stroke) == 1
        audited_table = audited_table.replace(
            old_q0_stroke, r"\TMtrans{q_1}{\TMstroke}{\TMright}", 1
        )
        audited_table = audited_table.replace(
            old_q1_blank, r"\TMtrans{q_1}{\TMblank}{\TMright}", 1
        )
        audited_table = audited_table.replace(
            old_q1_stroke, r"\TMtrans{q_0}{\TMstroke}{\TMright}", 1
        )
        representing_tm_table_fix = (
            mathparts(audited_table) - target_math == collections.Counter()
            and target_math - mathparts(audited_table) == collections.Counter({"q_0": 1})
            and "BN-SRC-164" in documented
        )
        assert state_one_fix and representing_tm_table_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-163", "BN-SRC-164"],
            "initial_configuration_state": "q_0",
            "machine_table_field_order": ["new state", "new symbol", "movement direction"],
            "corrected_machine_table_cells": 3,
        }
    elif row["unit_id"] == "OLP-0257":
        configuration_empty_input_fix = (
            source_math - target_math == collections.Counter()
            and target_math - source_math
            == collections.Counter({r"\tuple{\TMendtape\frown\TMblank,1,q_0}.": 1})
            and all(f"BN-SRC-{number}" in documented for number in range(165, 169))
        )
        flattened_source = re.sub(r"\s+", " ", source)
        assert "input string begins immediately to the left end marker" in flattened_source
        assert "নিবেশ-প্রতীকক্রমটি বাঁ প্রান্তের\nচিহ্নটির ঠিক ডান পাশে শুরু হয়" in checked_target
        assert "সসীম\nবা অসীম অনুক্রম~$C_i$" in checked_target
        assert "এমন প্রতীকক্রম না থাকলে" in checked_target
        assert configuration_empty_input_fix
        tex_command_check = {
            "documented_corrections": [
                "BN-SRC-165",
                "BN-SRC-166",
                "BN-SRC-167",
                "BN-SRC-168",
            ],
            "input_begins_right_of_end_marker": True,
            "empty_input_configuration_has_scanned_blank": True,
            "runs_allow_finite_or_infinite_sequences": True,
            "output_requires_preserved_end_marker_form": True,
        }
    elif row["unit_id"] == "OLP-0258":
        old = (
            r"edge [loop above] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (B)"
            "\n        (B) edge"
        )
        new = (
            r"edge [loop above] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (A)"
            "\n        (B) edge"
        )
        assert source.count(old) == 1
        audited_unary = source.replace(old, new, 1)
        unary_adder_endpoint_normalization = (
            mathparts(audited_unary) == target_math
            and "BN-SRC-173" in documented
            and "BN-NORM-169" in normalizations
        )
        flattened_source = re.sub(r"\s+", " ", source)
        partial_undefined_output_fix = (
            "does not halt at all, or with an output that is not a single block" in flattened_source
            and "থামলেও তার কোনো নির্গম নির্ধারিত হয় না" in checked_target
            and "BN-SRC-173" in documented
        )
        assert unary_adder_endpoint_normalization and partial_undefined_output_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-173",
            "source_normalization": "BN-NORM-169",
            "rendered_addition_q0_stroke_edge": "q_0 self-loop in source and target",
            "normalized_endpoint_count": 1,
            "tikz_loop_style_overrides_explicit_endpoint": True,
            "undefined_value_allows_halt_without_defined_output": True,
        }
    elif row["unit_id"] == "OLP-0260":
        old = (
            r"edge [loop below] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (B)"
            "\n        (B) edge"
        )
        new = (
            r"edge [loop below] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (A)"
            "\n        (B) edge"
        )
        assert source.count(old) == 1
        audited_disciplined = source.replace(old, new, 1)
        disciplined_adder_endpoint_normalization = (
            mathparts(audited_disciplined) == target_math
            and "BN-NORM-170" in normalizations
        )
        assert disciplined_adder_endpoint_normalization
        tex_command_check = {
            "source_normalization": "BN-NORM-170",
            "rendered_addition_q0_stroke_edge": "q_0 self-loop in source and target",
            "normalized_endpoint_count": 1,
            "tikz_loop_style_overrides_explicit_endpoint": True,
        }
    elif row["unit_id"] == "OLP-0261":
        old = (
            r"edge [loop above] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (B)"
            "\n        (B) edge"
        )
        new = (
            r"edge [loop above] node {\TMtrans{\TMstroke}{\TMstroke}{\TMright}} (A)"
            "\n        (B) edge"
        )
        assert source.count(old) == 3
        audited_combined = source.replace(old, new)
        audited_combined_math = mathparts(audited_combined)
        combined_machine_fix_and_endpoint_normalization = (
            audited_combined_math - target_math == collections.Counter()
            and target_math - audited_combined_math
            == collections.Counter({r"\delta(q,\sigma)": 1})
            and "BN-SRC-171" in documented
            and "BN-NORM-172" in normalizations
            and r"যদি $q \in Q$ এবং $\delta(q,\sigma)$ সংজ্ঞায়িত হয়" in checked_target
        )
        assert "\\delta(q,\\sigma) & \\text{if $q \\in Q$}\\\\" in source
        assert combined_machine_fix_and_endpoint_normalization
        tex_command_check = {
            "documented_correction": "BN-SRC-171",
            "source_normalization": "BN-NORM-172",
            "first_machine_branch_requires_defined_transition": True,
            "rendered_addition_q0_stroke_edge": "q_0 self-loop in source and target",
            "normalized_endpoint_count": 3,
            "tikz_loop_style_overrides_explicit_endpoint": True,
        }
    elif row["unit_id"] == "OLP-0262":
        variant_boundary_marker_fix = (
            "nothing prevents us from writing and reading $\\TMendtape$\n"
            "on squares other than square~$0$" in source
            and "আবার ঘর~$0$-এর চিহ্নটিও মুছে ফেলা যায়" in checked_target
            and "কখনও না মুছে এবং অন্য কোথাও না লিখে" in checked_target
            and "BN-SRC-174" in documented
        )
        assert variant_boundary_marker_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-174",
            "reserved_boundary_marker_never_overwritten": True,
            "reserved_boundary_marker_never_written_elsewhere": True,
            "left_transition_deletion_uses_reserved_marker": True,
        }
    elif row["unit_id"] == "OLP-0266":
        standard_machine_simulation_fix = (
            "why every Turing machine can be computed by a\n"
            "  ``standard'' machine" in source
            and "প্রতিটি টুরিং যন্ত্রকে কেন\n"
            "  কোনো “মানক” যন্ত্র অনুকরণ করতে পারে" in checked_target
            and source_math == target_math
            and "BN-SRC-175" in documented
        )
        assert standard_machine_simulation_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-175",
            "standard_machine_relation": "simulates arbitrary machine behavior",
        }
    elif row["unit_id"] == "OLP-0267":
        universal_output_decoding_fix = (
            "For\n  each block of three~$\\TMstroke$'s" in source
            and "If $U$ encounters something other than a block of\n"
            "  three~$\\TMstroke$'s" in source
            and "প্রথম এক-দাগের খণ্ডটি শেষ-চিহ্নের সংকেত" in checked_target
            and "দুই-দাগের ফাঁকা-প্রতীকের সংকেত থাকলে তার পরের বাকি সব খণ্ডও একই"
            in re.sub(r"\s+", " ", checked_target)
            and source_math == target_math
            and "BN-SRC-176" in documented
        )
        assert universal_output_decoding_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-176",
            "leading_end_marker_code_checked": True,
            "output_stroke_code_is_three": True,
            "trailing_blank_code_is_two": True,
            "entire_encoded_tape_shape_validated": True,
        }
    elif row["unit_id"] == "OLP-0268":
        old_combination = r"S\concatJ"
        new_combination = r"S\frownJ"
        halting_machine_combination_notation_fix = (
            source_math - target_math == collections.Counter({old_combination: 2})
            and target_math - source_math == collections.Counter({new_combination: 2})
            and source.count("$S \\concat J$") == 1
            and source.count("$S\n  \\concat J$") == 1
            and checked_target.count("$S \\frown J$") == 2
            and "BN-SRC-177" in documented
        )
        assert halting_machine_combination_notation_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-177",
            "machine_combination_symbol": "frown",
            "corrected_occurrences": 2,
        }
    elif row["unit_id"] == "OLP-0270":
        audited_representation = source
        old = (
            r"\Obj S_{\sigma'}(x', y') \land" + "\n"
            r"!A(x, y))) \land {}"
        )
        new = (
            r"\Obj S_{\sigma'}(x', y') \land" + "\n"
            r"!A(x', y))) \land {}"
        )
        assert audited_representation.count(old) == 1
        audited_representation = audited_representation.replace(old, new, 1)
        representing_formula_classification_fix = (
            "let $!A(x, y)$ be the conjunction of all !!{sentence}s" in source
            and "$!A(x,y)$ বলতে $\\sigma\\in\\Sigma$-এর প্রত্যেকটির জন্য" in checked_target
            and "সব !!{formula}-র সংযোজন" in checked_target
            and semantic_tokens(source)
            - semantic_tokens(checked_target)
            == collections.Counter({"!!{sentence}s": 1})
            and semantic_tokens(checked_target)
            - semantic_tokens(source)
            == collections.Counter({"!!{formula}": 1})
            and "BN-SRC-178" in documented
        )
        representing_fo_fixes = (
            mathparts(audited_representation) == target_math
            and representing_formula_classification_fix
            and set(documented) == {"BN-SRC-178", "BN-SRC-179"}
        )
        assert representing_fo_fixes
        tex_command_check = {
            "documented_corrections": ["BN-SRC-178", "BN-SRC-179"],
            "A_xy_classified_as_formula": True,
            "left_move_frame_excludes_written_square": "x-prime",
        }
    elif row["unit_id"] == "OLP-0271":
        audited_verification = source
        replacements = [
            ("$T(M, w) \\Entails !E(M, w)$", "$!T(M, w) \\Entails !E(M, w)$"),
            ("iff $T$, when run on input~$w$", "iff $M$, when run on input~$w$"),
            (
                "$\\Obj Q_{q'}(\\num{m}, \\num{n}) \\land S_{\\sigma'}(\\num{m},\n"
                "\\num{n}) \\Entails \\bigvee_{\\tuple{q, \\sigma} \\in X} (\\Obj Q_q(\\num{m},\n"
                "\\num{n}) \\land \\Obj S_{\\sigma}(\\num{m}, \\num{n}))$",
                "$\\Obj Q_q(\\num{m},\\num{n})\\land\\Obj S_\\sigma(\\num{m},\\num{n})\n"
                "\\Entails \\bigvee_{\\tuple{q',\\sigma'}\\in X}\n"
                "(\\Obj Q_{q'}(\\num{m},\\num{n})\\land\n"
                "\\Obj S_{\\sigma'}(\\num{m},\\num{n}))$",
            ),
            ("$\\tuple{q',\\sigma'} \\in X$", "$\\tuple{q,\\sigma}\\in X$"),
            ("Suppose $n > 0$", "Suppose $n \\ge 0$"),
            (
                "$S_{\\sigma_m}(\\num{m},\\num{n}')$",
                "$\\Obj S_{\\sigma_m}(\\num{m},\\num{n}')$",
            ),
            ("!A(x, y))) \\land {}", "!A(x', y))) \\land {}"),
            ("!A(\\num{l}, \\num{n}))", "!A(\\num{l}', \\num{n}))"),
            ("$!A(m, n)$", "$!A(\\num{m},\\num{n})$"),
        ]
        for old, new in replacements:
            assert audited_verification.count(old) == 1, old
            audited_verification = audited_verification.replace(old, new, 1)
        verification_representation_fixes = (
            mathparts(audited_verification) == target_math
            and checked_target.count("প্রথম থামার সময়") >= 3
            and "BN-SRC-183" in documented
            and source.count("      z)]]]$.)") == 1
            and checked_target.count("অনাবদ্ধ বন্ধনী") == 0
            and set(documented)
            == {f"BN-SRC-{number:03d}" for number in range(180, 188)}
            | {"BN-SRC-197"}
        )
        assert verification_representation_fixes
        tex_command_check = {
            "documented_corrections": [f"BN-SRC-{number:03d}" for number in range(180, 188)]
            + ["BN-SRC-197"],
            "validity_entailment_uses_metavariable_T": True,
            "canonical_structure_runs_machine_M": True,
            "halting_disjunction_witnesses_scoped": True,
            "configuration_induction_includes_halting_time": True,
            "inductive_step_includes_n_zero": True,
            "predicate_object_marker_restored": True,
            "left_move_frame_excludes_written_square": "x-prime",
            "frame_exercise_uses_numerals": True,
            "unmatched_exercise_delimiter_removed": True,
        }
    elif row["unit_id"] == "OLP-0272":
        audited_unsolvability = source
        assert audited_unsolvability.count(r"\concat") == 3
        audited_unsolvability = audited_unsolvability.replace(r"\concat", r"\frown")
        old = "!!a{sentence}~$B$ as input"
        new = "!!a{sentence}~$!B$ as input"
        assert audited_unsolvability.count(old) == 1
        audited_unsolvability = audited_unsolvability.replace(old, new, 1)
        decision_unsolvability_fixes = (
            mathparts(audited_unsolvability) == target_math
            and checked_target.count(r"$E\frown D$") == 3
            and set(documented) == {"BN-SRC-188", "BN-SRC-189"}
        )
        assert decision_unsolvability_fixes
        tex_command_check = {
            "documented_corrections": ["BN-SRC-188", "BN-SRC-189"],
            "machine_combination_symbol": "frown",
            "corrected_machine_combination_occurrences": 3,
            "validity_input_metavariable_marker_restored": True,
        }
    elif row["unit_id"] == "OLP-0273":
        audited_trakhtenbrot = source
        replacements = [
            ("larger of~$k$ and the length", "larger of~$k+1$ and the length"),
            (
                r"\delta(q_0,\TMblank) = \tuple{q,\TMblank,\TMstay}",
                r"\delta(q_0,\TMblank) = \tuple{q_0,\TMblank,\TMstay}",
            ),
            (
                r"\Assign{\prime}{M''}(0) =" + "\n"
                r"    \Assign{\prime}{M'}(1) = 1",
                r"\Assign{\prime}{M''}(0) =" + "\n"
                r"    \Assign{\prime}{M''}(1) = 1",
            ),
            (
                "!A(x, y))) \\land {}",
                "!A(x', y) \\land !B(y'))) \\land {}",
            ),
            ("$n = \\max(k,\\len{w})$", "$n = \\max(k+1,\\len{w})$"),
            (
                r"\Sat{M'}{!T'(M,w) \land E(M,w)}",
                r"\Sat{M'}{!T'(M,w) \land !E(M,w)}",
            ),
            (
                r"\Sat{M'}{!T(M,w) \land E(M,w)}",
                r"\Sat{M'}{!T'(M,w) \land !E(M,w)}",
            ),
            (
                r"model of~$!T(M,w) \land !E(M, w)$",
                r"model of~$!T'(M,w) \land !E(M, w)$",
            ),
        ]
        for old, new in replacements:
            assert audited_trakhtenbrot.count(old) == 1, old
            audited_trakhtenbrot = audited_trakhtenbrot.replace(old, new, 1)
        trakhtenbrot_fixes = (
            mathparts(audited_trakhtenbrot) == target_math
            and checked_target.count(r"\tuple{q_0,\TMblank,\TMstay}") == 2
            and checked_target.count("সব ধনাত্মক~$n\\in\\Nat$-এর জন্য") == 1
            and "কোনো ধনাত্মক সময়~$n$-এর আগে না থামে" in checked_target
            and "ধনাত্মক~$n$-তম ধাপের আগে না থামে" in checked_target
            and set(documented) == {f"BN-SRC-{number:03d}" for number in range(190, 197)}
        )
        assert trakhtenbrot_fixes
        tex_command_check = {
            "documented_corrections": [f"BN-SRC-{number:03d}" for number in range(190, 197)],
            "finite_domain_bound": "max(k+1,len(w))",
            "single_state_transition_target": "q_0",
            "successor_interpretation_structure": "M-double-prime",
            "left_move_frame_excludes_written_square": "x-prime",
            "left_move_adds_fresh_time_condition": True,
            "halting_conjunct_marker_restored": True,
            "exercise_uses_T_prime_and_E_marker": True,
            "contrapositive_model_uses_T_prime": True,
            "fresh_time_condition_scope": "positive times",
        }
    elif row["unit_id"] == "OLP-0278":
        assert overview_math_fix
        tex_command_check = {
            "documented_corrections": ["BN-SRC-201", "BN-SRC-202"],
            "roadmap_order_clarified": True,
            "object_provability_predicate_restored": True,
        }
    elif row["unit_id"] == "OLP-0279":
        assert undecidability_math_fix
        tex_command_check = {
            "documented_correction": "BN-SRC-203",
            "diagonal_family_subscript_restored": True,
            "corrected_subscript_occurrences": 2,
        }
    elif row["unit_id"] == "OLP-0284":
        assert arithmetization_syntax_math_fix, (
            row["unit_id"],
            mathparts(audited_arithmetization_syntax) - target_math,
            target_math - mathparts(audited_arithmetization_syntax),
            documented,
        )
        tex_command_check = {
            "documented_corrections": ["BN-SRC-205", "BN-SRC-206", "BN-SRC-207"],
            "atomic_predicate_argument_count_checked": True,
            "formation_sequence_uses_primitive_recursive_bound": True,
            "sentence_quantifier_scope_repaired": True,
        }
    elif row["unit_id"] == "OLP-0286":
        assert arithmetization_syntax_math_fix, (
            row["unit_id"],
            mathparts(audited_arithmetization_syntax) - target_math,
            target_math - mathparts(audited_arithmetization_syntax),
            documented,
        )
        tex_command_check = {
            "documented_corrections": [f"BN-SRC-{number:03d}" for number in range(208, 213)],
            "initial_sequent_example_parenthesis_repaired": True,
            "end_sequent_function_name_consistent": True,
            "initial_sequent_predicate_name_consistent": True,
            "derivation_code_variable_consistent": True,
            "proof_conclusion_parenthesis_closed": True,
            "proof_sentence_code_variable_is_y": True,
        }
    elif row["unit_id"] == "OLP-0287":
        assert arithmetization_syntax_math_fix, (
            row["unit_id"],
            mathparts(audited_arithmetization_syntax) - target_math,
            target_math - mathparts(audited_arithmetization_syntax),
            documented,
        )
        tex_command_check = {
            "documented_corrections": ["BN-SRC-213", "BN-SRC-214"],
            "immediate_subderivation_index_offset": 1,
            "subsequence_reference_restored": True,
        }
    elif row["unit_id"] == "OLP-0288":
        assert arithmetization_syntax_math_fix, (
            row["unit_id"],
            mathparts(audited_arithmetization_syntax) - target_math,
            target_math - mathparts(audited_arithmetization_syntax),
            documented,
        )
        tex_command_check = {
            "documented_corrections": ["BN-SRC-215", "BN-SRC-216", "BN-SRC-217"],
            "quantifier_rule_preceding_line_index_bounded": True,
            "quantifier_rule_constant_variable_consistent": True,
            "nested_conditional_recursion_calls_helper": True,
        }
    elif row["unit_id"] == "OLP-0291":
        assert representability_q_math_fix and representability_q_control_fix
        assert checked_target.count(r"!!a{formula}~$!A_f(x_0, \dots, x_k, y)$") == 1
        assert checked_target.count(r"$A_f(\num{n_0}, \dots, \num{n_k}, \num{(s)_1})$") == 1
        tex_command_check = {
            "documented_corrections": ["BN-SRC-218", "BN-SRC-219"],
            "representing_formula_subscript_consistent": True,
            "computed_value_embedded_as_numeral": True,
        }
    elif row["unit_id"] == "OLP-0293":
        assert representability_q_math_fix and representability_q_control_fix
        assert checked_target.count(r"$h(\vec x,y)$") == 1
        assert checked_target.count(
            r"\bforall{i <" + "\n" + r"  y}{\beta(d,i+1) = g(\vec x, i,\beta(d,i))})}."
        ) == 1
        tex_command_check = {
            "documented_corrections": ["BN-SRC-220", "BN-SRC-221"],
            "primitive_recursion_signature_consistent": True,
            "minimization_condition_parenthesis_closed": True,
        }
    elif row["unit_id"] == "OLP-0294":
        assert representability_q_math_fix and representability_q_control_fix
        assert checked_target.count(r"0 & \text{অন্যথায়}") == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-233",
            "cases_fallback_is_text": True,
        }
    elif row["unit_id"] == "OLP-0295":
        assert representability_q_math_fix and representability_q_control_fix
        assert checked_target.count(r"\lexists[y_0][\dots \lexists[y_{k-1}][") == 1
        assert checked_target.count(r"\olref[inc][req][cmp]{prop:rep1}") == 1
        assert checked_target.count(r"\olref[inc][req][cmp]{prop:rep2}") == 1
        tex_command_check = {
            "documented_corrections": ["BN-SRC-222", "BN-SRC-223"],
            "composition_existentials_balanced": True,
            "exercise_references_both_guiding_propositions": True,
        }
    elif row["unit_id"] == "OLP-0296":
        assert representability_q_math_fix and representability_q_control_fix
        assert checked_target.count(
            r"\Th{Q} & \Proves \eq[(a' + \num n)'][(a + \num n')'] \quad"
        ) == 1
        assert checked_target.count(
            r"\Th{Q} & \Proves \eq[(a' + \num n')][(a + \num n')'] \quad"
        ) == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-224",
            "successor_addition_induction_not_circular": True,
        }
    elif row["unit_id"] == "OLP-0297":
        assert representability_q_math_fix and representability_q_control_fix
        assert "যে সঙ্গতিপূর্ণ !!{derivation} পদ্ধতিতে" in checked_target
        assert "সঙ্গতিপূর্ণ স্বতঃসিদ্ধায়িত তত্ত্বের" in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-225",
            "general_representation_claim_requires_consistency": True,
        }
    elif row["unit_id"] == "OLP-0300":
        assert representability_q_math_fix and representability_q_control_fix, (
            mathparts(audited_representability_q) - target_math,
            target_math - mathparts(audited_representability_q),
            controls(audited_representability_q) - controls(checked_target),
            controls(checked_target) - controls(audited_representability_q),
        )
        assert checked_target.count(r"\olfileid{inc}{req}{s1c}") == 1
        assert checked_target.count(r"$!Q_2$-এর মাধ্যমে বিরোধ দেয়") == 2
        assert "শূন্যপদী সংযোজন" in checked_target
        tex_command_check = {
            "documented_corrections": [
                "BN-SRC-226",
                "BN-SRC-227",
                "BN-SRC-228",
                "BN-SRC-229",
                "BN-SRC-230",
                "BN-SRC-231",
                "BN-SRC-232",
            ],
            "chapter_identifier_consistent": True,
            "second_term_value_uses_m": True,
            "less_than_witness_addend_order_matches_q8": True,
            "successor_zero_contradictions_use_q2": True,
            "empty_universal_expansion_is_conjunction": True,
            "bounded_existential_scope_braced": True,
            "sigma1_existential_macro_well_formed": True,
        }
    elif row["unit_id"] == "OLP-0303":
        assert theories_computability_math_fix
        assert checked_target.count(
            r"\Th{Q} \Proves \lnot !A_T(\num x, \num x, \num n)"
        ) == 1
        assert checked_target.count(
            r"\lexists[s][!A_T(\num x,\num x,s)]"
        ) == 2
        assert checked_target.count(
            r"\lexists[s][!A_T(\num x,"
        ) >= 2
        tex_command_check = {
            "documented_corrections": ["BN-SRC-234", "BN-SRC-235"],
            "reverse_direction_uses_standard_model_soundness": True,
            "reduction_sentence_uses_representing_formula": True,
        }
    elif row["unit_id"] == "OLP-0305":
        assert theories_computability_math_fix
        assert checked_target.count(r"S(n)") == 2
        assert r"S(\num n) &" not in checked_target
        assert r"\lnot S(\num n) &" not in checked_target
        assert checked_target.count(r"\Setabs{!A}{\Sat{N}{!A}}") == 1
        tex_command_check = {
            "documented_corrections": ["BN-SRC-236", "BN-SRC-237"],
            "meta_relation_takes_number_argument": True,
            "true_arithmetic_uses_standard_structure": True,
        }
    elif row["unit_id"] == "OLP-0306":
        assert theories_computability_math_fix
        assert "হলে তা শনাক্ত করতে স্বতঃসিদ্ধগুলি থেকে" in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-238",
            "unbounded_search_is_positive_recognizer": True,
        }
    elif row["unit_id"] == "OLP-0307":
        assert theories_computability_math_fix
        assert checked_target.count("স্বতঃসিদ্ধসমষ্টি~$A$ থেকে") == 1
        assert checked_target.count("$A$ থেকে") >= 2
        tex_command_check = {
            "documented_correction": "BN-SRC-239",
            "parallel_proof_search_uses_computable_axiom_set": True,
        }
    elif row["unit_id"] == "OLP-0308":
        assert theories_computability_math_fix and theories_computability_token_fix
        assert checked_target.count("!!{axiomatized}") == 0
        assert checked_target.count("!!{axiomatizable}") >= 2
        tex_command_check = {
            "documented_correction": "BN-SRC-240",
            "lemma_hypothesis_uses_axiomatizable": True,
        }
    elif row["unit_id"] == "OLP-0309":
        assert theories_computability_math_fix
        assert checked_target.count(r"S(n)") == 2
        assert r"S(\num n) &" not in checked_target
        assert r"\lnot S(\num n) &" not in checked_target
        assert checked_target.count(r"R(\Gn{!D_S(u)},y)") == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-241",
            "meta_relation_takes_number_argument": True,
            "universal_relation_uses_formula_code": True,
        }
    elif row["unit_id"] == "OLP-0311":
        assert theories_computability_math_fix
        assert "$\\Th{ZFC}$-এর কোনো সঙ্গতিপূর্ণ নির্ণেয় প্রসারণ নেই" in checked_target
        assert checked_target.count("মানক মডেলে সত্য") >= 3
        tex_command_check = {
            "documented_corrections": ["BN-SRC-242", "BN-SRC-243"],
            "zfc_corollary_requires_consistent_extension": True,
            "presburger_truth_is_in_standard_model": True,
        }
    elif row["unit_id"] == "OLP-0316":
        assert incompleteness_provability_math_fix
        assert r"\ORProv_T(y)" not in checked_target
        assert r"$T$" not in checked_target
        tex_command_check = {
            "documented_corrections": ["BN-SRC-250", "BN-SRC-251"],
            "rosser_predicate_theory_index_normalized": True,
            "derivation_source_theory_macro_restored": True,
        }
    elif row["unit_id"] == "OLP-0318":
        assert incompleteness_provability_math_fix
        assert checked_target.count(
            r"\lexists[x][\OPrf[\Th{PA}](x,y)]"
        ) == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-244",
            "object_language_provability_definition_restored": True,
        }
    elif row["unit_id"] == "OLP-0319":
        assert (
            incompleteness_provability_math_fix
            and incompleteness_provability_token_fix
        )
        assert r"\Prov[\Th{PA}]" not in checked_target
        assert r"\gn{G}" not in checked_target
        assert "!!{axiomatized}" not in checked_target
        assert checked_target.count(r"\OCon[\Th{T}]") == 1
        tex_command_check = {
            "documented_corrections": [
                "BN-SRC-245",
                "BN-SRC-246",
                "BN-SRC-247",
                "BN-SRC-248",
            ],
            "object_language_provability_macro_restored": True,
            "godel_sentence_marker_restored": True,
            "axiomatizable_classification_restored": True,
            "theory_macro_in_consistency_statement_restored": True,
        }
    elif row["unit_id"] == "OLP-0320":
        assert incompleteness_provability_math_fix
        assert checked_target.count(r"\Th{T} \Proves") >= 6
        assert r"T \Proves" not in checked_target
        assert "$\\Th{T}$ সঙ্গতিপূর্ণ হলে এটি" in checked_target
        tex_command_check = {
            "documented_corrections": ["BN-SRC-249", "BN-SRC-252"],
            "exercise_theory_macro_normalized": True,
            "godel_sentence_unprovability_requires_consistency": True,
        }
    elif row["unit_id"] == "OLP-0324":
        assert second_order_syntax_semantics_math_fix
        assert r"\Obj{V^1_0}(\Obj v_0)" not in checked_target
        assert r"\Obj{V^1_0}(v_0)" not in checked_target
        assert checked_target.count(r"\Obj{V^1_0}(\Obj{v_0})") >= 4
        tex_command_check = {
            "documented_correction": "BN-SRC-253",
            "object_variable_notation_normalized": True,
        }
    elif row["unit_id"] == "OLP-0329":
        assert second_order_syntax_semantics_math_fix
        assert re.search(
            r"সসীম\s+তালিকার শেষ উপাদানকে নিজের কাছেই পাঠাও",
            checked_target,
        )
        tex_command_check = {
            "documented_correction": "BN-SRC-254",
            "finite_enumeration_terminal_case_restored": True,
        }
    elif row["unit_id"] == "OLP-0332":
        assert second_order_metatheory_math_fix
        assert r"\lforall[w][u(x')=u" not in checked_target
        assert r"\lforall[w][u(w')=u" in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-255",
            "addition_recursion_binder_restored": True,
        }
    elif row["unit_id"] == "OLP-0333":
        assert second_order_metatheory_math_fix
        assert r"$\Sat{M}{!P \lif !A}$" in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-256",
            "satisfaction_expression_balanced": True,
        }
    elif row["unit_id"] == "OLP-0334":
        assert second_order_metatheory_math_fix
        assert second_order_metatheory_control_fix
        assert r"\ollabel{thm:sol-not-compact}" in checked_target
        assert r"!A^{\ge k} \in \Gamma_0" in checked_target
        assert r"!A^{\ge n} \in \Gamma_0" in checked_target
        tex_command_check = {
            "documented_corrections": ["BN-SRC-257", "BN-SRC-258"],
            "compactness_theorem_label_unique": True,
            "finite_fragment_indices_scoped": True,
            "empty_finite_fragment_case_supplied": True,
        }
    elif row["unit_id"] == "OLP-0338":
        assert second_order_set_theory_math_fix
        restricted = r"X(x) \land X(y) \land"
        assert checked_target.count(restricted) == 2
        tex_command_check = {
            "documented_corrections": ["BN-SRC-259", "BN-SRC-260"],
            "comparison_injectivity_restricted_to_X": True,
            "equinumerosity_injectivity_restricted_to_X": True,
        }
    elif row["unit_id"] == "OLP-0339":
        assert second_order_set_theory_math_fix
        assert r"X(x) \lif X(u(x))" in checked_target
        assert r"\lnot\lexists[x][X(x)] \lor" in checked_target
        assert r"Y \subseteq X \land Y(z)" in checked_target
        assert r"\fn{Aleph_1}(X) \ident \fn{Inf}(X) \land" in checked_target
        tex_command_check = {
            "documented_corrections": ["BN-SRC-261", "BN-SRC-262", "BN-SRC-263"],
            "infinite_subset_endomap_restricted": True,
            "empty_enumerable_subset_case_included": True,
            "enumeration_minimality_restricted_to_X": True,
            "aleph_one_requires_infinite_X": True,
        }
    elif row["unit_id"] == "OLP-0340":
        assert second_order_set_theory_math_fix
        assert "$s(X)$-এর" in checked_target
        assert r"\fn{Cont}(Y) \land" in checked_target
        assert r"\lforall[x][Y(u(x))]" in checked_target
        assert norm(
            r"\lforall[x][\lforall[y][((Y(x) \land Y(y) \land "
            r"\eq[u(x)][u(y)]) \lif \eq[x][y])]]"
        ) in norm(checked_target)
        tex_command_check = {
            "documented_corrections": ["BN-SRC-264", "BN-SRC-265", "BN-SRC-266"],
            "continuum_proof_base_set_restored": True,
            "domain_continuum_bijection_complete": True,
            "cantor_injectivity_restricted_to_Y": True,
        }
    elif row["unit_id"] == "OLP-0347":
        assert lambda_introduction_completion_math_fix
        assert r"\Subst{\Subst{P}{M_1}{x_1}\ldots}{M_n}{x_n}" not in checked_target
        assert checked_target.count(
            r"\Subst{\Subst{N}{M_1}{x_1}\ldots}{M_n}{x_n}"
        ) == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-267",
            "curried_body_symbol_restored": True,
        }
    elif row["unit_id"] == "OLP-0348":
        assert lambda_introduction_completion_math_fix
        assert r"f(x_0, \dots, x_{k-1})$ একটি $k$-স্থানীয়" in checked_target
        assert r"F, \num{n_0}" not in checked_target
        assert checked_target.count(r"F\, \num{n_0}") == 2
        tex_command_check = {
            "documented_corrections": ["BN-SRC-268", "BN-SRC-269"],
            "lambda_definition_arity_index_restored": True,
            "undefined_case_application_separator_restored": True,
        }
    elif row["unit_id"] == "OLP-0349":
        assert lambda_introduction_completion_math_fix
        assert r"X \num m_0" not in checked_target
        assert checked_target.count(r"X \num{m_0} \ldots \num{m_{n-1}}") == 1
        assert checked_target.count(r"X \num{m_0} \dots \num{m_{n-1}}") == 1
        tex_command_check = {
            "documented_correction": "BN-SRC-270",
            "church_numeral_macro_arguments_braced": True,
        }
    elif row["unit_id"] == "OLP-0353":
        assert lambda_introduction_completion_math_fix
        assert r"f(x+1, \vec z) & = h(x, f(x,\vec z), \vec z)." in checked_target
        assert r"F(\num{0}, \vec z) & \equiv G'(\vec z)" in checked_target
        assert r"F(\overline{n+1}, \vec z) & \equiv H'(\num{n}, F(\num{n}, \vec z), \vec z)" in checked_target
        assert r"H(u,v) & = \lambd[\vec z][H'(u,v(\vec z),\vec z)]." in checked_target
        tex_command_check = {
            "documented_corrections": ["BN-SRC-271", "BN-SRC-272", "BN-SRC-273"],
            "primitive_recursion_term_roles_restored": True,
            "recursion_index_restored": True,
            "curried_recursive_value_application_restored": True,
        }
    elif row["unit_id"] == "OLP-0354":
        assert lambda_introduction_completion_math_fix
        assert all(
            phrase in checked_target
            for phrase in ("স্থির-বিন্দু সমাবেশক", "কারির সমাবেশক", "টুরিংয়ের সমাবেশক")
        )
        tex_command_check = {
            "fixed_point_combinator_terms_reviewed": True,
            "curry_and_turing_forms_distinguished": True,
        }
    elif row["unit_id"] == "OLP-0355":
        assert lambda_introduction_completion_math_fix
        assert "যেহেতু $f$ ল্যাম্বডা-সংজ্ঞেয়" in checked_target
        assert "যেহেতু $f$ আদিম পুনরাবৃত্ত" not in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-274",
            "lemma_premise_used_without_extra_primitive_recursive_assumption": True,
        }
    elif row["unit_id"] == "OLP-0356":
        assert lambda_syntax_foundations_math_fix
        assert r"\olchapter{lam}{syn}{বাক্যগঠন}" in checked_target
        assert checked_target.count(r"\olimport{") == 10
        tex_command_check = {
            "syntax_chapter_title_reviewed": True,
            "all_ten_source_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0357":
        assert lambda_syntax_foundations_math_fix
        assert r"$\Obj{v_0}$, $\Obj{v_1}$" in checked_target
        assert all(
            phrase in checked_target
            for phrase in ("আরোহীভাবে", "বিমূর্তনের", "প্রয়োগের", "পূর্ণ-বন্ধনীযুক্ত")
        )
        tex_command_check = {
            "term_formation_vocabulary_reviewed": True,
            "object_variable_macros_preserved": True,
        }
    elif row["unit_id"] == "OLP-0358":
        assert lambda_syntax_foundations_math_fix
        assert all(
            phrase in checked_target
            for phrase in ("একক পাঠযোগ্যতা", "গঠনপ্রণালী", "প্রকৃত পূর্বাংশ")
        )
        tex_command_check = {
            "unique_readability_vocabulary_reviewed": True,
            "unique_formation_argument_symbols_preserved": True,
        }
    elif row["unit_id"] == "OLP-0359":
        assert lambda_syntax_foundations_math_fix
        assert all(
            phrase in checked_target
            for phrase in ("সংক্ষিপ্ত পদ", "বাঁ থেকে ডান দিকে", "সর্বাধিক বিস্তৃত")
        )
        tex_command_check = {
            "abbreviation_conventions_reviewed": True,
            "application_associativity_and_scope_preserved": True,
        }
    elif row["unit_id"] == "OLP-0360":
        assert lambda_syntax_foundations_math_fix
        assert "BN-SRC-275" in documented
        assert (
            "কোনো পদ~$N$-এর ভিতরে $\\lambd[x][M]$ ঘটলে~$M$-এর সংশ্লিষ্ট সংঘটনটিই"
            in checked_target
        )
        assert all(
            phrase in checked_target
            for phrase in ("পরিসর", "মুক্ত ও বদ্ধ সংঘটন", "পরিবেশের", "বদ্ধ পদ, সমাবেশক")
        )
        tex_command_check = {
            "documented_correction": "BN-SRC-275",
            "lambda_scope_is_abstraction_body": True,
            "free_bound_environment_vocabulary_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0361":
        assert lambda_syntax_foundations_math_fix
        assert set(documented) == {"BN-SRC-276", "BN-SRC-277", "BN-SRC-282", "BN-SRC-283"}
        assert r"\Subst{(\lambd[x][P])}{N}{x} = \lambd[x][P]" in checked_target
        assert all(
            phrase in checked_target
            for phrase in ("প্রতিস্থাপন", "অসংজ্ঞায়িত", "আরোহ-অনুমান", "মুক্ত চলরাশি")
        )
        tex_command_check = {
            "documented_corrections": documented,
            "capture_avoiding_substitution_reviewed": True,
            "shadowing_clause_restored": True,
            "free_variable_theorems_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0362":
        assert lambda_syntax_foundations_math_fix
        assert set(documented) == {"BN-SRC-278", "BN-SRC-279", "BN-SRC-280", "BN-SRC-281", "BN-SRC-284"}
        assert r"$R'' \aeq R$" in checked_target
        assert all(
            phrase in checked_target
            for phrase in ("বদ্ধ চলরাশির পরিবর্তন", "সামঞ্জস্যশীল", "প্রতিবিম্ব ধর্ম", "তুল্যতা সম্পর্ক")
        )
        tex_command_check = {
            "documented_corrections": documented,
            "alpha_conversion_relations_reviewed": True,
            "substitution_modulo_alpha_reviewed": True,
            "free_variable_notation_normalized": True,
        }
    elif row["unit_id"] == "OLP-0363":
        assert lambda_syntax_foundations_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in ("দ্য ব্রুইন সূচক", "শূন্য থেকে সূচকিত", r"F_\Gamma", r"G_\Gamma")
        )
        tex_command_check = {
            "de_bruijn_index_vocabulary_reviewed": True,
            "forward_and_inverse_translations_preserved": True,
            "alpha_invariance_proposition_preserved": True,
        }
    elif row["unit_id"] == "OLP-0364":
        assert lambda_syntax_foundations_math_fix
        assert set(documented) == {"BN-SRC-285", "BN-SRC-286", "BN-SRC-287", "BN-SRC-288"}
        assert all(
            phrase in checked_target
            for phrase in ("সমতুল্যতা-শ্রেণি", "প্রতিনিধি", r"\Lambda$-পদ", "প্রক্ষেপণ")
        )
        assert r"$\FV{\rep{M}[0]} = \FV{\rep{M}[1]}$" in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "alpha_equivalence_class_operations_reviewed": True,
            "class_valued_substitution_repaired": True,
            "free_variable_notation_normalized": True,
        }
    elif row["unit_id"] == "OLP-0365":
        assert lambda_syntax_foundations_math_fix and lambda_syntax_control_fix
        assert set(documented) == {"BN-SRC-289"}
        assert r"\olfileid{lam}{syn}{bet}" in checked_target
        assert all(
            phrase in checked_target
            for phrase in (r"$\beta$-সংকোচন", "রিডেক্স", "স্বাভাবিক রূপ", "স্বাভাবিক কৌশল", r"$\beta$-সমতুল্যতা")
        )
        tex_command_check = {
            "documented_correction": "BN-SRC-289",
            "syntax_file_identity_restored": True,
            "beta_reduction_and_equivalence_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0366":
        assert lambda_syntax_foundations_math_fix
        assert set(documented) == {"BN-SRC-290", "BN-SRC-291"}
        assert r"\lambd[x][M x] \equal M \text{ যদি } x \notin \FV{M}" in checked_target
        assert all(
            phrase in checked_target
            for phrase in (r"$\eta$-সংকোচন", r"$\beta\eta$-হ্রাস", r"$\eta$-সমতুল্যতা", "ব্যাপ্তিগততা")
        )
        tex_command_check = {
            "documented_corrections": documented,
            "eta_conversion_schema_and_freshness_restored": True,
            "extensionality_notation_normalized": True,
        }
    elif row["unit_id"] == "OLP-0367":
        assert lambda_church_rosser_math_fix
        assert not documented
        assert r"\olchapter{lam}{cr}{চার্চ--রসার ধর্ম}" in checked_target
        assert checked_target.count(r"\olimport{") == 5
        tex_command_check = {
            "church_rosser_chapter_title_reviewed": True,
            "all_five_source_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0368":
        assert lambda_church_rosser_math_fix
        assert set(documented) == {"BN-SRC-292"}
        assert all(phrase in checked_target for phrase in ("চার্চ--রসার ধর্ম", "হ্রাসযোগ্যতা-সম্বন্ধ", "তুচ্ছ হ্রাস", "চূড়ান্ত ফল"))
        assert r"P_m \, (=P)" in checked_target and r"Q_n \, (=Q)" in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-292",
            "church_rosser_grid_argument_reviewed": True,
            "transitive_closure_endpoints_identified": True,
        }
    elif row["unit_id"] == "OLP-0369":
        assert lambda_church_rosser_math_fix
        assert set(documented) == {"BN-SRC-293", "BN-SRC-294"}
        assert all(phrase in checked_target for phrase in (r"সমান্তরাল $\beta$-হ্রাস", r"$\beta$-পূর্ণ বিকাশ", "আরোহ-অনুমান", "চার্চ--রসার ধর্ম"))
        assert r"$N \bredpar N'$" in checked_target
        assert r"\lambd[x][\Subst{N'}{R'}{y}]" in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "parallel_beta_rules_reviewed": True,
            "complete_development_argument_reviewed": True,
            "substitution_replacement_prime_restored": True,
        }
    elif row["unit_id"] == "OLP-0370":
        assert lambda_church_rosser_math_fix
        assert set(documented) == {"BN-SRC-295", "BN-SRC-296"}
        assert all(
            phrase in checked_target
            for phrase in (r"$\beta$-হ্রাস", "ব্যুৎপত্তির উপর আরোহ", "ক্ষুদ্রতম পরিযায়ী সম্বন্ধ", "চার্চ--রসার ধর্ম")
        )
        assert "$N$, $N'$," in checked_target
        assert "$Q$, $Q'$-এর জন্য" in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "compatible_beta_contraction_cases_restored": True,
            "parallel_and_ordinary_beta_equivalence_reviewed": True,
            "missing_reduced_body_metavariable_restored": True,
        }
    elif row["unit_id"] == "OLP-0371":
        assert lambda_church_rosser_math_fix
        assert set(documented) == {"BN-SRC-297", "BN-SRC-298", "BN-SRC-299", "BN-SRC-303", "BN-SRC-304"}
        assert all(
            phrase in checked_target
            for phrase in (r"সমান্তরাল $\beta\eta$-হ্রাস", r"$\beta\eta$-পূর্ণ বিকাশ", "অধিক বিশেষ চতুর্থ ও পঞ্চম ধারা", "চার্চ--রসার ধর্ম")
        )
        assert r"$N \beredpar N'$" in checked_target
        assert checked_target.count(r"\FV{N}") == 4
        assert "কোনো $x$, $N$ ও~$N'$-এর জন্য" in checked_target
        assert "আলফা-অভিন্ন তাজা প্রতিনিধি" in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "parallel_beta_eta_abstraction_rule_restored": True,
            "free_variable_notation_normalized": True,
            "complete_development_priority_and_overlap_case_restored": True,
            "missing_eta_body_witness_restored": True,
            "capture_avoiding_fresh_representative_restored": True,
        }
    elif row["unit_id"] == "OLP-0372":
        assert lambda_church_rosser_math_fix
        assert set(documented) == {"BN-SRC-300", "BN-SRC-301", "BN-SRC-302"}
        assert all(
            phrase in checked_target
            for phrase in (r"$\beta\eta$-হ্রাস", r"$M \eredone M'$", r"$x \notin \FV{N}$", "প্রথম চারটি ক্ষেত্র")
        )
        tex_command_check = {
            "documented_corrections": documented,
            "mixed_one_step_relation_defined_and_eta_symbol_restored": True,
            "free_variable_notation_normalized": True,
            "parallel_to_ordinary_missing_cases_restored": True,
        }
    elif row["unit_id"] == "OLP-0373":
        assert lambda_definability_opening_math_fix
        assert not documented
        assert r"\olchapter{lam}{rep}{ল্যাম্বডা-সংজ্ঞেয়তা}" in checked_target
        assert all(
            phrase in checked_target
            for phrase in (
                r"\olimport{introduction}",
                r"\olimport{arithmetical-functions}",
                r"\olimport{lambda-definable-recursive}",
                r"%\olimport{lists}",
            )
        )
        tex_command_check = {
            "lambda_definability_chapter_title_reviewed": True,
            "all_nine_active_imports_and_commented_lists_import_preserved": True,
        }
    elif row["unit_id"] == "OLP-0374":
        assert lambda_definability_opening_math_fix
        assert set(documented) == {"BN-SRC-305"}
        collapsed_target = re.sub(r"\s+", " ", checked_target)
        assert all(
            phrase in collapsed_target
            for phrase in (
                "চার্চ সংখ্যাপদ",
                "চার্চ--রসার ধর্ম",
                "বহুস্থানীয় ও আংশিক অপেক্ষক",
                "স্বাভাবিক রূপ নেই",
                r"$c_k(n) = k$",
            )
        )
        tex_command_check = {
            "documented_correction": "BN-SRC-305",
            "church_numeral_computation_and_partial_definability_reviewed": True,
            "constant_function_subscript_restored": True,
        }
    elif row["unit_id"] == "OLP-0375":
        assert lambda_definability_opening_math_fix
        assert set(documented) == {"BN-SRC-306"}
        assert all(
            phrase in checked_target
            for phrase in (
                "উত্তরসূরি অপেক্ষক",
                "যোগ",
                "গুণ",
                "সূচক",
                "ক্রমযুগলের সাংকেতিকরণ",
            )
        )
        assert r"\fn{Mult}' \ident \lambd[ab][a (\fn{Add}\, b) \num{0}]." in checked_target
        tex_command_check = {
            "documented_correction": "BN-SRC-306",
            "church_successor_addition_multiplication_exponentiation_reviewed": True,
            "alternate_multiplication_operand_restored": True,
        }
    elif row["unit_id"] == "OLP-0376":
        assert lambda_definability_pairs_truth_pr_math_fix
        assert set(documented) == {"BN-SRC-307"}
        assert all(
            phrase in checked_target
            for phrase in (
                "ক্রমযুগল ও পূর্বসূরি",
                "অভিক্ষেপ অপেক্ষক",
                "ছাঁটা বিয়োগ",
                r"\fn{Pred}",
                r"\fn{Sub}",
            )
        )
        assert checked_target.count(r"\tuple{\num{0}, \num{0}}") == 2
        tex_command_check = {
            "documented_correction": "BN-SRC-307",
            "pair_constructor_projections_predecessor_and_subtraction_reviewed": True,
            "raw_zero_pair_states_restored_as_church_numerals": True,
        }
    elif row["unit_id"] == "OLP-0377":
        assert lambda_definability_pairs_truth_pr_math_fix
        assert set(documented) == {"BN-SRC-308"}
        assert all(
            phrase in checked_target
            for phrase in (
                "সত্যমান ও সম্বন্ধ",
                "নির্বাচক",
                "নঞর্থকরণ ও সংযোজন",
                "অন্তর্ভুক্তিমূলক ও",
                "বর্জনমূলক বিয়োজন",
                r"R \subseteq \Nat^k",
            )
        )
        tex_command_check = {
            "documented_correction": "BN-SRC-308",
            "selector_encoding_relation_definability_and_boolean_functions_reviewed": True,
            "relation_arity_symbol_restored": True,
        }
    elif row["unit_id"] == "OLP-0378":
        assert lambda_definability_pairs_truth_pr_math_fix
        assert set(documented) == {"BN-SRC-309", "BN-SRC-310"}
        assert all(
            phrase in checked_target
            for phrase in (
                "মৌলিক আদিম পুনরাবৃত্ত অপেক্ষক",
                "মিশ্রণ",
                "আদিম পুনরাবৃত্তি",
                "ক্রমযুগল; এর প্রথম",
                "আরোহ-অনুমান থেকে",
                r"$G_{k-1}$",
                r"তাহলে $h$ হলো",
                r"g(x_1, \dots, x_n, y, h(x_1, \dots, x_n, y))",
            )
        )
        assert r"তাহলে $H$ হলো" not in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "basic_functions_composition_and_primitive_recursion_reviewed": True,
            "composition_representer_index_and_conclusion_restored": True,
            "primitive_recursion_step_function_restored": True,
        }
    elif row["unit_id"] == "OLP-0379":
        assert lambda_definability_completion_math_fix
        assert set(documented) == {"BN-SRC-311", "BN-SRC-312"}
        collapsed_target = re.sub(r"\s+", " ", checked_target)
        assert all(
            phrase in collapsed_target
            for phrase in (
                "স্থির-বিন্দুসমূহ",
                r"\fn{Fac} \ident",
                r"Y \ident (\lambd[ux][x(uux)])(\lambd[ux][x(uux)])",
                r"Y_C \ident \lambd[g][(\lambd[x][g(xx)])(\lambd[x][g(xx)])]",
                r"Y_C g \equal[\beta] g(Y_C g)",
                r"Y_C g \bred g(Y_C g)",
            )
        )
        assert r"Yg \equal[\beta] g(Yg)" not in collapsed_target
        assert r"\fn{Mult} \ident \lambd[ab][a (\fn{Add}\, b) \num{0}]" in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "factorial_fixpoints_turing_and_church_combinators_reviewed": True,
            "multiplication_example_operand_and_church_zero_restored": True,
            "church_combinator_comparison_subscript_restored": True,
        }
    elif row["unit_id"] == "OLP-0380":
        assert lambda_definability_completion_math_fix
        assert set(documented) == {"BN-SRC-313", "BN-SRC-314", "BN-SRC-317"}
        collapsed_target = re.sub(r"\s+", " ", checked_target)
        assert all(
            phrase in collapsed_target
            for phrase in (
                "ন্যূনীকরণ",
                r"\umin{y}{f(x_1,\dots,x_k, y) = 0}",
                r"\fn{Search} & \ident",
                r"G & \ident \lambd[\vec x]",
                r"\num{g(n_1, \dots, n_k)}",
            )
        )
        assert r"(g\, f\, \vec{x} (\fn{Succ}\, y))]]" in checked_target
        assert r"    H & \ident" not in checked_target
        tex_command_check = {
            "documented_corrections": documented,
            "regular_minimization_search_and_closure_reviewed": True,
            "minimized_function_and_representer_names_restored": True,
            "recursive_search_application_closed": True,
            "recursive_search_representer_carried": True,
        }
    elif row["unit_id"] == "OLP-0381":
        assert lambda_definability_completion_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                r"আংশিক পুনরাবৃত্ত অপেক্ষকগুলি \usetoken{S}{lambda definable}",
                r"\lambd[x][F (G x)]",
                "স্বাভাবিক রূপহীন",
                "সব আংশিক পুনরাবৃত্ত অপেক্ষক !!{lambda definable}।",
            )
        )
        tex_command_check = {
            "partial_recursive_composition_strictness_issue_reviewed": True,
            "partial_recursive_lambda_definability_theorem_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0382":
        assert lambda_definability_completion_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                r"\usetoken{S}{lambda definable} অপেক্ষকগুলি পুনরাবৃত্ত",
                r"\ollabel{thm:lambda-computable}",
                "পাটিগণিতায়ন",
                r"\fn{normalize}(t)",
                r"\fn{toChurch}",
                r"\fn{fromChurch}",
                r"!!{lambda define}s",
            )
        )
        tex_command_check = {
            "lambda_definable_to_partial_recursive_converse_reviewed": True,
            "godel_coding_normalization_and_church_conversion_outline_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0383":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                r"\olpart{mvl}{বহুমানী যুক্তিবিদ্যা}",
                "বচনমূলক বহুমানী যুক্তিবিদ্যা",
                r"\olimport[syntax-and-semantics]{syntax-and-semantics}",
                r"\olimport[three-valued-logics]{three-valued-logics}",
                r"\olimport[infinite-valued-logics]{infinite-valued-logics}",
                r"\olimport[sequent-calculus]{sequent-calculus}",
            )
        )
        tex_command_check = {
            "many_valued_logic_part_title_reviewed": True,
            "all_four_part_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0384":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert r"\olchapter{mvl}{syn}{সংকেতবিন্যাস ও অর্থতত্ত্ব}" in checked_target
        assert all(
            rf"\olimport{{{name}}}" in checked_target
            for name in (
                "introduction",
                "connectives",
                "formulas",
                "matrices",
                "valuations-sat",
                "semantic-notions",
                "sublogics",
            )
        )
        tex_command_check = {
            "syntax_semantics_chapter_title_reviewed": True,
            "all_seven_chapter_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0385":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "ধ্রুপদি দ্বিমানী যুক্তিবিদ্যার এমন সাধারণীকরণ",
                "সত্যমান-অপেক্ষকধর্মী",
                "মনোনীত মানসমূহ",
                r"\pSat{v}{!A}[\Log L]",
                r"\Gamma \Entails[\Log L] !A",
            )
        )
        tex_command_check = {
            "many_valued_generalization_and_designated_values_reviewed": True,
            "satisfaction_tautology_and_entailment_overview_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0386":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "বচনমূলক ভাষা",
                "স্থানসংখ্যা",
                "$n$-স্থানীয়",
                "গুণন যুক্তিবিদ্যা",
                "নির্ধারিততা অপারেটর",
            )
        )
        tex_command_check = {
            "language_connective_arity_definition_reviewed": True,
            "product_logic_and_determinateness_examples_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0387":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                r"\Frm[L]",
                "আরোহীভাবে সংজ্ঞায়িত",
                r"\star(!A_1, \dots, !A_n)",
                r"\triangle (\Obj p_1",
            )
        )
        tex_command_check = {
            "general_propositional_formula_formation_reviewed": True,
            "product_and_determinateness_formula_examples_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0388":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "ম্যাট্রিক্স",
                r"V \neq \emptyset",
                r"V^+ \subseteq V",
                r"\tf{\star} : V^n \to V",
                r"\ollabel{fig:tf-CL}",
            )
        )
        tex_command_check = {
            "logical_matrix_definition_reviewed": True,
            "classical_matrix_truth_tables_preserved": True,
        }
    elif row["unit_id"] == "OLP-0389":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                r"\pAssign{v} \colon \PVar \to V",
                r"\pValue{v} \colon \Frm[L] \to V",
                r"\pValue{v}(!A)[\Log L] \in V^+",
                r"\pSat/{v}{!A}[\Log L]",
            )
        )
        tex_command_check = {
            "many_valued_valuation_and_evaluation_recursion_reviewed": True,
            "designated_value_satisfaction_definition_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0390":
        assert many_valued_syntax_semantics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "পরিতৃপ্তিযোগ্য",
                "সর্বতঃসত্য",
                "একঘেয়েতা",
                "পরিযায়িতা",
                "অর্থগত নিঃসরণ উপপাদ্য",
                "সবসময় সত্য নয়",
            )
        )
        tex_command_check = {
            "many_valued_semantic_notions_reviewed": True,
            "conditional_dependent_failures_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0391":
        assert many_valued_syntax_semantics_math_fix
        assert set(documented) == {"BN-SRC-315", "BN-SRC-316"}
        assert all(
            phrase in checked_target
            for phrase in (
                "উল্লিখিত চারটি সংযোজক ব্যবহার করে বচনচল থেকে গঠিত",
                "সাধারণ চার-সংযোজক ভাষার সূত্রসমষ্টি ও সূত্রের জন্য",
                r"\pSat{v}{\Gamma}[\Log L]",
                r"\pSat/{v}{!B}[\Log L]",
                r"{\Entails[\Log L]} \subseteq {\Entails[\LogCL]}",
            )
        )
        tex_command_check = {
            "classical_fragment_agreement_induction_reviewed": True,
            "satisfaction_not_entailment_for_countervaluation_restored": True,
            "shared_four_connective_scope_restored": True,
        }
    elif row["unit_id"] == "OLP-0392":
        assert three_valued_logics_math_fix
        assert not documented
        assert "ত্রিমানী যুক্তিবিদ্যা" in checked_target
        assert all(
            f"\\olimport{{{name}}}" in checked_target
            for name in (
                "introduction",
                "lukasiewicz",
                "kleene",
                "goedel",
                "multiple-designation",
            )
        )
        tex_command_check = {
            "three_valued_logics_chapter_title_reviewed": True,
            "all_five_chapter_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0393":
        assert three_valued_logics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in ("আর একটি মান", "যেকোনো সমন্বয়", "উভয়কেই, মনোনীত")
        )
        tex_command_check = {
            "third_truth_value_overview_reviewed": True,
            "truth_function_and_designation_choices_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0394":
        assert three_valued_logics_math_fix
        assert set(documented) == {"BN-SRC-318", "BN-SRC-319", "BN-SRC-323"}
        assert all(
            phrase in checked_target
            for phrase in (
                "ভবিষ্যৎ-আপতিক",
                r"\tf{\land}(\Undef, \False) = \False",
                r"$(\lnot p \land p) \lif q$",
                r"\pValue v(\lnot \Diamond(p \land \lnot p)) = \False",
                "সম্ভাব্যতা ও",
                "আবশ্যিকতার মতো মোডাল পার্থক্য",
            )
        )
        tex_command_check = {
            "lukasiewicz_future_contingent_semantics_reviewed": True,
            "symmetric_false_conjunction_case_restored": True,
            "unmatched_exercise_parenthesis_removed": True,
            "modal_countervaluation_value_restored": True,
            "modal_extension_and_limitation_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0395":
        assert three_valued_logics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "সমান্তরালে মূল্যায়ন",
                "শক্তিশালী ক্লিনি যুক্তিবিদ্যা",
                "দুর্বল ক্লিনি যুক্তিবিদ্যা",
                "বহিঃস্থ নঞর্থকরণ",
            )
        )
        tex_command_check = {
            "strong_and_weak_kleene_computational_semantics_reviewed": True,
            "bochvar_external_connectives_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0396":
        assert three_valued_logics_math_fix
        assert not documented
        assert all(
            phrase in checked_target
            for phrase in (
                "স্বজ্ঞাবাদী যুক্তিবিদ্যা",
                r"\tf{\lnot}(\Undef) = \False",
                r"(p \lif q) \lor (q \lif p)",
            )
        )
        tex_command_check = {
            "three_valued_godel_matrix_reviewed": True,
            "intuitionistic_and_classical_comparisons_reviewed": True,
        }
    elif row["unit_id"] == "OLP-0397":
        assert three_valued_logics_math_fix
        assert set(documented) == {"BN-SRC-320", "BN-SRC-321", "BN-SRC-322"}
        assert all(
            phrase in checked_target
            for phrase in (
                "কূটাভাসের যুক্তিবিদ্যা",
                "অর্থহীনতার যুক্তিবিদ্যা",
                "পরাসঙ্গত",
                r"\pValue v(!C)[\LogKs] = \False",
                r"\pValue v(!C)[\LogKs] = \True",
                r"\tf{\lfalse}=\False",
            )
        )
        tex_command_check = {
            "multiple_designation_logics_reviewed": True,
            "lp_induction_basis_repaired": True,
            "lp_conjunction_induction_variables_restored": True,
            "rm3_falsum_interpretation_restored": True,
        }
    elif row["unit_id"] == "OLP-0398":
        assert infinite_valued_logics_math_fix and not documented
        assert "অসীমমানী যুক্তিবিদ্যাসমূহ" in checked_target
        assert all(f"\\olimport{{{name}}}" in checked_target for name in ("introduction", "lukasiewicz", "goedel"))
        tex_command_check = {"infinite_valued_logics_chapter_driver_reviewed": True}
    elif row["unit_id"] == "OLP-0399":
        assert infinite_valued_logics_math_fix
        assert set(documented) == {"BN-SRC-324", "BN-SRC-325"}
        assert all(phrase in checked_target for phrase in (
            r"0<m \text{ and } n\le m", r"n\le m-1", "সমান ব্যবধানে", "ফাজি",
        ))
        tex_command_check = {
            "rational_unit_interval_and_designation_reviewed": True,
            "nonzero_denominator_restored": True,
            "m_value_cardinality_restored": True,
        }
    elif row["unit_id"] == "OLP-0400":
        assert infinite_valued_logics_math_fix
        assert set(documented) == {"BN-SRC-327"}
        assert all(phrase in checked_target for phrase in (
            "অসীমমানী \\L ukasiewicz", r"\min(1,1-(x-y))", "সসীম $\\Gamma$-এর ক্ষেত্রে এর বিপরীত দাবিটিও সত্য",
        ))
        tex_command_check = {
            "infinite_lukasiewicz_matrix_and_finite_restrictions_reviewed": True,
            "converse_restricted_to_finite_premises": True,
        }
    elif row["unit_id"] == "OLP-0401":
        assert infinite_valued_logics_math_fix
        assert set(documented) == {"BN-SRC-326", "BN-SRC-328"}
        assert all(phrase in checked_target for phrase in (
            "অসীমমানী G\\\"odel", r"\tf{\lnot}[\LogGod](x)",
            "G\\\"odel--Dummett", "স্বজ্ঞাবাদীভাবে সিদ্ধ নয়",
            "সসীম $\\Gamma$-এর ক্ষেত্রে এর বিপরীত দাবিটিও সত্য",
        ))
        tex_command_check = {
            "infinite_godel_matrix_and_linearity_reviewed": True,
            "nested_math_delimiters_removed": True,
            "converse_restricted_to_finite_premises": True,
        }
    elif row["unit_id"] == "OLP-0402":
        assert many_valued_sequent_calculus_math_fix and not documented
        assert r"\olchapter{mvl}{seq}{সিকোয়েন্ট কলন}" in checked_target
        assert all(f"\\olimport{{{name}}}" in checked_target for name in (
            "introduction", "rules-and-proofs", "structural-rules", "propositional-rules",
        ))
        tex_command_check = {
            "many_valued_sequent_chapter_title_reviewed": True,
            "all_four_chapter_imports_preserved": True,
        }
    elif row["unit_id"] == "OLP-0403":
        assert many_valued_sequent_calculus_math_fix
        assert set(documented) == {"BN-SRC-329", "BN-SRC-330"}
        assert all(phrase in checked_target for phrase in (
            "সসীমসংখ্যক", "উভমুখী শর্ত", r"!A_1, \dots, !A_m",
            r"\pValue{v}(!A) = \False", "প্রতি সত্যমানের জন্য",
        ))
        tex_command_check = {
            "classical_to_n_sided_semantic_construction_reviewed": True,
            "antecedent_index_restored": True,
            "valuation_argument_restored": True,
        }
    elif row["unit_id"] == "OLP-0404":
        assert many_valued_sequent_calculus_math_fix
        assert set(documented) == {"BN-SRC-331"}
        assert all(phrase in checked_target for phrase in (
            "প্রারম্ভিক সিকোয়েন্ট", "মনোনীত সত্যমান", r"\Gamma_i",
            r"\Gamma_0 \subseteq \Gamma", "অনুমান-বিধি",
        ))
        tex_command_check = {
            "n_sided_sequent_initial_theorem_derivability_definitions_reviewed": True,
            "generic_position_index_restored": True,
        }
    elif row["unit_id"] == "OLP-0405":
        assert many_valued_sequent_calculus_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            "গঠনগত বিধি", "দ্বৈত অনুমান-রেখা", r"\iR{\Cut}{i,j}",
        ))
        tex_command_check = {
            "all_positionwise_structural_rules_reviewed": True,
            "distinct_position_cut_preserved": True,
        }
    elif row["unit_id"] == "OLP-0406":
        assert many_valued_sequent_calculus_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            "নির্বাচিত যুক্তিবিদ্যার বচনগত বিধি", "শক্তিশালী ক্লিনি",
            r"\begin{sidewaysfigure}", r"\caption{$\LogLuk[3]$-এ !!{derivation}-এর উদাহরণ}",
        ))
        tex_command_check = {
            "negation_conjunction_disjunction_implication_rule_families_reviewed": True,
            "example_derivation_and_caption_preserved": True,
        }
    elif row["unit_id"] == "OLP-0407":
        assert normal_modal_opening_math_fix
        assert r"\olpart{nml}{স্বাভাবিক মোডাল যুক্তিবিদ্যা}" in checked_target
        assert all(rf"\olimport[{name}]{{{name}}}" in checked_target for name in (
            "syntax-and-semantics", "frame-definability", "axioms-systems",
            "completeness", "filtrations", "tableaux", "sequent-calculus",
        ))
        tex_command_check = {"normal_modal_part_title_and_all_seven_imports_reviewed": True}
    elif row["unit_id"] == "OLP-0408":
        assert normal_modal_opening_math_fix
        assert r"\olchapter{nml}{syn}{সংকেতবিন্যাস ও অর্থতত্ত্ব}" in checked_target
        assert all(rf"\olimport{{{name}}}" in checked_target for name in (
            "introduction", "language-modal-logic", "substitution", "relational-models",
            "truth-at-w", "truth-in-model", "modal-validity", "tautological-instances",
            "schemas", "entailment",
        ))
        tex_command_check = {"syntax_semantics_title_and_ten_imports_reviewed": True}
    elif row["unit_id"] == "OLP-0409":
        assert normal_modal_opening_math_fix
        assert all(phrase in checked_target for phrase in (
            "আবশ্যিকভাবে সম্ভব", "কার্নাপ", "ক্রিপকে", "অভিগম্যতা",
            "অনুরূপতা তত্ত্ব", r"\Ax{D}", r"\Ax{T}", r"\Ax{B}", r"\Ax{4}", r"\Ax{5}",
        ))
        tex_command_check = {"modal_history_kripke_accessibility_and_correspondence_reviewed": True}
    elif row["unit_id"] == "OLP-0410":
        assert normal_modal_opening_math_fix
        assert set(documented) == {"BN-SRC-332"}
        assert all(phrase in checked_target for phrase in (
            "মৌলিক মোডাল যুক্তিবিদ্যার ভাষা", r"\tagitem{prvBox}",
            r"\tagitem{prvDiamond}", r"\iftag{prvOr}{$\lnot !A \lor !B$}",
        ))
        tex_command_check = {"modal_language_formation_and_connective_definitions_reviewed": True}
    elif row["unit_id"] == "OLP-0411":
        assert normal_modal_opening_math_fix
        assert set(documented) == {"BN-SRC-333", "BN-SRC-334"}
        assert all(phrase in checked_target for phrase in (
            "যুগপৎ প্রতিস্থাপন", r"\tagitem{prvIff}{\indcase{!A}{(!B \liff",
            r"\tagitem{prvBox}{\indcase{!A}{\Box !B}",
            "পর্যায়ক্রমিক প্রতিস্থাপনের", r"\Subst{(\Subst{!A}{!D_2}{p_2})}{!D_1}{p_1}",
        ))
        tex_command_check = {"simultaneous_substitution_cases_and_iterated_counterexamples_reviewed": True}
    elif row["unit_id"] == "OLP-0412":
        assert normal_modal_opening_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\mModel{M}", r"\tuple{W, R, V}", r"\olref{fig:simple}",
            r"\caption{একটি সরল মডেল।}",
        ))
        tex_command_check = {"relational_model_world_relation_valuation_and_diagram_reviewed": True}
    elif row["unit_id"] == "OLP-0413":
        assert normal_modal_completion_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\tagitem{prvBox}{\ollabel{defn:sub:mmodels-box}",
            r"\tagitem{prvDiamond}{\ollabel{defn:sub:mmodels-diamond}",
            r"\mSat/{M}{\Box\lnot !A}[w]",
            "শূন্যতাবশে", "প্রতিবিম্বী",
        ))
        tex_command_check = {"pointwise_modal_clauses_duality_and_exercises_reviewed": True}
    elif row["unit_id"] == "OLP-0414":
        assert normal_modal_completion_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\ollabel{prop:truthfacts}", r"\mSat{M}{!A \lif !B}",
            "প্রত্যেক জগতে", r"\draw[reflexive above]",
        ))
        tex_command_check = {"global_model_truth_counterexamples_and_three_world_exercise_reviewed": True}
    elif row["unit_id"] == "OLP-0415":
        assert normal_modal_completion_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\mClass{C} \Entails !A", r"\Entails \Box!A",
            "প্রতিবিম্বী মডেলের শ্রেণিতে",
        ))
        tex_command_check = {"class_relative_validity_and_necessitation_reviewed": True}
    elif row["unit_id"] == "OLP-0416":
        assert normal_modal_completion_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\tagitem{prvNot}{\indcase{!A}{\lnot !B}",
            r"\pSat{v}{!B \liff !C} \Leftrightarrow",
            r"\mSat{M}{}[w]$-এর সংজ্ঞা",
            r"\olref{lem:valid-taut}",
        ))
        tex_command_check = {"tautological_instance_induction_all_constructor_cases_reviewed": True}
    elif row["unit_id"] == "OLP-0417":
        assert normal_modal_completion_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\Ax{K}", r"\Dual{}", r"\ollabel{prop:valid-instances}",
            r"\caption{বৈধ ও অবৈধ স্কিমা।}",
        ))
        tex_command_check = {"schema_characteristic_formula_validity_and_table_reviewed": True}
    elif row["unit_id"] == "OLP-0418":
        assert normal_modal_completion_math_fix
        assert all(phrase in checked_target for phrase in (
            r"p \lif \Diamond p \Entails \Box\lnot p \lif \lnot p",
            r"\mModel{M'} = \tuple{W', R', V'}",
            r"\Entails/ \Box p \lif p$-এর বিপরীত উদাহরণ",
        ))
        tex_command_check = {"pointwise_entailment_positive_example_and_both_countermodels_reviewed": True}
    elif row["unit_id"] == "OLP-0419":
        assert frame_definability_math_fix and not documented
        assert r"\olchapter{nml}{frd}{কাঠামো-সংজ্ঞায়নযোগ্যতা}" in checked_target
        assert all(r"\olimport{" + name + "}" in checked_target for name in (
            "introduction", "properties-accessibility", "frames", "definability",
            "first-order-definability", "equivalence-S5", "second-order-definability",
        ))
        tex_command_check = {"frame_definability_title_and_seven_imports_reviewed": True}
    elif row["unit_id"] == "OLP-0420":
        assert frame_definability_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\mModel{F} \Entails !A", r"V(p) =", r"\Box p \lif p",
        ))
        tex_command_check = {"fixed_model_vs_all_valuations_and_frame_intro_reviewed": True}
    elif row["unit_id"] == "OLP-0421":
        assert frame_definability_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\ollabel{tab:five}", r"\ollabel{tab:anotherfive}",
            r"\ollabel{prop:reflexive}", r"\ollabel{fig:Bsymm}",
            "সিরিয়াল", "প্রতিবিম্বী", "প্রতিসম", "পরিযায়ী", "ইউক্লিডীয়",
        ))
        tex_command_check = {"both_correspondence_tables_proof_diagram_and_countermodel_reviewed": True}
    elif row["unit_id"] == "OLP-0422":
        assert frame_definability_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\mModel{F} = \tuple{W,R}", r"\mClass{F} \Entails !A",
            "অশূন্য সমষ্টি", "উপর প্রতিষ্ঠিত",
        ))
        tex_command_check = {"frame_model_and_frame_class_validity_definitions_reviewed": True}
    elif row["unit_id"] == "OLP-0423":
        assert frame_definability_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\mSat{M}{\Box !A}[w]", r"V(q) = \emptyset$)",
            r"\ollabel{thm:fullCorrespondence}", r"\ollabel{prop:relation-facts}",
        ))
        tex_command_check = {"five_converse_constructions_two_corollaries_and_relation_facts_reviewed": True}
    elif row["unit_id"] == "OLP-0424":
        assert frame_definability_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\Gamma = \{!F, !A_2, !A_3, \dots\}",
            r"$n\ge 2$", r"$k=2$", r"$i\ge2$",
            r"\lforall[x][\lforall[y][\Atom{Q}{x,y}]]",
        ))
        tex_command_check = {"loeb_compactness_defined_indices_and_universality_reviewed": True}
    elif row["unit_id"] == "OLP-0425":
        assert frame_definability_math_fix and not documented
        assert all(phrase in checked_target for phrase in (
            r"\ollabel{prop:equivalences}", r"\ollabel{prop:S5=univ}",
            r"\ollabel{fig:partition}", r"V'(p) = V(p) \cap W'",
        ))
        tex_command_check = {"equivalence_s5_partition_and_universal_countermodel_reviewed": True}
    elif row["unit_id"] == "OLP-0426":
        assert frame_definability_math_fix
        assert all(phrase in checked_target for phrase in (
            r"\tagitem{prvTrue}{\indcase{!A}{\ltrue}",
            r"\tagitem{prvIff}{\indcase{!A}{(!B \liff !C)}",
            r"\Sat{M}{\lforall[y][(\Atom{Q}{x,y} \lif",
            r"\ollabel{prop:st}",
        ))
        tex_command_check = {"standard_translation_all_cases_monadic_definition_and_reflexivity_proof_reviewed": True}
    elif 427 <= unit_number <= 440:
        assert axioms_systems_math_fix
        axioms_review_anchors = {
            "OLP-0427": (r"\olchapter{nml}{prf}", r"\olimport{consistency}"),
            "OLP-0428": (r"\olfileid{nml}{axs}{int}", r"\begin{prooftree}", r"\Sigma \Proves !A"),
            "OLP-0429": (r"\ollabel{prop:rk}", r"\ollabel{prop:notDiamondBot}", r"\Frm[L]"),
            "OLP-0430": (r"\Setabs{!B}{\Log{K}", r"\Ax{K} \in \Sigma"),
            "OLP-0431": (r"\olfileid{nml}{prf}{prk}", r"\begin{derivation}", r"\iftag{prvBox}"),
            "OLP-0432": (r"\ollabel{prop:rewriting}", r"\Subst{!C}{!B}{q}", r"\PL"),
            "OLP-0433": (r"\Diamond(!A \lor!B)", r"\olref[der]{sec}"),
            "OLP-0434": (r"\ollabel{def:duals}", r"\Ax{5_\Diamond}", r"\ollabel{prop:dualsys}"),
            "OLP-0435": (r"\ollabel{prop:S5facts}", r"\Log{KTB4} = \Log{KT5}", r"\ollabel{prop:S5}"),
            "OLP-0436": (r"\ollabel{thm:soundness}", r"\mClass{C}_1 \cap \dots \cap \mClass{C}_n"),
            "OLP-0437": (r"\ollabel{thm:KTBnot45}", r"\ollabel{thm:KD5not4}", r"\ollabel{fig:KD5not4}"),
            "OLP-0438": (r"\ollabel{defn:Gammaproves}", r"\Gamma \Proves[\Sigma] !A"),
            "OLP-0439": (r"\ollabel{prop:derivabilityfacts-cut}", r"\ollabel{prop:derivabilityfacts-ruleT}"),
            "OLP-0440": (r"\ollabel{prop:consistencyfacts}", r"\Gamma \Proves/[\Sigma] \lfalse"),
        }
        assert all(anchor in checked_target for anchor in axioms_review_anchors[row["unit_id"]])
        tex_command_check = {"modal_axioms_systems_proofs_and_anchors_reviewed": True}
    elif 441 <= unit_number <= 449:
        assert modal_completeness_math_fix
        if row["unit_id"] == "OLP-0447":
            assert modal_completeness_control_fix
        modal_completeness_review_anchors = {
            "OLP-0441": (r"\olchapter{nml}{com}", r"\olimport{frame-completeness}"),
            "OLP-0442": (r"\mSat/{M}{!A}", r"\Proves/[\Sigma] \lnot !A"),
            "OLP-0443": (r"\ollabel{prop:ccs-properties}", r"\ollabel{prop:ccs-liff}"),
            "OLP-0444": (r"\ollabel{thm:lindenbaum}", r"\ollabel{cor:provability-characterization}"),
            "OLP-0445": (r"\ollabel{lem:box1}", r"\ollabel{lem:box-iff-diamond}", r"\iftag{prvBox}"),
            "OLP-0446": (r"\mModel{M}^\Sigma", r"\Diamond\Delta' \subseteq \Delta"),
            "OLP-0447": (r"\ollabel{prop:truthlemma}", r"\tagitem{prvDiamond}"),
            "OLP-0448": (r"\ollabel{thm:determination}", r"\ollabel{cor:Kcomplete}"),
            "OLP-0449": (r"\ollabel{thm:completeframeprops}", r"\ollabel{thm:generaldet}", r"\ollabel{prop:anotherfive-a}"),
        }
        assert all(
            anchor in checked_target
            for anchor in modal_completeness_review_anchors[row["unit_id"]]
        )
        tex_command_check = {"modal_completeness_proofs_and_anchors_reviewed": True}
    elif 450 <= unit_number <= 459:
        assert filtrations_math_fix
        filtration_review_anchors = {
            "OLP-0450": (r"\olchapter{nml}{fil}", r"\olimport{euclidean-filtrations}"),
            "OLP-0451": (r"BN-SRC-360", r"BN-SRC-361", r"\mSat{M}{!B}[v]"),
            "OLP-0452": (r"\ollabel{defn:modallyclosed}", r"[w] = \Setabs{v}{v \equiv w}"),
            "OLP-0453": (r"\ollabel{thm:filtrations}", r"\tagitem{prvDiamond}", r"\begin{cor}"),
            "OLP-0454": (r"\ollabel{prop:finest}", r"\ollabel{fig:ex-filtration}", r"\begin{tagenumerate}"),
            "OLP-0455": (r"\ollabel{prop:filt-are-finite}", r"\card{W^*} \le \card{\Pow{\Gamma}}"),
            "OLP-0456": (r"\ollabel{prop:K-fmp}", r"\ollabel{cor:S5fmp}", r"BN-SRC-362"),
            "OLP-0457": (r"\olsection{\Log{S5} সিদ্ধান্তযোগ্য}", r"\olref[fmp]{cor:S5fmp}"),
            "OLP-0458": (r"\ollabel{tab:Cn-filtrations}", r"\ollabel{thm:more-filtrations}", r"C_4(u,v)"),
            "OLP-0459": (r"\ollabel{fig:ser-eucl2}", r"\ollabel{thm:modal-closed-filt}", r"BN-SRC-364"),
        }
        assert all(anchor in checked_target for anchor in filtration_review_anchors[row["unit_id"]])
        tex_command_check = {"filtrations_definitions_diagrams_proofs_and_anchors_reviewed": True}
    elif 460 <= unit_number <= 469:
        assert modal_tableaux_math_fix
        modal_tableaux_review_anchors = {
            "OLP-0460": (r"\olchapter{nml}{tab}", r"\olimport{countermodels}"),
            "OLP-0461": (r"\olfileid{nml}{tab}{int}", r"\sFmla{\True}{\Box !A \lif !A}[1.2]"),
            "OLP-0462": (r"\ollabel{tab:prop-rules}", r"\ollabel{tab:rules-K}", r"BN-SRC-371"),
            "OLP-0463": (r"\olfileid{nml}{tab}{prk}", r"\begin{oltableau}", r"\begin{prob}"),
            "OLP-0464": (r"\ollabel{thm:tableau-soundness}", r"\ollabel{cor:entailment-soundness}", r"BN-SRC-372"),
            "OLP-0465": (r"\ollabel{tab:logics-rules}", r"\Log{S5} \Proves \Box!A \lif \Box\Diamond!A", r"BN-SRC-373"),
            "OLP-0466": (r"\ollabel{prop:soundness-4r}", r"\ollabel{cor:soundness-logics}", r"BN-SRC-376"),
            "OLP-0467": (r"\olfileid{nml}{tab}{s5}", r"\begin{oltableau}", r"\Ax{5}"),
            "OLP-0468": (r"\ollabel{thm:tableau-completeness}", r"BN-SRC-377", r"BN-SRC-384"),
            "OLP-0469": (r"\ollabel{fig:counter-Box}", r"\ollabel{fig:counter-Diamond}", r"BN-SRC-388"),
        }
        assert all(anchor in checked_target for anchor in modal_tableaux_review_anchors[row["unit_id"]])
        if row["unit_id"] == "OLP-0462":
            wrong = r"[\pFmla{\False}{\formula{A}}{1.1}, just = {\TRule{\True}{\Box}[2]}"
            right = r"[\pFmla{\False}{\formula{A}}{1.1}, just = {\TRule{\False}{\Box}[2]}"
            assert wrong in source and wrong not in checked_target and right in checked_target
        if row["unit_id"] == "OLP-0469":
            wrong = r"[\pFmla{\False}{\Diamond(p \land q) \lif (\Diamond p \land \Diamond q)}{1}"
            right = r"[\pFmla{\False}{(\Diamond p \land \Diamond q) \lif \Diamond(p \land q)}{1}"
            assert wrong in source and wrong not in checked_target
            assert checked_target.count(right) == source.count(right) + 1
        tex_command_check = {"modal_tableaux_rules_proofs_and_anchors_reviewed": True}
    elif 470 <= unit_number <= 474:
        assert set(documented) == (
            {"BN-SRC-389"} if row["unit_id"] == "OLP-0473" else set()
        )
        modal_sequent_review_anchors = {
            "OLP-0470": (r"\olchapter{nml}{seq}", r"\begin{editorial}", r"\olimport{more-rules}"),
            "OLP-0471": (r"\olfileid{nml}{seq}{int}", r"\DisplayProof", r"\Cut"),
            "OLP-0472": (r"\olfileid{nml}{seq}{rul}", r"\RightLabel{$\Box*$}", r"\RightLabel{$\Diamond*$}"),
            "OLP-0473": (r"\olfileid{nml}{seq}{prk}", r"\Dual", r"BN-SRC-389"),
            "OLP-0474": (r"\ollabel{tab:more-rules}", r"\ollabel{tab:logics-rules}", r"\RightLabel{\Cut}"),
        }
        assert all(anchor in checked_target for anchor in modal_sequent_review_anchors[row["unit_id"]])
        if row["unit_id"] == "OLP-0473":
            wrong = "\\Axiom$!A \\fCenter !A$\n    \\RightLabel{\\RightR{\\lnot}}\n    \\UnaryInf$\\lnot !A, !A \\fCenter $"
            assert wrong in source and wrong not in checked_target
            assert r"\RightLabel{\LeftR{\lnot}}" in checked_target
        tex_command_check = {"modal_sequent_rules_proofs_and_anchors_reviewed": True}
    elif 475 <= unit_number <= 480:
        assert set(documented) == (
            {"BN-SRC-390"} if row["unit_id"] == "OLP-0478" else set()
        )
        temporal_review_anchors = {
            "OLP-0475": (r"\olpart{aml}", r"\begin{editorial}", r"\olimport[epistemic-logic]{epistemic-logic}"),
            "OLP-0476": (r"\olchapter{aml}{tl}", r"\olimport{possible-histories}"),
            "OLP-0477": (r"\olfileid{aml}{tl}{int}", r"\olsection{ভূমিকা}"),
            "OLP-0478": (r"\ollabel{defn:tmodels}", r"\ollabel{defn:sub:mmodels-g}", r"BN-SRC-390"),
            "OLP-0479": (r"\ollabel{tab:correspondence}", r"$\Ftemp \Ftemp p \lif \Ftemp p$"),
            "OLP-0480": (r"\ollabel{defn:since-until}", r"\ollabel{defn:sub:mmodels-until}"),
        }
        assert all(anchor in checked_target for anchor in temporal_review_anchors[row["unit_id"]])
        if row["unit_id"] == "OLP-0478":
            assert "$F !A$" in source and "$F !A$" not in checked_target
            assert "$\\Ftemp !A$" in checked_target
            temporal_math_fix = (
                source_math - target_math == collections.Counter({"F!A": 1})
                and target_math - source_math == collections.Counter({r"\Ftemp!A": 1})
            )
        tex_command_check = {"temporal_semantics_frames_and_operators_reviewed": True}
    elif 481 <= unit_number <= 485:
        assert set(documented) == (
            {"BN-SRC-391"} if row["unit_id"] == "OLP-0483" else set()
        )
        epistemic_opening_anchors = {
            "OLP-0481": (r"\olfileid{aml}{tl}{poss}", r"\ollabel{defn:phmodels}", r"\Diamond \Ftemp p"),
            "OLP-0482": (r"\olchapter{aml}{el}", r"\olimport{bisimulations}", r"\olimport{public-announcement-logic-semantics}"),
            "OLP-0483": (r"\olfileid{aml}{el}{int}", "Jaakko Hintikka", r"BN-SRC-391"),
            "OLP-0484": (r"\olfileid{aml}{el}{lan}", r"\Knows_a !A", r"\CKnows_G !A"),
            "OLP-0485": (r"\olfileid{aml}{el}{rel}", r"\tuple{W, R, V}", r"R_a ww'"),
        }
        assert all(anchor in checked_target for anchor in epistemic_opening_anchors[row["unit_id"]])
        if row["unit_id"] == "OLP-0483":
            assert source.count("Jaako Hintikka") == 1
            assert "Jaako Hintikka" not in checked_target
            assert checked_target.count("Jaakko Hintikka") == 1
        tex_command_check = {"temporal_histories_and_epistemic_opening_reviewed": True}
    elif 486 <= unit_number <= 490:
        assert set(documented) == (
            {"BN-SRC-392"} if row["unit_id"] == "OLP-0489" else set()
        )
        epistemic_completion_anchors = {
            "OLP-0486": (r"\olfileid{aml}{el}{trw}", r"\ollabel{defn:sub:mmodels-box}", r"\CKnows_{G'} !A"),
            "OLP-0487": (r"\olfileid{aml}{el}{acc}", r"\ollabel{tab:four}", r"\Knows \neg \Knows p"),
            "OLP-0488": (r"\olfileid{aml}{el}{bsd}", r"\leftrightarroweq", r"\ollabel{fig:bisimilar}"),
            "OLP-0489": (r"\olfileid{aml}{el}{pal}", r"\iftag{prvIff}", r"\tagitem{limitClause}"),
            "OLP-0490": (r"\olfileid{aml}{el}{psm}", r"\ollabel{defn:sub:mmodels-pal}", r"\ollabel{fig:announcement-example}"),
        }
        assert all(anchor in target for anchor in epistemic_completion_anchors[row["unit_id"]])
        if row["unit_id"] == "OLP-0489":
            assert r"\iftag{prvIff}" not in source
            assert r"\iftag{prvIff}" not in checked_target
            assert target.count(r"\iftag{prvIff}") == 1
            assert r"\tagitem{prvIff}" in source and r"\tagitem{prvIff}" in target
        tex_command_check = {"epistemic_truth_frames_bisimulation_and_announcements_reviewed": True}
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
            arithmetic_math_fix,
            interpolation_math_fix,
            bounded_minimization_math_fix,
            s_m_n_index_fix,
            halting_parenthetical_name_fix,
            russell_self_membership_fix,
            ce_equivalence_math_fixes,
            complement_ce_index_fixes,
            reducibility_pair_fix,
            reduction_type_fix,
            complete_ce_direction_fix,
            total_partial_equality_fix,
            rice_partial_equality_fix,
            rice_monotonicity_prose_fix,
            fixed_point_partial_equalities_fix,
            fixed_point_application_scope_fixes,
            self_reference_partial_equality_fix,
            representing_tm_table_fix,
            configuration_empty_input_fix,
            unary_adder_endpoint_normalization,
            disciplined_adder_endpoint_normalization,
            combined_machine_fix_and_endpoint_normalization,
            partial_undefined_output_fix,
            variant_boundary_marker_fix,
            standard_machine_simulation_fix,
            universal_output_decoding_fix,
            halting_machine_combination_notation_fix,
            representing_fo_fixes,
            verification_representation_fixes,
            decision_unsolvability_fixes,
            trakhtenbrot_fixes,
            overview_math_fix,
            undecidability_math_fix,
            arithmetization_syntax_math_fix,
            representability_q_math_fix,
            theories_computability_math_fix,
            incompleteness_provability_math_fix,
            second_order_syntax_semantics_math_fix,
            second_order_metatheory_math_fix,
            second_order_set_theory_math_fix,
            lambda_introduction_completion_math_fix,
            lambda_syntax_foundations_math_fix,
            lambda_church_rosser_math_fix,
            lambda_definability_opening_math_fix,
            lambda_definability_pairs_truth_pr_math_fix,
            lambda_definability_completion_math_fix,
            many_valued_syntax_semantics_math_fix,
            three_valued_logics_math_fix,
            infinite_valued_logics_math_fix,
            many_valued_sequent_calculus_math_fix,
            normal_modal_opening_math_fix,
            normal_modal_completion_math_fix,
            frame_definability_math_fix,
            axioms_systems_math_fix,
            modal_completeness_math_fix,
            filtrations_math_fix,
            modal_tableaux_math_fix,
            temporal_math_fix,
            shared_audit_fix,
        )
    )
    controls_ok = (
        controls(source) == controls(checked_target)
        or axd_control_fix
        or completeness_control_fix
        or representability_q_control_fix
        or second_order_metatheory_control_fix
        or lambda_syntax_control_fix
        or modal_completeness_control_fix
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
            or representing_formula_classification_fix
            or theories_computability_token_fix
            or incompleteness_provability_token_fix
            or second_order_syntax_semantics_token_fix
            or second_order_metatheory_token_fix
        ),
        "unicode_nfc": unicodedata.is_normalized("NFC", target),
        "documented_source_corrections": documented,
        "tex_command_check": tex_command_check,
        "target_sha256": hashlib.sha256(target_path.read_bytes()).hexdigest(),
    }
    if normalizations:
        checks["documented_source_normalizations"] = normalizations
    assert checks["source_blocks"] == checks["target_blocks"], row["unit_id"]
    assert all(
        checks[key]
        for key in ("math_parity", "controls_parity", "env_parity", "token_parity", "unicode_nfc")
    ), (row["unit_id"], checks)
    print(json.dumps(checks, ensure_ascii=False))
    checked_ids.append(row["unit_id"])

if os.environ.get("OPENLOGIC_REGENERATING_DRAFT_STATUS") != "1":
    draft = json.loads((repo / "evidence/DRAFT_STATUS.json").read_text(encoding="utf-8"))
    assert sorted(checked_ids) == sorted(draft["draft_scope"]["translated_units"]), checked_ids
