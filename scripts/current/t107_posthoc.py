"""t107 post hoc (after P2 failed its 1e-12 threshold). The double-precision det of a product with condition number
up to 1e10 carries rounding; the exact statement is det(H) = product of real eigenvalues. Recompute theta-bar as the
sum of the phases of eigvalsh (real by construction) and compare with the conditioning of the worst pairs."""
import numpy as np
ns = {}; src = open(__file__.replace('t107_posthoc.py', 't107_strong_cp.py')).read(); exec(src[:src.index("tbs, Js = [], []")], ns)
rng = np.random.default_rng(107); ns['rng'] = rng; pairs = []
for _ in range(1000):
    A, B = ns['rherm'](), ns['rherm'](); pairs.append((abs(ns['thetabar'](A, B)), A, B))
pairs.sort(key=lambda p: -p[0])
worst_exact = 0
for tb, A, B in pairs:
    ev = np.concatenate([np.linalg.eigvalsh(A), np.linalg.eigvalsh(B)]); ph = np.angle(np.prod(np.sign(ev)).astype(complex))
    worst_exact = max(worst_exact, abs(ph))
for tb, A, B in pairs[:5]:
    print(f'double det {tb:.2e}  cond(A)cond(B) {np.linalg.cond(A)*np.linalg.cond(B):.1e}  hermiticity err {max(np.abs(A-A.conj().T).max(), np.abs(B-B.conj().T).max()):.1e}')
print('theta-bar from real eigenvalues, worst over 1000 pairs:', worst_exact)
