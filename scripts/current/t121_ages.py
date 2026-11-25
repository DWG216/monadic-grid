"""t121: the end of an Age and the next. t120's world. Novelty = mean over monads of the L1 change in attention per tick
(how much the record rewrites the monads). Age 1 runs T ticks; then spacetime closes: phases redrawn, attention reset to
near-uniform (the record forgotten); capacities kept ('souls keep'), or reset too ('souls reset', control). Age 2 runs T ticks.
Arrival = first tick with K >= 1 laws and median attention on laws > 0.9."""
import numpy as np, sys
def age(rng, a, T, M, N, gamma=0.02, kappa=0.2, eta=0.3, eps=1e-3):
    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    nov = []; arrive = -1
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); phi += np.minimum(kappa*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/p.sum(0); e = (p*w).sum(1)/w.mean(); a = np.clip(a*e**gamma, 0.01, 1.0)
        p_new = p*w**(0.1*a[:, None]); p_new /= p_new.sum(1, keepdims=True); p_new = (1 - eps)*p_new + eps/N
        nov.append(float(np.abs(p_new - p).sum(1).mean())); p = p_new
        if arrive < 0 and t % 5 == 0:
            r = np.abs(np.exp(1j*phi).mean(0)); laws = r > 0.8
            if laws.any() and np.median(p[:, laws].sum(1)) > 0.9: arrive = t
    r = np.abs(np.exp(1j*phi).mean(0)); laws = set(np.where(r > 0.8)[0].tolist())
    return a, np.array(nov), arrive, laws
def run(seed, keep=True, M=120, N=64, T=600):
    rng = np.random.default_rng(seed); a = 10**rng.uniform(-2, 0, M); a_init = a.copy()
    a, nov1, arr1, laws1 = age(rng, a, T, M, N)
    a2 = a if keep else a_init.copy()
    a, nov2, arr2, laws2 = age(rng, a2, T, M, N)
    a3 = a if keep else a_init.copy(); a, nov3, arr3, laws3 = age(rng, a3, T, M, N)
    peak = nov1[:50].max(); floor = np.median(nov1[-100:])
    jac = len(laws1 & laws2)/max(1, len(laws1 | laws2))
    return dict(arrive1=arr1, arrive2=arr2, ratio=(arr2/arr1) if (arr1 > 0 and arr2 >= 0) else np.nan, novelty_drop=float(peak/floor),
                floor=float(floor), K1=len(laws1), K2=len(laws2), jaccard=float(jac), arrive3=arr3, K3=len(laws3), ratio32=(arr3/arr2) if (arr2 > 0 and arr3 >= 0) else np.nan)
if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(12000, 12003) if m == 'sanity' else range(13000, 13010)
    for keep in (True, False):
        rs = [run(s, keep) for s in seeds]
        for s, r in zip(seeds, rs): print('keep' if keep else 'reset', s, {k: round(v, 4) if isinstance(v, float) else v for k, v in r.items()})
        print('MEDIAN', 'keep' if keep else 'reset', {k: round(float(np.nanmedian([r[k] for r in rs])), 4) for k in rs[0]})
