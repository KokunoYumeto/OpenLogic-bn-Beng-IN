"""Build the cumulative semantic MathML reader from the checked print inputs.

Figures are vector excerpts of the same compiled PDF, not reinterpreted art.
The editable Bengali TeX remains source-aligned; this only adapts rendering.
"""
import base64, hashlib, html, json, pathlib, re, subprocess
import fitz
from bs4 import BeautifulSoup
repo=pathlib.Path(__file__).resolve().parents[1]
build=repo/'build/reader'
tex=(build/'openlogic-bn-reader.tex').read_text(encoding='utf-8')
aux=(build/'openlogic-bn-reader.aux').read_text(encoding='utf-8')
labels=dict(re.findall(r'\\newlabel\{([^{}]+)\}\{\{([^{}]*)\}',aux))
preamble,body=tex.split('\\begin{document}',1)
def arg_at(s,pos):
    while s[pos].isspace(): pos+=1
    assert s[pos]=='{',s[pos:pos+70]
    start=pos+1;depth=1;pos+=1
    while depth:
        if s[pos] in '{}' and s[pos-1]!='\\': depth+=1 if s[pos]=='{' else -1
        pos+=1
    return s[start:pos-1],pos
# Match the print reader's conditional references, rather than exposing a
# nonexistent later chapter or silently dropping both source branches.
def conditionals(s):
    while '\\oliflabeldef' in s:
        a=s.index('\\oliflabeldef'); p=a+len('\\oliflabeldef')
        label,p=arg_at(s,p);yes,p=arg_at(s,p);no,p=arg_at(s,p)
        s=s[:a]+conditionals(yes if label in labels else no)+s[p:]
    return s
body=conditionals(body)
ref_pattern=re.compile(r'\\olfileid\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}|\\olref((?:\[[^\]]*\])*)\{([^{}]*)\}')
context=['sfr','set','bas'];ref_count=0
def fix_ref(m):
    global context,ref_count
    if m[1] is not None: context=[m[1],m[2],m[3]];return m[0]
    opts=re.findall(r'\[([^\]]*)\]',m[4]); prefix=context[:3-len(opts)]+opts
    target=':'.join(prefix+[m[5]])
    assert target in labels,('Missing reader reference',target)
    ref_count+=1
    return r'\hyperref['+target+']{'+labels[target]+'}'
body=ref_pattern.sub(fix_ref,body)
# Explicit visible environment labels also serve readers who disable CSS.
names={'defn':'সংজ্ঞা','ex':'উদাহরণ','prop':'প্রতিজ্ঞা','thm':'উপপাদ্য','prob':'অনুশীলনী'}
chapter=section=theorem=problem=0;env_count=0
events=re.compile(r'\\chapter\{|\\olsection\{|\\begin\{(defn|ex|prop|thm|prob)\}(?:\[([^\]]*)\])?')
def env_labels(m):
    global chapter,section,theorem,problem,env_count
    if m[0]==r'\chapter{': chapter+=1;section=theorem=problem=0;return m[0]
    if m[0]==r'\olsection{': section+=1;theorem=0;return m[0]
    env=m[1];env_count+=1
    if env=='prob': problem+=1;number=f'{chapter}.{problem}'
    else: theorem+=1;number=f'{chapter}.{section}.{theorem}'
    title=f'{names[env]} {number}.'+(f' ({m[2]})' if m[2] else '')
    return '\\begin{'+env+'}\\textbf{'+title+'}\\par\n'
body=events.sub(env_labels,body)
body=body.replace('\\nicefrac','\\frac')
# Pandoc's MathML converter accepts aligned rows, not multline shove commands.
body=body.replace(r'\begin{multline*}',r'\begin{gathered}').replace(r'\end{multline*}',r'\end{gathered}')
for name in ('shoveleft','shoveright'):
    while '\\'+name+'{' in body:
        a=body.index('\\'+name+'{');content,end=arg_at(body,a+len(name)+1)
        body=body[:a]+content+body[end:]
# Wrap gathered rows in a real display math environment.
body=body.replace(r'\begin{gathered}',r'\[\begin{gathered}').replace(r'\end{gathered}',r'\end{gathered}\]')
for name in ('union','intersection','difference','function','surjective','injective','bijective','composition'):
    body=re.sub(r'\\olasset(?:\[[^\]]*\])?\{assets/diagrams/'+name+r'\.tikz\}',lambda m:'DIAGRAM'+name.upper()+'TOKEN',body)
# The source overlays a vertical stroke at the middle of a right arrow.
# MathML has this as U+21F8; Pandoc does not implement the TeX ooalign primitive.
partial_arrow_count=len(re.findall(r'\\pto\b',body))
body=re.sub(r'\\pto\b',lambda m:r'\text{PARTIALARROWTOKEN}',body)
graph=re.compile(r'\\begin\{align\*\}(\s*&\s*\\begin\{tikzpicture\}.*?\\end\{align\*\})',re.S)
def graph_replace(m):
    middle=m[1].index('\\intertext');caption,end=arg_at(m[1],middle+len('\\intertext'))
    return '\nDIAGRAMGRAPHONETOKEN\n\n'+caption+'\n\nDIAGRAMGRAPHTWOTOKEN\n'
body,count=graph.subn(graph_replace,body);assert count==1
body,count=re.subn(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}','DIAGRAMTREETOKEN',body,flags=re.S);assert count==1
source=build/'semantic-input.tex';source.write_text(preamble+'\\begin{document}'+body,encoding='utf-8')
out=build/'openlogic-bn-reader.html'
result=subprocess.run(['pandoc',str(source),'-f','latex','-t','html5','--standalone','--mathml','--toc','--metadata','lang=bn-IN','--metadata','title=ওপেন লজিক: সেট, সম্পর্ক ও অপেক্ষক','-o',str(out)],cwd=build,capture_output=True,text=True,encoding='utf-8')
(build/'html-build-log.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
assert result.returncode==0,result.stderr
assert not result.stderr.strip(),result.stderr
soup=BeautifulSoup(out.read_text(encoding='utf-8'),'html.parser')
assert not soup.select('span.math'), 'Unconverted TeX math'
partial_tags=soup.find_all('mtext',string='PARTIALARROWTOKEN')
assert len(partial_tags)==partial_arrow_count,(len(partial_tags),partial_arrow_count)
for tag in partial_tags:
    tag.name='mo';tag.string='⇸';tag['title']='আংশিক অপেক্ষকের তির'
for tag in soup.find_all('annotation'):
    if tag.string and 'PARTIALARROWTOKEN' in tag.string:
        tag.string=tag.string.replace(r'\text{PARTIALARROWTOKEN}',r'\pto')
assert 'PARTIALARROWTOKEN' not in str(soup)
doc=fitz.open(build/'openlogic-bn-reader.pdf')
groups=[]
for pageno,page in enumerate(doc):
    boxes=[d['rect'] for d in page.get_drawings() if d['rect'].width>=3 or d['rect'].height>=3]
    merged=[]
    for box in sorted(boxes,key=lambda r:r.y0):
        if merged and box.y0<=merged[-1].y1+10: merged[-1]|=box
        else: merged.append(fitz.Rect(box))
    groups.extend((pageno,r) for r in merged if r.width>30 and r.height>30)
figures=[('UNION','দুটি সেটের সংযোগ: যেকোনো একটি সেটে থাকা অংশ চিহ্নিত।'),('INTERSECTION','দুটি সেটের ছেদ: উভয় সেটে থাকা সাধারণ অংশ চিহ্নিত।'),('DIFFERENCE','সেটের অন্তর: প্রথম সেটে আছে কিন্তু দ্বিতীয়টিতে নেই এমন অংশ চিহ্নিত।'),('GRAPHONE','নির্দেশিত গ্রাফ: 1 থেকে 1, 2 ও 3-এ এবং 2 থেকে 3-এ তির; 4 বিচ্ছিন্ন শীর্ষ।'),('GRAPHTWO','একই প্রান্তসমষ্টির গ্রাফ, কিন্তু শীর্ষসমষ্টিতে 4 নেই।'),('TREE','মূল r-এর সন্তান a ও b; a-এর সন্তান c, d ও e।')]
figures.extend([('FUNCTION','অপেক্ষক: সংজ্ঞাক্ষেত্রের প্রত্যেক উপাদান থেকে সহসংজ্ঞাক্ষেত্রের একটিমাত্র উপাদানে তির যায়।'),('SURJECTIVE','সমাপতিত অপেক্ষক: সহসংজ্ঞাক্ষেত্রের প্রত্যেক উপাদানে অন্তত একটি তির এসে পৌঁছায়।'),('INJECTIVE','একৈক অপেক্ষক: ভিন্ন ইনপুটের তির ভিন্ন আউটপুটে পৌঁছায়।'),('BIJECTIVE','একৈক সমাপতিত অপেক্ষক: সহসংজ্ঞাক্ষেত্রের প্রত্যেক উপাদানে ঠিক একটি তির এসে পৌঁছায়।'),('COMPOSITION','অপেক্ষকের মিশ্রণ: প্রথমে f দিয়ে A থেকে B-তে, তারপর g দিয়ে B থেকে C-তে যাওয়া হয়; সরাসরি তিরগুলি g বৃত্ত f বোঝায়।')])
assert len(groups)==len(figures),(len(groups),'Unexpected diagram grouping')
figure_receipts=[]
for (pageno,rect),(name,alt) in zip(groups,figures):
    rect=rect+(-4,-4,4,4)
    clipdoc=fitz.open();page=clipdoc.new_page(width=rect.width,height=rect.height)
    page.show_pdf_page(page.rect,doc,pageno,clip=rect)
    svg=page.get_svg_image(text_as_path=True)
    tag=soup.new_tag('img',alt=alt);tag['src']='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode();tag['class']='diagram'
    token=soup.find(string=lambda t:t and 'DIAGRAM'+name+'TOKEN' in t)
    assert token is not None,name
    token.replace_with(tag)
    figure_receipts.append({'name':name,'pdf_page':pageno+1,'clip':list(rect),'svg_sha256':hashlib.sha256(svg.encode()).hexdigest()})
# Embed pinned fonts so the single HTML file works offline.
style=soup.new_tag('style')
regular=base64.b64encode((repo/'fonts/NotoSerifBengali-Regular.ttf').read_bytes()).decode()
bold=base64.b64encode((repo/'fonts/NotoSerifBengali-Bold.ttf').read_bytes()).decode()
style.string=f'''@font-face{{font-family:BN;src:url(data:font/ttf;base64,{regular})}}@font-face{{font-family:BN;src:url(data:font/ttf;base64,{bold});font-weight:700}}
html{{background:#f3f1ed;color:#17232c}}body{{max-width:52rem;margin:2rem auto;padding:2.5rem;background:white;font-family:BN,serif;font-size:18px;line-height:1.8}}h1,h2,h3{{line-height:1.5}}a{{color:#155c89}}math{{font-family:'Cambria Math',math}}math[display=block]{{display:block;overflow-x:auto;padding:1rem 0}}.diagram{{display:block;max-width:100%;max-height:25rem;margin:1rem auto}}.defn,.prop,.thm,.prob{{border-left:3px solid #78909c;padding:.3rem 1rem;margin:1.2rem 0}}.translationnote{{background:#eef4f6;padding:1rem}}nav{{border:1px solid #ccc;padding:1rem}}@media(max-width:650px){{body{{margin:0;padding:1rem;font-size:17px}}}}'''
soup.head.append(style)
main=soup.new_tag('main',id='reader-content')
for child in list(soup.body.contents): main.append(child.extract())
soup.body.append(main)
license_box=soup.new_tag('details')
license_title=soup.new_tag('summary');license_title.string='ব্যবহৃত ফন্টের লাইসেন্স';license_box.append(license_title)
license_text=soup.new_tag('pre');license_text.string=(repo/'fonts/Noto-fonts-LICENSE.txt').read_text(encoding='utf-8');license_box.append(license_text)
main.append(license_box)
ids=[t['id'] for t in soup.find_all(id=True)]
assert len(ids)==len(set(ids)),'Duplicate HTML anchors'
broken=[a['href'] for a in soup.select('a[href^="#"]') if a['href'][1:] not in ids]
assert not broken,broken
section_count=len(re.findall(r'\\olsection\{',body))
assert len(soup.find_all('h2'))==section_count==21
assert len(soup.select('div.defn,div.ex,div.prop,div.thm,div.prob'))==env_count
assert len(soup.select('img.diagram'))==len(figures)==11
assert 'DIAGRAM' not in soup.get_text()
out.write_text(str(soup),encoding='utf-8')
receipt={'html_bytes':out.stat().st_size,'html_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'input_tex_sha256':hashlib.sha256((build/'openlogic-bn-reader.tex').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((build/'openlogic-bn-reader.pdf').read_bytes()).hexdigest(),'sections':section_count,'numbered_environments':env_count,'mathml_expressions':len(soup.find_all('math')),'partial_function_arrows':partial_arrow_count,'resolved_source_references':ref_count,'broken_internal_links':broken,'figures':figure_receipts,'offline_fonts':True,'pandoc_warnings':0,'visual_status':'Browser visual inspection pending: local-file URL policy rejected navigation; no bypass attempted.'}
(build/'html-receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='figures'},ensure_ascii=False))
