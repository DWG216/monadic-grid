"""t103: candidate rules for the chord phase. Pre-registration: PREDICTIONS_t103.md."""
up = dict(Q=0.889, d=0.0504, s=0.0023); dn = dict(Q=0.741, d=0.1016, s=0.0153)
out = {}
out['P1'] = dict(up_pull=(up['d'] - up['Q']/3)/up['s'], down_pull=(dn['d'] - dn['Q']/3)/dn['s'], pass_=abs(up['d'] - up['Q']/3) <= 3*up['s'] and abs(dn['d'] - dn['Q']/3) <= 3*dn['s'])
out['P2'] = dict(up_pull=(up['d'] - 1/18)/up['s'], down_pull=(dn['d'] - 1/9)/dn['s'], pass_=abs(up['d'] - 1/18) <= 3*up['s'] and abs(dn['d'] - 1/9) <= 3*dn['s'])
for k, v in out.items(): print(k, v)
