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
མ་འོངས་པའི་དུས་སུ་ཡང་གསུང་བར་མི་འགྱུར་རོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་གསང་བ་ཆེན་པོ༌[^312]དེའི་སྣོད་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 632]
དེ་བས་ན་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ།། །།

[Block 633 [HEADING]]
### ལེའུ་གསུམ་པ། ^2-3-0

[Block 634]
ལེའུ་གཉིས་པ་བརྗོད་ཟིན་ནས་གསུམ་པ་བརྗོད་པར་རིགས་པས་དེའི་ཕྱིར་ལེའུ་གསུམ་པ་ལས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ལེའུ་གསུམ་པ་ནི་འདིར་གྲངས་ཀྱིས༌[^313]

[Block 635]
གསུམ་པ་ཉིད་དོ། །

[Block 636]
ལས་ཞེས་པ་འདིར་འབྱུང་ཁུངས་ཀྱི་དོན་ཏེ༌[^314]ལེའུ་གསུམ་པ་ལས་ཡོངས་སུ་གྱུར་པ་དག་པའི་ལྷའི་རྣལ་འབྱོར་གསལ་བར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་དག་པའི་ལྷའི་རྣལ་འབྱོར་གྱི་རྟོག་པ་རྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 637]
ལེའུ་གསུམ་པ་ལས་ལྷའི་རྣལ་འབྱོར་དེ་ཉིད་ཀྱང་རྙེད་པ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་ནི་འདི༌[^315]ལ་བསམས་ནས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 638]
ཡོངས་སུ་དག་པའི་ལྷའི་རྣལ་འབྱོར་ཡང་གང་ཞིག་ཡིན། དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན་གང་གིས་མ་དག་པ༌[^316]རྣམ་པར་བཅད་ནས་གང་ཞིག་དག་པར་གྱུར་པ་ཡོངས་སུ་གཅོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 639]
ཡོངས་སུ་དག་པ་ཡང་ཡིན་ལ་ལྷའི་རྣལ་འབྱོར་ཡང་ཡིན་པའི་ཕྱིར་ཡོངས་སུ་དག་པ་ལྷའི་རྣལ་འབྱོར་ཏེ་རྣམ་པར་རྟོག་པ་དང་བྲལ་བའི་ལྷ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱའོ། །

[Block 640]
ཡོངས་སུ་དག་པ་ལ་སོགས་པ་འདི་ཡང་གང་ཞིག་ཡིན་ཏེ། དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན་སྤང་བྱས་ཡོངས་སུ་དག་པ་སྟེ། བསྐྱེད་པའི་རིམ་པའི་ལྷའི་རྣལ་འབྱོར་གྱི༌[^317]ཏིང་ངེ་འཛིན་དང་ལྡན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 641]
ཡང་ན་བྲལ་བའི་དོན་གྱིས༌[^318]ཡོངས་སུ་དག་པའི་ལྷའི་རྣལ་འབྱོར་ཏེ་ཞེས་བྱ་བ༌[^319]སྟེ། རྣམ་པར་རྟོག་པ་རགས་པ་དང་བྲལ་བ་སྒྱུ་མ་ལྟ་བུའི་སྐུ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 642]
ཡང་ན་ཉེ་བར་ལོངས་སྤྱོད་པའི་དོན་གྱིས་ཡོངས་སུ་དག་པ་ལྷའི་རྣལ་འབྱོར་ཞེས་བྱ་སྟེ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 643]
ཡང་ན་སྣ་ཚོགས་པ་དང་། ཐོགས་པ་མེད་པའི་ཕྱིར་ཡོངས་སུ་དག་པ་ལྷའི་རྣལ་འབྱོར་ཏེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྤྲུལ་པའི་སྐུ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 644 [HEADING]]
### ལེའུ་བཞི་པ། ^2-4-0

[Block 645]
ལེའུ་བཞི་པ་ལས་ནི་དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་སྟོན་ཏོ་ཞེས་བྱ་བ་ནི་སློབ་མ་དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་ཆེན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 646]
འདིར་ཡང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དཀྱིལ་འཁོར་ཆེན་པོ་ནི་རྣམ་པ་གཉིས་སུ་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དངོས་གྲུབ་ཀྱི་དཀྱིལ་འཁོར་དང་། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་རོ། །

[Block 647]
འདིར་ཡང་དབང་བསྐུར་བ་ཁོ་ནའི་དཀྱིལ་འཁོར་མ་ཡིན་གྱི། དབང་བསྐུར་བ་ཁོ་ན༌[^320]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 648 [HEADING]]
### ལེའུ་ལྔ་པ། ^2-5-0

[Block 649]
ལེའུ་ལྔ་པ་ལས་ནི་རྣལ་འབྱོར་གྱི་སྤྱོད་པ་གསུངས་སོ་ཞེས་བྱ་བ་ནི་རྣལ་འབྱོར་གྱི་སྤྱོད་པ་ནི། རྣལ་འབྱོར་གྱི་སྤྱོད་པ་སྟེ། ཏིང་ངེ་འཛིན་གྱི་སྤྱོད་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 650]
རྣལ་འབྱོར་གྱི་སྤྱོད་པ་ཡང་བསྡུས་པ་དང་རྒྱས་པ་ཞེས་རྟོག་གྲང་ན། རྒྱས་པ་འོག་ནས་སྟོན་པའི་ཕྱིར་འདི་ནི་བསྡུས་པ་ཞེས་བྱའོ། །

[Block 651]
དེ་གང་ལ་སྟོན་པའི་ལེའུ་ནི་རྣལ་འབྱོར་གྱི་སྤྱོད་པའོ། །

[Block 652 [HEADING]]
### ལེའུ་དྲུག་པ། ^2-6-0

[Block 653]
ལེའུ་དྲུག་པ་ལས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྐུ་དང་གསུང་དང་ཐུགས་བྱིན་གྱིས་རློབ་པའི་ལེའུ་ནི་སྐུ་དང་གསུང་དང་ཐུགས་བྱིན་གྱིས་རློབ་པའི་ལེའུའོ། །

[Block 654]
དེ་གང་གིས་གསུངས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 655]
སྐུ་བྱིན་གྱིས་རློབ་པ་ནི་རྣམ་པ་གཉིས་ཏེ་བླངས་པས༌[^321]བྱིན་གྱིས་རློབ་པ་དང་ཐོབ་པས་བྱིན་གྱིས་རློབ་པའོ། །

[Block 656]
གསུང་དང་ཐུགས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 657 [HEADING]]
### ལེའུ་བདུན་པ། ^2-7-0

[Block 658]
ལེའུ་བདུན་པ་ལས་ནི་ལེའུ་ལྔ་པའི༌[^322]བཤད་པ༌[^323]སྤྱོད་པ་སྤྲོས་ནས་སྟོན་ཏོ་ཞེས་བྱ་བ༌[^324]ནི་ལེའུ་ལྔ་པ་ལས་བཤད་པའི་སྤྱོད་པ་ཉིད་སྤྲོས་ནས་སྟོན་གྱི་དེ་ལས་གཞན་དུ་བཤད་པའི་སྤྱོད་པ་ནི་མ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་མཆོག་གི་སྤྱོད་པ་ནི་ལེའུ་ལྔ་པ་ལས་བཤད་པ་ལས་ནམ་ཡང་གཞན་ནས༌[^325]འབྱུང་བར་མི༌[^326]འགྱུར་བའི་ཕྱིར་རོ། །

[Block 659 [HEADING]]
### ལེའུ་བརྒྱད་པ། ^2-8-0

[Block 660]
ལེའུ་བརྒྱད་པ་ལས་ནི་གསང་བའི་དབང་བསྐུར་བ་གསུངས་སོ་ཞེས་པ་ནི། གང་ལ་བྱང་ཆུབ་སེམས་ཀྱི་དབང་བསྐུར་བར་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 661 [HEADING]]
### ལེའུ་དགུ་པ། ^2-9-0

[Block 662]
ལེའུ་དགུ་པ་ལས་ནི་རྨད་དུ་བྱུང་བའི་ལུང་བསྟན་པ་གསུངས་སོ་ཞེས་པ་ནི་མཆོག་ཏུ་གྱུར་པའི་ལུང་སྟོན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 663 [HEADING]]
### ལེའུ་བཅུ་པ། ^2-10-0

[Block 664]
ལེའུ་བཅུ་པ་ལས་ནི་མངོན་པར་འདོད་པའི་དངོས་གྲུབ་མངོན་དུ་བྱ་བའི་ཕྱིར་ཕྱི་དང་ནང་གི་བདག་ཉིད་ཅན་གྱི་ལྷའི་སྙིང་པོ་བསྐུལ་བ་གསུངས་སོ་ཞེས་པ་ནི་མངོན་པར་འདོད་པའི་དངོས་གྲུབ་ནི་བླང་བར་བྱ་བའི་དངོས་གྲུབ་སྟེ་ཐུན་མོང་དང་མཆོག་གི་དངོས་གྲུབ་རྣམ་པ་གཉིས་སོ། །

[Block 665]
དེ་ཐོབ་པར་བྱེད་པའི་ཐབས་ནི་ལྷའི་སྙིང་པོ་ཡིན་པས་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 666 [HEADING]]
### ལེའུ་བཅུ་གཅིག་པ། ^2-11-0

[Block 667]
ལེའུ་བཅུ་གཅིག་པ་ལས་ནི་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་དང་ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་སྟོན་ཏོ་ཞེས་པ་ནི་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་འདིས་བསྐྱེད་པའི་དབང་དུ་གསུངས་སོ། །

[Block 668]
ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་དབང་དུ་བྱས་པའོ། །

[Block 669]
ཡང་ན་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 670]
ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །
--- END BLOCKS ---
