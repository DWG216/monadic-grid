"""t118: laws with content. A relation law is a triad (k1, k2, k3), k1 + k2 = k3 mod N, whose phase sum
psi_j = phi_k1 + phi_k2 - phi_k3 is shared across monads (triad order R_t > 0.8) while each frequency alone is scattered
(r_k < 0.3 for all three): a pure relation. Dynamics as t116 but the record read at third order:
B_t = sum_j a_jt e^{i psi_jt}, a_jt = sqrt(p_k1 p_k2 p_k3) N^{3/2}; each monad turns psi toward arg B_t with gain
min(kappa a_jt, 1) shared over its three phases (+, +, -); listening p <- p w^beta, w_k = max_{t contains k} |B_t|^2 / sum_j a_jt^2.
Controls: 'pair' = t116's second-order dynamics; 'none' = no turning."""
import numpy as np, sys
def triads(N):
    return np.array([(a, b, (a + b) % N) for a in range(1, N) for b in range(a, N) if (a + b) % N not in (0, a, b)])
def run(seed, mode='triad', kappa=0.2, M=50, N=24, T=300, eta=0.3, beta=0.1, eps=1e-3, return_state=False):
    rng = np.random.default_rng(seed); tr = triads(N); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True)
    phi = rng.uniform(0, 2*np.pi, (M, N))
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        if mode == 'triad':
            psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; a = np.sqrt(p[:, tr[:, 0]]*p[:, tr[:, 1]]*p[:, tr[:, 2]])*N**1.5
            B = (a*np.exp(1j*psi)).sum(0); g = np.minimum(kappa*a, 1.0)*np.sin(np.angle(B) - psi)/3
            d = np.zeros_like(phi); np.add.at(d.T, tr[:, 0], g.T); np.add.at(d.T, tr[:, 1], g.T); np.add.at(d.T, tr[:, 2], -g.T); phi += d
            coh = np.abs(B)**2/(a**2).sum(0); w = np.ones(N)
            for c in range(3): np.maximum.at(w, tr[:, c], coh)
        elif mode == 'pair':
            z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); phi += np.minimum(kappa*N*p, 1.0)*np.sin(np.angle(z) - phi); w = np.abs(z)**2/p.sum(0)
        else:
            w = np.abs((np.sqrt(p)*np.exp(1j*phi)).sum(0))**2/p.sum(0)
        p = p*w[None, :]**beta; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    if return_state: return phi, p, tr
    psi = phi[:, tr[:, 0]] + phi[:, tr[:, 1]] - phi[:, tr[:, 2]]; R = np.abs(np.exp(1j*psi).mean(0)); r = np.abs(np.exp(1j*phi).mean(0))
    rmax = np.max(r[tr], axis=1); pure = (R > 0.8) & (rmax < 0.3); synced = (R > 0.8) & (rmax >= 0.3)
    z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); w2 = np.abs(z)**2/p.sum(0)
    a = np.sqrt(p[:, tr[:, 0]]*p[:, tr[:, 1]]*p[:, tr[:, 2]]); B = (a*np.exp(1j*psi)).sum(0); w3 = np.abs(B)**2/(a**2).sum(0)
    pf = np.unique(tr[pure].ravel()) if pure.any() else np.array([], int)
    return dict(pure=int(pure.sum()), synced=int(synced.sum()), single_laws=int((r > 0.8).sum()),
                w2_on_pure=float(np.median(w2[pf])) if len(pf) else float('nan'), R_on_pure=float(np.median(R[pure])) if pure.any() else float('nan'), w3_on_pure=float(np.median(w3[pure])) if pure.any() else float('nan'),
                share_pure=float(p[:, pf].sum(1).mean()) if len(pf) else 0.0)
if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(7000, 7003) if m == 'sanity' else range(8000, 8012)
    for mode in ('triad', 'pair', 'none'):
        rs = [run(s, mode) for s in seeds]
        print(mode, {k: round(float(np.nanmedian([r[k] for r in rs])), 3) for k in rs[0]})
