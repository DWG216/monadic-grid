"""t182: music theory from the record. Pre-registration: PREDICTIONS_t182.md."""
import numpy as np, itertools
from fractions import Fraction as Fr
w = np.exp(2j*np.pi*np.arange(12)/12)
subsets = [s for r in range(13) for s in itertools.combinations(range(12), r)]
# P1
parts = [frozenset({k, k + 6}) for k in range(6)] + [frozenset({k, k + 4, k + 8}) for k in range(4)]
def decomposable(S):
    S = frozenset(S)
    if not S: return True
    m = min(S)
    return any(m in p and p <= S and decomposable(S - p) for p in parts)
bal = [s for s in subsets if abs(w[list(s)].sum()) < 1e-9]
P1 = all(decomposable(s) for s in bal)
print('P1', dict(balanced_subsets=len(bal), all_pairs_and_triads=P1, pass_=P1))
# P2: set classes under T and I
def canon(S):
    forms = []
    for j in range(12):
        for inv in (1, -1):
            forms.append(tuple(sorted((inv*x + j) % 12 for x in S)))
    return min(forms)
classes = {}
for s in subsets: classes.setdefault(canon(s), None)
def record(S):
    v = np.zeros(12); v[list(S)] = 1
    return tuple(np.round(np.abs(np.fft.fft(v))**2, 8))
groups = {}
for c in classes: groups.setdefault(record(c), []).append(c)
multi = [g for g in groups.values() if len(g) > 1]
pairs = [g for g in multi if len(g) == 2]
by_size = {}
for g in pairs: by_size[len(g[0])] = by_size.get(len(g[0]), 0) + 1
P2 = len(multi) == len(pairs) and len(pairs) == 23 and by_size == {4: 1, 5: 3, 6: 15, 7: 3, 8: 1}
print('P2', dict(set_classes=len(classes), record_classes=len(groups), z_pairs=len(pairs), by_size=dict(sorted(by_size.items())), larger_groups=len(multi) - len(pairs), pass_=P2))
# P3
names = ['m2', 'M2', 'm3', 'M3', 'P4', 'TT', 'P5', 'm6', 'M6', 'm7', 'M7', 'P8']
ratios = [Fr(16, 15), Fr(9, 8), Fr(6, 5), Fr(5, 4), Fr(4, 3), Fr(45, 32), Fr(3, 2), Fr(8, 5), Fr(5, 3), Fr(16, 9), Fr(15, 8), Fr(2, 1)]
def C(r, n=8):
    a = [Fr(1, k) for k in range(1, n + 1)]
    num = sum(a[i]*a[j] for i in range(n) for j in range(n) if Fr(i + 1) == r*(j + 1))
    den = sum(a)**2
    return float(num/den)
cs = {nm: C(r) for nm, r in zip(names, ratios)}; cs['P1'] = C(Fr(1))
order = sorted(cs, key=lambda k: -cs[k])
print('P3', dict(order=order, values={k: round(cs[k], 4) for k in order}, pass_=order[:4] == ['P1', 'P8', 'P5', 'P4'] and order[-1] == 'm2'))
