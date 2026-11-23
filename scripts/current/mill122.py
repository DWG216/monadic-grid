def U(n,u0,u1):
    a,b=u0,u1
    if n>=0:
        for _ in range(n): a,b=b,a+b
        return a
    for _ in range(-n): a,b=b-a,a
    return a
F=lambda n:U(n,0,1); V=lambda n:U(n,1,4); e=11
print("Q0 sequence -8..8:",[V(n) for n in range(-8,9)])
print("Q1 row n=0:",[V(0)**2]+[V(-k)*V(k) for k in range(1,6)],"(printed 1, 12, -10, 45, -98, 276)")
printed={-3:[-11,11,-44,99,-275],-2:[11,-11,44,-99,275],-1:[-11,11,-44,99,-275],0:[11,-11,44,-99,275],1:[-11,11,-44,99,-275],2:[11,-11,44,-99,275],3:[-11,11,-44,99,-275]}
calc={n:[V(n-k)*V(n+k)-V(n)**2 for k in range(1,6)] for n in printed}
form=all(calc[n][k-1]==-(-1)**((n-k)%2)*e*F(k)**2 for n in printed for k in range(1,6))
print("Q2 matches printed 35/35:",calc==printed," formula:",form)
print("Q3 x=0,r=1: lhs",V(-1)*V(1)-V(0)**2,"U(r)^2",V(1)**2,"; corrected holds:",all(V(x-r)*V(x+r)-V(x)**2==-(-1)**((x-r)%2)*e*F(r)**2 for x in range(-12,13) for r in range(-12,13)))
print("Q4 a=0 of p.125 form:",all(V(x-r)*V(x+r)-V(x)**2==(-1)**(x%2)*e*F(-r)*F(r) for x in range(-12,13) for r in range(-12,13)))
bad=0;tot=0
for u0 in range(1,31):
    for u1 in range(u0+1,31):
        tot+=1; m=min(range(-40,41),key=lambda n:(abs(U(n,u0,u1)),abs(n)))
        if abs(m)>1: bad+=1
print(f"Q5 min |U| within one step of 0: {tot-bad}/{tot}")
