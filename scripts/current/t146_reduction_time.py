"""t146: the reduction time tau = pi hbar / E_G. Pre-registration: PREDICTIONS_t146.md."""
import numpy as np
from scipy.integrate import quad
hbar, G = 1.054571817e-34, 6.67430e-11
# P1: two-branch orthogonalisation and the speed limit
EG = 1.0; t = np.linspace(0, 2*np.pi, 2_000_001)
ov = np.abs(0.5*(1 + np.exp(-1j*EG*t)))                        # |<psi0|psi_t>| for equal weights across a gap E_G (hbar = 1)
t0 = t[np.argmax(ov < 1e-6)]
from scipy.optimize import brentq
tz = brentq(lambda s: np.cos(EG*s/2), 0.5, 4.0)                 # |overlap| = |cos(E_G t / 2)|
err1 = abs(tz - np.pi/EG)/(np.pi/EG)
rng = np.random.default_rng(1460); beaten = 0; met = 0
for _ in range(10_000):
    n = rng.integers(2, 9); E = rng.uniform(0, 1, n); c = rng.dirichlet(np.ones(n))
    if rng.random() < 0.1: n, E, c = 2, np.array([0.0, rng.uniform(0.1, 1)]), np.array([0.5, 0.5])
    dE = np.sqrt(c@E**2 - (c@E)**2); tb = np.pi/(2*dE)
    ts = np.linspace(0, tb, 4001)[:-1]
    ovl = np.abs(np.exp(-1j*np.outer(ts, E))@c)
    if ovl.min() < 1e-9: beaten += 1
    tt = np.linspace(0, tb*1.000001, 4001); o2 = np.abs(np.exp(-1j*np.outer(tt, E))@c)
    if o2.min() < 1e-5: met += 1
print(f'P1 two-branch zero at t*E_G/hbar = {tz:.12f} (pi = {np.pi:.12f}), rel err {err1:.1e}; random states beating the bound: {beaten} / 10000; meeting it: {met}')
P1 = err1 < 1e-9 and beaten == 0
# P2: E_G for a uniform sphere, closed form against an independent Fourier integral
def EG_closed(m, R, d):
    lam = d/(2*R)
    return G*m**2/R*(2*lam**2 - 1.5*lam**3 + lam**5/5) if lam <= 1 else G*m**2*(6/(5*R) - 1/d)
def EG_fourier(m, R, d):
    f = lambda k: (m*3*(np.sin(k*R) - k*R*np.cos(k*R))/(k*R)**3)**2*(1 - np.sinc(k*d/np.pi))
    val = sum(quad(f, a, a + 2*np.pi/R, limit=200)[0] for a in np.arange(0, 400*2*np.pi/R, 2*np.pi/R))
    return 2*G/np.pi*val
m, R = 1.0, 1.0
join = abs(G*m**2/R*(2 - 1.5 + 0.2) - G*m**2*(6/(5*R) - 1/(2*R)))/(G*m**2/R)
devs = {lam: abs(EG_fourier(m, R, 2*R*lam)/EG_closed(m, R, 2*R*lam) - 1) for lam in (0.25, 0.5, 1.0)}
print('P2 join at d = 2R:', f'{join:.1e}', '| Fourier vs closed:', {k: f'{v:.2e}' for k, v in devs.items()})
P2 = join < 1e-12 and max(devs.values()) < 0.01
print('P1 pass:', P1, '| P2 pass:', P2)
# Reported: benchmarks
for name, mm, rho, d in [('1e-14 kg, displaced by its diameter', 1e-14, 2000, None), ('1e-17 kg, by its diameter', 1e-17, 2000, None),
                         ('1 ug at 0.1 nm', 1e-9, 2000, 1e-10)]:
    RR = (3*mm/(4*np.pi*rho))**(1/3); dd = 2*RR if d is None else d; E = EG_closed(mm, RR, dd)
    print(f'{name:38s} R = {RR:.2e} m  E_G = {E:.2e} J  hbar/E_G = {hbar/E:.3g} s  tau = pi hbar/E_G = {np.pi*hbar/E:.3g} s')
