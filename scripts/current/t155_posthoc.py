"""t155 post hoc (after scoring): which difference between two scalars and the Regge-Wheeler photon carries the bulk shortfall?"""
import numpy as np
import t154_schwarzschild_log as b
def S_var(L, lmin, rs3, rbox=4.0, tol=1e-14):
    eps, M, r, rm = b.setup(L, rbox); tot = 0.0; l = lmin; prev = np.inf
    sf, sfm = np.sqrt(1 - 1/r), np.sqrt(1 - 1/rm); s = 1/np.sqrt(eps/sf)
    while True:
        W = l*(l + 1)/r**2 + (1/r**3 if rs3 else 0)
        d = (sfm[:-1] + sfm[1:])/eps + eps*sf*W; off = -sfm[1:-1]/eps
        A = np.diag(d*s*s) + np.diag(off*s[:-1]*s[1:], 1) + np.diag(off*s[:-1]*s[1:], -1)
        x = 4*np.pi*np.sqrt(np.linalg.eigvalsh(A))
        with np.errstate(over='ignore'): t = (2*l + 1)*float(np.sum(x/np.expm1(x) - np.log(-np.expm1(-x))))
        tot += t
        if t < tol and t < prev and l > 5: break
        prev = t; l += 1
    return tot
Ls = [8, 10, 12, 14, 16, 20, 24, 28, 32, 40]
for name, lmin, rs3 in [('scalar l>=0 with r_s/r^3 (t154)', 0, True), ('scalar l>=1 with r_s/r^3', 1, True), ('scalar l>=0 without r_s/r^3', 0, False), ('scalar l>=1 without (one photon parity)', 1, False)]:
    c = b.fit(Ls, [S_var(L, lmin, rs3) for L in Ls]); print(f'{name:42s} c_log = {c[1]:+.6f}  (x90 = {c[1]*90:+.3f})')
l0 = b.fit(Ls, [S_var(L, 0, True) - S_var(L, 1, True) for L in Ls]); print(f'l = 0 wave alone (with r_s/r^3)            c_log = {l0[1]:+.6f}  (x90 = {l0[1]*90:+.3f})')
