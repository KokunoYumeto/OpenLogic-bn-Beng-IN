# Modal tableaux, first source tranche: semantic review

The Bengali source tranche covers frozen units OLP-0460–OLP-0464: the chapter driver (OLP-0460), the introduction, K rules, K proof examples, and K soundness. It is a checked **source** tranche, not a completed tableaux chapter or a new reader release. OLP-0465–OLP-0469 still require translation.

The Tripura mathematical-reasoning page BN-IN-P008 and the West Bengal university proposition, relation, and proof pages BN-IN-P009, P013, and P025 were visually reread for sentence and proof register. They support logic, relation, and argument phrasing. They do not directly attest the specialist prefixed-tableau vocabulary; T344–T346 record definition-governed choices, with T074 and T089 supplying established tableau terminology.

Reverse paraphrase samples checked against the frozen source:

| Unit | Bengali passage, paraphrased back into English | Invariant checked |
| --- | --- | --- |
| OLP-0461 | A signed tableau branches downward; a branch closes only when the same formula bears both truth signs. Derivability from Γ requires a closed tableau from the false conclusion and a finite true-premise subset of Γ. | Closure and finite-premise direction. |
| OLP-0461 | Prefixes are nonempty positive-integer sequences; σ.n extends σ and names a world accessible from σ's world. | Sequence domain, concatenation, and accessibility direction. |
| OLP-0462 | A K rule for true box or false diamond may use only a successor prefix already on the branch; false box or true diamond must introduce a new successor prefix. Closure compares both formula and prefix. | Used/new asymmetry and same-world contradiction. |
| OLP-0462 | Without those restrictions, two drawn closed trees would appear to prove invalid entailments between box and diamond. | These are deliberately invalid hypothetical derivations, not K theorems. |
| OLP-0463 | The box conjunction and diamond disjunction examples close both branches after the modal step at prefix 1.1. | Signs, worlds, and leaf closure. |
| OLP-0464 | The contrapositive starts from a world satisfying every B_i and falsifying A. The interpretation f maps prefixes to worlds and sends σ.n to an R-successor of f(σ). Each rule preserves at least one satisfiable branch. | Soundness direction and witness construction. |

The frozen source contains seven independently logged corrections. BN-SRC-366 restores the false conclusion in the opening countermodel. BN-SRC-367 and BN-SRC-369 replace A by B in the false-box and true-diamond rule conclusions. BN-SRC-368 restores modal-model and modal-satisfaction commands in those two witness cases. BN-SRC-370 changes the final corollary conclusion from derivability to entailment. BN-SRC-371 repairs the false-box justification label in a hypothetical tree. BN-SRC-372 restores the missing prefix on the false-disjunction exercise premise. All changed mathematical spans are exact exceptions in the source checker; the other math, control, environment, and semantic-token multisets match. The source's mistaken chapter comment was aligned with the tableaux chapter identity.

The five aligned source files were reviewed for Bengali prose, titles, captions, rule descriptions, and exercises. No TeX build or new PDF is claimed for this tranche. The public HTML/EPUB reader remains at the earlier 299-unit release pending cumulative reader integration.
