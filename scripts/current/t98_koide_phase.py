"""t98: Koide's phase from the masses; delta = 2/9 test. Pre-registration: PREDICTIONS_t98.md."""
import numpy as np
rng = np.random.default_rng(98)
def chord(ms):
    s = np.sqrt(np.array(ms, float)); A = s.mean(); x = s/A - 1
    z = (2/3)*sum(x[k]*np.exp(-2j*np.pi*k/3) for k in range(3))
    c, d = abs(z), np.angle(z) % (2*np.pi/3)
    d = min(d, 2*np.pi/3 - d)                                    # fold delta -> -delta
    Q = sum(ms)/s.sum()**2
    return A, c, d, Q
def masses(A, c, d): return np.sort([(A*(1 + c*np.cos(d + 2*np.pi*k/3)))**2 for k in range(3)])
me, mmu, mtau, dtau = 0.51099895000, 105.6583755, 1776.86, 0.12
A, c, d, Q = chord([me, mmu, mtau]); rec = masses(A, c, d)
out = {'S1': dict(rel=float(np.max(np.abs(rec/np.array([me, mmu, mtau]) - 1))), pass_=np.max(np.abs(rec/np.array([me, mmu, mtau]) - 1)) < 1e-9)}
ds = [chord([me, mmu, mtau + dtau*rng.standard_normal()])[2] for _ in range(20000)]; sd = float(np.std(ds))
out['P1'] = dict(delta=d, Q=Q, sigma=sd, pull=(d - 2/9)/sd, pass_=abs(d - 2/9) <= 3*sd)
p = masses(1.0, np.sqrt(2), 2/9); scale = mmu/p[1]; pe, ptau = p[0]*scale, p[2]*scale
out['P2'] = dict(m_e_pred=pe, rel_e=pe/me - 1, m_tau_pred=ptau, pull_tau=(ptau - mtau)/dtau, pass_=abs(pe/me - 1) < 1e-3 and abs(ptau - mtau) <= 3*dtau)
m1 = 0.365e-3; m2 = np.sqrt(m1**2 + 7.50e-5); m3 = 59.16e-3 - m1 - m2
quarks = dict(up=[1.54e-3, 0.599, 169.6], down=[3.1e-3, 0.057, 2.87])
out['info'] = {k: dict(zip(('A', 'c', 'delta', 'Q'), [float(v) for v in chord(ms)])) for k, ms in dict(neutrinos=[m1, m2, m3], **quarks).items()}
for k, v in out.items(): print(k, v)
