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

[Block 1686]
རྣམ་པ་བཅུས་ན་སངས་རྒྱས་ཟས༌[^1018]ཀྱིས་ཟས་ཀྱི་བྱ་བ་མི་མཛད་ཀྱང་སྐུ་ཟས་ཀྱིས་གནས་པར་སྟོན་ཏེ། སེམས་ཅན་རྣམས་ཀྱི་བསོད་ནམས་བསགས་པའི་ཕྱིར་དང་། ཆོས་མཐུན་པ་ཉིད་དུ་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་དང་། རིགས་པ་ལ་ལོངས་སྤྱད༌[^1019]པར་རྗེས་སུ་བསླབ་པར་བྱ་བའི་ཕྱིར་དང་། ཆགས་པ་མེད་པར་བསླབ་པར་བྱ་བའི་ཕྱིར་དང་། མཆོད་པ་ཉེ་བར་བསྡུ་བའི་ཕྱིར་དང་། བརྩོན་འགྲུས་བརྩམས་པ་ཡང་དག་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དང་། དགེ་བའི་རྩ་བ་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་དང་། བདག་ཉིད་ཆགས་པ་མེད་པར་བསྟན་པར་བྱ་བའི་ཕྱིར་དང་། ལས་ལ་གུས་པ་ཉེ་བར་བསྟན་པར་བྱ་བའི་ཕྱིར་དང་། སྨོན་ལམ་འབྱུང་བ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1687 [HEADING]]
#### རྣམ་པར་གནས་པ་དང་གྲངས་དང་ཕྲིན་ལས་ཟབ་པ་ཉིད། ^9-1-5-0

[Block 1688 [HEADING]]
##### རྣམ་པར་གནས་པ་ཟབ་པ། ^9-1-5-1-0

[Block 1689]
དེ་ལ་གང་འོག་ནས་བརྗོད་པར་བྱ་བ་རྣམ་པར་གནས་པ་དང་། གྲངས་དང་ཕྲིན་ལས་ཟབ་པ་ཉིད་ཚིགས་སུ་བཅད་པས་བསྟན་པ། ཐ་དད་མེད་ཅིང་དཔག་ཏུ་མེད། །ཅེས་བྱ་བ་སྟེ། རྣམ་པར་གནས་པ་ཟབ་པ་ཡིན་ནོ། །

[Block 1690]
དེ་ལ་ཐ་དད་མེད་ཅེས་བྱ་བ་ནི་ཆོས་ཀྱི་སྐུ་ལ་དབྱེ་བ་མེད་པའོ། །

[Block 1691]
དཔག་ཏུ་མེད་པ་ནི་རྟེན་དུ་མ་ལས་མངོན་པར་བྱང་ཆུབ་པས་སོ། །

[Block 1692 [HEADING]]
##### གྲངས་ཟབ་པ་ཉིད། ^9-1-5-2-0

[Block 1693]
ཕྲིན་ལས་དཔག་ཏུ་མེད་ཅིང་གཅིག །ཅེས་བྱ་བ་ནི་གྲངས་ཟབ་པ་ཉིད་དེ། གང་གི་ཕྱིར་སངས་རྒྱས་རྣམས་དུ་མ་ཉིད་ཡིན་ན་ཡང་ཕྲིན་ལས་ནི་གཅིག་པ་ཉིད་ཡིན་ནོ། །

[Block 1694 [HEADING]]
##### ཕྲིན་ལས་ཟབ་པ་ཉིད། ^9-1-5-3-0

[Block 1695 [VERSE]]
མི་བརྟན་བརྟན་པའི་ཕྲིན་ལས་ཅན། །
སངས་རྒྱས་རྣམས་ནི་སྐུ་གསུམ་ལྡན། །

[Block 1696]
ཞེས་བྱ་བ་ལ། སངས་རྒྱས་རྣམས་སྐུ་གསུམ་དང་ལྡན་པས་ལོངས་སྤྱོད་རྫོགས་པའི་ཕྲིན་ལས༌[^1020]ནི་བརྟན་པ་ཡིན་ལ། སྤྲུལ་པའི་ཕྲིན་ལས༌[^1021]ནི་མི་བརྟན་པ་ཡིན་ཏེ། དེ་ལྟ་བུ་དག་ནི་ཕྲིན་ལས་ཟབ་པ་ཉིད་ཡིན་ནོ། །

[Block 1697 [HEADING]]
#### མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཟབ་པ་ཉིད། ^9-1-6-0

[Block 1698]
མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཟབ་པ་ཉིད་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ནི། གང་ཡང་མངོན་རྫོགས་སངས་རྒྱས་མེད། །ཅེས་བྱ་བ་ནི། གང་ཟག་དང་ཆོས་དངོས་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1699]
ཐམས་ཅད་སངས་རྒྱས་མ་ཡིན་མིན། །ཞེས་བྱ་བ་ནི་འདི་ལྟར་གདགས་པ་ནི་ཡང་སངས་རྒྱས་ཐམས་ཅད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་ཡིན་ནོ། །

[Block 1700]
དེའི་མངོན་པར་རྫོགས་པ་ཇི་ལྟ་བུ་ཞེ་ན། སྐད་ཅིག་རེ་ལ་དཔག་ཏུ་མེད། །ཅེས་བྱ་བས་བསྟན་ཏེ། གང་གི་ཕྱིར་སྐད་ཅིག་རེ་རེ་ལ་ཡང་དཔག་ཏུ་མེད་པ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་བས་སོ། །

[Block 1701]
དངོས་པོའི་དངོས་མེད་རབ་ཏུ་ཕྱེ། །ཞེས་བྱ་བ་ནི་འདིར་དེ་བཞིན་ཉིད་ནི་དངོས་པོའི་དངོས་པོ་མེད་པ་སྟེ། དེས་རབ་ཏུ་ཕྱེ་བ་ནི་སངས་རྒྱས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1702 [HEADING]]
#### འདོད་ཆགས་དང་བྲལ་བ་ཟབ་པ་ཉིད། ^9-1-7-0

[Block 1703]
འདོད་ཆགས་དང་བྲལ་བ་ཟབ་པ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། ཆགས་པ་མ༌[^1022]ཡིན་མི་ཆགས་མིན། །ཞེས་བྱ་བ་གསུངས་ཏེ། འདོད་ཆགས་མེད་པས་ཆགས་པ་མ་ཡིན་ལ། ཆགས་པ་མེད་པ་ཉིད་ཀྱིས་ན་ཡང་མི་ཆགས་པ་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་ཆགས་པ་ཡོད་ན་མི་ཆགས་པ་ཡང་རིགས་པའི་ཕྱིར་རོ། །

[Block 1704]
འདོད་ཆགས་ཉིད་ཀྱིས་བྱུང་བ་ཡིན། །ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་འདོད་ཆགས་ཀྱི་ཀུན་ནས་དཀྲིས་པ་སྤངས་པས་འདོད་ཆགས་ཀྱི་བག་ལ་ཉལ་དག་མ་བཟུང་བའི་ཕྱིར་གང་འདི་མ་བཟུང་བ་ཉིད་ཀྱིས་དེས་ན་ཉན་ཐོས་བཞིན་དུ་མྱ་ངན་ལས་འདའ་བར་འགྱུར་བས་སོ། །

[Block 1705 [VERSE]]
འདོད་ཆགས་འདོད་ཆགས་མིན་མཁྱེན་ནས། །
འདོད་ཆགས་ཆོས་ཉིད་ལ་ཡང་ཞུགས། །

[Block 1706]
ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་བརྟགས་པའི་འདོད་ཆགས་ནི་འདོད་ཆགས་མ་ཡིན་ནོ་ཞེས་རྣམ་པར་ཤེས་ནས། འདོད་ཆགས་ཀྱི་དེ་བཞིན་ཉིད་ལ་ཞུགས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1707 [HEADING]]
#### ཕུང་པོ་སྤངས་པ་ཟབ་པ་ཉིད། ^9-1-8-0

[Block 1708]
ཕུང་པོ་སྤངས་པ་ཟབ་པ་ཉིད་སྟོན་པའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 1709 [VERSE]]
སངས་རྒྱས་ཕུང་པོ་རྣམས་ལས་འདས། །
ཕུང་པོ་རྣམས་ལའང་རྣམ་པར་བཞུགས། །

[Block 1710]
ཞེས་བྱ་བ་སྟེ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་གཟུགས་ལ་སོགས་པ་ལས་ཤིན་ཏུ་འདས་ནས་དེ་དག་མི་དམིགས་པའི་ཆོས་ཉིད་ཀྱི་ཕུང་པོ་ལ་རབ་ཏུ་གནས་པའོ། །

[Block 1711]
དེ་ལས་གཞན་མིན་གཞན་མིན་མིན། །ཞེས་བྱ་བ་ནི། ཀུན་ཏུ་བརྟགས་པའི་ཕུང་པོ་དེ་དག་སྤངས་པ་ལས་དེ་གཞན་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་དག་ཉིད་ཀྱི་ཆོས་ཉིད་གང་ཡིན་པ་དེ་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 1712]
ཡང་གཞན་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། གང་གཅིག་ཉིད་ཡིན་ན་ཡང་ཀུན་ཏུ་བརྟགས་པ་རྣམ་པར་དག་པ་ལ་དམིགས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1713]
དེ་མ་བཏང་བས་ལེགས་པར་འདས། །ཞེས་བྱ་བ་ནི་དེ་དག་གིས༌[^1023]ཡོངས་སུ་གྲུབ་པའི་ཕུང་པོ་མ་བཏང་བས་ལེགས་པར་འདས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1714 [HEADING]]
#### ཡོངས་སུ་སྨིན་པར་མཛད་པ། ^9-1-9-0

[Block 1715]
ཡོངས་སུ་སྨིན་པར་མཛད་པ་སྟོན་པའི་ཚིགས་སུ་བཅད་པ་ནི། ཀུན་ཀྱང་འདྲེས་པའི་ཕྲིན་ལས་ཅན། །ཞེས་བྱ་བ་སྟེ། ཐམས་ཅད་ཀྱང་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་མཛད་པའི་ཕྲིན་ལས་མཉམ་པ་ཉིད་ཡིན་ནོ། །ཇི་ལྟ་བུར་ཞེ་ན། རྒྱ་མཚོར་ཆུ་འདྲ་ཞེས་བྱ་བ་སྟེ། ཇི་ལྟར་རྒྱ་མཚོར་འཇུག་པའི་ཆུ་རྣམས་ནི་ཉ་དང་། རུས་སྦལ་ལ་སོགས་པ༌[^1024]རྣམས་ཀྱི་ཉེ་བར་སྤྱད་པར་འགྱུར་རོ། །

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
--- END BLOCKS ---
