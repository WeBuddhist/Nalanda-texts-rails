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
- Block 17 — CONNECTOR_ENDING: སྟོན་པ་དང་།…
- Block 19 — SHORT_FRAGMENT (3 syllables): གནས་དང་…
- Block 21 — SHORT_FRAGMENT (2 syllables): འཁོར་རོ། །…
- Block 31 — SHORT_FRAGMENT (3 syllables): ཞེས་གསུངས་སོ། །…
- Block 43 — OBJECTION_REPLY_FUSED: འོ་ན་སྐབས་དེ་ལྟ་བུ་ལ་བརྟེན་ནས་བྱུང་བའི་མདོའི་དབང་དུ་བྱས་པའི་གང་ཟག་ཇི་ལྟ་བུ་ཡིན་ས…
- Block 45 — OBJECTION_REPLY_FUSED: འོ་ན་གླེང་གཞི་དེ་གཉིས་རྒྱུར་བྱས་པ་ལས་རྩོམ་པ་འབྱུང་བའི་མདོ་གང་ཞེ་ན། དྲིས་པ་དང་ལན་…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 15]
ཐུན་མོང་ལ་བཞི་སྟེ། དུས་དང་

[Block 16] [HEADING]
##### སྟོན་པ། ^1-2-1-2-0

[Block 17 — CONNECTOR_ENDING]
སྟོན་པ་དང་།

[Block 18] [HEADING]
##### གནས། ^1-2-1-3-0

[Block 19]
གནས་དང་

──────────────────────────────────────────────────

[Block 17]
སྟོན་པ་དང་།

[Block 18] [HEADING]
##### གནས། ^1-2-1-3-0

[Block 19 — SHORT_FRAGMENT (3 syllables)]
གནས་དང་

[Block 20] [HEADING]
##### འཁོར། ^1-2-1-4-0

[Block 21]
འཁོར་རོ། །

──────────────────────────────────────────────────

[Block 19]
གནས་དང་

[Block 20] [HEADING]
##### འཁོར། ^1-2-1-4-0

[Block 21 — SHORT_FRAGMENT (2 syllables)]
འཁོར་རོ། །

[Block 22] [HEADING]
#### ཁྱད་པར་གྱི་གླེང་གཞི། ^1-2-2-0

[Block 23] [HEADING]
##### གཙོ་བོ་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པ། ^1-2-2-1-0

──────────────────────────────────────────────────

[Block 29] [VERSE]
དད་ལྡན་འཇུག་པའི་ཡན་ལག་ཏུ། །
རང་ཉིད་ཚད་མར་རབ་བསྒྲུབ་ཕྱིར། །
སྟོན་པ་དང་ནི་འཁོར་དབང་པོ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ཡིན། །

[Block 30] [VERSE]
སྡུད་པར་བྱེད་པས་འཇིག་རྟེན་དུ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ནི། །
དཔང་པོར་བཅས་པའི་ཚིག་བརྗོད་ན། །
རང་ཉིད་ཚད་མར་འགྲོ་བ་ཡིན། །

[Block 31 — SHORT_FRAGMENT (3 syllables)]
ཞེས་གསུངས་སོ། །

[Block 32]
འདི་རྣམས་ཀྱི་ཚིག་དོན་དང་ཚིག་རྣམ་པར་སྦྱར་བ་ནི་གསལ་ལོ། །དེས་ན་མདོ་ཐམས་ཅད་དེ་ལྟར་བཤད་པར་བྱ་བ་ཡིན་པར་བརྒྱད་སྟོང་པའི་བསྡུས་དོན་ན༌[^10]བསྟན་ཏོ། །ལྷག་མ་ནི་མཐུན་ནོ། །

[Block 33] [HEADING]
## རང་གི་ལུགས་གསལ་བར་བྱེད་པ། ^2-0

──────────────────────────────────────────────────

[Block 41]
སྐྱོན་གཉིས་པ་དེ་དགོས་པ་དེ་བསྒྲུབ་པར་ནུས་སུ་ཆུག་ཀྱང་དཔང་པོ་ཉིད་དུ་མི་འགྱུར་ཏེ། །དཔང་པོར་འགྱུར་བ་ལ་འདི་དང་འདི་དག་སྟེ་ཞེས་འཁོར་རྣམས་ཀྱི་མིང་བསྟན་པས་དཔང་པོར་འགྱུར་བར་འདོད་ན། རབ་འབྱོར་དང་ཞེས་བྱ་བ་ལ༌[^14]སོགས་པ་དངོས་སུ་མིང་བསྟན་པས༌[^15]དེ་ལྟར་དཔང་དུ་འགྱུར་བ་ལ་རག་ན། མདོ་འདི་བཞིན་དུ་འཁོར་གྱི་མིང་མེད་པ་དང་དཔང་དུ་ཇི་ལྟར་འགྱུར་ཞེས་ཟེར་རོ། །

[Block 42]
དེས་ན་འདི་ལྟར་བཤད་དེ། སྔོན་བྱུང་བའི་གླེང་གཞི་དང་བཅས་པའི་མདོ་བཤད་པའི་སྔོན་རོལ་དུ་དེའི་གླེང་སློང་བར་བྱེད་པ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པའི༌[^16]གསུངས་པ་ཡིན་ནོ། །འདིས་ནི་དབྲི་བསྐྱུངས་མེད་པར་ཡང་དག་པར་ཐོས་པར་བསྟན་ཏེ། དེས་འཁོར་རྣམས་ཀྱིས་ཕྱིན་ཅི་མ་ལོག་པར་བསྟན་པར་ཤེས་པས་སྡུད་པ་པོ་ལ་ལེགས་པར་རྣ་བ་གཏོད་པ་ལ་སོགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །ད་ནི་གང་ལ་བརྟེན་ནས་མདོ་འདི་འབྱུང་བའི་སྐབས་སུ་གྱུར་པའི་གནས་སྐབས་དེ་རྩོམ་པ་སྟེ། དེ་ལ་འཇུག་པར་བྱེད་པ་ནི་དུས་གཅིག་ན་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 43 — OBJECTION_REPLY_FUSED]
འོ་ན་སྐབས་དེ་ལྟ་བུ་ལ་བརྟེན་ནས་བྱུང་བའི་མདོའི་དབང་དུ་བྱས་པའི་གང་ཟག་ཇི་ལྟ་བུ་ཡིན་སྙམ་ནས་བསྟན་པར་གཏོགས་པ་འདུས་པ་སྟེ། དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཆོས་ཉན༌[^17]པའི་སྐལ་པ༌[^18]ཡོད་པ་ཚོགས་པ་དང་ལྡན༌[^19]པར་གཏོགས་པ་འདུས་པ་ཞེས་བྱའོ། །ཁྱད་པར་གྱི་གླེང་གཞི་གང་ཞེ་ན། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཙོ་བོ་དང་འཁོར་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་གཉིས་བསྟན་ཏོ། །

[Block 44] [HEADING]
## མདོ་དངོས། ^3-0

[Block 45]
འོ་ན་གླེང་གཞི་དེ་གཉིས་རྒྱུར་བྱས་པ་ལས་རྩོམ་པ་འབྱུང་བའི་མདོ་གང་ཞེ་ན། དྲིས་པ་དང་ལན་གཉིས་ཀྱིས་སྟོན་པ་ནི་དེ་ནས་ཞེས་བྱ་བ་ནས་དེ་ལྟར་བསླབ་པར་བྱ་བའི་བར་གྱིས་བསྟན་ཏོ། །

──────────────────────────────────────────────────

[Block 43]
འོ་ན་སྐབས་དེ་ལྟ་བུ་ལ་བརྟེན་ནས་བྱུང་བའི་མདོའི་དབང་དུ་བྱས་པའི་གང་ཟག་ཇི་ལྟ་བུ་ཡིན་སྙམ་ནས་བསྟན་པར་གཏོགས་པ་འདུས་པ་སྟེ། དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཆོས་ཉན༌[^17]པའི་སྐལ་པ༌[^18]ཡོད་པ་ཚོགས་པ་དང་ལྡན༌[^19]པར་གཏོགས་པ་འདུས་པ་ཞེས་བྱའོ། །ཁྱད་པར་གྱི་གླེང་གཞི་གང་ཞེ་ན། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཙོ་བོ་དང་འཁོར་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་གཉིས་བསྟན་ཏོ། །

[Block 44] [HEADING]
## མདོ་དངོས། ^3-0

[Block 45 — OBJECTION_REPLY_FUSED]
འོ་ན་གླེང་གཞི་དེ་གཉིས་རྒྱུར་བྱས་པ་ལས་རྩོམ་པ་འབྱུང་བའི་མདོ་གང་ཞེ་ན། དྲིས་པ་དང་ལན་གཉིས་ཀྱིས་སྟོན་པ་ནི་དེ་ནས་ཞེས་བྱ་བ་ནས་དེ་ལྟར་བསླབ་པར་བྱ་བའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 46]
འོ་ན་དེ་དེ་བཞིན་གཤེགས་པས་མ་གསུངས་པར་སྤྱན་རས་གཟིགས་ཀྱིས་བཤད་པ་འདི་ཅང་ཡིན་ནམ་སྙམ་པའི་འཁོར་གྱི་ལོག་རྟོག་བཟློག་པའི་ཕྱིར་ཤཱཀྱ་ཐུབ་པ་ཉིད་ཀྱིས་མཐུན་འགྱུར་བྱིན་པའོ། །

[Block 47]
འོ་ན་འདི་ཡང་སྙིགས་མ་ལྔ་བདོ་བའི་དུས་སུ་སངས་རྒྱས་པས། སངས་རྒྱས་གཞན་པས་འོད་ལ་སོགས་པ་ཆུང་བས་དེ་ཁོ་ན་ལྟར་ཡིན་ནམ་མ་ཡིན་ནམ༌[^20]སྙམ་པ་ལ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱང་རྗེས་སུ་ཡི་རང་ངོ་ཞེས་བྱ་བ༌[^21]དེ་ཁོ་ན་ལྟར་ཟད་དོ་སྙམ་དུ་དགོངས་པའོ། །འདི་གཉིས་ནི་མཐུན་འགྱུར་རོ། །
