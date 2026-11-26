"""t140: chords on E6's 27 tones with a time-averaged record. Pre-registration: PREDICTIONS_t140.md.
Tones: hearing from averaged power (|z|^2 has no rotation). Chords: averaged complex amplitude B (rotates at the triple's
summed frequency, so only resonant chords survive averaging); hearing of a tone = mean averaged coherence over its chords."""
import numpy as np, sys, itertools
from t128_community import nsum
exec(open('t136_e6_resonance.py').read().split('out = {}')[0])
cubic = set()
for X in 'ABC':
    for perm in itertools.permutations(range(3)): cubic.add(frozenset(idx[(X, i, perm[i])] for i in range(3)))
for c_, l_, r_ in itertools.product(range(3), repeat=3): cubic.add(frozenset((idx[('A', c_, l_)], idx[('B', l_, r_)], idx[('C', r_, c_)])))
assert len(cubic) == 45
TR = np.array(list(itertools.combinations(range(27), 3))); NT = len(TR)
member = np.zeros((27, NT)); 
for col in range(3): member[TR[:, col], np.arange(NT)] = 1
member /= member.sum(1, keepdims=True)
def run(seed, L=12, moves=3, T=600, r=2, eta=0.3, will=0.2, tau=20.0):
    rng = np.random.default_rng(seed); M = L*L; N = 27; eps = 1/T; nb = (2*r + 1)**2; k = 1/tau
    v = rng.normal(size=9); om = W @ v; om = 0.3*om/np.abs(om).max()
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    for g in range(moves):
        if g > 0: perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        Pz = None; Bb = None; Ab = None; Rb = None
        for t in range(T):
            phi = phi + om + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
            z = nsum(c, L, r); den = nsum(p, L, r)
            Pz = np.abs(z)**2/den if Pz is None else (1 - k)*Pz + k*np.abs(z)**2/den
            phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
            psi = phi[:, TR].sum(2); at = np.sqrt(p[:, TR].prod(2))
            B = nsum(at*np.exp(1j*psi), L, r); A2 = nsum(at**2, L, r); U = nsum(np.exp(1j*psi), L, r)/nb
            Bb = B if Bb is None else (1 - k)*Bb + k*B; Ab = A2 if Ab is None else (1 - k)*Ab + k*A2; Rb = U if Rb is None else (1 - k)*Rb + k*U
            coh = np.abs(Bb)**2/np.maximum(Ab, 1e-30); cn = coh/np.maximum(coh.max(1, keepdims=True), 1e-30)
            gg = np.minimum(will*a[:, None]*at*N**1.5, 1.0)*cn*np.sin(np.angle(Bb) - psi)/3
            d = np.zeros_like(phi)
            for col in range(3): np.add.at(d.T, TR[:, col], gg.T)
            phi = phi + d
            w = np.maximum(Pz, coh @ member.T)
            e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
            p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    locked = np.where((np.abs(Rb) > 0.8).sum(0) >= 5)[0]
    kinds = []
    for i in locked:
        s = frozenset(TR[i].tolist()); blocks = {states[q][0] for q in s}
        kinds.append('det' if (s in cubic and len(blocks) == 1) else 'trace' if s in cubic else 'non-cubic')
    kstar = int(np.bincount(p.argmax(1), minlength=27).argmax())
    return dict(n_locked=len(locked), kinds=kinds, kstar=states[kstar], focus_frac=round(float((p.argmax(1) == kstar).mean()), 3),
                kstar_in_locked=bool(any(kstar in TR[i] for i in locked)), C_med=round(float(np.median((p**2).sum(1))), 3))
if __name__ == '__main__':
    for s in range(int(sys.argv[1]), int(sys.argv[2])): print(s, run(s), flush=True)
