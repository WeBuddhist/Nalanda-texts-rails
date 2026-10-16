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
[Block 6091]
གནས་རྣམས༌[^3912]བཞི་ལས་སྐྱེས་པའི་ཤ་བསྟན་པ་ཡིན་ཏེ། དུས་ཇི་ལྟ་བ་དང་། ནད་གཞི༌[^3913]ཇི་ལྟ་བ་བཞིན་དུ་སྨན་པས༌[^3914]ན་བ་ཉིད་དུ་སྦྱར་རོ། །

[Block 6092]
དེ་ལྟར་རེ་ཞིག་ཡིད་དུ་འོང་ཞིང་འདོད་པའི་ཤ་རྙེད་ཅིང་འགྲུབ་པ་ཉིད་དུ་བསྟན་ནས། གཞན་ཡང་བདེ་བ་ཐོབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། རྔ་སྒྲ་སྙན་པ་དབྱར་གྱི་འབྲུག་སྒྲ་བཞིན་དུ་སྒྲོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6093]
རྔ་སྒྲ་སྙན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་དང་པོས་ནི། སྦྱིན་པའི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོའི་ཕན་ཡོན་ཡོངས་སུ་བཏང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6094]
གཉེན་དང་། བུ་དང་། ནང་མི་ཞེས་བྱེ་བ་ཕྱེད་འོག་མས་ནི། བཟོད་པའི་འབྲས་བུ་གཡོག་འཁོར་མང་པོས་ཕན་ཡོན་ཡོངས་སུ་བཏང་བ་བསྟན་ཏོ། །

[Block 6095]
དགག་པར་བྱ་བ་དང་། དགག་པ་ལ་སྦྱར་ཞིང་དབང་བྱ་བ་དེ་གཉིས་ཀྱི་རྒྱུའི་དབང་དུ་བྱས་ནས། རྒྱལ་པོའི་སེམས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། རྒྱལ་པོའི་སེམས་ཀྱི་དབང་དུ་འགྲོ་བ་ནི་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕྱི་རོལ་གྱི་སྟོབས་དང་ལྡན་པ་ལས་ཀྱང་རྒྱལ་བར་ནུས་པ་ཡིན་པའི་ཕྱིར། ནང་གི་བདེ་བ་ནི་ཚར་བཅད་ཅིང་རྒྱལ་བར་བྱ་བ་དེ་ལ་སྡང་བར་བྱ་བ༌[^3915]མི་རིགས་སོ། །

[Block 6096]
ཆོས་དང་། སྲིད་ལ་མི་གནོད་པའི་ལམ་དུ་འཇུག་པར་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མི་ཡི་བདག་པོ་འཇིག་རྟེན་ཕྱི་མའང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6097]
ཆོས་དང་སྲིད་ལ་མི་གནོད་ལམ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། འཇིག་རྟེན་ཕ་རོལ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 6098]
ཆོས་དང་། སྲིད་ལ་མི་གནོད་པ་དེ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། ཆོས་དང་སྲིད༌[^3916]ལ་གནོད་པའི་དབང་དུ་བྱས་ནས། དེ་བས་འགའ་ཡང་ཕན་པ་མ་ཡིན་བསྟན༌[^3917]མི་རིགས། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 6099]
གང་ཆོས་དང་། སྲིད་ལ་གནོད་པ་མ་ཡིན་པའི་ལམ་དེ་ཉིད་སྨྲས་པ། ལམ་གང་ཡིད་དུ་འོང་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་བྱེད་འོག་མའོ། །

[Block 6100]
གྲགས་དང་མི་འགལ་བ་ཞེས་བྱ་བའི་གྲགས་པ་དང་མི་འགལ་བའི་མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། ལམ་གང་ཡིད་དུ་འོང་ལ་ཞེས་བྱ་བ་སྟེ། དམ་པ་རྣམས་བཞེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 6101]
ཇི་ལྟར་མི་དགའ་བ་ཡིན་ན་ཡང་ཕན་པའི་སྨན་ནི་ནད་པས་བཏུང་བར་བྱ་བ་དེ་བཞིན་དུ་བསྟེན་པའི་རིགས་སོ། །

[Block 6102]
རྒྱུའི་སྐབས་སུ༌[^3918]གནས་པ་སྟེ། ཇི་ལྟར་ཞེ་ན། གྲགས་པའི་རྒྱུ་ཡིས་འགྲོ་བ་འདི་དག་ཁྱབ། །ཅེས་བྱ་བ་ཡིན་ཏེ། དེ་ཉིད་བསྟན་པའོ། །

[Block 6103]
འདི་ལྟར་གང་གིས་སྡིག་པ་སྤྱོད་པ་དེ་ནི་འདི་ལྟར་སྡིག་པ་སྤྱོད་པ་དེའོ། །

[Block 6104]
སྡིག་པ་སྤྱོད་པའི་འཆི་བདག་གི་ཕོ་ཉ་གང་ཡིན་པ་དེ་ནི་འཆི་བདག་ཕོ་ཉར་གྱུར་པ་སྟེ།

[Block 6105 [VERSE]]
སྡིག་པ་སྤྱོད་པའི་ཁྱད་པར་འདིས་སོ། །
བདག་ལ་ཇི་ལྟར་བཀའ་སྩལ༌[^3919]དེ་བཞིན་བགྱི། །

[Block 6106]
ཞེས་བྱ་བ་ནི་བཀའ་སྩལ་པ་གཞན་ཡང་དེ་བཞིན་དུ་བགྱིའོ་ཞེས་པའོ། །

[Block 6107]
བཙོན་རར་སྩལ་བས་མི་དགའ་ཞིང་། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 6108]
བཞིན་མདངས་ཉམས་ལ་ཞེས་བྱ་བ་ནི་གཟུགས་ཀྱི་ལུས་ཀྱི་གཟི་མདངས་ཉམས་པར་བསྟན་ཏོ། །

[Block 6109]
མྱ་ངན་གདུངས་པའི་ཡིད་ཅེས་བྱ་བ་ནི། མིག༌[^3920]གི༌[^3921]སྡུག་བསྔལ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6110]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བུ་ཟླ་བའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 6111 [HEADING]]
## ལྕགས་ཀྱི་ཁྱིམ་ནས་བསྐྱེད་པའི་སྐྱེས་པའི་རབས། ^35-0

[Block 6112]
ལེགས་པའི་ལམ་ནི་ཐར་པའི་ལམ་མོ། །

[Block 6113]
རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་དང་། སྡུག་པ་དང་བྲལ་བ་ཞེས་བྱ་བ་ལ་འདིར་སྩོགས་པ༌[^3922]སྨོས་པས་ནི། མི་སྡུག་པ་དང་ཕྲད་པ་གང་འདོད་པ་བཙལ་ཏེ་མ་རྙེད་པ་དེ་ཡང་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཟུང་ངོ་། །མགོན་མེད་པ་རྣམས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་སྡུག་བསྔལ་ཞིང་འདོད་པས་འཇུག་པ་སྟེ། དེ་མེད་པའོ། །

[Block 6114]
སྐྱབས་མེད་པ་ཞེས་བྱ་བ་ནི་སྐྱོབ་པར་བྱེད་པ་བདག་ཉིད་ལ༌[^3923]མེད་པ་སྟེ། འདི་ནི་སྐྱབས་མེད་པའོ། །

[Block 6115]
དཔུང་གཉེན་མེད་པ་ཞེས་བྱ་བ་ནི་བདེ་ལེགས་སུ་ཡུལ་དག་ཏུ་ཕྱིན་པར་བྱེད་པ། བྱང་ཆུབ་སེམས་ལས་གཞན་མེད་པ་སྟེ། རྒྱུ་དེ་གསུམ་མེད་པར་བསྟན་ཏོ། །

[Block 6116]
སྙིང་རྗེས་བསྐུལ་ཏེ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་མགོན་མེད་པ་ལ་བདག་ཉིད་མགོན་དུ་ཁས་ལེན་པ་བསྟན་ཏོ། །

[Block 6117]
དེ་དག་བསྐྱབ་པར་སེམས་པ་ཞེས་བྱ་བ་ནི། དེ་ལྟར་སྐྱབས་མེད་པ་དག་ལ་བདག་ཉིད་བསྐྱབ་པར་སེམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6118]
རབ་ཏུ་དགེ་བའི་རང་བཞིན་ཅན་དེ་བསྒྲུབ་པར༌[^3924]འདོད་པའི་ཡིད་ཅེས་བྱ་བ་ནི་དཔུང་གཉེན་མེད་པའི་འཇིག་རྟེན་ལ་བདག་ཉིད་དཔུང་གཉེན་བྱེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6119]
འདིས་ནི་གསུམ་པོ་དེ་དག་གི་ཁྱད་པར་བསྟན་པ་ཡིན་ཏེ། མགོན་མེད་པ་དང་། སྐྱབས་མེད་པ་དང་། དཔུང་གཉེན་མེད་པ་དག་གི་ཁྱད་པར་དུ་གཏོགས་པར་བྱ་སྟེ། སྙིང་རྗེས་བསྐུལ་བའི་ཕྱིར་མགོན་ནོ། །

[Block 6120]
དེ་དག་བསྐྱབ་པར་སེམས་པའི་ཕྱིར་སྐྱབས་སོ། །

[Block 6121]
རབ་ཏུ་དགེ་བའི་རང་བཞིན་ཅན་དེ་ཕན་པ་དང་། བདེ་བའི་ཁྱད་པར་ཅན་ཞེས་བྱ་བ་འདིས་ནི་དཔུང་གཉེན་ནོ། །

[Block 6122]
རྒྱུ་འདི་གསུམ་དང་ལྡན་པའི་ཕྱིར། སྡུག་བསྔལ་ལས་སྐྱོབ་པ་ཉིད་ཀྱིས༌[^3925]ཕན་པ་དང་བདེ་བ་བསྒྲུབ་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6123]
དེ་བཞིན་དུ་གཞན་འདས་པ་གང་དང་གང་དག་ཏུ་ཚིག་གསུམ་པོ་འདི་བསྟན་པ༌[^3926]དེ་དང་དེ་དག་ཏུ་ཡང་འདི་བཞིན་དུ་རྟོགས་པར་བྱའོ། །

[Block 6124]
འབངས་རྣམས་གློ་བ་ཉེ་བའི་བདེ་བ་དང་འཁྲུག་པ་མེད་པའི་དར་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་འདིས་ནི་རང་གི་ཡུལ་གྱི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6125]
རྒྱལ་ཕྲན་ཐམས་ཅད་ཀྱི་དྲེགས་པ་གང་ཡིན་པ་དེ་ནི་རྒྱལ་ཕྲན་ཐམས་ཅད་ཀྱི་དྲེགས་པའོ། །

[Block 6126]
དེ་རྣམས་ཕྱག་འཚལ་བ་ནི་རྒྱལ་ཕྲན་དྲེགས་པ་རྣམས་ཕྱག་འཚལ་བའོ། །

[Block 6127]
འདིས་ནི་ཡུལ་གཞན་དུ་གྱུར་བའི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6128]
དུལ་བ་ལ་དགའ་བས་ཞེས་བྱ་བས༌[^3927]མ་འོངས་པའི་འབྲས་བུ༌[^3928]རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6129]
རྒྱལ་པོའི་རིགས་དེ་དང་དེ་དག་བདེ་བ་དང་སྡུག་བསྔལ༌[^3929]འདྲ་བར་འགྱུར་བ༌[^3930]སྟེ། དེའི་བདེ་བ་སྡུག་བསྔལ་མཉམ་པའོ། །

[Block 6130]
སྦྱིན་པ༌[^3931]ཐོབ་པས་བྲམ་ཟེ་མགུ་ཞིང་གཡེངས། །[^3932]ཞེས་བྱ་བ་ནི་ཕོངས་པའི༌[^3933]སྐྱེ་བོ་མགུ་བ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་པའོ། །
--- END BLOCKS ---
