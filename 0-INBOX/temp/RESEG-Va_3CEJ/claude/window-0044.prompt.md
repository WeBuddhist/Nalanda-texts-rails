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
[Block 1541]
ཡང་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 1542 [VERSE]]
འདུ་ཤེས་མེད་པ་པ་འདུ་ཤེས། །
མེད་པར་སེམས་དང་སེམས་བྱུང་རྣམས། །

[Block 1543]
འགོག་པའོ། །

[Block 1544]
འདུ་ཤེས་མེད་པའི་ལྷ་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བ༌[^689]དག་གི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་གང་ཡིན་པ་དེ་ནི་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བའི་རྫས་ཡིན་ཏེ། གང་གིས་མ་འོངས་པའི་དུས་ཀྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་དུས་གཞན་གྱི་བར་དུ་ཀླུང༌[^690]གི་ཆུ་འགོག་པ་བཞིན་དུ་འགོག་ཅིང་སྐྱེར་མི་སྟེར་བའོ། །

[Block 1545]
དེ་ཡང་གཅིག་ཏུ་རྣམ་པར༌[^691]སྨིན། །གང་གི་རྣམ་པར་སྨིན་པ་ཡིན་ཞེ་ན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པའི་ཡིན་ནོ། །

[Block 1546]
གང་དག་ན་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་འཁོད་པའི་སེམས་ཅན་དེ་དག་གང་ཞེ་ན། དེ་འབྲས་ཆེའང་།[^692] གང་དག་གི་ཕྱོགས་གཅིག་ན་སེམས་ཅན་འདུ་ཤེས་མེད་པ་ཁ་ཅིག་འཁོད་པའི་ལྷ་དེ་དག་ནི་འབྲས་བུ་ཆེ་བ༌[^693]ཞེས་བྱ་བ་ཡིན་ཏེ། བསམ་གཏན་ཁྱད་པར་ཅན་བཞིན་ནོ། །ཅི་དེ་དག་ནམ་ཡང་འདུ་ཤེས་ཅན་དུ་མི་འགྱུར་རམ་ཞེ་ན། སྐྱེ་བའི་དུས་དང་འཆི་འཕོས་པའི༌[^694]དུས་ན་འགྱུར་ཏེ།

[Block 1547]
མདོ་ལས།

[Block 1548]
སེམས་ཅན་དེ་དག་དུས་རིང་མོ་ཞིག་ཏུ་འདུག༌[^695]སྟེ། འདུ་ཤེས་སྐྱེས་ནས་གནས་དེ་ནས་འཆི་འཕོ་བར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །

[Block 1549]
དེ་དག་ཀྱང་ཡུན་རིང་པོར་གཉིད་ཀྱིས༌[^696]ལོག་པ་ལས་སངས་པ་བཞིན་དུ་དེ་ནས་ཤི་འཕོས་ནས་སྔོན་གྱི་སྙོམས་པར་འཇུག་པའི་འདུ་བྱེད་ཡོངས་སུ་ཟད་པའི་ཕྱིར་དང་། སྔོན་མེད་པ་མ་བསགས་པའི་ཕྱིར་མདའ་འཕངས་པ་ཤུགས་ཟད་པ་དག་ས་ལ་ལྟུང་བ་བཞིན་དུ་འདོད་པའི་ཁམས་སུ་སྐྱེ་བར་འགྱུར་ཏེ། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1550]
གང་ཞིག་དེར་སྐྱེ་བར་འགྱུར་བ་དེ་ལ་ནི་གདོན་མི་ཟ་བར་འདོད་པ་ན་སྤྱོད་པའི་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཡོད་དེ། དཔེར་ན་བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ཀྱི་ལྷར་སྐྱེ་བ་མྱོང་བར་འགྱུར་བ་བཞིན་ནོ། །

[Block 1551 [HEADING]]
#### སྙོམས་པར་འཇུག་པ། ^2-3-5-0

[Block 1552]
ཡང་། སྙོམས་འཇུག་དག་ཅེས་གང་བཤད་པ། །སྙོམས་པར་འཇུག་པ་དེ་དག་གང་ཡིན་ཞེ་ན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དང་། འགོག་པའི་སྙོམས་པར་འཇུག་པའོ། །

[Block 1553 [HEADING]]
##### འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ། ^2-3-5-1-0

[Block 1554]
འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་འདི་ཅི་ཞེ་ན། ཇི་ལྟར་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་ལ་འདུ་ཤེས་མེད་པ་པར་བཤད་པ། དེ་བཞིན་འདུ་ཤེས་མེད་སྙོམས་འཇུག །འདུ་ཤེས་མེད་པ་རྣམས་ཀྱི་སྙོམས་པར་འཇུག་པའམ་འདུ་ཤེས་མེད་པ་ཅན༌[^697]ཡིན་པས་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྟེ། དེ་ཡང་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་འགོག་པ་ཡིན་ནོ། །

[Block 1555]
དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲས་ནི་དེ་ཙམ་ཞིག་མཐུན་པར་འདོན༌[^698]ཏོ། །

[Block 1556]
སྙོམས་པར་འཇུག་པ་དེ་ནི་བསམ་གཏན་ཐ་མར། བསམ་གཏན་ཐ་མ་ནི་བཞི་པ་སྟེ། དེ༌[^699]ནི་དེར་གཏོགས་པ་ཡིན་གྱི་ས་གཞན་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་འདི་ལ་སྙོམས་པར་འཇུག་ཅེ་ན། འབྱུང་འདོད་པས། འདི་ལ་ངེས་པར་འབྱུང་བར་སེམས་ཏེ། དེའི་ཕྱིར་ཐར་པར་འདོད་པས་སྙོམས་པར་འཇུག་གོ། །

[Block 1557]
འདུ་ཤེས་མེད་པ་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིན་པའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 1558]
འདི་ནི་དགེ་བའོ། །

[Block 1559]
འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ནི་དགེ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 1560]
དེའི་རྣམ་པར་སྨིན་པ་ནི་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་ཀྱི་ནང་དུ་ཕུང་པོ་ལྔ་འགྲུབ་པའོ།[^700] །དེ་དགེ་བ་ཡིན་ཡང་། སྐྱེས་ནས་མྱོང་འགྱུར་ཉིད། སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་ཁོ་ན་ཡིན་གྱི་མཐོང་བའི་ཆོས་དང་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བ་ཡང་མ་ཡིན་ལ་མ་ངེས་པ་ཡང་མ་ཡིན༌[^701]ནོ། །

[Block 1561]
གང་ཞིག་གིས་འདི་བསྐྱེད་ནས་ཡོངས་སུ་ཉམས་པ་དེ་ཡང་གདོན་མི་ཟ་བར་ཡང་བསྐྱེད༌[^702]ནས་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བར་འགྱུར་རོ། །ཞེས་གྲག་གོ། །

[Block 1562]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ཐོབ་པ་ནི་ངེས་པ་ལ་མི་འཇུག་གོ། །

[Block 1563]
དེ་ཡང་སོ་སོའི༌[^703]སྐྱེ་བོ་ཁོ་ནའི་ཡིན་པར་འདོད་ཀྱི། འཕགས་པའི་མ་ཡིན། འཕགས་པ་རྣམས་ནི་འདི་ལ་རྣམ་པར་ལྟུང་བའི་གནས་ལྟ་བུར་གཟིགས་པས་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་མི་འཇུག་གི་ངེས་པར་འབྱུང་བའི་འདུ་ཤེས་ཅན་དག་ནི་དེ་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 1564]
ཡང་ཅི་འཕགས་པ་བསམ་གཏན་བཞི་པ་ཐོབ་ནས་བསམ་གཏན་བཞིན་དུ་འདི་འདས་པ་དང་མ་འོངས་པ་དག་ཀྱང་འཐོབ་བམ་ཞེ་ན། རེ་ཞིག་གཞན་དག་གིས་ཀྱང་མི་འཐོབ་པོ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་འདྲིས་པ༌[^704]ཡིན་ཡང་མངོན་པར་འདུ་བྱ་བ་ཆེན་པོས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་དང་། སེམས་མེད་པ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1565]
དུས་གཅིག་འཐོབ་དུས་གཅིག་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། སོ་སོར་ཐར་པའི་སྡོམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ད་ལྟར་གྱི་དུས་པ་ཁོ་ན་འཐོབ་པོ། །སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པར་ནི་ཇི་སྲིད་མི་གཏོང་བ་དེ་སྲིད་དུ་ཐོབ་པ་འདས་པ་དང་ཡང་ལྡན་པ་ཡིན་ནོ། །

[Block 1566]
སེམས་མེད་པ་པ་ཡིན་པའི་ཕྱིར་མ་འོངས་པ་ནི་མི་འཐོབ་པོ། །

[Block 1567 [HEADING]]
##### འགོག་པའི་སྙོམས་པར་འཇུག་པ། ^2-3-5-2-0

[Block 1568]
ད་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་གང་ཞེ་ན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཇི་ལྟ་བུར། འགོག་པ་ཞེས་པའང་དེ་བཞིན་ཉིད། །དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲས་རྣམ་པ་གང་ཞིག་གཟུང་ཞེ་ན། སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པའོ་ཞེས་བྱ་བ་གཟུང་ངོ་། །འདིའི་ཁྱད་པར་ནི་འདི་ཡིན་ཏེ། འདི་གནས་དོན་དུ། ཞི་བར་གནས་པའི་འདུ་ཤེས་སྔོན་དུ་བཏང་བའི་ཡིད་ལ་བྱེད་པས་འདི་ལ་སྙོམས་པར་འཇུག་གི །དེ་ལ་ནི་ངེས་པར་འབྱུང་བའི་འདུ་ཤེས་སྔོན་དུ་བཏང་བས་སོ། །

[Block 1569]
ཡང་དེ་ནི་བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་གྱི་འདི་ནི། སྲིད་རྩེ་སྐྱེས། འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན༌[^705]སྐྱེ་མཆེད་ཀྱི་ས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1570]
འདི་ནི་དགེ་བའོ། །

[Block 1571]
དགེ་བ་ཁོ་ན་ཡིན་ཏེ།[^706] ཉོན་མོངས་པ་ཅན་ཡང་མ་ཡིན་ལ། ལུང་དུ་མ་བསྟན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1572]
དགེ་བ་ཡིན་ཡང་། གཉིས་སུ་མྱོང་འགྱུར་དང་མ་ངེས། །སྐྱེ་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བ་སྟེ།[^707] དུས་གཉིས་སུ་མྱོང་བར་འགྱུར་བ་དང་། རྣམ་པར༌[^708]སྨིན་པའི་ཕྱིར་མ་ངེས་པ་ཡང་ཡིན་ཏེ། གལ་ཏེ་འདིར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་བྱེད་ན་ནམ་ཡང་རྣམ་པར་མི་སྨིན་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 1573]
དེའི་རྣམ་པར་སྨིན་པ་ནི་སྲིད་པའི་རྩེ་མོའི་ཕུང་པོ་བཞི་ཡིན་ནོ། །

[Block 1574]
དེ་ཡང་གཅིག་ཏུ་འཕགས་པའི༌[^709]སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིས་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སྐྱེད་མི་ནུས་ཏེ། ཆད་པས་འཇིགས་པའི་ཕྱིར་དང་། འཕགས་པའི་ལམ་གྱི་སྟོབས་ཀྱིས་བསྐྱེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 1575]
མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པ་ནི་དེ་ལ་མོས་པའི་ཕྱིར་རོ། །

[Block 1576]
འཕགས་པའི་ཡང་འདི་ནི་འདོད་ཆགས་དང༌[^710]བྲལ་བས་ཐོབ་པར་བྱ་བ་མ་ཡིན་ཏེ། འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། སྦྱོར་བས་འཐོབ། འདི་ནི་སྦྱོར་བས་འཐོབ་པར་བྱ་བ་ཁོ་ན་ཡིན་པས། འདས་པ་ཡང་མི་འཐོབ་ལ་མ་འོངས་པ་ཡང་མི་འཐོབ་སྟེ། དེ་ནི་སེམས་ཀྱི་སྟོབས་ཀྱིས་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 1577]
ཅི་བཅོམ་ལྡན་འདས་ཀྱི་ཡང་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 1578]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། ཐུབ་པའི་བྱང་ཆུབ་ཀྱིས་ཐོབ་བྱ། །སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་ནི་འདི་ཟད་པ་མཁྱེན་པ་དང་དུས་མཉམ་དུ་བརྙེས༌[^711]སོ། །

[Block 1579]
སངས་རྒྱས་རྣམས་ཀྱི་ནི་སྦྱོར་བ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དེ། དེ་དག་གི་ཡོན་ཏན་འབྱོར་པ་མངོན་སུམ་དུ་འགྱུར་བ་ཐམས་ཅད་ནི་བཞེད་པ་ཙམ་ལ་རག་ལུས་པ་ཡིན་པས་དེ་ལྟ་བས་ན་དེ་དག་གི་ཐམས་ཅད་ནི། འདོད་ཆགས་དང་བྲལ་བས་བརྙེས་པ་ཡིན་ནོ། །

[Block 1580]
ད་ནི་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འགོག་པའི་སྙོམས་པར་འཇུག་པ་མ་བསྐྱེད་ན་ཟད་པ་མཁྱེན་པའི་དུས་སུ་གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བར་ཇི་ལྟར་འགྲུབ་ཅེ་ན། འགྲུབ་སྟེ། བསྐྱེད་ཟིན་པ་བཞིན་དུ་དེ་ལ་མངའ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
