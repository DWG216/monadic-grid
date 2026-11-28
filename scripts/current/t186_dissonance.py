"""t186: dissonance as the record's repeat period sqrt(pq). Pre-registration: PREDICTIONS_t186.md."""
from fractions import Fraction as Fr
import math
iv = {'P1': Fr(1), 'm2': Fr(16, 15), 'M2': Fr(9, 8), 'm3': Fr(6, 5), 'M3': Fr(5, 4), 'P4': Fr(4, 3), 'TT': Fr(45, 32),
      'P5': Fr(3, 2), 'm6': Fr(8, 5), 'M6': Fr(5, 3), 'm7': Fr(16, 9), 'M7': Fr(15, 8), 'P8': Fr(2)}
D = {k: math.sqrt(r.numerator*r.denominator) for k, r in iv.items()}
order = sorted(D, key=D.get)
cons = [k for k in order if k in ('P1', 'P8', 'P5', 'P4', 'M6', 'M3', 'm3', 'm6')]
P1 = cons == ['P1', 'P8', 'P5', 'P4', 'M6', 'M3', 'm3', 'm6'] and len(set(round(v, 9) for v in D.values())) == 13
print('P1', dict(order=order, D={k: round(D[k], 3) for k in order}, pass_=P1))
hist = ['P1', 'P8', 'P5', 'P4', 'M3', 'M6', 'm6', 'm3', 'TT', 'm7', 'M2', 'M7', 'm2']
rh = {k: i for i, k in enumerate(hist)}; rd = {k: i for i, k in enumerate(order)}
n = 13; rho = 1 - 6*sum((rh[k] - rd[k])**2 for k in iv)/(n*(n*n - 1))
print('P2', dict(spearman=rho, pass_=rho >= 0.8))
dis = [k for k in order if k in ('m2', 'M2', 'TT', 'm7', 'M7')]
print('reported', dict(dissonances_least_to_most=dis, historical=[k for k in hist if k in dis]))
