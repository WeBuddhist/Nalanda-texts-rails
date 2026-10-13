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
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དེ་དག་ཀྱང་རིགས་གསུམ་ཡིན་ཏེ། །དེ་ལ། གཉིས་སློབ་རིགས་ལས་བཟློག་ནས་ནི། །སངས་རྒྱས་སུ་འགྱུར། དྲོ་བར་གྱུར་པ་དང་། རྩེ་མོ་སྐྱེས་པ་ཉན་ཐོས་ཀྱི་རིགས་ལས་བཟློག་ནས་ཡང་སངས་རྒྱས་སུ་འགྱུར་བ་ནི་སྲིད་དོ། །

[Block 3327]
གཞན་གསུམ་ཡང་། གསུམ་ཡང༌[^1314]ཉན་ཐོས་ཀྱི་རིགས་ལས་བཟློག་ནས་སངས་རྒྱས་ལས་གཞན་དུ་འགྱུར་རོ། །

[Block 3328]
རང་སངས་རྒྱས་ཀྱི་རིགས་རྣམས་ནི་བཟློག་པར་མི་ནུས་ཏེ། འདི་ལྟར།

[Block 3329 [VERSE]]
སྟོན་དང་བསེ་རུ་བྱང་ཆུབ་པར། །
བསམ་གཏན་མཐའ་རྟེན་གཅིག་ལ་ཀུན། །

[Block 3330]
སངས་རྒྱས་དང་། རང་སངས་རྒྱས་དག་ནི་བསམ་གཏན་བཞི་པ་ཁོ་ན་ལ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ལས༌[^1315]བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་བར་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 3331]
གཞན་དག་ན་རེ་མི་སྡུག་པ་ནས་བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་བར་དུའོ་ཞེའོ། །

[Block 3332]
ཅི་ཚེ་དང་པོ་ཁོ་ན་ལ་སྦྱོར་བ་བྱས་ཏེ། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་སྐྱེད་པར་བྱེད་དམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་ཀྱི་ངེས་པར། དེ་ཡི་སྔོན་དུ་ཐར་ཆ་མཐུན། །སྐྱེད་པར་བྱེད་དོ། །

[Block 3333]
ཐམས་ཅད་ལས་ཤིན་ཏུ། མྱུར་བར་སྲིད་པ་གསུམ་གྱི༌[^1316]མཐར། །ས་བོན་འདེབས་པ་དང་། འབྲུ་སྐྱེ་བ་དང་། འབྲས་བུ་ཆགས་པ་བཞིན་དུ་ཚེ་གཅིག་ལ་ནི་ཐར་པའི་ཆ་དང་མཐུན་པ་དང་།

[Block 3334]
གཉིས་པ་ལ་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དང་།

[Block 3335]
གསུམ་པ་ལ་ནི་འཕགས་པའི་ལམ་སྐྱེད་པར་བྱེད་དོ། །

[Block 3336 [HEADING]]
#### ཐར་པའི་ཆ་དང་མཐུན་པ། ^6-1-7-0

[Block 3337]
ཐར་པའི་ཆ་དང་མཐུན་པ་དེ་ཡང་། ཐོས་བསམས༌[^1317]ལས་བྱུང་། ཡིན་པར་བརྗོད་དེ། བསྒོམས་པ༌[^1318]ལས་བྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 3338]
ལས་གསུམ་མོ། །

[Block 3339]
གཙོ་བོར་ནི་ཡིད་ཀྱི་ལས་སོ། །

[Block 3340]
དེའི་སྨོན་ལམ་གྱིས་ཡོངས་སུ་བཟུང་བའི་ཕྱིར་ལུས་དང་ངག་གི་ལས་ཀྱང་ཐར་པའི་ཆ་དང་མཐུན་པ་ཡིན་ནོ། །

[Block 3341]
དེ་ཡང་འདི། མི་ཡི་ནང་ནས་འཕེན་པར་བྱེད། །མི་ཁོ་ནའི་ནང་དུ་སྟེ། གཞན་དུ་མ་ཡིན་ཏེ། ཅི་རིགས་པར་ཤེས་རབ་དང་སྐྱོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3342 [HEADING]]
#### བདེན་པ་མངོན་རྟོགས་སེམས་བཅུ་དྲུག། ^6-1-8-0

[Block 3343]
ཐར་པའི་ཆ་དང་མཐུན་པ་ཞར་ལས་འོངས་པ་བཤད་ནས། གནས་སྐབས་ཀྱི་འབད་པར་བྱ་སྟེ།

[Block 3344 [VERSE]]
འཇིག་རྟེན་པ་ཡི་ཆོས་མཆོག་ལས། །
ཆོས་ཀྱི་བཟོད་པ་ཟག་པ་མེད། །

[Block 3345]
འཇིག་རྟེན་པའི་ཆོས་མཆོག་གི་མཇུག་ཐོགས་སུ་ཆོས་ཤེས་པའི་བཟོད་པ་ཟག་པ་མེད་པ་སྐྱེའོ། །

[Block 3346]
དམིགས་པ་གང་ལ་ཞེ་ན། འདོད་སྡུག་བསྔལ་ལ། དེའི་དམིགས་པ་ནི་འདོད་པ་ན༌[^1319]སྤྱོད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 3347]
དེ་ནས་ནི། དེ་ཉིད་ལ་ཆོས་ཤེས། འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་དེ་ཁོ་ན་ལ་ཆོས༌[^1320]ཤེས་པ་སྐྱེའོ། །

[Block 3348]
དེ་བཞིན་སྡུག་བསྔལ་ལྷག་ལ་རྗེས་བཟོད་ཤེས། །གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་སྤྱི་ལ་དམིགས་པ་སྐྱེའོ། །

[Block 3349]
དེ་ནས་ནི་རྗེས་སུ་ཤེས་པའོ། །

[Block 3350]
ཇི་ལྟར་སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་བཟོད་པ་དང་ཤེས་པ་བཞི་པོ་དེ་དག་སྐྱེ་བ་ལྟར། བདེན་པ་གསུམ་ལའང་དེ་བཞིན་ནོ། །

[Block 3351]
ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་དག་ལ་འདོད་པའི་ཁམས་དང་གོང་མར་ཆོས་དང་ཆོས་སུ་ཤེས་པའི་བཟོད་པ་དང་ཤེས་པ་རྣམས་སོ། །

[Block 3352]
དེ་ལྟར་བདེན་པ་མངོན་རྟོགས་འདི། །སེམས་བཅུ་དྲུག་གོ། །

[Block 3353]
རིམ་པ་དེས་ན་བདེན་པ་མངོན་པར་རྟོགས་པ་འདི་ནི་སེམས་བཅུ་དྲུག་ཡིན་ནོ། །

[Block 3354]
དེ་ནི་རྣམ་གསུམ་སྟེ། མཐོང་དམིགས་བྱ་བ་ཞེས་བྱའོ། །

[Block 3355]
མཐོང་བའི་མངོན་པར་རྟོགས་པ་ནི་ཤེས་རབ་ཀྱིས༌[^1321]བདེན་པ་རྣམས་སོ། །

[Block 3356]
དམིགས་པའི་མངོན་པར་རྟོགས་པ་ནི་དེ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་ཀྱིས་ཀྱང་ངོ་། །བྱ་བའི་མངོན་པར་རྟོགས་པ་ནི་ལྡན་པ་མ་ཡིན་པའི་ཚུལ་ཁྲིམས་དང་སྐྱེ་བ་ལ་སོགས་པས་ཀྱང་ངོ་། །སྡུག་བསྔལ་མཐོང་ན་དེའི་མངོན་པར་རྟོགས་པ་ནི་གསུམ་མོ། །

[Block 3357]
ཀུན་འབྱུང་བ་ལ་སོགས་པའི་ནི་བྱ་བའི་མངོན་པར་རྟོགས་པ་ཡིན་ཏེ། སྤོང་བ་དང་། མངོན་སུམ་དུ་བྱེད་པ་དང་། བསྒོམ་པའི་ཕྱིར་རོ། །

[Block 3358]
མངོན་པར་རྟོགས་པ་སེམས་བཅུ་དྲུག་པར་བཤད་པ་གང་ཡིན་པ། དེ་ནི་ཆོས་མཆོག་དང་ས་གཅིག །ཆོས་ཀྱི་མཆོག་ས༌[^1322]གང་ཡིན་པ་སེམས་བཅུ་དྲུག་པོ་འདི་དག་ཀྱང་དེའི༌[^1323]ས་པ་དག་གོ། །

[Block 3359]
ཅིའི་ཕྱིར་གདོན་མི་ཟ་བར་བཟོད་པ་དག་དང་ཤེས་པ་དག་ཡིན་ཞེ་ན།

[Block 3360 [VERSE]]
བཟོད་དང་ཤེས་པ་གོ་རིམས་བཞིན། །
བར་ཆད་མེད་དང་རྣམ་གྲོལ་ལམ། །

[Block 3361]
བཟོད་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་རྣམ་པར་གཅོད་པ་ལ་བར་ཆད་བྱ་བར་མི་ནུས་པའི་ཕྱིར་བར་ཆད་མེད་པའི་ལམ་དག་ཡིན་ནོ། །ཤེས་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་ལས་རྣམ་པར་གྲོལ་བའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རྣམ་པར་གྲོལ་བའི་ལམ་དག་ཡིན་ནོ། །

[Block 3362]
ཅི་སེམས་བཅུ་དྲུག་པོ་ཐམས་ཅད་བདེན་པ་མཐོང་བའི་ལམ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་དེ་ལས་སྐད་ཅིག་བཅོ་ལྔ་ནི། མ་མཐོང་མཐོང་ཕྱིར་མཐོང་བའི་ལམ། །སེམས་བཅུ་དྲུག་པ་ལ་ནི་སྔོན༌[^1324]མ་མཐོང་བ་བལྟ་བར་བྱ་བ་མེད་ཀྱི། ཇི་ལྟར་མཐོང་བ་གོམས་པར་བྱེད་པའི་ཕྱིར་བསྒོམ་པའི་ལམ་ཁོ་ནའོ། །

[Block 3363]
མཐོང་བའི་ལམ་དང་བསྒོམ་པའི༌[^1325]ལམ་ཇི་ལྟར་སྐྱེ་བ་བཤད་ཟིན་ཏོ། །

[Block 3364 [HEADING]]
### འཕགས་པའི་ལམ་སྐྱེས་པའི་གང་ཟག་རྣམས་རྣམ་པར་གཞག་པ། ^6-2-0

[Block 3365 [HEADING]]
#### ངེས་པར་འཇུག་པའི་གང་ཟག་རྣམ་པར་གཞག་པ། ^6-2-1-0
--- END BLOCKS ---
