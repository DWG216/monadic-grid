# Step 3: Schwinger-Keldysh doubling of the golden chain (forward strand x reverse strand)
import numpy as np
src=open('step2.py').read().split("lucas=")[0]; ns={}; exec(src,ns)
M,B=ns['H'](10); n=M.shape[0]; E=np.linalg.eigvalsh(M)
# doubled generator on density matrices, Lv = H(x)1 - 1(x)H^T ; its eigenvalues are exactly E_i - E_j
w=(E[:,None]-E[None,:]).ravel()
print('single chain dim',n,'-> doubled dim',n*n)
print('trace of doubled generator (net zero): Tr(H)*n - n*Tr(H) =',round(np.trace(M)*n-n*np.trace(M),12))
print('doubled spectrum symmetric under swapping strands (w -> -w):',np.allclose(np.sort(w),np.sort(-w)))
print('zero modes (stationary states):',int(np.sum(abs(w)<1e-9)),' >= number of eigenstates',n)
# small explicit check that kron form matches E_i-E_j, on a small chain
Ms,_=ns['H'](6); m=Ms.shape[0]; Lv=np.kron(Ms,np.eye(m))-np.kron(np.eye(m),Ms.T)
Es=np.linalg.eigvalsh(Ms); print('explicit doubled generator matches E_i-E_j (L=6):',np.allclose(np.sort(np.linalg.eigvalsh(Lv)),np.sort((Es[:,None]-Es[None,:]).ravel())))
for t in [0,2,5,10,20]:
    Z=np.sum(np.exp(-1j*E*t)); P=Z*np.conj(Z)
    print(f't={t:4}  forward Z = {Z.real:+8.3f} {Z.imag:+8.3f}i   forward x reverse = {P.real:9.3f}  imaginary part = {abs(P.imag):.1e}')
