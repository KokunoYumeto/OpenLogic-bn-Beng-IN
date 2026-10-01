The current browser capture of OLP-0683 exposed a reader conversion error:
`\Obj c_0` was rendered as the literal word “Obj” followed by the constant.
The frozen configuration declares `\Obj` with one mandatory argument and
renders that argument with `\mathsfit`. Mandatory TeX arguments include
unbraced characters and control sequences.

The reader now consumes that argument through the existing required-argument
parser and uses the actual upstream sans-serif italic style. A local Pandoc
probe confirmed native MathML `mathvariant="sans-serif-italic"` without
warnings. Braced and unbraced arguments use the same conversion; a missing
argument raises an error instead of inventing a symbol.

This is a rendering-script correction. Frozen English and Bengali source
files are unchanged, and it creates no new English source erratum. Current
corpus conversion, reader hashes and visual approval are recorded separately
after the rebuild.
