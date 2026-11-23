import numpy as np
R,a,S=0.040,0.015,36; mu0=4e-7*np.pi
order=[1,2,4,8,7,5]
def loop(phi,aa,n=60):
    t=np.linspace(0,2*np.pi,n+1)
    return np.stack([(R+aa*np.cos(t))*np.cos(phi),(R+aa*np.cos(t))*np.sin(phi),aa*np.sin(t)],1)
def run(p1,p2,aa,n=8):
    if p2<p1: p2+=2*np.pi
    ph=np.linspace(p1,p2,n+1)
    return np.stack([(R+aa)*np.cos(ph),(R+aa)*np.sin(ph),0*ph],1)
def wire(shift,aa,sense=1):
    slots=[9*b+r for b in range(4) for r in order]
    pts=[]; prev=None
    for s in slots:
        phi=2*np.pi*((s+shift)%S)/S
        if prev is not None:
            d=((phi-prev+np.pi)%(2*np.pi))-np.pi
            pts.append(run(prev,prev+d,aa) if d>=0 else run(prev+d,prev,aa)[::-1])
        L=loop(phi,aa); pts.append(L if sense>0 else L[::-1]); prev=phi
    P=np.concatenate(pts); return P
def mutual(P1,P2):
    d1=np.diff(P1,axis=0); m1=0.5*(P1[1:]+P1[:-1]); d2=np.diff(P2,axis=0); m2=0.5*(P2[1:]+P2[:-1])
    r=np.linalg.norm(m1[:,None,:]-m2[None,:,:],axis=2)
    return mu0/(4*np.pi)*np.sum((d1@d2.T)/r)
jumps=[(order[(i+1)%6]-order[i]) for i in range(6)]
res={'R1 jumps':jumps,'R1 net advance per block':int(sum(((j+4)%9)-4 for j in jumps))}
A=wire(0,a); M=[mutual(A,wire(k,a+0.0005)) for k in range(9)]
res['M(k) uH, k=0..8']=[round(m*1e6,4) for m in M]
res['R2 max |M(k)-M(k+3)|/|M|']=max(abs(M[k]-M[k+3])/abs(M[k]) for k in range(6))
res['R3 |M1-M2|/|M1|']=abs(M[1]-M[2])/abs(M[1])
Mc=[mutual(A,wire(k,a+0.0005,sense=-1)) for k in (0,1)]
res['R4 counter-wound M(0), M(1) uH']=[round(m*1e6,4) for m in Mc]
# self-inductance proxy: mutual with a copy displaced by the wire radius (0.25 mm)
L=mutual(A,wire(0,a+0.00025)); res['L (uH, thin-wire proxy)']=round(L*1e6,4); res['R5 coupling M(0)/L']=M[0]/L
for k,v in res.items(): print(k,v)
