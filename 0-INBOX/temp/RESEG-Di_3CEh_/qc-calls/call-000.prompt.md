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
- Block 2 — SHORT_FRAGMENT (1 syllables): ༄༅༅། །…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 1] [HEADING]
## ༄༅། །ཨེ་ཀ་ནཱ་ཐའི་དོན་འགྲེལ།

[Block 2 — SHORT_FRAGMENT (1 syllables)]
༄༅༅། །

[Block 3] [HEADING]
## བསྟོད་པ་དངོས། ^1-0

[Block 4]
སྲིད་པ་གསུམ་གྱི་བླ་མ་གནས་སྐབས་ཀུན་ཏུ་འགྲོ་བ་རྣམས་ལ་ཕན་མཛད་པ། །མཁས་ཤིང་གསལ་བའི་བློ་དང་བསམ་གཏན་མངོན་ཤེས་ཐུགས་བསྒོམ་པ། །སྟོབས་བཅུ་མངའ་བ་རྣལ་འབྱོར་དང་ནི་མཁྱེན་པར་ལྡན་པ་ཁྱོད་འདྲ་ལས་གཞན་པ། །ལྷ་ཡུལ་ས་ལ་ཡོད་མིན་འཇིག་རྟེན་འདིར་མིན་རྣམ་ཐོས་བུ་ཡི་གནས་ནའང་མེད། །ལེགས་སྤྱད་དམ་པ་རྨད་བྱུང་གཅིག་ཏུ་མཛེས་པ་མི་ཡི་མིག་ལ་མཛེས་རྣམས་དང་། །བདེ་བར་གཤེགས་པ་དྲི་མེད་འཇིག་རྟེན་ལས་འདས་དགེ་བའི་གསུང་དང་མཚན་རྣམས་ཀྱིས། །ཉེ་བར་བསགས་པའི་སྐུ་ནི་གཟི་བརྗིད་འཕྲེང་བ་ལྡན་པ་ཁྱོད་དང་མཚུངས་པ་ནི། །ལྷ་ཡི་ཕོ་བྲང་གནས་མཆོག་དག་ནའང་མེད་ལ་ཕྱོགས་དང་ཕྱོགས་མཚམས་དག་ནའང་མེད། །སྙན་ཅིང་མཉེན་ལ་དག་ཅིང་མ་འཁྱུགས༌[^1]གསུང་གིས་མི་དང་ལྷ་རྣམས་ལ། །ཁྱབ་བདག་ཁྱོད་ཀྱིས་དེ་ཉིད་བཤད་པ་བརྩལ་ཏེ་ཁྱོད་དང་མཚུངས་པ་ནི། །མང་དུ་འདི་ཅི་ཐུབ་པ་གང་གིས་རྣམ་དཔྱོད་བཅས་པས་དྭོགས་མེད་པར། །རི་དང་ནགས་སུ་བཅས་པའི་ནོར་འཛིན་ཡངས་པ་ཀུན་ཏུ་རྒྱུས་ཀྱང་རྙེད་མ་ལགས། །ཞི་དང་དུལ་ལ་དགྱེས་ཤིང་ཡང་དག་གསུང་བ་ལྷ་དབང་ཕྱག་བྱས་པ། །རྒྱགས་དང་ཞེ་སྡང་མ་རིག་བྲལ་ཞིང་ཡང་སྲིད་སྤངས་གྱུར་པ། །གདུལ་བྱའི་བསམས་པ་ཇི་བཞིན་འཇམ་ཞིང་ཕན་པའི་གཏམ་གྱིས་དགའ་མཛད་པ། །སྐྱེས་བུ་ཁྱུ་མཆོག་ཁྱོད་དང་འདྲ་བའི་དགེ་སྦྱོང་ཆེན་པོ་གཞན་དག་ག་ལ་ཞིག །
