# Pre-registration (2026-11-22, 16:55): the multiverse as the branching aether fluid (record §87)
Histories = reduced braid words in the 3-strand Burau representation at q = e^(2 pi i / r) (as §57); a branch = a distinct projective state reached by histories of length <= L. Fungibility = (number of histories) / (number of distinct states).
SANITY RUN (seen, L = 8): r = 4: 1, 5, 15, 23, 24 then 24 (saturates at the order 24); r = 6: saturates at 12; r = 10: at 60; r = 5: 1, 5, 17, 42, 90, 184, 360, 690, 1314 (ratio 1.90 at L = 8). Fungibility at L = 8: 547 (r = 4), 1093 (r = 6), 219 (r = 10), 10 (r = 5).
B1 [real] frame (r = 4, 6, 10): branch count constant from L = 8 to L = 12, equal to the group order (24, 12, 60).
B2 [real] fluid (r = 5, 7, 8, 12): branch count keeps growing, ratio B(L)/B(L-1) above 1.5 at every L from 8 to 12.
B3 [real] fungibility at L = 12: above 10^4 for every frame point and below 50 for every fluid point.
E1 [exploratory] r = 3 (unipotent Burau case, §57); the fluid growth ratios at L = 12.
Reading fixed in advance: in the frame, exponentially many histories land on finitely many states (fungible, re-merging; classically simulable, §57); in the fluid they keep differentiating. A Deutsch multiverse of distinct branches exists only in the fluid; in the frame it collapses to a finite set.

## Results (branching.log)
B1 PASS: r = 4, 6, 10 constant at 24, 12, 60 from L = 8 (r = 10 from L = 6).
B2 PASS: fluid ratios at L = 8..12 all above 1.5: r = 5 1.90 -> 1.885; r = 7 1.99 -> 1.976; r = 8 1.75 -> 1.726; r = 12 1.96 -> 1.948.
B3 FAIL as registered: frame fungibility 17,715 / 44,287 / 88,573 (above 10^4, as predicted), fluid 46.0 (r = 7), 50.3 (r = 12), 63.6 (r = 5), 123.8 (r = 8): three of four above my bound of 50. The separation is 140-1,900 fold, but the braid relations (s1 s2 s1 = s2 s1 s2, the centre) make many reduced words coincide even in the fluid; the bound ignored them.
E1 (exploratory, registered): r = 3 grows polynomially: 1, 5, 17, 40, 72, 112, 162, 220, 288, 364, 450, 544, 648 (second differences about 8-10, roughly 4.6 L^2); ratios fall toward 1 (1.19 at L = 12). The fluid ratios differ by r (1.73-1.98), so the images are not all the same group at these lengths.
