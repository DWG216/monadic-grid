"""t179: static potential and Cornell fit from t177's Wilson loops; glueball ratio. Pre-registration: PREDICTIONS_t179.md."""
import numpy as np
from scipy.optimize import curve_fit
NB = 20
def cornell(R, V0, s, e): return V0 + s*R - e/R
def analyse(W, O):
    m = W.mean(0); R = np.arange(1, 5, dtype=float)
    V = np.log(m[1:5, 3]/m[1:5, 4])
    p, _ = curve_fit(cornell, R, V, p0=[0.5, 0.07, 0.26])
    L = O.shape[1]; Oc = O - O.mean()
    C = lambda t: np.mean([np.mean(Oc[:, x]*Oc[:, (x + t) % L]) for x in range(L)])
    mass = np.log(C(1)/C(2))
    return np.array([p[1], p[2], mass, mass/np.sqrt(p[1])]), V
res = {}
for g in ('SU2', '2I'):
    d = np.load('t177_%s.npz' % g); W, O = d['W'], d['O']
    full, V = analyse(W, O)
    nbW, nbO = len(W)//NB, len(O)//NB
    jk = np.array([analyse(np.concatenate([W[:i*nbW], W[(i + 1)*nbW:NB*nbW]]), np.concatenate([O[:i*nbO], O[(i + 1)*nbO:NB*nbO]]))[0] for i in range(NB)])
    err = np.sqrt((NB - 1)*np.mean((jk - jk.mean(0))**2, 0))
    res[g] = dict(sigma=full[0], sigma_err=err[0], e=full[1], e_err=err[1], mass=full[2], mass_err=err[2], ratio=full[3], ratio_err=err[3], V=V.round(4).tolist())
    print(g, res[g])
su, i2 = res['SU2'], res['2I']
print('P1', dict(e=su['e'], sigma=su['sigma'], pass_=(0.13 <= su['e'] <= 0.52) and abs(su['sigma']/0.071 - 1) < 0.30))
print('P2', dict(ratio=su['ratio'], rel=abs(su['ratio']/3.78 - 1), pass_=abs(su['ratio']/3.78 - 1) < 0.20))
ds = abs(su['sigma'] - i2['sigma']); dr = abs(su['ratio'] - i2['ratio'])
print('P3', dict(dsigma=ds, two_sig_sigma=2*np.hypot(su['sigma_err'], i2['sigma_err']), dratio=dr, two_sig_ratio=2*np.hypot(su['ratio_err'], i2['ratio_err']),
                 pass_=ds < 2*np.hypot(su['sigma_err'], i2['sigma_err']) and dr < 2*np.hypot(su['ratio_err'], i2['ratio_err'])))
