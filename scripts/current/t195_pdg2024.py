"""t195: counts against PDG 2024 inputs, run with Huang-Zhou's ratios. See PREDICTIONS_t195.md."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(195); N = 20000
# Huang-Zhou inputs (their Sec. 2) and outputs
HZin = dict(u=2.16e-3, d=4.67e-3, s=0.093, c=1.27, b=4.18)           # GeV at 2 GeV / own mass
HZMZ = dict(u=1.23e-3, d=2.67e-3, s=53.16e-3, c=0.620, b=2.839, t=168.26)
HZMt = dict(u=1.18e-3, c=0.594, t=161.98); HZ1e5 = dict(u=0.86e-3, c=0.435, t=123.77)
v = 246.22; tv = (np.log(v)-np.log(173.1))/(np.log(1e5)-np.log(173.1))
at_v = {k: np.exp((1-tv)*np.log(HZMt[k]) + tv*np.log(HZ1e5[k])) for k in HZMt}
# PDG 2024 (1 sigma)
P = dict(u=(2.16e-3,0.04e-3), d=(4.70e-3,0.04e-3), s=(93.5e-3,0.5e-3), c=(1.2730,0.0028), b=(4.183,0.004))
# --- U1: up chord at v
ru_v = at_v["u"]/HZin["u"]; rc_v = at_v["c"]/HZin["c"]
mt_v = rng.normal(at_v["t"], 0.755, N)            # pole input unchanged (172.4(7)); HZ error carried
mu_v = rng.normal(P["u"][0], P["u"][1], N)*ru_v
def mc_from(mu_, mt):
    f = lambda mc: (mu_+mc+mt)/(np.sqrt(mu_)+np.sqrt(mc)+np.sqrt(mt))**2 - 8/9
    return brentq(f, 1e-3, 20.0)
mc_v = np.array([mc_from(a, b) for a, b in zip(mu_v, mt_v)])
mc_mc = mc_v/rc_v
pred, sp = mc_mc.mean(), np.hypot(mc_mc.std(), 0.010*mc_mc.mean())
zU = (pred - P["c"][0])/np.hypot(sp, P["c"][1])
print(f"U1: m_c(v) predicted {mc_v.mean():.4f} GeV; carried: m_c(m_c) = {pred:.4f} +- {sp:.4f} (incl. 1% running) vs {P['c'][0]} +- {P['c'][1]}: z = {zU:+.2f}")
# --- D1: down chord at M_Z
def draw(c, s): x = rng.normal(c, s, 3*N); return x[x > 0][:N]
r = {k: HZMZ[k]/HZin[k] for k in "dsb"}
md = draw(*P["d"])*r["d"]; ms = draw(*P["s"])*r["s"]
mb = draw(*P["b"])*r["b"]*rng.normal(1, 0.005, N)
m = np.array([md, ms, mb]); Qd = m.sum(0)/np.sqrt(m).sum(0)**2
zD = (Qd.mean()-0.75)/Qd.std()
print(f"D1: m(M_Z) d {md.mean()*1e3:.3f} MeV, s {ms.mean()*1e3:.2f} MeV, b {mb.mean():.4f} GeV; Q_d = {Qd.mean():.5f} +- {Qd.std():.5f}: z = {zD:+.2f}")
print()
print("U1:", "PASS" if abs(zU) <= 2 else "FAIL")
print("D1:", "PASS" if abs(zD) <= 2 else "FAIL")
