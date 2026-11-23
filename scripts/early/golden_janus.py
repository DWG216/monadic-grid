import numpy as np, itertools
from scipy.linalg import expm
phi=(1+5**.5)/2; R1=np.exp(-4j*np.pi/5); Rt=np.exp(3j*np.pi/5)
print('=== A. The Fibonacci-anyon braid IS a complex Fibonacci recurrence ===')
F=np.array([[1/phi,phi**-.5],[phi**-.5,-1/phi]]); B=F@np.diag([R1,Rt])@F
c=np.exp(3j*np.pi/5); a=c*(R1+Rt); Bn=c*B
print(' normalised braid b=cB obeys b^2 = a b + 1 :',np.allclose(Bn@Bn,a*Bn+np.eye(2)),'  with a =',np.round(a,6),' a^2 = phi-3:',np.isclose(a*a,phi-3))
print(' Millington\'s Q=[[1,1],[1,0]] obeys Q^2 = 1*Q + 1 (a=1). det Q =',round(np.linalg.det([[1,1],[1,0]])),'; det b =',np.round(np.linalg.det(Bn),6))
f=[0,1]
for n in range(30): f.append(a*f[-1]+f[-2])
cas=[f[n-1]*f[n+1]-f[n]**2 for n in range(1,25)]
print(' complex Fibonacci f_n: Cassini f(n-1)f(n+1)-f(n)^2 = (-1)^n for n=1..24:',np.allclose(cas,[(-1)**n for n in range(1,25)]))
print(' |f_n| for n=0..10:',np.round(np.abs(f[:11]),4),' (bounded/periodic: elliptic, vs Q hyperbolic)')
print(' mirror hand uses R*: a* =',np.round(np.conj(a),6),' -> f_n -> conj(f_n), Cassini sign unchanged')
# ---------- golden chain ----------
L=10
basis=[s for s in itertools.product([0,1],repeat=L) if all(s[i] or s[(i+1)%L] for i in range(L))]  # 0=trivial,1=tau; no two adjacent trivials
idx={s:k for k,s in enumerate(basis)}; D=len(basis)
def Pop(i):
    M=np.zeros((D,D))
    for s in basis:
        a_,b_=s[(i-1)%L],s[(i+1)%L]
        if a_==1 and b_==1:
            for x in (0,1):
                t=list(s); t[i]=x; t=tuple(t)
                if t in idx: M[idx[t],idx[s]]=[[phi**-2,phi**-1.5],[phi**-1.5,phi**-1]][x][s[i]]
        elif a_==0 and b_==0: M[idx[s],idx[s]]=1
    return M
P=[Pop(i) for i in range(L)]; Bi=[R1*p+Rt*(np.eye(D)-p) for p in P]
print('\n=== golden chain, L=%d, Hilbert dim %d (Lucas number L_10 = 123) ==='%(L,D))
print(' P_i projectors:',all(np.allclose(p@p,p) for p in P),' braids unitary:',all(np.allclose(b.conj().T@b,np.eye(D)) for b in Bi),
      ' Yang-Baxter B_i B_i+1 B_i = B_i+1 B_i B_i+1:',all(np.allclose(Bi[i]@Bi[(i+1)%L]@Bi[i],Bi[(i+1)%L]@Bi[i]@Bi[(i+1)%L]) for i in range(L)))
H0=-sum(P); C=sum(1j*(P[i]@P[(i+1)%L]-P[(i+1)%L]@P[i]) for i in range(L))
print(' chiral term C is Hermitian and purely imaginary (odd under i->-i):',np.allclose(C,C.conj().T),np.allclose(C.real,0),' |C|=',round(np.linalg.norm(C),3))
H=lambda lam:H0+lam*C
lam=0.3
# embedding into qubits, for region entropies
emb=np.array([int(''.join(map(str,s)),2) for s in basis])
def S_region(vec_big,nq,A):
    Bq=[k for k in range(nq) if k not in A]
    M=np.transpose(vec_big.reshape([2]*nq),list(A)+Bq).reshape(2**len(A),-1)
    w=np.linalg.svd(M,compute_uv=False)**2; w=w[w>1e-14]; return float(-(w*np.log2(w)).sum())
def tfd(Hl,beta):
    E,V=np.linalg.eigh(Hl); w=np.exp(-beta*(E-E.min())/2); w/=np.linalg.norm(w)
    return sum(w[k]*np.kron(V[:,k],V[:,k].conj()) for k in range(D))     # sum e^{-bE/2}|E>|E*>
def to_big(v2):
    big=np.zeros(2**(2*L),complex); big[(emb[:,None]*2**L+emb[None,:]).ravel()]=v2; return big
print('\n=== TEST 1. Conjugate match: which shadow keeps the double in equilibrium under the Janus clock G = H_aether x 1 - 1 x H_shadow ? ===')
print(' aether chirality lam=+0.3 ; shadow chirality lam\' scanned ; conjugate would be lam\'=-0.3')
ts=np.linspace(0.5,8,16); Areg=list(range(5))+list(range(L,L+5))   # half the aether + matching half of the shadow
for beta in [0.0,1.0]:
    T0=tfd(H(lam),beta); S0=S_region(to_big(T0),2*L,Areg)
    print(' beta=%.1f   (cross-region entropy at t=0: %.4f bits)'%(beta,S0))
    for lp in [-0.6,-0.4,-0.32,-0.3,-0.28,-0.2,0.0,0.3]:
        Ea,Va=np.linalg.eigh(H(lam)); Es,Vs=np.linalg.eigh(H(lp)); co=(Va.conj().T@T0.reshape(D,D)@Vs.conj())  # coeffs in product eigenbasis
        fid=[];dS=[]
        for t in ts:
            Tt=(Va@(np.exp(-1j*(Ea[:,None]-Es[None,:])*t)*co)@Vs.T).reshape(-1); fid.append(1-abs(np.vdot(T0,Tt))**2)
            if t in ts[::5]: dS.append(S_region(to_big(Tt),2*L,Areg)-S0)
        tag=' <- conjugate' if np.isclose(lp,-lam) else (' <- same hand (no conjugation)' if np.isclose(lp,lam) else '')
        print('   lam\'=%+.2f  mean drift 1-|overlap|^2 = %.2e   entropy change of cross region (t=.5,3,5.5) = %s%s'%(lp,np.mean(fid),np.round(dS,4),tag))
np.save('gj_state.npy',np.array([0]))
