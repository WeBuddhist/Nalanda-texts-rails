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
[Block 3781]
ཤར་གྱི་མཚམས་ནས་བརྩམས་ཏེ་ཞེས་པ་ནི་མེ་དང་། བདེན་བྲལ་དང་རླུང་དང་དབང་ལྡན་གྱི་མཚམས་རྣམས༌[^2363]སུའོ། །

[Block 3782]
མི་གཡོ་བ༌[^2364]ལ་སོགས་པ༌[^2365]དགོད་པར་བྱའོ་ཞེས་པ་ནི༌[^2366]མི་གཡོ་མགོན་དང་འདོད་པའི་རྒྱལ་པོ་དང་དབྱུག་སྔོན་ཅན་དང་སྟོབས་པོ་ཆེ་དགོད་པ་ནི་བསམ་པར་བྱའོ། །

[Block 3783]
ཤར་ཕྱོགས་སུ་ནི་སྣམ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནང་གི་དཀྱིལ་འཁོར་གྱི་ཕྱི་རོལ་དུ་སྣམ་བུ་བཞི་ལ་ནི་ཤར་དུ་སའི་སྙིང་པོ་དང་བྱམས་པ་དག་གོ། །

[Block 3784]
ལྷོའི་སྣམ་བུ་ལ་ནམ་མཁའི་སྙིང་པོ་དང་ཕྱག་ན་རྡོ་རྗེ་དག་གོ། །

[Block 3785]
ནུབ་ཀྱི་སྣམ་བུ་ལ་འཇམ་དཔལ་དང་འཇིག་རྟེན་དབང་ཕྱུག་གོ། །

[Block 3786]
བྱང་གི་སྣམ་བུ་ལ་ནི་ཀུན་དུ་བཟང་པོ་དང་སྒྲིབ་པ་རྣམ་པར་སེལ་བ་དག་དགོད་པ་ནི་བསྒོམ་པར༌[^2367]བྱའོ། །

[Block 3787]
ནང་གི་དཀྱིལ་འཁོར་ཞེས་པ་ནི་གང་དུ་བཅོམ་ལྡན་འདས་མི་བསྐྱོད་པ་དབུས་སུ་བཞུགས་པ་དང་། ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་རྣམ་པར་སྣང་མཛད་དང་། རིན་ཆེན་འབྱུང་ལྡན་དང་། སྣང་བ་མཐའ་ཡས་དང་། དོན་ཡོད་གྲུབ་པ་དགོད་པའོ། །

[Block 3788]
མཚམས་སུ་ནི་སངས་རྒྱས་སྤྱན༌[^2368]དང་། མཱ་མ་ཀཱི་དང་། གོས་དཀར་མོ་དང་། སྒྲོལ་མ་དགོད་པར་བྱའོ། །

[Block 3789]
དེའི་དཀྱིལ་འཁོར་གྱི་ཕྱི་རོལ་གྱི་བྱང་ཤར་གྱི་མཚམས་ནས་བརྩམས་ཏེ་ཞེས་པ་ལ་ནང་གི་དཀྱིལ་འཁོར་གྱི་ཕྱི་རོལ་དང་བྱང་ཆུབ་སེམས་དཔའི་སྣམ་བུའི་བར་དུ་གྲྭ༌[^2369]རྣམས་ལ་གཟུགས་རྡོ་རྗེ་ལ་སོགས་པ་དགོད་དོ་ཞེས་པ་ནི་གཟུགས་རྡོ་རྗེ་མ་དང་། སྒྲ་རྡོ་རྗེ་མ་དང་། དྲི་རྡོ་རྗེ་མ་དང་། རོ་རྡོ་རྗེ་མ་རྣམས་དགོད་དོ། །

[Block 3790]
རེག་བྱ་རྡོ་རྗེ་མ་ནི་དབུས་ཀྱི་བདག་པོ་ལ་བརྟེན་ཏེ་བཞུགས་སོ། །

[Block 3791]
སྟེང་དང་འོག་དག་ཏུ་ནི་གནོད་མཛེས་དང་གཙུག་ཏོར་དགོད་དོ་ཞེས་རིག་པར༌[^2370]བྱའོ། །

[Block 3792]
དེ་ལྟར་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ཀྱི་དཀྱིལ་འཁོར་ཡིན་ནོ། །

[Block 3793]
ཐམས་ཅད་ཀྱི་གདན་ལ་སོགས་པའི་ངེས་པ་ཞེས་བྱ་བ་ནི་གདན་དང་སྐུ་མདོག་དང་ཕྱག་མཚན་ལ་སོགས་པའི་ངེས་པའོ། །

[Block 3794]
སྒྲུབ་ཐབས་སུ་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་པ་ནི་མདོར་བསྡུས་པའི་སྒྲུབ་ཐབས་སམ་ཡང་ན་རང་གིས་བྱས་པ་ལས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3795]
དེ་ལྟར་ན་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་དཀྱིལ་འཁོར་གང་ལས་རྟོགས་པར་བྱ༌[^2371]སྟེ། བཅུ་གསུམ་ལས་མ་བསྟན་ཞེ་ན། སྨྲས་པ། ལྷ་ཡི་རྣལ་འབྱོར་ཇི་ལྟ་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ལྷའི་རྣལ་འབྱོར་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 3796]
དཀྱིལ་འཁོར་ནི་རྟེན་དང་བརྟེན་པའི་མཚན་ཉིད་དོ། །

[Block 3797]
གཞན་དག་ཏུ་བཤད་པའི་རྒྱུད་ལ་སོགས་པར་རོ། །

[Block 3798]
རྫོགས་པ་ནི་མ་ལུས་པའོ། །

[Block 3799]
བཅོམ་ལྡན་འདས་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོས་སོ། །

[Block 3800]
མ་གསུངས་པ་ནི་མ་བསྟན་པའོ། །

[Block 3801]
སློབ་དཔོན་མེད་པར་འཇུག་པར་མ་གྱུར་ཅིག་སྙམ་དུ་དགོངས་པ་ཡིན་ནོ་ཞེས་པ་ལ། སློབ་དཔོན་དང་སློབ་མའི་རིམ་པ་ཇི་ལྟ་བ༌[^2372]བཞིན་དུ་གྱུར་ཅིག་ཅེས་དགོངས་ནས་སོ། །

[Block 3802]
གཞན་དུ་ན་གླེགས་བམ་ཀློག་པ་ཙམ་གྱིས་བདག་ཅག་སློབ་དཔོན་ཡིན་ཞེས་སྨོས་པ་རྣམས་ལ་ང་རྒྱལ་སྐྱེ་བར་གྱུར་པས་སོ། །

[Block 3803]
དེ་བཞིན་དུ་འདིར་ཡང་ཞེས་པ་ནི། དཔལ་གསང་བ་འདུས་པའི་ལེའུ་དང་པོ་ལས་ཀྱང་མ་བསྟན་ཏོ། །

[Block 3804]
སྐུའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་མ་ལུས་པ་ཉེ་བར་སྡུད༌[^2373]པའི་དུས་སུ་དཀྱིལ་འཁོར་པ་ཐམས་ཅད་སྐུའི་དཀྱིལ་འཁོར་དུ་བསྒོམ་པར་བྱའོ། །

[Block 3805]
དེ་བཞིན་དུ་ཕྱུང་བའི་དཀྱིལ་འཁོར་ལ་ཡང་ཞེས་པ་ནི༌[^2374]ཕྱུང་བའི་དུས་སུ་ཡང་ལྷ་སུམ་ཅུ་རྩ་གཉིས་དེ་བཞིན་དུ་སྤྲོ་བར་བྱའོ། །

[Block 3806]
[^2375]དེ་ལྟ་ན་གང་མ་གྲུབ་པས་གྲུབ་པར་བྱེད་པ་དེ་ཡང་མ་གྲུབ་པ་ཉིད་ཅེས་འབྱུང་བས་སྐུའི་དཀྱིལ་འཁོར་ཉིད་ལ་ཡང་ངེས་པ་འདི༌[^2376]ག་ལས་འགྱུར་ཞེ་ན། སྨྲས་པ། བཅོམ་ལྡན་འདས་ཉིད༌[^2377]ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལན་བསྟན་ཏོ། །

[Block 3807]
བཤད་པའི་རྒྱུད་ཅེས་པ་ནི། རྡོ་རྗེ་ཕྲེང་བ་ལས་སོ། །

[Block 3808]
འདུས་པ་རྣམས་ལ་ཞེས་པ་ནི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་གསང་བ་འདུས་པའི་རྣལ་འབྱོར་པ་རྣམས་ལའོ། །

[Block 3809]
དོན་ཐེ་ཚོམ་མེད་པར་ཞེས་པ་ནི་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ལྷ་བཅུ་གསུམ༌[^2378]གྱི་བདག་ཉིད་ཡིན་ནམ་སུམ་ཅུ་རྩ་གཉིས་ཡིན་ཞེས་ཐེ་ཚོམ་མེད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3810]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། སེམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སེམས་དཔའ་ཆེན་པོ་ཞེས་པ་ནི་ཁྲོ་བོའི་རྒྱལ་པོ་གཤིན་རྗེ་གཤེད་ལ་བོད་པའོ། །

[Block 3811]
གང་གི་ཕྱིར་རྡོ་རྗེ་ཕྲེང་བའི་རྒྱུད་ལས་ནི་གཤིན་རྗེ་གཤེད་ཁོ་ན་ཞུ་བ་པོ་ཡིན་ནོ། །

[Block 3812]
རྡོ་རྗེ་སློབ་དཔོན་ལུས་འདི་ལ། །ཞེས་པ་ནི་རྡོ་རྗེ་སློབ་དཔོན་གྱི་ལུས་བཤད་པའི་སྒོ་ནས་རྡོ་རྗེ་འཆང་བའི་སྐུ་ཁོ་ན་བསྟན་པར་འགྱུར་ཏེ། བདེན་པར་རྡོ་རྗེ་སློབ་དཔོན་དང་རྡོ་རྗེ་འཆང་ཆེན་པོར་དབྱེར་མེད་པ་ཡིན་ནོ། །

[Block 3813]
རྒྱལ་བའི་སྐུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ༌[^2379]རྒྱལ་བ་དང་། རྒྱལ་བའི་སྲས་ནི་རྒྱལ་བའོ། །ཞེས་མི་འདྲ་བ་རྣམས་ལ་གཅིག་ལྷག་མའི་བསྡུ་བའོ།[^2380] །

[Block 3814]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་ཀྱི་སྐུ་གནས་པ་ཉིད་བསྟན་ཏོ། །

[Block 3815]
དང་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ་རྡོ་རྗེ་སློབ་དཔོན་ཉིད་ཀྱི་ལུས་ཞེས་བྱ་བའི་བར་དུ་ནི་གོ་སླའོ། །

[Block 3816]
འོན་ཀྱང་དཀྱིལ་འཁོར་པ་ཐམས་ཅད་ལ་དེ་བཞིན་གཤེགས་པའི་ཚིག་གི་ཁྱད་པར་ནི་ལོངས་སྤྱོད་རྫོགས་པ་དང་སྤྲུལ་པའི་སྐུ་དབྱེར་མེད་པར་བསྟན་པའོ། །

[Block 3817]
གཟུགས་ལ་སོགས་པ་ཡང་རྣམ་པར་དག་པར་ཤེས་པར་བྱའོ། །

[Block 3818]
གང་གི་ཕྱིར་རྡོ་རྗེ་ཕྲེང་བ་ལས།

[Block 3819]
གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པ་རྣམས་སྐུའི་དཀྱིལ་འཁོར་ལ་དགོད་པ༌[^2381]མ་བསྟན་ཏོ་ཞེས་པ༌[^2382]ནི་ལོགས་ནས་སྨྲ་བར་བྱའོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དཀྱིལ་འཁོར་པ་རྣམས་ཀྱི་ཁ་དོག་ལྔ་གང་ཡིན་པ་དེ་ནི་གཟུགས་རྡོ་རྗེ་མའོ། །

[Block 3820]
སྔགས་བརྗོད་པའི་སྒྲའམ་རྗེས་སུ་ཆགས་པའི་སྒྲ༌[^2383]རྡོ་རྗེ་མའོ། །
--- END BLOCKS ---
