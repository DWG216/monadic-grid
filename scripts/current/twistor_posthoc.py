# POST HOC (labelled): is the wave-equation residual of twistor.py a finite-difference error? Shrink the step.
src=open('twistor.py').read(); exec(src[:src.index("r,_=resid")])
xs=[rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)) for _ in range(20)]
for h in (4e-3,2e-3,1e-3,5e-4): print(f"h = {h}: max wave-equation residual {max(box(x,[0,1,2,3,4],h) for x in xs):.2e}; median {np.median([box(x,[0,1,2,3,4],h) for x in xs]):.2e}")
