import numpy as np
exec(open('t19_action_vs_loss.py').read().split('res={}')[0])
for T,eu in [(1,False),(4,False),(4,True)]:
    H,b=hess(T,eu); ev,V=np.linalg.eigh(H); xs=np.linalg.solve(H,b); lr=1/ev.max()
    # exact GD error after k steps in eigenbasis: e_k = (1-lr*ev)^k e_0, e_0=-xs
    e0=V.T@(-xs)
    for k in [2e5,1e7,1e9]:
        ek=(1-lr*ev)**k*e0
        print(f"T={T} euclid={eu} steps={k:.0e} |err|={np.linalg.norm(ek):.3e}  lowest eig={ev[0]:.4e} cond={ev[-1]/abs(ev[0]):.2e}")
