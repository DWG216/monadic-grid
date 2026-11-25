"""t120 post hoc (labelled): (1) P1's registered measure was broken by the post-sanity edit (fin restricted to a0 < 0.5 also
entered frac_half); recompute the fraction of ALL monads at a >= 0.5 by the end. (2) Time for the median capacity to reach 0.5,
with and without laws."""
import numpy as np
import t120_climb as T
src = open(T.__file__).read()
def run2(seed, kappa):
    ns = {}; exec(src.split("if __name__")[0].replace("return dict(K=K,", "return dict(frac_all=float((a >= 0.5).mean()), t_med=int(np.argmax(np.array(med) >= 0.5)) if max(med) >= 0.5 else -1, K=K,"), ns)
    return ns['run'](seed, kappa=kappa)
for kappa, name in ((0.2, 'climb'), (0.0, 'climb_nolaws')):
    rs = [run2(s, kappa) for s in range(11000, 11010)]
    print(name, 'frac of all monads at a>=0.5 at end: min', round(min(r['frac_all'] for r in rs), 3), 'median', round(float(np.median([r['frac_all'] for r in rs])), 3),
          '| ticks for median capacity to reach 0.5:', [r['t_med'] for r in rs], '| attention on laws', round(float(np.median([r['L_med'] for r in rs])), 3))
