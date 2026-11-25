# t90 Leptogenesis from the heaviest right-handed neutrino, with the grid's Dirac masses (pre-registered 2026-11-25, before any t90 code is written or run)

Ground and bridges carried over: light neutrinos (section 125) m1 = 0.365 meV, normal ordering, sum 59.16 meV; Dirac masses m_D = diag(m_e, m_mu, m_tau) in the charged-lepton basis (t89, the lepton bifundamental). Mixing (NuFIT-6-type central values, normal ordering): theta12 = 33.4 deg, theta13 = 8.6 deg, theta23 = 49.0 deg, delta = 212 deg. Majorana phases alpha21, alpha31 unknown: scanned uniformly on [0, 2 pi)^2, 20,000 points, seed 90.

Construction [M, standard]: m_nu = U* diag(m) U^dagger; M_R = -m_D^T m_nu^(-1) m_D; Takagi-diagonalise M_R = W* diag(M) W^dagger; Dirac couplings in the heavy basis m_D W. Flavoured CP asymmetries eps_i,alpha with the full one-loop vertex + self-energy functions (Covi-Roulet-Vissani), v = 174 GeV. Decay parameters K_i,alpha = |(m_D W)_alpha,i|^2 / (M_i m*), m* = 1.08e-3 eV. Efficiency kappa(K) = (2/(K z_B))(1 - exp(-K z_B/2)), z_B = 2 + 4 K^0.13 exp(-2.5/K). Each flavour alpha treated separately (three-flavour approximation throughout); the asymmetry produced by N_i in flavour alpha is washed out by every lighter N_j by exp(-3 pi K_j,alpha / 8). eta_B = 0.0096 * sum. Observed 6.1e-10.

S1 Sanity: the seesaw round trip m_D M_R^(-1) m_D^T reproduces m_nu to 1e-8 relative.
S2 Sanity: with U = identity the heavy masses are t89's (7.2e5, 1.3e9, 6.3e10 GeV) and every eps vanishes (< 1e-20).
P1 [M] At least 1% of the Majorana-phase plane gives eta_B >= 6.1e-10.
P2 [M] Where P1 holds, the asymmetry comes mainly from the heaviest N (its share of eta_B > 50% at the best point).
Information: heavy masses at the scan's median; max eta_B; the fraction within a factor 2 of observation.

Verdict: P1-P2 pass -> the grid's Dirac masses give the observed matter excess from the heaviest right-handed neutrino, for a band of Majorana phases that neutrinoless double beta decay can probe. P1 fail -> the matter excess needs another route (resonant or non-thermal) and the bridge goes in the correction map.
