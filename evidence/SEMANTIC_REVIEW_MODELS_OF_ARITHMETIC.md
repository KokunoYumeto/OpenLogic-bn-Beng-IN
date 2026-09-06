# Semantic review: Model Theory — Models of Arithmetic

This review covers OLP-0191 through OLP-0197, the complete frozen Models of Arithmetic chapter. I reread every Bengali block against its frozen English block, checked every displayed formula and source control, and reverse-paraphrased the mathematical claims. Canon passages actually used for translated blocks are recorded in `SEGMENT_CANON_USE.jsonl`; the page hashes and source identities are revalidated there.

## Scope and method

- OLP-0191 is the chapter driver; OLP-0192 through OLP-0197 are its six reader units.
- The block verifier reports 91 aligned blocks, all with source/target block parity, audited formula parity, protected-control parity, environment parity, semantic-token parity and NFC normalization.
- The seven imported reader units contribute 84 translated and semantically reviewed prose blocks; the chapter driver contributes seven unchanged structural blocks. Reader integration, TeX, PDF and semantic-HTML rendering remain pending because the shared TeX mutex is reserved by another lane.
- Source corrections BN-SRC-118 through BN-SRC-133 are disclosed beside the affected passage and in `SOURCE_CORRECTIONS.jsonl`. Correction-note formulas are excluded from ordinary source-formula parity and are checked by the exact public checker transformations.

## Unit review

### OLP-0191 — chapter driver

The chapter identity, six imports and model-theoretic hierarchy are retained. The driver introduces standard and nonstandard arithmetic models without adding a second chapter or changing reader reachability. Reverse paraphrase: this file is only the chapter assembly boundary, while the mathematical content remains in the six imported units.

### OLP-0192 — introduction

The standard model, the finite-string model, isomorphism motivation and incompleteness witness are retained. The finite-string domain is `{a}^*`, so its addition and multiplication arguments must be `a^n,a^m`; the length relation supplies the missing `<` interpretation (BN-SRC-118, BN-SRC-119). The consistency witness binds `x` as a proof code in `OPrf_PA(x, code(false))` (BN-SRC-120). Reverse paraphrase: a model must interpret every language symbol on its own domain, and a proof-code existential must actually bind the proof code.

### OLP-0193 — standard models

The standard natural-number structure, induction consequences, categoricity argument and characterization of successor are retained. In the surjectivity paragraph, an incomplete successor map fails because an element is missing from its range, not its already-whole domain (BN-SRC-121). Reverse paraphrase: the map has source `M` and target `M\{z}`, so surjectivity is exactly the assertion that every target element is hit.

### OLP-0194 — nonstandard models

The compactness construction, arbitrary finite subset argument, countable-model conclusion and relation to nonstandard elements are retained. The proof now handles a finite subset with no numeral equation before selecting a largest `k` (BN-SRC-122), and explicitly invokes downward Lowenheim--Skolem after compactness to obtain an enumerable model (BN-SRC-123). Reverse paraphrase: compactness gives existence; downward Lowenheim--Skolem supplies the claimed countability.

### OLP-0195 — models of Q

The `K` structure, operation table, order, and verification of the Robinson-Q axioms are retained. The sum explanation is parenthesized (BN-SRC-124); the sole nonstandard element is consistently `a` (BN-SRC-125); the all-nonstandard table row ends with `(b \nsplus a)^\nssucc` (BN-SRC-126); and the final arbitrary-element argument remains in `x` rather than switching to the example-specific `a` (BN-SRC-127). Reverse paraphrase: each case is governed by the domain and table just defined, so all names and substituted terms must remain within that structure.

### OLP-0196 — models of PA

The strict linear order, arithmetic blocks, nonstandard-block ordering, midpoint argument and countable-model conclusion are retained. The trichotomy display is balanced (BN-SRC-128); predecessor claims exclude zero (BN-SRC-129); four undefined `\oplus` symbols are restored to the chapter’s `\nsplus` operation (BN-SRC-130); and the rational-like denumerability conclusion is restricted to countable nonstandard models (BN-SRC-131). Reverse paraphrase: PA makes the order discrete at the element level, while the set of blocks is dense and denumerable only under a countability hypothesis.

### OLP-0197 — computable models

The computable natural-domain presentation of the Q example, transported operations, decidable order and Tennenbaum theorem are retained. The order relation’s set-builder condition binds `x`, matching its ordered-pair component (BN-SRC-132). The theorem states uniqueness of the computable PA model up to isomorphism, which permits computable presentations transported by a computable bijection while excluding computable nonstandard models (BN-SRC-133). Reverse paraphrase: computability is presentation-sensitive, so literal uniqueness of the underlying set is too strong; the invariant theorem is uniqueness up to isomorphism.

## Terminology and regional review

Decisions BN-IN-T127 through BN-IN-T133 record standard/nonstandard models, arithmetic theories, arithmetic blocks, computability, order scope, arithmetic operations and transport of structure. The checked university and school witnesses support the component Bengali roots; specialized model-theory compounds remain explicitly provisional and open to expert review. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. Bangladesh Bengali is not used as an overriding authority.

## Open verification

The source and semantic review are complete for this chapter. Final printed/PDF page fields, visual inspection of integrated reader pages, semantic HTML inspection and release-level archive readback will be recorded only after the reader is rebuilt under the global TeX mutex. The full 722-unit objective remains active.
