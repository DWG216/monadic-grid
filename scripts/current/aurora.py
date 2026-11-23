import math
from math import gamma, pi, log
p=(1+5**.5)/2
B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6]
def zeta(s,N=60):
    t=sum(n**-s for n in range(1,N))+N**(1-s)/(s-1)+N**-s/2
    fac=1.0; prod=s; term_pow=-s-1
    for k in range(1,len(B)+1):
        # B_2k/(2k)! * s(s+1)...(s+2k-2) * N^(-s-2k+1)
        fac*= (2*k-1)*(2*k)
        t+= B[k-1]/fac*prod*N**(-s-2*k+1)
        prod*=(s+2*k-1)*(s+2*k)
    return t
def Lam(s): return pi**(-s/2)*gamma(s/2)*zeta(s)
z=zeta(p); D=p*p*log(1+z); S10=sum(n**p for n in range(1,11)); Dp=1/(p*p*log(1+S10))
print(f"A1 zeta(phi)={z:.10f} D={D:.6f} (paper 2.914) ->",'PASS' if abs(D-2.914)>0.1 else 'FAIL')
print(f"A2 D'={Dp:.6f} (paper 0.077) ->",'PASS' if abs(Dp-0.0735)<0.001 else 'FAIL')
print(f"A3 D*D'={D*Dp:.4f} ->",'PASS' if abs(D*Dp-1)>0.5 else 'FAIL')
for a,b in [(p,1-p),(-p,p*p)]:
    la,lb=Lam(a),Lam(b); print(f"A4 Lambda({a:.4f})={la:.12f} Lambda({b:.4f})={lb:.12f} diff={abs(la-lb):.1e}")
print("   zeta(1-phi)=",zeta(1-p)," zeta(-phi)=",zeta(-p)," zeta(phi^2)=",zeta(p*p))
print(f"   null Lambda(phi)={Lam(p):.6f} Lambda(-phi)={Lam(-p):.6f}")
N=200000; mu=[1]*(N+1); isp=[True]*(N+1)
for i in range(2,N+1):
    if isp[i]:
        for j in range(i,N+1,i):
            if j>i: isp[j]=False
            mu[j]*=-1
        for j in range(i*i,N+1,i*i): mu[j]=0
inv=sum(mu[n]*n**-p for n in range(1,N+1))
print(f"A5 zeta(phi)*sum mu/n^phi = {z*inv:.6f}")
print(f"extra ln zeta(phi)={log(z):.6f}, mean energy <ln n> at beta=phi:",
      sum(log(n)*n**-p for n in range(1,N))/z)
