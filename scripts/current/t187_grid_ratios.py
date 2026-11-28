"""t187: the record's ratio for each interval class: the five-limit Tonnetz coset member with the smallest sqrt(pq).
Pre-registration: PREDICTIONS_t187.md."""
from fractions import Fraction as Fr
import math
names = ['P1', 'm2', 'M2', 'm3', 'M3', 'P4', 'TT', 'P5', 'm6', 'M6', 'm7', 'M7']
def octave_reduce(r):
    while r >= 2: r /= 2
    while r < 1: r *= 2
    return r
best = {}
for b in range(-12, 13):
    for c in range(-6, 7):
        k = (7*b + 4*c) % 12
        r = octave_reduce(Fr(3)**b*Fr(5)**c)
        d = math.sqrt(r.numerator*r.denominator)
        if k not in best or d < best[k][1] - 1e-12: best[k] = (r, d)
ratios = {names[k]: best[k][0] for k in range(12)}; ratios['P8'] = Fr(2)
expect = {'m2': Fr(16, 15), 'M2': Fr(9, 8), 'm3': Fr(6, 5), 'M3': Fr(5, 4), 'P4': Fr(4, 3), 'P5': Fr(3, 2), 'm6': Fr(8, 5), 'M6': Fr(5, 3), 'M7': Fr(15, 8), 'm7': Fr(9, 5), 'TT': Fr(25, 18)}
P1 = all(ratios[k] == v for k, v in expect.items())
print('P1', dict(ratios={k: str(v) for k, v in ratios.items()}, pass_=P1))
D = {k: math.sqrt(r.numerator*r.denominator) for k, r in ratios.items()}
order = sorted(D, key=D.get)
hist = ['P1', 'P8', 'P5', 'P4', 'M3', 'M6', 'm6', 'm3', 'TT', 'm7', 'M2', 'M7', 'm2']
rh = {k: i for i, k in enumerate(hist)}; rd = {k: i for i, k in enumerate(order)}
rho = 1 - 6*sum((rh[k] - rd[k])**2 for k in D)/(13*168)
print('P2', dict(order=order, D={k: round(D[k], 2) for k in order}, spearman=rho, tritone_last=order[-1] == 'TT', pass_=rho >= 0.918 - 1e-9 and order[-1] == 'TT'))
print('reported', dict(tritone_cents_25_18=round(1200*math.log2(25/18), 1), tempered=600.0))
