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
[Block 211]
ཅེས་བྱ་བ་ལ། ལག་པ་དང་ལྷུང་བཟེད་བཀྲུས་པའི་འོག་ཏུ་སྦྱིན་པའི་ཡོན་བདག་གི་སྨོན་ལམ་བདག་དང་གཞན་ལ་གནོད་པར་འགྱུར་བ་བཟློག་སྟེ། སྦྱིན་པའི་འབྲས་བུ་ལྷ་དང་མིའི་ལུས་ཐོབ་པའི་ལོངས་སྤྱོད་ཆེན་པོ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པའི་ཡོན་བདག་གི་དོན་དུ་ཚིགས་སུ་བཅད་པ་གཅིག་བཀླགས་པ༌[^120]དང་། ཀླུའི་རྒྱལ་པོ་དགའ་བོ་དང་། ཉེ༌[^121]དགའ་བོའི་དོན་དུ་ཚིགས་སུ་བཅད་པ་གཅིག་བཀླགས་ཏེ༌[^122]དེ་ལྟར་ཚིགས་སུ་བཅད་པ་གཉིས་ཤིག་གདོན་ཏོ། །

[Block 212 [HEADING]]
## དགེ་བ་བྱ་བ། ^4-0

[Block 213 [VERSE]]
མན་ངག་ཡོད་ན་བསམ་གཏན་བྱ། །
རབ་ཏུ་འབད་དེ་བཀླག་པར་བྱ། །
སྡོམ་དང་ཆོ་ག་མཁས་པ་དང་། །
བསྒྲུབ་པ་ལ་ནི་བརྩོན་པར་བྱ། །

[Block 214]
ཞེས་བྱ་བས་དགེ་བ་བྱ་བ་བསྟན་ཏེ། དེ་རྣམ་པ་བཞི་ཡོད་དེ་བསམ་གཏན་བྱ་བ་དང་། བཀླག་པ་དང་། ལྟུང་བ་དང་། མི་ལྟུང་བ་ལ་མཁས་པ་དང་།

[Block 215 [HEADING]]
### བསམ་གཏན་བྱ་བ། ^4-1-0

[Block 216 [VERSE]]
ཚུལ་ཁྲིམས་མ་ཉམས་པར་བསྲུང་བར་བྱའོ། །
མན་ངག་ཡོད་ན་བསམ་གཏན་བྱ། །

[Block 217]
ཞེས་བྱ་བས་བསམ་གཏན་བྱ་བར་བསྟན་ཏེ། དེ་ལ་ཡང་གང་ཟག་རྣམ་པ་བཞི་ཡོད་དེ།[^123] འདོད་ཆགས་ལ་སྤྱོད་པའི་གང་ཟག་དང་། ཞེ་སྡང་ལ་སྤྱོད་པའི་གང་ཟག་དང་། གཏི་མུག་ལ་སྤྱོད་པའི་གང་ཟག་དང་། རྣམ་པར་རྟོག་པ་ལ་སྤྱོད་པའི་གང་ཟག་གོ། །

[Block 218]
དེ་ལ་འདོད་ཆགས་ལ་སྤྱོད་པའི་གང་ཟག་གིས་ནི་མི་གཙང་བ་བསྒོམ༌[^124]མོ། །

[Block 219]
ཞེ་སྡང་ལ་སྤྱོད་པའི་གང་ཟག་གིས་ནི་སེམས་ཅན་ཐམས་ཅད་གཉེན་བཤེས་དང་ཉེ་དུ་བཞིན་དུ་སྡུག་པ་དང་ཕངས་པར་བསྒོམ་མོ། །

[Block 220]
གཏི་མུག་ལ་སྤྱོད་པའི་གང་ཟག་གིས་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལུགས་བཞིན་འབྱུང་བ་དང་ལུགས་ལས་བཟློག་པའི་མཚན་ཉིད་བསྒོམ་མོ། །

[Block 221]
རྣམ་པར་རྟོག་པ་ལ་སྤྱོད་པའི་གང་ཟག་གིས་ནི་དབུགས་ཕྱི་ནང་དུ་རྒྱུ་བ་བསྒོམ་མོ། །

[Block 222]
སྒོམ་པ་འདི་དག་ནི་བདུད་རྩིའི་སྒོ་ཞེས་བྱ་སྟེ། མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི༌[^125]རྒྱུ་ཡིན་ནོ། །

[Block 223]
གལ་ཏེ་བསམ་གཏན་འདི་དག་ལ་སོགས་པ་མན་ངག་གང་མཁན་པོ་དང་སློབ་དཔོན་ལ་ཐོས་ནས་ཟས་ཟོས་པའི་འོག་ཏུ་བསམ་གཏན་བྱའོ། །

[Block 224 [HEADING]]
### བཀླག་པ། ^4-2-0

[Block 225]
རབ་ཏུ་འབད་དེ་ཀླག༌[^126]པར་བྱེད། །ཅེས༌[^127]བྱ་བས་བཀླག་པར་བྱ་བ་བསྟན་ཏེ། གལ་ཏེ་བསམ་གཏན་བསྒོམ་པའི་མན་ངག་མེད་ན་བཀླག་པར་བྱ་སྟེ་ཁ་ཏོན་བྱ་བ་འམ། དྷརྨ་གླེགས་བམ་ལ་བཀླག་པར་བྱ་བའོ།[^128] །དེ་ལྟར་ཀློག་པའི་དུས་ན་ཡང་རབ་ཏུ་འབད་དེ་བཀླག་པར་བྱའོ། །

[Block 226]
དཀྱིལ་འཁོར་དང་མཆོད་པ་ལ་སོགས་པ་བྱས་ལ་སེམས་མ་ཡེངས་པར་རྩེ་གཅིག་ཏུ་བསྡུས་ནས་ལྷ་ཀླུ་ལ་སོགས་པ་ལ་ཆོས་ཀྱི་སྦྱིན་པ་བྱའོ། །

[Block 227]
ཧ་ཅང་ཡང་མི་དྲག་ཧ་ཅང་ཡང༌[^129]མི་དལ་བར་རེན་པར༌[^130]བྱ་སྟེ། ཟུར་ཕྱིན་པར་བཀླག་གོ། །

[Block 228]
བཀླགས༌[^131]པའི་རྗེས་ལ་ཡང་བསོད་ནམས་བདག་དང་སེམས་ཅན་གྱི་དོན་དུ་བསྔོའོ། །

[Block 229 [HEADING]]
### ལྟུང་བ་དང་མི་ལྟུང་བ་ལ་མཁས་པ། ^4-3-0

[Block 230]
སྡོམ་དང་ཆོ་ག་མཁས་པ་དང་། །ཞེས་བྱ་བས་ལྟུང་བ་དང་མི་ལྟུང་བར་བྱ་བ་ལ་མཁས་པར་བྱ་བ་བསྟན་ཏེ། སྡོམ་པའི་སྒྲ་ནི་ཕས་ཕམ་པ་བཞི་ལ་བྱ་ལ། ཆོ་གའི་སྒྲ་ནི་སྦོམ་པོ་དང་ཉེས་བྱས་ལ་སོགས་པ་བསླབ་ཚིག༌[^132]ཕྲ་མོ་དང་དགེ་སྦྱོང་གི་བྱ་བ་རྣམས་ལ་བྱ་སྟེ། མཁས་པ་ཞེས་བྱ་བས་ནི་འདི་ཙམ་གྱི༌[^133]ཕས་ཕམ་པར་འགྱུར་ལ། འདི་ཙམ་གྱིས་ཕས་ཕམ་པར་མི་འགྱུར་ཞེས་ཤེས་པར་བྱ་བ༌[^134]དང་། འདི་དག་ནི་ཉེས་བྱས་ཡིན། འདི་དག་ནི་བདག་གི་ལས་སུ་བྱ་བ་ཡིན། འདི་དག་ནི་བདག་གི༌[^135]ལས་སུ་བྱ་བ་མ་ཡིན་ནོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 231 [HEADING]]
### ཚུལ་ཁྲིམས་མ་ཉམས་པར་བསྲུང་བ། ^4-4-0

[Block 232]
བསྒྲུབ་པ་ལ་ནི་བརྩོན་པར་བྱ། །ཞེས་བྱ་བས་ཚུལ་ཁྲིམས་ལྷུར་ལེན་པ་བསྟན་ཏེ། ཕས་ཕམ་པ་དང་སྦོམ་པོ་དང་ཉེས་བྱས་ལ་སོགས་པ་མི་འབྱུང་བར་བསྲུང་བ་ཉིད་བསྒྲུབ་པར་བྱ་བ་ལ་བརྩོན་པ་ཡིན་ནོ། །

[Block 233 [HEADING]]
## ཕས་ཕམ་པའི་གནས། ^5-0

[Block 234]
ད་ནི་ཕས་ཕམ་པའི་གནས་འཆད་དེ། དེ་ལ་ཕས་ཕམ་པའི་དོན་ཅི་ཞེ་ན།

[Block 235 [VERSE]]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་ཆོས་ཀྱི་རྒྱལ་པོ། །
བདག་ནི་ཆོས་ཀྱི་རྒྱལ་པོའི་རྒྱལ་ཚབ་བོ། །

[Block 236]
ཚུལ་ཁྲིམས་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་ནི་བདག་གི་ཉོན་མོངས་པ་ཐམས་ཅད་ཞི་བར་བྱ་བའི་གྲོགས་སམ་མིག་ལྟ་བུ་ཡིན་ཏེ།

[Block 237]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱིས་ཉོན་མོངས་པ་བཅོམ་ནས་ཆོས་ཀྱི་རྒྱལ་པོའི་གནས་ཐོབ་པར་བྱ་བ་ཡིན་པ་ལས།

[Block 238]
འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པའི་དབང་དུ་གྱུར་པ་རྣམས་ཀྱིས་ཚུལ་ཁྲིམས་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་མེད་པར་བྱས་པས་བདག་གིས་ཆོས་ཀྱི་རྒྱལ་པོའི་གནས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱ་བའི་སྐལ་བ༌[^136]མེད་པ་ལ་ཕས་ཕམ་པ་ཞེས་བྱ་སྟེ། ཉོན་མོངས་པའི་གནས་སུ་གྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 239]
དེ་ལ་ཕས་ཕམ་པ་རྣམ་པ་བཞི་སྟེ། སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་དང་། མི་ཚངས་པར་སྤྱོད་པ་དང་། བརྫུན༌[^137]དུ་སྨྲ་བའོ། །

[Block 240]
ཕས་ཕམ་པ་འབྱུང་བའི་རྒྱུ་ནི་རྣམ་པ་གསུམ་སྟེ། ཞེ་སྡང་དང་། འདོད་ཆགས་དང་། གཏི་མུག་གོ། །

[Block 241]
དེ་ལ་ཞེ་སྡང་ལས་ནི་སྲོག་གཅོད་པའི་ཕས་ཕམ་པ་འབྱུང་ངོ་། །འདོད་ཆགས་ལས་ནི་མ་བྱིན་པར་ལེན་པ་དང་མི་ཚངས་པར་སྤྱོད་པའི་ཕས་ཕམ་པ་འབྱུང་ངོ་། །གཏི་མུག་ལས་ནི་བརྫུན་དུ་སྨྲ་བའི་ཕས་ཕམ་པ༌[^138]འབྱུང་ངོ་། །བཅོམ་ལྡན་འདས་ཀྱི༌[^139]ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལ་ལོ་བཅུ་གཉིས་ཀྱི་བར་དུ་ལྟ་བ་མཉམས་སྐྱོན་མེད་པས། དེས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་འདིར་མདོར་བསྡུས་ཏེ། ཉན་ཐོས་རྣམས་ལ་སོ་སོར་ཐར་པའི་མདོ་བཤད་དེ་བསྟན་པ།

[Block 242 [VERSE]]
སྡིག་པ་ཐམས་ཅད་མི་བྱ་སྟེ། །
དགེ་བ་ཕུན་སུམ་ཚོགས་པར་བྱ། །
རང་གི་སེམས་ནི་ཡོངས་སུ་གདུལ། །
འདི་ནི་སངས་རྒྱས་བསྟན་པའོ། །

[Block 243 [VERSE]]
ལུས་ཀྱི་སྡོམ་པ་ལེགས་པ་སྟེ། །
ངག་གི་སྡོམ་པ་ལེགས་པ་ཡིན། །

[Block 244]
ཡིད་ཀྱི་སྡོམ་པ་ལེགས་པ་སྟེ།[^140] །

[Block 245 [VERSE]]
ཐམས་ཅད་དུ་ནི་སྡོམ་པ་ལེགས། །
ཀུན་དུ་བསྡམས་པའི༌[^141]དགེ་སློང་ནི། །

[Block 246]
སྡུག་བསྔལ་ཀུན་ལས་རབ་ཏུ་གྲོལ།[^142] །

[Block 247 [VERSE]]
ངག་རྣམས་བསྲུངས་ཤིང་ཡིད་ཀྱང་རབ་བསྡམས་ཏེ། །
ལུས་ཀྱིས༌[^143]མི་དགེ་བ་དག་མི་སྤྱོད་ཅིང་། །

[Block 248]
ལས་རྣམས་གསུམ་པོ་འདི་དག་རབ་སྦྱངས་ནས།[^144] །དྲང་སྲོང་གསུང་བའི་ལམ་ནི་ཐོབ་པར་འགྱུར། །ཞེས་གསུངས་པས་སློབ་པར་ཟད་དོ། །

[Block 249]
ལོ་བཅུ་གཉིས་འདས་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^145]བསྟན་པ་ལ་སྐྱོན་དང་ཕན༌[^146]འབྱུང་ངོ་། །

[Block 250 [HEADING]]
### སྲོག་གཅོད་པའི་ཕས་ཕམ་པ། ^5-1-0
--- END BLOCKS ---
