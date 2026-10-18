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
[Block 1646]
ཞེས་བྱ་བ་ལ། གལ་ཏེ་དོན་གྱི་ངོ་བོ་ཉིད་དུ་ཡོད་ན་ནི་དེས་ན་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་མེད་པར་འགྱུར་རོ། །

[Block 1647]
འོན་ཏེ་དེ་མེད་པའི་ངོ་བོ་ཉིད་ནི་འདོད་པ་ཡིན་ནོ་ཞེ་ན། དེས་ན་རྣམ་པར་མི་རྟོག་པ་དེ་མེད་པས་ན་སངས་རྒྱས་ཉིད་ཀྱང་འཐོབ་པར་མི་འགྱུར་རོ། །

[Block 1648]
དེས་ན་ངེས་པར་འདི་ལྟར་འདོད་པར་བྱ་བ་ཡིན་པས། བྱང་ཆུབ་སེམས་དཔའ་དབང་ཐོབ་དང་། །ཞེས་བྱ་བ་སྟེ། དབང་ཐོབ་པར་གྱུར་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1649]
མོས་དབང་གིས་ཞེས་བྱ་བ་ནི་བསམ་པའི་དབང་གིས་དེ་ལྟ་བུ་མེད་པའི་ས་ལ་སོགས་པ་དག་འདི་ལྟར་གསེར་ལ་སོགས་པའི་རང་བཞིན་དུ་འགྱུར་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1650]
བསམ་གཏན་པའི་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ལ་སོགས་པ་གཞན་གྱི་ཡང་ངོ་། །འདི་ལ་རྣམ་པར་འབྱེད་གྲུབ་པ། །ཞེས་བྱ་བ་ནི་ལྷག་མཐོང་གྲུབ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1651]
བློ་ལྡན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 1652]
ཞི་བ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཐོབ་པ་ཞེས་བྱ་བའི་དོན་ཏེ་ནང་གི་བདག་ཉིད་ཀྱིའོ། །

[Block 1653 [VERSE]]
ཆོས་ཀུན་ཡིད་ལ་བྱེད་པ་ལ། །
དེ་ལྟར་དོན་དུ་སྣང་ཕྱིར་རོ། །

[Block 1654]
ཞེས་བྱ་བ་ལ་འདི་ལྟར་ཇི་ལྟ་ཇི༌[^997]ལྟར་མདོ་སྡེ་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱི་དོན་ཡིད་ལ་བྱེད་པ་ན་དེ་ལ་དེ་ལྟ༌[^998]དེ་ལྟ་བུར་སྣང་བར་འགྱུར་ཏེ། གལ་ཏེ་སངས་རྒྱས་ཉིད་ཡིན་ནོ་ཞེས་ཆོས་དེ་དང་དེ་དག་ཡིད་ལ་བྱེད་པ་ན་སངས་རྒྱས་ཀྱི་དོན་དུ་སྣང་བར་འགྱུར་རོ། །

[Block 1655]
དེ་བཞིན་དུ་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་ནོ། །

[Block 1656 [VERSE]]
ཡེ་ཤེས་རྒྱུ་བ་རྟོག་མེད་ལ། །
དོན་རྣམས་ཐམས་ཅད་མི་སྣང་ཕྱིར། །

[Block 1657]
ཞེས་བྱ་བ་ལ། རྣམ་པར་རྟོག་པ་མེད་པའི་ཡེ་ཤེས་ཀྱི་རྒྱུ་བ་འཇུག་པ་ལ་འདི་ལྟར་དོན་ཐམས་ཅད་སྣང་བར་མི་འགྱུར་རོ། །

[Block 1658]
དེའི་ཕྱིར། དོན་མེད་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ། དེས༌[^999]ན་གལ་ཏེ་དོན་མེད་པ་ཡིན་ན་རྣམ་པར་རིག་པ་ཡང་མེད་པར་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན། རྣམ་པར་རིག་པ་མེད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། དོན་མེད་པས་ན་རྣམ་རིག་མེད། །ཅེས་བྱ་བ་ལ། [^1000]རྣམ་པར་རིག་པར་བྱ་བའི་དོན་མེད་ན། རྣམ་པར་རིག༌[^1001]པ་ཡང་རིགས་པར་མི་འགྱུར་བས་དེ་མེད་པར་བལྟ་བར་བྱའོ། །

[Block 1659]
དོན་འདི་ནི་ཤེས་བྱའི་མཚན་ཉིད་དུ་གོ་སླ་བར་ཕྱེ་ཟིན་ཏོ། །

[Block 1660 [HEADING]]
### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^8-20-0

[Block 1661]
དེ་ལྟ་བུའི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་གང་ཡིན་པ་དེ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་གནས་པའི་ཚུལ་གྱིས་གནས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་བས་སོ། །

[Block 1662 [HEADING]]
#### མུ་སྟེགས་ཅན་གྱི་ངར་འཛིན་པའི་གནས་ཡོངས་སུ་སྤོང་བ། ^8-20-1-0

[Block 1663]
དེ་དག་ཉིད་ཀྱི་དོན་གསལ་བར་བྱ་བར་འདོད་ནས་གཞུང་འདི་དག་གིས༌[^1002]བསྟན་ཏེ། ཇི་ལྟར་མི་གནས་པའི་ཚུལ་གྱིས་གནས་ནས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེ་ན། མུ་སྟེགས་ཅན་གྱི༌[^1003]ངར་འཛིན་པའི་གནས་ཡོངས་སུ་སྤོང་བ་དང་ཞེས་བྱ་བ་ལ་མུ་སྟེགས་ཅན་ཤེས་རབ་ལ་གནས་ནས་ང་རྒྱལ་དང་བཅས་པར་འགྱུར་ཏེ། བདག་ནི་ཤེས་རབ་ལ་གནས་པ། བདག་གི་ཤེས་རབ་ནི་འདི་ལྟ་བུ་ཞེས་མུ་སྟེགས་ཀྱི་གནས་པའི་རྣམ་པར་རྟོག་པ་སྤོང་བའི་ཕྱིར་ཤེས་རབ་ཀྱིས་གནས་པ་མེད་པའི་ཚུལ་གྱིས་གནས་པར་འགྱུར་རོ། །

[Block 1664 [HEADING]]
#### དེ་ཁོ་ན་མ་མཐོང་བའི་བྱང་ཆུབ་སེམས་དཔའི་རྣམ་པར་རྟོག་པ་གནས་ཡོངས་སུ་སྤོང་བ། ^8-20-2-0

[Block 1665]
དེ་ཁོ་ན་མ་མཐོང་བའི་བྱང་ཆུབ་སེམས་དཔའི་རྣམ་པར་རྟོག་པ་གནས་ཡོངས་སུ་སྤོང་བ་དང་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་དེ་ཁོ་ན་མ་མཐོང་བའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་བརྟག་པར་བྱ་བ་མེད་པ་ལ་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ་ཞེས་རྣམ་པར་རྟོག་པར་བྱེད་པ་དེས་ན༌[^1004]མི་གནས་པའི་ཚུལ་གྱིས་དེ་བཞིན་དུ་རྣམ་པར་རྟོག་པར་མི་བྱེད་དོ། །

[Block 1666 [HEADING]]
#### འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་མཐའ་གཉིས་ཀྱི་གནས་ཡོངས་སུ་སྤོང་བ། ^8-20-3-0

[Block 1667]
འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་མཐའ་གཉིས་ཀྱི་གནས་ཡོངས་སུ་སྤོང་བ་དང་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་འཇིག་རྟེན་པ་འཁོར་བའི་མཐའ་ལ་གནས་པ་དང་། ཉན་ཐོས་མྱ་ངན་ལས་འདས་པའི་མཐའ་ལ་གནས་པ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་གནས་པ་མ་ཡིན་ཏེ། དེ་ལྟར་ན་མི་གནས་པས་གནས་པ་ནི་ཇི་ལྟར་རིགས་པ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1668 [HEADING]]
#### ཉོན་མོངས་པའི་སྒྲིབ་པ་སྤངས་པ་ཙམ་གྱིས་ཆོག་པར་འཛིན་པའི་གནས་ཡོངས་སུ་སྤོང་བ། ^8-20-4-0

[Block 1669]
ཉོན་མོངས་པའི་སྒྲིབ་པ་སྤངས་པ་ཙམ་གྱིས་ཆོག་པར་འཛིན་པའི་གནས་ཡོངས་སུ་སྤོང་བ་དང་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཉན་ཐོས་རྣམས་ཉོན་མོངས་པའི་སྒྲིབ་པ་སྤངས་པ་ཙམ་གྱིས་ཆོག༌[^1005]པར་འཛིན་པ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་ནི་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ན་དགོངས་པ་འདིར་བྱང་ཆུབ་སེམས་དཔའ༌[^1006]རྣམས་མི་གནས་པའི་ཚུལ་གྱིས་གནས་པར་རིག་པར་བྱའོ། །

[Block 1670 [HEADING]]
#### སེམས་ཅན་གྱི་དོན་ལ་མི་ལྟ་བ་ཕུང་པོ་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་གནས་ཡོངས་སུ་སྤོང་བ། ^8-20-5-0

[Block 1671]
སེམས་ཅན་གྱི་དོན་ལ་མི་ལྟ་བ༌[^1007]ཕུང་པོ༌[^1008]ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་གནས་ཡོངས་སུ་སྤོང་བ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཉན་ཐོས་རྣམས་སེམས་ཅན་གྱི་དོན་ལ་ལྟོས་པ༌[^1009]མེད་པར་ཕུང་པོ་དག་པ་དང་མ་དག་པ་ནི་རྟེན་ཉིད་ཡིན་ནོ། །

[Block 1672 [HEADING]]
## དེའི་འབྲས་བུ་ཡེ་ཤེས། ^9-0

[Block 1673 [HEADING]]
### ཟབ་པ་ཉིད། ^9-1-0

[Block 1674]
དེ་དག་ནི་ཁམ་གྱི༌[^1010]ཟས་བོར་བ་རེག་པ་དང་། ཡིད་ལ་སེམས་པ་དང་། རྣམ་པར་ཤེས་པའི་ཟས་གསུམ་གྱིས་དེའི་རྟེན་གནས་པར་བྱེད་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་དེའི་རྟེན་གནས་པར་བྱེད་པ་ནི་གསུམ་ཡིན་ནོ། །

[Block 1675]
དག་པའི་རྟེན་གནས་པར་བྱེད་པ་ནི་ཁམ་གྱི་ཟས་ལ་སོགས་པ་བཞི་པོ་དེ་དག་ཉིད་ཡིན་ཏེ། ཉན་ཐོས་ལ་སོགས་པ་དེ་དག་གི་རྟེན་ཡང་དག་པ་རྣམས་འདི་ལྟར་གནས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1676]
གནས་པར་སྟོན་པ་ཡང་བཞི་པོ་དེ་དག་ཉིད་དེ། དེ་ཡང་གནས་པ་ལྟར་སྟོན་པའི་ཟས་ནི་སངས་རྒྱས་རྣམས་ཀྱི་སྟེ་བཞི་པའོ། །

[Block 1677]
འདི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་དེས་སྟོན་པ༌[^1011]ལྟར་སྟོན་ཏེ། སེམས་ཅན་སྦྱིན་པ་པོ་རྣམས་དེས་རབ་ཏུ་མགུ་བར་བྱ་བའི་ཕྱིར་དང་། བསོད་ནམས་བསགས་པའི་དོན་དུ་ཡིན་གྱི་ཡང་དེ་དག་གི་ཟས་ཀྱི་བྱ་བ་མཛད་པར་མི་འགྱུར་ཏེ། ཟས་དེ་དག་བཞེས་པའི་དུས་སུ་སངས་རྒྱས་ལས་ལྷ་རྣམས་ཀྱིས་བླངས་ནས་གཞན་སེམས་ཅན་རྣམས་ལ་སྦྱིན་པར་བྱེད་དེ། དེ་དག་ཀྱང་རྒྱུ་དེས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1678]
དེ་དག་ཐམས་ཅད་ཀྱང་ཟབ་པ་གཅིག་ཉིད་དུ༌[^1012]རིག་པར་བྱའོ། །

[Block 1679 [HEADING]]
#### སངས་རྒྱས་ཀྱི་སྐྱེ་བ་མེད་པ་དང་སྐྱེ་བའི་མཚན་ཉིད། ^9-1-1-0

[Block 1680]
དེ་ལྟ༌[^1013]མོད་ཀྱི་སངས་རྒྱས་ཀྱི་སྐྱེ་བ་མེད་པ་དང་སྐྱེ་བའི་མཚན་ཉིད་ནི་རྣམ་པ་བཅུར་རིག་པར་བྱ་སྟེ། ཀུན་ཏུ་རྨོངས་པ་རྣམ་པར་སེལ་བ་ཉིད་དང་། ཐ་དད་པ་རྣམ་པར་སེལ་བ་ཉིད་དང་། ལེན་པ་ལ་རང་དབང་ཉིད་དང་། གནས་པ་ལ་རང་དབང་ཉིད་དང་། གཏོང་བ་ལ་རང་དབང་ཉིད་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་། སྣང་བ་ཙམ་ཉིད་དང་། སྒྱུ་མ་ལྟ་བུ་ཉིད་དང་། མི་གནས་པར་རབ་ཏུ་གནས་པ་ཉིད་དང་། དོན་ཆེན་པོ་སྒྲུབ་པ་ཉིད་དོ། །

[Block 1681 [HEADING]]
#### འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ལ་རབ་ཏུ་མི་གནས་པ། ^9-1-2-0

[Block 1682]
རྣམ་པ་བཅུས་དེ་བཞིན་གཤེགས་པ་རྣམས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ལ་རབ་ཏུ་མི་གནས་པར་རིག་པར་བྱ་སྟེ། ལགས་པར༌[^1014]ཡོངས་སུ་ཤེས་པ་ཉིད་དང་། ལེགས་པར་སྤངས་པ་ཉིད་དང་། དངོས་པོ་མེད་པ་ཤེས་པ་ཉིད་དང་། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཤེས་པ་ཉིད་དང་། མི་དམིགས་ཤིང་མི་རྟོག་པ་ཉིད་དང་། སེམས་ཡོངས་སུ་སྤངས་པ་ཉིད་དང་། སེམས་སོ་སོར་ཐོབ་པ་ཉིད་དང་། སེམས་མཉམ་པ་ཉིད་དང་། དངོས་པོ་ལ་མི༌[^1015]དམིགས་པ་ཉིད་དང་། དམིགས་པ་ལ་དམིགས་པ་ཉིད་དོ། །

[Block 1683 [HEADING]]
#### སངས་རྒྱས་ཀྱི་མཛད་པ་ལྷུན་གྱིས་གྲུབ་པ། ^9-1-3-0

[Block 1684]
སངས་རྒྱས་རྣམས་ཀྱིས་སངས་རྒྱས༌[^1016]ཀྱི་མཛད་པ་ལྷུན་གྱིས་གྲུབ་པ་ཡང་རྣམ་པ་བཅུས་འགྲུབ་སྟེ་རབ་ཏུ་སྤངས་པ་ཉིད་དང་། བྱ་བ་ལ་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་། བྱེད་པ་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་། ལས་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་། མེད་པ་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་། ཡོད་པ་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་། སྔ་མ་ལས་ཁྱད་ཡོད་པ༌[^1017]ཉིད་དང་། བྱ་བ་མཐར་ཕྱིན་པ་ཉིད་དང་། བྱ་བ་མཐར་མ་ཕྱིན་པ་ཉིད་དོ། །

[Block 1685 [HEADING]]
#### སྐུ་ཟས་ཀྱིས་གནས་པར་སྟོན་པ། ^9-1-4-0
--- END BLOCKS ---
