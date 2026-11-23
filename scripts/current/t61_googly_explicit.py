import itertools, random
random.seed(5)
E=[(a,b) for a in range(3) for b in range(3)]; Z0=(0,0); ONE=(1,0)
def mul(x,y): a,b=x;c,d=y; return ((a*c+b*d)%3,(a*d+b*c+b*d)%3)
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def pw(x,n):
    r=ONE
    for _ in range(n): r=mul(r,x)
    return r
cub=lambda x: pw(x,3)
inv=lambda x: next(y for y in E if mul(x,y)==ONE)
def normp(v):
    k=next(i for i,c in enumerate(v) if c!=Z0); iv=inv(v[k]); return tuple(mul(iv,c) for c in v)
pts=sorted(set(normp(v) for v in itertools.product(E,repeat=4) if any(c!=Z0 for c in v)))
D=lambda Z: normp((cub(Z[2]),cub(Z[3]),cub(Z[0]),cub(Z[1])))
Dinv=lambda W: normp((cub(W[2]),cub(W[3]),cub(W[0]),cub(W[1])))
res={}
res['E1']=(len(set(D(p) for p in pts))==820, all(D(D(p))==p for p in pts))
ok=True
for _ in range(30):
    x=[random.choice(E) for _ in range(4)]; a,b,c,d=x
    for p0,p1 in [(ONE,t) for t in E]+[(Z0,ONE)]:
        Z=(add(mul(a,p0),mul(b,p1)),add(mul(c,p0),mul(d,p1)),p0,p1); W=D(Z)
        lam=(W[0],W[1]); mu=(W[2],W[3]); xc=[cub(v) for v in x]
        ok&= normp((lam[0],lam[1],add(mul(xc[0],lam[0]),mul(xc[1],lam[1])),add(mul(xc[2],lam[0]),mul(xc[3],lam[1]))))==normp((lam[0],lam[1],mu[0],mu[1]))
res['E1_lines']=ok
# fibers: pi-fiber = points with given [pi]; D maps to points with given [lambda]
def base(Z,i0,i1):
    p=(Z[i0],Z[i1]); return None if p==(Z0,Z0) else normp(p+ (Z0,Z0))[:2]
fib_ok=True
for pb in set(base(p,2,3) for p in pts if base(p,2,3)):
    F=[p for p in pts if base(p,2,3)==pb]; lb={base(D(p),0,1) for p in F}
    fib_ok&= len(lb)==1
res['E2']=fib_ok
eps=(1,0)
def g(w0,t): return mul(mul(w0,w0),t)
def PhiA(Z):   # chart pi0 != 0 and pi1 != 0 (overlap); identity elsewhere
    w0,w1,p0,p1=Z
    if p0==Z0 or p1==Z0: return Z
    t=mul(p1,inv(p0)); return (w0, add(w1,neg(mul(eps,mul(g(w0,t),p0)))), p0, p1)   # degree-1 homogeneous form: g * pi0
def PhiS(W):
    l0,l1,m0,m1=W
    if l0==Z0 or l1==Z0: return W
    u=mul(l1,inv(l0)); return (l0,l1,m0, add(m1,neg(mul(eps,mul(g(m0,u),l0)))))
E3=True; E4=True; E5=True
for p in pts:
    q=Dinv(normp(PhiS(D(p))))
    w0,w1,p0,p1=p
    if p0!=Z0 and p1!=Z0:
        t=mul(p1,inv(p0)); pred=normp((w0, add(w1,neg(cub(mul(eps,mul(g(cub(w0),cub(t)),cub(p0)))))), p0, p1))
        E3&= q==pred
        E5&= cub(g(cub(w0),cub(t)))==g(w0,t)
    else: E3&= q==p
    r=normp(PhiA(q)); E4&= (r[2],r[3])==(p[2],p[3]) or normp(r)==normp(p) or base(r,2,3)==base(p,2,3)
res['E3']=E3; res['E4']=(E4, len(set(normp(PhiA(Dinv(normp(PhiS(D(p)))))) for p in pts))==820); res['E5']=E5
# E6 formal sections over Z/9[phi]-free check: polynomial identity with g_total = w^2 t + w^18 t^9, sample over F9 and Z/9 at unit t
def ring(m):
    def M(x,y): a,b=x;c,d=y; return ((a*c+b*d)%m,(a*d+b*c+b*d)%m)
    def A(x,y): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
    def P(x,n):
        r=(1,0)
        for _ in range(n): r=M(r,x)
        return r
    return M,A,P
def laurent_split_check(m):
    M,A,P=ring(m); ok=0
    for _ in range(25):
        a,b,c,d=[(random.randrange(m),random.randrange(m)) for _ in range(4)]
        # coefficients of g_total(a+bt, t) as polynomial in t: compute by expansion with binomials
        from math import comb
        coeff={}
        for (e,s) in [(2,1),(18,9)]:
            for j in range(e+1):
                cf=M(P(a,e-j),P(b,j)); cf=((cf[0]*comb(e,j))%m,(cf[1]*comb(e,j))%m)
                k=j+s; coeff[k]=A(coeff.get(k,(0,0)),cf)
        hi={k:v for k,v in coeff.items() if k>=2}; lo={k:v for k,v in coeff.items() if k<=1}
        # U0 omega1 = c + d t + sum_{k>=2} hi_k t^k ; U1 omega1 = c + d t - sum_{k<=1} lo_k t^k ; matching: U0 - g = U1
        t=(1,1) if m==3 else (1,3)
        val=lambda C: (lambda s: s)(sum_poly(C,t,M,A,P))
        U0=A(A(c,M(d,t)),sum_poly(hi,t,M,A,P)); U1=A(A(c,M(d,t)),neg_m(sum_poly(lo,t,M,A,P),m)); gt=sum_poly(coeff,t,M,A,P)
        ok+= A(U0,neg_m(gt,m))==U1
    return ok
def sum_poly(C,t,M,A,P):
    s=(0,0)
    for k,v in C.items(): s=A(s,M(v,P(t,k)))
    return s
def neg_m(x,m): return ((-x[0])%m,(-x[1])%m)
res['E6']=laurent_split_check(3)+laurent_split_check(9)
# E7 null relation over F9: formal sections evaluated on points, ASD only vs googly (w^2 t + w^18 t^9), eps = 1
from math import comb
def sec(x,terms):
    a,b,c,d=x; pts0=[]
    for tv in E:
        t=tv; w0=add(a,mul(b,t)); hi=(0,0)
        for (e,s) in terms:
            for j in range(e+1):
                k=j+s
                if k>=2:
                    cf=mul(pw(a,e-j),pw(b,j)); cf=((cf[0]*comb(e,j))%3,(cf[1]*comb(e,j))%3); hi=add(hi,mul(cf,pw(t,k)))
        pts0.append((t,w0,add(add(c,mul(d,t)),hi)))
    lo=(0,0)
    for (e,s) in terms:
        for j in range(e+1):
            if j+s==1:
                cf=mul(pw(a,e-j),pw(b,j)); cf=((cf[0]*comb(e,j))%3,(cf[1]*comb(e,j))%3); lo=add(lo,cf)
    pts0.append(('inf',b,add(d,neg(lo))))
    return frozenset(pts0)
M4=list(itertools.product(E,repeat=4)); samp=random.sample(M4,20)
SA={x:sec(x,[(2,1)]) for x in M4}; SG={x:sec(x,[(2,1),(18,9)]) for x in M4}
diff=sum(1 for x in samp if {y for y in M4 if y!=x and SA[x]&SA[y]}!={y for y in M4 if y!=x and SG[x]&SG[y]})
res['E7']=diff
for k,v in res.items(): print(k,v)
