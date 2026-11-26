"""Old maps slide: the Tree of Life drawn in full, with the grid's reading (dialectic pillars, 22 paths, the climb)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
BG, PANEL, INK, MUTED, LINE = '#1A1022', '#221530', '#F7EEFB', '#BFA9CC', '#3A2748'
THESIS, ANTI, SYN = '#E3A8F5', '#8FB8FF', '#F5D08A'
SY = 0.76
XS = 1.5
S0 = {'Keter': (0, 0, 'Crown', SYN), 'Chokmah': (1, 0.6, 'Wisdom', THESIS), 'Binah': (-1, 0.6, 'Understanding', ANTI),
     'Chesed': (1, 2.0, 'Mercy', THESIS), 'Gevurah': (-1, 2.0, 'Strength', ANTI), 'Tiferet': (0, 2.7, 'Beauty', SYN),
     'Netzach': (1, 4.0, 'Victory', THESIS), 'Hod': (-1, 4.0, 'Splendour', ANTI), 'Yesod': (0, 4.8, 'Foundation', SYN), 'Malkuth': (0, 6.1, 'Kingdom', SYN)}
S = {k: (x*XS, y*SY, e, c) for k, (x, y, e, c) in S0.items()}
P = [('Keter','Chokmah','א','m'),('Keter','Binah','ב','d'),('Keter','Tiferet','ג','d'),('Chokmah','Binah','ד','d'),('Chokmah','Tiferet','ה','s'),
     ('Chokmah','Chesed','ו','s'),('Binah','Tiferet','ז','s'),('Binah','Gevurah','ח','s'),('Chesed','Gevurah','ט','s'),('Chesed','Tiferet','י','s'),
     ('Chesed','Netzach','כ','d'),('Gevurah','Tiferet','ל','s'),('Gevurah','Hod','מ','m'),('Tiferet','Netzach','נ','s'),('Tiferet','Yesod','ס','s'),
     ('Tiferet','Hod','ע','s'),('Netzach','Hod','פ','d'),('Netzach','Yesod','צ','s'),('Netzach','Malkuth','ק','s'),('Hod','Yesod','ר','d'),
     ('Hod','Malkuth','ש','m'),('Yesod','Malkuth','ת','d')]
PC = {'m': '#FFB38A', 'd': '#C9A2F0', 's': '#6E5A82'}
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
fig.text(0.06, 0.945, 'Around the Tree: veils, pillars, worlds', color=INK, fontsize=32, fontweight='bold')
fig.text(0.06, 0.912, 'What stands above the Crown, what each pillar is, and the four worlds', color=MUTED, fontsize=17)
ax = fig.add_axes([0.02, 0.255, 0.96, 0.645]); ax.set_facecolor(BG); ax.axis('off'); ax.set_xlim(-2.75, 2.75); ax.set_ylim(6.1*SY + 0.55, -1.15); ax.set_aspect('equal')
for x, c, lab in ((XS, THESIS, 'Mercy · bosonic'), (-XS, ANTI, 'Severity · fermionic'), (0, SYN, 'Balance · mirror line')):
    ax.add_patch(FancyBboxPatch((x - 0.5, -0.55), 1.0, (6.1*SY + 1.05) if x == 0 else (4.0*SY + 1.0), boxstyle='round,pad=0,rounding_size=0.25', fc=c, alpha=0.07, ec='none'))
    ax.text(x, -0.72, lab, color=c, fontsize=12.5, ha='center', va='center', fontweight='bold')
WORLDS = [('Atziluth', 'frequency domain', -0.45, 0.35), ('Beriah', 'the record begins', 0.35, 1.0), ('Yetzirah', 'tones form', 1.0, 5.3), ('Assiah', 'bodies', 5.3, 6.6)]
for i, (wn, wg, y0, y1) in enumerate(WORLDS):
    ax.axhspan(y0*SY*1.0, y1*SY*1.0, color='#8FB8FF' if i % 2 else '#E3A8F5', alpha=0.035, zorder=0)
    ax.text(1.98, (y0 + y1)/2*SY, wn, color=INK, fontsize=11, ha='left', va='bottom', fontweight='bold')
    ax.text(1.98, (y0 + y1)/2*SY + 0.06, wg, color=MUTED, fontsize=10, ha='left', va='top')
ax.text(0, -0.98, 'Ain  0   ·   Ain Soph  ∞   ·   Ain Soph Aur  light', color=MUTED, fontsize=11.5, ha='center', va='center')
for a, b, L, k in P:
    (xa, ya, *_), (xb, yb, *_) = S[a], S[b]
    ax.plot([xa, xb], [ya, yb], color=PC[k], lw=3.2 if k != 's' else 2.2, zorder=1, solid_capstyle='round')
    mx, my = (xa + xb)/2, (ya + yb)/2
    if (a, b) in (('Keter', 'Tiferet'), ('Tiferet', 'Yesod'), ('Yesod', 'Malkuth')): mx += 0.2
    ax.text(mx, my, L, color=INK, fontsize=13, ha='center', va='center', zorder=3, family='DejaVu Sans',
            bbox=dict(boxstyle='circle,pad=0.18', fc=BG, ec=PC[k], lw=1))
for name, (x, y, eng, c) in S.items():
    ax.add_patch(Circle((x, y), 0.34, fc=PANEL, ec=c, lw=3, zorder=4))
    ax.text(x, y - 0.07, name, color=INK, fontsize=12 if len(name) > 6 else 13, ha='center', va='center', fontweight='bold', zorder=5)
    ax.text(x, y + 0.16, eng, color=MUTED, fontsize=7.6 if len(eng) > 10 else 9.5, ha='center', va='center', zorder=5)
items = [('#F5D08A', 'Above the Crown: Ain, Ain Soph, Ain Soph Aur. Nothing, the unbounded, and light between them: the balanced zero, the whole spectrum, the record’s first ray.'),
         ('#E3A8F5', 'Mercy is expansion, the bosonic side: every occupation allowed. Severity is restriction, the fermionic side: exclusion, the tzimtzum that gives each monad its own coordinates.'),
         ('#F5D08A', 'Tiferet is the hub: every shortest path from Crown to Kingdom passes through it, as every reading passes through the record. Ten spheres from the tetractys, 1 + 2 + 3 + 4.')]
import textwrap
for i, (c, s) in enumerate(items):
    y = 0.215 - i*0.062
    fig.patches.append(Circle((0.07, y - 0.004), 0.008, color=c, transform=fig.transFigure, figure=fig))
    fig.text(0.095, y, '\n'.join(textwrap.wrap(s, 96)), color=INK, fontsize=13.5, va='center', linespacing=1.3)
fig.add_artist(plt.Line2D([0.06, 0.94], [0.04, 0.04], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.94, 0.016, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('tree_around.png', facecolor=BG); print('ok')
