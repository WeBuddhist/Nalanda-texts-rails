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
[Block 351]
རྗེས་སུ་བསྒྲུབ་པ་ལ་འདི་བྱེད་པ་པོ༌[^241]ཉིད་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟོས་པའི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར་དེ་ནི་མིད་ན་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟོས་པ་དེ་ནི་མིད་ན་དངོས་གཞིར་གྱུར་པའི་ཟོས་པའོ། །

[Block 352]
གང་ཞིག་འདུན་ནས་ཞེས་བྱ་བ་འདིར་དོན་མ་ཡིན་ནོ། །

[Block 353]
གཞན་གྱི་དོན་དུ་ན་ན་སྨད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་དུ་དགེ་སློང་མས་སྦྱོར་དུ་བཅུག་པ་གཞན་གྱིས༌[^242]ཟ་བ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 354]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གཞན་གྱི་དོན་དུ་སྦྱོར་དུ་བཅུག་པར་ཤེས་བཞིན་དུ་ཟོས་ན་ཉེས་བྱས་སོ། །

[Block 355]
མི་ཤེས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 356]
རང་གི་ཆོས་མེད་པ་ལ་ཇི་ལྟ་བུའི་རྣམ་པར་ཉེ་བར་འཚེ་བ་ལྟ་བུ་ནི་གཞན་གྱི་ཆོས་ལ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཡང་བ་ནི་འདི་ཡིན་ཏེ་དེ་བས་ན་འདི་ཤེས་པའོ། །

[Block 357]
བསོད་སྙོམས་ལ་ཞུགས་པ་ན་བྱིན་ཅིག་ཅེས་ཟེར་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱིན་ཅིག་ཅེས་བྱ་བ་འདི་ལྟར་ན་སྨད་པ་ཉིད་བྱས་པ་ཉིད་དོ། །ཅིའི་དོན་དུ༌[^243]བྱིན་ཅིག་ཅེས་བརྗོད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བསོད་སྙོམས་ལ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 358]
གནས་སྐབས་གང་ལ་ལྟུང་བ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཞུགས་པ་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། བསོད་སྙོམས་ལ་ཞེས་བྱ་བ་སྦྱར་རོ། །

[Block 359]
ཁྱིམ་གྱི་ནང་དུ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 360]
ཁྱིམ་གྱི་ནང་དུ་བསོད་སྙོམས་ཀྱི་ཕྱིར་ཞུགས་པ་ལ་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བའི་དོན་བསྡུས་པ་དང་། བྱིན་ཅིག་ཅེས་བྱ་བ་ཡང་བརྗོད་པ་ལ་ན་སྨད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 361]
འདིར་དང་པོ་བཤགས་པར་བྱ་བའི་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། དེ་ན་དགེ་སློང་མ་ཞིག་ཁྱིམ་བདག་ལ་འདི་སྐད་ཅེས་དགེ་སློང་འདི་ལ་བསོད་སྙོམས་བྱིན་ཅིག་ཅེས་མཆི་ཞིང་དགེ་སློང་དེས་ཀྱང་དེ་བླངས་ཏེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 362]
སྦྱོར་དུ་བཅུག་པ་ལ་རིགས་འདྲི་བ༌[^244]འདི་ནི་ཚིག་ཡིན་ཏེ། དེའི་ཕྱིར་འདི་དང་འབྲེལ་བ་ཉིད་ལ་ཁ་ན་མ་ཐོ་བ་འདི་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ཅེས་བྱ་བ་འདིར་གྲགས་པ་ཡིན་ནོ། །

[Block 363]
དགེ་སློང་མས་སྦྱོར་དུ་བཅུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 364]
ཁྱིམ་གཞན་དུ་ཡང་ཟན་ལ་བོས་པ་དང་དུ་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་གཙུག་ལག་ཁང་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཁྱིམ་གཞན་དུ་ཡང་ངོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུའོ། །

[Block 365]
གནས་མལ་གྱི་ལྟུང་བྱེད་ལས་འདི་ལ་སོགས་པ་སྐོམ་གྱི་ཕྱིར་ཞེས་བྱ་བའི་བར་དུ་འདི་དྲངས་པའོ། །

[Block 366]
དུས་ཤེས་པར་བྱ་སྟེ་འཇུག་པར་བྱའི་སྔ་ཚོམས༌[^245]སུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་ཁྱིམ་གཞན་དུ་གང་དུ་བོས་པ་འདི་དང་དུ་བླངས་པར་གྱུར་ན་ཞེས་བྱ་བ་དེ་མ་ཐག་པ་ལས་རྟོགས་པའོ། །ཇི་ལྟར་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཎྜཱི་བརྡུངས་ཏེ་རང་གི་འཁོར་ལ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་གཞན་དུ་མགྲོན་དུ་བོས་པ་ལའོ། །

[Block 367]
གློ་བུར་དུ་འོངས་པ་ལ་ནི་གནས་བརྟན་གྱིས་སོ་ཞེས་བྱ་བ་ནི་འཁོར་དེ་ལ་གནས་བརྟན་གང་ཡིན་པ་དེས་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་གྱིས་རྟོགས་པའོ། །

[Block 368]
འདིར་དགེ་འདུན་གྱིས་གནས་བརྟན་ལ་གནས་བརྟན་དུ་བརྗོད་པ་ཞེས་བྱ་བའོ། །

[Block 369]
དེ་བས་ན་འདིར་གཞུང་ནི་ཡིད་ཆེས་པའི་འཁོར་གྱི་ནང་དུ་སྤྱོད་པའི་དགེ་སློང་གི་འཁོར་ལ་བལྟས་ཏེ་འགྲོ་བར་བྱའོ། །

[Block 370]
གང་ཞིག་དགེ་སློང་གློ་བུར་དུ་འོངས་པ་དེ་ལ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་བལྟ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 371]
གྱ་ཚོམ་དུ་ཟན་གཅད་པར༌[^246]མི་བྱའོ། །

[Block 372]
སྐོམ་གྱི་ཕྱིར་གསོལ་བ་དག༌[^247]འདེབས་ན་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། ཡང་ཡང་ཟ་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཅིག་ཅར་ཡང་རུང་ཕྱིས་ཀྱང་རུང་སྟེ་གོས་ཀྱི་རྙེད་པ་མེད་པའི་མགྲོན་དུ་བོས་པ་རྙེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་ཀྱི་རྙེད་པ་མེད་པའི་མགྲོན་དུ་བོས་པ་གཉིས་པ་རྙེད་པ་ནི་བྱེད་པ་པོ་ཡིན་ཏེ། ཅིག་ཅར་རམ་དུས་གང་ལ་མགྲོན་དུ་བོས་པ་གཅིག་ལ་རྙེད་པ་དེ་ཉིད་ལ་ཡང་རྙེད་པ་གཞན་གྱི་ཕྱི་ནས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 373]
ཅིག་ཅར་དང་དུ་ལེན་པར་བྱེད་པ་ལ་གཉིས་ཀ་ལ་ཡང་གལ་ཏེ་གོས་མེད་པ་ཉིད་ཡིན་ན་གང་ལ་ཕྱིས་བཟའ་བ་མཐོང་བ་དེ་ལས་ཆོས་ཉིད་ཀྱིས་ཉེས་བྱས་བསྐྱེད་པའོ། །

[Block 374]
གལ་ཏེ་གཅིག་ལ་གོས་མེད་པ་ཞེས་བྱ་བ་རིག་པར་བྱའོ། །

[Block 375]
འདིར་གོས་དང་བཅས་པ་དང་གོས་མེད་པ་དང་གོས་དང་བཅས་ཤིང་གོས་ཀྱི་རིན་དང་ཡང་བཅས་པ་དང་། གོས་མེད་ཅིང་གོས་ཀྱི་རིན་ཡང་མེད་པ་རྣམ་པ་བཞིས་ལྟུང་བ་བསྟན་པར་མཛད་དོ། །

[Block 376]
དེ་ལ་གོས་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་གོས་དང་བཅས་པ་གཞན་ནས་འདིར་གོས་ལ་བོས་པའོ། །

[Block 377]
གོས་མེད་པ་ཞེས་བྱ་བ་ནི་གོས་དང་བཅས་པ་གཞན་ནས་འདིར་གོས་མེད་པ་ལ་བོས་པའོ། །

[Block 378]
གོས་དང་བཅས་ཤིང་གོས་ཀྱི་རིན་དང་ཡང་བཅས་པ་དང་། གོས་མེད་ཅིང་གོས་ཀྱི་རིན་ཡང་མེད་པ་གཉིས་ཀ་བརྩམས་པ་ཡིན་ཏེ། དེ་ནི་འདིར་མི་འདུས་པར་ཤེས་པར་མི་བྱའོ། །

[Block 379]
གོས་གཅིག་པ་ཡིན་མོད་དུ་མ་འམ་གང་ཡང་རུང་བ་གོས་དང་བཅས་པ་ཉིད་ཀྱི་འདིར་དགོས་པའོ། །

[Block 380]
དེ་བས་ན་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 381]
ཁ་ཅིག་ནི་གོས་དང་བཅས་ཤིང་གོས་ཀྱི་རིན་དང་ཡང་བཅས་པ་ཞེས་བྱ་བ་དང་། གོས་མེད་ཅིང་རིན་ཡང་མེད་པ་ཞེས་བྱ་བ་ལ་རྣམ་པ་གཉིས་པོ་འདི་དག་ལ་གོས་ཀྱི་རིན་ཞེས་བྱ་བ་ནི་གོས་དང་ལྡན་པ་ཞེས་བྱ་བ་སྨྲས་པ་ཡིན་ཏེ། འདིས་ཀྱང་གོས་དང་བཅས་པ་ཉིད་རིག་པར་བྱའོ། །

[Block 382]
དེ་བས་ན་དེ་ལ་འདི་བསྟན་པ་སྟེ། དེ་ཡང་འདིར་བསྡུས་པར་ཤེས་པར༌[^248]བྱ་བ་མ་ཡིན་ནོ། །

[Block 383]
གོས་བརྟག་པ་ཉིད་ཀྱིས་དེའི་རིན་ཐང་བཟུང་བ་སྟེ། ཟས་ཙམ་ལ་བརྟེན་ནས་སླར་མགྲོན་དུ་བོས་པ་ལ་འདོད་པ་ཚོལ་བར་མངོན་པ་ཡིན་གྱི། རྙེད་པ་གཞན་ལ་བརྟེན་ནས་འཇུག་པ་ལ་འདི་སྐྱེ་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་རྣམ་པར་གཞག་པའོ། །ཅི་ཞིག་ལ་མགྲོན་དུ་བོས་པ་ལ༌[^249]ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 384]
ཇི་ལྟར་ལ་ཡིན་ན་དེའི་ཕྱིར་ལྔའི་ཁོངས་སུ་གཏོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྲས་ཆན་དང་ཟན་དྲོན་དང་ལྡེ་གུ་དང་ཤ་དང་སྣུམ་ཁུར་ཞེས་བྱ་བ་ལྔ་པོ་གང་ཡང་རུང་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 385]
མགྲོན་དུ་བོས་པ་སྔ་མ་ལས་གཉིས་པའི་རྙེད་པ་བྱེད་པ༌[^250]པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གཞན་ཡང་དེ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་བཟའ་བར་བྱ་བ་དེ་ཉིད་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ལྔ་པོས་དང་པོར་མགྲོན་དུ་བོས་པ་རྙེད་པ་དེ་ལ་ནི་བྱེད་པ་པོ་ཉིད་ཡིན་ལ་གལ་ཏེ་དེ་ཉིད་མ་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 386]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་སྔར་བཟའ་བ་མ་ལགས་པ་ལ་གཡར་དྲངས་ན། དེ་སླད་ཀྱིས་བཟའ་བ་ལ་གཡར་དྲངས་ཏེ་དེས་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ། །

[Block 387]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་བཟའ་བ་ལྔ་པོ་རྣམས་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་བཟའ་བ་དག་ལ་སྔར་གཡར་དྲངས་ནས་དེ་སླད་ཀྱིས༌[^251]བཟའ་བ་ལྔ་པོ་རྣམས་ལ་གཡར་དྲངས་ཏེ་དེས་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་ཐམས་ཅད་ལ་ལྟུང་བ་འདི་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ན་བ་མ་ཡིན་པ་དང་ལས་མ་བྱས་པ་དང་། ལམ་དུ་མ་སོང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ན་བ་ལ་སོགས་པར་གནས་པའི་དུས་དང་ལྡན་པ་རྣམས་ལ་ལྟུང་བ་མེད་དོ། །

[Block 388]
གནས་པ་མ་ཡིན་པའི་དུས་ཐམས་ཅད་ལ་ནི་ཉས་བྱས་སོ་ཞེས་གསུངས་པ་མི་གནས་པའི་དུས་ལ་ཉེས་བྱས་ཞེས་བྱ་སྟེ། དེ་བས་ན་ཉེས་བྱས་སུ་གཏོགས་པར་བྱའོ། །

[Block 389]
རྙེད་པ་གང་ལ་གང་གི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེ་བླངས་ན༌[^252]ཉེས་བྱས་ཀྱིའོ། །

[Block 390]
ཟོས་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དང་དུ་བླངས་ཡིད་ཀྱི་ཡིན་པའི་ཕྱིར་དེ་ནི་བསྡམ་པར་བྱ་བའི་ཉེས་བྱས་སུ་གསུངས་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
