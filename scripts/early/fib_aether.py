import numpy as np, itertools
from math import comb
phi=(1+5**.5)/2
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1]).astype(complex);I=np.eye(2)
# ---------------- models ----------------
F_fib=np.array([[1/phi,1/np.sqrt(phi)],[1/np.sqrt(phi),-1/phi]])
R_fib=np.diag([np.exp(-4j*np.pi/5),np.exp(3j*np.pi/5)])
s1f=R_fib; s2f=F_fib@R_fib@F_fib
H=np.array([[1,1],[1,-1]])/2**.5
R_is=np.exp(-1j*np.pi/8)*np.diag([1,1j])          # Ising: braid = sqrt(Z)-type up to phase
s1i=R_is; s2i=H@R_is@H
# ---------------- F1 ----------------
print('F1 Fibonacci: F^2=1 %.1e | unitary %.1e %.1e | Yang-Baxter %.1e'%(np.linalg.norm(F_fib@F_fib-I),np.linalg.norm(s1f@s1f.conj().T-I),np.linalg.norm(s2f@s2f.conj().T-I),np.linalg.norm(s1f@s2f@s1f-s2f@s1f@s2f)))
# hexagon (for Fibonacci with these conventions): R_1^{tt} etc. Check standard form: F R F = R^-1 F R^-1 F ... use the braid relation already; plus Fibonacci counting
def fib_dim(n):  # number of fusion trees of n tau with total charge 1
    a={'1':1,'t':0}  # after 0 anyons: vacuum
    a={'1':0,'t':1}  # after 1 anyon
    for _ in range(n-1): a={'1':a['t'],'t':a['1']+a['t']}
    return a['1']
print('   fusion-space dims (total charge 1) for n = 2..12 tau anyons:',[fib_dim(n) for n in range(2,13)])
# ---------------- F2: group growth (projective) ----------------
def key(U):
    U=U/np.sqrt(np.linalg.det(U)); k=np.argmax(abs(U.reshape(-1))>1e-6); U=U*abs(U.reshape(-1)[k])/U.reshape(-1)[k]
    return tuple(np.round(U.reshape(-1),7))
def growth(gens,L):
    seen={key(I):I}; frontier=[I]; out=[]
    for l in range(1,L+1):
        new=[]
        for U in frontier:
            for g in gens:
                V=g@U; k=key(V)
                if k not in seen: seen[k]=V; new.append(V)
        frontier=new; out.append(len(seen))
        if len(seen)>200000: break
    return out,list(seen.values())
gi=[s1i,s2i,np.linalg.inv(s1i),np.linalg.inv(s2i)]; gf=[s1f,s2f,np.linalg.inv(s1f),np.linalg.inv(s2f)]
cnt_i,elems_i=growth(gi,12); cnt_f,elems_f=growth(gf,12)
print('F2 distinct elements (up to phase) by word length 1..12:\n   Ising     ',cnt_i,'\n   Fibonacci ',cnt_f)
# ---------------- F3 ----------------
ev=np.angle(np.linalg.eigvals(s1f)); rel=(ev[1]-ev[0])%(2*np.pi)
print('F3 sigma1 relative phase = %.4f pi -> rotation angle %.4f pi, half-angle %.4f pi (7/10 = 0.7000)'%(rel/np.pi,rel/np.pi,(2*np.pi-rel)/2/np.pi if rel>np.pi else rel/2/np.pi))
th=7*np.pi/10; print('   f(n)=i^(n-1)sin(n th)/sin th at th=7pi/10, |f(n)| n=1..10:',np.round([abs(np.sin(n*th)/np.sin(th)) for n in range(1,11)],3).tolist())
# ---------------- F4: magic ----------------
def M2(psi):
    r=np.outer(psi,psi.conj()); x,y,z=[np.real(np.trace(r@P)) for P in (X,Y,Z)]
    return -np.log2((1+x**4+y**4+z**4)/2), (x,y,z)
def is_stab(b): return min(np.linalg.norm(np.array(b)-s*e) for e in np.eye(3) for s in (1,-1))<1e-7
e0=np.array([1,0],complex)
for name,el in [('Ising',elems_i),('Fibonacci',elems_f)]:
    vals=[M2(U@e0) for U in el]; m=[v[0] for v in vals]; stab=[v[1] for v in vals if is_stab(v[1])]
    uniq=[];
    for b in stab:
        if all(np.linalg.norm(np.array(b)-np.array(c))>1e-6 for c in uniq): uniq.append(b)
    print('F4 %-9s states reached %d | max M2 %.4f (single-qubit max 0.5850) | distinct stabilizer states reached: %d %s'%(name,len(el),max(m),len(uniq),[tuple(np.round(u,3)) for u in uniq]))
# ---------------- F5: spectral gap on PU(2) irreps ----------------
def so3(U):
    U=U/np.sqrt(np.linalg.det(U)); return np.array([[0.5*np.real(np.trace(P@U@Q@U.conj().T)) for Q in (X,Y,Z)] for P in (X,Y,Z)])
def spin_mats(j):
    m=np.arange(j,-j-1,-1); Jp=np.zeros((2*j+1,2*j+1))
    for k in range(1,2*j+1): Jp[k-1,k]=np.sqrt(j*(j+1)-m[k]*(m[k]+1))
    return (Jp+Jp.T)/2,(Jp-Jp.T)/(2j),np.diag(m)
def Dj(U,J):
    U=U/np.sqrt(np.linalg.det(U)); a=np.real(np.trace(U))/2; v=np.real([1j*np.trace(U@P) for P in (X,Y,Z)])/2; s=np.linalg.norm(v)
    if s<1e-12: return np.eye(J[0].shape[0])
    th=2*np.arctan2(s,a); n=v/s; Hh=n[0]*J[0]+n[1]*J[1]+n[2]*J[2]; w,W=np.linalg.eigh(Hh); return (W*np.exp(-1j*th*w))@W.conj().T
ram=2*np.sqrt(3)/4
for name,gens in [('Ising',gi),('Fibonacci',gf)]:
    lam=[]
    for j in range(1,41):
        J=spin_mats(j); T=sum(Dj(g,J) for g in gens)/4
        lam.append(max(abs(np.linalg.eigvals(T))))
    lam=np.array(lam)
    print('F5 %-9s max |eig| over j=1..40: %.4f at j=%d | min %.4f | #j above Ramanujan 0.866: %d'%(name,lam.max(),1+lam.argmax(),lam.min(),(lam>ram+1e-9).sum()))
    np.save('fib_spec_%s.npy'%name,lam)
# ---------------- F6 ----------------
D2=1+phi**2; print('F6 D^2 = 1+phi^2 = %.6f ; 2+phi = %.6f ; phi*sqrt5 = %.6f ; gamma = ln D = %.4f ; (2+phi)^2+2 = %.6f ; 7+5phi = %.6f'%(D2,2+phi,phi*5**.5,0.5*np.log(D2),(2+phi)**2+2,7+5*phi))
