# Workflow grouping benchmark — gemini-3.8-flash thinking low vs medium

Block-boundary F1 against `0-INBOX/processed/root/` (Claude-agent grouping; editor-reviewed for Ar_3CBa_ and Ar_3CBf_). P = share of Gemini's block ends that the reference has; R = share of the reference's block ends that Gemini found.

| Text | Form | Level | Blocks (ref) | F1 | P | R | Cost | Time | Thinking tok | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| Ar_3CBf_ | free | low | 13 (17) | 0.867 | 1.000 | 0.765 | $0.003 | 4 s | 0 |  |
| Ar_3CBf_ | free | medium | 14 (17) | 0.903 | 1.000 | 0.824 | $0.030 | 55 s | 7326 |  |
| Ar_3CBa_ | free | low | 0 (637) | 0.000 | 0.000 | 0.000 | $0.190 | 144 s | 0 | grouping group-in-part4.md: blocks must cover lines 1707–2279 exactly once, in order (missing [], not in the input []) |
| Ar_3CBa_ | free | medium | 527 (637) | 0.828 | 0.915 | 0.757 | $0.629 | 840 s | 141274 |  |
| Ar_3CBk_ | free | low | 43 (59) | 0.824 | 0.977 | 0.712 | $0.010 | 9 s | 0 |  |
| Ar_3CBk_ | free | medium | 48 (59) | 0.860 | 0.958 | 0.780 | $0.085 | 125 s | 20280 |  |
| Na_3CBI | free | low | 133 (129) | 0.977 | 0.962 | 0.992 | $0.066 | 41 s | 0 |  |
| Na_3CBI | free | medium | 128 (129) | 0.988 | 0.992 | 0.984 | $0.161 | 253 s | 37220 |  |
| Ar_3CBh_ | prose | low | 142 (139) | 0.875 | 0.866 | 0.885 | $0.029 | 14 s | 0 |  |
| Ar_3CBh_ | prose | medium | 128 (139) | 0.884 | 0.922 | 0.849 | $0.140 | 219 s | 30149 |  |
| Dh_3CFD | prose | low | 42 (49) | 0.857 | 0.929 | 0.796 | $0.011 | 7 s | 0 |  |
| Dh_3CFD | prose | medium | 44 (49) | 0.882 | 0.932 | 0.837 | $0.028 | 36 s | 4516 |  |
| **mean** | | low | | **0.733** | | | $0.308 total | 220 s total | | |
| **mean** | | medium | | **0.891** | | | $1.074 total | 1528 s total | | |
