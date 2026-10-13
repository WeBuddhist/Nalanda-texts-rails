# Gemini benchmark — gemini-3.8-flash, thinking low vs high, 3 runs per setting

Baseline: Opus 5.5 runs `o2-r1..r3` (same prompts, same scoring).
Composite = mean of boundary F1, heading F1, placement × recall, ID × recall. Median over runs (min–max).

| file | Opus 5.5 | Gemini 3.8-flash low | Gemini 3.8-flash high |
|---|---|---|---|
| taranatha | 0.850 (0.849–0.851) | 0.869 (0.825–0.871) | 0.898 (0.896–0.900) |
| dharmabhadra | 0.994 (0.994–0.994) | 0.990 (0.990–0.990) | 0.992 (0.992–0.992) |
| tenga | 0.906 (0.906–0.906) | 0.906 (0.905–0.906) | 0.909 (0.909–0.909) |
| gendun-drub | 0.898 (0.898–0.898) | 0.897 (0.897–0.897) | 0.897 (0.897–0.897) |
| karma-maitri | 0.935 (0.930–0.935) | 0.946 (0.939–0.946) | 0.946 (0.946–0.946) |
| sangye-nyenpa | 0.976 (0.976–0.976) | 0.897 (0.796–0.897) | 0.976 (0.851–0.976) |
| padma-namgyal | 0.971 (0.967–0.975) | 0.971 (0.969–0.975) | 0.970 (0.970–0.973) |
| drakpa | 0.903 (0.896–0.905) | 0.853 (0.843–0.858) | 0.898 (0.890–0.908) |
| **mean** | **0.929** | **0.916** | **0.936** |

## Detail (medians)

| file | setting | composite | boundary F1 | heading F1 | placement | not placed | invalid ops | verse violations | JSON errors | text identical |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| taranatha | Opus 5.5 | 0.850 | 0.817 | 0.893 | 0.828 | 0 | 0 | 0 | 0 | True |
| taranatha | 3.8-flash low | 0.869 | 0.788 | 0.929 | 0.862 | 0 | 0 | 0 | 0 | True |
| taranatha | 3.8-flash high | 0.898 | 0.800 | 0.964 | 0.897 | 0 | 0 | 0 | 0 | True |
| dharmabhadra | Opus 5.5 | 0.994 | 1.000 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| dharmabhadra | 3.8-flash low | 0.990 | 0.984 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| dharmabhadra | 3.8-flash high | 0.992 | 0.995 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| tenga | Opus 5.5 | 0.906 | 0.854 | 0.971 | 0.829 | 0 | 0 | 0 | 0 | True |
| tenga | 3.8-flash low | 0.906 | 0.854 | 0.971 | 0.829 | 0 | 0 | 0 | 0 | True |
| tenga | 3.8-flash high | 0.909 | 0.866 | 0.971 | 0.829 | 0 | 0 | 0 | 0 | True |
| gendun-drub | Opus 5.5 | 0.898 | 0.849 | 0.943 | 0.857 | 0 | 0 | 0 | 0 | True |
| gendun-drub | 3.8-flash low | 0.897 | 0.845 | 0.943 | 0.857 | 0 | 0 | 0 | 0 | True |
| gendun-drub | 3.8-flash high | 0.897 | 0.845 | 0.943 | 0.857 | 0 | 0 | 0 | 0 | True |
| karma-maitri | Opus 5.5 | 0.935 | 0.912 | 0.957 | 0.913 | 0 | 0 | 0 | 0 | True |
| karma-maitri | 3.8-flash low | 0.946 | 0.873 | 1.000 | 0.913 | 0 | 0 | 0 | 0 | True |
| karma-maitri | 3.8-flash high | 0.946 | 0.873 | 1.000 | 0.913 | 0 | 0 | 0 | 0 | True |
| sangye-nyenpa | Opus 5.5 | 0.976 | 0.965 | 0.985 | 0.970 | 0 | 0 | 0 | 0 | True |
| sangye-nyenpa | 3.8-flash low | 0.897 | 0.965 | 0.985 | 0.652 | 5 | 0 | 0 | 0 | True |
| sangye-nyenpa | 3.8-flash high | 0.976 | 0.965 | 0.985 | 0.970 | 0 | 0 | 0 | 0 | True |
| padma-namgyal | Opus 5.5 | 0.971 | 0.883 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| padma-namgyal | 3.8-flash low | 0.971 | 0.885 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| padma-namgyal | 3.8-flash high | 0.970 | 0.881 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| drakpa | Opus 5.5 | 0.903 | 0.611 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| drakpa | 3.8-flash low | 0.853 | 0.414 | 1.000 | 1.000 | 0 | 3 | 0 | 0 | True |
| drakpa | 3.8-flash high | 0.898 | 0.592 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |

## Cost and time per run (Gemini)

| file | thinking | calls | input tok | output tok | of which thinking | API seconds | est. cost (USD) |
|---|---|---:|---:|---:|---:|---:|---:|
| taranatha | 3.8-flash low | 8 | 76,136 | 2,815 | 0 | 18 | 0.068 |
| taranatha | 3.8-flash high | 8 | 71,366 | 161,950 | 158,792 | 468 | 0.661 |
| dharmabhadra | 3.8-flash low | 5 | 26,063 | 308 | 158 | 9 | 0.021 |
| dharmabhadra | 3.8-flash high | 5 | 26,063 | 37,088 | 36,909 | 116 | 0.159 |
| tenga | 3.8-flash low | 5 | 50,926 | 265 | 0 | 9 | 0.039 |
| tenga | 3.8-flash high | 5 | 51,380 | 94,817 | 94,496 | 301 | 0.394 |
| gendun-drub | 3.8-flash low | 5 | 26,911 | 1,815 | 1,156 | 15 | 0.027 |
| gendun-drub | 3.8-flash high | 5 | 26,911 | 115,542 | 114,883 | 351 | 0.453 |
| karma-maitri | 3.8-flash low | 4 | 24,358 | 2,040 | 66 | 12 | 0.026 |
| karma-maitri | 3.8-flash high | 4 | 24,379 | 60,363 | 58,647 | 194 | 0.245 |
| sangye-nyenpa | 3.8-flash low | 5 | 48,584 | 5,197 | 0 | 21 | 0.056 |
| sangye-nyenpa | 3.8-flash high | 5 | 48,690 | 70,662 | 66,540 | 212 | 0.301 |
| padma-namgyal | 3.8-flash low | 5 | 42,684 | 1,296 | 0 | 11 | 0.037 |
| padma-namgyal | 3.8-flash high | 5 | 42,210 | 147,245 | 146,050 | 456 | 0.584 |
| drakpa | 3.8-flash low | 4 | 29,885 | 792 | 0 | 7 | 0.025 |
| drakpa | 3.8-flash high | 3 | 27,602 | 135,725 | 134,518 | 412 | 0.530 |

(Text identical = the output's text is exactly the source text. Not placed = headings whose anchor could not be found. Invalid ops / verse violations = model operations the pipeline rejected. Prices: Gemini 3.8 Flash introductory rates; thinking is billed as output.)
