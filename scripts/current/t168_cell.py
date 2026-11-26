"""t168: one cell size for the horizon's 1/4 and for Lambda. Pre-registration: PREDICTIONS_t168.md."""
import numpy as np
from scipy.integrate import quad
c, hbar, G = 2.99792458e8, 1.054571817e-34, 6.67430e-11
lP = np.sqrt(hbar*G/c**3); tP = lP/c
H0 = 67.4e3/3.0856775814913673e22; Om, OL, Orad = 0.315, 0.685, 9.1e-5
Om_eff = 1 - OL - Orad
H = lambda a: H0*np.sqrt(Orad/a**4 + Om_eff/a**3 + OL)
chi = lambda a: quad(lambda x: c/(x*x*H(x)), a, 1, limit=400)[0]
V4 = (4*np.pi/3)*quad(lambda a: a**2*chi(a)**3/H(a), 1e-12, 1, limit=400, points=[1e-4, 1e-2, 0.1, 0.5])[0]
V4P = V4/(lP**3*tP)
obs = 3*OL*H0**2/c**2*lP**2
a4 = np.sqrt(3)/10; vc = (4*a4*np.log(16))**2
pred = np.sqrt(vc/V4P); pred1 = np.sqrt(1/V4P); vc_exact = (obs**2)*V4P
t0 = quad(lambda a: 1/(a*H(a)), 1e-12, 1, limit=400)[0]
print('ages', dict(t0_Gyr=t0/3.15576e16, V4_m3s=V4, V4_planck=V4P, crude_H0tP4=(1/(H0*tP))**4))
print('P1', dict(v_c=vc, Lambda_lP2_pred=pred, observed=obs, ratio=pred/obs, pass_=abs(pred/obs - 1) < 0.15))
print('reported', dict(planck_cell_pred=pred1, planck_cell_ratio=pred1/obs, exact_cell=vc_exact))
