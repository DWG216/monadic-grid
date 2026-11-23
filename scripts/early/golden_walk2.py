import numpy as np, itertools
exec(open('golden_walk.py').read().split("li,ai=walk")[0])
s2=2**.5
cases=[('Pauli C4 + T4',proj_close([X,Z]),np.array([[1,1-1j],[1+1j,-1]])/3**.5),
       ('Hurwitz C12 + T12',None,np.array([[3,1-1j],[1+1j,-3]])/11**.5),
       ('Clifford C24 + T24',C24,np.array([[-1-s2,2-s2+1j],[2-s2-1j,1+s2]]))]
hur=[q2u(q) for q in ([np.eye(4)[k]*s for k in range(4) for s in (1,-1)]+[np.array(s)/2 for s in itertools.product([1,-1],repeat=4)])]
C12=proj_close(hur); cases[1]=(cases[1][0],C12,cases[1][2])
for name,Cg,Tm in cases:
    Tm=Tm/np.sqrt(abs(np.linalg.det(Tm)))
    q=len(Cg)-1; b=2*np.sqrt(q)/(q+1); lam,_=walk(Cg,Tm,40); m=max(v for _,v in lam)
    print('%-20s |C|=%2d unitary err %.1e | max|lambda| %.4f | bound %.4f | ratio %.3f | %s'%(name,len(Cg),np.linalg.norm(Tm@Tm.conj().T-I),m,b,m/b,'PASS' if 0.9*b<=m<=b+1e-6 else 'FAIL'))
