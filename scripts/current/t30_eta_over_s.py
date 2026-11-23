import numpy as np
def run(sig0,P,lam1,kap,n=200000):
    # integrate backward from p (lam=0) to lam1<0: theta(0)=0, sigma(0)=sig0
    h=lam1/n; lam=0.0; th=0.0; sg=complex(sig0); lnA=0.0; fl=0.0
    def f(l,y):
        th,sg,lnA,fl=y
        s2=2*abs(sg)**2
        return np.array([-th*th/2-s2, -th*sg+P, th, kap*abs(l)*s2])  # fl accumulates int sigma_v^2 dv = int kappa |lam| s2 dlam
    y=np.array([th,sg,lnA,fl],dtype=complex)
    for i in range(n):
        k1=f(lam,y);k2=f(lam+h/2,y+h/2*k1);k3=f(lam+h/2,y+h/2*k2);k4=f(lam+h,y+h*k3)
        y=y+h/6*(k1+2*k2+2*k3+k4); lam+=h
    th,sg,lnA,fl=y
    dA=np.exp(-lnA.real)-1        # area at p relative to area at lam1 (growth toward p is the shear-driven change)
    G=1.0; s=1/(4*G)
    diS=s*abs(dA)                 # entropy produced = s * |area change from shear|
    T=kap/(2*np.pi)
    flux=abs(fl.real)/kap         # int sigma_v^2 dv: dv = dlam/(kappa lam), sigma_v = kappa lam sigma_lam -> kappa lam s2 dlam ... /kappa^? see below
    # sigma_v^2 dv = (kappa lam)^2 s2 * dlam/(kappa lam) = kappa lam s2 dlam  (fl already holds this)
    flux=abs(fl.real)
    eta=diS*T/(2*flux)
    return eta/s
res={}
for lam1 in [-1e-1,-1e-2,-1e-3]:
    res[f'V1 lam1={lam1}']=run(0.3+0.2j,0.0,lam1,1.0)
target=1/(4*np.pi)
res['V1 rel err at 1e-3']=abs(res['V1 lam1=-0.001']-target)/target
vals=[run(s0,P,-1e-3,k) for s0 in [0.3+0.2j,1.1] for P in [0.0,0.5-0.4j] for k in [0.5,1.0,2.0]]
res['V2 max rel dev']=max(abs(v-target)/target for v in vals)
res['target 1/4pi']=target
for k,v in res.items(): print(k,v)
