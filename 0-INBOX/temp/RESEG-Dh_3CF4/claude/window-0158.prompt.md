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
[Block 5531]
བསྲེགས་པ་ནི་མེ་འམ། རྫ་མ་ཆེན་པོའི་ནང་དུ་བཅུག་སྟེ། བཙོ་བ༌[^3526]ལ་སོགས་པས་སོ། །

[Block 5532 [VERSE]]
གཞོག་པ་ནི་སྟེའུ་ལ་སོགས་པས་སོ། །
བརྡུང་བ་ནི་བན་གླང་ལ་སོགས་པ་དང་།
བསྡུས་འཇོམས་ཀྱི༌[^3527]རི་བོ་ལ་སོགས་པས་སོ། །
གཞིག་པ་ནི༌[^3528]མདུང་ཐུང་ལ་སོགས་པས་སོ། །

[Block 5533]
གནོད་པ་མང་པོས་སྡུག་བསྔལ་བ་སྟེ། དེ་ལྟར་བཤད་པ་དག་ལས་མ་གྲོལ་བ་ཡིན་ན། ཇི་ལྟར་ངལ་བུ་ལོན་གཞལ་བའོ། །

[Block 5534]
དེ་དག་བདག་གིས་ཞེས་བྱ་བས་ནི་བསད་པ་ལ་སོགས་པས་སོ། །

[Block 5535]
དགེ་བ་དག་གི་གནས་ནི་དགེ་བའི་གནས་སོ། །

[Block 5536]
ཡང་ན་དགེ་བའི་གནས་གང་ཡིན་པ་དེ་ནི་དགེ་བའི་གནས་སོ། །

[Block 5537]
གནོད་པ་མང་པོས༌[^3529]ཡིད་མི་དགའ་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི༌[^3530]དམྱལ་བའི་གཏམ་ཐོས་པས་སོ། །

[Block 5538]
ལྟ་བ་དྲང་པོར་གྱུར་ནས་ཞེས་བྱ་བ་ནི་དེ་སྨད་པར་བྱ་བའི་ལོག་པའི་ལྟ་བ་ཡོངས་སུ་བཏང་བས་སོ། །

[Block 5539]
ཆོས་སྒྲུབ་པའི༌[^3531]སྣོད་ཅེས་བྱ་བ་ནི་མྱ་ངན་ལས་འདས་པའི་ལམ་སྒྲུབ་པའི༌[^3532]སྣོད་དོ། །

[Block 5540]
ཡང་ན་ཆོས་ནི་བསོད་ནམས་ཀྱི་ཆོགས་ཏེ། དེ་སྒྲུབ་པའི་སྣོད་དོ། །

[Block 5541]
སྔོན་གྱི་རྒྱལ་པོ་ཡོན་ཏན་དགའ་བ་རྣམས། །ཞེས་བྱ་བ་ཕྱེད་དང་པོ་འདིས༌[^3533]ནི་ཡོན་ཏན་གྱི་ཞིང་སྒྲུབ་པ༌[^3534]ཉིད་བསྟན་ཏོ། །

[Block 5542]
འབངས་ལ་ངང་ཚུལ་སྙིང་རྗེ་ལྡན་བརྟན་པ། ། ཞེས་བྱ་བ་འདིས་ནི་སྙིང་རྗེའི་ཞིང་སྒྲུབ་པ༌[^3535]ཉིད་བསྟན་ཏོ། །

[Block 5543]
གྲགས་ལྡན་ཞེས་བྱ་བས་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་ཡིན་ནོ། །

[Block 5544]
མཐོ་རིས་འགྲོ་ཞེས་བྱ་བ་འདི་ནི། འཇིག་རྟེན་ཕ་རོལ་གྱི་ཡོན་ཏན་ནོ། །

[Block 5545]
དེ་བས་ན་ཆོས་མིན་ཐུབ་དཀའ་ཐུབ་བྱེད་ཅིང་ཞེས་བྱ་བ་འདིས་ནི་ཚུལ༌[^3536]ཁྲིམས་ཀྱི་བསོད་ནམས་ཀྱི་ཚོགས་བསྟན་ཏེ། ཆོས་མ་ཡིན་པའི་མི་མཐུན་པའི་ཕྱོགས་ལས་ཆོས་ཀྱིས༌[^3537]རྒྱལ་བར་བྱེད་དོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 5546]
སེར་སྣ་ནི་ཆགས་པ་སྟེ། དེ་མེད་པ་ནི་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཏེ་གཉེན་པོ་ཡིན་ནོ། །

[Block 5547]
དེ་རིང་དུ་སྤངས་པ་ནི་གཉེན་པོ་ཡིན་པའི་ཕྱིར། སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5548]
རིན་ཆེན་མཆོག་འབར་ཞེས་བྱ་བ་དེས་འགྲོ་བས་སོ། །

[Block 5549]
ཡང་དག་པའི་ལྟ་བ་ལ་འདྲིས་པ་ནི༌[^3538]གོམས་པའོ། །

[Block 5550]
གནས་པ་ནི་བརྟེན༌[^3539]པའོ། །

[Block 5551]
བློ་ནི་འདོད་པའོ། །

[Block 5552]
བྱིས་པ་དག་ཆགས་པར་བྱེད་པས༌[^3540]ནི་བྱིས་པ་དགའ་བར་བྱེད་པ་སྟེ། བྱིས་པ་དགའ་བར་བྱེད་པ་ངེས་སོ། །

[Block 5553]
ཆོས་ཉིད་ངེས་པ་ཞེས་བྱ་བ་ནི༌[^3541]ཆོས་ལ་ངེས་པའོ། །

[Block 5554]
[^3542]ཡང་དག་པའི་ལྟ་བ༌[^3543]ཡང་ཡིན་ལ། དགེ་བ་ཡང་ཡིན་པས་ཡང་དག་ལྟ་བ༌[^3544]དགེ་བའོ། །

[Block 5555]
ཡང་དག་པའི་ལྟ་བ་དགེ་བ་དེས། ད་ནི་ཞེས་བྱ་བ་ནི་ཕྱིན་ཆད་དོ། །

[Block 5556]
འགྲོ་བར་སྤྲོ་བ་ནི་འགྲོ་བར་འདོད་པའོ། །

[Block 5557]
ཡོན་ཏན་དག་ལ་རྩུབ་པ་ནི། ཡོན་ཏན་དག་ལ་མི་དགའ་བ་སྟེ། མི་དགའ་བ་ནི་སྐྱོ༌[^3545]བའོ། །

[Block 5558]
ལམ་དུ་གྱུར་པའི་གོ་འཕང་དེས། ལམ་དུ་བྱས་པ་ཡིན་པས་ལམ་དུ་གྱུར་པའོ། །

[Block 5559]
གོ་འཕང་ནི་ལམ་དུ་གྱུར་པའི་རབ་ཏུ་གནས་པའོ། །

[Block 5560]
ཡོན་ཏན་སྒྲུབ་པ༌[^3546]དབྱིག་ཏུ་བྱོས། །ཞེས་བྱ་བ་འདིས་ནི། སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 5561]
བདག་དང་གཞན་ལ་ཕན་འདོགས་ཞེས་བྱ་བ་འདིས་ནི།

[Block 5562 [VERSE]]
བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །
ཚུལ་ཁྲིམས་བརྟན་ཞིང་དབང་པོ་རབ་ཏུ་སྡོམས། །

[Block 5563]
ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 5564]
རབ་གསལ་ཞེས་བྱ་བ་ནི་ནུས་པ་ཆེ་བས་སོ། །

[Block 5565]
ཡིད་དུ་འོང་བས་ནི་ཡིད་ཀྱི་ནུས་པ་ཉིད་དོ། །

[Block 5566]
གྲགས་པ་ནི་སྙན་པའི་ཕན་པ་དང་ལྡན་པའི་འགྲོ་བའི་སྡུག་བསྔལ་བསལ༌[^3547]བའོ། །

[Block 5567]
དེ་ཡང་ཤིང་རྟ་ཡོད་པ་དེ་ནི་ཤིང་རྟ་དག་གོ། །

[Block 5568]
བཀུར་སྟི་ཉིད་སྦྱིན་པའི་ཤིང་རྟ་གང་ཡིན་པ་དེ་ནི་བཀུར་སྟི་སྦྱིན་པའི་ཤིང་རྟ་སྟེ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་ཤིང་རྟ་དག་གོ། །

[Block 5569]
ཡོན་ཏན་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་སྐྱེ་བ་ཡིན་པས་ཡོན་ཏན་འབྱུང་བ་སྟེ། དེ་ནི་ཤིང་རྟ་ཉིད་དེ་རང་གི་ལུས་སོ། །

[Block 5570]
མི་རྩུབ་པའི་མིག་དང་ལྡན་པ་གང༌[^3548]ཡིན་པ་དེ་ནི་མི་རྩུབ་མིག་ལྡན་ཏེ། མི་རྩུབ་པའི་བྱམས་པའོ། །
--- END BLOCKS ---
