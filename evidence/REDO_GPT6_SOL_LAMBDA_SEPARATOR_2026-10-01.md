# Lambda abstraction and formation-clause rendering

The current HTML inspection found that the two-argument `lambd` macro
lost the separator dot preserved by the frozen configuration. Its HTML
conversion now emits the exact dot and thin space before the body; the
one-argument and argument-free forms keep their original meaning.
The three labels inside OLP-0357's term definition now display their
distinct clause numbers, rather than the surrounding definition number.
The mathematical source and Bengali translation remain unchanged.

The PDF's tableau assumption label is localized to `অনুমান` in the
assembly configuration. This changes a visible label, not a rule or proof.
Rebuilt artifacts, macro probes and current visual receipts provide the
verification; older visual approvals are not reused for changed outputs.
