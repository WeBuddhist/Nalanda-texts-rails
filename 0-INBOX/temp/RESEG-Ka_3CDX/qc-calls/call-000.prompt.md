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
- Block 111 — OVER_LENGTH (267 syllables): རིགས་པ་ཅན་རྣམས་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ཀྱི་མཚན་ཉིད་ནི། འཁྲུལ་པ་དང་བཅས་པ་དང་། …
- Block 128 — OBJECTION_REPLY_FUSED: འོ་ན་ཅི་ཞེ་ན། ངེས་པ་མ་སྐྱེས་པའི་ཕྱིར་རོ། །ཁྱོད་ཀྱིས་སུན་འབྱིན་པ་ལ་ཡང་ཀླན་ཀ་འདི་ཐ…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 109]
འཇིག་རྟེན་རྒྱང་པན་པ༌[^133]རྣམས་ནི་གཞན་དག་ལ་རང་གི་བརྗོད་པར༌[^134]འདོད་པའི་དོན་ལྐོག་ཏུ་གྱུར་པ་ཚིག་རྟགས་དེ་མེད་ན་མི༌[^135]འབྱུང་བའི་སྒོ་ནས་རྗེས་སུ་དཔོག་པར་བྱེད་ཀྱང་། རྗེས་སུ་དཔག་པ་ཚད་མ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རབ་ཏུ་ཤེས་ཏེ། དེའི་ཕྱིར་རང་གི་ཚིག་དང་འགལ་བ་བརྗོད་དོ། །

[Block 110] [HEADING]
### གཏན་ཚིགས་ལྟར་སྣང་བ། ^5-5-0

[Block 111 — OVER_LENGTH (267 syllables)]
རིགས་པ་ཅན་རྣམས་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ཀྱི་མཚན་ཉིད་ནི། འཁྲུལ་པ་དང་བཅས་པ་དང་། འགལ་བ་དང་། སྐབས་དང་། མཚུངས་པ་དང་། བསྒྲུབ་པར་བྱ་བ་དང་། མཚུངས་པ་དང་། དུས་ལས་འདས་པ་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་དག་ཡིན་ནོ་ཞེས་གཞན་དུ་འཆད་པར་བྱེད་དེ། དེ་ལ་འཁྲུལ་པ་དང་བཅས་པ་མ་ངེས་པ་ཡིན་ཏེ། དཔེར་ན་སྒྲ་ནི་རྟག་པ་སྟེ། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །གྲུབ་པའི་མཐའ་ཁས་བླངས་པས་དེ་དང་འགལ་བར་བྱེད་པ་ནི་འགལ་བ་སྟེ། དཔེར་ན་བྱེ་བྲག་ནི༌[^136]རྡུལ་ཕྲ་རབ་དག་ནི་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རྩོམ་པར་བྱེད་པ་མ་ཡིན༌[^137]ཞེས་ཟེར་བ་ལྟ་བུའོ། །གང་གི་ཕྱིར་སྐབས་བསམ་པ༌[^138]དེ་གཏན་ལ་དབབ་པའི་ཕྱིར། བསྟན་པ་ནི་སྐབས་དང་མཚུངས་པ་སྟེ། དཔེར་ན་བདག་ནི་རྟག་པ་སྟེ་ལུས་ལས་གཞན་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །བསྒྲུབ་པར་བྱ་བ་དང་ཁྱད་པར་མེད་པ༌[^139]བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་ཏེ། དཔེར་ན་སྒྲ་ནི་རྟག་པ་སྟེ། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་བློ་ལྟ་བུ་ཞེས་བྱ་བ་ལྟ་བུ༌[^140]དང་། གཞན་དག་ན་རེ་རྫས་ཡིན་ཏེ། ལུས་ལས་འོང་བ་དང་ལྡན་པའི་ཕྱིར་རོ་ཞེས་དཔེར་རྗོད་པར༌[^141]བྱེད་པ་ལྟ་བུའོ། །དུས་འདས་ནས་བསྟན་པ་ནི་དུས་ལས་འདས་པ་སྟེ། དཔེར་ན་སྒྲ་ནི་མི་རྟག་པ་སྟེ་བུམ་པ་བཞིན་ནོ་ཞེས་སྨྲས་ནས་དྲིས་པ་དང་བྱས་པའི་ཕྱིར་རོ་ཞེས་གཏན་ཚིགས་སྨྲས་པ༌[^142]ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 112]
བྱེ་བྲག་པ་རྣམས་ན་རེ་སྟོན་པ་མ་ཡིན་པ་ནི་རབ་ཏུ་མ་གྲུབ་པ་དང་། མེད་པ་དང་། ཐེ་ཚོམ་ཟ་བའོ་ཞེས་ཟེར་ཏེ། གང་ལ་རྟགས་དང་རྟགས་ཅན་དག་འབྲེལ་པར་མ་གྲུབ་པ་དེ་ལ་མ་གྲུབ་པ་ཡིན་ནོ། །འབྲེལ་པ་མེད་པ་ནི་མེད་པ་སྟེ། དཔེར་ན་རྭ་ཅན་ཡིན་པའི་ཕྱིར་རྟའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །རྭ་ཅན་ཡིན་པའི་ཕྱིར་བ་ལང་ངོ་ཞེས་བྱ་བ་ལྟ་བུ་ནི་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 113]
དེ་དག་དགག་པའི་ཕྱིར་དང་གཞན་གྱིས་རབ་ཏུ་སྦྱར་བའི་གཏན་ཚིགས་རྣམས་ཀྱི་མ་གྲུབ་པ་ཉིད་ལ་སོགས་པའི་སྐྱོན་བརྗོད་པའི༌[^143]ཕྱིར་གཏན་ཚིགས་ལྟར་སྣང་བ་དག་བསྟན་ཏོ། །

──────────────────────────────────────────────────

[Block 126]
དེ་ལ་ལྟག་ཆོད༌[^165]རྣམས་ཀྱི་དཔེར་བརྗོད་པ༌[^166]ཕྱོགས་ཙམ་ཞིག་བརྗོད་པར་བྱ་སྟེ། དཔེར་ན་མི་རྟག་པ་ཉིད་ལ་སོགས་པ་ནི༌[^167]བསྒྲུབ་པར་བྱས་པ་ཉིད་དང་བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ལ་སོགས་པ་ཡང་དག་པར་སྦྱར་ཀྱང་ལྟག་ཆོད་སྨྲ་བས་རྒོལ༌[^168]བ་ཁྱོད་ཀྱི་གཏན་ཚིགས་འདི་ཅི་བསྒྲུབ་པར་བྱ་བ་དང་ཕྲད་ནས་སྒྲུབ་པར་བྱེད་དམ་འོན་ཏེ་མ་ཕྲད་ནས། གལ་ཏེ་ཕྲད་ནས་ཡིན་ན་ནི། དེའི་ཚེ་བསྒྲུབ་པར་བྱ་བ་དང་ཁྱད་པར་མེད་པར་འགྱུར་ཏེ། ཀླུང་གི་ཆུ་རྒྱ་མཚོ་དང་ཕྲད་པ་བཞིན་ནོ། །གཞན་ཡང་འདི་བསྒྲུབ་པར་བྱ་བ་གྲུབ་ཟིན་པ་དང་ལྷན་ཅིག་ཕྲད་པར་འགྱུར་རམ། མ་གྲུབ་པ་དང་ཕྲད། རེ་ཞིག་མ་གྲུབ་པ་དང་ནི་མ་ཡིན་ཏེ། རི་བོང་གི་རྭ་བཞིན་མེད་པའི་ཕྱིར་རོ། །བསྒྲུབ་པར་བྱ་བ་གྲུབ་ཟིན་ན་ཡང་འདི་གང་གི་གཏན་ཚིགས་ཡིན་པར་འགྱུར། དེའི་ཕྱིར་ཕྲད་པའི་ཕྱོགས་ནི་རིགས་པ་མ་ཡིན་ནོ། །ཡང་མ་ཕྲད་ཅེས་བྱ་བའི་ཕྱོགས་ཀྱང་མ་ཡིན་ཏེ། གཏན་ཚིགས་མ་ཕྲད་པ་རྣམས་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་ནོ། །འདི་ནི་ཕྲད་པ་དང་མ་ཕྲད་པ་མཚུངས་པ་ཞེས་བྱ་བའི་ལྟག༌[^169]ཆོད་ཡིན་ཏེ། རིགས་པ་མེད་པས་གཏན་ཚིགས་སུན་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 127]
གང་ལ་ཕྲད་པ་དང་མ་ཕྲད་པར༌[^170]ཡོད་པར་ཆོས་མཐུན་པ་ཙམ་གྱིས་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པ་ཡང་གཏན་ཚིགས་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ལ་རིགས་པ་ཅི་ཞིག་ཡོད། ཆུ་དང་འབྱུང་བ་ཉིད་ལ་སོགས་པར་ཆོས་མཐུན་པའི་ཕྱིར་མེས་མི་བསྲེག་པ༌[^171]ནི་མ་ཡིན་ནོ། །བསྒྲུབ་པར་བྱ་བ་ཡང་རི་བོང་གི་རྭ་བཞིན་དུ་ཤིན་ཏུ་མ་གྲུབ་པ་ཉིད༌[^172]མ་ཡིན་ནོ། །

[Block 128 — OBJECTION_REPLY_FUSED]
འོ་ན་ཅི་ཞེ་ན། ངེས་པ་མ་སྐྱེས་པའི་ཕྱིར་རོ། །ཁྱོད་ཀྱིས་སུན་འབྱིན་པ་ལ་ཡང་ཀླན་ཀ་འདི་ཐམས་ཅད་མཚུངས་པས་སུན་འབྱིན་པ་མ་ཡིན་པ་ཉིད་དོ། །དེ་ལྟ་བས་ན་འདྲི་བ་ལོག་པ་དེ་ལྟ་བུ་དག་ལ་མཐའ་མེད་པས།[^173] དེ་དག་གི་མཚན་ཉིད་ལོགས་ཤིག་ཏུ་བརྗོད་པར་མི་བྱ་སྟེ། ཚད་མའི་མཚན་ཉིད་ཇི་སྐད་བཤད་པ་ངེས་པར་གཟུང་བ་ཁོ་ནས་དེ་དག་བསལ་བ༌[^174]ཉིད་དོ་སྙམ་དུ་བསམས་པ༌[^175]ཡིན་ནོ། །

[Block 129] [HEADING]
## མཇུག་བྱང། ^b-0

[Block 130] [HEADING]
### མཛད་བྱང། ^b-1-0
