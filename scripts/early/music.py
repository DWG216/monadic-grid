import math
phi=(1+5**.5)/2
def mos(g,N=60):  # sizes n where n stacked generators (mod 1) give exactly 2 step sizes
    out=[]
    for n in range(2,N+1):
        pts=sorted((k*g)%1 for k in range(n)); gaps=[(pts[(i+1)%n]-pts[i])%1 or 1 for i in range(n)]
        if len({round(x,9) for x in gaps})==2: out.append(n)
        if len({round(x,9) for x in gaps})>3: print('three-gap violated!')
    return out
fifth=math.log2(1.5)
print('scales with two step sizes, generator = fifth :',mos(fifth))
print('scales with two step sizes, generator = golden:',mos(1/phi))
# commas tempered out by 12-equal: map prime exponents (2,3,5) -> steps (12,19,28)
val=(12,19,28)
for name,e in [('Pythagorean comma 3^12/2^19',(-19,12,0)),('syntonic comma 81/80',(-4,4,-1)),('diesis 128/125',(7,0,-3))]:
    print('%-28s maps to %d steps in 12-equal'%(name,sum(a*b for a,b in zip(e,val))))
print('tritone in 12-equal = 2^(6/12) =',2**.5,'(sqrt 2) | minor third x4 =',2**(12/12))
