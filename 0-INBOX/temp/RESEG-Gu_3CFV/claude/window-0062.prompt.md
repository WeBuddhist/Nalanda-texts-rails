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
[Block 2171]
ཁབ་རལ་འཆོས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2172]
རྐང་པ༌[^1377]དམའ་བ་དང་ལྡན་པའི་ཁྲི་ལ་ཉལ་བར་མི་བྱ་བའོ༌[^1378]ཞེས་བྱ་བ་ནི། གང་ཞིག་འབྱུང་བར་འགྱུར༌[^1379]བའི་མགོ་བོ་ལ་ཉེས༌[^1380]པར་འགྱུར་བ་དེ་ལྟ་བུའི་ས་དང་གང་ལ་འཁྱིལ་བ་མ་བཅགས་པར༌[^1381]སྦྲུལ་གྱིས་སོས༌[^1382]བཏབ་པ་བསྒྲུབ་པ་མི་འབྱུང་བ་དེ་ལྟ་བུའི༌[^1383]ས་ལ་ཞེས་བྱ་བ་གླེང་གཞི་ལས་རྟོགས་པར་བྱའོ། །

[Block 2173]
མལ་དང་འབྲེལ་པའི་ཁྲིའི་ཉེ་འཁོར་གྱི་ཕྱོགས་སུ་རྐང་པ་བཀྲུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉལ་བའི་གནས་དང་འབྲེལ་པའི་ཁྲིའི་ཉེན་ཀོར༌[^1384]དང་འབྲེལ་པའི་ཕྱོགས་སུ་རྐང་པ་བཀྲུ་བར་མི་བྱའོ། །

[Block 2174]
ཁྱིམ་པའི་གནས་མལ་གྱི་གནས་གཞན་དང་འབྲེལ་པ་ཉིད་ལ་འདི་དང་མི་མཐུན་པ་སྟེ། དེ་བས་ན་དེ་ལས་ཡང་ཉེས་པ་འདིའོ། །

[Block 2175]
ཁྱིམ་པའི་གནས་མལ༌[^1385]ཉིད་ལ་འདི་ནི་ཤིན་ཏུ་ན་སྨད་པར་རིག་པར་བྱའོ། །ཅི་ཐམས་ཅད་ཀྱིས་བཀྲུ་བར་མི་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་ལྷམ་ཡོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2176]
ཅི་འདིར་ཕྱོགས་ཐམས་ཅད་དུ་གཞན་ལ་བཀྲུ་བར་བྱ་བ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱིས་ནི་མགོ་ལོགས་དང་རྐང་ལོགས་མ་གཏོགས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཀྲུ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2177]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་གང་དག་ལ་མཆིལ་ལྷམ་མི་བདོག་པ༌[^1386]དེ་དག་གིས་མགོ་ལོགས་སམ་རྐང་ལོགས་སུ་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2178]
རིགས་པ་ཡང་དེ་ལྟར་ཁོ་ན་སྟེ། འདི་ནི་མི་མཐུན་པ་ཞེས་བྱ་བ༌[^1387]འདིས་སྤང་བའོ། །

[Block 2179]
སྦྲུལ་ལ་སོགས་པ་གནས་པའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2180]
འདིར་འཇུག་པ་ཙམ་ནི་གླེང་གཞི་ལས་གཙོ་བོ་སྟེ། ཉེས་དམིགས་ནི་མ་ཡིན་ནོ། །

[Block 2181]
འདི་ནི་མི་བྱ་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་འཇུག་པ་བརྟེན་པ་མ་གསུངས་སོ། །

[Block 2182]
ཉེས་དམིགས་བྱེད་པ་ཉིད་ཀྱིས་ལྟུང་བ་དང་། ཁྲུས་ལ་སོགས་པ་ལ་ཡང་དག་པར་བྱ་བ་ཉིད་དུ་ཐལ་བའི་ཕྱིར་རོ། །

[Block 2183]
མགོ་ལོགས་སམ་རྐང་ལོགས་སུ་འདི་ལ་ཤིན་ཏུ་ཡང་མི་མཐུན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2184]
མལ་སྟན་མཐོན་པོ་དང་། མལ་སྟན་ཆེན་པོ་ལ་འདུག་པ་འམ་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མལ་སྟན་ཆེན་པོ་ནི་གསེར་ལ་སོགས་པ་རིན་པོ་ཆེ་དང་དངུལ་གྱི་རང་བཞིན་ཉིད་དོ། །

[Block 2185]
འདོད་བསླབ་པའི་གཞི་གང་ཞིག་ལས་ཚད་ལས་ལྷག་པ་ཉིད་ཀྱི་རྐང་པ་རྣམས་བསྒྲུབ་པར་མི་བྱའོ་ཞེས་གསུངས་ཏེ། འདི་ནི་མཐོན་པོའི་ངོ་བོ་ཉིད་དོ། །

[Block 2186]
དེ་བས་ན་མལ་སྟན་མཐོན་པོ་ཞེས་བྱ་བ་ནི། རྩ་བ་བུ་གར་གཞུག་པ་མ་གཏོགས་པར་གནང་བར༌[^1388]འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ལ་ཁྲུ་གང་ལས་ལྷག་པའོ། །

[Block 2187]
དེ་ལྟར་ཡང་གཞན་དུ་རྩ་བའི་བུ་གར་ཞེས་སྨོས་པས༌[^1389]སོ། །

[Block 2188]
ཁྲི་དང་ཁྲིའུའི་ལྟུང་བྱེད་ཀྱི་ཞུ་བ་ལས་སོར་བརྒྱད་ཀྱི་ཚད་ལས་ལྷག་པར་གནས་མལ་དེ་ཡོད་པ་ཡིན་ཏེ། དེ་དགེ་སློང་གིས་གདོན་པར་མ་བྱས་པར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 2189]
མི་རུང་བ་ཉིད་ཀྱི་ཕྱིར་ན་སྨད་པ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2190]
སོར་བརྒྱད་ཀྱིས་ལྷག་པ་ཉིད་ནི་མི་རུང་བ་ཉིད་དོ། །

[Block 2191]
འདིར་མལ་སྟན་ཞེས་སྨོས་པས་སྟན་ཡང་འཕངས་པར་རིག་པར་བྱ་སྟེ། འདུག་པ་བཀག་པར་གཏོགས་པའོ། །

[Block 2192]
ཁྱིམ་གཞན་དུ་གཞན་མེད་ན་སྔ་མ་ཤོས་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་དུ་མི་མཐོ༌[^1390]དང་མི་ཆེ་བ་མེད་ན་ཁྱིམ་གྱི་ནང་དུ་བྱའོ། །

[Block 2193]
མལ༌[^1391]སྟན་མཐོན་པོ་དང་། མལ་སྟན་ཆེན་པོ་སྔ༌[^1392]མ་ཤོས་བྱ་སྟེ། ཀུན་དགའ་བོ་དེ་དག་ཐམས་ཅད་དུ་འབྱོར་པར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2194]
རྐང་རྟེན་དང་བཅས་པ་ལ་མལ་བཅའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཕྱོགས་གཅིག་མཐོ་བ༌[^1393]ཉིད་ཀྱིས་ནི་མལ་སྟན་མཐོན་པོ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2195]
དེ་བས་ན་རྐང་རྟེན་དང་པོའི་ཆོ་ག་འདི་སྟོན་པར་བྱེད་པ་མཐོན་པོ་བཀག་པ་ལ་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ཏེ། དེ་བསྡུ་བར་བྱ་ཞིང་བཀག་པ་འདིར་རྟོགས་པར་བྱའོ། །

[Block 2196]
རྐང་རྟེན་དང་བཅས་པ་ལ་ཉོལ་ཅིག་ཅེས་བྱ་བ་ཅིའི་ཕྱིར་མ་གསུངས།

[Block 2197]
ཉལ་བའི་དོན་ཅན་མ་ཡིན་པའི་སྒྲ་ལ་ཡང་ཁོངས་སུ་གཏོགས་པར་བསྡུ་བའི་དོན་དུ། ཕྲན་ཚེགས་རྣམས་ལས་འདི་གསུངས་སོ། །

[Block 2198]
ཁྲི་རྩེག་མའི་སྟེང་དུ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་སྨན་གྱི་གཞི་ལས་བཤད་པ་ཡིན་ཏེ། ཐུན་མོང་བའི་མཐོན་པོ་ཉིད་ཀྱིས༌[^1394]དེ་འདིར་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 2199]
ཁྲི་རྩེག་མ་ཞེས་བྱ་བ་ནི་ཁྲིའི་སྟེང་དུ་ཁྲི་བཞག་པའོ། །

[Block 2200]
གང་ལ་ཁྲིའི་རྐང་པ་འཆོས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པའི་གཞི་གཞན་རྣམས་ལ་དོན་འདི་ཡོངས་སུ་ཐོབ་པ་ཡིན་ཏེ། གཉིས་པའི་འོག་མ་གསུམ་པོ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་གང་ཞིག༌[^1395]འདིར་བསླབ་པའི་གཞི་འདིའི་འོག་མ་གཉིས་པ་ཤིང་བལ་གྱིས་གོས་པར་བྱ་བ༌[^1396]དགག་པ་ཞེས་བྱ་བའི་བསླབ་པའི་གཞིའོ། །

[Block 2201]
དེའི་འོག་མ་གསུམ་པོ་དེ་དག་ཅེས་བྱ་བ་ནི་གདིང་བ་ལས་གྱུར་པ་དང་། གཡན་པ་དགབ་པ་ལས་གྱུར་པ་དང་དབྱར་གྱི་རས་ཆེན་ལས་གྱུར་པ་ཞེས་བྱ་བ་རྣམས་ཏེ་བསླབ་པའི་གཞི་དེ་གསུམ་ལ་ཡང་ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལས་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ་འདི་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལ་ཞེ་ན། རྐང་པ་དག་གིའོ་ཞེས་བྱ་བ་འོག་ནས་འབྱུང་ངོ་། །གང་གི་རྐང་པ་དག་ཅེ་ན། དེའི་ཕྱིར་ཁྲིའམ་ཁྲིའུ་དག་གིའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ཐམས་ཅད་ཀྱིས་སམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁ་ན་མ་ཐོ་བ་འདི་ལ་དེ་བསྒྲུབ་པར་གྱུར་པའི་མཐར་ཐུག་པ་སྟེ། གང་ཞིག་དགེ་འདུན་མ་ལོག་པའི་ལམ་ལ་བརྟག་པ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 2202]
འོག་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་འདི་འོག་མ་ཤིང་བལ་གྱིས་གོས་པར་བྱས་པ་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་ལ་ཡང་ཁྲིའམ་ཁྲིའུ་དག་ལའོ། །

[Block 2203]
དགེ་འདུན་གྱིའོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2204]
དགེ་འདུན་གྱི་དོན་དུ་འདི་ལ་ལོག་པར་རྟོགས་པ་ལ་བསྒྲུབ་པར་གྱུར་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་ཡང་དགེ་འདུན་དག་གི་ཞེས་བྱ་བས་ཤེས་པའོ། །

[Block 2205]
གང་གི་ཆད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལ་ནི་ཁྲིའི་རྐང་པ་འཆོས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྐང་པ་དག་གིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་སྙེད་པ་རྣམས་ཀྱིས་ཁྲིའམ་ཁྲིའུ་དེའི་གནས་སྐབས་བསྒྲུབ་པ་ནི། དཔེར་ན་དཔུང་གི་ཚོགས་ཡན་ལག་བཞི་ལྟ་བུའམ་བཞི་ཡིས་གཉིས་སམ་གསུམ་གྱིས་འགྲུབ་པ་འདི་དཔེར་ན་ཤིང་གི་ཁྲིའུ་གཅིག༌[^1397]ལྟ་བུ་སྟེ། དེ་སྙེད་ཅེས་བྱ་བ་ནི་ཤུགས་ཀྱིས་ཁོངས་སུ་ཆུད་པར་བྱའོ། །

[Block 2206]
གཞན་གྱིས་ནི་དེ་དག་ངེས་པར་སྦྱར་བ་གཅིག་གམ་དུ་མར་བྱས་པ་ལ་ལྷག་མ་སྒྲུབ་པར་བྱེད་ཅིང་ཉེས་བྱས་སོ་ཞེས་བྱ་བའོ། །

[Block 2207]
ཁང་པའམ་གཙུག་ལག་ཁང་དང་གདིང་བ་རྣམས་ལས་བརྩམས་པ་མཐར་བྱས་པ་ལ་ན་སྨད་པའི་ཚིག་གིས་རིག་པར་བྱའོ། །

[Block 2208]
ཅི་སླར་རྐང་པ་དེ་དག་གི་ཚད་གང་ཡིན་པ་གང་གིས་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ལྟུང་བྱེད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་གི་ཆད་ནི་བུ་གར་གཞུག་པའི་ཕྱོགས་མ་གཏོགས་པར་ཁྲུ་གང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུ་གར་གཞུག་པ་ཞེས་བྱ་བའི་ཕྱོགས་དག་མ་གཏོགས་པར་ལྷག་མ་འདི་རྣམས་ཀྱི་ཚད་ཁྲུ་གང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2209]
གལ་ཏེ་གང་ཡོད་ན་འདི་ལ་གང་ཡོད་པར་གྱུར་ན་འདི་གལ་ཏེ་གང་ལས་གཏོགས་པའི་ཕྱོགས་ལས་བརྩམས་ཏེ། ཆ་ཕྱེད་ལ་བུ་གར་གཞུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2210]
ཁྲུ་ཅི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བར་གཤེགས་པའི་སུམ་ཆས་སོ་ཞེས་བྱ་བ༌[^1398]སྨོས་ཏེ། བདེ་བར་གཤེགས་པའི་ཁྲུའི་སུམ་ཆར་གྱུར་པས་ཀྱང་ངོ་། །བསླབ་པའི་གཞི་རྣམས་ལ་བདེ་བར་གཤེགས་པའི་ཁྲུ་ཆ་གསུམ་དུ་གྱུར་པའི་ཁྲུ་ཚད་ཀྱི་རྣམ་པར་གཞག་པ་དེ་བས་ན་འདི་ལྟར་འདི་ལ་དེ་རྣམས་ལ་འབྲེལ་པ༌[^1399]རྣམ་པར་གཞག་པས་རྟོགས་པའོ། །
--- END BLOCKS ---
