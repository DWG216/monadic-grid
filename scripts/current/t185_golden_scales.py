"""t185: golden generators and well-formed scales. Pre-registration: PREDICTIONS_t185.md."""
import numpy as np
phi = (1 + 5**0.5)/2
def steps(g, n):
    x = np.sort((np.arange(n)*g) % 1.0); d = np.diff(np.append(x, x[0] + 1))
    u = []
    for v in sorted(d):
        if not u or v - u[-1] > 1e-9: u.append(v)
    return u
res = {}
for name, g in (('golden', 1/phi), ('fifth', np.log2(1.5))):
    mx = max(len(steps(g, n)) for n in range(2, 301))
    two = [n for n in range(2, 301) if len(steps(g, n)) == 2]
    res[name] = (mx, two)
print('P1', dict(max_steps={k: v[0] for k, v in res.items()}, pass_=all(v[0] <= 3 for v in res.values())))
fib = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
ratios = [max(steps(1/phi, n))/min(steps(1/phi, n)) for n in fib]
P2 = res['golden'][1] == fib and all(abs(r - phi) < 1e-9 for r in ratios)
print('P2', dict(two_step_sizes=res['golden'][1], ratio_err=max(abs(r - phi) for r in ratios), pass_=P2))
tf = [n for n in res['fifth'][1] if n <= 60]
P3 = all(k in tf for k in (5, 7, 12, 41, 53)) and min(n for n in tf if n > 7) == 12
print('P3', dict(fifth_two_step_to_60=tf, pass_=P3))
