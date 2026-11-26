"""t158: the record's links as the covariant decoherence kernel. Pre-registration: PREDICTIONS_t158.md. Units rho = 1 (grain)."""
import numpy as np
from scipy.integrate import quad
rho = 1.0; a = rho*np.pi/24                      # link probability exp(-rho * pi tau^4 / 24)
out = {}

# S1: time integral of 2 delta(t^2 - r^2), Gaussian-regularised in w = t^2 - r^2 (width eps)
eps = 1e-4
def S1(r):
    g = lambda t: 2*np.exp(-((t*t - r*r)/eps)**2/2)/(eps*np.sqrt(2*np.pi))
    return sum(quad(g, c - 50*eps/r, c + 50*eps/r, limit=200, points=[c])[0] for c in (-r, r))
s1 = {r: S1(r)*r for r in (1.0, 3.0, 10.0)}
out['S1'] = dict(r_times_integral=s1, pass_=all(abs(v - 1) < 1e-3 for v in s1.values()))

# P1: I(s) and the Johnston normalisation
def I(s):
    f = lambda w: np.exp(-a*w*w)/(2*np.sqrt(w + s*s))
    if s > 0: return quad(f, 0, np.inf, limit=400)[0]
    return quad(lambda u: np.exp(-a*u**4), 0, np.inf, limit=400)[0]   # s = 0: w = u^2, dw/(2 sqrt w) = du
ratio20 = 2*20*I(20.0)/np.sqrt(6)
ss = np.geomspace(10, 100, 12); Is = np.array([I(s) for s in ss])
power = np.polyfit(np.log(ss), np.log(Is), 1)[0]
out['P1'] = dict(ratio_at_20=ratio20, power=power, pass_=abs(ratio20 - 1) < 0.02 and abs(power + 1) < 0.02)

# P2: two point blobs moving together; link density per unit proper time vs rest
def J(eta, orient, r=20.0):
    v = np.tanh(eta); g = np.cosh(eta)
    rl = np.array([0.0, r, 0.0]) if orient == 'perp' else np.array([r/g, 0.0, 0.0])
    vv = np.array([v, 0.0, 0.0])
    def tau2(t): d = rl + vv*t; return t*t - d @ d
    def f(t):
        t2 = tau2(t); return np.exp(-a*t2*t2) if t2 > 0 else 0.0
    # light-cone crossings: t^2 - |rl + v t|^2 = 0
    A = 1 - v*v; B = -2*v*rl[0]; C = -(rl @ rl); disc = np.sqrt(B*B - 4*A*C)
    roots = sorted([(-B - disc)/(2*A), (-B + disc)/(2*A)])
    tot = 0.0
    for rt, sgn in ((roots[1], 1), (roots[0], -1)):
        lo, hi = (rt, rt + 60) if sgn > 0 else (rt - 60, rt)
        tot += quad(f, lo, hi, limit=400, points=[rt])[0]
    return tot
J0 = J(0.0, 'perp')
p2 = {}
for eta in (0.5, 1.0):
    g = np.cosh(eta)
    for o in ('perp', 'par'):
        p2[f'eta{eta}_{o}'] = J(eta, o)/(g*J0)          # cells per proper time: (V/g)^2 rho^2 J g / (V^2 rho^2 J0) -> J/(g J0)
newton = {f'eta1.0_{o}': (np.cosh(1.0) if o == 'perp' else np.cosh(1.0)**2) for o in ('perp', 'par')}
out['P2'] = dict(links=p2, newtonian=newton,
                 pass_=all(abs(v - 1) < 0.03 for v in p2.values()) and all(abs(v - 1) > 0.10 for v in newton.values()))

# P3: the link kernel at zero separation
k0 = I(0.0)*2/np.sqrt(6)
R_link = 1/(np.sqrt(np.pi)*k0)
lP = 1.616255e-35; grain = 3.33*lP
out['P3'] = dict(k0=k0, R_link_grain_units=R_link, R_link_m=R_link*grain, gran_sasso_m=0.54e-10,
                 orders_short=float(np.log10(0.54e-10/(R_link*grain))), pass_=R_link*grain < 0.54e-10)
for k, v in out.items(): print(k, v)
