"""Assign stable numeric sort keys using Windows' Bengali (India) collation."""
from argparse import ArgumentParser
from pathlib import Path
from functools import cmp_to_key
import ctypes
import json
import re
import unicodedata


def group(text, start):
    depth = 1
    i = start + 1
    while i < len(text):
        c = text[i]
        if c == "\\" and i + 1 < len(text) and text[i + 1] in "{}":
            i += 2
            continue
        if c == "{":
            depth += 1
        if c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError("Unbalanced entry")


parser = ArgumentParser(description=__doc__)
parser.add_argument("glossary", type=Path)
parser.add_argument("receipt", type=Path)
parser.add_argument("--headwords", type=Path)
args = parser.parse_args()
provided = json.loads(args.headwords.read_text(encoding="utf-8")) if args.headwords else {}
text = args.glossary.read_text(encoding="utf-8")
text = re.sub(r"(?m)^[ \t]*sort=\{বিকল্প\},[ \t]*\n", "", text)
entries = {}
markers = {}
for m in re.finditer(r"(?m)^\\newglossaryentry\{([^{}\n]+)\}\s*\{", text):
    key = m[1]
    assert key not in entries
    block, _ = group(text, m.end() - 1)
    name = re.search(r"(?:^|,)\s*name\s*=\s*\{", block)
    headword = group(block, name.end() - 1)[0]
    # The glossary has the literal variable name in its x-variant headword.
    # Compare that name as the Bengali letter name, without changing display.
    collation_headword = provided.get(key, {}).get("sort_bn", headword.replace("$x$", "এক্স"))
    assert not re.search(r"[\\$]", collation_headword), (key, headword)
    assert not re.search(r"(?:^|,)\s*sort\s*=", block), key
    entries[key] = unicodedata.normalize("NFC", collation_headword)
    markers[key] = m.end()
assert len(entries) == 79

compare = ctypes.windll.kernel32.CompareStringEx
compare.argtypes = [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_int,
                    ctypes.c_wchar_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
compare.restype = ctypes.c_int
def order(a, b):
    result = compare("bn-IN", 0, entries[a], -1, entries[b], -1, None, None, 0)
    if result not in (1, 2, 3):
        raise OSError("Bengali (India) collation unavailable")
    return (result - 2) or ((a > b) - (a < b))

keys = sorted(entries, key=cmp_to_key(order))
assert all(order(a, b) < 0 for a, b in zip(keys, keys[1:]))
rank = {key: index for index, key in enumerate(keys, 1)}
for key, position in sorted(markers.items(), key=lambda item: item[1], reverse=True):
    text = text[:position] + f"sort={{bn{rank[key]:03d}}}," + text[position:]
args.glossary.write_text(text, encoding="utf-8", newline="\n")
receipt = {"locale": "bn-IN", "method": "Windows NLS CompareStringEx; stable ASCII build keys",
           "keys": keys, "headwords": [entries[key] for key in keys]}
args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8", newline="\n")
print(json.dumps({"entries": len(keys), "first": keys[0], "last": keys[-1]}))
