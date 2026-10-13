---
source: taranatha-g31-flash-lite-high-r2
skill: block-resegmentation
stage: qc
date: 2026-10-08
model: gemini-2.5-flash
repaired: true
flags_before: 4
flags_after: 4
blocks_before: 127
blocks_after: 126
---

# Block QC Report — taranatha-g31-flash-lite-high-r2

## Flags found  (before repair)

- Block 78 — **OVER_LENGTH** (269 syllables)  `ཚིགས་བཅད་ཉི་ཤུ་པ་ཕྱག་འཚལ་ཉི་མ་སོགས་ལ། ཉི་མ་དང་ཟླ་བ་འོད་ཟེར་རབ་ཏུ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཉིས་པོ་ལ་འོད་ཟེར་འབར་བ་རབ་ཏུ་གསལ་བ…`
- Block 79 — **CONNECTOR_ENDING**  `སྦས་དོན་ནི། ཉི་ཟླའི་བརྡས་ནང་གི་ཁུ་རྡུལ་གཉིས་ཡིན་ལ། དེ་ཡིས་ཡོངས་སུ་གང་བའི་སྤྱན་ནི་དབུ་མའི་སྟེང་འོག་གི་སྔགས་གཉིས་ཡིན་ཞིང་།`
- Block 92 — **CONNECTOR_ENDING**  `འདི་ལྟ་བུའི་རིགས་ནི། སྒྲོན་གསལ་ལས།`
- Block 116 — **CONNECTOR_ENDING**  `གནས་སྐབས་སྔགས་ཀྱི་མཐུས་ཕན་ཡོན་གཞན་ཡང་བསྟན་པའི་ཕྱིར། ཚིགས་བཅད་གསུམ་པ་གསུངས་པ་ལས།`

## Corrections applied

- **MERGE** blocks [102, 103]

## Flags remaining after repair

- Block 78 — **OVER_LENGTH** (269 syllables)  `ཚིགས་བཅད་ཉི་ཤུ་པ་ཕྱག་འཚལ་ཉི་མ་སོགས་ལ། ཉི་མ་དང་ཟླ་བ་འོད་ཟེར་རབ་ཏུ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཉིས་པོ་ལ་འོད་ཟེར་འབར་བ་རབ་ཏུ་གསལ་བ…`
- Block 79 — **CONNECTOR_ENDING**  `སྦས་དོན་ནི། ཉི་ཟླའི་བརྡས་ནང་གི་ཁུ་རྡུལ་གཉིས་ཡིན་ལ། དེ་ཡིས་ཡོངས་སུ་གང་བའི་སྤྱན་ནི་དབུ་མའི་སྟེང་འོག་གི་སྔགས་གཉིས་ཡིན་ཞིང་།`
- Block 92 — **CONNECTOR_ENDING**  `འདི་ལྟ་བུའི་རིགས་ནི། སྒྲོན་གསལ་ལས།`
- Block 115 — **CONNECTOR_ENDING**  `གནས་སྐབས་སྔགས་ཀྱི་མཐུས་ཕན་ཡོན་གཞན་ཡང་བསྟན་པའི་ཕྱིར། ཚིགས་བཅད་གསུམ་པ་གསུངས་པ་ལས།`
