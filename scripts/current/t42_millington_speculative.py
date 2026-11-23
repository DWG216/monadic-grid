import numpy as np
def pisano(m):
    a,b,n=0,1,0
    while True:
        a,b=b,(a+b)%m; n+=1
        if (a,b)==(0,1): return n
def zeros(m,N):
    a,b=0,1; z=[]
    for n in range(N):
        if a%m==0: z.append(n)
        a,b=b,a+b
    return z
print('Moon/Earth mass ratio 1/x, x =',5.972e24/7.342e22,'  3^4 =',81,'  3^3 =',27)
print('sidereal month (days) 27.3217 vs 27; synodic 29.5306 vs L(7)=29')
print('Fibonacci mod 29: period',pisano(29),'; mod 13 zeros at',zeros(13,60)[:6],'(F(7)=13: zero every 7); mod 169 zeros',zeros(169,400)[:4])
print('Pisano periods: mod 9 ->',pisano(9),' half ->',pisano(9)//2,'; kissing numbers 2D 6, 3D 12, 4D 24')
print('sidereal days per year 366.2422 - 364 =',round(366.2422-364,4),'; solar 365.2422 - 364 =',round(365.2422-364,4))
