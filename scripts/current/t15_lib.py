# The operator from the primes: generator of scaling D on test functions, with the Weil form as inner product.
# Basis: phi_c(r) = exp(-(r-c)^2/2s^2) + exp(-(r+c)^2/2s^2) (frequency side). Gram G_ij = sum over zeros phi_i phi_j,
# H_ij = sum over zeros gamma^2 phi_i phi_j, both computed from the primes by the explicit formula (no zeros used).
import numpy as np
from scipy.special import psi
from scipy.linalg import eigh
def prime_powers(X):
    out=[]; sieve=np.ones(X+1,bool); sieve[:2]=False
    for p in range(2,X+1):
        if sieve[p]:
            sieve[p*p::p]=False; q=p
            while q<=X: out.append((q,np.log(p))); q*=p
    return out
def phi(r,c,s): return np.exp(-(r-c)**2/(2*s*s))+np.exp(-(r+c)**2/(2*s*s))
def forms_from_primes(cs,s,PP,fake=None,dr=0.004):
    R=max(cs)+9*s; r=np.arange(0,R,dr); P=np.array([phi(r,c,s) for c in cs]); K=np.real(psi(0.25+0.5j*r))
    u=np.array([np.log(n if fake is None else fake[i]) for i,(n,l) in enumerate(PP)]); w=np.array([l/np.sqrt(n) for n,l in PP])
    keep=u<np.sqrt(2*40)/ (s/np.sqrt(2)) ; u=u[keep]; w=w[keep]
    C=np.cos(np.outer(u,r)); wt=np.full(len(r),dr); wt[0]=wt[-1]=dr/2
    k=len(cs); G=np.zeros((k,k)); H=np.zeros((k,k)); pc=np.array([phi(0.5j,c,s) for c in cs]).real
    for i in range(k):
        for j in range(i,k):
            for p,M in ((0,G),(1,H)):
                h=P[i]*P[j]*r**(2*p)
                g0=np.sum(h*wt)/np.pi; gu=(C@(h*wt))/np.pi
                val=2*pc[i]*pc[j]*(-0.25)**p - g0*np.log(np.pi) + np.sum(h*K*wt)/np.pi - 2*np.sum(w*gu)
                M[i,j]=M[j,i]=val
    return G,H
def forms_from_zeros(cs,s,zeros):
    V=np.array([phi(zeros,c,s) for c in cs]); return 2*V@V.T, 2*(V*zeros**2)@V.T
def ritz(G,H,tol=1e-7):
    e,U=np.linalg.eigh(G); keep=e>tol*e.max(); T=U[:,keep]/np.sqrt(e[keep])
    ev=np.linalg.eigvalsh(T.T@H@T); return np.sqrt(np.abs(ev))*np.sign(ev), int(keep.sum()), e
