# Semantic review: Model Theory — Interpolation

This review covers OLP-0198 through OLP-0202, the complete frozen Interpolation chapter. I reread every Bengali block against its frozen English block, checked every displayed formula and source control, and reverse-paraphrased the mathematical claims. Canon passages actually used for translated blocks are recorded in `SEGMENT_CANON_USE.jsonl`; page hashes and source identities are revalidated there.

## Scope and method

- OLP-0198 is the chapter driver; OLP-0199 through OLP-0202 are its four reader units.
- The five units contain 41 aligned source/target blocks, of which 32 contain translated prose. The driver contributes its structural imports and chapter boundary; the four reader units carry the mathematical exposition.
- Every unit passes source-to-target replay. Source and target block counts agree; protected controls, environment order, OpenLogic semantic-token multisets and Unicode NFC agree. Mathematical fragments agree literally except for the audited repairs BN-SRC-134 through BN-SRC-137. BN-SRC-138 is a prose repair completing the theorem's biconditional wording.
- Correction notes are disclosed beside the affected passage and in `SOURCE_CORRECTIONS.jsonl`. The public checker removes note bodies, applies the exact audited source transformations, and then requires complete formula parity.

## Unit review

### OLP-0198 — chapter driver

The chapter identity and all four imports are retained in source order, with the end hook unchanged. The Bengali chapter title identifies interpolation without changing reader reachability.

### OLP-0199 — introduction

The overview states the interpolation consequence `A entails B`, the existence of an interpolant `C`, and the shared nonlogical-symbol condition. It also identifies Beth definability and Robinson joint consistency as the principal applications. Reverse paraphrase: an interpolant mediates between the two formulas while using only vocabulary common to them.

### OLP-0200 — separation

The separation definition, model-class diagram, common-language restriction and two lemmas are retained. The first lemma uses compactness to remove newly added constants from a separator; the second adds a fresh witness for an existential formula without creating a separator. BN-SRC-134 replaces the undefined `delta` with the finite conjunction `!H`, and BN-SRC-135 restores the missing square bracket in `\\lexists[x][!S]`. Reverse paraphrase: separation in the expanded language would yield separation in the original language, and existential witness expansion preserves inseparability.

### OLP-0201 — Craig interpolation proof

The contrapositive proof constructs increasing pairs `(Gamma_n, Delta_n)`, extends them to a maximally inseparable pair, proves maximal consistency and obtains models `M'_1` and `M'_2`. Their common-language reducts are isomorphic; the final model combines the two interpretations and satisfies `A` and `not B`, contradicting entailment. BN-SRC-136 changes the left-language predicate transport to start with `M'_1`, matching the following tuple equivalence and the direction of `h`. Reverse paraphrase: if no interpolant exists, the two sides can be extended consistently until a shared-language isomorphism amalgamates them into a countermodel.

### OLP-0202 — Beth definability

The explicit and implicit definability definitions, expansion argument, compactness reduction and Craig-interpolant construction are retained. BN-SRC-137 restores the atomic formula `\\Atom{P'}{c_1,\\dots,c_n}` in the compactness display, and BN-SRC-138 completes the theorem statement as `যদি এবং কেবল যদি`. Reverse paraphrase: uniqueness of a predicate's interpretation across expansions yields a formula in the base language that explicitly defines it, and explicit definition immediately gives uniqueness.

## Technical claim audit

- Separation is expressed by `Gamma entails C` and `Delta entails not C`; inseparability is the absence of such a sentence.
- The language-extension lemma uses compactness and generalization to replace fresh constants by universally quantified variables. The existential-witness lemma distinguishes whether the fresh constant occurs in the proposed separator.
- The interpolation proof's alternating construction handles both existential witness clauses, proves both induction statements, and uses compactness only after finite separation would contradict the induction invariant.
- Maximal consistency is used to build constant-generated models. The common reducts agree on every shared-language sentence, so the map induced by corresponding constant interpretations is an isomorphism.
- The amalgamated model interprets symbols from `L_2 minus L_1` in `M'_2`, symbols from `L_1 minus L_2` by transport from `M'_1`, and common symbols through the isomorphism. Formula induction then gives the contradiction.
- Beth definability separates the `P` and `P'` copies, applies interpolation to the atomic implication, and generalizes fresh constants back to variables.

## Terminology and edition scope

Decisions BN-IN-T134 through BN-IN-T138 record the interpolation, separation, maximal-consistency, amalgamation and definability register. The checked logic, quantification, relation, mapping and proof witnesses support the component Bengali roots; specialized model-theory compounds remain explicitly provisional and open to expert review. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. Bangladesh Bengali is not used as an overriding authority.

## Remaining release boundary

This is source-complete chapter evidence, not a reader release. No TeX attempt was made for this chapter because the shared global TeX mutex is reserved by the Persian reader lane. PDF rendering, glyph inspection, semantic HTML checks, printed-page locators and release-level archive readback remain pending under that policy.
