import numpy as np, itertools
from fractions import Fraction
from functools import lru_cache
def mk(k):
    l=k+2
    def qn(n): return np.sin(n*np.pi/l)/np.sin(np.pi/l)
    @lru_cache(None)
    def qf(n): return 1.0 if n<=0 else qf(n-1)*qn(n)
    def adm(a,b,c):  # doubled spins
        return (a+b+c)%2==0 and abs(a-b)<=c<=a+b and a+b+c<=2*k
    def D(a,b,c): return np.sqrt(qf((a+b-c)//2)*qf((a-b+c)//2)*qf((-a+b+c)//2)/qf((a+b+c)//2+1))
    def sixj(j1,j2,j3,j4,j5,j6):
        tri=[(j1,j2,j3),(j1,j5,j6),(j4,j2,j6),(j4,j5,j3)]
        if not all(adm(*t) for t in tri): return 0.0
        lo=max(sum(t) for t in tri)//2; hi=min(j1+j2+j4+j5,j2+j3+j5+j6,j3+j1+j6+j4)//2; s=0
        for z in range(lo,hi+1):
            s+=(-1)**z*qf(z+1)/(qf(z-(j1+j2+j3)//2)*qf(z-(j1+j5+j6)//2)*qf(z-(j4+j2+j6)//2)*qf(z-(j4+j5+j3)//2)*
               qf((j1+j2+j4+j5)//2-z)*qf((j2+j3+j5+j6)//2-z)*qf((j3+j1+j6+j4)//2-z))
        return np.prod([D(*t) for t in tri])*s
    def F(a,b,c,d):
        E=[e for e in range(2*k+1) if adm(a,b,e) and adm(e,c,d)]; Fs=[f for f in range(2*k+1) if adm(b,c,f) and adm(a,f,d)]
        M=np.array([[(-1)**((a+b+c+d)//2)*np.sqrt(qn(e+1)*qn(f+1))*sixj(a,b,e,c,d,f) for f in Fs] for e in E]); return E,Fs,M
    def R(j,c): return (-1)**((2*j-c)//2)*np.exp(2j*np.pi/l*(c*(c+2)/8-j*(j+2)/8))
    return qn,adm,F,R
def order(z,maxden=500):
    x=(np.angle(z)/(2*np.pi))%1; f=Fraction(x).limit_denominator(maxden)
    return f.denominator if abs(float(f)-x)<1e-9 else None
hits=[]
for k in range(3,61):
    if k==4: continue
    qn,adm,F,R=mk(k)
    for j in range(1,k+1):           # doubled spin
        d=qn(j+1)
        if abs(d*d-round(d*d))<1e-9: continue   # frozen strand
        for Y in range(0,2*k+1):
            ch=[c for c in range(0,2*k+1) if adm(j,j,c) and adm(c,j,Y)]
            if len(ch)!=2: continue
            n=order(R(j,ch[1])/R(j,ch[0]))
            if n in (3,4,5): hits.append((k,j,Y,n,ch,d*d))
for n,name in [(3,'tetrahedral'),(4,'octahedral'),(5,'icosahedral')]:
    h=[x for x in hits if x[3]==n]
    print('U1 %-11s windows from fluid strands: %d | first few (k, spin j, target Y, d^2):'%(name,len(h)),[(x[0],x[1]/2,x[2]/2,round(x[5],4)) for x in h[:6]])
