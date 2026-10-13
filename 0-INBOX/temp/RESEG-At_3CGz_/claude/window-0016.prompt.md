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
དགེ་སྦྱོང་གི་ཚུལ་ཤས་ཆེར་ལྟ་བ་དང་། སྟོན་པ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དང་། བསྟན་པ་ལ་དགའ་བའི་ལྷ་དག་དང་། སྐྱེ་བོ་མཁས་པ་དང་། འཇིག་རྟེན་པ་དག་གིས་སྨད་པར༌[^300]འགྱུར་རོ་སྙམ་པ་དང་། བདག་ཉིད་ལ་དཔྱས༌[^301]ནས་ངོ་ཚ་བ་དང་། ཁྲེལ་ཡོད་པ་ནི་རྒྱུ་གཉིས་པའོ། །

[Block 562]
དོན་ཉུང་བ་བྱ་བ་ཉུང་བ། ལས་ཀྱི་མཐའ་ཉུང་བ་ནི་རྒྱུ་གསུམ་པའོ། །

[Block 563]
ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བ་དང་མི་འདྲེ་བར་གནས་པ་དང་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་ལ་མཁས་པ་དང་དགེ་བའི་ཕྱོགས་ལ་བརྩོན་པ་ནི་རྒྱུ་བཞི་པའོ། །

[Block 564]
ལས་དང་པོ་པ་དང་སྨྱོས་པ༌[^302]དང་གཉིད་ལོག་པ་དང་། སེམས་འཁྲུགས་པ༌[^303]དང་། ཚོར་བས་ཉེན་པ་ནི་རྒྱུ་ལྔ་པའོ། །

[Block 565 [HEADING]]
### ལྟུང་བ་ལས་ལྡང་བ། ^5-6-0

[Block 566]
ལྟུང་བ་ལས་ལྡང་བ་ནི་གསུམ་སྟེ། འགྱོད་པ་ལྔ་བསྐྱེད་པ་དང་། ཡན་ལག་ལྔས་བསྡུས་པའི་བག་ཡོད་པ་དང་། རྣམ་པ་ལྔས་འགྱོད་པ་བསལ་བའོ། །

[Block 567]
ཡན་ལག་ལྔས་བསྡུས་པ་ནི་ཉན་ཐོས་ཀྱིསར་བལྟ་བར་བྱའོ། །

[Block 568]
འགྱོད་པ་ལྔས་བསྐྱེད༌[^304]པ་ནི་འདི་ན་ལ་ལ་དག་ལ་ལྟུང་བ་བྱུང་བ་ན་འདི་སྙམ་དུ་བདག་ཉིད་ལ་གཞི་འདིས་ཚུལ་ཁྲིམས་ཉམས་པར་འགྱུར་རོ་སྙམ་པ་དང་། སྟོན་པ་དང་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་མཁས་པ་དག་གིས་སྨད་པར་འགྱུར་རོ་སྙམ་པ་དང་། ལྷ་དག་གིས་སྨད་པར་འགྱུར་རོ་སྙམ་པ་དང་། ཕྱོགས་དང་ཕྱོགས་མཚམས་དག་ཏུ་སྡིག་པ་ཅན་གྱི་སྐྱེ་བོས་གྲགས་པ་དང་སྒྲ་དང་ཚིགས་སུ་བཅད་པ་མ་ཡིན་པ་བརྗོད་པར་འགྱུར་རོ་སྙམ་པ་དང་། མི་དགེ་བའི་གཞི་འདིས་བདག་ལུས་ཞིག་ནས་ངན་སོང་དག་ཏུ་སྐྱེས་ན་མི་རུང་ངོ་སྙམ་འགྱོད་པ་སྐྱེས༌[^305]པའོ། །

[Block 569]
རྣམ་པ་ལྔས་འགྱོད་པ་བསལ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་གཞི་དང་བཅས། ངེས་པར་འབྱུང་བ་དང་བཅས་པའི་ཆོས་བསྟན༌[^306]པས་ལྟུང་བ་ལས་ལྡང་བའི་ཐབས་ཡོད་དོ་སྙམ་པ་དང་། མི་ཤེས་པ་དང་བག་མེད༌[^307]པ་དང་མ་གུས་པ་དང་ཉོན་མོངས་པ་ཆེ་བ་དག་གིས་ལྟུང་བ་བྱུང་བ་མི་ཤེས་པ་ནས་བཞི་པོ་དེ་དག་སྐྱེས་སོ་སྙམ་པ་དང་། ལྟུང་བ་ལ་ལྟུང་བ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་ལྷག་པའི་བསམ་པ་ཐག་པ་ནས་སེམས་བསྐྱེད་དོ་སྙམ་པ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་མཁས་པ་དག་གི་མདུན་དུ་ལེགས་པར་བཤགས་པ༌[^308]ཟིན་ཏོ་སྙམ་པ་དང་། བདག་ལེགས་པར་གསུངས་པའི་ཆོས་འདུལ་བ་ལས་རབ་ཏུ་བྱུང་ནས་བསླབ་པ་དང་འགལ་ན་འགྱོད་པ་བྱེད་པ་དེ་ནི་ཡང་དག་པ་དང་ལེགས་པ་མ་ཡིན་གྱི།[^309] བདག་བཅོམ་ལྡན་འདས་ཀྱིས་འགྱོད་པའི་རྒྱུན་སྒྲིབ་པའི་གནས་རྣམ་གྲངས་དུ་མར་སྨད་པ། བར་དུ་གཅོད་པའི་ཆོས་གང་ཡིན་པ་དེས་མང་དུ་གནས་ཤིང་དང་དུ་ལེན་པར་བྱེད་ལ། སེལ་བར་མི་བྱེད་ལ་མི་སེལ་བ་གང་ཡིན་པ་དེ་ནི་བདག་དགེ་བ་དང་ལེགས་པ་མ་ཡིན་ནོ་སྙམ་ནས་འགྱོད་པ་སེལ་བའོ། །

[Block 570]
ཡང་ན་སྡེ་པ་སོ་སོའི་རང་རང་གི་འདུལ་བ་ལས་འབྱུང་བའི་ཐབས་ཀྱིས་བཤགས༌[^310]པར་བྱའོ། །

[Block 571]
ཡང་ན་བདག་གིས་བྱས་པའི་ལྟུང་བ་བཤགས་པའི་ཆོ་ག་རྒྱས་པའི་ཐབས་དེས་བཤགས་པར་བྱའོ། །

[Block 572]
ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་སོ་སོར༌[^311]ཐར་པའི་མདོ་གདོན་ཞིང་གསོ་སྦྱོང་ལ་རབ་ཏུ་བརྩོན་པར་བྱའོ། །

[Block 573]
དགེ་སློང་འདུལ་བའི་བསླབ་པ་ལ་དེ་ལྟར་བརྩོན་པ་ནི་ལྟུང་བ་ལ་མཁས་པ་ཡིན། ལྟུང་བ་ལས་ངེས་པར་འབྱུང་བ་ལ་མཁས་པ་ཡིན། བདག་ཉིད་དག་པ་དང་། གཙང་བ་དང་། དྲི་མ༌[^312]མེད་པ་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པས༌[^313]འགྱོད་པ་མེད་དེ་དེ༌[^314]ཁྱིམ་ནས་ཁྱིམ་མེད་པར་རབ་ཏུ་བྱུང་ནས་ལེགས་པར་གསུངས་པའི་ཆོས་འདུལ་བའི་ཚུལ་ཁྲིམས་ཉམས་པ་དང་ཞིག་པ་དང་རལ་བ་དང་། ནག་ནོག་ཅན་དང་མི་གཙང་བ་མེད་ཅིང་ལེགས་པར་བསྲུང་བ་དང་། སྦྱངས་པའི་ཡོན་ཏན་བཅུ་གཉིས་དང་། དགེ་སྦྱོང་གི་རྒྱན་བཅུ་བདུན་གྱིས་བརྒྱན༌[^315]ནས་གནས་པ་ནི་དགེ་སློང་ཡང་དག་པ་ཡིན་ནོ་སྙམ་དུ་བསམས་ནས།

[Block 574 [VERSE]]
ཚངས་སྤྱོད་དཔལ་དང་ལྡན་པ་ཡི། །
དགེ་སློང་སྡོམ་པ་དག་ཏུ་བཞེད། །

[Block 575]
ཅེས་སྨྲས་སོ། །

[Block 576]
དེས་ན༌[^316]མགོན་པོ་མི་ཕམ་པའི་ཞལ་ནས།

[Block 577 [VERSE]]
ལྟུང་བ༌[^317]འབྱུང་དང་ལྡན་པ་དང་། །
ངེས་པར་འབྱུང་དང་གང་ཟག་དང་། །
བཅས་པ་དང་ནི་རབ་དབྱེ་བས། །
རྣམ་པར་ངེས་ཕྱིར་འདུལ་བའི་ཆོས། །

[Block 578]
ཞེས་མདོ་སྡེ་རྒྱན་ལས་གསུངས་སོ། །

[Block 579]
ཉན་ཐོས་ཀྱི་ཐེག་པའི་སྐབས་རྫོགས་སོ།། །།

[Block 580]
འདི་ལྟར་སོ་སོར༌[^318]ཐར་པའི་སྡོམ༌[^319]པ་ཙམ། སྨོན་པའི་སེམས་བསྐྱེད་པ་ཙམ་གྱིས་ཆོག་ཅིང་དེ་ཙམ་ལ་ལྟོས་པར་མི་བྱ་སྟེ། འཕགས་པ་དཀོན་མཆོག་སྤྲིན་ལས་རིགས་ཀྱི་བུ་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་བསླབ་པའི་སྡོམ་པས་བསྡམས་པ་ཡིན་ཞེ་ན། འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་འདི་ལྟར་སྤྱོད་དེ། སོ་སོར༌[^320]ཐར་པའི་སྡོམ་པ་ཙམ་གྱིས་བདག་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་ནུས་ཀྱི།[^321] དེ་བཞིན་གཤེགས་པས་གང་འདི་མདོ་སྡེ་དེ་དང་དེ་དག་ལས་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པའི་གནས་བཅས་པ་དེ་དག་ལ་བདག་གིས་བསླབ་པར་བྱའོ་ཞེས་གསུངས་པས་ན།[^322] འདིར་ཡང་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་རྒྱ་ཆེན་པོ་ལ་བསླབ་པར་བྱ་བའི་ཕྱིར་བདག་གིས་བླ་མའི་རྗེས་སུ་བསྟན་པ་དང་། ཐེག་པ་ཆེན་པོའི་མདོ་སྡེའི་རྗེས་སུ་འབྲངས་ནས་བཤད་པར་བྱའོ། །

[Block 581 [HEADING]]
## བླ་མ་བཟང་ལས་སྡོམ་པ་བླང། ^6-0

[Block 582]
དེ་ལྟར་ཐེག་པ་ཆེན་པོའི་ཐུན་མོང་མ་ཡིན་པའི་རྟེན་བསྟན་ནས། ད་ནི་ཤིང་རྟ་ཆེན་པོའི་ལམ་བསྟན་པའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའི་ས་དག་གི །ཚུལ་ཁྲིམས་ལེའུ༌[^323]གསུངས་ཆོ་ག་ཡིས། །ཞེས་བྱ་བ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ས་ནི་འཕགས་པ་ཐོགས་མེད་ཀྱིས༌[^324]མཛད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བཀོད༌[^325]པའི་བསྟན་བཅོས་སོ། །

[Block 583]
དེ་ལས་ཀྱང་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལེའུ་ལས་སོ། །

[Block 584]
དེ་ཡང་དགུ་ཡིན་ཏེ།

[Block 585 [VERSE]]
ངོ་བོ་ཉིད་དང་ཐམས་ཅད་དང་། །
དཀའ་བ་དང་ནི་སྒོ་ཀུན་དང་། །
སྐྱེས་བུ་དམ་པ་ཉིད་དང་ནི། །
རྣམ་ཀུན་དང་ནི་ཕོངས་ཤིང་འདོད། །

[Block 586]
འདི་དང་གཞན༌[^326]དུ་བདེ་འགྱུར་དང་། །རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 587]
དེ་དག་གི་ནང་ནས་ཀྱང་ངོ་བོ་ཉིད༌[^327]ཐམས་ཅད་ཀྱི་ཚུལ་ཁྲིམས་ལས་གསུངས་སོ་ཞེས་བྱའོ། །ཇི་ལྟར་གསུངས་ཤེ་ན། ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་ལས་གསུངས་པའི་ཆོ་གས་བྱའོ། །

[Block 588]
ཆོ་ག་དེ་ཡང་ཇི་ལྟ༌[^328]ཞེ་ན།

[Block 589 [VERSE]]
ཡང་དག་མཚན་ཉིད་ལྡན་པ་ཡི།[^329] །
བླ་མ་བཟང་ལས་སྡོམ་པ་བླང་།[^330] །

[Block 590]
ཞེས་སྨྲས་སོ། །

[Block 591]
ཡང་དག་པའི་མཚན་ཉིད་བཟང་པོ་དེ་དང་ལྡན་པའི་བླ་མ་བཟང་པོ་དེ་ཡང་གང་ཞེ་ན།

[Block 592 [VERSE]]
སྡོམ་པའི་ཆོ་ག་ལ་མཁས་དང་། །
བདག་ཉིད་གང་ཞིག་སྡོམ་ལ་གནས། །
སྡོམ་པ་འབོགས་བཟོད་སྙིང་རྗེ་ལྡན། །
བླ་མ་བཟང་པོར་ཤེས་པར་བྱ། །

[Block 593]
ཞེས་བྱ་བ་དེ་ཡིན་ནོ། །

[Block 594]
དེ་ལ་སྡོམ་པའི་ཆོ་ག་ལ་མཁས་པ༌[^331]ཞེས་པ་ནི་དེ་ལ་མཁས་ཤིང་བྱང་བའོ། །

[Block 595]
སྡོམ་ལ་གནས་ཞེས་པ་ནི་བླ་མའི་ཚུལ་ཁྲིམས་ཉམས་པ་དང་ཞིག་པ་མེད་ཅིང་གཙང་བའོ། །

[Block 596]
བཟོད་ཅེས་པ་ནི་ནུས་པ་དང་ལྡན་པ་སྟེ་སྡོམ་པ་འབོགས་པ་ལ་རག་མ་ལས་པར་ཆས་པའོ། །

[Block 597]
སྙིང་རྗེ་ལྡན་ཞེས་པ་ནི་སློབ་མ་ལ་བུའི་འདུ་ཤེས་དང་། གཞན་གྱི་སྡུག་བསྔལ་ལ་སེམས་མི་བཟོད་པའོ། །

[Block 598]
བླ་མ་ཞེས་བྱ་བ་ནི་བླ་མར་བྱ་བའི་གནས་སུ་གྱུར་པ་ཉིད་ལ་ནོད་པར་བྱའི་གཞན་ལས་ནི་མ་ཡིན་ཏེ། གུས་པས་བླ་མར་འཛིན་པ་དང་། དེའི་རྗེས་སུ་སློབ་མའི་ངང་ཚུལ་ཅན་དང་། དེས་བསྟན་པའི་དོན་ལ་གུས་པ་ཆེན་པོ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 599]
ཡང༌[^332]བླ་མ་དེ་ཕུན་སུམ་ཚོགས་པ་བཞི་དང་ལྡན་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དང་། ཡོན་ཏན་ཕུན་སུམ༌[^333]ཚོགས་པ་དང་། བསམ་པ་ཕུན་སུམ༌[^334]ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ༌[^335]ཚོགས་པའོ། །

[Block 600]
དེ་ལ་བདག་ཉིད་གང་ཞིག་སྡོམ་པ་གང༌[^336]ལ་གནས་ཞེས་པས་ནི་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
