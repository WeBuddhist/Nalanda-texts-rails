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
[Block 1471]
སོ་སོར་བརྟགས་པས་འགོག་པའི་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་ཡིན་ལ། ཟག་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 1472]
ལམ་གྱི་བདེན་པའི༌[^646]ཟག་པ་མེད་པ་ཉིད་དོ། །

[Block 1473]
དེ་ནི་མདོར་བསྡུས་ཏེ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 1474]
སློབ་པའི་ཆོས་རྣམས་ཀྱི་ཐོབ་པ་ནི་སློབ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1475]
མི་སློབ་པ་རྣམས་ཀྱི་ནི་མི་སློབ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1476]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་བྱེ་བྲག་ཡོད་པས་དེ་བསྟན་པར་བྱ་སྟེ། སློབ་དང་མི་སློབ་མིན་གྱི་གསུམ། །སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པའི་ཆོས་ཞེས་བྱ་བ་ནི་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་དང་། འདུས་མ་བྱས་སོ། །

[Block 1477]
དེ་དག་གི་ཐོབ་པ་ནི་སློབ་པ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གསུམ་སྟེ། རེ་ཞིག་ཟག་པ་དང་བཅས་པ༌[^647]རྣམས་དང་། སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་དང་། འཕགས་པ་མ་ཡིན་པས་ཐོབ་པ་སོ་སོར་བརྟགས་པས་འགོག་པའི་ཐོབ་པ་ནི་སློབ་པ་ཡང་མ་ཡིན༌[^648]མི་སློབ་པ་ཡང༌[^649]མ་ཡིན་ནོ། །

[Block 1478]
དེ་ཉིད་སློབ་པའི་ལམ་གྱིས་ཐོབ་པའི་ནི་སློབ་པའོ། །

[Block 1479]
མི་སློབ་པའི་ལམ་གྱི་ས་ཐོབ་པའི་ནི་མི་སློབ་པའོ། །

[Block 1480]
མཐོང་བ་དང་བསྒོམ་པས༌[^650]སྤང་བར་བྱ་བ་རྣམས་ནི༌[^651]ཐོབ་པ་ནི་རིམ་པ༌[^652]བཞིན་དུ་མཐོང་བས༌[^653]དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 1481]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་བྱེ་བྲག་ཡོད་པས་དེ་བསྟན་པར་བྱ་བ༌[^654]སྟེ། སྤང་བྱ་མིན་པའི་རྣམ་གཉིས་འདོད། །སྤང་བར་བྱ་བ་མ་ཡིན་པའི་ཆོས་དག་ནི་ཟག་པ་མེད་པ་རྣམས་ཏེ། དེ་དག་ལས་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་དང་། འཕགས་པ་མ་ཡིན་པས་ཐོབ་པ༌[^655]སོ་སོར་བརྟགས་པས་འགོག་པའི་ཐོབ་པ་ནི་བསྒོམ་པས་སྤང་བར་བྱའོ། །

[Block 1482]
དེ་ཉིད་འཕགས་པའི་ལམ་གྱིས་ཐོབ་པའི་དང་། ལམ་གྱི་བདེན་པ༌[^656]ནི་ཟག་པ་མེད་པ་སྟེ་སྤང་བར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 1483]
དུས་གསུམ་པའི་རྣམ་པ་གསུམ་ཞེས་སྤྱིར་བསྟན་པ་གང་ཡིན་པ་དེའི་དམིགས་ཀྱིས་བསྟན་པ་ནི་འདི་ཡིན་ཏེ། ལུང་བསྟན་མིན་ཐོབ་ལྷན་ཅིག་སྐྱེ། །མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་སྟོབས་ཆུང་བའི་ཕྱིར་ལྷན་ཅིག་སྐྱེ་བ་ཁོ་ན་སྟེ། སྔར་སྐྱེ་བ་ཡང་མེད་ལ་དུས་ཕྱིས་སྐྱེ་བ་ཡང་མེད་དོ། །

[Block 1484]
དེས་ན་དེ་དག་གི་ནི་འདས་པ་རྣམས་ཀྱི་ཡང་འདས་པ་ཁོ་ན་ཡིན་ལ། ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་བར་དུ་ཡང་ད་ལྟར་བྱུང་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 1485]
ཅི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཐམས་ཅད་ཀྱི་དེ་དང་འདྲ་འམ་ཞེ་ན། མངོན་ཤེས་སྤྲུལ་པ་མ་གཏོགས་པ། །ཐམས་ཅད་ཀྱི་དེ་དང་མི༌[^657]འདྲ་སྟེ། མངོན་པར་ཤེས་པ་ལུང་དུ་མ་བསྟན་པ་གཉིས་དང་། སྤྲུལ་པའི་སེམས་མ་གཏོགས་པའོ། །

[Block 1486]
དེ་དག་ནི༌[^658]སྦྱོར་བའི་ཁྱད་པར་གྱིས་འགྲུབ་པས་སྟོབས་དང་ལྡན་པའི་ཕྱིར་སྔར་དང་ཕྱིས་དང་ལྷན་ཅིག་ཏུ༌[^659]སྐྱེ་བ་ཡང་ཡོད་དོ། །

[Block 1487]
བཟོའི་གནས་པ་ཁ་ཅིག་དང་། སྤྱོད་ལམ་པ་ཤིན་ཏུ་གོམས་པ༌[^660]ཡང་འདོད༌[^661]དོ། །

[Block 1488]
ཅི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ༌[^662]བསྟན་པ་ཁོ་ནའི་ཐོབ་པ་ལ༌[^663]ལྷན་ཅིག་སྐྱེ་བ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། བསྒྲིབས་པའི་གཟུགས་ཀྱིའང་། གཟུགས་ཀྱི་རྣམ་པར་རིག་བྱེད་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་ཐོབ་པ་ཡང་ལྷན་ཅིག་སྐྱེ་བ་ཁོ་ན་སྟེ། ཆེན་པོས་ཀྱང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མི་སློབ་པས༌[^664]སྟོབས་ཆུང་བས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1489]
[^665]ཇི་ལྟར་ལུང་དུ་མ་བསྟན་པའི་ཆོས་རྣམས་ཀྱི་ཐོབ་པའི་བྱེ་བྲག་འདི་ཡིན་པ་ལྟར་དགེ་བ་དང་མི་དགེ་བ་རྣམས་ཀྱི་ཐོབ་པ་ལ་ཡང་བྱེ་བྲག་འགའ་ཞིག་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། ཡོད་དེ། འདོད་པ་ན། གཟུགས་ཀྱི་སྔར་ནི་སྐྱེ་བ་མེད། །འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་ཐོབ་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་སྔར་སྐྱེ་བ་མེད་དོ།[^666] །ལྷན་ཅིག་སྐྱེ་བ་དང་། དུས་ཕྱིས་སྐྱེ་བ་ནི་ཡོད་དོ། །

[Block 1490 [HEADING]]
#### མ་ཐོབ་པ། ^2-3-2-0

[Block 1491]
ཅི་མ་ཐོབ་པ་ཡང་ཐོབ་པ་བཞིན་དུ་རྣམ་པའི་བྱེ་བྲག་ཡོད་དམ། སྨྲས་པ་མེད་དོ། །

[Block 1492]
འོ་ན་ཅི་ལྟ་བུ༌[^667]ཞེ་ན། མ་ཐོབ་མ་བསྒྲིབས་ལུང་མ་བསྟན། །མ་ཐོབ་པ་ཐམས་ཅད་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1493]
དུས་ཀྱི་བྱེ་བྲག་གིས་ནི། འདས་མ་སྐྱེས་ཀྱི་དེ་རྣམ༌[^668]གསུམ། །ད་ལྟར་བྱུང་བའི་མ་ཐོབ་པ་ད་ལྟར་བྱུང་བ་ནི་མེད་དོ། །

[Block 1494]
འདས་པ་དང་མ་འོངས་པ་དག་གི་ནི་དུས་གསུམ་པ་མ༌[^669]ཡིན་ནོ། །

[Block 1495]
འདོད་སོགས་གཏོགས་དང་དྲི་མེད་ཀྱིའང་། །རྣམ་གསུམ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདོད་པར་གཏོགས་པ་རྣམས་ཀྱི་ནི་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན༌[^670]སྤྱོད་པ་ཡིན་ལ། གཟུགས་དང་གཟུགས་མེད་པར་གཏོགས་པ༌[^671]རྣམས་དང་། མ་གཏོགས་པ་རྣམས་ཀྱི་ཡང་དེ་དང་འདྲའོ། །

[Block 1496]
མ་ཐོབ་པ་ཟག་པ་མེད་པ་ནི་འགའ་ཡང་མེད་དེ། འདི་ལྟར། ལམ་མ་ཐོབ་པ་སོ་སོ་ཡི། །སྐྱེ་བོར་འདོད་དོ། །

[Block 1497]
བསྟན་བཅོས་ལས།

[Block 1498]
སོ་སོའི་སྐྱེ་བོ་ཉིད་གང་ཞེ་ན། འཕགས་པའི་ཆོས་རྣམས་ཀྱི་མ་རྙེད་པའོ་ཞེས་འདོན་ཏེ། གལ་ཏེ་མ་རྙེད་པ་ཞེས་བྱ་བ་མ་ཐོབ་པ་ཡིན་པས་སོ་སོའི་སྐྱེ་བོ་ཉིད་ནི་ཟག་པ་མེད་པ་ཡིན་པར་མི་འོས་སོ། །

[Block 1499]
འཕགས་པའི་ཆོས་གང་དག་གི་མ་རྙེད་པ་ཡིན་ཞེ་ན། ཐམས་ཅད་ཀྱི་ཡིན་ཏེ། ཁྱད་པར་མེད་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1500]
དེ་ནི་རྙེད་པ་མེད་པར་མ་རྙེད་པ་གང་ཡིན་པ་སྟེ། དེ་ལྟ་མ་ཡིན་ན་སངས་རྒྱས་ཀྱང་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་རིགས་ཅན་དག་དང་མི་ལྡན་པའི་ཕྱིར་དང༌[^672]འཕགས་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1501]
འོ་ན་ནི་ཁོ་ན་ཞེས་བྱ་བའི་སྒྲ་འདོན༌[^673]དགོས་སོ། །

[Block 1502]
གདོན་མི་དགོས་ཏེ། ཚིག་གཅིག་པུ་དག་ཀྱང་ངེས་པར་འཛིན་པ་ཡིན་ཏེ། དཔེར་ན་ཆུ་འཐུང་བའོ། །

[Block 1503]
རླུང་ཟ་བའོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1504]
གཞན་དག་ན་རེ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་དེ་དག་ལྷན་ཅིག་འབྱུང་བ་རྣམས་ཀྱི་འོ་ཞེས་ཟེར་རོ། །

[Block 1505]
དེ་དག་བཏང་བས་འཕགས་པ་མ་ཡིན་པ་ཉིད་དུ་ཐལ་བར་ཡང་མི་འགྱུར་ཏེ། [^674]དེ་དག་གི་མ་རྙེད་པ་གཏན་དུ་བཅོམ་པའི་ཕྱིར་རོ། །

[Block 1506]
འོ་ན་ནི་དེ་དག་ཀྱང་རིགས་གསུམ་པ་ཡིན་ན་གང་དག་གི་མ་རྙེད་པ་ཡིན། ཐམས་ཅད་ཀྱི་ཡིན་ནོ། །

[Block 1507]
འོ་ན་ནི་ཉེས་པ་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1508]
ལན་ཡང་དེ་ཉིད་ཡིན་ནོ། །

[Block 1509]
འོ་ན་ནི་འབད་པ་དོན་མེད་པར་འགྱུར་བས་མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ་བ་དེ་ལྟ་བུ་ནི་ལེགས་པ་ཡིན་ནོ། །

[Block 1510]
མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ་བུ་ཡིན། འཕགས་པའི་ཆོས་རྣམས་མ་སྐྱེས་པའི་རྒྱུད༌[^675]ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
