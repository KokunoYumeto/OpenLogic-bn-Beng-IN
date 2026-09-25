# Semantic review — Normal Modal Logic opening

Date: 2026-09-25
Scope: OLP-0407--OLP-0412
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

The Normal Modal Logic part driver and the first four sections of its Syntax and Semantics chapter are translated into India-standard Bengali and reread against the frozen English. The six units have 59 aligned blocks: 44 translated prose-bearing blocks and 15 unchanged structural or formal blocks. The strict checker passes source-hash, audited-formula, protected-control, environment, semantic-token and Unicode NFC checks for all six. The chapter has six further sections, OLP-0413--OLP-0418, so this is an opening source tranche, not chapter or reader completion.

## Canon actually consulted

The Tripura mathematical-reasoning page `BN-IN-P008` (printed p. 153), Suri Vidyasagar College proposition/quantification spread `BN-IN-P009` (printed pp. 110--111), NSOU relation page `BN-IN-P013` (printed p. 360), and NSOU function page `BN-IN-P018` (printed p. 365) were visually read while reviewing these units on 2026-09-25. The exact subset attributed to each translated block is recorded in `SEGMENT_CANON_USE.jsonl`, and the indexer revalidated the local original and page-image hashes. These Indian witnesses support connective, proposition, relation and function usage. They do not directly attest specialized modal compounds; `BN-IN-T319` and `BN-IN-T320` therefore leave those choices provisional and governed by the source definitions. Existing `BN-IN-T026` fixes প্রতিবিম্ব ধর্ম, প্রতিসাম্য and পরিযায়িতা for reflexivity, symmetry and transitivity. The source, not a canon witness, controls the logic.

An official University of North Bengal [philosophy syllabus](https://trove.nbu.ac.in/ipForward.aspx?APP_ID=19%2Fnbuweb%2Fdoc%2Facr%2Fsyllabus%2FPG_Philosophy_CBCS_2022.pdf) was also consulted for the Indian academic context of modal logic, possible worlds and T/S4/S5. Because that syllabus is in English, it was not entered as a Bengali terminology attestation or attributed to translation segments.

## Reverse paraphrase and unit identities

- **OLP-0407**, `bn-Beng-IN/content/normal-modal-logic/normal-modal-logic.tex`, SHA-256 `72c06fd2218465e935ab694e1f32f04a4f0fbf03648c27d7326500d3e3e655b3`: the part treats the metatheory of normal modal logics, credits the existing notes on classical correspondence theory, and imports the seven frozen-source chapters in order. The editorial statement does not claim this edition has translated all seven.
- **OLP-0408**, `bn-Beng-IN/content/normal-modal-logic/syntax-and-semantics/syntax-and-semantics.tex`, SHA-256 `ceab817d8b381b74fc7c7c99a10be1f5c5cdc701cae7d40149a035fedba67f6d`: the `nml/syn` chapter retains all ten section imports and its end hook.
- **OLP-0409**, `bn-Beng-IN/content/normal-modal-logic/syntax-and-semantics/introduction.tex`, SHA-256 `b30bd5dd8d71da68032b704d554ace3f0114856492ad505d2eff40da65d20233`: necessity entails possibility, whereas possibility alone does not entail necessity; iterated modal operators motivate a semantics richer than Carnap's all-state-description truth. Kripke's accessibility relation makes necessity at a world depend on truth at every world accessible from it. Correspondence theory relates properties of that relation to modal schemas, including the reflexivity schema Box A implies A. Historical names, dates, S1--S5 labels and D/T/B/4/5 schema controls are retained.
- **OLP-0410**, `bn-Beng-IN/content/normal-modal-logic/syntax-and-semantics/language-modal-logic.tex`, SHA-256 `1790c6cca44dc13b3e4f9ab0a59e2bb04aecf668f0077a0bacc4be8c3a033523`: the language has optional truth/falsity constants, denumerably many propositional variables, the displayed propositional connectives and Box/Diamond. The inductive formula clauses and defined-operator abbreviations are preserved. Box and Diamond are dual via negation. `BN-SRC-332` removes an unmatched closing parenthesis from the source's disjunctive abbreviation of implication.
- **OLP-0411**, `bn-Beng-IN/content/normal-modal-logic/syntax-and-semantics/substitution.tex`, SHA-256 `ed15ed9814871e8406915cfe12fbceb7ac5d668e386d5f88b5f0d110b6c6b3d9`: simultaneous substitution replaces each original occurrence of `p_i` with its corresponding `D_i` without recursively replacing variables newly inserted by a different `D_j`. All constants, variable, connective and modal-operator induction cases are preserved. The worked example shows that either sequential substitution order can differ from simultaneous substitution. `BN-SRC-333` puts the biconditional case under `prvIff`; `BN-SRC-334` tags the Box case as `prvBox`. Neither changes its formula.
- **OLP-0412**, `bn-Beng-IN/content/normal-modal-logic/syntax-and-semantics/relational-models.tex`, SHA-256 `d4ca40617ee8a89689ed2b0872f3b0a13630bcf205198e5eab64996dfd34dde7`: a model is `(W,R,V)` with nonempty worlds, binary accessibility and a proposition-to-world-set assignment. `Rww'` says `w'` is accessible from `w`; `w in V(p)` makes `p` true there. The three-world diagram preserves both arrows from `w_1`, the `p/q` truth labels, the specified valuation sets and its translated caption.

## Audited frozen-source corrections

- `BN-SRC-332`: the `prvOr` alternative for implication ends its disjunction with an unmatched `)`; the target omits that character.
- `BN-SRC-333`: the biconditional induction clause is guarded by `prvIf` in the source; the target uses `prvIff`.
- `BN-SRC-334`: the Box induction clause is a bare item in the source; the target guards it with `prvBox`, matching the language's optional-constructor convention.

Each correction has an adjacent Bengali note, frozen-source hash, target marker span, exact audited comparison and review question in `SOURCE_CORRECTIONS.jsonl`. Formula parity excludes only the explanatory note and the exact source repair. No target change is silently treated as source identity.

The cumulative segment index now has 4,647 aligned rows, 3,925 translated, SHA-256 `59d1447165a0268b0b9ed386087f74fd4898064d8224d7f4bbc924db9e1176e0`. No TeX engine, BibTeX, Biber or latexmk process was launched for this source tranche. Cumulative PDF/HTML/EPUB integration and visual pagination remain pending; the verified reader remains the 299-unit release.
