import math
def fac(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def s(f): return ' * '.join(f'{p}^{e}' if e>1 else str(p) for p,e in sorted(f.items()))
sym={'schematic year':360,'sar':3600,"Plato's number":12960000,'Berossus great year':432000,'precession (Great Year)':25920}
obs={'Saros (months)':223,'Saros (years)':18,'Metonic (years)':19,'Metonic (months)':235,'Venus goal-year':8,'Mercury':46,'Mars a':47,'Mars b':79,'Jupiter a':71,'Jupiter b':83,'Saturn':59}
for title,d in [('SYMBOLIC',sym),('OBSERVED',obs)]:
    print(title); k=0
    for n,v in d.items():
        f=fac(v); r=all(p in (2,3,5) for p in f); k+=r
        print('   %-26s %10d = %-22s %s'%(n,v,s(f),'(2,3,5) only' if r else ''))
    print('   built from 2,3,5 only: %d of %d'%(k,len(d)))
# A3: year/synodic month ratio continued fraction
x=365.242189/29.530589; cf=[]; y=x
for _ in range(8): a=int(y); cf.append(a); y=1/(y-a)
h,k=[1,0],[0,1]; conv=[]
for a in cf: h.append(a*h[-1]+h[-2]); k.append(a*k[-1]+k[-2]); conv.append(f'{h[-1]} months / {k[-1]} yr')
print('A3 months per year = %.6f, continued fraction %s'%(x,cf)); print('   near-closures:',conv[:7])
