"""t74 post hoc (after run 1): does the threshold keep falling as the degree grows? Labelled post hoc."""
import importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location('t74', __file__.replace('t74_posthoc.py', 't74_lowdegree_root.py'))
m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
from math import sqrt, log
for n in (10**6,):
    row = {D: round(m.kstar(n, D, True) / sqrt(n), 3) for D in (8, 12, 16, 20, 24)}
    print('n', n, 'log n', round(log(n), 1), row)
