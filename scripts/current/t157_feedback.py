"""t157: t156 with the Newtonian field acting back on its source (Tilloy-Diosi). Pre-registration: PREDICTIONS_t157.md.
Units G = hbar = m = R0 = 1. Measurement part a*E_G/hbar, feedback part E_G/(4a hbar)."""
import numpy as np
from scipy.special import erf
rng = np.random.default_rng(1570)
G = hbar = m = R0 = 1.0; Nsite = 24
x = np.arange(Nsite, dtype=float); r = np.abs(x[:, None] - x[None, :])
with np.errstate(invalid='ignore', divide='ignore'):
    K = np.where(r > 0, erf(r/(2*R0))/r, 1/(R0*np.sqrt(np.pi)))
a_site, b_site = 10, 13
ma = np.zeros(Nsite); ma[a_site] = m; mb = np.zeros(Nsite); mb[b_site] = m
EG = G*m**2*(K[a_site, a_site] - K[a_site, b_site])

def simulate(a, ntraj=20000, dt=0.01):
    Ci = 4*a*G/hbar*K; C = np.linalg.inv(Ci); Lc = np.linalg.cholesky(C)
    tot = (a + 1/(4*a))*EG/hbar; T = 2/tot; steps = int(T/dt)
    al = np.full(ntraj, 1/np.sqrt(2)) + 0j; be = al.copy(); coh = [0.5]
    for _ in range(steps):
        pa = np.abs(al)**2; br = rng.random(ntraj) < pa
        dY = np.where(br[:, None], ma, mb)*dt + (rng.normal(size=(ntraj, Nsite))@Lc.T)*np.sqrt(dt)
        ua, ub = dY - ma*dt, dY - mb*dt
        la = -np.einsum('ij,jk,ik->i', ua, Ci, ua)/(4*dt); lb = -np.einsum('ij,jk,ik->i', ub, Ci, ub)/(4*dt)
        mx = np.maximum(la, lb); al = al*np.exp(la - mx); be = be*np.exp(lb - mx)
        Phidt = -G*dY@K                                   # Phi dt at every site, written from the record
        al = al*np.exp(-1j*(Phidt@ma)/hbar); be = be*np.exp(-1j*(Phidt@mb)/hbar)   # the field acts back on its source
        nrm = np.sqrt(np.abs(al)**2 + np.abs(be)**2); al /= nrm; be /= nrm
        coh.append(abs(np.mean(al*np.conj(be))))
    coh = np.array(coh); ts = np.arange(len(coh))*dt
    return -np.polyfit(ts, np.log(coh/0.5), 1)[0], tot

out = {}
g, tot = simulate(1/np.pi)
out['S1'] = dict(rate_fit_over_EG=g/EG, predicted=1/np.pi + np.pi/4, dev=g/tot - 1, pass_=abs(g/tot - 1) < 0.02)
avals = np.linspace(0.1, 2.0, 41); totals = avals + 1/(4*avals)
sims = {a: simulate(a)[0]/EG for a in (0.25, 0.5, 1.0)}
out['P1'] = dict(a_min=float(avals[np.argmin(totals)]), total_min=float(totals.min()), simulated=sims,
                 pass_=abs(totals.min() - 1) < 1e-3 and all(abs(sims[a]/(a + 1/(4*a)) - 1) < 0.02 for a in sims))
f = 1/np.pi + np.pi/4
out['P2'] = dict(R0_bound_t156_kernels_A=0.54*f**(1/3), R0_bound_least_decoherence_A=0.54, pass_=abs(0.54*f**(1/3) - 0.558) < 0.002)
out['P3'] = dict(bohr_signal_over_bound_t156=f*(0.54/0.529177)**3, bohr_signal_over_bound_PLD=(0.54/0.529177)**3,
                 pass_=f*(0.54/0.529177)**3 > 1 and (0.54/0.529177)**3 > 1)
for k, v in out.items(): print(k, v)
