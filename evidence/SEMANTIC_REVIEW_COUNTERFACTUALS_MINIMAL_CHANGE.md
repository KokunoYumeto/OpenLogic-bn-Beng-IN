# প্রতিবাস্তব শর্তবচন: ন্যূনতম পরিবর্তনের অর্থতত্ত্বের অর্থপর্যালোচনা

মূল কর্তৃপক্ষ: OpenLogicProject/OpenLogic-এর হিমায়িত সংস্করণ
`9620cc73f9c8e0ad003c514a5d3748f29611c4c0`; পূর্ণ উৎস-তালিকার
SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`।
OLP-0522–OLP-0528-এ একটি অধ্যায়চালক ও ছয়টি বিভাগ আছে; মূল ও বাংলা
উভয় পাঠে মোট ৫০টি সমরেখ ব্লক। অধ্যায়চালকের ছয়টি আমদানি অক্ষত।

| ইউনিট | বাংলা পাঠের বিপরীতার্থক ইংরেজি পাঠ | অর্থ ও গঠন যাচাই |
| --- | --- | --- |
| OLP-0522 | The chapter introduces minimal-change semantics through six sections. | অধ্যায়-পরিচয় ও ছয়টি আমদানি অক্ষত। |
| OLP-0523 | A counterfactual is checked at the closest antecedent worlds; Lewis's nested spheres represent relative closeness. | দেশলাই-উদাহরণ, Lewis/Stalnaker-এর চিহ্ন, `\cif`, পরিতৃপ্তি-সূত্র ও গোলকচিত্র অক্ষত। |
| OLP-0524 | A sphere model assigns each world a centered, nested sphere system closed under nonempty unions and intersections. The counterfactual is vacuously true when the antecedent occurs nowhere in the spheres, or nonvacuously true when some antecedent-admitting sphere satisfies the material conditional throughout. | সংজ্ঞার চার শর্ত, চিত্রের জগৎ-মাননির্ধারণ ও অন্তঃস্থ পূর্বপক্ষ-স্বীকারক গোলক না-থাকার অসীম ক্ষেত্র অক্ষত। BN-SRC-422 ছোট গোলক সম্পর্কে ভুল অবাধ দাবিটি সীমিত করে; BN-SRC-423 অংশ-পরিচয় ঠিক করে। |
| OLP-0525 | A counterfactual can be nonvacuously true, vacuously true, or false with either a false or true consequent-negated opposite; it can vary in truth between worlds. | পাঁচটি চিত্র, তাদের শিরোনাম, চারটি সত্য-মিথ্যা ক্ষেত্র ও আপতিক মডেল অক্ষত। BN-SRC-424 অংশ-পরিচয় ঠিক করে। |
| OLP-0526 | Striking a match normally makes it light, while striking it in outer space need not; strengthening the antecedent fails. | উদ্ধৃত অনুমিতি, নিকটত্ব-ব্যাখ্যা, তিন-জগতের মাননির্ধারণ ও চিত্র অক্ষত। BN-SRC-425 উৎসের light/strike অসঙ্গতি মেটায়। |
| OLP-0527 | In the Hoover example, two counterfactual premises can be true while their chained conclusion is false. | তিনটি অনুশীলন ও সতর্কীকরণ-পাদটীকা অক্ষত। BN-SRC-426 `q→r`-এর ভুল অপরিতৃপ্তি চিহ্ন সরায়; BN-SRC-429 শৈশবের সময়গত অসঙ্গতি মেটায়। |
| OLP-0528 | The Goethe example and a three-world model show that a counterfactual need not entail its contrapositive. | দুই বাক্যের যুগল, চিত্র, মাননির্ধারণ ও প্রতিদৃষ্টান্ত অক্ষত। BN-SRC-427 গোলকব্যবস্থাকে `O_w` বলে; BN-SRC-428 মডেলের নাম এক রাখে। |

সংজ্ঞা অনুযায়ী BN-SRC-422 প্রয়োজন: কোনও গোলক `S`-এ পূর্বপক্ষ-সত্য
জগৎ এবং সর্বত্র `B→C` থাকলে তার ছোট গোলকে দ্বিতীয় শর্তটি থেকে যায়,
কিন্তু সেখানে পূর্বপক্ষ-সত্য জগৎ নাও থাকতে পারে। তাই অশূন্যার্থক
সিদ্ধান্ত কেবল ছোট *পূর্বপক্ষ-স্বীকারক* গোলকের জন্য। সবচেয়ে ভিতরের
এমন গোলক আদৌ না-থাকার মূলের সম্ভাবনাটিও বাংলা পাঠে রাখা হয়েছে।

তিনটি সসীম প্রতিদৃষ্টান্ত আলাদাভাবে গণনা করা হয়েছে। OLP-0526-এর
`w,w_1,w_2` মডেলে `p⇝r` সত্য অথচ `(p∧q)⇝r` মিথ্যা;
OLP-0527-এ `p⇝q` ও `q⇝r` সত্য অথচ `p⇝r` মিথ্যা;
OLP-0528-এ `p⇝q` সত্য অথচ `¬q⇝¬p` মিথ্যা। প্রতিটি
পরীক্ষায় ক্ষুদ্রতম পূর্বপক্ষ-স্বীকারক গোলক ও তার সব জগতের
বস্তুগত শর্তবচন যাচাই করা হয়েছে। BN-SRC-426-এর ক্ষেত্রে
`w`-তে `q` মিথ্যা এবং `w_1`-তে `q,r` উভয়ই সত্য;
অতএব `{w,w_1}`-এর সর্বত্র `q→r` সত্য।

BN-SRC-429-এর ঐতিহাসিক যাচাই: [FBI-র জীবনী](https://www.fbi.gov/history/directors/j-edgar-hoover)
হুভারের জন্ম ১ জানুয়ারি ১৮৯৫ বলে; [রুশ রাষ্ট্রীয় আর্কাইভ](https://statearchive.ru/468)
সোভিয়েত ইউনিয়নের প্রতিষ্ঠা ডিসেম্বর ১৯২২ বলে। তাই একই জন্মসাল ধরে
সোভিয়েত ইউনিয়নে বড় হওয়ার উৎস-বাক্যটি কালানুক্রমে অসম্ভব। বাংলা
পাঠে রাশিয়ায় বেড়ে ওঠা এবং *পরে* সোভিয়েত ইউনিয়নে কমিউনিস্ট
হওয়ার অনুমান পৃথক করা হয়েছে; যুক্তির তিনটি সূত্র ও মডেল বদলায়নি।

ত্রিপুরার BN-IN-P007-এর পৃষ্ঠা ৯-এ উপসেট ও সেটের সাধারণ ভাষা,
NSOU-র BN-IN-P012-এর পৃষ্ঠা ৩৪৯-এ সংযুক্তি–ছেদ,
BN-IN-P014-এর পৃষ্ঠা ৩৬৬-এ সংক্রমণশীলতা এই পর্বে দৃশ্যত
পুনর্পাঠ করা হয়েছে। আগে দেখা BN-IN-P008/P009/P013-এর
উক্তি–সংযোজক–সম্পর্কের পৃষ্ঠাও পরামর্শ-করা হয়েছে। এই সাক্ষ্যগুলি
Lewis–Stalnaker-এর বিশেষ গোলক অর্থতত্ত্ব সরাসরি প্রতিষ্ঠা করে না;
BN-IN-T379–T381-এ সেই সীমা ও বিকল্পগুলি নথিবদ্ধ। প্রতি ভাষাগত
ব্লকে প্রকৃত পরামর্শ-পৃষ্ঠা, উৎস/লক্ষ্য বাইট-পরিসর ও হ্যাশ
`DRAFT_SEGMENT_CANON_USE.jsonl`-এ আছে।

সমগ্র ৫২৭ ইউনিটে সূত্র, নিয়ন্ত্রণ-ক্রম, পরিবেশ, টোকেন, NFC এবং
প্রতি ফাইলের ব্লক-সংখ্যা পরীক্ষিত। আটটি সংশোধনের ব্যতিক্রম
সূত্র বা পরিচয়ের ঠিক কোন স্থানে প্রযোজ্য, পরীক্ষকে নির্দিষ্ট।
এটি স্বাধীন মানব-বিশেষজ্ঞের পাঠ বা নির্মিত TeX পৃষ্ঠার দৃশ্যপরীক্ষা
বলে দাবি নয়। অধ্যায়টি সমষ্টিগত HTML/EPUB পাঠকে এখনও যুক্ত হয়নি;
এই পর্বের নতুন PDF নির্মিত হয়নি।
