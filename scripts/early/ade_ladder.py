import numpy as np, itertools
phi=(1+5**.5)/2
def T(n):  # nodes: centre + arms of lengths 1,2,n-1 (so arms have 2,3,n nodes counting centre)
    arms=[1,2,n-1]; N=1+sum(arms); A=np.zeros((N,N)); k=1
    for L in arms:
        prev=0
        for _ in range(L): A[prev,k]=A[k,prev]=1; prev=k; k+=1
    return 2*np.eye(N)-A
print('A1  n  rank  det   1/2+1/3+1/n   positive definite')
for n in range(2,11):
    C=T(n); print('   %2d  %2d  %5.2f   %.3f        %s'%(n,len(C),np.linalg.det(C),1/2+1/3+1/n,np.linalg.eigvalsh(C).min()>1e-9))
# A2: binary polyhedral groups in SU(2)
def q(w,x,y,z): return np.array([[w+1j*x, y+1j*z],[-y+1j*z, w-1j*x]])
def close(gens):
    key=lambda M: tuple(np.round(M.reshape(-1),6)); G={key(np.eye(2)):np.eye(2,dtype=complex)}; fr=[np.eye(2,dtype=complex)]
    while fr:
        nw=[]
        for M in fr:
            for g in gens:
                P=g@M; k=key(P)
                if k not in G: G[k]=P; nw.append(P)
        fr=nw
    return list(G.values())
groups={'2T':[q(0,1,0,0),q(.5,.5,.5,.5)],'2O':[q(.5,.5,.5,.5),q(2**-.5,2**-.5,0,0)],'2I':[q(.5,.5,.5,.5),q(phi/2,1/(2*phi),.5,0)]}
for name,gens in groups.items():
    G=close(gens); n=len(G)
    # conjugacy classes (by trace suffices in SU(2) for these groups? use actual conjugation)
    key=lambda M: tuple(np.round(M.reshape(-1),6)); idx={key(g):i for i,g in enumerate(G)}
    cls=[];seen=set()
    for i,g in enumerate(G):
        if i in seen: continue
        c={idx[key(h@g@h.conj().T)] for h in G}; seen|=c; cls.append(sorted(c))
    k=len(cls); cid=np.zeros(n,int)
    for a,c in enumerate(cls): cid[c]=a
    # class multiplication matrices -> character table (Burnside)
    mul=np.zeros((n,n),int)
    for i,a in enumerate(G):
        for j,b in enumerate(G): mul[i,j]=idx[key(a@b)]
    Ms=[]
    for r in range(k):
        M=np.zeros((k,k))
        for s in range(k):
            rep=cls[s][0]
            # count pairs: number of x in class r, y in class t with x*y = rep  -> M[s? ] use standard: C_r C_t = sum a_rts C_s
        Ms.append(M)
    # simpler: characters via eigenvectors of random combination of class sums acting on class functions
    Z=np.zeros((k,k))  # class sum operator of random combo on center of group algebra
    rng=np.random.default_rng(1); w=rng.normal(size=k)
    for r in range(k):
        for x in cls[r]:
            for t in range(k):
                y=cls[t][0]; Z[cid[mul[x,y]],t]+=w[r]
    ev,V=np.linalg.eig(Z)
    sizes=np.array([len(c) for c in cls]); chars=[]
    for j in range(k):
        v=np.real_if_close(V[:,j])  # coefficients on class sums of a central idempotent ~ chi(g^-1)
        # normalise to character: chi_i(C_t)/... use omega = sizes*chi/d ; recover chi up to scale via orthonormality
        chi=v/sizes; inv=[cid[idx[key(G[cls[t][0]].conj().T)]] for t in range(k)]
        chi=np.conj(chi[inv]); nrm=np.sqrt(np.sum(sizes*abs(chi)**2)/n); chi=chi/nrm
        e=cls.index([idx[key(np.eye(2))]]) if [idx[key(np.eye(2))]] in cls else None
        chi=chi*abs(chi[e])/chi[e]; chars.append(chi)
    dims=np.round([np.real(c[e]) for c in chars]).astype(int)
    V2=np.array([np.real(np.trace(G[cls[t][0]])) for t in range(k)])
    A=np.array([[np.real(np.sum(sizes*V2*chars[i]*np.conj(chars[j]))/n) for j in range(k)] for i in range(k)])
    A=np.round(A).astype(int); deg=sorted(A.sum(1)); pf=max(abs(np.linalg.eigvals(A)))
    print('A2 %s order %d | irreps %d | dims %s | sum d^2 %d | McKay degrees %s | Perron %.6f | dims are Perron vector: %s'%(
        name,n,k,sorted(dims.tolist()),int((dims**2).sum()),deg,pf,np.allclose(A@dims,2*dims)))
    # arm lengths from the branch node
    br=int(np.argmax(A.sum(1))); arms=[]
    for nb in np.nonzero(A[br])[0]:
        L=1;prev,cur=br,nb
        while True:
            nx=[x for x in np.nonzero(A[cur])[0] if x!=prev]
            if not nx: break
            prev,cur=cur,nx[0]; L+=1
        arms.append(L)
    print('   arms from branch node (nodes):',sorted(arms))
