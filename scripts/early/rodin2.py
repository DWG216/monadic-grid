def fib_mod(N,m):
    a,b=0,1; out=[0]
    for _ in range(N): a,b=b,(a+b)%m; out.append(a)
    return out
def is_sq(x,p): return pow(x%p,(p-1)//2,p)==1
print('Q1 shifts 3,4,5 ->',[pow(2,s,9) for s in (3,4,5)],' negatives of',[(-pow(2,s,9))%9 for s in (0,1,2)])
for n,p in ((4,3),(5,5),(7,13),(11,89),(13,233),(17,1597)):
    M=p*p; f=fib_mod(n*12+2,M)
    ws=[sum(f[k*n+1:k*n+n])%M for k in range(10)]
    r=ws[1]*pow(ws[0],-1,M)%M
    geo=all(ws[k+1]==ws[k]*r%M for k in range(9))
    m=fib_mod(n+1,p)[n+1]
    pred = (n%2==0 and p%4==3) or (n%2==1 and p%8!=1)
    alt=[ 's' if is_sq(w,p) else 'n' for w in ws[:8]]
    print('n=%2d p=%4d: geometric %s, r=%d, r mod p=%d, m=F(n+1) mod p=%d, m^2=%d (=(-1)^n %s) | wires %s | predicted alternate %s, observed %s'%(
        n,p,geo,r,r%p,m,m*m%p,(m*m-(-1)**n)%p==0,''.join(alt),pred,not is_sq(r,p)))
# Q4
ws=[7,1,18,24]; print('Q4 mod 25 word sums',ws,'wires',['square' if is_sq(w,5) else 'non-square' for w in ws])
# control
def rec(N,m):
    a,b=0,1; out=[0]
    for _ in range(N): a,b=b,(b+2*a)%m; out.append(a)
    return out
for p in (3,5,7,11,13):
    s=rec(200,p); z=next(k for k in range(1,200) if s[k]==0)
    print('control x+2x p=%d first zero at %d, multiplier %d, square? %s'%(p,z,s[z+1],is_sq(s[z+1],p)))
