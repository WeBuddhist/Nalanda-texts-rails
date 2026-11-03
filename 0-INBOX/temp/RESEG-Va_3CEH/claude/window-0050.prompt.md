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

[Block 1756 [HEADING]]
#### བསམ་གྱིས་མི་ཁྱབ་པ་ཟབ་པ་ཉིད། ^9-1-15-0

[Block 1757]
བསམ་གྱིས་མི་ཁྱབ་པ་ཟབ་པ་ཉིད་དེ་བསྟན་པར་བྱ་སྟེ། དེ་ཡང་འདི་ལྟར། ཉོན་མོངས་བྱང་ཆུབ་ཡན་ལག་འགྱུར། །ཞེས་བྱ་བ་སྟེ། ཀུན་འབྱུང་གི་བདེན་པའོ། །

[Block 1758]
འཁོར་བའང་ཞེས་བྱ་བ་སྡུག་བསྔལ་གྱི་བདེན་པ་ནི་ཞི་བའི་བདག་ཉིད་དོ། །

[Block 1759]
དེ་ལྟ་བུ་ཐམས་ཅད་ཀྱིས་ནི་དེ་བཞིན་གཤེགས་པའི་བསམ་གྱིས་མི་ཁྱབ་པ་སྔར༌[^1032]བསྟན་པ་རྒྱུ་གསུམ་གྱིས་སོ་སོར་རང་གིས་རིག་པར་བྱ་བ་ཡིན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 1760 [HEADING]]
### སངས་རྒྱས་རྗེས་སུ་དྲན་པ་རྣམ་པ་བདུན། ^9-2-0

[Block 1761]
ད་ནི་ཇི་ལྟར་སངས་རྒྱས་རྣམས་ཆོས་ཀྱི་སྐུར་རྗེས་སུ་དྲན་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔས༌[^1033]རྣམ་པ་བདུན་གྱིས༌[^1034]རྗེས་སུ་དྲན་པར་བྱེད་ཅིང་དེ་དག་གིས་དེ་བསྒོམ་པ་ཉིད་དོ། །

[Block 1762]
དེ་ལ་ཆོས་ཐམས་ཅད་ལ་དབང་སྒྱུར་བ་ཞེས་བྱ་བ་ནི་མངོན་པར་ཤེས་པ་དག་གིས་ཆོས་ཐམས་ཅད་ལ་དབང་སྒྱུར་བ་དེ་དག་ཉིད་ཀྱིས་གནས་པ་སྟེ། འདི་ལྟར་འཇིག་རྟེན་གྱི༌[^1035]ཁམས་ཐམས་ཅད་དུ་ཐོགས་པ་མེད་པའི་མངོན་པར་ཤེས་པ་ཅན་དུ་སངས་རྒྱས་རྣམས་འགྱུར་གྱི། ཉན་ཐོས་བཞིན་དུ་ཐོགས་པ་དང་བཅས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1763]
གལ་ཏེ་ཆོས་ཐམས་ཅད་ལ་དབང་སྒྱུར་བ༌[^1036]ཡིན་ན་དེ༌[^1037]ཅིའི་ཕྱིར་སེམས་ཅན་ཐམས་ཅད་མྱ་ངན་ལས་འདས་པར་མི་བྱེད་ཅེ་ན། དེ་ཚིགས་སུ་བཅད་པས་སྟོན་པར་བྱེད་དེ། རྒྱུ་གང་གི་ཕྱིར་མྱ་ངན་ལས་བཟླ་བར་མི་ནུས་པ་ནི། བསྒྲིབས་ཤིང་རྒྱུ་དང་མི་ལྡན་ལ།[^1038] །ཞེས་པ༌[^1039]ལ་སོགས་པ་སྟེ། དེ་ལ་བསྒྲིབས་ཤིང་ཞེས་བྱ་བ་ནི་གང་ལས་ལས་ལ་སོགས་པའི་སྒྲིབ་པས་བསྒྲིབས་པ༌[^1040]སངས་རྒྱས་མང་པོས་ཀྱང་མྱ་ངན་ལས་བཟླ་བར་མི་ནུས་སོ། །

[Block 1764]
རེ་ཞིག་དེ་དག་ལ་རྣམ་པ་དེ་ལྟ་བུར་སངས་རྒྱས་རྣམས་ལ་ཡང་ནུས་པ་མི་མངའ་བ་ཉིད་དོ། །

[Block 1765]
རྒྱུ་དང་མི་ལྡན་ལ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་བའི་ཆོས་ཅན་ནི་འདིར་རྒྱུ་དང་མི་ལྡན་པར་འདོད་དེ། གང་ལ་དེའི་རིགས་མེད་པའོ། །

[Block 1766]
ངེས་པ་གཉིས་དང་ལྡན་པའི་ཞེས་བྱ་བ་ལ། [^1041]ངེས་པ་གཉིས་ནི་ལས་བྱས་པར་ངེས་པ་དང་། རྣམ་པར་སྨིན་པ་སོ་སོར་མྱོང་བར་ངེས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1767]
དེའི་ཕྱིར་ན་ཡང་ངེས་པ་གཉིས་པོ་དེ་དག་ལ་སངས་རྒྱས་རྣམས་ལ་ནུས་པ་མི་མངའ་འོ། །

[Block 1768]
དེ་ལ་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ནི་ལྐུགས་པའི་དངོས་པོ་ལ་སོགས་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1769]
རྣམ་པར་སྨིན་པ་སོ་སོར་མྱོང་བ་ནི་ཡང་དམྱལ་བ་ལ་སོགས་པ་དག་ཏུ་ངེས་པར་འགྲོ་བར་འགྱུར་བ་སྟེ། དེ་ནི་དེ་དག་གི་བྱེ་བྲག་གོ། །

[Block 1770]
སྐུ་རྟག་པའོ་ཞེས་བྱ་བ་ནི་དྲི་མ་ལས་རྣམ་པར་གྲོལ་བའི་དེ་བཞིན་ཉིད་རྒྱུན་མི་འཆད་པ་དེ་ནི་རྟག་པ་ཡིན་ལ། དེ་ནི་དེ་བཞིན་གཤེགས་པའི་སྐུ་ཡིན་ཏེ། དེའི་ཕྱིར་ན་སྐུ་རྟག་པའོ། །

[Block 1771]
དེ་བཞིན་གཤེགས་པ་རྣམས་ལོངས་སྤྱོད་ཆེན་པོ་མངའ་བའོ་ཞེས་བྱ་བ་ནི་གང་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་དེ་ནི་ཆེན་པོ་ཡིན་ལ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རྗེས་སུ༌[^1042]ལོངས་སྤྱོད་པར་མཛད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1772]
དོན་ཆེན་པོའོ་ཞེས་བྱ་བའི་དོན་ཆེན་པོ་ཉིད་ནི་སངས་རྒྱས་རྣམས་ཀྱིས་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་མཛད་པ་རྣམས་ཡོངས་སུ་གྲོལ་བར་མཛད་པ་དང་། མ་སྨིན་པ་རྣམས་སྨིན་པ་དང་། མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་མྱ་ངན་ལས་འདའ་བར་བྱེད་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1773]
སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་རྣམ་པ་ལྷག་མ་རྣམས་ཀྱི་དོན་ནི་གོ་སླའོ། །

[Block 1774]
སངས་རྒྱས་རྗེས་སུ་དྲན་པ་རྣམ་པ་བདུན་པོ་དེ་དག་ཉིད་ཡང་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་བསྟན་པ་ནི། རང་གི་སེམས་ལ་རག་ལས་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ལ་རྣམ་པ་བདུན་པོ་དེས་ནི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ལ་རེ་ཞིག་དང་པོར་རང་གི་སེམས་ལ་རག་ལས་པའོ་ཞེས་བྱང་ཆུབ་སེམས་དཔའ་སངས་རྒྱས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་དྲན་པར་བྱའོ། །

[Block 1775]
དེ་ཡང་རྟག་དང་དགེ་ལྡན་ཏེ། །དེའི་ཕྱིར་ན་ཡང་མཆོག་ཏུ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 1776]
བཙལ༌[^1043]མི་དགོས་ཞེས་བྱ་བ་ནི་ལྷུན་གྱིས་གྲུབ་པར་སངས་རྒྱས་ཀྱི་མཛད་པ་མཛད་པའོ། །

[Block 1777]
ཆོས་ཀྱི་ལོངས་སྤྱོད་ཆེན་པོ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་རིག་པར་བྱའོ། །

[Block 1778]
དབང་དུ་མ་གྱུར་རབ་ཏུ་རྒྱུ། །ཞེས་བྱ་བ་ནི་གང་སྡུག་བསྔལ་གྱི་དབང་དུ་མ་གྱུར་པ་ཡང་ཡིན་ལ། དེ་ནི་རབ་ཏུ་རྒྱུ་བ་ཡང་ཡོད་དེ། སངས་རྒྱས་རྣམས་ཀྱི་ཐ་སྙད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1779]
དེའི་ཕྱིར་འདི་ལྟར། སྐྱེ་བོ་མང་པོར་དེ་འདོད་དོ། །ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་མང་པོའི་དོན་འདོད་པས༌[^1044]ཕུན་སུམ་ཚོགས་པ་རྗེས་སུ་དྲན་པ་གང་ཡིན་པའོ། །

[Block 1780 [HEADING]]
### སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ། ^9-3-0

[Block 1781 [HEADING]]
#### ཡོན་ཏན་ཕུལ་དུ་བྱུང་བ། ^9-3-1-0

[Block 1782]
གང་ཡང་སྟོང་ཕྲག་བརྒྱ་པའི་མདོ་སྡེའི་གླེང་གཞི་ལས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་རབ་ཏུ་བསྟན་ཏེ། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་དེའི་ཡོན་ཏན་ཕུལ་དུ་བྱུང་བ་གང་ཡིན་པ་དེ་ཚིག་འདི་རྣམས་ཀྱིས་གསལ་བར་བྱེད་དེ། རེ་ཞིག་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་ནི་རིན་པོ་ཆེ་སྣ་བདུན་ཏེ། གསེར་དང་། དངུལ་དང་། བཻ་ཌཱུཪྻ་དང་། མུ་ས་ལ་གར་བ༌[^1045]དང་། རྡོའི་སྙིང་པོ་དང་། དེ་སྨོས་པས་མརྒད༌[^1046]ལ་སོགས་པ་ཡང་གཟུང་བར༌[^1047]རིག་པར་བྱ་བ་དང་། མུ་ཏིག་དམར་པོ་སྟེ། དེ་ཡང་སྲོག་ཆགས་དམར་པོ་ཞིག་གི་ནང་ནས་འབྱུང་སྟེ། དེ་ཡང་ཐམས་ཅད་ཀྱི་མཆོག་ཡིན་ཏེ།[^1048] འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རིན་པོ་ཆེའི་རྒྱལ་པོས་ཀུན་ཏུ་སྣང་བར་བྱེད་དེ།[^1049] བཤད་མ་ཐག་པའི་རིན་པོ་ཆེ་རྣམས་ལས་ཀུན་ཏུ་བྱུང་བས༌[^1050]སོ། །

[Block 1783]
ཚིག་གཅིག་གིས་ནི་དབྱིབས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1784]
ཚིག་གཅིག་གིས་ནི་ཚད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1785]
ཚིག་གཅིག་གིས་ནི་ཡུལ་ཕུན་སུམ་ཚོགས་པའོ། །ཇི་ལྟ་བུའི་རྒྱུ་ལས་ཤེ་ན། འཇིག་རྟེན་ལས་འདས་པ་རྣམ་པར་མི་རྟོག་པ་དང་། དེའི་བླ་མ་རྗེས་ལས་ཐོབ་པ་དང་། དེ་དག་གཉི་གའི་དགེ་བའི་རྩ་བ་ལས་ཡང་དག་པར་བྱུང་བའི་དགེ་བའི་རྩ་བ་ནི་རྒྱུ་ཡིན་ཏེ། རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དེ་ལྟ་བུ་ཡང་ཚིག་གཅིག་གིས་སོ། །

[Block 1786]
འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག་གིས་སོ། །

[Block 1787]
ཤིན་ཏུ་རྣམ་པར་དག་པའི་རིགས༌[^1051]ལ་གང་དབང་སྒྱུར་བའི་མཚན་ཉིད་དེ་ནི་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་སྟེ་ཚིག་གཅིག་གིས་སོ། །

[Block 1788]
ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་ནི་ཚིག་གཅིག་གིས་སོ། །

[Block 1789]
ཞམ༌[^1052]རིང་བ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག༌[^1053]གིས་སོ།[^1054] །དེ་དག་ཉིད་ལ་ཀླུ་སྨོས་པས༌[^1055]ནི་ལྟོ་འཕྱེ་ཆེན་པོ་ཡང༌[^1056]གཟུང་བར་བྱ་སྟེ། སྦྲུལ་ཆེན་པོ་བསྡུ་བའི་ཕྱིར་རོ། །

[Block 1790]
དེ་ལ་ཉེ་བར་སྟོན་པར་བྱེད་པ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། ཚིག་གཅིག་གིས་བསྟན་ཏོ། །
--- END BLOCKS ---
