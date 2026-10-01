# অঙ্কবাচক যোগ, গুণ ও ঘাত: চার সম্পূর্ণ পাঠ

২০২৬-০৯-৩০; gpt-6.1-sol, ultra। OLP-0586–0589-এর সম্পূর্ণ স্থির ইংরেজি ও বাংলা নতুন করে তুলিত; ইংরেজি পরিচয় 9620cc73f9c8e0ad003c514a5d3748f29611c4c0। পুরোনো BN-SRC-455–458 পুনঃপরীক্ষিত এবং যথার্থ। নতুন808–811-এ অনির্ধারিত rank-অনুশীলন, square-প্রমাণের ordertype-ধাপ, গুণের অসমাপ্ত অংশ এবং সসীম ভিত্তির দফা মেরামত। মানব-পর্যালোচনা, নতুন সম্পূর্ণ reader বা প্রকাশনার দাবি নেই।

এই চ্যাটে পড়া P005 সংখ্যা, P007/P012 সেট, P008/P009 বচন, P013/P014 সম্পর্ক, P017 প্রমাণ, P018 ক্ষেত্র, P023 চিত্রণ এবং P027/P028 সসীম/অসীম ও সসীম cardinal রীতি ব্যবহৃত। পুরো transfinite ক্রিয়া ও মানক ক্রমের নাম সংজ্ঞা-নিয়ন্ত্রিত; T413 নতুন প্রমাণে বাঁধা। T412-র arithmetic অংশ এখানে তুলিত, কিন্তু একই term-row-র cardinal-successor অংশ পরের590-এ বাকি; তাই সম্পূর্ণ row-টি fresh-reviewed বলে নতুন দাবি করা হয়নি। T414-র CH/aleph/beth অংশও পরের পাঠে। ভুল canon-সূত্র/উদাহরণ নেওয়া হয়নি।

## OLP-0586–0587: ক্রিয়া এবং অপেক্ষক-সেটের অস্তিত্ব

পাঁচ import ও chapter-hook সঠিক; CH ও fixed-point বিভাগ পরের unit। যোগ বিযুক্ত সংযোগের cardinal, গুণ কার্তেসীয় গুণফলের cardinal, ঘাত b→a মোট অপেক্ষকগুলির সেটের cardinal। শেষ দিকটি অপরিহার্য; a→b নিলে উল্টো ঘাত। সব সেট X/Y-তে অপেক্ষক-সেট Zminus-তেই আছে: X×Y সেট, তার ঘাত সেটে পৃথকীকরণে single-valued ও ঠিক X-domain/ Y-range-এর graph। Replacement বা সর্বজনীন set-collection দরকার নেই।

খালি X-তে একটিমাত্র খালি graph, তাই অপেক্ষক-সেটের rank১ এবং cardinal১; অশূন্য X ও খালি Y-তে কোনও graph নেই, rank/cardinal০। এই দুই case-তে০⁰=১ convention-ও পরিষ্কার। Nonempty X/Y-তে প্রতিটি graph X×Y-র subset; function-space⊆Pow(X×Y), তাই rank সর্বোচ্চ rank(X×Y)+১।

## OLP-0587: কেন দুই rank-এ এক উত্তর নেই

BN-SRC-808 মূলের অনুশীলন সংশোধন করেছে। λ=ω·২, Y=λ, X₀={ω} ও X₁=ω+১। দুই X-র rankω+১, Y-র rankλ একই। X₀ থেকে প্রত্যেক function-এর graph এক pair⟨ω,y⟩। y=γ<λ হলে pair-rank max(ω,γ)+২, graph-rank max(ω,γ)+৩<λ। ওই graph-rank-গুলি λ-তে সহশেষী; ফলে পুরো function-space-র rankλ।

X₁ থেকে কোনও function-এর pair-rankλ-র নিচে, তাই graph-rank≤λ। কিন্তু f(n)=ω+n, n∈ω, f(ω)=০-তে pair-rank-গুলি λ-তে সহশেষী, ফলে graph-rank ঠিকλ। Function-space-এ সেই graph সদস্য, অন্য graph-গুলির rank≤λ, তাই space-rankλ+১। একই দুই input-rank-এ ভিন্ন output-rank; একক formula চাওয়া ভুল। এখন exercise সম্ভাব্য সীমা ও দৃষ্টান্ত পরীক্ষা করে।

আরও সাধারণ পরিধি: nonempty X/Y-তে সব functions-এর graph-সংযোগ ঠিক X×Y; প্রত্যেক pair⟨x,y⟩ একটি constant-y function-এ থাকে। আগের union-rank ফল ও উপরকার bound থেকে r=rank(X×Y) উত্তরসূরি হলে space-rankr+১; r limit হলে spacerankr বাr+১। কোনটি হবে তা শুধু দুই input-rank নয়, পূর্ণ ক্ষেত্র/লক্ষ্যের গঠন ও উপলব্ধ সহশেষী image-র উপর নির্ভর করতে পারে।

## OLP-0587: বিনিময়, বন্ধনী ও characteristic function

বিযুক্ত যোগে চিহ্ন বদল এবং গুণে স্থানাঙ্ক বদলের bijection-এ বিনিময়। তিন tagged summand-কে এক একই তিনচিহ্ন-ক্ষেত্রে পাঠিয়ে, আর product-এ ⟨⟨x,y⟩,z⟩↔⟨x,⟨y,z⟩⟩-এ বন্ধনী বদললেও cardinal একই। “সম্বন্ধীয়” একা অস্পষ্ট ছিল; property-টি plain বাংলায় বন্ধনী বদলেও একই ফল হিসেবে লেখা হয়েছে। অসীম cardinal-এ এক নতুন সদস্য যোগেও bijection, finite ক্ষেত্রে নতুন সদস্যসংখ্যা সত্যিই এক বাড়ে; global set-কথনে ZFC প্রেক্ষাপট অক্ষত।

B⊆A-র characteristic map χB(x)=১ iff x∈B, অন্যথায়০; inverse-এ {x∈A:f(x)=১}। ফলে Pow(A)↔Fun(A,২) bijection, শূন্য A-ও অন্তর্ভুক্ত। A↔card A bijection দিয়ে domain পরিবহন করলে Fun(A,২)↔Fun(card A,২), তাই ঘাত-set cardinal২^(card A)। Cantor-র diagonal ফল strict বৃদ্ধি দেয়; ordinal২^ω=ω-এর সঙ্গে cardinal২^ω>ω আলাদা।

Continuum exercise-এর স্বাধীন পূর্ণ পথ: A⊆ω-কে বাস্তব f(A)=Σ(২·χA(n)/৩^(n+১)) পাঠাই। ভিন্ন A/B-র প্রথম ভিন্ন n-এ main difference২/৩^(n+১), বাকি সব পার্থক্য সর্বোচ্চ১/৩^(n+১); তাই total difference অশূন্য। অন্য দিকে একটি নির্দিষ্ট rational enumeration qn নিয়ে g(r)={n:qn<r}; r<s-র মাঝে rational থাকায় g(r)≠g(s)। দুই injections ও Schröder–Bernstein-এ Real≈Powω, তাই cardinal Real=২^ω। Binary expansion-এর দ্বৈত প্রকাশের সমস্যা এড়িয়ে ternary০/২ নেওয়া হয়েছে। এই proof source exercise-এর সমাধান নথিতে; frozen English বদলায়নি।

## OLP-0588: মানক square-ক্রম এবং least-counterexample

Pair-এর key(max(first,second),first,second)। অশূন্য subset-এ least max, সেই shell-এ least first, তারপর least second—তিনটি ordinal-minimum। Max-গুলির set চাইলে α-তে bounded Separation-ই যথেষ্ট। Key-এর প্রথম ভিন্ন স্থানে ordinal strict order-এ সংযুক্ততা, পরিযায়িতা ও অসাম্য; তাই well-order। Bijection f:α→β দুই স্থানাঙ্কে প্রয়োগ করলে square-bijection, inverse-ও দুই স্থানে f⁻¹।

Least infinite failure α-র card α ছোট হলে সেটিও infinite এবং আগের square identity-তে α-র ফল চলে আসবে; তাই α initial ordinal। ω-square enumeration-এ baseω সত্য, α>ω। Max coordinateγ<α-র পূর্বখণ্ড (γ+১)×(γ+১)-এর subset। γ finite হলে finite খণ্ড<α; পুরোনো455-র যোগ করা case যথার্থ। γ infinite হলে γ+১≈γ, squares সমসংখ্যক, least-failure অনুমানেγ×γ≈γ; α initial এবংγ<α-তে strict cardinal bound। উৎসের ordtimes-লেখা ওই Cartesian product-এর ordinal ordertype; তার cardinal-size পরিবহন বৈধ, কোনও নতুন ভুল product-ধরন নয়।

BN-SRC-809 শেষ inference স্পষ্ট: পুরো square-order typeρ>α হলে α-স্থানটির proper prefix-এর ordertypeα, cardinalওα। কিন্তু প্রতিটি proper prefix-এর cardinal<α—বিরোধ। তাইρ≤α; ordinal isomorphism ও inclusion-এ square→α injection। অন্য দিকে x↦⟨x,০⟩ injection; Schröder–Bernstein-এα≈α²। এই proof well-orderable ordinal-গুলির জন্য; স্বয়ং arbitrary Choice-বিহীন set-square identity দাবি নয়।

Infinite cardinals a≥b-তে displayed chain a≤a+b≤a+a≤a²=a যোগের ফল দেয়। BN-SRC-811 গুণের বাদ পড়া অংশ: b nonempty বলে নির্দিষ্টβ₀∈b-তে x↦⟨x,β₀⟩ injection a→a×b; a×b⊆a², তাই a≤a·b≤a²=a। দুই অসমতায় productওa।

Family union-এ প্রত্যেক Xβ→a injection-গুলি একসঙ্গে বাছতে family-choice দরকার; global ZFC-তেই করছি। Arbitrary a-তে এটি শুধু countable-choice বলা হয়নি। Family সেটে well-ordering/Choice এবং Replacement-এ injection-family রাখা যায়। v-র least β with v∈Xβ আছে; g(v)=⟨β,fβ(v)⟩। এক image হলেβ একই এবং fβ একৈকে v একই; তাই union→a² injection, square-sizea-তে bound। খালি union-ও খালি injection-এ বৈধ।

## OLP-0589: split, curry এবং সসীম ভিত্তির সূক্ষ্ম ধাপ

পুরোনো456 ঠিক: f-র দুই tagged restriction f_b/f_c একটি **ক্রমযুগল**, product-function f_b×f_c নয়। Inverse-এ দুই function-কে আলাদা tagged domains-এ জুড়ে দিই; empty domain/codomain case-ও bijection। পুরোনো457 ঠিক: f:c→Fun(b,a) থেকে f*(β,γ)=f(γ)(β)-র প্রকৃত domain b×c, cardinal product-number নয়। Inverse-এ প্রতিটিγ-র sliceβ↦h(β,γ); দুই mapping পরস্পর inverse। তারপর b×c-এর তার initial cardinal b·c-র সঙ্গে bijection দিয়ে domain পরিবহনে claimed exponent-law।

২≤a≤b, b infinite-তে base-monotonicity:২^b≤a^b≤(২^a)^b=২^(a·b)। শেষ a·b=b-তে উদ্ধৃত theorem-এর wording দুই factor infinite, অথচ a finiteও হতে পারে। BN-SRC-810 বিস্তৃত সত্যটি প্রমাণ করে: a≥১-তে fixed প্রথম সদস্যে b→a×b, আর a×b⊆b²; infinite b-তে b²≈b। তাই product=b, finite positive a-ও covered। মধ্যের a≤২^a-তে Cantor ও power-set correspondence; শুধু lemma-name-কে অযাচিত standalone দাবি নয়।

পুরোনো458-তে finite exponent n অবশ্যই **অশূন্য**। n=১ basea; successor-এ আগের infinite producta, তাই induction-এ প্রতিটি positive finite n-তে a^n=a। n=০-তে function-এর domain খালি, ফল১; source-এর বাদ পড়া guard সঠিকভাবে যুক্ত।

Infinite b এবং২≤b<a≤২^b-তে২^b≤a^b≤(২^b)^b=২^(b·b)=২^b, তাই শেষ equalityও যথার্থ। “আর সহজে কত হয় বলা যায় না” informal motivation; Cantor lower bound থেকে একা কোনও সব-formula অসম্ভাব্যতার theorem দাবি নয়। পরের CH/cofinality অংশ নতুন করে পড়া বাকি।

## যাচাই ও সীমা

GPT6_SOL_REDO_CARDINAL_ARITHMETIC_CHECK.json-এ চার current target hash।৬৪finite-HF function-space rank,১,৯০৬split ও২২,০৮০curry map/inverse case,১,০২৩characteristic map,১০,০০০canonical Nat-square pair/inverse এবং৪,০৯৬overlapping family-র least-index injection পাস। Infinite rank-counterexample, arbitrary cardinal square, continuum ও Choice-সংক্রান্ত সাধারণ proofs উপরে পৃথক; finite গণনা তাদের বিকল্প নয়। সব722source-check পাস; reader/exports/script-audit/publication বাকি।
