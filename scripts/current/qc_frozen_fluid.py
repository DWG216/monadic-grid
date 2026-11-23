import cmath, math
print("Q1 r with integer 2cos(2pi/r), r<=60:", [r for r in range(1,61) if abs(2*math.cos(2*math.pi/r)-round(2*math.cos(2*math.pi/r)))<1e-12])
def mul(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def key(A):
    flat=[A[0][0],A[0][1],A[1][0],A[1][1]]
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]; s=cmath.sqrt(det); flat=[z/s for z in flat]
    for z in flat:
        if abs(z)>1e-7: ph=z/abs(z); break
    flat=[z/ph for z in flat]
    return tuple((round(z.real,6)+0.0,round(z.imag,6)+0.0) for z in flat)
def image(r,cap=20000):
    t=cmath.exp(2j*math.pi/r)
    g=[((-t,1),(0,1)),((1,0),(t,-t))]
    ginv=[]
    for A in g:
        det=A[0][0]*A[1][1]-A[0][1]*A[1][0]; ginv.append(((A[1][1]/det,-A[0][1]/det),(-A[1][0]/det,A[0][0]/det)))
    gens=g+ginv; I=((1,0),(0,1)); seen={key(I)}; frontier=[I]
    while frontier and len(seen)<=cap:
        nf=[]
        for A in frontier:
            for G in gens:
                B=mul(A,G); k=key(B)
                if k not in seen:
                    seen.add(k); nf.append(B)
        frontier=nf
    return len(seen), (not frontier)
res={}
for r in range(3,13):
    n,closed=image(r); res[r]=(n,closed); print(f"Q2 r={r}: elements {n}{'' if closed else '+'} closed={closed}")
print("Q2 finite set:",[r for r in res if res[r][1]])
print("Q3 r=10 order:",res[10][0]," r=5 closed:",res[5][1])
# post hoc (labelled): why r = 3 fails in the Burau form
t=cmath.exp(2j*math.pi/3); s1=((-t,1),(0,1)); s2=((1,0),(t,-t))
d2=s2[0][0]*s2[1][1]-s2[0][1]*s2[1][0]; s2i=((s2[1][1]/d2,-s2[0][1]/d2),(-s2[1][0]/d2,s2[0][0]/d2))
M=mul(s1,s2i); det=M[0][0]*M[1][1]-M[0][1]*M[1][0]; tr=(M[0][0]+M[1][1])/cmath.sqrt(det)
print("post hoc r=3: normalised trace of s1*s2^-1 =",complex(round(tr.real,9),round(tr.imag,9)),"(|trace| = 2 and not scalar => unipotent, infinite order)")
print("post hoc r=3: Jones/Temperley-Lieb rep at d = 2cos(pi/3) = 1 has 3-strand quotient of dimension", 1, "(d^2 - 1 = 0 kills the 2-dim block)")
