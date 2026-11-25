"""t116: laws that form themselves. No lawful set is given. Monads keep their phases between ticks; each tick
(1) noise: phi += eta * N(0, 1); (2) choice: each monad turns its phase at k toward the record's phase Phi_k = arg z_k,
z_k = sum_j sqrt(p_jk) e^{i phi_jk}, by min(kappa * N * p_jk, 1) * sin(Phi_k - phi_jk) (attention-weighted; uniform attention gives kappa);
(3) listening at rate beta: p <- p * w^beta, then a floor eps (a monad is never without perceptions, Monadology 21), w_k = |z_k|^2 / sum_j p_jk. Laws = frequencies whose phase order r_k = |mean_j e^{i phi_jk}| > 0.8."""
import numpy as np, sys
def run(seed, kappa, M=50, N=64, T=300, eta=0.3, weighted=True, dissent=0.0, beta=0.1, eps=1e-3):
    rng = np.random.default_rng(seed); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True)
    phi = rng.uniform(0, 2*np.pi, (M, N)); free = rng.random(M) < dissent
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); Phi = np.angle(z)
        gain = np.minimum(kappa*N*p, 1.0) if weighted else np.minimum(kappa*np.ones_like(p), 1.0)
        step = gain*np.sin(Phi - phi); step[free] = 0; phi += step
        w = np.abs(z)**2/p.sum(0); p = p*w**beta; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    r = np.abs(np.exp(1j*phi[~free]).mean(0)); laws = r > 0.8
    share = p[:, laws].sum(1).mean() if laws.any() else 0.0
    sh_free = float(p[free][:, laws].sum(1).mean()) if (laws.any() and free.any()) else 0.0
    return dict(K=int(laws.sum()), share=float(share), C=float((p**2).sum(1).mean()), r_max=float(r.max()), share_dissenters=sh_free)
def agg(rs): return {k: float(np.median([r[k] for r in rs])) for k in rs[0]}
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(3000, 3004) if mode == 'sanity' else range(4000, 4020)
    for kappa in (0.0, 0.02, 0.05, 0.1, 0.2, 0.4):
        print('kappa', kappa, 'weighted', {k: round(v, 3) for k, v in agg([run(s, kappa) for s in seeds]).items()},
              'uniform', {k: round(v, 3) for k, v in agg([run(s, kappa, weighted=False) for s in seeds]).items()})
    if mode != 'sanity':
        print('dissent 0.3, kappa 0.1', {k: round(v, 3) for k, v in agg([run(s, 0.1, dissent=0.3) for s in seeds]).items()})
