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
[Block 631 [VERSE]]
དབང་པོ་དང་ནི་ཡུལ་དག་ལ། །
བརྟེན་ཏེ་ཡིད་ནི་གང་སྐྱེས་པ། །
དེ་ནི་མན་ཞེས་བརྗོད་པ་སྟེ། །
སྐྱོབ་པའི་དོན་གྱིས་ཏྲ་ཞེས་བྱ། །

[Block 632]
ཞེས་སོ། །

[Block 633]
ལུང་བསྟན་པ་ལས་ཀྱང་། །མན་ཏྲ་གསང་བར་བརྗོད་པའི་དོན་ཏོ། །

[Block 634]
དེ་བས་ན་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་མི་ཤེས་ན་གང་ལས་བྱེད་པ་དེའི་ལས་དེ་རྣམས་འགྲུབ་པར་མི་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་བྱེ་མ་ལ་མར་བཞིན་ནོ། །

[Block 635]
སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཤེས་པའི་རྣལ་འབྱོར་པས་ཞི་བ་ལ་སོགས་པ་འབད་པ་མེད་པར་འགྲུབ་པར་འགྱུར་ཏེ། དེ་རྣམས་ཞར་ལ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 636]
དེ་བས་ན་རྣམ་པ་ཐམས་ཅད་དུ་བླ་མའི་དྲིན་ལ་བརྟེན་ཏེ་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་བཙལ་བར་བྱའོ། །

[Block 637]
དེ་ལྟར་རྣམ་པ་བཞིས་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་ཏོ། །

[Block 638 [HEADING]]
##### རྡོ་རྗེ་བཟླས་པ། ^1-2-1-3-0

[Block 639 [HEADING]]
###### རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས་པ། ^1-2-1-3-1-0

[Block 640]
རླུང་གི་དེ་ཁོ་ན་ཉིད་དང་། སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་ནས། རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་བརྗོད་པར་བྱ་སྟེ། དེ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས་པ་ཞེས་བྱ་བ་ནི་དང་པོ་རྣལ་འབྱོར་པས་མྱུར་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་རེག་བྱ་རྡོ་རྗེ་མ་དང་སྙོམས་པར་ཞུགས་པར་བསམས་ཏེ། ལྟེ་བར་རྩིབས་བརྒྱད་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོའི་དཀྱིལ་འཁོར་དུ་མར་མེ་འབར་བའི་འོད་དང་མཚུངས་པའི་ཡི་གེ་ཨ་ལ་དམིགས་ཏེ། དེའི་འོད་ཟེར་གྱིས་མེ་སྟག་དང་འདྲ་བའི་ཡི་གེ་གསུམ་མདོག་ཇི་ལྟ་བ་བཞིན་དུ་སྤྲོས་ཏེ། སྙིང་ལ་སོགས་པའི་གནས་གསུམ་དུ་དགོད་དེ། འཇུག་པ་ལ་སོགས་པའི༌[^412]རིམ་པས་ཡན་ལག་མ་ཉམས་པར་བཟླས་ཏེ། ཇི་སྲིད་སེམས་རྩེ་གཅིག་པར་གྱུར་གྱི་བར་དུ་ཐ་མར་མར༌[^413]མེ་དང་འདྲ་བའི་འོད་གསལ་བའི་ཡི་གེ་ལ་གནས་པར་བྱའོ། །

[Block 641]
གདོད་མ་ནས་མ་སྐྱེས་པའི་ཡི་གེ་ཙམ༌[^414]ལ་དམིགས་ཏེ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཏིང་ངེ་འཛིན་མངོན་དུ་བྱས་ཏེ། སྲོག་ལ་སོགས་པའི་འཁོར་ལོ་དང་། ཡིད་དང་དེ་ཉིད་དུ་ཞུགས་པས་བརྟན་པ་དང་གཡོ་བའི་དངོས་པོ་ཐམས་ཅད་ཀྱི་རྣམ་པར་རྟོག་པ་ཞི་བས། ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དཔལ་རྡོ་རྗེ་སེམས་དཔའི་རང་བཞིན་འོད་གསལ་བ་ལ་རྣལ་འབྱོར་པས་གནས་པར༌[^415]བྱའོ་ཞེས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས༌[^416]པའོ། །

[Block 642]
[^417]

[Block 643 [HEADING]]
###### སྐུའི་བཟླས་པ། ^1-2-1-3-2-0

[Block 644]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་སངས་རྒྱས་སྤྱན་དང་སྙོམས་པར་ཞུགས་པའི་རྣམ་པར་སྣང་མཛད་དུ་བདག་ཉིད་བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་རྣམ་པར་དགོད་དེ། དེའི་འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་སེམས་ཅན་གྱི་དོན་བྱས་ལ། ཐུགས་དང་གསུང་གི་ས་བོན་སྐུའི་ས་བོན་ལ་འཇུག་པར་བྱ་སྟེ། ཡི་གེ་ཨོཾ་གཅིག་པུ་ལ་དམིགས་ཤིང་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་རབ་ཏུ་ཞི་བར་གྱུར་པར་གནས་པར་བྱའོ་ཞེས་སྐུའི་བཟླས་པའོ། །

[Block 645 [HEADING]]
###### གསུང་གི་བཟླས་པ། ^1-2-1-3-3-0

[Block 646]
[^418]དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱི་གོས་དཀར་མོ་དང་སྙོམས་པར་ཞུགས་པ་འོད་དཔག་ཏུ་མེད་པར་བདག་ཉིད་བསྒོམས་ཏེ།[^419] ཡི་གེ་གསུམ་ལྐོག་མ་ལ་སོགས་པར་དགོད་དེ། དེའི་འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བས་སེམས་ཅན་གྱི་དོན་བྱས་པས། ཐུགས་དང་སྐུའི་ས་བོན་གསུང་གི་ས་བོན་ལ་འཇུག་པར་བྱས་ཏེ། ཡི་གེ་ཨཱཿགཅིག་པུ་ལ་དམིགས་ཤིང་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་དུ་རྟོག་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་གནས་པར་བྱའོ་ཞེས་གསུང་གི༌[^420]བཟླས་པའོ། །

[Block 647 [HEADING]]
###### ཐུགས་ཀྱི་བཟླས་པ། ^1-2-1-3-4-0

[Block 648 [HEADING]]
###### རིན་པོ་ཆེའི་བཟླས་པ། ^1-2-1-3-5-0

[Block 649]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་མཱ་མ་ཀཱི་དང་སྙོམས་པར་ཞུགས་པའི་ཐུགས་ཀྱི་རྡོ་རྗེར་བདག་ཉིད་རྣམ་པར་བསྒོམས་ཏེ། ཐུགས་ལ་སོགས་པའི་ཡི་གེ་གསུམ་དགོད་དེའི༌[^421]འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བས་སེམས་ཅན་གྱི༌[^422]དོན་བྱས་ལ་ལུས་དང་ངག་གི་ས་བོན་ཐུགས་ཀྱི་ས་བོན་ལ་འཇུག་པར་བྱ་སྟེ། ཡི་གེ་ཧཱུཾ་གཅིག་པུ་ལ་དམིགས་ཤིང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས༌[^423]ཀྱི་ངོ་བོ་ཉིད་དུ་རྟོག་པ་མ་ལུས་པར་རབ་ཏུ་ཞི་བར་གནས་པར་བྱའོ་ཞེས་ཐུགས་ཀྱི་བཟླས་པའོ། །

[Block 650]
[^424]

[Block 651]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་མཱ་མ་ཀཱི་དང་སྙོམས་པར་ཞུགས་པ༌[^425]རིན་ཆེན་འབྱུང་ལྡན་དུ་བདག་ཉིད་རྣམ་པར་བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་དགོད་དེ། འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་སེམས་ཅན་ཐམས་ཅད་ལ་དབུལ་བའི་སྡུག་བསྔལ་ཕྲོགས་ཏེ། ཡི་གེ་གསུམ་པོ་ཐིག་ལེ་ལ་འཇུག་པར་བྱ་སྟེ། ནམ་མཁའ་དང་མཚུངས་པའི་ཐིག་ལེ་ལ་སེམས་གཏད་དེ། མཉམ་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་དུ་དམིགས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་བྱའོ་ཞེས་རིན་པོ་ཆེའི་བཟླས་པའོ། །

[Block 652 [HEADING]]
###### དོན་ཡོད་བཟླས་པ། ^1-2-1-3-6-0

[Block 653]
[^426]དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་དམ་ཚིག་སྒྲོལ་མ་དང་སྙོམས་པར་ཞུགས་པ་དོན་ཡོད་གྲུབ་པར་བདག་ཉིད་བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་དགོད་དེ། འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་གཞལ་ཡས་ཁང་པ་དང་བཅས་པའི་དེ་བཞིན་གཤེགས་པ་སྤྲོས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱས་ལ་ཐོ་རངས་ཀྱི་སྐར་མ་ལྟ་བུའི་ཐིག་ལེ་ལ་ཡི་གེ་གསུམ་བསྡུས་ཏེ། བྱ་བ་ནན་ཏན་གྱི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་དུ་བྱ་བ་བྱས་པ་ཉིད་ཀྱིས་གནས་པར་བྱའོ་ཞེས་དོན་ཡོད་བཟླས་པའོ། །

[Block 654]
[^427]

[Block 655 [HEADING]]
###### གཏི་མུག་གི་བཟླས་པ། ^1-2-1-3-7-0

[Block 656]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་བདག་ཉིད་གཏི་མུག་རྡོ་རྗེར་སྙོམས་པར་ཞུགས་པར་བསམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་དགོད་དེ། ས་བོན་གཉིས་ཡི་གེ་ཨོཾ་ལ་འཇུག་པར་བྱ་སྟེ། དེའི་འོད་ཟེར་གྱིས༌[^428]གཏི་མུག་གི་རིགས་ཅན་གྱི་སེམས༌[^429]ཅན་ཐམས་ཅད་བཀུག་ལ་དེ་ཉིད་དུ༌[^430]འཇུག་པར་བྱ་སྟེ། གཏི་མུག་རྣམ་པར་དག་པའི་གནས་སུ་སེམས་ཅན་འཇོག་པར་བྱའོ་ཞེས་ལྷག་པར་མོས་པས་གཏི་མུག་ཅེས་བྱ་བ་གཅིག་པ་དང་དུ་མ་མ༌[^431]ཡིན་ཞེས་དཔྱོད་པས་གང་སེམས་རྩེ་གཅིག་པ་ཉིད་དེ་ནི་གཏི་མུག་གི་བཟླས་པའོ། །

[Block 657 [HEADING]]
###### འདོད་ཆགས་ཀྱི་བཟླས་པ། ^1-2-1-3-8-0

[Block 658]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་འདོད་ཆགས་རྡོ་རྗེར་བདག་ཉིད་སྙོམས་པར་ཞུགས་པར་བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་དགོད་ཅིང་ས་བོན་གཉིས་གསུང་གི་ཡི་གེ་ལ་བསྡུས་ཏེ། དེའི་འོད་ཟེར་གྱིས་འདོད་ཆགས་ཀྱི་རིགས་ཅན་གྱི་སེམས་ཅན་བཀུག་ཅིང་དེ་ཉིད་དུ་འཇུག་པར་བྱས་ལ། འདོད་ཆགས་རྣམ་པར་དག་པའི་གནས་སུ་དགོད་པར་བྱའོ་ཞེས་ལྷག་པར་མོས་པས་འདོད་ཆགས་ཞེས་བྱ་བ་གཅིག་པ་དང་དུ་མ་མ་ཡིན་ཞེས་སྤྱོད་པས་གང་སེམས་རྩེ་གཅིག་པ་དེ་ནི་འདོད་ཆགས་ཀྱི་བཟླས་པའོ། །

[Block 659 [HEADING]]
###### ཞེ་སྡང་གི་བཟླས་པ། ^1-2-1-3-9-0

[Block 660]
དེ་བཞིན་དུ་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་བདག་ཉིད་ཞེ་སྡང་རྡོ་རྗེར༌[^432]སྙོམས་པར་ཞུགས་པར་བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་དགོད་དེ་ས་བོན་གཉིས་ཧཱུཾ་ལ་འཇུག་པར་བྱས་ལ། དེའི་འོད་ཟེར་གྱིས་ཞེ་སྡང་གི་རིགས་ཅན་གྱི་སེམས༌[^433]ཅན་བཀུག་ལ་དེ་ཉིད་དུ་འཇུག་པར་བྱ་སྟེ། ཞེ་སྡང་རྣམ་པར་དག་པའི་གནས་སུ་དགོད་པར་བྱ་ཞེས་ལྷག་པར་མོས་པས་ཞེ་སྡང་ཞེས༌[^434]བྱ་བ་ནི་གཅིག་གམ་དུ་མར་མེད་ཅེས་དཔྱོད་པས་གང་སེམས་རྩེ་གཅིག་པ་དེ་ནི་ཞེ་སྡང་གི་བཟླས་པའོ། །

[Block 661]
[^435]

[Block 662 [HEADING]]
###### ཁྲོ་བོའི་བཟླས་པ། ^1-2-1-3-10-0

[Block 663]
དེ་བཞིན་དུ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རང༌[^436]འདོད་པའི་ལྷ་གང་ཡང་རུང་བ་སྙོམས་པར་ཞུགས་པར་བདག་ཉིད་རྣམ་པར༌[^437]བསྒོམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་པོ་བཀོད་པ་དེ་ལ་དམིགས་པས་ཕྱོགས་བཅུ་ན་བཞུགས་པའི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བདག་གིས༌[^438]སྔགས་བརྗོད་པར་གྱུར་པ་འདི་ཉོན་ཅིག་ཅེས༌[^439]ལྷག་པར་མོས་པས་དངོས་གྲུབ་འདོད་པའི་སྒྲུབ་པ་པོས་རང་ངམ་གཞན་གྱིས་ཐོས་པར་གྱུར་པ་ཁྲོ་བར་བརྗོད་པས་ན་ཁྲོ་བོའི་བཟླས་པའོ། །

[Block 664 [HEADING]]
###### མ་ནིང་གི་བཟླས་པ། ^1-2-1-3-11-0

[Block 665]
[^440]དེ་བཞིན་དུ༌[^441]མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པ་གང་ཡང་རུང་བ་རང་གི་ཤེས་རབ་མ་དང་སྙོམས་པར་ཞུགས་པར་བདག་ཉིད་བསམས་ཏེ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་པོ་དགོད་ཅིང་། ལྟེ་བར་རྩིབས་བརྒྱད་པ་ཁ་དོག་དཀར་པོ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོ་དེའི་ལྟེ་བར་དབྱངས་ཡིག་དང་པོ་མར་མེ་དང་འདྲ་བ་ལ་དམིགས་ཏེ། དེའི་འོད་ཟེར་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་སེམས་ཅན་མ་ལུས་པའི་དོན་བྱས་ལ། སེམས་རྩེ་གཅིག་པར་གྱུར་པས་ཆ་དང་ཆའི་དབྱེ་བས་ཡི་གེ་གསུམ་པོ་སྐྱེ་བ་མེད་པའི་ཡི་གེ་ཨ་ལ་འཇུག་པར་བྱ་སྟེ། དེ་ཡང་རྩིབས་བརྒྱད་པའི་འཁོར་ལོ་ལ་ཐིམ་ཞིང་དེ་ཡང་ལྟེ་བའི་ནམ་མཁའ་ལ་དབྱེར་མེད་པར་བསམས་ལ། རྣམ་པར་རྟོག་པའི་བག་ཆགས་རབ་ཏུ་ཞི་བ་སྒོ་ཐམས་ཅད་འགགས་པ་འགྲོ་བ༌[^442]དང་འོང་བ་ལས་ངེས་པར་གྲོལ་བ༌[^443]སྲོག་ལ་སོགས་པའི་རླུང་གི་འཁོར་ལོ་ཐམས་ཅད་རོ་གཅིག་པར་གྱུར་ན། དྲི་མ་མེད་པའི་མཐའ་ཡས་པའི་ནམ་མཁའ་དང་མཚུངས་པ་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་འབའ་ཞིག་ཏུ་རྣལ་འབྱོར་པས༌[^444]གནས་པར་བྱའོ། །

[Block 666]
འདི་ནི་ཐབས་དང་ཤེས་རབ་རོ་གཅིག་པའི་བདག་ཉིད་བུད་མེད་དང་སྐྱེས་པའི་ཐ་སྙད་དང་བྲལ་བའི་མ་ནིང་གི་བཟླས་པར་བཤད་དོ་ཞེས་རྡོ་རྗེ་བཟླས་པ་རྣམ་པ་བཅུ་གཅིག་པའོ། །

[Block 667]
[^445]

[Block 668]
རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས་པ་ལ༌[^446]ཡང་དབྱེ་བ་གཞན་བཤད་པར་བྱ་སྟེ། རེ་ཞིག་དང་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱ་ཆེན་པོའི༌[^447]གཟུགས་སུ་བདག་ཉིད་བསམས་ཏེ། ལྐོག་མ་དང་སྙིང་ག་དང་ལྟེ་བ་དང་གསང་བ་དག་ཏུ་འབྱུང་བ་ཆེན་པོ་བཞིའི་རང་བཞིན་གྱི་དཀྱིལ་འཁོར་མྱུར་དུ་དགོད་དེ། དེ་རྣམས་ཀྱི་སྟེང་དུ་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་གྱི་ཆ༌[^448]རེ་རེ་རྣམ་པར་བཀོད་ལ། འཇུག་པ་ལ་སོགས་པའི་རིམ་པས་ཇི་སྲིད་སེམས་རྩེ་གཅིག་པའི་བར་དུ་བསམ་པར་བྱའོ། །

[Block 669]
དེ་ལ་ཆ་དགོད་པའི་རིམ་པ་འདི་ཡིན་ཏེ། སྙིང་གའི་པདྨར་ཡི་གེ་མགོ་མེད་དེ་དཔེར་ན་ཧའོ། །

[Block 670]
ལྐོག་མའི་པདྨར་མགོ་བོ་སྟེ། དཔེར་ན་ཨའོ། །
--- END BLOCKS ---
