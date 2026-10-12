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
- Block 14 — CONNECTOR_ENDING: དེ་ཡང་མདོ་ལས།…
- Block 26 — CONNECTOR_ENDING: དེ་ཡང་ཤེས་བྱེད་ཡང་དག་པའི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ནས་བདག་བྱིན་གྱིས་བརླབ་པའི་རང་…
- Block 28 — CONNECTOR_ENDING: དེ་ཡང་དབང་པོ་ལྔས་དབང་བྱས་ནས་བསྒོམ་པ་དང་།…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 12]
དེ་ཀྭའི་ཞེས་བོས་ནས་གདམས་པའོ། །གཟུགས་བརྙན་ལ་འཁྲུལ་བར་མ་བྱེད། གཟུགས་བརྙན་གྱི་རང་བཞིན་མི་ཤེས་པར་མ་བྱེད་ཅེས་པའོ། །

[Block 13]
དེ་ལྟར་མདོར་བསྟན་ནས་དཔེ་དོན་གྱི་མཚན་ཉིད་རྒྱས་པར་བསྟན་པའི་ཕྱིར། དྲི་མེད་མཁའ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། [^3]ནམ་མཁའ་དྲི་མ་མེད་པ་དང་། ནོར་བུ་དང་། མེ་ལོང་དག་པ་དང་། བཞིན་གསུམ་འདུས་པ་ལས་གཟུགས་བརྙན་སྣང་བ་དེ་བཞིན་དུ་སེམས་དང་རླུང་དང་ལས་དང་མ་རིག་པ་ལས་བདག་དང་ཁམས་གསུམ་པའི་གཟུགས་བརྙན་སྣང་སྟེ། དེ་ལ་འཁྲུལ་ཏེ་རྟག་པ་དང་ཡང་དག་པར་ཤེས་པ་ནི་སེང་གེ་རང་གི་གྲིབ་མ་ལ་བརྒལ་བས་རྒྱ་མཚོར་ཤི་བ་དང་འདྲ་སྟེ་བླུན་པའོ། །ཡང་བརྡ་མི་ཤེས་པའི་བྱིས་པས་རང་གི་གཟུགས་བརྙན་ལ་འབྲད་པ་དང་འདྲ་སྟེ་བླུན་པའོ། །དེ་བཞིན་དུ་བདག་དང་ཁམས་གསུམ་པ་གཟུགས་བརྙན་ལྟར་སྣང་བ་ལ་བདག་དང་གཞན་དུ་ཅིའི་ཕྱིར་འཁྲུལ་ཏེ་འཁྲུལ་པར་མ་བྱེད་ཅེས་བྱ་བའོ། །

[Block 14 — CONNECTOR_ENDING]
དེ་ཡང་མདོ་ལས།

[Block 15] [VERSE]
ཇི་ལྟར་མེ་ལོང་ངོས་ལ་ནི། །
སྣང་ཡང༌[^4]དེ་ན་ཡོད་མིན་ལྟར། །
དེ་བཞིན་དངོས་རྣམས་ངོ་བོ་ཉིད། །

[Block 16]
ཅེས་པ་དང་། ཡང་།

──────────────────────────────────────────────────

[Block 24]
དེ་ཡང་རང་བཞིན་གྱིས་ཟག་པ་མེད་པའི་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཡིན་པ་ཤེས་པ་མེད་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 25] [HEADING]
#### དེར་ཤེས་པ། ^1-2-3-0

[Block 26 — CONNECTOR_ENDING]
དེ་ཡང་ཤེས་བྱེད་ཡང་དག་པའི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ནས་བདག་བྱིན་གྱིས་བརླབ་པའི་རང་བཞིན་དུ་དཔེ་གསུམ་དང་བཅུ་གཉིས་ཀྱི་སྒོ་ནས་མཚོན་ཅིང་ཤེས་པ་དང་།

[Block 27] [HEADING]
#### དེར་བསྒོམ་པ། ^1-2-4-0

[Block 28]
དེ་ཡང་དབང་པོ་ལྔས་དབང་བྱས་ནས་བསྒོམ་པ་དང་།

──────────────────────────────────────────────────

[Block 26]
དེ་ཡང་ཤེས་བྱེད་ཡང་དག་པའི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ནས་བདག་བྱིན་གྱིས་བརླབ་པའི་རང་བཞིན་དུ་དཔེ་གསུམ་དང་བཅུ་གཉིས་ཀྱི་སྒོ་ནས་མཚོན་ཅིང་ཤེས་པ་དང་།

[Block 27] [HEADING]
#### དེར་བསྒོམ་པ། ^1-2-4-0

[Block 28 — CONNECTOR_ENDING]
དེ་ཡང་དབང་པོ་ལྔས་དབང་བྱས་ནས་བསྒོམ་པ་དང་།

[Block 29] [HEADING]
#### བྱིན་གྱི་རླབས་འབྱུང་བ། ^1-2-5-0

[Block 30]
དེ་ལས་བྱིན་གྱི་རླབས༌[^7]ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟར་སྣང་བ་ངེས་པའི་ཤེས་པ་སྐྱེའོ། །གཞན་ལྷས་སྐྱོང་བ་ལ་སོགས་པ་འཕགས་པའི་ལྷས་བཤད་པ་ལས་ཤེས་པར་བྱའོ། །
