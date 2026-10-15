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
[Block 316]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ལྔ་པོ་དག་ནི་མི་འདྲ་བ་དག་ཡིན་ཏེ། ཕྱིང་པ་ཐམས་ཅད་དང་། ལ་བ་ཐམས་ཅད་དང་། བེའུ་ཕྲུག་ཐམས་ཅད་དང་། ཀླམ་ཐམས་ཅད་དང་། གོས་སེངས་པ་ཐམས་ཅད་དང་། ལྷན་ཐབས་གླན་ཏེ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 317]
དེ་ལ༌[^310]ཅུང་ཟད་ཀྱང་ནུས་པར་བྱ་བ་མ་ཡིན་མོད་ཀྱི་འདིར་བྱིན་གྱིས་བརླབ་པར༌[^311]བྱ་བ་ཉིད་ཀྱིས་ཁས་བླངས་པ་རྟོགས་པའི་ཕྱིར་ཞེས་བྱ་བ་འདི་ལྟར་ཤེས་པ་ཡིན་ནོ། །

[Block 318]
གནས་མལ་མི་གཙང་བས་གོས་པར་གྱུར་ན་དེའི་མོད་ལ་སྦྱར་བར༌[^312]བྱའོ། །

[Block 319]
དགེ་འདུན་གྱི་རྩྭའི་ཁྲི་དང་ཁྲིའུ་མ་གཏོགས་པ་སྟན་ཡན་ཆད་ལ་དེ་མ་ཡིན་པའི་གདིང་བ་མེད་པ་དང་གདིང་གཡོགས་ལ་ཡང་བར་ཆད་མ་བཅུག་པ་ཉེ་བར་སྤྱད་པར༌[^313]མི་བྱའོ་ཞེས་བྱ་བ་ལ༌[^314]ཁྲི་དང་ཁྲིའུ་མ་གཏོགས་པ་ཞེས་བྱ་བ་ནི་ཁྲི་དང་ཁྲིའུ་ལས་གཞན་པའོ། །

[Block 320]
རྩྭའི་ཁྲི་དང་ཁྲིའུ་ཞེས་བྱ་བ་ནི་འདིར་རྩྭ་མུན་ཛ་དང་གྲེས་མའི་ཁྲི་དང་ཁྲིའུ་ལ་སོགས་པའི་ཐགས་མས་བརྒྱུས་པ་ལ་སྨོས་སོ། །

[Block 321]
གང་ཞིག་འདི་ཕྲན་ཚེགས་རྣམས་ལས་གསུངས་ཏེ། ཚེ་དང་ལྡན་པ་གནས་མལ་བསྡུས་སམ། དེ༌[^315]སྨྲས་པ། བདག་གིས་གདིང་བ་མ་བསྡུས་སོ། །

[Block 322]
དེ་རྩའི༌[^316]ཁྲི་ལ་ཉལ་ཞིང་མ་བསྡུས་པ་དེ་བས་ན་དེ་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 323]
གང་གི་ཕྱིར་འདིར་གང་ཟག་གི་རྩྭའི་ཁྲི་དང་ཁྲིའུ་འདི་མ་བསྡུས་སོ་སྙམ་དུ་ཡིད་ལ་བཟུང་བ་ཡིན་ནོ། །

[Block 324]
གྲོལ་བ་ལས་ཀྱང་འདི་ཐོབ་པ༌[^317]འདི་དག་དྲི་མ་ཅན་དུ་བྱས་པ་དོན་མེད་དོ་ཞེས་འདིའི་རྗེས་སུ་འབྲངས་པས་ཀྱང་། རྩྭའི་ཁྲི་དང་ཁྲིའུ་རྗེས་སུ་གནང་བའི་འཇིག་པའི་ཆོས་ཅན་དང་ལྡན་པར་གྱུར་པ་ལ་ཡང་དྲི་མ་ཅན་དུ་བྱས་པ་དོན་མེད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེ་དང་ལྡན་པ་ལ་ཡང་འདིའི་རྗེས་སུ་འབྲངས་པས༌[^318]རྟོགས་པར་བྱའོ། །

[Block 325]
དེ་ཞེས་བྱ་བ་ནི༌[^319]དགེ་འདུན་གྱི་མ་ཡིན་པས་སོ། །

[Block 326]
དགེ་འདུན་ལས་གཞན་གྱི་གདིང་བ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 327]
གདིང་བ་མེད་པ་དང་ཞེས་བྱ་བ་ནི་འདུག་པ་ལས་ཇི་སྲིད་དུ་ཉེ་བར་ལོངས་སྤྱོད་པར་མི་བྱའོ། །

[Block 328]
འདུག་པའི་སྟན་ཡན་ཆད་ལ་ཡང་གདིང་བ་མེད་པར་དགེ་འདུན་གྱི་ལ་འདུག་པར་མི་བྱའོ། །

[Block 329]
འདིར་ལོངས་སྤྱོད་པ་ནི་ཁོངས་སུ་མ་གཏོགས་པ་ནི་མ་ཡིན་ནོ་སྙམ་དུ་ཤེས་པར་བྱ་བའི་དོན་ཏོ། །

[Block 330]
ཡན་ལག་གིས་རེག་པ་ཙམ་ལ་ཡང་གདིང་བ་གཞུག་དགོས་པར་རིག་པར་བྱའོ། །

[Block 331]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 332]
དགེ་སློང་རྣམས་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་འདུག་པར་གནང་སྟེ་གནས་མལ་སྦ་བའི་དོན་དུའོ། །

[Block 333]
གདིང་བ་མེད་པར་ཉེ་བར་སྤྱད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 334]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་ཀྱང་། བཙུན་པ་སྟན་ཁྲ་བོ་ལ་འདུག་ཏུ་རུང་ངམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་གདིང་བ་ཡོད་པར་གྱུར་པ་ན་རུང་སྟེ། གང་ཞིག་ཕལ་ཆེར་ཉམས་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 335]
ཕལ་ཆེར་མ་ཉམས་པ་ལ་ཞེས་བྱ་བ་འདིར་ཡང་ཚིག་ནི་འདི་ཉིད་ཡིན་ཏེ། འདིར་གཞུང་ནི། དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་རིག་པར་བྱའོ། །

[Block 336]
གདིང་གཡོགས་ལ་ཡང་ཞེས་བྱ་བ་ནི་སྟེང་དུ་གཡོགས་པ་ལ་གདིང་གཡོགས་སུ་འདོད་དོ། །

[Block 337]
གཞན་ཡང་བར་ཆད་མ་བཅུག་པ་ནི། དགེ་འདུན་གྱི༌[^320]གདིང་གཡོགས་པའོ། །

[Block 338]
དེ་ལ་ཡང་བར་ཆད་མ་བཅུག༌[^321]པར་ལོངས་སྤྱོད་པར་མི་བྱའོ། །

[Block 339]
ཐམས་ཅད་ཀྱི་ཁྲ་བོ་ཕལ་ཆེར་མ་ཉམས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གི་གནས་མལ་ལ་ཡང་གདིང་བར་མ་བྱས་པ་ལ་མི་འདུག་པ་ལས་གདིང་གཡོགས་ལ་ཡང་བར་ཆད་མ་བཅུག་པར་ཉེ་བར་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་གང༌[^322]གི་སྒྲས་དྲངས་པའོ། །

[Block 340]
དེ་མ་ཡིན་པའི་ནི་འདིར་ཁྲ་བོ་ལས་ཕལ་ཆེར་མ་ཉམས་པ་ལས།

[Block 341]
གཞན་གྱིས༌[^323]བྱ་བ་དོན་གྱིས་རྣམ་པར་གཞག་པའོ། །

[Block 342]
ངན་ངོན་ཅན་དང་དྲི་མ་ཅན་གྱིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་གདིང་བ་ལ་ཡང་བར་ཆད་མ་བཅུག་པ་ལ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་ནས་ཀྱང་སླར་གདིང་བའི་ཆོ་ག་ལ་འདིར་བར་ཆད་མ་བཅུག་པའི་ཆོ་ག་ཐོབ་པའོ།[^324] །བར་ཆད་མ་བཅུག་པའི་ཆོ་ག་ལས་ཀྱང་གདིང་བའི་ཆོ་གའོ། །

[Block 343]
དེ་ལྟ་བས་ན་ཐམས་ཅད་དུ་འདིས་གཉི་གའི༌[^325]ཁོངས་སུ་བསྡུས་པར་བྱས་པའོ། །

[Block 344]
གདིང་བ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བར་ཆད་མ་བཅུག་པ་བཟློག་པའི་དོན་དུ་འདི་སྨོས་སོ། །

[Block 345]
དེ་ནི་སྟུག་ན་ཚིག་རྐྱང༌[^326]རུང་ངོ་ཞེས་བྱ་བ་ནི་གདིང་བ་དེའོ། །

[Block 346]
སེངས་པ་ནི་ཉི་རིམ་མོ། །

[Block 347]
ཁྲ་ཁྲ་བོ༌[^327]མི་རུང་ངོ་ཞེས་བྱ་བ་ནི༌[^328]གདིང་བ་ཁྲ་བོ་བཀྲ་བ་ཁྲ་ཁྲ་བོར་འདུག་པ་དེ་བཀག་པའོ། །

[Block 348]
འདིར་མཚོན་གྱིས་དྲས་ཏེ་བཅང་བར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 349]
མཚོན་གྱིས་དྲས་པའི་གོས་ལོངས་སྤྱད༌[^329]པར་བྱའོ་ཞེས་བྱ་བ་སྤྱིའི་ཆོ་ག་བསྒྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་མ་བསྡུས་པའོ། །

[Block 350]
དེ་ལ་གླེགས་བུའི་འཕྲོ༌[^330]བྱའོ་ཞེས་བྱ་བ་ནི་གདིང་བ་དེ་ལའོ། །

[Block 351]
ཕྱོགས་གང་དུ་ཞེ་ན། དེའི་ཕྱིར་འོག༌[^331]རོལ་གྱི་སུམ་ཆའི་དང་པོར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འོག་རོལ་ཞེས་བྱ་བ་ནི་རྐང་པའི་མཐའ་ལོགས་སུ་སུམ་ཆའི་གང་ཡིན་པ་དེའི་དང་པོ་དང་དབུས་དང་ཐ་མར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 352]
གླེགས་བུ་གཅིག་པ་བྱིན་གྱིས་བརླབ་པར༌[^332]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གདིང་བ་སྟེ་མ་མོ་ལས་འདུག་པ་འདི་ནི་འདིར་གདིང་བའོ། །

[Block 353]
གཡན་པ་དགབ་པ༌[^333]དེ་དང་ལྡན་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དང་ལྡན་པས་ཞེས་བྱ་བ་ནི་གཡན་པའོ། །

[Block 354]
དེ་ཞག་ལྔ་འམ་དྲུག་ཅིང་སྦྱང་བར་བྱའོ། །

[Block 355]
སྲིན་བལ་གྱི་དང་། བལ༌[^334]གྱི་དང་། ཤ་ནའི་དང་། ཟར་མའི་རུང་ངོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་བསམ་པའི་བྱེ་བྲག་གོ་བར་བྱེད་ནུས་པ་མེད་པའི་ཕྱིར་ཆོས་གོས་གསུམ་པོ་ཉིད་ཀྱིས་ཀྱང་ཆོས་གོས་ལྷག་པ་ཉིད༌[^335]ཀྱང་རིག་པར་བྱའོ། །
--- END BLOCKS ---
