"""Old maps slides: the Merkaba, the flower of life, the zodiac wheel, the chakras. Each: the full figure, equations on it, one tying sentence."""
import numpy as np, itertools, textwrap, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Wedge, Ellipse
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
BG, PANEL, INK, MUTED, LINE = '#1A1022', '#221530', '#F7EEFB', '#BFA9CC', '#3A2748'
THESIS, ANTI, SYN, FLASH = '#E3A8F5', '#8FB8FF', '#F5D08A', '#FFB38A'
OUT = 'drafts/old_maps/visuals/'

def frame(title, sub, notes):
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
    fig.text(0.06, 0.95, title, color=INK, fontsize=32, fontweight='bold')
    fig.text(0.06, 0.918, sub, color=MUTED, fontsize=16.5)
    y = 0.232
    for c, s in notes:
        w = textwrap.wrap(s, 100); h = 0.0185*len(w)
        fig.patches.append(Circle((0.07, y - h/2 + 0.009), 0.007, transform=fig.transFigure, fc=c, ec='none'))
        fig.text(0.095, y + 0.0095, '\n'.join(w), color=INK, fontsize=12.5, va='top', linespacing=1.3); y -= h + 0.013
    fig.add_artist(plt.Line2D([0.06, 0.94], [0.035, 0.035], color=LINE, lw=1.5, transform=fig.transFigure))
    fig.text(0.94, 0.012, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
    return fig

def label(ax, x, y, eq, gloss, c=INK, ha='center', fs=15, dy=0.3, **kw):
    ax.text(x, y, eq, color=c, fontsize=fs, ha=ha, va='bottom', **kw)
    ax.text(x, y - dy*0.25, gloss, color=MUTED, fontsize=11, ha=ha, va='top', **kw)

# 1. The Merkaba: the star tetrahedron
fig = frame('The Merkaba is the two hands', 'Two tetrahedra, one turning each way: the balanced pair and the swap that joins them',
            [(THESIS, 'The upward tetrahedron alone has 12 rotations (the tetrahedral group A₄); its double cover 2T (24) is the McKay partner of E6.'),
             (ANTI, 'Interlock its mirror and the rotations that swap the two hands join in: S₄ = A₄ + swap (24), the family symmetry of the grid (TM1 mixing; the strong CP angle zero).'),
             (SYN, 'Counter-rotating fields are the balanced pair: the two turnings sum to 2 cos ωt, real, a sum that writes one tick and leaves nothing over.'),
             (FLASH, 'What the vehicle of light pictures is what the equation says: one form held by two opposite turnings.')])
ax = fig.add_axes([0.04, 0.30, 0.92, 0.58], projection='3d'); ax.set_facecolor(BG); ax.axis('off')
V = np.array(list(itertools.product([-1, 1], repeat=3)), float)
up = V[np.prod(V, 1) > 0]; dn = V[np.prod(V, 1) < 0]
for T, c in ((up, THESIS), (dn, ANTI)):
    faces = [T[list(f)] for f in itertools.combinations(range(4), 3)]
    ax.add_collection3d(Poly3DCollection(faces, facecolor=c, alpha=0.22, edgecolor=c, linewidth=2.2))
for a, b in itertools.combinations(range(8), 2):
    if np.sum(V[a] != V[b]) == 1: ax.plot(*zip(V[a], V[b]), color=LINE, lw=0.8, alpha=0.6)
ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=18, azim=28); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_zlim(-1.3, 1.3)
ax2 = fig.add_axes([0, 0, 1, 1]); ax2.axis('off'); ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
label(ax2, 0.22, 0.85, r'$A_4\ (12)\ \subset\ 2T\ (24)\ \to\ \hat E_6$', 'one hand; McKay', c=THESIS, dy=0.02)
label(ax2, 0.8, 0.85, r'$S_4 = A_4 + \mathrm{swap}$', 'both hands: family', c=ANTI, dy=0.02)
label(ax2, 0.5, 0.315, r'$e^{+i\omega t}+e^{-i\omega t}=2\cos\omega t$', 'counter-rotation: the balanced pair', c=SYN, dy=0.02)
fig.savefig(OUT + 'merkaba.png', facecolor=BG); plt.close(fig)

# 2. The flower of life: SU(3)'s hexagon and lattice
fig = frame('The flower of life is SU(3)', 'Its centres are the A₂ lattice; the seed is the hexagon of the strong force',
            [(SYN, 'The seed of life: one circle and six around it. The six centres are the six roots of SU(3); with the two at the centre (its Cartan pair) they make the 8 gluons.'),
             (THESIS, 'The upward triangle of centres is the quark triplet 3, the downward one the antiquarks 3̄: the hexagram is the 3 and 3̄ laid together.'),
             (ANTI, 'Every circle meets its neighbours at 60°: α·α = 2, α·β = −1, the Cartan matrix of A₂. The flower is the lattice those angles generate.'),
             (FLASH, 'What the flower draws is what the equation says: colour charge lives on a hexagonal lattice.')])
ax = fig.add_axes([0.08, 0.29, 0.84, 0.61]); ax.set_facecolor(BG); ax.axis('off'); ax.set_aspect('equal')
a1, a2 = np.array([1, 0]), np.array([0.5, np.sqrt(3)/2]); C = []
for i, j in itertools.product(range(-3, 4), repeat=2):
    p = i*a1 + j*a2
    if np.linalg.norm(p) < 2.05: C.append(p)
for p in C: ax.add_patch(Circle(p, 1, fill=False, ec='#6E5A86', lw=1.1, alpha=0.8))
ax.add_patch(Circle((0, 0), 3.0, fill=False, ec=MUTED, lw=1.8))
roots = [np.array([np.cos(k*np.pi/3), np.sin(k*np.pi/3)]) for k in range(6)]
for r in roots: ax.add_patch(Circle(r, 1, fill=False, ec=SYN, lw=2.2)); ax.plot(*r, 'o', color=SYN, ms=8, zorder=5)
ax.add_patch(Circle((0, 0), 1, fill=False, ec=SYN, lw=2.2)); ax.plot(0, 0, 'o', color=SYN, ms=11, zorder=5); ax.plot(0, 0, 'o', color=BG, ms=5, zorder=6)
w3 = [np.array([np.cos(np.pi/2 + k*2*np.pi/3), np.sin(np.pi/2 + k*2*np.pi/3)])/np.sqrt(3) for k in range(3)]
ax.add_patch(Polygon(w3, closed=True, fill=False, ec=THESIS, lw=2.6)); ax.add_patch(Polygon([-w for w in w3], closed=True, fill=False, ec=ANTI, lw=2.6))
for w in w3: ax.plot(*w, 'o', color=THESIS, ms=7, zorder=6); ax.plot(*(-w), 'o', color=ANTI, ms=7, zorder=6)
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.4, 3.6)
label(ax, 0, 3.35, r'$\mathbf{8} = 6\ \mathrm{roots} + 2\ \mathrm{Cartan}$', 'the seed: gluons', c=SYN)
label(ax, -2.25, 2.55, r'$\mathbf{3}\ \oplus\ \bar{\mathbf{3}}$', 'the hexagram', c=THESIS)
label(ax, 2.2, 2.55, r'$\alpha\cdot\alpha=2,\ \ \alpha\cdot\beta=-1$', 'the 60° meeting', c=ANTI)
label(ax, 0, -3.25, r'$\Lambda_{A_2}=\{\,m\alpha_1+n\alpha_2\,\}$', 'the flower: the lattice', c=MUTED)
fig.savefig(OUT + 'flower_of_life.png', facecolor=BG); plt.close(fig)

# 3. The zodiac wheel and the chords the sky holds
fig = frame('The zodiac and the chords in the sky', 'Twelve signs around the ecliptic; inside, three moons locked in a three-voice chord',
            [(SYN, 'As a claim that birth positions shape a person, astrology does not pass. What the sky does hold is phase relations: chords.'),
             (THESIS, 'Io, Europa and Ganymede orbit in 1 : 2 : 4, and the Laplace angle λ(Io) − 3λ(Europa) + 2λ(Ganymede) stays at 180°: no two moons fix it, all three hold it.'),
             (ANTI, 'That is the shape of a third-order law (t118): a relation among three phases, each alone free, seen only by a reader that hears in threes.'),
             (FLASH, 'The wheel turns once in about 25,800 years as the equinox precesses: the Great Year, the sky\'s slowest held tone.')])
ax = fig.add_axes([0.06, 0.29, 0.88, 0.61]); ax.set_facecolor(BG); ax.axis('off'); ax.set_aspect('equal')
signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
elem = [FLASH, SYN, ANTI, THESIS]*3
for k, s in enumerate(signs):
    a0 = 90 + 30*k
    ax.add_patch(Wedge((0, 0), 3.0, a0, a0 + 30, width=0.62, fc=elem[k], alpha=0.16, ec=LINE, lw=1.2))
    am = np.radians(a0 + 15); ax.text(2.69*np.cos(am), 2.69*np.sin(am), s, color=INK, fontsize=10.5, ha='center', va='center', rotation=((a0 + 15 - 90) if (a0 + 15) % 360 <= 180 else (a0 + 15 + 90)) % 360)
ax.add_patch(Circle((0, 0), 2.38, fill=False, ec=MUTED, lw=1.2))
ax.add_patch(Circle((0, 0), 0.28, fc=SYN, ec='none'))
lam = {'Io': (0.85, np.radians(20)), 'Europa': (0.85*2**(2/3), np.radians(20 + 180/1.0 - 0)), 'Ganymede': (0.85*4**(2/3), 0)}
lI = np.radians(30); lE = np.radians(130); lG = (np.pi + lI*0 - lI + 3*lE)/2                       # lambda_I - 3 lambda_E + 2 lambda_G = pi
for (n, r, l, c) in (('Io', 0.75, lI, FLASH), ('Europa', 0.75*2**(2/3), lE, THESIS), ('Ganymede', 0.75*4**(2/3), lG, ANTI)):
    ax.add_patch(Circle((0, 0), r, fill=False, ec=c, lw=1.6, ls=(0, (4, 3))))
    ax.plot(r*np.cos(l), r*np.sin(l), 'o', color=c, ms=11, zorder=5); ax.text(r*np.cos(l) + 0.12, r*np.sin(l) + 0.14, n, color=c, fontsize=12, zorder=6)
assert abs(((lI - 3*lE + 2*lG) - np.pi + np.pi) % (2*np.pi) - np.pi) < 1e-9
ax.set_xlim(-3.25, 3.25); ax.set_ylim(-3.9, 3.3)
label(ax, 0, -3.35, r'$\lambda_I-3\lambda_E+2\lambda_G=180^\circ,\qquad n_I:n_E:n_G = 4:2:1$', 'the Laplace chord: three voices, one held relation', c=SYN)
fig.savefig(OUT + 'zodiac_chords.png', facecolor=BG); plt.close(fig)

# 4. The chakras: a body that rings in nested bands
fig = frame('The chakras are the body\'s bands', 'Seven centres up the column; the body rings at nested frequencies, slow below, fast above',
            [(SYN, 'As wheels in the anatomy the chakras do not pass; as a ladder they do: the body rings in nested bands, gut, heart, breath, voice, brain.'),
             (THESIS, 'Higher up the column is higher-order hearing: pairs of phases (the power rule p·w^β), then chords of three (t118), each order blind to the one above.'),
             (ANTI, 'The bands lock to one another, breath to heart, heart to brain: entrainment is many rhythms keeping one count.'),
             (FLASH, 'What the column pictures is what the equations say: one body, one record, read at more orders as a mind develops.')])
ax = fig.add_axes([0.04, 0.29, 0.92, 0.61]); ax.set_facecolor(BG); ax.axis('off'); ax.set_aspect('equal')
ax.add_patch(Ellipse((0, 5.2), 1.15, 1.4, fc=PANEL, ec=LINE, lw=1.5))
ax.add_patch(Polygon([(-0.25, 4.5), (0.25, 4.5), (0.3, 4.2), (1.4, 3.9), (1.5, 2.2), (1.05, 2.0), (1.05, 0.9), (0.95, 0.2), (-0.95, 0.2), (-1.05, 0.9), (-1.05, 2.0), (-1.5, 2.2), (-1.4, 3.9), (-0.3, 4.2)], closed=True, fc=PANEL, ec=LINE, lw=1.5))
ax.plot([0, 0], [0.35, 5.75], color=LINE, lw=2)
chak = [('Root', 0.45, '#E05252', r'$0.05\ \mathrm{Hz}$', 'gut slow wave, 3 per min'),
        ('Sacral', 1.15, '#F08A3C', r'$0.1\ \mathrm{Hz}$', 'blood-pressure wave'),
        ('Solar plexus', 1.9, '#F2C94C', r'$0.25\ \mathrm{Hz}$', 'breath'),
        ('Heart', 2.85, '#5CC98A', r'$1.2\ \mathrm{Hz}$', 'heartbeat'),
        ('Throat', 4.15, '#4FB3E8', r'$100$–$250\ \mathrm{Hz}$', 'voice'),
        ('Third eye', 5.25, '#6C7BE0', r'$10\ \mathrm{Hz}$', 'alpha: the whole cortex'),
        ('Crown', 5.95, '#B07CE8', r'$40\ \mathrm{Hz}$', 'gamma: binding')]
for i, (n, y, c, eq, g) in enumerate(chak):
    ax.add_patch(Circle((0, y), 0.2, fc=c, ec=INK, lw=1, zorder=5))
    ax.text(-0.38, y, n, color=c, fontsize=12.5, ha='right', va='center', fontweight='bold')
    ax.text(0.38, y + 0.08, eq, color=INK, fontsize=13, ha='left', va='center'); ax.text(0.38, y - 0.17, g, color=MUTED, fontsize=10.5, ha='left', va='center')
ax.annotate('', xy=(3.3, 6.0), xytext=(3.3, 0.4), arrowprops=dict(arrowstyle='-|>', color=FLASH, lw=2))
for y, eq, g in ((1.0, r'$p\,w^{\beta}$', 'second order: tones'), (3.2, r'$\varphi_1+\varphi_2-\varphi_3=\theta$', 'third order: chords'), (5.4, r'$d\ln a = d\ln e$', 'capacity: the climb')):
    ax.text(3.45, y + 0.1, eq, color=FLASH, fontsize=14, ha='left', va='center'); ax.text(3.45, y - 0.2, g, color=MUTED, fontsize=10.5, ha='left', va='center')
ax.set_xlim(-3.0, 6.2); ax.set_ylim(-0.1, 6.5)
fig.savefig(OUT + 'chakras_bands.png', facecolor=BG); plt.close(fig)
print('ok')
