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
ལན་གསུམ་པ་བརྗོད་པའི་ཚེ་རྣམ་པར་རིག་བྱེད་དང་དེའི་སྐད་ཅིག་གི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཡིན་པ༌[^448]འདི་ནི་ལས་ཀྱི་ལམ་དངོས་ཡིན་ནོ། །

[Block 632]
དེའི་འོག་ཏུ་ཇི་སྲིད་དུ་གནས་བསྒོ་བའམ།[^449] དེའི་རྟེན༌[^450]རྣམ་པར་རིག་པར་བྱེད་པ་དང་། ཇི་སྲིད་དུ་རྣམ་པར་རིག་པར༌[^451]བྱེད་པ་མ་ཡིན་པ་རྗེས་སུ་འབྲང་བ་འདི་ནི་མཇུག༌[^452]ཡིན་ནོ། །

[Block 633 [HEADING]]
### ལས་ཀྱི་ལམ་མཐར་ཕྱིན་པར་བྱེད་པ། ^1-44-0

[Block 634]
ལས་ཀྱི་ལམ་ཐམས་ཅད་ཆགས་པ་ལ་སོགས་པས་མཐར་ཕྱིན་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་གང་བཤད་ན། འོ་ན་གང་ཞིག་གང་གིས་མཐར་ཕྱིན་པར་བྱེད་ཅེ་ན།

[Block 635 [VERSE]]
གསོད་དང་གནོད་སེམས་ཚིག་རྩུབ་པོ། །
ཞེ་སྡང་གིས་ནི་མཐར་ཕྱིན་བྱེད། །

[Block 636]
སྲོག་གཅོད་པ་དང་། གནོད་སེམས་དང་། ཚིག་རྩུབ་པོ་དང་འདི་དག་ནི་ཞེ་སྡང་གིས་མཐར་ཕྱིན་པར་བྱེད་དེ། ཡོངས་སུ་འདོར་བ་དང་། རྩུབ་པའི་སེམས་མངོན་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 637 [VERSE]]
ལོག་གཡེམ་བརྣབ་སེམས་མ་བྱིན་ལེན། །
ཆགས་པ་སེམས༌[^453]ནི་རྫོགས་པར་བྱེད། །

[Block 638]
འདོད་པས་ལོག་པར་གཡེམ་པ་དང་། བརྣབ་སེམས་དང་། མ་བྱིན་པར་ལེན་པ་རྣམས་ནི་ཆགས་པས་རྫོགས་པར་བྱེད་དོ། །

[Block 639]
ལོག་པར་ལྟ་བ་གཏི་མུག་གིས། །ཆེར་རྨོངས་པར་གྱུར་ན་མཐར་ཕྱིན་པར་བྱེད་དོ། །

[Block 640]
ལྷག་མ་གསུམ་གྱིས་རྫོགས་པར་འདོད།[^454] །ལྷག་མ་ཡང་གང་དག༌[^455]ཅེ་ན། བརྫུན་དུ་སྨྲ་བ་དང་། ཕྲ་མ་དང་། ཚིག་ཀྱལ་པ་སྟེ། དེ་དག་ནི་ཆགས་པའམ། ཞེ་སྡང་ངམ། གཏི་མུག་གསུམ་ཀས༌[^456]ཀྱང་མཐར་ཕྱིན་པར་བྱེད་དོ། །

[Block 641 [HEADING]]
### ལས་ཀྱི་ལམ་གྱི་གཞི། ^1-45-0

[Block 642]
གང་འདི་ལས་ཀྱི་ལམ་ཆ་བཞིར་བཤད་པ་དེ་དག་ནི་གསུམ་དང་། གསུམ་དང་། གཅིག་དང་། གསུམ་དང་། གོ་རིམས་བཞིན་ཏེ།

[Block 643 [VERSE]]
གཞི༌[^457]ནི་སེམས་ཅན་ལོངས་སྤྱོད་དང་། །
མིང་དང་གཟུགས་དང་མིང་ཡིན་ནོ། །

[Block 644]
སྲོག་གཅོད་པ་ལ་སོགས་པའི་གཞི་ནི་སེམས་ཅན་ཡིན་ནོ། །

[Block 645]
གཞན་གྱི་བུད་མེད་ཀྱི་གན་དུ་འགྲོ་བ་ལ་སོགས་པའི་གཞི་ནི་ལོངས་སྤྱོད་ཡིན་ནོ། །

[Block 646]
ལོག་པར་ལྟ་བའི་གཞི་ནི་མིང་དང་། གཟུགས་ཡིན་ནོ། །

[Block 647]
བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པའི་གཞི་ནི༌[^458]མིང་གི་ཚོགས་ཡིན་ནོ། །

[Block 648 [HEADING]]
### སྔ་དང་མཉམ་དུ་ཤི་བ། ^1-46-0

[Block 649]
གང་ཞིག་གི༌[^459]ཕ་རོལ་པོ་འཆི་བར་ངེས་པར་བྱས་ནས་དེ་དང་མགོ་མཉམ་དུ་འམ་སྔར་ཤི་ན་ཅི་དེ་ལ་ལས་ཀྱི་ལམ་དངོས་ཡོད་དམ་འོན་ཏེ་མེད་ཅེ་ན།

[Block 650 [VERSE]]
སྔ་དང་མཉམ་དུ་ཤི་བ་ལ། །
དངོས་པོ༌[^460]མེད་དེ་ཉིད་ཀྱི་ཕྱིར། །

[Block 651]
སྦྱོར་བ་ཡང་བྱས་ལ་འབྲས་བུ་ཡང་ཡོངས་སུ་རྫོགས་པར་གྱུར་ཀྱང་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་མི་འགྱུར་བ་ལྟ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། འདི་ལྟ་སྟེ་གསོད་པ་པོ་སྔར་རམ་མཉམ་དུ་ཤི་བར་གྱུར་པ་ལྟ་བུའོ་ཞེས་གསུངས་སོ། །

[Block 652]
དེ་ལ་རྒྱུ་ཅི་ཞིག་ཡོད་ཅེ་ན། གསད་པར་བྱ་བ་གསོན་བཞིན་དུ་གསོད་པ་པོ་ལ་ཁ་ན་མ་ཐོ་བ་དང་ལྡན་པ་ཡང་མེད་ལ། གསོད་པ་པོ་ཤི་བ་ལ་ཡང་མ་ཡིན་ཏེ། ལུས་གཞན་སྐྱེས་ཕྱིར་རོ། །

[Block 653]
ལུས་གང་གིས་དེ་ལ་སྦྱོར་བ་བྱས་པ་དེ་ནི་ཆད་ལ་རིས་མཐུན་པ་ཐ་དད་པ་གཞན་གྱི་ལུས་ཁོ་ན་ཞིག་བྱུང་སྟེ། དེ་ནི་སྦྱོར་བ་པོ་མ་ཡིན་པའི་ཕྱིར་ལས་ཀྱི་ལམ་དང་ལྡན་པར་རིག་པ༌[^461]མ་ཡིན་ནོ། །

[Block 654 [HEADING]]
### དམག་ལ་སོགས་པར་དོན་གཅིག་པ། ^1-47-0

[Block 655]
གང་དམག་གིས༌[^462]གདབ་པ་དང་། ལིངས་འདེབས་པ་དང་། མ་འཕྲིགས་པར་གདབ་པ་དག་ཏུ་ཕ་རོལ་པོ་གསད་པར༌[^463]བྱ་བའི་ཕྱིར་མང་པོ༌[^464]ཚོགས་པས་བཏབ༌[^465]ལ་གཅིག་ཅིག་གིས་སྲོག་གཅོད་ན་དེ་དང་སུ་ཞིག་ལྡན་པར་འགྱུར་ཞེ་ན།

[Block 656 [VERSE]]
དམག་ལ་སོགས་པར༌[^466]དོན་གཅིག་ཕྱིར། །
ཐམས་ཅད་བྱེད་པ་བློ༌[^467]བཞིན་ལྡན། །

[Block 657]
དོན་གཅིག་པའི་ཕྱིར་ཐམས་ཅད་བྱེད་པ་པོ་ཇི་ལྟ་བ་བཞིན་ལྡན་པར་འགྱུར་ཏེ། དེ་དག་ནི་དོན་གྱིས་ན་ཕན་ཚུན་དུ་སྦྱོར་བར་བྱེད་པ༌[^468]ཡིན་ནོ། །

[Block 658]
འོ་ན་གང་ཞིག་ནན་གྱིས་ཁྲིད་པ་དེ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ཡང་ལྡན་པར་འགྱུར་བ་སྟེ།[^469] གང་ཞིག་འདི་སྙམ་དུ་སྲོག་གི་ཕྱིར་ཡང་སྲོག་ཆགས་མི་གསོད་དེ༌[^470]ཞེས་བྱ་བར་ངེས་པར་བྱས་ཏེ་འགྲོ་བ་ནི་མ་གཏོགས་སོ། །

[Block 659 [HEADING]]
### ལས་ཀྱི་ལམ་བཅུ་པོའི་མཚན་ཉིད། ^1-48-0

[Block 660]
རང་གི༌[^471]སྲོག་གཅོད་པར་བྱེད་པ་ལ་ཇི་ཙམ་གྱིས་ལས་ཀྱི་ལམ་དུ་འགྱུར་ཞེས་བྱ་བ་ནས་ཇི་ཙམ་གྱིས་ན་ལོག་པར་ལྟ་བའི༌[^472]ལས་ཀྱི་ལམ་དུ་འགྱུར་ཞེས་བྱ་བའི་མཚན་ཉིད་བརྗོད་པར་བྱ་སྟེ། དེ་བརྗོད་དོ། །

[Block 661 [HEADING]]
#### སྲོག་གཅོད་པ། ^1-48-1-0

[Block 662]
སྲོག་གཅོད་པ་ནི་བསམས་བཞིན་དུ་མ་ནོར་བ༌[^473]ནི་གཞན་གསད་པའོ། །

[Block 663]
གལ་ཏེ་འདི་བསད༌[^474]དོ་སྙམ་དུ་བསམས་ནས་གསོད་པར་བྱེད་ལ། གཞན་དང་མ་ནོར་བར་དེ་ཉིད་ཀྱང་གསོད་པར་བྱེད་ན་དེ་ཙམ་གྱིས་སྲོག་གཅོད་པ༌[^475]ཡིན་ནོ། །

[Block 664]
འོ་ན་གང་ཞིག་འདི་ཅི་སྲོག་ཆགས་སམ་སྲོག་ཆགས་མ་ཡིན། དེ་འམ་གཞན་ཞིག་ཡིན་སྙམ་དུ་ཐེ་ཚོམ་ཟོས་ནས་གསོད་པར་བྱེད་པ་དེ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ཡང་གདོན་མི་ཟ་བར་གང་ཡིན་པ་ཡིན་ཞེས་བྱ་བའི་ངེས་པ་འདི་རྙེད་ནས་དེ་ལ་སྣུན་པར་བྱེད་པས་དེས་ན་འདོར་བའི་སེམས་སུ་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 665]
ཕུང་པོ་སྐད་ཅིག་མ་རྣམས་ལ་ཇི་ལྟར་སྲོག་གཅོད་པ་ཡིན་ཞེ་ན། སྲོག་ཞེས༌[^476]བྱ་བ་ནི་ལུས་དང་སེམས་ལ་བརྟེན་ནས་འཇུག་པའི་རླུང་ཡིན་ཏེ། དེ་གཅོད་པར་བྱེད་དོ། །

[Block 666]
དཔེར་ན་མར་མེ་འམ། དྲིལ་བུའི་སྐད་འགག་པར་བྱེད་པ་དང་འདྲའོ། །

[Block 667]
ཡང་ན་སྲོག་གི་དབང་པོ་སྲོག་ཡིན་ཏེ། དེ་འགག་པར་བྱེད་དོ། །

[Block 668]
གལ་ཏེ་སྲོག་གི་དབང་པོའི་སྐད་ཅིག་མ་གཅིག་སྐྱེ་བ་ལ་བར་ཆད་བྱེད་ན་ཡང་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 669]
དེ་མེད་པས་གང་ཞིག་འཆི་བར་འགྱུར་བའི་སྲོག་དེ་གང༌[^477]ཡིན་ཞེ་ན། གང་གི་ཞེས་བྱ་བའི་དྲུག་པ་ནི་གང་ཟག་ཏུ་སྨྲ་བ་དགག་པར་དཔྱད་པར་བྱའོ། །

[Block 670]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་།
--- END BLOCKS ---
