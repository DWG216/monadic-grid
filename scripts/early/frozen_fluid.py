import numpy as np, itertools
def qn(m,l): return np.sin(m*np.pi/l)/np.sin(np.pi/l)
def rep(k,n):
    l=k+2; paths=[]
    def rec(p):
        if len(p)==n+1: paths.append(tuple(p)); return
        for s in (p[-1]-1,p[-1]+1):       # j stored as 2j
            if 0<=s<=k: rec(p+[s])
    rec([0]); ix={p:i for i,p in enumerate(paths)}; D=len(paths); d=qn(2,l)
    A=1j*np.exp(1j*np.pi/(2*l)); gens=[]
    for i in range(1,n):
        E=np.zeros((D,D))
        for p in paths:
            if p[i-1]!=p[i+1]: continue
            a=p[i-1]
            for b in (a-1,a+1):
                q=list(p); q[i]=b; q=tuple(q)
                if q in ix: E[ix[q],ix[p]]=np.sqrt(qn(p[i]+1,l)*qn(b+1,l))/qn(a+1,l)
        S=A*np.eye(D)+E/A; gens.append(S)
    return gens,D
def key(U):
    f=U.reshape(-1); j=np.argmax(abs(f)>1e-6); U=U*abs(f[j])/f[j]; return tuple(np.round(U.reshape(-1),6))
def order(gens,cap=30000):
    gs=gens+[np.linalg.inv(g) for g in gens]; I=np.eye(gens[0].shape[0]); seen={key(I)}; fr=[I]
    while fr:
        nw=[]
        for U in fr:
            for g in gs:
                V=g@U; kk=key(V)
                if kk not in seen:
                    seen.add(kk); nw.append(V)
                    if len(seen)>cap: return '>%d'%cap
        fr=nw
    return str(len(seen))
res={}
for k in range(1,9):
    l=k+2; dims=[qn(m+1,l) for m in range(k+1)]; wi=all(abs(x*x-round(x*x))<1e-9 for x in dims)
    row=[]
    for n in (3,4,5,6):
        g,D=rep(k,n); un=max(np.linalg.norm(G@G.conj().T-np.eye(D)) for G in g); row.append(order(g))
    res[k]=row
    print('k=%d ell=%2d d_1/2=%.4f weakly integral=%-5s | unitarity %.0e | image order n=3,4,5,6: %s'%(k,l,dims[1],wi,un,row))
