"""t91: hypercharge on the cut: Y = a T8_L + b T3_R + c T8_R. Pre-registration: PREDICTIONS_t91.md."""
import numpy as np, itertools
r3 = np.sqrt(3); W3 = [(0.5, 1/(2*r3)), (-0.5, 1/(2*r3)), (0.0, -1/r3)]; W3b = [(-x, -y) for x, y in W3]
out = {}
out['S1'] = dict(pass_=abs(sum(w[0] for w in W3)) < 1e-12 and abs(sum(w[1] for w in W3)) < 1e-12)
# G1: quarks (3, 3bar, 1): L-antitriplet components 0,1 doublet (Q), 2 singlet (D): Y = a T8_L
a = (1/6)/W3b[0][1]; out['G1'] = dict(a=a, D=a*W3b[2][1], pass_=abs(a + 1/r3) < 1e-12 and abs(a*W3b[2][1] + 1/3) < 1e-12)
# G2: antiquarks (3bar, 1, 3): R-triplet; choose which component is u^c
sols = []
for k in range(3):
    tgt = [1/3]*3; tgt[k] = -2/3
    A = np.array([[W3[i][0], W3[i][1]] for i in range(3)]); x, res, *_ = np.linalg.lstsq(A, np.array(tgt), rcond=None)
    if np.max(np.abs(A @ x - tgt)) < 1e-12: sols.append((k, x))
out['G2'] = dict(n=len(sols), sols=[(k, [round(v, 6) for v in x]) for k, x in sols], pass_=len(sols) == 3)
# G3: leptons (1, 3, 3bar): L-triplet i, R-antitriplet j
want = sorted([-0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 1.0, 0.0, 0.0])
g3 = []
for k, (b, c) in sols:
    Ys = [[a*W3[i][1] + b*W3b[j][0] + c*W3b[j][1] for j in range(3)] for i in range(3)]
    ok = sorted(np.round(np.array(Ys).ravel(), 9)) == sorted(np.round(want, 9))
    doublets_consistent = all(abs(Ys[0][j] - Ys[1][j]) < 1e-12 for j in range(3))     # rows 0,1 form SU(2)_L doublets
    g3.append(ok and doublets_consistent)
out['G3'] = dict(each=g3, pass_=all(g3) and len(g3) == 3)
# G4: sin^2 theta_W = Tr T3_L^2 / Tr Q^2 over the 27
g4 = []
for k, (b, c) in sols:
    t3, q = [], []
    for col in range(3):                      # quarks
        for i in range(3): T = W3b[i][0]; Y = a*W3b[i][1]; t3.append(T); q.append(T + Y)
    for col in range(3):                      # antiquarks: SU(2)_L singlets
        for j in range(3): t3.append(0.0); q.append(b*W3[j][0] + c*W3[j][1])
    for i in range(3):                        # leptons
        for j in range(3): T = W3[i][0]; Y = a*W3[i][1] + b*W3b[j][0] + c*W3b[j][1]; t3.append(T); q.append(T + Y)
    g4.append(sum(x*x for x in t3)/sum(x*x for x in q))
out['G4'] = dict(values=g4, pass_=all(abs(v - 3/8) < 1e-12 for v in g4))
for k_, v in out.items(): print(k_, v)
