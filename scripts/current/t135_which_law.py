"""t135: which law the Community holds. Pre-registration: PREDICTIONS_t135.md. Dynamics: t134 age() (t128's run)."""
import numpy as np, sys
from t134_community_ages import age
from t128_community import nsum
def run(seed, f, a_maj, a_min, L=24, N=64, ages=3, k1=10, k2=40):
    rng = np.random.default_rng(seed); M = L*L
    maj = rng.random(M) < f
    a = np.where(maj, a_maj, a_min).astype(float)
    p = np.full((M, N), 0.5/(N - 1)); p[maj, k1] = 0.5; p[~maj, k2] = 0.5
    phi = rng.uniform(0, 2*np.pi, (M, N)); phi[maj, k1] = 0.3*rng.standard_normal(maj.sum()); phi[~maj, k2] = 1.7 + 0.3*rng.standard_normal((~maj).sum())
    for g in range(ages):
        perm = rng.permutation(M); a, p, phi = a[perm], p[perm], phi[perm]
        a, p, phi, K, comp = age(rng, L, a, p, phi)
    r = 2; order = np.abs(nsum(np.exp(1j*phi), L, r))/(2*r + 1)**2; top = p.argmax(1); held = order[np.arange(M), top] > 0.8
    ids, cnt = np.unique(top[held], return_counts=True); law = int(ids[cnt.argmax()]) if len(ids) else -1
    return dict(K=K, complete=round(comp, 3), law=('k1' if law == k1 else 'k2' if law == k2 else f'other{law}'), share_k2=round(float((top == k2).mean()), 3))
if __name__ == '__main__':
    name, f, amaj, amin = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    for s in range(35000, 35010): print(name, s, run(s, f, amaj, amin), flush=True)
