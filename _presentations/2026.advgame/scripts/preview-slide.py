"""Build selected slides with the actual deck template, then render PNGs."""
from pathlib import Path
import argparse, os, re, shutil, subprocess, sys
import pymupdf
from slide_source import ROOT, frame_labels
parser=argparse.ArgumentParser()
parser.add_argument('labels',nargs='+',help='Stable slide labels, e.g. beam-rl')
args=parser.parse_args()
labels=[x for item in args.labels for x in item.split(',')]
known=frame_labels()
for label in labels:
    if label not in known:parser.error(f'Unknown slide: {label}')
job='preview-'+labels[0]
out=ROOT/'build'/'slide-previews';out.mkdir(parents=True,exist_ok=True)
env=os.environ.copy();env['PATH']='/Library/TeX/texbin:'+env.get('PATH','')
command=['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error',
         '-outdir='+str(out),'-jobname='+job,
         '-usepretex=\\def\\previewframes{'+','.join(labels)+'}',
         'advgame-presentation.tex']
with (out/(job+'-build.txt')).open('w') as log:
    result=subprocess.run(command,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
if result.returncode:
    print((out/(job+'-build.txt')).read_text()[-6000:]);sys.exit(result.returncode)
pdf=out/(job+'.pdf')
log=(out/(job+'.log')).read_text()
if re.search(r'Overfull|Missing character|^! ',log,re.M):
    print('Layout warning: inspect '+str(out/(job+'.log')))
selected=[x for x in known if x in labels]
with pymupdf.open(pdf) as doc:
    assert len(doc)==len(selected),(len(doc),selected)
    for page,label in zip(doc,selected):
        # A single-slide PDF is convenient for reviewing diagrams outside the deck.
        one=pymupdf.open();one.insert_pdf(doc,from_page=page.number,to_page=page.number)
        one.save(out/(label+'.pdf'));one.close()
        subprocess.run(['pdftoppm','-png','-r','165.6','-singlefile',
                        str(out/(label+'.pdf')),str(out/label)],check=True)
        print(f'{label}: {out/(label+".png")}')
