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
ཡོན་ཏན་གཞན་ལ་རག་མ་ལུས་པ་ནི་བདག་གིས༌[^1870]ཡོན་ཏན་རྣམས་ཐོབ་པར་བྱ་བ་གཞན་ལ་མི་བརྟེན་ཞིང་གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པའོ། །

[Block 2137]
བདག་གི་ཡོན་ཏན་མི་སྙེམས་པ་ནི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་ཤིང་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 2138]
གཞན་གྱི་ཡོན་ཏན་བརྗོད་པ་ནི་ཕྲག་དོག་མེད་པའི་ཕྱིར་རོ། །

[Block 2139]
ལེགས་པར་བྱ་བའི་ལས་བྱེད་པ་ནི་དགེ་བ་ཤ་སྟག་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2140]
ལས་ཀྱི་རྣམ་པར་སྨིན་པ་དང་འགལ་བར་མི་བྱེད་པ་ནི་སྟོང་པ་ཉིད་ཀྱི་ཆོས་རྟོགས་ཀྱང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོད་པར་ལྟ་བའོ། །

[Block 2141]
ལས་ཡོངས་སུ་དག་པའི་ཡེ་ཤེས་ནི་ལུས་དང་ངག་དང་ཡིད་གསུམ་གྱི་ལས་ཡོངས་སུ་དག་པར་བྱེད་པ་ལ་མཁས་པའོ། །

[Block 2142 [HEADING]]
#### ཡེ་ཤེས་ཀྱི་ཚོགས་རྣམ་པ་བཞི། ^7-2-3-0

[Block 2143]
ཡེ་ཤེས་ཀྱི་ཚོགས་རྣམ་པ་གཞན་ཡང་བསྟན་པར་བཞེད༌[^1871]ནས། གཞན་ཡང་ཡེ་ཤེས་ཀྱི་ཚོགས་རྣམ་པ་བཞི་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཡེ་ཤེས་སྐྱེ་བའི་རྒྱུ་རྣམ་པ་བཞི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2144]
སྟན་ནི་སེང་གེའི་ཁྲི་ལ་སོགས་པའོ། །

[Block 2145]
བཀུར་སྟི་ནི་ཕྱག་འཚལ་བ་ལ་སོགས་པའོ། །

[Block 2146]
ཚིགས་སུ་བཅད་པ་ནི་བསྟོད་པའོ། །

[Block 2147]
ཆོས་བསྡུ་བ་ནི་བདག་ཉིད་ཀྱིས་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2148]
གཡོ་མེད་པ་ནི་ཀུ་རེའི་བསམ་པ༌[^1872]མ་ཡིན་གྱི་སྙིང་ཐག་པ་ནས་དང་བའི་སེམས་ཀྱིས་སོ། །

[Block 2149]
ཇོ་བོ་བཞིན་དུ་སྲུང་བ༌[^1873]ནི་རྒྱལ་པོ་ལ་ཕངས་ཤིང་གཅེས་པ་བཞིན་དུ་ཆོས་སྨྲ་བ་ཡང་ཕངས་ཤིང་གཅེས་པར་བྱེད་ཅིང་ཆུད་མི་ཟ་བར་སྲུང་བར་བྱེད་པའོ། །

[Block 2150]
ཡང་ན་རྒྱལ་པོའི་འཇིགས་པ་ལས་སྐྱོབ་པར་བྱེད་པའོ། །

[Block 2151]
དགེ་བའི་རྩ་བ་སྲུང་བ༌[^1874]ནི༌[^1875]ཇི་ནས་ཀྱང་ཆོས་སྨྲ་བ་དེའི་དགེ་བའི་རྩ་བ་རྐྱེན་གཞན་གྱིས་བསྐལ་ནས་ཕངས་པར་མི་འགྱུར་བའི་ཐབས་སྦྱོར་ཞིང་བྱ་བ་བྱེད་པའོ། །

[Block 2152]
ཡུལ་དང་ལྗོངས་ཀྱི་ཕྱོགས་སྲུང་བ༌[^1876]ནི༌[^1877]ཆོས་སྨྲ་བ་དེ་ཡུལ་དང་ལྗོངས་རྒྱུ་བའི་ཚེ་དེ་ཕྱིས་ཀྱི་འཇིགས་པ༌[^1878]སྣ་ཚོགས་ལས་སྐྱོབ་པའོ། །

[Block 2153]
ཕན་པའི་དངོས་པོ་སྲུང་བ༌[^1879]ནི་ཕན་ནོ་ཅོག་དང་སྦྱོར་ལ། གནོད་དོ་ཅོག་ལས་བཟློག༌[^1880]པའོ། །

[Block 2154]
ཟང་ཟིང་གིས་ཉེ་བར་རྟོན་པ་ནི་བཟའ་བ་དང་བགོ་བ་ལ་སོགས་པའི་ཟང་ཟིང་གིས༌[^1881]ཕོངས་པ་མེད་པར་ཕན་འདོགས་པའོ། །

[Block 2155]
ཆོས་ཀྱིས་ཉེ་བར་རྟོན་པ་ནི་དེས་བཤད་པའི་དམ་པའི་ཆོས་རིང་དུ་གནས་པར་འགྱུར་བའི་བྱ་བ་བྱེད་པའོ། །ཤེས་རབ་ཀྱིས་ཉེ་བར་རྟོན་པ་ནི་དེའི་ཤེས་རབ་ཉམས་པར་མི་འགྱུར་བའི་ཐབས་སྣ་ཚོགས་ཤོམ་པའོ། །

[Block 2156]
ཡེ་ཤེས་ཀྱིས་ཉེ་བར་རྟོན་པ་ནི་ཡེ་ཤེས་གོང་ནས་གོང་དུ་སྐྱེ་ཞིང་ཉམས་པར་མི་འགྱུར་བའི་བྱ་བ་བྱེད་པ་སྟེ་སྟོན་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་ལྟ་བུ་ལ་བྱའོ། །

[Block 2157]
མོས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཆོས་དང་ཆོས་སྨྲ་བ་ལ་ཡིད་ཆེས་པ་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2158]
ཐོས་པ་ཚོལ་བ་ནི་རྒྱུན་དུ་ཆོས་ཉན་པ༌[^1882]ཚོལ་པའོ། །

[Block 2159]
བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ༌[^1883]ནི་བདག་དང་གཞན་ལ་ཕན་པའི་བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པའོ། །

[Block 2160]
མཉམ་པ་ཉིད་ལ་སེམས་ངེས་པར་སེམས་པ་ནི་སྟོང་པ་ཉིད་ལ་སེམས་རྩེ་གཅིག་ཏུ་འཇོག་པའོ། །

[Block 2161]
ཐོས་པའི་སྟོབས་ནི་ཉན་པའི་དུས་ན་ཆོས་རྣམས་རྟོགས་པར་ནུས་པའི་མཐུ་དང་ལྡན་པའོ། །

[Block 2162]
ཆོས་ལ་རབ་ཏུ་དགའ་བའི་ཚུལ་ཁྲིམས་ནི་དམ་པའི་ཆོས་ཉན་པར་མོས་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 2163]
ཆོས་ཡོངས་སུ་ཚོལ་བ་ནི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ཞིང་ཉན་པ་དང་། ཀློག་པ་དང་འདྲི་བ་ལ་སོགས་པ་བྱེད་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 2164]
ཆོས་ལ་ངེས་པར་སེམས་པ་ནི་ཆོས་ཇི་ལྟར་བཙལ་བ་ལ་རིགས་པ་རྣམས་ཀྱིས་འཇལ་བའི་རང་བཞིན་ནོ། །

[Block 2165]
ངན་དུ་བརྗོད་པ་དང་ངན་དུ་སྨྲ་བ་ཞེས་བྱ་བ་ནི་གཅིག་ཏུ་ཆོས་ཚོལ་བ་ལ་འབད་པས་ཆོས་ཚོལ་བའི་ཚེ་གཞན་གྱིས་འཕྱས་བཏགས་ཤིང་མི་སྙན་པར་སྨྲ་བ་རྣམས་བཟོད་པའོ། །

[Block 2166]
ངན་དུ་བརྗོད་པ་ནི་ལྐོག་ནས་སྐྱོན་བརྗོད་པའོ། །

[Block 2167]
ངན་དུ་སྨྲ་བ་ནི་དངོས་སུ་སྨྲ་བའོ། །

[Block 2168]
མཁན་པོ་དང་སློབ་དཔོན་དང་མཐུན་པར་འཇུག་པའི་བཟོད་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་ཕྱིར་དེ་དག་གིས༌[^1884]ཇི་སྐད༌[^1885]བསྒོ་བ་བཞིན་བྱེད་པའི་སྡུག་བསྔལ་བཟོད་པའོ། །

[Block 2169]
ཉན་པའི་བརྩོན་འགྲུས་ནི་གཞུང་མང་དུ་ཉན་པར་བྱེད་པའི་ཕྱིར་འབད་པའོ། །

[Block 2170]
འཛིན་པའི་བརྩོན་འགྲུས་ནི་མཉན་ནས་དོན་མི་བརྗེད་པར་བྱེད་པའི་ཕྱིར་འབད་པའོ། །

[Block 2171]
བསྟན་པའི་བརྩོན་འགྲུས་ནི་ཇི་ལྟར་མཉན་ཅིང་བཟུང་བའི་ཆོས་གཞན་ལ་བསྟན་པ་ལ་འབད་པར་བྱེད་པའོ། །

[Block 2172]
ནན་ཏན་གྱི་བརྩོན་འགྲུས་ནི་མཉན་པ་དང་བཟུང་བའི་ཆོས་བསྒོམ་པར་བྱ་བ་ལ་འབད་པར་བྱེད་པའོ། །

[Block 2173]
དབེན་པ་ནི་ལུས་དབེན་པ་ལ་གནས་པ་ཚོལ་བའོ། །

[Block 2174]
རྩེ་གཅིག་པ་ནི་སེམས་དབེན་པ་ལ་ཚོལ་བའོ། །

[Block 2175]
བསམ་གཏན་དང་མངོན་པར་ཤེས་པ་ཚོལ་བ་ནི་བསམ་གཏན་ལ་བརྟེན་ནས་མངོན་པར་ཤེས་པ་ལྔ་ཐོབ་པར་བྱེད་པའོ། །
--- END BLOCKS ---
