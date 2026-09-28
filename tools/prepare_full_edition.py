"""Prepare the complete Bengali edition, integrating every source in its chapter.

The translated source files remain unchanged. Rendered labels receive a unit
namespace so alternate historical versions cannot overwrite one another.
"""

from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re

import build_cumulative_semantic_reader as reader

REPO = pathlib.Path(__file__).resolve().parents[1]
BUILD = REPO / "build/full-edition"
MANIFEST = REPO / "evidence/FULL_SOURCE_MANIFEST.jsonl"
FULL_TOKEN_TRANSLATIONS = {
    "proof": "প্রমাণ", "prove": "প্রমাণ", "proving": "প্রমাণ",
    "provable": "প্রমাণযোগ্য", "height": "উচ্চতা", "depth": "গভীরতা",
    "hp": "hp", "introduction": "প্রবর্তন", "elimination": "অপসারণ",
    "parameter": "পরামিতি", "relational model": "সম্পর্কীয় মডেল",
    "lambda define": "ল্যাম্বডা-সংজ্ঞায়িত",
    "lambda defined": "ল্যাম্বডা-সংজ্ঞায়িত",
    "lambda definable": "ল্যাম্বডা-সংজ্ঞায়নযোগ্য",
    "colorC": "লাল", "colorD": "নীল", "colorE": "সবুজ",
    "sentences": "বাক্যগুলি",
}
reader.TOKEN_TRANSLATIONS.update(FULL_TOKEN_TRANSLATIONS)
_noun_inflection = reader.inflect_token


def full_token_inflection(term, plural, suffix, key=""):
    # English present-tense verb s is not a Bengali noun plural.
    if key in {"prove", "lambda define"}:
        plural = False
    return _noun_inflection(term, plural, suffix, key)


reader.inflect_token = full_token_inflection


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def body(raw):
    if r"\begin{document}" not in raw:
        return raw
    return raw.split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]


def normalize_heading_options(raw, uid, notes):
    for name, arity in (("olsection", 1), ("olchapter", 3), ("olpart", 2)):
        def heading(source, position, name=name, arity=arity):
            short, position = reader.parse_optional(source, position)
            args = []
            for _ in range(arity):
                value, position = reader.parse_required(source, position)
                args.append(value)
            if short is not None:
                notes.append({"unit_id": uid, "macro": name, "short_title": short,
                              "long_title": args[-1]})
            return "\\" + name + "".join("{" + arg + "}" for arg in args), position
        raw = reader.replace_macro(raw, name, heading)
    return raw


def restore_exercise_statements(raw, notes):
    """Retain source propositions that the selected exercises explicitly cite."""
    wanted = {"defEx": "prop:sat-ex", "defAll": "prop:sat-all"}

    def branch(source, position):
        tag, position = reader.parse_required(source, position)
        yes, position = reader.parse_required(source, position)
        no, position = reader.parse_required(source, position)
        if tag in wanted and (r"\ollabel{" + wanted[tag] + "}") in yes:
            notes.append({"unit_id": "OLP-0163", "source_label": "fol:syn:sat:" + wanted[tag],
                          "source_condition": tag,
                          "action": "উৎসের মূল প্রস্তাবটি অপরিবর্তিত রেখে সংশ্লিষ্ট অনুশীলনীর আগে দেখানো হয়েছে; অন্য সংজ্ঞা/নির্বাচন-বিধি বদলানো হয়নি।"})
            note = (r"\par\noindent\textnormal{\small পাঠক-টীকা: হিমায়িত উৎসের এই প্রস্তাবটি "
                    r"শর্তসাপেক্ষে আড়াল হয়, যদিও পরের অনুশীলনী সেটির প্রমাণ চায়। "
                    r"অনুশীলনীর বক্তব্য স্পষ্ট রাখতে এখানে উৎসের প্রস্তাবটি দেখানো হয়েছে।}\par")
            return yes + "\n" + note, position
        return r"\iftag{" + tag + "}{" + yes + "}{" + no + "}", position

    return reader.replace_macro(raw, "iftag", branch)


def edition_order(rows):
    """Group detached versions with their subject, never in a separate supplement."""
    parts = [r for r in rows if r["source_role"] == "part_driver" and r["reader_reachable"]]
    proof = next(r for r in rows if r["source_path"] == "content/proof-theory/proof-theory.tex")
    pos = next(i for i, r in enumerate(parts) if "/model-theory/" in r["source_path"])
    parts.insert(pos, proof)
    result = [rows[0], rows[1]]
    for part in parts:
        directory = pathlib.PurePosixPath(part["source_path"]).parent
        candidates = [r for r in rows if pathlib.PurePosixPath(r["source_path"]).is_relative_to(directory)]
        result.append(part)
        chapters = collections.defaultdict(list)
        for row in candidates:
            if row["unit_id"] == part["unit_id"]:
                continue
            chapters[str(pathlib.PurePosixPath(row["source_path"]).parent)].append(row)
        for directory_name, group in sorted(chapters.items(), key=lambda item: min(r["order"] for r in item[1])):
            primary = [r for r in group if r["source_role"] == "chapter_driver" and r["reader_reachable"]]
            if not primary:
                primary = [r for r in group if r["source_role"] == "chapter_driver"][:1]
            if primary:
                result.append(primary[0])
            result.extend(r for r in sorted(group, key=lambda r: r["order"])
                          if not primary or r["unit_id"] != primary[0]["unit_id"])
    ids = [r["unit_id"] for r in result]
    assert len(ids) == len(set(ids)) == 722
    assert set(ids) == {r["unit_id"] for r in rows}
    return result


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    rows = load_rows(MANIFEST)
    status = json.loads((REPO / "evidence/DRAFT_STATUS.json").read_text(encoding="utf-8"))
    assert len(rows) == status["draft_scope"]["translated_count"] == 722
    assert digest(MANIFEST) == reader.MANIFEST_SHA256
    checks = {r["unit_id"]: r for r in status["current_checks"]["unit_checks"]}
    order = edition_order(rows)
    units = {}
    for row in order:
        path = REPO / "bn-Beng-IN" / row["source_path"]
        assert digest(path) == checks[row["unit_id"]]["target_sha256"]
        units[row["unit_id"]] = path.read_text(encoding="utf-8")
    heading_options = []
    render_inputs = {uid: normalize_heading_options(reader.strip_comments(body(raw)), uid, heading_options)
                     for uid, raw in units.items()}
    reader_adjustments = []
    render_inputs["OLP-0163"] = restore_exercise_statements(render_inputs["OLP-0163"], reader_adjustments)
    assert len(reader_adjustments) == 2
    known = reader.collect_known_labels(list(render_inputs.items()))
    selected = {uid: reader.evaluate_selectors(raw, known) for uid, raw in render_inputs.items()}
    for _ in range(4):
        visible = reader.collect_known_labels(list(selected.items()))
        updated = {uid: reader.evaluate_selectors(raw, visible)
                   for uid, raw in render_inputs.items()}
        if updated == selected:
            break
        selected = updated
    else:
        raise RuntimeError("visible-label selector evaluation did not converge")

    owners = collections.defaultdict(list)
    selected_labels = reader.collect_known_labels(list(selected.items()))
    for uid, raw in selected.items():
        for label in reader.collect_known_labels([(uid, raw)]):
            owners[label].append(uid)
        for label in re.findall(r"\\label\{([^{}]+)\}", raw):
            if uid not in owners[label]:
                owners[label].append(uid)
        if r"\olfileid" not in raw:
            for label in re.findall(r"\\ollabel\{([^{}]+)\}", raw):
                if uid not in owners[label]:
                    owners[label].append(uid)
    # Shared first-order source modules have both PL and FOL reference names.
    aliases = {}
    for label in list(owners):
        if label.endswith(":part") and label.count(":") == 1:
            aliases[label.split(":")[0] + ":::part"] = label
        if label.endswith(":chap") and label.count(":") == 2:
            aliases[label.rsplit(":", 1)[0] + "::chap"] = label
        if label.startswith("fol:"):
            other = "pl:" + label[4:]
            if other not in owners:
                aliases[other] = label
    known = set(owners) | set(aliases) | selected_labels
    # A wrapper-free rule table has a plain tab:... label, while its
    # containing section often uses an olref-qualified spelling.
    for uid, value in selected.items():
        probe = reader.literalize_string_commands(value)
        preliminary = reader.normalize_cross_references(probe, uid, known)
        for missing in re.findall(r"বর্তমান পাঠের বাইরের সূত্র \(([^)]+)\)", preliminary):
            local = ":".join(missing.split(":")[-2:])
            if local.startswith("tab:") and local in owners and len(owners[local]) == 1:
                aliases[missing] = local
    known |= set(aliases)
    unresolved = []
    proof_title_reference_adjustments = []
    caption_reference_adjustments = []
    display_blank_line_adjustments = []
    tabular_spacing_adjustments = []
    documented_missing = []
    label_map = []
    transformed = []
    primary_chapters = set()
    for row in order:
        uid = row["unit_id"]
        render_source = selected[uid]
        render_source = re.sub(
            r"(!!\^?a?\{)([^{}]+)(\})",
            lambda m: m[1] + " ".join(m[2].split()) + m[3],
            render_source,
        )
        # Source-correction notes quote literal macro spellings with escaped
        # braces. These are code examples, not active OpenLogic text tokens.
        render_source = render_source.replace(r"!!\{", r"\string!\string!\{")
        if uid == "OLP-0718":
            literal = "অসম্পূর্ণ ভাষাগত !! চিহ্ন"
            assert render_source.count(literal) == 1
            render_source = render_source.replace(
                literal, r"অসম্পূর্ণ ভাষাগত \string!\string! চিহ্ন", 1
            )
        try:
            raw = reader.replace_tokens(render_source)
        except Exception as exc:
            fragments = re.findall(r".{0,35}!!.{0,55}", render_source)
            raise RuntimeError(f"{uid}: token expansion failed; examples {fragments[-5:]}") from exc
        raw = reader.literalize_string_commands(raw)
        raw = raw.replace("!!", r"\string!\string!")
        if uid == "OLP-0349":
            assert raw.count(r"$\num$") == 1
            raw = raw.replace(r"$\num$", r"\texttt{\textbackslash num}")
            reader_adjustments.append({"unit_id": uid, "source_correction": "BN-SRC-270",
                                       "action": "সংশোধন-টীকায় উদ্ধৃত আর্গুমেন্টহীন ম্যাক্রো-নামটি গণিত হিসেবে সক্রিয় না করে কোডরূপে দেখানো হয়েছে।"})
        if uid == "OLP-0702":
            old = r"\UnaryInf$!D, !C \fCenter !E, !C$" + "\n" + r"\]"
            assert raw.count(old) == 1
            note = (r"\par\noindent\textnormal{\small পাঠক-টীকা: হিমায়িত উৎসে এই "
                    r"সংক্ষিপ্ত প্রমাণটির শেষে \texttt{\textbackslash DisplayProof} অনুপস্থিত। "
                    r"উৎসে দেওয়া অনুমান ও সিদ্ধান্তগুলি দৃশ্যমান করতে প্রদর্শন-নির্দেশটি যোগ করা হয়েছে।}\par")
            raw = raw.replace(old, old[:-2] + r"\DisplayProof" + "\n" + r"\]" + "\n" + note)
            reader_adjustments.append({"unit_id": uid, "source_path": row["source_path"],
                                       "action": "একটি সংক্ষিপ্ত প্রমাণে উৎসের অনুপস্থিত DisplayProof নির্দেশ যোগ করা হয়েছে; কোনো অনুমান, সিদ্ধান্ত বা বিধি বদলানো হয়নি।"})
        if uid == "OLP-0660":
            # This source fragment inherits its part from the cut-elimination
            # chapter instead of declaring an olfileid of its own.
            raw = r"\olfileid{pt}{cut}{int}" + "\n" + raw
        raw = reader.normalize_cross_references(raw, uid, known)
        raw = reader.normalize_structural_macros(raw, preserve_proof_layout=True)
        raw = reader.normalize_bengali_token_suffixes(raw)
        chapter_id = re.search(r"\\olchapter\{([^{}]+)\}\{([^{}]+)\}", selected[uid])
        chapter_key = chapter_id.groups() if chapter_id else (uid,)
        if row["source_role"] == "chapter_driver":
            if chapter_key in primary_chapters:
                raw = re.sub(r"\\chapter\{", r"\\section{বিকল্প অধ্যায়-বিন্যাস: ", raw, count=1)
            else:
                primary_chapters.add(chapter_key)
        elif row["source_role"] == "part_driver" and not row["reader_reachable"] and "/proof-theory/" not in row["source_path"]:
            raw = re.sub(r"\\part\{", r"\\section{বিকল্প অংশ-বিন্যাস: ", raw, count=1)

        def physical_label(match):
            old = match.group(2)
            if old.startswith(":::") and old[3:] in owners:
                old = old[3:]
            new = uid.lower() + ":" + old
            label_map.append({"unit_id": uid, "source_label": old, "reader_label": new})
            return "\\" + match.group(1) + "{" + new + "}"

        raw = re.sub(r"\\(label|hypertarget)\{([^{}]+)\}", physical_label, raw)

        def missing_reference_note(old):
            expected = {f"fol:{method}:prv:prop:provability-lor-{side}"
                        for method in ("seq", "ntd") for side in ("left", "right")}
            assert uid == "OLP-0644" and old in expected, (uid, old)
            assert old not in known
            unresolved.append({"unit_id": uid, "source_label": old})
            documented_missing.append({"unit_id": uid, "source_label": old,
                                       "status": "এই নামের প্রস্তাব হিমায়িত উৎসে নেই; অপ্রাসঙ্গিক প্রস্তাবে নির্দেশ ঘোরানো হয়নি।"})
            label_text = old.replace(":", r":\allowbreak ")
            return (r"\textnormal{সূত্রনির্দেশ-টীকা}\footnote{হিমায়িত ইংরেজি উৎসে "
                    r"\texttt{" + label_text + r"} নামের প্রস্তাবটির সংজ্ঞা নেই। "
                    r"উৎসের এই নির্দেশটি অমীমাংসিত হিসেবে নথিভুক্ত।}")

        def physical_reference(match):
            old = match.group(2)
            canonical = aliases.get(old, old)
            candidates = owners.get(canonical, [])
            owner = uid if uid in candidates else (candidates[0] if candidates else None)
            if not owner:
                return missing_reference_note(old)
            return "\\" + match.group(1) + "{" + owner.lower() + ":" + canonical + "}"

        raw = re.sub(r"\\(hyperlink|ref|eqref|cref|Cref)\{([^{}]+)\}", physical_reference, raw)
        def stable_caption_reference(match):
            target = match.group(1)
            assert ":thm:" in target or ":fig:" in target, (uid, target)
            short = "সংশ্লিষ্ট উপপাদ্যের মডেল" if ":thm:" in target else "সংশ্লিষ্ট চিত্রের ফিল্ট্রেশন"
            caption_reference_adjustments.append({"unit_id": uid, "target": target,
                "action": "চিত্রশিরোনামের লিখিত সংক্ষিপ্ত রূপে ভঙ্গুর hyperlink বাদ; দৃশ্যমান শিরোনামে মূল সংযোগ অক্ষত।"})
            return (r"\caption[" + short + r"]{\protect\hyperlink{" + target
                    + r"}{দেখুন}" + match.group(2) + "}")
        raw = re.sub(r"\\caption\{\\hyperlink\{([^{}]+)\}\{দেখুন\}([^{}]*)\}",
                     stable_caption_reference, raw)
        def proof_title(match):
            def stable_reference(link):
                assert link.group(2) == "দেখুন", (uid, link.group(2))
                proof_title_reference_adjustments.append({"unit_id": uid, "target": link.group(1),
                    "action": "প্রমাণ-শিরোনামের ভঙ্গুর hyperlink-এর বদলে একই লক্ষ্যযুক্ত স্বয়ংক্রিয় ref; মূল ফল অপরিবর্তিত।"})
                return r"\ref{" + link.group(1) + "}"
            return re.sub(r"\\hyperlink\{([^{}]+)\}\{([^{}]+)\}", stable_reference, match.group(0))
        raw = re.sub(r"(?m)^\\begin\{proof\}\[[^\n]*\]", proof_title, raw)
        for heading in (h for h in heading_options if h["unit_id"] == uid):
            command = {"olsection": "section", "olchapter": "chapter", "olpart": "part"}[heading["macro"]]
            long = reader.replace_tokens(heading["long_title"])
            short = reader.replace_tokens(heading["short_title"])
            old = "\\" + command + "{" + long + "}"
            if old in raw:
                raw = raw.replace(old, "\\" + command + "[" + short + "]{" + long + "}", 1)
        for missing in re.findall(r"বর্তমান পাঠের বাইরের সূত্র \(([^)]+)\)", raw):
            raw = raw.replace("বর্তমান পাঠের বাইরের সূত্র (" + missing + ")", missing_reference_note(missing))
        def display_without_paragraph(match):
            blanks = re.findall(r"\n[ \t]*\n", match.group(2))
            if blanks:
                display_blank_line_adjustments.append({"unit_id": uid, "environment": match.group(1),
                    "blank_paragraphs_removed": len(blanks),
                    "action": "গাণিতিক প্রদর্শনের ভিতর অনিচ্ছাকৃত ফাঁকা অনুচ্ছেদ সরানো; সমীকরণ অপরিবর্তিত।"})
            body = re.sub(r"\n(?:[ \t]*\n)+", "\n", match.group(2))
            return r"\begin{" + match.group(1) + "}" + body + r"\end{" + match.group(1) + "}"
        raw = re.sub(r"\\begin\{(align\*?|gather\*?|multline\*?|equation\*?|array)\}(.*?)\\end\{\1\}",
                     display_without_paragraph, raw, flags=re.S)
        def adjacent_table_break(match):
            tabular_spacing_adjustments.append({"unit_id": uid,
                "action": "দুটি সত্যসারণির মাঝের উৎস-লাইনবিরতির আগে অনিচ্ছাকৃত অনুচ্ছেদ-সমাপ্তি সরানো; বিরতি ও সারণি অপরিবর্তিত।"})
            return match.group(1) + "\n" + match.group(2)
        raw = re.sub(r"(\\end\{tabular\})\n(?:[ \t]*\n)+(\\\\\[[0-9.]+(?:em|ex|pt)\])",
                     adjacent_table_break, raw)
        transformed.append((row, raw))
    assert len(documented_missing) == 4
    assert len(proof_title_reference_adjustments) == 6
    assert sum(item["blank_paragraphs_removed"] for item in display_blank_line_adjustments) == 9
    assert len(tabular_spacing_adjustments) == 1

    token_setup = "\n".join(r"\settexttoken{" + key + "}{" + value + "}{" + value + "}"
                            for key, value in reader.TOKEN_TRANSLATIONS.items())
    captions = {
        "theorem": "উপপাদ্য", "example": "উদাহরণ", "definition": "সংজ্ঞা",
        "lemma": "সহায়ক উপপাদ্য", "proposition": "প্রস্তাব", "corollary": "অনুসিদ্ধান্ত",
        "problem": "অনুশীলন", "problems": "অনুশীলন", "remark": "মন্তব্য",
        "axiom": "স্বতঃসিদ্ধ", "note": "টীকা", "case": "ক্ষেত্র",
        "convention": "রীতি", "history": "ঐতিহাসিক টীকা", "reading": "অতিরিক্ত পাঠ",
        "photocredits": "ছবির স্বীকৃতি", "appendix": "পরিশিষ্ট", "appendices": "পরিশিষ্ট",
        "OLP": "ওপেন লজিক প্রকল্প", "OLT": "ওপেন লজিক পাঠ",
    }
    caption_setup = "\n".join(r"\setlocalecaption{english}{" + key + "}{" + value + "}"
                              for key, value in captions.items())
    preamble = r"""\documentclass[11pt,a4paper,openany]{memoir}
\usepackage[margin=22mm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\newfontfamily\latinfont{Latin Modern Roman}
\newfontfamily\bengalifont{NotoSerifBengali-Regular.ttf}[Path=../../fonts/,Script=Bengali,BoldFont=NotoSerifBengali-Bold.ttf,ItalicFont=NotoSerifBengali-Regular.ttf,BoldItalicFont=NotoSerifBengali-Bold.ttf,ItalicFeatures={FakeSlant=0.15}]
\usepackage[Bengali,DevanagariDanDa,BasicLatin,GeneralPunctuation]{ucharclasses}
\setTransitionsFor{Bengali}{\bengalifont}{\latinfont}
\setTransitionsFor{DevanagariDanDa}{\bengalifont}{\latinfont}
\newcommand{\olpath}{../../upstream}
\input{\olpath/sty/open-logic.sty}
"""
    preamble += caption_setup + "\n" + token_setup + "\n"
    # Keep exercises in place. The upstream defer package would move them
    # into chapter hooks that are deliberately suppressed in this assembly.
    preamble += r"""\includeenv{editorial}
\tagtrue{""" + ",".join(sorted(reader.TRUE_TAGS)) + r"""}
\tagfalse{""" + ",".join(sorted(reader.FALSE_TAGS)) + r"""}
\input{\olpath/open-logic-complete-config.sty}
\hypersetup{pdftitle={ওপেন লজিক: সম্পূর্ণ ভারতীয় বাংলা উৎসসংস্করণ},pdfauthor={Open Logic Project; OpenAI Codex},pdfsubject={bn-Beng-IN; 722 source units}}
\setlength{\emergencystretch}{3em}
\renewcommand{\contentsname}{সূচিপত্র}
\renewcommand{\chaptername}{অধ্যায়}
\renewcommand{\partname}{অংশ}
\renewcommand{\figurename}{চিত্র}
\renewcommand{\tablename}{সারণি}
\renewcommand{\proofname}{প্রমাণ}
\linespread{1.16}
\begin{document}
% open-logic.sty selects English at begin-document, restoring Babel's
% default captions after the preamble assignments above.
\renewcommand{\contentsname}{সূচিপত্র}
\renewcommand{\chaptername}{অধ্যায়}
\renewcommand{\partname}{অংশ}
\renewcommand{\figurename}{চিত্র}
\renewcommand{\tablename}{সারণি}
\renewcommand{\proofname}{প্রমাণ}
\begin{titlingpage}
\centering{\Huge ওপেন লজিক\par}\bigskip
{\LARGE বাংলা (ভারত)\par}\bigskip
সম্পূর্ণ ৭২২-ইউনিট উৎসসংস্করণ\par
\vfill
এআই-সহায়ক অনুবাদ, সংশোধন ও স্বয়ংক্রিয় পর্যালোচনা\par
OpenAI Codex: GPT-5.6 Sol এবং GPT-6 Sol; Ultra effort\par
স্বাধীন মানব-পর্যালোচনা দাবি করা হচ্ছে না।\par
\end{titlingpage}
\tableofcontents
"""
    row_by_id = {row["unit_id"]: row for row, _ in transformed}
    text_by_id = {row["unit_id"]: text for row, text in transformed}
    id_by_path = {row["source_path"]: row["unit_id"] for row in order}
    imports = []
    imported_targets = set()

    def imported_id(uid, name):
        path = pathlib.PurePosixPath(row_by_id[uid]["source_path"]).parent / name
        if path.suffix != ".tex":
            path = path.with_suffix(".tex")
        target = id_by_path[path.as_posix()]
        assert row_by_id[target]["source_role"] == "auxiliary_fragment", (uid, target)
        return target

    for uid, text in text_by_id.items():
        for name in re.findall(r"\\subfile\{([^{}]+)\}", text):
            target = imported_id(uid, name)
            imports.append({"unit_id": uid, "included_unit_id": target, "source_argument": name,
                            "action": "সম্পর্কিত উৎসের আমদানি-স্থানে বাংলা সূত্রসারণি একবার সংযোজিত।"})
            imported_targets.add(target)
    emitted = []

    def emit(uid):
        if uid in emitted:
            return r"\hyperlink{unit-" + uid.lower() + "}{পূর্বে সংযোজিত সূত্রসারণি দেখুন}"
        emitted.append(uid)
        row = row_by_id[uid]

        def include(source, position):
            name, position = reader.parse_required(source, position)
            return emit(imported_id(uid, name)), position

        text = reader.replace_macro(text_by_id[uid], "subfile", include)
        return ("\n% SOURCE-UNIT " + uid + " " + row["source_path"] + "\n"
                + r"\hypertarget{unit-" + uid.lower() + "}{}\n" + text
                + "\n% END-SOURCE-UNIT " + uid + "\n")

    parts = [preamble]
    for row, _ in transformed:
        uid = row["unit_id"]
        if uid not in imported_targets and uid not in emitted:
            parts.append(emit(uid))
    assert len(emitted) == len(set(emitted)) == 722
    assert set(emitted) == set(row_by_id)
    assert len(caption_reference_adjustments) == 3
    parts.append(r"""
\bibliographystyle{plainnat}
\bibliography{../../upstream/bib/open-logic}
\end{document}
""")
    tex = BUILD / "openlogic-bn-Beng-IN-complete.tex"
    tex.write_text("\n".join(parts), encoding="utf-8", newline="\n")
    receipt = {
        "schema": "openlogic-bn-full-edition-preparation/1",
        "source_revision": reader.SOURCE_REVISION,
        "source_manifest_sha256": digest(MANIFEST),
        "draft_status_sha256": digest(REPO / "evidence/DRAFT_STATUS.json"),
        "source_units": 722,
        "reader_order": emitted,
        "integrated_source_imports": imports,
        "tex": {"path": tex.relative_to(REPO).as_posix(), "bytes": tex.stat().st_size,
                "sha256": digest(tex)},
        "label_map": label_map,
        "reference_aliases": aliases,
        "heading_options": heading_options,
        "full_token_translations": FULL_TOKEN_TRANSLATIONS,
        "token_governance": "T072/T077/T081/T122/T315/T437/T444/T446/T447; exact source predicates and definitions govern specialist terms; no new direct canon attestation is claimed.",
        "unresolved_references": unresolved,
        "documented_missing_source_references": documented_missing,
        "reader_adjustments": reader_adjustments,
        "proof_title_reference_adjustments": proof_title_reference_adjustments,
        "caption_reference_adjustments": caption_reference_adjustments,
        "display_blank_line_adjustments": display_blank_line_adjustments,
        "tabular_spacing_adjustments": tabular_spacing_adjustments,
        "status": "prepared; compilation, semantic HTML and visual QA pending",
    }
    (BUILD / "PREPARATION.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ("source_units", "tex", "status")}
                     | {"labels": len(label_map), "unresolved_references": len(unresolved)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
