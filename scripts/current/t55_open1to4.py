import numpy as np, itertools
from collections import Counter, deque
phi=(1+5**.5)/2; psi=1-phi
res={}
# ---------- 1
def vecs(t): return np.array([[1,t,0],[-1,t,0],[0,1,t],[0,-1,t],[t,0,1],[-t,0,1]],float).T
Ep,Eq=vecs(phi),vecs(psi)
res['1a']=np.abs(Ep@Eq.T).max(); A=Ep@Ep.T; B=Eq@Eq.T
res['1b']=max(np.abs(A-A[0,0]*np.eye(3)).max(),np.abs(B-B[0,0]*np.eye(3)).max())
E=np.vstack([Ep,Eq]); M=np.linalg.solve(E,np.vstack([phi*Ep,psi*Eq]))
M2=2*M; res['1c_halfint']=np.abs(M2-np.round(M2)).max()
M3=np.linalg.matrix_power(M,3)
res['1c_M_int']=np.abs(M-np.round(M)).max(); res['1c_M3_int']=np.abs(M3-np.round(M3)).max()
print('M =\n',np.round(M,3)); print('eigenvalues of M:',np.round(sorted(np.linalg.eigvals(M).real),6))
Q=np.array([[0,1],[1,1]]); ev=sorted(np.linalg.eigvals(Q).real); res['1d']=(abs(ev[0]-psi)+abs(ev[1]-phi), round(np.linalg.det(Q),9))
# ---------- 2
def qmat(a,b,c,d): return np.array([[a+1j*b, c+1j*d],[-c+1j*d, a-1j*b]])
def key(m): return tuple(np.round(np.concatenate([m.real.ravel(),m.imag.ravel()]),6))
def close(gens):
    I=np.eye(2,dtype=complex); G={key(I):I}; fr=[I]
    while fr:
        n=[]
        for g in fr:
            for h in gens:
                x=g@h; k=key(x)
                if k not in G: G[k]=x; n.append(x)
        fr=n
    return list(G.values())
i_=qmat(0,1,0,0); j_=qmat(0,0,1,0); w=qmat(.5,.5,.5,.5)
Q8=close([i_,j_]); T2=close([i_,j_,w])
g5=qmat(phi/2,.5,1/(2*phi),0)   # an order-10 element of 2I
I2=close([i_,j_,w,g5])
def order(m):
    X=m.copy();k=1
    while np.abs(X-np.eye(2)).max()>1e-6: X=X@m;k+=1
    return k
def mckay(G):
    n=len(G); K={key(g):idx for idx,g in enumerate(G)}; inv=[K[key(np.linalg.inv(g))] for g in G]
    mult=[[K[key(G[a]@G[b])] for b in range(n)] for a in range(n)]
    cl=[-1]*n; C=[]
    for a in range(n):
        if cl[a]>=0: continue
        s=set(mult[mult[h][a]][inv[h]] for h in range(n)); C.append(sorted(s))
        for x in s: cl[x]=len(C)-1
    r=len(C); sz=np.array([len(c) for c in C])
    a=np.zeros((r,r,r))
    for I_ in range(r):
        for J in range(r):
            for k in range(r):
                z=C[k][0]; a[I_,J,k]=sum(1 for x in C[I_] if cl[mult[inv[x]][z]]==J)
    rng=np.random.default_rng(1); Acomb=sum(rng.normal()*a[I_] for I_ in range(r))
    _,V=np.linalg.eig(Acomb)
    chars=[]
    for v in V.T:
        e=next(idx for idx,c in enumerate(C) if np.allclose(G[c[0]],np.eye(2)))
        om=v/v[e]; d2=n/np.sum(np.abs(om)**2/sz); d=np.sqrt(d2.real)
        chars.append(d*om/sz)
    chars=np.array(chars); chiV=np.array([np.trace(G[c[0]]) for c in C])
    Amk=np.real(np.array([[np.sum(sz*chiV*ci*np.conj(cj))/n for cj in chars] for ci in chars]))
    dims=np.real(chars[:,[next(idx for idx,c in enumerate(C) if np.allclose(G[c[0]],np.eye(2)))]]).ravel()
    return np.round(Amk).astype(int),np.round(dims).astype(int),r
def shape(Adj):
    n=len(Adj); deg=Adj.sum(1); edges=deg.sum()//2
    br=[v for v in range(n) if deg[v]>=3]
    arms=[]
    if len(br)==1:
        b=br[0]
        for nb in np.where(Adj[b])[0]:
            L=1; prev,cur=b,nb
            while True:
                nx=[x for x in np.where(Adj[cur])[0] if x!=prev]
                if not nx: break
                prev,cur=cur,nx[0]; L+=1
            arms.append(L)
    return dict(nodes=n,edges=int(edges),tree=int(edges)==n-1,branch_deg=[int(deg[b]) for b in br],arms=sorted(arms))
for name,G in [('Q8',Q8),('2T',T2),('2I',I2)]:
    Adj,d,r=mckay(G); sh=shape(Adj)
    res['2_'+name]=dict(order=len(G),**sh,dims=sorted(d.tolist()),Ad_eq_2d=bool(np.all(Adj@d==2*d)))
    print(name,res['2_'+name])
res['2e_2T']=dict(sorted(Counter(order(g) for g in T2).items())); res['2e_2I']=dict(sorted(Counter(order(g) for g in I2).items()))
# ---------- 3  F9 = F3[phi], elements (a,b) = a + b phi
def fm(x,y): a,b=x; c,d=y; return ((a*c+b*d)%3,(a*d+b*c+b*d)%3)
def fpow(x,n):
    r=(1,0)
    for _ in range(n): r=fm(r,x)
    return r
P=(0,1); i9=fpow(P,2)
res['3a']=(fpow(P,3)==((1-0)%3,(-1)%3), fpow(i9,3)==((-i9[0])%3,(-i9[1])%3), 'i=phi^2=',i9)
def detmul(x): a,b=x; return (a*(a+b)-b*b)%3   # det of multiplication by a+b phi on (1,phi)
F=[0,1]
for k in range(70): F.append(F[-1]+F[-2])
res['3b']=all(detmul(fpow(P,n))==((-1)**n)%3 and F[n-1]*F[n+1]-F[n]**2==(-1)**n for n in range(1,61))
res['3c']=sorted(set(fpow(P,n) for n in range(8) if detmul(fpow(P,n))==1))==sorted({(1,0),i9,(2,0),((-i9[0])%3,(-i9[1])%3)})
z=np.array([np.exp(1j*0.7),np.exp(-1j*0.7)])
iz=i_@z; jz=j_@z
res['3d']=(np.allclose(iz,[1j*z[0],-1j*z[1]]), np.allclose(jz,[-z[1],z[0]]) or np.allclose(jz,[z[1],-z[0]]), np.allclose(j_@j_,-np.eye(2)))
print('j acting on (z+,z-):',np.round(jz,3),' z=',np.round(z,3))
# ---------- 4
def grp(m,gens):
    def mul(A,B): return ((A[0]*B[0]+A[1]*B[2])%m,(A[0]*B[1]+A[1]*B[3])%m,(A[2]*B[0]+A[3]*B[2])%m,(A[2]*B[1]+A[3]*B[3])%m)
    I=(1,0,0,1); G={I}; dq=deque([I])
    while dq:
        g=dq.popleft()
        for h in gens:
            x=mul(g,h)
            if x not in G: G.add(x); dq.append(x)
    return len(G)
Qm=(0,1,1,1); Um=(1,1,0,1)
def sq(A,m): return ((A[0]*A[0]+A[1]*A[2])%m,(A[0]*A[1]+A[1]*A[3])%m,(A[2]*A[0]+A[3]*A[2])%m,(A[2]*A[1]+A[3]*A[3])%m)
res['4']={}
for k in [1,2,3,4]:
    m=3**k; a=grp(m,[sq(Qm,m),Um]); b=grp(m,[Qm,Um]); res['4'][m]=(a,24*27**(k-1),b)
    print('mod',m,': <Q^2,U> =',a,' predicted',24*27**(k-1),'; <Q,U> =',b)
res['4c']=grp(81,[Qm])
for k,v in res.items(): print(k,v)
