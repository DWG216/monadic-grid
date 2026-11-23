exec(open('frozen_fluid.py').read().split('res={}')[0])
for k,n,cap in [(4,5,600000),(8,4,600000)]:
    g,D=rep(k,n); print('k=%d n=%d dim=%d image order: %s'%(k,n,D,order(g,cap)),flush=True)
