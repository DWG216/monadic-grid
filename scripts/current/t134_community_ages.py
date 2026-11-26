"""t134: the Community of Gods across Ages with the whole monad carried. Pre-registration: PREDICTIONS_t134.md.
Dynamics exactly t128_community.py's run(); here the state (a, p, phi) can be passed in and returned."""
import numpy as np, sys
from t128_community import nsum
def age(rng, L, a, p, phi, N=64, T=600, r=2, eta=0.3, will=0.2):
    M = L*L; eps = 1/T
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den; e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2
    top = p.argmax(1); held = order[np.arange(M), top] > 0.8; ids, cnt = np.unique(top[held], return_counts=True)
    C = (p**2).sum(1); K = int((cnt >= 5).sum()); comp = float(((a >= 0.5) & (C > 0.8) & held).mean())
    return a, p, phi, K, comp
def run(seed, L, variant, ages=5, N=64):
    rng = np.random.default_rng(seed); M = L*L
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    rows = []
    for g in range(ages):
        if g > 0:
            if variant == 'A':
                p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
            elif variant == 'B':
                perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        a, p, phi, K, comp = age(rng, L, a, p, phi)
        rows.append((K, round(comp, 3)))
    return rows
if __name__ == '__main__':
    jobs = [('A', 24), ('B', 24), ('B', 12), ('C', 24)] if len(sys.argv) < 2 else [(sys.argv[1], int(sys.argv[2]))]
    for v, L in jobs:
        for s in range(34000, 34010):
            print(v, L, s, run(s, L, v), flush=True)
