import numpy as np
from scipy.stats import ks_2samp
N=10**7
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]
# Y1
cm=[];cls=[];turn=[]
for p in P[(P>=7)&(P<=20000)]:
    p=int(p); a,b=1,1; m=p*p
    while a%p: a,b=b,(a+b)%m
    cm.append(((a//p)%p)/p); cls.append('c' if p%5 in (2,3) else 'h')
    mu=b%p; o=1; y=mu
    while y!=1: y=y*mu%p; o+=1
    turn.append(o)
cm=np.array(cm); cls=np.array(cls); turn=np.array(turn)
print("Y1 circle vs hyperbola KS p=%.3f, mean diff=%.4f (n=%d,%d)"%(ks_2samp(cm[cls=='c'],cm[cls=='h']).pvalue, cm[cls=='c'].mean()-cm[cls=='h'].mean(),(cls=='c').sum(),(cls=='h').sum()))
for a_,b_ in ((1,2),(1,4),(2,4)):
    print(f"Y1 turn {a_} vs {b_}: KS p={ks_2samp(cm[turn==a_],cm[turn==b_]).pvalue:.3f} (n={(turn==a_).sum()},{(turn==b_).sum()})")
# Y2, Y3
r=P%5
D=np.cumsum(np.where(np.isin(r,(2,3)),1,np.where(np.isin(r,(1,4)),-1,0)))
E=np.cumsum(np.where(r==1,1,np.where(r==4,-1,0)))
mask=P>=100
print("Y2 fraction of primes x in [100,1e7] with circle ahead: %.4f"%np.mean(D[mask]>0))
xs=np.logspace(4,7,60); idx=np.searchsorted(P,xs,side='right')-1
B=D[idx]*np.log(xs)/np.sqrt(xs); C=E[idx]*np.log(xs)/np.sqrt(xs)
print("Y2 mean B=%.3f (min %.3f, max %.3f)"%(B.mean(),B.min(),B.max()))
print("Y3 mean |B| 1-vs-4 = %.3f, fraction positive = %.3f, sign changes over primes = %d"%(np.abs(C).mean(),np.mean(E[mask]>0),int(np.sum(np.diff(np.sign(E[mask]))!=0))))
np.save("yy.npy",np.vstack([xs,B,C]))
