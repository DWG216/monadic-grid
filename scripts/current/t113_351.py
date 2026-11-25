"""t113: the 351' half of the record and b/tau. Pre-registration: PREDICTIONS_t113.md."""
import numpy as np, itertools, contextlib, io
src = open(__file__.replace('t113_351.py', 't112_doublet_direction.py')).read(); ns = {'__file__': __file__}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index('\nout = {}')], ns)
eps, iL, iQL, iQR, Q, hessian = ns['eps'], ns['iL'], ns['iQL'], ns['iQR'], ns['Q'], ns['hessian']
def tensors(W):
    lep = np.zeros((27, 27)); qk = np.zeros((27, 27))
    for i, j, a, b in itertools.product(range(3), repeat=4):
        lep[iL(i, a), iL(j, b)] = sum(eps[i, j, k]*eps[a, b, c]*W[k, c] for k in range(3) for c in range(3))
    for al, i, a in itertools.product(range(3), repeat=3):
        qk[iQL(al, i), iQR(a, al)] = qk[iQR(a, al), iQL(al, i)] = W[i, a]
    return lep, qk
def h351(W): lep, qk = tensors(W); return 3*lep + 2*qk
def masses(t, kap=1e-10):
    Wh = np.zeros((3, 3)); Wh[2, 2] = 1.0; Wh[2, 1] = t
    Wl = np.zeros((3, 3)); Wl[0, 1] = kap
    M = hessian(Wh) + h351(Wl); out = {}
    for name, q, sel in [('b', -1/3, lambda k: 9 <= k < 12 or 18 <= k < 27 and (k - 18) % 3 == 0), ('tau', -1, lambda k: k < 9)]:
        rows = [k for k in range(27) if abs(Q[k] - q) < 1e-9 and sel(k)]; cols = [k for k in range(27) if abs(Q[k] + q) < 1e-9 and sel(k)]
        out[name] = np.linalg.svd(M[np.ix_(rows, cols)], compute_uv=False)
    return out
ratio = lambda t: (lambda m: m['b'][-1]/m['tau'][-1])(masses(t))
out = {}
W1 = np.zeros((3, 3)); W1[0, 1] = 1; l, q = tensors(W1)
ip = float(np.sum(l*(3*l + 2*q)*0) + np.sum((l - q)*(3*l + 2*q)))
out['S1'] = dict(inner_27_351=ip, ratio_t0=ratio(0), pass_=abs(ip) < 1e-12 and abs(ratio(0) - 2/3) < 1e-6)
out['P1'] = dict(ratio=ratio(0), dev=ratio(0)/0.678 - 1, pass_=abs(ratio(0)/0.678 - 1) < 0.05)
ts = np.logspace(-1, 1, 41); rs = np.array([ratio(t) for t in ts])
out['P2'] = dict(min=rs.min(), max=rs.max(), at_t1=ratio(1), pass_=bool(np.all(np.abs(rs/0.678 - 1) < 0.05)))
src2 = open(__file__.replace('t113_351.py', 't109_posthoc.py')).read(); ns2 = {'__file__': __file__.replace('t113_351.py', 't109_posthoc.py')}
exec(src2[:src2.index('\nfor n, c in')], ns2); cfgB = (1.0e3, 2, 3.16e12, 4.98e13, 2)
s_mu = ns2['R'](cfgB, 0.055/0.1027)[1]; d_e = ns2['R'](cfgB, 2.75e-3/4.87e-4)[1]
out['P3'] = dict(s_over_mu=s_mu, d_over_e=d_e, pass_=abs(s_mu/(2/3) - 1) < 0.05 and abs(d_e/(2/3) - 1) < 0.05)
for k_, v in out.items(): print(k_, v)
