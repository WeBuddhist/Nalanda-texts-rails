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

[Block 2281]
འདི་ནི་བཟོད་པའོ་ཞེས་འདོགས་པར་བྱེད་དེ། འདོགས་པ་དེ་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྒྱུ་ལས་འགྱུར་གྱི་གཞན་ལས་ནི༌[^1605]མ་ཡིན་ཏེ། འདིར་ཡང་བུད་མེད་རིན་པོ་ཆེའི་དཔེས༌[^1606]བསྟན་ཏོ། །

[Block 2282 [HEADING]]
##### ཆོས་གང་ཡང་ཡོངས་སུ་འཛིན་པ་དང་གཏོང་བ་མེད་པ། ^1-2-7-26-0

[Block 2283]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཆོས་གང་ཡང་ཡོངས་སུ་འཛིན་པའམ་གཏོང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ཆོས་འགའ་ཞིག་འཛིན་ན་དེ་ཉིད་མངོན་པར་ཞེན་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 2284]
གལ་ཏེ་གཏོང་ན་ཡང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཡེ་ཤེས་གྲུབ་པར༌[^1607]ནི་འགྱུར་ཏེ། དེ་བས་ན་མི་འཛིན་མི་གཏོང་ངོ་། །ཡང་ན་ཀུན་བརྟགས་པའི་དབང་གིས་ནི་མི་འཛིན། ཆོས་ཉིད་ཀྱི་དབང་གིས་ནི་མི་གཏོང་ངོ་། །རབ་འབྱོར་གང་གཟུགས་ཡིད་ལ་མི་བྱེད་པ་འདི་ནི་གཟུགས་ཡོངས་སུ་མི་འཛིན་པའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་མི་འཛིན་ཞེས་བྱ་བ་གང་ཡང་མེད་ཀྱི། ཡང་དག་པ་མ་ཡིན་པ་ནི་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཡིད་ལ་མི་བྱེད་པ་ཉིད་ཡོངས་སུ་མི་འཛིན་པ་ཞེས་བྱའོ། །

[Block 2285]
རབ་འབྱོར་གང་གི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་གཟུགས་ཡིད་ལ་མི་བྱེད་པ་ནས། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་བར་དུ་ཡིད་ལ་མི་བྱེད་པ་དེའི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་དགེ་བའི་རྩ་བ་རྣམས་རྣམ་པར་འཕེལ་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པའི༌[^1608]ཆོས་རྣམས་མེད་པས་དངོས་པོ་མེད་པའི་བདག་ཉིད་དུ་ཡོངས་སུ་ཤེས་ནས་ཡིད་ལ་མི་བྱེད་པ་ཉིད་དགེ་བའི་རྩ་བ་འཕེལ་བ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 2286]
བྱང་ཆུབ་སེམས་དཔའ་དེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ཉམས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་མཚན་མར་དམིགས་པའི་ཉེས་པས་ཆགས་པའོ། །

[Block 2287]
ཆོས་ཐམས་ཅད་ཡོངས་སུ་མ་བཟུང་བ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མ་ཆགས་པ་དེ་ཉིད༌[^1609]ཡོངས་སུ་མ་བཟུང་བ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ནི་གང་དུ་ཡང་ཆགས་པ་མེད་ལ། གང་ཡང་ཡོངས་སུ་མི་འཛིན་ཏོ། །

[Block 2288]
འདི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མ་བྲལ་བ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་དུས་ཐམས་ཅད་དུ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་ཉིད་དང་མ་བྲལ་བའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2289 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མངོན་པར་བསྒྲུབ་པ། ^1-2-7-27-0

[Block 2290]
དེ་ལྟར་ཆོས་ཐམས་ཅད་ཀྱང་ཇི་ལྟ་ཇི་ལྟ་བུའི་ངོ་བོ་ཉིད་དང་མ་བྲལ༌[^1610]ལགས་ན། འོ་ན་ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མངོན་པར་བསྒྲུབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་དང་མ་བྲལ་བ་ཡིན་ན། འོ་ན་ཇི་ལྟར་དེ་དག་དགེ་བའི་རྩ་བ་ལ་སོགས་པས་ཉེ་བར་གཟུང་བར༌[^1611]བྱ་ཞེས་ཞུས་པའོ། །

[Block 2291]
གཟུགས་ལ་མངོན་པར་ཞེན་པ་མེད་དེ་འདི་ནི་གཟུགས་སོ། །

[Block 2292]
འདི་ནི་གཟུགས་སོ་ཞེས་བྱ་བར་མངོན་པར་ཞེན་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་སྟོན་ཏེ། [^1612]ཆོས་ནི་ཆོས་མངོན་པར་མི་སྒྲུབ་སྟེ། ཆོས་ཐམས་ཅད་ལ་མངོན་པར་ཞེན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2293]
ཡང་དག་པར་རྗེས་སུ་མ༌[^1613]མཐོང་བས་ཇི་ལྟ་ཇི་ལྟ་བུར་གནས་པའི་མཚན་ཉིད་ཀྱི་ཆོས་ཀྱི༌[^1614]ཡང་དག་པ༌[^1615]ཇི་ལྟ་བ་རྟོགས་པ་ཉིད་མངོན་པར་སྒྲུབ་པ་ཞེས་བྱའི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །ཞེས་དེ་སྐད་སྟོན་ཏོ། །

[Block 2294]
འཁོར་ལོས་སྒྱུར་བའི་དཔེ་དང་། ཁ་ལོ་སྒྱུར་བའི་དཔེས་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 2295 [HEADING]]
##### ཆོས་གང་ཡང་སྐྱེད་པ་དང་འགོག་པ་མེད་པ། ^1-2-7-28-0

[Block 2296]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆོས་གང་སྐྱེད༌[^1616]པ་མ་ལགས་འགོག་པ་མ་ལགས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས། འདི་སྐད་ཞུས་ཏེ། གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ཆོས་གང་ཡང་མི་སྐྱེད་ལ། ནག་པོའི་ཆོས་ཀྱང་མི་འགོག་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་གིས་ཅི་ཞིག་བྱ་སྟེ། ཇི་ལྟར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡོངས་སུ་རྫོགས་པར་བྱ་ཞེས་ཞུས་པའོ། །

[Block 2297]
རབ་འབྱོར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་དམིགས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས། བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་གསུངས་ཏེ། ཅི་ཞིག་བསྐྱེད་པར་བྱའོ་སྙམ་མམ། ཅི་ཞིག་དགག་པར་བྱའོ་སྙམ་དུ་བསམས་ཏེ། ཚོགས་ཡོངས་སུ་རྫོགས་པར་མི་བྱ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་འབའ་ཞིག་ཏུ་ཡོངས་སུ་བསྔོ་ཞིང་ཡོངས་སུ་རྫོགས་པར་བསྟན་པའོ། །

[Block 2298]
གཟུགས་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སྤྱོད་ན། གཟུགས་ལ་ཀུན་ཏུ་སྦྱོར་བ་ལས་དབྲལ་བར་བྱའོ། །

[Block 2299]
མི་ལྡན་པ༌[^1617]བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བའི་བློ་བསྐྱེད༌[^1618]པར་མི་བྱ་སྟེ། འདི་ལྟར་བདག་ཉིད་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2300]
གཟུགས་ལ་གནས་པར་བྱའོ་ཞེས་བརྩོན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས། རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བའི་ཕུང་པོ་ལ་སོགས་པ་ལ་གནས་པར་བྱའོ་སྙམ་པའམ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་ཡང་འབྲས་བུའི་ཚུལ་དུ་གནས་པར་བྱའོ་སྙམ་དུ་བརྩོན་པར་མི་བྱ་བའོ། །

[Block 2301]
གཟུགས་ནི་གང་ལ་ཡང་མི་གནས་སོ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་ལ་བྱའོ། །

[Block 2302]
བཟའ་ཤིང་གི་དཔེ་དང་། ཐམས་ཅད་ཀྱི་སྒོ་དང་། འཕོང་གི་སློབ་དཔོན་གྱི་དཔེའོ། །

[Block 2303 [HEADING]]
##### སངས་རྒྱས་ཀྱི་དགོངས་པ། ^1-2-7-29-0

[Block 2304]
དེའི་འོག་ཏུ་སངས་རྒྱས་ཀྱི་དགོངས་པ་ལ་ཅི་ནས་ཀྱང་སྦྱིན་པ་མི་དམིགས་པ་དང་། ཚུལ་ཁྲིམས་དང་བཟོད་པ་མི་དམིགས་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྦྱིན་པ་ལ་སོགས་པ་མི་དམིགས་པས་མི་དམིགས་པའི་ཚུལ་དུ་དགོངས་པ་སྟེ། ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཡང་མི་དམིགས་པའི་ཚུལ་གྱིས་དགོངས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2305]
དེ་བཞིན་ཉིད་ཤེས་ན་ཆོས་ཐམས་ཅད་ཀྱི་མདོ་དང་རྒྱས་པ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་ཡོངས་སུ་གྲུབ་པ་དེ་བཞིན་ཉིད་ཙམ་དུ་ཤེས་པ་དེའི་ཚེ་མདོ་ཤེས་པར་འགྱུར་རོ། །

[Block 2306]
གང་གི་ཚེ་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་དང་། ཚོར་བའི་དེ་བཞིན་ཉིད༌[^1619]ལ་སོགས་པ་མ་དག་ཅིང་ཡོངས་སུ་མ་གྲུབ་པར་ཤེས་པ་དེའི་ཚེ་རྒྱས་པ༌[^1620]ཤེས་པར་འགྱུར་རོ། །

[Block 2307]
རབ་འབྱོར་མཐའ་མེད་པ་ནི་ཡང་དག་པའི་མཐའ་སྟེ་ཞེས་བྱ་བ་ནི་མཐའ༌[^1621]ཞེས་བྱ་བའི་སྒྲ་ནི༌[^1622]རྩེ་མོའི་དོན་ཏེ། དཔེར་ན་རིའི་རྩེ་མོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 2308]
ཁ་ཅིག་ཏུ་ནི་མཐའ་ལ་བྱ་སྟེ་དཔེར་ན་རྒྱ་མཚོའི་མཐའ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 2309]
མཐའ་དེ་གཉི་ག་ཡང་དེ་ལ་མེད་དེ་དེ་ལ་རྩེ་མོའི་མཐའ་མེད་པ་ནི་མཐའ་གང་ལ༌[^1623]ཆད་པ་ཡང་མ་ཡིན་ཞེས་གསུངས་པའོ། །

[Block 2310]
མཐའ་མེད་པ་ནི་ཡོངས་སུ་ཆད་པ་མེད་ཅེས་གསུངས་པ་སྟེ། དེ་བས་ན་ཡང་དག་པའི་མཐའ་ཞེས་བྱ་བ་ནི་དེ་ཁོ་ན་མི་འགྱུར་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2311]
རབ་འབྱོར་ཇི་ལྟར་ཆོས་ཐམས་ཅད་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་པ༌[^1624]ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་གཉི་གར་ཡང་མི་འགྱུར་རོ། །

[Block 2312]
གཅིག་གི་ཚིག་བླ་དགས་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གྲངས་ཤེས་པ་བསྟན་ཏོ། །

[Block 2313]
བུད་མེད་ཀྱི་ཚིག་བླ་དགས་ལ་མཁས་པ༌[^1625]ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རྟགས་ཤེས་པ་བསྟན་ཏོ། །

[Block 2314]
ལམ་གྱི་རྒྱུན་བཅད་པ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་ལམ་ལ་མཁས་པའོ། །

[Block 2315]
ལམ་གྱི་རྒྱུན་མ་བཅད་པ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་ལ་མཁས་པའོ། །
--- END BLOCKS ---
