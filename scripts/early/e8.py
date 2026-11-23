import numpy as np, itertools
phi=(1+5**.5)/2
# E1
C=2*np.eye(8); edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(4,7)]   # E8: chain 0..6, branch 7 at node 4
for a,b in edges: C[a,b]=C[b,a]=-1
Adj=2*np.eye(8)-C; w,V=np.linalg.eigh(Adj); v=abs(V[:,-1]); m=np.sort(v/v.min())
print('E1 top eigenvalue %.6f vs 2cos(pi/30) %.6f | masses/m1:'%(w[-1],2*np.cos(np.pi/30)),np.round(m,4).tolist(),'| m2/m1 %.6f phi %.6f'%(m[1],phi))
# icosians as 4 components, each (p,q) meaning (p+q*phi)/2
U=[]
for i in range(4):
    for s in (2,-2):
        c=[(0,0)]*4; c[i]=(s,0); U.append(tuple(c))
for s in itertools.product((1,-1),repeat=4): U.append(tuple((x,0) for x in s))
evp=[p for p in itertools.permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0]
base=[(0,0),(1,0),(-1,1),(0,1)]   # 0, 1/2, phi^-1/2, phi/2
for p in evp:
    for s in itertools.product((1,-1),repeat=3):
        c=[base[0]]+[(s[k]*base[k+1][0],s[k]*base[k+1][1]) for k in range(3)]
        U.append(tuple(c[p[i]] for i in range(4)))
U=list(set(U)); print('units:',len(U))
def flat(c): return np.array([x for pq in c for x in pq])
def tphi(c): return tuple((q,p+q) for p,q in c)
gens=np.array([flat(u) for u in U]+[flat(tphi(u)) for u in U])
def AB(v):
    v=np.asarray(v); p,q=v[0::2],v[1::2]; return int((p*p+q*q).sum()), int((2*p*q+q*q).sum())
def Q(v): A,B=AB(v); return (A+B)/4
# Z-basis by integer row reduction (HNF-like)
def zbasis(rows):
    R=[list(map(int,r)) for r in rows]; basis=[]; col=0
    ncol=len(R[0])
    for col in range(ncol):
        R=[r for r in R if any(r)]
        piv=[r for r in R if r[col]!=0]
        if not piv: continue
        rest=[r for r in R if r[col]==0]
        while len(piv)>1:
            piv.sort(key=lambda r:abs(r[col])); p=piv[0]; nxt=[p]
            for r in piv[1:]:
                f=r[col]//p[col]; r2=[a-f*b for a,b in zip(r,p)]
                (nxt if r2[col]!=0 else rest).append(r2)
            piv=nxt
        basis.append(piv[0]); R=rest
    return basis
Bz=np.array(zbasis(gens))
print('E3 rank',len(Bz))
G=np.array([[Q(a+b)-Q(a)-Q(b) for b in Bz] for a in Bz]); G2=G.copy(); np.fill_diagonal(G2,[2*Q(a) for a in Bz])
print('   Gram of 2Q: even diag',all(int(x)%2==0 for x in np.diag(G2)),'| det %.6f'%np.linalg.det(G2),'| min eig %.4f'%np.linalg.eigvalsh(G2).min())
Binv=np.linalg.inv(Bz.T.astype(float))
def member(v):
    x=Binv@np.asarray(v,float); return np.allclose(x,np.round(x),atol=1e-8)
# enumerate icosians with 4*N = A + B phi
def count(Atar,Btar):
    comps=[(p,q) for p in range(-20,21) for q in range(-12,13)]
    sq={}
    for p,q in comps:
        a,b=p*p+q*q,2*p*q+q*q
        if a+b*phi<=Atar+Btar*phi+1e-9 and a+b*(1-phi)<=Atar+Btar*(1-phi)+1e-9: sq.setdefault((a,b),[]).append((p,q))
    keys=list(sq); pair={}
    for k1 in keys:
        for k2 in keys:
            pair.setdefault((k1[0]+k2[0],k1[1]+k2[1]),[]).append((k1,k2))
    n=0; found=[]
    for (a12,b12),L12 in pair.items():
        L34=pair.get((Atar-a12,Btar-b12))
        if not L34: continue
        for k1,k2 in L12:
            for k3,k4 in L34:
                for c in itertools.product(sq[k1],sq[k2],sq[k3],sq[k4]):
                    if member(flat(c)): n+=1
    return n
print('   vectors with Q=1 (count over norms 1 and phi^-2 and others):',sum(1 for _ in []) or 'see below')
print('E3 icosians of norm 1:',count(4,0),'| norm phi^-2 (4N = 8 - 4 phi):',count(8,-4))
t=((0,0),(2,0),(2,0),(4,2))
print('E4 tau60 (0,1,1,2+phi): member',member(flat(t)),'| Q =',Q(flat(t)))
for perm in itertools.permutations(range(4)):
    pass
print('E4 icosians of reduced norm 7+5phi:',count(28,20),'(predicted 7200)')
print('Control norm 3:',count(12,0),'(predicted 1200)')
