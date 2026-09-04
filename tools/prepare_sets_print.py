import hashlib,pathlib,re,shutil
repo=pathlib.Path(__file__).resolve().parents[1]
state=pathlib.Path(r'C:\interlanguage-task-state\openlogic-bn-Beng-IN')
build=repo/'build'/'sets'; build.mkdir(parents=True,exist_ok=True)
fonts=repo/'fonts'; fonts.mkdir(exist_ok=True)
for name,digest in [('NotoSerifBengali-Regular.ttf','04935aea18655c451d05b1d4bb5bdc835226a221663f89a2ecfbcfdc4483e399'),('NotoSerifBengali-Bold.ttf','f752131cd292f3e0fd7a25c8fc86f5424062bc06e29f6dfadcb3c09ff4881dd0'),('Noto-fonts-LICENSE.txt','0dab92d0544f7b233403f14b84a663bdbfa746982eda629e7f4f9ffe1b036feb')]:
    if (fonts/name).exists():
        assert hashlib.sha256((fonts/name).read_bytes()).hexdigest()==digest
    else:
        data=(state/'canon'/'originals'/name).read_bytes(); assert hashlib.sha256(data).hexdigest()==digest
        (fonts/name).write_bytes(data)
parts=[(repo/'tools'/'sets-preamble.tex').read_text(encoding='utf-8')]
for name in ['basics','subsets','important-sets','unions-and-intersections','pairs-and-products','russells-paradox','proofs-about-sets']:
    text=(repo/'bn-Beng-IN'/'content'/'sets-functions-relations'/'sets'/f'{name}.tex').read_text(encoding='utf-8')
    text=text.split('\\begin{document}',1)[1].rsplit('\\end{document}',1)[0]
    text=re.sub(r'!!(\^)?(a)?\{element\}(s)?',lambda m:('একটি ' if m[2] else '')+'উপাদান',text)
    assert '!!' not in text
    parts.append(text)
parts.append('\\end{document}\n')
(build/'openlogic-bn-sets.tex').write_text('\n'.join(parts),encoding='utf-8')
print('Prepared eight-unit Sets chapter, including the alternative proof section, with pinned font bytes.')
