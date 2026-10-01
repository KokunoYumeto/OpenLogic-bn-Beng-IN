The first current complete PDF converged in four guarded XeLaTeX passes, but
the missing-character log and visual inspection exposed an actual symbol loss.
The legacy accent slot `^^V` is absent from the fontspec bold text math alphabet.
Consequently `\Th{\bar Q}` and `\Th{\bar T}` appeared as unbarred bold letters.
In the computable-inseparability proof this makes distinct sets look identical.

The preparation step now places the bar outside that alphabet:
`\Th{\bar Q}` becomes `\overline{\Th{Q}}`, and likewise for T. The letter,
bold style and overbar remain present. This is a documented, mathematically
equivalent rendering adjustment in the assembled edition; the frozen English
and the Bengali translation files remain unchanged. Per-unit counts are in
`PREPARATION.json`. A fresh build and inspection must attest the final PDF;
the earlier converged PDF is not approved by this repair record.
