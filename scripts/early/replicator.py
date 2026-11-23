import numpy as np, random
comp=str.maketrans('ACGU','UGCA')
rc=lambda s: s.translate(comp)[::-1]
random.seed(1); s=''.join(random.choice('ACGU') for _ in range(45))
print('reverse-complement is an involution:', rc(rc(s))==s, '| complement alone is too:', s.translate(comp).translate(comp)==s)
duplex=lambda a: frozenset([a,rc(a)])
print('duplex invariant under strand swap (half-turn):', duplex(s)==duplex(rc(s)))
# spinor parallel: SU(2) conjugation implemented by a 180-degree rotation (i sigma_y)
sy=np.array([[0,-1j],[1j,0]]); eps=1j*sy
U=np.linalg.qr(np.random.default_rng(0).normal(size=(2,2))+1j*np.random.default_rng(1).normal(size=(2,2)))[0]; U=U/np.sqrt(np.linalg.det(U))
print('SU(2): eps U* eps^-1 = U ->', np.allclose(eps@U.conj()@np.linalg.inv(eps),U), '| eps antisymmetric (pairs two spinors into a singlet):', np.allclose(eps,-eps.T))
A=np.array([[2,1j],[0,0.5]]); A=A/np.sqrt(np.linalg.det(A))
print('SL(2,C) boost-type element: eps A* eps^-1 = A ->', np.allclose(eps@A.conj()@np.linalg.inv(eps),A), '(conjugate hand is a different representation)')
# Eigen error threshold: mu_g = L*eps must stay below ~ln(sigma)
rows=[('CChMVd viroid (Gago 2009)',399,0.0025),('phiX174 ssDNA phage (Cuevas 2009)',5386,1.0e-6),('RNA virus, typical high (1e-4/nt, 10 kb)',1e4,1e-4),('RNA virus, typical low (1e-6/nt, 10 kb)',1e4,1e-6),('E. coli via Drake rule (0.003/genome)',4.6e6,0.003/4.6e6)]
for n,L,e in rows: print('  %-42s L=%-8.0f eps=%.2g  mu_g=L*eps=%.3g'%(n,L,e,L*e))
for sig in [2,10,100]: print('ln sigma for sigma=%d: %.2f'%(sig,np.log(sig)))
print('QT45 (45 nt): to copy itself below threshold needs per-nt error < %.3f (sigma=2) ... %.3f (sigma=10)'%(np.log(2)/45,np.log(10)/45))
