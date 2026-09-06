# First-order Logic models and theories semantic review (OLP-0167–OLP-0173)

Date: 2026-09-06
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete Models and Theories chapter of the First-order Logic part: seven source units from `models-theories.tex` through `size-of-structures.tex`. The batch contains 60 source blocks. Forty-seven blocks contain Bengali linguistic translation and thirteen are unchanged structural or formal blocks. Exact byte and line spans for every block are recorded in `SEGMENT_CANON_USE.jsonl`; canon passages are attributed only to linguistically translated blocks.

Every unit passes source-to-target replay. Source and target block counts agree; protected controls, environment order, OpenLogic semantic-token multisets and Unicode NFC agree. Mathematical fragments agree literally except for the six independently justified and adjacent repairs `BN-SRC-103` through `BN-SRC-108`. The validator applies each exact repair to the frozen English source, asserts the source-fragment multiplicity and correction markers, and then requires complete mathematical-fragment equality. `SOURCE_CORRECTIONS.jsonl` records each defect, source and target hashes, controlling evidence, repair policy and an expert-review question.

The semantic reread compared every Bengali paragraph with its frozen English counterpart. It corrected draft-only semantic-token multiplicities in OLP-0168, OLP-0169, OLP-0170, OLP-0171, OLP-0172 and OLP-0173; restored the repeated `$x$` and `$y$` identities and the literal relation fragment `$\subseteq X \times Y$` in OLP-0172; and made the minimality explanation for a mereological sum explicit in OLP-0170. No omission, placeholder or untranslated English prose remains in these seven targets.

This is source-draft evidence. The seven units have not yet been integrated into the built reader. No TeX process was launched for this batch, and no new PDF, semantic HTML, pagination or reader release is claimed.

## Canon actually consulted

These page images were consulted during drafting and chapter-level rereading. Index generation revalidates each page-image hash and the hash of its preserved original. They establish India-standard Bengali set, relation, mapping, quantification, proof, finiteness and cardinality usage. The frozen OpenLogic source and its formal definitions remain the mathematical authority.

| Passage | Page and role | Page-image SHA-256 |
|---|---|---|
| `BN-IN-P001` | NSOU, PDF p. 321 / printed p. 316: set definition and membership | `d0d40bee2e570baad552d278122504b0b1b51e5c36fe1545329c5da79b73fc78` |
| `BN-IN-P002` | NSOU, PDF p. 322 / printed p. 317: set-builder notation and membership | `745fe0e68b58e73b398e93812145882da8df69cfbaf06f0434d57ccdf16c155b` |
| `BN-IN-P006` | Tripura class XI mathematics, PDF/printed p. 8: finite, empty and equal sets | `a7cc3c439cb144f18df6a2b9b7b915380b0d57347cb02390ff1c7145ad963c0c` |
| `BN-IN-P007` | Tripura class XI mathematics, PDF/printed p. 9: subsets and power sets | `7b3af5d0d7ca4e67670de79351edda804c7f407c1519273e4057d36d3df8d360` |
| `BN-IN-P009` | Suri Vidyasagar College, PDF p. 1 / printed pp. 110–111: propositions and universal quantification | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | Suri Vidyasagar College, PDF p. 2 / printed pp. 112–113: existential quantification and scope | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P011` | NSOU, PDF p. 329 / printed p. 324: power-set definition and example | `9a0eb86bf6fe322767e5ea7668d6b0693888ad0b3e9866a9ee79cf5f88c3deb5` |
| `BN-IN-P013` | NSOU, PDF p. 365 / printed p. 360: relation and reflexivity | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P018` | NSOU, PDF p. 370 / printed p. 365: function, domain, codomain and range | `3ac3864f15dc0517325b9116e2f11ae57aeb40f50e7ba5782ecddf4a18645022` |
| `BN-IN-P023` | NSOU, PDF p. 371 / printed p. 366: injective, surjective and bijective mappings | `adcd9898538fe4d9015062edc664142f460e0e9e27aa4952b15eec36b413f0f2` |
| `BN-IN-P025` | NSOU, PDF p. 373 / printed p. 368: inverse-bijection proof and uniqueness | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |
| `BN-IN-P027` | NSOU, PDF p. 324 / printed p. 319: finite and infinite sets | `74f9f4ec28833932ff66e625febe150affa52896a5e202179255c8cd52e8658e` |
| `BN-IN-P028` | NSOU, PDF p. 325 / printed p. 320: finite cardinality and set-size examples | `0e2aee7c091db5be3edfd99b16db531fefb078d88d099343e773684d5da639bb` |

Decisions `BN-IN-T020`, `BN-IN-T023`, `BN-IN-T029`, `BN-IN-T032`, `BN-IN-T039`, `BN-IN-T040`, `BN-IN-T043`, `BN-IN-T070`, `BN-IN-T091`, `BN-IN-T094`, `BN-IN-T098`, `BN-IN-T100` and `BN-IN-T103` continue to govern overlapping terminology. New decisions `BN-IN-T106`, `BN-IN-T107`, `BN-IN-T108`, `BN-IN-T109`, `BN-IN-T110` and `BN-IN-T111` record the chapter’s axiomatic-method, example-theory, mereology, definability, set-foundational and model-size compounds. Specialized words without direct page attestation remain explicitly provisional and open to correction.

## Unit-by-unit comparison and reverse paraphrase

| Unit | Blocks (translated) | Reverse paraphrase and judgment |
|---|---:|---|
| `OLP-0167` | 8 (1) | The chapter driver retains its identity and imports introduction, structural properties, example theories, definable relations, set theory and structure size exactly once and in source order. |
| `OLP-0168` | 7 (7) | An axiomatic theory is the semantic closure of its axioms. An axiom system succeeds when exactly its intended structures model it; unintended models motivate stronger axioms. Models witness consistency, countermodels witness independence, and definability determines whether a relation needs its own primitive. Every implication and satisfiability test is preserved. |
| `OLP-0169` | 5 (4) | Sentences can distinguish structural properties. A model of a sentence set satisfies every member. The three displayed order axioms express reflexivity, antisymmetry and transitivity, so their models are exactly partial orders. |
| `OLP-0170` | 11 (10) | The examples preserve strict linear-order, group and Peano-arithmetic axioms, including the infinite induction schema. Pure sets are built without urelements; unrestricted comprehension makes the theory unsatisfiable. Mereological parthood is a partial order, the displayed sum is its least common upper bound, and the final supplementation principle retains proper parts, disjointness and fusion. `BN-SRC-103` repairs the pure-set extensionality quantifier. |
| `OLP-0171` | 10 (9) | A formula with specified free variables expresses a relation in a fixed structure through every matching assignment. The arithmetic formulas define order, successor and predecessor with the correct argument directions. The exercises preserve divisibility, primality, inverse, relative product, transitive closure and all finite/cofinite definability claims. `BN-SRC-104` restores the object-language variable macro in the second strict-order formula. |
| `OLP-0172` | 11 (10) | ZFC uses membership alone but defines subset, emptiness, union, power set, ordered pairs, products and functions through formulas. A function represented as pairs must lie in the product, be total on its source and have a unique value; injectivity requires equal outputs to imply equal inputs. Unrestricted comprehension yields Russell’s paradox, while separation restricts selection to a prior set. `BN-SRC-105` through `BN-SRC-107` restore the three malformed displays without altering their stated meanings. |
| `OLP-0173` | 8 (6) | Purely logical sentences express finite lower bounds, upper bounds and exact sizes. A structure is infinite exactly when it models every finite lower-bound sentence, but no single purely logical sentence expresses infinitude. Compactness and Löwenheim–Skolem imply the stated limits for finiteness and nonenumerability. `BN-SRC-108` restores the exact-size formula’s final quantifier closure. |

## Source findings resolved in this chapter

| Finding | Unit | Repair | Validation |
|---|---|---|---|
| `BN-SRC-103` | `OLP-0170` | Restored the opening and closing square brackets of the inner universal quantifier in the pure-set extensionality axiom. | Exact one-fragment audited-source transformation. |
| `BN-SRC-104` | `OLP-0171` | Restored `\Obj` before `v_2` in the second formula defining strict order. | Exact one-fragment audited-source transformation. |
| `BN-SRC-105` | `OLP-0172` | Put product membership, totality and uniqueness inside their intended implication and quantifier scopes. | Exact whole-`align*` transformation governed by the preceding three prose conditions. |
| `BN-SRC-106` | `OLP-0172` | Moved the two universal-quantifier closures to the end of the complete injectivity implication. | Exact whole-`multline*` transformation governed by the following definition. |
| `BN-SRC-107` | `OLP-0172` | Added the missing parenthesis closing the separation biconditional. | Exact one-fragment audited-source transformation. |
| `BN-SRC-108` | `OLP-0173` | Closed the exact-size disjunction before the universal-quantifier bracket and removed the surplus round parenthesis. | Exact one-fragment audited-source transformation. |

## Variety, notation and remaining gates

One `bn-Beng-IN` edition remains the supported recommendation. Bengali prose follows modern India-standard academic usage, with West Bengal university mathematics and philosophy plus Tripura school mathematics in distinct witness roles. Bangladesh Bengali remains only a labelled contrastive witness elsewhere in the canon inventory. The evidence gives no reason to split this chapter by script, orthography, register, notation or Indian region.

Formal material retains Latin metavariables, Arabic indices, left-to-right mathematics, OpenLogic controls and source hierarchy. The six displayed repairs are visible beside their targets and exhaust the mathematical differences. The chapter keeps model and structure, truth and satisfaction, expression and definition, element and subset, and finite size and nonenumerability distinct.

Remaining gates are integration into the full reader, mutex-guarded TeX compilation, visual PDF inspection, semantic-HTML verification and pagination backfill. Those gates remain separate from this completed source-draft semantic review.
