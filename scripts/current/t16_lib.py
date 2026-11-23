# More on the operator: general L-function (even real character mod q), prime cutoffs, ablations.
exec(open('t15_lib.py').read()); from scipy.special import loggamma
from math import factorial
def forms(cs,s,PP,q=1,chi=None,pole=True,use_primes=True,dr=0.004):
    R=max(cs)+9*s; r=np.arange(0,R,dr); P=np.array([phi(r,c,s) for c in cs]); K=np.real(psi(0.25+0.5j*r))
    u=np.array([np.log(n) for n,l in PP]); w=np.array([l/np.sqrt(n)*(1 if chi is None else chi(n)) for n,l in PP])
    keep=(u<np.sqrt(80)/(s/np.sqrt(2)))&(w!=0); u=u[keep]; w=w[keep]
    C=np.cos(np.outer(u,r)); wt=np.full(len(r),dr); wt[0]=wt[-1]=dr/2
    k=len(cs); G=np.zeros((k,k)); H=np.zeros((k,k)); pc=np.array([phi(0.5j,c,s) for c in cs]).real
    for i in range(k):
        for j in range(i,k):
            for p,M in ((0,G),(1,H)):
                h=P[i]*P[j]*r**(2*p); g0=np.sum(h*wt)/np.pi
                val=(2*pc[i]*pc[j]*(-0.25)**p if pole else 0.0) + g0*np.log(q/np.pi) + np.sum(h*K*wt)/np.pi
                if use_primes and len(u): val-=2*np.sum(w*((C@(h*wt))/np.pi))
                M[i,j]=M[j,i]=val
    return G,H
chi5=lambda n: (0,1,-1,-1,1)[n%5]
_B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510]
def hurwitz(s,a,N=None):
    if N is None: N=int(abs(s.imag)/np.pi)+200
    n=np.arange(N); tot=np.sum((n+a)**(-s))+(N+a)**(1-s)/(s-1)+0.5*(N+a)**(-s); fac=s; pw=(N+a)**(-s-1)
    for k in range(1,9): tot+=_B[k-1]/factorial(2*k)*fac*pw; fac*=(s+2*k-1)*(s+2*k); pw/=(N+a)**2
    return tot
def Zchi5(t):
    s=0.5+1j*t; L=5**(-s)*sum(chi5(a)*hurwitz(s,a/5) for a in range(1,5)); th=t/2*np.log(5/np.pi)+np.imag(loggamma(0.25+0.5j*t)); return (np.exp(1j*th)*L).real
def zeros_chi5(lo,hi,step=0.02):
    ts=np.arange(lo,hi,step); zs=np.array([Zchi5(t) for t in ts]); out=[]
    for i in np.where(zs[:-1]*zs[1:]<0)[0]:
        a,b=ts[i],ts[i+1]
        for _ in range(40):
            m=(a+b)/2
            if Zchi5(a)*Zchi5(m)<=0: b=m
            else: a=m
        out.append((a+b)/2)
    return np.array(out)
