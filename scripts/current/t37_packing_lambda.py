import numpy as np, sys
sys.setrecursionlimit(10000)
Tmax=20000; ks=[-1,2,2,3]
def rec(a,b,c,d):
    k=2*(a+b+c)-d
    if k>Tmax: return
    ks.append(k); rec(k,b,c,a); rec(a,k,c,b); rec(a,b,k,c)
# the packing from root (-1,2,2,3): generate from each of the 4 positions of the root quadruple
r=[-1,2,2,3]
rec(r[0],r[1],r[2],r[3]); rec(r[0],r[1],r[3],r[2]); rec(r[0],r[2],r[3],r[1]); rec(r[1],r[2],r[3],r[0])
ks=np.sort(np.array(ks))
Ts=np.logspace(2.5,np.log10(Tmax),12); N=[np.sum(ks<=T) for T in Ts]
delta=np.polyfit(np.log(Ts),np.log(N),1)[0]
print('circles counted:',len(ks),' delta fit:',round(delta,4),' (Hausdorff 1.30568)')
print('implied Lambda exponent from packing count: -delta/2 =',round(-delta/2,3),'  Sorkin 4-volume count: -2')
T=1e61; print('at T=1e61: packing gives Lambda ~',f'{T**(-delta/2):.1e}','; 4-volume count gives',f'{T**-2:.1e}','; observed ~1e-122')
