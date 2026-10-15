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
[Block 4691]
ལྷག་མའི་དུས་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་ཕྱི་མ་ཤོས༌[^3204]ངེས་པར་བྱས༌[^3205]ན་ནི་སྟོན་ཟླ་ཆུངས༌[^3206]ཉ་ཚུན་ཆད་དོ་ཞེས་གསུངས་སོ། །

[Block 4692]
ཁས་བླངས་པ་སྔ་མ་ལ་ནི་སྟོན་ཟླ་འབྲིང་པོའི་ཉ༌[^3207]ཚུན་ཆད་དུས་མ་ཡིན་ནོ། །

[Block 4693]
དེ་ནི་མི་བསྐོ་བར༌[^3208]མི་བྱའོ་ཞེས་བྱ་བ་ནི་བརྟད་པ་ལས་བྱུང་བའི་དུས་སུ་གཏང་བར༌[^3209]བྱ་བ་ཉིད་ལ་གོས་སྦེད་པ་མ་ཡིན་པ་འདི་བསམ་པར་མི་བྱའོ། །

[Block 4694]
ཞུ་བ་ལས་བསླབ་པའི་གཞི་འདི་ལ་རིམ་པ་ནི་འདི་ཡིན་ནོ། །

[Block 4695]
རྣམ་པར་འབྱེད་པ་ལས་ནི་འཕྲོག་པའི༌[^3210]བསླབ་པའི་གཞི་ལས་ནི་དེ་མ་ཐག་པའོ། །

[Block 4696]
དེ་ལས་འཆང་བ་ལ་འཆང་བའི་རྗེས་སུ་འབྲེལ་པའི་རིགས་ཏེ་ཞེས་བྱ་བའི་རིམ་པ་འདི་ལྟར་བསྟན༌[^3211]པའོ། །

[Block 4697]
བརྟད་པ་ལས་བྱུང་བའི་སྤང་བའོ།། །།

[Block 4698]
ཅི་ཞིག་བྱས་ན་བསྔོས་པ་ལས་བསྒྱུར་བའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱིས་གང་ཟག་གཞན་རྣམ༌[^3212]དགེ་འདུན་ལ་བསྔོས་པའི་གོས་ཤེས་བཞིན་དུ་བདག་ཉིད་ལ་བསྒྱུར་ཏེ་ཐོབ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གྱི་རྙེད་པ་ཞེས་བྱ་བ་འདི་ལ་མདོ༌[^3213]འདི་ལྟུང་བ་རྒྱས་པར་བཤད་པ་ལ། གང་ཟག་གི་ཡང་བདག་ཉིད་ལ་བསྔོས་པས་ཐོབ་པ་ལ་དངོས་གཞིར་གསུངས་སོ། །

[Block 4699]
དགེ་སློང་གིས་གང་ཟག་གཅིག༌[^3214]ལ་བསྔོས་པའི་རྙེད་པ་གང་ཟག་བདག་ཉིད་ལ་སྒྱུར་བར༌[^3215]བྱེད་པ་དེ་ལ་ཉེས་བྱས་སུ་འགྱུར་ལ། ཐོབ་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱའོ། །

[Block 4700]
དེ་ལ་དཔེ་ནི་འདི་ཡིན་ཏེ། སྐྱེ་བའི་དབང་གིས་བརྟེན་པ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་བཞག་པའོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གི་ཚིག་གོ། །

[Block 4701]
གང་ཟག་བདག་ཉིད་ལ་གང་ཟག་ཡིན་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་བྱེ་བྲག་འབྱེད་པ་ནི་གང་ཟག་གཞན་ནམ་ཞེས་བྱ་བ་སྟེ། གང་ཞིག་འདི་ལྟུང་བ་འབྱིན་པར་བྱེད་པ་ལས་གང་ཟག་གཞན་ལ་བསྔོས་པ་ལ་སྟེ་དེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4702]
རང་གིས༌[^3216]བསྔོས་པ་ལ་བདག་ཉིད་ལ་བསྔོས་པ་ནི་འགོད་པ་མ་ཡིན་ནོ། །

[Block 4703]
དེ་ལ་ཡང་ཉེས་བྱས་སུ་འབྱུང་བར་འགྱུར་ཏེ། དེ་བས་ན་གཞན་གྱིས་ཞེས་བྱ་བའི་ཁྱད་པར་ཏེ། གཞན་གྱིས་བསྔོས་པ་སྟེ་བདག་ཉིད་ཀྱིས་ནི༌[^3217]མ་ཡིན་ནོ། །

[Block 4704]
བསྔོས་པ་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གོས་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 4705]
དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4706]
རང་གི་དོན་དུ་འདི་ལ་གོས་ཀྱི་རྙེད་པ་མངོན་པར་འདོད་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4707]
བླངས་པར་གྱུར་པ་སུ་ཞིག་དང་ལྷན་དུ་མི་ཤེས་བཞིན་དུ་བསྔོ་བར་འགྱུར་ཏེ། དོར་བྱས་པའི་དབང་གིས་སམ། འཇམ་པར་བྱས་པའི་དབང་གིས་སམ། སུ་ཞིག་དེ་ལ་རྗེས་སུ་འདོད་ཅིང་འདུག་པ་ཞེས་བྱ་བ་འམ། གང་ཡང་རུང་བ་དེ་ལ་འགེད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་འམ། གཞན་དུ་བསྔོས་པ་ལ་མི་སྦྱིན་པའོ། །

[Block 4708]
འདིར་ནི་བསྒྱུར་བ་ཉིད་མེད་པ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ས་བོན་མི་ཤེས་པའི་ཕྱོགས་ལ་རྨོ་བ་ལ་སོགས་པ་ལས༌[^3218]མི་བྱེད་ཅིང་སྐྱེད་པར་བྱེད་པར་མི་འགྱུར་རམ། དེ་བས་ན་ཤེས་བཞིན་དུ་ཞེས་བྱ་བའི་ཁྱད་པར་རོ། །

[Block 4709]
འདིར་མདོ་ནི་གང་སླར་ཤེས་བཞིན་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 4710]
འདིའི་རྣམ་པར་འབྱེད་པ་ནི་རང་ཉིད་ཀྱིས༌[^3219]འདི་ལ་རིག་པར་འགྱུར་རོ། །

[Block 4711]
གཞན་རྣམས་ཀྱིས་གོ་བར་བྱས་པ་ཞེས་བྱ་བའོ། །

[Block 4712]
དེ་ལྟར་ན། གཞན་ལ་གཞན་གྱིས་གོས་བསྔོས་པ་ཞེས་བྱ་བ་ཤེས་བཞིན་དུ་བདག་ཉིད་ལ་བསྒྱུར་བ་ཡིན་པ་དེ་ལ༌[^3220]གང་ཞིག་ཐོབ་པ་གང་ཡིན་པ་དེ་ལ་སྤང་བའི་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4713]
གལ་ཏེ་ཐོབ་པ་ལ་དངོས་གཞི་ཡིན་ན་བསྒྱུར་བ་ལ་ཁ་ན་མ་ཐོ་བ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསྒྱུར་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གོས་ནི་དཔེ་ཡིན་ཏེ། ཁ་ཟས་ལ་སོགས་པ་གཞན་པ་ལ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4714]
དེ་བས་ན་གཞན་དུ་ཡང་རྙེད་པ་ལ་སྤང་བ་འདི་ཡོད་པའོ། །

[Block 4715]
འདི་ནི་རྙེད་པར་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཟས་འདི་ལ་ཁས་ལེན་པར་བྱེད་པའོ། །

[Block 4716]
རྙེད་པ་གཞན་ལ་ནི་རང་ཉིད་ལ་བསྒྱུར་བ་ཞེས་བྱ་བ་འདི་ཁ་ན་མ་ཐོ་བ་སྟེ། བཏུང་བ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 4717]
དེ་བས་ན་འདིར་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ནི་སྐབས་མ་ཡིན་ནོ། །

[Block 4718]
འདི་ལྟར་ཞུ་བ་ལས་ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཉེ་དུ་མ་ལགས་པ་ལས་གོས་ལེན་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་ན། དགེ་སློང་མ་ལས་གོས་ལེན་པར་བྱེད་ན་དེ་ལ་ཡང་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་དེས་གལ་ཏེ་དགེ་འདུན་གྱི༌[^3221]ཕྱིར་ཉེ་བར་གཞག་པ་ཡིན་ལ། དགེ་སློང་གིས་བདག་ཉིད་ལ་སྦྱོར་བར་བྱེད་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4719]
ཇི་ལྟར་འདིར་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ཡན་ལག་མ་ཡིན་པ་བཞིན་དུ་ཚིག་ཉིད་ཀྱང་དེ་དང་འདྲའོ། །

[Block 4720]
གལ་ཏེ་འབྲལ་བར་བྱ་བ་དགེ་སློང་ཡིན་ན་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 4721]
འདིར་གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། གཞན་ལ་ཞེས་བྱ་བ་ནི་བསྔོས་པ་ལའོ། །

[Block 4722]
གང་ཟག་གཞན་ལ་འདི་བསྔོས་པ་གཞན་ལ་སྒྱུར་བར་བྱེད་ན་ཡང་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4723]
དེའི་འབྲས་བུ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཐོབ་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4724]
བདག་ཉིད་ལས་གཞན་པ་ལ་སྒྱུར་བར་བྱེད་ན་དངོས་གཞི་ལ་ཡང་ཉེས་བྱས་ཡིན་ལ། སྦྱོར་བ་གཅིག་པུ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4725]
གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟས་ལས༌[^3222]གཞན་པའི་རྙེད་པ་སྒྱུར་བར་བྱེད་ན་ཁ་ན་མ་ཐོ་བ་བཤད་ཟིན་ཏོ། །

[Block 4726]
འདིར་ཟས་ནི་ལྷག་མར་བྱས་པ་སྟེ། བསྒྱུར་བ་དང་བསྒྲུབ་པ༌[^3223]ལ་འདི་ནི་ཉེས་བྱས༌[^3224]སུ་བརྗོད་པའོ། །

[Block 4727]
འདིར་གཞུང་ནི་འདི་ཡིན་ཏེ། མུ༌[^3225]ཏོ་བ་གཅིག་ལ་བསྔོས་པའི་ཟས་མུ༌[^3226]ཏོ་བ་གཞན་ལ་སྒྱུར་བར་བྱེད་ན་ཉེས་བྱས་སུ་བརྗོད་པ་གང་ཡིན་པ་བཟའ་བར་བྱ་བ་ལ༌[^3227]ཡང་དེའོ་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 4728]
དབྲལ་བ་དང་སྦྱར་བ་གཉིས་ཀ་སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གནས་ཁང་ལ་སོགས་པ་སེམས་ཅན་དུ་བགྲང་བ་ཉིད་མ་ཡིན་པ་གནས་ཁང་ལ་སོགས་པ་གང་ལ་རྙེད་པ་འདི་བསྔོས་པ་འདི་ནི་འདིར་དབྲལ་བར་བྱ་བར་བརྗོད་དོ། །

[Block 4729]
གང་དུ་སྔོ་བར༌[^3228]བྱེད་པ་དེ་ནི་སྦྱོར་བའོ། །

[Block 4730]
འདིར་ཡང་བསྔོ་བ་དང་གྲུབ་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བ་འདིར་ངག་གི་དོན་ཏོ། །
--- END BLOCKS ---
