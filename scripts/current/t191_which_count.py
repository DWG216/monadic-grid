"""t191: neutrinos under the two candidate counts for n. See PREDICTIONS_t191.md."""
import numpy as np
from scipy.optimize import brentq
def Q(x): x = np.array(x, float); return np.sum(x**2)/np.sum(x)**2   # x = signed square roots
def solve(d21, dA, order, neg, Qt):
    def ms(l):
        if order == 'NO': return [l, np.sqrt(l*l+d21), np.sqrt(l*l+dA)]
        return [np.sqrt(l*l+dA-d21), np.sqrt(l*l+dA), l]
    def f(l):
        m = ms(l); s = [np.sqrt(v)*(-1 if i == neg else 1) for i, v in enumerate(m)]; return Q(s) - Qt
    g = np.linspace(1e-7, 0.3, 30001); v = np.array([f(t) for t in g]); out = []
    for i in np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]:
        l = brentq(f, g[i], g[i+1]); out.append((l, ms(l)))
    return out
BOUND = 64.2e-3
summary = {}
for label, Qt in [("C (Q = 2/3)", 2/3), ("I (Q = 3/4)", 3/4)]:
    sums = []
    print(label)
    for order, dA in [('NO', 2.513e-3), ('IO', 2.484e-3)]:
        for neg in [None, 0, 1, 2]:
            sols = solve(7.50e-5, dA, order, neg, Qt)
            txt = [(round(l*1e3, 4), round(sum(m)*1e3, 3)) for l, m in sols] if sols else 'none'
            print(f"  {order} negative root {neg}: (lightest meV, sum meV) {txt}")
            sums += [sum(m) for _, m in sols]
    summary[label] = sums
    below = [s for s in sums if s < BOUND]
    print(f"  solutions: {len(sums)}; below 64.2 meV: {[round(s*1e3,3) for s in below]}")
print()
I = summary["I (Q = 3/4)"]; C = summary["C (Q = 2/3)"]
p1 = not any(s < BOUND for s in I)
p2 = any(abs(s - 59.16e-3) < 0.1e-3 for s in C)
print("P1 (candidate I has no solution below the bound):", "PASS" if p1 else "FAIL")
print("P2 (candidate C reproduces 59.16 meV):", "PASS" if p2 else "FAIL")
