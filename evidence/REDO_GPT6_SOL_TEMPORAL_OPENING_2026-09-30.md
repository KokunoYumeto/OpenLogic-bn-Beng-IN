# কালগত যুক্তিবিদ্যার সূচনার পুনঃপরীক্ষা

২০২৬-০৯-৩০; GPT-6.1 Sol, Ultra। OLP-0475–0480-এর সম্পূর্ণ স্থিরীকৃত ইংরেজি, বাংলা, পুরোনো BN-SRC-390 ও নতুন BN-SRC-742/743 পড়া ও তুলনা হয়েছে। উৎস commit 9620cc73f9c8e0ad003c514a5d3748f29611c4c0 অপরিবর্তিত। এটি AI-পুনঃপরীক্ষা; স্বাধীন মানব-পর্যালোচনা নয়।

আজ বাস্তবে পড়া P008/P009 বচন/সংযোজক এবং P013/P014 সম্পর্কের রীতি; P017 প্রমাণের গদ্য ও P018 অপেক্ষকের ক্ষেত্র প্রাসঙ্গিক। এই batch-এ NSOU PDF-পৃষ্ঠা ৩৬৬, মুদ্রিত ৩৬১ (P014) আবার দৃশ্যত পড়া: শিরোনাম “পরিযায়ী সম্পর্ক”, শর্ত aRb ও bRc⇒aRc। OLP-0479-এ আগের “সঞ্চারী” সরিয়ে প্রকৃত canon ও T324-এর “পরিযায়ী” ফিরেছে। বিশেষ কালগত/ভবিষ্যৎ-আপতিক/Since/Until-পদের প্রত্যক্ষ সাক্ষ্য দাবি নেই; মূল সংজ্ঞা নিয়ন্ত্রণ করে। পুরোনো T351 rationale ভুল করে P013-পৃষ্ঠায় transitivity আরোপ করছিল; fresh rationale সঠিক P014-তে বাঁধা। P017-এর ভুল প্রদর্শিত সূত্র গণিতের ভিত্তি নয়।

## OLP-0475–0477: গঠন ও ভূমিকা

প্রয়োগের অংশে কালগত ও জ্ঞানতাত্ত্বিক দুটি import এবং পরীক্ষামূলক খসড়া নোট অক্ষত। কালগত অধ্যায়ে পাঁচ import যথার্থ। কিন্তু শেষে অংশ-hook ছিল। BN-SRC-743-তে অধ্যায়-hook হয়েছে: স্থিরীকৃত open-logic-defer.sty-র problemsperchapter সংজ্ঞা OLEndChapterHook-এ deferred problems বন্ধ ও মুদ্রণ করে। দুই hook আলাদা; বর্তমান reader-এ visible effect না থাকলেও অধ্যায়ের সঠিক callback প্রয়োজন।

ভূমিকায় Prior-এর tense treatment, কুকুরের ভিন্ন সময়ে বসা/না-বসা, ভবিষ্যৎ disjunction-এর inference, determinism ও অজানা সত্যমান বনাম অনির্ধারিত সত্যমান, এবং linear/branching/circular/discrete/continuum পছন্দ পৃথকভাবে বাংলা মেলে। আপতিকের অর্থ neither necessary nor impossible; শুধু আমাদের অজ্ঞতা নয়। Temporal-এর “কালগত” ও tense-এর “কালরূপের” ভেদ যথার্থ।

## OLP-0478: ভাষা ও অর্থতত্ত্ব

পাঁচ সংযোজক, নির্বাচিত সত্য/মিথ্যা ধ্রুবক, গণনাযোগ্য অসীম propositional variables এবং চার unary temporal operator-এর formation clause মেলে। BN-SRC-390-র Ftemp ভবিষ্যৎ-অপারেটর ঠিক; খালি F উৎসের typo। মডেলের T অশূন্য, prec⊆T×T, V(p)⊆T এবং prec-এ আপাতত কোনো order-শর্ত নেই। P/H-তে t′≺t, F/G-তে t≺t′; P/F existential এবং H/G universal। Boolean সাত clause-এ সব sign ও operand মেলে। H=not P not এবং G=not F not, মৃত অতীত/ভবিষ্যৎ বিন্দুতেও যথার্থ।

Past ও future পৃথক স্বাধীন সম্পর্ক নয়: একই prec-এর বিপরীত দিক। তাই p→G P p এবং p→H F p সব মডেলে বৈধ। OLP-0479-এর “পরিচিত স্বতঃসিদ্ধের মধ্যে কেবল K” বাক্যটি পরিচিত single-modality D/T/B/4/5-এর সীমায়; দুই দিকের সব interaction formula বাদ দেওয়ার দাবি হিসেবে পড়া হয়নি।

## OLP-0479: পাঁচ sufficient frame law

K_G ও K_H সাধারণ universal implication argument-এ বৈধ। পাঁচ row-তে source-এর শর্ত ও ফল যথার্থ। Transitivity-তে FFp-এর দুই সাক্ষীর পথ একটি Fp-সাক্ষী দেয়। Comparability-তে FPp বা PFp-র চূড়ান্ত p-সাক্ষী বর্তমানের আগে/একই/পরে হয়; তাই Pp∨p∨Fp। Density-তে Fp-সাক্ষীর পথে মধ্যবর্তী বিন্দু বেছে FFp। Past/future seriality-তে সব পূর্ববর্তী/পরবর্তী বিন্দুতে p হলে অন্তত একটি Pp/Fp-সাক্ষী আছে। Universal-এ কোনো গন্তব্য না থাকলে সত্য এবং existential-এ মিথ্যা—এই শূন্য ক্ষেত্র যথাযথ।

সারণির “রৈখিক” প্রদর্শিত শর্ত global comparability; একা transitivity বা irreflexivity-র সংজ্ঞা নয়। সারণির heading “যদি ... তবে”; linear row-কে exact iff correspondence বলা হয়নি। দুটি সম্পর্কহীন মৃত বিন্দুতে modal formula vacuously valid, কিন্তু global comparability মিথ্যা। অন্য চার row-এর converse valuation-argument-ও মেলে: ব্যর্থ transitive/dense edge-এর target-এ একমাত্র p; predecessor/successor না থাকলে p=false-তে universal থেকে existential inference ব্যর্থ।

মৌলিক unary tense ভাষায় irreflexivity frame-formula দ্বারা সংজ্ঞায়িত নয়। পূর্ণসংখ্যার strict <-frame থেকে reflexive এক-বিন্দুর frame-এ constant map future ও past উভয় দিকের bounded morphism: প্রত্যেক পূর্ণসংখ্যায় পরের ও আগের বিন্দু আছে। এক-বিন্দুর valuation টেনে নিয়ে structural induction-এ formula-সত্যতা মেলে। ফলে সব irreflexive frame-এ বৈধ কোনো basic-tense formula reflexive ওই frame-এও বৈধ। এই যুক্তি এখানে unary P/H/F/G ভাষার; অতিরিক্ত binary operator-এ একই map-এর preservation অনুক্তভাবে ধরে নেওয়া হয়নি।

## OLP-0480: Since ও Until

Source-নির্ধারিত operand order অক্ষত: প্রথম B সাক্ষীর বিন্দুতে, দ্বিতীয় C নির্দিষ্ট মধ্যবর্তী সব বিন্দুতে। Since-এ t′≺t; Until-এ t≺t′; মধ্যবর্তী দুই তিরের দিক ঠিক। BN-SRC-742-তে স্বাভাবিক গদ্যের endpoint-সীমা স্পষ্ট: C(t) আলাদাভাবে দাবি নয়। Strict linear তিন-বিন্দুর chain-এ B শেষে, C কেবল মাঝখানে সত্য হলেও Until B C প্রথমে সত্য; প্রথম বিন্দুতে C মিথ্যা। Since-এর বিপরীত সাক্ষীও মেলে। এক ধাপের strict chain-এ কোনো মাঝের বিন্দু নেই বলে C=false হলেও witness B থাকলে Until সত্য। কিন্তু arbitrary prec-এ self-loop অনুমোদিত: তখন বর্তমান নিজেই প্রদর্শিত মধ্যবর্তী predicate পূরণ করতে পারে; নোটটি শুধু strict order-এর দুই endpoint বাদ পড়ার দাবি করে, সব সম্পর্কের নয়। অন্য প্রচলিত operand order বা non-strict Until নীরবে প্রতিস্থাপন করা হয়নি।

## বর্তমান bytes-এ পরীক্ষা

GPT6_SOL_REDO_TEMPORAL_OPENING_CHECK.json ছয় target ও প্রকৃত deferred-hook source-এর hash বাঁধে। সর্বোচ্চ তিন জগতে ৩৩,০৩২ model/valuation পরীক্ষা: দুই K-law, দুই duality ও converse-direction interaction পাস। প্রকৃত পাঁচ সারণি-সূত্রের condition-case সংখ্যা যথাক্রমে ১১,১৬০; ১৪,০২৪; ২১,৫২৮; ২২,১০০; ২২,১০০। চার exact law-এর converse এবং linear row-এর ব্যর্থ converse-এর সাক্ষীও পাস। কঠোর endpoint, খালি middle ও self-loop আলাদা সাক্ষী। ক্ষুদ্র গণনা সাধারণ প্রমাণ নয়; ওপরের সাধারণ সম্পর্ক-যুক্তি আলাদাভাবে তুলিত। source/canon refresh, reader নির্মাণ ও প্রকাশনা এখনও বাকি।
