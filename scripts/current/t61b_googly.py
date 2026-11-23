import itertools, random
random.seed(6)
E=[(a,b) for a in range(3) for b in range(3)]; Z0=(0,0); ONE=(1,0); PHI=(0,1)
def mul(x,y): a,b=x;c,d=y; return ((a*c+b*d)%3,(a*d+b*c+b*d)%3)
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def pw(x,n):
    r=ONE
    for _ in range(n): r=mul(r,x)
    return r
cub=lambda x: pw(x,3); sig=lambda x: ((x[0]+x[1])%3,(-x[1])%3)
inv=lambda x: next(y for y in E if mul(x,y)==ONE)
def normp(v):
    k=next(i for i,c in enumerate(v) if c!=Z0); iv=inv(v[k]); return tuple(mul(iv,c) for c in v)
pts=sorted(set(normp(v) for v in itertools.product(E,repeat=4) if any(c!=Z0 for c in v)))
D=lambda Z: normp((cub(Z[2]),cub(Z[3]),cub(Z[0]),cub(Z[1])))
Dinv=lambda W: normp((cub(W[2]),cub(W[3]),cub(W[0]),cub(W[1])))
def shearA(Z,c):
    w0,w1,p0,p1=Z
    if p0==Z0 or p1==Z0: return normp(Z)
    gA=mul(c,mul(mul(w0,w0),mul(p1,inv(mul(p0,p0))))); return normp((w0,add(w1,neg(gA)),p0,p1))
def shearS(W,c):
    l0,l1,m0,m1=W
    if l0==Z0 or l1==Z0: return normp(W)
    gS=mul(c,mul(mul(m0,m0),mul(l1,inv(mul(l0,l0))))); return normp((l0,l1,m0,add(m1,neg(gS))))
res={}
wd=all(shearA(normp(tuple(mul(l,v) for v in p)),ONE)==shearA(p,ONE) for p in pts for l in E[1:])
res['F1']=(wd, len(set(shearA(p,ONE) for p in pts))==820)
res['F2']=all(D(shearA(Dinv(W),ONE))==shearS(W,ONE) for W in pts)
def curveA(x,eps=ONE):
    a,b,c,d=x; S=set()
    for t in E:
        w0=add(a,mul(b,t)); w1=add(add(c,mul(d,t)),mul(eps,add(mul((2,0),mul(mul(a,b),mul(t,t))),mul(mul(b,b),pw(t,3)))))
        S.add(normp((w0,w1,ONE,t)))
    S.add(normp((b,add(d,neg(mul(eps,mul(a,a)))),Z0,ONE))); return frozenset(S)
def curveS(y,eps=ONE):
    a,b,c,d=y; S=set()
    for u in E:
        m0=add(a,mul(b,u)); m1=add(add(c,mul(d,u)),mul(eps,add(mul((2,0),mul(mul(a,b),mul(u,u))),mul(mul(b,b),pw(u,3)))))
        S.add(normp((ONE,u,m0,m1)))
    S.add(normp((Z0,ONE,b,add(d,neg(mul(eps,mul(a,a))))))); return frozenset(S)
X=[tuple(random.choice(E) for _ in range(4)) for _ in range(30)]
res['F3']=sum(frozenset(D(p) for p in curveA(x))==curveS(tuple(cub(v) for v in x)) for x in X)
Xn=[x for x in (tuple(random.choice(E) for _ in range(4)) for _ in range(200)) if tuple(cub(v) for v in x)!=x][:30]
res['F4']=sum(frozenset(D(p) for p in curveA(x))!=curveS(x) for x in Xn)
res['F5']=all(Dinv(shearS(D(p),PHI))==shearA(p,sig(PHI)) for p in pts)
comb=[shearA(Dinv(shearS(D(p),PHI)),ONE) for p in pts]
res['F6']=(all(comb[i]==shearA(p,add(ONE,sig(PHI))) for i,p in enumerate(pts)), len(set(comb))==820, 'c_total =',add(ONE,sig(PHI)))
for k,v in res.items(): print(k,v)
