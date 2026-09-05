# Tableaux semantic review (OLP-0098–OLP-0111)

Date: 2026-09-05
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete Tableaux chapter, fourteen source units from `tableaux.tex` through `soundness-identity.tex`. The units contain 166 source blocks. Of these, 132 contain Bengali linguistic translation and 34 are unchanged structural or formal blocks. Every block has a source and target span in `SEGMENT_CANON_USE.jsonl`; no translated block is assigned a canon passage that was not actually consulted.

The chapter passed one consolidated source-to-target replay after translation and repair. All fourteen source and target block counts agree. Correction-stripped mathematical fragments, protected controls, environment order, OpenLogic semantic tokens and Unicode NFC agree under fifteen exact source-correction transformations. The findings `BN-SRC-043` through `BN-SRC-057` are marked beside the repaired target passages, asserted by the checker and recorded in `SOURCE_CORRECTIONS.jsonl`.

This is a source-draft review. These units have not been added to the 18-unit reader, and no new PDF or semantic HTML result is claimed. Translation-decision occurrence records therefore leave final printed/PDF page fields explicitly pending until pagination rather than inventing page numbers.

## Canon actually consulted

The following page images were visually reread during this chapter review. Index generation revalidates each page-image hash and the hash of its original document. The pages support India-standard academic Bengali register and adjacent logical vocabulary. OpenLogic remains the mathematical authority, and Tableaux-specific terms stay provisional where the decision log says so.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153 | গাণিতিক যুক্তি, উক্তি, যৌগিক উক্তি, সংযোজক and negation prose | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and proof-oriented prose | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and quantified negation | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | University mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব, প্রতিসাম্য and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P020` | West Bengal mathematics, PDF p. 227 / printed p. 48 | সমান চিহ্ন, উভয় পক্ষ and equality-operation prose | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P025` | University mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, inverse-map proof and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |

Earlier decision `BN-IN-T074` governs `ট্যাবলো`, `সত্য-বৃক্ষ`, `চিহ্নিত সূত্র`, `সত্যমান-চিহ্ন` and open/closed branch. Two chapter-specific decisions were added. `BN-IN-T088` records rule applicability, construction check marks, branch-splitting rules and repeatable closed-term instantiation. `BN-IN-T089` records satisfaction of signed formulas, satisfiable branches and tableaux, the branch-preservation soundness argument, unsatisfiability and proof by contrapositive. Identity terminology continues under `BN-IN-T085`.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were produced from the Bengali targets and compared with the frozen English blocks. They sample every unit and every major semantic function. The segment index supplies complete block-level identity and span coverage.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0098` | 16 (3) | `B002–B003` | The chapter presents a signed analytic tableau system and imports the complete propositional, quantified, proof-theoretic, soundness and identity sequence. The `prfTab` tag controls tableau material. `BN-SRC-043` corrects the source’s stale reference to Natural Deduction. |
| `OLP-0099` | 8 (7) | `B003–B008` | A signed formula pairs a sentence with True or False. A tableau begins with signed assumptions and grows downward by rules. A branch closes when it contains both signs of one formula; a tableau closes when every branch does. The source distinction between the abstract derivation and its numbered construction display is retained. |
| `OLP-0100` | 13 (7) | `B003–B012` | Each connective has True and False expansion rules. Some add formulas on one branch, while others split the branch. Negation swaps the sign; Cut introduces the same formula under both signs on separate branches. Every premise, conclusion, branch shape and rule label agrees with the source. |
| `OLP-0101` | 11 (9) | `B003–B010` | True universal and false existential rules instantiate with a closed term and have no extra freshness condition. False universal and true existential rules introduce an eigenconstant absent above the inference. The invalid existential-to-universal counterexample shows why freshness matters. `BN-SRC-044` repairs two raw universal labels and `BN-SRC-045` preserves the closed-term restriction. |
| `OLP-0102` | 7 (5) | `B003–B007` | A formal tableau is a finite rooted tree whose initial trunk consists of assumptions and whose later nodes arise from correct rule applications to earlier occurrences on their branch. Closure is branchwise. The construction notation adds line numbers, justifications and check marks without changing the formal object. |
| `OLP-0103` | 14 (13) | `B003–B013` | Tableau construction starts from the signed assumptions, applies the unique eligible rule, marks an occurrence only after its rule has been applied on every open branch containing it, and closes branches as soon as a sign conflict appears. Branching order affects size but not correctness. `BN-SRC-046` separates the malformed ninth exercise into True `A or B`, True `not B` and False `A`. |
| `OLP-0104` | 9 (7) | `B003–B009` | For quantified tableaux, eigenvariable-sensitive rules are normally applied early because later constants can block freshness. The non-eigenvariable rules may be repeated with suitable closed terms already present on the branch. Both long worked constructions preserve their rule order and closure witnesses. `BN-SRC-047` restores closedness; `BN-SRC-048` restores line 4 as the reusable false existential. |
| `OLP-0105` | 21 (20) | `B003–B020` | The tableau counterparts of validity, entailment and satisfiability are theoremhood, derivability and consistency. Each definition uses a finite set of signed assumptions drawn from the premise set. Reflexivity, monotonicity, transitivity and compactness follow through finite witnesses and tableau transformations. `BN-SRC-049` restores the braces required for one finite subset. |
| `OLP-0106` | 16 (15) | `B003–B015` | Provability and inconsistency interconvert by replacing False `A` with True `not A`, or conversely, and applying the appropriate negation rule. Cut combines tableaux witnessing inconsistency under `A` and `not A`. `BN-SRC-050` keeps the two finite premise-set lengths independent; `BN-SRC-051` restores the true-negation premise; `BN-SRC-052` removes a duplicated “left.” |
| `OLP-0107` | 9 (8) | `B003–B009` | Closed tableaux establish the expected conjunction, disjunction and conditional provability facts. The proof trees retain both assumptions, every expansion and each closing pair. `BN-SRC-053` repairs eight malformed signed-formula calls without changing a single sign or formula. |
| `OLP-0108` | 6 (5) | `B003–B006` | Strong generalization replaces a false instance `A(c)` with a false universal while preserving closure when `c` is fresh for the premises and open formula. The two elementary quantified provability facts follow by one expansion each. `BN-SRC-054` removes a comma after the final assumption in the second proof introduction. |
| `OLP-0109` | 22 (21) | `B003–B022` | A structure or valuation satisfies a signed formula according to its sign. The soundness proof assumes a satisfiable branch and checks that each tableau rule leaves at least one satisfiable extended branch. Therefore a closed tableau cannot have satisfiable assumptions. Validity, semantic consequence and satisfiable-implies-consistent follow as corollaries. `BN-SRC-055` makes each universal case use one coherent formula metavariable. |
| `OLP-0110` | 8 (7) | `B003–B008` | Identity rules add reflexive True identities and substitute identical closed terms under either truth sign. The examples derive substitutability, symmetry and transitivity. `BN-SRC-056` restores `s_1=s_2` as the result of substituting `s_2` into the declared open formula `s_1=x`. |
| `OLP-0111` | 6 (5) | `B003–B006` | Reflexive identities are true in every structure. If two closed terms denote the same object, substitution preserves satisfaction of the open formula, so both True and False identity rules preserve a satisfiable branch. `BN-SRC-057` restores the True sign in the True-rule case and keeps the False case separate. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-043` | `OLP-0098` | Restored tableaux as the system controlled by `prfTab`. | Frozen and corrected editorial phrases asserted. |
| `BN-SRC-044` | `OLP-0101` | Replaced two raw `forall` rule labels with configurable `lforall`. | Exact command counts asserted. |
| `BN-SRC-045` | `OLP-0101` | Retained the closed-term condition while excluding only extra freshness. | Frozen overbroad sentence and corrected clause asserted. |
| `BN-SRC-046` | `OLP-0103` | Split one malformed assumption into three signed formulas. | Exact one-for-one formula-multiset transformation asserted. |
| `BN-SRC-047` | `OLP-0104` | Restored “closed” before the freely chosen term. | Frozen and corrected prose asserted. |
| `BN-SRC-048` | `OLP-0104` | Changed reusable line 3 to line 4. | Exact line-number formula transformation asserted. |
| `BN-SRC-049` | `OLP-0105` | Added braces around a finite subset. | Exact malformed/corrected formula transformation asserted. |
| `BN-SRC-050` | `OLP-0106` | Changed the last `Gamma_1` index from `n` to `m`. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-051` | `OLP-0106` | Applied True-negation to True `not A`. | Erroneous frozen premise and repaired rule application asserted. |
| `BN-SRC-052` | `OLP-0106` | Removed duplicated “left.” | Exact frozen typo and target direction asserted. |
| `BN-SRC-053` | `OLP-0107` | Restored eight two-argument `sFmla` calls. | Malformed and corrected macro-shape counts asserted. |
| `BN-SRC-054` | `OLP-0108` | Removed the trailing formula-list comma. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-055` | `OLP-0109` | Used `A` consistently in both universal soundness cases. | Exact five-occurrence formula transformation asserted. |
| `BN-SRC-056` | `OLP-0110` | Restored the declared identity substitution instance. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-057` | `OLP-0111` | Restored the True sign in the True-identity case. | Exact one-for-one signed-formula transformation asserted. |

## Semantic conclusions and remaining gates

The translation keeps formal tableaux distinct from the check marks and line annotations used while constructing them. It preserves branch-local rule application, the requirement that every branch close, the difference between branch-splitting and single-branch rules, and the permission to repeat only the quantified rules whose closed terms have no eigenvariable condition.

The proof-theoretic chapters consistently separate syntactic derivability and consistency from semantic consequence and satisfiability. The soundness argument retains the direction from a satisfiable initial set through rule-preserving branch extension to the impossibility of closure. Identity prose preserves logical identity, ordinary equality notation, substitution direction and the two truth signs.

The remaining gates for these units are reader integration, a mutex-guarded TeX build, visual PDF inspection, semantic-HTML verification and pagination backfill in the occurrence ledger. Those gates remain separate from this completed source-draft semantic review.
