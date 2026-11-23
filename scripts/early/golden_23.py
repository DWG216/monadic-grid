import numpy as np, io, contextlib
src=open('golden_janus.py').read().split("print('\\n=== TEST 1")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
def rhoA(v,A):
    big=np.zeros(2**L,complex); big[emb]=v; Bq=[k for k in range(L) if k not in A]
    M=np.transpose(big.reshape([2]*L),list(A)+Bq).reshape(2**len(A),-1); return M@M.conj().T
tdist=lambda r1,r2: 0.5*np.abs(np.linalg.eigvalsh(r1-r2)).sum()
E0,V0=np.linalg.eigh(H0); psi0=V0[:,0].real.astype(complex)        # real starting state (golden-chain ground state)
print('=== TEST 2. Cassini: does the braid clock alternate the hands step by step? ===')
cb=np.exp(3j*np.pi/5)
Ue=np.eye(D,dtype=complex); Uo=np.eye(D,dtype=complex)
for i in range(0,L,2): Ue=Ue@(cb*Bi[i])
for i in range(1,L,2): Uo=Uo@(cb*Bi[i])
Up=Uo@Ue; Um=Up.conj()                                               # hand + uses R, hand - uses R*
A=list(range(5)); vp=psi0.copy(); vm=psi0.copy(); out=[]
for n in range(0,21):
    out.append(tdist(rhoA(vp,A),rhoA(vm,A))); vp=Up@vp; vm=Um@vm
print(' hand separation D(n) (trace distance, half chain) n=0..20:'); print(' ',np.round(out,4))
d=np.array(out[1:]); print(' even-n mean %.4f  odd-n mean %.4f'%(d[1::2].mean(),d[0::2].mean()))
# single-site braid Floquet (one braid repeated) -> exact complex Fibonacci
b=cb*Bi[4]; v=psi0.copy(); amps=[np.vdot(psi0,np.linalg.matrix_power(b,n)@psi0) for n in range(0,12)]
cas=[amps[n-1]*amps[n+1]-amps[n]**2 for n in range(1,11)]
print(' one braid repeated: return amplitudes obey the complex Fibonacci recurrence g(n+1)=a g(n)+g(n-1):',
      np.allclose([amps[n+1]-(a*amps[n]+amps[n-1]) for n in range(1,10)],0))
print(' Cassini of return amplitudes g(n-1)g(n+1)-g(n)^2, n=1..10:',np.round(cas,4))
# full circuit: eigenphases of U+ vs U-
ph=np.sort(np.angle(np.linalg.eigvals(Up))); phm=np.sort(np.angle(np.linalg.eigvals(Um)))
print(' circuit spectrum: U- eigenphases are minus U+ eigenphases:',np.allclose(np.sort(-ph),phm,atol=1e-8),'; det U+ =',np.round(np.linalg.det(Up),4))
print('\n=== TEST 3. Tank: does the cross-hand term oscillate at twice the frequency? ===')
w=1.0; sy=np.array([[0,-1j],[1j,0]]); q0=np.array([1,0],complex)
for t in [0,0.4,0.8,1.2]:
    qp=__import__('scipy.linalg',fromlist=['expm']).expm(-1j*w*sy*t)@q0; qm=qp.conj()
    print('  qubit, chiral H=w*sigma_y, t=%.1f: <+|+> = %.4f   cross <-|+> = %.4f   cos(2wt) = %.4f'%(t,np.vdot(qp,qp).real,np.vdot(qm,qp).real,np.cos(2*w*t)))
from scipy.linalg import expm
for lam in [0.0,0.1,0.3]:
    Hl=H(lam); Ev,Vv=np.linalg.eigh(Hl); c=Vv.conj().T@psi0
    ts=np.linspace(0,60,3000); Cx=[]; Au=[]
    for t in ts:
        vp=Vv@(np.exp(-1j*Ev*t)*c); vm=vp.conj().copy()  # careful: hand - evolves with H* from same real start
        vm=(Vv.conj())@(np.exp(1j*Ev*t)*c.conj())        # = conj(vp) only if... compute exactly: e^{-iH* t}psi0
        vm=np.conj(Vv@(np.exp(1j*Ev*t)*c))
        Cx.append(np.vdot(vm,vp)); Au.append(abs(np.vdot(psi0,vp))**2)
    Cx=np.array(Cx); fr=np.fft.rfftfreq(len(ts),ts[1]-ts[0])*2*np.pi
    s1=np.abs(np.fft.rfft(np.array(Au)-np.mean(Au))); s2=np.abs(np.fft.rfft(Cx.real-Cx.real.mean()))
    print('  chain lam=%.1f: cross-hand overlap Re<-|+> ranges %.4f..%.4f ; 1-|<-|+>|^2 mean %.4f ; dominant freq single-hand return %.3f, cross-hand %.3f'%(
        lam,Cx.real.min(),Cx.real.max(),np.mean(1-np.abs(Cx)**2),fr[np.argmax(s1)] if s1.max()>1e-9 else 0,fr[np.argmax(s2)] if s2.max()>1e-9 else 0))
# beat structure: frequencies in cross term are E_j-E_l ; in a single-hand observable also E_j-E_l
