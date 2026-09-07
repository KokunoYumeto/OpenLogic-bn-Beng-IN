# Semantic review: Model Theory — Lindström

This review covers OLP-0203 through OLP-0207, the complete frozen Lindström chapter. I reread every Bengali block against its frozen English block, checked the displayed formulas, controls and protected semantic tokens, and reverse-paraphrased the model-theoretic claims. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; the indexed passage images and original files are hash-verified during index generation.

## Scope and method

- OLP-0203 is the chapter driver; OLP-0204 through OLP-0207 are the four reader units.
- The five units contain 38 aligned source/target blocks. The driver has six structural blocks; the introduction has two; Abstract Logics has seven; Compactness and Löwenheim--Skolem Properties has twelve; and Lindström's Theorem has eleven. Thirty-one blocks contain translated Bengali prose; seven retain unchanged structural or formal material and are recorded as such.
- Every unit passes the public source replay. Block counts agree; mathematical fragments, protected controls, environment order, OpenLogic semantic-token multisets and Unicode NFC all pass. Formal math is retained byte-for-byte after whitespace normalization, including the source's `\Domain{N}*` spelling in OLP-0206; no unrecorded source correction is introduced.
- The chapter has no source-correction record. The target prose translates explanatory text while preserving every metavariable, relation, macro, theorem label, reference and figure command.

## Unit review

### OLP-0203 — chapter driver

The Bengali chapter title identifies Lindström's theorem, and all four section imports remain in their frozen order. The part/chapter identity, document class and end hook are unchanged. Reverse paraphrase: the driver exposes the same chapter boundary and reader reachability as the source.

### OLP-0204 — introduction

The introduction states the characterization of first-order logic as the maximal logic satisfying compactness and downward Löwenheim--Skolem under the stated extra assumptions. It preserves the two theorem references and the restriction to relational languages containing predicates and individual constants but no functions. Reverse paraphrase: the section announces the target theorem and narrows the ambient language before the abstract-logic definitions.

### OLP-0205 — abstract logics

The definition of an abstract logic remains a pair `(L, models_L)` assigning sentences to each language and a satisfaction relation to structures. The examples of ordinary first-order logic, infinitary conjunction/disjunction, nonstandard quantifiers and variable conventions are retained. The normality definition preserves L-monotonicity, the finite expansion property, isomorphism invariance, renaming, Boolean closure, quantification and relativization. The final definition preserves comparison by expressiveness and equivalence, followed by the observation that first-order logic is normal and embeds into every normal logic. Reverse paraphrase: normality gives enough closure and invariance to support the later coding arguments, while the language remains abstract beyond ordinary syntax.

### OLP-0206 — compactness, Löwenheim--Skolem and partial isomorphism

The compactness and downward Löwenheim--Skolem definitions preserve finite satisfiability and enumerable-model claims. The explanatory passage keeps the algebraic nature of partial isomorphism, explains why ordinary formula induction is unavailable for arbitrary abstract sentences, and states the theorem that normal logics with the Löwenheim--Skolem property make partially isomorphic structures elementarily equivalent. The proof's finite-sequence coding, concatenation predicates, internal relation, relativized first-order sentences and contradiction from enumerable partial isomorphisms are all retained, including the figure and its labels. Reverse paraphrase: the coding turns a putative abstract distinction between partially isomorphic structures into a first-order statement that survives in an enumerable model, where back-and-forth forces an isomorphism.

### OLP-0207 — Lindström's lemma and theorem

The lemma preserves the finite-language and bounded-quantifier-rank hypothesis, the finite conjunction of rank-n types and the finite disjunction over models satisfying the abstract sentence. The theorem proof retains the reduction from n-equivalence to `I_n`, the sequence of countermodels, the union and coded expansions, the discrete order with a nonstandard index supplied by compactness, and the final partial-isomorphism contradiction. Reverse paraphrase: bounded rank makes each abstract sentence first-order definable; if no bound existed, compactness would produce a nonstandard stage whose two structures are partially isomorphic yet disagree on the sentence, contradicting the previous theorem.

## Technical claim audit

- Abstract-logics normality is recorded as a list of seven closure/invariance conditions, with the source's language inclusions and structure expansions intact.
- The partial-isomorphism proof uses finite sequences and ternary concatenation/extension predicates to express the back-and-forth relation inside a first-order expansion; the relativization property supplies the sentences distinguishing the two substructures.
- The Lindström lemma uses the finiteness of first-order sentences of bounded quantifier rank up to logical equivalence, then takes a finite disjunction over the models satisfying the abstract sentence.
- The main theorem assumes compactness and downward Löwenheim--Skolem, codes all finite approximants in one ordered structure, and uses a nonstandard index to obtain a partial isomorphism at every standard finite depth.
- All displayed equations, set builders, relation symbols, quantifier macros, theorem labels and cross-references are structurally identical to the frozen source under the public checker.

## Terminology and edition scope

Decisions BN-IN-T139 through BN-IN-T148 record the abstract-logic, normality, compactness, Löwenheim--Skolem, partial-isomorphism, expressiveness, relativization, quantifier-rank and Lindström-theorem register. The checked logic, quantification, relation, mapping, proof and cardinality witnesses support the Bengali component roots; specialized model-theory compounds remain explicitly provisional and open to expert review. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set; Bangladesh Bengali is not used as an overriding authority.

## Remaining release boundary

This is source-complete chapter evidence, not a reader release. No TeX attempt was made because the shared global TeX mutex is reserved by the Persian reader lane. PDF rendering, glyph inspection, semantic HTML checks, printed-page locators and release-level archive readback remain pending under that policy.
