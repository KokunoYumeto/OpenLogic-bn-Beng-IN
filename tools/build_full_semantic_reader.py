"""Convert the integrated 722-unit LaTeX edition to audited native MathML HTML.

No TeX process is invoked. Historical published reader artifacts are retained.
"""

from __future__ import annotations

import collections
import json
import pathlib
import re
import subprocess
import base64

import prepare_full_edition as full
import build_cumulative_semantic_reader as reader
import build_reader_operator_font as operators
from bs4 import BeautifulSoup

BUILD = full.BUILD
HTML = BUILD / "openlogic-bn-Beng-IN-complete.html"


def full_math(value):
    value = re.sub(r"\\textsc(?![A-Za-z@])", r"\\text", value)
    for name, (code, _, _, _) in operators.GLYPHS.items():
        value = re.sub(r"\\" + name + r"(?![A-Za-z@])", lambda _m, code=code: r"\mathrel{\text{" + chr(code) + "}}", value)

    def rule(source, position):
        kind, position = reader.parse_required(source, position)
        symbol, position = reader.parse_required(source, position)
        subscript, position = reader.parse_optional(source, position)
        return (r"\ensuremath{{" + kind + ("_{" + subscript + "}" if subscript is not None else "")
                + "}" + symbol + "}", position)
    value = reader.replace_macro(value, "iR", rule)
    for command, style, text in (("Refut", "mathrm", "Ref"), ("ORefut", "mathsf", "Ref"),
                                 ("RProv", "mathrm", "RProv"), ("ORProv", "mathsf", "RProv")):
        def relation(source, position, style=style, text=text):
            sub, position = reader.parse_optional(source, position)
            return "\\" + style + "{" + text + "}" + ("_{" + sub + "}" if sub else ""), position
        value = reader.replace_macro(value, command, relation)
    for command, text in (("TrmSOL", "Trm"), ("FrmSOL", "Frm")):
        def second_order(source, position, text=text):
            language, position = reader.parse_optional(source, position)
            return r"\mathrm{" + text + "}^{2}" + (r"(\mathcal{" + language + "})" if language else ""), position
        value = reader.replace_macro(value, command, second_order)
    value = reader.replace_macro(value, "smash", lambda source, position: reader.parse_required(source, position))
    value = value.replace(r"\supstrict", r"\operatorname{lsub}")
    value = re.sub(r"\\hskip\s*[-+]?[0-9.]+\s*(?:em|ex|pt)", "", value)
    value = re.sub(r"\\hspace\*?\{[-+]?[0-9.]+(?:em|ex|pt)\}", r"\\quad ", value)
    # Typography inside math is expressed as native MathML text.
    def normalize_math(match):
        fragment = match[0]
        for command in ("textsc", "emph"):
            fragment = reader.replace_macro(fragment, command, lambda source, position: (
                r"\text{" + reader.parse_required(source, position)[0] + "}", reader.parse_required(source, position)[1]))
        return fragment
    value = re.sub(r"(?<!\\)\$(?:[^$]|\\\$)*(?<!\\)\$", normalize_math, value)
    value = re.sub(r"(?<!\\)\\\[.*?(?<!\\)\\\]", normalize_math, value, flags=re.S)
    return value


def expand_finite_tikz_loops(value):
    pattern = re.compile(r"\\foreach\s+((?:\\[A-Za-z]+/?)+)\s+in\s*")
    while True:
        match = pattern.search(value)
        if not match:
            return value
        values, position = reader.parse_required(value, match.end())
        position = reader.skip_space(value, position)
        if value[position] == "{":
            statement, end = reader.parse_required(value, position)
        else:
            end = value.index(";", position) + 1
            statement = value[position:end]
        variables = re.findall(r"\\[A-Za-z]+", match[1])
        expanded = []
        for item in values.split(","):
            fields = item.strip().split("/")
            if len(fields) < len(variables):
                fields.extend([fields[-1]] * (len(variables) - len(fields)))
            require(len(fields) == len(variables), "unhandled TikZ loop binding")
            require("..." not in item, "unexpanded TikZ range")
            instance = statement
            for variable, field in sorted(zip(variables, fields), key=lambda pair: -len(pair[0])):
                instance = re.sub(re.escape(variable) + r"(?![A-Za-z@])", lambda _m, field=field: field, instance)
            expanded.append(instance)
        value = value[:match.start()] + "\n".join(expanded) + value[end:]


def expand_fixed_preamble(value):
    def declaration(source, position):
        name, position = reader.parse_required(source, position)
        arity, position = reader.parse_optional(source, position)
        body, position = reader.parse_required(source, position)
        for _ in range(12):
            expanded = full_math(reader.special_math_macros(body))
            if expanded == body:
                break
            body = expanded
        else:
            raise RuntimeError("preamble math normalization did not converge: " + name)
        return r"\newcommand{" + name + "}" + ("[" + arity + "]" if arity else "") + "{" + body + "}", position
    return reader.replace_macro(value, "newcommand", declaration)


def expand_constant_aliases(body, preamble):
    aliases = {}
    def declaration(source, position):
        name, position = reader.parse_required(source, position)
        arity, position = reader.parse_optional(source, position)
        value, position = reader.parse_required(source, position)
        if arity is None:
            aliases[name] = value
        return "", position
    reader.replace_macro(preamble, "newcommand", declaration)
    pattern = re.compile(r"\\[A-Za-z@]+")
    for _ in range(16):
        # Preserve one-token macro arguments and prevent adjacent control words
        # from merging (for example, \in followed by a macro expanding to R).
        expanded = pattern.sub(lambda match: "{" + aliases[match[0]] + "}" if match[0] in aliases else match[0], body)
        if expanded == body:
            return full_math(reader.normalize_display_environments(body))
        body = expanded
    raise RuntimeError("constant macro aliases did not converge")


def lift_formula_arrays(value):
    semantic = ("proof-tree-semantic", "tableau-semantic", "derivation-semantic")
    def convert(body, _index):
        layout, position = reader.parse_required(body, 0)
        content = body[position:]
        if not any(r"\begin{" + name + "}" in content for name in semantic):
            return r"\begin{array}{" + layout + "}" + content + r"\end{array}"
        # Retain row/cell order; every contained proof stays independently auditable.
        content = re.sub(r"\\hline\b", "", content)
        content = re.sub(r"\\\\(?:\[[^\]]*\])?", r"\\par ", content)
        content = content.replace("&", r"\par ")
        return r"\begin{display-prose}" + content + r"\end{display-prose}"
    return reader.transform_environments(value, "array", convert)[0]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def create_semantic_input():
    receipt = json.loads((BUILD / "PREPARATION.json").read_text(encoding="utf-8"))
    tex_path = full.REPO / receipt["tex"]["path"]
    require(full.digest(tex_path) == receipt["tex"]["sha256"], "prepared LaTeX bytes changed")
    raw = tex_path.read_text(encoding="utf-8")
    pieces = list(re.finditer(r"^% SOURCE-UNIT (OLP-\d{4}) ([^\n]+)\n", raw, re.M))
    order = [piece[1] for piece in pieces]
    require(order == receipt["reader_order"] and len(set(order)) == 722, "complete reader order changed")
    reader.BUILD = BUILD
    reader.HTML_OUTPUT = HTML
    reader.EXPECTED_UNITS = order
    reader.EXPECTED_UNIT_COUNT = 722
    reader.EXPECTED_UNTRANSLATED = 0
    reader.PRESERVE_MATH_LINKS = True
    reader.MATH_LINK_TARGETS.clear()
    reader.PROOF_GRAPH_RECEIPTS.clear()
    counter = 1
    markers = {}
    results = []
    for index, piece in enumerate(pieces):
        uid, path = piece[1], piece[2]
        reader.CURRENT_SOURCE_UNIT = uid
        end = pieces[index + 1].start() if index + 1 < len(pieces) else raw.index(r"\bibliographystyle", piece.end())
        value = reader.strip_comments(raw[piece.end():end])
        try:
            value = reader.replace_macro(value, "eqref", lambda source, position: (
                r"\hyperlink{" + reader.parse_required(source, position)[0] + "}{দেখুন}",
                reader.parse_required(source, position)[1]))
            def prefixed_formula(source, position):
                sign, position = reader.parse_required(source, position)
                formula, position = reader.parse_required(source, position)
                prefix, position = reader.parse_required(source, position)
                return r"\sFmla{" + sign + "}{" + formula + "}[" + prefix + "]", position
            value = reader.replace_macro(value, "pFmla", prefixed_formula)
            value, proofs = reader.transform_proof_trees(value)
            value, tableaux = reader.transform_tableaux(value)
            value, derivations = reader.transform_derivations(value)
            value = reader.normalize_structural_macros(value)
            value = expand_finite_tikz_loops(value)
            value, diagrams = reader.transform_diagrams(value)
            for _ in range(12):
                expanded = reader.special_math_macros(value)
                if expanded == value:
                    break
                value = expanded
            else:
                raise RuntimeError("math macro expansion did not converge")
            value = value.replace(r"\mathrel{||}\joinrel\Relbar", r"\vDash")
            value = full_math(value)
            value = reader.replace_formula_metavariables(value)
            value = value.replace(r"\/", "")
            value = lift_formula_arrays(value)
            value = re.sub(r"\\def\\arraystretch\{[^{}]+\}", "", value)
            value = value.replace(r"\def\fCenter{}", "")
            value = reader.normalize_display_environments(value)
            value = full_math(value)
            value, found, counter = reader.mark_environment_titles(value, counter)
            require(not (markers.keys() & found.keys()), "duplicate environment marker")
            markers.update(found)
            value = rf"\texttt{{UNITMARKER-{uid}}}\par" + "\n" + value
            results.append(reader.UnitResult(uid, path, value, proofs, tableaux, diagrams, derivations, found))
        except Exception as exc:
            raise RuntimeError(f"{uid} ({path}): {exc}") from exc
    body = "\n\n".join(result.body for result in results)
    macros = expand_fixed_preamble(reader.extract_fixed_macro_preamble(set(re.findall(r"\\([A-Za-z@]+)", body))))
    body = expand_constant_aliases(body, macros)
    environments = ("scope-note", "proof-tree-semantic", "tableau-semantic", "derivation-semantic",
                    "diagram-semantic", "display-prose", "translationnote", "editorial", "intro", "explain", "digress", "history")
    declarations = "\n".join(r"\newenvironment{" + name + "}{}{}" for name in environments)
    note = r"""
\chapter*{এই সংস্করণ সম্পর্কে}
\begin{scope-note}
এই সম্পূর্ণ পাঠে হিমায়িত OpenLogic উৎসের সব ৭২২টি অনূদিত একক সংযোজিত।
বিকল্প অধ্যায়-বিন্যাস ও স্বতন্ত্র সূত্রসারণি সংশ্লিষ্ট বিষয়ের সঙ্গেই আছে।
অধ্যায়-চালকের আমদানি-নির্দেশের বদলে প্রত্যেক উৎস একক একবার সংযোজিত হয়েছে।
সূত্রের মূল পরিচয় সংরক্ষিত; বিকল্প উৎসপাঠের সূত্রনির্দেশে পৃথক একক-পরিচয় আছে।
হিমায়িত উৎসে চারটি অনুপস্থিত প্রস্তাব-নাম স্থানীয় সূত্রনির্দেশ-টীকায় চিহ্নিত।
তৃপ্তির দুটি উৎস-প্রস্তাব সংশ্লিষ্ট অনুশীলনীর বক্তব্য স্পষ্ট করতে দেখানো হয়েছে।
সূত্রগুলি নেটিভ MathML; প্রমাণ-বৃক্ষ, ট্যাবলো, নিষ্পাদন ও চিত্রের সংযোগগুলি
পুনঃপ্রবাহযোগ্য পাঠ্যরূপে আছে। মূল চিত্রের জন্য সংশ্লিষ্ট PDF ও সম্পাদনাযোগ্য LaTeX দেখুন।
এআই-সহায়ক অনুবাদ, সংশোধন ও স্বয়ংক্রিয় পর্যালোচনা:
OpenAI Codex — GPT-5.6 Sol এবং GPT-6 Sol; Ultra effort।
স্বাধীন মানব-পর্যালোচনা বা সম্পূর্ণ আনুষ্ঠানিক প্রমাণ-যাচাইয়ের দাবি করা হচ্ছে না।
\end{scope-note}
"""
    source = BUILD / "semantic-input.tex"
    source.write_text(r"\documentclass{book}" + "\n" + r"\usepackage{amsmath,amssymb}" + "\n"
                      + declarations + "\n" + macros + "\n" + r"\begin{document}" + "\n" + note + "\n" + body
                      + "\n" + r"\chapter*{সংস্করণ ও লাইসেন্স}" + "\n"
                      + "মূল রচনা Open Logic Project। উৎস ও বাংলা অনুবাদ Creative Commons Attribution 4.0 International লাইসেন্সে প্রকাশিত।\n"
                      + r"উৎস সংস্করণ: \texttt{" + reader.SOURCE_REVISION + "}.\n"
                      + r"\end{document}" + "\n", encoding="utf-8", newline="\n")
    stats = {name: sum(getattr(result, name) for result in results)
             for name in ("proof_trees", "tableaux", "derivations", "diagrams")}
    stats.update(source_units=722, numbered_environments=len(markers),
                 prepared_tex_sha256=receipt["tex"]["sha256"],
                 semantic_input_sha256=full.digest(source), semantic_input_bytes=source.stat().st_size,
                 documented_missing_source_references=receipt["documented_missing_source_references"],
                 reader_adjustments=receipt["reader_adjustments"])
    reader.write_json(BUILD / "SEMANTIC_INPUT.json", stats)
    reader.write_json(BUILD / "environment-markers.json", markers)
    reader.write_json(BUILD / "proof-graphs.json", reader.PROOF_GRAPH_RECEIPTS)
    reader.write_json(BUILD / "math-link-targets.json", reader.MATH_LINK_TARGETS)
    print(json.dumps({"prepared_semantic_units": 722, "semantic_input_bytes": source.stat().st_size,
                      "proof_trees": stats["proof_trees"], "tableaux": stats["tableaux"], "diagrams": stats["diagrams"]}), flush=True)
    return source, stats, markers


def main():
    operator_font = operators.build()
    source, source_stats, markers = create_semantic_input()
    cache_path = BUILD / "PANDOC_INPUT.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    pandoc = BUILD / "pandoc.html"
    identities = {"semantic_input_sha256": full.digest(source), "bibliography_sha256": full.digest(reader.BIB_PATH),
                  "pandoc_version": subprocess.check_output(["pandoc", "--version"], text=True, encoding="utf-8").splitlines()[0]}
    if (all(cache.get(key) == value for key, value in identities.items()) and pandoc.exists()
            and cache.get("html_sha256") == full.digest(pandoc)):
        warnings = (BUILD / "pandoc.log").read_text(encoding="utf-8")
        require("Could not convert TeX math" not in warnings, "cached mathematical conversion failed")
    else:
        pandoc, warnings = reader.run_pandoc(source)
        reader.write_json(cache_path, identities | {"html_sha256": full.digest(pandoc)})
    epub_source, html_receipt = reader.postprocess_html(
        pandoc, markers, edition_title="ওপেন লজিক: সম্পূর্ণ ভারতীয় বাংলা সংস্করণ",
        edition_subtitle="সব ৭২২টি উৎস এককের সম্পূর্ণ পাঠ · বাংলা (ভারত)", strict_links=True,
        chapter_level=2, section_level=3)
    # These original operator glyphs have no standard-font substitute here.
    # Embed their exact project outlines and mark their mathematical names.
    def embed_operator_font(path, embed_fonts):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        style = soup.new_tag("style")
        styles = []
        for font_path in sorted(set(operator_font.values())):
            font_url = "data:font/ttf;base64," + base64.b64encode(font_path.read_bytes()).decode("ascii") if embed_fonts else font_path.name
            styles.append("@font-face{font-family:" + font_path.stem + ";src:url('" + font_url + "')}")
        style.string = "\n".join(styles)
        soup.head.append(style)
        license_details = soup.new_tag("details", id="operator-font-license")
        license_summary = soup.new_tag("summary")
        license_summary.string = "গাণিতিক প্রতীকের মূল ফন্ট ও লাইসেন্স"
        license_details.append(license_summary)
        license_intro = soup.new_tag("p")
        license_intro.string = ("boxright ও fishhookright-এর রেখা TX Fonts থেকে এবং "
                                "leftrightarroweq-এর রেখা St Mary’s Road থেকে নেওয়া হয়েছে। "
                                "এই সংস্করণে মূল রেখা পৃথক অফলাইন ফন্টে রূপান্তরিত।")
        license_details.append(license_intro)
        tx_text = soup.new_tag("pre")
        tx_text["class"] = "license-text"
        tx_text.string = (BUILD / "font-sources/TXFONTS-COPYRIGHT.txt").read_text(encoding="ascii")
        license_details.append(tx_text)
        stmary_text = soup.new_tag("p")
        stmary_text.string = ("St Mary’s Road ফন্টের স্বত্ব Jeremy Gibbons ও Alan Jeffrey-এর; "
                              "মূল নথিতে LaTeX Project Public License 1.0 বা পরবর্তী সংস্করণে বিতরণের শর্ত আছে। ")
        source_link = soup.new_tag("a", href="https://tug.ctan.org/fonts/stmaryrd/stmaryrd.pdf")
        source_link.string = "মূল ফন্ট-নথি"
        stmary_text.append(source_link)
        license_details.append(stmary_text)
        soup.find("main", id="reader-content").append(license_details)
        for name, (code, _, _, _) in operators.GLYPHS.items():
            for text in list(soup.find_all(string=lambda text: text is not None and chr(code) in str(text))):
                if text.parent.name == "annotation":
                    text.replace_with(str(text).replace(chr(code), "\\" + name))
                    continue
                if text.parent.name in ("mtext", "mi", "mo"):
                    text.parent["style"] = "font-family:" + operator_font[name].stem + ";font-style:normal"
                    text.parent["aria-label"] = "\\" + name
        for text in list(soup.find_all(string=re.compile(r"MATHREF\d{6}"))):
            if text.parent.name == "annotation":
                replacement = str(text)
                for marker in re.findall(r"MATHREF\d{6}", replacement):
                    record = reader.MATH_LINK_TARGETS[marker]
                    replacement = replacement.replace(marker, record["text"] + " (" + record["target"] + ")")
                text.replace_with(replacement)
                continue
            parts = re.split(r"(MATHREF\d{6})", str(text))
            for part in parts:
                if part in reader.MATH_LINK_TARGETS:
                    record = reader.MATH_LINK_TARGETS[part]
                    target = soup.find(id=record["target"])
                    require(target is not None, "missing mathematical reference: " + record["target"])
                    environment = target.find_parent("div", class_=lambda value: value and any(n in value.split() for n in reader.NUMBERED_ENVS))
                    title = environment.find(class_="environment-title") if environment else None
                    link = soup.new_tag("a", href="#" + record["target"])
                    link.string = title.get_text(" ", strip=True) if title else "সূত্র " + record["target"].split(":", 1)[0].upper()
                    text.insert_before(link)
                elif part:
                    text.insert_before(part)
            text.extract()
        ids = {node["id"] for node in soup.find_all(id=True)}
        require(all(link["href"][1:] in ids for link in soup.select('a[href^="#"]')), "reference restoration introduced a broken link")
        path.write_text(str(soup), encoding="utf-8", newline="\n")
    embed_operator_font(HTML, True)
    embed_operator_font(epub_source, False)
    html_receipt.update(html_bytes=HTML.stat().st_size, html_sha256=full.digest(HTML),
                        epub_source_bytes=epub_source.stat().st_size, epub_source_sha256=full.digest(epub_source))
    for html_key, source_key in (("proof_tree_blocks", "proof_trees"), ("tableau_blocks", "tableaux"),
                                 ("derivation_blocks", "derivations"), ("diagram_blocks", "diagrams"),
                                 ("numbered_environments", "numbered_environments")):
        require(html_receipt[html_key] == source_stats[source_key], f"{source_key} semantic coverage changed")
    audit = {"schema": "openlogic-bn-full-semantic-reader/1", "source_units": 722,
             "status": "structural checks passed; visual QA pending", "source": source_stats,
             "html": html_receipt,
             "pandoc_warnings": [line for line in warnings.splitlines() if line.strip()],
             "method": "সব একক সংযোজিত; নেটিভ MathML, একক-নির্দিষ্ট সূত্রনির্দেশ এবং পুনঃপ্রবাহযোগ্য প্রমাণ/চিত্র। এই রূপান্তরে TeX চালু হয়নি।"}
    reader.write_json(BUILD / "SEMANTIC_READER_QA.json", audit)
    print(json.dumps({"html": str(HTML.relative_to(full.REPO)), "bytes": html_receipt["html_bytes"],
                      "sha256": html_receipt["html_sha256"], "mathml": html_receipt["native_mathml"],
                      "units": html_receipt["unit_markers"], "status": audit["status"]}), flush=True)


if __name__ == "__main__":
    main()
