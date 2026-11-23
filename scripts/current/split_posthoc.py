# POST HOC (labelled): are the S1 residuals numerical? Vary the circle resolution NT and the step h.
src=open('split.py').read()
for NT in (256,1024,4096):
    for h in (1e-4,1e-5):
        s=src.replace('NT=256',f'NT={NT}').replace('def dx(F,x,i,j,h=1e-5)',f'def dx(F,x,i,j,h={h})')
        g={}; exec(s[:s.index('x0=rng')],g); g['rng']=__import__('numpy').random.default_rng(7)
        print(f"NT={NT}, h={h}: +2 residual {g['res_plus'](g['psi']):.1e}; -2 residual {g['res_minus'](g['phi']):.1e}",flush=True)
