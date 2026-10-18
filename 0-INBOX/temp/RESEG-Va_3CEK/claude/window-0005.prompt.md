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
སྦྱར་བའི་ཆང་ནི་རྫས་ལས་སྦྱར་བའི་བཏུང་བའོ། །

[Block 177]
དེ་དག་ཀྱང་རེས་འགའ་མྱོས་པར་འགྱུར་བའི་དངོས་པོར་མ་རེད་པའམ་ཡལ་བར་འགྱུར་བས་དེའི་ཕྱིར་མྱོས་པར་འགྱུར་བ་ཞེས་བྱ་བར་སྨོས་སོ། །

[Block 178]
གླ༌[^120]གོར་ཞོ་ཤ་དང་ཁྲེ་རྒོད༌[^121]ལ་སོགས་པ་ཡང་མྱོས་པར་བྱེད་པས་འབྲུའི་ཆང་དང་སྦྱར་བའི་ཆང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 179]
བཅས་པའི༌[^122]ཁ་ན་མ་ཐོ་བ་ཡིན་ཡང་བག་མེད་པ་ཐམས་ཅད་ཀྱི་གནས་སུ་གྱུར་པས་བསྒྲིམས༌[^123]ཏེ་སྤང་བར་བྱ་བ་ཉིད་ཡིན་པའི་རྒྱུ་ཤེས་པར་བྱ་བའི་ཕྱིར་བག་མེད་པའི་གནས་ཞེས་སྨོས་སོ། །

[Block 180 [HEADING]]
### སྡོམ་པ་གང་ལས་འཐོབ་པ། ^1-16-0

[Block 181]
ཅི་སོ་སོར་ཐར་པ་དང་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དང་གསུམ་པོ་འདི་དག་གང་ལས་གཅིག་འཐོབ་པ་དེ་ལས་ལྷག་མ་དག་ཐོབ་པའམ༌[^124]ཞེ་ན། མ་ཡིན་ནོ། །

[Block 182]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 183 [VERSE]]
འདོད་གཏོགས་ཐམས་ཅད་གཉི་ག་དང་། །
ད་ལྟར་དག་ལས་འཐོབ་པར་འགྱུར། །

[Block 184]
འདོད་གཏོགས་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡིན་ནོ། །

[Block 185]
ཐམས་ཅད་ལས༌[^125]ཞེས་བྱ་བ་ནི་སྦྱོར་བ་དང་དངོས་དང་མཇུག་ལས་སོ། །

[Block 186]
གཉི་ག་ལས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པར་སྟོན་པ་དང་། རང་བཞིན་དང་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ལས་སོ། །

[Block 187]
སེམས་ཅན་གྱི་རྟེན་ལ་འཇུག་པའི་ཕྱིར་ད་ལྟར་གྱི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཁོ་ན་ལས་འཐོབ་ཀྱི་འདས་པ་དང་མ་འོངས་པ་དག་ལས་ནི༌[^126]མ་ཡིན་ཏེ། དེ་དག་ནི་སེམས་ཅན་དུ་མི་བགྲང་བའི་ཕྱིར་རོ། །

[Block 188 [VERSE]]
བསམ་གཏན་ཟག་མེད་སྡོམ་པ་ནི། །
དངོས་དང་དུས་ནི་ཐམས་ཅད་ལ། །

[Block 189]
བསམ་གཏན་དང༌[^127]ཟག་པ་མེད་པའི་སྡོམ་པ་ནི་ལས་ཀྱི་ལམ་དངོས་ཁོ་ན་ལས་འཐོབ་ཀྱི་སྦྱོར་བ་དང་མཇུག་ལས་ཀྱང་མ་ཡིན་ན་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ལ༌[^128]ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དུས་ཐམས་ཅད་ཀྱི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལས་འཐོབ་སྟེ། འདས་པ་དང་མ་འོངས་པ་དག་ལས་ཀྱང༌[^129]འཐོབ་བོ། །

[Block 190]
དེ་ཉིད་ཀྱི་ཕྱིར་གང་དག་ལས་སོ་སོར་ཐར་པའི་སྡོམ་པ་འཐོབ་ལ་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དག་མ་ཡིན་པའི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དེ་དག་ཀྱང་ཡོད་ཅེས་བྱ་བ་རྒྱས་པར་མུ་བཞིར་འགྱུར་ཏེ། མུ་དང་པོ་ནི་ད་ལྟར་བྱུང་བའི་ཉེར་བསྡོགས༌[^130]དང་མཇུག༌[^131]དག་དང་། བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ལས་སོ། །

[Block 191]
གཉིས་པ་ནི་འདས་པ་དང་མ་འོངས་པའི་ལས་ཀྱི་ལམ་དངོས་དག་ལས་སོ། །

[Block 192]
གསུམ་པ་ནི་ད་ལྟར་བྱུང་བའི་ལས་ཀྱི་ལམ་དངོས་དག་ལས་སོ། །

[Block 193]
བཞི་པ་ནི་འདས་པ་དང་མ་འོངས་པའི་ཉེར་བསྡོགས༌[^132]དང་མཇུག་དག༌[^133]ལས་སོ། །

[Block 194]
སྡོམ་པ་འཐོབ་པའི་ཚེ་ན༌[^134]ད་ལྟར་གྱི་ལས་ཀྱི་ལམ་རྣམས་མེད་པས་ད་ལྟར་གྱི་གཞི་ཅན་ལས་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 195]
མ་འོངས་པ་རྣམས་ཁོ་ན་ལས་སྡོམ་པར་རུང་གི་འདས་པ་དང་ད་ལྟར་གྱི་རྣམས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 196]
ཡང་ཅི་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དག་སེམས་ཅན་ཐམས་ཅད་དང་། ཡན་ལག་ཐམས་ཅད་དང་། རྒྱུ་ཐམས་ཅད་ཀྱིས་འཐོབ་བམ། འོན་ཏེ་བྱེ་བྲག་ཅི༌[^135]ཡོད་ཅེ་ན། རེ་ཞིག་ངེས་པར། སྡོམ་པ་སེམས་ཅན་ཐམས་ཅད་ལས། །

[Block 197]
འཐོབ་ལ། ཡན་ལག་རྒྱུ་ལ་དབྱེ་བ་ཡོད། ། སྡོམ་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ལས་འཐོབ་པ་ཉིད་དེ་འགའ་ལས་མ་ཡིན་ནོ། །

[Block 198]
ཡན་ལག་ལས་ནི་དབྱེ་བ་ནི༌[^136]ཡོད་དེ། ལ་ལ་ནི་ཐམས་ཅད་ལས་འཐོབ་སྟེ། དགེ་སློང་གི་སྡོམ་པ་ཐོབ་པའོ།[^137] །ལ་ལ་ནི་གཞི་ལས་ཏེ་དེ་ལས་གཞན་པའོ། །

[Block 199]
ལས་ཀྱི་ལམ་རྣམས་ནི་སྡོམ་པའི་ཡན་ལག་དག༌[^138]ཡིན་ནོ། །

[Block 200]
རྒྱུ་ལས་ཀྱང་རྣམ་གྲངས་ལ་ལ༌[^139]ལས་ནི་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 201]
ལ་ལ༌[^140]ལས་ནི་གཅིག་གིས་སོ། །

[Block 202]
རེ་ཞིག་གང་གིས་ན་ཐམས་ཅད་ཀྱིས༌[^141]ཡིན་ཞེ་ན། གལ་ཏེ་མ་ཆགས་པ་དང་ཞེ་སྡང་མེད་པ་དང་གཏི་མུག་མེད་པ་རྒྱུར༌[^142]འདོད་ནའོ། །གང་གིས་ན་གཅིག་གིས་ཤེ་ན། གལ་ཏེ་སེམས་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་དག་རྒྱུར་འདོད་ནའོ། །

[Block 203]
རྣམ་གྲངས་ཐ་མ་ངེས་པ་ལ་བརྟེན་ཏེ་སྨྲས་པ། སྡོམ་པ་ལ་གནས་པ་སེམས་ཅན་ཐམས་ཅད་ལ་བསྡམས་ལ་ཡན་ལག་ཐམས་ཅད་དང་། རྒྱུ་ཐམས་ཅད་ཀྱི་མ་ཡིན་པ་ཡང་ཡོད་དེ། གང་ཞིག་སེམས་ཆུང་ངུ་འམ་འབྲིང་ངམ་ཆེན་པོས་དགེ་བསྙེན་དང་བསྙེན་གནས་པ་དང་། དགེ་ཚུལ་གྱི་སྡོམ་པ་ཡང་དག་པར་ལེན་པའོ། །

[Block 204]
སེམས་ཅན་ཐམས་ཅད་དང་། ཡན་ལག་ཐམས་ཅད་ཀྱིས་བསྡམས་ལ་རྒྱུ་ཐམས་ཅད་ཀྱི་མ་ཡིན་པ་ཡང་ཡོད་དེ། གང་ཞིག་སེམས་ཆུང་ངུ་འམ་འབྲིང་ངམ་ཆེན་པོས་དགེ་སློང་གི་སྡོམ་པ་ཡང་དག་པར་ལེན་པའོ། །

[Block 205]
སེམས་ཅན་ཐམས་ཅད་དང་ཡན་ལག་ཐམས་ཅད་དང་རྒྱུ་ཐམས་ཅད་ཀྱིས་བསྡམས༌[^143]པ་ཡང་ཡོད་དེ། གང་ཞིག་སེམས་རྣམ་པ་གསུམ་གྱིས་སྡོམ་པ་རྣམ་པ་གསུམ་ཡང་དག་པར་ལེན་པའོ། །

[Block 206]
སེམས་ཅན་ཐམས་ཅད་དང་། རྒྱུ་ཐམས་ཅད་ཀྱིས་བསྡམས་པ༌[^144]ལ་ཡན་ལག་ཐམས་ཅད་ཀྱིས་མ་ཡིན་པ་ཡང་ཡོད་དོ། །

[Block 207]
གང་ཞིག་སེམས་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་དག་གིས་དགེ་བསྙེན་དང༌[^145]བསྙེན་གནས་དང་དགེ་སྦྱོང་གི༌[^146]སྡོམ་པ་ཡང་དག་པར་ལེན་པའོ། །

[Block 208]
གང་ཞིག་སེམས་ཅན་ཐམས་ཅད་ལ་མ་བསྡམས་པ་དེ་ལྟ་བུ་ནི་མེད་དེ། འདི་ལྟར་སེམས་ཅན་ཐམས་ཅད་ཀྱི་རྗེས་སུ་སོང་བའི་སེམས་དགེ་བ་ལ་གནས་པས་སྡོམ་པ་འཐོབ༌[^147]ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། སྡིག་པའི་བསམ་པ་དང་མ་བྲལ་བའི་ཕྱིར་རོ། །

[Block 209]
ངེས་པ་ལྔ་པོ་སེམས་ཅན་དང་། །ཡན་ལག་དང་ཡུལ་དང་། དུས་དང་། ཚེ་ངེས་པ་མི་བྱེད༌[^148]ན་སོ་སོར་ཐར་པའི་སྡོམ་པ་འཐོབ་སྟེ། སེམས་ཅན་ཆེ་གེ་མོ་ཞིག་ལས་སྤོང་ངོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ངེས་པའོ། །

[Block 210]
ཡན་ལག་ཆེ་གེ་མོ་ཞིག་ལས་ཞེས་བྱ་བ་ནི་ཡན་ལག་ངེས་པའོ། །

[Block 211]
ཡུལ་ཆེ་གེ་མོ་ཞིག་ཏུ་ཞེས་བྱ་བ་ནི་ཡུལ་ངེས་པའོ། །

[Block 212]
ཟླ་བའི་བར་དུ་ཞེས་བྱ་བ་ནི་དུས་ངེས་པའོ། །

[Block 213]
འཐབ་མོ༌[^149]མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་ཚེ་ངེས་པ་སྟེ། དེ་ལྟར་མནོས་ན་ལེགས་པར་སྤྱད་པ་ཙམ་དུ་ནི༌[^150]འགྱུར་རོ། །ཇི་ལྟར་ན་མི་ནུས་པ་དག་ལས་སྡོམ་པ་འཐོབ་ཅེ་ན། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྲོག་ལ་མི་གནོད་པའི་བསམ་པས་ཁས་བླང་བའི༌[^151]ཕྱིར་རོ། །

[Block 214]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གལ་ཏེ་ནུས་པ་དག་ཁོ་ན་ལས་སྡོམ་པ་འཐོབ་ན་ནི་སེམས་ཅན་ནུས་པ་དང་མི་ནུས་པ་རྣམས་ནི་ཕན་ཚུན་འཕོ་བས་འཕེལ་བ་དང་འགྲིབ་པ་དང་ལྡན་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་འཐོབ་པ་དང་གཏོང་བའི་རྒྱུ་དག་མེད་པར་ཡང་སྡོམ་པ་འཐོབ་པ་དང་གཏོང་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 215]
དེ་ལྟར་ནི་མི་འགྱུར་ཏེ། ཇི་ལྟར་སྔོན་མེད་པའི་རྩྭ་ལ་སོགས་པ་སྐྱེས་སམ་བསྐམས༌[^152]ན་སྡོམ་པ་འཕེལ་བ་དང་འགྲིབ་པར༌[^153]མི་འགྱུར་བ་དེ་བཞིན་དུ་ནུས་པ་དང༌[^154]མི་ནུས་པ་འཕོས་སུ་ཟིན་ཀྱང་མི་འགྱུར་རོ། །
--- END BLOCKS ---
