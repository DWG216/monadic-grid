"""t81: Grigoriev's degree-4 pseudo-expectation for 3-XOR, PSD check, local balanced record. Pre-registration: PREDICTIONS_t81.md."""
import numpy as np, itertools
rng = np.random.default_rng(81)
def elim_refutes(n, eqs):
    piv = {}
    for mask, s in eqs:
        r = mask | ((1 if s < 0 else 0) << n)
        for c in range(n):
            if (r >> c) & 1:
                if c in piv: r ^= piv[c]
                else: piv[c] = r; break
        else:
            if (r >> n) & 1: return True
    return False
def instance(n, m):
    while True:
        eqs = []
        for _ in range(m):
            t = rng.choice(n, 3, replace=False); mask = (1 << int(t[0])) | (1 << int(t[1])) | (1 << int(t[2]))
            eqs.append((mask, int(rng.choice([-1, 1]))))
        if elim_refutes(n, eqs): return eqs
def closure(eqs, d):
    """Restricted closure: combine derivable equations while degree stays <= d. Returns dict mask->sign or None if inconsistent."""
    known = {}
    frontier = []
    for mask, s in eqs:
        if mask in known and known[mask] != s: return None
        if mask not in known: known[mask] = s; frontier.append(mask)
    while frontier:
        new = []
        items = list(known.items())
        for a in frontier:
            sa = known[a]
            for b, sb in items:
                c = a ^ b
                if bin(c).count('1') > d: continue
                s = sa * sb
                if c == 0:
                    if s != 1: return None
                    continue
                if c in known:
                    if known[c] != s: return None
                else:
                    known[c] = s; new.append(c); items.append((c, s))
        frontier = new
    return known
out = {}
# S1: y0y1y2 = 1, y1y2y3 = -1 -> y0y3 = -1
k = closure([(0b0111, 1), (0b1110, -1)], 4)
out['S1'] = dict(found=k.get(0b1001), pass_=k is not None and k.get(0b1001) == -1)
n, m, d = 60, 70, 4
monos = [0] + [1 << i for i in range(n)] + [(1 << i) | (1 << j) for i in range(n) for j in range(i + 1, n)]
res = []
for _ in range(10):
    eqs = instance(n, m)
    K = closure(eqs, d)
    if K is None: res.append(dict(consistent=False)); continue
    E = lambda S: 1.0 if S == 0 else float(K.get(S, 0))
    M = np.array([[E(a ^ b) for b in monos] for a in monos])
    lam = float(np.linalg.eigvalsh(M)[0])
    cons = all(abs(E(mask ^ S) - s * E(S)) < 1e-12 for mask, s in eqs for S in monos if bin(mask ^ S).count('1') <= d and bin(S).count('1') <= 1)
    local = all(E(1 << v) == 0 for mask, _ in eqs for v in range(n) if (mask >> v) & 1) and \
            all(E(mask & ~(1 << v)) == 0 for mask, _ in eqs for v in range(n) if (mask >> v) & 1) and \
            all(E(mask) == s for mask, s in eqs)
    res.append(dict(consistent=True, min_eig=lam, constraints=cons, local_record=local))
    print(res[-1], flush=True)
ok = [r for r in res if r['consistent']]
out['P1'] = dict(consistent=len(ok), pass_=len(ok) >= 8)
out['P2'] = dict(min_eig=min(r['min_eig'] for r in ok) if ok else None, pass_=bool(ok) and all(r['min_eig'] >= -1e-8 and r['constraints'] for r in ok))
out['P3'] = dict(pass_=bool(ok) and all(r['local_record'] for r in ok))
out['P4'] = dict(pass_=True, note='instances kept only if elimination refutes')
for k_, v in out.items(): print(k_, v)
