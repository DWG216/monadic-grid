# Step 2: q-deformed (SU(2)_3, q=e^{i pi/5}) lattice dynamics = the golden chain of Fibonacci anyons
import numpy as np, itertools, sys
phi=(1+5**.5)/2
def basis(L):  # periodic fusion paths: labels 0=1(trivial),1=tau ; no two adjacent trivial
    return [s for s in itertools.product((0,1),repeat=L) if all(not(s[i]==0 and s[(i+1)%L]==0) for i in range(L))]
P={(1,0,1,1,0,1):phi**-2,(1,0,1,1,1,1):phi**-1.5,(1,1,1,1,0,1):phi**-1.5,(1,1,1,1,1,1):phi**-1,(0,1,0,0,1,0):1.0}
def H(L,J=1.0):
    B=basis(L); idx={s:k for k,s in enumerate(B)}; n=len(B); M=np.zeros((n,n))
    for k,s in enumerate(B):
        for i in range(L):
            a,b,c=s[i-1],s[i],s[(i+1)%L]
            for bp in (0,1):
                v=P.get((a,b,c,a,bp,c))
                if v is None: continue
                t=list(s); t[i]=bp; t=tuple(t)
                if t in idx: M[idx[t],k]-=J*v
    return M,B
lucas=lambda n: round(phi**n+(1-phi)**n)
print('L  dim  Lucas(L)  E0/L       gap ratio (E2-E0)/(E1-E0)')
res=[]
for L in range(6,17,2):
    M,B=H(L); E=np.sort(np.linalg.eigvalsh(M))
    Eu=np.unique(np.round(E,9))
    r=(Eu[2]-Eu[0])/(Eu[1]-Eu[0])
    res.append((L,E[0]))
    print(L,len(B),lucas(L),round(E[0]/L,6),round(r,4))
# central charge from E0(L)= e L - pi c v/(6L): need v; estimate v from gap ratio method is unreliable, so fit e and A=pi c v/6
Ls=np.array([r[0] for r in res]);E0=np.array([r[1] for r in res])
A=np.vstack([Ls,-1/Ls]).T; e,Acoef=np.linalg.lstsq(A[-4:],E0[-4:],rcond=None)[0]
print('fitted bulk energy per site e =',round(e,6),' finite-size coefficient pi*c*v/6 =',round(Acoef,5))
# velocity from first gap identified as x=3/40: E1-E0 = 2 pi v x / L
L=16;M,B=H(L);E=np.sort(np.linalg.eigvalsh(M));Eu=np.unique(np.round(E,9))
v=(Eu[1]-Eu[0])*L/(2*np.pi*(3/40)); c=6*Acoef/(np.pi*v)
print('velocity v (assuming first gap = 3/40) =',round(v,4),'  central charge c =',round(c,4),' (tricritical Ising c=7/10)')
print('rescaled low spectrum at L=16, x=(E-E0)L/(2 pi v):',np.round((Eu[:8]-Eu[0])*L/(2*np.pi*v),3))
