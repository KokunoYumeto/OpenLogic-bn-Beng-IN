# Semantic review: Turing Machines — mechanism, representations and configurations

This review covers OLP-0252 through OLP-0257: the Turing Machines part driver, the Turing Machine Computations chapter driver, Introduction, Representing Turing Machines, Turing Machines, and Configurations and Computations. I reread every Bengali block against its frozen English block, followed both example machines instruction by instruction, checked the diagrams and table against the transition equations, checked every configuration clause, and reverse-paraphrased the definitions and examples. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The six units contain 4 + 12 + 7 + 27 + 5 + 10 aligned source/target blocks, for 65 aligned blocks in total. Forty-four contain Bengali translation and are marked `translated_semantically_reviewed`; 21 are import-only or diagram-only structural/formal blocks and are marked `unchanged_structural_or_formal`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the seven documented source repairs are normalized for comparison.
- I consulted BN-IN-P001, BN-IN-P005 through BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for set, number, relation, function, sequence, logic and proof language. BN-IN-T170 governs the existing Church--Turing and machine-model register; BN-IN-T201 through BN-IN-T208 record this batch's tape, transition, halting, resource, representation, configuration, execution and construction terms.
- BN-SRC-162 through BN-SRC-168 disclose and repair seven frozen-source defects beside their affected passages. No frozen English byte is changed.

## Unit review

### OLP-0252 — Turing Machines part driver

The part title and both imports are present in source order: Turing Machine Computations followed by Undecidability. The part identifier, end hook and document wrapper are unchanged. Reverse paraphrase: this driver establishes the Turing Machines part and delegates its mathematical content to the two named chapters.

### OLP-0253 — Turing Machine Computations chapter driver

The translated chapter title accurately scopes computations by Turing machines. All ten imported sections remain in their frozen order, from the conceptual introduction and representations through formal machines, configurations, unary arithmetic, halting conventions, disciplined and combined machines, variants and the Church--Turing thesis. Reverse paraphrase: the chapter progresses from an intuitive mechanism to formal computation and then to normalizations, constructions and the model's intended reach.

### OLP-0254 — Introduction

The opening keeps the distinction between an ideal mathematical model and a physical machine: computability places no practical bound on time or memory. The mechanism description preserves a right-infinite tape divided into squares, a finite alphabet, the end, blank and stroke symbols, finitely many states, and a partial state-symbol transition that writes, moves left/right/stays, and changes state. The two-step example preserves both transition triples and the visible tape contents. Halting occurs exactly when the current state-symbol pair has no instruction.

The digression retains Turing's three kinds of support for the adequacy of his definition and separates unrestricted computability from bounded-resource complexity. The historical note preserves every date, machine and interval, including the Manchester SSEM's stored-program distinction. Reverse paraphrase: a Turing program controls a finite-state head over unbounded tape through a partial transition table, providing an idealized but mathematically precise account of effective procedure.

BN-SRC-162 places the initial head on the first input square immediately to the right of the end marker, matching the later formal initial configuration; the frozen introduction instead says it scans the leftmost square containing the marker.

### OLP-0255 — Representing Turing machines

The first state diagram has two nodes and one instruction: in `q_0`, reading blank writes a stroke, moves right and enters `q_1`. The even machine alternates between `q_0` and `q_1` on strokes; in `q_0` it halts on the first blank, while in `q_1` it repeatedly follows the blank loop to the right. The four-stroke trace therefore halts and accepts, and the three-stroke trace runs forever and rejects. Adding the missing `q_0` blank loop makes both parity cases nonhalting. Reverse paraphrase: state parity after the input block determines whether the first blank has no instruction or begins an infinite blank-scanning loop.

The machine table records the same three transitions by current-state row and scanned-symbol column. Each populated cell now lists new state, new symbol and direction in the order stated by the prose and shown in the transition equations. The doubler erases one input stroke, crosses the remaining input and separator, appends two output strokes, returns to the erased prefix and repeats; after every input stroke has been consumed, exactly twice as many output strokes remain. The exercises preserve equality recognition for ordered A/B blocks, arbitrary string copying, order recognition and stable-count alphabetization. Reverse paraphrase: diagrams, transition equations and tables are equivalent finite presentations, and multi-state sweeps implement memory by marks and position on the tape.

BN-SRC-163 changes the trace's erroneous “state one” to `q_0`. BN-SRC-164 reverses the swapped new-symbol/new-state fields in all three populated machine-table cells.

### OLP-0256 — Formal Turing machines

The definition preserves the exact quadruple: a finite state set `Q`, finite alphabet `Sigma` containing the end and blank symbols, initial state `q_0`, and partial transition function from state-symbol pairs to new-state, new-symbol and direction triples. The one-way tape convention and optional preservation of the end marker are retained, as is the explicit choice to permit overwriting it. The even-machine example repeats exactly the state set, alphabet and three transitions from the preceding representation. Reverse paraphrase: the mathematical object contains precisely the finite control and instruction data needed to determine each machine step, while the tape supplies unbounded storage.

### OLP-0257 — Configurations and computations

A configuration remains the triple of finite represented tape content, a valid head position below its length, and a current state. The initial configuration places the end marker before the input and the head at position one; for empty input the repaired definition explicitly represents the scanned blank at that position. The one-step relation preserves all six governing requirements: scanned symbol, applicable transition, overwritten symbol, head movement with the left boundary, rightward extension by a blank, and every unaffected old square. Reverse paraphrase: a machine computation is completely determined by successive finite snapshots even though its physical tape is idealized as infinite.

A run may now be finite or infinite and every successive pair follows the one-step relation. A finite run halts after `k` steps only when its final state-symbol pair has no transition. Output removes only the trailing blanks after the end marker; if a machine used the earlier permission to erase that marker and no required final-tape form exists, the convention assigns no output. BN-SRC-165 corrects “left of the marker” to “right”; BN-SRC-166 supplies a valid empty-input configuration; BN-SRC-167 restores finite terminating runs; BN-SRC-168 resolves the output-existence conflict created by optional marker overwriting.

## Technical claim audit

- All file identifiers, imports, labels, cross-references, captions, TikZ environments, transition equations, configuration triples, one-step clauses and output expressions are preserved except the exact three table-field reorderings and the empty-input configuration documented by BN-SRC-164 and BN-SRC-166.
- The checker transforms only the three audited table cells before comparing mathematical fragments, separately accounts for the corrected symbolic initial state, and permits exactly one added empty-input configuration. It independently asserts the five repaired prose claims.
- The even-machine diagram, equations, table and both traces agree. The doubler diagram implements the stated erase, traverse, append-two and return strategy. The configuration definition respects its own index bound for both empty and nonempty inputs.
- All seven correction notes share the target file hash recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T201 through BN-IN-T208 cover tape and head components, transition data, halting and acceptance, resource bounds, state diagrams and machine tables, configurations and runs, parity-machine execution, and constructive machine strategies. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. OLP-0258, Unary Representation of Numbers, is the next untranslated source unit.
