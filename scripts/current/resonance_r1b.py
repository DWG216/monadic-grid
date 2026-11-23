import numpy as np, json
def rot(W,K,n=20000,burn=2000):
    th=np.zeros_like(W)
    for _ in range(burn): th=th+W-K/(2*np.pi)*np.sin(2*np.pi*th)
    t0=th.copy()
    for _ in range(n): th=th+W-K/(2*np.pi)*np.sin(2*np.pi*th)
    return (th-t0)/n
M=8000; W=np.linspace(0,1,M,endpoint=False)
res={}
for K in [0.1,0.5,1.0]:
    r=rot(W,K); flat=np.abs(np.diff(r))<1e-7
    lk=np.zeros(M,bool); lk[:-1]|=flat; lk[1:]|=flat
    res[K]=r; print(f"R1b K={K}: plateau fraction {lk.mean():.3f}")
json.dump({"W":W[::16].tolist(),"r1":res[1.0][::16].tolist(),"r05":res[0.5][::16].tolist()},open('staircase.json','w'))
