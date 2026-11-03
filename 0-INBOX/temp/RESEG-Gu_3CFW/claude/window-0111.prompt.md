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
[Block 3886]
སྣོད་དུ་བཅུག་སྟེ་རྩིག་པ་ལ་གཞག་གོ་ཞེས་བྱ་བ་ནི་འདྲེག་མཁན་གྱི་ལག་ཆའོ། །

[Block 3887]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 3888]
དགེ་སློང་གིས༌[^4013]དགེ་འདུན་གྱི་ཕྱིར་འདྲེག་མཁན་གྱི་ལག་ཆ་བཅང་བར་བྱ་ཞིང་སྣོད་དུ་བཅུག་སྟེ་རྩིག་པ་ལ་གཞག་པར་བྱའོ་ཞེས༌[^4014]གསུངས་པ་ཡིན་ནོ། །

[Block 3889]
སྟེའུ་དང་སྟ་རེ་དང་གཟོང་ལ་སོགས་པ་དང་དེ་དག་གི་སྣོད་དང་བཅས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དགེ་འདུན་གྱིས་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^4015]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། དེ་དག་གི་སྣོད་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་སྟེའུ་དང་སྟ་རེ་དང་གཟོང་ལ་སོགས་པ་དེ་དག་གི་སྣོད་དོ། །

[Block 3890]
འདིར་གཞུང་ནི་ཤིང་དག་གཤགས༌[^4016]པར་མི་ནུས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་འདུན་གྱི་ཕྱིར་སྟེའུ་དང་སྟ་རེ་དང་གཟོང་བཅང་བར་བྱའོ། །

[Block 3891]
དགེ་སློང་ཞིག་གི་ཁྲི་ཆག་ནས་དགེ་སློང་དེས་སྨྲས་པ༌[^4017]ན་ཁོ་བོ་ལ་གཟོང་ཡོད་དེ་ཞེས་བྱ་བ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དབེན་པའི་ཕྱོགས་སུ་བྱའོ། །

[Block 3892]
དགེ་འདུན་གི༌[^4018]སྟེའུ་དང་སྣོད་ཀྱང་བཅང་བར་བྱའོ། །

[Block 3893]
གང་ཟག་གིས༌[^4019]འཆང་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3894]
དེས༌[^4020]གཡར་པོ་ཉིད་དུ་ས་ལས་བྱས་པ་ཡན་ཆད་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དེས་དགེ་སློང་དེ་ལ་ལག་ཆའི་སྣོད་ཐ་ན་ས༌[^4021]ལས་བྱས་པ་ཡན་ཆད་ཀྱང་གཡར་པོ་ཉིད་དུ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3895]
དགེ་སློང་མས་མཆིང་བུའི་སྣོད་བཅང་བར་མི་བྱའོ། །

[Block 3896]
ཐམས་ཅད་ཀྱིས་འབྲུ་མར་གྱི་སྣོད་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དང་དགེ་སློང་མ་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 3897]
ཕུལ་གང་མན་ཆད་ནས་ཕུལ་ཕྱེད་ཡན་ཆད་ཤོང་བའོ་ཞེས་བྱ་བ་ནི། འདིར་ཡན་ཆད་ཀྱི་སྒྲ་བྲི་བར་བྱ་སྟེ་ཕུལ་ཕྱེད་ཡན་ཆད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3898]
ལྕགས་ཀྱི་དོག་ལེ་ཡང༌[^4022]ངོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱིས་བཅང་བར་བྱའོ། །

[Block 3899]
དེའི་ལྕགས་སྒྱེད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི་དོག་ལེའི༌[^4023]ལྕགས་སྒྱེད་རྐང་པ་གསུམ་པའམ། རྐང་པ་བཞི་པ་ཡང་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3900]
ས་ལས་བྱས་པའི་ཐབ་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རྒྱ་ཐབ་དང་སྒྱེད་པོ་ཡང་བཅང་བར་བྱའོ། །

[Block 3901]
གནང་བ་ཐོབ་པས་འཁར་བའོ་ཞེས་བྱ་བ་ནི་གནང་བ་ཐོབ་པ་ཐམས་ཅད་ཀྱིས་བཅང་བར་བྱའོ། །

[Block 3902]
དྲ་བ་ཁ་དོག་གཅིག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར༌[^4024]དྲ་བ་ཞེས་བྱ་བ་ནི་བྱ་རྒྱའི་རྣམ་པ་ལྟ་བུ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདི་ཉིད་དུ་དེ་གྲགས་པའི་ཕྱིར་རོ། །

[Block 3903]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་དྲ་བ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བཀའ་སྩལ་པ་དང་། དྲུག་སྡེ་དག་གིས་ཚོན་སྣ་ལྔའི་དྲ་བ་དག་ཉེ་བར་བཞག་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཚོན་སྣ་ལྔའི་དྲ་བ་དག་ཉེ་བར་གཞག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3904]
དེའི་ཕྱིར་དྲ་བ་ཁ་དོག་གཅིག་པ་ཡང༌[^4025]ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3905]
གནང་བ་འདི་དག་ལ་སྦྱིན་པར་རིགས་སམ་ཞེ་ན། དེའི་ཕྱིར་དེ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3906]
ཅི་ཐམས་ཅད་ལའམ་ཞེ་ན་དེའི་ཕྱིར་རྒས་པ་དང་ནད་པ་དག་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3907]
དེ་གཉིས་ཚིག་གཅིག་གིས༌[^4026]སྦྱིན་པ་ཡང་སྲིད་དོ་ཞེས་བྱ་བ་ནི་གཅིག་གིས་ཞེས་བྱ་བ་ནི་སྔགས་ཀྱི་ཚིག་གཅིག་གིས་སོ། །

[Block 3908]
སྡིག་སྦྲུལ་ལ་སོགས་པའི་གཉེན་པོའི་ཕྱིར་འཁར་བ་སྒྲ་དང་བཅས་པ་བཅང་ངོ་ཞེས་བྱ་བ་ལ། སྔར་རྒན་པོ་དང་ནད་པ་དག་ལ་གནང་བ་སྦྱིན་པའི་འཁར་བ་ནི་ལུས་རྟེན་པའི་ཕྱིར། བེ་ཅོན་སྦོམ་པོ་རྗེས་སུ་གནང་བ་ཡིན་ནོ། །

[Block 3909]
དེ་དང་མི་འདྲ་བའི་ཕྱིར་དེ་བས་ན་འདིར་རྗེས་སུ་མཐུན་པར་ངེས་པ་སྟེ་དེ་ལས་གཞན་པའི་སྐབས་ཀྱི༌[^4027]བྱེ་བྲག་མེད་དོ། །

[Block 3910]
དེ་བས་ན་དེ་འཆང་བའི་ཆོ་ག་འདི་དགོས་པ་གཞན་གྱི༌[^4028]བརྗོད་པར་ཤེས་པར་བྱའོ། །

[Block 3911]
མ་མོ་དག་ལས་དེ་དང་པོར་བྱ༌[^4029]སྟེ། དེ་བྱིན་པས་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3912]
ཡུ་བའི་རྩ་བ་ནས་གས་ན་སྦུ་གུ་བསྐོན་ནོ་ཞེས་བྱ་བ་ལ་འཁར་བའི་ཡུ་བ་དང་། འཁར༌[^4030]གསིལ་གྱི་ཡུ་བ་དང་། གོས་ཀྱི་སྲོག་ཤིང་གི་ཡུ་བ་དག་ཅེས་སྨོས་པས་གཟུང༌[^4031]བའོ། །

[Block 3913]
དེ་དག་གི་རྩ་བ་མ་ཐོག༌[^4032]གས་ན་ལྕགས་ཀྱི་སྦུ་གུ་ངོས་གཅིག་ནས་ཞབས་བཅུག་པ་བསྐོན་པར༌[^4033]བྱའོ། །

[Block 3914]
ཡ༌[^4034]ཐོག་དཀྲི་བས་སོ་ཞེས་བྱ་བ་ནི་ཡུ་བ་དེ་དག་གི་ཡ་ཐོག་གས་ན་དཀྲི་བ་བསྐོན་པར་བྱ་སྟེ། ལྕགས་ཀྱི་གླེགས་བུས་ཀུན་ནས་འཁོར་བར་དཀྲི་བར་བྱའོ། །

[Block 3915]
འདིར་གཞུང་ནི་རྒྱལ་པོའི་ཁབ་ཀྱི་གྲོང་ཁྱེར་གྱི་བསིལ་བའི་ཚལ་གྱི་དུར་ཁྲོད་ན་སྡིག་སྦྲུལ་དག་མང་བས་དེ་ན་དགེ་སློང་དུར་ཁྲོད་དུ་འགྲོ་བ་དག་སྡིག་སྦྲུལ་དག་གིས་ཟིན་པ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྡིག་སྦྲུལ་བཟློག་པའི་ཕྱིར་འཁར་བ་སྒྲ་དང་བཅས་པ་རྗེས་སུ་གནང་ངོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3916]
སྨྱིག་མ་མཁན་གྱིས་བྱས་པའམ་ལོ་མ་ལས་བྱས་པའི་གདུགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། སྨྱིག་མས་འཚོ་བ་ནི་སྨྱིག་མ་མཁན་ཏེ། དེ་ནི་སྐྱེ་བོ་ཐམས་ཅད་ཀྱི༌[^4035]དོན་དུ་གདུགས་ཁྲ་བོ་བཀྲ་བ་དག་བྱེད་པས་དེ་འདིར་ཉེས་པ་མེད་པར་བསྟན་པའི་ཕྱིར་སྨྱིག་མ་མཁན་གྱི་སྒྲས་སྨོས་པར་བྱའོ། །

[Block 3917]
དེ་ལས་གཞན་པ་ཁྲ་བོ་བཀྲ་བ་དག་བརྟག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 3918]
ཡུ་བ་ནི་ལུས་ཀྱི་ཚད་དོ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཚད་ཀྱི་ཡུ་བ་འདིར་ཞེས་བསྡུ་བའོ།[^4036] །དེས་གྲོང་དབུས་སུ་འགྲོ་བར་མི་བྱའོ༌[^4037]ཞེས་བྱ་བ་ལ་དེས་ཞེས༌[^4038]བྱ་བ་ནི༌[^4039]གདུགས་དེས་སོ། །

[Block 3919]
གལ་ཏེ་ལམ་གྱི་དབང་གིས་ན་གློར་བསྙལ༌[^4040]ཏེའོ། །

[Block 3920]
ཆར་འབབ་པ་ཉིད་ན་བསོད་སྙོམས་ལ་རྒྱུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གདུགས་ཀྱིས་གྲོང་དབུས་སུའོ། །

[Block 3921]
ཡུ་བ་ལ་གཞར་དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དྲི་མ་བཀྲུ་བར་བྱ་བའི་ཕྱིར་ཡུ་བ་ལ་བྱི་དོར་བྱ་བར་རིག་པར་བྱ་སྟེ། །འདིར་དེ་ལྟར་བརྗོད་པར་བྱའོ། །

[Block 3922]
ཆད་ན་ཁྱིམ་དག་ཏུ་གཞག་གོ་ཞེས་བྱ་བ་ནི་ཆར་པ་ཆད་ན་དེའི་དྲུང་དུ་འདུག་པའི༌[^4041]ཁྱིམ་གང་ཡིན་པ་དེར་གདུགས་དེ༌[^4042]བཏགས་ཏེ་གཞག་གོ། །

[Block 3923]
འབྱུང་ཁར་བླང་ངོ་ཞེས་བྱ་བ་ནི་གདུགས་གང་དུ་གཞག་པའི་གྲོང་དེ་ནས་ཕྱིར་འབྱུང་ཁར་དེ་བླང་ངོ་། །གཙུག་ལག་ཁང་ན་གནས་པའི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 3924]
ད་ནི་གནས་གཞན་ན་གནས་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། །རོལ་མོ་མཁན་གྱི་གནས་དང་། སྨད་འཚོང་མའི་གནས་དང་། ཆང་འཚོང་མའི་གནས་དང་། རྒྱལ་པོའི་ཕོ་བྲང་དང་། གདོལ་པའི་ཁྱིམ་གྱི་གནས་དག་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། རོལ་མོ་ཞེས་བྱ་བ་ནི་གླུ་མཁན་ལ་སོགས་པ་རྩེ་འཇོའི༌[^4043]གནས་སོ། །

[Block 3925]
གདོལ་པའི་ཁྱིམ་གྱི་གནས་དག་ཞེས་བྱ་བ་ནི་གདོལ་པའི་གནས་དག་གོ། །
--- END BLOCKS ---
