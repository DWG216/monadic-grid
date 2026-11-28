"""t183: the Tonnetz as the A2 lattice; P, L, R as the hand swap. Pre-registration: PREDICTIONS_t183.md."""
import itertools
pc = lambda a, b: (7*a + 4*b) % 12
ker = [(a, b) for a in range(-12, 13) for b in range(-12, 13) if pc(a, b) == 0]
gen_ok = all(any((a, b) == (4*i, -i + 3*j) for i in range(-12, 13) for j in range(-12, 13)) for a, b in ker)
tri = set()
for a in range(12):
    for b in range(12):
        tri.add(('up', frozenset({pc(a, b), pc(a + 1, b), pc(a, b + 1)})))
        tri.add(('down', frozenset({pc(a + 1, b), pc(a, b + 1), pc(a + 1, b + 1)})))
major = {frozenset({r, (r + 4) % 12, (r + 7) % 12}) for r in range(12)}
minor = {frozenset({r, (r + 3) % 12, (r + 7) % 12}) for r in range(12)}
ups = {t for o, t in tri if o == 'up'}; downs = {t for o, t in tri if o == 'down'}
P1 = gen_ok and len({pc(a, b) for a in range(12) for b in range(12)}) == 12 and len(tri) == 24 and ups == major and downs == minor
print('P1', dict(kernel_generated_by_04m1_03=gen_ok, triangles=len(tri), up_is_major=ups == major, down_is_minor=downs == minor, pass_=P1))
triads = sorted(major | minor, key=lambda s: sorted(s)); idx = {t: i for i, t in enumerate(triads)}
def move(ic):
    perm = []
    for t in triads:
        edge = [e for e in itertools.combinations(t, 2) if min((e[0] - e[1]) % 12, (e[1] - e[0]) % 12) == ic][0]
        other = [u for u in triads if u != t and set(edge) <= u]
        assert len(other) == 1; perm.append(idx[other[0]])
    return tuple(perm)
P, R, L = move(5), move(4), move(3)          # shared fifth, major third, minor third
isM = [t in major for t in triads]
def comp(p, q): return tuple(p[i] for i in q)  # apply q then p
ident = tuple(range(24)); G = {ident}; fr = [ident]
while fr:
    new = []
    for g in fr:
        for h in (P, L, R):
            x = comp(h, g)
            if x not in G: G.add(x); new.append(x)
    fr = new
def order(g):
    k, x = 1, g
    while x != ident: x = comp(g, x); k += 1
    return k
invol = all(comp(m, m) == ident for m in (P, L, R))
flips = all(all(isM[i] != isM[m[i]] for i in range(24)) for m in (P, L, R))
P2 = invol and flips and len(G) == 24 and max(order(g) for g in G) == 12
print('P2', dict(involutions=invol, each_flips_major_minor=flips, group_order=len(G), max_element_order=max(order(g) for g in G), pass_=P2))
def root_q(t):
    for r in range(12):
        if t == frozenset({r, (r + 4) % 12, (r + 7) % 12}): return r, 'M'
        if t == frozenset({r, (r + 3) % 12, (r + 7) % 12}): return r, 'm'
pres = [g for g in G if all(isM[i] == isM[g[i]] for i in range(24))]
rev = [g for g in G if all(isM[i] != isM[g[i]] for i in range(24))]
def is_transposition(g):
    shifts = {(root_q(triads[g[i]])[0] - root_q(triads[i])[0]) % 12 for i in range(24)}
    return len(shifts) == 1
P3 = len(pres) == 12 and all(is_transposition(g) for g in pres) and len(rev) == 12 and len(pres) + len(rev) == 24
print('P3', dict(orientation_preserving=len(pres), all_transpositions=all(is_transposition(g) for g in pres), orientation_reversing=len(rev), pass_=P3))
