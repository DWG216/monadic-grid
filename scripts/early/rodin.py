from math import gcd
F=[0,1]
for i in range(800): F.append(F[-1]+F[-2])
L=[2,1]
for i in range(800): L.append(L[-1]+L[-2])
def cyc(a,m):
    out=[1]
    while True:
        x=out[-1]*a%m
        if x==1: return out
        out.append(x)
# R1
fwd=cyc(2,9); rev=[pow(5,k,9) for k in range(6)]
print('R1 forward',fwd,'reverse',rev)
for s in range(6):
    prod=[fwd[k]*rev[(k-s)%6]%9 for k in range(6)]
    print('   shift',s,'products',prod,'constant' if len(set(prod))==1 else 'NOT constant')
# R2
grey=[(1+15*k)%36 or 36 for k in range(12)]; brown=[g+1 for g in grey]
print('R2 grey',grey,'\n   brown',brown)
cls=lambda S: sorted(set(x%9 for x in S))
vac=[x for x in range(1,37) if x not in grey and x not in brown]
print('   classes mod 9: grey',cls(grey),'brown',cls(brown),'vacant',cls(vac),'| vacant = multiples of 3:',vac==list(range(3,37,3)))
lab={**{r:'g' for r in cls(grey)},**{r:'b' for r in cls(brown)},**{r:'v' for r in cls(vac)}}
print('   doubling cycle by wire:',' '.join('%d%s'%(x,lab[x]) for x in fwd),'| 2*vacant =',sorted(2*x%9 for x in cls(vac)))
# R3/R4 word sums
def wordsums(n,sign=1,count=None):
    m=F[n]**2
    step=n  # zeros of F mod F(n) at multiples of n
    out=[]
    for k in range(count or 8):
        xs=range(k*step+1,k*step+step)
        if sign>0: S=sum(F[x] for x in xs)
        else: S=sum((-1)**(x+1)*F[x] for x in xs)   # F(-x)
        out.append(S%m)
    return out,m
def bal(v,m):
    v%=m; return v-m if v>m//2 else v
for n in (4,5,6,7):
    for sg,name in ((1,'F(x)  '),(-1,'F(-x) ')):
        ws,m=wordsums(n,sg,12)
        rat=[ (ws[k+1]*pow(ws[k],-1,m))%m if gcd(ws[k],m)==1 else None for k in range(len(ws)-1)]
        dif=[(ws[k+1]-ws[k])%m for k in range(len(ws)-1)]
        print('R3/4 MNS-%d %s word sums'%(m,name),ws,'| ratios',sorted(set(rat)),'| diffs',sorted(set(dif)))
# R5
for m in (9,25,64,169):
    z=[x for x in range(1,400) if F[x]%m==0][:3]
    print('R5 mod',m,'L(x)L(-x) at F-zeros',[ ((-1)**x*L[x]*L[x])%m for x in z])
# C1
for a,m in ((4,9),(3,7)):
    c=cyc(a,m); inv=pow(a,-1,m); r=[pow(inv,k,m) for k in range(len(c))]
    print('C1 a=%d mod %d:'%(a,m),[sorted(set(c[k]*r[(k-s)%len(c)]%m for k in range(len(c)))) for s in range(len(c))])
# C2
for st in (7,11,13,15,17,21,33):
    w=sorted(set((1+st*k)%36 for k in range(36)))
    print('C2 step',st,'gcd',gcd(st,36),'slots per wire',len(w),'classes mod 9',sorted(set(x%9 for x in w)))
