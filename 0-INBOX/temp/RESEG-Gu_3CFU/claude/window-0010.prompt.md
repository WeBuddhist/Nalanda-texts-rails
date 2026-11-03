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
དེ་དག་འཛིན་དུ་འཇུག་ནུས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་རྣམས་མངོན་པར་མི་ཤེས་པ་ལ་དེ་རྣམས་ལ༌[^240]འཛིན་དུ་འཇུག་ཅིང་གོ་བར་བྱེད་ནུས་པ་ཡིན་ནོ། །

[Block 352]
དེ་བས་ན་སྡེ་སྣོད་མངོན་པར་ཤེས་པའི་ཚིག་འདི་ཁྱད་པར་ཉིད་ལ་རིག་པར་བྱའོ། །

[Block 353]
ལྷག་པའི་ཚུལ་ཁྲིམས་དང་སེམས་དང་ཤེས་རབ་ལ་སློབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། སློབ་པའི་དངོས་པོ་ནི་སློབ་པ་ཉིད་དེ་གཉིས་ལྡན་གྱིས་གཅིག་དང་ལྡན་པའི་དངོས་པོའོ། །

[Block 354]
ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱི་ཚིག་གིས་འདུལ་བའི་ལུགས་ཐམས་ཅད་གཟུང་བ་ཡིན་ནོ། །

[Block 355]
ལྷག་པའི་སེམས་ཀྱི་ཚིག་གིས་ནི་བསམ་གཏན་རྣམས་སོ།[^241] །ལྷག་པའི་ཤེས་རབ་ཀྱི་ཚིག་གིས་ནི་བདེན་པ་མཐོང་བའི་གོམས་པ་ལའོ། །

[Block 356]
སློབ་ཏུ་འཇུག་ཀྱང་ནུས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལྷག་པའི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཡིད་ཆེས་པ༌[^242]བསྐྱེད་པའི་དོན་དུ་ཀྱང་གི་སྒྲ་བྱས་པ་ཡིན་གྱི་ཐ་དད་པ་རྟོག་པའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 357]
ལྷག་པའི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ལ་མི་སློབ་ཅིང་དེས༌[^243]སློབ་པ་ལ་སྟོབས་དང་ལྡན་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 358]
སློབ་པ་ཞེས་བྱ་བའི་ཚིག་གིས་འདི་བྱེ་བྲག་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 359]
ལྷག་པའི་སྤྱོད་པ་དང་འདུལ་བ་དང་སོ་སོར་ཐར་པ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་ནོ་ཞེས་བྱ་བ་འདིས་སློབ་པ་ཉིད་ལ་འཇུག་ནུས་པ་ཉིད་དམ་སློབ་ཏུ་འཇུག་པ་ལ་ཞེས་བྱ་བ་འདི་གཟུང་བའོ། །

[Block 360]
དེ་བས་ན་ལྷན་ཅིག་སྦྱར་བ་འདི་དག་གཉིས་སུ་གྱུར་པ་ཡིན་ཏེ། དེ་ལ་ལྷག་པའི་སྤྱོད་པ་ནི་རིག་པར་སྤྱོད་པ་ཅན་ནོ། །

[Block 361]
འདུལ་བ་ནི་ལྷག་པར་གྱུར་པའོ། །

[Block 362]
སོ་སོར་ཐར་པའི་བསླབ་པ་རྣམས་དང་། གཞིའི་ཆོ་ག་རྣམས་ཡན་ལག་དང་བཅས་པ་ནི། སོ་སོར་ཐར་པ་སྟེ། དེ་ཞེས་བྱ་བ་ནི་མདོར་གཏོགས་པའི་བསླབ་པའི་གཞི་རྣམས་སོ། །

[Block 363]
དད་པ་དང་ཚུལ་ཁྲིམས་དང་ཐོས་པ་དང་གཏོང་བ་དང་ཤེས་རབ་ཕུན་སུམ་ཚོགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ཚུལ་ཁྲིམས་ཀྱི་ཚིག་གིས་ནི་འདིར་འདུལ་བ་བཟུང་བ་ཡིན་ནོ། །

[Block 364]
ཚུལ་ཁྲིམས་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་དང་རྣམ་པར་གྲོལ་བ་དང་དེ་ཤེས་པ་དང་མཐོང་བ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཕུན་སུམ་ཚོགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 365]
ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པའི་ཚིག་གིས་འདིར་འདུལ་བ་གྲགས་པ་ཉིད་ཡིན་གྱི༌[^244]གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 366]
དགེ་སློང་གི་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ལ་ཡང་དག་པར་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 367]
དེ་ཤེས་པ་ཞེས་བྱ་བ་ལ་དེའི་སྒྲས་ནི་རྣམ་པར་གྲོལ་བ༌[^245]བཟུང་བ་ཡིན་ཏེ། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བ་ཞེས་བྱ་བའོ། །

[Block 368]
བརྩོན་འགྲུས་བརྩམས་པ་ཉིད་དང་ཤེས་རབ་དང་ལྡན་པ་ཉིད་དང་ཡང་སྦྱར་རོ་ཞེས་བྱ་བ་ནི་སློབ་པ་ཉིད་ཡན་ཆད་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་ཡང་གི་སྒྲས་ནི་སོ་སོར་ཉེ་བར་གནས་པ་འདིའི་འོག་ཏུ་སློབ་པ་ཉིད་ཡན་ཆད་གང་ཞིག་ལྷན་ཅིག་ཏུ་གསུངས་པ་ལྔ་པ༌[^246]མ་ཡིན་པ་དེ་ནི་བརྩོན་འགྲུས་བརྩམས་པ་ཉིད་དང་ཤེས་རབ་དང་ལྡན་པ་ཉིད་དག་གིས་ལྷན་ཅིག་ཏུ་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 369]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་དག་གིས་ཀྱང་གསུམ་པོ་འདི་རེ་རེ་ལས་གྲོལ་བ་རྣམས་སོ། །

[Block 370]
དྲན་པ་དང་ལྡན་པ་ཉིད་དང་ནང་དུ་ཡང་དག་པར་བཞག་པ༌[^247]ཉིད་དང་མཉམ་པར་བཞག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་རྣམས་ལ་བཞི་པོ་འདི་ཁ་སྐོང་བ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། མང་དུ་ཐོས་པ་དང་། བརྩོན་འགྲུས་བརྩམས་པ་ཉིད་དང་། ཤེས་རབ་དང་ལྡན་པ་ཉིད་དང་། དྲན་པ་དང་ལྡན་པ་ཡིན་ཏེ། སླར་བཞི་པོ་འདི་བརྗོད་ནས་ནང་དུ་ཡང་དག་པར་བཞག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་དང་། སླར་མཉམ་པར་བཞག་པ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 371]
སློབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སློབ་པའི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་དང་ཡང་དག་པར་ལྡན་པ་ཡིན་པ་དང་། སློབ་པའི་ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་དང་། རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་དང་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 372]
མི་སློབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མི་སློབ་པའི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། གང་ཞིག་འདི་དག་ལ་ཆོས་ཉིད་དང་རྣམ་པར་ངེས་པའི་ཚུལ་ཁྲིམས་དེ་ལ་གང་ཞིག་ལེགས་པ་དང་མི་ལེགས་པ་ཉིད་ཡོངས་སུ་ཤེས་པ་དེ་ནི་རེ་ཞིག་འདི་དག་ལས་རྟོགས་པ༌[^248]འབྱུང་བ་ཡིན་ནོ། །

[Block 373]
གང་ཞིག་ལྟུང་བ་རྣམ་པར་གཞག་པ་ཡོངས་སུ་ཤེས་པ་དང་། ལྷག་མའི་འདུལ་བའི་ཆོ་ག་ལ༌[^249]ཡང་གང་ཞིག་དེ་ལ་ཡང་འདི་དག་ལོ་བཅུ་ལོན་པ་ལ་སོགས་པ་ཉིད་རང་དགར་རྣམ་པར་གནས་པ་ངེས་པར་འབད་པ་བྱས་ཞེས་བྱ་བ་འདི་ལ་ཤིན་ཏུ་འདའ་བར་མ་བྱས་པར་བྱེད་དུ་འཇུག་པ༌[^250]ཤིན་ཏུ་འདའ་བར་བྱས་པ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 374]
བྱུང་བ་དང་བཅས་པ་དང་རྗེས་སུ་བཅས་པ་དང་བཀག་པ་དང་གནང་བ་མངོན་པར་ཤེས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་ལས་འདི་བྱུང་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་བསྐྱེད་པའི་རྒྱུ་ལ་བསྐྱེད་པའི་སྒྲས་བརྗོད་དོ། །

[Block 375]
བསླབ་པའི་གཞི་རྣམ་པར་གཞག་པར་བྱེད་པ་ནི་བཅས་པའོ། །

[Block 376]
བྱས་པའི་ཚིག་གིས་ནི་འདི༌[^251]ཙམ་དང་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བ་བཤགས་པར་བྱ༌[^252]ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་གཟུང་ངོ་། །འདི་ནི་འདིར་སླར་བཀག་པ་དང་གནང་བ་མངོན་པར་ཤེས་པ་ཉིད་ཅེས་བྱ་བ་ནི་རྗེས་སུ་བཅས་པའོ། །

[Block 377]
དཔེར་ན་མཆིལ་ལྷམ་རྗེས་སུ་གནང་བས་ཀྲིག་ཀྲིག་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བྱེ་བྲག་བཀག་པའོ། །

[Block 378]
དུས་མ་ཡིན་པའི་ཁ་ཟས་བཀག་ཀྱང་ནད་པ་ལ་སྨན་པའི་ཚིག་གིས་གནང་བའོ། །

[Block 379]
ཤིན་ཏུ་ནས་ཀྱང་འདི་མི་བྱ་ཞེས་བྱ་བ་བསྒྲུབ་པ་ནི་བཀག་པའོ། །

[Block 380]
དཔེར་ན་རྩྭ༌[^253]མཆོག་གིས་ཀྱང་ཆང་མི་བཏུང་བ་དང་མི་ཚངས་པར་སྤྱོད་པ་ལ་སོགས་པ་ལའོ། །

[Block 381]
གནང་བ་མངོན་པར་ཤེས་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་སླར་བྱ་བ་གང་ཞིག་བྱེད་པ་ལ་སྐྱོན་མེད་པ་དེར་འཇུག་པ་ལ་མི་བྱེད་དམ་བྱེད་ན་འཇུག་པ་ལའོ། །

[Block 382]
དཔེར་ན་ཕས་ཀྱི་རྒོལ་བ་ཚར་གཅད་པའི༌[^254]ཕྱིར་ཕྱི་རོལ་གྱི་བསྟན་བཅོས་རྣམས་བཀླག༌[^255]པར་བྱ་ཞེས༌[^256]བྱ་བ་ལ་སོགས་པ་འདི་ལ་མི་བྱེད་པ་དང་མི་བྱེད་པ་ལ་ལྟུང་བའི་སྐྱོན་འགའ་ཡང་མེད་དེ༌[^257]ངས་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 383]
བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་ཡོངས་སུ་ཤེས་པ་འདི་ཙམ་ནི་འདུལ་བ་སོ་སོ་ལས་ཤེས་པར་བྱའོ། །

[Block 384]
འདི་ནི་འདུལ་བ་ཤེས་པ་མ་ཡིན་པ་ཉིད་གཅིག་ཏུ་ལྔ་པས་བསྟན་པ་དང་ལྟུང་བ་ལ་སོགས་པ་ལྔ་པས་ཀྱང་རིག་པར་བྱའོ། །

[Block 385]
བར་དུ་གཅོད་པ་དང་བར་དུ་གཅོད་པ་མ་ཡིན་པ་མངོན་པར་ཤེས་པ་ཉིད་དང་། སྨྲ་བ་པོ་ཉིད་དང་། རྗེས་སུ་སྟོན་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་བར་དུ་གཅོད་པ་དང་བར་དུ་གཅོད་པ་མ་ཡིན་པ་མངོན་པར་ཤེས་པ་ཉིད་དང་སྨྲ་བ་པོ༌[^258]ཉིད་དང་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 386]
གང་ཞིག་འདུལ་བ་ལ་བྱ་བ་མ་ཡིན་པ་དེ་ནི་བར་ཆད་དོ། །

[Block 387]
གང་ཞིག༌[^259]དེ་ནི་བར་ཆད་མ་ཡིན་པའོ། །

[Block 388]
དེ་དག་ལ་མངོན་པར་ཤེས་པ་ཉིད་དོ། །

[Block 389]
གཉིས་པོ་འདི་ནི་འདུལ་བ་ལ་གནས་པའི་དོན་ཉིད་བསྟན་ཏོ། །

[Block 390]
སྨྲ་བ་པོ་ཉིད་ནི་སླར་སྨྲ་བའི་ཕྱིར་དང་རྟོགས་པའི་ཕྱིར་གཉིས་པོ་འདི་ལ་མཁས་པར་འགྱུར་བའི་ནུས་པ་འམ་ལེ་ལོ་མེད་པ་ཉིད་དོ། །
--- END BLOCKS ---
