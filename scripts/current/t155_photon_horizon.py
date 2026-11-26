"""t155: the photon on a Schwarzschild horizon: two transverse polarisations (Regge-Wheeler, spin 1) on the t154 lattice,
plus the edge term from balanced flux pairs on the horizon sphere. Pre-registration: PREDICTIONS_t155.md."""
import numpy as np
from scipy.special import zeta as hz, binom, digamma
import t154_schwarzschild_log as b

def zeta_S2(s, K=40):
    """Sum over l >= 1 of (2l+1)(l(l+1))^(-s), continued to small s: l(l+1) = x^2 - 1/4, x = l + 1/2, binomial series in Hurwitz zetas.
    k = 0: zeta_H(2s - 1, a) taken at -1 by Bernoulli, -B2(a)/2 (error O(s)); k = 1: pole, zeta_H(1 + d, a) = 1/d - digamma(a) + O(d)."""
    a = 1.5; tot = 2*(-(a*a - a + 1/6)/2)
    tot += binom(-s, 1)*(-0.25)*2*(1/(2*s) - digamma(a))
    for k in range(2, K):
        tot += binom(-s, k)*(-0.25)**k*2*hz(2*s + 2*k - 1, a)
    return tot

def S_l_photon(l, eps, M, r, rm):
    sf, sfm = np.sqrt(1 - 1/r), np.sqrt(1 - 1/rm)
    W = l*(l + 1)/r**2                                   # Regge-Wheeler, spin 1
    d = (sfm[:-1] + sfm[1:])/eps + eps*sf*W; off = -sfm[1:-1]/eps
    s = 1/np.sqrt(eps/sf)
    A = np.diag(d*s*s) + np.diag(off*s[:-1]*s[1:], 1) + np.diag(off*s[:-1]*s[1:], -1)
    x = 4*np.pi*np.sqrt(np.linalg.eigvalsh(A))
    with np.errstate(over='ignore'):
        return float(np.sum(x/np.expm1(x) - np.log(-np.expm1(-x))))

def S_photon(L, rbox=4.0, tol=1e-14):
    eps, M, r, rm = b.setup(L, rbox); tot = 0.0; l = 1; prev = np.inf
    while True:
        t = 2*(2*l + 1)*S_l_photon(l, eps, M, r, rm); tot += t       # two parities
        if t < tol and t < prev and l > 5: break
        prev = t; l += 1
    return tot

if __name__ == '__main__':
    out = {}
    z0 = zeta_S2(1e-12)
    out['S1'] = dict(zeta0=float(z0), target=-2/3, pass_=abs(z0 + 2/3) < 1e-10)
    Ls = [8, 10, 12, 14, 16, 20, 24, 28, 32, 40]
    S = {}
    for L in Ls:
        S[L] = S_photon(L); print(f'L={L:3d}  S_bulk={S[L]:.10f}', flush=True)
    c = b.fit(Ls, [S[L] for L in Ls])
    edge = float(z0)/2
    out['P1'] = dict(c_log_bulk=c[1], target=4/90, dev=c[1]/(4/90) - 1, pass_=abs(c[1]/(4/90) - 1) < 0.15)
    tot = c[1] + edge
    out['P2'] = dict(edge=edge, total=tot, target=-26/90, dev=tot/(-26/90) - 1, pass_=abs(tot/(-26/90) - 1) < 0.15)
    for k, v in out.items(): print(k, v)
