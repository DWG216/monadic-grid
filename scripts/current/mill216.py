def F(n):
    a,b=0,1
    for _ in range(abs(n)): a,b=b,a+b
    return a if n>=0 else (-1)**(-n+1)*a
def L(n): return F(n-1)+F(n+1)
ok=all(F(2*X-3)==F(X)*F(X-1)-F(X-2)*F(X-3) for X in range(-40,41)); print("M1 all X in [-40,40]:",ok, " F(11) via X=7:",F(7)*F(6)-F(5)*F(4), " F(-11) via X=-4:",F(-4)*F(-5)-F(-6)*F(-7), F(-11))
ok2=all(F(n)==F(n//2)*L(n//2)==F(n//2+1)**2-F(n//2-1)**2 for n in range(-40,41,2)); print("M2:",ok2)
bal=lambda v,m=9: ((v+m//2)%m)-m//2
fs=[bal(F(n)) for n in range(0,48)]; ls=[bal(L(n)) for n in range(0,48)]
print("M3 Fib bal mod 9:",fs[:25]); print("   Lucas bal mod 9:",ls[:25])
print("   antiperiod 12:",all(fs[n+12]==bal(-fs[n]) for n in range(36)),all(ls[n+12]==bal(-ls[n]) for n in range(36)), " period 24:",fs[:24]==fs[24:48], ls[:24]==ls[24:48])
print("M4 2*5 mod 9 =",10%9, all((F(n-1)*F(n+1)-(-1)**n)%(F(n)**2)==0 for n in range(2,30)))
pts=[(bal(5*L(n)),bal(5*F(n))) for n in range(24)]
print("M5:",all((x*x-5*y*y-(-1)**n)%9==0 for n,(x,y) in enumerate(pts)), pts)
print("M6:",all(F(n)**2-F(n-r)*F(n+r)==(-1)**((n-r)%2)*F(r)**2 for n in range(-30,31) for r in range(-30,31)))
import json; json.dump(pts,open('mill_pts.json','w'))
