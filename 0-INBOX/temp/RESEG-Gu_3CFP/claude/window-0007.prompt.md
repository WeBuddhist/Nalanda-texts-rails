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
[Block 246]
རྙེད་པའི་རྒྱུ་ཞེས་བྱ་བ་ནི། མཐོང་བ་ལ་དོན་མེད་པའི་རྙེད་པ་སྒྲུབ་པའོ། །

[Block 247]
གཞན་དག་གི་སྤྲོ་བ་སྐྱེད་པ་ཞེས་བྱ་བ་དང་། ཡང་དག་པ་མ་ཡིན་པའི་ཡོན་ཏན་སྣ་ཚོགས་སྟོན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་ནི་གཞན་གྱི་དོན་མེད་པར་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 248]
གལ་ཏེ་གཞན་རྣམས་ཡང་དག་པར་མགུ་བར་འགྱུར༌[^144]ན་གཞན་གྱི་དོན་ཡང་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་མེད་པར་བསྟན་པ་ཡིན་ཏེ། དེ་ལྟར་ན་དགེ་བའི་ཆོས་སྡུད་པ་ཉིད་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 249]
བདག་ལ་བསྙེན་བཀུར་བྱ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 250]
བསྙེན་བཀུར་བྱ་བ་བདག་གིར་བྱ་བ་འདོད་པས་ཞེས་བྱ་བ་ནི་བསམ་པ་ཉིད་ཀྱིས་སོ། །

[Block 251]
བསྙེན་བཀུར་བྱ་བ་བདག་གིར་བྱ་བའི་དོན་དུ་ཞེས་བྱ་བ་ནི། སྦྱོར་བ་དང་གཉི་ག་དག་ལ་རང་གི་དོན་ཏོ།[^145] །ཆོས་མ་ཡིན་པ་ཉིད་ཀྱིས་ཡིན་གྱི་ཆོས་ཀྱིས༌[^146]མ་ཡིན་ཞེས་བྱ་བ་ནི། འབའ་ཞིག་གིས་སོ། །

[Block 252]
ཚོགས་སྡུད་པ་ཞེས་བྱ་བ་ནི་ཕན་པ་བྱ་བ་མེད་པའོ།[^147] །ཚེ་འདིའི་བདེ་བ་ལ་གནས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། མཐོ་རིས་ཀྱི་དོན་གྱི་བསམ་གཏན་ནི་འབའ་ཞིག་པ་སྟེ། སྔར་བསྟན་པའོ། །

[Block 253]
འདི་ལྟར་ཡང་བཟོད་པ་ཞེས་བྱ་བ་ལ། མཐོ་རིས་ཀྱི་དོན་དུ་ཚུལ་ཁྲིམས་དང་། བརྩོན་འགྲུས་རྩོམ་པ་དང་། བསམ་གཏན་དང་། ཤེས་རབ་རྣམས་ཡང་དག་པར་བླངས་ནས་གནས་པ་ནི་འབའ་ཞིག་པར་སྔར་བསྟན་ཏོ། །

[Block 254]
སྦྱིན་པ་དང་། བཟོད་པ་ཡང་དག་པར་བླངས་ཏེ་གནས་པའི་མ་བསྟན་པའི་རྒྱུ་རབ་ཏུ་བསྟན་པ་ལས་བརྩམས་ཏེ། སྙིང་རྗེ་སྔོན་དུ་འགྲོ་བའམ་ཞེས་བྱ་བ་ལ། སྙིང་རྗེ་མེད་པར༌[^148]སྔོན་དུ་འགྲོ་བ༌[^149]ན་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 255]
བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོས་པའམ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་ཏུ་ཡོངས་སུ་མ་བསྔོས་པ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 256]
སྦྱིན་པ་དང་བཟོད་པ་འདི་དག་ནི་འབའ་ཞིག་པ་ཡིན་ན་ཡང་རང་གི་དོན་གྱི་ངོ་བོར་ནི༌[^150]མི་འགྱུར་ཏེ། ངེས་པར་འཚང་རྒྱ་བ་ཉིད་དང་གཞན་པའི་རང་གི་དོན་དུ་ཡང་འགྱུར་བས། བྱང་ཆུབ་ཀྱང༌[^151]འཐོབ་ལ། མཐོ་རིས་ཀྱི་རྒྱུ་ཡང་ཡིན་ཏེ། མཐོ་རིས་ཀྱི་ཕྱིར་དང་རང་གི་མཐོ་རིས་ཀྱི༌[^152]ཕྱིར་ཡིན་པས་སྦྱིན་པ་དང་བཟོད་པ་འབའ་ཞིག་ཉིད་ཡིན་ན་ཡང་གཞན་གྱི་དོན་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 257]
མཐོ་རིས་ཀྱི་ཕྱིར་མ་ཡིན་པ་ནི་སྔ་མ་ལྟར་འབའ་ཞིག་པ་ཉིད་དུ། [^153]ལྟ་བ་ལོག་པར་ཞུགས་པ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན། སྨྲས་པ། འོང་བ་མ་མཐོང་བ་དང་། འབྲས་བུ་མ་མཐོང་བ་ཞེས་བྱ་བ་སྟེ། འཇིག་རྟེན་ཕ་རོལ་མེད་དོ་ཞེའམ། ལེགས་པར་སྤྱད་པ་དང་། ཉེས་པར་སྤྱད་པའི་འབྲས་བུ་རྣམ་པར་སྨིན་པ་མེད་དོ་ཞེས་ཟེར་བའོ། །

[Block 258]
ཚུལ་ཁྲིམས་ཉམས་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་འཆལ་བའོ། །

[Block 259]
སྒྲུབ་པ་མེད་པ་ཞེས་བྱ་བ་ནི། ནན་ཏན་མི་བྱེད་པའོ། །

[Block 260]
ས་འོག་མ་ལས་ཡང་དག་པར་འདས་པ་ཞེས་བྱ་བ་ནི། འདོད་པའི་ཁམས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་མི་འོང་བའམ། ཁམས་ཉིད་ལ་འདོད་ཆགས་དང་བྲལ་བའོ། །

[Block 261]
བསམ་གཏན་ལས་གྱུར་པ༌[^154]ལ་མཁས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ནི། བསམ་གཏན་ལ་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 262]
འདི་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འདིར་རྒྱུ་བསྟན་ཏོ། །

[Block 263]
དེ་ལ་གཞན་གྱི་དོན་འབའ་ཞིག་ཡིན་ན་ཇི་སྐད་བསྟན་པ་སྔ་མ་གཉིས་ནི་ཞེས་བྱ་བ་ནི་ལྟ་བ་ལོག་པར་ཞུགས་པའི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ཉམས་པས་ཆོས་སྟོན་པའོ། །

[Block 264]
དེ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ས་འོག་མ་ལས་ཡང་དག་པར་འདས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཇི་སྐད་བསྟན་པའོ། །

[Block 265]
དེ་ལ་དགེ་བ་ཡོངས་སུ་འཛིན་པར་བྱེད་ཅེས་བྱ་བ་ནི། དགེ་བ་སྐྱེད་པར༌[^155]བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 266]
དགེ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི། དགེ་བ་སྤེལ་བའོ། །

[Block 267]
དགེ་བ་ཡོངས་སུ་གཟུང་བ་ཡང་དག་པར་འཛིན་དུ་འཇུག་ཅེས་བྱ་བ་ནི། དགེ་བ་ཉེ་བར་སོག་ཏུ་འཇུག་པའོ། །

[Block 268]
འདུལ་བར༌[^156]བྱེད་ཅེས་བྱ་བ་དང་འཇུག་པར༌[^157]བྱེད་ཅེས་བྱ་བ་དང་། འགོད་པར་བྱེད་ཅེས་བྱ་བ་ནི། ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོ་ཉིད་དོ། །

[Block 269]
རང་དང་གཞན་གྱི་དོན་གྱིས་བསྡུས་པའི་དོན་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ངོ་བོ་ཉིད་དང་རྒྱུ་ཉིད་དང་། དུས་ཉིད་དང་། ཉེ་བར་ཞི་བ་ཉིད་དོ་ཞེས་བསྟན་ཏེ། ཕན་པ་བྱེད་པ་ཉིད་ཀྱིས་དེ་ནི་ཕན་པ་ཉིད་དོ། །

[Block 270]
རྒྱུ་བཞིའི་བསྡུས་པའི་དོན་ནི། རྒྱུ་རྣམ་པ་གཉིས་ཏེ། བདེ་བ་འཕེལ་བ་དང་སྐྱེད་པའོ། །

[Block 271]
སྐྱེད་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། རྟེན་དང་། དམིགས་པ་དང་། ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་གྱི་མཚན་ཉིད་དོ། །

[Block 272]
འཕེན་པ་ཡང་རྣམ་པ་གཉིས་ཏེ་མཐོང་བའི་ཆོས་ཅན་དང་། ཕ་རོལ་པའི་དབྱེ་བས་སོ། །

[Block 273]
བདེ་བའི་རྒྱུ་ལ་བདེ་བར་ཉེ་བར་བརྟགས་པར་བྱས་ནས། རྒྱུ་བདེ་བ་ཞེས་བརྗོད་དོ། །

[Block 274]
དཔེར་ན་མེ་བདེ་བ༌[^158]ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 275]
རྒྱུ་བདེ་བར་བསྡུས་པའི་རྒྱུ་གསུམ་པོ་དེ་དག་ཅེས་བྱ་བ་ནི། དབང་པོ་དང་། ཡུལ་དང་། བདེ་བ་ཚོར་བར་འགྱུར་བའི་རེག་པ་ནི་ལུས་ཀྱི་ལས་ཀྱིས་བསྡུས་པའི་དབང་པོ་ལྔ་སྡུད་པར་བྱེད་པས་ཉམས་སུ་མྱོང་བའི་ཚོར་བའོ། །

[Block 276]
སློབ་པ་དང་མི་སློབ་པའི་ལམ་དང་ཡང་དག་པར་ལྡན་པའོ། །

[Block 277]
གྲང་བ་དང་ཚ་བས་བསྡུས་པ་ནི་དུས་ལས་འབྱུང་བའི༌[^159]སྡུག་བསྔལ་གྱིས༌[^160]བསྡུས་པའོ། །

[Block 278]
བཀྲེས་པ་དང་། སྐོམ་པས་བསྡུས་པ་ནི། ནང་གི་བདག་ཉིད་ཅན་གྱིས་བསྡུས་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་དང་།[^161] ངལ་བའི་སྡུག་བསྔལ་དང་། གློ་བུར་བའི་སྡུག་བསྔལ་དག་གོ། །

[Block 279]
སྡིག་པ་མི་དགེ་བའི་ཆོས་སྤངས་ཏེ་དབེན་པས་ཞེས་བྱ་བ་ནི། སྤངས་པ་ཉིད་དབེན་པའོ། །

[Block 280]
ཡང་ན༌[^162]སྤངས་པའི་མཚན་ཉིད་ཀྱིས་དབེན་པ་ཉིད་དེ་ཉེ་བར་ཞི་བའི་བདེ་བའོ། །

[Block 281]
ཡང་དག་པར་སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི། ཚོར་བ་རྣམ་པ་གསུམ་པོ་དག་གིས༌[^163]སྡུག་བསྔལ་ལོ། །

[Block 282]
དེ་ལས་གཞན་པ་ལྷག་མ་རྣམས་ནི་གནོད་པ་མེད་པའི་བདེ་བ་ཞེས་བྱ་བ་ལ། མངོན་པར་འབྱུང་བའི་བདེ་བ་དང་། རབ་ཏུ་དབེན་པའི་བདེ་བ་དང་།

[Block 283 [VERSE]]
ཉེ་བར་ཞི་བའི་བདེ་བའོ། །
ཐ་མ་ཞེས་བྱ་བ་ནི།
རྫོགས་པར་བྱང་ཆུབ་པའི་བདེ་བའོ། །

[Block 284]
མངོན་པར་འབྱུང་བའི་བདེ་བ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པ་ཉིད་ཡིན། རབ་ཏུ་དབེན་པའི་བདེ་བ་ནི་དེའི་ཕྱོགས་པ་ཉིད་ཡིན། ཉེ་བར་ཞི་བའི་བདེ་བ་ནི་དེ་འདྲེན་པར་བྱེད་པ་ཉིད་ཡིན་གྱི། དོན་དམ་པར་ནི་མ་ཡིན་ཏེ། དོན་དམ་པའི་ནི་ཐ་མ་ཉིད་དེ། གནོད་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 285]
བདེ་བ་འདོད་པ༌[^164]ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། བསམ་པས་སོ། །
--- END BLOCKS ---
