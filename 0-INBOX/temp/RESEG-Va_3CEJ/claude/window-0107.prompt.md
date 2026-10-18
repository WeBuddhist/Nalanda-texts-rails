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
[Block 3746]
སྤྲིན་མེད་པ་རྣམས་ཀྱི་ནི་ཉིས་འགྱུར་དུ་བསྒྱུར་ནས་དེ་ལས་དཔག་ཚད་གསུམ་ཕྲི་ནས་དཔག་ཚད་བརྒྱ་ཉི་ཤུ་རྩ་ལྔ་པའོ།[^2132] །དེ་ཡན་ཆད་བསོད་ནམས་སྐྱེས་པ་ལ་སོགས་པ་ནས་འོག་མིན་པ་རྣམས་ཀྱི་ལུས་དཔག་ཚད༌[^2133]ཁྲི་དྲུག་སྟོང་ཡིན་པའི་བར་དུ་ཉིས་འགྱུར་ཉིས་འགྱུར་དུ་བསྒྱུར༌[^2134]རོ། །

[Block 3747 [HEADING]]
#### ཚེའི་ཚད། ^3-2-3-0

[Block 3748 [HEADING]]
##### བདེ་འགྲོའི་ཚེའི་ཚད། ^3-2-3-1-0

[Block 3749 [HEADING]]
###### མི་རྣམས། ^3-2-3-1-1-0

[Block 3750]
ཅི་དེ་ལྟར་བོང་ཚོད་ཐ་དད་པ་རྣམས་ཀྱི་ཚེ་ཡང་བྱེ་བྲག་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དེ། སྒྲ་མི་སྙན་ན་ཚེ་སྟོང་སྟེ། །ལོ་རྣམས་སོ། །

[Block 3751]
གཉིས་ལ༌[^2135]ཕྱེད་ཕྱེད་སྤངས་པའོ། །

[Block 3752]
གཉིས་ལ་ནི་ཕྱེད་ཕྱེད་སྤངས་ནས། བ་ལང་སྤྱོད་པ་ལ་སོགས་པ༌[^2136]རྣམས་ཀྱི་ནི་ལོ་ལྔ་བརྒྱའོ། །

[Block 3753]
ཤར་གྱི་ལུས་འཕགས་པ་རྣམས་ཀྱི་ནི་ཉིས་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3754]
འདི་ན༌[^2137]མ་ངེས། འཛམ་བུ༌[^2138]གླིང་འདི༌[^2139]ན་ནི་ཚེ་ངེས་པ་མེད་དེ། རེས་འགའ་ནི་རིང་པོར་འགྱུར་རོ། །

[Block 3755]
རེས་འགའ་ནི་ཐུང་ངོ་། །ཐ་མར་ནི། ལོ་བཅུ། ལོ་ཞེས་བྱ་བ་ནི་ལོ་སྐོར༌[^2140]ཡིན་ཏེ། ཐ་མ་ཐུང་ངུར་གྱུར་པ་ན་ཚེ་ལོ་བཅུ་པར་འགྱུར་རོ། །

[Block 3756]
དང་པོ་དཔག་ཏུ་མེད། བསྐལ་པ་དང་པོ་པའི་མི་རྣམས་ཀྱི་ཚེ་ནི་དཔག་ཏུ་མེད་པ་ཡིན་ཏེ། སྟོང་ལ་སོགས་པའི་གྲངས་ཀྱིས་ཡོངས་སུ་ཚད་གཟུང་བར༌[^2141]མི་ནུས་སོ། །

[Block 3757]
མི་རྣམས་ཀྱི་བཤད་ཟིན་ཏོ། །

[Block 3758 [HEADING]]
###### ལྷ་རྣམས། ^3-2-3-1-2-0

[Block 3759]
ལྷ་རྣམས་ཀྱི༌[^2142]བརྗོད་པར་བྱ་སྟེ། དེ་ཡང་ཉིན་ཞག་རྣམ་པར་བཞག་ནས་བརྗོད་པར་ནུས་པས་རེ་ཞིག་དེ་དག་གི་དེ་ཉིད་རྣམ་པར་གཞག་པར་བྱ་སྟེ། མི་རྣམས་ཀྱི་ལོ་ལྔ་བཅུ་ལ།

[Block 3760 [HEADING]]
###### **འདོད་པ་དང་ལྡན་པ་རྣམས།** ^3-2-3-1-2-1-0

[Block 3761 [VERSE]]
འདོད་པ་དག་གི་ལྷ་རྣམས་ལས། །
འོག་མ་དག་གི་ཉིན་ཞག་གཅིག །

[Block 3762]
མི་རྣམས་ཀྱི་ལོ་ལྔ་བཅུ་གང་ཡིན་པ་དེ་དག་ནི་འདོད་པ་ན་སྤྱོད་པའི་ལྷ་རྒྱལ་ཆེན་བཞིའི་རིས་པ་རྣམས་ཀྱི་ཉིན་ཞག་གཅིག་གོ། །

[Block 3763]
དེས་ན་ཚེ་ལོ་ལྔ་བརྒྱའོ། །

[Block 3764]
དེའི༌[^2143]ཉིན་ཞག་དེས་ན་དེ་རྣམས་ཀྱི་ཚེའི་ཚད་ནི་ཞག་སུམ་ཅུ་ལ་ཟླ་བ་གཅིག་གོ། །

[Block 3765]
ཟླ་བ་བཅུ་གཉིས་ལ་ལོ་གཅིག་ཏུ་བརྩིས་པའི་ལྷའི་ལོ་ལྔ་བརྒྱའོ། །

[Block 3766]
གོང་མ་གཉི་ག་ཉིས་འགྱུར་རོ། །

[Block 3767]
ལྔ་པོ་གོང་མ་རྣམས་ནི་ཉིན་ཞག་དང་ཚེ་གཉི་ག་ཉིས༌[^2144]འགྱུར་ཏེ། ཇི་ལྟ་ཞེ་ན། མི་རྣམས་ཀྱི་ཚེ་ལོ་བརྒྱ་གང་ཡིན་པ་དེ་ནི་སུམ་ཅུ་རྩ་གསུམ་གྱི་ལྷ་རྣམས་ཀྱི་ཉིན་ཞག་གཅིག་ཡིན་ལ། ཉིན་ཞག་དེས་ན་ཚེ་ལྷའི་ལོ་སྟོང་ཐུབ་བོ། །

[Block 3768]
དེ་བཞིན་དུ་མི་རྣམས་ཀྱི་ལོ་ཉིས་བརྒྱ་དང་། བཞི་བརྒྱ་དང་། བརྒྱད་བརྒྱ་དང་། སྟོང་དྲུག་བརྒྱ་ནི་འཐབ་བྲལ་ལ་སོགས་པའི་ཉིན༌[^2145]ཞག་གཅིག་ཡིན་ལ། ཉིན་ཞག་དེས་ན་ཚེའི་ཚད་ལྷའི་ལོ་ཉིས་སྟོང་དང་། བཞི་སྟོང་དང་། བརྒྱད་སྟོང་དང་། ཁྲི་དྲུག་སྟོང་ཐུབ་བོ། །

[Block 3769]
གཉའ་ཤིང་འཛིན་ཡན་ཆད་ན་ཉི་མ་དང་ཟླ་བ་མེད་པའི་ཕྱིར་ལྷ་རྣམས་ཀྱི་ཉིན་ཞག་རྣམ་པར་གཞག་པ་དང་། སྣང་བའི་བྱ་བ་ཇི་ལྟ་བུ་ཞེ་ན། ཀུ་མུ་ཏ༌[^2146]དང་པད་མ་བཞིན་དུ་མེ་ཏོག་རྣམས་ཁ་འཛུམས༌[^2147]པ་དང་། ཁ་འབྱེད་པ༌[^2148]དང་། བྱ་རྣམས་སྐད་འབྱིན་པ་དང་། སྐད་མི་འབྱིན་པ་དང་། གཉིད་སངས་པ་དང་། བྲོ་བ་ལས་སོ། །

[Block 3770]
སྣང་བའི་བྱ་བ་ནི་བདག་ཉིད་ལ་འོད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3771]
འདོད་པ་དང་ལྡན་པ་རྣམས་ཀྱི་ཚེའི་ཚད་བཤད་ཟིན་ཏོ། །

[Block 3772 [HEADING]]
###### **གཟུགས་ཅན།** ^3-2-3-1-2-2-0

[Block 3773]
གཟུགས་ཅན་ཉིན་མཚན་མེད་ཚེ་ནི།[^2149] །རང་ལུས་གཞལ་བའི་བསྐལ་པ་ཡིས། །གཟུགས་ཅན་གང་དག་གི་ལུས་དཔག་ཚད་ཕྱེད་ཡིན་པ་དེ་དག་གི་ཚེ༌[^2150]བསྐལ་པ་ཕྱེད་ཡིན་ལ། གང་དག་གི་དཔག་ཚད་གཅིག་ཡིན་པ་དེ་དག་གི་ནི་བསྐལ་པ་གཅིག་ཡིན་པ་ནས། དེ་བཞིན་དུ་འོག་མིན་པ་རྣམས་ཀྱི་ཚེའི་ཚད་བསྐལ་པ་ཁྲི་དྲུག་སྟོང་ཡོད་པའི་བར་དུ་གང་གི༌[^2151]ལུས་དཔག་ཚད་ཇི་སྙེད་པ་དེའི་ཚེ་ཡང༌[^2152]བསྐལ་པ་དེ་སྙེད་དོ། །

[Block 3774 [HEADING]]
###### **གཟུགས་མེད།** ^3-2-3-1-2-3-0

[Block 3775 [VERSE]]
གཟུགས་མེད་བསྐལ་པ་སྟོང་ཕྲག་ནི། །
ཉི་ཤུ་ལྷག་པས༌[^2153]ལྷག་པ་ཡིན། །

[Block 3776]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ན་ནི་ཚེའི་ཚད་བསྐལ་པ་ཉི་ཁྲིའོ། །

[Block 3777]
རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་ན་ནི་དེ་ལས་ཉི་ཁྲི་ལྷག་གོ། །

[Block 3778]
ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ན་ནི་དེ་ལས་ཉི་ཁྲི་ལྷག་གོ། །

[Block 3779]
སྲིད་པའི་རྩེ་མོ་ན་ནི་དེ་ལས་ཉི་ཁྲི་ལྷག་པའོ། །

[Block 3780]
དེ་ལྟར་ན་དེ་དག་གི་ཚེའི་ཚད་ནི་གོ་རིམས་བཞིན་དུ་བསྐལ་པ་ཉི་ཁྲི་དང་། བཞི་ཁྲི་དང་། དྲུག་ཁྲི་དང་། བརྒྱད་ཁྲི་ཡིན་ནོ། །

[Block 3781]
འདིར་བསྐལ་པ་གང་ཞིག་ཡིན་པར་རིག་པར་བྱ། ཅི་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཆགས་པ་དང་། གང་ཡང་ཆགས་ནས་བར་གྱི༌[^2154]བསྐལ་པ་ཉི་ཤུ༌[^2155]པ་ཆེན་པོ་ཞིག་ཡིན་ཞེ་ན།

[Block 3782 [VERSE]]
འོད་ཆུང་ནས་བཟུང་བསྐལ་ཆེན་ཏེ། །
དེ་ཡི་འོག་མ་ཕྱེད་ཡིན་ནོ། །

[Block 3783]
ལྷའི་རིས་འོད་ཆུང་ནས་བཟུང་བའི་ཚེའི་ཚད་ནི་བསྐལ་པ་ཆེན་པོར་རིག་པར་བྱའོ། །

[Block 3784]
དེའི་འོག་མ་ཚངས་ཆེན་ལ་སོགས་པའི་ཚེའི་ཚད་ནི་བསྐལ་པ་ཆེན་པོ་ཕྱེད་ལ་བསྐལ་པར་བྱས་ནས་རྣམ་པར་བཞག་གོ། །ཇི་ལྟ་བུ་ཞེ་ན། གང་ཡང་འཇིག་རྟེན་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་ཆགས་པ༌[^2156]དང་། གང་ཡང་ཆགས་ནས་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འདུག་པ་དང་། གང་ཡང་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཇིག་པ་དང་། བར་གྱི་བསྐལ་པ་དྲུག་ཅུ༌[^2157]པོ་དེ་དག་ལ་ཚངས་པ་ཆེན་པོའི་བསྐལ་པ་ཕྱེད་དང་གཉིས་སུ་བཤད་དེ། [^2158]དེ་ལྟར་བྱས་ན་བསྐལ་པ་ཆེན་པོའི་ཕྱེད་བར་གྱི་བསྐལ་པ་བཞི་བཅུ་ལ་བསྐལ་པར་བྱས་ནས་དེ་དག་གིས༌[^2159]ཚེའི་ཚད་དུ་བྱས་ནས་བཤད་པ་ཡིན་ནོ། །

[Block 3785]
བདེ་འགྲོའི་ཚེའི་ཚད་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
