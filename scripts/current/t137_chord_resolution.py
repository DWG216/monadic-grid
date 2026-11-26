"""t137: can minds that hear chords resolve to a chord? t129's dynamics with t134's movements. Pre-registration: PREDICTIONS_t136_t137.md."""
import numpy as np, sys
from t128_community import nsum
from t118_relations import triads
def age(rng, mode, L, a, p, phi, N=24, T=600, r=2, eta=0.3, will=0.2):
    M = L*L; eps = 1/T; tr = triads(N)
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den
        if mode == 'third':
            psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; at = np.sqrt(p[:, tr[:, 0]]*p[:, tr[:, 1]]*p[:, tr[:, 2]])
            B = nsum(at*np.exp(1j*psi), L, r); coh = np.abs(B)**2/np.maximum(nsum(at**2, L, r), 1e-30)
            g = np.minimum(will*a[:, None]*at*N**1.5, 1.0)*np.sin(np.angle(B) - psi)/3
            dd = np.zeros_like(phi); np.add.at(dd.T, tr[:, 0], g.T); np.add.at(dd.T, tr[:, 1], g.T); np.add.at(dd.T, tr[:, 2], -g.T); phi = phi + dd
            w3 = np.ones_like(w)
            for col in range(3): np.maximum.at(w3.T, tr[:, col], coh.T)
            w = np.maximum(w, w3)
        e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    return a, p, phi
def measure(L, a, p, phi, N=24, r=2):
    M = L*L; nb = (2*r + 1)**2; tr = triads(N); tset = {tuple(x) for x in tr.tolist()}
    psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; R = np.abs(nsum(np.exp(1j*psi), L, r))/nb
    order = np.abs(nsum(np.exp(1j*phi), L, r))/nb; C = (p**2).sum(1); top = p.argmax(1)
    tone = (a >= 0.5) & (C > 0.8) & (order[np.arange(M), top] > 0.8)
    t3 = np.argsort(-p, 1)[:, :3]; chord = np.zeros(M, bool); which = np.full(M, -1)
    for j in range(M):
        s = sorted(t3[j].tolist()); sh = p[j, s]
        for ti, (x, y, zz) in enumerate(tr.tolist()):
            if sorted((x, y, zz)) == s and R[j, ti] > 0.8 and sh.sum() > 0.9 and sh.min() >= 0.2 and a[j] >= 0.5:
                chord[j] = True; which[j] = ti; break
    tv, tc = np.unique(top[tone], return_counts=True); cv, cc = np.unique(which[chord], return_counts=True)
    return dict(chord_frac=float(chord.mean()), same_chord_frac=float(cc.max()/M) if len(cc) else 0.0, tone_frac=float(tone.mean()),
                same_tone_frac=float(tc.max()/M) if len(tc) else 0.0, C_med=float(np.median(C)), relations=int(((R > 0.8).sum(0) >= 5).sum()))
def run(seed, mode, L=24, N=24, moves=5):
    rng = np.random.default_rng(seed); M = L*L
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N)); rows = []
    for g in range(moves):
        if g > 0: perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        a, p, phi = age(rng, mode, L, a, p, phi); m = measure(L, a, p, phi)
        rows.append({k: round(v, 3) if isinstance(v, float) else v for k, v in m.items()})
    return rows
if __name__ == '__main__':
    mode, s0, s1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    for s in range(s0, s1): print(mode, s, run(s, mode), flush=True)
