import numpy as np, json
R=25.0                                   # controllable interval range, minutes (10-35)
def cap_interval(sig): return 0.5*np.log2(1+(R**2/12)/sig**2)
windows={'causal window (first spike -> polar body, ~2.5 h)':150,'whole train (-> pronuclei, ~10.5 h)':630}
spacing={'fast (10 min)':10,'typical (22.5 min)':22.5,'slow (35 min)':35}
jit={'optimistic 0.5 min':0.5,'median 2 min':2,'pessimistic 5 min':5}
out={}
for wn,W in windows.items():
    print(wn)
    for sn,s in spacing.items():
        K=int(W//s); row=[]
        for jn,sg in jit.items():
            c=K*cap_interval(sg); row.append(c); out[(wn,sn,jn)]=c
        print('   %-18s spikes %2d | bits: '%(sn,K)+' | '.join('%s %.1f'%(j.split()[0],c) for j,c in zip(jit,row)))
print('control: sigma = R ->', round(cap_interval(R),3),'bits per interval; sigma = 10R ->',round(cap_interval(10*R),4))
print('sperm choice (not addressable, precedes signal): %.1f-%.1f bits'%(np.log2(200),np.log2(500)))
print('demonstrated readout (Ozil 2006: too few / normal / too many oscillation regimes): log2(3) = %.1f bits (generous upper ~ log2(16) = 4)'%np.log2(3))
c=[out[k] for k in out if k[0].startswith('causal')]
print('B1 causal min capacity %.1f bits (need >1)'%min(c))
print('B2 causal >=23 only for:',[ (k[1],k[2]) for k in out if k[0].startswith('causal') and out[k]>=23])
print('B3 whole train, typical spacing, median jitter: %.1f bits (need >23)'%out[('whole train (-> pronuclei, ~10.5 h)','typical (22.5 min)','median 2 min')])
json.dump({str(k):v for k,v in out.items()},open('docking_budget.json','w'))
