import cmath, math, itertools, random
def F(n):
    a,b=0,1
    if n>=0:
        for _ in range(n): a,b=b,a+b
        return a
    for _ in range(-n): a,b=b-a,a
    return a
L=lambda n:F(n+1)+F(n-1)
ok=all(F(2*n-1)==F(n)**2+F(n-1)**2 and F(2*n)==F(n+1)**2-F(n-1)**2 for n in range(-20,21))
print("S1 doubling formulas:",ok,"; roots of x = x^2 (v, iv, ii with F(0)=0): {0, 1}; of x = -x^2 (i): {0, -1}")
random.seed(1); res=0
for _ in range(1000):
    f0=random.uniform(-3,3); f2=(1+random.choice([1,-1])*math.sqrt(1+4*f0*f0))/2
    z=complex(f2,f0); res=max(res,abs(z*z+1j*f0*(1-2*f2)-z))
print("S2 max residual of z = z^2 + iF(0)(1-2F(2)) given (v):",f"{res:.1e}","; F(0)=0: z in {0 (|2z|=0 attracting), 1 (|2z|=2 repelling)}")
phi=(1+5**.5)/2
print("S3 phi, -1/phi fixed by z^2-1:",abs(phi**2-1-phi)<1e-12,abs((1/phi)**2-1+1/phi)<1e-12,"|2z|:",round(2*phi,3),round(2/phi,3))
z0=0
for _ in range(1001): z0=z0*z0-1
print("   c=-1 orbit after 1001 steps:",z0,"-> 2-cycle 0, -1")
def period(c,N=100000,tol=1e-8):
    z=0j
    for _ in range(N):
        z=z*z+c
        if abs(z)>2: return None
    w=z
    for p in range(1,100):
        w=w*w+c
        if abs(w-z)<tol: return p
    return None
def probe(p,q):
    t=2*math.pi*p/q; card=cmath.exp(1j*t)/2-cmath.exp(2j*t)/4
    out=card/abs(card) if abs(card)>0 else 1
    for k in range(1,200):
        c=card+out*k*0.002/q**2
        r=period(c)
        if r: return r
    return None
S4=[(F(n-1),F(n),probe(F(n-1),F(n))) for n in range(3,9)]
print("S4 golden convergents (p, q, period):",S4," null 2/7:",probe(2,7))
s5=5**.5; Fc=lambda u:(phi**u-math.cos(math.pi*u)*phi**(-u))/s5
print("S5 F(2t)/F(t):",[round(Fc(2*t)/Fc(t),6) for t in (0.1,0.01,0.001,1e-5)],"; F(0) = L(0)F(0):",F(0)==L(0)*F(0))
ex=[F(4)*F(-4)-(-1)*F(3)*F(-5), F(7)*F(-7)-(-1)*F(6)*F(-8), F(5)*F(-5)-F(3)*F(-7), F(10)*F(-10)-(-1)*F(7)*F(-13), F(1)*F(-1)+(-1)*F(-1)*F(-1)]  # p.54 rewritten form: F(0)F(-0) = F(r)F(-r) + (-1)^r F(x-r)F(-(x+r)), x=0, r=1
print("S6 worked examples:",ex," (printed 1, 1, -1, 4, 0)")
# S7: a = a^2+b^2, b = c^2-a^2, c = c^2+b^2. Exact case analysis: a, c roots of y^2-y+b^2; b=(c-a)(c+a).
sols=[(0,0,0),(1,0,1)]
for sb in (1,-1):
    b=sb/s5; c=(1+b)/2; a=(1-b)/2; sols.append((a,b,c))
chk=[max(abs(a-a*a-b*b),abs(b-c*c+a*a),abs(c-c*c-b*b)) for a,b,c in sols]
print("S7 solutions (F(-1),F(0),F(1)):",[tuple(round(v,6) for v in s) for s in sols],"residuals",[f"{r:.0e}" for r in chk])
g=lambda n:phi**n/s5; h=lambda n:-(-1/phi)**n/s5
print("   = vacuum, Fibonacci, phi^n/sqrt5 at n=-1,0,1:",[round(g(n),6) for n in (-1,0,1)],", -psi^n/sqrt5:",[round(h(n),6) for n in (-1,0,1)])
print("   each pure mode satisfies all doubling formulas:",all(abs(f(2*n)-(f(n+1)**2-f(n-1)**2))<1e-9 and abs(f(2*n-1)-(f(n)**2+f(n-1)**2))<1e-9 for f in (g,h) for n in range(-8,9)))
print("   but a constant multiple k*phi^n/sqrt5 does not (k=2):",abs(2*g(2)-(4*g(2)**2-4*g(0)**2)*1)<1e-9)
mirror=[s for s in sols if abs(s[0]-s[2])<1e-12]
print("S8 mirror condition F(1)=F(-1) keeps:",mirror)
