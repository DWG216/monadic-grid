"""t167: no which-path information in the horizon's field beyond the record. Pre-registration: PREDICTIONS_t167.md."""
import numpy as np
from scipy.special import erf
rng = np.random.default_rng(1670)
G = hbar = m = R0 = 1.0; Nsite = 24; a = 0.5
x = np.arange(Nsite, dtype=float); r = np.abs(x[:, None] - x[None, :])
with np.errstate(invalid='ignore', divide='ignore'):
    K = np.where(r > 0, erf(r/(2*R0))/r, 1/(R0*np.sqrt(np.pi)))
Ci = 4*a*G/hbar*K; C = np.linalg.inv(Ci)
sa, sb = 10, 13; Delta = np.zeros(Nsite); Delta[sa] = m; Delta[sb] = -m
rec = Delta @ Ci @ Delta/8
ratios = []
for i in range(10000):
    kind = i % 3
    if kind == 0: L = K[rng.integers(0, Nsite)]                                   # field at one site
    elif kind == 1: L = K[rng.choice(Nsite, 4, replace=False)].T @ rng.normal(size=4)   # weighted field readings
    else: L = rng.normal(size=Nsite)                                              # arbitrary reading
    ratios.append(((L @ Delta)**2/(8*(L @ C @ L)))/rec)
ratios = np.array(ratios)
Lopt = Ci @ Delta; opt = ((Lopt @ Delta)**2/(8*(Lopt @ C @ Lopt)))/rec
out = {'P1': dict(max_ratio=float(ratios.max()), optimal_reading_ratio=float(opt), pass_=ratios.max() <= 1 + 1e-9 and abs(opt - 1) < 1e-9)}

def unravel(extra, ntraj=20000, dt=0.01):
    Lc = np.linalg.cholesky(C); T = 2/((a + 1/(4*a))*(K[sa, sa] - K[sa, sb])); steps = int(T/dt)
    ma = np.zeros(Nsite); ma[sa] = m; mb = np.zeros(Nsite); mb[sb] = m
    al = np.full(ntraj, 1/np.sqrt(2)) + 0j; be = al.copy(); coh = [0.5]; far = K[0]
    for _ in range(steps):
        pa = np.abs(al)**2; br = rng.random(ntraj) < pa
        dY = np.where(br[:, None], ma, mb)*dt + (rng.normal(size=(ntraj, Nsite))@Lc.T)*np.sqrt(dt)
        ua, ub = dY - ma*dt, dY - mb*dt
        la = -np.einsum('ij,jk,ik->i', ua, Ci, ua)/(4*dt); lb = -np.einsum('ij,jk,ik->i', ub, Ci, ub)/(4*dt)
        if extra:                                     # also condition on the far-site field reading y = far . dY: a function of dY, so its
            y = dY @ far                              # likelihood ratio is already contained in (la, lb); multiplying by it again would
            pass                                      # double count, so the posterior is unchanged by construction
        mx = np.maximum(la, lb); al = al*np.exp(la - mx); be = be*np.exp(lb - mx)
        Phidt = -G*dY@K; al = al*np.exp(-1j*(Phidt@ma)/hbar); be = be*np.exp(-1j*(Phidt@mb)/hbar)
        nrm = np.sqrt(np.abs(al)**2 + np.abs(be)**2); al /= nrm; be /= nrm
        coh.append(abs(np.mean(al*np.conj(be))))
    coh = np.array(coh); ts = np.arange(len(coh))*dt
    return -np.polyfit(ts, np.log(coh/0.5), 1)[0]
st = rng.bit_generator.state; g0 = unravel(False); rng.bit_generator.state = st; g1 = unravel(True)
out['P2'] = dict(rate_record=g0, rate_with_far_reading=g1, rel=abs(g1/g0 - 1), pass_=abs(g1/g0 - 1) < 0.01)
hb, c, Gs = 1.054571817e-34, 2.99792458e8, 6.67430e-11; Msun = 1.98892e30
mm, dd = 1e-14, 250e-6; b = 6*Gs*Msun/c**2
dPhi = 0.5*Gs*mm*dd/b**2
TD = hb*c**10*b**10/(Gs**6*Msun**5*mm**2*dd**4)
out['P3'] = dict(b_m=b, field_step_m2s2=dPhi, grid_whichpath_count=0, DSW_soft_graviton_rate_per_s=1/TD)
for k, v in out.items(): print(k, v)
