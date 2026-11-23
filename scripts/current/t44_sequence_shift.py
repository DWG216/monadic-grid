import numpy as np
exec(open('t43_rodin_coil.py').read().split('jumps=')[0])
def wire_seq(kstep,aa):
    o=order[kstep:]+order[:kstep]          # start the doubling cycle kstep steps later
    slots=[9*b+r for b in range(4) for r in o]; pts=[]; prev=None; segs=[]
    for s in slots:
        phi=2*np.pi*(s%S)/S
        if prev is not None:
            d=((phi-prev+np.pi)%(2*np.pi))-np.pi
            pts.append(run(prev,prev+d,aa) if d>=0 else run(prev+d,prev,aa)[::-1])
        pts.append(loop(phi,aa)); prev=phi
    return np.concatenate(pts)
def mutual_c(P1,P2,lam=None):
    d1=np.diff(P1,axis=0); m1=0.5*(P1[1:]+P1[:-1]); d2=np.diff(P2,axis=0); m2=0.5*(P2[1:]+P2[:-1])
    r=np.linalg.norm(m1[:,None,:]-m2[None,:,:],axis=2); K=(d1@d2.T)/r
    if lam is None: return mu0/(4*np.pi)*K.sum()
    s1=np.concatenate([[0],np.cumsum(np.linalg.norm(d1,axis=1))])[:-1]; s2=np.concatenate([[0],np.cumsum(np.linalg.norm(d2,axis=1))])[:-1]
    ph=np.exp(1j*2*np.pi*(s1[:,None]-s2[None,:])/lam)
    return mu0/(4*np.pi)*(K*ph).sum()
A=wire_seq(0,a)
Ltot=np.sum(np.linalg.norm(np.diff(A,axis=0),axis=1))
print('wire length (m):',round(Ltot,3))
Ms=[mutual_c(A,wire_seq(k,a+0.0005)) for k in range(3)]
print('low frequency, shift along the doubling sequence k=0,1,2 (uH):',[round(m*1e6,4) for m in Ms])
for frac in [1.0,0.5]:
    lam=Ltot*frac
    Mh=[mutual_c(A,wire_seq(k,a+0.0005),lam) for k in range(3)]
    print(f'wavelength = {frac} x wire length: |M| (uH) =',[round(abs(m)*1e6,4) for m in Mh],' ratios to k=0:',[round(abs(m)/abs(Mh[0]),3) for m in Mh])
