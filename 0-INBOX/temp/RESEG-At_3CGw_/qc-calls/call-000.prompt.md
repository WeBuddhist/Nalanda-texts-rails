=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

A deterministic checker has scanned a block-resegmented Tibetan commentary and
produced a list of issues. Your job is to review each flagged block in context,
decide whether it is a real issue or a false positive, and output correction
operations for real issues only.

━━━ ISSUE TYPES ━━━

CONNECTOR_ENDING
  The block ends with a connector particle (དང་། / ཞིང་། / ཅིང་། / ནས། / ལས། /
  སྟེ། / ཏེ།) that grammatically requires continuation. Real issue if the next
  block is the grammatical continuation. False positive if this is a closing verse
  pāda or a deliberate short citation frame.

OBJECTION_REPLY_FUSED
  The block contains both an objection marker (ཅེ་ན། / ཞེ་ན། / སྙམ་ན།) and a reply
  opener (འོ་ན།). These should always be two separate blocks. Almost always a
  real issue.

OVER_LENGTH
  The block exceeds the syllable threshold. Usually NOT wrong: a whole explanation
  unit is legitimately long. Split only if a new node opener (ordinal + title +
  ནི། / ལ་ N།) or the treatment of a new verse is buried mid-block.

SHORT_FRAGMENT
  The block is suspiciously short — may be a stray split artifact that should be
  merged with an adjacent block.

━━━ CORRECTION OPERATIONS ━━━

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>"]}
]

Rules:
- Only output corrections for REAL issues. Skip false positives entirely.
- Block numbers are CONTINUOUS and include heading blocks. Only merge blocks with
  consecutive numbers (N and N+1); never merge across a heading or skip a number.
- "after" must be verbatim from the block and unique within it. To break one long
  block into 3+ units, set "after" to a LIST of substrings in document order.
- Each block number appears in AT MOST ONE operation.
- Heading blocks (lines starting with #) and [VERSE] blocks are NEVER touched.
- If no corrections are needed, output: []
- Output ONLY the JSON array. No commentary, no code fences.

=== USER PROMPT ===
The deterministic checker found the following issues in a Tibetan commentary resegmentation. Review each flagged block in context and output correction operations for real issues only.

--- ISSUES ---
- Block 22 — OVER_LENGTH (261 syllables): དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་དད་པ་རྙེད་པར་དཀའ་ཞེས་པས་གཞི་དད་པ་བསྟན། བྱང་ཆུབ་ཀྱི་སེ…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 20]
གོ་རིམས་ཀྱང་འདི་ལྟར་ཤེས་ཏེ། དང་པོ་གསུམ་ནི་རྒྱུ་བྱ་བ་བྱེད་པའི་རིགས་པ་ཡིན་ལ་བར་མ་གསུམ་ནི་རྐྱེན་ལྟོས་པའི་རིགས་པ་ཡིན་ཞིང་ཐ་མ་ནི་འབྲས་བུ་ཆོས་ཉིད་ཀྱི༌[^16]རིགས་པ་ཡིན་ཏེ། དཔེ་བདུན་ནི་འཐད་པ་སྒྲུབ་པའི༌[^17]རིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 21]
དེ་ལ། སངས་རྒྱས་འབྱུང་བ་རྙེད་པར་དཀའ། །ཞེས་བྱ་བ་ལ་སོགས་པས་རྐྱེན་གཞན་གྱི་འབྱོར་པ་ལྔ་མཚོན་ལ། མིར་གྱུར་པ་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱུ་བདག་ཉིད་ཀྱི་འབྱོར་བ་ལྔ་མཚོན་ནོ། །དལ་འབྱོར་རྙེད་པར་དཀའ་ཞེས་བྱ་བས་རྒྱུ་རྐྱེན་ཚོགས་པའི་དལ་འབྱོར་བཅུ་མཚོན་པ་ཡིན་ནོ། །

[Block 22 — OVER_LENGTH (261 syllables)]
དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་དད་པ་རྙེད་པར་དཀའ་ཞེས་པས་གཞི་དད་པ་བསྟན། བྱང་ཆུབ་ཀྱི་སེམས་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡུལ་སངས་རྒྱས་ལ་དམིགས་པའི་སེམས་བསྐྱེད་པ་བསྟན། སེམས་ཅན་ཐམས་ཅད་ལ་སྙིང་རྗེ་ཆེན་པོ་སྐྱེ་བར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་སེམས་ཅན་ལ་དམིགས་པའི་སེམས་བསྐྱེད་པ་བསྟན། བྱང་ཆུབ་སེམས་དཔའ་ལ་རྨ་འབྱིན་པ་ཞེས་བྱ་བ་ནས་བར་དུ་གཅོད་པའི་ཆོས་སྤོང་བ་རྙེད་པར་དཀའ་ཞེས་བྱ་བའི་བར་གྱིས༌[^18]རྐྱེན་བར་ཆད་བསལ་བའི་མདོ་བསྟན། ཁྱིམ་པར་གྱུར་ཀྱང་ཆོས་རྣམས་ལ་ནན་ཏན་གྱིས་གཅེས་པར་བསྒྲུབ་པ་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྒྲུབ་པ༌[^19]ནན་ཏན་སྙིང་པོར་བྱེད་པའི་མདོ་བསྟན། མྱ་ངན་ལས་འདས་པ་ལ་མོས་པའི་སེམས་ཅན་རྙེད་པར་དཀའ་ཞེས་པ་ནས་ཐེག་པ་གཅིག་ལ་མོས་པའི་སེམས་ཅན་རྙེད་དཀའ་ཞེས་བྱ་བའི་བར་གྱིས་བློ་ཐེག་པ་གཅིག་ལ་སྦྱང་བའི་མདོ་བསྟན། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་ཆེ་བ་ཉིད་རྒྱ་ཆེན་པོ་ལ་འཇུག་པའི་སེམས་ཅན་ནི༌[^20]རྙེད་པར་དཀའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ལམ་ཆེ་བའི་ཡོན་ཏན་གྱིས་བགྲོད་པའི་མདོ་བསྟན། དེ་ལྟར་རིགས་པ་བཞིས་མདོར་བསྟན། ལུང་གི་མདོ་བདུན་གྱིས་རྒྱས་པར་བཤད་པའི་དོན་དེ་བློ་ལ་གོ་བར་བྱས་ནས་ཉམས་སུ་བླངས་པས་ན་སེམས་བསྐྱེད་པའི་རིགས་བཞི་སྐྱེ་སྟེ། དང་པོ་གཡོ་སྨོན་གྱི་ཚུལ་དང་། འཇུག་ཅིང་བསྟན་པ་དང་གནས་པ་དང་མཐར་ཕྱིན་པའི་རིམ་པའོ། །

[Block 23]
དེ་ཡང་དང་པོ་ས་བོན་དང་ཟླ་གྲངས༌[^21]དང་། ཡོན་ཏན་མཐོང་ཐོས་དང་། བྱིན་རླབས་ཀྱི་སྲུང༌[^22]མ་རྣམས་ཀྱིས་རྩྭ་མེ༌[^23]བཞིན་དུ་སྐྱེ་བོ༌[^24]དེའི་གཞིའི༌[^25]སྟེང་དུ་སྙིང་རྗེ་དང་ལྡན་པ་ལ་གོམས་པས་ཟླ་བ་ཡར་ངོ་བཞིན་དུ་འཕེལ་བའི་ཚེ་དབང་དང་ཡོ་བྱད་ལ་སོགས་པ་འཇུག་ཅིང་བསྟན་པའི་ཡན་ལག་ཏུ་འགྱུར་རོ། །

[Block 24]
དེ་ནས་གནས་པ་གསུམ་གྱི་མཐུ་རྫོགས་པར་བྱེད་པ་ཁ་ཅིག་འཕགས་པ་རྟོགས་པ་ཆེན་པོ་ཡོངས་སུ་རྒྱས་པའི་མདོ་ལས་འགྱོད་ཚངས་ཀྱིས་སྡིག་པ་སྦྱང་སྟེ།[^26] མཆོད་བསྟོད་དང་། སྐྱབས་སུ་གསོལ་བ་དང་། དབང་གཟུགས་པ་དང་། དངོས་པོ་བཤགས་པ་དང་། དམ་བཅའ་ཞིང་སྡོམ་པ་གཟུང་བ་དང་། ཁྲུས་བྱ་བ་དང་། ཚངས་པ་ཐོབ་པ་དང་། རྗེས་སུ་སྤྲོ་བ་དང་། གཟེངས་བསྟོད་པའི་ཚུལ་གྱིས་གདམས་པ་དང་། དམིགས་པ་མེད་ཅིང་ཐེག་པ་གཅིག་ཏུ་བློ་སྦྱང་བ༌[^27]དང་། དག་པའི་མཚན་མ་མཐོང་བ་དང་། མིང་གདགས་པ་དང་། ལམ་རྒྱུད་ལ་བསྐྱེད་པ་དང་། འབྲས་བུ་ཐོབ་པའི་བར་དུ་བྱེད་དོ། །
