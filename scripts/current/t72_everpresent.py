"""t72: everpresent Lambda against DESI DR2. Pre-registration: PREDICTIONS_t72.md (written before this code)."""
import numpy as np, math
OM = 0.31; AI = 1e-3; DL = 2e-4; NR = 20000
lna = np.arange(math.log(AI), DL/2, DL); a_grid = np.exp(lna)
fitmask = a_grid >= 1/3
X = np.column_stack([np.ones(fitmask.sum()), -3*np.log(a_grid[fitmask]), -3*(np.log(a_grid[fitmask]) + 1 - a_grid[fitmask])])
def cpl_fit(lnrho):
    """lnrho rows over a in [1/3, 1]; model ln rho0 - 3(1+w0) ln a - 3 wa (ln a + 1 - a)."""
    c, *_ = np.linalg.lstsq(X, lnrho.T, rcond=None)
    return c[1]-1, c[2]                       # w0, wa
out = {}
# S1: constant Lambda
lnr = np.full((1, fitmask.sum()), math.log(2.0)); w0, wa = cpl_fit(lnr)
out['S1'] = dict(w0=float(w0[0]), wa=float(wa[0]), pass_=abs(w0[0]+1) < 1e-6 and abs(wa[0]) < 1e-6)
# S2: synthetic CPL
af = a_grid[fitmask]; lnr = (-3*(1-0.42-1.75)*np.log(af) - 3*(-1.75)*(1-af))[None]
w0, wa = cpl_fit(lnr)
out['S2'] = dict(w0=float(w0[0]), wa=float(wa[0]), pass_=abs(w0[0]+0.42) < 1e-6 and abs(wa[0]+1.75) < 1e-6)

def run(alpha, seed=72):
    rng = np.random.default_rng(seed)
    V = np.full(NR, (4*math.pi/3)*OM**-2*AI**6/6); W = rng.normal(0, np.sqrt(V))
    alive = np.ones(NR, bool); rho = np.empty((NR, fitmask.sum())); k_fit = 0
    for k, la in enumerate(lna):
        a = math.exp(la); Lam = alpha*W/V; H2 = OM*a**-3 + Lam/3
        alive &= H2 > 0
        if fitmask[k]: rho[:, k_fit] = Lam/3; k_fit += 1
        if k == lna.size-1: break
        H2s = np.where(alive, H2, 1.0)
        dV = (4*math.pi/3)*H2s**-2*DL
        W = W + np.sqrt(dV)*rng.standard_normal(NR); V = V + dV
    OL0 = np.where(alive, (Lam/3)/np.where(alive, H2, 1), np.nan)
    acc = alive & (OL0 >= 0.65) & (OL0 <= 0.73)
    pos = acc & np.all(rho > 0, axis=1)
    r = dict(alpha=alpha, survived=int(alive.sum()), accepted=int(acc.sum()), acc_rate=float(acc.mean()),
             neg_somewhere_frac=float((acc & ~pos).sum()/max(acc.sum(), 1)), fitted=int(pos.sum()))
    if pos.sum():
        w0, wa = cpl_fit(np.log(rho[pos]))
        box = (np.abs(w0+0.42) <= 0.42) & (np.abs(wa+1.75) <= 1.16)
        sn = (np.abs(w0+0.7) <= 0.42) & (np.abs(wa+1.0) <= 1.16)
        quad = (w0 > -1) & (wa < 0)
        r.update(desi_box=float(box.mean()), quadrant=float(quad.mean()), median_abs_w0p1=float(np.median(np.abs(w0+1))),
                 sn_point_box=float(sn.mean()), w0_med=float(np.median(w0)), wa_med=float(np.median(wa)),
                 w0_16_84=[float(x) for x in np.percentile(w0, [16, 84])], wa_16_84=[float(x) for x in np.percentile(wa, [16, 84])])
        r['_w'] = (w0, wa)
    return r
runs = [run(al) for al in (0.5, 1, 2, 4, 8)]
prim = max(runs, key=lambda r: r['acc_rate'])
for r in runs: print('alpha', {k: v for k, v in r.items() if k != '_w'})
p = prim
out['primary_alpha'] = p['alpha']
if 'desi_box' in p:
    out['P1'] = dict(desi_box=round(p['desi_box'], 4), pass_=p['desi_box'] >= 0.05, refuted=p['desi_box'] < 0.01)
    out['P2'] = dict(median_abs_w0p1=round(p['median_abs_w0p1'], 3), pass_=p['median_abs_w0p1'] > 0.1)
    out['P3'] = dict(quadrant=round(p['quadrant'], 4), pass_=p['quadrant'] >= 0.25)
    np.savez('t72_primary_w.npz', w0=p['_w'][0], wa=p['_w'][1])
for k, v in out.items(): print(k, v)
