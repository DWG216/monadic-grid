import numpy as np, json
N=64; y,x=np.mgrid[0:N,0:N]
o=((np.hypot(x-22,y-22)<9)|((abs(x-44)<3)&(abs(y-40)<16))|((abs(y-40)<3)&(abs(x-44)<16))|((abs(x-y)<2)&(x>8)&(x<30)&(y>36))).astype(float)
U=np.fft.fftshift(np.fft.fft2(o))/N                       # object wave at the plate (Fourier hologram)
A=np.abs(U).max(); f0=0.0
def record(phase_noise):
    R=A*np.exp(1j*phase_noise)                             # reference wave (coherent if noise = 0)
    I=np.abs(U+R)**2                                       # what the plate records: interference intensity
    cross=I-np.abs(U)**2-np.abs(R)**2                      # interference term U R* + U* R
    return cross
def readout(cross,mask=None):
    R0=A*np.ones_like(U)                                   # read with an ideal coherent reference
    # isolate U R*: with real reference, cross = 2 Re(U R*): recover via analytic trick using known reference phase
    Uest=cross*R0/(2*A**2)
    if mask is not None: Uest=Uest*mask
    img=np.abs(np.fft.ifft2(np.fft.ifftshift(Uest))*N)
    return img
def corr(a,b): a=a-a.mean(); b=b-b.mean(); return float((a*b).sum()/np.sqrt((a*a).sum()*(b*b).sum()))
# note: with a real cross term the reconstruction contains the object plus its mirror (twin image); compare to o + mirror
twin=o+np.flip(np.flip(o,0),1); twin=np.roll(np.roll(twin,1,0),1,1)
full=readout(record(0))
q=np.zeros((N,N)); q[:N//2,:N//2]=1                        # keep one quarter of the plate
qmask=np.fft.fftshift(np.fft.ifftshift(q))
part=readout(record(0),mask=q)
photo=o*q                                                  # a quarter of an ordinary photograph
rng=np.random.default_rng(0)
noisy={s:readout(record(rng.normal(0,s,(N,N)))) for s in (0.5,1.0,2.0)}
print('full hologram vs object+twin: %.3f'%corr(full,twin))
print('quarter of hologram, whole scene recovered: %.3f'%corr(part,twin))
print('quarter of photograph vs whole object: %.3f'%corr(photo,o))
for s,img in noisy.items(): print('reference phase jitter %.1f rad: %.3f'%(s,corr(img,twin)))
out={k:(v/v.max()).round(3).tolist() for k,v in {'object':o,'photo_quarter':photo,'holo_quarter':part,'noisy1':noisy[1.0]}.items()}
json.dump(out,open('holo_imgs.json','w'))
# fairer comparison: a central quarter of the plate (any contiguous quarter works; this one keeps the low frequencies)
c=np.zeros((N,N)); c[N//4:3*N//4,N//4:3*N//4]=1
part_c=readout(record(0),mask=c)
def quad_scores(img,ref):
    s=[]
    for a in (slice(0,N//2),slice(N//2,N)):
        for b in (slice(0,N//2),slice(N//2,N)):
            r=ref[a,b]
            if r.std()>0: s.append(corr(img[a,b],r))
    return s
print('central quarter of hologram: whole-object corr %.3f | per-quadrant %s'%(corr(part_c,twin),np.round(quad_scores(part_c,twin),2).tolist()))
print('quarter of photograph:      whole-object corr %.3f | per-quadrant %s'%(corr(photo,o),np.round(quad_scores(photo,o),2).tolist()))
out['holo_quarter']=(part_c/part_c.max()).round(3).tolist(); json.dump(out,open('holo_imgs.json','w'))
