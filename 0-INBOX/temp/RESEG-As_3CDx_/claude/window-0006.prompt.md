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
དེ་ལྟར་བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དེ་ལ་འཚེ་བ་མེད་པ་ཡང་དགོས་པས་དེའི་ཕྱིར་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཉོན་མོངས་པའི་དྲི་མའི་གནོད་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ནི་རང་གི༌[^165]ནང་གི་རྒྱུད་ལས་བྱུང་བའི་གནོད་པ་མེད་པར་སྟོན་ཏོ། །

[Block 212]
དེ་ལ་ཉོན་མོངས་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའོ། །

[Block 213]
དྲི་མ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དེ་དག་ཉིད་དྲི་མའོ། །

[Block 214]
གནོད་པ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་དྲི་མ་ལས་བྱུང་བའི་གནོད་པ་སྟེ་སྡུག་བསྔལ་སྣ་ཚོགས་སོ། །

[Block 215]
ཉོན་མོངས་པའི་དྲི་མ་དེ་དག་ནི་གནོད་པའི་རྒྱུ་ཡིན་ཏེ། དེ་དག་མེད་པས་དེ་ལས་བྱུང་བའི་གནོད་པ་ཡང་མེད་དོ། །

[Block 216]
འོ་ན་དེ་ཇི་ལྟར་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཞེ་ན། ཉོན་མོངས་པའི་དྲི་མས་བྱས་པའི་གནོད་པ་མེད་པ་གང་ཡིན་པ་དེ་ཉིད་འཚེ་བ་མེད་པ་ཡང་ཡིན་ཏེ། དཔེར་ན་བདག་པོས་ཕན་མ་བཏགས་ཀྱང་མ་གཙེས་པའི་ཕྱིར་བདག་གི་རྗེ་བོ༌[^166]དཔོན་གྱིས་མ་གཙེས་སོ་ཞེས་ཟེར་བ་ལྟ་བུ་སྟེ། དེ་ནི་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 217 [HEADING]]
##### ཕྱིར་རྒོལ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-13-0

[Block 218]
དེ་ལྟར་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། ནང་གི་གནོད་པ་མེད་པས་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་ལ་ཕྱི་རོལ་གྱི་གནོད་པའི་རྒྱུ་ཡང་མེད་པས་དེའི་ཕྱིར་ཕྱིར་རྒོལ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་མཛད་ནས་བདུད་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ་ཞེས་གསུངས་ཏེ། དེས་ནི་ཕྱི་རོལ་གྱི་གནོད་པ་མེད་པར་སྟོན་ཏོ། །

[Block 219]
དེ་ལ་བདུད་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཕུང་པོ་དང་། ཉོན་མོངས་པ་དང་། འཆི་བདག་དང་། ལྷའི་བུའི་བདུད་རྣམས་སོ། །

[Block 220]
ཡོངས་སུ་སྤངས་པ་ཞེས་བྱ་བ་ནི་དེ་དག་གིས་དེ་ཡོངས་སུ་སྤངས་ཏེ། དེ་དག་གིས་དེར་མི་བརྫི་བའམ༌[^167]དེས་དེ་དག་ཡོངས་སུ་སྤངས་ཏེ། དེ་ན་དེ་དག་མེད་པའོ། །

[Block 221]
བདུད་དེ་དག་ནི་ཕྱིར་རྒོལ་བ་ཡིན་ཏེ་དེ་དག་ལས་རྒྱལ་ནས་ནི་དེའི་ཕྱིར་རྒོལ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 222 [HEADING]]
##### གནས་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-14-0

[Block 223]
དེ་ལྟར་ཕྱིར་རྒོལ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། ཕྱིར་རྒོལ་བ་མེད་པ་དེའི་ཕུན་སུམ་ཚོགས་པ་དེའི་གནས་ཀྱི་ཁྱད་པར་ཅི་འདྲ་ཞེ་ན། དེའི་ཕྱིར་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས་ཐམས་ཅད་ཀྱི་བཀོད་པ་ལས་ལྷག་པ་དེ་བཞིན་གཤེགས་པའི་བཀོད་པའི་གནས་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དམ་གཞན་དག་གི་བཀོད་པ་ལས་ལྷག་པ་སྟེ། དེ་བཞིན་གཤེགས་པའི་བཀོད་པ་དང་ལྡན་པའི་གནས་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 224]
དེ་བཞིན་གཤེགས་པའི་གནས་ཉིད་དེ་ལྟར་སྣང༌[^168]ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ཐམས་ཅད་ཀྱི་གནས་ལས་ཁྱད་པར་དུ་འཕགས་པས་ན་དེ་ནི་གནས་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 225 [HEADING]]
##### བདག་པོའི་གནས་ཀྱི་བྱེ་བྲག་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-15-0

[Block 226]
དེ་ལྟར་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། དེར་འགྲོ༌[^169]བའི་ལམ་ཅི་འདྲ་བ་ཞེ་ན། དེའི་ཕྱིར་བདག་པོའི་གནས་ཀྱི་བྱེ་བྲག་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དྲན་པ་དང་། བློ་གྲོས་དང་། རྟོགས་པ་ཆེན་པོས་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་དྲན་པ་ཞེས་བྱ་བ་ནི་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་སྟེ། ཐོས་ན་དོན༌[^170]ཕྱིན་ཅི་མ་ལོག་པར་མངོན༌[^171]པར་རྫོགས་པའི༌[^172]ཕྱིར་རོ། །

[Block 227]
བློ་གྲོས་ཞེས་བྱ་བ་ནི་བསམས་པ༌[^173]ལས་བྱུང་བའི་ཤེས་རབ་སྟེ། ཐོས་པའི་དོན་རིག་པས༌[^174]ངེས་པར་རྟོགས་པར་བྱེད་པ་ལ་ངེས་པའི་བློ་གྲོས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 228]
རྟོགས་པ་ཞེས་བྱ་བ་ནི་བསྒོམས་པ༌[^175]ལས་བྱུང་བའི་ཤེས་རབ་སྟེ། བསྒོམས་པའི༌[^176]སྟོབས་ཀྱིས་དེ་ཁོ་ན་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 229]
ཆེན་པོ་ཞེས་བྱ་བ་ནི་དྲན་པ་ལ་སོགས་པ་གསུམ་ཆར་དང་སྦྱར་ཏེ། དེ་ཡང་ཐེག་པ་ཆེན་པོའི་ཆོས་ལ་དམིགས་པ་ལས་བྱུང་བའི་ཕྱིར་དང་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་དང་། ཐེག་པ་ཆེན་པོས་བསྡུས་པ་ཡིན་པའི་ཕྱིར་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 230]
ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནི་འདིས་ངེས་པར་འབྱུང་བ་སྟེ་ལམ་མོ། །

[Block 231]
དེ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་དྲན་པ་ལ་སོགས་པའི་ལམ་འདིས་གནས་དེས་ངེས་པར་འབྱུང་བས་དྲན་པ་ལ་སོགས་པས་ངེས་པར་འབྱུང་བར་སྦྱར་ཏེ། དེ་ནི་བདག་པོའི་གནས་ཀྱི་བྱེ་བྲག་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 232 [HEADING]]
##### བཞོན་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-16-0

[Block 233]
དེ་ལྟར་བདག་པོའི་གནས་ཀྱི་བྱེ་བྲག་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས་གང་ལ་ཞོན་ནས་དེར་འཇུག་པའི་བཞོན་པ་ཡང་དགོས་པས་དེའི་ཕྱིར་བཞོན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཞི་གནས་དང་ལྷག་མཐོང་ཆེན་པོ་བཞོན་པ་ཡིན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་ཞི་གནས་ཞེས༌[^177]བྱ་བ་ནི་སེམས་རྩེ་གཅིག་པའི༌[^178]ཏིང་ངེ་འཛིན་ཏོ། །

[Block 234]
ལྷག་མཐོང་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་མཐོང་བ་སྟེ་ཤེས་རབ་བོ། །

[Block 235]
ཆེན་པོ་ཞེས་བྱ་བ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 236]
དེ་གཉིས་མཉམ་པར་འཇུག་པ་ནི་བཞོན་པ་ཡིན་ཏེ། དེ་གཉིས་ཀྱི་ས་ལམ་དེ་ནས་གནས་དེར་འགྲོ་བའི་ཕྱིར་ཏེ། དེ་ནི་བཞོན་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 237 [HEADING]]
##### སྒོ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-17-0

[Block 238]
དེ་ལྟར་བཞོན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། བཞོན་པ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་དེ་སྒོ་གང་ནས་དེར་འཇུག་པར་འགྱུར་བའི་སྒོ་ཡང་དགོས་པས་དེའི་ཕྱིར་སྒོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་དང་སྨོན་པ་མེད་པ་ནས་འཇུག་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་རྣམ་པར་ཐར་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གྲོལ་བ་སྟེ་མྱ་ངན་ལས་འདས་པའོ། །

[Block 239]
སྒོ་ཞེས་བྱ་བ་ནི་སྒོ་མོ་སྟེ། མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་ཐབས་སོ། །

[Block 240]
ཆེན་པོ་ཞེས་བྱ་བ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 241]
དེ་ཡང་དངོས་སུ་ན་སྟོང་པ་ཉིད་ལ་སོགས་པ་ཉིད་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་ཡིན་ཏེ། སྒོ་དེ་ནས་དེར་འཇུག་པར་སྦྱར་རོ། །

[Block 242]
དེ་ལ་སྟོང་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཆོས་བདག་མེད་པ་སྟེ། ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ཀྱི་ཆོས་མེད་པའོ། །

[Block 243]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །

[Block 244]
མཚན་མ་མེད་པ་ཞེས་བྱ་བ་ལ་མཚན་མ་ནི་གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་རྣམས་དང་སྐྱེས་པ་དང་། བུད་མེད་དང་། སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་ལ་སོགས་པ་སྟེ། དེ་དག་གང་ལ་མེད་པ་དེ་ནི་མཚན་མ་མེད་པའོ། །

[Block 245]
དེ་ཡང་གང་ཞེ་ན་མྱ་ངན་ལས་འདས་པ་སྟེ། དེ་ནི་མཚན་མ་ཐམས་ཅད་བསལ་བའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 246]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ༌[^179]མཚན་མ་མེད་པ་ཞེས་བྱའོ། །

[Block 247]
སྨོན་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སྨོན་པ་ནི་སྨོན་ལམ་སྟེ༌[^180]འདོད་པའོ། །

[Block 248]
དེ་གང་ལ་མེད་པ་ནི་སྨོན་པ་མེད་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན་ཁམས་གསུམ་པ་སྡུག་བསྔལ་བར་མཐོང་ན་དེ་ལ་སྨོན་པར་བྱ་བ་མེད་དོ༌[^181]སྙམ་ནས་དེར་སྨོན་ལམ་མི་འདེབས་པ༌[^182]ནི་སྨོན་པ་མེད་པའོ། །

[Block 249]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་སྨོན་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 250]
ནས་འཇུག་པས་ཞེས༌[^183]བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་སོགས་པ་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་དེ་དག་ནས་དེར་འཇུག་པར་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ནི་སྒོ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
