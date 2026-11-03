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
དེས་པ་ནི༌[^864]བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། འགྲོགས་ན་བདེ་བའི་དངོས་པོ་ནི་དེས་པ་སྟེ། བཟོད་པ་དང་ལྡན་པ་ནི་དེས་པར་འགྱུར་རོ། །

[Block 1542]
སོགས་པ་སྨོས་པས་ནི་བརྩོན་འགྲུས་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་བ་དང་། བསྡུ་བའི་དངོས་པོ་ལ་སོགས་པ་གཟུང་ངོ་། །འཇིག་རྟེན་ལ་ཕན་འདོགས་པ་དང་མཐུན་པ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་ཞིང་བདེ་བ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 1543]
ཡོན་ཏན་ཁྱད་པར་ཅན་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ་ས་བཅུ་པ་ལ་སོགས་པ་དག་ཏུ་གསུངས་པའོ། །

[Block 1544]
དེ་བྱམས་པའི་སྟོབས་ཞེས་བྱ་བའི་མིང་ནི་ས་བཅུ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། སེམས་ཅན་ཐམས་ཅད་ལ་བྱམས་པའི་ཡིད་དུ་གྱུར་པ་ཞེས་སྨོས་སོ། །

[Block 1545]
དེ་བཞིན་དུ་གྱུར༌[^865]ཞེས་བྱ་བ་ནི་བདེ་བའམ་སྡུག་བསྔལ་དེ་བཞིན་དུ་གྱུར་པ་སྟེ། ཇི་ལྟར་སྐྱེ་དགུ་རྣམས་ལ་གནོད་པ་དང་ཕན་འདོགས་པར་བྱེད་པ་དེ་བཞིན་དུ་དེ་ཡང་གནོད་པ་དང་ཕན་འདོགས་པར་བྱེད་དོ། །

[Block 1546]
མཚོན་ཆ་དང་ནི་གཙུག་ལག་རྣམས་ལ་གོམས། །ཞེས་བསྟན་པ༌[^866]ལ། ཇི་ལྟར་གོམས་པ་ཡིན་ཞེ་ན། དེ་བསྒྲུབ་པའི༌[^867]ཕྱིར།

[Block 1547 [VERSE]]
མིའི་དབང་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
དེ་ཡི་མཚོན་ཆ་རྒྱན་དང་འདྲ་བར་གྱུར། །

[Block 1548]
ཞེས་བྱ་བ་ནི་ཆད་པར་སྒྲུབ་པ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །ཅིའི་ཕྱིར་ཞེ་ན། མིའི་དབང་པོས་བཀའ་ཁྲིམས་སྤྱི་བོས་མནོས་པའི་ཕྱིར་སྐལ་བ་ཁྱད་པར་ཅན་ཉིད་ཀྱིས་རྒྱལ་ཕྲན་རྣམས་རང་ཉིད་འདུ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1549]
དེ༌[^868]ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1550 [VERSE]]
འཇིག་རྟེན་ཕན་འབྱུང་བསྟན་ངག་ཚུལ་རྣམས་ཀྱི། །
གཙུག་ལག་རྣམས་ཀྱང་རྣམ་པར་གསལ་བར་སྣང་། །

[Block 1551]
ཞེས་སྨོས་ཏེ། འཇིག་རྟེན་ལ་གནོད་པར་མི་འཇུག་པའོ། །

[Block 1552]
བསྟན་ངག་ཚུལ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ལ་འཇིག་རྟེན་ལ་གནོད་པར་མི་འཇུག་པའི་ཚུལ་ནི་བསྟན་ངག་ཚུལ་ལོ། །

[Block 1553]
ཕན་པར་སེམས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་བསམ་པ་དང་ལྡན་པའི་ཕྱིར་ཏེ། འདིས་ནི་ཚུལ་ཁྲིམས༌[^869]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1554]
ཚུལ་མཁས་ཞེས་བྱ་བ་འདིས་ནི་ཤེས་རབ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1555]
རྟོགས༌[^870]མཁས་ཞེས་བྱ་བས༌[^871]ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་དང་། ཤེས་རབ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1556]
ཕ་དང་འདྲ་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། བྱེད་པ་ཕུན་སུམ་ཚོགས་པར༌[^872]བསྟན་ཏེ། དཔེར་ན་བུ་དག་ལ་ཚར་གཅོད་པ་དང་། ཕན་འདོགས་པར་བྱེད་པ་དང་། ཆོས་དང་འགལ་བར་མི་བྱེད་པའི་ཕ་བཞིན་དུ་སྐྱེ་དགུ་རྣམས་ལ་ཡང་དེ་ལྟར་སྦྱར་བར་བྱའོ། །

[Block 1557]
བདེན་པ་དང་། གཏོང་བ་དང་། ཉེ་བར་ཞི་བ་དང་། ཤེས་རབ་ལ་སོགས་པ་བྱིན་གྱི་རླབས༌[^873]འདི་བཞིས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསྟན་ཏེ། དེ་ལས་དང་པོ་གསུམ་གྱིས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་བསྟན་ཏོ། །ཤེས་རབ་ཀྱིས་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་བསྟན་ཏོ། །

[Block 1558]
གཞན་ལ་ཕན་པར་ཡོངས་སུ་བསྔོ་བའི་ཕྱིར་ཞེས་བྱ་བ་ཡིན་ཏེ། གཞན་དུ་ན་བྱིན་གྱི་རླབས་རྣམ༌[^874]པ་བཞི་ནི་རང་གི་དོན་དུ་ཡོངས་སུ་བསྔོས་པར་འགྱུར་ཞིང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་རྒྱུར་འགྱུར་བས་བསྔོ་བ་བྱེ་བྲག་མེད་པར་འགྱུར་རོ། །

[Block 1559]
ཁྱད་པར་ཅན་དུ་གྱུར་ལ་རླབས་ཆེ་བའི་རིམ་པས༌[^875]ཞེས་བྱ་བ་ནི་ཁྱད་པར་དང་བཅས་པ་ཡིན་པར་ཁྱད་པར་དུ་གྱུར་པ་སྟེ། སྲ་ཆུང་བའི་ཕྱིར་རོ། །

[Block 1560]
སྔ་མ་མོས་པས༌[^876]སྤྱོད་པའི་ས་ལས་ཁྱད་པར་དུ་གྱུར་པས་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 1561]
རླབས་ཆེ་བ་ནི་ཁྱད་པར་དུ་གཞན་ལ་ཕན་པ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 1562]
རིམ་པ་ཞེས་བྱ་བ༌[^877]སྨོས་པ་ནི་ས་དང་ས་དག་ཏུ་ཁྱད་པར་དུ་བྱེད་པའི་ཕྱིར་དང་། རླབས་ཆེ་བའི་ཕྱིར་རོ། །

[Block 1563]
བྱང་ཆུབ་ཀྱི་ཚོགས་བསགས་ཤིང་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་དག་གིས༌[^878]ཚོགས་ཀྱི་བྱ་བ་ཡིན་པས་བྱང་ཆུབ་ཀྱི་ཚོགས་ཏེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཡོན་ཏན་གཞན་ཡང་ས་བཅུ་པའི་མདོ་ལས་གསུངས་པའོ། །

[Block 1564]
གནོད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་མེ་དང་། ཆུ་དང་། ནད་དང་། མུ་གེ་དང་། བྱི་བ་དང་། སྲོག་ཆགས་གདུག་པ་སྦྲུལ་དང་། བདག་གི་དམག་ཚོགས་དང་། གཞན་གྱི་དམག་ཚོགས་དང་། རྐུན་མ་ལ་སོགས་པ་དང་བྲལ་བའི་ཕྱིར་གནོད་པ་ཐམས་ཅད་མེད་པའོ། །

[Block 1565]
ཕུན་སུམ་ཚོགས་ཕ་མཆོག་དང་ལྡན་པས་ཞེས་བྱ་བ་ནི་ལོ་ལེགས་པ་ལ་སོགས་པའི་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པའོ། །

[Block 1566]
མགུ་ཞིང་དར་བ་ཞེས་བྱ་བ་ལ། མགུ་བ་ནི་ཡིད་བདེ་ཞིང་ཚིམ་པ༌[^879]ཕུན་སུམ་ཚོགས་པ་སྟེ། འདོད་པ་ཤས་ཆེ་བ་ཡོད་པའོ། །

[Block 1567]
དར་བ་ནི་ལུས་འཕེལ་བའོ། །

[Block 1568]
དེའི་ཡུལ་ན་ནི་ཞེས་བྱ་བའི་ཡུལ་ཏེ་དེ་དག་ན་གནས་པ་གང་ཡིན་པ་དེ་ནི་དེ་ན་གནས་པའོ། །

[Block 1569]
མཐུ་ཁྱད་ཆེ་བས་ན་ཞེས་བྱ་བ་ནི་ཁྱད་པར་ཡིན་ཏེ། ཁྱད་པར་ནི་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་ཏེ། དཔག་ཏུ་མེད་པའི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཉེ་བར་བསགས་པའི་ཕྱིར་རོ། །

[Block 1570]
གང་གི་ཞེས་བྱ་བ་ནི་མདངས་འཕྲོགས༌[^880]པའི་གནས་སུ་ཕྱིན་པར་གྱུར་ཀྱང་ངོ་། །རིག༌[^881]སྔགས་དང་དཀའ་ཐུབ་ནི་རིག༌[^882]སྔགས་དང་དཀའ་ཐུབ་བོ། །

[Block 1571]
དེ་གཉིས་གྲུབ་པ་ནི་རིག༌[^883]སྔགས་དང་དཀའ་ཐུབ་གྲུབ་པའི་རང་བཞིན་ཏེ། རིག༌[^884]སྔགས་དཀའ་ཐུབ་གྲུབ་པའི་ངོ་བོ་ཉིད། །ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1572]
མིང་ནི་དོན་དང་མཐུན་པར་མ་གྱུར་ཞེས་བྱ་བ་ལ། དོན་མེད་པའི་མིང་གང་ཡིན་པ་དེ་ནི་དོན༌[^885]མི་མཐུན་པའི་མིང་སྟེ། གང་གི་ཕྱིར་མདངས་འཕྲོགས༌[^886]པ་ཞེས་བྱ་བ་དེའི་མིང་དོན་མེད་པར་འགྱུར་བ་སྟེ། འདི་ལྟར་མདངས་འཕྲོགས༌[^887]པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1573]
ནགས་ན་རབ་ཏུ་རྒྱུ་བ་ཞེས་བྱ་བ་ལ། འདིར་རབ་ཏུ༌[^888]ཞེས་བྱ་བའི་སྒྲ་ནི་དེ་དང་ལྡན་པ་སྟེ། ནགས་དང་ལྡན་པ་ན་རྒྱུ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1574]
གྲིབ་མ་དང་ལྡན་པའི་ཤིང་ནི་གྲིབ་ཤིང་སྟེ་དེའི་རྩ་བ་དེ་ནི་གྲིབ་ཤིང་གི་དྲུང་ནའོ། །

[Block 1575]
སྲད་བུ་འཁལ་ཞེས་བྱ་བ་ལ་སྲད་བུ་འཁལ་བ་ལ་ཞུགས་པ་ནི་སྲད་བུ་འཁལ་བ་སྟེ་དེ་བྱེད་པའོ། །

[Block 1576]
འདི་ལྟ་བུའི་དགོན་པ་ཞེས་བྱ་བ་ནི་དེ་ན་སྐྱེ་བོ་གནས་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1577]
འགྲོ་བ་མེད་པ་ན༌[^889]ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ལམ་དུ་འགྲོ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1578]
གཅིག་པུ་ནི་གྲོགས་པོ་མེད་པའོ། །

[Block 1579]
བལྟས་པས་ནི་གྱེན་ཀུན་དུ་བལྟས་པར་བྱས་པ༌[^890]སྟེ།

[Block 1580 [VERSE]]
སྲིན་པོ་དང་ཤ་ཟ་དེ་དག་ལའོ། །
དེ་བས་ནགས་ནའང་ཁྱིམ་བཞིན་དུ། །
--- END BLOCKS ---
