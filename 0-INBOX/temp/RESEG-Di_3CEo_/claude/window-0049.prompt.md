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
དེ་ལ་ཡང་། བསེ་རུ་བསྐལ་པ་བརྒྱ་ཡི་རྒྱུས། །རང་སངས་རྒྱས་ནི་རྣམ་པ་གཉིས་ཏེ། ཚོགས་ཤིང་སྤྱོད་པ་རྣམས་དང་། བསེ་རུ་ལྟ་བུ་རྣམས་སོ། །

[Block 1717]
དེ་དག་གི་ཕྱི་མ་ནི་བསྐལ་པ་ཆེན་པོ༌[^651]བརྒྱར་བྱང་ཆུབ་ཀྱི་ཚོགས་དག་ལ་སྤྱད་པས་རང་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་འཐོབ༌[^652]པའོ། །

[Block 1718 [HEADING]]
#### འཁོར་ལོས་སྒྱུར་བ། ^3-8-6-0

[Block 1719]
ཡང་འཁོར་ལོས་སྒྱུར་བ་རྣམས་ནམ་འབྱུང་ཞེ་ན།

[Block 1720 [VERSE]]
འཁོར་ལོས་སྒྱུར་བ༌[^653]འབྱུང་བ་ནི། །
སྟོང་ཕྲག་བརྒྱད་ཅུ་ལས་མི་འཕྱི། །

[Block 1721]
མི་རྣམས་ཀྱི་ཚེ་དཔག་ཏུ་མེད་པ་ནས་བརྒྱད་ཁྲིའི་བར་དུ་འཁོར་ལོས་སྒྱུར་བ་རྣམས་འབྱུང་སྟེ། འོག་ཏུ་ནི་མ་ཡིན་ནོ། །

[Block 1722]
དེ་དག་ནི་རྒྱལ་སྲིད་འཁོར་ལོས་སྒྱུར་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་འཁོར་ལོས་སྒྱུར་བ་རྣམས་སོ། །

[Block 1723]
དེ་དག་ཀྱང་རྣམ་པ་བཞི་སྟེ།

[Block 1724 [VERSE]]
གསེར་དངུལ་ཟངས་ལྕགས་འཁོར་ལོ་ཅན། །
དེ་དག་གླིང་གཅིག་གླིང་གཉིས་དང་། །
གསུམ་དང་བཞི་ལ་མས་རིམ་བཞིན། །

[Block 1725]
གང་ལ་ལྕགས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་གླིང་གཅིག་ལ་དབང་བྱེད་པ་ནས་གང་ལ་གསེར་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་གླིང་བཞི་ལ་དབང་བྱེད་པའི་བར་རོ། །

[Block 1726]
འཁོར་ལོས་སྒྱུར་བ་དེ་དག་ནི་འདི་ལྟར་འབྱུང་སྟེ། ལྷན་ཅིག་གཉིས་མིན་སངས་རྒྱས་བཞིན། །དེ་ལ་འགའ་ཞིག་ན་རེ་འཇིག་རྟེན་གྱི་ཁམས་སུ་སངས་རྒྱས་གཉིས་མི་འབྱུང་སྟེ། འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1727]
ཁ་ཅིག་ན་རེ་ཐམས་ཅད་དུ་མི་འབྱུང་ཞེས་འཛེར་ཏོ། །

[Block 1728]
ཡང་འཁོར་ལོས་སྒྱུར་བ་དག་ས་ལས་རྒྱལ་བར་བྱེད་པ་ན་ཇི་ལྟར་རྒྱལ་བར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ། ཕས་བསུ་རང་འགྲོ་གཡུལ་བཤམས་དང་། །མཚོན་བརྩམས་པས་རྒྱལ། གང་ལ་གསེར་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ལ་ནི་ཁམས་ཀྱི་རྒྱལ་ཕྲན་རྣམས་རང་རེས་ཕས་བསུ༌[^654]བར་བྱེད་དོ། །

[Block 1729]
གང་ལ་དངུལ་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་བདག་ཉིད་དེ་དག་གི་ཐད་དུ་འགྲོ་སྟེ་ཕྱིས་འདུད་དོ། །

[Block 1730]
གང་ལ་ཟངས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་དེར་སོང་ནས་གཡུལ་ཤམ༌[^655]པར་བྱེད་དོ། །

[Block 1731]
གང་ལ་ལྕགས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་དེ་དག་གི་ཐད༌[^656]དུ་སོང་ནས་ཕན་ཚུན་མཚོན་བརྩམས་པས་སོ། །

[Block 1732]
འཁོར་ལོས་སྒྱུར་བ་ཐམས་ཅད་ཀྱང་། །གནོད་པ་མེད། མཚོན་ཆས་རྒྱལ་ཡང་གསོད་དུ་མི་འཇུག་གོ། །

[Block 1733]
རྒྱལ་པོ་གཞན་དག་ལས་འདི་དག་སྐྱེས་བུ་ཆེན་པོའི་མཚན་དག་ནི་ཁྱད་པར་རོ། །

[Block 1734]
དེ་ལ་ཡང་།

[Block 1735 [VERSE]]
ཐུབ་མཚན་ཡུལ་ན་གནས་པ་དང་། །
གསལ་ལ་རྫོགས་པས་འཕགས་པ་ཡིན། །

[Block 1736]
[^657]སངས་རྒྱས་རྣམས་ཀྱི་མཚན་ནི་ཤིན་ཏུ་ཡུལ་ན་གནས་པ་དང་། ཤིན་ཏུ་གསལ་བ་དང་། ཤིན་ཏུ་ཀུན་དུ༌[^658]རྫོགས་པ་དག་ཡིན་པས་དེ་དག་གི་ཁྱད་པར་ནི་དེ་ཡིན་ནོ། །

[Block 1737 [HEADING]]
#### བསྐལ་པ་དང་པོའི་མི། ^3-8-7-0

[Block 1738]
ཡང་ཅི་བསྐལ་པ་དང་པོའི་མི་རྣམས་ཀྱང་རྒྱལ་པོ་དང་བཅས་པར་གྱུར་ཏམ། འོན་ཀྱང་།

[Block 1739 [VERSE]]
སྔར་བྱུང་སེམས་ཅན་གཟུགས་ཅན་བཞིན། །
དེ་ནས་རིམ་གྱིས་རོ་ལ་ཆགས། །
ལེ་ལོས་གསོག༌[^659]འཇོག་བྱས་ནས་ནི། །
འཛིན་བཅས་རྣམས་ཀྱིས་ཞིང་དཔོན་བསྟབས། །

[Block 1740]
བསྐལ་པ་དང་པོའི་མི་རྣམས་ནི་མངལ་ནས་སྐྱེས་པ་མ་ཡིན། དགའ་བའི་ཟས་ཅན་དང་། རང་གི་འོད་ཅན།[^660] བདག་གི་བ་མེད་པ་ཡོངས་སུ་གཟུང་བ༌[^661]མེད་པར་གྱུར་ཏོ། །

[Block 1741]
དེ་བཞིན་དུ་བྱུང་བ་དེ་དག་སའི་རོ་དང་ཞག་ལ་སོགས་པའི་རོ་ལ་བརྐམ་པར༌[^662]གྱུར་པས་དེ་ཡང་ནུབ་ནས་སཱ་ལུ༌[^663]ལ་སོགས་པ་ཡོངས་སུ་འཛིན་ཏེ། དེ་ལ་ཡང་བརྐུ་བ་ལ་སོགས་པ་ལ་རབ་ཏུ་འཇུག་པ་ན་དེ་བསྲུང་བའི༌[^664]ཕྱིར་རྒྱལ་པོ་བསྟབས་ཏེ། རྒྱལ་པོ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་རྩོམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 1742 [VERSE]]
དེ་ནས་ལས་ཀྱི་ལམ་ལྷག་པས། །
ཚེ་ཐུང་ལོ་ནི་བཅུ་ཡིན་ནོ། །

[Block 1743]
དེ་ནས་དེ་ལྟར་ལས་ཀྱི་ལམ་རྣམས་འཕེལ་བ་དང་། མི་རྣམས་ཀྱི་ཚེ་ཁད་ཀྱིས་ཐུང་ངུར་འགྱུར་ཏེ།

[Block 1744]
ཚེ་ལོ་བཅུ་པར་འགྱུར་རོ། །

[Block 1745 [HEADING]]
#### མཚོན་དང་ནད་དང་མུ་གེ། ^3-8-8-0

[Block 1746 [VERSE]]
བསྐལ་པ་མཚོན་དང་ནད་དང་ནི། །
མུ་གེ་དག་གིས༌[^665]ཚར་ཕྱིན་ཏོ། །

[Block 1747]
བར་གྱི་བསྐལ་པ་ནི་མཚོན་དང་ནད་དང་མུ་གེ་གསུམ་གྱིས༌[^666]ཚར་ཕྱིན་ཏོ། །

[Block 1748]
ཡང་མཚོན་གྱི་གནོད་པ་དང་། ནད་དང་མུ་གེ་དག་དུས་ཇི་སྲིད་གཅིག་འབྱུང་ཞེ་ན། །

[Block 1749 [VERSE]]
ཞག་རྣམས་དང་ནི་ཟླ་བ་དང་། །
ལོ་བདུན་དག་ཏུ་གོ་རིམས་བཞིན། །

[Block 1750]
མཚོན་ཆའི་བསྐལ་པ་བརྡེག་པ༌[^667]ནི་ཞག་བདུན་འབྱུང་ངོ་། །ནད་ནི་ཟླ་བ་བདུན༌[^668]དང་ཞག་བདུན་འབྱུང་ངོ་། །མུ་གེ་ནི་ལོ་བདུན་དང་ཟླ་བ་བདུན་དང་ཞག་བདུན་དུའོ། །

[Block 1751 [HEADING]]
#### འཇིག་པ་གསུམ། ^3-8-9-0

[Block 1752]
ཡང་འཇིག་པ་དག་ནི་དུ་ཞེ་ན།

[Block 1753 [VERSE]]
མེ་དང་ཆུ་དང་རླུང་དག་གིས། །
འཇིག་པ་དག་ནི་ཡང་གསུམ་ཡིན། །

[Block 1754]
འདིའི་སེམས་ཅན་རྣམས་བསམ་གཏན་གཅིག་ཏུ་འདུ་བས་ན་འཇིག་པ་ཡིན་ནོ། །

[Block 1755]
ཉི་མ་བདུན་དུ་ནི་མེས་འཇིག་པ་ཡིན་ནོ། །
--- END BLOCKS ---
