"""t149: record-sourced gravity and the decoherence-diffusion trade-off. Pre-registration: PREDICTIONS_t149.md."""
import numpy as np
rng = np.random.default_rng(1490)

def run(k, g=1.0, eta=1.0, k_extra=0.0, D_extra=0.0, n=4000, dt=1e-3, T=2.0):
    """Qubit under continuous sigma_z measurement (strength k, efficiency eta) plus unread dephasing k_extra;
    classical probe pushed by g * (measurement current estimate of sigma_z) plus extra force noise D_extra.
    Returns fitted coherence decay rate gamma and probe momentum diffusion D."""
    steps = int(T/dt); ke = eta*k; kt = k + k_extra
    # coherence: start in |+> (Bloch x = 1, z = 0)
    x = np.ones(n); z = np.zeros(n); xs = [1.0]
    for _ in range(steps):
        dW = rng.normal(0, np.sqrt(dt), n)
        dx = -2*kt*x*dt - 2*np.sqrt(ke)*z*x*dW
        dz = 2*np.sqrt(ke)*(1 - z**2)*dW
        x, z = x + dx, np.clip(z + dz, -1, 1); xs.append(x.mean())
    xs = np.array(xs); ts = np.arange(steps + 1)*dt; m = xs > 0.05
    gamma = -np.polyfit(ts[m], np.log(xs[m]), 1)[0]
    # diffusion: start in the sigma_z = +1 eigenstate; force fed from the recorded current
    p = np.zeros(n)
    for _ in range(steps):
        dW = rng.normal(0, np.sqrt(dt), n)
        dY = 2*np.sqrt(ke)*1.0*dt + dW                    # <sigma_z> = 1 stays 1
        p += g*dY/(2*np.sqrt(ke)) + np.sqrt(D_extra)*rng.normal(0, np.sqrt(dt), n)
    D = np.var(p)/T
    return gamma, D

R = lambda gam, D, g=1.0: gam*D/(g**2/2)
out = {}
gam, D = run(1.0)
out['S1'] = dict(gamma=gam, gamma_expect=2.0, D=D, D_expect=0.25,
                 pass_=abs(gam/2 - 1) < 0.02 and abs(D/0.25 - 1) < 0.03)
p1 = {kk: R(*run(kk)) for kk in (0.5, 1.0, 2.0)}
out['P1'] = dict(R=p1, pass_=all(abs(v - 1) < 0.03 for v in p1.values()))
p2 = dict(extra_dephasing=R(*run(1.0, k_extra=1.0)), extra_noise=R(*run(1.0, D_extra=0.25)), efficiency_half=R(*run(1.0, eta=0.5)))
out['P2'] = dict(R=p2, pass_=all(abs(v/2 - 1) < 0.05 for v in p2.values()))
rs = []
for _ in range(200):
    kk = rng.uniform(0.3, 2); et = rng.uniform(0.1, 1); kx = rng.uniform(0, 2); dx_ = rng.uniform(0, 2)
    gam, D = run(kk, eta=et, k_extra=kx, D_extra=dx_, n=4000, T=1.0)
    rs.append(R(gam, D))
rs = np.array(rs)
out['P3'] = dict(R_min=rs.min(), R_median=float(np.median(rs)), below=int(np.sum(rs < 0.97)), pass_=bool(rs.min() >= 0.97))
# P4: Bose geometry, numbers
hbar, G = 1.054571817e-34, 6.67430e-11
m, rho, dx, d = 1e-14, 3500.0, 250e-6, 450e-6
Rad = (3*m/(4*np.pi*rho))**(1/3)
EG = G*m**2*(6/(5*Rad) - 1/dx)                            # uniform spheres displaced by dx > 2R (t146 closed form)
tau = np.pi*hbar/EG; gamma = 1/tau
a_near, a_far = G*m/(d - dx/2)**2, G*m/(d + dx/2)**2      # acceleration of the second mass from each branch of the first
g_a = (a_near - a_far)/2
D_a = g_a**2/(2*gamma)
out['P4'] = dict(R_sphere=Rad, E_G=EG, tau=tau, gamma=gamma, g_a=g_a, D_a=D_a, pass_=tau < 0.1)
for k_, v in out.items(): print(k_, v)
