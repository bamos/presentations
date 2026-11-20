"""Check rendered labels, numbers, notes, bounds, and logs.

This supplements the recorded visual review; it cannot establish that every
diagram or sentence is correct merely from successful compilation.
"""
from pathlib import Path
import hashlib
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
from slide_source import assembled_source
source = assembled_source()
manifest = json.loads((ROOT/'checks/manifest.json').read_text())
frames = re.findall(r'\\talkslide\{([^}]+)\}', source)
assert len(frames) == len(set(frames)) == manifest['new_count'], 'Missing/duplicate frame labels'
assert frames == [f['label'] for f in manifest['frames']], 'Manifest frame order is stale'
assert len(re.findall(r'\\speak\{', source)) == len(frames), 'One notes entry required per frame'
assert not re.search(r'\\(?:pause|only|onslide|uncover|visible)\b', source), 'Use physical frames for builds'
snm = (ROOT/'build/advgame-presentation.snm').read_text()
rendered = dict((k, int(v)) for k,v in re.findall(r'\\beamer@slide \{([^<>}]+)\}\{(\d+)\}', snm))
assert rendered == dict(zip(frames, range(1,len(frames)+1))), 'Overlay/frame pagination mismatch'

deck = pymupdf.open(ROOT/'advgame-presentation.pdf')
notes = pymupdf.open(ROOT/'speaker-notes.pdf')
assert len(deck) == len(frames)
notes_text = '\n'.join(p.get_text() for p in notes)
assert [int(n) for n in re.findall(r'\bSlide (\d+)\.', notes_text)] == list(range(1,len(frames)+1))
slide_objects = []
for page in notes:
    labels = re.findall(r'\bSlide (\d+)\.', page.get_text())
    embedded = [int(name[2:]) for _,name,invoker,_ in page.get_xobjects()
                if invoker == 0 and re.fullmatch(r'Im\d+',name)]
    assert [int(n) for n in labels] == embedded, f'Notes heading/thumbnail mismatch on page {page.number+1}'
    slide_objects.extend(embedded)
assert slide_objects == list(range(1,len(frames)+1)), 'Missing/duplicate actual slide in notes'

for name,doc in [('slides',deck),('notes',notes)]:
    for p in doc:
        if name == 'slides':
            assert abs(p.rect.width/p.rect.height - 16/9) < .002
        for x0,y0,x1,y1,*_ in p.get_text('words'):
            assert x0 >= -1 and y0 >= -1 and x1 <= p.rect.width+1 and y1 <= p.rect.height+1, \
                f'Text outside {name} page {p.number+1}: {(x0,y0,x1,y1)}'
for name in ['advgame-presentation','speaker-notes']:
    log=(ROOT/f'build/{name}.log').read_text()
    assert not re.search(r'Overfull|undefined references|Reference .+ undefined|Missing character|^! ',log,re.M), \
        f'Inspect {name}.log for overflow or unresolved content'

reference = json.loads((ROOT/'checks/numeric-reference.json').read_text())
checked=0
for label,item in reference['slides'].items():
    text=deck[rendered[label]-1].get_text().replace('−','-')
    values=[float(x) for x in re.findall(r'(?<![\w.])[-+]?\d+(?:\.\d+)?(?![\w.])', text)]
    pos=0
    for row in item['rows']:
        # Match each complete row, so numbers from unrelated parts cannot fill gaps.
        while pos <= len(values)-len(row) and values[pos:pos+len(row)] != row:
            pos += 1
        assert pos <= len(values)-len(row), f'Numeric row missing/out of order: {label}, {row}'
        pos += len(row)
        checked += len(row)

handout=ROOT/'advgame-handout.pdf'
if handout.exists():
    with pymupdf.open(handout) as doc:
        assert len(doc)==(len(deck)+3)//4
        for i,p in enumerate(doc):
            for j in range(i*4,min((i+1)*4,len(deck))):
                assert deck[j].get_text().splitlines()[0] in p.get_text(), f'Handout missing slide {j+1}'

result={'slides':len(deck),'notes_pages':len(notes),
        'numeric_values_checked':checked,'physical_frame_labels':True,'embedded_notes_slides':len(slide_objects),
        'text_bounds':'pass','build_overflows':0,
        'pdf_sha256':hashlib.sha256((ROOT/'advgame-presentation.pdf').read_bytes()).hexdigest()}
(ROOT/'build/validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
