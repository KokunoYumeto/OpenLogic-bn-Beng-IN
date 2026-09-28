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


def build():
    sources = BUILD / "font-sources"
    sources.mkdir(parents=True, exist_ok=True)
    fonts = {}
    provenance = []
    originals = {}
    for filename in sorted({v[1] for v in GLYPHS.values()}):
        target = sources / filename
        original = pathlib.Path(subprocess.check_output(["kpsewhich", filename], text=True).strip())
        assert original.is_file()
        if not target.exists():
            target.write_bytes(original.read_bytes())
        assert target.read_bytes() == original.read_bytes(), "installed font source changed"
        originals[filename] = original
        font = T1Font(str(target))
        font.parse()
        fonts[filename] = font
        provenance.append({"file": filename, "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                           "font_name": font["FontName"], "font_info": font["FontInfo"]})
    dependencies = []
    for filename in ("ntxsyc.vf", "ntxsyc.tfm", "txsyc.tfm", "stmary10.tfm"):
        original = pathlib.Path(subprocess.check_output(["kpsewhich", filename], text=True).strip())
        assert original.is_file()
        target = sources / filename
        if not target.exists():
            target.write_bytes(original.read_bytes())
        assert target.read_bytes() == original.read_bytes()
        dependencies.append({"file": filename, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()})
    tex_root = originals["txsyc.pfb"].parents[4]
    tx_notice = tex_root / "doc/fonts/txfonts/COPYRIGHT"
    assert tx_notice.is_file()
    tx_target = sources / "TXFONTS-COPYRIGHT.txt"
    if not tx_target.exists():
        tx_target.write_bytes(tx_notice.read_bytes())
    assert tx_target.read_bytes() == tx_notice.read_bytes()
    # The St Mary package documentation names its authors and LPPL 1.0-or-later
    # terms. Keep that primary document with the exact font source archive.
    stmary_doc = originals["stmary10.pfb"].parents[4] / "doc/fonts/stmaryrd/stmaryrd.pdf"
    assert stmary_doc.is_file()
    stmary_target = sources / "stmaryrd.pdf"
    if not stmary_target.exists():
        stmary_target.write_bytes(stmary_doc.read_bytes())
    assert stmary_target.read_bytes() == stmary_doc.read_bytes()
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
