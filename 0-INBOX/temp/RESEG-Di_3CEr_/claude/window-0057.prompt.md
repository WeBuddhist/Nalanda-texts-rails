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
[Block 1996]
གཏན་ཚིགས་ཀྱི་དོན་རྟག་པ༌[^1574]ལས་ཀྱང་ཐེ་ཚོམ་མཚུངས་པའི་ལྟག་སྤྱོད༌[^1575]ཡིན་ནོ། །

[Block 1997]
དཔེར་ན་སྔར་བཞིན་བྱས་པ་ལ་བརྩལ༌[^1576]མ་ཐག་ཏུ་བྱུང་བ་བསལ་བ་དང་། སྐྱེས་པ་མཐོང་བ་ལས་ཐེ་ཚོམ་དུ་འགྱུར་ཏེ། ཅི་འདི་གསལ་བར་བྱ་བ༌[^1577]ཡིན་ནམ། བསྐྱེད་པར་བྱ་བ་ཡིན་ཞེས་སོ། །

[Block 1998]
འདི་རིགས་པ་མ་ཡིན་ཏེ། གང་གཏན་ཚིགས་དེ་དག་ལས་མི་རྟག་པའོ་ཞེས་པ་དེའི་ལྟ༌[^1578]ན། བསྒྲུབ་བྱ་སྒྲོ༌[^1579]བཏགས༌[^1580]མ་ངེས་པ། །ལྟར་སྣང་། འདི་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་དམིགས་ནས་འཇིག་པ་ཉིད་དུ་སྒྲུབ་པ་ལ་གང་ཞིག་དེ་ལྟར་སྒྲོ་འདོགས་ན་མི༌[^1581]རྟག་པ་བསྐྱེད་པར་བྱ་སྟེ། དེ་ལ་ཡང་མ་ངེས་པ་ཡིན་པའི་ཕྱིར་ཐེ་ཚོམ་ཡིན་ནོ། །

[Block 1999]
འདི་ལྟར་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་དམིགས་པ་བསལ་བ་ནི་རྩྭ༌[^1582]དང་ཆུ་ལ་སོགས་པ་ལ་ཡོད་པས་དེ་མ་ངེས་པ་ལ་སྣང་བ་སྟེ། འཇིག་པ་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2000]
གསལ་བ་རྣམས་ལ་ཡང་འཇིག་པ་ཉིད་ཡོད་པ་སྟེ། དེའི་ཕྱིར་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 2001]
རྟགས་མ་གྲུབ་ལྟར་སྣང་། སྒྲོ་བཏགས་ནས་ཤེས་པར་བྱའོ། །

[Block 2002]
གལ་ཏེ་གཏན་ཚིགས་སུ་སྒྲོ་བཏགས་པར་བྱ་བའི་བརྩལ་མ་ཐག་ཏུ་བྱུང་བའི་ཕྱིར༌[^1583]སྐྱེས་པ༌[^1584]སུན་བཏོན་ན་ནི་དེ་ལས་མ་གྲུབ་པ་ལྟར་སྣང་བ་སྟེ། གཏན་ཚིགས་སུ་བརྗོད་པའི་བརྩལ༌[^1585]མ་ཐག་ཏུ་བྱུང་བར་དམིགས་པ་དེ་བརྩལ༌[^1586]མ་ཐག་ཏུ་སྐྱེས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2003 [HEADING]]
### དོན་གྱིས་གོ་བར་མཚུངས་པ། ^6-12-0

[Block 2004]
དོན་གྱིས་འདོད་མིན་མི་མཐུན་ཕྱོགས། །བསྒྲུབ༌[^1587]བརྗོད་དོན་གོ་མཚུངས། དཔེར་ན་གལ་ཏེ་རྩོལ་བ་ལས་བྱུང་བ་མི་རྟག་པ་ཡིན་ན། དོན་གྱི་ཤུགས་ཀྱི་རྩོལ་བ་ལས་མ་བྱུང་བའི་གློག་ལ་སོགས་པ་རྣམས་རྟག་པའོ་ཞེས་འགྱུར་བས་དེ་ལྟ་བུ་ནི་དོན་གྱིས་གོ་བར་མཚུངས་པའོ། །

[Block 2005]
འདི་ནི།

[Block 2006]
འཁྲུལ་པ་གཞན་གྱི་བསྒྲུབ་བྱ་ལ། །དེ་ཡིས་སྒྲུབ་པ་དེ་ལྟར་སྣང་། །

[Block 2007]
རྩོལ་བ་ལས་བྱུང་བ་ཉིད་ལས་མི་རྟག་པ་ཉིད་སྒྲུབ་པ་ལ་རྩོལ་བ་ལས་མ་བྱུང་བ་ཉིད་ལས་རྟག་པའི་དོན་དུ་སྒྲོ་འདོགས༌[^1588]པར་བྱེད་པ་དེ་ལ་ནི་མ་ངེས་པ་སྔར་སྒྲོ་འདོགས་པར་བྱེད་དོ། །

[Block 2008]
དེས་ན་མ་ངེས་པ་ལྟར་སྣང་བ་སྟེ་རྟག་པ་ལ་ཡང་གཏན་ཚིགས་ཞུགས་པ་ནི་མ་ཡིན་པས་ན་གང་ལས་བསྒྲུབ་བར་བྱ་བ་ལས་མ་ངེས་པར་འགྱུར། ཡང་ན་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་པ༌[^1589]ཉིད་དོ་ཞེས་སྒྲུབ་པ་ལ་རྩོལ་བ་ལས་བྱུང་བ་ཉིད་ལ་སོགས་པ་དེ་དག་མེད་ཀྱང་གློག་ལ་སོགས་པ་ནི༌[^1590]མི་རྟག་པ་གྲུབ་པས༌[^1591]སོ་ཞེས་རྩོད་པར༌[^1592]བྱེད་དོ། །

[Block 2009]
དེ་ཡང་མ་ངེས་པ་ལྟར་སྣང་བ་སྟེ། དེ་རྟག་པ་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2010 [HEADING]]
### ཐལ་བར་འགྱུར་བ་མཚུངས་པ། ^6-13-0

[Block 2011]
ཐལ་འགྱུར་མཚུངས་པར་འདོད་པ་ཡང་། །གང་ཡང་གཉིས་ཀ་གཏན་ཚིགས་ལམ། །

[Block 2012]
དཔེར་ན་སྔར་བཞིན་སྒྲུབ་པ་ལ་རེ་ཞིག་འདིར་བུམ་པ་ཁོ་ན་མི་རྟག་པའོ་ཞེས་པའི་གཏན་ཚིགས་གང་ཡིན་ཞེས་སོ། །

[Block 2013]
དེ་ནི་དཔེ་ལྟར་སྣང་བ་བཞིན། །དེ་བུམ་པ་མི་རྟག་པ་གྲུབ་པ་མཐོང་བ་བཞིན་དུ་ཡང་རྩོད་པ་ནི་བསྒྲུབ་བྱའི་རྗེས་འགྲོ་མེད་པའི་དཔེ་ལྟར་སྣང་བར་རིགས་པའི་ཕྱིར་དེ་ལྟ་བུ༌[^1593]དེ་ལྟར་སྣང་བ་སྟེ། གོང་དུ་འབྲས་བུ་མཚུངས་པར་གཏན་ཚིགས་ཀྱི་རྗེས་འགྲོ་བརྗོད་ཟིན་ཏོ། །

[Block 2014 [HEADING]]
### ལྟག་གཅོད་ཀུན་ལ་ཕྱོགས་ཙམ། ^6-14-0

[Block 2015]
དེ་དག་ནི། ལྟག་གཅོད༌[^1594]ཀུན་ལ་ཕྱོགས་ཙམ་མོ། །

[Block 2016]
ཇི་ལྟར་ལྟག་གཅོད་དེ་དག་རྣམས་ལ་མ་ཚང་བ་ལ་སོགས་པ་ལྟར་སྣང་བ་ཉིད་ཀྱིས་མི་རིགས་པར་ལན་བརྗོད་པ་དེ་བཞིན་དུ་ལྷག་པ༌[^1595]མཚུངས་པ་ལ་སོགས་པ་གཞན་རྣམས་ལ་ཡང་ངོ་། །དེ་དག་ཉིད་ལ་སྦྱོར་བའི་བྱེ་བྲག་ཅུང་ཟད་ཙམ་གྱིས་དབྱེ་བས༌[^1596]མཐའ་ཡས་པར་འགྱུར་རོ། །

[Block 2017]
དེ་ལ་ཁོ་བོ་ཅག་གིས་མ་ཚང་བ་ལྟར་སྣང་བ་དང་། མ་གྲུབ་པ་ལྟར་སྣང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་དག་བརྗོད་པ་དེ་ནི་རྗོད་པར་བྱེད་པ་ལ་བརྗོད་པར་བྱ་བ་བརྟགས༌[^1597]ནས་ཡིན་ཏེ། དེ་ལྟར་མ་ཡིན་ན་མ་ཚང་བ་ཉིད་དུ་རྩོད་པ་ལྟར་སྣང་བ་དང་མ་གྲུབ་པ་ཉིད་དུ་རྩོད་པ་ལྟར་སྣང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཉིད་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 2018]
དེ་ལྟ༌[^1598]ན་ཡང་གཞུང་མངས་པར་འགྱུར་ཏེ། འདི་ལྟར་གང་ཁ་ཅིག་ཏུ་ལྟག་གཅོད༌[^1599]དེ་མ་རྟོགས་ཀྱིས་བསྟན་ནས་དེ་དེ་དང་འབྲེལ་བར་འགྱུར་བའི་ཕྱིར་དང་། གང་མ་ནིང་གི་རྟགས་ཀྱིས་བསྟན་ནས་ལན་ཡང་དེ་དང་མངོན་པར་འབྲེལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2019]
མཚུངས་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཐམས་ཅད་ཀྱི་མཇུག་བསྡུ་བར་ལྟག་གཅོད་རྣམས་ལ་ཐལ་བར་འགྱུར་བར་མཚུངས་པར་རིག་པར་བྱའོ། །

[Block 2020]
དེ་ལྟར་རེ་ཞིག་ཁོ་བོ་ཅག་གིས་ལྟག་གཅོད་རྣམས་ལ་མ་ཚང་བ་ལྟར་སྣང་བ་དང་། མ་གྲུབ་པ་ལྟར་སྣང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་དག་བརྗོད་དོ། །

[Block 2021]
ལྟག་གཅོད༌[^1600]

[Block 2022 [HEADING]]
### ལྟག་གཅོད་རྣམས་ལ་སྐྱོན་གསུམ། ^6-15-0

[Block 2023 [VERSE]]
རྣམས་ལ་རྩོད་སྒྲུབ་ཏུ། །
ཕྱིན་ཅི་ལོག་དང་བརྫུན་ཉིད་དང་། །
འགལ་བ་ཉིད་དེ་སྐྱོན་གསུམ་སྟེ། །
གསུམ་པོ་ཐ་དད་དུ་མཚོན་མིན། །

[Block 2024]
རྩོད་པ་སྒྲུབ་པར༌[^1601]ནི་ཕྱིན་ཅི་ལོག་དང་། ཡང་དག་པ་མ་ཡིན་པ་ཉིད་དང་འགལ་བ་ཉིད་རྣམས་ཀྱིས་ལན་སྐྱོན་བརྗོད་པ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 2025 [HEADING]]
#### ཕྱིན་ཅི་ལོག། ^6-15-1-0

[Block 2026]
དེ་ལ་ཕྱིན་ཅི་ལོག་ནི་ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་དང་རྣམ་པར་རྟོག་པ་དང་། བྱེ་བྲག་མེད་པ་དང་ཕྲད་པ་དང་། མ་ཕྲད་པ་རྣམས་ལ་ནི་གཏན་ཚིགས་དམིགས་ཤིང་། འབྲས་བུ་མཚུངས་པ་ལ་སོགས་པ་ནི་ཐེ་ཚོམ་དུ་བརྗོད་དོ། །

[Block 2027]
དེ་ལ་བཞི་པོ་རྣམས་ཀྱིས་ཕྱིན་ཅི་ལོག་ཉིད་ནི་འདི་ལྟར་ཕྱོགས་གཅིག་ཏུ་ངེས་པའི་གཏན་ཚིགས་ཀྱི་རྗེས་སུ་དཔོག་པར་བརྗོད་ལ། མ་ངེས་པ་ནི༌[^1602]ཆོས་མཐུན་པ་ལ་སོགས་པས་འགལ་ཟླ་འཇོག་པར་བྱེད་དོ། །

[Block 2028]
ཕྱོགས་གཅིག་ཏུ་ངེས་པ་ནི་ཇི་ལྟར་མ་ངེས་པ་དང་ཕྱིན་ཅི་ལོག༌[^1603]བཞིན་དུ་འགལ་ཡང་ལྷན་ཅིག་མི་གནས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2029]
བདེན་ན་ཡང་དོན་ཕྱོགས་གཅིག་ཏུ་ངེས་པར་སྦྱོར་བའི་ལྟ་ན་མ་ངེས་པ་ཡིན་པས་བརྫུན་ཡིན་ཡང་རྣམ་པར་རྟོག་པ་མཚུངས་པར་བརྗོད་ནུས་སོ། །

[Block 2030]
དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། བསྲེག་པར་བྱ་བ་ཉིད་ལ་སོགས་པ་མེད་པར་མ་མཐོང་བ་མཐོང་བ༌[^1604]མ་ཡིན་ཏེ། རླུང་ཡབ་ཀྱི་རླུང་ལ་སོགས་པ་ནི་མི་རྟག་པ་ཉིད་དོ་ཞེས་འབྱུང་བས་སོ། །

[Block 2031]
གཞན་གྱིས་ནི་བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་དང་། མིག་གིས་གཟུང་བྱ་མ་ཡིན་པ་ཉིད་ལ་སོགས་པས་སྒྲ་རྟག་པ་ཉིད་དོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 2032]
བསྲེག་པར་བྱ་བ་ཉིད་ལ་སོགས་པས་བུམ་པ༌[^1605]མི་རྟག་པ་ཉིད་དུ་ནི༌[^1606]མ་ཡིན་ནོ། །

[Block 2033]
དེ་ལ་འདི་སྐད་བརྗོད་པར་བྱ་སྟེ། བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་རྟག་པ་ཁོ་ནར་མཐོང་བ་ནི་མེད་ཀྱི།[^1607] འོན་ཀྱང་རྟག་པ་ལའོ་ཞེས་སོ། །

[Block 2034]
དེ་ལྟར་ནི་གཞན་གྱི་ཕྱོགས་ལ་མ་ངེས་པ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2035]
འདི་སྔ་མ་ཉིད་ལ་ཁྱབ་པར་བྱེད་པ་ཡིན་ལ་ཁྱབ་བྱེད་མ་ཡིན༌[^1608]པ་གཏན་ཚིགས་མ་ཡིན་ནོ། །
--- END BLOCKS ---
