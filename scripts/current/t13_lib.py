# Step 4 library: measures of the cut inside a slice (boundary, sensitivity, witnesses).
exec(open('t12_lib.py').read())
def boundary(f,A): f=f.astype(float); return float(f@(A@(1-f)))          # Johnson edges with f = 1 at one end, 0 at the other
def boundary_spectral(f,A,lam): comp=levels(f,A,lam); return float(sum((lam[0]-l)*(c@c) for l,c in zip(lam,comp)))
def sens(f,A): f=f.astype(float); return np.where(f==1,A@(1-f),A@f)     # per point: swaps that flip the answer
def hit_table(n,pts,lab,cap):
    """for every partial assignment (P present, Q absent), |P|+|Q| <= cap: which classes have a consistent slice point. Returns list by size of boolean arrays (rows x classes)."""
    X=np.array(pts,dtype=np.int64); nc=lab.max()+1; out=[]
    for s in range(cap+1):
        rows=[]
        for S in it.combinations(range(n),s):
            for r in range(s+1):
                for P in it.combinations(S,r):
                    p=sum(1<<i for i in P); q=sum(1<<i for i in S)-p
                    ok=((X&p)==p)&((X&q)==0)
                    if ok.any(): rows.append(np.bincount(lab[ok],minlength=nc)>0)
        out.append(np.array(rows))
    return out
def witness(cls_val,H,b):
    """smallest partial assignment forcing value b on the slice (None if above cap)."""
    bad=(cls_val!=b)
    for s,T in enumerate(H):
        if len(T) and (~(T[:,bad].any(axis=1))).any(): return s
    return len(H)   # cap+1 means 'more than cap'
def degree_ge(x,m,idx,d):
    deg=[0]*m
    for (a,b),i in idx.items():
        if x>>i&1: deg[a]+=1; deg[b]+=1
    return int(max(deg)>=d)
