# Block Resegmentation Log — Ar_3CBd_

Original blocks : 169
Result blocks   : 164
Ops applied     : 2
Errors skipped  : 0
Conflicts       : 4

## Applied Operations

**MERGE** blocks [122, 123]
  Block 122: མེའི་ཕྱོགས་སུ་ནི་སྤྱོད་པ་ནག་མོའི་ལྷ་མོ༌[^73]ཁ་དོག་དམར་མོ། །
  Block 123: ཕྱག་ན་ཤཀྟི་བསྣམས་ཤིང་ཀ་རཉྫ་ལ་གནས་པའོ། །

**MERGE** blocks [137, 138, 139, 140, 141]
  Block 137: ཀརྐཌ་དང་རོ་ཧི་ཏ་ནི༌[^77]སྣའི་སྟེང་དུའོ། །
  Block 138: ཆུ་སྲིན་དང་མོ་ཧི༌[^78]ཏ་ནི་སྣའི་འོག་ཏུའོ། །
  Block 139: བི་བཱ་དང་ཙ་བ་ན་དང་། ཀྵུཾ་དང་དུ་བ་དང་མེའོ། །
  Block 140: སེང་གེ་དང་མི་ཀི་རི༌[^79]དང་། ཧཱུཾ་དང་པདྨ་དང་སའོ། །
  Block 141: གཞོན་ནུ་མ་དང་། བི་ཏྲི་དང་། དཀར་མོ་དང་། སུཾ་དང་ཆུའོ། །

## Overlap Disagreements — Boundary Kept

Overlapping windows disagreed whether these blocks belong together; the
boundary was kept. To merge anyway, edit the relevant `window-NNNN.json`
staging file and re-run with `--apply-only`.

Blocks 141 | 142 — windows [3, 4], joined by [3]:
  Block 141: གཞོན་ནུ་མ་དང་། བི་ཏྲི་དང་། དཀར་མོ་དང་། སུཾ་དང་ཆུའོ། །
  Block 142: འདོད་པ་དང་གཞུ་དང་། ཡུཾ་དང་རླུང་སྟེ། དེ་དག་སྣ་བུག་གཡས་པ་ལའོ། །

Blocks 142 | 143 — windows [3, 4], joined by [3]:
  Block 142: འདོད་པ་དང་གཞུ་དང་། ཡུཾ་དང་རླུང་སྟེ། དེ་དག་སྣ་བུག་གཡས་པ་ལའོ། །
  Block 143: གླང་དང༌[^80]ཀུཾ་མ་དང་ཀྵྨྼྻུཾ་དང་རོ་ཙ་ན་དང་མེའོ། །

Blocks 143 | 144 — windows [3, 4], joined by [3]:
  Block 143: གླང་དང༌[^80]ཀུཾ་མ་དང་ཀྵྨྼྻུཾ་དང་རོ་ཙ་ན་དང་མེའོ། །
  Block 144: བུམ་པ་དང་མོ་ཧི་ཏ་དང་། ཧྨྼྻུཾ་དང་དྲི་མེད་གསུམ་དང་སའོ། །

Blocks 144 | 145 — windows [3, 4], joined by [3]:
  Block 144: བུམ་པ་དང་མོ་ཧི་ཏ་དང་། ཧྨྼྻུཾ་དང་དྲི་མེད་གསུམ་དང་སའོ། །
  Block 145: ཉ་དང་བྷ་ཏྲ་དང་སྨྼྻུཾ་དང་ཆུ་དང་སའི་གདུགས་སོ། །
