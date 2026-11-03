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
[Block 1576]
གཡོགས་མ༌[^1099]ཅན་ཉིད་ལ་ཞེས་བྱ་བ་ནི་གཡོགས་པ་ཉིད་ལའོ། །

[Block 1577]
རོ་ཉིད་དག་ལ་ཞེས་བྱ་བ་ནི་བགྲོད་པར་བྱ་བ་ལའོ།[^1100] །མ་ཚོར་བ་དང་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པ་ལ་སོགས་པ་ལ་བཅུག་པ་ཉིད་ལའོ། །

[Block 1578]
རང་བཞིན་ཉམས་པའི་གནས་སྐབས་དང་མི་འདོད་བཞིན་དུ་བཅུག་པ་ཉིད་ནའོ་ཞེས་བྱ་བའི་ཡུལ་གྱི་བདག་གི་བ་མེད་པ་ཉིད་ལའོ། །

[Block 1579]
སྔར་ཕྱི་རོལ་དུ་དྲུད་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི་ཁ་དང་བཤང་བའི་ལམ་དག་ལ་ཕྱི་རོལ་ཏུ་དྲུད་པ་སྔོན་དུ་འགྲོ་བ་ཉིད་ཀྱིས་བཅུག་པ་ཉིད་ནའོ། །

[Block 1580]
ནང་དུ་མི་དབོ་བར་ཕྱི་རོལ་ཉིད་དུའོ་ཞེས་བྱ་བ་ལ། ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1581]
མི་མོ་ལ་རོ་གང་གིས་དེ་ཉིད་དུ་མི་ལ་ཕམ་པར་རིག་པ༌[^1101]ཞེས་བྱ་བ་ལ་སོགས་པ་དོགས་པ་ལ་དེ་བཟློག་པའི་དོན་དུ་ཚིག་འདིའོ། །

[Block 1582]
རོ་གཞན་མ་རྣམས་ནི་འདི་ཡིན་ཏེ། འདི་རྣམས་ཀྱི་ཕྱི་རོལ་གྱི་ངོ་བོ་འདི༌[^1102]ཙམ་སྟེ། འདིར་བསྟན་པ༌[^1103]ལམ་རྫོགས་པ་ཉིད༌[^1104]དེ། དེ་བས་ན་འདིར་ན་སྨད་པ་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 1583]
མ་བསྲུངས་པར་ཉིན་མོ་གློས༌[^1105]ཕབ་སྟེ་གཉིད་ལོག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། གང་གིས་འདི༌[^1106]བསྲུངས་པའི་སྒྲར་བརྗོད་དོ། །

[Block 1584]
བསྲུངས་པ་དེ་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་བསྲུངས་པ་ནི་གསུམ་སྟེ། སྒོ་བཅད་ཅིང་ཀུན་ནས་བསྐོར་བ་ན་གནས་པ་ཉིད་ཅེས་བྱ་བ་སྨོས་ཏེ། སྒོ་བཅད་ཅིང་ཀུན་ནས་བསྐོར་བ་ན་ཐམས་ཅད་ནས་ཀུན་དུ་བསྐོར་བའི་གནས་ལ་གནས་པ་ན་སྒོ་བཅད་ཅིང་ཀུན་ནས་བསྐོར་བ་ན་གནས་པའོ། །

[Block 1585]
དེའི་དངོས་པོ་ནི་དེ་ཉིད་དེ་ཀུན་ནས་བསྲུངས་པ༌[^1107]ཉིད་དོ། ། སུས་ཤེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་ཀུན་ནས་བསྲུངས་པ་ཉིད་དང་། ཤམ་ཐབས་ཀྱི་མཐའ་བཅིངས་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1586]
མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་རྣམ་པར་འབྱེད་པ་སྟེ་ཕམ་པ་དང་པོའི་རྣམ་པར་འབྱེད་པ་རྫོགས་སོ།། །།

[Block 1587]
གང་དུ་བུད་མེད་ཀྱིས་བརྔོད༌[^1108]པ་དེར་འགྲོ་བར་མི་བྱའོ། །

[Block 1588]
གང་དུ་མི་མ་ཡིན་པས་གནོད་པའི་ཕྱིར་བརྩལ་བ་དེར་གནས་པར་མི་བྱའོ། །

[Block 1589]
འདོད་ཆགས་ཤས་ཆེ་བས་འཛག་སྣོད་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འཛག་སྣོད་ཅེས་བྱ་བ་རགས་པ༌[^1109]འདིའི་དོན་དུ་འདི་ཞེས་བྱ་བ་ཁུ་བ་འཛག་པར་གྱུར་ན་འདི་མངོན་པར་གནང་བ་སྟེ། རྫས་ཅི་ཞིག་ལས་བྱ་ཞེ་ན། དེའི་ཕྱིར་རའམ་རི་དགས་སམ་བྱི་བའི་པགས་པ་ལས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1590]
པགས་པ་འདི་རྣམས་ནི་དཔེ་ཡིན་ཏེ། སྤང་བར་བྱ་བ་མ་ཡིན་པ་ལ་འཇིག་རྟེན་པ་རྣམས་ཀྱིས་མི་བྱེད་ཅིང་སེང་གེའི་པགས་པ་བཞིན་དུ་ཉེས་དམིགས་སོ། །ཅིའི་པགས་པ་ལས་བྱ་ཞེ་ན། དེའི་ཕྱིར་བྱི་བ༌[^1110]དང་ལུག་ལྤགས་ལ་སོགས་པ་ཡང་འདིས་འཕངས་པའོ། །

[Block 1591]
དྲི་མི་ང་བར་བྱ་བའི་ཕྱིར་སྐབས་སུ་བཀྲུ་བའམ་བསྐམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དྲི་མི་ང་བར་བྱ་བའི་དོན་དུ་ཞེས་བྱ་བའོ། །

[Block 1592]
དེའི་དུས་ཀྱི་ཆེད་དུ་གཞན་བྱའོ་ཞེས་བྱ་བ་ནི་འཛག་སྣོད་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1593]
དེའི་དུས་ཀྱི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་བཀྲུ་བ་དང་བསྐམ་པའི་དུས་ཀྱི་དོན་དུ་སྟེ། འཛག་སྣོད་གཉིས་པ་བཅང་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1594]
ཁུ་བ་ཧ་ཅང་མང་བས་ལྡར་བར༌[^1111]གྱུར་ན་ཕྲུ་བླུགས་སོ་ཞེས་སྨོས་ན་ཕྲུ་ཅི་འདྲ་བ་བླུགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་བྱེ་མའམ་སའིའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1595]
ཟན་ཟ་བ་དང་མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བའི་ཚེ་ཕོག་ལ་བཀྲུས་ཏེའོ་ཞེས་བྱ་བ་ལ། ཕོག་ལ་ཞེས་བྱ་བ་ནི་འཛག་སྣོད་དེ་དབང་པོ་ལས་བསལ་བར་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1596]
དེ་ནས་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར་བཀྲུས་ཏེ་ཟན་ཟ་བ་དང་མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བ་ཞེས་བྱ་བ་སྨོས་ཏེ་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷག་མའོ། །

[Block 1597]
མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་ལས་ཕྲན་ཚེགས་ཀྱི་སྐབས་རྫོགས་སོ།། །།

[Block 1598]
རྨའི་སྒོ་གསུམ་རྣམས་ལས་ཕྱོགས་གང་ཕམ་པར་བྱེད་པ་ཉིད་ལ་དང་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཁའི་དང་པོ་ནི་སོ་ཕན་ཆད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོའི་ནང་ལོགས་ཀྱི་ངོས་ཀྱི་སོའི་མཐར་ཐུག་པ་སྟེ་དེ་ཕན་ཆད་ནི་ཁའི་དང་པོའོ། །

[Block 1599]
བཤང་བའི་ལམ་གྱི་ནི་བུ་གའི་སྦུབས་ཀྱི་མཐའ་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་བུ་གར་གྱུར་པའི་སྦུབས་ཡིན་པས་བུ་གའི་སྦུབས་ཏེ་གཙང་མའི་རྩ་སྟེ་དེ་ལའོ། །

[Block 1600]
དེ་ནས་བརྩམས་ཏེ་བཤང་བའི་ལམ་གྱི་དང་པོའོ། །

[Block 1601]
གང་ནས་བརྩམས་ཏེ་བྱ་ཞིང་གནོད་པ་དང་བཅས་པའི་ནད༌[^1112]ཡོད་པ་གང་ནས་འབྱུང་ཞིང་རྨའི་སྒོའི་མིག་དང་འདྲ་བ་སླར་དགའ་བས་འཇུག་པར་བྱ་བ་མ་ཡིན་པ་ཡོད་པ་དེ་ནི་མཐའ་མ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1602]
ཟག་བྱེད་ཀྱི་ནི་པགས་རིམ་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་དུ་གྲངས་གཅིག་པ་གཉིས་ཀའི་རིམ་པ་སྟེ། དེ་ལས་གཞན་ནི་པགས་རིམ་ཡན་ཆད་ཤའི་རྣམ་པའི་དང་པོར་གྱུར་པ་རྡུལ་ཕྲ་རབ་ཀྱི་མཚམས་ལ་ཐུག་པ་ནི་དང་པོ་སྟེ། དེ་ལས་གཞན་པ་ནི་ཟག་བྱེད་ཀྱི་དང༌[^1113]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1603]
དེར་ནོར་བུ་བཅུག་པ་ཉིད་ནི་དེའི་མཐའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་ཟག་བྱེད་ཀྱིའོ། །

[Block 1604]
ནོར་བུའི་གང་ཞིག་བཅུག་པ་ཉིད་ནི་དེའི་མཐའ་སྟེ་བཅུག་པའི་མཐའ་མའོ། །

[Block 1605]
ཐམས་ཅད་ལས་ཆུང་བ་བཅུག་པ་ཉིད་དེ་ནོར་བུ་རིལ་གྱིས་མ་འདས་མོད་ཀྱི། འོན་ཀྱང་གང་གིས་བཅུག་པའི་རེག་པ་ཉམས་སུ་མྱོང་བར་བྱས་པ་ཞེས་བྱ་བ་དེས་བཅུག་པ་བསྟན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1606]
འདིར་གཞུང་ནི། སོ་དག་ལས་ནོར་བུ་འདའ་བར་བྱེད་པ་དང་། བུ་གུའི་སྦུབས་ལས་ནོར་བུ་འདའ་བར་བྱེད་པ་དང་། པགས་པ་ལས་ནོར་བུ་འདའ་བར་བྱེད་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1607]
སོ་དག་ཅེས༌[^1114]བྱ་བ་འདི་ནི་སོ་རྣམས་ལས་ཞེས་བྱ་བ་འདི་ལ་ཟུར་ཆག་པའི་སྒྲ་ཞེས་བྱ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 1608]
རྣམ་པར་འབྱེད་པའི་མདོ་ལས།

[Block 1609]
གང་ཞིག་རྨའི་སྒོ་ཉིད་རྣམས་ལ་ཉམས་པ་ཉིད་སྨྲས་པ་དེའི་མཚན་ཉིད་བརྗོད་པར་བྱ་སྟེ། ཕྱོགས་ཀྱི་དང་པོ་ཅུང་ཟད་ཟིན་པ་ཉིད་དང་སུངས་པ་ཉིད་དང༌[^1115]རུལ་བ་ཉིད་དང་མྱགས་པ་ཉིད་དང་སྲོག་ཆགས་དག་གིས་ཟོས་པ་ཉིད་ལྟ་བུ༌[^1116]ཉམས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། གང་གི་རྨའི་སྒོ་རྣམས་མ་ཟིན་པའམ་ཟིན་པར་གྱུར་པ་རྣམས་ཀྱང་རུལ་བ་དང་སུངས་པ་ཞེས་བྱ་བ་འདི་གཞུང་འདི་ལ་ཕྱོགས་འདི་ནི་མ་བརྟེན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1610]
ཕྱོགས་ཀྱི་དང་པོ་ཞེས་བྱ་བ་འདི་སྨོས་པ་ཡིན་ནོ། །

[Block 1611]
གཞུང་གཞན་ལས་ཅུང་ཟད་ཟིན་ཏམ། སྐྲངས་པ་ཉིད་དམ། རུལ་བ་ཉིད་དམ། སྲོག་ཆགས་དག་གིས་ཟོས་པ་ཉིད་དམ་ཞེས་གསུངས་པ་སྟེ། དེ་ལ་འདིར་སྐྲངས་པ་དང་སྲོག་ཆགས་རྣམས་ཀྱིས་ཟིན་པའི་ཚིག་བྱས་པ་ཡིན་ནོ། །

[Block 1612]
འདིར་ཅུང་ཟད་ཟིན་པས་ནི་མ་ཟིན་པ་ཤེས་པར་བྱའོ། །

[Block 1613]
ལྷག་མ་ནི་གོ་སླ་བ་ཉིད་ཀྱི་ཕྱིར་རྒྱས་པར་མ་བཤད་དོ། །

[Block 1614]
རྨའི་སྒོ་ལ་བརྟེན་པའི་ཕྱོགས་འདི་བཟུང་བ་ཡིན་གྱི་གཞན་གྱི་ལུས་ལ་བརྟེན་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1615]
བགྲོད༌[^1117]པར་བྱ་བ་ཕྱེད་བཅད་པ་ཉིད་ལ་ཡང་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་བགྲོད་པར་བྱ་བའི་ཚིག་གིས་གནས་མ་ལུས་པ་བཟུང་བ་སྟེ། རྨའི་སྒོ་ཙམ་ལ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
