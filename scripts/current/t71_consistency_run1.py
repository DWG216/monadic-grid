"""t71: do posts 30, 62 and 64 agree? Pre-registration: PREDICTIONS_t71.md (written before this code)."""
import numpy as np, math, io, contextlib, itertools
from collections import Counter
here = __file__.rsplit('/', 1)[0] + '/'
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(here + 't66_lib.py').read())
out = {}
SK = 2.4e34; YR = 3.156e7; S = 1/6.582e-25; MP = 0.938; MPL = 1.22e19
def mbound(alpha): return (SK*YR*S * alpha**2 * MP**5)**0.25

# t70 two-loop meetings (same code, same grid)
src = open(here + 't70_twoloop.py').read().split('s1, m1, a1 = scan')[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(src)
sp, M3, AIN = scan(cfg, twoloop=True); hit = sp < 0.5
j = int(np.argmin(np.where(hit, sp, np.inf)))
out['S1'] = dict(M_E6_min_at_42_4=f'{mbound(1/42.4):.3e}', best_M3=f'{M3[j]:.3e}', best_ainv=round(AIN[j], 2),
                 pass_=abs(mbound(1/42.4)/4.64e15-1) < 0.01 and abs(M3[j]/4.48e13-1) < 0.01 and abs(AIN[j]-38.8) < 0.05)
M3max = M3[hit].max(); a3 = AIN[j]

# G1: E6 bound with alpha run above M3 (b = -5 + n_h), solving M = mbound(alpha(M))
g1 = {}
for nh in range(4):
    b = -5 + nh; M = 4.6e15
    for _ in range(50):
        ainv = a3 - b/(2*math.pi)*math.log(M/M3[j]); M = mbound(1/ainv)
    g1[nh] = dict(ainv_at_M=round(ainv, 2), M_E6_min=f'{M:.3e}', ratio=round(M/4.64e15, 3))
out['G1'] = dict(by_n_h=g1, pass_=all(1/1.1 <= v['ratio'] <= 1.1 for v in g1.values()) and all(float(v['M_E6_min']) < MPL for v in g1.values()))

# G2a: U(1)_psi in the Cartan of SU(3)_L x SU(3)_R
Ainv = np.linalg.inv(Acart.astype(float))
armvec = [[np.eye(6)[0], np.eye(6)[2]], [np.eye(6)[4], np.eye(6)[5]], [np.eye(6)[1], -np.array(marks, float)]]
Wm = np.array(W, float)
g2a = {}
for node in range(6):
    f = Ainv[node]                    # coweight: f(l) = (A^-1 l)_node
    vals = Counter(np.round(Wm @ f, 6))
    if sorted(vals.values()) != [1, 10, 16]: continue
    basis = np.array([v for arm in armvec for v in arm])          # rows: C?, by arm index 0,1,2
    coef = np.linalg.solve(basis.T, f).reshape(3, 2)
    LR = [k for k in range(3) if k != C]
    fit_LR = np.linalg.lstsq(np.array([v for k in LR for v in armvec[k]]).T, f, rcond=None)
    res_LR = float(np.abs(np.array([v for k in LR for v in armvec[k]]).T @ fit_LR[0] - f).max())
    fit_C = np.linalg.lstsq(np.array(armvec[C]).T, f, rcond=None)
    res_C = float(np.abs(np.array(armvec[C]).T @ fit_C[0] - f).max())
    # psi charges normalised: singlet -> 4
    v1 = [k for k, n in vals.items() if n == 1][0]; v10 = [k for k, n in vals.items() if n == 10][0]; v16 = [k for k, n in vals.items() if n == 16][0]
    shift = (v1 + 2*v10 + 0)  # not used
    ratio = (v16 - v10)/(v1 - v10)
    g2a[node] = dict(values={str(k): n for k, n in vals.items()}, colour_coeffs=np.round(coef[C], 9).tolist(),
                     residual_LR_only=res_LR, residual_C_only=round(res_C, 4))
psi_nodes = [n for n, v in g2a.items() if v['residual_LR_only'] < 1e-9]
out['G2a'] = dict(candidates=g2a, psi_nodes_inside_LR=psi_nodes, pass_=len(psi_nodes) >= 1)
out['C1'] = dict(residual_C_only=[v['residual_C_only'] for v in g2a.values()], pass_=all(v['residual_C_only'] > 0.1 for v in g2a.values()))

# G2: Z'_psi vs M3
g = math.sqrt(4*math.pi/a3)
MR3_high, MR3_pole = 1.28e14, 5.94e14
out['G2'] = dict(g=round(g, 3), M3_max=f'{M3max:.2e}', gMR3_high=f'{g*MR3_high:.2e}', ratio_high=round(g*MR3_high/M3max, 2),
                 pass_=g*MR3_high <= 3*M3max)
out['C2'] = dict(gMR3_pole=f'{g*MR3_pole:.2e}', ratio_pole=round(g*MR3_pole/M3max, 2), pass_=g*MR3_pole > g*MR3_high)

# G3: triplets between the proton bound and the breaking scale
gm = np.sqrt(4*np.pi/AIN)
ok = hit & (MDv >= 5.5e11) & (MDv <= M3/gm)
win = {}
for n in (2, 3):
    m = ok & (nH == n)
    win[n] = dict(count=int(m.sum()), MH=(f'{MH[m].min():.1e}', f'{MH[m].max():.1e}') if m.any() else None,
                  MD=(f'{MDv[m].min():.1e}', f'{MDv[m].max():.1e}') if m.any() else None)
out['G3'] = dict(meetings=int(hit.sum()), with_triplets_inside=int(ok.sum()), above_breaking=int((hit & (MDv > M3/gm)).sum()),
                 windows=win, M3=(f'{M3[ok].min():.1e}', f'{M3[ok].max():.1e}') if ok.any() else None, pass_=bool(ok.any()))
for k, v in out.items(): print(k, v)
