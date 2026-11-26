"""t145: which Z3 textures (one part per entry) can carry the light generations. Pre-registration: PREDICTIONS_t145.md."""
import numpy as np, itertools
from scipy.optimize import least_squares
lep = np.array([2.88e-4, 0.0595, 1.0]); data = np.array([0.231, 2.44, 0.678]); tol = np.array([0.10, 0.10, 0.05])
CL = {'c': -1.0, 'o': 2/3}
ENT = [(i, j) for i in range(3) for j in range(i, 3)]
sv = lambda M: np.sort(np.linalg.svd(M, compute_uv=False))
def mat(tex, x, clebsch=False):
    M = np.zeros((3, 3))
    for (ij, part), v in zip(tex, x):
        i, j = ij; M[i, j] = M[j, i] = v*(CL[part] if clebsch else 1.0)
    return M
textures = {}
for q in itertools.product(range(3), repeat=3):
    for hc, ho in itertools.product(range(3), repeat=2):
        tex, bad = [], False
        for (i, j) in ENT:
            r = (q[i] + q[j]) % 3; parts = [p for p, h in (('c', hc), ('o', ho)) if (r + h) % 3 == 0]
            if len(parts) > 1: bad = True; break
            if parts: tex.append(((i, j), parts[0]))
        if bad or ((2, 2), 'o') not in tex or len(tex) < 3: continue
        rng = np.random.default_rng(0)
        if min(sv(mat(tex, rng.uniform(0.5, 1.5, len(tex))))) < 1e-9: continue           # rank 3 for generic sizes
        canon = min(tuple(sorted(((tuple(sorted((perm[i], perm[j]))), p) for (i, j), p in tex))) for perm in [(0, 1, 2), (1, 0, 2)])
        textures.setdefault(canon, (q, hc, ho))
print('kept textures:', len(textures))
rng = np.random.default_rng(1450); passes = []
for canon, (q, hc, ho) in textures.items():
    tex = list(canon); k33 = tex.index(((2, 2), 'o')); others = [k for k in range(len(tex)) if k != k33]
    solve, draw = others[:2], others[2:]
    best = (np.inf, None); n_ok = 0
    for d in range(400 if draw else 1):
        x = np.zeros(len(tex)); x[k33] = 1.0
        x[draw] = rng.choice([-1, 1], len(draw))*10**rng.uniform(-4, 0, len(draw))
        for _ in range(4):
            def res(y):
                xx = x.copy(); xx[solve] = y; s = sv(mat(tex, xx)); return np.log(s/s[2] + 1e-30) - np.log(lep)
            r = least_squares(res, rng.choice([-1, 1], 2)*10**rng.uniform(-3, 0, 2))
            if np.max(np.abs(r.fun)) > 1e-6: continue
            xx = x.copy(); xx[solve] = r.x; n_ok += 1
            sl, sd = sv(mat(tex, xx)), sv(mat(tex, xx, True))
            pred = np.array([sd[1]/sl[1], sd[0]/sl[0], sd[2]/sl[2]])
            off = np.abs(pred/data - 1)
            if np.all(off <= tol): passes.append((canon, pred))
            score = np.max(off/tol)
            if score < best[0]: best = (score, pred)
    lab = ' '.join(f'{i+1}{j+1}{p}' for (i, j), p in canon)
    print(f'{lab:32s} q={q} hc={hc} ho={ho} | lepton-consistent {n_ok:5d} | best (s/mu, d/e, b/tau) =',
          None if best[1] is None else np.round(best[1], 3), '| worst/tol', round(best[0], 2))
print('points within tolerance:', len(passes)); print('P1 pass:', len(passes) > 0)
