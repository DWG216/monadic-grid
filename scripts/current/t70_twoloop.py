"""t70: the t67 coupling meeting at two loops. Pre-registration: PREDICTIONS_t70.md (written before this code)."""
import numpy as np, math
MZ = 91.1876; A0 = np.array([59.0, 29.6, 8.47]); YT0 = 0.99
B_SM = np.array([41/10, -19/6, -7.0])
BIJ_SM = np.array([[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, -26]])
CY = np.array([17/10, 3/2, 2.0]); C2G = np.array([0, 2.0, 3.0])
def weyl(Y, d2, d3):
    """S2, C2 vectors (U1 GUT-norm, SU2, SU3) for one Weyl multiplet (d2, d3 = 1, 2 or 3; 3 means triplet)."""
    dim = d2*d3
    S2 = np.array([(3/5)*Y**2*dim, 0.5*d3 if d2 == 2 else 0, 0.5*d2 if d3 == 3 else 0])
    C2 = np.array([(3/5)*Y**2, 0.75 if d2 == 2 else 0, 4/3 if d3 == 3 else 0])
    return S2, C2
def db1(F): S2, C2 = F; return (2/3)*S2
def db2(F): S2, C2 = F; return 2*np.outer(S2, C2) + np.diag((10/3)*C2G*S2)
D, Dc, H, Hb = weyl(1/3, 1, 3), weyl(1/3, 1, 3), weyl(1/2, 2, 1), weyl(1/2, 2, 1)
DB_D, DB_H = db1(D)+db1(Dc), db1(H)+db1(Hb)
DBB_D, DBB_H = db2(D)+db2(Dc), db2(H)+db2(Hb)
res = {}
# S2: formula check on SM fermions (3 generations)
gen = [weyl(1/6, 2, 3), weyl(2/3, 1, 3), weyl(1/3, 1, 3), weyl(1/2, 2, 1), weyl(1, 1, 1)]
F2 = 3*sum(db2(F) for F in gen)
res['S2'] = dict(b33_fermions=round(F2[2, 2], 6), b12_fermions=round(F2[0, 1], 6), pass_=abs(F2[2, 2]-76) < 1e-9 and abs(F2[0, 1]-9/5) < 1e-9)

T = np.linspace(math.log(MZ), math.log(1e19), 6000); DT = T[1]-T[0]
def scan(cfg, twoloop=True):
    """cfg: arrays tH, tD (log thresholds), kH, kD (multiples of the H-pair and D-pair shifts at tH), mD_H (H pairs at tD)."""
    tH, tD, nH_light, nH_heavy, nD = cfg
    N = tH.size; a = np.tile(A0, (N, 1)); y = np.full(N, YT0)
    best = np.full(N, np.inf); bestT = np.zeros(N); bestA = np.zeros(N)
    def coeffs(t0):
        wH = np.clip((t0+DT-tH)/DT, 0, 1)[:, None]; wD = np.clip((t0+DT-tD)/DT, 0, 1)[:, None]
        b = B_SM + wH*nH_light[:, None]*DB_H + wD*(nH_heavy[:, None]*DB_H + nD[:, None]*DB_D)
        bij = BIJ_SM + wH[:, :, None]*nH_light[:, None, None]*DBB_H + wD[:, :, None]*(nH_heavy[:, None, None]*DBB_H + nD[:, None, None]*DBB_D)
        return b, bij
    def rhs(a, y, b, bij):
        al = 1/a
        da = -b/(2*math.pi)
        if twoloop:
            da = da - np.einsum('nij,nj->ni', bij, al)/(8*math.pi**2) + CY*(y**2)[:, None]/(32*math.pi**3)
        g2 = 4*math.pi*al
        dy = y/(16*math.pi**2)*(4.5*y**2 - 8*g2[:, 2] - 2.25*g2[:, 1] - 0.85*g2[:, 0]) if twoloop else 0*y
        return da, dy
    for k in range(T.size):
        s = a.max(1)-a.min(1); better = s < best
        best = np.where(better, s, best); bestT = np.where(better, T[k], bestT); bestA = np.where(better, a.mean(1), bestA)
        if k == T.size-1: break
        b, bij = coeffs(T[k])
        k1a, k1y = rhs(a, y, b, bij)
        k2a, k2y = rhs(a+0.5*DT*k1a, y+0.5*DT*k1y, b, bij)
        a = a + DT*k2a; y = y + DT*k2y
    return best, np.exp(bestT), bestA

grid = np.logspace(3, 16, 105); gD = grid[grid >= 5.5e11]
rows = [(nH, MH, MD) for nH in (1, 2, 3) for MH in grid for MD in gD]
nH = np.array([r[0] for r in rows], float); MH = np.array([r[1] for r in rows]); MDv = np.array([r[2] for r in rows])
cfg = (np.log(MH), np.log(MDv), nH, 3-nH, np.full(nH.size, 3.0))
def summarise(sp, M3, ain):
    hit = sp < 0.5; out = dict(n_meetings=int(hit.sum()))
    if hit.any():
        for n in (1, 2, 3):
            m = hit & (nH == n)
            out[f'nH{n}'] = dict(count=int(m.sum()), MH=(f'{MH[m].min():.1e}', f'{MH[m].max():.1e}') if m.any() else None)
        out['M3'] = (f'{M3[hit].min():.1e}', f'{M3[hit].max():.1e}'); out['ainv'] = (round(ain[hit].min(), 1), round(ain[hit].max(), 1))
        j = int(np.argmin(np.where(hit, sp, np.inf)))
        out['best'] = dict(nH=int(nH[j]), MH=f'{MH[j]:.2e}', MD=f'{MDv[j]:.2e}', spread=round(sp[j], 3), M3=f'{M3[j]:.2e}', ainv=round(ain[j], 1))
    return out, hit
s1, m1, a1 = scan(cfg, twoloop=False); r1, h1 = summarise(s1, m1, a1)
res['S1'] = dict(**r1, pass_=r1['n_meetings'] == 1108 and r1.get('M3') == ('4.1e+13', '6.1e+13'))
s2, m2, a2 = scan(cfg, twoloop=True); r2, h2 = summarise(s2, m2, a2)
res['G1'] = dict(**r2, pass_=r2['n_meetings'] > 0 and r2.get('nH1', {}).get('count', 0) == 0 and bool(np.all(MH[h2] < MDv[h2])))
res['G2'] = dict(pass_=bool(h2.any() and np.all((m2[h2] >= 1e13) & (m2[h2] <= 1e17) & (a2[h2] >= 30) & (a2[h2] <= 45))))
res['G3'] = dict(max_MH=f'{MH[h2].max():.1e}' if h2.any() else None, pass_=bool(h2.any() and MH[h2].max() <= 2e8))
if h2.any():
    j1 = int(np.argmin(np.where(h1, s1, np.inf))); j2 = int(np.argmin(np.where(h2, s2, np.inf)))
    res['G4'] = dict(M3_one_loop=f'{m1[j1]:.2e}', M3_two_loop=f'{m2[j2]:.2e}', ratio=round(m2[j2]/m1[j1], 2))
# controls
one = np.array([1.0]); z = np.array([0.0])
c1, _, _ = scan((np.array([99.0]), np.array([99.0]), z, z, z)); 
cm = scan((np.log(grid), np.log(grid), np.zeros(grid.size), np.full(grid.size, 3.0), np.full(grid.size, 3.0)))[0]
res['C1'] = dict(spread=round(float(c1[0]), 2), pass_=bool(c1[0] > 0.5))
res['C2'] = dict(min_spread=round(float(cm.min()), 2), pass_=bool(cm.min() > 0.5))
for k, v in res.items(): print(k, v)
