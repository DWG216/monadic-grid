"""t86: everpresent Lambda histories (t72, alpha = 1, regenerated) against DESI DR2 BAO distances. Pre-registration: PREDICTIONS_t86.md."""
import numpy as np, math
OM = 0.31; AI = 1e-3; DL = 2e-4; NR = 20000
lna = np.arange(math.log(AI), DL/2, DL); a_grid = np.exp(lna)
keep = a_grid >= 0.29; ka = a_grid[keep]; kl = lna[keep]
fitmask = a_grid >= 1/3
Z = [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330]
DATA = [('V', 0.295, 7.942, 0.075), ('M', 0.510, 13.588, 0.167), ('H', 0.510, 21.863, 0.425), ('M', 0.706, 17.351, 0.177), ('H', 0.706, 19.455, 0.330),
        ('M', 0.934, 21.576, 0.152), ('H', 0.934, 17.641, 0.193), ('M', 1.321, 27.601, 0.318), ('H', 1.321, 14.176, 0.221), ('M', 1.484, 30.512, 0.760),
        ('H', 1.484, 12.817, 0.516), ('M', 2.330, 38.988, 0.531), ('H', 2.330, 8.632, 0.101)]
d = np.array([x[2] for x in DATA]); sg = np.array([x[3] for x in DATA])
def chi2_from_E(E):
    """E over the kept ln a grid (ascending), normalised to 1 at a = 1."""
    f = 1/(ka*E)                                         # integrand in ln a
    cum = np.concatenate([[0], np.cumsum(0.5*(f[1:]+f[:-1])*np.diff(kl))])
    DMfull = cum[-1] - cum                               # integral from ln a to 0
    m = []
    for kind, z, _, _ in DATA:
        la = -math.log(1+z); DM = np.interp(la, kl, DMfull); Ez = np.interp(la, kl, E)
        DH = 1/Ez
        m.append(DM if kind == 'M' else DH if kind == 'H' else (z*DM**2*DH)**(1/3))
    m = np.array(m); s = np.sum(d*m/sg**2)/np.sum(m**2/sg**2)
    return float(np.sum(((d - s*m)/sg)**2)), s
def E_lcdm(om): return np.sqrt(om*ka**-3 + 1 - om)
out = {}
oms = np.arange(0.20, 0.40001, 0.0005); c2 = [chi2_from_E(E_lcdm(o))[0] for o in oms]
ib = int(np.argmin(c2)); chi2_ref, om_best = c2[ib], oms[ib]; chi2_031 = chi2_from_E(E_lcdm(0.31))[0]
# S1: constant Lambda through the history path (H2 = OM a^-3 + Lam/3 with Omega_L0 = 0.69 relative to H(a=1))
Lam = 3*0.69/0.31*OM; H2 = OM*ka**-3 + Lam/3; Ec = np.sqrt(H2/H2[-1])
out['S1'] = dict(chi2=chi2_from_E(Ec)[0], chi2_lcdm031=chi2_031, pass_=abs(chi2_from_E(Ec)[0]-chi2_031) < 0.01)
out['S2'] = dict(om_best=round(float(om_best), 4), chi2_ref=chi2_ref, pass_=0.28 <= om_best <= 0.32)
# regenerate t72 alpha = 1 exactly
rng = np.random.default_rng(72); alpha = 1
V = np.full(NR, (4*math.pi/3)*OM**-2*AI**6/6); W = rng.normal(0, np.sqrt(V))
alive = np.ones(NR, bool); H2keep = np.empty((NR, keep.sum()), np.float32); rhofit = np.empty((NR, fitmask.sum())); kk = 0; kf = 0
for k, la in enumerate(lna):
    a = math.exp(la); LamV = alpha*W/V; H2v = OM*a**-3 + LamV/3
    alive &= H2v > 0
    if keep[k]: H2keep[:, kk] = H2v; kk += 1
    if fitmask[k]: rhofit[:, kf] = LamV/3; kf += 1
    if k == lna.size-1: break
    H2s = np.where(alive, H2v, 1.0); dV = (4*math.pi/3)*H2s**-2*DL
    W = W + np.sqrt(dV)*rng.standard_normal(NR); V = V + dV
OL0 = np.where(alive, (LamV/3)/np.where(alive, H2v, 1), np.nan)
acc = np.where(alive & (OL0 >= 0.65) & (OL0 <= 0.73))[0]
out['S3'] = dict(accepted=len(acc), pass_=len(acc) == 347)
res = []
for i in acc:
    H = H2keep[i].astype(float); E = np.sqrt(H/H[-1]); c, s = chi2_from_E(E)
    neg = bool(np.any(rhofit[i] <= 0)); res.append((c, neg))
c = np.array([r[0] for r in res]); neg = np.array([r[1] for r in res])
ok = c <= chi2_ref + 4
out['P1'] = dict(frac=float(ok.mean()), n=int(ok.sum()), of=len(c), pass_=ok.mean() >= 0.05, refuted=ok.mean() < 0.01)
out['P2'] = dict(best_chi2=float(c.min()), chi2_lcdm031=chi2_031, n_better=int((c < chi2_031).sum()), pass_=bool((c < chi2_031).any()))
out['P3'] = dict(frac=float(ok[neg].mean()) if neg.any() else None, n=int(ok[neg].sum()), of=int(neg.sum()), pass_=bool(neg.any()) and ok[neg].mean() >= 0.05)
out['info'] = dict(chi2_ref=chi2_ref, chi2_median=float(np.median(c)), chi2_16_84=[float(x) for x in np.percentile(c, [16, 84])], passers_with_negative=int((ok & neg).sum()))
for k, v in out.items(): print(k, v)
