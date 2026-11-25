"""t128: a Community of Gods? t126's derived dynamics (listening p w^a, a <= 1; growth a <- clip(a e, 1/T, 1); floor 1/T;
turning: direction = ascent of the record, strength = will kappa scaled by capacity x attention), but each monad hears the record of
its neighbourhood only: monads on an L x L periodic grid, neighbourhood = Chebyshev radius r (r = L//2 covers all: the global
control). Per monad j: z_jk = sum over neighbours of sqrt(p) e^{i phi}, w_jk = |z_jk|^2 / sum over neighbours of p.
A monad's law: its most attended frequency, if the local phase order there exceeds 0.8. Distinct laws: frequencies held as law by >= 5 monads."""
import numpy as np, sys
def nsum(X, L, r):
    G = X.reshape(L, L, -1); S = np.zeros_like(G)
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1): S = S + np.roll(np.roll(G, dx, 0), dy, 1)
    return S.reshape(L*L, -1)
def run(seed, L=12, N=64, T=600, r=2, eta=0.3, will=0.2, half=False, a_init=None, rng=None):
    rng = rng or np.random.default_rng(seed); M = L*L; eps = 1/T
    a = a_init.copy() if a_init is not None else 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    glob = (2*r + 1) >= L; mid = None
    def laws_now():
        c = np.exp(1j*phi); order = np.abs(c.sum(0))/M*np.ones((M, N)) if glob else np.abs(nsum(c, L, r))/(2*r + 1)**2
        top = p.argmax(1); held = order[np.arange(M), top] > 0.8; ids, cnt = np.unique(top[held], return_counts=True)
        return top, held, int((cnt >= 5).sum())
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        if glob: z = np.broadcast_to(c.sum(0), (M, N)); den = np.broadcast_to(p.sum(0), (M, N))
        else: z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den; e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
        if t == T//2 - 1: mid = laws_now()[2]
    top, held, K = laws_now(); C = (p**2).sum(1)
    return dict(a=a, K=K, K_mid=mid, frac_complete=float(((a >= 0.5) & (C > 0.8) & held).mean()), frac_held=float(held.mean()), C_med=float(np.median(C)), a_med=float(np.median(a)))
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(20000, 20003) if mode == 'sanity' else range(21000, 21010)
    fmt = lambda x: {k: round(v, 3) if isinstance(v, float) else v for k, v in x.items() if k != 'a'}
    for (L, r, name) in ((12, 2, 'A small L=12 r=2'), (24, 2, 'B large L=24 r=2'), (12, 6, 'global L=12')):
        for s in seeds: print(name, s, fmt(run(s, L=L, r=r)))
    if mode != 'sanity':
        for s in seeds:
            rng = np.random.default_rng(s); a = None; row = []
            for age in range(3):
                x = run(s, L=24, r=2, a_init=a, rng=rng); a = x['a']; row.append((x['K'], round(x['frac_complete'], 3)))
            print('AGES B', s, row)
