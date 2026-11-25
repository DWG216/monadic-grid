"""t87: constant Lambda (fixed count) against DESI DR2 BAO; CPL scan; the count's size. Pre-registration: PREDICTIONS_t87.md."""
import numpy as np, math
from scipy.stats import chi2 as C2
src = open(__file__.replace('t87_constant_lambda.py', 't86_everpresent_distances.py')).read()
ns = {}; exec(src[:src.index('def E_lcdm')], ns)              # DATA, grids, chi2_from_E
ka, chi2_from_E = ns['ka'], ns['chi2_from_E']
def E_cpl(om, w0, wa): return np.sqrt(om*ka**-3 + (1-om)*ka**(-3*(1+w0+wa))*np.exp(-3*wa*(1-ka)))
out = {}
oms = np.arange(0.20, 0.40001, 0.0005); c = [chi2_from_E(E_cpl(o, -1, 0))[0] for o in oms]; i = int(np.argmin(c)); chi_l, om_l = c[i], oms[i]
out['S1'] = dict(om=round(float(om_l), 4), chi2=chi_l, pass_=abs(om_l-0.2995) < 1e-9 and abs(chi_l-11.4383) < 1e-3)
W0 = np.round(np.arange(-2.0, 0.50001, 0.05), 4); WA = np.round(np.arange(-3.0, 2.00001, 0.1), 4); OMc = np.arange(0.20, 0.40001, 0.01)
best = (1e9, None)
for o in OMc:
    for w0 in W0:
        for wa in WA:
            E2 = o*ka**-3 + (1-o)*ka**(-3*(1+w0+wa))*np.exp(-3*wa*(1-ka))
            if np.any(E2 <= 0): continue
            v = chi2_from_E(np.sqrt(E2))[0]
            if v < best[0]: best = (v, (round(float(o), 3), float(w0), float(wa)))
# refine around the best
o0, w00, wa0 = best[1]
for o in np.arange(o0-0.01, o0+0.01001, 0.001):
    for w0 in np.arange(w00-0.05, w00+0.05001, 0.005):
        for wa in np.arange(wa0-0.1, wa0+0.10001, 0.01):
            if not (0.20 - 1e-9 <= o <= 0.40 + 1e-9 and -2.0 - 1e-9 <= w0 <= 0.5 + 1e-9 and -3.0 - 1e-9 <= wa <= 2.0 + 1e-9): continue   # run 2: stay inside the registered box
            E2 = o*ka**-3 + (1-o)*ka**(-3*(1+w0+wa))*np.exp(-3*wa*(1-ka))
            if np.any(E2 <= 0): continue
            v = chi2_from_E(np.sqrt(E2))[0]
            if v < best[0]: best = (v, (round(float(o), 4), round(float(w0), 4), round(float(wa), 4)))
out['S2'] = dict(lcdm_in_grid=bool((-1.0 in W0) and (0.0 in WA)), pass_=bool((-1.0 in W0) and (0.0 in WA)))
out['P1'] = dict(chi2=chi_l, dof=11, p=float(C2.sf(chi_l, 11)), pass_=C2.sf(chi_l, 11) > 0.05)
out['P2'] = dict(best_cpl=best[1], chi2_cpl=best[0], delta=chi_l-best[0], pass_=chi_l-best[0] < 6.18)
H0 = 67.7*1e3/3.0857e22; tP = 5.391e-44; N = (1/(H0*tP))**4; est = 1/math.sqrt(N); obs = 2.9e-122
out['P3'] = dict(N=N, estimate=est, observed=obs, ratio=est/obs, pass_=1/3 <= est/obs <= 3)
for k, v in out.items(): print(k, v)
