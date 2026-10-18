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
དེ་དག་དང་འདྲེས་པའི་ཕྱིར། འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་ཡང་ཡོད་པ་ལ་ནི་སྒྲིབ་པོ། །མེད་པ་ལ་ནི་འཛིན་ཏོ། །

[Block 2242]
དེ་དག་གིས་བསྐྱེད་པའི་ཕྱིར། བསོད་ནམས་དང་། བསོད་ནམས་མ་ཡིན་པ་ལ་སོགས་པའི་ལས་བྱེད་པའི་སེམས་པ་ཡང་། ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པ་ཡིན་ཏེ་ལས་དེ་དང་རྣམ་པར་རྟོག་པ་དེ་དག་གིས་བསྐྱེད་པའི་ཕྱིར། རྣམ་པར་སྨིན་པའི་ཤེས་པ་ཡང་དེ་ཁོ་ན་ཉིད་འཛིན་པ་མ་ཡིན་ནོ། །

[Block 2243]
དེ་བས་ན་འདུན་པ་དང་། འདོད་ཆགས་ལ་སོགས་པ་ཡང་དེ་ཁོ་ན་མ་ཡིན་པའི་ཡུལ་ཅན་ཏེ། ཀུན་འབྱུང་བ་ཐམས་ཅད་ནི་ཡང་དག་པའི་ངོ་བོ་ཉིད༌[^1566]མ་ཡིན་ནོ། །

[Block 2244]
སེམས་ཅན་དམྱལ་བ་དང་། དུད་འགྲོ་དང་། ཡི་དགས་དང་། ལྷ་དང་མིའི་འགྲོ་བ་རྣམས་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ལྔ་པོ་དག་དེ་ཁོ་ནའི་ངོ་བོ་ཉིད་དུ༌[^1567]སྟོན་ཏེ། དེའི་ཕྱིར་ཆོས་རྣམས་རྣམ་པར་མི་རྟོག་པ་ཡིན་ཡང་དེ་ལྟར་འཁོར་བར༌[^1568]རྣམ་པར་གཞག་གོ། །

[Block 2245]
རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ལ་ཡང་། རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་རྣམ་པར་གཞག་ཅིང་། ཐམས་ཅད་ཀྱང་རྣམ་པར་མི་རྟོག་པ་ཉིད་དེ། རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་ནས། དེ་བཞིན་གཤེགས་པའི་བར་དུ་ངོ་བོ་ཉིད་ཀྱིས་ཐ་དད་པ་ནི་གང་ཡང་མེད་དེ། ཐམས་ཅད་ཀྱང་ཆོས་ཀྱི་སྐུ་ལས་མ་འདས་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པའོ། །

[Block 2246 [HEADING]]
##### སྙིང་པོ་མེད་པ་ལ་སྤྱོད་པ། ^1-2-7-21-0

[Block 2247]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཆོས་ཉིད་ཐོས་པས་ཤཱ་རིའི་བུའི་བློ་རྒྱ་ཆེར་གྱུར་ནས། ཀྱེ་མ་བྱང་ཆུབ་སེམས་དཔའ་གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་དེ་ནི་སྙིང་པོ་ལ་སྤྱོད་པའོ་ཞེས་གསུངས་པ་དང་། དེ་ནས་རབ་འབྱོར་གྱིས་སྙིང་པོ་མེད་པ་ལ་སྤྱོད་པའོ་ཞེས་གསུངས་ཏེ། དངོས་པོ་མེད་པ་དང་། ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་སྙིང་པོ་མེད་པ་ཉིད་ཡིན་པར་དེའི་ཡིད་ལ་བཞག་ནས། སྙིང་པོ་མེད་པ་ཉིད་ཀྱང་མི་དམིགས་ན་སྙིང་པོ་དམིགས་པ་ལྟ་ག་ལ་ཡོད་ཅེས་འཇིག་རྟེན་པའི་རིགས་པ་གསུངས་ཏེ། འཇིག་རྟེན་ན་ཡང་སྙིང་པོ་མེད་པ་ནི་རྙེད་སླའོ། །

[Block 2248]
[^1569]སྙིང་པོ་ཅན་ནི་རྙེད་པར་དཀའོ་ཞེས་ཐ་སྙད་དུ་བྱེད་དོ། །

[Block 2249]
གང་དག་ཆོས་འདི་དག་མཉམ་པ་ཉིད་དུ་མངོན་སུམ་དུ་མི་བྱེད་པ་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་དང་། དེ་བཞིན་གཤེགས་པ་མཉམ་པ་ཉིད་དང་། ཆོས་ཀྱི་སྐུ་དང་ཡང་དག་པའི་མཐའ་ཡང་མཉམ་པ་ཉིད་དོ། །

[Block 2250]
ནམ་མཁའ་དབེན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་དབེན་པའི་རྣམ་པས་སོ། །

[Block 2251]
འདི་ཡང་འགྲེས་གསུམ༌[^1570]སྟེ། ནམ་མཁའ་དང་སེམས་ཅན་མཐུན་པའི་འགྲེས་དང་། ནམ་མཁའ་ལྟ་བུའི་སེམས་ཅན་གྱི་གོ་ཆའི་འགྲེས་དང་། གཟུགས་ལ་སོགས་པ་དང་། སེམས་ཅན་མཐུན་པའི་འགྲེས་སོ། །

[Block 2252]
དབེན་པ་བཤད་པ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཕན་ཡོན་ཡང་གོ་སླའོ། །

[Block 2253 [HEADING]]
##### དེ་བཞིན་ཉིད་དུ་གནས་པ། ^1-2-7-22-0

[Block 2254]
བཅོམ་ལྡན་འདས་གང་ཡང༌[^1571]དེ་བཞིན་ཉིད་དུ་གནས་ཤིང༌[^1572]དེ་བཞིན་ཉིད་དུ་ནན་ཏན་བགྱིས་ཏེ། ཆོས་གང་ཡང་མི་དམིགས་ན་དེ་ཇི་ལྟར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་གནས་པར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ལ་གནས་པ་དང་། སྒྲུབ་པ་ཆོས་འགའ་ཞིག་ཡོད་ན་ནི་རིགས་ན། གལ་ཏེ་ཆོས་ཐམས་ཅད་མི་དམིགས་ན་ཇི་ལྟར་གནས་པར་འགྱུར་ཞེས་དྲིས་པའོ། །

[Block 2255]
རབ་འབྱོར་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ཇི་ལྟ་བ་བཞིན་དུ་གནས་སོ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་བྱ་བ་ཐམས་ཅད་བྱེད་ཅིང་གནས་པ་དེ་བཞིན་དུ། བྱང་ཆུབ་སེམས་དཔའ་ཡང་གནས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2256]
བཅོམ་ལྡན་འདས༌[^1573]གང་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ཞེས་བགྱི་བའི༌[^1574]ཆོས་གང་ཡང་མི་དམིགས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས། འདི་སྐད་དུ་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ཞེས་བྱ་བའི་ཆོས་གང་ཡང་མེད་དེ། དེ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བཞིན་ཉིད་ལ་གནས་པ་དང་། སྒྲུབ་པ་དང་། མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། ཆོས་བསྟན་པ་ཡང་མེད་ལ། བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད༌[^1575]ནི་ཡོད་དོ་ཞེས་བྱ་བ་ཇི་ལྟར་རིགས་པར༌[^1576]འགྱུར་ཞེས་བསྟན་པའོ། །

[Block 2257]
དེ་བཞིན་ཉིད་ཀྱང་མི་དམིགས་ན། གང་དེ་བཞིན་ཉིད་ལ་གནས་པར་འགྱུར་བ་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བ་འདིས་ཀྱང་མི་རིགས་པ་གཞན་དག་སྟོན་ཏོ། །

[Block 2258]
དེ་བཞིན་ཉིད་ཀྱང་དྲི་མ་དང་བཅས་པའི་གནས་སྐབས་ན་ཀུན་བརྟགས་པ་དང་མཚུངས་པའི་ཕྱིར་དེ་སྐད་བཤད་དོ། །

[Block 2259]
[^1577]དེའི་ཚེ་དེ་བཞིན་ཉིད་ཀྱང་དེ་བཞིན་ཉིད་ཀྱི་བདག་ཉིད་དུ་མི་དམིགས་སོ། །

[Block 2260]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་རབ་འབྱོར་དེ་དེ་བཞིན་ནོ་དེ་དེ་བཞིན་ཏེ་ཞེས༌[^1578]བཀའ་སྩལ་པའི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། གལ་ཏེ་ཁ་ཅིག་དམིགས་ལ། ཁ་ཅིག་མི་དམིགས་ན་ནི་ཀླན་ཀར་ཡང་འགྱུར་ན། འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། བྱང་ཆུབ་དང་། གནས་པ་དང་། སྒྲུབ་པ་ཐམས་ཅད་མེད་ན་དེ་ལ་ཀླན་ཀར་འགྱུར་བ་ཅི་ཞིག་ཡོད་ཅེས་གསུངས་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། རབ་འབྱོར་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་། མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཅེས་བྱ་བ་གནས་པ་ཡིན་པའི་ཕྱིར་དེ་དུས་ཐམས་ཅད་དུ་ཡོད་དེ། དེའི་ཕྱིར་གནས་པ་ཞེས་བྱ་བ་དང་། སྒྲུབ་པ་ཞེས་བྱ་བ་གང་ཡང་མེད༌[^1579]དེ། དེ་བཞིན་ཉིད་ལ་ནི་གནས་པ་དང་། སྒྲུབ་པ་དང་། མངོན་པར་རྫོགས་པར༌[^1580]བྱང་ཆུབ་པར་བྱེད་པ་གང་ཡང་མེད་དོ་ཞེས་སྟོན་ཏོ། །

[Block 2261 [HEADING]]
##### རབ་འབྱོར་ལ་བསྟོད་པ་ལ་སོགས་པ། ^1-2-7-23-0

[Block 2262]
དེའི་འོག་ཏུ་རབ་འབྱོར་ལ་བསྟོད་པ་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་བསྟོད་པ་དང་། ལྷ་རྣམས་ཀྱིས་མཆོད་པ་དང་། དགེ་སློང་དྲུག་སྟོང་གི་གཏམ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཕན་ཡོན་དང་། ཀུན་དགའ་བོ་ལ་ཡོངས་སུ་གཏད་པ་དང་། རྫུ་འཕྲུལ་མངོན་པར་འདུ་མཛད་པ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བསླབ་པ་དང་། རབ་ཏུ་བསྔགས་པ་དང་། མི་ཟད་པའི་གཏམ་མོ། ཀུན་དགའ་བོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ནི་ཡི་གེ་ཐམས་ཅད་ལ་འཇུག་གོ། །

[Block 2263]
ཡི་གེ་མེད་པ་ཐམས་ཅད་ལ་འཇུག་གོ། །

[Block 2264]
ཀུན་དགའ་བོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ནི་གཟུངས༌[^1581]ཀྱི་སྒོ་གང་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་བསླབ་པར་བྱ་བའི་གཟུངས་ཐམས་ཅད་ཀྱི་སྒོ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་གང་དག༌[^1582]ཡི་གེར་གཏོགས་པའི་དྲན་པ་དང་། ཤེས་རབ་དང་། ཏིང་ངེ་འཛིན་དེ་དག་ལ་འཇུག་པར་འགྱུར་བ༌[^1583]དང་། གང་དག་གི༌[^1584]ཡི་གེར་མ་གཏོགས་པའི་དྲན་པ་དང་། ཤེས་རབ་དང་། ཏིང་ངེ་འཛིན་དེ་དག་ལ་འཇུག་པར་འགྱུར་བ༌[^1585]དང་། གང་ཡང་ཆོས་ཀྱི་གཟུངས་དང་། དོན་གྱི་གཟུངས་དང་། [^1586]བཟོད་པའི་གཟུངས་དང་། སྔགས་ཀྱི་གཟུངས་དེ་དག་གི་སྒོར་གྱུར་པའོ། །

[Block 2265 [HEADING]]
##### མི་ཟད་པ་ཉིད་ལ་དམིགས་ནས་ཤེས་རབ་བསྐྱེད་པ། ^1-2-7-24-0

[Block 2266]
རབ་འབྱོར་གཟུགས་མི༌[^1587]ཟད་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མངོན་པར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱི་མི་ཟད་པ་ཉིད་ལ་དམིགས་ནས་ཤེས་རབ་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2267]
རབ་འབྱོར་གཞན་ཡང་གཟུགས་དང་ནམ་མཁའ་ཟད་མི་ཤེས་པས་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པའི་དེ་བཞིན་ཉིད་དང་། ནམ་མཁའ་ལ་དམིགས་ནས་ཡང་དེ་དག་མི་ཟད་པ་ཉིད་དུ་ཤེས་རབ་བསྐྱེད་པར་བྱའོ། །

[Block 2268]
དེའི་འོག་ཏུ་ནམ་མཁའ་ལྟར་ཟད་མི་ཤེས་པ་བསྒོམས་པའི༌[^1588]ཕན་ཡོན་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་རེ་རེ་ལ་སྦྱར་བས༌[^1589]ནི་གོ་སླའོ། །

[Block 2269]
ནང་སྟོང་པ་ཉིད་ལ་ནང༌[^1590]སྟོང་པ་ཉིད་ཅེས་བྱ་བར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ནི་འདི་ནང་སྟོང་པ་ཉིད་དོ་ཞེས་རྣམ་པར་མི་རྟོག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2270]
གཟུགས་སྟོང་ཞེས་བྱ་བའམ། མི་སྟོང་ཞེས་བྱ་བར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ནི་གཉི་གར་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 2271]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་གཅིག་ལ་གཅིག་སྦྱར་བ་དང་། དེའི་འོག་ཏུ་ཐབས་མཁས་པ་དང་། ཚོགས་ཡོངས་སུ་རྫོགས་པའི་གཏམ་དང་འཁོར་ལོས་སྒྱུར་བའི་དཔེ་དང་། བུད་མེད་ཀྱི་དཔེ་དང་། གཡུལ་ངོར་འགྲོ་བའི་སྐྱེས་བུ་དཔའ་བའི༌[^1591]དཔེ་དང་། ཁམས་ཀྱི་རྒྱལ་པོའི་དཔེ་དང་། ཆུ་ཀླུང་གི་དཔེ་དང་། ལག་པ་གཡས་པའི་དཔེ་དང་། རྒྱ་མཚོའི༌[^1592]ཆེན་པོའི་རོའི་དཔེ་དང་། འཁོར་ལོ་རིན་པོ་ཆེའི་དཔེ་དང་། དེ་ནས་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བཤད་པ་དག་ནི་གོ་སླའོ། །

[Block 2272 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔའི་རབ། ^1-2-7-25-0

[Block 2273]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཐ་དད་པ་མ་མཆིས་ན་ཅིའི་སླད་དུ༌[^1593]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཉིད༌[^1594]ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔའི་རབ་ཅེས་བགྱི་ཞེས་བྱ་བ་ནི་ཐ་དད་པ་མེད་པའི་ཕྱིར་ཁྱད་པར་མེད་དེ། གཅིག་པ་ལ་རབ་ཅེས་བྱ་བ་མི་རིགས་སོ་ཞེས་དགོངས་པའོ། །

[Block 2274]
རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 2275]
དེ་དེ་བཞིན༌[^1595]ཏེ་ཞེས་བྱ་བ༌[^1596]དགོངས་པ་ནི་འདི་ལྟ༌[^1597]སྟེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཡོངས་སུ་ཟིན་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་པོ་དག་ཐ་དད་པར་མི་འགྱུར་ཏེ། དེ་བས་ན་ཐ་དད་པ་མེད་པ་དེ༌[^1598]ཉིད༌[^1599]ལ་རག་ལུས་པའི་ཕྱིར་དེ་ལ་རབ་ཅེས་བྱ་སྟེ། འདིར་ཡང༌[^1600]རི་རབ་ཀྱི་དཔེས་བསྟན་ཏོ། །

[Block 2276]
དོན་གྱི་རྗེས་སུ་ཞུགས་པ་ལ་ནི་ཆོས་གང་ལ་ཡང་བྱེ་བྲག་དང་ཁྱད་པར་མེད་དེ་ཞེས་བྱ་བ་ནི་དོན་གྱི་རྗེས་སུ་ཞུགས་པའི་གང་ཟག་ལ་ཆོས་གང་ཡང་བྱེ་བྲག་ཏུ་མི་སྣང་ངོ་། །དེ་བཞིན་དུ་དོན་གྱི་དབང་གིས་ཆོས་རྣམས་ལ་བྱེ་བྲག་གང་ཡང་མེད་དེ། དེ་བས་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཁོ་ན་མཆོག༌[^1601]ཅེས་བརྗོད་པར་མི་བྱའོ་ཞེས་བྱའོ་ཞེས་གསུངས༌[^1602]པའོ། །

[Block 2277]
རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 2278]
དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ནི༌[^1603]འདི་སྐད་བསྟན་ཏེ། དོན་གྱི་རྗེས་སུ་ཞུགས་པ་དེ་ཉིད་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་གིས་འགྱུར་ཏེ།[^1604] དེ་བས་ན་དེ་རབ་ཅེས་བྱའོ། །

[Block 2279]
འདི་ལྟར་བྱེ་བྲག་མེད་ཀྱང་འཇིག་རྟེན་ན་བརྡའི་རྗེས་སུ་འབྲང་བས་འདི་ནི་སྦྱིན་པས་སོ། །

[Block 2280]
འདི་ནི་ཚུལ་ཁྲིམས་སོ། །
--- END BLOCKS ---
