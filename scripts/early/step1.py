# Step 1: matrix Fibonacci, exact integer arithmetic
def mul(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
                      (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
tr=lambda M:M[0][0]+M[1][1]
det=lambda M:M[0][0]*M[1][1]-M[0][1]*M[1][0]
inv=lambda M:((M[1][1],-M[0][1]),(-M[1][0],M[0][0]))  # inverse for det 1
def run(A,B,N=12,label=''):
    M=[B,A]
    for _ in range(N): M.append(mul(M[-1],M[-2]))
    t=[tr(m) for m in M]
    I=[t[n+1]**2+t[n]**2+t[n-1]**2-t[n+1]*t[n]*t[n-1]-2 for n in range(1,len(t)-1)]
    comm=tr(mul(mul(A,B),mul(inv(A),inv(B))))
    print(label)
    print('  traces:',t[:9],'...')
    print('  invariant along sequence (all equal?):',len(set(I))==1,'value',I[0],'| tr(A B A^-1 B^-1) =',comm)
    print('  digits in last trace:',len(str(abs(t[-1]))))
# non-commuting golden boosts (both det 1)
S=((2,1),(1,1)); T=((1,1),(1,2))            # Q^2 and a boost in a different direction
U=((1,1),(0,1)); V=((1,0),(1,1))            # the two unipotent generators of the modular group
C=((2,1),(1,1)); D=((5,3),(3,2))            # Q^2 and Q^4: commute
run(S,T,label='Non-commuting: Q^2 and a differently-directed golden boost')
run(U,V,label='Non-commuting: modular-group generators')
run(C,D,label='Commuting control: Q^2 and Q^4 (Millington flat case)')
# Millington's sign alternation: with det A=-1 (Q itself) determinants alternate in a Fibonacci pattern
Q=((1,1),(1,0)); I2=((1,0),(0,1))
M=[I2,Q]
for _ in range(10): M.append(mul(M[-1],M[-2]))
print('det signs with M0=I, M1=Q:',[det(m) for m in M])
