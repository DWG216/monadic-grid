"""t100: lambda(M*) = 0 -> m_h, SM two-loop running. Pre-registration: PREDICTIONS_t100.md."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
k = 1/(16*np.pi**2)
def beta(t, y):
    g1, g2, g3, yt, l = y
    b1 = k*41/6*g1**3 + k**2*g1**3*(199/18*g1**2 + 9/2*g2**2 + 44/3*g3**2 - 17/6*yt**2)
    b2 = -k*19/6*g2**3 + k**2*g2**3*(3/2*g1**2 + 35/6*g2**2 + 12*g3**2 - 3/2*yt**2)
    b3 = -k*7*g3**3 + k**2*g3**3*(11/6*g1**2 + 9/2*g2**2 - 26*g3**2 - 2*yt**2)
    byt = k*yt*(9/2*yt**2 - 17/12*g1**2 - 9/4*g2**2 - 8*g3**2) + k**2*yt*(-12*yt**4 + yt**2*(131/16*g1**2 + 225/16*g2**2 + 36*g3**2 - 12*l)
          + 1187/216*g1**4 - 3/4*g1**2*g2**2 + 19/9*g1**2*g3**2 - 23/4*g2**4 + 9*g2**2*g3**2 - 108*g3**4 + 6*l**2)
    bl = k*(24*l**2 - 6*yt**4 + 12*l*yt**2 - 3*l*(g1**2 + 3*g2**2) + 3/8*(2*g2**4 + (g1**2 + g2**2)**2)) + k**2*(
          -312*l**3 - 144*l**2*yt**2 + 36*l**2*(3*g2**2 + g1**2) - 3*l*yt**4 + l*yt**2*(80*g3**2 + 45/2*g2**2 + 85/6*g1**2)
          - 73/8*l*g2**4 + 39/4*l*g1**2*g2**2 + 629/24*l*g1**4 + 30*yt**6 - 32*g3**2*yt**4 - 8/3*g1**2*yt**4 - 9/4*g2**4*yt**2
          + 21/2*g1**2*g2**2*yt**2 - 19/4*g1**4*yt**2 + 305/16*g2**6 - 289/48*g1**2*g2**4 - 559/48*g1**4*g2**2 - 379/48*g1**6)
    return [b1, b2, b3, byt, bl]
def lam_mt(mh, Mt): return 0.12604 + 0.00206*(mh - 125.15) - 0.00004*(Mt - 173.34)
def run(mh, Mt, mu):
    y0 = [0.35830, 0.64779, 1.1666, 0.93690 + 0.00556*(Mt - 173.34), lam_mt(mh, Mt)]
    s = solve_ivp(beta, [np.log(Mt), np.log(mu)], y0, rtol=1e-10, atol=1e-12, dense_output=True); return s
out = {}
s = run(125.20, 173.34, 1.22e19); lpl = s.y[4, -1]
ts = np.linspace(np.log(173.34), np.log(1.22e19), 4000); ls = s.sol(ts)[4]; cross = float(np.exp(ts[np.argmax(ls < 0)])) if (ls < 0).any() else None
out['S1'] = dict(lambda_MPl=float(lpl), crossing_GeV=cross, pass_=-0.020 <= lpl <= -0.008 and cross is not None and 1e9 <= cross <= 1e12)
Mstar = 2.435e18
def mh_pred(Mt): return brentq(lambda mh: run(mh, Mt, Mstar).y[4, -1], 100, 160)
mc = mh_pred(172.57)
out['P1'] = dict(mh_pred=mc, measured=125.20, diff=mc - 125.20, pass_=abs(mc - 125.20) <= 2.0)
band = [mh_pred(172.57 + d) for d in (-0.58, 0.58)]
Mt_needed = brentq(lambda Mt: mh_pred(Mt) - 125.20, 160, 180)
out['info'] = dict(mh_band_2sigma_Mt=band, Mt_for_125p2=Mt_needed)
for k_, v in out.items(): print(k_, v)
