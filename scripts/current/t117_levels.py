"""t117: do Leibniz's levels appear? t116's dialectic with a capacity a_j per monad (log-uniform on [0.01, 1]):
listening rate beta_j = 0.1 a_j, turning strength kappa_j = kappa a_j. Per monad at the end: distinctness C_j,
lawfulness L_j (attention share on laws), memory R_j (fraction of the last 100 ticks its top content stayed the same)."""
import numpy as np, sys
def run(seed, kappa=0.2, M=200, N=64, T=400, eta=0.3, eps=1e-3, lo=0.01, hi=1.0):
    rng = np.random.default_rng(seed); a = 10**rng.uniform(np.log10(lo), np.log10(hi), M)
    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    tops = []
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); Phi = np.angle(z)
        phi += np.minimum(kappa*a[:, None]*N*p, 1.0)*np.sin(Phi - phi)
        w = np.abs(z)**2/p.sum(0); p = p*w**(0.1*a[:, None]); p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
        if t >= T - 100: tops.append(p.argmax(1))
    r = np.abs(np.exp(1j*phi).mean(0)); laws = r > 0.8; tops = np.array(tops)
    C = (p**2).sum(1); L = p[:, laws].sum(1) if laws.any() else np.zeros(M); R = (tops == tops[-1]).mean(0)
    return a, C, L, R, int(laws.sum())
def summary(a, C, L, R, K):
    la = np.log10(a); order = np.argsort(la); lc = np.log10(C)[order]; L_ = L[order]
    bins = np.linspace(-2, 0, 11); idx = np.digitize(la[order], bins) - 1
    prof = [(round(float(np.median(L_[idx == b])), 2), round(float(np.median(lc[idx == b])), 2)) for b in range(10) if np.any(idx == b)]
    return dict(K=K, profile_L_logC_by_capacity_decile=prof)
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'
    if mode == 'sanity':
        for s in (5000, 5001):
            a, C, L, R, K = run(s); print(s, summary(a, C, L, R, K))
        raise SystemExit
    res = []
    for s in range(6000, 6010):
        a, C, L, R, K = run(s); la = np.log10(a); lc = np.log10(C); bins = np.linspace(-2, 0, 11); idx = np.clip(np.digitize(la, bins) - 1, 0, 9)
        med = np.array([np.median(lc[idx == b]) for b in range(10)]); steps = np.diff(med); i = int(np.argmax(steps)); srt = np.sort(steps)
        sharp = steps.max()/steps.mean(); second = srt[-2]/srt[-1]
        Lab = float(np.median(L[idx > i])); Lbe = float(np.median(L[idx <= i]))
        res.append((K, sharp, second, Lab, Lbe)); print(s, dict(K=K, sharpness=round(sharp, 2), second_over_first=round(second, 2), L_above=round(Lab, 2), L_below=round(Lbe, 2), steps=[round(x, 2) for x in steps]))
    wl = [r for r in res if r[0] >= 1]; nl = [r for r in res if r[0] == 0]
    print('P1 fraction with laws', len(wl)/len(res))
    if wl: print('P2 median sharpness (laws)', round(float(np.median([r[1] for r in wl])), 2), 'pass', np.median([r[1] for r in wl]) > 3)
    if nl: print('P3 median sharpness (no laws)', round(float(np.median([r[1] for r in nl])), 2), 'pass', np.median([r[1] for r in nl]) < 3)
    if wl:
        print('P4 L above / below', round(float(np.median([r[3] for r in wl])), 2), round(float(np.median([r[4] for r in wl])), 2), 'pass', np.median([r[3] for r in wl]) > 0.5 and np.median([r[4] for r in wl]) < 0.3)
        print('P5 second/first', round(float(np.median([r[2] for r in wl])), 2), 'pass', np.median([r[2] for r in wl]) < 0.6)
