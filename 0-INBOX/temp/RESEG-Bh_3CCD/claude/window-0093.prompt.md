=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 3256]
དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི༌[^2090]འདོད་པའི་དབང་ཕྱུག་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་ལྷ་མོ་དགུའི་བདག་ཉིད་གཟུངས་ཀྱི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 3257]
སེམས་གཙོ་བོ་ནི་ངག་དང་ལུས་ཀྱི་ནང་ནས་སེམས་ཁོ་ན་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3258]
མི་བསྐྱོད་པའི་བསྡུས་པའི་དཀྱིལ་འཁོར་སྤྲུལ་པའི་བྱ་བ་ཞེས་པ་ནི༌[^2091]རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་རྗེས་སུ་ཞུགས་པས་བསྐྱེད་པའི༌[^2092]ཐུགས་ཀྱི་རྡོ་རྗེའི་གཞི་དང་། གཞི་ཅན་གྱི་མཚན་ཉིད་ཀྱི་དཀྱིལ་འཁོར་གྱི་སྤྲུལ་པ་མཛད་ཅེས་ཐ་ཚིག་གོ། །

[Block 3259]
སྔ་མ་བཞིན་ཏེ་ཤེས་རབ་ཀྱི་གནས། །ཞེས་པ་ནི་བགེགས་བསྐྲད་པ་དང་སྟོང་པ་ཉིད་བསྒོམ་པའི་རྗེས་སུ་ཧཱུཾ་ལས་བྱུང་བའི་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱ་ལའོ། །

[Block 3260]
དེར་ཆུད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡེ་ཤེས་ཀྱི་ས་གཞི་དང་རི་རབ་ལ་སོགས་པ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་གྲུ་བཞི་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་གཞིའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3261]
དམ་ཚིག་ཆེན་པོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔའོ། །

[Block 3262]
དེ་གང་དུ་འདུས་པ་དེ་དམ་ཚིག་ཆེན་པོ་སྟེ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁོ་ནའོ། །

[Block 3263]
དྲི་མ་ཐམས་ཅད་དང་བྲལ་བ་ལས་ཞེས་པ་ནི་འདོད་ཆགས་ཀྱི་ཉོན་མོངས་པའི་དྲི་མས་མ་གོས་པའོ། །

[Block 3264]
སྤྲུལ་པར་མཛོད་ཅེས་པ་ནི་བསྐྱེད་པའི་རིམ་པས་སྤྲུལ་ཏོ་ཞེས་ཐ་ཚིག་གོ། །

[Block 3265]
གཞལ་ཡས་ཁང་པའི་ཕྱི་རོལ་ན། །ཞེས་བྱ་བ་ལ་སོགས་པས་ཤིན་ཏུ་དང་བ་ཉིད་བསྟན་ཏོ། །

[Block 3266]
ཨིནྡྲ་ནཱི་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་རིན་པོ་ཆེའི་ཁ་དོག་ལྔ་བསྟན་ཏོ། །

[Block 3267]
ཕྱུང་བའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བ་ལ་སོགས་པས་དེའི་ནང་དུ་སྣ་ཚོགས་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་དཀྱིལ་འཁོར་དག་ཏུ་མྱུར་དུ་བསྒོམས་པའི༌[^2093]ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ཀྱི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོས་ཉེ་བར་མཛེས་པའོ། །

[Block 3268]
འདིས་ནི་གཞལ་ཡས་ཁང་པ་བསྒོམ་པའི་འོག་ཏུ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 3269]
ཕྱོགས་བཅུ་ཞེས་བྱ་བ༌[^2094]ལ་སོགས་པ་ནས་བརྩམས་ཏེ། དཀྱིལ་འཁོར་ཞེས་བྱ་བའི་དོན་ཏོ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་ཉིད་ཀྱི་ཁྱད་པར་རོ། །

[Block 3270]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་དབུས་ཀྱི་གཙོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོས་བྱིན་གྱིས་བརླབ་པ་བསྟན་ཏོ། །

[Block 3271]
རིགས་ལྔས་བསྡུས་པའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དེ་ཉིད་རྡོ་རྗེ་ཕྲེང་བའི་རྒྱུད་ལས་གསུངས་པའི་རིམ་པས་སྐུའི་དཀྱིལ་འཁོར་ལ༌[^2095]འཇུག་པའི་མཚན་ཉིད་ཅན་གྱི༌[^2096]དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 3272]
དྲང་བའི་དོན་ཞེས་བྱ་བ་ནི་དང་པོ་སྦྱོར་བའི་ཏིང་འཛིན༌[^2097]གྱི་ཕྱོགས་གཅིག༌[^2098]བསྟན་པའི་ཕྱིར་རོ། །

[Block 3273]
ཚིག་གི་དོན་ཡང༌[^2099]འདི་ཡིན་ཏེ། ལེའུ་བཅོ་བརྒྱད་པ་ལས་གསུངས་པའི་གཟུངས་ཀྱི་དཀྱིལ་འཁོར་སྤྲུལ་ཏེ། འདོད་པའི་དབང་ཕྱུག་ཉིད་དུ་གྱུར་པ་བསྟན་ནས་གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་སྤྲོ་བ་སྔོན་དུ་འགྲོ་བས་ཁྲོ་བོའི་འཁོར་ལོས་བགེགས་བསྐྲད་ལ་ལེའུ་གཉིས་པ་ལས་གསུངས་པའི་དངོས་པོ་མེད་པ་ཞེས་བྱ་བ༌[^2100]ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་སྟོང་པ་ཉིད་མངོན་དུ་བྱས་ལ། རླུང་ལ་སོགས་པའི་དཀྱིལ་འཁོར་བཞི་ཡོངས་སུ་གྱུར་པའི་ཡེ་ཤེས་ཀྱིས་གཞིར་བྱིན་གྱིས་བརླབས་ཏེ། རི་རབ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་གཞལ་ཡས་ཁང་པ་བསམས་ལ། དེའི་ནང་དུ་སྣ་ཚོགས་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་སྟེང་དུ་མྱུར་དུ་དཀྱིལ་འཁོར་པའི་ཚོགས་བསྐྱེད་དེ། དེ་ཉིད་སླར་ཡང་རང་གི་ལུས་ལ་འཇུག་པའི་མཚན་ཉིད་ཅན་དོན་དམ་པའི༌[^2101]དཀྱིལ་འཁོར་དུ་རྣམ་པར་བསམས་ཏེ། བདག་པོ་དེ་ཡང་དབང་པོ་གཉིས་ཀྱིས༌[^2102]སྙོམས་པར་ཞུགས་པ་ལས་འབྱུང་བའི་འདོད་ཆགས་ཀྱི་སེམས་ཞུ་བར་གྱུར་པར་བསམས་ཏེ། སྟོང་པ་ཉིད་ཀྱི་སྔགས་ཀྱིས་བརྟན་པར༌[^2103]བྱ་ཞིང་གནས་པར་བྱའོ། །

[Block 3274]
རྣམ་པར་ཤེས་པའི་བདག་ཉིད་ཅེས་པ་ནས་བརྩམས་ཏེ་སྐྱེ་གནས་ཡིན་ཏེ་ཞེས་བྱ་བའི་བར༌[^2104]དུ་ནི་རྫོགས་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 3275]
དེ་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་གཉིས་པས་འོད་གསལ་བ་ཐོབ་པ་བསྟན་ཏོ། །

[Block 3276]
དགོངས་པ་ལུང་བསྟན་ཞེས་བྱ་བས་ལུང་གི་ཚིག་ཚད་མ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3277]
སངས་རྒྱས་ཀུན་གྱི་གང་བསྟན་པའི། །ཞེས་པ་ནི་དེ་ཉིད་ལ་བརྟེན་ཏེ། །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་བྱང་ཆུབ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3278]
སར་གྱུར་དེ་ནི་བཅུ་གསུམ་པ། ཞེས་པ་ནི་ལྷག་པར་མོས་པའི་སྤྱོད་པའི་ས་ནི་ཚོགས་ཀྱི་ལམ་མོ། །

[Block 3279]
རབ་ཏུ་དགའ་བ་ནི་མཐོང་བའི་ལམ་མོ། །

[Block 3280]
དྲི་མ་མེད་པ་དང་། འོད་བྱེད་པ་དང་། འོད་འཕྲོ་བ་དང་། སྦྱང་དཀའ་བ་དང་། མངོན་དུ་གྱུར་པ་དང་། རིང་དུ་སོང་བ་དང་། མི་གཡོ་བ་དང་། ལེགས་པའི་བློ་གྲོས་དང་། ཆོས་ཀྱི་སྤྲིན་རྣམས་ནི་བསྒོམ་པའི་ལམ་མོ། །

[Block 3281]
ཀུན་ཏུ་འོད་ཀྱིས་ནི་མི་སློབ་པའི་ལམ་མོ། །

[Block 3282]
དེ་ལ་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་ལས་འདས་པ་དང་། དེའི་རྗེས་ལ་སྐྱེས་པ་སྟེ་དག་པ་འཇིག་རྟེན་པའོ། །

[Block 3283]
ཇི་སྐད་དུ། རྣམ་པར་མི་རྟོག་པ་ལ་འཇུག་པའི་གཟུགས་ལས་ཤེས་བྱ་མ་ལུས་པའི་ཡེ་ཤེས་ཀྱིས་ནམ་མཁའི་དཀྱིལ་དང་མཚུངས་པར་ཆོས་ཐམས་ཅད་མཐོང་ངོ་། །དེའི་རྗེས་ལས་སྐྱེས་པས་ནི་སྒྱུ་མ་དང་། སྨིག་རྒྱུ་དང་། དྲི་ཟའི་གྲོང་ཁྱེར་དང་། བྲག་ཅ་དང་། གཟུགས་བརྙན་དང་། མཚུངས་པར་རྣལ་འབྱོར་པས༌[^2105]མཐོང་ངོ་། །དེའི་ཕྱིར་ན་ས་བཅུ་གསུམ་པ་སྟེ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་འོ། །

[Block 3284]
བཙུན་མོ་ནི་ཤེས་རབ་པོ། །དམ༌[^2106]ཆོས་བྷ་ག་ནི་ནང་དུ་སོང་བའི་དངོས་པོའི་རྐྱེན༌[^2107]དུ་ཤེས་པར་བྱ་སྟེ། དེས་ན་ཆོས་ཉིད་ནི་ས་བཅུ་གསུམ་པའོ། །

[Block 3285]
འཇོག་པར་གྱུར་པ་ནི་འོད་གསལ་བ་ལ་ཡེ་ཤེས་ཀྱི་སྐུ་འཇུག་པར་མཛད་དེ། མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་སོ་ཞེས་ཚིག་གི༌[^2108]ལྷག་མའོ། །

[Block 3286]
གསལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་འོད་གསལ་བ༌[^2109]རབ་ཏུ་བཞུགས་པར་གྱུར་ཏོ་ཞེས་པ་ནི་དེའི་བདག་ཉིད་དུ་མཛད་པའོ། །

[Block 3287]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་རིམ་པ་བཞི་པའི༌[^2110]སྒོམ་པས་དེ་ཁོ་ན་ཉིད་ཐོབ་པས་ན་འགྲོ་བའི་དོན་བྱ་བའི་ཕྱིར། ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱིས་རྡོ་རྗེའི་སྐུ༌[^2111]བླངས་སོ་ཞེས་བསྟན་ཏོ། །

[Block 3288]
ཇི་སྐད་དུ། ནམ་མཁའི༌[^2112]ཀུན་གྱི་སྐབས་ན་དཔལ། །ཞེས་པ་ནི་ནམ་མཁའི་དབྱིངས་མ་ལུས་པ་ལས༌[^2113]ཁྱབ་པའི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི༌[^2114]ཚོགས་དང་ལྡན་པའོ། །

[Block 3289]
རྡོ་རྗེ་སེམས་དཔའ་རབ་ཏུ་བཞུགས། །ཞེས་པ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ངོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོའོ། །

[Block 3290]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དམ་པའི་དཀྱིལ་འཁོར་ཡང་སྔ་མ་བཞིན་དུ་བཤད་པར་བྱའོ། །

[Block 3291]
ངེས་པའི་དོན་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་བདག་ལ་བྱིན་གྱིས་བརླབ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པ་དང་། ཟུང་དུ་འཇུག་པའི་རིམ་པས༌[^2115]བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3292]
དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་བར་དུ་བསྒོམ་པ་རྫོགས་པ་ན༌[^2116]དེ་ཉིད་ཡང་སྤྲོས་ཏེ། བསྟན་པར་བྱ་བའི་ཕྱིར། དོན་འདི་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདས་པ་དང་། མ་འོངས་པ་ཞེས་པ་ནི་དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ། །

[Block 3293]
ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པའི་རིམ་གྱིས་གཅིག་ཏུ་མཛད་པ་ནི་ཞེས་པ་ལ། ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དུ་ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པའི་སྟེང་དུ་རྣམ་པར་དགོད་ཅིང་བསྒོམ་པ་གང་ཡིན་པ་དེ་ནི་ཟིལ་གྱིས་གནོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3294]
དེའི་དོན་དུ་རྡོ་རྗེ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཏིང་ངེ་འཛིན་གྱི་མིང་ངོ་། །དེ་ལ་སྙོམས་པར་ཞུགས་ཞེས་པ་ནི་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དུ་བདག་པོ་ཉིད་དུ་གནས་སོ། །

[Block 3295]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས་དབུས་ཀྱི་བདག་པོ་དེ་ཉིད་ཀྱིས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་དཀྱིལ་འཁོར་པ་རྣམས་མྱུར་དུ་བསྒོམ་པར་བསྟན་ཏོ། །
--- END BLOCKS ---
