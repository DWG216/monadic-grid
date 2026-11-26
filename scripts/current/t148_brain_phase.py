"""t148: voices in phase, the brain at alpha, beside the heart at its beat. Pre-registration: PREDICTIONS_t148.md.
Inputs:
  f, fraction of units locked to alpha: 0.16-0.40 (human single units, two participants; Large-scale communication in the human brain is
     rhythmically modulated through alpha coherence, Current Biology 2019). Taken for the whole neocortex, which favours the brain
     (recordings sit where alpha is present).
  r, locking strength of a locked unit: no clean published value found; set to 1, the most favourable to the brain (deviation, stated).
  S, alpha phase agreement across the cortex: travelling waves at 0.25-0.75 m/s (Zhang et al. 2018, Neuron), 8-12 Hz, over a path of
     0.10-0.17 m (posterior cortex to a hemisphere's length). A uniform phase gradient over L gives S = |sin(pi L/lam)/(pi L/lam)|; its
     envelope min(1, lam/(pi L)) is used, again the side favouring the brain.
  N = 1.6e10 neocortical neurons (Azevedo et al. 2009). Heart: R = 0.98, N = 2.5e9, R^2 N = 2.4e9 (t147).
"""
import numpy as np, itertools
gm = lambda lo, hi: np.sqrt(lo*hi)
f = (0.16, 0.40); r = 1.0; v = (0.25, 0.75); fr = (8.0, 12.0); L = (0.10, 0.17); N = 1.6e10; heart = 2.4e9
S = lambda vv, ff, LL: min(1.0, (vv/ff)/(np.pi*LL))
Ss = [S(a, b, c) for a, b, c in itertools.product(v, fr, L)]; Sm = S(gm(*v), gm(*fr), gm(*L))
R = gm(*f)*r*Sm; Rhi = f[1]*r*max(Ss); Rlo = f[0]*r*min(Ss)
print(f'wavelength {gm(*v)/gm(*fr)*100:.1f} cm; cycles across the path {gm(*L)/(gm(*v)/gm(*fr)):.1f}; S = {Sm:.3f} (range {min(Ss):.3f} to {max(Ss):.3f})')
print(f'brain R = f r S = {R:.3f} (range {Rlo:.3f} to {Rhi:.3f}), r = 1 assumed')
print(f'brain voices in phase R^2 N = {R**2*N:.2e} (range {Rlo**2*N:.1e} to {Rhi**2*N:.1e}); heart 2.4e9; ratio {R**2*N/heart:.1e} (at most {Rhi**2*N/heart:.1e})')
print('P1 pass:', R <= 0.1, f'(holds at the range top: {Rhi <= 0.1})', '| P2 pass:', R**2*N <= 0.01*heart, f'(holds at the range top: {Rhi**2*N <= 0.01*heart})')
