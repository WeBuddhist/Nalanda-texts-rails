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
[Block 2136]
གསུམ་པ་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་མ་ཆད་པའི་གནས་སྐབས་ལྷག་མ་རྣམས་སུའོ། །

[Block 2137]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2138]
མི་དགེ་བའི་མུ་དང་པོ་ནི་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་དང་ལྡན་པས་ཐམས་ཅད་ཀྱི་ཐ་མར་འདོར་བའི་ཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2139]
གཉིས་པ་ནི་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པས་ཐམས་ཅད་ཀྱི་དང་པོར་འཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2140]
འདི་སྐད་དུ་དེ་དག་ཉིད་ཀྱིས་ཡོངས་སུ་ཉམས་པའི་ཞེས་བརྗོད་པར་བྱ་བ་ནི་ཡིན་ནོ། །

[Block 2141]
གསུམ་པ་ནི་འདོད་པའི་འདོད་ཆགས་དང༌[^1125]བྲལ་བའི་གནས་སྐབས་ལྷག་མ་རྣམས་སུའོ། །

[Block 2142]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2143]
བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་ཡང་དེ་བཞིན་དུ་དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་དང་ཡོངས་སུ་ཉམས་པ་ལས་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 2144]
མ་བསྒྲིབས་ལ་ལུང་དུ་མ༌[^1126]བསྟན་པའི་ནི་ཚིག་ཕྱི་མ་དང་སྦྱོར་བ་སྟེ། རེ་ཞིག་འབྱིན་པ་གང་ཡིན་པ༌[^1127]ནི་འཛིན་པ་ཡང་ཡིན་ནོ། །

[Block 2145]
འཛིན་པ་ལས་མི༌[^1128]འབྱིན་པ་ཡང་ཡོད་དེ། དགྲ་བཅོམ་པའི་ཕུང་པོ་ཐ་མ་རྣམས་སོ། །

[Block 2146]
དམིགས་པ་དང་བཅས་པའི་ངེས་པས་ནི་སྐད་ཅིག་རེ་རེ་ལ་སྟེ། དགེ་བའི་སྐལ་བ་མཉམ་པའི་འབྲས་བུ་འཛིན་ལ་མི་འབྱིན་པ་ཞེས་བྱ་བ་མུ་བཞིའོ། །

[Block 2147]
མུ་དང་པོ་ནི་དགེ་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་ཉོན་མོངས་པ་ཅན་ནམ་ལུང་དུ་མ་བསྟན་པའི་སེམས་མངོན་དུ་བྱེད་པའོ། །

[Block 2148]
གཉིས་པ་ནི་བཟློག་པའོ། །

[Block 2149]
གསུམ་པ་ནི་དགེ་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་དགེ་བ་ཁོ་ནའོ། །

[Block 2150]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2151]
མི་དགེ་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2152]
ཡང་ཇི་ལྟར་ན་འབྲས་བུ་གཟུང་བ་ཡིན༌[^1129]ཞེ་ན། དེའི་ས་བོན་གྱི་དངོས་པོར་ཉེ་བར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 2153]
གཅིག་ནི་འདས་པས་འབྱིན་པར་འགྱུར། །རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་འདས་པ་ཁོ་ནས་འབྲས་བུ་འབྱིན་ཏེ། འདི་ལྟར་ལྷན་ཅིག་གམ་དེ་མ་ཐག་ཏུ་རྣམ་པར་སྨིན་པ་ནི་མེད་དོ།[^1130] །གཞན་དག་ནི་འབྲས་བུ་རྣམ་པ་བཞི་ཞིག་ཏུ་ཡང་འཆད་དེ། རྟེན་གྱི་འབྲས་བུ་ནི། འདི་ལྟ་སྟེ་རླུང་གི་དཀྱིལ་འཁོར་གྱིས་ཆུའི་དཀྱིལ་འཁོར༌[^1131]ལྟ་བུ་ནས་ས་གཞིའི་རྩ་བ༌[^1132]ལ་སོགས་པའི་བར་ལྟ་བུའོ། །

[Block 2154]
སྦྱོར་བའི་འབྲས་བུ་ནི་འདི་ལྟ་སྟེ་མི་སྡུག་པ་ནས༌[^1133]མི་སྐྱེ་བ་ཤེས་པའི་བར་ལྟ་བུའོ། །

[Block 2155]
ཚོགས་པའི་འབྲས་བུ་ནི་འདི་ལྟ་སྟེ། མིག་ལ་སོགས་པ་དག་གི་མིག་གི༌[^1134]རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དག་ལྟ་བུའོ། །

[Block 2156]
བསྒོམ་པའི་འབྲས་བུ་ནི་འདི་ལྟ་སྟེ་གཟུགས་ན་སྤྱོད་པའི་ལམ་གྱི་སྤྲུལ་པའི་སེམས་ལྟ་བུའོ། །

[Block 2157]
འདི་ཐམས་ཅད་ནི་སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གི་ཁོངས་སུ་འདུས་སོ། །

[Block 2158]
རྒྱུ་རྣམས་དང་འབྲས་བུ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2159 [HEADING]]
#### ཆོས་གང་ཞིག་རྒྱུ་དག་དུ་ཞིག་གིས་སྐྱེད་པ། ^2-4-3-0

[Block 2160]
དེ་ལ་ཆོས་གང་ཞིག་རྒྱུ་དག་དུ་ཞིག་གིས་སྐྱེད་པར་བྱེད་ཅེ་ན་སྨྲས་པ། མདོར་བསྡུ་ན་ཆོས་ནི་རྣམ་པ་བཞི་པོ་འདི་དག་ཡིན་ཏེ། འདི་ལྟ་སྟེ་ཆོས་ཉོན་མོངས་པ་ཅན་རྣམས་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་རྣམས་དང་། ཟག་པ་མེད་པའི་དབང་པོ༌[^1135]རྣམས་དང་། དེ་དག་གི་ལྷག་མ་རྣམས་སོ། །

[Block 2161]
ལྷག་མ་ཡང་གང་དག་ཡིན་ཞེ་ན། རྣམ་པར་སྨིན་པ་ལས༌[^1136]མ་གཏོགས་པའི་ལུང་དུ་མ་བསྟན་པ་རྣམས་དང་། ཟག་པ་མེད་པའི་སྐད་ཅིག་མ་དང་པོ་མ་གཏོགས་པའི་དགེ་བ་རྣམས་སོ། །

[Block 2162]
ཆོས་རྣམ་པ་བཞི་པོ་དེ་དག་ནི།

[Block 2163 [VERSE]]
ཉོན་མོངས་ཅན་དང་རྣམ་སྨིན་སྐྱེས། །
ལྷག་དང་དང་པོ༌[^1137]འཕགས་རིམ་བཞིན། །
རྣམ་སྨིན་ཀུན་འགྲོ་དེ་གཉིས་དང་། །
སྐལ་མཉམ་མ་གཏོགས་ལྷག་ལས་སྐྱེས། །

[Block 2164]
ཆོས་ཉོན་མོངས་པ་ཅན་རྣམས་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ་ལྔ་ལས་སྐྱེའོ། །

[Block 2165]
རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་རྣམས་ནི་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ་ལྔ་པོ་ཁོ་ན་ལས་སྐྱེའོ། །

[Block 2166]
ཆོས་ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་དེ་དག་མ་གཏོགས་པ་ལྷག་མ་བཞི་ལས་སྐྱེའོ། །

[Block 2167]
ཟག་པ་མེད་པའི་དང་པོ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་དེ་དག་དང་། སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ་གསུམ་ལས་སྐྱེའོ། །

[Block 2168]
ཆོས་རྣམ་པ་བཞི་པོ་བསྟན་པ་དེ་དག་གང་ཡིན་སྙམ་པ་ལ། སེམས་དང་སེམས་ལས་བྱུང་བ་ཡིན་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2169]
འོ་ན་གང་དག་སེམས་དང༌[^1138]ལྡན་པ་མ་ཡིན་པ་དང་། གཟུགས་ཅན་གྱི་ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཞེ་ན། མཚུངས་ལྡན་མ་གཏོགས་གཞན་དེ་བཞིན། །མཚུངས་པར་ལྡན་པའི་རྒྱུ་གཅིག་པོ༌[^1139]མ་གཏོགས་པ་ཆོས་ཉོན་མོངས་པ་ཅན་ལ་སོགས་པ་གཞན་ཡང་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་སྐྱེ་སྟེ། དེ་ལ༌[^1140]ཉོན་མོངས་པ་ཅན་རྣམས་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་རྣམས་ནི་བཞི་ལས་སོ། །

[Block 2170]
ལྷག་མ་རྣམས་ནི་གསུམ་ལས་སོ། །

[Block 2171]
ཟག་པ་མེད་པའི་དང་པོ་ནི་གཉིས་ལས་ཏེ། རྒྱུ་གཅིག་ལས་བྱུང་བའི་ཆོས་ནི་མེད་དོ། །

[Block 2172]
རྒྱུ་རྒྱ་ཆེར་བཤད་པ་རྫོགས་སོ། །

[Block 2173]
[^1141]

[Block 2174 [HEADING]]
### རྐྱེན་རྣམས། ^2-5-0

[Block 2175]
རྐྱེན་རྣམས་གང་ཞེ་ན། རྐྱེན་ནི་བཞི་པོ་དག་ཏུ་གསུངས། །
--- END BLOCKS ---
