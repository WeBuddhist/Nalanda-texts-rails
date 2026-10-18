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
གཏུབ་པ༌[^516]དང་གཤེགས་པ་ལ་སོགས་པའི་གཞིར་གྱུར་པའི་ཕྱིར་དམྱལ་བའོ། །

[Block 457]
ལྷ་མ་ཡིན་ནི་སྔར་བསྟན་པ་ཡིན་ནོ། །

[Block 458]
སྐྱེད་པའི་རྒྱུ་ནི་འགྲོ་བ་དྲུག་པོ་ཀུན་ཀྱང་རྣམ་པར་སྨིན་པའི་རྣམ་པར་ཤེས་པས་བསྐྱེད་པའི༌[^517]རང་བཞིན་ཅན་མ་བསྒྲིབས་ལ་ལུང་དུ༌[^518]མ་བསྟན་པའོ། །

[Block 459]
བསྡུ་བ་དང་དབྱེ་བ་ལ།

[Block 460 [VERSE]]
འགྲོ་བ་དྲུག་ཅེས་པ་ནི་བསྡུ་བའོ། །
དེ་ཡང་དགེ་བ༌[^519]བསྐྱེད་པ་དང་།
མི་དགེ་བ༌[^520]བསྐྱེད་པ་ནི་དབྱེ་བའོ། །

[Block 461]
ཡང་ན་འཁོར་བ་ཞེས་པ་ནི་བསྡུ་བའོ། །

[Block 462]
སྲིད་པ་གསུམ་དང་སྐྱེ་བ་རྣམ་བཞི་ནི་དབྱེ་བའོ། །

[Block 463]
གནས་ནི་ཁམས་གསུམ་པའོ། །

[Block 464 [HEADING]]
###### དཀོན་མཆོག་གསུམ་སྣང་བར་བྱས་པ། ^4-1-8-3-2-0

[Block 465]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དག་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས༌[^521]བཞུགས་ཤིང་འཚོ་སྐྱོང་བ་ནས་འབྲས་བུ་ཐོབ་པ་དང་མ་ཐོབ་པ་ཐམས་ཅད་ཀྱང་སྣང་ངོ་ཞེས་པ་ནི་འདི་ནི་དཀོན་མཆོག་གསུམ་འབྱུང་བ་བསྟན་པ་སྟེ། སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་སྣང་བའོ། །

[Block 466]
དགེ་འདུན་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཉན་ཐོས་ཀྱི་དགེ་འདུན་དང་བྱང་ཆུབ་སེམས་དཔའི་དགེ་འདུན་ནོ། །

[Block 467]
ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལ་ཡང་འཕགས་པའི་འབྲས་བུ་ཐོབ་པ་དང་རྣལ་འབྱོར་པ་ལམ་ལ་གནས་ཤིང་འབྲས་བུ་མ་ཐོབ་པ་དང་རྣམ་པ་གཉིས་སོ། །

[Block 468]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དག་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་པ་ནས༌[^522]སྤྱོད་པ་ཐམས་ཅད་སྣང་ངོ་ཞེས་པ༌[^523]ནི་བྱང་ཆུབ་སེམས་དཔའི་དགེ་འདུན་ཏེ། འགྲོ་བ་མང་པོ་སྡུག་བསྔལ་གྱི་ས་ནས་འདོན་པའི༌[^524]ཕྱིར་དད་པ་དང་ཐབས་སྣ་ཚོགས་ཀྱིས༌[^525]བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་འཛུད༌[^526]ཅིང་སྤྱོད་པ་དང་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་བརྒྱན་པའི་ཕྱིར་བསྡུ་བ་རྣམ་པ་བཞི་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་ཏེ་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་སྣ་ཚོགས་སྤྱོད་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་སྟེ། དད་པ་ནི་མོས་པས་སྤྱོད༌[^527]ཅིང་འཕགས་པའི་འབྲས་བུ་མ་ཐོབ་པའི་སའོ། །

[Block 469]
འགྲེལ་པ་ལས་ཀྱང་བསྡུ་བ་རྣམ་པ༌[^528]བཞིས་སེམས་ཅན་ཐམས་ཅད་ཐབས་སུ་སྡུད་ཅིང་བསྟན་པ་ལ་འཇོག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་སྟེ། སྦྱིན་པ་དང་ཚིག་སྙན་པ་དང་དོན་སྤྱོད་པ་དང་དོན་མཐུན་པས་འདྲེན་པའོ། །

[Block 470 [HEADING]]
###### མྱ་ངན་ལས་འདས་པའི་སྤྱོད་པ། ^4-1-8-3-3-0

[Block 471]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དག་ན་རིང་བསྲེལ་གྱི་མཆོད་རྟེན་རིན་པོ་ཆེ་ལས༌[^529]བྱས་པ་སྣང་ངོ་ཞེས་པ་ནི་མྱ་ངན་ལས་འདས་པའི་འོག་གི་སྤྱོད་པ་བསྟན་པ་སྟེ། མྱ་ངན་ལས་འདའ་བར༌[^530]འཇུག་པ་དང་མཆོད་རྟེན་བསྟན་པའོ། །

[Block 472]
མྱ་ངན་ལས་འདས་པ་ཡང་རྣམ་པ་དྲུག་སྟེ། རང་བཞིན་དང་མིང་དང་དུས་དང་གང་ཟག་དང་བསྟན་པ་དང་། མྱ་ངན་ལས་འདའ་བར་འཇུག་པའི་དོན་ཏོ། །

[Block 473]
རང་བཞིན་ལ་རྣམ་པ་བཞི་སྟེ། རང་བཞིན་གྱིས༌[^531]མྱ་ངན་ལས་འདས་པ་དང་། ལྷག་མ་དང་བཅས་པ་དང་། ལྷག་མ་མེད་པའི༌[^532]མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 474]
དེ་བཞི་སྤྱིར་མྱ་ངན་ལས་འདས་པ་སྟེ་ཡང་དག་པ་ཉིད་དུ་དོན་གཅིག་པའོ། །

[Block 475]
བཅོམ་ལྡན་འདས་མངོན་པར་བྱང་ཆུབ་ནས་སེམས་ཅན་མ་གྲོལ་བ་རྣམས་གྲོལ་བར་མཛད་དོ། །

[Block 476]
རྒྱུ་ཡོད་པ་རྣམས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་མཆོད་རྟེན་བཞག་པས་གྲོལ་བར་འགྱུར་བའི་རྒྱུ་བསྟན་ཏོ། །

[Block 477 [HEADING]]
#### གླེང་གཞི་ཆོས་འདྲི་བ། ^4-1-9-0

[Block 478]
མདོ་ལས་དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ༌[^533]བྱམས་པ་འདི་སྙམ་དུ་སེམས་ཏེ། དེ་བཞིན་གཤེགས་པས་ཆོ་འཕྲུལ་ཆེན་པོ་མཛད་པ་འདི་ཅིའི་ལྟས་ཞེས་པ་ནི་འཁོར་མང་པོ་རྣམས་ལྟས་དེ་དག་དབང་པོ་ཞན་པ་རྣམས་ཀྱིས་ཅིའི་ལྟས་སུ་བསྟན་པ་མི་ཤེས་པས་འཕགས་པ་བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པས་འགྲོ་བ་མང་པོའི་ཐེ་ཚོམ་བསལ་བའི་ཕྱིར་འདྲི་བར་བརྩམས་སོ། །

[Block 479]
མདོ་འདིའི་དོན་བདག་གིས་སུ་ལ་དྲི། ལན་ལྡོན་སུས་ནུས། དེ་ཡང་འདི་ལྟར་ཞེས་པ་ནས་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་དོན་འདི་འདྲིའོ་སྙམ་དུ་བསམས་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^534]ཆོ་འཕྲུལ་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ་འདི་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་འདྲིའོ་ཞེས་པ་ལེགས་པ་ཆེན་པོ་འཇམ་དཔལ་ལ་ཡོད་པ་བསྟན་པ་སྟེ། སྔོན་གྱི་རྒྱལ་བ་ལ་བྱ་བ་བྱས་ནས༌[^535]ཆོས་ཀྱི་རྒྱལ་ཚབ་ཏུ་དབང་བསྐུར་བ་སྟེ། འགྲེལ་པ་ལས་ཀྱང་དོན་ཟབ་མོ་གཅིག་ལ་དྲིས་དང་མང་པོ་ཐོས་པར་འགྱུར་བས་ཀུན་གྱི་ཐེ་ཚོམ་གཅོད་པ་ནི་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པའོ་ཞེས་འབྱུང་། ཡང་འགྲེལ་པ་ལས་ཀྱང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དགོངས་པ་མཐུན་པར་གྱུར་པས་སྒྲུབ་པ་དང་བཤད་པའི་ཆོས་གཉི་ག་འགྲུབ་པར་འགྱུར་བའི་ཕྱིར་ལྟས་ཆེན་པོ་བསྟན་པའི་དོན་དམ་པའི་ཆོས་འདི་ཉིད་བཤད་པའི་གླེང་གཞི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 480]
ཆོས་འདི་ཐེ་ཚོམ་ཅིའི་ཕྱིར་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་འབའ་ཞིག་ལ་དྲི་ཞེ་ན། དོན་རྣམ་པ་གཉིས་ཀྱི་ཕྱིར་ཏེ། ཆོས་འདི་ཉིད་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་འབའ་ཞིག་གིས་མངོན༌[^536]དུ་གྱུར་པའི་ཕྱིར་དང་། རང་གི་སེམས་ཀྱིས་རྟོགས་པ་ཉིད་ཡིན་གྱི། གཞན་ལ་མཉན་མི་དགོས་པའི་ཕྱིར་རོ། །

[Block 481]
ཡང་འགྲེལ་པ་ལས་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པས་དྲིས་པ་དེའི་ལུང་བསྟན་པར་ནུས་པ་ནི་འཇམ་དཔལ་དེ་ཕུན་སུམ་ཚོགས་པ་གཉིས་དང་ལྡན་པའི་ཕྱིར་ཏེ། བསོད་ནམས་ཕུན་སུམ་ཚོགས་པ་དང་ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 482]
རྒྱུ་དེ་གཉིས་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་ཆོས་དེ་སྟོན་པར་འོས་པའོ། །

[Block 483]
མདོ་ལས་དགེ་སློང་ཕ་དང་དགེ་སློང་མ་ནས་བདག་ཅག་གིས་སུ་ལ་དྲི་སྙམ་པའི་བར་དུ་ནི་དོན་སླ་བས་མ་བཤད་དོ། །

[Block 484]
དེ་ནས་ཡང༌[^537]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱམས་པས་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་འདི་སྐད་ཅེས༌[^538]སྨྲས་སོ་ཞེས་པ་ནི་དོན་རྣམ་པ་གཉིས་ཀྱིས༌[^539]གླེང་གཞི་ཆོས་འདྲི་བ་ལ་སྔར་ནི་ཚིག་ལྷུག་པས་བཤད། དེའི་འོག་ཏུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 485 [HEADING]]
##### ཚིག་ལྷུག་པས་བཤད་པ། ^4-1-9-1-0

[Block 486]
[^540]མདོ་ལས་འཇམ་དཔལ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^541]གང་འདི་ལྟ་བུའི་ལྟས་ཞེས་པ་ནས་འདི་ཅིའི་རྒྱུ་ཅིའི་རྐྱེན་ཞེས་པའི་བར་དུ་ནི་ལྟས་དང་ཆོ་འཕྲུལ་དྲི་བ་བསྡུ་བའོ། །

[Block 487]
ཞིང་འདི་དག་སྣ་ཚོགས་བལྟ༌[^542]ན་སྡུག་པ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་ཞིང་རྣམ་པ་སྣ་ཚོགས་ཏེ། ཞིང་ཡོངས་སུ་དག་པ་དང་མ་དག་པ་རྣམས་སོ། །

[Block 488]
སངས་རྒྱས་ཐོག་མར་བཞུད་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་འདྲེན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 489 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན་པ། ^4-1-9-2-0

[Block 490]
མདོ་ལས་ཚིགས་སུ་བཅད་པ་འདི་གསུངས་པ་ནི་འདི་ཚིགས་བཅད་ཀྱི༌[^543]བསྡུ་བ་སྟེ་དུམ་བུ་བཅུར་དབྱེའོ། །

[Block 491]
དབང་པོ་རྣོ་རྟུལ༌[^544]གཉི་ག་ལ་ཕན་པ་དང་སྔ་ཕྱི་རྣམ་གཉིས་ཀྱི་འཁོར་བ༌[^545]ལ་ཕན་གདགས་པ་དང་། དྲང་པོ་དང་དེ་མ་ཡིན་པ་གཉིས་དགའ་བར་བྱ་བ་དང་། དཀའ་སླ་གཉི་གའི་ཆེད་དང་དོན་དམ་པ་དང་ཀུན་རྫོབ་གཉི་གའི་དོན་དང་། བླང་དོར་གཉི་གའི་ཆ་དང་། གསལ་མི་གསལ་དབྱེ་བ་དང་། ཤེས་པ་དང་སྤོབས་པ་དབྱེ་བ་དང་། ཐེ་ཚོམ་དང་འཆིང་བ་དབྱེ་བ་དང་། བཤད་པ་དང་སྤྱོད་པ་བསྟན་པའོ། །

[Block 492]
མདོ་ལས་འཇམ་དཔལ་ཞེས་པ་ནས་ཞལ་གྱི་མཛོད་སྤུ་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་འདི་དག་ལ་རྩ་བ་དྲུག་ཅུ་རྩ་གཉིས་ཡོད་དེ། དུམ་བུ་གཉིས་སུ་དབྱེའོ། །

[Block 493]
དང་པོ་རྩ་བ་ལྔ་བཅུ་རྩ་བཞིས་ནི་ལྟས་རྣམས་ཀྱི་དོན་བསྟན། རྩ་བ་བརྒྱད་ཀྱིས་ནི་དོན་འདྲི་བའོ། །

[Block 494 [HEADING]]
###### ལྟས་རྣམས་ཀྱི་དོན་བསྟན་པ། ^4-1-9-2-1-0

[Block 495 [HEADING]]
###### **འོད་ཀྱིས་སྣང་བར་མཛད་པའི་གླེང་གཞི།** ^4-1-9-2-1-1-0
--- END BLOCKS ---
