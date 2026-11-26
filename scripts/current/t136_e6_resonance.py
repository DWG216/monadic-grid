"""t136: resonant triples of E6's 27 = the cubic's monomials. Pre-registration: PREDICTIONS_t136_t137.md."""
import numpy as np, itertools
u = np.eye(3) - 1/3                                  # SU(3) fundamental weights (3 coords, sum-zero subspace)
Z = np.zeros(3); states = []; W = []
for c, l in itertools.product(range(3), repeat=2): states.append(('A', c, l)); W.append(np.concatenate([u[c], -u[l], Z]))    # (3, 3bar, 1)
for l, r in itertools.product(range(3), repeat=2): states.append(('B', l, r)); W.append(np.concatenate([Z, u[l], -u[r]]))    # (1, 3, 3bar)
for r, c in itertools.product(range(3), repeat=2): states.append(('C', r, c)); W.append(np.concatenate([-u[c], Z, u[r]]))    # (3bar, 1, 3)
W = np.array(W); idx = {s: i for i, s in enumerate(states)}; out = {}
d = np.linalg.norm(W[:, None] - W[None], axis=2) + np.eye(27)
out['S1'] = dict(distinct=bool(d.min() > 1e-9), nonzero=bool(np.linalg.norm(W, axis=1).min() > 1e-9))
# cubic monomials: det A, det B, det C (6 each), tr(ABC) (27)
cubic = set()
for X in 'ABC':
    for perm in itertools.permutations(range(3)):
        cubic.add(frozenset(idx[(X, i, perm[i])] for i in range(3)))
for c, l, r in itertools.product(range(3), repeat=3):
    cubic.add(frozenset((idx[('A', c, l)], idx[('B', l, r)], idx[('C', r, c)])))
zs = {frozenset(t) for t in itertools.combinations(range(27), 3) if np.abs(W[list(t)].sum(0)).max() < 1e-9}
rep = [(a, b) for a in range(27) for b in range(27) if a != b and np.abs(2*W[a] + W[b]).max() < 1e-9]
out['P1'] = dict(n_cubic=len(cubic), n_zero_sum=len(zs), equal=zs == cubic, repeated_state_triples=len(rep), pass_=(zs == cubic and len(cubic) == 45 and not rep))
rng = np.random.default_rng(136); same = 0
for _ in range(1000):
    v = rng.normal(size=9); om = W @ v
    res = {frozenset(t) for t in itertools.combinations(range(27), 3) if abs(om[list(t)].sum()) < 1e-9}
    same += res == cubic
out['P2'] = dict(draws_matching=same, pass_=same == 1000)
for k, v in out.items(): print(k, v)
