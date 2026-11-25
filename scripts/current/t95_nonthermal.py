"""t95: maximum CP asymmetry per right-handed neutrino over the Majorana-phase plane. Pre-registration: PREDICTIONS_t95.md."""
import numpy as np
src = open(__file__.replace('t95_nonthermal.py', 't90_leptogenesis.py')).read(); ns = {}; exec(src[:src.index('out = {}')], ns)
pm, run = ns['pmns'], ns['run']
rng = np.random.default_rng(90); etas = []
for _ in range(20000):
    a21, a31 = rng.uniform(0, 2*np.pi, 2); etas.append(abs(run(pm(np.radians(33.4), np.radians(8.6), np.radians(49.0), np.radians(212), a21, a31))[3].sum()))
out = {'S1': dict(max_eta=max(etas), pass_=abs(max(etas)/8.242270760008952e-15 - 1) < 1e-6)}
A = np.linspace(0, 2*np.pi, 400, endpoint=False); best = [(0, None, None)]*3
for a21 in A:
    for a31 in A:
        Ms, eps, *_ = run(pm(np.radians(33.4), np.radians(8.6), np.radians(49.0), np.radians(212), a21, a31))
        order = np.argsort(Ms)
        for r, i in enumerate(order):
            e = abs(eps[i].sum())
            if e > best[r][0]: best[r] = (e, float(Ms[i]), (round(float(a21), 3), round(float(a31), 3)))
need = lambda e: 2.45e-10/(1.5*e)          # required T_R/m_phi
out['eps_max'] = [dict(N=r+1, eps=b[0], M=b[1], at=b[2], TR_over_mphi_needed=need(b[0]) if b[0] else None) for r, b in enumerate(best)]
p1 = [b for b in best if b[0] >= 1e-6]
out['P1'] = dict(pass_=bool(p1))
# P2: T_R < lightest N (~1e5 GeV); need m_phi > 2 M_i and T_R/m_phi >= need: m_phi <= T_R/need
ok = False; info = []
for b in p1:
    TR = 1e5; mphi_max = TR/need(b[0]); info.append(dict(M=b[1], mphi_window=(2*b[1], mphi_max))); ok |= mphi_max > 2*b[1]
out['P2'] = dict(windows=info, pass_=ok)
for k, v in out.items(): print(k, v)
