"""t173: positive energy from the singlet: Witten's identity on time-symmetric, spherically symmetric, conformally flat slices.
Pre-registration: PREDICTIONS_t173.md. G = c = 1."""
import numpy as np
from scipy.integrate import solve_ivp, simpson
rng = np.random.default_rng(1730)
R = 12.0; rr = np.linspace(1e-6, R, 60001)

def profile(sign):
    c = rng.uniform(0.5, 4, 3); w = rng.uniform(0.2, 1, 3)
    amp = rng.uniform(0, 0.02, 3) if sign == 'singlet' else rng.uniform(-0.02, 0.02, 3)
    return lambda r: np.sum(amp[:, None]*np.exp(-((np.atleast_1d(r)[None, :] - c[:, None])/w[:, None])**2), 0)

def run(rho):
    f = lambda r, y: [y[1], -2*y[1]/r - 2*np.pi*rho(r)[0]*y[0]]
    s = solve_ivp(f, [rr[0], R], [1.0, 0.0], t_eval=rr, rtol=1e-12, atol=1e-14, method='DOP853')
    psi, dpsi = s.y
    # outside the source psi = A + B/r: A = psi + r psi', B = -r^2 psi'
    A = psi[-1] + R*dpsi[-1]; B = -R**2*dpsi[-1]
    psi, dpsi = psi/A, dpsi/A; m = 2*B/A
    if np.any(psi <= 0): return None
    rt = rho(rr)
    i1 = 6*dpsi**2*psi**-4; i2 = 4*np.pi*rt*psi**-2
    b = B/A; tail = 8*np.pi*b*(1 - (1 + b/R)**-3)                     # exact exterior: psi = 1 + b/r, int_R^inf 6 psi'^2 psi^-4 4 pi r^2 dr
    I = simpson((i1 + i2)*4*np.pi*rr**2, x=rr) + tail
    return dict(m=m, I=I, rel=abs(I - 4*np.pi*m)/max(abs(4*np.pi*m), 1e-300), min_i1=i1.min(), min_i2=i2.min())

res = {}
for kind in ('singlet', 'with_cross_term'):
    rs = [run(profile(kind)) for _ in range(1000)]
    bad = sum(r is None for r in rs); rs = [r for r in rs if r is not None]
    res[kind] = dict(n=len(rs), psi_nonpositive=bad, max_rel=max(r['rel'] for r in rs), m_min=min(r['m'] for r in rs),
                     m_max=max(r['m'] for r in rs), frac_negative_m=np.mean([r['m'] < 0 for r in rs]),
                     min_i1=min(r['min_i1'] for r in rs), min_i2=min(r['min_i2'] for r in rs))
    print(kind, res[kind])
s, x = res['singlet'], res['with_cross_term']
print('P1', dict(max_rel_singlet=s['max_rel'], max_rel_cross=x['max_rel'], pass_=s['max_rel'] < 1e-6 and x['max_rel'] < 1e-6))
print('P2', dict(m_min=s['m_min'], min_integrands=(s['min_i1'], s['min_i2']), pass_=s['m_min'] > 0 and s['min_i1'] >= 0 and s['min_i2'] >= 0))
print('P3', dict(frac_negative_m=x['frac_negative_m'], pass_=x['frac_negative_m'] >= 0.10))
