# অঙ্কবাচক সংখ্যা ও হিউমের নীতি: ছয় সম্পূর্ণ পাঠ

২০২৬-০৯-৩০; gpt-6.1-sol, ultra। OLP-0580–0585-এর সম্পূর্ণ স্থির ইংরেজি ও বাংলা পুনঃতুলিত; ইংরেজির পরিচয় 9620cc73f9c8e0ad003c514a5d3748f29611c4c0। পুরোনো BN-SRC-452–454 যথার্থ; নতুন806-এ তুলনা-প্রমাণের বাদ পড়া ধাপ এবং807-এ দ্বিতীয়-ক্রমের নীতির আনুষ্ঠানিক পরিধি মেরামত। মানব-পর্যালোচনা, সম্পূর্ণ নতুন reader বা প্রকাশনা সম্পন্ন হওয়ার দাবি নেই।

এই চ্যাটে সত্যিই পড়া P005 সংখ্যা, P007/P012 সেট-ক্রিয়া, P008/P009 বচন, P013/P014 সম্পর্ক, P017 প্রমাণ, P018 ক্ষেত্র, P023 চিত্রণ এবং P027/P028 সসীম/অসীম ও সসীম অঙ্কবাচক সংখ্যার রীতি ব্যবহৃত। P028-তে সসীম অঙ্কবাচক সংখ্যার নাম প্রত্যক্ষ; অসীম প্রাথমিক ordinal, Choice বা Hume-পদের পুরো বিশেষ নাম নয়। T408–411 সংজ্ঞা ও নিচের যুক্তিতে নিয়ন্ত্রিত। P012/P017/P027-এর ভুল সূত্র/উদাহরণ নেওয়া হয়নি।

## OLP-0580–0581: অধ্যায় ও কান্টরের নীতি

পাঁচ বিভাগের import ও chapter-hook সঠিক। সমরূপ সুক্রমবিন্যাসের একই ক্রমপ্রকার; কাঠামো না-রেখে কেবল bijection থাকলে সমসংখ্যক হওয়া—এই দুই তুলনা পৃথক। অঙ্কবাচকতা-অভিন্ন iff সমসংখ্যক কান্টরের নীতির চাহিদা; ওই চাহিদা দিয়েই সব সেটে পদটির অস্তিত্ব ধরে নেওয়া হয়নি। “সম্ভবত কান্টরই প্রথম” উৎসের সতর্ক ঐতিহাসিক কথন বজায়, নতুন priority-অনুসন্ধানে প্রথমত্ব প্রমাণের দাবি নেই। প্রাপ্তবয়স্ক সম্বোধন ও সম্পর্ক/অপেক্ষকের রীতি ফিরেছে।

## OLP-0582: ক্ষুদ্রতম ordinal, মোট অস্তিত্ব এবং comparison

সুক্রমিত A-র ordinal-প্রতিনিধি β আছে। {γ∈β+১:A≈γ} সূত্রে পৃথকীকরণে সেট এবং β তার সদস্য, তাই অশূন্য। তার ক্ষুদ্রতম γ আগের সব ordinal বাদ দেয়; β-র উপরের কোনও ordinal আরও ছোট হতে পারে না। পুরোনো452-র সীমাবদ্ধ সেটে ক্ষুদ্রতম নেওয়ার নির্দেশ তাই যথার্থ; সব প্রতিনিধির proper class-কে সেট ধরা নয়। γ≈A; γ-র নিচে δ সমসংখ্যক হলে transitivity of equinumerosity-তে A≈δ, ক্ষুদ্রতমতার বিরোধ। তাই γ নিজেই প্রাথমিক ordinal, card γ=γ। শূন্য A-তে γ=০ বৈধ।

প্রত্যেক A-তে এই ordinal-সংজ্ঞা মোট করতে সব সেটের সুক্রমবিন্যাস চাই। ZF-এ শুধু সুক্রমিত সেটে আংশিক সংজ্ঞা বৈধ; ZFC-তে সবার জন্য মোট। এটি অন্য কোনও Choice-বিহীন cardinal-ধারণা অসম্ভব বলে না। এখানে লেখকের বাছা প্রাথমিক-ordinal সংজ্ঞার কথা।

তিন তিরের composition κ=card A→A→B→λ=card B একৈক। কিন্তু সাধারণ ordinal-এ injection থেকে ordinal inequality মেলে না: ω+১→ω-তে শেষ সদস্য ω-কে০ এবং প্রতিটি n-কে n+১ পাঠালে bijection, অথচ ω+১>ω। BN-SRC-806 diagram-এর পরে missing ধাপ যোগ করেছে। E=ran j⊆λ, তার সদস্যতা-ক্রমের ordinal type ρ; e:ρ→E increasing onto। আবেশে ξ≤e(ξ): প্রত্যেক η<ξ-তে η≤e(η)<e(ξ), তাই ξ⊆e(ξ)। ρ>λ হলে e(λ) সংজ্ঞায়িত, কিন্তু λ≤e(λ)<λ—অসম্ভব; তাই ρ≤λ। j ও e-তে κ≈ρ; κ-র ক্ষুদ্রতমতার সংজ্ঞায় κ≤ρ≤λ। এই প্রমাণ শ্র্যোডার–বার্নস্টাইন ব্যবহার করে না।

অন্য দিক κ≤λ-তে inclusion এবং A/B-র bijection থেকে A-তে B-র একৈক চিত্রণ। A≈B হলে দুই ক্ষুদ্রতম প্রতিনিধি একই; প্রতিনিধি সমান হলে composition-এ A≈B। কঠোর cardinal comparison-এ inequality ও অসমতা একসঙ্গে। ফলে তিন দ্বিশর্ত সম্পূর্ণ। পরে দুই cardinal-এর ordinal order-এ বিপ্রতিসাম্য থেকে শ্র্যোডার–বার্নস্টাইন পাওয়ায় বৃত্ত নেই। এই পুনঃপ্রমাণ Replacement/Well-Ordering-নির্ভর; আগের স্বনির্ভর Zminus-প্রমাণের শক্তি আলাদা।

চিত্রের চার node, দুই inverse-bijection তির, উপরকার injection ও dashed composite মূল coordinates-এ আছে। এটি composition-এর schematic; missing inequality চিত্র একা প্রতিষ্ঠা করে না। বর্তমান সংস্করণের TeX-render ও দৃশ্যমান inspection পরে।

## OLP-0583: ZFC-র সঠিক স্বতঃসিদ্ধ

সদস্যভিত্তিক সমতা, সংযোগ, যুগল, ঘাত সেট, অসীমতা, ভিত্তি, সুক্রমবিন্যাস এবং পৃথকীকরণ/প্রতিস্থাপনের সব দৃষ্টান্ত। ZF-তে Choice নেই; এখানেই সুক্রমবিন্যাস যোগ। Choice iff Well-Ordering ফল পরে ZF-সাপেক্ষে; এই পাঠে পূর্ণ প্রমাণ দেওয়ার দাবি নেই। “বিস্তৃতিত্ব”, “ঘাতসেট” ও অসামঞ্জস্যপূর্ণ যুগলের শব্দ আগের রীতিতে ফিরেছে; কোনও স্বতঃসিদ্ধ বাদ/যোগ হয়নি।

## OLP-0584: সসীম, গণনীয় ও সমস্ত cardinal-এর শ্রেণি

ভিন্ন finite m,n-এ ছোটটি বড়টির যথার্থ উপসেট; bijection হলে বড়টি Dedekind-infinite, Nat ফলের বিরোধ। তাই finite ordinal-ই finite initial ordinal। পুরোনো453 যথার্থ: card A∉ω মানে A-র অঙ্কবাচকতা স্বাভাবিক সংখ্যা নয়, A নিজে স্বাভাবিক সংখ্যা নয় বলা মিথ্যা। Card A-র ordinal অসীমতা ও bijection-এ Dedekind-ধর্ম স্থানান্তরে তিন iff; global card পদ ও সাধারণ equivalence এখানে ZFC-প্রেক্ষাপটে। Choice ছাড়া intrinsic finite মানে কোনও n∈ω-র সমসংখ্যক, এবং infinite Dedekind-finite সেটের সম্ভাবনা আলাদা; আংশিক card পদ ব্যবহার করে অনির্দিষ্ট বস্তু চালানো হয়নি।

ω কোনও finite n-র সমসংখ্যক নয়, তাই least infinite initial ordinal। অসীম successor α=β+১-র β finite হলে α-ও finite, তাই β infinite; পুরোনো454-র যুক্তি ও ভুল reference অপসারণ যথার্থ। β≈β+১, card β≤β<α, তাই card α=card β<α: α initial নয়। ফলে infinite cardinal limit ordinal।

Enumerable-এ শূন্য, finite n এবং ω-র সমসংখ্যক তিন ক্ষেত্রই card A≤ω; বিপরীতে A-র ω-তে injection-এর range ω-র subset, increasing enumeration-এ finite বা ω-র সমসংখ্যক। মূলের referenced enumeration ফল প্রযোজ্য। ω≤κ≤ω-তে enumerable infinite cardinal কেবল ω।

X-র প্রত্যেক সদস্য cardinal হলে ⋃X ordinal। α∈⋃X-তে কোনও b∈X-তে α<b, তাই α-র b-তে injection আছে কিন্তু bijection নেই। b⊆⋃X। যদি α≈⋃X হত, তবে α<b≤⋃X এবং ⋃X-র α-তে bijection মিলে b-র α-তে injection; cardinal/initial-ordinal comparison-এর বিরোধ। তাই ⋃X-র কোনও ছোট ordinal সমসংখ্যক নয়, এটি cardinal। X খালি হলে ⋃X=০, একই ফল।

Cantor-র ঘাত-সেট ফল ও ওই সেটের cardinal অস্তিত্বে প্রতিটি cardinal-এর বড় cardinal। সব cardinal-এর সেট C ধরলে ⋃C cardinal এবং তার চেয়ে বড় b cardinal; b∈C-তে b⊆⋃C, আবার b>⋃C—বিরোধ। এটি proper-class ফল, cardinal-এর “সেটের cardinality” আগেই নির্দিষ্ট নয়।

## OLP-0585: হিউমের নীতির প্রকার ও পূর্ণ মডেল

প্রথম নীতিতে A/B সেট-নির্দেশক প্রথম-ক্রমের পদ; দ্বিতীয়টিতে F/G/R বিধেয় ও দ্বিপদী সম্পর্কের স্থান। প্রদর্শিত R-শর্তের প্রথম conjunct R-র উৎস F ও লক্ষ্য G-তে সীমাবদ্ধ করে; পরে প্রত্যেক F-এর ঠিক এক G এবং প্রত্যেক G-এর ঠিক এক F। তাই bijection ঠিক, শূন্য/শূন্যে খালি R-ও সত্য। শুধু F/G নামের সংখ্যা নয়, তাদের পূরণকারী বস্তুর সংখ্যা তুলনা—বাংলা বাক্যটি স্পষ্ট করা হয়েছে।

[Hume, Treatise ১.৩.১.৫](https://davidhume.org/texts/t/1/3/1)-র প্রাসঙ্গিক মূল অনুচ্ছেদ পড়া হয়েছে; প্রথম পুস্তক, তৃতীয় ভাগ, §১ locator যথার্থ এবং বাংলায় ফিরেছে। Frege §৬৩-র উল্লেখ স্থির উৎস থেকে তুলিত; ওই মূল বই নতুন করে পড়ার দাবি নেই।

পূর্ণ বিধেয়-ক্ষেত্র এবং একই object-domain-এ extension-map-সহ Basic Law V-তে Russell-বিরোধ; সীমিত comprehension/Henkin-ক্ষেত্রে একই নামমাত্র impredicativity থেকে সেই বিরোধ ধরে নেওয়া যায় না। BN-SRC-807 এই পরিধি আগের story-সংশোধনের সঙ্গে মিলিয়েছে। “সরল বোধসূত্র” সাধারণ উপলব্ধির অর্থ দিচ্ছিল; অনানুষ্ঠানিক ধর্মনির্দেশে সেট-গঠন রীতি ফিরেছে। প্রেডিকেটিভ পৃথক প্রকার এবং একই ক্ষেত্রের ইমপ্রেডিকেটিভ object-ফিরে-আসা—এই পাঠের নিজস্ব ব্যবহার বজায়; সব দার্শনিক ব্যবহারকে এক সংজ্ঞায় বাঁধার দাবি নেই।

পূর্ণ HP-র নির্মাণ: D=ω+১, সব একপদী বিধেয় P(D) এবং সব প্রয়োজনীয় relation P(Dⁿ)। #F সসীম হলে তার স্বাভাবিক সদস্যসংখ্যা, অসীম হলে ω। সব মান D-তে। D countable; তার দুই infinite subset-এ increasing enumeration ও প্রয়োজনে শেষ ω-বস্তুটিকে finite স্থানান্তরে মেলালে উভয় ω-র সমসংখ্যক। দুই finite subset-এর bijection iff সমান n; finite/infinite bijection নেই। তাই #F=#G iff F≈G। সব relation পূর্ণ হওয়ায় ওই bijection-গুলি উপলব্ধ। সব comprehension-ও পূর্ণ predicate domains-এ সত্য। এটি বাইরের সেটতত্ত্বে একটি মডেল, বাইরের তত্ত্বের সঙ্গততার স্বাধীন প্রমাণ নয়।

[Sean Walsh, Comparing Peano Arithmetic, Basic Law V, and Hume’s Principle, §১.২, মুদ্রিত পৃ. ৫](https://arxiv.org/pdf/1407.0436)-র প্রাসঙ্গিক সংজ্ঞা ও non-cardinal ordinal-এ পূর্ণ model পড়া হয়েছে; আমাদের D সেই সহজ উদাহরণ। পূর্ণ paper-পাঠ বা সীমিত hyperarithmetic subsystem-এর নতুন প্রমাণের দাবি নেই।

Finite object-domain m হলে পূর্ণ concepts-এ সমসংখ্যক শ্রেণি ০..m, মোট m+১টি; HP তাদের পৃথক abstract object চাইবে, কিন্তু object আছে m—অসম্ভব। পাঠের সরাসরি ধারায়ও #∅, #singleton এবং আগের finite distinct object-গুলির predicate-তে একে একে নতুন পৃথক object; প্রতি fixed finite ধাপে উপযুক্ত comprehension থাকলে ফল। এটি পূর্ণ semantics-এ অসীমতা, কোনও সীমিত relation-domain-এ অন্ধ generalization নয়। Modern Setabs G-তে Frege-সংজ্ঞার শেষ notation heuristic, first-order set-ধারণার বৈধ construction নয়; naive formation-এর সমস্যা বলেই সেটি শেষ হয়েছে।

## যাচাই ও সীমা

GPT6_SOL_REDO_CARDINALS_CHECK.json-এ ছয় বর্তমান target hash। তিন তিরের সীমিত composition,১২-position ordinal-subset enumeration, তিন-বস্তুর সব relation-এ ৩২,৭৬৮ প্রদর্শিত bijection-শর্ত,৬৪ concept-pair, ω+১→ω map-এর২১ prefix এবং৯ finite-domain class-বাধা পাস। সসীম পরীক্ষাকে পূর্ণ infinite cardinal/HP-model-এর প্রমাণ বলা হয়নি; সাধারণ যুক্তি উপরে পৃথক। বর্তমান সব722source-check পাস; নতুন reader, চিত্রের render, export, পূর্ণ script audit ও প্রকাশনা বাকি।
