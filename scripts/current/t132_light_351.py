"""t132 (enumeration; see PREDICTIONS_t132.md). Two-zero texture with the 351's quark-only antisymmetric weight x on the 1-2 entries."""
import numpy as np, itertools
from scipy.optimize import brentq
r = {'cubic': -1.0, 'orth': 2/3, 'both': 1/4}; data = {'s/mu': 0.231, 'd/e': 2.44}
c, a, b = 0.06, 0.008, 1.0
def ratios(r22, r12, x):
    Md = np.array([[0, (r12 + x)*a, 0], [(r12 - x)*a, r22*c, 0], [0, 0, 2/3*b]]); Me = np.array([[0, a, 0], [a, c, 0], [0, 0, b]])
    sd, se = np.sort(np.linalg.svd(Md, compute_uv=False)), np.sort(np.linalg.svd(Me, compute_uv=False)); return sd[1]/se[1], sd[0]/se[0]
for k22, k12 in itertools.product(r, r):
    sm = ratios(r[k22], r[k12], 0)[0]
    lo = abs(r[k12]**2)/abs(r[k22])
    f = lambda x: ratios(r[k22], r[k12], x)[1] - data['d/e']
    xs = np.linspace(0, 3, 3001); v = np.array([f(x) for x in xs]); roots = [brentq(f, xs[i], xs[i+1]) for i in range(len(xs)-1) if np.sign(v[i]) != np.sign(v[i+1])]
    simple = {x0: ratios(r[k22], r[k12], x0)[1] for x0 in (0, .5, 2/3, 1)}
    hits = [x0 for x0, de in simple.items() if abs(de/data['d/e'] - 1) < .1]
    print(f'2-2 {k22:5s} 1-2 {k12:5s}  s/mu {sm:.3f} ({sm/data["s/mu"]-1:+.0%})  x needed {", ".join(f"{q:.3f}" for q in roots) or "none"}  d/e at x=0,1/2,2/3,1: ' + ', '.join(f'{v_:.2f}' for v_ in simple.values()) + f'  simple x within 10%: {hits}')
# leading-order check
sm, de = ratios(0.25, 2/3, 1.0); print('check both/orth x=1: exact d/e', round(de, 3), 'leading', round(abs((2/3)**2 - 1)/0.25, 3))
