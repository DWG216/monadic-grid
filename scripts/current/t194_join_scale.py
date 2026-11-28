"""t194: the up chord at mu = v. See PREDICTIONS_t194.md."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(194); N = 100_000
v = 246.22
scales = {"M_Z":91.1876,"M_h":125.10,"M_t":173.1,"1e5":1e5,"1e8":1e8,"1e12":1e12}
up = {"M_Z":[(1.23e-3,.21e-3),(.620,.017),(168.26,.75)],"M_h":[(1.20e-3,.21e-3),(.607,.017),(165.05,.75)],
      "M_t":[(1.18e-3,.20e-3),(.594,.017),(161.98,.75)],"1e5":[(.86e-3,.15e-3),(.435,.013),(123.77,.85)],
      "1e8":[(.69e-3,.12e-3),(.350,.011),(102.49,.89)],"1e12":[(.56e-3,.10e-3),(.283,.009),(85.07,.89)]}
def interp(mu, a, b):
    t = (np.log(mu)-np.log(scales[a]))/(np.log(scales[b])-np.log(scales[a]))
    return [(np.exp((1-t)*np.log(x[0])+t*np.log(y[0])), (1-t)*x[1]+t*y[1]) for x, y in zip(up[a], up[b])]
def Q(m): return m.sum(0)/np.sqrt(m).sum(0)**2
def draw(sec):
    out=[]
    for c,s in sec:
        x=rng.normal(c,s,2*N); out.append(x[x>0][:N])
    return np.array(out)
uv = interp(v, "M_t", "1e5")
print("masses at v (GeV):", [(round(c,6), round(s,6)) for c,s in uv])
q = Q(draw(uv)); z = (q.mean()-8/9)/q.std()
print(f"Q_u(v) = {q.mean():.5f} +- {q.std():.5f}, z = {z:+.2f}")
# P2: Q = 8/9 exactly, fix m_t, m_u; solve for m_c
def mc_from(mu_, mt):
    f = lambda mc: (mu_+mc+mt)/(np.sqrt(mu_)+np.sqrt(mc)+np.sqrt(mt))**2 - 8/9
    return brentq(f, 1e-3, 20.0)
d = draw(uv)
pred = np.array([mc_from(d[0,i], d[2,i]) for i in range(20000)])
zc = (pred.mean()-uv[1][0])/np.hypot(pred.std(), uv[1][1])
print(f"predicted m_c(v) = {pred.mean():.4f} +- {pred.std():.4f} GeV against {uv[1][0]:.4f} +- {uv[1][1]:.4f}, z = {zc:+.2f}")
# S1: band of scales within 1 sigma
band=[]
for lg in np.arange(np.log10(91.1876), 12.01, 0.25):
    mu = 10**lg
    keys=list(scales); 
    for a,b in zip(keys[:-1],keys[1:]):
        if scales[a] <= mu <= scales[b]: sec=interp(mu,a,b); break
    qq=Q(draw(sec)); 
    if abs(qq.mean()-8/9) <= qq.std(): band.append(lg)
print(f"S1: Q_u within 1 sigma of 8/9 for log10(mu/GeV) in [{min(band):.2f}, {max(band):.2f}]")
print()
print("P1 (Q_u(v) within 1 sigma of 8/9):", "PASS" if abs(z) <= 1 else "FAIL")
print("P2 (m_c(v) from Q = 8/9 within 1 sigma):", "PASS" if abs(zc) <= 1 else "FAIL")
