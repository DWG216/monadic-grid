"""t144 post hoc (labelled): the four-entry Z3 textures (cubic class + 351' class), one free size; scan it."""
import numpy as np, itertools
from scipy.optimize import least_squares
lep = np.array([2.88e-4, 0.0595, 1.0]); data = dict(s_mu=0.231, d_e=2.44, b_tau=0.678)
CL = {'cubic': -1.0, 'orth': 2/3}
cls = {0: [(0, 0), (1, 2)], 1: [(2, 2), (0, 1)], 2: [(1, 1), (0, 2)]}          # q = (0,1,2): entry class r = q_i + q_j mod 3
sv = lambda M: np.sort(np.linalg.svd(M, compute_uv=False))
best = []
for rc, ro in itertools.permutations(range(3), 2):
    if (2, 2) not in cls[ro]: continue                                         # 3-3 entry from the 351'
    ent = [(ij, 'cubic') for ij in cls[rc]] + [(ij, 'orth') for ij in cls[ro]]
    def build(x, cl=False):
        M = np.zeros((3, 3))
        for (ij, n), v in zip(ent, x):
            i, j = ij; c = CL[n] if cl else 1.0; M[i, j] = M[j, i] = c*v
        return M
    i33 = [k for k, (ij, n) in enumerate(ent) if ij == (2, 2)][0]
    rng = np.random.default_rng(1440)
    for t in np.concatenate([-np.logspace(-4, 0, 60), np.logspace(-4, 0, 60)]):
        free = [k for k in range(4) if k != i33][0]                          # scan the first non-3-3 entry
        def res(y):
            x = np.insert(y, [free, i33][::1] if False else 0, 0)            # placeholder, rebuilt below
            return 0
        others = [k for k in range(4) if k not in (i33, free)]
        def r2(y):
            x = np.zeros(4); x[i33] = 1.0; x[free] = t; x[others] = y
            s = sv(build(x)); return np.log(s/s[2] + 1e-30) - np.log(lep)
        for _ in range(8):
            r = least_squares(r2, rng.uniform(-1, 1, 2))
            if np.max(np.abs(r.fun[:2])) < 1e-6:
                x = np.zeros(4); x[i33] = 1.0; x[free] = t; x[others] = r.x
                sl, sd = sv(build(x)), sv(build(x, True))
                p = dict(s_mu=sd[1]/sl[1], d_e=sd[0]/sl[0], b_tau=sd[2]/sl[2])
                off = max(abs(p['s_mu']/data['s_mu'] - 1), abs(p['d_e']/data['d_e'] - 1), abs(p['b_tau']/data['b_tau'] - 1))
                best.append((off, (rc, ro), {f'{i+1}{j+1}': n for (i, j), n in ent}, {k: round(v, 3) for k, v in p.items()}))
best.sort(key=lambda z: z[0])
print('textures scanned:', len({b[1] for b in best}), '| lepton-consistent points:', len(best))
for b in best[:5]: print(round(b[0], 3), b[1], b[2], b[3])
