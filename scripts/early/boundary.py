import numpy as np, itertools
from scipy.linalg import expm
rng=np.random.default_rng(11)
I=np.eye(2);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1]).astype(complex)
def ket(n):
    th=np.arccos(np.clip(n[2],-1,1));ph=np.arctan2(n[1],n[0]);return np.array([np.cos(th/2),np.exp(1j*ph)*np.sin(th/2)])
# ---------------- STEP 1 ----------------
ens={'Z':[(0.5,np.array([1,0],complex)),(0.5,np.array([0,1],complex))],
     'X':[(0.5,np.array([1,1],complex)/2**.5),(0.5,np.array([1,-1],complex)/2**.5)]}
def rot(axis,ang): a=np.array(axis)/np.linalg.norm(axis); return expm(-1j*ang/2*(a[0]*X+a[1]*Y+a[2]*Z))
def run(variant,kappa,par,rounds=8):
    """returns {record string: prob} and averaged final state, for each Alice choice"""
    s,axis,fb,H0=par
    M0=np.sqrt(np.diag([0.5+s/2,0.5-s/2])); M1=np.sqrt(np.eye(2)-M0@M0)
    R=rot(axis,np.pi/2); M=[R@M0@R.conj().T, R@M1@R.conj().T]      # weak measurement along a tilted axis
    out={}
    for ch,E in ens.items():
        dist={}; rho=np.zeros((2,2),complex)
        def rec(psi,p,string,r):
            nonlocal rho
            if p<1e-15: return
            if r==rounds:
                dist[string]=dist.get(string,0)+p; rho=rho+p*np.outer(psi,psi.conj()); return
            # evolution step
            if variant=='B':
                for _ in range(10):
                    h=kappa*np.real(np.vdot(psi,Z@psi))*X+H0; psi=expm(-1j*0.05*h)@psi; psi/=np.linalg.norm(psi)
            else: psi=expm(-1j*0.5*H0)@psi
            probs=[np.real(np.vdot(Mk@psi,Mk@psi)) for Mk in M]
            if variant=='C':
                tilt=kappa*np.real(np.vdot(psi,X@psi)); probs=[probs[0]*(1+tilt),probs[1]*(1-tilt)]; probs=[q/sum(probs) for q in probs]
            for k in (0,1):
                phi=M[k]@psi; nrm=np.linalg.norm(phi)
                if nrm<1e-15: continue
                phi=phi/nrm; phi=rot(axis if k==0 else [axis[1],-axis[0],axis[2]],fb*(1 if k else -1))@phi   # feedback from own record
                rec(phi,p*probs[k],string+str(k),r+1)
        for w,psi in E: rec(psi,w,'',0)
        out[ch]=(dist,rho)
    keys=set(out['Z'][0])|set(out['X'][0])
    tv=0.5*sum(abs(out['Z'][0].get(k,0)-out['X'][0].get(k,0)) for k in keys)
    td=0.5*np.abs(np.linalg.eigvalsh(out['Z'][1]-out['X'][1])).sum()
    return tv,td
print('STEP 1: can Alice signal to Bob through Bob\'s feedback loop?')
pars=[(rng.uniform(0.2,0.9),rng.normal(size=3),rng.uniform(0,np.pi),0.6*(rng.normal()*X+rng.normal()*Y+rng.normal()*Z)) for _ in range(20)]
A=max(max(run('A',0,p)) for p in pars)
print('  A  linear + record-driven feedback (20 random loops): max signalling %.1e'%A)
for k in [0,0.5,1]:
    b=max(run('B',k,p) for p in pars[:5]); c=max(run('C',k,p) for p in pars[:5])
    print('  kappa=%.1f | B state-driven nonlinear evolution: TV %.3e, trace %.3e | C state-tilted Born rule: TV %.3e, trace %.3e'%(k,b[0],b[1],c[0],c[1]))
# ---------------- STEP 2 ----------------
print('\nSTEP 2a: decoherence rate Lambda*dx^2 (Joos-Zeh constants, cm^-2 s^-1), dx = object size')
L={'cosmic background':[1e6,1e-6,1e-12],'300 K photons':[1e19,1e12,1e6],'sunlight':[1e21,1e17,1e13],'air molecules':[1e36,1e32,1e30],'lab vacuum':[1e23,1e19,1e17]}
sizes=[1e-3,1e-5,1e-6]; names=['dust grain 10 um','particle 100 nm','large molecule 10 nm']
for j,(a,n) in enumerate(zip(sizes,names)):
    r={k:v[j]*a**2 for k,v in L.items()}
    light=max(r['sunlight'],r['300 K photons'],r['cosmic background'])
    print('  %-22s air %.0e /s | lab vacuum %.0e /s | sunlight %.0e /s | 300K %.0e | CMB %.0e  -> air/light = %.0e, vacuum/light = %.0e'%(n,r['air molecules'],r['lab vacuum'],r['sunlight'],r['300 K photons'],r['cosmic background'],r['air molecules']/light,r['lab vacuum']/light))
print('\nSTEP 2b: quantum Darwinism toy (system + 12 environment qubits)')
NE=12
def haar2():
    q,r=np.linalg.qr(rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))); return q*(np.diag(r)/abs(np.diag(r)))
def apply2(psi,U,i,j,n):
    psi=psi.reshape([2]*n); psi=np.moveaxis(psi,[i,j],[0,1]); s=psi.shape; psi=(U@psi.reshape(4,-1)).reshape(s); return np.moveaxis(psi,[0,1],[i,j]).reshape(-1)
def entropy(rho):
    w=np.linalg.eigvalsh(rho); w=w[w>1e-14]; return float(-(w*np.log2(w)).sum())
def red(psi,qubits,n):
    keep=sorted(qubits); t=psi.reshape([2]*n); rest=[q for q in range(n) if q not in keep]
    return np.moveaxis(t,keep+rest,list(range(n))).reshape(2**len(keep),-1)
def Sof(psi,qubits,n):
    m=red(psi,qubits,n); sv=np.linalg.svd(m,compute_uv=False); w=sv**2; w=w[w>1e-14]; return float(-(w*np.log2(w)).sum())
def MI(psi,F,n): return Sof(psi,[0],n)+Sof(psi,F,n)-Sof(psi,[0]+F,n)
def profile(psi,n):
    Hs=Sof(psi,[0],n); prof=[]
    for f in range(1,NE+1):
        Fs=[list(c) for c in itertools.combinations(range(1,n),f)]
        Fs=[Fs[i] for i in rng.choice(len(Fs),min(12,len(Fs)),replace=False)]
        prof.append(np.mean([MI(psi,F,n) for F in Fs]))
    return Hs,prof
def redundancy(Hs,prof,delta=0.1):
    for f,m in enumerate(prof,1):
        if m>=(1-delta)*Hs: return NE/f
    return 0.0
n=NE+1; theta=0.85*np.pi      # partial record per environment qubit (imperfect copies)
psi=np.zeros(2**n,complex); psi[0]=1
psi=apply2(psi,np.kron(I,I),0,1,n)
sys=np.array([1,1])/2**.5; psi=np.kron(sys,np.eye(2**NE)[0]).astype(complex)
CR=np.zeros((4,4),complex); CR[:2,:2]=I; CR[2:,2:]=expm(-1j*theta/2*Y)   # controlled partial copy
for e in range(1,n): psi=apply2(psi,CR,0,e,n)
Hs,p_photon=profile(psi,n); R_ph=redundancy(Hs,p_photon)
Itot=MI(psi,list(range(1,n)),n)
gas=psi.copy()
for layer in range(6):
    perm=rng.permutation(range(1,n))
    for a,b in zip(perm[::2],perm[1::2]): gas=apply2(gas,haar2(),a,b,n)
Hs2,p_gas=profile(gas,n); R_gas=redundancy(Hs2,p_gas); Itot2=MI(gas,list(range(1,n)),n)
print('  H(S) = %.3f bits; total I(S:E) photon-like %.3f, gas-like %.3f (control: unchanged by scrambling)'%(Hs,Itot,Itot2))
print('  photon-like: I(S:F) by fragment size',np.round(p_photon,3).tolist(),' -> R_0.1 = %.1f'%R_ph)
print('  gas-like   : I(S:F) by fragment size',np.round(p_gas,3).tolist(),' -> R_0.1 = %.1f'%R_gas)
np.save('boundary_profiles.npy',np.array([p_photon,p_gas]))
