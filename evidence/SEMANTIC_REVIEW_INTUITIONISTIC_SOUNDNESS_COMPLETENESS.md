# Intuitionistic soundness and completeness: source-to-Bengali review

Frozen authority: OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`, units OLP-0503–OLP-0510. The eight source files have 75 aligned blocks: 66 translated prose blocks and nine structural/formal blocks. The cumulative checked draft has 509 of 722 units, 5,666 aligned blocks and 4,793 translated blocks. This is source-draft coverage; the published HTML/EPUB reader still covers 299 units.

## Meaning and reverse-paraphrase checks

| Unit | Bengali passage read back into English | Scope retained |
| --- | --- | --- |
| OLP-0503 | Soundness and completeness results are collected, while the editorial still says some provability facts used later must be stated and proved. | Seven chapter imports and the source's warning remain. |
| OLP-0504 | An induction on axiomatic derivation length handles an axiom, an assumption, and modus ponens; reflexivity lets implication be applied at the current world. | The two-argument satisfaction predicate is repaired at BN-SRC-400. |
| OLP-0505 | Natural-deduction soundness follows by induction over rule cases; the negation introduction and elimination cases remain exercises. | Both tag-controlled short exercise variants, the full proof cases and all three nonderivability problems remain. BN-SRC-401–404 repair four local formula/notation defects. |
| OLP-0506 | A prime set is consistent, deductively closed and has the disjunction property. The construction keeps A underivable and eventually resolves each eligible disjunction. | The fixed-index progress proof is repaired at BN-SRC-405; no theorem hypothesis or conclusion changed. |
| OLP-0507 | Worlds are finite sequences of natural numbers, ordered by prefix; a prime extension is attached when B does not derive C. | The valuation and monotonicity argument retain the original definitions. |
| OLP-0508 | At a sequence-world, a formula is true exactly when the associated prime set derives it. | The source's negation induction case is empty and remains empty. Thus the printed proof is incomplete; this review does not certify a complete proof. |
| OLP-0509 | If Γ fails to derive A, the root of the canonical model satisfies Γ and refutes A. | The contrapositive and all three exercises remain; the upstream truth-lemma gap still affects the written proof chain. |
| OLP-0510 | Every counterexample to A yields a finite one by retaining the truth of all subformulas of A, and parallel searches decide validity. | BN-SRC-406–408 repair an invalid quotient, correct the exercise's domain and notation, and explain the decision procedure. |

## Finite-model correction

The frozen OLP-0510 quotient identifies worlds by the propositional variables true there. This does not preserve intuitionistic negation or implication. For example, let `p` be false at worlds `w` and `v`, let `w` have no later `p`-true world, and let `v` have a later `p`-true world `u`. Both `w` and `v` have the same atomic `p` valuation, but `¬p` is true at `w` and false at `v`. The claimed induction over all formulas using variables from `P` therefore fails.

The target takes `Σ` to be the finite subformula set of the particular formula `A`, sets `T(w)={B∈Σ : M,w⊨B}`, orders the finitely many realized types by inclusion, and makes each variable true at precisely the types containing it. Persistence in the original model makes the new valuation monotone. An induction proves equivalence only for `B∈Σ`, which is what the theorem needs. In the implication step, if `B→C` belongs to `T(w)` and `T(w)⊆T(v)`, it also holds at `v`, so reflexivity gives `C` at `v` whenever `B` holds there. If `B→C` fails at `w`, an original successor witnessing `B` without `C` supplies an inclusion-larger finite type. Primitive negation has the analogous two directions. Thus `A` remains false at `T(w₀)` and the finite model has at most `2^|Σ|` worlds. The corrected exercise asks for this restricted induction. Finite monotone valuations on finite partial orders can be enumerated alongside derivations; soundness, completeness and the finite-model result guarantee termination on one side.

An academic primary source independently confirms the finite-model method: [Intuitionistic Logic, pp. 17–18, finite adequate subformula sets or filtration](https://www.math.uni-hamburg.de/home/khomskii/intuitionistic_old_2008/PP-2006-25.text.pdf). The explicit type construction and counterexample above are this translation audit's derivation, not a quotation from that source.

## Indian Bengali canon and limits

The indexed passages BN-IN-P007/P008/P009/P012/P013/P014/P025 were visually consulted earlier in this task and their preserved originals and page images were rehashed by the segment index. They support ordinary set, proposition, relation and proof language. They do not directly attest specialist labels such as prime set, canonical model or intuitionistic filtration. BN-IN-T369–T371 mark those compounds provisional and bind them to the exact source definitions. Every linguistically translated block has passage IDs and a non-fabricated consultation role in `SEGMENT_CANON_USE.jsonl`.

Structural comparison passed for all 509 present source units: frozen source hashes, 5,666 source/target block counts, audited math, protected controls, environments, semantic tokens and NFC. The nine documented findings are BN-SRC-400–408. This review does not claim a TeX render, a completed negation proof, cumulative reader integration or a full edition.
