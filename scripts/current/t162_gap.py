"""t162: a monad analogue of the Yang-Mills mass gap. Pre-registration: PREDICTIONS_t162.md."""
import numpy as np, itertools
exec(open('t136_e6_resonance.py').read().split('out = {}')[0])            # W (27 x 9, entries in thirds)
W3 = np.rint(3*W).astype(int)
rng = np.random.default_rng(1620)

def chord_sums(n):
    """All multisets of n of the 27 tones: integer weight sums (3W) as rows; returns unique sums with multiplicity ignored."""
    S = set()
    for c in itertools.combinations_with_replacement(range(27), n):
        S.add(tuple(W3[list(c)].sum(0)))
    return np.array(sorted(S))

sums = {n: chord_sums(n) for n in range(2, 7)}
zero = {n: int(np.sum(np.all(sums[n] == 0, axis=1))) for n in sums}
n3_inv = sum(1 for c in itertools.combinations_with_replacement(range(27), 3) if not W3[list(c)].sum(0).any())
out = {'S1': dict(invariant_3_chords=n3_inv, pass_=n3_inv == 45)}

gen, grain = [], []
for _ in range(10):
    v = rng.normal(size=9); om = W @ v; scale = np.abs(om).max()
    gen.append({n: float(np.min(np.abs((sums[n] @ v)/3/scale)[np.any(sums[n] != 0, axis=1)])) for n in sums})
    vi = rng.integers(-3, 4, size=9)
    while not np.any(W3 @ vi): vi = rng.integers(-3, 4, size=9)
    vals = np.abs(sums[n] @ vi) if False else None
    grain.append({n: int(np.min(np.abs(sums[n] @ vi)[(np.any(sums[n] != 0, axis=1)) & ((sums[n] @ vi) != 0)])) if np.any((sums[n] @ vi) != 0) else None for n in sums})
falls = all(all(g[n] <= g[n - 1] + 1e-15 for n in range(3, 7)) for g in gen)
out['P1'] = dict(min_mismatch_by_n=[{n: round(g[n], 5) for n in g} for g in gen], pass_=falls and all(g[6] < 0.01 for g in gen))
out['P2'] = dict(min_nonzero_mismatch_by_n=grain, pass_=all(all(x is not None and x >= 1 for x in g.values()) for g in grain))

def laplacian_gap(L, r=2):
    k = 2*np.pi*np.arange(L)/L
    lam = np.zeros((L, L))
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx == 0 and dy == 0: continue
            lam += 1 - np.cos(k[:, None]*dx + k[None, :]*dy)
    return np.sort(lam.ravel())[1]
Ls = np.array([8, 12, 16, 24, 32, 48, 64]); gaps = np.array([laplacian_gap(L) for L in Ls])
expo = np.polyfit(np.log(Ls), np.log(gaps), 1)[0]
z3 = 24*(1 - np.cos(2*np.pi/3))
out['P3'] = dict(continuous_gaps=dict(zip(Ls.tolist(), np.round(gaps, 6).tolist())), exponent=expo, z3_single_flip=z3,
                 pass_=abs(expo + 2) < 0.1 and abs(z3 - 36) < 1e-12)
for k, v in out.items(): print(k, v)
