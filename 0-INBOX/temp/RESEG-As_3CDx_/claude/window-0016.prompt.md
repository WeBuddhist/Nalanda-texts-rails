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
[Block 561]
དད་པ་འདི་ནི་ལས་དང་འབྲས་བུ་ལ་ཡིད་ཆེས་པའོ། །

[Block 562]
འདི་ནི་དཀོན་མཆོག་དང་བདེན་པ་ལ་སེམས་དད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་བྱེ་བྲག་ཏུ་རྣམ་པར་རྟོག་པའོ། །

[Block 563]
ཡོངས་སུ་རྟོག་པ་ཞེས་བྱ་བ་ནི༌[^413]ངོ་བོ་ཉིད་དང་བྱེ་བྲག་ཏུ་ཡོངས་སུ་རྟོག་པ་སྟེ། འདི་ནི་གཟུགས་ཏེ། གཟུགས་འདི་ནི་ཟག་པ་དང་བཅས་པའོ། །

[Block 564]
འདི་ནི་ཟག་པ་མེད་པའོ། །

[Block 565]
འདི་ནི་ཚོར་བ་སྟེ། ཚོར་བ་འདི་ནི་སྲེད་པས་བརླན་པའོ།[^414] །འདི་ནི་སྲེད་པས་མ་བརླན་པའོ། །

[Block 566]
འདི་ནི་འདོད་ཆགས་ཏེ། འདོད་ཆགས་འདི་ནི་མཐོང་བས་སྤང་བར་བྱའོ། །

[Block 567]
འདི་ནི་བསྒོམ་པས༌[^415]སྤང་བར་བྱའོ། །

[Block 568]
འདི་ནི་དད་པ་སྟེ། དད་པ་འདི་ནི་ལས་དང་འབྲས་བུ་ལ་ཡིད་ཆེས་པའོ། །

[Block 569]
འདི་ནི་དཀོན་མཆོག་བདེན་པ་ལ་སེམས་དང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་ངོ་བོ་ཉིད་དང་བྱེ་བྲག་ཏུ་ཡོངས་སུ་རྟོག་པའོ། །

[Block 570]
དེ་དག་ཐམས་ཅད་བྲལ་བ་ནི་སྤྱོད་པ་བཞི་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་ཏེ། རྣམ་པར་མི་རྟོག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྤྱོད་པ༌[^416]ཡོངས་སུ་རྫོགས་པ་དང་། ཉོན་མོངས་པ་མེད་པའི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པ་དང་། འཛིན་པ་མེད་པར་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པ་དང་། ཆགས་པ་མེད་པར་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 571]
དེ་ལ་ཐབས་མཁས་པས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྤྱོད་པ་འགྲུབ་བོ། །

[Block 572]
ཡོངས་སུ་འདྲིས་པའི་ཤེས་པས་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་སྤྱོད་པ་འགྲུབ་བོ། །

[Block 573]
སྙིང་རྗེས་ནི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་སྤྱོད་པ་འགྲུབ་བོ། །ཤེས་རབ་ཀྱིས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱེད༌[^417]པའི་སྤྱོད་པ་འགྲུབ་སྟེ། དེ་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཐབས་ལ་མཁས་པ་དང་། ཡོངས་སུ་འདྲིས་པའི་ཤེས་པ་དང་། སྙིང་རྗེ་དང་། ཤེས་རབ་དང་ལྡན་པས་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བའི༌[^418]ཉན་ཐོས་ལྟར་འགོག་པའི་སྟོབས་ཀྱིས་བཀག་པ་ནི༌[^419]མ་ཡིན་ནོ། །

[Block 574]
ཚིག་གི་དོན་དེ་དག་གིས༌[^420]སྐབས་གཞན་དུ་ནི་ཡོན་ཏན་གཞན་ཡང་སྟོན་ཏོ། །

[Block 575]
སྐབས་འདིར་ནི་དེ་དག་གིས་ཀྱང་དུས་ཆེན་པོ་ཉིད་བསྟན་པ་ཡིན་ཏེ། དེ་ཡང་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ལྟར་ཐབས་ལ་མཁས་པ་ལ་སོགས་པས་སྤྱོད་པ་བཞི་ཡོངས་སུ་རྫོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྟོག་པ་དང་། རྣམ་པར་རྟོག་པ་དང་། ཡོངས་སུ་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བ་ནི་འཁོར་བ་ཡང་མི་སྤོང་། མྱ་ངན་ལས་འདས་པ་ཡང་མི་ལེན་པར༌[^421]ཕྱི་མའི་མཐའི་མུར་ཐུག་པའི་བར་དུ་བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་སྒྲུབ་པར་བྱེད་པས་ན་དེས་ཀྱང་དུས་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 576 [HEADING]]
###### **འདོད་པ་མེད་པ་ཆེན་པོ།** ^3-2-3-2-1-2-5-0

[Block 577]
འདོད་པ་མེད་པ་ཆེན་པོ་ནི་བདུད་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ངེས་པར་བཅོམ་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། འདོད་པ་མེད་པ་ནི་ཡོངས་སུ་འཛིན་པ་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ་ཡིན་པས་དེ་ཉིད་ཀྱིས་བདུད་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ངེས་པར་བཅོམ་པ་ཡིན་ཏེ།[^422] ཇི་སྐད་དུ་བློ་གྲོས་རྒྱ་མཚོ་གང་གི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་ཡོངས་སུ་འཛིན་པ་ཐམས་ཅད་མི་འདོད་པར་འགྱུར་བ་དེའི་ཚེ་བདུད་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ངེས་པར་བཅོམ་པ་ཡིན་ནོ༌[^423]ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 578]
དེ་ལྟར་ཡོངས་སུ་འཛིན་པ་ཐམས་ཅད་སྤངས་ཏེ། བདུད་ཕྱིར་རྒོལ་བ་ངེས་པར་བཅོམ་པ་ཉིད་འདོད་པ་མེད་པ་ཡིན་པས་ན་དེས་ནི་འདོད་པ་མེད་པ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 579 [HEADING]]
###### **ཡིད་ལ་བྱེད་པ་ཆེན་པོ།** ^3-2-3-2-1-2-6-0

[Block 580]
ཡིད་ལ་བྱེད་པ་ཆེན་པོ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཡིད་ལ་བྱེད་པ་ཐམས་ཅད་ལས་རིང་དུ་གྱུར་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་དང་པོ་སེམས་བསྐྱེད་པ་ནས་ཐེག་པ་དམན་པའི་ཡིད་ལ་བྱེད་པ་ཐག་རིང་དུ་སྤངས་པ་ཡིན་པའི་ཕྱིར་ཏེ། འདི་ལྟར་ཐེག་པ་དམན་པའི་ཡིད་ལ་བྱེད་པ་ཐག་རིང་དུ་སྤངས་པ༌[^424]ཉིད་ཐེག་པ་ཆེན་པོའི་བསམ་པ་ཡིད་ལ་བྱེད་པ་ཡིན་པས་ན་དེས་ནི་ཡིད་ལ་བྱེད་པ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 581 [HEADING]]
###### **རྟོགས་པ་ཆེན་པོ།** ^3-2-3-2-1-2-7-0

[Block 582]
རྟོགས་པ་ཆེན་པོ་ནི། ཆོས་ཀྱི་རོའི་དགའ་བ་དང་། བདེ་བ་ཆེན་པོས་བསྟན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོས་བསྟན་པ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟར་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོས་བསྟན་པ་ཉིད་བྱང་ཆུབ་སེམས་དཔའི་གནས་པ་དང་། སངས་རྒྱས་ཀྱི་གནས་པ་ལ་གནས་པར་འགྱུར་བའི་རྒྱུ་ཡིན་པས་ན་དེས་ནི་རྟོགས་པ་ཆེན་པོ་བསྟན་པ༌[^425]ཡིན་ནོ། །

[Block 583 [HEADING]]
###### **ཡོངས་སུ་དག་པ་ཆེན་པོ།** ^3-2-3-2-1-2-8-0

[Block 584]
ཡོངས་སུ་དག་པ་ཆེན་པོ་ནི། འཇིགས་པ་ཆེན་པོ༌[^426]ལྔ་ལས་ཤིན་ཏུ་འདས་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། ལས་རྣམ་པ་གསུམ་དང་ལྷག་པའི་བསམ་པ་ཡོངས་སུ་དག་པས་འཇིགས་པ་ཐམས་ཅད་ལས་ཤིན་ཏུ་འདས་པ་སྟེ། ངན་འགྲོས་འཇིགས་པ་ལ་སོགས་པའི་རྒྱུ༌[^427]ཚུལ་ཁྲིམས་འཆལ་བ་ལ་སོགས་པའི༌[^428]དྲི་མ་ཡོངས་སུ་དག་པའི་ཕྱིར་རོ། །

[Block 585]
འཇིགས་པ་ལྔ་ནི་འཚོ་བ་མེད་པས་འཇིགས་པ་དང་། མི་བསྔགས་པས་འཇིགས་པ་དང་། འཆི་བས་འཇིགས་པ་དང་། ངན་འགྲོས་འཇིགས་པ་དང་། འཁོར་གྱི་ནང་དུ་བག་ཚ་བས་འཇིགས་པ་སྟེ། དེ་དག་ནི་ལྷག་པའི་བསམ་པ་དག་པའི་ས་ཐོབ་ནས་མེད་པར་འགྱུར་རོ། །

[Block 586]
དེ་ལྟར་འཇིགས་པ་ལྔ་ལས་ཤིན་ཏུ་འདས་པ་ནི་ལས་རྣམ་པ་གསུམ་ཡོངས་སུ་དག་པ་དང་ལྷག་པའི༌[^429]བསམ་པ་ཡོངས་སུ་དག་པ་ཡིན་པས་ན་དེས་ནི་ཡོངས་སུ་དག་པ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 587 [HEADING]]
###### **རྟོགས་པ་ཆེན་པོ།** ^3-2-3-2-1-2-9-0

[Block 588]
རྟོགས་པ་ཆེན་པོ་ནི། ཕྱིར་མི་ལྡོག་པའི་ས་བགྲོད་པ་གཅིག་པར་གྱུར་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་ལུང་བསྟན་པའི་ས་ཐོབ་པས་བགྲོད་པ་གཅིག་པར་གྱུར་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་ས་བདུན་པོ་དག་ལ་ནི་མངོན་པར་འདུ་བྱེད་པས་འཇུག་པའི་ཕྱིར་བགྲོད་པ་གཅིག་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 589]
ཕྱིར་མི་ལྡོག་པའི་ས་ནི་ས་བརྒྱད་པའོ། །

[Block 590]
བགྲོད་པ་ནི་ལམ་སྟེ་ས་བརྒྱད་པ་དེ་ཐོབ་པ་དེ་མ་ཡིན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ས་བརྒྱད་པ་ཐོབ་པ་གཞན་དག་དང་བགྲོད་པ་གཅིག་པར་གྱུར་པ་ཡིན་ཏེ། ས་བརྒྱད་པ་བགྲོད་པ་གཅིག་པར་གྱུར་པ་གང་དག་ཡིན་པ་དེ་དག་ལ་དེ་སྐད་ཅེས་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 591]
དེ་ལྟར་ཕྱིར་མི་ལྡོག་པའི་ས་ཐོབ་ཅིང་དེ་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་གཞན་དག་དང་བགྲོད་པ་གཅིག་པར་གྱུར་པ་ཉིད་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་ཡིན་པས་ན། དེས་ནི་རྟོགས་པ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 592 [HEADING]]
###### **ལས་ཆེན་པོ།** ^3-2-3-2-1-3-0

[Block 593]
དེ་ལ་ལས་ཆེན་པོ་ནི། སེམས་ཅན་ཐམས་ཅད་ཀྱི་གནོད་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ས་མངོན༌[^430]དུ་གྱུར་པ་ཤ་སྟག་ཅེས་གསུངས་པས་བསྟན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་ནང་གི་མཚན་མ་ལ་སོགས་པའི་གནོད་པ་གང་དག་ཡིན་པ་དེ་དག་ས་གང་གིས་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ས་དེ་མངོན་དུ་གྱུར་པ་གང་དག་ཡིན་པ་དེ་དག་ལ་འདི་སྐད་ཅེས་བྱ་སྟེ། ས་དེ་ཡང་གང་ཞེ་ན། བྱམས་པ་ཆེན་པོ་དང་། སྙིང་རྗེ་ཆེན་པོ་སྟེ། དེ་གཉིས་ཀྱིས༌[^431]བློ་མྱུར་དུ་བྱུང་བ་ལ་སོགས་པའི་གནོད་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་བྱེད་པ་དང་། དབུལ་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 594]
དེ་ལྟར་བྱམས་པ་ཆེན་པོ་དང་སྙིང་རྗེ་ཆེན་པོ་དེ་གཉིས་ཀྱིས་སེམས་ཅན་བདེ་བ་ལ་བཀོད་པ་དང་། སྡུག་བསྔལ་ལས་བསྐྱབ་པ་ལ་སོགས་པའི་དོན་བྱ་བ་ཕལ་ཆེར་བྱེད་ལ་དེའི་ས་མངོན་དུ་གྱུར་པས་ན་དེས་ནི་ལས་ཆེན་པོ་བསྟན་པ་ཡིན་ཏེ། དེ་ནི་རེ་ཞིག་རྣམ་གྲངས་གཞན་ཡིན་ནོ། །

[Block 595 [HEADING]]
###### འཇུག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ། ^3-2-3-2-2-0

[Block 596]
ཡང་རྣམ་གྲངས་གཞན་དུ་ན་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 597]
སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པ་ཐམས་ཅད་ཀྱང་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་བཞུགས་པ་ཞེས་བསྟན་ཏོ། །

[Block 598]
གནས་ཆེན་པོ་ལ་ཡང་དག་པར་བཞུགས་པ་ཞེས་བྱ་བ་འདི་སྐབས་འདིར་ནི་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་མི་བྱའི། འཇུག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་བར་བཤད་དེ། འཇུག་པ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའི་ལམ་གྱི་རང་བཞིན་ལ་བྱའོ། །

[Block 599]
དེ་ལ་འཇུག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་དེ་ནི་ལམ་གྱི་སྐྱོན་རྣམ་པ་དགུ་ཡོངས་སུ་སྤོང་བར་ཡང་དག་པར་ཞུགས་པས་འཇུག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་སྟེ། དེ་ཉིད་དེའི་ཕུན་སུམ་ཚོགས་པ་ཡང་ཡིན་ནོ། །

[Block 600]
དེ་ལ་ལམ་གྱི་སྐྱོན་རྣམ་པ་དགུ་གང་ཞེ་ན། འདི་སྐད་དུ།
--- END BLOCKS ---
