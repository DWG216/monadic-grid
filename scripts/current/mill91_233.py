import random
random.seed(20261121)
def F(n):
    a,b=0,1
    for _ in range(abs(n)): a,b=b,a+b
    return a if n>=0 else (-1)**(-n+1)*a
def L(n): return F(n-1)+F(n+1)
print("N1:",all((F(n-1)*F(-(n+1))-1)%(F(n)**2)==0 for n in range(3,40)), [(F(n-1),F(-(n+1))%F(n)**2,F(n)**2) for n in (4,5,6,7)])
bad=[(n,r) for n in range(4,30) for r in range(1,n) if (F(n-r)*F(n+r))%F(n)**2 in (1,F(n)**2-1)]
print("N2 unit Catalan pairs only r in", sorted(set(r for n,r in bad)), "| r=3 n=5:",F(2)*F(8)%25, "= -(-1)^(n-r)F(r)^2 mod 25:",(-(-1)**(5-3)*F(3)**2)%25)
order=lambda a,m: next(k for k in range(1,m) if pow(a,k,m)==1)
print("N3 orders mod 25:",{a:order(a,25) for a in (2,3,8,13,17,22)})
prs1=[(8,22),(14,9),(13,2),(19,4),(3,17),(9,14)]; prs2=[(8,3),(22,17),(13,23),(2,12),(3,8),(17,22)]
print("N4:",[a*b%25 for a,b in prs1],[a*b%25 for a,b in prs2])
bal=lambda v: ((v+4)%9)-4
for s in range(-12,13):
    if all(bal(5*L(n))==bal(F(n+s)) for n in range(-30,30)): print("N5a shift s =",s)
    if all(bal(2*F(n))==bal(L(n-s)) for n in range(-30,30)): print("N5b shift s =",s)
def U(n,u0,u1):
    a,b=u0,u1
    if n>=0:
        for _ in range(n): a,b=b,a+b
        return a
    for _ in range(-n): a,b=b-a,a
    return a
for u0,u1 in [(1,6),(1,4)]:
    vals=[U(n,u0,u1)*U(n+2,u0,u1)-U(n+1,u0,u1)**2 for n in range(-6,6)]
    print(f"N6 U0={u0},U1={u1}: e={u1*u1-u0*u1-u0*u0}; Cassini values {sorted(set(vals))}; U(-8..8)=",[U(n,u0,u1) for n in range(-8,9)])
def fac(n):
    n=abs(n); f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def ok(e): return all(k%2==0 for p,k in fac(e).items() if p%5 in (2,3))
good=sum(ok(u1*u1-u0*u1-u0*u0) for u0 in range(61) for u1 in range(61) if u1*u1-u0*u1-u0*u0!=0)
tot=sum(1 for u0 in range(61) for u1 in range(61) if u1*u1-u0*u1-u0*u0!=0)
nul=sum(ok(random.randint(1,3000)) for _ in range(tot))
print(f"N7 norms with inert primes to even powers: {good}/{tot}; null random integers: {nul}/{tot} = {nul/tot:.2f}; 29 mod 5 = {29%5}, 11 mod 5 = {11%5}")
