import sys,json; sys.argv=['x']
exec(open('bigcode.py').read())
codes={k:design(*k) for k in [(67,2),(97,3),(127,4)]}
for k,c in codes.items():
    es=np.linspace(0.30,0.499,80); good=[e for e in es if out(c,e)[0]<e]
    print('N=%d order %d: threshold %.3f | control eps=0.5 -> out %.6f | eps=0.45 -> %.4f'%(k[0],k[1],max(good) if good else 0.30,out(c,0.5)[0],out(c,0.45)[0]))
def pipeline(step,nq_accept,eps0,goal):
    e=eps0; cost=1; r=0
    while e>goal and r<30:
        eo,p=step(e)
        if eo>=e: return None
        e=eo; cost*=nq_accept(p); r+=1
    return cost,r
f15=lambda e:(35*e**3,1-15*e)      # 15-to-1 leading order (accept ~ 1-15e)
fbk=None
print('\nRaw states per expensive gate, and per full single-qubit rotation (gate counts from Blackman-Stier heuristics):')
rows=[]
for eps0 in [1e-3,1e-2]:
    for goal_exp in [6,10,15]:
        goal=10.**-goal_exp
        nT=7/3*3*goal_exp*np.log2(10); nTau=7/3*3*goal_exp*np.log(10)/np.log(59)
        c15=pipeline(f15,lambda p:15/p,eps0,goal/nT)
        cI={k:pipeline(lambda e,c=c:out(c,e),lambda p,k=k:k[0]/p,eps0,goal/nTau) for k,c in codes.items()}
        best=min((v[0],k) for k,v in cI.items() if v)
        r=(eps0,goal_exp,nT,c15[0],nT*c15[0],nTau,best[0],nTau*best[0],best[1][0])
        rows.append(r)
        print('  raw err %.0e, rotation precision 1e-%d: Clifford+T %3.0f T x %.3g = %.3g | icosahedral %2.0f tau60 x %.3g (N=%d) = %.3g | ratio ico/CT %.1f'%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[8],r[7],r[7]/r[4]))
# post-projection noise requirement for distance-3 block of N qubits
for N in [67,97,127]:
    print('distance-3 block of %d qubits: to keep post-projection logical failure < 1e-10 needs per-qubit error < %.1e'%(N,np.sqrt(2e-10/(N*(N-1)))))
# curves for chart
es=np.logspace(-4,np.log10(0.45),26)
D={'e':list(es)}
for k,c in codes.items(): D['N%d'%k[0]]=[float(out(c,e)[0]) for e in es]
D['ctrl']=[float(out(design(67,1),e)[0]) for e in es]
D['r15']=[float(min(35*e**3,0.5)) for e in es]
D['rows']=rows
json.dump(D,open('bigviz.json','w'))
