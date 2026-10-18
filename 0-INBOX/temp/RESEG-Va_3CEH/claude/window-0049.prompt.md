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
[Block 1716]
དེ་བཞིན་དུ་ཆོས་ཀྱི་དབྱིངས་སུ་བཞུགས་པ་དེ་དག་ཀྱང་། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་མཛད་པ་ཉེ་བར་འབྱུང་བ་མཉམ་པ་ཉིད་ཡིན་ནོ། །

[Block 1717]
བྱས་སོ་བྱེད་དོ་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དུ་སེམས་ཅན་གཞན་གྱི་དོན་ལ་དགོངས་པ་མེད་ཅེས་བྱ་བ་སྟེ། དེ་ལྟ༌[^1025]ན་ཡང་ནོར་བུ་དང་སིལ་སྙན་བཞིན་དུ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་མཛད་པར་འཇུག་པར་འགྱུར་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1718 [HEADING]]
#### མཐོང་བ་ཟབ་པ་ཉིད། ^9-1-10-0

[Block 1719]
མཐོང་བ་ཟབ་པ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། གང་། སངས་རྒྱས་རྟག་པའི་སྐུ་ཡིན་ནོ། །ཞེས་བརྗོད་པ་དེ་ལ་རྟག་པའི་སྐུ་ཉིད་ཡིན་ན་འཇིག་རྟེན་གྱིས་མི་མཐོང་བ་དེ་རྒྱུ་གང་གིས་མི་མཐོང་ཞེ་ན།

[Block 1720 [VERSE]]
སེམས་ཅན་ཉེས་པས་མི་སྣང་སྟེ། །
སྣོད་ཆག་པ༌[^1026]ཡི་ཟླ་བ་བཞིན། །

[Block 1721]
ཇི་ལྟར་སྣོད་ཆག་པའི་ནང་དུ་ཆུ་གནས་པར་མི་འགྱུར་ལ། དེ་མེད་ན་ཡང་དེར་ཟླ་བ་མཐོང་བར་མི་འགྱུར་རོ། །

[Block 1722]
དེ་བཞིན་དུ་ཞི་གནས་ཀྱི་རླན་མེད་པའི་སེམས་ཅན་གྱི་རྒྱུད་ལ་ཡང་སངས་རྒྱས་ཀྱི་ཟླ་བ་མཐོང་བར་མི་འགྱུར་ཏེ། འདིར་ཆུ་ཟླ༌[^1027]ལྟ་བུ་ནི་ཏིང་ངེ་འཛིན་ཡིན་ཏེ།

[Block 1723 [VERSE]]
རླན་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །
འཇིག་རྟེན་ཀུན་ལ་ཉི་བཞིན་དུ། །
དེ་དག་ཆོས་འོད་ཁྱབ་པར་མཛད། །

[Block 1724]
ཅེས་བྱ་བ་ནི། སངས་རྒྱས་རྣམས་ནི་མ་མཐོང་དུ་ཟིན་ཀྱང་ཕྲིན་ལས་མཛད་པ་ཉིད་ཡིན་ཏེ། འདི་ལྟར་མདོའི་སྡེ་ལ་སོགས་པའི་ཆོས་བསྟན་པ་འོད་ཟེར་ལྟ་བུ་གང་ཡིན་པ་དེས། སངས་རྒྱས་ཀྱི་མཛད་པ་སེམས་ཅན་ཡོངས་སུ་སྨིན་པ་ལ་སོགས་པ་འཇིག་རྟེན་ལ་སྣང་བར༌[^1028]མཛད་པ་ཉིད་ཡིན་ནོ། །

[Block 1725 [HEADING]]
#### མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་མྱ་ངན་ལས་འདས་པ་ཀུན་ཏུ་སྟོན་པ་ཟབ་པ་ཉིད། ^9-1-11-0

[Block 1726]
མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཀུན་ཏུ་སྟོན་པ་ཟབ་པ་ཉིད་ནི།

[Block 1727 [VERSE]]
ལ་ལར་རྫོགས་པར་བྱང་ཆུབ་སྟོན། །
ལ་ལར་མེ་བཞིན་མྱ་ངན་འདས། །

[Block 1728]
ཞེས་བྱ་བ་སྟེ། ལ་ལར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། ལ་ལར་མྱ་ངན་ལས་འདས་པ་སྟོན་པ་ནི་མེ་བཞིན་དུ་སྟེ། ཇི་ལྟར་མེ་ནི་ལ་ལ་ན་འབར། ལ་ལ་ན་ཞི་བ་དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱང་སེམས་ཅན་ཡོངས་སུ་སྨིན་པ་ཁ་ཅིག་ལ་ནི་མྱ་ངན་ལས་འདས་པར་སྟོན་ལ། ཡོངས་སུ་མ་སྨིན་པ་ཁ་ཅིག་ལ་ནི་དེ་ཡོངས་སུ་གྲོལ་བར་བྱ་བའི་ཕྱིར་རྫོགས་པར་བྱང་ཆུབ་པར་སྟོན་ཏེ། མེར་ཐ་མི་དད་པ་གཅིག་ལ་ཇི་ལྟ་བ༌[^1029]དེ་བཞིན་དུ་ཆོས་ཀྱི་སྐུ་གཅིག་ལ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 1729]
ཚིགས་སུ་བཅད་པ་ལྷག་མའི་དོན་ནི་གོ་སླའོ། །

[Block 1730 [HEADING]]
#### བཞུགས་པ་ཟབ་པ་ཉིད། ^9-1-12-0

[Block 1731]
བཞུགས་པ་ཟབ་པ་ཉིད་བསྟན་པའི་ཕྱིར།

[Block 1732 [VERSE]]
སངས་རྒྱས་འཕགས་མིན་ཆོས་རྣམས་དང་། །
མི་དང་ངན་སོང་བ་རྣམས་དང་། །
ཚངས་སྤྱོད་མ་ཡིན་ཆོས་རྣམས་ལས། །
བདག་ཉིད་དང་ནི་བཞུགས་པ་མཆོག །

[Block 1733]
ཅེས་བྱ་བ་ལ། བདག་ཉིད་མཆོག་དང་བཞུགས་པ་མཆོག་སྟེ། འཕགས་པ་ལ་སོགས་པའི་བཞུགས་པས་བཞུགས་པའོ། །

[Block 1734]
དེ་ལ་འཕགས་པའི་བཞུགས་པ་ནི་སྟོང་པ་ཉིད་ལ་བཞུགས་པ་གང་ཡིན་པའོ། །

[Block 1735]
ལྷའི་བཞུགས་པ་ནི་བསམ་གཏན་གྱིས་བཞུགས་པའོ། །

[Block 1736]
ཚངས་པའི་བཞུགས་པ་ནི་བྱམས་པ་ལ་སོགས་པ་ཚད་མེད་པ་དག་གིས་བཞུགས་པའོ། །

[Block 1737]
དེ་ལ་འཕགས༌[^1030]མིན་ཆོས་རྣམས་ཞེས་བྱ་བ་ནི་མི་དགེ་བ་སྟེ། དེས་དེ་དག་སྟོང་པ་ཉིད་ལ་བཞུགས་པས་དེའི་ཕྱིར་ཡང་འཕགས་པའི་བཞུགས་པའོ། །

[Block 1738]
གང་མི་དང་ངན་སོང་བ་རྣམས་ཀྱི་སེམས་ཅན་དེ་དག་ལ་དམིགས་པའི་བསམ་གཏན་དེ་ནི་ལྷའི་བཞུགས་པའོ། །

[Block 1739]
ཚངས་པར་སྤྱོད་པ་མ་ཡིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ལས་མཆོག་ཀྱང་ཡིན་ལ་བདག་ཉིད་ཀྱང་ཡིན་པས་འདི་ནི་བདག་ཉིད་མཆོག་སྟེ། སྟོང་པ་ཉིད་ལ་བཞུགས་པ་དེའི་བདག་ཉིད་དོ། །

[Block 1740 [HEADING]]
#### སྐུ་ཀུན་ཏུ་སྟོན་པ་ཟབ་པ་ཉིད། ^9-1-13-0

[Block 1741]
སྐུ་ཀུན་ཏུ་སྟོན་པ་ཟབ་པ་ཉིད་ནི།

[Block 1742 [VERSE]]
དེ་དག་ཀུན་ཏུ་རྣམ་པར་དཔྱོད། །
གང་དུའང་རྣམ་པར་དཔྱོད་མི་མངའ། །

[Block 1743]
ཞེས་བྱ་བ་ལ། དགེ་བ་དང་མི་དགེ་བ་ལ་བློ་འཇུག་པར་འགྱུར་བ་སྟེ། དེའི་རྗེས་ལས་ཐོབ་པས་དེ་དག་ཡོངས་སུ་དཔྱོད་ལ། རྣམ་པར་མི་རྟོག་པས་ནི་གང་ལ་ཡང་དཔྱོད་པར་མི་བྱེད་དོ། །

[Block 1744]
དོན་གཞན་གཉིས་པ་ནི་སྤྲུལ་པའི་སྐུས་ནི་ཐམས་ཅད་ལ་དཔྱོད་པར་བྱེད་ལ། སྐུ་གཞན་གྱིས་ནི་མ་ཡིན་ནོ། །ཞེས་བྱ་བའོ། །

[Block 1745]
གནས་རྣམས་ཀུན་ནའང་མཐོང་མོད་ཀྱི། །ཞེས་བྱ་བ་ནི་སྤྲུལ་པའི་ལུས་དེ་ཉིད་ཐམས་ཅད་དུ་མཐོང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1746]
དབང་པོ་དྲུག་གི་སྤྱོད་ཡུལ་མིན། །ཞེས་བྱ་བ་ནི་སེམས་ཅན་དམྱལ་བ་ལ་སོགས་པར་སྐྱེས་པས་མཐོང་བའི་སྤྲུལ་པ་དེ་ནི་དེར་སྐྱེས་པ་དེ་དག་འདུལ་བའི་ཕྱིར་ཡིན་གྱི། དེ་དག་ཉིད་ནི་སྤྲུལ་པའི་སྐུའི་ངོ་བོ་ཉིད་ནི་མ་ཡིན་ཏེ། དམྱལ་བ་དེ་དག་གིས་དེ་མཐོང་བ་ན་འདི་ཡང་སེམས་ཅན་དམྱལ་བ་ཡིན་ནོ་ཞེས་ཤེས་པས་ཡང་དམྱལ་བ་དེ་དག་གིས་དེ་དབང་པོ་དྲུག་གི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1747 [HEADING]]
#### ཉོན་མོངས་པ་སྤངས་པ་ཟབ་པ་ཉིད། ^9-1-14-0

[Block 1748]
ཉོན་མོངས་པ་སྤངས་པ་ཟབ་པ་ཉིད་སྟོན་པ་ནི།

[Block 1749 [VERSE]]
ཉོན་མོངས་ཐུལ་ལ་སྤངས་པ་མེད། །
སྔགས་ཀྱིས་བསད་པའི་དུག་དང་འདྲ། །

[Block 1750]
ཞེས་བྱ་བ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་གནས་སྐབས་ཀྱི་ཀུན་ནས་དཀྲིས་པའི་ཉོན་མོངས་པ་ཐུལ་ན་ཡང་ཉོན་མོངས་པ་སྤངས་པ་ནི་མ་ཡིན་ཏེ།

[Block 1751 [VERSE]]
དེའི་བག་ལ་ཉལ་ཡོད་པའི་ཕྱིར་རོ། །
སྔགས་ཀྱིས་བསད་པའི་དུག་དང་འདྲ། །

[Block 1752]
ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྔགས་ཀྱིས་བསད་པའི་དུག་གིས་ནི་འཆི་བར་མི་ནུས་པ་དེ་བཞིན་དུ་དེ་དག་གིས་ཀྱང་ཉོན་མོངས་པ་ཡོངས་སུ་ཤེས་པས་ཀུན་ནས་ཉོན་མོངས་པར་མི་བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1753]
སངས་རྒྱས་རྣམས་ནི་ཉོན་མོངས་ལས། །

[Block 1754]
ཉོན་མོངས་ཟད་པ་ཀུན་མཁྱེན་བརྙེས།[^1031] །ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཉོན་མོངས་པའི་བག་ཆགས་བཟུང་བ་དང་ལྡན་པ་ནི་ཉན་ཐོས་བཞིན་དུ་མྱ་ངན་ལས་འདའ་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1755]
སངས་རྒྱས་རྣམས་ནི་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཟད་པ་དང་བཅས་པའི་ཐམས་ཅད་མཁྱེན་པ་ཉིད་བརྙེས་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
