import numpy as np
from collections import Counter, deque
phi=(1+5**.5)/2
exec(open('t55_open1to4.py').read().split('# ---------- 2')[1].split('def shape')[0].replace('return np.round(Amk).astype(int),np.round(dims).astype(int),r','return np.round(Amk).astype(int),np.round(dims).astype(int),r,chars,C,G'))
Adj,dims,r,chars,C,G=mckay(T2)
eid=[k for k,c in enumerate(C) if np.allclose(G[c[0]],np.eye(2))][0]
w2=w@w   # order 3 element
cw=[k for k,c in enumerate(C) if any(np.allclose(G[x],w2) for x in c)][0]
triv=[a for a in range(r) if dims[a]==1 and np.allclose(chars[a],1)][0]
vnode=[a for a in range(r) if dims[a]==2 and np.allclose(chars[a][cw],-1)]
print('irrep dims:',dims.tolist(),' trivial node',triv)
# R0 V x V
chiV=np.array([np.trace(G[c[0]]) for c in C]); sz=np.array([len(c) for c in C])
mult=[round(np.real(np.sum(sz*chiV*chiV*np.conj(ch))/24)) for ch in chars]
print('R0 V x V multiplicities by irrep dim:',[(int(dims[a]),mult[a]) for a in range(r) if mult[a]])
ones=[a for a in range(r) if dims[a]==1 and a!=triv]
print('R1 nontrivial 1-dim nodes',ones,' values on order-3 element:',[np.round(chars[a][cw],3) for a in ones],' degrees',[int(Adj[a].sum()) for a in ones])
keep=[a for a in range(r) if a!=triv]; A=2*np.eye(6,dtype=int)-Adj[np.ix_(keep,keep)]
idx={a:i for i,a in enumerate(keep)}
print('E6 Cartan det =',round(np.linalg.det(A)))
def orbit(k):
    lam=np.zeros(6,int); lam[k]=1; seen={tuple(lam)}; dq=deque([lam])
    while dq:
        mu=dq.popleft()
        for i in range(6):
            nu=mu-mu[i]*A[i]
            t=tuple(nu)
            if t not in seen: seen.add(t); dq.append(nu)
    return lam,[np.array(s) for s in seen]
Ainv=np.linalg.inv(A)
def grade(lam,mus,k): return [int(round(((lam-mu)@Ainv)[k])) for mu in mus]
res={}
for name,a in [('w',ones[0]),('w2',ones[1])]:
    k=idx[a]; lam,O=orbit(k); g=grade(lam,O,k); res[name]=(len(O),dict(sorted(Counter(g).items())))
    print('R2/R3',name,': orbit',len(O),' split by own U(1):',res[name][1])
    # R4 D5 orbits within levels
    for lev in sorted(set(g)):
        S={tuple(O[i]) for i in range(len(O)) if g[i]==lev}; comps=[]
        while S:
            s0=S.pop(); comp={s0}; dq=deque([np.array(s0)])
            while dq:
                mu=dq.popleft()
                for i in range(6):
                    if i==k: continue
                    t=tuple(mu-mu[i]*A[i])
                    if t in S: S.remove(t); comp.add(t); dq.append(np.array(t))
            comps.append(len(comp))
        print('   level',lev,'D5 orbit sizes',comps)
sizes={}
for a in keep:
    lam,O=orbit(idx[a]); sizes[(int(dims[a]),int(Adj[a,triv]))]=sizes.get((int(dims[a]),int(Adj[a,triv])),[])+[len(O)]
print('R5 orbit sizes by (irrep dim, adjacent to trivial):',sizes)
c=[a for a in keep if dims[a]==3][0]; lam,O=orbit(idx[ones[0]]); gc=grade(lam,O,idx[c])
print('control: 27 graded by centre node:',dict(sorted(Counter(gc).items())))
