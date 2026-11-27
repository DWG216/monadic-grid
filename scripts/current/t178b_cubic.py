"""t178b: planar area coefficient of a free massless scalar on the cubic lattice (dimensional reduction to 1D chains).
Pre-registration: PREDICTIONS_t178b.md (with its amendment)."""
import numpy as np, sys, time
def S1_factory(N):
    n = 2*N
    K0 = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    lam, V = np.linalg.eigh(K0); VA = V[:N]
    def S1(M2):
        w = lam + M2
        X = 0.5*(VA*w**-0.5)@VA.T; P = 0.5*(VA*w**0.5)@VA.T
        ev = np.linalg.eigvals(X@P).real
        nu = np.sqrt(np.clip(ev, 0.25, None))
        a, b = nu + 0.5, nu - 0.5
        return float(np.sum(a*np.log(a) - np.where(b > 1e-15, b*np.log(np.where(b > 1e-15, b, 1)), 0)))
    return S1
def area_coeff(N, nodes):
    S1 = S1_factory(N)
    x, w = np.polynomial.legendre.leggauss(nodes); k = 0.5*np.pi*(x + 1); wk = 0.5*np.pi*w
    u = 4*np.sin(k/2)**2; tot = 0.0; cache = {}
    for i in range(nodes):
        for j in range(i, nodes):
            s = S1(u[i] + u[j]); f = wk[i]*wk[j]*s
            tot += f if i == j else 2*f
    return 4*tot/(2*np.pi)**2                    # four quadrants of [-pi, pi]^2
t0 = time.time()
main = area_coeff(400, 64); print('main N=400 nodes=64', main, 'sec', int(time.time() - t0), flush=True)
c1 = area_coeff(200, 64); print('check N=200 nodes=64', c1, flush=True)
c2 = area_coeff(400, 48); print('check N=400 nodes=48', c2, flush=True)
print('S1', dict(rel_N=abs(c1/main - 1), rel_nodes=abs(c2/main - 1), pass_=abs(c1/main - 1) < 0.01 and abs(c2/main - 1) < 0.01))
print('P1', dict(s_cubic=main, s_spherical=0.2954314/(4*np.pi), ratio=main/(0.2954314/(4*np.pi)), pass_=abs(main/(0.2954314/(4*np.pi)) - 1) > 0.05))
