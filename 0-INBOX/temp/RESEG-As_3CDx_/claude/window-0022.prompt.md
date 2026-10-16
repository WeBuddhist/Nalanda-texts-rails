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
[Block 771]
དེ་ལ་ཚིགས་སུ་བཅད་པ་དང་པོའི་རྩ་བ་གོང་མ་གཉིས་ནི།

[Block 772 [VERSE]]
ཟབ་མོའི་བྱིས་པའི་སྤྱོད་ཡུལ་མ་ཡིན་པ། །
བརྗོད་མེད་གཉིས་མེད་རྒྱལ་བས་བསྟན་མཛད་ཀྱང་། །

[Block 773]
ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ནི་དོན་དམ་པའི་ཟབ་མོའི་སྤྱོད་ཡུལ་མ་ཡིན་པ༌[^596]བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་ལྡན་པ། རྒྱལ་བ་སྟོབས་བཅུ་དང་ལྡན་པ། ཐུགས་རྗེ་དམ་པ་མངའ་བས་བསྟན་པའི་སྒོ་ནས་མཚན་ཉིད་གཉིས་ཀྱི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེ་གཉིས་ཀྱི༌[^597]རྣམ་པར་བྱང་བའི་ཕྱོགས་ཀྱང་བསྟན་པ་ཡིན་ནོ། །

[Block 774 [HEADING]]
###### ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས། ^4-1-1-4-2-0

[Block 775]
རྩ་བ་གོང་མ་གཉིས་ནི།

[Block 776 [VERSE]]
བྱིས་པ་གཏི་མུག་རྨོངས་པ་འདི་དག་ནི། །
སྨྲ་བའི་སྤྲོས་ལ་དགའ་ཞིང་གཉིས་ལ་གནས། །

[Block 777]
ཞེས་གསུངས་པ་ཡིན་ཏེ། དེས་ནི་བྱིས་པ་གཏི་མུག་གིས་རྨོངས༌[^598]པ་འདི་དག་ནི་དོན་དམ་པས་བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དང་ལྡན་པ་མི་ཤེས་པས་སྨྲ་བའི་སྤྲོས་པ་ལ་དགའ་བ་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་ལྡན་པ་མི་ཤེས་པས་གཉིས་ལ་གནས་པའི་སྒོ་ནས་མཚན་ཉིད་གཉིས་ཀྱིས་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེ་ཉིད་ཀྱི༌[^599]ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ཀྱང་བསྟན་པ་ཡིན་ནོ། །

[Block 778 [HEADING]]
###### ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ལ་གནས་པ་རྣམས་ཀྱི་ཉེས་དམིགས། ^4-1-1-4-3-0

[Block 779]
ཚིགས་སུ་བཅད་པ་གཉིས་པོ་ནི།

[Block 780 [VERSE]]
མ་རྟོགས་པའམ་ལོག་པར་རྟོགས་པ༌[^600]དག །
ལུག་དང་བ་ལང༌[^601]དག་ཏུ་ཡང་སྐྱེ་ཞིང་། །
དེ་དག་ཤེས་པའི་སྨྲ་བ་དེར༌[^602]བོར་ནས། །

[Block 781]
ཤིན་ཏུ་ཡུན་རིང་འཁོར་བ་འདིར་འཁོར་འགྱུར།[^603] །ཞེས་གསུངས་པ་སྟེ། དེས་ནི་བྱིས་པ་གཏི་མུག་གིས་རྨོངས་པའི་དོན་དམ་པ་བརྗོད་དུ་མེད་པ་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་ལྡན་པ་མ་རྟོགས་པ་དང་། ལོག་པར་རྟོགས་པ་དེ་དག་ནི་ལུག་དང་བ་ལང༌[^604]ལ་སོགས་པ་ངན་སོང་གསུམ་པོ་དག་ཏུ་ཡང་དང་ཡང་དུ་སྐྱེ་ཞིང་ཆོས་ཐམས་ཅད་རྣམ་པར་ཤེས་པ་ཙམ་དུ་སྨྲ་བ་དེ་བོར་ནས་ཡུན་རིང་པོར་འཁོར་བ་འདིར་འཁོར་བར་འགྱུར་རོ་ཞེས་བསྟན་ཏེ། དེ་ཉིད་ཀྱིས༌[^605]ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ལ་གནས་པ་རྣམས་ཀྱི༌[^606]ཉེས་དམིགས་བསྟན་པ་ཡིན་ནོ། །

[Block 782]
ལེའུ་དང་པོའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 783 [HEADING]]
#### འཕགས་པ་ཆོས་འཕགས་ཀྱི་ལེའུ། ^4-1-2-0

[Block 784]
དེ་ལྟར་བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ཀྱིས༌[^607]དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་ནས། དེ་ནི་རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་ཀྱིས་དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་འཕགས་ཀྱིས་འདི་སྐད་ཅེས་གསོལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འཕགས་པ་ཆོས་འཕགས་ཀྱི་ལེའུ་གཉིས་པ་འདི་གསུངས་སོ། །

[Block 785]
དེ་ལ་ལེའུ་གཉིས་པ་འདིའི་བསྡུས་པའི་དོན་ནི་མདོར་བསྡུ་ན་རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 786]
དེ་ཡང་རྣམ་པར་དབྱེ་བ་རྣམ་པ་བཞི་སྟེ་རྟོག་གེ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་དང་། དོན་དམ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་དང་། དཔེའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་དང་། དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པའོ། །

[Block 787]
དེ་ལ་རྟོག་གེ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་ནི། བཅོམ་ལྡན་འདས་སྔོན་གྱི་གདུགས་རྣམས་ཀྱི་ཤིན་ཏུ་སྔ་བ་ཞིག་ན་ཞེས་བྱ་བ་ནས། ངོ་མཚར་རྨད་དུ་བྱུང་བ་ལེགས་སོ་སྙམ་བགྱིད་ལགས་སོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 788]
དོན་དམ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་ནི་འདི་སྐད༌[^608]ཅེས་གསོལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་འཕགས་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ནས། ཆོས་འཕགས་དེའི་ཕྱིར་རྣམ་གྲངས་དེས་ཀྱང་ཁྱོད་ཀྱིས་རྟོག་གེའི་སྤྱོད་ཡུལ་ཐམས་ཅད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་གང་ཡིན་པ་ནི་དོན་དམ་པ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་གསུངས་པའི་ཚར་ཐ་མའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 789]
དཔེའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་ནི། ཆོས་འཕགས་འདི་ལྟ་སྟེ་དཔེར་ན་ཞེས་བྱ་བ་ནས། ཆོས་འཕགས་དེ་བཞིན་དུ་རྟོག་གེ་པ་ཐམས་ཅད་ཀྱིས་ཀྱང་དོན་དམ་པ་རྟོག་གེ་ཐམས་ཅད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་ལ་བརྟག་པའམ། རྗེས་སུ་དཔག་པའམ་མོས་པར་མི་ནུས་སོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 790]
དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་མངོན་པར༌[^609]བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་ནི་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་དོན་དམ་པ་རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པའི་ཚིག་གི་དོན་དེ་དག་གི་དངོས་པོ་བསྡུ་བ་བསྟན་པ་དང་སྦྱར་རོ། །

[Block 791 [HEADING]]
##### རྟོག་གེ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ། ^4-1-2-1-0

[Block 792]
དེ་ལ་དང་པོ་རྟོག་གེ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། རྟོག་གེ་པའི་མཚན་ཉིད་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་དགེ་སྦྱོང་དང་བྲམ་ཟེ་རྟོག་གེ་པ་དང་ལྡན་པ་རྟོག་གེར་གཏོགས་པའི་ས་རང་གི་སྤོབས་པ་ལས་བྱུང་བ། སོ་སོའི་སྐྱེ་བོ་ས༌[^610]སྤྱོད་པའི་རྗེས་སུ་སྤྱོད་པ་ལ་གནས་པ། ཐམས་ཅད་མཁྱེན་པ་མ་ཡིན་པར་ཐམས་ཅད་མཁྱེན་པ༌[^611]མངོན་པའི་ང་རྒྱལ་ཅན་བདག་དང་། སེམས་ཅན་དང་། སྲོག་དང་། གང་ཟག་ལ་སོགས་པར་མཐོང་བའི༌[^612]ཆོས་རྣམས་ཀྱི་དོན་དམ་པ་ཡིན་པར་ལྟ་ཞིང་དོན་དམ་པ་རྟོག་གེའི༌[^613]ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པ་ཁོང་དུ་མ༌[^614]ཆུད་པ་དེ་དག་གི་མཚན་ཉིད་ཅི༌[^615]འདྲ་བ་མངོན་པར་བསྒྲུབ་པའི་ཚུལ་རྣམ་པར་གཞག་པ་གང་ཡིན་པའོ། །

[Block 793]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། འདིར་འཕགས་པ་ཆོས་འཕགས་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་བཅོམ་ལྡན་འདས་སྔོན་གྱི་གདུགས་རྣམས་ཀྱི་ཤིན་ཏུ་སྔ་བ་ཞིག་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསོལ་ཏེ། རྒྱས་པར་མདོ་ཉིད་ལས་འབྱུང་བ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 794]
ད་ནི་དེ་དག་གི་ཚིག་གི་དོན་བཤད་པར་བྱ་སྟེ། དེ་ལ་སྔོན་གྱི་གདུགས་རྣམས་ཞེས་བྱ་བ་ནི་གང་དག་ལ་བཅོམ་ལྡན་འདས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའི་དུས་དག་སྟེ། དེ་ཡང་དང་པོར་བྱང་ཆུབ་ལ་གཞོལ་བ་ནས་ཐ་མ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་བར་གྱི་དུས་རྣམས་ལ་ཕྱིར༌[^616]བསྙགས་པའི་ཕྱིར་གདུགས་རྣམས་ཞེས་མང་པོའི་ཚིག་ཏུ་བྱས་སོ། །

[Block 795]
ཤིན་ཏུ་སྔ་བ་ཞིག་ན་ཞེས་བྱ་བ་ནི་གང་དག་ལ་བཅོམ་ལྡན་འདས་པས༌[^617]སྔར་སངས་རྒྱས་གཞན་དག་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའི་དུས་ནའོ། །

[Block 796]
འདི་ན་ཞེས་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^618]གནས་ཕུན་སུམ་ཚོགས་པ་སྔར་བསྟན་པ་དེ་ནས་སམ། འཇིག་རྟེན་གྱི་ཁམས་མི་མཇེད་འདི་ནས་སོ། །

[Block 797]
དེ་ན་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་གྱི་ཁམས་གྲགས་པ་ཅན་དེ་ནའོ། །

[Block 798]
མུ་སྟེགས་པ་རང་རང་གི་སྟོན་པ་ལ་སོགས་པ་ཞེས་བྱ་བ༌[^619]ནི་རྟོག་གེ་པ་གྲུབ་པའི་མཐའ་དང་གཞུང་ལུགས་ཐ་དད་པ་རང་རང་གི་མཁན་པོ་དང་དགེ་འདུན་གྱི་ཚོགས་དང་བཅས་པ་དག་གོ། །

[Block 799]
ཆོས་རྣམས་ཀྱི་དོན་དམ་པའི་མཚན་ཉིད་བསམ་པ་ལས་བརྩམས་ནས་ཞེས་བྱ་བ་ནི་དངོས་པོ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་གཏན་ལ་དབབ་པར་འདོད་ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 800]
མཆིས་ཤིང་ཞེས་བྱ་བ་ནི་གང་དག་དངོས་པོ་དེ་ཇི་ལྟ་བ་བཞིན་གཏན་ལ་དབབ་པའི༌[^620]ཕྱིར་སྔར་དེར་འཁོད་པ་དག་གོ། །

[Block 801]
འདུས་ནས་ཞེས་བྱ་བས་ནི་གང་དག་གིས་སྔ་མ་དེ་དག་མཐོང་ནས་དེའི་འོག་ཏུ་དེར་ལྷགས་པ་རྣམས་སོ། །

[Block 802]
སེམས་པར་བགྱིད་ཅེས་བྱ་བ་ནི་བསྟན་པའི་ཐ་ཚིག་གོ། །

[Block 803]
འཇལ་བར་བགྱིད་དེ༌[^621]ཉེ་བར་རྟོག་པར་བགྱིད་ཅེས་བྱ་བ༌[^622]ནི་བཤད་པའི་ཚིག་སྟེ། དེ་ཡང་རང་གི་གཞུང་ལུགས་ཀྱི་སྒྲོ་འདོགས་པ་དང་། སྐུར་པ་དང་བྲལ་བས་སེམས་པར་བྱེད་པ་ནི་འཇལ་བར་བགྱིད་ཅེས་བྱ་བས་བསྟན་ཏོ། །

[Block 804]
རིགས་པ་ལ་བརྟེན་ནས་སེམས་པར་བྱེད་པ་ནི་ཉེ་བར་རྟོག་པར་བགྱིད་ཅེས་བྱ་བས་བསྟན་ཏེ། དེ་ལྟར་ན་དེ་གཉིས་ཀྱིས་ནི་ཇི་ལྟར་སེམས་པར་བྱེད་པ་དང་། གང་གིས༌[^623]སེམས་པར་བྱེད་པ་བསྟན་པ་ཡིན་ཏེ་གོ་རིམ༌[^624]བཞིན་དུ་སྦྱར་རོ། །

[Block 805]
ཡོངས་སུ་ཚོལ་བར་བགྱིད་ཀྱང་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བསྟན་པ་དང་བཤད་པའི་ཚིག་དེ་དག་གཉིས་ཀྱིས་གཏན་ལ་འབེབས་པར་བྱེད་ཀྱང༌[^625]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 806]
མ་རྟོགས་ནས་ནི་ཞེས་བྱ་བ་ནི་གཏན་ལ་མ་ཕེབས་ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 807]
བློ་གྲོས་ཐ་དད་པ་ཞེས་བྱ་བ་ནི་བློ་གྲོས་སོ་སོར་གྱུར་པའོ། །

[Block 808]
ཡིད་གཉིས་ཅན་ཞེས་བྱ་བ་ནི་གང་དག་སོམ་ཉི་ཟ་བ་དག་གོ། །

[Block 809]
བློ་གྲོས་ངན་པ་ཞེས་བྱ་བ་ནི། དེ་དག་ལས་གང་དག་ལོག་པར་ངེས་པ་དེ་དག་གོ། །

[Block 810]
རྩོད་པ་ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས་སོ། །
--- END BLOCKS ---
