"""t141: the soloist. Pre-registration: PREDICTIONS_t141.md. Dynamics as t134/t135, with will per monad."""
import numpy as np, sys
from t128_community import nsum
def age(rng, L, a, p, phi, will, N=64, T=600, r=2, eta=0.3):
    M = L*L; eps = 1/T
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will[:, None]*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den; e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2
    top = p.argmax(1); held = order[np.arange(M), top] > 0.8; ids, cnt = np.unique(top[held], return_counts=True)
    C = (p**2).sum(1); comp = float(((a >= 0.5) & (C > 0.8) & held).mean()); K = int((cnt >= 5).sum())
    law = int(ids[cnt.argmax()]) if len(ids) else -1
    return a, p, phi, K, comp, law
def run(seed, ws, f=0.75, L=24, N=64, moves=3, k1=10, k2=40):
    rng = np.random.default_rng(seed); M = L*L; maj = rng.random(M) < f
    a = np.full(M, 0.5); will = np.where(maj, 0.2, ws)
    p = np.full((M, N), 0.5/(N - 1)); p[maj, k1] = 0.5; p[~maj, k2] = 0.5
    phi = rng.uniform(0, 2*np.pi, (M, N)); phi[maj, k1] = 0.3*rng.standard_normal(maj.sum()); phi[~maj, k2] = 1.7 + 0.3*rng.standard_normal((~maj).sum())
    for g in range(moves):
        perm = rng.permutation(M); a, p, phi, will = a[perm], p[perm], phi[perm], will[perm]
        a, p, phi, K, comp, law = age(rng, L, a, p, phi, will)
    return dict(K=K, complete=round(comp, 3), law='k1' if law == k1 else 'k2' if law == k2 else f'other{law}')
if __name__ == '__main__':
    name, ws = sys.argv[1], float(sys.argv[2])
    for s in range(41000, 41010): print(name, s, run(s, ws), flush=True)
