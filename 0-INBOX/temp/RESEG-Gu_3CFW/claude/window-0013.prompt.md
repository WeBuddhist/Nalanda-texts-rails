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
[Block 456]
ཅི་ཐམས་ཅད་དུ་རྣམ་པར་གཞག་པ་འདི་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ་དེའི་ཕྱིར་ཅིག༌[^416]ཤོས་ཡོད་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅིག་ཤོས་ཞེས་བྱ་བ་གོང་ན་མཚན་མཐུན་པ་ཡོད་པ་དེ་མཚན་མ་མཐུན༌[^417]པ་མི་དབང་ངོ་ཞེས༌[^418]བྱ་བའི་དོན་ཏོ། །

[Block 457]
གནས་ནས་ཕྱུང་བའི་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་ཅིག་ཤོས་ཡོད་ན་ཤི་བའི་ཡོ་བྱད་ལ་ཡང་གནས་ནས་ཕྱུང་བའི་མི་དབང་ངོ་ཞེས་བྱ་བ་འདིར་ཉེ་བར་གཞག་པའོ། །

[Block 458]
འདིར་གནས་ནས་ཕྱུང་བའི་ནི་ཅིག་ཤོས་ཉིད་ལ་མཐར་ཐུག་པའོ། །

[Block 459]
འདིར་གནས་ནས་མ་ཕྱུང་བ་ལ་ནི་ཅིག་ཤོས་ཀྱི་སྒྲའི་རྣམ་པར་གཞག་པའོ། །

[Block 460]
མེད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཅིག་ཤོས་ལའོ། །

[Block 461]
རྒྱུ་ལས་སེམས་མ་ལོག་ནའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མ་མཐོང་བ་ལ་སོགས་པའི་རྒྱུ་གང་གིས་དེ་སྤང་བའི་ལས་བྱས་པའི་རྒྱུ་དེ་ལས་སེམས་མ་ལོག༌[^419]ཅིང་བཟློག་པར་མ་བྱས་པ་དེ་ལའོ། །

[Block 462]
འདིར་གཞུང་ནི། གང་དབང་ལགས། དེ་དག་ལས་གང་གིས་དང་པོར་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་སྤོང་བར་བྱེད་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 463]
གང་གིས་མ་བཏང་བ་ཉིད་ལ་གཞན་གྱིས་ཀྱང་ཞེས་བྱ་བའི་འདིར་ཚིག་ཡོད་པ་དེ་དེ་བས་ན་འདིར་མདོ་བྱས་སོ། །

[Block 464]
འདིར་ལྟ་བ་དང་། འབྲེལ་བ་སྤང་བའི་རྒྱུ་ལས་མངོན་པར་ཞེན་པར་རིག་པར་བྱ་སྟེ། མཆོག་ཉིད་དུ་མཐོང་བའི་རབ་ཏུ་དབྱེ་བ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་ལྟ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 465]
དེའི་དེ་མནོད་པར་བྱ་བ་ཉིད་ལ་དེ་ནི་ཐ་དད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྤངས་པ་དེ་ཤི་བའི་ཡོ་བྱད་རྣམས་དེ་མནོད་པར་བྱ་བ་ཉིད་ལ་སྤངས་པ་དེ་མ་སྤངས་པ་དང་ཐ་དད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 466]
སྤངས་པ་ནི་དགེ་འདུན་ལས་ཐ་དད་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་འོས་པ་ཉིད་དོ། །

[Block 467]
དེའི་ཤི་བའི་ཡོ་བྱད་ལ་རང་བཞིན་གྱིས་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 468]
ཐ་དད་པའི་ལ་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདོད་པ་གཞན་ལ་བརྟེན་པས་ཐ་དད་པ་ཕྱོགས་གཞན་དང་འབྲེལ་བ་ལ་ནི། ཐ་དད་པ་ཉིད་དེ་ཕྱོགས་གཞན་ལས་ཐ་དད་པར་གྱུར་པ་ཉིད་དོ། །

[Block 469]
དེའི་དེ་མནོད་པ་ཉིད་ལ་གཞན་གྱི་ཕྱོགས་སུ་གཏོགས་པའི་ཤི་བའི་ཡོ་བྱད་ལ་གཞན་གྱི་ཕྱོགས་སུ་གཏོགས་པ་ལ་འོས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 470]
ཆོས་དང་མཐུན་པའི་འདོད་པ༌[^420]ལ་བརྟེན་པ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 471]
འདིར་གཞུང་ནི། ཁས་བླངས་པ་རྣམས་ཀྱི་གནས་སུ་ཁས་མ་བླངས་པའི་དགེ་ཚུལ་འོངས་ཏེ། དུས་བྱས་པར་གྱུར་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 472]
ཆོས་དང་མཐུན་པའི་ཕྱོགས་ཁས་བླངས་པ་ནི་ཁས་བླངས་པ་ཡིན་ལ་ཆོས་མ་ཡིན་པ་དང་མཐུན་པའི་ཕྱོགས་ཁས་བླངས་པ་ནི་ཁས་མ་བླངས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 473]
རབ་ཏུ་བྱུང་བ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ལས་གཞན་པ་དག་དེ་མི་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ༌[^421]ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དག་ལས་གཞན་ཉེ་དུ་ལ་སོགས་པ་དང་། རྒྱལ་པོ་ལ་ཡང་རབ་ཏུ་བྱུང་བ་ཤི་བའི་ཡོ་བྱད་དེ་མི་དབང་བ་ཡིན་ཏེ། དེ་ནི་རབ་ཏུ་བྱུང་བ་དང་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དག་ཁོ་ན་དབང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 474]
འདིར་དགེ་སློང་ཞེས་མ་སྨོས་པ་ནི་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ཡང་དབང་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 475]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཞེས་སྨོས་པ་ནི་གཞན་མུ་སྟེགས་ཅན་བསལ་བའི་ཕྱིར་རོ། །

[Block 476]
གསོལ་བའམ་དང་པོ་དང་ཐ་མས་བྱིན་གྱིས་བརླབས་ཟིན་པ་ན་འོངས་པ་ནི་མི་དབང་ངོ་ཞེས་བྱ་བ་ནི་ཤི་བའི་ཡོ་བྱད་ལ་བྱིན་གྱིས་བརླབས་ཟིན་ཀྱང་རུང་སྟེ། གང་ཞིག་ཟིན་པ་ན་འོངས་པ་དེ་ལ་ཡང་དེ་དག་ནི་མི་དབང་བ་ཉིད་ཡིན་ནོ། །

[Block 477]
དེ་ལྟར་བྱུང་བ་བྱིན་གྱིས་བརླབ་པ༌[^422]མ་ཟིན་པ་ནི་དབང་བ་ཉིད་ཡིན་ནོ། །

[Block 478]
ལྷོ་ཕྱོགས་སུ་མཚན་མོའི་འོག་ཏུ་འདི་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་དུ་གསུངས་སོ། །

[Block 479]
དེ་ལ་གང་ཞིག་མདུན་རོལ་དུ་བྱིན་གྱིས་བརླབ་པ་གཉིས་པོ་འདི་བྱེད་པར་འགྱུར་བ༌[^423]དེས་གཞན་རྣམས་ལ་སྐལ་བ་མི་དབང་བ་ཉིད་དུ་ཡང་མི་འགྱུར་བ་ལས་དེ་མ་གྲགས་པ་ཉིད་ཀྱི་ཕྱིར་ལས་ཀྱི་ཆོ་ག་ལས་འདས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 480]
དེ་ལས་འགའ་ཞིག་དགེ་འདུན་གྱི་རྒན་པ་དང་གསར་བུ་གཉིས་ལ་བྱིན་པ་ནི་དེ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཤི་བའི་ཡོ་བྱད་དེ་ལས་སོ། །

[Block 481]
འགའ་ཞིག་ཅེས་བྱ་བ་ནི་དངོས་པོ་འགའ་ཞིག་གོ། །

[Block 482]
དགེ་འདུན་གྱི་རྒན་པ་དང་དགེ་འདུན་གྱི་གསར་བུ་གཉིས་ལས་བྱིན་པ་ནི་དང་པོ་དང་ཐ་མ་ཡིན་པ་ཞེས་བྱའོ། །

[Block 483]
འདིར་གཞུང་ནི། ཡོ་བྱད་གཅིག་བཙོངས༌[^424]ཏེ་ཅུང་ཞིག་དགེ་འདུན་གྱི་རྒན་པ་དང་དགེ་འདུན་གྱི་གསར་བུ་ལ་བྱིན་ནས་གསུངས་པ་ཡིན་ནོ། །

[Block 484]
དེ་ལ་དོན་གྱི༌[^425]དབང་གིས་ནི་འདིར་ཅུང་ཞིག་ཉིད་དང་། ཉོ་ཚོང་ཡང་ངེས་པ་ཅན་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་འདིར་མདོར་བྱས་སོ། །

[Block 485]
གང་ན་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་འདུག་པ་དེའི་མཚམས་སུ་གཏོགས་པ་རྣམས་བྱིན་གྱིས་རློབ་པར༌[^426]བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་གང་ན་བྱིན་གྱིས་བརླབ་པར་བྱ་བའི་དངོས་པོ་འདུག་པ་དེའི་མཚམས་སུ་གཏོགས་པའི་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་པོ་རྣམས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 486]
འདི་ལ་ཤི་བའི་གནས་ཉིད་ཀྱི་རྒྱུ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་ཤི་བའི་ཡོ་བྱད་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་འདི་ལ་ཤི་བའི་གནས་ཉིད་ནི་རྒྱུ་མ་ཡིན་པའོ། །

[Block 487]
འདིར་ཤི་བ་དེའི་དབང་གིས་མཚམས་དེ་ན་གནས་པ་རྣམས་ཀྱིས༌[^427]ཤི་བའི་ཡོ་བྱད་འདུག་པ་བྱིན་གྱིས་བརླབ་ཏུ་མི་རུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 488]
མཚམས་ཀྱི་བར་ན་འདུག་པ་ལ་ལུས་སམ་གཞན་གྱིས་རེག་པས་ཇི་ཙམ་ནོན་པ་དེར་གཏོགས་པ་རྣམས་སོ་ཞེས་བྱ་བ་ལ། མཚམས་ཀྱི་བར་ན་འདུག་པའི་ཤི་བའི་ཡོ་བྱད་དེ་ལ་ཤི་བ་དེའི་ལུས་ཀྱིས་རེག་གམ། གཞན་གྱིས་རེག་པའི་ཡོ་བྱད་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་དེས་མཚམས་ཇི་ཙམ་ནོན་ཅིང་ཁྱབ་པའི་མཚམས་དེར་གཏོགས་པའི་དགེ་སློང་རྣམས་ཀྱིས་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་ཡིན་ཏེ། འདི་ལ་ནི་བྱིན་གྱིས་བརླབ་པར་བྱ་བའི་རྫས་ཀྱི་དབང་གིས་རྣམ་པར་གཞག་གི་ཤི་བའི་རོའི་དབང་གིས༌[^428]ནི་མ་ཡིན་གྱི་ཞེས་བྱ་བ་དེ་ལ་བརྗོད་པ་སྟེ། མདོ་འདི་ནི་གླེང་གཞི་རྣམས་ལས་སོ། །

[Block 489]
གང་ན་ནོར་དང་འདྲ་བ་དེ་འདུག་པའི་ཁོངས་སུ་ཡོ་བྱད་གཏོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནོར༌[^429]དང་འདྲ་བར་འགྱུར་བའི་དངོས་པོ་དེ་ལ༌[^430]ཁྱིམ་པའམ་རབ་ཏུ་བྱུང་བའི་ནི་ནོར་དང་འདྲ་བའོ། །

[Block 490]
དེའི་ཁོངས་སུ་གཏོགས་པ་དེ་ནི་དེའི་ལུས་སུ་གྱུར་པ་སྟེ། འདི་འཛིན་པའི་བདག་ཉིད་ཅན་གྱི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 491]
དེ་ཁས་ལེན་པ་ཉིད་ལ་གང་དུ་འདི་ནོར༌[^431]དང་འདྲ་བར་འགྱུར་བ་དེའི་ཁོངས་སུ་ཡོ་བྱད་གཏོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 492]
དེའི་ཕྱིར་ནོར་དང་འདྲ་བས་གཞན་ན༌[^432]འདུག་པ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ན་འདུག་པས་ཀྱང་ཤི་བའི་ཡོ་བྱད་ཀྱི་ནོར་དང་འདྲ་བའི་གང་ཟག་དྲུང་ན་འདུག་པས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 493]
བསྐུར་བ་སྐུར་བར༌[^433]བྱ་བས་མ་སྤངས་པ་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྐུར་བའི་དངོས་པོ་མ་སྤངས་པ་ནི་གང་གིས་སྐུར་བར་བྱེད་པས་བསྐུར་བར་བྱ་བ་ནི། དེ་ཉིད་ཡིན་ཏེ་བསྐུར་བར་བྱ་བ་དང་བཅས་པ་ཉིད་དོ། །

[Block 494]
སྤངས་པ་ནི་སྐུར་བར་བྱེད་པ་ཉིད་ཀྱིའོ་ཞེས་བྱ་བ་ནི་སྐུར་བར༌[^434]བྱེད་པ༌[^435]ནི་སྐུར་བར་བྱེད་པ་ཉིད་དེ་དངོས་པོ་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི༌[^436]དོན་ཏོ། །

[Block 495]
དེས་སྤངས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ༌[^437]ནི་སྐུར་བར་བྱེད་པ་དེས་སོ། །
--- END BLOCKS ---
