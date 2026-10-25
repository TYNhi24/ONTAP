"""Read local sources without changing them; retain page/sheet/slide locations."""
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8')
import hashlib, json, zipfile, re
import xml.etree.ElementTree as ET
from collections import defaultdict
import openpyxl

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'AIQE_REVIEW' / '00_tracking'
NS = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main', 'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
records = []
for p in sorted((ROOT / 'document').rglob('*')):
    if not p.is_file() or any(x in p.relative_to(ROOT).parts for x in ['AIQE_REVIEW','.git','node_modules','.codex']):
        continue
    rel = p.relative_to(ROOT).as_posix()
    r = dict(path=rel, sha256=hashlib.sha256(p.read_bytes()).hexdigest(), units=[], media=[], status='')
    try:
        if p.suffix == '.xlsx':
            wb = openpyxl.load_workbook(p, data_only=False)
            for s in wb:
                r['units'].append({'location':'sheet '+s.title, 'text':'\n'.join(f'row {i}: '+' | '.join(f'{openpyxl.utils.get_column_letter(j)}={v}' for j,v in enumerate(row,1) if v is not None) for i,row in enumerate(s.values,1) if any(v is not None for v in row))})
            r['status']='trích xuất ô; chưa xem bố cục/hình Excel'
        elif p.suffix in ['.pptx','.docx']:
            with zipfile.ZipFile(p) as z:
                names = [n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)] if p.suffix=='.pptx' else ['word/document.xml']
                names.sort(key=lambda n:int(re.search(r'(\d+)\.xml',n).group(1)) if p.suffix=='.pptx' else 0)
                for n in names:
                    e=ET.fromstring(z.read(n))
                    texts=[t.text or '' for t in e.findall('.//a:t',NS)] if p.suffix=='.pptx' else [''.join(t.text or '' for t in para.findall('.//w:t',NS)) for para in e.findall('.//w:p',NS)]
                    r['units'].append({'location':n,'text':'\n'.join(texts)})
                r['media']=[n for n in z.namelist() if '/media/' in n]
                if p.suffix=='.pptx':
                    for n in z.namelist():
                        if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml',n):
                            r['units'].append({'location':n,'text':'\n'.join(t.text or '' for t in ET.fromstring(z.read(n)).findall('.//a:t',NS))})
                r['status']='trích xuất chữ; hình/biểu đồ chưa xem'
        elif p.suffix.lower() in ['.png','.jpg','.jpeg']:
            r['status']='chưa xem hình'
        else:
            r['units']=[{'location':'toàn văn','text':p.read_text(encoding='utf-8-sig')}]
            r['status']='đã trích xuất toàn văn; chưa đồng nghĩa đã đọc'
    except Exception as e:
        r['status']='không đọc được: '+str(e)
    records.append(r)
(OUT/'extracted-sources.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(records)==len({r['path'] for r in records})
print(f'{len(records)} sources; {sum(len(r["units"]) for r in records)} text units')
for r in records:
    print(r['path'],len(r['units']),r['status'], 'media='+str(len(r['media'])))
