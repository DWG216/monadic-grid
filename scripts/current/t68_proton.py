"""t68: where E6 breaks, and the coloured triplets, against proton decay. Pre-registration: PREDICTIONS_t68.md."""
import numpy as np, itertools, math, io, contextlib
from collections import Counter
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(__file__.replace('t68_proton.py', 't66_lib.py')).read())
out = {}
SK = 2.4e34; YR = 3.156e7; S = 1/6.582e-25; MP = 0.938; MPL = 1.22e19
def mbound(c, tau=SK): return (tau*YR*S * c**2 * MP**5)**0.25
out['S1'] = dict(M_bound_alpha_1_40=f'{mbound(1/40):.2e}', pass_=1e15 <= mbound(1/40) <= 10**16.5)

# colour SU(3) from t66 (best fit): arm C, simple roots arm_roots[C]
beta = [rootvec(x) for x in arm_roots[C]]
def col_labels_root(a): return [int(np.array(a) @ Acart @ b) for b in beta]
def triality(lbl): return (lbl[0] + 2*lbl[1]) % 3
fixed = [a for a in roots if a[3] % 3 == 0]; rest = [a for a in roots if a[3] % 3 != 0]
tf = Counter(triality(col_labels_root(a)) != 0 for a in fixed); tr = Counter(triality(col_labels_root(a)) != 0 for a in rest)
out['G1'] = dict(fixed_dim=len(fixed)+6, fixed_coloured_triplets=tf[True], rest=len(rest), rest_coloured_triplets=tr[True],
                 pass_=len(fixed)+6 == 24 and tf[True] == 0 and len(rest) == 54 and tr[True] == 54)

# G2: Dynkin index of the 27 for each SU(3) arm: T = sum_w <w, alpha>^2 / 4 for a root alpha of the factor
def index(arm):
    a = rootvec(arm_roots[arm][0]); return sum(int(l @ a)**2 for l in W)/4
T = [index(k) for k in range(3)]
out['G2'] = dict(T_C_L_R=T, b_formula='b = -11 + (2/3) T n_Weyl27 + (1/3) T n_Higgs27', pass_=len(set(T)) == 1)

# G3: bound on E6 bosons with alpha^-1 = 42.4 (t66 G7)
M6 = mbound(1/42.4)
out['G3'] = dict(M_E6_min_GeV=f'{M6:.2e}', in_expected=1e15 <= M6 <= 10**16.5, pass_=M6 < MPL)

# G4: cubic invariant of the 27
col = lambda l: kind(armlabels[C](l))
isD = lambda i: col(W[i]) in ('3', '3b') and T3[i] == 0 and abs(abs(Y[i]) - 1/3) < 1e-9 and abs(Q[i]) - 1/3 < 1e-9
trip = [t for t in itertools.combinations(range(27), 3) if not np.any(W[t[0]] + W[t[1]] + W[t[2]])]
ncol = Counter(sum(col(W[i]) != '1' for i in t) for t in trip)
withD = lambda t: any(isD(i) for i in t)
diq = [t for t in trip if all(col(W[i]) != '1' for i in t) and withD(t)]
lq = [t for t in trip if sum(col(W[i]) != '1' for i in t) == 2 and withD(t)]
out['G4'] = dict(n_terms=len(trip), by_number_of_coloured_fields=dict(sorted(ncol.items())),
                 diquark_terms_with_Y_1_3_triplet=len(diq), leptoquark_terms_with_Y_1_3_triplet=len(lq),
                 pass_=len(trip) == 45 and len(diq) > 0 and len(lq) > 0)

# G5: coloured triplet scalars with first-generation Yukawas
v = 246.0; yy = lambda m: math.sqrt(2)*m/v
yu, yd, ye = yy(2.16e-3), yy(4.67e-3), yy(0.511e-3)
MTud = mbound(yu*yd); MTue = mbound(yu*ye)
out['G5'] = dict(MT_min_yu_yd=f'{MTud:.2e}', MT_min_yu_ye=f'{MTue:.2e}', pass_=MTud < 1e13 and MTue < 1e13)

# controls
fixedC1 = [a for a in roots if a[0] % 3 == 0]
out['C1'] = dict(fixed_dim=len(fixedC1)+6, coloured_triplets=sum(triality(col_labels_root(a)) != 0 for a in fixedC1))
out['C1']['pass_'] = out['C1']['coloured_triplets'] > 0
out['C2'] = dict(MT_min_order_one=f'{mbound(1.0):.2e}', pass_=mbound(1.0) > 1e13)
for k, val in out.items(): print(k, val)
