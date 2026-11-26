"""t153: the scalar's -1/90 log term on the t27 lattice (Srednicki's radial chain). Pre-registration: PREDICTIONS_t153.md.
Precision: X_A P_A - 1/4 = -(1/4) (K^-1/2)_AB (K^1/2)_BA exactly, so the small symplectic excesses are computed without cancellation.
Large l: exact diagonalisation up to L1; beyond, the two-site perturbative excess x0(l) times a correction r(l) = 1 + a/l^2 + b/l^4 fitted
on the exact values near L1, summed directly to 2e6 and by an integral beyond."""
import numpy as np, sys, time

def Kmat(l, N):
    j = np.arange(1, N + 1, dtype=float)
    c = (j + 0.5)**2
    d = l*(l + 1)/j**2 + c/j**2
    d[1:] += c[:-1]/j[1:]**2
    off = -c[:-1]/(j[:-1]*j[1:])
    return d, off

def S_exact(l, n, N):
    d, off = Kmat(l, N)
    K = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
    w, V = np.linalg.eigh(K)
    Kh = (V*np.sqrt(w))@V.T; Kmh = (V/np.sqrt(w))@V.T
    mu = np.linalg.eigvals(-0.25*Kmh[:n, n:]@Kh[n:, :n]).real
    mu = mu[mu > 0]
    nu = np.sqrt(0.25 + mu); x = mu/(nu + 0.5)
    return float(np.sum((x + 1)*np.log1p(x) - x*np.log(x)))

def x0(l, n):
    l = np.asarray(l, dtype=float)
    d1 = l*(l + 1)/n**2 + ((n + 0.5)**2 + (n - 0.5)**2)/n**2
    d2 = l*(l + 1)/(n + 1)**2 + ((n + 1.5)**2 + (n + 0.5)**2)/(n + 1)**2
    k = -(n + 0.5)**2/(n*(n + 1)); w1, w2 = np.sqrt(d1), np.sqrt(d2)
    g = k/(w1 + w2)
    return g**2/(4*w1*w2)

def Sx(x): return (x + 1)*np.log1p(x) - x*np.log(x)

def S_total(n, L1=4000, ratio=6):
    N = ratio*n
    ex = np.array([S_exact(l, n, N) for l in range(L1 + 1)])
    head = float(np.sum((2*np.arange(L1 + 1) + 1)*ex))
    # correction ratio fitted on the last stretch of exact values
    ls = np.arange(L1//2, L1 + 1, 50); r = ex[ls]/Sx(x0(ls, n))
    A = np.column_stack([np.ones_like(ls, dtype=float), 1/ls**2, 1/ls**4]); coef = np.linalg.lstsq(A, r, rcond=None)[0]
    rfun = lambda l: coef[0] + coef[1]/l**2 + coef[2]/l**4
    lt = np.arange(L1 + 1, 2_000_001, dtype=float)
    tail = float(np.sum((2*lt + 1)*Sx(x0(lt, n))*rfun(lt)))
    # beyond 2e6: (2l+1) S ~ C l^-3 (ln l + c'); integral of the fitted form
    lb = 2e6; fb = (2*lb + 1)*Sx(x0(lb, n))*rfun(lb)
    tail += fb*lb/2                                     # integral of f(lb)(lb/l)^3 from lb to infinity (log factor varies by < 1e-6 here)
    return head + tail, dict(coef0=coef[0], resid=float(np.max(np.abs(A@coef - r))))

if __name__ == '__main__':
    t0 = time.time(); out = {}
    ns = [10, 12, 14, 16, 20, 24, 28, 32, 40]
    S = {}; diag = {}
    for n in ns:
        S[n], diag[n] = S_total(n); print(f'n={n:3d}  S={S[n]:.9f}  r-fit c0={diag[n]["coef0"]:.8f} resid={diag[n]["resid"]:.1e}', flush=True)
    s2, _ = S_total(20, L1=8000)
    out['S2'] = dict(S20=S[20], S20_doubled=s2, diff=abs(s2 - S[20]), pass_=abs(s2 - S[20]) < 1e-6)
    R = np.array(ns) + 0.5; y = np.array([S[n] for n in ns])
    def fit(R, y, inv2=True):
        cols = [R**2, np.log(R), np.ones_like(R)] + ([1/R**2] if inv2 else [])
        return np.linalg.lstsq(np.column_stack(cols), y, rcond=None)[0]
    c = fit(R, y)
    out['S1'] = dict(c2=c[0], t27=0.295, pass_=abs(c[0]/0.295 - 1) < 0.02)
    out['P1'] = dict(c_log=c[1], target=-1/90, dev=c[1]*90 + 1, pass_=abs(c[1]*90 + 1) < 0.10)
    c_no2 = fit(R, y, inv2=False); c_big = fit(R[3:], y[3:])
    out['P2'] = dict(c_log_no_inv2=c_no2[1], c_log_drop3=c_big[1],
                     pass_=abs(c_no2[1]*90 + 1) < 0.15 and abs(c_big[1]*90 + 1) < 0.15)
    for k, v in out.items(): print(k, v)

