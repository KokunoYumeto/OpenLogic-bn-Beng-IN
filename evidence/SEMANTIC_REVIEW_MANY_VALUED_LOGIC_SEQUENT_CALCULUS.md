# Semantic review — Many-Valued Logic: Sequent Calculus

Date: 2026-09-25
Scope: OLP-0402--OLP-0406
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

## Result

The complete Many-Valued Logic Sequent Calculus chapter is translated into India-standard Bengali and reread against the frozen English source. Its five units contain 54 aligned blocks: 37 translated prose-bearing blocks and 17 unchanged structural or formal blocks. The strict source checker passes block count, audited mathematics, protected controls, environments, semantic tokens and Unicode NFC for every unit. This is source-level completion; the chapter is not yet integrated into the cumulative 299-unit semantic reader.

## Canon actually consulted

The relevant source images for `BN-IN-P008` (Tripura mathematical reasoning, printed p. 153), `BN-IN-P009` (West Bengal university philosophy, printed pp. 110–111), `BN-IN-P018` (West Bengal university function prose, printed p. 365) and `BN-IN-P025` (West Bengal university proof prose, printed p. 368) were visually reread on 2026-09-25 while drafting this chapter. The exact subset listed for each unit in `SEGMENT_CANON_USE.jsonl` reflects the terms and prose actually used there. The indexer revalidated original and page-image hashes against `CANON_SOURCES.jsonl` and `CANON_PASSAGES.jsonl`.

These witnesses support the established adult register for connectives, propositions, functions, variables and mathematical proof, alongside the edition's previously fixed sequent terms in `BN-IN-T073`, `BN-IN-T077`, `BN-IN-T079`, `BN-IN-T081` and `BN-IN-T084`. They do not directly attest the full many-sided sequent construction. `BN-IN-T318` therefore records `$n$-পাশবিশিষ্ট সিকোয়েন্ট কলন` and its truth-value-position compounds as provisional and governed by the displayed definitions. The frozen English source, not a witness, controls formal meaning and rule trees.

## Unit-by-unit semantic comparison

### OLP-0402 — chapter driver

Reverse paraphrase: the Sequent Calculus chapter retains its `mvl/seq` identity and imports introduction, rules and proofs, structural rules and propositional rules in frozen-source order. All four `\olimport` controls and the end hook remain unchanged.

Target: `bn-Beng-IN/content/many-valued-logic/sequent-calculus/sequent-calculus.tex`
SHA-256: `ccb2352400ed7660d0e4a42d334933a52250cb9355ad1e286244adfb85c86ae6`

### OLP-0403 — introduction

Reverse paraphrase: a finite truth-value matrix permits a sequent calculus analogous to the classical one. Classically, a sequent with `m` antecedent and `n` succedent formulas expresses the conditional from their conjunction to their disjunction, and is satisfied when some antecedent is false or some succedent is true. The two displayed conditional rules, interpreted semantically, state both directions of their truth conditions; alternative conjunction-left and disjunction-right rules also have this property. In a three-valued calculus, each of the three positions corresponds to False, Undef or True, and a sequent is satisfied when some formula occurs in its own value's position. The all-three-position initial sequent is therefore always satisfied.

The source's left endpoint and missing valuation argument are repaired exactly as documented below. All other displayed formulas and both inference-rule pairs are retained.

Target: `bn-Beng-IN/content/many-valued-logic/sequent-calculus/introduction.tex`
SHA-256: `d58132be40d50049794021fa3b4ff57ddec0e3e5f6551688c50dd86268bf9b27`

### OLP-0404 — rules and proofs

Reverse paraphrase: an `$n$`-sided sequent consists of `n` finite, possibly empty sentence sequences. Initial sequents repeat a sentence in every position; a zero-place connective supplies an additional initial sequent in the position matching its fixed value. Each connective has a logical rule for every value it can take. Derivations are trees rooted in correctly applied rules with initial sequents at their tops. A theorem has a derivation of the sequent placing the conclusion in all designated positions. Derivability from premises uses a finite subset, putting the conclusion in designated positions and a finite premise sequence in the others. In the Łukasiewicz three-valued example, only True is designated, so the target sequent places the conclusion in that position; the parenthetical example shows how it changes if Undef is designated too.

The generic-position subscript in the first definition is repaired exactly as documented below. File identity, macro tokens, formal sequents and all designation conditions remain source-identical.

Target: `bn-Beng-IN/content/many-valued-logic/sequent-calculus/rules-and-proofs.tex`
SHA-256: `aada51e6b18271dce3e701ce5e175ec95a70f0065a03a33fc9d3c4a940eca245`

### OLP-0405 — structural rules

Reverse paraphrase: weakening, contraction and exchange work at each one of the `n` positions, and a chain of these steps may be shown by double inference lines. Cut has one form for each ordered choice of distinct positions `i` and `j`. Every premise, conclusion, position index and rule label in the four displayed forms is unchanged.

Target: `bn-Beng-IN/content/many-valued-logic/sequent-calculus/structural-rules.tex`
SHA-256: `cebeac76233733f3332c240f5f7af7945b8fcf43acb1c22c34e681030c7b2d78`

### OLP-0406 — selected propositional rules

Reverse paraphrase: an `$n$`-sided rule depends on the connective's characteristic truth function, so equal truth functions across logics give equal rules. The chapter displays negation rules for Łukasiewicz/Kleene and separately for Gödel, including the absence of a Gödel Undef-negation rule. It then gives shared conjunction and disjunction rules for Łukasiewicz, strong Kleene and Gödel, followed by separate implication rule families for Łukasiewicz, strong Kleene and Gödel. The sideways Łukasiewicz derivation and its translated caption remain present. Every formal rule tree, rule label, truth-value position and conclusion is byte-equivalent after whitespace normalization.

Target: `bn-Beng-IN/content/many-valued-logic/sequent-calculus/propositional-rules.tex`
SHA-256: `e436e94d30eb8ab784d47ce17bbb21c557de353130783646afb788952795ff14`

The target comment headers normalize the frozen source's erroneous part/chapter metadata in the driver and selected sections. These are non-rendered comments; file IDs, imports, labels and references remain source-identical.

## Audited source corrections

- `BN-SRC-329`: the first displayed antecedent ends at `A_n`, but its associated conjunction ends at `A_m`. Antecedent and succedent lengths may differ; the target uses `A_m` and retains `B_n`.
- `BN-SRC-330`: the initial-sequent explanation uses `\pValue(!A)` without the command's mandatory valuation argument. The target supplies `{v}`, as required by the macro declaration and the surrounding valuation equations.
- `BN-SRC-331`: the general `$n$`-sided definition says “each Γ₁” after displaying Γ₁ through Γₙ. The target states “each Γᵢ,” ranging over all positions.

Each correction has an adjacent Bengali note, frozen-source identity, target marker span, review question and exact audited-source transformation. Notes are excluded from formula parity. No source rule or semantic condition is silently changed.

## Structural and mathematical QA

- Source/target block counts: `54/54`; translated/unchanged: `37/17`.
- Protected `\olfileid`, `\olimport`, rule labels and semantic tokens: exact after audited corrections.
- Environments, all displayed inference trees and formal formulas: exact except the three audited repairs.
- Unicode: all five targets NFC-normalized.
- Segment index after integration: 4,588 rows, 3,881 translated, SHA-256 `f0a6df2663a8b76dff052a833767954cbfb1b6dc9a3e80555c93df283eaaf48b`.

No TeX engine, BibTeX, Biber or latexmk process was launched for this source batch. Visual pagination and cumulative PDF/HTML/EPUB integration remain deferred to the next reader tranche; no new reader release is claimed.
