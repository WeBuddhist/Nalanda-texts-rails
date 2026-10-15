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
[Block 3326]
གླེང་བ་པོ་ཉིད་ཀྱང་དེ་བཞིན་ནོ། །

[Block 3327]
འདི་ལ་གྲངས་ཀྱི་བྱེ་བྲག་ནི་ངེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་གླེང་བར་བྱ་བ་དང་གླེང་བ་པོ་གཉིས༌[^3351]ལ་གླེང་བར་བྱ་བ་ཇི་སྙེད་པ་དེ་སྙེད་པ་ཁོ་ནའི་གླེང་བ་པོ་དག་གིས་བྱ་བར་མ་ངེས་པའོ། །

[Block 3328]
གླེང་བ་པོ་ལུས་དང་ངག་དག་གིས་བསྡམས་པ་ཉིད་དང་། སྡེ་སྣོད་དག་ཤེས་པ་ཉིད་དང་། དགེ་འདུན་གྱི་ནང་དུ་བསམས་བཞིན༌[^3352]དུ་ཆོས་དང་འདུལ་བ་ལོག༌[^3353]པ་དང་། དེ་བཟློག་པ་དག་མི་སྟོན་པ་ཉིད་ཅེས་བྱ་བ་གསུམ་དང་ལྡན་པ་ལ་གུས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་བཟློག་པར་ཞེས་བྱ་བ་ནི་ཆོས་དང་འདུལ་བ་མ་ཡིན་པ་ལས་ཏེ། ཆོས་ཀྱང་ཤེས་བྱ་རྣམ་པར་གཞག་པ་ལས་རིག་པར་བྱའོ། །

[Block 3329]
འདུལ་བ་ནི་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པའི་ཆོ་གའོ། །

[Block 3330]
གླེང་བ་པོ་གང་ཞིག་ལུས་དང་ངག་དག་གིས་བསྡམས་པ་ཉིད་དང་། སྡེ་སྣོད་དག་ལ་མཁས་པ་ཉིད་དང་། དགེ་འདུན་གྱི་ནང་དུ་བསམས་བཞིན་དུ་ཆོས་དང༌[^3354]ཆོས་མ་ཡིན་པར་མི་སྟོན།[^3355] ཆོས་མ་ཡིན་པ་ཆོས་སུ་མི་སྟོན་པ་དང་། [^3356]འདུལ་བ་འདུལ་བ་མ་ཡིན་པར་མི་སྟོན་པ་དང་། འདུལ་བ་མ་ཡིན་པ་འདུལ་བར་མི་སྟོན་པའི་གླེང་བ་པོ་འདི་ལྟ་བུ་ལ་གུས་པར་བྱའོ། །

[Block 3331]
ཚུལ་ཁྲིམས་འཆལ་པ་དང་ལོག་པར་སྟོན་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གླེང་བ་པོ་ཚུལ་ཁྲིམས་འཆལ་པ་དང་། ཆོས་དང་འདུལ་བ་ཆོས་མ་ཡིན་པ་དང་། འདུལ་བ་མ་ཡིན་པར་ལོག་པར་སྟོན་པ་ལ་ནི་མཐུན་པར་མི་བྱ་སྟེ། མི་བགྲང༌[^3357]ཞིང་སྨད་པ་དང་ཚིག་གིས་ཅུང་ཟད་ཀྱང་བསྒྲུབ་པར༌[^3358]མི་བྱའོ། །

[Block 3332]
དགོས་པ་དང་ལྡན་པ་ཉིད་ཀྱིས་གླེང་བ་ལ་རྣམ་པ༌[^3359]གཞན་གྱིས་དེར་འདི་ལ་གླེང་བ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ངེས་པར་ཤེས་པ་ལ་མཐུན་པར་བྱ་བའོ།[^3360] །ངེས་པར་ཤེས་པ་མེད་པ་ལ་འདི་ལ་གུས་པར་མི་བྱ་བ་ཉིད་དོ། །

[Block 3333]
ཁ་ཅིག༌[^3361]ནི་ལོག་པར་སྟོན་པ་ལ་སྣང་བ་དང་། རབ་ཏུ་སྣང་བ༌[^3362]དེ་དཔྱད་པར་བྱ་ཞེས་ཟེར་བ་སྟེ། འཇོམས་པ་དང་རབ་ཏུ་འཇོམས་པ་མ་ཡིན་པར་ཞེས་བྱ་བར་སྨྲ་སྟེ་དེ་ནི་མི་རིགས་སོ། །

[Block 3334]
འདི་ལྟ་བུའི་དོན་རྣམས་ལ་ཚུལ་ཁྲིམས་ཉམས་པ་དང་། ལྟ་བ་ཉམས་པ་ལས་གུས་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3335]
རྣམ་པ་དེ་ལྟ་བུ་མ་ཡིན་པ༌[^3363]སྡེ་སྣོད་དག་འཛིན་ཅིང་མི་ཤེས་པ་ལ་ནི་བློན་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གླེང་བ་པོ་ལོག་པར་སྟོན་པའི་རྣམ་པ་དེ་ལྟ་བུ་མ་ཡིན་པ་ལུས་དང་ངག་དག༌[^3364]གིས་བསྡམས་པ༌[^3365]དེ་ལ་སྡེ་སྣོད་འཛིན་པ་པོ་སྟེ་མི་ཤེས་པ་ལ་བློན་གདབ་པར་བྱའོ། །

[Block 3336]
མི་ཤེས་པ་ཉིད་ཀྱིས་གླེང་བར་བྱེད་པ་ལ་ཞེས་བྱ་བ་གང་དུ་ངེས་པར་ཤེས་པར་བྱ་བ་ལ་དེར་ལན་གདབ་པ་ངེས་པར་བྱའི་ཤེས་པ༌[^3366]ལ་གུས་པར་མི་བྱ་བ་ཉིད་དོ། །

[Block 3337]
གང་ཞིག་གླེང་བ་པོ༌[^3367]ཡོན་ཏན་གསུམ་དང་ལྡན་པ་ལ་གུས་པར་བྱའོ་ཞེས་ཇི་སྐད་བསྟན་པ་དེ་ལ་བརྟག་པ་ཙམ་ཡང་མི་བྱའམ་ཞེ་ན། དེའི་ཕྱིར། དེ་ལ་བསམ་པ་རྟོགས་པར་བྱ་བའི་ཕྱིར་བརྒལ༌[^3368]ཞིང་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སེམས་ཀྱི་སྤྱོད་པ་ནི་གཡོ་བ་ཡིན་པས་སྔར་སྡིག་པ་ལ་མ་ཞུགས་སུ་ཟིན་ཀྱང་ཕྱིས་འཇུག་སྲིད་པས་དེའི་ཕྱིར་སེམས་ཀྱི་སྤྱོད་པ་བསྒོམ་པའི༌[^3369]ཕྱིར་བརྒལ༌[^3370]ཞིང་བརྟག་པར་བྱའོ། །

[Block 3338]
བསམ་པ་རྟོགས་པར་བྱ་བ་ནི་འདིར་བསམ་པ་རྟོགས་པར་བྱ་བ་སྟེ། འདིའི་བསམ་པ་ཇི་ལྟ་བུས་ཞེས་བྱ་བ་དེའི་དོན་དུའོ། །ཇི་ལྟར་བརྒལ༌[^3371]ཞིང་བརྟག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གནས་སུ་མི་གཞག་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^3372]འདི་ནི་ལོག་པའི་བསམ་པ་རྗེས་སུ་བརྩལ་བ༌[^3373]ཡིན་གྱི། ཡང་དག་པའི་བསམ་པ༌[^3374]རྗེས་སུ་བརྩལ་བར༌[^3375]བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3339]
དུས་ལ་སོགས་པའི་གནས་སུ་གླེང་བའི་ཚིག་གིས༌[^3376]འཇོག་པར་མི་བྱེད་ན་ལོག་པར་གླེང་བ་ལ་ཞུགས་པར་ངེས་པ་ཡིན་པས་དེའི་ཕྱིར། གནས་སུ་མི་འཇོག་ན་བསམ་པ་ལོག་པར་ཤེས་པར་བྱའོ། །

[Block 3340]
གལ་ཏེ་གང་ཟག་དེ་ལ་བརྒལ༌[^3377]ཞིང་བརྟགས་པ་ན་དུས་ལ་སོགས་པའི་གླེང་བའི་ཚིག་འཇིག་པར༌[^3378]མི་བྱེད་ན་ཞེས་བྱ་བའོ། །

[Block 3341]
གང་དུ་མི་འཇོག་ན་བསམ་པ་ལོག་པར་མཚོན་པར༌[^3379]བྱ་བའི་གནས་དེ་དག་གང་ཞེ་ན་དེའི་ཕྱིར། གནས་སུ་ནི་དུས་དང་ཡུལ་དང་སྤྱོད་ལམ་དང་རྗེས་སུ་སྒྲུབ་པ་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དུས་ཞེས་སྨོས་པས་ནི་མཚན་མོ་བྱས་པས་གླེང་བ་དང་ཉིན་མོ་བྱས་པས་གླེང་བ་ལ་སོགས་པ༌[^3380]བསྡུས་སོ། །

[Block 3342]
ཡུལ་ཞེས་སྨོས་པས་ནི་ལྐོག་ཏུ་བྱས་པ༌[^3381]དང་གསལ་བར་བྱས་པ་དང་ལམ་དུ་བྱས་པ་དང་ལམ་གོལ་བར་བྱས་པ་དང་གྲོང་དུ་བྱས་པ་དང་དགོན་པར་བྱས་པ་ལ་སོགས་པ་བསྡུས་སོ། །

[Block 3343]
སྤྱོད་ལམ་ཞེས་སྨོས་པ་ནི་འགྲོ་བ་དང་འགྲེང་བ༌[^3382]དང་འདུག་པ་དང་ཉལ་བས་བྱས་པས་གླེང་བ་བསྡུས་སོ། །

[Block 3344]
རྗེས་སུ་བསྒྲུབ་པ་ཞེས་སྨོས་པས༌[^3383]ནི་ཕམ་པར༌[^3384]འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མ་དང་ལྟུང་བྱེད་དང་སོ་སོར་བཤགས་པར་བྱ་བ་དང་ཉེས་བྱས་སུ་བསྒྲུབ་པས་གླེང་བ་བསྡུས་སོ། །

[Block 3345]
གནས་གཞན་དུ་འཕོ་བ་དང་། རྙོག་པ་ཅན་དུ་གྱུར་ན་གླེང་བ་མི༌[^3385]འཆགས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གླེང་བ་པོ་དེ་ལ་གལ་ཏེ་དེ་ལྟར་བརྒལ་ཞིང༌[^3386]བརྟགས་པ་ན་གནས་ནས་གཞན་དུ་འཕོ་བ་དང་འཁྲུག་པའི༌[^3387]རྙོག་པ་ཅན་དུ་གྱུར་ན་དེའི་ཚེ། དེ་ལ་གླེང་བ་མི་འཆགས་པ་ཉིད་ཡིན་ཏེ། གླེང་བའི་བྱ་བ་མ་བྱས་པ་ཉིད་དང་། མ་བྱུང་བ་ཉིད་དང་མི་སྐྱེད་པ༌[^3388]ཉིད་ཡིན་ནོ། །

[Block 3346]
དེ་ཡོད་པ་ན་གླེང་བ་ཉིད་དང་གླེང་བ་པོ་མེད་པ་ཉིད་ཡིན་ཏེ། དེ་ཉིད་ཀྱིས་འདིར་དགོས་པ་འགྲུབ་པར་འགྱུར་ཏེ། དེ་ཡོད་ན་རྩོད་པ་ཉེ་བར་ཞི་བ་ཉིད་འགྲུབ་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 3347]
དེ་བས་ན་དེ་ལ༌[^3389]གླེང་བ་ལ་མི་འཆགས་སོ་ཞེས་སྨོས་སོ། །

[Block 3348]
གླེང་བས་ཁས་བླངས་ན་མཐར་ཐུག་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཟག་གང་ལ་གླེངས་པ༌[^3390]དེས་ལྟུང་བ་དེ་ཁས་བླངས་ན་དེ་ནི་འདིར་རྩོད་པའི་མཐར་ཐུག་པ་ཡིན་ཏེ། ཁས་བླངས་ན་རྩོད་པ་དེ་ཉེ་བར་ཞི༌[^3391]བར་འགྱུར་རོ། །

[Block 3349]
སྨྲ་བ་པོ་བདེན་པ་མཐོང་བ་ཉིད་དང་། ཡོན་ཏན་ལས་ཆེས་མཆོག་ཏུ་གྱུར་པ་ཁྱིམ་པ༌[^3392]ཡང་རུང་བ་གཞན་ཚད་མར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་ཐམས་ཅད་ཉིད་དེ་དོན་ཚོལ་བ་དང་དོན་བརྗོད་པའི་དབང་པོ་གླེང་བར་བྱ་བ་དང་། གླེང་བར་བྱེད་པ་སྨྲ་བ་པོ་ཉིད་ཀྱིས་གཟུང་བར་རིག་པར་བྱའི་ཆེ་བཞིར༌[^3393]གྱུར་པ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3350]
རབ་ཏུ་བྱུང་བ༌[^3394]འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་སྨྲ་བ་པོ་བདེན་པ་མཐོང་བ་ཉིད་དམ་ཁྱིམ་པ་ཡང་རུང་བ་གཞན་དག་ཚད་མར་བྱས་ཏེ། འདི་ནི་མི་གཡོ་བའི་ཆོས་དང་ལྡན་པ་ཉིད་ལ་དཔེ་ཙམ་དུ་རིག་པར་བྱ་སྟེ། ཡོན་ཏན་གཞན་གྱིས་ཀྱང་གང་ཞིག་བདེན་པ་ལས་མི་གཡོ་བ་དེ་ཡང་འདིར་བསྡུས་པ་ཉིད་དོ། །

[Block 3351]
མི་གཡོ་བའི་ཆོས་བྱེད་པ་ལས་གཞན་གང༌[^3395]ཡིན་པ་དེ་ལ་ཡོན་ཏན་ལས་ཆོས་མཆོག་ཏུ་གྱུར་པ་ཉིད་ཚད་མར་བྱ་སྟེ། དེ་དག་ཆེ་བཞིར་དྲིའོ༌[^3396]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3352]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གཉིས་ལ་ཐ་དད་པར་སྨྲ་བ་དང་འགལ་བར་སྨྲ་བ་དང་མི་མཐུན་པར་སྨྲ་བ་དག་བྱུང་བ་ན། གང་གི་ཚིག་གཟུང་བར་བགྱི། གང་ཚུལ་ཁྲིམས་དང་ལྡན་པའི་འོ།[^3397] །གཉིས་ཀ་ཚུལ་ཁྲིམས་དང་ལྡན་ན་གང་མང་དུ་ཐོས་པའི་འོ།[^3398] །གཉིས་ཀ༌[^3399]མང་དུ་ཐོས་པ་ལགས་ན་གང་ཡང་དག་པར་བསྡམས་པའི་འོ། །

[Block 3353]
གཉིས་ཀ་ཡང་དག་པར་བསྡམས་པ་ལགས་ན་གང་ཆེས་ཡང་དག་པར་བསྡམས་པའི་འོ། །

[Block 3354]
གཉིས་ཀ་ཆེས་ཡང་དག་པར་བསྡམས་པ་ལགས་ན་དེ་ནི་གནས་མ་ཡིན་སྐབས་མ་ཡིན༌[^3400]ཏེ། གལ་ཏེ་གཉིས་ཀ་ཆེས་ཡང་དག་པར་བསྡམས་པ་ལ་ཐ་དད་པར་སྨྲ་བ་དང་འགལ་བར་སྨྲ་བ་དང་མི་མཐུན་པར་སྨྲ་བ་དག་འབྱུང་བ་དེ་ནི་གནས་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3355]
གཞན་དང་བཅས་པ་ཉིད་ན་ཚིག་བསྟུན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆེ་བཞི༌[^3401]དེ་ལ་གལ་ཏེ་གཞན་ཕ་རོལ་པོ་ཉེ་བར་གནས་པར་གྱུར་ན་གཞན་དེ་ལ་དྲི་བར༌[^3402]བྱ་བ༌[^3403]ཡིན་ཞིང་དེ་དང༌[^3404]ལྷན་ཅིག་དེའི་ཚིག་གོ་བར་བྱའོ། །

[Block 3356]
མི་གཡོ་བ་རྙེད་པ་འདི་དག་གིས་འཁྲུལ་བ་མེད་པ་ཤེས་པར་བྱ་བའི་ཕྱིར་དེ་བསྐོའོ། །

[Block 3357]
མ་རྙེད་པ་མི་གཡོ་བའི་ཆོས་དང་ལྡན་པ་ལ༌[^3405]མ་ཤེས་པ་ཤེས་པའི་དོན་དུ་བསྐོ་བ་འདིའོ། །

[Block 3358]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་བསྙེན་མ་དད་པ་ཅན་དགེ་སློང་རྣམས་ཀྱི་དྲུང་དུ་མཆིས་ཏེ། འདི་སྐད་ཅེས་བཙུན་པ་དག་བདག་གིས་དགེ་སློང་ཞིག་རྒྱལ་རིགས་མོ་དང་ལྷན་ཅིག་མི་ཚངས་པར་སྤྱོད་པས་ཉམས་པར་བགྱིད་པ་མཐོང་ངོ་ཞེས་མཆི་ན། བགྱིད་དུ་སྩལ་ཅིང་དེ་ལ་དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་དང་མཐུན་པ་བསྩལ་བར༌[^3406]བགྱིའམ་ཉེ་བ༌[^3407]འཁོར་མི་བྱ་སྟེ། དྲི་བར༌[^3408]བྱ་ཞིང་གལ་ཏེ་དེ་ན་སྲིང་མོ༌[^3409]གཞན་གང་ཞིག་ཀྱང༌[^3410]ཡོད་དོ་ཞེས་ཟེར་ན་གཉིས་ཀ་དྲི་བར༌[^3411]བྱའོ། །

[Block 3359]
གལ་ཏེ་མཐུན་ན་དགེ་བསྙེན་མ་དད་པ་ཅན་གྱི་ཚིག་གིས་བྱེད་དུ་གཞུག་ཅིང་དེ་ལ་དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་དང་མཐུན་པ་ཡང༌[^3412]སྦྱིན་པར་བྱའོ། །

[Block 3360]
གལ་ཏེ་འདིས་རྒྱལ་རིགས་མོ་དང༌[^3413]མི་ཚངས་པར་སྤྱོད་པ་མ་བྱས་ཀྱི། འདིས་བྲམ་ཟེ་མོ་དང་ལྷན་ཅིག་མི་ཚངས་པར་སྤྱོད་པ་བྱས་སོ་ཞེས་ཟེར་ན་དགེ་སློང་གིས་དམ་བཅས་པས་བྱེད་དུ་གཞུག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3361]
ཐེ་ཚོམ་ཉིད་དུ་གྱུར༌[^3414]ན་ཤེས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དོན་གང་ལ་ཐེ་ཚོམ་ཉིད་དུ་གྱུར་པ་དེས་དོན་དེ༌[^3415]ཤེས་པ་ཉིད་མ་ཡིན་ཏེ། འདི་ལྟར་ངེས་པའི་ཤེས་པ་མ་བསྐྱེད་པའི༌[^3416]ཕྱིར་རོ། །

[Block 3362]
གང་ལ་བརྗོད་པ་གཞན་ལ་གླེང་བར་བྱས་པ་ལ་དུས་མ་ཡིན་པར་ལི་ཁ་རའི་ཆུ་འཐུང་བ་ལ་སོགས་པ་མཐོང་ནས་དཔང་པོ་དང་གླེང་བ་པོ་དག་གིས་ཅིག་ཤོས་བྱས་པར་ཐེ་ཚོམ་ཟ་བ་ཉིད་དུ་ཐོབ་པར་གྱུར་པ་ལ་དེས་བརྗོད་པར་གྱུར་པ་ལ༌[^3417]དེས་ཤེས་པ་དང་བྲལ་བ་ཉིད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3363]
དེས་རྩོད་པ་དེ་ལ་རྣམ་པར་གཞག་པ༌[^3418]མེད་པར་དེ་བས་ན་འདི་ལ་དོན་གྱིས་བྱས་པའོ། །

[Block 3364]
འདིར་ཐེ་ཚོམ་ཟ་བར་གྱུར་པ་ཉིད་འདི་ནི་དཔེ་ཡིན་ཏེ་གཡོ་བའི་དབང་གིས་བརྗོད་པ་ལའོ། །

[Block 3365]
ངག་གི་རྣམ་པར་འགྱུར་བ་ནི་རྙོག་པ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
