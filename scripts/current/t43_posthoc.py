import numpy as np
exec(open('t43_rodin_coil.py').read().split('jumps=')[0])
def parts(shift,aa,sense=1):
    slots=[9*b+r for b in range(4) for r in order]; loops=[]; runs=[]; prev=None
    for s in slots:
        phi=2*np.pi*((s+shift)%S)/S
        if prev is not None:
            d=((phi-prev+np.pi)%(2*np.pi))-np.pi
            runs.append(run(prev,prev+d,aa) if d>=0 else run(prev+d,prev,aa)[::-1])
        L=loop(phi,aa); loops.append(L if sense>0 else L[::-1]); prev=phi
    return loops,runs
def msum(A,B): return sum(mutual(x,y) for x in A for y in B)
LA,RA=parts(0,a)
out={}
ML=[];MR=[]
for k in range(9):
    LB,RB=parts(k,a+0.0005); ML.append(msum(LA,LB)); MR.append(msum(RA,RB)+msum(LA,RB)+msum(RA,LB))
out['loops-only M(k) uH']=[round(m*1e6,4) for m in ML]
out['loops-only period-3 dev']=max(abs(ML[k]-ML[k+3])/abs(ML[k]) for k in range(6))
out['loops-only |M1-M2|/M1']=abs(ML[1]-ML[2])/ML[1]
out['runs and cross terms M(k) uH']=[round(m*1e6,4) for m in MR]
LBc,RBc=parts(0,a+0.0005,-1); out['loops-only counter-wound M(0) uH']=round(msum(LA,LBc)*1e6,4)
for k,v in out.items(): print(k,v)
