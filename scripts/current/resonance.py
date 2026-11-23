import numpy as np, json
from fractions import Fraction
rng=np.random.default_rng(20261121)
def rot(W,K,n=3000,burn=500):
    th=np.zeros_like(W)
    for _ in range(burn): th=th+W-K/(2*np.pi)*np.sin(2*np.pi*th)
    t0=th.copy()
    for _ in range(n): th=th+W-K/(2*np.pi)*np.sin(2*np.pi*th)
    return (th-t0)/n
def locked_fraction(K,M=6000):
    W=np.linspace(0,1,M,endpoint=False)+0.5/M; r=rot(W,K)
    lk=np.zeros(M,bool)
    for i,x in enumerate(r):
        f=Fraction(float(x)).limit_denominator(60)
        lk[i]=abs(float(f)-x)<2e-4
    return W,r,lk
out={}
for K in [0.1,0.5,1.0]:
    W,r,lk=locked_fraction(K); out[K]=(W,r,lk); print(f"R1 K={K}: locked fraction {lk.mean():.3f}")
W,r,lk=out[1.0]
def width(p,q):
    m=np.abs(r-p/q)<2e-4; return m.mean()
ws={f"{p}/{q}":width(p,q) for p,q in [(0,1),(1,2),(1,3),(2,5),(3,8)]}
print("R2 widths at K=1:",{k:round(v,4) for k,v in ws.items()})
g=(3-5**.5)/2
for K in [0.5,0.9,0.99]:
    # find W giving rotation number = golden by bisection
    lo,hi=0.3,0.45
    for _ in range(40):
        mid=(lo+hi)/2
        if rot(np.array([mid]),K,4000)[0]<g: lo=mid
        else: hi=mid
    print(f"R2 golden rotation reached at K={K}, W={lo:.6f}")
json.dump({"W":W[::10].tolist(),"r":r[::10].tolist()},open('staircase.json','w'))
def kura(N,K,signs=False,T=200,dt=0.05):
    w=0.5*np.tan(np.pi*(rng.random(N)-0.5)); th=rng.random(N)*2*np.pi
    s=np.where(rng.random(N)<0.5,-1,1) if signs else np.ones(N)
    rs=[]
    for t in range(int(T/dt)):
        z=np.mean(s*np.exp(1j*th)) if signs else np.mean(np.exp(1j*th))
        th=th+dt*(w+K*np.abs(z)*np.sin(np.angle(z)-th)*(s if signs else 1))
        if t*dt>T/2: rs.append(abs(np.mean(np.exp(1j*th))))
    return np.mean(rs)
Ks=[0.25,0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0]; res={}
for N in [50,200,2000]:
    res[N]=[kura(N,K) for K in Ks]; print("R3 N=%d"%N,[round(x,3) for x in res[N]])
print("R3 theory",[round(np.sqrt(max(0,1-1/K)),3) for K in Ks])
print("null signs K=2, N=2000:",round(kura(2000,2.0,signs=True),3),"1/sqrtN=",round(1/np.sqrt(2000),3))
json.dump({"Ks":Ks,"res":{str(k):v for k,v in res.items()}},open('kura.json','w'))
