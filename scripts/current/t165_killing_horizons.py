"""t165: Rindler and de Sitter horizon decoherence (DSW) against the record's rate. Pre-registration: PREDICTIONS_t165.md."""
import numpy as np
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
g0 = 9.80665; Mmoon, Rmoon = 7.342e22, 1.7374e6
def EG(m, R, d):
    lam = d/(2*R)
    return G*m**2/R*(2*lam**2 - 1.5*lam**3 + lam**5/5) if lam <= 1 else G*m**2*(6/(5*R) - 1/d)   # t146 closed form
T_rind = lambda m, d, a: hbar*c**10/(G*m**2*d**4*a**5)
T_ds = lambda m, d, RH: hbar*RH**5/(G*m**2*d**4)
out = {}
s1 = T_rind(Mmoon, Rmoon, g0)
out['S1'] = dict(T_D_s=s1, paper_s=2e-15, pass_=2e-15/3 < s1 < 6e-15)
m, rho, d = 1e-14, 3500.0, 250e-6; R = (3*m/(4*np.pi*rho))**(1/3); E = EG(m, R, d); Trec = hbar/E
astar = (c**10*E/(G*m**2*d**4))**0.2
out['P1'] = dict(T_record_s=Trec, a_star=astar, a_star_over_g=astar/g0, pass_=1e21/3 < astar < 3e21)
ratio_moon = T_rind(Mmoon, Rmoon, g0)/(hbar/EG(Mmoon, Rmoon, Rmoon))
out['P2'] = dict(record_faster_by=ratio_moon, pass_=ratio_moon > 1e40)
H0 = 67.4e3/3.0857e22; RH = c/H0
ratio_ds = T_ds(m, d, RH)/Trec
out['P3'] = dict(R_H_m=RH, record_faster_by=ratio_ds, pass_=ratio_ds > 1e140)
for k, v in out.items(): print(k, v)
