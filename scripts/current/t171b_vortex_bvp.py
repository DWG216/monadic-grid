"""t171b: t171's P2 rerun with a boundary-value solver. Pre-registration: PREDICTIONS_t171b.md."""
import numpy as np
from scipy.integrate import solve_bvp
tau = 1.0; r0, R = 1e-4, 15.0
res = {}
for N in (1, 2, 3):
    def f_(r, y): return np.vstack([N*(1 - y[1])*y[0]/r, r*(tau - y[0]**2)/(2*N)])
    def bc(ya, yb): return np.array([ya[1], yb[0] - 1.0])
    # two first-order ODEs need two conditions; f(r0) ~ c r0^N is enforced by the ODE's regular branch at r0 via a(r0) = 0,
    # and f(R) = 1; a(R) = 1 is then checked, not imposed.
    r = np.concatenate([np.geomspace(r0, 1, 200), np.linspace(1.01, R, 800)])
    y = np.vstack([np.tanh(r)**N, np.tanh(r**2/4)])
    s = solve_bvp(f_, bc, r, y, tol=1e-8, max_nodes=100000)
    rr = np.concatenate([np.geomspace(r0, 1, 4000), np.linspace(1.0001, R, 40000)])
    f, a = s.sol(rr); fp, ap = f_(rr, np.vstack([f, a]))
    resid = np.abs(s.sol(rr, 1) - f_(rr, s.sol(rr))).max()
    B = N*ap/rr
    dens = 0.5*B**2 + 0.5*(fp**2 + (N*(1 - a)/rr)**2*f**2) + 0.125*(tau - f**2)**2
    E = np.trapezoid(2*np.pi*rr*dens, rr)
    res[N] = dict(status=s.status, nodes=len(s.x), f_R=f[-1], a_R=a[-1], resid=resid, flux_rel=abs(a[-1] - 1),
                  E=E, E_rel=abs(E/(np.pi*tau*N) - 1), monotone=bool(np.all(np.diff(f) >= -1e-12)), max_f2=float((f**2).max()),
                  f_small_r_over_rN=float(f[0]/rr[0]**N))
    print('N=%d' % N, res[N])
ok = all(o['status'] == 0 and abs(o['f_R'] - 1) < 1e-3 and abs(o['a_R'] - 1) < 1e-3 and o['resid'] < 1e-6 and o['flux_rel'] < 1e-3
         and o['E_rel'] < 0.01 and o['monotone'] and o['max_f2'] <= tau + 1e-6 for o in res.values())
print('P2', dict(pass_=ok))
