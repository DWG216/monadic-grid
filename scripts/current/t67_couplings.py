"""t67: do the couplings meet with the E6 extras as thresholds? Pre-registration: PREDICTIONS_t67.md (written before this code)."""
import numpy as np, math
MZ = 91.1876
A0 = np.array([59.0, 29.6, 8.47])            # alpha_i^-1 at MZ, alpha_1 GUT-normalised (as t66)
B_SM = np.array([41/10, -19/6, -7.0])
def weyl(dimC, dimL, Y, T3, T2):              # Delta b from one Weyl multiplet: (2/3) T(R) per SU(N), (2/3)(3/5) Y^2 * dim for U(1)
    return np.array([(2/3)*(3/5)*Y**2*dimC*dimL, (2/3)*T2*dimC, (2/3)*T3*dimL])
DB_D = weyl(3, 1, 1/3, 0.5, 0) + weyl(3, 1, 1/3, 0.5, 0)      # D + D^c (one generation)
DB_H = weyl(1, 2, 1/2, 0, 0.5) + weyl(1, 2, 1/2, 0, 0.5)      # H + Hbar (one generation)
LMU = np.linspace(math.log(MZ), math.log(1e19), 6000)

def run(thresholds):
    """thresholds: list of (mass, delta_b). Returns alpha^-1 on LMU grid, shape (3, N)."""
    out = np.empty((3, LMU.size)); a = A0.copy(); b = B_SM.copy(); lm = math.log(MZ)
    th = sorted([(math.log(m), db) for m, db in thresholds], key=lambda x: x[0]); k = 0
    for j, L in enumerate(LMU):
        while k < len(th) and th[k][0] <= L:
            a = a - b/(2*math.pi)*(th[k][0]-lm); lm = th[k][0]; b = b + th[k][1]; k += 1
        out[:, j] = a - b/(2*math.pi)*(L-lm)
    return out

def meet(alpha):
    spread = alpha.max(0) - alpha.min(0); j = int(np.argmin(spread))
    return spread[j], math.exp(LMU[j]), alpha[:, j].mean()

res = {}
# S1: SM alone
al = run([]); d12 = al[0]-al[1]; j = int(np.argmin(np.abs(d12)))
res['S1'] = dict(M12=f'{math.exp(LMU[j]):.2e}', a12=round(al[0, j], 1), a3=round(al[2, j], 1), best_spread=round(meet(al)[0], 2),
                 pass_=abs(math.log10(math.exp(LMU[j]))-13) < 0.15 and meet(al)[0] > 0.5)
# G1: one 27's extras beyond the 16 = complete 5 + 5bar
db = DB_D + DB_H
res['G1'] = dict(DB_D=np.round(DB_D, 4).tolist(), DB_H=np.round(DB_H, 4).tolist(), sum=np.round(db, 4).tolist(), pass_=bool(np.allclose(db, db[0])))
# G2-G4: split thresholds
grid = np.logspace(3, 16, 105)
hits = []
for nH in (1, 2, 3):
    for MH in grid:
        for MD in grid[grid >= 5.5e11]:
            th = [(MH, nH*DB_H), (MD, 3*DB_D + (3-nH)*DB_H)]
            s, M3, ainv = meet(run(th))
            if s < 0.5: hits.append((nH, MH, MD, s, M3, ainv))
hits_arr = hits
res['G2'] = dict(n_meetings=len(hits), all_MH_below_MD=all(h[1] < h[2] for h in hits), pass_=len(hits) > 0 and all(h[1] < h[2] for h in hits))
if hits:
    best = min(hits, key=lambda h: h[3])
    res['G2']['best'] = dict(nH=best[0], MH=f'{best[1]:.2e}', MD=f'{best[2]:.2e}', spread=round(best[3], 3), M3=f'{best[4]:.2e}', alpha_inv=round(best[5], 1))
    byn = {n: [h for h in hits if h[0] == n] for n in (1, 2, 3)}
    res['G2']['by_nH'] = {n: dict(count=len(v), MH_range=(f'{min(h[1] for h in v):.1e}', f'{max(h[1] for h in v):.1e}') if v else None,
                               MD_range=(f'{min(h[2] for h in v):.1e}', f'{max(h[2] for h in v):.1e}') if v else None) for n, v in byn.items()}
    res['G3'] = dict(M3_range=(f'{min(h[4] for h in hits):.1e}', f'{max(h[4] for h in hits):.1e}'),
                     ainv_range=(round(min(h[5] for h in hits), 1), round(max(h[5] for h in hits), 1)),
                     pass_=all(1e13 <= h[4] <= 1e17 and 30 <= h[5] <= 45 for h in hits))
    res['G4'] = dict(max_MH=f'{max(h[1] for h in hits):.1e}', pass_=all(h[1] <= 1e10 for h in hits))
else:
    res['G3'] = res['G4'] = dict(pass_=False, note='no meetings')
# C2: all extras at one common mass
c2 = [meet(run([(M, 3*(DB_D+DB_H))]))[0] for M in grid]
res['C2'] = dict(min_spread=round(min(c2), 2), sm_spread=round(meet(al)[0], 2), pass_=min(c2) > 0.5)
# C3: light triplets (MD < MH)
c3 = []
for nH in (1, 2, 3):
    for MD in grid:
        for MH in grid[grid > MD]:
            th = [(MD, 3*DB_D), (MH, 3*DB_H)]
            s, M3, ainv = meet(run(th))
            if s < 0.5: c3.append((nH, MD, MH, s, M3))
res['C3'] = dict(n_meetings=len(c3), with_MD_above_bound=sum(1 for c in c3 if c[1] >= 5.5e11),
                 pass_=all(c[1] < 5.5e11 for c in c3))
for k, v in res.items(): print(k, v)
