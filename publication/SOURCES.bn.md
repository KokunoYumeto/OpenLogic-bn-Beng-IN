# ওপেন লজিকের ভারতীয় বাংলা সংস্করণ

এই সংগ্রহে মূল ইংরেজি রচনার ৭২২টি একক ও তাদের বাংলা অনুবাদ আছে। অংশ, অধ্যায় ও অনুচ্ছেদ অনুসারে সাজানো সম্পূর্ণ সম্পাদনযোগ্য পাঠটি `build/full-edition/openlogic-bn-Beng-IN-complete.tex` ফাইলে। একক ধরে পড়তে বা সম্পাদনা করতে `bn-Beng-IN/content/` দেখুন। তার সঙ্গে মিলিয়ে দেখার জন্য ইংরেজি পাঠ `upstream/content/`-এ আছে। দুই পাঠের ফাইলের নাম ও হ্যাশ `units.jsonl`-এ দেওয়া হয়েছে।

ইংরেজি মূল রচনা Open Logic Project-এর লেখক ও অবদানকারীদের। বাংলা অনুবাদ করেছে OpenAI Codex-এর GPT-5.6 Sol ও GPT-6 Sol। GPT-6.1 Sol বাংলা পাঠ পরীক্ষা করেছে এবং পরিবর্তিত ইংরেজি অংশের সঙ্গে মিলিয়েছে। GPT-6 Astra দুটি বিধিতে ইংরেজি মূলের চিহ্ন মিলিয়েছে, মূলের দুটি সংক্ষিপ্ত নাম ব্যাখ্যা করেছে, RM3 সারণির সূত্রনির্দেশ যাচাই করেছে এবং পাঠের মুদ্রণরূপ, শ্রেণিবাচক পদের বিন্যাস ও ডিজিটাল সংস্করণ প্রস্তুত করেছে। প্রতিটি মডেলের যুক্তিপ্রয়াসের স্তর ছিল Ultra। মূল রচনার স্বীকৃতি ও লাইসেন্স `upstream/README.md` ও `upstream/LICENSE.md`-এ আছে। [Open Logic Project](https://github.com/OpenLogicProject/OpenLogic)

## পাঠ তৈরি

ইংরেজি ও বাংলা পাঠে ব্যবহৃত বিধির চিহ্ন এবং সেটের সমসংখ্যকতার একটি পাঠভেদ আলাদা করে দেওয়া হয়েছে। [গাণিতিক চিহ্ন ও পাঠভেদ](source-readings.bn.md)

পাইথন ৩.১১ বা পরবর্তী সংস্করণ, Pandoc, XeLaTeX ও BibTeX লাগবে। পাইথনের জন্য `beautifulsoup4`, `lxml` ও `fonttools` ইনস্টল করুন। Windows-এ PDF তৈরির স্ক্রিপ্টটি PowerShell ও MiKTeX ব্যবহার করে। সংগ্রহের মূল ফোল্ডার থেকে চালান।

```sh
python tools/prepare_full_edition.py
pwsh -NoProfile -File tools/build_full_edition_windows.ps1
python tools/build_full_semantic_reader.py
python tools/build_full_epub.py --epubcheck-jar /path/to/epubcheck.jar
```

সম্পূর্ণ PDF, HTML ও EPUB তৈরি হয় `build/full-edition/`-এ। HTML-এ গাণিতিক সূত্র MathML-এ দেওয়া আছে। EPUB যাচাইয়ের জন্য Java ও EPUBCheck লাগবে। বাংলা ফন্টের স্বত্ব ও শর্ত `fonts/Noto-fonts-LICENSE.txt`-এ আছে। বিশেষ গাণিতিক চিহ্নের উৎস, TX Fonts-এর শর্ত ও Jeremy Gibbons এবং Alan Jeffrey-এর St Mary’s Road ফন্টের দলিল `build/full-edition/font-sources/`-এ আছে।
