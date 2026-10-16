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
[Block 106]
[^78]དེ་དག་གི་གཞུང་ལུགས་ཀྱི༌[^79]འབྲེལ་པ་དེ་དག་ཁོ་ནར༌[^80]འབྲེལ་པའི་གཏན་ཚིགས་ནི་རྟོགས་པར་བྱེད་པ༌[^81]ཡིན་ཏེ། དེ་བསལ་བའི་ཕྱིར་འབྲེལ་པ་གཉིས་པ༌[^82]བརྗོད་དོ། །

[Block 107 [HEADING]]
### མི་དམིགས་པའི་རབ་ཏུ་དབྱེ་བ། ^3-7-0

[Block 108]
སྤྱོད་པ་པ་རྣམས་ནི་ད་ལྟར་ཐམས་ཅད་མཁྱེན་པ་ལ་སོགས་པ་མི་དམིགས་པའི་ཕྱིར། མ་འོངས་པའི་དུས་ན་ཡང་དེའི་སྒོ་ནས་དེ་མེད་པར་ཤེས་ཏེ། དེ་བསལ་བའི་ཕྱིར་མི་དམིགས་པ་བརྗོད་དོ། །

[Block 109]
རྒྱལ་དཔོག་པ་ལ་སོགས་པ་གང་དག་རང་གི་དམིགས་པ་ལ་སོགས་པ་རྒྱུ་མ་ཡིན་པ་དང་། ཁྱད་པར༌[^83]བྱེད་པ་མ་ཡིན་པ་དང་། འབྲས་བུ་མ་ཡིན་པའི་བཀག་པ་དང་། ཚིག་ལ་སོགས་པ་དངོས་པོ༌[^84]དང་བསྒྲུབ་པས༌[^85]ཀྱང་མི་འགལ་བ་བསྒྲུབ་པའི་སྒོ་ནས་ཐམས་ཅད་མཁྱེན་པ་ལ་སོགས་པ་འགོག་པར་སྨྲ་སྟེ། དེ་དག་གི་དེ་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་བསྟན་པའི་ཕྱིར་དང་། འཇིག་པ༌[^86]རྒྱུ་དང་བཅས་པར་སྨྲ་བ་འགག་པའི༌[^87]ཕྱིར། མི་དམིགས་པའི་རབ་ཏུ་དབྱེ་བ་བརྗོད་དོ། །

[Block 110]
དགག་པའི་གཏན་ཚིགས་ཀྱི་སྦྱོར་བའི་དབྱེ་བ་རྣམ་པ་མང་པོ་ཞིག་ཡོད་ཀྱང་། མེ་ལ་སོགས་པ་མེ་ཉིད་ལ་སོགས་པ་གཞན་ལས་དགག་པ་འགྲུབ་པ་མ་ཡིན་གྱི། འོན་ཀྱང་རང་བཞིན་མི་དམིགས་པ་ཁོ་ནས་ཡིན་ནོ་ཞེས་བྱ་བ༌[^88]བསྟན་པའི་ཕྱིར། ཁོངས་སུ་འདུ་བ་འཐད་པ་དང་བཅས་པ་བརྗོད་དེ། འཐད་པ་ནི་ཐམས་ཅད་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 111]
བསྐལ་པའི་ཡུལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ཕ་རོལ་པོས་རབ་ཏུ་སྦྱར་བའི་མི་དམིགས་པ་ལ་ནུས་པ་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 112 [HEADING]]
## རྗེས་སུ་དཔག་པའི་མཚན་ཉིད་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། ^4-0

[Block 113]
རྗེས་སུ་དཔག་པ་འདིའི་མཚན་ཉིད་ནི། བཅོམ་ལྡན་འདས་རྗེས་སུ་དཔག་པའི་རྟེན་གྱི་རྟགས་སྟོན་པར་མཛད་པ་ཉིད་ཀྱིས་གསུངས་ཏེ། འདི་ལ་རྟགས་ནི་བསྒྲུབ་པར་བྱ་བ་མེད་ན་ནི༌[^89]འབྱུང་བར་ངེས་པ་ཡིན་ན། རྗེས་སུ་དཔག་པའི་ཤེས་པའི་རྒྱུ་ཡིན་ཏེ། དེ་ཡང་དགེ་སློང་དག་ཀུན་དུ༌[^90]འབྱུང་བའི་ཆོས་ཅན་གང་ཅི་ཡང་རུང་བ་དེ་ཐམས་ཅད་ནི་འགོག་པའི་ཆོས་ཅན་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་བསྒྲུབ་པར་བྱ་བས། གཏན་ཚིགས་ལ་ཁྱབ་པར་སྟོན་པར་མཛད་པས། བསལ་བ༌[^91]ཁོ་ནར་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ། །

[Block 114 [HEADING]]
### རང་བཞིན་ཞེས་བྱ་བའི་གཏན་ཚིགས། ^4-1-0

[Block 115]
རྟགས་དེ་ཡང་རང་བཞིན་དང་། འབྲས་བུ་དང་། མི་དམིགས་པའི་བདག་ཉིད་རྣམ་པ་གསུམ་དུ་ཡང་བསྟན་པ་ཁོ་ན་སྟེ། དེ་ལ་དགེ་སློང་དག་ཀུན་འབྱུང་བའི་ཆོས་ཅན་གང་ཅི་ཡང་རུང་ཞེས་བྱ་བ་འདིས་ནི་རང་བཞིན་ཞེས་བྱ་བའི་གཏན་ཚིགས་བཤད་དོ། །

[Block 116 [HEADING]]
### འབྲས་བུ། ^4-2-0

[Block 117]
འབྲས་བུ་ཞེས་བྱ་བ་ཡང་།

[Block 118 [VERSE]]
དུ་བ་ལས་ནི་མེར་ཤེས་ཏེ། །
ཆུ་སྐྱར་ལས་ནི་ཆུ་ཡིན་ནོ། །
བྱང་ཆུབ་སེམས་དཔའ་བློ་ལྡན་གྱི། །
རིགས་ནི་མཚན་མ་རྣམས་ལས་ཤེས། །

[Block 119]
ཞེས་བྱ་བ་འདིས་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 120 [HEADING]]
### མི་དམིགས་པའི་ཁྱད་པར། ^4-3-0

[Block 121]
མི་དམིགས་པ་ཙམ་ཚད་མ་ཉིད་ཡིན་པ་སྤང༌[^92]བར་མཛད་པས། མི་དམིགས་པའི་ཁྱད་པར་ཞེས་བྱ་བ་ཡང་བསྟན་པ་ཁོ་ན་སྟེ། ཇི་སྐད་དུ། དགེ་སློང་དག་གང་ཟག་གིས་གང་ཟག་ལ་ཚོད་མ་འཛིན་ཅིག །གང་ཟག་ལ་ཚད་ཀྱང་མ་འཛིན་ཅིག །དགེ་སློང་དག་གང་ཟག་གིས་གང་ཟག་ལ་ཚོད་འཛིན་པ་ནི་ཉམས་པར་འགྱུར་ཏེ། གང་ཟག་གི་ཚོད་ནི་ང་འམ་ང་དང༌[^93]འདྲ་བ་ཡོད་པ་གང་ཡིན་པས་གཟུང་བར༌[^94]བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 122]
འདིས་ནི་ངོ་བོ་ཉིད་ཀྱིས་བསྐལ་པའི་དོན་དག་ལ་མི་དམིགས་པ་ཙམ་ཚད་མ་ཉིད་ཡིན་པ་སྤོང་བར་མཛད་པས། མི་དམིགས་པ་ཁོ་ན་ཚད་མ་ཡིན་གྱི། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 123 [HEADING]]
## གཞན་གྱི་དོན་གྱི་རྗེས་སུ་དཔག་པ། ^5-0

[Block 124 [HEADING]]
### རང་གི་ངོ་བོ། ^5-1-0

[Block 125]
རིགས་པ་ཅན་ལ་སོགས་པ་ནི་གཞན་གྱི་དོན་གྱི་རྗེས་སུ་དཔག་པ་ཚིག་ཡན་ལག་ལྔ་པ་ཡིན་ཏེ། ཡན་ལག་ལྔ་ནི། དམ་བཅས༌[^95]པ་དང་། གཏན་ཚིགས་དང་། དཔེ་དང་། ཉེ་བར་སྦྱར་བ་དང་། མཇུག་བསྡུ་བ་རྣམས་སོ་ཞེས་ཟེར་རོ། །

[Block 126]
རང་གི་སྡེ་པ་ཁ་ཅིག་ཀྱང་། གཞན་གྱི་དོན་གྱི་རྗེས་སུ་དཔག་པ་ནི། ཚིག་ཡན་ལག་གསུམ་པ་ཡིན་ཏེ། ཡན་ལག་གསུམ་ནི་དམ་བཅའ་བ་དང་། གཏན་ཚིགས་དང་། དཔེ་རྣམས་སོ་ཞེས་བྱ་བར་བསྟན་ཏོ།[^96] །གཞན་དག་ནི་སྔར་བཤད་པའི་ཡན་ལག་ལྔ་པོ་དེ༌[^97]ཁོ་ན་ལྟར་འདོད་དེ། དེ་དག་དགག་པར་འདིའི་རང་གི་ངོ་བོ་བསྟན་ཏོ། །

[Block 127 [HEADING]]
### རབ་ཏུ་དབྱེ་བ། ^5-2-0

[Block 128]
རྟོག་གེ་པ་གཞན་ཐམས་ཅད་ནི། འདི༌[^98]རེ་ཞིག་ཆོས་མཐུན་པ་དང་། ཆོས་མི་མཐུན་པ་དང་ལྡན་པའི་ཚིག་སྦྱོར་བ་གང་ཡིན་པ་འདི་ཙམ་ཞིག་ཆུལ་ཡིན་ནོ། །

[Block 129]
དེ་ལྟ་མ་ཡིན་ན་ཆོས་མཐུན་པ་ཙམ་ཞིག་སྦྱར་བས་ཀྱང་། ཇི་ལྟར་ཆོས་མི་མཐུན་པར༌[^99]རྟོགས་པར་འགྱུར། ཆོས་མི་མཐུན་པ་ཙམ་ཞིག་སྦྱར་ན་ཡང་ཆོས་མཐུན་པ་རྟོགས་པར་ག་ལ་འགྱུར། དེ་ལྟ་བས་ན་གཉི་ག་རྟོགས་པར་བྱ་བའི་ཕྱིར་གཉི་ག་བརྗོད་པར་བྱ་དགོས་སོ་ཞེས་བྱ་བར་རྟོགས་སོ། །

[Block 130]
དེ་བསལ་བའི་ཕྱིར་དེ་ནི་རྣམ་པ་གཉིས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་རབ་ཏུ་དབྱེ་བ་བརྗོད་དོ། །

[Block 131]
དེ་ལ་སྦྱོར་བ་གཅིག་གི་ཡང་ནུས་པ་ཉེ་བར་བསྟན་པའི་ཕྱིར། དཔེར་བརྗོད་པ་བསྙད་དོ། །

[Block 132]
བྱེ་བྲག་པ་ལ་སོགས་པ་ནི་སྐྱེ་བ་དང་ལྡན་པ་ཐམས་ཅད་ལ་འབྲེལ་པ་ལ་སོགས་པ་ཁྱད་པར་སྒྲ་རྣམས་འཇུག་པའི་རྒྱུ་མཚན་ཐ་དད་པ་ཁོ་ན་ཡོད་པར་ཉེ་བར་རྟོག་ཅིང་། སྒྲ་ཙམ་ཐ་དད་པའི་སྒོ་ནས་དོན་ཐ་དད་པར་རྟོགས་ཏེ། དེ་དག་གི་གཞུང་ལུགས་དགག་པའི་ཕྱིར། རང་བཞིན་གྱི་གཏན་ཚིགས་ཀྱིས་རབ་ཏུ་དབྱེ་བ་རྣམ་པ་གསུམ་བསྟན་ཏོ། །

[Block 133]
རང་བཞིན་གྱི་གཏན་ཚིགས་རྣམ་པ་འདི་གསུམ་ཆར་གྱི་ཡང་ལོག་པར་རྟོགས་པར༌[^100]བསལ་བའི་ཕྱིར། སྔར་བཤད་པ་ཁོ་ནའི་ཡུལ་ཉེ་བར་བསྟན་པར་བསྒྲུབ་པའི་ཆོས་དེ་དག་ཐམས་ཅད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 134]
སྦྱོར་བ་གཅིག་ལ་ཡང་ཚུལ་གསུམ་པའི་རྟགས་བསྒྲུབ་པའི་ནུས་པ་ཡོད་པ་ཁོ་ནའོ་ཞེས་བྱ་བར་བསྟན་པའི་ཕྱིར། ཆོས་མཐུན་པས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཆོས༌[^101]ཉེ་བར་བརྗོད་དོ། །

[Block 135 [HEADING]]
### ཕྱོགས་ཀྱི་མཚན་ཉིད། ^5-3-0

[Block 136]
རང་གི་སྡེ་པ་གང་དག་ཉེ་བར་སྦྱར་བ་དང་། མཇུག་བསྡུ་བ་དག་ནི་ལྡོག་པ༌[^102]ཡིན་པའི་ཕྱིར་མ་བསྟན་པ་ལ་ཡང་རག་ན་ཕྱོགས་གོ་ཅི་སྟེ་སྟོན་པར་མི་བྱེད་སྙམ་སྟེ་སེམས་པ་དེ་དག་ལ་སྦྱོར་བ་འདི་གཉི་ག་ལ་ཡང་ཕྱོགས་བསྟན་པར་ངེས་པ་མེད་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།[^103] གཞན་དག་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་པ་ཡང་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་བཟུང་ནས། དེའི་སྒོ་ནས་གཏན་ཚིགས་ཀྱི་སྐྱོན་རྗོད༌[^104]པར་བྱེད་དེ། དེ་དག་བསལ་བའི༌[^105]ཕྱོགས་ཀྱི་མཚན་ཉིད་བཤད་དོ། །

[Block 137]
རིགས་པ་ཅན་ལ་སོགས་པ་ནི་དམ་བཅའ་ནི་བསྒྲུབ་པར་བྱ་བ་བསྟན་པ་ཡིན་ནོ་ཞེས་ཕྱོགས་ཀྱི་མཚན་ཉིད་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པར་ཉེ་བར་སྟོན་ཏོ། །

[Block 138]
དེ་བཞིན་དུ་རང་གི་སྡེ་པ་ཁ་ཅིག་གིས་ཀྱང་མཚན་ཉིད་ཡོངས་སུ་མ་དག་པར་ཉེ་བར་བསྟན་ཏེ། དེ་སྐད་དུ་སློབ་དཔོན་དབྱིག་གཉེན་གྱིས་རྣམ་པར་དཔྱད་པར་འདོད་པའི་དོན་ཕྱོགས་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 139]
ནམ་མཁའི་གོས་ཅན་རྣམས་ནི་ཕྱོགས་ཀྱི་ཕྱོགས་གཅིག་ལ་ཡོད་པར༌[^106]ཡང་གཏན་ཚིགས་ཡིན་པར་རྟོགས་ཏེ། དཔེར་ན་ཤིང་རྣམས་ནི་སེམས་ཅན་ཡིན་ཏེ། ནུབ་མོ་ཉལ་བའི་ཕྱིར་རོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 140]
དེ་དག་གིས་ཉལ་བ་འདབ་མ་འཁུམས་པ་ལ་སོགས་པ་ཙམ་གྱི་མཚན་ཉིད་ཡིན་པར་བརྗོད་པར༌[^107]འདོད་མོད་ཀྱི། འོན་ཀྱང་འདི་ནི་ཕྱོགས་སུ༌[^108]བྱས་པའི་ཤིང་ཐམས་ཅད་ལ་མ་གྲུབ༌[^109]སྟེ། དེ་ཤིང་ཏི་ན་ཏི་ཀ་ལ་སོགས་པ་ཁོ་ན་ལ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 141]
དེ་རྣམ་པར་གཅད་པར་གོ་རིམས་བཞིན་དུ་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་པ་དང་། ངེས་པར་གཟུང་བ༌[^110]སྨོས་ཏེ། ཡུལ་ཁྱད་པར་ཅན་དུ་ངེས་པར་གཟུང་བ༌[^111]ནི་འདོད་པའི་དོན་རྟོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 142]
དེ་ལྟ་མ་ཡིན་ན་བཤད་མ་ཐག་པའི་དོན་རྟོགས་པར་མི་འགྱུར་རོ། །

[Block 143]
བྱེ་བྲག༌[^112]ལ་སོགས་པ་ནི་རྗེས་སུ་དཔག་པར་བྱ་བ་ཁོ་ན་ལ་ཡོད་པ་ཐུན་མོང་མ་ཡིན་པ་མ་ངེས་པ་ཡང་དངོས་སུ་གཏན་ཚིགས་ཡིན་པར་ཁས་ལེན་ཏེ། དཔེར་ན་གསོན་པོའི་ལུས་ནི་བདག་དང་བཅས་པ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་རོ༌[^113]ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 144]
དེ་བཟློག་པའི་ཕྱིར་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་བརྗོད་དོ། །

[Block 145]
ཕྱོགས་ཀྱི་མཚན་ཉིད་འདི་རྣམ་པ་གཉི་ག་ཡང་ཧ་ཅང་ཁྱབ་ཆེ་བའི༌[^114]ཉེས་པ་ཡོད་ལ། དེ་དག་ལ་གཏན་ཚིགས་དང་དཔེ་མ་གྲུབ་པ་སྨྲ་བ་ཡང་ཡོད་པའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་ཡང་ཕྱོགས་ཀྱི་མཚན་ཉིད་བསྟན་པ། [^115]གྲངས་ཅན་པ་རྣམས་ནི་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་དག་ལ་མ་གྲུབ་པ་ཡང་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་སྟོན་ཏེ། དཔེར་ན་མིག་ལ་སོགས་པ་ནི་གཞན་གྱི་དོན་ཡིན་ནོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །
--- END BLOCKS ---
