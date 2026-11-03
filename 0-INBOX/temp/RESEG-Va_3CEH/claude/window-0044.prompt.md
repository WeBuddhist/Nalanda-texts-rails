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
སྦྱོར་བ་ལས་བྱུང་བ་དེའི་ཕན་ཡོན་གང་ཞེ་ན།

[Block 1542 [VERSE]]
རྣམ་རྟོག་མེད་པའི་ཡེ་ཤེས་དེ། །
གོས་པ་མེད་དེ་ནམ་མཁའ་བཞིན། །

[Block 1543]
གང་གིས་མ་གོས་ཤེ་ན། དེ་བསྟན་པ། སྡིག་པ་སྣ་ཚོགས་དྲག་རྣམས་ཀྱིས་སོ། །

[Block 1544]
རྒྱུ་གང་གིས་མ་གོས་པ་དེ་བསྟན་པ། དད་པ་ཙམ་དང་མོས་པ་ཡིས། །ཞེས་བྱ་བ་ལ། དད་པ་ཙམ་དང་། གང་རྣམ་པར་མི་རྟོག་པ་ལ་ལྷག་པར་མོས་པ་དེ་ནི་དེའི་ཕྱིར་ངན་འགྲོར་འགྲོ་བའི་གཉེན་པོ་ཉིད་ཡིན་ཞིང་། སྒྲིབ་པ་སྤངས་པར་གྱུར་པས་མི་གོས་པའོ། །

[Block 1545 [HEADING]]
#### རྩ་བ་རྣམ་པར་མི་རྟོག་པའི་ཕན་ཡོན། ^8-13-2-0

[Block 1546]
རྩ་བ་རྣམ་པར་མི་རྟོག་པའི་ཕན་ཡོན་ཡང་། གོས་པ་མེད་དེ་ནམ་མཁའ་བཞིན། གང་ཞེ་ན། རྣམ་རྟོག་མེད་པའི་ཡེ་ཤེས་དེ། །[^954]གང་གིས་ཤེ་ན། སྒྲིབ་པ་ཀུན་ལས་སོ། །ཇི་ལྟར་ཞེ་ན། ཐོབ་དང་གྲུབ་དང་ལྡན་པས་ན། །ཞེས་བྱ་བ་སྟེ། ས་རྣམས་ཐོབ་པ་དང་ལྡན་པ་དང་། གྲུབ་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1547]
འདིས་ནི་སྒྲིབ་པ་དེའི་གཉེན་པོ་ཉིད་བསྟན་པར་འགྱུར་རོ། །

[Block 1548 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པའི་ཕན་ཡོན། ^8-13-3-0

[Block 1549]
རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པའི་ཕན་ཡོན་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། དེ་ཡང་།

[Block 1550 [VERSE]]
རྣམ་རྟོག་མེད་པའི་ཡེ་ཤེས་དེ། །
གོས་པ་མེད་དེ་ནམ་མཁའ་བཞིན། །
འཇིག་རྟེན་དག་ན་རྣམ་རྒྱུ་ཡང་། །
འཇིག་རྟེན་ཆོས་ཀྱིས༌[^955]རྟག་མི་གོས། །

[Block 1551]
ཞེས་བྱ་བ་ལ། ཡེ་ཤེས་དེ་ཉིད་ཀྱིས་ནི་སེམས་ཅན་གྱི་དོན་མཐོང་ནས་སྲིད་པ་དག་ཏུ་ཡང་སྐྱེ་བར་འགྱུར་ལ། དེ་འཇིག་རྟེན་དུ་སྐྱེས་པར་གྱུར་ན་ཡང་དེ་ལ་འཇིག་རྟེན་གྱི་ཆོས་ཀྱིས་ནི་མི་གོས་ཏེ། འཇིག་རྟེན་གྱི་ཆོས་ནི་རྙེད་པ་དང་མ་རྙེད་པ་དང་། གྲགས་པ་དང་། མ་གྲགས་པ་དང་། བསྟོད་པ་དང་། སྨད་པ་དང་། བདེ་བ་དང་། སྡུག་བསྔལ་ཞེས་བྱའོ། །

[Block 1552]
དེ་ཡང་རྣམ་པར་མི་རྟོག་པ་ཉིད་ཡིན་ཏེ། རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ལས་དེ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1553 [HEADING]]
### ཡེ་ཤེས་གསུམ་པོ་དེ་དག་གི་བྱེ་བྲག། ^8-14-0

[Block 1554]
གང་ཡེ་ཤེས་གསུམ་པོ་དེ་དག་ཉིད་ཀྱི་བྱེ་བྲག་ནི་ཇི་ལྟར་དེ་དག་བསྟན་པ་བཞིན་དུ་དེ་ཡང་བསྟན་པར་བྱའོ། །

[Block 1555]
ཇི་ལྟར་ལྐུགས་པས་དོན་ནི་མྱོང་འདོད་ལྟར་ཏེ། བརྗོད་པ་མེད་པ་ལྟར་སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་མི་རྟོག་པ་ནི་དེ་བཞིན་ནོ། །

[Block 1556]
ཇི་ལྟར་ལྐུགས་པས་དོན་མྱོང་དང་སྟེ་བརྗོད་པ་མེད་པ་དེ་ལྟ་བུ་ནི་དངོས་གཞི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1557]
མ་ལྐུགས་པས་ནི་དོན་མྱོང་ལྟར་ཏེ། བརྗོད་པ་ལྟར་དེ་བཞིན་དུ་རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པའི་རྣམ་པར་མི་རྟོག་པ་བལྟ་བར་བྱའོ། །

[Block 1558]
འདིར་བརྗོད་པ་ནི་ཡི་གེ༌[^956]བརྗོད་པ་ཡིན་པར་བཞེད་དོ། །

[Block 1559]
རྨོངས་པས་དོན་ནི་མྱོང་འདོད་དང་། །ཞེས་བྱ་བ་ལ། འདིར་ཐ་སྙད་ལ་མ་བྱང་བ་ནི་རྨོངས་པ་ཡིན་པར་བཞེད་དོ། །

[Block 1560]
རྨོངས་པ་འདི་དག་ཀྱང་ཡེ་ཤེས་གསུམ་དང་དཔེ་ཡང་ལྐུགས་པ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1561]
ལྔ་པོས་དོན་ནི་མྱོང་འདོད་དང་། །ཞེས་བྱ་བ་ལ། ལྔ་སྨོས་པས་ནི་རྟོག་པ་མེད་པའི་མིག་ལ་སོགས་པ་རྣམས་བསྡུ་བར་བལྟ་བར་བྱའོ། །

[Block 1562]
དེ་དག་གི་འདོད་པ་དང་མྱོང་བ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ལྐུགས་པ་བཞིན་དུ་ཡེ་ཤེས་གསུམ་དང་སྦྱར་བའོ། །

[Block 1563]
ཡིད་ཀྱིས་དོན་ནི་མྱོང་བ་ལྟར། །ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཡིད་ཀྱིས་དོན་ལ་རྣམ་པར་རྟོག་ཅིང་ཉམས་སུ་མྱོང་བ་ལྟར་དེའི་རྗེས་ལས་ཐོབ་པས་ཉམས་སུ་མྱོང་བ་ཡང་དེ་བཞིན་ཏེ། རྣམ་པར་རྟོག་པར་བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1564]
བསྟན་བཅོས་མ༌[^957]ཤེས་པས་བསྟན་བཅོས་འདོད་པ་ལྟ་བུ་ནི་སྦྱོར་བ་ལས་བྱུང་བའོ། །

[Block 1565]
ཇི་ལྟར་བསྟན་བཅོས་དེའི་ཆོས་དང་དོན་མྱོང་བ་ལྟ་བུ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1566]
འདིར་ཆོས་ནི་ཡི་གེ་ཙམ་དུ་བཞེད་དོ། །

[Block 1567]
ཇི་ལྟར་བསྟན་བཅོས་ཤེས་པས་ཆོས་དང་དོན་མྱོང་བ་དེ་ལྟ་བུར་ནི་དེའི་རྗེས་ལས་ཐོབ་པར༌[^958]བལྟ་བར་བྱའོ། །

[Block 1568]
གོ་རིམས་སྨོས་པ་ནི་འདིར་ཆོས་དང་དོན་དང་ཡེ་ཤེས་གཉིས་བསྟན་པ་ཡིན་ནོ། །

[Block 1569 [HEADING]]
### རྣམ་པར་མི་རྟོག་པ་དང་དེའི་རྗེས་ལས་ཐོབ་པ་གཉིས་ཀྱི་བྱེ་བྲག། ^8-15-0

[Block 1570]
མི་ཞིག་མིག་ནི་བཙུམས༌[^959]པ་ལྟར། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་ནི་རྣམ་པར་མི་རྟོག་པ་དང་། དེའི་རྗེས་ལས་ཐོབ་པ་གཉིས་པོ་དེ་དག་གི་བྱེ་བྲག་བསྟན་ཏོ། །

[Block 1571]
ནམ་མཁའ་བཞིན་དུ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་ནམ་མཁའ་ཁྱབ་པ་དང་། མ་གོས་པ་དང་། མི་རྟོག་པ་དང་། བརྟག་པར་བྱ་བ་མ་ཡིན་པ་དེ་བཞིན་དུ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱང་ཆོས་ཐམས་ཅད་ལ་རོ་གཅིག་པ་སྟོང་པ་ཉིད་ཀྱིས་ཁྱབ་པས་ན་ཁྱབ་པའོ། །

[Block 1572]
ཆོས་ཐམས་ཅད་ཀྱིས་མ་གོས་པས་ན་གོས་པ་མེད་པའོ། །

[Block 1573]
རང་ཉིད་ཀྱིས་རྣམ་པར་མི་རྟོག་པས་ན༌[^960]རྣམ་པར་རྟོག་པ་མེད་པའོ། །

[Block 1574]
གཞན་གྱིས་བརྟག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱིས་རྣམ་པར་བརྟག་པར་བྱ་བ་མ་ཡིན་པ་སྟེ། རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ནི་དེ་ལྟར་བལྟ་བར་བྱའོ། །

[Block 1575 [VERSE]]
དེ་ལ་གཟུགས་ནི་སྣང་བ་ལྟར། །
དེ་ཡི་རྗེས་ཐོབ་ཤེས་དེ་འདྲ། །

[Block 1576]
ཇི་ལྟར་ནམ་མཁའ་ལ་གཟུགས་ཀྱི་སྣང་བ་རྣམ་པར་བརྟགས་པ་ལྟར། དེ་བཞིན་དུ་དེའི་རྗེས་ལས་ཐོབ་པའི་ཡེ་ཤེས་བལྟ་བར་བྱ་སྟེ། རྣམ་པར་བརྟག་པར༌[^961]བྱ་བ་ལ་རྣམ་པར་རྟོག་པ་མེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1577 [HEADING]]
### སེམས་ཅན་གྱི་དོན་མཛད་པ་རྣམ་པར་རྟོག་པ་མེད་པ། ^8-16-0

[Block 1578]
ཡང་གལ་ཏེ་དེ་ལྟ་བུའི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་རབ་ཏུ་བསྒོས་པའི་སངས་རྒྱས་ཉིད་དེས་སེམས་ཅན་གྱི་རྣམ་པར་རྟོག་པ་མེད་པ་དེ་བཞིན་དུ། དེའི་སེམས་ཅན་གྱི་དོན་མཛད་པ་ཡང་རྣམ་པར་རྟོག་པ་མེད་པར་ཇི་ལྟར་འགྱུར་ཞེ་ན། དེ་ཚིགས་སུ་བཅད་པས་ནོར་བུ་དང་སིལ་སྙན་གྱི་དཔེས་བསྟན་པ། ཇི་ལྟར་ནོར་བུ་སིལ་སྙན་དག །ཅེས་བྱ་བ་ལ། ཇི་ལྟར་ཡིད་བཞིན་གྱི་ནོར་བུ་རྣམ་པར་རྟོག་པ་མེད་པ་བཞིན་དུ་ཡང་སེམས་ཅན་རྣམས་ཀྱི་འདོད་པའི་དོན་གྱི་ལས་བྱེད་པ་དང་། ལྷ་རྫས་ཀྱི་སིལ་སྙན་རྣམས་མ་བརྡུངས་པར་ཡང་དེར་སྐྱེས་པའི་སེམས་ཅན་རྣམས་ཀྱི་འདོད་པ་བཞིན་དུ་སྒྲ་འབྱུང་བར་འགྱུར་བ་ལྟར། སངས་རྒྱས་རྣམས་ཀྱང་རྣམ་པར་རྟོག་པ་མི་མངའ་བཞིན་དུ་ཡང་ཕྲིན་ལས་རྣམ་པ་སྣ་ཚོགས་འབྱུང་བར་འགྱུར་རོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 1579 [HEADING]]
### རྣམ་པར་མི་རྟོག་པའི་ཟབ་པ་ཉིད། ^8-17-0

[Block 1580]
རྣམ་པར་མི་རྟོག་པའི་ཟབ་པ་ཉིད་བརྗོད་པར་བྱ་སྟེ། ཅི་ཡེ་ཤེས་དེ་གཞན་གྱི་དབང་ཞེས་བརྗོད་པའི་རྣམ་པར་བརྟག་པར༌[^962]བྱ་བའི་དངོས་པོ་ལ་འཇུག་གམ། འོན་ཏེ་གཞན་ཞིག་ལ་དམིགས་དེས༌[^963]ཅིར་འགྱུར། གལ་ཏེ་རྣམ་པར་བརྟག་པར༌[^964]བྱ་བ་ལ་དམིགས་ན་ནི་དེའི་རྣམ་པར་མི་རྟོག་པ་ཉིད་མི་དམིགས་སོ། །
--- END BLOCKS ---
