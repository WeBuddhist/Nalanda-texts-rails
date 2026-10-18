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
[Block 211]
བརྒྱད་པའི་ས་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་འཇུག་པའི་ས་སྟེ། དེ་ནི་དགྲ་བཅོམ་པའི་འབྲས་བུ་ལ་གནས་པ་ནས་བཟུང་སྟེ་བགྲངས་ནས་བརྒྱད་པར་འགྱུར་རོ། །

[Block 212]
མཐོང་བའི་ས་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་གནས་པའི་སའོ། །

[Block 213]
བསྲབས་པའི་ས་ཞེས་བྱ་བ་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་ས་སྟེ། དེའི༌[^151]འདོད་པའི་འདོད་ཆགས་ལ་སོགས་པ་སྲབ་མོར་བྱས་པ་ཙམ་དུ་ཟད་དོ། །

[Block 214]
འདོད་ཆགས་དང་བྲལ་བའི་ས་ནི་ཕྱིར་མི་འོང་བ་སྟེ།[^152] དེས་འདོད་པ་ལ་འདུན་པ་དང་གནོད་སེམས་ཡང་དག་པར་བཅད་པ་དང༌[^153]འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ནོ། །

[Block 215]
བྱས་པ་རྟོགས་པ་ཅན་གྱི་ས་ནི་དགྲ་བཅོམ་པ་ཉིད་དེ། བྱ་བ་བྱས་སོ་ཞེས་ཁོང་དུ་ཆུད་པ་ནི་བྱས་པ་རྟོགས་པ་སྟེ། དེ་འདི་ལ་ཡོད་པས་ན་བྱས་པ་རྟོགས་པ་ཅན་ཞེས་བྱ་སྟེ་དགྲ་བཅོམ་པའོ། །

[Block 216]
ཡང་ན་འདི་བྱས་པ་ཁོང་དུ་ཆུད་པའི་ངང་ཚུལ་ཅན་ཡིན་པས་བྱས་པ་རྟོགས་པ་ཅན་ཏེ། དེའི་ས་ནི་བྱས་པ་རྟོགས་པ་ཅན་གྱི་སའོ། །

[Block 217]
ཐེག་པ་ཆེན་པོ་ལ༌[^154]ཡང་དག་པར་ཞུགས་པ་བསྟན་པའོ། །

[Block 218 [HEADING]]
#### ཐེག་པ་དེ་གང་ནས་ངེས་པར་འབྱུང་བ། ^1-1-3-0

[Block 219]
དེ་ལྟར་ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་བསྟན་ནས། དེའི་འོག་ཏུ་ཐེག་པ་དེ་གང་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ཞུས༌[^155]པས་གསུམ་པ་བརྩམས་ཏེ། ཁམས་གསུམ་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཞིང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་གང་ན་བ་དེར་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་དག་ལ་ཡང་ཁམས་གསུམ་ནས་ངེས་པར་འབྱུང་བ་ཡང༌[^156]ཡོད་པས་དེ་བསལ་བའི༌[^157]ཕྱིར་ཁམས་གསུམ་ནས་བྱུང་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བས་ཐེག་པ་ཆེན་པོ་ལ་བྱ་བ་གཉིས་ཡོད་པར་བསྟན་ཏེ། ཐེག་པ་ཆེན་པོ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་གནས་པར་འགྱུར་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 220]
དེ་ཡང་གཉིས་སུ་མེད་པའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ནི་གཉིས་ལ་ཐ་དད་པ་ཡོད་དོ༌[^158]སྙམ་དུ་ལོག་པར་ཞུགས་པ་རྣམས་ལ་འབྲས་བུ་ཐ་དད་པ་མེད་པར་སྟོན་ཏེ། ཐེག་པ་ཆེན་པོ་ལ་འབྲས་བུའི་གནས་སྐབས་ན་སངས་རྒྱས་ཉིད་དུ་ཟད་པས་ཐེག་པ་ཆེན་པོ་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་ཐ་དད་པ་མེད་དོ། །

[Block 221]
དེ་བས་ན་གཉིས་སུ་མེད་པ་ཉིད་དེ། དེའི་ཕྱིར་ཆོས་འདི་གཉིས་ནི་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གཅིག་པ་དང་ཐ་དད་པའི་མཚན་ཉིད་མེད་པར་བསྟན་པའོ། །

[Block 222]
ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ལ། གཅིག་པ་མེད་པའི་ཕྱིར་ལྡན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 223]
ཐ་དད་པ་མེད་པའི་ཕྱིར་མི་ལྡན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 224]
འཛུགས་པར་མི་བྱེད་པའི་ཕྱིར་གཟུགས་མེད་པའོ། །

[Block 225]
བསྟན་པར་མི་ནུས་པས་བསྟན་དུ་མེད་པའོ། །

[Block 226]
འདི་གཉིས་ཀྱིས་ནི་འཛིན་པ་དང་། གཟུང་བ་མེད་པར་བསྟན་ཏེ། གང་གི་ཕྱིར་འཛུགས༌[^159]པར་མི་བྱེད་པ་དེའི་ཕྱིར་འཛིན་པ་མེད་པའོ། །

[Block 227]
གང་གི་ཕྱིར་བསྟན་པར་མི་ནུས་པ་དེའི་ཕྱིར་གཟུང་བ་མེད་པའོ། །

[Block 228]
ཐོགས་པ༌[^160]མེད་པ་ཞེས་བྱ་བ་འདིས་ནི་དབང་པོ་དང་། ཡུལ་ལྟར་ཐོགས༌[^161]པའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་ཡུལ་དང་། ཡུལ་ཅན་མེད་པར་བསྟན་པའོ། །

[Block 229]
དེ་ལྟར་མཚན་ཉིད་མེད་པའི་ཕྱིར་མཚན་ཉིད་མེད་པ་སྟེ། གཉི་ག་ཡང་མཚན་ཉིད་མེད་པར་མཚན་ཉིད་གཅིག་པའི་ཕྱིར། འདི་ལྟར་མཚན་ཉིད་མེད་པར་མཚན་ཉིད་གཅིག་པའོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 230]
རབ་འབྱོར་མཚན་ཉིད་མེད་པའི་ཆོས་ལ༌[^162]ནི་འབྱུང་བའམ། འབྱུང་བར་འགྱུར་བའམ། འབྱུང་བར༌[^163]འགྱུར་བ༌[^164]མེད་དོ་ཞེས་བྱ་བ་ནི། འདི་ལྟར༌[^165]ཡོངས་སུ་གྲུབ་པའི་ཆོས་ནི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཐམས་ཅད་དང་བྲལ་ཞིང་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པ་སྟེ། དེའི་ཕྱིར་རང་བཞིན་གྱིས་ངེས་པར་འབྱུང༌[^166]ཟིན་པས་དེ་ལ་གློ་བུར་གྱི་ངེས་པར་འབྱུང་བ་མེད་དོ། །

[Block 231]
རབ་འབྱོར་མཚན་ཉིད་མེད་པའི་ཆོས་རྣམས་ལས་ངེས་པར་འབྱུང་བར་འདོད་པ་གང་ཡིན་པ༌[^167]དེ་ནི་དེ་བཞིན་ཉིད་འབྱུང་བར་འདོད་དུ་ཟད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གློ་བུར་གྱི་ངེས་པར་འབྱུང་བ་མེད་པ་དེ་ཉིད་རྒྱ་ཆེར་བསྟན་ཏོ། །

[Block 232]
དེ་བཞིན་ཉིད་ནི་རང་བཞིན་ཉིད་ཀྱིས་ཅིས་ཀྱང་མ་གོས་ཤིང་ནམ་མཁའ་ལྟ་བུ་ལ་ངེས་པར་འབྱུང་བ་མེད་དོ། །

[Block 233]
དེ་བས་ན་རབ་འབྱོར་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ནི་ཁམས་གསུམ་ནས་ངེས་པར་འབྱུང་བ་མེད་དོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 234]
དེ་བཞིན་ཉིད་ནི་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཀྱིས༌[^168]སྟོང་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ལ་དེ་བཞིན་ཉིད་ཀྱི༌[^169]ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ཀུན་བརྟགས་པ་གང་ཡང་མེད་ན། གང་གི་ཕྱིར་དེ་དེ་ལས༌[^170]ངེས་པར་འབྱུང་བར་འགྱུར། དེ་བཞིན་ཉིད་ལ་སོགས་པ་བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་ཀྱི་མཐར་ཐུག་པའི་བར་འོག་ནས་འབྱུང་བ༌[^171]དག་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 235]
སྤོང་བའི་དབྱིངས་དང་། འདོད་ཆགས་དང་བྲལ་བའི་དབྱིངས་དང་། འགོག་པའི་དབྱིངས་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དེ༌[^172]ཉོན་མོངས་པ་དང་། ཤེས་བྱའི༌[^173]སྒྲིབ་པའི་སྤྲོས་པ་ཐམས་ཅད་སྤོང་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་སྤོང་བའི་དབྱིངས་ཞེས་བྱའོ། །

[Block 236]
སྲིད་པ་གསུམ་གྱི་འདོད་ཆགས་དང་བྲལ་བའི་རྒྱུ་ཡིན་པ་དང་། འཇིག་རྟེན་ཐམས་ཅད་ལས་འདས་པའི་ཕྱིར་འདོད་ཆགས་དང་བྲལ་བའི་དབྱིངས་ཞེས་བྱའོ། །

[Block 237]
སྡུག་བསྔལ་ཐམས་ཅད་འགོག་པའི༌[^174]རྒྱུ་ཡིན་པས་འགོག་པའི་དབྱིངས་ཞེས་བྱའོ། །

[Block 238]
མིང་དང་མཚན་མ་དང་བརྡ་དང་། ཐ་སྙད་དང་། གདགས་པ་ཞེས་བྱ་བ་ཚིག་ལྔ་པོ་དག་གིས་ནི་ཀུན་བརྟགས་པ་བསྡུ་སྟེ། དཔེར་ན་བ་ལང་གི་རྫས་ལ་བ་ལང་ཞེས་བྱ་བ་ནི་མིང་ངོ་། །ལྐོག་ཤལ་དང་མཇུག་མ་ལ་སོགས་པ་ནི་མཚན་མའོ། །

[Block 239]
ཟལ་མོའི་བུ་དམར་མོའི་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བརྡའོ། །

[Block 240]
བ་ཁྲིད་དེ༌[^175]ཤོག་བ་ཞོས་ཤིག་ཅེས་བྱ་བ་ལ་སོགས་པ༌[^176]ནི་ཐ་སྙད་དོ། །

[Block 241]
བརྗོད་པ་ཐམས་ཅད་ནི་གདགས་པའོ། །

[Block 242]
སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་མེད་པ་དང༌[^177]ཞེས་བྱ་བ་ནི་ཚིག་ལྔ་པོ་དག་གིས་ཡོངས་སུ་གྲུབ་པ་བསྡུས་ཏེ། སྐྱེ་བ་མེད་པའི་ཕྱིར་མི་སྐྱེ་བའོ། །

[Block 243]
འགག་པ་མེད་པའི་ཕྱིར་མི་འགག་པའོ། །

[Block 244]
གོས་པ་མེད་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའོ། །

[Block 245]
རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར་རྣམ་པར་བྱང་བ་མེད་པའོ། །

[Block 246]
རྣམ་པར་དག་པའི་རྒྱུར་མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་ཕྱིར། མངོན་པར་འདུ་བྱ་བ་མེད་པའོ། །

[Block 247 [HEADING]]
#### ཐེག་པ་གང་དུ་གནས་པ། ^1-1-4-0

[Block 248]
ད་ནི་ཐེག་པ་གང་དུ་གནས་པར་འགྱུར་ཞེས་བྱ་བ་ནི༌[^178]ཞུས་པ་བཞི་པ༌[^179]བརྩམས་ཏེ། རབ་འབྱོར་ཐེག་པ་དེ་ནི་གང་དུ་ཡང་གནས་པར་འགྱུར་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ནམ་མཁའ་གང་ན་ཡང་མི་གནས་པ་དེ་བཞིན་དུ་ཐེག་པ་ཆེན་པོ་ཡང་མཐར་ཕྱིན་ཅིང་ཆོས་ཀྱི་སྐུའི་བདག་ཉིད་ཡིན་པས་གང་དུ་ཡང་གནས་པར་མི་འགྱུར་རོ། །

[Block 249]
[^180]ཐེག་པ་ཆེན་པོ་འབའ་ཞིག་གནས་པར་མི་འགྱུར་བར་མ་ཟད་ཀྱི། ཀུན་བརྟགས་པ་དང་། ཡོངས་སུ་གྲུབ་པའི་ཆོས་ཐམས་ཅད་ཀྱང༌[^181]གང་ན་ཡང་མི་གནས་སོ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 250]
ཆོས་ཐམས་ཅད་གནས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། ཀུན་བརྟགས་པ་ནི་མེད་པའི་ཕྱིར་གང་ན་ཡང་མི་གནས་སོ། །
--- END BLOCKS ---
