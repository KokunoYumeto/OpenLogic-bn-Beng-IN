Inspection of the current lambda formation page exposed a PDF reference
regression: references printed only “দেখুন” instead of the definition or
clause number. The shared HTML normalizer produced hyperlinks and anchors;
the PDF preparation reused those anchors without restoring their source
counter labels. Clickable destinations did not restore a printable reference.

Preparation now retains each anchor and adds its corresponding real label,
then uses automatic references to the same physical target. Reference names
are localized in Bengali. The six existing stable proof-title references and
three captions retain their specific handling; no missing frozen reference
is redirected to an unrelated proposition. All four documented source gaps
remain explicit.

The native HTML conversion coalesces each adjacent anchor/counter label into
one target before Pandoc, and restores its semantic hyperlinks. Duplicate
physical targets are still rejected. Source translations and frozen English
are unchanged. Actual preparation counts, converged PDF reference warnings,
rendered definition/clause examples and final HTML link checks must be bound
to the rebuilt artifacts before publication.
