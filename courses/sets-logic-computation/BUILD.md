# সেট, যুক্তি, গণনা — উৎস থেকে স্ক্রিন PDF

উৎস-ZIP খুলে ফাইল ও ফোল্ডারগুলির বিন্যাস অক্ষত রাখুন। বইটি সাজাতে যে LaTeX শৈলী, গ্রন্থপঞ্জি, ছবি, বাংলা ফন্ট ও ফন্ট-ম্যাপ লাগে, সেগুলি এই বিন্যাসেই খোঁজা হয়।

## যা লাগবে

- একটি পূর্ণ ও হালনাগাদ TeX বিতরণে XeLaTeX, xdvipdfmx, BibTeX ও MakeIndex রাখুন। নিচের নির্দেশগুলি PowerShell 7.4 বা পরবর্তী সংস্করণে চালানো যায়।
- TeX বিতরণে বাংলা লোকেলসহ Babel এবং memoir, fontspec, ucharclasses, glossaries, natbib, newtx, txfonts, baskervaldx, mathalpha, ntheorem, cleveref, hyperref, TikZ/PGF, forest, prooftrees, bussproofs, answers ও subfiles এবং তাদের নির্ভরতা লাগবে। XeLaTeX-কে Latin Modern Roman, Sans ও Mono ফন্ট খুঁজে পেতে হবে।
- বাংলা অক্ষরের জন্য বইটি উৎসের মূল ফোল্ডারের `fonts/` থেকে Noto Serif Bengali Regular ও Bold ব্যবহার করে। বইয়ের ফোল্ডারে STIX Two Math-এর অক্ষররেখা থেকে তৈরি ছয়টি Type 1 ফন্ট আছে। এই ফন্টের মাপ ও গাণিতিক বিন্যাসের জন্য TeX বিতরণের NewTX মাপের ফাইল এবং অন্য প্রয়োজনীয় ফন্টগুলি লাগে। বইয়ের ফোল্ডারের `fonts/`-এ `bn-slc-newtx-unicode.map` ও তার সাতটি CMap আছে। গাণিতিক প্রতীক খোঁজা ও অনুলিপি করার জন্য ফন্ট ও ম্যাপের আপেক্ষিক অবস্থান অক্ষত রাখুন। ফন্টের উৎস, স্বীকৃতি ও লাইসেন্স দেখুন। [গাণিতিক ফন্টের স্বীকৃতি](locale/bn/courses/sets-logic-computation/STIX-MATH-CREDITS.md)

## কোন LaTeX ফাইল চালাবেন

- মডিউলভিত্তিক উৎসের জন্য `locale/bn/courses/sets-logic-computation/slc-screen.tex` ব্যবহার করুন। ফল হবে `slc-screen.pdf`।
- সমষ্টিগত সম্পাদনযোগ্য উৎসের জন্য ওই একই ফোল্ডারের `slc-screen-bn.tex` ব্যবহার করুন। আলাদা করে নামানো সমষ্টিগত ফাইলটিও উৎস-ZIP-এর ওই ফোল্ডারে রাখুন। ফল হবে `slc-screen-bn.pdf`। এই ফাইলটি নির্মাণের সময় সন্নিবিষ্ট LaTeX পাঠ পাশেই আলাদা ফাইলে লেখে। শৈলী, ছবি, গ্রন্থপঞ্জি ও ফন্টের জন্য উৎস-ZIP-এর ফোল্ডারগুলি সঙ্গে রাখুন।

## নির্মাণের ধাপ

উৎস-ZIP যে মূল ফোল্ডারে খুলেছেন, সেখান থেকে নিচের নির্দেশগুলি চালান। সমষ্টিগত উৎস ব্যবহার করলে শুধু `$entry`-র মান `'slc-screen-bn.tex'` করুন। প্রথম XeLaTeX ধাপ গ্রন্থপঞ্জি ও পরিভাষাকোষের সহায়ক ফাইল তৈরি করে। BibTeX `natbib-oup.bst` শৈলী ও `bib/open-logic.bib` ব্যবহার করে। MakeIndex উৎসে দেওয়া বাংলা বর্ণক্রমের চাবি অনুসারে পরিভাষাকোষ সাজায়।

```powershell
Set-Location 'locale/bn/courses/sets-logic-computation'

$entry = 'slc-screen.tex'
$job = [IO.Path]::GetFileNameWithoutExtension($entry)

& {
    $ErrorActionPreference = 'Stop'
    $PSNativeCommandUseErrorActionPreference = $true
    $savedBstInputs = $env:BSTINPUTS
    $env:BSTINPUTS = (Resolve-Path '../../../../bib').Path + [IO.Path]::PathSeparator
    try {
        $texArgs = @(
            '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
            '-file-line-error', '-recorder', "-jobname=$job", $entry
        )

        xelatex @texArgs
        bibtex $job
        makeindex -s "$job.ist" -t "$job.glg" -o "$job.gls" "$job.glo"

        xelatex @texArgs
        bibtex $job
        makeindex -s "$job.ist" -t "$job.glg" -o "$job.gls" "$job.glo"

        xelatex @texArgs
        xelatex @texArgs
    }
    finally {
        $env:BSTINPUTS = $savedBstInputs
    }
}
```

PDF ও `.log` বইয়ের ফোল্ডারেই পাবেন। LaTeX আবার চালাতে বললে বইয়ের ফোল্ডার থেকে একই `$entry` ও `$job` দিয়ে XeLaTeX ধাপটি পুনরাবৃত্তি করুন। গ্রন্থপঞ্জির সূত্র বা পরিভাষাকোষের সহায়ক ফাইল বদলালে যথাক্রমে BibTeX বা MakeIndex আবার চালিয়ে তারপর XeLaTeX চালান। কোনও ধাপে ত্রুটি হলে XeLaTeX-এর `.log`, BibTeX-এর `.blg` বা MakeIndex-এর `.glg`-এ সংশ্লিষ্ট বার্তাটি দেখুন। ফন্ট বা ম্যাপ না মিললে TeX বিতরণের ফন্টগুলি ও ZIP-এর আপেক্ষিক ফোল্ডারগুলি পরীক্ষা করুন।

PDF-এ সূচিপত্র, গ্রন্থপঞ্জি, পরিভাষাকোষ ও ছবির স্বীকৃতি দেখা যাচ্ছে কি না দেখে নিন। গণিতের কয়েকটি সূত্রে PDF থেকে পাঠ অনুলিপি করেও পরীক্ষা করুন।
