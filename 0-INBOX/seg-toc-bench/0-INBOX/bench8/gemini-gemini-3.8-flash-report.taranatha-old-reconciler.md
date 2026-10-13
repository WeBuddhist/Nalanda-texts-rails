# Gemini benchmark — gemini-3.8-flash, thinking low vs high, 3 runs per setting

Baseline: Opus 5.5 runs `o2-r1..r3` (same prompts, same scoring).
Composite = mean of boundary F1, heading F1, placement × recall, ID × recall. Median over runs (min–max).

| file | Opus 5.5 | Gemini 3.8-flash low | Gemini 3.8-flash high |
|---|---|---|---|
| taranatha | 0.850 (0.849–0.851) | 0.863 (0.820–0.865) | 0.892 (0.889–0.894) |
| **mean** | **0.850** | **0.863** | **0.892** |

## Detail (medians)

| file | setting | composite | boundary F1 | heading F1 | placement | not placed | invalid ops | verse violations | JSON errors | text identical |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| taranatha | Opus 5.5 | 0.850 | 0.817 | 0.893 | 0.828 | 0 | 0 | 0 | 0 | True |
| taranatha | 3.8-flash low | 0.863 | 0.766 | 0.929 | 0.862 | 0 | 3 | 0 | 0 | True |
| taranatha | 3.8-flash high | 0.892 | 0.775 | 0.964 | 0.897 | 0 | 3 | 0 | 0 | True |

## Cost and time per run (Gemini)

| file | thinking | calls | input tok | output tok | of which thinking | API seconds | est. cost (USD) |
|---|---|---:|---:|---:|---:|---:|---:|
| taranatha | 3.8-flash low | 8 | 72,809 | 3,118 | 304 | 19 | 0.066 |
| taranatha | 3.8-flash high | 8 | 69,976 | 159,244 | 156,151 | 459 | 0.650 |

(Text identical = the output's text is exactly the source text. Not placed = headings whose anchor could not be found. Invalid ops / verse violations = model operations the pipeline rejected. Prices: Gemini 3.8 Flash introductory rates; thinking is billed as output.)
