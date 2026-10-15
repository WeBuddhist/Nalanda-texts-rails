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
[Block 4831]
བརྫུན་དུ་སྨྲ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 4832]
རུང་བ་མ་ཡིན་པར་བསམ་པས༌[^3291]གང་ཡང་རུང་བའི་སྐྱོན་ནས་སྨྲ་བར་འདོད་ནས་སྐྱོན་ནས་སྨྲ་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འཆད་པར་འགྱུར་རོ། །

[Block 4833]
དེ་ལ་ཅི་ཞིག་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཡང་རུང་བ་མ་ཡིན་པར་བསམ་པ་བརྗོད་པ་ཡང་འདི་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགེ་སློང་ནི་ཡུལ་དུ་རྟོགས་པར་བྱ་སྟེ། དགེ་སློང་གི་ཡུལ་བརྗོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4834]
འོག་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཕྲ་མ་བྱེད་པའི་ལྟུང་བྱེད་ལ་ཡུལ་དགེ་སློང་ཉིད་དུ་རྟོགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4835]
སྨྲས་ན་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་གཉིས་ཀ་ཡང་དགེ་སློང་གི་ཡུལ་ཁོ་ན་ལ༌[^3292]རིག་པར་བྱ་སྟེ། དགེ་སློང་ལ་བརྗོད་པ་ལ་ཞེས་བྱ་བའོ། །

[Block 4836]
གཞན་ལ་ནི་འདི་དག་བརྗོད་པ་འམ་སྨྲས་པ་གཅིག་པུ་ལ་གཏོགས་པའི༌[^3293]ཕྱོགས་ཉིད་ཀྱི་ཕྱིར་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 4837]
དག་པའི་སེམས་ཀྱིས་ཀྱང་རུང་བ་མ་ཡིན་པར་བསམ་པ་བརྗོད་པ་བྱུང་བ་ཡིན་ནོ། །

[Block 4838]
དེའི་ཁྱད་པར་དུ་བྱས་པ་སྟེ། སྐྱོན་ཉིད་བརྗོད་པར་འདོད་པས་སོ་ཞེས་བྱ་བའོ། །

[Block 4839]
ཚིག་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་འཇམ་པས་ཀྱང་རུང་རྩུབ་པས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱོན་ལས་སྨྲ་བ་དང་བཅས་པའི་ཚིག་རྩུབ་མོ༌[^3294]སྨྲས་ན་དངོས་གཞིར་འགྱུར་གྱི་གཞན་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བའོ། །

[Block 4840]
དེ་ལྟར་ན་ཚིག་རྩུབ་པོ་སྨྲས་པ་ཡང་བསླབ་པའི་གཞི་འདི་དག་ཉིད་ལ་ཁོངས་སུ་བསྡུ་བ་ཉིད་ཅེས་བྱ་བ་འདིས་ཡང་དག་པར་རིག་པར་བྱའོ། །

[Block 4841]
རུང་བ་མ་ཡིན་པར་བསམ་པ་གང་ཡང་རུང་བ་སྨྲ་ནའོ་ཞེས་བྱ་བ་ནི། ཁྱོད་ནི་མཛེ་ཅན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྒྲ༌[^3295]ལ་ཡང་ཁྲོ་བ་པོ་ཉིད་ཅེས་བྱ་བ་ཉེ་བའི་ཉོན་མོངས་པ་ལ་སོགས་པ་སྨད་པར་བསམ་པ་གང་ཡང་རུང་བ་བརྗོད་པ་ལ་སྐྱོན་ནས་སྨྲ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4842]
མི་དགའ་བ་ཉིད་དུ་མ་གྱུར་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། མི་དགའ་བ་ཉིད་ཅེས་བྱ་བ་ནི། ཁྲོས་པ་དང་འཁྲུགས་པ༌[^3296]དང་ཡི་ཆད་པ་དང་སྐེངས་པ་དང་ཡུལ་ཡུལ་བོར་གྱུར་པ་ཞེས་བྱ་བ་རྣམས་དང་དོན་གཅིག་གོ། །

[Block 4843]
དེ་ལྟར་འདིར་གཞུང་ནི་དགེ་སློང་སྤ་བཀོང་བ་ཉིད་དུ་གྱུར་ཀྱང་རུང་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4844]
གཞན་རྒྱལ་རིགས་ཉིད་དང་བྲམ་ཟེ་ཉིད་ལ་སོགས་པ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ་གཞན་ཞེས་བྱ་བ་ནི། རུང་བ་མ་ཡིན་པར་བསམ་པ༌[^3297]ལས་གཞན་པ་སྟེ། རྒྱལ་རིགས་ཉིད་དང་བྲམ་ཟེ་ཉིད་ལ་སོགས་པ་ལ་རུང་བ་མ་ཡིན་པའི་བསམ་པས་སྨྲ་ན་ཉེས་བྱས་སོ། །

[Block 4845]
སྐྱོན་ནས་སྨྲ་བའོ།། །།

[Block 4846]
གང་དུ་ཕྲ་མ་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཕྲ་མ་བྱེད་འདོད་པས་ཆེ་གེ་མོ་ཞིག་ཟེར་རོ་ཞེས་སྨྲ་ནའོ་ཞེས༌[^3298]བྱ་བ་སྨོས་ཏེ། འདིར་སྐྱོན་ཉིད་ཀྱང་ཡན་ལག་མ་ཡིན་ལ་རུང་བ་མ་ཡིན་པ་བསམས་པ་ཉིད་ཀྱང༌[^3299]བྲམ་ཟེ་ལ་སོགས་པས་སོ། །

[Block 4847]
བྱེ་བྲག་ཏུ་སྨྲ་བའི་སྒྲ་ལ་ཐ་དད་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བས་ན༌[^3300]མི་བརྟེན༌[^3301]པའོ། །

[Block 4848]
སྤྱིར༌[^3302]ཡང་ཆེ་གེ་མོ་ཞིག་ཟེར་རོ་ཞེས་བྱ་བ་བརྗོད་པ་འདི་ལ་ལྟུང་བ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་མིང་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆེ་གེ་མོ་ཞིག་ཟེར་རོ་ཞེས་བྱ་བ་གལ་ཏེ་དེའི་མིང་གིས་སྨོས་པར་བྱེད་ན་གལ་ཏེ་མིང་གིས་ཆེ་གེ་མོ་དེ་ལ་བརྗོད་པར༌[^3303]བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4849]
དེ་ཡང་དགེ་སློང་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི་གང་གི་མིང་དེས་གལ་ཏེ་བརྗོད་ན་ཞེས་བྱ་བ་སྨོས་པར་བྱད་ན་གལ་ཏེ་དེ་ལ་དགེ་སློང་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4850]
དགེ་སློང་ཉིད་མ་ཡིན་པ་ལ་གཅིག་གམ་གཉིས་པོ་དག་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་ནས་རྟོགས་པར་བྱའོ། །

[Block 4851]
གཞན་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་གོ་བར་བྱེད་པ་མ་ཡིན་པས་རྣམ་གཅོད༌[^3304]ལ་རིགས་ལ་སོགས་པ་དང་ལྡན་པས་བརྗོད་པ་ལ་ཉེས་བྱས་སོ། །

[Block 4852]
ཕྲ་མ་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 4853]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་ལ་བྱེད་པ་པོ་ཉིད་གཙོ་ཆེར་ཞེས༌[^3305]བྱ་བའི་དོན་ཏོ། །

[Block 4854]
འདུ་ཤེས་གང་ལས་ཤེ་ན། དེའི་ཕྱིར་དགེ་སློང་གཉིས་ཀྱི་རྩོད་པ་ཉིད་དགེ་འདུན་གྱིས་ལེགས་པར་ཞི་བར༌[^3306]བྱས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྩོད་པ་ལ་དགེ་འདུན་གྱི་ཡང་དག་པར་དགེ་འདུན་གྱིས་སོ། །

[Block 4855]
དགེ་འདུན་ལ་ཡང་རྩོད་པ་ཉིད་ལ་འདུ་ཤེས་ལ་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4856]
རྩོད་པའི་གཞི་ལ་རྩོད་པའི་གཞིར་འདུ་ཤེས་པ་ཞེས་བྱ་བ་རྩོད་པའི་གཞི་ལ་འདུ་ཤེས་གང་ཞིག་རྙེད་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4857]
རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་གཉིས་ཀ་ལ་དགེ་སློང་ཉིད་ཡིན་ན་སྐྱོ་སྔོགས་བྱེད་པའི་དངོས་གཞིའོ། །

[Block 4858]
གཅིག་གམ་གཉིས་ཀ་དག་གམ་གཞན་ཉིད་ལ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4859]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་གིས་དགེ་སློང་མ་དང་རྩོད་པ་ལ་སྐྱོ་སྔོགས་བགྱིད་ན་ལྟུང༌[^3307]བ་ཅིར་འགྱུར་ཉེས་བྱས་སུའོ། །

[Block 4860]
དེ་བཞིན་དུ་དགེ་སློང་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དང་དགེ་བསྙེན་དང་དགེ་བསྙེན་མ་ལ་ཡང་རྩོད་པའི་གཞི་དགེ་སློང་གིས་སྐྱོ་སྔོགས་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 4861]
དེ་བཞིན་དུ་དགེ་སློང་དང་དགེ་ཚུལ་དང་དགེ་སློབ་མ་དང་དགེ་ཚུལ་མ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 4862]
སྐྱོ་སྔོགས་སོ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པར་བྱས་པ་ཉིད་དུ་འབྱུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4863]
ཡང་ལས་སུ་བྱས་པ༌[^3308]ཡང་བྱ་བ་ཉིད་ཀྱིས་ཤེས་པ་འདིར་གང་ཞིག་སྨོས་པ་དེ་འདིར་ངེས་པ་ཅན་གྱི་ཆོས་ལ་རྗེས་སུ་བརྗོད་པའོ། །

[Block 4864]
ཡང་དག་པར་བྱ་བ་འབྱུང་བ་ལ་སྐྱོ་སྔོགས་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4865]
དེ་བས་ན་འདིར་བསྡུ་བའོ། །

[Block 4866]
གང་ཟག་ཇི་ལྟ་བུ་དང་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་ལ་འདིར་འདུ་ཤེས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཉུག་མར་གནས་པ་དང་ལས་བྱེད་པ་དང་འདུན་པ་འབུལ་བ་རྣམས་ཁོ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏོ། །

[Block 4867]
དེས༌[^3309]འདི་རྣམས་ལ་ཡང་དག་པར་བཞག་པ་ཉིད་ལ་ངེས་པ་ཞེས་བྱ་བ་འདི་ལས་མདུན་དུ་གང་ཞིག་འདུ་ཤེས་པར་གྱུར་པ་ཉིད་ཀྱི་སྐྱོ་སྔོགས་བྱེད་པ་དེ་འདི་རྣམས་ལ་དངོས་གཞིའོ། །

[Block 4868]
དངོས་གཞིའི་གནས་ལ་ཡང་གཞན་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་འདི་ལ་སྤྲོས་པ་འདི་རིག༌[^3310]པར་བྱའོ། །

[Block 4869]
ལྟ་བ་སྨྲ་བ་དང་གློ་བུར་དུ་འོངས་པ་དག་ལ་ནི་ཉེས་བྱས་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་གློ་བུར་དུ་འོངས་པ་ཉིད་ཡིན་པས་རྒྱུས༌[^3311]མི་ཤེས་པའི་ཕྱིར་རྩོད་པའི་གཞི་དང་བཅས་པ་ལ་འདི་ཐོག་མ་དང་བར་དང་ཐ་མར་མངོན་པར་མི༌[^3312]ཤེས་པའི་ལྟ་བ་སྨྲས་པ་ཉིད་ནི་སྐྱོ་སྔོགས་བྱེད་པ་འདི་དག་གི་ལྟ་བ་སྨྲ་བར་བྱེད་པ་དག་ནི་འདི་མི་འདོད་ཅེས་བྱ་བ་ངེས་པ་འདི་དག་ལ་ཡང་དག་པར་བཞག་པ་ཉིད་ལ་ངེས་པ་མེད་ཅེས་བྱ་བ་དེའི་ཕྱིར་གང་ཞིག་རྒྱུས་མི་ཤེས་པར་འགྱུར་རོ། །

[Block 4870]
སྐྱོ་སྔོགས་བྱེད་པ་དེ་བས་ན་འདི་ནི་ཉེས་བྱས་སོ། །
--- END BLOCKS ---
