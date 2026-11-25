"""t73: clique on one slice, read against the reference. Pre-registration: PREDICTIONS_t73.md (written before this code)."""
import numpy as np, math
rng = np.random.default_rng(73)
T = 200
def sample(n, k, planted):
    iu = np.triu_indices(n, 1); m = iu[0].size; M = m // 2
    x = np.zeros(m, bool)
    if planted and k >= 2:
        S = rng.choice(n, k, replace=False); inS = np.zeros(n, bool); inS[S] = True
        cl = inS[iu[0]] & inS[iu[1]]
        x[cl] = True
        rest = np.flatnonzero(~cl); x[rng.choice(rest, M - cl.sum(), replace=False)] = True
    else:
        x[rng.choice(m, M, replace=False)] = True
    A = -np.ones((n, n)); A[iu] = np.where(x, 1.0, -1.0); A = np.triu(A, 1); A = A + A.T
    return A, x.sum()
def stats(A):
    deg = (A > 0).sum(1)
    return np.linalg.eigvalsh(A)[-1], deg.var()
def auc(y, z):
    y = np.asarray(y); z = np.asarray(z)
    return float(((y[:, None] > z[None, :]).mean() + 0.5 * (y[:, None] == z[None, :]).mean()))
out = {}
# S1, S2
ye, ne, yv, nv = [], [], [], []
for _ in range(50):
    A, e = sample(100, 50, True); ye.append(e); yv.append(stats(A)[0])
    A, e = sample(100, 50, False); ne.append(e); nv.append(stats(A)[0])
out['S1'] = dict(auc_edges=auc(ye, ne), pass_=auc(ye, ne) == 0.5)
out['S2'] = dict(auc_eig=auc(yv, nv), pass_=auc(yv, nv) == 1.0)
R = [0.5, 1, 1.5, 2, 3, 4]; N = [100, 200, 400, 800]
tab = {}
for n in N:
    T_n = T if n <= 400 else 100
    no = [stats(sample(n, 0, False)[0]) for _ in range(T_n)]
    for r in R:
        k = max(2, int(round(r * math.sqrt(n))))
        yes = [stats(sample(n, k, True)[0]) for _ in range(T_n)]
        tab[(n, r)] = (auc([a for a, _ in yes], [a for a, _ in no]), auc([b for _, b in yes], [b for _, b in no]), k)
    print('n', n, {r: (round(tab[(n, r)][0], 3), round(tab[(n, r)][1], 3), tab[(n, r)][2]) for r in R}, flush=True)
spread = {r: round(max(tab[(n, r)][0] for n in N) - min(tab[(n, r)][0] for n in N), 3) for r in R}
out['G1'] = dict(spread=spread, pass_=all(v < 0.1 for v in spread.values()))
out['G2'] = dict(low=[round(tab[(n, 0.5)][0], 3) for n in N], high=[round(tab[(n, 4)][0], 3) for n in N],
                 pass_=all(tab[(n, 0.5)][0] < 0.6 for n in N) and all(tab[(n, 4)][0] > 0.95 for n in N))
out['C1'] = dict(eig_auc=round(tab[(800, 2)][0], 3), degvar_auc=round(tab[(800, 2)][1], 3), pass_=tab[(800, 2)][1] < tab[(800, 2)][0])
for k_, v in out.items(): print(k_, v)
