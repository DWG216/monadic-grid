"""t110: one count for baryons and dark matter. Pre-registration: PREDICTIONS_t110.md."""
import numpy as np
rng = np.random.default_rng(110); Mstar = 2.435e18; mp = 0.938272
oc, ob = rng.normal(0.1200, 0.0012, 100000), rng.normal(0.02237, 0.00015, 100000); mN = oc/ob*mp
lo, hi = np.percentile(mN, [16, 84]); m = float(np.median(mN))
out = {'P1': dict(m_N=m, band=(lo, hi), window=(0.015, 21), pass_=0.015 < lo and hi < 21)}
out['info'] = dict(v_psi=(m*Mstar**3)**0.25, M3_A=4.48e13, M3_B=4.98e13, MD_A=3.16e13)
for a, b in out.items(): print(a, b)
