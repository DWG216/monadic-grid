"""t161: the jump in the written source at writing, against one tick's resolution. Pre-registration: PREDICTIONS_t161.md.
Units G = hbar = m = R0 = 1 for S1; SI for P1."""
import numpy as np
from scipy.special import erf
rng = np.random.default_rng(1610)
K = lambda d: np.where(d > 0, erf(d/2)/np.where(d > 0, d, 1), 1/np.sqrt(np.pi))     # Gaussian-smeared Newton kernel (R0 = 1)
worst, maxdev = 0.0, 0.0
for _ in range(10000):
    d = 10**rng.uniform(-1, 1); pB = rng.random(); pA = 1 - pB
    EG = K(0.0) - K(d)                                   # G m^2 (K(0) - K(d))
    tau = np.pi/EG                                        # pi hbar / E_G
    PhiA_at_A, PhiB_at_A = -K(0.0), -K(d)                 # potentials at branch A's position from each branch
    Phi_mix_at_A = pA*PhiA_at_A + pB*PhiB_at_A
    disc = abs(Phi_mix_at_A - PhiA_at_A)*tau              # phase discrepancy of branch A over tau (m = hbar = 1)
    maxdev = max(maxdev, abs(disc - pB*np.pi)); worst = max(worst, disc)
print('S1', dict(max_dev_from_pB_pi=float(maxdev), max_discrepancy=float(worst), pi=np.pi, pass_=maxdev < 1e-10 and worst <= np.pi))
hbar, g, u = 1.054571817e-34, 9.80665, 1.66053906660e-27
m = 86.909*u; d = 0.5
rate = 0.5*m*g*d/hbar; t_write = np.pi/rate
print('P1', dict(rate_per_s=rate, write_time_s=t_write, observed_coherence_s=1.0, pass_=t_write < 1e-6))
