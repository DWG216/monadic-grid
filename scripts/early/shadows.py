# Curvature hands as z / z-bar shadows on a point's sky (Penrose-Petrov quartic). Known math; demonstration.
import numpy as np
v =lambda z: np.array([1-z*z, 1j*(1+z*z), -2*z])      # isotropic (light-like) direction, read with z      -> hand +
vb=lambda z: np.array([1-z*z,-1j*(1+z*z), -2*z])      # same sky read with z-bar                         -> hand -
def quartic(Q,vf):   # coefficients of P(z)=v(z)^T Q v(z), degree 4
    zs=np.exp(2j*np.pi*np.arange(5)/5)*0.7; P=np.array([vf(z)@Q@vf(z) for z in zs])
    return np.linalg.solve(np.vander(zs,5),P)            # highest power first
def directions(c,mirror=False,tol=1e-6):
    c=np.array(c,complex); lead=np.argmax(abs(c)>tol*abs(c).max()); r=list(np.roots(c[lead:])) if lead<4 else []
    out=[np.array([0,0,1.0])]*lead                       # missing degree = roots at infinity
    for z in r:
        n=np.array([2*z.real,2*z.imag,abs(z)**2-1])/(1+abs(z)**2)
        if mirror: n[1]=-n[1]
        out.append(n)
    return out
def fmt(ds): return '  '.join('(%+.2f,%+.2f,%+.2f)'%tuple(d) for d in ds)
def petrov(ds):
    m=[sum(np.linalg.norm(d-e)<1e-3 for e in ds) for d in ds]; mx=max(m)
    return {1:'I (4 distinct)',2:'D or II (repeated)',3:'III',4:'N (one quadruple)'}[mx] if mx<4 or True else ''
cases={}
cases['Schwarzschild (radial = z)']=(np.diag([1.,1,-2]),np.zeros((3,3)))
cases['Plane gravitational wave (along z)']=(np.diag([1.,-1,0]),np.array([[0,1.,0],[1,0,0],[0,0,0]]))
rng=np.random.default_rng(4); A=rng.normal(size=(3,3));A=A+A.T;A-=np.trace(A)/3*np.eye(3); B=rng.normal(size=(3,3));B=B+B.T;B-=np.trace(B)/3*np.eye(3)
cases['Generic curved point (random E, B)']=(A,B)
for name,(E,Bm) in cases.items():
    Qp=E-1j*Bm; Qm=E+1j*Bm
    dp=directions(quartic(Qp,v)); dm=directions(quartic(Qm,vb),mirror=True)
    same=all(min(np.linalg.norm(a-b) for b in dm)<1e-4 for a in dp)
    print('%s\n   hand + light directions: %s\n   hand - light directions: %s\n   same real sky directions: %s | type %s'%(name,fmt(dp),fmt(dm),same,petrov(dp)))
# complexified (not a real spacetime): E, B complex and independent
E=A+0.6j*rng.normal(size=(3,3)); E=(E+E.T)/2; E-=np.trace(E)/3*np.eye(3); Bm=B.astype(complex)
dp=directions(quartic(E-1j*Bm,v)); dm=directions(quartic(E+1j*Bm,vb),mirror=True)
same=all(min(np.linalg.norm(a-b) for b in dm)<1e-4 for a in dp)
print('Complexified point (not real)\n   hand + : %s\n   hand - : %s\n   same real sky directions: %s'%(fmt(dp),fmt(dm),same))
print('   (hand + directions are not even unit-length real directions when roots come from a non-real metric: |n| =',np.round([np.linalg.norm(d) for d in dp],3),')')
