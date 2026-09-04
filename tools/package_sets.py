import hashlib,json,pathlib,zipfile
repo=pathlib.Path(__file__).resolve().parents[1]
dist=repo/'dist';dist.mkdir(exist_ok=True)
release_ids={'OLP-0004','OLP-0005','OLP-0006','OLP-0007','OLP-0008','OLP-0009','OLP-0010','OLP-0721'}
manifest=[json.loads(s) for s in (repo/'evidence'/'SOURCE_MANIFEST.jsonl').read_text(encoding='utf-8').splitlines()]
assert {r['unit_id'] for r in manifest}==release_ids
files=[repo/'README.md',repo/'.gitignore']
for sub in ['upstream','fonts','tools','evidence']:
    files.extend(p for p in (repo/sub).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
files.extend(repo/'bn-Beng-IN'/r['source_path'] for r in manifest)
archive=dist/'openlogic-bn-Beng-IN-sets-sources.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(set(files)):
        info=zipfile.ZipInfo('OpenLogic-bn-Beng-IN/'+p.relative_to(repo).as_posix(),date_time=(2026,9,4,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes())
pdf=dist/'openlogic-bn-Beng-IN-sets.pdf';pdf.write_bytes((repo/'build'/'sets'/'openlogic-bn-sets.pdf').read_bytes())
rows=[{'filename':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [pdf,archive]]
(dist/'SHA256SUMS.txt').write_text(''.join(r['sha256']+'  '+r['filename']+'\n' for r in rows),encoding='ascii')
print(json.dumps(rows,indent=2))
