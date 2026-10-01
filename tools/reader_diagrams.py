"""Retain named and unnamed TikZ nodes, positions and labelled paths in text."""
import re
import build_cumulative_semantic_reader as reader


def node_records(body):
    records = []
    pattern = re.compile(r"\\(?:node|path\s+node)(?![A-Za-z@])")
    for match in pattern.finditer(body):
        cursor = reader.skip_space(body, match.end())
        options = []
        identity = None
        position = None
        while cursor < len(body):
            if body[cursor] == "[":
                option, cursor = reader.parse_delimited(body, cursor, "[", "]")
                options.append(option)
            elif body[cursor] == "(":
                item, cursor = reader.parse_delimited(body, cursor, "(", ")")
                reader.require(identity is None, "multiple diagram node identities")
                identity = item
            elif body[cursor:cursor+2] == "at" and not body[cursor+2:cursor+3].isalpha():
                cursor = reader.skip_space(body, cursor+2)
                reader.require(body[cursor:cursor+1] == "(", "diagram node location missing")
                position, cursor = reader.parse_delimited(body, cursor, "(", ")")
            elif body[cursor] == "{":
                label, cursor = reader.parse_delimited(body, cursor, "{", "}")
                records.append({"id": identity, "position": position, "options": options,
                                "label": label, "source_start": match.start(), "source_end": cursor})
                break
            else:
                raise ValueError("unrecognized diagram node header in " + reader.CURRENT_SOURCE_UNIT + ": " + body[cursor:cursor+90])
            cursor = reader.skip_space(body, cursor)
        else:
            raise ValueError("unterminated diagram node in " + reader.CURRENT_SOURCE_UNIT)
    return records


def convert(body, index):
    nodes = node_records(body)
    entries = []
    for node in nodes:
        label = reader.clean_tikz_text(node["label"])
        entry = "শীর্ষ"
        if node["id"]:
            entry += " " + node["id"]
        entry += ": " + (label if label else "লেবেল নেই")
        if node["position"]:
            entry += "; অবস্থান (" + node["position"] + ")"
        if node["options"]:
            entry += "; অবস্থান ও অন্যান্য চিহ্ন: " + reader.clean_tikz_text(", ".join(node["options"]))
        entries.append(entry)
    paths = []
    for match in re.finditer(r"\\(clip|filldraw|fill|shade|path|draw|coordinate)\b(.*?);", body, re.S):
        command, geometry = match[1], match[2]
        if command == "path" and re.match(r"\s*node\b", geometry):
            continue
        description = reader.clean_tikz_text(geometry)
        if description:
            before = body[:match.start()]
            depth = len(re.findall(r"\\begin\{scope\}", before)) - len(re.findall(r"\\end\{scope\}", before))
            scope = f" (স্থানীয় পরিসর {depth})" if depth else ""
            kind = {"clip": "ছাঁটের সীমানা", "filldraw": "ভরাট ও অঙ্কিত অঞ্চল",
                    "fill": "ভরাট অঞ্চল", "shade": "ছায়াযুক্ত অঞ্চল",
                    "path": "পথ বা নির্মাণ", "draw": "সংযোগ বা নির্দেশ",
                    "coordinate": "স্থানাঙ্কের পরিচয়"}[command]
            entries.append(f"{kind}{scope}: {description}")
            paths.append({"command": command, "geometry": geometry, "scope_depth": depth})
    reader.DIAGRAM_GRAPH_RECEIPTS.append({
        "unit_id": reader.CURRENT_SOURCE_UNIT, "diagram_index": index+1,
        "source_body_sha256": reader.sha256(body.encode("utf-8")),
        "nodes": nodes, "paths": paths,
        "scope_declarations": re.findall(r"\\begin\{scope\}(?:\[[^\]]*\])?", body),
        "representation": "textual coordinates and paths; geometric layout remains in the PDF",
    })
    if not entries:
        entries = ["উৎসচিত্রে কোনো পৃথক পাঠ্য-লেবেল নেই; পার্শ্ববর্তী অনুচ্ছেদ চিত্রটির গাণিতিক ভূমিকা ব্যাখ্যা করে।"]
    return ("\n\\begin{diagram-semantic}\n\\textbf{চিত্রের পুনঃপ্রবাহযোগ্য পাঠ্যরূপ}\n"
            "\\begin{itemize}\n" + "\n".join(r"\item " + entry for entry in entries)
            + "\n\\end{itemize}\n\\end{diagram-semantic}\n")
