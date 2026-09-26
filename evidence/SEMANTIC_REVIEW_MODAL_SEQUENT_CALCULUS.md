# Modal sequent calculus source chapter: semantic review

The Bengali source tranche covers frozen units OLP-0470–OLP-0474: chapter driver, introduction, K rules, K derivations and additional modal rules. The source itself labels the chapter a **draft** and says examples plus soundness and completeness proofs are missing. Its commented imports of soundness, more soundness and hypersequent sections remain commented. Translation of the five frozen files is complete; mathematical completeness of the source chapter is not claimed. This is a checked source tranche, not a new reader release.

The Tripura mathematical-reasoning page BN-IN-P008 and West Bengal university proposition, relation and proof pages BN-IN-P009, P013 and P025 were visually consulted on 2026-09-26. They support the Bengali proof and relation register, including প্রতিবিম্বী, প্রতিসম and পরিযায়ী. They do not directly attest modal sequent or hypersequent compounds. T073 and T079 fix সিকোয়েন্ট কলন and কর্তন, T324 fixes frame properties, and T348 records the provisional hypersequent term.

Reverse paraphrase samples checked against the frozen source:

| Unit | Bengali passage, paraphrased back into English | Invariant checked |
| --- | --- | --- |
| OLP-0470 | The chapter is a draft and its soundness and completeness proofs have not been written in the source. | Editorial status and active versus commented imports. |
| OLP-0471 | K adds a modal sequent rule to LK; S5 has no known cut-free complete ordinary LK extension of the displayed sort, while a cut-free complete hypersequent calculus exists. | Distinction between ordinary and hypersequent calculi, and the role of Cut. |
| OLP-0472 | A modal conclusion boxes every left-context formula and diamonds every right-context formula; in one-primitive variants the principal side has at most one formula. Empty contexts remain empty. | Both primitive choices, premise/conclusion orientation, and context restrictions. |
| OLP-0472 | If the principal side may contain arbitrarily many formulas, the two displayed hypothetical derivations lead to K-invalid formulas. Leaving side formulas unchanged under the modal step gives another pair of invalid results. | These trees demonstrate why the restrictions are required; they are not K theorems. |
| OLP-0473 | The Box example derives Box A and Box B imply Box(A and B); the Diamond example derives Diamond(A or B) imply Diamond A or Diamond B. The duality derivation and four exercises retain their formulas. | Sequent rules, signs, structural steps, and formulas. |
| OLP-0474 | T, D, B, 4 and 5 rule families are matched to reflexive, serial, symmetric, transitive and Euclidean frames. K4 derives axiom 4. The S5 examples derive axiom 5 under each primitive convention, while the last S5 derivation uses Cut for a valid formula unavailable cut-free in this system. | All three conditional tables, frame conditions, proof-tree conclusions, and the Cut distinction. |

BN-SRC-389 corrects one frozen-source rule label: the duality derivation moves an A from the right side of a sequent to its negation on the left, so the printed right-negation label must be left-negation. No displayed mathematical span changed. The checker confirms all five source/target block counts, mathematical spans, controls, environments, semantic-token counts and NFC, and it asserts the exact corrected proof-tree step. Formal rule tables and derivation trees were inspected as TeX source. No TeX build or PDF is claimed. The public HTML/EPUB reader remains at 299 units pending cumulative integration.
