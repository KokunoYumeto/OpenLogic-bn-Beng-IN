"""Preserve three project operator glyphs in an offline, reproducible HTML font."""

import hashlib
import json
import pathlib
import subprocess

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.t1Lib import T1Font

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / "build/full-edition"
GLYPHS = {
    "boxright": (0xE000, "txsyc.pfb", 128, "squareright"),
    "fishhookright": (0xE001, "txsyc.pfb", 74, "strict"),
    "leftrightarroweq": (0xE002, "stmary10.pfb", 45, "leftrightarroweq"),
}
SOURCE_HASHES = {
    "txsyc.pfb": "daba10834af8bf5dcb3c6b03e919daf61e6ba74c3ef71aa3c74f80dc3945ec5e",
    "stmary10.pfb": "eff077f7d9ca7c2f02695e1c51bb97327f097dbdf6b2677579772bcd4f6a6844",
    "ntxsyc.vf": "449dc24da3c0178168ce444d1a0fe47a17e7b55e9c787b23bc477f0b46e8e7e4",
    "ntxsyc.tfm": "29f01929af4a75a146bee9243b61b58e42e8829af9fa06a558e4c572d2467e39",
    "txsyc.tfm": "ec685ceaf907aaf2f8bf955969de391cd8e91a9d6a63a8a06c006313f5c54a1d",
    "stmary10.tfm": "9c41cd0d9cfb12c5f7ed6dccfe0367be6378e5b755a5b22424c47b975b57af8f",
    "TXFONTS-COPYRIGHT.txt": "339ed0e30e6fe614a7a677f1c77e6d0736a7822b23c2a43cc046fac43bb80d63",
    "stmaryrd.pdf": "7db46cdb142097ab0151aaa976db1a3b3761b498bd80ba26e4ecb90ceaff7826",
}


def build():
    sources = BUILD / "font-sources"
    sources.mkdir(parents=True, exist_ok=True)
    fonts = {}
    provenance = []
    originals = {}
    def retained_source(filename, locate):
        target = sources / filename
        if not target.exists():
            original = locate()
            assert original.is_file(), filename
            data = original.read_bytes()
            assert hashlib.sha256(data).hexdigest() == SOURCE_HASHES[filename], "installed source differs: " + filename
            target.write_bytes(data)
        assert hashlib.sha256(target.read_bytes()).hexdigest() == SOURCE_HASHES[filename], "retained source differs: " + filename
        return target
    def installed(filename):
        original = pathlib.Path(subprocess.check_output(["kpsewhich", filename], text=True).strip())
        assert original.is_file(), filename
        originals[filename] = original
        return original
    for filename in sorted({v[1] for v in GLYPHS.values()}):
        target = retained_source(filename, lambda filename=filename: installed(filename))
        font = T1Font(str(target))
        font.parse()
        fonts[filename] = font
        provenance.append({"file": filename, "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                           "font_name": font["FontName"], "font_info": font["FontInfo"]})
    dependencies = []
    for filename in ("ntxsyc.vf", "ntxsyc.tfm", "txsyc.tfm", "stmary10.tfm"):
        target = retained_source(filename, lambda filename=filename: installed(filename))
        dependencies.append({"file": filename, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()})
    tx_target = retained_source("TXFONTS-COPYRIGHT.txt", lambda: installed("txsyc.pfb").parents[4] / "doc/fonts/txfonts/COPYRIGHT")
    # The St Mary package documentation names its authors and LPPL 1.0-or-later
    # terms. Keep that primary document with the exact font source archive.
    stmary_target = retained_source("stmaryrd.pdf", lambda: installed("stmary10.pfb").parents[4] / "doc/fonts/stmaryrd/stmaryrd.pdf")
    licenses = [
        {"file": tx_target.name, "sha256": hashlib.sha256(tx_target.read_bytes()).hexdigest(),
         "terms": "TX fonts GPL with June 2002 document-embedding exception; original notice retained"},
        {"file": stmary_target.name, "sha256": hashlib.sha256(stmary_target.read_bytes()).hexdigest(),
         "terms": "St Mary's Road font and package LPPL 1.0 or later; original documentation retained",
         "primary_documentation_url": "https://tug.ctan.org/fonts/stmaryrd/stmaryrd.pdf"},
    ]
    outputs = {}
    font_receipts = []
    for source_filename in sorted(fonts):
        selected = {name: spec for name, spec in GLYPHS.items() if spec[1] == source_filename}
        order = [".notdef", *selected]
        outlines = {}
        metrics = {}
        for name in order:
            pen = TTGlyphPen(None)
            if name == ".notdef":
                width = 500
            else:
                _, filename, code, glyph_name = selected[name]
                font = fonts[filename]
                assert font["Encoding"][code] == glyph_name
                char = font["CharStrings"][glyph_name]
                char.draw(Cu2QuPen(pen, 0.5, reverse_direction=True))
                width = round(char.width)
            outlines[name] = pen.glyph()
            metrics[name] = (width, 0)
        stem = "OpenLogicReaderTXOperators" if source_filename == "txsyc.pfb" else "OpenLogicReaderStMaryOperators"
        builder = FontBuilder(1000, isTTF=True)
        builder.setupGlyphOrder(order)
        builder.setupCharacterMap({spec[0]: name for name, spec in selected.items()})
        builder.setupGlyf(outlines)
        builder.setupHorizontalMetrics(metrics)
        builder.setupHorizontalHeader(ascent=900, descent=-250)
        builder.setupNameTable({"familyName": stem, "styleName": "Regular",
                               "uniqueFontIdentifier": stem + " 1.0", "fullName": stem, "psName": stem,
                               "version": "Version 1.0",
                               "copyright": "Original " + fonts[source_filename]["FontName"] + "; see preserved Type 1 metadata and licence."})
        builder.setupOS2(sTypoAscender=900, sTypoDescender=-250, usWinAscent=900, usWinDescent=250)
        builder.setupPost()
        builder.setupMaxp()
        builder.font.recalcTimestamp = False
        builder.font["head"].created = builder.font["head"].modified = 3873398400
        path = BUILD / (stem + ".ttf")
        builder.save(path)
        outputs.update({name: path for name in selected})
        font_receipts.append({"file": path.name, "bytes": path.stat().st_size,
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                              "source_font": source_filename})
    receipt = {"schema": "openlogic-reader-operator-font/1", "sources": provenance,
               "source_dependencies": dependencies, "license_documents": licenses,
               "virtual_slot_mapping": "ntxsyc.vf slot 128 -> txsyc slot 128; slot 74 -> txsyc slot 74, verified from vftovp and the retained virtual/metric files. St Mary slot 45 is declared as leftrightarroweq in stmaryrd.sty.",
               "glyphs": {name: {"codepoint": hex(spec[0]), "source_font": spec[1],
                                  "source_slot": spec[2], "source_glyph": spec[3]}
                          for name, spec in GLYPHS.items()},
               "ttf_fonts": font_receipts,
               "conversion": "মূল Type 1 সংকেতের রেখা সংরক্ষিত; TTF রূপান্তরে সর্বাধিক ০.৫/১০০০ em বক্ররেখা-ত্রুটি। গণিতের সংকেত বদলানো হয়নি।"}
    (BUILD / "OPERATOR_FONT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return outputs


if __name__ == "__main__":
    build()
