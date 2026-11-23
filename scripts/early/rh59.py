import numpy as np, itertools, sys
phi=(1+5**.5)/2
def sqrt_mod(a,q):
    for x in range(q):
        if x*x%q==a%q: return x
    return None
def setup(q):
    ph=[x for x in range(q) if (x*x-x-1)%q==0][0]   # phi mod q (choose root consistent? either root = Galois choice)
    inv2=pow(2,-1,q)
    # coordinates as (a,b) meaning (a+b*phi)/2
    def val(c): a,b=c; return (a+b*ph)*inv2%q
    # splitting: I^2=J^2=-1
    x=y=None
    for xx in range(q):
        r=(-1-xx*xx)%q; yy=sqrt_mod(r,q)
        if yy is not None: x,y=xx,yy; break
    E=np.eye(2,dtype=np.int64); I=np.array([[0,1],[q-1,0]],dtype=np.int64); J=np.array([[x,y],[y,(q-x)%q]],dtype=np.int64); K=I@J%q
    def mat(qt): return (val(qt[0])*E+val(qt[1])*I+val(qt[2])*J+val(qt[3])*K)%q
    return ph,mat
# icosians in (a,b) coordinates
def icosians():
    out=[]
    Z=(0,0)
    for k in range(4):
        for s in (1,-1):
            e=[Z]*4; e[k]=(2*s,0); out.append(tuple(e))
    for sg in itertools.product((1,-1),repeat=4): out.append(tuple((s,0) for s in sg))
    # even perms of (0, 1, 1/phi, phi)/2 with signs; 1/phi = phi-1 -> (a,b)=(-1,1); phi -> (0,1); 1 -> (1,0)
    base=[(0,0),(1,0),(-1,1),(0,1)]
    evens=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[i]<p[j])%2==0]
    for p in evens:
        for sg in itertools.product((1,-1),repeat=3):
            vals=[base[0]]+[(sg[i]*base[i+1][0],sg[i]*base[i+1][1]) for i in range(3)]
            qv=[None]*4
            for i in range(4): qv[p[i]]=vals[i]
            out.append(tuple(qv))
    return list(dict.fromkeys(out))
ICO=icosians(); assert len(ICO)==120, len(ICO)
TAU=((0,0),(2,0),(2,0),(4,2))   # (0,1,1,2+phi) in halves
def norm_key(M,q):
    f=M.reshape(-1)%q; j=next(i for i in range(4) if f[i]); inv=pow(int(f[j]),-1,q); return tuple(int(v) for v in (f*inv)%q)
def graph(q):
    ph,mat=setup(q)
    A5={}
    for u in ICO:
        M=mat(u); A5.setdefault(norm_key(M,q),M)
    A5m=list(A5.values()); T=mat(TAU)
    assert len(A5m)==60, len(A5m)
    # enumerate PGL2(F_q) projectively
    els=[]
    for a,b,c,d in itertools.product(range(q),repeat=4):
        if (a*d-b*c)%q==0: continue
        M=np.array([[a,b],[c,d]],dtype=np.int64)
        if norm_key(M,q)==(a,b,c,d) if False else None: pass
        els.append((a,b,c,d))
    keys=set(norm_key(np.array(e).reshape(2,2),q) for e in els)
    keys=sorted(keys)
    A5stack=np.array(A5m)
    def coset(k):
        M=np.array(k).reshape(2,2)
        prods=np.einsum('ij,njk->nik',M,A5stack)%q
        return min(norm_key(P,q) for P in prods)
    cos={}
    for k in keys:
        c=coset(k)
        if c not in cos: cos[c]=len(cos)
    n=len(cos); A=np.zeros((n,n))
    UT=np.einsum('nij,jk->nik',A5stack,T)%q
    for c,i in cos.items():
        M=np.array(c).reshape(2,2)
        for P in np.einsum('ij,njk->nik',M,UT)%q:
            A[i,cos[coset(norm_key(P,q))]]+=1
    return A,len(keys)
bound=2*59**.5
rng=np.random.default_rng(3)
for q in (11,19,29,31):
    A,G=graph(q); n=len(A)
    ev=np.linalg.eigvalsh((A+A.T)/2); sym=np.abs(A-A.T).max()
    nontriv=[e for e in ev if abs(abs(e)-60)>1e-6]
    mx=max(abs(e) for e in nontriv)
    rnd=[]
    for _ in range(20):
        R=np.zeros((n,n))
        for _ in range(30):
            P=np.eye(n)[rng.permutation(n)]; R+=P+P.T
        e2=np.linalg.eigvalsh(R); rnd.append(np.sort(np.abs(e2))[-2])
    print('q=%d |PGL2|=%d vertices=%d degree=%d symmetric=%s trivial(+-60) count=%d | max nontrivial |lambda|=%.3f <= %.3f? %s | random: mean %.2f, max %.2f, exceed %d/20'%(
        q,G,n,int(A.sum(1)[0]),sym==0,len(ev)-len(nontriv),mx,bound,mx<=bound+1e-9,np.mean(rnd),max(rnd),sum(r>bound for r in rnd)),flush=True)
    if q==11: np.save('A11.npy',A)
