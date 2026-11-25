"""t120: the climb. t117's world (capacities log-uniform on [0.01, 1] setting listening 0.1 a_j and turning kappa a_j),
but capacity grows with experience: e_j = E_{p_j}[w] / mean_k(w) (what j's attention hears over a uniform listener),
a_j <- clip(a_j * e_j^gamma, 0.01, 1). Per monad: capacity over time, time to reach a = 0.5."""
import numpy as np, sys
def run(seed, gamma=0.02, kappa=0.2, M=120, N=64, T=800, eta=0.3, eps=1e-3, climb=True):
    rng = np.random.default_rng(seed); a = 10**rng.uniform(-2, 0, M); a0 = a.copy()
    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    t_half = np.full(M, np.inf); med = []
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); phi += np.minimum(kappa*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/p.sum(0)
        if climb: e = (p*w).sum(1)/w.mean(); a = np.clip(a*e**gamma, 0.01, 1.0)
        p = p*w**(0.1*a[:, None]); p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
        t_half[(a >= 0.5) & np.isinf(t_half)] = t; med.append(np.median(a))
    r = np.abs(np.exp(1j*phi).mean(0)); laws = r > 0.8; K = int(laws.sum())
    C = (p**2).sum(1); L = p[:, laws].sum(1) if K else np.zeros(M)
    fin = np.isfinite(t_half) & (a0 < 0.5); from scipy.stats import spearmanr
    rho = spearmanr(a0[fin], t_half[fin]).correlation if fin.sum() > 5 else np.nan
    return dict(K=K, a_med_end=float(np.median(a)), frac_half=float(fin.mean()), rho=float(rho), C_med=float(np.median(C)), L_med=float(np.median(L)),
                a_med_t=[round(float(med[i]), 3) for i in (0, 99, 199, 399, 599, 799)])
if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(10000, 10003) if m == 'sanity' else range(11000, 11010)
    for climb in (True, False):
        for s in seeds: print('climb' if climb else 'fixed', s, run(s, climb=climb))
    if m != 'sanity':
        for s in seeds: print('climb_nolaws', s, run(s, kappa=0.0))
