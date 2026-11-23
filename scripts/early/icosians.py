import itertools, numpy as np
phi=(1+5**.5)/2; a,b,c=0.5,phi/2,1/(2*phi)
pts=set()
def add(v): pts.add(tuple(round(x,9) for x in v))
for i in range(4):
  for s in (1,-1): v=[0]*4; v[i]=s; add(v)
for s in itertools.product((a,-a),repeat=4): add(s)
even=[p for p in itertools.permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==1]
for p in even:
  for s in itertools.product((1,-1),repeat=3):
    base=[s[1]*b,s[0]*a,s[2]*c,0]; add([base[p[k]] for k in range(4)])
P=[np.array(v) for v in pts]
def qm(x,y):
  a1,b1,c1,d1=x;a2,b2,c2,d2=y
  return np.array([a1*a2-b1*b2-c1*c2-d1*d2,a1*b2+b1*a2+c1*d2-d1*c2,a1*c2-b1*d2+c1*a2+d1*b2,a1*d2+b1*c2-c1*b2+d1*a2])
S=set(pts)
closed=all(tuple(round(x,9) for x in qm(x,y)) in S for x in P for y in P)
noncomm=sum(not np.allclose(qm(x,y),qm(y,x)) for x in P for y in P)
print('unit icosians:',len(P),' all norm 1:',all(abs(np.dot(v,v)-1)<1e-9 for v in P))
print('closed under quaternion multiplication (a group of order 120):',closed)
print('ordered pairs that do not commute:',noncomm,'of',len(P)**2)
