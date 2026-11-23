# Step 3 library: the slice's own Fourier side (Johnson scheme) for graph functions.
import itertools as it, numpy as np, scipy.sparse as sp
def setup(m,k):
    E=list(it.combinations(range(m),2)); n=len(E); idx={e:i for i,e in enumerate(E)}
    pts=[sum(1<<i for i in c) for c in it.combinations(range(n),k)]; pos={x:i for i,x in enumerate(pts)}
    rows=[];cols=[]
    for a,x in enumerate(pts):
        ones=[i for i in range(n) if x>>i&1]; zeros=[i for i in range(n) if not x>>i&1]
        for i in ones:
            for j in zeros: rows.append(a); cols.append(pos[x^(1<<i)^(1<<j)])
    A=sp.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(pts),len(pts)))
    J=min(k,n-k); lam=[(k-j)*(n-k-j)-j for j in range(J+1)]
    return E,idx,n,pts,pos,A,lam
def levels(f,A,lam):
    """components f_j of f in the Johnson eigenspaces (projector = polynomial in A)."""
    out=[]
    for j,lj in enumerate(lam):
        v=f.astype(float).copy()
        for i,li in enumerate(lam):
            if i!=j: v=(A@v-li*v)/(lj-li)
        out.append(v)
    return out
def weights(f,A,lam):
    comp=levels(f,A,lam); w=np.array([c@c for c in comp]); return w[1:]/w[1:].sum()   # variance shares, levels 1..J
def mean_level(f,A,lam): w=weights(f,A,lam); return float(w@np.arange(1,len(w)+1))
def has_clique(x,m,idx,q): return int(any(all(x>>idx[p]&1 for p in it.combinations(T,2)) for T in it.combinations(range(m),q)))
def classes(m,E,idx,pts):
    """isomorphism class label of each slice point (canonical = min image under S_m)."""
    perms=[]
    for p in it.permutations(range(m)): perms.append([idx[tuple(sorted((p[a],p[b])))] for a,b in E])
    P=np.array(perms); bits=np.array([[x>>i&1 for i in range(len(E))] for x in pts],dtype=np.int64)
    pw=1<<np.arange(len(E),dtype=np.int64); canon=np.full(len(pts),np.iinfo(np.int64).max)
    for row in P:
        img=np.zeros(len(pts),dtype=np.int64); img+= (bits*pw[row]).sum(axis=1); canon=np.minimum(canon,img)
    _,lab=np.unique(canon,return_inverse=True); return lab
