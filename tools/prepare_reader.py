import hashlib, pathlib, re
repo=pathlib.Path(__file__).resolve().parents[1]
build=repo/'build/reader'; build.mkdir(parents=True,exist_ok=True)
for name,digest in [('NotoSerifBengali-Regular.ttf','04935aea18655c451d05b1d4bb5bdc835226a221663f89a2ecfbcfdc4483e399'),('NotoSerifBengali-Bold.ttf','f752131cd292f3e0fd7a25c8fc86f5424062bc06e29f6dfadcb3c09ff4881dd0')]:
    assert hashlib.sha256((repo/'fonts'/name).read_bytes()).hexdigest()==digest
preamble=(repo/'tools/sets-preamble.tex').read_text(encoding='utf-8')
additions=(repo/'tools/reader-additions.tex').read_text(encoding='utf-8')
preamble=preamble.replace('\\begin{document}',additions+'\n\\begin{document}')
preamble=preamble.replace('pdftitle={ওপেন লজিক: সেট}','pdftitle={ওপেন লজিক: সেট, সম্পর্ক ও অপেক্ষক}')
preamble=preamble.replace('Sets chapter; full edition in progress','Sets, Relations and Functions; full edition in progress')
preamble=preamble.replace('{\\LARGE সেট\\par}','{\\LARGE সেট, সম্পর্ক ও অপেক্ষক\\par}')
preamble=preamble.replace('এই অধ্যায়টি','এই অধ্যায়গুলি').replace('এই অংশে উৎসের OLP-0004 থেকে OLP-0010 এবং OLP-0721 অন্তর্ভুক্ত।','এই অংশে উৎসের OLP-0004 থেকে OLP-0026 এবং OLP-0721-এর পাঠ অন্তর্ভুক্ত। বিকল্প অধ্যায়-চালক OLP-0719 সম্পাদনাযোগ্য উৎসে আছে; সেটি একই অধ্যায় পুনরাবৃত্তি না করে দার্শনিক অংশ বাদ দেওয়ার বিন্যাসটি দেয়। পূর্ণ 722টি উৎস ফাইলের মধ্যে 25টির অনুবাদ এই সংস্করণে আছে।')
preamble=preamble.replace('\\url{https://openlogicproject.org/}','\\url{https://github.com/KokunoYumeto/OpenLogic-bn-Beng-IN}\n\\par\n\\url{https://openlogicproject.org/}')
parts=[preamble]
groups={'sets':['basics','subsets','important-sets','unions-and-intersections','pairs-and-products','russells-paradox','proofs-about-sets'],'relations':['relations-as-sets','reflections','special-properties','equivalence-relations','orders','graphs','trees','operations'],'functions':['function-basics','function-kinds','functions-relations','inverses','composition','partial-functions']}
notes={
'functions-relations':r'শুধু ক্রমযুগলের সেট থেকে অপেক্ষকের নির্বাচিত সহসংজ্ঞাক্ষেত্র উদ্ধার করা যায় না; গ্রাফ হিসেবে অপেক্ষক বিবেচনা করার সময় ঘোষিত সংজ্ঞাক্ষেত্র ও সহসংজ্ঞাক্ষেত্রও মনে রাখতে হবে। OLFUN-004 ও OLFUN-005 সংশোধনগুলি অনূদিত মূল পাঠের পাশেই দেওয়া আছে।',
'relations-as-sets':r'এই অংশের উদাহরণে উৎসে ব্যবহৃত $I$ হল আগে বর্ণিত কর্ণের সম্পর্ক $\Id{\Nat}$; ইংরেজি উৎসে $I$-এর নামকরণ স্পষ্টভাবে করা হয়নি।',
'orders':r'অনুক্রমের প্রসারণ-ক্রম রৈখিক নয়—এই দাবির প্রদত্ত উদাহরণে $A$-তে অন্তত দুটি ভিন্ন উপাদান থাকতে হয়। শূন্য বা এক-উপাদানবিশিষ্ট বর্ণমালার ক্ষেত্রে প্রসারণ-ক্রম রৈখিক। এই অংশে $R^+$ প্রতিবিম্ব আবরণ বোঝায়; সম্পর্কের উপর ক্রিয়া অংশে একই চিহ্নের আলাদা স্থানীয় সংজ্ঞা আছে।',
'trees':r'শাখার সংজ্ঞায় ইংরেজি উৎসের $z\in X\setminus B$-তে $X$ অসংজ্ঞায়িত; এখানে $A$ বোঝানো হয়েছে। অনুবাদের সূত্রে মূল অক্ষর রাখা হয়েছে। নিচের উপবৃক্ষের উদাহরণে মূলবিশিষ্ট বৃক্ষের সংজ্ঞা মানতে নিম্নমুখী বদ্ধ সেটটিকে অশূন্যও ধরতে হবে।',
'operations':r'এই অংশে $R^+$ পরিযায়ী আবরণ বোঝায়। ক্রমসম্পর্ক অংশে $R^+$-এর যে স্থানীয় সংজ্ঞা দেওয়া হয়েছিল, এটি তার থেকে আলাদা।'}
for group,names in groups.items():
    if group=='relations': parts.append('\\chapter{সম্পর্ক}\n')
    if group=='functions': parts.append('\\chapter{অপেক্ষক}\n')
    for name in names:
        text=(repo/'bn-Beng-IN/content/sets-functions-relations'/group/f'{name}.tex').read_text(encoding='utf-8')
        text=text.split('\\begin{document}',1)[1].rsplit('\\end{document}',1)[0]
        words={'element':'উপাদান','formula':'সূত্র','derivation':'নিষ্পাদন','injective':'একৈক','injection':'একৈক অপেক্ষক','surjective':'সমাপতিত','surjection':'সমাপতিত অপেক্ষক','bijective':'একৈক সমাপতিত','bijection':'একৈক সমাপতিত অপেক্ষক'}
        text=re.sub(r'!!(\^)?(a)?\{('+('|'.join(words))+r')\}(s)?',lambda m:('একটি ' if m[2] else '')+words[m[3]],text)
        assert '!!' not in text
        if name in notes:
            match=re.search(r'\\olsection\{[^{}]*\}',text)
            text=text[:match.end()]+'\n\\begin{translationnote}'+notes[name]+'\\end{translationnote}\n'+text[match.end():]
        parts.append(text)
parts.append(r'''\chapter*{তথ্যসূত্র}
\addcontentsline{toc}{chapter}{তথ্যসূত্র}
\label{bib:Benacerraf1965}
Paul Benacerraf (1965). ``What numbers could not be.'' \emph{The Philosophical Review} 74(1): 47--73.
\end{document}
''')
(build/'openlogic-bn-reader.tex').write_text('\n'.join(parts),encoding='utf-8')
print('Prepared cumulative Sets, Relations and Functions reader: 25 translated source units, 21 sections; alternate driver integrated without duplication.')
