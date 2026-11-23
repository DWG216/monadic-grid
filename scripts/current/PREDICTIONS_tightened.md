# Pre-registration (2026-11-22): consequences made unconditional by RH (certified) and Dirichlet GRH (claimed in the same archive, statement not yet separately vetted)
T1 [GRH-Dirichlet consequence, Ankeny/Bach] the least quadratic non-residue n(p) satisfies n(p) <= 2 (ln p)^2 for every odd prime p < 10^7; its mean over these primes lies in [3.55, 3.75] (Erdos: limit sum p_k / 2^k = 3.6746). Grid: n(p) is the first slot of Rodin's second wire (non-squares) in the doll p.
T2 [RH consequence, Carneiro-Milinovich-Soundararajan explicit form] for primes 3 < p < 10^8, the gap to the next prime is below (22/25) sqrt(p) ln p; predicted max ratio < 0.10.
T3 [GRH-Dirichlet consequence, Bach] Miller-Rabin with all bases a <= 2 (ln n)^2 detects every odd composite n < 10^6 (0 failures). Null: base 2 alone misses some (strong pseudoprimes to base 2 below 10^6: count > 0).
T4 [descriptive, not a prediction] Chebyshev bias mod 5: share of x in [10^3, 10^7] (sampled every 1000) where non-residue primes (2, 3 mod 5) lead residue primes (1, 4 mod 5); logarithmic density of the lead over the same range.

## Results
T1 pass: 0 violations among 664,578 primes; mean n(p) = 3.6631; max n(p)/(2 ln^2 p) = 0.83 (at p = 3).
T2 FAIL as pre-registered (threshold, not the theorem): the bound holds for every prime (max ratio 0.883 < 1), but the maximum is 0.883 at p = 7 (gap 4), not < 0.10; my threshold ignored tiny primes. Post hoc for p > 1000: see tightened.out (last line). Largest gap below 10^8: 220 at p = 47,326,693.
T3 pass: 0 failures among odd composites below 10^6 with bases up to 2 (ln n)^2; null: 46 strong pseudoprimes to base 2.
T4 (descriptive): non-residue primes mod 5 lead at every sampled x in [10^3, 10^7]; weighted log-density estimate 1.000 on this range (the true logarithmic density, Rubinstein-Sarnak, is below 1; leads reverse only far out, and computing it needs the linear-independence hypothesis, still open).
