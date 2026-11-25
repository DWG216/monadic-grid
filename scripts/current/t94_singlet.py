"""t94: neutral mass matrix of the 27's odd states (N, h_u0, h_d0). Pre-registration: PREDICTIONS_t94.md."""
import numpy as np
v = 174.0; mu = 1100.0; Mstar = 2.435e18
MN = [vp**4/Mstar**3 for vp in (4.48e13, 7.3e13)]
def spec(lam, tb, mN):
    vu, vd = v*np.sin(np.arctan(tb)), v*np.cos(np.arctan(tb))
    M = np.array([[mN, lam*vd, lam*vu], [lam*vd, 0, mu], [lam*vu, mu, 0]])
    w, U = np.linalg.eigh(M); idx = np.argsort(np.abs(w)); return np.abs(w[idx]), U[:, idx]
out = {}
m0, U0 = spec(0, 10, MN[0]); out['S1'] = dict(masses=m0.tolist(), pass_=abs(m0[1] - mu) < 1e-9 and abs(m0[2] - mu) < 1e-9 and abs(m0[0] - MN[0]) < 1e-12)
out['P1'] = dict(M_N=MN, pass_=all(1e-3 <= x <= 10 for x in MN))
rows = []; p2 = True; p3 = True
for mN in MN:
    for lam in (0.1, 0.3, 1.0):
        for tb in (2, 10, 50):
            m, U = spec(lam, tb, mN)
            split = abs(m[2] - m[1]); fN = U[0, 0]**2
            rows.append(dict(M_N=round(mN, 4), lam=lam, tb=tb, lightest=round(float(m[0]), 4), N_frac=round(float(fN), 4), split_GeV=float(split)))
            p2 &= split > 2e-4; p3 &= fN > 0.5
out['P2'] = dict(min_split_GeV=min(r['split_GeV'] for r in rows), pass_=p2)
out['P3'] = dict(min_N_frac=min(r['N_frac'] for r in rows), pass_=p3)
for r in rows: print(r)
for k, x in out.items(): print(k, x)
