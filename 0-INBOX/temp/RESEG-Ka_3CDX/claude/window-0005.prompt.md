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
[Block 176]
པེའི་ལུ་ཀ་ན་རེ་སྤྱི་ནི་ཐམས་ཅད་ན༌[^151]ཡོད་པ་ཡིན་ཏེ། གསལ་བ་དག་དང་དེ་དག་གི༌[^152]སྟོང་བ་ཐམས་ཅད་ན་ཡོད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 177]
པེའི་ཐ་ར་ན་རེ་དེ་ནི་གསལ་བ་ཐམས་ཅད་ན་ཡོད་པ་ཡིན་གྱི།[^153] བར་གྱི་ཡུལ་ལ་ཡོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 178 [HEADING]]
### དཔེ་ལྟར་སྣང་བ། ^5-6-0

[Block 179]
རིགས་པ་ཅན་ལ་སོགས་པ་ནི་མཚན་ཉིད་གསུམ་པའི་གཏན་ཚིགས་ལས་མ་གཏོགས་པ་དཔེ་ཞེས་བྱ་བ་སྒྲུབ་པའི་ཡན་ལག་ཡོད་དོ་ཞེས་ཟེར་ཏེ། དེ་བསལ་བའི་ཕྱིར། མཚན་ཉིད་གསུམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 180]
གཞན་གྱིས༌[^154]རབ་ཏུ་སྦྱར་བའི་དཔེ་ཁ་ཅིག་ཀྱང་སྐྱོན་ཅན་ཉིད་དུ་བརྗོད་པའི་ཕྱིར། དཔེ་ལྟར་སྣང་བ་ཉེ་བར་བཀོད་དེ།[^155] བྱེ་བྲག་པ་ལ་སོགས་པའི་ལྟར་ན་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྟག་པ་ཡང་ཡིན་ལ་ལུས་ཅན་ཡང་ཡིན་ཏེ། ལུས་ཅན་ནི་རྫས་ཐམས་ཅད་ན་ཡོད་པ་མ་ཡིན་པའི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 181]
ལས་ནི་ལུས་ཅན་ཡང་མ་ཡིན་ལ་མི་རྟག་པ་ཡང༌[^156]ཡིན་ནོ། །

[Block 182]
བུམ་པ་ནི་མི་རྟག་པ༌[^157]ཡིན་ལ་ལུས་ཅན་ཡང་ཡིན་ནོ། །

[Block 183]
སེར་སྐྱ་ལ་སོགས་པ་ནི་འདོད་ཆགས་དང་ལྡན་པ་ཡིན་ཏེ་སྨྲ་བའི་ཕྱིར་ལམ་པོའི༌[^158]ཆེའི་མི་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྒྱལ་དཔོག་པ་རྣམས་ཀྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 184]
བྱེ་བྲག་པ་ལ་སོགས་པ་ན་རེ། སྒྲ་མི་རྟག་པ་སྟེ་བྱས་པའི་ཕྱིར་བུམ་པ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 185]
[^159]དེ་དག་ཉིད་རྗེས་སུ་འགྲོ་བ་རབ་ཏུ་བསྟན་པའི་གཏན་ཚིགས་ཀྱང་རབ་ཏུ་སྦྱོར་བར༌[^160]བྱེད་དོ། །

[Block 186]
སེར་སྐྱ་ལ་སོགས་པ་ཐམས་ཅད་མཁྱེན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ནམ་མཁའི་གོས་ཅན་རྣམས་ཀྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 187]
གསུམ་རིག་པའི༌[^161]བྲམ་ཟེས་ནི་མི་འགའ་ཞིག་གིས་བརྗོད་པར༌[^162]འདོད་པའི་ཚིག་གཟུང་བར་མི་བྱ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བྲམ་ཟེ་རྣམས་ཀྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 188]
སེར་སྐྱ་ལ་སོགས་པ་ནི་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ནམ་མཁའི་གོས་ཅན་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 189]
སྨྲ་བའི་ཕྱིར་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དཔྱོད་པ༌[^163]པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 190]
སྒྲ་ནི་མི་རྟག་པ་ཉིད་དེ༌[^164]བྱས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་པ་ཅན་གྱི་ཡིན་ནོ། །

[Block 191 [HEADING]]
### ལྟག་ཆོད། ^5-7-0

[Block 192]
དེ་ལ་ལྟག་ཆོད༌[^165]རྣམས་ཀྱི་དཔེར་བརྗོད་པ༌[^166]ཕྱོགས་ཙམ་ཞིག་བརྗོད་པར་བྱ་སྟེ། དཔེར་ན་མི་རྟག་པ་ཉིད་ལ་སོགས་པ་ནི༌[^167]བསྒྲུབ་པར་བྱས་པ་ཉིད་དང་བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ལ་སོགས་པ་ཡང་དག་པར་སྦྱར་ཀྱང་ལྟག་ཆོད་སྨྲ་བས་རྒོལ༌[^168]བ་ཁྱོད་ཀྱི་གཏན་ཚིགས་འདི་ཅི་བསྒྲུབ་པར་བྱ་བ་དང་ཕྲད་ནས་སྒྲུབ་པར་བྱེད་དམ་འོན་ཏེ་མ་ཕྲད་ནས། གལ་ཏེ་ཕྲད་ནས་ཡིན་ན་ནི། དེའི་ཚེ་བསྒྲུབ་པར་བྱ་བ་དང་ཁྱད་པར་མེད་པར་འགྱུར་ཏེ། ཀླུང་གི་ཆུ་རྒྱ་མཚོ་དང་ཕྲད་པ་བཞིན་ནོ། །

[Block 193]
གཞན་ཡང་འདི་བསྒྲུབ་པར་བྱ་བ་གྲུབ་ཟིན་པ་དང་ལྷན་ཅིག་ཕྲད་པར་འགྱུར་རམ། མ་གྲུབ་པ་དང་ཕྲད། རེ་ཞིག་མ་གྲུབ་པ་དང་ནི་མ་ཡིན་ཏེ། རི་བོང་གི་རྭ་བཞིན་མེད་པའི་ཕྱིར་རོ། །

[Block 194]
བསྒྲུབ་པར་བྱ་བ་གྲུབ་ཟིན་ན་ཡང་འདི་གང་གི་གཏན་ཚིགས་ཡིན་པར་འགྱུར། དེའི་ཕྱིར་ཕྲད་པའི་ཕྱོགས་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 195]
ཡང་མ་ཕྲད་ཅེས་བྱ་བའི་ཕྱོགས་ཀྱང་མ་ཡིན་ཏེ། གཏན་ཚིགས་མ་ཕྲད་པ་རྣམས་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་ནོ། །

[Block 196]
འདི་ནི་ཕྲད་པ་དང་མ་ཕྲད་པ་མཚུངས་པ་ཞེས་བྱ་བའི་ལྟག༌[^169]ཆོད་ཡིན་ཏེ། རིགས་པ་མེད་པས་གཏན་ཚིགས་སུན་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 197]
གང་ལ་ཕྲད་པ་དང་མ་ཕྲད་པར༌[^170]ཡོད་པར་ཆོས་མཐུན་པ་ཙམ་གྱིས་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པ་ཡང་གཏན་ཚིགས་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ལ་རིགས་པ་ཅི་ཞིག་ཡོད། ཆུ་དང་འབྱུང་བ་ཉིད་ལ་སོགས་པར་ཆོས་མཐུན་པའི་ཕྱིར་མེས་མི་བསྲེག་པ༌[^171]ནི་མ་ཡིན་ནོ། །

[Block 198]
བསྒྲུབ་པར་བྱ་བ་ཡང་རི་བོང་གི་རྭ་བཞིན་དུ་ཤིན་ཏུ་མ་གྲུབ་པ་ཉིད༌[^172]མ་ཡིན་ནོ། །

[Block 199]
འོ་ན་ཅི་ཞེ་ན། ངེས་པ་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 200]
ཁྱོད་ཀྱིས་སུན་འབྱིན་པ་ལ་ཡང་ཀླན་ཀ་འདི་ཐམས་ཅད་མཚུངས་པས་སུན་འབྱིན་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 201]
དེ་ལྟ་བས་ན་འདྲི་བ་ལོག་པ་དེ་ལྟ་བུ་དག་ལ་མཐའ་མེད་པས།[^173] དེ་དག་གི་མཚན་ཉིད་ལོགས་ཤིག་ཏུ་བརྗོད་པར་མི་བྱ་སྟེ། ཚད་མའི་མཚན་ཉིད་ཇི་སྐད་བཤད་པ་ངེས་པར་གཟུང་བ་ཁོ་ནས་དེ་དག་བསལ་བ༌[^174]ཉིད་དོ་སྙམ་དུ་བསམས་པ༌[^175]ཡིན་ནོ། །

[Block 202 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 203 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 204]
རིགས་པའི་ཐིགས་པའི་ཕྱོགས་སྔ་མ་མདོར་བསྡུས་པ། སློབ་དཔོན་མང་དུ་ཐོས་པ་ཀ་མ་ལ་ཤཱི་ལས་མཛད་པ་རྫོགས་སོ།། །།

[Block 205 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 206]
རྒྱ་གར་གྱི་མཁན་པོ༌[^176]ཤུདྡྷ་སིཾ་ཧ་དང་། ཞུ་ཆེན་གྱི་ལོ་ཙཱ་བ་དགེ་སློང་དཔལ་བརྩེགས༌[^177]རཀྵི་ཏས་བསྒྱུར་ཏེ་གཏན་ལ་ཕབ་པའོ། །
--- END BLOCKS ---
