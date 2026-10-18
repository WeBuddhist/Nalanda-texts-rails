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
བཙུན་པ་དབྱིག་བཤེས་ཀྱིས་ནི་ཡོངས་སུ་དྲིས་པ༌[^737]ལས།

[Block 1612]
འདི་ནི་གང་གི་ལྟར་ན་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སེམས་མེད་པ་པ༌[^738]ཡིན་པ་དེ་ལ་སྐྱོན་དུ་འགྱུར་གྱི་ཁོ་བོ་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སེམས་དང་བཅས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1613]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་དེ་ནི་མི་འཐད་དེ། བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཤེས་པ་ཡོད་ན་གསུམ་འདུས་པ་ལས་རེག་པ། རེག་པའི་རྐྱེན་གྱིས་ཚོར་བ་དང་འདུ་ཤེས་དང་སེམས་པ་ཞེས་གསུངས་ཏེ། དེའི་ཕྱིར་འདི་ལ་འདུ་ཤེས་དང་ཚོར་བ་དག་ཀྱང་འགག་པར་མི་འགྱུར་རོ། །

[Block 1614]
འོན་ཏེ་ཚོར་བའི་རྐྱེན་གྱིས་སྲེད་པ་ཞེས་གསུངས་མོད་ཀྱི་དགྲ་བཅོམ་པ་ལ་ཚོར་བ་ཡོད་བཞིན་དུ་སྲེད་པ་མི་སྐྱེ་བ་དེ་བཞིན་དུ་རེག་པ་ཡོད་བཞིན་དུ་ཚོར་བ་ལ་སོགས་པ་མི་འབྱུང་ངོ་ཞེ་ན། ཁྱད་པར་དུ་བྱས་པའི་ཕྱིར་དེ་ནི་མ་ཡིན་ཏེ། མ་རིག་པའི་འདུས་ཏེ་རེག་པ་ལས་སྐྱེས་པའི་ཚོར་བ་ལ་བརྟེན་ནས་སྲེད་པ་སྐྱེས་སོ་ཞེས་གསུངས་ཀྱི། ཚོར་བ་སྐྱེས་པ༌[^739]ལ་རེག་པ་ནི་བྱེ་བྲག་ཏུ་མ་བྱས་པས་འདི་ནི་མི་འདྲའོ། །

[Block 1615]
དེ་ལྟ་བས་ན་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་སེམས་མེད་པ་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1616]
ཇི་ལྟར་ན་སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཉིད་ཡིན་ཞེ་ན། འབྱུང་བ་ཆེན་པོ་མཉམ་པ་ཉིད་དུ་སྒྲུབ་པའི་ཕྱིར་རམ། ཡང་ན་སྙོམས་པར་འཇུག་པའི་སེམས་ཀྱིས་དེ་ལ་སྙོམས་པར་འཇུག་ཅིང་འཐོབ་པར་འགྱུར་བས་ན་སྙོམས་པར་འཇུག་པ་ཡིན་ནོ། །

[Block 1617]
ཡང་ཅི་སྙོམས་པར་འཇུག་པ་འདི་དག་རྫས་སུ་ཡོད་དམ་འོན་ཏེ་བཏགས་པར་ཡོད་ཅེ་ན། སེམས་སྐྱེ་བ་ལ་བགེགས་བྱེད༌[^740]པའི་ཕྱིར་རྫས་སུ་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 1618]
མ་ཡིན་ཏེ། སྙོམས་པར་འཇུག་པའི་སེམས་ཁོ་ན་དེ་ལ་བགེགས་བྱེད༌[^741]པའི་ཕྱིར་རོ། །

[Block 1619]
སྙོམས་པར་འཇུག་པའི་སེམས་ཁོ་ན་དེ་དང་འགལ་བའི་རྟེན་སྐྱེད་པའི་ཕྱིར་གང་གིས་ན་དུས་གཞན་གྱི་བར་དུ་སེམས་མི་འཇུག་པ་ཙམ་དུ་འགྱུར་བ་དེ་ལས་གཞན་པའི་སེམས་དང་འགལ་བར་སྐྱེ་སྟེ། དེ་ལ་སྙོམས་པར་འཇུག་པ་ཞེས་གདགས་སོ། །

[Block 1620]
མི་འཇུག་པ་ཙམ་སྟེ༌[^742]ཡང་སྔོན་མ་བྱུང་བ་དང་ཕྱིས་ལངས་པ་ལ་མེད་པ་ཡིན་པས་སྙོམས་པར་འཇུག་པ་འདི་ནི་འདུས་བྱས་སུ་བཏགས་སོ། །

[Block 1621]
ཡང་ན་རྟེན་ཉིད་དེ་ལྟར་མཉམ་པར་བསྒྲུབས་པས༌[^743]ན་སྙོམས་པར་འཇུག་པ་ཡིན་ནོ། །

[Block 1622]
འདུ་ཤེས་མེད་པ་པ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱ་སྟེ། འདིས་དེས༌[^744]སེམས་ཁོ་ན་སེམས་འཇུག་པ་དང་འགལ་བ་ཐོབ་སྟེ། མི་འཇུག་པ་ཙམ་དེ་ཡང་འདུ་ཤེས་མེད་པ་པར་གདགས་སོ། །

[Block 1623]
དེ་སྐད་དུ་ནི་མི་བརྗོད་དོ། །

[Block 1624]
སྙོམས་པར་འཇུག་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 1625 [HEADING]]
#### སྲོག། ^2-3-6-0

[Block 1626]
སྲོག་གང་ཞེ་ན། སྲོག་ནི་ཚེ་ཡིན། ཆོས་མངོན་པ་ལས་འདི་སྐད་དུ། སྲོག་གི་དབང་པོ་གང་ཞེ་ན། ཁམས་གསུམ་པའི་ཚེ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །ཚེ་ཞེས་བྱ་བའི་ཆོས་དེ༌[^745]གང་ཡིན་པ་དེ་ཡང་མི་ཤེས་པས། དྲོད་དང་ནི།

[Block 1627 [VERSE]]
རྣམ་ཤེས་རྟེན་གང་ཡིན་པའོ། །
བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ།
ཚེ་དང་དྲོད་དང་རྣམ་ཤེས་འདིས། །
གང་ཚེ་ལུས་ནི་འདོར་བྱེད་ཅིང་། །

[Block 1628 [VERSE]]
བོར་ནས་དེ་ཚེ་འདུག་པ་ནི། །
སེམས་མེད་ཇི་ལྟར་ཤིང་བཞིན་ནོ། །

[Block 1629]
ཞེས་གསུངས་ཏེ། དེ་ལྟ་བས་ན་དྲོད་དང་རྣམ་པར་ཤེས་པའི་རྟེན་དུ་གྱུར་པའི་ཆོས་གནས་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་ཚེ་ཡིན་ནོ། །

[Block 1630]
ད༌[^746]ནི་ཚེ་དེའི་རྟེན་དུ་གྱུར་པ་གང་ཡིན་ཞེ་ན། དྲོད་དང་རྣམ་པར་ཤེས་པ་དེ་དག་ཉིད་ཡིན་ནོ། །

[Block 1631]
འོ་ན་ནི་ཕན་ཚུན་ལྟོས་ཏེ་འཇུག་པའི་ཕྱིར། དེ་དག་ལས་གང་གི༌[^747]དབང་གིས་ན་གཞན་དག་ལྡོག་པར་འགྱུར་བ་གང་ཞིག་སྔར༌[^748]ལྡོག་པར་འགྱུར་ཏེ། རྟག་ཏུ་ལྡོག་པ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1632]
འོ་ན་ནི་ཚེའི་རྟེན་དུ་གྱུར་པ་ལས་ཡིན་ཏེ། ལས་ཀྱིས་ཇི་སྲིད་དུ་འཕངས་པ༌[^749]དེ་སྲིད་དུ་རྗེས་སུ་འཇུག་པའི་ཕྱིར་རོ་ཞེ་ན། དྲོད་དང་རྣམ་པར་ཤེས་པ་དག་གི་རྟེན་དུ་གྱུར་པ་ཡང་ལས་ཁོ་ན་ཡིན་པར་ཅིའི་ཕྱིར་མི་འདོད་དོ།[^750] །མ་ཤི་བའི༌[^751]བར་དུ་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་རྣམ་པར་སྨིན་པར་འགྱུར་དུ་འོང་ངོ་། །འོ་ན་ནི་དྲོད་ཀྱི་རྟེན་དུ་གྱུར་པ་ལས་ཡིན་པར་འགྱུར་ལ། དྲོད་ཀྱང་རྣམ་པར་ཤེས་པའི་རྟེན་དུ་གྱུར་པ༌[^752]ཡིན་པར་འགྱུར་རོ། །

[Block 1633]
དེ་ལྟ་ན་ནི་གཟུགས་མེད་པ་དག་ན་དྲོད་མེད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་རྟེན་མེད་པར་འགྱུར་རོ། །

[Block 1634]
དེའི་རྟེན་ནི་ལས་ཡིན་པར་འགྱུར་རོ། །

[Block 1635]
གང་ལ་ལར་ནི་རྣམ་པར་ཤེས་པའི་རྟེན་དྲོད་ཁོ་ན་ཡིན་པར་འགྱུར་རོ། །

[Block 1636]
ལ་ལར་ནི་ལས་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བ་འདོད་དགུ་མི་འཐོབ་པ་ཉིད་དེ་བཤད་ཀྱང་ཟིན་ཏོ། །

[Block 1637]
ཇི་སྐད་དུ་བཤད་ཅེ་ན། མ་ཤི་བའི༌[^753]བར་དུ་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་རྣམ་པར་སྨིན་པར་འགྱུར་དུ་འོང་ངོ་ཞེས་བཤད་དོ། །

[Block 1638]
དེ་ལྟ་བས་ན་དེ་གཉིས་ཀྱི་རྐྱེན་དུ་གྱུར་པ་ཚེ༌[^754]ནི་ཡོད་པ་ཁོ་ནའོ། །

[Block 1639]
མེད་དོ་ཞེས་ནི་མི་སྨྲ་མོད་ཀྱི་རྫས་གཞན་ནི་མེད་དོ། །

[Block 1640]
འོ་ན་དེ་ཅི་ཡིན་ཞེ་ན། ཁམས་གསུམ་པའི་ལས་ཀྱིས་རིས་མཐུན་པ་གནས་པའི་དུས་ཀྱིས༌[^755]འཕེན་པ་ཡིན་ཏེ། དུས་འདི་སྲིད་ཅིག་ཏུ་གནས་པར་བྱའོ་ཞེས་ཇི་སྲིད་དུ་ལས་ཀྱི་རིས་མཐུན་པ་འཕངས་པ་དེ་སྲིད་དུ་དེ་གནས་པ་དེ་ལ་ཚེ་ཞེས་བྱ་སྟེ། འབྲུ་རྣམས་ཀྱི་སྨིན་པའི་དུས་ཀྱིས༌[^756]འཕེན་པ་ལྟ་བུ་དང་། མདའ་འཕངས་པ་དག་གི་གནས་པའི་དུས་ཀྱིས༌[^757]འཕེན་པ་བཞིན་ནོ། །

[Block 1641]
གང་ཞིག་འདུ་བྱེད་ཅེས་བྱ་བ་ཡོན་ཏན་གྱི་ཁྱད་པར་འགའ་མདའ་ལ་སྐྱེ་སྟེ། དེའི་དབང་གིས་ན་མ་ལྟུང་གི་བར་དུ་འགྲོ་བར་འགྱུར་རོ་སྙམ་དུ་སེམས་པ་དེའི་དེ་ནི་གཅིག་པུ་ཡིན་པའི་ཕྱིར་དང་། གེགས་བྱེད་པ་མེད་པའི་ཕྱིར་ཡུལ་གཞན་དག་ཏུ་མགྱོགས་པ་དང་ཆེས་དང་ཤིན་ཏུ་ཆེས་མགྱོགས་པར་ཕྱིན་པའི་དུས་ཀྱི་བྱེ་བྲག་ཀྱང་མི་འཐད་ལ་ལྟུང་བ་ཡང་མི་འཐད་དོ། །

[Block 1642]
གལ་ཏེ་རླུང་གིས༌[^758]དེ་ལ་གེགས་བྱེད་དོ་ཞེ་ན། རླུང་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་དྲུང་དུ་ལྟུང་བ་འམ་ཡང་ན་གཞར་ཡང་མི་ལྟུང་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 1643]
འདི་སྐད་དུ་ཚེ་རྫས་གཞན་ཁོ་ན་ཞིག་ཡོད་དོ་ཞེས་ནི་བརྗོད་དོ། །

[Block 1644]
ཡང་ཅི༌[^759]ཚེ་ཟད་པ་ཁོ་ནས་འཆི་བར་འགྱུར་རམ། འོན་ཏེ་གཞན་དུ་ཡང་ཡིན་ཞེ་ན།

[Block 1645]
བཏགས་པ་ལས།

[Block 1646]
ཚེ་ཟད་པར་འཆི་བར་འགྱུར་ལ་བསོད་ནམས་ཟད་པས་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞི༌[^760]གསུངས་ཏེ། མུ་དང་པོ་ནི་ཚེ་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་ཡོངས་སུ་གཏུགས་པ་ལས་སོ། །

[Block 1647]
གཉིས་པ་ནི༌[^761]ལོངས་སྤྱོད་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་ཡོངས་སུ་གཏུགས་པ་ལས་སོ། །

[Block 1648]
གསུམ་པ་ནི་གཉི་གའོ། །

[Block 1649]
བཞི་པ་ནི་ཡ་ང་བ་ཡོངས་སུ་མ་སྤངས༌[^762]སོ། །

[Block 1650]
ཚེ་བཏང་བ་ལས་ཀྱང་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
