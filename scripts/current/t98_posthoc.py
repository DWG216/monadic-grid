"""t98 post hoc (labelled, after seeing t98's information line): quark chord phases with errors; is delta halving (2/9, 1/9, 1/18) within errors?"""
import numpy as np
src = open(__file__.replace('t98_posthoc.py', 't98_koide_phase.py')).read(); ns = {}; exec(src[:src.index('me, mmu')], ns); chord = ns['chord']
rng = np.random.default_rng(980)
for name, v, e, target in (('down', [3.1e-3, 0.057, 2.87], [0.5e-3, 0.012, 0.06], 1/9), ('up', [1.54e-3, 0.599, 169.6], [0.50e-3, 0.050, 2.3], 1/18)):
    ds = np.array([chord([max(x + s*rng.standard_normal(), 1e-9) for x, s in zip(v, e)])[2] for _ in range(20000)])
    print(name, 'delta', round(float(np.mean(ds)), 4), '+-', round(float(np.std(ds)), 4), 'halving target', round(target, 4), 'pull', round(float((np.mean(ds) - target)/np.std(ds)), 2))
