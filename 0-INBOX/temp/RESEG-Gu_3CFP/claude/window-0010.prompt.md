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
[Block 351]
ཐ་མ་ནི་ཇི་སྙེད་ཡོད་པའི་མཚན༌[^199]ཉིད་དོ། །

[Block 352]
ཡུན་རིང་པོ༌[^200]ཞེས་བྱ་བ་ནི། སྦྱོར་བ་དེ་ཇི་སྙེད་པས་རྒྱུན་མི་འཆད་པར་གྲིམས་པར་བྱེད་པ་དག་གོ། །

[Block 353]
ཇི་ལྟར་འབྱུང་བར༌[^201]སྦྱོར་བས་ནི་བག་མེད་པ་རྣམས་ཡང་དག་པར་ལེན་དུ་གཞུག་པའི་ཕྱིར་བསྔགས་པ་བརྗོད་པ་ཉིད་དོ། །

[Block 354]
ཡང་དག་པར་བླངས་པ་རྣམས་ལ་ཡང་ཞེས་བྱ་བ་ལ། ཡང་དག་པར་ཞུགས་པ་དང་། ཞུམ་པ་རྣམས་ངེས་པར་གཞུག་པ་དང་། རབ་ཏུ་དགོད༌[^202]པའོ། །

[Block 355]
སྦྱོར་བ་འདིའི་བསྡུས་པའི་དོན་ནི། རྣམ་པ་ཇི་ལྟ་བུས་དང་། གང་ལ་སྦྱོར་བས་སོ། །

[Block 356]
ཡང་རྟག་པའི་སྦྱོར་བ་དེའི་འབྲས་བུ་ལ་གནས་པ་ཉིད་ནི་ཞིང་དག་པར་རིག་པར་བྱ་སྟེ། ཞིང་དང་འདྲ་བས་ཞིང་ཞེས་བྱ་བ་ལ། འབྲས་བུ་འབྱིན་པར་འདྲ་བར༌[^203]ཆོས་ནི་དེ་དག་པ་སྟེ། འབྲས་བུ་ལ་གནས་པའོ། །

[Block 357]
བདག་གི་དོན་དང་གཞན་གྱི་དོན་ལས་བརྩམས་ནས་ཞེས་བྱ་བ་ལ། བདག་གི་དོན་ལས་བརྩམས་པ་ནི་ཡུན་རིང་པོར་དགེ་བའི་ཕྱོགས་ལ་སྦྱོར་བ་ཞེས་བྱ་བའོ། །

[Block 358]
གཞན་གྱི་དོན་ལས་བརྩམས་པ་ནི། དགེ་བའི་རྩ་བ་མང་པོ་སོགས་པར༌[^204]བྱེད་པ་ཞེས་བྱ་བའོ། །

[Block 359]
ཡང་ན་རང་གི་དོན་ལ་ཡང་ཡུན་རིང་པོར་དགེ་བའི་ཕྱོགས་ལ་སྦྱོར་བ་དང་། དགེ་བའི་རྩ་བ༌[^205]སོགས་པ་ཡིན་ལ། དེ་བཞིན་དུ་གཞན་གྱི་དོན་ལ་ཡང༌[^206]སྦྱོར་བར་བྱ་སྟེ། སྦྱོར་བར༌[^207]བྱས་ནས་མཇུག་གི་དུས་སུ་སོགས་པར་བྱེད་པའོ། །

[Block 360]
ཁ་དོག་ཕུན་སུམ་ཚོགས་པར་གྱུར༌[^208]ན་ཞེས་བྱ་བ་ནི། སྔར་བསྟན་པའི་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་ཉིད་དང་།[^209] གཟུགས་བཟང་བ་ཉིད་དང་། བལྟ་ན་སྡུག་པ་ཉིད་དང་། མཛེས་པ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 361]
དེ་ལ་གཟུགས་བཟང་བའི་མཚན་ཉིད་ཀྱི་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་ནི་སྐྱེ་བོའི་ཚོགས་ཆེན་པོའི༌[^210]སྙིང་དུ་སྡུག་པར་འགྱུར་རོ། །

[Block 362]
སྙིང་དུ་སྡུག་པར་གྱུར་ན་དྲུང་དུ་འདུ་བར་འགྱུར་རོ། །

[Block 363]
དེ་ནས༌[^211]ཡིད་དུ་འོང་བ་ཞེས་བྱ་བ་རབ་ཏུ་མཛེས་པ་ཉིད་ཀྱིས་མངོན་སུམ༌[^212]དུ་ཕྲད་དུ་འོང་བར་འགྱུར་བས་བལྟ༌[^213]ན་སྡུག་པ་ཉིད་དོ། །

[Block 364]
སྐྱེ་བོའི་ཚོགས་ཆེན་པོ་དག་དེའི་ཚིག་མཉན་པ་དང་བྱ་བར་སེམས་ཏེ་ཞེས་བྱ་བ་ནི། མངོན་དུ་བསྒྲུབ་པར༌[^214]བྱའོ་སྙམ་དུ་སེམས་པའོ། །

[Block 365]
སྐྱེ་བོའི་ཚོགས་ཀུན་གྱིས་བཀུར་བ་དང་ཞེས་བྱ་བ་ནི། ཡིད་ཀྱིས་སོ། །

[Block 366]
མཆོད་པ་ནི་ལུས་ཀྱིས་སོ། །

[Block 367]
བསྔགས་པ་ནི་ངག་གིས་ཏེ། ང་རྒྱལ་མེད་པའི་སེམས་ཀྱི༌[^215]ཡོན་ཏན་དང་ལྡན་པ་དང་། བླ་མ་ལ་ལུས༌[^216]དང་ཡིད༌[^217]དང་ངག་གི་ལས་ཀྱིས་དེ་བྱ་བའི་དུས་སུ་མཆོད་པ་བྱེད་པ་ཉིད་ཀྱིས་སོ། །

[Block 368]
འདོད་པ་ལ་བྱིན་པས་གང་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པར་གྱུར་པས་ནི། སེམས་ཅན་རྣམས་སྡུད་པར་བྱེད་དོ། །

[Block 369]
ཡོ་བྱད་ཀྱིས་ཕོངས་པ་ལ་བྱིན་པས་གང་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པར་གྱུར་ན། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ། །

[Block 370]
ཚིག་རྩུབ་པོ་མེད་པའི་རྒྱུས་ཚིག་བཙུན་པ་ཉིད་དུ་གྱུར་ན་སྙན་པར་སྨྲ་བ་ཉིད་པས༌[^218]སེམས་ཅན་རྣམས་སྡུད་དོ། །

[Block 371]
བདེན་པར་སྨྲ་བའི་རྒྱུ་ཉིད་ཀྱི༌[^219]དོན་སྤྱོད་པས་སེམས་ཅན་རྣམས་རྗེས་སུ་འཛིན་ཏོ། །

[Block 372]
ཕྲ་མ་མེད་པ་དང་། འཁྱལ་པ་མེད་པར་སྨྲ་བས་སེམས་ཅན་རྣམས་སྡུད་ཅིང་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ། །

[Block 373]
ཡང་ན་སྙན་པར་སྨྲ་བས་ནི་སེམས་ཅན་རྣམས་སྡུད་པར་བྱེད་ལ། དོན་སྤྱོད་པ་དང་དོན་མཐུན་པ་ཉིད་ཀྱིས་ནི་སེམས་ཅན་རྣམས་ཡོངས་སུ༌[^220]སྨིན་པར་བྱེད་དོ། །

[Block 374]
གུས་པ་དང་ཞེས་བྱ་བ་ནི། གང་གིས་འདི་འཇིག་རྟེན་ལ་གྲགས་པར་འགྱུར་བའོ། །

[Block 375]
བྱས་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་གང་གིས༌[^221]འཇིག་རྟེན་ན་སྙན་པར་གྲགས་པར་འགྱུར་བའོ། །

[Block 376]
བཀུར་སྟི་དང་གུས་པ་དང་བཅས་པས་ཞེས་བྱ་བ་ནི། དེ་དག་ཉིད་ཀྱིས་སོ། །

[Block 377]
བྱང་ཆུབ་སེམས་དཔའ་སྐྱེས་པར་གྱུར་ན་ཞེས་བྱ་བ་ལ། སྐྱེས་པའི་དངོས་པོ་ལ་མངོན་པར་དགའ་ཞིང་བུད་མེད་ཀྱི་དངོས་པོ་ལ་མི་དགའ་བ་དག་གིས་སོ། །

[Block 378]
ཕོའི་དབང་པོ་དང་ལྡན་པས་ཞེས་བྱ་བ་ལ། གཞན་དག་ལ་སྐྱེས་པ་ཉིད་བསྒྲུབས་པས་སྐྱེས་པར་གྱུར་པ་ཉིད་ཡོན་ཏན་ཐམས་ཅད་དང་། བཙལ་བ༌[^222]ཐམས་ཅད་དང་། ཤེས་བྱ་ཐམས་ཅད་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་དག་གི་སྣོད་དུ་གྱུར་པ་ལྟར་བུད་མེད་ནི་དེ་ལྟ་བུ༌[^223]མ་ཡིན་ཏེ། སྐྱེས་པའི་དབང་པོ་དང་ལྡན་པའི་ཕྱིར་འཇིགས་པ་མེད་པར་འགྱུར་བ་དང་འཇུག་པ་ལ་སྒྲིབ་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 379]
སེམས་ཅན་རྣམས་ལ༌[^224]ཞལ་ཏ་བྱེད་པའི་རྒྱུས་སྟོབས་དང་ལྡན་པས་སྐྱོ་བ་མེད་པར་འགྱུར་ཏེ། དགེ་བའི་ཆོས་སྒྲུབ་པའི་བྱ་བ་ལ་གྲོགས་བྱེད་པའི་རྒྱུ་ཉིད་ཀྱི་སྟོབས་ཀྱིས་སེམས་ཅན་རྣམས༌[^225]ལ་ཕན་གདགས་པའི་སྦྱོར་བས་མི་སྐྱོ་བར་འགྱུར་རོ། །

[Block 380]
ལས་དོན་ཆེ་ཞེས་བྱ་བ་ནི་མང་བའོ། །

[Block 381]
མཐུན་པ་ཞེས་བྱ་བ་ནི་འཚམ་ཞིང་རྗེས་སུ་མཐུན་པའོ། །

[Block 382]
བདག་ཉིད་སངས་རྒྱས་ཀྱི༌[^226]ཆོས་རྣམས་ལ་ཡོངས་སུ་སྨིན་པར་བྱེད་ལ་ཞེས་བྱ་བ་ནི། ཡོངས་སུ་སྨིན་ན༌[^227]བདག་ཉིད་བླ་ན་མེད་པ༌[^228]ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱའོ། །

[Block 383]
སེམས་ཅན་རྣམས་ཀྱང་ཐེག་པ་གསུམ་ལ་མྱུར་བ་ཉིད་དུ་ཡོངས་སུ་སྨིན་པར་བྱེད་ལ་ཞེས་བྱ་བ་ནི། སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པ་ཉིད་ནི༌[^229]རྣམ་པར་གྲོལ་བར་བྱེད་དོ། །

[Block 384]
བྱམས་པ་ལ་སོགས་པ་ཚད་མེད་པ་རྣམས་བསྒོམས་པའམ༌[^230]ཞེས་བྱ་བ་ནི། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྒོམ་པའི་ཕྱོགས་ཀྱི༌[^231]བརྩོན་འགྲུས་སོ། །

[Block 385]
རབ་ཏུ་འབྱེད་ཅིང་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཕྱོགས་ཀྱིའོ། །

[Block 386]
དེ་ལྟ་བུའི་བསོད་ནམས་དང་ཡེ་ཤེས་དེ་ཡང་མདོར་བསྡུ་ན་རྣམ་པ་དྲུག་ཏུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་མཚན་ཉིད་དོ། །

[Block 387]
ཡང་ན་བསོད་ནམས་དང་བསོད་ནམས་ཀྱི་ཕྱོགས་དང་། བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་། ཡེ་ཤེས་དང་ཡེ་ཤེས་ཀྱི་ཕྱོགས་དང་། བརྩོན་འགྲུས་དང་བསམ་གཏན་ཞེས་བྱ་བའོ། །

[Block 388]
བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་འབྲས་བུ་ནི་མདོར་བསྡུ་ན་ཅི་རིགས་པར་རྣམ་པ་བཞིར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། བསོད་ནམས་ཀྱི་འབྲས་བུ་རྣམ་པ་གཉིས་ནི་གནོད་པ་མེད་པར་འཁོར་བ་ན་འཁོར་ཞིང་སྡུག་བསྔལ་པ་དག་གིས་ཤིན་ཏུ་གཟིར་བ་མེད་པ་དང་། ཇི་ལྟར་དགའ་བར་སེམས་ཅན་གྱི་དོན་དང་ཕན་འདོགས་པར་ནུས་པ་ཞེས་བྱ་བའོ། །

[Block 389]
ཡེ་ཤེས་ཀྱི་འབྲས་བུ་རྣམ་པ་གཉིས་ནི་ཡེ་ཤེས་ལ་བརྟེན་ནས་ཡང་དག་པར་བསོད་ནམས་ཡོངས་སུ་འཛིན་པ་དང་། མཁས་པར་བྱ་བ་རྣམ་པ་སྣ་ཚོགས་དཔག་ཏུ་མེད་པ་དག་གིས་ཀྱང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བའི་བར་དུའོ། །

[Block 390]
གང་རྣམ་པར་སྨིན་པ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་བསོད་ནམས་ལ་བརྟེན་པའོ། །
--- END BLOCKS ---
