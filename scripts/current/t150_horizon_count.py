"""t150: horizon microstates as balanced records of SO(10) spinor cells. Pre-registration: PREDICTIONS_t150.md."""
import itertools, math
import numpy as np
from math import comb, log

def N0(n):
    """Number of n-tuples of SO(10) spinor weights ((+-1/2)^5, even number of minus signs) summing to zero."""
    if n % 2: return 0
    tot = 0
    for t in range(n + 1):
        c = sum((-1)**k*comb(t, k)*comb(n - t, n//2 - k) for k in range(t + 1) if 0 <= n//2 - k <= n - t)
        tot += comb(n, t)*c**5
    assert tot % 2**n == 0
    return tot >> n

W = [w for w in itertools.product((1, -1), repeat=5) if w.count(-1) % 2 == 0]
assert len(W) == 16
def brute(n):
    cnt = 0
    for tup in itertools.product(range(16), repeat=n):
        if all(sum(W[i][j] for i in tup) == 0 for j in range(5)): cnt += 1
    return cnt
out = {}
bf = {n: brute(n) for n in (2, 4)}
# n = 6 brute force by convolution over weight sums
from collections import Counter
dist = Counter({(0,)*5: 1})
for _ in range(6):
    new = Counter()
    for s, c in dist.items():
        for w in W: new[tuple(a + b for a, b in zip(s, w))] += c
    dist = new
bf[6] = dist[(0,)*5]
out['S1'] = dict(formula={n: N0(n) for n in bf}, brute=bf, pass_=all(N0(n) == bf[n] for n in bf))
ns = np.arange(200, 2001, 100)
corr = np.array([math.log(N0(int(n))) - n*log(16) for n in ns])
slope, const = np.polyfit(np.log(ns), corr, 1)
out['P1'] = dict(log_coefficient=slope, const=const, pass_=abs(slope + 2.5) < 0.02)
sen = {}
for label, nF in (('Dirac, n_F = 24', 24), ('Majorana, n_F = 48', 48)):
    C = (2*4 - 26*12 + 7*nF + 424)/90
    sen[label] = dict(C_local=C, lnA_coefficient=(C - 1)/2)
grid = -2.5
out['P2'] = dict(grid=grid, sen=sen, pass_=all(abs(grid - v['lnA_coefficient']) < 0.5 for v in sen.values()))
for k, v in out.items(): print(k, v)
