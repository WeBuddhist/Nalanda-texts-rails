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
དེ་ལ་ཕུལ་དུ་བྱུང་བ་བསྐྱེད་པ་ནི་མ་ཡིན་ཏེ། མི་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2032]
དེ་ནི་ངོ་བོ་སྔ་མ་དང་ཕྱི་མ་ཉམས་པ་དང་སྐྱེ་བའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2033]
ཅི་སྟེ།

[Block 2034 [VERSE]]
གལ་ཏེ་ཁྱེད་ཀྱི་དེ་ངོ་བོའི། །
སྒྲིབ་བྱེད་བྲལ་བ་གསལ་ཡིན་ནའང་། །
ཅི་ཕྱིར༌[^1477]མེད་པ་ལ་མེད་པའི། །
ཚོགས་ཀྱི་ནུས་པ་དེ་རུང་འགྱུར། །

[Block 2035]
སྒྲིབ་པར་བྱེད་པ་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་ནུས་པ་ཞེས་བྱ་བ་མེད་དོ། །

[Block 2036]
བྲལ་བ་ཡང་མེད་པ་ཡིན་ལ་མེད་པ་ཡང་འབྲས་བུ་མ་ཡིན་ནོ་ཞེས་བརྗོད་ཟིན་ཏོ། །

[Block 2037]
སྒྲ་རྟག་པའི་སྒྲིབ་པར་བྱེད་པ་ཡང་ཅུང་ཟད་ཀྱང་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2038]
དེ་བས་ན་སྒྲིབ་པར་བྱེད་པ་ལ་བྱེད་པ་དག་ཉེ་བར་དགོད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2039]
དེ་དག་ནི་ནུས་པ་མེད་པ༌[^1478]མ་ཡིན་ཏེ། དེ་དག་གི་བྱ་བ་མེད་པར་སྒྲ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2040]
དེ་བས་ན་དེ་དག་གིས་སྒྲའི་ངོ་བོ་ཡིན་པ་བྱེད་པར་རིགས་པ་ཡིན་ནོ། །

[Block 2041]
དེ་ལྟ་མ་ཡིན་ན།

[Block 2042 [VERSE]]
[^1479]སྒྲ་དང་ཁྱད་པར་མེད་པའི་ཕྱིར། །
གཞན་དག་ཀྱང་གསལ་ཐོབ་པར་འགྱུར། །
དེ་བཞིན་དུ་ནི་ཁས་ལེན་ན། །
རྒྱུ་རྣམས་ཀུན་ནི་དོན་མེད་ཉིད། །

[Block 2043]
གལ་ཏེ་རྒྱུ་ཐམས་ཅད་དང་ཆོས་མཐུན་པ་ཅན་གྱི་བྱེད་པ་གསལ་བྱེད་པ༌[^1480]དག་གིས་ཀྱང་། ད་ནི་འབྲས་བུ་ཅུང་ཞིག་ཀྱང་བྱེད་པར་མི་འགྱུར་ན་དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2044]
དངོས་པོ་ནི་བྱ་བ་མ་ཡིན་པ༌[^1481]ཁྱད་པར་ཅན་ཉིད༌[^1482]ཡིན་པའི་ཕྱིར་རོ། །

[Block 2045]
སྒྲིབ་པར་བྱེད་པ་མེད་པ་ནི་འབྲས་བུ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2046]
དེའི་ཤེས་པ་ཡང་དངོས་པོ་དང་འདྲ་བར་གྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །ཤེས་པ་ལ་འགའ་ཞིག་བྱེད་པ་པོར་འདོད་ན་དེ་ལྟ་བུར་གྱུར་པ་གཞན་དག་ལ་ཡང་དེ་ལྟར་འགྱུར་བར་ཐལ་བའི་སྒོ་ནས་ཐམས་ཅད་འབྲས་བུ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2047]
དེ་བས་ན་དོན་གྱི་ཚོགས་བྱེད་པ་པོར་མངོན་པར་འདོད་པ་འདི་གསལ་བ་ལ་མ་ཡིན་ཞིང་བྱ་བ་ལ་མ་ཡིན་པའི་ཕྱིར། དོན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2048]
དེ་ལྟར་ན༌[^1483]ཕན་གདགས་པར་བྱ་བ་དང་ཕན་འདོགས་པར་བྱེད་པ་ཅན་མ་ཡིན་པའི་འགྲོ་བ་འདི་བྱེད་པ༌[^1484]མེད་པར་འགྱུར་རོ། །

[Block 2049 [VERSE]]
སྒྲ་རྟག་པ་ཉིད་ཡིན་ན་ཡང་ངོ་། །
ངོ་ཤེས་པ་དང་ཡོད་སྦྱོར་སོགས། །
གང་ཡིན་སྒྲུབ་བྱེད་འདོད་ན་ནི། །
དཔེ་མེད་ཅན་ཡིན་དངོས་ཀུན་ནི། །
སྐད་ཅིག་གིས་ནི་འཇིག་ཕྱིར་རོ། །

[Block 2050]
དངོས་པོ་ཐམས་ཅད་ནི་འཇིག་པའི་རྒྱུ་མེད་པ་ཉིད་ཀྱི་ཕྱིར། སྐད་ཅིག་མས་འཇིག་པ་ཡིན་ནོ། །ཞེས་བཤད་ཅིང་འཆད་པར་ཡང་འགྱུར་རོ། །

[Block 2051]
གཞན་ལས་སྐྱེ་བ་ཅན་ཡང་ཡིན་ཏེ། ཡོད་པ་ཉིད་ནི་གློ་བུར་བ་ཉིད་དུ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2052]
དེ་བས་ན་ངོ་ཤེས་པ་དང་ཡོད་པར་སྦྱོར་བ་ལ་སོགས་པ་འདིའི་ནི༌[^1485]བརྟན་པའི་ངོ་བོ་གཅིག་པ་ཅན་འགའ་ཞིག་ལ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 2053]
སྒྲོན་མ་ལ་སོགས་པ་རང་བཞིན༌[^1486]གཞན་དང་གཞན་དུ་གྱུར་པ་ཅན་དག་ལ་མཐོང་བའི་ཕྱིར་འགལ་བ་ཉིད་ཡིན་ནོ། །

[Block 2054]
མ་ཡིན་ཏེ། སྐྱེ་བ་ཐ་དད་པ་མེད་པ་ཅན་ནི་ཆོས་མཐུན་པ་ཉིད་ཅན་དུ་རྣམ་པར་འཁྲུལ་པས་སྒྲོན་མ་ལ་སོགས་པ་དག་ལ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2055]
སྐྱེ་བ་ཐ་དད་ཅེས༌[^1487]བྱ་བ་གང་ལ་བརྟེན་ནས་བརྗོད་པ་ཡིན། ཐ་དད་པ་མེད་པ་དེ༌[^1488]ནི་ཐམས་ཅད་ལ་སྔ་ཕྱིར་དཔྱད་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2056]
གལ་ཏེ་དེ་བཞིན་དུ་ཐ་དད་པ་ཡང་ཡིན་ནོ་ཞེ་ན། དེ་ཉིད་ཀྱིས་ཐེ་ཚོམ་ཡིན་པའམ་བླ་སྟེ། ཐེ་ཚོམ་ལས་གྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2057]
གལ་ཏེ་ཐ་དད་པར་མཐོང་བ་མེད་པའི་ཕྱིར། གཅིག་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཤེས་པ་སྔ་ཕྱིས་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་གྲུབ་པའི་ཕྱིར། རང་བཞིན་ཐ་དད་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2058]
གལ་ཏེ་ཕྱིས་འབྱུང་བའི་ཤེས་པ་སྔར་རྒྱུ་ཐག་ཉེ་བ་ཅན་དག་ཡིན་ན་ཤེས་པ་སྔ་མ་དང་འདྲ་བར་སྐྱེ་བ་ཉིད་དུ་འགྱུར་ལ། མི་སྐྱེ་ན་ནི་རྒྱུ་དང་བྲལ་བ་ཉིད་སྟོན་པར་བྱེད་ནུས་པ་སྐྱེད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2059]
ནུས་པ་མེད་ན་ཡང་ཕྱིས་ཀྱང་ནུས་པ་དང་མི་ལྡན་པའི་ཕྱིར་དང་། ལྡན་པ༌[^1489]ཉིད་ཡིན་ན་ནི་མི་བརྟན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2060]
དེ་བས་ན་ཡོད་པའི་སྦྱོར་བ་འདི་ཡིན་པ་དེ་ལྟར་ན་ཡང་སྦྱོར་བ་པོའི་ནུས་པས་བསྐྱེད་པ་ཉིད་ཡིན་ཏེ། བདག་ཉིད་ཀྱི་ནུས་པ་ལ་དེ་ནི་ཉེ་བར་སྦྱོར་བ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2061]
སྦྱོར་བ་ཞེས་བྱ་བ་ཡང་རིགས་མཐུན་པའི་ཉེ་བར་ལེན་པ་ལྟོས་པ་ཅན་ནམ། ལྟོས་པ་མེད་པ་ཅན་འདོད་པ་སྒྲུབ་པར་བྱེད་པ་ལ་ནུས་པ་བསྐྱེད་པ་ཉིད་ཡིན་པར་བརྗོད་དེ། སྟེའུ་ལ་སོགས་པའི་སྦྱོར་བ་སྦྱོར་བ༌[^1490]བཞིན་དང་། ལས་ལ་སོགས་པའི་སྦྱོར་བ་བཞིན་ནོ། །

[Block 2062]
མངོན་སུམ་དུ་གྱུར་པ་ངོ་ཤེས་པ་ནི་མངོན་སུམ་ཉིད་ཡིན་ཏེ། མངོན་སུམ་དེ་ལས་བརྟན་པ་གྲུབ་པ་ཡིན་ནོ་སྙམ་དུ་སེམས་པ་གང་ཡིན་པ་དེ་ཡང་འོག་ནས་དགག་པར་བྱའོ། །

[Block 2063 [HEADING]]
### རྟགས་ངན་གཞན་སུན་དབྱུང་བ། ^7-2-0

[Block 2064]
རྟགས་ངན་གཞན་ཡང་སུན་དབྱུང་བྱ། །གང་ཆོས་འགའ་ཞིག་ཀྱང་རིགས་མཐུན་པའི་རྗེས་སུ་འགྲོ་བ་མེད་དེ། ཆོས་ཐམས་ཅད་དེའི་གནས་སྐབས་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2065]
བརྟེན་པར༌[^1491]དམ་བཅས་པ་ཐམས་ཅད་ཀྱང་ཇི་སྐད་དུ་བརྗོད་པའི་རིགས་པ་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 2066]
རྟག་པའི་གཏན་ཚིགས་གཞན་དག་ཀྱང་སྐྱོན་ཅན་དུ་བརྗོད་པར་བྱའོ། །

[Block 2067 [VERSE]]
བློ་ནི་སྐྱེས་བུའི༌[^1492]རྟེན་ཅན་མིན། །
ཁས་བླངས་མངོན་སུམ་གྲགས་པ་དང་། །
རྗེས་སུ་དཔག་པས་ཅིག་ཅར་གནོད། །

[Block 2068]
གལ་ཏེ་གསལ་བ་བློ་ཡིན་ན་ནི༌[^1493]དེའི་གོ་རིམས་ངག་ཡིན་ལ། དེ་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་ན་བློ་རྣམས་ནི་སྐྱེས་བུའི་ཡོན་ཏན་ཉིད་དུ་ཁས་བླངས་པས་འདིའི་གྲུབ་པའི་མཐའ་ལ་གནོད་པར་འགྱུར་རོ། །

[Block 2069]
བློ་འདིའི༌[^1494]ནི་སྐྱེས་བུར་འགྲང་བ༌[^1495]ཅན་དང་། སྐྱེས་བུའི་ཡོན་ཏན་ཡིད་ལ་བྱེད་པ་ལ་སོགས་པ་དག་ལས་འགྱུར་རོ། །ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ཡང་མངོན་སུམ་ཡིན་ནོ། །

[Block 2070]
ཡོད་པ་དང་མེད་པའི་ཁྱད་པར་ལས་འབྲས་བུ་ཞེས་བྱ་བ་གཞན་མེད་དེ། ཡོད་པ་དེ་ཡང་མངོན་སུམ་ཡིན་ཞིང་མི་དམིགས་པའི་མཚན་ཉིད་ཅན་གྱི་མེད་པ་ཡང་མངོན་སུམ་གྱི་སྟོབས་ཀྱིས་གྲུབ་པ་ཡིན་ནོ། །ཞེས་འཆད་པར༌[^1496]འགྱུར་རོ། །
--- END BLOCKS ---
