# সেট, যুক্তি, গণনা

**অধিযুক্তিবিদ্যার একটি উন্মুক্ত ভূমিকা** — [Richard Zach](https://richardzach.org/)-এর
[*Sets, Logic, Computation*](https://slc.openlogicproject.org/)-এর ভারতীয় বাংলা সংস্করণ।
সেট, সম্বন্ধ ও অপেক্ষক দিয়ে শুরু করে বইটি প্রথম-ক্রমের যুক্তিবিদ্যার ভাষা,
অর্থতত্ত্ব ও প্রমাণপদ্ধতি, টুরিং যন্ত্র এবং নির্ণয়ের সীমা আলোচনা করে।
চারটি পরিশিষ্টে প্রমাণের কৌশল, আরোহ, যুক্তিবিদদের জীবনী ও গ্রিক বর্ণমালা আছে।
বারোটি অধ্যায়ের সারাংশ এবং ৭৯টি পদের পরিভাষাকোষ রয়েছে।

- [স্ক্রিন পিডিএফ পড়ুন](slc-screen-bn.pdf)
- [সমষ্টিগত সম্পাদনযোগ্য LaTeX](slc-screen-bn.tex)
- [সমস্ত প্রয়োজনীয় উৎসসহ ZIP](slc-screen-bn-sources.zip)
- [মডিউলভিত্তিক উৎস](source/locale/bn/) · [উৎস ও সংস্করণের পরিচয়](MANIFEST.json)

মূল পাঠ্যবইয়ের রচয়িতা ও সংকলক Richard Zach। পাঠ্যবইটি
[Open Logic Project](https://openlogicproject.org/)-এর সহযোগিতামূলক পাঠের উপর ভিত্তি করে।
পুনর্ব্যবহৃত বাংলা পাঠের ভিত্তি [ভারতীয় বাংলা ওপেন লজিক](https://github.com/KokunoYumeto/OpenLogic-bn-Beng-IN/releases/tag/v1.0.1-corrected-edition)।
এটি OpenAI Codex-এর এআই অনুবাদ। পাঠ্যবইয়ের অনুবাদ, সম্পাদনা ও
অক্ষরবিন্যাসে GPT-6.1 Sol (Ultra) ব্যবহৃত হয়েছে। পুনর্ব্যবহৃত বাংলা
ওপেন লজিক পাঠের অনুবাদ GPT-5.6 Sol ও GPT-6 Sol-এর, এবং সম্পাদনা
GPT-6.1 Sol-এর; নথিভুক্ত প্রচেষ্টা-স্তর Ultra।

পাঠ্যবইয়ের পাঠ ও ওপেন লজিক পাঠ [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)।
প্রচ্ছদ ও অধ্যায়-ফলকের প্রতিকৃতি [Matthew Leadbeater](https://github.com/OpenLogicProject/portraits)-এর,
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)।
জীবনীগুলির আলোকচিত্রের নিজস্ব শর্ত ও স্বীকৃতি বইয়ের শেষে এবং
[মূল অনুমতি-নথিতে](source/assets/photos/README.md) আছে।
Noto Serif Bengali ফন্টের [SIL Open Font License](source/fonts/Noto-fonts-LICENSE.txt) আলাদা।

## উৎস থেকে স্ক্রিন পিডিএফ

Windows-এ PowerShell 7, Python 3.10 বা নতুন, XeLaTeX, BibTeX, MakeIndex,
বাংলা লোকেলসহ বর্তমান Babel এবং Poppler-এর pdfinfo লাগবে। TeX বিতরণে
memoir, fontspec, ucharclasses, newtx, Baskervaldx, glossaries, cleveref,
ntheorem, answers, subfiles ও সংশ্লিষ্ট Open Logic নির্ভরতা থাকতে হবে।

    pwsh -NoProfile -File build.ps1

এই নির্দেশ পাশের source গাছ থেকে স্ক্রিন পিডিএফ তৈরি করে।
একত্র সম্পাদনযোগ্য ফাইল দিয়ে নির্মাণ করতে:

    pwsh -NoProfile -File build.ps1 -Cumulative

দ্বিতীয় নির্মাণে অন্তর্ভুক্ত LaTeX মডিউলগুলি অস্থায়ী কাজের ফোল্ডারে
লেখা হয়; ফন্ট, ছবি ও শৈলীর জন্য একই source গাছ লাগে। পরিভাষাকোষের
বাংলা (ভারত) বর্ণক্রম প্রস্তুত উৎসে সংরক্ষিত।

স্ক্রিন সংস্করণের পাশাপাশি মুদ্রণ-প্রচ্ছদের বাংলা পাঠও উৎসে আছে।
ওই দুটি মুদ্রণ-নমুনা স্ক্রিন পিডিএফের নির্মাণের অংশ নয়।
