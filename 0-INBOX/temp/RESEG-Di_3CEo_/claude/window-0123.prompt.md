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
[Block 4306]
གསུམ་པོ་དང་ནི་རྟག་ཏུ་ལྡན་ནོ། །

[Block 4307 [HEADING]]
#### རྣམ་པར་ཐར་པ་བརྒྱད། ^8-3-2-0

[Block 4308]
རྣམ་པར་ཐར་བརྒྱད། གཟུགས་ཅན་གཟུགས་རྣམས༌[^1648]ལ་ལྟ་བ་ཞེས་བྱ་བ་ནི་དང་པོའོ། །

[Block 4309]
ནང་གཟུགས་མེད་པར་འདུ་ཤེས་པས་ཕྱི་རོལ་གྱི་གཟུགས་རྣམས་ལྟ་བ་ནི་གཉིས་པའོ། །

[Block 4310]
སྡུག་པའི་རྣམ་པར་ཐར་པ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱས་ཏེ་རྫོགས་པར་བྱས་ནས་གནས་པ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 4311]
གཟུགས་མེད་པ་བཞི་དང་།

[Block 4312]
བརྒྱད་པ་འདུ་ཤེས་དང་། ཚོར་བ་འགོག་པའོ། །

[Block 4313]
དེ་རྣམས་ལས། དང་པོ་གཉིས། མི་སྡུག །

[Block 4314]
དང་པོ་གཉིས་ནི་རྣམ་པར་བསྔོས་པ་ལ་སོགས་པའི་རྣམ་པ་ཅན་ཡིན་པའི་ཕྱིར་མི་སྡུག་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4315]
དེ་དག །བསམ་གཏན་གཉིས་ན་ཡོད།

[Block 4316 [VERSE]]
དང་པོ༌[^1649]དང་གཉིས་པ་ནའོ། །
གསུམ་པ་མཐའ་ན་དེ་མ་ཆགས། །

[Block 4317]
བསམ་གཏན་བཞི་པ་ན་མ་ཆགས་པའི་རང་བཞིན་ཡིན་ནོ། །

[Block 4318]
དེ་དག་འཁོར་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་བདག་ཉིད་དོ། །

[Block 4319]
གཟུགས་མེད་མཉམ་གཞག་དགེ་རྣམས་སོ། །

[Block 4320]
གཟུགས་མེད་པ་བཞིའི་ནི་མཉམ་པར་གཞག་པ་དགེ་བ་ཁོ་ན་རྣམ་པར་ཐར་པ་ཞེས་བྱའོ། །

[Block 4321]
འགོག་པའི་སྙོམས་པར་འཇུག་པའོ། །

[Block 4322]
རྣམ་པར་ཐར་པ་བརྒྱད་པ་འདུ་ཤེས་དང་ཚོར་བ་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སྟེ། དེ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4323]
དེ་ལ་ནི། ཕྲ་བ་ཕྲ་བའི་མཇུག་ཐོགས་སུ། །སྲིད་པའི་རྩེ་མོའི་འདུ་ཤེས་ནི་ཕྲ་བ་སྟེ། དེ་བས་ཀྱང་ཆེས་ཕྲ་བར་བྱས་ནས་འགོག་པ༌[^1650]ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4324 [VERSE]]
སྙོམས་པར་འཇུག་པ་རྣམས་ནི། །
རང་གི་ས་དང་འོག་མ་ཡི། །
འཕགས་པའི་སེམས་ཀྱིས་དེ་ལས་ལྡང་། །
སྲིད་པའི་རྩེ་མོའི་སེམས༌[^1651]པའམ། །

[Block 4325]
ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི་ས་པའི་སེམས་ཟག་པ་མེད་པས༌[^1652]དེ་ལས་ལྡང་ངོ་། །

[Block 4326 [VERSE]]
རྣམ་པར་ཐར་པ་འདི་དག་ལས། །
དང་པོ་འདོད་གཏོགས༌[^1653]སྣང་ཡུལ་ཅན། །

[Block 4327]
འདི་དག་གི་དམིགས་པ་ནི་ཅི་རིགས་པར་འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡིད་དུ་མི་འོང་བ་དང་ཡིད་དུ་འོང་བ་ཡིན་ནོ། །

[Block 4328 [VERSE]]
གང་དག་གཟུགས་ཅན་མིན་དེ་དག །
སྤྱོད་ཡུལ་གོང་དང་རང་གི་སའི། །
སྡུག་བསྔལ་སོགས་དང་རྗེས་ཤེས་ཕྱོགས། །

[Block 4329]
གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་རྣམས་ཀྱི་དམིགས་པ་ནི་རང་གི་ས་པ་དང་གོང་མའི༌[^1654]སྡུག་བསྔལ་དང་། དེའི་རྒྱུ་དང་། འགོག་པ་དང་། རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལམ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 4330 [HEADING]]
#### ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་བརྒྱད། ^8-3-3-0

[Block 4331]
ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་བརྒྱད། །ནང་གཟུགས་སུ་འདུ་ཤེས་པས་ཕྱི་རོལ་གྱི་གཟུགས་ཆུང་ངུ་ཁ་དོག་བཟང་པོ་ལ་སོགས་པ་རྣམས་ལ་ལྟ་ཞིང་། གཟུགས་དེ་དག་ཟིལ་གྱིས་མནན་ནས་ཤེས་ཟིལ་གྱིས་མནན་ནས་མཐོང་སྟེ། དེ་ལྟ་བུར་འདུ་ཤེས༌[^1655]པ་འདི་ནི་དང་པོའོ། །

[Block 4332]
དེ་བཞིན་དུ་ཆེན་པོ་རྣམས་ཀྱང་ཤེས་པར་བྱའོ།[^1656] །

[Block 4333]
དེ་ཁོ་ན་བཞིན་དུ་ནང་གཟུགས་མེད་པར་འདུ་ཤེས་པ་སྟེ། དེ་ལྟར་ན་བཞི་པོ་དེ་དག་དང་། །ནང་ན༌[^1657]གཟུགས་མེད་པར་འདུ་ཤེས་པ་དག་ཁོ་ན་སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། དཀར་པོ་རྣམས་ལ་ལྟ་བ་སྟེ། དེ་ལྟར་ན་བརྒྱད་ཡིན་ནོ། །

[Block 4334]
དེ་དག་ལས།

[Block 4335]
གཉིས་ནི་རྣམ་ཐར་དང་པོ་བཞིན། །

[Block 4336]
དང་པོ་དང་གཉིས་པའོ། །

[Block 4337]
གཉིས་ནི་གཉིས་པ་བཞིན་ནོ། །

[Block 4338]
གསུམ་པ་དང་བཞི་པ་ནི་རྣམ་པར་ཐར་པ་གཉིས་པ་བཞིན་ནོ། །

[Block 4339]
གཞན། སྡུག་པའི་རྣམ་པར་ཐར་པ་བཞིན། །སྡུག་པའི་རྣམ་པར་ཐར་པ་ཇི་ལྟ་བར་གཞན་བཞི་ཡང་དེ་དག་འདྲ་སྟེ། ཁྱད་པར་ནི་དེ་དག་གིས་ནི་རྒྱབ་ཀྱིས་ཕྱོགས་པ༌[^1658]ཙམ་དུ་ཟད་པ།[^1659] འདི་དག་གིས་དམིགས་པ་ཟིལ་གྱིས་གནོན་ཏོ། །

[Block 4340]
[^1660]ཇི་ལྟར་འདོད་པ་བཞིན་དུ་མོས་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 4341 [HEADING]]
#### ཟད་པར་བཅུ། ^8-3-4-0

[Block 4342]
ཟད་པར་བཅུའོ། །

[Block 4343]
བར་ཆད་མེད་པར་ཟད་པར་རྒྱས་པར་བྱེད་པའི་ཕྱིར། ཟད་པར་གྱི་སྐྱེ་མཆེད་ནི་བཅུ་སྟེ། ཟད་པར་ས་དང་ཆུ་དང་། མེ་དང་། རླུང་དང་། སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། དཀར་པོ་དང་། ཟད་པར་ནམ་མཁའ་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དོ། །

[Block 4344]
དེ་རྣམས་ལས།

[Block 4345]
བརྒྱད་མ་ཆགས།
--- END BLOCKS ---
