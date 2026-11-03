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
[Block 3466]
སྨན་གྱི་རྒྱལ་པོ་འདི་ནི་ཞེས་པ་ནས་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཞལ་བཞུགས་པ་ན་ཡང་གསངས་ཏེ། ཀུན་ལ་བསྟན་པ་མ་ཡིན་པའང་ཆུད་དཀའ་བའི་ཕྱིར་མ་འོངས་པའི་དུས་ན་དབང་པོ་མ་རྟོགས་པ་རྣམས་ལ་བསྟན་ན་སྐུར་བ་འདེབས་པའི་ཕྱིར་མ་སྟོན་ཅིག་པར་བསྟན་པའོ། །

[Block 3467]
མདོ་ལས་འདི་ལྟར་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་ཕྱག་གིས་བྱུག་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་འདིའི་མཐུས་འདོན་པའི་གང་ཟག་ཡོན་ཏན་ཅན༌[^2923]དུ་འགྱུར་བ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ན་བཟའ་ནི་བཟོད་པ། ཞི་བ། དུལ་བ། བྱམས་པ་དང་སྙིང་རྗེར་ལྡན་པ། ངོ་ཚ་བ་དང་འཛེམ་པ་སྤངས་པ་སྟེ། ན་བཟའ་དེས་བཀབ་པར་གྱུར་པ་དང་། དབང་པོ་སྨིན་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^2924]དགོངས་ཤིང་སྐྱོབ་པར་འགྱུར་བ་དང་། མོས་པ་ཆེ་བར་འགྱུར་བ་དང་། སྨོན་ལམ་དང་དད་པ་བཙན་པའི༌[^2925]རང་བཞིན་ཅན་དུ་འགྱུར་བ་དང་། དགེ་བའི་རྩ་བ་ཅན་དུ་འགྱུར་བ་དང་། སྟོང་པ་ཉིད་དང་སྙིང་རྗེའི་ཁྱད་པར༌[^2926]བཅོམ་ལྡན་འདས་དང་འདྲ་བར་འཇུག་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཕྱག་གིས་བྱུག་ཅིང་གནས་འཚོབ་པར་ལུང་བསྟན་པ་འཐོབ་པའོ། །

[Block 3468 [HEADING]]
###### འདོན་པའི་གནས་མཆོད་རྟེན་དུ་གྱུར་པ། ^4-10-6-1-2-0

[Block 3469 [HEADING]]
###### **ཆོས་ཀྱི་སྐུ་དང་རིང་བསྲེལ།** ^4-10-6-1-2-1-0

[Block 3470]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་མཆོད་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་སྐུ་དང་། རིང་བསྲེལ་མཆོད་པར་འོས་པ་བསྟན་ཏེ། དེ་ལ་དང་པོ༌[^2927]ཆོས་ཀྱི་སྐུ་དང་། རིང་བསྲེལ་བསྟན་པ་དང་། འདི་ལ་བརྟེན་ཏེ་ཆོས་སྨྲ་བ་ཡོན་ཏན་ཅན་དུ་འགྱུར་བ་བསྟན་ཏོ། །

[Block 3471]
ཆོས་དེ་དང་རིང་བསྲེལ་མཆོད་པར་འོས་པ་ནི་གཞུང་དང་ཡེ་ཤེས་ལྡན་པའི་ཕྱིར་ཏེ། སེམས་ཅན་རྣམས་ལ་ཡང་དག་པའི་ཡེ་ཤེས་ཕྱེ་བ་དང་། བསྟན་པ་དང་རྟོགས་ཤིང་འཇུག་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3472 [HEADING]]
###### **ཆོས་སྨྲ་བ་ཡོན་ཏན་ཅན་དུ་འགྱུར་བ།** ^4-10-6-1-2-2-0

[Block 3473]
མདོ་ལས་ཡང་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་ཤིན་ཏུ་ཉེ་བར་གྱུར་པར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་འདི་ལ་བརྟེན་ནས་ཆོས་སྨྲ་བ་ཡོན་ཏན་ཅན་དུ་འགྱུར་བ་བསྟན་ཏེ། བྱང་ཆུབ་ཏུ་བསྙེན་པ་དང་། སྤྱོད་པ་དམ་པ་ལ་གཞོལ་བ༌[^2928]དང་། བྱང་ཆུབ་ཆེན་པོ་འགྲུབ་པར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 3474]
མདོ་ལས།

[Block 3475]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་ཉེ་བར་གནས་པ་ཡིན་ནོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་འདི་ཐོས་པས་སྤྱོད་པ་དམ་པ་ལ་གཞོལ་བའི་རྒྱུ་བསྟན་ཏེ། མཐོང་བ༌[^2929]དང་། ཐོས་པ་དང་། ཀློག་པ་དང་། འདོན་པ་དང་། འདྲི་བ་དང་། འཛིན་པ་དང་། མཆོད་པའོ། །

[Block 3476]
དེ་དག་ཀྱང་དཔེ་དང་། དོན་དང་། བསྡུ་བ་དང་གསུམ་མོ། །

[Block 3477]
ཡང་མཐོང་བ༌[^2930]དང་། བསམ་པ་དང་། བསྒོམ་པའི༌[^2931]ཤེས་རབ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3478]
མདོ་ལས།

[Block 3479]
འདི་ལྟ་སྟེ་དཔེར་ན་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་ཆུ་འདི་ནི་ཐག་ཉེའོ་སྙམ་ཞེས་པའི་བར་དུ་ནི་དཔེ་བསྟན་ཏེ། སློབ་པ་འབྱུང་བ་རྩོལ་བ་འཁོར་བ་ལ་གནས་ཤིང་ཡང་དག་པའི་ལམ་ཚོལ་བའོ། །

[Block 3480]
ཡང་ན་འགྲེལ་པ་ལས་ཀྱང་ཆུ་ནི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་ནོ། །

[Block 3481]
རྐོ་ཞེས་པ་ནི་ཡང་དག་པའི་ཤེས་རབ་སྔོན་དུ་བཏང་བས་ལུས་དང་། ངག་དང་ཡིད་གསུམ་གྱི་ལས་ཀྱིས་འབད་པའོ། །

[Block 3482]
ས་སྐམ་པོ་མཐོང་བ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་བསྟན་པ་དྲང་བའི་དོན་དུ་བཤད་པ་དང་སྦྱར་རོ། །

[Block 3483]
ས་གཤེར་བ་མཐོང་ཞེས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐེག་པ་ཆེན་པོའི་བསྟན་པ་དང་ཕྲད་པ་སྟེ། བླ་ན་མེད་པའི་བྱང་ཆུབ་དང་ཉེ་ཞེས་པའི་དོན་ཏོ། །

[Block 3484]
འགྲེལ་པ་ལས་ཀྱང་མདོ་འདི་འཛིན་པའི་གང་ཟག་དེ་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་གྱི་ཆུ་དང་ཕྲད་པས་བླ་ན་མེད་པའི་བྱང་ཆུབ་དང་ཉེ་ཞེས་པའི་དོན་ཏོ། །

[Block 3485]
མདོ་ལས་དེ་བཞིན་དུ་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་སྐྱེའོ༌[^2932]ཞེས་པའི་བར་དུ་ནི་འདིས་དཔེ་དང་དོན་དུ་སྦྱར་བ་སྟེ། ཤེས་རབ་རྣམ་གསུམ་དང་ཆོས་སྤྱོད་པ་བཅུ་དང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3486]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་གསང་བའི་གནས་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་འདིས་གཏན་ཚིགས་སྟོན་ཏེ། བྱང་ཆུབ་ཆེན་པོའི་ཆོས་འདི་རྒྱུ་དང་བཅས་པ། [^2933]འབྲས་བུ་དང་བཅས་པ། ཉེ་བའི་རྒྱུ་དང་ལྡན་པ། རིང་བའི་རྒྱུ་དང་ལྡན་པ། ལུང་དང་གཞུང་དང་། སྤྱོད་པ་དང་། འབྲས་བུར༌[^2934]བཅས་པ་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་དང་ཡེ་ཤེས་ཀྱི་རང་བཞིན་དང་། ཡེ་ཤེས་རྣམ་ལྔ་ཀུན་ཀྱང་མདོ་འདི་ལས་སྐྱེ། མདོ་འདི་ལས་ཐོབ་པའོ། །

[Block 3487]
ལྡེམ་པོ་ངག་མཆོག་འགྲེལ་པ་ནི་དྲང་བ་དང་ངེས་པའི་དོན་འགྲེལ་པའོ། །

[Block 3488 [HEADING]]
###### ཆོས་ཇི་ལྟར་བཤད་པའི་ཚུལ། ^4-10-6-1-3-0

[Block 3489 [HEADING]]
###### **བཤད་པའི་ཚུལ།** ^4-10-6-1-3-1-0

[Block 3490 [HEADING]]
###### **དྲིས་པ།** ^4-10-6-1-3-1-1-0

[Block 3491]
མདོ་ལས་སྨན་པའི༌[^2935]རྒྱལ་པོ་བྱང་ཆུབ་སེམས་དཔའ་ལ་ལ་ཞེས༌[^2936]པ་ནས་ཡང་དག་པར་སྟོན་ན་ཞེས་པའི་བར་དུ་ནི། ཆོས་ཇི་ལྟར་བཤད་པའི་ཚུལ་བསྟན་ཏེ། དེ་ལ་ཡང་བཤད་པའི་ཚུལ་དང་། བཀའ་བཞིན་དུ་མཉན་པས་དེ་བཞིན་གཤེགས་པས་རྗེས་སུ་སྐྱོབ་པའོ། །

[Block 3492]
ཚིག་དང་པོ་ལ་ཡང་དྲིས་པ་དང་། བཤད་པ་དང་། བསྡུས་པ་སྟེ། འདི་ནི་དྲིས་པའོ། །

[Block 3493 [HEADING]]
###### **བསྟན་པ།** ^4-10-6-1-3-1-2-0

[Block 3494]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་བྱང་ཆུབ་སེམས་དཔའ་དེས་ཞེས་པ་ནས་ཡང་དག་པར་བཤད་དོ་ཞེས་པའི་བར་དུ་འདི་ནི་བསྟན་པའོ། །

[Block 3495]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་ཆོས་ཀྱི་གཞུང་འདི་འཁོར་བཞི་ལ་ཡང་དག་པར་བསྟན་པའོ་ཞེས་པའི་བར་དུ་ནི་དངོས་སུ་བསྟན་པ་སྟེ། བྱམས་པ་དང་སྙིང་རྗེ་ལ་སྐུ་དང་ཐུགས་རྟག་ཏུ་གནས་པའི་ཕྱིར་གནས་ལྟ་བུར་བལྟའོ།[^2937] །ཡང་ན་ཐེག་པ་ཆེན་པོ་ཉིད་མཐར་ཕྱིན་པའི་གནས་ཉིད་དོ། །

[Block 3496]
ཞི་ཞིང་དུལ་བ་དང་བཟོད་ཅིང་བྱམས་པས་ལུས་མཛེས་པར་བྱས་པའམ། དེའི་དགོས་པས་ཕྱི་རོལ་གྱི་གནོད་པས་མི་བརྫི་བའི༌[^2938]ཕྱིར་གོས་ལྟ་བུར་བལྟའོ། །

[Block 3497]
ཆོས་སྟོང་པ༌[^2939]ཉིད༌[^2940]དུ་བསྟན་པ་ཡང་མདོ་དག་ལས་ཀྱང་བསམ་གཏན་བཞི་ནི་གདན་ཏེ་ཞེས་པ་སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་ལ་གནས་པ་ཉིད་གདན་ལྟ་བུར་བལྟའོ། །

[Block 3498 [HEADING]]
###### **བསྡུས་པ།** ^4-10-6-1-3-1-3-0

[Block 3499]
མདོ་ལས་བྱང་ཆུབ་སེམས་དཔའ་མི་ཞན༌[^2941]པའི་སེམས་ཀྱིས་ཞེས་པ་ནས་ཡང་དག་པར་བཤད་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་གསུམ་པ་སྟེ་བསྡུས་པའོ། །

[Block 3500 [HEADING]]
###### **དེ་བཞིན་གཤེགས་པས་རྗེས་སུ་སྐྱོབ་པ།** ^4-10-6-1-3-2-0

[Block 3501]
མདོ་ལས།

[Block 3502]
སྨན་གྱི་རྒྱལ་པོ་ང་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་པ་ནས་ཁ་ཏོན་བྱེད་པ་ནས་སླར་འཐོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཚིག་དེ་དང་མཐུན་པར་བྱས་ན་དེ་བཞིན་གཤེགས་པ་ཡང་རྗེས་སུ་སྐྱོབ་ཅིང་ཉན་དུ་འཛུད། མཐོང༌[^2942]བར་བྱེད་མི་བརྗེད་པར་བྱེད་དོ། །

[Block 3503]
སྤྲུལ་པས་སྤྲུལ་པ་བསྡུ་ཞིང་ཆོས་སྟོན་པའོ། །

[Block 3504 [HEADING]]
##### ཚིགས་སུ་བཅད་པ། ^4-10-6-2-0

[Block 3505 [HEADING]]
###### མོས་པར་དཀའ་བ། ^4-10-6-2-1-0
--- END BLOCKS ---
