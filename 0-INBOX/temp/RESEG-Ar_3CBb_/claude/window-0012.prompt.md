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
[Block 421]
དངོས་སུ་སྐལ་བ་ངན་པ་ནི་རིགས་ཆད་པའི་གང་ཟག་འབའ་ཞིག་གོ། །

[Block 422]
རིགས་ཆད་པའི་ཞེས་བྱ་བ་ཡང་ས་བོན་དང་བྲལ་བ་ནི་མ་ཡིན་གྱི། ཉོན་མོངས་པའི་སྤྱོད་པ་འབའ་ཞིག་ལ་ལྟོས༌[^210]ནས་སྐལ་བ་ངན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། དངོས་སུ་ན༌[^211]ཉན་ཐོས་ལ་སོགས་པའི་ཕྱིའི་ཕྱོགས་སུ་གཏོགས་པ་དང༌[^212]ཚོགས་ཀྱི་གང་ཟག་ནང་པའི་ཕྱོགས་སུ་གཏོགས་པའོ། །

[Block 423]
འདི་དག་ལ་ཡང་ཅིའི་ཕྱིར་སྐལ་བ་ངན་པ་ཞེས་བྱ་ཞེ་ན། དམ་པའི་ཆོས་ཟབ་ཅིང་རྒྱ་ཆེ་བ་ཉན་པའི༌[^213]སྐལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 424]
སྐལ་བ་མེད་པའི་ཕྱིར་རིགས་ཆད་པ་མ་ཡིན་ནམ། ཅིའི་ཕྱིར་ལྟོས༌[^214]ནས་སྐལ་བ་ངན་པ་ཞེས་བྱ་ཞེ་ན། རིགས་ཆད་པ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱི་འབྲས་བུ་མི་ཐོབ་པ་གང་ཡིན་པའོ། །

[Block 425]
འགའ་འགས་ཀྱང་ནི༌[^215]མི་ཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 426]
དེ་ལ་རྒྱལ་བས་གང་སྦས། སྦ་བ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པའི་ཆོས་ཟབ་ཅིང་རྒྱ་ཆེ་བ་ལ་སོགས་པ་སྦས་པ་སྟེ། མཐོང་བ་ཙམ་གྱིས་སྐྲག་པའི་ཕྱིར་རོ། །

[Block 427]
ཐམས་ཅད་ནས་ཐམས་ཅད་དུ་བསྟན་པར་བྱ་བ་མ་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར་གསུངས་པ། དྲང་བའི་དོན་ནི༌[^216]ཞེས་སྨོས་ཏེ། བཅོམ་ལྡན་འདས་ཉིད་ཀྱིས་ཀྱང་བདག་དང་། སྲོག་དང་། གསོ་བ་དང་། སྐྱེས་བུ་དང་། གང་ཟག་དང་། བྱེད་པ་པོ་དང་། ཚོར་བ་པོ་ལ་སོགས་པ་འཇིག་རྟེན་ན་ཡོད་དོ་ཞེས་གསུངས་པ་དང་། སེམས་དཔའ་ཆེན་པོ་མ་རིག་པ་ལས་ནི་འདུ་བྱེད་འབྱུང་ངོ་ཞེས་གསུངས་པ་དང་རྒྱལ་བའི་སྲས་དག་འདི་དག་སྟེ་ཁམས་གསུམ་པ་འདི་དག་ནི་རྣམ་པར་རིག་པ་ཙམ་མོ་ཞེས་འབྱུང་བ་དང་། གཞན་ཡང་ཆོས་ཐམས་ཅད་ནི་རང་བཞིན་མེད་པ་སྟེ་སྣང་བ་ཙམ་ནི་མ་གཏོགས་སོ། །

[Block 428]
རིགས་ཀྱི་བུ་ལྷའི་རྣལ་འབྱོར་ལ་དད་པར་གྱིས་ཤིག །འདི་ལས་ཡང་དག་པའི་ཐབས་ནི་ནམ་ཡང་རྙེད་པར་འགྱུར་བ་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་འདི་ནི་བཅོམ་ལྡན་འདས་ཉིད་ཀྱིས་ལམ་ཁྱད་པར་ཅན་དང་འབྲས་བུ་ཁྱད་པར་ཅན་ཐུགས་ལ་ཆུད་ནས་སྐལ་བ་ངན་པའི་སེམས་ཅན་གང་ལ་གང་གིས་འདུལ་བ་དེ་ལ་དེའི་སྒོ་ནས་དེ་ལྟར་ཆོས་སྟོན་པ་འདི་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དྲང་བའི་དོན་ཞེས་བྱའོ། །

[Block 429]
དེ་ལ་ངེས་པའི་དོན་གང་ཞེ་ན་ཞེས་དྲིས་པ་དང་། དེའི་ལན་དུ།

[Block 430 [VERSE]]
མཆོག་འདོད་སེམས་ཅན་རྣམས་ཀྱི་ཕྱིར། །
ངེས་པའི་དོན་ཡང་གསུངས་པ་ཡིན། །

[Block 431]
ཞེས༌[^217]མཆོག་འདོད་པའི་སེམས་ཅན་ནི་སྐལ་བ་བཟང་པོ་ཞེས་བྱ་བ་སྟེ། འབྲས་བུ་བཟང་པོ་ལ་སྤྱོད་པའི་སྐལ་བ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 432]
མཆོག་ཅེས་བྱ་བ་ནི་མཆོག་གི་དངོས་གྲུབ་སྟེ་དེ་འདོད་པ་ནི་དེ་ལ་གཅེས་པར་འཛིན་པའོ། །

[Block 433]
ཡང་ན་མཆོག་འདོད་པ་ནི་འདུན་པ་སྐྱེད་པ༌[^218]སྟེ་འདུན་པ་ནི་འདོད་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 434]
གྲོགས་ནི་མོས་པའོ། །

[Block 435]
དད་པ་དང་དྲན་པ་ལ་སོགས་པ་ཡང་ཅི་རིགས་སུ་འགྱུར་རོ། །

[Block 436]
མཆོག་འདོད་པའི་སེམས་ཅན་རྣམས་ཀྱི་ཕྱིར། དེ་ཉིད་ཀྱི་དོན་གསུངས་པ་ནི་ངེས་པའི་དོན་ཞེས་བྱའོ། །དེ་ཅིའི་ཕྱིར༌[^219]ངེས་པའི་དོན་ཞེས་བྱ་ཞེ་ན། ལམ་ངེས་པ་ཉིད་དང་། འབྲས་བུ་ངེས་པ་ཉིད་དང་། མཆོག་ཏུ་གྱུར་པ་ངེས་པ་ཉིད་དང་། རྨད་དུ་བྱུང་བ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར། དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 437]
ཡང་ན་ངེས་པའི་དོན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་ནས་མངོན་པར་སངས་རྒྱས་ཀྱི་བར་དུ་མི་སྤོང་། མི་འདོར། སྒྲིབ་པ་དང་། གོ་གཅོད་པར་མི་བྱེད། བསླབ་པ་དང་། དྲན་པ་ལ་སོགས་པ་འཕེལ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ངེས་པའི་དོན་ཞེས་བྱའོ། །

[Block 438]
དགོངས་པས་བཤད་པ་གང་ཞེ་ན། དེ་བཤད་པའི་ཕྱིར། མཆོག་འདོད་སེམས་ཅན་རྣམས་ཀྱི་ཕྱིར། །ཞེས་བྱ་བ་སྨོས་ཏེ། མཆོག་འདོད༌[^220]པ་ནི་མཆོག་འདོད་པ་སྟེ། མཆོག་གི་དངོས་གྲུབ་འདོད་ཅེས་པའི་དོན་ཏོ། །

[Block 439]
མཆོག་འདོད་པ་ཡང་ཡིན་ལ། སེམས་ཅན་ཡང་ཡིན་པས་མཆོག་འདོད་པའི་སེམས་ཅན་རྣམས་ཏེ་རྣམས་ཞེས་བྱ་བ་ནི་འདིར་མང་པོ་ལ་བྱའོ། །

[Block 440]
དེ་བས་ན་མཆོག་འདོད་པའི་སེམས་ཅན་མང་པོའི་ཕྱིར་བསྟན༌[^221]པའོ། །

[Block 441]
མཆོག་འདོད་པ་ནི་ཐུན་མོང་གི་དངོས་གྲུབ་འདོད་པ་མ་ཡིན་ཞེས་བྱའོ།[^222] །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཆོས་ཀྱི་དེ་ཉིད་རབ་སྟོན་པ། །ཞེས་སྨོས་ཏེ་ཆོས་ཀྱི་དེ་ཁོ་ན་ཉིད་ནི་ཆོས་རྣམས་ཀྱི་ངེས་པའི་དོན་ཏོ། །

[Block 442]
དེ་རབ་ཏུ་སྟོན་པ་ནི་ཆོས་ཀྱི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་སྟོན་པའོ། །ཇི་ལྟར་སྟོན་ཞེ་ན། འགལ་བའི་ཚིག་གི་སྦྱོར་བ་ཡིས། །གསུངས་ཞེས་པ་སྟེ་བསྟན་བཅོས་ལ་འགལ་བ་ནི་མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པ་བྱེད་པ་སྟེ་འདི་ལྟར་མ་བྱིན་པར་ལེན་པ་སྤངས་པ་དང་། མ་བྱིན་པར་ལེན་པ་བྱ་བ་ནི་གཅིག་གིས་གཅིག་སྤངས་པའི་ཕྱིར་རོ། །

[Block 443]
དེ་བས་ན་མ་བྱིན་པར་ལེན་པའི་སྟོབས་ཀྱིས་སངས་རྒྱས༌[^223]པར་འགྱུར་ཞེས་པ་ནི་བསྟན་བཅོས་དང་འགལ་བར་འགྱུར་རོ། །

[Block 444]
འགལ་བའི་ཚིག་གི་སྦྱོར་བ་དེའི༌[^224]དེ་ཁོ་ན་ཉིད༌[^225]སྟོན་པར་བྱེད་པ་གང་ཡིན་པ་འདི་ནི་དགོངས་པས་བཤད་པ་སྟེ། འདི་ཅི་ལ་དགོངས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དགོངས་པ་ལུང་སྟོན་པའི་རྒྱུད་དུ་ཤེས་པར་བྱའོ། །

[Block 445]
འདིར་ནི་བཤད་པར་བྱ་བ་དང་། བཤད་པའི་དགོས་པ་དང་། བཤད་པའི་ཡུལ་དང་། བཤད་པའི་སྦྱོར་བ་དང་། བཤད་པའི་མིང་ཙམ་སྟོན་པར་འགྱུར་རོ། །

[Block 446]
འདི་ཡང་གང་ཟག་ཇི་ལྟ་བུ་ལ་བཤད་ཅེ་ན་ཤེས་རབ་མཆོག་ཏུ་གྱུར་པ་དང་། བརྡ་ལ་གོམས་པ་རྣམས་སོ་ཞེས་པའོ། །

[Block 447]
བློ་དམན་རྣམས་ལ་མི་སྟོན་པ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་ལམ་ལོག་པ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 448]
འོ་ན་ཐམས་ཅད་དུ་ཐམས་ཅད་སྟོན་པར་བྱེད་པ་མ་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 449]
དབང་པོ་དམན་པའི་སེམས་ཅན་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དབང་པོ་དམན་པ་ནི་དད་པའི་དབང་པོ་ལ་སོགས་པ་དམན་པའོ། །

[Block 450]
འདི་ལྟར་ཟག་པ་མེད་པའི་དབང་པོ་ཐམས་ཅད་ནི་སྔར༌[^226]འགྱུར་ཏེ། འདིར་ནི་ཤེས་རབ་ཀྱི་དབང་པོ་དམན་ཞེས་པའོ། །ཤེས་རབ་ཀྱི་དབང་པོ་དམན་པ་ཞེས་པ༌[^227]ཤེས་རབ་ཞན་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 451]
འདི་དག་གིས་ནི་བཤད་པར་བྱ་བའི་ཡུལ་བསྟན་ཏོ། །

[Block 452]
དེ་ནས་བཤད་པའི་དགོས་པ་བསྟན་པའི་ཕྱིར་རྟོགས་ཕྱིར་ཞེས་བྱ་བ་སྨོས་ཏེ། དབང་པོ་དམན་པའི་སེམས་ཅན་གྱིས་རྟོགས་པའི་ཕྱིར་དགོངས་པ་མ་ཡིན་པས་བཤད་ཅེས་པའོ། །

[Block 453]
བཤད་པའི་སྦྱོར་བ་བསྟན་པའི་ཕྱིར་མཆོག་ཏུ་གསལ་བ་ཡིས་ཞེས་པ་སྨོས་ཏེ། མཆོག་ཏུ་གསལ་བ་ནི་དགོངས་པས་བཤད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 454]
བཤད་པར་བྱ་བ་བསྟན་པའི་ཕྱིར། དེ་ཉིད་ངེས་པར་སྟོན་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཉིད་ཅེས་བྱ་བ་ནི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན་ཉིད་ལ་སོགས་པའོ། །

[Block 455]
དེ་ཉིད་མ་ནོར་བར་སྟོན་པ་ནི་ངེས་པར་སྟོན་པའོ། །

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
--- END BLOCKS ---
