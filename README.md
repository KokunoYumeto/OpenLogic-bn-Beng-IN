# ওপেন লজিক — বাংলা (ভারত)

OpenLogic-এর ভারতীয় বাংলা সংস্করণ তৈরির চলমান প্রকল্প। সম্পূর্ণ উৎসের ৭২২টি TeX একক অনুবাদ করাই লক্ষ্য। এই সংস্করণে সেট ও সম্পর্ক অধ্যায়ের ১৮টি উৎস-ফাইল অনূদিত: OLP-0004–OLP-0019, OLP-0719 এবং OLP-0721। পূর্ণাঙ্গ সংস্করণ এখনও সম্পূর্ণ হয়নি; ৭০৪টি ফাইলের অনুবাদ বাকি।

This is an **in-progress, machine-translated Bengali (India) edition**. The cumulative reader covers Sets and Relations: 15 prose sections, two chapter drivers and one alternate Relations driver, totaling 18 translated source files. The alternate driver is provided as a configuration without duplicating its chapter. The superseded Sets proof explanation appears with its subject and original editorial note. All exercises, captions, mathematical examples and philosophical prose in these files are translated. Another 704 source files remain untranslated; the complete frozen corpus remains the objective.

Source authority: [Open Logic Project](https://github.com/OpenLogicProject/OpenLogic), revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. `upstream/` preserves the pristine English archive, including all 722 content files and upstream/component licenses. `bn-Beng-IN/content/` contains source-aligned translations. English files in `upstream/` are **not** counted as translations.

International programme: [OpenLogic translations hub](https://github.com/KokunoYumeto/OpenLogic-translations). This edition links back to the hub; hub maintenance belongs to its programme coordinator.

## Evidence and review

West Bengal university mathematics is represented by NSOU's EMT-03 Bengali algebra/set-theory material. SCERT Tripura's Bengali Class XI mathematics workbook is a separately labelled regional witness. Official Suri Vidyasagar College philosophy readings provide university-level quantification terminology. See `evidence/` for source identities, page/image hashes, passage roles, provisional term decisions and actual consultation records. These witnesses inform Bengali usage; OpenLogic determines the mathematics. No Bangladesh source has silently replaced Indian Bengali evidence.

Recovered West Bengal Class VII and Tripura Class VI materials were freshly verified and four original pages visually read. They add arithmetic terminology and explanatory prose for subsequent work; they do not retroactively become claimed inputs to earlier drafts. `evidence/REUSE_RECONCILIATION.md` records exact source/page identities, distinctions and limitations. Existing textbook translations remain with their book owners and receive no OpenLogic translation credit here.

The canon PDFs and page images are local research copies and are **not redistributed**. Their original rights notices remain applicable. Citation records and short terminology observations do not imply an open license for those third-party works.

Review is automated/model-based. No independent human review is claimed or required as a release gate. Current checks cover source/translation block alignment, formula skeletons, references, environments, identifiers, token parity, Unicode normalization, semantic comparisons and reverse-paraphrase samples. PDF build, glyph and visual checks are reported per release; the status file states the exact scope. Provisional terms remain explicitly marked.

## Build

Run `python tools/prepare_reader.py`, then `pwsh -File tools/build_sets_windows.ps1 -Edition reader`. Requirements: Python 3, XeLaTeX/MiKTeX, fontspec, ucharclasses, standard AMS packages, TikZ, hyperref and Latin Modern Roman. Pinned Noto Serif Bengali fonts and their SIL Open Font License are in `fonts/`. The Windows builder acquires `Global\InterlanguageTeXSlotV1` before any TeX process, captures the process tree, disables shell escape/package installation, and holds the mutex across up to four convergence passes and log checks. Attempt receipts are persisted in the build directory. The current 21-page PDF passed visual inspection and the last two guarded passes produced identical bytes.

After the PDF build, `python tools/build_reader_html.py` creates a single offline HTML file with embedded Bengali fonts, native MathML, linked references, numbered definitions/exercises and all six diagrams extracted as vectors from the same PDF. It additionally requires Pandoc, PyMuPDF and Beautiful Soup 4. Structural HTML checks pass with 909 MathML expressions, 88 numbered environments and no unresolved internal links or conversion warnings. **Browser visual inspection remains pending:** local-file navigation was blocked by the browser security policy. This limitation is preserved in the release evidence; PDF visual QA does not certify HTML layout or assistive-technology behavior.

Reader notes identify source issues without silently changing aligned formulas: an unnamed identity-relation symbol, an alphabet-size qualification, an undefined variable in the branch definition and the local reuse of the R-plus notation. The remaining alternative wrappers and Proof Theory part will be integrated as their translations are completed. Full-corpus and independent clean-platform reproducibility remain unfinished.

## License

OpenLogic source and this translation: Creative Commons Attribution 4.0 International, with upstream attribution and component exceptions preserved. See `upstream/LICENSE.md` and the source component notices. Noto fonts: SIL Open Font License 1.1. Translation changes are identified by the `bn-Beng-IN/` directory and the machine-translation status above.
