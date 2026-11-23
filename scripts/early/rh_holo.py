import numpy as np, json
def theta(t): return t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
def Z(t):
    a=np.sqrt(t/(2*np.pi)); N=int(np.floor(a)); p=a-N
    n=np.arange(1,N+1)
    s=2*np.sum(np.cos(theta(t)-t*np.log(n))/np.sqrt(n))
    C0=np.cos(2*np.pi*(p*p-p-1/16))/np.cos(2*np.pi*p)
    return s+(-1)**(N-1)*(t/(2*np.pi))**(-0.25)*C0
ts=np.arange(10,400,0.02); zs=np.array([Z(t) for t in ts]); zeros=[]
for i in range(len(ts)-1):
    if zs[i]*zs[i+1]<0:
        a,b=ts[i],ts[i+1]
        for _ in range(40):
            m=(a+b)/2
            if Z(a)*Z(m)<=0: b=m
            else: a=m
        zeros.append((a+b)/2)
zeros=np.array(zeros); print('zeros found up to t=400:',len(zeros),' first five',np.round(zeros[:5],4))
# Riemann-von Mangoldt count check: N(T) ~ T/2pi log(T/2pi e)+7/8
T=400; print('expected count to 400: %.1f'%(T/(2*np.pi)*np.log(T/(2*np.pi*np.e))+7/8))
# primes / von Mangoldt
X=np.linspace(2,60,1161)
def psi_true(x):
    s=0
    for n in range(2,int(x)+1):
        m=n;p=None
        for q in range(2,n+1):
            if m%q==0: p=q;break
        while m%p==0: m//=p
        if m==1: s+=np.log(p)
    return s
true=[psi_true(x) for x in X]
def psi_K(x,K):
    g=zeros[:K]; rho=0.5+1j*g
    return x - np.sum(2*np.real(x**rho/rho)) - np.log(2*np.pi) - 0.5*np.log(1-x**-2)
out={'X':X[::5].round(2).tolist(),'true':np.array(true)[::5].round(3).tolist()}
for K in (5,30,len(zeros)):
    v=np.array([psi_K(x,K) for x in X]); out['K%d'%K]=v[::5].round(3).tolist()
    print('K=%3d zeros: mean |error| vs true psi on [2,60] = %.3f'%(K,np.mean(np.abs(v-np.array(true)))))
# equal amplitude: off-line test - push one zero to sigma=0.6 and see error growth
json.dump(out,open('rh_holo.json','w'))
