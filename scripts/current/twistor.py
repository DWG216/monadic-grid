import numpy as np
rng=np.random.default_rng(20261122); al=rng.normal(size=4)+1j*rng.normal(size=4); be=rng.normal(size=4)+1j*rng.normal(size=4)
def psi(x,weights):
    a0=1j*(al[0]*x[0,0]+al[1]*x[1,0])+al[2]; a1=1j*(al[0]*x[0,1]+al[1]*x[1,1])+al[3]
    b0=1j*(be[0]*x[0,0]+be[1]*x[1,0])+be[2]; b1=1j*(be[0]*x[0,1]+be[1]*x[1,1])+be[3]
    za=-a0/a1; zb=-b0/b1; rho=abs(za-zb)/2; th=2*np.pi*np.arange(96)/96; z=za+rho*np.exp(1j*th); dz=1j*rho*np.exp(1j*th)*(2*np.pi/96)
    f=1/((a0+a1*z)**3*(b0+b1*z)**3); return np.array([np.sum(z**w*f*dz)/(2j*np.pi) for w in weights])
def d(x,A,Ap,weights,h=1e-5):
    e=np.zeros((2,2),complex); e[A,Ap]=h; return (psi(x+e,weights)-psi(x-e,weights))/(2*h)
def box(x,weights,h=2e-3):
    def dd(A,Ap,B,Bp):
        e1=np.zeros((2,2),complex); e1[A,Ap]=h; e2=np.zeros((2,2),complex); e2[B,Bp]=h
        return (psi(x+e1+e2,weights)-psi(x+e1-e2,weights)-psi(x-e1+e2,weights)+psi(x-e1-e2,weights))/(4*h*h)
    a=dd(0,0,1,1); b=dd(0,1,1,0); return np.abs(a-b).max()/max(np.abs(a).max(),np.abs(b).max())
def resid(weights):
    out=[]
    for _ in range(20):
        x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); r=0
        for A in (0,1):
            d0=d(x,A,0,weights); d1=d(x,A,1,weights)
            for k in range(4): r=max(r,abs(d0[k+1]-d1[k])/max(abs(d0[k+1]),abs(d1[k])))
        out.append(r)
    return max(out),min(out)
r,_=resid([0,1,2,3,4]); print(f"E1 helicity-2 field equations: max relative residual {r:.2e} ->",'PASS' if r<1e-6 else 'FAIL')
bx=max(box(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)),[0,1,2,3,4]) for _ in range(20)); print(f"E1 wave equation: max relative residual {bx:.2e} ->",'PASS' if bx<1e-6 else 'FAIL')
rn,rmin=resid([0,2,4,6,8]); print(f"E1-null scrambled weights: residual min {rmin:.2e}, max {rn:.2e} ->",'PASS' if rmin>1e-2 else 'FAIL')
a=1.3
def K(z,extra=0.0):
    u=abs(z[0])**2+abs(z[1])**2; s=np.sqrt(u*u+a**4); return s+a*a*np.log(u/(a*a+s))+extra*u*u
def det(z,extra=0.0,h=1e-3):
    def D(f,i,bar):   # Wirtinger derivative by central differences
        e=np.zeros(2,complex); e[i]=h; fx=lambda w:(f(w+e)-f(w-e))/(2*h); fy=lambda w:(f(w+1j*e)-f(w-1j*e))/(2*h)
        return (lambda w: 0.5*(fx(w)+1j*fy(w))) if bar else (lambda w: 0.5*(fx(w)-1j*fy(w)))
    f=lambda w: K(w,extra); H=np.array([[D(D(f,j,True),i,False)(z) for j in range(2)] for i in range(2)]); return np.linalg.det(H).real
pts=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(20)]
dv=np.array([det(z) for z in pts]); print(f"E2 Eguchi-Hanson det of the Kahler metric: min {dv.min():.7f}, max {dv.max():.7f} ->",'PASS' if np.abs(dv-1).max()<1e-5 else 'FAIL')
dn=np.array([det(z,0.05) for z in pts]); print(f"E2-null perturbed potential: det ranges {dn.min():.3f} .. {dn.max():.3f} ->",'PASS' if dn.max()-dn.min()>1e-2 else 'FAIL')
