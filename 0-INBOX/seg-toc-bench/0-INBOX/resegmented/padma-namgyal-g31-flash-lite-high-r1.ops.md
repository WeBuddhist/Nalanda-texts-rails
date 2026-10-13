# Block Resegmentation Log — padma-namgyal-g31-flash-lite-high-r1

Original blocks : 77
Result blocks   : 73
Ops applied     : 6
Errors skipped  : 0
Conflicts       : 1

## Applied Operations

**MERGE** blocks [10, 11]
  Block 10: སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་…
  Block 11: ཚོགས་བསགས་དངོས་ལ་ཡན་ལག་བདུན་ལས།

**MERGE** blocks [28, 29]
  Block 28: སེམས་ཅན་རྣམས་ཀྱི་བསམ་པ་དང་། ། བློ་ཡི་བྱེ་བྲག་ཇི་ལྟ་བར། །
  Block 29: <small>ཐེག་པ་</small>ཆེ<small>ན་པོ་བྱང་སེམས་ཀྱི་ཐེག་པ་མདོ་སྔགས་གཉིས་དང་</small>ཆ…

**MERGE** blocks [35, 36]
  Block 35: གཉིས་པ་སྒྲོལ་མའི་རྒྱུད་ལས་ཁོལ་དུ་ཕྱུང་བའི་བསྟོད་པའི་ཚིག་བྱིན་རླབས་ཀྱི་སྤྲིན་ཆར་ག…
  Block 36: དང་པོ་མཚན་རྒྱ་གར་སཾ་སྐྲྀ་ཏའི་སྐད་དུ་སྨོས་ན། ན་མཿཏཱ་ར་ཨེ་ཀ་བིམ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ་ཧ…

**MERGE** blocks [40, 41]
  Block 40: ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་ཡུམ་མཆོག་ཏུ་གྱུར་པས་རྗེ་བཙུན་མ་སོ་སོའི་སྐྱེ་བོའ…
  Block 41: འདི་ནི་དཔལ་ལྡན་ཇོ་བོ་རྗེ་སོགས་ཀྱིས་རྒྱུད་གཞན་ནས་ཁ་སབ་པར་གྲགས་པ་སྒྲོལ་མ་བསྡུས་པའི…

**SPLIT** block 68  after: `བཤད་པ་ཡིན་ལ།`
  Block 68: དེ་ལྟར་སྒྲོལ་མ་ཉེར་གཅིག་ལ་དོན་དེ་ལྟ་བུའི་རྩ་བའི་སྔགས་ཡི་གེ་བཅུ་པ་ཉིད་ཀྱི་སྒོ་ནས་…

**MERGE** blocks [69, 70]
  Block 69: རྒྱུད་འདིའི་བསྟན་དོན་རྒྱས་ན། སྒྲོལ་མ་ཉིན་ཞི་མཚན་ཁྲོའི་སྒྲུབ་ཐབས་དང་། སྒྲུབ་ཐབས་ཉ…
  Block 70: དེས་དངོས་གཞི་བསྟོད་པའི་དོན་སོང༌།

## Overlap Disagreements — Boundary Kept

Overlapping windows disagreed whether these blocks belong together; the
boundary was kept. To merge anyway, edit the relevant `window-NNNN.json`
staging file and re-run with `--apply-only`.

Blocks 72 | 73 — windows [1, 2], joined by [2]:
  Block 72: གསུམ་པ་མཇུག་ཕན་ཡོན་གྱི་དོན་ནི། བསྟོད་ཡུལ་ལྷ་མོ་ལ་བསྟོད་པ་པོ་གུས་པ་ཡང་དག་ལྡན་པའི།…
  Block 73: རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་དངོས་ཉམས་དང་རྨི་ལམ་ཅི་རིགས་པར། མྱུར་དུ་རླུང་སེམས…
