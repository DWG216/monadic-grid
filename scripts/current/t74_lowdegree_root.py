"""t74: the low-degree norm on one slice; the root from meeting term against exclusion. Pre-registration: PREDICTIONS_t74.md."""
from math import comb, sqrt
from functools import lru_cache
@lru_cache(None)
def a(v, e):
    return sum((-1)**j * comb(v, j) * comb(comb(v - j, 2), e) for j in range(v + 1))
def falling(x, r):
    p = 1.0
    for i in range(r): p *= (x - i)
    return p
def norm(n, k, D, drop_one_edge):
    s = 0.0
    for e in range(1, D + 1):
        if drop_one_edge and e == 1: continue
        for v in range(2, min(2 * e, n) + 1):
            c = a(v, e)
            if c == 0: continue
            w = falling(k, v) / falling(n, v)
            s += comb(n, v) * c * w * w
    return s
def kstar(n, D, drop):
    lo, hi = 2, n
    if norm(n, hi, D, drop) < 1: return None
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if norm(n, mid, D, drop) >= 1: hi = mid
        else: lo = mid
    return hi
out = {}
tot4 = sum(a(4, e) for e in range(0, 7))
out['S1'] = dict(a21=a(2, 1), a32=a(3, 2), a33=a(3, 3), total4=tot4, pass_=(a(2, 1), a(3, 2), a(3, 3), tot4) == (1, 3, 1, 41))
k1 = kstar(10**6, 1, False)
out['S2'] = dict(ratio=k1 / sqrt(10**6), target=2**0.25, pass_=abs(k1 / sqrt(10**6) / 2**0.25 - 1) < 0.05)
tab = {}
for D in (2, 4, 6, 8):
    tab[D] = {n: round(kstar(n, D, True) / sqrt(n), 3) for n in (10**3, 10**4, 10**5, 10**6, 10**7)}
    print('D', D, tab[D], flush=True)
out['G1'] = dict(pass_=all(max(r.values()) / min(r.values()) <= 1.5 for r in tab.values()))
out['G2'] = dict(D8_at_1e6=tab[8][10**6], D2_at_1e6=tab[2][10**6], pass_=tab[8][10**6] >= 0.5)
for k_, v in out.items(): print(k_, v)
