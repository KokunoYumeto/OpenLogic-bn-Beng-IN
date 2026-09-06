# First-order Logic syntax and semantics semantic review (OLP-0149–OLP-0166)

Date: 2026-09-06
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete Syntax and Semantics chapters of the First-order Logic part: eighteen source units from `syntax.tex` through `semantic-notions.tex`. The reviewed units contain 369 source blocks: 332 contain Bengali linguistic translation and 37 are unchanged structural or formal blocks. Every block has exact source and target byte and line spans in `SEGMENT_CANON_USE.jsonl`; canon passages are attributed only to translated blocks.

The complete batch passes source-to-target replay. Every source and target block count agrees. Correction-stripped mathematical fragments, protected controls, environment order, OpenLogic semantic tokens and Unicode NFC agree either literally or after the exact, enumerated transformations for `BN-SRC-088` through `BN-SRC-102`. The validator checks the multiplicity of every repaired source fragment before transformation, requires every adjacent correction marker, and then demands complete mathematical-fragment equality. Each finding is also recorded in `SOURCE_CORRECTIONS.jsonl` with the frozen file hash, target hash, controlling evidence and an open expert-review question.

The review fixed two draft-only parity slips before accepting the batch: the second singular `!!{variable}` token in `assignments.tex` was restored, and the malformed `\olref{ass}{cor:sat-sentence}` call in `extensionality.tex` was restored to `\olref[ass]{cor:sat-sentence}`. Both now match the frozen source’s semantic-token and protected-control inventories exactly.

This remains source-draft evidence. These units have not yet been integrated into the verified 18-unit reader. No new PDF, semantic HTML or final pagination is claimed; those fields remain pending until a mutex-guarded reader build and visual review are possible.

## Canon actually consulted

The following page images were consulted during drafting and chapter-level rereading. Index generation revalidated every page-image hash and the hash of its preserved original. They establish India-standard Bengali academic style and adjacent logic, quantification, relation, variable, mapping, proof and finite-set usage. OpenLogic’s frozen source, formal definitions and displayed derivations remain the mathematical authority.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153 | গাণিতিক যুক্তি, উক্তি, সংযোজক and negation prose | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and variable language | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and quantified negation | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | NSOU university mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P019` | West Bengal school mathematics, PDF p. 189 / printed p. 10 | চল, ধ্রুবক and mathematical-expression prose | `c55d1f090e29adaf5053e21ad875b0c0e01c5d94f24afba0f9b6fad04da80c00` |
| `BN-IN-P020` | West Bengal school mathematics, PDF p. 227 / printed p. 48 | equality-operation and উভয় পক্ষ prose | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P023` | NSOU university mathematics, PDF p. 371 / printed p. 366 | mapping, domain/codomain, bijection and identity-map language | `adcd9898538fe4d9015062edc664142f460e0e9e27aa4952b15eec36b413f0f2` |
| `BN-IN-P025` | NSOU university mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, theorem structure and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |
| `BN-IN-P027` | NSOU university mathematics, PDF p. 324 / printed p. 319 | সসীম সেট, অসীম সেট and empty-set distinctions | `74f9f4ec28833932ff66e625febe150affa52896a5e202179255c8cd52e8658e` |
| `BN-IN-P028` | NSOU university mathematics, PDF p. 325 / printed p. 320 | finite cardinality, set-size examples and empty-set cardinality | `0e2aee7c091db5be3edfd99b16db531fefb078d88d099343e773684d5da639bb` |

Decisions `BN-IN-T060`, `BN-IN-T063`, `BN-IN-T065`, `BN-IN-T078` and `BN-IN-T096` through `BN-IN-T100` continue to govern the chapter. New decisions `BN-IN-T101`, `BN-IN-T102`, `BN-IN-T103`, `BN-IN-T104` and `BN-IN-T105` record structural-decomposition terms, induction principles, variable assignments and variants, covered and standard structures, free logic, extensionality and Skolem normal form. Sparse specialized compounds remain explicitly provisional and open to correction.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were made from the Bengali targets and compared with the frozen English units. They sample every unit and every major semantic function; the segment index supplies exhaustive block-level coverage.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0149` | 11 (1) | `B001–B011` | The Syntax driver preserves the chapter identity, title, attribution and all nine imports in source order. No imported section is duplicated or omitted. |
| `OLP-0150` | 3 (2) | `B002–B003` | A first-order vocabulary supplies symbols from which strings are formed; syntax identifies the strings that are terms, formulas and sentences. The chapter will also establish unique parsing and structural-induction principles. |
| `OLP-0151` | 18 (16) | `B002–B018` | A first-order language has denumerably many variables, logical symbols and an arbitrary nonlogical vocabulary of constants, predicates and functions with fixed arities. The arithmetic, set-theory, order and empty vocabularies preserve every symbol class, arity and infix convention. |
| `OLP-0152` | 39 (37) | `B002–B039` | Terms begin with variables and constants and close under function application. Atomic formulas apply predicates to the right number of terms or identify two terms; formulas close under the selected connectives and quantifiers, and nothing else qualifies. The term and formula induction principles follow exactly these constructors. `BN-SRC-088` removes one unmatched parenthesis from the defined conditional abbreviation. |
| `OLP-0153` | 36 (35) | `B002–B036` | Unique readability means each term or formula has one outer constructor and uniquely determined immediate constituents. The proof proceeds by string length, uses symbol-class disjointness and the no-proper-prefix lemma, and retains every term, connective and quantifier case. |
| `OLP-0154` | 15 (14) | `B002–B015` | The main operator is the outermost connective or quantifier of a nonatomic formula. The table maps each form to its operator and conventional name, and induction shows exactly one operator applies. `BN-SRC-089` places the conjunction’s closing parenthesis inside math mode. |
| `OLP-0155` | 19 (17) | `B002–B019` | Immediate subformulas are determined by the outer constructor; all subformulas arise recursively from them, and proper subformulas exclude the whole formula. The relation is transitive, and a formula of length n has at most 2n+1 subformulas. |
| `OLP-0156` | 30 (29) | `B002–B030` | Formation sequences give finite bottom-up witnesses for terms and formulas. Strong induction yields existence; the shortest sequence ending in an expression is unique even though longer sequences may repeat or contain unused material. `BN-SRC-090` supplies exactly k function arguments, `BN-SRC-091` retains the arbitrary language L, and `BN-SRC-092` makes every final-member case concern A_n under syntactic identity. |
| `OLP-0157` | 15 (13) | `B002–B015` | Variable occurrences are tracked through atomic formulas and constructors. A quantifier binds corresponding occurrences in its scope; all other occurrences are free. Sentences have no free occurrences, and the recursive free-variable clauses preserve each constructor and binding subtraction. |
| `OLP-0158` | 23 (22) | `B002–B023` | Term substitution is homomorphic. Formula substitution is defined only when the replacement term is free for the variable, with quantifier clauses preventing capture. Every example, free-for test and simultaneous distinction is retained. |
| `OLP-0159` | 9 (1) | `B001–B009` | The Semantics driver preserves its identity and all seven imports in source order: introduction, structures, covered structures, satisfaction, assignments, extensionality and semantic notions. |
| `OLP-0160` | 4 (3) | `B002–B004` | Semantics assigns values to terms, gives formulas satisfaction conditions in structures, and defines validity, consequence and satisfiability. Because open subformulas contain free variables, satisfaction is first defined relative to assignments. |
| `OLP-0161` | 10 (9) | `B002–B010` | A structure supplies a nonempty domain and arity-correct interpretations of constants, predicates and functions. The natural-number structure is the standard arithmetic model; HF interprets membership over hereditarily finite sets. Allowing empty domains or nondesignating names leads to free logic and alters existential generalization. |
| `OLP-0162` | 7 (6) | `B002–B007` | Closed-term values are defined without a variable assignment. A structure is covered when every domain element is the value of a closed term. The numeral-and-operation example evaluates the displayed composite term to 6 and retains the standard-model exercise. |
| `OLP-0163` | 44 (43) | `B002–B044` | An assignment maps every variable into the domain; term values and formula satisfaction are recursive, and quantified clauses range over the appropriate x-variants. The worked four-element structure retains every value and truth calculation. `BN-SRC-093` through `BN-SRC-099` repair the relation interpretation, two unmatched parentheses, one internal comma, the false conditional clause, a missing m, an n/m summary mismatch and a false (2,4) counterexample. |
| `OLP-0164` | 47 (46) | `B002–B047` | A term’s value depends only on assignments to its variables, and a formula’s satisfaction depends only on assignments to its free variables. The structural proofs preserve every base, connective and quantifier case. Sentences therefore have assignment-independent truth, supporting assignment-free satisfaction notation. `BN-SRC-100` restores the tuple’s first term t_1; `BN-SRC-101` builds the two universal-case variants from s_1 and s_2 respectively. |
| `OLP-0165` | 19 (18) | `B002–B019` | Extensionality says satisfaction depends only on the domain and interpretations of symbols actually occurring in the formula. The term and formula substitution propositions connect syntactic substitution with assignment modification. `BN-SRC-102` adds the required condition that t-prime be free for x in A. |
| `OLP-0166` | 20 (20) | `B001–B020` | A structure satisfies a sentence when every assignment does, a sentence is valid when every structure satisfies it, Gamma entails A when every Gamma-model satisfies A, and a set is satisfiable when one structure satisfies all its members. The quantified consequences and tagged variants preserve their distinct universal and existential conditions. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-088` | `OLP-0152` | Removed one unmatched closing parenthesis from the conditional abbreviation. | Exact one-for-one mathematical-fragment transformation. |
| `BN-SRC-089` | `OLP-0154` | Moved the closing math delimiter after the conjunction parenthesis. | Exact one-for-one mathematical-fragment transformation. |
| `BN-SRC-090` | `OLP-0156` | Changed `m_0,…,m_k` and the corresponding application to end at `m_{k-1}`. | Exact two-fragment, multiplicity-aware transformation. |
| `BN-SRC-091` | `OLP-0156` | Replaced both undefined `L_0` occurrences by the theorem parameter `L`. | Exact two-occurrence transformation scoped to the theorem. |
| `BN-SRC-092` | `OLP-0156` | Restored `A_n` throughout the final-member cases and `\ident` in the conjunction case. | Exact ten-fragment replay scoped to the uniqueness theorem. |
| `BN-SRC-093` | `OLP-0163` | Removed `[s]` from the fixed interpretation `\Assign{R}{M}`. | Exact one-for-one transformation. |
| `BN-SRC-094` | `OLP-0163` | Removed a surplus opening parenthesis from two defined-existential formulas. | Exact two-occurrence transformation. |
| `BN-SRC-095` | `OLP-0163` | Removed the comma inside the existential formula. | Exact one-for-one transformation. |
| `BN-SRC-096` | `OLP-0163` | Restored false `R(x,a)` as the antecedent for `m=2,3,4`. | Exact formula replay plus target-prose assertion. |
| `BN-SRC-097` | `OLP-0163` | Restored the missing variable in `m=2`. | Exact one-for-one transformation. |
| `BN-SRC-098` | `OLP-0163` | Changed the universal summary from all `n` to all `m`. | Exact one-for-one transformation. |
| `BN-SRC-099` | `OLP-0163` | Used witnesses `(m,n)=(1,4)` and `(2,1)` instead of false witness `(2,4)`. | Exact multiplicity-aware witness replay plus target-prose assertion. |
| `BN-SRC-100` | `OLP-0164` | Began the predicate tuple with `t_1` rather than `t_i`. | Exact one-for-one transformation. |
| `BN-SRC-101` | `OLP-0164` | Defined the variants from `s_1` and `s_2` respectively. | Exact two-formula transformation. |
| `BN-SRC-102` | `OLP-0165` | Added that `t'` is free for `x` in `A`. | Exact source replay plus target-prose assertion. |

## Variety, script, register, notation and numeral assessment

One `bn-Beng-IN` edition remains the supported recommendation. It uses Bengali script and normalized modern India-standard academic Bengali. NSOU supplies university mathematical prose; the university philosophy scan anchors Bengali quantification and scope language; West Bengal and Tripura sources provide distinct school-level explanatory witnesses. Bangladesh Bengali, where recorded elsewhere in the canon inventory, remains a labelled contrastive witness and is not silently substituted for the India locale.

The evidence does not support splitting the edition by Bengali script, orthography, numeral practice, mathematical notation, register or Indian region. Formal material keeps Latin metavariables, Arabic indices, left-to-right mathematics, logical symbols, macro structure, labels and citations from the frozen source except for the fifteen documented repairs. Ordinary prose follows India-standard spellings; mathematical numerals remain as in the source. The recorded `মানক`/`প্রমিত` alternative for “standard” is an expert-review item, not a second edition.

## Retrospective expert-review index

The regenerated decision index covers all 105 current substantive terminology choices across the complete 165-unit draft. Each record carries the English concept, chosen Bengali, rationale, plausible alternatives, confidence, an explicit invitation to expert correction, representative frozen-source wording, and every target occurrence mapped to stable unit and source/target line spans. `TRANSLATION_DECISION_OCCURRENCES.csv` is the exhaustive occurrence view and `TRANSLATION_DECISION_INDEX.json` is its machine-readable companion. No external review response is required for continued production; provisional choices remain reversible and open to correction.

## Semantic conclusions and remaining gates

The translation preserves the distinction between strings and well-formed expressions, terms and formulas, atomic and compound formulas, immediate and transitive subformula relations, free and bound occurrences, and syntactic identity versus semantic truth. It keeps structures separate from assignments, interpretations separate from assignment-dependent term values, and satisfaction, validity, entailment and satisfiability under their correct quantifier patterns. The reverse paraphrase verifies all constructor cases, both quantifier cases and both assignment-independence proofs.

Remaining work for these units is reader integration, mutex-guarded TeX compilation, visual PDF inspection, semantic-HTML verification and final pagination backfill. Those gates remain distinct from the completed source-draft semantic review.
