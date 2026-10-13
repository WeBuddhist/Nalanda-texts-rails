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
[Block 281]
མདོ་གཞན་དག་ལས།

[Block 282]
ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་གཞན༌[^113]གང་དག་གསུངས་པ་དེ་དག་ཀྱང་བསྟན་བཅོས་འདི་ལས་ཇི་སྐད་བཤད་པ་བཞིན་དེ་དག་གི་རང་རང་གི་མཚན་ཉིད་ལེགས་པར་དཔྱད་ནས་ཕུང་པོ་ལ་སོགས་པ་འདི་སྐད་བཤད་པ་འདི་དག་ཉིད་དུ་བསྡུ་བར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་ཚུལ་ཁྲིམས་དང་། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་དང་། རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་དག་ལས་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ནི་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 283]
ལྷག་མ་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 284]
ཟད་པར་གྱི་སྐྱེ་མཆེད་བཅུ་པོ་དག་ལས་བརྒྱད་ནི་མ་ཆགས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱིས་བསྡུས་སོ། །

[Block 285]
འཁོར་རྣམས་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་ཏེ། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དག་ཀྱང་དེ་དང་འདྲའོ། །

[Block 286]
ཟད་པར་ནམ་མཁའ་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དག་དང་། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་བཞི་པོ་དག་ནི་ཕུང་པོ་བཞིའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་སོ། །

[Block 287]
རྣམ་པར་གྲོལ་བའི་སྐྱེ་མཆེད་ལྔ་པོ་དག་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱིས་བསྡུས་སོ། །

[Block 288]
འཁོར་རྣམས་དང་བཅས་ན་ནི་སྒྲ་དང་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་རྣམས་ཀྱིས༌[^114]བསྡུས་སོ། །

[Block 289]
སྐྱེ་མཆེད་གཉིས་ལས་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་ནི་དྲི་དང་རོའི་སྐྱེ་མཆེད་མེད་པའི་ཕྱིར་སྐྱེ་མཆེད་བཅུ་པོ་རྣམས་ཀྱིས་བསྡུས་སོ། །

[Block 290]
འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་དུ་ཉེ་བར་འགྲོ་བ་ནི་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་སོ། །

[Block 291]
ཁམས་མང་པོ་པ་ལས་གང་དག་སའི་ཁམས་དང་། ཆུའི་ཁམས་དང་། མེའི་ཁམས་དང་། རླུང་གི་ཁམས་དང་། ནམ་མཁའི་ཁམས་དང་། རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་བསྟན་པ་ལ། དེ་དག་ལས་གཉིས་ཀྱི་མཚན་ཉིད་མ་བཤད་ན་དེ་ཅི་ནམ་མཁའ་ཉིད་ནམ་མཁའི་ཁམས་ཡིན་པའམ། རྣམ་པར་ཤེས་པ་ཐམས་ཅད༌[^115]ཀྱང་རྣམ་པར་ཤེས་པའི་ཁམས་ཡིན་པར་རིག་པར་བྱའམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 292]
འོ་ན་ཅི་ཞེ་ན། སྒོ་དང་། སྐར་ཁུང་དང་། ཁ་དང་སྣ་ལ་སོགས་པའི་བུ་ག་ནམ་མཁའི་ཁམས་ཞེས་བྱ། བུ་ག་ཞེས་བྱ་བ་ཅི་ཞིག་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། སྣང་དག་མུན་པ་དག་ཡིན་ལོ། །

[Block 293]
བུ་ག་ནི་སྣང་བ་དང་། མུན་པ་དག་ལས་གཞན་གཟུང་དུ་མེད་དོ། །

[Block 294]
དེ་ལྟ་བས་ན་ནམ་མཁའི་ཁམས་ནི་སྣང་བ་དང་མུན་པའི་རང་བཞིན་ཏེ། མཚན་མོ་དང་ཉིན་མོའི་རང་བཞིན་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་གྲག་གོ། །

[Block 295]
ཟག་དང་བཅས་པའི་རྣམ་ཤེས་ནི། །རྣམ་ཤེས་ཁམས་ཡིན། ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་ལ་མི་བྱ་ཞེ་ན། འདི་ལྟར་ཁམས་དྲུག་པོ་འདི་དག་ནི། སྐྱེ་བའི་རྟེན་ཡིན་པར་འདོད་དེ། དེ་དག་ནི་ཉིང་མཚམས་སྦྱོར་བའི་སེམས་ནས་འཆི་བའི་སེམས་ཀྱི་བར་དུ་སྐྱེ་བའི་གཞིར་གྱུར་པ་སྟེ། ཟག་པ་མེད་པའི་ཆོས་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 296]
དེའི་ཕྱིར། དེ་ལྟར་ན་དེ་དག་ལས་ཁམས་བཞི་ནི་རེག་བྱའི་ཁམས་ཀྱི་ནང་དུ་འདུས་སོ། །

[Block 297]
ལྔ་པ་ནི་གཟུགས་ཀྱི་ཁམས་ཀྱི་ནང་དུ་འདུས་སོ། །

[Block 298]
དྲུག་པ་ནི་རྣམ་པར་ཤེས་པའི་ཁམས་བདུན་པོ་དག་ཏུ་འདུས་སོ། །

[Block 299 [HEADING]]
### ཁམས་བཅོ་བརྒྱད་བསྟན་པ། ^1-18-0

[Block 300 [HEADING]]
#### བསྟན་དུ་ཡོད་པ། ^1-18-1-0

[Block 301]
གང་དག་ཁམས་བཅོ་བརྒྱད་བསྟན་པ་དེ་དག་ལས་བསྟན་དུ་ཡོད་པ་རྣམས་ནི་དུ། བསྟན་དུ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན།

[Block 302 [VERSE]]
བསྟན་ཡོད་འདིར་ནི་གཟུགས་གཅིག་པུ།[^116] །
དེ་ནི་འདི་ནི་འདི་ནའོ། །

[Block 303]
ཆེ་གེ་མོ་ཞིག་གོ་ཞེས་བསྟན་པར་ནུས་སོ། །

[Block 304]
ལྷག་མ་རྣམས་ནི་བསྟན་དུ་མེད་པའོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 305 [HEADING]]
#### ཐོགས་པ་དང་བཅས་པ། ^1-18-2-0

[Block 306]
ཐོགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཐོགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། ཐོགས་དང་བཅས་པ་གཟུགས་ཅན་བཅུ། །གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་པའི་ཁམས་བཅུ་གང་དག་བཤད་པ་དེ་དག་ནི་སྒྲིབ་པ་ལ་ཐོགས་པས་ཐོགས་པ་དང་བཅས་པ་རྣམས་སོ། །

[Block 307 [HEADING]]
#### དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ། ^1-18-3-0

[Block 308]
ལུང་མ་བསྟན་བརྒྱད་དེ་དག་ཉིད། །གཟུགས་སྒྲ་མ་གཏོགས་དབང་པོ་ལྔ་པོ་རྣམས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་རྣམས་ཏེ་བརྒྱད་པོ་དེ་དག་ནི་དགེ་བ་དང་མི་དགེ་བའི་ངོ་བོར་ལུང་བསྟན་དུ་མེད་པའི་ཕྱིར་ལུང་མ་བསྟན་དག་གོ། །

[Block 309]
གཞན་རྣམ་གསུམ། སེམས་ཀྱི་ཁམས་བདུན་མ་ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན༌[^117]པ་དག་ནི་དགེ་བ་ཡིན་ནོ། །

[Block 310]
ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པ་དག་ནི་མི་དགེ་བ་ཡིན་ནོ། །

[Block 311]
གཞན་དག་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 312]
ཆོས་ཀྱི་ཁམས་ནི་མ་ཆགས་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དང་མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་བསླང་བ༌[^118]དང་། སོ་སོར་བརྟགས་པས་འགོག་པ་ནི་དགེ་བའོ། །

[Block 313]
ཆགས་པ་ལ་སོགས་པའི་ངོ་བོ་དང་མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་བསླང་བ་ནི་མི་དགེ་བའོ། །

[Block 314]
གཞན་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 315]
གཟུགས་དང་སྒྲའི་ཁམས་ནི་ལུས་དང་ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱིས་བསྡུས་པ་དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པའི་སེམས་ཀྱིས་ཀུན་ནས་བསླང་བ་དག་ནི་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 316 [HEADING]]
#### འདོད་པའི་ཁམས་སུ་གཏོགས་པ། ^1-18-4-0

[Block 317]
འདོད་པའི་ཁམས་སུ་གཏོགས་པ་དག་ནི་དུ་ཞེ་ན། འདོད་ཁམས་གཏོགས་པ་ཐམས་ཅད་དོ། །

[Block 318]
གཏོགས་པ་ནི་མ་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 319 [VERSE]]
གཟུགས་ཀྱི་ཁམས་ན་བཅུ་བཞི་སྟེ། །
དྲི་དང་རོ་དང་སྣ་དང་ནི། །
ལྕེ་ཡི་རྣམ་ཤེས་ཁམས་མ་གཏོགས། །

[Block 320]
དེ་ན་དྲི་དང་རོ་དག་མེད་དེ། [^119]གཉིས་ནི་ཁམས་ཀྱི་ཟས་ཡིན་པའི་ཕྱིར་ཡིན་ལ། དེ་ལ་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེར་སྐྱེ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
