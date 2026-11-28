"""t181: width-to-spacing ratio R = Gamma/omega0 of the ln 3 Hawking line spectrum. Pre-registration: PREDICTIONS_t181.md."""
import numpy as np
a0 = 2.011e-4; fnu, fga, fgr = 0.814, 0.167, 0.019
per_f = a0*fnu/3/2; per_v = a0*fga/2; per_g = a0*fgr/2         # per degree of freedom
Eb, Ef = 2.701, 3.151                                           # mean energy per quantum / T (blackbody)
def R(dof_f, dof_v, dof_g=2, dof_s=0):
    # P = alpha/M^2, T = 1/(8 pi M): Ndot = sum_i alpha_i/(M^2 <E_i>) = sum_i alpha_i 8 pi/(M <E_i>/T); omega0 = ln3/(8 pi M)
    rate = (dof_f*per_f/Ef + dof_v*per_v/Eb + dof_g*per_g/Eb + dof_s*per_f/Eb)*8*np.pi
    return rate/(np.log(3)/(8*np.pi))
low = R(dof_f=6, dof_v=2); high = R(dof_f=90, dof_v=27, dof_s=1)
print('check alpha_low', 6*per_f + 2*per_v + 2*per_g)
print('P1', dict(R_cold=low, pass_=low < 0.1))
print('P2', dict(R_burst=high, pass_=high > 0.3))
print('reported', dict(R_cold_ln2=low*np.log(3)/np.log(2), R_burst_ln2=high*np.log(3)/np.log(2)))
