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
[Block 5986]
གང་ལས༌[^3822]བདག་གི་ཡིད་ནི་འགྱོད་འགྱུར་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་བདག་ནི་དེ་གཉི་གའི་དོན་གྱི་ཚུལ་མེད་པ་ཡིན་ཏེ།

[Block 5987 [VERSE]]
དེས་ན་འཆི་བའི་འཇིགས་པ་མེད་དོ་ཞེས་པའོ། །
ཕོངས་པ་རྣམས་ནི་སློང་དུ་འོངས་པ་ལ། །

[Block 5988]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བསྟན་མ་ཐག་པ། དཀར་པོའི་ལས་ཀྱང་རབ་ཏུ་གོམས་བྱས་པ། །ཞེས་བྱ་བ་སྟེ། དཀར་པོའི་ཆོས་བྱས་པའི་ཕྱིར་རོ། །

[Block 5989]
ཆོས་ལ་གནས་པ་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། མགུ་བ་རྙེད་པར་འགྱུར་ཞེས་བྱ་བ་སྟེ། སློང་དུ་འོངས་པ་ལ་ནོར་ཐོབ་པས་མགུ་བ་ཡིན་ཏེ། ཕོངས་པ་རྣམས་མི་མགུ་བར་བྱས་པ་ནི་མེད་དེ་མ་དྲན་པའོ། །

[Block 5990]
བདག་གིས་བྱས་པར་ཡང་མི་དྲན་ཞེས་བྱ་བ་དེ་གང་ཡིན་ཞེ་ན་དེ་ཉིད་བསྟན་པའི་ཕྱིར། རིང་དུ་བརྟགས་ཏེ་བསམས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5991]
སྡིག་པ་བྱས་པར་ཡོངས་མི་དྲན། །ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལ་སོགས་པའོ། །

[Block 5992]
ཡིད་ལ་བསམས་པ་ཙམ་ཡང་ཞེས་བྱ་བ་ནི་ཡོད་པར་བཀོད་པ་ཡིན་པས་ཡིད་ལ་བསམས་པའོ། །

[Block 5993]
ཡང་ན་ཡིད་ཉིད་བསམས་པ་ཡིན་པས་ཡིད་ལ་བསམས་པ་སྟེ། སེམས༌[^3823]བསྐྱེད་པ་ཙམ་ཡང་མ་དྲན་ནོ་ཞེས་བྱ་བའི་དོན་ཏེ། [^3824]དེ་ལྟར་རྣམ་པ་གཉིས་ཀྱིས་མཐོ་རིས་ཀྱི་ལམ་སྦྱངས་པ་གང་ཡིན་པ་དེ་ནི་མཐོ་རིས་ལམ་སྦྱངས་སོ། །

[Block 5994]
དེ་ལྟར་དེ་གཉིས་ཀྱིས༌[^3825]ཆོས་ལ་འཇུག་པ་དང་། སྡིག་པ་ལས་ལྡོག་པའི་ཚུལ་ལོ། །

[Block 5995]
ཕོངས་པ་རྣམས་ནི་སློང་དུ་འོངས་པ་ལ། མགུ་བར་མ་བྱས་པ་ནི་ཡོངས༌[^3826]མི་དྲན། །ཞེས་བསྟན་པ་ལ། ཕོངས་པ་དེ་དག་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། བྲམ་ཟེ་རྣམས་དང་གཉེན་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5996]
དེ་ལ་བྲམ་ཟེ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་ཞིང་ངོ་། །གཉེན་དང་མཛའ་བོ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པའི་ཞིང་ངོ་། །བརྟེན་པ་དང་ཕོངས་པ༌[^3827]ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི༌[^3828]ཞིང་ངོ་། །ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཕན་འདོགས༌[^3829]མགུ་བར་བྱེད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། དེ་དག་ལ་ནོར་མང་པོ་བཞག་ཅིང་ཇི་ལྟར་འོས་པའི་སྦྱིན་པས་ཕོངས་པ་རྣམས་མགུ་བའི་ཕྱིར་རོ། །

[Block 5997]
ཡང་ན་ནོར་ཤིན་ཏུ་མང་པོ་ཅི་རིགས་པར༌[^3830]སྦྱིན་པ་ཡིན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དང་གཉི་ག་ཡང་དགའ་བའི༌[^3831]ཕྱིར་རོ། །

[Block 5998]
གང་གི་བྱ་བ་ཅི་ཡོད་དེ་ཡང་བདག་གིས་བྱས་པ་ཞེས་བྱ་བ་ནི་གཞན་དག་ཀྱང་རྗེས་སུ་བསྟན་པའོ། །

[Block 5999]
ང་མི་འཇིགས་ཞེས་བྱ་བ་ནི་ཆོས་ལ་གནས་པའི་ཕྱིར་དང་། མཐོ་རིས་ཀྱི་ལམ་སྦྱངས་པའི་ཕྱིར་རོ། །

[Block 6000]
དེ་བྱས་དགའ་བར་གྱུར་པས་ཞེས་བྱ་བ་ནི་ཆོས་ལ་གནས་པ་དགའ་བ་ཐོབ་པའི་ཕྱིར་དང་། མཐོ་རིས་ཀྱི་ལམ་སྦྱངས་པའི་ཕྱིར་རོ། །

[Block 6001]
ཡང་ན་བྲམ་ཟེ་ལ་སོགས་པ་ནོར་མང་པོ་བཞག་པའི་ཕྱིར་དགའ་བར་འགྱུར་བ་སྟེ། རྒྱུ་རྣམ་པ་གཉིས་ཀྱིས་དགའ་བ་ཡིན་ནོ། །

[Block 6002]
བདག་གི་སྤྱོད་པ་ནི་བདག་གི༌[^3832]སྤྱོད་པའོ། །

[Block 6003]
བདག་གི་སྤྱོད་པ་ཉིད་གཟུགས་ཡིན་པས་བདག་གི་སྤྱོད་པའི་གཟུགས་ཏེ་ངན་པའོ། །

[Block 6004]
དེ་ནི་དེ་ལྟ་བུའི་ཆོས་ཀྱི་མེ་ལོང༌[^3833]ལའོ། །

[Block 6005]
དགའ༌[^3834]དང་ལྡན་པའི་མིག་གིས་ལྟ། །[^3835]ཞེས་བྱ་བ་འདིས༌[^3836]ནི་ཆོས་འཆད་པ་ལ་གུས་པ་དང་ལྡན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6006]
ཚིག་གི་བདུད་རྩི་འཐུང་བ་བཞིན། །ཞེས་བྱ་བ་འདིས༌[^3837]ནི་ཚིག་ལ་རྣ་གཏོད་པ་ཉིད་དོ། །

[Block 6007 [VERSE]]
གུས་པ་བསྐྱེད་ཅིང་རྩེ་གཅིག་བཏུད། །
རབ་ཏུ་དང་ལ་དྲི་མེད་ཡིད། །

[Block 6008]
ཅེས་བྱ་བ་འདིས་ནི་དོན་ལ་རྣ་གཏོད་པ་ཉིད་ཀྱིས་དམ་པའི་ཆོས་མཉན་པར་བྱའོ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་དག་གིས་ནི་དམ་པའི་ཆོས་མཉན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 6009]
ཇི་ལྟར་འདོད་པར་ཕྲད་ཀྱང་རུང་། །ཞེས་བྱ་བ་ནི་དམ་པ་དག་དང་འགྲོགས་པ་ལ་དགོངས་པ་ཡིན་ཏེ། བསྙེན་བཀུར་མ༌[^3838]བྱས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6010]
ལན་ཅིག་ཙམ་ཞེས་བྱ་བ་འདིས་ནི་རྟག་ཏུ་བྱེད་པ་མེད་པ༌[^3839]ཉིད་དོ། །

[Block 6011]
བསྙེན་བཀུར་བྱས་པ་མེད་ཀྱང་སྐྱེ་བོ་དམ་པ་དང་འགྲོགས་པ་བརྟེན་པ༌[^3840]ཉིད་དུ་བསྟན་ཏོ། །

[Block 6012]
རབ་ཏུ་བརྟན་པ་ཉིད་དུ་འགྱུར། ། ཞེས་བྱ་བ་འདིས་ནི་དེ་ལ་རྟག་ཏུ་བྱས་པ་མེད་ཀྱང་དུས་ཡུན་རིང་དུ་གནས་པ་ཐོབ་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6013]
འདྲིས་པ་དང་བྱ་བ་ནི་འདྲིས་པར་བྱ་བའོ།[^3841] །འདྲེས་པར་བྱ་བ་དེ་ལ་མི་ལྟོས་པ་ནི་འདྲིས་པར་བྱ་བ་ནི་མི་དགོས་པར་རོ། །

[Block 6014]
བསྙེན་བཀུར་བྱས་པའི་བྱ་བ་ཡང་མི་དགོས་ཏེ། ཇི་ལྟར་ཕྲད་ཀྱང་རུང་བའི་ཕྱིར་རོ། །

[Block 6015]
ཇི་ལྟར་ཕྲད་ཀྱང་རུང་སྟེ། དམ་པ་དག་དང་འགྲོགས་པ་ནི་བརྟན་པར་འགྱུར་ཏེ། དེ་ཅིའི༌[^3842]ཕྱིར་ཞེ་ན། བྱ་བ་མི་དགོས་པ་སྟེ། སྐྱེ་བོ་དམ་པ་དག་དང་འགྲོགས་པ་ལ༌[^3843]བྱ་བ་མི་དགོས་པའི་ཕྱིར་རོ། །

[Block 6016]
འདི་ལྟར་འདྲིས་པ་ལ་ལྟོས་པ་ཡིན་ན་ནི༌[^3844]ལན་ཅིག་ཕྲད་པས་གཏན་དུ་མི་འགྱུར་ཏེ་ཅིའི་ཕྱིར་ཞེ་ན། འདྲིས་པ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 6017]
མགོ་བསྒྱུར་བ་དང་། སེ་གོལ་གཏོགས་པ༌[^3845]གཉིས་ནི་མགོ་བསྒྱུར་སེ་གོལ་གཏོགས༌[^3846]པའོ། །

[Block 6018]
དམ་པ་རྣམས་ནི་སུས་ཀྱང་མི་བསྲིང༌[^3847]ངོ་། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་ནི། དམ་པ་དག་དང་ལྷན་ཅིག༌[^3848]ཙམ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་རྗེས་སུ་བསྟན་པའོ། །

[Block 6019]
སྔར་བསྟན་པའི་ཇི་ལྟར་འདོད་པར་ཕྲད་པར༌[^3849]རུང་སྟེ་ཞེས་བྱ་བའམ།[^3850] གུས་པར་བྱེད་པ་དང་། རྟག་ཏུ་སྦྱོར་བ་གཉིས་དང་བྲལ་བ་ལ་ཡང་དམ་པ་དག་དང་འགྲོགས་པ་དང་བརྟན་པ་དང་། གཏན་དུ་བ་ཉིད་བསྟན་ཏོ། །

[Block 6020]
ད་ནི་གུས་པ་དང་རྟག་ཏུ་བྱ་བའི་སྦྱོར་བས་དམ་པ་དག་དང་འགྲོགས་པར་འདོད་པ་དང་སྒྱར་བའི་ཕན་ཡོན་བསྟན་པར་འདོད་པས། [^3851]དམ་པ་རྣམས་ནི་སུས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་བརྩམས་སོ། །

[Block 6021]
དམ་པ་རྣམས་ནི་སུས་ཀྱང་མི་བསྲིང༌[^3852]ངོ་། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་དམ་པ་དག་དང་འགྲོགས་ན་གཏན་དུ་བ༌[^3853]ཡིན་པའི་ཕྱིར་རོ། །

[Block 6022]
དུལ་བའི་ཚུལ་གྱིས༌[^3854]དགེ་ལ་བསྟན་པར༌[^3855]བྱ། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཇི་ལྟར་འདོད་ཀྱང་རུང་སྟེ་ཞེས་བྱ་བ་ཡིན་ཏེ། དམ་པ་དག་དང་འགྲོགས་པ་ནི་བརྟན་པའི༌[^3856]ཕྱིར་རོ། །

[Block 6023]
དགེ་བདག་ལ་བསྟེན་པ༌[^3857]ཇི་ལྟར་བྱ་ཞེ་ན། སྨྲས་པ། དུལ་བའི་ཚུལ་དུ་བྱ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་གུས་པར་བྱེད་པའི་སྦྱོར་བ་ཉིད་དུ་སྦྱོར་བ་ཡིན་ནོ། །

[Block 6024]
དམ་པ་དག་དང་འགྲོགས་པ་ལ་དེ་གཉི་གའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་སྨྲས་པ། དེ་དང་ཉེ་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་ཡིན་ནོ། །

[Block 6025]
ཆེད་དུ་མ་བསྒྲུབས་པར་ཡང་ཞེས་བྱ་བ་ནི་བསྟན་བཅོས་ཉན་པ་ལ་སོགས་པའི་བྱ་བ་མ་བྱས་པར་ཡང་སྟེ། མ་བསྲིངས་པ་དེ་ཙམ་སྟེ། མ་བསྲིངས་པ་དང་དུལ་བའི་ཚུལ་ཙམ་གྱིས་སོ། །
--- END BLOCKS ---
