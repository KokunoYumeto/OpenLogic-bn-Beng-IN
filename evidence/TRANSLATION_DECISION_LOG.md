# Bengali translation decision log

This retrospective and forward review index covers every current substantive entry in `TERM_DECISIONS.jsonl` and grows with the unfinished 722-file translation. Machine records give exact frozen-source wording and block hashes, every exact matching target line, Bengali script and locale, consulted-page identities, alternatives, confidence, an explicit expert-review flag and a plain double-check question. Final printed/PDF pages remain explicitly pending until reader integration and final pagination.

## Edition-scope assessment

The checked India university and school witnesses show lexical variation, but the current translated scope does not justify separate script, orthographic, notation or regional editions. One bn-Beng-IN edition remains the evidence-based set.
No variant has been introduced. Reassess as the corpus grows and coordinate any proposed additional edition and its locale/name with the OpenLogic Internationalization Manager before creating it.

Script: Use Bengali script for Bengali prose. Preserve Latin metavariables, source-defined object-language glyphs and conventional mathematical symbols.
Orthography: Use normalized modern India-standard university Bengali orthography consistently; record directly witnessed regional variants as alternatives rather than silently mixing them.
Notation and direction: Preserve the frozen source formula order, left-to-right mathematical direction, macro vocabulary, labels and reference controls except for separately documented source corrections.
Numerals: Use Bengali digits for ordinary Bengali prose numerals when idiomatic; preserve source Arabic numerals and Latin subscripts inside mathematical notation and identifiers.

## Decision overview

| ID | Source concept | Chosen Bengali | Status | Confidence | Priority | Occurrences | Authorities | Expert review |
|---|---|---|---|---|---|---:|---|---|
| `BN-IN-T001` | set | সেট | attested | high_for_attested_scope | low | 887 | BN-IN-P001, BN-IN-P006 | welcome/open to correction |
| `BN-IN-T002` | element | উপাদান | attested | high_for_attested_scope | low | 73 | BN-IN-P001 | welcome/open to correction |
| `BN-IN-T003` | member | সদস্য | attested | high_for_attested_scope | low | 55 | BN-IN-P001 | welcome/open to correction |
| `BN-IN-T004` | empty set | শূন্য সেট | attested | high_for_attested_scope | low | 18 | BN-IN-P006 | welcome/open to correction |
| `BN-IN-T005` | subset | উপসেট | attested | high_for_attested_scope | low | 85 | BN-IN-P003, BN-IN-P007 | welcome/open to correction |
| `BN-IN-T006` | proper subset | প্রকৃত উপসেট | attested | high_for_attested_scope | low | 3 | BN-IN-P004, BN-IN-P007 | welcome/open to correction |
| `BN-IN-T007` | power set | ঘাত সেট | attested-regional | high_for_attested_scope | low | 6 | BN-IN-P007 | welcome/open to correction |
| `BN-IN-T008` | extensionality | সদস্যভিত্তিক সমতার নীতি | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 20 | BN-IN-P004, BN-IN-P006 | welcome/open to correction |
| `BN-IN-T009` | natural number | স্বাভাবিক সংখ্যা | attested | high_for_attested_scope | low | 65 | BN-IN-P005 | welcome/open to correction |
| `BN-IN-T010` | proposition (logic) | বচন | attested | high_for_attested_scope | low | 52 | BN-IN-P009, BN-IN-P008 | welcome/open to correction |
| `BN-IN-T011` | quantifier | পরিমাণসূচক | attested | high_for_attested_scope | low | 96 | BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T012` | universal quantifier | সার্বিক পরিমাণসূচক | attested | high_for_attested_scope | low | 4 | BN-IN-P009 | welcome/open to correction |
| `BN-IN-T013` | existential quantifier | অস্তিত্বমূলক পরিমাণসূচক | attested | high_for_attested_scope | low | 0 | BN-IN-P010 | welcome/open to correction |
| `BN-IN-T014` | if and only if | যদি এবং কেবল যদি | provisional-phrase | medium_definition_and_adjacent-canon_support | medium | 198 | BN-IN-P004 | welcome/open to correction |
| `BN-IN-T015` | perfect number | নিখুঁত সংখ্যা | provisional-descriptive | low_pending_occurrence | high | 0 | BN-IN-P005 | welcome/open to correction |
| `BN-IN-T016` | union; intersection; disjoint; difference | সংযোগ; ছেদ; বিচ্ছিন্ন; অন্তর | attested | high_for_attested_scope | low | 88 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T017` | ordered pair | ক্রমযুগল | attested | high_for_attested_scope | low | 40 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T018` | Cartesian product | কার্তেসীয় গুণফল | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T019` | string; sequence; tuple; word | প্রতীকক্রম; অনুক্রম; টিউপল; শব্দ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 229 | BN-IN-P002, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T020` | paradox; contradiction; comprehension; naive set theory | কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 49 | BN-IN-P001, BN-IN-P004, BN-IN-P009 | welcome/open to correction |
| `BN-IN-T021` | conjunction; conjunction elimination; absorption | সংযোজন; সংযোজন অপসারণ; শোষণ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P008, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T022` | relation; binary relation; order relation; identity relation | সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 278 | BN-IN-P013, BN-IN-P014, BN-IN-P004 | welcome/open to correction |
| `BN-IN-T023` | irreflexive; strict order; empty relation; universal relation | আত্মসম্পর্কহীন; কঠোর ক্রম; শূন্য সম্পর্ক; সার্বিক সম্পর্ক | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 19 | BN-IN-P013, BN-IN-P006, BN-IN-P009 | welcome/open to correction |
| `BN-IN-T024` | continuum; mathematical proposition heading; general conditional proof | সতত সমষ্টি; প্রতিজ্ঞা; সাধারণ শর্তাধীন প্রমাণ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 15 | BN-IN-P005, BN-IN-P009, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T025` | predicate; singular term; metaphysical identity; set-theoretic reductionism | বিধেয়; একবস্তুনির্দেশক পদ; অধিবিদ্যাগত অভিন্নতা; সেটতত্ত্বে পর্যবসনবাদ | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P009, BN-IN-P013 | welcome/open to correction |
| `BN-IN-T026` | reflexivity; symmetry; transitivity; equivalence relation | প্রতিবিম্ব ধর্ম; প্রতিসাম্য; পরিযায়িতা; তুল্যতা সম্পর্ক | attested-roots-normalized-properties | high_for_attested_scope | low | 57 | BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T027` | antisymmetric; asymmetric; connected (relation) | বিপ্রতিসম; একমুখী; সংযুক্ত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 28 | BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T028` | equivalence class; partition; quotient set; congruence modulo n | তুল্যতা শ্রেণি; বিভাজন; ভাগসেট; মডুলো n সমতুল্যতা | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 18 | BN-IN-P015, BN-IN-P016, BN-IN-P017 | welcome/open to correction |
| `BN-IN-T029` | preorder; partial order; linear order; total order; closure; initial segment | প্রাক্‌ক্রম; আংশিক ক্রম; রৈখিক ক্রম; পূর্ণ ক্রম; আবরণ; প্রারম্ভিক খণ্ড | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 70 | BN-IN-P013, BN-IN-P014, BN-IN-P016 | welcome/open to correction |
| `BN-IN-T030` | graph; directed graph; vertex; edge; isolated vertex | গ্রাফ; নির্দেশিত গ্রাফ; শীর্ষ; প্রান্ত; বিচ্ছিন্ন শীর্ষ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 27 | BN-IN-P012, BN-IN-P013 | welcome/open to correction |
| `BN-IN-T031` | tree; root; successor; predecessor; branch; chain; least element; well-order | বৃক্ষ; মূল; উত্তরসূরি; পূর্বসূরি; শাখা; শৃঙ্খল; ক্ষুদ্রতম উপাদান; সুক্রম | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 373 | BN-IN-P001, BN-IN-P013, BN-IN-P014, BN-IN-P016 | welcome/open to correction |
| `BN-IN-T032` | inverse relation; relative product; restriction; application; transitive closure | বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 188 | BN-IN-P012, BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T033` | formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma | সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য | provisional-contextual | medium_definition_and_adjacent-canon_support | medium | 283 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T034` | variable; constant; sum; arithmetic product; equation | চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ | attested-in-school-algebra | high_for_attested_scope | low | 235 | BN-IN-P019, BN-IN-P020, BN-IN-P022 | welcome/open to correction |
| `BN-IN-T035` | function; mapping; domain; codomain; range; image/value | অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান | attested-university | high_for_attested_scope | low | 713 | BN-IN-P018 | welcome/open to correction |
| `BN-IN-T036` | function argument; input; output; black box; extensionality for functions | আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 27 | BN-IN-P018, BN-IN-P019, BN-IN-P020, BN-IN-P022 | welcome/open to correction |
| `BN-IN-T037` | injective/injection; surjective/surjection; bijective/bijection; identity function | একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক | attested-university-with-normalization | high_for_attested_scope | low | 21 | BN-IN-P023, BN-IN-P024 | welcome/open to correction |
| `BN-IN-T038` | inverse function; left inverse; right inverse; composition | বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ | attested-root-with-provisional-normalization | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P024, BN-IN-P025, BN-IN-P026 | welcome/open to correction |
| `BN-IN-T039` | partial function; total function; functional relation; serial relation; Axiom of Choice | আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 14 | BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T040` | size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable | সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয় | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 322 | BN-IN-P027, BN-IN-P028, BN-IN-P023, BN-IN-P024 | welcome/open to correction |
| `BN-IN-T041` | actual infinity | বাস্তবায়িত অসীম | provisional-philosophical | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P009, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T042` | ceiling function; induction; recursive definition; corollary | ঊর্ধ্ব পূর্ণাংশ অপেক্ষক; গাণিতিক আরোহ; পূর্ববর্তী মানের সাহায্যে ধাপে ধাপে সংজ্ঞা; অনুসিদ্ধান্ত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 31 | BN-IN-P018, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T043` | zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function | আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 158 | BN-IN-P009, BN-IN-P012, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P024, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T044` | non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence | অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P001, BN-IN-P002, BN-IN-P009, BN-IN-P010, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T045` | reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction | হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 13 | BN-IN-P009, BN-IN-P010, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T046` | equinumerous/equinumerosity; same cardinality; cardinal equality | সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P014, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P025, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T047` | no larger than; strictly smaller cardinality; cardinal comparison; Cantor's theorem; Schröder–Bernstein theorem | আকারে বড় নয়; আকারে ছোট; অঙ্কবাচকতার তুলনা; কান্টরের উপপাদ্য; শ্র্যোডার–বার্নস্টাইন উপপাদ্য | mixed-normalized-and-proper-name | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P014, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P025, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T048` | integer; positive/negative integer; natural number represented as an integer; equivalence-class representative | পূর্ণসংখ্যা; ধনাত্মক/ঋণাত্মক পূর্ণসংখ্যা; স্বাভাবিক সংখ্যার পূর্ণসংখ্যা-রূপ; তুল্যতা শ্রেণির প্রতিনিধি | mixed-direct-and-normalized | medium_definition_and_adjacent-canon_support | medium | 66 | BN-IN-P005, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T049` | arithmetization as set-theoretic construction of number systems; induced arithmetic operations; well-defined on equivalence classes | সেটতাত্ত্বিক সংখ্যা-নির্মাণ; তুল্যতা শ্রেণির উপর গাণিতিক ক্রিয়া; প্রতিনিধিনিরপেক্ষভাবে সুসংজ্ঞায়িত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P012, BN-IN-P015, BN-IN-P016, BN-IN-P017, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T050` | rational number; nonzero denominator; rational representative/embedding; cross multiplication | মূলদ সংখ্যা; অশূন্য হর; মূলদ-প্রতিনিধি/পূর্ণসংখ্যার মূলদ-রূপ; আড়গুণ | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 41 | BN-IN-P005, BN-IN-P012, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T051` | real line; irrational number; ordered field; Completeness Property; upper bound; least upper bound | বাস্তব সংখ্যারেখা; অমূলদ সংখ্যা; ক্রমিত ক্ষেত্র; পূর্ণতা ধর্ম; ঊর্ধ্বসীমা; লঘিষ্ঠ ঊর্ধ্বসীমা | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 32 | BN-IN-P005, BN-IN-P009, BN-IN-P015, BN-IN-P016, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T052` | Dedekind cut; lower half; proper initial segment; greatest lower bound; maximum element; rational-to-real embedding | ডেডেকিন্ড কর্তন; নিম্নাংশ; প্রকৃত প্রারম্ভিক খণ্ড; গরিষ্ঠ নিম্নসীমা; গরিষ্ঠ উপাদান; মূলদ সংখ্যার বাস্তব-রূপ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P005, BN-IN-P015, BN-IN-P016, BN-IN-P017, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T053` | commutative ring; ordered ring; ordered field; associative/commutative/identity/additive inverse/distributive laws; trichotomy | বিনিমেয় বলয়; ক্রমিত বলয়; ক্রমিত ক্ষেত্র; সংযোগী/বিনিময়/অভেদী/যোগাত্মক বিপরীত/বণ্টন ধর্ম; ত্রিবিভাজন | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 25 | BN-IN-P009, BN-IN-P013, BN-IN-P014, BN-IN-P017, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T054` | Cauchy sequence; rational approximation; tends to zero; equivalence modulo null sequences; constant-sequence embedding; monotone increasing/decreasing | কোশি অনুক্রম; মূলদ আসন্নমান; সীমায় শূন্যের দিকে যায়; শূন্যমুখী অনুক্রমের মডুলো তুল্যতা; ধ্রুব অনুক্রমে অন্তর্ভুক্তি; একঘেয়ে বর্ধমান/হ্রাসমান | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 16 | BN-IN-P005, BN-IN-P009, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T055` | rigour of a construction; metaphysical identification; set-theoretic embedding; rival constructions; Benacerraf-style underdetermination | নির্মাণের কঠোরতা; অধিবিদ্যাগত অভিন্নকরণ; সেটতাত্ত্বিক অন্তর্ভুক্তি; প্রতিদ্বন্দ্বী নির্মাণ; বেনাসেরাফ-ধর্মী অনির্ধার্যতা | provisional-philosophical | low_pending_occurrence | high | 0 | BN-IN-P009, BN-IN-P013, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T056` | infinite set; Dedekind-infinite set; Hilbert's Hotel | অসীম সেট; ডেডেকিন্ড-অসীম সেট; হিলবার্টের হোটেল | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P023, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T057` | Dedekind algebra; successor function; self-map; f-closed set; closure under f | ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 23 | BN-IN-P013, BN-IN-P014, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T058` | parameter of a formula; free variable; recursive definition | সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 18 | BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T059` | isomorphic structures; structuralist; surrogate for the natural numbers; pure laws of thought | সমরূপ গঠন; গঠনবাদী; স্বাভাবিক সংখ্যার প্রতিস্থাপক; চিন্তার বিশুদ্ধ বিধি | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P009, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T060` | syntax; semantics; metatheory; inductive definition; unique readability | সংকেতবিন্যাস; অর্থতত্ত্ব; অধিতত্ত্ব; আরোহী সংজ্ঞা; একক পাঠযোগ্যতা | provisional-formally-governed | medium_definition_and_adjacent-canon_support | medium | 102 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T061` | propositional variable; propositional/logical connective; truth value; truth-functional; material conditional | বচনচল; বচনসংযোজক/যৌক্তিক সংযোজক; সত্যমান; সত্যমান-অপেক্ষকধর্মী; বস্তুগত শর্তবচন | mixed-attested-roots-and-provisional | medium_definition_and_adjacent-canon_support | medium | 43 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020 | welcome/open to correction |
| `BN-IN-T062` | negation; conjunction; disjunction; conditional/implication; biconditional/material equivalence | নঞর্থকরণ; সংযোজন; বিয়োজন; শর্তবচন/নিহিতকরণ; দ্বিশর্তবচন/বস্তুগত সমতুল্যতা | attested-variants-normalized | high_for_attested_scope | low | 38 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T063` | denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation | অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 129 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019 | welcome/open to correction |
| `BN-IN-T064` | formula induction; balanced formula; proper initial segment; parsing; uniform substitution | সূত্রের উপর আরোহ; সুষম সূত্র; প্রকৃত প্রারম্ভিক খণ্ড; গঠনবিশ্লেষণ; সমরূপ প্রতিস্থাপন | provisional-mathematically-governed | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T065` | formation sequence; junk/redundant formula; strong induction | গঠন-অনুক্রম; অপ্রয়োজনীয় সূত্র; প্রবল আরোহ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 73 | BN-IN-P008, BN-IN-P009, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T066` | valuation; evaluation function; satisfaction; local determination; truth table | সত্যমান-আরোপ; মূল্যায়ন অপেক্ষক; পরিতৃপ্তি; স্থানীয় নির্ধারণ; সত্যসারণি | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 186 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T067` | satisfiable/unsatisfiable; tautology; contingent; semantic entailment; monotonicity; semantic deduction theorem | পরিতৃপ্তিযোগ্য/অপরিতৃপ্তিযোগ্য; সর্বতঃসত্য; আপতিক; অর্থগত অনুসিদ্ধান্ত; একঘেয়েতা; অর্থগত নিঃসরণ উপপাদ্য | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 154 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T068` | derivation system; purely syntactic object/method; mechanical verification; metatheoretical treatment | নিষ্পাদন পদ্ধতি; সম্পূর্ণ সংকেতবিন্যাসগত বস্তু/পদ্ধতি; যান্ত্রিক যাচাই; অধিতাত্ত্বিক বিচার | provisional-contextual | medium_definition_and_adjacent-canon_support | medium | 144 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T069` | soundness; completeness; consistency/inconsistency; syntactic counterpart | বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 140 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T070` | axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens | স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স | provisional-formally-governed | medium_definition_and_adjacent-canon_support | medium | 214 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T071` | natural deduction; proof by cases; indirect proof; conditional proof | স্বাভাবিক নিষ্পাদন; ক্ষেত্রবিচারে প্রমাণ; পরোক্ষ প্রমাণ; শর্তাধীন প্রমাণ | provisional-proof-patterns | medium_definition_and_adjacent-canon_support | medium | 32 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T072` | introduction/elimination rule; assumption/hypothesis; discharge/undischarged assumption; proof-theoretic semantics | প্রবর্তন/অপসারণ-বিধি; অনুমিতি/পূর্বধারণা; অনুমিতি অবমুক্ত করা/অনবমুক্ত অনুমিতি; প্রমাণতাত্ত্বিক অর্থতত্ত্ব | provisional-natural-deduction-register | medium_definition_and_adjacent-canon_support | medium | 249 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T073` | sequent calculus; sequent; initial sequent; left/right side; weakening rule | সিকোয়েন্ট কলন; সিকোয়েন্ট; প্রারম্ভিক সিকোয়েন্ট; বাঁ/ডানপাশ; দুর্বলীকরণ-বিধি | provisional-transliterated-system | medium_definition_and_adjacent-canon_support | medium | 166 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T074` | tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus | ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 264 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T075` | resolution method; resolution refutation; mechanization/implementation; read a satisfying structure off an open branch | রেজোলিউশন পদ্ধতি; রেজোলিউশন খণ্ডন; যান্ত্রিক প্রয়োগ/রূপায়ণ; খোলা শাখা থেকে পরিতৃপ্তিকারী গঠন পড়ে নেওয়া | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T076` | antecedent; succedent; associated sentence of a sequent; sequence concatenation | পূর্বাংশ; উত্তরাংশ; সিকোয়েন্টের সংশ্লিষ্ট বাক্য; অনুক্রমের সংযুক্তি | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T077` | logical rule; structural rule; upper/lower sequent; left/right rule | যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি | provisional-rule-register | medium_definition_and_adjacent-canon_support | medium | 95 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T078` | quantifier rule; eigenvariable/eigenvariable condition; closed term | পরিমাণসূচকের বিধি; আইগেনচল/আইগেনচল-শর্ত; বদ্ধ পদ | provisional-quantifier-rule-register | medium_definition_and_adjacent-canon_support | medium | 113 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T079` | contraction; exchange; cut; inference line; LK derivation/end-sequent | সংকোচন; অদলবদল; কর্তন; অনুমান-রেখা; LK-নিষ্পাদন/অন্তিম সিকোয়েন্ট | provisional-structural-rule-register | medium_definition_and_adjacent-canon_support | medium | 54 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T080` | proof search; apply a rule backwards; split into branches; finish at an initial sequent | প্রমাণ-অন্বেষণ; বিধি উল্টো দিকে প্রয়োগ; শাখায় ভাগ; প্রারম্ভিক সিকোয়েন্টে শেষ করা | provisional-pedagogical-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T081` | provability/derivability relation; theorem; reflexivity; monotonicity; transitivity; compactness | প্রমাণযোগ্যতা/নিষ্পাদনযোগ্যতা-সম্পর্ক; উপপাদ্য; প্রতিবিম্ব ধর্ম; একঘেয়েতা; পরিযায়িতা; সংহতি | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 195 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T082` | propositional facts about provability; modus ponens; shared sequent context | বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ | provisional-rule-governed | medium_definition_and_adjacent-canon_support | medium | 20 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T083` | strong generalization; fresh constant; quantifier provability facts | প্রবল সাধারণীকরণ; নতুন ধ্রুবক; পরিমাণসূচক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য | provisional-quantifier-metatheory | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T084` | valid sequent; satisfy a sequent; soundness induction; induction hypothesis; variable assignment | বৈধ সিকোয়েন্ট; সিকোয়েন্ট পরিতৃপ্ত করা; বিশুদ্ধতার আরোহ-প্রমাণ; আরোহের অনুমান; চলরাশি-আরোপ | provisional-semantics-proof-register | medium_definition_and_adjacent-canon_support | medium | 73 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T085` | identity/equality rules; substitutability of identicals; Leibniz's Law; symmetry and transitivity | অভিন্নতা/সমতার বিধি; অভিন্ন বস্তুর প্রতিস্থাপনযোগ্যতা; লাইবনিজের সূত্র; প্রতিসাম্য ও পরিযায়িতা | mixed-attested-roots-and-provisional | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P013, BN-IN-P020, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T086` | natural-deduction derivation tree; branch; inference premise and conclusion; subderivation/subproof | স্বাভাবিক নিষ্পাদন-বৃক্ষ; শাখা; অনুমানের পূর্বধারণা ও সিদ্ধান্ত; উপ-নিষ্পাদন/উপপ্রমাণ | provisional-tree-structure-register | medium_definition_and_adjacent-canon_support | medium | 132 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T087` | natural-deduction eigenvariable condition; discharged A(a) assumption; major existential premise; freshness | স্বাভাবিক নিষ্পাদনের আইগেনচল-শর্ত; অবমুক্তযোগ্য A(a) অনুমিতি; প্রধান অস্তিত্বসূচক পূর্বধারণা; নতুনত্ব | provisional-rule-specific-freshness | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T088` | rule-applicable signed formula; check off with a check mark; branch-splitting rule; repeat a quantified rule with a closed term | বিধি প্রয়োগের উপযোগী চিহ্নিত সূত্র; টিকচিহ্ন দেওয়া; শাখা-বিভাজক বিধি; বদ্ধ পদ দিয়ে বিধিটি কয়েকবার প্রয়োগ | provisional-tableau-construction-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T089` | satisfy a signed formula; satisfiable set/branch/tableau; rule extension preserves satisfiability; unsatisfiable; contrapositive | চিহ্নিত সূত্রকে পরিতৃপ্ত করা; পরিতৃপ্তিযোগ্য সমষ্টি/শাখা/ট্যাবলো; বিধি-প্রসারণে পরিতৃপ্তিযোগ্যতা বজায় রাখা; অপরিতৃপ্তিযোগ্য; বিপরীত-প্রতিজ্ঞা | provisional-tableau-soundness-register | medium_definition_and_adjacent-canon_support | medium | 173 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T090` | syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations | নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো | provisional-axiomatic-metatheory-register | medium_definition_and_adjacent-canon_support | medium | 20 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T091` | complete consistent theory; axiomatizable; decidable | পূর্ণ সঙ্গত তত্ত্ব; স্বতঃসিদ্ধযোগ্য; নির্ণেয় | provisional-completeness-metatheory-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T092` | Henkin expansion; saturated set; witness; counterexample | হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত | provisional-henkin-construction-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T093` | term model; Truth Lemma; covered model; factor a model by an equivalence relation | পদ-মডেল; সত্যতা-সহায়ক উপপাদ্য; আচ্ছাদিত মডেল; তুল্যতা সম্পর্ক দিয়ে মডেলের ভাগকরণ | mixed-attested-roots-and-provisional-model-theory | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P013, BN-IN-P015, BN-IN-P016, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T094` | finitely satisfiable; infinitesimal; standard model of arithmetic | সসীমভাবে পরিতৃপ্তিযোগ্য; অতিক্ষুদ্র সংখ্যা; পাটীগণিতের প্রমিত মডেল | provisional-compactness-application-register | medium_definition_and_adjacent-canon_support | medium | 27 | BN-IN-P008, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T095` | downward Löwenheim–Skolem theorem; countable model; Skolem's paradox | লোয়েনহাইম--স্কোলেম উপপাদ্য; গণনীয় মডেল; স্কোলেমের কূটাভাস | provisional-model-size-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T096` | formal language; first-order language; quantificational logic; predicate logic; vocabulary; expression/string | বিধিবদ্ধ ভাষা; প্রথম-ক্রমের ভাষা; পরিমাণসূচকীয় যুক্তিবিদ্যা; বিধেয় যুক্তিবিদ্যা; শব্দভাণ্ডার; অভিব্যক্তি/প্রতীকক্রম | mixed-contextual-and-provisional-first-order-register | medium_definition_and_adjacent-canon_support | medium | 96 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019 | welcome/open to correction |
| `BN-IN-T097` | term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope | পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর | mixed-attested-roots-and-definition-governed | medium_definition_and_adjacent-canon_support | medium | 587 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T098` | structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment | গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ | mixed-attested-roots-and-provisional-semantics | medium_definition_and_adjacent-canon_support | medium | 315 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T099` | substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma | প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য | provisional-definition-and-lemma-governed | medium_definition_and_adjacent-canon_support | medium | 30 | BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T100` | model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain | মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র | mixed-attested-roots-and-provisional-model-theory | medium_definition_and_adjacent-canon_support | medium | 174 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T101` | main operator; immediate subformula; proper subformula; proper prefix | প্রধান অপারেটর; অব্যবহিত উপসূত্র; প্রকৃত উপসূত্র; প্রকৃত পূর্বাংশ | provisional-definition-governed-syntax-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T102` | term induction principle; formula induction principle; unique formation sequence | পদের উপর আরোহের নীতি; সূত্রের উপর আরোহের নীতি; একক গঠন-অনুক্রম | provisional-induction-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P008, BN-IN-P009, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T103` | variable assignment; x-variant; term valuation under an assignment; satisfaction under an assignment | চলরাশি-আরোপ; x-বিকল্প; আরোপের অধীনে পদের মান; আরোপের অধীনে পরিতৃপ্তি | mixed-attested-roots-and-provisional-tarskian-register | medium_definition_and_adjacent-canon_support | medium | 45 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T104` | covered structure; standard model of arithmetic; hereditarily finite sets; free logic | আচ্ছাদিত গঠন; পাটিগণিতের মানক মডেল; বংশগতভাবে সসীম সেট; মুক্ত যুক্তিবিদ্যা | mixed-definition-governed-and-provisional-model-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T105` | extensionality; relevance; Skolem normal form | ব্যাপ্তিগততা; প্রাসঙ্গিকতা; স্কোলেম স্বাভাবিক রূপ | provisional-definition-and-theorem-governed | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T106` | axiomatic theory; closure of a sentence set; axiomatized by; intended structure; capture a class; redundant axiom; definability | স্বতঃসিদ্ধমূলক তত্ত্ব; বাক্যসমষ্টির আবরণ; স্বতঃসিদ্ধায়িত; অভিপ্রেত গঠন; কোনো শ্রেণিকে ধারণ করা; অপ্রয়োজনীয় স্বতঃসিদ্ধ; সংজ্ঞেয়তা | mixed-attested-roots-and-provisional-axiomatic-register | medium_definition_and_adjacent-canon_support | medium | 9 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T107` | strict linear-order theory; group theory; Peano arithmetic; induction schema; pure set; urelement; set extensionality; naive comprehension scheme | কঠোর রৈখিক ক্রমের তত্ত্ব; গোষ্ঠীর তত্ত্ব; পেয়ানো পাটীগণিত; আরোহ-ছক; বিশুদ্ধ সেট; উর-উপাদান; সেটের সদস্যভিত্তিক সমতা; অনানুষ্ঠানিক ধর্মনির্দেশে সেট-গঠন ছক | mixed-attested-roots-and-provisional-theory-examples | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P001, BN-IN-P002, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P011, BN-IN-P013, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T108` | mereology; parthood; parthood structure; proper/improper part; mereological sum; fusion | অংশতত্ত্ব; অংশ-সম্পর্ক; অংশ-গঠন; যথার্থ/অযথার্থ অংশ; অংশতাত্ত্বিক যোগ; সংযোজন | provisional-definition-governed-mereology-register | medium_definition_and_adjacent-canon_support | medium | 26 | BN-IN-P001, BN-IN-P013, BN-IN-P018, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T109` | express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model | কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল | mixed-attested-roots-and-provisional-definability-register | medium_definition_and_adjacent-canon_support | medium | 29 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T110` | ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox | জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস | mixed-attested-set-roots-and-provisional-foundational-register | medium_definition_and_adjacent-canon_support | medium | 14 | BN-IN-P001, BN-IN-P002, BN-IN-P006, BN-IN-P007, BN-IN-P011, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T111` | size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure | গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন | mixed-attested-finiteness-and-provisional-model-size-register | medium_definition_and_adjacent-canon_support | medium | 225 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T112` | logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning | প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার | mixed-attested-roots-and-provisional-philosophical-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T113` | many-sorted logic; sort; sort-specific domain; typed function or relation; relativized quantifier; first-order embedding | বহুজাতীয় যুক্তিবিদ্যা; জাতি; জাতি-নির্দিষ্ট সংজ্ঞাক্ষেত্র; টাইপযুক্ত অপেক্ষক বা সম্পর্ক; আপেক্ষিক পরিমাণসূচক; প্রথম-ক্রমীয় নিবেশন | mixed-attested-roots-and-provisional-many-sorted-register | medium_definition_and_adjacent-canon_support | medium | 26 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T114` | second-order logic; relation variable; comprehension schema; impredicative/predicative comprehension; full/weak second-order semantics; categorical description; effective proof system | দ্বিতীয়-ক্রমের যুক্তিবিদ্যা; সম্পর্ক-চলরাশি; ধর্মনির্দেশ-ছক; অপ্রেডিকেটিভ/প্রেডিকেটিভ ধর্মনির্দেশ; পূর্ণ/দুর্বল দ্বিতীয়-ক্রমীয় অর্থতত্ত্ব; সমরূপতা-অবধি একক বর্ণনা; কার্যকর প্রমাণ-ব্যবস্থা | mixed-attested-roots-and-provisional-second-order-register | medium_definition_and_adjacent-canon_support | medium | 323 | BN-IN-P001, BN-IN-P002, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T115` | higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types | উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব | mixed-attested-roots-and-provisional-type-theory-register | medium_definition_and_adjacent-canon_support | medium | 57 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T116` | intuitionistic logic; constructive proof; BHK interpretation; formulas-as-types; Curry--Howard isomorphism; double-negation translation; Kripke structure; forcing relation | স্বজ্ঞাবাদী যুক্তিবিদ্যা; নির্মাণমূলক প্রমাণ; BHK ব্যাখ্যা; সূত্র-হিসেবে-টাইপ; কারি--হাওয়ার্ড সমরূপতা; দ্বিনঞর্থকতা অনুবাদ; ক্রিপকে গঠন; বাধ্যকরণ সম্পর্ক | mixed-attested-roots-and-provisional-intuitionistic-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T117` | modal logic; necessity/possibility; possible world; accessibility relation; intensional/extensional logic; provability/epistemic/temporal logic; S4/S5 | মোডাল যুক্তিবিদ্যা; আবশ্যিকতা/সম্ভাব্যতা; সম্ভাব্য জগৎ; অভিগম্যতা সম্পর্ক; অভিপ্রায়গত/ব্যাপ্তিগত যুক্তিবিদ্যা; প্রমাণযোগ্যতা/জ্ঞানতাত্ত্বিক/কালগত যুক্তিবিদ্যা; S4/S5 | mixed-attested-roots-and-provisional-modal-register | medium_definition_and_adjacent-canon_support | medium | 23 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T118` | fuzzy logic; probabilistic logic; default logic; nonmonotonic logic; defeasible reasoning; epistemic logic; causal logic; deontic logic | ফাজি যুক্তিবিদ্যা; সম্ভাবনামূলক যুক্তিবিদ্যা; ডিফল্ট যুক্তিবিদ্যা; অ-একঘেয়ে যুক্তিবিদ্যা; প্রত্যাহারযোগ্য যুক্তিবিচার; জ্ঞানতাত্ত্বিক যুক্তিবিদ্যা; কারণমূলক যুক্তিবিদ্যা; কর্তব্যগত যুক্তিবিদ্যা | provisional-survey-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P008, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T119` | model theory; basics; incomplete and experimental material; adaptation | মডেল তত্ত্ব; মূল বিষয়; অসম্পূর্ণ ও পরীক্ষামূলক উপকরণ; অভিযোজন | mixed-attested-roots-and-provisional-model-theory-editorial-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P001, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T120` | reduct; expansion; substructure; extension; common language; induced relational substructure | হ্রাসিত রূপ; সম্প্রসারণ; উপগঠন; বর্ধিত গঠন; অভিন্ন ভাষা; সম্পর্ক-প্রসূত উপগঠন | mixed-attested-roots-and-provisional-structure-comparison-register | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P001, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T121` | overspill; arbitrarily large finite models; finite satisfiability; infinite model | ওভারস্পিল; ইচ্ছামতো বড় সসীম মডেল; সসীমভাবে পরিতৃপ্তিযোগ্য; অসীম মডেল | mixed-attested-finiteness-and-provisional-compactness-register | medium_definition_and_adjacent-canon_support | medium | 33 | BN-IN-P001, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T122` | elementary equivalence; isomorphic structures; isomorphism; automorphism; definable subset; invariance | মৌলিকভাবে সমতুল্য; সমরূপ গঠন; সমরূপতা; স্বসমরূপতা; সংজ্ঞেয় উপসেট; অপরিবর্তিতা | mixed-attested-roots-and-provisional-isomorphism-register | medium_definition_and_adjacent-canon_support | medium | 25 | BN-IN-P006, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T123` | theory of a structure; complete theory; elementary equivalence; complete set of sentences | কোনো গঠনের তত্ত্ব; পূর্ণ তত্ত্ব; মৌলিক সমতুল্যতা; বাক্যের পূর্ণ সেট | mixed-attested-roots-and-provisional-complete-theory-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T124` | partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union | আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ | mixed-attested-roots-and-provisional-back-and-forth-register | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T125` | quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence | পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা | mixed-attested-roots-and-provisional-bounded-rank-register | medium_definition_and_adjacent-canon_support | medium | 24 | BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T126` | dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order | অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম | mixed-attested-order-roots-and-provisional-dense-order-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |

## Detailed review entries

### BN-IN-T001

- Source term or concept: set
- Chosen Bengali: সেট
- Rationale: Shared modern form in university and Tripura evidence.
- Plausible alternatives: সমষ্টি is a plausible alternative for set; সেট follows the directly checked university and school sources and avoids conflating an arbitrary set with a sum or collection in ordinary prose.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সেট’ express the OpenLogic sense(s) ‘set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 887 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:65`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:66`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:67`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:71`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:38-40` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:39`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the induction basis, we prove the claim for every !!{derivation}
of length~$1$. !!^a{derivation} of~$!B$ from $\Gamma \cup \{!A\}$ of
length~$1$ consists of $!B$ by itself; and if it is correct $!B$ is
either $\in \Gamma \cup \{!A\}$ or is an axiom.  If $!B \in \Gamma$ or
is an axiom, then $\Gamma \Proves !B$. We also have that $\Gamma
\Proves !B \lif (!A \lif !B)$ by \olref[prp]{ax:lif1}, and
\olref{prop:mp} gives $\Gamma \Proves !A \lif !B$. If $!B \in \{ !A\}$
then $\Gamma \Proves !A \lif !B$ because the last !!{sentence}~$!A
\lif !B$ is the same as $!A \lif !A$, and we have !!{derive}d that in
\olref[pro]{ex:identity}.
```

### BN-IN-T002

- Source term or concept: element
- Chosen Bengali: উপাদান
- Rationale: Use for set elements; preserve member synonym সদস্য where source distinguishes wording.
- Plausible alternatives: সেটের মৌল and সদস্য are plausible alternatives for element; উপাদান preserves the source distinction between an element as an object and membership as a relation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উপাদান’ express the OpenLogic sense(s) ‘element’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 73 occurrence(s). Representative locations:
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:13`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:48-81` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:47`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:81`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:102-112` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:109`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:200-222` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:190`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{editorial}
  No effort has been made yet to ensure that the material in this
  chapter respects various tags indicating which connectives and
  quantifiers are primitive or defined: all are assumed to be
  primitive, except $\liff$ which is assumed to be defined. If the FOL
  tag is true, we produce a version with quantifiers, otherwise
  without.
\end{editorial}
```

### BN-IN-T003

- Source term or concept: member
- Chosen Bengali: সদস্য
- Rationale: Synonym in set context only.
- Plausible alternatives: উপাদান is a plausible alternative for member; সদস্য is directly attested and pairs transparently with সদস্যতা for the membership relation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সদস্য’ express the OpenLogic sense(s) ‘member’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 55 occurrence(s). Representative locations:
  - `OLP-0132` `upstream/content/first-order-logic/completeness/construction-of-model.tex:249-260` → `bn-Beng-IN/content/first-order-logic/completeness/construction-of-model.tex:264`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:31-55` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:41`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:31-55` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:51`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:57-71` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:58`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:71-88` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:85`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\tagitem{prvEx}{%
  \iftag{probEx}{%
    \indcase!{!A}{\lexists[x][!B(x)]}{}}{%
    \indcase{!A}{\lexists[x][!B(x)]}{$\Sat{M(\Gamma^*)}{\indfrm}$ iff
      $\Sat{M(\Gamma^*)}{!B(t)}$ for at least one term~$t$
      (\olref{prop:quant-termmodel}).  By induction hypothesis, this
      is the case iff $!B(t) \in \Gamma^*$ for at least one term~$t$.
      By \olref[hen]{prop:saturated-instances}, this in turn is the
      case iff $\lexists[x][!B(x)] \in \Gamma^*$.}}}{}
}{}
\end{enumerate}
\end{proof}
```

### BN-IN-T004

- Source term or concept: empty set
- Chosen Bengali: শূন্য সেট
- Rationale: Do not conflate empty with zero as an element.
- Plausible alternatives: ফাঁকা সেট is a transparent alternative; শূন্য সেট is directly attested and remains distinct from the number zero through the adjacent set notation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘শূন্য সেট’ express the OpenLogic sense(s) ‘empty set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 18 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:32-36` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:33`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:89-93` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:87`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:187`; final reader page pending
  - `OLP-0143` `upstream/content/first-order-logic/introduction/satisfaction.tex:13-25` → `bn-Beng-IN/content/first-order-logic/introduction/satisfaction.tex:16`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:57-71` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:59`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Theorems]
!!^a{formula}~$!A$ is a \emph{theorem} if there is !!a{derivation} of
$!A$ from the empty set.  We write $\Proves !A$ if $!A$ is a theorem
and $\Proves/ !A$ if it is not.
\end{defn}
```

### BN-IN-T005

- Source term or concept: subset
- Chosen Bengali: উপসেট
- Rationale: Preserve inclusion signs exactly.
- Plausible alternatives: অন্তর্ভুক্ত সেট is a descriptive alternative; উপসেট is directly attested, compact and compatible with প্রকৃত উপসেট.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উপসেট’ express the OpenLogic sense(s) ‘subset’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 85 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:119`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:121`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:35`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:129-167` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:128`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:169-181` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:172`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}[Compactness]
\ollabel{prop:proves-compact}
  \begin{enumerate}
  \item If $\Gamma \Proves !A$ then there is a finite subset $\Gamma_0
    \subseteq \Gamma$ such that $\Gamma_0 \Proves !A$.
  \item If every finite subset of~$\Gamma$ is
    consistent, then $\Gamma$ is consistent.
  \end{enumerate}
\end{prop}
```

### BN-IN-T006

- Source term or concept: proper subset
- Chosen Bengali: প্রকৃত উপসেট
- Rationale: Prefer NSOU university form; Tripura যথার্থ উপসেট is recorded as regional variant.
- Plausible alternatives: যথার্থ উপসেট (Tripura regional witness); প্রকৃত উপসেট selected from university usage.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রকৃত উপসেট’ express the OpenLogic sense(s) ‘proper subset’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:158-168` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:122`; final reader page pending
  - `OLP-0050` `upstream/content/sets-functions-relations/infinite/hilberts-hotel.tex:60-64` → `bn-Beng-IN/content/sets-functions-relations/infinite/hilberts-hotel.tex:44`; final reader page pending
  - `OLP-0006` `upstream/content/sets-functions-relations/sets/subsets.tex:19-25` → `bn-Beng-IN/content/sets-functions-relations/sets/subsets.tex:23`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
Since $\alpha$ and $\beta$ are both cuts, $\alpha + \beta = \Setabs{p
+ q}{p \in \alpha \land q \in \beta}$ is a non-empty proper subset of
$\Rat$. Now suppose $x < p + q$ for some $p \in \alpha$ and $q \in \beta$.
Then $x - p < q$, so $x - p \in \beta$, and $x = p + (x - p) \in
\alpha + \beta$. So $\alpha + \beta$ is an initial segment of $\Rat$.
Finally, for any $p + q \in \alpha + \beta$, since $\alpha$ and
$\beta$ are both cuts, there are $p_1 \in \alpha$ and $q_1 \in \beta$
such that $p < p_1$ and $q < q_1$; so $p + q < p_1 + q_1 \in \alpha +
\beta$; so $\alpha + \beta$ has no maximum.
\end{proof}
```

### BN-IN-T007

- Source term or concept: power set
- Chosen Bengali: ঘাত সেট
- Rationale: Tripura directly attests term and concept; university corroboration of exact phrase remains open.
- Plausible alternatives: শক্তিসেট and ঘাতসমষ্টি are plausible alternatives for power set; ঘাত সেট is the directly witnessed Tripura form and remains marked as regional pending broader attestation.
- Status: attested-regional; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ঘাত সেট’ express the OpenLogic sense(s) ‘power set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:73-90` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:84`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:73-90` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:87`; final reader page pending
  - `OLP-0010` `upstream/content/sets-functions-relations/sets/russells-paradox.tex:27-34` → `bn-Beng-IN/content/sets-functions-relations/sets/russells-paradox.tex:25`; final reader page pending
  - `OLP-0006` `upstream/content/sets-functions-relations/sets/subsets.tex:9-10` → `bn-Beng-IN/content/sets-functions-relations/sets/subsets.tex:10`; final reader page pending
  - `OLP-0006` `upstream/content/sets-functions-relations/sets/subsets.tex:75-81` → `bn-Beng-IN/content/sets-functions-relations/sets/subsets.tex:72`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To talk about operations on sets, such as $X \cup Y$ and $\Pow{X}$, we
have to use a similar trick.  There are no function symbols in the
language of set theory, but we can express the functional relations $X
\cup Y = Z$ and $\Pow{X} = Y$ by
\begin{align*}
& \lforall[u][((u \in x \lor u \in y) \liff u \in z)]\\
& \lforall[u][(u \subseteq x \liff u \in y )]
\end{align*}
since the !!{element}s of $X \cup Y$ are exactly the sets that are
either !!{element}s of~$X$ or !!{element}s of~$Y$, and the
!!{element}s of $\Pow{X}$ are exactly the subsets of~$X$.  However,
this doesn't allow us to use $x \cup y$ or $\Pow{x}$ as if they were
terms: we can only use the entire !!{formula}s that define the
relations $X \cup Y = Z$ and $\Pow{X} = Y$. In fact, we do not know
that these relations are ever satisfied, i.e., we do not know that
unions and power sets always exist. For instance, the !!{sentence}
$\lforall[x][\lexists[y][\Pow{x} = y]]$ is another axiom
of~$\Log{ZFC}$ (the power set axiom).
```

### BN-IN-T008

- Source term or concept: extensionality
- Chosen Bengali: সদস্যভিত্তিক সমতার নীতি
- Rationale: Evidence attests equality by members, not the exact technical name; transparent descriptive term avoids false canon claim.
- Plausible alternatives: বহির্বিস্তার নীতি / extensionality loan; neither was found in checked pages, so descriptive সদস্যভিত্তিক সমতার নীতি remains provisional.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সদস্যভিত্তিক সমতার নীতি’ express the OpenLogic sense(s) ‘extensionality’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 20 occurrence(s). Representative locations:
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:31-55` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:41`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:71-88` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:85`; final reader page pending
  - `OLP-0023` `upstream/content/sets-functions-relations/functions/functions-relations.tex:32-37` → `bn-Beng-IN/content/sets-functions-relations/functions/functions-relations.tex:26`; final reader page pending
  - `OLP-0015` `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:47-55` → `bn-Beng-IN/content/sets-functions-relations/relations/equivalence-relations.tex:32`; final reader page pending
  - `OLP-0016` `upstream/content/sets-functions-relations/relations/orders.tex:152-153` → `bn-Beng-IN/content/sets-functions-relations/relations/orders.tex:90`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To begin with, ``is an element of'' is not the only relation we are
interested in: ``is a subset of'' seems almost as important.  But we
can \emph{define} ``is a subset of'' in terms of ``is an element of.''
To do this, we have to find !!a{formula}~$!A(x, y)$ in
the language of set theory which is satisfied by a pair of
sets~$\tuple{X, Y}$ iff $X \subseteq Y$.  But $X$ is a subset of $Y$
just in case all !!{element}s of~$X$ are also !!{element}s of~$Y$.  So
we can define $\subseteq$ by the formula
\[
\lforall[z][(z \in x \lif z \in y)]
\]
Now, whenever we want to use the relation~$\subseteq$ in a formula, we
could instead use that formula (with $x$ and $y$ suitably replaced,
and the bound variable~$z$ renamed if necessary).  For instance,
extensionality of sets means that if any sets~$x$ and $y$ are
contained in each other, then $x$ and $y$ must be the same set. This
can be expressed by $\lforall[x][\lforall[y][((x \subseteq y \land y
    \subseteq x) \lif x = y)]]$, or, if we replace $\subseteq$ by the
above definition, by
\[
\lforall[x][\lforall[y][((\lforall[z][(z \in x \lif z \in y)] \land
    \lforall[z][(z \in y \lif z \in x)]) \lif x = y)]].
\]
This is in fact one of the axioms of $\Log{ZFC}$, the ``axiom of
extensionality.''
```

### BN-IN-T009

- Source term or concept: natural number
- Chosen Bengali: স্বাভাবিক সংখ্যা
- Rationale: Follow OpenLogic zero-inclusive convention regardless of witness convention.
- Plausible alternatives: প্রাকৃতিক সংখ্যা is a widespread alternative; স্বাভাবিক সংখ্যা is directly attested in the checked India-standard source, while OpenLogic controls whether zero is included.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাভাবিক সংখ্যা’ express the OpenLogic sense(s) ‘natural number’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 65 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:33`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:36`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:52`; final reader page pending
  - `OLP-0169` `upstream/content/first-order-logic/models-theories/expressing-props-of-structures.tex:13-37` → `bn-Beng-IN/content/first-order-logic/models-theories/expressing-props-of-structures.tex:30`; final reader page pending
  - `OLP-0158` `upstream/content/first-order-logic/syntax-and-semantics/substitution.tex:100-114` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/substitution.tex:109`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In practice, higher-order logic is often !!{formula}ted in terms of
functions instead of relations. (Modulo the natural identifications,
this difference is inessential.) Given some basic ``sorts'' $A$, $B$,
$C$,~\dots (which we will now call ``types''), we can create new ones
by stipulating
\begin{quote}
If $\sigma$ and $\tau$ are finite types then so is $\sigma \to \tau$.
\end{quote}
Think of types as syntactic ``labels,'' which classify the objects we
want in our !!{domain}; $\sigma \to \tau$ describes those objects that
are functions which take objects of type~$\sigma$ to objects of
type~$\tau$. For example, we might want to have a type $\Omega$ of
truth values, ``true'' and ``false,'' and a type $\Nat$ of natural
numbers. In that case, you can think of objects of type $\Nat \to
\Omega$ as unary relations, or subsets of $\Nat$; objects of type
$\Nat \to \Nat$ are functions from natural numbers to natural numbers;
and objects of type $(\Nat \to \Nat) \to \Nat$ are ``functionals,''
that is, higher-type functions that take functions to numbers.
```

### BN-IN-T010

- Source term or concept: proposition (logic)
- Chosen Bengali: বচন
- Rationale: University philosophy form preferred; distinguish sentence বাক্য and school উক্তি.
- Plausible alternatives: উক্তি occurs in school material; বচন selected for the proposition sense from university philosophy.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বচন’ express the OpenLogic sense(s) ‘proposition (logic)’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 52 occurrence(s). Representative locations:
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13`; final reader page pending
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:15-34` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:16`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:13`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:17`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:33-52` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Axioms and Rules for the Propositional Connectives}
```

### BN-IN-T011

- Source term or concept: quantifier
- Chosen Bengali: পরিমাণসূচক
- Rationale: Use mathematical quantifier semantics from OpenLogic.
- Plausible alternatives: পরিমাণক is a shorter plausible alternative; পরিমাণসূচক matches the checked university philosophy wording and exposes the quantifying role.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিমাণসূচক’ express the OpenLogic sense(s) ‘quantifier’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 96 occurrence(s). Representative locations:
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:14`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:17`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:11-11` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:11`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:14`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{editorial}
  No effort has been made yet to ensure that the material in this
  chapter respects various tags indicating which connectives and
  quantifiers are primitive or defined: all are assumed to be
  primitive, except $\liff$ which is assumed to be defined. If the FOL
  tag is true, we produce a version with quantifiers, otherwise
  without.
\end{editorial}
```

### BN-IN-T012

- Source term or concept: universal quantifier
- Chosen Bengali: সার্বিক পরিমাণসূচক
- Rationale: Retain source variable-binding convention.
- Plausible alternatives: সর্বজনীন পরিমাণসূচক and সকলবাচক পরিমাণসূচক are plausible alternatives; সার্বিক পরিমাণসূচক follows the attested সার্বিক root.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সার্বিক পরিমাণসূচক’ express the OpenLogic sense(s) ‘universal quantifier’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:34-63` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:42`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:91-104` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:99`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:134-141` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:134`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:23-36` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{enumerate}
\item Logical symbols
\begin{enumerate}
\item Logical connectives:
  \startycommalist
  \iftag{prvNot}{\ycomma $\lnot$ (negation)}{}%
  \iftag{prvAnd}{\ycomma $\land$ (conjunction)}{}%
  \iftag{prvOr}{\ycomma $\lor$ (disjunction)}{}%
  \iftag{prvIf}{\ycomma $\lif$ (!!{conditional})}{}%
  \iftag{prvIff}{\ycomma $\liff$ (!!{biconditional})}{}%
  \iftag{prvAll}{\ycomma $\lforall$ (universal quantifier)}{}%
  \iftag{prvEx}{\ycomma $\lexists$ (existential quantifier)}{}.
\tagitem{prvFalse}{The propositional constant for !!{falsity}~$\lfalse$.}{}
\tagitem{prvTrue}{The propositional constant for !!{truth}~$\ltrue$.}{}
\item The two-place !!{identity}~$\eq$.
\item A !!{denumerable}s set of !!{variable}s: $\Obj v_0$, $\Obj v_1$, $\Obj
  v_2$, \dots
\end{enumerate}
\item Non-logical symbols, making up the \emph{standard
  language} of first-order logic
\begin{enumerate}
\item A !!{denumerable}s set of $n$-place !!{predicate}s for each $n>0$: $\Obj
  A^n_0$, $\Obj A^n_1$, $\Obj A^n_2$, \dots
\item A !!{denumerable}s set of !!{constant}s: $\Obj c_0$, $\Obj c_1$, $\Obj
  c_2$, \dots.
\item A !!{denumerable}s set of $n$-place !!{function}s for each $n>0$:
  $\Obj f^n_0$, $\Obj f^n_1$, $\Obj f^n_2$, \dots
\end{enumerate}
\item Punctuation marks: (, ), and the comma.
\end{enumerate}
```

### BN-IN-T013

- Source term or concept: existential quantifier
- Chosen Bengali: অস্তিত্বমূলক পরিমাণসূচক
- Rationale: The source also uses an alternative form; choose one consistently.
- Plausible alternatives: অস্তিত্বসূচক পরিমাণসূচক is a compact alternative; অস্তিত্বমূলক পরিমাণসূচক follows the checked university formulation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অস্তিত্বমূলক পরিমাণসূচক’ express the OpenLogic sense(s) ‘existential quantifier’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T014

- Source term or concept: if and only if
- Chosen Bengali: যদি এবং কেবল যদি
- Rationale: Biconditional concept corroborated by equality criterion; exact phrase not claimed verbatim.
- Plausible alternatives: ঠিক তখনই যখন is a concise alternative for iff; যদি এবং কেবল যদি preserves both conditional directions explicitly and matches the edition’s proof register.
- Status: provisional-phrase; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যদি এবং কেবল যদি’ express the OpenLogic sense(s) ‘if and only if’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 198 occurrence(s). Representative locations:
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:33-36` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:35`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:55-58` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:58`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:87-107` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:102`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:200-222` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:197`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:200-222` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:200`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
\ollabel{prop:prov-incons}
$\Gamma \Proves !A$ iff $\Gamma \cup \{\lnot !A\}$ is inconsistent.
\end{prop}
```

### BN-IN-T015

- Source term or concept: perfect number
- Chosen Bengali: নিখুঁত সংখ্যা
- Rationale: Number-system vocabulary provides prose context only, not perfect-number attestation. Transparent provisional term preserves distinction from integer (পূর্ণসংখ্যা); definition from OpenLogic governs.
- Plausible alternatives: পরিপূর্ণ সংখ্যা is a literal alternative; নিখুঁত সংখ্যা avoids collision with logical completeness and is transparently governed by the divisor-sum definition.
- Status: provisional-descriptive; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিখুঁত সংখ্যা’ express the OpenLogic sense(s) ‘perfect number’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T016

- Source term or concept: union; intersection; disjoint; difference
- Chosen Bengali: সংযোগ; ছেদ; বিচ্ছিন্ন; অন্তর
- Rationale: University mathematical usage; qualify union with set context to distinguish logical conjunction.
- Plausible alternatives: মিলন or সম্মিলন, সাধারণ অংশ, নিঃছেদ and বিয়োগ are plausible alternatives; সংযোগ, ছেদ, বিচ্ছিন্ন and অন্তর follow the checked mathematical usage and keep the four operations or properties distinct.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংযোগ; ছেদ; বিচ্ছিন্ন; অন্তর’ express the OpenLogic sense(s) ‘union; intersection; disjoint; difference’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 88 occurrence(s). Representative locations:
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:13-15` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:13`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:116`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:13-17` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:16`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:13-17` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:15`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:83-98` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:86`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In order to accommodate $\eq$ in !!{derivation}s, we simply add new
axiom schemas. The definition of !!{derivation} and $\Proves$ remains
the same, we just also allow the new axioms.
```

### BN-IN-T017

- Source term or concept: ordered pair
- Chosen Bengali: ক্রমযুগল
- Rationale: Keep order-sensitive pair distinct from unordered two-element set.
- Plausible alternatives: ক্রমিত জোড়া and সুশৃঙ্খল যুগল are plausible alternatives; ক্রমযুগল is directly attested and compactly marks order sensitivity.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ক্রমযুগল’ express the OpenLogic sense(s) ‘ordered pair’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 40 occurrence(s). Representative locations:
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:92-110` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:89`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:92-110` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:91`; final reader page pending
  - `OLP-0042` `upstream/content/sets-functions-relations/arithmetization/integers.tex:13-18` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/integers.tex:16`; final reader page pending
  - `OLP-0042` `upstream/content/sets-functions-relations/arithmetization/integers.tex:13-18` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/integers.tex:18`; final reader page pending
  - `OLP-0042` `upstream/content/sets-functions-relations/arithmetization/integers.tex:22-30` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/integers.tex:24`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Now what about talk of ordered pairs or functions?  Here we have to
explain how we can think of ordered pairs and functions as special
kinds of sets.  One way to define the ordered pair $\tuple{x, y}$ is
as the set $\{\{x\}, \{x, y\}\}$.  But like before, we cannot
introduce !!a{function} that names this set; we can only define the
relation $\tuple{x, y} = z$, i.e., $\{\{x\}, \{x, y\}\} = z$:
\[
\lforall[u][(u \in z \liff (\lforall[v][(v \in u \liff v = x)] \lor
  \lforall[v][(v \in u \liff (v = x \lor v = y))]))]
\]
This says that the !!{element}s~$u$ of~$z$ are exactly those sets which
either have $x$ as its only !!{element} or have $x$ and~$y$ as its
only !!{element}s (in other words, those sets that are either identical
to $\{x\}$ or identical to $\{x, y\}$).  Once we have this, we can say
further things, e.g., that $X \times Y = Z$:
\[
\lforall[z][(z \in Z \liff \lexists[x][\lexists[y][(x \in
        X \land y \in Y \land \tuple{x, y} = z)]])]
\]
```

### BN-IN-T018

- Source term or concept: Cartesian product
- Chosen Bengali: কার্তেসীয় গুণফল
- Rationale: University witness attests concept and a related Cartesian multiplication wording; chosen normalized phrase remains provisional.
- Plausible alternatives: কার্তেসীয় গুণ chosen descriptively; no directly attested full compound found in checked pages.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কার্তেসীয় গুণফল’ express the OpenLogic sense(s) ‘Cartesian product’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0012` `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:23-32` → `bn-Beng-IN/content/sets-functions-relations/relations/relations-as-sets.tex:28`; final reader page pending
  - `OLP-0009` `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:9-10` → `bn-Beng-IN/content/sets-functions-relations/sets/pairs-and-products.tex:10`; final reader page pending
  - `OLP-0009` `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:52-58` → `bn-Beng-IN/content/sets-functions-relations/sets/pairs-and-products.tex:50`; final reader page pending
  - `OLP-0009` `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:52-58` → `bn-Beng-IN/content/sets-functions-relations/sets/pairs-and-products.tex:51`; final reader page pending
  - `OLP-0030` `upstream/content/sets-functions-relations/size-of-sets/zig-zag.tex:78-112` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/zig-zag.tex:73`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For this, recall two things from \olref[sfr][set][pai]{sec}. First,
recall the notion of an \emph{ordered pair}: given $a$ and $b$, we can
form~$\tuple{a, b}$. Importantly, the order of elements \emph{does}
matter here. So if $a \neq b$ then $\tuple{a, b} \neq \tuple{b, a}$.
(Contrast this with unordered pairs, i.e., $2$-element sets, where
$\{a, b\}=\{b, a\}$.) Second, recall the notion of a \emph{Cartesian
product}: if $A$ and $B$ are sets, then we can form~$A \times B$, the
set of all pairs $\tuple{x, y}$ with $x \in A$ and $y \in B$. In
particular, $A^{2}= A \times A$ is the set of all ordered pairs
from~$A$.
```

### BN-IN-T019

- Source term or concept: string; sequence; tuple; word
- Chosen Bengali: প্রতীকক্রম; অনুক্রম; টিউপল; শব্দ
- Rationale: Canon provides mathematical prose and order-sensitive pair context, not direct attestation for every computing sense. Definitions follow English OpenLogic.
- Plausible alternatives: স্ট্রিং, ধারা, ক্রমিত টিউপল and অক্ষরসমষ্টি are plausible alternatives; প্রতীকক্রম, অনুক্রম, টিউপল and শব্দ preserve the four distinct source categories.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রতীকক্রম; অনুক্রম; টিউপল; শব্দ’ express the OpenLogic sense(s) ‘string; sequence; tuple; word’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 229 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:69-84` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:77`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:128`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:15-22` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:18`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:48-81` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:47`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
  Suppose $\{!A\} \cup \Delta \Proves !B$. Then there is
  !!a{derivation} $!B_1$, \dots, $!B_l = !B$ from~$\{!A\} \cup
  \Delta$. Some of the steps in that !!{derivation} will be correct
  because of a rule which refers to a prior line~$!B_i = !A$. By
  hypothesis, there is !!a{derivation} of~$!A$ from~$\Gamma$, i.e.,
  !!a{derivation}~$!A_1$, \dots, $!A_k = !A$ where every $!A_i$ is an
  axiom, !!a{element} of~$\Gamma$, or correct by a rule of
  inference. Now consider the sequence
  \[
  !A_1, \dots, !A_k = !A, !B_1, \dots, !B_l = !B.
  \]
  This is a correct !!{derivation} of~$!B$ from $\Gamma \cup \Delta$
  since every $B_i = !A$ is now justified by the same rule which
  justifies~$!A_k = !A$.
\end{proof}
```

### BN-IN-T020

- Source term or concept: paradox; contradiction; comprehension; naive set theory
- Chosen Bengali: কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব
- Rationale: Set/proposition evidence gives context only; no claim of direct attestation. Preserve distinction between conditional uniqueness and existence.
- Plausible alternatives: প্যারাডক্স, বিরোধ, অবাধ ধর্মগ্রহণ and সরল সেটতত্ত্ব are plausible alternatives; the selected forms distinguish a paradox from a formal contradiction and describe unrestricted comprehension without claiming direct canon attestation.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব’ express the OpenLogic sense(s) ‘paradox; contradiction; comprehension; naive set theory’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 49 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:113`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:75`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:19`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:133-149` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:142`; final reader page pending
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:48-61` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:45`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  \ollabel{prop:derivfacts}
\begin{enumerate}
\item $\Proves (!A \lif !B) \lif ((!B \lif !C)
  \lif (!A \lif !C)$; \ollabel{derivfacts:a}
\item If $\Gamma \cup \{ \lnot !A\}
  \Proves \lnot !B$ then $\Gamma \cup \{ !B\} \Proves
  !A$ (Contraposition); \ollabel{derivfacts:b}
\item  $\{ !A, \lnot!A\} \Proves
    !B$ (Ex Falso Quodlibet, Explosion); \ollabel{derivfacts:c}
\item  $\{ \lnot\lnot!A\} \Proves
  !A$ (Double Negation Elimination);\ollabel{derivfacts:d}
\item If $\Gamma \Proves \lnot\lnot!A$ then $\Gamma \Proves
  !A$;\ollabel{derivfacts:e}
\end{enumerate}
\end{prop}
```

### BN-IN-T021

- Source term or concept: conjunction; conjunction elimination; absorption
- Chosen Bengali: সংযোজন; সংযোজন অপসারণ; শোষণ
- Rationale: Logic and set-operation witnesses inform wording; these exact normalized phrases are not claimed directly attested. Preserve Elim rule labels as formal notation.
- Plausible alternatives: অন্তঃসংযোগ is a directly witnessed regional alternative for conjunction; সংযোজন continues the edition-wide connective choice, while অপসারণ and শোষণ identify the formal rule and law.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংযোজন; সংযোজন অপসারণ; শোষণ’ express the OpenLogic sense(s) ‘conjunction; conjunction elimination; absorption’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:108-141` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:138`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:34-63` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:38`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:91-104` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:95`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:120-132` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:120`; final reader page pending
  - `OLP-0154` `upstream/content/first-order-logic/syntax-and-semantics/main-operator.tex:79-99` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/main-operator.tex:89`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The language of mereology contains a single two-place predicate
symbol~$\Obj P$, and $\Atom{\Obj P}{x, y}$ ``means'' that $x$ is a
part of~$y$.  When we have this interpretation in mind, !!a{structure}
for this language is called a \emph{parthood structure}.  Of course,
not every structure for a single two-place predicate will really
deserve this name.  To have a chance of capturing ``parthood,''
$\Assign{\Obj P}{M}$ must satisfy some conditions, which we can lay
down as axioms for a theory of parthood.  For instance, parthood is a
partial order on objects: every object is a part (albeit an
\emph{improper} part) of itself; no two different objects can be parts
of each other; a part of a part of an object is itself part of that
object.  Note that in this sense ``is a part of'' resembles ``is a
subset of,'' but does not resemble ``is an element of'' which is
neither reflexive nor transitive.
\begin{align*}
& \lforall[x][\Atom{\Obj P}{x,x}] \\
& \lforall[x][\lforall[y][((\Part{x}{y} \land \Part{y}{x})
      \lif \eq[x][y])]] \\
& \lforall[x][\lforall[y][\lforall[z][((\Part{x}{y} \land
        \Part{y}{z}) \lif \Part{x}{z})]]]\\
\intertext{Moreover, any two objects have a mereological sum (an object that has
  these two objects as parts, and is minimal in this respect).}  &
\lforall[x][\lforall[y][\lexists[z][\lforall[u][(\Part{z}{u} \liff
        (\Part{x}{u} \land \Part{y}{u}))]]]]
\end{align*}
These are only some of the basic principles of parthood considered by
metaphysicians.  Further principles, however, quickly become hard to
formulate or write down without first introducing some defined
relations.  For instance, most metaphysicians interested in mereology
also view the following as a valid principle: whenever an
object~$x$ has a proper part~$y$, it also has a part~$z$ that has no
parts in common with~$y$, and so that the fusion of $y$ and $z$ is
$x$.
\end{ex}
```

### BN-IN-T022

- Source term or concept: relation; binary relation; order relation; identity relation
- Chosen Bengali: সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক
- Rationale: সম্পর্ক and set-based relation definition are directly attested; binary/order/identity compounds follow source definitions and are provisionally normalized.
- Plausible alternatives: চিত্রণ is reserved for mapping/function use; সম্পর্ক is directly attested for relation.
- Status: mixed-attested-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক’ express the OpenLogic sense(s) ‘relation; binary relation; order relation; identity relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 278 occurrence(s). Representative locations:
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:15-17` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:15`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:16`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:21`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:34`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:19`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We will now establish a number of properties of the !!{derivability}
relation.  They are independently interesting, but each will play a
role in the proof of the completeness theorem.
```

### BN-IN-T023

- Source term or concept: irreflexive; strict order; empty relation; universal relation
- Chosen Bengali: আত্মসম্পর্কহীন; কঠোর ক্রম; শূন্য সম্পর্ক; সার্বিক সম্পর্ক
- Rationale: Explicitly descriptive compounds; irreflexive means no self-pair and is distinguished from failure of reflexivity. Source supplies definitions.
- Plausible alternatives: অপ্রতিবিম্বী, দৃঢ় ক্রম and সর্বসম্বন্ধ are plausible alternatives; আত্মসম্পর্কহীন, কঠোর ক্রম and সার্বিক সম্পর্ক state the defining conditions more transparently.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আত্মসম্পর্কহীন; কঠোর ক্রম; শূন্য সম্পর্ক; সার্বিক সম্পর্ক’ express the OpenLogic sense(s) ‘irreflexive; strict order; empty relation; universal relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 19 occurrence(s). Representative locations:
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:49-98` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:90`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:49-98` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:92`; final reader page pending
  - `OLP-0016` `upstream/content/sets-functions-relations/relations/orders.tex:37-43` → `bn-Beng-IN/content/sets-functions-relations/relations/orders.tex:29`; final reader page pending
  - `OLP-0016` `upstream/content/sets-functions-relations/relations/orders.tex:82-85` → `bn-Beng-IN/content/sets-functions-relations/relations/orders.tex:48`; final reader page pending
  - `OLP-0016` `upstream/content/sets-functions-relations/relations/orders.tex:82-85` → `bn-Beng-IN/content/sets-functions-relations/relations/orders.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The important logical facts that make this formal approach to the
axiomatic method so important are the following.  Suppose $\Gamma$ is
an axiom system for a theory, i.e., a set of sentences.
\begin{enumerate}
\item We can state precisely when an axiom system captures an intended
  class of !!{structure}s.  That is, if we are interested in a certain
  class of !!{structure}s, we will successfully capture that class by
  an axiom system~$\Gamma$ iff the !!{structure}s are exactly
  those~$\Struct M$ such that $\Sat{M}{\Gamma}$.
\item We may fail in this respect because there are $\Struct M$ such
  that $\Sat{M}{\Gamma}$, but $\Struct M$ is not one of the
  !!{structure}s we intend.  This may lead us to add axioms which are
  not true in~$\Struct M$.
\item If we are successful at least in the respect that $\Gamma$ is
  true in all the intended !!{structure}s, then a sentence~$!A$ is true in
  all intended !!{structure}s whenever $\Gamma \Entails !A$.  Thus we can
  use logical tools (such as !!{derivation} methods) to show that sentences are
  true in all intended !!{structure}s simply by showing that they are
  entailed by the axioms.
\item Sometimes we don't have intended !!{structure}s in mind, but instead
  start from the axioms themselves: we begin with some primitives that
  we want to satisfy certain laws which we codify in an axiom system.
  One thing that we would like to verify right away is that the axioms
  do not contradict each other: if they do, there can be no concepts
  that obey these laws, and we have tried to set up an incoherent
  theory.  We can verify that this doesn't happen by finding a model
  of~$\Gamma$.  And if there are models of our theory, we can use
  logical methods to investigate them, and we can also use logical
  methods to construct models.
\item The independence of the axioms is likewise an important
  question.  It may happen that one of the axioms is actually a
  consequence of the others, and so is redundant.  We can prove that
  an axiom $!A$ in $\Gamma$ is redundant by proving $\Gamma \setminus
  \{!A\} \Entails !A$.  We can also prove that an axiom is not
  redundant by showing that $(\Gamma \setminus \{!A\}) \cup \{\lnot
  !A\}$ is satisfiable.  For instance, this is how it was shown that the
  parallel postulate is independent of the other axioms of geometry.
\item Another important question is that of definability of concepts
  in a theory: The choice of the language determines what the models
  of a theory consist of.  But not every aspect of a theory must be
  represented separately in its models.  For instance, every ordering
  $\le$ determines a corresponding strict ordering~$<$---given one, we
  can define the other.  So it is not necessary that a model of a
  theory involving such an order must \emph{also} contain the
  corresponding strict ordering.  When is it the case, in general,
  that one relation can be defined in terms of others?  When is it
  impossible to define a relation in terms of others (and hence must
  add it to the primitives of the language)?
\end{enumerate}
\end{explain}
```

### BN-IN-T024

- Source term or concept: continuum; mathematical proposition heading; general conditional proof
- Chosen Bengali: সতত সমষ্টি; প্রতিজ্ঞা; সাধারণ শর্তাধীন প্রমাণ
- Rationale: Relevant number/proposition/proof contexts support interpretation, not exact phrase attestation. Mathematical proposition headings are distinguished from logical propositions (বচন).
- Plausible alternatives: নিরবচ্ছিন্নতা, উপপাদ্য and সাধারণ শর্তসাপেক্ষ প্রমাণ are plausible alternatives; সতত সমষ্টি, প্রতিজ্ঞা and সাধারণ শর্তাধীন প্রমাণ keep the set, heading and proof-pattern senses separate.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সতত সমষ্টি; প্রতিজ্ঞা; সাধারণ শর্তাধীন প্রমাণ’ express the OpenLogic sense(s) ‘continuum; mathematical proposition heading; general conditional proof’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 15 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:111`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:137`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:59-66` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:62`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:129-140` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:134`; final reader page pending
  - `OLP-0091` `upstream/content/first-order-logic/natural-deduction/proof-theoretic-notions.tex:146-157` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proof-theoretic-notions.tex:157`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  \ollabel{prop:derivfacts}
\begin{enumerate}
\item $\Proves (!A \lif !B) \lif ((!B \lif !C)
  \lif (!A \lif !C)$; \ollabel{derivfacts:a}
\item If $\Gamma \cup \{ \lnot !A\}
  \Proves \lnot !B$ then $\Gamma \cup \{ !B\} \Proves
  !A$ (Contraposition); \ollabel{derivfacts:b}
\item  $\{ !A, \lnot!A\} \Proves
    !B$ (Ex Falso Quodlibet, Explosion); \ollabel{derivfacts:c}
\item  $\{ \lnot\lnot!A\} \Proves
  !A$ (Double Negation Elimination);\ollabel{derivfacts:d}
\item If $\Gamma \Proves \lnot\lnot!A$ then $\Gamma \Proves
  !A$;\ollabel{derivfacts:e}
\end{enumerate}
\end{prop}
```

### BN-IN-T025

- Source term or concept: predicate; singular term; metaphysical identity; set-theoretic reductionism
- Chosen Bengali: বিধেয়; একবস্তুনির্দেশক পদ; অধিবিদ্যাগত অভিন্নতা; সেটতত্ত্বে পর্যবসনবাদ
- Rationale: University-level philosophy uses subject/predicate and individual-reference contrasts. The longer philosophical compounds are descriptive provisional decisions; no direct phrase attestation is claimed.
- Plausible alternatives: একক পদ, অধিবিদ্যাগত একত্ব and সেটতাত্ত্বিক হ্রাসবাদ are plausible alternatives; the selected compounds preserve singular reference, identity and reductionism as distinct philosophical claims.
- Status: mixed-contextual-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিধেয়; একবস্তুনির্দেশক পদ; অধিবিদ্যাগত অভিন্নতা; সেটতত্ত্বে পর্যবসনবাদ’ express the OpenLogic sense(s) ‘predicate; singular term; metaphysical identity; set-theoretic reductionism’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:41`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:135-149` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:137`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:44-64` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:62`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:31-39` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:35`; final reader page pending
  - `OLP-0140` `upstream/content/first-order-logic/introduction/first-order-logic.tex:13-31` → `bn-Beng-IN/content/first-order-logic/introduction/first-order-logic.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
No easy answers are forthcoming. The word ``logic'' is used in
different ways and in different contexts, and the notion, like that of
``truth,'' has been analyzed from numerous philosophical stances. For
example, one might take the goal of logical reasoning to be the
determination of which statements are necessarily true, true a priori,
true independent of the interpretation of the nonlogical terms, true
by virtue of their form, or true by linguistic convention; and each of
these conceptions requires a good deal of clarification. Even if one
restricts one's attention to the kind of logic used in mathematics,
there is little agreement as to its scope. For example, in the
\textit{Principia Mathematica}, Russell and Whitehead tried to develop
mathematics on the basis of logic, in the {\em logicist} tradition
begun by Frege. Their system of logic was a form of higher-type logic
similar to the one described below. In the end they were forced to
introduce axioms which, by most standards, do not seem purely logical
(notably, the axiom of infinity, and the axiom of reducibility), but
one might nonetheless hold that some forms of higher-order reasoning
should be accepted as logical. In contrast, Quine, whose ontology does
not admit ``propositions'' as legitimate objects of discourse, argues
that second-order and higher-order logic are really manifestations of
set theory in sheep's clothing; in other words, systems involving
quantification over predicates are not purely logical.
```

### BN-IN-T026

- Source term or concept: reflexivity; symmetry; transitivity; equivalence relation
- Chosen Bengali: প্রতিবিম্ব ধর্ম; প্রতিসাম্য; পরিযায়িতা; তুল্যতা সম্পর্ক
- Rationale: NSOU headings attest প্রতিবিম্ব, প্রতিসম, পরিযায়ী and তুল্যতা সম্পর্ক. Property nouns are normalized derivatives; reflexivity is worded প্রতিবিম্ব ধর্মবিশিষ্ট when an adjective is required.
- Plausible alternatives: প্রতিবিম্ব root in NSOU versus reflexivity loan; compound keeps the property distinct from function image by context.
- Status: attested-roots-normalized-properties; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রতিবিম্ব ধর্ম; প্রতিসাম্য; পরিযায়িতা; তুল্যতা সম্পর্ক’ express the OpenLogic sense(s) ‘reflexivity; symmetry; transitivity; equivalence relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 57 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:43-46` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:43`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:63-67` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:63`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:54-58` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:52`; final reader page pending
  - `OLP-0131` `upstream/content/first-order-logic/completeness/lindenbaums-lemma.tex:65-74` → `bn-Beng-IN/content/first-order-logic/completeness/lindenbaums-lemma.tex:69`; final reader page pending
  - `OLP-0147` `upstream/content/first-order-logic/introduction/models-theories.tex:32-54` → `bn-Beng-IN/content/first-order-logic/introduction/models-theories.tex:33`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}[Reflexivity]
\ollabel{prop:reflexivity}
If $!A \in \Gamma$, then $\Gamma \Proves !A$.
\end{prop}
```

### BN-IN-T027

- Source term or concept: antisymmetric; asymmetric; connected (relation)
- Chosen Bengali: বিপ্রতিসম; একমুখী; সংযুক্ত
- Rationale: Witness directly attests symmetry but not these three properties. Antisymmetry permits self-pairs and excludes distinct reciprocal pairs; asymmetry excludes all reciprocal pairs including self-pairs. Connected means every distinct pair is comparable here, not graph connectivity. Definitions remain explicit.
- Plausible alternatives: প্রতিসম-বিরোধী, অসমমিত and তুলনীয় are plausible alternatives; বিপ্রতিসম, একমুখী and সংযুক্ত remain governed by the explicit relation clauses, especially the different treatment of self-pairs.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিপ্রতিসম; একমুখী; সংযুক্ত’ express the OpenLogic sense(s) ‘antisymmetric; asymmetric; connected (relation)’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 28 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:188`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:189`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:46-50` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:51`; final reader page pending
  - `OLP-0152` `upstream/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:176-183` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:171`; final reader page pending
  - `OLP-0152` `upstream/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:176-183` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:174`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In addition, one can define the class of well-orderings, by adding the
following to the definition of a linear ordering:
\[
\lforall[P][(\lexists[x][\Atom{P}{x}] \lif \lexists[x][(\Atom{P}{x}
    \land \lforall[y][(y < x \lif \lnot \Atom{P}{y})])])].
\]
This asserts that every non-empty set has a least element, modulo the
identification of ``set'' with ``one-place relation''. For another
example, one can express the notion of connectedness for graphs, by
saying that there is no nontrivial separation of the vertices into
disconnected parts:
\[
\lnot \lexists[A][(\lexists[x][A(x)] \land \lexists[y][\lnot A(y)]
  \land \lforall[w][\lforall[z][((\Atom{A}{w} \land \lnot \Atom{A}{z})
      \lif \lnot \Atom{R}{w,z})]])].
\]
For yet another example, you might try as an exercise to define the
class of finite !!{structure}s whose !!{domain} has even size. More
strikingly, one can provide a categorical description of the real
numbers as a complete ordered field containing the rationals.
```

### BN-IN-T028

- Source term or concept: equivalence class; partition; quotient set; congruence modulo n
- Chosen Bengali: তুল্যতা শ্রেণি; বিভাজন; ভাগসেট; মডুলো n সমতুল্যতা
- Rationale: Class and partition roots directly attested, শ্রেণি uses modern spelling. Quotient and modular phrase are provisional normalizations. Each block is a বিভাজনখণ্ড, not itself the entire partition; source's loose English partition usage is rendered conceptually accurately.
- Plausible alternatives: তুল্যতা শ্রেণী is an orthographic alternative, while খণ্ডায়ন, ভাগফল সেট and মডুলো সমাপতন are lexical alternatives; the selected terms follow the checked class/partition roots and keep quotienting distinct from arithmetic division.
- Status: mixed-attested-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘তুল্যতা শ্রেণি; বিভাজন; ভাগসেট; মডুলো n সমতুল্যতা’ express the OpenLogic sense(s) ‘equivalence class; partition; quotient set; congruence modulo n’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 18 occurrence(s). Representative locations:
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:109-125` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:64`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:133-147` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:70`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:149-163` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:84`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:169-171` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:100`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:176-179` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:106`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Consequently, we again need to define an equivalence relation on the
Cauchy sequences, and identify real numbers with equivalence
relations. First we need the idea of a function which tends to $0$ in
the limit. For any function $h : \Nat \to \Rat$, say that \emph{$h$
tends to $0$} iff for any positive $\epsilon \in \Rat$ we have that
$(\exists \ell \in \Nat)(\forall n > \ell)|h(n)| <
\epsilon$.\footnote{Compare this with the definition of $\lim_{x
\mathord{\rightarrow}\infty}f(x) = 0$ in
\olref[his][set][limits]{sec}.} Further, where $f$ and $g$ are
functions $\Nat \to \Rat$, let $(f-g)(n) = f(n) - g(n)$. Now define:
\[
	f \Realequiv g \text{ iff $(f-g)$ tends to $0$}.
\]
We need to check that $\Realequiv$ is an equivalence relation; and it
is. We can then, if we like, define the reals as the equivalence
classes, under $\Realequiv$, of all Cauchy sequences from $\Nat \to
\Rat$.
```

### BN-IN-T029

- Source term or concept: preorder; partial order; linear order; total order; closure; initial segment
- Chosen Bengali: প্রাক্‌ক্রম; আংশিক ক্রম; রৈখিক ক্রম; পূর্ণ ক্রম; আবরণ; প্রারম্ভিক খণ্ড
- Rationale: Witness supplies the defining relation properties and proof prose, not these exact order/closure names. Source definitions govern. Closure means adding the required pairs, not a topological assertion; provisional wording remains revisable.
- Plausible alternatives: পূর্বক্রম, অসম্পূর্ণ ক্রম, সরল ক্রম, সমগ্র ক্রম, সংবরণ and আদি খণ্ড are plausible alternatives; the selected terms preserve the hierarchy fixed by the displayed reflexivity, transitivity and comparability clauses.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রাক্‌ক্রম; আংশিক ক্রম; রৈখিক ক্রম; পূর্ণ ক্রম; আবরণ; প্রারম্ভিক খণ্ড’ express the OpenLogic sense(s) ‘preorder; partial order; linear order; total order; closure; initial segment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 70 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:200-222` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:187`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:41-48` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:39`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:180`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0147` `upstream/content/first-order-logic/introduction/models-theories.tex:32-54` → `bn-Beng-IN/content/first-order-logic/introduction/models-theories.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
A Kripke !!{structure}~$\mModel M = \tuple{W, R, V}$ for a propositional
language consists of a set~$W$, partial order~$R$ on~$W$ with a least
!!{element}, and an ``monotone'' assignment of propositional variables to
the !!{element}s of~$W$. The intuition is that the !!{element}s of $W$
represent ``worlds,'' or ``states of knowledge''; an element $v \geq
u$ represents a ``possible future state'' of~$u$; and the
propositional variables assigned to~$u$ are the propositions that are
known to be true in state~$u$. The forcing relation $\mSat{M}{!A}[w]$
then extends this relationship to arbitrary !!{formula}s in the
language; read $\mSat{M}{!A}[w]$ as ``$!A$ is true in state~$w$.'' The
relationship is defined inductively, as follows:
\begin{enumerate}
\item $\mSat{M}{\Obj p_i}[w]$ iff $\Obj p_i$ is one of the
  propositional variables assigned to~$w$.
\item $\mSat/{M}{\lfalse}[w]$.
\item $\mSat{M}{(!A \land !B)}[w]$ iff $\mSat{M}{!A}[w]$ and $\mSat{M}{!B}[w]$.
\item $\mSat{M}{(!A \lor !B)}[w]$ iff $\mSat{M}{!A}[w]$ or $\mSat{M}{!B}[w]$.
\item $\mSat{M}{(!A \lif !B)}[w]$ iff, whenever $w' \geq w$ and
  $\mSat{M}{!A}[w']$, then $\mSat{M}{!B}[w']$.
\end{enumerate}
It is a good exercise to try to show that $\lnot (p \land q) \lif
(\lnot p \lor \lnot q)$ is not intuitionistically valid, by cooking up a
Kripke !!{structure} that provides a counterexample.
```

### BN-IN-T030

- Source term or concept: graph; directed graph; vertex; edge; isolated vertex
- Chosen Bengali: গ্রাফ; নির্দেশিত গ্রাফ; শীর্ষ; প্রান্ত; বিচ্ছিন্ন শীর্ষ
- Rationale: Set/relation evidence supports encoding by ordered pairs. Graph terminology is provisionally normalized and is not claimed attested on these pages. Preserve vertex-set versus edge-relation distinction.
- Plausible alternatives: লেখ, দিকযুক্ত গ্রাফ, শীর্ষবিন্দু, ধার and নিঃসঙ্গ শীর্ষ are plausible alternatives; the selected graph loans and Bengali vertex/edge terms are definition-governed and avoid importing geometric meanings.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গ্রাফ; নির্দেশিত গ্রাফ; শীর্ষ; প্রান্ত; বিচ্ছিন্ন শীর্ষ’ express the OpenLogic sense(s) ‘graph; directed graph; vertex; edge; isolated vertex’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 27 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:188`; final reader page pending
  - `OLP-0067` `upstream/content/first-order-logic/proof-systems/tableaux.tex:15-29` → `bn-Beng-IN/content/first-order-logic/proof-systems/tableaux.tex:29`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:76-108` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:69`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:158-215` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:202`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:46-50` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:48`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In addition, one can define the class of well-orderings, by adding the
following to the definition of a linear ordering:
\[
\lforall[P][(\lexists[x][\Atom{P}{x}] \lif \lexists[x][(\Atom{P}{x}
    \land \lforall[y][(y < x \lif \lnot \Atom{P}{y})])])].
\]
This asserts that every non-empty set has a least element, modulo the
identification of ``set'' with ``one-place relation''. For another
example, one can express the notion of connectedness for graphs, by
saying that there is no nontrivial separation of the vertices into
disconnected parts:
\[
\lnot \lexists[A][(\lexists[x][A(x)] \land \lexists[y][\lnot A(y)]
  \land \lforall[w][\lforall[z][((\Atom{A}{w} \land \lnot \Atom{A}{z})
      \lif \lnot \Atom{R}{w,z})]])].
\]
For yet another example, you might try as an exercise to define the
class of finite !!{structure}s whose !!{domain} has even size. More
strikingly, one can provide a categorical description of the real
numbers as a complete ordered field containing the rationals.
```

### BN-IN-T031

- Source term or concept: tree; root; successor; predecessor; branch; chain; least element; well-order
- Chosen Bengali: বৃক্ষ; মূল; উত্তরসূরি; পূর্বসূরি; শাখা; শৃঙ্খল; ক্ষুদ্রতম উপাদান; সুক্রম
- Rationale: Set/relation/property and inclusion-proof pages support prose and concepts only. Tree terminology is a documented descriptive choice, not direct canon attestation. Immediate predecessor is distinguished from any smaller ancestor; maximal chain means maximal by inclusion, not largest cardinality.
- Plausible alternatives: ট্রি, রুট, সাকসেসর, প্রিডেসেসর and well-order loans are plausible alternatives; বৃক্ষ, মূল, উত্তরসূরি, পূর্বসূরি, শাখা, শৃঙ্খল and সুক্রম provide a consistent Bengali family governed by the order definitions.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বৃক্ষ; মূল; উত্তরসূরি; পূর্বসূরি; শাখা; শৃঙ্খল; ক্ষুদ্রতম উপাদান; সুক্রম’ express the OpenLogic sense(s) ‘tree; root; successor; predecessor; branch; chain; least element; well-order’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 373 occurrence(s). Representative locations:
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:9`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:10`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18-29` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:16`; final reader page pending
  - `OLP-0123` `upstream/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:16-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\iftag{FOL}
      {\olchapter{fol}{axd}{Axiomatic \usetoken{P}{derivation}}}
      {\olchapter{pl}{axd}{Axiomatic \usetoken{P}{derivation}}}
```

### BN-IN-T032

- Source term or concept: inverse relation; relative product; restriction; application; transitive closure
- Chosen Bengali: বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ
- Rationale: Existing university evidence attests pair/set operations and transitivity but not these exact operator names. Inverse swaps coordinates; relative-product direction follows source R then S. Restriction here cuts both coordinates to A; application is relational image, not necessarily a function.
- Plausible alternatives: উল্টো সম্পর্ক, সম্পর্ক-সংযোজন, সংকোচন, প্রতিবিম্ব and পরিযায়ী সংবরণ are plausible alternatives; the selected terms distinguish inversion, relative product, restriction, application and closure as separate operations.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ’ express the OpenLogic sense(s) ‘inverse relation; relative product; restriction; application; transitive closure’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 188 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:18-20` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:20`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:61-62` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:61`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:75-95` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:92`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:47-54` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:54`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:38-44` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:44`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
We again proceed by induction on the length
of the !!{derivation} of $!B$ from $\Gamma \cup \{!A\}$.
```

### BN-IN-T033

- Source term or concept: formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma
- Chosen Bengali: সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য
- Rationale: Early Trees mentions require these terms before their full chapters. Quantification/proposition and university mathematical prose provide context, not direct name attestation. Token IDs remain untouched; reader expansion uses these provisional terms. Later logic-specific canon may refine wording without changing formal definitions.
- Plausible alternatives: সুসম্বদ্ধ সূত্র, অবরোহ, প্রস্তাবনা যুক্তিবিদ্যা, প্রথম ঘাতের যুক্তিবিদ্যা, সম্পূর্ণতা and পরিগণনাযোগ্যতা are plausible alternatives; the selected vocabulary aligns with the project tokens and preserves syntactic, semantic and computational distinctions.
- Status: provisional-contextual; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য’ express the OpenLogic sense(s) ‘formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 283 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:71`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:20`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:23`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:26-30` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:29`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:15-17` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:16`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the induction basis, we prove the claim for every !!{derivation}
of length~$1$. !!^a{derivation} of~$!B$ from $\Gamma \cup \{!A\}$ of
length~$1$ consists of $!B$ by itself; and if it is correct $!B$ is
either $\in \Gamma \cup \{!A\}$ or is an axiom.  If $!B \in \Gamma$ or
is an axiom, then $\Gamma \Proves !B$. We also have that $\Gamma
\Proves !B \lif (!A \lif !B)$ by \olref[prp]{ax:lif1}, and
\olref{prop:mp} gives $\Gamma \Proves !A \lif !B$. If $!B \in \{ !A\}$
then $\Gamma \Proves !A \lif !B$ because the last !!{sentence}~$!A
\lif !B$ is the same as $!A \lif !A$, and we have !!{derive}d that in
\olref[pro]{ex:identity}.
```

### BN-IN-T034

- Source term or concept: variable; constant; sum; arithmetic product; equation
- Chosen Bengali: চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ
- Rationale: Freshly consulted recovered West Bengal and Tripura pages supplement university witnesses. Applies to arithmetic/algebra senses; does not claim logical term, model-theoretic constant or first-order formula attestation. New evidence is not retroactively attributed to earlier drafting.
- Plausible alternatives: চলরাশি and অচল are plausible alternatives for variable and constant; চল and ধ্রুবক follow the checked school algebra page, while যোগফল, গুণফল and সমীকরণ are directly supported there.
- Status: attested-in-school-algebra; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ’ express the OpenLogic sense(s) ‘variable; constant; sum; arithmetic product; equation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 235 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:40`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:75-95` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:78`; final reader page pending
  - `OLP-0123` `upstream/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:27-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:30`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:34-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:37`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:87-107` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:91`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the inductive step, suppose again that the !!{derivation} of $!B$
from $\Gamma \cup \{!A\}$ ends with a step~$!B$ which is justified by
an inference rule. If the inference rule is modus ponens, we proceed
as in the proof of \olref[ded]{thm:deduction-thm}. If the inference
rule is \QR, we know that $!B \ident !C \lif \lforall[x][!D(x)]$ and
!!a{formula} of the form $!C \lif !D(a)$ appears earlier in the
!!{derivation}, where $a$ does not occur in~$!C$, $!A$, or $\Gamma$. We
thus have that
\begin{align*}
  \Gamma \cup \{!A\} & \Proves !C \lif !D(a),\\
  \intertext{and the induction hypothesis applies, i.e., we have that}
    \Gamma & \Proves !A \lif (!C \lif !D(a)).\\
  \intertext{By}
  & \Proves (!A \lif (!C \lif !D(a))) \lif ((!A \land !C) \lif !D(a))\\
  \intertext{and modus ponens we get}
  \Gamma & \Proves (!A \land !C) \lif !D(a).\\
  \intertext{Since the eigenvariable condition still applies, we can add a step to this !!{derivation} justified by \QR, and get}
    \Gamma & \Proves (!A \land !C) \lif \lforall[x][!D(x)].\\
    \intertext{We also have}
    & \Proves ((!A \land !C) \lif \lforall[x][!D(x)]) \lif (!A \lif (!C \lif \lforall[x][!D(x)]),\\
    \intertext{so by modus ponens,}
    \Gamma & \Proves !A \lif (!C \lif \lforall[x][!D(x)]),
\end{align*}
i.e., $\Gamma \Proves !B$.
```

### BN-IN-T035

- Source term or concept: function; mapping; domain; codomain; range; image/value
- Chosen Bengali: অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান
- Rationale: NSOU PDF370 directly supplies the function definition and these roles. Codomain may strictly contain the range. প্রতিবিম্ব labels the mapped object and মান the function value; scope separates this from the reflexivity property.
- Plausible alternatives: ফলন, মানচিত্রণ, ক্ষেত্র, সহক্ষেত্র, মানসমষ্টি and চিত্র are plausible alternatives; অপেক্ষক and চিত্রণ follow the checked university source, and the selected domain/range family keeps each set role explicit.
- Status: attested-university; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান’ express the OpenLogic sense(s) ‘function; mapping; domain; codomain; range; image/value’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 713 occurrence(s). Representative locations:
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:36-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:38`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:23-30` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:26`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:23-30` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:29`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:26`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:27`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Modus ponens]
  If $!B$ and $!B \lif !A$ already occur in !!a{derivation}, then $!A$ is
  a correct inference step.
\end{defn}
```

### BN-IN-T036

- Source term or concept: function argument; input; output; black box; extensionality for functions
- Chosen Bengali: আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি
- Rationale: University mapping and freshly consulted recovered variable/equation prose support explanations. Input/output/argument are explicit provisional loans; function argument is not logical argument (যুক্তি). Function extensionality requires same domain/codomain and equal values at every argument; equation-operation evidence is prose support only.
- Plausible alternatives: পরামিতি, নিবেশ, নির্গম, অস্বচ্ছ বাক্স and বহির্বিস্তার নীতি are plausible Bengali alternatives; the selected loans are familiar in technical prose, while মানভিত্তিক সমতার নীতি states the governing extensional condition.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি’ express the OpenLogic sense(s) ‘function argument; input; output; black box; extensionality for functions’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 27 occurrence(s). Representative locations:
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:19-26` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:23`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:28-42` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:33`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:28-42` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:34`; final reader page pending
  - `OLP-0076` `upstream/content/first-order-logic/sequent-calculus/proving-things-quant.tex:31-83` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things-quant.tex:58`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:12-31` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:15`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Many-sorted logic provides this kind of framework. One starts with a
list of ``sorts''---the ``sort'' of an object indicates the
``!!{domain}'' it is supposed to inhabit. One then has !!{variable}s
and quantifiers for each sort, and (usually) an !!{identity} for each
sort. Functions and relations are also ``typed'' by the sorts of
objects they can take as arguments. Otherwise, one keeps the usual
rules of first-order logic, with versions of the quantifier-rules
repeated for each sort.
```

### BN-IN-T037

- Source term or concept: injective/injection; surjective/surjection; bijective/bijection; identity function
- Chosen Bengali: একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক
- Rationale: NSOU directly attests একৈক, সমাপতিত, সমরূপ and অভেদ চিত্রণ. Prefer its explicit compound একৈক সমাপতিত for bijective to keep সমরূপ available for later isomorphism distinctions. Replace mapping noun with the already attested অপেক্ষক when translating function; noun/adjective token variants remain separate. Earlier identity-function prose will be harmonized at reader integration.
- Plausible alternatives: সমরূপ চিত্রণ is directly printed for bijective; একৈক সমাপতিত selected to avoid collision with later isomorphism.
- Status: attested-university-with-normalization; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক’ express the OpenLogic sense(s) ‘injective/injection; surjective/surjection; bijective/bijection; identity function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 21 occurrence(s). Representative locations:
  - `OLP-0022` `upstream/content/sets-functions-relations/functions/function-kinds.tex:80-81` → `bn-Beng-IN/content/sets-functions-relations/functions/function-kinds.tex:58`; final reader page pending
  - `OLP-0026` `upstream/content/sets-functions-relations/functions/partial-functions.tex:42-48` → `bn-Beng-IN/content/sets-functions-relations/functions/partial-functions.tex:32`; final reader page pending
  - `OLP-0054` `upstream/content/sets-functions-relations/infinite/card-sb.tex:89-101` → `bn-Beng-IN/content/sets-functions-relations/infinite/card-sb.tex:68`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:102-107` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:80`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:112-113` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:88`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The identity function $f\colon \Nat \to \Nat$ given by $f(x) = x$ is
both !!{injective} and !!{surjective}.
```

### BN-IN-T038

- Source term or concept: inverse function; left inverse; right inverse; composition
- Chosen Bengali: বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ
- Rationale: বিপরীত চিত্রণ and মিশ্র চিত্রণ are directly attested. মিশ্রণ is the normalized operation noun; left/right inverse compounds are provisional and defined by their respective equations. Composition applies f before g; no attestation of arbitrary choice or empty-domain claims is inferred.
- Plausible alternatives: ব্যস্ত অপেক্ষক, বাঁ/ডান ব্যস্ত and যৌগ are plausible alternatives; বিপরীত অপেক্ষক, বাম/ডান বিপরীত and মিশ্রণ follow the checked inverse/composition roots and retain the order fixed by the formulas.
- Status: attested-root-with-provisional-normalization; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ’ express the OpenLogic sense(s) ‘inverse function; left inverse; right inverse; composition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
  - `OLP-0187` `upstream/content/model-theory/basics/isomorphism.tex:67-106` → `bn-Beng-IN/content/model-theory/basics/isomorphism.tex:66`; final reader page pending
  - `OLP-0025` `upstream/content/sets-functions-relations/functions/composition.tex:9-10` → `bn-Beng-IN/content/sets-functions-relations/functions/composition.tex:10`; final reader page pending
  - `OLP-0025` `upstream/content/sets-functions-relations/functions/composition.tex:12-21` → `bn-Beng-IN/content/sets-functions-relations/functions/composition.tex:13`; final reader page pending
  - `OLP-0025` `upstream/content/sets-functions-relations/functions/composition.tex:23-37` → `bn-Beng-IN/content/sets-functions-relations/functions/composition.tex:15`; final reader page pending
  - `OLP-0025` `upstream/content/sets-functions-relations/functions/composition.tex:23-37` → `bn-Beng-IN/content/sets-functions-relations/functions/composition.tex:20`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
Let $h$ be an isomorphism of $\Struct{M}$ onto $\Struct M'$. For any
assignment~$s$, $h \circ s$ is the composition of $h$ and $s$, i.e.,
the assignment in $\Struct{M'}$ such that $(h \circ s)(x) = h(s(x))$.
By induction on $t$ and $!A$ one can prove the stronger claims:
\begin{enumerate}
  \item[a.] $h(\Value{t}{M}[s]) = \Value{t}{M'}[h\circ s]$.
  \item[b.] $\Sat{M}{!A}[s]$ iff $\Sat{M'}{!A}[h \circ s]$.
\end{enumerate}
The first is proved by induction on the complexity of~$t$.
\begin{enumerate}
\item If $t \ident c$, then $\Value{c}{M}[s] = \Assign{c}{M}$ and
  $\Value{c}{M'}[h \circ s] = \Assign{c}{M'}$. Thus,
  $h(\Value{t}{M}[s]) = h(\Assign{c}{M}) = \Assign{c}{M'}$ (by
  \olref{defn:iso-const} of \olref{defn:isomorphism}) $=
  \Value{t}{M'}[h \circ s]$.
\item If $t \ident x$, then $\Value{x}{M}[s] = s(x)$ and
  $\Value{x}{M'}[h \circ s] = h(s(x))$. Thus, $h(\Value{x}{M}[s]) =
  h(s(x)) = \Value{x}{M'}[h \circ s]$.
\item If $t \ident f(t_1, \dots, t_n)$, then
  \begin{align*}
    \Value{t}{M}[s] & = \Assign{f}{M}(\Value{t_1}{M}[s], \dots, \Value{t_n}{M}[s]) \quad\text{and}\\
  \Value{t}{M'}[h \circ s] & = \Assign{f}{M}(\Value{t_1}{M'}[h \circ
    s], \dots, \Value{t_n}{M'}[h \circ s]).
  \end{align*}
  The induction hypothesis is that for each $i$, $h(\Value{t_i}{M}[s])
  = \Value{t_i}{M'}[h\circ s]$. So,
  \begin{align}
    h(\Value{t}{M}[s])
    & = h(\Assign{f}{M}(\Value{t_1}{M}[s], \dots, \Value{t_n}{M}[s]) \notag\\
    & = \Assign{f}{M'}(h(\Value{t_1}{M}[s]), \dots,
    h(\Value{t_n}{M}[s])) \ollabel{iso-1}\\
    & = \Assign{f}{M'}(\Value{t_1}{M'}[h \circ s], \dots,
    \Value{t_n}{M'}[h \circ s]) \ollabel{iso-2}\\
    & = \Value{t}{M'}[h\circ s] \notag
  \end{align}
  Here, \olref{iso-1} follows by \olref{defn:iso-func} of
  \olref{defn:isomorphism} and \olref{iso-2} by induction hypothesis.
\end{enumerate}
Part (b) is left as an exercise.
```

### BN-IN-T039

- Source term or concept: partial function; total function; functional relation; serial relation; Axiom of Choice
- Chosen Bengali: আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ
- Rationale: University relations and total mappings support concept and proof prose, not direct attestation of these extensions. Serial is a provisional loan immediately defined by existence of an output for each input. Partial means at most one output; total means exactly one for every input in the specified ambient set. Choice and one-sided inverse hypotheses remain those in OpenLogic, with separate source notes for defects.
- Plausible alternatives: পূর্ণ অপেক্ষক versus সর্বত্র সংজ্ঞায়িত অপেক্ষক; the descriptive form exposes totality and avoids collision with completeness/full order.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ’ express the OpenLogic sense(s) ‘partial function; total function; functional relation; serial relation; Axiom of Choice’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 14 occurrence(s). Representative locations:
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:13-29` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:16`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:73-90` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:72`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:12-31` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:15`; final reader page pending
  - `OLP-0024` `upstream/content/sets-functions-relations/functions/inverses.tex:97-114` → `bn-Beng-IN/content/sets-functions-relations/functions/inverses.tex:71`; final reader page pending
  - `OLP-0026` `upstream/content/sets-functions-relations/functions/partial-functions.tex:12-12` → `bn-Beng-IN/content/sets-functions-relations/functions/partial-functions.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Almost all of mathematics can be developed in the theory of sets.
Developing mathematics in this theory involves a number of things.
First, it requires a set of axioms for the relation~$\in$.  A number
of different axiom systems have been developed, sometimes with
conflicting properties of~$\in$.  The axiom system known as
$\Log{ZFC}$, Zermelo--Fraenkel set theory with the axiom of choice
stands out: it is by far the most widely used and studied, because it
turns out that its axioms suffice to prove almost all the things
mathematicians expect to be able to prove.  But before that can be
established, it first is necessary to make clear how we can even
\emph{express} all the things mathematicians would like to express.
For starters, the language contains no !!{constant}s or !!{function}s,
so it seems at first glance unclear that we can talk about particular
sets (such as $\emptyset$ or $\Nat$), can talk about operations on
sets (such as $X \cup Y$ and $\Pow{X}$), let alone other
constructions which involve things other than sets, such as relations
and functions.
```

### BN-IN-T040

- Source term or concept: size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable
- Chosen Bengali: সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয়
- Rationale: NSOU directly attests finite/infinite sets and finite cardinality's মাত্রা/অঙ্কবাচক সংখ্যা. সেটের আকার is a descriptive chapter title, not geometric shape or dimension. Enumeration/listability and countability terms remain provisional: the elementary and abstract source sections give different definitions, so their own finite/empty-set conventions govern. No computable-enumerability meaning is imported. Infinite cardinality and actual infinity are not directly attested on these pages.
- Plausible alternatives: গণনীয় versus তালিকায়নযোগ্য; elementary enumeration sections use তালিকায়নযোগ্য, while গণনীয় is reserved as a possible later countability/computability-sensitive term.
- Status: mixed-attested-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয়’ express the OpenLogic sense(s) ‘size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 322 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:119`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:121`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:127`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:27`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}[Compactness]
\ollabel{prop:proves-compact}
  \begin{enumerate}
  \item If $\Gamma \Proves !A$ then there is a finite subset $\Gamma_0
    \subseteq \Gamma$ such that $\Gamma_0 \Proves !A$.
  \item If every finite subset of~$\Gamma$ is
    consistent, then $\Gamma$ is consistent.
  \end{enumerate}
\end{prop}
```

### BN-IN-T041

- Source term or concept: actual infinity
- Chosen Bengali: বাস্তবায়িত অসীম
- Rationale: The introductory historical phrase means an infinite collection treated as an existing completed whole, rather than merely an indefinitely extendable process. The consulted philosophical and mathematical pages support Bengali exposition but do not directly attest this technical phrase; no such attestation is claimed. It is distinct from the set of real numbers and from finite cardinality.
- Plausible alternatives: প্রকৃত অসীম is a plausible philosophical alternative; বাস্তবায়িত অসীম avoids possible confusion with the real-number continuum and marks infinity treated as a completed totality.
- Status: provisional-philosophical; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বাস্তবায়িত অসীম’ express the OpenLogic sense(s) ‘actual infinity’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0028` `upstream/content/sets-functions-relations/size-of-sets/introduction.tex:13-19` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/introduction.tex:13`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
When Georg Cantor developed set theory in the 1870s, one of his aims
was to make palatable the idea of an infinite collection---an actual
infinity, as the medievals would say.  A key part of this was his
treatment of the \emph{size} of different sets. If $a$, $b$ and $c$ are
all distinct, then the set $\{a, b, c\}$ is intuitively \emph{larger}
than $\{a, b\}$. But what about infinite sets? Are they all as large
as each other? It turns out that they are not.
```

### BN-IN-T042

- Source term or concept: ceiling function; induction; recursive definition; corollary
- Chosen Bengali: ঊর্ধ্ব পূর্ণাংশ অপেক্ষক; গাণিতিক আরোহ; পূর্ববর্তী মানের সাহায্যে ধাপে ধাপে সংজ্ঞা; অনুসিদ্ধান্ত
- Rationale: Enumeration section needs these concepts before their dedicated development. Consulted university mapping, proof and finite-set prose supports exposition but does not directly attest the names. Ceiling is explicitly explained as rounding upward to the nearest integer. Recursive construction is described through earlier values; no assertion of an effective algorithm or computable enumeration is introduced.
- Plausible alternatives: সিলিং অপেক্ষক, গাণিতিক আরোহন, পুনরাবৃত্ত সংজ্ঞা and ফলিত are plausible alternatives; the selected wording makes upward rounding and dependence on earlier stages explicit where direct term attestation is absent.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ঊর্ধ্ব পূর্ণাংশ অপেক্ষক; গাণিতিক আরোহ; পূর্ববর্তী মানের সাহায্যে ধাপে ধাপে সংজ্ঞা; অনুসিদ্ধান্ত’ express the OpenLogic sense(s) ‘ceiling function; induction; recursive definition; corollary’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 31 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:17`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:24`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:23`; final reader page pending
  - `OLP-0127` `upstream/content/first-order-logic/completeness/introduction.tex:15-22` → `bn-Beng-IN/content/first-order-logic/completeness/introduction.tex:17`; final reader page pending
  - `OLP-0127` `upstream/content/first-order-logic/completeness/introduction.tex:24-47` → `bn-Beng-IN/content/first-order-logic/completeness/introduction.tex:37`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
Just as we've defined a number of important semantic notions
(\iftag{FOL}{validity}{tautology}, entailment, satisfiability), we now
define corresponding \emph{proof-theoretic notions}.  These are not
defined by appeal to satisfaction of !!{sentence}s in !!{structure}s,
but by appeal to the !!{derivability} or !!{nonderivability} of
certain formulas.  It was an important discovery that these notions
coincide.  That they do is the content of the \emph{soundness} and
\emph{completeness theorems}.
\end{explain}
```

### BN-IN-T043

- Source term or concept: zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function
- Chosen Bengali: আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক
- Rationale: Freshly reread university ordered-pair/product/complement summary and recovered West Bengal algebraic operations/factorization page before these drafts. They attest underlying pair/product and arithmetic prose, not the specialized coding or Cantor names. Pairing means an injective numerical encoding; its inverse can be partial. Cofinite is immediately defined by a finite complement in the naturals. Truth function is explicitly distinguished from a propositional function; no direct name attestation is claimed.
- Plausible alternatives: জোড়া-লাগানো অপেক্ষক / pairing-function loan; যুগলায়ন selected as a concise provisional compound.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক’ express the OpenLogic sense(s) ‘zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 158 occurrence(s). Representative locations:
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:41-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:50`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:30-65` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:40`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:129-167` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:135`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:226-234` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:226`; final reader page pending
  - `OLP-0128` `upstream/content/first-order-logic/completeness/outline.tex:34-47` → `bn-Beng-IN/content/first-order-logic/completeness/outline.tex:41`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
\iftag{FOL}{We have to verify that all the axioms are valid. For
  instance, here is the case for \olref[qua]{ax:q1}: suppose $t$ is
  !!{free for} $x$ in $!A$, and assume
  $\Sat{M}{\lforall[x][!A]}[s]$. Then by definition of satisfaction,
  for each $\varAssign{s'}{s}{x}$, also $\Sat{M}{!A}[s']$, and in particular
  this holds when $s'(x) = \Value{t}{M}[s]$. By
  \olref[syn][ext]{prop:ext-formulas},
  $\Sat{M}{\Subst{!A}{t}{x}}[s]$. This shows that
  $\Sat{M}{(\lforall[x][!A] \lif \Subst{!A}{t}{x})}[s]$.}{Do truth
  tables for each axiom to verify that they are tautologies.}
\end{proof}
```

### BN-IN-T044

- Source term or concept: non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence
- Chosen Bengali: অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম
- Rationale: Checked university set, quantification, proof-prose and finite/infinite pages do not directly attest Cantor's diagonal terminology. অতালিকায়নযোগ্য mirrors the elementary source definition by absence of an enumeration; অগণনীয় is reserved as a conventional alternative. কর্ণ is the matrix diagonal, not an anatomical claim. The constructed binary sequence flips each diagonal bit, so the descriptive phrase avoids suggesting geometric reflection. Source formulas and universal counter-list argument determine the meaning.
- Plausible alternatives: অগণনযোগ্য, কর্ণীয় পদ্ধতি, কর্ণায়ন, একমুখী অসীম তালিকা and পরিপূরক-বিট অনুক্রম are plausible alternatives; the selected terms remain tied to absence of enumeration and the explicit diagonal bit flip.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম’ express the OpenLogic sense(s) ‘non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0039` `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:13-18` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:14`; final reader page pending
  - `OLP-0039` `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:33-41` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:25`; final reader page pending
  - `OLP-0039` `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:105-111` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:68`; final reader page pending
  - `OLP-0033` `upstream/content/sets-functions-relations/size-of-sets/non-enumerability.tex:13-18` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/non-enumerability.tex:14`; final reader page pending
  - `OLP-0033` `upstream/content/sets-functions-relations/size-of-sets/non-enumerability.tex:33-41` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/non-enumerability.tex:21`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{editorial}
  This section proves the non-enumerability of $\Bin^\omega$ and
  $\Pow{\Nat}$ using the definitions in \olref[enm-alt]{sec}, i.e.,
  requiring a bijection with~$\Nat$ instead of a surjection from
  $\PosInt$.
\end{editorial}
```

### BN-IN-T045

- Source term or concept: reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction
- Chosen Bengali: হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ
- Rationale: Checked logic, set and function sources support implication and mapping prose but do not directly attest problem reduction or characteristic sequences. হ্রাসকরণ means transforming a presumed enumeration of A into one of B; it is not subtraction, quotienting or proof simplification. The surjection must run from A to B for the contradiction used here. The binary sequence is the membership indicator of a subset of positive integers.
- Plausible alternatives: রিডাকশন, চরিত্রাঙ্ক অনুক্রম, নিঃশেষে তালিকাভুক্ত করা and হ্রাসের দিক are plausible alternatives; the selected wording exposes the transformation and its source-to-target orientation.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ’ express the OpenLogic sense(s) ‘reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 13 occurrence(s). Representative locations:
  - `OLP-0040` `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:11-11` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/reduction-alt.tex:11`; final reader page pending
  - `OLP-0040` `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:13-18` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/reduction-alt.tex:14`; final reader page pending
  - `OLP-0040` `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:48-50` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/reduction-alt.tex:28`; final reader page pending
  - `OLP-0040` `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:48-50` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/reduction-alt.tex:29`; final reader page pending
  - `OLP-0040` `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:106-110` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/reduction-alt.tex:67`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Reduction}
```

### BN-IN-T046

- Source term or concept: equinumerous/equinumerosity; same cardinality; cardinal equality
- Chosen Bengali: সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা
- Rationale: NSOU directly attests finite cardinality as setের মাত্রা/অঙ্কবাচক সংখ্যা and equivalence-relation proof vocabulary, but not infinite equinumerosity. সমসংখ্যকতা is selected as a transparent property name defined by existence of a bijection. মাত্রাসমতা is recorded as a notation-oriented alternative but could suggest geometric dimension. The relation is proved reflexive, symmetric and transitive using identity, inverse and composition.
- Plausible alternatives: সমানসংখ্যক, সমঅঙ্কবাচক and কার্ডিনাল সমতা are plausible alternatives; সমসংখ্যকতা and মাত্রাসমতা remain explicitly defined by existence of a bijection.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা’ express the OpenLogic sense(s) ‘equinumerous/equinumerosity; same cardinality; cardinal equality’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:13-24` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:14`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11-11` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:29-32` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:20`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:34-36` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:24`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:38-40` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:28`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
We have offered a precise statement of the idea that two sets have the
same size. We can also offer a precise statement of the idea that one
set is smaller than another. Our definition of ``is smaller than (or
equinumerous)'' will require, instead of !!a{bijection} between the
sets, !!a{injection} from the first set to the second. If such a
function exists, the size of the first set is less than or equal to
the size of the second. Intuitively, !!a{injection} from one set to
another guarantees that the range of the function has at least as many
!!{element}s as the domain, since no two !!{element}s of the domain
map to the same !!{element} of the range.
\end{explain}
```

### BN-IN-T047

- Source term or concept: no larger than; strictly smaller cardinality; cardinal comparison; Cantor's theorem; Schröder–Bernstein theorem
- Chosen Bengali: আকারে বড় নয়; আকারে ছোট; অঙ্কবাচকতার তুলনা; কান্টরের উপপাদ্য; শ্র্যোডার–বার্নস্টাইন উপপাদ্য
- Rationale: Finite-cardinality and equivalence proof pages support comparison prose but do not directly attest transfinite cardinal inequalities or theorem names. The relation A no larger than B is defined by an injection A to B; strict comparison additionally denies a bijection. Proper names are transliterated while original Latin spelling remains in TeX controls/citations. Schröder–Bernstein converts injections in both directions into a bijection; no proof is silently supplied where the source postpones it.
- Plausible alternatives: অঙ্কবাচকভাবে বড় নয়, যথার্থভাবে ক্ষুদ্রতর and cardinal-order loans are plausible alternatives; the selected comparison phrases remain governed by injections and absence of bijections.
- Status: mixed-normalized-and-proper-name; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আকারে বড় নয়; আকারে ছোট; অঙ্কবাচকতার তুলনা; কান্টরের উপপাদ্য; শ্র্যোডার–বার্নস্টাইন উপপাদ্য’ express the OpenLogic sense(s) ‘no larger than; strictly smaller cardinality; cardinal comparison; Cantor's theorem; Schröder–Bernstein theorem’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:11-11` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:11`; final reader page pending
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:13-24` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:14`; final reader page pending
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:26-29` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:18`; final reader page pending
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:36-40` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:24`; final reader page pending
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:137-140` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:77`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Sets of Different Sizes, and Cantor's Theorem}
```

### BN-IN-T048

- Source term or concept: integer; positive/negative integer; natural number represented as an integer; equivalence-class representative
- Chosen Bengali: পূর্ণসংখ্যা; ধনাত্মক/ঋণাত্মক পূর্ণসংখ্যা; স্বাভাবিক সংখ্যার পূর্ণসংখ্যা-রূপ; তুল্যতা শ্রেণির প্রতিনিধি
- Rationale: NSOU directly lists পূর্ণ বা অখণ্ড সংখ্যা and its positive/negative subsets; the edition standardizes the compact form পূর্ণসংখ্যা. NSOU also directly attests তুল্যতা শ্রেণী, normalized here to modern শ্রেণি. The constructed integer n_Int is the equivalence class of (n,0); calling it a natural number's integer form describes the embedding and does not assert literal identity between the set-theoretic constructions.
- Plausible alternatives: অখণ্ড সংখ্যা is a directly witnessed alternative to পূর্ণসংখ্যা; প্রতিনিধি পদ and প্রোথিত রূপ are plausible alternatives for representative and embedding, while the selected wording makes each constructed number-system level explicit.
- Status: mixed-direct-and-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পূর্ণসংখ্যা; ধনাত্মক/ঋণাত্মক পূর্ণসংখ্যা; স্বাভাবিক সংখ্যার পূর্ণসংখ্যা-রূপ; তুল্যতা শ্রেণির প্রতিনিধি’ express the OpenLogic sense(s) ‘integer; positive/negative integer; natural number represented as an integer; equivalence-class representative’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 66 occurrence(s). Representative locations:
  - `OLP-0161` `upstream/content/first-order-logic/syntax-and-semantics/structures.tex:67-73` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/structures.tex:69`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:75-87` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:44`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:109-125` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:57`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:149-163` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:80`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:149-163` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:84`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
However, there are many other possible !!{structure}s for~$\Lang
L_A$. For instance, we might take as the domain the set~$\Int$ of
integers instead of~$\Nat$, and define the interpretations of $\Obj
0$, $\Obj \prime$, $\Obj +$, $\Obj \times$, $\Obj <$ accordingly.  But
we can also define structures for~$\Lang L_A$ which have nothing even
remotely to do with numbers.
\end{ex}
```

### BN-IN-T049

- Source term or concept: arithmetization as set-theoretic construction of number systems; induced arithmetic operations; well-defined on equivalence classes
- Chosen Bengali: সেটতাত্ত্বিক সংখ্যা-নির্মাণ; তুল্যতা শ্রেণির উপর গাণিতিক ক্রিয়া; প্রতিনিধিনিরপেক্ষভাবে সুসংজ্ঞায়িত
- Rationale: The chapter constructs integers, rationals and reals inside naive set theory; সেটতাত্ত্বিক সংখ্যা-নির্মাণ exposes that sense and avoids collision with Gödel-style arithmetization. Checked pages attest ordered pairs, equivalence classes, operations and proof prose, but not this chapter title or the technical well-definedness phrase. Representatives may vary while the induced class result must remain unchanged; the later OpenLogic checking-details section governs the proof.
- Plausible alternatives: পাটীগণিতায়ন, শ্রেণিতে প্রবর্তিত ক্রিয়া and প্রতিনিধিস্বাধীন সুসংজ্ঞা are plausible alternatives; সেটতাত্ত্বিক সংখ্যা-নির্মাণ avoids confusion with Gödel-style arithmetization and states the construction performed here.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সেটতাত্ত্বিক সংখ্যা-নির্মাণ; তুল্যতা শ্রেণির উপর গাণিতিক ক্রিয়া; প্রতিনিধিনিরপেক্ষভাবে সুসংজ্ঞায়িত’ express the OpenLogic sense(s) ‘arithmetization as set-theoretic construction of number systems; induced arithmetic operations; well-defined on equivalence classes’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0041` `upstream/content/sets-functions-relations/arithmetization/arithmetization.tex:8-8` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/arithmetization.tex:8`; final reader page pending
  - `OLP-0046` `upstream/content/sets-functions-relations/arithmetization/reflections.tex:36-60` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/reflections.tex:20`; final reader page pending
  - `OLP-0046` `upstream/content/sets-functions-relations/arithmetization/reflections.tex:99-102` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/reflections.tex:42`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olchapter{sfr}{arith}{Arithmetization}
```

### BN-IN-T050

- Source term or concept: rational number; nonzero denominator; rational representative/embedding; cross multiplication
- Chosen Bengali: মূলদ সংখ্যা; অশূন্য হর; মূলদ-প্রতিনিধি/পূর্ণসংখ্যার মূলদ-রূপ; আড়গুণ
- Rationale: NSOU directly lists মূলদ সংখ্যা; ordered-pair, equivalence-class and arithmetic pages support the construction prose. অশূন্য হর and আড়গুণ are conventional descriptive compounds but were not directly found on the checked pages. A rational is an equivalence class of integer pairs with nonzero second coordinate, and i_Rat names the class of (i,1_Int); the wording does not identify the earlier integer construction literally with that class.
- Plausible alternatives: পরিমেয় সংখ্যা, শূন্য নয় এমন হর, মূলদ প্রোথিতকরণ and তির্যক গুণ are plausible alternatives; মূলদ সংখ্যা is directly attested and the selected compounds expose the pair/class construction.
- Status: mixed-direct-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মূলদ সংখ্যা; অশূন্য হর; মূলদ-প্রতিনিধি/পূর্ণসংখ্যার মূলদ-রূপ; আড়গুণ’ express the OpenLogic sense(s) ‘rational number; nonzero denominator; rational representative/embedding; cross multiplication’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 41 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:37-43` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:34`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:45-47` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:39`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:123-154` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:125`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:68-83` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:72`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To take another, perhaps less contrived example, consider the
following question. We know that it is possible to raise an irrational
number to a rational power, and get a rational result. For example,
$\sqrt{2}^2 = 2$. What is less clear is whether or not it is possible
to raise an irrational number to an \emph{irrational} power, and get a
rational result. The following theorem answers this in the
affirmative:
```

### BN-IN-T051

- Source term or concept: real line; irrational number; ordered field; Completeness Property; upper bound; least upper bound
- Chosen Bengali: বাস্তব সংখ্যারেখা; অমূলদ সংখ্যা; ক্রমিত ক্ষেত্র; পূর্ণতা ধর্ম; ঊর্ধ্বসীমা; লঘিষ্ঠ ঊর্ধ্বসীমা
- Rationale: NSOU directly lists বাস্তব and অমূলদ number systems, while checked proof and order pages support exposition. The compounds for ordered field, completeness and least upper bound remain provisional because the exact technical phrases were not found on the checked pages. Completeness here says every nonempty bounded-above real set has a least upper bound; it is distinct from metric/Cauchy completeness, which the chapter treats later.
- Plausible alternatives: বাস্তবরেখা, সুশৃঙ্খল ক্ষেত্র, সম্পূর্ণতা বৈশিষ্ট্য and সর্বনিম্ন ঊর্ধ্বসীমা are plausible alternatives; the selected forms remain governed by the ordered-field and least-upper-bound definitions.
- Status: mixed-direct-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বাস্তব সংখ্যারেখা; অমূলদ সংখ্যা; ক্রমিত ক্ষেত্র; পূর্ণতা ধর্ম; ঊর্ধ্বসীমা; লঘিষ্ঠ ঊর্ধ্বসীমা’ express the OpenLogic sense(s) ‘real line; irrational number; ordered field; Completeness Property; upper bound; least upper bound’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 32 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:37-43` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:34`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:45-47` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:39`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:21-36` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:16`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:169-171` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:100`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To take another, perhaps less contrived example, consider the
following question. We know that it is possible to raise an irrational
number to a rational power, and get a rational result. For example,
$\sqrt{2}^2 = 2$. What is less clear is whether or not it is possible
to raise an irrational number to an \emph{irrational} power, and get a
rational result. The following theorem answers this in the
affirmative:
```

### BN-IN-T052

- Source term or concept: Dedekind cut; lower half; proper initial segment; greatest lower bound; maximum element; rational-to-real embedding
- Chosen Bengali: ডেডেকিন্ড কর্তন; নিম্নাংশ; প্রকৃত প্রারম্ভিক খণ্ড; গরিষ্ঠ নিম্নসীমা; গরিষ্ঠ উপাদান; মূলদ সংখ্যার বাস্তব-রূপ
- Rationale: The checked pages support real/rational, partition, class and order prose but do not directly attest Dedekind-cut terminology. কর্তন is chosen over ছেদ so the construction is not confused with set intersection. A cut is explicitly nonempty, proper, downward closed and has no greatest element. The embedded rational p is the lower cut of rationals below p, not literal identity with the prior rational object.
- Plausible alternatives: ডেডেকিন্ড ছেদ, অধঃখণ্ড, যথার্থ আদি খণ্ড, বৃহত্তম নিম্নসীমা and সর্বাধিক উপাদান are plausible alternatives; কর্তন avoids collision with set intersection and the selected bound terms follow the edition’s order vocabulary.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ডেডেকিন্ড কর্তন; নিম্নাংশ; প্রকৃত প্রারম্ভিক খণ্ড; গরিষ্ঠ নিম্নসীমা; গরিষ্ঠ উপাদান; মূলদ সংখ্যার বাস্তব-রূপ’ express the OpenLogic sense(s) ‘Dedekind cut; lower half; proper initial segment; greatest lower bound; maximum element; rational-to-real embedding’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:50-52` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:51`; final reader page pending
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:81-88` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:88`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:13-19` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:13`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:158-168` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:124`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:184-205` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:138`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop} \ollabel{prop:noinit}
No proper initial segment of !!a{formula} is !!a{formula}.
\end{prop}
```

### BN-IN-T053

- Source term or concept: commutative ring; ordered ring; ordered field; associative/commutative/identity/additive inverse/distributive laws; trichotomy
- Chosen Bengali: বিনিমেয় বলয়; ক্রমিত বলয়; ক্রমিত ক্ষেত্র; সংযোগী/বিনিময়/অভেদী/যোগাত্মক বিপরীত/বণ্টন ধর্ম; ত্রিবিভাজন
- Rationale: Checked algebra, order and proof pages support the formulas and explanatory style, but the exact abstract-algebra compounds were not found. The displayed axioms govern each term. The field convention includes 0 not equal to 1; BN-SRC-011 supplies the condition omitted by the frozen source so the zero ring is not misclassified as a field.
- Plausible alternatives: আদানপ্রদানীয় বলয়, সম্বন্ধী ধর্ম, একক ধর্ম and ত্রৈধনীতি are plausible alternatives; the selected algebraic terms remain tied to the displayed axiom clauses and avoid ordinary-language ambiguity.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিনিমেয় বলয়; ক্রমিত বলয়; ক্রমিত ক্ষেত্র; সংযোগী/বিনিময়/অভেদী/যোগাত্মক বিপরীত/বণ্টন ধর্ম; ত্রিবিভাজন’ express the OpenLogic sense(s) ‘commutative ring; ordered ring; ordered field; associative/commutative/identity/additive inverse/distributive laws; trichotomy’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 25 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:158-215` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:172`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:169-171` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:100`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:10-11` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:11`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:18-21` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:15`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In addition, one can define the class of well-orderings, by adding the
following to the definition of a linear ordering:
\[
\lforall[P][(\lexists[x][\Atom{P}{x}] \lif \lexists[x][(\Atom{P}{x}
    \land \lforall[y][(y < x \lif \lnot \Atom{P}{y})])])].
\]
This asserts that every non-empty set has a least element, modulo the
identification of ``set'' with ``one-place relation''. For another
example, one can express the notion of connectedness for graphs, by
saying that there is no nontrivial separation of the vertices into
disconnected parts:
\[
\lnot \lexists[A][(\lexists[x][A(x)] \land \lexists[y][\lnot A(y)]
  \land \lforall[w][\lforall[z][((\Atom{A}{w} \land \lnot \Atom{A}{z})
      \lif \lnot \Atom{R}{w,z})]])].
\]
For yet another example, you might try as an exercise to define the
class of finite !!{structure}s whose !!{domain} has even size. More
strikingly, one can provide a categorical description of the real
numbers as a complete ordered field containing the rationals.
```

### BN-IN-T054

- Source term or concept: Cauchy sequence; rational approximation; tends to zero; equivalence modulo null sequences; constant-sequence embedding; monotone increasing/decreasing
- Chosen Bengali: কোশি অনুক্রম; মূলদ আসন্নমান; সীমায় শূন্যের দিকে যায়; শূন্যমুখী অনুক্রমের মডুলো তুল্যতা; ধ্রুব অনুক্রমে অন্তর্ভুক্তি; একঘেয়ে বর্ধমান/হ্রাসমান
- Rationale: No checked page directly attests Cauchy-sequence or analytic-limit terminology. The definition quantifies only over positive rationals to avoid presupposing the reals being constructed. Two sequences represent the same real exactly when their difference tends to zero; operations and order live on equivalence classes and must be independent of representatives.
- Plausible alternatives: কশি অনুক্রম, মূলদ সন্নিকর্ষ, শূন্যাভিমুখী অনুক্রমে তুল্যতা, ধ্রুব-অনুক্রম প্রোথিতকরণ and একঘাত বর্ধমান/হ্রাসমান are plausible alternatives; the selected forms spell out the quotient and limiting behavior.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কোশি অনুক্রম; মূলদ আসন্নমান; সীমায় শূন্যের দিকে যায়; শূন্যমুখী অনুক্রমের মডুলো তুল্যতা; ধ্রুব অনুক্রমে অন্তর্ভুক্তি; একঘেয়ে বর্ধমান/হ্রাসমান’ express the OpenLogic sense(s) ‘Cauchy sequence; rational approximation; tends to zero; equivalence modulo null sequences; constant-sequence embedding; monotone increasing/decreasing’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 16 occurrence(s). Representative locations:
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:11-11` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:11`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:13-19` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:13`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:38-73` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:23`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:75-87` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:44`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:97-107` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:51`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Appendix: the Reals as Cauchy Sequences}
```

### BN-IN-T055

- Source term or concept: rigour of a construction; metaphysical identification; set-theoretic embedding; rival constructions; Benacerraf-style underdetermination
- Chosen Bengali: নির্মাণের কঠোরতা; অধিবিদ্যাগত অভিন্নকরণ; সেটতাত্ত্বিক অন্তর্ভুক্তি; প্রতিদ্বন্দ্বী নির্মাণ; বেনাসেরাফ-ধর্মী অনির্ধার্যতা
- Rationale: University philosophy and set/function pages support the prose register but do not directly attest these compound labels. The section distinguishes representing arithmetic structures inside set theory from claiming that numbers metaphysically are the particular sets selected. Alternative ordered-pair encodings yield equally adequate but literally different set objects; the citation and source argument govern the sense.
- Plausible alternatives: বিধিবদ্ধ কঠোরতা, অধিবিদ্যাগত একীভবন, সেটতাত্ত্বিক প্রোথিতকরণ, বিকল্প নির্মাণ and বেনাসেরাফীয় অল্পনির্ধারণ are plausible alternatives; the selected wording preserves the passage’s construction-versus-identification distinction.
- Status: provisional-philosophical; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নির্মাণের কঠোরতা; অধিবিদ্যাগত অভিন্নকরণ; সেটতাত্ত্বিক অন্তর্ভুক্তি; প্রতিদ্বন্দ্বী নির্মাণ; বেনাসেরাফ-ধর্মী অনির্ধার্যতা’ express the OpenLogic sense(s) ‘rigour of a construction; metaphysical identification; set-theoretic embedding; rival constructions; Benacerraf-style underdetermination’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T056

- Source term or concept: infinite set; Dedekind-infinite set; Hilbert's Hotel
- Chosen Bengali: অসীম সেট; ডেডেকিন্ড-অসীম সেট; হিলবার্টের হোটেল
- Rationale: NSOU directly attests finite and infinite sets, while its mapping page supports the injection language in the definition. The Dedekind compound and Hilbert title are transliterations governed by the OpenLogic definitions and historical attribution, not direct canon attestations. Dedekind-infinite means that the set injects into a proper subset; it is not being silently identified with every later notion of infinitude.
- Plausible alternatives: ডেডেকিন্ড অসীম সেট and হিলবার্টের সরাইখানা are plausible alternatives; the selected forms retain the named mathematical criteria while matching the established অসীম সেট root.
- Status: mixed-direct-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অসীম সেট; ডেডেকিন্ড-অসীম সেট; হিলবার্টের হোটেল’ express the OpenLogic sense(s) ‘infinite set; Dedekind-infinite set; Hilbert's Hotel’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 22 occurrence(s). Representative locations:
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:19`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:21`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:23`; final reader page pending
  - `OLP-0173` `upstream/content/first-order-logic/models-theories/size-of-structures.tex:63-70` → `bn-Beng-IN/content/first-order-logic/models-theories/size-of-structures.tex:70`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:91-96` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:73`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
One important consequence of the completeness theorem is the
compactness theorem.  The compactness theorem states that if each
\emph{finite} subset of a set of !!{sentence}s is satisfiable, the
entire set is satisfiable---even if the set itself is infinite. This
is far from obvious. There is nothing that seems to rule out, at first
glance at least, the possibility of there being infinite sets of
!!{sentence}s which are contradictory, but the contradiction only
arises, so to speak, from the infinite number.  The compactness
theorem says that such a scenario can be ruled out: there are no
unsatisfiable infinite sets of !!{sentence}s each finite subset of
which is satisfiable. Like the completeness theorem, it has a version
related to entailment: if an infinite set of !!{sentence}s entails
something, already a finite subset does.
```

### BN-IN-T057

- Source term or concept: Dedekind algebra; successor function; self-map; f-closed set; closure under f
- Chosen Bengali: ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ
- Rationale: The checked relation, mapping, injection, proof and infinite-set pages support the mathematical prose but do not directly attest these structural compounds. বীজগঠন names the triple consisting of a carrier, a self-map and a distinguished element rather than the school subject of algebra. স্ব-অপেক্ষক makes the common domain/codomain carrier explicit where the frozen lemma leaves A unbound. Closure is the intersection-defined least f-closed set containing the stated seed, and is distinct from topological closure.
- Plausible alternatives: ডেডেকিন্ড বীজগণিত, পরবর্তী অপেক্ষক, স্বচিত্রণ, f-সংবৃত সেট and f-সংবরণ are plausible alternatives; the selected terms distinguish the carrier structure, endomap and least closed set.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ’ express the OpenLogic sense(s) ‘Dedekind algebra; successor function; self-map; f-closed set; closure under f’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 23 occurrence(s). Representative locations:
  - `OLP-0022` `upstream/content/sets-functions-relations/functions/function-kinds.tex:83-84` → `bn-Beng-IN/content/sets-functions-relations/functions/function-kinds.tex:60`; final reader page pending
  - `OLP-0024` `upstream/content/sets-functions-relations/functions/inverses.tex:12-16` → `bn-Beng-IN/content/sets-functions-relations/functions/inverses.tex:13`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:9-10` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:10`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:16-39` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:14`; final reader page pending
  - `OLP-0051` `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:16-39` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-algebra.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The successor function $f \colon \Nat \to \Nat$ given by $f(x) = x+1$
is !!{injective} but not !!{surjective}.
```

### BN-IN-T058

- Source term or concept: parameter of a formula; free variable; recursive definition
- Chosen Bengali: সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা
- Rationale: University quantification and school algebra pages directly support formula and variable prose, while the exact parameter/free-variable compounds and recursive-definition label remain provisional. A parameter is an additional freely assignable object in phi(x,c1,...,ck). Recursive definition fixes later values through the displayed base and successor clauses; it does not by itself claim effective computability. This concise label refines the descriptive recursive wording in T042 without changing that earlier sense.
- Plausible alternatives: সূত্রের সহগ, অবদ্ধ চল and আবর্ত সংজ্ঞা are plausible alternatives; পরামিতি, মুক্ত চলরাশি and পুনরাবৃত্ত সংজ্ঞা preserve the syntactic and recursive senses fixed by the formulas.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা’ express the OpenLogic sense(s) ‘parameter of a formula; free variable; recursive definition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 18 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:73`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:30-65` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:64`; final reader page pending
  - `OLP-0145` `upstream/content/first-order-logic/introduction/semantic-notions.tex:13-25` → `bn-Beng-IN/content/first-order-logic/introduction/semantic-notions.tex:17`; final reader page pending
  - `OLP-0164` `upstream/content/first-order-logic/syntax-and-semantics/assignments.tex:13-27` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/assignments.tex:22`; final reader page pending
  - `OLP-0164` `upstream/content/first-order-logic/syntax-and-semantics/assignments.tex:107-116` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/assignments.tex:113`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
As in the case of second-order logic, one can think of higher-order
logic as a kind of many-sorted logic, where there is a sort for each
type of object we want to consider. But it is usually clearer just to
define the syntax of higher-type logic from the ground up. For
example, we can define a set of finite types inductively, as follows:
\begin{enumerate}
\item $\Nat$ is a finite type.
\item If $\sigma$ and $\tau$ are finite types, then so is $\sigma
  \to \tau$.
\item If $\sigma$ and $\tau$ are finite types, so is $\sigma \times
  \tau$.
\end{enumerate}
Intuitively, $\Nat$ denotes the type of the natural numbers,
$\sigma \to \tau$ denotes the type of functions from $\sigma$ to
$\tau$, and $\sigma \times \tau$ denotes the type of pairs of objects,
one from $\sigma$ and one from $\tau$. We can then define a set of
terms inductively, as follows:
\begin{enumerate}
\item For each type $\sigma$, there is a stock of variables $x$, $y$,
  $z$, \dots of type $\sigma$
\item $\Obj 0$ is a term of type $\Nat$
\item $\Obj S$ (successor) is a term of type $\Nat \to \Nat$
\item If $s$ is a term of type $\sigma$, and $t$ is a term of type
  $\Nat \to (\sigma \to \sigma)$, then $\Obj{R}_{st}$ is a term of type
  $\Nat \to \sigma$
\item If $s$ is a term of type $\tau \to \sigma$ and $t$ is a
  term of type~$\tau$, then $s(t)$ is a term of type $\sigma$
\item If $s$ is a term of type~$\sigma$ and $x$ is a variable of
  type~$\tau$, then $\lambd[x][s]$ is a term of type $\tau \to \sigma$.
\item If $s$ is a term of type~$\sigma$ and $t$ is a term of
  type~$\tau$, then $\tuple{s, t}$ is a term of type $\sigma \times
  \tau$.
\item If $s$ is a term of type~$\sigma \times \tau$ then $p_1(s)$ is a
  term of type~$\sigma$ and $p_2(s)$ is a term of type~$\tau$.
\end{enumerate}
Intuitively, $\Obj{R}_{st}$ denotes the function defined recursively by
\begin{align*}
\Obj{R}_{st}(0) & = s \\
\Obj{R}_{st}(x+1) & = t(x, R_{st}(x)),
\end{align*}
$\tuple{s, t}$ denotes the pair whose first component is~$s$ and whose
second component is~$t$, and $p_1(s)$ and~$p_2(s)$ denote the first
and second elements (``projections'') of~$s$. Finally, $\lambd[x][s]$
denotes the function~$f$ defined by
\[
f(x) = s
\]
for any~$x$ of type~$\sigma$; so item (6) gives us a form of
comprehension, enabling us to define functions using
terms. !!^{formula}s are built up from !!{identity} statements $\eq[s][t]$
between terms of the same type, the usual propositional connectives,
and higher-type quantification. One can then take the axioms of the
system to be the basic equations governing the terms defined above,
together with the usual rules of logic with quantifiers and !!{identity}.
```

### BN-IN-T059

- Source term or concept: isomorphic structures; structuralist; surrogate for the natural numbers; pure laws of thought
- Chosen Bengali: সমরূপ গঠন; গঠনবাদী; স্বাভাবিক সংখ্যার প্রতিস্থাপক; চিন্তার বিশুদ্ধ বিধি
- Rationale: NSOU uses the root সমরূপ in mapping context, and T037 deliberately reserves it from the chosen bijection label so it can express isomorphism here. The structuralist and philosophical compounds are provisional renderings supported only by university-level prose context. The passage claims shared mathematical structure among Dedekind algebras, not literal identity of their carrier sets or a completed proof that set existence follows from logic.
- Plausible alternatives: সমাকৃতি গঠন, কাঠামোবাদী, স্বাভাবিক সংখ্যার বিকল্প প্রতিনিধি and চিন্তার খাঁটি নিয়ম are plausible alternatives; the selected forms preserve isomorphism, philosophical structuralism and surrogate-object claims as separate notions.
- Status: mixed-contextual-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সমরূপ গঠন; গঠনবাদী; স্বাভাবিক সংখ্যার প্রতিস্থাপক; চিন্তার বিশুদ্ধ বিধি’ express the OpenLogic sense(s) ‘isomorphic structures; structuralist; surrogate for the natural numbers; pure laws of thought’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0187` `upstream/content/model-theory/basics/isomorphism.tex:9-10` → `bn-Beng-IN/content/model-theory/basics/isomorphism.tex:10`; final reader page pending
  - `OLP-0052` `upstream/content/sets-functions-relations/infinite/dedekind-induction.tex:12-14` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-induction.tex:12`; final reader page pending
  - `OLP-0052` `upstream/content/sets-functions-relations/infinite/dedekind-induction.tex:29-31` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-induction.tex:28`; final reader page pending
  - `OLP-0053` `upstream/content/sets-functions-relations/infinite/dedekinds-proof.tex:28-40` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekinds-proof.tex:18`; final reader page pending
  - `OLP-0053` `upstream/content/sets-functions-relations/infinite/dedekinds-proof.tex:42-64` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekinds-proof.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{mod}{bas}{iso}
\olsection{Isomorphic Structures}
```

### BN-IN-T060

- Source term or concept: syntax; semantics; metatheory; inductive definition; unique readability
- Chosen Bengali: সংকেতবিন্যাস; অর্থতত্ত্ব; অধিতত্ত্ব; আরোহী সংজ্ঞা; একক পাঠযোগ্যতা
- Rationale: The checked school and university logic pages support proposition, connective and quantified-formula discourse but do not directly attest these five metalogical compounds. সংকেতবিন্যাস is used because this chapter first specifies strings and formation rules, while অর্থতত্ত্ব specifies truth under valuations. আরোহী সংজ্ঞা follows the project's established mathematical-induction register. Unique readability means unique structural parsing, not merely legible typography.
- Plausible alternatives: বাক্যগঠন for syntax was considered; সংকেতবিন্যাস was selected because the chapter governs formal symbol strings rather than ordinary sentence grammar. একক অর্থোদ্ধার for unique readability was rejected because the theorem proves unique syntactic parsing before semantics is assigned.
- Status: provisional-formally-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংকেতবিন্যাস; অর্থতত্ত্ব; অধিতত্ত্ব; আরোহী সংজ্ঞা; একক পাঠযোগ্যতা’ express the OpenLogic sense(s) ‘syntax; semantics; metatheory; inductive definition; unique readability’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 102 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:102-112` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:103`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:102-112` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:107`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:102-112` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:108`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:119`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
As in the case of second-order logic, there are different versions of
higher-type semantics that one might want to use. In the full version,
variables of type $\sigma \to \tau$ range over the set of \emph{all}
functions from the objects of type~$\sigma$ to objects of type~$\tau$.
As you might expect, this semantics is too strong to admit a complete,
effective !!{derivation} system. But one can consider a weaker semantics, in
which !!a{structure} consists of sets of elements $T_\tau$ for each
type $\tau$, together with appropriate operations for application,
projection, etc. If the details are carried out correctly, one can
obtain completeness theorems for the kinds of !!{derivation} systems described
above.
```

### BN-IN-T061

- Source term or concept: propositional variable; propositional/logical connective; truth value; truth-functional; material conditional
- Chosen Bengali: বচনচল; বচনসংযোজক/যৌক্তিক সংযোজক; সত্যমান; সত্যমান-অপেক্ষকধর্মী; বস্তুগত শর্তবচন
- Rationale: P008 directly supplies truth-evaluable statement and connective language, P009 supplies বচন, and the school algebra pages support variable prose. The compounds remain normalized rather than directly quoted. A propositional variable stands for a truth-evaluable proposition; truth-functional means that the displayed output truth value depends only on input truth values. The material conditional is the particular truth function defined later, not every conditional in ordinary language.
- Plausible alternatives: বচনীয় চলরাশি and উক্তিচল were possible compounds; বচনচল continues the university বচন sense and remains provisional. সত্যমূল্য is a common loan-shaped alternative; সত্যমান aligns with the already chosen truth-function vocabulary.
- Status: mixed-attested-roots-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বচনচল; বচনসংযোজক/যৌক্তিক সংযোজক; সত্যমান; সত্যমান-অপেক্ষকধর্মী; বস্তুগত শর্তবচন’ express the OpenLogic sense(s) ‘propositional variable; propositional/logical connective; truth value; truth-functional; material conditional’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 43 occurrence(s). Representative locations:
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13`; final reader page pending
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:15-34` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:16`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:13`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:17`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Axioms and Rules for the Propositional Connectives}
```

### BN-IN-T062

- Source term or concept: negation; conjunction; disjunction; conditional/implication; biconditional/material equivalence
- Chosen Bengali: নঞর্থকরণ; সংযোজন; বিয়োজন; শর্তবচন/নিহিতকরণ; দ্বিশর্তবচন/বস্তুগত সমতুল্যতা
- Rationale: P008 directly uses না-ক্রিয়া, অন্তঃসংযোগ, বিকল্প/বিয়োজন and connective notation. The edition retains the prior T021 choice সংযোজন for conjunction and uses concise normalized compounds for the other operators. The source's truth tables and abbreviation clauses control each meaning; biconditional is not being identified with syntactic identity.
- Plausible alternatives: P008 prints না-ক্রিয়া and অন্তঃসংযোগ; নঞর্থকরণ and the prior T021 সংযোজন are normalized edition forms, while the witnessed variants remain recorded. সমতুল্যতা alone was not used for biconditional because it could collide with semantic or relation-theoretic equivalence.
- Status: attested-variants-normalized; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নঞর্থকরণ; সংযোজন; বিয়োজন; শর্তবচন/নিহিতকরণ; দ্বিশর্তবচন/বস্তুগত সমতুল্যতা’ express the OpenLogic sense(s) ‘negation; conjunction; disjunction; conditional/implication; biconditional/material equivalence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 38 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:115`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:33-52` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:36`; final reader page pending
  - `OLP-0131` `upstream/content/first-order-logic/completeness/lindenbaums-lemma.tex:15-25` → `bn-Beng-IN/content/first-order-logic/completeness/lindenbaums-lemma.tex:22`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:108-141` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:138`; final reader page pending
  - `OLP-0066` `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:15-31` → `bn-Beng-IN/content/first-order-logic/proof-systems/natural-deduction.tex:18`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  \ollabel{prop:derivfacts}
\begin{enumerate}
\item $\Proves (!A \lif !B) \lif ((!B \lif !C)
  \lif (!A \lif !C)$; \ollabel{derivfacts:a}
\item If $\Gamma \cup \{ \lnot !A\}
  \Proves \lnot !B$ then $\Gamma \cup \{ !B\} \Proves
  !A$ (Contraposition); \ollabel{derivfacts:b}
\item  $\{ !A, \lnot!A\} \Proves
    !B$ (Ex Falso Quodlibet, Explosion); \ollabel{derivfacts:c}
\item  $\{ \lnot\lnot!A\} \Proves
  !A$ (Double Negation Elimination);\ollabel{derivfacts:d}
\item If $\Gamma \Proves \lnot\lnot!A$ then $\Gamma \Proves
  !A$;\ollabel{derivfacts:e}
\end{enumerate}
\end{prop}
```

### BN-IN-T063

- Source term or concept: denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation
- Chosen Bengali: অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ
- Rationale: The exact compounds are sparse in the checked canon, so the source definitions govern them. অসীম গণনীয় distinguishes denumerable from the finite-inclusive countable usage recorded in T040. প্রতীকক্রম continues T019. Syntactic identity requires equal length and the same symbol at every place; it is distinct from semantic equivalence. A defined symbol is an abbreviation rather than a primitive member of the language.
- Plausible alternatives: ক্রমগণনীয় was considered for denumerable; অসীম গণনীয় makes the exclusion of finite sets explicit. সমানতা was not used for syntactic identity because the relation concerns literal symbol-by-symbol identity rather than equality of denotation or truth value.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ’ express the OpenLogic sense(s) ‘denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 129 occurrence(s). Representative locations:
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:14`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:16`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:17`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:23`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:92`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{editorial}
  No effort has been made yet to ensure that the material in this
  chapter respects various tags indicating which connectives and
  quantifiers are primitive or defined: all are assumed to be
  primitive, except $\liff$ which is assumed to be defined. If the FOL
  tag is true, we produce a version with quantifiers, otherwise
  without.
\end{editorial}
```

### BN-IN-T064

- Source term or concept: formula induction; balanced formula; proper initial segment; parsing; uniform substitution
- Chosen Bengali: সূত্রের উপর আরোহ; সুষম সূত্র; প্রকৃত প্রারম্ভিক খণ্ড; গঠনবিশ্লেষণ; সমরূপ প্রতিস্থাপন
- Rationale: Checked logic, variable and proof pages support the register but not all five exact compounds. The formal propositions control the senses: balanced counts matching parentheses, proper initial means strictly shorter from the beginning, parsing recovers the one formation case, and uniform substitution replaces every occurrence of the selected propositional variable simultaneously.
- Plausible alternatives: বিশ্লেষণ alone was considered for parsing; গঠনবিশ্লেষণ makes the formation-tree sense explicit. সর্বত্র প্রতিস্থাপন was considered; সমরূপ প্রতিস্থাপন follows the source convention that every occurrence of the selected variable is replaced uniformly.
- Status: provisional-mathematically-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সূত্রের উপর আরোহ; সুষম সূত্র; প্রকৃত প্রারম্ভিক খণ্ড; গঠনবিশ্লেষণ; সমরূপ প্রতিস্থাপন’ express the OpenLogic sense(s) ‘formula induction; balanced formula; proper initial segment; parsing; uniform substitution’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:50-52` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:51`; final reader page pending
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:58-62` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:60`; final reader page pending
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:76-79` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:82`; final reader page pending
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:81-88` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:88`; final reader page pending
  - `OLP-0059` `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:91-98` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/preliminaries.tex:94`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop} \ollabel{prop:noinit}
No proper initial segment of !!a{formula} is !!a{formula}.
\end{prop}
```

### BN-IN-T065

- Source term or concept: formation sequence; junk/redundant formula; strong induction
- Chosen Bengali: গঠন-অনুক্রম; অপ্রয়োজনীয় সূত্র; প্রবল আরোহ
- Rationale: These labels are not directly attested in the checked pages. A formation sequence is the finite bottom-up witness defined by its indexed clauses; it may repeat or include formulas unused in the final construction. The strong-induction hypothesis applies to every earlier final index. The Bengali prose avoids treating the source's informal 'junk' label as a distinct mathematical class.
- Plausible alternatives: নির্মাণ-অনুক্রম was considered; গঠন-অনুক্রম stays close to the chapter formation terminology. The source colloquial junk is rendered descriptively as অপ্রয়োজনীয় সূত্র rather than adopted as a technical noun.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠন-অনুক্রম; অপ্রয়োজনীয় সূত্র; প্রবল আরোহ’ express the OpenLogic sense(s) ‘formation sequence; junk/redundant formula; strong induction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 73 occurrence(s). Representative locations:
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:11-11` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:11`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:13-23` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:16`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:40-49` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:38`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:40-49` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:41`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:40-49` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:46`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Formation Sequences}
```

### BN-IN-T066

- Source term or concept: valuation; evaluation function; satisfaction; local determination; truth table
- Chosen Bengali: সত্যমান-আরোপ; মূল্যায়ন অপেক্ষক; পরিতৃপ্তি; স্থানীয় নির্ধারণ; সত্যসারণি
- Rationale: P008 supports truth-evaluable statements and connective tables, and T043 already fixes সত্যসারণি and সত্যমান-অপেক্ষক. The remaining compounds are definition-governed. A valuation assigns true or false only to propositional variables; the evaluation function extends it recursively to every formula. Satisfaction is exactly evaluation to True, and local determination says only variables occurring in the fixed formula matter.
- Plausible alternatives: মূল্যায়ন alone was considered for valuation; সত্যমান-আরোপ distinguishes the initial variable assignment from the recursively extended মূল্যায়ন অপেক্ষক. সিদ্ধি/সন্তুষ্টি were possible satisfaction loans; পরিতৃপ্তি is retained as the explicit model-theoretic relation and remains provisional.
- Status: mixed-contextual-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সত্যমান-আরোপ; মূল্যায়ন অপেক্ষক; পরিতৃপ্তি; স্থানীয় নির্ধারণ; সত্যসারণি’ express the OpenLogic sense(s) ‘valuation; evaluation function; satisfaction; local determination; truth table’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 186 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:17`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:20`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:26`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:41-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:45`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:41-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:50`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
Just as we've defined a number of important semantic notions
(\iftag{FOL}{validity}{tautology}, entailment, satisfiability), we now
define corresponding \emph{proof-theoretic notions}.  These are not
defined by appeal to satisfaction of !!{sentence}s in !!{structure}s,
but by appeal to the !!{derivability} or !!{nonderivability} of
certain formulas.  It was an important discovery that these notions
coincide.  That they do is the content of the \emph{soundness} and
\emph{completeness theorems}.
\end{explain}
```

### BN-IN-T067

- Source term or concept: satisfiable/unsatisfiable; tautology; contingent; semantic entailment; monotonicity; semantic deduction theorem
- Chosen Bengali: পরিতৃপ্তিযোগ্য/অপরিতৃপ্তিযোগ্য; সর্বতঃসত্য; আপতিক; অর্থগত অনুসিদ্ধান্ত; একঘেয়েতা; অর্থগত নিঃসরণ উপপাদ্য
- Rationale: The checked logic and proof pages support the proposition and truth register but not these exact metalogical labels. Each Bengali term is governed by the adjacent quantified definition. সর্বতঃসত্য requires truth under every valuation; আপতিক means satisfiable but not tautological. Entailment quantifies over valuations satisfying the premises, and the deduction theorem internalizes one premise with the material conditional.
- Plausible alternatives: স্বতঃসত্য was considered for tautology but could suggest an axiom accepted without proof; সর্বতঃসত্য exposes truth under every valuation. অর্থগত ফলন was considered for entailment; অর্থগত অনুসিদ্ধান্ত better preserves the premise-to-conclusion relation.
- Status: provisional-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিতৃপ্তিযোগ্য/অপরিতৃপ্তিযোগ্য; সর্বতঃসত্য; আপতিক; অর্থগত অনুসিদ্ধান্ত; একঘেয়েতা; অর্থগত নিঃসরণ উপপাদ্য’ express the OpenLogic sense(s) ‘satisfiable/unsatisfiable; tautology; contingent; semantic entailment; monotonicity; semantic deduction theorem’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 154 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:17`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:52-56` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:52`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:26`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:41-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:50`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:59-66` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:63`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
Just as we've defined a number of important semantic notions
(\iftag{FOL}{validity}{tautology}, entailment, satisfiability), we now
define corresponding \emph{proof-theoretic notions}.  These are not
defined by appeal to satisfaction of !!{sentence}s in !!{structure}s,
but by appeal to the !!{derivability} or !!{nonderivability} of
certain formulas.  It was an important discovery that these notions
coincide.  That they do is the content of the \emph{soundness} and
\emph{completeness theorems}.
\end{explain}
```

### BN-IN-T068

- Source term or concept: derivation system; purely syntactic object/method; mechanical verification; metatheoretical treatment
- Chosen Bengali: নিষ্পাদন পদ্ধতি; সম্পূর্ণ সংকেতবিন্যাসগত বস্তু/পদ্ধতি; যান্ত্রিক যাচাই; অধিতাত্ত্বিক বিচার
- Rationale: T033 already fixes নিষ্পাদন for derivation. The proof-systems introduction extends it compositionally to নিষ্পাদন পদ্ধতি and distinguishes finite formal syntax from semantics. The checked pages support logic, formula and proof prose but do not directly attest the full compounds. Mechanical verification means that correctness of a proposed finite derivation is decidable by inspecting its form; it does not claim that a derivation can always be found mechanically.
- Plausible alternatives: প্রমাণপদ্ধতি was considered, but the source consistently exposes the narrower token derivation and T033 already fixes নিষ্পাদন for it. রূপতাত্ত্বিক was considered for syntactic but could be confused with linguistic morphology; সংকেতবিন্যাসগত states the formal-symbol sense.
- Status: provisional-contextual; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিষ্পাদন পদ্ধতি; সম্পূর্ণ সংকেতবিন্যাসগত বস্তু/পদ্ধতি; যান্ত্রিক যাচাই; অধিতাত্ত্বিক বিচার’ express the OpenLogic sense(s) ‘derivation system; purely syntactic object/method; mechanical verification; metatheoretical treatment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 144 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18-29` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:15-22` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:17`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:16`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:18`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:28`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
As we've seen, giving !!{derivation}s in an axiomatic system is
cumbersome, and !!{derivation}s may be hard to find. Rather than
actually write out long lists of !!{formula}s, it is generally easier
to argue that such !!{derivation}s exist, by making use of a few
simple results. We've already established three such results:
\olref[ptn]{prop:reflexivity} says we can always assert that $\Gamma
\Proves !A$ when we know that $!A \in
\Gamma$. \olref[ptn]{prop:monotonicity} says that if $\Gamma \Proves !A$
then also $\Gamma \cup \{!B\} \Proves !A$. And
\olref[ptn]{prop:transitivity} implies that if $\Gamma \Proves !A$ and
$!A \Proves !B$, then $\Gamma \Proves !B$. Here's another simple
result, a ``meta''-version of modus ponens:
```

### BN-IN-T069

- Source term or concept: soundness; completeness; consistency/inconsistency; syntactic counterpart
- Chosen Bengali: বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ
- Rationale: T033 already records পূর্ণতা. The remaining proof-theoretic compounds were not directly attested in the checked canon and therefore remain governed by the adjacent biconditionals. বিশুদ্ধতা is the direction from derivability to entailment or validity; পূর্ণতা is the converse. Syntactic consistency is required to coincide with semantic satisfiability, so সঙ্গতি is kept distinct from both semantic truth and formula equivalence.
- Plausible alternatives: যথার্থতা and শুদ্ধতা were considered for soundness; বিশুদ্ধতা remains provisional and is fixed by the explicit derivability-to-entailment direction. সামঞ্জস্য was considered for consistency; সঙ্গতি is shorter and remains distinct from semantic equivalence by definition.
- Status: provisional-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ’ express the OpenLogic sense(s) ‘soundness; completeness; consistency/inconsistency; syntactic counterpart’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 140 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:23`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:38-41` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:38`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:13`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:15-17` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:16`; final reader page pending
  - `OLP-0122` `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:15-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:19`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
Just as we've defined a number of important semantic notions
(\iftag{FOL}{validity}{tautology}, entailment, satisfiability), we now
define corresponding \emph{proof-theoretic notions}.  These are not
defined by appeal to satisfaction of !!{sentence}s in !!{structure}s,
but by appeal to the !!{derivability} or !!{nonderivability} of
certain formulas.  It was an important discovery that these notions
coincide.  That they do is the content of the \emph{soundness} and
\emph{completeness theorems}.
\end{explain}
```

### BN-IN-T070

- Source term or concept: axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens
- Chosen Bengali: স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স
- Rationale: The checked logic and proof pages support স্বতঃসিদ্ধ, formula and proof register, but not the complete proof-system terminology. Each axiom schema denotes a fixed form with substitution instances rather than one sentence. A line is সমর্থিত when it is an axiom, a stated premise or follows by an inference rule. মোডাস পোনেন্স is transliterated because no directly attested India-standard Bengali replacement was found in the checked pages.
- Plausible alternatives: স্বতঃসিদ্ধমূলক অবরোহ was considered, but নিষ্পাদন keeps the system aligned with the project derivation token. ন্যায়সংগত পংক্তি was considered for justified line; সমর্থিত পংক্তি more directly marks that a listed axiom, premise or rule warrants the step.
- Status: provisional-formally-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স’ express the OpenLogic sense(s) ‘axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 214 occurrence(s). Representative locations:
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:36-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:36`; final reader page pending
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:41-41` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:41`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:26`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:27`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Modus ponens]
  If $!B$ and $!B \lif !A$ already occur in !!a{derivation}, then $!A$ is
  a correct inference step.
\end{defn}
```

### BN-IN-T071

- Source term or concept: natural deduction; proof by cases; indirect proof; conditional proof
- Chosen Bengali: স্বাভাবিক নিষ্পাদন; ক্ষেত্রবিচারে প্রমাণ; পরোক্ষ প্রমাণ; শর্তাধীন প্রমাণ
- Rationale: The exact system and proof-pattern names were not directly attested in the checked canon. স্বাভাবিক নিষ্পাদন retains the established derivation term and the source's contrast with regimented ordinary mathematical reasoning. ক্ষেত্রবিচারে প্রমাণ is the familiar mathematical pattern of proving the same conclusion from each disjunct; পরোক্ষ প্রমাণ assumes the negation and derives contradiction; শর্তাধীন প্রমাণ derives the consequent under the antecedent.
- Plausible alternatives: স্বাভাবিক অবরোহ is a possible loan-shaped system name; স্বাভাবিক নিষ্পাদন preserves the established derivation vocabulary while remaining provisional. ক্ষেত্রভিত্তিক প্রমাণ was used in an early draft; ক্ষেত্রবিচারে প্রমাণ was selected as the more idiomatic mathematical phrasing.
- Status: provisional-proof-patterns; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাভাবিক নিষ্পাদন; ক্ষেত্রবিচারে প্রমাণ; পরোক্ষ প্রমাণ; শর্তাধীন প্রমাণ’ express the OpenLogic sense(s) ‘natural deduction; proof by cases; indirect proof; conditional proof’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 32 occurrence(s). Representative locations:
  - `OLP-0140` `upstream/content/first-order-logic/introduction/first-order-logic.tex:60-73` → `bn-Beng-IN/content/first-order-logic/introduction/first-order-logic.tex:62`; final reader page pending
  - `OLP-0140` `upstream/content/first-order-logic/introduction/first-order-logic.tex:60-73` → `bn-Beng-IN/content/first-order-logic/introduction/first-order-logic.tex:65`; final reader page pending
  - `OLP-0088` `upstream/content/first-order-logic/natural-deduction/derivations.tex:15-21` → `bn-Beng-IN/content/first-order-logic/natural-deduction/derivations.tex:17`; final reader page pending
  - `OLP-0084` `upstream/content/first-order-logic/natural-deduction/natural-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/natural-deduction/natural-deduction.tex:9`; final reader page pending
  - `OLP-0084` `upstream/content/first-order-logic/natural-deduction/natural-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/natural-deduction/natural-deduction.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Another topic you probably remember from your first introduction to
formal logic is that there are \emph{!!{derivation}s}.  If you have
taken a first formal logic course, your instructor will have made you
practice finding such !!{derivation}s, perhaps even !!a{derivation}
that shows that the above entailment holds.  There are many different
ways to give !!{derivation}s: you may have done something called
``natural deduction'' or ``truth trees,'' but there are many others.
The purpose of !!{derivation} systems is to provide tools using which the
logicians' questions above can be answered: e.g., a natural deduction
!!{derivation} in which $\lforall[x][(!A(x) \lif !B(x))$ and
$\lexists[x][!A(x)]$ are premises and $\lexists[x][!B(x)]]$ is the
conclusion (last line) \emph{verifies} that $\lexists[x][!B(x)]$
logically follows from $\lforall[x][(!A(x) \lif !B(x))]$ and
$\lexists[x][!A(x)]$.
```

### BN-IN-T072

- Source term or concept: introduction/elimination rule; assumption/hypothesis; discharge/undischarged assumption; proof-theoretic semantics
- Chosen Bengali: প্রবর্তন/অপসারণ-বিধি; অনুমিতি/পূর্বধারণা; অনুমিতি অবমুক্ত করা/অনবমুক্ত অনুমিতি; প্রমাণতাত্ত্বিক অর্থতত্ত্ব
- Rationale: These compounds are controlled by the natural-deduction explanation and proof tree rather than directly attested canonical terms. অনুমিতি names a leaf available within a derivation, while পূর্বধারণা is used in explanatory prose for a temporarily supposed claim. Discharge removes an assumption from the dependencies of the conclusion, not from the printed tree. প্রমাণতাত্ত্বিক অর্থতত্ত্ব names the philosophical view that introduction and elimination rules can determine logical meaning.
- Plausible alternatives: অনুমান খারিজ করা and অনুমান নিরসন were considered for discharge; অবমুক্ত করা states that the assumption ceases to be a dependency without suggesting deletion of the printed leaf. প্রবেশ/বর্জন-বিধি were possible compact alternatives; প্রবর্তন/অপসারণ follows the direction of the connective rules more transparently.
- Status: provisional-natural-deduction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রবর্তন/অপসারণ-বিধি; অনুমিতি/পূর্বধারণা; অনুমিতি অবমুক্ত করা/অনবমুক্ত অনুমিতি; প্রমাণতাত্ত্বিক অর্থতত্ত্ব’ express the OpenLogic sense(s) ‘introduction/elimination rule; assumption/hypothesis; discharge/undischarged assumption; proof-theoretic semantics’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 249 occurrence(s). Representative locations:
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:41-56` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:53`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:35`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:31`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:84-98` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:92`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:165-180` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:161`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}\ollabel{ex:identity}
Let's try to find !!a{derivation} of $!D \lif !D$.  It is not an
instance of an axiom, so we have to use \MP{} to !!{derive} it.
\olref[prp]{ax:lif1} is an axiom of the form~$!A \lif !B$ to which we
could apply~\MP. To be useful, of course, the $!B$ which \MP{} would
justify as a correct step in this case would have to be~$!D \lif !D$,
since this is what we want to !!{derive}. That means $!A$ would also
have to be $!D$, i.e., we might look at this instance of
\olref[prp]{ax:lif1}:
\[
!D \lif (!D \lif !D)
\]
In order to apply \MP, we would also need to justify the corresponding
second premise, namely~$!A$. But in our case, that would be~$!D$, and
we won't be able to !!{derive}~$!D$ by itself. So we need a different
strategy.
```

### BN-IN-T073

- Source term or concept: sequent calculus; sequent; initial sequent; left/right side; weakening rule
- Chosen Bengali: সিকোয়েন্ট কলন; সিকোয়েন্ট; প্রারম্ভিক সিকোয়েন্ট; বাঁ/ডানপাশ; দুর্বলীকরণ-বিধি
- Rationale: No checked page directly attests sequent-calculus terminology. The system name and object are therefore transparently transliterated, with কলন marking a formal calculus. A sequent is explicitly a pair of finite sentence sequences separated by the sequent sign, and either side may be empty. প্রারম্ভিক সিকোয়েন্ট names the special leaves also called axioms; দুর্বলীকরণ is reserved for the structural rule macro.
- Plausible alternatives: সিকুয়েন্ট ক্যালকুলাস and অনুসিদ্ধান্ত কলন were considered; সিকোয়েন্ট কলন keeps the international object name while avoiding collision with semantic entailment. প্রাথমিক সিকোয়েন্ট was considered for initial sequent; প্রারম্ভিক better marks the special leaf position rather than elementary difficulty.
- Status: provisional-transliterated-system; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সিকোয়েন্ট কলন; সিকোয়েন্ট; প্রারম্ভিক সিকোয়েন্ট; বাঁ/ডানপাশ; দুর্বলীকরণ-বিধি’ express the OpenLogic sense(s) ‘sequent calculus; sequent; initial sequent; left/right side; weakening rule’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 166 occurrence(s). Representative locations:
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:58-80` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:61`; final reader page pending
  - `OLP-0144` `upstream/content/first-order-logic/introduction/sentences.tex:29-52` → `bn-Beng-IN/content/first-order-logic/introduction/sentences.tex:29`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:57-96` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:77`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:116-147` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:114`; final reader page pending
  - `OLP-0064` `upstream/content/first-order-logic/proof-systems/introduction.tex:38-48` → `bn-Beng-IN/content/first-order-logic/proof-systems/introduction.tex:39`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The other axiom involving just~$\lif$ is \olref[prp]{ax:lif2}, i.e.,
\[
(!A \lif (!B \lif !C)) \lif ((!A \lif !B) \lif (!A \lif !C))
\]
We could get to the last nested conditional by applying \MP{}
twice. Again, that would mean that we want an instance of
\olref[prp]{ax:lif2} where $!A \lif !C$ is $!D \lif !D$, the !!{formula} we
are aiming for. Then of course, $!A$ and $!C$ are both~$!D$. How
should we pick~$!B$ so that both $!A \lif (!B \lif !C)$ and $!A \lif
!B$, i.e., in our case $!D \lif (!B \lif !D)$ and $!D \lif !B$, are
also !!{derivable}? Well, the first of these is already an instance of
\olref[prp]{ax:lif1}, whatever we decide $!B$ to be. And $!D \lif !B$ would
be another instance of \olref[prp]{ax:lif1} if $!B$ were $(!D \lif !D)$.
So, our !!{derivation} is:
\begin{derivation}
  1. & $!D \lif ((!D \lif !D) \lif !D)$ & \olref[prp]{ax:lif1}\\
  2. & $(!D \lif ((!D \lif !D) \lif !D)) \lif {}$\\
  & \qquad $((!D \lif (!D \lif !D)) \lif (!D \lif !D))$ & \olref[prp]{ax:lif2}\\
  3. & $(!D \lif (!D \lif !D)) \lif (!D \lif !D)$ & 1, 2, \MP\\
  4. & $!D \lif (!D \lif !D)$ & \olref[prp]{ax:lif1}\\
  5. & $!D \lif !D$ & 3, 4, \MP
\end{derivation}
\end{ex}
```

### BN-IN-T074

- Source term or concept: tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus
- Chosen Bengali: ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন
- Rationale: The checked sources support formula, truth value and proof-tree prose but not this system vocabulary. The section explicitly defines a signed formula as a truth-value sign paired with a sentence and defines closure by a matching true/false pair on every branch. ট্যাবলো is retained as the international system name, with সত্য-বৃক্ষ recorded as its explanatory synonym.
- Plausible alternatives: সত্যচিহ্নিত সূত্র was considered for signed formula; চিহ্নিত সূত্র is shorter because the immediately adjacent definition supplies the True/False sign. সত্য-বৃক্ষ is retained as an explanatory synonym, while ট্যাবলো remains the primary token-compatible system name.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন’ express the OpenLogic sense(s) ‘tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 264 occurrence(s). Representative locations:
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:20`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:17-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:23`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:38-40` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:39`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:42-45` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:43`; final reader page pending
  - `OLP-0123` `upstream/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:34-37` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex:40`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Axioms for quantifiers]
The \emph{axioms} governing quantifiers are
all instances of the following:
\begin{align}
\ollabel{ax:q1} & \lforall[x][!B] \lif !B(t), \\
\ollabel{ax:q2} & !B(t) \lif \lexists[x][!B].
\end{align}
for any closed term~$t$.
\end{defn}
```

### BN-IN-T075

- Source term or concept: resolution method; resolution refutation; mechanization/implementation; read a satisfying structure off an open branch
- Chosen Bengali: রেজোলিউশন পদ্ধতি; রেজোলিউশন খণ্ডন; যান্ত্রিক প্রয়োগ/রূপায়ণ; খোলা শাখা থেকে পরিতৃপ্তিকারী গঠন পড়ে নেওয়া
- Rationale: The exact resolution and implementation compounds were not directly attested in the checked canon. Resolution is transliterated to avoid conflating its formal inference operation with ordinary সমাধান. খণ্ডন marks a derivation aimed at contradiction. In the tableau discussion, পড়ে নেওয়া is explicitly conditional on saturation of the open branch and therefore does not claim that an arbitrary unfinished branch already determines a satisfying structure.
- Plausible alternatives: সমাধান পদ্ধতি was rejected for resolution because it suggests ordinary problem solving rather than the formal resolution rule. অসিদ্ধি-প্রমাণ was considered for refutation; খণ্ডন directly marks derivation of contradiction and remains provisional.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘রেজোলিউশন পদ্ধতি; রেজোলিউশন খণ্ডন; যান্ত্রিক প্রয়োগ/রূপায়ণ; খোলা শাখা থেকে পরিতৃপ্তিকারী গঠন পড়ে নেওয়া’ express the OpenLogic sense(s) ‘resolution method; resolution refutation; mechanization/implementation; read a satisfying structure off an open branch’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0064` `upstream/content/first-order-logic/proof-systems/introduction.tex:38-48` → `bn-Beng-IN/content/first-order-logic/proof-systems/introduction.tex:40`; final reader page pending
  - `OLP-0064` `upstream/content/first-order-logic/proof-systems/introduction.tex:38-48` → `bn-Beng-IN/content/first-order-logic/proof-systems/introduction.tex:41`; final reader page pending
  - `OLP-0064` `upstream/content/first-order-logic/proof-systems/introduction.tex:50-71` → `bn-Beng-IN/content/first-order-logic/proof-systems/introduction.tex:52`; final reader page pending
  - `OLP-0067` `upstream/content/first-order-logic/proof-systems/tableaux.tex:72-87` → `bn-Beng-IN/content/first-order-logic/proof-systems/tableaux.tex:82`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Other !!{derivation} systems have been developed with the aim of
making it easier to construct !!{derivation}s or easier to understand
!!{derivation}s once they are complete.  Examples are natural
deduction, truth trees, also known as tableaux proofs, and the sequent
calculus.  Some !!{derivation} systems are designed especially with
mechanization in mind, e.g., the resolution method is easy to
implement in software (but its !!{derivation}s are essentially
impossible to understand). Most of these other !!{derivation} systems
represent !!{derivation}s as trees of !!{formula}s rather than
sequences. This makes it easier to see which parts of !!a{derivation}
depend on which other parts.
```

### BN-IN-T076

- Source term or concept: antecedent; succedent; associated sentence of a sequent; sequence concatenation
- Chosen Bengali: পূর্বাংশ; উত্তরাংশ; সিকোয়েন্টের সংশ্লিষ্ট বাক্য; অনুক্রমের সংযুক্তি
- Rationale: The checked logic pages support sentence, connective and implication prose but do not directly attest the names of the two sequent sides. The adjacent definition fixes পূর্বাংশ as the finite sequence left of the sequent sign and উত্তরাংশ as the finite sequence right of it. The associated sentence is the implication from the left conjunction to the right disjunction, with the displayed empty-side conventions. সংযুক্তি joins two sequences in their given order rather than forming a set union.
- Plausible alternatives: পূর্বপক্ষ/উত্তরপক্ষ were considered, but those terms can suggest argument roles; পূর্বাংশ/উত্তরাংশ directly name the two printed parts of one sequent. সংযোজন was considered for concatenation; সংযুক্তি is retained to distinguish ordered sequence joining from logical conjunction.
- Status: provisional-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পূর্বাংশ; উত্তরাংশ; সিকোয়েন্টের সংশ্লিষ্ট বাক্য; অনুক্রমের সংযুক্তি’ express the OpenLogic sense(s) ‘antecedent; succedent; associated sentence of a sequent; sequence concatenation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0077` `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:45-67` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:69`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:18-48` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:26`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:76-108` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:69`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:110-152` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:104`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:18-26` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:24`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Because of the contraction, weakening, and exchange rules, the order
and number of !!{sentence}s in~$\Gamma_0'$ does not matter: if a
sequent $\Gamma_0' \Sequent !A$ is !!{derivable}, then so is
$\Gamma_0'' \Sequent !A$ for any $\Gamma_0''$ that contains the same
!!{sentence}s as~$\Gamma_0'$.  For instance, if $\Gamma_0 = \{!B, !C\}$
then both $\Gamma_0' = \tuple{!B, !B, !C}$ and $\Gamma_0'' =
\tuple{!C, !C, !B}$ are sequences containing just the !!{sentence}s
in~$\Gamma_0$. If a sequent containing one is !!{derivable}, so is the
other, e.g.:
\begin{prooftree}
  \AxiomC{}
  \Deduce$!B, !B, !C \fCenter !A$
  \RightLabel{\LeftR{\Contraction}}
  \UnaryInf$!B, !C \fCenter !A$
  \RightLabel{\LeftR{\Exchange}}
  \UnaryInf$!C, !B \fCenter !A$
  \RightLabel{\LeftR{\Weakening}}
  \UnaryInf$!C, !C, !B \fCenter !A$
\end{prooftree}
From now on we'll say that if $\Gamma_0$ is a finite set of
!!{sentence}s then $\Gamma_0 \Sequent !A$ is any sequent where the
antecedent is a sequence of !!{sentence}s in~$\Gamma_0$ and tacitly include
contractions, exchanges, and weakenings if necessary.
```

### BN-IN-T077

- Source term or concept: logical rule; structural rule; upper/lower sequent; left/right rule
- Chosen Bengali: যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি
- Rationale: The sources support logical connective and proof prose, while the complete sequent-rule compounds remain provisional. A logical rule is named for the principal connective or quantifier introduced in its lower conclusion. A structural rule rearranges, duplicates, removes or adds surrounding sequence material. Upper and lower refer to the printed premise/conclusion positions, and left/right refer to the side containing the principal formula.
- Plausible alternatives: রূপগত বিধি was considered for structural rule; গঠনগত বিধি better marks changes to sequent arrangement without implying ordinary linguistic morphology. বাম/ডান বিধি were possible forms; বাঁ/ডান continues the edition’s established side vocabulary.
- Status: provisional-rule-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি’ express the OpenLogic sense(s) ‘logical rule; structural rule; upper/lower sequent; left/right rule’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 95 occurrence(s). Representative locations:
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:58-80` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:61`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:32-35` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:28`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:166-170` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:154`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:166-170` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:156`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:44-64` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:50`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The other axiom involving just~$\lif$ is \olref[prp]{ax:lif2}, i.e.,
\[
(!A \lif (!B \lif !C)) \lif ((!A \lif !B) \lif (!A \lif !C))
\]
We could get to the last nested conditional by applying \MP{}
twice. Again, that would mean that we want an instance of
\olref[prp]{ax:lif2} where $!A \lif !C$ is $!D \lif !D$, the !!{formula} we
are aiming for. Then of course, $!A$ and $!C$ are both~$!D$. How
should we pick~$!B$ so that both $!A \lif (!B \lif !C)$ and $!A \lif
!B$, i.e., in our case $!D \lif (!B \lif !D)$ and $!D \lif !B$, are
also !!{derivable}? Well, the first of these is already an instance of
\olref[prp]{ax:lif1}, whatever we decide $!B$ to be. And $!D \lif !B$ would
be another instance of \olref[prp]{ax:lif1} if $!B$ were $(!D \lif !D)$.
So, our !!{derivation} is:
\begin{derivation}
  1. & $!D \lif ((!D \lif !D) \lif !D)$ & \olref[prp]{ax:lif1}\\
  2. & $(!D \lif ((!D \lif !D) \lif !D)) \lif {}$\\
  & \qquad $((!D \lif (!D \lif !D)) \lif (!D \lif !D))$ & \olref[prp]{ax:lif2}\\
  3. & $(!D \lif (!D \lif !D)) \lif (!D \lif !D)$ & 1, 2, \MP\\
  4. & $!D \lif (!D \lif !D)$ & \olref[prp]{ax:lif1}\\
  5. & $!D \lif !D$ & 3, 4, \MP
\end{derivation}
\end{ex}
```

### BN-IN-T078

- Source term or concept: quantifier rule; eigenvariable/eigenvariable condition; closed term
- Chosen Bengali: পরিমাণসূচকের বিধি; আইগেনচল/আইগেনচল-শর্ত; বদ্ধ পদ
- Rationale: P009 and P010 directly support quantification discourse but not eigenvariable terminology. আইগেনচল retains the international technical stem and the source footnote records that the displayed symbol is formally a constant. The definition controls freshness: the constant cannot occur in the lower sequent, equivalently nowhere outside the displayed A(a) in the upper sequent. The instantiating term t remains closed but has no analogous freshness restriction.
- Plausible alternatives: আইগেন ভেরিয়েবল was considered as a full loan; আইগেনচল combines the international technical stem with the established Bengali variable root. মুক্ত ধ্রুবক was rejected because the condition requires absence from the lower sequent, not merely freedom from a quantifier.
- Status: provisional-quantifier-rule-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিমাণসূচকের বিধি; আইগেনচল/আইগেনচল-শর্ত; বদ্ধ পদ’ express the OpenLogic sense(s) ‘quantifier rule; eigenvariable/eigenvariable condition; closed term’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 113 occurrence(s). Representative locations:
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:20`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:23-30` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:23`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:40`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:17-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:23`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:38-40` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:39`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Axioms for quantifiers]
The \emph{axioms} governing quantifiers are
all instances of the following:
\begin{align}
\ollabel{ax:q1} & \lforall[x][!B] \lif !B(t), \\
\ollabel{ax:q2} & !B(t) \lif \lexists[x][!B].
\end{align}
for any closed term~$t$.
\end{defn}
```

### BN-IN-T079

- Source term or concept: contraction; exchange; cut; inference line; LK derivation/end-sequent
- Chosen Bengali: সংকোচন; অদলবদল; কর্তন; অনুমান-রেখা; LK-নিষ্পাদন/অন্তিম সিকোয়েন্ট
- Rationale: The checked proof page supports mathematical proof prose but does not directly attest these sequent-calculus labels. The displayed rules control each sense: contraction combines duplicate occurrences, exchange swaps adjacent occurrences, and cut removes the linking formula while combining the remaining contexts. An LK derivation is the finite rule tree in the definition, and its unique bottommost node is the end-sequent.
- Plausible alternatives: সঙ্কোচন is an orthographic variant; সংকোচন follows the edition’s normalized spelling. ছেদন was considered for cut, but কর্তন keeps this proof rule distinct from the already established set-theoretic lower-cut vocabulary.
- Status: provisional-structural-rule-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংকোচন; অদলবদল; কর্তন; অনুমান-রেখা; LK-নিষ্পাদন/অন্তিম সিকোয়েন্ট’ express the OpenLogic sense(s) ‘contraction; exchange; cut; inference line; LK derivation/end-sequent’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 54 occurrence(s). Representative locations:
  - `OLP-0097` `upstream/content/first-order-logic/natural-deduction/soundness-identity.tex:23-45` → `bn-Beng-IN/content/first-order-logic/natural-deduction/soundness-identity.tex:47`; final reader page pending
  - `OLP-0068` `upstream/content/first-order-logic/proof-systems/axiomatic-deduction.tex:46-64` → `bn-Beng-IN/content/first-order-logic/proof-systems/axiomatic-deduction.tex:60`; final reader page pending
  - `OLP-0074` `upstream/content/first-order-logic/sequent-calculus/derivations.tex:23-35` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/derivations.tex:32`; final reader page pending
  - `OLP-0074` `upstream/content/first-order-logic/sequent-calculus/derivations.tex:37-119` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/derivations.tex:57`; final reader page pending
  - `OLP-0077` `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:45-67` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Suppose the last inference in !!a{derivation} is \Elim{\eq}, i.e., the
!!{derivation} has the following form:
\begin{prooftree}
  \AxiomC{$\Gamma_1$}
  \RightLabel{$\delta_1$}
  \DeduceC{$\eq[t_1][t_2]$}
  \AxiomC{$\Gamma_2$}
  \RightLabel{$\delta_2$}
  \DeduceC{$!A(t_1)$}
  \RightLabel{\Elim{\eq}}
  \BinaryInfC{$!A(t_2)$}
\end{prooftree}
The premises $\eq[t_1][t_2]$ and $!A(t_1)$ are !!{derive}d from
!!{undischarged} assumptions~$\Gamma_1$ and $\Gamma_2$, respectively.
We want to show that $!A(t_2)$ follows from $\Gamma_1 \cup \Gamma_2$.
Consider !!a{structure}~$\Struct{M}$ with $\Sat{M}{\Gamma_1 \cup
  \Gamma_2}$. By induction hypothesis, $\Sat{M}{!A(t_1)}$ and
$\Sat{M}{\eq[t_1][t_2]}$. Therefore, $\Value{t_1}{M} = \Value{t_2}{M}$. Let
$s$ be any variable assignment, and $m = \Value{t_1}{M} = \Value{t_2}{M}$. By
\olref[fol][syn][ext]{prop:ext-formulas}, $\Sat{M}{!A(t_1)}[s]$ iff
$\Sat{M}{!A(x)}[\Subst{s}{m}{x}]$ iff $\Sat{M}{!A(t_2)}[s]$. Since
$\Sat{M}{!A(t_1)}$, we have $\Sat{M}{!A(t_2)}$.
\end{proof}
```

### BN-IN-T080

- Source term or concept: proof search; apply a rule backwards; split into branches; finish at an initial sequent
- Chosen Bengali: প্রমাণ-অন্বেষণ; বিধি উল্টো দিকে প্রয়োগ; শাখায় ভাগ; প্রারম্ভিক সিকোয়েন্টে শেষ করা
- Rationale: The checked logic and proof pages support the surrounding register but do not directly attest proof-search vocabulary. প্রমাণ-অন্বেষণ denotes constructing a derivation from its desired end-sequent upward. Applying a rule উল্টো দিকে therefore means inferring possible premises from the displayed conclusion, while branch splitting and termination are governed by the proof trees themselves.
- Plausible alternatives: প্রমাণ অনুসন্ধান was considered; প্রমাণ-অন্বেষণ is kept as a compact provisional compound for the algorithmic search activity. বিধি পশ্চাৎমুখে প্রয়োগ was possible; উল্টো দিকে প্রয়োগ is clearer in the worked bottom-to-top diagrams.
- Status: provisional-pedagogical-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রমাণ-অন্বেষণ; বিধি উল্টো দিকে প্রয়োগ; শাখায় ভাগ; প্রারম্ভিক সিকোয়েন্টে শেষ করা’ express the OpenLogic sense(s) ‘proof search; apply a rule backwards; split into branches; finish at an initial sequent’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0076` `upstream/content/first-order-logic/sequent-calculus/proving-things-quant.tex:31-83` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things-quant.tex:42`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:54-74` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:61`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:158-215` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:161`; final reader page pending
  - `OLP-0103` `upstream/content/first-order-logic/tableaux/proving-things.tex:76-171` → `bn-Beng-IN/content/first-order-logic/tableaux/proving-things.tex:95`; final reader page pending
  - `OLP-0099` `upstream/content/first-order-logic/tableaux/rules-and-proofs.tex:33-42` → `bn-Beng-IN/content/first-order-logic/tableaux/rules-and-proofs.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Starting as usual, we write
\begin{prooftree}
\AxiomC{}
\UnaryInf$\lexists[x][\lnot !A(x)] \fCenter \lnot \lforall[x][!A(x)]$
\end{prooftree}
We could either carry out the \LeftR{\exists} rule or the \RightR{\lnot}
rule. Since the \LeftR{\exists} rule is subject to the eigenvariable
condition, it's a good idea to take care of it sooner rather than
later, so we'll do that one first.
\begin{prooftree}
\AxiomC{}
\UnaryInf$ \lnot !A(a) \fCenter \lnot \lforall[x][!A(x)]$
\RightLabel{\LeftR{\lexists}}
\UnaryInf$ \lexists[x][\lnot !A(x)] \fCenter \lnot \lforall[x][!A(x)]$
\end{prooftree}
Applying the \LeftR{\lnot} and \RightR{\lnot} rules backwards, we get
\begin{prooftree}
\AxiomC{}
\UnaryInf$\lforall[x][!A(x)] \fCenter !A(a)$
\RightLabel{\LeftR{\lnot}}
\UnaryInf$\lnot !A(a), \lforall[x][!A(x)] \fCenter $
\RightLabel{\LeftR{\Exchange}}
\UnaryInf$\lforall[x][!A(x)], \lnot !A(a) \fCenter $
\RightLabel{\RightR{\lnot}}
\UnaryInf$ \lnot !A(a) \fCenter \lnot \lforall[x] !A(x)$
\RightLabel{\LeftR{\lexists}}
\UnaryInf$ \lexists[x] \lnot !A(x) \fCenter \lnot \lforall[x] !A(x)$
\end{prooftree}
At this point, our only option is to carry out the \LeftR{\forall}
rule. Since this rule is not subject to the eigenvariable restriction,
we're in the clear. Remember, we want to try and obtain an initial
sequent (of the form $!A(a) \Sequent !A(a)$), so we should choose $a$
as our argument for $!A$ when we apply the rule.
\begin{prooftree}
\Axiom$!A(a) \fCenter !A(a)$
\RightLabel{\LeftR{\lforall}}
\UnaryInf$\lforall[x][!A(x)] \fCenter !A(a)$
\RightLabel{\LeftR{\lnot}}
\UnaryInf$\lnot !A(a), \lforall[x][!A(x)] \fCenter $
\RightLabel{\LeftR{\Exchange}}
\UnaryInf$\lforall[x][!A(x)], \lnot !A(a) \fCenter $
\RightLabel{\RightR{\lnot}}
\UnaryInf$ \lnot !A(a) \fCenter \lnot \lforall[x][!A(x)]$
\RightLabel{\LeftR{\lexists}}
\UnaryInf$ \lexists[x][ \lnot !A(x)] \fCenter \lnot \lforall[x][!A(x)]$
\end{prooftree}
It is important, especially when dealing with quantifiers, to double
check at this point that the eigenvariable condition has not been
violated. Since the only rule we applied that is subject to the
eigenvariable condition was \LeftR{\exists}, and the eigenvariable~$a$
does not occur in its lower sequent (the end-sequent), this is a
correct !!{derivation}.
\end{ex}
```

### BN-IN-T081

- Source term or concept: provability/derivability relation; theorem; reflexivity; monotonicity; transitivity; compactness
- Chosen Bengali: প্রমাণযোগ্যতা/নিষ্পাদনযোগ্যতা-সম্পর্ক; উপপাদ্য; প্রতিবিম্ব ধর্ম; একঘেয়েতা; পরিযায়িতা; সংহতি
- Rationale: The checked sources support proposition, proof and relation prose but not the full metalogical terminology. Each term is governed by its adjacent LK definition: theorem means derivability from an empty antecedent; reflexivity, monotonicity and transitivity state the displayed closure properties of Proves; compactness says a finite premise subset witnesses derivability or inconsistency.
- Plausible alternatives: সিদ্ধতা was considered for provability, but প্রমাণযোগ্যতা avoids collision with semantic truth and remains paired with the existing নিষ্পাদনযোগ্য token rendering. সংহততা was considered for compactness; সংহতি is retained provisionally and is fixed by the finite-witness clauses rather than by topological usage.
- Status: provisional-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রমাণযোগ্যতা/নিষ্পাদনযোগ্যতা-সম্পর্ক; উপপাদ্য; প্রতিবিম্ব ধর্ম; একঘেয়েতা; পরিযায়িতা; সংহতি’ express the OpenLogic sense(s) ‘provability/derivability relation; theorem; reflexivity; monotonicity; transitivity; compactness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 195 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:11-11` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:11`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:13-16` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:13`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:16-16` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:16`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:46-47` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:46`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:49-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:48`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{The Deduction Theorem with Quantifiers}
```

### BN-IN-T082

- Source term or concept: propositional facts about provability; modus ponens; shared sequent context
- Chosen Bengali: বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ
- Rationale: Connective and proof vocabulary is supported by the checked pages, while the complete compound remains provisional. The displayed derivations fix the intended facts for conjunction, disjunction and the material conditional. অভিন্ন সিকোয়েন্ট-প্রসঙ্গ names the identical antecedent and succedent material required in both premises of the additive right-conjunction rule; it does not mean formula identity.
- Plausible alternatives: সাধারণ প্রসঙ্গ was considered for shared context; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ emphasizes literal equality of the two premise contexts. The modus-ponens loan is retained under T070 because no checked page directly attested a stable Bengali replacement.
- Status: provisional-rule-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ’ express the OpenLogic sense(s) ‘propositional facts about provability; modus ponens; shared sequent context’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 20 occurrence(s). Representative locations:
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:36-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:36`; final reader page pending
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:41-41` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:41`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:27`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:38`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:44`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Modus ponens]
  If $!B$ and $!B \lif !A$ already occur in !!a{derivation}, then $!A$ is
  a correct inference step.
\end{defn}
```

### BN-IN-T083

- Source term or concept: strong generalization; fresh constant; quantifier provability facts
- Chosen Bengali: প্রবল সাধারণীকরণ; নতুন ধ্রুবক; পরিমাণসূচক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য
- Rationale: Quantification and proof discourse is supported, but the theorem label is not directly attested. Strong generalization promotes a derivation of A(c) to a universal conclusion only when c occurs in neither the premise set nor A(x). নতুন ধ্রুবক is descriptive of this freshness condition and is kept distinct from an arbitrary closed term.
- Plausible alternatives: সবল সাধারণীকরণ was considered; প্রবল সাধারণীকরণ follows the existing প্রবল আরোহ register. তাজা ধ্রুবক is a common technical calque; নতুন ধ্রুবক is used descriptively because the adjacent occurrence condition gives the exact meaning.
- Status: provisional-quantifier-metatheory; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রবল সাধারণীকরণ; নতুন ধ্রুবক; পরিমাণসূচক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য’ express the OpenLogic sense(s) ‘strong generalization; fresh constant; quantifier provability facts’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:13-30` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:24`; final reader page pending
  - `OLP-0186` `upstream/content/model-theory/basics/overspill.tex:17-26` → `bn-Beng-IN/content/model-theory/basics/overspill.tex:18`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
Part of the challenge in proving the completeness theorem is that the
model we construct from a complete consistent set~$\Gamma$ must make
all the quantified !!{formula}s in~$\Gamma$ true.  In order to
guarantee this, we use a trick due to Leon Henkin.  In essence, the
trick consists in expanding the language by infinitely many !!{constant}s
and adding, for each !!{formula} with one free !!{variable} $!A(x)$ a
formula of the form
\iftag{prvEx}
      {$\lexists[x][!A(x)] \lif !A(c)$}
      {$\lnot\lforall[x][!A(x)] \lif \lnot !A(c)$},
where $c$ is one of the new !!{constant}s.  When we construct the
!!{structure} satisfying~$\Gamma$, this will guarantee that each
\iftag{prvEx}
{true existential sentence has a witness}
{false universal sentence has a counterexample}
among the new constants.
\end{explain}
```

### BN-IN-T084

- Source term or concept: valid sequent; satisfy a sequent; soundness induction; induction hypothesis; variable assignment
- Chosen Bengali: বৈধ সিকোয়েন্ট; সিকোয়েন্ট পরিতৃপ্ত করা; বিশুদ্ধতার আরোহ-প্রমাণ; আরোহের অনুমান; চলরাশি-আরোপ
- Rationale: Earlier decisions govern validity, satisfaction and soundness; this entry fixes their sequent-specific composition. A structure or valuation satisfies a sequent when some antecedent is false or some succedent is true, and validity quantifies over every such interpretation. The proof inducts on the number of inference steps, so আরোহের অনুমান applies to the strictly shorter premise derivations. চলরাশি-আরোপ is reserved for first-order assignments, distinct from propositional সত্যমান-আরোপ.
- Plausible alternatives: আরোহের প্রকল্প appeared in the initial draft, but প্রকল্প means plan or project; আরোহের অনুমান expresses induction hypothesis directly. চল-নির্দেশ was considered for variable assignment; চলরাশি-আরোপ parallels propositional সত্যমান-আরোপ while keeping the domains distinct.
- Status: provisional-semantics-proof-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বৈধ সিকোয়েন্ট; সিকোয়েন্ট পরিতৃপ্ত করা; বিশুদ্ধতার আরোহ-প্রমাণ; আরোহের অনুমান; চলরাশি-আরোপ’ express the OpenLogic sense(s) ‘valid sequent; satisfy a sequent; soundness induction; induction hypothesis; variable assignment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 73 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:25-48` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:34`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:75-95` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:81`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:34-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:37`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:68-77` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:70`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:68-77` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:72`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the inductive step, suppose again that the !!{derivation} of $!B$
from $\Gamma \cup \{!A\}$ ends with a step~$!B$ which is justified by
an inference rule. If the inference rule is modus ponens, we proceed
as in the proof of \olref[ded]{thm:deduction-thm}. If the inference
rule is \QR, we know that $!B \ident !C \lif \lforall[x][!D(x)]$ and
!!a{formula} of the form $!C \lif !D(a)$ appears earlier in the
!!{derivation}, where $a$ does not occur in~$!C$, $!A$, or $\Gamma$. We
thus have that
\begin{align*}
  \Gamma \cup \{!A\} & \Proves !C \lif !D(a),\\
  \intertext{and the induction hypothesis applies, i.e., we have that}
    \Gamma & \Proves !A \lif (!C \lif !D(a)).\\
  \intertext{By}
  & \Proves (!A \lif (!C \lif !D(a))) \lif ((!A \land !C) \lif !D(a))\\
  \intertext{and modus ponens we get}
  \Gamma & \Proves (!A \land !C) \lif !D(a).\\
  \intertext{Since the eigenvariable condition still applies, we can add a step to this !!{derivation} justified by \QR, and get}
    \Gamma & \Proves (!A \land !C) \lif \lforall[x][!D(x)].\\
    \intertext{We also have}
    & \Proves ((!A \land !C) \lif \lforall[x][!D(x)]) \lif (!A \lif (!C \lif \lforall[x][!D(x)]),\\
    \intertext{so by modus ponens,}
    \Gamma & \Proves !A \lif (!C \lif \lforall[x][!D(x)]),
\end{align*}
i.e., $\Gamma \Proves !B$.
```

### BN-IN-T085

- Source term or concept: identity/equality rules; substitutability of identicals; Leibniz's Law; symmetry and transitivity
- Chosen Bengali: অভিন্নতা/সমতার বিধি; অভিন্ন বস্তুর প্রতিস্থাপনযোগ্যতা; লাইবনিজের সূত্র; প্রতিসাম্য ও পরিযায়িতা
- Rationale: The checked relation and equality pages support identity/equality, symmetry and transitivity roots, while the proof-rule compounds and Leibniz label remain provisional. অভিন্নতা names the logical predicate's intended relation; সমতা is retained around the equality symbol and ordinary equations. The two displayed rules allow substitution in either direction under a true identity premise.
- Plausible alternatives: অভেদ was considered for identity; অভিন্নতা continues the established identity-relation vocabulary, while ordinary displayed equations retain সমতা. লাইবনিজের নিয়ম was possible; লাইবনিজের সূত্র is retained provisionally for the source label Leibniz’s Law.
- Status: mixed-attested-roots-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অভিন্নতা/সমতার বিধি; অভিন্ন বস্তুর প্রতিস্থাপনযোগ্যতা; লাইবনিজের সূত্র; প্রতিসাম্য ও পরিযায়িতা’ express the OpenLogic sense(s) ‘identity/equality rules; substitutability of identicals; Leibniz's Law; symmetry and transitivity’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 22 occurrence(s). Representative locations:
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:33-38` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:32`; final reader page pending
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:40-46` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:39`; final reader page pending
  - `OLP-0133` `upstream/content/first-order-logic/completeness/identity.tex:9-10` → `bn-Beng-IN/content/first-order-logic/completeness/identity.tex:10`; final reader page pending
  - `OLP-0096` `upstream/content/first-order-logic/natural-deduction/identity.tex:36-38` → `bn-Beng-IN/content/first-order-logic/natural-deduction/identity.tex:37`; final reader page pending
  - `OLP-0097` `upstream/content/first-order-logic/natural-deduction/soundness-identity.tex:23-45` → `bn-Beng-IN/content/first-order-logic/natural-deduction/soundness-identity.tex:47`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}
\ollabel{noidentity-ls} If $\Gamma$ is a consistent set of !!{sentence}s
in the language of first-order logic without identity, then it has
!!a{denumerable} model, i.e., it is satisfiable in !!a{structure}
whose domain is infinite and !!{enumerable}.
\end{thm}
```

### BN-IN-T086

- Source term or concept: natural-deduction derivation tree; branch; inference premise and conclusion; subderivation/subproof
- Chosen Bengali: স্বাভাবিক নিষ্পাদন-বৃক্ষ; শাখা; অনুমানের পূর্বধারণা ও সিদ্ধান্ত; উপ-নিষ্পাদন/উপপ্রমাণ
- Rationale: The checked logic and proof pages support the surrounding university register but do not directly attest the complete natural-deduction tree vocabulary. A derivation is a finite tree whose top sentences are assumptions; each lower node follows from one to three premise nodes by an inference and the bottom sentence is its conclusion. উপ-নিষ্পাদন is used where the derivation token remains explicit, while উপপ্রমাণ is the smoother prose form for the temporary proof beneath a discharge rule.
- Plausible alternatives: প্রমাণ-বৃক্ষ was considered; নিষ্পাদন-বৃক্ষ preserves the established rendering of the formal derivation object while the surrounding prose still calls it a proof. উপ-নিষ্পাদন is retained where the semantic derivation token is explicit; উপপ্রমাণ is used for fluent prose about the temporary proof governed by a discharge rule.
- Status: provisional-tree-structure-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাভাবিক নিষ্পাদন-বৃক্ষ; শাখা; অনুমানের পূর্বধারণা ও সিদ্ধান্ত; উপ-নিষ্পাদন/উপপ্রমাণ’ express the OpenLogic sense(s) ‘natural-deduction derivation tree; branch; inference premise and conclusion; subderivation/subproof’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 132 occurrence(s). Representative locations:
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:98-114` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:95`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:116-147` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:124`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:149-176` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:148`; final reader page pending
  - `OLP-0085` `upstream/content/first-order-logic/natural-deduction/rules-and-proofs.tex:26-29` → `bn-Beng-IN/content/first-order-logic/natural-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0095` `upstream/content/first-order-logic/natural-deduction/soundness.tex:130-153` → `bn-Beng-IN/content/first-order-logic/natural-deduction/soundness.tex:130`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In each of the two branches on the right, we want to !!{derive} $!A
\lif !B$, which is best done using \Intro{\lif}.
\begin{prooftree}
\AxiomC{$\Discharge{\lnot !A \lor !B}{1}$}
\AxiomC{$\Discharge{\lnot !A}{2}, \Discharge{!A}{3}$}
\DeduceC{$!B$}
\DischargeRule{\Intro{\lif}}{3}
\UnaryInfC{$!A \lif !B$}
\AxiomC{$\Discharge{!B}{2}, \Discharge{!A}{4}$}
\DeduceC{$!B$}
\DischargeRule{\Intro{\lif}}{4}
\UnaryInfC{$!A \lif !B$}
\DischargeRule{\Elim{\lor}}{2}
\TrinaryInfC{$!A \lif !B$}
\DischargeRule{\Intro{\lif}}{1}
\UnaryInfC{$(\lnot !A \lor !B) \lif (!A \lif !B)$}
\end{prooftree}
```

### BN-IN-T087

- Source term or concept: natural-deduction eigenvariable condition; discharged A(a) assumption; major existential premise; freshness
- Chosen Bengali: স্বাভাবিক নিষ্পাদনের আইগেনচল-শর্ত; অবমুক্তযোগ্য A(a) অনুমিতি; প্রধান অস্তিত্বসূচক পূর্বধারণা; নতুনত্ব
- Rationale: P009 and P010 support quantifier and scope language but do not directly attest eigenvariable terminology. In universal introduction the eigenconstant may occur in the displayed A(a) premise but not in the conclusion or any undischarged assumption. In existential elimination it may occur in the special A(a) assumption but not in the major existential premise, the conclusion or any other undischarged assumption. The rule-specific wording prevents the frozen source's false blanket claim that the eigenvariable occurs in no premise.
- Plausible alternatives: নতুন চল was considered, but the source explicitly notes that the displayed eigenvariable is formally a constant; আইগেনচল preserves the established technical label. A blanket পূর্বধারণায় অনুপস্থিত phrasing was rejected because the eigenconstant necessarily occurs in the displayed A(a) premise; the Bengali wording enumerates the forbidden contexts rule by rule.
- Status: provisional-rule-specific-freshness; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাভাবিক নিষ্পাদনের আইগেনচল-শর্ত; অবমুক্তযোগ্য A(a) অনুমিতি; প্রধান অস্তিত্বসূচক পূর্বধারণা; নতুনত্ব’ express the OpenLogic sense(s) ‘natural-deduction eigenvariable condition; discharged A(a) assumption; major existential premise; freshness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0087` `upstream/content/first-order-logic/natural-deduction/quantifier-rules.tex:58-61` → `bn-Beng-IN/content/first-order-logic/natural-deduction/quantifier-rules.tex:59`; final reader page pending
  - `OLP-0101` `upstream/content/first-order-logic/tableaux/quantifier-rules.tex:79-107` → `bn-Beng-IN/content/first-order-logic/tableaux/quantifier-rules.tex:81`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The condition that an eigenvariable neither occur in the premises nor
in any assumption that is !!{undischarged} in the !!{derivation}s
leading to the premises for the \Intro{\lforall} or \Elim{\lexists}
inference is called the \emph{eigenvariable condition}.
```

### BN-IN-T088

- Source term or concept: rule-applicable signed formula; check off with a check mark; branch-splitting rule; repeat a quantified rule with a closed term
- Chosen Bengali: বিধি প্রয়োগের উপযোগী চিহ্নিত সূত্র; টিকচিহ্ন দেওয়া; শাখা-বিভাজক বিধি; বদ্ধ পদ দিয়ে বিধিটি কয়েকবার প্রয়োগ
- Rationale: The checked logic and proof pages support formula, rule and proof prose but do not directly attest the operational tableau vocabulary. A signed formula is eligible when its unique governing rule can still be applied on an open branch. A check mark records that the rule has been applied on every open branch containing that occurrence; it is a construction aid rather than part of the formal tableau. Branch-splitting names rules with two successor branches. The quantified rules without an eigenvariable condition may need repeated applications, but each instantiating term remains closed.
- Plausible alternatives: চিহ্নিত সূত্র পরীক্ষা করা was considered for check off; টিকচিহ্ন দেওয়া matches the literal construction mark and keeps it distinct from semantic verification. শাখাকারী বিধি was considered; শাখা-বিভাজক বিধি states the two-successor effect directly.
- Status: provisional-tableau-construction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিধি প্রয়োগের উপযোগী চিহ্নিত সূত্র; টিকচিহ্ন দেওয়া; শাখা-বিভাজক বিধি; বদ্ধ পদ দিয়ে বিধিটি কয়েকবার প্রয়োগ’ express the OpenLogic sense(s) ‘rule-applicable signed formula; check off with a check mark; branch-splitting rule; repeat a quantified rule with a closed term’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0104` `upstream/content/first-order-logic/tableaux/proving-things-quant.tex:212-315` → `bn-Beng-IN/content/first-order-logic/tableaux/proving-things-quant.tex:233`; final reader page pending
  - `OLP-0103` `upstream/content/first-order-logic/tableaux/proving-things.tex:173-299` → `bn-Beng-IN/content/first-order-logic/tableaux/proving-things.tex:170`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}
We construct !!a{tableau} for the set
\[
\sFmla{\True}{\lforall[x][!A(x)]}, \sFmla{\True}{\lforall[x][!A(x)]
  \lif \lexists[y][!B(y)]}, \sFmla{\True}{\lnot\lexists[y][!B(y)]}.
\]
Starting as usual, we write down the assumptions:
\begin{oltableau}
  [\sFmla{\True}{\lforall[x][\formula{A}(x)]}, just=\TAss
    [\sFmla{\True}{\lforall[x][\formula{A}(x)] \lif
        \lexists[y][\formula{B}(y)]}, just=\TAss
      [\sFmla{\True}{\lnot\lexists[y][\formula{B}(y)]}, just=\TAss
      ]
    ]
  ]
\end{oltableau}
We begin by applying the $\TRule{\True}{\lnot}$ rule to line~$3$. A
corollary to the rule ``always apply rules with eigenvariable
conditions first'' is ``defer applying quantifier rules without
eigenvariable conditions until needed.'' Also, defer rules that result
in a split.
\begin{oltableau}
  [\sFmla{\True}{\lforall[x][\formula{A}(x)]}, just=\TAss
    [\sFmla{\True}{\lforall[x][\formula{A}(x)] \lif
        \lexists[y][\formula{B}(y)]}, just=\TAss
      [\sFmla{\True}{\lnot\lexists[y][\formula{B}(y)]}, just=\TAss, checked
        [\sFmla{\False}{\lexists[y][\formula{B}(y)]}, just={\TRule{\True}{\lnot}[3]}]
      ]
    ]
  ]
\end{oltableau}
The new line~$4$ requires $\TRule{\False}{\lexists}$, a quantifier
rule without the eigenvariable condition. So we defer this in favor of
using $\TRule{\True}{\lif}$ on line~$2$.
\begin{oltableau}
  [\sFmla{\True}{\lforall[x][\formula{A}(x)]}, just=\TAss
    [\sFmla{\True}{\lforall[x][\formula{A}(x)] \lif
        \lexists[y][\formula{B}(y)]}, just=\TAss, checked
      [\sFmla{\True}{\lnot\lexists[y][\formula{B}(y)]}, just=\TAss, checked
        [\sFmla{\False}{\lexists[y][\formula{B}(y)]},
          just={\TRule{\True}{\lnot}[3]},
          [\sFmla{\False}{\lforall[x][\formula{A}(x)]}, just={\TRule{\True}{\lif}[2]}]
          [\sFmla{\True}{\lexists[y][\formula{B}(y)]}, just={\TRule{\True}{\lif}[2]}]
        ]
      ]
    ]
  ]
\end{oltableau}
Both new !!{signed formula}s require rules with eigenvariable conditions, so
these should be next:
\begin{oltableau}
  [\sFmla{\True}{\lforall[x][\formula{A}(x)]}, just=\TAss
    [\sFmla{\True}{\lforall[x][\formula{A}(x)] \lif
        \lexists[y][\formula{B}(y)]}, just=\TAss, checked
      [\sFmla{\True}{\lnot\lexists[y][\formula{B}(y)]}, just=\TAss, checked
        [\sFmla{\False}{\lexists[y][\formula{B}(y)]},
          just={\TRule{\True}{\lnot}[3]}
          [\sFmla{\False}{\lforall[x][\formula{A}(x)]}, just={\TRule{\True}{\lif}[2]},checked
            [\sFmla{\False}{\formula{A}(b)}, just={\TRule{\False}{\lforall}[5]}]
          ]
          [\sFmla{\True}{\lexists[y][\formula{B}(y)]}, just={\TRule{\True}{\lif}[2]},checked
            [\sFmla{\True}{\formula{B}(c)}, just={\TRule{\True}{\lexists}[5]}]
          ]
        ]
      ]
    ]
  ]
\end{oltableau}
To close the branches, we have to use the !!{signed formula}s on lines $1$
and~$3$. The corresponding rules (\TRule{\True}{\lforall} and
\TRule{\False}{\lexists}) don't have eigenvariable conditions, so we
are free to pick whichever terms are suitable. In this case, that's
$b$ and~$c$, respectively.
\begin{oltableau}
  [\sFmla{\True}{\lforall[x][\formula{A}(x)]}, just=\TAss
    [\sFmla{\True}{\lforall[x][\formula{A}(x)] \lif
        \lexists[y][\formula{B}(y)]}, just=\TAss, checked
      [\sFmla{\True}{\lnot\lexists[y][\formula{B}(y)]}, just=\TAss, checked
        [\sFmla{\False}{\lexists[y][\formula{B}(y)]},
          just={\TRule{\True}{\lnot}[3]}
          [\sFmla{\False}{\lforall[x][\formula{A}(x)]},
            just={\TRule{\True}{\lif}[2]},checked
            [\sFmla{\False}{\formula{A}(b)},
              just={\TRule{\False}{\lforall}[5]}
              [\sFmla{\True}{\formula{A}(b)},
                just={\TRule{\True}{\lforall}[1]},close
              ]
            ]
          ]
          [\sFmla{\True}{\lexists[y][\formula{B}(y)]},
            just={\TRule{\True}{\lif}[2]},checked
            [\sFmla{\True}{\formula{B}(c)},
              just={\TRule{\True}{\lexists}[5]}
              [\sFmla{\False}{\formula{B}(c)},
                just={\TRule{\False}{\lexists}[4]},close
              ]
            ]
          ]
        ]
      ]
    ]
  ]
\end{oltableau}
\end{ex}
```

### BN-IN-T089

- Source term or concept: satisfy a signed formula; satisfiable set/branch/tableau; rule extension preserves satisfiability; unsatisfiable; contrapositive
- Chosen Bengali: চিহ্নিত সূত্রকে পরিতৃপ্ত করা; পরিতৃপ্তিযোগ্য সমষ্টি/শাখা/ট্যাবলো; বিধি-প্রসারণে পরিতৃপ্তিযোগ্যতা বজায় রাখা; অপরিতৃপ্তিযোগ্য; বিপরীত-প্রতিজ্ঞা
- Rationale: Earlier decisions fix satisfaction and soundness; this entry fixes their tableau-specific composition. A structure or valuation satisfies a true-signed formula when it satisfies its formula and a false-signed formula when it does not. A branch is satisfiable when its signed-formula set is satisfiable, and a tableau is satisfiable when at least one branch is. The soundness proof shows that each rule extension preserves some satisfiable branch, so a closed tableau cannot start from satisfiable assumptions. The final consistency corollary is proved by contrapositive.
- Plausible alternatives: সন্তুষ্টিযোগ্য and satisfiable loan forms were considered; পরিতৃপ্তিযোগ্য continues the model-theoretic satisfaction vocabulary already fixed under T066. প্রতিবিপরীতের প্রমাণ was considered for contrapositive; বিপরীত-প্রতিজ্ঞা is used in the target and the surrounding proof immediately states the negated conclusion as its assumption.
- Status: provisional-tableau-soundness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চিহ্নিত সূত্রকে পরিতৃপ্ত করা; পরিতৃপ্তিযোগ্য সমষ্টি/শাখা/ট্যাবলো; বিধি-প্রসারণে পরিতৃপ্তিযোগ্যতা বজায় রাখা; অপরিতৃপ্তিযোগ্য; বিপরীত-প্রতিজ্ঞা’ express the OpenLogic sense(s) ‘satisfy a signed formula; satisfiable set/branch/tableau; rule extension preserves satisfiability; unsatisfiable; contrapositive’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 173 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:111`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:137`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:26`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:129-140` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:134`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:21`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  \ollabel{prop:derivfacts}
\begin{enumerate}
\item $\Proves (!A \lif !B) \lif ((!B \lif !C)
  \lif (!A \lif !C)$; \ollabel{derivfacts:a}
\item If $\Gamma \cup \{ \lnot !A\}
  \Proves \lnot !B$ then $\Gamma \cup \{ !B\} \Proves
  !A$ (Contraposition); \ollabel{derivfacts:b}
\item  $\{ !A, \lnot!A\} \Proves
    !B$ (Ex Falso Quodlibet, Explosion); \ollabel{derivfacts:c}
\item  $\{ \lnot\lnot!A\} \Proves
  !A$ (Double Negation Elimination);\ollabel{derivfacts:d}
\item If $\Gamma \Proves \lnot\lnot!A$ then $\Gamma \Proves
  !A$;\ollabel{derivfacts:e}
\end{enumerate}
\end{prop}
```

### BN-IN-T090

- Source term or concept: syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations
- Chosen Bengali: নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো
- Rationale: The checked India Bengali pages support proposition, connective, quantifier and proof prose but do not directly attest these full metatheoretic compounds. নিঃসরণ উপপাদ্য is reserved here for the syntactic biconditional between derivability from Gamma union {A} and derivability of A conditional B from Gamma; T067 keeps the distinct semantic name অর্থগত নিঃসরণ উপপাদ্য. অনুমিতি নিঃসরণ describes moving the extra premise into a conditional, স্বতঃসিদ্ধের রূপ means an instance obtained from an axiom schema, and নিষ্পাদনগুলি পরপর বসানো preserves the ordered-sequence operation without colliding with logical conjunction.
- Plausible alternatives: অবরোহ উপপাদ্য and ডিডাকশন উপপাদ্য were considered; নিঃসরণ উপপাদ্য matches the movement of one premise into a conditional and remains explicitly provisional. অর্থগত নিঃসরণ উপপাদ্য is reserved under T067 for entailment; the unqualified form here is syntactic because both sides use Proves. নিষ্পাদন-সংযুক্তি was considered for concatenation; পরপর বসানো states the ordered-sequence operation directly and avoids collision with logical সংযোজন.
- Status: provisional-axiomatic-metatheory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো’ express the OpenLogic sense(s) ‘syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 20 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:11-11` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:11`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:13-16` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:13`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:16-16` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:16`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:49-52` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:48`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:97-98` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:97`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{The Deduction Theorem with Quantifiers}
```

### BN-IN-T091

- Source term or concept: complete consistent theory; axiomatizable; decidable
- Chosen Bengali: পূর্ণ সঙ্গত তত্ত্ব; স্বতঃসিদ্ধযোগ্য; নির্ণেয়
- Rationale: The checked logic, quantification and proof pages support the surrounding university register but do not directly attest these full metatheoretic compounds. A sentence set is পূর্ণ when it contains each sentence or its negation, and সঙ্গত retains the proof-theoretic sense fixed under T069. স্বতঃসিদ্ধযোগ্য means that a decidable sentence set axiomatizes the theory; নির্ণেয় means that membership can be decided effectively. The adjacent definitions govern each provisional term.
- Plausible alternatives: সিদ্ধান্তযোগ্য was considered for decidable; নির্ণেয় is shorter and the adjacent effective membership test fixes its technical sense. স্বতঃসিদ্ধায়নযোগ্য was considered; স্বতঃসিদ্ধযোগ্য states that a decidable axiom set can present the same theory.
- Status: provisional-completeness-metatheory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পূর্ণ সঙ্গত তত্ত্ব; স্বতঃসিদ্ধযোগ্য; নির্ণেয়’ express the OpenLogic sense(s) ‘complete consistent theory; axiomatizable; decidable’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:25-31` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
!!^{complete} sets of sentences leave no questions unanswered. For
any !!{sentence}~$!A$, $\Gamma$ ``says'' if $!A$ is true or false.  The
importance of !!{complete} sets extends beyond the proof of the
completeness theorem. A theory which is !!{complete} and
axiomatizable, for instance, is always decidable.
\end{explain}
```

### BN-IN-T092

- Source term or concept: Henkin expansion; saturated set; witness; counterexample
- Chosen Bengali: হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত
- Rationale: The checked proposition, quantifier and proof pages support the prose, but the Henkin-specific compounds are not directly attested. হেনকিন সম্প্রসারণ names the language extension by fresh constants. A set is সম্পৃক্ত when each true existential has a named witness or, in the alternative configuration, each false universal has a named counterexample. সাক্ষী and প্রতিদৃষ্টান্ত are fixed by those displayed membership conditions rather than by ordinary evidential senses.
- Plausible alternatives: পরিপূর্ণ সেট was considered for saturated set, but পূর্ণ is already reserved for completeness; সম্পৃক্ত distinguishes the witness property. প্রতিউদাহরণ was considered for counterexample; প্রতিদৃষ্টান্ত pairs transparently with the selected witness language in the quantified construction.
- Status: provisional-henkin-construction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত’ express the OpenLogic sense(s) ‘Henkin expansion; saturated set; witness; counterexample’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:11-11` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:11`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:13-30` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:27`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:13-30` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:28`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:39-47` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:39`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:149-158` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:153`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Henkin Expansion}
```

### BN-IN-T093

- Source term or concept: term model; Truth Lemma; covered model; factor a model by an equivalence relation
- Chosen Bengali: পদ-মডেল; সত্যতা-সহায়ক উপপাদ্য; আচ্ছাদিত মডেল; তুল্যতা সম্পর্ক দিয়ে মডেলের ভাগকরণ
- Rationale: The checked university pages directly support relation, equivalence class, partition, mapping, equality and proof roots. They do not directly attest the full model-theoretic compounds. পদ-মডেল has closed terms as its domain; আচ্ছাদিত means that every domain element is the value of a closed term. সত্যতা-সহায়ক উপপাদ্য names the induction linking satisfaction in the constructed model with membership in the complete set. ভাগকরণ is the quotient construction determined by provable identity, with representative independence proved explicitly.
- Plausible alternatives: টার্ম মডেল was considered; পদ-মডেল uses the established Bengali term root while the definition supplies its exact domain. সত্য উপপাদ্য was considered, but সত্যতা-সহায়ক উপপাদ্য avoids suggesting that the lemma itself is merely true rather than connecting truth with set membership. ভাগফল মডেল was considered; ভাগকরণ describes the construction while the equivalence-class notation remains visible.
- Status: mixed-attested-roots-and-provisional-model-theory; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পদ-মডেল; সত্যতা-সহায়ক উপপাদ্য; আচ্ছাদিত মডেল; তুল্যতা সম্পর্ক দিয়ে মডেলের ভাগকরণ’ express the OpenLogic sense(s) ‘term model; Truth Lemma; covered model; factor a model by an equivalence relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 22 occurrence(s). Representative locations:
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:15-24` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:21`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:26-29` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:25`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:128-143` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:134`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:128-143` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:138`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:145-151` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:147`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We can prove the Compactness Theorem directly, without appealing to
the Completeness Theorem, using the same ideas as in the proof of the
completeness theorem.  In the proof of the Completeness Theorem we
started with a consistent set~$\Gamma$ of !!{sentence}s, expanded it
to a consistent\iftag{FOL}{, saturated,}{} and !!{complete}
set~$\Gamma^*$ of !!{sentence}s, and then showed that in the
\iftag{FOL}{term
  model~$\Struct{M(\Gamma^*)}$}{!!{valuation}~$\pAssign{v(\Gamma^*)}$}
constructed from $\Gamma^*$, all !!{sentence}s of~$\Gamma$ are true,
so $\Gamma$ is satisfiable.
```

### BN-IN-T094

- Source term or concept: finitely satisfiable; infinitesimal; standard model of arithmetic
- Chosen Bengali: সসীমভাবে পরিতৃপ্তিযোগ্য; অতিক্ষুদ্র সংখ্যা; পাটীগণিতের প্রমিত মডেল
- Rationale: The checked logic, proof and finite/infinite-set pages support the component senses but do not directly attest the complete model-theoretic phrases. সসীমভাবে পরিতৃপ্তিযোগ্য means that every finite subset has a model. অতিক্ষুদ্র সংখ্যা is fixed by the example as positive and smaller than every positive reciprocal numeral. পাটীগণিতের প্রমিত মডেল names the natural-number interpretation contrasted with a compactness-produced nonstandard model.
- Plausible alternatives: সসীমত পরিতৃপ্তিযোগ্য was considered; সসীমভাবে পরিতৃপ্তিযোগ্য is more transparent and is fixed by the every-finite-subset clause. অণুমাত্র সংখ্যা was considered for infinitesimal; অতিক্ষুদ্র সংখ্যা directly matches the example’s positive but smaller-than-every-reciprocal condition.
- Status: provisional-compactness-application-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সসীমভাবে পরিতৃপ্তিযোগ্য; অতিক্ষুদ্র সংখ্যা; পাটীগণিতের প্রমিত মডেল’ express the OpenLogic sense(s) ‘finitely satisfiable; infinitesimal; standard model of arithmetic’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 27 occurrence(s). Representative locations:
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:26-29` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:24`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:26-29` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:26`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:31-36` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:30`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:58-63` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:59`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:58-63` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:60`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We can use the same method to show that a finitely satisfiable set of
sentences is satisfiable. We just have to prove the corresponding
versions of the results leading to the truth lemma where we replace
``consistent'' with ``finitely satisfiable.''
```

### BN-IN-T095

- Source term or concept: downward Löwenheim–Skolem theorem; countable model; Skolem's paradox
- Chosen Bengali: লোয়েনহাইম--স্কোলেম উপপাদ্য; গণনীয় মডেল; স্কোলেমের কূটাভাস
- Rationale: The checked mapping, proof and finite/infinite-set pages support countability and cardinality discourse but do not directly attest these named model-theoretic results. The section proves the downward form: an infinite theory with a model has one no larger than the countable language. গণনীয় retains the countability sense governed by T040. স্কোলেমের কূটাভাস names the apparent tension between a countable model of set theory and the model's own assertion that some internal sets are uncountable; the target explanation preserves the internal/external distinction.
- Plausible alternatives: নিম্নগামী and অধোমুখী were considered for downward; the source section title itself says only Löwenheim--Skolem, while the theorem statement makes the cardinality direction explicit. স্কোলেমের আপাতবিরোধ was considered; কূটাভাস is retained because the explanation resolves an apparent external/internal conflict rather than a formal contradiction.
- Status: provisional-model-size-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘লোয়েনহাইম--স্কোলেম উপপাদ্য; গণনীয় মডেল; স্কোলেমের কূটাভাস’ express the OpenLogic sense(s) ‘downward Löwenheim–Skolem theorem; countable model; Skolem's paradox’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:9-10` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:10`; final reader page pending
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:12-18` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:12`; final reader page pending
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:48-61` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:45`; final reader page pending
  - `OLP-0137` `upstream/content/first-order-logic/completeness/downward-ls.tex:48-61` → `bn-Beng-IN/content/first-order-logic/completeness/downward-ls.tex:54`; final reader page pending
  - `OLP-0127` `upstream/content/first-order-logic/completeness/introduction.tex:59-73` → `bn-Beng-IN/content/first-order-logic/completeness/introduction.tex:65`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{fol}{com}{dls}
\olsection{The L\"owenheim--Skolem Theorem}
```

### BN-IN-T096

- Source term or concept: formal language; first-order language; quantificational logic; predicate logic; vocabulary; expression/string
- Chosen Bengali: বিধিবদ্ধ ভাষা; প্রথম-ক্রমের ভাষা; পরিমাণসূচকীয় যুক্তিবিদ্যা; বিধেয় যুক্তিবিদ্যা; শব্দভাণ্ডার; অভিব্যক্তি/প্রতীকক্রম
- Rationale: The checked Indian Bengali logic pages directly support proposition, connective, quantification, predicate and scope discourse, while the school algebra page supports variable/constant explanatory prose. They do not directly attest every full compound. বিধিবদ্ধ ভাষা marks a language fixed by an explicit vocabulary and formation rules. প্রতীকক্রম is reserved for the ordered symbol object, while অভিব্যক্তি covers a permitted term, formula or sentence. প্রথম-ক্রমের retains the project-wide decision in T033.
- Plausible alternatives: আনুষ্ঠানিক ভাষা was considered for formal language; বিধিবদ্ধ ভাষা emphasizes that the vocabulary and formation rules explicitly regulate the symbol strings. কোয়ান্টিফায়ার যুক্তিবিদ্যা and প্রেডিকেট যুক্তিবিদ্যা were possible loans; পরিমাণসূচকীয় যুক্তিবিদ্যা and বিধেয় যুক্তিবিদ্যা retain the attested Bengali roots. স্ট্রিং was considered for string; প্রতীকক্রম states the ordered-symbol object, while অভিব্যক্তি is reserved for a permitted expression.
- Status: mixed-contextual-and-provisional-first-order-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিধিবদ্ধ ভাষা; প্রথম-ক্রমের ভাষা; পরিমাণসূচকীয় যুক্তিবিদ্যা; বিধেয় যুক্তিবিদ্যা; শব্দভাণ্ডার; অভিব্যক্তি/প্রতীকক্রম’ express the OpenLogic sense(s) ‘formal language; first-order language; quantificational logic; predicate logic; vocabulary; expression/string’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 96 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:135-149` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:137`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:44-64` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:50`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:31-39` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:35`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:13-28` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:15`; final reader page pending
  - `OLP-0140` `upstream/content/first-order-logic/introduction/first-order-logic.tex:13-31` → `bn-Beng-IN/content/first-order-logic/introduction/first-order-logic.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The \emph{double-negation translation} describes an important
relationship between classical and intuitionist logic. It is defined
inductively follows (think of $!A^N$ as the ``intuitionist''
translation of the classical !!{formula}~$!A$):
\begin{align*}
!A^N & \ident \lnot\lnot !A \quad \text{for atomic !!{formula}s $!A$} \\
(!A \land !B)^N & \ident (!A^N \land !B^N) \\
(!A \lor !B)^N & \ident  \lnot\lnot (!A^N \lor !B^N) \\
(!A \lif !B)^N & \ident (!A^N \lif !B^N) \\
(\lforall[x][!A])^N & \ident \lforall[x][!A^N] \\
(\lexists[x][!A])^N & \ident \lnot\lnot\lexists[x][!A^N]
\end{align*}
Kolmogorov and Glivenko had versions of this translation for
propositional logic; for predicate logic, it is due to G\"odel and
Gentzen, independently. We have
```

### BN-IN-T097

- Source term or concept: term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope
- Chosen Bengali: পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর
- Rationale: The quantification witness directly discusses individual variables, predicates, universal and existential quantification and scope; the school algebra witness supports the variable/constant register. The exact metalogical compounds remain governed by the chapter definitions. A sentence is a formula with no free variable occurrence. সংঘটন means a token occurrence at a position, so different occurrences of the same variable may be bound by different quantifiers. সংশ্লিষ্ট names a quantifier associated with that occurrence, while অনুরূপ identifies the corresponding token position through a recursive clause; this avoids সঙ্গত, which the edition reserves for consistency. পদ is the syntactic term category, not an algebraic monomial here.
- Plausible alternatives: আণবিক সূত্র was considered for atomic formula; পরমাণু সূত্র continues the established logical atom vocabulary and remains definition-governed. বদ্ধ সূত্র was considered for sentence, but বাক্য follows the source category while the no-free-occurrence definition prevents ordinary-language ambiguity. উপস্থিতি and আবির্ভাব were considered for occurrence; সংঘটন marks a token at a particular syntactic position. সঙ্গত was considered for both matching and corresponding, but the edition reserves that root for consistency; সংশ্লিষ্ট পরিমাণসূচক and অনুরূপ সংঘটন keep the two syntactic relations distinct. ব্যাপ্তি was considered for scope; পরিসর stays distinct from the domain term সংজ্ঞাক্ষেত্র.
- Status: mixed-attested-roots-and-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর’ express the OpenLogic sense(s) ‘term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 587 occurrence(s). Representative locations:
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:13-21` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:20`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18-29` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:17-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:23`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:38-40` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:39`; final reader page pending
  - `OLP-0125` `upstream/content/first-order-logic/axiomatic-deduction/identity.tex:42-45` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/identity.tex:43`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Axioms for quantifiers]
The \emph{axioms} governing quantifiers are
all instances of the following:
\begin{align}
\ollabel{ax:q1} & \lforall[x][!B] \lif !B(t), \\
\ollabel{ax:q2} & !B(t) \lif \lexists[x][!B].
\end{align}
for any closed term~$t$.
\end{defn}
```

### BN-IN-T098

- Source term or concept: structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment
- Chosen Bengali: গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ
- Rationale: The checked relation and mapping pages directly support relation, domain and function language, and the logic pages support truth and quantification. They do not directly attest the full Tarskian compounds. A structure supplies a nonempty domain plus denotations or interpretations of nonlogical symbols. Satisfaction for an open formula is relative to a variable assignment; the modified assignment differs at the named variable only. This keeps first-order গঠন distinct from ordinary prose uses through the adjacent formal notation.
- Plausible alternatives: কাঠামো was considered for structure; গঠন is shorter and the formal Struct notation fixes the technical sense. পরিসর was considered for domain, but সংজ্ঞাক্ষেত্র avoids collision with quantifier scope and function codomain. সন্তুষ্টি was considered for satisfaction; পরিতৃপ্তি continues T066 and is fixed by the recursive truth clauses. মূল্যায়ন was considered for assignment; আরোপ distinguishes variable assignment from propositional valuation and from the structure’s interpretation function.
- Status: mixed-attested-roots-and-provisional-semantics; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ’ express the OpenLogic sense(s) ‘structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 315 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:132`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:87-107` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:88`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:118`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:121`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:27`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
  \begin{enumerate}
    \item If $\Gamma \Proves !A$, then there is a finite sequence of
      !!{formula}s $!A_1$, \dots,~$!A_n$ so that $!A \ident !A_n$ and
      each $!A_i$ is either a logical axiom, !!a{element} of~$\Gamma$
      or follows from previous !!{formula}s by modus ponens.  Take
      $\Gamma_0$ to be those $!A_i$ which are in~$\Gamma$.  Then the
      !!{derivation} is likewise !!a{derivation} from~$\Gamma_0$, and
      so $\Gamma_0 \Proves !A$.
    \item This is the contrapositive of~(1) for the special case $!A
      \ident \lfalse$.
\end{enumerate}
\end{proof}
```

### BN-IN-T099

- Source term or concept: substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma
- Chosen Bengali: প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য
- Rationale: The checked pages support quantifier scope, variable, equality-operation, mapping and proof prose but do not directly attest the full substitution vocabulary. The introduction warns that replacing every written x is not always legitimate because binding matters. Universal instantiation removes a universal quantifier only with an admissible term instance. The later substitution lemma equates satisfaction of the substituted formula with satisfaction under the assignment modified to the term's value; its exact hypotheses govern the terminology.
- Plausible alternatives: বদলি was considered for substitution; প্রতিস্থাপন is the established operation name and works for terms and formulas. বিশেষীকরণ was considered for universal instantiation; সার্বিক নিদর্শনায়ন names formation of a particular admissible instance without suggesting an unrestricted replacement. প্রতিস্থাপন উপপাদ্য was considered; প্রতিস্থাপন-সহায়ক উপপাদ্য retains the source’s lemma status and its role in the later soundness argument.
- Status: provisional-definition-and-lemma-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য’ express the OpenLogic sense(s) ‘substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 30 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:30-65` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:56`; final reader page pending
  - `OLP-0132` `upstream/content/first-order-logic/completeness/construction-of-model.tex:99-114` → `bn-Beng-IN/content/first-order-logic/completeness/construction-of-model.tex:107`; final reader page pending
  - `OLP-0133` `upstream/content/first-order-logic/completeness/identity.tex:12-24` → `bn-Beng-IN/content/first-order-logic/completeness/identity.tex:19`; final reader page pending
  - `OLP-0146` `upstream/content/first-order-logic/introduction/substitution.tex:11-11` → `bn-Beng-IN/content/first-order-logic/introduction/substitution.tex:11`; final reader page pending
  - `OLP-0146` `upstream/content/first-order-logic/introduction/substitution.tex:30-45` → `bn-Beng-IN/content/first-order-logic/introduction/substitution.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The rules for second-order logic simply extend the quantifier rules to
the new second order variables. Here, however, one has to be a little
bit careful to explain how these variables interact with the !!{predicate}s
of~$\Lang{L}$, and with !!{formula}s of~$\Lang{L}$ more generally. At the bare
minimum, relation variables count as terms, so one has inferences of
the form
\[
!A(R) \Proves \lexists[R][!A(R)]
\]
But if $\Lang{L}$ is the language of arithmetic with a constant
relation symbol~$<$, one would also expect the following inference to
be valid:
\[
x < y \Proves \lexists[R][\Atom{R}{x,y}]
\]
or for a given !!{formula}~$!A$,
\[
!A(x_1, \dots, x_k) \Proves \lexists[R][\Atom{R}{x_1,\dots,x_k}]
\]
More generally, we might want to allow inferences of the form
\[
\Subst{!A}{\lambd[\vec x][!B(\vec x)]}{R} \Proves
\lexists[R][!A]
\]
where $\Subst{!A}{\lambd[\vec x][!B(\vec x)]}{R}$ denotes the result
of replacing every atomic !!{formula} of the form
$\Obj{R}{t_1,\dots,t_k}$ in~$!A$ by $!B(t_1, \dots, t_k)$. This last
rule is equivalent to having a {\em comprehension schema}, i.e., an
axiom of the form
\[
\lexists[R][\lforall[x_1, \dots, x_k][(!A(x_1, \dots, x_k) \liff
\Atom{R}{x_1, \dots, x_k})]],
\]
one for each !!{formula}~$!A$ in the second-order language, in which
$R$ is not a free variable. (Exercise: show that if $R$ is allowed to
occur in~$!A$, this schema is inconsistent!)
```

### BN-IN-T100

- Source term or concept: model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain
- Chosen Bengali: মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র
- Rationale: The checked university pages directly support relations, mappings, proof, finite/infinite sets and quantification, while the full model-theory compounds remain provisional. A model satisfies every sentence in the given set. Characterizing a class means that exactly the intended structures satisfy the description. Expressibility is restricted to formulas or sentence sets in the specified first-order language. T040 and T044 govern the finite and nonenumerable size vocabulary; compactness and Löwenheim–Skolem govern the stated limitations.
- Plausible alternatives: নমুনা তত্ত্ব was considered for model theory; মডেল তত্ত্ব retains the established technical loan and avoids suggesting an illustrative example. স্বতঃসিদ্ধ পদ্ধতি was considered; স্বতঃসিদ্ধমূলক পদ্ধতি states that a class is described through a set of sentences used as axioms. সুনির্দিষ্ট করা was considered for characterize; চরিত্রায়িত করা retains the exact-class sense supplied by the biconditional explanation. অভিব্যক্তিযোগ্যতা was considered for expressibility; প্রকাশযোগ্যতা states whether the specified first-order language can express the property.
- Status: mixed-attested-roots-and-provisional-model-theory; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র’ express the OpenLogic sense(s) ‘model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 174 occurrence(s). Representative locations:
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18-29` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:18`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:119`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:121`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:127`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
As we've seen, giving !!{derivation}s in an axiomatic system is
cumbersome, and !!{derivation}s may be hard to find. Rather than
actually write out long lists of !!{formula}s, it is generally easier
to argue that such !!{derivation}s exist, by making use of a few
simple results. We've already established three such results:
\olref[ptn]{prop:reflexivity} says we can always assert that $\Gamma
\Proves !A$ when we know that $!A \in
\Gamma$. \olref[ptn]{prop:monotonicity} says that if $\Gamma \Proves !A$
then also $\Gamma \cup \{!B\} \Proves !A$. And
\olref[ptn]{prop:transitivity} implies that if $\Gamma \Proves !A$ and
$!A \Proves !B$, then $\Gamma \Proves !B$. Here's another simple
result, a ``meta''-version of modus ponens:
```

### BN-IN-T101

- Source term or concept: main operator; immediate subformula; proper subformula; proper prefix
- Chosen Bengali: প্রধান অপারেটর; অব্যবহিত উপসূত্র; প্রকৃত উপসূত্র; প্রকৃত পূর্বাংশ
- Rationale: The checked logic and algebra pages support operator, formula and symbol-sequence discourse but do not directly attest all four compounds. প্রধান অপারেটর names the outermost connective or quantifier governing the recursive form. অব্যবহিত উপসূত্র is fixed by the one-step formation clauses, while প্রকৃত উপসূত্র excludes the formula itself. প্রকৃত পূর্বাংশ means a nonempty initial symbol sequence shorter than the whole expression; its length condition distinguishes it from an arbitrary substring.
- Plausible alternatives: মুখ্য অপারেটর was considered for main operator; প্রধান অপারেটর follows the chapter’s selected explanatory register and the outer-constructor definition. সরাসরি উপসূত্র was considered for immediate subformula; অব্যবহিত উপসূত্র marks exactly one formation step. যথার্থ উপসূত্র and আদি খণ্ড were considered for proper subformula and proper prefix; প্রকৃত keeps the strict exclusion parallel across both definitions.
- Status: provisional-definition-governed-syntax-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রধান অপারেটর; অব্যবহিত উপসূত্র; প্রকৃত উপসূত্র; প্রকৃত পূর্বাংশ’ express the OpenLogic sense(s) ‘main operator; immediate subformula; proper subformula; proper prefix’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
  - `OLP-0154` `upstream/content/first-order-logic/syntax-and-semantics/main-operator.tex:13-19` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/main-operator.tex:15`; final reader page pending
  - `OLP-0154` `upstream/content/first-order-logic/syntax-and-semantics/main-operator.tex:13-19` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/main-operator.tex:17`; final reader page pending
  - `OLP-0154` `upstream/content/first-order-logic/syntax-and-semantics/main-operator.tex:71-77` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/main-operator.tex:75`; final reader page pending
  - `OLP-0154` `upstream/content/first-order-logic/syntax-and-semantics/main-operator.tex:79-99` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/main-operator.tex:96`; final reader page pending
  - `OLP-0153` `upstream/content/first-order-logic/syntax-and-semantics/unique-readability.tex:113-116` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/unique-readability.tex:107`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
It is often useful to talk about the last operator used in
constructing !!a{formula}~$!A$.  This operator is called the \emph{main
  operator} of~$!A$. Intuitively, it is the ``outermost'' operator
of $!A$. For example, the main operator of $\lnot !A$ is $\lnot$,
the main operator of $(!A \lor !B)$ is $\lor$, etc.
\end{explain}
```

### BN-IN-T102

- Source term or concept: term induction principle; formula induction principle; unique formation sequence
- Chosen Bengali: পদের উপর আরোহের নীতি; সূত্রের উপর আরোহের নীতি; একক গঠন-অনুক্রম
- Rationale: The canonical witnesses support mathematical induction and proof prose, while the exact structural-induction compounds remain sparse. The two principles follow the recursive term and formula formation clauses and license proofs from the corresponding base and constructor cases. একক গঠন-অনুক্রম combines the formation-sequence term fixed in T065 with uniqueness of the shortest sequence ending in the expression; it does not assert that longer sequences containing unused material are unique.
- Plausible alternatives: কাঠামোগত আরোহ was considered for both induction principles; the selected পদের/সূত্রের উপর আরোহের নীতি explicitly states which recursive object is the induction domain. ন্যূনতম গঠন-অনুক্রম was considered, but একক গঠন-অনুক্রম follows the theorem’s uniqueness claim while the text separately identifies shortest length.
- Status: provisional-induction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পদের উপর আরোহের নীতি; সূত্রের উপর আরোহের নীতি; একক গঠন-অনুক্রম’ express the OpenLogic sense(s) ‘term induction principle; formula induction principle; unique formation sequence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0152` `upstream/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:189-205` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/terms-formulas.tex:183`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{lem}[\emph{Principle of induction on terms}]
    \ollabel{lem:trmind}
    Let $\Lang L$ be a first-order language.
    If some property~$P$ is such that
    %
    \begin{enumerate}
        \item it holds for every !!{variable}~$v$,
        %
        \item it holds for every !!{constant}~$a$ of~$\Lang L$, and
        %
        \item it holds for $f(t_1,\dotsc,t_n)$ whenever it holds for
        $t_1$,~\dots, $t_n$ and $f$~is an $n$-place
            !!{function} of~$\Lang L$
    \end{enumerate}
    (assuming $t_1$,~\dots, $t_n$ are terms of~$\Lang{L}$),
    then $P$ holds for every term in~$\Trm[L]$.
\end{lem}
```

### BN-IN-T103

- Source term or concept: variable assignment; x-variant; term valuation under an assignment; satisfaction under an assignment
- Chosen Bengali: চলরাশি-আরোপ; x-বিকল্প; আরোপের অধীনে পদের মান; আরোপের অধীনে পরিতৃপ্তি
- Rationale: The checked pages directly support variable, mapping, domain, relation, truth and quantification vocabulary, but not the complete Tarskian compounds. A চলরাশি-আরোপ is a total map from variables into the structure's domain. An x-বিকল্প may differ from the original assignment only at x, including the unchanged assignment itself. The recursive value and satisfaction clauses use the assignment only for variables and free-variable dependence; T098 and T099 govern the surrounding structure and substitution terminology.
- Plausible alternatives: চল-নির্দেশ and চলরাশি-মূল্যায়ন were considered for variable assignment; চলরাশি-আরোপ parallels the established assignment register without colliding with propositional valuation. x-পরিবর্তন was considered for x-variant; x-বিকল্প keeps the at-most-one-variable difference explicit through the adjacent definition.
- Status: mixed-attested-roots-and-provisional-tarskian-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চলরাশি-আরোপ; x-বিকল্প; আরোপের অধীনে পদের মান; আরোপের অধীনে পরিতৃপ্তি’ express the OpenLogic sense(s) ‘variable assignment; x-variant; term valuation under an assignment; satisfaction under an assignment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 45 occurrence(s). Representative locations:
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:34-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:37`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:87-107` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:91`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:87-107` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:106`; final reader page pending
  - `OLP-0171` `upstream/content/first-order-logic/models-theories/expressing-relations.tex:14-33` → `bn-Beng-IN/content/first-order-logic/models-theories/expressing-relations.tex:25`; final reader page pending
  - `OLP-0171` `upstream/content/first-order-logic/models-theories/expressing-relations.tex:14-33` → `bn-Beng-IN/content/first-order-logic/models-theories/expressing-relations.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  If $!A$ is an axiom, then
  \iftag{FOL}
    {$\Sat{M}{!A}[s]$ for each !!{structure}~$\Struct{M}$ and assignment~$s$.}
    {$\pSat{v}{!A}$ for each !!{valuation}~$\pAssign{v}$.}
\end{prop}
```

### BN-IN-T104

- Source term or concept: covered structure; standard model of arithmetic; hereditarily finite sets; free logic
- Chosen Bengali: আচ্ছাদিত গঠন; পাটিগণিতের মানক মডেল; বংশগতভাবে সসীম সেট; মুক্ত যুক্তিবিদ্যা
- Rationale: The Indian Bengali witnesses support arithmetic, finite sets, relations, mappings and quantification, while the full model-theory compounds remain provisional. A structure is আচ্ছাদিত exactly when every domain element is denoted by a closed term. মানক মডেল names the intended natural-number interpretation and is harmonized here with the chapter's current wording; T094's earlier প্রমিত wording is retained as a recorded alternative pending expert correction. বংশগতভাবে সসীম follows the displayed cumulative finite powerset construction. মুক্ত যুক্তিবিদ্যা names the explicitly contrasted setting that permits empty domains or nondesignating names and therefore changes existential generalization.
- Plausible alternatives: আচ্ছাদক গঠন was considered for covered structure; আচ্ছাদিত গঠন describes the structure as covered by closed-term values. প্রমিত মডেল is the earlier recorded alternative to মানক মডেল; both remain open to expert adjudication, and the current chapter consistently uses মানক. উত্তরাধিকারসূত্রে সসীম and hereditary-set loans were considered; বংশগতভাবে সসীম is governed by the cumulative powerset display. স্বাধীন যুক্তিবিদ্যা was considered for free logic; মুক্ত যুক্তিবিদ্যা retains the established free-variable root while the digression gives the distinct semantic sense.
- Status: mixed-definition-governed-and-provisional-model-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আচ্ছাদিত গঠন; পাটিগণিতের মানক মডেল; বংশগতভাবে সসীম সেট; মুক্ত যুক্তিবিদ্যা’ express the OpenLogic sense(s) ‘covered structure; standard model of arithmetic; hereditarily finite sets; free logic’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0162` `upstream/content/first-order-logic/syntax-and-semantics/covered-structures.tex:68-70` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/covered-structures.tex:70`; final reader page pending
  - `OLP-0161` `upstream/content/first-order-logic/syntax-and-semantics/structures.tex:82-92` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/structures.tex:84`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
Is $\Struct N$, the standard model of arithmetic, covered? Explain.
\end{prob}
```

### BN-IN-T105

- Source term or concept: extensionality; relevance; Skolem normal form
- Chosen Bengali: ব্যাপ্তিগততা; প্রাসঙ্গিকতা; স্কোলেম স্বাভাবিক রূপ
- Rationale: The canonical pages support relation, function, variable, proof and quantifier discourse but do not directly attest these specialized compounds. ব্যাপ্তিগততা is fixed by the proposition saying satisfaction depends only on the domain and interpretations of symbols occurring in the formula; প্রাসঙ্গিকতা records the source's alternate name without replacing that technical definition. স্কোলেম স্বাভাবিক রূপ names the universal formula with a function witness obtained in the exercise; the displayed equivalence and quantifier pattern govern the phrase.
- Plausible alternatives: বহির্বিস্তারণতা and extensionality loans were considered; ব্যাপ্তিগততা is fixed by dependence only on the occurring vocabulary and domain. সংশ্লিষ্টতা was considered for relevance; প্রাসঙ্গিকতা is used only as the source’s alternative label. স্কোলেমীয় স্বাভাবিক রূপ was considered; স্কোলেম স্বাভাবিক রূপ keeps the proper name compact and is governed by the displayed universal-function form.
- Status: provisional-definition-and-theorem-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ব্যাপ্তিগততা; প্রাসঙ্গিকতা; স্কোলেম স্বাভাবিক রূপ’ express the OpenLogic sense(s) ‘extensionality; relevance; Skolem normal form’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0164` `upstream/content/first-order-logic/syntax-and-semantics/assignments.tex:348-351` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/assignments.tex:358`; final reader page pending
  - `OLP-0165` `upstream/content/first-order-logic/syntax-and-semantics/extensionality.tex:11-11` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/extensionality.tex:11`; final reader page pending
  - `OLP-0165` `upstream/content/first-order-logic/syntax-and-semantics/extensionality.tex:13-19` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/extensionality.tex:14`; final reader page pending
  - `OLP-0165` `upstream/content/first-order-logic/syntax-and-semantics/extensionality.tex:21-26` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/extensionality.tex:20`; final reader page pending
  - `OLP-0165` `upstream/content/first-order-logic/syntax-and-semantics/extensionality.tex:28-37` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/extensionality.tex:26`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
(This problem is a special case of what's known as Skolem's Theorem;
$\lforall[x][!A(x,f(x))]$ is called a \emph{Skolem normal form} of
$\lforall[x][\lexists[y][!A(x,y)]]$.)
\end{prob}
```

### BN-IN-T106

- Source term or concept: axiomatic theory; closure of a sentence set; axiomatized by; intended structure; capture a class; redundant axiom; definability
- Chosen Bengali: স্বতঃসিদ্ধমূলক তত্ত্ব; বাক্যসমষ্টির আবরণ; স্বতঃসিদ্ধায়িত; অভিপ্রেত গঠন; কোনো শ্রেণিকে ধারণ করা; অপ্রয়োজনীয় স্বতঃসিদ্ধ; সংজ্ঞেয়তা
- Rationale: The checked set, relation, quantification and proof pages support the academic register and the component words, but do not directly attest these complete model-theoretic compounds. The closure of Gamma is exactly the set of its semantic consequences; Delta axiomatizes Gamma exactly when Gamma is that closure. An axiom system captures a class when precisely the intended structures model it. Redundancy is tested by consequence from the remaining axioms, while definability asks whether one relation can be expressed using the language's other primitives. T029, T070, T091 and T100 govern the overlapping closure, axiom-system and model vocabulary.
- Plausible alternatives: সমাপ্তি was considered for closure; আবরণ continues T029 and denotes the full consequence set rather than a proof ending. চরিত্রায়িত করা remains available for characterize under T100; ধারণ করা follows this chapter’s capture metaphor and exact-model condition. অতিরিক্ত স্বতঃসিদ্ধ was considered for redundant axiom; অপ্রয়োজনীয় marks derivability from the others without suggesting syntactic duplication.
- Status: mixed-attested-roots-and-provisional-axiomatic-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বতঃসিদ্ধমূলক তত্ত্ব; বাক্যসমষ্টির আবরণ; স্বতঃসিদ্ধায়িত; অভিপ্রেত গঠন; কোনো শ্রেণিকে ধারণ করা; অপ্রয়োজনীয় স্বতঃসিদ্ধ; সংজ্ঞেয়তা’ express the OpenLogic sense(s) ‘axiomatic theory; closure of a sentence set; axiomatized by; intended structure; capture a class; redundant axiom; definability’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 9 occurrence(s). Representative locations:
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:21-26` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:22`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:33-35` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:35`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:37-47` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:39`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:37-47` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:40`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:49-98` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:87`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The axiomatic method and logic were made for each other.  Formal logic
provides the tools for formulating axiomatic theories, for proving
theorems from the axioms of the theory in a precisely specified way,
for studying the properties of all systems satisfying the axioms in a
systematic way.
\end{explain}
```

### BN-IN-T107

- Source term or concept: strict linear-order theory; group theory; Peano arithmetic; induction schema; pure set; urelement; set extensionality; naive comprehension scheme
- Chosen Bengali: কঠোর রৈখিক ক্রমের তত্ত্ব; গোষ্ঠীর তত্ত্ব; পেয়ানো পাটীগণিত; আরোহ-ছক; বিশুদ্ধ সেট; উর-উপাদান; সেটের সদস্যভিত্তিক সমতা; অনানুষ্ঠানিক ধর্মনির্দেশে সেট-গঠন ছক
- Rationale: The India-standard witnesses directly support set membership, emptiness, equality, subsets, power sets, relations, quantification and proof flow. They do not directly attest every named first-order theory or schema. The displayed axioms govern strict order, group and arithmetic meanings. আরোহ follows T042 and T102; the schema is the infinite family of induction sentences. বিশুদ্ধ excludes urelements hereditarily. সেটের সদস্যভিত্তিক সমতা distinguishes the set axiom from semantic extensionality in T105. The naive comprehension scheme is the unrestricted existence family that yields Russell's contradiction, under T020.
- Plausible alternatives: গাণিতিক আরোহ-ছক was considered; আরোহ-ছক is compact because Peano arithmetic supplies the mathematical context. অপরিশীলিত and নির্বিচার were considered for naive; অনানুষ্ঠানিক follows T020 while the adjacent Russell derivation fixes unrestricted comprehension. বহির্বিস্তারণ was considered for set extensionality; সদস্যভিত্তিক সমতা states the member criterion and stays distinct from T105’s semantic extensionality.
- Status: mixed-attested-roots-and-provisional-theory-examples; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কঠোর রৈখিক ক্রমের তত্ত্ব; গোষ্ঠীর তত্ত্ব; পেয়ানো পাটীগণিত; আরোহ-ছক; বিশুদ্ধ সেট; উর-উপাদান; সেটের সদস্যভিত্তিক সমতা; অনানুষ্ঠানিক ধর্মনির্দেশে সেট-গঠন ছক’ express the OpenLogic sense(s) ‘strict linear-order theory; group theory; Peano arithmetic; induction schema; pure set; urelement; set extensionality; naive comprehension scheme’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:31-55` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:41`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:13-27` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:14`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:29-38` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:31`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:40-57` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:41`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:40-57` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:55`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To begin with, ``is an element of'' is not the only relation we are
interested in: ``is a subset of'' seems almost as important.  But we
can \emph{define} ``is a subset of'' in terms of ``is an element of.''
To do this, we have to find !!a{formula}~$!A(x, y)$ in
the language of set theory which is satisfied by a pair of
sets~$\tuple{X, Y}$ iff $X \subseteq Y$.  But $X$ is a subset of $Y$
just in case all !!{element}s of~$X$ are also !!{element}s of~$Y$.  So
we can define $\subseteq$ by the formula
\[
\lforall[z][(z \in x \lif z \in y)]
\]
Now, whenever we want to use the relation~$\subseteq$ in a formula, we
could instead use that formula (with $x$ and $y$ suitably replaced,
and the bound variable~$z$ renamed if necessary).  For instance,
extensionality of sets means that if any sets~$x$ and $y$ are
contained in each other, then $x$ and $y$ must be the same set. This
can be expressed by $\lforall[x][\lforall[y][((x \subseteq y \land y
    \subseteq x) \lif x = y)]]$, or, if we replace $\subseteq$ by the
above definition, by
\[
\lforall[x][\lforall[y][((\lforall[z][(z \in x \lif z \in y)] \land
    \lforall[z][(z \in y \lif z \in x)]) \lif x = y)]].
\]
This is in fact one of the axioms of $\Log{ZFC}$, the ``axiom of
extensionality.''
```

### BN-IN-T108

- Source term or concept: mereology; parthood; parthood structure; proper/improper part; mereological sum; fusion
- Chosen Bengali: অংশতত্ত্ব; অংশ-সম্পর্ক; অংশ-গঠন; যথার্থ/অযথার্থ অংশ; অংশতাত্ত্বিক যোগ; সংযোজন
- Rationale: The checked pages support part-like set and relation prose, mapping language and proof style, but they do not directly attest the mereological compounds. The source definitions therefore control them. Parthood is axiomatized as a partial order. A proper part excludes identity; an improper part may be the object itself. The displayed biconditional fixes a mereological sum as the least common upper bound under parthood, while fusion names the same composition in the final explanatory principle.
- Plausible alternatives: অংশবিদ্যা was considered for mereology; অংশতত্ত্ব marks a formal theory of the parthood relation. প্রকৃত/অপ্রকৃত অংশ were considered; যথার্থ/অযথার্থ preserves the paired proper/improper distinction already used in the target. মিলন was considered for fusion but collides with set union; সংযোজন remains governed by the displayed least-upper-bound condition.
- Status: provisional-definition-governed-mereology-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অংশতত্ত্ব; অংশ-সম্পর্ক; অংশ-গঠন; যথার্থ/অযথার্থ অংশ; অংশতাত্ত্বিক যোগ; সংযোজন’ express the OpenLogic sense(s) ‘mereology; parthood; parthood structure; proper/improper part; mereological sum; fusion’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 26 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:169-181` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:171`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:102-106` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:104`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:102-106` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:105`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:108-141` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:108`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:108-141` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:111`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In set-theoretic terms, a function is just a special kind of relation;
for example, a unary function~$f$ can be identified with a binary
relation~$R$ satisfying $\lforall[x][\lexists![y][R(x,y)]]$. As a result, one
can quantify over functions too. Using the full semantics, one can
then define the class of infinite !!{structure}s to be the class of
!!{structure}s $\Struct M$ for which there is an injective function from the
!!{domain} of $\Struct M$ to a proper subset of itself:
\[
\lexists[f][(\lforall[x][\lforall[y][(\eq[f(x)][f(y)] \lif \eq[x][y])]]
  \land \lexists[y][\lforall[x][\eq/[f(x)][y]]])].
\]
The negation of this sentence then defines the class of finite
!!{structure}s.
```

### BN-IN-T109

- Source term or concept: express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model
- Chosen Bengali: কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল
- Rationale: The university witnesses directly support relations, domains, mappings and quantification; the full definability compounds remain provisional. A formula expresses R only relative to the stated structure and assignments of its free variables. A predicate is superfluous when a formula using the remaining vocabulary expresses its interpretation. The arithmetic examples preserve argument order for successor and predecessor. The chapter uses প্রমিত consistently with T094; the মানক alternative remains recorded in T104 for expert review. T032 governs inverse, relative product and transitive closure, and T043 governs cofinite.
- Plausible alternatives: সংজ্ঞায়ক সম্পর্ক was considered for definable relation; সংজ্ঞেয় সম্পর্ক states that some formula can define it in the fixed structure. পরবর্তী/পূর্ববর্তী সম্পর্ক were considered; উত্তরসূরি/পূর্বসূরি aligns with the arithmetic direction displayed in the formulas. মানক মডেল remains a recorded alternative under T104; প্রমিত মডেল continues T094 in this chapter.
- Status: mixed-attested-roots-and-provisional-definability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল’ express the OpenLogic sense(s) ‘express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 29 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:60`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:156-167` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:155`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:156-167` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:159`; final reader page pending
  - `OLP-0171` `upstream/content/first-order-logic/models-theories/expressing-relations.tex:55-67` → `bn-Beng-IN/content/first-order-logic/models-theories/expressing-relations.tex:59`; final reader page pending
  - `OLP-0171` `upstream/content/first-order-logic/models-theories/expressing-relations.tex:55-67` → `bn-Beng-IN/content/first-order-logic/models-theories/expressing-relations.tex:62`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
As in the case of second-order logic, one can think of higher-order
logic as a kind of many-sorted logic, where there is a sort for each
type of object we want to consider. But it is usually clearer just to
define the syntax of higher-type logic from the ground up. For
example, we can define a set of finite types inductively, as follows:
\begin{enumerate}
\item $\Nat$ is a finite type.
\item If $\sigma$ and $\tau$ are finite types, then so is $\sigma
  \to \tau$.
\item If $\sigma$ and $\tau$ are finite types, so is $\sigma \times
  \tau$.
\end{enumerate}
Intuitively, $\Nat$ denotes the type of the natural numbers,
$\sigma \to \tau$ denotes the type of functions from $\sigma$ to
$\tau$, and $\sigma \times \tau$ denotes the type of pairs of objects,
one from $\sigma$ and one from $\tau$. We can then define a set of
terms inductively, as follows:
\begin{enumerate}
\item For each type $\sigma$, there is a stock of variables $x$, $y$,
  $z$, \dots of type $\sigma$
\item $\Obj 0$ is a term of type $\Nat$
\item $\Obj S$ (successor) is a term of type $\Nat \to \Nat$
\item If $s$ is a term of type $\sigma$, and $t$ is a term of type
  $\Nat \to (\sigma \to \sigma)$, then $\Obj{R}_{st}$ is a term of type
  $\Nat \to \sigma$
\item If $s$ is a term of type $\tau \to \sigma$ and $t$ is a
  term of type~$\tau$, then $s(t)$ is a term of type $\sigma$
\item If $s$ is a term of type~$\sigma$ and $x$ is a variable of
  type~$\tau$, then $\lambd[x][s]$ is a term of type $\tau \to \sigma$.
\item If $s$ is a term of type~$\sigma$ and $t$ is a term of
  type~$\tau$, then $\tuple{s, t}$ is a term of type $\sigma \times
  \tau$.
\item If $s$ is a term of type~$\sigma \times \tau$ then $p_1(s)$ is a
  term of type~$\sigma$ and $p_2(s)$ is a term of type~$\tau$.
\end{enumerate}
Intuitively, $\Obj{R}_{st}$ denotes the function defined recursively by
\begin{align*}
\Obj{R}_{st}(0) & = s \\
\Obj{R}_{st}(x+1) & = t(x, R_{st}(x)),
\end{align*}
$\tuple{s, t}$ denotes the pair whose first component is~$s$ and whose
second component is~$t$, and $p_1(s)$ and~$p_2(s)$ denote the first
and second elements (``projections'') of~$s$. Finally, $\lambd[x][s]$
denotes the function~$f$ defined by
\[
f(x) = s
\]
for any~$x$ of type~$\sigma$; so item (6) gives us a form of
comprehension, enabling us to define functions using
terms. !!^{formula}s are built up from !!{identity} statements $\eq[s][t]$
between terms of the same type, the usual propositional connectives,
and higher-type quantification. One can then take the axioms of the
system to be the basic equations governing the terms defined above,
together with the usual rules of logic with quantifiers and !!{identity}.
```

### BN-IN-T110

- Source term or concept: ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox
- Chosen Bengali: জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস
- Rationale: The West Bengal and Tripura sources directly support set membership, subsets, equality, emptiness, power sets, ordered pairs, relations and mappings, but do not directly attest the complete foundational names. OpenLogic's formulas govern each phrase. Extensionality identifies sets with the same members; the power-set axiom supplies the set of all subsets. A function is encoded as a set of ordered pairs satisfying inclusion, totality and uniqueness. Unrestricted comprehension is inconsistent by Russell's paradox, while separation restricts the selected members to a pre-existing set. T020 and T039 govern the overlapping comprehension and function vocabulary.
- Plausible alternatives: ব্যাপ্তিগততার স্বতঃসিদ্ধ was considered for extensionality; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ exposes the set-membership criterion and avoids collision with T105. সর্বগ্রাহী নীতি and comprehension loan forms were considered; ধর্মনির্দেশে সেট-গঠন states the exact unrestricted existence claim. বিভাজন নীতি was considered for separation; পৃথকীকরণ makes restriction to a prior set distinct from partitions.
- Status: mixed-attested-set-roots-and-provisional-foundational-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস’ express the OpenLogic sense(s) ‘ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 14 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:75`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:73-90` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:87`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:149-171` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:162`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:149-171` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:168`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:149-171` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:169`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
When logicians refer to the ``axioms of second-order logic'' they
usually mean the minimal extension of first-order logic by
second-order quantifier rules together with the comprehension
schema. But it is often interesting to study weaker subsystems of
these axioms and rules. For example, note that in its full generality
the axiom schema of comprehension is \emph{impredicative}: it allows
one to assert the existence of a relation $\Atom{R}{x_1, \dots, x_k}$
that is ``defined'' by !!a{formula} with second-order quantifiers; and
these quantifiers range over the set of all such relations---a set
which includes $R$ itself!{} Around the turn of the twentieth century, a
common reaction to Russell's paradox was to lay the blame on such
definitions, and to avoid them in developing the foundations of
mathematics. If one prohibits the use of second-order quantifiers in
the !!{formula}~$!A$, one has a {\em predicative} form of
comprehension, which is somewhat weaker.
```

### BN-IN-T111

- Source term or concept: size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure
- Chosen Bengali: গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন
- Rationale: The NSOU pages directly attest finite and infinite sets and finite cardinality; the logic and relation pages support quantified model descriptions. The specialized structure-size compounds remain definition-governed. The displayed sentences express lower, upper and exact finite bounds. Infinitude requires the infinite family of all lower-bound sentences and cannot be expressed by one purely logical sentence. Compactness and Löwenheim--Skolem govern the stated nonexpressibility of finiteness and nonenumerability. T040 and T100 govern size and nonenumerability terminology.
- Plausible alternatives: গঠনের মাত্রা was considered for structure size; আকার avoids suggesting vector-space dimension while T040 reserves finite set মাত্রা as an attested cardinality phrase. সর্বাধিক n was considered for at most n; বড়জোর n is the transparent Bengali bound used in the target. অগণনীয় was considered for nonenumerable; অতালিকায়নযোগ্য preserves the edition’s distinction from countability and follows T100.
- Status: mixed-attested-finiteness-and-provisional-model-size-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন’ express the OpenLogic sense(s) ‘size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 225 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:119`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:121`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:127`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:68-77` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:71`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}[Compactness]
\ollabel{prop:proves-compact}
  \begin{enumerate}
  \item If $\Gamma \Proves !A$ then there is a finite subset $\Gamma_0
    \subseteq \Gamma$ such that $\Gamma_0 \Proves !A$.
  \item If every finite subset of~$\Gamma$ is
    consistent, then $\Gamma$ is consistent.
  \end{enumerate}
\end{prop}
```

### BN-IN-T112

- Source term or concept: logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning
- Chosen Bengali: প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার
- Rationale: The checked school and university logic pages support statement, connective, quantification and proof vocabulary, while the complete philosophical compounds remain provisional. The overview treats a logic as a formal language with an optional deductive system and intended semantics, and preserves the rival necessary, a-priori, formal and conventional conceptions of logical truth. যুক্তিবাদ names the Frege--Russell--Whitehead program; higher-order reasoning remains distinct from Quine's set-theoretic reading.
- Plausible alternatives: প্রথম-ক্রমের পরবর্তী যুক্তিবিদ্যা was considered; পরিসরের বাইরে matches the chapter’s survey of extensions and restrictions without imposing a historical order. নিষ্পাদন ব্যবস্থা was considered for deductive system; অবরোহী ব্যবস্থা is broader here because the overview is not tied to one project derivation formalism. লজিসিজম was considered; যুক্তিবাদ keeps the philosophical program in Bengali while the Frege--Russell--Whitehead context fixes its sense.
- Status: mixed-attested-roots-and-provisional-philosophical-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার’ express the OpenLogic sense(s) ‘logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:13-19` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:14`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:14`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:16`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:32`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:81-95` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:76`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Passing from first-order logic to second-order logic enabled us to
talk about sets of objects in the first-order !!{domain}, within the
formal language. Why stop there? For example, third-order logic should
enable us to deal with sets of sets of objects, or perhaps even sets
which contain both objects and sets of objects. And fourth-order logic
will let us talk about sets of objects of that kind. As you may have
guessed, one can iterate this idea arbitrarily.
```

### BN-IN-T113

- Source term or concept: many-sorted logic; sort; sort-specific domain; typed function or relation; relativized quantifier; first-order embedding
- Chosen Bengali: বহুজাতীয় যুক্তিবিদ্যা; জাতি; জাতি-নির্দিষ্ট সংজ্ঞাক্ষেত্র; টাইপযুক্ত অপেক্ষক বা সম্পর্ক; আপেক্ষিক পরিমাণসূচক; প্রথম-ক্রমীয় নিবেশন
- Rationale: The checked witnesses directly support quantification, relations, domains, mappings and proof prose, but not the full many-sorted compounds. জাতি is the syntactic/semantic classifier called a sort and is kept distinct from the higher-order টাইপ. Each variable, identity and symbol receives the relevant sort restrictions. The displayed German predicate shows relativization, and the first-order translation collects the disjoint domains while unary predicates track their sorts.
- Plausible alternatives: বহু-সর্ট যুক্তিবিদ্যা was considered; বহুজাতীয় যুক্তিবিদ্যা gives the classifier a readable Bengali form while retaining the source definition. প্রকার was considered for sort; জাতি keeps the sort layer distinct from the higher-order টাইপ layer in T115. সীমাবদ্ধ পরিমাণসূচক was considered; আপেক্ষিক পরিমাণসূচক highlights replacement by a unary sort predicate.
- Status: mixed-attested-roots-and-provisional-many-sorted-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বহুজাতীয় যুক্তিবিদ্যা; জাতি; জাতি-নির্দিষ্ট সংজ্ঞাক্ষেত্র; টাইপযুক্ত অপেক্ষক বা সম্পর্ক; আপেক্ষিক পরিমাণসূচক; প্রথম-ক্রমীয় নিবেশন’ express the OpenLogic sense(s) ‘many-sorted logic; sort; sort-specific domain; typed function or relation; relativized quantifier; first-order embedding’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 26 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:23`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:41`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:42`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:11-11` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:11`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:19-26` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:19`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In practice, higher-order logic is often !!{formula}ted in terms of
functions instead of relations. (Modulo the natural identifications,
this difference is inessential.) Given some basic ``sorts'' $A$, $B$,
$C$,~\dots (which we will now call ``types''), we can create new ones
by stipulating
\begin{quote}
If $\sigma$ and $\tau$ are finite types then so is $\sigma \to \tau$.
\end{quote}
Think of types as syntactic ``labels,'' which classify the objects we
want in our !!{domain}; $\sigma \to \tau$ describes those objects that
are functions which take objects of type~$\sigma$ to objects of
type~$\tau$. For example, we might want to have a type $\Omega$ of
truth values, ``true'' and ``false,'' and a type $\Nat$ of natural
numbers. In that case, you can think of objects of type $\Nat \to
\Omega$ as unary relations, or subsets of $\Nat$; objects of type
$\Nat \to \Nat$ are functions from natural numbers to natural numbers;
and objects of type $(\Nat \to \Nat) \to \Nat$ are ``functionals,''
that is, higher-type functions that take functions to numbers.
```

### BN-IN-T114

- Source term or concept: second-order logic; relation variable; comprehension schema; impredicative/predicative comprehension; full/weak second-order semantics; categorical description; effective proof system
- Chosen Bengali: দ্বিতীয়-ক্রমের যুক্তিবিদ্যা; সম্পর্ক-চলরাশি; ধর্মনির্দেশ-ছক; অপ্রেডিকেটিভ/প্রেডিকেটিভ ধর্মনির্দেশ; পূর্ণ/দুর্বল দ্বিতীয়-ক্রমীয় অর্থতত্ত্ব; সমরূপতা-অবধি একক বর্ণনা; কার্যকর প্রমাণ-ব্যবস্থা
- Rationale: The set, relation, mapping, quantification and proof witnesses support the component language, while the complete second-order terminology remains definition-governed. Relation variables range over k-ary relations. The comprehension schema supplies a relation coextensive with a formula; impredicative instances may quantify over a totality containing the relation itself. Full semantics quantifies over every relation and yields categorical descriptions but no complete effective proof system; weak semantics ranges over a selected relation domain and recovers completeness through many-sorted first-order logic.
- Plausible alternatives: সম্পর্ক-পরিমাণায়ন ছক was considered for comprehension; ধর্মনির্দেশ-ছক continues T107 and T110 while the displayed biconditional fixes relation formation. অবিধেয়মূলক/বিধেয়মূলক were considered; অপ্রেডিকেটিভ/প্রেডিকেটিভ retain the internationally recognizable foundational distinction pending expert review. ক্যাটেগরিক্যাল বর্ণনা was considered; সমরূপতা-অবধি একক বর্ণনা states the exact model-theoretic sense rather than suggesting an ordinary category.
- Status: mixed-attested-roots-and-provisional-second-order-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘দ্বিতীয়-ক্রমের যুক্তিবিদ্যা; সম্পর্ক-চলরাশি; ধর্মনির্দেশ-ছক; অপ্রেডিকেটিভ/প্রেডিকেটিভ ধর্মনির্দেশ; পূর্ণ/দুর্বল দ্বিতীয়-ক্রমীয় অর্থতত্ত্ব; সমরূপতা-অবধি একক বর্ণনা; কার্যকর প্রমাণ-ব্যবস্থা’ express the OpenLogic sense(s) ‘second-order logic; relation variable; comprehension schema; impredicative/predicative comprehension; full/weak second-order semantics; categorical description; effective proof system’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 323 occurrence(s). Representative locations:
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:54-56` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:58`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:46-47` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:45`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:16`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:22`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:23`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
  Complete the proof of \olref[fol][axd][ddq]{thm:deduction-thm-q}.
\end{prob}
```

### BN-IN-T115

- Source term or concept: higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types
- Chosen Bengali: উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব
- Rationale: The checked pages support number, variable, function and proof roots but do not directly attest higher-type theory. টাইপ is kept distinct from the many-sorted জাতি while the formation clauses govern function and product types. A functional maps functions to numbers; lambda abstraction forms a function term; the two projections recover pair components. Church's simple theory of types is fixed by the truth-value type and replacement of complex formulas by terms of that type.
- Plausible alternatives: প্রকার was considered for type but is already ordinary Bengali and risks collapsing the sort/type distinction; টাইপ retains the formal hierarchy explicitly. অপেক্ষকাত্মক was considered for functional; ফাংশনাল is the recognizable higher-type noun and is immediately defined as a function taking functions to numbers. লাম্বডা নিষ্কর্ষ was considered; ল্যাম্বডা বিমূর্তন remains provisional and its term-forming clause supplies the exact sense.
- Status: mixed-attested-roots-and-provisional-type-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব’ express the OpenLogic sense(s) ‘higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 57 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:11-11` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:11`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:21`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:24`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:27`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:21-38` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Higher-Order logic}
```

### BN-IN-T116

- Source term or concept: intuitionistic logic; constructive proof; BHK interpretation; formulas-as-types; Curry--Howard isomorphism; double-negation translation; Kripke structure; forcing relation
- Chosen Bengali: স্বজ্ঞাবাদী যুক্তিবিদ্যা; নির্মাণমূলক প্রমাণ; BHK ব্যাখ্যা; সূত্র-হিসেবে-টাইপ; কারি--হাওয়ার্ড সমরূপতা; দ্বিনঞর্থকতা অনুবাদ; ক্রিপকে গঠন; বাধ্যকরণ সম্পর্ক
- Rationale: The checked witnesses support numbers, connectives, quantification, variables and proof prose, while the specialized intuitionistic terminology remains source-defined. Constructive existence supplies a witness and constructive disjunction specifies a side. The BHK clauses interpret proofs as data and procedures, motivating formulas-as-types and Curry--Howard. The double-negation translation embeds classical provability. Kripke structures order knowledge states and the forcing relation gives the recursive intuitionistic semantics.
- Plausible alternatives: অন্তর্দৃষ্টিবাদী যুক্তিবিদ্যা was considered; স্বজ্ঞাবাদী যুক্তিবিদ্যা is selected provisionally for the Brouwer--Heyting tradition. সূত্র-প্রকার দৃষ্টান্ত was considered; সূত্র-হিসেবে-টাইপ keeps the Curry--Howard direction explicit. বলবৎকরণ and সত্যায়ন were considered for forcing; বাধ্যকরণ সম্পর্ক remains tied to the recursive Kripke clauses.
- Status: mixed-attested-roots-and-provisional-intuitionistic-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বজ্ঞাবাদী যুক্তিবিদ্যা; নির্মাণমূলক প্রমাণ; BHK ব্যাখ্যা; সূত্র-হিসেবে-টাইপ; কারি--হাওয়ার্ড সমরূপতা; দ্বিনঞর্থকতা অনুবাদ; ক্রিপকে গঠন; বাধ্যকরণ সম্পর্ক’ express the OpenLogic sense(s) ‘intuitionistic logic; constructive proof; BHK interpretation; formulas-as-types; Curry--Howard isomorphism; double-negation translation; Kripke structure; forcing relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:117`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:11-11` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:11`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:74-79` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:66`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:81-95` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:84`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:97-112` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:88`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Higher-type logic is attractive because it provides a framework in
which we can embed a good deal of mathematics in a natural way:
starting with $\Nat$, one can define real numbers, continuous
functions, and so on. It is also particularly attractive in the
context of intuitionistic logic, since the types have clear
``constructive'' interpretations. In fact, one can develop constructive
versions of higher-type semantics (based on intuitionistic, rather
than classical logic) that clarify these constructive interpretations
quite nicely, and are, in many ways, more interesting than the
classical counterparts.
```

### BN-IN-T117

- Source term or concept: modal logic; necessity/possibility; possible world; accessibility relation; intensional/extensional logic; provability/epistemic/temporal logic; S4/S5
- Chosen Bengali: মোডাল যুক্তিবিদ্যা; আবশ্যিকতা/সম্ভাব্যতা; সম্ভাব্য জগৎ; অভিগম্যতা সম্পর্ক; অভিপ্রায়গত/ব্যাপ্তিগত যুক্তিবিদ্যা; প্রমাণযোগ্যতা/জ্ঞানতাত্ত্বিক/কালগত যুক্তিবিদ্যা; S4/S5
- Rationale: The checked logic, relation and proof pages support the component register, while modal compounds remain definition-governed. Box expresses truth at every accessible world and diamond is its dual. অভিগম্যতা names the frame relation. অভিপ্রায়গত is contrasted with T105's ব্যাপ্তিগত sense. Provability, epistemic and temporal readings preserve the three applications; the displayed axioms and reflexive/transitive or universal frames govern S4 and S5.
- Plausible alternatives: প্রকারগত যুক্তিবিদ্যা was considered for modal logic; মোডাল যুক্তিবিদ্যা avoids collision with the type/sort vocabulary and is widely recognizable. সম্ভব-জগৎ was considered; সম্ভাব্য জগৎ keeps the counterfactual reading explicit. মনোগত/বহির্বিস্তারণমূলক were considered for intensional/extensional; অভিপ্রায়গত/ব্যাপ্তিগত aligns the latter with T105 while retaining the semantic contrast.
- Status: mixed-attested-roots-and-provisional-modal-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মোডাল যুক্তিবিদ্যা; আবশ্যিকতা/সম্ভাব্যতা; সম্ভাব্য জগৎ; অভিগম্যতা সম্পর্ক; অভিপ্রায়গত/ব্যাপ্তিগত যুক্তিবিদ্যা; প্রমাণযোগ্যতা/জ্ঞানতাত্ত্বিক/কালগত যুক্তিবিদ্যা; S4/S5’ express the OpenLogic sense(s) ‘modal logic; necessity/possibility; possible world; accessibility relation; intensional/extensional logic; provability/epistemic/temporal logic; S4/S5’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 23 occurrence(s). Representative locations:
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:11-11` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:11`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:31-39` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:28`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:41-48` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:37`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:41-48` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:38`; final reader page pending
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:41-48` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:40`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Modal Logics}
```

### BN-IN-T118

- Source term or concept: fuzzy logic; probabilistic logic; default logic; nonmonotonic logic; defeasible reasoning; epistemic logic; causal logic; deontic logic
- Chosen Bengali: ফাজি যুক্তিবিদ্যা; সম্ভাবনামূলক যুক্তিবিদ্যা; ডিফল্ট যুক্তিবিদ্যা; অ-একঘেয়ে যুক্তিবিদ্যা; প্রত্যাহারযোগ্য যুক্তিবিচার; জ্ঞানতাত্ত্বিক যুক্তিবিদ্যা; কারণমূলক যুক্তিবিদ্যা; কর্তব্যগত যুক্তিবিদ্যা
- Rationale: The checked pages support general logic and proof vocabulary but do not directly attest these modern subfield names. Each term is therefore fixed by the source's one-sentence functional description: vagueness, uncertainty, retractable defaults, knowledge, causation and obligation respectively. অ-একঘেয়ে marks that adding information can withdraw an inference, while প্রত্যাহারযোগ্য states the defeasible behavior without treating it as ordinary falsification.
- Plausible alternatives: অস্পষ্ট যুক্তিবিদ্যা was considered for fuzzy logic; ফাজি যুক্তিবিদ্যা preserves the established subfield label while the following sentence defines its purpose. অ-একতান যুক্তিবিদ্যা was considered for nonmonotonic logic; অ-একঘেয়ে যুক্তিবিদ্যা directly negates the mathematical monotonicity term used elsewhere. খণ্ডনযোগ্য যুক্তিবিচার was considered for defeasible reasoning; প্রত্যাহারযোগ্য says that later information can withdraw an otherwise reasonable inference.
- Status: provisional-survey-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ফাজি যুক্তিবিদ্যা; সম্ভাবনামূলক যুক্তিবিদ্যা; ডিফল্ট যুক্তিবিদ্যা; অ-একঘেয়ে যুক্তিবিদ্যা; প্রত্যাহারযোগ্য যুক্তিবিচার; জ্ঞানতাত্ত্বিক যুক্তিবিদ্যা; কারণমূলক যুক্তিবিদ্যা; কর্তব্যগত যুক্তিবিদ্যা’ express the OpenLogic sense(s) ‘fuzzy logic; probabilistic logic; default logic; nonmonotonic logic; defeasible reasoning; epistemic logic; causal logic; deontic logic’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0180` `upstream/content/first-order-logic/beyond/modal-logics.tex:50-65` → `bn-Beng-IN/content/first-order-logic/beyond/modal-logics.tex:57`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:23`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:24`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:25`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:28`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Modal logic is sometimes called an ``intensional'' logic, as opposed
to an ``extensional'' one. The intended semantics for an extensional
logic, like classical logic, will only refer to a single world, the
``actual'' one; while the semantics for an ``intensional'' logic
relies on a more elaborate ontology. In addition to !!{structure}ing
necessity, one can use modality to !!{structure} other linguistic
constructions, reinterpreting $\Box$ and $\Diamond$ according to the
application. For example:
\begin{enumerate}
\item In provability logic, $\Box !A$ is read ``$!A$ is provable''
  and $\Diamond !A$ is read ``$!A$ is consistent.''
\item In epistemic logic, one might read $\Box !A$ as ``I know
  $!A$'' or ``I believe $!A$.''
\item In temporal logic, one can read $\Box !A$ as ``$!A$ is always
  true'' and $\Diamond !A$ as ``$!A$ is sometimes true.''
\end{enumerate}
```

### BN-IN-T119

- Source term or concept: model theory; basics; incomplete and experimental material; adaptation
- Chosen Bengali: মডেল তত্ত্ব; মূল বিষয়; অসম্পূর্ণ ও পরীক্ষামূলক উপকরণ; অভিযোজন
- Rationale: The checked logic, set, relation, mapping, proof and size pages support the surrounding mathematical register, while the full model-theory title and editorial labels remain provisional. মডেল তত্ত্ব continues T100. মূল বিষয় names the introductory chapter without claiming exhaustive foundations. অসম্পূর্ণ ও পরীক্ষামূলক উপকরণ preserves the source warning, and অভিযোজন identifies the stated relation to Antonelli's notes rather than presenting the text as a literal edition.
- Plausible alternatives: মডেলতত্ত্ব as one word was considered; মডেল তত্ত্ব continues the spacing already used in T100 and in the part heading. ভিত্তি was considered for basics; মূল বিষয় fits an introductory collection without claiming a complete axiomatic foundation. রূপান্তর was considered for adaptation; অভিযোজন preserves editorial reuse without implying a literal translation of Antonelli’s notes.
- Status: mixed-attested-roots-and-provisional-model-theory-editorial-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মডেল তত্ত্ব; মূল বিষয়; অসম্পূর্ণ ও পরীক্ষামূলক উপকরণ; অভিযোজন’ express the OpenLogic sense(s) ‘model theory; basics; incomplete and experimental material; adaptation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0147` `upstream/content/first-order-logic/introduction/models-theories.tex:13-30` → `bn-Beng-IN/content/first-order-logic/introduction/models-theories.tex:26`; final reader page pending
  - `OLP-0148` `upstream/content/first-order-logic/introduction/soundness-completeness.tex:50-55` → `bn-Beng-IN/content/first-order-logic/introduction/soundness-completeness.tex:48`; final reader page pending
  - `OLP-0183` `upstream/content/model-theory/basics/basics.tex:8-8` → `bn-Beng-IN/content/model-theory/basics/basics.tex:8`; final reader page pending
  - `OLP-0182` `upstream/content/model-theory/model-theory.tex:7-7` → `bn-Beng-IN/content/model-theory/model-theory.tex:7`; final reader page pending
  - `OLP-0182` `upstream/content/model-theory/model-theory.tex:9-17` → `bn-Beng-IN/content/model-theory/model-theory.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Once we've defined the syntax and semantics of first-order logic, we
can get to work investigating the properties of !!{structure}s and the
semantic notions. We can also define !!{derivation} systems, and
investigate those.  For a set of !!{sentence}s, we can ask: what
!!{structure}s make all the !!{sentence}s in that set true?  Given a
set of !!{sentence}s~$\Gamma$, !!a{structure}~$\Struct{M}$ that
satisfies them is called a \emph{model of~$\Gamma$}.  We might start
from~$\Gamma$ and try to find its models---what do they look like? How
big or small do they have to be? But we might also start with a single
!!{structure} or collection of !!{structure}s and ask: what
!!{sentence}s are true in them?  Are there !!{sentence}s that
\emph{characterize} these !!{structure}s in the sense that they, and
only they, are true in them? These kinds of questions are the domain
of \emph{model theory}.  They also underlie the \emph{axiomatic
  method}: describing a collection of !!{structure}s by a set of
!!{sentence}s, the axioms of a theory. This is made possible by the
observation that exactly those !!{sentence}s entailed in first-order
logic by the axioms are true in all models of the axioms.
```

### BN-IN-T120

- Source term or concept: reduct; expansion; substructure; extension; common language; induced relational substructure
- Chosen Bengali: হ্রাসিত রূপ; সম্প্রসারণ; উপগঠন; বর্ধিত গঠন; অভিন্ন ভাষা; সম্পর্ক-প্রসূত উপগঠন
- Rationale: The witnesses directly support sets, subset inclusion, relations, domains and mappings, but do not directly attest the complete model-theoretic compounds. হ্রাসিত রূপ describes forgetting symbols outside the smaller language while preserving the common interpretations. সম্প্রসারণ adds interpretations or enlarges a structure as fixed by each adjacent definition. উপগঠন is governed by domain inclusion and agreement on constants, functions and predicates; the purely relational construction restricts each relation to the chosen nonempty domain.
- Plausible alternatives: রিডাক্ট and হ্রাস were considered for reduct; হ্রাসিত রূপ states the resulting structure and avoids suggesting a numerical reduction. বিস্তার was considered for expansion; সম্প্রসারণ is already used consistently for adding language symbols or extending a structure. অধোগঠন was considered for substructure; উপগঠন follows the established subset and subformula compound pattern.
- Status: mixed-attested-roots-and-provisional-structure-comparison-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হ্রাসিত রূপ; সম্প্রসারণ; উপগঠন; বর্ধিত গঠন; অভিন্ন ভাষা; সম্পর্ক-প্রসূত উপগঠন’ express the OpenLogic sense(s) ‘reduct; expansion; substructure; extension; common language; induced relational substructure’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:14`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:166-170` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:157`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:69`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:11-11` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:11`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:57`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
First-order logic is not the only system of logic of interest: there
are many extensions and variations of first-order logic. A logic
typically consists of the formal specification of a language, usually,
but not always, a deductive system, and usually, but not always, an
intended semantics. But the technical use of the term raises an
obvious question: what do logics that are not first-order logic have
to do with the word ``logic,'' used in the intuitive or philosophical
sense? All of the systems described below are designed to model
reasoning of some form or another; can we say what makes them logical?
```

### BN-IN-T121

- Source term or concept: overspill; arbitrarily large finite models; finite satisfiability; infinite model
- Chosen Bengali: ওভারস্পিল; ইচ্ছামতো বড় সসীম মডেল; সসীমভাবে পরিতৃপ্তিযোগ্য; অসীম মডেল
- Rationale: The checked pages support finite and infinite sets, model vocabulary, quantification and proof prose. The specialized theorem name remains a recognizable loan. ইচ্ছামতো বড় means that for every positive lower bound some finite model has at least that size. The new pairwise-distinct constants make every finite fragment satisfiable, and compactness then produces an infinite model; this sense continues T094's finite-satisfiability term.
- Plausible alternatives: অতিপ্রবাহ was considered as a Bengali calque for overspill; ওভারস্পিল keeps the recognizable theorem name while the theorem statement gives its exact content. যত বড় চাই তত বড় was considered; ইচ্ছামতো বড় is shorter and the following every-m-positive clause fixes the unbounded finite-size meaning.
- Status: mixed-attested-finiteness-and-provisional-compactness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ওভারস্পিল; ইচ্ছামতো বড় সসীম মডেল; সসীমভাবে পরিতৃপ্তিযোগ্য; অসীম মডেল’ express the OpenLogic sense(s) ‘overspill; arbitrarily large finite models; finite satisfiability; infinite model’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 33 occurrence(s). Representative locations:
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:26-29` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:24`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:26-29` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:26`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:31-36` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:30`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:58-63` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:59`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:58-63` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:60`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We can use the same method to show that a finitely satisfiable set of
sentences is satisfiable. We just have to prove the corresponding
versions of the results leading to the truth lemma where we replace
``consistent'' with ``finitely satisfiable.''
```

### BN-IN-T122

- Source term or concept: elementary equivalence; isomorphic structures; isomorphism; automorphism; definable subset; invariance
- Chosen Bengali: মৌলিকভাবে সমতুল্য; সমরূপ গঠন; সমরূপতা; স্বসমরূপতা; সংজ্ঞেয় উপসেট; অপরিবর্তিতা
- Rationale: The witnesses support relation, mapping, bijection, equality and proof language, while the full model-theoretic compounds remain definition-governed. মৌলিকভাবে সমতুল্য means agreement on every sentence of the common language and is weaker than isomorphism. সমরূপতা requires a bijection preserving constants, predicates and functions. স্বসমরূপতা is an isomorphism from a structure to itself, under which every parameter-free definable subset is invariant.
- Plausible alternatives: প্রাথমিকভাবে সমতুল্য was considered for elementarily equivalent; মৌলিকভাবে সমতুল্য avoids suggesting chronological priority and is defined by agreement on all first-order sentences. সমাকৃতি and গঠনসমতা were considered for isomorphism; সমরূপতা continues the established mapping-preservation term. অটোসমরূপতা was considered; স্বসমরূপতা transparently marks an isomorphism from a structure to itself.
- Status: mixed-attested-roots-and-provisional-isomorphism-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মৌলিকভাবে সমতুল্য; সমরূপ গঠন; সমরূপতা; স্বসমরূপতা; সংজ্ঞেয় উপসেট; অপরিবর্তিতা’ express the OpenLogic sense(s) ‘elementary equivalence; isomorphic structures; isomorphism; automorphism; definable subset; invariance’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 25 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:97-112` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:97`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:100-127` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:117`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:129-167` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:150`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:198`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:35`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
There is an informal constructive interpretation of the intuitionist
connectives, usually known as the BHK interpretation (named after
Brouwer, Heyting, and Kolmogorov). It runs as follows: a proof of $!A
\land !B$ consists of a proof of $!A$ paired with a proof of $!B$; a
proof of $!A \lor !B$ consists of either a proof of $!A$, or a proof
of $!B$, where we have explicit information as to which is the case; a
proof of $!A \lif !B$ consists of a procedure, which transforms a
proof of $!A$ to a proof of~$!B$; a proof of $\lforall[x][!A(x)]$
consists of a procedure which returns a proof of $!A(x)$ for any value
of~$x$; and a proof of $\lexists[x][!A(x)]$ consists of a value
of~$x$, together with a proof that this value satisfies~$!A$. One can
describe the interpretation in computational terms known as the
``Curry--Howard isomorphism'' or the ``!!{formula}s-as-types
paradigm'': think of !!a{formula} as specifying a certain kind of
data type, and proofs as computational objects of these data types
that enable us to see that the corresponding !!{formula} is true.
```

### BN-IN-T123

- Source term or concept: theory of a structure; complete theory; elementary equivalence; complete set of sentences
- Chosen Bengali: কোনো গঠনের তত্ত্ব; পূর্ণ তত্ত্ব; মৌলিক সমতুল্যতা; বাক্যের পূর্ণ সেট
- Rationale: The checked logic, quantification, relation and proof pages support theory and sentence prose, while the model-theoretic compounds remain source-defined. The theory of M is exactly the set of all sentences true in M and is complete because it contains either each sentence or its negation. Equality of these theories gives elementary equivalence. পূর্ণ follows the project's established completeness family and is fixed here by the explicit sentence-or-negation condition.
- Plausible alternatives: সম্পূর্ণ তত্ত্ব was considered; পূর্ণ তত্ত্ব continues the project completeness vocabulary and the sentence-or-negation clause prevents confusion with exhaustive exposition. গঠনতত্ত্ব was rejected for theory of a structure because it could be read as the discipline model theory; কোনো গঠনের তত্ত্ব explicitly marks Theory(M).
- Status: mixed-attested-roots-and-provisional-complete-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কোনো গঠনের তত্ত্ব; পূর্ণ তত্ত্ব; মৌলিক সমতুল্যতা; বাক্যের পূর্ণ সেট’ express the OpenLogic sense(s) ‘theory of a structure; complete theory; elementary equivalence; complete set of sentences’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:68-83` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:78`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{rem}
  Let $\Struct{S}$ be any !!{enumerable} dense linear ordering without
  endpoints. Then (by \olref{thm:cantorQ}) $\Struct{S} \iso
  \Struct{Q}$, where $\Struct{Q} = (\Rat, <)$ is the !!{enumerable}
  dense linear ordering having the set $\Rat$ of the rational numbers
  as its domain. Now consider again the !!{structure}~$\Struct{R} =
  (\Real, <)$ from \olref[thm]{remark:R}. We saw that there is
  !!a{enumerable} !!{structure}~$\Struct{S}$ such that $\Struct{R}
  \elemequiv \Struct{S}$. But $\Struct{S}$ is !!a{enumerable} dense
  linear ordering without endpoints, and so it is isomorphic (and
  hence elementarily equivalent) to the !!{structure}~$\Struct{Q}$. By
  transitivity of elementary equivalence, $\Struct{R} \elemequiv
  \Struct{Q}$. (We could have shown this directly by establishing
  $\Struct{R} \iso[p] \Struct{Q}$ by the same back-and-forth
  argument.)
\end{rem}
```

### BN-IN-T124

- Source term or concept: partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union
- Chosen Bengali: আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ
- Rationale: The witnesses support finite sets, relations, mappings, inclusion and proof prose, while the back-and-forth terminology remains definition-governed. An আংশিক সমরূপতা is a finite partial function preserving the isomorphism clauses wherever defined. অগ্র extends the domain and পশ্চাৎ extends the range. Alternating the two conditions along enumerations yields an inclusion-increasing chain whose union is the required total isomorphism.
- Plausible alternatives: আংশিক সমাকৃতি was considered; আংশিক সমরূপতা extends T122 and the finite partial-function definition fixes its scope. সামনে-পিছনে and back-and-forth loan forms were considered; আগ-পিছু is concise, while অগ্র and পশ্চাৎ name the two formal extension clauses. ঊর্ধ্বমুখী সংযোগ was considered for increasing union; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ states the ordering relation on the partial maps.
- Status: mixed-attested-roots-and-provisional-back-and-forth-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ’ express the OpenLogic sense(s) ‘partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:35`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:37`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:41`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:58`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:63-66` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:64`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
  Let $\Struct{M_1}$ and $\Struct{M_2}$ be !!{enumerable} dense linear
  orderings without endpoints, with ${<_1} = \Assign{<}{M_1}$ and ${<_2} =
  \Assign{<}{M_2}$, and let $\PIso{I}$ be the set of all partial
  isomorphisms between them. $\PIso{I}$ is not empty since at least
  $\emptyset \in \PIso{I}$. We show that $\PIso{I}$ satisfies the
  Back-and-Forth property.  Then $\Struct{M_1} \iso[p] \Struct{M_2}$,
  and the theorem follows by \olref[pis]{thm:p-isom1}.
```

### BN-IN-T125

- Source term or concept: quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence
- Chosen Bengali: পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা
- Rationale: The sources support quantification, finite objects, sequences, relations and proof language, but do not directly attest the bounded-rank compounds. পরিমাণসূচক-ক্রমাঙ্ক counts maximum quantifier nesting. n-সমতুল্য গঠন agree on sentences of rank at most n. সংযুক্তি appends one element to a finite sequence and stays distinct from logical conjunction. The recursive I_n relation connects sequence extension with formulas of bounded rank, using finiteness only up to logical equivalence.
- Plausible alternatives: পরিমাণসূচক গভীরতা was considered for quantifier rank; পরিমাণসূচক-ক্রমাঙ্ক follows the source rank notation and remains fixed by maximum nesting depth. ক্রমসংযোজন was considered for sequence concatenation; সংযুক্তি continues T076 and is distinguished from logical conjunction by context. n-মৌলিক সমতুল্য was considered; n-সমতুল্য গঠন stays close to the notation and the bounded-rank sentence definition.
- Status: mixed-attested-roots-and-provisional-bounded-rank-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা’ express the OpenLogic sense(s) ‘quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 24 occurrence(s). Representative locations:
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:15-16` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:16`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:46-50` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:51`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:25-31` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:26`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:40-49` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:40`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[!!^{derivability}]
If $\Gamma$ is a set of !!{formula}s of $\Lang L$ then a
\emph{!!{derivation}} from~$\Gamma$ is a finite sequence $!A_1$,
\dots,~$!A_n$ of !!{formula}s where for each $i \le n$ one of the
following holds:
\begin{enumerate}
\item $!A_i \in \Gamma$; or
\item $!A_i$ is an axiom; or
\item $!A_i$ follows from some $!A_j$ (and $!A_k$) with $j < i$ (and
  $k < i$) by a rule of inference.
\end{enumerate}
\end{defn}
```

### BN-IN-T126

- Source term or concept: dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order
- Chosen Bengali: অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম
- Rationale: The checked pages support order relations, rational numbers, mappings, quantification, countability and proof prose. The complete dense-order compound remains governed by the six displayed axioms: strict linear order, points above and below every element, and a point strictly between any two ordered points. অন্তবিন্দু names an excluded least or greatest boundary point. The back-and-forth theorem makes all enumerable models of this theory isomorphic, including the rational order.
- Plausible alternatives: প্রান্তবিন্দুহীন was considered for without endpoints; অন্তবিন্দুহীন is selected because the axioms exclude both a least and a greatest element of the order. সঘন রৈখিক ক্রম was considered; ঘন রৈখিক ক্রম is more idiomatic and is fixed by the between-any-two-points axiom. ক্যান্টরের উপপাদ্য was considered; কান্টরের আগ-পিছু উপপাদ্য distinguishes this countable-order result from Cantor’s other theorems.
- Status: mixed-attested-order-roots-and-provisional-dense-order-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম’ express the OpenLogic sense(s) ‘dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:12-26` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:13`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:28-31` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:29`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:34`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:55`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:68-83` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:69`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
  A \emph{dense linear ordering without endpoints} is !!a{structure}
  $\Struct{M}$ for the !!{language} containing a single 2-place
  !!{predicate}~$<$ satisfying the following sentences:
  \begin{enumerate}
  \item $\lforall[x][\lnot x < x]$;
  \item $\lforall[x][\lforall[y][\lforall[z][(x < y \lif (y < z \lif x
    <z ))]]]$;
  \item $\lforall[x][\lforall[y][(x< y \lor \eq[x][y] \lor y < x)]]$;
  \item $\lforall[x][\lexists[y][x < y]]$;
  \item $\lforall[x][\lexists[y][y < x]]$;
  \item $\lforall[x][\lforall[y][(x < y \lif \lexists[z][(x < z \land
        z < y))]]]$.
 \end{enumerate}
\end{defn}
```
