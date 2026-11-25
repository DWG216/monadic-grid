"""t130: a local world of reflective monads. t128's dynamics (L x L periodic grid, radius r, N frequencies, derived rules, will
for turning), with a fraction of reflective monads: each keeps a memory of its own local record w_jk over the whole Age, measures its
correlation time (lag-1 autocorrelation pooled as the median over its frequencies), and acts (listening and growth) only where
m - 1 exceeds Student's t for N T alpha = 1 with n_eff - 1 degrees of freedom (t127); otherwise it hears 1.
Measures: complete (a >= 0.5, C > 0.8, holds a law at its focus), fixated (no coherent frequency nearby, C > 0.8), open (C < 0.1)."""
import numpy as np, sys
from scipy.stats import t as student
from t128_community import nsum
def run(seed, refl_frac, L=24, N=64, T=600, r=2, eta=0.3, will=0.2):
    rng = np.random.default_rng(seed); M = L*L; eps = 1/T; nb = (2*r + 1)**2
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    refl = rng.random(M) < refl_frac
    m = np.zeros((M, N)); s2 = np.zeros((M, N)); c1 = np.zeros((M, N)); w_prev = None
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den
        dm = w - m; m_old = m; m = m + dm/(t + 1); s2 = s2 + (dm*(w - m) - s2)/(t + 1)
        if w_prev is not None: c1 = c1 + ((w - m)*(w_prev - m_old) - c1)/t
        w_prev = w
        r1 = np.clip(np.median(c1/np.maximum(s2, 1e-12), axis=1), 0.0, 0.999); tau = (1 + r1)/(1 - r1)
        n_eff = np.maximum((t + 1)/tau, 2.0); thr = student.isf(1/(N*T), n_eff - 1)
        sig = (m - 1 > thr[:, None]*np.sqrt(s2/n_eff[:, None])) & (t > 2); judged = np.where(sig, m, 1.0)
        heard = np.where(refl[:, None], judged, w)
        e = (p*heard).sum(1)/heard.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*heard**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    order = np.abs(nsum(np.exp(1j*phi), L, r))/nb; coherent = order > 0.8; C = (p**2).sum(1); top = p.argmax(1)
    complete = (a >= 0.5) & (C > 0.8) & coherent[np.arange(M), top]; fix = (coherent.sum(1) == 0) & (C > 0.8); opn = C < 0.1
    foc_sig = sig[np.arange(M), top]; foc_order = order[np.arange(M), top]
    diag = dict(focus_judged_sig=float(foc_sig[refl].mean()) if refl.any() else np.nan, focus_order_med=float(np.median(foc_order)),
                focus_mem_m=float(np.median(m[np.arange(M), top])), focus_now_w=float(np.median(w[np.arange(M), top])), a_med=float(np.median(a)))
    held = top[coherent[np.arange(M), top]]; ids, cnt = np.unique(held, return_counts=True)
    out = dict(K=int((cnt >= 5).sum()), complete=float(complete.mean()), fixated=float(fix.mean()), open=float(opn.mean()))
    for nm, g in (('refl', refl), ('plain', ~refl)):
        if g.any(): out[f'complete_{nm}'] = float(complete[g].mean()); out[f'fixated_{nm}'] = float(fix[g].mean()); out[f'open_{nm}'] = float(opn[g].mean())
    out.update(diag); return out
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(24000, 24002) if mode == 'sanity' else range(25000, 25006)
    for f in ((0.0, 1.0, 0.5) if mode == 'sanity' else (0.0, 1.0)):
        for s in seeds: print(f'refl={f}', s, {k: round(v, 3) if isinstance(v, float) else v for k, v in run(s, f).items()}, flush=True)
