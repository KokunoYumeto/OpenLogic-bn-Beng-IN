# Rebuilding the retained operator fonts

The source collection already contains the exact Type 1 outlines, metric
and virtual files, and primary licence documents used for the reader's
three special operators. The font builder nevertheless called `kpsewhich`
and required installed copies on every rebuild. It now checks the retained
files against explicit SHA-256 pins and uses them directly. First bootstrap
still requires the same pinned installed sources when retained files are absent.

An actual font rebuild with every installed-source subprocess lookup
forbidden produced identical bytes for both operator TTF files and the
font-provenance receipt. The current inspected HTML and EPUB glyphs are
unchanged. This verifies the concrete archive dependency repair, not a
claim of a new mathematical or translation correction.
