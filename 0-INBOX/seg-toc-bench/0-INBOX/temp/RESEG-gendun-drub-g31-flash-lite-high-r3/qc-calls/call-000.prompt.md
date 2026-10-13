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
- Block 76 — OVER_LENGTH (269 syllables): བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་པ་ནི། གཉིས་གསུམ་བདུན་དུ་མངོན་པར་བརྗོད་ན། ཞེས་…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 74]
གཞན་དོན་ནི། སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ་། །ཞེས་གཞན་གྱི་དོན་དུ་ཡང་གུས་པ་དང་ལྡན་པས་སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ཏེ། སྐུ་སོགས་ཡིད་ལ་དྲན་བཞིན་དུ་བརྗོད་ན་ཕན་ཡོན་གོང་བཞིན་དུ་ཐོབ་ཅེས་པའོ། །

[Block 75] [HEADING]
#### བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་པ། ^2-3-4-0

[Block 76 — OVER_LENGTH (269 syllables)]
བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་པ་ནི། གཉིས་གསུམ་བདུན་དུ་མངོན་པར་བརྗོད་ན། ཞེས་པ། གྲགས་པའི་མཎྜལ་བཞི་མ་ལྟར་ཏེ། དེའི་དོན་ལ་སྙན་ངག་པ་འགའ་ཞིག །གཉིས་སུ་བརྗོད་ན་བུ་འདོད་པས་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། གསུམ་དུ་བརྗོད་ན་ནོར་འདོད་པས་ནི་ནོར་རྣམས་ཉིད་ཐོབ། བདུན་དུ་བརྗོད་ན་འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ་ཞེས་ཟེར། སྤང་ལོས་ནི། གཉིས་གསུམ་ཞེས་པ་ལ། གཉིས་ནི། སྒྲུབ་པ་པོ་རྟེན་གྱི་གང་ཟག་གི་ཁྱད་པར་ཏེ། བློ་ལྡན་གང་གིས་ཞེས་པས། དབང་རྣོན་ཆོས་ཀྱི་རྗེས་འབྲངས་དང་། རབ་དད་ཅེས་པས་དབང་རྟུལ་དད་པའི་རྗེས་འབྲངས་བསྟན་ལ། གསུམ་ཞེས་པས་དུས་ཀྱི་ཁྱད་པར་བསྟན་ཏེ། སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ནས་ཞེས་པ་ནམ་ལངས་ནས་སྲོད་ཐུན་གྱི་བར་རོ། །བདུན་དུ་མངོན་པར་བརྗོད་ན། ཞེས་པ་གྲངས་ཀྱི་ཁྱད་པར་ཏེ། དུས་གསུམ་པོ་དེ་ལ་བདུན་བདུན་ཏེ། བདུན་གསུམ་ཉི་ཤུ་རྩ་གཅིག་བརྗོད་ན། མི་འཇིགས་པ་ཐམས་ཅད་སྟེར་བ་ལ་སོགས་པ་འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། དེ་ཐོབ་པ་ལ་ཡང་བར་ཆད་བྱེད་པར་མ་ནུས་པས། བགེགས་རྣམས་མེད་ཅིང་དེའི་གཉེན་པོ་རེ་རེས་སྤང་བྱ་རེ་རེ་འཇོམས་པར་འགྱུར་ཅེས་གསུངས་སོ། །རིན་པོ་ཆེ་བུ་སྟོན་གྱིས་ནི། གཉིས་ཞེས་བྱ་བ་ཉིན་མཚན་གྱི་ཆ་གཉིས། གསུམ་ཞེས་པ་དེ་རེ་རེ་ལ་ཐུན་གསུམ་གསུམ་སྟེ། ཉིན་མོ་ལ་སྔ་དྲོ། ཉིན་གུང་རྒོངས་ཐུན་གསུམ། མཚན་མོ་ལ་སྲོད་གུང་ཐུན། ཐོ་རངས་ཏེ་ཐུན་དྲུག་པོ་འདི་ལ། བདུན་བདུན་ཏེ་བཞི་བཅུ་རྩ་གཉིས་ཉིན་མཚན་ཕྲུགས་གཅིག་ལ་བརྗོད་ན། ཕན་ཡོན་དེ་རྣམས་འབྱུང་བ་ཡིན་གསུང་།

[Block 77] [HEADING]
## མཇུག་བྱང། ^a-0

[Block 78] [HEADING]
### མཛད་བྱང། ^a-1-0
