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
[Block 3256]
དབང་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པ་བཞི་སྟེ། སྐྱེས་བུ་ཆེན་པོར་གྱུར་པ་དང་། སེང་གེའི་སྒྲ་ཆེན་པོ་ཅན་དང་། ཤིན་ཏུ་དམ་བཅས་པ་ཅན་དང་། མི་བརྗེད་པའི་ཆོས་ཅན་ནོ། །

[Block 3257 [HEADING]]
### སྐྱེས་བུ་ཆེན་པོར་གྱུར་པ། ^13-1-0

[Block 3258]
སེམས་ཅན་གྱི་མཆོག་དམ་པ་སྐྱེས་བུ་ཆེན་པོ་ཞེས་བྱ་བ་ནི། གང་མཚན་དང་དཔེ་བྱད་རྣམས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3259 [HEADING]]
### སེང་གེའི་སྒྲ་ཆེན་པོ་ཅན། ^13-2-0

[Block 3260]
སེང་གེའི༌[^2820]སྒྲ་ཆེན་པོ་ཅན་ནི་གང་སྟོབས་བཅུ་ཐོབ་པ་སྟེ། ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་སྤོབས་པ༌[^2821]དང་། ཁྱུ་མཆོག་གི་གནས་ཆེན་པོ་རབ་ཏུ་ཤེས་ཤིང་ཚངས་པའི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་དང་། འཁོར་དུ་སེང་གེའི་སྒྲ་ཡང་དག་པར་སྒྲོག༌[^2822]པར་བྱེད་པའོ། །

[Block 3261 [HEADING]]
### ཤིན་ཏུ་དམ་བཅས་པ་ཅན། ^13-3-0

[Block 3262]
ཤིན་ཏུ་དམ་བཅས་པ་ནི་མི་འཇིགས་པ་བཞི་ཐོབ་པ་དག༌[^2823]གིས་ཤེས་པ་དང་། སྤོང་བ༌[^2824]ཡང་ཡང་དག་པར་རབ་ཏུ་ཤེས་ལ། གཞན་གྱི༌[^2825]མི་མཐུན་པའི་ཕྱོགས་དང་གཉེན་པོ་ཡང་རབ་ཏུ་ཤེས་པའོ། །

[Block 3263 [HEADING]]
### མི་བརྗེད་པའི་ཆོས་ཅན། ^13-4-0

[Block 3264]
མི་བརྗེད་པའི་ཆོས་ཅན་སེམས་ཅན་མཆོག་དམ་པ་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་ཐོབ་པ་སྟེ། སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། རྙེད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ནན་ཏན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3265 [HEADING]]
## མི་ཟད་པ་བརྒྱད་ཅུ། ^14-0

[Block 3266]
བཙུན་པ་ཤ་ར་དྭ༌[^2826]ཏིའི་བུ་གཞན་ཡང་འདི་དག་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མི་ཟད་པ་བརྒྱད་ཅུ༌[^2827]ཞེས་བྱ་བ་ལ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ནས་ཐབས་ཀྱི་བར་དུ་མིང་གིས་སྨོས་པ་དེ་རྣམས་མི་ཟད་པ་བརྒྱད་ཅུ་ཞེས་བྱ་སྟེ། དེ་དག་མི་ཟད་པ་ཡང་རྟག་ཏུ་དགེ་བ་དང་། ངོ་བོ་ཉིད་མི་ཉམས་པ་དང་། ངོ་བོ་ཉིད་མི་གཏོང་བ་དང་། བདག་གི་ལས་བྱེད་པ་དང་། རྟག་ཏུ་འབྲས་བུ་ཡོངས་སུ་འཛིན་པ་དང་། རྒྱུ་ཡོངས་སུ་མི་ཟད་པ་དང་། དོན་དམ་པར་མི་ཟད་པའོ། །

[Block 3267 [HEADING]]
### རྟག་ཏུ་དགེ་བ། ^14-1-0

[Block 3268]
དེ་ལ་རྟག་ཏུ་དགེ་བས་མི་ཟད་པ་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ལ་སོགས་པ་བརྒྱད་ཅུ་པོ་དེ་རྣམས་ནམ་ཡང་མི་དགེ་བར་མི་འགྱུར་གྱི། རྟག་ཏུ་དགེ་བའི་རྒྱུན་མི་འཆད་པའི་ཕྱིར་རོ། །

[Block 3269 [HEADING]]
### ངོ་བོ་ཉིད་མི་ཉམས་པ། ^14-2-0

[Block 3270]
ངོ་བོ་ཉིད་མི་མཉམ་པ༌[^2828]ནི་བརྒྱད་ཅུ་པོ་དེ་རྣམས་ཀྱི་རང་བཞིན་བྲི༌[^2829]ཞིང་ཉམས་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3271 [HEADING]]
### ངོ་བོ་ཉིད་མི་གཏོང་བ། ^14-3-0

[Block 3272]
ངོ་བོ་ཉིད་མི་གཏོང་བ་ནི། བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་བརྒྱད་ཅུ་པོ་དེ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའམ། གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 3273 [HEADING]]
### བདག་གི་ལས་བྱེད་པ། ^14-4-0

[Block 3274]
བདག་གི༌[^2830]ལས་བྱེད་པ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་བརྒྱད་ཅུ་པོ་དེ་རྣམས་རང་རང་གི་དམིགས་པའམ་བྱ་བ་གང་ཡིན་པ་ལས་མི་འགྱུར་བའོ། །

[Block 3275 [HEADING]]
### རྟག་ཏུ་འབྲས་བུ་ཡོངས་སུ་འཛིན་པ། ^14-5-0

[Block 3276]
རྟག་པར་འབྲས་བུ་ཡོངས་སུ་འཛིན་པ་ནི། བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་སོ་སོའི་འབྲས་བུ་གང་ཡིན་པ་ཐོབ་པར་བྱེད་དེ། འབྲས་བུ་མེད་པར་མི་འགྱུར་བའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 3277 [HEADING]]
### རྒྱུ་ཡོངས་སུ་མི་ཟད་པ། ^14-6-0

[Block 3278]
རྒྱུ་ཡོངས་སུ་མི་ཟད་པ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ༌[^2831]དེ་སྐྱེ་བའི་རྒྱུ་ནི་སེམས་ཅན་ལ་དམིགས་པ་སྟེ། དམིགས་པར་བྱ་བའི་སེམས་ཅན་རྣམས་མི་ཟད་པས་ན། བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་དེ་དག་ཀྱང་མི་ཟད་པའོ། །

[Block 3279 [HEADING]]
### དོན་དམ་པར་མི་ཟད་པ། ^14-7-0

[Block 3280]
དོན་དམ་པར་མི་ཟད་པ་ནི། དོན་དམ་པར་བརྒྱད་ཅུ་པོ་དེ་དག་ཐམས་ཅད༌[^2832]ཀྱང་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་སྟེ། དེ་བཞིན་ཉིད་ནི་ནམས་ཀྱང་འགྱུར་བ་མེད་པའི་ཕྱིར་མི་ཟད་པའོ།[^2833] །

[Block 3281 [HEADING]]
## བསྟན་པ་རྫོགས་པའི་དོན་བཅུ་གཅིག། ^15-0

[Block 3282]
མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱ་བ་མན་ཆད༌[^2834]བསྟན་པ་རྫོགས་པས་དོན་བཅུ་གཅིག༌[^2835]བསྟན་ཏེ། བསྟན་པའི་བདག་ཉིད་ཆེན་པོ་དང་། སྟོན་པ་ལ་མཆོད་ཅིང་བསྟོད་པ་དང་། སྟོན་པས་རྗེས་སུ་ཡི་རང་བ་དང་། དགེ་བའི་བཤེས་གཉེན་དང་། བསྟན་པ་ལ་དྲིན་གཟོ་ཞིང་རྗེས་སུ་ཡི་རང་བ་དང་། སྟོན་པ་དང་བསྟན་པ་གཅེས༌[^2836]པར་བྱ་བ་དང་། དེའི་རྒྱུ་བརྗོད་པ་དང་། བསྟན་པ་བསྲུང་བར་དམ་བཅས་པ་དང་། བསྟན་པ་གཏད་པ་དང་། འགལ་བ་སྟོན་པ་ལ་བཟོད་པར་གསོལ་བ་དང་། མཚན་དྲི་བ་དང་། བཙུན་དུ་བྱ་བའོ། །

[Block 3283]
དེ་ལ་མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བཟོད་པ་ཐོབ་པར་གྱུར་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2837]བསྟན་པའི་བདག་ཉིད་ཆེན་པོ་བསྟན་ཏོ། །

[Block 3284]
ཐམས་ཅད་དང་ལྡན་པའི་འཁོར་དེ་ཡང་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། མི་ཟད་པ་འདི་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་ཆེད་དུ༌[^2838]བརྗོད་པ་ཆེད་དུ་བརྗོད་དོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2839]སྟོན་པ་ལ་མཆོད་ཅིང་བསྟོད་པ་བསྟན་ཏོ། །

[Block 3285]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འཇིག་རྟེན་གྱི་མཆོད་རྟེན་ལགས་སོ་ཞེས་གསོལ་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་སྟོན་པས༌[^2840]རྗེས་སུ་ཡི་རང་བར་བསྟན་ཏོ། །

[Block 3286]
དེ་ནས་ཕྱོགས་བཅུ་ཀུན་ནས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དགའ་བ་འདི་དག་བཏང་ངོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2841]དགེ་བའི་བཤེས་གཉེན་དང་བསྟན་པ་ལ་དྲིན་གཟོ་ཞིང་རྗེས་སུ་ཡི་རང་བར༌[^2842]བསྟན་ཏོ། །

[Block 3287]
དེ་ནས་ཐམས་ཅད་དང་ལྡན་པའི་འཁོར་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། རྒྱ་ཆེར་རབ་ཏུ་སྟོན་པ་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་སྟོན་པ་དང་བསྟན་པ་གཅེས་པར༌[^2843]བྱ་བ༌[^2844]བསྟན་ཏོ། །

[Block 3288]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་འཁོར་དེའི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ལ་གཞོལ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2845]དེའི་རྒྱུ་བརྗོད་པ་བསྟན་ཏོ། །

[Block 3289]
དེ་ནས་རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བག་ཙམ་གྱིས་ཀྱང་བར་ཆད་བགྱིད་དུ་མི་མཆིའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསྟན་པ་བསྲུང་བར་དམ་བཅས་པ་བསྟན་ཏོ། །

[Block 3290]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་ལ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལེགས་སོ་ལེགས་སོ༌[^2846]ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསྟན་པ་གཏད་པ་བསྟན་ཏོ། །

[Block 3291]
དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བློ་གྲོས་མི་ཟད་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཁྱོད་འདྲ་བའི་སྐྱེས་བུ་དམ་པ་རྣམས་ལ་ཤིན་ཏུ་བཟོད་དོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས། འགལ་བ་སྟོན་པ་ལ་བཟོད་པར་གསོལ་བ་བསྟན་ཏོ། །

[Block 3292]
དེ་ནས་བཅོམ་ལྡན་འདས་ལ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འདི་ཇི་ལྟ་བུར་གཟུང་བར་བགྱི་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་མཚན་དྲི་བ་བསྟན་ཏོ། །

[Block 3293]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སངས་རྒྱས་ཀྱི་བྱ་བས་ཉེ་བར་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2847]མཚན་དུ་བྱ་བར་བསྟན་ཏོ། །

[Block 3294]
མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་འདི་ལས་མི་ཟད་པར་གཏོགས་པའི་ཆོས་དཔག་ཏུ་མེད་པ་འབྱུང་བ་ན༌[^2848]མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱའོ། །

[Block 3295]
ཆེད་དུ་བརྗོད་པ་ཆེད་དུ་བརྗོད་ཅེས་བྱ་བ་ནི་དགའ་བ་དང་། གཟེངས་མཐོས་པའི་ཚིག་འདི་སྐད་དུ་སྨྲས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
