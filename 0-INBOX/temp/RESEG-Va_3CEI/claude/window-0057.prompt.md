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
ཉན་ཐོས་པ༌[^1650]རྣམས་ནི་བུས་པ༌[^1651]མང༌[^1652]དུ་བླངས་ཏེ་སྒོར་འབྱིན་པ་བཞིན་མངོན་པར་ཤེས་པའི་མཐུས་ཐེག་པ་ཆེན་པོ་ལ་འཛུད་དོ། །

[Block 1997 [HEADING]]
###### **རྒྱུ་བསྟན་ཏེ་འཛུད་པ།** ^4-3-5-4-1-1-1-3-1-2-0

[Block 1998]
མདོ་ལས་དེ་ཡང་འདི་སྙམ་དུ་སེམས་ཏེ་ཁང་པ་འདི་སྲང་གཅིག་ལ་སྒོ་ཡང་དོག་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་རྒྱུད་བསྟན་ཏེ་འཛུད་པ་སྟེ། དེ་ལས༌[^1653]རྒྱུ་བསྟན་པ་ཡང་ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ཆེན་པོ་ལ་བརྟེན་པ་དང་། སྐུར་བའི་སེམས་སྐྱེས་ན་ངན་སོང་དུ་ལྟུང་བར་བསྟན་པ་དང་། དཀའ་བ་སྣ་ཚོགས་སྟོན་ཅིང་ཐེག་པ་ཆེན་པོ་ཉིད་གསངས་ཏེ་སྨོན་པ༌[^1654]དང་གསུམ་ལས༌[^1655]འདི་ནི་དང་པོའོ། །

[Block 1999 [HEADING]]
###### **ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ཆེན་པོ་ལ་བརྟེན་པ།** ^4-3-5-4-1-1-1-3-1-2-1-0

[Block 2000]
ཁམས་གསུམ་ནས་འབྱུང་བའི༌[^1656]སྲང་ཐེག་པ་ཆེན་པོ་གཅིག་ཡིན་པའི་ཕྱིར་སྲང་གཅིག་ཅེས་པ་དང་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་ཉན་ཐོས་པའི་སྤྱོད་པས་མི་ཆུད་པའི་ཕྱིར་སྒོ་ཡང་དོག༌[^1657]པ་ཞེས་སྨོས་ཏེ། རྒྱ་མཚོ་ཤིན་ཏུ་ཡངས་ཀྱང་མི་རོ་ཞག་ཏུ་མི་འཇོག་པ༌[^1658]བཞིན་ནོ། །

[Block 2001 [HEADING]]
###### **སྐུར་བའི་སེམས་སྐྱེས་ན་ངན་སོང་དུ་ལྟུང་བ།** ^4-3-5-4-1-1-1-3-1-2-2-0

[Block 2002]
མདོ་ལས་ཁྱེའུ་འདི་དག་ཀྱང་ཞེས་པ་ནས་བྱིས་པ་དེ་དག་ལ་འབོད་དེ་ཞེས་པའི་བར་དུ་ནི་གང་འདི་ལ་མ་དད་པ་རྣམས་ངན་སོང་དུ་ལྟུང་བ་བསྟན་པ་སྟེ། སེམས་ཅན་རྣམས་འཇིག་རྟེན་ལས་འབྱུང་བའི་རྒྱུད༌[^1659]ཡོད་དུ་ཟིན་གྱིས་ཀྱང་འབྱུང་བར་རྩོལ་བ་མེད་པས་ན་བྱིས་པ་ཞེས་བྱའོ། །

[Block 2003]
ཇི་ལྟར་བྱིས་པ་ལེགས་ཉེས་ཀྱི་བྱེ་བྲག་མི་ཤེས་པ་བཞིན་ཐེག་པ་ཆེན་པོ་འདིའི་ཡོན་ཏན་མ་རྟོགས་ཤིང་། སྐུར་པའི་སེམས་བསྐྱེད་པ༌[^1660]རྣམས་སྡུག་བསྔལ་སྣ་ཚོགས་མྱོང་བ་ཡང་ཇི་ལྟར་མེའི་ཕུང་པོ་ལས་བྱོལ་བར་མི་སེམས་པའི་བྱིས་པ་བཞིན་ནོ། །

[Block 2004 [HEADING]]
###### **ཐེག་པ་ཆེན་པོ་གསངས་ཏེ་བསྟན་པ།** ^4-3-5-4-1-1-1-3-1-2-3-0

[Block 2005]
མདོ་ལས་ཁྱིམ་འདི་ལ་ཞེས་པ་ནས་ཚུར་ཤེག༌[^1661]ཕྱིར་འབྱུང་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་ལ་ཐེག་པ་ཆེན་པོ་གསངས་ཏེ་བསྟན་པའི་དཔེ་དང་། ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་བསྟན་ཏེ་འཛུད་པ་སྟོན་པ་ལ་དེ་ཡན་ཆད་རྒྱུ་དང་འབྲས་བུ་དང་སྤྱོད་པ་ལ་གཟུད་པའི་དཔེ་བསྟན་ཏོ། །

[Block 2006]
མདོ་ལས་དེ༌[^1662]ལྟར་ཕན་པར་འདོད་པའི་སྐྱེས་བུ་དེས་ཞེས་པ་ནས་ཁྱིམ་འདི་ནས་གདོན་ཏོ་སྙམ་ཞེས་པའི་བར་དུ་ནི་ཕུང་པོ་ལྔ་ལ་ཆགས་ཤིང་ཉོན་མོངས་པ་སྣ་ཚོགས་ཀྱི་མེས༌[^1663]གདུང་བར་བྱེད་པའི་ཕྱིར་ཚུལ་བཞིན་མ་ཡིན་པའི་མེས་ཚིག་ཅེས་པའི་དོན་ཏོ། །

[Block 2007]
[^1664]སྙམ་པ་ནི་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་རྣམས་མྱ་ངན་ལས་འདས་པའི་བདེ་བ་བརྙེས་པའི་ས་ན་བཞུགས་པ་བཞིན་སེམས་ཅན་ཐམས་ཅད་ཀྱང་ས་དེར་གདོན་ཅིང་འཇོག་ཅེས་པའི་དོན་ཏོ། །

[Block 2008 [HEADING]]
###### **ཐེག་པ་རྣམ་གསུམ་དངོས་སུ་བཤད་པའི་དཔེ།** ^4-3-5-4-1-1-1-3-2-0

[Block 2009]
མདོ་ལས་སྐྱེས་བུ་དེས་བྱིས་པ་དེ་དག་གི་བསམ་པ་ཤེས་ཞེས་པ་ནས་རྣམ་པ་དུ་མ་ཡིན་ན་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་རྣམ་གསུམ་དངོས་སུ་བཤད༌[^1665]པའི་དཔེ་སྟོན་པར་གླེང་པ་ལ་སྔར་སོ་སོའི་དབང་པོ་ཤེས་པ་དང་། ཕྱིས་དངོས་སུ་སྟོན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2010 [HEADING]]
###### **སོ་སོའི་དབང་པོ་ཤེས་པ།** ^4-3-5-4-1-1-1-3-2-1-0

[Block 2011]
བྱིས་པ་དེ་དག་གི་བསམ་པ་དང་དད་པ་རིག་ནས་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གསུམ་གྱི་རིགས་ཤེས་པ་སྟེ། དབང་པོ་མཐོ་དམན་ཤེས་པའོ། །

[Block 2012]
མཛེས་པ་དང་སྡུག་པ་དང་ཡིད་དུ་འོང་བ་དང༌[^1666]ཞེས་པ་ནི་ཐེག་པ་རྣམ་གསུམ་གྱི་དོན་ཏོ། །

[Block 2013 [HEADING]]
###### **དངོས་སུ་སྟོན་པ།** ^4-3-5-4-1-1-1-3-2-2-0

[Block 2014]
མདོ་ལས་དེ་དག༌[^1667]དཀོན་པར་གྱུར་ཏེ་ཞེས་པ་ནས་མྱུར་དུ་བརྒྱུགས་ཏེ་ཤོག༌[^1668]ཤིག་ཅེས་པའི་བར་དུ༌[^1669]ཐེག་པ་རྣམ་གསུམ་གྱི་དཔེ་ཤིང་རྟ་རྣམ་གསུམ་དང་སྦྱར་ཏེ་སྟོན༌[^1670]ལ་སྔར་སྦྱིན་ནོ་བྱ་བར་གླེང་པ་དང་། རྣམ་གསུམ་གྱི་མིང་བསྟན་པ་དང་། དངོས་སུ་བྱིན་པ་དང་གསུམ་དུ་བགོ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 2015]
ཐེག་པ་རྣམ་པ༌[^1671]གསུམ་གྱི་མཐུ་དང་སྤྱོད་རླབས་ཁྱད་པར་ཡོད་པའི་ཕྱིར་དཔེ་ཡང་བཟང་ངན་གསུམ་དུ་བཀོད་དོ། །

[Block 2016]
ཕྱི་སྒོར་བཀོད་ཅེས་པ་ནི་འཇིག་རྟེན་གྱི་དགེ་བའི་རྩ་བ་སྣ་ཚོགས་དང་ཏིང་ངེ་འཛིན་གྱི་ཡོན་ཏན་ཐམས་ཅད་ཐེག་པ་དེ་གསུམ་གྱི་སྒོ་ནས་འཇུག་ཅིང་འཐོབ་པའི་ཕྱིར་སྒོ་ཞེས་བྱའོ། །

[Block 2017]
བསྟན་པ་འདི་ལ་བརྟེན༌[^1672]ཏེ་ཐེག་པ་རྣམ་གསུམ་གྱིས༌[^1673]མྱ་ངན་ལས་འདའ་བའི་འབྲས་བུ་ཕྱིས་ཐོབ་པར་བྱེད་པའི་ཕྱིར་ཕྱི་སྒོར་བཀོད་ཅེས་བྱ་སྟེ། རྒྱུ་ལ༌[^1674]བརྟེན་ཏེ་འབྲས་བུ་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 2018]
ཐེག་པ་འདི་རྣམ་གསུམ་ཡང་སྐྱེད་པ་དང་ཕྱིན་པར་བྱེད་པའི་དོན་དུ་འདྲ་བས་ཇི་ལྟར་ཤིང་རྟ་ཡང་མང་ཉུང་སྐྱེད་པ༌[^1675]ལ་མི་འདྲ་ཡང་སྤྱིར་ཤིང་རྟ་ཞེས་མིང་གཅིག་སྟེ། འདུས་མ་བྱས་ལ་དབྱེ་བ་མེད་མོད་ཀྱི་འདུས་བྱས་ཀྱི་སྒོ་ནས་ཆེ་ཆུང་རིམ་པར་དབྱེ་བའི་ཕྱིར་གླང་དང་ར་དང་རི་དགས་ཀྱི་ཤིང་རྟ་ཞེས་སྨོས་སོ། །

[Block 2019 [HEADING]]
###### **ཁམས་གསུམ་ལས་ཐར་པའི་དཔེ།** ^4-3-5-4-1-1-1-4-0

[Block 2020 [HEADING]]
###### **བུས་པ་རྣམས་ཉོན་མོངས་པ་ལས་ཐར་བ།** ^4-3-5-4-1-1-1-4-1-0

[Block 2021]
མདོ་ལས་དེ་ནས་བྱིས་པ༌[^1676]དེ་དག་ཅེས་པ་ནས་དེ་ནས་མྱུར་དུ་ཕྱིར་འཐོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་གསུངས་རབ༌[^1677]ལ་བརྟེན་པས་ཁམས་གསུམ་ལས་ཐར་པའི་དཔེ་བསྟན་ཏེ། དེ་ཡང་བུས་པ༌[^1678]རྣམས་ཉོན་མོངས་པ་ལས་ཐར་བ་དང་། ཕ་བདེ་བར་འདུག་པའི་དཔེས་སེམས་ཅན་རྣམས་ཐེག་པ་རྣམ་གསུམ་ལ་བཀོད་པས་བཅོམ་ལྡན་འདས་དགྱེས་ཞེས་པའི་དོན་ཏོ། །

[Block 2022]
གཅིག་གིས་གཅིག་བདས༌[^1679]ཤིང་བརྒྱུགས་ཏེ་ཞེས་པ་ནི་བརྩོན་འགྲུས་ཆེན་པོ་རྩོལ་བ་བསྟན་ཏོ། །

[Block 2023 [HEADING]]
###### **ཕ་བདེ་བར་འདུག་པ།** ^4-3-5-4-1-1-1-4-2-0

[Block 2024]
མདོ་ལས་དེ་ནས་སྐྱེས་བུ་དེས་ཞེས་པ་ནས་འཇིགས་པ་མེད་པ་ཐོབ་པར་གྱུར་ཏེ་ཞེས་པའི་བར་དུ། དཔོང་ས་བཞི་མདོ་ཞེས་པ༌[^1680]ནི། བདེན་པ་རྣམ་བཞིའི་དོན་བསྟན་པའོ། །

[Block 2025]
འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པས་ཉོན་མོངས་པ་ལས་རྣམ་པར་གྲོལ་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པ་ཤེས་བྱའི་སྒྲིབ་པ་ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་སྐྱབས་དང་སྒྲིབ་པ་མེད་པ་ནི་བླ་གབ་མེད་པར་གནས་པ་བཞིན་ནོ། །

[Block 2026 [HEADING]]
###### **ངེས་པའི་དོན་གྱི་དཔེ།** ^4-3-5-4-1-1-2-0

[Block 2027]
མདོ་ལས་དེ་ནས་བྱིས་པ་དེ་དག་ཅེས་པ་ནས་བདག་ཅག་སྩལ་དུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་དཔེ་སྔ་མས་ནི་དྲང་བའི་དོན་བསྟན། དཔེ་འདིས་ནི་ངེས་པའི་དོན་སྟོན་ཏེ། དེ་ཡང་བུ་རྣམས་ཀྱིས་སྦྱིན་པར་བྱས་པ་དེ་བསླངས་པ་དང་། ཕས་གཅིག་བྱིན་པ་བསྟན་པ་དང་། ཕས་བསམས་པའི་དོན་དང་བུས་པ༌[^1681]རྣམས་ཀྱི་བསམ་པ་དང་འགལ་བ་དང་བཞིར་དབྱེ་བ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2028 [HEADING]]
###### **བུ་རྣམས་ཀྱིས་སྦྱིན་པར་བྱས་པ་དེ་བསླངས་པ།** ^4-3-5-4-1-1-2-1-0

[Block 2029]
ཐེག་པ་རྣམ་པ༌[^1682]

[Block 2030]
གཉིས་པ་དག་ནི་ཕུང་པོ་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བ་ཐོབ་ཏུ་ཟིན་གྱིས༌[^1683]ཀྱང་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་མ༌[^1684]ཐོབ་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་མ་ཐོབ་པ་དེ་གཉིས་ཀྱི་དཔེར་བུས་པ༌[^1685]ཕྱིར་འཐོན་པ་རྣམས་ཕ་ལ་སོ་སོ་ནས་སྔར་བྱིན་པར་བྱ་བ་དེ་བསླངས༌[^1686]ཞེས་པར་སྦྱར་རོ། །

[Block 2031]
ཡང་ན་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་ཏུ་ཟིན་གྱིས་ཀྱང་ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདས་པ་མ་ཐོབ་པའི་ཕྱིར་སྦྱིན་པར་བྱས་པ་དེ་བླངས་སོ། །

[Block 2032 [HEADING]]
###### **ཕས་ཀུན་ལ་འདྲ་བར་བྱིན་པ།** ^4-3-5-4-1-1-2-2-0

[Block 2033]
མདོ་ལས་དེ་ནས་ཤཱ་རིའི་བུ་སྐྱེས་བུ་དེས་ཞེས་པ་ནས་བདག་གི་བུ་རྣམས་ལ་རླུང་ལྟར་མགྱོགས་ཤིང་མཐུ་དང་ལྡན་པའི་གླང་པོ་ཆེའི་ཤིང་རྟ་བྱིན་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཕས་ཀུན་ལ་འདྲ་བར་བྱིན་པ་བསྟན་ཏེ་དེ་ཡང་ཤིང་རྟ་བྱིན་པ་དང་། དེའི་རྒྱན་དང་གླང་དེའི་མཚན་དང་དེའི་འཁོར་བསྟན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2034 [HEADING]]
###### **ཤིང་རྟ་བྱིན་པ།** ^4-3-5-4-1-1-2-2-1-0

[Block 2035]
གླང་པོ་ཆེའི་ཤིང་རྟ་ནི་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་བསྟན་ཏེ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཅན་ནམ༌[^1687]ཡེ་ཤེས་བཞི་དང་ལྔའི་དངོས་པོའོ། །
--- END BLOCKS ---
