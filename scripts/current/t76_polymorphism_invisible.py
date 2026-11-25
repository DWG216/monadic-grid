"""t76: the minority polymorphism is invisible to bounded-degree meetings (exact). Pre-registration: PREDICTIONS_t76.md."""
from math import comb, log10
from fractions import Fraction
from itertools import combinations, product
def K(n, w):
    return sum((-1)**j * comb(w, j) * comb(n - w, 3 - j) for j in range(4))
def Ns(n, D):
    Kw = [K(n, w) for w in range(n + 1)]; Cw = [comb(n, w) for w in range(n + 1)]
    out = {}
    for t in range(1, D + 1):
        s = sum(c * k**t for c, k in zip(Cw, Kw))
        assert s % (1 << n) == 0
        out[t] = s >> n
    return out
def norm(n, m, N, D):
    c3 = comb(n, 3)
    return sum(Fraction(comb(m, t) * N[t], c3**t) for t in range(1, D + 1))
def mstar(n, D, N):
    lo, hi = 1, 1
    while norm(n, hi, N, D) < 1: hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if norm(n, mid, N, D) >= 1: hi = mid
        else: lo = mid
    return hi
out = {}
N20 = Ns(20, 2)
out['S1'] = dict(N1=N20[1], N2=N20[2], C=comb(20, 3), pass_=N20[1] == 0 and N20[2] == comb(20, 3))
trip = [frozenset(c) for c in combinations(range(7), 3)]
masks = [sum(1 << i for i in c) for c in trip]
direct = 0
for a in masks:
    for b in masks:
        ab = a ^ b
        for c in masks:
            direct += masks.count(ab ^ c)
out['S2'] = dict(formula=Ns(7, 4)[4], direct=direct, pass_=Ns(7, 4)[4] == direct)
tab = {}
for n in (100, 200, 500, 1000, 2000):
    N = Ns(n, 8)
    tab[n] = {D: mstar(n, D, N) for D in (2, 4, 6, 8)}
    print('n', n, {D: (tab[n][D], round(tab[n][D] / n**1.5, 3)) for D in (2, 4, 6, 8)}, flush=True)
ratios = {D: [tab[n][D] / n**1.5 for n in tab] for D in (2, 4, 6, 8)}
out['G1'] = dict(pass_=all(max(r) / min(r) <= 1.5 for r in ratios.values()))
out['G2'] = dict(m_star_D8=tab[2000][8], ten_n=20000, pass_=tab[2000][8] > 10 * 2000)
for k, v in out.items(): print(k, v)
