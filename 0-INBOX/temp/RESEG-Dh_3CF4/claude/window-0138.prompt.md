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
ཞེས་བྱ་བ་དེ་ལ། དེ་མི་འདོད་པ་ནི་ཅི། ཇི་ལྟར༌[^3130]བསྒྲུབ་པར་བྱ་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། གང་ལ་བརྟེན་ནས་དཔལ་གྱི་གནས་གྱུར་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དཔལ་གྱི་གནས་སུ་གྱུར་ཅེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་འབྲས་བུ་བསྟན་ཏེ། གང་གི་ཕྱིར་སྦྱིན་པས་ནི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་འཐོབ་པར་འགྱུར་ཏེ། གཞན་དག་གི་དབུལ་བ་བསལ་བས་བདག་ལ་ཡང་དབུལ་བའི་གཉེན་པོ་ལོངས་སྤྱོད་འབྱུང་བ་ཡིན་ཏེ། དེ་བས་ན་བདག་ཉིད་འདོད་པ་གཞན་ལ་སྤྱད་པ་ཡིན་ནོ། །

[Block 4832]
གང་ལ་བརྟེན་ནས༌[^3131]ཞེས་བྱ་བ་ནི་སྦྱིན་པ་གང་ལ་བརྟེན་ནས་སོ། །

[Block 4833]
འཇིག་རྟེན་བསྔགས་པ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་འཇིག་རྟེན་པ་རྣམས་ལ་བཟོད་པ་བྱས་ནས་ནི་སྐྱེ་བོ་མང་པོ་དག་དགའ་བར་འགྱུར་ཏེ། གཡོག་འཁོར་མང་བར་ཡང་འགྱུར་རོ། །

[Block 4834]
གང་ལ་བརྟེན་ནས་ཞེས་བྱ་བ་ནི་བཟོད་པ་གང་ལ་བརྟེན་ནས་སོ། །

[Block 4835]
རྒྱལ་སྲིད་འཐོབ་འགྱུར་ཞེས་བྱ་བས་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་བསྟན་ཏེ། གང་གི་ཕྱིར་རིགས་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པ༌[^3132]ཁྱད་པར་དུ་གྱུར་བ་ལ་ནི་རྒྱལ༌[^3133]སྲིད་ཅེས་བརྗོད་དེ། རྒྱལ་སྲིད་ཐོབ་པ་དེ་ཡང་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུའོ། །

[Block 4836]
གང་ལ་བརྟེན༌[^3134]ནས་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་གང་ལ་བརྟེན་ནས་སོ། །

[Block 4837]
བསོད་ནམས་ཉིད་ཅེས་བྱ་བ་ནི་སྦྱིན་པ་དང་། བཟོད་པ་དང་། ཚུལ་ཁྲིམས་རྣམས་ནི་བསོད་ནམས་ཏེ། བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་བཟུང་བའི་ཕྱིར། གསུམ་པོ་འདི་ཐོབ་པ་ཡིན་ནོ། །

[Block 4838]
དེ་བས་ན་མང་པོའི་ཚིག་ཏུ་བསྟན་ཏེ། རྒྱལ་སྲིད་ཐོབ་པར༌[^3135]འགྱུར་བའི་བསོད་ནམས་ཀྱི་ཚོགས༌[^3136]དེ་འཕེལ་བར་མཛོད་ཅིག་པའོ། །

[Block 4839]
གྲོགས་པོ་རབ་ལ་གང་བྱས་པ་ནི། དེས་སྦྱར་བ་ཡིན་ཏེ། སྤང་བའི་ཡང་མི་རིགས་པའོ། །

[Block 4840]
གནོད་པ་ཆུང་ངུ་བྱེད་པ་ཡིན་ན་ཡང་གྲོགས་པོ་ལ་ཇི་ལྟར་བྱ་བ་དེ་ལྟར་ནི་བསྒྲུབ་པར་བྱའི་གཞོམ་པར་ནི་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4841]
འདིར་ཡང་ཕན་འདོགས་ཕྱོགས་ནི་ཞེས་བྱ་བ་ལ། ཕན་འདོགས་པའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་ཕན་འདོགས་ཕྱོགས་སོ། །

[Block 4842]
གྲོགས་པོའི་ཕྱོགས་ནི་ཕན་འདོགས་པའི་ཕྱོགས་ཏེ། གྲོགས་པོའི་དོན་ཉིད་དུ་བསྟན་པར་འགྱུར་རོ། །

[Block 4843]
དོན་མ་ནུས་ཀྱང་གཞག་པར་བྱ་བ་ནི་ཡིན་ཏེ། ཇི་ལྟར་གྲོགས་པོ་དམན་པ་ལ་བསྒྲུབ་པར་བྱ་བ་དེ་ལྟར་རོ། །

[Block 4844]
བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པ་གསུམ་བྱ་བ་དེའི་དབང་དུ་བྱས་ནས། དུས་སུ་རིམ་གྲོ་བྱས་པའི་སྦྱིན་པ་རྒྱ་ཆེན་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4845]
དུས་སུ་རིམ་གྲོ་བྱས་པའི་སྦྱིན་པ་རྒྱ་ཆེན་དང་། །ཞེས་བྱ་བ་ལ་གང་རབ་ཏུ་སྦྱིན་པ་དེ་ནི་སྦྱིན་པའོ། །

[Block 4846]
རྒྱུ་འདི་གསུམ་གྱིས་ཏེ། དུས་སུ་སྦྱིན་པ་དང་། རིམ་གྲོ་བྱས་ཏེ། སྦྱིན་པ་དང་། རྒྱ་ཆེན་པོའི་སྦྱིན་པ་བསྟན་ཏོ། །

[Block 4847]
དུས་སུ་སྦྱིན་པས་ནི་ལོངས་སྤྱོད་དུས་སུ་འཐོབ་པར་འགྱུར་རོ། །

[Block 4848]
རིམ་གྲོ་བྱས་བ༌[^3137]སྦྱིན་པས་ནི་གུས་བའི་སྦྱིན་པ་འཐོབ་བོ། །

[Block 4849]
རྒྱ་ཆེན་པོ་བྱིན་པས་ནི་ལོངས་སྤྱོད་རྒྱ་ཆེན་པོ་འཐོབ་པ་ཡིན་ནོ། །

[Block 4850]
སྐྱེ་བོ་དམ་པ་དང་འབྲེལ་བ་ནི་སྐྱེ་བོ་དགེ་བ་དང་མཐུན༌[^3138]པའོ། །

[Block 4851]
སྐྱེ་བོ་དགེ་བ་དང་མཐུན་པའི་བརྟན་པ་ནི་དུས་རྟག་ཏུ་ཉམས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏེ། [^3139]སྐྱོན་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4852]
བདག་དང་འདྲ་བར་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི༌[^3140]བློས། །ཞེས་བྱ་བ་ལ་ཕན་པའི་བློ་ནི་ཕན་པ་བསྒྲུབ་པ་དེས་སོ། །

[Block 4853]
འདིས་ནི་བསམ་པ་དང་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བློ་ཞེས་སྨོས་པས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4854]
སྒྲུབ་པ་སྨོས་བས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4855]
སྩོགས་ཞེས་སྨོས་པས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་འདི་གསུམ་གཟུང་བར༌[^3141]བྱའོ་ཞེས་བྱ༌[^3142]བའི་དོན་ཏོ། །

[Block 4856]
གྲོགས༌[^3143]དང་བདེ་བ་བསྒྲུབ་པ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་དང་། འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་བསྟན་ཏེ། མཐོང་བའི་ཆོས་དང་འཇིག་རྟེན་ཕ་རོལ་ལ་ཇི་ལྟར་སྔར་བཤད་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 4857]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་རི་དགས་ཤ་ར་བྷའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 4858 [HEADING]]
## རི་དགས་རུ་རུའི་སྐྱེས་པའི་རབས། ^28-0

[Block 4859]
དེ་མི་བཟོད་ཀྱི་ཞེས་བྱ་བ་ནི་གཞན་གྱི་སྡུག་བསྔལ་ཡིན་གྱི། བདག་གི་སྡུག་བསྔལ་མི་བཟོད་པ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་མི་བཟོད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4860]
གང་ན་ཤིང་སཱ་ལ་ལ༌[^3144]སོགས་པ་མང་པོ་ཡོད་པའི་དགོན་པའི་ཕྱོགས་དེ་ནི་ཤིང་སཱ་ལ་ལ་སོགས་པ་ཡོད་པའི་དགོན་པའི་ཕྱོགས་ཏེ་དེ༌[^3145]ནའོ། །

[Block 4861]
རྣམ་པ་སྣ་ཚོགས་པའི་ཤིང་ལྗོན་པའི་ལྡུམ་བུའི་འཁྲི་ཤིང༌[^3146]གིས་དཀྲིས་པ་གང་ན་ཡོད་པ་དེ་ནི་ཤིང་ལྗོན་པའི་ལྡུམ་བུ་མང་པོའི་འཁྲི་ཤིང༌[^3147]སྣ་ཚོགས་ཀྱིས་དཀྲིས་པའོ། །

[Block 4862]
གསེར་བཙོ་མའི་ཁ་དོག་གསལ་བ་འདྲ་བའི་སྤུ་རབ་ཏུ་འཇམ་པ་གང་ཡིན་པ་ནི། གསེར་བཙོ་མའི་ཁ་དོག་གསལ་བ་འདྲ་བ་སྤུ་རབ་ཏུ་འཇམ་པའོ། །

[Block 4863]
ལུས་ཀྱི་མདོག་རིན་པོ་ཆེ་ཨནྡ་རྙིལ་དང་། མརྒད་དང་། བཻ་ཌཱུརྱའི་ཁ་དོག་འདྲ་བའི་ཚོན་སྣ་ཚོགས་ཀྱི་ཐིག་ལེས་བརྒྱན་པ་གང་ཡིན་པ་དེ་ནི་ལུས་ཀྱི་མདོག་རིན་པོ་ཆེ་ཨནྡ་རྙིལ་དང་། མརྒད་དང་། བཻ་ཌཱུརྱའི་ཁ་དོག་འདྲ་བའི་ཚོན་སྣ་ཚོགས་ཀྱི་ཐིག་ལེས་བརྒྱན་པའོ། །

[Block 4864]
སློབ་པ་ཞེས་བྱ་བ་ནི་འཁྲུལ་འཁོར་ལ་སོགས་པའོ། །

[Block 4865]
རི་དགས་རྣམས་ཀྱི་བདག་པོ་བྱེད་ཅིང་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་བདག་པོ་བྱེད་ཅེ་ན། སྔར་བསྟན་པའི་དོན་མདོར་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། གཟུགས་དང་ཤེས་པ་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་བདག་ཉིད་ཕུན་སུམ་ཚོགས་པ་དང་། གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཚིགས་བཅད་དང་པོ་ཕྱེད་ཀྱིས་ནི༌[^3148]བདག་ཉིད༌[^3149]ཕན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4866]
བདག་ལ་ཕན་འདོགས་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་པ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4867]
བདག་གི་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། གཟུགས་ཀྱི་ལུས་ཕུན་སུམ་ཚོགས་པ་དང་། མིང་གི་ལུས༌[^3150]ཕུན་སུམ་ཚོགས་པ་དང་། བྱ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4868]
གསེར་བཙོ་མའི་ཁ་དོག་གསལ་བ་འདྲ་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གཟུགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4869]
དེ་སེམས་རྣོ་བ་ཞེས་བྱ་བས༌[^3151]ནི་ཤེས་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4870]
འཁྲུལ་འཁོར་དང་གཏོར་ཞེས་བྱ་བ་དག་གིས་ནི་བྱ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
