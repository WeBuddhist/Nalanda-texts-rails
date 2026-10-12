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
བཤད་པའི་མིང་བསྟན་པ། ཇི་སྐད་ཅེས་བྱ་བ་བཤད་པ་ཡིན་ཞེ་ན། དགོངས་པ་མིན་པས་བཤད་པའོ། །ཞེས་སྨོས་སོ། །

[Block 457]
འདིའི་དོན་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ཇི་ལྟ་བུའི་རྣམ་པར་སྟོན་པས་ནི་དགོངས་པ་མ་ཡིན་པས་བཤད་པའོ་ཞེས་སྨོས་སོ། །

[Block 458]
དེ་ནས་སྒྲ་ཇི་བཞིན་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དཀྱིལ་འཁོར་རྫོགས༌[^228]དང་རྟོག་པ་ལས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་དཀྱིལ་འཁོར་དང་སྒྲུབ་པ་དང་། དབང་དང་། དམ་ཚིག་དང་། ཕྲིན་ལས་ཞེས་བྱ་བའོ།

[Block 459]
[^229] །རྟོག་པ་ནི་དེ་ཉིད་གསལ་བར་སྟོན་པར་བྱེད་པའི་རྒྱུད་དོ། །

[Block 460]
དེ་ལས་སྤྱོད་པ་ཇི་ལྟར་གསུངས། །ཞེས་པ་ནི་དོན་ཇི་ལྟ་བར་སྒྲ་ཡང་དེ་ལྟར་གསུངས་ཞེས་པའོ། །

[Block 461]
དེ་ལྟ་བུའི་དོན་རྒྱས་པར༌[^230]བཤད་པ་གང་ཡིན་པ་དེ་ནི་ཇི་བཞིན་སྒྲར་གསུངས་པའོ་ཞེས་པའོ། །

[Block 462]
སྒྲ་ཇི་བཞིན་པ་མ་ཡིན་པ་གང་ཞེ་ན། ཀོ་ཊ་ཀྵ་ལ་སོགས་པའི་སྒྲ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཀོ་ཊ་ཀྵ་ནི་ཀོ་ཊ་ཀྵ་སྟེ་ཀོ་ཊ་བ་ཞེས་པ་ལ་སོགས་པ་གཟུང་ངོ་། །འདི་ཉིད་ནི་བརྡ་ཉིད་དོ། །

[Block 463]
བརྡ་ཅན་ཡང་གང་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཁྱབ་བྱེད་ཀྱི་རླུང་ལ་སོགས་པའོ། །

[Block 464]
དེ་ལྟ་བུའི་བསྟན་བཅོས་ཤིན་ཏུ་དཀོན་པའི་ཕྱིར། འཇིག་རྟེན་བསྟན་བཅོས་ལ་མེད་ཅིང་། །ཞེས་བྱ་བ་སྨོས་ཏེ། འཇིག་རྟེན་གྱི་བསྟན་བཅོས་ནི་འཇིག་རྟེན་གྱི་བསྟན་བཅོས་ཏེ། དེ་ལ་གང་མེད་པ་ནི་འཇིག་རྟེན་གྱི་བསྟན་བཅོས་ལ་མེད་པའོ། །

[Block 465]
འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་ལ་མེད་པ་མ་ཡིན་ནམ། འདི་ཅིའི་ཕྱིར་འཇིག་རྟེན་གྱི་བསྟན་བཅོས་ལ་མེད་ཅེས་སྨོས་ཤེ་ན་མ་ཡིན་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པའི་བརྡར་གྱུར་པ། །ཞེས་སྨོས་ཏེ་དེ་བཞིན་གཤེགས་པ་ཁོ་ནའི་བརྡར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 466]
འཇིག་རྟེན་བསྟན་བཅོས་ལ་མེད་ཅིང་། །ཞེས་བྱ་བ་འདིས་ནི་ཐུན་མོང་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 467]
དེ་བཞིན་གཤེགས་པའི་བརྡར་གྱུར་པ། །ཞེས་བྱ་བ་འདི་ནི་གཉིས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཁོ་ནའི་བརྡར་གྱུར་པ་ཞེས་པ་འདིས་གཞན་དང་ལྡན་པ་རྣམ་པར་བཤད༌[^231]པའོ། །

[Block 468]
དེ་བཞིན་གཤེགས་པའི་བརྡར་གྱུར་པ་ཁོ་ནའི༌[^232]ཞེས་བྱ་བ་འདི་ནི་མ་འབྲེལ་པ་རྣམ་པར་བཤད༌[^233]པའོ། །

[Block 469]
འདིའི་མིང་ཅི་ཞེ་ན། དེ་ནི་ཇི་བཞིན་མིན་པར་བསྒྲགས། །ཞེས་བྱ་བ་སྨོས་ཏེ་སྒྲ་ཇི་བཞིན་པ་ལ་སོགས༌[^234]པའི་ཕྱིར་ཇི་བཞིན་མིན་པར་བསྒྲགས་ཞེས་སྨོས་སོ། །

[Block 470]
མཐའ་དྲུག་དབྱེ་བ་བསྟན་ནས་ནི། །ཞེས་པ་མཐའ་དྲུག་གི་དབྱེ་བ་ནི་མཐའ་དྲུག་གི་དབྱེ་བ་སྟེ། མཐའ་དྲུག་སྤྲོས་པ་དང་བཅས་པ་བསྟན་ཞེས་བྱ་བའོ། །

[Block 471]
ནི་ཞེས་བྱ་བ་ནི་གཞན་འདྲེན་པའི་ཚིག་གོ། །

[Block 472]
བཤད་པའི་དབྱེ་བ་བརྗོད་པར་བྱ། །ཞེས་བྱ་བ་ནི་བཤད་པའི་དབྱེ་བ་ནི་ཡི་གེའི་དོན་ལ་སོགས་པའོ། །

[Block 473]
དེ་ཉིད་བཤད་པ་ནི་རྣམ་པ་གསུམ་སྟེ་བསྡུས་པའི་དབྱེ་བ་དང་། བར་མཚམས་ཀྱི་དབྱེ་བ་དང་། ཤིན་ཏུ་རྒྱས་པའི་དབྱེ་བའོ། །

[Block 474]
བསྡུས་པའི་དབྱེ་བ་ནི་ཚིག་གི་དོན་དང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 475]
བར་མཚམས་ཀྱི་དབྱེ་བ་ནི།

[Block 476]
དང་པོ་གཅིག་པུ་ཁོ་ན་ཉིད། །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 477]
ཤིན་ཏུ་རྒྱས་པའི་དབྱེ་བ་བསྟན་པའི་ཕྱིར། སྒྲ་ཙམ་ལ་ནི་རབ་གཞོལ་བའི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 478]
དེ་ཉིད་བཤད་པ་ཡི་གེའི་དོན་ཞེས་བྱ་བ་ནི་དུ་ཞིག །ཅིའི་ཕྱིར་ཡི་གེའི་དོན་དུ་བརྟག་ཅེ་ན་བཤད་པ། སྒྲ་ཙམ་ལ༌[^235]ནི་རབ་གཞོལ་བའི། །ཞེས་པ་ནི་སྒྲ་འབའ་ཞིག་ལ་ཉེ་བར་གཞོལ་གྱི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་དོན་ནི་མ་ཡིན་ནོ། །

[Block 479]
ཕྱི་རོལ་བསྟན་བཅོས་མཁས་པ་ཡིས། །ཞེས་བྱ་བ་ནི་གཞུང་འདི་པ་མ་ཡིན་པའི་ཕྱི་རོལ་གྱི་བསྟན་བཅོས་རྗེས་སུ་ཐོབ་པའོ། །

[Block 480]
དེ་ཡི་བཀོད་པ་རབ་བསྟན་པ། །ཞེས་པ་ནི་སྒྲའི་བཀོད་པ་ཉིད་དོ། །ཇི་སྐད་བྱ་བ་ཡིན་ཞེ་ན། ཡི་གེའི་དོན་ནི་ཡིན་པར་བཤད། ཅེས་སྨོས་ཏེ། སྒྲའི་བཤད་པ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 481]
དང་པོ་ནི་བཤད་པར་བྱ་བའི་ལུང་བསྟན་ཏོ། །

[Block 482]
ཞར་ལ་ནི་བཤད་པའི་དགོས་པ་བསྟན་ཏོ།[^236] །གཉིས་པས་ནི་བཤད་པ་པོ་བསྟན་ཏོ།[^237] །ཞར་ལ་ནི་དེའི་དགོས་པ་བསྟན་ཏོ། །

[Block 483]
གསུམ་པས་ནི་བཤད་པའི་ཐབས་བསྟན་ཏོ། །

[Block 484]
ཞར་ལ་ནི་དེའི་དགོས་པ་བསྟན་ཏོ། །

[Block 485]
བཞི་པས་ནི་བཤད་པའི་མིང་བསྟན་ཏོ། །

[Block 486]
ཞར་ལ་ནི་དེའི་དགོས་པ་བསྟན་ཏོ། །

[Block 487]
དེ་ནས་གཉིས་པ་བསྟན་པའི་ཕྱིར། སྤྱིའི་དོན་གྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མདོ་སོགས་ལ་ནི་རབ་བཞུགས་པའི། །ཞེས་སྨོས་སོ། །

[Block 488]
མདོ་སྡེ་དང་། འདུལ་བ་དང་མངོན་པའི་རྗེས་སུ་ཞུགས་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 489]
དེ་ལ་འགྱོད་པ་ནི་ཐེག་པ་ཆེན་པོའི་སེམས་བསྐྱེད་པ༌[^238]ལའོ། །

[Block 490]
དེའི་འགྱོད་པ་ཟློག་པར་བྱེད་པ་ནི་དེ་དང་མཐུན་པར་སྟོན་པའོ། །

[Block 491]
ཇི་སྐད་དུ་རིན་པོ་ཆེ་འབར་བའི་རྒྱུད་ལས་ཀྱང་། རིགས་ཀྱི་བུ་འདུལ་བ་ལ་དད་པར་གྱིས་ཤིག །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་བཞི་ཡིན་ནོ་ཞེས་པ་ལྟ་བུའོ། །

[Block 492]
བསྐྱེད་པའི་རིམ༌[^239]དང་ལྡན་པ་དག །ཅེས་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ཉིད་དོ། །

[Block 493]
དེ་དང་གང་ལྡན་པ་ནི་བསྐྱེད་པའི་རིམ་པ་དང་ལྡན་པའོ། །

[Block 494]
འདི་ཡང་སྤྱིའི༌[^240]ཡིན་ཞེས་པར་སྦྱར་རོ། །

[Block 495]
འདི་ལ་ཡང་ཅིའི་ཕྱིར་སྤྱི་ཞེས་བྱ་ཞེ་ན། འདི་ནི་ཁྱབ་པའི་ཕྱིར༌[^241]སྤྱི་ཡིན་ཞེས་པའོ། །
--- END BLOCKS ---
