import numpy as np, sys
def lap(X):
    P=np.pad(X,((0,0),(1,1),(1,1)),mode='edge')   # Neumann
    return P[:,:-2,1:-1]+P[:,2:,1:-1]+P[:,1:-1,:-2]+P[:,1:-1,2:]-4*X
def rhs(X,K,delta=1.0,rho=2.0,D=1.0,space=True):
    S=X.sum(0); sup=np.zeros_like(X)
    for i in range(X.shape[0]):
        for j,k in K.get(i,[]): sup[i]+=k*X[j]
    r=-delta*X+(1-S)*(rho+sup)*X
    return r+D*lap(X) if space else r
def setupK(n=6,with_par=False):
    K={i:[((i-1)%n,500.0)] for i in range(n)}
    if with_par: K[n]=[(n-1,530.0)]
    return K
mode=sys.argv[1]; seed=int(sys.argv[2]) if len(sys.argv)>2 else 0
rng=np.random.default_rng(seed); N=147; n=6; dt=0.1
if mode=='well':
    X=np.array([0.1]*n+[0.0])[:,None,None]*np.ones((7,1,1)); X[6]=0.01
    K=setupK(with_par=True)
    for t in range(200000):
        X=np.clip(X+dt*0.1*rhs(X,K,space=False),0,1)
    print('S2 well-mixed: members',np.round(X[:6,0,0],4).tolist(),'parasite',round(float(X[6,0,0]),4))
else:
    X=np.zeros((7,N,N)); X[:6,60:87,60:87]=rng.random((6,27,27))*0.1   # random seed patch
    K=setupK()
    T1=int(1500/dt)
    for t in range(T1): X=np.clip(X+dt*rhs(X,K),0,1)
    m=X[:6].mean((1,2)); print('S1 after t=1500: member means',np.round(m,4).tolist(),'| spatial var X1 %.4g'%X[0].var(),flush=True)
    X[6]=0; X[6][:,0:5]=0.01
    K=setupK(with_par=True)
    for t in range(int(1500/dt)): X=np.clip(X+dt*rhs(X,K),0,1)
    m=X[:6].mean((1,2)); print('S3-edge seed %d after parasite t=1500 more: member means %s | parasite max %.3g mean %.3g'%(seed,np.round(m,4).tolist(),X[6].max(),X[6].mean()))
    np.save('bh_edge_final_%d.npy'%seed,X)
