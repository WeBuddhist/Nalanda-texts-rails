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
རིགས་བརྒྱའི་དབྱེ་བ་ནི་གཟུགས་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 492]
ཚོར་བའི་ཕུང་པོའི་ཚོགས་ནི་རིན་ཆེན་འབྱུང་ལྡན་ནོ། །

[Block 493]
འདུ་ཤེས་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་འོད་དཔག་ཏུ་མེད་པའོ། །

[Block 494]
འདུ་བྱེད་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་དོན་ཡོད་གྲུབ་པའོ། །

[Block 495]
རྣམ་པར་ཤེས་པའི་ཕུང་པོའི་ཚོགས་ནི་མི་བསྐྱོད་པའོ། །

[Block 496]
དེ་རྣམས་རེ་རེ་རིགས་ལྔའི་དབྱེ་བས་ཉི་ཤུ་རྩ་ལྔར་འགྱུར་རོ། །

[Block 497 [VERSE]]
ས་ནི་སངས་རྒྱས་སྤྱན་ཡིན་ཏེ། །
ཆུ་ཁམས་མཱ་མ་ཀཱི་རུ་བཤད། །
གཟི་བརྗིད་གོས་དཀར་མོ་ཡིན་ཏེ། །
རླུང་ནི་དམ་ཚིག་སྒྲོལ་མར་བཤད། །

[Block 498]
དེ་རྣམས་རེ་རེ་རིགས་ལྔ་ལྔའི༌[^352]དབྱེ་བས་ཉི་ཤུར་འགྱུར་རོ། །

[Block 499 [VERSE]]
རྡོ་རྗེ་སྐྱེ་མཆེད་འདི་དག་ཀྱང་། །
བྱང་ཆུབ་སེམས་དཔའི་དཀྱིལ་འཁོར་མཆོག །

[Block 500]
ཅེས་བྱ་བས་མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་རེ་རེའང་རིགས་ལྔ་ལྔའི་དབྱེ་བས་ཉི་ཤུ་རྩ་ལྔར་ཤེས་པར་བྱའོ། །

[Block 501]
ཡུལ་གྱི་ལྷ་མོ་རྣམས་རེ་རེ་རིགས་ལྔ་ལྔའི་དབྱེ་བས་ཉི་ཤུ་རྩ་ལྔའོ། །

[Block 502]
ཁྱབ་པར་བྱེད་པ་ཡེ་ཤེས་ལྔ་ནི་རིགས་བརྒྱའི་བྱེ་བྲག་གོ། །

[Block 503]
ཇི་སྐད་དུ།

[Block 504 [VERSE]]
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་རྣམས་ལ་ནི། །
ལྔ་པོའི་དབྱེ་བས་ལྔ་རུ་བྱས་པ་ལ། །
དེ་བཞིན་གཤེགས་པས་སོ་སོར་བྱིན་གྱིས་བརླབས།[^353] །
 འཁོར་བའི་ལས་རྣམས་དག་ནི་གང་ལས་འབྱུང་།[^354] །

[Block 505 [VERSE]]
དེ་བཞིན་དབང་པོ་ཕྱི་རོལ་ཡུལ་བཅས་ལྔ། །
རེ་རེ་ཞིག་ཀྱང་བདེ་གཤེགས་ལྔ་རྣམས་ཀྱིས། །
དེ་ལ་རང་རང་རྟག་ཏུ་བྱིན་རློབ༌[^355]ཅིང་། །
ཡེ་ཤེས་ལྔ་དང་གསུམ་དུ་ཡང་དག་གནས། །

[Block 506]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ་ཡང་།

[Block 507 [VERSE]]
རིགས་ནི་རྣམ་པ༌[^356]བརྒྱར་བཤད་པ། །
མདོར་བསྡུས་པ་ནི་རྣམ་པ་ལྔ། །
ལུས་ངག་ཡིད་ཀྱི་དབྱེ་བ་ཡིས། །
ཕྱིས་ནི་རྣམ་པ་གསུམ་དུ་འགྱུར། །

[Block 508]
ཞེས་འབྱུང་བས་སོ། །

[Block 509]
རིགས་བརྒྱའི་དབྱེ་བས་ལྷའི་གཟུགས་སུ་ལུས་རྣམ་པར་དབེན་པར་བྱས་ལ། ཐམས་ཅད་སྟོང་པའི་རང་བཞིན་དེ་ཁོ་ན་ཉིད་རྣལ་འབྱོར་པས་མངོན་དུ་བྱེད་དེ། དེ་ཅིའི༌[^357]ཕྱིར་ཞེ་ན། རིགས་བརྒྱ་པོ་གང་བཤད་པ་དེ་མདོར་བསྡུས་པས་ལྔ་རུ་འགྱུར་ཏེ་ཕུང་པོ་ལྔ་དང་ཉོན་མོངས་པ་ལྔ་དང་འབྱུང་བ་ཆེན་པོ་ལྔ་དང་ཡེ་ཤེས་ལྔས་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 510]
རིགས་ལྔ་པོ་དེ་ཡང་སླར་ཡང་གསུམ་དུ་འགྱུར་ཏེ། སྐུ་དང་གསུང་དང་ཐུགས་ཀྱིས་སོ། །

[Block 511]
རིན་ཆེན་དང་དོན་ཡོད་པའི་རིགས་དག་ནི་སྐུའི་རིགས་དང་གསུང་ངམ་ཐུགས་ཀྱི་རིགས་སུ་བསྡུ་བར་བྱའོ། །

[Block 512]
དེ་ལ་ང་རྒྱལ་གྱི་ངོ་བོ་ཉིད་རིན་ཆེན་འབྱུང་ལྡན་ནི་གཏི་མུག་ལས་འབྱུང་བའི་ཕྱིར་སྐུའི་རིགས་སུ་བསྡུ་བར་བྱའོ། །

[Block 513]
དོན་ཡོད་གྲུབ་པ་ཕྲག་དོག་གི་ངོ་བོ་ཉིད་ནི་འདོད་ཆགས་སམ་ཞེ་སྡང་ལས་འབྱུང་བའི་ཕྱིར་འདོད་ཆགས་ཀྱི་རིགས་སམ་ཞེ་སྡང་གི༌[^358]རིགས་སུ་བསྡུའོ། །

[Block 514]
རིགས༌[^359]གསུམ་པོ་དེ་གཅིག་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 515]
གང་གི་ཕྱིར་ལུས་དང་ངག༌[^360]ནི་ཐུགས་ཀྱི་རྡོ་རྗེ་ལ་བསྡུ་བ་ཡིན་ཏེ་སྣང་བ་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 516]
སེམས་དེ་ཡང་སྣང་བ་དང་སྣང་བ་མཆེད་པ་དང་སྣང་བ༌[^361]ཉེ་བར་ཐོབ་པའི་དབྱེ་བས་དཔྱད་པ་ན་ཐམས་ཅད་སྟོང་པའི་ངོ་བོ་ཉིད་དུ་འགྱུར་ཏེ། ཇི་སྐད་དུ། སྟོང་པའི་ཆོས་ལས་སྟོང་པའི༌[^362]ཆོས་རྣམས་འབྱུང་། །ཞེས་སློབ་དཔོན་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་ཀྱིས་གསུངས་སོ། །

[Block 517]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 518 [VERSE]]
ཇི་ལྟར་ཆུ་ཀླུང་དངས་པ༌[^363]ལས། །
ཉ་དག་མྱུར་དུ་ལྡང་གྱུར་ཏེ། །
དེ་བཞིན་ཐམས་ཅད་སྟོང་གསལ་ལ། །
སྒྱུ་འཕྲུལ་དྲ་བ་འབྱུང་བར་འགྱུར། །

[Block 519]
ཞེས་འབྱུང་ངོ་། །རིགས་བརྒྱའི་དབྱེ་བ་བསྒོམ་པའི་རིམ་པ་འདིས། །རྣལ་འབྱོར་པ་ཕྱིར་མི་ལྡོག་པའི༌[^364]ས་བརྒྱད་པ་ལ་གནས་པར་འགྱུར་རོ། །

[Block 520 [HEADING]]
#### དང་པོ་རྡོ་རྗེ་བཟླས་པ། ^1-2-1-0

[Block 521]
དེ་ལྟར་བསྐྱེད་པའི་རིམ་པ་ལ་མཐར་ཕྱིན་ནས་རྫོགས་པའི་རིམ་པའི༌[^365]

[Block 522]
དང་པོ་རྡོ་རྗེ་བཟླས་པ༌[^366]ལ་གོམས་པར་བྱའོ། །

[Block 523]
དེ་ལ་དང་པོ་རླུང་གི་དེ་ཁོ་ན་ཉིད་ལ་དམིགས་ནས་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ལ་དམིགས་པར་རོ། །

[Block 524 [HEADING]]
##### དང་པོ་རླུང་གི་དེ་ཁོ་ན་ཉིད། ^1-2-1-1-0

[Block 525]
རླུང་གི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བ་ནི་གདོང་གི་སྣ་ལ་སོགས་པར་གནས་པའི་ཡུངས་ཀར་ཕྲ་མོ་ཙམ་གྱི་ཐིག་ལེ་བསྒོམ་པའོ། །

[Block 526]
གང་གི་ཕྱིར་རླུང་ནི་ལུས་ཐམས་ཅད་ལ་ཁྱབ་པ་དང་། ལས་ཐམས་ཅད་བྱེད་ཅིང་སྲོག་ཆགས་ཐམས་ཅད་ཀྱི་སྲོག་ཏུ་གྱུར་པ་རྣམ་ཤེས་ཀྱི་བཞོན་པ་གཅིག་པུ་ཁོ་ནའོ། །

[Block 527]
དེ་ཡང་ཕུང་པོ་ལྔའི་དབྱེ་བས་ལྔ་རུ་འགྱུར་ཏེ། སྲོག་དང་། ཐུར་དུ་སེལ་བ་དང་། མེ་དང་མཉམ་པ་དང་། གྱེན་དུ་རྒྱུ་བ་དང་། ཁྱབ་པའོ། །

[Block 528]
དེ་ལ་སྲོག་ནི་ལྟེ་བ་ལ་གནས་ཤིང་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་མངོན་པར༌[^367]སྐྱེད་པར་བྱེད་པའི་ལས་ཅན་ནོ། །

[Block 529]
ཐུར་དུ་སེལ་བ་ནི་བཤང་ལམ་ལ་གནས་ཤིང་ཚོར་བའི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^368]ལས་ཅན་ནོ། །

[Block 530]
གྱེན་དུ་རྒྱུ་བ༌[^369]ནི་མགྲིན་པ་ལ་གནས་ཤིང་འདུ་ཤེས་ཀྱི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^370]ལས་ཅན་ནོ། །
--- END BLOCKS ---
