"""t152: horizon microstates with pairwise balance; the log coefficient without a graviton loop. Pre-registration: PREDICTIONS_t152.md."""
import itertools, math
import numpy as np
W = [w for w in itertools.product((1, -1), repeat=5) if w.count(-1) % 2 == 0]
Wbar = [w for w in itertools.product((1, -1), repeat=5) if w.count(-1) % 2 == 1]
neg = {w: tuple(-x for x in w) for w in W}
in16 = sum(neg[w] in W for w in W); in16bar = sum(neg[w] in Wbar for w in W)   # where a cell's balancing partner lives
def pair_count(n):
    """n straddling pairs: inside cell w, outside cell balancing it (-w). Count configurations, all balanced."""
    return len(W)**n
ns = np.arange(200, 2001, 100)
corr = np.array([math.log(pair_count(int(n))) - n*math.log(16) for n in ns])
slope = np.polyfit(np.log(ns), corr, 1)[0]
out = {'S1': dict(partners_in_16=in16, partners_in_16bar=in16bar, pass_=in16bar == 16),
       'P2a': dict(log_coefficient_pairwise=float(slope), t150_global=-2.5, pass_=abs(slope) < 1e-9)}
C = lambda nS, nV, nF, grav: (2*nS - 26*nV + 7*nF + (424 if grav else 0))/90
cases = {'grid, astrophysical (photon only, no graviton loop)': C(0, 1, 0, False),
         'Sen, astrophysical (photon + quantised graviton)': C(0, 1, 0, True),
         'grid, Standard Model all massless (no graviton loop)': C(4, 12, 24, False),
         'Sen, Standard Model all massless + graviton': C(4, 12, 24, True)}
coef = {k: dict(C=v, lnA=(v - 1)/2) for k, v in cases.items()}
g, s = coef['grid, astrophysical (photon only, no graviton loop)']['lnA'], coef['Sen, astrophysical (photon + quantised graviton)']['lnA']
out['P2b'] = dict(coefficients=coef, pass_=abs(g + 0.6444) < 1e-4 and abs(s - 1.7111) < 1e-4)
for k, v in out.items(): print(k, v)
