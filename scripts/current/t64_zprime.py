import numpy as np
from collections import Counter, deque
exec(open('t56_generation.py').read().split("sizes={}")[0])
k=idx[ones[0]]; lam,O=orbit(k); g=grade(lam,O,k)
levels=Counter(g); mean=sum(l*c for l,c in levels.items())/27
q={l:round(3*(mean-l),6) for l in levels}
print('Z1 levels',dict(levels),' charges by level',q,' trace',sum(q[l]*c for l,c in levels.items()))
D5=[i for i in range(6) if i!=k]; A6=A
deg=lambda i: sum(1 for j in D5 if j!=i and A6[i,j]!=0)
ends=[i for i in D5 if deg(i)==1]; br=[i for i in D5 if deg(i)==3][0]
spin=[e for e in ends if A6[e,br]!=0]; vec=[e for e in ends if A6[e,br]==0]
def sub_orbits(level,node,exclude):
    S={tuple(O[i]) for i in range(27) if g[i]==level}; sizes=[]
    while S:
        s0=S.pop(); comp={s0}; dq=deque([np.array(s0)])
        while dq:
            mu=dq.popleft()
            for i in range(6):
                if i in exclude: continue
                t=tuple(mu-mu[i]*A6[i])
                if t in S: S.remove(t); comp.add(t); dq.append(np.array(t))
        sizes.append(len(comp))
    return sorted(sizes)
print('D5 ends: spinor-type',spin,' vector-type',vec)
for sn in spin:
    print('Z2 delete spinor end',sn,': 16 ->',sub_orbits(1,sn,{k,sn}),' 10 ->',sub_orbits(2,sn,{k,sn}))
for vn in vec:
    print('Z3 delete vector end',vn,': 16 ->',sub_orbits(1,vn,{k,vn}))
