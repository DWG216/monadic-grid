"""t138: does the locked chord contain the attended tone? Same path as t137 (seeds, five movements). Pre-registration: PREDICTIONS_t138_t139.md."""
import numpy as np, sys
from t137_chord_resolution import age, measure
from t128_community import nsum
from t118_relations import triads
def run(seed, L=24, N=24, moves=5, r=2):
    rng = np.random.default_rng(seed); M = L*L
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    for g in range(moves):
        if g > 0: perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        a, p, phi = age(rng, 'third', L, a, p, phi); m = measure(L, a, p, phi)
    tr = triads(N); psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; R = np.abs(nsum(np.exp(1j*psi), L, r))/(2*r + 1)**2
    best = int((R > 0.8).sum(0).argmax()); kstar = int(np.bincount(p.argmax(1)).argmax())
    return dict(tone_frac=m['tone_frac'], relations=m['relations'], kstar=kstar, chord=tr[best].tolist(), in_chord=kstar in tr[best].tolist(), chord_monads=int((R[:, best] > 0.8).sum()))
if __name__ == '__main__':
    for s in range(int(sys.argv[1]), int(sys.argv[2])): print(s, run(s), flush=True)
