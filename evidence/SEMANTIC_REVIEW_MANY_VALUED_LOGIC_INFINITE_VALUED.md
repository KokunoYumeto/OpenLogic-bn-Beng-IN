# Semantic review — Many-Valued Logic: Infinite-Valued Logics

Date: 2026-09-25
Scope: OLP-0398--OLP-0401
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

## Result

The complete Infinite-Valued Logics chapter is translated into India-standard Bengali and reread against the frozen English source. Its four units contain 34 aligned blocks: 27 translated prose-bearing blocks and 7 unchanged structural or formal blocks. The strict checker passes block count, audited mathematical parity, protected controls, environments, semantic tokens and Unicode NFC for every unit. This is source-level completion; the chapter is not yet in the cumulative 299-unit reader.

## Canon actually consulted

Exact, hash-bound passages `BN-IN-P005`, `BN-IN-P008`, `BN-IN-P018`, `BN-IN-P019`, `BN-IN-P023` and `BN-IN-P025` supplied the established number, logical, function, algebraic, mapping and proof register. The original and page-image identities are in `CANON_SOURCES.jsonl` and `CANON_PASSAGES.jsonl` and were revalidated by `index_batch.py`. The canon supports the surrounding prose rather than directly attesting the complete specialized compounds for infinite-valued or Gödel–Dummett logic; those remain provisional and definition-governed in `BN-IN-T316`--`BN-IN-T317`. `BN-IN-P005` uses its own positive-natural convention, whereas the OpenLogic set-builder must be interpreted with the project's zero-inclusive `\Nat` convention; the denominator repair is recorded explicitly in `BN-SRC-324`.

## Unit-by-unit semantic comparison

### OLP-0398 — chapter driver

Reverse paraphrase: the chapter is titled Infinite-Valued Logics and imports introduction, Łukasiewicz and Gödel in the frozen-source order. The chapter identity and all three `\olimport` controls remain unchanged.

Target: `bn-Beng-IN/content/many-valued-logic/infinite-valued-logics/infinite-valued-logics.tex`
SHA-256: `bf16b94f163e60681d688abe7709c7d3e36df5686e4e692a2505f6cd6be4db4e`

### OLP-0399 — introduction

Reverse paraphrase: a matrix may have infinitely many truth values. The rational unit interval `V_\infty` supplies one example, and each `V_m` is a finite grid of exactly `m` evenly spaced values from 0 to 1; `V_5` is the displayed five-value instance. Usually only 1 is designated, 0 means absolute falsity, and formulas may take intermediate values. The real unit interval and other infinite subsets are also possible; the real-interval systems are often called fuzzy. The two set-builder bounds are repaired as documented below.

Target: `bn-Beng-IN/content/many-valued-logic/infinite-valued-logics/introduction.tex`
SHA-256: `d78010f37742e5682446e07ba67e6328eb93da673a2f29a09da164ecc50e3345`

### OLP-0400 — infinite-valued Łukasiewicz logic

Reverse paraphrase: the source explicitly marks the section as a short preliminary stub. Its matrix has rational truth values, only 1 designated, negation `1-x`, conjunction/minimum, disjunction/maximum and implication `min(1,1-(x-y))`. Replacing `V_\infty` by `V_m` gives the finite matrix, and the displayed three-valued tables establish agreement with the preceding chapter. Consequence in `L_\infty` implies consequence in every `L_m`; the converse is true for finite premise sets, as corrected below. The final prose contrasts this conditional with defining it as `\lnot A\lor B` and the exercise asks for linearity.

Target: `bn-Beng-IN/content/many-valued-logic/infinite-valued-logics/lukasiewicz.tex`
SHA-256: `1952dad832ddc924d9bd85961bdf0f1d84134756deba93b86533990767249558`

### OLP-0401 — infinite-valued Gödel logics

Reverse paraphrase: the preliminary section defines a rational-valued Gödel matrix with falsum 0, crisp negation, min/max conjunction and disjunction, and implication equal to 1 when `x<=y` and to `y` otherwise. Its three-valued restriction agrees with the preceding chapter's matrix. Consequence in `G_\infty` implies consequence in every `G_m`; the converse requires finite premises, as corrected below. Intuitionistic tautologies remain tautologies; the listed six classical schemas remain non-tautologies. Linearity remains valid, and adding its schema to intuitionistic logic characterizes Gödel–Dummett logic. The two final exercises retain the valid linearity formula and the formula valid in `G_3` but not `G_\infty`.

Target: `bn-Beng-IN/content/many-valued-logic/infinite-valued-logics/goedel.tex`
SHA-256: `9bc2924c3314bb2239353f887e50851d753397638826e526cfe813c28cd109bc`

The target comment headers normalize the frozen source's erroneous chapter/section metadata in the latter two sections. These comments are non-rendered; file IDs, import paths, labels and references remain source-identical.

## Audited source corrections

- `BN-SRC-324`: the `V_\infty` set builder permits denominator `m=0` under the project's `\Nat` convention. Adding `0<m` makes every displayed quotient defined and retains the rational unit interval.
- `BN-SRC-325`: the frozen `V_m` numerator bound `n<=m` yields `m+1` values and one value greater than 1. The bound `n<=m-1` gives the stated `m` values and agrees with `V_5`.
- `BN-SRC-326`: the Gödel negation `cases` expression nested `$1$` and `$0$` inside `align*` math mode. Removing those dollar pairs preserves the values and yields valid TeX math syntax.
- `BN-SRC-327`: the unqualified Łukasiewicz converse fails for infinite premises. Let `p\oplus q := \lnot p\lif q`, so its value is `min(1,p+q)`, and let `D_n` be the `(n-1)`-fold strong disjunction of `p_n`. Premises `(D_n\lif\lnot p_n)\land(\lnot p_n\lif D_n)` for every `n>=2` force `p_n=1/n`. No finite `V_m` can realize all these values, yet rational `V_\infty` does; setting an unrelated conclusion `q=0` refutes the unrestricted converse. The target restricts it to finite premises.
- `BN-SRC-328`: the unqualified Gödel converse also fails for infinite premises. Include `p_n\lif q` and `((p_{n+1}\lif p_n)\lif p_n)` for every `n>=1`. In a finite-grid countervaluation with `q<1`, these require `p_n<=q<1` and the impossible infinite strict chain `p_n<p_{n+1}`. In `V_\infty`, `q=1/2` and `p_n=n/(2(n+1))` satisfy every premise while refuting `q`. The target restricts the converse to finite premises.

For either finite-premise converse, a rational countervaluation uses finitely many variable values; choosing `m-1` divisible by all their denominators places them together in `V_m`. Every correction has an adjacent Bengali note, frozen-source identity, target marker span, review question and exact audited-source transformation. Correction-note material is excluded from parity.

## Structural and mathematical QA

- Source/target block counts: `34/34`; translated/unchanged: `27/7`.
- Protected `\olfileid`, `\ollabel`, `\olref` and `\olimport` controls, environments and semantic tokens: exact after audited corrections.
- All truth-function formulas and finite truth-table cells: preserved except the exact audited repairs above.
- Unicode: all four targets NFC-normalized.
- Segment index after integration: 4,534 rows, 3,844 translated, SHA-256 `fb8b72a86ed6982dc1972d900c74d16f0965b99705883b7e5b6bafea284400fa`.

No TeX engine, BibTeX, Biber or latexmk process was launched for this source batch. Visual pagination and cumulative PDF/HTML/EPUB integration remain deferred to the next reader tranche; no new reader release is claimed.
