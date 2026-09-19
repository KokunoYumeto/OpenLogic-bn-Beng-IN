# Semantic review: Second-order Logic Syntax and Semantics

Review date: 2026-09-19

Locale: `bn-Beng-IN`

Units: OLP-0322--OLP-0329

Scope: 74 aligned source/target blocks across the Second-order Logic part driver, the Syntax and Semantics chapter driver, introduction, terms and formulas, satisfaction, semantic notions, expressive power and domain-size section. Of these, 59 blocks contain reviewed Bengali translation and 15 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of second-order variable ranges, formation clauses, assignment-relative satisfaction, relation and function quantification, semantic consequence, relation definability, transitive closure and domain-size characterizations. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidate the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0322 | Second-order Logic part driver | 6 | 2 | Part identity and three imported chapters |
| OLP-0323 | Syntax and Semantics chapter driver | 9 | 2 | Chapter identity, scope note and six imported sections |
| OLP-0324 | Introduction | 4 | 3 | Extension from object variables to relation and function variables, standard semantics and quantified examples |
| OLP-0325 | Terms and formulas | 14 | 13 | Variable families, arity, metavariables and formation clauses |
| OLP-0326 | Satisfaction | 19 | 18 | Assignments, term values, variants, substitution assignments, quantifier clauses and worked examples |
| OLP-0327 | Semantic notions | 5 | 5 | Validity, entailment, satisfiability and unsatisfiability |
| OLP-0328 | Expressive power | 7 | 7 | Definability, identity without equality and transitive closure |
| OLP-0329 | Infinite and enumerable domains | 10 | 9 | Dedekind infinitude, finiteness, enumerability, `Inf`, `Fin` and `Count` |

## Source-level corrections carried into the Bengali draft

The following two corrections are marked next to the affected target passages and recorded in `SOURCE_CORRECTIONS.jsonl`. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-253 (OLP-0324):** both predicate arguments in the final explanatory formula use the declared object-variable form `\Obj{v_0}`. The frozen source uses an unbraced `\Obj v_0` once and raw `v_0` once, although the same formula immediately above uses the declared form in both positions.
* **BN-SRC-254 (OLP-0329):** the forward proof for `Count` maps the final member of a finite enumeration to itself. The frozen proof permits finite enumerations but later gives only the successor clause, which leaves the function undefined at the last index.

## Reverse-paraphrase checks

1. **Second-order scope and standard semantics:** first-order structures remain unchanged, while variable assignments gain values for relation and function variables. Under standard semantics, an (n)-place relation variable ranges over every subset of the (n)-fold domain and an (n)-place function variable ranges over every function from that power to the domain. The universal and existential examples therefore quantify over every, or at least one, subset of the domain.
2. **Terms and formulas:** each arity has a denumerable family of relation variables and a denumerable family of function variables. Function variables form terms when applied to the appropriate number of terms; relation variables form atomic formulas; both kinds admit universal and existential quantification. Metavariables remain distinct from the object-language variable symbols they range over.
3. **Assignments and satisfaction:** an assignment maps object variables to domain elements, relation variables to relations of the correct arity and function variables to functions of the correct type. Term values extend the first-order recursion by applying the assigned function. The four added satisfaction clauses vary only the quantified relation or function coordinate and range over all admissible values.
4. **Worked semantic examples:** the complement formula is satisfied exactly when the assigned unary relations are complements in the domain. Universal relation quantification makes the displayed sentence false under the full-domain assignment, while existential relation quantification permits a proper subset and its nonempty complement. The final exercise uses universal relation quantification to define the remaining connectives from universal quantification and implication.
5. **Validity, consequence and satisfiability:** the first-order definitions carry over unchanged once second-order satisfaction is fixed. Validity requires truth in every structure, entailment preserves truth from every structure satisfying the premise set, and satisfiability requires at least one satisfying structure.
6. **Expressive power:** quantification over subsets defines identity without using the equality symbol because identical objects belong to exactly the same subsets. Quantification over binary relations then defines the transitive closure of a relation as the least transitive relation containing it. The leastness clause quantifies over every transitive relation containing the original relation.
7. **Domain size:** `Inf` asserts the existence of an injective nonsurjective endomap and therefore characterizes Dedekind-infinite domains; `Fin` is its negation. `Count` asserts the existence of a starting element and an endomap whose every closed subset containing that start is the full domain, thereby characterizing finite or countably infinite enumerability. The corrected terminal self-map makes the forward construction total for finite enumerations, and `Inf \land Count` isolates the denumerable case.

## Terminology and authority scope

BN-IN-T268 records the second-order syntax and standard-semantics register; BN-IN-T269 covers formation vocabulary; BN-IN-T270 covers assignment and satisfaction; BN-IN-T271 covers the core semantic notions; BN-IN-T272 covers expressive power; BN-IN-T273 covers domain size; and BN-IN-T274 covers enumerability. Earlier decisions continue to govern sets, membership, powersets, relations, functions, identity, quantification, transitive closure, finiteness and countability. The linked canon pages support the surrounding India-standard Bengali set, logic, number, relation, function, variable and proof prose. They do not directly attest every complete second-order compound, so the new choices remain provisional, definition-governed and open to expert correction.

## Validation state

The per-unit checker passes all 328 translated target units. The cumulative index contains 3,857 aligned blocks: 3,268 translated and semantically reviewed, and 589 unchanged structural or formal blocks. This batch contributes 74 blocks, of which 59 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 328-unit public checkpoint with anonymous immutable-archive readback.
