"""t133: the limit of free will per tick. Pre-registration: PREDICTIONS_t133.md."""
import numpy as np, os
from scipy.stats import spearmanr
os.chdir(os.path.dirname(os.path.abspath(__file__)))
rng = np.random.default_rng(133); out = {}
wrap = lambda x: np.angle(np.exp(1j*x))
# S1 aliasing (t_P = 1)
n = np.arange(1000); err = 0.0
for _ in range(1000):
    w = rng.uniform(-np.pi, np.pi)
    for m in (-2, -1, 1, 2): err = max(err, np.abs(np.exp(1j*w*n) - np.exp(1j*(w + 2*np.pi*m)*n)).max())
out['S1'] = dict(max_err=float(err), pass_=err < 1e-9)   # n up to 999 times 4pi: float error grows ~ n*eps*|w|
# P1 indistinguishability
M, N = 6, 8
def record(p, phi):
    z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); R = np.abs(z)**2
    cross = [2*np.sqrt(p[i]*p[j])*np.cos(phi[i] - phi[j]) for i in range(M) for j in range(i + 1, M)]
    return np.concatenate([R, np.ravel(cross)])
worst = 0.0
for _ in range(100000):
    p = rng.uniform(0.2, 1, (M, N)); phi = rng.uniform(0, 2*np.pi, (M, N)); d = rng.uniform(-4*np.pi, 4*np.pi)
    a = phi.copy(); a[0] += d; b = phi.copy(); b[0] += wrap(d)
    ra, rb = record(p, a), record(p, b); worst = max(worst, float(np.abs(ra - rb).max()/np.abs(ra).max()))
out['P1'] = dict(max_rel_diff=worst, pass_=worst < 1e-12)
# P2 recovery with two quadrature references (known phases 0 and pi/2, unit weight)
def recover(phi0, phi1):
    est = []
    for ph in (phi0, phi1):
        c = (np.abs(1 + np.exp(1j*ph))**2 - 2)/2; s = (np.abs(np.exp(1j*np.pi/2) + np.exp(1j*ph))**2 - 2)/2   # cos(ph), cos(ph - pi/2) = sin(ph)
        est.append(np.arctan2(s, c))
    return wrap(est[1] - est[0])
ds = rng.uniform(-4*np.pi, 4*np.pi, 200000); ph0 = rng.uniform(0, 2*np.pi, ds.size)
rec = recover(ph0, ph0 + ds)
inside = np.abs(ds) < np.pi - 1e-6
e_in = float(np.abs(rec[inside] - ds[inside]).max()); e_wrap = float(np.abs(wrap(rec - wrap(ds))).max())
out['P2'] = dict(max_err_inside=e_in, max_err_vs_wrap=e_wrap, max_abs_recovered=float(np.abs(rec).max()), pass_=e_in < 1e-9 and np.abs(rec).max() <= np.pi + 1e-12)
# P3 t117 dynamics, instrumented (identical update)
def run(seed, kappa=0.2, M=200, N=64, T=400, eta=0.3, eps=1e-3, lo=0.01, hi=1.0):
    rng = np.random.default_rng(seed); a = 10**rng.uniform(np.log10(lo), np.log10(hi), M)
    p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N)); turn = np.zeros(M)
    for t in range(T):
        phi += eta*rng.standard_normal((M, N))
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); Phi = np.angle(z)
        dphi = np.minimum(kappa*a[:, None]*N*p, 1.0)*np.sin(Phi - phi); phi += dphi; turn += np.abs(dphi).mean(1)
        w = np.abs(z)**2/p.sum(0); p = p*w**(0.1*a[:, None]); p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/N
    return a, turn/T
rhos, lows, tops = [], [], []
for s in range(6000, 6010):
    a, tr = run(s); rho = spearmanr(a, tr).correlation; d = np.clip(np.digitize(np.log10(a), np.linspace(-2, 0, 11)) - 1, 0, 9)
    rhos.append(float(rho)); lows.append(float(np.median(tr[d == 0])/np.pi)); tops.append(float(np.median(tr[d == 9])/np.pi))
    print(s, dict(rho=round(rho, 3), low_decile_frac_of_pi=round(lows[-1], 5), top_decile_frac_of_pi=round(tops[-1], 4)), flush=True)
out['P3'] = dict(rhos=[round(r, 3) for r in rhos], low_decile_median=float(np.median(lows)), top_decile_median=float(np.median(tops)),
                 pass_=sum(r > 0.5 for r in rhos) >= 8 and np.median(lows) < 0.01)
for k, v in out.items(): print(k, v)
