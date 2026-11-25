"""t85: the E6 breaking scale at the gravitational meeting; proton lifetimes. Pre-registration: PREDICTIONS_t85.md."""
import numpy as np
SK = 2.4e34; HK = 1e35; YR = 3.156e7; S = 1/6.582e-25; MP = 0.938; MRED = 2.435e18
M3, AINV3 = 4.48e13, 38.76
def tau(M, c): return M**4 / (c**2 * MP**5) / S / YR          # years
def mbound(c, t=SK): return (t*YR*S * c**2 * MP**5)**0.25
def ainv(mu, nh): return AINV3 - (-5 + nh) / (2*np.pi) * np.log(mu / M3)
out = {}
out['S1'] = dict(M=mbound(1/42.4), pass_=abs(mbound(1/42.4)/4.64e15 - 1) < 0.01)
g1 = {nh: ainv(MRED, nh) for nh in range(4)}; out['G1'] = dict(alpha_inv_at_Mred=g1, pass_=all(v > 1 for v in g1.values()))
g2 = {nh: tau(MRED, 1/g1[nh]) for nh in range(4)}; out['G2'] = dict(tau_yr=g2, pass_=all(v > 1e40 for v in g2.values()))
v = 246.0; yu, yd = np.sqrt(2)*2.16e-3/v, np.sqrt(2)*4.67e-3/v; c = yu*yd
lo, hi = tau(5.6e11, c), tau(7.5e13, c); reach = mbound(c, HK)
out['G3'] = dict(tau_low=lo, tau_high=hi, hyperK_reach_mass=reach, pass_=lo > SK and hi > HK)
out['C1'] = dict(tau=tau(M3, 1/AINV3), pass_=tau(M3, 1/AINV3) < SK)
t2 = tau(2e16, 1/40.0); out['C2'] = dict(tau=t2, pass_=1e35 < t2 < 1e40)
for k, x in out.items(): print(k, x)
