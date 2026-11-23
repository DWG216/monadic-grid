import itertools, random
# F9 elements as a+b*phi, phi^2 = phi+1, coded 3a+b? use pairs
E=[(a,b) for a in range(3) for b in range(3)]
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def mul(x,y): a,b=x;c,d=y; return ((a*c+b*d)%3,(a*d+b*c+b*d)%3)
def pw(x,n):
    r=(1,0)
    for _ in range(n%8 if x!=(0,0) else n): r=mul(r,x)
    return r if n>0 or x!=(0,0) else (1,0)
def fr(x): return mul(mul(x,x),x)
Z0=(0,0)
def Sig(Z):
    t=Z0
    for i,j in [(0,2),(2,0),(1,3),(3,1)]: t=add(t,mul(Z[i],fr(Z[j])))
    return t
vecs=[v for v in itertools.product(E,repeat=4) if any(c!=Z0 for c in v)]
res={}
res['G1']=all(Sig(v)[1]==0 for v in vecs)
def norm_pt(v):
    k=next(i for i,c in enumerate(v) if c!=Z0); inv=next(y for y in E if mul(y,v[k])==(1,0))
    return tuple(mul(inv,c) for c in v)
pts=sorted(set(norm_pt(v) for v in vecs)); null=[p for p in pts if Sig(p)==Z0]
res['G2']=(len(pts),len(null))
nullset=set(null); lines=set()
for p,q in itertools.combinations(null,2):
    L=set()
    for a in E:
        for b in E:
            if a==Z0 and b==Z0: continue
            v=tuple(add(mul(a,p[i]),mul(b,q[i])) for i in range(4)); L.add(norm_pt(v))
    if L<=nullset: lines.add(frozenset(L))
per_pt={p:0 for p in null}
for L in lines:
    for p in L: per_pt[p]+=1
res['G3']=(len(lines),set(len(L) for L in lines),set(per_pt.values()))
phi=(0,1)
res['G4']=all(Sig(tuple(mul(phi,c) for c in v))==((-Sig(v)[0])%3,(-Sig(v)[1])%3) for v in vecs[:3000]) and pw(phi,4)==(2,0)
res['G5']=(all((3*n)%8==(-n-4)%8 for n in range(1,16,2)), all((3*n+4)%8==(-n-4)%8 for n in range(0,16,2)),
           all((3*(3*n))%8==n%8 for n in range(8)), all((-(-n-4)-4)%8==n%8 for n in range(8)))
random.seed(0); ok=True
for _ in range(500):
    Z=random.choice(vecs); lam=random.choice(E[1:]); a=random.randint(0,6); b=random.randint(0,6); n=a+b
    f=lambda Z: mul(pw(fr(Z[0]),a) if a else (1,0), pw(fr(Z[1]),b) if b else (1,0))
    lZ=tuple(mul(lam,c) for c in Z)
    ok&= f(lZ)==mul(pw(lam,3*n) if 3*n else (1,0),f(Z))
    g=lambda Z: mul(f(Z),Sig(Z))
    ok&= g(lZ)==mul(pw(lam,3*n+4),g(Z))
res['G6']=ok
pp=[q for q in range(2,50) if any(q==p**k for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] for k in range(1,7))]
res['G7']=[q for q in pp if q+1==4]
for k,v in res.items(): print(k,v)
