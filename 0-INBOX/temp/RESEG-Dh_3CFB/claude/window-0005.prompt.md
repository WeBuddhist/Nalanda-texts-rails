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
འགའ་ཞིག་ལ་དེ་ལོག་སྟེ།[^110] སྲོག་ལ་སོགས་པ་ལོག་ཀྱང་འབྲེལ་པ་མེད་པའི་ཕྱིར། ཐམས་ཅད་ལས༌[^111]ལྡོག་པ༌[^112]མི་འགྲུབ་པས་རྟོགས་པར་བྱེད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 177]
གང་ཡང་མ་གྲུབ་པའི་སྦྱོར་བ་དེ་བཞིན་དུ་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་། མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཡང་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ། མ་གྲུབ་སྦྱར་བ༌[^113]དེ་ཡང་བརྗོད་བྱ་མིན། །མི་དམིགས་པ་ཁོ་ནར་ཟད་ན་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་ཏེ། དམིགས་ན་དེ༌[^114]མེད་པའི་ཕྱིར་རོ། །

[Block 178]
མི་དམིགས་པའི་ཕྱིར་ལྡོག་གོ་ཞེས་བྱས་ན་ཐེ་ཚོམ་དུ་གྱུར་པ་ཡང་མ་བཟློག་པར་འགྱུར་རོ། །

[Block 179]
གལ་ཏེ་ཅི་རིགས་པར་ཞེས་སྨོས་པ་ཕྱིར་མ་ལྡོག་པ༌[^115]ཁོ་ན་ཡིན་ནོ། །

[Block 180]
ཞེ་ན། ཅི༌[^116]ཡིན་ཏེ། བརྗོད་པ་གང་ཞིག་གཉི་ག་ལ་ངེས་པ་ཁོ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 181]
དེའི་ཕྱིར་མི་དམིགས་ཀྱང་ཐེ་ཚོམ་ཟ་བས་ལྡོག་པ་མེད་པར་དགོས༌[^117]ཏེ། དེ་དགག་པར་བཤད་པ་ཡིན་ནོ། །

[Block 182]
གཞན་ཡང་།

[Block 183 [VERSE]]
ཁྱད་པར་རྣམ་པར་གཅོད་པ་ཡི། །
གཏན་ཚིགས་སུ་འགྱུར༌[^118]མ་མཐོང་ཕྱིར། །

[Block 184]
མཉམ་པར༌[^119]བྱ་བ་ཉིད་ཀྱང་རྟག་པ་དང་མི་རྟག་པ་དག་ལ་མ་མཐོང་བའི་ཕྱིར་ལྡོག་པས། དེ་དག་རྣམ་པར་གཅོད་པའི་གཏན་ཚིགས་ཉིད་དུ་འགྱུར་རོ། །

[Block 185]
རྣམ་པར་གཅོད་པ་ནི་དེ་དག་ལས་ལྡོག༌[^120]པ་ལས་གཞན་པ༌[^121]ཡིན་ནོ། །

[Block 186]
རྣམ་པར་གཅོད་པ་མ་ཡིན་པ་ནི་གང་ལས་ཀྱང་ལོག་པ་ཉིད་དུ་མ་ངེས་པའི་ཕྱིར་རོ། །

[Block 187]
གང་ཞིག་གང་ལ་མེད་དོ་ཞེས་བྱ་བར་ངེས་པ་དེ་ཡོད་ན་ཇི་ལྟར་དེ་མེད་པར་རྟོགས་པར་མི་བྱེད་དེ། གལ་ཏེ་ཚད་མ་གཞན་གྱིས་གནོད། །ཅི་སྟེ་གཉི་ག་རྣམ་པར་གཅོད་པ་ཡིན་ན་གནོད་པར་བྱེད་པའི་ཚད་མ་གཞན་ཡོད་དོ། །

[Block 188]
ཕན་ཚུན་རྣམ་པར་གཅོད་པའི་ངོ་བོ་ཅན་རྣམས་ནི་གཅིག་རྣམ་པར་གཅོད་པས་གཞན་སྒྲུབ་པའི་ཕྱིར་དགག་པ་མ་ཡིན་ཏེ། སྒྲུབ་པ་དང་དགག་པ་དག་ནི་འགལ་བའི་ཕྱིར་རོ་ཞེ་ན། ད་ནི་མ་མཐོང་ལས་མེད་མིན། །དེ་ལྟར་ན་མ་མཐོང་བ་ནི་ཚད་མ་མ་ཡིན་ཏེ། གནོད་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 189 [VERSE]]
དེ་བཞིན་དུ་ནི་གཞན་ལ་ཡང་། །
ཚད་མ་གཞན་གྱིས་གནོད་པ་སྲིད། །

[Block 190]
མཚན་ཉིད་དང་ལྡན་པ་ལ་གནོད་པ་སྲིད་ན། དེའི་མཚན་ཉིད་སུན་ཕྱུང་བ་ཁོ་ནར་འགྱུར་བས་ཐམས་ཅད་ལ་ཡིད་བརྟན་དུ་མི་རུང་ངོ་། །གལ་ཏེ་རྗེས་སུ་དཔག་པའི་ཡུལ་ལ་ཡང་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དང་འགལ་བ་མཐོང་བས་ཡིད་བརྟེན༌[^122]དུ་མི་རུང་བར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། ཇི་སྐད་བཤད་པ་ལྟ་བུ་ལ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 191]
སྲིད་ན་ནི་དེའི་མཚན་ཉིད་ཀྱང་མ་ཡིན་པའི་ཕྱིར། གལ་ཏེ་འགལ་བ་འཁྲུལ་པ་མེད་པ་ཅན་གྱི་བརྗོད་པར་འགྱུར་རོ་ཞེ་ན། རྗེས་སུ་དཔག་པའི་ཡུལ་ལ་མ་བརྗོད་པའི་ཕྱིར་འདོད་པ་ཡིན་ཏེ། འདིའི་ཡུལ་ནི་བསྟན་པར་བྱའོ། །

[Block 192]
གཞན་ཡང་།

[Block 193 [VERSE]]
མ་མཐོང་ཕྱིར་རེག་མཐོང་བ་དང་། །
མི་ལྡན་འཁྲུལ་པ་མེད་པ་ཅན། །

[Block 194]
གལ་ཏེ་མི་དམིགས་པས་ལྡོག་པ་འགྲུབ་པར་འགྱུར་ན། གལ་ཏེ་མ་མཐོང་བ་ཙམ་གྱིས་མཆོང་བ༌[^123]ལ༌[^124]ལས་འགོག་པར་བྱེད་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ་ཞེས་གང་བཤད་པ་ཇི་ལྟར་རིགས་པ་མ་ཡིན་ཏེ། མི་དམིགས་པས་མེད་པ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 195]
རེག་པ་དམིགས་པའི༌[^125]མཚན་ཉིད་ཀྱིར་གྱུར་པ་དགག་པ་རིགས་པ་ཁོ་ན་མ་ཡིན་ནམ་ཞེ་ན། རིགས་པ་མ་ཡིན་ཏེ། སྣང་བ་དང་དེའི་རང་བཞིན་གྱི་ཡུལ་ཙམ་ལ་འགོག༌[^126]པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 196]
དེས་ནི་ས་ལ་སོགས་པ་སྤྱིར་བཟུང་ནས་དགག་པ་སྨྲས་སོ། །

[Block 197]
དེ་ལ༌[^127]ཤིང་བལ་དང་རྡོ་བ་དང་ལོ་མ་ལ་སོགས་པ་ལ་དེ་ཡོད་ཀྱང་རེག་པ་ཐ་དད་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 198]
འདི་ཡང་ཁྱད་པར་འགའ་ཞིག་ལ་སྲིད་པར་དགོས་པར་འགྱུར་བས་ཐམས་ཅད་ལ་ནི༌[^128]མཐོང་བས་དགག་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 199]
དེ་ལྟར་ན་སློབ་དཔོན༌[^129]མི་དམིགས་པས་མེད་པ་སྨྲ་བ་འགའ་ཞིག་གིས་ཀླན་ཀ་བཙལ་བ་ཡིན་ནོ། །

[Block 200]
གཞན་ཡང་།

[Block 201 [VERSE]]
ཡུལ་ལ་སོགས་པའི་ཁྱད་པར་ལས། །
རྫས་ལ་ནུས་པ་ཐ་དད་སྣང་། །

[Block 202]
དེ་ལ་གཅིག་མཐོང་བས་གཞན་ན་དེ་ཡོད་པར་ངེས་པར་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 203]
གལ་ཏེ་ཇི་ཞིག་ལྟར་མི་མཐུན་པའི་ཕྱོགས་ལ༌[^130]མཐོང་བ་ཙམ་གྱིས་འབྲེལ་པ་མེད་པ་ཡང་དེ་འཁྲུལ་པ་མེད་དོ་ཞེ་ན། ཡུལ་འགའ་ཞིག་ན་རྫས་ཁ་ཅིག་ཅི་ཞིག་ལྟར་མཐོང་བ་གཞན་ན་གཞན་དུ་ཡང་སྣང་ངོ་། །དཔེར་ན་སྨན་ཁ་ཅིག་ཞིང་ཁྱད་པར་ཅན་ལས་རོ་དང་ནུས་པ་དང་ཁྱད་པར་དུ་སྨིན་པར་བྱེད་པ་ཁྱད་པར་ཅན་དུ་འགྱུར་ལ། གཞན་ལ༌[^131]ནི་མ་ཡིན་པ་ལྟ་བུ་སྟེ། དུས་དང་ལེགས་པར་བྱ་བའི་ཁྱད་པར་ལས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 204]
ཡུལ་དེ་པ་རྣམས་ཀྱིས༌[^132]དེ་ལྟར་མཐོང་ཞེས་ཏེ། ཐམས་ཅད་དེ་ཉིད་དུ་དེ་ལྟ་བུ་ཡིན་པར་ནི་འགྲུབ་པར་མི་འགྱུར་ཏེ། ཡོན་ཏན་གྱི་ཁྱད་པར་རྣམས་ནི་རྒྱུའི་ཁྱད་པར་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 205]
རྒྱུའི་ཁྱད་པར་མེད་ན་ནི་རྗེས་སུ་དཔག་ཏུ་རུང་སྟེ། བྱེད་པ་པོ་མ་མཐོང་བ་ཅན་གྱི་ཚིག་ཀྱང་སྐྱེས་བུའི་འདུ་བྱེད་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་ཏེ། ཚིག་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 206]
རྣམ་པ་ཐམས་ཅད་སྐྱེས་བུ་དག་གིས་བྱེད་པར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 207]
ལེགས་པར་བྱ་བའི་བྱེ་བྲག་ལས་ཁྱད་པར་རྟོགས་པའི་ཕྱིར། ཡོན་ཏན་ཐམས་ཅད་ལ་ཁྱད་པར་མཐོང་བས་ན་གང་གིས་ན་ཚིག་ལ་སོགས་པ་ཅུང་ཟད་ཙམ་ཆོས་མཐུན་པས་རྣམ་པ་ཐམས་ཅད་དུ་མཐུན་པར་རྗེས་སུ་དཔག་པར་འགྱུར་བ་དེ་ལྟ་བུར་སྐྱེས་བུ་དག་ནི་རྒྱུའི་ཁྱད་པར་མེད་པ་ཅན་མ་ཡིན་པ་ཉིད་དོ། །

[Block 208]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་སྲིད་པའི་ཕྱིར་རོ། །

[Block 209]
མི་སྲིད་པར་རྗེས་སུ་དཔག་པ༌[^133]ཡང་གནོད་པར་བྱེད་པའི་གཏན་ཚིགས་མེད་པའི་ཕྱིར་ཏེ། འདོད་ཆགས་དང་བྲལ་བ་མ་མཐོང་བའི་ཕྱིར་ལ། མ་མཐོང་བར༌[^134]ཡང༌[^135]གནོད་པར་བྱ་བ་དང་། གནོད་པར་བྱེད་པའི་དངོས་པོ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 210]
འདོད་ཆགས་ལ་སོགས་པའི་འབྲས་བུ་འཁྲུལ་པ་མེད་པ་ཅན་མེད་པའི་ཕྱིར་རོ། །

[Block 211]
སྲིད་ཀྱང་ཁྱད་པར་རྣམས་བལྟ་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 212]
དེ་ལྟ་བུ་དག་ནི་སྤང་བར་འོས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 213]
ཚིག་རྣམས་ནི༌[^136]དེ་ལྟ་བུ་མ་ཡིན་ཏེ། ཁྱད་པར་བལྟར་རུང་བའི་ཕྱིར་རོ། །

[Block 214]
བལྟར་མི་རུང་བ་ཞིག༌[^137]ཡིན་ན་ཡང་ཁྱད་པར་མ་མཐོང་བ་རྣམས་རིགས་མི་མཐུན་པ་ཉིད་དུ་ཁས་ལེན་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 215]
དེའི་ཁྱད་པར་རྣམས་ནི་གཞན་ལ་ཡང་བྱ་བར་ནུས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
