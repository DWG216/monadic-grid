"""t109: y_b/y_tau at gravity's meeting. Pre-registration: PREDICTIONS_t109.md."""
import numpy as np
from scipy.integrate import solve_ivp
src = open(__file__.replace('t109_b_tau.py', 't108_veltman.py')).read(); ns = {'__file__': __file__.replace('t109_b_tau.py', 't108_veltman.py')}
exec(src[:src.index('\nout = {}')], ns); traj, Mstar = ns['traj'], ns['Mstar']; k = 1/(16*np.pi**2)
def R_at(cfg, R0, Mt=172.57):
    f, _ = traj(125.2, Mt, cfg, top=Mstar)
    def rhs(t, y): gp, g2, g3, yt, l = f(t); return [k*(-1.5*yt**2 + 10/3*gp**2 - 8*g3**2)]
    return float(np.exp(solve_ivp(rhs, [np.log(Mt), np.log(Mstar)], [np.log(R0)], rtol=1e-10).y[0, -1]))
cases = {'A': (1.33e8, 3, 3.16e13, 4.48e13, 2), 'B': (1.0e3, 2, 3.16e12, 4.98e13, 2), 'SM': (None, 0, None, None, 0)}
out = {}
R = {n: R_at(c, 2.75/1.75) for n, c in cases.items()}
out['P1'] = dict(R_B=R['B'], pass_=0.9 < R['B'] < 1.1)
# information: s/mu and d/e (same running, light Yukawas): masses at m_t, m_s 0.055, m_mu 0.1027, m_d 2.75e-3, m_e 4.87e-4
out['info'] = dict(R=R, s_over_mu_B=R_at(cases['B'], 0.055/0.1027), d_over_e_B=R_at(cases['B'], 2.75e-3/4.87e-4))
for a, b in out.items(): print(a, b)
