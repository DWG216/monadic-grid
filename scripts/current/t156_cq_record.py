"""t156: the record as a classical-quantum dynamics in the weak field. Pre-registration: PREDICTIONS_t156.md.
Units G = hbar = m = h = R0 = 1. Kernel K(r) = erf(r/2R0)/r (Gaussian-smeared Newton), K(0) = 1/(R0 sqrt(pi))."""
import numpy as np
from scipy.special import erf
rng = np.random.default_rng(1560)
G = hbar = m = R0 = 1.0; Nsite = 24
x = np.arange(Nsite, dtype=float)
r = np.abs(x[:, None] - x[None, :])
with np.errstate(invalid='ignore', divide='ignore'):
    K = np.where(r > 0, erf(r/(2*R0))/r, 1/(R0*np.sqrt(np.pi)))
D1 = -G*K; D2 = (4*G/(np.pi*hbar))*K; D0 = D1@np.linalg.solve(D2, D1)
out = {}
B = np.block([[D0, D1], [D1, D2]]); ev = np.linalg.eigvalsh(B)
nzero = int(np.sum(np.abs(ev) < 1e-9*ev.max()))
out['S1'] = dict(min_eig_rel=float(ev.min()/ev.max()), zero_eigs=nzero, D0_equals=float(np.max(np.abs(D0 - np.pi*hbar*G/4*K))),
                 pass_=ev.min() > -1e-10*ev.max() and nzero == Nsite)
# P1: unravelling, one mass in a superposition of sites a and b
a, b = 10, 13; ma = np.zeros(Nsite); ma[a] = m; mb = np.zeros(Nsite); mb[b] = m
EG = G*m**2*(K[a, a] - K[a, b]); Gam = EG/(np.pi*hbar)
C = (np.pi*hbar/(4*G))*np.linalg.inv(K); Ci = np.linalg.inv(C); Lc = np.linalg.cholesky(C)
ntraj, dt = 20000, 0.01; T = 2/Gam; steps = int(T/dt)
alpha = np.full(ntraj, 1/np.sqrt(2)) + 0j; beta = np.full(ntraj, 1/np.sqrt(2)) + 0j
probes = [5, 11, 18]; KP = K[probes]
coh = [0.5]; resid_sum = np.zeros(3); resid_n = 0; cov_acc = np.zeros((3, 3)); res_sq = np.zeros(3)
for _ in range(steps):
    pa = np.abs(alpha)**2
    branch_a = rng.random(ntraj) < pa
    mean = np.where(branch_a[:, None], ma, mb)*dt
    dY = mean + (rng.normal(size=(ntraj, Nsite))@Lc.T)*np.sqrt(dt)
    mexp = pa[:, None]*ma + (1 - pa)[:, None]*mb                     # <m> before the update
    Phi = -G*(dY/dt)@KP.T; Phi_mean = -G*mexp@KP.T
    res = Phi - Phi_mean; resid_sum += res.sum(0); res_sq += (res**2).sum(0); resid_n += ntraj
    cov_acc += (res.T@res)*dt
    ua, ub = dY - ma*dt, dY - mb*dt
    la = -np.einsum('ij,jk,ik->i', ua, Ci, ua)/(4*dt); lb = -np.einsum('ij,jk,ik->i', ub, Ci, ub)/(4*dt)
    mx = np.maximum(la, lb); alpha = alpha*np.exp(la - mx); beta = beta*np.exp(lb - mx)
    nrm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2); alpha /= nrm; beta /= nrm
    coh.append(float(np.mean((alpha*np.conj(beta)).real)))
coh = np.array(coh); ts = np.arange(steps + 1)*dt
gfit = -np.polyfit(ts, np.log(coh/0.5), 1)[0]
mean_res = resid_sum/resid_n; se = np.sqrt(res_sq/resid_n - mean_res**2)/np.sqrt(resid_n)
cov = cov_acc/resid_n; target = np.pi*hbar*G/4*K[np.ix_(probes, probes)]
out['P1'] = dict(Gamma_fit=gfit, Gamma=Gam, a_dev=gfit/Gam - 1,
                 b_mean_resid_over_se=(mean_res/se).tolist(),
                 c_cov_rel_dev=float(np.max(np.abs(cov/target - 1))),
                 pass_=abs(gfit/Gam - 1) < 0.02 and bool(np.all(np.abs(mean_res/se) < 3)) and np.max(np.abs(cov/target - 1)) < 0.05)
R_bound_DP = 0.54; R_bound_grid = R_bound_DP/np.pi**(1/3)
out['P2'] = dict(R0_bound_DP_A=R_bound_DP, R0_bound_grid_A=R_bound_grid, pass_=abs(R_bound_grid - 0.372) < 0.005)
a0 = 0.529177
out['P3'] = dict(R0_proposal_A=a0, signal_over_bound=(R_bound_grid/a0)**3)
for k, v in out.items(): print(k, v)
