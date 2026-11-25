"""t77: Nullstellensatz degree over F2 and F3 for 3-XOR and 3-SAT. Pre-registration: PREDICTIONS_t77.md."""
import numpy as np, itertools
rng = np.random.default_rng(77)
def mono_mul(poly, T):
    """poly: dict mask->coef; multiply by monomial T (mask) in the multilinear ring."""
    out = {}
    for S, c in poly.items():
        k = S | T; out[k] = out.get(k, 0) + c
    return out
def popc(x): return bin(x).count('1')
def xor_poly(cl, b, p):
    a, bb, c = cl
    if p == 2:
        P = {1 << a: 1, 1 << bb: 1, 1 << c: 1}
        if b: P[0] = 1
        return {k: v % 2 for k, v in P.items() if v % 2}
    # parity(x,y,z) = x+y+z -2(xy+xz+yz) + 4xyz ; polynomial = parity - b
    P = {1 << a: 1, 1 << bb: 1, 1 << c: 1, (1 << a) | (1 << bb): -2, (1 << a) | (1 << c): -2, (1 << bb) | (1 << c): -2, (1 << a) | (1 << bb) | (1 << c): 4}
    if b: P[0] = -1
    return {k: v % p for k, v in P.items() if v % p}
def sat_poly(cl, signs, p):
    # product of (1 - lit); lit = x if positive, 1 - x if negative -> factor (1-x) or x
    P = {0: 1}
    for v, s in zip(cl, signs):
        f = {0: 1, 1 << v: -1} if s else {1 << v: 1}
        new = {}
        for S, c in P.items():
            for T, d in f.items():
                k = S | T; new[k] = new.get(k, 0) + c * d
        P = new
    return {k: v % p for k, v in P.items() if v % p}
def deg(P): return max(popc(k) for k in P)
def rank_mod(M, p):
    M = M.copy() % p; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        nz = np.flatnonzero(M[:, c]); nz = nz[nz != r]
        if nz.size: M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
        if r == rows: break
    return r
def ns_degree(polys, n, p):
    for d in range(1, n + 1):
        monos = [S for S in range(1 << n) if popc(S) <= d]
        idx = {S: i for i, S in enumerate(monos)}
        colsv = []
        for P in polys:
            dp = deg(P)
            if dp > d: continue
            for T in range(1 << n):
                if popc(T) > d - dp: continue
                Q = mono_mul(P, T)
                v = np.zeros(len(monos), np.int64)
                for k, c in Q.items(): v[idx[k]] = (v[idx[k]] + c) % p
                if v.any(): colsv.append(v)
        if not colsv: continue
        A = np.array(colsv).T
        e = np.zeros((len(monos), 1), np.int64); e[idx[0]] = 1
        if rank_mod(A, p) == rank_mod(np.hstack([A, e]), p): return d
    return None
def unsat(check, n):
    return not any(check(x) for x in range(1 << n))
def xor_instance(n, m):
    while True:
        cls = [tuple(int(v) for v in rng.choice(n, 3, replace=False)) for _ in range(m)]; bs = [int(v) for v in rng.integers(0, 2, m)]
        chk = lambda x: all(((x >> a) ^ (x >> b) ^ (x >> c)) & 1 == bb for (a, b, c), bb in zip(cls, bs))
        if unsat(chk, n): return cls, bs
def sat_instance(n, m, want_unsat=True):
    while True:
        cls = [tuple(int(v) for v in rng.choice(n, 3, replace=False)) for _ in range(m)]; sg = [tuple(int(v) for v in rng.integers(0, 2, 3)) for _ in range(m)]
        chk = lambda x: all(any(((x >> v) & 1) == s for v, s in zip(c, g)) for c, g in zip(cls, sg))
        if unsat(chk, n) == want_unsat: return cls, sg
out = {}
cls, bs = xor_instance(7, 14)
d1 = ns_degree([xor_poly(c, b, 2) for c, b in zip(cls, bs)], 7, 2)
out['S1'] = dict(deg=d1, pass_=d1 == 1)
scls, ssg = sat_instance(7, 10, want_unsat=False)
s2 = [ns_degree([sat_poly(c, g, p) for c, g in zip(scls, ssg)], 7, p) for p in (2, 3)]
out['S2'] = dict(degrees=s2, pass_=s2 == [None, None])
res = {}
for n in (7, 8, 9):
    rx2, rx3, rs2, rs3 = [], [], [], []
    for _ in range(5):
        cls, bs = xor_instance(n, 2 * n)
        rx2.append(ns_degree([xor_poly(c, b, 2) for c, b in zip(cls, bs)], n, 2))
        rx3.append(ns_degree([xor_poly(c, b, 3) for c, b in zip(cls, bs)], n, 3))
        scls, ssg = sat_instance(n, 10 * n)
        rs2.append(ns_degree([sat_poly(c, g, 2) for c, g in zip(scls, ssg)], n, 2))
        rs3.append(ns_degree([sat_poly(c, g, 3) for c, g in zip(scls, ssg)], n, 3))
    res[n] = dict(xor_F2=rx2, xor_F3=rx3, sat_F2=rs2, sat_F3=rs3)
    print('n', n, res[n], flush=True)
mean = lambda L: sum(L) / len(L)
out['P1'] = dict(pass_=all(v == 1 for n in res for v in res[n]['xor_F2']))
out['P2'] = dict(means=[mean(res[n]['xor_F3']) for n in res], pass_=all(v >= 3 for n in res for v in res[n]['xor_F3']) and mean(res[9]['xor_F3']) >= mean(res[7]['xor_F3']))
out['P3'] = dict(means_F2=[mean(res[n]['sat_F2']) for n in res], means_F3=[mean(res[n]['sat_F3']) for n in res],
                 pass_=all(v >= 3 for n in res for k in ('sat_F2', 'sat_F3') for v in res[n][k]) and all(mean(res[9][k]) >= mean(res[7][k]) for k in ('sat_F2', 'sat_F3')))
out['P4'] = dict(gap=mean(res[9]['xor_F3']) - mean(res[9]['xor_F2']), pass_=mean(res[9]['xor_F3']) - mean(res[9]['xor_F2']) >= 2)
for k, v in out.items(): print(k, v)
