# Natural Deduction semantic review (OLP-0084–OLP-0097)

Date: 2026-09-05
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete Natural Deduction chapter, fourteen source units from `natural-deduction.tex` through `soundness-identity.tex`. The units contain 179 source blocks. Of these, 141 contain Bengali linguistic translation and 38 are unchanged structural or formal blocks. Every translated block has a segment record in `SEGMENT_CANON_USE.jsonl`; no translated block is assigned a canon passage that was not actually consulted.

The chapter passed one consolidated source-to-target replay after the semantic review and repairs. For all fourteen units, source and target block counts agree; correction-stripped formula multisets, protected controls, environments and semantic-token multisets agree under the explicit source-correction transformations; and every target is NFC-normalized. Ten source findings, `BN-SRC-033` through `BN-SRC-042`, are documented beside the repaired target passage and in `SOURCE_CORRECTIONS.jsonl`.

This is a source-draft review. The chapter has not been added to a reader build, and no PDF or HTML result is claimed here.

## Canon actually consulted

The following page images were visually reread during this chapter review. The segment-index generator also revalidated each image hash and the hash of its original document. The sources guide India-standard Bengali register and attested adjacent vocabulary; they do not supersede OpenLogic as the mathematical authority, and the specialized Natural Deduction compounds remain provisional where the decision log says so.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153; regional logic contrast | গাণিতিক যুক্তি, উক্তি, সংযোজক | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and proof-oriented prose | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and negation examples | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | University mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব, প্রতিসাম্য and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P020` | West Bengal mathematics, PDF p. 227 / printed p. 48 | equality prose using the same operation on উভয় পক্ষ | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P025` | University mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, inverse-map proof and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |

Two chapter-specific decisions were added. `BN-IN-T086` records the provisional tree vocabulary—`স্বাভাবিক নিষ্পাদন-বৃক্ষ`, `শাখা`, inference `পূর্বধারণা` and `সিদ্ধান্ত`, and `উপ-নিষ্পাদন/উপপ্রমাণ`. `BN-IN-T087` records the distinct freshness domains for universal introduction and existential elimination, avoiding a blanket condition that would incorrectly exclude the required displayed `A(a)` assumption.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were produced from the Bengali target without copying the English sentence structure, then compared with the frozen English block. They sample every unit and each major semantic function of the chapter. Full block-by-block structural coverage comes from the segment index and consolidated checker.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0084` | 16 (3) | `B002–B003` | The chapter presents a Gentzen/Prawitz-style Natural Deduction system and uses the `prfND` tag for proof-system material. Scope, attribution and editorial control are all retained. |
| `OLP-0085` | 7 (5) | `B003–B005` | A Natural Deduction proof mirrors informal mathematical reasoning: top nodes are assumptions; each lower sentence follows from one to three premise sentences; paired introduction/elimination rules manipulate the main operator; labels show which inference discharges which assumption. This matches the source after `BN-SRC-033` restores “sentences” for the mistakenly named “sequents.” |
| `OLP-0086` | 14 (8) | `B013–B014` | Negation introduction and the classical falsity rule differ in whether the conclusion is negated or positive. A displayed discharge is permission rather than obligation, so conditional introduction may discharge zero or more matching assumptions in the premise derivation. The rule distinction and zero case are preserved. |
| `OLP-0087` | 12 (9) | `B005`, `B008–B011` | Universal introduction requires a closed instantiating term and an eigenconstant absent from the conclusion and undischarged dependencies; existential elimination additionally excludes it from the major existential premise and conclusion while allowing it in the special discharged `A(a)` assumption. The invalid counterexample explains why freshness is required for soundness. The Bengali rule-specific summary agrees with the formal schemata. |
| `OLP-0088` | 8 (6) | `B004–B008` | A derivation from Γ to A is a finite sentence tree: top sentences lie in Γ or are discharged, A is the bottom sentence, and every other sentence is a premise of a correct inference immediately below it. The examples preserve substitution into a derivation and the fact that discharge remains optional. |
| `OLP-0089` | 15 (14) | `B003–B012` | Proof search starts from the desired bottom conclusion and works upward by its main operator. The larger example separates disjunction branches, discharges only dependencies actually needed, and uses the classical falsity rule to derive excluded middle when introduction alone cannot choose a disjunct. `BN-SRC-035` restores “terminal conclusion”; `BN-SRC-042` restores negation elimination on the step from not-A and A to falsity. |
| `OLP-0090` | 12 (11) | `B003–B009` | Quantifier proof search applies freshness-sensitive rules early. The first construction derives “if something is not A, then not everything is A” by existential elimination, negation introduction and universal elimination. The second combines an existential A-and-B premise with a universal B-implies-C premise to obtain an existential C conclusion while keeping the eigenconstant fresh. Formula roles and inference order are retained. |
| `OLP-0091` | 21 (20) | `B003–B020` | The syntactic counterparts of validity, entailment and satisfiability are theoremhood, derivability and consistency. The text preserves reflexivity, monotonicity, transitivity by splicing derivations, finite-premise notation, the three equivalent inconsistency conditions and compactness through the finite set of undischarged assumptions. |
| `OLP-0092` | 13 (12) | `B004–B013` | If Γ proves A while Γ together with A is inconsistent, Γ is inconsistent; Γ proves A exactly when Γ plus not-A is inconsistent; explicit contradiction and exhaustive inconsistency results follow by composing and discharging derivations. `BN-SRC-038` removes a duplicate renderer label while retaining the discharge-aware classical rule. |
| `OLP-0093` | 10 (9) | `B003–B010` | Natural Deduction supplies the connective facts needed later for completeness: conjunction projections and pairing, disjunctive inconsistency and injections, modus ponens, and two ways to derive a conditional. Every displayed dependency and optional discharge is retained. |
| `OLP-0094` | 9 (6) | `B004–B009` | Strong generalization adds universal introduction to a derivation of `A(c)` only when `c` occurs in neither Γ nor `A(x)`. Existential introduction and universal elimination then give the two elementary quantified derivability facts. The freshness restriction and both proof trees agree with the source. |
| `OLP-0095` | 28 (27) | `B005–B023`, `B026–B028` | Soundness is proved by induction on the number of inferences. The base is a single undischarged assumption; the step applies the induction hypothesis to the immediate subderivations and checks each rule semantically. The reviewed cases retain discharged-assumption unions, arbitrary structures or valuations, the universal-introduction reassignment argument, conditional truth, and the satisfiable-implies-consistent contrapositive. |
| `OLP-0096` | 9 (7) | `B003–B009` | Identity adds reflexive introduction and substitution in both directions for closed terms. The examples retain substitutability, symmetry/transitivity exercises and the backward construction that uses an existential uniqueness premise to show that any two A-objects are identical. |
| `OLP-0097` | 5 (4) | `B003–B005` | Reflexive identities are valid for every structure. For elimination, equal term values make satisfaction of `A(t1)` and `A(t2)` coincide under arbitrary assignments. The reverse elimination direction follows by exchanging the term roles, supplied explicitly under `BN-SRC-041`. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-033` | `OLP-0085` | Restored sentence nodes in the Natural Deduction tree. | Frozen phrase and corrected Bengali phrase both asserted. |
| `BN-SRC-034` | `OLP-0087` | Replaced the self-contradictory blanket eigenvariable summary with the two rule-specific conditions. | Source phrase, both corrected rule clauses and markers asserted. |
| `BN-SRC-035` | `OLP-0089` | Replaced stale end-sequent language with terminal conclusion. | Exact source phrase and corrected target phrase asserted. |
| `BN-SRC-036` | `OLP-0090` | Restored the missing negation in the cited existential major premise. | Exact one-for-one formula-multiset transformation asserted. |
| `BN-SRC-037` | `OLP-0090` | Replaced raw `exists` in the rule label with configurable `lexists`. | Exact source/target command counts asserted. |
| `BN-SRC-038` | `OLP-0092` | Removed a duplicate classical-falsity label directive. | Plain-label and discharge-label counts asserted. |
| `BN-SRC-039` | `OLP-0095` | Named a structure in FOL and a valuation in PL. | Exact tagged target alternatives and semantic-token preservation asserted. |
| `BN-SRC-040` | `OLP-0095` | Replaced raw `forall` in the rule label with configurable `lforall`. | Exact source/target command counts asserted. |
| `BN-SRC-041` | `OLP-0097` | Supplied the omitted reverse identity-elimination case. | Frozen one-direction proof and corrected symmetric-case prose asserted. |
| `BN-SRC-042` | `OLP-0089` | Restored negation elimination on the tree step from not-A and A to falsity. | One wrong source label becomes one additional correct label; all formulas and semantic tokens remain unchanged. |

## Semantic conclusions and remaining gates

The Bengali consistently distinguishes an assumption (`অনুমিতি`) from an inference (`অনুমান` or `অনুমান-বিধি`), and uses `পূর্বধারণা` and `সিদ্ধান্ত` for the premises and conclusion of an inference. Natural Deduction trees are never redescribed as sequents. The prose preserves the source distinction between syntactic derivability and semantic consequence, and between the classical falsity rule and the weaker intuitionistic rule.

Quantifier wording preserves closed-term restrictions, substitution direction and each eigenvariable exclusion domain. Identity wording preserves the difference between logical identity (`অভিন্নতা`) and ordinary equation prose (`সমতা`). The exact OpenLogic-specific compounds remain marked provisional in the decision log because the consulted canon supplies adjacent academic Bengali rather than direct attestation of the full terminology.

The remaining gates for these units are reader integration, a mutex-guarded TeX build, visual PDF inspection and semantic-HTML verification. Those gates are intentionally separate from this completed source-draft semantic review.
