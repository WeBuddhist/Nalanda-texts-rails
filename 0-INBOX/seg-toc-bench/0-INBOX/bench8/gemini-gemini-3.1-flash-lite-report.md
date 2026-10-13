# Gemini benchmark — gemini-3.1-flash-lite, thinking high, 3 runs per setting

Baseline: Opus 5.5 runs `o2-r1..r3` (same prompts, same scoring).
Composite = mean of boundary F1, heading F1, placement × recall, ID × recall. Median over runs (min–max).

| file | Opus 5.5 | Gemini 3.1-flash-lite high |
|---|---|---|
| taranatha | 0.850 (0.849–0.851) | 0.621 (0.596–0.654) |
| dharmabhadra | 0.994 (0.994–0.994) | 0.992 (0.991–0.992) |
| tenga | 0.906 (0.906–0.906) | 0.904 (0.903–0.907) |
| gendun-drub | 0.898 (0.898–0.898) | 0.867 (0.866–0.897) |
| karma-maitri | 0.935 (0.930–0.935) | 0.948 (0.939–0.953) |
| sangye-nyenpa | 0.976 (0.976–0.976) | 0.974 (0.813–0.978) |
| padma-namgyal | 0.971 (0.967–0.975) | 0.872 (0.795–0.971) |
| drakpa | 0.903 (0.896–0.905) | 0.826 (0.746–0.829) |
| **mean** | **0.929** | **0.875** |

## Detail (medians)

| file | setting | composite | boundary F1 | heading F1 | placement | not placed | invalid ops | verse violations | JSON errors | text identical |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| taranatha | Opus 5.5 | 0.850 | 0.817 | 0.893 | 0.828 | 0 | 0 | 0 | 0 | True |
| taranatha | 3.1-flash-lite high | 0.621 | 0.719 | 0.800 | 0.517 | 13 | 0 | 0 | 0 | True |
| dharmabhadra | Opus 5.5 | 0.994 | 1.000 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| dharmabhadra | 3.1-flash-lite high | 0.992 | 0.995 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| tenga | Opus 5.5 | 0.906 | 0.854 | 0.971 | 0.829 | 0 | 0 | 0 | 0 | True |
| tenga | 3.1-flash-lite high | 0.904 | 0.846 | 0.971 | 0.829 | 0 | 0 | 0 | 0 | True |
| gendun-drub | Opus 5.5 | 0.898 | 0.849 | 0.943 | 0.857 | 0 | 0 | 0 | 0 | True |
| gendun-drub | 3.1-flash-lite high | 0.867 | 0.725 | 0.943 | 0.857 | 0 | 7 | 0 | 0 | True |
| karma-maitri | Opus 5.5 | 0.935 | 0.912 | 0.957 | 0.913 | 0 | 0 | 0 | 0 | True |
| karma-maitri | 3.1-flash-lite high | 0.948 | 0.857 | 1.000 | 0.913 | 0 | 0 | 0 | 0 | True |
| sangye-nyenpa | Opus 5.5 | 0.976 | 0.965 | 0.985 | 0.970 | 0 | 0 | 0 | 0 | True |
| sangye-nyenpa | 3.1-flash-lite high | 0.974 | 0.972 | 0.985 | 0.970 | 3 | 0 | 0 | 0 | True |
| padma-namgyal | Opus 5.5 | 0.971 | 0.883 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| padma-namgyal | 3.1-flash-lite high | 0.872 | 0.846 | 1.000 | 0.667 | 1 | 0 | 0 | 0 | True |
| drakpa | Opus 5.5 | 0.903 | 0.611 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |
| drakpa | 3.1-flash-lite high | 0.826 | 0.318 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | True |

## Cost and time per run (Gemini)

| file | thinking | calls | input tok | output tok | of which thinking | API seconds | est. cost (USD) |
|---|---|---:|---:|---:|---:|---:|---:|
| taranatha | 3.1-flash-lite high | 8 | 68,548 | 51,030 | 47,916 | 154 | 0.094 |
| dharmabhadra | 3.1-flash-lite high | 5 | 26,063 | 21,629 | 21,460 | 63 | 0.039 |
| tenga | 3.1-flash-lite high | 5 | 51,439 | 44,677 | 44,413 | 137 | 0.080 |
| gendun-drub | 3.1-flash-lite high | 5 | 23,955 | 39,010 | 38,046 | 117 | 0.065 |
| karma-maitri | 3.1-flash-lite high | 4 | 24,528 | 19,111 | 17,550 | 55 | 0.035 |
| sangye-nyenpa | 3.1-flash-lite high | 6 | 50,024 | 28,425 | 25,387 | 87 | 0.055 |
| padma-namgyal | 3.1-flash-lite high | 4 | 44,547 | 29,109 | 28,492 | 93 | 0.055 |
| drakpa | 3.1-flash-lite high | 3 | 28,414 | 24,777 | 24,111 | 73 | 0.044 |

(Text identical = the output's text is exactly the source text. Not placed = headings whose anchor could not be found. Invalid ops / verse violations = model operations the pipeline rejected. Prices: Gemini 3.8 Flash introductory rates; thinking is billed as output.)
