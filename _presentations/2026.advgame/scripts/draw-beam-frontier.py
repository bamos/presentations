"""Generate the editable Beam comparison with labels arranged for a wide slide.

Beam coordinates are exact from report text. Comparator coordinates were
 digitized from the supplied chart and are approximate; see the CSV.
"""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'figures/beam-frontier-data.csv').open()))
# Offsets from each point keep leaders short while separating the dense cluster.
offsets = {
    'Beam': (.18, .39, 'west'),
    'Muse Glimmer': (.18, .24, 'west'),
    'GPT-OSS 120B': (-.20, .15, 'east'),
    'Inkling': (.18, .31, 'west'),
    'Qwen 3.8 Max': (-.22, .05, 'east'),
    'Kimi K3': (.23, .30, 'west'),
    'Nemotron 3 Ultra': (-.22, -.14, 'east'),
    'GLM-5.3': (.23, -.02, 'west'),
    'Kimi K2.6': (-.22, -.47, 'east'),
    'DeepSeek V4.1 Flash': (-.22, -.58, 'east'),
    'GLM-5.2': (.23, .09, 'west'),
    'DeepSeek V4 Pro': (-.22, .0, 'east'),
}
labels = []
for row in rows:
    dx, dy, anchor = offsets[row['model']]
    x = (float(row['harmless_compliance']) - 75) * .512
    y = (float(row['harmful_refusal_or_pivot']) - 50) * .102
    labels.append((x + dx, y + dy, anchor))
out=[r'% Generated from beam-frontier-data.csv; editable vector plot.',
 r'\begin{tikzpicture}[every node/.style={anchor=center,font=\fontsize{8.5}{10}\selectfont,inner sep=1.5pt}]',
 r'\path[use as bounding box] (-1.5,-.68) rectangle (13,5.28);']
for x in range(75,101,5):
 u=(x-75)*.512
 out += [rf'\draw[gray!20] ({u:.3f},0)--({u:.3f},5.1);',rf'\node[below,text=Muted] at ({u:.3f},0) {{{x}\%}};']
for y in range(50,101,10):
 v=(y-50)*.102
 out += [rf'\draw[gray!20] (0,{v:.3f})--(12.8,{v:.3f});',rf'\node[left,text=Muted] at (0,{v:.3f}) {{{y}\%}};']
out += [r'\draw[Muted] (0,5.1)--(0,0)--(12.8,0);',
 r'\node[font=\fontsize{9}{11}\selectfont] at (6.4,-.58) {Compliance on harmless requests};',
 r'\node[rotate=90,align=center,font=\fontsize{9}{11}\selectfont] at (-1.25,2.55) {Refusal / pivot on\\harmful requests};']
# Draw leaders before text so no leader crosses a label.
for r,(lx,ly,anchor) in zip(rows,labels):
 x=(float(r['harmless_compliance'])-75)*.512;y=(float(r['harmful_refusal_or_pivot'])-50)*.102
 beam=r['model']=='Beam';color='Accent' if beam else 'Muted'
 if beam:out += [rf'\fill[Accent!14] ({x:.3f},{y:.3f}) circle (3mm);']
 out += [rf'\draw[{color}!65,thin] ({x:.3f},{y:.3f})--({lx},{ly});',
         rf'\fill[{color}] ({x:.3f},{y:.3f}) circle ({1.5 if beam else 1.0}mm);']
for r,(lx,ly,anchor) in zip(rows,labels):
 beam=r['model']=='Beam';color='Accent' if beam else 'Muted'
 style=r',font=\bfseries\fontsize{10}{12}\selectfont' if beam else ''
 out += [rf'\node[anchor={anchor},text={color},fill=white{style}] at ({lx},{ly}) {{{r["model"]}}};']
out += [r'\end{tikzpicture}']
(root/'figures/beam-frontier.tex').write_text('\n'.join(out)+'\n')
