import numpy as np
rng=np.random.default_rng(4)
sig=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
H=lambda x: sum(x[a]*sig[a] for a in range(4))      # spacetime point as a Hermitian matrix, det = x0^2 - |x|^2
cay=lambda X: (X-1j*np.eye(2))@np.linalg.inv(X+1j*np.eye(2))
res={'real points unitary (max |WW*-1|)':0,'future tube in ball (max sing. value)':0,'past tube outside (min sing. value)':9}
for _ in range(2000):
    x=rng.normal(size=4)*3; W=cay(H(x))
    res['real points unitary (max |WW*-1|)']=max(res['real points unitary (max |WW*-1|)'],np.abs(W@W.conj().T-np.eye(2)).max())
    y=rng.normal(size=3); y0=np.linalg.norm(y)+abs(rng.normal())+1e-3    # future timelike imaginary part
    Wf=cay(H(x)+1j*H(np.concatenate([[y0],y]))); res['future tube in ball (max sing. value)']=max(res['future tube in ball (max sing. value)'],np.linalg.svd(Wf,compute_uv=False).max())
    Wp=cay(H(x)-1j*H(np.concatenate([[y0],y]))); res['past tube outside (min sing. value)']=min(res['past tube outside (min sing. value)'],np.linalg.svd(Wp,compute_uv=False).min())
# null separation <-> det(W1 - W2) = 0 on the rim
d=[]
for _ in range(500):
    x=rng.normal(size=4); n=rng.normal(size=3); n/=np.linalg.norm(n); k=np.concatenate([[1],n])*rng.uniform(0.5,2)
    d.append(abs(np.linalg.det(cay(H(x))-cay(H(x+k)))))
res['null-separated pairs: max |det(W1-W2)|']=max(d)
x=rng.normal(size=4); res['timelike pair: |det(W1-W2)|']=abs(np.linalg.det(cay(H(x))-cay(H(x+np.array([1,0.2,0,0])))))
for k,v in res.items(): print(k,v)
