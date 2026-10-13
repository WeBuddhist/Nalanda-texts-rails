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
ཀྱེ་མ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྨྲེ་སྔགས་འདོན་པའམ་ངེས་པར་རིག་པར་བྱའོ། །

[Block 562]
དེ་ལྟར་འཇིག་རྟེན་ཞེས་བྱ་བ་ཕུང་པོ་ལྔ་པོ་རང་གི་མཚན་ཉིད་ཀྱིས་གྲུབ་པར་འདོད་ན་ཡང་མཐུན་པར་སྐྱོན་དུ་འགྱུར་བར་སྦྱར་རོ། །

[Block 563]
ཡང་ན་འདི་ནི་དོན་གཞན་ཏེ། གངས་ཅན་ལ་སོགས་པ་གང་དག་མ་བརྟེན་པར་བདག་རྟག་པ་དང་། ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མ་ཡིན་པ་དང་། འཇིག་རྟེན་ཡང་རང་བཞིན་གྱི་བདག་ཉིད་དང་། རང་བཞིན་ཡང་འགྱུར་བ་མེད་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ༌[^340]པར་ཞེན་ལ་འགྱུར་བའི་ཚོགས་ནི་ལྡོག་པར་འདོད་དོ། །

[Block 564]
གཞན་དག་ནི་གཞན་དུ་འདོད། ཀྱེ་མ་དེ་དག་ནི་གདོན་མི་ཟ་བར་རྟག་པ་དང་མི་རྟག་པ་ལ་སོགས་པའི་ལྟ་བ་རྣམས་ཀྱིས་འཕྲོགས་པར་འགྱུར་རོ། །

[Block 565]
རང་གི་སྡེ་པ་གང་དག་ཕུང་པོ་ལྔ་དང་བདག་བརྟེན་པར་ཁས་ལེན་ཀྱང་རྫས་སུ་ཡོད་པ་ཉིད་དུ་ཞུགས་པ་དང་གང་དག་མ་རིག་པ་དང་འདུ་བྱེད་ལ་སོགས་པ་རྒྱུ་དང་རྐྱེན་ཚོགས་པ་ལས་བྱུང་བ་ཡིན་ཡང་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྫས་སུ་ཡོད་པ་ཉིད་དུ་བརྗོད་པ་དེ་དག་ཀྱང་དེ་བཞིན་དུ་ལྟ་བ་ལོག་པར་ཞུགས་པ་ཡིན་པར་བསྟན་པའི་ཕྱིར།

[Block 566 [HEADING]]
### ཚིགས་བཅད་ཞེ་བཞི་པ། ^1-45-0

[Block 567 [VERSE]]
གང་དག་བརྟེན་ནས་དངོས་པོ་རྣམས། །
ཡང་དག་ཉིད་དུ་འགྲུབ་འདོད་པ། །
དེ་དག་ལ་ཡང་རྟག་སྩོགས་ཀྱི། །
སྐྱོན་དེ་ཇི་ལྟར་འབྱུང་མི་འགྱུར། །

[Block 568]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 569]
ཇི་ལྟར་བདག་དང་ཆོས་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་དོན་ཡོད་པ་དང་། མེད་པར་ཁས་བླངས་པ་ལ་རྟག་པ་དང་། ཆད་པའི་སྐྱོན་དུ་འགྱུར་བ་དང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 570]
ཇི་སྐད་སྨོས་པའི་ལྟ་བ་དག་བསལ་ནས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཇི་ལྟར་གནས་པའི་དོན་ཁོང་དུ་ཆུད་ན།

[Block 571 [HEADING]]
### ཚིགས་བཅད་ཞེ་ལྔ་པ། ^1-46-0

[Block 572 [VERSE]]
གང་དག་བརྟེན་ནས་དངོས་པོ་རྣམས། །
ཆུ་ཡི་ཟླ་བ་ལྟ་བུར་ནི། །
ཡང་དག་མ་ཡིན་ལོག་མིན་པར། །
འདོད་པ་དེ་དག་ལྟས་མི་འཕྲོགས། །

[Block 573]
གལ་ཏེ་གཟུགས་ལ་སོགས་པ་ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་ཡིན་ན། དེ་དག་ངོ་བོ་ཉིད་ཀྱིས་མེད་པས་ངོ་བོ་ཉིད་གཞན་དུ་འགྱུར་མི་སྲིད་དེ། ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་ནི་ཕྱིས་ཡོད་པར་མི་རུང་ངོ་། །རྒྱུ་དང་རྐྱེན་ཡོད་དུ་ཟིན་ཀྱང་གང་ཡང་སྐྱེ་མི་སྲིད་པ་དང་རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱང་དེ་ལྟ་བུའི་རང་བཞིན་ཡིན་པས་མི་སྲིད་པའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 574]
འོན་ཏེ་ཉེས་པ་དེ་ཡོངས་སུ་སྤང་བར་འདོད་དེ། ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པར་ཁས་ལེན་ན་ཡང་དེའི་ཚེ་དེ་ལྟར་བྱུང་བ་བཞིན་དུ་རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱིས་ཀྱང་འབྱུང་བར་མི་འགྱུར་ཏེ། རྒྱུ་དང་རྐྱེན༌[^341]རྣམས་ཀྱང་དགོས་པ་མེད་པས་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 575]
དེ་ལྟ་ན་ཡང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 576]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་འགལ་ན་རྣམ་པར་གཞག་པ་ཐམས་ཅད་ཞིག་པར་འགྱུར་རོ།[^342] །བོང་བུའི་རྭ་ལ་སོགས་པ་བཞིན་དུ་འགྲོ་བ་ཡང་མི་དམིགས་པར་འགྱུར་རོ། །

[Block 577]
དེ་བས་ན་ཁམས་དང་འགྲོ་བ་དང་། སྐྱེ་གནས་དང་། རིགས་དང་། རུས་དང་། ཆོ་རིགས་དང་། ཁ་དོག་དང་། གཟུགས་དང་། སྟོབས་དང་། བློ་དང་། དབང་པོ་སོ་སོ་ཐ་དད་པའི་འགྲོ་བ་དང་། འགྲོ་བ་མ་ལུས་པའི་རྟེན་ཕྱི་རོལ་གྱི་རླུང་གི་དཀྱིལ་འཁོར་ལ་སོགས་པ་དང་། གསེར་དང་། དངུལ་དང་། ཨནྡ་རྙིལ་དང་། ཤེལ་དང་། པདྨ་རཱ་ག་ལ་སོགས་པ༌[^343]དང་། ཀུ་མུ་ད་དང་། པདྨ་དང་། ཤིང་དང་། རི་དང་། སྨན་དང་། བུམ་པ་དང་། ཤིང་རྟ་ལ་སོགས་པ་དམིགས་སུ་མེད་པ་སྣ་ཚོགས་ཀྱང་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 578]
དེ་དམིགས་སུ་ཡོད་བཞིན་དུ་མེད་པར་ཁས་བླང་བ༌[^344]ནི་མི་རིགས་སོ། །

[Block 579]
དེ་བས་ན་གང་བརྟེན་ཏེ་འབྱུང་བའི་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་དང་མེད་པ་སྤངས་པ་སྟེ། རྐྱེན་འདི་ཙམ་གྱིས་གྲུབ་པས་གཟུགས་བརྙན་བཞིན་དུ་དེ་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པར་ཁས་བླང་བར་བྱ་སྟེ། ཇི་ལྟར་འཕགས་པ་ལྷས།

[Block 580 [VERSE]]
འབྲས་བུ་ཡོད་པར་གང་འདོད་དང་། །
འབྲས་བུ་མེད་པར་གང་འདོད་ལ། །
ཀ་བ་ལ་སོགས་ཁྱིམ་དོན་དུ། །
བརྒྱན་པའི༌[^345]དོན་ཀྱང་མེད་པར་འགྱུར། །

[Block 581]
ཞེས་སྨོས་པ་ལྟ་བུའོ། །

[Block 582]
དེ་ལྟར་རྟག་པ་དང་ཆད་པ་སྤངས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གཟུགས་བརྙན་ལྟ་བུ་བློ་ཕྱིན་ཅི་ལོག་གི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་དང་འགལ་བ་མེད་པས་ཇི་སྐད་སྨོས་པའི་འགྲོ་བ་སྣ་ཚོགས་མི་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 583]
འཕགས་པ་རྣམས་ཀྱང་ཕྱིན་ཅི་ལོག་སྤངས་ཏེ། བརྫུན་དུ་སྒྲོ་མི་འདོགས་པས་རྣམ་པར་གྲོལ་བ་མི་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 584]
གང་གི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འདི་ལྟར་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པ་དེའི་ཕྱིར་རིགས་པ་འདིས་དངོས་པོ་རྣམས་ལ་གང་དག་བརྟེན་ནས་དངོས་པོ་རྣམས་ཆུའི་ཟླ་བ་ལྟ་བུར་ནི་འདོད་པ་དེ་དག་རང་གི་ངོ་བོར་གྲུབ་པ་མེད་པས་གཟུགས་བརྙན་བཞིན་དུ་རང་གི་ངོ་བོ་ཉིད་ཀྱི་བདེན་པ་ཡང་མ་ཡིན་བརྫུན་པ་ཡང་མ་ཡིན་པར་འདོད་དེ། འདི་ལྟར་བསམ་པ་འདི་ནི་དངོས་པོར་གྱུར་པ་ལ་བརྟེན་པ་སྟེ། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ནི་དངོས་པོ་ཡོད་པ་མ་ཡིན་ལ། གཟུགས་བརྙན་ལྟ་བུར་གྱུར་པ་དེའི་ཕྱིར་དེ་ཡང་དག་པ་མ་ཡིན་ནོ། །

[Block 585]
ཡང་དག་པར་ཡོད་ན་གཞན་དུ་འགྱུར་མི་སྲིད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 586]
འཇིག་རྟེན་ན་ཡང༌[^346]དག་པ་དང་འདྲ་བར་སྣང་བས་ལོག་པ་ཡང་མ་ཡིན་ནོ། །

[Block 587]
ཡང་དག་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ཡང་ལ་ལ་ལ་བསྟན་པ་དང་དགོས་པ་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 588]
གང་གི་ཕྱིར་ཡང་དག་པ་མ་ཡིན་པ་དེའི་ཕྱིར་རྟག་པར་སྨྲ་བ་མ་ཡིན་ནོ། །

[Block 589]
གང་གི་ཡང་དག་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་དེའི་ཕྱིར་ཆད་པར་སྨྲ་བའམ་ལོག་པར་སྨྲ་བ་མ་ཡིན་ནོ། །

[Block 590]
དེ་ལྟར་གཟུགས་བརྙན་བཞིན་དུ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་རང་བཞིན་མེད་པར་ཁོང་དུ་ཆུད་ན་གདོན་མི་ཟ་བར་ཚུལ་བཞིན་མ་ཡིན་པར་རྣམ་པའི་རླུང་གིས་དཀྲུགས་ཏེ་འཁྲུགས་པར་གྱུར་པའི་རྦ་རླབས་ཆེན་པོ་བརྟག་པ་དང་མི་རྟག་པ་ལ་སོགས་པའི་ལྟ་བའི་ཆུ་བོ་ལས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཤེས་པའི་གྲུས་བརྒལ་ནས་མྱ་ངན་ལས་འདས་པའི་སྐྱེད་མོས་ཚལ་གྱི་ཐང་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པའི་ཤིང་གི་ཚལ་གྱིས་མཛེས་པར་བྱས་པ། བྱང་ཆུབ་ཀྱི་ཡན་ལག་གི་རིན་པོ་ཆེ་སྣ་ཚོགས་ཡིད་འཕྲོག་པ༌[^347]ཡོད་པ། སྟོབས་བཅུ་དང་ལྡན་པས་དྲི་མ་མེད་པ། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པས་དབེན་པར་བདེ་བར་ཕྱིན་ཏེ། གཞན་དག་ལ་ཡང་དེའི་རྗེས་སུ་འགྲོ་བ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་གཏམ་གསང་བསྟོད་དེ༌[^348]སྟོན་པས་བསྒོ་བ་དེ་བསྒྲུབ་པ༌[^349]ལ་བརྩོན་པ༌[^350]འཁོར་བའི་རྒྱ་མཚོ་ཆེན་པོའི་ནང་ན་འདུག་པ་རྟག་པ་ལ་སོགས་པའི་ལྟ་བའི་ཆུ་བོ་རྣམས་ཀྱིས་མགོ་རྨོངས་པ་དེ་དག་ངེས་པར་སྒྲོལ་ལོ། །

[Block 591]
གང་དག་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཆོས་ཉིད་འདི་ཁོང་དུ་མ༌[^351]ཆུད་དེ། དངོས་པོ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད༌[^352]ཡོངས་སུ་རྟོག་པ་དེ་དག་ནི་གདོན་མི་ཟ་བར་

[Block 592 [HEADING]]
### ཚིགས་བཅད་ཞེ་དྲུག་པ། ^1-47-0

[Block 593]
དངོས་པོར་ཁས་ལེན་ཡོད་ན་ནི།

[Block 594 [VERSE]]
འདོད་ཆགས་ཞེ་སྡང་འབྱུང་བ་ཡི། །
ལྟ་བ་མི་བཟད་མ་རུངས་འཛིན། །
དེ་ལས་བྱུང་བའི་རྩོད་པར་འགྱུར། །

[Block 595]
དེ་ལ་འདོད་ཆགས་ནི་རང་གི་ཕྱོགས་ལ་མངོན་པར་ཞེན་པའི་མཚན་ཉིད་དོ། །

[Block 596]
ཞེ་སྡང་ནི་གཞན་གྱི་ཕྱོགས་ལ་རྒྱབ་ཀྱིས་བལྟས་པའི་མཚན་ཉིད་དོ། །

[Block 597]
འདོད་ཆགས་དང་ཞེ་སྡང་གང་ལས་འབྱུང་བ་དེ་འདོད་ཆགས་དང་ཞེ་སྡང་འབྱུང་བའོ། །

[Block 598]
རྣམ་པར་སྨིན་པ་ཤིན་ཏུ་མི་བདེ་བ་དང་ཤིན་ཏུ༌[^353]བཟོད་པར་དཀའ་བའི་ཕྱིར་མི་བཟོད་པའོ། །

[Block 599]
སེམས་ཀྱི་རྒྱུད་ལ་གནོད་པ་སྐྱེད་པར་བྱེད་པ་དང་། འདའ་བར་དཀའ་བའི་ཕྱིར་མ་རུངས་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། ལྟ་བ་ཡོངས་སུ་འཛིན་པའོ། །

[Block 600]
ལྟ་བ་ལ་གནས་པ་འདི་ལྟ་བུ་འདི་ཡང་དངོས་པོར༌[^354]ལེན་པ་ལས་སྐྱེའོ། །
--- END BLOCKS ---
