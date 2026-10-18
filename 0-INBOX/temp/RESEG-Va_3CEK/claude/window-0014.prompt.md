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
[Block 491]
ལུས་ཀྱི༌[^349]གཡོ་ལས་སྐྱེས་པ་ནི་གྱ་གྱུའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་ཡོན་པོ་ཞེས་བཤད་དེ་ངག་དང་ཡིད་ཀྱི་ཡོན་པོ་ཡང་དེ་དང་འདྲའོ། །

[Block 492]
ལུས་ཀྱི་ལས་ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་སྡང་བའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་ཉེས་པ་ཞེས་བཤད་དེ། ངག་དང་ཡིད་ཀྱི་ཉེས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 493]
ལུས་ཀྱི་ལས་འདོད་ཆགས་ལས་སྐྱེས་པ་ནི་ཆགས་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་སྙིགས་མ་ཞེས་བཤད་དེ། ངག་དང་ཡིད་ཀྱི་སྙིགས་མ་ཡང་དེ་དང་འདྲའོ། །

[Block 494 [HEADING]]
### དཀར་ནག་ལ་སོགས་པའི་ལས་རྣམ་པ་བཞི། ^1-34-0

[Block 495 [VERSE]]
དཀར་ནག་ལ་སོགས་བྱེ་བྲག་གིས། །
ལས་ནི་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 496]
གནག་ལ་རྣམ་པར་སྨིན་པ་གནག་པའི་ལས་ཀྱང་ཡོད། དཀར་ལ་རྣམ་པར་སྨིན་པ་དཀར་བའི་ལས་ཀྱང་ཡོད། དཀར་གནག་ལ་རྣམ་པར་སྨིན་པ་དཀར་གནག་པའི་ལས་ཀྱང་ཡོད། མི་དཀར་མི་གནག་ཅིང་རྣམ་པར་སྨིན་པ་མེད་པ་ལས༌[^350]ཟད་པར་བྱེད་པའི་ལས་ཀྱང་ཡོད་དེ། དེ་ལ། མི་དགེ་གཟུགས་དང་འདོད་གཏོགས་པའི།[^351] །

[Block 497 [VERSE]]
དགེ་བ་ཉིད་ནི་རིམ་བཞིན་དུ། །
གནག་དང་དཀར་དང་གཉི་གའི་ལས། །

[Block 498]
དེ་ཟད་བྱེད་པ་ཟག་མེད་ཡིན།[^352] །ལས་མི་དགེ་བ་ནི་ཉོན་མོངས་པ་ཅན་ཡིན་པའི་ཕྱིར་གཅིག་ཏུ་གནག་པ་ཡིན་ལ། རྣམ་པར་སྨིན་པ་ཡིད་དུ་མི་འོང་བའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡང་གནག་པ་ཡིན་ནོ། །

[Block 499]
གཟུགས་སུ་གཏོགས་པའི་དགེ་བ་ནི། །མི་དགེ་བ་དང་མ་འདྲེས་པའི་ཕྱིར་གཅིག་ཏུ་དཀར་བ་ཡིན་ལ། རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡང་དཀར་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་གཟུགས་མེད་པར་གཏོགས་པ་མ་བཤད་ཅེ་ན། གང་ན་རྣམ་པར་སྨིན་པ་རྣམ་པ་གཉིས་པོ་སྲིད་པ་བར་མ་པ་དང་། སྐྱེ་བའི་སྲིད་པ་ཡང༌[^353]ཡོད་པ་དང་། ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་རྣམ་པ་གསུམ་ཆར་གྱི་ཡོད་པ་དེ་ཁོ་ནར་བཤད་དོ་ཞེས་གྲག་སྟེ། མདོ་གཞན་ལས་དེ་ཡང་བཤད་དོ། །

[Block 500]
འདོད་པར་གཏོགས་པའི་དགེ་བ་ནི་མི་དགེ་བ་དང་འདྲེས་པའི་ཕྱིར་དཀར་གནག་ཡིན་ལ། རྣམ་པར་སྨིན་པ་འདྲེས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡང་དཀར་གནག་ཡིན་ནོ། །

[Block 501]
འདི་ནི་རྒྱུད་ཀྱི་སྒོ་ནས་རྣམ་པར་གཞག་གི་ངོ་བོ་ཉིད་ཀྱི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། ལས་སམ་རྣམ་པར་སྨིན་པ་གཅིག་ལ་དཀར་པོ་ཡང་ཡིན། ནག་པོ་ཡང་ཡིན་པས༌[^354]དེ་ལྟ་བུ་ནི་མེད་དོ། །

[Block 502]
[^355]ཕན་ཚུན་འགལ་བའི་ཕྱིར་རོ། །

[Block 503]
དེ་ལྟ་ན༌[^356]མི་དགེ་བ་ཡང་དགེ་བ་དང་འདྲེས་པའི་ཕྱིར། [^357]དཀར་གནག་ཏུ་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། འདོད་པའི་ཁམས་ནི་མི་དགེ་བ་གདོན་མི་ཟ་བར་དགེ་བ་དང་འདྲེ་བ་ནི་མ་ཡིན་ཏེ། དེ་སྟོབས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 504]
དགེ་བ་ནི་སྟོབས་ཆུང་བའི་ཕྱིར་འདྲེ་བར་འགྱུར་རོ། །

[Block 505]
ཟག་པ་མེད་པའི་ལས་ནི་ལས་གསུམ་པོ་དེ་དག་ཟད་པར་བྱེད་ཅིང་སྤོང་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 506]
དེ་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་མི་གནག༌[^358]པའོ། །

[Block 507]
རྣམ་པར་སྨིན་པ་དཀར་པོ་ཉིད་མེད་པའི་ཕྱིར་མི་དཀར་བའོ། །

[Block 508]
མི་དཀར་བ་ཞེས་བྱ་བའི་སྒྲ་འདི༌[^359]ནི་དགོངས་པ་ཅན་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་སྟོང་པ་ཆེན་པོའི་མདོ་ལས་མི་སློབ་པའི་ཆོས་ལས་བརྩམས་ཏེ། ཀུན་དགའ་བོ་ཆོས་འདི་དག་ནི་གཅིག་ཏུ་དཀར་བ་གཅིག་ཏུ་དགེ་བ། གཅིག་ཏུ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 509]
བསྟན་བཅོས་ལས་ཀྱང་། ཆོས་དཀར་པོ་རྣམས་གང་ཞེ་ན། དགེ་བའི་ཆོས་རྣམས་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་རྣམས་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །འཇུག་པ་དང་འགལ་བས་ཁམས་སུ་མ་གཏོགས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །

[Block 510 [HEADING]]
### ལས་རྣམ་པ་གསུམ་པོ་ཟད་པར་བྱེད་པ། ^1-35-0

[Block 511]
ཅི་ཟག་པ་མེད་པའི་ལས་དང་ལས་ཐམས་ཅད་ལས་རྣམ་པ་གསུམ་པོ་འདི་དག་ཐམས་ཅད་ཟད་པར་བྱེད་པ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 512]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 513 [VERSE]]
ཆོས་བཟོད་འདོད་ཆགས་བྲལ་བ༌[^360]ཡི། །
བར་ཆད་མེད་ལམ་བརྒྱད་ཀྱི་གང་། །
སེམས་པ༌[^361]རྣམ་པ་བཅུ་གཉིས་དེ། །
ནག་པོ་ཟད་པར་བྱེད་པའི་ལས། །

[Block 514]
མཐོང་བའི་ལམ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་བཞི་དང་། འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་བར་ཆད་མེད་པའི་ལམ་བརྒྱད་ཀྱི་སེམས་པ་གང་ཡིན་པ་སྟེ། སེམས་པ༌[^362]རྣམ་པ་བཅུ་གཉིས་པོ་དེ་ནི་ནག་པོའི་ལས་ཟད་པར་བྱེད་པའི་ལས་ཡིན་ནོ། །

[Block 515 [VERSE]]
དགུ་པའི་སེམས་པ་གང་ཡིན་པ། །
དེ་ནི་དཀར་ནག་ཟད་བྱེད་ཡིན། །

[Block 516]
འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ༌[^363]ལས་བར༌[^364]ཆད་མེད་པའི་ལམ་དགུ་པའི་སེམས་པ༌[^365]གང་ཡིན་པ་དེ་ནི་དཀར་གནག་སྟེ་དགེ་བ་དང་མི་དགེ་བ་ནག་པོ་རྣམ་པ་དགུ་པོ་སྤོང་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 517 [VERSE]]
དཀར་པོ་བསམ་གཏན་ཆགས་བྲལ་ལ། །
བར་ཆད་མེད་ལམ་སྐྱེས་ཐ་མས། །

[Block 518]
བསམ་གཏན་དང་བསམ་གཏན་ལས་འདོད་ཆགས་དང་བྲལ་བར༌[^366]བྱེད་པའི་བར་ཆད་མེད་པའི་ལམ་ཐ་མ་དགུ་པ་དེའི་སེམས་པ་གང་ཡིན་པ་སྟེ། སེམས་པ༌[^367]རྣམ་པ་བཞི་པོ་དེ་ནི་དཀར་པོའི་ལས་སྤོང་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 519]
ཅིའི་ཕྱིར་བར་ཆད་མེད་པའི་ཕྱིར༌[^368]ལམ་ཐ་མ་ཁོ་ནས༌[^369]སྤོང་བར་བྱེད་ལ་གཞན་གྱིས་ནི་མ་ཡིན་ཞེ་ན། དེའི་རང་གི་ངོ་བོ་ནི་སྤོང་བ་མ་ཡིན་ཏེ། སྤངས་ཀྱང་མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 520]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་སྤངས་པའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་ཇི་སྲིད་དུ་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པའི་རྣམ་པ་གཅིག་ཡོད་པ་དེ་སྲིད་དུ་དེ་མི་སྤོང་བ་མི་འཐད་དོ། །

[Block 521]
གཞན་ནི་དམྱལ་བ་མྱོང་འགྱུར་དང་། །འདོད་གཞན་མྱོང་འགྱུར་གཉིས་སུ་རིགས།[^370] །སློབ་དཔོན་གཞན་དག་ནི་དམྱལ་བ་མྱོང་བར་འགྱུར་བ་དང་། དམྱལ་བ་ལས་གཞན་པའི་འདོད་པའི་ཁམས་མྱོང་བར་འགྱུར་བའི་ལས་ནི་རིམ་བཞིན་དུ་ནག་པོ་དང་དཀར་ནག་ཡིན་ཏེ། དམྱལ་བ་ན་ནི་ལས་མི་དགེ་བ་ཁོ་ནའི་རྣམ་པར་སྨིན་པ་ཡོད་པས་དེའི་ཕྱིར་དེ་མྱོང་བར་འགྱུར་བ་ནི་ནག་པོ་ཞེས་བྱའོ། །

[Block 522]
དེ་ལས་གཞན་པའི་འདོད་པའི་ཁམས་ན་ནི་ལས་དགེ་བ༌[^371]དང་མི་དགེ་བའི་རྣམ་པར་སྨིན་པ་ཡོད་པས་དེའི་ཕྱིར་དེ་མྱོང་བར་འགྱུར་བ་ནི་དཀར་ནག་ཅེས་བྱ་བར་ལྟའོ། །

[Block 523]
གཞན་ནི་མཐོང་བས་སྤང་བྱ་གནག །གཞན་དག་ན་རེ་མཐོང་བས་སྤང་བར་བྱ་བའི་ལས་ནི་དགེ་བ་དང་མ་འདྲེས་པའི་ཕྱིར་ནག་པོ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 524]
འདོད་པ་ལས་སྐྱེས་གཞན་དཀར་གནག །འདོད་པ་ན་སྤྱོད་པའི་ལས་གཞན་ནི་དཀར་གནག་ཡིན་ནོ། །

[Block 525]
དེ་ལས་གཞན་པ་ཅི་ཞིག་ཅེ་ན། བསྒོམ་པས་སྤང་བར་བྱ་བ་སྟེ། དེ་ནི་དགེ་བ་ཡང་ཡིན་ལ་མི་དགེ་བ་ཡང་ཡིན་ནོ། །

[Block 526 [HEADING]]
### ཐུབ་པའི་གསུམ། ^1-36-0

[Block 527]
མདོ་ལས་ཐུབ་པའི་ནི་གསུམ་སྟེ། ཐུབ་པའི་ལུས་དང་། ཐུབ་པའི་ངག་དང་། ཐུབ་པའི་ཡིད་ཡོད༌[^372]དོ་ཞེས་གསུངས་པ་དེ་ལ།

[Block 528 [VERSE]]
མི་སློབ་ལུས་ངག་ལས་ཡིད་ཉིད། །
ཐུབ་པའི་གསུམ་སྟེ་གོ་རིམས་བཞིན། །

[Block 529]
མི་སློབ་པའི་ལུས་དང་ངག་གི་ལས་དག་ནི་ཐུབ་པའི་ལུས་དང་ངག་ཡིན་ནོ། །

[Block 530]
མི་སློབ་པའི་ཡིད་ཁོ་ན་ཡིད་ཀྱི་ཐུབ་པ་ཡིན་ཏེ། ཡིད་ཀྱི་ལས་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ནི་དོན་དམ་པར་ཐུབ་པ་ཡིན་ལ། དེ་ནི་ལུས་དང་ངག་གི་ལས་དག་གི་སྒོ་ནས་རྗེས་སུ་དཔག་པར་བྱ་བ་ཡིན་ནོ་ཞེས་གྲག་གོ། །
--- END BLOCKS ---
