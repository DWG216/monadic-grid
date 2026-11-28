"""t189: Koide meeting shares for up and down quarks, Huang-Zhou 2020 masses at M_Z.
See PREDICTIONS_t189.md (registered before this file)."""
import numpy as np
from fractions import Fraction

rng = np.random.default_rng(189)
N = 100_000
# (central, sigma), GeV, MS-bar at mu = M_Z, arXiv:2009.04851 Table 2, full SM
up = [(1.23e-3, 0.21e-3), (0.620, 0.017), (168.26, 0.75)]
down = [(2.67e-3, 0.19e-3), (53.16e-3, 4.61e-3), (2.839, 0.026)]

def Q(m):
    m = np.asarray(m)
    return m.sum(0) / np.sqrt(m).sum(0) ** 2

def draw(sector):
    out = []
    for c, s in sector:
        x = rng.normal(c, s, N * 2)
        x = x[x > 0][:N]
        out.append(x)
    return np.array(out)

def fractions_in(lo, hi, qmax=9):
    fs = set()
    for q in range(1, qmax + 1):
        for p in range(0, q + 1):
            f = Fraction(p, q)
            if lo <= float(f) <= hi:
                fs.add(f)
    return sorted(fs)

results = {}
for name, sector, target in [("up", up, Fraction(8, 9)), ("down", down, Fraction(3, 4))]:
    q0 = Q([c for c, _ in sector])
    qs = Q(draw(sector))
    mu, sd = qs.mean(), qs.std()
    z = (mu - float(target)) / sd
    win = fractions_in(mu - 2 * sd, mu + 2 * sd)
    p1 = abs(z) <= 2
    p3 = (len(win) == 1 and win[0] == target)
    results[name] = (p1, p3)
    print(f"{name}: Q(central) = {q0:.5f}; MC Q = {mu:.5f} +- {sd:.5f}; target {target} = {float(target):.5f}; z = {z:+.2f}")
    print(f"  2-sigma window [{mu-2*sd:.5f}, {mu+2*sd:.5f}] fractions q<=9: {[str(f) for f in win]}")
    print(f"  within 2 sigma: {p1}; window holds only the target: {p3}")

print()
print("P1 (Q_u ~ 8/9):", "PASS" if results["up"][0] else "FAIL")
print("P2 (Q_d ~ 3/4):", "PASS" if results["down"][0] else "FAIL")
print("P3 (control):", "PASS" if results["up"][1] and results["down"][1] else "FAIL")
