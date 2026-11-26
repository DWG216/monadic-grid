"""Prototype visual for The old maps, post 6: the enneagram on the clock of nine (Orchid dawn palette, proposed)."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG, PANEL, INK, MUTED, ACC, GOLD, LINE = '#1A1022', '#241631', '#F7EEFB', '#BFA9CC', '#E3A8F5', '#F5D08A', '#3A2748'
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.08, 0.22, 0.84, 0.6]); ax.set_facecolor(BG); ax.set_aspect('equal'); ax.axis('off')
pos = {k: (np.sin(2*np.pi*(k % 9)/9), np.cos(2*np.pi*(k % 9)/9)) for k in range(1, 10)}
t = np.linspace(0, 2*np.pi, 400); ax.plot(np.cos(t), np.sin(t), color=LINE, lw=2.5)
def path(seq, col, lw, ls='-'):
    for a, b in zip(seq, seq[1:] + seq[:1]):
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=col, lw=lw, ls=ls, solid_capstyle='round')
path([1, 4, 2, 8, 5, 7], ACC, 4)
path([3, 6, 9], GOLD, 4)
for k, (x, y) in pos.items():
    ax.add_patch(plt.Circle((x, y), 0.085, color=BG, zorder=3)); ax.add_patch(plt.Circle((x, y), 0.085, fill=False, color=GOLD if k % 3 == 0 else ACC, lw=2.5, zorder=4))
    ax.text(x, y, str(k), ha='center', va='center', color=INK, fontsize=24, fontweight='bold', zorder=5)
ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.2, 1.25)
fig.text(0.07, 0.93, 'The enneagram is a clock of nine', color=INK, fontsize=34, fontweight='bold')
fig.text(0.07, 0.895, 'An old figure, drawn by arithmetic', color=MUTED, fontsize=20)
lines = [(ACC, '1/7 = 0.142857…  draws the inner figure: 1 → 4 → 2 → 8 → 5 → 7'),
         (ACC, 'Its six points are the numbers the clock of nine can invert; doubling visits all six'),
         (GOLD, '3, 6, 9: the multiples of three, which the clock cannot invert')]
for i, (c, s) in enumerate(lines):
    y = 0.175 - i*0.04; fig.patches.append(plt.Circle((0.085, y + 0.007), 0.008, color=c, transform=fig.transFigure, figure=fig))
    fig.text(0.11, y, s, color=INK, fontsize=17.5)
fig.text(0.07, 0.055, 'The grid counts on this clock: the lepton phase 2/9 is two hands over its nine points.', color=MUTED, fontsize=15)
fig.add_artist(plt.Line2D([0.07, 0.93], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.93, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('enneagram_prototype.png', facecolor=BG); print('ok')
