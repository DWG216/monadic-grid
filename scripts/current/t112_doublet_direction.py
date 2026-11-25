"""t112: the light doublet's direction and b/tau from the E6 cubic norm. Pre-registration: PREDICTIONS_t112.md."""
import numpy as np, itertools
eps = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)): eps[p] = np.linalg.det(np.eye(3)[list(p)])
# field index: L[i,a] -> 0..8, QL[al,i] -> 9..17, QR[a,al] -> 18..26
iL = lambda i, a: 3*i + a; iQL = lambda al, i: 9 + 3*al + i; iQR = lambda a, al: 18 + 3*a + al
def hessian(W):
    M = np.zeros((27, 27))
    for i, j, a, b in itertools.product(range(3), repeat=4):
        M[iL(i, a), iL(j, b)] = sum(eps[i, j, k]*eps[a, b, c]*W[k, c] for k in range(3) for c in range(3))
    for al, i, a in itertools.product(range(3), repeat=3):
        M[iQL(al, i), iQR(a, al)] = M[iQR(a, al), iQL(al, i)] = -W[i, a]
    return M
t3 = np.array([.5, -.5, 0]); t8 = np.array([1, 1, -2])/(2*np.sqrt(3))
# Y = a t8_L + b t3_R + c t8_R; unbroken on L[2,2] and L[2,1] (rows/cols 0-based: the t106 vevs H1_33, H2_32); q doublet Y = 1/6
A = np.array([[t8[2], -t3[2], -t8[2]], [t8[2], -t3[1], -t8[1]], [-t8[0], 0, 0]]); a, b, c = np.linalg.solve(A, [0, 0, 1/6])
gL, gR = a*t8, b*t3 + c*t8
Y = np.zeros(27); T3 = np.zeros(27)
for i, a_ in itertools.product(range(3), repeat=2):
    Y[iL(i, a_)] = gL[i] - gR[a_]; T3[iL(i, a_)] = t3[i]
    for al in range(3): Y[iQL(al, i)] = -gL[i]; T3[iQL(al, i)] = -t3[i]; Y[iQR(a_, al)] = gR[a_]
Q = T3 + Y
neutral_dn = [(i, a_) for i in range(2) for a_ in range(3) if abs(Q[iL(i, a_)]) < 1e-12 and abs(Y[iL(i, a_)] + .5) < 1e-12]
neutral_up = [(i, a_) for i in range(2) for a_ in range(3) if abs(Q[iL(i, a_)]) < 1e-12 and abs(Y[iL(i, a_)] - .5) < 1e-12]
print('Y(L) =\n', np.round(Y[:9].reshape(3, 3), 4), '\nQ(L) =\n', np.round(Q[:9].reshape(3, 3), 4))
print('neutral down-type doublet entries', neutral_dn, ' up-type', neutral_up)
def masses(x, t, kap=1e-10, ku=0.0):
    W = np.zeros((3, 3)); W[2, 2] = 1.0; W[2, 1] = t
    (i2, a2), (i3, a3) = sorted(neutral_dn, key=lambda e: e[1])[:2] if True else None
    W[i2, a2] = kap; W[i3, a3] = x*kap
    if neutral_up: W[neutral_up[0]] = ku*kap
    M = hessian(W); out = {}
    for name, q, sel in [('b', -1/3, lambda k: 9 <= k < 12 or 18 <= k < 27 and (k - 18) % 3 == 0), ('tau', -1, lambda k: k < 9)]:
        rows = [k for k in range(27) if abs(Q[k] - q) < 1e-9 and sel(k)]; cols = [k for k in range(27) if abs(Q[k] + q) < 1e-9 and sel(k)]
        sv = np.linalg.svd(M[np.ix_(rows, cols)], compute_uv=False); out[name] = sv
    return out
out = {}
m = masses(0, 0); out['S1'] = dict(ratio=m['b'][-1]/m['tau'][-1], sv_b=m['b'], sv_tau=m['tau'], pass_=abs(m['b'][-1]/m['tau'][-1] - 1) < 1e-6)
m = masses(0, 1); out['S2'] = dict(sv_b=m['b'], sv_tau=m['tau'], pass_=m['b'][-2]/m['b'][-1] > 1e6 and m['tau'][-2]/m['tau'][-1] > 1e6)
r = lambda x, t: (lambda m: m['b'][-1]/m['tau'][-1])(masses(x, t))
out['P1'] = dict(ratio=r(0, 1), pass_=0.537 <= r(0, 1) <= 0.657)
ts = np.logspace(-1, 1, 41); rs = np.array([r(0, t) for t in ts])
hit = [float(ts[k]) for k in range(len(ts)-1) if (rs[k]-0.597)*(rs[k+1]-0.597) < 0]
out['P2'] = dict(min=rs.min(), max=rs.max(), t_star=hit, pass_=(rs.max()-rs.min())/rs.mean() < 0.01 or bool(hit))
out['P3'] = dict(ratio=r(1, 1), pass_=0.537 <= r(1, 1) <= 0.657)
grid = {f'x={x},t={t}': round(r(x, t), 4) for x in (0, 0.25, 0.5, 1, 2) for t in (0.1, 1, 10)}
out['info'] = dict(grid=grid, R1_t1_with_ku50=(lambda m: m['b'][-1]/m['tau'][-1])(masses(0, 1, ku=50)))
for k_, v in out.items(): print(k_, v)
