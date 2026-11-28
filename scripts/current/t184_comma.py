"""t184: the comma as holonomy; temperament as a choice of connection. Pre-registration: PREDICTIONS_t184.md."""
import numpy as np
L3, L5 = 1200*np.log2(3), 1200*np.log2(5)
def hol(b, c):
    x = b*L3 + c*L5; return x - 1200*round(x/1200)
vals = {'syntonic (4,-1)': hol(4, -1), 'lesser diesis (0,3)': hol(0, 3), 'Pythagorean (12,0)': hol(12, 0), 'greater diesis (4,-4)': hol(4, -4)}
direct = {'syntonic (4,-1)': 1200*np.log2(81/80), 'lesser diesis (0,3)': -1200*np.log2(128/125),
          'Pythagorean (12,0)': 1200*np.log2(531441/524288), 'greater diesis (4,-4)': 1200*np.log2(648/625)}
add = abs(hol(12, 0) - (3*hol(4, -1) + hol(0, 3))) < 1e-9 and abs(hol(4, -4) - (hol(4, -1) - hol(0, 3))) < 1e-9
P1 = add and all(abs(vals[k] - direct[k]) < 1e-3 for k in vals)
print('P1', dict(values={k: round(v, 4) for k, v in vals.items()}, direct={k: round(v, 4) for k, v in direct.items()}, additive=add, pass_=P1))
rng = np.random.default_rng(1840); steps = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1)]; worst = 0.0
for _ in range(10000):
    path = [steps[i] for i in rng.integers(0, 6, 20)]
    s = np.sum(path, 0); path.append(tuple(-s))
    total = sum(b*L3 + c*L5 for b, c in path); worst = max(worst, abs(total))
print('P2', dict(max_contractible_holonomy=worst, pass_=worst < 1e-6))
A = np.array([[4., -1.], [0., 3.]]); f, t = np.linalg.solve(A, [2400., 1200.])
print('P3', dict(fifth=f, third=t, det=np.linalg.det(A), pass_=abs(f - 700) < 1e-9 and abs(t - 400) < 1e-9 and abs(np.linalg.det(A)) > 0))
