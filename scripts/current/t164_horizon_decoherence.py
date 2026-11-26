"""t164: horizon decoherence (Danielson-Satishchandran-Wald) against the record's rate. Pre-registration: PREDICTIONS_t164.md."""
import numpy as np
from scipy.optimize import brentq
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
Msun, au, Mearth, Rearth = 1.98892e30, 1.495978707e11, 5.9722e24, 6.371e6
T_dsw = lambda m, d, M, b: hbar*c**10*b**10/(G**6*M**5*m**2*d**4)
s1 = T_dsw(Mearth, Rearth, Msun, au)
out = {'S1': dict(T_D_s=s1, paper_s=1e-5, pass_=1e-5/3 < s1 < 3e-5)}
m, rho, d = 1e-14, 3500.0, 250e-6
R = (3*m/(4*np.pi*rho))**(1/3); EG = G*m**2*(6/(5*R) - 1/d)
T_grid = lambda k=1.0: hbar/(k*EG)                                       # total record decoherence E_G/hbar ... 1.10 E_G/hbar
ratio = lambda M: T_dsw(m, d, M, 6*G*M/c**2)/T_grid()
Mstar = brentq(lambda lM: np.log(ratio(10**lM)), 10, 40); Mstar = 10**Mstar
out['P1'] = dict(T_grid_s=T_grid(), T_grid_fast_s=T_grid(1.1036), M_star_kg=Mstar, pass_=4e21/2 < Mstar < 4e21*2)
r_sun = ratio(Msun)
out['P2'] = dict(ratio_at_1Msun_6rg=r_sun, ratio_grows_with_M=bool(ratio(10*Msun) > r_sun), pass_=r_sun > 1e20 and ratio(10*Msun) > r_sun)
for k, v in out.items(): print(k, v)
