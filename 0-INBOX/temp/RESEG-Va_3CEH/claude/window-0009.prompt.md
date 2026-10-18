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
[Block 316]
འདོད་ཆགས་ལ་སོགས་པ་དང་བཅས་པར་འབྱུང་དུ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས༌[^201]པ་དང་བཅས་པར་འབྱུང་བའོ། །

[Block 317]
དེ་ལྟ་བས་ན་འདས་པའི་རྒྱུ་ལས་ནི་མི་རུང་སྟེ། འདི་ལྟར་འདས་པའི་དུས༌[^202]ལས་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་འབྱུང་བ་ཇི་ལྟར་མི་རུང་བ་བཞིན་དུ་དེའི་ཡང་མི་རུང་ངོ་། །གལ་ཏེ་བྱེ་བྲག་ཏུ་སྨྲ་བ་འདས་པ་ཡོད་པ་ཉིད་དུ་འདོད་པས་དེའི་ཕྱིར་འདས་པ་ལས་འབྱུང་ངོ་ཞེ་ན། དེ་དག་གི༌[^203]འདས་པ་ཞེས་བྱ་བ་ནི་བརྗོད་པས་བརྗོད་པར་བྱ་བ་ཉིད་དུ་མི་འགྲུབ་པས་དེ་ནས༌[^204]འདས་པ་ཞེས་བྱ་བ་འདི་གང་ཡིན། ཆོས་གང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྐྱེས་པ་ཡོད་པ་དེ་ནི་བག་ཆགས་མེད་པས་མ་ཡིན་ནོ། །

[Block 318]
མིག་གི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ། [^205]རེ་ཞིག་མིག་གི་རྣམ་པར་ཤེས་པ་འདོད་ཆགས་ལ་སོགས་པ་དང་ལྷན་ཅིག་འབྱུང་བ་དེ་ལ་ཡང་བག་ཆགས་མི་རུང་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ༌[^206]ལས་སྐྱེས་པ་དེ་ལ་བག་ཆགས་ཇི་ལྟར་རིགས། རེ་ཞིག་འདོད་ཆགས་ལ་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་བག་ཆགས་ནི༌[^207]མི་རིགས་ཏེ། གང་གི་ཕྱིར་འདོད་ཆགས་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་བརྟེན་པའི་ཕྱིར་དང་། མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 319]
རྣམ་པར་ཤེས་པ་གཞན་དག་ལ་ཡང་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་རྣ་བའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ༌[^208]ལ་སྟེ། གང་གི་ཕྱིར་དེ་དག་ནི་གནས་ཐ་དད་པའི་ཕྱིར་དང་། གནས་ཐ་དད་པ་ཉིད་ཡོད་ན་ལྷན་ཅིག་འབྱུང་བ་དང་འགག་པ་མེད་པའི༌[^209]ཕྱིར་རོ། །

[Block 320]
མིག་གི་རྣམ་པར་ཤེས་པའི་གནས་ནི་མིག །རྣ་བའི་རྣམ་པར་ཤེས་པའི་གནས༌[^210]ནི་རྣ་བའོ། །

[Block 321]
དེ་བཞིན་དུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་གནས་ནི་ཡིད་ཅེས་བྱ་བའི་བར་དུ་སྟེ། འདི་ལྟར་དེས་ན་བསྐལ་པའི་གནས་ཉིད་ཡིན་པས་གཞན་དག་ལ་གཞན་དག་གི་བག་ཆགས་མི་རིགས་སོ། །

[Block 322]
རང་གི་དངོས་པོ་ལ་ཡང་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ལ། མིག་གི་རྣམ་པར་ཤེས་པ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་བག་ཆགས་ཀྱང་མ་ཡིན་ཏེ། མིག་གི་རྣམ་པར་ཤེས་པ་གཉིས་འབྱུང་བ་ནི་མེད་དེ། གཉིས་ཀྱི་ངོ་བོ་མེད་པས་ན་ལྷན་ཅིག་འབྱུང་བ་དང་འགག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 323]
དེ་ལྟ་བས་ན་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པས་བག་ཆགས་བསྒོས་པར་མི་རུང་ལ། མིག་གི་རྣམ་པར་ཤེས་པ་དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་བག་ཆགས་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 324]
ཐོག་མ་ཉིད་དུ་ཞེས་བྱ་བ་ནི་འདིར་དང་པོར་རོ། །

[Block 325]
དེ་ཡང་ས་བོན་མེད་པར་སྐྱེ་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་རྒྱུ་མེད་པར་སྐྱེ་བའོ། །

[Block 326]
བག་ཆགས་དེ་གནས་དང་བཅས་པར་ཞེས་བྱ་བ་ནི་སེམས་དང་བཅས་པའི་ཉོན་མོངས་པའི་བག་ཆགས་སོ། །

[Block 327]
ཉོན་མོངས་པའི་གཉེན་པོའི་རྣམ་པར་ཤེས་པ་བྱུང་ན་དེ་མ་ཡིན་པ་གཞན་འཇིག་རྟེན་པའི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ནི་འགགས་ན་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཤེས་པ་དྲུག་པོ་འགགས་པ་ནའོ། །

[Block 328]
རྣམ་པར་ཤེས་པ་དེ་ནི་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པའི་ས་བོན་དང་བཅས་པར་མི་རུང་སྟེ་ཞེས་བྱ་བ་ནི་གང་གཉེན་པོའི་རྣམ་པར་ཤེས་པའི་རྒྱུན་ཅན་དུ་འཇིག་རྟེན་པའི་རྣམ་པར་ཤེས་པ་རྣམ་པར༌[^211]འཇུག་པར་འགྱུར་རོ། །

[Block 329]
དེའི་འོག་ཏུ་ཡང་ཞེས་བྱ་བ་ནི་དེས་ན་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་ཉིད༌[^212]ཀྱི་རྟིང་ལའོ། །

[Block 330]
བག་ཆགས་དེ་གནས་དང་བཅས་ཏེ་ཞེས་བྱ་བ་ལ། གནས་དང་བཅས་པ་སྟེ། རྣམ་པར་ཤེས་པ་དང་བཅས་པའོ། །

[Block 331]
བག་ཆགས་དེ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་། ཉོན་མོངས་པའི་བག་ཆགས་སོ། །

[Block 332]
ས་བོན་མེད་པ་ལས་ཞེས་བྱ་བ་ནི་རྒྱུ་མེད་པ་ལས་སོ། །

[Block 333]
སྐྱེ་བར་ནི་འབྱུང་བར་རོ། །

[Block 334]
འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་པར་ཡང་ངོ་། །དེ་ལ་ཉོན་མོངས་པ་ཉིད་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ཉིད་དེ། ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 335]
དེ་ལྟར་ན་འདིར་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་མི༌[^213]རུང་ངོ་། །

[Block 336 [HEADING]]
##### ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ། ^1-5-1-2-0

[Block 337]
ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་རྣམ་པ་གང་གིས་མི་རུང་བ་དེ་བསྒྲུབ་པར་བྱ་སྟེ། ཇི་ལྟར་མི་རུང་ཞེ་ན། འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་མི་རུང་བའི་ཕྱིར་ཞེས་པ་ནི་བསོད་ནམས་དང་། བསོད་ནམས་མ་ཡིན་པ་དང་། མི་གཡོ་བའི་འདུ་བྱེད་འབྱུང་བ་དང་། འགག་པ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་གང་ལ་བག་ཆགས་འཇོག་པར་འགྱུར། ཇི་ལྟར་ན་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་གིས་བག་ཆགས་མི་འཛིན་པ་ནི༌[^214]སྔར་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་བསྟན་པར་བསྒྲུབས་ཟིན་ཏོ། །

[Block 338]
དེ་མེད་ན་ཞེས་བྱ་བ་ནི་འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་མེད་ནའོ། །

[Block 339]
ལེན་པའི་རྐྱེན་གྱིས་སྲེད་པ་ཡང་མི་རུང་སྟེ། གང་གི་ཕྱིར་འདུ་བྱེད་ཀྱིས་ཡོངས་སུ་བསྒོས་པའི་རྣམ་པར་ཤེས་པ་ལེན་པའི་དབང་གིས་བག་ཆགས་རྒྱས་པས་སྲིད་པ་འབྱུང་བས་སོ། །

[Block 340]
དེ་ལ་ལས་ཉིད་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པའམ། ལས་ལས་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་སྟེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན། དེ་ཡང་མི་རུང་ངོ་། །

[Block 341 [HEADING]]
##### ཉིང་མཚམས་སྦྱོར་བ་སྦྲེལ་བ་མི་རུང་བ། ^1-5-1-3-0

[Block 342]
དེའི་ཚེ་ཀུན་ནས་ཉོན་མོངས་པ་ཡང་ཇི་ལྟར་མི་རུང་ཞེ་ན། དེ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ།[^215] །ཉིང་མཚམས་སྦྱོར་བ་སྦྲེལ་བ་མི་རུང་བའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། བདག་གི་དངོས་པོ་འཐོབ་པ་ཡང༌[^216]མི་རིགས་པའོ། །

[Block 343 [HEADING]]
###### མཉམ་པར་མ་བཞག་པའི་ཉིང་མཚམས་སྦྱོར་བ། ^1-5-1-3-1-0

[Block 344]
མཉམ་པར་མ་བཞག་པའི་ས་ནས་ཞེས་བྱ་བ་ནི་འདོད་པའི་ཁམས་ནས་སོ། །

[Block 345]
ཤི་འཕོས་པའི་ཞེས་བྱ་བ་ནི་ཤི་བའོ།[^217] །ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཉོན་མོངས་པ་ཅན་གྱིས་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་བཅས་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའོ། །

[Block 346]
ཉིང་མཚམས་སྦྱོར་ཞིང་སྦྲེལ་ཏེ་ཞེས་བྱ་བ་ནི་བདག་གི་དངོས་པོ་ཡོངས་སུ་འཛིན་པའོ། །

[Block 347]
དེ་ཡང་ཉོན་མོངས་པ་ཅན་གྱི༌[^218]ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་སྐྱེ་བའི་སྲིད་པ་ལ་དམིགས་ནས་བར་མ་དོའི་སྲིད་པ་འགག་པར་འགྱུར་རོ། །

[Block 348]
བརྒྱལ་བ་དེ་ལ་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཁུ་བ་དང་ཁྲག་དང་ལྷན་ཅིག་གྲུབ་པ་དང་། བདེ་བ་གཅིག་པར་འགྱུར་བ༌[^219]སྟེ། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་བརྒྱལ་བར་གྱུར་པ་དེ་ལ་བརྟེན་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཞན་ཉིད་འཇུག་པར་འགྱུར་རོ། །

[Block 349]
ལྷན་ཅིག་ཏུ་ཞེས་བྱ་བ་ནི་དུས་གཅིག་ཏུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་བརྒྱལ་བར༌[^220]གྱུར་པ༌[^221]དེ་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པར་གྱུར་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དུས་རྟག་ཏུ་ཉོན་མོངས་པ་ཅན་གནས་ཡིན་པའི་ཕྱིར་ཏེ། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ༌[^222]འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་གནས་ཏེ། འབྱུང་བའི་སྲིད་པ་ལ་དམིགས་པ༌[^223]ཡིད་ཉོན་མོངས་པ་ཅན་འདིའི་གནས་ཡིན་པས་འདི་ནི་ཉོན་མོངས་པ་ཅན་གྱི༌[^224]གནས་སོ། །

[Block 350]
རྣམ་པར་སྨིན་པ་ལུང་དུ་མ་བསྟན་པའི་གནས་སྐབས༌[^225]དེ་ན་ཉོན་མོངས་པ་ཅན་གྱི་གནས་ནི་མི་སྲིད་དོ། །

[Block 351]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ལ་མི་དམིགས་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་དམིགས་པ་ལ་ཉེ་བར་གནས་ཏེ། འདི་ལྟ་སྟེ་ཆོས་སོ། །

[Block 352]
བརྒྱལ་བར་གྱུར་པ་དེ་ལ་ནི་དམིགས་པ་མེད་དེ། དེའི་ཕྱིར་འདི་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཉིད་དུ་མི་རུང་ངོ་། །ཉིང་མཚམས་སྦྱོར་བ་སྦྲེལ་ཟིན་པ་ཞེས་བྱ་བ་ནི་བདག་གི་ལུས་རབ་ཏུ་ཐོབ་པའོ། །

[Block 353]
དེ་ནས༌[^226]གཞན་ཞེས་བྱ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མ་ཡིན་པ་ནི་གཞན་པ་སྟེ། གཞན་རྣམ་པར་ཤེས་པ་དྲུག་པོ་རྣམས་ནི་གནས་སོ་སོར་ངེས་པ་དང་གཡོ་བའི་ཕྱིར་རོ། །

[Block 354]
ཇི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པ་གནས་སོ་སོར་ངེས་པ་ཡིན་པ་བཞིན་དུ་རྣ་བའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ལྷག་མ་རྣམས་ཀྱི་ཡང་རྣ་བ་ལ་སོགས་པ་དབང་པོ་གཟུགས་ཅན་རྣམས་ནི་རྟེན་ཡིན་ནོ། །

[Block 355]
དེས་ན་གལ་ཏེ་རྣམ་པར་ཤེས་པ་དེ་དག་གི་རང་རང་གི་གནས་བླངས་པར་གྱུར་ལ། རྣམ་པར་ཤེས་པ་དེ་རྣམས་འགགས་པར་གྱུར་པ་ན་ཐོབ་པའི་མིག་ལ་སོགས་པ་རྣམས་རུལ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
