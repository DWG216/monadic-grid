# Amended after sanity run 1 (t22_run1.log): run 1 integrated rho ~ -1/lam directly from lam=1e-6 and the
# singular part swamped the result (null control gave 1e-4). Here the singular part is removed analytically:
# rho = -1/lam + delta; D = -(ln A - 2 ln lam) obeys D' = 2 Re delta. Same predictions, same thresholds.
import numpy as np
def run(Psi0,Phi00,lam_end=0.05,n=20000):
    l0=1e-4
    d=Phi00*l0/3+abs(Psi0)**2*l0**3/45; s=Psi0*l0/3; D=Phi00*l0**2/3+abs(Psi0)**2*l0**4/90
    y=np.array([d,s,D],dtype=complex); lam=l0; h=(lam_end-l0)/n
    def f(l,y):
        d,s,D=y; dr=d.real
        return np.array([-2*d/l+d*d+s*np.conj(s)+Phi00, -2*s/l+2*dr*s+Psi0, 2*dr])
    for i in range(n):
        k1=f(lam,y);k2=f(lam+h/2,y+h/2*k1);k3=f(lam+h/2,y+h/2*k2);k4=f(lam+h,y+h*k3)
        y=y+h/6*(k1+2*k2+2*k3+k4); lam+=h
    d,s,D=y
    return lam,s/lam,d.real/lam**3,D.real
res={}
P=0.8*np.exp(0.7j)
lam,s,d,D=run(P,0)
res['S1 sigma/lam / (Psi0/3)']=complex(s/(P/3))
res['S1 delta/lam^3 / (|P|^2/45)']=float(d/(abs(P)**2/45))
res['S1 deficit/lam^4 / (|P|^2/90)']=float(D/lam**4/(abs(P)**2/90))
lam,s,d,D2=run(0,0.5)
res['S2 deficit/lam^2 / (Phi00/3)']=float(D2/lam**2/(0.5/3))
lam,s,d,DA=run(P,0); lam,s,d,DB=run(2*P*np.exp(1.3j),0)
res['S3 ratio (expect 4)']=float(DB/DA)
lam,s,d,D0=run(0,0)
res['C0 deficit']=float(abs(D0))
for k,v in res.items(): print(k,v)
