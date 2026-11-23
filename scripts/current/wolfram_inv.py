import numpy as np
def step_all(rule,n):
    N=1<<n; s=np.arange(N,dtype=np.int64)
    bits=[(s>>i)&1 for i in range(n)]; out=np.zeros(N,np.int64)
    for i in range(n):
        l,c,r=bits[(i+1)%n],bits[i],bits[(i-1)%n]
        out|=((rule>>(l*4+c*2+r))&1)<<i
    return len(np.unique(out))/N
for rule in (30,110,204,170,150):
    print(rule,[ (n,round(step_all(rule,n),3)) for n in range(8,17)])
bad=[m for m in range(2,201) if len({((b)%m,(a+b)%m) for a in range(m) for b in range(m)})!=m*m]
print("Fibonacci step non-bijective moduli 2..200:",bad)
