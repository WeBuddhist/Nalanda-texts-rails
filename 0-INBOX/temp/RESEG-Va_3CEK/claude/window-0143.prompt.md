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
[Block 5006]
འདི་ནི་སེམས་ཀྱི་རྣམ་པ་ཐམས་ཅད་ལ་ཕྱོགས་ཙམ་དུ་ཟད་ཀྱི་མཇུག༌[^3558]ཐོགས་ཀྱི་རྒྱུ་ཤེས་པ་ལ་ནི་སངས་རྒྱས་རྣམས༌[^3559]མངའ་བདག་ཡིན་ཏེ། འདི་སྐད་དུ་རྨ་བྱའི་མདོངས་ནི་གཅིག་ལ་ཡང་། །

[Block 5007 [VERSE]]
རྒྱུ་ཡི་རྣམ་པ་ཐམས་ཅད་ནི། །
ཀུན་མཁྱེན་མིན་པས་ཤེས་བྱ་མིན། །
དེ་ཤེས་ཀུན་མཁྱེན་སྟོབས་ཡིན་ནོ། །

[Block 5008]
ཞེས་བཤད་ན། གཟུགས་ཅན་མ་ཡིན་པ་སེམས་ཀྱི་བྱེ་བྲག་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། ཅིའི་ཕྱིར་དེ་དང་འདྲ་བ་ཁོ་ནར་སྐྱེ་བར་མི་འགྱུར་ཞིང་མྱུ་གུ་དང་སྡོང་བུ་དང་འདབ་མ་ལ་སོགས་པ་བཞིན་དུ་རིམ་པ་ངེས་པར་སྐྱེ་བར་མི་འགྱུར་ཞེས་བྱ་བ་འདི་ནི་མུ་སྟེགས་ཅན་གང་ལ་ལ་སེམས་ནི་བདག་ལས་སྐྱེའོ་སྙམ་དུ་སེམས་པ་དེ་ཁོ་ན་ལ་གསལ་བར་ཀླན་ཀར་འགྱུར་རོ། །

[Block 5009 [HEADING]]
#### ཡིད་དང་ཕྲད་པའི་བྱེ་བྲག། ^6-3-6-0

[Block 5010]
གལ་ཏེ་ཡིད་དང་ཕྲད་པའི་བྱེ་བྲག་ལ་ལྟོས་པའི་ཕྱིར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། འབྲེལ་པ་གཞན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5011]
འབྲེལ་པ་ཅན་དག་ཡོངས་སུ་ཆད་པའི་ཕྱིར་དང་། ཕྲད་པ་ཞེས་བྱ་བའི་མཚན་ཉིད་ནི་མ་ཕྲད་པ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱི་ཕྲད་པ་ཡིན་ནོ་ཞེས་རྣམ་པར་བཤད་པའི་ཕྱིར་བདག་ཡོངས་སུ་ཆད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 5012]
དེའི་ཕྱིར་ཡིད་འཕྲོས་པ༌[^3560]ལ༌[^3561]བདག་འཕོ་བའམ། ཉམས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 5013]
གལ་ཏེ་ཕྱོགས་གཅིག་ཕྲད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། ཕྱོགས་དེ་དེ་ཉིད་ཀྱི་ཡིན་པ་ཉིད་དུ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 5014]
ཕྲད་པ་ཡོད་དུ་ཆུག་ན་ཡང་འོན་ཀྱང་ཡིད་རྟག་ཏུ་ཁྱད་པར་མེད་པ་ལ་ཇི་ལྟར་ཕྲད་པ་ཁྱད་པར་དུ་འགྱུར། [^3562]གལ་ཏེ་བློའི་ཁྱད་པར་ལ་ལྟོས་པ་ཡིན་ནོ་ཞེ་ན། ཇི་ལྟར་བློའི་ཁྱད་པར་ཡིན་ཞེས་དེ་ཉིད་ལ་ཀླན་ཀ་ཚོལ་བར་བྱེད་དོ། །

[Block 5015]
གལ་ཏེ་འདུ་བྱེད་ཀྱི་ཁྱད་པར་ལ་ལྟོས་པའི་བདག་དང་ཡིད་ཕྲད་པ་ལས་སོ་ཞེ་ན། འདུ་བྱེད་ཀྱི་ཁྱད་པར་ལ་ལྟོས་པའི་སེམས་ཁོ་ན་ལས་ཡིན་པར་ཟད་ཀྱི་བདག་གིས༌[^3563]ནུས་པ་ནི་ཅུང་ཟད་ཀྱང་མི་དམིགས་ཏེ། སྨན་གྱི་འབྲས་བུ་གྲུབ་པ་ལ་སྨན་པ་ངན་གཡོ་ཅན་གྱིས་ཕུ་སྭཱ་ཧཱ་ཞེས་སྨྲས་པ་དག་བཞིན་ནོ། །

[Block 5016]
གལ་ཏེ་བདག་ཡོད་ན་དེ་གཉིས་སྲིད་དོ་ཞེ་ན་ནི། ཚིག་ཙམ་དུ་ཟད་དོ། །

[Block 5017]
གལ་ཏེ་དེ་ནི་རྟེན་ཡིན་ནོ་ཞེ་ན། དཔེར་ན་གང་གི་རྟེན་གང་ཡིན་པ་ལྟ་བུ་དེ་དག་ཀྱང་རི་མོ་དང་རྒྱ་ཤུག༌[^3564]ལ་སོགས་པ་ལྟར་བརྟེན་པ་མ་ཡིན་ལ། དེ་ཡང་རྩིག་པ་དང་གཞོང་བུ་ལ་སོགས་པ་ལྟར་རྟེན་དུ་རིགས་པ་མ་ཡིན་ཏེ། ཐོགས་པ་དང་ཐ་དད་པ་ཉིད་ཀྱིས༌[^3565]ཉེས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 5018]
གལ་ཏེ་དེ་ནི་དེ་ལྟ་བུར༌[^3566]རྟེན་མ་ཡིན་ནོ། །

[Block 5019]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དཔེར་ན་དྲི་ལ་སོགས་པའི་ས་ལྟ་བུའོ༌[^3567]ཞེ་ན། འདི་ཉིད་ཁོ་བོའི་བདག་མེད་དོ་ཞེས་བྱ་བ་ཡིད་ཆེས་པར་བྱེད་པ་ཡིན་པས་ཁོ་བོ་ཡོངས་སུ་ཚིམ་པར་བྱས་ཏེ། དཔེར་ན་དྲི་ལ་སོགས་པ་ལས་ས་གཞན་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 5020]
དྲི་ལ་སོགས་པ་ལས་ས་གཞན་ཡིན་པར་ངེས་པར་འཛིན་པར་བྱེད་པ་དེ་སུ་ཞིག་ཡིན། སའི་དྲི་ལ་སོགས་པ་ཞེས་བྱ་བའི་ཐ་སྙད་ནི་ཅི་ནས་དྲི་ལ་སོགས་པ་དེ་དག་ཉིད་དེ་ཞེས་བྱའི། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་ཤེས་པར་འགྱུར་བ་ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་ཏེ། ཤིང་གི༌[^3568]གཟུགས་ཀྱི་ལུས་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 5021]
འདུ་བྱེད་ཀྱི་ཁྱད་པར་ལ་ལྟོས་པ་ཡིན་དུ་ཟིན་ཀྱང་ཅིའི་ཕྱིར་ཤེས་པ་ཐམས་ཅད་དུས་གཅིག་ཏུ་སྐྱེ་བར་མི་འགྱུར། གང་ཞིག་སྟོབས་ཆེ་བ་དེས་གཞན་དག་ལ་གེགས་བྱེད་དོ། །

[Block 5022]
སྟོབས་ཆེ་བ་དེ་ཉིད་ཅིའི་ཕྱིར་རྟག་པར་འབྲས་བུ་མི་འབྱིན་ཏེ། འདིའི་ཚུལ་གང་ཡིན་པ་དེ་བསྒོས་པ་ཡིན་ན་བདག་ཏུ་རྟོག་པ་ནི་དོན་མེད་པ་ཡིན་ནོ། །

[Block 5023 [HEADING]]
#### དྲན་པ་ལ་སོགས་པ་ཡོན་ཏན་གྱི་དངོས་པོ། ^6-3-7-0

[Block 5024]
གལ་ཏེ་བདག་ནི་གདོན་མི་ཟ་བར་ཁས་བླང་བར་བྱ་སྟེ། དྲན་པ་ལ་སོགས་པ་ནི་ཡོན་ཏན་གྱི་དངོས་པོ་ཡིན་པའི་ཕྱིར་ལ་དེ་ཡང་གདོན་མི་ཟ་བར་རྫས་ལ་བརྟེན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5025]
དེ་དག་གི་རྟེན་གཞན་ཡིན་པར་ཡང་མི་རུང་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 5026]
འདི་དག་ནི་ཡོན་ཏན་གྱི་དངོས་པོ་ཉིད་ཡིན་པར་མ་གྲུབ་བོ། །

[Block 5027]
ཁོ་བོ་ཅག་གི་ལྟར་ན་ཡོད་པ་ཐམས་ཅད་ནི་རྫས་ཡིན་ཏེ། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་ནི་རྫས་དྲུག་གོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 5028]
དེ་དག་རྫས༌[^3569]ལ་བརྟེན་པ་ཉིད་དུ་ཡང་མ་གྲུབ་སྟེ། རྟེན་གྱི་དོན་ནི་བརྟགས་ཟིན་ཏོ། །

[Block 5029]
དེ་ལྟ་བས་ན་འདི་ནི་གྱི་ནའོ། །

[Block 5030 [HEADING]]
#### བདག་མེད་ན་ལས་རྩོམ་པ། ^6-3-8-0

[Block 5031]
བདག་མེད་ན་ཅིའི་ཕྱིར་ལས་རྩོམ། བདག་བདེ་བར་གྱུར་ཅིག །བདག་སྡུག་བསྔལ་བར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་དེའི་ཕྱིར་རོ། །

[Block 5032]
ཡང་བདག་ཅེས་བྱ་བ་ཡང་གང་ཞིག་ཡིན། བདག་ཏུ་འཛིན་པ་འདིའི་ཡུལ་གང་ཡིན་པའོ། །

[Block 5033]
བདག་ཏུ་འཛིན་པ་འདིའི་ཡུལ་གང་ཞིག་ཡིན། ཡུལ་ནི་ཕུང་པོ་ཡིན་ནོ། །

[Block 5034]
ཇི་ལྟར་ཤེས། དེ་དག་ལ་ཆགས་པའི་ཕྱིར་དང་། དཀར་ཤམ་ལ་སོགས་པའི་བློས་གཞི་མཐུན་པར་བྱེད་པའི་ཕྱིར་ཏེ། བདག་དཀར་ཤམ་མོ། །

[Block 5035]
བདག་སྔོ་བསངས་སོ། །

[Block 5036]
བདག་སྦོམ་མོ། །

[Block 5037]
བདག་སྐེམ་མོ། །

[Block 5038]
བདག་རྒས་སོ། །

[Block 5039]
བདག་དར་ལ་བབ་པོ་ཞེས་དཀར་ཤམ་ལ་སོགས་པའི་བློས་བདག་ཏུ་འཛིན་པ་འདི་གཞི་མཐུན་པར་བྱེད་པར་སྣང་ངོ་། །རྣམ་པ་དེ་དག་བདག་གི་ཡིན་པར་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་འདི་ནི་ཕུང་པོ་རྣམས་ལ་འཛིན་པར་ཤེས་སོ། །

[Block 5040]
བདག་ལ་ཕན་འདོགས་པའི་ལུས་ལ་ཡང་བདག་ཉེ་བར་འདོགས་ཏེ། དཔེར་ན་བདག་གང་ཡིན་པ་དེ་ཉིད་བདག་གི་བྲན་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་བཞིན་ནོ་ཕན་འདོགས་པ་ལ་བདག་ཉེ་བར་འདོགས་པ་ཡིན་ཡང་བདག་ཏུ་འཛིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 5041]
ལུས་ལ་དམིགས་པ་ཡིན་ན་ཅིའི་ཕྱིར་ཕ་རོལ་གྱི་ལུས་ལ་དམིགས་པ་ཡང་མ་ཡིན། འབྲེལ་པ་མེད་པའི་ཕྱིར་ཏེ། འདི་ནི་ལུས་སམ་སེམས་གང་དང་ལྷན་ཅིག་འབྲེལ་པ་དེ་ཁོ་ན་ལ་བདག་ཏུ་འཛིན་པ་འདི་འབྱུང་གི་གཞན་ལ་ནི་མ་ཡིན་ཏེ། འཁོར་བ་ཐོག་མ་མེད་པ་ནས་དེ་ལྟར་གོམས་པའི་ཕྱིར་རོ། །

[Block 5042]
འབྲེལ་པ་ཡང་གང་ཞིག་ཡིན། རྒྱུ་དང་འབྲས་བུའི་དངོས་པོའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 5043]
གལ་ཏེ་བདག་མེད་པ༌[^3570]ན་བདག་ཏུ་འཛིན་པ་ནི་སུའི་ཡིན། འདི་ནི་དྲུག་པ་འདིའི་དོན་ཇི་ལྟ་བུ་ཡིན་ཞེས་བྱ་བ་ནས་དེ་ནི་དྲན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ཁོ་ན༌[^3571]ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དེ་ཉིད་འོངས་པ་ཡིན་ནོ། །

[Block 5044]
འདིའི་རྒྱུ་གང་ཞིག་ཡིན་ཞེ་ན། སྔོན་བདག་ཏུ་འཛིན་པས་ཡོངས་སུ་བསྒོས་པ་རང་གི་རྒྱུད་ཀྱི་ཡུལ་ཅན་མ་རིག་པ་དང་བཅས་པའི་སེམས་ཡིན་ནོ། །

[Block 5045 [HEADING]]
#### བདེ་བའམ་སྡུག་བསྔལ་བ། ^6-3-9-0
--- END BLOCKS ---
