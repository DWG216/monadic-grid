import numpy as np
from scipy.special import jv
exec(open('t8_lib.py').read())   # g (201 zeros), rho, zp = zeta'(rho), taper, mu, lam, S, jumps
def jacobi(ev,w):
    """Lanczos: Jacobi matrix with eigenvalues ev and e1-spectral weights w (w >= 0). Returns a, b, Q (rows = Lanczos vectors in eigen coordinates)."""
    n=len(ev); q=np.sqrt(w/w.sum()); Q=[q]; a=[]; b=[]; qprev=np.zeros(n); beta=0
    for k in range(n):
        v=ev*Q[-1]-beta*qprev; al=Q[-1]@v; v-=al*Q[-1]
        for _ in range(2):
            for u in Q: v-=(u@v)*u
        a.append(al); beta=np.linalg.norm(v)
        if k<n-1: b.append(beta); qprev=Q[-1]; Q.append(v/beta)
    return np.array(a),np.array(b),np.array(Q)
def eigerr(a,b,ev): return np.abs(np.sort(np.linalg.eigvalsh(np.diag(a)+np.diag(b,1)+np.diag(b,-1)))-np.sort(ev)).max()
def tri(a,b,x): y=a*x; y[:-1]+=b*x[1:]; y[1:]+=b*x[:-1]; return y
def kpm(a,b,f,us,K=None):
    """<f, exp(iuJ) e1> for each u, from the entries a, b only (Chebyshev recurrence; no diagonalisation)."""
    n=len(a); lo=min(a.min()-2*b.max(),a.min()); hi=a.max()+2*b.max()   # Gershgorin
    c0=(hi+lo)/2; r=(hi-lo)/2*1.01
    if K is None: K=int(r*max(us))+60
    T0=np.zeros(n); T0[0]=1.0; T1=(tri(a,b,T0)-c0*T0)/r
    mom=[np.conj(f)@T0, np.conj(f)@T1]
    for _ in range(K-2):
        T2=2*(tri(a,b,T1)-c0*T1)/r-T0; mom.append(np.conj(f)@T2); T0,T1=T1,T2
    mom=np.array(mom); k=np.arange(K); cf=np.where(k==0,1,2)*(1j)**k
    return np.array([np.exp(1j*u*c0)*np.sum(cf*jv(k,u*r)*mom) for u in np.atleast_1d(us)])
def old_detector(a,xs):
    k=np.arange(len(a)); d=a-np.polyval(np.polyfit(k,a,3),k)
    return np.array([abs(np.sum(d*np.exp(1j*a*x)))**2 for x in xs])
def peak(Sfun,u0,d=0.04):
    """height of |S| at u0 relative to its median over a window +-0.5 (excluding +-d)."""
    us=np.linspace(u0-0.5,u0+0.5,201); v=np.abs(Sfun(us)); m=np.abs(us-u0)>d
    return np.abs(Sfun(np.array([u0])))[0]/np.median(v[m])
