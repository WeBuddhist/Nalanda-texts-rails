---
source: Gu_3CFQ
skill: block-resegmentation
stage: qc
date: 2026-10-06
model: gemini-3.8-flash
repaired: true
flags_before: 5
flags_after: 3
blocks_before: 154
blocks_after: 152
---

# Block QC Report — Gu_3CFQ

## Flags found  (before repair)

- Block 41 — **CONNECTOR_ENDING**  `སྡུག་བསྔལ་བ༌[^41]རྣམས་ཀྱི་གྲོགས་སུ༌[^42]དོན་གྱི་མདོ་ནི་སྡུག་བསྔལ་བ་རྣམ་པ་གཉིས་ཏེ། ལུས་ཀྱི་ལས་དང་སེམས་ཀྱིའོ། །ལུས་ཀྱི་ཡང་…`
- Block 72 — **SHORT_FRAGMENT** (2 syllables)  `ཅེས་བྱའོ། །`
- Block 94 — **CONNECTOR_ENDING**  `ཕམ་པའི་གནས་ལྟ་བུའི་ཆོས་བཞི་ཞེས་བྱ་བ་འདིས་ཅི་བསྟན་ཞེ་ན། འདི་ལ་གནས་པས་ན་གནས་ཞེས་བྱ་སྟེ།`
- Block 131 — **CONNECTOR_ENDING**  `དགེ་སྦྱོང་གི་རྒྱན་ནི་འདི་དག་ཡིན་ཏེ།`
- Block 154 — **OVER_LENGTH** (744 syllables)  `[^1]: ཕན་པ་ ༼སྣར། པེ།༽ ཕན་ [^2]: སྙིང་བརྩེ་བ་ ༼སྣར། པེ།༽ སྙིང་བརྩེ་ [^3]: གཉེར་བ་དང་དོན་དང་ལྡན་ ༼སྣར། པེ།༽ གཉེར་བ་དངལྡན་…`

## Corrections applied

- **MERGE** blocks [41, 42]
- **MERGE** blocks [94, 95]

## Flags remaining after repair

- Block 71 — **SHORT_FRAGMENT** (2 syllables)  `ཅེས་བྱའོ། །`
- Block 129 — **CONNECTOR_ENDING**  `དགེ་སྦྱོང་གི་རྒྱན་ནི་འདི་དག་ཡིན་ཏེ།`
- Block 152 — **OVER_LENGTH** (744 syllables)  `[^1]: ཕན་པ་ ༼སྣར། པེ།༽ ཕན་ [^2]: སྙིང་བརྩེ་བ་ ༼སྣར། པེ།༽ སྙིང་བརྩེ་ [^3]: གཉེར་བ་དང་དོན་དང་ལྡན་ ༼སྣར། པེ།༽ གཉེར་བ་དངལྡན་…`
