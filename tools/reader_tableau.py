"""Preserve Forest tableau ancestry, sibling branches and schematic nodes."""

import re
import build_cumulative_semantic_reader as reader


def parse_nodes(body):
    nodes = []
    roots = []

    def tree(start, parent):
        identity = len(nodes) + 1
        node = {"id": identity, "parent": parent, "children": [],
                "source_start": start, "source_end": None, "header": ""}
        nodes.append(node)
        if parent is None:
            roots.append(identity)
        else:
            nodes[parent - 1]["children"].append(identity)
        cursor = start + 1
        parts = []
        while cursor < len(body):
            char = body[cursor]
            if char == "\\":
                match = re.match(r"\\(?:[A-Za-z@]+|.)", body[cursor:])
                reader.require(match is not None, "invalid tableau control sequence")
                end = cursor + len(match[0])
                if match[0] in (r"\sFmla", r"\pFmla"):
                    _, end = reader.parse_required(body, end)
                    _, end = reader.parse_required(body, end)
                    if match[0] == r"\pFmla":
                        _, end = reader.parse_required(body, end)
                    # A prefixed running-text formula may have a bracketed
                    # optional argument. Consume it with its macro, rather
                    # than interpreting its world prefix as a child branch.
                    elif body[end:end+1] == "[":
                        _, end = reader.parse_optional(body, end)
                parts.append(body[cursor:end])
                cursor = end
            elif char == "{":
                _, end = reader.parse_delimited(body, cursor, "{", "}")
                parts.append(body[cursor:end])
                cursor = end
            elif char == "[":
                cursor = tree(cursor, identity)
            elif char == "]":
                node["header"] = "".join(parts).strip()
                node["source_end"] = cursor + 1
                return cursor + 1
            else:
                parts.append(char)
                cursor += 1
        raise ValueError(f"unterminated tableau node at {start} in {reader.CURRENT_SOURCE_UNIT}")

    cursor = 0
    while cursor < len(body):
        if body[cursor] == "{":
            _, cursor = reader.parse_delimited(body, cursor, "{", "}")
        elif body[cursor] == "\\":
            match = re.match(r"\\(?:[A-Za-z@]+|.)", body[cursor:])
            reader.require(match is not None, "invalid tableau prefix")
            cursor += len(match[0])
        elif body[cursor] == "[":
            cursor = tree(cursor, None)
        else:
            reader.require(body[cursor] != "]", "unmatched tableau closing bracket")
            cursor += 1
    reader.require(nodes and roots, "tableau has no bracket tree")
    for node in nodes:
        header = node["header"]
        matches = list(re.finditer(r"\\(?:sFmla|pFmla)(?![A-Za-z@])", header))
        reader.require(len(matches) <= 1, "multiple signed formulas in one tableau node")
        node.update(sign=None, formula=None, prefix=None, source_line=None, justification=None)
        if matches:
            cursor = matches[0].end()
            node["sign"], cursor = reader.parse_required(header, cursor)
            node["formula"], cursor = reader.parse_required(header, cursor)
            if matches[0][0] == r"\pFmla":
                node["prefix"], cursor = reader.parse_required(header, cursor)
            else:
                node["prefix"], cursor = reader.parse_optional(header, cursor)
            options = header[cursor:]
        else:
            options = header
        match = re.search(r"(?:^|,)\s*just\s*=", options)
        if match:
            node["justification"], _ = reader.parse_required(options, match.end())
        node["closed"] = bool(re.search(r"(?:^|,)\s*close\s*(?:,|$)", options))
        node["checked"] = bool(re.search(r"(?:^|,)\s*checked\s*(?:,|$)", options))
    return nodes, roots


def transform(value):
    total = 0
    for environment in ("oltableau", "tableau"):
        def convert(body, index, environment=environment):
            nodes, roots = parse_nodes(body)
            entries = []
            for node in nodes:
                detail = f"শীর্ষ {node['id']}"
                detail += f"; পূর্বশীর্ষ {node['parent']}" if node["parent"] else "; মূলশীর্ষ"
                if node["formula"] is not None:
                    detail += ": $" + node["sign"] + r"\;" + node["formula"] + "$"
                elif node["header"].strip():
                    detail += ": " + reader.ensure_math(node["header"].split(",", 1)[0])
                else:
                    detail += ": উৎসে ফাঁকা স্থান"
                if node["prefix"]:
                    detail += " (উপসর্গ $" + node["prefix"] + "$)"
                if node["justification"]:
                    detail += "; কারণ $" + node["justification"] + "$"
                if node["checked"]:
                    detail += "; সূত্রটি ব্যবহৃত"
                if node["closed"]:
                    detail += "; শাখা বন্ধ"
                if len(node["children"]) > 1:
                    detail += "; পৃথক শাখার পরবর্তী শীর্ষ: " + ", ".join(map(str, node["children"]))
                entries.append(detail)
            reader.TABLEAU_GRAPH_RECEIPTS.append({
                "unit_id": reader.CURRENT_SOURCE_UNIT, "environment": environment,
                "tree_index": total + index + 1,
                "source_body_sha256": reader.sha256(body.encode("utf-8")),
                "nodes": nodes, "roots": roots,
            })
            return (
                "\n\\begin{tableau-semantic}\n"
                "\\textbf{ট্যাবলোর পুনঃপ্রবাহযোগ্য শাখা-পাঠ}\n"
                "\\begin{enumerate}\n"
                + "\n".join(r"\item " + entry for entry in entries)
                + "\n\\end{enumerate}\n\\end{tableau-semantic}\n"
            )

        value, count = reader.transform_environments(value, environment, convert)
        total += count
    return value, total
