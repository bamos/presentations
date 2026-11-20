"""Render every final slide and notes page, plus contact sheets for visual review."""
from pathlib import Path
import subprocess
import pymupdf as fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
outputs=[('advgame-presentation.pdf','slides',2.3),('speaker-notes.pdf','notes',1.3)]
if (root/'advgame-handout.pdf').exists(): outputs.append(('advgame-handout.pdf','handout',1.3))
for name,folder,scale in outputs:
 out=root/'previews'/folder;out.mkdir(parents=True,exist_ok=True)
 # Drop stale generated pages/contact sheets when the deck becomes shorter.
 for old in out.glob('*.png'):
  if old.stem.isdigit() or old.stem.startswith('contact-'): old.unlink()
 doc=fitz.open(root/name)
 # Render with Poppler independently of the PyMuPDF structural checks.
 subprocess.run(['pdftoppm','-png','-r',str(72*scale),str(root/name),str(out/'page')],check=True)
 for i in range(len(doc)):
  candidates=list(out.glob(f'page-*{i+1}.png'))
  source=next(p for p in candidates if int(p.stem.split('-')[-1])==i+1)
  source.rename(out/f'{i+1:02d}.png')
 for first in range(0,len(doc),6):
  w,h=(700,1020) if folder=='notes' else (960,570)
  sheet=Image.new('RGB',(w*2,h*3),'#ddd');draw=ImageDraw.Draw(sheet)
  for j,i in enumerate(range(first,min(first+6,len(doc)))):
   im=Image.open(out/f'{i+1:02d}.png');im.thumbnail((w-12,h-30));x=j%2*w;y=j//2*h
   sheet.paste(im,(x+6,y+25));draw.text((x+10,y+6),f'{folder} {i+1}',fill='black')
  sheet.save(out/f'contact-{first+1:02d}.png')
 print(f'Rendered {len(doc)} {folder} pages')
