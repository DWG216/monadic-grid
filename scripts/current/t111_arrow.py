"""t111: balanced pairs as null constructors; the arrow is the count. Pre-registration: PREDICTIONS_t111.md."""
import numpy as np, itertools, collections
rng = np.random.default_rng(111); out = {}
S = complex(rng.standard_normal(), rng.standard_normal()); th = rng.uniform(0, 2*np.pi, 100000)
dS = np.abs((np.exp(1j*th) + np.exp(1j*(th + np.pi))))
out['P1'] = dict(max_dS=float(dS.max()), pass_=dS.max() < 1e-12)
dec = []
for _ in range(200):
    z = np.cumsum(np.exp(1j*rng.uniform(0, 2*np.pi, 10000))); r = np.abs(z)**2; dec.append(np.mean(np.diff(r) < 0))
out['P2'] = dict(frac_record_decreasing=float(np.mean(dec)), count_increasing=1.0, pass_=0.4 < np.mean(dec) < 0.6)
w = np.exp(2j*np.pi*np.arange(12)/12); cls = collections.Counter()
for ph in itertools.product(range(12), repeat=4):          # 4 free phases, rest fixed: 12^4 assignments of n=8 (pairs fixed)
    s = w[list(ph)].sum() + w[[0, 3, 6, 9]].sum(); cls[round(abs(s)**2, 9)] += 1
out['P3'] = dict(n_values=len(cls), min_class=min(cls.values()), pass_=min(cls.values()) > 1)
for a, b in out.items(): print(a, b)
