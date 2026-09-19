# Semantic review: Second-order Logic and Set Theory

Review date: 2026-09-20

Locale: `bn-Beng-IN`

Units: OLP-0336--OLP-0340

Scope: 46 aligned source/target blocks across the Second-order Logic and Set Theory chapter driver, introduction, set-comparison, cardinality, and power-of-continuum sections. Of these, 37 blocks contain reviewed Bengali translation and 9 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of second-order set definitions, subset-cardinality comparison, Dedekind infinitude, enumerability, aleph cardinalities, relation-based power-set coding, continuum cardinality, CH, and NCH. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed. The source chapter's own editorial warning that its proofs are incomplete and its definitions or results may contain problems is retained prominently in Bengali.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidate the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0336 | Second-order Logic and Set Theory chapter driver | 7 | 2 | Chapter identity, editorial warning, and four imported sections |
| OLP-0337 | Introduction | 3 | 2 | Set-theoretic expression without primitive membership vocabulary |
| OLP-0338 | Comparing Sets | 12 | 11 | Subset, identity, nonemptiness, cardinal comparison, and Schröder--Bernstein |
| OLP-0339 | Cardinalities of Sets | 7 | 6 | Inf, Count, aleph-zero, aleph-one, and continuum motivation |
| OLP-0340 | Power of the Continuum | 17 | 16 | Relational coding, encoded power sets, Cantor, Cont, CH, and NCH |

## Source-level corrections carried into the Bengali draft

The following eight corrections are marked next to the affected target passages and recorded in `SOURCE_CORRECTIONS.jsonl`. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-259 (OLP-0338):** the no-larger-than formula restricts injectivity to pairs from `X`. The frozen formula unnecessarily requires a whole-domain injection, which an injection from `X` into `Y` need not extend to.
* **BN-SRC-260 (OLP-0338):** the equinumerosity formula likewise restricts injectivity to `X`, while preserving the map-into-`Y` and surjectivity-onto-`Y` clauses. It now expresses a bijection between the two subsets.
* **BN-SRC-261 (OLP-0339):** `Inf(X)` requires `u` to map `X` into itself and restricts injectivity to `X`. Without closure, the frozen formula can make a finite `X` satisfy the purported infinitude condition by mapping its members outside `X`.
* **BN-SRC-262 (OLP-0339):** `Count(X)` includes the empty set, keeps `u` on `X`, and restricts the least-closed-set condition to `Y` contained in `X`. The frozen formula makes every whole domain an eligible `Y`, so no proper subset can satisfy its minimality clause, and it also omits the empty enumerable set.
* **BN-SRC-263 (OLP-0339):** `Aleph_1(X)` explicitly includes `Inf(X)`. The frozen formula otherwise classifies every finite set as aleph-one because all its subsets are finite and it is not aleph-zero.
* **BN-SRC-264 (OLP-0340):** the proof of `Cont(Y)` refers consistently to subsets of `s(X)`. Its final frozen sentence unexpectedly says `s(Z)`, although no such fixed or free `Z` occurs in the proposition.
* **BN-SRC-265 (OLP-0340):** the domain-continuum sentence uses `Cont(Y)` and a genuine bijection from the whole structure domain onto `Y`: every value lies in `Y`, the map is injective, and every member of `Y` is hit. The frozen formula neither excludes duplicate subset codes nor requires all map values to lie in `Y`.
* **BN-SRC-266 (OLP-0340):** the Cantor sentence restricts injectivity to the code set `Y`. The surrounding prose denies an injection from `Y` into `X`, whereas the frozen subformula instead requires injectivity on the entire structure domain.

## Reverse-paraphrase checks

1. **Second-order set theory:** because second-order variables range over subsets and functions on the domain, unions, intersections, inclusion, cardinal comparisons, and Cantor-type statements can be expressed without adding membership as primitive nonlogical vocabulary. The Bengali phrase `যুক্তিবহির্ভূত` preserves this technical logical/nonlogical contrast; the misleading ordinary sense of `অযৌক্তিক` was also harmonized in OLP-0277 and decision T278.
2. **Basic set relations and cardinal comparison:** universal implication defines subset, universal biconditional defines set identity, and existential membership defines nonemptiness. An injection from `X` into `Y` defines no-larger-than; a map into `Y` that is injective on `X` and covers `Y` defines equinumerosity. Injections both ways yield equinumerosity by Schröder--Bernstein.
3. **Infinitude and enumerability of a subset:** `Inf(X)` asks for an injective nonsurjective endomap of `X`. `Count(X)` says either `X` is empty or `X` is generated from one seed by repeatedly applying an endomap; the corrected relative minimality condition prevents unrelated elements of the ambient domain from interfering.
4. **Aleph cardinalities:** `Aleph_0(X)` combines infinitude and enumerability. `Aleph_1(X)` requires `X` to be infinite and non-aleph-zero while every subset is finite or aleph-zero, expressing the first uncountable cardinal under the source's intended set-theoretic background. The continuum is the cardinality of the power set of the naturals, equivalently of the real line.
5. **Relation-based coding:** because second-order logic cannot quantify directly over sets of subsets, a binary relation `R` lets a domain element `x` code the set of all `y` related to it. `Codes` defines one code, and `Pow(Y,R,X)` says the elements of `Y` code exactly all subsets of `X`. This simulates the needed third-order quantification only when the ambient domain is large enough to supply the codes.
6. **Cantor and continuum size:** the corrected Cantor sentence denies an injection from the code set `Y` into `X`. `Cont(Y)` adds uniqueness of codes to the full power-set coding of an aleph-zero set, producing exactly continuum size. The corrected domain sentence then asserts a bijection between the entire domain and such a `Y`.
7. **CH and NCH:** `CH` identifies the aleph-one and continuum predicates across every subset. In small domains both may be absent, so simple invalidity of `CH` is not itself a validity expressing failure of the hypothesis. `NCH` instead says every continuum-sized set has a nonenumerable proper-cardinality subset, giving the stated validity characterization of the negated hypothesis.

## Terminology and authority scope

BN-IN-T281 records the second-order set-theory and nonlogical-vocabulary register; BN-IN-T282 covers definability and subset-cardinality comparison; BN-IN-T283 covers finite, enumerable, and aleph-cardinality vocabulary; BN-IN-T284 covers relation-based coding and simulated third-order quantification; and BN-IN-T285 covers continuum cardinality, CH, and NCH. Existing T005, T007, T024, T037, T040, T046, T047, T268, and T274 continue to govern subset, power set, continuum, mappings, cardinality, equinumerosity, Cantor/Schröder--Bernstein, second-order syntax, and enumerability. T278 now uses `যুক্তিবহির্ভূত` for nonlogical symbols to avoid the ordinary sense “irrational.” The linked canon pages directly support the set, power-set, finite/infinite, mapping, and finite-cardinality roots and the surrounding India-standard Bengali mathematical prose. They do not directly attest every higher-order coding or transfinite compound, so those complete choices remain provisional, definition-governed, and open to expert correction.

## Validation state

The per-unit checker passes all 339 translated target units. The cumulative index contains 3,949 aligned blocks: 3,340 translated and semantically reviewed, and 609 unchanged structural or formal blocks. This batch contributes 46 blocks, of which 37 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 339-unit public checkpoint with anonymous immutable-archive readback.
