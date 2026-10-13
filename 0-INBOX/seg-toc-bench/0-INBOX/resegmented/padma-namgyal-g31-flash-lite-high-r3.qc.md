---
source: padma-namgyal-g31-flash-lite-high-r3
skill: block-resegmentation
stage: qc
date: 2026-10-08
model: gemini-2.5-flash
repaired: true
flags_before: 3
flags_after: 3
blocks_before: 69
blocks_after: 67
---

# Block QC Report — padma-namgyal-g31-flash-lite-high-r3

## Flags found  (before repair)

- Block 3 — **SHORT_FRAGMENT** (3 syllables)  `ཨོཾ་སྭ་སྟི།`
- Block 9 — **CONNECTOR_ENDING**  `སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་གསོལ། ། ཞེས་མདུན་མཁར་པདྨ་ཟླ་བའི་གདན་གྱི་…`
- Block 53 — **CONNECTOR_ENDING**  `ཡང་ཕྱག་གང་ལ་འཚལ་ན་གོང་གསལ་གྱི་སྔགས་རྣམས་དང་ཁྱད་པར་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་བདུན་པོ་ལ་མགོ་ན་ཨོཾ་དང་མཇུག་ན་སྭཱ་ཧཱ་བཅས་སྔགས་ཀྱི…`

## Corrections applied

- **SPLIT** block 32  after: `དེ་ལྟར་སྦྱར།`
- **MERGE** blocks [43, 44]
- **MERGE** blocks [55, 56]
- **SPLIT** block 63  after: `['ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །', 'ཕྱི་མ་སངས་རྒྱས་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ།']`

## Flags remaining after repair

- Block 3 — **SHORT_FRAGMENT** (3 syllables)  `ཨོཾ་སྭ་སྟི།`
- Block 9 — **CONNECTOR_ENDING**  `སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་གསོལ། ། ཞེས་མདུན་མཁར་པདྨ་ཟླ་བའི་གདན་གྱི་…`
- Block 52 — **CONNECTOR_ENDING**  `ཡང་ཕྱག་གང་ལ་འཚལ་ན་གོང་གསལ་གྱི་སྔགས་རྣམས་དང་ཁྱད་པར་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་བདུན་པོ་ལ་མགོ་ན་ཨོཾ་དང་མཇུག་ན་སྭཱ་ཧཱ་བཅས་སྔགས་ཀྱི…`
