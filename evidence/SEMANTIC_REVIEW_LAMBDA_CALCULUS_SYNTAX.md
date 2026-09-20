# Semantic review: Lambda Calculus Syntax foundations

Review date: 2026-09-20

Locale: `bn-Beng-IN`

Units: OLP-0356--OLP-0360

Scope: 48 aligned source/target blocks across the Lambda Calculus Syntax chapter driver and its first four sections: terms, unique readability, abbreviated syntax, and free variables. Of these, 37 blocks contain reviewed Bengali translation and 11 are unchanged structural import blocks in the chapter driver.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of inductive term formation, abstraction and application, fully parenthesized syntax, unique formation, proper initial parts, the three abbreviation conventions, lambda scope, shadowing, free and bound occurrences, recursive free-variable sets, environments, closed terms, and combinators. Every source/target pair passes block-count, audited-mathematics, protected-control, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index generation revalidates the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0356 | Syntax chapter driver | 12 | 1 | Bengali chapter identity and all ten imports in frozen-source order |
| OLP-0357 | Terms | 6 | 6 | Variable supply, three formation clauses, abstraction/application, full parentheses, formation analysis, and exercise |
| OLP-0358 | Unique readability | 11 | 11 | Starting-symbol lemmas, proper initial parts, formation induction, three-way unique decomposition, and exact metavariable preservation |
| OLP-0359 | Abbreviated syntax | 5 | 5 | Left-to-right application, widest abstraction scope, multiple abstraction, full expansion example, and exercise |
| OLP-0360 | Free variables | 14 | 14 | Scope and shadowing, free/bound occurrences, recursive free-variable clauses, exercises, environment dependence, closed terms, and combinators |

## Source review outcome

One source-level defect was corrected with an adjacent Bengali note and an exact validator transformation.

1. **BN-SRC-275 (OLP-0360):** after introducing an occurrence of `\lambd[x][M]` inside an enclosing term `N`, the frozen definition says that the corresponding occurrence of `N` is the scope of `\lambd[x]`. The formation clause makes `M` the abstraction body, and every following example identifies that body as the scope. The target therefore restores `M`; `N` remains only the enclosing term. The checker transforms exactly this second inline-math occurrence of `N` to `M` before comparing the mathematical streams.

The source comments at the heads of OLP-0358 and OLP-0360 say `Chapter: introduction`, while their paths, file identifiers, imports, and rendered chapter placement put them in Syntax. Because these are non-rendered maintenance comments and do not alter reader content or mathematical meaning, they are reported here rather than entered as target corrections. OLP-0357 also contains the ordinary prose misspellings `desginate` and `demnostrates`, and OLP-0359 says `From example`; the Bengali text renders the intended ordinary prose idiomatically. None changes a formal object or technical claim, so none receives a correction record.

## Reverse-paraphrase checks

1. **Term alphabet and metavariables:** lambda terms are built from an infinite variable supply, the lambda symbol, and parentheses. The object variables `v_0`, `v_1`, and the ellipsis retain their source macros. Lowercase `x,y,z,...` designate variables, while uppercase `M,N,P,...` designate arbitrary terms.
2. **Inductive formation:** a variable is a term; if `x` is a variable and `M` a term, `(\lambd[x][M])` is a term; and if `M,N` are terms, `(MN)` is a term. The Bengali definition preserves all three hypotheses and conclusions without treating metavariables as object-language symbols.
3. **Abstraction and application:** a term formed by the second clause is the result of abstraction, and the `x` attached to its lambda is the parameter. A term formed by the third clause is the result of application. The explanatory paragraph and labels continue the Introduction chapter's abstraction/application register.
4. **Formation analysis:** the official syntax is fully parenthesized even though later conventions reduce the written burden. In the worked term, the last constructor is an abstraction with parameter `x`; its body is an application of two terms; and each component is itself an abstraction. The exercise preserves the complete self-application term whose formation is to be described.
5. **Starting-symbol lemmas:** a term begins either with a variable or with a parenthesis, because those exhaust the three formation clauses. An application begins with two parentheses or with a parenthesis followed by a variable: after its opening parenthesis, its left component is itself a term and therefore satisfies the first lemma.
6. **Proper initial parts:** no proper initial part of a term is itself a term. The exercise asks for induction on term length, and the proposition uses this exact prefix fact to rule out two different splits of an application into left and right components.
7. **Unique formation, variable case:** if `M` is a variable `x`, abstraction and application cannot have produced it because both begin with parentheses. Its only formation is therefore the single variable clause. Both explicit occurrences of `x` remain present in the target.
8. **Unique formation, abstraction case:** if `M` has form `(\lambd[x][N])`, it is neither a single variable nor an application. It can arise only by abstraction from `N`, whose own formation is unique by the induction hypothesis.
9. **Unique formation, application case:** if `M=(PQ)`, it cannot be a variable; and the starting-symbol lemma prevents `P` from beginning with lambda in a way that would make the whole term an abstraction. A second split `(P'Q')` would make one of `P,P'` a proper initial part of the other. The proper-initial-part lemma excludes this, so `P` and `Q`, and then their formations, are unique. Every `P` and `Q` explicitly typeset in the source remains explicitly typeset in Bengali.
10. **Three-way decomposition:** the restated proposition gives exactly three and only three term forms: a uniquely determined variable `x`; an abstraction with uniquely determined parameter `x` and body `N`; or an application with uniquely determined components `P,Q`. This is a readable equivalent of the formation proposition, not a new syntax.
11. **Abbreviation conventions:** omitting parentheses makes application associate from left to right, so `MNPQ` expands to `(((MN)P)Q)`. Lambda abstraction takes the widest possible scope, so `\lambd[x][MNP]` is one abstraction over the whole application string. A lambda with several variables abbreviates nested single-variable abstractions. Both displayed example directions and the exercise are formula-identical to the source.
12. **Binding intuition and shadowing:** in `\lambd[x][M]`, the binder captures free occurrences of `x` in `M`, while an inner `\lambd[x][N]` binds its own body's occurrences and shields them from the outer binder. The target preserves the occurrence-level distinction and does not imply that every written `x` is governed by the nearest outer abstraction indiscriminately.
13. **Scope correction:** if `\lambd[x][M]` occurs inside `N`, the governing lambda's scope is the corresponding occurrence of its body `M`. It is not all of `N`. BN-SRC-275 makes the definition agree with the constructor and the examples without changing any other symbol.
14. **Worked free/bound classifications:** in `\lambd[x][xy]`, `x` is bound and `y` is free. In `\lambd[x][xx]`, both `x` occurrences are bound because both are free in the body `xx`. In `((\lambd[x][xx])x)`, the last `x` is outside the abstraction and free. In `\lambd[x][(\lambd[x][x])x]`, the inner lambda binds the penultimate `x`, while the outer lambda binds the final `x`; the two scopes remain distinct.
15. **Free-variable recursion:** `FV(x)={x}`; `FV(\lambd[x][N])=FV(N)\setminus\{x\}`; and `FV(PQ)=FV(P)\cup FV(Q)`. These clauses respectively handle variables, removal of the newly bound parameter, and union across application components. All set braces, operators, labels, and metavariables are preserved.
16. **Exercises:** the first exercise asks for the scopes of `\lambd[g]` and both `\lambd[x]` occurrences in the same displayed term. The second asks whether every variable occurrence is bound and by which abstraction. The third asks for the free-variable set of the nested `x,y,z` term. The Bengali prompts retain these three distinct tasks.
17. **Environment dependence:** a free variable acts as a reference to an external environment. In `\lambd[x][fx]`, `f` is free, so the term's value depends on the environment's value for `f`. Abstracting over `f` yields `\lambd[f][\lambd[x][fx]]`, which takes both inputs explicitly and no longer depends on an environmental `f`. The translation preserves this semantic explanation without identifying an environment with a lambda term.
18. **Closed terms and the closing lemma:** a term with no free variables is a closed term, or combinator. For `y\ne x`, membership of `y` in `FV(\lambd[x][N])` is equivalent to membership in `FV(N)`; and membership in `FV(PQ)` is equivalent to membership in at least one component's free-variable set. The proof remains an exercise, followed by the explicit problem reference.

## Terminology and authority scope

BN-IN-T298 records lambda-term formation, formation rules, fully parenthesized terms, and parameters. BN-IN-T299 records unique readability, unique formation, proper initial parts, and unique decomposition. BN-IN-T300 records abbreviated terms and the three parenthesis-omission conventions. BN-IN-T301 records scope, free and bound occurrences, environments, closed terms, and combinators. Existing BN-IN-T058, BN-IN-T097, BN-IN-T101, BN-IN-T249, and BN-IN-T286 through BN-IN-T290 continue to govern variables, parameters, proper initial parts, environments, lambda terms, abstraction/application, alpha-equivalence, binding, and reduction vocabulary where their senses recur.

The checked India-standard pages directly support variables, algebraic expressions, functions, mappings, and university proof and uniqueness prose. They do not directly attest every lambda-specific compound. Those choices are definition-governed, explicitly provisional, and open to expert correction. The new decisions record alternatives and exact target occurrences without claiming unlisted dictionary or expert consultation.

## Validation state

The per-unit checker recognizes all 359 translated target units and passes OLP-0356--OLP-0360 individually. The cumulative index now contains 4,093 aligned blocks: 3,454 translated and semantically reviewed, and 639 unchanged structural or formal blocks. This batch contributes 48 blocks, 37 translated and 11 unchanged. Evidence now has 285 source-correction records and 301 translation decisions, 282 of them provisional, with 23,616 indexed target-line occurrences and 286 decisions tied to representative exact source wording. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 359-unit public checkpoint with anonymous immutable-archive readback.
