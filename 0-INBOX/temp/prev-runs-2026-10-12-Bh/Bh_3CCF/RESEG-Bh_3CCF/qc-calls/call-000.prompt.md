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
- Block 67 — CONNECTOR_ENDING: ཞེས་གསུངས་པ་ལ། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཛྙཱ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་དྲུག་དང་། རིགས་གསུམ…
- Block 252 — CONNECTOR_ENDING: ཡང་དབང་པོ་གཉིས་ཀྱི་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བའི་ཕྱི་རོལ་གྱི་མེ་ལ་ལྷག་མ་ལ་སོགས་པ…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 65]
སྐུ་གསུང་ཐུགས་ཀྱིས༌[^39]མཚན་པ་ཞེས་པ་ནི་སྐུ་རྡོ་རྗེ་རྣམ་པར་སྣང་མཛད་ཀྱིས༌[^40]དཀྱིལ་འཁོར་བ་རྣམས་ལ་ཡང་མཚན་པ་སྟེ། གཙོར་བྱས་པའི་རང་བཞིན་འདིས་ནི་ཐུགས་དང་གསུང་རྣམས་ལ་ཡང་གོ་བར་བྱའོ། །རྡོ་རྗེ་གསུམ་པོ་རྣམ༌[^41]པ༌[^42]རེ་རེ་ལ་ཡང་ནང་ཕན་ཚུན་དུ་ལྡན་པར་གསལ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 66] [VERSE]
རྣམ་པར་སྣང་མཛད་ཐུགས་རྗེ་ཆེ། །
སྐུ་གསུང་ཐུགས་ཀྱི་མཚན་མ་འམ། །

[Block 67 — CONNECTOR_ENDING]
ཞེས་གསུངས་པ་ལ། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཛྙཱ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་དྲུག་དང་། རིགས་གསུམ་དང་།

[Block 68] [VERSE]
མཐར་རིགས་གཅིག་ཏུ་ཐུག་པར་བསྟན་ཏོ། །
བཞི་བཞི་ཡི་ནི་སྦྱོར་བ་ཡིས། །

[Block 69]
ཞེས་པ་ལ་སོགས་པ་ནི་དཀྱིལ་འཁོར་རེ་རེ་ཞིང་ཡང་དཀྱིལ་འཁོར་བཞི་བཞིའི་རང་བཞིན་ཡིན་པ་ལ་བྱའོ། །

──────────────────────────────────────────────────

[Block 250]
པདྨས་བརྒྱན་པ་བྲིས་ལ་ཞེས་བྱ་བ་ནི་པདྨའི་དཀྱིལ་འཁོར་ཟླ་བའི་དབྱིབས་ལྟ་བུར་པདྨའི་ཕྲེང་བས་བརྒྱན་པ་སྟེ། ལྷ་དེ་ཁོ་ན་ཉིད་ཀྱི་ཕྱིར་ལྷའི་བདག་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་དུ་བྱའོ། །

[Block 251]
སྔགས་ལ་མཆོག་ཏུ་གཞོལ་བ་སྟེ་དེས་ནི་ཞེས་བྱ་བ་ནི་འཕགས་པ་དེ་ཁོ་ན་ཉིད་བསྡུས་པ་ལས༌[^124]གསུངས་པའི་ཚུལ་ཤེས་པས་རྣལ་འབྱོར་ཙམ་བསྐྱེད་པ་ཡིན་ཡང་གསང་བ་འདུས་པ་དང༌[^125]མཚུངས་པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 252 — CONNECTOR_ENDING]
ཡང་དབང་པོ་གཉིས་ཀྱི་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བའི་ཕྱི་རོལ་གྱི་མེ་ལ་ལྷག་མ་ལ་སོགས་པའི་སྲེག་རྫས་རྣམས་ཕྱིའི་སྦྱིན་སྲེག་བྱེད་པ་དེ་བཞིན་དུ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བས་ཀྱང་ནང་གི་བདག་ཉིད་ཀྱི་སྦྱོར་བས་ནང་གི་སྦྱིན་སྲེག་བྱ༌[^126]སྟེ།

[Block 253]
དབབ་པའི་རྡོ་རྗེས་ཞེས་བྱ་བ་ནི་འོད་དཔག་མེད་ཀྱི་རང་གི་ངོ་བོས་ཕབ་ལ་གཟུང༌[^127]ངོ་། །འདི་ཡིས་ནི་སྔོན་དུ་བརྗོད་པའི་དབབ་པའི་ཆོ་ག་གསལ་བར་བྱེད་དོ། །

[Block 254]
དབབ་པ་བྱས་ནས་མི་བསྐྱོད་པ་ལ་སོགས་པས་བསྒྲུབ་བྱའི་ལུས་དང་ངག་དང་ཡིད་ལ་བྱིན་གྱིས་བརླབ་པར༌[^128]མཛད་དོ། །
