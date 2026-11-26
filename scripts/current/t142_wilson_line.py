"""t142: E6 broken by an order-three holonomy. Pre-registration: PREDICTIONS_t142.md."""
import numpy as np, itertools, collections
u = np.eye(3) - 1/3; Z = np.zeros(3)
roots = []
for blk in range(3):
    for i, j in itertools.permutations(range(3), 2):
        v = np.zeros(9); v[3*blk:3*blk + 3] = np.eye(3)[i] - np.eye(3)[j]; roots.append(v)
for a, b, c in itertools.product(range(3), repeat=3):
    v = np.concatenate([u[a], u[b], u[c]]); roots.append(v); roots.append(-v)
R = np.array(roots); assert len(R) == 72
G = R @ R.T; norms = np.round(np.diag(G), 6); print('root lengths', set(norms))
t = np.random.default_rng(142).normal(size=9); pos = R[R @ t > 0]
simple = [a for a in pos if not any(np.allclose(a, b + c) for b in pos for c in pos)]
S = np.array(simple); print('simple roots', len(S))
cart = 2*(S @ S.T)/np.diag(S @ S.T)[:, None]; print('Cartan matrix det', round(np.linalg.det(cart)))
# coweights: dual to simple coroots alpha^vee = 2 alpha/|alpha|^2, within the 6-dim span
basis = S; coroots = 2*S/np.diag(S @ S.T)[:, None]
W = np.linalg.pinv(coroots)          # columns: vectors w_j with coroot_i . w_j = delta_ij in span
W = W.T                              # rows are coweights
assert np.allclose(coroots @ W.T, np.eye(6), atol=1e-9)
def unbroken(H):
    x = R @ H; keep = np.abs(x - np.round(x)) < 1e-9; Rk = R[keep]
    rank = np.linalg.matrix_rank(Rk, tol=1e-9) if len(Rk) else 0
    return int(keep.sum()), int(rank)
cnt = collections.Counter(); ss = []
for c in itertools.product(range(3), repeat=6):
    if not any(c): continue
    H = (np.array(c) @ W)/3; n, rk = unbroken(H); cnt[(n, rk)] += 1
    if rk == 6: ss.append(n)
print('unbroken (roots, semisimple rank): count', sorted(cnt.items()))
out = {}
out['P1'] = dict(rank6_root_counts=sorted(set(ss)), pass_=bool(ss) and set(ss) == {18})
out['P2'] = dict(n_SU3cubed=sum(1 for n in ss if n == 18), pass_=18 in ss)
H = np.concatenate([np.array([2, -1, -1])/3, Z, Z]); n, rk = unbroken(H)
wA = [np.concatenate([u[c], -u[l], Z]) for c in range(3) for l in range(3)]
wB = [np.concatenate([Z, u[l], -u[r]]) for l in range(3) for r in range(3)]
wC = [np.concatenate([-u[c], Z, u[r]]) for r in range(3) for c in range(3)]
ph = lambda ws: sorted({round(float((w @ H) % 1), 6) for w in ws})
phases = dict(A=ph(wA), B=ph(wB), C=ph(wC))
distinct = all(len(v) == 1 for v in phases.values()) and len({v[0] for v in phases.values()}) == 3
out['P3'] = dict(roots=n, rank=rk, phases=phases, pass_=(n == 18 and rk == 6 and distinct))
for k, v in out.items(): print(k, v)
