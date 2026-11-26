"""Old maps slide: the Tree of Life in the grid's equations; the lightning flash (descent) as the order of derivation; the middle pillar as the symmetry chain."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
BG, PANEL, INK, MUTED, LINE = '#1A1022', '#221530', '#F7EEFB', '#BFA9CC', '#3A2748'
THESIS, ANTI, SYN, FLASH = '#E3A8F5', '#8FB8FF', '#F5D08A', '#FFB38A'
SY, XS = 0.80, 1.55
S0 = {'Keter': (0, 0, SYN, r'$e^{i\pi}+1=0$', 'balanced zero'),
      'Chokmah': (1, 0.6, THESIS, r'$e^{+i\omega t}$', 'thesis'),
      'Binah': (-1, 0.6, ANTI, r'$e^{-i\omega t}$', 'antithesis'),
      'Chesed': (1, 2.0, THESIS, r'$2\,\mathrm{Re}(O^*R)$', 'cross terms: quantum'),
      'Gevurah': (-1, 2.0, ANTI, r'$\omega=\omega$ terms $\geq 0$', 'meeting: gravity'),
      'Tiferet': (0, 2.7, SYN, r'$|O+R|^2$', 'the record'),
      'Netzach': (1, 4.0, THESIS, r'$M^2$ vs $M$', 'held tones'),
      'Hod': (-1, 4.0, ANTI, r'$p\,w^{\beta}$', 'hearing'),
      'Yesod': (0, 4.8, SYN, r'$\Delta S\leq h/2$', 'the beat'),
      'Malkuth': (0, 6.1, SYN, r'$G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}$', 'matter and its laws')}
S = {k: (x*XS, y*SY, *r) for k, (x, y, *r) in S0.items()}
P = [('Keter','Chokmah'),('Keter','Binah'),('Keter','Tiferet'),('Chokmah','Binah'),('Chokmah','Tiferet'),('Chokmah','Chesed'),('Binah','Tiferet'),
     ('Binah','Gevurah'),('Chesed','Gevurah'),('Chesed','Tiferet'),('Chesed','Netzach'),('Gevurah','Tiferet'),('Gevurah','Hod'),('Tiferet','Netzach'),
     ('Tiferet','Yesod'),('Tiferet','Hod'),('Netzach','Hod'),('Netzach','Yesod'),('Netzach','Malkuth'),('Hod','Yesod'),('Hod','Malkuth'),('Yesod','Malkuth')]
order = ['Keter','Chokmah','Binah','Chesed','Gevurah','Tiferet','Netzach','Hod','Yesod','Malkuth']
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
fig.text(0.06, 0.95, 'The Tree in the grid’s equations', color=INK, fontsize=32, fontweight='bold')
fig.text(0.06, 0.918, 'The lightning flash runs down the order in which the record is built', color=MUTED, fontsize=16.5)
ax = fig.add_axes([0.0, 0.205, 1.0, 0.70]); ax.set_facecolor(BG); ax.axis('off'); ax.set_aspect('equal')
ax.set_xlim(-2.75, 2.75); ax.set_ylim(6.1*SY + 0.95, -0.55)
for a, b in P:
    (xa, ya, *_), (xb, yb, *_) = S[a], S[b]; ax.plot([xa, xb], [ya, yb], color='#5A4870', lw=1.6, zorder=1)
fx = [S[k][0] for k in order]; fy = [S[k][1] for k in order]
ax.plot(fx, fy, color=FLASH, lw=3.2, zorder=2, alpha=0.95)
for i, k in enumerate(order):
    x, y, c, eq, word = S[k]
    ax.add_patch(Circle((x, y), 0.3, fc=PANEL, ec=c, lw=2.6, zorder=4))
    ax.text(x, y - 0.06, k, color=INK, fontsize=11.5, ha='center', va='center', fontweight='bold', zorder=5)
    ax.text(x, y + 0.13, str(i + 1), color=FLASH, fontsize=10, ha='center', va='center', zorder=5)
    dx = 0.36 if x > 0.1 else (-0.36 if x < -0.1 else 0.36)
    ha = 'left' if dx > 0 else 'right'
    if k in ('Tiferet', 'Yesod'): dx, ha = 0.36, 'left'
    if k == 'Keter': dx, ha = -0.36, 'right'
    if k == 'Malkuth': ax.text(0, y + 0.55, eq, color=INK, fontsize=15, ha='center', va='center', zorder=5); ax.text(0, y + 0.8, word, color=MUTED, fontsize=11.5, ha='center', va='center')
    else:
        ax.text(x + dx, y - 0.08, eq, color=INK, fontsize=14.5, ha=ha, va='center', zorder=5, bbox=dict(boxstyle='round,pad=0.15', fc=BG, ec='none'))
        ax.text(x + dx, y + 0.15, word, color=MUTED, fontsize=11, ha=ha, va='center', zorder=5, bbox=dict(boxstyle='round,pad=0.15', fc=BG, ec='none'))
for k, dim in (('Keter', 'E8: 248'), ('Tiferet', 'E6: 78'), ('Yesod', 'SU(3)³: 24'), ('Malkuth', 'SU(3)×SU(2)×U(1): 12')):
    x, y = S[k][0], S[k][1]
    ax.text(x + (0.36 if k == 'Keter' else -0.36), y + (0.0), dim, color=SYN, fontsize=11.5, ha=('left' if k == 'Keter' else 'right'), va='center', fontweight='bold', zorder=6, bbox=dict(boxstyle='round,pad=0.15', fc=BG, ec='none'))
items = [(FLASH, 'Down the flash: balance, its two hands, the two kinds of term, the record, held tones, hearing, the beat, matter. Each sphere is the step the one above forces.'),
         (SYN, 'Down the middle pillar, symmetry narrows: E8 (248) holds E6 (78) with the family SU(3); a Z₃ holonomy of the grain breaks E6 to SU(3)³ (24) at gravity’s meeting (t142), and that breaks to the forces we see (12) at the cut.'),
         (THESIS, 'Up the paths, the climb: capacity grows by what is heard, d ln a = d ln e, from 1/T to 1.')]
import textwrap
for i, (c, s) in enumerate(items):
    y = 0.172 - i*0.052
    fig.patches.append(Circle((0.07, y - 0.002), 0.008, color=c, transform=fig.transFigure, figure=fig))
    fig.text(0.095, y, '\n'.join(textwrap.wrap(s, 100)), color=INK, fontsize=12.5, va='center', linespacing=1.25)
fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('tree_equations.png', facecolor=BG); print('ok')
