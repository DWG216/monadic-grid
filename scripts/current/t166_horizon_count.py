"""t166: the 1/4 from a count of cells (horizon molecules on the Planck-density grain, 16 states per pair).
Pre-registration: PREDICTIONS_t166.md. Units rho = 1; Rindler horizon t = x; Sigma: t = 0."""
import numpy as np
from scipy.integrate import quad

def vcap(r, c):
    if c >= r: return 4*np.pi*r**3/3
    if c <= -r: return 0.0
    return np.pi*(r*r*c - c**3/3 + 2*r**3/3)

def VB(h, x0, eps=1e-10):
    return quad(lambda t: vcap(t + h, t - x0), -h, 0, epsabs=eps, epsrel=eps, limit=200)[0]

def a4(eps=1e-10):
    inner = lambda h: quad(lambda x0: VB(h, x0, eps), -h, h, epsabs=eps, epsrel=eps, limit=200)[0]*np.exp(-np.pi*h**4/3)
    return quad(inner, 0, 4.0, epsabs=eps, epsrel=eps, limit=200)[0]

out = {}
A1, A2 = a4(1e-8), a4(1e-11)
out['S1'] = dict(a4=A2, a4_loose=A1, rel=abs(A1/A2 - 1), pass_=abs(A1/A2 - 1) < 1e-6)

rng = np.random.default_rng(1660)
T, X, m, Lc = 2.5, 5.5, 2.5, 4.0; Lt = 2*m + Lc
counts = []
for _ in range(40):
    n = rng.poisson(T*2*X*Lt*Lt)
    P = np.column_stack([-T*rng.random(n), -X + 2*X*rng.random(n), Lt*rng.random(n), Lt*rng.random(n)])
    cand = np.where((P[:, 2] > m) & (P[:, 2] < m + Lc) & (P[:, 3] > m) & (P[:, 3] < m + Lc) & (P[:, 1] > P[:, 0]))[0]
    c = 0
    for i in cand:
        dt = P[:, 0] - P[i, 0]; dx = P[:, 1:] - P[i, 1:]
        fut = (dt > 0) & (dt*dt > (dx*dx).sum(1))
        if fut.sum() == 1:
            j = np.where(fut)[0][0]
            if P[j, 0] > P[j, 1]: c += 1
    counts.append(c/(Lc*Lc))
counts = np.array(counts); mc, se = counts.mean(), counts.std(ddof=1)/np.sqrt(len(counts))
out['S2'] = dict(mc_per_area=mc, se=se, a4=A2, z=(mc - A2)/se, pass_=abs(mc - A2) < 3*se)
coef16 = A2*np.log(16)
out['P1'] = dict(a4_ln16=coef16, target=0.25, ratio=coef16/0.25, pass_=abs(coef16/0.25 - 1) < 0.10)
out['reported'] = dict(a4_ln2=A2*np.log(2), states_for_quarter=float(np.exp(0.25/A2)))
for k, v in out.items(): print(k, v)
