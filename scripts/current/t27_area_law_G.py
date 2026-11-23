import numpy as np, time
N=60
def Kmat(l):
    K=np.zeros((N,N))
    for j in range(1,N+1):
        i=j-1
        K[i,i]+= (l*(l+1))/j**2
        # (j+1/2)^2 (phi_j/j - phi_{j+1}/(j+1))^2 ; j=N term with phi_{N+1}=0
        c=(j+0.5)**2
        K[i,i]+= c/j**2
        if j<N:
            K[i+1,i+1]+= c/(j+1)**2
            K[i,i+1]-= c/(j*(j+1)); K[i+1,i]-= c/(j*(j+1))
    return K
def S_l(l,n):
    w,V=np.linalg.eigh(Kmat(l)); Om=V@np.diag(np.sqrt(w))@V.T
    A=Om[:n,:n]; B=Om[:n,n:]; C=Om[n:,n:]
    beta=0.5*B.T@np.linalg.solve(A,B); gam=C-beta
    lam=np.linalg.eigvals(np.linalg.solve(gam,beta)).real
    lam=lam[(lam>1e-16)&(lam<1)]
    xi=lam/(1+np.sqrt(1-lam**2))
    return float(-(np.log(1-xi)+xi/(1-xi)*np.log(xi)).sum())
def S_tot(n,lmax):
    tot=0
    for l in range(lmax+1):
        s=S_l(l,n); tot+=(2*l+1)*s
        if l>200 and (2*l+1)*s<1e-12: break
    return tot
t0=time.time()
ns=list(range(6,25,3)); Ss=[S_tot(n,2000) for n in ns]; R=np.array(ns)+0.5; Ss=np.array(Ss)
res={}
c2,c0=np.polyfit(R**2,Ss,1); res['A1 c (S = c R^2 + c0)']=(float(c2),float(c0))
r2=np.sum((np.polyval([c2,c0],R**2)-Ss)**2)
c3,c03=np.polyfit(R**3,Ss,1); r3=np.sum((np.polyval([c3,c03],R**3)-Ss)**2)
res['A2 residual ratio vol/area']=float(r3/r2)
s4=S_tot(24,4000); res['A3 rel change lmax 2000->4000']=float(abs(s4-Ss[-1])/Ss[-1])
res['S values']=[round(float(x),3) for x in Ss]
res['G per species (units a^2) = pi/c']=float(np.pi/c2)
res['runtime s']=round(time.time()-t0,1)
for k,v in res.items(): print(k,v)
