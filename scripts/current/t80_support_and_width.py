"""t80: BLP support check (t79 open item) and (2,3)-consistency on 3-SAT, 3-XOR, 2-SAT. Pre-registration: PREDICTIONS_t80.md."""
import numpy as np, itertools, importlib.util, io, contextlib
from scipy.optimize import linprog
here = __file__.rsplit('/', 1)[0] + '/'
spec = importlib.util.spec_from_file_location('t79', here + 't79_balanced_record.py')
t79 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(t79)   # regenerates t79's instances, seed 79
out = {}
# Part A
def support_full(n, cls, allowed):
    A, b, cols, nw = t79.blp_system(n, cls, allowed)
    N = A.shape[1]
    for k in range(nw):
        c = np.zeros(N); c[k] = -1
        r = linprog(c, A_eq=A, b_eq=b, bounds=[(0, 1)] * N, method='highs')
        if r.status != 0 or -r.fun <= 1e-9: return False
    return True
a1 = [support_full(10, c, a) for c, a in t79.sats[:5]]
out['A1'] = dict(full_support=sum(a1), pass_=sum(a1) == 5)
# Part B
rng = np.random.default_rng(80)
def clauses_ok(assign, cl):
    """cl: (vars, allowed-set of tuples)."""
    return all(tuple(assign[v] for v in vs) in al for vs, al in cl)
def brute_sat(n, cls):
    X = (np.arange(1 << n)[:, None] >> np.arange(n)) & 1
    ok = np.ones(1 << n, bool)
    for vs, al in cls:
        sub = X[:, list(vs)]; m = np.zeros(1 << n, bool)
        for t in al: m |= np.all(sub == np.array(t), axis=1)
        ok &= m
        if not ok.any(): return False
    return True
def k3sat(n, m):
    out = []
    for _ in range(m):
        vs = tuple(int(v) for v in rng.choice(n, 3, replace=False)); f = tuple(int(v) for v in rng.integers(0, 2, 3))
        out.append((vs, {t for t in itertools.product((0, 1), repeat=3) if t != f}))
    return out
def k3xor(n, m):
    out = []
    for _ in range(m):
        vs = tuple(int(v) for v in rng.choice(n, 3, replace=False)); b = int(rng.integers(0, 2))
        out.append((vs, {t for t in itertools.product((0, 1), repeat=3) if sum(t) % 2 == b}))
    return out
def k2sat(n, m):
    out = []
    for _ in range(m):
        vs = tuple(int(v) for v in rng.choice(n, 2, replace=False)); f = tuple(int(v) for v in rng.integers(0, 2, 2))
        out.append((vs, {t for t in itertools.product((0, 1), repeat=2) if t != f}))
    return out
def gen(kind, n, m, want_unsat=True):
    while True:
        cls = {'sat': k3sat, 'xor': k3xor, '2sat': k2sat}[kind](n, m)
        if brute_sat(n, cls) != want_unsat: return cls
def consistency23(n, cls):
    """(2,3)-consistency on pairs; returns True if refuted."""
    P = {(x, y): set(itertools.product((0, 1), repeat=2)) for x in range(n) for y in range(x + 1, n)}
    def pair(x, y, a, b):
        return (a, b) in P[(x, y)] if x < y else (b, a) in P[(y, x)]
    inside = {}
    for vs, al in cls:
        key = tuple(sorted(vs)); inside.setdefault(key, []).append((vs, al))
    # constraints restrict pairs directly
    for vs, al in cls:
        for i, j in itertools.combinations(range(len(vs)), 2):
            x, y = vs[i], vs[j]
            proj = {(t[i], t[j]) for t in al}
            if x > y: x, y = y, x; proj = {(b, a) for a, b in proj}
            P[(x, y)] &= proj
    def triple_ok(x, y, z, a, b, c):
        if not (pair(x, y, a, b) and pair(x, z, a, c) and pair(y, z, b, c)): return False
        asg = {x: a, y: b, z: c}
        for key in [tuple(sorted((x, y, z)))]:
            for vs, al in inside.get(key, []):
                if tuple(asg[v] for v in vs) not in al: return False
        return True
    changed = True
    while changed:
        changed = False
        for (x, y), S in P.items():
            for (a, b) in list(S):
                for z in range(n):
                    if z in (x, y): continue
                    if not any(triple_ok(x, y, z, a, b, c) for c in (0, 1)):
                        S.discard((a, b)); changed = True; break
            if not S: return True
    return False
def elim_refutes(n, cls):
    rows = []
    for vs, al in cls:
        b = sum(next(iter(al))) % 2
        r = 0
        for v in vs: r |= 1 << v
        rows.append(r | (b << n))
    piv = {}
    for r in rows:
        for c in range(n):
            if (r >> c) & 1:
                if c in piv: r ^= piv[c]
                else: piv[c] = r; break
        else:
            if (r >> n) & 1: return True
    return False
n = 20
s_sat = gen('sat', n, 100, want_unsat=False); s_2 = gen('2sat', n, 30, want_unsat=False)
out['S1'] = dict(pass_=not consistency23(n, s_sat) and not consistency23(n, s_2))
r2 = [consistency23(n, gen('2sat', n, 60)) for _ in range(10)]
r3 = [consistency23(n, gen('sat', n, 100)) for _ in range(10)]
xs = [gen('xor', n, 25) for _ in range(10)]
rx = [consistency23(n, c) for c in xs]; re = [elim_refutes(n, c) for c in xs]
out['B1'] = dict(refuted=sum(r2), pass_=sum(r2) == 10)
out['B2'] = dict(refuted=sum(r3), pass_=sum(r3) <= 1)
out['B3'] = dict(width_refuted=sum(rx), elim_refuted=sum(re), pass_=sum(rx) <= 1 and sum(re) == 10)
for k, v in out.items(): print(k, v)
