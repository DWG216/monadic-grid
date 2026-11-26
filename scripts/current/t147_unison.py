"""t147: voices in unison, heart and brain. Pre-registration: PREDICTIONS_t147.md.
Inputs (published; ranges carried, geometric middle used):
  Heart QRS equivalent current dipole: 0.4-1 uA m (Bison et al. 2011, arXiv:1106.4779, 13 subjects 0.4-0.76; Haberkorn et al. 2006 use 1 uA m as the cardiac example).
  Cardiomyocytes: 2-3e9 (whole heart; commonly cited; Bergmann et al.).
  Brain alpha/beta rhythm: about 100 nA m from about 6e6 synchronous pyramidal cells (Lee & Jones 2013, Front. Hum. Neurosci. 7:869; consistent with recorded MEG rhythms).
  Neocortical neurons: 1.6e10 (Azevedo et al. 2009).
  One cardiomyocyte's dipole: no published value found; computed (deviation from the registration, stated) from
  q = pi a^2 sigma_i (dV/dt / theta) L, with radius a 8-12 um, intracellular conductivity sigma_i 0.17-0.6 S/m,
  upstroke dV/dt 150-300 V/s, conduction velocity theta 0.3-0.7 m/s, cell length L 80-120 um (the upstroke spans about 0.5 mm, longer than the cell).
"""
import numpy as np, itertools
gm = lambda lo, hi: np.sqrt(lo*hi)
Qh = (0.4e-6, 1.0e-6); Nh = (2e9, 3e9)
Mb = (3e6, 1.2e7); Nb = 1.6e10                               # 6e6 'on the order of': a factor 2 either way carried
a, s, dv, th, L = (8e-6, 12e-6), (0.17, 0.6), (150, 300), (0.3, 0.7), (80e-6, 120e-6)
qs = [np.pi*A**2*S*(D/T)*LL for A, S, D, T, LL in itertools.product(a, s, dv, th, L)]
q = (min(qs), max(qs)); qm = np.pi*gm(*a)**2*gm(*s)*(gm(*dv)/gm(*th))*gm(*L)
Mh = (Qh[0]/q[1], Qh[1]/q[0]); Mhm = gm(*Qh)/qm
print(f'one cardiomyocyte: q = {qm:.2e} A m (range {q[0]:.1e} to {q[1]:.1e}); one neuron in the alpha rhythm: {100e-9/6e6:.1e} A m')
print(f'heart: M = Q/q = {Mhm:.2e} (range {Mh[0]:.1e} to {Mh[1]:.1e}); f = M/N = {Mhm/gm(*Nh):.1e}')
print(f'brain alpha: M = {gm(*Mb):.1e} (range {Mb[0]:.0e} to {Mb[1]:.1e}); f = {gm(*Mb)/Nb:.1e}')
r = Mhm/gm(*Mb); print(f'M_heart / M_brain = {r:.2e} (range {Mh[0]/Mb[1]:.1e} to {Mh[1]/Mb[0]:.1e})')
P1 = r >= 100; P2 = (Mhm/gm(*Nh) >= 0.01) and (gm(*Mb)/Nb <= 1e-3)
print('P1 pass:', P1, '| P2 pass:', P2, f'(f_heart >= 0.01: {Mhm/gm(*Nh) >= 0.01}; f_brain <= 1e-3: {gm(*Mb)/Nb <= 1e-3})')
# reported, labelled post hoc: phase unison at the beat (the record's own measure is phase agreement, not the vector sum)
T, qrs = 60/72, 0.09                                          # beat period at 72 per minute; activation spread over the QRS
ph = np.linspace(0, 2*np.pi*qrs/T, 10001); Rh = abs(np.exp(1j*ph).mean())
print(f'post hoc: every cardiomyocyte fires once per beat within {qrs*1e3:.0f} ms of {T*1e3:.0f} ms: phase agreement at the beat |<e^(i phi)>| = {Rh:.3f}, so about {Rh**2*gm(*Nh):.1e} voices in phase')
print('the vector sum (Q) cancels across the wall\'s many directions; the phases do not')
