import numpy as np, io, contextlib
from scipy.linalg import expm
src=open('golden_janus.py').read().split("print('\\n=== TEST 1")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
print('=== TEST 3. Tank ===')
sy=np.array([[0,-1j],[1j,0]]); q0=np.array([1,0],complex); w=1.0
for t in [0,0.4,0.8,1.2]:
    qp=expm(-1j*w*sy*t)@q0; qm=expm(-1j*w*sy.conj()*t)@q0      # hand -: same start, conjugate Hamiltonian
    print('  qubit t=%.1f: E=%.3f B=%.3f | E^2+B^2 (<+|+>) = %.4f | cross <-|+> = %.4f | cos 2wt = %.4f'%(t,qp[0].real,qp[1].real,np.vdot(qp,qp).real,np.vdot(qm,qp).real,np.cos(2*w*t)))
E0,V0=np.linalg.eigh(H0)
Refl=np.zeros((D,D))
for s in basis: Refl[idx[tuple(s[::-1])],idx[s]]=1
print('  chain: reflection R flips the chiral term (R C R = -C):',np.allclose(Refl@C@Refl,-C))
rng=np.random.default_rng(0)
for name,psi0 in [('reflection-symmetric start (ground state)',V0[:,0]),('asymmetric real start',V0[:,0]+0.6*V0[:,3]+0.5*np.linalg.qr(rng.normal(size=(D,1)))[0][:,0])]:
    psi0=psi0/np.linalg.norm(psi0); psi0=psi0.astype(complex)
    print('  %s, mirror-symmetric? %s'%(name,np.allclose(Refl@psi0,psi0) or np.allclose(Refl@psi0,-psi0)))
    for lam in [0.0,0.1,0.3]:
        Ev,Vv=np.linalg.eigh(H(lam)); c=Vv.conj().T@psi0
        Ew,Vw=np.linalg.eigh(H(-lam)); cw=Vw.conj().T@psi0
        ts=np.linspace(0,80,4000); Cx=[];Ob=[]
        for t in ts:
            vp=Vv@(np.exp(-1j*Ev*t)*c); vm=Vw@(np.exp(-1j*Ew*t)*cw)
            Cx.append(np.vdot(vm,vp)); Ob.append(np.vdot(vp,P[0]@vp).real+np.vdot(vm,P[0]@vm).real)
        Cx=np.array(Cx); fr=np.fft.rfftfreq(len(ts),ts[1]-ts[0])*2*np.pi
        s_cross=np.abs(np.fft.rfft(np.abs(Cx)**2-np.mean(np.abs(Cx)**2))); s_obs=np.abs(np.fft.rfft(np.array(Ob)-np.mean(Ob)))
        print('    lam=%.1f  hand fidelity |<-|+>|^2: min %.4f mean %.4f | peak freq: cross-hand %.3f , single-hand observable %.3f'%(
            lam,(np.abs(Cx)**2).min(),(np.abs(Cx)**2).mean(),fr[np.argmax(s_cross)] if s_cross.max()>1e-8 else 0,fr[np.argmax(s_obs)]))
    if 'asym' in name:
        lamS=[0.02,0.04,0.08]; t=3.0; v=[]
        for lam in lamS:
            Ev,Vv=np.linalg.eigh(H(lam)); Ew,Vw=np.linalg.eigh(H(-lam))
            vp=Vv@(np.exp(-1j*Ev*t)*(Vv.conj().T@psi0)); vm=Vw@(np.exp(-1j*Ew*t)*(Vw.conj().T@psi0)); v.append(1-abs(np.vdot(vm,vp))**2)
        print('    small-lam scaling of 1-fidelity at t=3: ',np.round(v,6),' ratios',np.round(np.array(v[1:])/np.array(v[:-1]),3),' (4 = quadratic)')
