"""Monads chapter: the heart and the brain on the grid's measures (t147 values; post hoc rows labelled)."""
import numpy as np, matplotlib, textwrap; matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG, INK, MUTED, LINE, PANEL = '#160D10', '#FBEFE6', '#D8B9A6', '#3A2420', '#201317'
HEART, BRAIN = '#F0606A', '#B07CE8'
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
fig.text(0.06, 0.95, 'The heart holds the tone, the brain the chords', color=INK, fontsize=29, fontweight='bold')
fig.text(0.06, 0.918, 'Field strength mixes three things; the grid measures them apart', color=MUTED, fontsize=16.5)

# Heart: left ventricle as a truncated ellipsoidal shell, coloured by activation time, outward dipoles at the front
ax = fig.add_axes([0.0, 0.53, 0.5, 0.37], projection='3d'); ax.set_facecolor(BG); ax.axis('off')
th, ph = np.meshgrid(np.linspace(0, 0.64*np.pi, 120), np.linspace(0, 2*np.pi, 160))
X, Y, Z = 0.75*np.sin(th)*np.cos(ph), 0.75*np.sin(th)*np.sin(ph), -1.2*np.cos(th)
cmhh = matplotlib.colors.LinearSegmentedColormap.from_list('h', ['#F0606A', '#B91C1C', '#5B1016', '#2A0A0E'])
act = (th/(0.64*np.pi))*0.8 + 0.2*(1 + np.cos(ph - 0.6))/2
front = np.exp(-((act - 0.42)/0.05)**2); shade = 0.55 + 0.45*np.clip(np.cos(ph + 0.95), 0, 1)
colh = cmhh(act)*shade[..., None]; colh[..., :3] = np.clip(colh[..., :3]*(1 - front[..., None]) + np.array([1.0, 0.93, 0.6])*front[..., None], 0, 1); colh[..., 3] = 1

ax.plot_surface(X, Y, Z, facecolors=colh, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
for p0 in np.linspace(-2.2, 0.9, 6):
    t0 = 0.27*np.pi + 0.1*(1 + np.cos(p0 - 0.6)); x, y, z = 0.75*np.sin(t0)*np.cos(p0), 0.75*np.sin(t0)*np.sin(p0), -1.2*np.cos(t0)
    n = np.array([np.sin(t0)*np.cos(p0)/0.75, np.sin(t0)*np.sin(p0)/0.75, -np.cos(t0)/1.2]); n /= np.linalg.norm(n)
    ax.quiver(x, y, z, *(0.45*n), color=INK, lw=1.6, arrow_length_ratio=0.25)
ax.set_box_aspect((1, 1, 1.3)); ax.view_init(elev=22, azim=-35); ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-1.4, 0.4)
fig.text(0.25, 0.545, 'Heart: the wave crosses the wall in 90 ms', color=HEART, fontsize=13.5, ha='center', fontweight='bold')
fig.text(0.25, 0.525, 'arrows point every way: the vector sum cancels', color=MUTED, fontsize=11.5, ha='center')

# Brain: a folded cortical sheet in one alpha phase, dipoles normal to the sheet, opposite across each fold
ax = fig.add_axes([0.5, 0.53, 0.5, 0.37], projection='3d'); ax.set_facecolor(BG); ax.axis('off')
u, v = np.meshgrid(np.linspace(-np.pi, np.pi, 220), np.linspace(-1.2, 1.2, 60))
Zb = 0.55*np.sin(2*u)
dzdu = 1.1*np.cos(2*u); nz = 1/np.sqrt(1 + dzdu**2); phase = 2*(0.25 + 0.6*nz*(0.6 + 0.4*np.sign(-dzdu)*np.abs(dzdu)/1.1*0.5)) - 1
cmb = matplotlib.colors.LinearSegmentedColormap.from_list('b', ['#1E0B3D', '#5B21B6', '#8B5CF6', '#DDD6FE'])
ax.plot_surface(u, v, Zb, facecolors=cmb((phase + 1)/2), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
for uu in np.linspace(-np.pi + 0.35, np.pi - 0.35, 12):
    dz = 1.1*np.cos(2*uu); n = np.array([-dz, 0, 1]); n /= np.linalg.norm(n)
    ax.quiver(uu, -0.9, 0.55*np.sin(2*uu), *(0.75*n), color=INK, lw=1.6, arrow_length_ratio=0.22)
ax.set_box_aspect((2.2, 1, 0.9)); ax.view_init(elev=24, azim=-70); ax.set_zlim(-1.2, 1.4)
fig.text(0.75, 0.545, 'Cortex: the folded sheet at the alpha rhythm', color=BRAIN, fontsize=13.5, ha='center', fontweight='bold')
fig.text(0.75, 0.525, 'opposite walls of each fold cancel too', color=MUTED, fontsize=11.5, ha='center')

# Scoreboard
ax = fig.add_axes([0.06, 0.07, 0.88, 0.43]); ax.set_facecolor(BG); ax.axis('off'); ax.set_xlim(0, 1); ax.set_ylim(-0.1, 1)
ax.text(0.0, 0.97, 'Measure', color=MUTED, fontsize=12, va='center'); ax.text(0.48, 0.97, 'Heart', color=HEART, fontsize=13, va='center', fontweight='bold')
ax.text(0.76, 0.97, 'Brain (alpha)', color=BRAIN, fontsize=13, va='center', fontweight='bold')
rows = [('Field outside the body', 'what biophysics reports', '50–100 pT', 'about 1 pT', (100, 1)),
        ('One cell\'s source', 'current dipole', r'$4\times10^{-12}$ A m', r'$2\times10^{-14}$ A m', (4e-12, 1.7e-14)),
        ('Voices in the vector sum', 'Q / q  (t147)', r'$1.5\times10^{5}$', r'$6\times10^{6}$', (1.5e5, 6e6)),
        ('Voices in phase at its own rhythm', 'the record\'s measure (t147, t148)', r'$2.4\times10^{9}$ (0.98)', r'$1.2\times10^{7}$ (0.03)', (2.4e9, 1.2e7)),
        ('Order of chord held', 'how many voices one relation binds', '2: a tone and its overtones', '3 and up: rhythms locked across bands', None),
        ('Poise', 'can one small step tip the whole?', 'built not to tip', 'one neuron can shift behaviour', None)]
y = 0.87
for name, sub, h, b, vals in rows:
    ax.add_artist(plt.Line2D([0, 1], [y + 0.065, y + 0.065], color=LINE, lw=1))
    ax.text(0.0, y + 0.018, name, color=INK, fontsize=12.5, va='center'); ax.text(0.0, y - 0.025, sub, color=MUTED, fontsize=10, va='center')
    ax.text(0.48, y + 0.018, h, color=INK, fontsize=12, va='center'); ax.text(0.76, y + 0.018, '\n'.join(textwrap.wrap(b, 26)), color=INK, fontsize=12, va='center')
    if vals and vals[1] is not None:
        lo, hi = np.log10(min(vals)) - 0.5, np.log10(max(vals)) + 0.2
        for x0, val, c in ((0.48, vals[0], HEART), (0.76, vals[1], BRAIN)):
            w = 0.2*(np.log10(val) - lo)/(hi - lo); ax.add_patch(plt.Rectangle((x0, y - 0.04), w, 0.018, color=c, alpha=0.8))
    elif vals:
        ax.add_patch(plt.Rectangle((0.48, y - 0.04), 0.2, 0.018, color=HEART, alpha=0.8))
    y -= 0.14
ax.text(0.0, -0.1, '\n'.join(textwrap.wrap('Every heart cell fires once a beat, in phase: the body\'s held tone, the drone everything keeps time with. The brain sounds with fewer of its cells, but binds rhythms into chords and sits at the break: there the choices register.', 105)),
        color=MUTED, fontsize=12, va='bottom')
fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('drafts/monads/visuals/heart_brain.png', facecolor=BG); print('ok')
