"""t92: minimum right-handed mass ratio over the Majorana-phase plane. Pre-registration: PREDICTIONS_t92.md."""
import numpy as np
src = open(__file__.replace('t92_degenerate_pair.py', 't90_leptogenesis.py')).read(); ns = {}; exec(src[:src.index('out = {}')], ns)
pm, run = ns['pmns'], ns['run']
best = (1e99, None); med = None
A = np.linspace(0, 2*np.pi, 400, endpoint=False)
for a21 in A:
    for a31 in A:
        Ms = np.sort(run(pm(np.radians(33.4), np.radians(8.6), np.radians(49.0), np.radians(212), a21, a31))[0])
        r = min(Ms[1]/Ms[0] - 1, Ms[2]/Ms[1] - 1)
        if r < best[0]: best = (r, (round(float(a21), 4), round(float(a31), 4)), Ms.tolist())
        if med is None: med = Ms.tolist()
out = {}
out['S1'] = dict(masses_at_origin=med, pass_=1e4 < med[0] < 1e6 and 1e8 < med[1] < 1e10 and 1e11 < med[2] < 1e13)
out['P1'] = dict(min_ratio=best[0], at=best[1], masses=best[2], pass_=best[0] > 10)
for k, v in out.items(): print(k, v)
