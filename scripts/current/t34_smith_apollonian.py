import numpy as np, itertools
# Descartes form Q(k) = (sum k)^2 - 2 sum k^2 ; as a quadratic form k^T M k
M=np.ones((4,4))-2*np.eye(4)
w=np.linalg.eigvalsh(M); print('Descartes form eigenvalues (signature):',np.round(w,6))
# Apollonian generators: k_i -> 2(sum of others) - k_i
S=[]
for i in range(4):
    A=np.eye(4); A[i,:]=2; A[i,i]=-1; S.append(A)
print('generators preserve the form:',all(np.allclose(A.T@M@A,M) for A in S))
# integral packing from (-1,2,2,3)
root=(-1,2,2,3); seen={tuple(sorted(root))}; frontier=[np.array(root)]; curv=set(root); bad=0
for depth in range(7):
    new=[]
    for q in frontier:
        for A in S:
            q2=A@q
            if q2.min()<-1 or q2.max()>500: continue
            t=tuple(sorted(q2))
            if t in seen: continue
            seen.add(t); new.append(q2); curv.update(q2.tolist())
            if abs(q2@M@q2)>1e-9: bad+=1
    frontier=new
print('quadruples generated:',len(seen),' all null (Q=0):',bad==0,' all integer:',all(float(c).is_integer() for c in curv))
print('smallest curvatures:',sorted(curv)[:15])
# Smith chart: Gamma = (z-1)/(z+1) maps Re z>0 onto |Gamma|<1; VSWR and hyperbolic distance from centre
for z in [1,2,0.5,1+1j,3-2j,1j]:
    G=(z-1)/(z+1); g=abs(G); vswr=(1+g)/(1-g) if g<1 else np.inf
    d=2*np.arctanh(g) if g<1 else np.inf
    print(f'z={z}: |Gamma|={g:.4f}  VSWR={vswr:.4f}  ln VSWR={np.log(vswr) if np.isfinite(vswr) else np.inf:.4f}  hyperbolic dist={d:.4f}')
