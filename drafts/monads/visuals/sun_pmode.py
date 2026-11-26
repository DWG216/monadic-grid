"""Monads, post 17: a solar p-mode drawn in 3-D (spherical harmonic l = 5, m = 3 on the Sun's surface)."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.special import sph_harm_y
BG, INK, MUTED, LINE = '#160D10', '#FBEFE6', '#D8B9A6', '#3A2420'
l, m = 5, 3
th, ph = np.meshgrid(np.linspace(0, np.pi, 220), np.linspace(0, 2*np.pi, 440))
Y = np.real(sph_harm_y(l, m, th, ph)); Y /= np.abs(Y).max()
r = 1 + 0.08*Y
x, y, z = r*np.sin(th)*np.cos(ph), r*np.sin(th)*np.sin(ph), r*np.cos(th)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list('sun', ['#3B1F8F', '#C2410C', '#F59E0B', '#FDE68A'])
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.02, 0.2, 0.96, 0.66], projection='3d'); ax.set_facecolor(BG)
ax.plot_surface(x, y, z, facecolors=cmap((Y + 1)/2), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
ax.set_box_aspect((1, 1, 1)); ax.axis('off'); ax.view_init(elev=22, azim=35); lim = 0.78; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
fig.text(0.06, 0.95, 'The Sun rings as one body', color=INK, fontsize=32, fontweight='bold')
fig.text(0.06, 0.918, 'One of its millions of standing waves, drawn in three dimensions', color=MUTED, fontsize=16.5)
fig.text(0.5, 0.205, r'$\xi(\theta,\varphi,t)\ \propto\ Y_5^{3}(\theta,\varphi)\,e^{i\omega t},\quad \omega/2\pi\approx 3\ \mathrm{mHz}$', color=INK, fontsize=19, ha='center')
lines = [('A p-mode: sound trapped inside the Sun, l = 5, m = 3. Periods near five minutes.', INK),
         ('Every patch of the surface carries the whole interior: helioseismology images the far side from the near side.', INK),
         ('Its dynamo flips every 11 years and holds the new polarity: a held choice, on a star’s clock.', INK),
         ('In the grid: a body that rings as a whole and holds a break that a small step can tip can carry a mind.', MUTED)]
import textwrap
for i, (s, c) in enumerate(lines):
    fig.text(0.06, 0.17 - i*0.035, '\n'.join(textwrap.wrap(s, 100)), color=c, fontsize=13.5, va='center')
fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('drafts/monads/visuals/sun_pmode.png', facecolor=BG); print('ok')
