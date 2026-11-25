"""t101: lambda(M*) = 0 with the grid's exotic thresholds and the meeting. Pre-registration: PREDICTIONS_t101.md."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
src = open(__file__.replace('t101_higgs_full.py', 't100_higgs.py')).read(); ns = {}; exec(src[:src.index('out = {}')], ns)
beta_sm, lam_mt = ns['beta'], ns['lam_mt']; k = 1/(16*np.pi**2); Mstar = 2.435e18
def make_beta(MH, nH, MD, M3, nh):
    def beta(t, y):
        mu = np.exp(t)
        if M3 is not None and mu >= M3:
            g, yt, l = y[0], y[3], y[4]
            g1, g2 = np.sqrt(3/5)*g, g
            bg = -(-5 + nh)*k*g**3 * (-1)        # alpha^-1 decreases? b = -5 + n_h with d(alpha^-1)/dt = -b/(2 pi): dg/dt = b g^3 k
            bg = (-5 + nh)*k*g**3
            b = beta_sm(t, [g1, g2, g, yt, l])
            return [bg, bg, bg, b[3], b[4]]
        b = beta_sm(t, y)
        g1, g2, g3 = y[0], y[1], y[2]
        if MH is not None and mu >= MH: b[0] += k*nH*(2/3)*g1**3; b[1] += k*nH*(2/3)*g2**3
        if MD is not None and mu >= MD: b[0] += k*3*(4/9)*g1**3; b[2] += k*3*(2/3)*g3**3
        return b
    return beta
def run(mh, Mt, cfg):
    MH, nH, MD, M3, nh = cfg
    y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(mh, Mt)]
    if M3 is None:
        return solve_ivp(make_beta(*cfg), [np.log(Mt), np.log(Mstar)], y0, rtol=1e-10, atol=1e-12).y[:, -1], None
    s1 = solve_ivp(make_beta(MH, nH, MD, None, nh), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12)
    g1, g2, g3, yt, l = s1.y[:, -1]; gs = [g3, g2, np.sqrt(5/3)*g1]; g = float(np.mean(gs)); spread = (max(gs) - min(gs))/g
    s2 = solve_ivp(make_beta(MH, nH, MD, M3, nh), [np.log(M3), np.log(Mstar)], [g, g, g, yt, l], rtol=1e-10, atol=1e-12)
    return s2.y[:, -1], spread
def mh_pred(Mt, cfg): return brentq(lambda mh: run(mh, Mt, cfg)[0][4], 90, 200)
out = {}
m0 = mh_pred(172.57, (None, 0, None, None, 0)); out['S1'] = dict(mh=m0, pass_=abs(m0 - 128.4986) < 0.01)
cases = {'A': (1.33e8, 3, 3.16e13, 4.48e13), 'B': (1.0e3, 2, 3.16e12, 4.98e13)}
res = {}
for name, (MH, nH, MD, M3) in cases.items():
    res[name] = {}
    for nh in range(4):
        cfg = (MH, nH, MD, M3, nh); m = mh_pred(172.57, cfg); _, spread = run(125.2, 172.57, cfg)
        res[name][nh] = dict(mh=round(m, 3), spread=round(spread, 4))
out['S2'] = dict(spreads={n: res[n][0]['spread'] for n in res}, pass_=all(res[n][0]['spread'] < 0.02 for n in res))
out['P1'] = dict(mh={nh: res['A'][nh]['mh'] for nh in range(4)}, pass_=all(abs(res['A'][nh]['mh'] - 125.20) <= 2 for nh in range(4)))
out['P2'] = dict(mh={nh: res['B'][nh]['mh'] for nh in range(4)}, pass_=all(abs(res['B'][nh]['mh'] - 125.20) <= 2 for nh in range(4)))
out['info'] = dict(Mt_for_125p2_A_nh0=brentq(lambda Mt: mh_pred(Mt, (1.33e8, 3, 3.16e13, 4.48e13, 0)) - 125.20, 165, 180))
for k_, v in out.items(): print(k_, v)
