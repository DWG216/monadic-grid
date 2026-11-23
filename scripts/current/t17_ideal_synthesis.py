import itertools, math
def hnf2(vecs):
    # canonical basis {(a,b),(0,d)} of the Z-lattice spanned by vecs in Z^2
    rows=[list(v) for v in vecs if v!=(0,0)]
    while sum(1 for r in rows if r[0]!=0)>1:
        rows.sort(key=lambda r:(r[0]==0, abs(r[0])))
        p=rows[0]
        for r in rows[1:]:
            if r[0]!=0:
                q=r[0]//p[0]; r[0]-=q*p[0]; r[1]-=q*p[1]
    rows.sort(key=lambda r:(r[0]==0, abs(r[0])))
    top=rows[0]
    if top[0]<0: top=[-top[0],-top[1]]
    import math
    d=0
    for r in rows[1:]: d=math.gcd(d,r[1])
    b=top[1]%d if d else top[1]
    return (top[0],b,0,d)
D=-5
def mul(a,b): return (a[0]*b[0]+D*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def lattice(gens):
    vecs=[]
    for g in gens:
        vecs+= [g, mul(g,(0,1))]
    return hnf2(vecs)
def ideal_mul(A,B): return [mul(a,b) for a in A for b in B]
w=(0,1)
P2=[(2,0),(1,1)]; P3=[(3,0),(1,1)]; P3c=[(3,0),(1,-1)]
norm=lambda a:a[0]**2-D*a[1]**2
res={}
res['I1_products']= mul((2,0),(3,0))==(6,0) and mul((1,1),(1,-1))==(6,0)
small={norm((x,y)) for x in range(-5,6) for y in range(-3,4)}
res['I1_no_norm_2_3']= (2 not in small) and (3 not in small)
L=lattice
res['I2_P2sq=(2)']= L(ideal_mul(P2,P2))==L([(2,0)])
res['I2_P3P3c=(3)']= L(ideal_mul(P3,P3c))==L([(3,0)])
res['I2_P2P3=(1+w)']= L(ideal_mul(P2,P3))==L([(1,1)])
res['I2_P2P3c=(1-w)']= L(ideal_mul(P2,P3c))==L([(1,-1)])
six=L(ideal_mul(ideal_mul(P2,P2),ideal_mul(P3,P3c)))
res['I2_(6)=P2^2P3P3c']= six==L([(6,0)])
res['I3_nonprincipal']= res['I1_no_norm_2_3']
Q=[(2,0),(0,1)]; 
res['C2_Q_is_whole_ring']= L(Q)==L([(1,0)])
# C1 Gaussian integers: factorizations of 6 into irreducibles up to units
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
gn=lambda a:a[0]**2+a[1]**2
units=[(1,0),(-1,0),(0,1),(0,-1)]
def assoc(a): return min(gmul(a,u) for u in units)
irr=set()
for x in range(-6,7):
  for y in range(-6,7):
    n=gn((x,y))
    if n>1 and 36%n==0:
      ok=all(not(1<gn((p,q))<n and n%gn((p,q))==0 and any(gmul((p,q),(r,s))==(x,y) for r in range(-6,7) for s in range(-6,7))) for p in range(-6,7) for q in range(-6,7))
      if ok: irr.add(assoc((x,y)))
irr=sorted(irr)
facts=set()
for k in range(1,5):
  for combo in itertools.combinations_with_replacement(irr,k):
    prod=(1,0)
    for c in combo: prod=gmul(prod,c)
    if prod in [gmul((6,0),u) for u in units]: facts.add(combo)
res['C1_Zi_parses_of_6']=len(facts)
for k,v in res.items(): print(k,v)
