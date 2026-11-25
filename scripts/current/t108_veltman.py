"""t108: Str M^2 = 0 (Veltman's C = 0) at gravity's meeting. Pre-registration: PREDICTIONS_t108.md."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
src = open(__file__.replace('t108_veltman.py', 't101_higgs_full.py')).read(); ns = {'__file__': __file__.replace('t108_veltman.py', 't101_higgs_full.py')}
exec(src[:src.index('\nout = {}')], ns)
make_beta, lam_mt, Mstar = ns['make_beta'], ns['lam_mt'], ns['Mstar']
def traj(mh, Mt, cfg, top=10*Mstar):
    MH, nH, MD, M3, nh = cfg
    y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(mh, Mt)]
    if M3 is None:
        s = solve_ivp(make_beta(*cfg), [np.log(Mt), np.log(top)], y0, rtol=1e-10, atol=1e-12, dense_output=True)
        return lambda t: s.sol(t), None
    s1 = solve_ivp(make_beta(MH, nH, MD, None, nh), [np.log(Mt), np.log(M3)], y0, rtol=1e-10, atol=1e-12, dense_output=True)
    g1, g2, g3, yt, l = s1.y[:, -1]; g = float(np.mean([g3, g2, np.sqrt(5/3)*g1]))
    s2 = solve_ivp(make_beta(MH, nH, MD, M3, nh), [np.log(M3), np.log(top)], [g, g, g, yt, l], rtol=1e-10, atol=1e-12, dense_output=True)
    def f(t):
        if t < np.log(M3): return s1.sol(t)
        gg, _, _, yt, l = s2.sol(t); return np.array([np.sqrt(3/5)*gg, gg, gg, yt, l])
    return f, M3
def C(y): gp, g2, g3, yt, l = y; return 6*l + 9/4*g2**2 + 3/4*gp**2 - 6*yt**2
def crossing(f, Mt=172.57):
    ts = np.linspace(np.log(Mt)+0.01, np.log(10*Mstar), 4000); cs = [C(f(t)) for t in ts]
    roots = [brentq(lambda t: C(f(t)), ts[i], ts[i+1]) for i in range(len(ts)-1) if cs[i]*cs[i+1] < 0]
    return [float(np.exp(r)) for r in roots], C(f(np.log(Mstar)))
out = {}
f, _ = traj(125.2, 172.57, (None, 0, None, None, 0)); r, cM = crossing(f)
out['P1'] = dict(mu_V=r, C_Mstar=cM, pass_=any(Mstar/10 < x < 10*Mstar for x in r))
cases = {'A': (1.33e8, 3, 3.16e13, 4.48e13), 'B': (1.0e3, 2, 3.16e12, 4.98e13)}; res = {}; ok = True
for name, (MH, nH, MD, M3) in cases.items():
    for nh in range(4):
        f, _ = traj(125.2, 172.57, (MH, nH, MD, M3, nh)); r, cM = crossing(f)
        res[f'{name}{nh}'] = dict(mu_V=[f'{x:.2e}' for x in r], C_Mstar=round(cM, 4)); ok &= any(Mstar/10 < x < 10*Mstar for x in r)
out['P2'] = dict(cases=res, pass_=ok)
for a, b in out.items(): print(a, b)
