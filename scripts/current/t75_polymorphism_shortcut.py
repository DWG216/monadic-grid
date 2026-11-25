"""t75: a reading beats the meetings only through a polymorphism. Pre-registration: PREDICTIONS_t75.md."""
import numpy as np
rng = np.random.default_rng(75)
def consistent(Arows, y, n):
    """Gaussian elimination over F2 on rows packed as Python ints (bit n = right-hand side)."""
    rows = [a | (int(b) << n) for a, b in zip(Arows, y)]
    piv = {}
    for r in rows:
        for c in range(n):
            if not (r >> c) & 1: continue
            if c in piv: r ^= piv[c]
            else: piv[c] = r; break
        else:
            if r >> n & 1: return False
            continue
        if r == 0: continue
    return True
def system(n, m):
    rows = []
    for _ in range(m):
        t = rng.choice(n, 3, replace=False); rows.append((1 << int(t[0])) | (1 << int(t[1])) | (1 << int(t[2])))
    return rows
def lhs(rows, x):
    return np.array([bin(r & x).count('1') & 1 for r in rows])
def separates(n, m, eta, trials=100):
    ok = 0
    for _ in range(trials):
        rows = system(n, m); x = int(rng.integers(0, 2**63)) & ((1 << n) - 1) if n <= 63 else int(''.join(rng.choice(['0', '1'], n)), 2)
        yp = lhs(rows, x) ^ (rng.random(m) < eta)
        yr = rng.integers(0, 2, m)
        cp, cr = consistent(rows, yp, n), consistent(rows, yr, n)
        if cp != cr:
            ok += 1 if (cp and not cr) else 0
        else:
            ok += 0.5
    return ok
out = {}
out['S1'] = dict(score=separates(100, 95, 0.0) / 100, pass_=abs(separates(100, 95, 0.0) / 100 - 0.5) < 0.1)
g1 = {n: separates(n, 2 * n, 0.0) for n in (100, 200, 400)}
g2 = {n: separates(n, 2 * n, 0.1) for n in (100, 200, 400)}
out['G1'] = dict(clean=g1, pass_=all(v == 100 for v in g1.values()))
out['G2'] = dict(noisy=g2, pass_=all(v <= 60 for v in g2.values()))
out['G3'] = dict(pass_=g2[400] <= g2[100] + 10)
for k, v in out.items(): print(k, v)
