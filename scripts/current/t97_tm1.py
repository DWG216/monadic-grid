"""t97: which S4 Z2 generates S4 with the counting-phase Z3; TM1 predictions. Pre-registration: PREDICTIONS_t97.md."""
import numpy as np, itertools
src = open(__file__.replace('t97_tm1.py', 't96_flavour.py')).read(); ns = {}; exec(src[:src.index('# P1: critical axes')], ns)
A4 = ns['A4']
def closure(gens):
    G = [np.eye(3)]; frontier = [np.eye(3)]
    while frontier:
        g = frontier.pop()
        for h in gens:
            k = np.round(g @ h, 9)
            if not any(np.allclose(k, x) for x in G): G.append(k); frontier.append(k)
    return G
T = np.roll(np.eye(3), 1, axis=0)                              # cyclic permutation: the counting phase, axis (1,1,1)
assert any(np.allclose(T, R) for R in A4)
S = np.diag([1., -1., -1.])
out = {'S1': dict(order=len(closure([T, S])), pass_=len(closure([T, S])) == 12)}
def rot_pi(ax):
    a = np.array(ax, float); a /= np.linalg.norm(a); return 2*np.outer(a, a) - np.eye(3)
edges = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
S4 = closure(A4 + [rot_pi(e) for e in edges])
res = []
for e in edges:
    U = rot_pi(e); n = len(closure([T, U])); orth = abs(np.dot(e, (1, 1, 1))) < 1e-12
    res.append(dict(axis=e, generated=n, orthogonal_to_T_axis=orth))
gen_full = [r for r in res if r['generated'] == 24]
out['P1'] = dict(S4_order=len(S4), table=res, pass_=len(S4) == 24 and all((r['generated'] == 24) == (not r['orthogonal_to_T_axis']) for r in res)
                 and all(r['generated'] == 6 for r in res if r['orthogonal_to_T_axis']))
w = np.exp(2j*np.pi/3); F = np.array([[w**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
cols = [np.round(sorted(np.abs(F.conj() @ (np.array(r['axis'])/np.linalg.norm(r['axis'])))**2, reverse=True), 6).tolist() for r in gen_full]
out['P2'] = dict(columns=cols, pass_=all(np.allclose(c, [2/3, 1/6, 1/6]) for c in cols))
s13 = 0.02215; s12 = 1 - 2/(3*(1 - s13))
out['P3'] = dict(sin2_12=s12, pull_JUNO=(s12 - 0.3092)/0.0087, pass_=abs(s12 - 0.3092) <= 2*0.0087)
def cosd(s23):
    t23 = np.arcsin(np.sqrt(s23)); return -(1 - 5*s13)*(1/np.tan(2*t23))/(2*np.sqrt(2)*np.sqrt(s13)*np.sqrt(1 - 3*s13))
grid = np.linspace(0.455, 0.573, 200); cs = [cosd(x) for x in grid]
out['P4'] = dict(cos_delta_range=[float(min(cs)), float(max(cs))], pass_=all(abs(c) <= 1 for c in cs))
out['info'] = {f's23={x}': [round(float(np.degrees(np.arccos(cosd(x)))), 1), round(float(360 - np.degrees(np.arccos(cosd(x)))), 1)] for x in (0.470, 0.5, 0.561)}
for k, v in out.items(): print(k, v)
