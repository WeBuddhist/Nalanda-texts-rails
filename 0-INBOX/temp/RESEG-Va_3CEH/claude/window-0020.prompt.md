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
[Block 701]
གཅིག་པུ་ཉིད་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོའི་གཞུང་ནི་གཟུགས་ཀྱི་སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། གལ་ཏེ་གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པ་དག་གཅིག་ཡིན་ན་དེས་ན་གཞན་གྱི་དབང་ཡང་ཡོངས་སུ་གྲུབ་པ་བཞིན་དུ་དམིགས་པ་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 702 [HEADING]]
##### ཐ་དད་པ་ཉིད་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-6-0

[Block 703]
ཐ་དད་པ་ཉིད་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོའི་གཞུང་ནི་གཟུགས་ནི་སྟོང་པ་ཉིད་ལས་གཞན་པ་ཡང་མ་ཡིན་ཏེ། གཟུགས་ཉིད་སྟོང་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཕྱིར་དེ་དག་ཐ་དད་པ་ཡིན་ན་ཆོས་ལས་ཆོས༌[^487]ཉིད་ཐ་དད་པ་ཉིད་དུ་འགྱུར་ན། ཐ་དད་པ་ཉིད་དུ་འགྱུར་བ་ནི་མི༌[^488]རུང་བ་མ་ཡིན་ཏེ། མི་རྟག་པའི་མི་རྟག་པ་ཉིད་བཞིན་ནོ། །

[Block 704]
ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཡོངས་སུ་བཟུང་ནས་གཟུགས་ཉིད་སྟོང་པ་ཉིད་དོ། །

[Block 705]
སྟོང་པ་ཉིད་གཟུགས་སོ་ཞེས་བྱ་བ་སྟེ། གང་ཀུན་ཏུ་བརྟགས་པ༌[^489]དེའི་ངོ་བོ་ཉིད་མེད་པ་དེ་ནི་སྟོང་པ་ཉིད་ཡིན་ལ། གང་སྟོང་པ་ཉིད་ཡིན་པ་དེ་ནི་དེའི་ངོ་བོ་ཉིད་མེད་པ་ཡིན་གྱི། ཇི་ལྟར་གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པ་དག་ནི་མ་ཡིན་ནོ། །

[Block 706 [HEADING]]
##### ངོ་བོ་ཉིད་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-7-0

[Block 707]
ངོ་བོ་ཉིད་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོའི་གཞུང་ནི་རབ་འབྱོར་འདི་ལྟ་སྟེ། གཟུགས་ཞེས་བྱ་བ་འདི་ནི་མིང་ཙམ་མོ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཕྱིར་འདི་ལ་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 708 [HEADING]]
##### ཁྱད་པར་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-8-0

[Block 709]
ཁྱད་པར་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོ་ནི་ངོ་བོ་ཉིད་ནི་མི་སྐྱེ་མི་འགག་ཀུན་ནས་ཉོན་མོངས་པ་མ་ཡིན། རྣམ་པར་བྱང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་སྐྱེ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 710]
འགག་པ་ནི་རྣམ་པར་བྱང་བ་སྟེ། དེ་ལྟར་མི་སྐྱེ་མི་འགག །ཀུན་ནས་ཉོན་མོངས་པ་མ་ཡིན། རྣམ་པར་བྱང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། རྐང་པ་འདི་རྣམས་ཀྱི་དོན་ནི་དེ་ཡིན་ནོ། །

[Block 711 [HEADING]]
##### མིང་ཇི་ལྟ་བ་བཞིན་དུ་དོན་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-9-0

[Block 712]
མིང་ཇི་ལྟ་བ་བཞིན་དུ་དོན་དུ༌[^490]རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ནི་མིང་ཇི་ལྟ་བ་བཞིན་དུ་དོན་དུ་རྣམ་པར་གཡེང་བར་འགྱུར་བའོ། །

[Block 713]
དེའི་གཉེན་པོ་ནི་མིང་བཅོས་མ་ལ་ཆོས་དེ་དག་སོ་སོར་བརྟགས་ནས་ཞེས་བྱ་བ་སྟེ། སོ་སོར་ཞེས་བྱ་བ་ནི་མིང་དང་མིང་གིས༌[^491]སོ་སོར་རོ། །

[Block 714 [HEADING]]
##### དོན་ཇི་ལྟ་བ་བཞིན་དུ་མིང་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-10-0

[Block 715]
དོན་ཇི་ལྟ་བ་བཞིན་དུ་མིང་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དོན་ཇི་ལྟ་བ་བཞིན་དུ་མིང་དུ་རྣམ་པར་གཡེང་བར༌[^492]འགྱུར་བ་སྟེ། དེའི་གཉེན་པོ་ནི་གློ་བུར་བའི་མིང་གིས་ཐ་སྙད་དུ་བྱེད་དེ་ཞེས་བྱ་བ་སྟེ། དོན་གྱི་ངོ་བོ་ཉིད་ཀྱི་མིང་ནི་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 716]
རྣམ་པར་གཡེང་བ་བཅུ་པོ་འདི་དག་གི་གཉེན་པོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏེ། ཡང༌[^493]བསྟན་པའི་རྒྱུ་ལས་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་འབྱུང་བར་འགྱུར་རོ། །

[Block 717 [HEADING]]
### ཇི་ལྟར་སྣང་བ་དེའི་བདག་ཉིད་མ་ཡིན་པ། ^2-12-0

[Block 718]
གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་དུ་ཇི་ལྟར་སྣང་བ་དེའི་བདག་ཉིད་མ་ཡིན་པར་ཅི་མངོན་ཞེ་ན། དེ་བསྟན་པ་ནི་མིང་གི་སྔ་རོལ་ན་བློ་མེད་པས་དེའི་བདག་ཉིད་དུ་འགལ་བའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། གལ་ཏེ་གཞན་གྱི་དབང་དང་ཀུན་ཏུ་བརྟགས་པ་དག་གཅིག་པ་ཉིད་དུ་གྱུར་ན་མིང་ལ་མ་ལྟོས་པར༌[^494]བློ་དོན་ལ་འཇུག་པར་འགྱུར་ཏེ། ཇི་ལྟར་བུམ་པ་ཞེས་བྱ་བའི་མིང་མེད་པར་ནི་བུམ་པའི་དོན་ལ་བུམ་པའི་བློ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 719]
གལ་ཏེ་ཡང་བུམ་པ་ཞེས་བྱ་བའི་མིང་དང་བུམ་པ་མཚན་ཉིད་གཅིག་པ༌[^495]ཡིན་ན་ནི་དེ་ལ་འཇུག་པར་འགྱུར་ན་ཡང་གང་གི་ཕྱིར་མཚན་ཉིད་གཅིག་པ་ནི་མ་ཡིན་པ་ཉིད་དེ། དེས་ན་མིང་དང་དོན་དེའི་བདག་ཉིད་ཡིན་པར་འགལ་བར་འགྱུར་རོ། །

[Block 720]
ཡང་འདིར་ནི་མིང་ནི་གཞན་གྱི་དབང་ཡིན་ལ། དོན་ནི་ཀུན་བརྟགས་པ་ཉིད་དུ་རྣམ་པར་གཞག་སྟེ། གང་གི་ཕྱིར་མིང་གཞན་གྱི་དབང་གི་སྟོབས་ཀྱིས་དོན་གཅིག་ལ་ཡང་མིང་མང་པོ་ཀུན་ཏུ་རྟོག་སྟེ། གལ་ཏེ་མིང་དང་དོན་དག་མཚན་ཉིད་གཅིག་པ་ཉིད་ཡིན་ན་དེས་ན་མིང་བཞིན་དུ་དོན་ཡང་མང་པོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 721]
དེ་ལྟར་གྱུར་ན་དོན་ཡང་མང་པོའི་བདག་ཉིད་དུ་འགྱུར་བས་དོན་གཅིག་མང་པོ་ཉིད་ཀྱང་ཡིན་ཞེས་བྱ་བ་ནི་འདི་ལྟར་འགལ་བ༌[^496]ཉིད་ཡིན་ནོ། །

[Block 722]
གཞན་ཡང་དེ་དག་ངོ་བོ་ཉིད་གཅིག་པ་ཡིན་ན་འགལ་བ་གཉིས་པ་འདིར་ཡང་ཐལ་བར་འགྱུར་ཏེ། གང་གི་ཕྱིར་གོའི་སྒྲ་དོན་རྣམ་པ་བཅུ་ལ་འཇུག་པར་འགྱུར་བ་ལྟ་བུས་མིང་ལ་ནི་ངེས་པར་མེད་པ་མ༌[^497]ཡིན་ཏེ། དེས་ན་གལ་ཏེ་མིང་དང་དོན་དག་གཅིག་པ་ཉིད༌[^498]འདོད་ན་ནི་དོན་དེ་གཉིས་ཀྱི་བདག་ཉིད་ཅན་ཡིན་པས་འགལ་བར་འགྱུར་རོ། །

[Block 723]
དེ་ལྟར་འདོད་ན་སྐྱོན་གསུམ་ལ༌[^499]ཡང་འབྱུང་བར་འགྱུར་ཏེ། གང་གི་ཕྱིར་བག་ཆགས་ལ་སོགས་པ་མཚན་ཉིད་ཅན་གྱི་མིང་གི་དོན་རྣམས་གཅིག་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 724]
དོན་འདི་ཉིད་ཚིགས་སུ་བཅད་པས༌[^500]བསྟན་པ་ལ། གྲུབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་དང་ཀུན་ཏུ་བརྟགས་པ་དག་གཅིག་པ་ཉིད་དུ་འགྲུབ༌[^501]པའོ། །

[Block 725]
ཆོས་རྣམས་མེད་ལ་དམིགས་པ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་འདི་ནི་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་དག་གིས༌[^502]སློབ་མ་ཡིད་ཆེས་པར་བྱེད་པ་ཡིན་ཏེ། སློབ་མས་འགལ་བ་གཉིས་དྲིས་པ་ནི་ཆོས་རྣམས་མེད་ལ་དམིགས་པ་དང་། ཉོན་མོངས་མེད་ལ་རྣམ་པར་དག་པ་འགལ་ལོ་ཞེས་ཐེ་ཚོམ་ཟ་བས་དེ་ལ་སྒྱུ་མའི་དཔེས་བསྟན་ཏེ། ཇི་ལྟར་སྒྱུ་མའི་གླང་པོ་མེད་བཞིན་དུ་ཡང་དམིགས་པར་འགྱུར་བ་དེ་བཞིན་དུ་ཡང་ཡོད་པ་མ་ཡིན་ན་ཡང་དམིགས་སུ་རུང་ངོ་ཞེས་བལྟ་བར་བྱ་བ་དང་། ཇི་ལྟར་ནམ་མཁའ་རང་བཞིན་གྱིས་འོད་གསལ་བ་ཡིན་པའི་ཕྱིར་ཁུག་རྣ་ལ་སོགས་པས་བསྒྲིབས་པ་མ་ཡིན་ན་ཡང་དེ་དག་མེད་པ་ཙམ་ལ་དང་བ་ཞེས་བརྗོད་པ་བཞིན་དུ་ཆོས་རྣམས་ཀྱང་རང་བཞིན་གྱིས་འོད་གསལ་བ་ཡིན་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་ཉིད་མེད་པ་ཡིན་ན་ཡང་གློ་བུར་བའི་དྲི་མས༌[^503]སྒྲིབ་གཡོགས་སུ་སྣང་བ་མེད་པར་གྱུར་པ་ནི་ཡང་རྣམ་པར་དག་པར་བལྟ་བར་བྱའོ། །

[Block 726 [HEADING]]
### ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མེད་པར་མི་འགྱུར་བ། ^2-13-0

[Block 727]
གཞན་གྱི་དབང་ཇི་ལྟར་སྣང་བ་བཞིན༌[^504]མེད་དུ་ཟིན་ན་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མེད་པར་ཅིའི་ཕྱིར་མི་འགྱུར། དེ་མེད་ན་ཡང་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཀྱང་མེད་པར་འགྱུར་ཏེ། གང་གི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་ལ་རྣམ་པར་བྱང་བར་འགྱུར་བས་སོ། །

[Block 728]
དེས་ན་དེ་དག་གཉི་ག་མེད་ན་ཡང་ཐམས་ཅད་མེད་པར་ཇི་ལྟར་མི་འགྱུར་བས་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་མེད་པའི་ཉེས་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་པ་སྟེ།[^505] གང་གི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་ནི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 729]
དེས་ན་དེ་དག་གཉི་ག་དམིགས་བཞིན་དུ་ཡང་མེད་དོ་ཞེས་འདོད་པ་དེས་ནི་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དག་ཡོད་བཞིན་དུ་ཡང་མེད་དོ་ཞེས་སྐུར་པ་བཏབ་པར་འགྱུར་རོ།། །།

[Block 730 [HEADING]]
### རྣམ་པར་བྱང་བ་རྣམ་པ་བཞི། ^2-14-0

[Block 731 [HEADING]]
#### རང་བཞིན་གྱིས་རྣམ་པར་བྱང་བ། ^2-14-1-0

[Block 732]
བམ་པོ་བཞི་པ། རང་བཞིན་གྱིས་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་བྱང་བའི་ངོ་བོ་ཉིད་དེ། དེ་ཡང་དེ་བཞིན་ཉིད་དུ་ཡོད་པ་ཡིན་ནོ༌[^506]སེམས་ཅན་ཐམས་ཅད་ལ་སྤྱིའི་མཚན་ཉིད་ཀྱིས་དེ་ནི་ཡོད་པ་ཉིད་ཀྱི་ཕྱིར་ཆོས་ཐམས་ཅད་ནི་དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་ཅན་ཞེས་གསུངས་སོ། །

[Block 733 [HEADING]]
#### དྲི་མ་མེད་པས་རྣམ་པར་བྱང་བ། ^2-14-2-0

[Block 734]
དྲི་མ་མེད་པས་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དེ་ཉིད་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ཞེས་བྱ་བའི༌[^507]དྲི་མ་དང་བྲལ་བར་གྱུར་པའི་ཕྱིར་གང་རྣམ་པར་དག་པའི་དེ་བཞིན་ཉིད་ཀྱིས་རབ་ཏུ་ཕྱེ་བའི་སངས་རྒྱས་ཉིད་དོ། །

[Block 735 [HEADING]]
#### དེ་འཐོབ་པའི་ལམ་རྣམ་པར་བྱང་བ། ^2-14-3-0

[Block 736]
དེ་འཐོབ་པའི་ལམ་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་དེ་འཐོབ་པའི་ལམ་གང་ཡིན་པ་དེ་ཡང་རྣམ་པར་བྱང་བ་སྟེ། དེ་ཡང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པའོ། །

[Block 737 [HEADING]]
#### དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ། ^2-14-4-0

[Block 738]
དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་དེ་རྣམས་མངོན་པར་རྟོགས་པ་སྐྱེད་པ་ཡང་ཡིན་ལ་དམིགས་པ་ཡང་ཡིན་པས་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པའོ། །

[Block 739]
དེ་རྣམ་པར་བྱང་བ་ཡང་ཡིན་པས་དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ་ཞེས་བྱའོ། །

[Block 740]
དེ་ཡང་མདོའི་སྡེ་ལ་སོགས་པ་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་སུ་གཏོགས་པའི་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་བསྟན་པ་གང་ཡིན་པ་དེ་ཀུན་ཏུ་བརྟགས་པ་ཡིན་ན་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་རྒྱུ་ལས་བྱུང་བར་འགྱུར་རོ། །
--- END BLOCKS ---
