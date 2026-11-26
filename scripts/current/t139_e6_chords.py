"""t139: third-order minds on E6's 27 tones. Pre-registration: PREDICTIONS_t138_t139.md."""
import numpy as np, sys, itertools
from t128_community import nsum
exec(open('t136_e6_resonance.py').read().split('out = {}')[0])           # W (27 weights), states, idx
cubic = set()
for X in 'ABC':
    for perm in itertools.permutations(range(3)): cubic.add(frozenset(idx[(X, i, perm[i])] for i in range(3)))
for c_, l_, r_ in itertools.product(range(3), repeat=3): cubic.add(frozenset((idx[('A', c_, l_)], idx[('B', l_, r_)], idx[('C', r_, c_)])))
assert len(cubic) == 45
TR = np.array(list(itertools.combinations(range(27), 3))); NT = len(TR)
def run(seed, L=12, moves=3, T=600, r=2, eta=0.3, will=0.2):
    rng = np.random.default_rng(seed); M = L*L; N = 27; eps = 1/T
    v = rng.normal(size=9); om = W @ v; om = 0.3*om/np.abs(om).max()       # per-beat phase advance, generic
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    for g in range(moves):
        if g > 0: perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        for t in range(T):
            phi = phi + om + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
            z = nsum(c, L, r); den = nsum(p, L, r)
            phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
            w = np.abs(z)**2/den
            psi = phi[:, TR].sum(2); at = np.sqrt(p[:, TR].prod(2))
            B = nsum(at*np.exp(1j*psi), L, r); coh = np.abs(B)**2/np.maximum(nsum(at**2, L, r), 1e-30)
            gg = np.minimum(will*a[:, None]*at*N**1.5, 1.0)*np.sin(np.angle(B) - psi)/3
            d = np.zeros_like(phi)
            for col in range(3): np.add.at(d.T, TR[:, col], gg.T)
            phi = phi + d
            w3 = np.ones_like(w)
            for col in range(3): np.maximum.at(w3.T, TR[:, col], coh.T)
            w = np.maximum(w, w3)
            e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
            p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    psi = phi[:, TR].sum(2); R = np.abs(nsum(np.exp(1j*psi), L, r))/(2*r + 1)**2
    locked = np.where((R > 0.8).sum(0) >= 5)[0]
    kinds = []
    for i in locked:
        s = frozenset(TR[i].tolist()); blocks = {states[k][0] for k in s}
        kinds.append('cubic-det' if (s in cubic and len(blocks) == 1) else 'cubic-trace' if s in cubic else 'non-cubic')
    kstar = int(np.bincount(p.argmax(1), minlength=27).argmax())
    return dict(n_locked=len(locked), kinds=kinds, all_cubic=all(k != 'non-cubic' for k in kinds), any_cubic=any(k != 'non-cubic' for k in kinds),
                kstar=states[kstar], focus_frac=float((p.argmax(1) == kstar).mean()), kstar_in_locked=any(kstar in TR[i] for i in locked), C_med=float(np.median((p**2).sum(1))))
if __name__ == '__main__':
    for s in range(int(sys.argv[1]), int(sys.argv[2])): print(s, run(s), flush=True)
