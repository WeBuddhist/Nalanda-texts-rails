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
[Block 211]
ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་འདི་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་བཀན་པ་ཉིད་དང་རྐང་རྟེན་བཅུག་པ་ཉིད་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལས་ཐོག་ཉིད་དང་རྩ་བ་ཕུར་བུ་ལྟ་བུ་ཉིད་དེ་གཉིས་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གནོན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མནན་པར་འོས་པ་ཞེས་བྱ་བ་དབང་དུ་བྱེད་པ་ལས་ཤེས་པར་བྱེད་དོ། །

[Block 212]
མངོན་པར་འདུག་པར་བྱ་བའམ། མངོན་པར་འདུག་པ་ཞེས་བྱ་བ་འདིར་འདུག་པ་ཙམ་ནི་གཙོ་བོར་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བ་འདི་ལྟར་ཉེ་བར་བརྟག་པར༌[^148]བྱའོ། །

[Block 213]
ཅི་ཞིག་ཅི་ཡང་རུང་བ་ཉིད་ཀྱིས་དེ་གཉིས༌[^149]ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བའི་རྣམ་པས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 214]
འདིར་གཞུང་ནི་དགེ་སློང་གང་ཤེས་བཞིན་དུ་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 215]
རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་འདིར་རང་ཉིད་ཀྱིས་རིག་པར་གྱུར་པའམ་གཞན་དག་གིས་བརྗོད་པས་སོ་ཞེས་གསུངས་སོ། །

[Block 216]
དགེ་སློང་གནོན་པར་བྱས་པའི་གླེང་གཞི་དང་སྦྱིན་པ་གཅད་པའི༌[^150]ཕྱིར་འདི་རྣམས་བརྟགས་པའོ། །

[Block 217]
རྩ་བ་འབྱུང་བ་ལ་འདུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 218]
ཡང་གང་ཞིག་བསླབ་པའི་གཞི་འདི་ལ་ཡང་དགེ་སློང་གང་ཤེས་བཞིན་དུ་སྲོག་ཆགས་དང་བཅས་པའི་ཆུས་རྩྭའམ༌[^151]ཞེས་བྱ་བ་དང་། གང་ཞིག་ཡང་སླར་ཤེས་བཞིན་དུ་སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་སྤྱོད་ན་ཞེས་བྱ་བ་གཅིག་པོ་ཉིད་གཉིས་སུ་འགྱུར་ཏེ། ཡུལ་གྱི་བྱེ་བྲག་གིས་ནི་དེ་གཉིས་ལྟུང་བ་ཐ་དད་པ་ཉིད་ཡིན་པས་གང་ཞིག་དེར་ཆོ་ག་དེ་ཉིད་ཅེས་བྱ་བ་མངོན་པར་བརྟེན་ནས་ཡུལ་གང་ལ་འདི་དང་དེ་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། རང་སྤྱོད་པའི་དོན་ཉིད་དེ་ལས་གཞན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་སྤྱོད་པ་ཉིད་གཞག་པར་བྱ་བ་གཞན་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་དེ་ལ་ནི་སྲོག་ཆགས་དང་བཅས་པ་ལ་སྤྱོད་པ་ཞེས་བྱ་བའི་ལྷག་མ་དེ་ཉིད་ལས་རྟོགས་པར་བྱའོ། །

[Block 219]
སྲོག་ཆགས་དང་བཅས་པ་ལ་སྤྱོད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 220]
སྒོ་ཆ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྒོ་ཆ་ཞེས་བྱ་བ་ནི་སྒོ་སྐྱེས༌[^152]ལ་སོགས་པ་སྒོ་དང་འབྲེལ་པའི་ཡོ་བྱད༌[^153]དོ། །

[Block 221]
འདི་ལྟར་ཡ་ཕུབས་ལས་གཞན་སྒོ་སྐྱེས༌[^154]བཟུང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་རྟོགས་པར་བྱའོ། །

[Block 222]
སྒོ་གླེགས་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ན༌[^155]འདིར་སྒོ་གླེགས་ཞེས་བྱ་བ་སྒོ་ལེབ་ལ་བྱ་སྟེ། དེ་ཡང་སྒོ་གླེགས་ཞེས་སྨོས་པའི་ཚིག་གིས་སོ། །

[Block 223]
སྐར་ཁུང་དག་ཀྱང་གདོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འཇུག་པར་བྱའོ། །

[Block 224]
ལྟུང་བ་འདི་ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཙུག་ལག་ཁང་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 225]
འདི་ལ་ཚད་ཇི་ཙམ་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྤྱོད་ལམ་བཞི་ཤོང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་སྤྱོད་ལམ་རྣམ་བཞི་བྱར་རུང་ཞིང་ཤོང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 226]
ཅི་གཙུག་ལག་ཁང་ཚད་དེ་ཙམ་དང་ལྡན་པ་ཐམས་ཅད་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཐམས་ཅད་རྡོའམ་སོ་ཕག་གམ་ཤིང་ལས་བྱས་པ་མ་ཡིན་ནའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད༌[^156]དུ་གཙུག་ལག་ཁང་ལ་ཡང་ད་ལྟར་ཁྱིམ་ལ་དབང་བ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་རྟོགས་པའོ། །

[Block 227]
འདིར་བྱེ་བྲག་གཞན་ཡང་བརྗོད་པར་བྱ་སྟེ། ཆར་ཆུ་བསྐྱབ་པའི་གཡོགས༌[^157]མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཐམས་ཅད་ཉི་མ་རེ་རེ་ཞིང་བྱ་བ་བྱས་པ་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 228]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་དག་ཡོད་དེ། རྩིག་པ་རིམ་པ་གཉིས་སམ་གསུམ་ལས་ལྷག་པར་རྩིག་ཅིང་དེ་ལ་ལྟུང་བྱེད་དུ་ཡང་མི་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་རྩྭ༌[^158]དག་གིས་གཡོགས་པར༌[^159]བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 229]
སྤང་ལེབ་དག་གིས་གཡོགས་པར༌[^160]བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 230]
ཤིང་ལེབ་དག་གིས་གཡོགས་པར༌[^161]བྱེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 231]
རྩ་བའི་ལྟུང་བ་འབྱིན་པར་བྱེད་ན་ཐམས་ཅད་ལ་འདི་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ་དེའི་ཕྱིར་ཡོན་བདག་གིས་བྱས་སམ་ཟིན་ནམ་བལྟའོ་ཞེས་མ་སྨྲས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 232]
སྨྲས་པ་ལ་ནི་ཉེས་པ་མེད་པ་ཉིད་ཡིན་ནོ། །གང་ལ་དེ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཕ་གུ༌[^162]རིམ་པ་གསུམ་ལས་ལྷག་པ་ལའོ་ཞེས་བྱ་བ་སྨྲས་སོ། །ཅི་བདག་ཉིད་ཁོ་ནས་སམ་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་བྱེད་དུ་བཅུག་ན་ཡང་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་གི་ཚེ་བརྩིགས་ཤེ་ན། དེའི་ཕྱིར་ཉི་མ་དེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉི་མ་གང་ལ་རིམ་པ་གསུམ་བརྩིགས་པའི་ཉི་མ་དེ་ཉིད་ལ་གལ་ཏེ་ལྷག་པར་བརྩིགས་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 233]
རིམ་པ་གང་དང་གང་ལ་ཉི་མ་གཞན་ལ་བརྩིགས་པ་ཉིད་དེ་ལ་ནི་འདིར་གྲངས་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 234]
གཞན་ལ་ཡང་འཇིམ་པ་མེད་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་ཉི་མ་གཞན་ལ་ཡང་ཕ་གུ་འཇིམ་པ་མེད་པ་གསུམ་ལས་ལྷག་པར་བརྩིག་པ་བྱས་ན་ཞེས་བྱ་བའི་དོན་ཏོ།[^163] །བར་དུ་ཆོད་པ་ཕ་གུ་འཇིམ་པ་མེད་པ་ལ་འདིར་བགྲང་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་དོན་གྱིས་རྟོགས་པའོ། །

[Block 235]
ཆུ་ཁུང་དག་མ་བཏོད་པ༌[^164]ཡང་རུང་ངོ་ཞེས་བྱ་བ་ནི་ཉི་མ་གཞན་ལ་ཡང་ཕ་གུ་རིམ་པ་གསུམ་ལས་ལྷག་པར་བརྩིག་པར་བྱས་ནས༌[^165]གཞན་ལ་ཡང་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 236]
གང་ཞིག་རྟེན་གྱིས་རིགས་པ་ལས་མ༌[^166]འདས་པའི་ཆུ་ཁུང་བཏོད་པའི༌[^167]གནས་ཡན་ཆད་ནས་འདིར་རིམ་པ་གསུམ་བགྲང་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་དོན་གྱིས་རྣམ་པར་གཞག་པའོ། །

[Block 237]
བརྐོས་ཏེ་རྩ་བ་མ་བཙུགས་པ༌[^168]ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཉི་མ་གཞན་ལ་ཡང་ཕ་གུའི་རིམ་པ་གསུམ་ལས་ལྷག་པར་བརྩིག་པར༌[^169]བྱ་བ་ལ༌[^170]གཞན་གྱིས་ཀྱང་ཐོག་མ་ནས་བརྩམས་ཏེ། འདིར་བགྲང་བར་བྱ་བ་ཉིད་ནི་རིམ་པ་རེ་རེར་བྱེད་དུ་བཅུག་ན་ཡང་དངོས་གཞིར་རིག་པར་བྱའོ། །གང་ལ་མི་སྦྱིན་པ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བརྐོས་ཏེ་རྩ་བ་མ་བཙུགས་པ༌[^171]ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་སྟེ། བརྐོས་ཏེ་རྨང་གི་རྩ་བ༌[^172]འཛུགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 238]
སྒོ་ཆ་གོང་མ་མ་བཅུག་པ་ལས༌[^173]ཡང་རུང་ངོ་ཞེས་བྱ་བ་ནི། རིམ་པ་གསུམ་ལས་ལྷག་པར་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 239]
ཇི་སྲིད་དུ་སྒོ་ཆ་གོང་མ་འགེབས་པར་འདོད་པས་ཕ་གུའི་རྟེན་བཙུགས་པ༌[^174]དེ་འདིར་གཅིག་གམ་དུ་མ་སྨོས་པ་ཞེས་བྱ་བ་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 240]
ཕྱོགས་དེ་ནས་བརྩམས་ཏེ་བགྲང་བ་ཉིད་ཅེས་བྱ་བ་ཡང་ངོ་། །རྩིག་པ་གཞན་གསུམ་ལ་འདིར་རིམ་པ་མ་ཡིན་པ་སྦྱོར་བ་ལ་ཉེས་བྱས་ཀྱི་སྦྱོར་བ་ཐམས་ཅད་ལ་ཉེས་བྱས་ཐམས་ཅད་དུ་ཞེས་བྱ་བ་དེ་ཐོས༌[^175]པའོ། །

[Block 241]
དེ་ཡང་ཉི་མ་དང་པོ་ནས་ཞེས་བྱ་བ་བསྟན་པའི་མཚན་མ་ལས་སྔ་མ་ཉིད་ཀྱིས་གསུམ་ལ་བརྟེན་ནས་དགག་པར་བྱའོ། །

[Block 242]
དང་པོའི་མདུན་རོལ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ཡང་ལྟུང་བའི་རྒྱུར་གྱུར་པ་ལས་དང་པོ་གསུམ་ལས་རིམ་པ་ལྷག་པར་རྩིག་པ༌[^176]ལ་དེ་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 243]
གཙུག་ལག་ཁང་གི་ལྟུང་བྱེད་དོ།། །།

[Block 244]
ཕམ་པར་གྱུར་པ་མ་བྱུང་བ་མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་ལོ་ཉི་ཤུ་ལས་མི་ཉུང་བ་གྲོང་ཁྱེར་པའི་སྐད་སྨྲ་བ་དགེ་སློང་མ་ལ་ལུས་ཉེ་བར་གཞོལ་བ་ཉིད་ཀྱི་ཕྱིར་བཅོས་པ་བྱས་པ་དགེ་སློང་མའི་སྟོན་པར་བསྐོའོ༌[^177]ཞེས་བྱ་བ་ནི༌[^178]གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལ་མཚམས་ཀྱི་ནང་དུའོ། །

[Block 245]
ཕམ་པར་འགྱུར་བ་མ་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཕམ་པར་འགྱུར་བའི་ལྟུང་བ་མ་བྱུང་བའོ། །

[Block 246]
ལོ་ཉི་ཤུ་ལས་མི་ཉུང་བ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཚིག་འདིས༌[^179]ནི་རྒྱལ་ཚབ༌[^180]ལྟ་བུ་ཞེས་བྱ་བ་མངའ༌[^181]བདག་ཉིད་དང་བདག་པོ་དང་ལྡན་པ་ཉིད་དེའི་དོན་ཏོ། །

[Block 247]
གནས་བརྟན་ཉིད་ཀྱི་བདག་པོ་ཉིད་གང་ཡིན་པ་དེ་ནི་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་གནས་བརྟན་གྱི་རྣམ་གྲངས་ཉིད་ཀྱིས་བརྗོད་པར་རྟོགས་པའོ། །

[Block 248]
གྲོང་ཁྱེར་བའི་སྐད་སྨྲ་བ་ཞེས་བྱ་བ་ནི་སྒྲ་མཁས་པ་སྟེ་རིགས་པ་དང་གྲོལ་བར་སྨྲ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 249]
རང་བཞིན་ཉིད་ཀྱིས༌[^182]གཞན་གང་ཞིག་སྤང་བ་རྣམས་ལ་བདག་གིས་བརྩམས་པ་གང་ཞིག་སྤོང་བ་རྣམས་ལ་ཁྱོད་ཀྱི་ལས་ཏེ། འདི་སྐད་ཅེས་གང་ཞིག་སྤང་བར་བྱ་བ་ཉིད་བདག་གིས་སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་མི་ནུས་པ་ལ་མཐོ་བཙམས༌[^183]པ་ཞེས་བྱ་བ་དེ་ལ་བརྟེན་པའོ། །

[Block 250]
དགེ་སློང་མ་ལ་ལུས་ཉེ་བར་གཞོལ་བ་ཉིད་ཀྱི་ཕྱིར་བཅོས་པ་བྱས་པ་ཞེས་བྱ་བ་ལ། [^184]འདིར་གཞི་ནི་འདིས༌[^185]དགེ་སློང་མ་ལུས་ཉེ་བར་འདྲེས་པས་སྐྱོན་ཅན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
