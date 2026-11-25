"""t83: Schoenebeck's reduction run directly. Random 3-SAT (density 4.5) -> XOR on the parity class opposite each falsifying tuple -> degree-4 restricted closure E~ -> check every 3-SAT clause and its degree-4 products, local PSD.
Pre-registration: PREDICTIONS_t83.md. Helper functions copied from t82_sos_scale.py."""
import numpy as np, itertools, time
from collections import defaultdict, deque
rng = np.random.default_rng(83)
CAP = 5_000_000
def elim_refutes(n, eqs):
    piv = {}
    for S, s in eqs:
        r = 0
        for v in S: r |= 1 << v
        r |= (1 if s < 0 else 0) << n
        low = r & ((1 << n) - 1)
        while low:
            c = (low & -low).bit_length() - 1
            if c in piv: r ^= piv[c]; low = r & ((1 << n) - 1)
            else: piv[c] = r; break
        else:
            if (r >> n) & 1: return True
    return False

def random_eqs(n, m, planted=None):
    eqs = []
    for _ in range(m):
        t = [int(x) for x in rng.choice(n, 3, replace=False)]
        s = int(np.prod([planted[v] for v in t])) if planted is not None else int(rng.choice([-1, 1]))
        eqs.append((frozenset(t), s))
    return eqs

def instance(n, m):
    while True:
        eqs = random_eqs(n, m)
        if elim_refutes(n, eqs): return eqs

def closure(eqs, d=4):
    known, index, q = {}, defaultdict(list), deque()
    def add(S, s):
        if not S: return s == 1
        if S in known: return known[S] == s
        known[S] = s; q.append(S); return True
    for S, s in eqs:
        if not add(S, s): return None, 'conflict'
    while q:
        a = q.popleft(); sa = known[a]
        seen = set()
        for v in a:
            for b in index[v]:
                if b in seen: continue
                seen.add(b)
                c = a ^ b
                if len(c) > d: continue
                if not add(c, sa * known[b]): return None, 'conflict'
        for v in a: index[v].append(a)
        if len(known) > CAP: return None, 'cap'
    return known, 'ok'

def ball(eqs, start, size=30):
    occ = defaultdict(list)
    for S, _ in eqs:
        for v in S: occ[v].append(S)
    order, seenv, dq = [], set(), deque(sorted(start))
    for v in start: seenv.add(v)
    while dq and len(order) < size:
        v = dq.popleft(); order.append(v)
        for S in occ[v]:
            for w in sorted(S):
                if w not in seenv: seenv.add(w); dq.append(w)
    return order

def local_psd(K, vars_):
    monos = [frozenset()] + [frozenset([v]) for v in vars_] + [frozenset(p) for p in itertools.combinations(vars_, 2)]
    E = lambda S: 1.0 if not S else float(K.get(S, 0))
    M = np.array([[E(a ^ b) for b in monos] for a in monos])
    return float(np.linalg.eigvalsh(M)[0])

def local_record(K, eqs):
    for S, s in eqs:
        if K.get(S) != s: return False
        for v in S:
            if frozenset([v]) in K: return False
        for p in itertools.combinations(S, 2):
            if frozenset(p) in K: return False
    return True


def to_xor(clauses):
    return [(frozenset(t), -(-1) ** (sum(f) % 2)) for t, f in clauses]
def random_sat(n, m, hidden=None):
    cl = []
    while len(cl) < m:
        t = tuple(int(x) for x in rng.choice(n, 3, replace=False)); f = tuple(int(x) for x in rng.integers(0, 2, 3))
        if hidden is not None and sum(f) % 2 == sum(hidden[v] for v in t) % 2: continue
        cl.append((t, f))
    return cl
def Ez(K, S): return 1.0 if not S else float(K.get(frozenset(S), 0))
def viol(K, t, f, extra=()):
    tot = 0.0
    for r in range(4):
        for S in itertools.combinations(range(3), r):
            sg = 1
            for i in S: sg *= (-1) ** f[i]
            mono = set(t[i] for i in S)
            for v in extra: mono ^= {v}
            tot += sg * Ez(K, mono)
    return tot / 8
out = {}
cover = [((1, 2, 3), (1, 0, 0)), ((1, 2, 4), (1, 0, 0)), ((3, 5, 6), (1, 0, 0)), ((4, 5, 6), (0, 0, 0))]
assert [s for _, s in to_xor(cover)] == [1, 1, 1, -1]
K, why = closure(to_xor(random_sat(2000, 9000) + cover)); out['S1'] = dict(result=why, pass_=K is None); print('S1', out['S1'], flush=True)
s2 = []
for _ in range(3):
    h = rng.integers(0, 2, 2000); cl = random_sat(2000, 9000, hidden=h)
    K, why = closure(to_xor(cl))
    sat = all((-1) ** int(sum(h[v] for v in S) % 2) == s for S, s in to_xor(cl))
    s2.append((why, sat))
out['S2'] = dict(results=s2, pass_=all(w == 'ok' and s for w, s in s2)); print('S2', out['S2'], flush=True)
cons = {}; p2 = []; psd = []
for n in (2000, 4000, 8000):
    cons[n] = 0
    for i in range(10):
        t0 = time.time(); cl = random_sat(n, int(4.5 * n)); xs = to_xor(cl)
        K, why = closure(xs); line = dict(n=n, i=i, closure=why, size=len(K) if K else None)
        if K is not None:
            cons[n] += 1
            ok = all(abs(viol(K, t, f)) < 1e-12 for t, f in cl)
            for j in rng.choice(len(cl), 20, replace=False):
                t, f = cl[int(j)]
                outside = [int(v) for v in rng.choice(n, 5, replace=False) if v not in t]
                ok = ok and all(abs(viol(K, t, f, (v,))) < 1e-12 for v in list(t) + outside)
            p2.append(ok); line['clauses_ok'] = ok
            if n == 8000:
                lam = min(local_psd(K, ball(xs, xs[int(j)][0])) for j in rng.choice(len(xs), 20, replace=False))
                psd.append(lam); line['min_local_eig'] = lam
        line['sec'] = round(time.time() - t0, 1); print(line, flush=True)
out['P1'] = dict(consistent_8000=cons[8000], pass_=cons[8000] >= 8)
out['P2'] = dict(pass_=bool(p2) and all(p2))
out['P3'] = dict(min_eig=min(psd) if psd else None, pass_=bool(psd) and min(psd) >= -1e-8)
out['P4'] = dict(consistent=cons, pass_=cons[8000] >= cons[2000])
for k, v in out.items(): print(k, v)
