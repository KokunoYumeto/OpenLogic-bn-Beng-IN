# Model Theory Basics semantic review (OLP-0182–OLP-0190)

Date: 2026-09-06
Locale and script: `bn-Beng-IN`, Bengali (`Beng`)
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

## Scope and result

This review covers the Model Theory part driver and the complete **Basics** chapter: its chapter driver and the sections Reducts and Expansions, Substructures, Overspill, Isomorphic Structures, The Theory of a Structure, Partial Isomorphisms and Dense Linear Orders. The nine units contain 84 aligned source/target blocks, of which 68 contain translated prose. Every active paragraph, editorial paragraph, definition, theorem, proof, remark, enumeration, example and exercise prompt is present. Structural imports, the commented-out future import and formal displays retain their source order and active/commented state.

Every unit passes source-to-target replay. Source and target block counts agree; protected controls, environment order, OpenLogic semantic-token multisets and Unicode NFC agree. Mathematical fragments agree literally except for the four independently justified formula or proof-fragment repairs `BN-SRC-113` through `BN-SRC-115` and `BN-SRC-117`. Two prose repairs, `BN-SRC-112` and `BN-SRC-116`, preserve all source formulas and controls while correcting a missing domain qualification and the precise finiteness claim. The validator applies each mathematical repair to the frozen English source, asserts its unique source occurrence and adjacent correction marker, and then requires complete mathematical-fragment equality. `SOURCE_CORRECTIONS.jsonl` binds all six defects and targets to full-file hashes and records controlling evidence, repair policy and an expert-review question.

The semantic reread compared every Bengali block with its frozen English counterpart and independently reconstructed each definition and proof step. The parity pass restored plural semantic-token forms, the explicit owning structure in the substructure remark, two repeated formula metavariables and the source's combined sequence-variable fragment. These changes preserve the source's token and mathematical multiplicities while keeping the Bengali prose idiomatic. No placeholder or untranslated English prose remains; proper names, conventional theorem names, source-defined identifiers and OpenLogic semantic-token keys remain as required.

## Unit-level reverse paraphrase

| Unit | Blocks (translated) | Reconstructed content checked against the frozen source |
|---|---:|---|
| `OLP-0182` | 7 (2) | The part driver retains the model-theory identity, the warning that the material is incomplete and experimental, the Antonelli adaptation and omissions, the Arana work note, four chapter imports and the end hook. |
| `OLP-0183` | 10 (1) | The Basics driver retains all seven active section imports, the commented-out nonstandard-arithmetic import and the chapter end hook in source order. |
| `OLP-0184` | 7 (7) | A reduct forgets symbols outside the smaller language while keeping the same domain and common interpretations; an expansion supplies interpretations for added symbols. Satisfaction of sentences in the smaller language is invariant, and the one-predicate expansion notation interprets the new predicate as the chosen relation. |
| `OLP-0185` | 5 (4) | A substructure has a subdomain and agrees on every shared constant, function and predicate; the larger structure is its extension. In a purely relational language, restriction of each relation to a nonempty subset induces a substructure. `BN-SRC-112` supplies the nonempty condition required by the governing definition of a structure. |
| `OLP-0186` | 5 (5) | If a sentence set has arbitrarily large finite models, adding countably many pairwise-distinct constants yields a finitely satisfiable extension. Compactness gives a model in which all those constants differ, hence an infinite model. Negating a hypothetical first-order definition of infinitude gives the contradiction corollary. |
| `OLP-0187` | 10 (10) | Elementary equivalence means agreement on every sentence. Isomorphism is a bijection preserving constants, predicates and functions and therefore preserves term values, formula satisfaction and sentence truth. Automorphisms preserve parameter-free definable subsets. `BN-SRC-113` evaluates the recursive target term in `M'`; `BN-SRC-114` closes the outer `h` application. |
| `OLP-0188` | 10 (9) | The theory of a structure is the set of all sentences true in it and is complete in the sentence-or-negation sense. Any model of that complete theory is elementarily equivalent to the original structure. The real order and its enumerable elementary equivalent show that elementary equivalence need not imply isomorphism. |
| `OLP-0189` | 23 (23) | Finite partial isomorphisms with Forth and Back yield an isomorphism between enumerable structures. In a pure relational language they preserve all sentences. Quantifier rank and the recursively defined relations `I_n` connect bounded extension depth with agreement on formulas of bounded rank. `BN-SRC-115` makes the alternating construction reach `b_0`; `BN-SRC-116` forms the needed finite conjunction from representatives of finitely many logical-equivalence classes. |
| `OLP-0190` | 7 (7) | Six axioms define dense linear orders without endpoints. All finite partial isomorphisms between two enumerable models satisfy Forth and Back, so Cantor's theorem makes the models isomorphic. The rational order is the canonical enumerable model, and the final remark combines this with the real order's enumerable elementary equivalent. `BN-SRC-117` handles both an empty partial map and an already-mapped element before choosing a point in an interval. |

## Audited source repairs

| Finding | Unit | Frozen-source defect | Target action and constraint |
|---|---|---|---|
| `BN-SRC-112` | `OLP-0185` | The relational-language remark says any subset `N` determines a substructure, although `N` may be empty and the edition's structure definition requires a nonempty domain. | Added only the qualification that `N` is nonempty; the induced relation formula and all other content remain aligned. |
| `BN-SRC-113` | `OLP-0187` | The recursive calculation of a term's value in `M'` wrongly interprets the outer function symbol in `M`. | Changed that one interpretation to `M'`, matching the left-hand term value and the next homomorphism step. The same repair is present in the current upstream text. |
| `BN-SRC-114` | `OLP-0187` | The first line of the homomorphism calculation lacks the closing parenthesis for the outer application of `h`. | Restored exactly one closing parenthesis before `\notag`; every inner argument remains unchanged. The same repair is present in the current upstream text. |
| `BN-SRC-115` | `OLP-0189` | The even successor-stage clause writes `n+1=2r` and inserts `b_r`; its first application therefore starts with `b_1`, so it never guarantees `b_0` enters the range. | Uses `n=2r+1`, making the even successor stages insert `b_0,b_1,\ldots` while leaving the alternating construction unchanged. |
| `BN-SRC-116` | `OLP-0189` | The converse proof calls the syntactic set `T^a_n` finite, although the preceding proposition proves only finitely many formulas up to logical equivalence. | Chooses one representative of each equivalence class and takes their finite conjunction, the finite formula actually required by the proof. |
| `BN-SRC-117` | `OLP-0190` | The Forth proof immediately chooses mapped neighbors around `a`; those neighbors do not exist when the partial map is empty, and no strict-interval case applies when `a` is already mapped. | Takes `q=p` for an already-mapped `a`, chooses any target element for an empty map, and uses the source's interval cases only for the remaining nonempty case. |

## Technical claim audit

- Reducts and expansions keep one domain and preserve interpretations only for symbols in the common language. The satisfaction proposition is restricted to sentences of that smaller language.
- The substructure definition preserves function values on tuples from the smaller domain; it does not treat arbitrary subsets as substructures when functions or constants impose closure requirements. The purely relational shortcut is explicitly limited to nonempty subsets.
- Overspill uses arbitrarily large finite models to satisfy every finite set of distinctness constraints. It does not assume that one finite model realizes all countably many new constants.
- The isomorphism proof evaluates the source term in `M`, the target term in `M'`, and composes the assignment with the isomorphism in the correct direction. The theorem asserts only isomorphism implies elementary equivalence.
- `Theory(M)` contains exactly the sentences true in `M`. Its completeness proof uses classical bivalence, and the example correctly separates elementary equivalence from isomorphism through different cardinalities.
- The countable back-and-forth construction alternates domain and range coverage beginning with `a_0` and `b_0`. The elementary-equivalence theorem is stated first for pure relational languages; the function-symbol remark passes to generated substructures.
- Quantifier rank counts maximum nesting. The `I_{n+1}` clause requires both Forth and Back extensions, and the converse proof relies on finite equivalence classes rather than a literally finite syntactic formula set.
- The dense-order proof exhausts the least, greatest and between-neighbor positions only after the empty and already-mapped cases are settled. Density and absence of endpoints supply the new image in each remaining case.

## Terminology and edition scope

Decisions `BN-IN-T119` through `BN-IN-T126` record the model-theory editorial register, reducts and substructures, overspill, isomorphism and automorphism, complete theories, partial isomorphisms and back-and-forth, quantifier rank and bounded equivalence, and dense linear orders without endpoints. Each decision lists the India-standard Bengali rendering, alternatives considered, actual canon passages consulted, definition-controlled scope and an expert-review question. Specialized compounds remain provisional where the checked Bengali pages attest only their component concepts.

The chapter introduces no evidence for another script, orthography or regional edition. The active edition set therefore remains one `bn-Beng-IN` Bengali-script edition. Latin metavariables, structure names, `I_n`, proper names and conventional mathematical notation remain Latin where their formal identity requires it.

## Remaining release boundary

This is source-complete chapter evidence, not a reader release. No TeX attempt was made for this chapter. PDF rendering, glyph inspection, semantic HTML checks, printed-page locators and reader integration remain pending under the shared global TeX mutex policy.
