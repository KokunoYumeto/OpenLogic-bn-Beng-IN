# Bengali reader through Representability in Q — 299 of 722 units

This prerelease publishes the first cumulative semantic reader for the current Bengali (India) draft. It includes every translated unit once: OLP-0004–OLP-0300, OLP-0719, and OLP-0721. The remaining 423 frozen-source units are still untranslated, so this is an in-progress edition rather than a complete Open Logic book.

Read the edition online at [kokunoyumeto.github.io/OpenLogic-bn-Beng-IN](https://kokunoyumeto.github.io/OpenLogic-bn-Beng-IN/).

The reader is available as a standalone offline HTML file and a reflowable EPUB 3. Both formats use embedded Bengali fonts and native MathML. Proof trees, tableaux, derivations, and source diagrams are represented as semantic, reflowable structures. A complete expanded cumulative LaTeX file contains all 299 units without external chapter imports, and the source ZIP preserves the complete editable project snapshot. The build does not use a TeX engine.

Automated validation covered all 299 unit markers, 18,795 MathML expressions, 948 numbered environments, 186 proof trees, 51 tableaux, 7 derivations, 32 diagrams, and 867 internal links. EPUBCheck 5.3.0 reported zero messages. A cold EPUB rebuild was byte-identical. Representative pages throughout the reader were also rendered and visually inspected for Bengali shaping, mathematics, tables of contents, diagrams, tableaux, and boundary units.

No PDF is included because this edition was designed as a semantic, reflowable reader. The online HTML is the directly readable preview.

## Assets

- `openlogic-bn-Beng-IN-through-representability.html` — standalone offline reader
- `openlogic-bn-Beng-IN-through-representability.epub` — validated EPUB 3 reader
- `openlogic-bn-Beng-IN-through-representability.tex` — complete expanded 299-unit cumulative LaTeX source
- `openlogic-bn-Beng-IN-v0.3.0-source.zip` — source snapshot for this release
- `BUILD_QA.json` — machine-readable build and validation receipt
- `SHA256SUMS.txt` — SHA-256 checksums for the release files

The translation and review are model-based. No independent human review is claimed. Open Logic source and translation changes are licensed under CC BY 4.0, subject to the upstream component notices. Embedded Noto Serif Bengali fonts are licensed under the SIL Open Font License 1.1.

Source authority: Open Logic Project revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`; frozen source manifest SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`.
