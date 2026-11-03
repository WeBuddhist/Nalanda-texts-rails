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
ལྟུང་བ་མི་འཆབ་པ་ནི་ཚུལ་ཁྲིམས་ཡང་དག་པར་བླངས་པ་ལས་ཉམས་པར་གྱུར་པ་རྣམས་གཞན་ལ་མཐོལ་བའོ། །

[Block 1997]
སྡིག་པ་འཆགས་པ་ནི་མཚམས་མེད་པ་ལ་སོགས་པའི་སྡིག་པ་བྱས་པ་འགྱོད་པའི་ཡིད་ཀྱིས༌[^1762]འཆགས་པའོ། །

[Block 1998]
བཞུགས་པ་ནི་ད་དུང་འཇིག་རྟེན་ན༌[^1763]བཞུགས་པའོ། །

[Block 1999]
མྱ་ངན་ལས་འདས་པ་ནི་སངས་རྒྱས་ཀྱི་བྱ་བ་མཛད་ནས་མྱ་ངན་ལས་འདས་པའོ། །

[Block 2000]
མཆོད་པ་ནི་གདུགས་དང་རྒྱལ་མཚན་དང་ན་བཟའ་ལ་སོགས་པས་མཆོད་པའོ། །

[Block 2001]
རིམ་གྲོ་ནི་བསྐོར་བ་དང་ཕྱག་འཚལ་བ་ལ་སོགས་པ་བྱེད་པའོ། །

[Block 2002]
སྟོན་པ་བཞིན་དུ་ཕངས་པར་འཛིན་པ་ནི་འཁོར་བ་ལས༌[^1764]འབྱིན་པར་བྱེད་པའི་སྟོན་པ་ཕངས་པ་བཞིན་དུ་མཁན་པོ་དང་སློབ་དཔོན་ལ་ཡང༌[^1765]ཕངས་པར་བྱེད་པའོ། །

[Block 2003]
རིན་པོ་ཆེ་ཚོལ་བ་ལྟར་བརྩོན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རིན་ཐང་མེད་པའི་རིན་པོ་ཆེ་རྒྱ་མཚོར་སྲོག་ལ་འབབ་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་རྣམས་ཀྱང་ཉམས་སུ་བླངས་ནས་བདོག་པ་ཐམས་ཅད་བཏང་སྟེ༌[^1766]རིང་དུ་སོང་ནས་ཚོལ་བ་ལ་འབད་པ་དེ་བཞིན་དུ་ཆོས་རིན་པོ་ཆེ་ཡང་ལུས་དང་སྲོག་ལ་ཡང་མི་ཕངས་པར་བྱ་སྟེ། ཤིན་ཏུ་རིང་དུ་སོང་ནས་ཀྱང་ཚོལ་བ་ལ་འབད་པར་བྱེད་པའོ་སངས་རྒྱས་བཞིན་དུ་ཕངས་པར་འཛིན་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དང་འདྲ་བར་ཆོས་སྟོན་པ་རྣམས་ལ་ཡང་ཕངས་པར་བྱེད་པའོ། །

[Block 2004]
དཔག་ཚད་བརྒྱར་ཞེས་བྱ་བ་ནི་མཚོན་པའི་ཚིག་ཙམ་དུ་ཟད་དེ་དེ་བས་ཀྱང་རིང་དུ་སོང་ཞིང་ཆོས་ཉན་པའོ། །

[Block 2005]
དཔེ་མཁྱུད་མེད་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་ཀྱང་གཞན་ལ་མ་ལུས་པར་སྟོན་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2006]
ཟང་ཟིང་མེད་པར་ཆོས་སྦྱིན་པ་ཞེས་བྱ་བ་ནི་ཁེ་དང་བཀུར་སྟི་ལ་མི༌[^1767]ཆགས་པར་ཆོས་སྟོན་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2007]
ཆོས་ལ་རིང་ཐང་མེད་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རིན་ཐང་མེད་པའི་རིན་པོ་ཆེ་གཅེས་ཤིང་ཕངས་པ་དེ་བཞིན་དུ་ཆོས་རིན་པོ་ཆེ་ལ་ཡང་གཅེས་ཤིང་ཕངས་པར་བྱེད་པའོ། །

[Block 2008]
ཕ་མ་ལ་བསྙེན་བཀུར་བྱེད་པ་ཞེས་བྱ་བ་ནི་ཕན་བཏགས༌[^1768]པའི་གནས་ཡིན་པས་བླ་མ་དང་བཙུན་པར་འཛིན་ཅིང་བཟའ་བ་དང་། བགོ་བ་ལ་སོགས་པས་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 2009]
བྱས་པ་གཟོ་བ༌[^1769]ཞེས་བྱ་བ་ནི༌[^1770]ཕན་བཏགས་པ་རྣམས་ལ་ཡང་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 2010]
བྱས་པ་ཚོར་བ་ནི་ཕན་བཏགས་པ་ཤེས་ཤིང་མི་བརྗེད་པའོ། །

[Block 2011]
བྱས་ནས་འགྱོད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གཞན་ལ་ཕན་བཏགས་པ་དང་དགེ་བ་བྱས་པ་རྣམས་བྱས་ནས་ཕྱིས་བྱས་པ་ཉེས་སོ་ཞེས་འགྱོད་པ་མེད་པའོ། །

[Block 2012]
བསོད་ནམས་ལ་སོགས་པས་མི་ངོམས་ཞེས་བྱ་བ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་མང་དུ་བསགས་པ་ལ་ཆོག་མི་ཤེས་པའོ། །

[Block 2013]
ལུས་བསྡམས་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱིས༌[^1771]སྲོག་གཅོད་པ་ལ་སོགས་པའི་ཉེས་པ༌[^1772]མི་འབྱུང་བར་བསྡམས་པས་ཡོན་ཏན་དང་མི་ལྡན་ཡང་ལྡན་པ་འདྲ་བར་ཚུལ་འཆོས་པ༌[^1773]མེད་པའོ། །

[Block 2014]
ངག་བསྡམས་པ་ཞེས་བྱ་བ་ནི་ངག་གི་སྒོ་ནས་བརྫུན་དང་ཚིག་ཀྱལ་པ་ལ་སོགས་པ་མི་འབྱུང་བར༌[^1774]བསྡམས་པས་བརྫུན་དང་གཡོ་སྒྱུའི༌[^1775]ཚིག་སྣ་ཚོགས་མི་སྨྲ་བའོ། །

[Block 2015]
ཡིད་བསྡམས་པ་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་སྒོ་ནས་བརྣབ་སེམས་དང་གནོད་སེམས་ལ་སོགས་པ་མི་འབྱུང་བར་བསྡམས་པས་བརྣབ་སེམས་དང་གནོད་སེམས་ཀྱི་བསམ་པ་དང་། གཡོ་སྒྱུའི་བསམ་པ་སྣ་ཚོགས་མེད་པའོ། །

[Block 2016]
དེ་བཞིན་གཤེགས་པའི་མཆོད་རྟེན་རབ་ཏུ་འཇོག་པས་ཚངས་པའི་བསོད་ནམས་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་མཆོད་རྟེན་བརྩིགས་པ་དང་བྱས་པས༌[^1776]མྱ་ངན་ལས༌[^1777]འདས་པར་འགྱུར་བའི་བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པའོ། །

[Block 2017]
རྣམ་པ་གཅིག་ཏུ་ན་དེ་བཞིན་གཤེགས་པའི་མཆོད་རྟེན་གཅིག་བྱས་ནས་ཚངས་པའི་བསོད་ནམས་བསྐྱེད་པའི་ཕྱིར་ཏེ། མདོ་ལས་ཀྱང་སྤྱན་རས་གཟིགས་དབང་ཕྱུག་རིགས་ཀྱི་བུ་འམ་རིགས་ཀྱི་བུ་མོ་དད་པ་ཅན་ལ་ལ་ཞིག་གིས༌[^1778]མི་གནས་པའི་ཕྱོགས་སུ་མཆོད་རྟེན་ནི་སྐྱུ་རུ་རའི་འབྲུ་ཙམ། སྲོག་ཤིང་ཁབ་ཙམ་གདུགས་ནི་བ་ཀུ་ལའི་ལོ་མ་ཙམ་ཞིག་བྱས་ལ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཚིགས་སུ་བཅད་པ་ནང་དུ་བཅུག་ན་དེ་ཚངས་པའི་བསོད་ནམས་བསྐྱེད་པར༌[^1779]འགྱུར་ཏེ། འདི་ནི་ཤི་འཕོས་ཤིང་འཆི་བའི་དུས་བྱས་ནས་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2018]
གཏན་པ་མེད་པའི་མཆོད་སྦྱིན་བྱེད་པས་མཚན་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཞེས་བྱ་བ༌[^1780]ནི་དངོས་པོ་ཐམས་ཅད་སེམས་ཅན་ཐམས་ཅད་ལ་དུས་ཐམས་ཅད་དུ་གཏོང་བ༌[^1781]ནི་གཏན་པ་མེད་པའི་མཆོད་སྦྱིན་ཏེ། དེས་སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ་རྩ་གཉིས་རྫོགས་པར་བྱེད་པའོ། །

[Block 2019]
དགེ་བའི་རྩ་བའི༌[^1782]ཚོགས་ཞེས་བྱ་བའི་གོང་དུ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐབས་སུ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དགེ་བའི་རྩ་བ་གཅིག་ཏུ་བསྡུས་ནས། དད་པས་རྗེས་སུ་འབྲང་བའི་གང་ཟག་གི་དགེ་བའི་རྩ་བའི་བརྒྱའི་ཆར་ཡང་མི་ཕོད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ལྟ་བུའི་དགེ་བའི་རྩ་བའི་ཚོགས་ཐམས་ཅད་བསགས་པས་དཔེ་བྱད་བཟང་པོ་ཀུན་རྫོགས་པར་བྱེད་པའོ། །

[Block 2020]
ང་རྒྱལ་མེད་པ༌[^1783]ཞེས་བྱ་བ་ནི་ཆེ་བའི་ང་རྒྱལ་དང་། ཆུང་བའི་ང་རྒྱལ་ལ་སོགས་པ་སྤངས་པས་འཕྲལ་དུ་ཡང་འགྱིང་བའི་སྤྱོད་ལམ་མི་མཛེས་པ་མེད་ཅེས་ཚེ་རབས་གཞན་དུ་ཡང་ལུས་མཛེས་པ་ཐོབ་པར་འགྱུར་བས་ན་ལུས་བརྒྱན༌[^1784]པའོ། །

[Block 2021]
ངག་གི༌[^1785]ཉེས་པ་ཐམས་ཅད་སྤངས་ཞེས་བྱ་བ་ནི་བརྫུན༌[^1786]ལ་སོགས་པའི་ཉེས་པ་སྤངས་པས། འཕྲལ་དུ་ཡང་ཚིག་སྐྱོན་ཅན་མི་མཛེས་པ་མེད་པ་དང་། ཚེ་རབས་གཞན་དུ་ཡང་དེ་བཞིན་གཤེགས་པའི་དབྱངས་ཡན་ལག་དུ་མ་དང་ལྡན་པ་ཐོབ་པར༌[^1787]འགྱུར་བས་ངག་བརྒྱན་པའོ། །

[Block 2022]
སེམས་ཅན་ཐམས་ཅད་ལ་ཁོང་ཁྲོ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་ཞེ༌[^1788]སྡང་གི་སེམས་མེད་པས་འཕྲལ་དུ་ཡང་གནོད་པའི་བསམ་པ་དྲི་མ་ཅན་མེད་ཅིང་ཚེ་རབས་གཞན་དུ་ཡང་ཞེ་སྡང་མེད་པའི་སེམས་འཐོབ་པར་འགྱུར་བས་སེམས་བརྒྱན་པའོ། །

[Block 2023]
མངོན་པར་ཤེས་པ་རྣམ་པར་འཕྲུལ་པ་ནི་མངོན་པར་ཤེས་པ་ལྔའི་སྒོ་ནས་རྣམ་པར་འཕྲུལ་པ་མང་པོ་བཤད་པ་དང་ལྡན་པས་སངས་རྒྱས་ཀྱི་ཞིང་བཻ་ཌཱུརྱའི་ཁ་དོག་ལ་སོགས་པ་དང་། དཔག་བསམ་གྱི་ཤིང་དང་རིན་པོ་ཆེའི་གཞལ་ཡས༌[^1789]ཁང་ལ་སོགས་པ་མཛེས་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པར་བྱེད་པས་ན་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྒྱན་དུ་འགྱུར་བའོ། །

[Block 2024]
འདོད་ཆགས་དང་བྲལ་བའི་ཆོས་ཉིད་ཅེས་བྱ་བ་ལ། འདོད་ཆགས་དང་བྲལ་བའི་ཆོས་ཉིད་ནི་མྱ་ངན་ལས་འདས་པ་འམ། དེ་བཞིན་ཉིད་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ལ་བྱ་སྟེ། དེ་ཁོང་དུ་ཆུད་པས་བདག་གིས༌[^1790]བཤད་པའི་ཆོས་ཐམས་ཅད་ཀྱང་བཟང་བའི༌[^1791]ཕྱིར། །ཆོས་ཀྱི་རྒྱན་དུ་འགྱུར་བའོ། །

[Block 2025]
ཡང་ན་འདོད་ཆགས་དང་བྲལ་བ་ཉིད་ཆོས་ཀྱི་དེ་བཞིན་ཉིད་དང་མཐུན་པ་ཡིན་པས་དེ་སྐད་ཅེས་བྱའོ། །

[Block 2026]
སྨྲས་པའི་ཚིག་རྣམས་ཕན་ཚུན་སྐྱེལ་བ་ནི་ཕྲ་མའོ། །

[Block 2027]
མ་སྨྲས་པའི་ཚིག་རྣམས་ཕན་ཚུན་སྐྱེལ་བར་བྱེད་པ་ནི་འབྱེད་པའི་ཚིག་གོ། །

[Block 2028]
དེ་ལྟ་བུ་མེད་པས་བདག་གི་འཁོར་ཀྱང་གཡོ་མེད་པ་སྒྱུ་མེད་པ་དྲང༌[^1792]པོ་ཡོན་ཏན་དང་ལྡན་པ་ཤ་སྟག་དང་ལྡན་པར་འགྱུར་བས་ན་འཁོར་གྱི་རྒྱན་དུ་འགྱུར་བའོ། །

[Block 2029]
བརྗོད་པ་ལ་སེར་སྣ་མེད་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་བསྟན་པ་ལས་སེར་སྣ་མེད་པས་ཆོས་ཀྱི་སྣོད་དང་། ཆོས་གཟུང་བའི༌[^1793]འོས་སུ་གྱུར་པའི་ཕྱིར། ཆོས་གཟུང་བར༌[^1794]འགྱུར་བའོ། །

[Block 2030]
ལེགས་སོ་ཞེས་བྱ་བ་བྱིན་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཡོད་པའི་ཆོས་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ཐོབ་པས། རབ་ཏུ་དགའ་ནས་ལེགས་སོ་ཞེས་སྨྲ་བ་ཉིད་བསོད་ནམས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2031]
ལེགས་པར་བཤད་པ་ལ་རྟོག་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པས་གསུངས་པ་ཐོག་མར་ཡང་དགེ་བར་དུ་ཡང་དགེ་ཐ་མར་ཡང་དགེ་བའི་ཆོས་བཤད་པ་རྟོག་པས་སྒྲིབ་པ་ལྔ་སྐྱེ་བའི་སྐབས་མེད་པར་བྱེད་པ་ནི་རྣམ་པར་སྤོང་པའོ། །

[Block 2032]
ངེས་པར་འབྱིན་པའི་ཆོས་ནི་འཕགས་པའི་ལམ་སྟེ། ཁམས་གསུམ་ནས་ངེས་པར་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 2033]
དེ་བསྟི་སྟང༌[^1795]དུ་བྱས་ཏེ་ཉན་པ་ཉིད་ཀྱི་བསོད་ནམས་ཀྱི༌[^1796]ཚོགས་ཡིན་ནོ། །

[Block 2034]
དཀའ་ཐུབ་བསྒོམ་པའི་ནགས་ཚལ་ནི་བརྟུལ་ཞུགས་ཀྱི་ནགས་ཚལ་ལོ། །

[Block 2035]
བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་གི་རྒྱན་ནི་བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་མངོན་པར་བྱང་ཆུབ་པར་འགྱུར་བའི་རྒྱུ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སམ། མངོན་པར་བྱང་ཆུབ་པ་ཉིད་བྱང་ཆུབ་ཀྱི་ཤིང་གི་རྒྱན༌[^1797]ནོ། །
--- END BLOCKS ---
