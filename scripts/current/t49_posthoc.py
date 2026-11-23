import numpy as np
src=open('t49_peec.py').read(); exec(src.split("s1,s2,f2,r1,r2,fsr,hits=analyse")[0])
Lp,C=build(15)
print(' f(MHz)    r1      r2     r1^2')
for f in [20e6,40e6,56e6,80e6,120e6,200e6,300e6,450e6,600e6,678e6,800e6,1200e6,2000e6]:
    P=[powers(Lp,C,f,s)[0] for s in range(3)]; r1,r2=P[1]/P[0],P[2]/P[0]
    print(f'{f/1e6:7.0f} {r1:8.3f} {r2:8.3f} {r1*r1:8.3f}')
