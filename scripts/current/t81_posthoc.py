"""t81 post hoc (after run 1, labelled): least closure degree at which the restricted closure derives a contradiction, as n grows."""
import importlib.util, io, contextlib, numpy as np, time
spec = importlib.util.spec_from_file_location('t81', __file__.replace('t81_posthoc.py', 't81_sos_balanced.py'))
src = open(__file__.replace('t81_posthoc.py', 't81_sos_balanced.py')).read().split('out = {}')[0]
ns = {}; exec(src, ns)
ns['rng'] = np.random.default_rng(810)
for n in (30, 60, 120, 240):
    row = []
    for _ in range(4):
        eqs = ns['instance'](n, int(1.2 * n))
        first = None
        for d in range(3, 11):
            t0 = time.time()
            K = ns['closure'](eqs, d)
            if K is None: first = d; break
            if time.time() - t0 > 60: first = f'>{d}'; break
        row.append(first if first is not None else '>10')
    print('n', n, 'least inconsistent closure degree', row, flush=True)
