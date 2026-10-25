"""Check local Markdown links, corpus integrity and question-bank shape."""
from pathlib import Path
import hashlib, json, re, sys
from urllib.parse import unquote

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'AIQE_REVIEW'
errors=[]
links=0
for p in OUT.rglob('*.md'):
    t=p.read_text(encoding='utf-8')
    if '\ufffd' in t:
        errors.append(f'Invalid replacement character: {p.relative_to(OUT)}')
    if len(re.findall(r'\w\?\w',t))>5:
        errors.append(f'Possible lost Vietnamese encoding: {p.relative_to(OUT)}')
    # shortcut: inline links only, extend if reference-style links are introduced.
    for raw in re.findall(r'\]\((<[^>]+>|[^)\n]+)\)',t):
        dest=raw.strip().strip('<>')
        if re.match(r'^[a-z]+:',dest) or dest.startswith('#'):
            continue
        dest=unquote(dest.split('#',1)[0])
        if not dest:
            continue
        links+=1
        if not (p.parent/dest).exists():
            errors.append(f'Broken link: {p.relative_to(OUT)} -> {dest}')
records=json.loads((OUT/'00_tracking/extracted-sources.json').read_text(encoding='utf-8'))
for r in records:
    p=ROOT/r['path']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:
        errors.append('Original changed: '+r['path'])
questions=0
interviews=0
for p in (OUT/'04_quiz').glob('*.md'):
    if 'answers' in p.stem:
        continue
    t=p.read_text(encoding='utf-8')
    q=len(re.findall(r'^## (?:Câu )?[A-Z]?\d+(?:[.:]|\s*$)',t,re.M))
    options=len(re.findall(r'^(?:- )?(?:\*\*)?[A-D][.)](?:\*\*)?\s',t,re.M))
    if q==0 or options!=q*4:
        errors.append(f'Question shape {p.name}: {q} questions, {options} options')
    questions+=q
for p in (OUT/'03_interview').glob('*.md'):
    interviews+=len(re.findall(r'^## (?:Câu )?[A-Z]?\d+(?:[.:]|\s*$)',p.read_text(encoding='utf-8'),re.M))
report=dict(originals=len(records),markdown_files=len(list(OUT.rglob('*.md'))),checked_local_links=links,quiz_questions=questions,interview_questions=interviews,errors=errors)
(OUT/'00_tracking/validation-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert not errors, 'Review validation failed'
