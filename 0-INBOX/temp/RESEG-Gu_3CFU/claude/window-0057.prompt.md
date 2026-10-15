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
གནས་མ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར་དང་རབ་ཏུ་རྒྱུ་བ་མི་གནས་པ་ཉིད་ཀྱིས་གྲོལ་བའི་དུད་འགྲོ་ལ་གནས་ཀྱི་ཐ་མ་འདི་ལ་སྤོ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1997]
དེ་ཡང་འདི་ལ་འདི་རྣམ་པར་གནས་ནས་ཏེ་གང་ཞིག་སྟོབས་ཀྱི་བདག་ཉིད་བརྟན་པའི་ཕྱིར་དེའི་ཚེ་མི་ནུས་པའམ། འཇིགས་པས་ཀྱང་འཇུག་པ་དེ་བས་ན་དེ་ལྟ་བུར་གྱུར་པའི་དུད་འགྲོའི་འདི་ལ་བཟུང་བར་རྟོགས་པར་བྱའོ། །

[Block 1998]
དེ་བས་ན་གཞན་དུ་ཡང་འདི་ལྟ་བུར་གྱུར་པའི་སྲོག་ཆགས་ལ་རྣམ་པར་གཞག་པས་འདི་ལ་དཔེ་ཉིད་དོ། །

[Block 1999]
འདིར་གཞུང་ནི། མིག་ལམ་དུ་སྣང་བར་མ་གྱུར་ན་བརྐུས་ཞེས་བྱ་བའོ། །ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2000]
གསང་སྔགས་དག་གིས་འདྲེན་པ་ནི་སྣང་བ་ནའོ་ཞེས་བྱ་བ་ནི་གསང་སྔགས་རྣམས་ཀྱིས་གཏེར་ལ་སོགས་པ་འདྲེན་པ་ན་གཏེར་ལ་སོགས་པ་སྣང་བ་ན་བརྐུས་པ་ཡིན་ནོ། །

[Block 2001]
ཡུལ་དེ་ན་གནས་པ་ན་ཡང་ཁ་བྱེ་བ་ཉིད་བསྒྲུབས་པས་སྣང་བར་གྱུར་ན་འདིར་བསྒྲུབ་པའི༌[^1387]བློར་འགྲོ་བ་མ༌[^1388]ཡིན་ཏེ། ཅི་སྟེ་ཤིན་ཏུ་ཐག་རིང་པོ་ནས་དྲངས་ཏེ་རྐང་པའི་དྲུང་དུ་བཀུག་ཅིང་འབྲེལ་པ་ལ་ཡང་རྐང་པའི་དྲུང་དུ་སྣང་བར་མ་གྱུར་པ་ལ་གྲུབ་པའི་བློ་སྐྱེ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་སྣང་བ་ལ་རྐུ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 2002]
མང་པོ་ཞིག་ཡོད་པ་ལ་གཅིག་ཁོ་ན་ཞིག་གིས་འཇུག་པ་ལ༌[^1389]ཡང་སྣང་བར་སྒྲུབ་པ་ལ་ཐམས་ཅད་བསྒྲུབ་པ༌[^1390]ཉིད་ཅེས་བྱ་བ་རྐུ་བའི་ཆོ་ག་དང་བཅས་པར་རྟོགས་པར་བྱའོ། །

[Block 2003]
གཏེར་ལ་ནི་འདི་བཤད་པ་ཡིན་ཏེ་ཐམས་ཅད་དུ་འདི་སྦྱར་བ་ཞེས་བྱ་བ་དཔེ༌[^1391]ཉིད་དུ་རྣམ་པར་ཤེས་པ་ཁྱད་པར་དུ་སྔར་ཉེ་བར་བརྟགས་པ་བསྟན་པའི་ཕྱིར་ཕྱི་བཞིན་འབྲང་བ་དང་ནང་བྱན་བྱེད་པ་གཉིས་ནུར་བ་དང་འབྱངས་པ་དང་འབྱམ་པ་དང་འཇུག་པ་དང་འཛེག་པ༌[^1392]རྣམས་ཀྱིས་སྔ་མ་ལྟར་ཡིན་གྱི་དེ་གཉིས་ཀྱིས་བླངས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་དེ་ལ་སྔར་མི་སྣང་བ་ཉིད་མ་ཡིན་ནོ། །སུ་ལ་མི་སྣང་བ་ཉིད་ཅེ་ན། དེའི་ཕྱིར་ཕྱི་བཞིན་འབྲང་བ་དང་ནང་བྱན་བྱེད་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱབ་ནས་འགྲོ་ཞིང་ཆོས་གོས་ཉེ་བར་ཁྱེར་བར་བྱེད་པ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2004]
གཟུང་བ་མ་ཡིན་པ་དེ་དག་གིས་བཟུང་བ་ལ་རྐུ་བའི་དངོས་པོ་ཉིད་དུ་ཁས་བླངས་པའི་རྫས་ལ་མི་སྣང་བ་ཉིད་ནི་བརྐུས་པ་མ་ཡིན་ནོ། །

[Block 2005]
གང་གི་ཕྱིར་དེ་བརྐུ༌[^1393]བཞིན་པ་ཉིད་ཀྱིས་ཀྱང་ཅུང་ཟད་མི་སྣང་བར་འགྱུར་ཏེ། དེ་ལ་གང་ཞིག་མ་ཉམས་པ་ཙམ་ལ་ཡང་བརྐུས་པར་ཐལ་བའོ། །

[Block 2006]
ཕྱི་བཞིན་འགྲོ་བ་དང་ནང་བྱན་བྱེད་ཅིང་སྣང་བར་གྱུར་པ་དང་མི་སྣང་བར་གྱུར་པའི་རྫས༌[^1394]ལ་ཡང་མ་བཅད་པའི་བློ་མ་ཡིན་པ་ལ་གནས་ནས་སྤོ་བ་དག་ལ་མི་སྣང་བར་གྱུར་པ་ཉིད་ལ་མ་ཆད་པའི་བློ་ཡོད་པར་འགྱུར་རོ། །

[Block 2007]
རྣམ་པ་གང་གིས་མི་སྣང་བར་གྱུར་པ་ཉིད་ཅེ་ན། དེའི་ཕྱིར་ནུར་བ་དང་འབྱངས་པ་དང་འབྱམ་པ་དང་འཇུག་པ་དང་འཛེག་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ནུར་བ་ནི་གང་ཞིག་མ་ཉམས་པ་ཉིད་ཀྱིས༌[^1395]འགྲོ་བའོ། །

[Block 2008]
འབྱངས་པ་ནི་ཕྱིར་ནུར་ཏེ་སོང་བའོ། །

[Block 2009]
མ་བརྗོད་པའི་དོན་རྣམས་ལ་འདི་བསྡུས་པའོ། །

[Block 2010]
དེ་རྣམས་ཀྱང་འདའ་བར་བྱས་ནས་འགྲོ་བ་དང་མི་སྣང་བ་དང་གསང་སྔགས་དང་སྨན་དག་གིས་གཟུགས་གཞན་དུ་བསྒྱུར་བ་དང་། འདི་དག་གིས་ནི་ལུས་གཞན་རྣམ་པར་བཀབ་པས་ནུས་པ་ངེས་པར་གནས་པའོ། །

[Block 2011]
འཇུག་པ་ཞེས་བྱ་བ་ནི་གནས་ཁང་དུའོ། །

[Block 2012]
འཛེག་པ་ཞེས་བྱ་བ་ནི་ཡང་ཐོག་གཞན་དུ་འཛེག་པའོ། །

[Block 2013]
འབྱམ་པ་ཞེས་བྱ་བ་ནི་གནས་གཏང་བ༌[^1396]སྟེ། དཔེར་ན་གཤོང་ནས་ཐང་ལ་འབྱུང་བ་དང་ཐང་ལས་གཤོང་དུ་འབབ་པ་དང་། མངོན་པར་སྐབས་ཡོད་པ་ནས་ཐིབས་པོར་འཇུག་པ་དང་། ཐིབས་པོ་ནས་མངོན་པར་སྐབས་ཡོད་པར་འགྲོ་བ་དང་། གནས་ཁང་ནས་ཁྱམས་སུ་དང་ཁྱམས་ནས་གནས་ཁང་དུ་དང་། ཡང་ཐོག་ནས་ཡང་ཐོག་གཞན་དུ་འཛེག་པ་དང་ཡང་ཐོག་ནས་ཡང་ཐོག་གཞན་དུ་འབབ་པ་དང་། ཁྱམས་ནས་སྒོ་ཁང་དུ་འཇུག་པ་དང་། སྒོ་ཁང་ནས་དང་ར་ཁྱད་ཁྱུད་དུ་འགྲོ་བ་ལ་སོགས་པ་སྟེ། ནུར་བ་ལ་སོགས་པ་འདི་རྣམས་ཀྱིས་ཕྱི་བཞིན་འབྲང་བ་དང་ནང་བྱན་བྱེད་པ་དག་མི་སྣང་བར་གྱུར་པ་ཉིད་གང་ཡིན་པ་དེ་བརྐུས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2014]
ཇི་ལྟར་ཡང་འགྲོ་བར་བྱ་བ་ཉིད་ལ་ཡང༌[^1397]གནས་ཁང་དུ་ཞུགས་པ་དང་། ཡང་ཐོག་གཞན་དུ་འཛེག་པ་དང་ཁྱམས་ནས་གནས་ཁང་ལ་སོགས་པ་བྱས་པ་ཉིད་དམ་མ་མཐོང་བའི་མཐའ་མ་ཉིད་ནི་ཆོམ་རྐུན་པ་ལ་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 2015]
འདིར་གཞུང་ནི། ཇི་ལྟར་ཡང་མཁན་པོ་དང་སློབ་དཔོན་དག་ལམ་དུ་ཞུགས་པར་གྱུར་པ་དེ་དག་གིས་ལྷན་ཅིག་གནས་པ་དང་ཉེ་གནས་དག་གི༌[^1398]ལག་ཏུ་ཆོས་གོས་དག་གཏད་པ་ན་དེ་ལ་དེ་དག་རྐུ་སེམས་ཉེ་བར་གནས་པར་གྱུར་ཅིང་དེ་དག་གོམ་པ་བསྲི་བས་འགྲོ་ཞིང་དལ་བུས་འགྲོ་ན་གོམ་པ་རེ་རེ་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2016]
ཇི་སྲིད་དུ་མིག་སྔར་སྣང་བར་གྱུར་པ་དེ་སྲིད་དུ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2017]
མིག་སྔར་སྣང་བར་མ་གྱུར་ན་བརྐུས་པར་བརྗོད་པར་བྱ་སྟེ་རིན་ཐང་བརྩི་བར་བྱའོ། །

[Block 2018]
དེ་རྣམས་ནི་གཤོང་ནས་ཐང་ལ་འབྱུང་བར་བྱེད་པ་དང་། ཐང་ལས་གཤོང་དུ་འཇུག་པར་བྱེད་པ་དང་། མངོན་པར་སྐབས་ཡོད་པ་ནས་ཐིབས་པོར་འཇུག་པ་དང་། ཐིབས་པོ་ནས་མངོན་པར་སྐབས་ཡོད་པར་འགྲོ་བ་དང་ཇི་སྲིད་དུ་མིག་སྔར་སྣང་བར་གྱུར་པ༌[^1399]དེ་སྲིད་དུ་སྔ་མ་བཞིན་དུ་ཇི་ལྟར་ཡང་དེ་རྣམས་དང་ལྷན་ཅིག་གནས་པ་དང་། ཉེ་གནས་དག་ལ་མཁན་པོ་དང་སློབ་དཔོན་རྣམས་ཀྱི་ཆོས་གོས་དག་ཁུར་བར་བྱེད་པ་དེར་དེ་ལ་རྐུ་སེམས་ཉེ་བར་གནས་པར་གྱུར་ཅིང་། དེ་རྣམས་གནས་ཁང་ནས་ཁྱམས་སུ་འགྲོ་ཞིང་། ཁྱམས་ནས་གནས་ཁང་དུ་ཞུགས་པར་བྱེད་པ་དང་། འོག་ཁང་ནས་ཡང་ཐོག་དུ་འཛེག་པར་བྱེད་པ་དང་། ཡང་ཐོག་ནས་འོག་དུ་འཇུག་པར་བྱེད་པ་དང་། ཁྱམས་ནས་སྒོ་ཁང་དུ་འཇུག་པ་དང་། སྒོ་ཁང་ནས་དང་ར་ཁྱད་ཁྱུད་དུ་འབྱུང་བ་དང་། ཇི་སྲིད་དུ་མིག་སྔར་སྣང་བར་གྱུར་པ་དེ་སྲིད་དུ་སྔ་མ་བཞིན་དུ་འདིར་གང་ཞིག་ནུར་བ་དང་། འབྱངས་པ་དང་འབྱམ་པ་དང་། འཇུག་པ་དང་། གནས་གཞན་དུ་འཛེག་པ་ལས་གཞན་འབྱམ་པ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 2019]
རྐུ་བར་བྱེད་ཅེས་བྱ་བ་འདིར་རྐུ་བ་ནི་ཉེ་བར་རྐུ་བའོ། །

[Block 2020]
གྲུ་ནི་སྐམས་དང་ཡུར་པོ་ཆེ་དང་ཆུ་འདལ་བ་དག་གིས་ཞེས་བྱ་བ་ནི་གྲུ་ནི་སྐམས༌[^1400]ལ་སོགས་པ་རྣམས་ཀྱིས་རྐུ་བ་ལ་མི་སྣང་བ་ཉིད་ནི་རྐུ་བ་སྟེ། རྣམ་པར་མི་གནས་པའི་རྒྱུ་བ་རིགས་སུ་འབྱུང་བ་ཉིད་ཀྱི༌[^1401]ཕྱིར་གྲུ་ལ་འདི་གནས་གཞན་དུ་འཕོ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2021]
འདིར་གྲུ་ནི་དཔེ་ཙམ་སྟེ། སེམས་མེད་པ་ཆུ་ལ་རྒྱུ་བའི་གཟིངས་ལ་ཡང་ཆོ་ག་འདི་ནི་ཤིང་དང་སྣོད་ལ་སོགས་པའི་རང་བཞིན་ཐམས་ཅད་ལའོ། །

[Block 2022]
རྒྱུན་ཕྱོགས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་རྐུ་བ༌[^1402]ཉིད་ནི་འདིར་རྐུ་བའོ། །

[Block 2023]
ཐད་ཀར་ཡང་ཕ༌[^1403]རོལ་གྱི་འགྲམ་དུ་མི་སྣང་བར་གྱུར་ནའོ་ཞེས་བྱ་བ་ནི་ཐད་ཀའི་ཕ་རོལ་གྱི་འགྲམ་དེ་མི་སྣང་བར་གྱུར་ན། དེའི་ཚེ་མི་སྣང་བ་འདི་ཉིད་རྐུ་བ་ཡིན་ནོ། །

[Block 2024]
དེ་ལས་གཞན་པ་ཉིད་ལ་ནི་དེར་ཕྱིན་ནའོ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་གྱི་འགྲམ་དེ་མི་སྣང་བ་ཉིད་ལ་ཕ་རོལ་གྱི་འགྲམ་ཐོབ་པ་ནི་བརྐུས་པའོ། །

[Block 2025]
རྒྱུན༌[^1404]ལས་བཟློག་པ་ལ་ནི་གྲུ་ཚུགས་ལས་འདས་ནའོ་ཞེས་བྱ་བ་ལ། རྒྱུན་ལས་བཟློག་པ་བརྐུས་པ་ལ་ནི་གྲུ་ཚུགས་ལས་འདས་པ་ན་བརྐུས་པའོ། །

[Block 2026]
རྒྱུན་ལས་བཟློག་པའི་ཕྱིར་འདི་ལ་རྒྱུ་བ་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། གྲུའི་འགྲོ་བའི་རྐྱེན་ལས་བཟློག་པ་ལ་མཐུན་པར་མི་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 2027]
ཐང་ལ་རྒྱུ་བའི་འགྲམ་གྱི་རྣམ་པར་ཡང་དག་པར་རྒྱུ་བ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2028]
དེ་བས་ན་གནས་གཞན་དུ་འཕོ་བའི་བདག་ཉིད་ཅན་ལ་འདིར་རྐུ་བའི་རྣམ་པར་གཞག་པའོ། །

[Block 2029]
གྲུ་ཚུགས་ལས་གནས་པ་ཉིད་ལའོ། །

[Block 2030]
འདི་ལ་ཡོངས་སུ་འགྲོ་བར་བྱེད་པའི་སྤྱོད་ཡུལ་དུ་མ་གྱུར་པ་ཉིད་ཀྱིས་མ་ལུས་པའི་གནས་དེ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 2031]
གྲུ་ཚུགས་པ་མེད་པ༌[^1405]ལ་འདིའི་གནས་བཟུང་བ་ཙམ་ཡིན་ཏེ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 2032]
གཞན་གྱི་ལས་ཀྱི་མཐའ་དག་ལ་ཆུ་གཏོང༌[^1406]བའམ་འགོག་པ་ལ་ནི་རང་གི་ལས་ཀྱི་མཐའ་གྲུབ་པའི་སྐྱེད་མ་གཏོགས་པ་དེའི་ཆེད་དུ་དེར་འདུན་པས་གཞན་དུ་གྱུར་ནའོ་ཞེས་བྱ་བ་ནི་གཏོང་བའམ་འགོག་པ་ལའོ། །

[Block 2033]
དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་རང་གི་ལས་ཀྱི་མཐའ་གྲུབ་པའི་དོན་དུའོ། །

[Block 2034]
སྐྱེད་མ་གཏོགས་པ་ཞེས་བྱ་བ་ནི་གྲུབ་པའི་ཁྱད་པར་རོ། །

[Block 2035]
སྐྱེད་མ་གཏོགས་པའི་གྲུབ་པ་ནི་རྐུ་བ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
