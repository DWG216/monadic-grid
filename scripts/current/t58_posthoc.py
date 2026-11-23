import itertools, random
random.seed(3)
src=open('t58_googly2.py').read()
exec(src.split('# ---------- A')[0]); exec(src[src.index('def ring'):src.index('out={}')])
mul,add,sg,pw=ring(3)
E=[(a,b) for a in range(3) for b in range(3)]; Z0=(0,0)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def normp(v):
    k=next(i for i,c in enumerate(v) if c!=Z0); inv=next(y for y in E if mul(y,v[k])==(1,0))
    return tuple(mul(inv,c) for c in v)
# f = omega0^4 (pi0 pi1)^3 ; flow: omega1 -> omega1 - df/domega0 = omega1 - omega0^3 (pi0 pi1)^3   (4 = 1 mod 3)
def Phi(Z):
    w0,w1,p0,p1=Z; return (w0, add(w1, neg(mul(pw(w0,3),pw(mul(p0,p1),3)))), p0, p1)
print('omega0^3 equals the Frobenius (hand swap) of omega0 on F9:',all(pw(x,3)==sg(x) for x in E))
pts=sorted(set(normp(v) for v in itertools.product(E,repeat=4) if any(c!=Z0 for c in v)))
wd=all(normp(Phi(tuple(mul(l,c) for c in p)))==normp(Phi(p)) for p in pts for l in E[1:])
print('well defined:',wd,' bijective:',len(set(normp(Phi(p)) for p in pts))==820)
Pi=sorted(set((p[2],p[3]) for p in pts if (p[2],p[3])!=(Z0,Z0) and (p[0],p[1])==(Z0,Z0)))
def curve(x,deform):
    a,b,c,d=x; S=set()
    for p0,p1 in Pi:
        Z=(add(mul(a,p0),mul(b,p1)),add(mul(c,p0),mul(d,p1)),p0,p1); S.add(normp(Phi(Z)) if deform else normp(Z))
    return frozenset(S)
M=list(itertools.product(E,repeat=4))
C0={x:curve(x,False) for x in M}; C1={x:curve(x,True) for x in M}
print('curve sizes',set(len(c) for c in C1.values()))
sample=random.sample(M,20); ch=0; counts=[]
for x in sample:
    n0={y for y in M if y!=x and C0[x]&C0[y]}; n1={y for y in M if y!=x and C1[x]&C1[y]}
    ch+= n0!=n1; counts.append(len(n1))
print('deformed null counts',sorted(set(counts)),' x with changed null set:',ch,'/20')
