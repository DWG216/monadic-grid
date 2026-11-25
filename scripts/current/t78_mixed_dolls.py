"""t78: weak symmetric representation of OR over Z2, Z3, Z6. Pre-registration: PREDICTIONS_t78.md."""
from math import comb, sqrt
import itertools
import numpy as np
def min_degree(n, m, dmax=40):
    W = np.arange(1, n + 1)
    for d in range(1, min(n, dmax) + 1):
        B = np.array([[comb(int(w), j) % m for j in range(1, d + 1)] for w in W], dtype=np.int64)  # n x d
        # search coefficients a in Z_m^d; vectorised in chunks over the last few coordinates
        if m ** d <= 2_000_000:
            A = np.array(list(itertools.product(range(m), repeat=d)), dtype=np.int64)  # (m^d) x d
            V = (A @ B.T) % m
            if np.any(np.all(V != 0, axis=1)): return d
        else:
            return -d  # exhaustive search stopped at degree d: true degree >= d
    return None
out = {}
def brute(n, m):
    for d in range(1, n + 1):
        for a in itertools.product(range(m), repeat=d):
            if all(sum(a[j - 1] * comb(w, j) for j in range(1, d + 1)) % m for w in range(1, n + 1)): return d
    return None
s1 = all(brute(n, 2) == min_degree(n, 2) for n in range(1, 9)) and all(min_degree(1, m) == 1 for m in (2, 3, 6))
out['S1'] = dict(pass_=s1)
res = {}
for n in range(2, 41):
    res[n] = {m: min_degree(n, m) for m in (2, 3, 6)}
print({n: res[n] for n in (2, 4, 8, 12, 16, 20, 24, 30, 35, 40)})
lb = lambda v: abs(v)  # a negative value -d means 'at least d'
g1 = all(lb(res[n][2]) >= min(n / 2, lb(res[n][2])) and (res[n][2] > 0 and res[n][2] >= n / 2 or res[n][2] < 0) and (res[n][3] > 0 and res[n][3] >= n / 3 or res[n][3] < 0) for n in res)
out['G1'] = dict(d2=[res[n][2] for n in (10, 20, 40)], d3=[res[n][3] for n in (10, 20, 40)], pass_=g1)
g2 = all(res[n][6] > 0 and res[n][6] < min(lb(res[n][2]), lb(res[n][3])) for n in res if n >= 12) and res[40][6] is not None and res[40][6] <= 2 * sqrt(40)
out['G2'] = dict(d6=[res[n][6] for n in (12, 20, 30, 40)], pass_=g2)
for k, v in out.items(): print(k, v)
