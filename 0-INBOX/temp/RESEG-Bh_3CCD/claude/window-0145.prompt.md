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
[Block 5076]
རིན་ཆེན་འབྱུང་ལྡན་གྱི་རྣལ་འབྱོར་པས་བགེགས་བསྐྲད་པ་ནས་བརྩམས་ཏེ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་ཀྱི་བར་དུ་རང་གི་སེམས་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བར་ལྷག་པར་མོས་ལ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་སྭ༌[^3001]དང་བཅས་པར་དགོད་ཅིང་ཡི་གེ་གསུམ་ཡང་རང་གི་ས་བོན་ལ་དགོད་དེ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་ཁ་དོག་སེར་པོ་ཟུར་དྲུག་པའི་རིན་པོ་ཆེ་བསྒོམས་ལ། དེ་ལས་ས་བོན་དེ་ཉིད་དགོད་དེ་ཟླ་བ་དང་རིན་པོ་ཆེ་དང་ཡིག་འབྲུ་ཡོངས་སུ་གྱུར་པ་ལས་བསྐྱེད་པའི་བཅོམ་ལྡན་འདས་རིན་ཆེན་འབྱུང་ལྡན་བསྒོམ་པར་བྱའོ། །

[Block 5077]
དོན་ཡོད་གྲུབ་པའི་རྣལ་འབྱོར་པས་བགེགས་བསྐྲད་པ་ནས་བརྩམས་ཏེ། ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་ཀྱི་བར་དུ་རང་གི་སེམས་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བར་བསྒོམས༌[^3002]ལ། ཡི་གེ་གསུམ་ཧ་དང་བཅས་པར་དགོད་དེ། ཡི་གེ་གསུམ་ཡང་རང་གི་ས་བོན་ལ་འཇུག་ཅིང་སྤྲོ་བ་དང་བསྡུ་བར་བྱས་ཏེ།[^3003] དེ་ཡོངས་སུ་གྱུར་པ་ལས་བསྐྱེད་པའི་རལ་གྲི་བསྒོམས༌[^3004]ལ། དེའི་ཆང་ཟུང༌[^3005]ལ་ཡིག་འབྲུ་དེ་ཉིད་དགོད་དེ། ཟླ་བ་དང་རལ་གྲི་དང་ས་བོན་ཡོངས་སུ་གྱུར་པ་ལས་བཅོམ་ལྡན་འདས་དོན་ཡོད་གྲུབ༌[^3006]པར༌[^3007]བསྒོམ་པར་བྱའོ། །

[Block 5078]
མི་བསྐྱོད་པའི་རྣལ་འབྱོར་པས་བགེགས་བསྐྲད་པ་ནས་བརྩམས་ཏེ། ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་ཀྱི་བར་དུ་རང་གི་སེམས་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བར་བསྒོམས་ལ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་དགོད་ཅིང་ཡི་གེ་གཉིས་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་ལ་ཞུགས་ཏེ། སྤྲོ་བ་དང་བསྡུ་བ་བྱས་ལ་དེ་ཡོངས་སུ་གྱུར་པ་ལས་བསྐྱེད་པའི་རྡོ་རྗེ་རྩེ་ལྔ་པ་རྣམ་པར་བསྒོམས་ལ། དེ་ཉིད་ཀྱི་དབུས་ཀྱི་རྩེ་མོར་ཡིག་འབྲུ་དེ་ཉིད་དགོད་ཅིང་ཟླ་བ་དང་རྡོ་རྗེ་དང་ས་བོན་ཡོངས་སུ་གྱུར་པ་ལས་བསྐྱེད་པའི་བཅོམ་ལྡན་འདས་མི་བསྐྱོད་པ༌[^3008]བསྒོམ་པར་བྱའོ། །

[Block 5079]
དེ་ཙམ་གྱིས༌[^3009]དང་པོའི་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་གཅིག་པར་གྱུར་པའི་རྣལ་འབྱོར་དང་རྗེས་སུ་རྣལ་འབྱོར་བསྟན་ཏོ། །

[Block 5080]
དེ་ཡང་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། ཕྱག་རྒྱ་ལེགས་པར་སྦྱང་བ༌[^3010]སྔོན་དུ་འགྲོ་བར་དཀྱིལ་འཁོར་རྒྱལ་བ༌[^3011]མཆོག་གི་ཏིང་ངེ་འཛིན་ཡང་བསྒོམ་པར་བྱའོ། །

[Block 5081]
ལས་ཀྱི་རྒྱལ་བ༌[^3012]མཆོག་གི་ཕྱོགས་གཅིག་ཕྲ་མོའི་རྣལ་འབྱོར་ནི་རང་གི་ཚིག་གིས་གསུངས་སོ་ཞེས་ཏིང་ངེ་འཛིན་གསུམ་གྱི་བདག་ཉིད་ཅན་གྱི་བསྐྱེད་པའི་རིམ་པ་བསྟན་པ་དང་རྫོགས་པའི་རིམ་པ་ཡང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་དབྱེ་བའི་སྒོ་ནས་བསྟན་ཏོ། །

[Block 5082]
དེ་ལྟར་རིམ་པ་གཉིས་ནི་གསལ་བར་བཤད་པ་ཡིན་ནོ། །

[Block 5083]
དེ་ལྟར་པདྨ་ཡོངས་སུ་གྱུར་པ་ལས་ཞེས་པ་ནི་ཟླ་བ་དང་པདྨ་དང་ཡིག་འབྲུ་ཡོངས་སུ་གྱུར་པ་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5084]
པདྨ་རཱ་གའི་འོད་ཅན་ནི་དབང་གི་ལས་ལ་ནུས་པའི་ཕྱིར་རོ། །

[Block 5085]
ཁ་དོག་སེར་པོ་ནི་རྒྱས་པའི༌[^3013]ལས་ལ་ནུས་པའི་ཕྱིར་ཏེ་གསེར་བཞིན་ནོ། །

[Block 5086]
སྣ་ཚོགས་རྡོ་རྗེ་ནི་སྒྲ་ཇི་བཞིན་མ་ཡིན་པས་རལ་གྲི་འམ་རང་གི་གཟུགས་སོ། །

[Block 5087]
ནམ་མཁའ་དང༌[^3014]འདྲ་བ་དེར་གནས་པ་ནི་ཞེས་པ་ནི་དེའི་ཁ་དོག་དང་ལྡན་པའོ། །

[Block 5088]
ནམ་མཁའ༌[^3015]ལྟར་སྔོ་བསངས་ཞེས་བྱ་བའི་དོན་ཏོ་ཞེས་པ་ནི་དེ་ཉིད་ཀྱི་བཤད་པའོ། །

[Block 5089]
སྐུ་དང་གསུང་དང་ཐུགས་སྒྲུབ་པས༌[^3016]མཚོན་པའི་ཞེས་པ་ནི་སྐུ་གསུང་ཐུགས་རྡོ་རྗེའི་ནང་ནས་ཐུགས་རྡོ་རྗེ་ཉིད་གཙོ་བོ་ཡིན་ཏེ། ལུས་དང་ངག་གི་རྩ་བ་དེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5090]
དེ་བས་ན་སྐུ་གསུང་ཐུགས་ཀྱི་སྒྲུབ་པ་ནི་དེ་བསྐྱེད་པ་ནི༌[^3017]རྒྱུར་གྱུར་པ་ཡི་གེ་གསུམ་མོ། །

[Block 5091]
དེས་མཚོན་པ་ནི་ཐུགས་རྡོ་རྗེ་འཆང་ཉིད་དེ་འོད་གསལ་བའི་རང་བཞིན་གྱི་ཐུགས་ལ་ཡི་གེ་གསུམ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 5092]
དེ་དང་འདྲ་བ་བཅོམ་ལྡན་འདས་ནི་མི་བསྐྱོད་པའོ། །

[Block 5093]
དེའི་རྡོ་རྗེ་ལས་བྱུང་བའོ་ཞེས་པ་ནི་ཟླ་བ་དང་རྡོ་རྗེ་དང་ཡིག་འབྲུ་དང་དེའི་བདག་ཉིད་ཀྱི་ང་རྒྱལ་ལས་བསྐྱེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5094]
ཐམས་ཅད་མཁྱེན་པ་ཉིད་ནི་ཞེས་པ་ལ་རང་གི་གོ་འཕང་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ལ་སོགས་པའོ། །

[Block 5095]
སེམས་ཅན་རྣམས་དམིགས་ཤིང་ཞེས་པ་ནི་སེམས་ཅན་རྣམས་ལ་སྟེར་བར་བྱེད་པ་བཅོམ་ལྡན་འདས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་རྣམས་སོ། །

[Block 5096]
ངང་ཚུལ་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ་ཞེས་པ་ནི་ཉེ་བར་བསྡུ་བའི་སྒོ་ནས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏེ་དེ་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5097]
རྡོ་རྗེ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ་ཞེས་པ་ནི་རྡོ་རྗེ་ལྟར༌[^3018]མི་ཕྱེད་པའི་ཡེ་ཤེས་དང་ལྡན་པའོ།[^3019] །

[Block 5098]
འདུས་པ་མཛད་པ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔའི་བདག་པོ་ཉིད་ཀྱིས་སོ། །

[Block 5099]
དེ་རྣམས་ཀྱི༌[^3020]རེ་རེ་ལ་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་དཀྱིལ་འཁོར་རོ། །

[Block 5100]
དེ་ལྟར་དཀྱིལ་འཁོར་སུམ་ཅུ་རྩ་གཉིས་ནི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་བསྡུས་པར་མཛད་པའོ། །

[Block 5101]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 5102 [HEADING]]
#### གཏི་མུག་གི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར། ^3-2-3-0

[Block 5103]
གཏི་མུག་གི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར་བསྟན་པར་བྱ་བའི་ཕྱིར༌[^3021]འོད་གསལ་བའོ་ཞེས་སྨོས་པ་ལ། །ལུས་རྣམ་པར་དབེན་པའི་མཐར་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5104]
དེའི་དབུས་སུ་གནས་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་དེ་མི་ཤིགས་པའོ་ཞེས་པ་ནི་ཟླ་བའི་དཀྱིལ་འཁོར་ལྟར་འབར་བར་འགྱུར་བའི་དབྱངས་ཀྱི་ཡི་གེ་དང་པོ་མི་ཤིགས་པ་ཞེས་བྱའོ། །

[Block 5105]
རབ་དུ་བྱེད་པ་ལས་ཀྱང་།

[Block 5106 [VERSE]]
ཐུང་ངུ་མ་ལུས་ངག་ཡིན་ཏེ། །
གཅིག་མིན་དུ་མ་མ་ཡིན་ནོ། །

[Block 5107]
ཞེས་འབྱུང་ངོ་།[^3022] །རྡོ་རྗེ་དཀྱིལ་འཁོར་གྱི་རྒྱན་ལས།

[Block 5108 [VERSE]]
འབར་ཞིང་མར་མེ་དང་མཚུངས་པའི། །
སྙིང་གའི་དབུས་ན་མི་ཤིགས་པ། །
མི་འགྱུར་པདྨ་ཕྲ་བ་སྟེ། །
ཨ་ཡིག་གཙོ་བོ་མཆོག་ཡིན་ནོ། །

[Block 5109]
ཞེས་འབྱུང་ངོ་། །

[Block 5110 [VERSE]]
སྒྱུ་འཕྲུལ་དྲ་བ་ལས་ཀྱང་། །
ཨ་ནི་ཡིག་འབྲུ་ཀུན་གྱི་མཆོག །
དོན་ཆེན་ཡི་གེ་དམ་པ་ཡིན། །
ཁོང་ནས་འབྱུང་བ་སྐྱེ་བ་མེད། །

[Block 5111 [VERSE]]
ཚིག་ཏུ་བརྗོད་པ་སྤངས་པ་སྟེ། །
བརྗོད་པ་ཀུན་གྱི་རྒྱུ་ཡི་མཆོག །

[Block 5112]
ཚིག་ཀུན་རབ་ཏུ་གསལ་བར་བྱེད། ཅེས་འབྱུང་ངོ་། །མི་ཤིགས་པ་ལ་ངེས་པར་འབྱུང་བའོ་ཞེས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོ་རྩིབས་བརྒྱད་པའི་ཡི་གེ་ཨ་ལས་འབྱུང་ཞིང་དེའི་སྤྲུལ་པ་ལས་བསྐྱེད་པའོ། །

[Block 5113]
ཆུའི་དཀྱིལ་འཁོར་ཏེ་མི་བསྐྱོད་པའི་ངོ་བོ་ཉིད་ཁ་དོག་དཀར་བ་ནི་ཞེས་པ་ལ་སྙིང་གར་གནས་པའི་ཕྱིར་དང་། ཆུའི་ཁམས་ཁ་དོག་དཀར་བའི་ཕྱིར་དང་། ཞི་བའི་ལས་ལ་བརྩོན་པའི་ཕྱིར་རོ། །

[Block 5114]
དལ་བར་རྒྱུ་བའི་ཕྱིར་རོ་ཞེས་པ་ནི་རླུང་གི་དཀྱིལ་འཁོར་བཞིན་དུ་ཆུ་ནི་དྲག་པར་རྒྱུ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་རང་བཞིན་གྱི་ཆུའི་ཁམས་དལ་བར་རྒྱུ་བ་སྟེ། སྟེང་དང་འོག་གི་གནས་ཀྱི་འབྲེལ་པས་དེ་རྣམས་ཀྱི་མྱུར་བ་དང་དམན་པ་དང་བར་མ་རྒྱུ་བ་ཡིན་ཏེ། ཆུ་བོ་དང་རྒྱ་མཚོ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 5115]
མེའི་དཀྱིལ་འཁོར་ཁ་དོག་དམར་པོའོ་ཞེས་པ་ལ་དེ་ཉིད་ཀྱི་རང་བཞིན་ལས་བྱུང་བ༌[^3023]གྲུ་གསུམ་པ་ལྐོག་མར་གནས་པའོ། །
--- END BLOCKS ---
