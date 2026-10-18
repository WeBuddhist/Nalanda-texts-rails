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
[Block 4726]
གཞན་མ་ཡིན་པར་ཡང་དམ་བཅའ་བར་མི་ནུས་ཏེ་ཆད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 4727]
རེ་ཞིག་ཀྱེ་བུད་ཤིང་ནི་ཅི། མེ་ནི་ཅི་ཡིན་པ་སྨྲོས་ཤིག་དང་། དེ་ལས་ཇི་ལྟར་ན་བུད་ཤིང་རྒྱུར་བྱས་ནས་མེ་འདོགས་པར་ཤེས་པར་བྱའོ། །

[Block 4728]
འདི་ལ་ཅི་ཞིག་བརྗོད་པར་བྱ། བསྲེག་བྱ་ནི་བུད་ཤིང་ཡིན་ལ་སྲེག་བྱེད་ནི་མེ་ཡིན་པར་ཟད་མོད། འདིར་བསྲེག་པར་བྱ་བ་ནི་ཅི། སྲེག་པར་བྱེད་པ་ནི་ཅི་ཡིན་པ་དེ་ཉིད་བརྗོད་པར་བྱའོ། །

[Block 4729]
རེ་ཞིག་འཇིག་རྟེན་ན༌[^3342]ནི་ཤིང་ལ་སོགས་པ་མ༌[^3343]འབར་བ་ལ་བུད་ཤིང་ཞེས་ཀྱང་བྱ་ལ་བསྲེག་བྱ་ཞེས་ཀྱང་བྱའོ། །

[Block 4730]
འབར་བ་ལ་ནི་མེ་ཞེས་ཀྱང་བྱ་ལ་སྲེག་བྱེད་ཅེས་ཀྱང་བྱ་སྟེ། འབར་བ་དང་ཤིན་ཏུ་ཚ་བ་གང་ཡིན་པ་དེས་དེ་ཚིག་པ་དང་སྲེག་པར་བྱེད་དེ། རྒྱུད་འགྱུར་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4731]
དེ་གཉི་ག་ཡང་རྫས་བརྒྱད་པ་ཡིན་ནོ། །

[Block 4732]
བུད་ཤིང་ལ་བརྟེན་ནས་མེ་འབྱུང་བ་དེ་ཡང་དཔེར་ན་འོ་མ་ལ་བརྟེན་ནས་ཞོ་འབྱུང་བ་དང་། མངར་པོ་ལ་བརྟེན་ནས་ཚ་བ༌[^3344]འབྱུང་བ་ལྟ་བུ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བུད་ཤིང་རྒྱུར་བྱས་ནས་ཞེས་བྱ་བ་ལ་དེ༌[^3345]ནི་དེ་དང་དུས་ཐ་དད་པའི་ཕྱིར་གཞན་པ་ཡང་ཡིན་ནོ། །

[Block 4733]
གལ་ཏེ་དེ་ལྟར་ཕུང་པོ་རྣམས་ལ་བརྟེན་ནས་གང་ཟག་སྐྱེ་ན་ནི་དེ་དག་ལས་གཞན་པ་དང་མི་རྟག་པར་ཡང་འགྱུར་རོ། །

[Block 4734]
འོན་ཏེ་ཤིང་ལ་སོགས་པ༌[^3346]འབར་བ་དེ་ཉིད་ལ་དྲོ་བ་ཉིད་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་མེ་ཡིན་ལ། དེ་དང་ལྷན་ཅིག་སྐྱེས་པའི་འབྱུང་བ་གསུམ་ནི་བུད་ཤིང་ཡིན་པར་འདོད་ན་ནི་དེ་གཉིས་ཀྱང་མཚན་ཉིད་ཐ་དད་པའི་ཕྱིར་གཞན་ཉིད་ཡིན་པར་གྲུབ་བོ། །

[Block 4735]
ཇི་ལྟར་ན་བུད་ཤིང་དེ་རྒྱུར་བྱས་ནས་མེ༌[^3347]འདོགས་པར་བྱེད་པ་རྒྱུར་བྱས་པའི་དོན་ཡང་བརྗོད་དགོས་ཏེ། དེ་ནི་དེའི་རྒྱུ་ཡང་མ་ཡིན་ལ་དེ་གདགས་པའི་རྒྱུ་ཡང་མ་ཡིན་གྱི་མ་ཉིད་དེ་གདགས་པའི༌[^3348]རྒྱུ་ཡིན་ནོ། །

[Block 4736]
གལ་ཏེ་རྒྱུར་བྱས་པའི་དོན་རྟེན་གྱི་དོན་ནམ་ལྷན་ཅིག་འབྱུང་བའི་དོན་ཡིན་ནོ་ཞེ་ན་ནི། ཕུང་པོ་རྣམས་ཀྱང་དེ་དང་འདྲ་བར་གང་ཟག་གི་རྟེན་ནམ་ལྷན་ཅིག་འབྱུང་བ་དག་ཡིན་པར་འགྱུར་བས༌[^3349]གཞན་ཉིད་དུ་གསལ་བར་དམ་འཆའ་བ་ཡིན་ནོ། །

[Block 4737]
དེ་མེད་ན་གང་ཟག་མེད་པར་ཡང་འགྱུར་ཏེ། བུད་ཤིང་མེད་ན་མེ་མེད་པ་བཞིན་ནོ། །

[Block 4738]
གང་ཡང་བུད་ཤིང་ལས་མེ་གཞན་ཡིན་ན་ནི༌[^3350]བུད་ཤིང་དྲོ་བ་ཉིད་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་སྨྲས་པ་དེ་དྲོ་བ་ཞེས་བྱ་བ་འདི་ཅི། རེ་ཞིག་གལ་ཏེ་དྲོ་བ་ཉིད་ཡིན་ནོ་ཞེ་ན་ནི་བུད་ཤིང༌[^3351]དྲོ་བ་ཉིད༌[^3352]མ་ཡིན་པ་ཁོ་ནར་འགྱུར་ཏེ། འབྱུང་བ་གཞན་གྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4739]
འོན་ཏེ་དྲོ་བ་ཉིད་དང་ལྡན་པ་ཡིན་ནོ་ཞེ་ན་ནི་དྲོ་བ་ཉིད་ཀྱི་རང་བཞིན་གྱི་མེ་ལས་གཞན་པ་དེ་ཡང་དྲོ་བ་ཡིན་པར་འགྲུབ་སྟེ། དྲོ་བ་ཉིད་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4740]
དེ་ལྟ་བས་ན་དོན་ཐ་དད་པ་ཉིད་ཡིན་ན་ཉེས་པ་མེད་དོ། །

[Block 4741]
འོན་ཏེ་ཤིང་ལ་སོགས་པ་འབར་བ་དེ་དག༌[^3353]ཐམས་ཅད་བུད་ཤིང་ཡང་ཡིན་ལ༌[^3354]མེ་ཡང་ཡིན་པར་འདོད་ན་ནི་དེས་ན་རྒྱུར་བྱས་པའི་དོན་ཡང་བརྗོད་པར་བྱའོ། །

[Block 4742]
ཕུང་པོ་རྣམས་ཁོ་ན་ཡང་གང་ཟག་ཡིན་པས་གཞན་པ་མ་ཡིན་པ༌[^3355]ཉིད་མི་ལྡོག་པར༌[^3356]འགྱུར་རོ། །

[Block 4743]
དེ་ལྟ་བས་ན་ཇི་ལྟར་བུད་ཤིང་རྒྱུར་བྱས་ནས་མེ་འདོགས་པ་དེ་ལྟར་ཕུང་པོ་རྣམས་རྒྱུར་བྱས་ནས་གང་ཟག་འདོགས་སོ་ཞེས་བྱ་བ་འདི་མི་འགྲུབ་བོ། །

[Block 4744]
གལ་ཏེ་ཡང་འདི་ཕུང་པོ་རྣམས་ལས་གཞན་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་ན། ཤེས༌[^3357]བྱ༌[^3358]ནི་རྣམ་པ་ལྔ་སྟེ། འདས་པ་དང་། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བ་དང་། འདུས་མ་བྱས་དང་། བརྗོད་པར་བྱ་བ་མ་ཡིན་པའོ་ཞེས་བརྗོད་པར་མི་བྱ་བར་འགྱུར་ཏེ། དེ་ནི་འདས་པ་ལ་སོགས་པ་ལས་ལྔ་པ་ཡང་མ་ཡིན་ལ་ལྔ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པར་བརྗོད་པར་བྱའོ། །

[Block 4745]
གང་གི་ཚེ་གང་ཟག་འདོགས་པ་ན་ཅི་རེ་ཞིག་ཕུང་པོ་རྣམས་དམིགས་ནས་འདོགས་སམ། འོན་ཏེ་གང་ཟག་དམིགས་ནས་འདོགས། རེ་ཞིག་གལ་ཏེ་ཕུང་པོ་རྣམས་ན་ནི་དེ་དག་ཁོ་ན་ལ་གང་ཟག་འདོགས་པར་འགྱུར་ཏེ། གང་ཟག་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 4746]
འོན་ཏེ་གང་ཟག་ན་ནི་འདི་ཇི་ལྟར་ན་ཕུང་པོ་རྣམས་རྒྱུར་བྱས་ནས་འདོགས་པ་ཡིན་ཏེ། གང་ཟག་ཁོ་ན་དེའི་རྒྱུ་ཡིན་པར་འགྱུར༌[^3359]རོ། །

[Block 4747]
འོན་ཏེ་ཕུང་པོ་རྣམས་ཡོད་ན་གང་ཟག་དམིགས་ཏེ། དེའི་ཕྱིར་ཕུང་པོ་རྣམས་རྒྱུར་བྱས་ནས་འདི་འདོགས་སོ་ཞེས་བྱ་བར་འདོད་དོ་ཞེ་ན་ནི། དེ་ལྟ་ན་གཟུགས་ཀྱང་དམིགས་པ༌[^3360]དང་ཡིད་ལ་བྱེད་པ་དང་སྣང་བ་རྣམས་ཡོད་ན་དམིགས་པས་དེ་དག་རྒྱུར་བྱས་ནས་བཏགས་པ་ཡིན་པར་བརྗོད་པར་བྱའོ། །

[Block 4748 [HEADING]]
#### གང་ཟག་རྣམ་པར་ཤེས་པ་གང་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ། ^6-2-4-0

[Block 4749]
རེ་ཞིག་འདི་ཡང་བརྗོད་པར་བྱ་སྟེ། རྣམ་པར་ཤེས་པ་དྲུག་རྣམས་ལས་གང་ཟག་རྣམ་པར་ཤེས་པ་གང་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན། དྲུག་ཅར་གྱིས་ཀྱང་ཤེས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱའོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། གལ་ཏེ་མིག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བའི་གཟུགས་རྣམས་ལ་བརྟེན་ནས། གང་ཟག་དམིགས་པར་བྱེད་ན་ནི་གང་ཟག་མིག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་ལ། གཟུགས་རྣམས་ཞེས་ཀྱང་བརྗོད་པར༌[^3361]མི་བྱ། གཟུགས་རྣམས་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱའོ། །

[Block 4750]
དེ་བཞིན་དུ་ཡིད་ཀྱིས་རྣམ་པར་ཤེས་པར་བྱ་བའི་ཆོས་རྣམས་ཀྱི་བར་ལ་བརྟེན་ནས། གང་ཟག་དམིགས་པར་བྱེད་ན་ནི། གང་ཟག་ཡིད་ཀྱིས༌[^3362]རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་ལ། ཆོས་རྣམས་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ་ལ། [^3363]ཆོས་རྣམས་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱའོ། །

[Block 4751]
དེ་ལྟ་ན་ནི་འོ་ན་འོ་མ་ལ་སོགས་པ་དང་འདྲ་བར་འགྱུར་ཏེ། གལ་ཏེ་མིག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བའི་གཟུགས་རྣམས་ལ་བརྟེན་ནས་འོ་མ་འམ། ཆུ་དམིགས་པར་བྱེད་ན་ནི་འོ་མ་འམ་ཆུ་མིག་གི༌[^3364]རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་ལ་གཟུགས་རྣམས་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ། གཟུགས་རྣམས་མ་ཡིན་ནོ༌[^3365]ཞེས་ཀྱང་བརྗོད་པར་མི་བྱའོ། །

[Block 4752]
དེ་བཞིན་དུ་གལ་ཏེ་སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱིས༌[^3366]རྣམ་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་པར་བརྗོད་པར་བྱ་ལ། རེག་བྱ་རྣམས་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ། རེག་བྱ་རྣམས་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ་སྟེ། འོ་མ་དང་ཆུ་གཉིས་བཞི་ཉིད་དུ་ཐལ་བར་འགྱུར་དུ་འོང་བས་སོ། །

[Block 4753]
དེའི་ཕྱིར་ཇི་ལྟར་གཟུགས་ལ་སོགས་པའི་སྤྱི་ཁོ་ན་ལ། འོ་མ་འམ། ཆུ་ཞེས་འདོགས་པ་དེ་བཞིན་དུ་ཕུང་པོ་རྣམས་ལ་གང་ཟག་འདོགས་སོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 4754]
གང་ཡང་མིག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བའི༌[^3367]གཟུགས་རྣམས་ལ་བརྟེན་ནས་གང་ཟག་དམིགས་པར་བྱེད་ཅེས་སྨྲས་པའི་ཚིག་དེའི་དོན་ཅི་ཞིག་ཡིན། ཅི་རེ་ཞིག་གཟུགས་རྣམས་གང་ཟག་དམིགས་པའི་རྒྱུ་ཞིག་ཡིན་ནམ། འོན་ཏེ་གཟུགས་རྣམས་དམིགས་ན་གང་ཟག་དམིགས་སོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4755]
གལ་ཏེ་གཟུགས་རྣམས་གང་ཟག་དམིགས་པའི་རྒྱུ་ཡིན་ལ་དེ་ཡང་དེ་དག་ལས་གཞན་དུ་བརྗོད་པར་མི་བྱའོ་ཞེ་ན་ནི། དེ་ལྟ་ན་ནི་འོ་ན་གཟུགས་ཀྱང་སྣང་བ་དང་མིག་དང་ཡིད་ལ་བྱེད་པ་དག་ལས་གཞན་དུ་བརྗོད་པར་མི་བྱ་སྟེ། དེ་དག་ནི་དེ་དམིགས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4756]
འོན་ཏེ་གཟུགས་རྣམས་དམིགས་ན་གང་ཟག་དམིགས་སོ་ཞེ་ན་ནི་ཅི་དམིགས་པ་དེ་ཁོ་ནས་དམིགས་སམ། འོན་ཏེ་གཞན་གྱིས་གལ་ཏེ་དེ་ཁོ་ནས་སོ་ཞེ་ན་ནི་གང་ཟག་གཟུགས་ལས་རང་བཞིན་ཐ་མི་དད་པའམ་གཟུགས་ཁོ་ན་ལ་དེ་འདོགས་པར་འགྱུར་ན། འདི་ནི་གཟུགས་སོ། །

[Block 4757]
འདི་ནི་གང་ཟག་གོ་ཞེས་བྱ་བ་འདི་ཡང་ཇི་ལྟར་ཡོངས་སུ་གཅོད། འོན་ཏེ་དེ་ལྟར་ཡོངས་སུ་མི་གཅོད་ན་ནི་གཟུགས་ཀྱང་ཡོད་དོ། །

[Block 4758]
གང་ཟག་ཀྱང་ཡོད་དོ་ཞེས་བྱ་བ་འདི་ཡང་ཇི་ལྟར་དམ་འཆའ་སྟེ། དམིགས་པའི་དབང་གིས་དེ་ཡོད་པར་དམ་འཆའ་བར་ཟད་དོ། །

[Block 4759]
དེ་བཞིན་དུ་ཆོས་ཀྱི་བར་དག་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 4760]
འོན་ཏེ་གཞན་གྱིས་སོ་ཞེ་ན་ནི། དུས་ཐ་དད༌[^3368]དམིགས་པའི་ཕྱིར་གཟུགས་ལས་གཞན་ཡིན་པར་འགྱུར་ཏེ། སྔོན་པོ་ལས་སེར་པོ་ལྟ་བུ་དང་། སྐད་ཅིག་མ་ལས་སྐད་ཅིག་མ་གཞན་བཞིན་ནོ། །

[Block 4761]
དེ་བཞིན་དུ་ཆོས་ཀྱི་བར་དག་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 4762]
འོན་ཏེ་གཟུགས་དང་གང་ཟག་བཞིན་དུ་དེ་དག་དམིགས་པ་དག་ཀྱང་གཞན་དང་གཞན་མ་ཡིན་པ་ཉིད་དུ་བརྗོད་པར་མི་བྱའོ་ཞེ་ན། འོ་ན་ནི་དེས་ན་འདུས་མ༌[^3369]བྱས་ཀྱང་བརྗོད་པར་བྱ་བ་མ་ཡིན་པར་གྱུར་པས།[^3370] གྲུབ་པའི་མཐའ་ཉམས་པ་ཡིན་ནོ། །

[Block 4763]
གལ་ཏེ་ཡང་འདི་ཡོད་ལ་གཟུགས་རྣམས་ཞེས་ཀྱང༌[^3371]བརྗོད་པར་མི་བྱ། [^3372]གཟུགས་རྣམས་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ་ན། འོ་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་གཟུགས་བདག་མ་ཡིན་པ་ནས།

[Block 4764]
རྣམ་པར་ཤེས་པ་བདག་མ་ཡིན་ཞེས་བྱ་བའི་བར་གསུངས།

[Block 4765]
མིག་གི་རྣམ་པར་ཤེས་པ་གང་གིས་གང་ཟག་འདི་དམིགས་པ་དེ་ཅི་གཟུགས་ལ་བརྟེན་ནས་སྐྱེ་འམ། འོན་ཏེ་གང་ཟག་གམ། གཉི་ག་ལ་བརྟེན་ནས་སྐྱེ། གལ་ཏེ་གཟུགས་རྣམས་ལ་བརྟེན་ནས་སྐྱེ་ན་ནི་སྒྲ་ལ་སོགས་པ་བཞིན་དུ་གང་ཟག་དམ༌[^3373]པར་ཤེས་པར་མི་ནུས་ཏེ། ཡུལ་གང་ཁོ་ན༌[^3374]ལ་བརྟེན་ནས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་དེ་ཉིད་དེའི་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །
--- END BLOCKS ---
