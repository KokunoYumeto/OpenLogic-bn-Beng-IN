# Semantic review: Turing Machines — undecidability foundations

This review covers OLP-0264 through OLP-0269: the Undecidability chapter driver, Introduction, Enumerating Turing Machines, Universal Turing Machines, the Halting Problem, and the Decision Problem. I reread every Bengali block against its frozen English block, reconstructed the finite machine code field by field, traced the universal simulator's tape representation and output decoder, checked both branches of the halting diagonal, and reverse-paraphrased the planned reduction from first-order validity to halting. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The six units contain 11 + 8 + 15 + 13 + 16 + 5 aligned source/target blocks, for 68 aligned blocks in total. Fifty-four contain Bengali translation and are marked `translated_semantically_reviewed`; 14 are import-only, diagram-only or other structural/formal blocks and are marked `unchanged_structural_or_formal`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the three documented source repairs are normalized for comparison.
- I consulted BN-IN-P001, BN-IN-P005 through BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 and BN-IN-P028 for number, set, sequence, mapping, countability, logic and proof language. Existing T040, T044, T063, T091, T153, T170, T174, T182 and T201 through T216 anchor the inherited register; T217 through T223 record the new undecidability, enumeration, indexing, universal-simulation, halting and decision-problem vocabulary.
- BN-SRC-175 through BN-SRC-177 disclose and repair three frozen-source defects beside their affected passages. No frozen English byte is changed.

## Unit review

### OLP-0264 — Undecidability chapter driver

The chapter title and all nine imports are present in frozen order: motivation, enumeration of machines, a universal machine, the halting problem, the decision problem, representation of machines in first-order logic, verification, the formal unsolvability proof and Trakhtenbrot's theorem. The chapter identifier, end hook and document wrapper are unchanged. Reverse paraphrase: the driver moves from machine coding and a canonical undecidable problem to reductions establishing limits of first-order validity over arbitrary and finite structures.

### OLP-0265 — Introduction

The radioactive-decay example preserves the difference between inability to imagine an algorithm and proof of uncomputability. If the universe has only finitely many future seconds, the resulting partial function has finite domain and can be implemented by a finite, though enormous, lookup table or machine. The prime-number display then defines effective decision of a yes/no question through its total zero-one function. Reverse paraphrase: intuitive complexity is not a mathematical lower bound; an impossibility proof must use a precise computation model.

The Church--Turing step remains explicit: first prove that a fixed formal model cannot compute a function or decide a problem, then use the thesis to transfer the negative result to all effective procedures. Cardinality supplies existence because machines have enumerable descriptions while even binary-valued functions on the naturals are nonenumerable. The remainder identifies the concrete halting problem, explains why machine descriptions can themselves be inputs, states that no total quality-control machine decides all index-input pairs, and introduces first-order validity as the historical decision problem. The independent Church and Turing attribution is retained.

### OLP-0266 — Enumerating Turing machines

A machine is finitely described by finite state and alphabet sets plus the finitely many defined values of its partial transition function. Arbitrary objects could technically serve as state names, so raw set membership is separated from behavior: bijective renaming of states and symbols leaves a machine's operation unchanged. The two parity diagrams agree transition by transition, and their positive-integer version uses 1 for the end marker, 2 for blank, 3 for stroke, states 1 and 2, and direction codes 1/2/3 for left/right/stay. Reverse paraphrase: quotienting harmless names lets every behavior be represented by a standard machine over positive-integer labels.

The finite code records the number and list of states, number and list of symbols, initial state, and one quintuple for each defined transition. The displayed parity-machine sequence has exactly those fields and each direction code agrees with its annotated transition. Since finite positive-integer sequences are enumerable, standard machines and therefore Turing-computable functions are enumerable; all functions from the naturals to themselves are not, so some functions are not Turing-computable. BN-SRC-175 repairs the final exercise's category error: a standard machine simulates an arbitrary machine's behavior rather than computing the machine object.

### OLP-0267 — Universal Turing machines

A fixed effective enumeration assigns an index to each description, with multiple indices allowed for reordered but equivalent descriptions. Both translations are effective: an index yields its description and a description yields an index. This makes simple syntactic properties such as number of states computable by decoding the description and retaining its first block. Reverse paraphrase: indices turn programs into numeric inputs while preserving effective access to their finite instructions.

The universal-machine theorem preserves both clauses. On input `e,n`, `U` halts exactly when `M_e` halts on `n`; whenever the simulated machine has numeric output `m`, `U` has the same output. The partial function is undefined when the simulated run diverges or halts without numeric output. The construction stores the index, input, current state, unary head-position counter and an encoded sequence of tape-symbol codes. Each simulation cycle reads the counter-selected symbol, finds the matching instruction, rewrites the symbol code, changes the stored state and adjusts the head counter; the footnote preserves the need to shift the encoded tape when a counter grows.

BN-SRC-176 repairs the frozen final decoder. The source says to translate three-stroke blocks and reject every other block even though the encoded tape necessarily begins with its explicitly specified one-stroke end marker and any represented blank has its explicitly specified two-stroke code. The Bengali algorithm checks and skips the marker, translates consecutive code-3 output symbols, accepts zero or more trailing code-2 blanks only if the entire remainder is blank, and otherwise halts with nonnumeric output. Thus valid tapes of the previously defined output form produce exactly `m` strokes, while malformed simulated outputs still leave the partial value undefined.

### OLP-0268 — The Halting Problem

The total halting function `h(e,n)` returns one exactly when indexed machine `M_e` halts on unary input `n`; the halting problem asks for that value for every pair. Its diagonal specialization `s(e)` asks whether `M_e` halts on its own index. Assuming a disciplined machine `S` computes `s`, the proof connects it to `J`, which halts on the empty unary input and runs forever on nonempty input. Because the combined machine has some index `e`, running it on `e` yields both contradiction cases: a predicted one makes `J` diverge, while a predicted zero makes `J` halt. Reverse paraphrase: making a purported decider control the opposite terminal behavior on its own description defeats either possible answer.

If `h` were computable, a copier would turn input `e` into the pair `e,e` and feed it to an `h`-machine, computing the impossible `s`; hence the halting problem is unsolvable. All four exercises retain their scope: fixed three-stroke input, off-diagonal pairs, direct descriptions instead of indices, and the positive semidecision partial function. BN-SRC-177 replaces both frozen `S \concat J` expressions with the previously defined `S \frown J`; `\concat` remains reserved for string concatenation.

### OLP-0269 — The Decision Problem

First-order logic is decidable exactly if a total effective method decides validity of any given sentence. By the Church--Turing thesis, failure of every Turing-machine validity decider rules out every effective validity method. The proposed reduction assumes such a decider and would use it to compute the already impossible halting function. Reverse paraphrase: encode a machine `M` and input `w` into a sentence `T(M,w)` describing its computation constraints and a sentence `E(M,w)` asserting eventual halting, so that the implication from `T` to `E` is valid exactly when `M` halts on `w`.

The direction of reduction is preserved: a solution to validity would yield a solution to halting, so halting's impossibility entails validity's impossibility. The next sections must construct the two sentences and prove the biconditional; this unit makes no premature claim that the construction has already been verified.

## Technical claim audit

- All file identifiers, imports, labels, references, captions, environments, transition labels, displayed functions and code sequences are preserved except the two audited machine-combination symbols documented by BN-SRC-177.
- The checker asserts the exact source and Bengali relation in BN-SRC-175, validates all three existing symbol codes and the complete optional-blank output shape in BN-SRC-176, and permits exactly two `concat`-to-`frown` math substitutions for BN-SRC-177.
- The parity-machine diagrams agree under state/symbol renaming. The displayed integer code reconstructs three transitions: `(1,3)` to `(2,3,R)`, `(2,2)` to `(2,2,R)`, and `(2,3)` to `(1,3,R)`.
- The universal simulator preserves the initial head position 1 and the symbol codes 1/2/3. Its corrected decoder accepts exactly the output convention established in OLP-0257, including the case of no represented trailing blanks.
- Both diagonal branches were checked with the same machine index `e`; each conclusion negates its branch assumption. The reduction from `h` to `s` duplicates the input before invoking the hypothetical decider.
- All three correction notes share the target file hashes recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted because the shared TeX mutex is reserved elsewhere. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending.

## Terminology and edition scope

BN-IN-T217 through BN-IN-T223 cover undecidability and effective decision, standard-machine enumeration, numeric program indices and decoding, universal simulation state, the halting diagonal, fixed-input and partial recognition variants, and the validity decision reduction. Specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. OLP-0270, Representing Turing Machines in First-Order Logic, is the next untranslated source unit.
