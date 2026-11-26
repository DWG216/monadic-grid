"""Prototype: the grid's table of correspondences (The old maps). Dense, one row per structure; colour swatch per row."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
BG, PANEL, INK, MUTED, LINE, HEAD = '#1A1022', '#221530', '#F7EEFB', '#BFA9CC', '#3A2748', '#E3A8F5'
rows = [
 ('#F5D08A', 'Balanced zero',   'Silence',            '0',        'The circle',            'Ein Sof; the Tao',              r'$e^{i\pi}+1=0$'),
 ('#E3A8F5', 'The two hands',   'A standing tone',    '±ω',       'Yin-yang; hexagram',    'Shiva and Shakti; the Merkaba', r'$e^{+i\omega t}+e^{-i\omega t}$' + '\n' + r'$=2\cos\omega t$'),
 ('#F2C46D', 'The clock of five','The golden interval','φ = 1.618','Pentagram; icosahedron','Pythagoras; the golden spiral', 'E8 rings at φ (cobalt niobate)'),
 ('#9FD98A', 'The hexagon',     'Six around one',     '6 + 2',    'Seed of life',          'Flower of life',                'SU(3): the strong force'),
 ('#8FB8FF', 'The swap',        'Mirror pitch',       r'$S_4$' + ' = 24',  'Star tetrahedron',      'Star of David; Sri Yantra',     'Flavour; ' + r'$\bar{\theta}=0$'),
 ('#C9A2F0', 'The clock of nine','Nine-fold division','2/9',      'Enneagram circle',      'Digital roots; gematria',       'Lepton phase 2/9'),
 ('#F49AC1', 'All pairs meet',  'Every interval',     '231',      'A web joining 22 letters',    'Sefer Yetzirah’s gates',        'Cross terms: quantum mechanics'),
 ('#FFB38A', 'The meeting',     'Unison',             'ω = ω',    'Two circles as one',    'Love and attraction; the black hole','Non-beating terms: gravity'),
 ('#F7EEFB', 'The octave',      '2 : 1',              'k, k, 2k', 'Circle within circle',  'Pythagoras’ first ratio',       'A mind’s note and its overtone'),
 ('#5FD6C4', 'Three voices',    'A triad',            '45 terms', 'Three-coloured triangle','The three mothers; trinities',  'E6’s cubic: three fields'),
 ('#E06D53', 'The beat',        'One pulse',          'h/2',      'A single stroke',       'Power quanta (Nietzsche)',      'Will per Planck time'),
 ('#B49CFF', 'The ladder',      'Low to high octaves',r'$C=\Sigma p^2$',  'Red to violet',         'Chakras; the sefirot',          'Levels of mind (continuum)'),
 ('#F5D08A', 'The resolved chord','Final cadence',    '1',        'The full circle',       'Tikkun; Adam Kadmon; Omega',    'Every mind in tune (t134)'),
]
cols = [('', 0.055), ('Structure', 0.075), ('Sound', 0.235), ('Number', 0.37), ('Figure', 0.47), ('Old map', 0.625), ('Grid', 0.78)]
fig = plt.figure(figsize=(10.8, 13.5), dpi=100); fig.patch.set_facecolor(BG)
fig.text(0.055, 0.945, 'The table of correspondences', color=INK, fontsize=32, fontweight='bold')
fig.text(0.055, 0.912, 'Each idea as a sound, a number, a figure, an old map, and its place in the grid', color=MUTED, fontsize=16)
top, bot = 0.875, 0.075; h = (top - bot)/(len(rows) + 1)
fig.patches.append(FancyBboxPatch((0.04, bot - 0.005), 0.92, top - bot + 0.01, boxstyle='round,pad=0,rounding_size=0.012', fc=PANEL, ec=LINE, lw=1, transform=fig.transFigure, figure=fig))
for name, x in cols[1:]: fig.text(x, top - h*0.55, name, color=HEAD, fontsize=14, fontweight='bold', va='center')
for i, (c, *cells) in enumerate(rows):
    y = top - h*(i + 1.55)
    fig.add_artist(plt.Line2D([0.055, 0.945], [y + h*0.5, y + h*0.5], color=LINE, lw=0.8, transform=fig.transFigure))
    fig.patches.append(Circle((0.06, y), 0.009, color=c, transform=fig.transFigure, figure=fig))
    for j, txt in enumerate(cells):
        x = cols[j + 1][1]; w = (cols[j + 2][1] if j + 2 < len(cols) else 0.955) - x - 0.008
        size = 12.5 if j != 0 else 13.5
        import textwrap; nchar = max(8, int(w*1080/(size*(0.74 if j == 0 else 0.68))))
        lines = [txt] if ('$' in txt or '\n' in txt) else textwrap.wrap(txt, nchar)
        fig.text(x, y, '\n'.join(lines), color=INK if j in (0, 5) else MUTED if j != 4 else INK, fontsize=size, va='center', fontweight='bold' if j == 0 else 'normal', linespacing=1.15)
fig.add_artist(plt.Line2D([0.055, 0.945], [0.04, 0.04], color=LINE, lw=1.5, transform=fig.transFigure))
fig.text(0.945, 0.016, 'The Monadic Grid', color=MUTED, fontsize=14, ha='right')
fig.savefig('correspondences_prototype.png', facecolor=BG); print('ok')
