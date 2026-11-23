import numpy as np, math, sys
b=3.0; f=lambda p: np.log1p((math.e**b-1)*p)/b; finv=lambda x: (np.exp(b*x)-1)/(math.e**b-1)
LR=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
def run(eps,gated,seed=20261122,N=50,T=600,dt=0.002):
    rng=np.random.default_rng(seed); w=1+0.03*rng.standard_normal(N); ph=rng.random(N); L=0.0; kp=rng.random()
    cnt=np.zeros(N,int); lcnt=0; kicked=False
    for step in range(int(T/dt)):
        t=step*dt; ph+=w*dt; newL=L+LR*dt; kick=False
        if gated and newL>=1: kick=True
        if (not gated) and (not kicked) and L<kp<=newL: kick=True; kicked=True
        if newL>=1:
            newL-=1
            if t>=T-200: lcnt+=1
            if not gated: kp=rng.random(); kicked=False
        L=newL
        if kick:
            x=np.minimum(f(np.clip(ph,0,1))+eps,1); ph=finv(x)
        fire=ph>=1
        if fire.any():
            ph[fire]=0
            if t>=T-200: cnt[fire]+=1
    return (cnt==lcnt).mean()
for gated in (True,False):
    print(f"leader rate {LR} {'GATED  ' if gated else 'UNGATED'}:", " ".join(f"eps={e}: {run(e,gated):.2f}" for e in (0.005,0.01,0.02,0.04,0.08)))
