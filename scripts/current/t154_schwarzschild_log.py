"""t154: scalar entanglement across a Schwarzschild horizon on a record lattice uniform in proper distance. Pre-registration: PREDICTIONS_t154.md.
Units r_s = 1, T_H = 1/(4 pi). Hartle-Hawking state outside = thermal in Killing time; entropy summed over partial waves."""
import numpy as np
from scipy.optimize import brentq

def rho_of_r(r): return np.sqrt(r*(r - 1)) + np.log(np.sqrt(r) + np.sqrt(r - 1))
def r_of_rho(p): return 1.0 if p == 0 else brentq(lambda r: rho_of_r(r) - p, 1.0, 1.0 + p + p*p + 1.0, xtol=1e-15, rtol=1e-15)

def setup(L, rbox):
    eps = 1.0/L; M = int(np.floor(rho_of_r(rbox)/eps)) - 1
    rs_site = np.array([r_of_rho((i + 1)*eps) for i in range(M)])
    rs_mid = np.array([r_of_rho((i + 0.5)*eps) for i in range(M + 1)])
    return eps, M, rs_site, rs_mid

def S_l(l, eps, M, r, rm):
    sf, sfm = np.sqrt(1 - 1/r), np.sqrt(1 - 1/rm)
    W = l*(l + 1)/r**2 + 1/r**3
    d = (sfm[:-1] + sfm[1:])/eps + eps*sf*W
    off = -sfm[1:-1]/eps
    m = eps/sf; s = 1/np.sqrt(m)
    A = np.diag(d*s*s) + np.diag(off*s[:-1]*s[1:], 1) + np.diag(off*s[:-1]*s[1:], -1)
    w2 = np.linalg.eigvalsh(A); x = 4*np.pi*np.sqrt(w2)
    return float(np.sum(x/np.expm1(x) - np.log(-np.expm1(-x))))

def S_total(L, rbox=4.0, tol=1e-14):
    eps, M, r, rm = setup(L, rbox); tot = 0.0; l = 0; prev = np.inf
    while True:
        t = (2*l + 1)*S_l(l, eps, M, r, rm); tot += t
        if t < tol and t < prev and l > 5: break
        prev = t; l += 1
    return tot, l

def fit(Ls, Ss):
    L = np.array(Ls, float); A = np.column_stack([L**2, np.log(L), np.ones_like(L), 1/L**2])
    return np.linalg.lstsq(A, np.array(Ss), rcond=None)[0]

if __name__ == '__main__':
    out = {}
    Ls = [8, 10, 12, 14, 16, 20, 24, 28, 32, 40]
    S4 = {}
    for L in Ls:
        S4[L], lm = S_total(L); print(f'L={L:3d}  S={S4[L]:.10f}  lmax={lm}', flush=True)
    s20b, _ = S_total(20, tol=1e-16)
    out['S1'] = dict(S20=S4[20], S20_tight=s20b, diff=abs(s20b - S4[20]), pass_=abs(s20b - S4[20]) < 1e-6)
    c4 = fit(Ls, [S4[L] for L in Ls])
    L6 = [L for L in Ls if L <= 32]; S6 = {L: S_total(L, rbox=6.0)[0] for L in L6}
    c6 = fit(L6, [S6[L] for L in L6])
    out['S2'] = dict(c_log_box4=c4[1], c_log_box6=c6[1], pass_=abs(c6[1]/c4[1] - 1) < 0.10)
    out['P1'] = dict(c2=c4[0], c_log=c4[1], target=1/45, dev=c4[1]*45 - 1, pass_=abs(c4[1]*45 - 1) < 0.15)
    out['P2'] = dict(sign_flat=-1, sign_horizon=int(np.sign(c4[1])), pass_=c4[1] > 0)
    for k, v in out.items(): print(k, v)
