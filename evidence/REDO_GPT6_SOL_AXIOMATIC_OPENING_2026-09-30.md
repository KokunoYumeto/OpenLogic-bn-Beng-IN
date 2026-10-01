# স্বতঃসিদ্ধমূলক মোডাল পদ্ধতির সূচনা: নতুন পরীক্ষা

OLP-0427–0430-এর ইংরেজি, বাংলা, দুটি বিধির proof tree, RK-এর আবেশ, normal closure ও derivability-set-এর দুই inclusion ২০২৬-০৯-৩০-এ OpenAI Codex — GPT-6.1 Sol, Ultra effort — নতুন করে তুলেছে। অন্য দশটি অধ্যায়-একক এই নথিতে পরীক্ষিত বলে দাবি করা হয়নি। কোনো স্বাধীন মানব-পর্যালোচনা হয়নি; নতুন reader ও প্রকাশনা বাকি।

P008/P009-এর বচন, সংযোজক ও পরিমাণকের গদ্য এবং P018-এর অপেক্ষক-সংজ্ঞা আজকের আগের batch-এ আবার পড়া হয়েছে। এই batch-এ আরও BN-IN-P017, NSOU EMT-03, PDF 369, মুদ্রিত 364-এর proof prose দৃশ্যত পড়া হয়েছে: membership থেকে relation, তারপর পৃথকভাবে reflexivity, symmetry ও transitivity পরীক্ষা। ওই পৃষ্ঠার প্রদর্শিত সূত্রে ভুল গঠনকে গণিতের authority ধরা হয়নি। মূল ও page-image hash unit-review ledger-এ। বিশেষ ‘হিলবার্ট-ধরনের’, ‘আবশ্যকীকরণ’ ও ‘স্বাভাবিক মোডাল পদ্ধতি’ পদের প্রত্যক্ষ পূর্ণ ভারতীয় বাংলা সাক্ষ্য নেই; সংশোধিত source-সংজ্ঞা ও প্রচলিত edition-choice অর্থ নিয়ন্ত্রণ করে।

| একক | ফল |
|---|---|
| OLP-0427 | বাংলা অধ্যায়-নাম, derivation-token এবং তেরোটি import অক্ষত। |
| OLP-0428 | MP, Nec, finite derivation ও earlier-line index-এর শর্ত তুলিত। BN-SRC-694-তে soundness-এর all-substitution-instance শর্ত এবং normality-র modal-axiom শর্ত স্পষ্ট। |
| OLP-0429 | modal/normal logic-এর সব closure, K/Dual, necessitation-এর global scope, RK-এর আবেশ ও smallest-system construction তুলিত। BN-SRC-693-তে smallest normal logic বলা এবং intersection proof-এর তিন আলাদা কারণ যোগ করা হয়েছে। |
| OLP-0430 | proof sequence-এর সূত্র ও axiom-instance শর্ত, দুই inclusion ও সব closure case তুলিত। BN-SRC-349-এ system-name K-এর বদলে axiom-formula K-এর সদস্যতা যথার্থ। সেই source-comment বাংলায় করা হয়েছে। |

## সংশোধনের কারণ ও সাধারণ প্রমাণ

OLP-0428-এ Σ স্বতঃসিদ্ধের প্রতিনিধিসূত্র রাখে; derivation তাদের প্রতিটি substitution instance ব্যবহার করতে পারে। তাই একটি স্থির মডেলে শুধু প্রতিনিধিসূত্র সত্য থাকা soundness-এর জন্য যথেষ্ট নয়। একটি এক-জগৎ মডেলে p সত্য রেখে Σ={p} নিলে p-র falsum-instance derivation-এর এক পংক্তি হতে পারে, অথচ মডেলে তা অসত্য। সংশোধিত শর্তে সমস্ত instance প্রত্যেক জগতে সত্য। tautological-instance case আগের theorem থেকে; MP pointwise সত্য সংরক্ষণ করে; Nec-তে previous formula মডেলের সমস্ত জগতে সত্য বলে প্রত্যেক successor-এ সত্য। arbitrary Σ-র derived set normal বলা যায় না: K ও প্রযোজ্য Dual-এর axioms দরকার।

OLP-0429 `prop:rk`: n=1-এ Nec। n>1-এ n−1 ফল প্রয়োগে শেষ দুই সূত্রের conditional-কে একটি সূত্র হিসেবে ধরি; K তার box-কে box-দুটির conditional-এ নিয়ে যায়। propositional tautological instance পুরো আগের implication-chain-এর ভিতরে ওই consequence স্থানান্তর করে। ¬diamond falsum পেতে ¬falsum-এর tautology, Nec ও Dual যথেষ্ট।

smallest-system proof-এ সমস্ত সূত্রের সেট থাকার অর্থ যে পরিবারের ছেদ নিচ্ছি সেই পরিবার অশূন্য; এর থেকে intersection অশূন্য সরাসরি আসে না। প্রত্যেক family-member-এ একই tautology ও modal axioms থাকে। সব member substitution, MP ও Nec-তে বন্ধ বলে intersection-ও বন্ধ। intersection প্রত্যেক member-এর subset, তাই ক্ষুদ্রতম normal logic। common tautologies থাকার জন্য intersection নিজেও অশূন্য। ‘normal’ বাদ দিলে এই proof বৃহত্তর সব modal logic-এর মধ্যে minimality প্রমাণ করে না।

OLP-0430-এ derivable-set ⊆ system: proof-length induction-এ axiom line system-এর সদস্য; MP ও Nec closure পরের line সংরক্ষণ করে। বিপরীত inclusion-এর জন্য derivable-set-এ tautologies ও modal axiom আছে; MP-তে দুটি finite proof জুড়ে index সরিয়ে শেষে conclusion, Nec-তে এক line বাড়াই। uniform substitution পুরো proof-এর প্রত্যেক occurrence-এ একইভাবে প্রয়োগ করলে tautology/axiom instance আবার instance থাকে; MP-এর দুই premise-এর গঠন ও Nec-এর box constructor অক্ষত থাকে। ফলে derived-set normal এবং additional axioms ধারণ করে; smallest normality থেকে converse inclusion।

বর্তমান সূত্র ও tags source checker-এ নির্দিষ্ট পুরোনো BN-SRC-349 পরিবর্তন বাদে অক্ষত; correction-notes-এর semantics আলাদা পড়া হয়েছে। এই proof reading কোনো অবশিষ্ট chapter, reader render বা স্বাধীন মানব-অনুমোদনের সনদ নয়।
