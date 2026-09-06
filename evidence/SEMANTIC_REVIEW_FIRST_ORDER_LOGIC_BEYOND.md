# First-order Logic Beyond semantic review (OLP-0174–OLP-0181)

Date: 2026-09-06
Locale and script: `bn-Beng-IN`, Bengali (`Beng`)
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`

## Scope and result

This review covers the complete First-order Logic **Beyond** chapter: its chapter driver and the sections Overview, Many-Sorted Logic, Second-Order Logic, Higher-Order Logic, Intuitionistic Logic, Modal Logics and Other Logics. The eight units contain 79 aligned source/target blocks, of which 64 contain translated prose. Every active paragraph, editorial paragraph, quotation, theorem, proof, enumeration, example, formula caption and exercise prompt is present. Structural imports and formal displays retain their source order and active/commented state.

Every unit passes source-to-target replay. Source and target block counts agree; protected controls, environment order, OpenLogic semantic-token multisets and Unicode NFC agree. Mathematical fragments agree literally except for the three independently justified and adjacent repairs `BN-SRC-109` through `BN-SRC-111`. The validator applies each exact repair to the frozen English source, asserts its unique source occurrence and correction marker, and then requires complete mathematical-fragment equality. `SOURCE_CORRECTIONS.jsonl` binds each defect and target to full-file hashes and records its controlling evidence, repair policy and expert-review question.

The semantic reread compared each Bengali block with its frozen English counterpart and reconstructed the target's claim without consulting the target wording. This caught two initially omitted repeated mathematical tokens: the second explicit `\Struct M` in the second-order definition of infinitude and the repeated `\sigma` classifying the variable stock in the higher-order term clauses. Both are restored. The reread also replaced an ambiguous Bengali paraphrase of “homomorphism” with the explicit technical loan `হোমোমরফিজম` and normalized “hypotheses” to `অনুমান`. No placeholder or untranslated English prose remains; proper names, conventional system names, source-defined object-language symbols and OpenLogic semantic-token keys remain as required.

## Unit-level reverse paraphrase

| Unit | Blocks (translated) | Reconstructed content checked against the frozen source |
|---|---:|---|
| `OLP-0174` | 10 (2) | The driver retains the chapter identity, Jeremy Avigad attribution, seven imports and part-level reuse intention exactly once and in source order. |
| `OLP-0175` | 5 (4) | A logic typically specifies a formal language and often a deductive system and intended semantics. Rival accounts connect logic with necessity, a-priori truth, form, interpretation independence or convention. Russell and Whitehead's logicism, the infinity and reducibility axioms, and Quine's objection to predicate quantification are all retained without choosing a philosophical side. |
| `OLP-0176` | 6 (5) | Many-sorted logic assigns variables, quantifiers, identities, functions and relations to distinct sorts. The French/German marriage example preserves both argument sorts and its conditional. The first-order embedding combines domains, uses unary sort predicates, relativizes quantifiers, requires disjointness and typing axioms, and transfers sentences, derivations, structures and completeness. `BN-SRC-109` restores the inner universal quantifier's opening variable bracket. |
| `OLP-0177` | 14 (13) | Second-order logic quantifies over relations. Relation equality is extensional; substitution of definable relations motivates comprehension. The predicative/impredicative distinction, weak/full semantics, proof-system ambiguity and completeness tradeoff remain explicit. Full semantics yields categorical arithmetic, expresses infinitude, well-ordering and graph connectedness, but lacks effective completeness, compactness and Löwenheim--Skolem. Weak semantics becomes many-sorted first-order logic in disguise. `BN-SRC-110` makes the successor-injectivity axiom use the declared prime notation. |
| `OLP-0178` | 8 (7) | Higher-order logic iterates object and set levels and is presented through function and product types. The finite-type and term formation clauses preserve every type, recursion operator, application, lambda abstraction, pair and projection. Full function-space semantics is too strong for effective completeness; weaker typed structures support completeness. Church's simple type theory and constructive higher-type interpretations remain. `BN-SRC-111` restores `\tau` as the lambda-bound variable's domain type. |
| `OLP-0179` | 24 (23) | The Riemann-number story and both irrational-power proofs distinguish classical existence from explicit construction. Constructive existence and disjunction, Brouwer/Heyting/Bishop motivations, every BHK clause, Curry--Howard, the three equivalent classical schemata and the Gödel--Gentzen double-negation translation are retained. The classical/intuitionist dialogue keeps its two viewpoints. Kripke states, monotonic valuation and all five forcing clauses support the final countermodel exercise. |
| `OLP-0180` | 7 (6) | The opening conditional motivates necessity beyond material truth. Box and diamond retain necessity/possibility duality. Possible worlds and accessibility give Kripke semantics; intensional and extensional readings remain distinct. Provability, epistemic and temporal interpretations are retained. Every S4/S5 axiom and rule remains literal, with reflexive/transitive and universal frame conditions respectively. |
| `OLP-0181` | 5 (4) | The survey keeps the playful invitation to design a syntax, deduction system and semantics, then distinguishes fuzzy, probabilistic, default, nonmonotonic, epistemic, causal and deontic logics by their intended reasoning domains. The Leibniz closing claim remains deliberately qualified rather than asserted as achieved. |

## Audited source repairs

| Finding | Unit | Frozen-source defect | Target action and constraint |
|---|---|---|---|
| `BN-SRC-109` | `OLP-0176` | The displayed marriage formula writes `\lforall x]`, omitting the opening bracket around the inner quantifier's variable argument. | Changed only that occurrence to `\lforall[x]`; the remaining matrix and both quantifier scopes are identical. |
| `BN-SRC-110` | `OLP-0177` | The arithmetic vocabulary declares successor with prime notation, but its injectivity axiom alone switches to undeclared `s(x)` and `s(y)`. | Replaced those two terms with `x'` and `y'`, matching the declaration, the surrounding recursion axioms and the later model construction. |
| `BN-SRC-111` | `OLP-0178` | Item (6) assigns bound variable `x` type `\tau` and the lambda term type `\tau \to \sigma`, but the explanation later calls `x` type `\sigma`. | Changed that explanatory type to `\tau`; `\sigma` remains the result term's type. |

The source's harmless English grammar slips (“your own a syntax,” “creatures studies,” “defined inductively follows,” and “an monotone”) have fluent Bengali grammar without altering any claim. They require no formal-source transformation because they change neither notation nor recoverable propositional content.

## Technical claim audit

- The many-sorted translation distinguishes a sort (`জাতি`) from the higher-order type (`টাইপ`). The first-order embedding preserves both domain union and unary-predicate relativization rather than claiming that sort information disappears without axioms.
- The second-order section keeps four separate choices: minimal versus full-comprehension deduction, and weak versus full semantics. It does not transfer completeness from weak semantics to full semantics.
- The categorical arithmetic argument preserves the injection proof from the first two axioms, the full-semantics use of the range set `P`, the induction proof of surjectivity and the final homomorphism step.
- The second-order infinitude sentence retains both injectivity and failure of surjectivity; its negation defines finitude. The well-ordering and graph-connectedness formulas retain all quantifier directions and polarity.
- The higher-order clauses preserve the direction of every function type. In particular, `\lambd[x][s]` has type `\tau \to \sigma`, application consumes a `\tau`, and the recursion operator has type `\Nat \to \sigma`.
- The intuitionistic examples do not claim that the first irrational-power proof supplies a witness. The BHK explanation requires explicit disjunct selection and existential witnesses. The double-negation theorem preserves both pure-logic and hypothesis-translated forms.
- Kripke forcing for implication quantifies over every future state `w' \geq w`; falsity is forced nowhere. The final De Morgan-style formula is presented only as a countermodel exercise.
- Modal `\Box` and `\Diamond` retain their dual definition. S4 and S5 are not conflated, and the necessitation rule remains separate from their displayed axioms.

## Terminology and edition scope

Decisions `BN-IN-T112` through `BN-IN-T118` record the chapter's philosophical overview, many-sorted logic, second-order logic, higher-order types, intuitionistic logic, modal logic and the closing survey. Each decision lists the India-standard Bengali rendering, alternatives considered, actual canon passages consulted, definition-controlled scope and an expert-review question. The specialized phrases remain provisional where the checked Bengali pages attest only their component concepts.

The chapter introduces no evidence for another script, orthography or regional edition. The active edition set therefore remains one `bn-Beng-IN` Bengali-script edition. Latin metavariables, names such as BHK/S4/S5, source-defined object-language identifiers and conventional mathematical notation remain Latin where their formal identity requires it.

## Remaining release boundary

This is source-complete chapter evidence, not a reader release. No TeX attempt was made for this chapter. PDF rendering, glyph inspection, semantic HTML checks, printed-page locators and reader integration remain pending under the shared global TeX mutex policy.
