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
ཞེས་བྱ་བ་ནི། དགེ་འདུན་སྤྱིའི་མལ་ཆ་དང་སྟན་ཁྲི་དང་ཁྲིའུ་ལ་སོགས་པ་ནི་ཤིན་ཏུ་སྤྱད་པར་བྱ་བ་མ་ཡིན་པས་མི་རྟག་པ་ལ་སོགས་པའི་ཆོས་དྲན་པར་བྱས་ཏེ་འདུག་པར་མི་བྱའོ། །

[Block 632]
དེ་ལྟ་བུའི་དྲན་པ་མེད་པར་ནི་འདུག་པར་མི་བྱའོ། །

[Block 633]
དེ་ལྟ་བུའི་ཆོས་ཡིད་ལ་བྱེད་པ་དང་ལྡན་པས་འདུག་ཏུ་གནང་སྟེ། དེ་བས་ན་དྲན༌[^488]དང་ལྡན་ན་ཉེས༌[^489]མེད་དོ། །

[Block 634 [VERSE]]
སོ་བཀྲུ་བ་དང་ཆུ་བཏུང༌[^490]དང་། །
བཤང་གཅི་བྱེད་དུ་འགྲོ་བ་དང་། །
མཚམས་ནང་སྟོན་ལ་ཕྱག་བྱ་བ། །
དེ་དག་མ་ཞུས་ཉེས་མེད་དོ། །

[Block 635]
ཞེས་བྱ་བའི་མིང་གིས་འབྱུང་བ་འདི་དག་ནི་མཁན་པོ་དང་སློབ་དཔོན་ལ་མ་ཞུས་ཀྱང་ཉེས་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 636 [VERSE]]
བརྟུལ་ཞུགས་ཅན་གྱིས་བྱ་བ་གཞན། །
དེ་དག་ཐམས་ཅད་མ་ལུས་པར། །
གལ་ཏེ་བླ་མ་མ་ཞུས་པར། །
བྱས་ན་དེ་ནི་ཉེས་བྱས་འགྱུར། །

[Block 637]
ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་གིས་བསྒོམ་ཞིང་བཀླག༌[^491]པར་བྱ་བ་དང་། གོས་དྲ་བ་དང་འདྲུབ་པ་ལ་སོགས་པ་ལས་སུ་ཅི་བྱ་བ་ཀུན་ཀྱང༌[^492]མཁན་པོ་ལ་ཞུ་བར་བྱ་སྟེ། གལ་ཏེ་མ་ཞུས་པར་སྣ་འགའ་བྱས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 638 [VERSE]]
མཆོད་རྟེན་ལ་སོགས་ཕྱག་བྱས་ཏེ། །
མི་ཉལ་བྱས་ནས་དེ་འོག་ཏུ། །

[Block 639]
བླ་མའི་རྐང་བཀྲུ། །ཞེས་བྱ་བ་ལ། ནུབ་མོ་དགེ་སྦྱོང་གིས་མཆོད་རྟེན་དང་སྐུ་གཟུགས་ལ་སོགས་པ་ལ་ཕྱག་བྱས་ཏེ། ཞུ་བའི་གནས་གང་ཡིན་པའི་གང་ཟག་ལ་སང་ནང་པར་གྱི་བར་དུ་མི་ཉལ་བར་དགེ་བ་རྔོ་ཐོགས༌[^493]ཚད་དུ་བགྱི་ཞེས་ཞུ་ཞིང་དེ་ལྟར་བྱས་པའི་འོག་ཏུ་མཁན་པོ་དང་སློབ་དཔོན་གཉིས་ཀ༌[^494]དང་བླ་མ་རྣམས་ཀྱི་རྐང་པ་ཆུ་གཙང་མས༌[^495]བཀྲུ་བར་བྱའོ། །

[Block 640]
བླ་མ་ལ། །བརྟུལ་ཞུགས་ཅན་གྱིས་ཀུན་ཞུས་ཏེ། །ཞེས་བྱ་བ་ནི་དེ་ལྟར་བླ་མའི་རྐང་ལག་བཀྲུ་བར་བྱས་ནས་དགེ་བ་ལ་སོགས་པ་ཅི་བྱ་བརྟུལ་ཞུགས་ཅན་དགེ་སྦྱོང་བདག་གིས་ཞུས་ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཅི་བྱ་ཞེ་ན།

[Block 641 [VERSE]]
རྐང་པ་གཉིས་ཀ་བཀྲུས་ནས་ནི། །
ནམ་གྱི་ཆ་སྟོད་ཆ་སྨད་ལ། །
བསྒྲིམས་ཏེ་མི་ཉལ་བྱ་བ་སྟེ། །

[Block 642]
ཞེས་བྱ་བ་སྟེ། སླར་བདག་གི་གནས་ཁང་དུ༌[^496]ཕྱིན་ནས། རྐང་པ་གཉིས་དག་ཏུ་བཀྲུས་ཏེ་ཞུས་པ་བཞིན་ནམ་གྱི་ཆ་སྟོད་སྲོད་དང་ནམ་གྱི་ཆ་སྨད་ཐོ༌[^497]རངས་ལ་བསྒྲིམས་པ་བརྩོན་འགྲུས་ཆེན་པོས་མི་ཉལ་བར་དགེ་སྦྱོར་བྱའོ། །

[Block 643]
དེ་ལྟར་བྱས་ན་ཞུས་པ་བཞིན་དགེ་སྦྱོང་དེས་ནི་བདེན་པར་སྨྲ་བར་འགྱུར་ཏེ།

[Block 644 [VERSE]]
ཞུས་པ་བཞིན་དུ་བྱས་པ་ཡིན་ནོ། །
ལྡང་དང་སྣང་བའི་འདུ་ཤེས་ཀྱིས། །
སེང་གེའི་ཉལ་ཐབས་བཞིན་དུ་བྱ། །

[Block 645]
ཞེས་བྱ་བ་ལ། གཉིད་འོང་སྟེ་མལ་དུ་ལུས་ཕབ་པའི་ཚེ་ན་ཡང་བསམ་པ་མེད་པར་ཉལ་བར་མི་བྱའི། མྱུར་དུ་ལྡང་བའི་བསམ་པ་དང་མྱུར་དུ་སད་ཅིང་སྣང༌[^498]བའི་འདུ་ཤེས་ཡིད་ལ་བྱས་ནས་སེང་གེ་བཞིན་དུ་གློ་གཡས་པ་ཕབ་སྟེ་ཉལ་བར་བྱའོ། །

[Block 646 [VERSE]]
དྲན་དང་བསམ་པའི་རྒྱུད་དག་དང་། །
དེ་བཞིན་མྱུར་དུ་སད་ནས་ནི། །
ཇི་སྐད་བསྟན་པ་བཞིན་དུ་བྱ། །

[Block 647]
ཞེས་བྱ་བ་ལ། དེ་ལྟར་སྣང་བ་དང་ལྡང་བའི་འདུ་ཤེས་ཀྱིས་ཉལ་བ་ནི་དྲན་པའི་བསམ་པ་དང་ལྡན་པ་ཞེས་བྱ་བ་སྟེ། དེས་ནི་མྱུར་དུ་སད་ཅིང་ལྡང་བར་འགྱུར་རོ། །

[Block 648]
དེ་ལྟར་སད་ནས།

[Block 649 [VERSE]]
ནམ་གྱི་ཆ་སྨད་མལ་ནས་ལངས། །
ནམ་ལངས་བར་དུ་ཁ་ཏོན༌[^499]བྱ། །

[Block 650]
ཞེས་ཇི་སྐད་བསྟན་པ་བཞིན་དུ་བསྒྲུབ་ཅིང་བསྒོམ་པར་བྱའོ་ཞེས་བྱ༌[^500]བའི་དོན་ཏོ། །

[Block 651]
ཕྱི་དྲོ་ཕན་ཆད་ཀྱི་བྱ་བ་བསྟན་ཟིན་ཏེ།[^501] །

[Block 652 [HEADING]]
## འབྲས་བུ། ^8-0

[Block 653]
ད་ནི་ཚིག་རྐང་གསུམ་གྱིས༌[^502]དགེ་སྦྱོང་གི་བསླབ་ཚིག་བསྲུང་བ་དང་། སྔ་དྲོ་དང་ཕྱི་དྲོའི་དུས་སུ་ཁ་ཟས་བཟའ་ཞིང་ཆུ་གཙང་བ་དང་། མཁན་པོ་དང་སློབ་དཔོན་དང་བླ་མ་རྣམས་ལ་ལུས་ངག་གི་སྒོ་ནས་བཀུར་སྟི་ལ་སོགས་པའི་ལས་སུ་བྱ་བ་ཇི་ལྟར་བསྟན་པ་བཞིན་དུ་ཉམས་སུ་བླངས་ཏེ་བསྒྲུབས་ན་ཡོན་ཏན་དང་འབྲས་བུ་གསུམ་འཐོབ་བོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 654 [VERSE]]
ཇི་ལྟར་ཉོན་མོངས་མྱུར་ཟད་ནས། །
བྱང་ཆུབ་དམ་པ་འཐོབ་འགྱུར་བ། །
དེ་ལྟར་བསྒྲིམས་དང་ལྡན་པར་བྱ། །

[Block 655]
ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་བསྒྲིམས་དང་ལྡན་པར་བྱ། །ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་པ་བཞིན་ནན་ཏན་བྱས་ན༌[^503]ཚེ་འདིར་ཡང་ཉོན་མོངས་པ་མྱུར་དུ་ཟད་པར་འགྱུར་ལ། མ་འོངས་པ་ན་ཡང་བྱང་ཆུབ་རྣམ་པ་གསུམ་ལས་དམ་པ་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 656 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 657 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 658]
དགེ་སྦྱོང་གི་ཀཱ་རི་ཀཱ་ལྔ་བཅུ་པ་མདོ་ཙམ་དུ་བཤད་པ། སློབ་དཔོན་ཀ་མ་ལ་ཤཱི་ལས་མཛད་པ་རྫོགས་སོ།། །།
--- END BLOCKS ---
