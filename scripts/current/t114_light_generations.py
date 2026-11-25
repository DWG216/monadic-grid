"""t114 (enumeration, not a pre-registered test: the writer computed the candidates analytically first).
Light generations in a two-zero texture M = [[0, a, 0], [a, c, 0], [0, 0, b]] with every entry drawn from the symmetric
halves of the pair's record: cubic half (down/lepton entry ratio -1), orthogonal 351' half (2/3), or both halves equally
((-1 + 2)/(1 + 3) = 1/4). Then m_s/m_mu = r22 and m_d/m_e = r12^2 / r22 (light-eigenvalue approximation, checked exactly)."""
import numpy as np, itertools
r = {'cubic': -1.0, 'orth': 2/3, 'both': 1/4}
data = {'s/mu': 0.231, 'd/e': 2.44}       # at M*, corrected running (t113 P3)
rows = []
for k22, k12 in itertools.product(r, r):
    c, a, b = 0.06, 0.008, 1.0
    Md = np.array([[0, r[k12]*a, 0], [r[k12]*a, r[k22]*c, 0], [0, 0, 2/3*b]]); Me = np.array([[0, a, 0], [a, c, 0], [0, 0, b]])
    sd, se = np.sort(np.linalg.svd(Md, compute_uv=False)), np.sort(np.linalg.svd(Me, compute_uv=False))
    sm, de = sd[1]/se[1], sd[0]/se[0]
    rows.append((k22, k12, sm, de, abs(sm/data['s/mu'] - 1), abs(de/data['d/e'] - 1)))
for row in sorted(rows, key=lambda x: x[4] + x[5]): print(f'2-2 {row[0]:5s} 1-2 {row[1]:5s}  s/mu {row[2]:.3f}  d/e {row[3]:.3f}  off {row[4]:.0%}, {row[5]:.0%}')
print('fits both within 10%:', [x[:2] for x in rows if x[4] < .1 and x[5] < .1])
