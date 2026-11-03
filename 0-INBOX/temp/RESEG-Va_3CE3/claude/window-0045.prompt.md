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
གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ཤིན་ཏུ་མེད་པའི་ཕྱིར་ཆོས་དེ་རྣམས་མཚན་མར་བཟུང་སྟེ་གོ་ཆ་འདིས་བགོས་པ་ནི་མ་ཡིན་གྱི། མཚན་མ་མེད་པའི་གོ་ཆ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 1577]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ས་མཚམས་བཅད་དེ་སེམས་ཅན་གྱི་དོན་དུ་གོ་ཆ་བཙལ་བ༌[^1101]མ་ལགས་སོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་འདི་སྙེད་ཅིག་མྱ་ངན་ལས་འདའ་འོ༌[^1102]ཞེས་བྱ་བར་ཡོངས་སུ་ངེས་པའི་མཚམས་བཅད་པ་གང་ཡང་མེད་དོ། །

[Block 1578]
སུས་ཀྱང་བསྒོམ་པར་མི་བགྱིའོ༌[^1103]ཞེས་བྱ་བ་ནི་བྱེད་པ་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1579]
གང་དུ་བསྒོམ་པར་མི་བགྱི་ཞེས་བྱ་བ་ནི་ཆོས་གང་ལས༌[^1104]བསྒོམ་པར་བྱ་བ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1580]
ཇི་ལྟར་ཡང་བསྒོམ་པར་མི་བགྱི་ཞེས་བྱ་བ་ནི་བསྒོམ་པའི་ཡིད་ལ་བྱེད་པ་ཡང་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1581]
དེ་ནི་བསྒོམ་པ་རྣམ་པར་འཇིག་པའོ་ཞེས་བྱ་བ་ནི་བསྒོམ་པ་མེད་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1582 [HEADING]]
##### ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡོངས་སུ་བརྟག་པ། ^1-2-5-18-0

[Block 1583]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ལ་ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཡོངས་སུ་བརྟག་པར༌[^1105]བྱའོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདིས། འདི༌[^1106]ཕྱིར་མི་ལྡོག་པ་ཡིན་ནམ། འོན་ཏེ་མ་ཡིན་ཞེས་ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་བརྟག་པར་བྱ་བའོ། །

[Block 1584]
དེའི་འོག་ཏུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ལ་མངོན་པར་ཞེན་པ་མེད་དམ་ཞེས་བྱ་བ་ནི་བརྟགས༌[^1107]པའི་མཚན་མ་སྟོན༌[^1108]སྟེ། བྱང་ཆུབ་སེམས་དཔའ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་ཞེས་བྱ་བ་ནས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བར་དང་། སྟོང་པ་ཉིད་ཐམས་ཅད་དང་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པའི་མཐར༌[^1109]ཐུག་པའི་བར་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་བར་དུ་བཤད་པ་ན་དེ་ལ་མངོན་པར་ཞེན་པ་མི་སྐྱེད༌[^1110]ཅིང་མི་གནས་ན་བྱང་ཆུབ་སེམས་དཔའ༌[^1111]ནི་ཕྱིར་མི་ལྡོག་པ་ཡིན་ནོ་ཞེས་ཡོངས་སུ་བརྟག་པར་བྱའོ། །

[Block 1585]
ལ་ལ་རང་བཞིན་གྱིས་གཞན་གྱིས་སྨྲས་པ་ལ་སྙིང་པོར་འདུ་ཤེས་མི་སྐྱེད༌[^1112]དོ། །

[Block 1586]
ལ་ལ་དད་པར་མི་འགྱུར་རོ། །

[Block 1587]
ལ་ལ་དེ་ལ་ཆགས་པར་མི་འགྱུར་རོ། །

[Block 1588]
ཞེ་སྡང་བར་མི་འགྱུར་གྱི་བཏང་སྙོམས་སུ་གནས་པར་འགྱུར་རོ། །

[Block 1589]
ལ་ལ་རང་བཞིན་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་མ་བྲལ་བ་ཡིན་ནོ། །

[Block 1590]
ལ་ལ་ཆོས་ཟབ་མོ་ཐོས་ན་སྐྲག་པ་ལ་སོགས་པར་མི་འགྱུར་གྱི་གོང་ནས་གོང་དུ་མངོན་པར་དགའ་ཞིང་ཉན་པར་འགྱུར་བ་དང་འཛིན་པ་དང་། འཆང་བར་འགྱུར་ཏེ། ཡོན་ཏན་དེ་རྣམས་དང་ལྡན་ན་ཕྱིར་མི་ལྡོག་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1591]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་རྣམ་པར༌[^1113]བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མངོན་པར་རྟོགས་པའི་དུས་ན་ལྷག༌[^1114]མཐོང་གིས་རྣམ་པར་བརྟག་པའོ། །

[Block 1592]
སྟོང་པ་ཉིད་ལ་གཞོལ་བ་དང་། སྟོང་པ་ཉིད་ལ་འབབ་པ་དང་། སྟོང་པ་ཉིད་ལ་བབ་པས༌[^1115]ཞེས་བྱ་བ་ནི་ཆུང་ངུ་དང་འབྲིང་པོ་དང་ཆེན་པོའི་དབང་གིས་ཚིག་གསུམ་མོ། །

[Block 1593]
སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་དང་སྨོན་པ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པ་ལ་སོགས་པའི་ཆོས་ཉིད་ཀྱིས་མངོན་པར་རྟོགས་པར་བྱས་ནས་རྣམ་པར་བརྟག་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1594]
དེ་སྐད་ཅེས་བཀའ་སྩལ་པ་དང་། གནས་བརྟན་རབ་འབྱོར་གྱིས། བཅོམ་ལྡན་འདས་དེ་ལྟར་སྟོང་པ་ཉིད་ལ་གཞོལ་བའི་བསམ་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ལ་རྟོག་པར་འགྱུར་བ་དེ་བཞིན་དུ༌[^1116]གཟུགས་དང་ཚོར་བ་དང་འདུ་ཤེས་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱང་དེ་ལྟར་བརྟག་པར་བགྱི་འམ། འོན་ཏེ་མི་བགྱི་ཞེས༌[^1117]ཞུས་པ། བཅོམ་ལྡན་འདས་ཅི་གཟུགས་ལ་རྟོག་པ་ལགས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1595]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ནི་གཟུགས་ལ་རྟོག༌[^1118]པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྟོན་ཏེ་མངོན་པར་རྟོགས་པའི་ཚེ་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་མེད་པའི་ཕྱིར་སྣང་བར་མི་འགྱུར་རོ། །

[Block 1596]
དེ་བས་ན་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི་ཆོས་རྣམས་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱིས༌[^1119]མཐར་ཐུག་པ༌[^1120]རྣམས་ཀྱིས་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ནི་མེད་ཀྱི། དེ་དག་གི་དེ་བཞིན་ཉིད་མངོན་པར་རྟོགས་པར་འགྱུར་རོ། །

[Block 1597]
དེ་བཞིན་ཉིད་དེ་ཡང་ཐ་དད་པ་མ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ༌[^1121]ཉིད་ཀྱང་གཅིག་གོ། །

[Block 1598]
དེ་བས་ན་དེ་བཞིན་ཉིད་གཅིག་པའི་ཕྱིར་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་བརྟག་པ༌[^1122]མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1599]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ནི་སུས་ཀྱང་མ་བྱས། འགྱུར་བར་མ་བྱས། གང་ནས་ཀྱང་མ་འོངས། གང་དུ་ཡང་མ་སོང་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྟོན་ཏེ། གལ་ཏེ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་བྱ་བ་དང་འགྱུར་བའི་ཆོས་སམ། འོང་བ་དང་འགྲོ་བ་དང་། གནས་པ་དང་ལྡན་པའམ། ཉི་ཚེ་བའམ། གྲངས་ལ་སོགས་པ་དང་ལྡན་ན་ནི། ཀུན་བརྟགས་པའི་རྣམ་པར་འགྱུར་ཏེ། འོ་ན་ནི་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་སུ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་འགྱུར་བ་ཞིག་ན་གང་གི་ཕྱིར་དེའི་རྣམ་པ་དང་བྲལ་ཏེ། ནམ་མཁའི་ཆོས་ཅན་ཡིན་པ་དེའི་ཕྱིར་དེ་གཟུགས་ལ་སོགས་པར་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་ནུས་སོ། །

[Block 1600]
ལྷ་རྣམས་ཀྱིས་ཆོས་ཟབ་མོ་དེ་ལྟ་བུ་ཐོས་ནས། བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་པོ༌[^1123]ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1124]མངོན་པར་བསྔགས་ནས་དེ་བཞིན་ཉིད་དེ་ཉིད་དོན་ཐ་དད་པ་མེད་པར་སྨྲས་སོ། །

[Block 1601]
གང་ལ་གཉིས་ཀུན་དུ་རྒྱུ་བ་མེད་པ་དེ་ནི་ཆོས་རྣམས་ཀྱི་ཟབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་ཀྱི་བདག་ཉིད་ཡིན་ལ། དེ་བཞིན་ཉིད་ཀྱང་གཅིག་པའི་ཕྱིར་གཅིག༌[^1125]རྒྱུ་བར་འགྱུར་གྱི། གཉིས་སུ་རྒྱུ་བར་མི་འགྱུར་རོ། །

[Block 1602]
ནམ་མཁའ་ཟབ་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྔར་བསྟན་པ་ཉིད་དོ། །

[Block 1603]
ཆོས་འདི་ནི་གཟུགས་གཟུང་བའི༌[^1126]སླད་དུ་བསྟན་པ་མ་ལགས། མི་གཟུང་བའི་སླད་དུ་ཡང་མ་ལགས་ཞེས་བྱ་བ་ནི། འདི་གཟུགས་སོ༌[^1127]ཞེས་མཚན་མར་འཛིན་པ་ནི་གཟུང་བའོ། །

[Block 1604]
གཟུགས་མེད་དོ་ཞེས་རྣམ་པ་ཐམས་ཅད་དུ་སྐུར་པ་འདེབས་པ་ནི་མི་གཟུང༌[^1128]བའོ། །

[Block 1605]
གཟུགས་ལ་ཐོགས་པ་མ་མཆིས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་ཐམས་ཅད་དང་རྗེས་སུ་མཐུན་པ་ཉིད་རྣམ་པར་བྱེད་དེ་གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་ལ་སྒྲོ་འདོགས་པ་དང་སྐུར་པ་འདེབས་པའི་མཐའ་མེད་པའི་ཕྱིར་ཐོགས་པ་མེད་པ༌[^1129]འདི་ལྟར་ཀུན་བརྟགས་པའི་གཟུགས་ནི་ཡོད་པ་མ་ཡིན་པས་སྒྲོ་འདོགས་པའི་མཐའ་མེད་དོ། །

[Block 1606]
ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་ཡོད་པའི་ཕྱིར་སྐུར་པ་འདེབས་པ་མེད་དེ། དེ་བས་ན་གཟུགས་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 1607]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1608 [HEADING]]
##### དེ་བཞིན་གཤེགས་པའི་རྗེས་སུ་སྐྱེས་པ། ^1-2-5-19-0

[Block 1609]
[^1130]གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ནི༌[^1131]མ་འོངས་མ་སོང་བ་སྟེ། དེ་བཞིན་དུ༌[^1132]རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་མ་འོངས་མ་སོང་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་དེ༌[^1133]བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་དང་། རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་མཉམ་པ་ཉིད་དུ་སྟོན་ཏེ། [^1134]རྗེས་སུ་སྐྱེས་པ་ཡིན་པར་བསྒྲུབ་པའི་ཕྱིར་མ་འོངས་མ་སོང་ཞེས་བྱ༌[^1135]སྨོས་ཏེ། གང་ནས་ཀྱང་མ་འོངས། གང་དུ༌[^1136]ཡང་མ་སོང་བའོ། །

[Block 1610]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ཉིད་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་དེའོ། །

[Block 1611]
ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ནི་རབ་འབྱོར༌[^1137]དེ་བཞིན་ཉིད་ཀྱང་དེའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་གཅིག་པའི་ཕྱིར་གཅིག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1612]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གནས་པ་ཞེས་བྱ་བ་ནི་ཆོས་གནས་པའི་མཚན་ཉིད་དུ་ཡང་གཅིག་གོ་ཞེས་སྟོན༌[^1138]ཏོ། །

[Block 1613]
འགྱུར་བ་མེད་ཅིང་རྣམ་པར་རྟོག་པ་མེད་ཅེས་བྱ་བ་ལ། འགྱུར་བ་མེད་ཅེས་བྱ་བ་འདིས་ནི་མི་འགྱུར་བའི་ཡོངས་སུ་གྲུབ་པས་ཡོངས་སུ་གྲུབ་པར་སྟོན༌[^1139]ཏོ། །

[Block 1614]
རྣམ་པར་རྟོག་པ་མེད་ཅེས་བྱ་བ་འདིས་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པས་ཡོངས་སུ་གྲུབ་པར་སྟོན་ཏོ། །

[Block 1615]
ཅི་ལ་འང་ཐོགས་པ་མེད་པ༌[^1140]ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་པ་སྟེ། གང་ན་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
