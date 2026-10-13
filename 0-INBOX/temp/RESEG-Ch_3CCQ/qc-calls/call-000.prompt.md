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
- Block 5 — CONNECTOR_ENDING: དབང་པོ་རྣམས་དང་དབང་པོ་རྣམས་ཀྱི་ཡུལ་གཉི་གའི་དབང་པོ་སྟེ། དབང་པོ་བཅུ་པོ་ཡུལ་དང་ཡུལ་…
- Block 19 — CONNECTOR_ENDING: རང་གི་གཟུགས་ལ་སོགས་པའོ། །དབང་པོ་ནི་མིག་ལ་སོགས་པ་སྟེ། དེ་ལ་དབང་པོ་གཉིས་དགག་ཅིང་ངེ…
- Block 24 — CONNECTOR_ENDING: དེ་ཡང་ཇི་སྐད་དུ་ལས་ཀྱི་མཐའ་རྣམ་པར་འབྱེད་པ་ལས།…
- Block 33 — CONNECTOR_ENDING: དཔལ་སྒྱུ་འཕྲུལ་དྲ་བ་ལས་ཀྱང་ལྷ་བསྐྱེད་པའི་དབྱེ་བ་འདི་ཉིད་གསལ་བར་གསུངས་ཏེ།…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཥཊ་ཨཾ་ག་ཡོ་ག་ནཱ་མ་ཊཱི་ཀ །བོད་སྐད་དུ། སྦྱོར་བ་ཡན་ལག་དྲུག་པ་ཞེས་བྱ་བའི་འགྲེལ་པ། དཔལ་རྡོ་རྗེ་སེམས་དཔའ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4] [HEADING]
## སོ་སོར་སྡུད་པ། ^1-0

[Block 5 — CONNECTOR_ENDING]
དབང་པོ་རྣམས་དང་དབང་པོ་རྣམས་ཀྱི་ཡུལ་གཉི་གའི་དབང་པོ་སྟེ། དབང་པོ་བཅུ་པོ་ཡུལ་དང་ཡུལ་ཅན་དེ༌[^1]རྣམས་ཀྱི་རང་གི་འཇུག་པ་ནི། ཇི་ལྟར་རང་ཉིད་ཀྱི་གཟུང་བ་དང་། འཛིན་པའི་རང་བཞིན་གྱིས་འཇུག་པ་ནི་རང་གི་འཇུག་པའོ། །དེར་གནས་པས་ན༌[^2]རང་གི་འཇུག་པ༌[^3]གནས་སོ། །ཐམས་ཅད་དུ་དམན་པ་དང་། བར་མ་དང་།

[Block 6] [VERSE]
མཆོག་གི་བྱེ་བྲག་གིས་སོ། །
འདོད་པ་སོ་སོར་སྡུད་པས་ན། །

[Block 7]
ཞེས་བྱ་བ་ནི་འདོད་ཅིང་ཆགས་པར་བྱ་བ་ཡིན་པས་ན། འདོད་པ་སྟེ་གཟུགས་ལ་སོགས་པའོ། །དེ་རྣམས་ལ་ནི་དབང་པོ་རྣམས་ཀྱིས་གང་སོ་སོར་ཡང་དང་ཡང་དུ་སྡུད་ཅིང་ལེན་པས་ན༌[^4]སྡུད་པ་ཞེས་བྱ་སྟེ། ཡན་ལག་དང་པོའི་བཤད་པའོ། །

──────────────────────────────────────────────────

[Block 17]
རང་སྔགས་སྙིང་གར་བསམས༌[^12]ཏེ། རང་གི་སྙིང་གར་བསམས་ཏེ། རང་གི་སྙིང་གའི་པདྨ་ལ་བསམས་ནས། སྲོག་ནི་ཐིག་ལེར་གྱུར་པར་བཞག །ཅེས་བྱ་བ་མི་ཤིགས་པ༌[^13]གཏོགས་པར་དགོད་པ་སྟེ་ཡན་ལག་གསུམ་པའོ། །

[Block 18] [HEADING]
## འཛིན་པ། ^4-0

[Block 19 — CONNECTOR_ENDING]
རང་གི་གཟུགས་ལ་སོགས་པའོ། །དབང་པོ་ནི་མིག་ལ་སོགས་པ་སྟེ། དེ་ལ་དབང་པོ་གཉིས་དགག་ཅིང་ངེས་པར་ཐིམ་ནས་དེའི་འོག་ཏུ་ཡུལ་དང་དབང་པོའི་རྟེན་དུ་གྱུར་པའི་རིན་པོ་ཆེ་སྟེ། སེམས་ཀྱི་རིན་པོ་ཆེ་སྲོག་དང་རྩོལ་བ་དང་བཅས་པར་བཀག་ཅིང་ནུབ་པར་གྱུར་པའི་གཟུང་བ་གང་ཡིན་པ་དེ་འཛིན་པ་ཡིན༌[^14]པར་བཤད་དེ། དེ་ཡང་གང་ཞེ་ན། ཡང་དག་པའི་མཐའ་ཞེས་བྱ་བ་སྟེ།

[Block 20] [VERSE]
སེམས་ནི་འགོག་པའི་རྡོ་རྗེར་འགྱུར། །
མཚན་མ༌[^15]ཉེར་འཛིན་འབྱུང་བར་འགྱུར། །

[Block 21]
ཞེས་བྱ་བ་ལ། འགོག་པའི་རྡོ་རྗེ་ནི་འོད་གསལ་བའོ། །དེར་གྱུར་པ་ནི་སེམས་དེར་གྱུར་པའོ། །མཚན་མ་རྣམས་ཀྱི་ཉེ་བར་འཛིན་པ་ན༌[^16]མཚན་མར་ཉེར་འཛིན་ཏེ། མཚན་མར་སྣང་བའོ། །འབྱུང་བར་གྱུར་པ་ནི་སྐྱེ་བར་གྱུར་པའོ། །

──────────────────────────────────────────────────

[Block 22] [VERSE]
མཚན་མའི་ཁམས་ནི་རྣམ་པ་ལྔར། །
བྱང་ཆུབ་རྡོ་རྗེ༌[^17]གསུངས་པ་ཡིན། །

[Block 23]
ཞེས་བྱ་བ་ནི་ས་ཆུ་ལ་ཐིམ་པར་གྱུར་པ་ལས་སྨིག་རྒྱུ་དང་འདྲ་བར་སྣང་བར་གྱུར་པ་ནི་མཚན་མ་དང་པོའོ། །དེ་བཞིན་དུ་ཆུ་མེ་ལ་ཐིམ་པར་གྱུར་པ་ལས་དུ་བ་ལྟ་བུ་སྟེ་གཉིས་པའོ། །མེ་རླུང་ལ་ཐིམ་པར་གྱུར་པ་ལས། ནམ་མཁའ་སྣང་བར་གྱུར་པ༌[^18]ལྟ་བུ་སྟེ་གསུམ་པའོ། །ཁམས་ཕྲ་བ་ཀུན་དུ་སྣང་བ་གསུམ་དུ་སོང་བ་ལས་མར་མེ་ལྟར་སྣང་བའི་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་ནི་བཞི་པའོ། །རང་བཞིན་ཀུན་དུ་སྣང་བ་ལ་ཐིམ་པར་གྱུར་པ་ལས་སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་ཞིང་རྟག་ཏུ་སྣང་བ་འོད་གསལ་བ་ཙམ་དུ་གྱུར་པ་ནི་ལྔ་པའོ། །མཚན་མ༌[^19]ལྔ་པོ་དེ་དག་གིས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 24 — CONNECTOR_ENDING]
དེ་ཡང་ཇི་སྐད་དུ་ལས་ཀྱི་མཐའ་རྣམ་པར་འབྱེད་པ་ལས།

[Block 25] [VERSE]
དང་པོ་ས་ནི་ཆུ་ལ་ཐིམ། །
ཆུ་ཡང་མེ་ལ་ཐིམ་པར་གྱུར། །
མེ་ནི་རླུང་ལ་ཐིམ་འགྱུར་ཞིང་། །
རླུང་ཡང་རྣམ་པར་ཤེས་ལ་འཇུག །

[Block 26] [VERSE]
རྣམ་ཤེས་གཟུང་བ་དེ་ཉིད་ནི། །
འོད་གསལ་པར་ཡང་འཇུག་པ་ཡིན། །

──────────────────────────────────────────────────

[Block 31] [HEADING]
## ཏིང་ངེ་འཛིན། ^6-0

[Block 32]
ཐབས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་འཇུག་པ་སྟེ། ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པའི་སྦྱོར་བས་དངོས་པོ་ཐམས་ཅད་དེ་རྒྱུ་བ་དང་། མི་རྒྱུ་བ་ལ༌[^26]གནས་པ་གོང་བུའི་ཚུལ་གྱིས་ཏེ། ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་ཀྱིས་གཅིག་ཏུ་བྱས་ནས་རྒྱུ་བ་དང་། མི་རྒྱུ་བ་དེའི་དབུས་སུ་ཟུང་དུ་འཇུག་པའི་བདག་ཉིད་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་རྣམ་པར་བསྒོམ་པར༌[^27]བྱའོ། །རིམ་པ་འདི་ཉིད་ཀྱིས༌[^28]ཡུད་ཀྱི༌[^29]ཞེས་པ་སྟེ། སྐད་ཅིག་ཙམ་གྱིས་སོ། །ཡེ་ཤེས་རྫོགས་པར་བྱེད་པ་ཞེས་པ་སྟེ། ཡེ་ཤེས་ཀྱི་སྐུ་རྫོགས་པར་བྱེད་པ་ནི་ཏིང་ངེ་འཛིན་ཏེ། ཡན་ལག་དྲུག་པ་ཡིན་པར་བཤད་དོ། །

[Block 33 — CONNECTOR_ENDING]
དཔལ་སྒྱུ་འཕྲུལ་དྲ་བ་ལས་ཀྱང་ལྷ་བསྐྱེད་པའི་དབྱེ་བ་འདི་ཉིད་གསལ་བར་གསུངས་ཏེ།

[Block 34] [VERSE]
རྣལ་འབྱོར་རྣམ་གསུམ་ཤེས་བྱ་སྟེ། །
བྱིན་གྱིས་བརླབས་དང་ཡོངས་བརྟག༌[^30]དང་། །
གཟུགས་ཉིད་ཡོངས་སུ་རྫོགས་པ་སྟེ། །
རྣལ་འབྱོར་སངས་རྒྱས་རྣམས་ཀྱི་བསྔགས། །

[Block 35] [VERSE]
སྔགས་ཀྱིས་བྱིན་བརླབས་ང་རྒྱལ་བསྐྱེད། །
རྣལ་འབྱོར་བྱིན་རླབས༌[^31]ཡིན་པར་གསུངས། །
བྱང་ཆུབ་སེམས་ནི་དག་པ་དང་། །
གསང་སྔགས་ས་བོན་སྐྱེ་བ་ཆེ། །
