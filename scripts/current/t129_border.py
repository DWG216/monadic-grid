"""t129: the border test. t128's local dynamics (L x L grid, radius r) with N = 24 frequencies, second order only ('second'),
or second plus third order ('third'): each monad also reads its neighbourhood's triad record B_t = sum over neighbours of
sqrt(p_k1 p_k2 p_k3) e^{i psi}, psi = phi_k1 + phi_k2 - phi_k3 (k1 + k2 = k3 mod N), listens to w_k = max(second-order w_k,
max over triads containing k of |B_t|^2 / sum a^2), and turns its psi toward arg B_t (will x capacity, shared over the three phases).
Measures: complete (t128: holds a law at its focus); whole (attention > 0.9 on the frequencies coherent in its neighbourhood, at least
a third of an even share on each); border monads = those whose neighbourhood holds >= 2 coherent frequencies."""
import numpy as np, sys
from t128_community import nsum
from t118_relations import triads
def run(seed, mode='third', L=24, N=24, T=600, r=2, eta=0.3, will=0.2):
    rng = np.random.default_rng(seed); M = L*L; eps = 1/T; tr = triads(N); nb = (2*r + 1)**2
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N))
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N)); c = np.sqrt(p)*np.exp(1j*phi)
        z = nsum(c, L, r); den = nsum(p, L, r)
        phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(z) - phi)
        w = np.abs(z)**2/den
        if mode == 'third':
            psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; at = np.sqrt(p[:, tr[:, 0]]*p[:, tr[:, 1]]*p[:, tr[:, 2]])
            B = nsum(at*np.exp(1j*psi), L, r); coh = np.abs(B)**2/np.maximum(nsum(at**2, L, r), 1e-30)
            g = np.minimum(will*a[:, None]*at*N**1.5, 1.0)*np.sin(np.angle(B) - psi)/3
            d = np.zeros_like(phi); np.add.at(d.T, tr[:, 0], g.T); np.add.at(d.T, tr[:, 1], g.T); np.add.at(d.T, tr[:, 2], -g.T); phi = phi + d
            w3 = np.ones_like(w)
            for col in range(3): np.maximum.at(w3.T, tr[:, col], coh.T)
            w = np.maximum(w, w3)
        e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    order = np.abs(nsum(np.exp(1j*phi), L, r))/nb; coherent = order > 0.8
    top = p.argmax(1); complete = (a >= 0.5) & ((p**2).sum(1) > 0.8) & coherent[np.arange(M), top]
    nS = coherent.sum(1); share = (p*coherent).sum(1)
    even_ok = np.array([np.all(p[j, coherent[j]] >= (1/3)*share[j]/max(nS[j], 1)) for j in range(M)])
    whole = (nS >= 1) & (share > 0.9) & even_ok; border = nS >= 2
    psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; R = np.abs(nsum(np.exp(1j*psi), L, r))/nb
    rel = int(((R > 0.8).sum(0) >= 5).sum())
    return dict(frac_complete=float(complete.mean()), frac_whole=float(whole.mean()), frac_border=float(border.mean()),
                whole_on_border=float(whole[border].mean()) if border.any() else np.nan, relations=rel, C_med=float(np.median((p**2).sum(1))), frac_fixated_incoherent=float(((nS == 0) & ((p**2).sum(1) > 0.8)).mean()))
if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(22000, 22002) if m == 'sanity' else range(23000, 23010)
    for mode in ('second', 'third'):
        for s in seeds: print(mode, s, {k: round(v, 3) if isinstance(v, float) else v for k, v in run(s, mode).items()}, flush=True)
