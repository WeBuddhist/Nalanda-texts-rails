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
[Block 596]
རྣམ་པར་རྟོག་པ་རྣམས་ནི་དེའི་ཆོས་ཉིད་ཁོ་ན་ལ་འཇུག་པ་ན་ཆོས་དུ་མ་དང་གཅིག་པ་དང་ཐ་དད་པ་དག་ཏུ་སྟོན་པར་བྱའོ།[^441] །དེ་རྣམས་རྟེན༌[^442]མེད་པ་ཡང་མ་ཡིན་ཏེ། དེའི་ཁྱད་པར་མཐོང་བ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 597]
དངོས་པོ་མེད་པའི་ཆོས་ཉིད་ཀྱང་མ་ཡིན་ཏེ། དེའི་རང་གི་ངོ་བོ་ཁོ་ན་དེ་ལྟར་སྣང་བའི་ཕྱིར་རོ། །

[Block 598]
དངོས་པོ་ལ་དུ་མ་དང་གཅིག་པ་དང་ཐ་དད་པར་འཛིན་པ་ནི་འཁྲུལ་པར་འགྱུར་ཏེ། དོན་གཅིག་དང་དུ༌[^443]མ་བྱེད་པ་དེ་ལ་དེ་ལྟར་ཤེས་པར་འདོད་ན་དེ་ལྟ་བུའི་ངོ་བོ་བསྟན་པའི་ཆེད་དུ་དེ་ལྟར་གཞག་པར་བྱས༌[^444]པའི་ཕྱིར་རོ། །

[Block 599]
དངོས་པོའི་ཁྱད་པར་གྱི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། གཅིག་པོ་དེ་ལ་དུ་མ་ཉིད་མི་རུང་བའི་ཕྱིར་དང་། དུ་མ་ལའང་གཅིག་པ་ཉིད་མི་རུང་བའི་ཕྱིར་དང་། ཐ་དད་པ་ཡང་བཀག་པའི་ཕྱིར་རོ། །

[Block 600]
དེ་རྣམས་ཀྱི་རང་བཞིན་ཐ་དད་པའི་ཕྱིར། སྒྲའི་དོན་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་ཡིན་པར་ཁས་ལེན་ན་གཞི་མཐུན་པ་ཉིད་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 601]
གལ་ཏེ་ཁྱད་པར་དེ་དག་དང་ལྡན་པ་གཅིག་བརྗོད་པའི་ཕྱིར། ཉེས་པ་མེད་དོ་ཞེ་ན། ཕན་མི་འདོགས་པ་ལ་གཞན་གྱི་དབང་ཉིད་མི་རུང་བའི་ཕྱིར་ཁྱད་པར་མ་ཡིན་ནོ། །

[Block 602]
གཞན་གྱི་དབང་ཉིད་ཡིན་ན་ནི་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པའི་དངོས་པོ་ཡིན་པས་ལྷན་ཅིག་མི་གནས་པའི་ཕྱིར། གཉིས་སུ་བརྗོད་པ༌[^445]མ་ཡིན་ནོ། །

[Block 603]
བློས་གཅིག་སྒྲོ་བཏགས༌[^446]ན་ནི་སྒྲ་དངོས་པོའི་ཡུལ་ཅན་དུ་མི་འགྱུར་རོ། །

[Block 604]
བློ་ལ་སྣང་བའི་ཡུལ་ཅན་ཉིད་གཅིག་ཡིན་ན་ནི་ཐམས་ཅད་ཀྱང་དེ་ཁོ་ན་དང་འདྲ་བར་འགྱུར་ཏེ། འཛིན་པ་ལ་དེ་ལྟ་བུའི་ཁྱད་པར་ཐ་དད་པ་དང་ལྡན་པ་གཅིག་པུ་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 605]
གལ་ཏེ་ཁྱད་པར༌[^447]དེ་དང་ལྡན་པ་ཕན་པར་བྱ་བ་དང་། ཕན་པར་བྱེད་པ་དག་ཀྱང་ལྷན་ཅིག་གནས་པའི་ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། གྲུབ་པ་ལ་གཞན་གྱི་དབང་མེད་པའི་ཕྱིར་ཁྱད་པར་ཉིད་མ་ཡིན་ནོ། །

[Block 606]
མ་གྲུབ་པ་ཡང་མ་ཡིན་ཏེ། རང་གི་ངོ་བོར་མ་རེང་པའི༌[^448]ཕྱིར་རོ། །

[Block 607]
རྣམ་པ་ཐམས་ཅད་དུ་གཞན་གྱི་དབང་ཉིད་མེད་པས་རྟོགས་པས་སྒྲོ་གདགས་པར༌[^449]བྱས་ནས། ཐ་སྙད་འདོགས་ན་ནི་ཐམས་ཅད་དུ་བློ་དེ་ཁོ་ན༌[^450]ཅི་སྟེ་མི་སྦྱོར། སྒྲ་དང་ཚད་མ་གཅིག་གིས་ཡུལ་དུ་བྱས་ན༌[^451]དངོས་པོའི་སྟོབས་ཀྱིས་ཁྱད་པར་མ་ལུས་པ་འཕངས་པའི་ཕྱིར། དེ་ལས་གཞན་པ་དོན་མེད་པར་ཡང་མི་འགྱུར་ཏེ། བློ་ལ་སྣང་བ་ནི་དངོས་པོ་མེད་པའི་ཕྱིར། དངོས་པོའི་མཐུ་ལས་འབྱུང་བ་རྣམས་སུ་ཐལ་བ་མེད་དོ། །

[Block 608]
དེ་ཐ་མི་དད་པ་ཡང༌[^452]རྣམ་པ་གཅིག་གི༌[^453]ཡུལ་དུ་བྱས་ཀྱང་རྣམ་པ་གཞན་མ་ངེས་པ་རྣམས་རྣམ་པ་གཞན་ལ༌[^454]རེ་བ་དང་བཅས་པའི་བློས་གཟུང་བར་བྱ་བ་དང་། སྒྲའི་དོན་ཐ་དད་པ་བསྒྲུབ་པ༌[^455]དག་ཀྱང་ཐ་མི་དད་པར་བློ་ལ་སྣང་བས་སྤྱི་དང་ཁྱད་པར་དང་ཁྱད་པར་གྱི་གཞིའི་དངོས་པོ་དང་། གཞི་མཐུན་པ་རྣམས་ཇི་ལྟར་ཤེས་པ་བཞིན་མི་འགལ་ལོ། །

[Block 609]
འདིའི་ཆོས་དང་ཆོས་ཅན་གྱི་ཁྱད་པར་དག་ཀྱང་དོན་དུ་མ་ལས་ཐ་དད་པ་ལ། དོན་གཅིག་ཅིག་ལས་ཐ་དད་པ་དེ་སྒྲུབ་པ་དང་། དགག་པ་ཤེས་པར་འདོད་པ་དང༌[^456]དངོས་པོ་དེ་ཁོ་ན་ཆོས་ཞེས་བྱ་བའི་སྒྲ་ཁྱད་པར་གཞན་སྤངས་པས༌[^457]བརྗོད་ནས་བློ་ལ་དེ་ལྟར་སྣང་བའི་ཕྱིར། [^458]ཆོས་ཐ་དད་པ་ལྟ་བུ་དང་བྱེ་བྲག་ཏུ་མ་ཕྱེ་བར་འདིའི་ངོ་བོ་ཉིད་གཞན་ཆོས་ཅན་ཉིད་དུ་རྣམ་པར་བཞག་ནས་རབ་ཏུ་སྟོན་ཏོ། །

[Block 610]
དེ་ཙམ་གྱི་ཆས་ཆོས་དང་ཆོས་ཅན་དག་ཐ་དད་པའི་ཕྱིར། བློ་ཐ་དད་པ་དང་ལྡན་པ་ལྟ་བུར་སྣང་གི་དངོས་པོ་ཐ་དད་པའི་ཕྱིར་ནི་མ་ཡིན་ཏེ། ཇི་སྐད་བཤད་པའི་ཉེས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 611]
ཐ་དད་པ་དེ་ལྟ་བུ་མང་པོ་བརྗོད་པས་ཚིག་ཐ་དད་པ་དང་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པ་ཐ་དད་པ་ཆོས་སྣང་བའི་ཁྱད་པར་དེའི་རང་གི༌[^459]ངོ་བོ་ལ་བརྟེན་པ་ཅན་དག་གིས། དེའི༌[^460]རང་གི་ངོ་བོས་རྟོགས་པར་བྱ་བའི་ཕྱིར་བྱེད་དོ། །

[Block 612 [VERSE]]
རང་བཞིན་དེ་འཛིན་རྣམ༌[^461]རྟོག་བློ། །
དོན་མེད་ཀྱང་དེའི་དོན་ཅན་འདྲ། །
དེ་ཡི་འབྲས་ཅན་མིན་དོན་ལས། །
ཐ་དད་མཐར་ཐུག༌[^462]སྐྱེ་བ་དང་།

[Block 613]
[^463] །

[Block 614 [VERSE]]
དེ་ལ་ངོ་བོ་ཕྱི་རོལ་དང་། །
གཅིག་ལྟར་གཞན་ལས་ལོག་ལྟ་བུར། །
སྣང་བ་གང་ཡིན་བརྟག་པ་ཡི། །
ཡན་ལག་མེད་ཕྱིར་དེ་ཉིད་མིན། །

[Block 615 [VERSE]]
ཤེས་པ་ཡོད་པའི་དོན་དེ་རྣམས། །
འདི་ལྟར་ལྡོག་པའི་ངོ་བོ་ཅན། །
དེས་ན་ཐ་དད་མིན་ལྟ་བུར། །
དེ་ཉིད་གཞན་ལས་ལོག་པར་ཡང་། །

[Block 616 [VERSE]]
སྣང་སྟེ་དེ་ལ་སྤྱི་དང་ནི། །
གཞི་མཐུན་སྤྱོད་ཡུལ་ཅན་དག་གི །
ཤེས་པ་དང་ནི་བརྗོད་པ་ཡིས། །
ཐ་སྙད་ནོར་དོན་ཅན་རྒྱས་བྱེད། །

[Block 617 [VERSE]]
དངོས་པོ་ཀུན་གྱི་དེ་ཀུན་ཀྱང་། །
ཕན་ཚུན་མེད་ལ་བརྟེན་པ་སྟེ། །
དེས་ན་གཞན་སེལ་ཡུལ་ཅན་དང་། །
གང་ལ་དངོས་དང་འབྲེལ་ཡོད་པ། །
དངོས་པོ་མེད་པའི༌[^464]རྟེན་ཡིན་ཏེ། །
རྗེས་དཔག་ཇི་སྐད་བཤད་ཇི་བཞིན། །
འཁྲུལ་པར་འདྲ་ཡང་གཞན་ལ་མིན།

[Block 618]
[^465] །

[Block 619 [VERSE]]
མར་མེའི་འོད་ལ་ནོར་བུ་བཞིན། །
དེ་ལའང་དུ་མ་འབྲས་གཅིག་ཅན། །
དེ་འབྲས་ཅན་མིན་གཞན་རྟེན༌[^466]ཅན། །
བརྗོད་དང་ཤེས་པས་གཅིག་ཉིད་དུ།

[Block 620 [VERSE]]
ཐ་དད༌[^467]རབ་ཏུ་འཇུག་པར་བྱེད། །
དེ་བཞིན་གཅིག་ཀྱང་དུ་མ་བྱེད། །
དེའི༌[^468]དངོས་ཡོངས་སུ་བསྟན་པའི་ཕྱིར། །

[Block 621]
དེ་ཡི་འབྲས་ཅན་མིན་དོན་ལས།

[Block 622]
[^469] །

[Block 623 [VERSE]]
ཐ་དད་པས་ཆོས་སྣ་ཚོགས་ཤེས། །
སྒྲ་དོན་འདི་དང་གཞི་མཐུན་ཉིད། །
ཡོད་པ་མིན་ཡང་ཇི་ལྟ་བུར། །
གྲགས་པ་བཞིན་དུ་བརྗོད་བ་སྟེ། །

[Block 624 [VERSE]]
དངོས་པོ༌[^470]འདི་ནི་མི་སྲིད་དོ། །
ཆོས་དང་ཆོས་ཅན་རྣམ་གཞག་དང་། །
ཐ་དད་ཐ་དད་མིན་ཅི་འདྲ། །
དེ་ཉིད་དོན་ནི་མ་བརྟགས་པ། །

[Block 625 [VERSE]]
འཇིག་རྟེན་ཇི་ལྟར་གྲགས་དེ་ལ། །
དེ་བཞིན་ཁོ་ནར་བརྟེན་ནས་ནི། །
བསྒྲུབ་བྱ་སྒྲུབ་པ་ཀུན་གཞག་པ། །
དམ་པའི་དོན་ལ་འཇུག་བྱའི་ཕྱིར། །

[Block 626 [VERSE]]
མཁས་པ་རྣམས་ཀྱིས་བྱས་པ་ཡིན། །
དམ་པའི་དོན་གྱིས་དོན་རྣམས་ནི། །
རང་གིས༌[^471]འདྲེ་དང་ཐ་དད་མེད། །
དེ་ལ་ངོ་བོ་གཅིག་པ་དང་། །

[Block 627 [VERSE]]
དུ་མ་བློ་ཡིས་བསླད་པ་ཡིན། །
དེ་སྤྱི་ཁྱད་པར་ཞེས་བྱ་བའི། །
བྱེ་བྲག་འདི་ནི་བློ་དོན་ལ། །
དེ་ཉིད་ལ་གཞན་ལས་ལྡོག་པས། །

[Block 628 [VERSE]]
ཆོས་ཀྱི་བྱེ་བྲག་རབ་ཏུ་བརྟག །
བསྒྲུབ་བྱ་སྒྲུབ་པར་རྟོགས་པ༌[^472]ལ། །
དངོས་པོ་མཐོང་བ་ཉམས་པའི་ཕྱིར། །
ཁྱད་པར་སྤྱི་དང་འདྲེས་པ་འདིར། །

[Block 629 [VERSE]]
རང་གི་མཚན་ཉིད་གཟུང་བྱ་མིན། །
དེ་ནི་སྤྱི་དང་ཁྱད་པར་གྱི། །
རྣམ་སོགས་ཅིར་ཡང་གཟུང་བྱ་མིན། །
བྱེ་བྲག་ཁྱད་པར་མང་པོ་རྣམས། །

[Block 630 [VERSE]]
དེ་གཅིག་ལ་ནི་མི་རུང་ཕྱིར། །
དེ་ཡི་ངོ་བོ་ཀུན་ལས་ལོག །
དེ་དེ་བཞིན་དུ་རྟོགས་བྱེད་པའི། །
སྒྲ་ཡོད་མ་ཡིན་རྟོགས་པ༌[^473]ཡང་། །
སྤྱི་ཉིད་དུ་ནི་འཇུག་ཕྱིར་རོ། །
ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 631 [HEADING]]
### རང་གི་མཚན་ཉིད་ལ་སྒྲ་རྣམས་མི་སྦྱོར་བ། ^4-2-0

[Block 632]
ཡང་ཅིའི་ཕྱིར་རང་གི་མཚན་ཉིད་ལ་སྒྲ་རྣམས་མི༌[^474]སྦྱོར་ཞེ་ན།

[Block 633 [VERSE]]
སྒྲ་རྣམས་ཀྱིས་ནི་བརྡར་བཏགས༌[^475]སྟོན། །
དེ་ནི་ཐ་སྙད་ཆེད་དུ་བྱས། །
དེ་ཚེ་རང་གི་མཚན་ཉིད་མེད། །
དེས་ན་དེ་ལ་བརྡར་མ༌[^476]ཡིན། །

[Block 634]
སྒྲ་རྣམས་ཀྱིས་ནི་བརྡར་བཏགས་པའི་དོན་རབ་ཏུ་སྟོན་པར་བྱེད་ལ། བརྡ་ཡང་ཅི་ནས་ཀྱང་དུས་ཕྱིས་བརྡར་བྱས་པའི་སྒྲ་འདི་ལས་དོན་འདི་རྟོགས་པར་འགྱུར་སྙམ་ནས་ཐ་སྙད་ཀྱི་དོན་དུ་འདོགས་ན། སྔར་རང་གི་མཚན་ཉིད་ལ་བརྡར་བྱས་པའི་སྒྲ་ཕྱིས་སྦྱོར་བ་ནི་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་བསལ་བ༌[^477]ཡུལ་དང་དུས་ཀྱི་ཐ་དད་པ་ལ་མི་འབྲང་བའི་ཕྱིར་རོ། །

[Block 635]
དེ་ལྟ་བས་ན་རང་གི་མཚན་ཉིད་ལ་བརྡར་བྱེད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
