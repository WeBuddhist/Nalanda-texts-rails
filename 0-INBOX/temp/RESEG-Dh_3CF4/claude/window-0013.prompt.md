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
གང་དེ་དག་ལ་མངོན་པར་དད་པ་དང་མ་དད་པ་རྣམས་ཀྱང་དང་བར་འགྱུར་རོ། །

[Block 457]
བདག་གི་དོན་བརྩོན་ཞེས་བྱ་བ་ནི་བདག་གི་དོན་ལ་གཞོལ་བའོ། །

[Block 458]
ངོ་ཚ་ཞེས་བྱ་བ་ནི་ངོ་ཚའི་གནས་ཀྱིས་སོ། །

[Block 459]
འཇུངས་དང་འདོད་ཆེན་ཞེས་བྱ་བ་ལ། འཇུངས་པ་ནི་ཀུན་ཏུ་བཟུང་བའི་ཡོ་བྱད་ཀྱི་ཚོགས་ཡོངས་སུ་མི་གཏོང་བའི་ངང་ཚུལ་ལོ། །

[Block 460]
འདོད་ཆེན་ཞེས་བྱ་བ་ནི་ཞེན༌[^184]པས་གཟུང་བ༌[^185]སྟེ། བཟུང་བ༌[^186]དང་རྗེས་སུ་འབྲེལ་པའོ། །

[Block 461]
དེ་ལྟར་དེས་ནི་འཇུངས་པ༌[^187]དང་འདོད་ཆེན་པའི་སེམས་ཉེ་བར་བཅོམ་པ་ཡིན་ཏེ། ངོ་ཚ་བསྐྱེད་པར༌[^188]གྱུར་པ་ཡིན་ནོ། །

[Block 462]
དད་པ༌[^189]བསྐྱེད་པ་ནི་དང་བར་བྱེད་པ་ཡིན་ཏེ། སུ་དག་ཅེ་ན། ཐེག་པ་མཆོག་ལ་བརྟེན་པ་རྣམས་སོ། །

[Block 463]
ཐེག་པ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པའོ། །

[Block 464]
མཆོག་གི་སྒྲ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ཡོངས་སུ་བཟུང་ངོ་། །བརྟེན་པ་རྣམས་ཀྱང་ཐེག་པ་གསུམ་ལ་བརྟེན་པ་དད་པའོ། །

[Block 465]
ངོ་མཚར་མེད་པ་ཞེས་བྱ་བ་ནི་ཡ་མཚན་མེད་པ་སྟེ། སུ་ཞིག་ཅེ་ན། གཏོང་བ་བྱས་པ་རྣམས་ཀྱི་སྟེ། སྦྱིན་པ་ཆུང་ངུས་སྙེམས་པ་དེ་རྣམས་ཀྱི་ངོ་མཚར་གཞིག་པའོ། །

[Block 466]
སྦྱང་ཕྱིར་ཞེས་བྱ་བ་ནི་དག་པར་བྱ་བའི་ཕྱིར་ཏེ། གང་གི༌[^190]ཞེ་ན། མཐོ་རིས་ལམ་ཆེན་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 467]
གཏོང་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་འདོད་པ་རྣམས་ཏེ། སུ་དག་ཅེ་ན། བྱང་ཆུབ་སེམས་དཔའ་སྦྱིན་པ་རྟུལ་ཕོད་པ་རྣམས་སོ། །

[Block 468]
གཏོང་ལ་དགའ་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས༌[^191]བཅད་མཐའ་དག་ལ་དེ་བས་ལུས་ཀྱིས༌[^192]ཡོངས་སུ་བསྲུང་བར་བྱ་ཞེས་སྦྱར་རོ། །

[Block 469]
དེའི་འབྲས་བུ༌[^193]ཡོད་པར་བྱ་ཞེས་བྱ་བ་ནི་དེ་འབྲས་བུ༌[^194]གང་ཡིན་པ་དེ་འབྲས་བུ་དང་བཅས་པར་བྱ་བ་སྟེ། ཡིད་ལ་སེམས་པའི་སྨོན་ལམ་མོ། །

[Block 470]
བྱང་ཆུབ༌[^195]མཆོག་ཀྱང་བདག་གིས་ཉེ་བར་བྱ། །ཞེས་བྱ་བ་ནི་བདག་གིས་བྱའོ་ཞེས་སྦྱར་རོ། །

[Block 471]
དེ་བས་ལུས་ཀྱིས༌[^196]ཡོངས་སུ་བསྲུང་བར་བྱ་བའི་དང་པོའོ། །

[Block 472]
ཚིགས་སུ་བཅད་པ་ལྔས་ནི་རིམ་པ་བཞིན་དུ་དཔྱད་པས༌[^197]དུས་གསུམ་གྱི་སེམས་ཅན་གྱི་དོན་སྒྲུབ་པའི་ཕྱིར་མངོན་པར་བརྟག༌[^198]ཅིང་ངེས་པར་བྱས་པ་སྟེ། རང་གི་ལུས་བཏང་བས་སྟག་མོ་དང་སྟག་ཕྲུག་གཉིས་ཡང་དག་པར་བསྲུངས་པ་ནི་ད་ལྟར་གྱི༌[^199]གཞན་གྱི་དོན་ནོ། །

[Block 473]
འཇིག་རྟེན་ཕན་བརྩོན་རྣམས་ལ་བསྟན་ཞེས་པའི་དང་པོའི་ཚིགས༌[^200]བཅད་གསུམ་གྱིས༌[^201]མ་འོངས་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བསྟན་ཏོ། །

[Block 474]
ཕུན་སུམ་ཚོགས་པ་བསྐྱེད་པ༌[^202]ལ་མངོན་པར༌[^203]བརྟགས་ནས་ལུས་ཙམ་གྱིས་ཀྱང་ནམ་ཞིག་ཕན་ཐོགས་པར་གྱུར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འདས་པའི་དུས་ཀྱི་ལུས་ཀྱིས་གཞན་ལ་ཕན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 475]
སྨོན་ལམ་ནི་འདོད་པའི་དོན་ནོ། །

[Block 476]
འབྲས་བུ་ཡོད་པར་བྱ་བའི་ཕྱིར་ཡང་བདག་གི་ལུས་གཏང་བར༌[^204]བྱ་སྟེ། དེ་ཡིས་བསམས་པའི་སྨོན་ལམ་འདས་པར་གྱུར་པ་ཡིན་པས་དེའི་སྨོན་ལམ་སྒྲུབ་པ་ནི་འདས་པའི་སེམས་ཅན་རྣམས་ཀྱི་དོན་ཞེས་བརྗོད་དོ། །

[Block 477]
བྱང་ཆུབ་མཆོག་ཀྱང་ཉེ་བར་བྱ་ཞེས་བྱ་བ་འདི་ལ་ཀྱང་གི་སྒྲ་ནི་གཞན་གྱི་སྒྲ་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 478]
བྱང་ཆུབ་ཀྱི་མཆོག་ཐོབ་པ་ནི་གཞན་གྱི་དོན་བྱ་བས་སོ། །

[Block 479]
འགྲན་ཕྱིར་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས༌[^205]བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། མཐོང་བའི་ཆོས་དང་། མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པའི་འབྲས་བུར་བཅས་པ་དང་འབྲེལ་པའི་ཕྱིར་བདག་གིས་བྱས་པ་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 480]
མཐོ་རིས་འདོད་དང་རྒྱལ་སྲིད་བསྒྲུབ༌[^206]ཕྱིར་མིན། །ཞེས་བྱ་བ་སྟེ། འཇིག་རྟེན་རྣམས་ནི་གཞན་ཕལ་ཆེར་ཟིལ་གྱིས་གནོན་པ༌[^207]དང་། བདག་ཉིད་ཀྱི་ཡོན་ཏན་འབྱུང་བའི་ཕྱིར་དགེ་བ་རྣམས་ལ་བརྩོན་པར་བྱེད༌[^208]དེ་གཉི་ག་མ་ཡིན་པའི་ཕྱིར་འགྲན་ཕྱིར་མ་ཡིན་གྲགས་པའི་དོན་ཕྱིར་མིན་ཞེས་བྱའོ། །

[Block 481]
འདི་གཉིས་ཀྱིས་ནི་མངོན་པར་མཐོ་བ་འདོད་པ་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 482]
མཐོ་རིས་འདོད་དང་རྒྱལ་སྲིད་བསྒྲུབ་ཕྱིར་མིན། །ཞེས་བྱ་བ་སྟེ། འདི་གཉིས་ཀྱིས་ནི་མངོན་པར་མཐོ་བའི་ལྷར་སྐྱེ་བ་དང་། མི་རིགས་ཁྱད་པར་ཅན་དུ་སྐྱེ་བ་མི་འདོད་པར་བསྟན་ཏོ། །

[Block 483]
བདག་གིས༌[^209]བདེ་བ་མཆོག་ནི་ཐོབ་ཕྱིར་མིན། །ཞེས་བྱ་བ་འདིས་ནི་ངེས་པར་ལེགས་པ་དོན་དུ་མི་གཉེར་བ་ཡིན། བདག་གིས༌[^210]བདེ་བ་མཆོག་ཅེས་བྱ་བ་ནི་བདག་བདེ་བ་མྱ་ངན་ལས་འདས་པ་ཐོབ་པ་ཡིན་ཏེ། དེ་ལ་ཡང་བརྩོན་པར་མི་བྱེད་དོ་ཞེས་པ་སྟེ། སྨྲས་པ། གཞན་དོན་སྒྲུབ་ཕྱིར་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་དོན་བསྒྲུབ་པ༌[^211]ཞེས་བྱ་བ་བཤད་པའི་གཞན་དོན་སྒྲུབ་པ་དེ་གང་ཡིན་ཞེ་ན། གཞན་གྱི་དོན་སྒྲུབ་པ་སྟེ། གཞན་གྱི་དོན་སྒྲུབ་པའི་རྣམ་པ་དོན་དུ་གཉེར་བའོ། །

[Block 484]
དེ་བས་བདག་ནི་ཞེས་བྱ་བས་ན༌[^212]མཐོང་ཞིང་ཐོས་སམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་མངོན་པར་མཐོ་བ་ལས་བརྩམས་ཏེ། འདིས་ཞེས་བྱ་བ་ནི་རང་གི་ལུས་སྦྱིན་པའི་དགེ་བས་སོ། །

[Block 485]
དུས་གཅིག་ཏུ་ཞེས་བྱ་བ་ནི་ཅིག་ཅར་སྡུག་བསྔལ་བསལ་བ༌[^213]དང་བདེ་བ་འབྱུང་བར་གྱུར་ཅིག་པའོ། །

[Block 486]
མངོན་པར་མཐོ་བ་ལས་བརྩམས་ཏེ། མཐོང་ཞིང་ཐོས་སམ་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་ལ། རེག་གམ་ཞེས་བྱ་བ་ནི་ལུས་དང་ངོ་། །གཏམ་དུ་བརྗོད་པར་གྱུར་ཀྱང་ཞེས་བྱ་བ་ནི་ཆོས་བསྟན་པ་དང་མཉན་པས་སོ། །

[Block 487]
རྣམ་ཀུན་ཏུ་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བ་བསྐྱེད་ཅིང་འཕེལ་བ་དང་། ནུས་པར་ལྡན་ཞིང་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་ནི། རྣམ་པ་ཀུན་ཏུ་ཕན་པའོ། །

[Block 488]
ཁྲོས་ཤིང་ངོ་མཚར་སྐྱེས་ནས་ཞེས་བྱ་བ་ལ། ཁྲོས་ཤིང་ངོ་མཚར་སྐྱེས་པ་ནི༌[^214]ཅི་ཞིག་ཅེས་ལངས་ནས་བྲོས་ཏེ་གཞན་དག་གི་ཕྲུ་གུ༌[^215]ཟོས་པར་དོགས་པ་དང་། ལྟོགས་པས༌[^216]ཟ་བར་འདོད་པ་ཡང་བཏང་སྟེའོ། །

[Block 489]
ཉེ་བར་འོངས་ཏེ་ཞེས་པ་ནི་དྲུང་དུ་ཕྱིན་པའོ། །

[Block 490]
བརྩམས་པ༌[^217]ནི་རྩོམ་པའོ། །

[Block 491]
དེ་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་དེའི་ལས་ཁྱད་པར་ཅན་ནོ། །

[Block 492]
ལས་ཁྱད་པར་ཅན་དེས་ངོ་མཚར་བ་དེ་ནི་སྤྱོད་པ་ཁྱད་པར་ཅན་ངོ་མཚར་རོ། །

[Block 493]
དེ་བས་ན་མྱ་ངན་དང་སྡུག་བསྔལ་ནི་མྱ་ངན་དང་སྡུག་བསྔལ་ཏེ། མྱ་ངན་ནི་བླ་མ་སྡུག་པ་དང་བྲལ་བས་སོ། །

[Block 494]
སྡུག་བསྔལ་ནི་མྱ་ངན་གྱིས༌[^218]ཀུན་ནས་བསླང་བ་སྟེ། ལུས་དང་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །

[Block 495]
དེ་གཉིས་ཀྱི་ཤུགས་ཀྱིས་ཡང་དག་པར་བསྐྱེད་པའོ། །
--- END BLOCKS ---
