import numpy as np
G=6.674e-11; hbar=1.0546e-34
def geom(m,dx,D,t):
    xs={'L':-dx/2,'R':dx/2}; A0=0.0; B0=D
    r=lambda i,j: abs((B0+xs[j])-(A0+xs[i]))
    return {(i,j):G*m*m*t/(hbar*r(i,j)) for i in 'LR' for j in 'LR'}
def concurrence(rho):
    sy=np.array([[0,-1j],[1j,0]]); YY=np.kron(sy,sy)
    R=rho@YY@rho.conj()@YY
    ev=np.sqrt(np.abs(np.sort(np.linalg.eigvals(R).real)[::-1]))
    return max(0.0,ev[0]-ev[1]-ev[2]-ev[3])
idx={'L':0,'R':1}
def quantum_state(ph):
    psi=np.zeros(4,dtype=complex)
    for (i,j),p in ph.items(): psi[2*idx[i]+idx[j]]=0.5*np.exp(1j*p)
    return np.outer(psi,psi.conj())
def meanfield_state(m,dx,D,t):
    ph=geom(m,dx,D,t)
    # A's branch i feels B's mean density (1/2 each); likewise B
    a=np.array([0.5*np.exp(1j*(0.5*ph[(i,'L')]+0.5*ph[(i,'R')])) for i in 'LR'])*np.sqrt(2)
    b=np.array([0.5*np.exp(1j*(0.5*ph[('L',j)]+0.5*ph[('R',j)])) for j in 'LR'])*np.sqrt(2)
    psi=np.kron(a,b)/np.sqrt(2)/np.sqrt(2)*2/ np.sqrt(np.vdot(np.kron(a,b),np.kron(a,b)).real)*np.sqrt(np.vdot(np.kron(a,b),np.kron(a,b)).real)/2
    psi=np.kron(a,b); psi/=np.linalg.norm(psi)
    return np.outer(psi,psi.conj())
def copied_state(m,dx,D,t):
    ph=geom(m,dx,D,t); rho=np.zeros((4,4),dtype=complex)
    # gravity copies each mass's path: both paths recorded -> mixture over outcomes (i,j), each a product of definite paths
    for i in 'LR':
        for j in 'LR':
            v=np.zeros(4,dtype=complex); v[2*idx[i]+idx[j]]=1
            rho+=0.25*np.outer(v,v)
    return rho
def dephase(rho,gamma,t):
    f=np.exp(-gamma*t); out=rho.copy()
    for a in range(4):
        for b in range(4):
            ai,aj=divmod(a,2); bi,bj=divmod(b,2)
            out[a,b]*=(f if ai!=bi else 1)*(f if aj!=bj else 1)
    return out
m,dx,D,t=1e-14,250e-6,450e-6,2.5
res={}
ph=geom(m,dx,D,t); dphi=ph[('R','L')]+ph[('L','R')]-ph[('L','L')]-ph[('R','R')]
res['phase difference (rad)']=float(dphi)
res['S1 concurrence']=concurrence(quantum_state(ph))
res['S2 concurrence max over t']=max(concurrence(meanfield_state(m,dx,D,tt)) for tt in np.linspace(0.1,5,50))
rc=copied_state(m,dx,D,t); res['S3 concurrence']=concurrence(rc)
rA=np.array([[rc[0,0]+rc[1,1],rc[0,2]+rc[1,3]],[rc[2,0]+rc[3,1],rc[2,2]+rc[3,3]]])
res['S3 path coherence of A']=float(abs(rA[0,1]))
gs=np.logspace(-4,1,400); last=None
for g in gs:
    if concurrence(dephase(quantum_state(ph),g,t))>1e-9: last=g
res['S4 largest gamma with C>0 (1/s)']=float(last)
res['control m=1e-20 S1 concurrence']=concurrence(quantum_state(geom(1e-20,dx,D,t)))
for k,v in res.items(): print(k,v)
