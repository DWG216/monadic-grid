import numpy as np
from collections import Counter, deque
src=open('t55_open1to4.py').read()
exec('phi=(1+5**.5)/2\n'+src.split('# ---------- 2')[1].split('def shape')[0].replace('return np.round(Amk).astype(int),np.round(dims).astype(int),r','return np.round(Amk).astype(int),np.round(dims).astype(int),r,chars,C,G'))
Adj,dims,r,chars,C,G=mckay(I2)
triv=[a for a in range(r) if dims[a]==1][0]
V=[a for a in range(r) if Adj[triv,a]][0]; nbV=[a for a in range(r) if Adj[V,a]]; Mn=[a for a in nbV if a!=triv][0]
print('G0 V dim',dims[V],' neighbours of V (dims):',[int(dims[a]) for a in nbV],' M dim',dims[Mn])
rest=[a for a in range(r) if a!=Mn]
sub=Adj[np.ix_(rest,rest)]
comp=[];seen=set()
for s in range(len(rest)):
    if s in seen: continue
    st=[s];c=set([s])
    while st:
        u=st.pop()
        for v in np.where(sub[u])[0]:
            if v not in c: c.add(v); st.append(v)
    seen|=c; comp.append(sorted(rest[i] for i in c))
for cpt in comp:
    A=2*np.eye(len(cpt))-Adj[np.ix_(cpt,cpt)]; print('G1 piece',[int(dims[a]) for a in cpt],' contains vacuum:',triv in cpt,' Cartan det',round(np.linalg.det(A)))
keep=[a for a in range(r) if a!=triv]; A8=2*np.eye(8,dtype=int)-Adj[np.ix_(keep,keep)]; idx={a:i for i,a in enumerate(keep)}
# roots in simple-root coordinates; reflection s_i(b) = b - (b A)_i e_i
def roots():
    e=np.zeros(8,int); e[0]=1; S={tuple(e)}; dq=deque([e])
    while dq:
        b=dq.popleft()
        for i in range(8):
            nb=b.copy(); nb[i]-= (b@A8)[i]
            t=tuple(nb)
            if t not in S: S.add(t); dq.append(nb)
    return [np.array(s) for s in S]
Rts=roots(); print('G2 roots:',len(Rts))
def split(node):
    k=idx[node]; c=[int(rt[k]) for rt in Rts]
    return Counter(c), c
cnt,c=split(Mn); print('G3 coefficient counts:',dict(sorted(cnt.items())),' c=0:',cnt[0],' c=+-3:',cnt[3]+cnt[-3],' c=1mod3:',sum(v for kk,v in cnt.items() if kk%3==1),' c=2mod3:',sum(v for kk,v in cnt.items() if kk%3==2))
# G4: E6 nodes = the 6-node piece; project roots onto E6 weights = pairing with E6 simple roots (b A)_i for i in E6
E6=[cp for cp in comp if triv not in cp][0]; e6i=[idx[a] for a in E6]
for res_ in [1,2]:
    W=[tuple((Rts[j]@A8)[e6i]) for j in range(len(Rts)) if c[j]%3==res_]
    cw=Counter(W); print('G4 class',res_,': distinct E6 weights',len(cw),' multiplicities',set(cw.values()))
    if res_==1:
        A6=A8[np.ix_(e6i,e6i)]; Wset=set(cw); start=next(iter(Wset)); orb={start}; dq=deque([np.array(start)])
        while dq:
            w=dq.popleft()
            for i in range(6):
                nw=tuple(w-w[i]*A6[i])
                if nw not in orb: orb.add(nw); dq.append(np.array(nw))
        print('G5 E6 orbit of one weight:',len(orb),' equals the 27 set:',orb==Wset)
br=[a for a in range(r) if Adj[a].sum()==3][0]; twos=[a for a in range(r) if Adj[br,a] and dims[a]==4]
ctrl=[a for a in range(r) if dims[a]==2 and a!=V][0]
cc,_=split(ctrl); print('control: grading by the other 2-dim node:',dict(sorted(cc.items())))
