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
གཞན་གྱིས་ནི་བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་དང་། མིག་གིས་གཟུང་བྱ་མ་ཡིན་པ་ཉིད་ལ་སོགས་པས་སྒྲ་རྟག་པ་ཉིད་དོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 2032]
བསྲེག་པར་བྱ་བ་ཉིད་ལ་སོགས་པས་བུམ་པ༌[^1605]མི་རྟག་པ་ཉིད་དུ་ནི༌[^1606]མ་ཡིན་ནོ། །

[Block 2033]
དེ་ལ་འདི་སྐད་བརྗོད་པར་བྱ་སྟེ། བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་རྟག་པ་ཁོ་ནར་མཐོང་བ་ནི་མེད་ཀྱི།[^1607] འོན་ཀྱང་རྟག་པ་ལའོ་ཞེས་སོ། །

[Block 2034]
དེ་ལྟར་ནི་གཞན་གྱི་ཕྱོགས་ལ་མ་ངེས་པ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2035]
འདི་སྔ་མ་ཉིད་ལ་ཁྱབ་པར་བྱེད་པ་ཡིན་ལ་ཁྱབ་བྱེད་མ་ཡིན༌[^1608]པ་གཏན་ཚིགས་མ་ཡིན་ནོ། །

[Block 2036]
གཞན་གྱི་སྒྲ་ལ་རྩོལ་བ་ལས་བྱུང་པའི་ཕྱིར་མཉན་བྱ་མ་ཡིན་པར་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་མཉན་བྱ་མ༌[^1609]ཡིན་པའི་ཕྱིར་སྒྲ་ཉིད་རྟག་པར་འགྱུར་བའོ་ཞེས་ཡིན་ནོ། །

[Block 2037]
ལན་ཕྱོགས་སྔ་མ་དང་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 2038]
[^1610]གལ་ཏེ་ཆོས་མཐུན་པས་བརྗོད་ན་ནི་བདེན་ཏེ། ཆོས་མི་མཐུན་པས་ནི་བསྒྲུབ་བྱ་མེད་པས་གཏན་ཚིགས་མེད་པར་སྟོན་པ་ཡིན་གྱི། བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་བསྒྲུབ་བྱ་མེད་པའོ༌[^1611]ཞེས་ནི་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ༌[^1612]ཡིན་དུ་ཆུག་ན་དཔེ་གཉིས་ཀ་རྗེས་འགྲོ་ཕྱིན་ཅི་ལོག་གིས་ཡིན་ནོ། །

[Block 2039]
དེ་ལྟར་རྩོད་པ་གྲུབ་པ་ན་ནི་མེད་དེ། ཇི་སྐད༌[^1613]དུ་མཉན་བྱ་མེད༌[^1614]ཉིད་རྟག་པ་ཉིད༌[^1615]མཐོང་བ་ནི་མེད་ལ། མཉན་བྱ་མ་ཡིན་པ་ཉིད་ཀྱི་ཡང་མ་ངེས་པ་ཡིན་པས་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2040]
གང་ཆོས་མཐུན་པ་དང་། ཆོས་མི་མཐུན་པ་དག་གིས་འདིའི་རྟག་པ་ཉིད་རྗེས་སུ་དཔོག་པར་བྱེད་དོ་ཞེས་འབྱུང་ངོ་། །དེ་འདིར་ཆོས་མི་མཐུན་པ་ལ་ཡོད་པ་ཉིད་དཔེ་ཡིན་ན། དེ་ལྟ་ན་ནི་མཉན་པར་བྱ་བ་ཉིད་མི་རྟག་པ་ཉིད་དུ་མཐོང་བ་ཡིན་ནོ།[^1616] །

[Block 2041]
འདི་འདྲ་བ་ཆོས་མི་མཐུན་པའི་དཔེ་སྦྱོར་བས་ཡིན་ན་ནི་གློག་རྟག་པ་ཡིན་ཏེ། རྩོལ་བ་ལས་མ་བྱུང་བའི་ཕྱིར་ཞེས་པ་སྐྱོན་མེད་པ༌[^1617]ཉིད་དུ་འགྱུར་རོ། །

[Block 2042]
རྩོལ་བ་ལས་མ་བྱུང་བའི་ནམ་མཁའ་རྟག་པ་དང་། རྩོལ་བ་ལས་བྱུང་བ་མི་རྟག་པ་ལ༌[^1618]ཕྱོགས་གཅིག་ཏུ་ངེས་པ་ཡང་མཐོང་བ་ཉིད་དོ། །

[Block 2043]
གཉིས་པ་ནི་ཕ་རོལ་པོས་བྱེ་བྲག་མེད་པར་མཚུངས་པ་ལ་གཏན་ཚིགས་མེད་པ་ཉིད་དུ་རྩོད་པར་བྱེད་དོ། །

[Block 2044]
དེ་ལ་ཕྱིན་ཅི་ལོག་ཉིད་མེད་པའི་ཕྱིར༌[^1619]སྐྱོན་གཞན་བརྗོད་པར་བྱའོ། །

[Block 2045]
དེ་བཞིན་དུ་ཕྲད་མ་ཕྲད་དང་གཏན་ཚིགས་མ༌[^1620]ཡིན་པ་མཚུངས་པ་དག་གིས། གཏན་ཚིགས་ཐམས་ཅད་བསལ་བའི་ཕྱིར་ལ། ཡང་འདི་དམ་བཅས་པའི་དོན་བསྐྱེད་པའི་སྒོ་ནས་གཏན་ཚིགས་ཀྱི་སྐྱོན་དུ་བརྗོད་པ་ཡང་མ་ཡིན་གྱི། འོན་ཀྱང་ཤེས་པར༌[^1621]བྱེད་པ་ཉིད་དོ། །

[Block 2046]
དེ་ལ་ཡང་ཕྲད་མ་ཕྲད་ཀྱི་སྐྱོན་དང་འབྲེལ་ཏོ། །

[Block 2047]
དེའི་ཕྱིར་དེ་ལྟར་ཡང་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་མ་ཡིན་ཞིང༌[^1622]དམིགས་པ་མཚུངས་པ་ཡང་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་མ་ཡིན་ལ་ཕ་རོལ་པོས་དེ་ལྟར་བརྩད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2048]
གཞན་ལ་ནི་མི་རྟག་པ་ལ་གཏན་ཚིགས་ཡོད་པ་ཡིན་ནོ། །

[Block 2049]
འོན༌[^1623]ཀྱང་དེ་དག་གིས༌[^1624]བསྒྲུབ་བྱ་གྲུབ་པ་མེད་པས་ཀྱང་གཏན་ཚིགས་མེད་པ་ཡིན་གྱི། གང་ཞིག་མེད་ཀྱང་དེ་དེའི་གཏན་ཚིགས་འབྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2050]
དེ་ལྟ་ན་ནི་དེའི་ལན་དུ་འགྱུར་རོ། །

[Block 2051]
དེ་ལྟ་མ་ཡིན་ན་ནི་ཕྱོགས་སྔ་མ་གཞན་བརྗོད་པར་འགྱུར་རོ། །

[Block 2052]
གཉིས་པ་ཡང་ཁྱབ་བྱེད་མ་ཡིན་པའི་ཕྱིར་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་གི་སྐྱོན་མ་ཡིན་ནོ། །

[Block 2053]
ཐེ་ཚོམ་མཚུངས་པར༌[^1625]ཡང་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་གི་ཡིན་གྱི།[^1626] འདི་ལྟར་བསྒྲུབ་བར་བྱ་བ་དང་གཏན་ཚིགས་ཀྱི་དོན་སྒྲོ་བཏགས་པ་ཡིན་ནོ། །

[Block 2054]
དམ་བཅའ་བ་ཕྱིན་ཅི་ལོག་གིས་ཀྱང་མངོན་པར་བརྗོད་པ་ཕྱིན་ཅི་ལོག་ཏུ་བཏགས་པའི་ཕྱིར་ཐམས་ཅད་དུ་ཕྱིན་ཅི་ལོག་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2055]
མ་བརྗོད་པ་མཚུངས་པ་ཡང་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་ཏུ་བརྗོད་པ་མ་ཡིན་ཏེ། ཕ་རོལ་པོས་འཇིག་པའི་གཏན་ཚིགས་སུ་བྱས་པ་ནི་མ་ཡིན་གྱི། སྔར༌[^1627]ནས་བརྗོད་པ༌[^1628]ཡོད་པའི་ཞེས་བརྗོད་དོ། །

[Block 2056]
བརྗོད་པའི་ཚེ་ན་ཡང་སྒྲའི་མི་རྟག་པ་ཉིད་ཐོབ་པ་མ་ཡིན་ཏེ། ཞིག་པའི་ཕྱིར་རོ། །

[Block 2057]
འབྲས་བུ་མཚུངས་པ་ཡང་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་གི་སྒོ་ནས་བརྗོད་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་ཅི་གཞན་གྱི་ཁོངས་སུ་འདུས་པ་ཉིད་ཀྱི་ཁྱད་པར་གྱིས་ཡིན་ནོ། །

[Block 2058]
དེའི་ཕྱིར་ལྟག་གཅོད་དེ་དག་གཏན་ཚིགས་ཕྱིན་ཅི་ལོག་ཉིད་དུ་མ་མཐོང་ངོ་། །

[Block 2059 [HEADING]]
#### ཡང་དག་པ་མ་ཡིན་པ། ^6-15-2-0

[Block 2060]
ཡང་དག་པ་མ་ཡིན་པ་ནི་ཐལ་བར་འགྱུར་པ་དང་། དོན་གྱིས་གོ་བར་མཚུངས་པ་ལ་སོགས་པའོ། །

[Block 2061]
དེ་ལ་རེ་ཞིག་ཐལ་བར་འགྱུར་བ་མཚུངས་པ་ནི་ཡང་དག་པ་མ་ཡིན་པ་སྟེ། གང་གི་ཕྱིར་དོན་གྱི་གཏན་ཚིགས་མ་མཐོང་ཡང་བསྒྲུབ་པར་བྱ་བ་བརྗོད་པས་སོ།[^1629] །

[Block 2062]
འདི་ལ་ཡང་ཕྱིན་ཅི་ལོག་དང་འགལ་བས་ཀྱང་བརྗོད་པར་ནུས་ཏེ། མ་མཐོང་བ་མཐོང་བ་ཡིན་པའི༌[^1630]ཕྱིན་ཅི་ལོག་དང་འགལ་བ་ཉིད་དོ་ཞེས་བྱས་ནས་སོ། །

[Block 2063]
དེ་བཞིན་དུ་དོན་གྱིས༌[^1631]གོ་བ་མཚུངས་པ་ཡང་ངོ་།[^1632] །ཇི་ལྟར་བསྒྲུབ་བྱ་མེད་པ་ལ༌[^1633]མ་དམིགས་པས་མེད་པར་དམིགས་པ་ཐོབ་པ་ཡང་དག་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་ཕྱིན་ཅི་ལོག་དང་འགལ་བ་ཡང་ངོ་། །

[Block 2064 [HEADING]]
#### འགལ་བ། ^6-15-3-0

[Block 2065]
འགལ་བ་ནི་མ་སྐྱེས་པ་དང་རྟག་པར་མཚུངས་པ་ལ་སོགས་པའོ། །

[Block 2066]
དེ་ལ་གང་གི་ཕྱིར་སྔ་ནས་སྐྱེས་པའི་སྒྲ་ཉིད་མེད་པ་དེའི་ཕྱིར་དེ་ལྟ་བུ་འགལ་བ་ཉིད་དོ། །

[Block 2067]
མེད་པ་ཡང་མི་རྟག་པའོ་ཞེས་འགལ་བ་ཡང་ངོ་། །དེ་བཞིན་དུ་ཡང་དག་པ༌[^1634]མ་ཡིན་པ་ཡང་ངོ་། །ཡོད་པ་རྟག་པའི༌[^1635]ཕྱིར་མེད་པའོ་ཞེས༌[^1636]རྟག་པ་ཉིད་ཕྱིན་ཅི་ལོག་ཏུ་མེད་ཀྱང་ངོ༌[^1637]ཞེས་བྱས་ནས་སོ། །

[Block 2068]
རྟག་པ་མཚུངས་པ་ཡང་ཇི་ལྟར་འགལ་བ་བཞིན་དུ་ཕྱིན་ཅི་ལོག་ཏུ་མེད་པར་བརྗོད་པར་ནུས་ཏེ། འདི་ལྟར་མི་རྟག་པ་དང་རྟག་པ་འགལ་བས་སོ། །

[Block 2069]
དེ་བཞིན་དུ་ཕྱིན་ཅི་ལོག་དང་ཡང་དག་པ་མ་ཡིན་པ་ཡང་དེ་ལྟར་རྟག་པ་ཉིད་ཡིན་ནོ། །

[Block 2070]
དེའི་ཕྱིར་ལྟག་གཅོད་རྣམས་ལ་ཕྱིན་ཅི་ལོག་དང་ཡང་དག་པ་མ་ཡིན་པ་དང་འགལ་བ་ཉིད་རྣམས་འདྲེས་པས་སྐྱོན་མེད་པར་བརྗོད་པར་མི་ནུས་སོ། །
--- END BLOCKS ---
