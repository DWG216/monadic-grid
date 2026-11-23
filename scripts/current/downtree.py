import numpy as np
from scipy.special import zeta, loggamma, gamma
phi=(1+5**.5)/2
def F(n):
    a,b=0,1
    for _ in range(abs(n)): a,b=b,a+b
    return a if n>=0 else (-1)**(abs(n)+1)*a
U=lambda x: x/(1-x-x*x); D=lambda x: -x/(1-x-x*x)
x=0.3; s=sum(F(n)*x**n for n in range(1,200)); print(f"T1 series {s:.15f} closed {U(x):.15f} diff {abs(s-U(x)):.1e}")
x=3.0; s=sum(F(-m)*x**(-m) for m in range(0,200)); print(f"T2 series {s:.15f} closed {D(x):.15f} diff {abs(s-D(x)):.1e}")
print(f"   golden annulus: {1/phi:.4f} <= |x| <= {phi:.4f}; at x=1 upward partial sums: {[sum(F(n) for n in range(1,k)) for k in (5,10,20)]}")
rng=np.random.default_rng(20261116); z=rng.normal(size=20)*2+1j*rng.normal(size=20)*2
print(f"T3 max |U+D| over 20 complex x: {np.max(np.abs(U(z)+D(z))):.1e}")
Lam=lambda s,zs: np.pi**(-s/2)*gamma(s/2)*zs
print(f"T4 Lambda(2)={Lam(2,zeta(2)):.12f} Lambda(-1)={Lam(-1,-1/12):.12f} pi/6={np.pi/6:.12f}")
print(f"T4 Lambda(4)={Lam(4,zeta(4)):.12f} Lambda(-3)={Lam(-3,1/120):.12f} pi^2/90={np.pi**2/90:.12f}")
for e in (1e-3,1e-5):
    print(f"T5 eps={e}: eps*Lambda(1+eps)={e*Lam(1+e,zeta(1+e)):.5f}  eps*Lambda(eps)=eps*Lambda(1-eps) by mirror={e*Lam(1-e,zeta(1-e) if False else None) if False else e*np.pi**(-(1-e)/2)*gamma((1-e)/2)*(-1/e+0.5772156649):.5f}")
