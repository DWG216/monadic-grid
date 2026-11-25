"""t122: reflection (judged memory). A reflective monad acts only on what its memory shows to be significant:
m_k - 1 > 3 standard errors (running variance v, effective samples tau*eta^2); otherwise it hears baseline 1.
Sanity history: memory alone (tau 20, then 100) reduced but did not stop the lawless climb.
Original note: t120's world, half the monads reflective. A reflective monad keeps a running memory of what it hears,
m_k <- (1 - 1/tau) m_k + w_k / tau (tau = 100, about 10x the noise correlation time 1/eta^2), and listens and climbs on that memory (what lasts) instead of the present w:
p <- p * m^(0.1 a), e = E_p[m] / mean(m). Unreflective monads as in t120. Lawful worlds kappa = 0.2; lawless kappa = 0."""
import numpy as np, sys
def run(seed, kappa, M=120, N=64, T=800, gamma=0.02, eta=0.3, eps=1e-3, tau=100.0):
    rng = np.random.default_rng(seed); a = 10**rng.uniform(-2, 0, M); refl = np.arange(M) % 2 == 0
    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N)); m = np.ones(N); v = np.ones(N)
    t_half = np.full(M, np.inf); false_sig = []
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); phi += np.minimum(kappa*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/p.sum(0); m = (1 - 1/tau)*m + w/tau; v = (1 - 1/tau)*v + (w - m)**2/tau
        se = np.sqrt(v/(tau/(1/eta**2))); judged = np.where(m - 1 > 3*se, m, 1.0)
        if t >= 200: false_sig.append(float((m - 1 > 3*se).mean()))
        heard = np.where(refl[:, None], judged[None, :], w[None, :])
        e = (p*heard).sum(1)/heard.mean(1); a = np.clip(a*e**gamma, 0.01, 1.0)
        p = p*heard**(0.1*a[:, None]); p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
        t_half[(a >= 0.5) & np.isinf(t_half)] = t
    r = np.abs(np.exp(1j*phi).mean(0)); laws = r > 0.8; C = (p**2).sum(1); L = p[:, laws].sum(1) if laws.any() else np.zeros(M)
    out = {}
    for name, g in (('refl', refl), ('plain', ~refl)):
        out[name] = dict(a_end=float(np.median(a[g])), frac_half=float((a[g] >= 0.5).mean()), C=float(np.median(C[g])), L=float(np.median(L[g])),
                         t_half=float(np.median(t_half[g][np.isfinite(t_half[g])])) if np.isfinite(t_half[g]).any() else np.nan)
    out['K'] = int(laws.sum()); out['sig_frac'] = float(np.mean(false_sig)); return out
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(14000, 14003) if mode == 'sanity' else range(15000, 15010)
    for kappa, nm in ((0.2, 'lawful'), (0.0, 'lawless')):
        rs = [run(s, kappa) for s in seeds]
        for s, r in zip(seeds, rs): print(nm, s, r)
        for g in ('refl', 'plain'): print('MEDIAN', nm, g, {k: round(float(np.nanmedian([r[g][k] for r in rs])), 3) for k in rs[0][g]})
        print('MEDIAN', nm, 'significant fraction of (tick, k) after tick 200:', round(float(np.median([r['sig_frac'] for r in rs])), 4), 'K', float(np.median([r['K'] for r in rs])))
