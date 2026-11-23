"""Distribute a post's empty space by the golden ratio: block gaps grow 21 -> 34 (Fibonacci),
then the rest splits 1 : phi above and below the content. Copy untouched."""
import glob, sys
from bs4 import BeautifulSoup
PHI = 1.618
G = 'flex: {g} 1 0px; min-height: 0; margin-top: -{gap}px{x}'
def sp(g, x='', gap=21): return f'<div data-gl="1" aria-hidden="true" style="{G.format(g=g, x=x, gap=gap)}"></div>'
def run(f):
    s = open(f).read()
    if 'data-gl="1"' in s: return 'skip'
    lines = s.split('\n'); offs = [0]
    for l in lines: offs.append(offs[-1] + len(l) + 1)
    soup = BeautifulSoup(s, 'html.parser')
    root = soup.find('div', style=lambda v: v and v.startswith('width: 1080px'))
    import re
    gap = int(re.search(r'gap: (\d+)px', root['style']).group(1))
    kids = [k for k in root.find_all(recursive=False) if 'position: absolute' not in (k.get('style') or '')]
    pos = lambda t: offs[t.sourceline - 1] + t.sourcepos
    ins = [(pos(kids[1]), sp(1, gap=gap))]                                   # above the content: 1
    ins += [(pos(k), sp(1, f'; max-height: {max(0, 34 - gap)}px', gap)) for k in kids[2:-1]]   # block gaps: 21 -> at most 34
    ins += [(pos(kids[-1]), sp(PHI, gap=gap))]                               # below the content: phi
    for p, t in sorted(ins, reverse=True): s = s[:p] + t + '\n' + s[p:]
    s = s.replace('margin-top: auto; display: flex; justify-content: space-between', 'margin-top: 0; display: flex; justify-content: space-between', 1)
    open(f, 'w').write(s); return len(kids)
for f in sorted(glob.glob(sys.argv[1] + '/*.dc.html')): print(f.split('/')[-1], run(f))
