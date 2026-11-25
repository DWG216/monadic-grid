"""t82: degree-4 restricted closure (Grigoriev's pseudo-expectation) for random 3-XOR at n = 1000-4000; local PSD; local balanced record.
Pre-registration: PREDICTIONS_t82.md."""
import numpy as np, itertools, time
from collections import defaultdict, deque
rng = np.random.default_rng(82)
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

out = {}
# S1 planted odd even cover
eqs = random_eqs(1000, 1000) + [(frozenset([1, 2, 3]), 1), (frozenset([1, 2, 4]), 1), (frozenset([3, 5, 6]), 1), (frozenset([4, 5, 6]), -1)]
K, why = closure(eqs); out['S1'] = dict(result=why, pass_=K is None and why == 'conflict'); print('S1', out['S1'], flush=True)
# S2 planted satisfiable
s2 = []
for _ in range(3):
    x = rng.choice([-1, 1], 1000)
    K, why = closure(random_eqs(1000, 1000, planted=x)); s2.append(why)
out['S2'] = dict(results=s2, pass_=all(w == 'ok' for w in s2)); print('S2', out['S2'], flush=True)

cons = {}; psd = []; rec = []; refuted = 0
for n in (1000, 2000, 4000):
    cons[n] = 0
    for i in range(10):
        t0 = time.time(); eqs = instance(n, n); refuted += 1
        K, why = closure(eqs)
        line = dict(n=n, i=i, closure=why, size=(len(K) if K else None), sec=round(time.time() - t0, 1))
        if K is not None:
            cons[n] += 1
            if n == 4000:
                picks = rng.choice(len(eqs), 20, replace=False)
                lam = min(local_psd(K, ball(eqs, eqs[int(j)][0])) for j in picks)
                psd.append(lam); r = local_record(K, eqs); rec.append(r)
                line.update(min_local_eig=lam, local_record=r)
        print(line, flush=True)
out['P1'] = dict(consistent_4000=cons[4000], pass_=cons[4000] >= 8)
out['P2'] = dict(consistent=cons, pass_=cons[4000] >= cons[1000])
out['P3'] = dict(min_eig=min(psd) if psd else None, pass_=bool(psd) and min(psd) >= -1e-8)
out['P4'] = dict(pass_=bool(rec) and all(rec))
out['P5'] = dict(refuted=refuted, pass_=refuted == 30, note='kept only if elimination refutes')
for k, v in out.items(): print(k, v)
