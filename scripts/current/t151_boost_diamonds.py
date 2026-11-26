"""t151: does the grain pick a frame? Counts and longest chains in boosted causal diamonds. Pre-registration: PREDICTIONS_t151.md."""
import numpy as np
from bisect import bisect_right
rng = np.random.default_rng(1510)
V, TRIALS, ETAS = 50.0, 3000, range(6)

def points(kind, u0, v0, du, dv):
    """Grain points inside [u0, u0 + du) x [v0, v0 + dv); density 1 per unit u-v area."""
    if kind == 'poisson':
        n = rng.poisson(du*dv)
        return np.column_stack([u0 + du*rng.random(n), v0 + dv*rng.random(n)])
    iu = np.arange(np.floor(u0) - 1, np.ceil(u0 + du) + 1); iv = np.arange(np.floor(v0) - 1, np.ceil(v0 + dv) + 1)
    U, Vv = np.meshgrid(iu, iv, indexing='ij'); P = np.column_stack([U.ravel(), Vv.ravel()]).astype(float)
    if kind == 'jitter':
        # jitter fixed per lattice site: seeded by the site, so the same grain is seen by every diamond
        h = (P[:, 0]*73856093 + P[:, 1]*19349663) % 2**31
        P = P + np.column_stack([np.sin(h)*43758.5453 % 1, np.sin(h + 1.7)*24634.6345 % 1])
    m = (P[:, 0] >= u0) & (P[:, 0] < u0 + du) & (P[:, 1] >= v0) & (P[:, 1] < v0 + dv)
    return P[m]

def longest_chain(P):
    """Longest causal chain (u and v both non-decreasing) = longest non-decreasing subsequence of v sorted by u."""
    if len(P) == 0: return 0
    P = P[np.lexsort((P[:, 1], P[:, 0]))]; tails = []
    for v in P[:, 1]:
        i = bisect_right(tails, v)
        if i == len(tails): tails.append(v)
        else: tails[i] = v
    return len(tails)

res = {}
for kind in ('lattice', 'jitter', 'poisson'):
    for eta in ETAS:
        du, dv = np.sqrt(V)*np.exp(eta), np.sqrt(V)*np.exp(-eta)
        cnt, ch = [], []
        for _ in range(TRIALS):
            u0, v0 = rng.uniform(0, 1000), rng.uniform(0, 1000)
            P = points(kind, u0, v0, du, dv); cnt.append(len(P)); ch.append(longest_chain(P))
        res[kind, eta] = (np.mean(cnt), np.var(cnt), np.mean(ch))
        print(f'{kind:8s} eta={eta}  mean={res[kind, eta][0]:7.2f}  var={res[kind, eta][1]:9.2f}  chain={res[kind, eta][2]:7.2f}')
out = {}
out['S1'] = dict(pass_=all(abs(res[k][0]/V - 1) < 0.03 for k in res), worst=max(abs(res[k][0]/V - 1) for k in res))
out['P1'] = dict(var0=res['lattice', 0][1], var5=res['lattice', 5][1], pass_=res['lattice', 5][1] > 10*res['lattice', 0][1])
jm0, jv0, jm5, jv5 = res['jitter', 0][0], res['jitter', 0][1], res['jitter', 5][0], res['jitter', 5][1]
out['P2'] = dict(var0_over_mean=jv0/jm0, var5_over_mean=jv5/jm5, pass_=jv0 < 0.5*jm0 and abs(jv5/jm5 - 1) < 0.2 and jv5/jv0 > 2)
pc0 = res['poisson', 0][2]
out['P3'] = dict(var_over_mean={e: res['poisson', e][1]/res['poisson', e][0] for e in ETAS}, chain={e: res['poisson', e][2] for e in ETAS},
                 pass_=all(abs(res['poisson', e][1]/res['poisson', e][0] - 1) < 0.1 and abs(res['poisson', e][2]/pc0 - 1) < 0.05 for e in ETAS))
out['P4'] = dict(lattice=(res['lattice', 0][2], res['lattice', 5][2]), jitter=(res['jitter', 0][2], res['jitter', 5][2]),
                 pass_=all(abs(res[k, 5][2]/res[k, 0][2] - 1) > 0.2 for k in ('lattice', 'jitter')))
for k, v in out.items(): print(k, v)
