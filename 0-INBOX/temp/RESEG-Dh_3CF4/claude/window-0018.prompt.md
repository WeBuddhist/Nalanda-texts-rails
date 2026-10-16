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
སྦྱིན་པའི་དངོས་པོ་ལ་ཆགས་པའམ། བདག་ཉིད་ལ་ཆགས་ཤིང་ཉམས་པས་འཇིགས་པའམ། ཕོངས་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་ཡལ་བར་འདོར་བས་ནི་ཁས་བླངས་པའི་དངོས་པོ་སྦྱོར་བར་མི་འདོད་པ་ཡིན་ཏེ། སྦྱིན་པའི་དངོས་པོ་ལ་ཆགས་པ་དེ་ཉིད་མི་རིགས་པའི་དབང་དུ་བྱས་ནས། གང་གིས་སྦྱིན་ཞེས་སྨྲས་ན་ནི། ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཡིན་ཏེ། སྐྱེ་བོ་རྣམས་ནི་སྦྱིན་པའི་དངོས་པོ་ལ༌[^333]ཆགས་ཤིང་འདོད་པ་ཡིན་པས་སོ། །

[Block 632]
འདོད་པ་གང་ཞེ་ན་སྦྱིན་པ་དང་འགལ་བའི་སེམས་ཀྱིས་ཀུན་ཏུ་འཛིན་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 633]
བདག་ལ་ཆགས་ཤིང་ཉམས་པས་འཇིགས་པའི་དབང་དུ་བྱས་ནས་སྦྱིན་ནོ་ཞེས་ནི་ཁས་བླངས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་ཡིན་ཏེ། གང་ཞིག་ཡིད་ལ་གཞན་སེམས་པ། །ཞེས་བྱ་བ་ནི་མི་སྦྱིན་པར་ཡིད་ལ་སེམས་པའོ། །

[Block 634]
སེར་སྣས་མ་ངེས་བློ་ཅན་ཏེ། །ཞེས་བྱ་བ་ནི་སེར་སྣས་བདག་ཉིད་ལ་ཆགས་ཤིང་སྦྱིན་པ་དང་མི་མཐུན་པ་ཡོད་པས་སོ།[^334] །སེར་སྣས་མ་ངེས་པའི་བློ་གང་ཡིན་པ་དེ་ནི། སེར་སྣས་མ་ངེས་པའི་བློ་ཅན་ཏེའོ། །

[Block 635]
མ་ངེས་པར་གྱུར་པ་དེ་ནི་ཕྱིས་མི་སྦྱིན་པའི་སེམས་ཡིན་ནོ་ཞེས་རྗེས་སུ་ཤེས་པའོ།[^335] ། ཕོངས་པའི་སྐྱེ་བོ་ཡལ་བར་དོར་བའི་དབང་དུ་བྱས་ནས་སྦྱོར་བ། སྦྱིན་ནོ་ཞེས་ནི་ཁས་བླངས་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 636]
བརྟན་པར་བྱས་ནས་ཞེས་བྱ་བ་ནི་ཅི་ནས་ཀྱང་སྦྱིན་པར༌[^336]བྱའོ་ཞེས་ཁས་བླངས་ནས་སོ། །

[Block 637]
སླུ་བའི་ཚིག་ནི་རྩུབ་པོ་ཡིས། །ཞེས་བྱ་བའི་ཚིག་གིས་ཕོངས་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་ཡལ་བར་དོར་བའམ་གཞག་པ་དེའི་ཚིག་སྨྲ་བར་མི་ནུས་པ་ཡང་ཡིན་ཏེ།

[Block 638 [VERSE]]
ཚིག་ནི་ངག་གི་སྦྱོར་བའོ། །
སྐྱིན་བསབ་པ་ནི་ཅི་ཡང་མེད། །

[Block 639]
ཅེས་བྱ་བ་ནི་ཤིན་ཏུ་སྡིག་ཆེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 640]
དེ་ལ་དེ་ཉིད་ངེས་པར་གཟུང་བས་བསྟན་པ་ནི་གཞན་གྱི་མིག་གིས༌[^337]གཞན་ལ་ཇི་ལྟར་སྦྱར་དུ་རུང་ཞེས་བྱ་བ་དེའི་ལན་འདིས་བསྟན་པ་ཡིན་ཏེ། རྒྱུ་གཅིག་གིས་ནི་གྲུབ་པ་ཡི། །ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། རྐྱེན་གཅིག་གིས་བསྐྱེད་པ་ནི་ཅི་ཡང་མེད་པའི་ཕྱིར་རྒྱུ་རྐྱེན་གཞན་ལ་མ་ལྟོས་པའི༌[^338]མིག་ནི་མེད་དོ། །

[Block 641]
རྒྱུ་རྐྱེན་གཞན་ལ་ལྟོས་པ༌[^339]ནི་ལྷ་རྣམས་ཀྱིས་བྱས་པའི་མིག་ཉིད་ཀྱང་སྦྱིན་པར་བྱ་བ་དང་། རྒྱུ་རྐྱེན་གཞན་ལ་ལྟོས་པར༌[^340]འགྱུར་བ་ཡིན་ནོ། །

[Block 642]
སྦྱིན་པ་ཆེན་པོ་ལ་བགེགས་བྱ་བ་ཞེས་བྱ་བ་ནི་ནང་གི་སྦྱིན་པ་ནི་སྦྱིན་པ་ཆེན་པོ་སྟེ། ཕྱི་རོལ་ལས་ཁྱད་པར་དུ་གྱུར་པ་ཡིན་ནོ། །

[Block 643]
གང་གི་ཕྱིར་ནང་གི་སྦྱིན་པ་ནི་ཤིན་ཏུ་དཀའ་བ་ཡིན་པས་དེ་དག་དང་མ་འདྲེས་པའོ། །

[Block 644]
སྦྱིན་པའི་བགེགས་བྱེད་པས་མི་ཚུགས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 645]
དོགས་པ་སྐྱེད་པའི་མཚན་ཉིད་ཐ་མི་དད་ཅིང་སྦྱིན་པའི་བྱེ་བྲག་མིག་སྦྱིན་པ་དགག་པའི་ཕྱིར་ཡང་སྨྲས་པ། ལྷ་ནོར་དང་འབྲུ་དང་རིན་པོ་ཆེ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་དག་སྦྱིན་པ་བགེགས་བྱས་པར་གྱུར་ན་དེའི་ཚེ་བགེགས་བྱེད་པ་ཡིན་ན། དེ་ལྟ་ནི་མ་ཡིན་གྱི་བདག་ཉིད་སྦྱིན་པ་ཉེས་པར༌[^341]འགྱུར་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 646]
གང་ཞིག་སློང་བ་དེ་ནི་སྦྱིན་པར་བྱ། །ཞེས་པའི་ཚིགས་བཅད་འདི་ལྟ་སྟེ། གཞན་ཡང་དེ་རྣམས་ཀྱི་སྦྱིན་པའི་བགེགས་ཀྱི་ཉེས་པར་བསྒྲུབས་པའི་ཕྱིར། གང་ཞིག་སློང་བ་དེ་ནི་སྦྱིན་པར་བྱ་ཞེས་བྱ་བ་འདིས་ཏེ། གང་ལས་ཤེ་ན། སློང་བ་དེ་ཉིད་ཐོབ་ཅིང་སློངས༌[^342]ནས་ནི་དགའ་བར་གྱུར་པ༌[^343]ཡིན་ཏེ། སྦྱིན་པ་ལེན་པ་པོ༌[^344]དགའ་བར་འགྱུར་བའི་དོན་ཡིན་ནོ། །

[Block 647]
དེ་ལྟར་རང་གི་མིག་སྦྱིན་པ་རིགས་པར་བསྟན་ནས་ནོར་དང་འབྲུ་ལ་སོགས་པ་གཞན་ནི་དེ་ལ་བྱིན་ཡང་སྦྱིན་པ་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར། མི་འདོད་པ་ནི་བྱིན་ཡང་དགར་མི་འགྱུར། །ཞེས་བྱ་བ་སྟེ། འདི་ནི་མི་མཐུན་པའི་སྦྱིན་པས་དགའ་བར་མི་འགྱུར་བ་བསྟན་པའི་ཕྱིར་བཤད་དེ། འདིས་ནི་དགེ་བ་སྐྱེ་བའི་མཐུས་མི་མཐུན་པ་དང་ལྡོག་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 648]
མི་སློང་བ་དང་མི་འདོད་པ་སྦྱིན་པ་ནི༌[^345]མི་མཐུན་ཅིང་དགོས་པ་མེད་པའི་ཕྱོགས་ཡིན་ཏེ། ཇི་ལྟ་བུ་ཞེ་ན། དཔེས་བསྟན་པའི་ཕྱིར། ཆུས༌[^346]ཁྱེར་བ་ལ་ཆུ་ཡིས་ཅི་ཞིག་བྱ། །ཞེས་པ་ཡིན་ཏེ། ཆོས་མཐུན་པའི་དཔེའོ། །

[Block 649]
སྐོམ་པ་ལ་ཆུའི་སྦྱིན༌[^347]པ་དང་འདྲ་བར་བསླངས་པའི་དོན་ནི་འདི་ལ་སྦྱིན་ཞེས་བྱ་བ་སྨོས་ཏེ། བླངས་པ༌[^348]དེ་ཉིད་སྦྱིན་ན་སྐྱེ་བོ་དགའ་བ་ཀུན་ཏུ་འཛིན་ཅིང་དགའ་བ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 650]
དེ་ནས་རྒྱལ་པོ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་འདིའི་བསྡུས་པའི་དོན་ནི་གང་སྨྲ་བ་དང་གང་གི་ཕྱིར་སྨྲ་བ་དང་། ཇི་ལྟར་སྨྲ་བ་དང་། གང་ལ་སྨྲ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་དག་སྟེ། ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 651]
ལ་ལས༌[^349]དཀའ་ཐུབ་ཏིང་འཛིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་རྒྱལ་སྲིད་ཐོབ་པའི་རྒྱུ་དང་། འབྲས་བུ་དང་ངོ་བོ་ཉིད་ཀྱི་ཁྱད་པར་ཡིན་ཏེ། རྟག་ཏུ་བྱེད་པ་དང་ཡུན་མི་ཐུང་བས་དེའི་དཀའ་ཐུབ་ཆེན་པོའོ། །

[Block 652]
དཀའ་ཐུབ་ཏིང་འཛིན༌[^350]ཆེན་པོ་ཞེས་བྱ་བ་ནི་དཀའ་ཐུབ་ཉིད་ཏིང་འཛིན༌[^351]ཡིན་པས་དཀའ་ཐུབ་ཏིང་ངེ་འཛིན་ནོ། །

[Block 653]
གང་དུ་རྒྱུ་སྦྱིན་པ་དང་། ཡང་དག་པར་སྡོམ་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཡོད་པ་དེ་ནི་དཀའ་ཐུབ་ཏིང་འཛིན༌[^352]ཆོ་ག་ཞེས་བྱའོ། །

[Block 654]
གུས་པར་བྱེད་པའི་རྒྱུས་ཆོ་ག་ཞེས༌[^353]བྱ་སྟེ། ཆོ་ག་ཉམས་ན་ནི་གང་གིས་ཀྱང་ངམ། ཐམས་ཅད་ཀྱིས་ལུས་ཉོན་མོངས་པར་བྱས་ཏེ་རྟག་ཏུ་དཀའ་ཐུབ་དང་ཐོས་པ༌[^354]ལ་བརྟེན་ཀྱང་། གུས་པར་སྦྱོར་བའི་ཆོ་ག་ཉམས་ན་མི་ཐོབ་པོ། །འདིས་ནི་རྒྱལ་སྲིད་ཐོབ་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 655]
མང་པོ་ཇི་ལྟར་བསྟན་པའི༌[^355]མཆོད་སྦྱིན་བརྒྱ་ཕྲག་ཡིན་ཏེ། འདིས་ནི་ཇི་སྲིད་དུ་བསྟེན་པར་བྱས་པའོ། །

[Block 656]
གྲགས་པ་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་སྟེ། མཐོ་རིས་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་ལོ། །

[Block 657]
དེ་ལྟར་ཇི་ལྟར་བསྟེན་པ་སྟེ་རྟག་ཏུ་བསྟེན་པ་དང་གུས་པར་བྱ་བའི་སྦྱོར་བའི་མཆོད་སྦྱིན་ཆེན་པོ་མང་པོས་འབྲས་བུ་ཅི་ཞིག་ཐོབ་ཅེ་ན། སྨྲས་པ། མཐོང་བའི་ཆོས་ལ་ནི་གྲགས་པའོ། །

[Block 658]
འཇིག་རྟེན་ཕ་རོལ་གྱི་འབྲས་བུ་ནི་མཐོ་རིས་སོ། །

[Block 659]
འདིས་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 660]
བརྒྱ་བྱིན་དང་འགྲན་པའི་ལོངས་སྤྱོད་ཅེས་བྱ་བས་ནི་རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 661]
ཅི་ཞིག་མཐོང་ན་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 662]
ཅི་ཞིག་མཐོང་ནས་མིག་སྦྱིན་ཞེས་བྱ་བའི་དོན་ཏེ། གང་སྦྱིན་པ་དེ་ཐམས་ཅད་འབད་པ་མེད་པར་ཡོད་དོ། །ཞེས་པའོ། །

[Block 663]
ཆོ་ག་འདི་ནི་སུ་ལས་ལོབས་ཞེས་བྱ་བ་ནི་ཆོ་ག་འདི་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཡང་དག་པར་འཐོབ་ཅེས་བྱ་བའི་ལུང་ངོ་། །སུ་ལས་ལོབས་ཞེས་བྱ་བ་ནི་གང་གིས་བསྟན་ཅེས་བྱ་བའི་ཚིག་སྟེ། ཅི་ཞིག་མཐོང་ནས༌[^356]ཁྱོད་ཀྱིས༌[^357]མིག་སྦྱིན་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 664]
གང་གི༌[^358]དོན་དུ་སྦྱིན་པ་དེ་ཐམས་ཅད་ཀྱང་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར་སྨྲས་པ།

[Block 665 [VERSE]]
མཆོད་སྦྱིན་བྱས་པས་སུམ་ཅུ་རྩ་གསུམ་ཉེ། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ཡིན་ནོ། །
དེའི་ཕྱིར་རྒྱུ་ནི་སྔར་བྱས་ཟིན་པས་སོ། །

[Block 666]
ཇི་ལྟ་བུ་ཞེ་ན། མཆོད་སྦྱིན་བྱས་པས་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 667]
གལ་ཏེ་འཇིག་རྟེན་འདིའི་འབྲས་བུ་གྲགས་པ་དང་། ཚིག་བཙུན་པོ་འདོད་ན་ནི་དེ་གཉི་ག་ཡང་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར།

[Block 668 [VERSE]]
གྲགས་པས་ཀུན་ཏུ་རབ་ཏུ་གསལ་གྱུར་ཅིང་། །
མི་དབང་གཙུག་གི༌[^359]འོད་ཀྱིས་རྐང་བརྒྱན་པ། །
ཞེས་བྱ་བ་སྟེ་གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །
ཅི་ཞིག་འདོད་ཕྱིར་མིག་ནི་སྦྱིན་པར་བྱེད། །

[Block 669]
ཅེས་བྱ་བ་ནི་གང་གི༌[^360]དོན་དུ་བསྟན་པ་དེ་ཅི་ཞིག་མཐོང་ན། ཁྱོད་ཀྱིས་མིག་སྦྱིན་ཞེས་བྱ་བ་སྟེ། དེ་ཉིད་འདིར་ཡང་བསྟན་པ་ཡིན་ནོ། །

[Block 670]
ས་ཀུན་འཐོབ་ཕྱིར་དང་མཐོ་རིས་དང་ཐར་པ་སྟེ་འཇིག་རྟེན་ཕ་རོལ༌[^361]གྱི་འབྲས་བུའོ། །
--- END BLOCKS ---
