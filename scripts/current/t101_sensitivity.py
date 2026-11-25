"""t101 sensitivity (after scoring, labelled; not a test): how much does m_h move if the Higgs quartic's gauge term above the meeting is larger than the SM form, as it is when the doublet sits in SU(3)_L x SU(3)_R multiplets? Gauge coefficient c g^4 with c from 1.71 (SM form used in t101) to 4.33 (two SU(3) fundamentals, no cross term)."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = open('t101_higgs_full.py').read(); ns = {'__file__': os.path.abspath('t101_higgs_full.py')}; exec(src[:src.index('\nout = {}')], ns)
beta_sm, lam_mt, make_beta, k, Mstar = ns['beta_sm'], ns['lam_mt'], ns['make_beta'], ns['k'], ns['Mstar']
def run(mh, Mt, MH, nH, MD, M3, nh, c):
    y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(mh, Mt)]
    s1 = solve_ivp(make_beta(MH, nH, MD, None, nh), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12)
    g1, g2, g3, yt, l = s1.y[:, -1]; g = float(np.mean([g3, g2, np.sqrt(5/3)*g1]))
    base = make_beta(MH, nH, MD, M3, nh)
    def b(t, y):
        r = base(t, y); r[4] += k*(c - 1.71)*y[0]**4; return r
    return solve_ivp(b, [np.log(M3), np.log(Mstar)], [g, g, g, yt, l], rtol=1e-10, atol=1e-12).y[4, -1]
for c in (1.71, 2.5, 3.0, 4.33):
    m = brentq(lambda mh: run(mh, 172.57, 1.0e3, 2, 3.16e12, 4.98e13, 0, c), 80, 200)
    print('gauge coefficient above the meeting', c, '-> m_h =', round(m, 2), 'GeV')
