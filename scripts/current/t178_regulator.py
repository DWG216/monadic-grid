"""t178: area and log coefficients of a scalar's entanglement entropy for two radial discretisations (Srednicki chain).
Pre-registration: PREDICTIONS_t178.md. Method as t153 (exact to L1, perturbative tail with fitted correction)."""
import numpy as np, sys, time
REG = {'A': lambda j: (j + 0.5)**2, 'B': lambda j: j*(j + 1.0)}

def Kmat(l, N, c):
    j = np.arange(1, N + 1, dtype=float); cj = c(j)
    d = l*(l + 1)/j**2 + cj/j**2
    d[1:] += cj[:-1]/j[1:]**2
    off = -cj[:-1]/(j[:-1]*j[1:])
    return d, off

def S_exact(l, n, N, c):
    d, off = Kmat(l, N, c)
    K = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
    w, V = np.linalg.eigh(K)
    Kh = (V*np.sqrt(w))@V.T; Kmh = (V/np.sqrt(w))@V.T
    mu = np.linalg.eigvals(-0.25*Kmh[:n, n:]@Kh[n:, :n]).real
    mu = mu[mu > 0]; nu = np.sqrt(0.25 + mu); x = mu/(nu + 0.5)
    return float(np.sum((x + 1)*np.log1p(x) - x*np.log(x)))

def x0(l, n, c):
    l = np.asarray(l, dtype=float)
    d1 = l*(l + 1)/n**2 + (c(n) + c(n - 1))/n**2
    d2 = l*(l + 1)/(n + 1)**2 + (c(n + 1) + c(n))/(n + 1)**2
    k = -c(n)/(n*(n + 1)); w1, w2 = np.sqrt(d1), np.sqrt(d2)
    g = k/(w1 + w2); return g**2/(4*w1*w2)

def Sx(x): return (x + 1)*np.log1p(x) - x*np.log(x)

def S_total(n, c, L1=3000, ratio=6):
    N = ratio*n
    ex = np.array([S_exact(l, n, N, c) for l in range(L1 + 1)])
    head = float(np.sum((2*np.arange(L1 + 1) + 1)*ex))
    ls = np.arange(L1//2, L1 + 1, 50); r = ex[ls]/Sx(x0(ls, n, c))
    A = np.column_stack([np.ones_like(ls, dtype=float), 1/ls**2, 1/ls**4]); coef = np.linalg.lstsq(A, r, rcond=None)[0]
    rfun = lambda l: coef[0] + coef[1]/l**2 + coef[2]/l**4
    lt = np.arange(L1 + 1, 2_000_001, dtype=float)
    tail = float(np.sum((2*lt + 1)*Sx(x0(lt, n, c))*rfun(lt)))
    lb = 2e6; fb = (2*lb + 1)*Sx(x0(lb, n, c))*rfun(lb); tail += fb*lb/2
    return head + tail

if __name__ == '__main__':
    reg = sys.argv[1]; c = REG[reg]; ns = [10, 12, 14, 16, 20, 24, 28, 32]; t0 = time.time()
    S = {}
    for n in ns:
        S[n] = S_total(n, c); print(reg, f'n={n} S={S[n]:.10f} sec={time.time()-t0:.0f}', flush=True)
    R = np.array(ns) + 0.5; y = np.array([S[n] for n in ns])
    A = np.column_stack([R**2, np.log(R), np.ones_like(R), 1/R**2]); co = np.linalg.lstsq(A, y, rcond=None)[0]
    print(reg, 'fit', dict(s=co[0], c_log=co[1], c0=co[2], d=co[3], s_per_area=co[0]/(4*np.pi)), flush=True)
    np.save('t178_%s.npy' % reg, np.array([R, y]))
