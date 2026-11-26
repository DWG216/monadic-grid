"""t144: the light generations from the grain's Z3 (enumeration, registered). Pre-registration: PREDICTIONS_t143_t144.md."""
import numpy as np, itertools
from scipy.optimize import least_squares
lep_target = np.array([2.88e-4, 0.0595, 1.0]); data = dict(s_mu=0.231, d_e=2.44, b_tau=0.678)
CL = {'cubic': -1.0, 'orth': 2/3}
def sv(M): return np.sort(np.linalg.svd(M, compute_uv=False))
kept = []; rows = []
for q in set(itertools.permutations((0, 1, 2))):
    for hc, ho, ha in itertools.product(range(3), repeat=3):
        part = {}; ok = True
        for i in range(3):
            for j in range(i, 3):
                al = [n for n, h in (('cubic', hc), ('orth', ho)) if (q[i] + q[j] + h) % 3 == 0]
                anti = (i != j) and (q[i] + q[j] + ha) % 3 == 0
                if len(al) > 1 or (anti and not al): ok = False
                if al: part[(i, j)] = al[0]
        if not ok or part.get((2, 2)) != 'orth' or len(part) != 3: continue
        kept.append((q, hc, ho, ha, dict(part)))
print('kept assignments:', len(kept))
for q, hc, ho, ha, part in kept:
    ent = list(part.items())
    def build(x, clebsch=False):
        M = np.zeros((3, 3))
        for (ij, n), v in zip(ent, x):
            c = CL[n] if clebsch else 1.0; i, j = ij; M[i, j] = M[j, i] = c*v
        return M
    def res(x):
        s = sv(build(x)); return np.log(s/s[2] + 1e-30) - np.log(lep_target)
    sols = []
    rng = np.random.default_rng(144)
    for _ in range(200):
        x0 = rng.uniform(-1, 1, 3)*np.array([1, 1, 1]); x0[[k for k, (ij, n) in enumerate(ent) if ij == (2, 2)][0]] = 1.0
        r = least_squares(res, x0)
        if np.max(np.abs(r.fun)) < 1e-8:
            key = tuple(np.round(np.abs(r.x)/np.max(np.abs(r.x)), 5))
            if key not in [s[0] for s in sols]: sols.append((key, r.x))
    for key, x in sols:
        L, D = build(x), build(x, True); sl, sd = sv(L), sv(D)
        pred = dict(s_mu=sd[1]/sl[1], d_e=sd[0]/sl[0], b_tau=sd[2]/sl[2])
        u, s_, vt = np.linalg.svd(D); idx = np.argsort(s_); U = u[:, idx]; th12 = float(np.degrees(np.arctan2(abs(U[0, 1]), abs(U[1, 1]))))
        hit = abs(pred['s_mu']/data['s_mu'] - 1) < 0.1 and abs(pred['d_e']/data['d_e'] - 1) < 0.1 and abs(pred['b_tau']/data['b_tau'] - 1) < 0.05
        rows.append(hit)
        print(dict(q=q, h=(hc, ho, ha), entries={f'{i+1}{j+1}': n for (i, j), n in ent}, s_mu=round(pred['s_mu'], 3), d_e=round(pred['d_e'], 3), b_tau=round(pred['b_tau'], 3), theta12_deg=round(th12, 2), hit=hit))
print('P1 pass:', any(rows), '| solutions examined:', len(rows))
