import numpy as np
n=256; L=1.0; xs=np.linspace(-L,L,n,endpoint=False); X,Y=np.meshgrid(xs,xs)
r=np.hypot(X,Y); ph=np.arctan2(Y,X); w=0.25
def obj(l): return (r/w)**abs(l)*np.exp(1j*l*ph)*np.exp(-(r/w)**2)*0.5
def winding(F):
    t=np.linspace(0,2*np.pi,400,endpoint=False); rr=w/2
    ix=((rr*np.cos(t)+L)/(2*L)*n).astype(int); iy=((rr*np.sin(t)+L)/(2*L)*n).astype(int)
    a=np.angle(F[iy,ix]); d=np.diff(np.concatenate([a,a[:1]])); d=(d+np.pi)%(2*np.pi)-np.pi
    return int(np.round(d.sum()/(2*np.pi)))
def corr(A,B): return abs(np.vdot(A,B))/np.linalg.norm(A)/np.linalg.norm(B)
kx=np.fft.fftfreq(n,d=2*L/n)*2*np.pi; KX,KY=np.meshgrid(kx,kx)
def run(l,k):
    O=obj(l); R=np.exp(1j*k*X); I=np.abs(O+R)**2
    S=np.fft.fft2(I); rad=0.45*(k if k>0 else 60)
    def band(c):
        M=(np.hypot(KX-c,KY)<rad); return np.fft.ifft2(S*M)
    p=band(+k)*np.exp(-1j*k*X)   # term conj(R) O ... sign by convention
    m=band(-k)*np.exp(+1j*k*X)
    z=band(0).real-1.0
    return O,p,m,z
res={}
O,p,m,z=run(2,120.0)
# identify which order carries O
a,b=(p,m) if corr(p,O)>corr(m,O) else (m,p)
res['H1 wind,corr']=(winding(a),round(corr(a,O),4))
res['H2 wind,corr(conj O)']=(winding(b),round(corr(b,np.conj(O)),4))
res['H3 wind,corr(|O|^2),min']=(winding(z+0j+1e-9),round(corr(z,np.abs(O)**2),4),round(float(z.min()),4))
O0,p0,m0,z0=run(0,120.0)
res['C1 windings']=(winding(p0),winding(m0),winding(z0+1e-9))
Oi,pi_,mi,zi=run(2,0.0)
res['C2 inline corr']=round(corr(pi_,Oi),4)
for k,v in res.items(): print(k,v)
