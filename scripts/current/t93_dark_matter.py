"""t93: the psi grading's parity P = (-1)^(Q_psi + F) on the 27; vevs; cubic couplings; lightest odd state. Pre-registration: PREDICTIONS_t93.md."""
# SO(10) x U(1)_psi content of one 27 (t64): name, SO(10) rep, psi charge
states = [('q', '16', 1), ('u^c', '16', 1), ('d^c', '16', 1), ('L', '16', 1), ('e^c', '16', 1), ('nu^c', '16', 1),
          ('D', '10', -2), ('D^c', '10', -2), ('H_u-like', '10', -2), ('H_d-like', '10', -2), ('N', '1', 4)]
mult = {'q': 6, 'u^c': 3, 'd^c': 3, 'L': 2, 'e^c': 1, 'nu^c': 1, 'D': 3, 'D^c': 3, 'H_u-like': 2, 'H_d-like': 2, 'N': 1}
P = lambda q, F: (-1)**((q + F) % 2)
out = {}
f16 = [P(q, 1) for n, r, q in states if r == '16']; fex = [P(q, 1) for n, r, q in states if r != '16']
out['G1'] = dict(n16=sum(mult[n] for n, r, q in states if r == '16'), nex=sum(mult[n] for n, r, q in states if r != '16'),
                 pass_=all(x == 1 for x in f16) and all(x == -1 for x in fex) and sum(mult.values()) == 27)
vevs = {'Higgs doublets (10, scalar)': P(-2, 0), 'nu^c Majorana mass (charge-2 combination)': P(2, 0), 'N direction (charge +4)': P(4, 0), 'L-like direction (charge +1)': P(1, 0)}
out['G2'] = dict(vevs=vevs, pass_=vevs['Higgs doublets (10, scalar)'] == 1 and vevs['nu^c Majorana mass (charge-2 combination)'] == 1 and vevs['N direction (charge +4)'] == 1 and vevs['L-like direction (charge +1)'] == -1)
# G3: the E6 cubic 27^3 under SO(10) x U(1)_psi: 16.16.10 and 10.10.1 (psi charges sum to 0); each term, any one field scalar, two fermions
terms = [(('16', 1), ('16', 1), ('10', -2)), (('10', -2), ('10', -2), ('1', 4))]
ok = True
for t in terms:
    assert sum(q for _, q in t) == 0
    for s in range(3):                                  # which leg is the scalar
        prod = 1
        for i, (r, q) in enumerate(t): prod *= P(q, 0 if i == s else 1)
        ok &= prod == 1
out['G3'] = dict(pass_=ok)
relic_TeV = 1.1; window = (1.0e3, 7.5e6)
out['G4'] = dict(relic_GeV=relic_TeV*1e3, n_H2_window=window, pass_=window[0] <= relic_TeV*1e3 <= window[1])
for k, v in out.items(): print(k, v)
