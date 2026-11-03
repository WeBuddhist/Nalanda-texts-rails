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
[Block 631]
འོ་ན་གང་བསྟན་བཅོས་བཏགས་པ་ལས།

[Block 632]
ཚིག་རྩུབ་པོ་སྤོང་བ་ཤིན་ཏུ་བསྒོམ་པའི༌[^254]ཕྱིར་སྐྱེས་བུ་ཆེན་པོའི་མཚན་ཚངས་པའི་དབྱངས་ཉིད་འགྲུབ་བོ་ཞེས་གསུངས་སོ། །

[Block 633]
ཁ་ཅིག་ན་རེ་ནི༌[^255]བརྒྱུད་པ་འདི་ནི་གསུམ་པ་ཡིན་ཏེ། ལས་དག་ལས་ནི་འབྱུང་བ་རྣམས་འགྲུབ། འབྱུང་བ་རྣམས་ལས་ནི་སྒྲ་འགྲུབ་བོ་ཞེས་ཟེར་རོ། །

[Block 634]
ཁ་ཅིག་ན་རེ་བརྒྱུད་པ་འདི་ནི་ལྔ་པ་ཡིན་ཏེ། ལས་དག་ལས་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་འབྱུང་བ་རྣམས་འགྲུབ། དེ་དག་ལས་ནི་རྒྱས་པ་ལས་བྱུང་བ་རྣམས་འགྲུབ། དེ་དག་ལས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་རྣམས་འགྲུབ་བོ། །

[Block 635]
དེ་དག་ལས་ནི་སྒྲ་འགྲུབ་བོ་ཞེས་ཟེར་རོ། །

[Block 636]
དེ་ལྟ་ན་འོ་ན་ནི་ལུས་ཀྱི་ཚོར་བ་ཡང་ལས་ལས་སྐྱེས་པའི་འབྱུང་བ་ལས་བྱུང་བའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 637]
གལ་ཏེ་སྒྲ་བཞིན་དུ་རིགས་པ་དང་འགལ་བར་གྱུར༌[^256]ན་རྣམ་པར་སྨིན་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 638]
རྒྱུ་མཐུན་ལས་བྱུང་རྣམ་སྨིན་སྐྱེས། །ཐོགས་པ་མེད་པ་བརྒྱད། བརྒྱད་གང་ཞེ་ན། སེམས་ཀྱི་ཁམས་བདུན་དག་དང་། ཆོས་ཀྱི་ཁམས་ཏེ་སྐལ་བ་མཉམ་པ་དང་ཀུན་དུ་འགྲོ་བའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་གོ། །

[Block 639]
རྣམ་པར་སྨིན་པའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་གོ། །

[Block 640]
རྒྱས་པ་ལས་བྱུང་བ་ནི་མེད་དེ། ཐོགས་པ་མེད་པ་རྣམས་ལ་རྒྱས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 641]
གཞན་རྣམ་གསུམ། གཞན་ནི་ལྷག་མ་བཞི་པོ་གཟུགས་དང་། སྒྲ་དང་།[^257] དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་དག་སྟེ། དེ་དག་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ཀྱང་ཡིན། རྒྱས་པ་ལས་བྱུང་བ་དག་ཀྱང་ཡིན། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་ཀྱང་ཡིན་ནོ། །

[Block 642 [HEADING]]
##### རྫས་དང་ལྡན་པ། ^1-3-13-2-0

[Block 643]
རྫས་དང་ལྷན་ཅིག །འདུས་མ་བྱས་ནི་བརྟན་པའི་ཕྱིར་རྫས་སོ། །

[Block 644]
དེ་ཡང་ཆོས་ཀྱི་ཁམས་ལ་ཡོད་པས་དེའི་ཕྱིར་ཆོས་ཀྱི་ཁམས་གཅིག་པུ༌[^258]རྫས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 645 [HEADING]]
##### སྐད་ཅིག་མ། ^1-3-13-3-0

[Block 646]
ཐ་མ་གསུམ་སྐད་ཅིག་མ་སྟེ། ཡིད་ཀྱི་ཁམས་དང་། ཆོས་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ནི་འདོན་པའི་རིམ་པས་ཐ་མ་དག་ཡིན་ཏེ། དེ་དག་ནི་ཟག་པ་མེད་པའི་བཟོད་པའི༌[^259]

[Block 647]
དང་པོ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པའི་ཚོགས་ལ་སྐད་ཅིག་མ་གཅིག་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་མ་ཡིན་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་སྐད་ཅིག་མ་རྣམས་ཞེས་བྱའོ། །

[Block 648]
འདུས་བྱས་གཞན་ནི་རྒྱུ་མཐུན་པ་ལས་མ་བྱུང་བ་འགའ་ཡང་མེད་དོ། །

[Block 649]
དེ་ལ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་ཡིད་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཡིན་ནོ། །

[Block 650]
ལྷག་མ་དེ་དང་ལྷན་ཅིག་འབྱུང་བ་རྣམས་ནི་ཆོས་ཀྱི་ཁམས་སོ། །

[Block 651 [HEADING]]
#### མིག་དང་རྣམ་ཤེས་ཁམས་དག་འཐོབ་པ། ^1-3-14-0

[Block 652]
འདི་དཔྱད་པར་བྱ་སྟེ། གང་གིས༌[^260]མིག་གི་ཁམས་དང་མི་ལྡན་པ་ལས་ལྡན་པ་འཐོབ་པ་དེ་མིག་གི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་ཡང་ཡིན་ནམ། གང་མིག་གི་རྣམ་པར་ཤེས་པ་དང་ཡིན་པ་དེ་མིག་གི་ཁམས་དང་ཡང་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མིག་དང་ནི།

[Block 653 [VERSE]]
རྣམ་ཤེས་ཁམས་དག་སོ་སོ་དང་། །
ལྷན་ཅིག་ཏུ་ཡང་འཐོབ་པ་ཡོད། །

[Block 654]
རེ་ཞིག་སོ་སོ་ནི་མིག་གི་ཁམས་དང་ཡིན་ལ། མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་མ་ཡིན་པ་ཡང་ཡོད་དེ། འདོད་པའི་ཁམས་ན་རིམ་གྱིས་མིག་གི་དབང་པོ་འཐོབ་པ་དང་། གཟུགས་མེད་པ་ནས་ཤི་འཕོས་ནས་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེ་བ་ནའོ། །

[Block 655]
མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཡིན་ལ་མིག་གི་ཁམས་དང་མ་ཡིན་པ་ཡང་ཡོད་དེ། བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པའི་མིག་གི་རྣམ་པར་ཤེས་པ་མངོན་དུ་བྱེད་པ་དང་། དེ་དག་ནས་ཤི་འཕོས་ནས་འོག་མར༌[^261]སྐྱེ་བ་ནའོ། །

[Block 656]
ལྷན་ཅིག་ཏུ་ཡང་ནི་གཉི་ག་དང་ལྡན་པ༌[^262]ཡང་ཡོད་དེ། གཟུགས་མེད་པའི་ཁམས་ནས་ཤི་འཕོས་ནས་འདོད་པའི་ཁམས་དང་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་ནའོ། །

[Block 657]
གཉི་ག་དང༌[^263]མ་ཡིན་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 658]
གང་མིག་གི་ཁམས་དང་ལྡན་པ་དེ་མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཡང་ཡིན་ནམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པ་མིག་གི་རྣམ་པར་ཤེས་པ་མངོན་དུ་མི་བྱེད་པ་ནའོ། །

[Block 659]
གཉིས་པ་ནི་འདོད་པའི་ཁམས་ན་མིག་མ་ཐོབ་པ་དང་ཉམས་པའོ། །

[Block 660]
གསུམ་པ་ནི་འདོད་པའི་ཁམས་ན་མིག་གི༌[^264]ཐོབ་པ་དང་མ་ཉམས་པ་དང་། བསམ་གཏན་དང་པོར་སྐྱེས་པ་དང་། བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པ་ལྟ༌[^265]བུའོ། །

[Block 661]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 662]
དེ་བཞིན་དུ་མིག་གི་ཁམས་དང་གཟུགས་དག་དང་། མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་། གཟུགས་དག་འཐོབ་པ་དང་ལྡན་པ་དག་ཀྱང་ཅི་རིགས་པར་བརྟག་པར་བྱའོ། །

[Block 663]
ལྷན་ཅིག་ཏུ་ཡང་ཞེས་བྱ་བའི་ཡང་གི་སྒྲ་ནི་ཞར་ལ་འོངས་པ་འདི་བསྡུ་བའི་དོན་ཏོ། །

[Block 664 [HEADING]]
#### ནང་གི་དང་ཕྱིའི། ^1-3-15-0

[Block 665]
ཁམས་དུ་དག་གཅིག་ནི༌[^266]ནང་གི་ཡིན། དུ་དག་གཅིག་ནི་ཕྱིའི་ཡིན་ཞེ་ན། ནང་གི་བཅུ་གཉིས། བཅུ་གཉིས་གང་དག་ཅེ་ན། གཟུགས་ལ་སོགས་པ་མ་གཏོགས་རྣམ་པར་ཤེས་པ་དྲུག་དང་། རྟེན་དྲུག་སྟེ། ཁམས་བཅུ་གཉིས་པོ་དེ་དག་ནི་ནང་གི་ཡིན་ནོ། །

[Block 666]
གཟུགས་ལ་སོགས་པ་ཡུལ་གྱི་ཁམས་དྲུག་པོ་དེ་དག་ནི་ཕྱིའི་ཡིན་ནོ། །

[Block 667]
བདག་མེད་ན་ཇི་ལྟར་ན་ནང་གི་འམ། ཕྱིའི་ཡིན་ཞེ་ན། སེམས་ནི་ངར་འཛིན་པའི་རྟེན་ཡིན་པའི་ཕྱིར་བདག་ཅེས་ཉེ་བར་འདོགས་ཏེ།

[Block 668 [VERSE]]
མཁས་པས་བདག་ཉིད་ཤིན་ཏུ་ནི། །
དུལ་བས་མཐོ་རིས་ཐོབ་པར༌[^267]འགྱུར། །

[Block 669]
ཞེས་གསུངས་ལ།

[Block 670]
བཅོམ་ལྡན་འདས་ཀྱིས་གཞན་ལས།
--- END BLOCKS ---
