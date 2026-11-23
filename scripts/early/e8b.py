exec(open('e8.py').read().split('Q=[toq(r) for r in Bz]')[0])
import numpy as np
Q=[toq(r) for r in Bz]
Bm=np.array([[float(c) for x in v for c in x] for v in Q])      # basis rows, 8 coords
def coords(v):  # solve for coefficients in the Z-basis
  x=np.linalg.solve(Bm.T,np.array([float(c) for t in v for c in t])); return x
def mulnum(u,num):  # multiply quaternion u (coords in Q(sqrt5)) by scalar num=(r,s)
  r,s=num; return [(a*r+5*b*s, a*s+b*r) for (a,b) in u]
norm=lambda u,al,be: al*re_inner(u,u)[0]+be*re_inner(u,u)[1]
psi=(Fr(1,2),Fr(-1,2))   # psi=(1-sqrt5)/2
phi=(Fr(1,2),Fr(1,2))
for al,be,tag,scal in [(2,2,'2(a+b)',psi),(2,-2,'2(a-b)',phi)]:
  roots=units+[mulnum(u,scal) for u in units]
  inlat=all(np.allclose(c:=coords(r),np.round(c)) for r in roots)
  ns=set(norm(r,al,be) for r in roots)
  distinct=len({tuple(r2 for t in r for r2 in t) for r in roots})
  print(f'form {tag}: roots = units and {"psi" if scal==psi else "phi"}*units -> distinct {distinct}, all in lattice {inlat}, norms {sorted(ns)}')
