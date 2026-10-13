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
[Block 4656]
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟེ་ཞེས་པ་ནི་དྲུག་པའོ། །

[Block 4657]
དེ་དང་ལྷན་ཅིག་ཏུ་སྦྱོར་བ་ཞེས་པ་ནི་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་གཅིག་ནི་ཏིང་ངེ་འཛིན་གྱིས་རྫོགས་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་བསྒོམས་པའི་འོག་ཏུ་རང་གི་ཐུགས་ཀ་ནས་མི་བསྐྱོད་པ་སྤྲོས་ཏེ། །དེས་འགྲོ་བའི་དོན་བྱས་ལ་དེ་དང་ལྷན་ཅིག་དུས་གཅིག་ཏུ་གྱུར་ནས་མི་བསྐྱོད་རྡོ་རྗེར་བདག་ཉིད་བསྒོམ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4658]
དེ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས་རིན་ཆེན་འབྱུང་ལྡན་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 4659]
སྐུ་མདོག་ཅེས་བྱ་བ་ལ་སོགས་པས་ཞེ་སྡང་རྡོ་རྗེ་ལ་སོགས་པའི་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་ཉམས་དང་རྣམ་པར་དག་པ་བསྟན་ཏེ། ཁྲོ་བ༌[^2798]དང་འདོད་ཆགས་ཆེན་པོ་འདྲེས་པར་གྱུར་པས་ཞེས་པ་ནི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ནི་འདོད་ཆགས་དང་། ཞེ་སྡང་རྣམ་པར་དག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4660]
དེ་ལ་མཆེ་བ་ཅུང་ཟད་གཙིགས་པའོ་ཞེས་པ་ནི་ཁྲོ་བོའི་ཉམས་དང་ལྡན་པ་དང་རེག་བྱ་རྡོ་རྗེ་མས་འཁྱུད་པ་ཆགས་པའི་རོ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 4661]
ཤེལ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྣམ་པར་སྣང་མཛད་ཀྱི་དབྱིབས་དང་སྐུ་མདོག་དང་ཕྱག་མཚན་རྣམས་བསྟན་ཏོ། །

[Block 4662]
གསེར་གྱི་མདོག་ཅན་ལ་ཞེས་པ་ནི་རྒྱས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4663]
དེ་བཞིན་གཤེགས་པའི་སྤྲིན་གྱིས་ཀུན་དུ་འཁྲིགས་པར་བསྒོམ་པའོ་ཞེས་པ་ནི་དབུས་ཀྱི་གཙོ་བོ་ཉིད་དུ་བཞུགས་ནས་འགྲོ་བ་དབུལ་བའི་སྡུག་བསྔལ་བཅོམ་པའི་ཕྱིར་རང་དང་རྗེས་སུ་མཐུན་པ༌[^2799]ཛམྦྷ་ལ་ལ་སོགས་པ་སྤྲོ་བར་མཛད་པའོ། །

[Block 4664]
རྡོ་རྗེ་རྩེ་དགུ་པ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔ་དང་ལྷ་མོ་བཞིའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4665]
བཤད་པའི་རྒྱུད་ལས་ཀྱང་།

[Block 4666 [VERSE]]
དབུས་རྩེ་རྣམ་པར་སྣང་མཛད་དང་། །
ཤར་ལ་མི་བསྐྱོད་རིན་ཆེན་ལྷོར། །
ནུབ་དང་བྱང་གི་རྩེ་དག་ལ། །
འོད་དཔག་མེད་དང་དོན་ཡོད་གྲུབ། །

[Block 4667 [VERSE]]
པདྨ་འདབ་མ་བརྒྱད་པ་ནི། །
དེ་ཡི༌[^2800]འདབ་མ་རེ་རེ་ལ། །
ཤིན་དུ་གསལ་བའི་ཕྱག་མཚན་ཅན། །
བྱང་ཆུབ་སེམས་དཔའ་བརྒྱད་ཡིན་ཏེ། །

[Block 4668 [VERSE]]
ལག་ན་པདྨ་བྱམས་པ་དང་། །
ནམ་མཁའི་སྙིང་པོ་ཀུན་དུ་བཟང་། །
གནོད་སྦྱིན་བདག་པོ་འཇམ་དཔལ་དང་། །
རྣམ་པར་སེལ་དང་ས་སྙིང་པོ། །

[Block 4669 [VERSE]]
འོག་ཏུ༌[^2801]ཤར་རྩེར་རྡོར་མཁའ་འགྲོ། །
[^2802]ལྷོར་འཇིགས་མ་ཡི་མཁའ་འགྲོ་མ། །
ནུབ་ཏུ་གཏུམ་མོ་ཞེས་ནི་བྱ། །
རོ་ལངས་མ་ནི་བྱང་དུ་དགོད།[^2803] །

[Block 4670 [VERSE]]
དབུས་སུ་ཡེ་ཤེས་མཁའ་འགྲོ་མ། །
འོག་རྩེ་རྣམ་པར་དག་པ་ཡིན། །
སྤྱན་མ་དང་ནི་མཱ་མ་ཀཱི། །
གོས་དཀར་མོ་དང་སྒྲོལ་མ་དང་། །

[Block 4671 [VERSE]]
སྐུལ་བྱེད་མ་དང་རིན་ཆེན་སྒྲོན། །
སྐེ་རགས༌[^2804]གཞན་གྱིས༌[^2805]མི་ཐུབ་མ། །
པདྨ་ལ་གནས་མཁའ་འགྲོ་མ། །
རྡོ་རྗེ་དེ་ཉིད་འདི་ཡིན་ནོ། །

[Block 4672 [VERSE]]
དབུས་ཀྱི་ཆང་ཟུང༌[^2806]ཡེ་ཤེས་དབྱིག །
སྤྲོ་དང་བསྡུ་བ་མཛད་པའོ། །

[Block 4673]
ཞེས་འབྱུང་ངོ་། །

[Block 4674]
དེ་ལྟར་ལྷ་ཉི་ཤུ་རྩ་བརྒྱད་ཀྱི་རང་བཞིན་ནི་རྡོ་རྗེ་ཡིན་ནོ། །

[Block 4675]
མར་ག་ཏ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་ལྟར་སྔོ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4676]
རིན་ཆེན་འབྱུང་ལྡན་གྱི་ཕྱག་མཚན་གསུངས་པའོ་ཞེས་པ་ནི་ཟུར་དྲུག་པའི་རིན་པོ་ཆེ་སྟེ་འགྲོ་བ་རིགས་དྲུག་པའི་སེམས་ཅན་གྱི་ཁམས་ཀྱི་ཟུར་རེ་རེས་བསམ་པ་ཐམས་ཅད་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4677]
འོད་དཔག་ཏུ་མེད་པའི་ཕྱག་མཚན་གསུངས་པའོ་ཞེས་པ་ནི་ཁ་ཕྱེད་པའི་ཕྱག་རྒྱ་དང་ལྡན་པའི་པདྨ་རཱ་གའི་ཁ་དོག་དང་འདྲ་བའི་པདྨ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4678 [VERSE]]
ཇི་ལྟར་པདྨ་དམར་པོ་འདི། །
འདམ་གྱི་སྐྱོན་གྱིས་མ་གོས་པ། །
དངོས་པོའི་སྐྱོན་ནི་སྣ་ཚོགས་པས། །
དེ་བཞིན་ཁམས་གསུམ་པ་ནི་དག །

[Block 4679]
ཅེས་འབྱུང་ངོ་། །སྣ་ཚོགས་པའི་འགྲོ་བ་མ་ལུས་པའི་དོན་སྒྲུབ་པར་མཛད་པའི་ངོ་བོ་ཉིད་ཡིན་པས་ཞེས་པ་ལ། དོན་ཡོད་པ་ནི་བྱ་བ་ནན་ཏན་གྲུབ་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4680]
འོད་ཟེར་དཀར་པོ་ལ་སོགས་པ༌[^2807]དང་ལྡན་པའི་ཕྱིར་རོ་ཞེས་པ་དེ༌[^2808]ནི་དོན་ཡོད་གྲུབ་པ་ལས་ཐམས་ཅད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4681]
རལ་གྲི་བསྣམས་པ་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་གཅོད་པར་བྱེད་པའི་ཤེས་རབ་ཀྱི་ངོ་བོ་འཆང་བས་སོ། །

[Block 4682]
དེས་ནི་སེམས་ཅན་རྣམས༌[^2809]གདུལ་བར་བྱ་བའི་ཕྱིར་ཡེ་ཤེས་ཉིད་སྔོན་པོ་ལ་སོགས་པའི་ཁ་དོག་གི་ཁྱད་པར་གྱི་རྣམ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4683 [VERSE]]
ཨིནྡྲ་བྷཱུ་ཏིའི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་། །
ཤིན་ཏུ་རྣམ་དག་ངོ་བོའི་ཕྱིར། །
ཁ་དོག་དཀར་པོས་རབ་ཏུ་བསྟན། །
ཀུན་ལ་གཏོང་བས་སེར་པོ་ཉིད། །

[Block 4684 [VERSE]]
རྟག་ཏུ་བརྩེ་བས་དམར་པོ་ཡིན། །
དཀོན་མཆོག་གསུམ་ལ་གནོད་བྱེད་སོགས། །
འདུལ་བར་བྱེད་པ་ལ་བརྩོན་པ། །
འགྲོ་བའི་དོན་ལ་མཛད་པའི་མཆོག །

[Block 4685 [VERSE]]
ཡེ་ཤེས་དེ་ནི་ནག་པོར་བཤད། །
སྣ་ཚོགས་ཐབས་ཀྱིས་གདུལ་བའི་ཕྱིར། །
ཁ་དོག་ལྗང་གུ་རབ་བསྟན་པའོ། །

[Block 4686]
ཞེས་གསུངས་སོ། །

[Block 4687]
དེ་བཞིན་དུ་ཐུགས་རྡོ་རྗེ་འཆང་བ་ལ་སོགས་པའི་རྡོ་རྗེ་ལ་སོགས་པ་ཕྱག་མཚན༌[^2810]གང་ཡིན་པ་དེ་རྣམས་ཡེ་ཤེས་ཀྱི་ཁྱད་པར་ཉིད་ཡིན་ནོ། །

[Block 4688]
ཇི་སྐད་དུ།

[Block 4689 [VERSE]]
གཟུགས་ལ་སོགས་པ་སྐྱེ་མཆེད་རྣམས། །
གང་ཕྱིར་རང་ཉིད་ཀྱིས་བརྗོད་པ། །
དེས་ན་སངས་རྒྱས་ཡེ་ཤེས་ནི། །
དེ་བཞིན་གཤེགས་པས་ཕྱག་དྲུག་གསུངས། །

[Block 4690 [VERSE]]
བྱང་ཆུབ་སེམས་ནི་རྡོ་རྗེ་སྟེ། །
ཤེས་རབ་དྲིལ་བུ་མངོན་པར་བརྗོད། །
མ་རིག་གཅོད་བྱེད་འཁོར་ལོ་སྟེ། །
རིན་ཆེན་རིན་ཐང་མེད་པའི་ཕྱིར། །

[Block 4691 [VERSE]]
སྲིད་པའི་སྐྱོན་གྱིས་མ་གོས་པས། །
ཡེ་ཤེས་དེ༌[^2811]ནི་པདྨར་བཤད། །
རལ་གྲི་ཉོན་མོངས་དགྲ་གཅོད་པ། །
ཨུཏྤལ་དེ་ལས་སྐྱོབ་པའི་ཕྱིར། །

[Block 4692 [VERSE]]
འཁོར་བའི༌[^2812]དྲ་བ་ངེས་ཚིག་པའི། །
གང་ཕྱིར་ཡེ་ཤེས་ཉིད་སྐྱེས་པ། །
སངས་རྒྱས་རྗེས་གནང༌[^2813]སེམས་ཅན་གྱིས། །
རྡེག་པར་བྱེད་པ་ཐོབ་པར་བཤད། །

[Block 4693 [VERSE]]
ཆད་པས་གདུལ་ཕྱིར་དབྱུག་པ་སྟེ། །
སེམས་ཅན་འདུལ་བྱེད་དེ་ཤེས་ཡིན། །
ཕན་ཚུན་ཁྱབ་པ་མི་བྱེད་ཕྱིར། །
སྣ་ཚོགས་རྡོ་རྗེ་ཡིན་པར་བཤད། །

[Block 4694]
སྐུ་མདོག་དང་ཕྱག་མཚན་དང་ཡེ་ཤེས་ཀྱི་རང་བཞིན་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། །འོན་ཀྱང་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ཡང་དེའི་ངོ་བོ་ཉིད་དོ། །

[Block 4695 [VERSE]]
སེམས་ཅན་ཀུན་ལ་སྣང་བྱེད་ཕྱིར། །
རང་གི་རང་བཞིན་སྣང་བྱེད་པས། །
དེ་བཞིན་གཤེགས་ཞེས་དག་པ་ནི། །
དེ་ནི་རྣམ་པར་སྣང་མཛད་བཤད། །
--- END BLOCKS ---
