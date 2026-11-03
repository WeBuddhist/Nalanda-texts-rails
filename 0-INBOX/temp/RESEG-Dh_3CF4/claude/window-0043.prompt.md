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
[Block 1506]
དྲང་པོའི་རིམ་པ༌[^853]མི་མཐུན་བ་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། གཟུ་ལུམས་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1507]
འདུལ་བ་དང་མི་མཐུན་པ༌[^854]ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1508 [VERSE]]
འདུལ་བ་ལ་བརྩོན་འགྲུས་ཆུང་ཞེས་པའི་ཕྱིར་རོ། །
མཁས་པའི་ང་རྒྱལ་གཏི་མུག་མེས་བསྲེགས་ཤིང་། །

[Block 1509]
ཞེས་བྱ་བ་ནི་བདག་ཉིད་གཞན༌[^855]གྱི་ཐད་དུ་སོང་ནས་ཕན་པའི་དྲི་བའི་ཚིག་སྒྲུབ་པ་མེད་པའི་ཕྱིར་ཏེ། དེས་ན་དེ་ཉིད་ཀྱིས་བདག་ཀྱང་ལོག་པར་སྒྲུབ་པར་བྱེད་ལ། གཞན་ཡང་དེ་ལ་སྦྱོར་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1510]
བརྟན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 1511]
གཡོ་སྒྱུ་མེད་པ་ནི་འདུལ་བས་རྟག་ཏུ་བརྒྱན་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་འདུལ་བ་དང་། དྲང་པོའི༌[^856]རིམ་པ་མི་མཐུན་པ་ཞེས་བྱ་བ་དེའི་གཉེན་པོའོ། །

[Block 1512]
ཕན་པའི་བསམ་བ་དང་ཞེས་བྱ་བ་ནི་ཅི་ནས་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 1513]
ཕན་འདོགས་པར་བྱེད་པ་དེ་ཡང་གལ་ཏེ་ཟང་ཟིང་དང་བཅས་པའི་སེམས་ཀྱིས་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། གུས་དང་ཞེས་སྨོས༌[^857]པས་སོ། །

[Block 1514]
མཐུ་ཡང་ཅི་ཡོད་ཅེས་བྱ་བ་ནི་ནུས་པས་ཕན་འདོགས་པ་སྟེ། རྒྱུ་འདི་གསུམ་གྱིས་ནི་ཕན་འདོགས་པར་འདོད་པ་ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས༌[^858]ནུས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1515]
སྦྱིན་ལ་དགའ་བ་དེས་ངེས་པར་གྱུར་པ་ནི་སྦྱིན་པ་ལ་དགའ་བ༌[^859]དང་མཐུན་པར་གྱུར་པའོ། །

[Block 1516]
སྦྱིན་པ་དང་མི་མཐུན་པ་ནི་བསྙེན་བཀུར་མ་ཡིན་པ་འདོད་པས་སོ། །

[Block 1517]
བཟླས་བརྗོད་བརྟུལ་ཞུགས་དཀའ་ཐུབ་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་འཇིག་རྟེན་ན་བསྙེན་བཀུར་དུ་མས་ང་ལ་མཆོག་སློང་བའི་ཕྱིར་འོང་ཞིང་མཐོང་བར་འདོད་དོ་ཞེས་བསྟན་པའི་ཚིག་རྐང་དེ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 1518]
མཆོག་སྦྱིན་པར་འོས་པ་ལ་ཞེས་བྱ་བ་འདིའི་ལན་ནི་འདི་ནི་མི་སྲུན་པའི་ཚུལ་མ་ལགས་ཞེས་པའོ། །

[Block 1519]
བཟླས་བརྗོད་བརྟུལ་ཞུགས་མཆོད་སྦྱིན་དཀའ་ཐུབ་སྤྱད་པ་ཡིས། །ཞེས་བྱ་བ་འདིའི་ལན་ནི། མགུ་བར་མ་བགྱིས་པ་ཡང་མ་ལགས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1520]
ཁྱོད་ནི་མཐོང་བར་མི་འདོད་ཅི་ཡི་ཕྱིར། །ཞེས་བྱ་བ་འདིའི་ལན་ནི། ཁྱོད་དང་ཕྲད་པར་མི་འཚལ་བ་ཡང་མ་ལགས་སོ། །

[Block 1521]
[^860]ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1522]
རྗེས་སུ་མཐུན་པའི་དངོས་པོའི་རྒྱུ་ནི་བསྟན་པར་མི་བྱ་སྟེ། རང་བཞིན་གྱིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1523]
ད་ནི་ཕྲད་པར་མི་འདོད་པ་མ་ཡིན་ན་ཇི་ལྟར་མཐོང་བར་མི་འདོད་པ་ཡིན་ཞེ་ན། ཕྲད་པར་འདོད་པའི་རྒྱུ་ཡོད་ན་ཡང་མི་མཐོང་བའི་མཆོག་སློང་བའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ལྷའི་གཟུགས་མཆོག་རྨད་དུ་བྱུང་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གང་མཐོང་བར་མི་འདོད་པའི་རྒྱུ་དེ་ཉིད་ཡིན་ནོ་ཞེས་བསྟན་ཏེ། ལྷའི་གཟུགས་མཆོག་རྨད་དུ་བྱུང་བ་ཞེས་བྱ་བ༌[^861]འདིས་ནི་དབྱིབས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1524]
གསལ་བ་གང་ཡིན་པ་དེ་ནི་གསལ་བའོ། །

[Block 1525]
གཟི་བརྗིད་དང་མདངས་ཀྱིས་ནི་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1526]
འདི་གཉིས་མཐོང་བར་མི་འདོད་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། བདག་གི་དཀའ་ཐུབ་ཉམས་པར་གྱུར་དུ་དོགས་ལགས་མོད། །ཅེས་བྱ་བ་འདིས་སོ། །

[Block 1527]
རབ་ཏུ་དང་ཞིང་ཞི་བར་གྱུར་པ་ཡང་། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པ་ཉིད་ཀྱི་གསལ་བའོ། །

[Block 1528]
དེ་ཉིད་བསྟན་པ་སྐྱེ་བོ་དཀའ་ཐུབ་ཅན་དང་མཐུན་པའི་ཚུལ་དག་དང་། ཞེས་བྱ་བ་ནི་སྡོང་བུ་དང་། རྩ་བ་དང་། འབྲས་བུ་ལ་སོགས་པ་འདི་དག་གིས་འཕགས་པའི་རིགས་གསུམ་བསྟན་ཏེ། ཁ་ཟས་ངན་ངོན་ཙམ་གྱིས་ཆོག་ཤེས་པ་དང་། གནས་མལ་ངན་ངོན་ཙམ་གྱིས་ཆོག་ཤེས་པ་དང་། ཆོས་གོས་ངན་ངོན་ཙམ་གྱིས་ཆོག་ཤེས་པའོ། །

[Block 1529]
བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། སྡོམ་པ་ཞེས་བྱ་བས་ནི་སྤོང་བ་ལ་དགའ་བའི་འཕགས་པའི་རིགས་བསྟན་ཏོ། །

[Block 1530]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཨ་ཀ་ཏའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 1531 [HEADING]]
## བྱམས་པའི་སྟོབས་ཀྱི་སྐྱེས་པའི་རབས། ^8-0

[Block 1532]
བདག་གི་ཆེ་བ་ཉིད་ཀྱིས་སྙིང་རྗེ་དང་ལྡན་ཞིང་། ཞེས་བྱ་བ་ལ། བདག་ཉིད་ཀྱི་ཆེ་བ་ནི་བདག་གི་ཆེ་བའོ། །

[Block 1533]
དེ་གང་ཡིན་ཞེ་ན། རིགས་ཀྱི༌[^862]ཤེས་རབ་ཆེ་བའོ། །

[Block 1534]
རིགས་དེ་གང་ཡིན་ཞེ་ན། མིང་དང་། རྒྱུ་དང་། ས་བོན་དང་། བྱེད་པ་དང་། ཁམས་ཞེས་བྱ་བ་ནི་དོན་གཞན་མ་ཡིན་ནོ། །

[Block 1535]
གང་རྒྱུ་ཡོད་པ་ལས་ནི་ཐེག་པ་གསུམ་གྱིས་མྱ་ངན་ལས་འདའ་བར་འགྱུར། བདག་ཉིད་ཀྱི་ཆེ་བ་དང་སྙིང་རྗེ་རྣམ་པ་གཉིས་ཡོད་པ་ནི་ལྡན་པ་སྟེ། མངོན་པར་གྲུབ་པ་དང་། རབ་ཏུ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་དོན་གཞན་མ་ཡིན་ནོ། །

[Block 1536]
འགྲོ་བ་ཡོངས་སུ་སྐྱོབ་པར་བྱེད་པས་འགྲོ་བ་ཡོངས་སུ་སྐྱོབ་པའོ། །

[Block 1537]
ཤས་ཆེ་བའི་བསམ་པ་སྟེ། ས་ལ་འཇུག་པའི་དུས་སུ་བསམ་པ་དེས་འགྲོ་བ་ཡོངས་སུ་བསྐྱབ་པའི་ལྷག་པའི༌[^863]བསམ་བ་ཅན་ཏེ། མངོན་པར་འཕེལ་བར་བྱེད་པ་ལྟ་བུའོ། །

[Block 1538]
སྦྱིན་པ་དང་། དུལ་བ་དང་། དེས་པ་ལ་སོགས་པ་གང་ཡིན་པའི་ཡོན་ཏན་ནི་སྦྱིན་པ་དང་། དུལ་བ་དང་། དེས་པ་དང་། ཡང་དག་བར་སྡོམ་པ་ལ་སོགས་པའོ། །

[Block 1539]
དུལ་བ་དང་སྡོམ་པ་གཉིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། དུལ་བ་ནི་དབང་པོའི་སྒོ་བསྡམས་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ཀྱི་འཁོར་ཞེས་བྱ་བས་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ནང་དུ་འདུས་པ་ཉིད་དོ། །

[Block 1540]
སྡོམ་པ་ཡང་ཚུལ་ཁྲིམས་ཉིད་དེ། ལུས་དང་ངག་གི་ཡང་དག་པར་སྡོམ་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
