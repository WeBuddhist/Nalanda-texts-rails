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
[Block 2241]
མདོ་ལས་འཕགས་པའི་བདེན་པ་རྣམས་ཞེས་འབྱུང་བ་དེའི་དོན་ཅི་ཞེ་ན། འདི་དག་ནི་འཕགས་པ་རྣམས་ལ་བདེན་པས།

[Block 2242]
དེ་ལྟ་བས་ན་མདོ་ཁོ་ན་ལས།

[Block 2243]
འཕགས་པའི་བདེན་པ་རྣམས་ཞེས་བཤད་དོ། །ཅི་འདི་དག་གཞན་རྣམས་ལ་བརྫུན་ནམ་ཞེ་ན། འདི་དག་ནི་ཕྱིན་ཅི་མ་ལོག་པའི་ཕྱིར་ཐམས་ཅད་ལ་བདེན་ན་འཕགས་པ་རྣམས་ཀྱིས་ནི་འདི་དག་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་གཟིགས་ཀྱི་གཞན་དག་གིས་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་འདི་དག་ནི་འཕགས་པ་རྣམས་ཀྱི་བདེན་པ་ཞེས་བྱ་བའི་ཕྱིན་ཅི་ལོག་ཏུ་མཐོང་བའི་ཕྱིར་འཕགས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་མ་ཡིན་ཏེ།

[Block 2244]
ཚིགས་སུ་བཅད་པ་ལས།

[Block 2245 [VERSE]]
འཕགས་པས་བདེ་བར་གང་གསུངས་པ། །
དེ་ནི་གཞན་གྱིས་སྡུག་བསྔལ་རིག །
གཞན་གྱིས་བདེ་བར་གང་སྨྲས་པ། །
དེ་ནི་འཕགས་པས་སྡུག་བསྔལ་རིག །

[Block 2246]
ཅེས་འབྱུང་ངོ་། །གཞན་དག་ན་རེ་གཉིས་ནི་འཕགས་པ་རྣམས་ཀྱི་བདེན་པ་ཡིན་ལ། གཉིས་ནི་འཕགས་པ་ཡང་ཡིན་འཕགས་པ་རྣམས་ཀྱི་བདེན་པ་ཡང་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2247 [HEADING]]
##### སྡུག་བསྔལ་ཉིད་གསུམ། ^3-1-2-4-0

[Block 2248]
གང་གི་ཚེ་ཚོར་བའི་ཕྱོགས་གཅིག་སྡུག་བསྔལ་གྱི་རང་བཞིན་ཡིན་པ་དེའི་ཚེ་ཇི་ལྟར་ན་འདུ་བྱེད་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་སྡུག་བསྔལ་ཞེས་བརྗོད་ཅེ་ན།

[Block 2249 [VERSE]]
ཡིད་འོང་ཡིད་དུ་མི་འོང་དང་། །
དེ་ལས་གཞན་ཟག་བཅས་རྣམས༌[^1641]ཉིད། །
སྡུག་བསྔལ་ཉིད་གསུམ་ལྡན་པའི་ཕྱིར། །
ཅི་རིགས་མ་ལུས་སྡུག་བསྔལ་ལོ། །

[Block 2250]
སྡུག་བསྔལ་ཉིད་ནི་གསུམ་སྟེ། སྡུག་བསྔལ་གྱི་སྡུག་བསྔལ་ཉིད་དང་། འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་དང་། འགྱུར་བའི་སྡུག་བསྔལ་ཉིད་དོ། །

[Block 2251]
དེ་དག་གིས་ཅི་རིགས་པར་འདུ་བྱེད་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་མ་ལུས་པར་སྡུག་བསྔལ་བ་ཡིན་ཏེ། དེ་ལ༌[^1642]ཡིད་དུ་འོང་བ་རྣམས་ནི་འགྱུར་བའི་སྡུག་བསྔལ་གྱིས་སྡུག་བསྔལ༌[^1643]བ་ཉིད་དོ། །

[Block 2252]
ཡིད་དུ་མི་འོང་བ་རྣམས་ནི་སྡུག་བསྔལ་གྱིས་སྡུག་བསྔལ༌[^1644]བ་ཉིད་དོ། །

[Block 2253]
དེ་དག་ལས་གཞན་པ་རྣམས་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་གྱིས༌[^1645]སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 2254]
ཡིད་དུ་འོང་བ་ནི་གང་དག་ཡིན། ཡིད་དུ་མི་འོང་བ་ནི་གང་དག་ཡིན། གཉི་ག་མ་ཡིན་པ་ནི་གང་དག་ཡིན་ཞེ་ན། ཚོར་བ་གསུམ་དང་གོ་རིམས་བཞིན་ཏེ། དེའི་དབང་གིས་བདེ་བ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པའི་འདུ་བྱེད་རྣམས་ཀྱང་ཡིད་དུ་འོང་བ་ལ་སོགས་པའི་མིང་འཐོབ་པོ། །བདེ་བའི་ཚོར་བ་ནི་འགྱུར་བའི༌[^1646]སྡུག་བསྔལ་བ༌[^1647]ཉིད་དེ།

[Block 2255]
མདོ་ལས།

[Block 2256]
བདེ་བའི་ཚོར་བ་ནི་སྐྱེ་བ་ན་ཡང་བདེ། གནས་པ་ན་ཡང་བདེ་ལ། འགྱུར་བ་ན་སྡུག་བསྔལ་ལོ་ཞེས་གསུངས་སོ། །

[Block 2257]
སྡུག་བསྔལ་ནི་སྡུག་བསྔལ་གྱི་རང་གི་ངོ་བོ་ཁོ་ནས་སྡུག་བསྔལ་བ་ཉིད་དེ།

[Block 2258]
མདོ་ལས།

[Block 2259]
སྡུག་བསྔལ་གྱི་ཚོར་བ་ནི་སྐྱེ་བ་ན་ཡང་སྡུག་བསྔལ་ལ། གནས་པ་ན་ཡང་སྡུག་བསྔལ་ལོ་ཞེས་གསུངས་སོ། །

[Block 2260]
བདེ་བ་ཡང་མ་ཡིན། སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་ནི་རྐྱེན་གྱིས་མངོན་པར་འདུ་བྱེད་པའི་ཕྱིར་འདུ་བྱེད་ཁོ་ནས་སྡུག་བསྔལ་བ་ཉིད་དེ། གང་མི་རྟག་པ་དེ་ནི་སྡུག་བསྔལ་བ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །དེ་མྱོང་བར་འགྱུར་བའི་འདུ་བྱེད་རྣམས་ཀྱང་ཚོར་བ་དང་འདྲ་བར་བརྗོད་དོ། །

[Block 2261]
གཞན་དག་ན་རེ་སྡུག་བསྔལ་ཉིད་སྡུག་བསྔལ་ཉིད་ཡིན་པས་སྡུག་བསྔལ་གྱི་སྡུག་བསྔལ་ཉིད་ཡིན་ལ། འདུ་བྱེད་ཉིད་སྡུག་བསྔལ་ཡིན་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ། །

[Block 2262]
འགྱུར་བ་ཡང་སྡུག་བསྔལ་གྱི་སྡུག་བསྔལ་དག་ནི་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བ་རྣམས་ཀྱི་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་བཤད་དོ། །

[Block 2263]
འདུ་བྱེད་ཐམས་ཅད་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་ཀྱིས་སྡུག་བསྔལ་བ་ཉིད་ལ་དེ་དག་ཀྱང་འཕགས་པ་རྣམས་ཁོ་ནས་གཟིགས་སོ། །

[Block 2264]
འདིར་སྨྲས་པ།

[Block 2265 [VERSE]]
ལག་མཐིལ་སྤུ་ཉག་གཅིག་འདུག་པ། །
མི་རྣམས་ཀྱིས་ནི་མི་རྟོགས་ལ། །
དེ་ཉིད་མིག་ཏུ་སོང་ན་ནི། །
མི་བདེ་བ་དང་གནོད་སྐྱེད༌[^1648]ལྟར། །

[Block 2266 [VERSE]]
བྱིས་པ་ལག་མཐིལ་འདྲ་བ་ཡིས། །
འདུ་བྱེད་སྡུག་བསྔལ་སྤུ་མི་རྟོགས། །
འཕགས་པ་མིག་དང་འདྲ་བ་ནི། །
དེ་ཡིས་ཤིན་ཏུ་ཡིད་ཀྱང་འབྱུང་། །

[Block 2267]
ཇི་ལྟར་འཕགས་པ་རྣམས་སྲིད་པའི་རྩེ་མོ༌[^1649]བ་དག་ལ་ཡང༌[^1650]སྡུག་བསྔལ་གྱི་བློ་འཇུག་པ་ལྟར་བྱིས་པ་རྣམས་ནི་མནར་མེད་པའི་ཕུང་པོ་རྣམས་ལ་ཡང་དེ་ལྟར་སྡུག་བསྔལ་གྱི་བློ་མི་འཇུག་གོ། །

[Block 2268]
དེ་ལྟ༌[^1651]ན་འོ་ན་ནི་ལམ་ཡང་འདུས་བྱས་ཡིན་པའི་ཕྱིར་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། སྡུག་བསྔལ་ཞེས་བྱ་བའི་མཚན་ཉིད་ནི་མི་མཐུན་པ་ཡིན་པའི་ཕྱིར་ལམ་ནི་སྡུག་བསྔལ་བ་མ་ཡིན་ཏེ། དེ་སྐྱེ་བ་ནི༌[^1652]སྡུག་བསྔལ་ཐམས་ཅད་ཟད་པ་འདྲེན་པའི༌[^1653]འཕགས་པ་རྣམས་དང་མི་མཐུན་པ་མེད་དོ། །

[Block 2269]
གང་གི་ཚེ་དེ་དག་མྱ་ངན་ལས་འདས་པ་ལ་ཞི་བར་ལྟ་བ་དེའི་ཚེ་ཡང་། སྡུག་བསྔལ་དུ་མཐོང་བ་གང་ཡིན་པ་དེ་ཁོ་ནའི་འགོག་པ་ལ་ཞི་བར་ལྟའོ། །

[Block 2270]
གང་གི་ཚེ་འདི་དག༌[^1654]ལ་བདེ་བ་ཡང་ཡོད་པ་དེའི་ཚེ་ཅིའི་ཕྱིར་སྡུག་བསྔལ་ཁོ་ན་འཕགས་པའི་བདེན་པ་ཞེས་བྱ་ཞེ་ན། ཁ་ཅིག་ན་རེ་བདེ་བ་མྱོང་བའི་ཕྱིར་ཏེ། མོན་སྲན་སྡེའུ་ལ་སོགས་པ་ཡོད་བཞིན་དུ་མོན་སྲན་གྲེའུའི༌[^1655]ཕུང་པོ་ཞེས་སྟོན་པ༌[^1656]བཞིན་ཏེ། མཁས་པ་སུ་ཞིག་ཆུས་བཏབ་པའི་བདེ་བ་ཆུང་ངུས་འབྲས་བུ་བདེ་བ་ཡིན་ནོ་སྙམ་དུ་སེམས་པར་འགྱུར། ཡང་སྨྲས་པ།

[Block 2271 [VERSE]]
སྡུག་བསྔལ་གྱི་ནི་རྒྱུ་ཕྱིར་དང་། །
སྡུག་བསྔལ་མང་པོས་བསྐྱེད་ཕྱིར་དང་།
སྡུག་བསྔལ་ཡོད་ན་བདེ་འདོད་ཕྱིར། །
བདེ་བ་སྡུག་བསྔལ་ཞེས་རྟོག་གོ། །

[Block 2272]
[^1657]སྲིད་པ་ཐམས་ཅད་ནི་བདེ་བ་དང་བཅས་ཏེ་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་དུ་རོ་གཅིག་པའི༌[^1658]འཕགས་པ་རྣམས་ཀྱིས་སྡུག་བསྔལ་དུ་གཟིགས་ཏེ། དེའི་ཕྱིར་སྡུག་བསྔལ་ཁོ་ན་འཕགས་པའི་བདེན་པར་རྣམ་པར་གཞག༌[^1659]གི་བདེན་པ༌[^1660]ནི་མ་ཡིན་ནོ། །

[Block 2273]
ད་ནི་ཇི་ལྟར་བདེ་བའི་རང་བཞིན་གྱི་ཚོར་བ་རྣམས་ལ་སྡུག་བསྔལ་དུ་ལྟ་ཞེ་ན། མི་རྟག་པའི་མཚན་ཉིད་ཀྱིས་མི་མཐུན་པའི་ཕྱིར་ཏེ། དཔེར་ན་གཟུགས་དང་འདུ་ཤེས་ལ་སོགས་པ་ལ་ཡང་སྡུག་བསྔལ་དུ་ལྟ༌[^1661]མོད་ཀྱི། དེ་དག་ཇི་ལྟར་སྡུག་བསྔལ་གྱི་ཚོར་བ་བཞིན་དུ་སྡུག་བསྔལ་བ་ནི་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2274]
གང་ཞིག་སྡུག་བསྔལ་གྱི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ་སྙམ་དུ་སེམས་པ་དེའི་དེ་ནི་ཀུན་འབྱུང་གི་རྣམ་པ་ཡིན་གྱི་སྡུག་བསྔལ་གྱི་རྣམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2275]
གཟུགས་དང་གཟུགས་མེད་པར་སྐྱེས་པ་དག་གིས་འཕགས་པ་རྣམས་ལ་ཡང་ཇི་ལྟར་སྡུག་བསྔལ་གྱི་འདུ་ཤེས་འཇུག་པར་འགྱུར་ཏེ། དེ་དག་གི་ཕུང་པོ་རྣམས་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 2276]
མདོ་ལས་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་ཀྱང་ཅིའི་ཕྱིར་གསུངས་པར་གྱུར། གལ་ཏེ་མི་རྟག་པའི་ཕྱིར་སྡུག་བསྔལ་ཉིད་དུ་ལྟ་ན་འོ་ན་མི་རྟག་པ་དང་སྡུག་བསྔལ་གྱི་རྣམ་པ་དག་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། སྐྱེ་ཞིང་འཇིག་པའི་ཆོས་ཅན་ཡིན་པའི་ཕྱིར་མི་རྟག་པར༌[^1662]ལྟ་ལ། མི་མཐུན་པ་ཡིན་པའི་ཕྱིར་སྡུག་བསྔལ་དུ་ལྟ༌[^1663]སྟེ། མི་རྟག་པར་མཐོང་ན་མི་མཐུན་པར་འགྱུར་བས་མི་རྟག་པའི་རྣམ་པས་སྡུག་བསྔལ་གྱི་རྣམ་པ་འདྲེན་པར་བྱེད་དོ། །

[Block 2277 [HEADING]]
##### བདེ་བའི་ཚོར་བ་ཡོད་པ། ^3-1-2-5-0

[Block 2278]
ཁ་ཅིག་ན་རེ་བདེ་བའི་ཚོར་བ་ཞེས་བྱ་བ་ནི་མེད་པ་ཉིད་དེ། ཐམས་ཅད་སྡུག་བསྔལ་ཁོ་ན་ཡིན་ནོ། །

[Block 2279]
འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། མདོ་དང་། རིགས་པ་ལས་ཏེ། རེ་ཞིག་མདོ་ལས་ཇི་ལྟ་བུ་ཞེ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་གང་ཅི་ཚོར་ཡང་རུང་དེ་ནི་འདིར་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བ་དང་། བདེ་བའི་ཚོར་བ་ནི་སྡུག་བསྔལ་དུ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་དང་། སྡུག་བསྔལ་ལ་བདེ་བའོ་སྙམ་དུ་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་གོ་ཞེས་གསུངས་ཏེ། རེ་ཞིག་མདོ་ལས་ནི་དེ་ལྟ་བུའོ། །

[Block 2280]
རིགས་པ་ལས་ཇི་ལྟ་བུ་ཞེ་ན། བདེ་བའི་རྒྱུ་རྣམ་པར་མི་གནས་པའི་ཕྱིར་ཏེ། ཁ་ཅིག་བདེ་བའི་རྒྱུ་བཏུང་བ་དང་བཟའ་བ་དང་གྲང་བ་དང་དྲོ་བ་ལ་སོགས་པར་འདོད་པ་གང་དག་ཡིན་པ་དེ་དག་ཁོ་ན་ཧ་ཅང་སྤྱད་པ་དང་། དུས་མ་ཡིན་པར་སྤྱད་པ་རྣམས་ཀྱང་སྡུག་བསྔལ་གྱི་རྒྱུ་དག་ཏུ་འགྱུར་རོ། །
--- END BLOCKS ---
