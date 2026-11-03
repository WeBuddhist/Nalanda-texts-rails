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

[Block 2036]
ཅིའི་ཕྱིར་སྐྱེད་མ་གཏོགས་པ་ཞེས་བྱ་བའི་ཁྱད་པར་བསྟན་པའི་དོན་དུ་ཅིག་ཤོས་ཞེས་བྱ་བ་སྨོས་ཏེ། གྲུབ་པ་ལས་ཅིག་ཤོས་གང་ཡིན་པའོ། །

[Block 2037]
ཕམ་པ་འདི་ཅི་ཡིན་པ་དང་ཕམ་པ་འདི་གང་ཡིན་པ༌[^1407]སྟེ་ཞེས་བྱ་བའི་རྟེན་འདི་ལ་བརྟེན་པའི་དོན་དུ་གཞན་གྱི་ལས་ཀྱི་མཐའ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2038]
དགོས་པ་ཅི་ལྟ་བུས་གཞན་གྱི་ལས་ཀྱི་མཐའ་ལ་ཕམ་པ་ཡོད་པ་ལ་རང་གི་ལས་ཀྱི་མཐའ་གྲུབ་པ་རྐུ་བ་ཞེས་བྱ་བ་དེར་འདུན་པས་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་གྱི་ཕུང་བར་བྱའོ། །

[Block 2039]
བདག་གི་གྲུབ་པར་བྱའོ་སྙམ་པས་བསམ་པ་འདིས་སོ། །

[Block 2040]
བསམ་པ་ཙམ་ཉིད་ཀྱིས་གཞན་གྱི་ཕུང་བར་ཡོད་པར་གྱུར་པ་དང་རང་ལ་གྲུབ་པ་རྐུ་བ་ཆུ་བཏང་བ་འམ་འགགས་པ་ལས་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་རང་གི་ལས་རྣམས་འཇུག་པ་དགག་པ་ལ་ཆུ་ཡོད་པར་འགྱུར་བ་དང་། གཞན་གྱི་ལས་ཀྱི་མཐའ་རྣམས་ལ༌[^1408]ཆུ་གཏོང་བ་ལ་ཆུ་ཡོད་པར་འགྱུར་རོ། །

[Block 2041]
འོན་ཏེ་ཆུ་དཀོན་པར་གྱུར་ན་རང་གི་ལས་ཀྱི་མཐའ་རྣམས་ལ་ཆུ་བཏང་བ་དང་། གཞན་གྱི་ལས་ཀྱི་མཐའ་རྣམས་ལས་འགོག་པར་བྱས་པ་ལ་གཞན་གྱིས་ཕུང་བར་བྱས་པའི་བསམ་པས་བྱེད་ལ། གང༌[^1409]གི་ལས་ཀྱི་མཐའ་གྲུབ་ཅིང་བརྐུས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2042]
རྒྱུན་ཕྱོགས་སུ་འགྲོ་བ་ལ་ཡང་ཆུ་བཏང་བ་དང་བཀག་པ་འདི་དག་ལས་ཀྱི་མཐར་འགྲོ་བ་ལ་གཏོགས་པར་བྱའོ། །

[Block 2043]
[^1410]འདིར་འབྲུ་ཕུན་སུམ་ཚོགས་པ་ལ་རྐུ་བར་གྱུར་པ་ཉིད་དུ་གནས་པའོ། །

[Block 2044]
ཆུ་གཏོང་བར་བྱེད་པའམ་རང་གི་ལས་ཀྱི་མཐའ་འགོག་པ་ལ་རྐུ་བར༌[^1411]མི་བྱེད་པར་ཐལ་བ་མ་ཡིན་ནོ།[^1412] །རང་འདོད་པ་དང་གཞན་ལ་ཉམས་པ་མེད་པར་གྱུར་པ་ལ་ཅུང་ཟད་བརྐུས་པར་འགྱུར་བ་མ་ཡིན་ཞེས་བྱ་བ་རྣམ་པར་ངེས་ནས་དེ་ལ་གྲུབ་པ་དང་གཞན་ལ་ཕུང་བ་ཞེས་བྱ་བ་ཡང་གཞན་ཕུང་བ་ལ་ཡང་དག་པར་བརྟན་པའི༌[^1413]གཞུང་ལ་བརྟེན་ནས་ཅིག་ཤོས་ཞེས་བྱ་བ་བྱས་ཏེ་ཆད་པའི་སེམས་མེད་པར་རྐུ་བ༌[^1414]བསྐྱེད་པ་མ་ཡིན་ནོ། །

[Block 2045]
འདི་ཡང་འདི་ལ་ཆད་པ་གང་ཞིག་ཉམས་པ་ཞེས་བྱ་བ་རྣམ་པར་ངེས་ནས་བདག་ལ་གྲུབ་པར་གྱུར་ཅིག །གཞན་ལ་ནི་ཕུང་བར་གྱུར་ཅིག་ཅེས་བྱ་བ་གཞན་པར་འདོད་པའི་ཚིག་ལ་བརྟེན་ནས་དེར་འདུན་པས་ཞེས་བྱ་བ་བྱས་སོ། །

[Block 2046]
ཇི་ཙམ་དུ་གཞན་ལས་གཅོད་པ་དེ་ཙམ་ལས་རྐུ་བ་ཉིད་ཅེས་བྱ་བ་ལྟ་བར༌[^1415]བྱས་ནས་སྐྱེད་མ་གཏོགས་ཞེས་བྱ་བ་བྱས་སོ། །

[Block 2047]
གང་ཞིག་གཞན་ཕུང་བ་མི་སྐྱེད་པའི༌[^1416]ཞིང་གི་ཡོན་ཏན་ལ་སོགས་པས་བསྒྲུབ་པར་གྱུར་པ་དེ་ལ་རྐུ་བ་ཉིད་མ་ཡིན་པ་གཏོགས་པར་བྱའོ། །

[Block 2048]
རྐུན་པོ་རྣམས་ལ་དེའི་ཆེད་དུ་ལམ་རྒྱུས་གོ་བར་བྱེད་པ་ལ་ནི་ཤས་ཐོབ་པར་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ། རྐུ་བའི་ལམ་ལ་བརྟེན་པའི་ལོ་རྒྱུས་ནི་ལམ་རྒྱུས་ཏེ་ལམ་ག་གེ་མོ་ནས་དེར་འགྲོ་བར་བྱའོ། །

[Block 2049]
དེ་ལྟར་འཇུག་པར་བྱ་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2050]
དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་ཤས་ཐོབ་པར་བྱ་བའི་ཆེད་དུའོ། །

[Block 2051]
རྐུན་པོ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་པ་རྣམས་ལ་གལ་ཏེ་རྐུ་བའི༌[^1417]དོན་དུ་ལམ་རྒྱུས་གོ་བར་བྱེད་པའི་ལས་བྱས་པ་ལ་དེ་རྣམས་ཀྱི་དྲུང་ནས་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི་ཤས་བརྐུས་པ་ཡིན་ནོ། །

[Block 2052]
འདི་ནི་རྐུན་པོ་ལས་ཤས་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཁས་ལེན་པ་ཡིན་ཏེ། །རྐུན་པོ་རྣམས་ལས་བརྐུས་པ་སོ་སོར་བཟུང་བ་ཉིད་དོ། །

[Block 2053]
དེའི་ཕྱིར་རྐུན་པོའི་ཚོགས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཀྱི༌[^1418]ཕྱིར་བརྐུས་པ་ཉིད་དོ། །

[Block 2054]
བདག་གི་དོན་དུ་ཡང་དེ་ལས་ཆ་ཤས་བརྐུ་བར་བྱ་བ་འདི་ལ་དེའི་དོན་དུ་རྐུ་བའོ། །

[Block 2055]
ཐོབ་པ་འདི་ལ་བྲན་གྱིས་ལས་དང་འདྲ་བ་ཉིད་དེ་འདིར་ནི་མཉམ་པོར་བྱ་བ་བྱེད་པ་ཉིད་ཀྱིས་དེ་ལས༌[^1419]གཞན་པའི་ཆོམ་རྐུན་བཞིན་དུ་ཆ་ཤས་དང་ལྡན་པ་ཉིད་ནི་མ་ཡིན་ནོ།[^1420] །ངེས་པར་སྦྱོར་བ་པོ་ཉིད་དང་གཏོང་བ་པོ་ཉིད་ཀྱི་བློ་ཡང་དག་པར་གནས་པ་ཞེས་བྱ་བ་ཐོབ་པ་ལ་རྐུ་བ་ཉིད་ཤེས་པ་ཡིན་ཏེ། འགྲོ་བའི་དུས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2056]
ས་གཞི་དང་ཁང་ཁྱིམ་དག༌[^1421]ཡོངས་སུ་བསྐོར་བས་ནི་མཚམས་འབྱོར་ནའོ་ཞེས་བྱ་བ་ནི་རིབ་མ་དང་རྩིག་པ་ལ་སོགས་པས་ཡོངས་སུ་བསྐོར་བས་ས་གཞི་ལ་སོགས་པ་རྐུ་བ་རིབ་མ་ལ་སོགས་པ་དེ་ལས༌[^1422]མཚམས་འབྱོར་ན་ནི་རྐུ་བའོ། །

[Block 2057]
འདིར་ངེས་པར་དེའི་ཚེ་ན་ཉེ་བར་བཟུང་བ་ཉིད་ཀྱི་བློ་ལ་ཡང་དག་པར་བསྟན་པ་ལ་དེ་རྣམ་པར་ཤེས་པའོ། །

[Block 2058]
ཤགས་ཀྱིས༌[^1423]གལ་ཏེ་བླའི་གྲར་རྒྱལ་ནའོ། །

[Block 2059]
གལ་ཏེ་འོག་ཟུར་ན་ཕ་རོལ་པོའི་སྦྱོར་བ་ཉིད་བཏང་ནའོ། །

[Block 2060]
དེ་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བླའི་གྲར་ཤགས་བཀྱེ་བ་ནི་ཤགས༌[^1424]ཀྱིས་རྐུ་བ་ལ་རྒྱལ་བ་ནི་བརྐུས་པ་ཡིན་ནོ། །

[Block 2061]
གལ་ཏེ་འོག་ཟུར་ན་ཕ་རོལ་པོའི་སྦྱོར་བ་པ༌[^1425]ཉིད་བཏང་བ་ནི་བརྐུས་པ་ཡིན་ནོ། །

[Block 2062]
རྒྱལ་བ་འདི་ལ་སྦྱོར་བ་ཉིད་ཡོངས་སུ་རྫོགས་པར་གྱུར་པའི་དངོས་པོ་ཅན་ལ་ཉེས་པ་སྦོམ་པོའོ། །

[Block 2063]
གཞན་དུ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2064]
ངེས་པར་འདིར་སོ་སོར་གསལ་བ་ཉིད་ལ་གཞན་ལ་གྲུབ་པའི་བློ་ཡང་དག་པར་གནས་པ་ཡིན་ནོ། །

[Block 2065]
བླའི་གྲལ་དུ་གཞན་ལ་གསལ་བ་ཉིད་ཡོད་ཀྱང་མངའ་བདག་ཉིད་ཀྱི་ཕྱིར་རྒྱལ་པོ་རྟེན་གྱི་མ་ངེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2066]
གྲུབ་པའི་བློ་ཡང་དག་པར་གནས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 2067]
ཤོ་གམ་གྱི་ས་ལས་འདས་ན་ཞེས་བྱ་བ་སྨོས་པ་དེར་ཤོ་གམ་གྱི་བརྐུས་པ་ཉིད་དུ་བརྗོད་དེ་ཤོ་གམ་གྱི་བྱ་བ་ཉིད་ལ་བརྟེན་པ་སྐྱེ་བ་དང་བཅས་པ་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པའི་ཚིག་རྣམས་གང་ཡིན་པ་དེ་རྣམས་ནི་རྣམ་པར་འབྱེད་པ་ལས་བསྡུ་བར་བྱ་སྟེ། རྐུ་སེམས་མེད་པ་ལ་ཤོ་གམ་དུ་གཏོགས་པའི་ཉེས་པ་འབྱུང་བར་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་སྤང་བ་མ་ཐོབ་པའི་དགེ་སློང་རྣམས་ཀྱིས་ཚོང་པ་རྣམས་ལ་ཤོ་གམ་དུ་གཏོགས་པ་ལས་འདའ་བར༌[^1426]བྱ་བའི་ཕྱིར་སྦྱིན་པ་གང་ཡིན་པ་དེར་ཚོང་པ་རྣམས་འདིར་རྐུ་བར་བྱེད་པ་ཉིད་མ་ཡིན་ཏེ་ཤོ་གམ་པའི་སེམས་བཟུང་བར་བྱས་པའི་ཚོང་པ་དེ་རྣམས་ལས་འདའ་བའི༌[^1427]ཕྱིར་རོ། །

[Block 2068]
གང་གི་ཕྱིར་དགེ་སློང་རྣམས་ལ་བརྐུས་པ་ཉིད་དུ་མི་འགྱུར་བ་དེའི་ཕྱིར་ལྟུང་བ་མེད་པའི་ཚིག་རིགས་པ་ཡིན་ནོ། །

[Block 2069]
གང་ཞིག་ཡོངས་སུ་སྤང་བ་མ་ཐོབ་པའི་དགེ་སློང་གིས་དགེ་སློང་གཞན་ལ་འདའ་བའི་ཕྱིར་སྣོད་སྦྱིན་པ་དེར་ཡང་དགེ་སློང་འདི་ཡིན་ཏེ། འདི་ནི་དེ་ལྟར་འདའ་བར་གྱུར་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་འདི་ལ་རྐུ་བ་ཉིད་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ལྟུང་བ་མ་ཡིན་པའི་རིགས་པར་གྱུར་པ་ཉིད་དེ་ངེས་པར་འདིར་འདིའི་བློ་ཞེས་བྱ་བ་རྐུ་བ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 2070]
གང་ཞིག་སྤོང་བ་ཐོབ་པ་རྣམས་ཚོང་པ་རྣམས་དང་འབྲེལ་པ་ལས་འདའ་བར་བྱེད་པ་དེར་འདི་རྣམས་ལ་གཞན་གྱི་དོན་དུ་བརྐུས་པ་ཉིད་ཡོད་པ་དེར་རང་གི་སྤོང་བ་ཐོབ་པ་འདི་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
