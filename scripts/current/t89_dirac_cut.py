"""t89: Dirac neutrino masses from the lepton bifundamental; seesaw; Davidson-Ibarra. Pre-registration: PREDICTIONS_t89.md."""
import math
m1 = 0.365e-12; m2 = math.sqrt(m1**2 + 7.50e-5*1e-18); m3 = 59.16e-12 - m1 - m2     # GeV
mn = [m1, m2, m3]; v = 174.0; M3 = 4.48e13
def seesaw(mD): return [d**2/m for d, m in zip(mD, mn)]
def eta_max(M1, kappa=0.1): return 9.6e-3 * kappa * (3/(16*math.pi)) * M1 * m3 / v**2
M_needed = 6.1e-10 / (9.6e-3 * 0.1 * (3/(16*math.pi)) * m3 / v**2)
out = {}
up = seesaw([2.16e-3, 1.27, 172.57]); out['S1'] = dict(M_R=up, pass_=abs(up[0]/1.3e7-1) < 0.1 and abs(up[2]/5.9e14-1) < 0.1)
lep = seesaw([0.51099895e-3, 0.1056583755, 1.776969]); out['P1'] = dict(M_R=lep, pass_=1e10 <= lep[2] <= 1e11)
out['P2'] = dict(M_R3=lep[2], M3=M3, pass_=lep[2] < M3)
out['P3'] = dict(eta_max_N1=eta_max(lep[0]), pass_=eta_max(lep[0]) < 6.1e-10)
out['P4'] = dict(M_needed=M_needed, M_R3=lep[2], pass_=lep[2] >= M_needed)
for k, x in out.items(): print(k, x)
