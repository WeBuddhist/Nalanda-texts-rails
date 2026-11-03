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
- Block 2186 — OBJECTION_REPLY_FUSED: འོ་ན་དེའི་འོག་ཏུ་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱ་བ་སྤང་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིར་མདོ་ལ…
- Block 2345 — CONNECTOR_ENDING: གཞན་འདྲི་བ་ལ་དོན་གཞན་བརྗོད་པ་ནི་གཞན་བརྗོད་པའོ། །རྟོག་པ༌[^3534]ཡོད་པ་ལ་དོན་གཞན་གྱ…

--- FLAGGED BLOCKS WITH CONTEXT ---
[Block 2184]
ཁ་ཅིག་ལས་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་འབྱུང་སྟེ། གང་ཞིག་འདིར་བལྟམ་པ༌[^3265]དང་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་དག་བཟུང་བ་ཡིན་གྱི་ཆོ་འཕྲུལ་ཆེན་པོ་དང་ལྷ་ལས་བབས་པ་དག་ནི་མ་ཡིན་ཏེ། དེ་ནི་ཡི་གེ་ཆད་པར་རིག་པར་བྱ་སྟེ། [^3266]ངེས་པ་རྣམས་ལ་ཆོ་ག་འདི་དང་ལྡན་པའི་ཕྱིར་དང་། བལྟམ་པ༌[^3267]དང་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་གནས་གཞན་ལ་ནི་མ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །བསྔོས་པ་ལས་བསྒྱུར་བའི་སྤང་བའོ།། །།

[Block 2185]
ཞག་བདུན་པར་བྱིན་གྱིས་བརླབས་པའི་ཉི་མ་འདས་སོ་ཅོག་དགེ་སློང་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེང་ཕྱིན་ཆད་དུ་ཉི་མ་དང་པོ་འདས་ཏེ་དེང་ཉི་མ་གཉིས་པ་ལགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །གང་དུ་གསོག་འཇོག་གི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བའི་ཕྱིར་འཆང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོག་འཇོག་ཉིད་ཀྱི་རྒྱུ་མཚན་ལ་བརྟགས་པའི་ཕྱིར་ཡོངས་སུ་སྤྱོད་པ་ལ་ལྟུང་བྱེད་འདི་རྣམ་པར་གཞག་པར་བྱས་པའོ། །གང་གི་ཕྱིར་སྤང་བ་ཡོངས་སུ་སྤྱད་པ་ལ་དོན་མེད་པ་གླགས་མེད་པ་ཉིད་དོ། །

[Block 2186 — OBJECTION_REPLY_FUSED]
འོ་ན་དེའི་འོག་ཏུ་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱ་བ་སྤང་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིར་མདོ་ལས་གསུངས་སོ་ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་འདིའི་འཆང་བ་ལ་ཉེ་བར་མཚོན་པ་དོན་གྱིས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །དེ་བཞིན་དུ་ལྟུང་བ་རྒྱས་པར་བཤད་པ་ནི་འདིར་འཆང་བ་ལ་ལྟུང་བ་བརྗོད་པའི་ཕྱིར་དགེ་སློང་ལ་ཚེས་གཅིག་ལ་སྨན་ཞིག་བྱུང་ལ་ཚེས་གཉིས་པ་ལ་ཡང་སྨན་ཕྱི་མ་ཞིག་བྱུང་ན་དགེ་སློང་དེས་ཉི་མ་བདུན་པོ་དེ་ཉིད་ཀྱི་ནང་དུ༌[^3268]སྔ་མ་ཤོས་བྱིན་གྱིས་བརླབ་པར༌[^3269]བྱ་ཞིང་ཕྱི་མ་ཤོས་གཏང་བར༌[^3270]བྱ་བའམ་གཞན་ལ་སྦྱིན་པར་བྱའོ། །ཡང་ན་ཕྱི་མ་ཤོས་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞིང་སྔ་མ་ཤོས་གཏང་བར༌[^3271]བྱ་བའམ་གཞན་ལ་སྦྱིན་པར་བྱའོ། །བྱིན་གྱིས་མི་རློབ་པར་བྱད་དམ་གཏོང་བར་མི་བྱེད་དམ་གཞན་ལ་སྦྱིན་པར་མི་བྱེད་ན་ཉི་མ་བརྒྱད་པའི་སྐྱ་རེངས༌[^3272]ཤར་བ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །ཇི་སྲིད་འཆང་ཞེ་ན། དེའི་ཕྱིར་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཞག་བདུན་པར་བྱིན་གྱིས་བརླབ་པར་བྱས་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2187]
བྱིན་གྱིས་མ་བརླབས་པ༌[^3273]ནི་ཞག་བདུན་ལས་འདས་པར་འཆང་བར་བྱ་བ་ཉིད་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་རུང་བ་ལ༌[^3274]འཆང་བར་བཀག་པ་སྟེ། འཐད་པའི་ངོ་བོར་ནི་མ་ཡིན་ཏེ། དབྱིག་དང་གསེར་ལ་ཡང་དོན་ལ་བརྟེན་ནས་རྗེས་སུ་གནང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2188]
ནམ་གྱི་ཚེ་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྐྱ་རེངས༌[^3275] བརྒྱད་པ་ཤར་ནའོ་ཞེས་བྱ་བ༌[^3276]སྨོས་ཏེ། འདིར་ཚད་ནི་བླངས་པ་ཉིད་ན་འབྱུང་བ་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

──────────────────────────────────────────────────

[Block 2343]
ཅི་ཞིག་བྱས་ན་བསྒོ་བ་རྣ་ལ་གཟོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་བསྒོ་བ་རྣ་ལ་གཟོན་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །བསམ་པ་ཇི་ལྟ་བུས༌[^3530]ཤེ་ན། འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །རྣ་ལ་གཟོན་པར་འདུན་པ་སྟེ་གཞན་དུ་ན༌[^3531]ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པའོ། །ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་གཞན་བརྗོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྒོ་བ་མ་ཡིན་པ་དང་འདྲ་བའི་དོན་གྱི༌[^3532]ཚིག་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བའི་ཕྱིར་འདིར་ཐམས་ཅད་དུ་དགེ་སློང་གིས་བསྒོ་བ་ཐམས་ཅད་དུ་རྣ་ལ་གཟོན་པ་ལ་ཐ་ན་འགྲོ་བ་ཡོངས་སུ་འདྲི་བའི་བདག་ཉིད་ཅན་ལ་དངོས་གཞི་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 2344]
དེ་ལྟར་ཡང་གཞུང་ནི་འདི༌[^3533]རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་གིས་ཇི་ཙམ་དུ་གཞན་འདྲི་བ་ལ་ལན་འདེབས་ན་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2345 — CONNECTOR_ENDING]
གཞན་འདྲི་བ་ལ་དོན་གཞན་བརྗོད་པ་ནི་གཞན་བརྗོད་པའོ། །རྟོག་པ༌[^3534]ཡོད་པ་ལ་དོན་གཞན་གྱིས་ནི་དངོས་ཏེ།

[Block 2346]
དེ་ལྟར་ཡང་གཞུང་ནི་ཞུ་བ་ལས། དབུས་པའི་ཚིག་གིས་མཐའ་འཁོབ་པ་ལ་འམ། མཐའ་འཁོབ་པའི་ཚིག་གིས་དབུས་པ་ལ་མཐའ་གཞན་དང་གཞན༌[^3535]བརྗོད་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2347]
ཅང་མི་སྨྲ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཅང་མི་སྨྲ་བས་དགེ་སློང་གིས་བསྒོས་པ༌[^3536]རྣ་ལ་གཟོན་ལ༌[^3537]ཉེས་བྱས་སོ། །
