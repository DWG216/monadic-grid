# Janus network: same {5,4} patch, every centre-neighbour link is a thermofield-double "gate"
# J = diag(cos th, sin th * e^{i phi}); phi = the TFD's time phase. Hand +: phi, hand -: -phi (i -> -i).
import numpy as np, itertools
exec(open('holenmer.py').read().split('# --- B2')[0])
T=T/np.linalg.norm(T)
print('Step 1. perfect tensor is real (its own mirror image):',np.allclose(T.imag if np.iscomplexobj(T) else 0,0))
def build(phis,th=0.6):
    psi=T[0]
    for k in range(5):
        J=np.diag([np.cos(th),np.sin(th)*np.exp(1j*phis[k])])*np.sqrt(2)
        psi=np.tensordot(psi,np.tensordot(J,T[0],axes=([1],[0])),axes=([0],[0]))
    psi=psi.reshape(-1); return psi/np.linalg.norm(psi)
n=20
def rho(psi,A):
    B=[k for k in range(n) if k not in A]
    M=np.transpose(psi.reshape([2]*n),list(A)+B).reshape(2**len(A),-1); return M@M.conj().T
def logm_h(r):
    w,v=np.linalg.eigh(r); w=np.clip(w,1e-300,None); return (v*np.log2(w))@v.conj().T, w
def S(r): w=np.linalg.eigvalsh(r); w=w[w>1e-13]; return float(-(w*np.log2(w)).sum())
def relent(r1,r2,tol=1e-10):
    w1,v1=np.linalg.eigh(r1); w2,v2=np.linalg.eigh(r2)
    P2=v2[:,w2>tol]@v2[:,w2>tol].conj().T; V1=v1[:,w1>tol]
    if np.linalg.norm(V1-P2@V1)>1e-6: return np.inf      # hand + has weight where hand - has none
    l1=(v1[:,w1>tol]*np.log2(w1[w1>tol]))@v1[:,w1>tol].conj().T
    l2=(v2[:,w2>tol]*np.log2(w2[w2>tol]))@v2[:,w2>tol].conj().T
    return float(np.real(np.trace(r1@(l1-l2))))
regions={'one tile (4)':list(range(4)),'arc 6':list(range(6)),'arc 8 (2 tiles)':list(range(8)),'two separated tiles':list(range(4))+list(range(8,12)),'scattered 8':list(range(0,16,2))}
rng=np.random.default_rng(3); phis=rng.uniform(0.3,1.2,5)
P=build(phis); M=build(-phis)
print('   hand - is exactly the complex conjugate (time-reversed) of hand +:',np.allclose(M,P.conj()))
print('\nStep 2. first order: entropies (and full spectra) of every region, hand + vs hand -')
same=True
for L in range(1,11):
    for s0 in range(0,20,3):
        A=[(s0+j)%20 for j in range(L)]
        same&=np.allclose(np.sort(np.linalg.eigvalsh(rho(P,A))),np.sort(np.linalg.eigvalsh(rho(M,A))),atol=1e-10)
print('   all 70 arcs: identical entanglement spectra ->',same,' (entropy is blind to the hand)')
print('   entropy is EVEN in phi (S(phi)-S(-phi)):',[round(S(rho(build(phis),A))-S(rho(build(-phis),A)),12) for A in regions.values()])
print('   entropy change from phi (vs real links):', {k:round(S(rho(P,A))-S(rho(build(0*phis),A)),6) for k,A in regions.items()})
print('\nStep 3a. second order: relative entropy S(hand+ || hand-) per region = energy gap measured on the other hand\'s modular clock')
for k,A in regions.items():
    print('   %-20s'%k, round(relent(rho(P,A),rho(M,A)),4), ' rank',np.linalg.matrix_rank(rho(P,A),1e-10),'of',2**len(A))
print('   scaling with the Janus phase (all links phi, region arc 8):')
for ph in [0,0.05,0.1,0.2,0.4]:
    p=build([ph]*5); m=build([-ph]*5); d=relent(rho(p,regions['arc 8 (2 tiles)']),rho(m,regions['arc 8 (2 tiles)']))
    print('     phi=%.2f  D=%.6f  D/phi^2=%s'%(ph,d,'-' if ph==0 else round(d/ph**2,4)))
print('   hands coupled vs not: maximal links (th=pi/4) vs thermal links (th=0.6), arc 8:')
for th in [np.pi/4,0.6,0.3]:
    p=build(phis,th); m=build(-phis,th); print('     th=%.2f  D=%.4f'%(th,relent(rho(p,regions['arc 8 (2 tiles)']),rho(m,regions['arc 8 (2 tiles)']))))
print('\nStep 3b. modular flow: run hand + along hand -\'s own clock K- for modular time s; how far does it move?')
A=regions['arc 8 (2 tiles)']; rp=rho(P,A); rm=rho(M,A)
def flow(r,s):
    w,v=np.linalg.eigh(r); return (v*np.exp(1j*s*np.log(np.clip(w,1e-300,None))))@v.conj().T
def moved(r,U):
    r2=U@r@U.conj().T; return 1-np.real(np.trace(r@r2))/np.real(np.trace(r@r))
for s_ in [0,0.25,0.5,1,2,-1]:
    print('     s=%5.2f  on the other hand\'s clock: 1-overlap=%.5f   on its own clock: %.1e'%(s_,moved(rp,flow(rm,s_)),abs(moved(rp,flow(rp,s_)))))
p0=build(0*phis); r0=rho(p0,A)
print('     real network (phi=0), other-hand clock at s=1: %.1e'%abs(moved(r0,flow(rho(build(-0*phis),A),1))))
