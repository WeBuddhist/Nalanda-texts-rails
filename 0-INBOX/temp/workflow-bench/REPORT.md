# Workflow grouping benchmark — gemini-3.8-flash thinking low vs medium

Block-boundary F1 against `0-INBOX/processed/root/` (Claude-agent grouping; editor-reviewed for Ar_3CBa_ and Ar_3CBf_). P = share of Gemini's block ends that the reference has; R = share of the reference's block ends that Gemini found.

| Text | Form | Level | Blocks (ref) | F1 | P | R | Cost | Time | Thinking tok | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| Ar_3CBf_ | free | low | 14 (17) | 0.903 | 1.000 | 0.824 | $0.024 | 44 s | 5748 |  |
| Ar_3CBf_ | free | medium | 13 (17) | 0.867 | 1.000 | 0.765 | $0.043 | 79 s | 10658 |  |
| Ar_3CBk_ | free | low | 43 (59) | 0.824 | 0.977 | 0.712 | $0.009 | 9 s | 0 |  |
| Ar_3CBk_ | free | medium | 45 (59) | 0.827 | 0.956 | 0.729 | $0.069 | 120 s | 15763 |  |
| Dh_3CFD | prose | low | 46 (49) | 0.884 | 0.913 | 0.857 | $0.017 | 18 s | 1666 |  |
| Dh_3CFD | prose | medium | 47 (49) | 0.875 | 0.894 | 0.857 | $0.075 | 124 s | 17289 |  |
| Na_3CBI | free | low | 134 (129) | 0.973 | 0.955 | 0.992 | $0.044 | 35 s | 0 |  |
| Na_3CBI | free | medium | 128 (129) | 0.981 | 0.984 | 0.977 | $0.186 | 285 s | 38099 |  |
| Ar_3CBh_ | prose | low | 122 (139) | 0.851 | 0.910 | 0.799 | $0.036 | 31 s | 2315 |  |
| Ar_3CBh_ | prose | medium | 126 (139) | 0.883 | 0.929 | 0.842 | $0.166 | 241 s | 36761 |  |
| Ar_3CBa_ | free | low | 511 (637) | 0.808 | 0.908 | 0.728 | $0.161 | 145 s | 0 |  |
| Ar_3CBa_ | free | medium | 539 (637) | 0.830 | 0.905 | 0.766 | $0.703 | 1072 s | 160125 |  |
| **mean** | | low | | **0.874** | | | $0.291 total | 281 s total | | |
| **mean** | | medium | | **0.877** | | | $1.241 total | 1920 s total | | |
