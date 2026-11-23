import numpy as np
def run(Psi0,Phi00,lam_end=0.05,n=200000):
    l0=1e-6; lam=l0; rho=-1/l0+Phi00*l0/3; sig=Psi0*l0/3; lnA=2*np.log(l0)
    h=(lam_end-l0)/n
    def f(l,y):
        r,s,a=y
        return np.array([r*r+s*np.conj(s)+Phi00, 2*r.real*s+Psi0, -2*r.real])
    y=np.array([rho,sig,lnA],dtype=complex)
    for i in range(n):
        k1=f(lam,y);k2=f(lam+h/2,y+h/2*k1);k3=f(lam+h/2,y+h/2*k2);k4=f(lam+h,y+h*k3)
        y=y+h/6*(k1+2*k2+2*k3+k4); lam+=h
    r,s,a=y
    return lam, s/lam, (r.real+1/lam)/lam**3, -(a.real-2*np.log(lam))
res={}
P=0.8*np.exp(0.7j)
lam,s,d,defi=run(P,0)
res['S1 sigma/lam vs Psi0/3']=(complex(s),P/3)
res['S1 drho/lam^3 vs |P|^2/45']=(float(d),abs(P)**2/45)
res['S1 deficit/lam^4 vs |P|^2/90']=(float(defi/lam**4),abs(P)**2/90)
lam,s,d,defi2=run(0,0.5)
res['S2 deficit/lam^2 vs Phi00/3']=(float(defi2/lam**2),0.5/3)
lam,s,d,dA=run(P,0); lam,s,d,dB=run(2*P*np.exp(1.3j),0)
res['S3 ratio (expect 4)']=float(dB/dA)
lam,s,d,d0=run(0,0)
res['C0 deficit']=float(abs(d0))
for k,v in res.items(): print(k,v)
