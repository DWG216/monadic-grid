import numpy as np, itertools, time, sys
exec(open('frozen_fluid.py').read().split('res={}')[0])   # qn, rep, key, order
phi=(1+5**.5)/2
I2=np.eye(2); X=np.array([[0,1],[1,0]]); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1.,-1])
def q2u(q): return q[0]*I2-1j*(q[1]*X+q[2]*Y+q[3]*Z)
def pkey(U):  # projective key
    f=U.reshape(-1); j=np.argmax(abs(f)>1e-6); U=U*abs(f[j])/f[j]; return tuple(np.round(U.reshape(-1),7))
# ---------- standard 2I and tau60 ----------
icos=[]
for s in (1,-1):
    for k in range(4): e=np.zeros(4); e[k]=s; icos.append(e)
icos+=[np.array(s)/2 for s in itertools.product([1,-1],repeat=4)]
base=[0,1,1/phi,phi]; evens=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[i]<p[j])%2==0]
for p in evens:
    for sg in itertools.product([1,-1],repeat=3):
        q=np.zeros(4); vals=[0]+[sg[i]*base[i+1] for i in range(3)]
        for i in range(4): q[p[i]]=vals[i]
        icos.append(q/2)
icos=np.unique(np.round(icos,12),axis=0); G=[q2u(q) for q in icos]; assert len(G)==120
N=7+5*phi; tau=q2u(np.array([0,1,1,2+phi])/np.sqrt(N))
# ---------- braid sector ----------
g4,D=rep(8,4); paths=[]
def rec(p):
    if len(p)==5: paths.append(tuple(p)); return
    for s in (p[-1]-1,p[-1]+1):
        if 0<=s<=8: rec(p+[s])
rec([0]); sec=[paths.index(p) for p in [(0,1,0,1,2),(0,1,2,1,2),(0,1,2,3,2)]]
S=[g[np.ix_(sec,sec)] for g in g4]
print('B1. sector unitarity %.1e'%max(np.linalg.norm(s@s.conj().T-np.eye(3)) for s in S))
print('    s1,s2 leakage couplings: %.1e %.1e | s3 coupling |1>-leak: %.3f'%(abs(S[0][:2,2]).max(),abs(S[1][:2,2]).max(),abs(S[2][1,2])))
# frame group (3x3, mod global phase)
fr={pkey(np.eye(3)):np.eye(3,dtype=complex)}; front=[np.eye(3,dtype=complex)]
while front:
    nw=[]
    for U in front:
        for g in (S[0],S[1],np.linalg.inv(S[0]),np.linalg.inv(S[1])):
            V=g@U; k=pkey(V)
            if k not in fr: fr[k]=V; nw.append(V)
    front=nw
F=list(fr.values()); qb={pkey(f[:2,:2]) for f in F}
print('    frame <s1,s2>: %d elements (mod global phase); qubit blocks projectively: %d'%(len(F),len(qb)))
# powers of s3 (mod global phase)
P3=[]; U=np.eye(3,dtype=complex)
while True:
    U=S[2]@U; k=pkey(U)
    if k==pkey(np.eye(3)): break
    P3.append(U.copy())
print('    s3 order (projective) %d -> %d nontrivial powers'%(len(P3)+1,len(P3)))
# ---------- frame map W: braid qubit frame -> standard 2I ----------
def su(M): return M/np.sqrt(np.linalg.det(M))
b1,b2=su(S[0][:2,:2]),su(S[1][:2,:2]); W=None
t1,t2,t12=[abs(np.trace(m)) for m in (b1,b2,b1@b2)]
for g in G:
    if abs(abs(np.trace(g))-t1)>1e-8: continue
    for h in G:
        if abs(abs(np.trace(h))-t2)>1e-8 or abs(abs(np.trace(g@h))-t12)>1e-8: continue
        for s1_,s2_ in itertools.product((1,-1),repeat=2):
            # solve W b1 = s1 g W, W b2 = s2 h W
            Mx=np.vstack([np.kron(np.eye(2),b1.T)-np.kron(s1_*g,np.eye(2)),np.kron(np.eye(2),b2.T)-np.kron(s2_*h,np.eye(2))])
            u,sv,vh=np.linalg.svd(Mx)
            if sv[-1]<1e-9:
                Wc=vh[-1].conj().reshape(2,2); Wc=Wc/np.sqrt(abs(np.linalg.det(Wc))); W=Wc; break
        if W is not None: break
    if W is not None: break
print('    frame map found: unitarity err %.1e'%np.linalg.norm(W@W.conj().T-I2))
Fq=[su(f[:2,:2]) for f in F]
chk=max(min(min(np.linalg.norm(W@f@W.conj().T-g),np.linalg.norm(W@f@W.conj().T+g)) for g in G) for f in Fq[:60])
print('    every frame qubit block maps into standard 2I: max err %.1e'%chk)
Gb=[W.conj().T@g@W for g in G]                       # 2I in braid frame
def dcoset(C):
    out={}
    for g in Gb:
        for h in Gb:
            M=g@C@h; out.setdefault(pkey(M),M)
    return np.array(list(out.values()))
tau_b=W.conj().T@tau@W
# ---------- B2 numeric support ----------
ks=[k for k in range(1,20) if np.gcd(k,20)==1]
norms=[np.prod([np.sin(m*k*np.pi/10)/np.sin(k*np.pi/10) for k in ks]) for m in range(1,10)]
print('B2. norms of q-integers [1..9] at q=e^(i pi/10):',[round(x,6) for x in norms])
k_std=q2u(np.array([0,0,0,1.])); print('    |tr(tau60 * k)|^2 = %.6f ; 4(2+phi)^2/(7+5phi) = %.6f ; norm of 7+5phi = %.3f'%(abs(np.trace(tau@k_std))**2,4*(2+phi)**2/N,N*(7+5*(1-phi))))
np.save('t60b_setup.npy',dict(S=S,F=np.array(F),P3=np.array(P3),W=W,tau_b=tau_b),allow_pickle=True)
# ---------- search ----------
def search(C, mmax=2, label=''):
    DC=dcoset(C); Cc=DC.reshape(len(DC),4).conj().T     # (4, nDC)
    res={}
    # m=0 : W = identity
    res[0]=np.sqrt(max(0,3-np.abs(np.eye(2).reshape(1,4)@Cc).max()-1))
    def best(Ws):
        b=9; arg=None
        for i in range(0,len(Ws),20000):
            ch=Ws[i:i+20000]; V=ch[:,:2,:2].reshape(len(ch),4); tr=np.abs(V@Cc).max(1)+np.abs(ch[:,2,2])
            j=np.argmax(tr);
            if 3-tr[j]<b: b=3-tr[j]; arg=i+j
        return np.sqrt(max(b,0)),arg
    W1=np.array(P3); res[1]=best(W1)[0]
    if mmax>=2:
        Fa=np.array(F); mid=np.einsum('aij,bjk->abik',W1,Fa).reshape(-1,3,3)   # s3^k g
        W2=np.einsum('aij,bjk->abik',mid,W1).reshape(-1,3,3); res[2]=best(W2)[0]
    print('   %-14s best error by s3-syllables: '%label+'  '.join('m=%d: %.4f'%(m,e) for m,e in res.items()),flush=True)
    return res,DC
t=time.time()
print('B3/C. exhaustive search m<=2 (frame braids free):')
r_tau,DC_tau=search(tau_b,2,'tau60'); print('      double coset size %d (projective); %.0fs'%(len(DC_tau),time.time()-t))
r_c1,_=search(Gb[17],1,'C1 2I element')
rng=np.random.default_rng(7); rand=[]
for i in range(3):
    q=rng.normal(size=4); q/=np.linalg.norm(q); rand.append(search(W.conj().T@q2u(q)@W,2,'C2 random %d'%(i+1))[0])
np.save('t60b_m2.npy',dict(tau=r_tau,rand=rand),allow_pickle=True)
