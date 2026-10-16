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
བརྒྱ་སྟོང་ཕྲག་དུ་མ་གྲངས་མང་པོའི་ཞེས་བྱ་བ་ནི། སྟོང་ཕྲག་དུ་མས་རྒྱ་ཆེ་བའི་གྲངས་གང་ཡིན་པ་དེ་ནི་དེའི་བརྒྱ་ཕྲག་དུ་མས་གྲངས་མང་པོའོ། །

[Block 3782]
དེ་བས་ན་ངང་པའི་ཁྱུ་ཆེན་པོ་ཡིན་ནོ། །

[Block 3783]
རིགས་པ་དང་མི་རིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་གིས་ནི་སྙན་ངག་གི་གཙུག་ལག་ཏུ་བསྟན་པའི་བློན་པོའི་རང་བཞིན་གྱི་ཡོན་ཏན་ཉི་ཤུ་རྩ་ལྔ་དང་ལྡན་པ་སྟེ། བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ཡིན་པར་ཅི་རིགས་པར་གཟུང་ངོ་། །དེ་དག་ལས་ཀྱང་ཁྱད་པར་དུ་གྱུར་པ་སྟེ། དེ་རྣམས་ཀྱི༌[^2456]དཔོན་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3784]
རིགས་པ་དང་མི་རིགས་པ་ཡོངས་སུ་ཤེས་པར་བྱ་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་འདིས་ནི་ཤེས་རབ་ཅན་དུ་བསྟན་ཏོ། །

[Block 3785]
ཡུན་རིང་པོར༌[^2457]ཡང་དྲན་པའི་མཐུ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཡུན་རིང་པོར་བྱས་པ་དང་། ཡུན་རིང་པོར་སྨྲས་པ་དང་། ཡུན་རིང་དུ་བསམས་པ་དང་། ཡུན་རིང་དུ་ཐོབ་པ་རྣམས་དྲན་པའོ། །

[Block 3786]
གཞན་དག་ཡུན་རིང་དུ་དྲན་པའི་མཐུ་ཞེས་སྨོས་པས༌[^2458]དྲན་པ་ཀུན་ཏུ་དག་པ་ཉིད་དོ། །

[Block 3787]
རིགས་མཐོན་པོའི་ནང་ན་གཙོ་བོར་གྱུར་པ་ཞེས་བྱ་བ་འདིས་ནི་རིགས་མཐོ་བ་སྔ་ན་མེད་པ་ཁྱད་པར་ཅན་ཉིད་དུ་བསྟན་ཏོ།[^2459] །མཁས་པ་ནི་ལེ་ལོ་མེད་པའོ། །

[Block 3788]
དེས་པ་ནི་ལེགས་པར་བྱེད་པ་ཉིད་དོ། །

[Block 3789]
དུལ་བ་ནི་ལུས་དང་ངག་གི་ལས་དག་པའོ། །

[Block 3790]
མཁས་པ་དང་། དེས་པ་དང་། དུལ་བ་ཉིད་ཀྱི་རྒྱན་གང་ལ་ཡོད་པ་དེ་ནི༌[^2460]མཁས་པ་དང་། དེས་པ་དང་། དུལ་བས་བརྒྱན་པའོ། །

[Block 3791]
བརྟན་པ་ནི་རྟག་ཏུ་མི་འགྱུར་བའི་ཕྱིར་ཏེ། བདག་དང་གཞན་གྱི་ཕྱོགས་ལ་ཁྲོ་བ་སྤངས་པར་གྱུར་པའོ། །

[Block 3792]
ཚུལ་ཁྲིམས་ལ་བརྟེན་ནས་སྤྱོད་པ་དང་། མི་སྤྱོད་པའི་ཚུལ་གང་དང་གང་དག་ལ་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་པར་བྱ་བ་དེ་དང་དེ་དག་ལ་དེ་བཞིན་དུ་འཇུག་པའོ།[^2461] །སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ནི་རིགས་བྱས་པའི་རྒྱུའོ། །

[Block 3793]
ཚུལ་ཁྲིམས་དང་། སྤྱོད་ཚུལ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་ནི་ཚུལ་ཁྲིམས་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3794]
བརྟན་པ་དང་། གཙང་བ་དང་། ཚུལ་ཁྲིམས་དང་། སྤྱོད་ཚུལ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་གང་ལ༌[^2462]ཡོད་པ་དེ་ནི་བརྟན་པ༌[^2463]དང་། གཙང་བ་དང་། ཚུལ་ཁྲིམས་དང་། སྤྱོད་ཚུལ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3795]
སྡུག་བསྔལ་བཟོད༌[^2464]ཅིང་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3796]
བག་ཡོད་པ་ཞེས་བྱ་བ་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ༌[^2465]རྗེས་སུ་འབད་པའོ། །

[Block 3797]
གཡུལ་ངོར་འགྱེད་པའི་དགྲ་ཐབས་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་དམག་གི་དགོད་པའི་རིགས་པ་དང་། ཡུལ་དང་དུས་དང་། མདུན་དུ་བསྣུར་བ་དང་། ཕྱིར་འགྱེད་པ་ལ་སོགས་པ་ལ་མཁས་པའོ། །

[Block 3798]
རྗེ་བོ་ལ་སྙིང་ཉེ་ཞིང་ལེགས་པར་ལྟ་བ་ཞེས་བྱ་བ་ནི་རྗེ་བོ་ལ་རྗེས་སུ་ཆགས་ཤིང་བརྟེན་པའི༌[^2466]གུས་པ་ཉིད་དོ། །

[Block 3799]
[^2467]དེ་ཉིད་ཀྱི་ཕྱིར། བཞིན་བཟངས་ཞེས་བྱ་བའི་མིང་དུ་བྱས་པའོ། །

[Block 3800]
སློབ་དཔོན་སློབ་མའི་གཙོ་བོ་བཞིན། །ཞེས་བྱ་བ་ནི༌[^2468]འཇིག་རྟེན་ཕ་རོལ་ལ་ཕན་པའོ། །

[Block 3801]
ཕ་དང་བུ་རབ༌[^2469]ཐུ་བོ་བཞིན། །ཞེས་བྱ་བས་ནི་འཇིག་རྟེན་འདི་ལ་ཕན་པ་ཉིད་དོ། །

[Block 3802]
དེ་ལྟར་འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པའོ། །

[Block 3803]
ལྷ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་ཡིད་བཞིན་གྱི་མཚོ་སྟེ། བརྟན་པའི༌[^2470]ཡུལ་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 3804]
དཀའ་ཐུབ་ཅན་ཞེས་སྨོས་པས་ནི་མངོན་པར་ཤེས་པའི་མཐུ་ཁྱད་པར་ཅན་གཟུང་བའི༌[^2471]ཕྱིར་རོ། །

[Block 3805]
བདེ་བ་ཉིད་ལུས་ཡིན་པས་བདེ་བའི་ལུས་སོ། །

[Block 3806]
དེའི་འདེགས་པ་ནི་བདེ་བའི་ལུས༌[^2472]འདེགས་པ་ཉིད་དོ། །

[Block 3807]
དེ་གཉིས་སྤྱོད་པ་གཅིག་ཏུ་གྱུར་པ་གང་ཡིན་པ་དེ་ནི། བདེ་བའི་ལུས་འདེགས་སྤྱོད་པ་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 3808]
གྲུབ་པ་གང་ཡིན་པ་དེ་དྲང་སྲོང་ཡིན་པས་གྲུབ་པ་དྲང་སྲོང་དག་སྟེ། གང་གི་རྫུ་འཕྲུལ་གྱིས་མི་སྣང་བ་དག་གོ། །

[Block 3809]
གྲུབ་པའི་དྲང་སྲོང་དང་། རིག་འཛིན་དང་། ལྷ་རྣམས་ནི་གྲུབ་པའི་དྲང་སྲོང་དང་། རིག་སྔགས་འཆང་དང་། ལྷའོ། །

[Block 3810]
དེ་རྣམས་ཀྱི་ཚོགས་ནི་གྲུབ་པ་དང་། དྲང་སྲོང་དང་། རིག་སྔགས་འཆང་དང་། ལྷ་མང་པོའོ། །

[Block 3811]
འདིར་ཅིའི་ཕྱིར་སྔར་བཤད་པའི་ཀླུ་མ་སྨོས་ཤེ་ན།

[Block 3812 [VERSE]]
དེ་ནི་ངེས་པར་གནས་པ་ཡིན་པའི་ཕྱིར་རོ། །
གསེར་མཆོག་བཙོ་མའི་ཁ་དོག་འདྲ་བའི་མདོག །

[Block 3813]
ཅེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་ལུས་དང་། ངག་དང་། ཡིད་ལ་བརྟེན་ནས་དེའི་གྲགས་པ་ཁྱད་པར་དུ་སྟོན་པ་ཡིན་ཏེ། གསེར་མཆོག་བཙོ༌[^2473]མའི་ཁ་དོག་འདྲ་བའི་མདོག །དཔལ་ལྡན་ལུས་ཞེས་བྱ་བས་ནི་ལུས་ཁྱད་པར་དུ་བསྟན་ཏོ། །

[Block 3814]
དུལ་ཞིང་རིགས་པ་ཆོས་ཀྱི་ཚུལ་ལས་བྱུང་། །ཞེས་བྱ་བས་ནི་ཡིད་ཀྱི་ལས་ཁྱད་པར་དུ་བསྟན་ཏོ། །

[Block 3815]
ངེས་པར་གཞན་ཞེས་བྱ་བ་ནི་ལྷ་ལ་སོགས་པར༌[^2474]ཁྱད་པར་ཅན་ཞིག་སྟེ། ངང་པའི་ཚུལ་ཞེས་བྱ་བ་ནི་ངང་བའི་ཆ་ལུགས་ཅན་ནོ། །

[Block 3816]
དེས་ན་ངང་པའི་ཚུལ་ཅན་འདི་གཉིས་ངེས་པར་གཞན་ཞེས་བྱ་བར་སྟོན༌[^2475]ཏོ། །

[Block 3817]
ཡོན་ཏན་བསྒྲགས་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཅན་བསྟན་པ་དང་། ཡོན་ཏན་གསལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏེ། དེ་དང་བྲལ་བ་ད༌[^2476]ནི་ཕྲག་དོག་སྟེ། ཕྲག་དོག་མེད་པས་སོ། །

[Block 3818]
རྒྱས་པར་གྱུར་ཞེས༌[^2477]བྱ་བས༌[^2478]ནི་གཞན་དང༌[^2479]གཞན་དེ་དག་གིས་གྲགས་པ་རྒྱ་ཆེར་བྱས་ཤིང་ཡོན་ཏན་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་གྲགས་པ་རྒྱས་པར་གྱུར་པ་དེ༌[^2480]བས་ན་དད་པ་སྐྱེས་པར་གྱུར་པ་སྟེ། ཡོན་ཏན་དང་ལྡན་པའི་ཚིག་ནི་གཟུང་བར་འོས་པའི་ཕྱིར་རོ། །

[Block 3819]
འདི་དག་ནི་སྔར་བསྟན་པ་རྣམས་ཏེ། གྲུབ་པ་དྲང་སྲོང་ལ་སོགས་པ་དང་། གང་ཡང་གཞན་དག་ལས་དེའི་གྲགས་པ་ཐོབ་པར་གྱུར་པ་དེས་གཅིག་ལ་གཅིག་བརྒྱུད་དེ་རྒྱས་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3820]
སྐྱེས་དང་འདྲ་བར་གྱུར་ཞེས་བྱ་བ་ནི་གང་ལས་ཐོས་པའི་གྲགས་པ་དེ་ཡང་གཞན་དག་ལ་སྟོན་ཏེ། དེས་ཀྱང་གཞན་དག་ལ་བརྟེན་པ༌[^2481]ཡིན་པས་ཉེ་བར་བརྒྱུད་པ་དེས་ན་སྐྱེས་དང་མཉམ་པར་གྱུར་པའོ། །
--- END BLOCKS ---
