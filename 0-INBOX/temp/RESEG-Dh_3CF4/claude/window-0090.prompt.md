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
[Block 3151]
དེས་མྱོས་པ་ནི་དཔལ་ལྡན་ཆང་གིས་མྱོས་བཞིན་ནའོ། །

[Block 3152]
དཔལ་དང་ལྡན་པ་ཆང་གིས་སེམས༌[^1995]ཡོངས་སུ་དཀྲུགས་ཏེ་བདག་གི་དོན་ཡང་འདོར་བ་ནི་བག་མེད་པའོ། །

[Block 3153]
བག་ཡོད་རྣམས་ནི་ཞེས་བྱ་བ་ནི་བག་དང་ལྡན་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་དང་གཞན་གྱི་དོན་དུའོ། །

[Block 3154]
བག་ཡོད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་མང་པོས་གདུངས་པའི་སེམས་ཅན་ལ། །ཞེས་སྨོས་ཏེ། འདིའི་བསྡུས་པའི་དོན་ནི་སྙིང་རྗེ་དང་། བརྟན་པ་དང་ཤེས་རབ་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་གཞན་གྱི་དོན་སྤྱོད་པ་ཡོངས་སུ་མི་བརྗོད༌[^1996]པའོ། །

[Block 3155]
སེམས་ཅན་ལ་བརྩེ་ཞིང་རང་གི་བདེ་བ་ལ་མ་ཆགས་པ་དང་། བརྟན་པ་ལ་གནས་པའི་སྤྱོད་པ་དང་། ཤེས་རབ་ཀྱི་རང་བཞིན་ཤེས་པས་སོ། །

[Block 3156]
སྙིང་རྗེ་བ་ནི་མི་དགེ་བའི་ལམ་ལས་བཟློག་པ་དོན་དུ་གཉེར་བའོ། །

[Block 3157]
བྱམས་པ་ནི་ཕན་པ་དང་བདེ་བ་ལ་སོགས༌[^1997]པའོ། །

[Block 3158]
མཐུ་ཆེ་བའི་མིག་གིས་ཞེས་བྱ་བ་ནི་ལྷའི་མིག་གིས་སོ། །

[Block 3159]
མི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་པའི་སྐྱོན་གྱིས་ཞེས་བྱ་བ་ནི་རྐྱེན་གྱིས༌[^1998]འབྱུང་བའི་ཕྱིར་རང་ཉིད་ཀྱིས་ནི་ལྡོག་པར་མི་ནུས་པ་ཉིད་དེ། དེ་བས་ན་སྐྱོན་ཞེས་བསྟན་ཏོ། །

[Block 3160]
བློན་པོ་དང་འབངས་སུ་བཅས་པར་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་མང་པོ་ལ་གནོད་པ་ཡིན་ཏེ། དེའི་རྐྱེན་གྱིས་སོ། །

[Block 3161]
དེ་ལ་ཞེས་བྱ་བ་ནི་ཆང་འཐུང་བ་ལའོ། །

[Block 3162]
སྐྱོན་དུ་ཡང་མི་ལྟ་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི། སྐྱོན་དུ་ལྟ་བའི་ནུས་པ་ལས་ཉམས་པར་སྟོན་ཏོ། །

[Block 3163]
སྐྱོན་ཆེ་བ་ཞེས་བྱ་བ་འདིས་ནི་དེ་ཉིད་སྟོན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 3164]
འདི་དག་ཐམས་ཅད་ནི་བསམ་པའི་དོན་གྱི་རྒྱུ་ཡིན་ཏེ། འཐུངས་ན་ཐོག་མར་རབ་ཏུ་ཞིམ་ཞེས་བྱ་བ་འདི་དག༌[^1999]སྨྲས་སོ། །

[Block 3165]
ཐོག་མར་ཞིམ་པ་ནི་སྐྱོན་དུ་ལྟ་བ་ལ་རྨོངས་པ་ཡིན་ཏེ། [^2000]ཕྱི་ནས་རྗེས་སུ་འབྲེལ་པའི་ཉེས་པ་ལ་ནི་རྨོངས་པར་གྱུར་པས་སོ། །

[Block 3166]
ལེགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པ་གཉིས་ལ་གཟུང་ངོ་། །ཡང་ན་ལོག་པའི་ལམ་བཞིན་ཞེས་བྱ་བ་ནི་ལམ་ངན་པ་བཞིན་དུའོ། །

[Block 3167]
ཅུང་ཟད་རྩུབ་པ་ཞེས་བྱ་བ་ནི་ཅུང་ཟད་རྩུབ་པའོ། །

[Block 3168]
རལ་པའི་ཐོར་ཚུགས་ཡིན་པས་ན་སྐྲའི་ཐོར་ཚུགས་སོ། །

[Block 3169]
གྱེན་དུ་མདུད་པའི༌[^2001]ཕྱིར་འཁྱིལ་བའོ། །

[Block 3170]
ཅུང་ཟད་རྩུབ་པ་ཡང་ཡིན་ལ་འཁྱིལ་པ་ཡིན་པས་ཅུང་ཟད་རྩུབ་ལ་འཁྱིལ་བའོ། །

[Block 3171]
སྐྲའི་ཐོར་ཚུགས་ཅུང་ཟད་རྩུབ་ལ་འཁྱིལ་བ་ག་ལ་ཡོད་པ་དེ་ནི་སྐྲའི་ཐོར་ཚུགས་ཅུང་ཟད་རྩུབ་པ་འཁྱིལ་བ་ཅན་ནོ། །

[Block 3172]
ཤིང་གི་ཤུན་ལྤགས་དང་། རི་དགས་ཨ་ཛི་ནའི་པགས་པ་གཉིས་གྱོན་པའོ། །

[Block 3173]
ཆང་གིས་གང་བ་ནི་ཆང་གིས་གང་བ་སྟེ། བུམ་པ་ཡང་མངོན་པར་སྤྲུལ་ལོ། །

[Block 3174]
རིམ་གྲོ་བསྐྱེད་པ་ཞེས་བྱ་བ་ནི་འདྲ་བའི་རིམ་གྲོ་བསྐྱེད་པ་སྟེ། རྗེས་སུ་མཐུན་པའི་རིམ་གྲོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3175]
མེ་ཏོག་གི་ཕྲེང་བ་མགུལ་ན་བཀོད་པ་གང་ཡིན་པ་དེ་ནི་མེ་ཏོག་གི་ཕྲེང་བ་མགུལ༌[^2002]ན་བཀོད་པའོ། །

[Block 3176]
རྒྱན་གྱིས་བརྒྱན་པ་ཡིན་ཏེ། གང་གིས་ཤེ༌[^2003]ན། བུམ་པའི་རྒྱན་གྱིས་ཏེ། བུམ་པའི་རྒྱན་ནི་རྣ་བ་ལ་བརྒྱན་པའོ། །

[Block 3177]
ཁྱོད་ཀྱི་སྐུ་ཞེས་བྱ་བ་ནི་ཆ་བྱད་དོ། །

[Block 3178]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་འོག་ནས་བསྟན་པའི་རྒྱུས་སོ། །

[Block 3179]
ཁྱེད་ཅག་འཇིག་རྟེན་གཞན་ལ་མི་འཇིགས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3180]
ངེད་ལ་ཞེས་བྱ་བ་ནི་མི་རྣམས་ལའོ། །

[Block 3181]
ཁྱོད་ལྟ་བུ་ཞེས་བྱ་བ་ནི་ལྷའོ།[^2004] །འདི་ནི་ཆུ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དེ་ནི༌[^2005]ཆང་འཐུང་བའི་ཕྱིར་གཞན་ལྟུང་བར༌[^2006]བྱ་བ་ལ་ཞོ་ལ་སོགས་པ་མི་འདོད་པ་ཡིན་པས་དེ་དག་གིས་དགའ་བ་མ་ཡིན་པ་བསྟན་པའི་ཕྱིར་དང་། ཆུ་ལ་སོགས་པ༌[^2007]འཇིག་རྟེན་པ་དག་ལ་རབ་ཏུ་བསྔགས་པ་ཡིན་ཏེ། དེས་ན༌[^2008]འདི་དག་སྨོས་སོ། །

[Block 3182]
གང་གོང་དུ་བསྟན་པ་དེ་ལ་སྐྱོན་དུ་ཡང་མི་ལྟ་བར་འགྱུར་ལ། ཆང་འཐུང་བ་ཡང་སྐྱོན་ཆེ་བར་མཐོང་ནས་ཞེས་བྱ་བ་ནི་ཆང་གི་སྐྱོན་ཆེ་བར༌[^2009]ཡང་དག་པར་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་བཅུ་བདུན་གྱིས་བསྟན་པ་སྟེ། དེ་ལ་ཆང་གི་སྐྱོན་ཡང་རྣམ་པ་གཉིས་ཏེ། མཐོང་བའི་ཆོས་ཀྱི་དང་། དེ་ལས་སྐྱེ་པ་གཞན་པའོ། །

[Block 3183]
དེ་ལ༌[^2010]མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་ནས་ཚིགས་བཅད་བཅུ་གསུམ་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ཀྱི་སྐྱོན་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། བྱ་བ་མི་འཕེལ་བའི་སྐྱོན་ཤི་བ་ལྟར་གྱུར་པ་དང་། བྱ་བ་མ་ཡིན་པ་ལ་འཇུག་པ་མྱོས་པ་ལྟར་གྱུར་པའོ། །

[Block 3184]
དེ་ལ་བྱ་བ་མི་འཕེལ་བའི་སྐྱོན་གྱི་དབང་དུ་བྱས་པའི་གོ་རིམས་མདོར་བསྟན་པ་ནི་ཚིགས་བཅད་གཅིག་གོ། །

[Block 3185]
འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་པའི་གོ་རིམས་མདོར་བསྟན་པ་ཡང་ཚིགས་བཅད་གཅིག་གོ། །

[Block 3186]
དེ་ལ་བྱ་བ་མི་འཕེལ་བའི་དབང་དུ་བྱས་པའི་ཚིགས་བཅད་བདུན་པོ་རྣམས་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། སློབ་དཔོན་བཙུན་པ་གཞན་ལ་ཕན་པའི༌[^2011]དབྱངས་ཀྱིས་མདོ་སྡེ་རྒྱན་གྱི་ནང་དུ་ཆང་འཐུང་བའི་ཉེས་པའི་དབང་དུ་བྱས་ནས་གསུངས་ཏེ། དེ་ནི་ཚིགས་བཅད་འདི་དག་བསྡུས་པའི་དོན་ཡིན་ཏེ། ཇི་སྐད་དུ། གང་ཞིག༌[^2012]འཐུངས་པས་ལུས་རྙོག་དྲན་འཕྲོག༌[^2013]ཚུལ་ལས་འདའ་བ་དང་། ། བློ་རྨོངས་ངོ་ཚའི་ཆོས་གཅོད་འདུ་ཤེས་ཉམས་ཤིང་རིགས་བསླད་འགྱུར། །དགའ་མཆོག་ཉམས་ཤིང༌[^2014]ཞེ་སྡང་སྐྱེད་པར་བྱེད་པ་གང་ཞིག་གིས། །འཐུངས་ན་མྱོས་པར་འགྱུར་ཞིང་དྲན་ཉམས་དེ་ནི་འཆི་བཞིན་གནས། །ཞེས་བཤད་དོ། །

[Block 3187]
དེ་བས་ན་ཚིགས་བཅད་འདིའི་གོ་རིམས་ཀྱིས་མཚོན་པ་འདིས་ནི། གང་ཞིག་འཐུངས་ན་ར་རོ་བློང་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དག་གི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 3188]
ལུས་རྙོག་ཅེས་བྱ་བ་དང་། དྲན་པ་འཕྲོག་པ་དང་། ཚུལ་ལས་འདའ་བ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་འཆི་བར་གྱུར༌[^2015]ན་ཡོན་ཏན་འདི་དག་ཉམས་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་ཆང་འདི་འཐུངས༌[^2016]ན་ཡང་ར་རོ་བློང་ནས་གོམ་པ་དབང་མེད་འདོར་ཞིང་འགྲོ་བ་དང་། ཡུལ་ཕྱོགས་མ་འདྲིས་པར་ཡང་འཁྱམ་ཞིང་རྡེག་འཆོས་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིར་ནི་སྔར་བསྟན་པའི་ལུས་རྙོག་ཅེས༌[^2017]བྱ་བ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 3189]
དྲན་པ་ཉམས་པ་ཞེས་བྱ་བ་འདིས་ནི་གོང་དུ་བསྟན་པའི་དྲན་པ་འཕྲོག་ཅིང་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 3190]
བཟའ་དང་མི་བཟའི༌[^2018]དཔྱད་པ་མེད་པར་དེ་དང་དེ་དག་ཟར་འགྱུར་བ། །ཞེས་བྱ་བ་འདིས་ནི་གང་གོང་དུ་བསྟན་པའི་ཚུལ་ལས་འདའ་བ་ཞེས་བྱ་བ་དེ་སྟོན་ཏོ། །
--- END BLOCKS ---
