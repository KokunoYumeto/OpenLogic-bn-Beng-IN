# মোডাল সিকোয়েন্ট কলনের পুনঃপরীক্ষা

২০২৬-০৯-৩০; GPT-6.1 Sol, Ultra। OLP-0470–0474-এর সম্পূর্ণ স্থিরীকৃত ইংরেজি ও বাংলা, সব অপারেটর-নির্বাচন, সূত্র, বিধি-চিহ্ন, পূর্বের BN-SRC-389 ও নতুন BN-SRC-737–741 তুলিত। উৎস commit 9620cc73f9c8e0ad003c514a5d3748f29611c4c0 অপরিবর্তিত। স্বাধীন মানব-পর্যালোচনা দাবি নেই।

আজ আগের পর্বে বাস্তবে পড়া P008/P009 বচন ও সংযোজক, P013/P014 সম্পর্কের ধর্ম, P017 প্রমাণ-গদ্য এবং P018 অপেক্ষকের রীতি প্রাসঙ্গিক। হাইপারসিকোয়েন্টের প্রত্যক্ষ canon সাক্ষ্য নয়; নির্দিষ্ট proof-form নিয়ন্ত্রণ করে। P017-এর ভুল প্রদর্শিত সূত্র গণিতের ভিত্তি নয়। এককভিত্তিক ledger প্রকৃত পৃষ্ঠা ও মূলের hash বাঁধে।

## OLP-0470 ও OLP-0471

চার সক্রিয় import, নিষ্ক্রিয় soundness/hypersequent import এবং মূলের খসড়া-সম্পাদনা নোট অক্ষত। অনুপস্থিত অধ্যায়প্রমাণকে অনুবাদে সম্পন্ন বলা হয়নি। K-র দুই মৌলিক মোডাল বিধি এবং এক অপারেটর মূল হলে অন্যটির সংজ্ঞাগত ব্যবহার যথার্থ।

BN-SRC-737: কোনো সাধারণ কর্তনমুক্ত S5-কলন জানা নেই—নির্বিশেষ বর্তমান দাবি যথার্থ নয়। প্রকাশকের মূল abstract-এ পুনর্লিখনের অতিরিক্ত বিধিযুক্ত সাধারণ কর্তনমুক্ত সিদ্ধান্ত-পদ্ধতি বর্ণিত। পাঠের দাবি এই অধ্যায়ের প্রদর্শিত LK-বর্ধনের সীমায় বাঁধা; হাইপারসিকোয়েন্টের অস্তিত্ব অক্ষত। দেখুন [Indrzejczak, ২০১৬, Simple Decision Procedure for S5 in Standard Cut-Free Sequent Calculus](https://doi.org/10.18778/0138-0680.45.2.05), Bulletin of the Section of Logic 45(2), 125–140। প্রকাশকের abstract সরাসরি পড়া হয়েছে; সম্পূর্ণ প্রবন্ধের প্রমাণ পড়ার দাবি নেই। [Sato, ১৯৮০](https://doi.org/10.2307/2273355)-র প্রকাশকের extract-ও সাধারণ Gentzen-type কর্তন-অপসারণের অস্তিত্ব বলে; বিভিন্ন কলনের শর্ত এক করা হয়নি।

## OLP-0472: মৌলিক বিধি ও নিষিদ্ধ বিস্তার

Box-বিধির উপসংহারে সব বাম Γ Box-যুক্ত, ডান Δ Diamond-যুক্ত এবং বিশেষ A Box-যুক্ত। তার counterworld u-তে সব Box Γ সত্য ও Diamond Δ মিথ্যা; Box A মিথ্যা বলে অভিগম্য v-তে A মিথ্যা, সব Γ সত্য এবং সব Δ মিথ্যা। তাই premise-ও counterworld v-তে ব্যর্থ। Diamond-বিধিতে True Diamond A-এর সাক্ষী v একই কাজ করে। খালি Γ/Δ-ও যুক্তিতে চলে; এক অপারেটর মূল হলে প্রদর্শিত সারণির সীমা ঠিক।

চার নিষিদ্ধ বিস্তারের প্রমাণ উদ্দেশ্যসাপেক্ষে যথার্থ। দুই ভিন্ন successor-এ A ও not A হলে Box A∨Box not A এবং Diamond A→not Diamond not A মিথ্যা। root-এ A সত্য রেখেও ওই দুই successor দিলে not A∨Box A এবং A→not Diamond not A মিথ্যা। unrestricted বা unmodalized পাশের সূত্র এই অবৈধ ফল দেয়। এগুলিকে বৈধ K-বিধি বলে নথিভুক্ত করা হয়নি।

## OLP-0473: প্রকৃত প্রমাণ ও পূর্বের বাদ-পড়া ভুল

Box-সংযোগ ও Diamond-বিয়োগের দুই প্রমাণের weakening, পৃথক operand-introduction, exchange, contraction এবং implication-ধাপ LK-র প্রদর্শিত বিধির সঙ্গে মেলে। চার অনুশীলনের সাধারণ যুক্তি: not p-এর প্রত্যেক successor-এ p→q; Box p অথবা Box q হলে সব successor-এ p∨q; Diamond p-এর একই সাক্ষী p∨q দেয়; Box(p∧q) থেকে প্রত্যেক successor-এ p। এটি অনুশীলনের দাবি যাচাই; পূর্ণ exercise-proof পাঠে দেওয়ার দাবি নয়।

Dual-এর প্রথম negation-এ আগের BN-SRC-389 সঠিক। দ্বিতীয় দিকেও ডান Diamond not A বামে নঞর্থক হয়ে যায়, অথচ Right-negation label ছিল—BN-SRC-738-তে Left-negation করেছি। শেষ Right-conjunction-এর পরে biconditional লিখতে দুই বিপরীত implication-এর conjunction সংজ্ঞাগত সংক্ষেপে নেওয়া হচ্ছে; BN-SRC-741 তা স্পষ্ট করে এবং দ্বিরেখা যোগ করে। primitive biconditional-এ একটি মাত্র conjunction-rule দাবি নেই। পুনরাবৃত্ত “একটি” মেরামত; অনুশীলনের নির্দেশ “দিন”।

## OLP-0474: সব অতিরিক্ত বিধি ও কর্তন

T-বিধির counterworld অপরিবর্তিত; প্রতিবিম্বের জন্য প্রয়োজনীয় মূল সূত্রের সত্যতা বা মিথ্যাতাও সেখানে মেলে। D-বিধির counterworld থেকে সিরিয়াল successor নিয়ে Γ সত্য এবং Δ মিথ্যা পাই। B-বিধিতে successor v নেওয়ার পর symmetry-এর vRu তির দিয়ে u-র সাধারণ Π/Δ থেকে v-র Diamond Π/Box Δ-এর উপযুক্ত মান পাই; Box Γ/Diamond Λ-এর জন্য uRv যথেষ্ট। 4-বিধিতে transitivity uRvRw⇒uRw universal ও existential side-context-এর মান স্থানান্তর করে। 5-বিধিতে transitivity ও euclideanity মিলিয়ে uRv হলে u ও v-র successor-set এক; সব modal side-context-এর মান সমান। কেবল euclidean মডেলের জন্য এই context-preserving 5-বিধির বিশুদ্ধতা দাবি নয়। সারণির S5-তে প্রতিবিম্ব ও euclideanity থেকে symmetry এবং transitivity-ও আসে।

সম্পূর্ণতার standard simulation-ও তুলিত: LK nonmodal tautology, মৌলিক Box-বিধি necessitation ও K-স্কিমা, প্রদর্শিত Dual বা সংজ্ঞাগত দ্বৈততা, এবং Cut modus ponens দেয়। অতিরিক্ত T/4/5-এর প্রদর্শিত axiom-proof মেলে। D-র Γ⇒Δ থেকে Box Γ⇒Diamond Δ নিয়ম A⇒A-তে D দেয়। এক-Box ভাষায় A,not A⇒খালি DBox-এ Box A,Box not A⇒খালি; এক-Diamond ভাষায় খালি⇒A,not A DDiamond-এ খালি⇒Diamond A,Diamond not A—দ্বৈত সংক্ষেপে D। BBox-এ Diamond A⇒Diamond A থেকে A⇒Box Diamond A; এক-Box ভাষায় খালি⇒Box A,not Box A থেকে খালি⇒A,Box not Box A, যা dual B। এক-Diamond ভাষায় not Diamond A,Diamond A⇒খালি থেকে Diamond not Diamond A,A⇒খালি, যা B। ফলে source-দাবির সংশ্লিষ্ট Hilbert axioms সিকোয়েন্টে পাওয়া যায়; এই নথি chapter-এর অনুপস্থিত পূর্ণ proof exposition পূরণের দাবি নয়।

এক-Diamond ভাষার Cut-উদাহরণে দুটি বাম সূত্র বিনিময় হচ্ছিল; BN-SRC-739-তে Right Exchange থেকে Left Exchange। BN-SRC-740-তে প্রতিটি পদ্ধতির মৌলিক বিধি নির্বাচিত অপারেটর অনুযায়ী দেখানো: উভয় মূল হলে Box ও Diamond উভয়; শুধু Diamond মূল হলে Diamond। উৎসের নির্বিশেষ Box-লেবেল মৌলিক Diamond-বিধি বাদ দিচ্ছিল।

দুই ভাষার axiom 4, তিন ভাষার axiom 5 এবং তিন ভাষার Cut-প্রমাণ সব প্রকৃত premise stack-এ তুলিত। প্রদর্শিত calculus-এ Diamond Box A⇒A cut-free হতে পারে না: modal root ভাঙার উপযুক্ত নিয়মের conclusion-side restriction A-র সাধারণ ডান সূত্র রাখে না; structural rule দিয়ে এই obstruction দূর হয় না। এক-Box/এক-Diamond-এর dual রূপেও একই শেষ-মোডাল-ধাপের বাধা। Cut-সহ দুই বৈধ intermediate sequent জুড়লে ফল পাওয়া যায়। এই নির্দিষ্ট বাধাকে সব S5-কলনের অনস্তিত্ব বলা হয়নি। ছয় শেষ অনুশীলনের frame-property প্রমাণ আগের পাঁচ-একক tableaux review-তে পূর্ণভাবে তুলিত; একই সূত্র ও system নাম এখানে অক্ষত।

## পরীক্ষা ও সীমা

GPT6_SOL_REDO_MODAL_SEQUENT_CHECK.json পাঁচ বর্তমান target-এর hash বাঁধে। নির্বাচনের তিন ধরনে মোট ১৪টি প্রদর্শিত প্রমাণ ও ৮১টি inference step প্রকৃত সূত্র, premise stack এবং বিধি-চিহ্নে পাস। তিন নির্বাচনের ২৩টি প্রকৃত modal rule, শূন্য ও এক-সূত্র context-এ সর্বোচ্চ দুই জগতে ১৩,৫৩,০২৪ case পাস। চার অবৈধ unrestricted conclusion-এর নির্দিষ্ট তিন-জগৎ সাক্ষী পাস। ক্ষুদ্র গণনা সাধারণ প্রমাণের বিকল্প নয়; ওপরের counterworld-transfer সাধারণ বহু-সূত্র context-এর জন্য। পূর্ণ source/canon পরীক্ষা ও বর্তমান hash refresh পরবর্তী ধাপ; reader rendering ও প্রকাশনা এখনও বাকি।
