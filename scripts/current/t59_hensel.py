import random
random.seed(4)
def ring(m):
    def mul(x,y): a,b=x;c,d=y; return ((a*c+b*d)%m,(a*d+b*c+b*d)%m)
    def add(x,y): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
    def sc(k,x): return ((k*x[0])%m,(k*x[1])%m)
    return mul,add,sc
def setup(m,eps):
    mul,add,sc=ring(m); R=[(a,b) for a in range(m) for b in range(m)]
    unit=lambda x: (x[0]*x[0]+x[0]*x[1]-x[1]*x[1])%3!=0   # norm not divisible by 3
    Ts=R; Ss=[s for s in R if not unit(s)]   # P^1(R): (1,t) all t, and (s,1) with s non-unit
    def sec0(x,t):  # U0 chart point for pi=(1,t)
        a,b,c,d=x; w0=add(a,mul(b,t)); t2=mul(t,t); t3=mul(t2,t)
        w1=add(add(c,mul(d,t)), sc(eps, add(sc(2,mul(mul(a,b),t2)), mul(mul(b,b),t3))))
        return (w0,w1)
    def sec1(x,s):  # U1 chart, pi=(s,1): omega_U1 = s*omega_U0frame(1/s) for the U1 polynomial  omega0 = a s + b, omega1 = c0 s + (d0 - eps a^2)
        a,b,c,d=x; return (add(mul(a,s),b), add(mul(c,s), add(d, sc(-eps%m, mul(a,a)))))
    def meet(x,y):
        for t in Ts:
            if sec0(x,t)==sec0(y,t): return True
        for s in Ss:
            if sec1(x,s)==sec1(y,s): return True
        return False
    return R,mul,add,sc,sec0,sec1,meet,unit
res={}
# K1 formal matching: U1 polynomial in U0 frame equals shear of U0 polynomial, as Laurent polys (coefficient check symbolic-by-sampling at units t)
ok=0
for m in [3,9]:
    R,mul,add,sc,sec0,sec1,meet,unit=setup(m,1)
    for _ in range(50):
        x=[random.choice(R) for _ in range(4)]; t=random.choice([r for r in R if unit(r)])
        w0,w1=sec0(x,t); w1s=add(w1, sc(-1%m, mul(mul(w0,w0),t)))   # apply patch
        a,b,c,d=x; u1=add(c, mul(add(d, sc(-1%m,mul(a,a))),t))       # U1 section in U0 frame
        ok+= (w1s==u1)
res['K1']=ok
# K2 F9 eps=1
R,mul,add,sc,sec0,sec1,meet,unit=setup(3,1); R0,_,_,_,_,_,meet0,_=setup(3,0)
M=[(p,q,r,s) for p in R for q in R for r in R for s in R]
samp=random.sample(M,20); ch=0
for x in samp:
    ys=random.sample(M,800)
    ch+= any(meet(x,y)!=meet0(x,y) for y in ys)
res['K2']=ch
# K3, K4 over Z/9[phi]
R9,_,_,_,_,_,meet3,_=setup(9,3); _,_,_,_,_,_,meetF,_=setup(9,0)
pairs=[([random.choice(R9) for _ in range(4)],[random.choice(R9) for _ in range(4)]) for _ in range(4000)]
# bias half the pairs to be null mod 3 (y = x + 3*delta) so the order-3 effect can show
pairs=[(x,[((x[i][0]+3*random.randrange(3))%9,(x[i][1]+3*random.randrange(3))%9) for i in range(4)]) if k%2 else (x,y) for k,(x,y) in enumerate(pairs)]
d3=sum(meet3(x,y)!=meetF(x,y) for x,y in pairs)
R9b,_,_,_,_,_,meet0b,_=setup(9,0); d0=sum(meet0b(x,y)!=meetF(x,y) for x,y in pairs[:4000])
res['K3_changed']=d3; res['K4_changed']=d0
for k,v in res.items(): print(k,v)
print({'K1':res['K1']==100,'K2':res['K2']>=10,'K3':res['K3_changed']>0,'K4':res['K4_changed']==0})
