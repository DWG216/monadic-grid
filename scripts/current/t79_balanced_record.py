"""t79: BLP+AIP on 3-SAT and 3-XOR; the balanced record. Pre-registration: PREDICTIONS_t79.md."""
import numpy as np, itertools
from scipy.optimize import linprog
rng = np.random.default_rng(79)
TUP = list(itertools.product((0, 1), repeat=3))
def sat_instance(n, m):
    while True:
        cls = [tuple(int(v) for v in rng.choice(n, 3, replace=False)) for _ in range(m)]
        fal = [tuple(int(v) for v in rng.integers(0, 2, 3)) for _ in range(m)]  # falsifying tuple of each clause
        ok = any(all(tuple((x >> v) & 1 for v in c) != f for c, f in zip(cls, fal)) for x in range(1 << n))
        if not ok: return cls, [[t for t in TUP if t != f] for f in fal]
def xor_instance(n, m):
    while True:
        cls = [tuple(int(v) for v in rng.choice(n, 3, replace=False)) for _ in range(m)]; bs = [int(v) for v in rng.integers(0, 2, m)]
        ok = any(all((((x >> a) ^ (x >> b) ^ (x >> c)) & 1) == bb for (a, b, c), bb in zip(cls, bs)) for x in range(1 << n))
        if not ok: return cls, [[t for t in TUP if sum(t) % 2 == bb] for bb in bs], bs
def blp_system(n, cls, allowed):
    """Variables: per clause one weight per allowed tuple, then per variable p_v(1). Equalities: weights sum to 1; marginal of each clause variable equals p_v(1)."""
    cols = []; ci = []
    for i, al in enumerate(allowed):
        for t in al: cols.append((i, t))
    nw = len(cols); N = nw + n
    rows, rhs = [], []
    for i, al in enumerate(allowed):
        r = np.zeros(N); r[[k for k, (j, _) in enumerate(cols) if j == i]] = 1; rows.append(r); rhs.append(1)
        for pos, v in enumerate(cls[i]):
            r = np.zeros(N)
            for k, (j, t) in enumerate(cols):
                if j == i and t[pos] == 1: r[k] = 1
            r[nw + v] = -1; rows.append(r); rhs.append(0)
    return np.array(rows), np.array(rhs, float), cols, nw
def blp_feasible(n, cls, allowed):
    A, b, cols, nw = blp_system(n, cls, allowed)
    res = linprog(np.zeros(A.shape[1]), A_eq=A, b_eq=b, bounds=[(0, 1)] * A.shape[1], method='highs')
    return res.status == 0
def check_record(n, cls, allowed, weights_fn, marg):
    A, b, cols, nw = blp_system(n, cls, allowed)
    x = np.zeros(A.shape[1])
    for k, (i, t) in enumerate(cols): x[k] = weights_fn(i, t)
    x[nw:] = marg
    return bool(np.all(np.abs(A @ x - b) < 1e-12))
def half_record(allowed):
    def w(i, t):
        fal = [u for u in TUP if u not in allowed[i]][0]
        return 0.25 if sum(t) % 2 != sum(fal) % 2 else 0.0
    return w
def int_record(allowed):
    def w(i, t):
        fal = [u for u in TUP if u not in allowed[i]][0]
        if fal != (1, 1, 1): return 1 if t == (1, 1, 1) else 0
        return {(1, 1, 0): 1, (1, 0, 1): 1, (0, 1, 1): 1, (1, 0, 0): -1, (0, 1, 0): -1, (0, 0, 1): -1, (0, 0, 0): 1}.get(t, 0)
    return w
def f2_consistent(n, cls, bs):
    rows = [(1 << a) | (1 << b) | (1 << c) | (bb << n) for (a, b, c), bb in zip(cls, bs)]
    piv = {}
    for r in rows:
        for c in range(n):
            if (r >> c) & 1:
                if c in piv: r ^= piv[c]
                else: piv[c] = r; break
        else:
            if (r >> n) & 1: return False
    return True
out = {}
n = 10
sats = [sat_instance(n, 80) for _ in range(10)]
xors = [xor_instance(n, 20) for _ in range(10)]
c0, a0 = sats[0]
out['S1'] = dict(lp=blp_feasible(n, c0, a0), record=check_record(n, c0, a0, half_record(a0), 0.5), pass_=blp_feasible(n, c0, a0) and check_record(n, c0, a0, half_record(a0), 0.5))
out['P1'] = dict(lp_accepts=sum(blp_feasible(n, c, a) for c, a in sats), record_ok=sum(check_record(n, c, a, half_record(a), 0.5) for c, a in sats))
out['P1']['pass_'] = out['P1']['lp_accepts'] == 10 and out['P1']['record_ok'] == 10
out['P2'] = dict(int_record_ok=sum(check_record(n, c, a, int_record(a), 1.0) for c, a in sats))
out['P2']['pass_'] = out['P2']['int_record_ok'] == 10
out['P3'] = dict(lp_accepts_xor=sum(blp_feasible(n, c, a) for c, a, _ in xors), aip_rejects_xor=sum(not f2_consistent(n, c, bs) for c, _, bs in xors))
out['P3']['pass_'] = out['P3']['lp_accepts_xor'] == 10 and out['P3']['aip_rejects_xor'] == 10
for k, v in out.items(): print(k, v)
