"""Old maps slide: the downward tree. The upward and downward Fibonacci series, the golden annulus between them, and the zeta mirror."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
BG, INK, MUTED, LINE = '#1A1022', '#F7EEFB', '#BFA9CC', '#3A2748'
UP, DOWN, VEIL, GOLD = '#E3A8F5', '#8FB8FF', '#FFB38A', '#F5D08A'
phi = (1 + 5**0.5)/2
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
fig.text(0.06, 0.95, 'The downward tree', color=INK, fontsize=32, fontweight='bold')
fig.text(0.06, 0.918, 'Each tree’s infinity is the other’s finite side; the veil lies between', color=MUTED, fontsize=16.5)
ax = fig.add_axes([0.05, 0.40, 0.9, 0.49]); ax.set_facecolor(BG); ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.25, 2.25)
ax.add_patch(Circle((0, 0), 2.2, color=DOWN, alpha=0.18, lw=0))
ax.add_patch(Wedge((0, 0), phi, 0, 360, width=phi - 1/phi, color=VEIL, alpha=0.35, lw=0))
ax.add_patch(Circle((0, 0), 1/phi, color=UP, alpha=0.45, lw=0))
for r, c in ((1/phi, UP), (phi, DOWN)): ax.add_patch(Circle((0, 0), r, fill=False, ec=c, lw=2.5))
ax.plot([1/phi, -phi], [0, 0], 'o', color=GOLD, ms=9, zorder=5)
ax.text(0, 0.02, 'upward tree', color='#2A1438', fontsize=12, ha='center', va='center', fontweight='bold')
ax.text(0, -0.22, '|x| < 1/φ', color='#2A1438', fontsize=11, ha='center', va='center')
ax.text(0, 1.0, 'the veil', color='#3A1A0E', fontsize=13, ha='center', va='center', fontweight='bold')
ax.text(0, 0.8, '1/φ ≤ |x| ≤ φ', color='#3A1A0E', fontsize=11, ha='center', va='center')
ax.text(0, 1.95, 'downward tree,  |x| > φ', color=INK, fontsize=12.5, ha='center', va='center', fontweight='bold')
ax.text(1/phi + 0.08, -0.17, '1/φ', color=GOLD, fontsize=11)
ax.text(-phi - 0.05, -0.2, '−φ', color=GOLD, fontsize=11, ha='right')
eqs = [(UP, r'$\sum_{n\geq 1} F(n)\,x^n=\frac{x}{1-x-x^2}$', 'the upward tree converges inside 1/φ'),
       (DOWN, r'$\sum_{m\geq 0} F(-m)\,x^{-m}=-\frac{x}{1-x-x^2}$', 'the downward tree converges outside φ'),
       (VEIL, r'$U+D=0$', 'joined, the two trees cancel: only the poles at 1/φ and −φ remain'),
       (GOLD, r'$\Lambda(s)=\Lambda(1-s)$', 'the same mirror for ζ: only s = 0 and s = 1 stay infinite; the zeros live in the veil')]
for i, (c, eq, gloss) in enumerate(eqs):
    y = 0.36 - i*0.07
    fig.patches.append(Circle((0.07, y), 0.008, color=c, transform=fig.transFigure, figure=fig))
    fig.text(0.095, y + 0.008, eq, color=INK, fontsize=17, va='center')
    fig.text(0.095, y - 0.024, gloss, color=MUTED, fontsize=13, va='center')
fig.text(0.06, 0.072, 'The Qliphoth, the shells, are each tree alone: an infinity with no partner.\nJoined at the mirror, every infinity cancels but the two ends.', color=INK, fontsize=13.5, linespacing=1.4)
fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('downtree.png', facecolor=BG); print('ok')
