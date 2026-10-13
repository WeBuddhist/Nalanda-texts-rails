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
དེ་ལྟ་ན་པདྨ་ལྟ་བུ་ལ་སོགས་པའི༌[^1090]བསྐྱེད་པའི་རིམ་པ་གཅིག་པུའི་སྣོད་ཡིན་པས་རྫོགས་པའི་རིམ་པ་ལྔ་པོའི༌[^1091]ཕྱིར་སྒོམ་པར་བྱེད་ཅེ་ན། སྨྲས་པ། དྲང་བའི་དོན་དུ་ཡང་རྫོགས་པའི་རིམ་པ་གསུངས་པས་ཀུན་གྱིས༌[^1092]བསྒོམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1542]
དེ་བས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་གཞན་དུ་གསུངས་ཏེ།

[Block 1543]
དེ་སྐད་དུ་སྤྱོད་པ་བསྡུས་པའི་སྒྲོན་མ་ལས།

[Block 1544]
རྡོ་རྗེ་སློབ་མས་གསོལ་བ། བདག་ཅག་ལྟ་བུའི་སོ་སོའི་སྐྱེ་བོ་ཐོག་མ་མེད་པ་ནས་ཕྱི་རོལ་གྱི་དངོས་པོ་རྣམ་པ་སྣ་ཚོགས་པ་ལ་མངོན་པར་ཞེན་པས་ཡོད་པ་དང་མེད་པ་དང་གཅིག་པ་དང་དུ་མ་དང་། གཉིས་དང་གཉིས་མ་ཡིན་པ་དང་། ཡོད་པ་མ་ཡིན༌[^1093]མེད་པའང་མ་ཡིན་པ་རྟག་པ༌[^1094]དང་མི་རྟག་པ་ལ་སོགས་པའི་རང་བཞིན་གྱི་བག་ཆགས་ཀྱི་རྒྱུས་རྣམ་པར་རྟོག་པ་ལ་མངོན་པར་ཞེན་པ་ལ་མ༌[^1095]ཞུགས་པ་རྣམས་ཀྱིས་རྫོགས་པའི་རིམ་པའི་གོ་རིམས་ཀྱི༌[^1096]ཏིང་ངེ་འཛིན་ལ་སློབ་པ་ན། གོ་རིམས༌[^1097]ཇི་ལྟ་བ་བཞིན་དུ་བསླབ་པར་བགྱི་བའམ་ཡང་ན་བླ་མའི་མན་ངག་ཙམ་གྱིས་དེ་དག་སྐད་ཅིག་ཙམ་གྱིས་སོ་སོར་སྣང་བར་བགྱི། རྡོ་རྗེ་སློབ་དཔོན་གྱིས་སྨྲས་པ། རིམ་གྱིས་འཇུག་པ་ལ་སློབ་པར༌[^1098]བྱའི་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1545]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལང་ཀར་གཤེགས་པའི་མདོ་ལས་གསུངས་ཏེ། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བློ་གྲོས་ཆེན་པོས་རང་གི་སེམས་སྣང་བའི་རྒྱུད་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཡང་གསོལ་བ་བཏབ་པ། བཅོམ་ལྡན་འདས་རང་གི་སེམས་སྣང་བའི་རྒྱུད་ཅིག་ཅར་རམ་རིམ་གྱིས་འཇུག་པས་སམ། ཇི་ལྟར་རྣམ་པར་དག་པར་གྱུར། [^1099]བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བློ་གྲོས་ཆེན་པོ་རང་གི་སེམས་སྣང་བའི་རྒྱུད་ནི་རིམ་གྱིས་འཇུག་པས་རྣམ་པར་དག་སྟེ་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1546]
འདི་ལྟ་སྟེ་བློ་གྲོས་ཆེན་པོ་ཤིང་ཨ་མྲའི་འབྲས་བུ་ནི་རིམ་གྱིས་སྨིན་པར་འགྱུར་གྱི༌[^1100]ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1547]
བློ་གྲོས་ཆེན་པོ་དེ་བཞིན་དུ་སེམས་ཅན་རྣམས་ཀྱི་རང་གི་སེམས་སྣང་བའི་རྒྱུད་ཀྱང་རིམ་གྱིས་རྣམ་པར་དག་པ༌[^1101]སྟེ། ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1548]
བློ་གྲོས་ཆེན་པོ་འདི་ལྟ་སྟེ། རྫ་མཁན་གྱི་སྣོད་རྣམས་ནི་རིམ་གྱིས་བྱེད་ཀྱི། ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1549]
བློ་གྲོས་ཆེན་པོ་དེ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པ་ཡང་སེམས་ཅན་རྣམས་ཀྱི་རང་གི་སེམས་སྣང་བའི་རྒྱུད་རིམ་གྱིས་རྣམ་པར་སྦྱོང་སྟེ།[^1102] ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1550]
བློ་གྲོས་ཆེན་པོ་འདི་ལྟ་སྟེ། ས་ཆེན་པོ་ལས་རྩྭ་དང་ཤིང་གེལ་བ་དང་། སྨན་དང་ནགས༌[^1103]ཚལ་རྣམས་རིམ་གྱིས་འཇུག་པས་སྐྱེའི་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1551]
བློ་གྲོས་ཆེན་པོ་དེ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་རང་གི་སེམས་སྣང་བའི་རྒྱུད༌[^1104]རིམ་གྱིས་སྦྱོང་སྟེ་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1552]
བློ་གྲོས་ཆེན་པོ་འདི་ལྟ་སྟེ། བཞད༌[^1105]གད་དང་། རོལ་མོ་དང་། གླུ་དང་། པི་ཝང་དང་། སིལ་སྙན་དང་། རོལ་མོ་དག་ལ་མཁས་པ་ནི་རིམ་གྱིས་འབྱུང་གི་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1553]
བློ་གྲོས་ཆེན་པོ་དེ་བཞིན་དུ། དེ་བཞིན་གཤེགས་པ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^1106]སེམས་སྣང་བའི་རྒྱུད་རྣམས་རིམ་གྱིས་སྦྱོང་སྟེ་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1554]
རིམ་པ་འདི་ཉིད་ནི་དཔའ་བར་འགྲོ་བའི་ཏིང་ངེ་འཛིན་གྱི་མདོ་ལས་ཀྱང་གསལ་བར་གསུངས་ཏེ། དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བློ་གྲོས་བརྟན་པས་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 1555]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་སློབ་ན་བྱང་ཆུབ་སེམས་དཔའ་བསླབ་པ་ཐམས་ཅད་ལ་དམིགས་པ་མ་མཆིས་པར་དཔའ་བར་འགྲོ་བའི་ཏིང་ངེ་འཛིན་ལ་སློབ་པ༌[^1107]ལགས།[^1108] དེ་སྐད་ཅེས་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས༌[^1109]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ༌[^1110]ཆེན་པོ་བློ་གྲོས་བརྟན་པ་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ། །

[Block 1556]
བློ་གྲོས་བརྟན་པ་འདི་ལྟ་སྟེ། དཔེར་ན་འཕོང་གི་སློབ་དཔོན་ནམ་འཕོང་གི་སློབ་མ་ནི་ཐོག་མར་བ་ལང༌[^1111]གི་ཀོ་བ་ལ་སློབ་པར་བྱེད་དོ། །

[Block 1557]
གང་གི་ཚེ་བ་ལང་གི་ཀོ་བ་ལ་ལོབས་པ་དེའི་ཚེ་ཤིང་ལེབ་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1558]
གང་གི་ཚེ་ཤིང་ལེབ་ལ་ལོབས་པ་དེའི་ཚེ། འབེན་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1559]
གང་གི་ཚེ་འབེན་ལ་ལོབས་པ་དེའི་ཚེ་དབྱུག་གུ་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1560]
གང་གི་ཚེ་དབྱུག་གུ༌[^1112]ལ་ལོབས་པ་དེའི་ཚེ་སྐྲ་བརྒྱ་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1561]
གང་གི་ཚེ་སྐྲ་བརྒྱ་ལ་ལོབས་པ་དེའི་ཚེ་སྐྲ་བཅུ་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1562]
གང་གི་ཚེ་སྐྲ་བཅུ་ལ་ལོབས་པ་དེའི་ཚེ། སྐྲ་གཅིག་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1563]
གང་གི་ཚེ་སྐྲ༌[^1113]གཅིག་ལ་ལོབས་པ་དེའི་ཚེ། སྒྲས་མཚོན་པ་ལ་འཕོག་པར་བྱེད་དོ། །

[Block 1564]
གང་གི་ཚེ་སྒྲས་མཚོན་པ་ལ་འཕོག་པ་དེའི་ཚེ། མི་འཆོར་བར་འཕོག་པར་བྱེད་དོ། །

[Block 1565]
གང་གི་ཚེ་མི་མཆོར་བར༌[^1114]འཕོག་པར་བྱེད་པ་དེའི་ཚེ་འཕོང་བསླབས་པ་མཐར་ཕྱིན་པ་ཡིན་ཏེ། དེ་འདོད་ན་ནུབ་མོ་མུན་པ་མུན་ནག་གི༌[^1115]ནང་ན་མི་དང་མི་མ་ཡིན་པ་གང་དང་གང་དག་གི་སྒྲ་གྲག་པ༌[^1116]དེ་དང་དེར་ལྷུན་གྱིས་གྲུབ་ཅིང་མི་འཆོར་བ་ཉིད་དུ་མདའ་འགྲོའོ། །

[Block 1566]
སྒྲས་མཚོན་པ་འཕོག་པར༌[^1117]བྱེད་པར་གནས་པས་ཕྱིས་གང་དུ་ཡང་མི་སློབ་སྟེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་ལེགས་པར་བསླབས་པའི་ཕྱིར་ཕོག་པར་བྱ་བ་ཐམས་ཅད་དེ་ལ་མངོན་སུམ་དུ་འགྱུར་རོ། །

[Block 1567]
བློ་གྲོས་བརྟན་པ་དེ་བཞིན་དུ་དཔའ་བར་འགྲོ་བའི་ཏིང་ངེ་འཛིན་འདི་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔས་ཕྱིས་ཆོས་གང་ལ་ཡང་བསླབ་པར་མི་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཏིང་ངེ་འཛིན་དེ་ཉིད་ལ་ལེགས་པར་བསླབས་པའི༌[^1118]ཕྱིར་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་གྱི་ཆོས་ཐམས་ཅད་མངོན་སུམ་དུ་འགྱུར་རོ། །

[Block 1568]
ཡང་ཚུལ་འདི་ཉིད་ཀྱིས་རྡོ་རྗེའི་ཐེག་པ་ལ་གནས་པའི་དཔའ་བར་འགྲོ་བའི་ཏིང་ངེ་འཛིན་ལ་སློབ་པར་འདོད་པས་ཀྱང་རིམ་པ་འདི་ཉིད་ཀྱིས་བསླབ་པར་བྱའོ། །

[Block 1569]
དེའི་རིམ་པ་འདི་ཡིན་ཏེ། ཐོག་མ་ཉིད་དུ་སངས་རྒྱས་ཀྱི་ཐེག་པའི་བསམ་པ་ལ་སློབ་བོ། །

[Block 1570]
གང་གི་ཚེ་སངས་རྒྱས་ཀྱི་ཐེག་པའི་བསམ་པ་ལ་ལོབས་པར་གྱུར་པ་དེའི་ཚེ་ཐེག་པ་སར་པ་ལ་དྲན་པ་གཅིག་པའི་ཏིང་ངེ་འཛིན་ལ་སློབ་བོ། །

[Block 1571]
གང་གི་ཚེ་ཐེག་པ་སར་པ་ལ་དྲན་པ་གཅིག་པའི་ཏིང་ངེ་འཛིན་ལ་ལོབས་པ་དེའི་ཚེ་རྟོག་པའི་རྣལ་འབྱོར་ལ་སློབ་བོ། །

[Block 1572]
གང་གི་ཚེ་རྟོག་པའི་རྣལ་འབྱོར་ལ་ལོབས་པ་དེའི་ཚེ་ལས་དང་པོ་པའི་ཏིང་ངེ་འཛིན་ལ་རབ་ཏུ་གནས་པར་འགྱུར་རོ། །

[Block 1573]
གང་གི་ཚེ་ལས་དང་པོ་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་པ་དེའི་ཚེ་རིགས་བརྒྱའི་དབྱེ་བ་ལ་འཇུག་གོ། །

[Block 1574]
གང་གི་ཚེ་རིགས་བརྒྱའི་དབྱེ་བས་ལུས་རྣམ་པར་དབེན་པ་ཤེས་པ་དེའི་ཚེ་སྐུ་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་ལ་གནས་པར་འགྱུར་རོ། །

[Block 1575]
ལུས་རྣམ་པར་དབེན་པ་ལ་གནས་ནས༌[^1119]ཨཱ་ལི་ཀཱ་ལིའི༌[^1120]སྒོ་ནས་ངག་རྣམ་པར་དབེན་པ་ལ་འཇུག་གོ། །

[Block 1576]
གང་གི་ཚེ་རྡོ་རྗེ་བཟླས་པའི་རིམ་གྱིས་སྲོག་དང་རྩོལ་བ་ཤེས་པར་འགྱུར་བ་དེའི་ཚེ་གསུང་གི་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན༌[^1121]གསལ་བར་འགྱུར་རོ། །

[Block 1577]
ངག་རྣམ་པར་དབེན་པ་ལ་གནས་ནས་རང་བཞིན་གྱིས༌[^1122]སྣང་བའི་རིམ་གྱིས་སེམས་ཀྱི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 1578]
སེམས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་ལ་གནས་ནས་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 1579]
གང་གི་ཚེ་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པ་དེའི་ཚེ༌[^1123]སངས་རྒྱས་ཀྱི་དབང་བསྐུར་བ་ཐོབ་བོ། །

[Block 1580]
གང་གི་ཚེ་དབང་བསྐུར་བ་ཐོབ་པ་དེའི་ཚེ་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་གནས་ནས་སྟོང་པ་ཆེན་པོ་བཅོ་བརྒྱད་ཀྱི་རིམ་པས་དོན་དམ་པའི༌[^1124]བདེན་པ་ལ་འཇུག་གོ། །
--- END BLOCKS ---
