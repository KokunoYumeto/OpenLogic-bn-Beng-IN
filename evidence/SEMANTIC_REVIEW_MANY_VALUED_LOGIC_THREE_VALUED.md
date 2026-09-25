# Semantic review — Many-Valued Logic: Three-Valued Logics

Date: 2026-09-21
Scope: OLP-0392--OLP-0397
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

## Result

The complete Three-Valued Logics chapter has been translated into India-standard Bengali and reread against the frozen English source. The six units contain 76 aligned blocks: 65 translated prose-bearing blocks and 11 unchanged structural or formal blocks. The strict source checker passes block count, audited mathematics, protected controls, environments, semantic tokens and Unicode NFC for every unit. This is source-level completion; the chapter is not yet integrated into the cumulative 299-unit reader.

## Canon actually consulted

The translation reused exact, hash-bound passages `BN-IN-P005`, `BN-IN-P008`, `BN-IN-P009`, `BN-IN-P010`, `BN-IN-P013`, `BN-IN-P018`, `BN-IN-P019`, `BN-IN-P023` and `BN-IN-P025`. These are India-standard Bengali witnesses for number terminology, truth-evaluable statements and connectives, proposition and quantification, scope, relations, functions, algebraic variables and products, mappings and proof prose. Their source identities, page locators and page-image hashes are preserved in `CANON_SOURCES.jsonl` and `CANON_PASSAGES.jsonl`; `index_batch.py` revalidated the original and page-image hashes while writing every translated segment.

The checked witnesses support the surrounding adult mathematical and philosophical register. They do not directly attest the complete modern compounds for three-valued, Kleene, Gödel, LP, Halldén or R-Mingle systems. Those choices are therefore explicitly provisional and definition-governed in `BN-IN-T313`--`BN-IN-T315`. The displayed matrices, designated sets and mathematical arguments remain controlling evidence for their exact meanings.

## Unit-by-unit semantic comparison

### OLP-0392 — chapter driver

Reverse paraphrase: the chapter is titled Three-Valued Logics and imports, in frozen-source order, the introduction, Łukasiewicz, Kleene, Gödel and multiple-designation sections. All five `\olimport` controls and the chapter identity are unchanged.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/three-valued-logics.tex`
SHA-256: `87358bfb72baef7ceb82cbdd85c0f245fdd106f3002666755fe7cbcf0703cb33`

### OLP-0393 — introduction

Reverse paraphrase: adding `\Undef` to `\True` and `\False` yields a three-valued setting, but it does not uniquely determine a logic. Each connective may receive any of many truth functions, and either only `\True` or both `\True` and `\Undef` may be designated. The section announces representative systems, motivations and properties without claiming exhaustiveness.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/introduction.tex`
SHA-256: `44c4d3ef9c0cbc5af12aeaa74c7cb670229c817d4008f64089ff554e48c325d8`

### OLP-0394 — Łukasiewicz logic

Reverse paraphrase: the third value models a future-contingent proposition whose truth is not yet settled. Negation preserves `\Undef`; conjunction and disjunction follow the min/max-style tables; implication is stipulated to make `A\lif A` true even when both occurrences have value `\Undef`. Only `\True` is designated. Classical assignments retain their classical values, but excluded middle and several other classical tautologies fail. The proposed possibility and necessity operators distinguish settled truth and falsity but cannot make the contradiction `p\land\lnot p` impossible in every valuation.

The quoted Warsaw example retains all modal qualifications: the future presence is possible but not necessary, neither positively nor negatively determined now, and assigned the third value `1/2`. The footnote preserves the historical, non-current sense of “possible.” Truth tables, nine-row worked table, exercises, labels and references are unchanged except for the three audited source corrections below.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/lukasiewicz.tex`
SHA-256: `92f2ef5b6deb51bb2a04411d1e640c89a41847d275d98f9ad4bab18857e60bf3`

### OLP-0395 — Kleene logics

Reverse paraphrase: `\Undef` first represents nontermination. Sequential evaluation yields weak Kleene behavior, where an undefined component infects a conjunction or disjunction. Parallel evaluation yields strong Kleene behavior, where a false conjunct or true disjunct settles the compound even if the other procedure does not terminate; under that reading `\Undef` may be read as unknown. Both matrices designate only `\True`, define implication as `\lnot A\lor B`, and have no tautologies because the all-`\Undef` valuation gives every formula value `\Undef`. Their consequence relations are nevertheless nontrivial. Bochvar's meaningless value, external negation and undefinedness operator remain distinguished by their displayed unary tables.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/kleene.tex`
SHA-256: `686762499955a2fe5b984d43139407caa13c7bf5570e7d177d7564a64c47be3b`

### OLP-0396 — Gödel logics

Reverse paraphrase: the displayed three-valued Gödel matrix designates only `\True`, interprets falsum as `\False`, uses the same conjunction and disjunction tables as Łukasiewicz and strong Kleene logic, but changes negation and implication. Every intuitionistically valid formula is a tautology of the matrix; several familiar classical principles fail, while linearity `(p\lif q)\lor(q\lif p)` and double-negation decidability `\lnot\lnot p\lor\lnot p` hold although they are not intuitionistically valid. The two exercise lists preserve the tautology and non-tautology directions.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/goedel.tex`
SHA-256: `8b90ff109a58eb96b37b985a23e0b21f344fc03b88082df08a47a300ad61ade7`

### OLP-0397 — multiple designation

Reverse paraphrase: designating `\Undef` as well as `\True` changes consequence even when truth functions stay fixed. LP uses strong Kleene functions; Halldén's logic uses weak Kleene functions plus the meaningless operator. Both regain tautologies. The LP proof collapses `\Undef` to classical `\True` and establishes by induction that any K3 value `\False` remains classically false and any K3 value `\True` remains classically true. LP is paraconsistent because contradiction does not entail an arbitrary conclusion. RM3 retains the Łukasiewicz functions while designating `\True` and `\Undef`. The final Gödel matrix exercise asks the reader to prove classical consequence after the same designated-set change.

Target: `bn-Beng-IN/content/many-valued-logic/three-valued-logics/multiple-designation.tex`
SHA-256: `1620f46b33753aca0f6d5e0909fa4f69560a360de1b74f28b15423537ce29987`

## Audited source corrections

- `BN-SRC-318`: the false/undetermined conjunction display repeated `tf(and)(False,Undef)` twice. The second term is restored as `tf(and)(Undef,False)`, matching the symmetric truth-table cell.
- `BN-SRC-319`: an exercise conditional had an unmatched final right parenthesis. The surplus delimiter is removed without changing the connective structure.
- `BN-SRC-320`: the LP induction basis unconditionally equated `v(p)` and `v'(p)`, which is false when `v(p)=Undef` because the definition maps that case to classical true. The target proves only the required false and true implications separately.
- `BN-SRC-321`: the conjunction induction step repeated the value of `B` where the second conjunct `C` was required, once in the false case and once in the true case. Both metavariables are restored.
- `BN-SRC-322`: the RM3 definition declared `\lfalse` in its language but supplied no interpretation, and the referenced Łukasiewicz language did not contain it. The target specifies `tf(falsum)=False`, completing the stated matrix.
- `BN-SRC-323`: the final modal countervaluation claimed value `Undef`. Direct composition of the displayed tables gives `not p=Undef`, `p and not p=Undef`, `Diamond Undef=True`, and `not True=False`. The target restores `False`; the intended non-tautology conclusion is unchanged.

Each correction has an adjacent Bengali note, an exact frozen-source identity, a target marker span, a review question and an explicit audited transformation in the strict checker. Correction notes are excluded from mathematical parity.

## Terminology decisions

- `BN-IN-T313`: `ত্রিমানী যুক্তিবিদ্যা`, `ভবিষ্যৎ-আপতিক`, `অনির্ধারিত সত্যমান`.
- `BN-IN-T314`: strong/weak Kleene terminology, parallel evaluation, external negation and the undefinedness operator.
- `BN-IN-T315`: three-valued Gödel, LP, Halldén and RM3 names, `পরাসঙ্গত`, and `বিস্ফোরণ নীতি`.

The distinctions among অনির্ধারিত (future truth not settled), অসংজ্ঞায়িত (nonterminating or partial computation), অজ্ঞাত (epistemic reading) and অর্থহীন (Bochvar/Halldén interpretation) were checked separately and are not treated as interchangeable synonyms.

## Structural and mathematical QA

- Source/target block counts: `76/76`.
- Translated/unchanged blocks: `65/11`.
- Protected `\olfileid`, `\ollabel`, `\olref` and `\olimport` controls: exact after audited corrections.
- Environments and semantic-token annotations: exact.
- Displayed matrices and truth tables: cell-for-cell preserved except the explicitly audited prose display repair in `BN-SRC-318`.
- Unicode: all six targets NFC-normalized.
- Segment index after integration: 4,500 rows, 3,817 translated, SHA-256 `fe5cd019a80d36541aeb6236504bb2ba2e1795f0e83a84e782363e1bd4b454fa`.

No TeX engine, BibTeX, Biber or latexmk process was launched for this source batch. Visual pagination and cumulative PDF/HTML/EPUB integration remain deferred to the next reader tranche; no new reader release is claimed.
