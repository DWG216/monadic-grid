"""Monads chapter: bodies that ring as a whole, drawn in 3-D (egg, brain, Earth, black hole). Same frame as sun_pmode.py."""
import numpy as np, matplotlib, textwrap; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.special import sph_harm_y
BG, INK, MUTED, LINE = '#160D10', '#FBEFE6', '#D8B9A6', '#3A2420'
OUT = 'drafts/monads/visuals/'
th, ph = np.meshgrid(np.linspace(0, np.pi, 220), np.linspace(0, 2*np.pi, 440))

def frame(title, sub, eq, lines):
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.02, 0.2, 0.96, 0.66], projection='3d'); ax.set_facecolor(BG); ax.axis('off')
    fig.text(0.06, 0.95, title, color=INK, fontsize=32, fontweight='bold')
    fig.text(0.06, 0.918, sub, color=MUTED, fontsize=16.5)
    fig.text(0.5, 0.215, eq, color=INK, fontsize=19, ha='center')
    for i, s in enumerate(lines):
        fig.text(0.06, 0.18 - i*0.039, '\n'.join(textwrap.wrap(s, 100)), color=MUTED if i == len(lines) - 1 else INK, fontsize=13, va='center')
    fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
    fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
    return fig, ax

def sphere(ax, Y, amp, cmap, scale=(1, 1, 1), lim=0.78, elev=22, azim=35):
    r = 1 + amp*Y
    x, y, z = scale[0]*r*np.sin(th)*np.cos(ph), scale[1]*r*np.sin(th)*np.sin(ph), scale[2]*r*np.cos(th)
    ax.plot_surface(x, y, z, facecolors=cmap((Y + 1)/2), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=elev, azim=azim)
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)

cm = lambda cols: matplotlib.colors.LinearSegmentedColormap.from_list('c', cols)

# 1. The egg: a calcium wave crossing the cell from the sperm's entry point
gam = np.arccos(np.clip(np.sin(th)*np.cos(ph)*np.sin(1.1)*np.cos(0.6) + np.sin(th)*np.sin(ph)*np.sin(1.1)*np.sin(0.6) + np.cos(th)*np.cos(1.1), -1, 1))
Y = np.exp(-((gam - 1.3)/0.35)**2)*2 - 1 + 0.6*np.exp(-(gam/0.25)**2)
fig, ax = frame('The egg rings as one cell', 'A calcium wave crosses the fertilised egg from the point of entry',
                r'$c(\gamma,t)\ =\ c_0 + A\,e^{-(R\gamma - vt)^2/w^2},\quad v\approx 10\text{–}30\ \mu\mathrm{m/s}$',
                ['At fertilisation a wave of calcium sweeps the whole egg (about 80 μm across) in seconds, then repeats as a rhythm for hours.',
                 'The wave starts where the sperm entered and reaches every part of the cell: one event, carried by the whole body.',
                 'The egg then holds a break: which pole keeps the chromosomes, decided at a balanced point a small step can tip.',
                 'In the grid: a body that rings as a whole and holds a break that a small step can tip can carry a mind.'])
sphere(ax, np.clip(Y, -1, 1), 0.03, cm(['#1E3A5F', '#2DD4BF', '#A7F3D0', '#F0FDF4']), elev=55, azim=20)
fig.savefig(OUT + 'egg_calcium.png', facecolor=BG); plt.close(fig)

# 2. The brain: a global standing wave of the cortex at the alpha rhythm
Y = np.real(sph_harm_y(2, 1, th, ph)); Y /= np.abs(Y).max()
fig, ax = frame('The brain rings as one organ', 'A global standing wave of the cortex, drawn on its closed surface',
                r'$\phi(\theta,\varphi,t)\ \propto\ Y_3^{2}(\theta,\varphi)\,e^{i\omega t},\quad \omega/2\pi\approx 10\ \mathrm{Hz}$',
                ['The alpha rhythm (8–12 Hz) is coherent across the whole cortex: in Nunez\'s model it is a standing wave of one closed sheet.',
                 'Its frequency is set by the sheet\'s size and the speed of its fibres, as a bell\'s pitch is set by its shape.',
                 'Every percept rides on this whole-organ rhythm; a decision tips a poised network one way at a moment within it.',
                 'In the grid: a body that rings as a whole and holds a break that a small step can tip can carry a mind.'])
pal = cm(['#3B0764', '#9333EA', '#F0ABFC', '#FDF4FF'])
for side in (-1, 1):
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, 300), np.linspace(0, np.pi, 160))
    x0, y0, z0 = 1.15*np.cos(v), side*0.5 + 0.52*np.sin(v)*np.cos(u), np.where(np.sin(u) > 0, 0.85, 0.55)*np.sin(v)*np.sin(u)
    R = np.sqrt(x0**2 + y0**2 + z0**2); TH, PH = np.arccos(z0/R), np.arctan2(y0, x0)
    Yb = np.real(sph_harm_y(3, 2, TH, PH)); Yb /= 0.5
    g = np.sin(22*u + 3*np.sin(5*v))*np.sin(15*v + 2*np.sin(4*u))
    f = 1 + 0.025*Yb + 0.018*g
    ax.plot_surface(f*x0, side*0.5 + f*(y0 - side*0.5), f*z0, facecolors=pal(np.clip((np.clip(Yb, -1, 1) + 1)/2 - 0.08*g, 0, 1)), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=38, azim=-50); lim = 0.95; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
fig.savefig(OUT + 'brain_alpha.png', facecolor=BG); plt.close(fig)

# 3. The Earth: its slowest free oscillation, the football mode 0S2
Y = np.real(sph_harm_y(2, 0, th, ph)); Y /= np.abs(Y).max()
fig, ax = frame('The Earth rings as one planet', 'Its slowest free oscillation, 0S2, drawn in three dimensions',
                r'$\xi\ \propto\ Y_2^{0}(\theta)\,e^{i\omega t},\ \ T = 53.9\ \mathrm{min};\quad f_n = \frac{c}{2\pi a}\sqrt{n(n+1)}$',
                ['After great earthquakes the whole planet rings for weeks; 0S2 stretches it into a football and back every 54 minutes.',
                 'Its atmosphere rings too: lightning keeps the cavity between ground and ionosphere sounding at 7.8 Hz (Schumann; 10.6 Hz for a lossless cavity).',
                 'Its core dynamo has flipped hundreds of times and holds each polarity for ages: a held choice on a planet\'s clock.',
                 'In the grid: a body that rings as a whole and holds a break that a small step can tip can carry a mind.'])
sphere(ax, Y, 0.07, cm(['#0C4A6E', '#0EA5E9', '#86EFAC', '#FEF9C3']))
for t0 in (np.arccos(1/np.sqrt(3)), np.pi - np.arccos(1/np.sqrt(3))):
    pp = np.linspace(0, 2*np.pi, 400); rr0 = 1.004
    ax.plot(rr0*np.sin(t0)*np.cos(pp), rr0*np.sin(t0)*np.sin(pp), rr0*np.cos(t0)*np.ones_like(pp), color='#FBEFE6', lw=1.2, alpha=0.7)
fig.savefig(OUT + 'earth_0S2.png', facecolor=BG); plt.close(fig)

# 4. The black hole: the ringdown of its l = 2, m = 2 quasinormal mode, seen on the orbital plane
fig, ax = frame('A black hole rings, then is still', 'The ringdown of its fundamental mode, the wave it sends out, in three dimensions',
                r'$h\ \propto\ \frac{1}{r}\,\mathrm{Re}\,[\,{}_{-2}Y_{22}\,e^{-i\omega(t-r)}\,],\quad M\omega_{220} = 0.3737 - 0.0890\,i$',
                ['A hole formed in a merger rings once, at a pitch and decay set by its mass and spin alone: GW150914\'s rang near 250 Hz.',
                 'Nothing else can be read from it: the ringdown is the whole body speaking, with no part left over.',
                 'It holds no break: once still, it keeps what it has, the most complete record a body can be.',
                 'In the grid: a body that rings as a whole and keeps everything it has written; the corpus calls black holes souls.'])
rr, aa = np.meshgrid(np.linspace(0.0, 9, 320), np.linspace(0, 2*np.pi, 400))
w = 0.3737 - 0.0890j; tt = 14.0
H = np.real(np.exp(2j*aa)*np.exp(-1j*w*(tt - rr)))/np.sqrt(np.maximum(rr, 1.0))*(1 - np.exp(-((rr - 1.2).clip(0))**2/0.8)); H /= np.abs(H).max()
cols = cm(['#1E1B4B', '#6366F1', '#F59E0B', '#FFFBEB'])((H + 1)/2); cols[rr < 1.2] = (0, 0, 0, 1)
X, Yp = rr*np.cos(aa), rr*np.sin(aa)
ax.plot_surface(X, Yp, 1.1*H, facecolors=cols, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
ax.set_box_aspect((1, 1, 0.45)); ax.view_init(elev=32, azim=30); ax.set_xlim(-7, 7); ax.set_ylim(-7, 7); ax.set_zlim(-2, 2)
fig.savefig(OUT + 'blackhole_ringdown.png', facecolor=BG); plt.close(fig)
print('ok')
