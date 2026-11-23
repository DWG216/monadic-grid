# t19 action vs loss (pre-registered 2026-11-22 17:36)
Discrete harmonic oscillator, x(0)=0, x(T)=1, N=400 steps.
A1 [M] Morse index (number of negative Hessian eigenvalues of the action S) = floor(T/pi) for T in {1,2,4,7,10}; i.e. the classical path is a minimum only before the first conjugate point T=pi.
A2 [M] Positive control: gradient descent on S at T=1 converges to sin(t)/sin(T) (max error < 1e-3). At T=4, gradient descent does not converge to the classical path (distance grows > 10x initial).
A3 [M] Wick-rotated (Euclidean) action S_E (sign of potential flipped) is positive definite for all T tested; gradient descent converges to sinh(t)/sinh(T) at T=4 (max error < 1e-3).
A4 [M] Backprop = adjoint: for a 4-layer tanh chain, gradients from the backward costate lambda equal central finite differences (rel. error < 1e-6), and dL/dW_k = lambda_{k+1} a_k^T (outer product of backward and forward signals).
Null control: random symmetric matrix with same diagonal as Hessian -> index not equal to floor(T/pi) pattern (reported, not thresholded).
