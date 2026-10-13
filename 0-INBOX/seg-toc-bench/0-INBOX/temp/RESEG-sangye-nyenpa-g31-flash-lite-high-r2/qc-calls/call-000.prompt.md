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
- Block 6 — SHORT_FRAGMENT (2 syllables): དང་པོ།…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 4]
ཞེས་མཆོད་པར་བརྗོད་པར་སྔོན་དུ་སོང་ནས། འཆད་བྱའི་གཞུང་ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་ཚིག་འགྲེལ་དང་། དེ་དག་གི་དམིགས་རིམ་བཅས། དེང་དུས་ཀྱི་ལེ་ལོ་དང་རྣམ་གཡེང་ཅན་རྣམས་ཀྱི་ཁམས་དང་འཚམས་པར་ཉུང་ངུའི་ངག་གིས་འགྲེལ་བ་ལ།

[Block 5] [HEADING]
## ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ། ^II-0

[Block 6 — SHORT_FRAGMENT (2 syllables)]
དང་པོ།

[Block 7] [HEADING]
## བསྟོད་པ་དངོས། ^1-0

[Block 8] [HEADING]
### ཕྱག་འཚལ་བ། ^1-1-0
