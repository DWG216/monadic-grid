"""t109 post hoc (found during t112): above M3 the trinification gauge terms of the quark coupling tr(Q_L L Q_R) and the
lepton coupling det L are equal (each sums C2 over three fields: 2(C_C + C_L + C_R) = 8 = 3 * 2 * 4/3), so the gauge
part of d ln(y_b/y_tau)/dt vanishes above the meeting. t109 kept the SM-form difference 10/3 g'^2 - 8 g3^2 there.
Recompute with the gauge difference switched off above M3 (top term kept as in t109)."""
import numpy as np
from scipy.integrate import solve_ivp
src = open(__file__.replace('t109_posthoc.py', 't108_veltman.py')).read(); ns = {'__file__': __file__.replace('t109_posthoc.py', 't108_veltman.py')}
exec(src[:src.index('\nout = {}')], ns); traj, Mstar = ns['traj'], ns['Mstar']; k = 1/(16*np.pi**2)
def R(cfg, R0, Mt=172.57):
    f, M3 = traj(125.2, Mt, cfg, top=Mstar)
    def rhs(t, y):
        gp, g2, g3, yt, l = f(t); gauge = 0 if (M3 and t >= np.log(M3)) else 10/3*gp**2 - 8*g3**2
        return [k*(-1.5*yt**2 + gauge)]
    sol = solve_ivp(rhs, [np.log(Mt), np.log(Mstar)], [np.log(R0)], rtol=1e-10, dense_output=True)
    return float(np.exp(sol.sol(np.log(M3))[0])), float(np.exp(sol.y[0, -1]))
for n, c in {'A': (1.33e8, 3, 3.16e13, 4.48e13, 2), 'B': (1.0e3, 2, 3.16e12, 4.98e13, 2)}.items():
    r3, rs = R(c, 2.75/1.75); print(n, 'y_b/y_tau at M3', round(r3, 4), 'at M*', round(rs, 4))
