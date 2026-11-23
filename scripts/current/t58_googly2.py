import itertools, random
random.seed(2)
# ---------- A: R_k elements (a,b) = a + b phi mod 3^k
def ring(m):
    def mul(x,y): a,b=x;c,d=y; return ((a*c+b*d)%m,(a*d+b*c+b*d)%m)
    def add(x,y): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
    def sg(x): a,b=x; return ((a+b)%m,(-b)%m)     # phi -> 1-phi
    def pw(x,n):
        r=(1,0); 
        while n: 
            if n&1: r=mul(r,x)
            x=mul(x,x); n>>=1
        return r
    return mul,add,sg,pw
out={}
for k in [1,2,3,4]:
    m=3**k; mul,add,sg,pw=ring(m)
    basis=[(1,0),(0,1)]
    A1=all(sg(mul(x,y))==mul(sg(x),sg(y)) for x in [(a,b) for a in range(m) for b in range(m)][:400] for y in basis) and all(sg(sg((a,b)))==(a%m,b%m) for a in range(5) for b in range(5))
    T=pw((0,1),9**(k-1)); A2=(pw(T,8)==(1,0), sg(T)==pw(T,3), pw(T,4)==((-1)%m,0))
    def Sig(Z):
        t=(0,0)
        for i,j in [(0,2),(2,0),(1,3),(3,1)]: t=add(t,mul(Z[i],sg(Z[j])))
        return t
    A3=True
    for _ in range(300):
        Z=[(random.randrange(m),random.randrange(m)) for _ in range(4)]; s=Sig(Z)
        A3&= sg(s)==s
        mm=random.randrange(8); TZ=[mul(pw(T,mm),c) for c in Z]; A3&= Sig(TZ)==mul(pw(T,4*mm),s)
    u=((1)%m,3%m); A4= sg(u)!=pw(u,3) if k>=2 else None
    out[k]=dict(A1=A1,A2=A2,A3=A3,A4=A4); print('k =',k,out[k])
# ---------- B over F9
B1={}
for h2 in range(-4,5):   # 2h
    n=-h2-2   # n = -2h-2
    B1[h2/2]=(n%8==(-n-4)%8)
print('B1 same degree class for helicity h:',B1)
mul,add,sg,pw=ring(3)
E=[(a,b) for a in range(3) for b in range(3)]; Z0=(0,0)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def normp(v):
    k=next(i for i,c in enumerate(v) if c!=Z0); inv=next(y for y in E if mul(y,v[k])==(1,0))
    return tuple(mul(inv,c) for c in v)
def Phi(Z):
    w0,w1,p0,p1=Z; ind=pw(mul(p0,p1),8)
    return (w0, add(w1, neg(mul((2,0),mul(w0,ind)))), p0, p1)
pts=sorted(set(normp(v) for v in itertools.product(E,repeat=4) if any(c!=Z0 for c in v)))
img=[normp(Phi(p)) for p in pts]
# well-defined: Phi(lambda Z) ~ Phi(Z)
wd=all(normp(Phi(tuple(mul(l,c) for c in p)))==normp(Phi(p)) for p in pts[:200] for l in E[1:])
B2=(wd, len(set(img))==len(pts)==820)
Pi=[normp((Z0,Z0,a,b)) for a in E for b in E if (a,b)!=(Z0,Z0)]; Pi=sorted(set((p[2],p[3]) for p in [normp((Z0,Z0,a,b)) for a in E for b in E if (a,b)!=(Z0,Z0)]))
def curve(x,deform):
    a,b,c,d=x; S=set()
    for p0,p1 in Pi:
        w0=add(mul(a,p0),mul(b,p1)); w1=add(mul(c,p0),mul(d,p1)); Z=(w0,w1,p0,p1)
        S.add(normp(Phi(Z)) if deform else normp(Z))
    return frozenset(S)
M=list(itertools.product(E,repeat=4))
C0={x:curve(x,False) for x in M}; C1={x:curve(x,True) for x in M}
B3=(set(len(c) for c in C1.values()),)
cnt={}
for x in M:
    for z in C1[x]: cnt[z]=cnt.get(z,0)+1
B3=B3+(set(cnt.values()),)
def null(C,x): return sum(1 for y in M if y!=x and C[x]&C[y])
sample=random.sample(M,20)
flat=[null(C0,x) for x in sample]; defo=[null(C1,x) for x in sample]
changed=sum(1 for x in sample if {y for y in M if y!=x and C0[x]&C0[y]}!={y for y in M if y!=x and C1[x]&C1[y]})
print('B2',B2); print('B3 curve sizes, twistor-point multiplicities:',B3)
print('B4 flat null counts',set(flat),' deformed null counts',sorted(set(defo)),' x with changed null set:',changed,'/20')
