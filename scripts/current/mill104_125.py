def U(n,u0,u1):
    a,b=u0,u1
    if n>=0:
        for _ in range(n): a,b=b,a+b
        return a
    for _ in range(-n): a,b=b-a,a
    return a
F=lambda n:U(n,0,1); L=lambda n:U(n,2,1)
R=range(-10,11)
print("P1:",all(F(x)*F(-x)-(-1)**(r%2)*F(x-r)*F(-(x+r))==F(r)*F(-r) for x in R for r in R))
print("P2:",all((-1)**(a%2)*F(x-a)*F(-(x+a))-(-1)**(r%2)*F(x-r)*F(-(x+r))==(-1)**(a%2)*F(r-a)*F(-(r+a)) for x in R for r in R for a in R))
c=lambda k:F(k)*F(-k)
M=[[c(k)-c(r) for k in range(6)] for r in range(6)]
print("P3 matrix:",M)
print("   equals +-F(k+r)F(k-r):",all(abs(M[r][k])==abs(F(k+r)*F(k-r)) for r in range(6) for k in range(6)))
def eqn12(Uf,CI):
    return all((-1)**(a%2)*Uf(x-a)*Uf(-(x+a))-(-1)**(r%2)*Uf(x-r)*Uf(-(x+r))==(-1)**(a%2)*CI*F(r-a)*F(-(r+a)) for x in R for r in R for a in R)
print("P4: 7F CI=49:",eqn12(lambda n:7*F(n),49)," 7L CI=245:",eqn12(lambda n:7*L(n),245)," L CI=5:",eqn12(L,5))
for u0,u1 in [(1,6),(1,4)]:
    e=u1*u1-u0*u1-u0*u0
    Uf=lambda n,u0=u0,u1=u1:U(n,u0,u1)
    comp=lambda x,k:-(-1)**(k%2)*Uf(x-k)*Uf(-(x+k))
    const=all(comp(x,k)-comp(x,0)==comp(0,k)-comp(0,0) for x in R for k in range(6))
    print(f"P5 U=({u0},{u1}) e={e}: columns constant {const}; row r=0 {[comp(0,k)-comp(0,0) for k in range(6)]} vs e*c_k {[e*c(k) for k in range(6)]}")
    ok6=all(Uf(x-r)*Uf(x+r)-Uf(x-a)*Uf(x+a)==(-1)**((x-r)%2)*e*F(a-r)*F(a+r) for x in R for r in R for a in R)
    print(f"P6 U=({u0},{u1}): modified-lite Catalan with CI={e}: {ok6}")
Uf=lambda n:U(n,1,6)
mix=lambda x,k: (-(-1)**(k%2))*(Uf(x+k)*Uf(-(x-k)) if k in (1,4) else Uf(x-k)*Uf(-(x+k)))
print("P7 mixed-pairing r=0 row:",[mix(0,k)-mix(0,0) for k in range(6)]," (his: 0, 37, -15, 82, -399, 485)")
bal=lambda v: ((v+12)%25)-12
print("P8 powers of 2:",[bal(pow(2,k,25)) for k in range(20)]); print("   powers of 13:",[bal(pow(13,k,25)) for k in range(1,21)], 2*13%25, F(3)*F(-7)-F(5)*F(-5))
# P6 corrected (post-hoc, labelled): two equivalent signed forms
for u0,u1 in [(0,1),(2,1),(1,6),(1,4),(3,-7)]:
    e=u1*u1-u0*u1-u0*u0; Uf=lambda n,u0=u0,u1=u1:U(n,u0,u1); R6=range(-8,9)
    A=all(Uf(x-r)*Uf(x+r)-Uf(x-a)*Uf(x+a)==(-1)**((x-a)%2)*e*F(a-r)*F(a+r) for x in R6 for r in R6 for a in R6)
    B=all(Uf(x-r)*Uf(x+r)-Uf(x-a)*Uf(x+a)==(-1)**((x-r)%2)*(-e)*F(r-a)*F(a+r) for x in R6 for r in R6 for a in R6)
    print(f"P6' U=({u0},{u1}) e={e}: (-1)^(x-a) e F(a-r)F(a+r): {A};  (-1)^(x-r) (-e) F(r-a)F(a+r): {B}")
