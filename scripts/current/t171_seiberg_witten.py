"""t171: the Seiberg-Witten equations as the record's law for a spinor pair.
Pre-registration: PREDICTIONS_t171.md."""
import numpy as np
from scipy.integrate import solve_ivp, quad
rng = np.random.default_rng(1710)

# P1: the pair's record splits into singlet and triplet; the triplet is the self-dual 2-forms on S+
I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
worst = 0.0
for _ in range(10000):
    psi = rng.normal(size=2) + 1j*rng.normal(size=2); n2 = np.vdot(psi, psi).real
    sig = np.outer(psi, psi.conj()) - 0.5*n2*I2
    errs = [abs(np.trace(sig))/n2, np.abs(sig - sig.conj().T).max()/n2,
            abs(np.trace(sig @ sig).real - 0.5*n2**2)/n2**2,
            abs(np.vdot(psi, sig @ psi).real - 0.5*n2**2)/n2**2,
            abs(np.trace(0.5*n2*I2).real - n2)/n2]
    worst = max(worst, max(errs))
e = [I2, -1j*sx, -1j*sy, -1j*sz]                      # Euclidean chiral basis: gamma_mu = [[0, e_mu], [e_mu^+, 0]]
def block(m, n): return 0.5*(e[m] @ e[n].conj().T - e[n] @ e[m].conj().T)   # action of e_m ^ e_n on S+
SD = [block(0, 1) + block(2, 3), block(0, 2) + block(3, 1), block(0, 3) + block(1, 2)]
ASD = [block(0, 1) - block(2, 3), block(0, 2) - block(3, 1), block(0, 3) - block(1, 2)]
def span_rank(Ms): return np.linalg.matrix_rank(np.array([np.concatenate([M.real.ravel(), M.imag.ravel()]) for M in Ms]), tol=1e-10)
sd_traceless_antiherm = all(abs(np.trace(M)) < 1e-12 and np.abs(M + M.conj().T).max() < 1e-12 for M in SD)
asd_zero = max(np.abs(M).max() for M in ASD)
print('P1', dict(max_rel_err=worst, SD_rank=span_rank(SD), SD_traceless_antihermitian=sd_traceless_antiherm,
                 ASD_on_Splus_max=asd_zero, pass_=worst < 1e-12 and span_rank(SD) == 3 and sd_traceless_antiherm))

# P2-P4: vortex reduction, radial N-vortex equations
tau = 1.0; R = 15.0; r0 = 1e-5
def rhs(eps, N):
    return lambda r, y: [N*(1 - y[1])*y[0]/r, eps*r*(tau - y[0]**2)/(2*N)]
def shoot(eps, N, c, rmax=R):
    y0 = [c*r0**N, eps*tau*r0**2/(4*N)]
    over = lambda r, y: y[0] - 1.5; over.terminal = True
    down = lambda r, y: N*(1 - y[1])*y[0]/r if r > 0.05 else 1.0; down.terminal = True
    return solve_ivp(rhs(eps, N), [r0, rmax], y0, events=[over, down], rtol=1e-12, atol=1e-14, dense_output=True, max_step=0.05)

def solve_plus(N):
    lo, hi = -12.0, 6.0                                       # log c
    for _ in range(200):
        mid = 0.5*(lo + hi); s = shoot(1, N, np.exp(mid))
        if len(s.t_events[0]): hi = mid                       # overshoot: c too big
        elif len(s.t_events[1]): lo = mid                     # turns down: c too small
        else: break
        if hi - lo < 1e-15: break
    s = shoot(1, N, np.exp(0.5*(lo + hi)))
    return s, np.exp(0.5*(lo + hi))

out = {}
for N in (1, 2, 3):
    s, c = solve_plus(N)
    rend = s.t[-1]; fR, aR = s.y[0][-1], s.y[1][-1]
    # stop where the shot is still in the vacuum (before the unstable mode grows), then evaluate there
    rs = np.linspace(r0, rend, 20000); Y = s.sol(rs); f, a = Y
    k = np.argmin(np.abs(f - 1) + np.abs(a - 1)); rv = rs[k]
    fp = N*(1 - a)*f/rs; ap = (rs*(tau - f**2)/(2*N)); B = N*ap/rs
    dens = 0.5*B**2 + 0.5*(fp**2 + (N*(1 - a)/rs)**2*f**2) + 0.125*(tau - f**2)**2
    E = np.trapezoid(2*np.pi*rs[:k+1]*dens[:k+1], rs[:k+1]); flux = 2*np.pi*N*a[k]
    out[N] = dict(c=c, r_reached=rend, r_vac=rv, f_vac=f[k], a_vac=a[k], f_R=fR, a_R=aR, flux_rel=abs(flux/(2*np.pi*N) - 1),
                  E=E, E_BPS=np.pi*tau*N, E_rel=abs(E/(np.pi*tau*N) - 1), max_f2=float((f[:k+1]**2).max()))
    print('P2 N=%d' % N, out[N])
P2 = all(abs(o['f_R'] - 1) < 1e-3 and abs(o['a_R'] - 1) < 1e-3 and o['flux_rel'] < 1e-3 and o['E_rel'] < 0.01 for o in out.values())
print('P2', dict(pass_=P2))

reg = 0
for N in (1, 2, 3):
    for c in np.logspace(-4, 2, 400):
        y0 = [c*r0**N, -tau*r0**2/(4*N)]
        big = lambda r, y: y[0] - 10; big.terminal = True
        s = solve_ivp(rhs(-1, N), [r0, R], y0, events=[big], rtol=1e-10, atol=1e-12, max_step=0.05)
        f, a = s.y
        if np.any((np.abs(f - 1) < 1e-3) & (np.abs(a - 1) < 1e-3)) and not len(s.t_events[0]) and s.t[-1] >= R - 1e-9: reg += 1
print('P3', dict(regular_found=reg, pass_=reg == 0))
print('P4', dict(max_f2={N: o['max_f2'] for N, o in out.items()}, pass_=all(o['max_f2'] <= tau + 1e-6 for o in out.values())))
