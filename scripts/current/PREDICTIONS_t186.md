# PREDICTIONS t186: ranking the dissonances by when the record repeats

Registered 2026-11-28, committed before t186_dissonance.py is written or run. Disclosure: the arithmetic below is simple enough that the ranking and its correlation were worked out while designing; the code reproduces them, and the derivation, not the comparison, is the content.

Derivation [S]. Two harmonic tones at the ratio p/q (lowest terms) leave a record that repeats exactly after q periods of the lower tone, which is p periods of the upper. Nothing privileges either tone, and intervals compose by multiplication, so the repeat is counted in the geometric-mean period: D = √(pq) periods. Until the record repeats, the meeting is not held as one record; the longer that takes, the more the two tones beat against each other. D extends t182's meeting share (which ranked only the consonances) to every interval, with the same just ratios as t182.

P1 [M]: D orders the eight consonances exactly as t182's meeting share (unison, octave, fifth, fourth, major sixth, major third, minor third, minor sixth), and has no ties among the thirteen intervals.
P2 [M]: the Spearman correlation between the D ranking and the historical median ranking of the chromatic dyads (Schwartz, Howe and Purves 2003, Figure 6, summarising Malmberg 1918 and six earlier studies: P1, P8, P5, P4, M3, M6, m6, m3, TT, m7, M2, M7, m2) is at least 0.8.
Reported: the ranking of the five dissonances, and where it departs from the historical order.
Gate: mathematics and music; public.

## Scoring (2026-11-28), run 1 (t186_run1.log)
- P1 PASS: D = 1, 1.41, 2.45, 3.46, 3.87, 4.47, 5.48, 6.32 for the consonances in t182's order; no ties.
- P2 PASS: Spearman 0.918 against the historical median order.
Reported: the dissonances, least to most: major second (8.5), major seventh (11.0), minor seventh (12.0), minor second (15.5), tritone (37.9). The historical order is tritone, minor seventh, major second, major seventh, minor second. The large departure is the tritone: as 45/32 its record takes 38 mean periods to repeat; heard as the simpler 7/5 it would take 5.9 and sit among the consonances. Which ratio the record uses for a tempered interval is a question for the ground (the simplest ratio within the record's resolution); not yet registered.
