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
| `BN-IN-T001` | set | সেট | attested | high_for_attested_scope | low | 1174 | BN-IN-P001, BN-IN-P006 | welcome/open to correction |
| `BN-IN-T002` | element | উপাদান | attested | high_for_attested_scope | low | 112 | BN-IN-P001 | welcome/open to correction |
| `BN-IN-T003` | member | সদস্য | attested | high_for_attested_scope | low | 57 | BN-IN-P001 | welcome/open to correction |
| `BN-IN-T004` | empty set | শূন্য সেট | attested | high_for_attested_scope | low | 18 | BN-IN-P006 | welcome/open to correction |
| `BN-IN-T005` | subset | উপসেট | attested | high_for_attested_scope | low | 94 | BN-IN-P003, BN-IN-P007 | welcome/open to correction |
| `BN-IN-T006` | proper subset | প্রকৃত উপসেট | attested | high_for_attested_scope | low | 3 | BN-IN-P004, BN-IN-P007 | welcome/open to correction |
| `BN-IN-T007` | power set | ঘাত সেট | attested-regional | high_for_attested_scope | low | 6 | BN-IN-P007 | welcome/open to correction |
| `BN-IN-T008` | extensionality | সদস্যভিত্তিক সমতার নীতি | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 20 | BN-IN-P004, BN-IN-P006 | welcome/open to correction |
| `BN-IN-T009` | natural number | স্বাভাবিক সংখ্যা | attested | high_for_attested_scope | low | 107 | BN-IN-P005 | welcome/open to correction |
| `BN-IN-T010` | proposition (logic) | বচন | attested | high_for_attested_scope | low | 56 | BN-IN-P009, BN-IN-P008 | welcome/open to correction |
| `BN-IN-T011` | quantifier | পরিমাণসূচক | attested | high_for_attested_scope | low | 107 | BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T012` | universal quantifier | সার্বিক পরিমাণসূচক | attested | high_for_attested_scope | low | 6 | BN-IN-P009 | welcome/open to correction |
| `BN-IN-T013` | existential quantifier | অস্তিত্বমূলক পরিমাণসূচক | attested | high_for_attested_scope | low | 0 | BN-IN-P010 | welcome/open to correction |
| `BN-IN-T014` | if and only if | যদি এবং কেবল যদি | provisional-phrase | medium_definition_and_adjacent-canon_support | medium | 259 | BN-IN-P004 | welcome/open to correction |
| `BN-IN-T015` | perfect number | নিখুঁত সংখ্যা | provisional-descriptive | low_pending_occurrence | high | 0 | BN-IN-P005 | welcome/open to correction |
| `BN-IN-T016` | union; intersection; disjoint; difference | সংযোগ; ছেদ; বিচ্ছিন্ন; অন্তর | attested | high_for_attested_scope | low | 119 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T017` | ordered pair | ক্রমযুগল | attested | high_for_attested_scope | low | 40 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T018` | Cartesian product | কার্তেসীয় গুণফল | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P012 | welcome/open to correction |
| `BN-IN-T019` | string; sequence; tuple; word | প্রতীকক্রম; অনুক্রম; টিউপল; শব্দ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 346 | BN-IN-P002, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T020` | paradox; contradiction; comprehension; naive set theory | কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 58 | BN-IN-P001, BN-IN-P004, BN-IN-P009 | welcome/open to correction |
| `BN-IN-T021` | conjunction; conjunction elimination; absorption | সংযোজন; সংযোজন অপসারণ; শোষণ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 37 | BN-IN-P008, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T022` | relation; binary relation; order relation; identity relation | সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 305 | BN-IN-P013, BN-IN-P014, BN-IN-P004 | welcome/open to correction |
| `BN-IN-T023` | irreflexive; strict order; empty relation; universal relation | আত্মসম্পর্কহীন; কঠোর ক্রম; শূন্য সম্পর্ক; সার্বিক সম্পর্ক | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 19 | BN-IN-P013, BN-IN-P006, BN-IN-P009 | welcome/open to correction |
| `BN-IN-T024` | continuum; mathematical proposition heading; general conditional proof | সতত সমষ্টি; প্রতিজ্ঞা; সাধারণ শর্তাধীন প্রমাণ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P005, BN-IN-P009, BN-IN-P012 | welcome/open to correction |
| `BN-IN-T025` | predicate; singular term; metaphysical identity; set-theoretic reductionism | বিধেয়; একবস্তুনির্দেশক পদ; অধিবিদ্যাগত অভিন্নতা; সেটতত্ত্বে পর্যবসনবাদ | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 19 | BN-IN-P009, BN-IN-P013 | welcome/open to correction |
| `BN-IN-T026` | reflexivity; symmetry; transitivity; equivalence relation | প্রতিবিম্ব ধর্ম; প্রতিসাম্য; পরিযায়িতা; তুল্যতা সম্পর্ক | attested-roots-normalized-properties | high_for_attested_scope | low | 57 | BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T027` | antisymmetric; asymmetric; connected (relation) | বিপ্রতিসম; একমুখী; সংযুক্ত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 38 | BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T028` | equivalence class; partition; quotient set; congruence modulo n | তুল্যতা শ্রেণি; বিভাজন; ভাগসেট; মডুলো n সমতুল্যতা | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 18 | BN-IN-P015, BN-IN-P016, BN-IN-P017 | welcome/open to correction |
| `BN-IN-T029` | preorder; partial order; linear order; total order; closure; initial segment | প্রাক্‌ক্রম; আংশিক ক্রম; রৈখিক ক্রম; পূর্ণ ক্রম; আবরণ; প্রারম্ভিক খণ্ড | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 75 | BN-IN-P013, BN-IN-P014, BN-IN-P016 | welcome/open to correction |
| `BN-IN-T030` | graph; directed graph; vertex; edge; isolated vertex | গ্রাফ; নির্দেশিত গ্রাফ; শীর্ষ; প্রান্ত; বিচ্ছিন্ন শীর্ষ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 33 | BN-IN-P012, BN-IN-P013 | welcome/open to correction |
| `BN-IN-T031` | tree; root; successor; predecessor; branch; chain; least element; well-order | বৃক্ষ; মূল; উত্তরসূরি; পূর্বসূরি; শাখা; শৃঙ্খল; ক্ষুদ্রতম উপাদান; সুক্রম | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 492 | BN-IN-P001, BN-IN-P013, BN-IN-P014, BN-IN-P016 | welcome/open to correction |
| `BN-IN-T032` | inverse relation; relative product; restriction; application; transitive closure | বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 211 | BN-IN-P012, BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T033` | formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma | সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য | provisional-contextual | medium_definition_and_adjacent-canon_support | medium | 341 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P014 | welcome/open to correction |
| `BN-IN-T034` | variable; constant; sum; arithmetic product; equation | চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ | attested-in-school-algebra | high_for_attested_scope | low | 329 | BN-IN-P019, BN-IN-P020, BN-IN-P022 | welcome/open to correction |
| `BN-IN-T035` | function; mapping; domain; codomain; range; image/value | অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান | attested-university | high_for_attested_scope | low | 1581 | BN-IN-P018 | welcome/open to correction |
| `BN-IN-T036` | function argument; input; output; black box; extensionality for functions | আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 60 | BN-IN-P018, BN-IN-P019, BN-IN-P020, BN-IN-P022 | welcome/open to correction |
| `BN-IN-T037` | injective/injection; surjective/surjection; bijective/bijection; identity function | একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক | attested-university-with-normalization | high_for_attested_scope | low | 25 | BN-IN-P023, BN-IN-P024 | welcome/open to correction |
| `BN-IN-T038` | inverse function; left inverse; right inverse; composition | বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ | attested-root-with-provisional-normalization | medium_definition_and_adjacent-canon_support | medium | 51 | BN-IN-P024, BN-IN-P025, BN-IN-P026 | welcome/open to correction |
| `BN-IN-T039` | partial function; total function; functional relation; serial relation; Axiom of Choice | আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 40 | BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T040` | size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable | সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয় | mixed-attested-and-provisional | medium_definition_and_adjacent-canon_support | medium | 517 | BN-IN-P027, BN-IN-P028, BN-IN-P023, BN-IN-P024 | welcome/open to correction |
| `BN-IN-T041` | actual infinity | বাস্তবায়িত অসীম | provisional-philosophical | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P009, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T042` | ceiling function; induction; recursive definition; corollary | ঊর্ধ্ব পূর্ণাংশ অপেক্ষক; গাণিতিক আরোহ; পূর্ববর্তী মানের সাহায্যে ধাপে ধাপে সংজ্ঞা; অনুসিদ্ধান্ত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 33 | BN-IN-P018, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T043` | zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function | আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 255 | BN-IN-P009, BN-IN-P012, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P024, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T044` | non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence | অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 18 | BN-IN-P001, BN-IN-P002, BN-IN-P009, BN-IN-P010, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T045` | reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction | হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 33 | BN-IN-P009, BN-IN-P010, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T046` | equinumerous/equinumerosity; same cardinality; cardinal equality | সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P014, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P025, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T047` | no larger than; strictly smaller cardinality; cardinal comparison; Cantor's theorem; Schröder–Bernstein theorem | আকারে বড় নয়; আকারে ছোট; অঙ্কবাচকতার তুলনা; কান্টরের উপপাদ্য; শ্র্যোডার–বার্নস্টাইন উপপাদ্য | mixed-normalized-and-proper-name | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P014, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P025, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T048` | integer; positive/negative integer; natural number represented as an integer; equivalence-class representative | পূর্ণসংখ্যা; ধনাত্মক/ঋণাত্মক পূর্ণসংখ্যা; স্বাভাবিক সংখ্যার পূর্ণসংখ্যা-রূপ; তুল্যতা শ্রেণির প্রতিনিধি | mixed-direct-and-normalized | medium_definition_and_adjacent-canon_support | medium | 86 | BN-IN-P005, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T049` | arithmetization as set-theoretic construction of number systems; induced arithmetic operations; well-defined on equivalence classes | সেটতাত্ত্বিক সংখ্যা-নির্মাণ; তুল্যতা শ্রেণির উপর গাণিতিক ক্রিয়া; প্রতিনিধিনিরপেক্ষভাবে সুসংজ্ঞায়িত | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P012, BN-IN-P015, BN-IN-P016, BN-IN-P017, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T050` | rational number; nonzero denominator; rational representative/embedding; cross multiplication | মূলদ সংখ্যা; অশূন্য হর; মূলদ-প্রতিনিধি/পূর্ণসংখ্যার মূলদ-রূপ; আড়গুণ | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 45 | BN-IN-P005, BN-IN-P012, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T051` | real line; irrational number; ordered field; Completeness Property; upper bound; least upper bound | বাস্তব সংখ্যারেখা; অমূলদ সংখ্যা; ক্রমিত ক্ষেত্র; পূর্ণতা ধর্ম; ঊর্ধ্বসীমা; লঘিষ্ঠ ঊর্ধ্বসীমা | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 32 | BN-IN-P005, BN-IN-P009, BN-IN-P015, BN-IN-P016, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T052` | Dedekind cut; lower half; proper initial segment; greatest lower bound; maximum element; rational-to-real embedding | ডেডেকিন্ড কর্তন; নিম্নাংশ; প্রকৃত প্রারম্ভিক খণ্ড; গরিষ্ঠ নিম্নসীমা; গরিষ্ঠ উপাদান; মূলদ সংখ্যার বাস্তব-রূপ | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P005, BN-IN-P015, BN-IN-P016, BN-IN-P017, BN-IN-P019, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T053` | commutative ring; ordered ring; ordered field; associative/commutative/identity/additive inverse/distributive laws; trichotomy | বিনিমেয় বলয়; ক্রমিত বলয়; ক্রমিত ক্ষেত্র; সংযোগী/বিনিময়/অভেদী/যোগাত্মক বিপরীত/বণ্টন ধর্ম; ত্রিবিভাজন | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 26 | BN-IN-P009, BN-IN-P013, BN-IN-P014, BN-IN-P017, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T054` | Cauchy sequence; rational approximation; tends to zero; equivalence modulo null sequences; constant-sequence embedding; monotone increasing/decreasing | কোশি অনুক্রম; মূলদ আসন্নমান; সীমায় শূন্যের দিকে যায়; শূন্যমুখী অনুক্রমের মডুলো তুল্যতা; ধ্রুব অনুক্রমে অন্তর্ভুক্তি; একঘেয়ে বর্ধমান/হ্রাসমান | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 16 | BN-IN-P005, BN-IN-P009, BN-IN-P016, BN-IN-P018, BN-IN-P019, BN-IN-P024, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T055` | rigour of a construction; metaphysical identification; set-theoretic embedding; rival constructions; Benacerraf-style underdetermination | নির্মাণের কঠোরতা; অধিবিদ্যাগত অভিন্নকরণ; সেটতাত্ত্বিক অন্তর্ভুক্তি; প্রতিদ্বন্দ্বী নির্মাণ; বেনাসেরাফ-ধর্মী অনির্ধার্যতা | provisional-philosophical | low_pending_occurrence | high | 0 | BN-IN-P009, BN-IN-P013, BN-IN-P015, BN-IN-P016, BN-IN-P018, BN-IN-P029 | welcome/open to correction |
| `BN-IN-T056` | infinite set; Dedekind-infinite set; Hilbert's Hotel | অসীম সেট; ডেডেকিন্ড-অসীম সেট; হিলবার্টের হোটেল | mixed-direct-and-provisional | medium_definition_and_adjacent-canon_support | medium | 23 | BN-IN-P023, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T057` | Dedekind algebra; successor function; self-map; f-closed set; closure under f | ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 30 | BN-IN-P013, BN-IN-P014, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T058` | parameter of a formula; free variable; recursive definition | সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা | provisional-normalized | medium_definition_and_adjacent-canon_support | medium | 35 | BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T059` | isomorphic structures; structuralist; surrogate for the natural numbers; pure laws of thought | সমরূপ গঠন; গঠনবাদী; স্বাভাবিক সংখ্যার প্রতিস্থাপক; চিন্তার বিশুদ্ধ বিধি | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P009, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T060` | syntax; semantics; metatheory; inductive definition; unique readability | সংকেতবিন্যাস; অর্থতত্ত্ব; অধিতত্ত্ব; আরোহী সংজ্ঞা; একক পাঠযোগ্যতা | provisional-formally-governed | medium_definition_and_adjacent-canon_support | medium | 102 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T061` | propositional variable; propositional/logical connective; truth value; truth-functional; material conditional | বচনচল; বচনসংযোজক/যৌক্তিক সংযোজক; সত্যমান; সত্যমান-অপেক্ষকধর্মী; বস্তুগত শর্তবচন | mixed-attested-roots-and-provisional | medium_definition_and_adjacent-canon_support | medium | 43 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020 | welcome/open to correction |
| `BN-IN-T062` | negation; conjunction; disjunction; conditional/implication; biconditional/material equivalence | নঞর্থকরণ; সংযোজন; বিয়োজন; শর্তবচন/নিহিতকরণ; দ্বিশর্তবচন/বস্তুগত সমতুল্যতা | attested-variants-normalized | high_for_attested_scope | low | 65 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T063` | denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation | অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 191 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019 | welcome/open to correction |
| `BN-IN-T064` | formula induction; balanced formula; proper initial segment; parsing; uniform substitution | সূত্রের উপর আরোহ; সুষম সূত্র; প্রকৃত প্রারম্ভিক খণ্ড; গঠনবিশ্লেষণ; সমরূপ প্রতিস্থাপন | provisional-mathematically-governed | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T065` | formation sequence; junk/redundant formula; strong induction | গঠন-অনুক্রম; অপ্রয়োজনীয় সূত্র; প্রবল আরোহ | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 73 | BN-IN-P008, BN-IN-P009, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T066` | valuation; evaluation function; satisfaction; local determination; truth table | সত্যমান-আরোপ; মূল্যায়ন অপেক্ষক; পরিতৃপ্তি; স্থানীয় নির্ধারণ; সত্যসারণি | mixed-contextual-and-provisional | medium_definition_and_adjacent-canon_support | medium | 188 | BN-IN-P008, BN-IN-P009, BN-IN-P010 | welcome/open to correction |
| `BN-IN-T067` | satisfiable/unsatisfiable; tautology; contingent; semantic entailment; monotonicity; semantic deduction theorem | পরিতৃপ্তিযোগ্য/অপরিতৃপ্তিযোগ্য; সর্বতঃসত্য; আপতিক; অর্থগত অনুসিদ্ধান্ত; একঘেয়েতা; অর্থগত নিঃসরণ উপপাদ্য | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 156 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T068` | derivation system; purely syntactic object/method; mechanical verification; metatheoretical treatment | নিষ্পাদন পদ্ধতি; সম্পূর্ণ সংকেতবিন্যাসগত বস্তু/পদ্ধতি; যান্ত্রিক যাচাই; অধিতাত্ত্বিক বিচার | provisional-contextual | medium_definition_and_adjacent-canon_support | medium | 192 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T069` | soundness; completeness; consistency/inconsistency; syntactic counterpart | বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 192 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T070` | axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens | স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স | provisional-formally-governed | medium_definition_and_adjacent-canon_support | medium | 264 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T071` | natural deduction; proof by cases; indirect proof; conditional proof | স্বাভাবিক নিষ্পাদন; ক্ষেত্রবিচারে প্রমাণ; পরোক্ষ প্রমাণ; শর্তাধীন প্রমাণ | provisional-proof-patterns | medium_definition_and_adjacent-canon_support | medium | 32 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T072` | introduction/elimination rule; assumption/hypothesis; discharge/undischarged assumption; proof-theoretic semantics | প্রবর্তন/অপসারণ-বিধি; অনুমিতি/পূর্বধারণা; অনুমিতি অবমুক্ত করা/অনবমুক্ত অনুমিতি; প্রমাণতাত্ত্বিক অর্থতত্ত্ব | provisional-natural-deduction-register | medium_definition_and_adjacent-canon_support | medium | 252 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T073` | sequent calculus; sequent; initial sequent; left/right side; weakening rule | সিকোয়েন্ট কলন; সিকোয়েন্ট; প্রারম্ভিক সিকোয়েন্ট; বাঁ/ডানপাশ; দুর্বলীকরণ-বিধি | provisional-transliterated-system | medium_definition_and_adjacent-canon_support | medium | 209 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T074` | tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus | ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন | provisional-explicitly-defined | medium_definition_and_adjacent-canon_support | medium | 332 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T075` | resolution method; resolution refutation; mechanization/implementation; read a satisfying structure off an open branch | রেজোলিউশন পদ্ধতি; রেজোলিউশন খণ্ডন; যান্ত্রিক প্রয়োগ/রূপায়ণ; খোলা শাখা থেকে পরিতৃপ্তিকারী গঠন পড়ে নেওয়া | provisional-descriptive | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T076` | antecedent; succedent; associated sentence of a sequent; sequence concatenation | পূর্বাংশ; উত্তরাংশ; সিকোয়েন্টের সংশ্লিষ্ট বাক্য; অনুক্রমের সংযুক্তি | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 13 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T077` | logical rule; structural rule; upper/lower sequent; left/right rule | যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি | provisional-rule-register | medium_definition_and_adjacent-canon_support | medium | 153 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T078` | quantifier rule; eigenvariable/eigenvariable condition; closed term | পরিমাণসূচকের বিধি; আইগেনচল/আইগেনচল-শর্ত; বদ্ধ পদ | provisional-quantifier-rule-register | medium_definition_and_adjacent-canon_support | medium | 113 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T079` | contraction; exchange; cut; inference line; LK derivation/end-sequent | সংকোচন; অদলবদল; কর্তন; অনুমান-রেখা; LK-নিষ্পাদন/অন্তিম সিকোয়েন্ট | provisional-structural-rule-register | medium_definition_and_adjacent-canon_support | medium | 56 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T080` | proof search; apply a rule backwards; split into branches; finish at an initial sequent | প্রমাণ-অন্বেষণ; বিধি উল্টো দিকে প্রয়োগ; শাখায় ভাগ; প্রারম্ভিক সিকোয়েন্টে শেষ করা | provisional-pedagogical-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T081` | provability/derivability relation; theorem; reflexivity; monotonicity; transitivity; compactness | প্রমাণযোগ্যতা/নিষ্পাদনযোগ্যতা-সম্পর্ক; উপপাদ্য; প্রতিবিম্ব ধর্ম; একঘেয়েতা; পরিযায়িতা; সংহতি | provisional-definition-governed | medium_definition_and_adjacent-canon_support | medium | 316 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T082` | propositional facts about provability; modus ponens; shared sequent context | বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ | provisional-rule-governed | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T083` | strong generalization; fresh constant; quantifier provability facts | প্রবল সাধারণীকরণ; নতুন ধ্রুবক; পরিমাণসূচক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য | provisional-quantifier-metatheory | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T084` | valid sequent; satisfy a sequent; soundness induction; induction hypothesis; variable assignment | বৈধ সিকোয়েন্ট; সিকোয়েন্ট পরিতৃপ্ত করা; বিশুদ্ধতার আরোহ-প্রমাণ; আরোহের অনুমান; চলরাশি-আরোপ | provisional-semantics-proof-register | medium_definition_and_adjacent-canon_support | medium | 73 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T085` | identity/equality rules; substitutability of identicals; Leibniz's Law; symmetry and transitivity | অভিন্নতা/সমতার বিধি; অভিন্ন বস্তুর প্রতিস্থাপনযোগ্যতা; লাইবনিজের সূত্র; প্রতিসাম্য ও পরিযায়িতা | mixed-attested-roots-and-provisional | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P013, BN-IN-P020, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T086` | natural-deduction derivation tree; branch; inference premise and conclusion; subderivation/subproof | স্বাভাবিক নিষ্পাদন-বৃক্ষ; শাখা; অনুমানের পূর্বধারণা ও সিদ্ধান্ত; উপ-নিষ্পাদন/উপপ্রমাণ | provisional-tree-structure-register | medium_definition_and_adjacent-canon_support | medium | 134 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T087` | natural-deduction eigenvariable condition; discharged A(a) assumption; major existential premise; freshness | স্বাভাবিক নিষ্পাদনের আইগেনচল-শর্ত; অবমুক্তযোগ্য A(a) অনুমিতি; প্রধান অস্তিত্বসূচক পূর্বধারণা; নতুনত্ব | provisional-rule-specific-freshness | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T088` | rule-applicable signed formula; check off with a check mark; branch-splitting rule; repeat a quantified rule with a closed term | বিধি প্রয়োগের উপযোগী চিহ্নিত সূত্র; টিকচিহ্ন দেওয়া; শাখা-বিভাজক বিধি; বদ্ধ পদ দিয়ে বিধিটি কয়েকবার প্রয়োগ | provisional-tableau-construction-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T089` | satisfy a signed formula; satisfiable set/branch/tableau; rule extension preserves satisfiability; unsatisfiable; contrapositive | চিহ্নিত সূত্রকে পরিতৃপ্ত করা; পরিতৃপ্তিযোগ্য সমষ্টি/শাখা/ট্যাবলো; বিধি-প্রসারণে পরিতৃপ্তিযোগ্যতা বজায় রাখা; অপরিতৃপ্তিযোগ্য; বিপরীত-প্রতিজ্ঞা | provisional-tableau-soundness-register | medium_definition_and_adjacent-canon_support | medium | 176 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T090` | syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations | নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো | provisional-axiomatic-metatheory-register | medium_definition_and_adjacent-canon_support | medium | 21 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T091` | complete consistent theory; axiomatizable; decidable | পূর্ণ সঙ্গত তত্ত্ব; স্বতঃসিদ্ধযোগ্য; নির্ণেয় | provisional-completeness-metatheory-register | medium_definition_and_adjacent-canon_support | medium | 35 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T092` | Henkin expansion; saturated set; witness; counterexample | হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত | provisional-henkin-construction-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T093` | term model; Truth Lemma; covered model; factor a model by an equivalence relation | পদ-মডেল; সত্যতা-সহায়ক উপপাদ্য; আচ্ছাদিত মডেল; তুল্যতা সম্পর্ক দিয়ে মডেলের ভাগকরণ | mixed-attested-roots-and-provisional-model-theory | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P013, BN-IN-P015, BN-IN-P016, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T094` | finitely satisfiable; infinitesimal; standard model of arithmetic | সসীমভাবে পরিতৃপ্তিযোগ্য; অতিক্ষুদ্র সংখ্যা; পাটীগণিতের প্রমিত মডেল | provisional-compactness-application-register | medium_definition_and_adjacent-canon_support | medium | 27 | BN-IN-P008, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T095` | downward Löwenheim–Skolem theorem; countable model; Skolem's paradox | লোয়েনহাইম--স্কোলেম উপপাদ্য; গণনীয় মডেল; স্কোলেমের কূটাভাস | provisional-model-size-register | medium_definition_and_adjacent-canon_support | medium | 13 | BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T096` | formal language; first-order language; quantificational logic; predicate logic; vocabulary; expression/string | বিধিবদ্ধ ভাষা; প্রথম-ক্রমের ভাষা; পরিমাণসূচকীয় যুক্তিবিদ্যা; বিধেয় যুক্তিবিদ্যা; শব্দভাণ্ডার; অভিব্যক্তি/প্রতীকক্রম | mixed-contextual-and-provisional-first-order-register | medium_definition_and_adjacent-canon_support | medium | 123 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019 | welcome/open to correction |
| `BN-IN-T097` | term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope | পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর | mixed-attested-roots-and-definition-governed | medium_definition_and_adjacent-canon_support | medium | 702 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T098` | structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment | গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ | mixed-attested-roots-and-provisional-semantics | medium_definition_and_adjacent-canon_support | medium | 403 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T099` | substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma | প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য | provisional-definition-and-lemma-governed | medium_definition_and_adjacent-canon_support | medium | 34 | BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T100` | model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain | মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র | mixed-attested-roots-and-provisional-model-theory | medium_definition_and_adjacent-canon_support | medium | 255 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T101` | main operator; immediate subformula; proper subformula; proper prefix | প্রধান অপারেটর; অব্যবহিত উপসূত্র; প্রকৃত উপসূত্র; প্রকৃত পূর্বাংশ | provisional-definition-governed-syntax-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T102` | term induction principle; formula induction principle; unique formation sequence | পদের উপর আরোহের নীতি; সূত্রের উপর আরোহের নীতি; একক গঠন-অনুক্রম | provisional-induction-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P008, BN-IN-P009, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T103` | variable assignment; x-variant; term valuation under an assignment; satisfaction under an assignment | চলরাশি-আরোপ; x-বিকল্প; আরোপের অধীনে পদের মান; আরোপের অধীনে পরিতৃপ্তি | mixed-attested-roots-and-provisional-tarskian-register | medium_definition_and_adjacent-canon_support | medium | 45 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T104` | covered structure; standard model of arithmetic; hereditarily finite sets; free logic | আচ্ছাদিত গঠন; পাটিগণিতের মানক মডেল; বংশগতভাবে সসীম সেট; মুক্ত যুক্তিবিদ্যা | mixed-definition-governed-and-provisional-model-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T105` | extensionality; relevance; Skolem normal form | ব্যাপ্তিগততা; প্রাসঙ্গিকতা; স্কোলেম স্বাভাবিক রূপ | provisional-definition-and-theorem-governed | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T106` | axiomatic theory; closure of a sentence set; axiomatized by; intended structure; capture a class; redundant axiom; definability | স্বতঃসিদ্ধমূলক তত্ত্ব; বাক্যসমষ্টির আবরণ; স্বতঃসিদ্ধায়িত; অভিপ্রেত গঠন; কোনো শ্রেণিকে ধারণ করা; অপ্রয়োজনীয় স্বতঃসিদ্ধ; সংজ্ঞেয়তা | mixed-attested-roots-and-provisional-axiomatic-register | medium_definition_and_adjacent-canon_support | medium | 19 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T107` | strict linear-order theory; group theory; Peano arithmetic; induction schema; pure set; urelement; set extensionality; naive comprehension scheme | কঠোর রৈখিক ক্রমের তত্ত্ব; গোষ্ঠীর তত্ত্ব; পেয়ানো পাটীগণিত; আরোহ-ছক; বিশুদ্ধ সেট; উর-উপাদান; সেটের সদস্যভিত্তিক সমতা; অনানুষ্ঠানিক ধর্মনির্দেশে সেট-গঠন ছক | mixed-attested-roots-and-provisional-theory-examples | medium_definition_and_adjacent-canon_support | medium | 19 | BN-IN-P001, BN-IN-P002, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P011, BN-IN-P013, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T108` | mereology; parthood; parthood structure; proper/improper part; mereological sum; fusion | অংশতত্ত্ব; অংশ-সম্পর্ক; অংশ-গঠন; যথার্থ/অযথার্থ অংশ; অংশতাত্ত্বিক যোগ; সংযোজন | provisional-definition-governed-mereology-register | medium_definition_and_adjacent-canon_support | medium | 56 | BN-IN-P001, BN-IN-P013, BN-IN-P018, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T109` | express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model | কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল | mixed-attested-roots-and-provisional-definability-register | medium_definition_and_adjacent-canon_support | medium | 55 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T110` | ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox | জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস | mixed-attested-set-roots-and-provisional-foundational-register | medium_definition_and_adjacent-canon_support | medium | 18 | BN-IN-P001, BN-IN-P002, BN-IN-P006, BN-IN-P007, BN-IN-P011, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T111` | size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure | গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন | mixed-attested-finiteness-and-provisional-model-size-register | medium_definition_and_adjacent-canon_support | medium | 319 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T112` | logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning | প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার | mixed-attested-roots-and-provisional-philosophical-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T113` | many-sorted logic; sort; sort-specific domain; typed function or relation; relativized quantifier; first-order embedding | বহুজাতীয় যুক্তিবিদ্যা; জাতি; জাতি-নির্দিষ্ট সংজ্ঞাক্ষেত্র; টাইপযুক্ত অপেক্ষক বা সম্পর্ক; আপেক্ষিক পরিমাণসূচক; প্রথম-ক্রমীয় নিবেশন | mixed-attested-roots-and-provisional-many-sorted-register | medium_definition_and_adjacent-canon_support | medium | 26 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T114` | second-order logic; relation variable; comprehension schema; impredicative/predicative comprehension; full/weak second-order semantics; categorical description; effective proof system | দ্বিতীয়-ক্রমের যুক্তিবিদ্যা; সম্পর্ক-চলরাশি; ধর্মনির্দেশ-ছক; অপ্রেডিকেটিভ/প্রেডিকেটিভ ধর্মনির্দেশ; পূর্ণ/দুর্বল দ্বিতীয়-ক্রমীয় অর্থতত্ত্ব; সমরূপতা-অবধি একক বর্ণনা; কার্যকর প্রমাণ-ব্যবস্থা | mixed-attested-roots-and-provisional-second-order-register | medium_definition_and_adjacent-canon_support | medium | 438 | BN-IN-P001, BN-IN-P002, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T115` | higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types | উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব | mixed-attested-roots-and-provisional-type-theory-register | medium_definition_and_adjacent-canon_support | medium | 74 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T116` | intuitionistic logic; constructive proof; BHK interpretation; formulas-as-types; Curry--Howard isomorphism; double-negation translation; Kripke structure; forcing relation | স্বজ্ঞাবাদী যুক্তিবিদ্যা; নির্মাণমূলক প্রমাণ; BHK ব্যাখ্যা; সূত্র-হিসেবে-টাইপ; কারি--হাওয়ার্ড সমরূপতা; দ্বিনঞর্থকতা অনুবাদ; ক্রিপকে গঠন; বাধ্যকরণ সম্পর্ক | mixed-attested-roots-and-provisional-intuitionistic-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P019, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T117` | modal logic; necessity/possibility; possible world; accessibility relation; intensional/extensional logic; provability/epistemic/temporal logic; S4/S5 | মোডাল যুক্তিবিদ্যা; আবশ্যিকতা/সম্ভাব্যতা; সম্ভাব্য জগৎ; অভিগম্যতা সম্পর্ক; অভিপ্রায়গত/ব্যাপ্তিগত যুক্তিবিদ্যা; প্রমাণযোগ্যতা/জ্ঞানতাত্ত্বিক/কালগত যুক্তিবিদ্যা; S4/S5 | mixed-attested-roots-and-provisional-modal-register | medium_definition_and_adjacent-canon_support | medium | 24 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T118` | fuzzy logic; probabilistic logic; default logic; nonmonotonic logic; defeasible reasoning; epistemic logic; causal logic; deontic logic | ফাজি যুক্তিবিদ্যা; সম্ভাবনামূলক যুক্তিবিদ্যা; ডিফল্ট যুক্তিবিদ্যা; অ-একঘেয়ে যুক্তিবিদ্যা; প্রত্যাহারযোগ্য যুক্তিবিচার; জ্ঞানতাত্ত্বিক যুক্তিবিদ্যা; কারণমূলক যুক্তিবিদ্যা; কর্তব্যগত যুক্তিবিদ্যা | provisional-survey-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P008, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T119` | model theory; basics; incomplete and experimental material; adaptation | মডেল তত্ত্ব; মূল বিষয়; অসম্পূর্ণ ও পরীক্ষামূলক উপকরণ; অভিযোজন | mixed-attested-roots-and-provisional-model-theory-editorial-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P001, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T120` | reduct; expansion; substructure; extension; common language; induced relational substructure | হ্রাসিত রূপ; সম্প্রসারণ; উপগঠন; বর্ধিত গঠন; অভিন্ন ভাষা; সম্পর্ক-প্রসূত উপগঠন | mixed-attested-roots-and-provisional-structure-comparison-register | medium_definition_and_adjacent-canon_support | medium | 16 | BN-IN-P001, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T121` | overspill; arbitrarily large finite models; finite satisfiability; infinite model | ওভারস্পিল; ইচ্ছামতো বড় সসীম মডেল; সসীমভাবে পরিতৃপ্তিযোগ্য; অসীম মডেল | mixed-attested-finiteness-and-provisional-compactness-register | medium_definition_and_adjacent-canon_support | medium | 33 | BN-IN-P001, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T122` | elementary equivalence; isomorphic structures; isomorphism; automorphism; definable subset; invariance | মৌলিকভাবে সমতুল্য; সমরূপ গঠন; সমরূপতা; স্বসমরূপতা; সংজ্ঞেয় উপসেট; অপরিবর্তিতা | mixed-attested-roots-and-provisional-isomorphism-register | medium_definition_and_adjacent-canon_support | medium | 50 | BN-IN-P006, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T123` | theory of a structure; complete theory; elementary equivalence; complete set of sentences | কোনো গঠনের তত্ত্ব; পূর্ণ তত্ত্ব; মৌলিক সমতুল্যতা; বাক্যের পূর্ণ সেট | mixed-attested-roots-and-provisional-complete-theory-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T124` | partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union | আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ | mixed-attested-roots-and-provisional-back-and-forth-register | medium_definition_and_adjacent-canon_support | medium | 24 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T125` | quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence | পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা | mixed-attested-roots-and-provisional-bounded-rank-register | medium_definition_and_adjacent-canon_support | medium | 34 | BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T126` | dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order | অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম | mixed-attested-order-roots-and-provisional-dense-order-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T127` | standard model; nonstandard model; standard number; nonstandard number | মানক মডেল; অমানক মডেল; মানক সংখ্যা; অমানক সংখ্যা | provisional-arithmetic-model-register | medium_definition_and_adjacent-canon_support | medium | 39 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T128` | arithmetic model; Robinson Q; Peano arithmetic; true arithmetic; consistency witness | পাটিগাণিতিক মডেল; রবিনসন Q; পেয়ানো পাটিগণিত; সত্য পাটিগণিত; সঙ্গতি-সাক্ষী | provisional-arithmetic-theory-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T129` | standard part; nonstandard part; arithmetic block; successor; predecessor | মানক খণ্ড; অমানক খণ্ড; পাটিগাণিতিক খণ্ড; উত্তরসূরি; পূর্বসূরি | provisional-arithmetic-block-register | medium_definition_and_adjacent-canon_support | medium | 62 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T130` | computable structure; computable function; decidable relation; computable presentation; Tennenbaum theorem | গণনসাধ্য গঠন; গণনসাধ্য অপেক্ষক; নির্ণেয় সম্বন্ধ; গণনসাধ্য উপস্থাপন; টেনেনবাউমের উপপাদ্য | provisional-computability-register | medium_definition_and_adjacent-canon_support | medium | 107 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T131` | discrete linear order; dense order; countable nonstandard model; no endpoints | কঠোর রৈখিক ক্রম; ঘন রৈখিক ক্রম; গণনীয় অমানক মডেল; অন্তবিন্দুহীন | provisional-arithmetic-order-register | medium_definition_and_adjacent-canon_support | medium | 21 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T132` | cancellation law; commutative operations; midpoint; arithmetic operation | যোগের কর্তন-বিধি; বিনিময়যোগ্য ক্রিয়া; গড়; পাটিগাণিতিক ক্রিয়া | provisional-arithmetic-operation-register | medium_definition_and_adjacent-canon_support | medium | 31 | BN-IN-P005, BN-IN-P019, BN-IN-P020, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T133` | transport of structure; computable presentation; up to isomorphism; bijection | গঠন পরিবাহন; গণনসাধ্য উপস্থাপন; সমরূপতা পর্যন্ত; বিজেকশন | provisional-arithmetic-presentation-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P024, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T134` | Craig interpolation; interpolant; shared-language vocabulary | ক্রেগের ইন্টারপোলেশন; ইন্টারপোল্যান্ট; অভিন্ন ভাষার সংকেত | provisional-interpolation-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T135` | separation; separator; inseparable sets | পৃথকীকরণ; পৃথককারী; অপৃথকযোগ্য সমষ্টি | provisional-separation-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T136` | maximally consistent; maximally inseparable pair; compactness | সর্বাধিক সঙ্গত; সর্বাধিক অপৃথকযোগ্য জোড়া; সংহতি | mixed-attested-roots-and-provisional-interpolation-register | medium_definition_and_adjacent-canon_support | medium | 39 | BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T137` | amalgamated model; common-language isomorphism; predicate interpretation | সম্মিলিত মডেল; অভিন্ন ভাষায় সমরূপতা; প্রেডিকেটের ব্যাখ্যা | provisional-amalgamation-register | low_pending_occurrence | high | 0 | BN-IN-P009, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T138` | explicit definability; implicit definability; Beth definability theorem | প্রকাশ্যভাবে সংজ্ঞায়িত; অন্তর্নিহিতভাবে সংজ্ঞায়িত; বেথের সংজ্ঞায়ন উপপাদ্য | provisional-definability-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T139` | abstract logic; abstract logic sentence; satisfaction relation | বিমূর্ত যুক্তিবিদ্যা; বিমূর্ত যুক্তিবিদ্যার বাক্য; সন্তুষ্টি-সম্পর্ক | provisional-abstract-logic-register | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T140` | normal abstract logic; monotonicity; expansion property; relativization property | স্বাভাবিক বিমূর্ত যুক্তিবিদ্যা; একঘেয়েমিতা; প্রসারণ ধর্ম; আপেক্ষিকীকরণ ধর্ম | provisional-normality-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T141` | compactness property; finite satisfiability | কম্প্যাক্টনেস ধর্ম; সসীমভাবে সন্তোষণীয় | mixed-attested-and-provisional-compactness-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T142` | downward Löwenheim--Skolem property; enumerable model | নিম্নমুখী লোয়েনহাইম--স্কোলেম ধর্ম; গণনীয় মডেল | provisional-lowenheim-skolem-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T143` | partial isomorphism; partially isomorphic; back-and-forth | আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু | provisional-partial-isomorphism-register | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027 | welcome/open to correction |
| `BN-IN-T144` | expressive power; at least as expressive; expressiveness ordering | প্রকাশক্ষমতা; অন্তত ততটাই প্রকাশক্ষম; প্রকাশক্ষমতার ক্রম | provisional-expressiveness-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T145` | elementary equivalence; elementarily equivalent structures | মৌলিকভাবে সমতুল্য; মৌলিকভাবে সমতুল্য গঠন | provisional-elementary-equivalence-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T146` | relativization; relativization property; reduct | আপেক্ষিকীকরণ; আপেক্ষিকীকরণ ধর্ম; রিডাক্ট | provisional-relativization-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T147` | quantifier rank; n-equivalent structures; finite rank types | পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম ক্রমাঙ্ক-প্রকার | provisional-quantifier-rank-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T148` | Lindström theorem; Lindström lemma; nonstandard element | লিন্ডস্ট্রমের উপপাদ্য; লিন্ডস্ট্রমের লেমা; অমানক উপাদান | provisional-lindstrom-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T149` | abstract-logic elementary equivalence; elementary equivalent | মৌলিকভাবে সমতুল্য কাঠামো | provisional-terminology-normalization-register | low_pending_occurrence | high | 0 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T150` | primitive recursion; primitive recursive definition; primitive recursive function | আদিম পুনরাবৃত্তি; আদিম পুনরাবৃত্তির মাধ্যমে সংজ্ঞা; আদিম পুনরাবৃত্ত অপেক্ষক | provisional-computability-recursion-register | medium_definition_and_adjacent-canon_support | medium | 83 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T151` | recursive function; recursive definition | পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত সংজ্ঞা | provisional-recursive-function-register | medium_definition_and_adjacent-canon_support | medium | 108 | BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T152` | computability theory | গণনসাধ্যতা তত্ত্ব | provisional-computability-theory-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T153` | characteristic function; computable relation | চরিত্রসূচক অপেক্ষক; গণনসাধ্য সম্বন্ধ | provisional-characteristic-function-register | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T154` | unbounded search | সীমাহীন অনুসন্ধান | provisional-unbounded-search-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T155` | partial recursive function; general recursive function | আংশিক পুনরাবৃত্ত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক | provisional-recursive-function-class-register | medium_definition_and_adjacent-canon_support | medium | 29 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T156` | arity; n-place function | স্থানসংখ্যা; n-স্থানীয় অপেক্ষক | provisional-arity-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T157` | primitive recursive notation; composition notation; recursion notation | আদিম পুনরাবৃত্ত সংকেতলিপি; মিশ্রণ-সংকেতলিপি; পুনরাবৃত্তি-সংকেতলিপি | provisional-recursive-notation-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T158` | exponentiation function; factorial function; truncated subtraction | ঘাতের অপেক্ষক; ক্রমগুণিতক অপেক্ষক; ছাঁটা বিয়োগ | provisional-arithmetic-function-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P005, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T159` | finite sum; finite product; integer division | সসীম যোগফল; সসীম গুণফল; পূর্ণসংখ্যা ভাগ | provisional-finite-arithmetic-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P005, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T160` | primitive recursive relation; Boolean operation | আদিম পুনরাবৃত্ত সম্বন্ধ; বুলীয় ক্রিয়া | provisional-primitive-relation-register | medium_definition_and_adjacent-canon_support | medium | 12 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 | welcome/open to correction |
| `BN-IN-T161` | bounded quantification; bounded universal quantifier; bounded existential quantifier | সীমাবদ্ধ পরিমাণায়ন; সীমাবদ্ধ সর্বজনীন পরিমাণসূচক; সীমাবদ্ধ অস্তিত্বমূলক পরিমাণসূচক | provisional-bounded-quantification-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013 | welcome/open to correction |
| `BN-IN-T162` | conditional function; definition by cases | শর্তাধীন অপেক্ষক; ক্ষেত্রভেদে সংজ্ঞা | provisional-conditional-function-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T163` | bounded minimization; least-number search | সীমাবদ্ধ ন্যূনীকরণ; ক্ষুদ্রতম-সংখ্যা অনুসন্ধান | provisional-bounded-minimization-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T164` | divides/divisibility; remainder; prime number; next prime | নিঃশেষে ভাগ করা/বিভাজ্যতা; ভাগশেষ; মৌলিক সংখ্যা; পরবর্তী মৌলিক সংখ্যা | provisional-prime-arithmetic-register | medium_definition_and_adjacent-canon_support | medium | 28 | BN-IN-P005, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T165` | sequence code; empty sequence; sequence concatenation; subsequence | অনুক্রমের সংকেত; শূন্য অনুক্রম; অনুক্রমের সংযুক্তি; উপ-অনুক্রম | provisional-computable-sequence-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P005, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T166` | tree; node; root; immediate subtree; leaf node | বৃক্ষ; নোড; মূল; অব্যবহিত উপবৃক্ষ; পত্র-নোড | provisional-coded-tree-register | medium_definition_and_adjacent-canon_support | medium | 295 | BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T167` | simultaneous recursion; course-of-values recursion; side value/parameter | যুগপৎ পুনরাবৃত্তি; পূর্বমান-ভিত্তিক পুনরাবৃত্তি; পার্শ্ব-মান/পরামিতি | provisional-extended-recursion-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P005, BN-IN-P008, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T168` | non-primitive-recursive function; effective enumeration; diagonalization | আদিম পুনরাবৃত্ত নয় এমন অপেক্ষক; কার্যকর তালিকায়ন; কর্ণীকরণ | provisional-diagonal-computability-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P005, BN-IN-P008, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T169` | Ackermann--Péter function; fast-growing function | আকারমান--পেতের অপেক্ষক; দ্রুত-বর্ধনশীল অপেক্ষক | provisional-fast-growth-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T170` | Church--Turing thesis; Turing machine; computational model; simulation | চার্চ--টুরিং থিসিস; টুরিং যন্ত্র; গণনামূলক মডেল; অনুকরণ | provisional-computation-model-register | medium_definition_and_adjacent-canon_support | medium | 220 | BN-IN-P005, BN-IN-P008, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T171` | partial function defined/undefined; equality up to simultaneous definedness | আংশিক অপেক্ষক সংজ্ঞায়িত/অসংজ্ঞায়িত; যুগপৎ সংজ্ঞায়িততার সাপেক্ষে সমতা | provisional-partial-definedness-register | medium_definition_and_adjacent-canon_support | medium | 48 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T172` | unbounded search operator; partial recursive function; recursive/total recursive function | সীমাহীন অনুসন্ধান অপারেটর; আংশিক পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত/সর্বত্র-সংজ্ঞায়িত পুনরাবৃত্ত অপেক্ষক | provisional-partial-recursion-register | medium_definition_and_adjacent-canon_support | medium | 281 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T173` | Kleene's normal form theorem; index; computation code | ক্লিনির স্বাভাবিক রূপের উপপাদ্য; সূচক; গণনার সংকেত | provisional-normal-form-register | medium_definition_and_adjacent-canon_support | medium | 226 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T174` | halting problem; halting function; nontermination | থামার সমস্যা; থামা-অপেক্ষক; গণনা না-থামা | provisional-halting-register | medium_definition_and_adjacent-canon_support | medium | 30 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T175` | regular function; general recursive function; conservative restriction | নিয়মিত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক; রক্ষণশীল সীমাবদ্ধকরণ | provisional-general-recursion-register | medium_definition_and_adjacent-canon_support | medium | 8 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T176` | computability theory; relative computability; recursion theory | গণনসাধ্যতা তত্ত্ব; আপেক্ষিক গণনসাধ্যতা; পুনরাবৃত্তি তত্ত্ব | provisional-computability-theory-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T177` | partial computable function; computable total function; computable relation | আংশিক গণনসাধ্য অপেক্ষক; গণনসাধ্য সর্বত্র-সংজ্ঞায়িত অপেক্ষক; গণনসাধ্য সম্বন্ধ | provisional-computability-class-register | medium_definition_and_adjacent-canon_support | medium | 35 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T178` | computation record; computation sequence; output | গণনার নথি; গণনা-অনুক্রম; নির্গম | provisional-computation-coding-register | medium_definition_and_adjacent-canon_support | medium | 63 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T179` | program specialization; fixed inputs; remaining arguments | প্রোগ্রামের বিশেষায়ন; আগে থেকে স্থির নিবেশ; অবশিষ্ট আর্গুমেন্ট | provisional-s-m-n-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T180` | universal partial computable function; effective enumeration; uniform computation | সার্বজনীন আংশিক গণনসাধ্য অপেক্ষক; কার্যকর তালিকায়ন; একই নিয়মে গণনা | provisional-universal-function-register | medium_definition_and_adjacent-canon_support | medium | 5 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T181` | no universal computable function; diagonal function; partial escape | সার্বজনীন গণনসাধ্য অপেক্ষকের অনস্তিত্ব; কর্ণ অপেক্ষক; আংশিকতার অবকাশ | provisional-no-total-universal-register | low_pending_occurrence | high | 0 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T182` | undecidability of the halting problem; infinite loop; self-input | থামার সমস্যার অনির্ণেয়তা; অসীম চক্র; স্ব-নিবেশ | provisional-halting-undecidability-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T183` | Russell's paradox; set of all sets; diagonalization argument | রাসেলের কূটাভাস; সব সেটের সেট; কর্ণীকরণ যুক্তি | provisional-russell-comparison-register | medium_definition_and_adjacent-canon_support | medium | 22 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T184` | computable set; computable relation; decidable | গণনসাধ্য সেট; গণনসাধ্য সম্বন্ধ; নির্ণেয় | provisional-decidable-set-register | medium_definition_and_adjacent-canon_support | medium | 44 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T185` | computably enumerable; recursively enumerable; c.e.; r.e. | গণনসাধ্যভাবে তালিকায়নযোগ্য; পুনরাবৃত্তভাবে তালিকায়নযোগ্য; c.e.; r.e. | provisional-ce-set-register | medium_definition_and_adjacent-canon_support | medium | 52 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T186` | semi-decidable; range characterization; domain characterization; existential characterization | অর্ধ-নির্ণেয়; মানপরিসর-চরিত্রায়ন; সংজ্ঞাক্ষেত্র-চরিত্রায়ন; অস্তিত্বমূলক চরিত্রায়ন | provisional-ce-characterization-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T187` | halting set; self-halting set; canonical undecidable set | থামা-সেট; স্ব-থামা সেট; আদর্শ অনির্ণেয় সেট | provisional-halting-set-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T188` | closure under union and intersection; parallel simulation; alternating enumeration | সংযোজন ও ছেদের অধীনে বদ্ধতা; সমান্তরাল অনুকরণ; পর্যায়ক্রমিক তালিকায়ন | provisional-ce-closure-register | low_pending_occurrence | high | 0 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T189` | complement criterion for computability; positive and negative enumeration; total decision | গণনসাধ্যতার পূরক-মানদণ্ড; সদস্যতা ও অসদস্যতার তালিকায়ন; সর্বত্র-সংজ্ঞায়িত নির্ণয় | provisional-complement-ce-register | low_pending_occurrence | high | 0 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T190` | many-one reduction; many-one reducible; many-one equivalent; one-one reducible | বহু-এক হ্রাসকরণ; বহু-এক হ্রাসযোগ্য; বহু-এক সমতুল্য; এক-এক হ্রাসযোগ্য | provisional-many-one-register | medium_definition_and_adjacent-canon_support | medium | 14 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T191` | transitivity of reducibility; Turing reducibility; Karp reducibility; Cook reducibility | হ্রাসযোগ্যতার সঞ্চারিতা; টুরিং হ্রাসযোগ্যতা; কার্প হ্রাসযোগ্যতা; কুক হ্রাসযোগ্যতা | provisional-reducibility-properties-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T192` | complete computably enumerable set; c.e.-hardest; neither computable nor complete | সম্পূর্ণ গণনসাধ্যভাবে তালিকায়নযোগ্য সেট; কঠিনতম c.e. সেট; গণনসাধ্যও নয়, সম্পূর্ণও নয় | provisional-ce-completeness-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T193` | oracle; fixed-input machine; K_1 halting set | ওরাকল; স্থির-নিবেশ যন্ত্র; K_1 থামা-সেট | provisional-K1-reduction-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T194` | totality; Tot index set; arithmetical hierarchy | সর্বত্র-সংজ্ঞায়িততা; Tot সূচক-সেট; পাটীগাণিতিক স্তরক্রম | provisional-totality-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T195` | Rice's theorem; nontrivial index set; semantic property of a computed function | রাইসের উপপাদ্য; অতুচ্ছ সূচক-সেট; গণিত অপেক্ষকের আচরণগত বৈশিষ্ট্য | provisional-rice-theorem-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T196` | program syntax; program behavior; index invariance | প্রোগ্রামের বাক্যগঠন; প্রোগ্রামের আচরণ; সূচক-অপরিবর্তিতা | provisional-rice-explanation-register | low_pending_occurrence | high | 0 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T197` | fixed-point theorem; self-reference; diagonal specialization; self-printing program | স্থির-বিন্দু উপপাদ্য; স্ব-উল্লেখ; কর্ণ বিশেষায়ন; স্ব-মুদ্রণকারী প্রোগ্রাম | provisional-fixed-point-register | medium_definition_and_adjacent-canon_support | medium | 14 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T198` | fixed-point combinator; Curry's combinator; Turing's combinator; beta-equivalent | স্থির-বিন্দু সমাবেশক; কারির সমাবেশক; টুরিংয়ের সমাবেশক; বিটা-সমতুল্য | provisional-lambda-fixed-point-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T199` | characteristic-function index extraction; computable-set index selector; fixed-point counterexample | চরিত্রসূচক-অপেক্ষকের সূচক নিষ্কাশন; গণনসাধ্য সেটের সূচক-নির্বাচক; স্থির-বিন্দু প্রতিদৃষ্টান্ত | provisional-index-extraction-register | low_pending_occurrence | high | 0 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T200` | recursive self-definition; greatest common divisor; remainder; termination by descent | স্ব-উল্লেখী পুনরাবৃত্ত সংজ্ঞা; গরিষ্ঠ সাধারণ গুণনীয়ক; ভাগশেষ; অবরোহণে সমাপ্তি | provisional-recursive-definition-register | medium_definition_and_adjacent-canon_support | medium | 10 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T201` | tape; read-write head; tape square; tape alphabet; end marker; blank symbol; stroke symbol | ফিতা; পাঠ-লেখ হেড; ফিতার ঘর; ফিতার বর্ণমালা; শেষ-চিহ্ন; ফাঁকা প্রতীক; দাগ-প্রতীক | provisional-turing-tape-register | medium_definition_and_adjacent-canon_support | medium | 115 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T202` | machine state; initial state; transition function; instruction set; direction of movement | যন্ত্রের দশা; আরম্ভিক দশা; অবস্থান্তর অপেক্ষক; নির্দেশ-সেট; চলনের দিক | provisional-turing-transition-register | medium_definition_and_adjacent-canon_support | medium | 37 | BN-IN-P005, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T203` | halt; halting state; accept an input; undefined transition | থামে; থামা-দশা; নিবেশ গ্রহণ করে; অসংজ্ঞায়িত অবস্থান্তর | provisional-turing-halting-register | medium_definition_and_adjacent-canon_support | medium | 119 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T204` | time requirement; memory requirement; bounded resources; computational complexity | সময়ের চাহিদা; স্মৃতির চাহিদা; সীমাবদ্ধ সম্পদ; গণনামূলক জটিলতা | provisional-resource-complexity-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T205` | state diagram; state node; outgoing arrow; machine table; transition label | দশা-চিত্র; দশা-নোড; বহির্মুখী তীর; যন্ত্র-সারণি; অবস্থান্তর-নির্দেশ | provisional-turing-representation-register | medium_definition_and_adjacent-canon_support | medium | 11 | BN-IN-P001, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T206` | configuration; initial configuration; run; yields in one step; head position | কনফিগারেশন; আরম্ভিক কনফিগারেশন; চালন; এক ধাপে দেয়; হেডের অবস্থান | provisional-turing-configuration-register | medium_definition_and_adjacent-canon_support | medium | 68 | BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T207` | even machine; accept; reject; loop forever; trace configurations | জোড়-যন্ত্র; গ্রহণ করে; বর্জন করে; চিরকাল চক্রাকারে চলে; কনফিগারেশন ধাপে ধাপে অনুসরণ করে | provisional-turing-execution-register | medium_definition_and_adjacent-canon_support | medium | 16 | BN-IN-P005, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T208` | doubler; strategy; erase input; duplicate a string; alphabetizer | দ্বিগুণকারী; কৌশল; নিবেশ মোছে; প্রতীকক্রমের অনুলিপি করে; বর্ণানুক্রমে সাজানোর যন্ত্র | provisional-turing-construction-register | medium_definition_and_adjacent-canon_support | medium | 39 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T209` | unary representation; arithmetical function; stroke block; encode a number; compute a partial function | এককীয় উপস্থাপনা; পাটিগাণিতিক অপেক্ষক; দাগের খণ্ড; সংখ্যার সংকেতায়ন; আংশিক অপেক্ষক গণনা করে | provisional-unary-computation-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T210` | addition machine; mover machine; single output block; temporary marker; equality machine | যোগ-যন্ত্র; স্থানান্তরক যন্ত্র; নির্গমের একটিমাত্র খণ্ড; সাময়িক চিহ্ন; সমতা-যন্ত্র | provisional-unary-machine-construction-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T211` | designated halting state; reject state; explicit acceptance; no added computing power | নির্দিষ্ট থামা-দশা; বর্জন-দশা; স্পষ্ট গ্রহণ; গণনক্ষমতা বাড়ে না | provisional-dedicated-halting-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T212` | disciplined machine; halt scanning square 1; preserve the tape-end marker; never attempt a left move from square 0 | শৃঙ্খলাবদ্ধ যন্ত্র; ঘর ১ পড়তে পড়তে থামে; ফিতার শেষ-চিহ্ন অক্ষুণ্ণ রাখে; ঘর ০ থেকে বাঁ দিকে যাওয়ার চেষ্টা করে না | provisional-disciplined-machine-register | medium_definition_and_adjacent-canon_support | medium | 4 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T213` | combine Turing machines; constituent stages; relabel disjoint state sets; transfer control; combined machine | টুরিং যন্ত্রের সংযোজন; উপাংশ পর্যায়; বিযুক্ত দশা-সেটের জন্য নতুন নাম দেয়; নিয়ন্ত্রণ হস্তান্তর করে; সংযোজিত যন্ত্র | provisional-machine-combination-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T214` | variant; liberal definition; restrictive definition; transition relation; nondeterministic Turing machine | রূপভেদ; উদার সংজ্ঞা; সীমাবদ্ধ সংজ্ঞা; অবস্থান্তর সম্বন্ধ; অনির্ধারণবাদী টুরিং যন্ত্র | provisional-turing-variant-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T215` | one-way infinite tape; two-way infinite tape; multiple tapes; binary representation; simulate; extensionally equivalent | একমুখী অসীম ফিতা; দ্বিমুখী অসীম ফিতা; একাধিক ফিতা; দ্বিমিক উপস্থাপনা; অনুকরণ করে; বহির্বিস্তারণগতভাবে সমতুল্য | provisional-equivalent-machine-model-register | medium_definition_and_adjacent-canon_support | medium | 9 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T216` | effective procedure; Church--Turing thesis; pseudo-code; invoke the thesis; effectively unsolvable | কার্যকর পদ্ধতি; চার্চ--টুরিং থিসিস; ছদ্ম-কোড; থিসিস আহ্বান করে; কার্যকরভাবে অসমাধানযোগ্য | provisional-church-turing-use-register | medium_definition_and_adjacent-canon_support | medium | 25 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T217` | undecidability; uncomputable function; effectively decide a yes/no question; decision problem | অনির্ণেয়তা; অগণনসাধ্য অপেক্ষক; হ্যাঁ/না প্রশ্ন কার্যকরভাবে নির্ণয় করে; সিদ্ধান্ত সমস্যা | provisional-undecidability-register | medium_definition_and_adjacent-canon_support | medium | 28 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T218` | enumerate Turing machines; standard machine; rename states and symbols; finite integer description | টুরিং যন্ত্র তালিকায়িত করে; মানক যন্ত্র; দশা ও প্রতীকের নতুন নাম দেয়; পূর্ণসংখ্যার সসীম বর্ণনা | provisional-machine-enumeration-register | medium_definition_and_adjacent-canon_support | medium | 3 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025, BN-IN-P027, BN-IN-P028 | welcome/open to correction |
| `BN-IN-T219` | Turing-machine index; fixed enumeration; machine description; encode/decode an index | টুরিং-যন্ত্রের সূচক; স্থির তালিকায়ন; যন্ত্রের বর্ণনা; সূচক সংকেতায়িত/বিসংকেতায়িত করে | provisional-turing-index-register | medium_definition_and_adjacent-canon_support | medium | 7 | BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T220` | universal Turing machine; simulate an indexed machine; current state; current head position; encoded tape | সার্বজনীন টুরিং যন্ত্র; সূচকযুক্ত যন্ত্র অনুকরণ করে; বর্তমান দশা; বর্তমান হেডের অবস্থান; সংকেতায়িত ফিতা | provisional-universal-machine-register | medium_definition_and_adjacent-canon_support | medium | 6 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T221` | halting function; halting problem; diagonal self-input function; unsolvability | থামা-অপেক্ষক; থামার সমস্যা; কর্ণীয় স্ব-নিবেশ অপেক্ষক; অসমাধানযোগ্যতা | provisional-machine-halting-register | medium_definition_and_adjacent-canon_support | medium | 31 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T222` | hook machines together; copier machine; Three Halting problem; partial halting recognizer | যন্ত্র জুড়ে দেয়; অনুলিপিকারী যন্ত্র; তিন-থামা সমস্যা; আংশিক থামা-স্বীকর্তা | provisional-halting-reduction-register | medium_definition_and_adjacent-canon_support | medium | 2 | BN-IN-P001, BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T223` | validity decision problem; validity function; reduce the halting problem; machine-configuration sentences | সিদ্ধতার সিদ্ধান্ত সমস্যা; সিদ্ধতা-অপেক্ষক; থামার সমস্যাকে হ্রাস করে; যন্ত্র-কনফিগারেশনের বাক্য | provisional-entscheidungsproblem-register | medium_definition_and_adjacent-canon_support | medium | 1 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T224` | first-order machine language; numeral; instant; state; tape symbol | প্রথম-ক্রমের যুক্তিবিদ্যা; সংখ্যাপদ; মুহূর্ত; দশা; ফিতা-প্রতীক | provisional-first-order-machine-encoding-register | medium_definition_and_adjacent-canon_support | medium | 216 | BN-IN-P005, BN-IN-P006, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T225` | machine-description axioms; initial configuration; transition; halting configuration; frame condition | স্বতঃসিদ্ধ; আরম্ভিক কনফিগারেশন; অবস্থান্তর; থামার কনফিগারেশন; অপরিবর্তনশীলতার শর্ত | provisional-machine-description-axiom-register | medium_definition_and_adjacent-canon_support | medium | 240 | BN-IN-P005, BN-IN-P006, BN-IN-P007, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T226` | verification of the representation; induction over computation steps; run; reverse direction | উপস্থাপনের যাচাই; আরোহ; চালনা; বিপরীত দিক | provisional-machine-verification-proof-register | medium_definition_and_adjacent-canon_support | medium | 226 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T227` | semidecidable validity; effective enumeration of derivations; soundness; completeness | অর্ধ-নির্ণেয়; কার্যকর অ্যালগরিদম; নিগমন; যথার্থতা; সম্পূর্ণতা | provisional-semidecision-proof-enumeration-register | medium_definition_and_adjacent-canon_support | medium | 39 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T228` | Trakhtenbrot's theorem; finite satisfiability; finite validity; finite model; positive time | ট্রাখতেনব্রোটের উপপাদ্য; সসীম সন্তোষণীয়তা; সসীম সিদ্ধতা; সসীম মডেল; ধনাত্মক সময় | provisional-finite-model-undecidability-register | medium_definition_and_adjacent-canon_support | medium | 17 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T229` | incompleteness theorem; historical background; mathematical logic; foundations of mathematics | অসম্পূর্ণতা উপপাদ্য; ঐতিহাসিক পটভূমি; গাণিতিক যুক্তিবিদ্যা; গণিতের ভিত্তি | provisional-incompleteness-history-register | medium_definition_and_adjacent-canon_support | medium | 28 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T230` | theory; closure under entailment; true arithmetic; standard model | তত্ত্ব; অনুগমনের অধীনে আবদ্ধ; সত্য পাটিগণিতের; মানক মডেল | provisional-incompleteness-theory-register | medium_definition_and_adjacent-canon_support | medium | 278 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T231` | Robinson Q; Peano arithmetic; induction schema; axiomatized theory | রবিনসনের; পেয়ানো পাটিগণিত; আরোহ-ছক; স্বতঃসিদ্ধায়িত | provisional-arithmetic-theory-register | medium_definition_and_adjacent-canon_support | medium | 26 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T232` | decidable; axiomatizable; computable procedure; undecidability | নির্ণেয়; স্বতঃসিদ্ধায়িত; গণনপদ্ধতি; অণির্ণেয়তা | provisional-decidability-register | medium_definition_and_adjacent-canon_support | medium | 55 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |
| `BN-IN-T233` | independent sentence; Gödel sentence; provability; representation | স্বাধীন; গ্যোডেল বাক্য; প্রমাণযোগ্যতা; উপস্থাপন | provisional-incompleteness-proof-register | medium_definition_and_adjacent-canon_support | medium | 55 | BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023, BN-IN-P025 | welcome/open to correction |

## Detailed review entries

### BN-IN-T001

- Source term or concept: set
- Chosen Bengali: সেট
- Rationale: Shared modern form in university and Tripura evidence.
- Plausible alternatives: সমষ্টি is a plausible alternative for set; সেট follows the directly checked university and school sources and avoids conflating an arbitrary set with a sum or collection in ordinary prose.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সেট’ express the OpenLogic sense(s) ‘set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1174 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:23`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:61`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:68`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
```

### BN-IN-T002

- Source term or concept: element
- Chosen Bengali: উপাদান
- Rationale: Use for set elements; preserve member synonym সদস্য where source distinguishes wording.
- Plausible alternatives: সেটের মৌল and সদস্য are plausible alternatives for element; উপাদান preserves the source distinction between an element as an object and membership as a relation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উপাদান’ express the OpenLogic sense(s) ‘element’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 112 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:44-65` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:54`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:44-65` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:61`; final reader page pending
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:24-38` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:29`; final reader page pending
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:40-51` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:39`; final reader page pending
  - `OLP-0228` `upstream/content/computability/computability-theory/computability-theory.tex:10-13` → `bn-Beng-IN/content/computability/computability-theory/computability-theory.tex:11`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the second proof, suppose again that $A$ is enumerated by~$f$ and
$B$ is enumerated by~$g$. Let
\[
k(x) = \begin{cases}
f(x/2) & \text{if $x$ is even} \\
g((x-1)/2) & \text{if $x$ is odd.}
\end{cases}
\]
Then $k$ enumerates $A \cup B$; the idea is that $k$ just alternates
between the enumerations offered by $f$ and~$g$. Enumerating $A \cap
B$ is tricker. If $A \cap B$ is empty, it is trivially computably
enumerable. Otherwise, let $c$ be any element of $A \cap B$, and
define $l$ by
\[
l(x) = \begin{cases}
f((x)_0) & \text{if $f((x)_0) = g((x)_1)$} \\
c & \text{otherwise.}
\end{cases}
\]
In computational terms, $l$ runs through pairs of elements in the
enumerations of $f$ and $g$, and outputs every match it finds;
otherwise, it just stalls by outputting $c$.
```

### BN-IN-T003

- Source term or concept: member
- Chosen Bengali: সদস্য
- Rationale: Synonym in set context only.
- Plausible alternatives: উপাদান is a plausible alternative for member; সদস্য is directly attested and pairs transparently with সদস্যতা for the membership relation.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সদস্য’ express the OpenLogic sense(s) ‘member’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 57 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 94 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 107 occurrence(s). Representative locations:
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:17-21` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:18`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:15-27` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:15`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:18-28` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:20`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:16-22` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:22`; final reader page pending
  - `OLP-0231` `upstream/content/computability/computability-theory/normal-form.tex:38-54` → `bn-Beng-IN/content/computability/computability-theory/normal-form.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}
\ollabel{thm:ce-comp}
Let $A$ be any set of natural numbers. Then $A$ is computable if and
only if both $A$ and $\Complement{A}$ are computably enumerable.
\end{thm}
```

### BN-IN-T010

- Source term or concept: proposition (logic)
- Chosen Bengali: বচন
- Rationale: University philosophy form preferred; distinguish sentence বাক্য and school উক্তি.
- Plausible alternatives: উক্তি occurs in school material; বচন selected for the proposition sense from university philosophy.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বচন’ express the OpenLogic sense(s) ‘proposition (logic)’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 56 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 107 occurrence(s). Representative locations:
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:101-119` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:107`; final reader page pending
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:101-119` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:120`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:14`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:12-19` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:17`; final reader page pending
  - `OLP-0115` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:11-11` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex:11`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
  By convention, we take $\bforall{z < 0}{R(\vec x, z)}$ to be true
  (for the trivial reason that there are no $z$ less than~$0$) and
  $\bexists{z < 0}{R(\vec x, z)}$ to be false. A bounded
  universal quantifier functions just like a finite product or
  iterated minimum, i.e., if $P(\vec x, y) \defiff \bforall{z <
  y}{R(\vec x, z)}$ then $\Char{P}(\vec x, y)$ can be defined by
  \begin{align*}
    \Char{P}(\vec x, 0) & = 1\\
    \Char{P}(\vec x, y+1) & =
    \fn{min}(\Char{P}(\vec x, y), \Char{R}(\vec x, y)).
  \end{align*}
  Bounded existential quantification can similarly be defined using
  $\fn{max}$. Alternatively, it can be defined from bounded universal
  quantification, using the equivalence $\bexists{z < y}{R(\vec x, z)}
  \liff \lnot \bforall{z < y}{\lnot R(\vec x, z)}$. Note that, for
  example, a bounded quantifier of the form $\bexists{x \leq y}{\dots
  x\dots}$ is equivalent to $\bexists{x < y+1}{\dots x \dots}$.
\end{proof}
```

### BN-IN-T012

- Source term or concept: universal quantifier
- Chosen Bengali: সার্বিক পরিমাণসূচক
- Rationale: Retain source variable-binding convention.
- Plausible alternatives: সর্বজনীন পরিমাণসূচক and সকলবাচক পরিমাণসূচক are plausible alternatives; সার্বিক পরিমাণসূচক follows the attested সার্বিক root.
- Status: attested; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সার্বিক পরিমাণসূচক’ express the OpenLogic sense(s) ‘universal quantifier’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:34-63` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:42`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:91-104` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:99`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:134-141` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:134`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:211-235` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:200`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:211-235` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:204`; final reader page pending
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 259 occurrence(s). Representative locations:
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:28-42` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:37`; final reader page pending
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:29-37` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:37`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:15-27` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:16`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:15-27` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:17`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:54-72` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:60`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In the other direction, suppose $A$ and~$\Complement{A}$ are both
computably enumerable. Let $A$ be the domain of~$\cfind{d}$, and let
$\Complement{A}$ be the domain of~$\cfind{e}$. Define $h$ by
\[
h(x) = \umin{s}{(T(d,x,s) \lor T(e,x,s))}.
\]
In other words, on input~$x$, $h$~searches for either a halting
computation of~$\cfind{d}$ or a halting computation of~$\cfind{e}$.
Now, if $x \in A$, it will succeed in the first case, and if $x \in
\Complement{A}$, it will succeed in the second case. So, $h$~is a
total computable function. But now we have that for every~$x$, $x \in
A$ if and only if $T(e, x, h(x))$, i.e., if $\cfind{e}$ is the one
that is defined. Since $T(e, x, h(x))$ is a computable relation,
$A$~is computable.
\end{proof}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 119 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:74-81` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:79`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:18-27` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:22`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:91-100` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:91`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection[Union and Intersection of C.E. Sets]{Computably Enumerable
  Sets are Closed under Union and Intersection}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 346 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:22`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:18`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:34`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:156`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:158`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
```

### BN-IN-T020

- Source term or concept: paradox; contradiction; comprehension; naive set theory
- Chosen Bengali: কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব
- Rationale: Set/proposition evidence gives context only; no claim of direct attestation. Preserve distinction between conditional uniqueness and existence.
- Plausible alternatives: প্যারাডক্স, বিরোধ, অবাধ ধর্মগ্রহণ and সরল সেটতত্ত্ব are plausible alternatives; the selected forms distinguish a paradox from a formal contradiction and describe unrestricted comprehension without claiming direct canon attestation.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কূটাভাস; স্ববিরোধ; ধর্মনির্দেশে সেট গঠন; অনানুষ্ঠানিক সেটতত্ত্ব’ express the OpenLogic sense(s) ‘paradox; contradiction; comprehension; naive set theory’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 58 occurrence(s). Representative locations:
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:10`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:12`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:15`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:22-32` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:23`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:50-53` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:52`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{rus}
\olsection{Comparison with Russell's Paradox}
```

### BN-IN-T021

- Source term or concept: conjunction; conjunction elimination; absorption
- Chosen Bengali: সংযোজন; সংযোজন অপসারণ; শোষণ
- Rationale: Logic and set-operation witnesses inform wording; these exact normalized phrases are not claimed directly attested. Preserve Elim rule labels as formal notation.
- Plausible alternatives: অন্তঃসংযোগ is a directly witnessed regional alternative for conjunction; সংযোজন continues the edition-wide connective choice, while অপসারণ and শোষণ identify the formal rule and law.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংযোজন; সংযোজন অপসারণ; শোষণ’ express the OpenLogic sense(s) ‘conjunction; conjunction elimination; absorption’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 37 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:84-86` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:78`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:108-141` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:138`; final reader page pending
  - `OLP-0151` `upstream/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:34-63` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/first-order-languages.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection[Union and Intersection of C.E. Sets]{Computably Enumerable
  Sets are Closed under Union and Intersection}
```

### BN-IN-T022

- Source term or concept: relation; binary relation; order relation; identity relation
- Chosen Bengali: সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক
- Rationale: সম্পর্ক and set-based relation definition are directly attested; binary/order/identity compounds follow source definitions and are provisionally normalized.
- Plausible alternatives: চিত্রণ is reserved for mapping/function use; সম্পর্ক is directly attested for relation.
- Status: mixed-attested-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সম্পর্ক; দ্বিপদ সম্পর্ক; ক্রমসম্পর্ক; অভিন্নতার সম্পর্ক’ express the OpenLogic sense(s) ‘relation; binary relation; order relation; identity relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 305 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:21-23` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:24`; final reader page pending
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:30-45` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:31`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:73-89` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:79`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:73-89` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:80`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:73-89` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:81`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In other words, complete computably enumerable sets are the
``hardest'' computably enumerable sets possible. They allow one to
answer questions about \emph{any} computably enumerable set.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 19 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 38 occurrence(s). Representative locations:
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:38-41` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:38`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:119-122` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:118`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:124-140` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:129`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:156-168` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:155`; final reader page pending
  - `OLP-0221` `upstream/content/computability/recursive-functions/trees.tex:37-68` → `bn-Beng-IN/content/computability/recursive-functions/trees.tex:44`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We'll now show that the operations of determining the length of a
sequence, determining its $i$th element, appending an element to a
sequence, and concatenating two sequences, are all primitive
recursive.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 75 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 33 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 492 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:62`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:63`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:123`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:159`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T032

- Source term or concept: inverse relation; relative product; restriction; application; transitive closure
- Chosen Bengali: বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ
- Rationale: Existing university evidence attests pair/set operations and transitivity but not these exact operator names. Inverse swaps coordinates; relative-product direction follows source R then S. Restriction here cuts both coordinates to A; application is relational image, not necessarily a function.
- Plausible alternatives: উল্টো সম্পর্ক, সম্পর্ক-সংযোজন, সংকোচন, প্রতিবিম্ব and পরিযায়ী সংবরণ are plausible alternatives; the selected terms distinguish inversion, relative product, restriction, application and closure as separate operations.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিপরীত সম্পর্ক; আপেক্ষিক গুণফল; সীমাবদ্ধন; প্রয়োগ; পরিযায়ী আবরণ’ express the OpenLogic sense(s) ‘inverse relation; relative product; restriction; application; transitive closure’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 211 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:10`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:46`; final reader page pending
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:46`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:52`; final reader page pending
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:12-12` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{apf}
\olsection{Applying the Fixed-Point Theorem}
```

### BN-IN-T033

- Source term or concept: formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma
- Chosen Bengali: সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য
- Rationale: Early Trees mentions require these terms before their full chapters. Quantification/proposition and university mathematical prose provide context, not direct name attestation. Token IDs remain untouched; reader expansion uses these provisional terms. Later logic-specific canon may refine wording without changing formal definitions.
- Plausible alternatives: সুসম্বদ্ধ সূত্র, অবরোহ, প্রস্তাবনা যুক্তিবিদ্যা, প্রথম ঘাতের যুক্তিবিদ্যা, সম্পূর্ণতা and পরিগণনাযোগ্যতা are plausible alternatives; the selected vocabulary aligns with the project tokens and preserves syntactic, semantic and computational distinctions.
- Status: provisional-contextual; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সূত্র; নিষ্পাদন; বচনমূলক যুক্তিবিদ্যা; প্রথম-ক্রমের যুক্তিবিদ্যা; পূর্ণতা; গণনাযোগ্যতা; ক্যোনিগের সহায়ক উপপাদ্য’ express the OpenLogic sense(s) ‘formula; derivation; propositional logic; first-order logic; completeness; computability; König's lemma’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 341 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:203-208` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:205`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:64-73` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:71`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:20`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:23`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:26-30` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For now, it is o.k.\ if you want to think of the proof as formal
trickery, or black magic. But you should be able to reconstruct the
details of the argument given above. When we prove the incompleteness
theorems (and the related ``fixed-point theorem'') we will discuss
other ways of understanding why it works.
\end{explain}
```

### BN-IN-T034

- Source term or concept: variable; constant; sum; arithmetic product; equation
- Chosen Bengali: চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ
- Rationale: Freshly consulted recovered West Bengal and Tripura pages supplement university witnesses. Applies to arithmetic/algebra senses; does not claim logical term, model-theoretic constant or first-order formula attestation. New evidence is not retroactively attributed to earlier drafting.
- Plausible alternatives: চলরাশি and অচল are plausible alternatives for variable and constant; চল and ধ্রুবক follow the checked school algebra page, while যোগফল, গুণফল and সমীকরণ are directly supported there.
- Status: attested-in-school-algebra; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চল; ধ্রুবক; যোগফল; গুণফল; সমীকরণ’ express the OpenLogic sense(s) ‘variable; constant; sum; arithmetic product; equation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 329 occurrence(s). Representative locations:
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:17-22` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:20`; final reader page pending
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:24-38` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:33`; final reader page pending
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:12-32` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:15`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:47-51` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:46`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:178`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{history}
Computably enumerable sets are also called \emph{recursively
  enumerable} instead. This is the original terminology, and today
both are commonly used, as well as the abbreviations ``c.e.'' and
``r.e.''
\end{history}
```

### BN-IN-T035

- Source term or concept: function; mapping; domain; codomain; range; image/value
- Chosen Bengali: অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান
- Rationale: NSOU PDF370 directly supplies the function definition and these roles. Codomain may strictly contain the range. প্রতিবিম্ব labels the mapped object and মান the function value; scope separates this from the reflexivity property.
- Plausible alternatives: ফলন, মানচিত্রণ, ক্ষেত্র, সহক্ষেত্র, মানসমষ্টি and চিত্র are plausible alternatives; অপেক্ষক and চিত্রণ follow the checked university source, and the selected domain/range family keeps each set role explicit.
- Status: attested-university; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অপেক্ষক; চিত্রণ; সংজ্ঞাক্ষেত্র; সহসংজ্ঞাক্ষেত্র; বিস্তৃতি; প্রতিবিম্ব/মান’ express the OpenLogic sense(s) ‘function; mapping; domain; codomain; range; image/value’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1581 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:21`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:24`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:25`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:28-32` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:29`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T036

- Source term or concept: function argument; input; output; black box; extensionality for functions
- Chosen Bengali: আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি
- Rationale: University mapping and freshly consulted recovered variable/equation prose support explanations. Input/output/argument are explicit provisional loans; function argument is not logical argument (যুক্তি). Function extensionality requires same domain/codomain and equal values at every argument; equation-operation evidence is prose support only.
- Plausible alternatives: পরামিতি, নিবেশ, নির্গম, অস্বচ্ছ বাক্স and বহির্বিস্তার নীতি are plausible Bengali alternatives; the selected loans are familiar in technical prose, while মানভিত্তিক সমতার নীতি states the governing extensional condition.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আর্গুমেন্ট; ইনপুট; আউটপুট; ব্ল্যাক বক্স; মানভিত্তিক সমতার নীতি’ express the OpenLogic sense(s) ‘function argument; input; output; black box; extensionality for functions’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 60 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:124`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:181-201` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:183`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:37-51` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:42`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:66-82` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:75`; final reader page pending
  - `OLP-0232` `upstream/content/computability/computability-theory/s-m-n.tex:30-41` → `bn-Beng-IN/content/computability/computability-theory/s-m-n.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
The ingredients are already implicit in the discussion of the halting
problem above. Let $\fn{diag}(x)$ be a computable function which for each
$x$ returns an index for the function $f_x(y) \simeq \cfind{x}(x,y)$,
i.e.
\[
\cfind{\fn{diag}(x)}(y) \simeq \cfind{x}(x,y).
\]
Think of $\fn{diag}$ as a function that transforms a program for a 2-ary
function into a program for a 1-ary function, obtained by fixing the
original program as its first argument. The function $\fn{diag}$ can be
defined formally as follows: first define $s$ by
\[
s(x,y) \simeq \fn{Un}^2(x,x,y),
\]
where $\fn{Un}^2$ is a 3-ary function that is universal for partial computable
2-ary functions. Then, by the $s$-$m$-$n$ theorem, we can find a primitive
recursive function $\fn{diag}$ satisfying
\[
\cfind{\fn{diag}(x)}(y) \simeq s(x,y).
\]
```

### BN-IN-T037

- Source term or concept: injective/injection; surjective/surjection; bijective/bijection; identity function
- Chosen Bengali: একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক
- Rationale: NSOU directly attests একৈক, সমাপতিত, সমরূপ and অভেদ চিত্রণ. Prefer its explicit compound একৈক সমাপতিত for bijective to keep সমরূপ available for later isomorphism distinctions. Replace mapping noun with the already attested অপেক্ষক when translating function; noun/adjective token variants remain separate. Earlier identity-function prose will be harmonized at reader integration.
- Plausible alternatives: সমরূপ চিত্রণ is directly printed for bijective; একৈক সমাপতিত selected to avoid collision with later isomorphism.
- Status: attested-university-with-normalization; confidence: high_for_attested_scope; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘একৈক/একৈক অপেক্ষক; সমাপতিত/সমাপতিত অপেক্ষক; একৈক সমাপতিত/একৈক সমাপতিত অপেক্ষক; অভেদ অপেক্ষক’ express the OpenLogic sense(s) ‘injective/injection; surjective/surjection; bijective/bijection; identity function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 25 occurrence(s). Representative locations:
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:24-38` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:31`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:13-23` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:14`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:27-36` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:33`; final reader page pending
  - `OLP-0193` `upstream/content/model-theory/models-of-arithmetic/standard-models.tex:115-125` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/standard-models.tex:122`; final reader page pending
  - `OLP-0022` `upstream/content/sets-functions-relations/functions/function-kinds.tex:80-81` → `bn-Beng-IN/content/sets-functions-relations/functions/function-kinds.tex:58`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
You should think about what the definition means, and why the
terminology is appropriate. The idea is that if $S$ is the range of
the computable function~$f$, then
\[
S = \{ f(0), f(1), f(2), \dots \},
\]
and so $f$ can be seen as ``enumerating'' the elements of~$S$. Note
that according to the definition, $f$~need not be an increasing
function, i.e., the enumeration need not be in increasing order. In
fact, $f$ need not even be injective, i.e., repetitions in the
enumeration $f(0)$, $f(1)$, $f(2)$, \dots{} of~$S$ are allowed. For
instance, the constant function $f(x) = 0$ enumerates the set $\{ 0
\}$.
\end{explain}
```

### BN-IN-T038

- Source term or concept: inverse function; left inverse; right inverse; composition
- Chosen Bengali: বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ
- Rationale: বিপরীত চিত্রণ and মিশ্র চিত্রণ are directly attested. মিশ্রণ is the normalized operation noun; left/right inverse compounds are provisional and defined by their respective equations. Composition applies f before g; no attestation of arbitrary choice or empty-domain claims is inferred.
- Plausible alternatives: ব্যস্ত অপেক্ষক, বাঁ/ডান ব্যস্ত and যৌগ are plausible alternatives; বিপরীত অপেক্ষক, বাম/ডান বিপরীত and মিশ্রণ follow the checked inverse/composition roots and retain the order fixed by the formulas.
- Status: attested-root-with-provisional-normalization; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিপরীত অপেক্ষক; বাম বিপরীত; ডান বিপরীত; মিশ্রণ’ express the OpenLogic sense(s) ‘inverse function; left inverse; right inverse; composition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 51 occurrence(s). Representative locations:
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:9-10` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:10`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:12-15` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:14`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:82`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:87`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:13-23` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:16`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{rec}{com}
\olsection{Composition}
```

### BN-IN-T039

- Source term or concept: partial function; total function; functional relation; serial relation; Axiom of Choice
- Chosen Bengali: আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ
- Rationale: University relations and total mappings support concept and proof prose, not direct attestation of these extensions. Serial is a provisional loan immediately defined by existence of an output for each input. Partial means at most one output; total means exactly one for every input in the specified ambient set. Choice and one-sided inverse hypotheses remain those in OpenLogic, with separate source notes for defects.
- Plausible alternatives: পূর্ণ অপেক্ষক versus সর্বত্র সংজ্ঞায়িত অপেক্ষক; the descriptive form exposes totality and avoids collision with completeness/full order.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক অপেক্ষক; সর্বত্র সংজ্ঞায়িত অপেক্ষক; অপেক্ষকধর্মী সম্পর্ক; সিরিয়াল সম্পর্ক; নির্বাচন স্বতঃসিদ্ধ’ express the OpenLogic sense(s) ‘partial function; total function; functional relation; serial relation; Axiom of Choice’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 40 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:67-70` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:65`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:67-70` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:66`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:67-70` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:67`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:32-40` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:32`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:32-40` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:34`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For the last proof, suppose $A$ is the \emph{domain} of the partial
function $m(x)$ and $B$ is the domain of the partial function
$n(x)$. Then $A \cap B$ is the domain of the partial function $m(x) +
n(x)$.
```

### BN-IN-T040

- Source term or concept: size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable
- Chosen Bengali: সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয়
- Rationale: NSOU directly attests finite/infinite sets and finite cardinality's মাত্রা/অঙ্কবাচক সংখ্যা. সেটের আকার is a descriptive chapter title, not geometric shape or dimension. Enumeration/listability and countability terms remain provisional: the elementary and abstract source sections give different definitions, so their own finite/empty-set conventions govern. No computable-enumerability meaning is imported. Infinite cardinality and actual infinity are not directly attested on these pages.
- Plausible alternatives: গণনীয় versus তালিকায়নযোগ্য; elementary enumeration sections use তালিকায়নযোগ্য, while গণনীয় is reserved as a possible later countability/computability-sensitive term.
- Status: mixed-attested-and-provisional; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সেটের আকার; সসীম/অসীম; সেটের মাত্রা (অঙ্কবাচক সংখ্যা); তালিকায়ন; তালিকায়নযোগ্য/গণনীয়; অগণনীয়’ express the OpenLogic sense(s) ‘size of sets; finite/infinite; cardinality; enumeration; enumerable/countable; uncountable’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 517 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:22`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:14-15` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:14`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:17-20` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:17`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:22-25` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 33 occurrence(s). Representative locations:
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:12-15` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:14`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:109-120` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:104`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:17`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:24`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:23`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Suppose $A$ is computably enumerable. Is the complement of~$A$,
$\Complement{A} = \Nat \setminus A$, always computably enumerable
as well? The following theorem and corollary show that the answer is
``no.''
```

### BN-IN-T043

- Source term or concept: zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function
- Chosen Bengali: আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক
- Rationale: Freshly reread university ordered-pair/product/complement summary and recovered West Bengal algebraic operations/factorization page before these drafts. They attest underlying pair/product and arithmetic prose, not the specialized coding or Cantor names. Pairing means an injective numerical encoding; its inverse can be partial. Cofinite is immediately defined by a finite complement in the naturals. Truth function is explicitly distinguished from a propositional function; no direct name attestation is claimed.
- Plausible alternatives: জোড়া-লাগানো অপেক্ষক / pairing-function loan; যুগলায়ন selected as a concise provisional compound.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আঁকাবাঁকা পথের পদ্ধতি; যুগলায়ন অপেক্ষক; সংকেতায়ন/সংকেত/সংকেতোদ্ধার; ত্রিভুজসংখ্যা; সহসসীম; সত্যসারণি/সত্যমান-অপেক্ষক’ express the OpenLogic sense(s) ‘zig-zag method; pairing function; encode/code/decode; triangular number; cofinite; truth table/truth function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 255 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:10`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:29`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:32`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:33`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:34`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{cod}
\olsection{Coding Computations}
```

### BN-IN-T044

- Source term or concept: non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence
- Chosen Bengali: অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম
- Rationale: Checked university set, quantification, proof-prose and finite/infinite pages do not directly attest Cantor's diagonal terminology. অতালিকায়নযোগ্য mirrors the elementary source definition by absence of an enumeration; অগণনীয় is reserved as a conventional alternative. কর্ণ is the matrix diagonal, not an anatomical claim. The constructed binary sequence flips each diagonal bit, so the descriptive phrase avoids suggesting geometric reflection. Source formulas and universal counter-list argument determine the meaning.
- Plausible alternatives: অগণনযোগ্য, কর্ণীয় পদ্ধতি, কর্ণায়ন, একমুখী অসীম তালিকা and পরিপূরক-বিট অনুক্রম are plausible alternatives; the selected terms remain tied to absence of enumeration and the explicit diagonal bit flip.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অতালিকায়নযোগ্য/অগণনীয়; কর্ণ পদ্ধতি; কর্ণীকরণ; একদিকে অসীম তালিকা; বিপরীত-বিট অনুক্রম’ express the OpenLogic sense(s) ‘non-enumerable/uncountable; diagonal method; diagonalization; one-way infinite list; mirror sequence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 18 occurrence(s). Representative locations:
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:24-33` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:27`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:38`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:41`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:43-49` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:45`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:37-48` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
The proof is a simple diagonalization: if $\fn{Un}'(k,x)$ were total
and computable, then
\[
d(x) = \fn{Un}'(x, x) + 1
\]
would also be total and computable. However, by definition, $d(k)$ is
not equal to $\fn{Un}'(k,k)$. Hence, for every $k$, the values of
$d(x)$ and~$\fn{Un}'(k, x)$ differ for at least one~$x$, namely $x = k$.
\end{proof}
```

### BN-IN-T045

- Source term or concept: reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction
- Chosen Bengali: হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ
- Rationale: Checked logic, set and function sources support implication and mapping prose but do not directly attest problem reduction or characteristic sequences. হ্রাসকরণ means transforming a presumed enumeration of A into one of B; it is not subtraction, quotienting or proof simplification. The surjection must run from A to B for the contradiction used here. The binary sequence is the membership indicator of a subset of positive integers.
- Plausible alternatives: রিডাকশন, চরিত্রাঙ্ক অনুক্রম, নিঃশেষে তালিকাভুক্ত করা and হ্রাসের দিক are plausible alternatives; the selected wording exposes the transformation and its source-to-target orientation.
- Status: provisional-descriptive; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হ্রাসকরণ; নির্দেশক অনুক্রম; সেটের সব উপাদান অন্তর্ভুক্ত করা; হ্রাসের অভিমুখ’ express the OpenLogic sense(s) ‘reduction (of one enumeration problem to another); characteristic sequence; exhaust a set; reduction direction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 33 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:47-49` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:50`; final reader page pending
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:30-45` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:41`; final reader page pending
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:70-81` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:77`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:24-27` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:24`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:24-27` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:25`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
Give a reduction of $K$ to $K_0$.
\end{prob}
```

### BN-IN-T046

- Source term or concept: equinumerous/equinumerosity; same cardinality; cardinal equality
- Chosen Bengali: সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা
- Rationale: NSOU directly attests finite cardinality as setের মাত্রা/অঙ্কবাচক সংখ্যা and equivalence-relation proof vocabulary, but not infinite equinumerosity. সমসংখ্যকতা is selected as a transparent property name defined by existence of a bijection. মাত্রাসমতা is recorded as a notation-oriented alternative but could suggest geometric dimension. The relation is proved reflexive, symmetric and transitive using identity, inverse and composition.
- Plausible alternatives: সমানসংখ্যক, সমঅঙ্কবাচক and কার্ডিনাল সমতা are plausible alternatives; সমসংখ্যকতা and মাত্রাসমতা remain explicitly defined by existence of a bijection.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সমসংখ্যক/সমসংখ্যকতা; একই অঙ্কবাচকতা; মাত্রাসমতা’ express the OpenLogic sense(s) ‘equinumerous/equinumerosity; same cardinality; cardinal equality’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
  - `OLP-0197` `upstream/content/model-theory/models-of-arithmetic/computable-models.tex:42-75` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/computable-models.tex:68`; final reader page pending
  - `OLP-0036` `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:13-24` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/comparing-size.tex:14`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11-11` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:29-32` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:20`; final reader page pending
  - `OLP-0035` `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:34-36` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:24`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}\ollabel{ex:comp-model-q}
Recall the structure $\Struct{K}$ from \olref[mdq]{ex:model-K-of-Q}.
Its domain was $\Domain{K} = \Nat
\cup \{a\}$ and interpretations
\begin{align*}
  \Assign{\Obj{0}}{K} & = 0\\
  \Assign{\prime}{K}(x) & =
  \begin{cases}
    x+1 & \text{if $x\in \Nat$}\\
    a & \text{if $x = a$}
  \end{cases}\\
  \Assign{+}{K}(x, y) & =
  \begin{cases}
    x+y & \text{if $x$, $y \in\Nat$}\\
    a & \text{otherwise}
  \end{cases}\\
  \Assign{\times}{K}(x, y) & =
  \begin{cases}
    xy & \text{if $x$, $y \in\Nat$}\\
    0 & \text{if $x=0$ or $y=0$}\\
    a & \text{otherwise}\\
  \end{cases}\\
  \Assign{<}{K} & =
  \Setabs{\tuple{x,y}}{x, y \in \Nat \text{ and } x<y} \cup
  \Setabs{\tuple{x,a}}{n \in \Domain{K}}
\end{align*}
But $\Domain{K}$ is !!{denumerable} and so is equinumerous
with~$\Nat$. For instance, $g\colon \Nat \to \Domain{K}$ with $g(0) =
a$ and $g(n) = n+1$ for $n>0$ is !!a{bijection}.  We can turn it into
an isomorphism between a new model~$\Struct{K'}$ of~$\Th{Q}$ and
$\Struct{K}$.  In $\Struct{K'}$, we have to assign different functions
and relations to the symbols of~$\Lang{L_A}$, since different
!!{element}s of~$\Nat$ play the roles of standard and non-standard
numbers.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 86 occurrence(s). Representative locations:
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:162-168` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:163`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:17`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:76-78` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:80`; final reader page pending
  - `OLP-0161` `upstream/content/first-order-logic/syntax-and-semantics/structures.tex:67-73` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/structures.tex:69`; final reader page pending
  - `OLP-0276` `upstream/content/incompleteness/introduction/historical-background.tex:92-110` → `bn-Beng-IN/content/incompleteness/introduction/historical-background.tex:83`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
Show that integer division $d(x, y) = \lfloor x/y \rfloor$ (i.e.,
division, where you disregard everything after the decimal point) is
primitive recursive. When $y = 0$, we stipulate $d(x, y) = 0$. Give an
explicit definition of~$d$ using primitive recursion and
composition.
\end{prob}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 45 occurrence(s). Representative locations:
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:37-43` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:34`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:45-47` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:39`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:123-154` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:125`; final reader page pending
  - `OLP-0276` `upstream/content/incompleteness/introduction/historical-background.tex:92-110` → `bn-Beng-IN/content/incompleteness/introduction/historical-background.tex:85`; final reader page pending
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 26 occurrence(s). Representative locations:
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:39`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:197`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:158-215` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:172`; final reader page pending
  - `OLP-0048` `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:169-171` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/cauchy.tex:100`; final reader page pending
  - `OLP-0047` `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:10-11` → `bn-Beng-IN/content/sets-functions-relations/arithmetization/checking-details.tex:11`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
\olref[uni]{thm:univ-comp} above shows that we can get around this
diagonalization argument, but only at the expense of allowing the
universal function to be partial. That is, $\fn{Un}$ is universal for
the total computable functions, it just isn't total. The
diagonalization argument doesn't work in the partial case.
\end{explain}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 23 occurrence(s). Representative locations:
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:68-73` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:68`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:19`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:21`; final reader page pending
  - `OLP-0135` `upstream/content/first-order-logic/completeness/compactness.tex:15-27` → `bn-Beng-IN/content/first-order-logic/completeness/compactness.tex:23`; final reader page pending
  - `OLP-0173` `upstream/content/first-order-logic/models-theories/size-of-structures.tex:63-70` → `bn-Beng-IN/content/first-order-logic/models-theories/size-of-structures.tex:70`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{digress}
It is true, but by no means obvious, that one-one reducibility really
is a stronger requirement than many-one reducibility. In other words,
there are infinite sets $A$ and~$B$ such that $A$ is many-one
reducible to~$B$ but not one-one reducible to~$B$.
\end{digress}
```

### BN-IN-T057

- Source term or concept: Dedekind algebra; successor function; self-map; f-closed set; closure under f
- Chosen Bengali: ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ
- Rationale: The checked relation, mapping, injection, proof and infinite-set pages support the mathematical prose but do not directly attest these structural compounds. বীজগঠন names the triple consisting of a carrier, a self-map and a distinguished element rather than the school subject of algebra. স্ব-অপেক্ষক makes the common domain/codomain carrier explicit where the frozen lemma leaves A unbound. Closure is the intersection-defined least f-closed set containing the stated seed, and is distinct from topological closure.
- Plausible alternatives: ডেডেকিন্ড বীজগণিত, পরবর্তী অপেক্ষক, স্বচিত্রণ, f-সংবৃত সেট and f-সংবরণ are plausible alternatives; the selected terms distinguish the carrier structure, endomap and least closed set.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ডেডেকিন্ড বীজগঠন; উত্তরসূরি অপেক্ষক; স্ব-অপেক্ষক; f-বদ্ধ সেট; f-এর অধীনে আবরণ’ express the OpenLogic sense(s) ‘Dedekind algebra; successor function; self-map; f-closed set; closure under f’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 30 occurrence(s). Representative locations:
  - `OLP-0211` `upstream/content/computability/recursive-functions/primitive-recursion.tex:71-97` → `bn-Beng-IN/content/computability/recursive-functions/primitive-recursion.tex:68`; final reader page pending
  - `OLP-0197` `upstream/content/model-theory/models-of-arithmetic/computable-models.tex:77-98` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/computable-models.tex:78`; final reader page pending
  - `OLP-0192` `upstream/content/model-theory/models-of-arithmetic/introduction.tex:12-39` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/introduction.tex:15`; final reader page pending
  - `OLP-0193` `upstream/content/model-theory/models-of-arithmetic/standard-models.tex:75-113` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/standard-models.tex:84`; final reader page pending
  - `OLP-0193` `upstream/content/model-theory/models-of-arithmetic/standard-models.tex:152-171` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/standard-models.tex:168`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In the definition of $\Add$ we used $+$ on the right-hand-side of
the second equation, but only to add~$1$. In other words, we used the
successor function $\Succ(z) = z+1$ and applied it to the previous value
$\Add(x,y)$ to define $\Add(x,y+1)$. So we can think of the
recursive definition as given in terms of a single function which we
apply to the previous value. However, it doesn't hurt---and sometimes
is necessary---to allow the function to depend not just on the previous
value but also on $x$ and~$y$. Consider:
\begin{align*}
  \Mult(x,0) & =  0 \\
  \Mult(x,y+1) & =  \Add(\Mult(x,y),x)
\end{align*}
This is a primitive recursive definition of a function $\Mult$ by
applying the function $\Add$ to both the preceding value
$\Mult(x,y)$ and the first argument~$x$. It also defines the
function~$\Mult(x,y)$ for all arguments $x$ and~$y$. For instance,
$\Mult(2,3)$ is determined by successively computing $\Mult(2,0)$,
$\Mult(2,1)$, $\Mult(2,2)$, and~$\Mult(2,3)$:
\begin{align*}
  \Mult(2,0) & = 0\\
  \Mult(2,1) & = \Mult(2,0+1) =
  \Add(\Mult(2,0), 2) = \Add(0, 2) = 2\\
  \Mult(2,2) & = \Mult(2,1+1) =
  \Add(\Mult(2,1), 2) = \Add(2, 2) = 4\\
  \Mult(2,3) & = \Mult(2,2+1) =
  \Add(\Mult(2,2), 2) = \Add(4, 2) = 6
\end{align*}
```

### BN-IN-T058

- Source term or concept: parameter of a formula; free variable; recursive definition
- Chosen Bengali: সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা
- Rationale: University quantification and school algebra pages directly support formula and variable prose, while the exact parameter/free-variable compounds and recursive-definition label remain provisional. A parameter is an additional freely assignable object in phi(x,c1,...,ck). Recursive definition fixes later values through the displayed base and successor clauses; it does not by itself claim effective computability. This concise label refines the descriptive recursive wording in T042 without changing that earlier sense.
- Plausible alternatives: সূত্রের সহগ, অবদ্ধ চল and আবর্ত সংজ্ঞা are plausible alternatives; পরামিতি, মুক্ত চলরাশি and পুনরাবৃত্ত সংজ্ঞা preserve the syntactic and recursive senses fixed by the formulas.
- Status: provisional-normalized; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সূত্রের পরামিতি; মুক্ত চলরাশি; পুনরাবৃত্ত সংজ্ঞা’ express the OpenLogic sense(s) ‘parameter of a formula; free variable; recursive definition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 35 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:15`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:56`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:29-45` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:34`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:58-76` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:62`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:83-97` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:82`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 65 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:84-86` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:78`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:115`; final reader page pending
  - `OLP-0129` `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:33-52` → `bn-Beng-IN/content/first-order-logic/completeness/complete-consistent-sets.tex:36`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection[Union and Intersection of C.E. Sets]{Computably Enumerable
  Sets are Closed under Union and Intersection}
```

### BN-IN-T063

- Source term or concept: denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation
- Chosen Bengali: অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ
- Rationale: The exact compounds are sparse in the checked canon, so the source definitions govern them. অসীম গণনীয় distinguishes denumerable from the finite-inclusive countable usage recorded in T040. প্রতীকক্রম continues T019. Syntactic identity requires equal length and the same symbol at every place; it is distinct from semantic equivalence. A defined symbol is an abbreviation rather than a primitive member of the language.
- Plausible alternatives: ক্রমগণনীয় was considered for denumerable; অসীম গণনীয় makes the exclusion of finite sets explicit. সমানতা was not used for syntactic identity because the relation concerns literal symbol-by-symbol identity rather than equality of denotation or truth value.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অসীম গণনীয়; পরমাণু সূত্র; মৌলিক/সংজ্ঞায়িত সংকেত; সংকেতবিন্যাসগত অভিন্নতা; প্রতীকক্রম/উপপ্রতীকক্রম/সংযুক্তকরণ’ express the OpenLogic sense(s) ‘denumerable; atomic formula; primitive/defined symbol; syntactic identity; string/substring/concatenation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 191 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:42-44` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:37`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:156`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:158`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:159`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:160`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
This fundamental fact is very powerful, and allows us to prove a
number of striking and important results about computability,
independently of the model of computation chosen.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 188 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 156 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 192 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:54`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:58`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:12-17` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:15`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:19-29` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:20`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:17-27` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To show that a function is computable, there are
two ways one can proceed:
\begin{enumerate}
\item Rigorously: describe a Turing machine or partial recursive
  function explicitly, and show that it computes the function you have
  in mind;
\item Informally: describe an algorithm that computes it, and appeal to
  Church's thesis.
\end{enumerate}
There is no fine line between the two; a detailed description of
an algorithm should provide enough information so that it is
relatively clear how one could, in principle, design the right Turing
machine or sequence of partial recursive definitions. Fully rigorous
definitions are unlikely to be informative, and we will try to find a
happy medium between these two approaches; in short, we will try to
find intuitive yet rigorous proofs that the precise definitions could
be obtained.
```

### BN-IN-T069

- Source term or concept: soundness; completeness; consistency/inconsistency; syntactic counterpart
- Chosen Bengali: বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ
- Rationale: T033 already records পূর্ণতা. The remaining proof-theoretic compounds were not directly attested in the checked canon and therefore remain governed by the adjacent biconditionals. বিশুদ্ধতা is the direction from derivability to entailment or validity; পূর্ণতা is the converse. Syntactic consistency is required to coincide with semantic satisfiability, so সঙ্গতি is kept distinct from both semantic truth and formula equivalence.
- Plausible alternatives: যথার্থতা and শুদ্ধতা were considered for soundness; বিশুদ্ধতা remains provisional and is fixed by the explicit derivability-to-entailment direction. সামঞ্জস্য was considered for consistency; সঙ্গতি is shorter and remains distinct from semantic equivalence by definition.
- Status: provisional-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিশুদ্ধতা; পূর্ণতা; সঙ্গতি/অসঙ্গতি; সংকেতবিন্যাসগত প্রতিরূপ’ express the OpenLogic sense(s) ‘soundness; completeness; consistency/inconsistency; syntactic counterpart’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 192 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:203-208` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:205`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:15-24` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:23`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:38-41` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:38`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:13`; final reader page pending
  - `OLP-0121` `upstream/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:15-17` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/provability-consistency.tex:16`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For now, it is o.k.\ if you want to think of the proof as formal
trickery, or black magic. But you should be able to reconstruct the
details of the argument given above. When we prove the incompleteness
theorems (and the related ``fixed-point theorem'') we will discuss
other ways of understanding why it works.
\end{explain}
```

### BN-IN-T070

- Source term or concept: axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens
- Chosen Bengali: স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স
- Rationale: The checked logic and proof pages support স্বতঃসিদ্ধ, formula and proof register, but not the complete proof-system terminology. Each axiom schema denotes a fixed form with substitution instances rather than one sentence. A line is সমর্থিত when it is an axiom, a stated premise or follows by an inference rule. মোডাস পোনেন্স is transliterated because no directly attested India-standard Bengali replacement was found in the checked pages.
- Plausible alternatives: স্বতঃসিদ্ধমূলক অবরোহ was considered, but নিষ্পাদন keeps the system aligned with the project derivation token. ন্যায়সংগত পংক্তি was considered for justified line; সমর্থিত পংক্তি more directly marks that a listed axiom, premise or rule warrants the step.
- Status: provisional-formally-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বতঃসিদ্ধমূলক নিষ্পাদন; স্বতঃসিদ্ধ-ছক/পদ্ধতি; অনুমান-বিধি; সমর্থিত পংক্তি; মোডাস পোনেন্স’ express the OpenLogic sense(s) ‘axiomatic derivation; axiom schema/system; rule of inference; justified line; modus ponens’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 264 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:54`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:58`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:12-17` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:15`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:19-29` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:20`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:17-27` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
To show that a function is computable, there are
two ways one can proceed:
\begin{enumerate}
\item Rigorously: describe a Turing machine or partial recursive
  function explicitly, and show that it computes the function you have
  in mind;
\item Informally: describe an algorithm that computes it, and appeal to
  Church's thesis.
\end{enumerate}
There is no fine line between the two; a detailed description of
an algorithm should provide enough information so that it is
relatively clear how one could, in principle, design the right Turing
machine or sequence of partial recursive definitions. Fully rigorous
definitions are unlikely to be informative, and we will try to find a
happy medium between these two approaches; in short, we will try to
find intuitive yet rigorous proofs that the precise definitions could
be obtained.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 252 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 209 occurrence(s). Representative locations:
  - `OLP-0211` `upstream/content/computability/recursive-functions/primitive-recursion.tex:53-69` → `bn-Beng-IN/content/computability/recursive-functions/primitive-recursion.tex:56`; final reader page pending
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:58-80` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:61`; final reader page pending
  - `OLP-0144` `upstream/content/first-order-logic/introduction/sentences.tex:29-52` → `bn-Beng-IN/content/first-order-logic/introduction/sentences.tex:29`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:57-96` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:77`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:116-147` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:114`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We can define even more fundamental functions like addition and
multiplication by primitive recursion. In these cases, however, the
functions in question are $2$-place. We fix one of the argument
places, and use the other for the recursion. E.g, to define
$\Add(x, y)$ we can fix~$x$ and define the value first for $y=0$
and then for $y+1$ in terms of~$y$. Since $x$ is fixed, it will appear
on the left and on the right side of the defining equations.
\begin{align*}
\Add(x,0) & =  x\\
\Add(x,y+1) & =  \Add(x,y)+1
\end{align*}
These equations specify the value of $\Add$ for all $x$
\emph{and}~$y$. To find $\Add(2,3)$, for instance, we apply the
defining equations for $x = 2$, using the first to find
$\Add(2,0) = 2$, then using the second to successively find
$\Add(2,1) = 2 + 1 = 3$, $\Add(2, 2) = 3 + 1 = 4$, $\Add(2,
3) = 4 + 1 = 5$.
```

### BN-IN-T074

- Source term or concept: tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus
- Chosen Bengali: ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন
- Rationale: The checked sources support formula, truth value and proof-tree prose but not this system vocabulary. The section explicitly defines a signed formula as a truth-value sign paired with a sentence and defines closure by a matching true/false pair on every branch. ট্যাবলো is retained as the international system name, with সত্য-বৃক্ষ recorded as its explanatory synonym.
- Plausible alternatives: সত্যচিহ্নিত সূত্র was considered for signed formula; চিহ্নিত সূত্র is shorter because the immediately adjacent definition supplies the True/False sign. সত্য-বৃক্ষ is retained as an explanatory synonym, while ট্যাবলো remains the primary token-compatible system name.
- Status: provisional-explicitly-defined; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ট্যাবলো/সত্য-বৃক্ষ; চিহ্নিত সূত্র; সত্যমান-চিহ্ন; বদ্ধ/খোলা শাখা; ট্যাবলো কলন’ express the OpenLogic sense(s) ‘tableau/truth tree; signed formula; truth-value sign; closed/open branch; tableau calculus’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 332 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:14-15` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:14`; final reader page pending
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:10`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:49`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:57`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection[Union and Intersection of C.E. Sets]{Computably Enumerable
  Sets are Closed under Union and Intersection}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 13 occurrence(s). Representative locations:
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:38-41` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:38`; final reader page pending
  - `OLP-0077` `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:45-67` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:69`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:18-48` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:26`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:76-108` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:69`; final reader page pending
  - `OLP-0075` `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:110-152` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/proving-things.tex:104`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We'll now show that the operations of determining the length of a
sequence, determining its $i$th element, appending an element to a
sequence, and concatenating two sequences, are all primitive
recursive.
```

### BN-IN-T077

- Source term or concept: logical rule; structural rule; upper/lower sequent; left/right rule
- Chosen Bengali: যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি
- Rationale: The sources support logical connective and proof prose, while the complete sequent-rule compounds remain provisional. A logical rule is named for the principal connective or quantifier introduced in its lower conclusion. A structural rule rearranges, duplicates, removes or adds surrounding sequence material. Upper and lower refer to the printed premise/conclusion positions, and left/right refer to the side containing the principal formula.
- Plausible alternatives: রূপগত বিধি was considered for structural rule; গঠনগত বিধি better marks changes to sequent arrangement without implying ordinary linguistic morphology. বাম/ডান বিধি were possible forms; বাঁ/ডান continues the edition’s established side vocabulary.
- Status: provisional-rule-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যৌক্তিক বিধি; গঠনগত বিধি; উপরের/নিচের সিকোয়েন্ট; বাঁ/ডান-বিধি’ express the OpenLogic sense(s) ‘logical rule; structural rule; upper/lower sequent; left/right rule’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 153 occurrence(s). Representative locations:
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:47`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:107-127` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:126`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:115`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:181-201` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:200`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:84-99` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:95`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For a concrete example, the ``greatest common divisor'' function
$\fn{gcd}(u,v)$ can be defined by
\[
\fn{gcd}(u,v) \simeq
\begin{cases}
v & \text{if $u = 0$} \\
\fn{gcd}(\fn{mod}(v, u), u) & \text{otherwise}
\end{cases}
\]
where $\fn{mod}(v, u)$ denotes the remainder of dividing $v$
by~$u$. An appeal to the fixed-point lemma shows that $\fn{gcd}$ is
partial computable. (In fact, this can be put in the format above,
letting $y$ code the pair $\tuple{u, v}$.) A subsequent induction
on~$u$ then shows that, in fact, $\fn{gcd}$ is total.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 56 occurrence(s). Representative locations:
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:59-64` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:55`; final reader page pending
  - `OLP-0097` `upstream/content/first-order-logic/natural-deduction/soundness-identity.tex:23-45` → `bn-Beng-IN/content/first-order-logic/natural-deduction/soundness-identity.tex:47`; final reader page pending
  - `OLP-0068` `upstream/content/first-order-logic/proof-systems/axiomatic-deduction.tex:46-64` → `bn-Beng-IN/content/first-order-logic/proof-systems/axiomatic-deduction.tex:60`; final reader page pending
  - `OLP-0074` `upstream/content/first-order-logic/sequent-calculus/derivations.tex:23-35` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/derivations.tex:32`; final reader page pending
  - `OLP-0074` `upstream/content/first-order-logic/sequent-calculus/derivations.tex:37-119` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/derivations.tex:57`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Without loss of generality, we can assume that the function $f$ which
is nowhere defined is not in $C$ (otherwise, switch $C$ and its
complement in the argument below). Let $g$ be any function in~$C$. The
idea is that if we could decide~$A$, we could tell the difference
between indices computing~$f$, and indices computing~$g$; and then we
could use that capability to solve the halting problem.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 316 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:10`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:18`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:38`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:46`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{apf}
\olsection{Applying the Fixed-Point Theorem}
```

### BN-IN-T082

- Source term or concept: propositional facts about provability; modus ponens; shared sequent context
- Chosen Bengali: বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ
- Rationale: Connective and proof vocabulary is supported by the checked pages, while the complete compound remains provisional. The displayed derivations fix the intended facts for conjunction, disjunction and the material conditional. অভিন্ন সিকোয়েন্ট-প্রসঙ্গ names the identical antecedent and succedent material required in both premises of the additive right-conjunction rule; it does not mean formula identity.
- Plausible alternatives: সাধারণ প্রসঙ্গ was considered for shared context; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ emphasizes literal equality of the two premise contexts. The modus-ponens loan is retained under T070 because no checked page directly attested a stable Bengali replacement.
- Status: provisional-rule-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বচনসংযোজক-সংক্রান্ত প্রমাণযোগ্যতার তথ্য; মোডাস পোনেন্স; অভিন্ন সিকোয়েন্ট-প্রসঙ্গ’ express the OpenLogic sense(s) ‘propositional facts about provability; modus ponens; shared sequent context’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 22 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 134 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:12`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:98-114` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:95`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:116-147` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:124`; final reader page pending
  - `OLP-0089` `upstream/content/first-order-logic/natural-deduction/proving-things.tex:149-176` → `bn-Beng-IN/content/first-order-logic/natural-deduction/proving-things.tex:148`; final reader page pending
  - `OLP-0085` `upstream/content/first-order-logic/natural-deduction/rules-and-proofs.tex:26-29` → `bn-Beng-IN/content/first-order-logic/natural-deduction/rules-and-proofs.tex:26`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The branch of logic known as \emph{computability theory} deals with
issues having to do with the computability, or relative computability,
of functions and sets. It is evidence of Kleene's influence
that the subject used to be known as \emph{recursion theory}, and
today, both names are commonly used.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 176 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:12`; final reader page pending
  - `OLP-0119` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:103-118` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:111`; final reader page pending
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:122-134` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:137`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:15-32` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:26`; final reader page pending
  - `OLP-0124` `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex:129-140` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/soundness.tex:134`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The branch of logic known as \emph{computability theory} deals with
issues having to do with the computability, or relative computability,
of functions and sets. It is evidence of Kleene's influence
that the subject used to be known as \emph{recursion theory}, and
today, both names are commonly used.
```

### BN-IN-T090

- Source term or concept: syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations
- Chosen Bengali: নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো
- Rationale: The checked India Bengali pages support proposition, connective, quantifier and proof prose but do not directly attest these full metatheoretic compounds. নিঃসরণ উপপাদ্য is reserved here for the syntactic biconditional between derivability from Gamma union {A} and derivability of A conditional B from Gamma; T067 keeps the distinct semantic name অর্থগত নিঃসরণ উপপাদ্য. অনুমিতি নিঃসরণ describes moving the extra premise into a conditional, স্বতঃসিদ্ধের রূপ means an instance obtained from an axiom schema, and নিষ্পাদনগুলি পরপর বসানো preserves the ordered-sequence operation without colliding with logical conjunction.
- Plausible alternatives: অবরোহ উপপাদ্য and ডিডাকশন উপপাদ্য were considered; নিঃসরণ উপপাদ্য matches the movement of one premise into a conditional and remains explicitly provisional. অর্থগত নিঃসরণ উপপাদ্য is reserved under T067 for entailment; the unqualified form here is syntactic because both sides use Proves. নিষ্পাদন-সংযুক্তি was considered for concatenation; পরপর বসানো states the ordered-sequence operation directly and avoids collision with logical সংযোজন.
- Status: provisional-axiomatic-metatheory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিঃসরণ উপপাদ্য; অনুমিতি নিঃসরণ; স্বতঃসিদ্ধের রূপ; নিষ্পাদনগুলি পরপর বসানো’ express the OpenLogic sense(s) ‘syntactic deduction theorem; discharge an assumption; axiom instance; concatenate derivations’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 21 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 35 occurrence(s). Representative locations:
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:29-30` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:28`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:40`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:32-34` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Computable sets and relations are also called \emph{decidable}.
\end{defn}
```

### BN-IN-T092

- Source term or concept: Henkin expansion; saturated set; witness; counterexample
- Chosen Bengali: হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত
- Rationale: The checked proposition, quantifier and proof pages support the prose, but the Henkin-specific compounds are not directly attested. হেনকিন সম্প্রসারণ names the language extension by fresh constants. A set is সম্পৃক্ত when each true existential has a named witness or, in the alternative configuration, each false universal has a named counterexample. সাক্ষী and প্রতিদৃষ্টান্ত are fixed by those displayed membership conditions rather than by ordinary evidential senses.
- Plausible alternatives: পরিপূর্ণ সেট was considered for saturated set, but পূর্ণ is already reserved for completeness; সম্পৃক্ত distinguishes the witness property. প্রতিউদাহরণ was considered for counterexample; প্রতিদৃষ্টান্ত pairs transparently with the selected witness language in the quantified construction.
- Status: provisional-henkin-construction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হেনকিন সম্প্রসারণ; সম্পৃক্ত সেট; সাক্ষী; প্রতিদৃষ্টান্ত’ express the OpenLogic sense(s) ‘Henkin expansion; saturated set; witness; counterexample’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 13 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 123 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:156`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:158`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:159`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:160`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:181-201` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:182`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
What's going on? Suppose you are given the task of writing a computer
program that prints itself out. Suppose further, however, that you are
working with a programming language with a rich and bizarre library of
string functions. In particular, suppose your programming language has
a function $\fn{diag}$ which works as follows: given an input
string~$s$, $\fn{diag}$ locates each instance of the symbol `x'
occurring in~$s$, and replaces it by a quoted version of the original
string. For example, given the string
\begin{quote}
\begin{verbatim}
hello x world
\end{verbatim}
\end{quote}
as input, the function returns
\begin{quote}
\begin{verbatim}
hello 'hello x world' world
\end{verbatim}
\end{quote}
as output. In that case, it is easy to write the desired program; you
can check that
\begin{quote}
\begin{verbatim}
print(diag('print(diag(x))'))
\end{verbatim}
\end{quote}
does the trick. For more common programming languages like C++ and
Java, the same idea (with a more involved implementation) still works.
```

### BN-IN-T097

- Source term or concept: term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope
- Chosen Bengali: পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর
- Rationale: The quantification witness directly discusses individual variables, predicates, universal and existential quantification and scope; the school algebra witness supports the variable/constant register. The exact metalogical compounds remain governed by the chapter definitions. A sentence is a formula with no free variable occurrence. সংঘটন means a token occurrence at a position, so different occurrences of the same variable may be bound by different quantifiers. সংশ্লিষ্ট names a quantifier associated with that occurrence, while অনুরূপ identifies the corresponding token position through a recursive clause; this avoids সঙ্গত, which the edition reserves for consistency. পদ is the syntactic term category, not an algebraic monomial here.
- Plausible alternatives: আণবিক সূত্র was considered for atomic formula; পরমাণু সূত্র continues the established logical atom vocabulary and remains definition-governed. বদ্ধ সূত্র was considered for sentence, but বাক্য follows the source category while the no-free-occurrence definition prevents ordinary-language ambiguity. উপস্থিতি and আবির্ভাব were considered for occurrence; সংঘটন marks a token at a particular syntactic position. সঙ্গত was considered for both matching and corresponding, but the edition reserves that root for consistency; সংশ্লিষ্ট পরিমাণসূচক and অনুরূপ সংঘটন keep the two syntactic relations distinct. ব্যাপ্তি was considered for scope; পরিসর stays distinct from the domain term সংজ্ঞাক্ষেত্র.
- Status: mixed-attested-roots-and-definition-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পদ; পরমাণু সূত্র; বাক্য; মুক্ত/বদ্ধ চলরাশির সংঘটন; সংশ্লিষ্ট পরিমাণসূচক; অনুরূপ সংঘটন; পরিমাণসূচকের পরিসর’ express the OpenLogic sense(s) ‘term; atomic formula; sentence; free/bound variable occurrence; matching quantifier; corresponding occurrence; quantifier scope’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 702 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:212`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:214`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:222`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:233`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:54`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{tagblock}{lambda}
\begin{digress}
The same idea can be used to get a ``fixed point'' combinator. Suppose
you have a lambda term $g$, and you want another term $k$ with the
property that $k$ is $\beta$-equivalent to $gk$. Define terms
\[
\fn{diag}(x) = xx
\]
and
\[
l(x) = g(\fn{diag}(x))
\]
using our notational conventions; in other words, $l$ is the term
$\lambd[x][g(xx)]$. Let $k$ be the term $ll$. Then we have
\begin{align*}
k & = (\lambd[x][g(xx)])(\lambd[x][g(xx)]) \\
& \red  g((\lambd[x][g(xx)])(\lambd[x][g(xx)])) \\
& = gk.
\end{align*}
If one takes
\[
Y = \lambd[g][((\lambd[x][g(xx)])(\lambd[x][g(xx)]))]
\]
then $Yg$ and $g(Yg)$ reduce to a common term; so $Yg \equiv_\beta
g(Yg)$. This is known as ``Curry's combinator.'' If instead one takes
\[
Y = (\lambd[xg][g(xxg)])(\lambd[xg][g(xxg)])
\]
then in fact $Yg$ reduces to $g(Yg)$, which is a stronger statement.
This latter version of $Y$ is known as ``Turing's combinator.''
\end{digress}
\end{tagblock}
```

### BN-IN-T098

- Source term or concept: structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment
- Chosen Bengali: গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ
- Rationale: The checked relation and mapping pages directly support relation, domain and function language, and the logic pages support truth and quantification. They do not directly attest the full Tarskian compounds. A structure supplies a nonempty domain plus denotations or interpretations of nonlogical symbols. Satisfaction for an open formula is relative to a variable assignment; the modified assignment differs at the named variable only. This keeps first-order গঠন distinct from ordinary prose uses through the adjacent formal notation.
- Plausible alternatives: কাঠামো was considered for structure; গঠন is shorter and the formal Struct notation fixes the technical sense. পরিসর was considered for domain, but সংজ্ঞাক্ষেত্র avoids collision with quantifier scope and function codomain. সন্তুষ্টি was considered for satisfaction; পরিতৃপ্তি continues T066 and is fixed by the recursive truth clauses. মূল্যায়ন was considered for assignment; আরোপ distinguishes variable assignment from propositional valuation and from the structure’s interpretation function.
- Status: mixed-attested-roots-and-provisional-semantics; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠন; সংজ্ঞাক্ষেত্র; ব্যাখ্যা/নির্দেশিত মান; আরোপ-সাপেক্ষ পরিতৃপ্তি; পরিবর্তিত আরোপ’ express the OpenLogic sense(s) ‘structure; domain; interpretation/denotation; satisfaction relative to an assignment; modified assignment’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 403 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:21`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:27-34` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:32`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:27-34` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:33`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:67-70` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:66`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:67-70` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:67`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
```

### BN-IN-T099

- Source term or concept: substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma
- Chosen Bengali: প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য
- Rationale: The checked pages support quantifier scope, variable, equality-operation, mapping and proof prose but do not directly attest the full substitution vocabulary. The introduction warns that replacing every written x is not always legitimate because binding matters. Universal instantiation removes a universal quantifier only with an admissible term instance. The later substitution lemma equates satisfaction of the substituted formula with satisfaction under the assignment modified to the term's value; its exact hypotheses govern the terminology.
- Plausible alternatives: বদলি was considered for substitution; প্রতিস্থাপন is the established operation name and works for terms and formulas. বিশেষীকরণ was considered for universal instantiation; সার্বিক নিদর্শনায়ন names formation of a particular admissible instance without suggesting an unrestricted replacement. প্রতিস্থাপন উপপাদ্য was considered; প্রতিস্থাপন-সহায়ক উপপাদ্য retains the source’s lemma status and its role in the later soundness argument.
- Status: provisional-definition-and-lemma-governed; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রতিস্থাপন; চলরাশি-বদ্ধতা-সংবেদনশীল প্রতিস্থাপন; পদের মান; সার্বিক নিদর্শনায়ন; প্রতিস্থাপন-সহায়ক উপপাদ্য’ express the OpenLogic sense(s) ‘substitution; capture-sensitive replacement; term value; universal instantiation; substitution lemma’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 34 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:160`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:181-201` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:193`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:30-65` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:56`; final reader page pending
  - `OLP-0132` `upstream/content/first-order-logic/completeness/construction-of-model.tex:99-114` → `bn-Beng-IN/content/first-order-logic/completeness/construction-of-model.tex:107`; final reader page pending
  - `OLP-0133` `upstream/content/first-order-logic/completeness/identity.tex:12-24` → `bn-Beng-IN/content/first-order-logic/completeness/identity.tex:19`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
What's going on? Suppose you are given the task of writing a computer
program that prints itself out. Suppose further, however, that you are
working with a programming language with a rich and bizarre library of
string functions. In particular, suppose your programming language has
a function $\fn{diag}$ which works as follows: given an input
string~$s$, $\fn{diag}$ locates each instance of the symbol `x'
occurring in~$s$, and replaces it by a quoted version of the original
string. For example, given the string
\begin{quote}
\begin{verbatim}
hello x world
\end{verbatim}
\end{quote}
as input, the function returns
\begin{quote}
\begin{verbatim}
hello 'hello x world' world
\end{verbatim}
\end{quote}
as output. In that case, it is easy to write the desired program; you
can check that
\begin{quote}
\begin{verbatim}
print(diag('print(diag(x))'))
\end{verbatim}
\end{quote}
does the trick. For more common programming languages like C++ and
Java, the same idea (with a more involved implementation) still works.
```

### BN-IN-T100

- Source term or concept: model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain
- Chosen Bengali: মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র
- Rationale: The checked university pages directly support relations, mappings, proof, finite/infinite sets and quantification, while the full model-theory compounds remain provisional. A model satisfies every sentence in the given set. Characterizing a class means that exactly the intended structures satisfy the description. Expressibility is restricted to formulas or sentence sets in the specified first-order language. T040 and T044 govern the finite and nonenumerable size vocabulary; compactness and Löwenheim–Skolem govern the stated limitations.
- Plausible alternatives: নমুনা তত্ত্ব was considered for model theory; মডেল তত্ত্ব retains the established technical loan and avoids suggesting an illustrative example. স্বতঃসিদ্ধ পদ্ধতি was considered; স্বতঃসিদ্ধমূলক পদ্ধতি states that a class is described through a set of sentences used as axioms. সুনির্দিষ্ট করা was considered for characterize; চরিত্রায়িত করা retains the exact-class sense supplied by the biconditional explanation. অভিব্যক্তিযোগ্যতা was considered for expressibility; প্রকাশযোগ্যতা states whether the specified first-order language can express the property.
- Status: mixed-attested-roots-and-provisional-model-theory; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মডেল তত্ত্ব; বাক্যসমষ্টির মডেল; স্বতঃসিদ্ধমূলক পদ্ধতি; কোনো শ্রেণিকে চরিত্রায়িত করা; প্রকাশযোগ্যতা; সসীম/অতালিকায়নযোগ্য সংজ্ঞাক্ষেত্র’ express the OpenLogic sense(s) ‘model theory; model of a sentence set; axiomatic method; characterize a class; expressibility; finite/nonenumerable domain’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 255 occurrence(s). Representative locations:
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:172`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:177`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:187-193` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:186`; final reader page pending
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:101-119` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:107`; final reader page pending
  - `OLP-0211` `upstream/content/computability/recursive-functions/primitive-recursion.tex:12-24` → `bn-Beng-IN/content/computability/recursive-functions/primitive-recursion.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
The set of primitive recursive functions is closed under the
following two operations:
\begin{enumerate}
\item Finite sums: if $f(\vec x, z)$ is primitive recursive, then so
is the function
\[
g(\vec x, y) \defis \sum_{z = 0}^y f(\vec x, z).
\]
\item Finite products: if $f(\vec x, z)$ is primitive recursive, then
so is the function
\[
h(\vec x, y) \defis \prod_{z = 0}^y f(\vec x, z).
\]
\end{enumerate}
\end{prop}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0162` `upstream/content/first-order-logic/syntax-and-semantics/covered-structures.tex:68-70` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/covered-structures.tex:70`; final reader page pending
  - `OLP-0161` `upstream/content/first-order-logic/syntax-and-semantics/structures.tex:82-92` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/structures.tex:84`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:45-57` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:40`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:73-79` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:64`; final reader page pending
  - `OLP-0193` `upstream/content/model-theory/models-of-arithmetic/standard-models.tex:9-10` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/standard-models.tex:10`; final reader page pending
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 19 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 19 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 56 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:12`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:84-86` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:78`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:29-39` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:33`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:169-181` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:171`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection[Union and Intersection of C.E. Sets]{Computably Enumerable
  Sets are Closed under Union and Intersection}
```

### BN-IN-T109

- Source term or concept: express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model
- Chosen Bengali: কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল
- Rationale: The university witnesses directly support relations, domains, mappings and quantification; the full definability compounds remain provisional. A formula expresses R only relative to the stated structure and assignments of its free variables. A predicate is superfluous when a formula using the remaining vocabulary expresses its interpretation. The arithmetic examples preserve argument order for successor and predecessor. The chapter uses প্রমিত consistently with T094; the মানক alternative remains recorded in T104 for expert review. T032 governs inverse, relative product and transitive closure, and T043 governs cofinite.
- Plausible alternatives: সংজ্ঞায়ক সম্পর্ক was considered for definable relation; সংজ্ঞেয় সম্পর্ক states that some formula can define it in the fixed structure. পরবর্তী/পূর্ববর্তী সম্পর্ক were considered; উত্তরসূরি/পূর্বসূরি aligns with the arithmetic direction displayed in the formulas. মানক মডেল remains a recorded alternative under T104; প্রমিত মডেল continues T094 in this chapter.
- Status: mixed-attested-roots-and-provisional-definability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কোনো গঠনে সম্পর্ক প্রকাশ করা; সংজ্ঞেয় সম্পর্ক; অপ্রয়োজনীয় বিধেয়; উত্তরসূরি/পূর্বসূরি সম্পর্ক; পাটীগণিতের প্রমিত মডেল’ express the OpenLogic sense(s) ‘express a relation in a structure; definable relation; superfluous predicate; successor/predecessor relation; standard arithmetic model’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 55 occurrence(s). Representative locations:
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:29-46` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:47`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:20-27` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:23`; final reader page pending
  - `OLP-0214` `upstream/content/computability/recursive-functions/notation-pr-functions.tex:12-21` → `bn-Beng-IN/content/computability/recursive-functions/notation-pr-functions.tex:14`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:12-47` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:34`; final reader page pending
  - `OLP-0224` `upstream/content/computability/recursive-functions/partial-functions.tex:42-62` → `bn-Beng-IN/content/computability/recursive-functions/partial-functions.tex:39`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
This may seem like an overly restrictive characterization of what
happens when we compute a new function using some existing ones. For
one thing, sometimes we do not use all the arguments of a function, as
when we defined $g(x, y, z) = \Succ(z)$ for use in the primitive
recursive definition of~$\Add$. Suppose we are allowed use of the
following functions:
\[
\Proj{n}{i}(x_0, \dots, x_{n-1}) = x_i
\]
The functions~$\Proj{k}{i}$ are called \emph{projection} functions:
$\Proj{n}{i}$ is an $n$-place function. Then $g$ can be defined by
\[
g(x, y, z) = \Succ(\Proj{3}{2}(x, y, z)).
\]
Here the role of $f$ is played by the $1$-place function $\Succ$, so
$k=1$. And we have one $3$-place function $\Proj{3}{2}$ which plays
the role of $g_0$. The result is a $3$-place function that returns the
successor of the third argument.
```

### BN-IN-T110

- Source term or concept: ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox
- Chosen Bengali: জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস
- Rationale: The West Bengal and Tripura sources directly support set membership, subsets, equality, emptiness, power sets, ordered pairs, relations and mappings, but do not directly attest the complete foundational names. OpenLogic's formulas govern each phrase. Extensionality identifies sets with the same members; the power-set axiom supplies the set of all subsets. A function is encoded as a set of ordered pairs satisfying inclusion, totality and uniqueness. Unrestricted comprehension is inconsistent by Russell's paradox, while separation restricts the selected members to a pre-existing set. T020 and T039 govern the overlapping comprehension and function vocabulary.
- Plausible alternatives: ব্যাপ্তিগততার স্বতঃসিদ্ধ was considered for extensionality; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ exposes the set-membership criterion and avoids collision with T105. সর্বগ্রাহী নীতি and comprehension loan forms were considered; ধর্মনির্দেশে সেট-গঠন states the exact unrestricted existence claim. বিভাজন নীতি was considered for separation; পৃথকীকরণ makes restriction to a prior set distinct from partitions.
- Status: mixed-attested-set-roots-and-provisional-foundational-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘জার্মেলো--ফ্রেঙ্কেল সেটতত্ত্বসহ নির্বাচন স্বতঃসিদ্ধ; সদস্যভিত্তিক সমতার স্বতঃসিদ্ধ; শূন্য সেটের স্বতঃসিদ্ধ; ঘাত সেটের স্বতঃসিদ্ধ; সম্পর্করূপে অপেক্ষক; ধর্মনির্দেশে সেট-গঠন নীতি; পৃথকীকরণ নীতি; রাসেলের কূটাভাস’ express the OpenLogic sense(s) ‘ZFC; axiom of extensionality; empty-set axiom; power-set axiom; function represented as a relation; comprehension principle; separation principle; Russell's paradox’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 18 occurrence(s). Representative locations:
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:10`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:12`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:15`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:22-32` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:23`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:75`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{rus}
\olsection{Comparison with Russell's Paradox}
```

### BN-IN-T111

- Source term or concept: size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure
- Chosen Bengali: গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন
- Rationale: The NSOU pages directly attest finite and infinite sets and finite cardinality; the logic and relation pages support quantified model descriptions. The specialized structure-size compounds remain definition-governed. The displayed sentences express lower, upper and exact finite bounds. Infinitude requires the infinite family of all lower-bound sentences and cannot be expressed by one purely logical sentence. Compactness and Löwenheim--Skolem govern the stated nonexpressibility of finiteness and nonenumerability. T040 and T100 govern size and nonenumerability terminology.
- Plausible alternatives: গঠনের মাত্রা was considered for structure size; আকার avoids suggesting vector-space dimension while T040 reserves finite set মাত্রা as an attested cardinality phrase. সর্বাধিক n was considered for at most n; বড়জোর n is the transparent Bengali bound used in the target. অগণনীয় was considered for nonenumerable; অতালিকায়নযোগ্য preserves the edition’s distinction from countability and follows T100.
- Status: mixed-attested-finiteness-and-provisional-model-size-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠনের আকার; অন্তত/বড়জোর/ঠিক n-টি উপাদান; সসীম/অসীম গঠন; বিশুদ্ধ যৌক্তিক বাক্য; অতালিকায়নযোগ্য গঠন’ express the OpenLogic sense(s) ‘size of a structure; at least/at most/exactly n elements; finite/infinite structure; purely logical sentence; nonenumerable structure’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 319 occurrence(s). Representative locations:
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:24-33` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:34`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:12-17` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:13`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:58-76` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:63`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:172`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:177`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
The proof is a simple diagonalization: if $\fn{Un}'(k,x)$ were total
and computable, then
\[
d(x) = \fn{Un}'(x, x) + 1
\]
would also be total and computable. However, by definition, $d(k)$ is
not equal to $\fn{Un}'(k,k)$. Hence, for every $k$, the values of
$d(x)$ and~$\fn{Un}'(k, x)$ differ for at least one~$x$, namely $x = k$.
\end{proof}
```

### BN-IN-T112

- Source term or concept: logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning
- Chosen Bengali: প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার
- Rationale: The checked school and university logic pages support statement, connective, quantification and proof vocabulary, while the complete philosophical compounds remain provisional. The overview treats a logic as a formal language with an optional deductive system and intended semantics, and preserves the rival necessary, a-priori, formal and conventional conceptions of logical truth. যুক্তিবাদ names the Frege--Russell--Whitehead program; higher-order reasoning remains distinct from Quine's set-theoretic reading.
- Plausible alternatives: প্রথম-ক্রমের পরবর্তী যুক্তিবিদ্যা was considered; পরিসরের বাইরে matches the chapter’s survey of extensions and restrictions without imposing a historical order. নিষ্পাদন ব্যবস্থা was considered for deductive system; অবরোহী ব্যবস্থা is broader here because the overview is not tied to one project derivation formalism. লজিসিজম was considered; যুক্তিবাদ keeps the philosophical program in Bengali while the Frege--Russell--Whitehead context fixes its sense.
- Status: mixed-attested-roots-and-provisional-philosophical-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রথম-ক্রমের পরিসরের বাইরের যুক্তিবিদ্যা; সম্প্রসারণ ও রূপভেদ; আনুষ্ঠানিক ভাষা; অবরোহী ব্যবস্থা; অভিপ্রেত অর্থতত্ত্ব; যুক্তিবাদ; উচ্চতর-ক্রমের যুক্তিবিচার’ express the OpenLogic sense(s) ‘logic beyond first order; extension and variation; formal language; deductive system; intended semantics; logicism; higher-order reasoning’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 438 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:17`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:24`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:31`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:42-44` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:38`; final reader page pending
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T115

- Source term or concept: higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types
- Chosen Bengali: উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব
- Rationale: The checked pages support number, variable, function and proof roots but do not directly attest higher-type theory. টাইপ is kept distinct from the many-sorted জাতি while the formation clauses govern function and product types. A functional maps functions to numbers; lambda abstraction forms a function term; the two projections recover pair components. Church's simple theory of types is fixed by the truth-value type and replacement of complex formulas by terms of that type.
- Plausible alternatives: প্রকার was considered for type but is already ordinary Bengali and risks collapsing the sort/type distinction; টাইপ retains the formal hierarchy explicitly. অপেক্ষকাত্মক was considered for functional; ফাংশনাল is the recognizable higher-type noun and is immediately defined as a function taking functions to numbers. লাম্বডা নিষ্কর্ষ was considered; ল্যাম্বডা বিমূর্তন remains provisional and its term-forming clause supplies the exact sense.
- Status: mixed-attested-roots-and-provisional-type-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উচ্চতর-ক্রমের যুক্তিবিদ্যা; টাইপ; অপেক্ষক-টাইপ; গুণন-টাইপ; ফাংশনাল; ল্যাম্বডা বিমূর্তন; অভিক্ষেপ; সরল টাইপতত্ত্ব’ express the OpenLogic sense(s) ‘higher-order logic; type; function type; product type; functional; lambda abstraction; projection; simple theory of types’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 74 occurrence(s). Representative locations:
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:66-82` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:76`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:29-46` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:38`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:48-57` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:49`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:48-57` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:57`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:70`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Here's how. Using the universal partial computable functions, we can
define a function
\[
h(x,y) \simeq
\begin{cases}
\text{undefined} & \text{if $\cfind{x}(x) \fundefined$} \\
g(y) & \text{otherwise.}
\end{cases}
\]
To compute $h$, first we try to compute $\cfind{x}(x)$; if that
computation halts, we go on to compute~$g(y)$; and if {\em that}
computation halts, we return the output. More formally, we can write
\[
h(x,y) \simeq \Proj{2}{0}(g(y),\fn{Un}(x,x)).
\]
where $\Proj{2}{0}(z_0, z_1) = z_0$ is the $2$-place projection
function returning the $0$-th argument, which is computable.
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 24 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 16 occurrence(s). Representative locations:
  - `OLP-0228` `upstream/content/computability/computability-theory/computability-theory.tex:10-13` → `bn-Beng-IN/content/computability/computability-theory/computability-theory.tex:11`; final reader page pending
  - `OLP-0209` `upstream/content/computability/recursive-functions/recursive-functions.tex:10-15` → `bn-Beng-IN/content/computability/recursive-functions/recursive-functions.tex:12`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:14`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:166-170` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:157`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:69`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{editorial}
  Material in this chapter should be reviewed and expanded. In
  particular, there are no exercises yet.
\end{editorial}
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 50 occurrence(s). Representative locations:
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
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0279` `upstream/content/incompleteness/introduction/undecidability.tex:19-22` → `bn-Beng-IN/content/incompleteness/introduction/undecidability.tex:19`; final reader page pending
  - `OLP-0279` `upstream/content/incompleteness/introduction/undecidability.tex:58-65` → `bn-Beng-IN/content/incompleteness/introduction/undecidability.tex:61`; final reader page pending
  - `OLP-0279` `upstream/content/incompleteness/introduction/undecidability.tex:78-81` → `bn-Beng-IN/content/incompleteness/introduction/undecidability.tex:78`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:68-83` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:78`; final reader page pending
  - `OLP-0196` `upstream/content/model-theory/models-of-arithmetic/models-of-pa.tex:238-259` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/models-of-pa.tex:263`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}
If $\Gamma$ is a consistent theory that !!{represents} every
!!{decidable} relation, then $\Gamma$ is not !!{decidable}.
\end{thm}
```

### BN-IN-T124

- Source term or concept: partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union
- Chosen Bengali: আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ
- Rationale: The witnesses support finite sets, relations, mappings, inclusion and proof prose, while the back-and-forth terminology remains definition-governed. An আংশিক সমরূপতা is a finite partial function preserving the isomorphism clauses wherever defined. অগ্র extends the domain and পশ্চাৎ extends the range. Alternating the two conditions along enumerations yields an inclusion-increasing chain whose union is the required total isomorphism.
- Plausible alternatives: আংশিক সমাকৃতি was considered; আংশিক সমরূপতা extends T122 and the finite partial-function definition fixes its scope. সামনে-পিছনে and back-and-forth loan forms were considered; আগ-পিছু is concise, while অগ্র and পশ্চাৎ name the two formal extension clauses. ঊর্ধ্বমুখী সংযোগ was considered for increasing union; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ states the ordering relation on the partial maps.
- Status: mixed-attested-roots-and-provisional-back-and-forth-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু ধর্ম; অগ্র; পশ্চাৎ; অন্তর্ভুক্তি-ক্রমবর্ধমান সংযোগ’ express the OpenLogic sense(s) ‘partial isomorphism; partially isomorphic; back-and-forth property; Forth; Back; increasing union’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 24 occurrence(s). Representative locations:
  - `OLP-0276` `upstream/content/incompleteness/introduction/historical-background.tex:81-90` → `bn-Beng-IN/content/incompleteness/introduction/historical-background.tex:70`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:35`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:37`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:41`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:42-61` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:58`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Calculus was invented by Newton and Leibniz in the seventeenth
century. (A fierce priority dispute raged for centuries, but most
scholars today hold that the two developments were for the most part
independent.)  Calculus involves reasoning about, for example,
infinite sums of infinitely small quantities; these features fueled
criticism by Bishop Berkeley, who argued that belief in God was no
less rational than the mathematics of his time. The methods of
calculus were widely used in the eighteenth century, for example by
Leonhard Euler, who used calculations involving infinite sums with
dramatic results.
```

### BN-IN-T125

- Source term or concept: quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence
- Chosen Bengali: পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা
- Rationale: The sources support quantification, finite objects, sequences, relations and proof language, but do not directly attest the bounded-rank compounds. পরিমাণসূচক-ক্রমাঙ্ক counts maximum quantifier nesting. n-সমতুল্য গঠন agree on sentences of rank at most n. সংযুক্তি appends one element to a finite sequence and stays distinct from logical conjunction. The recursive I_n relation connects sequence extension with formulas of bounded rank, using finiteness only up to logical equivalence.
- Plausible alternatives: পরিমাণসূচক গভীরতা was considered for quantifier rank; পরিমাণসূচক-ক্রমাঙ্ক follows the source rank notation and remains fixed by maximum nesting depth. ক্রমসংযোজন was considered for sequence concatenation; সংযুক্তি continues T076 and is distinguished from logical conjunction by context. n-মৌলিক সমতুল্য was considered; n-সমতুল্য গঠন stays close to the notation and the bounded-rank sentence definition.
- Status: mixed-attested-roots-and-provisional-bounded-rank-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম অনুক্রম; সংযুক্তি; I_n সম্পর্ক; যৌক্তিক সমতুল্যতা-অবধি সমতুল্যতা’ express the OpenLogic sense(s) ‘quantifier rank; n-equivalent structures; finite sequence; concatenation; I_n relation; equivalence up to logical equivalence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 34 occurrence(s). Representative locations:
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:12-25` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:14`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:38-41` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:38`; final reader page pending
  - `OLP-0113` `upstream/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:24-35` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/rules-and-proofs.tex:26`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:15-16` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:16`; final reader page pending
  - `OLP-0070` `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:46-50` → `bn-Beng-IN/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:51`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The set of primitive recursive functions is remarkably robust. But we
will be able to do even more once we have developed a adequate means
of handling \emph{sequences}. We will identify finite sequences of
natural numbers with natural numbers in the following way: the
sequence $\langle a_0, a_1, a_2, \dots, a_k \rangle$ corresponds to
the number
\[
p_0^{a_0+1} \cdot p_1^{a_1+1} \cdot p_2^{a_2+1} \cdot \dots \cdot
p_k^{a_k+1}.
\]
We add one to the exponents to guarantee that, for example, the
sequences $\langle 2, 7, 3\rangle$ and $\langle 2, 7, 3, 0, 0 \rangle$
have distinct numeric codes. We can take both $0$ and~$1$ to code the
empty sequence; for concreteness, let $\emptyseq$ denote~$0$.
```

### BN-IN-T126

- Source term or concept: dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order
- Chosen Bengali: অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম
- Rationale: The checked pages support order relations, rational numbers, mappings, quantification, countability and proof prose. The complete dense-order compound remains governed by the six displayed axioms: strict linear order, points above and below every element, and a point strictly between any two ordered points. অন্তবিন্দু names an excluded least or greatest boundary point. The back-and-forth theorem makes all enumerable models of this theory isomorphic, including the rational order.
- Plausible alternatives: প্রান্তবিন্দুহীন was considered for without endpoints; অন্তবিন্দুহীন is selected because the axioms exclude both a least and a greatest element of the order. সঘন রৈখিক ক্রম was considered; ঘন রৈখিক ক্রম is more idiomatic and is fixed by the between-any-two-points axiom. ক্যান্টরের উপপাদ্য was considered; কান্টরের আগ-পিছু উপপাদ্য distinguishes this countable-order result from Cantor’s other theorems.
- Status: mixed-attested-order-roots-and-provisional-dense-order-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অন্তবিন্দুহীন ঘন রৈখিক ক্রম; ঘনত্ব; অন্তবিন্দু; কান্টরের আগ-পিছু উপপাদ্য; মূলদ ক্রম’ express the OpenLogic sense(s) ‘dense linear order without endpoints; density; endpoint; Cantor back-and-forth theorem; rational order’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
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

### BN-IN-T127

- Source term or concept: standard model; nonstandard model; standard number; nonstandard number
- Chosen Bengali: মানক মডেল; অমানক মডেল; মানক সংখ্যা; অমানক সংখ্যা
- Rationale: The checked number, logic, relation, mapping, proof and cardinality pages support the component roots, while the arithmetic-model distinction is governed primarily by the OpenLogic definitions and formulas. মানক মডেল names the intended natural-number structure, whereas অমানক মডেল permits additional elements beyond all standard numerals; মানক সংখ্যা and অমানক সংখ্যা preserve that contrast in explanatory prose. The choice remains open to expert review because the specialized model-theoretic compounds are not directly settled by the checked canon pages.
- Plausible alternatives: প্রমিত মডেল was considered for standard model; মানক মডেল continues the established mathematical register. অমানক গঠন was considered for nonstandard model; অমানক মডেল keeps the contrast with মানক মডেল explicit.
- Status: provisional-arithmetic-model-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মানক মডেল; অমানক মডেল; মানক সংখ্যা; অমানক সংখ্যা’ express the OpenLogic sense(s) ‘standard model; nonstandard model; standard number; nonstandard number’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 39 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:129-167` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:149`; final reader page pending
  - `OLP-0162` `upstream/content/first-order-logic/syntax-and-semantics/covered-structures.tex:68-70` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/covered-structures.tex:70`; final reader page pending
  - `OLP-0161` `upstream/content/first-order-logic/syntax-and-semantics/structures.tex:53-65` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/structures.tex:65`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:45-57` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:40`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:59-71` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:58`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The language of second-order logic is quite rich. One can identify
unary relations with subsets of the !!{domain}, and so in particular you
can quantify over these sets; for example, one can express induction
for the natural numbers with a single axiom
\[
\lforall[R][((\Atom{R}{\Obj{0}} \land \lforall[x][(\Atom{R}{x} \lif
    \Atom{R}{x'})]) \lif \lforall[x][\Atom{R}{x}])].
\]
If one takes the language of arithmetic to have symbols $\Obj 0, \Obj \prime, +,
\times$ and $<$, one can add the following axioms to describe their
behavior:
\begin{enumerate}
\item $\lforall[x][\lnot x' = \Obj 0]$
\item $\lforall[x][\lforall[y][(s(x) = s(y) \lif x = y)]]$
\item $\lforall[x][(x + \Obj 0) = x]$
\item $\lforall[x][\lforall[y][(x + y') = (x + y)']]$
\item $\lforall[x][(x \times \Obj 0) = \Obj 0]$
\item $\lforall[x][\lforall[y][(x \times y') = ((x \times y) + x)]]$
\item $\lforall[x][\lforall[y][(x < y \liff \lexists[z][y = (x + z')])]]$
\end{enumerate}
It is not difficult to show that these axioms, together with the axiom
of induction above, provide a categorical description of the
!!{structure}~$\Struct{N}$, the standard model of arithmetic, provided
we are using the full second-order semantics. Given any
!!{structure}~$\Struct{M}$ in which these axioms are true, define a
function~$f$ from $\Nat$ to the !!{domain} of $\Struct{M}$ using
ordinary recursion on $\Nat$, so that $f(0) = \Assign{\Obj 0}{M}$ and
$f(x+1) = \Assign{\prime}{M}(f(x))$. Using ordinary induction
on~$\Nat$ and the fact that axioms (1) and~(2) hold in~$\Struct M$, we
see that $f$ is !!{injective}. To see that $f$ is !!{surjective},
let~$P$ be the set of elements of~$\Domain{M}$ that are in the range
of~$f$. Since $\Struct M$ is full, $P$ is in the second-order
!!{domain}. By the construction of~$f$, we know that $\Assign{\Obj
  0}{M}$ is in~$P$, and that $P$~is closed under
$\Assign{\prime}{M}$. The fact that the induction axiom holds in
$\Struct M$ (in particular, for~$P$) guarantees that $P$~is equal to
the entire first-order !!{domain} of~$\Struct M$. This shows that $f$
is !!a{bijection}. Showing that $f$ is a homomorphism is no more
difficult, using ordinary induction on $\Nat$ repeatedly.
```

### BN-IN-T128

- Source term or concept: arithmetic model; Robinson Q; Peano arithmetic; true arithmetic; consistency witness
- Chosen Bengali: পাটিগাণিতিক মডেল; রবিনসন Q; পেয়ানো পাটিগণিত; সত্য পাটিগণিত; সঙ্গতি-সাক্ষী
- Rationale: The Bengali roots for arithmetic, proof, quantification, relation and mapping are supported by the checked witnesses. The names Robinson Q, Peano arithmetic and true arithmetic are retained in recognizable form, while সঙ্গতি-সাক্ষী describes the proof-code element witnessing a negated consistency assertion. The source axioms and displayed formulas control the exact technical senses; direct canon attestation of these complete theory names remains incomplete.
- Plausible alternatives: পাটিগণিতীয় মডেল was considered; পাটিগাণিতিক মডেল follows the established পাটিগণিত root. সঙ্গতি-সাক্ষ্য was considered for consistency witness; সঙ্গতি-সাক্ষী names the witnessing element and its role more directly.
- Status: provisional-arithmetic-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পাটিগাণিতিক মডেল; রবিনসন Q; পেয়ানো পাটিগণিত; সত্য পাটিগণিত; সঙ্গতি-সাক্ষী’ express the OpenLogic sense(s) ‘arithmetic model; Robinson Q; Peano arithmetic; true arithmetic; consistency witness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:73-79` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:64`; final reader page pending
  - `OLP-0277` `upstream/content/incompleteness/introduction/definitions.tex:132-135` → `bn-Beng-IN/content/incompleteness/introduction/definitions.tex:120`; final reader page pending
  - `OLP-0192` `upstream/content/model-theory/models-of-arithmetic/introduction.tex:55-70` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/introduction.tex:57`; final reader page pending
  - `OLP-0196` `upstream/content/model-theory/models-of-arithmetic/models-of-pa.tex:238-259` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/models-of-pa.tex:249`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
The theory of \emph{true arithmetic} is the set of !!{sentence}s
satisfied in the standard model of arithmetic, i.e.,
\[
\Th{TA} = \Setabs{!A}{\Sat{N}{!A}}.
\]
\end{defn}
```

### BN-IN-T129

- Source term or concept: standard part; nonstandard part; arithmetic block; successor; predecessor
- Chosen Bengali: মানক খণ্ড; অমানক খণ্ড; পাটিগাণিতিক খণ্ড; উত্তরসূরি; পূর্বসূরি
- Rationale: The checked order, number, mapping and proof pages support the ordinary roots, but arithmetic block terminology is fixed by the chapter’s equivalence construction. মানক খণ্ড contains the standard numerals, while অমানক খণ্ড collects elements reachable from one nonstandard element by standard successor and predecessor steps. উত্তরসূরি and পূর্বসূরি follow the directional arithmetic definitions; the full block compound remains provisional.
- Plausible alternatives: অমানক অংশ was considered for nonstandard part; অমানক খণ্ড continues the chapter’s block vocabulary. পূর্বগামী was considered for predecessor; পূর্বসূরি matches the successor/predecessor pair already used in the edition.
- Status: provisional-arithmetic-block-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মানক খণ্ড; অমানক খণ্ড; পাটিগাণিতিক খণ্ড; উত্তরসূরি; পূর্বসূরি’ express the OpenLogic sense(s) ‘standard part; nonstandard part; arithmetic block; successor; predecessor’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 62 occurrence(s). Representative locations:
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:29-46` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:47`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:47-56` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:46`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:20-27` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:23`; final reader page pending
  - `OLP-0214` `upstream/content/computability/recursive-functions/notation-pr-functions.tex:12-21` → `bn-Beng-IN/content/computability/recursive-functions/notation-pr-functions.tex:14`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:12-47` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:34`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
This may seem like an overly restrictive characterization of what
happens when we compute a new function using some existing ones. For
one thing, sometimes we do not use all the arguments of a function, as
when we defined $g(x, y, z) = \Succ(z)$ for use in the primitive
recursive definition of~$\Add$. Suppose we are allowed use of the
following functions:
\[
\Proj{n}{i}(x_0, \dots, x_{n-1}) = x_i
\]
The functions~$\Proj{k}{i}$ are called \emph{projection} functions:
$\Proj{n}{i}$ is an $n$-place function. Then $g$ can be defined by
\[
g(x, y, z) = \Succ(\Proj{3}{2}(x, y, z)).
\]
Here the role of $f$ is played by the $1$-place function $\Succ$, so
$k=1$. And we have one $3$-place function $\Proj{3}{2}$ which plays
the role of $g_0$. The result is a $3$-place function that returns the
successor of the third argument.
```

### BN-IN-T130

- Source term or concept: computable structure; computable function; decidable relation; computable presentation; Tennenbaum theorem
- Chosen Bengali: গণনসাধ্য গঠন; গণনসাধ্য অপেক্ষক; নির্ণেয় সম্বন্ধ; গণনসাধ্য উপস্থাপন; টেনেনবাউমের উপপাদ্য
- Rationale: Number, function, relation, proof and cardinality pages support the Bengali roots. গণনসাধ্য গঠন and গণনসাধ্য অপেক্ষক name effective operations, while নির্ণেয় সম্বন্ধ names a decidable order relation. গণনসাধ্য উপস্থাপন describes transporting an arithmetic structure to the natural numbers, and টেনেনবাউমের উপপাদ্য is retained as the established proper-name theorem. The specialized computability register remains open to expert review.
- Plausible alternatives: হিসাবযোগ্য was considered for computable; গণনসাধ্য keeps the operation-as-effective-procedure sense distinct from mere counting. সিদ্ধান্তযোগ্য was considered for decidable; নির্ণেয় follows the established relation vocabulary and the explicit decision procedure sense.
- Status: provisional-computability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্য গঠন; গণনসাধ্য অপেক্ষক; নির্ণেয় সম্বন্ধ; গণনসাধ্য উপস্থাপন; টেনেনবাউমের উপপাদ্য’ express the OpenLogic sense(s) ‘computable structure; computable function; decidable relation; computable presentation; Tennenbaum theorem’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 107 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:28-32` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:29`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:34`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:27-34` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:26`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:27-34` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:27`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T131

- Source term or concept: discrete linear order; dense order; countable nonstandard model; no endpoints
- Chosen Bengali: কঠোর রৈখিক ক্রম; ঘন রৈখিক ক্রম; গণনীয় অমানক মডেল; অন্তবিন্দুহীন
- Rationale: The canon supports order, number, mapping, proof and countability roots, while the chapter-specific combination of discrete arithmetic and dense block order is source-governed. কঠোর রৈখিক ক্রম names the strict order satisfied by every PA model; ঘন রৈখিক ক্রম describes the order of blocks in countable nonstandard models. অন্তবিন্দুহীন continues the established no-endpoint term. The scope restriction to গণনীয় অমানক মডেল is part of the semantic decision and remains reviewable.
- Plausible alternatives: বিচ্ছিন্ন রৈখিক ক্রম was considered for discrete linear order; কঠোর রৈখিক ক্রম matches the displayed strict-order axioms. গণনীয় অমানক গঠন was considered; গণনীয় অমানক মডেল preserves the chapter’s model-theoretic noun.
- Status: provisional-arithmetic-order-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কঠোর রৈখিক ক্রম; ঘন রৈখিক ক্রম; গণনীয় অমানক মডেল; অন্তবিন্দুহীন’ express the OpenLogic sense(s) ‘discrete linear order; dense order; countable nonstandard model; no endpoints’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 21 occurrence(s). Representative locations:
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:13-27` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:14`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:13-27` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:24`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:13-27` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:25`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:9-10` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:10`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:12-26` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:13`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}
The theory of strict linear orders in the language~$\Lang L_<$ is
axiomatized by the set
\begin{align*}
\{\quad & \lforall[x][\lnot x < x], \\
& \lforall[x][\lforall[y][((x < y \lor y <
    x) \lor x = y)]], \\
& \lforall[x][\lforall[y][\lforall[z][((x < y
      \land y < z) \lif x < z)]]] \quad \}
\end{align*}
It completely captures the intended !!{structure}s: every strict
linear order is a model of this axiom system, and vice versa, if $R$
is a linear order on a set $X$, then the structure $\Struct M$ with
$\Domain M = X$ and $\Assign{<}{M} = R$ is a model of this theory.
\end{ex}
```

### BN-IN-T132

- Source term or concept: cancellation law; commutative operations; midpoint; arithmetic operation
- Chosen Bengali: যোগের কর্তন-বিধি; বিনিময়যোগ্য ক্রিয়া; গড়; পাটিগাণিতিক ক্রিয়া
- Rationale: The recovered West Bengal algebra pages and the university operation pages support যোগ, গুণ, ক্রিয়া and the language of equations. যোগের কর্তন-বিধি names the PA cancellation principle used to rule out a standard successor, বিনিময়যোগ্য ক্রিয়া names commutativity, and গড় names the midpoint element obtained by halving a sum. These compounds are kept distinct from ordinary subtraction and geometric averaging by the displayed arithmetic equations.
- Plausible alternatives: বাতিলন বিধি was considered for cancellation law; যোগের কর্তন-বিধি states both the operation and the proof role explicitly. মধ্যবিন্দু was considered for midpoint; গড় follows the arithmetic halving construction used in the proof.
- Status: provisional-arithmetic-operation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যোগের কর্তন-বিধি; বিনিময়যোগ্য ক্রিয়া; গড়; পাটিগাণিতিক ক্রিয়া’ express the OpenLogic sense(s) ‘cancellation law; commutative operations; midpoint; arithmetic operation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 31 occurrence(s). Representative locations:
  - `OLP-0210` `upstream/content/computability/recursive-functions/introduction.tex:12-28` → `bn-Beng-IN/content/computability/recursive-functions/introduction.tex:12`; final reader page pending
  - `OLP-0210` `upstream/content/computability/recursive-functions/introduction.tex:12-28` → `bn-Beng-IN/content/computability/recursive-functions/introduction.tex:13`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:92`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:114-123` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:120`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In order to develop a mathematical theory of computability, one has to,
first of all, develop a \emph{model} of computability.  We now think of
computability as the kind of thing that computers do, and computers
work with symbols.  But at the beginning of the development of
theories of computability, the paradigmatic example of computation was
\emph{numerical} computation.  Mathematicians were always interested
in number-theoretic functions, i.e., functions $f\colon \Nat^n \to
\Nat$ that can be computed. So it is not surprising that at the
beginning of the theory of computability, it was such functions that
were studied.  The most familiar examples of computable numerical
functions, such as addition, multiplication, exponentiation (of
natural numbers) share an interesting feature: they can be defined
\emph{recursively}.  It is thus quite natural to attempt a general
definition of \emph{computable function} on the basis of recursive
definitions.  Among the many possible ways to define number-theoretic
functions recursively, one particularly simple pattern of definition
here becomes central: so-called \emph{primitive recursion}.
```

### BN-IN-T133

- Source term or concept: transport of structure; computable presentation; up to isomorphism; bijection
- Chosen Bengali: গঠন পরিবাহন; গণনসাধ্য উপস্থাপন; সমরূপতা পর্যন্ত; বিজেকশন
- Rationale: The checked relation and mapping pages support bijections, inverses and isomorphism roots. গঠন পরিবাহন describes moving interpretations along a bijection, গণনসাধ্য উপস্থাপন names the resulting natural-number presentation, and সমরূপতা পর্যন্ত states the correct uniqueness scope for Tennenbaum’s theorem. বিজেকশন is retained as the concise mapping term in the computable-model example. The complete presentation register remains open to expert review.
- Plausible alternatives: সমরূপতা-অনুবহন was considered for transport of structure; গঠন পরিবাহন is more readable in Bengali explanatory prose. সমরূপতার সাপেক্ষে একক was considered for up to isomorphism; সমরূপতা পর্যন্ত is concise and matches the theorem statement.
- Status: provisional-arithmetic-presentation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গঠন পরিবাহন; গণনসাধ্য উপস্থাপন; সমরূপতা পর্যন্ত; বিজেকশন’ express the OpenLogic sense(s) ‘transport of structure; computable presentation; up to isomorphism; bijection’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0197` `upstream/content/model-theory/models-of-arithmetic/computable-models.tex:119-121` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/computable-models.tex:116`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}[Tennenbaum's Theorem]
$\Struct{N}$ is the only computable model of~$\Th{PA}$.
\end{thm}
```

### BN-IN-T134

- Source term or concept: Craig interpolation; interpolant; shared-language vocabulary
- Chosen Bengali: ক্রেগের ইন্টারপোলেশন; ইন্টারপোল্যান্ট; অভিন্ন ভাষার সংকেত
- Rationale: The logic, quantification, relation, mapping and proof witnesses support the component roots, while the complete model-theoretic interpolation vocabulary remains governed by the displayed theorem. ইন্টারপোল্যান্ট names the sentence implied by !A and implying !B, and the shared-language condition restricts its nonlogical symbols to those occurring on both sides. Proper-name rendering ক্রেগের is retained for the theorem attribution. Expert review remains welcome for the full compound অভিন্ন ভাষার সংকেত.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-interpolation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ক্রেগের ইন্টারপোলেশন; ইন্টারপোল্যান্ট; অভিন্ন ভাষার সংকেত’ express the OpenLogic sense(s) ‘Craig interpolation; interpolant; shared-language vocabulary’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:71-126` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:109`; final reader page pending
  - `OLP-0201` `upstream/content/model-theory/interpolation/interpolation-proof.tex:11-11` → `bn-Beng-IN/content/model-theory/interpolation/interpolation-proof.tex:11`; final reader page pending
  - `OLP-0201` `upstream/content/model-theory/interpolation/interpolation-proof.tex:13-20` → `bn-Beng-IN/content/model-theory/interpolation/interpolation-proof.tex:13`; final reader page pending
  - `OLP-0201` `upstream/content/model-theory/interpolation/interpolation-proof.tex:13-20` → `bn-Beng-IN/content/model-theory/interpolation/interpolation-proof.tex:19`; final reader page pending
  - `OLP-0201` `upstream/content/model-theory/interpolation/interpolation-proof.tex:29-32` → `bn-Beng-IN/content/model-theory/interpolation/interpolation-proof.tex:30`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
If $\Sigma(P)$ explicitly defines $P$ then both
\begin{align*}
  \Sigma(P) & \Entails & \lforall[x_1][\dots \lforall[x_n]
    [(\Atom{P}{x_1,\dots, x_n} \liff !C(x_1,\dots,x_n))]]\\
  \Sigma(P') & \Entails & \lforall[x_1][\dots \lforall[x_n]
    [(\Atom{P'}{x_1,\dots, x_n} \liff !C(x_1,\dots,x_n))]]
\end{align*}
and the conclusion follows. For the converse: assume that $\Sigma(P)$
implicitly defines $P$. First, we add !!{constant}s $c_1$, \dots,~$c_n$ to
$\Lang{L}$. Then
\[
\Sigma(P) \cup \Sigma(P') \Entails
\Atom{P}{c_1, \dots, c_n} \to  \Atom{P'}{c_1, \dots, c_n}.
\]
By compactness, there are finite sets $\Delta_0 \subseteq \Sigma(P)$
and $\Delta_1 \subseteq \Sigma(P')$ such that
\[
\Delta_0 \cup \Delta_1 \Entails
\Atom{P}{c_1, \dots, c_n} \to \Atom{P'}{c_1, \dots, c_n}.
\]
Let $!D(P)$ be the conjunction of all !!{sentence}s $!A(P)$ such that
either $!A(P) \in \Delta_0$ or $!A(P') \in \Delta_1$ and let $!D(P')$
be the conjunction of all !!{sentence}s $!A(P')$ such that either
$!A(P) \in \Delta_0$ or $!A(P') \in \Delta_1$. Then $!D(P) \land
!D(P') \Entails \Atom{P}{c_1, \dots, c_n} \to P'c_1\dots c_n$. We can
re-arrange this so that each !!{predicate} occurs on one side of
$\Entails$:
\[
!D(P) \land \Atom{P}{c_1, \dots, c_n} \Entails
!D(P') \to \Atom{P'}{c_1, \dots, c_n}.
\]
By Craig's Interpolation Theorem there is !!a{sentence} $!C(c_1,\dots, c_n)$
not containing $P$ or $P'$ such that:
\begin{align*}
  !D(P) \land \Atom{P}{c_1, \dots, c_n} & \Entails !C(c_1,\dots, c_n); \\
  !C(c_1,\dots, c_n) & \Entails !D(P') \to \Atom{P'}{c_1, \dots, c_n}.
\end{align*}
From the former of these two entailments we have: $!D(P) \Entails
\Atom{P}{c_1,\dots, c_n} \lif !C(c_1,\dots, c_n)$. And from the
latter, since an $\Lang{L} \cup \{P\}$-model $\Expan{M}{R}
\Entails !A(P)$ if and only if the corresponding $\Lang{L} \cup
\{P'\}$-model $\Expan{M}{R} \models !A(P')$, we have
$!C(c_1,\dots, c_n) \Entails !D(P) \lif \Atom{P}{c_1,\dots, c_n}$,
from which:
\[
!D(P) \Entails !C(c_1,\dots,c_n) \to \Atom{P}{c_1,\dots, c_n}.
\]
Putting the two together, $!D(P) \Entails \Atom{P}{c_1,\dots, c_n}
\liff !C(c_1, \dots, c_n)$, and by monotonicity and generalization also
\[
\Sigma(P) \Entails
\lforall[x_1][\dots\lforall[x_n][(\Atom{P}{x_1,\dots, x_n} \liff
    !C(x_1,\dots, x_n))]].
\]
\end{proof}
```

### BN-IN-T135

- Source term or concept: separation; separator; inseparable sets
- Chosen Bengali: পৃথকীকরণ; পৃথককারী; অপৃথকযোগ্য সমষ্টি
- Rationale: The checked logic, quantification, relation and proof pages support the semantic direction of a separator, but the exact interpolation lemma vocabulary is source-governed. পৃথককারী is the formula that entails from one set and whose negation follows from the other; অপৃথকযোগ্য records the absence of such a sentence. The target prose also retains the inflected verb পৃথক করে where the surrounding sentence calls for it.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-separation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পৃথকীকরণ; পৃথককারী; অপৃথকযোগ্য সমষ্টি’ express the OpenLogic sense(s) ‘separation; separator; inseparable sets’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:183-202` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:189`; final reader page pending
  - `OLP-0172` `upstream/content/first-order-logic/models-theories/set-theory.tex:149-171` → `bn-Beng-IN/content/first-order-logic/models-theories/set-theory.tex:169`; final reader page pending
  - `OLP-0200` `upstream/content/model-theory/interpolation/separation.tex:11-11` → `bn-Beng-IN/content/model-theory/interpolation/separation.tex:11`; final reader page pending
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

### BN-IN-T136

- Source term or concept: maximally consistent; maximally inseparable pair; compactness
- Chosen Bengali: সর্বাধিক সঙ্গত; সর্বাধিক অপৃথকযোগ্য জোড়া; সংহতি
- Rationale: The finite-set, relation, quantification and proof witnesses support maximality, consistency and compactness roots, while the simultaneous maximal-pair construction is governed by the source proof. সর্বাধিক সঙ্গত marks a set containing each sentence or its negation without inconsistency; সর্বাধিক অপৃথকযোগ্য জোড়া names the constructed pair; সংহতি carries the finite-support argument used to pass from the pair to its union.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: mixed-attested-roots-and-provisional-interpolation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সর্বাধিক সঙ্গত; সর্বাধিক অপৃথকযোগ্য জোড়া; সংহতি’ express the OpenLogic sense(s) ‘maximally consistent; maximally inseparable pair; compactness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 39 occurrence(s). Representative locations:
  - `OLP-0118` `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:112-120` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex:116`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:204-209` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:204`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:13-13` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:13`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:15-24` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:16`; final reader page pending
  - `OLP-0136` `upstream/content/first-order-logic/completeness/compactness-direct.tex:115-118` → `bn-Beng-IN/content/first-order-logic/completeness/compactness-direct.tex:115`; final reader page pending
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

### BN-IN-T137

- Source term or concept: amalgamated model; common-language isomorphism; predicate interpretation
- Chosen Bengali: সম্মিলিত মডেল; অভিন্ন ভাষায় সমরূপতা; প্রেডিকেটের ব্যাখ্যা
- Rationale: The quantification, relation and mapping witnesses support structure, interpretation and isomorphism roots, while the amalgamated-model construction is specific to the frozen proof. সমরূপতা names the map preserving constants, predicates and functions in the common language; প্রেডিকেটের ব্যাখ্যা states the transported relation used to build the final model. The compounds সম্মিলিত মডেল and অভিন্ন ভাষায় remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-amalgamation-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সম্মিলিত মডেল; অভিন্ন ভাষায় সমরূপতা; প্রেডিকেটের ব্যাখ্যা’ express the OpenLogic sense(s) ‘amalgamated model; common-language isomorphism; predicate interpretation’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T138

- Source term or concept: explicit definability; implicit definability; Beth definability theorem
- Chosen Bengali: প্রকাশ্যভাবে সংজ্ঞায়িত; অন্তর্নিহিতভাবে সংজ্ঞায়িত; বেথের সংজ্ঞায়ন উপপাদ্য
- Rationale: The logic, quantification, relation, mapping and proof witnesses support definition and entailment roots, while the explicit/implicit distinction and Beth theorem are governed by the source clauses. প্রকাশ্যভাবে সংজ্ঞায়িত gives a formula in the base language; অন্তর্নিহিতভাবে সংজ্ঞায়িত fixes the predicate interpretation across expansions; বেথের সংজ্ঞায়ন উপপাদ্য states their equivalence. Expert review remains welcome for the full model-theoretic register.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-definability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রকাশ্যভাবে সংজ্ঞায়িত; অন্তর্নিহিতভাবে সংজ্ঞায়িত; বেথের সংজ্ঞায়ন উপপাদ্য’ express the OpenLogic sense(s) ‘explicit definability; implicit definability; Beth definability theorem’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:13-32` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:18`; final reader page pending
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:13-32` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:28`; final reader page pending
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:34-44` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:34`; final reader page pending
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:46-57` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:47`; final reader page pending
  - `OLP-0202` `upstream/content/model-theory/interpolation/definability.tex:66-69` → `bn-Beng-IN/content/model-theory/interpolation/definability.tex:66`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
One important application of the interpolation theorem is Beth's
definability theorem.  To define an $n$-place relation~$R$ we can give
!!a{formula}~$!C$ with $n$ free !!{variable}s which does not
involve~$R$. This would be an \emph{explicit} definition of~$R$ in
terms of~$!C$.  We can then say also that a theory~$\Sigma(P)$ in a
!!{language} containing the $n$-place !!{predicate}~$P$ explicitly
defines~$P$ if it contains (or at least entails) a formalized explicit
definition, i.e.,
\[
\Sigma(P) \Entails \lforall[x_1][\dots
  \lforall[x_n][(\Atom{P}{x_1,\dots, x_n} \liff !C(x_1, \dots,
    x_n))]].
\]
But an explicit definition is only one way of defining---in the sense
of determining completely---a relation.  A theory may also be such
that the interpretation of~$P$ is fixed by the interpretation of the
rest of the !!{language} in any model.  The definability theorem
states that whenever a theory fixes the interpretation of~$P$ in this
way---whenever it \emph{implicitly defines}~$P$---then it also
explicitly defines it.
```

### BN-IN-T139

- Source term or concept: abstract logic; abstract logic sentence; satisfaction relation
- Chosen Bengali: বিমূর্ত যুক্তিবিদ্যা; বিমূর্ত যুক্তিবিদ্যার বাক্য; সন্তুষ্টি-সম্পর্ক
- Rationale: Logic, quantification, relation, mapping and proof witnesses support the component roots, while the abstract-logic compound is governed by the frozen definition. বিমূর্ত যুক্তিবিদ্যা names the pair consisting of a language-to-sentence assignment and a satisfaction relation; সন্তুষ্টি-সম্পর্ক names the relation between structures and sentences. Expert review remains welcome for the specialized compound.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-abstract-logic-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বিমূর্ত যুক্তিবিদ্যা; বিমূর্ত যুক্তিবিদ্যার বাক্য; সন্তুষ্টি-সম্পর্ক’ express the OpenLogic sense(s) ‘abstract logic; abstract logic sentence; satisfaction relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:9-10` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:10`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:12-22` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:13`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:12-22` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:22`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:48-106` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:50`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:48-106` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:75`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{mod}{lin}{alg}
\olsection{Abstract Logics}
```

### BN-IN-T140

- Source term or concept: normal abstract logic; monotonicity; expansion property; relativization property
- Chosen Bengali: স্বাভাবিক বিমূর্ত যুক্তিবিদ্যা; একঘেয়েমিতা; প্রসারণ ধর্ম; আপেক্ষিকীকরণ ধর্ম
- Rationale: The checked logic and proof pages support closure, relation, mapping and formula roots, but the seven-property normality package is source-defined. স্বাভাবিক বিমূর্ত যুক্তিবিদ্যা is the abstract logic satisfying language monotonicity, finite expansion, isomorphism, renaming, Boolean, quantifier and relativization conditions. The selected ধর্ম compounds remain open to expert correction.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-normality-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাভাবিক বিমূর্ত যুক্তিবিদ্যা; একঘেয়েমিতা; প্রসারণ ধর্ম; আপেক্ষিকীকরণ ধর্ম’ express the OpenLogic sense(s) ‘normal abstract logic; monotonicity; expansion property; relativization property’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:121-134` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:130`; final reader page pending
  - `OLP-0206` `upstream/content/model-theory/lindstrom/ls-property.tex:49-57` → `bn-Beng-IN/content/model-theory/lindstrom/ls-property.tex:51`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{rem}
  First-order logic, i.e., the abstract logic $\tuple{F, \models}$, is
  normal. In fact, the above properties are mostly straightforward for
  first-order logic. We just remark that the expansion property comes
  down to extensionality, and that the relativization of
  !!a{sentence} $!E$ to $\Atom{R}{x, c_1, \dots, c_n}$ is obtained by
  replacing each !!{subformula} $\lforall[x][!F]$ by
  $\lforall[x][(\Atom{R}{x, c_1, \dots, c_n} \lif \ !F)]$. Moreover,
  if $\tuple{L, \models_L}$ is normal, then
  $\tuple{F, \models} \leq \tuple{L, \models_{L}}$, as can be can
  shown by induction on first-order !!{formula}s. Accordingly, with no
  loss in generality, we can assume that every first-order
  !!{sentence} belongs to every normal logic.
\end{rem}
```

### BN-IN-T141

- Source term or concept: compactness property; finite satisfiability
- Chosen Bengali: কম্প্যাক্টনেস ধর্ম; সসীমভাবে সন্তোষণীয়
- Rationale: Finite/infinite, model, quantification and proof pages support the finite-subset implication. কম্প্যাক্টনেস ধর্ম is retained as the named abstract-logic property; সসীমভাবে সন্তোষণীয় states that every finite subset has a model. The complete compound remains definition-governed and open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: mixed-attested-and-provisional-compactness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কম্প্যাক্টনেস ধর্ম; সসীমভাবে সন্তোষণীয়’ express the OpenLogic sense(s) ‘compactness property; finite satisfiability’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0207` `upstream/content/model-theory/lindstrom/lindstrom-proof.tex:107-122` → `bn-Beng-IN/content/model-theory/lindstrom/lindstrom-proof.tex:107`; final reader page pending
  - `OLP-0206` `upstream/content/model-theory/lindstrom/ls-property.tex:16-21` → `bn-Beng-IN/content/model-theory/lindstrom/ls-property.tex:18`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:223-227` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:236`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:249-257` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:264`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Using the Compactness Property, we can find a model $\Struct{M}^*$ of
$!D$ in which the ordering contains a non-standard element~$n^*$. In
particular then $\Struct{M^*}$ will contain sub!!{structure}s
$\Struct{M_{n^*}}$ and $\Struct{N_{n^*}}$ such that $\Struct{M_{n^*}}
\models_L !E$ and $\Struct{N_{n^*}} \not\models_L !E$. But now we can
define a set $\mathcal{I}$ of pairs of $k$-tuples from
$\Domain{M_{n^*}}$ and $\Domain{N_{n^*}}$ by putting
$\tuple{\mathbf{a}, \mathbf{b}} \in \mathcal{I}$ if and only if
$J(n^*-k, \mathbf{a}, \mathbf{b})$, where $k$ is the length of
$\mathbf{a}$ and $\mathbf{b}$. Since $n^*$ is non-standard, for each
standard $k$ we have that $n^* - k >0$, and the set $\mathcal{I}$
witnesses the fact that $\Struct{M_{n^*}} \simeq_p
\Struct{N_{n^*}}$. But by \olref[lsp]{thm:abstract-p-isom},
$\Struct{M_{n^*}}$ is $L$-equivalent to $\Struct{N_{n^*}}$, a
contradiction.
\end{proof}
```

### BN-IN-T142

- Source term or concept: downward Löwenheim--Skolem property; enumerable model
- Chosen Bengali: নিম্নমুখী লোয়েনহাইম--স্কোলেম ধর্ম; গণনীয় মডেল
- Rationale: Number, countability, logic, relation, mapping and proof pages support enumerable and model roots, while the named property is governed by the chapter definition. নিম্নমুখী marks the direction of the cardinality reduction and গণনীয় মডেল names the enumerable witness. Proper-name spelling and the full compound remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-lowenheim-skolem-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিম্নমুখী লোয়েনহাইম--স্কোলেম ধর্ম; গণনীয় মডেল’ express the OpenLogic sense(s) ‘downward Löwenheim--Skolem property; enumerable model’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0196` `upstream/content/model-theory/models-of-arithmetic/models-of-pa.tex:238-259` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/models-of-pa.tex:263`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
The non-standard blocks are therefore ordered like the rationals: they
form !!a{denumerable} dense linear ordering without endpoints.  One can show
that any two such !!{denumerable} orderings are isomorphic. It follows
that for any two !!{enumerable} non-standard models $\Struct{M}_1$ and
$\Struct{M_2}$ of true arithmetic, their reducts to the language
containing $<$ and $=$ only are isomorphic. Indeed, an isomorphism $h$
can be defined as follows: the standard parts of $\Struct{M_1}$ and
$\Struct{M_2}$ are isomorphic to the standard model $\Struct{N}$ and
hence to each other. The blocks making up the non-standard part are
themselves ordered like the rationals and therefore isomorphic; an
isomorphism of the blocks can be extended to an isomorphism
\emph{within} the blocks by matching up arbitrary elements in each,
and then taking the image of the successor of $x$ in $\Struct{M_1}$ to
be the successor of the image of $x$ in $\Struct{M_2}$. Note that it
does \emph{not} follow that $\mathfrak{M}_1$ and $\mathfrak{M}_2$ are
isomorphic in the full language of arithmetic (indeed, isomorphism is
always relative to !!a{language}), as there are non-isomorphic ways to
define addition and multiplication over $\Domain{M_1}$ and
$\Domain{M_2}$. (This also follows from a famous theorem due to Vaught
that the number of countable models of a complete theory cannot be~2.)
\end{explain}
```

### BN-IN-T143

- Source term or concept: partial isomorphism; partially isomorphic; back-and-forth
- Chosen Bengali: আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু
- Rationale: Set, relation, mapping, inclusion and proof pages support the component roots, while the finite partial-map and back-and-forth package is source-defined. আংশিক সমরূপতা preserves constants and all relations/functions on the finite domain; আংশিকভাবে সমরূপ is its adjectival form; আগ-পিছু names the alternating extension conditions. Expert review remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-partial-isomorphism-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক সমরূপতা; আংশিকভাবে সমরূপ; আগ-পিছু’ express the OpenLogic sense(s) ‘partial isomorphism; partially isomorphic; back-and-forth’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:35`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:33-40` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:37`; final reader page pending
  - `OLP-0190` `upstream/content/model-theory/basics/dlo.tex:68-83` → `bn-Beng-IN/content/model-theory/basics/dlo.tex:79`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:9-10` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:10`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:12-31` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:14`; final reader page pending
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

### BN-IN-T144

- Source term or concept: expressive power; at least as expressive; expressiveness ordering
- Chosen Bengali: প্রকাশক্ষমতা; অন্তত ততটাই প্রকাশক্ষম; প্রকাশক্ষমতার ক্রম
- Rationale: Logic, relation, mapping and proof witnesses support the comparison language, while the abstract-logic ordering is fixed by equality of model classes. অন্তত ততটাই প্রকাশক্ষম states that every sentence of one logic has an equivalent sentence in the other; প্রকাশক্ষমতা names the resulting comparison. The full compound remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-expressiveness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রকাশক্ষমতা; অন্তত ততটাই প্রকাশক্ষম; প্রকাশক্ষমতার ক্রম’ express the OpenLogic sense(s) ‘expressive power; at least as expressive; expressiveness ordering’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:108-119` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:115`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
Given two abstract logics $\tuple{L_1, \models_{L_1}}$ and
$\tuple{L_2, \models_{L_2}}$ we say that the latter is \emph{at least
  as expressive} as the former, written $\tuple{L_1, \models_{L_1}}
\leq \tuple{L_2, \models_{L_2}}$, if for each !!{language} $\Lang{L}$
and !!{sentence} $!E \in L_1(\Lang{L})$ there is !!a{sentence} $!F
\in L_2(\Lang{L})$ such that $\Mod[L](L_1){!E} =
\Mod[L](L_2){!F}$. The logics $\tuple{L_1, \models_{L_1}}$ and
$\tuple{L_2, \models_{L_2}}$ are \emph{equivalent} if $\tuple{L_1,
  \models_{L_1}} \leq \tuple{L_2, \models_{L_2}}$ and $\tuple{L_2,
  \models_{L_2}} \leq \tuple{L_1, \models_{L_1}}$.
\end{defn}
```

### BN-IN-T145

- Source term or concept: elementary equivalence; elementarily equivalent structures
- Chosen Bengali: মৌলিকভাবে সমতুল্য; মৌলিকভাবে সমতুল্য গঠন
- Rationale: The checked logic, quantification, relation and proof pages support sentence, truth and equivalence roots. মৌলিকভাবে সমতুল্য means agreement on every sentence of the common language and is weaker than isomorphism; মৌলিকভাবে সমতুল্য গঠন is the corresponding noun phrase. The model-theoretic compound remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-elementary-equivalence-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মৌলিকভাবে সমতুল্য; মৌলিকভাবে সমতুল্য গঠন’ express the OpenLogic sense(s) ‘elementary equivalence; elementarily equivalent structures’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0187` `upstream/content/model-theory/basics/isomorphism.tex:12-24` → `bn-Beng-IN/content/model-theory/basics/isomorphism.tex:14`; final reader page pending
  - `OLP-0187` `upstream/content/model-theory/basics/isomorphism.tex:26-33` → `bn-Beng-IN/content/model-theory/basics/isomorphism.tex:29`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:39-46` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:44`; final reader page pending
  - `OLP-0206` `upstream/content/model-theory/lindstrom/ls-property.tex:29-39` → `bn-Beng-IN/content/model-theory/lindstrom/ls-property.tex:35`; final reader page pending
  - `OLP-0206` `upstream/content/model-theory/lindstrom/ls-property.tex:41-47` → `bn-Beng-IN/content/model-theory/lindstrom/ls-property.tex:44`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
First-order !!{structure}s can be alike in one of two ways. One way in
which they can be alike is that they make the same !!{sentence}s
true. We call such !!{structure}s \emph{elementarily equivalent}. But
structures can be very different and still make the same !!{sentence}s
true---for instance, one can be !!{enumerable} and the other not.
This is because there are lots of features of !!a{structure} that
cannot be expressed in first-order languages, either because the
language is not rich enough, or because of fundamental limitations of
first-order logic such as the L\"owenheim--Skolem theorem. So another,
stricter, aspect in which !!{structure}s can be alike is if they are
fundamentally the same, in the sense that they only differ in the
objects that make them up, but not in their structural features. A way
of making this precise is by the notion of an \emph{isomorphism}.
```

### BN-IN-T146

- Source term or concept: relativization; relativization property; reduct
- Chosen Bengali: আপেক্ষিকীকরণ; আপেক্ষিকীকরণ ধর্ম; রিডাক্ট
- Rationale: Logic, quantification, relation and proof pages support restriction and substructure roots, while the exact relativization construction is source-defined. আপেক্ষিকীকরণ restricts a sentence to the substructure cut out by a new predicate and constants; রিডাক্ট names the structure obtained by forgetting symbols. Expert review remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-relativization-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আপেক্ষিকীকরণ; আপেক্ষিকীকরণ ধর্ম; রিডাক্ট’ express the OpenLogic sense(s) ‘relativization; relativization property; reduct’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:48-106` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:60`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:48-106` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:61`; final reader page pending
  - `OLP-0205` `upstream/content/model-theory/lindstrom/abstract-logics.tex:121-134` → `bn-Beng-IN/content/model-theory/lindstrom/abstract-logics.tex:131`; final reader page pending
  - `OLP-0196` `upstream/content/model-theory/models-of-arithmetic/models-of-pa.tex:238-259` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/models-of-pa.tex:251`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
An abstract logic $\tuple{L,\models_L}$ for the !!{language} $\Lang{L}$
is \emph{normal} if it satisfies the following properties:
\begin{enumerate}
\item (\emph{$L$-Monotonicity}) For !!{language}s $\Lang{L}$ and
  $\Lang{L'}$, if $\Lang{L} \subseteq \Lang{L'}$, then
  $L(\Lang{L}) \subseteq L(\Lang{L'})$.
\item (\emph{Expansion Property}) For each $!E \in L(\Lang{L})$
  there is a \emph{finite} subset $\Lang{L'}$ of $\Lang{L}$ such that
  the relation $\Struct{M} \models_L !E$ depends only on the
  reduct of $\Struct{M}$ to $\Lang{L'}$; i.e., if $\Struct{M}$ and
  $\Struct{N}$ have the same reduct to $\Lang{L'}$ then $\Struct{M}
  \models_L !E$ if and only if $\Struct{N} \models_L !E$.
\item (\emph{Isomorphism Property}) If $\Struct{M} \models_L !E$
  and $\Struct{M} \simeq \Struct{N}$ then also $\Struct{N} \models_L
  !E$.
\item (\emph{Renaming Property}) The relation $\models_L$ is preserved
  under renaming: if the !!{language} $\Lang{L}'$ is obtained from
  $\Lang{L}$ by replacing each symbol $P$ by a symbol $P'$ of the same
  arity and each constant $c$ by a distinct constant $c'$, then for
  each !!{structure}~$\Struct{M}$ and !!{sentence}~$!E$, $\Struct{M}
  \models_L !E$ if and only if $\Struct{M}' \models_L !E'$,
  where $\Struct{M}'$ is the $\Lang{L}'$-!!{structure} corresponding
  to $\Lang{L}$ and $!E' \in L(\Lang{L}')$.
\item (\emph{Boolean Property}) The abstract logic $\tuple{L,
  \models_L}$ is closed under the Boolean connectives in the sense
  that for each $!E \in L(\Lang{L})$ there is a~$!F \in
  L(\Lang{L})$ such that $\Struct{M} \models_L !F$ if and only if
  $\Struct{M} \not\models_L !E$, and for each $!E$ and $!F$
  there is a $!G$ such that $\Mod(L){!G} = \Mod(L){!E} \cap
  \Mod(L){!F}$.  Similarly for atomic !!{formula}s and the other
  connectives.
\item (\emph{Quantifier Property}) For each constant $c$ in $\Lang{L}$
  and $!E \in L(\Lang{L})$ there is a $!F \in L(\Lang{L})$ such
  that
  \[
  \Mod[L'](L){!F} = \Setabs{\Struct{M}}{\Expan{M}{a} \in
  \Mod[L](L){!E} \text{ for some } a \in \Domain{M}},
  \]
  where $\Lang{L'} = \Lang{L} \setminus \{c\}$ and $\Expan{M}{a}$
  is the expansion of $\Struct{M}$ to $\Lang{L}$ assigning $a$
  to~$c$.
\item (\emph{Relativization Property}) Given !!a{sentence} $!E \in
  L(\Lang{L})$ and symbols $R$, $c_1$, \dots, $c_n$ not in $\Lang{L}$,
  there is !!a{sentence} $!F \in L(\Lang{L} \cup \{R,c_1,\ldots,c_n\})$
  called the \emph{relativization} of $!E$ to $\Atom{R}{x, c_1, \dots c_n}$,
  such that for each !!{structure}~$\Struct{M}$:
  \[
  \Expan{M}{X, b_1, \ldots, b_n} \models_L !F \text{ if and
    only if } \Struct{N} \models_L !E,
  \]
  where $\Struct{N}$ is the substructure of $\Struct{M}$ with !!{domain}
  $\Domain{N} = \Setabs{a\in \Domain{M}}{\Assign{R}{M}(a, b_1, \dots, b_n)}$
  (see \olref[bas][sub]{rem:substructure}), and $\Expan{M}{X, b_1, \ldots,
    b_n}$ is the expansion of $\Struct{M}$ interpreting $R$, $c_1$,
  \dots, $c_n$ by $X$, $b_1,$ \dots, $b_n$, respectively (with $X
  \subseteq M^{n+1}$).
\end{enumerate}
\end{defn}
```

### BN-IN-T147

- Source term or concept: quantifier rank; n-equivalent structures; finite rank types
- Chosen Bengali: পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম ক্রমাঙ্ক-প্রকার
- Rationale: Quantification, finite sequence, relation and proof pages support the component roots, while bounded quantifier rank is governed by the Lindström proof. পরিমাণসূচক-ক্রমাঙ্ক counts maximum nesting; n-সমতুল্য গঠন agree on first-order sentences up to rank n; সসীম ক্রমাঙ্ক-প্রকার names the finite logical-equivalence classes used in the disjunction. Expert review remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-quantifier-rank-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পরিমাণসূচক-ক্রমাঙ্ক; n-সমতুল্য গঠন; সসীম ক্রমাঙ্ক-প্রকার’ express the OpenLogic sense(s) ‘quantifier rank; n-equivalent structures; finite rank types’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:113-120` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:115`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:113-120` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:120`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:122-129` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:127`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:176-183` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:182`; final reader page pending
  - `OLP-0189` `upstream/content/model-theory/basics/partial-iso.tex:176-183` → `bn-Beng-IN/content/model-theory/basics/partial-iso.tex:185`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
  For any !!{formula}~$!A$, the \emph{quantifier rank} of $!A$, denoted
  by $\QuantRank{!A} \in \Nat$, is recursively defined as
  the highest number of nested quantifiers in $!A$.  Two
  !!{structure}s $\Struct{M}$ and $\Struct{N}$ are \emph{$n$-equivalent},
  written $\Struct{M} \elemequiv[n] \Struct{N}$, if they agree on all
  sentences of quantifier rank less than or equal to~$n$.
\end{defn}
```

### BN-IN-T148

- Source term or concept: Lindström theorem; Lindström lemma; nonstandard element
- Chosen Bengali: লিন্ডস্ট্রমের উপপাদ্য; লিন্ডস্ট্রমের লেমা; অমানক উপাদান
- Rationale: Number, logic, relation, mapping, proof and cardinality pages support theorem, lemma, model and nonstandard-element roots. লিন্ডস্ট্রমের উপপাদ্য names the compactness/Löwenheim--Skolem characterization; লিন্ডস্ট্রমের লেমা names the bounded-rank reduction; অমানক উপাদান is the compactness witness beyond every standard finite stage. Proper-name and chapter-specific compounds remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-lindstrom-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘লিন্ডস্ট্রমের উপপাদ্য; লিন্ডস্ট্রমের লেমা; অমানক উপাদান’ express the OpenLogic sense(s) ‘Lindström theorem; Lindström lemma; nonstandard element’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0207` `upstream/content/model-theory/lindstrom/lindstrom-proof.tex:11-11` → `bn-Beng-IN/content/model-theory/lindstrom/lindstrom-proof.tex:11`; final reader page pending
  - `OLP-0207` `upstream/content/model-theory/lindstrom/lindstrom-proof.tex:47-52` → `bn-Beng-IN/content/model-theory/lindstrom/lindstrom-proof.tex:48`; final reader page pending
  - `OLP-0207` `upstream/content/model-theory/lindstrom/lindstrom-proof.tex:107-122` → `bn-Beng-IN/content/model-theory/lindstrom/lindstrom-proof.tex:108`; final reader page pending
  - `OLP-0203` `upstream/content/model-theory/lindstrom/lindstrom.tex:8-8` → `bn-Beng-IN/content/model-theory/lindstrom/lindstrom.tex:8`; final reader page pending
  - `OLP-0192` `upstream/content/model-theory/models-of-arithmetic/introduction.tex:55-70` → `bn-Beng-IN/content/model-theory/models-of-arithmetic/introduction.tex:55`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olsection{Lindstr\"om's Theorem}
```

### BN-IN-T149

- Source term or concept: abstract-logic elementary equivalence; elementary equivalent
- Chosen Bengali: মৌলিকভাবে সমতুল্য কাঠামো
- Rationale: This entry records the noun phrase used when the abstract-logic definition and partial-isomorphism theorem state agreement on all sentences. মৌলিকভাবে সমতুল্য কাঠামো is kept distinct from সমরূপ গঠন: the former is sentence-theoretic agreement, while the latter requires a structure-preserving bijection. Expert review remains welcome for this edition normalization.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-terminology-normalization-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘মৌলিকভাবে সমতুল্য কাঠামো’ express the OpenLogic sense(s) ‘abstract-logic elementary equivalence; elementary equivalent’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T150

- Source term or concept: primitive recursion; primitive recursive definition; primitive recursive function
- Chosen Bengali: আদিম পুনরাবৃত্তি; আদিম পুনরাবৃত্তির মাধ্যমে সংজ্ঞা; আদিম পুনরাবৃত্ত অপেক্ষক
- Rationale: Number, relation, mapping and proof pages support the component roots, while the recursive-function construction is governed by the displayed zero and successor clauses. আদিম পুনরাবৃত্তি names the scheme that uses an initial value and the immediately preceding value; আদিম পুনরাবৃত্ত অপেক্ষক names a function obtained by that scheme. The chapter-specific compound remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computability-recursion-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আদিম পুনরাবৃত্তি; আদিম পুনরাবৃত্তির মাধ্যমে সংজ্ঞা; আদিম পুনরাবৃত্ত অপেক্ষক’ express the OpenLogic sense(s) ‘primitive recursion; primitive recursive definition; primitive recursive function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 83 occurrence(s). Representative locations:
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:18-28` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:24`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:32`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:45-52` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:45`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:132`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:36-60` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:45`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}
\ollabel{thm:ce-equiv}
Let $S$ be a set of natural numbers. Then the following are
equivalent:
\begin{enumerate}
\item\ollabel{case:ce} $S$ is computably enumerable.
\item\ollabel{case:ran-pc} $S$ is the range of a \emph{partial} computable function.
\item\ollabel{case:ran-prim} $S$ is empty or the range of a primitive recursive function.
\item\ollabel{case:ce-domain} $S$ is the \emph{domain} of a partial computable function.
\end{enumerate}
\end{thm}
```

### BN-IN-T151

- Source term or concept: recursive function; recursive definition
- Chosen Bengali: পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত সংজ্ঞা
- Rationale: The checked formula, proof and function pages support পুনরাবৃত্ত সংজ্ঞা as a definition referring to an earlier value of the same function. পুনরাবৃত্ত অপেক্ষক is reserved for the computational function class in this chapter; it does not by itself assert totality or effective computation beyond the stated construction.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-recursive-function-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত সংজ্ঞা’ express the OpenLogic sense(s) ‘recursive function; recursive definition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 108 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:15`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:18-28` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:24`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:32`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:45-52` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:45`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:132`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T152

- Source term or concept: computability theory
- Chosen Bengali: গণনসাধ্যতা তত্ত্ব
- Rationale: Number, function, relation and proof pages support the Bengali গণনসাধ্য root already used for computable structures and functions. গণনসাধ্যতা তত্ত্ব names the mathematical theory of effective numerical computation and remains distinct from mere enumeration/countability.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computability-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্যতা তত্ত্ব’ express the OpenLogic sense(s) ‘computability theory’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0228` `upstream/content/computability/computability-theory/computability-theory.tex:8-8` → `bn-Beng-IN/content/computability/computability-theory/computability-theory.tex:8`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:12`; final reader page pending
  - `OLP-0208` `upstream/content/computability/computability.tex:9-14` → `bn-Beng-IN/content/computability/computability.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olchapter{cmp}{thy}{Computability Theory}
```

### BN-IN-T153

- Source term or concept: characteristic function; computable relation
- Chosen Bengali: চরিত্রসূচক অপেক্ষক; গণনসাধ্য সম্বন্ধ
- Rationale: Relation, mapping and proof pages support the function-versus-relation distinction. চরিত্রসূচক অপেক্ষক maps membership to a numerical answer, so computable sets and relations can be treated as computable functions; গণনসাধ্য সম্বন্ধ retains the established relation term. Expert review remains welcome for the compound.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-characteristic-function-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চরিত্রসূচক অপেক্ষক; গণনসাধ্য সম্বন্ধ’ express the OpenLogic sense(s) ‘characteristic function; computable relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:25`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:28-32` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:30`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:35`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:68`; final reader page pending
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:28-42` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:39`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
```

### BN-IN-T154

- Source term or concept: unbounded search
- Chosen Bengali: সীমাহীন অনুসন্ধান
- Rationale: The checked number, function and proof pages support অনুসন্ধান as a search operation, while সীমাহীন marks the absence of a fixed upper bound in the source definition. The term is kept distinct from bounded minimization, which is a later section.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-unbounded-search-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সীমাহীন অনুসন্ধান’ express the OpenLogic sense(s) ‘unbounded search’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:12-18` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:16`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:12-18` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:17`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:20-27` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:24`; final reader page pending
  - `OLP-0225` `upstream/content/computability/recursive-functions/normal-form.tex:36-45` → `bn-Beng-IN/content/computability/recursive-functions/normal-form.tex:36`; final reader page pending
  - `OLP-0224` `upstream/content/computability/recursive-functions/partial-functions.tex:64-73` → `bn-Beng-IN/content/computability/recursive-functions/partial-functions.tex:58`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
There is another way to obtain a set of total functions. Say a total
function $f(x,\vec z)$ is \emph{regular} if for every sequence of
natural numbers $\vec z$, there is an $x$ such that $f(x,\vec z) = 0$.
In other words, the regular functions are exactly those functions to
which one can apply unbounded search, and end up with a total
function. One can, conservatively, restrict unbounded search to
regular functions:
```

### BN-IN-T155

- Source term or concept: partial recursive function; general recursive function
- Chosen Bengali: আংশিক পুনরাবৃত্ত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক
- Rationale: The established partial/total distinction under T039 and the new recursive-function register govern these class names. আংশিক পুনরাবৃত্ত অপেক্ষক permits nontermination or undefined values; সাধারণ পুনরাবৃত্ত অপেক্ষক is the total computable subclass identified in the introduction. Both compounds remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-recursive-function-class-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক পুনরাবৃত্ত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক’ express the OpenLogic sense(s) ‘partial recursive function; general recursive function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 29 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:29-39` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:35`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:50-66` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:49`; final reader page pending
  - `OLP-0231` `upstream/content/computability/computability-theory/normal-form.tex:70-74` → `bn-Beng-IN/content/computability/computability-theory/normal-form.tex:65`; final reader page pending
  - `OLP-0231` `upstream/content/computability/computability-theory/normal-form.tex:70-74` → `bn-Beng-IN/content/computability/computability-theory/normal-form.tex:68`; final reader page pending
  - `OLP-0233` `upstream/content/computability/computability-theory/universal-part-function.tex:28-40` → `bn-Beng-IN/content/computability/computability-theory/universal-part-function.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
One can explore the theory of computability without having to refer to
a specific model of computation. To do this, one shows that there is a
universal partial computable function~$\fn{Un}(k, x)$. This allows us
to enumerate the partial computable functions. We will adopt the
notation~$\cfind{k}$ to denote the $k$-th unary partial computable
function, defined by $\cfind{k}(x) \simeq \fn{Un}(k, x)$. (Kleene used
$\{ k \}$ for this purpose, but this notation has not been used as
much recently.)  Slightly more generally, we can uniformly enumerate
the partial computable functions of arbitrary arities, and we will use
$\cfind{k}[n]$ to denote the $k$-th $n$-ary partial recursive
function.
```

### BN-IN-T156

- Source term or concept: arity; n-place function
- Chosen Bengali: স্থানসংখ্যা; n-স্থানীয় অপেক্ষক
- Rationale: The relation, function and proof pages support the number-of-arguments sense. স্থানসংখ্যা names arity without suggesting spatial location; n-স্থানীয় অপেক্ষক marks the corresponding n-argument function. The notation remains governed by each displayed composition or recursion schema.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-arity-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্থানসংখ্যা; n-স্থানীয় অপেক্ষক’ express the OpenLogic sense(s) ‘arity; n-place function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:29-39` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:34`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:68`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:69`; final reader page pending
  - `OLP-0212` `upstream/content/computability/recursive-functions/composition.tex:67-88` → `bn-Beng-IN/content/computability/recursive-functions/composition.tex:70`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:20-27` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
One can explore the theory of computability without having to refer to
a specific model of computation. To do this, one shows that there is a
universal partial computable function~$\fn{Un}(k, x)$. This allows us
to enumerate the partial computable functions. We will adopt the
notation~$\cfind{k}$ to denote the $k$-th unary partial computable
function, defined by $\cfind{k}(x) \simeq \fn{Un}(k, x)$. (Kleene used
$\{ k \}$ for this purpose, but this notation has not been used as
much recently.)  Slightly more generally, we can uniformly enumerate
the partial computable functions of arbitrary arities, and we will use
$\cfind{k}[n]$ to denote the $k$-th $n$-ary partial recursive
function.
```

### BN-IN-T157

- Source term or concept: primitive recursive notation; composition notation; recursion notation
- Chosen Bengali: আদিম পুনরাবৃত্ত সংকেতলিপি; মিশ্রণ-সংকেতলিপি; পুনরাবৃত্তি-সংকেতলিপি
- Rationale: The checked number, logic and function pages support symbol-governed mathematical exposition, while the Comp and Rec codes are defined by the OpenLogic section itself. সংকেতলিপি names a finite syntactic code for a construction, not the function value or an informal abbreviation. The compound remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-recursive-notation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আদিম পুনরাবৃত্ত সংকেতলিপি; মিশ্রণ-সংকেতলিপি; পুনরাবৃত্তি-সংকেতলিপি’ express the OpenLogic sense(s) ‘primitive recursive notation; composition notation; recursion notation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0214` `upstream/content/computability/recursive-functions/notation-pr-functions.tex:47-49` → `bn-Beng-IN/content/computability/recursive-functions/notation-pr-functions.tex:48`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
  Give the complete primitive recursive notation for~$\Mult$.
\end{prob}
```

### BN-IN-T158

- Source term or concept: exponentiation function; factorial function; truncated subtraction
- Chosen Bengali: ঘাতের অপেক্ষক; ক্রমগুণিতক অপেক্ষক; ছাঁটা বিয়োগ
- Rationale: The university number and function witnesses support numerical-function prose, and each exact operation is fixed by its displayed equations. ঘাতের অপেক্ষক raises the first argument to the second; ক্রমগুণিতক অপেক্ষক multiplies the initial finite segment; ছাঁটা বিয়োগ returns zero rather than a negative value. These compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-arithmetic-function-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ঘাতের অপেক্ষক; ক্রমগুণিতক অপেক্ষক; ছাঁটা বিয়োগ’ express the OpenLogic sense(s) ‘exponentiation function; factorial function; truncated subtraction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:25-27` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:25`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:78-81` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:77`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:99-108` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:98`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  The exponentiation function $\fn{exp}(x, y) = x^y$ is primitive recursive.
\end{prop}
```

### BN-IN-T159

- Source term or concept: finite sum; finite product; integer division
- Chosen Bengali: সসীম যোগফল; সসীম গুণফল; পূর্ণসংখ্যা ভাগ
- Rationale: The checked number and function pages support the arithmetic roots; the source bounds and floor formula determine the exact operations. সসীম যোগফল and সসীম গুণফল are iterated through the stated bound, while পূর্ণসংখ্যা ভাগ discards the fractional remainder. Expert review remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-finite-arithmetic-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সসীম যোগফল; সসীম গুণফল; পূর্ণসংখ্যা ভাগ’ express the OpenLogic sense(s) ‘finite sum; finite product; integer division’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:162-168` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:163`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:172`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:170-185` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:177`; final reader page pending
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:187-193` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:186`; final reader page pending
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:101-119` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:107`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prob}
Show that integer division $d(x, y) = \lfloor x/y \rfloor$ (i.e.,
division, where you disregard everything after the decimal point) is
primitive recursive. When $y = 0$, we stipulate $d(x, y) = 0$. Give an
explicit definition of~$d$ using primitive recursion and
composition.
\end{prob}
```

### BN-IN-T160

- Source term or concept: primitive recursive relation; Boolean operation
- Chosen Bengali: আদিম পুনরাবৃত্ত সম্বন্ধ; বুলীয় ক্রিয়া
- Rationale: The relation witness directly supports সম্পর্ক while the edition consistently uses সম্বন্ধ for OpenLogic's formal relation register; the logic witness supplies connective usage. The characteristic-function definition governs আদিম পুনরাবৃত্ত সম্বন্ধ, and বুলীয় ক্রিয়া covers negation, conjunction, disjunction and implication without altering their formal macros.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-primitive-relation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আদিম পুনরাবৃত্ত সম্বন্ধ; বুলীয় ক্রিয়া’ express the OpenLogic sense(s) ‘primitive recursive relation; Boolean operation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 12 occurrence(s). Representative locations:
  - `OLP-0231` `upstream/content/computability/computability-theory/normal-form.tex:27-36` → `bn-Beng-IN/content/computability/computability-theory/normal-form.tex:27`; final reader page pending
  - `OLP-0218` `upstream/content/computability/recursive-functions/bounded-minimization.tex:12-25` → `bn-Beng-IN/content/computability/recursive-functions/bounded-minimization.tex:20`; final reader page pending
  - `OLP-0210` `upstream/content/computability/recursive-functions/introduction.tex:30-39` → `bn-Beng-IN/content/computability/recursive-functions/introduction.tex:33`; final reader page pending
  - `OLP-0225` `upstream/content/computability/recursive-functions/normal-form.tex:12-21` → `bn-Beng-IN/content/computability/recursive-functions/normal-form.tex:14`; final reader page pending
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:9-10` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}[Kleene's Normal Form Theorem]
\ollabel{thm:normal-form}
There is a primitive recursive relation~$T(e, x, s)$ and a primitive
recursive function~$U(s)$, with the following property: if $f$ is any
partial computable function, then for some~$e$,
\[
f(x) \simeq U(\umin{s}{T(e, x, s)})
\]
for every~$x$.
\end{thm}
```

### BN-IN-T161

- Source term or concept: bounded quantification; bounded universal quantifier; bounded existential quantifier
- Chosen Bengali: সীমাবদ্ধ পরিমাণায়ন; সীমাবদ্ধ সর্বজনীন পরিমাণসূচক; সীমাবদ্ধ অস্তিত্বমূলক পরিমাণসূচক
- Rationale: The university philosophy pages directly support universal and existential quantification and scope; সীমাবদ্ধ records the explicit numerical bound supplied by the source formulas. The finite-product/minimum and finite-maximum constructions govern the computational meaning. The full compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-bounded-quantification-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সীমাবদ্ধ পরিমাণায়ন; সীমাবদ্ধ সর্বজনীন পরিমাণসূচক; সীমাবদ্ধ অস্তিত্বমূলক পরিমাণসূচক’ express the OpenLogic sense(s) ‘bounded quantification; bounded universal quantifier; bounded existential quantifier’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:88-99` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:90`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{prop}
  The set of primitive recursive relations is closed under bounded
  quantification, i.e., if $R(\vec x, z)$ is a primitive recursive
  relation, then so are the relations
  \begin{align*}
    & \bforall{z < y}{R(\vec x, z)} \text{ and}\\
    & \bexists{z < y}{R(\vec x, z)}.
  \end{align*}
  $\bforall{z < y}{R(\vec x, z)}$ holds of $\vec x$ and $y$ if and
  only if $R(\vec x, z)$ holds for every~$z$ less than~$y$, and
  similarly for $\bexists{z < y}{R(\vec x, z)}$.
\end{prop}
```

### BN-IN-T162

- Source term or concept: conditional function; definition by cases
- Chosen Bengali: শর্তাধীন অপেক্ষক; ক্ষেত্রভেদে সংজ্ঞা
- Rationale: Logic and function witnesses support condition and function prose, while the displayed zero/nonzero cases fix the operator. শর্তাধীন অপেক্ষক selects one of two values from its first argument; ক্ষেত্রভেদে সংজ্ঞা names the finite cascade built from it and characteristic functions. Expert review remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-conditional-function-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘শর্তাধীন অপেক্ষক; ক্ষেত্রভেদে সংজ্ঞা’ express the OpenLogic sense(s) ‘conditional function; definition by cases’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0217` `upstream/content/computability/recursive-functions/pr-relations.tex:126-138` → `bn-Beng-IN/content/computability/recursive-functions/pr-relations.tex:130`; final reader page pending
  - `OLP-0038` `upstream/content/sets-functions-relations/size-of-sets/enumerability-alt.tex:99-124` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/enumerability-alt.tex:76`; final reader page pending
  - `OLP-0029` `upstream/content/sets-functions-relations/size-of-sets/enumerability.tex:140-162` → `bn-Beng-IN/content/sets-functions-relations/size-of-sets/enumerability.tex:93`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Another useful primitive recursive function is the conditional
function, $\fn{cond}(x,y,z)$, defined by
\begin{align*}
  \fn{cond}(x,y,z) & = \begin{cases}
  y & \text{if $x = 0$} \\
  z & \text{otherwise}.
\end{cases}
\intertext{This is defined recursively by}
\fn{cond}(0,y,z) & = y,\\
\fn{cond}(x+1,y,z) & = z.
\end{align*}
One can use this to justify definitions of primitive recursive functions
by cases from primitive recursive relations:
```

### BN-IN-T163

- Source term or concept: bounded minimization; least-number search
- Chosen Bengali: সীমাবদ্ধ ন্যূনীকরণ; ক্ষুদ্রতম-সংখ্যা অনুসন্ধান
- Rationale: The checked order, number, relation and function witnesses support the component roots, and the source proposition fixes the bounded search exactly. সীমাবদ্ধ ন্যূনীকরণ returns the least witness below the given bound and the bound itself when none exists; it remains distinct from T154's সীমাহীন অনুসন্ধান.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-bounded-minimization-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সীমাবদ্ধ ন্যূনীকরণ; ক্ষুদ্রতম-সংখ্যা অনুসন্ধান’ express the OpenLogic sense(s) ‘bounded minimization; least-number search’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0218` `upstream/content/computability/recursive-functions/bounded-minimization.tex:9-10` → `bn-Beng-IN/content/computability/recursive-functions/bounded-minimization.tex:10`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:12`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:46-62` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:57`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:76-78` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:80`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:48-72` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:67`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{rec}{bmi}
\olsection{Bounded Minimization}
```

### BN-IN-T164

- Source term or concept: divides/divisibility; remainder; prime number; next prime
- Chosen Bengali: নিঃশেষে ভাগ করা/বিভাজ্যতা; ভাগশেষ; মৌলিক সংখ্যা; পরবর্তী মৌলিক সংখ্যা
- Rationale: The checked number, relation and function pages support the arithmetic prose, while the displayed bounded formulas govern the exact senses. নিঃশেষে ভাগ করা fixes the direction of x dividing y, ভাগশেষ names the remainder, and মৌলিক সংখ্যা is restricted by the displayed divisor condition. The compound for the next-prime function remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-prime-arithmetic-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিঃশেষে ভাগ করা/বিভাজ্যতা; ভাগশেষ; মৌলিক সংখ্যা; পরবর্তী মৌলিক সংখ্যা’ express the OpenLogic sense(s) ‘divides/divisibility; remainder; prime number; next prime’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 28 occurrence(s). Representative locations:
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:45`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:50-55` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:49`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:9-10` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:10`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:16`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:18`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For a concrete example, the ``greatest common divisor'' function
$\fn{gcd}(u,v)$ can be defined by
\[
\fn{gcd}(u,v) \simeq
\begin{cases}
v & \text{if $u = 0$} \\
\fn{gcd}(\fn{mod}(v, u), u) & \text{otherwise}
\end{cases}
\]
where $\fn{mod}(v, u)$ denotes the remainder of dividing $v$
by~$u$. An appeal to the fixed-point lemma shows that $\fn{gcd}$ is
partial computable. (In fact, this can be put in the format above,
letting $y$ code the pair $\tuple{u, v}$.) A subsequent induction
on~$u$ then shows that, in fact, $\fn{gcd}$ is total.
```

### BN-IN-T165

- Source term or concept: sequence code; empty sequence; sequence concatenation; subsequence
- Chosen Bengali: অনুক্রমের সংকেত; শূন্য অনুক্রম; অনুক্রমের সংযুক্তি; উপ-অনুক্রম
- Rationale: T019 and T043 already establish অনুক্রম and সংকেতায়ন, and the checked function pages support the operations. The prime-power equations define অনুক্রমের সংকেত, শূন্য অনুক্রম denotes the length-zero case, সংযুক্তি preserves order, and উপ-অনুক্রম preserves a contiguous requested portion.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computable-sequence-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অনুক্রমের সংকেত; শূন্য অনুক্রম; অনুক্রমের সংযুক্তি; উপ-অনুক্রম’ express the OpenLogic sense(s) ‘sequence code; empty sequence; sequence concatenation; subsequence’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0231` `upstream/content/computability/computability-theory/normal-form.tex:56-62` → `bn-Beng-IN/content/computability/computability-theory/normal-form.tex:54`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:12-25` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:23`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:38-41` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:38`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:48-72` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:51`; final reader page pending
  - `OLP-0220` `upstream/content/computability/recursive-functions/sequences.tex:187-192` → `bn-Beng-IN/content/computability/recursive-functions/sequences.tex:185`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
In order to give a rigorous proof of the Normal Form Theorem, we would
have to fix a model of computation and carry out the coding of
descriptions of computable functions and of computation sequences in
detail, and verify that the relation~$T$ and function~$U$ are
primitive recursive.  For most applications, it suffices that $T$
and~$U$ are computable and that $U$~is total.
```

### BN-IN-T166

- Source term or concept: tree; node; root; immediate subtree; leaf node
- Chosen Bengali: বৃক্ষ; নোড; মূল; অব্যবহিত উপবৃক্ষ; পত্র-নোড
- Rationale: T031 already attests বৃক্ষ and মূল for the mathematical tree register. The recursive sequence code in the source fixes নোড and অব্যবহিত উপবৃক্ষ, while পত্র-নোড names an endpoint when measuring depth. The added compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-coded-tree-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বৃক্ষ; নোড; মূল; অব্যবহিত উপবৃক্ষ; পত্র-নোড’ express the OpenLogic sense(s) ‘tree; node; root; immediate subtree; leaf node’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 295 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:62`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:63`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:123`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:151-179` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:159`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T167

- Source term or concept: simultaneous recursion; course-of-values recursion; side value/parameter
- Chosen Bengali: যুগপৎ পুনরাবৃত্তি; পূর্বমান-ভিত্তিক পুনরাবৃত্তি; পার্শ্ব-মান/পরামিতি
- Rationale: The displayed schemes govern these specialized constructions. যুগপৎ marks functions advanced together, and পূর্বমান-ভিত্তিক states directly that the entire earlier value sequence may be consulted. পরামিতি continues the mathematical register, with পার্শ্ব-মান retained as the source's explanatory gloss.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-extended-recursion-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যুগপৎ পুনরাবৃত্তি; পূর্বমান-ভিত্তিক পুনরাবৃত্তি; পার্শ্ব-মান/পরামিতি’ express the OpenLogic sense(s) ‘simultaneous recursion; course-of-values recursion; side value/parameter’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:12-47` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:21`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:12-47` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:36`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:50-55` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:49`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:57-66` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:58`; final reader page pending
  - `OLP-0052` `upstream/content/sets-functions-relations/infinite/dedekind-induction.tex:37-44` → `bn-Beng-IN/content/sets-functions-relations/infinite/dedekind-induction.tex:33`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Using pairing and sequencing, we can justify more exotic (and
useful) forms of primitive recursion. For example, it is often useful
to define two functions simultaneously, such as in the following
definition:
\begin{align*}
h_0(\vec x, 0) & = f_0(\vec x) \\
h_1(\vec x, 0) & = f_1(\vec x) \\
h_0(\vec x, y+1) & = g_0(\vec x, y, h_0(\vec x, y), h_1(\vec x, y)) \\
h_1(\vec x, y+1) & = g_1(\vec x, y, h_0(\vec x, y), h_1(\vec x, y))
\end{align*}
This is an instance of \emph{simultaneous recursion}. Another useful
way of defining functions is to give the value of $h(\vec x, y+1)$ in
terms of \emph{all} the values $h(\vec x, 0)$, \dots,~$h(\vec x, y)$, as in
the following definition:
\begin{align*}
h(\vec x, 0) & = f(\vec x) \\
h(\vec x, y+1) & = g(\vec x, y, \tuple{h(\vec x, 0), \dots, h(\vec x, y)}).
\end{align*}
The following schema captures this idea more succinctly:
\[
h(\vec x, y) = g(\vec x, y, \tuple{h(\vec x, 0), \dots, h(\vec x, y-1)})
\]
with the understanding that the last argument to $g$ is just the
empty sequence when $y$ is $0$. In either formulation, the idea is
that in computing the ``successor step,'' the function $h$ can make
use of the entire sequence of values computed so far.
This is known as a \emph{course-of-values} recursion. For a particular
example, it can be used to justify the following type of definition:
\begin{align*}
h(\vec x, y) & = \begin{cases}
  g(\vec x, y, h(\vec x, k(\vec x, y))) & \text{if $k(\vec x, y) < y$} \\
  f(\vec x) & \text{otherwise}
\end{cases}
\end{align*}
In other words, the value of $h$ at $y$ can be computed in terms of
the value of $h$ at \emph{any} previous value, given by~$k$.
```

### BN-IN-T168

- Source term or concept: non-primitive-recursive function; effective enumeration; diagonalization
- Chosen Bengali: আদিম পুনরাবৃত্ত নয় এমন অপেক্ষক; কার্যকর তালিকায়ন; কর্ণীকরণ
- Rationale: T044 already supports কর্ণীকরণ and T040 supports তালিকায়ন. The diagonal equations fix the effective meaning: the enumeration can be evaluated algorithmically, while the diagonal function differs from each listed primitive recursive function at its own index.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-diagonal-computability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আদিম পুনরাবৃত্ত নয় এমন অপেক্ষক; কার্যকর তালিকায়ন; কর্ণীকরণ’ express the OpenLogic sense(s) ‘non-primitive-recursive function; effective enumeration; diagonalization’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:24-33` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:27`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:38`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:41`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:43-49` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:45`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:37-48` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:38`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
The proof is a simple diagonalization: if $\fn{Un}'(k,x)$ were total
and computable, then
\[
d(x) = \fn{Un}'(x, x) + 1
\]
would also be total and computable. However, by definition, $d(k)$ is
not equal to $\fn{Un}'(k,k)$. Hence, for every $k$, the values of
$d(x)$ and~$\fn{Un}'(k, x)$ differ for at least one~$x$, namely $x = k$.
\end{proof}
```

### BN-IN-T169

- Source term or concept: Ackermann--Péter function; fast-growing function
- Chosen Bengali: আকারমান--পেতের অপেক্ষক; দ্রুত-বর্ধনশীল অপেক্ষক
- Rationale: The proper name is transliterated in Bengali script and the governing iteration equations determine the growth claim. দ্রুত-বর্ধনশীল অপেক্ষক describes the hierarchy without adding a complexity classification absent from the source. Expert review of the name spelling is welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-fast-growth-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আকারমান--পেতের অপেক্ষক; দ্রুত-বর্ধনশীল অপেক্ষক’ express the OpenLogic sense(s) ‘Ackermann--Péter function; fast-growing function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0223` `upstream/content/computability/recursive-functions/non-pr-functions.tex:30-43` → `bn-Beng-IN/content/computability/recursive-functions/non-pr-functions.tex:41`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
One can provide more explicit examples of computable functions that
are not primitive recursive. For example, let the notation $g^n(x)$
denote $g(g(\dots g(x)))$, with $n$ $g$'s in all; and define a
sequence $g_0,g_1,\dots$ of functions by
\begin{eqnarray*}
g_0(x) & = & x+1 \\
g_{n + 1}(x) & = & g_n^x(x)
\end{eqnarray*}
You can confirm that each function $g_n$ is primitive recursive. Each
successive function grows much faster than the one before; $g_1(x)$ is
equal to $2x$, $g_2(x)$ is equal to $2^x \cdot x$, and $g_3(x)$ grows
roughly like an exponential stack of $x$ $2$'s. The Ackermann--P\'eter
function is essentially the function $G(x) = g_x(x)$, and one can show
that this grows faster than any primitive recursive function.
```

### BN-IN-T170

- Source term or concept: Church--Turing thesis; Turing machine; computational model; simulation
- Chosen Bengali: চার্চ--টুরিং থিসিস; টুরিং যন্ত্র; গণনামূলক মডেল; অনুকরণ
- Rationale: The checked logic and function pages support the explanatory register, while the source passage fixes the relation among intuitive computability, machines and simulation. থিসিস is retained as the familiar name of the claim; টুরিং যন্ত্র and গণনামূলক মডেল remain provisional India-standard compounds.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computation-model-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চার্চ--টুরিং থিসিস; টুরিং যন্ত্র; গণনামূলক মডেল; অনুকরণ’ express the OpenLogic sense(s) ‘Church--Turing thesis; Turing machine; computational model; simulation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 220 occurrence(s). Representative locations:
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:78-91` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:76`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:15`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:19`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:32-40` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:34`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:32-40` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:36`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Expressing $A \cup B$ as a set of halting values is more difficult,
because one has to simulate $m$ and $n$ in parallel. Let $d$ be an
index for $m$ and let $e$ be an index for $n$; in other words, $m =
\cfind{d}$ and $n = \cfind{e}$. Then $A \cup B$ is the domain of the
function
\[
p(x) = \umin{y}{(T(d,x,y) \lor T(e,x,y))}.
\]
\begin{explain}
In computational terms, on input $x$, $p$ searches for either a
halting computation for $m$ or a halting computation for $n$, and
halts if it finds either one.
\end{explain}
\end{proof}
```

### BN-IN-T171

- Source term or concept: partial function defined/undefined; equality up to simultaneous definedness
- Chosen Bengali: আংশিক অপেক্ষক সংজ্ঞায়িত/অসংজ্ঞায়িত; যুগপৎ সংজ্ঞায়িততার সাপেক্ষে সমতা
- Rationale: The checked number, logic, relation and function pages support the component vocabulary, while the source clauses fix the technical meanings of \fdefined, \fundefined and \simeq. সংজ্ঞায়িত and অসংজ্ঞায়িত track membership in the domain; the equality phrase records that both terms must either be undefined together or defined with equal values. The compound remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-partial-definedness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক অপেক্ষক সংজ্ঞায়িত/অসংজ্ঞায়িত; যুগপৎ সংজ্ঞায়িততার সাপেক্ষে সমতা’ express the OpenLogic sense(s) ‘partial function defined/undefined; equality up to simultaneous definedness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 48 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:43`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:52`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:61`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:62-68` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:66`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:45-52` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:48`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
Let $f$ be any computable function; we will construct an $e$
such that $W_e$ is computable, but $\cfind{f(e)}$ is not its
characteristic function. Using the fixed point theorem, we can find an
index $e$ such that
\[
\cfind{e}(y) \simeq
\begin{cases}
0 & \text{if $y=0$ and $\cfind{f(e)}(0) \fdefined = 0$} \\
\text{undefined} & \text{otherwise.}
\end{cases}
\]
That is, $e$ is obtained by applying the fixed-point theorem to the
function defined by
\[
g(x,y) \simeq
\begin{cases}
0 & \text{if $y=0$ and $\cfind{f(x)}(0) \fdefined = 0$} \\
\text{undefined} & \text{otherwise.}
\end{cases}
\]
Informally, we can see that $g$ is partial computable, as follows: on
input $x$ and $y$, the algorithm first checks to see if $y$ is equal
to~$0$. If it is, the algorithm computes $f(x)$, and then uses the
universal machine to compute $\cfind{f(x)}(0)$. If this last computation
halts and returns~$0$, the algorithm returns~$0$; otherwise, the
algorithm doesn't halt.
```

### BN-IN-T172

- Source term or concept: unbounded search operator; partial recursive function; recursive/total recursive function
- Chosen Bengali: সীমাহীন অনুসন্ধান অপারেটর; আংশিক পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত/সর্বত্র-সংজ্ঞায়িত পুনরাবৃত্ত অপেক্ষক
- Rationale: T154 and T155 establish the search and recursion roots, and the displayed minimization clause determines their extension to partial functions. সীমাহীন অনুসন্ধান requires every preceding computation to be defined before the first zero; আংশিক পুনরাবৃত্ত অপেক্ষক is the closure class, and পুনরাবৃত্ত or সর্বত্র-সংজ্ঞায়িত পুনরাবৃত্ত identifies its total members.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-partial-recursion-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সীমাহীন অনুসন্ধান অপারেটর; আংশিক পুনরাবৃত্ত অপেক্ষক; পুনরাবৃত্ত/সর্বত্র-সংজ্ঞায়িত পুনরাবৃত্ত অপেক্ষক’ express the OpenLogic sense(s) ‘unbounded search operator; partial recursive function; recursive/total recursive function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 281 occurrence(s). Representative locations:
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:17-22` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:18`; final reader page pending
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:24-38` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:32`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:15`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:35`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:18-28` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:24`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{history}
Computably enumerable sets are also called \emph{recursively
  enumerable} instead. This is the original terminology, and today
both are commonly used, as well as the abbreviations ``c.e.'' and
``r.e.''
\end{history}
```

### BN-IN-T173

- Source term or concept: Kleene's normal form theorem; index; computation code
- Chosen Bengali: ক্লিনির স্বাভাবিক রূপের উপপাদ্য; সূচক; গণনার সংকেত
- Rationale: The proper name is transliterated in Bengali script, while the theorem's T/U equation governs সূচক and গণনার সংকেত. An index names a partial-recursive procedure; a computation code records a finite computation that T can check and U can decode. Expert review of the name spelling remains welcome.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-normal-form-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ক্লিনির স্বাভাবিক রূপের উপপাদ্য; সূচক; গণনার সংকেত’ express the OpenLogic sense(s) ‘Kleene's normal form theorem; index; computation code’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 226 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:13`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:25`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:28-32` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:30`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:35`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T174

- Source term or concept: halting problem; halting function; nontermination
- Chosen Bengali: থামার সমস্যা; থামা-অপেক্ষক; গণনা না-থামা
- Rationale: The checked logic, function and proof pages support the explanatory register, and the two displayed case definitions fix the decision problem and its characteristic function. থামা denotes production of a result; গণনা না-থামা denotes undefined computation without adding a time-bound sense. The compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-halting-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘থামার সমস্যা; থামা-অপেক্ষক; গণনা না-থামা’ express the OpenLogic sense(s) ‘halting problem; halting function; nontermination’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 30 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:12`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:115`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:10`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Let's consider the halting problem again. As temporary
notation, let us write $\gn{\cfind{x}(y)}$ for $\tuple{x, y}$; think of
this as representing a ``name'' for the value $\cfind{x}(y)$. With this
notation, we can reword one of our proofs that the halting problem is
undecidable.
```

### BN-IN-T175

- Source term or concept: regular function; general recursive function; conservative restriction
- Chosen Bengali: নিয়মিত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক; রক্ষণশীল সীমাবদ্ধকরণ
- Rationale: The displayed totality condition fixes নিয়মিত অপেক্ষক as a total function whose unbounded search always succeeds. সাধারণ পুনরাবৃত্ত অপেক্ষক retains the historical name for closure under search restricted to regular functions, and রক্ষণশীল সীমাবদ্ধকরণ records that this restriction yields the same total class as recursive functions. The specialized register remains open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-general-recursion-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নিয়মিত অপেক্ষক; সাধারণ পুনরাবৃত্ত অপেক্ষক; রক্ষণশীল সীমাবদ্ধকরণ’ express the OpenLogic sense(s) ‘regular function; general recursive function; conservative restriction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 8 occurrence(s). Representative locations:
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:9-10` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:10`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:12-18` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:15`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:12-18` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:18`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:20-27` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:25`; final reader page pending
  - `OLP-0227` `upstream/content/computability/recursive-functions/general-recursive-functions.tex:29-39` → `bn-Beng-IN/content/computability/recursive-functions/general-recursive-functions.tex:28`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{rec}{gen}
\olsection{General Recursive Functions}
```

### BN-IN-T176

- Source term or concept: computability theory; relative computability; recursion theory
- Chosen Bengali: গণনসাধ্যতা তত্ত্ব; আপেক্ষিক গণনসাধ্যতা; পুনরাবৃত্তি তত্ত্ব
- Rationale: The checked logic and function pages support the component register, while the chapter introduction fixes the three field names and explicitly relates the historical alternative. গণনসাধ্যতা তত্ত্ব names the modern subject, আপেক্ষিক গণনসাধ্যতা preserves the comparison parameter, and পুনরাবৃত্তি তত্ত্ব is retained as the historically common synonym.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computability-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্যতা তত্ত্ব; আপেক্ষিক গণনসাধ্যতা; পুনরাবৃত্তি তত্ত্ব’ express the OpenLogic sense(s) ‘computability theory; relative computability; recursion theory’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0228` `upstream/content/computability/computability-theory/computability-theory.tex:8-8` → `bn-Beng-IN/content/computability/computability-theory/computability-theory.tex:8`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:12`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:13`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:15`; final reader page pending
  - `OLP-0208` `upstream/content/computability/computability.tex:9-14` → `bn-Beng-IN/content/computability/computability.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olchapter{cmp}{thy}{Computability Theory}
```

### BN-IN-T177

- Source term or concept: partial computable function; computable total function; computable relation
- Chosen Bengali: আংশিক গণনসাধ্য অপেক্ষক; গণনসাধ্য সর্বত্র-সংজ্ঞায়িত অপেক্ষক; গণনসাধ্য সম্বন্ধ
- Rationale: T039, T150 and T171 supply the function, computability and definedness roots. The source introduction governs the distinctions: আংশিক গণনসাধ্য permits undefined inputs, the unqualified গণনসাধ্য function is total, and a গণনসাধ্য সম্বন্ধ has a computable characteristic function. The compounds remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computability-class-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘আংশিক গণনসাধ্য অপেক্ষক; গণনসাধ্য সর্বত্র-সংজ্ঞায়িত অপেক্ষক; গণনসাধ্য সম্বন্ধ’ express the OpenLogic sense(s) ‘partial computable function; computable total function; computable relation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 35 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:28-32` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:29`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:34`; final reader page pending
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:28-42` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:39`; final reader page pending
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:12-32` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:14`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The fixed-point theorem essentially lets us define partial computable
functions in terms of their indices. For example, we can find an
index $e$ such that for every $y$,
\[
\cfind{e}(y) = e + y.
\]
As another example, one can use the proof of the fixed-point theorem
to design a program in Java or C++ that prints itself out.
```

### BN-IN-T178

- Source term or concept: computation record; computation sequence; output
- Chosen Bengali: গণনার নথি; গণনা-অনুক্রম; নির্গম
- Rationale: The checked sequence and function witnesses support the component words, and the coding section supplies their technical roles. গণনার নথি is the complete trace, গণনা-অনুক্রম stresses its ordered steps, and নির্গম is the value extracted from its final state. The T/U clauses determine these meanings independently of a machine model.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-computation-coding-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনার নথি; গণনা-অনুক্রম; নির্গম’ express the OpenLogic sense(s) ‘computation record; computation sequence; output’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 63 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:22`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:33`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:33-40` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:34`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:32-40` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:35`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:54-72` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:71`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T179

- Source term or concept: program specialization; fixed inputs; remaining arguments
- Chosen Bengali: প্রোগ্রামের বিশেষায়ন; আগে থেকে স্থির নিবেশ; অবশিষ্ট আর্গুমেন্ট
- Rationale: The s-m-n equation is controlling evidence: the first m arguments are fixed in advance and a program for the n remaining arguments is returned effectively. আগে থেকে স্থির নিবেশ and অবশিষ্ট আর্গুমেন্ট state those two roles directly; প্রোগ্রামের বিশেষায়ন names the operation without changing the theorem’s symbolic title.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-s-m-n-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রোগ্রামের বিশেষায়ন; আগে থেকে স্থির নিবেশ; অবশিষ্ট আর্গুমেন্ট’ express the OpenLogic sense(s) ‘program specialization; fixed inputs; remaining arguments’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0232` `upstream/content/computability/computability-theory/s-m-n.tex:30-41` → `bn-Beng-IN/content/computability/computability-theory/s-m-n.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
It is helpful to think of $s^m_n$ as acting on \emph{programs}. That
is, $s^m_n$ takes a program~$e$ for an $(m+n)$-ary function, as well
as fixed inputs $a_0$, \dots, $a_{m-1}$; and it returns a program
$s^m_n(x, a_0, \dots, a_{m-1})$ for the $n$-ary function of the
remaining arguments. \iftag{TMs}{It you think of $x$ as the description of a
Turing machine, then $s^m_n(e, a_0, \dots, a_{m-1})$ is the Turing
machine that, on input $y_0$, \dots,~$y_{n-1}$, prepends
$a_0$, \dots,~$a_{m-1}$ to the input string, and runs~$e$. Each $s^m_n$
is then just a primitive recursive function that finds a code for the
appropriate Turing machine.}{}
\end{explain}
```

### BN-IN-T180

- Source term or concept: universal partial computable function; effective enumeration; uniform computation
- Chosen Bengali: সার্বজনীন আংশিক গণনসাধ্য অপেক্ষক; কার্যকর তালিকায়ন; একই নিয়মে গণনা
- Rationale: The universal-function theorem and its normal-form definition govern this register. সার্বজনীন means that every unary partial computable function appears at some index; কার্যকর তালিকায়ন records the indexed sequence, and একই নিয়মে গণনা records that the evaluator is computable jointly from the index and input. The specialized compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-universal-function-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সার্বজনীন আংশিক গণনসাধ্য অপেক্ষক; কার্যকর তালিকায়ন; একই নিয়মে গণনা’ express the OpenLogic sense(s) ‘universal partial computable function; effective enumeration; uniform computation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 5 occurrence(s). Representative locations:
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:12`; final reader page pending
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:47-62` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:44`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:66-82` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:60`; final reader page pending
  - `OLP-0233` `upstream/content/computability/computability-theory/universal-part-function.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/universal-part-function.tex:10`; final reader page pending
  - `OLP-0233` `upstream/content/computability/computability-theory/universal-part-function.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/universal-part-function.tex:14`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
By construction, the universal partial computable
function~$\fn{Un}(e,x)$ is defined if and only if the computation of
the function coded by~$e$ produces a value for input~$x$. It is
natural to ask if we can decide whether this is the case. In fact, it
is not. For the Turing machine model of computation, this means that
whether a given Turing machine halts on a given input is
computationally undecidable. The following theorem is therefore known
as the ``undecidability of the halting problem.'' We will provide two
proofs below. The first continues the thread of our previous
discussion, while the second is more direct.
```

### BN-IN-T181

- Source term or concept: no universal computable function; diagonal function; partial escape
- Chosen Bengali: সার্বজনীন গণনসাধ্য অপেক্ষকের অনস্তিত্ব; কর্ণ অপেক্ষক; আংশিকতার অবকাশ
- Rationale: The diagonal equation is controlling evidence: adding one makes the total diagonal differ from every row of a putative total computable evaluator. সার্বজনীন গণনসাধ্য অপেক্ষকের অনস্তিত্ব names that conclusion, while আংশিকতার অবকাশ records why the existing universal partial evaluator avoids it. The compounds remain provisional.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-no-total-universal-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সার্বজনীন গণনসাধ্য অপেক্ষকের অনস্তিত্ব; কর্ণ অপেক্ষক; আংশিকতার অবকাশ’ express the OpenLogic sense(s) ‘no universal computable function; diagonal function; partial escape’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T182

- Source term or concept: undecidability of the halting problem; infinite loop; self-input
- Chosen Bengali: থামার সমস্যার অনির্ণেয়তা; অসীম চক্র; স্ব-নিবেশ
- Rationale: T174 supplies the halting terminology and the two diagonal proofs govern the stronger decision claim. থামার সমস্যার অনির্ণেয়তা states that no computable characteristic function decides definedness; অসীম চক্র and স্ব-নিবেশ express the Turing-machine reversal without weakening the biconditional contradiction.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-halting-undecidability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘থামার সমস্যার অনির্ণেয়তা; অসীম চক্র; স্ব-নিবেশ’ express the OpenLogic sense(s) ‘undecidability of the halting problem; infinite loop; self-input’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:84-99` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:93`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:32-34` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:32`; final reader page pending
  - `OLP-0265` `upstream/content/turing-machines/undecidability/introduction.tex:66-83` → `bn-Beng-IN/content/turing-machines/undecidability/introduction.tex:71`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Let's consider the halting problem again. As temporary
notation, let us write $\gn{\cfind{x}(y)}$ for $\tuple{x, y}$; think of
this as representing a ``name'' for the value $\cfind{x}(y)$. With this
notation, we can reword one of our proofs that the halting problem is
undecidable.
```

### BN-IN-T183

- Source term or concept: Russell's paradox; set of all sets; diagonalization argument
- Chosen Bengali: রাসেলের কূটাভাস; সব সেটের সেট; কর্ণীকরণ যুক্তি
- Rationale: The checked set and logic pages support membership and contradiction language, while the three displayed self-application cases determine the comparison. রাসেলের কূটাভাস is reserved for the inconsistent unrestricted set construction; কর্ণীকরণ যুক্তি names the analogous computability proof, whose conclusion is noncomputability rather than paradox.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-russell-comparison-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘রাসেলের কূটাভাস; সব সেটের সেট; কর্ণীকরণ যুক্তি’ express the OpenLogic sense(s) ‘Russell's paradox; set of all sets; diagonalization argument’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 22 occurrence(s). Representative locations:
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:38`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:35-41` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:41`; final reader page pending
  - `OLP-0234` `upstream/content/computability/computability-theory/no-universal-function.tex:43-49` → `bn-Beng-IN/content/computability/computability-theory/no-universal-function.tex:45`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:10`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:12`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
\olref[uni]{thm:univ-comp} above shows that we can get around this
diagonalization argument, but only at the expense of allowing the
universal function to be partial. That is, $\fn{Un}$ is universal for
the total computable functions, it just isn't total. The
diagonalization argument doesn't work in the partial case.
\end{explain}
```

### BN-IN-T184

- Source term or concept: computable set; computable relation; decidable
- Chosen Bengali: গণনসাধ্য সেট; গণনসাধ্য সম্বন্ধ; নির্ণেয়
- Rationale: The characteristic-function display fixes the terminology exactly. A গণনসাধ্য সেট or গণনসাধ্য সম্বন্ধ has a total computable zero-one characteristic function, and নির্ণেয় is its equivalent decision-theoretic name. This remains distinct from semidecidability in T186.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-decidable-set-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্য সেট; গণনসাধ্য সম্বন্ধ; নির্ণেয়’ express the OpenLogic sense(s) ‘computable set; computable relation; decidable’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 44 occurrence(s). Representative locations:
  - `OLP-0238` `upstream/content/computability/computability-theory/ce-sets.tex:40-51` → `bn-Beng-IN/content/computability/computability-theory/ce-sets.tex:37`; final reader page pending
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:28-42` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:39`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:10`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:12-13` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:12`; final reader page pending
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:29-30` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:28`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Any computable set is computably enumerable. To see this, suppose
$S$~is computable. If $S$ is empty, then by definition it is
computably enumerable. Otherwise, let $a$ be any element of
$S$. Define $f$ by
\[
f(x) =
\begin{cases}
x & \text{if $\Char{S}(x) = 1$} \\
a & \text{otherwise.}
\end{cases}
\]
Then $f$ is a computable function, and $S$ is the range of~$f$.
```

### BN-IN-T185

- Source term or concept: computably enumerable; recursively enumerable; c.e.; r.e.
- Chosen Bengali: গণনসাধ্যভাবে তালিকায়নযোগ্য; পুনরাবৃত্তভাবে তালিকায়নযোগ্য; c.e.; r.e.
- Rationale: T040 supplies তালিকায়ন and the source definition fixes the effective sense: the set is empty or the range of a total computable function. গণনসাধ্যভাবে তালিকায়নযোগ্য is the primary modern term; পুনরাবৃত্তভাবে তালিকায়নযোগ্য and the literal abbreviations c.e./r.e. retain the stated historical alternatives.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-ce-set-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্যভাবে তালিকায়নযোগ্য; পুনরাবৃত্তভাবে তালিকায়নযোগ্য; c.e.; r.e.’ express the OpenLogic sense(s) ‘computably enumerable; recursively enumerable; c.e.; r.e.’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 52 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:21-26` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:22`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:11-12` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:11`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:14-15` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:14`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:17-20` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:17`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:22-25` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Remember that if for each $e$, we let $W_e$ be the domain of $\cfind{e}$,
then the sequence $W_0$, $W_1$, $W_2$,~\dots enumerates the computably
enumerable sets. Some of these sets are computable. One can ask if
there is an algorithm which takes as input a value $x$, and, if $W_x$
happens to be computable, returns an index for its characteristic
function. The answer is ``no,'' there is no such algorithm:
```

### BN-IN-T186

- Source term or concept: semi-decidable; range characterization; domain characterization; existential characterization
- Chosen Bengali: অর্ধ-নির্ণেয়; মানপরিসর-চরিত্রায়ন; সংজ্ঞাক্ষেত্র-চরিত্রায়ন; অস্তিত্বমূলক চরিত্রায়ন
- Rationale: The equivalence theorem and its constructions govern these compounds. অর্ধ-নির্ণেয় promises eventual positive recognition only; the range, partial-domain and existential-projection clauses are extensionally equivalent presentations of c.e. sets. The terms retain মানপরিসর and সংজ্ঞাক্ষেত্র from the established function register.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-ce-characterization-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অর্ধ-নির্ণেয়; মানপরিসর-চরিত্রায়ন; সংজ্ঞাক্ষেত্র-চরিত্রায়ন; অস্তিত্বমূলক চরিত্রায়ন’ express the OpenLogic sense(s) ‘semi-decidable; range characterization; domain characterization; existential characterization’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:40`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:249-257` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:266`; final reader page pending
  - `OLP-0272` `upstream/content/turing-machines/undecidability/unsolvability-decision-problem.tex:70-77` → `bn-Beng-IN/content/turing-machines/undecidability/unsolvability-decision-problem.tex:76`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
The first three clauses say that we can equivalently take any non-empty
computably enumerable set to be enumerated by either a computable
function, a partial computable function, or a primitive recursive
function. The fourth clause tells us that if $S$ is computably
enumerable, then for some index~$e$,
\[
S = \Setabs{x}{\cfind{e}(x) \fdefined}.
\]
In other words, $S$ is the set of inputs on for which the computation
of $\cfind{e}$ halts. For that reason, computably enumerable sets are
sometimes called \emph{semi-decidable}: if a number is in the set, you
eventually get a ``yes,'' but if it isn't, you never get a ``no''!{}
\end{explain}
```

### BN-IN-T187

- Source term or concept: halting set; self-halting set; canonical undecidable set
- Chosen Bengali: থামা-সেট; স্ব-থামা সেট; আদর্শ অনির্ণেয় সেট
- Rationale: The displayed definitions of K_0 and K fix the two sets. থামা-সেট contains coded index-input pairs whose computations halt, স্ব-থামা সেট restricts to equal index and input, and আদর্শ অনির্ণেয় সেট records its later role as a standard comparison object. The compounds remain open to expert review.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-halting-set-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘থামা-সেট; স্ব-থামা সেট; আদর্শ অনির্ণেয় সেট’ express the OpenLogic sense(s) ‘halting set; self-halting set; canonical undecidable set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:36-40` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:38`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:36-40` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:39`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:36-40` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:40`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:42-45` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:43`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
The set $K_0$ is the set of pairs $\tuple{e,x}$ such that
$\cfind{e}(x) \fdefined$, i.e., $\tuple{e,x} \in K_0$ iff $\cfind{e}$
is defined (halts) on input~$x$, so it is also called the ``halting
set.'' The set $K = \Setabs{e}{\cfind{e}(e) \fdefined}$ is the
``self-halting set.'' It is often used as a canonical undecidable set.
```

### BN-IN-T188

- Source term or concept: closure under union and intersection; parallel simulation; alternating enumeration
- Chosen Bengali: সংযোজন ও ছেদের অধীনে বদ্ধতা; সমান্তরাল অনুকরণ; পর্যায়ক্রমিক তালিকায়ন
- Rationale: The three closure constructions govern this register: domain searches give intersection and union, alternating outputs enumerate a union, and paired or parallel searches recognize the two cases. সংযোজন ও ছেদের অধীনে বদ্ধতা states the theorem; সমান্তরাল অনুকরণ and পর্যায়ক্রমিক তালিকায়ন distinguish the two computational devices.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-ce-closure-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সংযোজন ও ছেদের অধীনে বদ্ধতা; সমান্তরাল অনুকরণ; পর্যায়ক্রমিক তালিকায়ন’ express the OpenLogic sense(s) ‘closure under union and intersection; parallel simulation; alternating enumeration’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T189

- Source term or concept: complement criterion for computability; positive and negative enumeration; total decision
- Chosen Bengali: গণনসাধ্যতার পূরক-মানদণ্ড; সদস্যতা ও অসদস্যতার তালিকায়ন; সর্বত্র-সংজ্ঞায়িত নির্ণয়
- Rationale: The theorem says that a set is decidable exactly when both its positive and negative cases are c.e. গণনসাধ্যতার পূরক-মানদণ্ড names that equivalence, while সদস্যতা ও অসদস্যতার তালিকায়ন and সর্বত্র-সংজ্ঞায়িত নির্ণয় record the dovetailed search and its guaranteed termination.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-complement-ce-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘গণনসাধ্যতার পূরক-মানদণ্ড; সদস্যতা ও অসদস্যতার তালিকায়ন; সর্বত্র-সংজ্ঞায়িত নির্ণয়’ express the OpenLogic sense(s) ‘complement criterion for computability; positive and negative enumeration; total decision’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T190

- Source term or concept: many-one reduction; many-one reducible; many-one equivalent; one-one reducible
- Chosen Bengali: বহু-এক হ্রাসকরণ; বহু-এক হ্রাসযোগ্য; বহু-এক সমতুল্য; এক-এক হ্রাসযোগ্য
- Rationale: The defining biconditional x in A iff f(x) in B fixes the direction and meaning. হ্রাসকরণ names the witnessing computable transformation, হ্রাসযোগ্য names the relation A <=_m B, সমতুল্য names its symmetric closure, and এক-এক retains the injective strengthening.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-many-one-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘বহু-এক হ্রাসকরণ; বহু-এক হ্রাসযোগ্য; বহু-এক সমতুল্য; এক-এক হ্রাসযোগ্য’ express the OpenLogic sense(s) ‘many-one reduction; many-one reducible; many-one equivalent; one-one reducible’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 14 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:14`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:29-33` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:30`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:44-51` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:44`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:63-66` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:63`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:63-66` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:64`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}
A set $A$ is a \emph{complete !!{computably enumerable} set}
(under many-one reducibility) if
\begin{enumerate}
\item $A$ is computably enumerable, and
\item for any other computably enumerable set $B$, $B \leq_m A$.
\end{enumerate}
\end{defn}
```

### BN-IN-T191

- Source term or concept: transitivity of reducibility; Turing reducibility; Karp reducibility; Cook reducibility
- Chosen Bengali: হ্রাসযোগ্যতার সঞ্চারিতা; টুরিং হ্রাসযোগ্যতা; কার্প হ্রাসযোগ্যতা; কুক হ্রাসযোগ্যতা
- Rationale: Composition governs সঞ্চারিতা. The digression distinguishes one-query answer-preserving many-one reduction from oracle-style টুরিং হ্রাসযোগ্যতা and explicitly names the polynomial-time analogues কার্প and কুক হ্রাসযোগ্যতা. The eponymic names are transliterated while the common relation suffix stays stable.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-reducibility-properties-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘হ্রাসযোগ্যতার সঞ্চারিতা; টুরিং হ্রাসযোগ্যতা; কার্প হ্রাসযোগ্যতা; কুক হ্রাসযোগ্যতা’ express the OpenLogic sense(s) ‘transitivity of reducibility; Turing reducibility; Karp reducibility; Cook reducibility’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:73-89` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:75`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:91-100` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:94`; final reader page pending
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:91-100` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:95`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{digress}
A more general notion of reducibility called \emph{Turing
reducibility} is useful in other contexts, especially for proving
undecidability results. Note that by \olref[cmp]{cor:comp-k}, the
complement of~$K_0$ is not reducible to~$K_0$, since it is not
computably enumerable. But, intuitively, if you knew the answers to
questions about $K_0$, you would know the answer to questions about
its complement as well. A set $A$ is said to be Turing reducible
to~$B$ if one can determine answers to questions in~$A$ using a
computable procedure that can ask questions about~$B$. This is more
liberal than many-one reducibility, in which (1)~you are only allowed
to ask one question about $B$, and (2)~a ``yes'' answer has to
translate to a ``yes'' answer to the question about $A$, and similarly
for ``no.'' It is still the case that if $A$~is Turing reducible
to~$B$ and $B$~is computable then $A$~is computable as well (though,
as we have seen, the analogous statement does not hold for computable
enumerability).
```

### BN-IN-T192

- Source term or concept: complete computably enumerable set; c.e.-hardest; neither computable nor complete
- Chosen Bengali: সম্পূর্ণ গণনসাধ্যভাবে তালিকায়নযোগ্য সেট; কঠিনতম c.e. সেট; গণনসাধ্যও নয়, সম্পূর্ণও নয়
- Rationale: The two-clause definition governs সম্পূর্ণ: the set is itself c.e. and every c.e. set many-one reduces to it. কঠিনতম records the induced ordering intuition, while the final phrase preserves the Friedberg-Muchnik contrast with intermediate c.e. examples.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-ce-completeness-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সম্পূর্ণ গণনসাধ্যভাবে তালিকায়নযোগ্য সেট; কঠিনতম c.e. সেট; গণনসাধ্যও নয়, সম্পূর্ণও নয়’ express the OpenLogic sense(s) ‘complete computably enumerable set; c.e.-hardest; neither computable nor complete’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:10`; final reader page pending
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:21-23` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:22`; final reader page pending
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:25-27` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:27`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{cce}
\olsection{Complete Computably Enumerable Sets}
```

### BN-IN-T193

- Source term or concept: oracle; fixed-input machine; K_1 halting set
- Chosen Bengali: ওরাকল; স্থির-নিবেশ যন্ত্র; K_1 থামা-সেট
- Rationale: The informal and s-m-n constructions govern the register. ওরাকল is the hypothetical source of correct halting answers, স্থির-নিবেশ যন্ত্র ignores its received argument and runs the encoded computation on a fixed input, and K_1 থামা-সেট names the indices defined at input zero.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-K1-reduction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ওরাকল; স্থির-নিবেশ যন্ত্র; K_1 থামা-সেট’ express the OpenLogic sense(s) ‘oracle; fixed-input machine; K_1 halting set’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0246` `upstream/content/computability/computability-theory/k-1.tex:30-45` → `bn-Beng-IN/content/computability/computability-theory/k-1.tex:33`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
This is a little bit tricky, since using $K_1$ we can
only ask questions about computations that start with a particular
input, $0$. Suppose you have a smart friend who can answer questions
of this type (friends like this are known as ``oracles''). Then
suppose someone comes up to you and asks you whether or not $\tuple{e,
  x}$ is in $K_0$, that is, whether or not machine $e$ halts on input
$x$. One thing you can do is build another machine, $e_x$, that, for
\emph{any} input, ignores that input and instead runs~$e$ on input
$x$. Then clearly the question as to whether machine $e$ halts on
input $x$ is equivalent to the question as to whether machine $e_x$
halts on input $0$ (or any other input). So, then you ask your friend
whether this new machine, $e_x$, halts on input $0$; your friend's
answer to the modified question provides the answer to the original
one. This provides the desired reduction of $K_0$ to~$K_1$.
\end{explain}
```

### BN-IN-T194

- Source term or concept: totality; Tot index set; arithmetical hierarchy
- Chosen Bengali: সর্বত্র-সংজ্ঞায়িততা; Tot সূচক-সেট; পাটীগাণিতিক স্তরক্রম
- Rationale: T177 supplies the total/partial function distinction, while the reduction from K governs the decision claim. সর্বত্র-সংজ্ঞায়িততা names the property of halting on every input, Tot সূচক-সেট names its index collection, and পাটীগাণিতিক স্তরক্রম retains the stated stronger classification without developing it here.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-totality-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সর্বত্র-সংজ্ঞায়িততা; Tot সূচক-সেট; পাটীগাণিতিক স্তরক্রম’ express the OpenLogic sense(s) ‘totality; Tot index set; arithmetical hierarchy’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0247` `upstream/content/computability/computability-theory/total.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/total.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{tot}
\olsection{Totality is Undecidable}
```

### BN-IN-T195

- Source term or concept: Rice's theorem; nontrivial index set; semantic property of a computed function
- Chosen Bengali: রাইসের উপপাদ্য; অতুচ্ছ সূচক-সেট; গণিত অপেক্ষকের আচরণগত বৈশিষ্ট্য
- Rationale: The theorem and proof govern the register: membership is invariant across all indices computing the same partial function, and every nonempty proper class of such functions yields an undecidable index set. আচরণগত বৈশিষ্ট্য marks the semantic target of Rice's theorem while leaving syntactic program questions outside its scope.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-rice-theorem-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘রাইসের উপপাদ্য; অতুচ্ছ সূচক-সেট; গণিত অপেক্ষকের আচরণগত বৈশিষ্ট্য’ express the OpenLogic sense(s) ‘Rice's theorem; nontrivial index set; semantic property of a computed function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:10`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:23-28` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:23`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:37-51` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:36`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:37-51` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:43`; final reader page pending
  - `OLP-0248` `upstream/content/computability/computability-theory/rice-theorem.tex:53-57` → `bn-Beng-IN/content/computability/computability-theory/rice-theorem.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{rce}
\olsection{Rice's Theorem}
```

### BN-IN-T196

- Source term or concept: program syntax; program behavior; index invariance
- Chosen Bengali: প্রোগ্রামের বাক্যগঠন; প্রোগ্রামের আচরণ; সূচক-অপরিবর্তিতা
- Rationale: The source's examples fix the contrast. বাক্যগঠন covers symbol, line and statement-form questions about a particular program; আচরণ covers the partial function it computes; সূচক-অপরিবর্তিতা names the requirement that all indices for that same function receive the same answer.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-rice-explanation-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রোগ্রামের বাক্যগঠন; প্রোগ্রামের আচরণ; সূচক-অপরিবর্তিতা’ express the OpenLogic sense(s) ‘program syntax; program behavior; index invariance’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T197

- Source term or concept: fixed-point theorem; self-reference; diagonal specialization; self-printing program
- Chosen Bengali: স্থির-বিন্দু উপপাদ্য; স্ব-উল্লেখ; কর্ণ বিশেষায়ন; স্ব-মুদ্রণকারী প্রোগ্রাম
- Rationale: The equation cfind_e(y) simeq g(e,y) governs স্থির-বিন্দু and স্ব-উল্লেখ. কর্ণ বিশেষায়ন names the computable diag operation that fixes a program's own index as its first input, and স্ব-মুদ্রণকারী প্রোগ্রাম records the concrete string-program analogy.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-fixed-point-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্থির-বিন্দু উপপাদ্য; স্ব-উল্লেখ; কর্ণ বিশেষায়ন; স্ব-মুদ্রণকারী প্রোগ্রাম’ express the OpenLogic sense(s) ‘fixed-point theorem; self-reference; diagonal specialization; self-printing program’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 14 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:10`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:12`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:12-19` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:18`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:38`; final reader page pending
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:46`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{cmp}{thy}{apf}
\olsection{Applying the Fixed-Point Theorem}
```

### BN-IN-T198

- Source term or concept: fixed-point combinator; Curry's combinator; Turing's combinator; beta-equivalent
- Chosen Bengali: স্থির-বিন্দু সমাবেশক; কারির সমাবেশক; টুরিংয়ের সমাবেশক; বিটা-সমতুল্য
- Rationale: The tagged lambda-calculus derivations govern these terms. সমাবেশক names the closed operator producing a fixed point; the Curry and Turing forms remain distinct as in the two displayed reductions, and বিটা-সমতুল্য records their common reduction behavior.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-lambda-fixed-point-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্থির-বিন্দু সমাবেশক; কারির সমাবেশক; টুরিংয়ের সমাবেশক; বিটা-সমতুল্য’ express the OpenLogic sense(s) ‘fixed-point combinator; Curry's combinator; Turing's combinator; beta-equivalent’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:234`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:210-241` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:239`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{tagblock}{lambda}
\begin{digress}
The same idea can be used to get a ``fixed point'' combinator. Suppose
you have a lambda term $g$, and you want another term $k$ with the
property that $k$ is $\beta$-equivalent to $gk$. Define terms
\[
\fn{diag}(x) = xx
\]
and
\[
l(x) = g(\fn{diag}(x))
\]
using our notational conventions; in other words, $l$ is the term
$\lambd[x][g(xx)]$. Let $k$ be the term $ll$. Then we have
\begin{align*}
k & = (\lambd[x][g(xx)])(\lambd[x][g(xx)]) \\
& \red  g((\lambd[x][g(xx)])(\lambd[x][g(xx)])) \\
& = gk.
\end{align*}
If one takes
\[
Y = \lambd[g][((\lambd[x][g(xx)])(\lambd[x][g(xx)]))]
\]
then $Yg$ and $g(Yg)$ reduce to a common term; so $Yg \equiv_\beta
g(Yg)$. This is known as ``Curry's combinator.'' If instead one takes
\[
Y = (\lambd[xg][g(xxg)])(\lambd[xg][g(xxg)])
\]
then in fact $Yg$ reduces to $g(Yg)$, which is a stronger statement.
This latter version of $Y$ is known as ``Turing's combinator.''
\end{digress}
\end{tagblock}
```

### BN-IN-T199

- Source term or concept: characteristic-function index extraction; computable-set index selector; fixed-point counterexample
- Chosen Bengali: চরিত্রসূচক-অপেক্ষকের সূচক নিষ্কাশন; গণনসাধ্য সেটের সূচক-নির্বাচক; স্থির-বিন্দু প্রতিদৃষ্টান্ত
- Rationale: The application theorem governs this register: even when W_e is computable, no partial computable procedure uniformly returns an index for its characteristic function. The singleton/empty fixed point makes the selected program disagree at zero, including the case where the selector itself is undefined.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-index-extraction-register; confidence: low_pending_occurrence; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘চরিত্রসূচক-অপেক্ষকের সূচক নিষ্কাশন; গণনসাধ্য সেটের সূচক-নির্বাচক; স্থির-বিন্দু প্রতিদৃষ্টান্ত’ express the OpenLogic sense(s) ‘characteristic-function index extraction; computable-set index selector; fixed-point counterexample’ without collision with adjacent logical or mathematical concepts?
- Exact target occurrence: none yet; this decision governs a token, compound variant or future translated source block.

### BN-IN-T200

- Source term or concept: recursive self-definition; greatest common divisor; remainder; termination by descent
- Chosen Bengali: স্ব-উল্লেখী পুনরাবৃত্ত সংজ্ঞা; গরিষ্ঠ সাধারণ গুণনীয়ক; ভাগশেষ; অবরোহণে সমাপ্তি
- Rationale: The fixed-point schema and Euclidean example govern the terms. স্ব-উল্লেখী পুনরাবৃত্ত সংজ্ঞা names a function defined through a recursive call, গরিষ্ঠ সাধারণ গুণনীয়ক and ভাগশেষ retain the arithmetic roles, and অবরোহণে সমাপ্তি records the later induction that upgrades partial computability to totality.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-recursive-definition-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্ব-উল্লেখী পুনরাবৃত্ত সংজ্ঞা; গরিষ্ঠ সাধারণ গুণনীয়ক; ভাগশেষ; অবরোহণে সমাপ্তি’ express the OpenLogic sense(s) ‘recursive self-definition; greatest common divisor; remainder; termination by descent’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 10 occurrence(s). Representative locations:
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:36`; final reader page pending
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:45`; final reader page pending
  - `OLP-0222` `upstream/content/computability/recursive-functions/other-recursions.tex:50-55` → `bn-Beng-IN/content/computability/recursive-functions/other-recursions.tex:49`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:16`; final reader page pending
  - `OLP-0219` `upstream/content/computability/recursive-functions/primes.tex:12-27` → `bn-Beng-IN/content/computability/recursive-functions/primes.tex:18`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For a concrete example, the ``greatest common divisor'' function
$\fn{gcd}(u,v)$ can be defined by
\[
\fn{gcd}(u,v) \simeq
\begin{cases}
v & \text{if $u = 0$} \\
\fn{gcd}(\fn{mod}(v, u), u) & \text{otherwise}
\end{cases}
\]
where $\fn{mod}(v, u)$ denotes the remainder of dividing $v$
by~$u$. An appeal to the fixed-point lemma shows that $\fn{gcd}$ is
partial computable. (In fact, this can be put in the format above,
letting $y$ code the pair $\tuple{u, v}$.) A subsequent induction
on~$u$ then shows that, in fact, $\fn{gcd}$ is total.
```

### BN-IN-T201

- Source term or concept: tape; read-write head; tape square; tape alphabet; end marker; blank symbol; stroke symbol
- Chosen Bengali: ফিতা; পাঠ-লেখ হেড; ফিতার ঘর; ফিতার বর্ণমালা; শেষ-চিহ্ন; ফাঁকা প্রতীক; দাগ-প্রতীক
- Rationale: T170 already fixes টুরিং যন্ত্র and the new mechanism description governs its concrete vocabulary. ফিতা continues the term already used in the computation-coding chapter; পাঠ-লেখ হেড keeps the familiar technical loan while stating both operations; ঘর names one discrete tape position. The three distinguished macros govern শেষ-চিহ্ন, ফাঁকা প্রতীক and দাগ-প্রতীক, independently of their printed glyphs.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-tape-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ফিতা; পাঠ-লেখ হেড; ফিতার ঘর; ফিতার বর্ণমালা; শেষ-চিহ্ন; ফাঁকা প্রতীক; দাগ-প্রতীক’ express the OpenLogic sense(s) ‘tape; read-write head; tape square; tape alphabet; end marker; blank symbol; stroke symbol’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 115 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:19`; final reader page pending
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:25`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:25`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:32`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T202

- Source term or concept: machine state; initial state; transition function; instruction set; direction of movement
- Chosen Bengali: যন্ত্রের দশা; আরম্ভিক দশা; অবস্থান্তর অপেক্ষক; নির্দেশ-সেট; চলনের দিক
- Rationale: The displayed partial map from a state-symbol pair to a new state, symbol and direction controls these terms. দশা continues the earlier computation-record wording; অবস্থান্তর অপেক্ষক names the map that changes a machine state; নির্দেশ-সেট names the finite program presentation. চলনের দিক covers left, right and staying put without treating the head movement as tape motion.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-transition-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যন্ত্রের দশা; আরম্ভিক দশা; অবস্থান্তর অপেক্ষক; নির্দেশ-সেট; চলনের দিক’ express the OpenLogic sense(s) ‘machine state; initial state; transition function; instruction set; direction of movement’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 37 occurrence(s). Representative locations:
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:33`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:34`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:48`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:58-68` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:61`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:97-125` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:103`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
How do we combine Turing machines $M = \tuple{Q, \Sigma, q_0, \delta}$
and~$M' = \tuple{Q', \Sigma', q_0', \delta'}$?  We now use the
configuration of the tape after $M$~has halted as the input
configuration of a run of machine~$M'$.  To get a single Turing
machine $M \frown M'$ that does this, do the following:
\begin{enumerate}
    \item Renumber (or relabel) all the states~$Q'$ of~$M'$ so that $M$
    and~$M'$ have no states in common ($Q \cap Q' = \emptyset$).
    \item The states of $M \frown M'$ are $Q \cup Q'$.
    \item The tape alphabet is $\Sigma \cup \Sigma'$.
    \item The start state is~$q_0$.
    \item The transition function is the function $\delta''$ given by:
    \[\delta''(q,\sigma) =
    \begin{cases}
      \delta(q,\sigma) & \text{if $q \in Q$}\\
      \delta'(q,\sigma) & \text{if $q \in Q'$}\\
      \tuple{q_0', \sigma, \TMstay} & \text{if $q \in Q$ and
      $\delta(q,\sigma)$ is undefined}
    \end{cases}\]
\end{enumerate}
The resulting machine uses the instructions of~$M$ when it is in a
state $q \in Q$, the instructions of~$M'$ when it is in a state~$q \in
Q'$. When it is in a state $q \in Q$ and is scanning a symbol~$\sigma$
for which $M$ has no transition (i.e., $M$ would have halted), it
enters the start state of~$M'$ (and leaves the tape contents and head
position as it is).
```

### BN-IN-T203

- Source term or concept: halt; halting state; accept an input; undefined transition
- Chosen Bengali: থামে; থামা-দশা; নিবেশ গ্রহণ করে; অসংজ্ঞায়িত অবস্থান্তর
- Rationale: T174 supplies the existing halting family. In this chapter a machine থামে exactly when no instruction is defined for its current state-symbol pair; থামা-দশা is an optional explicit convention, and নিবেশ গ্রহণ করে records the examples’ convention that halting counts as acceptance. The term অসংজ্ঞায়িত অবস্থান্তর preserves the partial-function account.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-halting-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘থামে; থামা-দশা; নিবেশ গ্রহণ করে; অসংজ্ঞায়িত অবস্থান্তর’ express the OpenLogic sense(s) ‘halt; halting state; accept an input; undefined transition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 119 occurrence(s). Representative locations:
  - `OLP-0250` `upstream/content/computability/computability-theory/application-fixed-point.tex:34-60` → `bn-Beng-IN/content/computability/computability-theory/application-fixed-point.tex:59`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:72-76` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:70`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:72-76` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:71`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:72-76` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:72`; final reader page pending
  - `OLP-0241` `upstream/content/computability/computability-theory/ce-closed-cup-cap.tex:78-91` → `bn-Beng-IN/content/computability/computability-theory/ce-closed-cup-cap.tex:84`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
Let $f$ be any computable function; we will construct an $e$
such that $W_e$ is computable, but $\cfind{f(e)}$ is not its
characteristic function. Using the fixed point theorem, we can find an
index $e$ such that
\[
\cfind{e}(y) \simeq
\begin{cases}
0 & \text{if $y=0$ and $\cfind{f(e)}(0) \fdefined = 0$} \\
\text{undefined} & \text{otherwise.}
\end{cases}
\]
That is, $e$ is obtained by applying the fixed-point theorem to the
function defined by
\[
g(x,y) \simeq
\begin{cases}
0 & \text{if $y=0$ and $\cfind{f(x)}(0) \fdefined = 0$} \\
\text{undefined} & \text{otherwise.}
\end{cases}
\]
Informally, we can see that $g$ is partial computable, as follows: on
input $x$ and $y$, the algorithm first checks to see if $y$ is equal
to~$0$. If it is, the algorithm computes $f(x)$, and then uses the
universal machine to compute $\cfind{f(x)}(0)$. If this last computation
halts and returns~$0$, the algorithm returns~$0$; otherwise, the
algorithm doesn't halt.
```

### BN-IN-T204

- Source term or concept: time requirement; memory requirement; bounded resources; computational complexity
- Chosen Bengali: সময়ের চাহিদা; স্মৃতির চাহিদা; সীমাবদ্ধ সম্পদ; গণনামূলক জটিলতা
- Rationale: The introduction explicitly idealizes computability by imposing no time or memory limit, then contrasts it with computation under bounded resources. সময়ের চাহিদা and স্মৃতির চাহিদা name the two resource measures; সীমাবদ্ধ সম্পদ states the restricted setting; গণনামূলক জটিলতা continues T170’s গণনামূলক root for the subject studying those bounds.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-resource-complexity-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সময়ের চাহিদা; স্মৃতির চাহিদা; সীমাবদ্ধ সম্পদ; গণনামূলক জটিলতা’ express the OpenLogic sense(s) ‘time requirement; memory requirement; bounded resources; computational complexity’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0244` `upstream/content/computability/computability-theory/prop-reduce.tex:91-100` → `bn-Beng-IN/content/computability/computability-theory/prop-reduce.tex:92`; final reader page pending
  - `OLP-0243` `upstream/content/computability/computability-theory/reducibility.tex:19-29` → `bn-Beng-IN/content/computability/computability-theory/reducibility.tex:22`; final reader page pending
  - `OLP-0254` `upstream/content/turing-machines/machines-computations/introduction.tex:86-108` → `bn-Beng-IN/content/turing-machines/machines-computations/introduction.tex:92`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:29-39` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:34`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
You should think about the various notions of reducibility we have
discussed, and understand the distinctions between them. We will,
however, only deal with many-one reducibility in this chapter.
Incidentally, both types of reducibility discussed in the last
paragraph have analogues in computational complexity, with the added
requirement that the Turing machines run in polynomial time: the
complexity version of many-one reducibility is known as \emph{Karp
reducibility}, while the complexity version of Turing reducibility is
known as \emph{Cook reducibility}.
\end{digress}
```

### BN-IN-T205

- Source term or concept: state diagram; state node; outgoing arrow; machine table; transition label
- Chosen Bengali: দশা-চিত্র; দশা-নোড; বহির্মুখী তীর; যন্ত্র-সারণি; অবস্থান্তর-নির্দেশ
- Rationale: The diagrams and table are controlling evidence for this visual register. A দশা-নোড carries one machine state, a labeled বহির্মুখী তীর gives an instruction from it, and a যন্ত্র-সারণি indexes the same instructions by current state and scanned symbol. অবস্থান্তর-নির্দেশ preserves the connection to T202 while keeping the displayed three-field label distinct from the whole partial function.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-representation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘দশা-চিত্র; দশা-নোড; বহির্মুখী তীর; যন্ত্র-সারণি; অবস্থান্তর-নির্দেশ’ express the OpenLogic sense(s) ‘state diagram; state node; outgoing arrow; machine table; transition label’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 11 occurrence(s). Representative locations:
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:58-68` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:61`; final reader page pending
  - `OLP-0255` `upstream/content/turing-machines/machines-computations/representing-tms.tex:12-23` → `bn-Beng-IN/content/turing-machines/machines-computations/representing-tms.tex:13`; final reader page pending
  - `OLP-0255` `upstream/content/turing-machines/machines-computations/representing-tms.tex:12-23` → `bn-Beng-IN/content/turing-machines/machines-computations/representing-tms.tex:14`; final reader page pending
  - `OLP-0255` `upstream/content/turing-machines/machines-computations/representing-tms.tex:58-64` → `bn-Beng-IN/content/turing-machines/machines-computations/representing-tms.tex:55`; final reader page pending
  - `OLP-0255` `upstream/content/turing-machines/machines-computations/representing-tms.tex:141-148` → `bn-Beng-IN/content/turing-machines/machines-computations/representing-tms.tex:137`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}
\emph{Combining Machines:} We'll design a machine which, when started
on input consisting of two blocks of~$\TMstroke$'s of length $n$
and~$m$, halts with a single block of $2(m+n)$ $\TMstroke$'s on the
tape. In order to build this machine, we can combine two machines we
are already familiar with: the addition machine, and the doubler. We
begin by drawing a state diagram for the addition machine.
\[
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2.8cm,
                    semithick]
  \tikzstyle{every state}=[fill=none,draw=black,text=black]
```

### BN-IN-T206

- Source term or concept: configuration; initial configuration; run; yields in one step; head position
- Chosen Bengali: কনফিগারেশন; আরম্ভিক কনফিগারেশন; চালন; এক ধাপে দেয়; হেডের অবস্থান
- Rationale: The formal triples and successor clauses govern these terms. কনফিগারেশন is retained as the recognizable technical loan for tape content, head position and state together; আরম্ভিক কনফিগারেশন fixes the input setup; চালন is a finite or infinite sequence of such triples; and এক ধাপে দেয় names the immediate transition relation.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-configuration-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কনফিগারেশন; আরম্ভিক কনফিগারেশন; চালন; এক ধাপে দেয়; হেডের অবস্থান’ express the OpenLogic sense(s) ‘configuration; initial configuration; run; yields in one step; head position’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 68 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:18`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:40-93` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:92`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:95-100` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:97`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:25`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:25-50` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:26`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T207

- Source term or concept: even machine; accept; reject; loop forever; trace configurations
- Chosen Bengali: জোড়-যন্ত্র; গ্রহণ করে; বর্জন করে; চিরকাল চক্রাকারে চলে; কনফিগারেশন ধাপে ধাপে অনুসরণ করে
- Rationale: The worked parity example controls this operational vocabulary. জোড়-যন্ত্র alternates its two states over strokes; under the section’s convention it গ্রহণ করে by halting and বর্জন করে by nontermination. চিরকাল চক্রাকারে চলে states the explicit infinite behavior, while ধাপে ধাপে অনুসরণ describes deriving successive configurations rather than merely inspecting a static diagram.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-execution-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘জোড়-যন্ত্র; গ্রহণ করে; বর্জন করে; চিরকাল চক্রাকারে চলে; কনফিগারেশন ধাপে ধাপে অনুসরণ করে’ express the OpenLogic sense(s) ‘even machine; accept; reject; loop forever; trace configurations’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 16 occurrence(s). Representative locations:
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:84-99` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:89`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:84-99` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:90`; final reader page pending
  - `OLP-0232` `upstream/content/computability/computability-theory/s-m-n.tex:30-41` → `bn-Beng-IN/content/computability/computability-theory/s-m-n.tex:32`; final reader page pending
  - `OLP-0021` `upstream/content/sets-functions-relations/functions/function-basics.tex:92-100` → `bn-Beng-IN/content/sets-functions-relations/functions/function-basics.tex:54`; final reader page pending
  - `OLP-0257` `upstream/content/turing-machines/machines-computations/configuration.tex:12-23` → `bn-Beng-IN/content/turing-machines/machines-computations/configuration.tex:13`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{tagblock}{TMs}
\begin{explain}
We can describe this argument in terms of Turing machines.  Suppose
there were a Turing machine~$H$ that takes as input a description of a
Turing machine~$E$ and an input~$x$, and decides whether or not $E$
halts on input~$x$. Then we could build another Turing machine~$G$
which takes a single input~$x$, runs $H$ to decide if the machine
$M_x$ with index~$x$ halts on input~$x$, and does the opposite. In
other words, if $H$ reports that $M_x$ halts on input~$x$, $G$ goes
into an infinite loop, and if $H$ reports that $M_x$ doesn't halt on
input~$x$, then $G$ just halts. Does $G$ halt on its own index as
input? The argument above shows that it does if and only if it
doesn't---a contradiction. So our supposition that there is a such
Turing machine~$H$ must be false.
\end{explain}
\end{tagblock}
```

### BN-IN-T208

- Source term or concept: doubler; strategy; erase input; duplicate a string; alphabetizer
- Chosen Bengali: দ্বিগুণকারী; কৌশল; নিবেশ মোছে; প্রতীকক্রমের অনুলিপি করে; বর্ণানুক্রমে সাজানোর যন্ত্র
- Rationale: The doubler construction and exercises govern this register. দ্বিগুণকারী turns n strokes into 2n strokes through a multi-state কৌশল that erases each processed input mark. প্রতীকক্রমের অনুলিপি করে distinguishes copying an arbitrary A/B word from numerical doubling, and বর্ণানুক্রমে সাজানোর যন্ত্র names the exercise that rearranges all A symbols before all B symbols.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-construction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘দ্বিগুণকারী; কৌশল; নিবেশ মোছে; প্রতীকক্রমের অনুলিপি করে; বর্ণানুক্রমে সাজানোর যন্ত্র’ express the OpenLogic sense(s) ‘doubler; strategy; erase input; duplicate a string; alphabetizer’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 39 occurrence(s). Representative locations:
  - `OLP-0216` `upstream/content/computability/recursive-functions/examples.tex:13-23` → `bn-Beng-IN/content/computability/recursive-functions/examples.tex:22`; final reader page pending
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:16-39` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:21`; final reader page pending
  - `OLP-0116` `upstream/content/first-order-logic/axiomatic-deduction/proving-things.tex:41-56` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/proving-things.tex:55`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:95-100` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:97`; final reader page pending
  - `OLP-0130` `upstream/content/first-order-logic/completeness/henkin-expansions.tex:13-30` → `bn-Beng-IN/content/first-order-logic/completeness/henkin-expansions.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We already have some examples of primitive recursive functions: the
addition and multiplication functions~$\Add$ and $\Mult$.  The
identity function $\fn{id}(x) = x$ is primitive recursive, since it is
just~$\Proj{1}{0}$. The constant functions $\fn{const}_n(x) = n$ are
primitive recursive since they can be defined from $\Zero$ and $\Succ$
by successive composition. This is useful when we want to use
constants in primitive recursive definitions, e.g., if we want to
define the function $f(x) = 2 \cdot x$ can obtain it by composition
from $\fn{const}_n(x)$ and multiplication as $f(x) =
\Mult(\fn{const}_2(x), \Proj{1}{0}(x))$. We'll make use of this trick
from now on.
```

### BN-IN-T209

- Source term or concept: unary representation; arithmetical function; stroke block; encode a number; compute a partial function
- Chosen Bengali: এককীয় উপস্থাপনা; পাটিগাণিতিক অপেক্ষক; দাগের খণ্ড; সংখ্যার সংকেতায়ন; আংশিক অপেক্ষক গণনা করে
- Rationale: The source definitions govern the representation: n is encoded by exactly n stroke symbols, with the empty string representing zero, and arguments are separated by blanks. এককীয় উপস্থাপনা contrasts explicitly with later দ্বিমিক উপস্থাপনা; পাটিগাণিতিক অপেক্ষক follows the established arithmetic root; and the halting/output clauses govern when a total or partial function is computed.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-unary-computation-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘এককীয় উপস্থাপনা; পাটিগাণিতিক অপেক্ষক; দাগের খণ্ড; সংখ্যার সংকেতায়ন; আংশিক অপেক্ষক গণনা করে’ express the OpenLogic sense(s) ‘unary representation; arithmetical function; stroke block; encode a number; compute a partial function’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0258` `upstream/content/turing-machines/machines-computations/unary-numbers.tex:9-10` → `bn-Beng-IN/content/turing-machines/machines-computations/unary-numbers.tex:10`; final reader page pending
  - `OLP-0258` `upstream/content/turing-machines/machines-computations/unary-numbers.tex:131-185` → `bn-Beng-IN/content/turing-machines/machines-computations/unary-numbers.tex:131`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:62-65` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:61`; final reader page pending
  - `OLP-0265` `upstream/content/turing-machines/undecidability/introduction.tex:12-19` → `bn-Beng-IN/content/turing-machines/undecidability/introduction.tex:12`; final reader page pending
  - `OLP-0267` `upstream/content/turing-machines/undecidability/universal-tm.tex:70-87` → `bn-Beng-IN/content/turing-machines/undecidability/universal-tm.tex:72`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{tur}{mac}{una}
\olsection{Unary Representation of Numbers}
```

### BN-IN-T210

- Source term or concept: addition machine; mover machine; single output block; temporary marker; equality machine
- Chosen Bengali: যোগ-যন্ত্র; স্থানান্তরক যন্ত্র; নির্গমের একটিমাত্র খণ্ড; সাময়িক চিহ্ন; সমতা-যন্ত্র
- Rationale: The worked diagrams control these construction terms. যোগ-যন্ত্র joins two unary blocks by filling their separator and erasing the final stroke; স্থানান্তরক যন্ত্র moves a displaced stroke block to the tape beginning; and সাময়িক চিহ্ন covers the deliberately reused end-marker symbol that bounds the block. The output convention requires one contiguous block where the exercises specify it.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-unary-machine-construction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যোগ-যন্ত্র; স্থানান্তরক যন্ত্র; নির্গমের একটিমাত্র খণ্ড; সাময়িক চিহ্ন; সমতা-যন্ত্র’ express the OpenLogic sense(s) ‘addition machine; mover machine; single output block; temporary marker; equality machine’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:58-68` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:60`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:58-68` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:61`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:74-89` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:80`; final reader page pending
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:127-150` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:142`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:52-58` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{ex}
\emph{Combining Machines:} We'll design a machine which, when started
on input consisting of two blocks of~$\TMstroke$'s of length $n$
and~$m$, halts with a single block of $2(m+n)$ $\TMstroke$'s on the
tape. In order to build this machine, we can combine two machines we
are already familiar with: the addition machine, and the doubler. We
begin by drawing a state diagram for the addition machine.
\[
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2.8cm,
                    semithick]
  \tikzstyle{every state}=[fill=none,draw=black,text=black]
```

### BN-IN-T211

- Source term or concept: designated halting state; reject state; explicit acceptance; no added computing power
- Chosen Bengali: নির্দিষ্ট থামা-দশা; বর্জন-দশা; স্পষ্ট গ্রহণ; গণনক্ষমতা বাড়ে না
- Rationale: T203 already fixes the halting vocabulary. This section distinguishes a single designated h state from a separate r state, while its two parity diagrams make acceptance and rejection explicit. গণনক্ষমতা বাড়ে না records the equivalence claim: adding these control states changes presentation, not the computable functions.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-dedicated-halting-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নির্দিষ্ট থামা-দশা; বর্জন-দশা; স্পষ্ট গ্রহণ; গণনক্ষমতা বাড়ে না’ express the OpenLogic sense(s) ‘designated halting state; reject state; explicit acceptance; no added computing power’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:12-25` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:14`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:27-35` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:27`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:37-50` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:36`; final reader page pending
  - `OLP-0259` `upstream/content/turing-machines/machines-computations/halting-states.tex:68-77` → `bn-Beng-IN/content/turing-machines/machines-computations/halting-states.tex:66`; final reader page pending
  - `OLP-0259` `upstream/content/turing-machines/machines-computations/halting-states.tex:68-77` → `bn-Beng-IN/content/turing-machines/machines-computations/halting-states.tex:68`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
In section \olref[hal]{sec}, we considered Turing machines that have a
single, designated halting state~$h$---such machines are guaranteed to
halt, if they halt at all, in state~$h$.  In this way, machines with a
single halting state are more ``disciplined'' than we allow Turing
machines in general to be.  There are other restrictions we might
impose on the behavior of Turing machines.  For instance, we also have
not prohibited Turing machines from ever erasing the tape-end marker
on square~$0$, or to attempt to move left from square~$0$. (Our
definition states that the head simply stays on square~$0$ in this
case; other definitions have the machine halt.) It is likewise
sometimes desirable to be able to assume that a Turing machine, if
it halts at all, halts on square~$1$.
\end{explain}
```

### BN-IN-T212

- Source term or concept: disciplined machine; halt scanning square 1; preserve the tape-end marker; never attempt a left move from square 0
- Chosen Bengali: শৃঙ্খলাবদ্ধ যন্ত্র; ঘর ১ পড়তে পড়তে থামে; ফিতার শেষ-চিহ্ন অক্ষুণ্ণ রাখে; ঘর ০ থেকে বাঁ দিকে যাওয়ার চেষ্টা করে না
- Rationale: The four-clause definition governs শৃঙ্খলাবদ্ধ: a unique halting state, a fixed final head position, preservation of the left marker, and no attempted left-boundary move. The descriptive Bengali clauses are retained rather than compressed into opaque compounds, and the proposition fixes behavioral equivalence with arbitrary machines.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-disciplined-machine-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘শৃঙ্খলাবদ্ধ যন্ত্র; ঘর ১ পড়তে পড়তে থামে; ফিতার শেষ-চিহ্ন অক্ষুণ্ণ রাখে; ঘর ০ থেকে বাঁ দিকে যাওয়ার চেষ্টা করে না’ express the OpenLogic sense(s) ‘disciplined machine; halt scanning square 1; preserve the tape-end marker; never attempt a left move from square 0’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 4 occurrence(s). Representative locations:
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:9-10` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:10`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:52-58` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:50`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:86-88` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:85`; final reader page pending
  - `OLP-0260` `upstream/content/turing-machines/machines-computations/disciplined-machines.tex:91-94` → `bn-Beng-IN/content/turing-machines/machines-computations/disciplined-machines.tex:90`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{tur}{mac}{dis}
\olsection{Disciplined Machines}
```

### BN-IN-T213

- Source term or concept: combine Turing machines; constituent stages; relabel disjoint state sets; transfer control; combined machine
- Chosen Bengali: টুরিং যন্ত্রের সংযোজন; উপাংশ পর্যায়; বিযুক্ত দশা-সেটের জন্য নতুন নাম দেয়; নিয়ন্ত্রণ হস্তান্তর করে; সংযোজিত যন্ত্র
- Rationale: The construction M-frown-M-prime governs the register. সংযোজন follows the printed concatenation symbol without colliding with logical conjunction in context; state relabeling makes Q and Q-prime disjoint; and নিয়ন্ত্রণ হস্তান্তর describes the added transition from an otherwise halting M configuration to the initial state of M-prime.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-machine-combination-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘টুরিং যন্ত্রের সংযোজন; উপাংশ পর্যায়; বিযুক্ত দশা-সেটের জন্য নতুন নাম দেয়; নিয়ন্ত্রণ হস্তান্তর করে; সংযোজিত যন্ত্র’ express the OpenLogic sense(s) ‘combine Turing machines; constituent stages; relabel disjoint state sets; transfer control; combined machine’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0261` `upstream/content/turing-machines/machines-computations/combining-machines.tex:9-10` → `bn-Beng-IN/content/turing-machines/machines-computations/combining-machines.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olfileid{tur}{mac}{cmb}
\olsection{Combining Turing Machines}
```

### BN-IN-T214

- Source term or concept: variant; liberal definition; restrictive definition; transition relation; nondeterministic Turing machine
- Chosen Bengali: রূপভেদ; উদার সংজ্ঞা; সীমাবদ্ধ সংজ্ঞা; অবস্থান্তর সম্বন্ধ; অনির্ধারণবাদী টুরিং যন্ত্র
- Rationale: The variant survey contrasts permissions and restrictions across equivalent machine definitions. অবস্থান্তর সম্বন্ধ is distinguished from T202’s single-valued অবস্থান্তর অপেক্ষক; it may associate one current pair with multiple successor triples, which governs অনির্ধারণবাদী. রূপভেদ covers the whole family without implying a different computability class.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-variant-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘রূপভেদ; উদার সংজ্ঞা; সীমাবদ্ধ সংজ্ঞা; অবস্থান্তর সম্বন্ধ; অনির্ধারণবাদী টুরিং যন্ত্র’ express the OpenLogic sense(s) ‘variant; liberal definition; restrictive definition; transition relation; nondeterministic Turing machine’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:14`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:67-70` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:66`; final reader page pending
  - `OLP-0266` `upstream/content/turing-machines/undecidability/enumerating-tms.tex:48-74` → `bn-Beng-IN/content/turing-machines/undecidability/enumerating-tms.tex:52`; final reader page pending
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

### BN-IN-T215

- Source term or concept: one-way infinite tape; two-way infinite tape; multiple tapes; binary representation; simulate; extensionally equivalent
- Chosen Bengali: একমুখী অসীম ফিতা; দ্বিমুখী অসীম ফিতা; একাধিক ফিতা; দ্বিমিক উপস্থাপনা; অনুকরণ করে; বহির্বিস্তারণগতভাবে সমতুল্য
- Rationale: The simulation paragraph governs the tape variants: even and odd squares encode two tracks or positive and negative halves, so the one-tape one-way model can simulate the alternatives. দ্বিমিক উপস্থাপনা contrasts with T209’s unary encoding. T170 supplies অনুকরণ, while বহির্বিস্তারণগতভাবে সমতুল্য states that all models compute exactly the same function class and supports the Church--Turing thesis.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-equivalent-machine-model-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘একমুখী অসীম ফিতা; দ্বিমুখী অসীম ফিতা; একাধিক ফিতা; দ্বিমিক উপস্থাপনা; অনুকরণ করে; বহির্বিস্তারণগতভাবে সমতুল্য’ express the OpenLogic sense(s) ‘one-way infinite tape; two-way infinite tape; multiple tapes; binary representation; simulate; extensionally equivalent’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 9 occurrence(s). Representative locations:
  - `OLP-0247` `upstream/content/computability/computability-theory/total.tex:24-39` → `bn-Beng-IN/content/computability/computability-theory/total.tex:36`; final reader page pending
  - `OLP-0263` `upstream/content/turing-machines/machines-computations/church-turing-thesis.tex:12-21` → `bn-Beng-IN/content/turing-machines/machines-computations/church-turing-thesis.tex:17`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:62-65` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:62`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:72-82` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:70`; final reader page pending
  - `OLP-0262` `upstream/content/turing-machines/machines-computations/variants.tex:72-82` → `bn-Beng-IN/content/turing-machines/machines-computations/variants.tex:71`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
To see that $\fn{Tot}$ is not computable, it suffices to show that $K$
is reducible to it. Let $h(x,y)$ be defined by
\[
h(x,y) \simeq
\begin{cases}
0 & \text{if $x \in K$} \\
\fundefined & \text{otherwise}
\end{cases}
\]
Note that $h(x,y)$ does not depend on $y$ at all. It should
not be hard to see that $h$~is partial computable: on input $x, y$, the
we compute~$h$ by first simulating the function~$\cfind{x}$ on input~$x$; if
this computation halts, $h(x,y)$ outputs $0$ and halts. So
$h(x,y)$ is just $\Zero(\umin{s}{T(x,x,s)})$, where $\Zero$ is the constant zero
function.
```

### BN-IN-T216

- Source term or concept: effective procedure; Church--Turing thesis; pseudo-code; invoke the thesis; effectively unsolvable
- Chosen Bengali: কার্যকর পদ্ধতি; চার্চ--টুরিং থিসিস; ছদ্ম-কোড; থিসিস আহ্বান করে; কার্যকরভাবে অসমাধানযোগ্য
- Rationale: T170 fixes the thesis name and machine-model relation. The chapter distinguishes its two uses: a described কার্যকর পদ্ধতি or ছদ্ম-কোড licenses existence of a machine without drawing it, while a machine impossibility plus the thesis establishes that no effective procedure exists. থিসিস is retained consistently with the earlier Computability chapter.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-church-turing-use-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘কার্যকর পদ্ধতি; চার্চ--টুরিং থিসিস; ছদ্ম-কোড; থিসিস আহ্বান করে; কার্যকরভাবে অসমাধানযোগ্য’ express the OpenLogic sense(s) ‘effective procedure; Church--Turing thesis; pseudo-code; invoke the thesis; effectively unsolvable’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 25 occurrence(s). Representative locations:
  - `OLP-0223` `upstream/content/computability/recursive-functions/non-pr-functions.tex:81-86` → `bn-Beng-IN/content/computability/recursive-functions/non-pr-functions.tex:81`; final reader page pending
  - `OLP-0223` `upstream/content/computability/recursive-functions/non-pr-functions.tex:88-96` → `bn-Beng-IN/content/computability/recursive-functions/non-pr-functions.tex:87`; final reader page pending
  - `OLP-0156` `upstream/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:13-23` → `bn-Beng-IN/content/first-order-logic/syntax-and-semantics/formation-sequences.tex:15`; final reader page pending
  - `OLP-0060` `upstream/content/propositional-logic/syntax-and-semantics/formation-sequences.tex:13-18` → `bn-Beng-IN/content/propositional-logic/syntax-and-semantics/formation-sequences.tex:15`; final reader page pending
  - `OLP-0263` `upstream/content/turing-machines/machines-computations/church-turing-thesis.tex:9-10` → `bn-Beng-IN/content/turing-machines/machines-computations/church-turing-thesis.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{tagblock}{TMs}
\begin{digress}
You may already be convinced that (with some work!) one can write a
program (say, in Java or C++) that does this; and now we can appeal to
the Church--Turing thesis, which says that anything that, intuitively,
is computable can be computed by a Turing machine.
```

### BN-IN-T217

- Source term or concept: undecidability; uncomputable function; effectively decide a yes/no question; decision problem
- Chosen Bengali: অনির্ণেয়তা; অগণনসাধ্য অপেক্ষক; হ্যাঁ/না প্রশ্ন কার্যকরভাবে নির্ণয় করে; সিদ্ধান্ত সমস্যা
- Rationale: T091 and T184 already fix নির্ণেয় for decidable, while T174 and T182 fix the halting-problem family. The chapter introduction governs the negatives: an অগণনসাধ্য অপেক্ষক has no Turing computation, and an অনির্ণেয় yes/no problem has no total effective zero-one decision procedure. সিদ্ধান্ত সমস্যা retains the historical name for first-order validity.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-undecidability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অনির্ণেয়তা; অগণনসাধ্য অপেক্ষক; হ্যাঁ/না প্রশ্ন কার্যকরভাবে নির্ণয় করে; সিদ্ধান্ত সমস্যা’ express the OpenLogic sense(s) ‘undecidability; uncomputable function; effectively decide a yes/no question; decision problem’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 28 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:51-58` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:57`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:40`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:32-34` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{digress}
So, it turns out that all the examples of computably enumerable sets
that we have considered so far are either computable, or complete.
This should seem strange!{} Are there any examples of computably
enumerable sets that are neither computable nor complete? The answer
is yes, but it wasn't until the middle of the 1950s that this was
established by Friedberg and Muchnik, independently.
\end{digress}
```

### BN-IN-T218

- Source term or concept: enumerate Turing machines; standard machine; rename states and symbols; finite integer description
- Chosen Bengali: টুরিং যন্ত্র তালিকায়িত করে; মানক যন্ত্র; দশা ও প্রতীকের নতুন নাম দেয়; পূর্ণসংখ্যার সসীম বর্ণনা
- Rationale: T040 supplies তালিকায়ন and the source's finite coding construction controls the specialized register. মানক যন্ত্র means one whose states and alphabet symbols are positive integers; state/symbol renaming preserves behavior, and a finite list records the sets, start state and transition quintuples. The source footnote itself warns that the label standard machine is local terminology.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-machine-enumeration-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘টুরিং যন্ত্র তালিকায়িত করে; মানক যন্ত্র; দশা ও প্রতীকের নতুন নাম দেয়; পূর্ণসংখ্যার সসীম বর্ণনা’ express the OpenLogic sense(s) ‘enumerate Turing machines; standard machine; rename states and symbols; finite integer description’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 3 occurrence(s). Representative locations:
  - `OLP-0266` `upstream/content/turing-machines/undecidability/enumerating-tms.tex:79-90` → `bn-Beng-IN/content/turing-machines/undecidability/enumerating-tms.tex:86`; final reader page pending
  - `OLP-0266` `upstream/content/turing-machines/undecidability/enumerating-tms.tex:79-90` → `bn-Beng-IN/content/turing-machines/undecidability/enumerating-tms.tex:87`; final reader page pending
  - `OLP-0266` `upstream/content/turing-machines/undecidability/enumerating-tms.tex:92-106` → `bn-Beng-IN/content/turing-machines/undecidability/enumerating-tms.tex:94`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\path (A) edge [bend left] node {\TMtrans{3}{3}{\TMright}} (B)
(B) edge [loop above] node {\TMtrans{2}{2}{\TMright}} (B)
edge [bend left] node {\TMtrans{3}{3}{\TMright}} (A);
\end{tikzpicture}
\]
\caption{A standard \emph{Even} machine}
\ollabel{fig:standard-even}
\end{figure}
We might call a Turing machine with states and symbols that are
positive integers a \emph{standard} machine, and only consider
standard machines from now on.\footnote{The terminology ``standard
machine'' is not standard.}
```

### BN-IN-T219

- Source term or concept: Turing-machine index; fixed enumeration; machine description; encode/decode an index
- Chosen Bengali: টুরিং-যন্ত্রের সূচক; স্থির তালিকায়ন; যন্ত্রের বর্ণনা; সূচক সংকেতায়িত/বিসংকেতায়িত করে
- Rationale: The definition e indexes the e-th description in a fixed effective enumeration and permits duplicate indices for reordered instruction lists. সূচক continues the program-index vocabulary of T175 and T193; বর্ণনা names the finite integer sequence, while সংকেতায়ন and বিসংকেতায়ন distinguish converting to and recovering from its numeric code.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-turing-index-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘টুরিং-যন্ত্রের সূচক; স্থির তালিকায়ন; যন্ত্রের বর্ণনা; সূচক সংকেতায়িত/বিসংকেতায়িত করে’ express the OpenLogic sense(s) ‘Turing-machine index; fixed enumeration; machine description; encode/decode an index’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 7 occurrence(s). Representative locations:
  - `OLP-0232` `upstream/content/computability/computability-theory/s-m-n.tex:30-41` → `bn-Beng-IN/content/computability/computability-theory/s-m-n.tex:34`; final reader page pending
  - `OLP-0266` `upstream/content/turing-machines/undecidability/enumerating-tms.tex:124-135` → `bn-Beng-IN/content/turing-machines/undecidability/enumerating-tms.tex:120`; final reader page pending
  - `OLP-0268` `upstream/content/turing-machines/undecidability/halting-problem.tex:12-16` → `bn-Beng-IN/content/turing-machines/undecidability/halting-problem.tex:13`; final reader page pending
  - `OLP-0268` `upstream/content/turing-machines/undecidability/halting-problem.tex:12-16` → `bn-Beng-IN/content/turing-machines/undecidability/halting-problem.tex:14`; final reader page pending
  - `OLP-0268` `upstream/content/turing-machines/undecidability/halting-problem.tex:128-136` → `bn-Beng-IN/content/turing-machines/undecidability/halting-problem.tex:127`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
It is helpful to think of $s^m_n$ as acting on \emph{programs}. That
is, $s^m_n$ takes a program~$e$ for an $(m+n)$-ary function, as well
as fixed inputs $a_0$, \dots, $a_{m-1}$; and it returns a program
$s^m_n(x, a_0, \dots, a_{m-1})$ for the $n$-ary function of the
remaining arguments. \iftag{TMs}{It you think of $x$ as the description of a
Turing machine, then $s^m_n(e, a_0, \dots, a_{m-1})$ is the Turing
machine that, on input $y_0$, \dots,~$y_{n-1}$, prepends
$a_0$, \dots,~$a_{m-1}$ to the input string, and runs~$e$. Each $s^m_n$
is then just a primitive recursive function that finds a code for the
appropriate Turing machine.}{}
\end{explain}
```

### BN-IN-T220

- Source term or concept: universal Turing machine; simulate an indexed machine; current state; current head position; encoded tape
- Chosen Bengali: সার্বজনীন টুরিং যন্ত্র; সূচকযুক্ত যন্ত্র অনুকরণ করে; বর্তমান দশা; বর্তমান হেডের অবস্থান; সংকেতায়িত ফিতা
- Rationale: The theorem and its stepwise simulation control these terms. A single সার্বজনীন টুরিং যন্ত্র decodes e, stores the simulated current state and head counter, encodes each simulated tape symbol by its unary code number, and reproduces M_e's halting and numeric output behavior. অনুকরণ continues T170 and T215 without suggesting that one machine is the value computed by another.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-universal-machine-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সার্বজনীন টুরিং যন্ত্র; সূচকযুক্ত যন্ত্র অনুকরণ করে; বর্তমান দশা; বর্তমান হেডের অবস্থান; সংকেতায়িত ফিতা’ express the OpenLogic sense(s) ‘universal Turing machine; simulate an indexed machine; current state; current head position; encoded tape’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 6 occurrence(s). Representative locations:
  - `OLP-0257` `upstream/content/turing-machines/machines-computations/configuration.tex:25-38` → `bn-Beng-IN/content/turing-machines/machines-computations/configuration.tex:35`; final reader page pending
  - `OLP-0254` `upstream/content/turing-machines/machines-computations/introduction.tex:29-53` → `bn-Beng-IN/content/turing-machines/machines-computations/introduction.tex:39`; final reader page pending
  - `OLP-0267` `upstream/content/turing-machines/undecidability/universal-tm.tex:9-10` → `bn-Beng-IN/content/turing-machines/undecidability/universal-tm.tex:10`; final reader page pending
  - `OLP-0267` `upstream/content/turing-machines/undecidability/universal-tm.tex:89-94` → `bn-Beng-IN/content/turing-machines/undecidability/universal-tm.tex:82`; final reader page pending
  - `OLP-0267` `upstream/content/turing-machines/undecidability/universal-tm.tex:96-121` → `bn-Beng-IN/content/turing-machines/undecidability/universal-tm.tex:90`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{defn}[Configuration]
A \emph{configuration} of Turing machine $M = \tuple{Q, \Sigma, q_0,
\delta}$ is a triple $\tuple{C, m, q}$ where
\begin{enumerate}
\item $C \in \Sigma^*$ is a finite sequence of symbols from $\Sigma$,
\item $m \in \Nat$ is a number $< \len{C}$, and
\item $q \in Q$
\end{enumerate}
Intuitively, the sequence~$C$ is the content of the tape (symbols of
all squares from the leftmost square to the last non-blank or
previously visited square), $m$~is the number of the square the
read/write head is scanning (beginning with $0$ being the number of
the leftmost square), and $q$ is the current state of the machine.
\end{defn}
```

### BN-IN-T221

- Source term or concept: halting function; halting problem; diagonal self-input function; unsolvability
- Chosen Bengali: থামা-অপেক্ষক; থামার সমস্যা; কর্ণীয় স্ব-নিবেশ অপেক্ষক; অসমাধানযোগ্যতা
- Rationale: T174 and T182 govern the established halting vocabulary. The total হ function returns one exactly for a halting index-input pair, while s specializes the input to the machine's own index and drives the two-case contradiction. অসমাধানযোগ্যতা states the absence of a total decision procedure, while the later s-prime exercise remains partial and computable.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-machine-halting-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘থামা-অপেক্ষক; থামার সমস্যা; কর্ণীয় স্ব-নিবেশ অপেক্ষক; অসমাধানযোগ্যতা’ express the OpenLogic sense(s) ‘halting function; halting problem; diagonal self-input function; unsolvability’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 31 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:12`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:113-133` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:115`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:9-10` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:10`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Let's consider the halting problem again. As temporary
notation, let us write $\gn{\cfind{x}(y)}$ for $\tuple{x, y}$; think of
this as representing a ``name'' for the value $\cfind{x}(y)$. With this
notation, we can reword one of our proofs that the halting problem is
undecidable.
```

### BN-IN-T222

- Source term or concept: hook machines together; copier machine; Three Halting problem; partial halting recognizer
- Chosen Bengali: যন্ত্র জুড়ে দেয়; অনুলিপিকারী যন্ত্র; তিন-থামা সমস্যা; আংশিক থামা-স্বীকর্তা
- Rationale: T213 supplies the formal machine-combination construction. The diagonal proof জুড়ে দেয় a disciplined s-machine with a machine that halts only on zero; the theorem uses an অনুলিপিকারী যন্ত্র to duplicate e. তিন-থামা preserves the exercise's fixed three-stroke input, and the partial recognizer distinguishes semidecision by halting only in the positive case.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-halting-reduction-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘যন্ত্র জুড়ে দেয়; অনুলিপিকারী যন্ত্র; তিন-থামা সমস্যা; আংশিক থামা-স্বীকর্তা’ express the OpenLogic sense(s) ‘hook machines together; copier machine; Three Halting problem; partial halting recognizer’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 2 occurrence(s). Representative locations:
  - `OLP-0268` `upstream/content/turing-machines/undecidability/halting-problem.tex:103-113` → `bn-Beng-IN/content/turing-machines/undecidability/halting-problem.tex:103`; final reader page pending
  - `OLP-0268` `upstream/content/turing-machines/undecidability/halting-problem.tex:115-120` → `bn-Beng-IN/content/turing-machines/undecidability/halting-problem.tex:112`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{proof}
Suppose $h$ were Turing computable, say, by a Turing machine~$H$. We
could use $H$ to build a Turing machine that computes~$s$: First, make
a copy of the input (separated by a~$\TMblank$ symbol). Then move back
to the beginning, and run~$H$.  We can clearly make a machine that
does the former (see \cref{tur:mac:dis:prob:copier}), and if $H$
existed, we would be able to ``hook it up'' to such a copier machine
to get a new machine which would determine if $M_e$ halts on
input~$e$, i.e., computes~$s$. But we've already shown that no such
machine can exist. Hence, $h$~is also not Turing computable.
\end{proof}
```

### BN-IN-T223

- Source term or concept: validity decision problem; validity function; reduce the halting problem; machine-configuration sentences
- Chosen Bengali: সিদ্ধতার সিদ্ধান্ত সমস্যা; সিদ্ধতা-অপেক্ষক; থামার সমস্যাকে হ্রাস করে; যন্ত্র-কনফিগারেশনের বাক্য
- Rationale: T032 and T217 govern validity and decision terminology. The reduction assumes a total সিদ্ধতা-অপেক্ষক and would use it on the effectively produced implication T(M,w) lif E(M,w) to compute the halting function. The two named sentences begin the later encoding of machine instructions, input and eventual halting into first-order logic.
- Plausible alternatives: No distinct alternative was recorded contemporaneously; this retrospective backfill does not invent one.
- Status: provisional-entscheidungsproblem-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘সিদ্ধতার সিদ্ধান্ত সমস্যা; সিদ্ধতা-অপেক্ষক; থামার সমস্যাকে হ্রাস করে; যন্ত্র-কনফিগারেশনের বাক্য’ express the OpenLogic sense(s) ‘validity decision problem; validity function; reduce the halting problem; machine-configuration sentences’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 1 occurrence(s). Representative locations:
  - `OLP-0269` `upstream/content/turing-machines/undecidability/decision-problem.tex:17-26` → `bn-Beng-IN/content/turing-machines/undecidability/decision-problem.tex:22`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In order to establish this important negative result, we prove that
the decision problem cannot be solved by a Turing machine.  That is,
we show that there is no Turing machine which, whenever it is started
on a tape that contains a first-order !!{sentence}, eventually halts
and outputs either $1$ or~$0$ depending on whether the
!!{sentence} is valid or not. By the Church--Turing thesis, every
function which is computable is Turing computable. So if this
``validity function'' were effectively computable at all, it would be
Turing computable. If it isn't Turing computable, then, it also cannot
be effectively computable.
```

### BN-IN-T224

- Source term or concept: first-order machine language; numeral; instant; state; tape symbol
- Chosen Bengali: প্রথম-ক্রমের যুক্তিবিদ্যা; সংখ্যাপদ; মুহূর্ত; দশা; ফিতা-প্রতীক
- Rationale: The representation uses a first-order language whose numerals name both tape squares and computation instants, with indexed binary predicates for machine states and tape symbols. সংখ্যাপদ retains the numeral-as-term distinction, মুহূর্ত marks the time coordinate, and দশা plus ফিতা-প্রতীক continue the established machine vocabulary.
- Plausible alternatives: প্রথম-স্তরের যুক্তিবিদ্যা was considered for first-order logic; প্রথম-ক্রমের যুক্তিবিদ্যা continues the established edition term. সংখ্যা-নাম was considered for numeral; সংখ্যাপদ makes its syntactic category explicit. কালক্ষণ was considered for instant; মুহূর্ত follows the source explanation while the formulas supply the discrete-step sense.
- Status: provisional-first-order-machine-encoding-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘প্রথম-ক্রমের যুক্তিবিদ্যা; সংখ্যাপদ; মুহূর্ত; দশা; ফিতা-প্রতীক’ express the OpenLogic sense(s) ‘first-order machine language; numeral; instant; state; tape symbol’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 216 occurrence(s). Representative locations:
  - `OLP-0230` `upstream/content/computability/computability-theory/coding-computations.tex:12-31` → `bn-Beng-IN/content/computability/computability-theory/coding-computations.tex:19`; final reader page pending
  - `OLP-0174` `upstream/content/first-order-logic/beyond/beyond.tex:8-8` → `bn-Beng-IN/content/first-order-logic/beyond/beyond.tex:8`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:13-19` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:13`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:13`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:13-21` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:19`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In every model of computation, it is possible to do the following:
\begin{enumerate}
\item Describe the \emph{definitions} of computable functions in a
  systematic way. For instance, you can think of Turing machine
  specifications, recursive definitions, or programs in a programming
  language as providing these definitions.
\item Describe the complete record of the computation of a function
  given by some definition for a given input. For instance, a Turing
  machine computation can be described by the sequence of
  configurations (state of the machine, contents of the tape) for each
  step of computation.
\item Test whether a putative record of a computation is in fact the
  record of how a computable function with a given definition would be
  computed for a given input (on which the function is
  defined, i.e., the computation halts).
\item Extract from such a description of the complete record of a
  computation the value of the function for a given input. For
  instance, the contents of the tape in the very last step of a
  halting Turing machine computation is the value.
\end{enumerate}
```

### BN-IN-T225

- Source term or concept: machine-description axioms; initial configuration; transition; halting configuration; frame condition
- Chosen Bengali: স্বতঃসিদ্ধ; আরম্ভিক কনফিগারেশন; অবস্থান্তর; থামার কনফিগারেশন; অপরিবর্তনশীলতার শর্ত
- Rationale: T(M,w) combines arithmetic-order axioms, an initial-configuration description, transition clauses and conditions preserving every tape square not written at that step. অবস্থান্তর names the configuration change, while অপরিবর্তনশীলতার শর্ত states the role of the source's frame formula without importing an unexplained English loan.
- Plausible alternatives: যন্ত্র-বর্ণনা বাক্যসমষ্টি was considered for the axiom package; স্বতঃসিদ্ধ follows the source presentation. রূপান্তর was considered for transition; অবস্থান্তর keeps the change between configurations explicit. ফ্রেম-শর্ত was considered; অপরিবর্তনশীলতার শর্ত states that all unscanned tape squares keep their symbols.
- Status: provisional-machine-description-axiom-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বতঃসিদ্ধ; আরম্ভিক কনফিগারেশন; অবস্থান্তর; থামার কনফিগারেশন; অপরিবর্তনশীলতার শর্ত’ express the OpenLogic sense(s) ‘machine-description axioms; initial configuration; transition; halting configuration; frame condition’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 240 occurrence(s). Representative locations:
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:18-20` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:21`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:50-53` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:52`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:9`; final reader page pending
  - `OLP-0112` `upstream/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:8-10` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axiomatic-deduction.tex:10`; final reader page pending
  - `OLP-0114` `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13-13` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex:13`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
  \emph{Conclusion:} There is no such set~$S$. Assuming the existence of a
  ``set of all sets'' is inconsistent with the other axioms of set
  theory.
```

### BN-IN-T226

- Source term or concept: verification of the representation; induction over computation steps; run; reverse direction
- Chosen Bengali: উপস্থাপনের যাচাই; আরোহ; চালনা; বিপরীত দিক
- Rationale: The forward proof uses induction over the actual run through its first halting configuration, while the reverse proof interprets the predicates in a canonical natural-number structure built from that run. আরোহ continues the established induction term, চালনা names the machine run, and বিপরীত দিক identifies the converse implication.
- Plausible alternatives: প্রতিনিধিত্বের সত্যতা-পরীক্ষা was considered; উপস্থাপনের যাচাই follows the section heading and the two implication proofs. আবর্তনের উপর আরোহ was considered, but চালনার ধাপগুলির উপর আরোহ states the induction parameter directly. বিপরীত অভিমুখ was considered; বিপরীত দিক is idiomatic and fixed by the converse implication.
- Status: provisional-machine-verification-proof-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘উপস্থাপনের যাচাই; আরোহ; চালনা; বিপরীত দিক’ express the OpenLogic sense(s) ‘verification of the representation; induction over computation steps; run; reverse direction’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 226 occurrence(s). Representative locations:
  - `OLP-0242` `upstream/content/computability/computability-theory/complement-ce.tex:28-42` → `bn-Beng-IN/content/computability/computability-theory/complement-ce.tex:27`; final reader page pending
  - `OLP-0251` `upstream/content/computability/computability-theory/def-functions-self-reference.tex:34-47` → `bn-Beng-IN/content/computability/computability-theory/def-functions-self-reference.tex:48`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:74-81` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:78`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:149-162` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:159`; final reader page pending
  - `OLP-0120` `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:18-20` → `bn-Beng-IN/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex:20`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
In the other direction, suppose $A$ and~$\Complement{A}$ are both
computably enumerable. Let $A$ be the domain of~$\cfind{d}$, and let
$\Complement{A}$ be the domain of~$\cfind{e}$. Define $h$ by
\[
h(x) = \umin{s}{(T(d,x,s) \lor T(e,x,s))}.
\]
In other words, on input~$x$, $h$~searches for either a halting
computation of~$\cfind{d}$ or a halting computation of~$\cfind{e}$.
Now, if $x \in A$, it will succeed in the first case, and if $x \in
\Complement{A}$, it will succeed in the second case. So, $h$~is a
total computable function. But now we have that for every~$x$, $x \in
A$ if and only if $T(e, x, h(x))$, i.e., if $\cfind{e}$ is the one
that is defined. Since $T(e, x, h(x))$ is a computable relation,
$A$~is computable.
\end{proof}
```

### BN-IN-T227

- Source term or concept: semidecidable validity; effective enumeration of derivations; soundness; completeness
- Chosen Bengali: অর্ধ-নির্ণেয়; কার্যকর অ্যালগরিদম; নিগমন; যথার্থতা; সম্পূর্ণতা
- Rationale: The recognizer systematically generates possible derivations and halts on a proof of B. যথার্থতা supplies the positive direction and সম্পূর্ণতা guarantees eventual discovery for every valid sentence; অর্ধ-নির্ণেয় records that invalid inputs may run forever.
- Plausible alternatives: আংশিক নির্ণেয় was considered for semidecidable; অর্ধ-নির্ণেয় keeps the recognized technical contrast with a total decision procedure. প্রমাণ was considered for derivation, but নিগমন preserves the formal proof-object vocabulary. শুদ্ধতা was considered for soundness; যথার্থতা continues the edition term paired with সম্পূর্ণতা.
- Status: provisional-semidecision-proof-enumeration-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অর্ধ-নির্ণেয়; কার্যকর অ্যালগরিদম; নিগমন; যথার্থতা; সম্পূর্ণতা’ express the OpenLogic sense(s) ‘semidecidable validity; effective enumeration of derivations; soundness; completeness’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 39 occurrence(s). Representative locations:
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:40`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:203-208` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:205`; final reader page pending
  - `OLP-0178` `upstream/content/first-order-logic/beyond/higher-order-logic.tex:102-112` → `bn-Beng-IN/content/first-order-logic/beyond/higher-order-logic.tex:112`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:186-198` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:173`; final reader page pending
  - `OLP-0176` `upstream/content/first-order-logic/beyond/many-sorted-logic.tex:44-64` → `bn-Beng-IN/content/first-order-logic/beyond/many-sorted-logic.tex:68`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{explain}
The first three clauses say that we can equivalently take any non-empty
computably enumerable set to be enumerated by either a computable
function, a partial computable function, or a primitive recursive
function. The fourth clause tells us that if $S$ is computably
enumerable, then for some index~$e$,
\[
S = \Setabs{x}{\cfind{e}(x) \fdefined}.
\]
In other words, $S$ is the set of inputs on for which the computation
of $\cfind{e}$ halts. For that reason, computably enumerable sets are
sometimes called \emph{semi-decidable}: if a number is in the set, you
eventually get a ``yes,'' but if it isn't, you never get a ``no''!{}
\end{explain}
```

### BN-IN-T228

- Source term or concept: Trakhtenbrot's theorem; finite satisfiability; finite validity; finite model; positive time
- Chosen Bengali: ট্রাখতেনব্রোটের উপপাদ্য; সসীম সন্তোষণীয়তা; সসীম সিদ্ধতা; সসীম মডেল; ধনাত্মক সময়
- Rationale: The reduction strengthens the machine description so every positive computation time is distinct, making a finite model possible exactly for a halting run. The theorem rules out a decider for finite satisfiability, and its corollary rules out a sound and complete derivation system for finite validity.
- Plausible alternatives: ট্রাখটেনব্রোটের and ট্রাখতেনব্রটের are transliteration alternatives; ট্রাখতেনব্রোটের follows the selected Bengali rendering. সসীম পরিতৃপ্তিযোগ্যতা was considered; সসীম সন্তোষণীয়তা follows the immediate chapter vocabulary. সসীম বৈধতা was considered; সসীম সিদ্ধতা keeps validity distinct from satisfaction.
- Status: provisional-finite-model-undecidability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘ট্রাখতেনব্রোটের উপপাদ্য; সসীম সন্তোষণীয়তা; সসীম সিদ্ধতা; সসীম মডেল; ধনাত্মক সময়’ express the OpenLogic sense(s) ‘Trakhtenbrot's theorem; finite satisfiability; finite validity; finite model; positive time’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 17 occurrence(s). Representative locations:
  - `OLP-0186` `upstream/content/model-theory/basics/overspill.tex:12-15` → `bn-Beng-IN/content/model-theory/basics/overspill.tex:13`; final reader page pending
  - `OLP-0186` `upstream/content/model-theory/basics/overspill.tex:35-40` → `bn-Beng-IN/content/model-theory/basics/overspill.tex:38`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:9-10` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:10`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:29-51` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:32`; final reader page pending
  - `OLP-0273` `upstream/content/turing-machines/undecidability/trakhtenbrot.tex:29-51` → `bn-Beng-IN/content/turing-machines/undecidability/trakhtenbrot.tex:49`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{thm}
\ollabel{overspill} If a set $\Gamma$ of sentences has arbitrarily
large finite models, then it has an infinite model.
\end{thm}
```

### BN-IN-T229

- Source term or concept: incompleteness theorem; historical background; mathematical logic; foundations of mathematics
- Chosen Bengali: অসম্পূর্ণতা উপপাদ্য; ঐতিহাসিক পটভূমি; গাণিতিক যুক্তিবিদ্যা; গণিতের ভিত্তি
- Rationale: The introduction frames the incompleteness results through an ঐতিহাসিক পটভূমি, distinguishes গাণিতিক যুক্তিবিদ্যা from the history of গণিতের ভিত্তি, and reserves অসম্পূর্ণতা উপপাদ্য for the qualified mathematical results developed in the part.
- Plausible alternatives: অসম্পূর্ণতার উপপাদ্য was considered as a fuller compound; অসম্পূর্ণতা উপপাদ্য follows the section heading and keeps the theorem name compact. ইতিহাস and পটভূমি were both considered; ঐতিহাসিক পটভূমি names the opening historical section.
- Status: provisional-incompleteness-history-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘অসম্পূর্ণতা উপপাদ্য; ঐতিহাসিক পটভূমি; গাণিতিক যুক্তিবিদ্যা; গণিতের ভিত্তি’ express the OpenLogic sense(s) ‘incompleteness theorem; historical background; mathematical logic; foundations of mathematics’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 28 occurrence(s). Representative locations:
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:203-208` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:205`; final reader page pending
  - `OLP-0181` `upstream/content/first-order-logic/beyond/other-logics.tex:22-36` → `bn-Beng-IN/content/first-order-logic/beyond/other-logics.tex:33`; final reader page pending
  - `OLP-0177` `upstream/content/first-order-logic/beyond/second-order-logic.tex:67-81` → `bn-Beng-IN/content/first-order-logic/beyond/second-order-logic.tex:76`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:62-69` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:62`; final reader page pending
  - `OLP-0274` `upstream/content/incompleteness/incompleteness.tex:9-14` → `bn-Beng-IN/content/incompleteness/incompleteness.tex:10`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
For now, it is o.k.\ if you want to think of the proof as formal
trickery, or black magic. But you should be able to reconstruct the
details of the argument given above. When we prove the incompleteness
theorems (and the related ``fixed-point theorem'') we will discuss
other ways of understanding why it works.
\end{explain}
```

### BN-IN-T230

- Source term or concept: theory; closure under entailment; true arithmetic; standard model
- Chosen Bengali: তত্ত্ব; অনুগমনের অধীনে আবদ্ধ; সত্য পাটিগণিতের; মানক মডেল
- Rationale: The definitions make a তত্ত্ব a set closed under অনুগমনের অধীনে আবদ্ধ, then define সত্য পাটিগণিতের from truth in the মানক মডেল. These terms keep semantic closure separate from an axiomatized presentation.
- Plausible alternatives: তত্ত্ব is retained for theory; মতবাদ was rejected because the passage fixes a deductive closure rather than a philosophical doctrine. সত্য পাটিগণিতের and মানক মডেল remain paired with the semantic definition.
- Status: provisional-incompleteness-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘তত্ত্ব; অনুগমনের অধীনে আবদ্ধ; সত্য পাটিগণিতের; মানক মডেল’ express the OpenLogic sense(s) ‘theory; closure under entailment; true arithmetic; standard model’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 278 occurrence(s). Representative locations:
  - `OLP-0228` `upstream/content/computability/computability-theory/computability-theory.tex:8-8` → `bn-Beng-IN/content/computability/computability-theory/computability-theory.tex:8`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:12`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:15`; final reader page pending
  - `OLP-0229` `upstream/content/computability/computability-theory/introduction.tex:29-39` → `bn-Beng-IN/content/computability/computability-theory/introduction.tex:27`; final reader page pending
  - `OLP-0236` `upstream/content/computability/computability-theory/russells-paradox.tex:18-20` → `bn-Beng-IN/content/computability/computability-theory/russells-paradox.tex:21`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\olchapter{cmp}{thy}{Computability Theory}
```

### BN-IN-T231

- Source term or concept: Robinson Q; Peano arithmetic; induction schema; axiomatized theory
- Chosen Bengali: রবিনসনের; পেয়ানো পাটিগণিত; আরোহ-ছক; স্বতঃসিদ্ধায়িত
- Rationale: রবিনসনের Q is introduced as a small arithmetic theory, while পেয়ানো পাটিগণিত extends it by every আরোহ-ছক instance; স্বতঃসিদ্ধায়িত names the resulting axiomatic presentation.
- Plausible alternatives: রবিনসনের তত্ত্ব was considered as a full Bengali label; রবিনসনের follows the source’s displayed Q name. আরোহ-প্রকল্প was rejected; আরোহ-ছক names the induction schema instances explicitly.
- Status: provisional-arithmetic-theory-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘রবিনসনের; পেয়ানো পাটিগণিত; আরোহ-ছক; স্বতঃসিদ্ধায়িত’ express the OpenLogic sense(s) ‘Robinson Q; Peano arithmetic; induction schema; axiomatized theory’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 26 occurrence(s). Representative locations:
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:33-35` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:35`; final reader page pending
  - `OLP-0168` `upstream/content/first-order-logic/models-theories/introduction.tex:37-47` → `bn-Beng-IN/content/first-order-logic/models-theories/introduction.tex:40`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:13-27` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:15`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:29-38` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:31`; final reader page pending
  - `OLP-0170` `upstream/content/first-order-logic/models-theories/theories.tex:40-57` → `bn-Beng-IN/content/first-order-logic/models-theories/theories.tex:42`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
We say that~$\Gamma$ is \emph{axiomatized by} a set of
sentences~$\Delta$ if $\Gamma$ is the closure of~$\Delta$.
\end{defn}
```

### BN-IN-T232

- Source term or concept: decidable; axiomatizable; computable procedure; undecidability
- Chosen Bengali: নির্ণেয়; স্বতঃসিদ্ধায়িত; গণনপদ্ধতি; অণির্ণেয়তা
- Rationale: The introduction distinguishes a নির্ণেয় set from an axiomatized or স্বতঃসিদ্ধায়িত theory, describes its গণনপদ্ধতি, and motivates the later অণির্ণেয়তা results. The terms are retained as the edition’s decision and computability vocabulary.
- Plausible alternatives: সিদ্ধান্তযোগ্য was considered for decidable; নির্ণেয় follows the established chapter wording. স্বতঃসিদ্ধায়িত and অণির্ণেয়তা remain distinct: the first describes an axiomatic presentation, while the second states failure of a decision procedure.
- Status: provisional-decidability-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘নির্ণেয়; স্বতঃসিদ্ধায়িত; গণনপদ্ধতি; অণির্ণেয়তা’ express the OpenLogic sense(s) ‘decidable; axiomatizable; computable procedure; undecidability’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 55 occurrence(s). Representative locations:
  - `OLP-0237` `upstream/content/computability/computability-theory/computable-sets.tex:29-30` → `bn-Beng-IN/content/computability/computability-theory/computable-sets.tex:28`; final reader page pending
  - `OLP-0239` `upstream/content/computability/computability-theory/equiv-ce-defs.tex:30-43` → `bn-Beng-IN/content/computability/computability-theory/equiv-ce-defs.tex:40`; final reader page pending
  - `OLP-0249` `upstream/content/computability/computability-theory/fixed-point-thm.tex:12-16` → `bn-Beng-IN/content/computability/computability-theory/fixed-point-thm.tex:15`; final reader page pending
  - `OLP-0235` `upstream/content/computability/computability-theory/halting-problem.tex:12-21` → `bn-Beng-IN/content/computability/computability-theory/halting-problem.tex:17`; final reader page pending
  - `OLP-0240` `upstream/content/computability/computability-theory/non-comp-set.tex:32-34` → `bn-Beng-IN/content/computability/computability-theory/non-comp-set.tex:32`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
Computable sets and relations are also called \emph{decidable}.
\end{defn}
```

### BN-IN-T233

- Source term or concept: independent sentence; Gödel sentence; provability; representation
- Chosen Bengali: স্বাধীন; গ্যোডেল বাক্য; প্রমাণযোগ্যতা; উপস্থাপন
- Rationale: The overview calls a sentence স্বাধীন when neither it nor its negation is provable, names the constructed example গ্যোডেল বাক্য, and uses প্রমাণযোগ্যতা and উপস্থাপন for the arithmetized proof predicate and its theory-relative role.
- Plausible alternatives: অমীমাংসিত was considered for independent; স্বাধীন is used because the definition is proof-theoretic. গ্যোডেল বাক্য is retained as the named constructed sentence, while প্রমাণযোগ্যতা and উপস্থাপন distinguish provability from representation.
- Status: provisional-incompleteness-proof-register; confidence: medium_definition_and_adjacent-canon_support; expert review welcome and open to correction: yes
- Review question: Please double-check: for India-standard university Bengali, does ‘স্বাধীন; গ্যোডেল বাক্য; প্রমাণযোগ্যতা; উপস্থাপন’ express the OpenLogic sense(s) ‘independent sentence; Gödel sentence; provability; representation’ without collision with adjacent logical or mathematical concepts?
- Exact occurrence index: `TRANSLATION_DECISION_OCCURRENCES.csv` contains all 55 occurrence(s). Representative locations:
  - `OLP-0245` `upstream/content/computability/computability-theory/complete-ce-sets.tex:51-58` → `bn-Beng-IN/content/computability/computability-theory/complete-ce-sets.tex:58`; final reader page pending
  - `OLP-0218` `upstream/content/computability/recursive-functions/bounded-minimization.tex:12-25` → `bn-Beng-IN/content/computability/recursive-functions/bounded-minimization.tex:18`; final reader page pending
  - `OLP-0209` `upstream/content/computability/recursive-functions/recursive-functions.tex:10-15` → `bn-Beng-IN/content/computability/recursive-functions/recursive-functions.tex:13`; final reader page pending
  - `OLP-0175` `upstream/content/first-order-logic/beyond/introduction.tex:23-44` → `bn-Beng-IN/content/first-order-logic/beyond/introduction.tex:27`; final reader page pending
  - `OLP-0179` `upstream/content/first-order-logic/beyond/intuitionistic-logic.tex:128-133` → `bn-Beng-IN/content/first-order-logic/beyond/intuitionistic-logic.tex:119`; final reader page pending
- Representative frozen-source wording (line-end whitespace omitted here; the machine indexes retain the exact text and block hash):

```tex
\begin{digress}
So, it turns out that all the examples of computably enumerable sets
that we have considered so far are either computable, or complete.
This should seem strange!{} Are there any examples of computably
enumerable sets that are neither computable nor complete? The answer
is yes, but it wasn't until the middle of the 1950s that this was
established by Friedberg and Muchnik, independently.
\end{digress}
```
