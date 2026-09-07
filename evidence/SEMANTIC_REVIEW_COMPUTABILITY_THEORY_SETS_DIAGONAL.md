# Semantic review: Computability Theory — sets and diagonal arguments

This review covers OLP-0234 through OLP-0240: No Universal Computable Function, The Halting Problem, Comparison with Russell’s Paradox, Computable Sets, Computably Enumerable Sets, Equivalent Definitions of Computably Enumerable Sets and There Are Non-Computable Sets. I reread every Bengali block against its frozen English block, audited the displayed mathematics and protected controls, and reverse-paraphrased the definitions and proofs. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The seven units contain 6 + 6 + 8 + 5 + 5 + 15 + 9 aligned source/target blocks, for 54 aligned blocks in total. Of these, 53 contain Bengali translation and are marked `translated_semantically_reviewed`; OLP-0239-B001 is a formal-only block preserved byte for byte and marked `unchanged_structural_or_formal`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the six documented source repairs are normalized for comparison.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, set, logic, quantification, relation, function, mapping and proof language. Existing decisions BN-IN-T040, BN-IN-T044, BN-IN-T153, BN-IN-T168, BN-IN-T171, BN-IN-T173, BN-IN-T174, BN-IN-T178 and BN-IN-T180 govern enumeration, diagonalization, characteristic functions, partiality, indices and halting; BN-IN-T181 through BN-IN-T187 record this batch’s specialized terminology.
- BN-SRC-144 through BN-SRC-149 disclose and repair six frozen-source defects beside their affected arguments. No frozen English byte is changed.

## Unit review

### OLP-0234 — No Universal Computable Function

The theorem rules out a total computable function whose rows enumerate all total computable unary functions. Its diagonal adds one to the self-application row, making the result total and computable yet different from every indexed row. The explanation correctly retains the universal partial evaluator: it covers all total computable functions but escapes the contradiction because the evaluator itself is partial. The problem asks what happens when the analogous partial diagonal is evaluated at its own index. Reverse paraphrase: totality closes the diagonal inside the class and forces a contradiction, while undefinedness leaves room for a universal partial evaluator.

The frozen opening calls the partial evaluator “total for” the partial computable functions. The preceding theorem and immediate contrast require “universal for.” BN-SRC-144 corrects that property in Bengali and records it without changing any formula.

### OLP-0235 — The Halting Problem

The first proof assumes a computable halting predicate and uses it to replace every undefined universal-evaluator value by zero. This creates a total computable universal function, contradicting the preceding theorem. The primitive-recursion witness and composition equation are preserved. The second proof defines a partial function that returns zero exactly when its diagonal computation is predicted not to halt. Giving that function an index makes both its defined and undefined cases contradictory.

The tagged machine proof builds a machine that reverses a purported halting decider on self-input: a predicted halt triggers an infinite loop and a predicted nonhalt triggers a halt. Reverse paraphrase: any effective termination predictor can be transformed into a program whose behavior on its own code disagrees with the prediction. BN-SRC-145 corrects the source parenthetical’s function name from `h` to `g`, since the displayed definition makes `g`, not the total zero-one predicate `h`, take only zero when defined.

### OLP-0236 — Comparison with Russell’s Paradox

The three cases preserve their distinct conclusions. Unrestricted set comprehension yields Russell’s contradiction and therefore no such set. Treating all functions as the domain of one function yields an incoherent self-application and therefore no such function. Diagonalizing over the partial computable functions yields a legitimate total set-theoretic function that is simply not computable. The closing classification retains four regions determined by totality and partial computability. Reverse paraphrase: the same self-reference pattern refutes an object’s existence in the first two unrestricted settings but only refutes computability in the effectively enumerable setting.

BN-SRC-146 repairs the frozen Russell biconditional’s unintroduced capital `X` to `S`, restoring self-nonmembership on both sides of the contradiction.

### OLP-0237 — Computable Sets

A set is computable exactly when its characteristic function is computable, and the same definition applies to relations of any arity. “Decidable” is retained as the equivalent name. The tagged explanation distinguishes a partial-function machine, which may fail to return, from a set decider, which always returns zero or one. Reverse paraphrase: set computability is total yes/no membership computation rather than arbitrary-value partial computation.

### OLP-0238 — Computably Enumerable Sets

The definition includes the empty set separately and otherwise requires the range of a total computable function. The historical recursively enumerable terminology and c.e./r.e. abbreviations remain. Enumeration may be unordered and repetitive; the constant-zero example is preserved. The final construction maps nonmembers of a nonempty computable set to a fixed member, proving that every computable set is c.e. Reverse paraphrase: an enumerator must eventually output every member, but it need not signal completion, order its outputs or avoid duplicates.

### OLP-0239 — Equivalent Definitions of Computably Enumerable Sets

The theorem preserves four equivalent presentations: c.e. directly, range of a partial computable function, empty or range of a primitive recursive function, and domain of a partial computable function. The first construction converts a partial enumerator into a primitive-recursive total enumerator by decoding certified computation pairs and returning a fixed member on invalid codes. The two directions between range and domain use unbounded search and encoded halting computations. The final theorem preserves the existential projection of a computable relation and its converse minimization construction.

BN-SRC-147 changes ordinary equality in the partial normal-form equation to `\simeq`, as in the cited theorem. BN-SRC-148 replaces an unbound `x` in the reverse range proof with the certified input `(z)_0`. BN-SRC-149 handles the empty c.e. set as the domain of the nowhere-defined partial computable function before the proof assumes a total enumerator. Reverse paraphrase: c.e. membership is positive evidence—an output, a terminating computation, or an existential witness—with no required negative certificate.

### OLP-0240 — There Are Non-Computable Sets

The paired halting set is the domain of a partial computable search for a certified computation, so it is c.e.; halting undecidability makes it noncomputable. The self-halting set restricts the pair to equal program and input and is also c.e. The diagonal proof assumes its characteristic function computable, defines a partial function whose definedness reverses self-membership, gives that function its own index, and obtains a contradiction. Reverse paraphrase: effective positive enumeration does not imply a total decision procedure, and the self-halting set is the canonical witness.

## Technical claim audit

- All file identifiers, labels, cross-references, tag blocks, environments, case definitions, universal-function equations, characteristic functions, c.e. set codes and diagonal expressions are preserved except the four exact mathematical substitutions documented by BN-SRC-145 through BN-SRC-148.
- The checker accepts only the audited fragment-counter differences: `h` to `g`, `X\notin S` to `S\notin S`, `=` to `\simeq` in normal form, and input `x` to `(z)_0`. It separately asserts the prose repairs BN-SRC-144 and BN-SRC-149.
- All six correction notes share the target file hash recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T181 through BN-IN-T187 cover total universal-function impossibility, halting undecidability, the Russell comparison, decidable sets and relations, c.e./r.e. terminology, semidecidable characterizations, and the halting/self-halting sets. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
