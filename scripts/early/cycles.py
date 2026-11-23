import numpy as np
rng=np.random.default_rng(0)
T,R,P,S=5,3,1,0; rounds=5; err=0.02
strats=['ALLC','ALLD','TFT']
def move(s,last):  # last = partner's previous move (1 coop) or None
    if s=='ALLC': m=1
    elif s=='ALLD': m=0
    else: m=1 if last in (None,1) else 0
    return m if rng.random()>err else 1-m
def play(a,b):
    la=lb=None; pa=pb=0; ca=0
    for _ in range(rounds):
        ma,mb=move(a,lb),move(b,la)
        pa+= {(1,1):R,(1,0):S,(0,1):T,(0,0):P}[(ma,mb)]; pb+={(1,1):R,(1,0):T,(0,1):S,(0,0):P}[(ma,mb)]
        ca+=ma+mb; la,lb=ma,mb
    return pa/rounds,pb/rounds,ca/(2*rounds)
A=np.zeros((3,3)); C=np.zeros((3,3))
for i,a in enumerate(strats):
    for j,b in enumerate(strats):
        r=[play(a,b) for _ in range(3000)]; A[i,j]=np.mean([x[0] for x in r]); C[i,j]=np.mean([x[2] for x in r])
print('payoff matrix (row vs column) ALLC ALLD TFT:\n',np.round(A,2))
def cycle(x0):
    x=x0.copy()
    for g in range(60):
        f=A@x; w=np.exp(1.0*(f-f.max())); x=x*w; x/=x.sum(); x=0.99*x+0.01/3
    return x, x@C@x
def history(k,ncyc=30):
    out=[]; summary=None
    for c in range(ncyc):
        if k==0 or summary is None: p=np.ones(3)/3
        else: p=np.array([summary/2,1-summary,summary/2])
        counts=rng.multinomial(200,p); x0=counts/200
        x,coop=cycle(x0); out.append(coop)
        if k>0:
            share=x[0]+x[2]; L=2**k-1; summary=np.round(share*L)/L if L>0 else 0.5
    return np.array(out)
print('\n k | mean coop cycles 21-30 | lag-1 correlation | share of histories ending cooperative (>0.5)')
res={}
for k in (0,1,2,4,8):
    H=np.array([history(k) for _ in range(20)]); res[k]=H
    a=H[:,:-1].ravel(); b=H[:,1:].ravel(); r=np.corrcoef(a,b)[0,1] if a.std()>1e-9 and b.std()>1e-9 else float('nan')
    print('%2d | %.3f | %.2f | %.2f'%(k,H[:,20:].mean(),r,(H[:,-1]>0.5).mean()))
print('\nk=0 single-cycle spread: min %.3f max %.3f'%(res[0].min(),res[0].max()))
np.save('cycles_res.npy',np.array([res[k] for k in (0,1,2,4,8)]))
