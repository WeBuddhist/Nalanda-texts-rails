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
[Block 1611]
འདིར་གཞི་གང་ལ་དབུལ་བ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྩིག་པ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཕྲེང༌[^1025]བའོ། །

[Block 1612]
དེ་ལ་དམིགས་ཀྱིས་བསལ་བར་གྱུར་པའི་ཆོ་ག་གཞན་བརྗོད་པར་བྱ་སྟེ། དེར་ཁབ་བམ་ཚེར་མ་བཙུགས་པ་ལ་ཕྲེང་བ་བརྒྱུས་པ་དག་དཔྱང་བར༌[^1026]བྱའོ་ཞེས་བྱ་བ་དེར་ཞེས་བྱ་བ་ནི་རྩིག་པའི་ངོས་བསྟན་པ་ལ་སྟེ་ཕྱེད་བརྐོས་པ༌[^1027]ལ་འཇུག་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1613]
ཚེར་མ་བཙུགས་པ་ལ་ཞེས་བྱ་བ་ནི་ཕྱེད་བཙུགས་པ་ལའོ། །

[Block 1614]
མིག་ལ་ཕན་པའི་དྲི་ཞིམ་པོ་དུས་དུས་སུ་བསྣམ་པར༌[^1028]བྱའོ་ཞེས་བྱ་བ་ནི་ཆོ་ག་འདི་ནི་གཉིས་ཀ༌[^1029]དང་འབྲེལ་པར་རིག་པར་བྱའོ། །

[Block 1615]
བྲམ་ཟེ་སྲད་བུ་ཐོགས་པ་བསྟེན་པར་མི་བྱའོ། །

[Block 1616]
སྔགས་སྐུད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སྔགས་སྐུད་ཐོགས་པ་བསྟེན་པར་མི་བྱའོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 1617]
བྱས་པ་ཉིད་ལ་ནི་གསོ་བའི་ཕྱིར་རྗེས་སུ་གནང་བ་ལ་བརྟན༌[^1030]ནས་གནས་ཀྱི་བྱེ་བྲག་བསྟན་པ་ནི་གསོ་བའི་ཕྱིར་ནི་དཔུང་བ་གཡོན་པར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1618]
སྔགས་སྐུད་ཐོགས་པ་ཡང་བསྟེན་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1619]
གར་བབ་བབ༌[^1031]ཏུ་ནི་མི་དོར་ཞེས་བྱ་བ་ནི་སོས་པར་གྱུར་ནས་སྔགས་སྐུད་དེའོ། །

[Block 1620]
གལ་ཏེ་ལྷག་མ་དང་བཅས་པར་གྱུར་ན་ཆོས་གོས་ཀྱི་ཐ་མའམ། སྐ་རགས་ལ་གདགས་སོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་ལྷག་མ་དང་བཅས་པར་གྱུར་ན་ཞེས་བྱ་བ་ནི་གནང་ངོ་། །གལ་ཏེ་མ་གྱུར་ན་ཀ་བའམ། རྩིག་པའི་གསེབ་ཏུ་གཞུག་ཅེས་བྱ་བ་ལ། གལ་ཏེ་མ་གྱུར་ན་ཞེས་བྱ་བ་ནི་ལྷག་མ་དང་བཅས་པར་རོ། །

[Block 1621]
རྩིག་པའི་གསེབ་ཏུ་ཞེས་བྱ་བ་ནི་དེའི་ནང་དུའོ། །

[Block 1622]
གར་དང་གླུ་དང་རོལ་མོ་ཀུན་དུ་སྤྱད་པར་མི་བྱའོ། །

[Block 1623]
བསླབ་པར་མི་བྱའོ། །

[Block 1624]
བཟླས་པར་མི་བྱའོ། །

[Block 1625]
ལྟ་བའི༌[^1032]ཕྱིར་འགྲོ་བར་མི་བྱའོ། །

[Block 1626]
དགེ་སློང་མ་ཀུན་དུ་གར་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གར་ནས་བརྩམས་ཏེ་དགེ་སློང་མས་མི་བྱའོ། །

[Block 1627]
དགེ་སློང་མ་གར་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱི་སྒྲ་འཇུག་པའོ། །

[Block 1628]
སྟོན་པའི་ཡོན་ཏན་ཡང་དག་པར་བསྒྲག་པ་དང་། རྒྱུན་ཆགས་གསུམ་པ་གདོན་པ་ལ་དབྱངས་ཀྱི་ང་རོ་བྱའོ་ཞེས་བྱ་བ་ནི་སྟོན་པའི་ཡོན་ཏན་བསྒྲག་པ༌[^1033]དང་། རྒྱུན་ཆགས་གསུམ་པ་གདོན་པ་ལས་གཞན་པའི་དབྱངས་ཀྱི་ང་རོ་བསྒྱུར་བ་ལ། གླུ་རྒྱང་གི་ཁོངས་སུ་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 1629]
དེ་དག་དབེན་པའི༌[^1034]ཕྱོགས་སུ་བསླབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་དབྱངས་ཀྱི་ང་རོ་དེ་དག་དབེན་པའོ། །

[Block 1630]
ཐོ༌[^1035]འཚམས་པ་དང་ཀུན་དུ་རྩེ་བ་དང་། ཀུན་དུ་ཅ་ཅོ་འདོན་པ་དང་། རྒོད་པ་དང་། དྲེགས་པ་དང་། ལུས་བརྡེག་པ༌[^1036]དག་མི་བྱའོ། །

[Block 1631]
རྒོད་པའི་བསམ་པས་ལུས་དང་ངག་གི་རྣམ་པར་འགྱུར་བ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་ཀོ་ལྤགས་ཀྱི་གཞི་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། དགེ་སློང་གིས་མཆིལ་ལྷམ་གཟུང་བར༌[^1037]མི་བྱའོ། །

[Block 1632]
ལག་འགྲོས་མཁན་རབ་ཏུ་བྱུང་བ་ཞིག་རྐང་ཁྲུས་སར་དེའི་ཆུ་སྣོད་གཞག་ཏེ་རྐང་པ་གཉིས་བཀྲུས་ནས་ཁ་ཆུས་བཀང་སྟེ། རྨ་བྱའི་འགྲོས་ཀྱིས་འདུག་པ་དང་དྲུག་སྡེ་དག་གིས་མཐོང་ནས་དེ་རྣམས་ཀྱིས་སྨྲས་པ། ཚེ་དང་ལྡན་པ་ལ་རོལ་མོ་མེད་པར་དགེ་སློང་གར་བྱེད་དེ། དེ་དག་གི༌[^1038]ཁས་གླུ་བླངས་པས་རོལ་མོའི་གླུ་བརྩམས་པའི་སྐབས་དེ་དགེ་སློང་དག་གིས་གསོལ་པ་ན། ཚེ་དང་ལྡན་པ་དག་ཅིའི་ཕྱིར་དགོད་པར༌[^1039]གྱུར་ཅེས་སྨྲས་པ་དང་། དེ་རྣམས་ཀྱིས་སྨྲས་པ་འདི་ལ་བགད༌[^1040]དུ་ཅི་ཞིག་ཡོད། ཁྱེད་རྣམས་ཀྱིས་མཐོང་ངམ་དགེ་སློང་རོལ་མོ་མེད་ཀྱང་གར་བྱེད་པ་ཞེས་བྱ་བའི་སྐབས་འདི་ནས། ཇི་སྲིད་དུ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དེ་ལ་དྲི་བ་མཛད་དེ་དགེ་སློང་བསམ་པ་གང་གིས་འདི་ལྟར་བྱས། བཙུན་པ་གནས་མལ་བསྐྱབ་པའི་དོན་ཅུང་ཟད་དང་དགོད་པའི༌[^1041]བསམ་པ་ཅུང་ཟད་ཀྱིས་སོ། །

[Block 1633]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གནས་མལ་བསྐྱབ་པའི་ཆེད་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1634]
དགོད་པའི༌[^1042]བསམ་པས་བྱས་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1635]
དྲུག་སྡེ་དག་ལ་སྨྲས་པ། བསམ་པ་གང་གིས་ཁྱེད་ཀྱིས་དེ་ལྟར་བྱས། བཙུན་པ་བསྡད་པའི་བསམ་པ་ཅུང་ཟད་དག་དང་། དགོད་པའི༌[^1043]བསམ་པ་ཅུང་ཟད་ཀྱིས་བགྱིས་སོ། །

[Block 1636]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བསྡད་པའི་བསམ་པ་དག་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1637]
གང་ཞིག་དགོད་པའི༌[^1044]བསམ་པས་བྱས་པ་དེ་ལ་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1638]
གང་ཞིག་འདིར་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ལ་ཡང་རིགས་མི་མཐུན་པས་བར་དུ་ཆོད་པ་དག་ལ་ལྟུང་བ་དང་ལྟུང་བ་མེད་པ་གཅིག་ཏུ་བསྟན་པའི་ཕྱིར་འདྲེས་པ་ནི་ཆར་སྡོམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆ་ཤས་ཀྱིས་འདྲེས་པ་ཉིད་ལ་རིགས་མི་མཐུན་པའི་ཆ་རྣམས་ཀྱིས་འདིར་རིགས་མི་མཐུན་པར༌[^1045]བར་དུ་གཅོད་པ༌[^1046]ཉིད་ཀྱི་དབང་གིས་ཐ་དད་པ་ཐམས་ཅད་རིགས་མཐུན་པའི་ཆ་རྣམས་ཆ་གཅིག་པ་ཉིད་ཀྱིས་མངོན་པར་འདོད་པ་ཉིད་དོ། །

[Block 1639]
ཆ་གཅིག་པ་ཉིད་ལ༌[^1047]དེ་ཉིད་ལ་འཇུག་པ་གཅིག༌[^1048]པ་ཉིད་དོ། །

[Block 1640]
འདིར་རིགས་གཞན་ཉིད་ཀྱིས་ཐ་དད་པའི་དངོས་པོའོ། །

[Block 1641]
འདིར་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར། བར་དུ་གཅོད་པ་ཉིད་མེད་པ་ལ་ཡང་གཅིག་ཉིད་དུ་རྣམ་པར་གཞག་པའོ། །

[Block 1642]
བར་ཆད་འགའ་ཞིག་ནི་དམན་པ་སྟེ། གང་ཞིག་མེད་པས་དེ་བས་ན་ངེས་པར་གནས་པ་དང་ལྟ་བ་དང་སྤྲུགས་པ་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ། །

[Block 1643]
སྣོད་བརྒྱུད་པས་ཟས་ཀྱི་བྱ་བ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་ཆང་འཐུང་བ་དག་ཕན་ཚུན་སྐོམ་སྣོད་བརྒྱུད་པས་ཆང་འཐུང་བར་བྱེད་པ་དེ་ལྟར་མི་བྱའོ། །

[Block 1644]
མེ་ཏོག་རྣ་རྒྱན་བརྒྱུ་བར་མི་བྱའོ་ཞེས་བྱ་བ༌[^1049]ནི། བཟོ་རྗེས་སུ་བསྒྲུབ་པར་མི་བྱའོ་ཞེས་བྱ་བའི་སྤྲོས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1645]
གདགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མེ་ཏོག་རྣ་རྒྱན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1646]
འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། འདིས་ཕྲེང༌[^1050]བ་བརྒྱུ་ཞིང་འདོགས་པ་ཐམས་ཅད་ལ་དགག་པར་བྱས་པ་རྟོགས་པར་བྱའོ། །

[Block 1647]
ངོ་སོ་ལས་བྱུང་བར་སྦྱིན་པར་མི་བྱའོ། །

[Block 1648]
མི་རིངས་པར་རྒྱུག་པར༌[^1051]མི་བྱའོ། །

[Block 1649]
མྱུར་བ་དང་མཆོངས་པར་མི་བྱའོ། །

[Block 1650]
བརླ་དང་ལག་པ་ཉ་ལྟར་བསྐོར་བར་མི་བྱའོ། །
--- END BLOCKS ---
