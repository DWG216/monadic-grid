"""t175: classical Dobrushin thresholds for SU(2) Wilson lattice gauge theory and for the grain's binary groups 2T, 2O, 2I.
Pre-registration: PREDICTIONS_t175.md."""
import numpy as np
from scipy.optimize import minimize
from scipy.special import eval_chebyu, i1, ive
rng = np.random.default_rng(1750)

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
def key(q): return tuple(np.round(q, 9) + 0.0)
def closure(gens):
    G = {key(np.array([1., 0, 0, 0])): np.array([1., 0, 0, 0])}; fr = list(G.values())
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h); k = key(p)
                if k not in G: G[k] = p; new.append(p)
        fr = new
    return np.array(list(G.values()))
phi = (1 + 5**0.5)/2
GROUPS = {'2T': closure([np.array([0., 1, 0, 0]), np.array([.5, .5, .5, .5])]),
          '2O': closure([np.array([2**-.5, 2**-.5, 0, 0]), np.array([.5, .5, .5, .5])]),
          '2I': closure([np.array([.5, .5, .5, .5]), np.array([phi/2, 1/(2*phi), .5, 0])])}
def conj(q): return q*np.array([1, -1, -1, -1])

def design_strength(G, tmax=30):
    gram = np.clip(G @ G.T, -1, 1)
    for k in range(1, tmax + 1):
        if abs(eval_chebyu(k, gram).mean()) > 1e-12: return k - 1
    return tmax

def class_reps(G):
    seen, reps = set(), []
    for v in G:
        if key(v) in seen: continue
        orb = {key(qmul(qmul(g, v), conj(g))) for g in G}; seen |= orb; reps.append(v)
    return reps

def tv_finite(G, beta, a, b):
    la, lb = beta*(G @ a), beta*(G @ b)
    pa = np.exp(la - la.max()); pa /= pa.sum(); pb = np.exp(lb - lb.max()); pb /= pb.sum()
    return 0.5*np.abs(pa - pb).sum()

# SU(2): uniform S^3 projected to a 2-plane is uniform on the unit disk
gr, gw = np.polynomial.legendre.leggauss(160); rr = 0.5*(gr + 1); wr = 0.5*gw
th = np.linspace(0, 2*np.pi, 512, endpoint=False)
R, TH = np.meshgrid(rr, th, indexing='ij'); W = (wr[:, None]*R)*(2*np.pi/len(th))/np.pi   # area weights / pi
Y1, Y2 = R*np.cos(TH), R*np.sin(TH)
def tv_su2(beta, a, b):
    e1 = a/np.linalg.norm(a) if np.linalg.norm(a) > 1e-12 else np.array([1., 0, 0, 0])
    bp = b - (b @ e1)*e1
    e2 = bp/np.linalg.norm(bp) if np.linalg.norm(bp) > 1e-12 else np.linalg.svd(np.vstack([e1]))[2][1]
    def dens(x):
        c1, c2 = beta*(x @ e1), beta*(x @ e2); c = np.hypot(c1, c2)
        Z = 1.0 if c < 1e-12 else 2*ive(1, c)/c                        # mean of exp(c y1) on the disk, scaled by e^{-c}
        return np.exp(c1*Y1 + c2*Y2 - c)/Z
    return 0.5*np.sum(W*np.abs(dens(a) - dens(b)))

def wmap(z):
    n = np.linalg.norm(z); return z if n < 1e-15 else 5*np.tanh(n)*z/n

def C_finite(G, beta, starts=6):
    best = 0.0; one = np.array([1., 0, 0, 0])
    for v2 in class_reps(G):
        if np.allclose(v2, one): continue
        f = lambda z: -tv_finite(G, beta, wmap(z) + one, wmap(z) + v2)
        for s in range(starts):
            z0 = rng.normal(size=4)*(0.3 if s else 0.0)
            r = minimize(f, z0, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=2000))
            best = max(best, -r.fun)
    return best

def C_su2(beta, starts=8):
    best = 0.0; one = np.array([1., 0, 0, 0])
    def f(p):
        t = p[0]; v2 = np.array([np.cos(t), np.sin(t), 0, 0]); w = wmap(p[1:])
        return -tv_su2(beta, w + one, w + v2)
    for s in range(starts):
        p0 = np.concatenate([[np.pi - (0 if s == 0 else rng.uniform(0, 1))], rng.normal(size=4)*(0.3 if s else 0.0)])
        r = minimize(f, p0, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=3000))
        best = max(best, -r.fun)
    return best

def threshold(Cfun, lo=0.02, hi=1.0, it=28):
    for _ in range(it):
        mid = 0.5*(lo + hi)
        if 18*Cfun(mid) < 1: lo = mid
        else: hi = mid
    return 0.5*(lo + hi)

out = {}
cs = 4/(3*np.pi)
for name, G in GROUPS.items():
    t = design_strength(G); c = np.abs(G[:, 0]).mean()
    small = C_finite(G, 1e-3)/1e-3
    bstar = threshold(lambda b: C_finite(G, b))
    out[name] = dict(order=len(G), design=t, c=c, small_ratio_err=abs(small/c - 1), beta_star=bstar)
    print(name, out[name], flush=True)
small = C_su2(1e-3)/1e-3; bstar = threshold(C_su2)
out['SU2'] = dict(c=cs, small_ratio_err=abs(small/cs - 1), beta_star=bstar)
print('SU2', out['SU2'], flush=True)

P1 = all(o['small_ratio_err'] < 1e-3 for o in out.values())
print('P1', dict(designs={g: out[g]['design'] for g in GROUPS}, pass_=P1))
order = sorted(GROUPS, key=lambda g: out[g]['design'])
dev = {g: abs(out[g]['beta_star']/out['SU2']['beta_star'] - 1) for g in GROUPS}
P2 = all(dev[order[i]] > dev[order[i + 1]] for i in range(len(order) - 1)) and dev['2I'] < 0.02
print('P2', dict(beta_star={g: out[g]['beta_star'] for g in out}, deviation=dev, pass_=P2))
devc = {g: abs(out[g]['c']/cs - 1) for g in GROUPS}
P3 = all(devc[order[i]] > devc[order[i + 1]] for i in range(len(order) - 1))
print('P3', dict(c={g: out[g]['c'] for g in out}, deviation=devc, pass_=P3))
