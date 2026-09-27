# পর্যায় ও স্তরাঙ্ক: উৎস–অনুবাদ অর্থপর্যালোচনা

মূল কর্তৃপক্ষ OpenLogicProject/OpenLogic-এর হিমায়িত সংস্করণ
`9620cc73f9c8e0ad003c514a5d3748f29611c4c0`; ৭২২-ইউনিট
তালিকার SHA-256
`5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`।
OLP-0558–0564-এ অধ্যায়চালক ও ছয়টি বিভাগ; উৎস ও লক্ষ্যের
৮২টি সমরেখ ব্লক: ৮০টিতে ভাষাগত অনুবাদ,
দুটিতে কেবল গঠন/সূত্র। ছয়টি আমদানি,
তাদের ক্রম এবং সব বিভাগ-পরিচয় অক্ষত।

| ইউনিট | বাংলা থেকে বিপরীতার্থক ইংরেজি পাঠ | অর্থ ও গঠন যাচাই |
| --- | --- | --- |
| OLP-0558 | The chapter driver imports six sections on stages and rank. | ছয় আমদানি, পরিচয় ও ক্রম অক্ষত। |
| OLP-0559 | The stages are defined internally by V₀=∅, successor power sets and limit unions, rather than by a proposed external model. | শূন্য, উত্তরসূরি ও সীমা তিন ক্ষেত্র, তত্ত্ব-অভ্যন্তরীণ চরিত্রায়ন এবং পুনরাবৃত্তি-ন্যায্যতার বাকি থাকা কাজ অক্ষত। |
| OLP-0560 | Bounded recursion gives a unique approximation at every ordinal; the general schema defines values by a term, and simple recursion validates the three clauses for Vα. | অনন্যতা ও অস্তিত্বের আবেশ, পদ বনাম সেটরূপ ফাংশনের পার্থক্য, বুরালি–ফোর্তি সতর্কতা এবং তিন রূপের যথাযথ পরিসর অক্ষত। BN-SRC-438 ভাঙা বাক্য স্পষ্ট করে; BN-SRC-439 শূন্য ফাংশনের বাদ পড়া ভিত্তি ক্ষেত্র পূরণ করে। |
| OLP-0561 | Every stage is transitive, downward closed under taking subsets of members, and cumulative; no stage contains itself, and ordinal order agrees with stage membership. | তিন ধর্মের একযোগে আবেশ, উত্তরসূরি/সীমা ক্ষেত্র, আত্মসদস্যতা-বর্জন ও ক্রমসংখ্যা-পর্যায় দ্বিশর্ত অক্ষত। |
| OLP-0562 | Foundation says every nonempty set has a member disjoint from it; transitive closure and a rank bound show that Foundation implies Regularity over ZF-minus. | পরিযায়ী আবরণের পুনরাবৃত্ত সংজ্ঞা, পরিযায়ী সেটের পর্যায়-সীমা, D-র শূন্যতা-প্রমাণ ও নিয়মিততার উপসংহার অক্ষত। BN-SRC-440-এ প্রদর্শিত অবদ্ধ `b`-র স্থলে নির্বাচিত `B`। |
| OLP-0563 | Adding Foundation to Z-minus yields Z; adding it to ZF-minus yields ZF. The equivalence with Regularity uses Replacement and need not hold over Z-minus. | স্বতঃসিদ্ধতালিকা, প্রতিস্থাপনের ভূমিকা, পর্যায়-সংজ্ঞার জন্য Z/Z-minus-এর দুর্বলতা এবং পরবর্তী ZF-রীতি অক্ষত। |
| OLP-0564 | A set's rank is the least α with A⊆Vα. Stage membership is equivalent to rank below α; ranks decrease along membership, yielding set induction and the converse Regularity-to-Foundation implication. | স্তরাঙ্কের সংজ্ঞা/অস্তিত্ব অনুশীলন, কঠোর নিম্নতা, সদস্যতা-আবেশ, supstrict সূত্র, ক্রমসংখ্যার নিজ স্তরাঙ্ক ও ন্যূনতম স্তরাঙ্কে ভিত্তির প্রমাণ অক্ষত। BN-SRC-441-এ উৎসের স্ববিরোধী শেষ সূত্র সংশোধিত। |

চারটি স্থানীয় উৎস-সংশোধনের সুনির্দিষ্ট পথ, পংক্তি ও
উৎস–লক্ষ্য SHA-256 `SOURCE_CORRECTIONS.jsonl`-এ আছে।
BN-SRC-438 শুধু গদ্য মেরামত। BN-SRC-439-এ উৎসের
`ξ(x)`-র প্রথম শাখা শূন্য সংজ্ঞাক্ষেত্র বাদ দিত,
যদিও পরের প্রমাণে `ξ(∅)=A` দরকার। বাংলা প্রথম
শাখায় শূন্য ফাংশন অন্তর্ভুক্ত। BN-SRC-440-এ
`B∈D` নির্বাচনের পর `x∈b`-র `b` অবদ্ধ;
বাংলায় `x∈B`। BN-SRC-441-এ `x∈Vα`
ধরে উৎস `x∉Vα` বলেছে; বাংলায় শূন্য,
উত্তরসূরি ও সীমা ক্ষেত্রের যুক্তি দেখিয়ে
প্রয়োজনীয় `rank(x)∈α` বলা হয়েছে।
শেষ দুই সূত্র-ভেদ `tools/check_source_draft.py`-এ
শুধু সংশ্লিষ্ট ইউনিট ও সংশোধন-ID-র জন্য কঠোরভাবে
নির্দিষ্ট; অন্য সূত্র ও নিয়ন্ত্রণ-চিহ্নের সামঞ্জস্য অক্ষত।

নতুন T395–T398-এ পর্যায়, স্তরাঙ্ক, ট্রান্সফাইনাইট
পুনরাবৃত্তি, সন্নিকটায়ন, উপসেট-অধোবদ্ধতা,
পরিযায়ী আবরণ, ভিত্তি ও নিয়মিততা নথিবদ্ধ।
আগের T382-এর পর্যায়, T391/T394-এর ক্রমসংখ্যা
ও সীমা ক্ষেত্র, T393-এর প্রতিস্থাপন এবং
T026/T032-এর পরিযায়ী রীতি অনুসৃত। দেখা ভারতীয়
পৃষ্ঠা সাধারণ সেট, উপসেট, সংখ্যা, সম্পর্ক,
চিত্রণ ও প্রমাণের ভাষা দেয়; এই বিশেষ
সেটতাত্ত্বিক যৌগগুলির প্রত্যক্ষ সাক্ষ্য নেই।
সেগুলি উৎস-সংজ্ঞা-নিয়ন্ত্রিত এবং সংশোধনযোগ্য।
প্রতি অনূদিত ব্লকের পৃষ্ঠা-ID, মূল ও ছবি-হ্যাশ
`DRAFT_SEGMENT_CANON_USE.jsonl`-এ নথিবদ্ধ;
নতুন করে প্রতিটি পৃষ্ঠা দেখার দাবি নেই।

এই অধ্যায়ের জন্য HTML/EPUB বা PDF পাঠক-নির্মাণ
এখনো করা হয়নি। প্রকাশিত সমষ্টিগত HTML/EPUB
পাঠকটি ২৯৯ ইউনিটের। `\supstrict`-এর TeX
সংজ্ঞা ও সম্পূর্ণ পাঠক-দৃশ্যপরীক্ষা পরবর্তী
নির্মাণে যাচাই করা বাকি; সফল TeX-নির্মাণের
দাবি এখানে নেই।
