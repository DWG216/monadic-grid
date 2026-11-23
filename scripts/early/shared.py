import numpy as np
rng=np.random.default_rng(5); N=64
y,x=np.mgrid[0:N,0:N]/N
O=((np.abs(x-0.5)<0.2)&(np.abs(y-0.5)<0.08)|(np.abs(x-0.5)<0.08)&(np.abs(y-0.5)<0.2)).astype(float)  # a cross
pool=[(a,b) for a in range(-12,13) for b in range(-12,13) if 3<=abs(a)+abs(b)]
pool=[pool[i] for i in rng.permutation(len(pool))[:400]]
def ref(ks,ph): return sum(np.exp(2j*np.pi*(a*x+b*y)+1j*p) for (a,b),p in zip(ks,ph))/np.sqrt(len(ks))
def fid(RA,RB):
    H=np.abs(O+RA)**2; img=H*RB            # read with B's reference
    # image term O*conj(RA)*RB; compare with O (complex correlation, all terms included)
    c=np.vdot(O.ravel(),img.ravel()); return abs(c)/(np.linalg.norm(O)*np.linalg.norm(O))/1.0
def run(f,coherent,trials=20):
    out=[]
    for t in range(trials):
        idx=rng.permutation(len(pool)); A=[pool[i] for i in idx[:40]]; s=int(round(40*f))
        B=A[:s]+[pool[i] for i in idx[40:80-s]]
        phA=rng.uniform(0,2*np.pi,40); phB=np.concatenate([phA[:s] if coherent else rng.uniform(0,2*np.pi,s), rng.uniform(0,2*np.pi,40-s)])
        out.append(fid(ref(A,phA),ref(B,phB)))
    return np.mean(out)
print('S1/S2 fidelity vs overlap fraction f (agreed phases | random phases on shared waves)')
for f in (0,0.25,0.5,0.75,1.0):
    print('   f=%.2f: %.3f | %.3f'%(f,run(f,True),run(f,False)))
print('S3: 20 monads with a phase-agreed core of c wavevectors')
for c in (0,10,20,30,40):
    core=[pool[i] for i in range(c)]; corep=rng.uniform(0,2*np.pi,c)
    mons=[]
    for m in range(20):
        priv=[pool[i] for i in rng.choice(np.arange(c,len(pool)),40-c,replace=False)]
        mons.append((core+priv,np.concatenate([corep,rng.uniform(0,2*np.pi,40-c)])))
    vals=[fid(ref(*mons[i]),ref(*mons[j])) for i in range(20) for j in range(20) if i!=j]
    print('   c=%2d: mean cross-reading fidelity %.3f'%(c,np.mean(vals)))
