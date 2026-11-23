import cmath, random, math
random.seed(20261121)
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def nonres(p):
    for r in range(2,p):
        if leg(r,p)==-1: return r
class F2:
    def __init__(s,p,r): s.p=p; s.r=r
    def mul(s,x,y): p=s.p; return ((x[0]*y[0]+s.r*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def pw(s,x,n):
        res=(1,0)
        while n:
            if n&1: res=s.mul(res,x)
            x=s.mul(x,x); n>>=1
        return res
def setup(p):
    r=nonres(p); K=F2(p,r); N=p*p-1
    fac=[q for q in range(2,N+1) if N%q==0 and all(q%d for d in range(2,int(q**.5)+1))]
    for a in range(p):
        for b in range(1,p):
            g=(a,b)
            if all(K.pw(g,N//q)!=(1,0) for q in fac): break
        else: continue
        break
    dlog={}; x=(1,0)
    for k in range(N): dlog[x]=k; x=K.mul(x,g)
    return K,dlog,N,r
def sqrtF2(K,d):  # sqrt of d in F_p or F_p2 representation
    p=K.p
    if d%p==0: return (0,0)
    if leg(d,p)==1:
        for t in range(p):
            if t*t%p==d%p: return (t,0)
    # d = r * u^2 -> sqrt = u*sqrt(r)
    inv_r=pow(K.r,p-2,p); u2=d*inv_r%p
    for t in range(p):
        if t*t%p==u2: return (0,t)
def ctype(M,p):
    a,b,c,d=M
    if b%p==0 and c%p==0 and (a-d)%p==0: return 'central'
    disc=((a+d)**2-4*(a*d-b*c))%p
    if disc==0: return 'unip'
    return 'split' if leg(disc,p)==1 else 'ellip'
def chi(M,p,K,dlog,N,j):
    th=lambda z: cmath.exp(2j*math.pi*j*dlog[z]/N)
    a,b,c,d=M; t=ctype(M,p); tr=(a+d)%p
    if t=='central': return (p-1)*th((a%p,0))
    if t=='unip': return -th((tr*pow(2,p-2,p)%p,0))
    if t=='split': return 0
    disc=(tr*tr-4*(a*d-b*c))%p; s=sqrtF2(K,disc); h=pow(2,p-2,p)
    z=((tr+s[0])*h%p,s[1]*h%p); zp=K.pw(z,p)
    return -(th(z)+th(zp))
def mm(A,B,p): a,b,c,d=A; e,f,g,h=B; return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
primes=[q for q in range(7,200) if all(q%d for d in range(2,int(q**.5)+1))]
ok=0; tot=0; nullhit=0; nulltot=0
for p in primes+[5]:
    Q=(1,1,1,0); M=(1,0,0,1); n=0
    while True:
        M=mm(M,Q,p); n+=1
        if M==(1,0,0,1): break
        t=ctype(M,p)
        if t=='central': continue
        pred='unip' if p==5 else ('split' if leg(5,p)==1 else 'ellip')
        tot+=1; ok+=(t==pred)
    for _ in range(50):
        R=tuple(random.randrange(p) for _ in range(4))
        if (R[0]*R[3]-R[1]*R[2])%p==0 or ctype(R,p)=='central': continue
        pred='unip' if p==5 else ('split' if leg(5,p)==1 else 'ellip')
        nulltot+=1; nullhit+=(ctype(R,p)==pred)
print(f"G2 Fibonacci walk type agreement {ok}/{tot}; null random matrices {nullhit}/{nulltot} = {nullhit/nulltot:.2f}")
for p in [5,7,11]:
    K,dlog,N,r=setup(p); j=1
    while (j*(p-1))%N==0 or (j*(p+1))%N==0 or (j%(p+1))==0: j+=1
    s=0; cnt=0
    for a in range(p):
      for b in range(p):
        for c in range(p):
          for d in range(p):
            if (a*d-b*c)%p: s+=abs(chi((a,b,c,d),p,K,dlog,N,j))**2; cnt+=1
    print(f"G3 p={p}: |G|={cnt}, <chi,chi>={s/cnt:.6f}")
def pisano(p):
    a,b,n=0,1,0
    while True:
        a,b=b,(a+b)%p; n+=1
        if (a,b)==(0,1): return n
for p in [7,13,17,11,19,29,31]:
    K,dlog,N,r=setup(p); j=1  # faithful theta: j=1
    vals=[]; M=(1,0,0,1); gates=[]
    for n in range(1,3*pisano(p)+1):
        M=mm(M,(1,1,1,0),p); v=chi(M,p,K,dlog,N,j); vals.append(v)
        if ctype(M,p)=='central': gates.append(n)
    per=next(T for T in range(1,len(vals)) if all(abs(vals[i]-vals[i+T])<1e-9 for i in range(len(vals)-T)))
    off=[abs(v) for n,v in enumerate(vals,1) if n not in gates]; on=[abs(vals[n-1]) for n in gates]
    print(f"G4 p={p} ({'circle' if leg(5,p)==-1 else 'hyperbola'}): period {per} vs pi(p) {pisano(p)}; max|chi| off gates {max(off):.3f}; |chi| at gates {set(round(x,3) for x in on)}; first gate n={gates[0]}")
# G5 trace shape
for p in [7,13,17,23]:
    K,dlog,N,r=setup(p); M=(1,0,0,1); good=0; tot=0
    L=[2,1]
    for n in range(2,200): L.append((L[-1]+L[-2])%p)
    for n in range(1,150):
        M=mm(M,(1,1,1,0),p)
        if ctype(M,p)!='ellip': continue
        tr=(M[0]+M[3])%p; tot+=1; good+=(tr==L[n]%p)
    print(f"G5 p={p}: trace(Q^n)=z+z^p equals L(n) mod p in {good}/{tot} elliptic steps")
# Rodin mod 71
p=71
print("R71a", 9*9%p, (9+1)%p, 8*9%p)
o9=next(k for k in range(1,p) if pow(9,k,p)==1); o8=next(k for k in range(1,p) if pow(8,k,p)==1)
S=set(pow(9,k,p) for k in range(o9)); QR=set(x*x%p for x in range(1,p))
print(f"R71b ord9={o9} ord8={o8} <9>==squares:{S==QR} leg(7)={leg(7,p)} coset7==nonsquares:{set(7*x%p for x in S)==set(range(1,p))-QR}")
cnt=0; two=0; lst=[]
for q in range(11,2000):
    if not all(q%d for d in range(2,int(q**.5)+1)) or q%5 not in (1,4): continue
    ph=[x for x in range(q) if (x*x-x-1)%q==0]
    cnt+=1
    for f in ph:
        o=next(k for k in range(1,q) if pow(f,k,q)==1)
        if o==(q-1)//2: two+=1; lst.append((q,f)); break
print(f"R71c split primes <2000: {cnt}; with a root phi of order (p-1)/2 (two-wire coil): {two} = {two/cnt:.2f}; first: {lst[:8]}")
print("mod 8 of two-wire primes:", sorted(set(q%8 for q,_ in lst)), " mod 4:", sorted(set(q%4 for q,_ in lst)))
