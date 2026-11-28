"""t188: triads as three voices meeting: D3 = (abc)^(1/3) with the grid's ratios. Pre-registration: PREDICTIONS_t188.md."""
from fractions import Fraction as Fr
from math import gcd, lcm
grid = {0: Fr(1), 1: Fr(16, 15), 2: Fr(9, 8), 3: Fr(6, 5), 4: Fr(5, 4), 5: Fr(4, 3), 6: Fr(25, 18), 7: Fr(3, 2), 8: Fr(8, 5), 9: Fr(5, 3), 10: Fr(9, 5), 11: Fr(15, 8)}
def ints(chord):
    rs = [grid[k] for k in chord]; L = lcm(*[r.denominator for r in rs])
    v = [int(r*L) for r in rs]; g = gcd(*v); return [x//g for x in v]
def D3(chord):
    a, b, c = ints(chord); return (a*b*c)**(1/3)
maj, mnr = ints((0, 4, 7)), ints((0, 3, 7))
mirror = sorted(int(Fr(1, x)*lcm(*maj)) for x in maj)
P1 = maj == [4, 5, 6] and mnr == [10, 12, 15] and sorted(mnr) == sorted(mirror) and D3((0, 4, 7)) < D3((0, 3, 7))
print('P1', dict(major=maj, minor=mnr, undertone_mirror_of_major=mirror, D3_major=round(D3((0, 4, 7)), 3), D3_minor=round(D3((0, 3, 7)), 3), pass_=P1))
six = {'major': (0, 4, 7), 'sus4': (0, 5, 7), 'sus2': (0, 2, 7), 'minor': (0, 3, 7), 'augmented': (0, 4, 8), 'diminished': (0, 3, 6)}
order = sorted(six, key=lambda k: D3(six[k]))
print('P2', dict(order=order, D3={k: round(D3(six[k]), 2) for k in order}, integers={k: ints(six[k]) for k in order},
                 pass_=order == ['major', 'sus4', 'sus2', 'minor', 'augmented', 'diminished']))
P3 = D3(six['major']) < D3(six['minor']) < min(D3(six['augmented']), D3(six['diminished']))
print('P3', dict(major_lt_minor_lt_aug_dim=P3, pass_=P3))
allc = [(0, x, y) for x in range(1, 12) for y in range(x + 1, 12)]
low = [c for c in allc if D3(c) < 5]; ap = [c for c in allc if (lambda v: v[0] + v[2] == 2*v[1])(ints(c))]
print('P4', dict(D3_below_5=[(c, ints(c)) for c in low], arithmetic=[(c, ints(c)) for c in ap], pass_=sorted(low) == sorted(ap)))
top = sorted(allc, key=D3)[:8]
print('reported', dict(eight_most_consonant=[(c, ints(c), round(D3(c), 2)) for c in top]))
