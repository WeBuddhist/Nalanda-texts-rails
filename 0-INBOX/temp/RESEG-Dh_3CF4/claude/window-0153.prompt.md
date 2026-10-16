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
[Block 5356]
ཚུལ་འཆོས་ཀྱི༌[^3426]བརྟུལ་ཞུགས་ནི་གཡོའི་བརྟུལ་ཞུགས་སོ། །

[Block 5357]
མྱ་ངན་མི་བྱེད་དེ་བདག་ཉིད་ཆེན་པོའི་ཉམས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5358]
བདག་ལ་གནོད་པ་བྱེད་པའི་རྒྱལ་པོ་ལ་ཡང་འཁྲུགས་པར་མི་བྱེད་དོ། །ཅིའི་ཕྱིར་མྱ་ངན་མི་བྱེད་ཅེ་ན། ལུས་ཀྱི་ཕུང་པོ་གནས་པའི་མཐའ་ཤེས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་འཁྲུགས་པར་མི་བྱེད་ཅེ་ན། སྐྱེ་བོ་རྣམས་ལ་བཟོད་པ་གོམས་ཤིང་འདྲིས་པའི་ཕྱིར་རོ། །

[Block 5359]
དེའི་སེམས་ཞེས་བྱ་བ་ནི་རང་གི་སེམས་སོ། །

[Block 5360]
དེའི་ཕྱིར། དགའ་བའི༌[^3427]ཚུལ་གྱིས་ཡོངས་སུ་ཉམས་བར་མ་གྱུར་ཏོ། །

[Block 5361]
སོ་སོར་བརྟགས་པ་ནི། བདག་གི་སྡུག་བསྔལ་ཆེན་པོ་ལའོ། །

[Block 5362]
སྙིང་རྗེ་ཅན་ནི་གནོད་པ་བྱེད་པ་ལའོ། །

[Block 5363]
དཀའ་ཐུབ་ཀྱི་ནགས་སུ་བདག་ཉིད་ལ་སྡུག་བསྔལ་ཆེན་པོ་འབྱུང་བ་ནི་བཟོད་པ༌[^3428]ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 5364]
དེ་ཉིད་ཀྱི་སྡུག་བསྔལ་གྱིས་གནོད་པར་གྱུར་པ་ནི། སྙིང་རྗེའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5365]
དེ་མ་ཐག་ཏུ་རིམས་ནད་ཅེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་ཡན་ལག་བཅད་མ་ཐག་ཉིད་དུའོ། །

[Block 5366]
ནགས་ཚལ་ཉེ་བའི་ནང་ནས་ཐ་མར་བྱུང་། །ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་བདག་ཉིད་ཆེན་པོ་དེའི་མངོན་སུམ་ནས་ཏེ། དེ་མ་ཐག་ཏུ་སོང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5367]
བླུན་ཞིང་ཞེས་བྱ་བ་ནི་གཏི་མུག་གི་རྒྱུས་སོ། །

[Block 5368]
ལྷག་པར་མི་བརྟན་པ་གང་ཡིན་པ་དེ་ནི། རབ་ཏུ་མི་བརྟན་པ་སྟེ་དེས་ན་མི་བརྟན་པ་དེས་སོ། །

[Block 5369]
བུད་མེད་དང་བྱིས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་སྙིང་རྗེའི་གནས་སོ། །

[Block 5370]
བྲམ་ཟེ་ཡོན་ཏན་གྱི་ཞིང་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5371]
འཆི་བ་དང་། ན་བའི་སྡུག་བསྔལ་ཅན་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་ལ་མྱ་ངན་བྱེད་མོད། ག་ལ་ཁྲོ་ཞེས་བྱ་བ་ཡིན་ཏེ། འཆི་བ་དང་། ན་བའི་སྡུག་བསྔལ་ཞེས་བྱ་བས་ནི། སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5372]
འདོད་ཆགས་ཞེ་སྡང་དབང་དུ་གྱུར། །ཞེས་བྱ་བས་ནི་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5373]
ཉེས་པར་སྤྱོད་པས་ཚིག་པ་ལ། །ཞེས་བྱ་བ་འདིས་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5374]
བདག་ལ་རྣམ་པར་སྨིན་པར་གྱུར་ཀྱང་རུང་སྟེ། དེ་ལ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་བསྒྲུབ་པའི་ཕྱིར། བདེ་བ་ཅན་ལ་སྡུག་བསྔལ་རྗེས་འབྲང་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འོག་མ་སྨོས་སོ། །

[Block 5375]
སྐྱོབ་པར༌[^3429]མ་ནུས་པ་ཞེས་བྱ་བ་ནི་ལས་བདག་གིར་བྱ་བའི༌[^3430]ཕྱིར་རོ། །

[Block 5376]
རྒྱལ་པོ་གྲོངས་ནའང་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་ཉི་ཚེར་མ་ཟད་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5377]
སྐྱེས་ན་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཡོད་ན་ཞེས་བྱ་བའོ། །

[Block 5378]
དེ་བས་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཡོད་ན་སྡུག་བསྔལ་ཡོད་པའི་ཕྱིར་ཏེ། སྐྱེ་བ་ནི་སྡུག་བསྔལ་གྱི་རྩ་བ་ཡིན་པའི་ཕྱིར། སྐྱེ་བ་ཉིད་ལ་འཁོན་དུ་གཟུང་བའི་རིགས་ཏེ། སྐྱེ་བ་མེད་ན་སྡུག་བསྔལ་མེད་པའི་ཕྱིར་རོ། །

[Block 5379]
སྐྱེ་བ་ཡོད་ན་ནི་སྡུག་བསྔལ་མྱོང་བ་ཡིན་ཏེ། བཟོད་པ་མི་བྱེད་པ་མ་ཡིན་པའི་རྒྱུའི་དབང་དུ་བྱས་ནས། ནགས་ན་གནས་ཤིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། ནགས་ན་གནས་ཞེས་བྱ་བས་ནི་ཡོངས་སུ་བཟུང་བ་ཐམས་ཅད་སྤངས་པར་སྟོན་ཏོ། །

[Block 5380]
རབ་ཏུ་འབྱུང་བར༌[^3431]ཤེས་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པ་ལ་དམ་བཅས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5381]
རབ་ཏུ་བྱུང་བ་རྣམས་ནི་བཟོད་པའི་སྟོབས་ཡོད་པའི་ཕྱིར་དང་། བཟོད་པ་སྨྲ་ལ༌[^3432]ཞེས་གཞན་དག་ལ་བཟོད་པའི་མན་ངག་སྟོན་པ་ཉིད་དེ། འདི་གཉིས་ཀྱིས་རབ་ཏུ་བྱུང་བ་རྣམས་ནི་བཟོད་པའོ། །

[Block 5382]
ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པས་ཀྱང་མི་བཟོད་པའི་རྣམ་པ་མེད་པར་སྟོན་ཏོ། །

[Block 5383]
རིང་པོར་མི་ཐོགས་འཆི་ཞེས་བྱ་བ་འདིས་ནི། འཇིག་རྟེན་ཕ་རོལ་དང་ཉེ་བ་ཉིད་པས་མི་བཟོད་པའི་འབྲས་བུའི་རྐྱེན་བྱུང་བར་ཉེ་བའི་ཕྱིར་རོ། །

[Block 5384]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས༌[^3433]བཟོད་པར༌[^3434]སྨྲ་བའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5385 [HEADING]]
## ཚངས་པའི་སྐྱེས་པའི་རབས། ^31-0

[Block 5386]
ཁ་ན་མ་ཐོ་བ་ནི་རབ་ཏུ་སྨད༌[^3435]པར་བྱ་བའོ། །

[Block 5387]
ཡུལ་གྱི་བདེ་བ་ཙམ་གྱི་ཚོད་ཀྱིས༌[^3436]ཀྱང་། །ཞེས་བྱ་བས་ནི་ངན་ངོན་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5388]
ཡུལ་གྱི་བདེ་བ་ནི་བསགས་པ༌[^3437]དང་། བསྲུང་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་མོང་པོའི༌[^3438]དབེན༌[^3439]དུ་གྱུར་པའི་ཕྱིར། ཡུལ་གྱི་བདེ་བ་ཙམ་ཞེས་བྱའོ།[^3440] །འཇིག་རྟེན་རྣམས་ནི་བག་མེད་དབང་དུ་གྱུར། །ཅེས་བྱ་བ་ནི་རང་གི་བདེ་བ་ཡང་མི་སྒྲུབ་པས་སོ། །

[Block 5389]
བསམ་གཏན་བདེ་པས་ཀྱང་ཞེས་བྱ་བས་ཀྱང་བསམ་གཏན་གྱི་བདེ་བ་ཁྱད་པར་དུ་འཕགས་པ་དེས་ཀྱང་ངོ་། །དེའི་ཁྱད་པར་དུ་འཕགས་པ་དེས་ནི་ཅིག་ཤོས་རྣམ་པར་བཅད་པ་ཡིན་ཏེ། བསགས་པ་ལ་སོགས་པའི་ཉེས་པ་དང་བྲལ་བའི་ཕྱིར་དང་། མཐར་ཡང་བདེ་འགྲོར་འགྲོ་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 5390]
གང་ན་གནོད་སེམས་མང་བའི་ཁམས་དང་། རྣམ་པར་འཚེ་བ་མང་བའི་ཁམས་དང་། འདོད་པ་མང་པའི་ཁམས་དེ་ནི། གནོད་སེམས་དང་། འཚེ་བ་མང་བ་འདོད་པའི་ཁམས་ཏེ། དེ་ལ་བལྟས་ནའོ།[^3441] །བཤེས་གཉེན་ངན༌[^3442]པ་ལ་བརྟེན་པའི༌[^3443]སྐྱོན་གྱིས་ཞེས་བྱ་བས་ནི། གཞན་གྱི་སྒྲའི་དྲིང་ལ་འཇོག་པར་བསྟན་ཏོ། །

[Block 5391]
ཡང་དག་པ་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལ་འདྲིས་པས་ཞེས་བྱ་བས་ནི་སྐྱོན་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཉིད་སྟོན་ཏོ། །

[Block 5392]
ལོག་པར་ལྟ་བ་སྟུག་པོའི་ཞེས་བྱ་བ་ནི་ལོག་པར་ལྟ་བ་ཡོངས་སུ་མ་བརྟགས་པའི༌[^3444]ཕྱིར། གཉི་གའི་རྐྱེན་ཅན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5393]
དགེ་བ་དང་མི་དགེ༌[^3445]བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི། འཇིག་རྟེན་ཕ་རོལ་གྱི་བླ་ན་མེད་པའི་ཕྱིར། དགེ་བ་དང་། མི་དགེ་བའི་འབྲས་བུ་རྣམ་པར་སྨིན་པ་ག་ལ་ཡོད་དེ། [^3446]འཇིག་རྟེན་ཕ་རོལ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 5394]
ཆོས་ལ་སྤྱོད་པའི་སྤྲོ་བ་མེད་པ་གང་ཡིན་པ་དེ་ནི་དེའོ། །

[Block 5395]
འདི་ནི་ལྷ་ཁང་དང་། གཙུག་ལག་ཁང་དང་། ཀུན་དགའ་ར་བ་དང་། རྫིང་བུ་ལ་སོགས་པ་བྱེད་པའི་སྤྲོ་བ་མེད་པའོ། །
--- END BLOCKS ---
