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
[Block 246 [VERSE]]
དེ་ཕྱིར་ཆོས་མི་མཐུན་དཔེ་ལ། །
ངེས་པར་འདི་ལ་གཞི་མི་འདོད། །
དེ་དག་མེད་ནའང་དེ་མེད་ཅེས། །
བརྗོད་པ་ལས་ཀྱང་དེ་རྟོགས་ཕྱིར། །

[Block 247]
འདི་ལྟར།

[Block 248 [VERSE]]
དཔེ་ལ་དེ་ཡི་ངོ་བོ་དང་། །
རྒྱུ་དངོས་དེ་དག་མི་ཤེས་ལ། །

[Block 249]
སྟོན་ཏེ། དཔེ་ལ་ནི༌[^147]བསྒྲུབ་པར་བྱ་བའི་ཆོས་ནི་དེའི་ངོ་བོར་དེ་ཙམ་དང་འབྲེལ་པས་དེའི་རང་གི་ངོ་བོ་ཉིད༌[^148]སྟོན་ཏོ། །

[Block 250]
བྱས་པའི་ངོ་བོ་ཉིད་སྐྱེད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་མི་རྟག་པའི་ངོ་བོ་ཉིད་མེད༌[^149]ན་སྐྱེད་པར་བྱེད་དོ་ཞེས་ཚད་མ་དཔེས་རབ་ཏུ་སྟོན་ཏོ། །

[Block 251]
དེ་ལྟ་མ་ཡིན་ན་ཆོས་གཅིག་ཡོད་པའི་ཕྱིར་དེ་ལས་གཞན་པ་ཡང་ཡོད་པར་འགྱུར་རོ་ཞེས་བྱ་བར་ངེས་པ་མེད་པའི་ཕྱིར་འཁྲུལ་པར་དགོས་པར༌[^150]འགྱུར་རོ། །

[Block 252]
ཚད་མ་ངེས་ཀྱང་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཀྱི་དེ་ཙམ་དང་འབྲེལ་པ་སྟོན་ཏེ། རང་གི་རྒྱུ་ཁོ་ན་ལས་བྱས་པ་འཇིག་པའི་ངང་ཚུལ་ཅན་སྐད་ཅིག་མར་གནས་པའི་ཆོས་གང་ཡིན་པ་དེ་ལྟ་བུ་སྐྱེས་ཏེ། གཞན་ལས་དེ་ཡོད་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 253]
ཡང་ན་རྒྱུའི་དངོས་པོར་ཏེ། ཡོད་པ་ཉིད་ཡིན་ན་ཡོད་པའི་ཕྱིར་རོ་ཞེས་དོན་གཞན་རབ་ཏུ་སྟོན་ཏོ། །

[Block 254]
[^151]

[Block 255]
དེ་ལྟར་དེའི་ངོ་བོ་དང་རྒྱུའི་དངོས་པོ་རབ་ཏུ་གྲུབ་ན་མི་རྟག་པ་ཉིད་མེད་ན་བྱས་པ་ཉིད་མེད་ལ་མེ་མེད་ན་ཡང་དུ་བ་སྟེ། འདི་ལྟར་དེ་ནི་རང་གི་ངོ་བོ་དང་རྒྱུ་ཡིན་ན། ཇི་ལྟར་རང་གི་ངོ་བོ་དང་རྒྱུ་མེད་པར་ཡོད་པར་འགྱུར། དེ་བས་ན་གཞི་མེད་པ་ཡང་ཆོས་མི་མཐུན་པའི་དཔེ་ལ་ལྡོག་པ་རབ་ཏུ་གྲུབ་པོ། །གང་དག་ལ་དེའི་ངོ་བོ་དང་རྒྱུའི་དངོས་པོ་དག་རབ་ཏུ་གྲུབ་པའི་མཁས་པ་རྣམས་ལ་ནི། གཏན་ཚིགས་འབའ་ཞིག་བརྗོད་པར་ཟད། གང་གི་དོན་དུ་དཔེ་བརྗོད་པའི་དོན་དེ་གྲུབ་པ་ཁོ་ན་ཡིན་པས་དེའི་ཚེ་དེ་བརྗོད་པས་ཅི་ཞིག་བྱ། དེ་རབ་ཏུ་བསྟན་ན་ཡང་ཆོས་མི་མཐུན་པའི་དཔེའི་གཞིས་ཅི་ཞིག་བྱ་སྙམ་དུ་དགོངས་ཤིང་གཞི་སྤང་བར༌[^152]མཛད་དོ། །

[Block 256 [VERSE]]
དེ་ཉིད་ཀྱི་ཕྱིར་འབྲེལ་ཤེས་ན། །
གཉིས་ལས་གང་ཡང་རུང་སྨྲས་པས། །
དོན་གྱིས་གོ་བས་ཅིག་ཤོས་ལའང་། །
དྲན་པ་ཡང་དག་སྐྱེ་བར་འགྱུར། །

[Block 257]
ཡང་ན་དོན་གྱིས་གོ་བས་གང་ཡང་རུང་བས་གཉི་ག་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ་ཞེས་བཤད་པ་གང་ཡིན་པ་སྟེ། དེར་ཡང་དཔེས་དེའི་ངོ་བོ་དང་རྒྱུའི་དངོས་པོ་རབ་ཏུ་སྟོན་པར་དགོངས་ཏེ། དོན་གྱིས་གོ་བས་གཅིག་བརྗོད་པས་ཅིག་ཤོས་འགྲུབ་པར་བཤད་དོ། །

[Block 258]
འདི་ལྟར་གང་བྱས་པ་དེ་ནི་མི་རྟོག༌[^153]པའོ་ཞེས་སྨྲས་ན། དོན་ཐ་དད་པ་མེད་ན། གསལ་བར་འདི་ནི་འདིའི་ངོ་བོ་ཉིད་དེ་ཙམ་དང་འབྲེལ་པ་ཚད་མས་མཐོང་བ་ཡིན་ནོ་ཞེས་བྱ་བར་ངེས་པར་འགྱུར་ཏེ། དེ་ཡོད་པར་ངེས་པའི་ཕྱིར་རོ། །

[Block 259]
དེ་བས༌[^154]ན་དེའི་ངོ་བོར་ཤེས་པས་ནི་དོན་གྱིས༌[^155]གོ་བས་མི་རྟག་པ་ཉིད་མེད་ན་བྱས་པ་ཉིད་མེད་དོ། །ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 260]
རང་གི་ངོ་བོ་མེད་པར་ཡོད་པར་མི་འགྱུར་ཏེ། ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 261]
དེ་ལྟ༌[^156]མ་ཡིན་ན་དེ༌[^157]ཡོད་དོ་ཞེས་བྱ་བ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 262]
དེ་བཞིན་དུ་དེ་མེད་ན་མེད་དོ་ཞེས་སྨྲས་ན།[^158] དེའི་ངོ་བོ་ཉིད་དུ་རིག་པ་ལས་འདི་ལྟར་འདི་ནི་འདིའི་ངོ་བོ་ཉིད་ཡིན་ཏེ། དེས་ནི༌[^159]དེ་མེད་ན་མེད་དོ། །

[Block 263]
དེ་ལྟ་མ་ཡིན་ན་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 264]
དེའི་ཕྱིར་དེའི་ངོ་བོ་ཉིད་དུ་རྟོགས་པས་རྗེས་སུ་འགྲོ་བ་དྲན་པ༌[^160]འབྱུང་ངོ་། །དེ་བཞིན་དུ་གང་ན༌[^161]དུ་བ་ཡོད་པ་དེ་ན་མེ་ཡོད་དོ་ཞེས་སྨྲས་ན། དུ་བ་ནི་མེའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 265]
དེས་ན་དུ་བ་ཡོད་ན་གདོན་མི་ཟ་བར་མེ་ཡོད་དོ། །

[Block 266]
དེ་ལྟ༌[^162]མ་ཡིན་ན་དོན་གཞན་དེ་དང་འབྲེལ་པར་ངེས་པ་མེད་པའི་ཕྱིར་ངོ་བོ་རང་དབང་ཅན་དུ་འགྱུར་རོ། །

[Block 267]
དེས་ན༌[^163]དེ་མེད་ཀྱང་རང་གི་ངོ་བོ་མ་ཚང་བ་མེད་པའི་ཕྱིར་མེད་པར་མི་འགྱུར་རོ། །

[Block 268]
འབྲས་བུ་ཡིན་ན་ནི་གདོན་མི་ཟ་བར་རྒྱུ་ཡོད་དོ། །

[Block 269]
རྒྱུ་རྒྱུ་ཉིད་ཡིན་པ་ནི་དེ་ཁོ་ན༌[^164]ཡིན་ཏེ། དོན་གཞན་ཡོད་ན་རང་གི་ངོ་བོ་ཉེ་བར་འཇོག་པ་གང་ཡིན་པའོ། །

[Block 270]
འབྲས་བུ་ཡང་དེ་ཡོད་པ་ཉིད་ན་ཡོད་པ་ཡིན་ནོ། །

[Block 271]
དེ་ཡང་དུ་བ་ལ་ཡོད་དོ། །

[Block 272]
དེ་ལྟ་བས༌[^165]ན་དུ་བ་ནི་འབྲས་བུ་ཡིན་ནོ་ཞེས་རྗེས་སུ་འགྲོ་བས་དེའི་འབྲས་བུ་ཉིད་ཤེས་པས་མེ་མེད་ན་དུ་བ་མེད་དོ་ཞེས་དོན་གྱིས་གོ་བས་ལྡོག་པ་རྟོགས་པར་འགྱུར་རོ། །

[Block 273]
དེ་བཞིན་དུ་མེ་མེད་ན་དུ་བ་མེད་དོ་ཞེས་སྨྲས་ན། མེ་ལས་དུ་བ་གདོན་མི་ཟ་བར་འབྱུང་ངོ་ཞེས་ཤུགས་ཀྱིས་རྗེས་སུ་འགྲོ་བ་རྟོགས་སོ། །

[Block 274]
དེ་ལྟ་མ་ཡིན་ན་དེ་མེད་ན་ཅི་སྟེ་ཡོད་པར་མི་འགྱུར། རྟག་པ་དང་མི་རྟག་པའི་དོན་གྱི་འབྲས་བུ་ཉིད་མ་ཡིན་ཡང་དེ་དག་མེད་ན་ཉན་པའི་ཤེས་པ་མེད་པ་མ་ཡིན་ནམ་ཞེ་ན། མེད་པ་ཉིད་མ་ཡིན་ཏེ། དེ་ལས་དེ་དག་ཉིད་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་རོ། །

[Block 275]
དེ་ལྟ་མ་ཡིན་ན་མེད་པས་ངེས་པའི་ཕྱིར། ཇི་ལྟར་དེ་དག་གི་ངོ་བོ་ལ་ལྟོས་ནས་ཐེ་ཚོམ་དུ་འགྱུར། ཡོད་པར་ངེས་པ་མེད་པའི་ཕྱིར་མེད་དོ་ཞེས་བྱ་བ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 276]
གང་གི་ཚེ་དཔེས་མེ་དང་དུ་བ་དག་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོར་མི་སྟོན་པ་དེའི་ཚེ་ནི་འབྲེལ་པ་མེད་པའི་ཕྱིར། གང་ན་དུ་བ་ཡོད་པ་དེ་ན་མེ་ཡོད་དོ་ཞེས་བྱ་བ་ཉིད་དུ་ཡང་མི་འགྱུར་ན། [^166]མེ་མེད་ན་དུ་བ་མེད་དོ་ཞེས་ཤུགས་ཀྱིས་ལྡོག་པ་འགྲུབ་པ་དང་། དེ་བཞིན་དུ་ཆོས་མི་མཐུན་པས་མེད་པ་མི་འགྲུབ་པའི༌[^167]ཕྱིར། །རྗེས་སུ་འགྲོ་བ་དྲན་པར་ལྟ་ག་ལ་འགྱུར། གང་གི་ཕྱིར་དེ་མེད་ན༌[^168]མི་སྲིད་པས་གཅིག་ཡོད་ན་གཞན་རབ་ཏུ་གྲུབ་པར་བྱ་བའི་ཕྱིར། དཔེས་ཇི་སྐད་བཤད་པའི་རང་བཞིན་འབྲེལ་པ་འདི་ཁོ་ན་རབ་ཏུ་སྟོན་པ།

[Block 277 [VERSE]]
དེའི་ཕྱིར་རྒྱུ་དང་རང་བཞིན་དག །
མེད་པ་འགའ་ཞིག་སྒྲུབ་པའི་ཡང་། །

[Block 278]
གཏན་ཚིགས་ཡིན་ཏེ། དེ་དག་ཁོ་ན་ལྡོག་པ་ན་རང་གི༌[^169]འབྲེལ་པ་ཟློག༌[^170]པར་བྱེད་པས་དེའི་ཕྱིར་དོན་གཞན་འགའ་ཞིག་དགག་པ་དང་སྒྲུབ་པར་འདོད་པས། རྒྱུའམ་རང་བཞིན་ཁྱབ་པར་བྱེད་པ་ལྡོག་པའི་གཏན་ཚིགས་ཉིད་དུ་བརྗོད་པར་བྱའོ། །

[Block 279]
མ་འབྲེལ་ན་ནི་ཇི་ལྟར་གཅིག་ལོག་པས་གཞན་ལྡོག་པ་སྒྲུབ་པར་བྱེད། དམིགས་པར་ནི།

[Block 280 [VERSE]]
རིགས་ལྡན་དེ་མི་རིགས་པར་ཡང་། །
དགག་པའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 281]
དགག་པའི་ཡུལ་ཅན་གྱི་ཐ་སྙད་ཀྱི་གཏན་ཚིགས་ལ་དེའི་གཏན་ཚིགས་ཞེས་བཤད་དེ། དེ་ལྟ་བུའི་མི་དམིགས་པ་ནི་རང་ཉིད་ཀྱིས་དགག་པའི༌[^171]ངོ་བོ་ཡིན་པའི་ཕྱིར། རྒྱུ་དང་ཁྱད་པར༌[^172]བྱེད་པ་མི་དམིགས་པ་ནི་གཉི་གའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 282 [VERSE]]
དེ་ལྟར་མི་དམིགས་འདི་རྣམ་གསུམ། །
བཤད་ཀྱང་རྣམ་པ་དུ་མ་སྟེ། །
དེ་དང་དེ་འགལ་ལ་སོགས་པ། །
མི༌[^173]རྟོགས་རྟོགས་དབྱེའི་སྦྱོར་སྒོ་ནས། །

[Block 283]
དགག་པའི་གཏན་ཚིགས་ནི་རྣམ་པ་གསུམ་ཁོ་ན་སྟེ། རྒྱུ་དང་ཁྱབ་པར་བྱེད་པ་དེ་ལྟར་ངེས་པ་དང་། རང་གི་བདག་ཉིད་དམིགས་སུ་ཡོད་པ་མི་དམིགས་པའོ། །

[Block 284]
དེ་ནི་སྦྱོར་བའི་དབང་གིས་དེ་དང་འགལ་བ་ལ་སོགས་པ་མ་རྟོགས་པ་དང་། རྟོགས་པའི་དབྱེ་བའི་སྒོ་ནས་རྣམ་པ་དུ་མར་བཤད་དེ། དེ་མ་རྟོགས་པ་དང་། དེ་དང་འགལ་བ་རྟོགས་པ་དང་། འགལ་བའི་འབྲས་བུ་རྟོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དབྱེ་བའི་སྦྱོར་བ་དག་གིས་སྔར་ཇི་སྐད་བཤད་པ་བཞིན་ནོ། །

[Block 285 [VERSE]]
རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་འམ། །
རང་བཞིན་ངེས་པར་འབྱེད་པ༌[^174]ལས། །
མེད་ན་མི་འབྱུང་ངེས་པ་སྟེ། །
མ་མཐོང་ལས་མིན་མཐོང་ལས་མིན། །
--- END BLOCKS ---
