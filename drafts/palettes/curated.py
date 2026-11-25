"""Curated series palettes. Hue slots from the golden-angle wheel (137.5 deg) starting at series 1's cyan; each scheme =
background/structure in its slot's hue family, an accent in the same family, and a counter-accent (second voice).
Structural roles keep series 1's OKLCH lightness; accent tints keep series 1's lightness at the accent's hue."""
import json, numpy as np, sys
from wheel import hex2oklch, oklch2hex, roles, base, contrast
S = {  # series: (name, bg, accent, second)
 'Series 1':              ('Navy & cyan',   None, None, None),
 'Series 1.1':            ('Ember',         None, None, None),
 'Ch 2 · Standard Model': ('Violet field',  '#17122B', '#B49CFF', '#6FD3C1'),
 'Ch 3 · P vs NP':        ('Graphite gold', '#121417', '#E9C46A', '#8AB4F8'),
 'Ch 4 · Foundations':    ('Deep teal',     '#0B1E1F', '#5FD6C4', '#F2C46D'),
 'Ch 5 · Cosmos':         ('Nebula rose',   '#1C1020', '#F49AC1', '#8FB8FF'),
 'Ch 6 · Gravity':        ('Forest',        '#0E1A14', '#9FD98A', '#E8D27A'),
 'Ch 7 · Cosmogony':      ('Orchid dawn',   '#1A1022', '#E3A8F5', '#F5D08A')}
ember = {'#0F1A2B':'#1E1410','#15233A':'#2A1C16','#16344A':'#3A2418','#2A3B57':'#4A3226','#A9B8CC':'#CDB8A8','#EEF2F7':'#F7EFE8','#7FD4E8':'#F2A65A','#5CC8E0':'#E8954A','#B5E6F2':'#F8CFA0','#9C8CF0':'#E06D53'}
B = dict(zip(roles, base))
def build(bg, ac, se):
    _, bc, bh = hex2oklch(bg); _, ac_c, ah = hex2oklch(ac); m = {'#0F1A2B': bg, '#7FD4E8': ac, '#9C8CF0': se}
    for r in ('#15233A', '#16344A', '#2A3B57', '#A9B8CC', '#EEF2F7'):
        L, C, _ = B[r]; m[r] = oklch2hex(L, min(C, max(bc*1.2, 0.006)) if r not in ('#A9B8CC', '#EEF2F7') else min(C, 0.03), bh)
    for r in ('#5CC8E0', '#B5E6F2'):
        L, C, _ = B[r]; m[r] = oklch2hex(L, min(ac_c, C*1.3), ah)
    return m
out = {}
for s, (nm, bg, ac, se) in S.items():
    m = {r: r for r in roles} if s == 'Series 1' else ember if s == 'Series 1.1' else build(bg, ac, se)
    out[s] = dict(name=nm, map=m, contrast=dict(text=round(contrast(m['#EEF2F7'], m['#0F1A2B']), 1), accent=round(contrast(m['#7FD4E8'], m['#15233A']), 1), second=round(contrast(m['#9C8CF0'], m['#15233A']), 1)),
                  hue=round(hex2oklch(m['#7FD4E8'])[2], 1))
    print(f"{s:24s} {nm:14s} accent hue {out[s]['hue']:6.1f}  contrast text {out[s]['contrast']}")
json.dump(out, open('curated.json', 'w'), indent=1)
