---
source: padma-namgyal-g31-flash-lite-high-r1
skill: block-resegmentation
stage: qc
date: 2026-10-08
model: gemini-2.5-flash
repaired: true
flags_before: 5
flags_after: 5
blocks_before: 71
blocks_after: 69
---

# Block QC Report — padma-namgyal-g31-flash-lite-high-r1

## Flags found  (before repair)

- Block 3 — **SHORT_FRAGMENT** (3 syllables)  `ཨོཾ་སྭ་སྟི།`
- Block 10 — **CONNECTOR_ENDING**  `སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་གསོལ། ། ཞེས་མདུན་མཁར་པདྨ་ཟླ་བའི་གདན་གྱི་…`
- Block 38 — **OVER_LENGTH** (251 syllables)  `ཕྱག་གང་ལ་འཚལ་ན་མཁྱེན་པས་དད་པ་ཅན་འཇིགས་པ་ཀུན་ལས་སྒྲོལ་མ་དེའང་བསྟོད་པ་པོ་ལ་བརྩེ་བས་ཕྲིན་ལས་སྐད་ཅིག་ཀྱང་མི་འགོར་བས་ཐུགས་རྗེ…`
- Block 58 — **CONNECTOR_ENDING**  `ཡང་ཕྱག་གང་ལ་འཚལ་ན་གོང་གསལ་གྱི་སྔགས་རྣམས་དང་ཁྱད་པར་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་བདུན་པོ་ལ་མགོ་ན་ཨོཾ་དང་མཇུག་ན་སྭཱ་ཧཱ་བཅས་སྔགས་ཀྱི…`
- Block 67 — **OVER_LENGTH** (323 syllables)  `རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་དངོས་ཉམས་དང་རྨི་ལམ་ཅི་རིགས་པར། མྱུར་དུ་རླུང་སེམས་སྣང་སྲིད་ཐམས་ཅད་ལ་དབང་དུ་བསྒྱུར་བའི་དབང…`

## Corrections applied

- **MERGE** blocks [49, 50]
- **MERGE** blocks [61, 62]

## Flags remaining after repair

- Block 3 — **SHORT_FRAGMENT** (3 syllables)  `ཨོཾ་སྭ་སྟི།`
- Block 10 — **CONNECTOR_ENDING**  `སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་གསོལ། ། ཞེས་མདུན་མཁར་པདྨ་ཟླ་བའི་གདན་གྱི་…`
- Block 38 — **OVER_LENGTH** (251 syllables)  `ཕྱག་གང་ལ་འཚལ་ན་མཁྱེན་པས་དད་པ་ཅན་འཇིགས་པ་ཀུན་ལས་སྒྲོལ་མ་དེའང་བསྟོད་པ་པོ་ལ་བརྩེ་བས་ཕྲིན་ལས་སྐད་ཅིག་ཀྱང་མི་འགོར་བས་ཐུགས་རྗེ…`
- Block 57 — **CONNECTOR_ENDING**  `ཡང་ཕྱག་གང་ལ་འཚལ་ན་གོང་གསལ་གྱི་སྔགས་རྣམས་དང་ཁྱད་པར་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་བདུན་པོ་ལ་མགོ་ན་ཨོཾ་དང་མཇུག་ན་སྭཱ་ཧཱ་བཅས་སྔགས་ཀྱི…`
- Block 65 — **OVER_LENGTH** (323 syllables)  `རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་དངོས་ཉམས་དང་རྨི་ལམ་ཅི་རིགས་པར། མྱུར་དུ་རླུང་སེམས་སྣང་སྲིད་ཐམས་ཅད་ལ་དབང་དུ་བསྒྱུར་བའི་དབང…`
