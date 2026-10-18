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
[Block 2136]
ཚོལ་བ་རྣམ་གསུམ་ནི་འདོད་པའི་ཚོལ་བ་དང་། སྲིད་པའི་ཚོལ་བ་དང་། [^1800]ལོག་པའི་སྤྱོད་པས་ཚོལ་བའོ། །

[Block 2137]
མདོ་ལས་དབང་པོ་དང་སྟོབས་དང་། བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་ཞེས་པ་ནས་ཡིད་བདེ་བ་ཆེན་པོ་དང་ལྡན་པར་བྱོས་ཤིག་ཅེས་པའི་བར༌[^1801]ནི་འདིས་ཐེག་པའི་དམིགས་པའི་ཡོན་ཏན་བསྟན་ཏེ་ཐེག་པ་ཆེན་པོ་དེ་སྟོབས་དང་། མི་འཇིགས་པ་དང་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་དང་། འཕགས་པའི་ལམ་ཡན་ལག༌[^1802]བརྒྱད་དང་། བསམ་གཏན་བཞི་དང་། སྙོམས་པར་འཇུག་པ་དགུ་དང་། རྣམ་པར་ཐར་པ་བརྒྱད་དང་། ཏིང་ངེ་འཛིན་གསུམ་ལ་སོགས་པ་ལ་དམིགས་ཤིང་གནས་པའི་ཕྱིར་བདེ་བ་དང་ཡིད་བདེ་བ་སྐྱེ་ཞེས་པའི་དོན་ཏོ། །

[Block 2138 [HEADING]]
###### **ཐེག་པ་རྣམ་གསུམ་སོ་སོར་གྲོལ་བ་ཐོབ་པ།** ^4-3-5-4-1-2-1-3-0

[Block 2139]
མདོ་ལས་དེ་ལ་ཤཱ་རིའི་བུ་སེམས་ཅན༌[^1803]གང་མཁས་པར་འགྱུར་ཞེས་པ་ནི་བྱིས་པ་ཁ་ཅིག་རི་དགས་ཀྱི་ཤིང་རྟ་འདོད་དེ་འབྱུང་བ་བཞིན་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ལ་བརྟེན་ཏེ། ཐེག་པ་རྣམ་གསུམ་སོ་སོར་གྲོལ་བ་ཐོབ་པར་སྟོན་པ་ལ། འདི་ཉན་ཐོས་ཀྱི་ཐེག་པ་དང་སྦྱར་ཏེ་དཔེ་དང་དོན་དུ༌[^1804]སྦྱར་བར་དབྱེའོ། །

[Block 2140]
མཁས་པར་གྱུར་པ་ཞེས་པ་ནི་མཐུ་རྣམ་བཞི་སྟོན་ཏེ་མཁས་པ་ནི་རྒྱུ་དང་ལྡན་པའི་མཐུའོ། །

[Block 2141]
དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནི་དགེ་བའི་བཤེས་གཉེན་གྱི་མཐུའོ། །

[Block 2142]
ཕ་རོལ་གྱི་སྒྲ་ཐོས་ཞེས་པ་ནི་ཡིད་ལ་བྱེད་པའི་མཐུའོ། །

[Block 2143]
བརྩོན་པར་བྱེད་ཅེས་པ་ནི་ཚོགས༌[^1805]པའི་མཐུའོ།[^1806] །དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་བ་དང་ཕྲད་དེ། རིགས་ཀྱི་རྒྱུ་བཞིན་དུ་སེམས་བསྐྱེད་ལ་དད་པས་ཆོས་ཉན༌[^1807]ཅིང་བརྩོན་པས་ཚིག་སྩོགས༌[^1808]པའོ། །

[Block 2144]
བརྩོན་པ་ནི་སྤྱོད་པ་ཐམས་ཅད་སྡུད་པའི་གཙོ་བོ་ཡིན་ནོ། །

[Block 2145]
བདག་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ཞེས་པ་ནི་སྤྱོད་པ་ཞན་པས་གཞན་གྱི་དོན་མི་བྱེད་པའོ། །

[Block 2146]
ཕ་རོལ་ལས་ཐོས་ཞེས་པ་ཡང་འཕགས་པའི་མན་ངག་པས་འབྲས་བུ་རྙེད་པར་འགྱུར་གྱི༌[^1809]གཞན་གྱིས༌[^1810]མ་ཡིན་ཞེས་པའོ། །

[Block 2147]
མདོ་ལས་སེམས་ཅན་གཞན་སློབ་དཔོན་མེད་པའི་ཡེ་ཤེས་དང་ཞེས་པ་ནས་བྱིས་པ་ཁ་ཅིག་རའི་ཤིང་རྟ་འདོད་པ་དེ་འབྱུང་བ་བཞིན་ནོ་ཞེས་པའི་བར་དུ་ནི་འདི་ནི་མཐུ་རྣམ་གསུམ་གྱིས༌[^1811]འབྱུང་བར་བྱེད་པ༌[^1812]དེའི་རྒྱུ༌[^1813]མི་དགོས་པར༌[^1814]རང་བཞིན་གྱི༌[^1815]ཤེས་པས་སངས་རྒྱས་མི་བཞུགས་པའི་འཇིག་རྟེན་དུ་འབྲས་བུ་ཐོབ་པར་བྱེད་པ་སྟེ། འཕགས་པ་ཉན་ཐོས་ལྟར་བཅོམ་ལྡན་འདས་ཀྱི་གསུང་མངོན་དུ་ཐོས་པས་ལམ་ཐོབ་པ་ལྟར་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་ཏེ་འབྱུང་བའི་དོན་ཟབ་མོ་རྟོགས་པས༌[^1816]འབྲས་བུ་ཐོབ་ཅེས་པའོ། །

[Block 2148]
དེ་ཡང་བསེ་རུ་བཞིན་གནས་པ་དང་ཁྱུས་ལྡིང་པའོ། །

[Block 2149]
སྔར་བཅོམ་ལྡན་འདས་ཀྱི་བསྟན་པ་ལ་ཞུགས་པ་ལ་ཕྱིས་འབྲས་བུ་ཐོབ་པས་ན་རང་གིས་རིག་ཞེས༌[^1817]པའོ། །

[Block 2150]
མདོ་ལས་སེམས་ཅན་གཞན་ཡང་ཐམས་ཅད་མཁྱེན་གྱི༌[^1818]ཡེ་ཤེས་ཞེས་པ་ནས་བུས་པ་ཁ་ཅིག་གླང་གི༌[^1819]ཤིང་རྟ་འདོད་དེ་འབྱུང་བ་ཡིན༌[^1820]ནོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་དང་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཞེས་དབྱེ་ཞིང་སྟོན་ཏེ། ཐམས་ཅད་མཁྱེན༌[^1821]པ་ནི་སྟོང་པ་མཁྱེན་པའི་ཡེ་ཤེས་སོ། །

[Block 2151]
ཐེག་པ་རྣམ་གསུམ་ཀུན་ལ་ཡང་ཡེ་ཤེས་མངའ་མོད་ཀྱི་དངོས་པོ་ལ་གཟིགས་པའི་ཡེ་ཤེས་ནི་བཅོམ་ལྡན་འདས་ཉག་གཅིག་ལ་མངའ་བ་དང་རང་རིག་པའི་ཡེ་ཤེས་ཉིད་ནི་རང་བྱུང་གི་ཡེ་ཤེས་སོ། །

[Block 2152]
གཞན་ལ་ལྟོས་པ༌[^1822]མེད་པར་མཁྱེན་པ་ནི༌[^1823]མཁན་པོ་མེད་པའི་ཡེ་ཤེས་སོ། །

[Block 2153]
ཡང་ན་དེ་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ནི་རང་བྱུང༌[^1824]གི་ཡེ་ཤེས་སོ། །

[Block 2154]
ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་ནི་མཁན་པོ་མེད་པའི་ཡེ་ཤེས་སོ། །

[Block 2155]
ཡེ་ཤེས་དེ་གཉིས་ཀྱི་འཁོར་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ནང་གི་ཡོན་ཏན་དག་གོ། །

[Block 2156]
ཡོན་ཏན་དེ་དག་གིས༌[^1825]འགྲོ་བ་རྣམས་བྱམས་པ་དང་ཐུགས་རྗེས་ཕན་པ་དང་བདེ་བར་མཛད་ཅིང་སེམས་ཅན་སྒྲོལ་བས་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 2157]
བྱང་ཆུབ་ཞེས༌[^1826]པ་ནི་ཐེག་པ་རྣམ་གསུམ་ཐུན་མོང་གི་མིང་སྟེ་དེ་དག་ལ་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར་སེམས་དཔའ་ཆེན་པོ་ཞེས་སྨོས་སོ། །

[Block 2158 [HEADING]]
###### **ཡང་དག་པ་ཉིད་སྟོན་པ།** ^4-3-5-4-1-2-2-0

[Block 2159 [HEADING]]
###### **ཡང་དག་བསྟན་པ།** ^4-3-5-4-1-2-2-1-0

[Block 2160]
མདོ་ལས་ཤཱ་རིའི་བུ་འདི་ལྟ་སྟེ་དཔེར་ན་ཞེས་པ་ནས་བུས་པ་དེ་དག་ལ་བཞོན་པ་ཆེན་པོ་གཅིག་བྱིན་པ་དེ་བཞིན་དུ་ཞེས་པའི་བར་དུ་ནི་ཡང་དག་པ་ཉིད་སྟོན་པ་ལ་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ། ཡང་དག་ལ༌[^1827]བསྟན་པ་དང་། ཐེ་ཙོམ་དགྲོལ་བའོ།[^1828] །དེ་ཡང་བུ་རྣམས་ཀྱི་རེ་བ་ལས་འགལ་བ་བསྟན་པ་དང་། དཔེ་དང་དོན་དུ་སྦྱར་བའོ། །

[Block 2161]
དཔེ་ལ་ཡང་བུའི་ཕྱིར་ཐོན་པ༌[^1829]མཐོང་བ་དང་། ཕའི་ཡིད་རངས་པ་བསྟན་པ་སྟེ། མདོ་དང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 2162]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་མྱ་ངན་ལས་འདས་པའི༌[^1830]བདེ་བ་ཐོབ་པར་གཟིགས་ན་ཞེས་པའི་བར་དུ་ནི་ཕའི་བསམ་པ་བསྟན་ཏེ་ཁམས་གསུམ་གཡང་ཟ་བ་མེ་འབར་བའི་ཁང་པ་ལྟ་བུ་ལས་འགྲོ་བ་མང་པོ་བཏོན་ནས་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ཡང་དག་པའི་སྒོར་གཟུད་པ་དང་། མྱ་ངན་ལས་འདའ་བའི་བདེ་བ་དམ་པ་ལ་ཡོངས་སུ་བཀོད་དེ་འཇིགས་པ་དང་འཚེ་བ༌[^1831]ཐམས་ཅད་ལས་ཐར་ཞེས་པའི་དོན་ཏོ། །

[Block 2163]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་དག་ལ་དེའི་ཚེ་ཞེས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་བྱེད་ཀྱི༌[^1832]ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་རྣམ་གཉིས་དང་བྱང་ཆུབ་སེམས་དཔའ་ལས་སྲས་སུ་འདྲ་བས་གཟུད་པའི་ཕྱིར་དེ་གཉི་ག་ཡང་ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདའ་བ་ལ་དགོད་ཀྱི་གཞན་ལ་མི་གསུང་ཞེས་པའི་དོན་ཏོ། །

[Block 2164]
མདོ་ལས་སེམས་ཅན་གང་ལ་ཡང་ཞེས་པ་ནས་དགའ་བར་འགྱུར་བ་ཐམས་ཅད་ཁ་དོག་གཅིག་པ་སྦྱིན་པར་མཛད་དོ་ཞེས་པའི་བར་དུ་ནི་དེ་ཡང་ཐེག་པའི་རང་བཞིན་དང་ཐེག་པའི་ཡོན་ཏན་སྟོན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2165]
མ་ངེས་པའི་རིགས་ཅན་དང་། བྱང་ཆུབ་སེམས་དཔའི་རིགས་དང་ཉན་ཐོས་པའི་རིགས་རྣམས་ལ་དགེ་བ་ཐམས་ཅད་རྫོགས་པར༌[^1833]བསྟན་པའི་ཕྱིར་ཐེག་པ་རྣམ་གཅིག་བྱིན་པ་བསྟན་ཏོ། །

[Block 2166]
ཁ་དོག་གཅིག་པ་བདེ་བ་དམ་རྩེན༌[^1834]པ། །ཞེས་པ་ནི་ཐེག་པའི་ཡོན་ཏན་བསྟན་ཏེ། རྒྱུ་དང་འབྲས་བུ་ཐམས་ཅད་ཉོན་མོངས་པ་དང་མ་འདྲེས་པ་ནི་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་གཞིར༌[^1835]གྱུར་པའོ། །

[Block 2167]
ཟག་པ་མེད་པའི་ཆོས་ཅན་འཕགས་པ་རྣམས་ཀྱིས༌[^1836]བསྔགས་པར་བྱའོ།[^1837] །

[Block 2168 [HEADING]]
###### **ཐེ་ཚོམ་དགྲོལ་བ།** ^4-3-5-4-1-2-2-2-0

[Block 2169]
མདོ་ལས་ཤཱ་རིའི་བུ་འདི་ལྟ་སྟེ་ཐམས་ཅད་ལ་བྱིན་པའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་མ་ཡིན་པ་དེ་བཞིན་དུ་ཞེས་པ་ནི་ཐེ་ཚོམ་བསལ་བ་བསྟན་ཏེ། དཔེས་གླེང་བ་དང་། དོགས་པ་བསལ་བ་དང་། དྲིས་པ་དང་། དེའི་ལན་ལ་སོགས་པ་ཅི་རིགས་པ་དང་སྦྱར་རོ། །

[Block 2170]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་ཟློ་བའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་མ་ཡིན་ནོ་ཞེས་པའི་བར་དུ་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 2171]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་བང་མཛོད་མང་པོ་དང་ལྡན་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་གཅིག་པོ་འདི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་དང་ལྡན་ཏེ། སེམས་ཅན་རྣམ་པ་སྣ་ཚོགས་ཀྱི་རིགས་ཅན་ཐམས་ཅད་ཀྱིས་དེ་ལ་ལོངས་སྤྱོད་དུ་ཟིན་གྱིས་ཀྱང་མི་ཟད་པ་བསྟན་ཏོ། །

[Block 2172]
མདོ་ལས་སེམས་ཅན་ཀུན་ཐམས་ཅད་མཁྱེན་གྱི་ཡེ་ཤེས་དང་ལྡན་པའི་ཆོས་ཞེས་པ་ནས་གཞུང་འདིས་ཀྱང་དེ་ལྟ་བུར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་འདིས་བསྡུས་པ་བསྟན་ཏེ་ཐེག་པ་གཅིག་པོ༌[^1838]སྟོན་པའི་རིགས་པ༌[^1839]དང་། རྒྱུ་དང་རྐྱེན་གྱི༌[^1840]ཐེག་པ་རྣམ་གསུམ་དུ་སྟོན་པའི་བྱེ་བྲག་དང༌[^1841]གཏན་ཚིགས་བསྟན་པས་འབྲས་བུ་བླ་ན་མེད་པ་ནི་གཅིག་ཏུ་ཟད་པར་བཤད་པ་ཡིན་ནོ།། །།

[Block 2173]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། བམ་པོ་དྲུག་པ།

[Block 2174 [HEADING]]
###### ཚིགས་སུ་བཅད་པ། ^4-3-5-4-2-0

[Block 2175]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་གསུངས་སོ་ཞེས་པ་ནས། ཀ་བའི་རྩ་བ་རུལ་བར་འགྱུར། །ཞེས༌[^1842]པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བརྒྱ་དང༌[^1843]དྲུག་ཅུ་རྩ་ལྔ་ཞིག་ཡོད་པ་ལས་དུམ་བུ་གཉིས་སུ་དབྱེ་སྟེ། དང་པོར་ཚིགས་བཅད་བརྒྱ་དང་དྲུག༌[^1844]ཅུ་རྩ་ཕྱེད་དང་ལྔས་ནི་ཆོས་དང་དཔེར་སྦྱར་བ་སྔར་སྨོས་པ་རྣམས་བསྟན་ཏེ། ཤཱ་རིའི་བུ་ཁྱོད་ལ་སོགས་པ་ཐམས་ཅད་ངའི་སྲས་ཡིན་ཞེས་པ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
