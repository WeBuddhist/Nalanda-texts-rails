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
[Block 5146]
དེའི་གནས་སུ་གྱུར་པ་ནི་སྐྱེད་མོས་ཚལ༌[^3308]གྱི་ཡོན་ཏན་བས་ཀྱང་ལྷག་པའི་གནས་སུ་གྱུར་པའོ། །

[Block 5147]
འཁྲིད་ཤིང༌[^3309]འཁྱིལ༌[^3310]པས་གཏིབས་པ་ཞེས་བྱ་བ་ནི། གྲང་ཕ་སེལ་བར་བྱེད་པ་སྟེ། ལྡིང་ཁང་ནི་བསིལ་བའོ། །

[Block 5148 [VERSE]]
མེ་ཏོག་རྒྱས་པའི་ལྗོན་ཤིང་དགོད་པ་བཞིན། །
པདྨ་རབ་ཏུ་རྒྱས་པའི་མཚོ་འགྲམ་ན། །
ཞེས་བྱ་བས་ནི་ཚ་བ་བཙལ་བས༌[^3311]སོ། །
གཞལ་མེད་ཁང་ལ་ལྟ་བས་ཆགས་གྱུར་བ། །

[Block 5149]
ཞེས་བྱ་བ་ནི་དུས་དྲོ་བའི་ཕྱིར་དང་། གཞལ་མེད་ཁང་རབ་ཏུ་མཛེས་པའི་ཕྱིར་རོ། །

[Block 5150]
པདྨའི་མཚོ་ཞེས་བྱ་བ་ལ་པདྨའི་མཚོ་ནི་གྲང་པའི་ཕྱིར་ཏེ། དུས་ནི་དྲོ་བ་ཉིད་ཀྱིས་བུང་བ་དང་རད་པ་བཞིན་དུ་མེ་ཏོག་ཤིང་ལ་ཞེས་པ༌[^3312]ནི་མེ་ཏོག་ལ་ལྷག་པར་ཆགས་པའི་ཕྱིར་རོ། །

[Block 5151]
སྐབས་ནི་མཚམས་ཏེ། དུས་ལ་བབ་པར་ཤེས་པ་སྟེ། གཉིད་ཀྱི་དབང་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 5152]
ཇི་ལྟར་དགའ་བའི་ཚན་ཚན་དུ་ཆད་པ་དེ་ནི་དགའ་སྟེ། དགའ་སྡེར་ཆད་པའོ། །

[Block 5153]
དེས་ན་དཀའ་ཐུབ་ཀྱི་གནས་སུ་ཕྱིན་པར་གྱུར་ཏོ། །

[Block 5154]
བསྙེན་དཀའ་བའི་རྒྱུས་རབ་ཏུ་ཟབ་པའོ། །

[Block 5155]
དཀའ་ཐུབ་ཀྱི་དཔལ་འབར་བ་དང་། བསམ་གཏན་ལ་གོམས་པར་བྱས་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 5156]
གཡེང་བ་དང་། འཛེམ་པ་དང་། འཕྱར་བ་གང་གིས་བཏང་བ་དེ་ནི། གཡེང་བ་དང་། འཛེམ་པ་དང་། འཕྱར་བ་བཏང་བའོ། །

[Block 5157]
དྲི་བ་ནི་དེ་དག་ལ་ནད་དྲི་བའོ། །

[Block 5158]
དེ་དག་ལ་ནད་དྲི་བའི་སྐབས་ནས་གླེང་བསླང་བ་གང་ཡིན་པའི་གཏམ་དེ་ན༌[^3313]དེ་དག་ལ་ནད་དྲི་པའི་སྐབས་ནས་གླེང་བསླང་བའོ། །

[Block 5159]
གོ་བར་སླ་བའི༌[^3314]དོན་གང་ཡིན་པ་དེ་ནི་གོ་བར་སླ༌[^3315]བའོ། །

[Block 5160]
བུད་མེད་ཀྱི་སྐྱེ་བོ་དག་གིས་གོ་བར་སླ་བའི༌[^3316]དོན་གང་ཡིན་པ་དེ་ནི། བུད་མེད་ཀྱིས་གོ་བར་སླ༌[^3317]བའོ། །

[Block 5161]
ཡང་ན་གཟུང་བར་བྱ་བ་ཡིན་པས་གཟུང་བའོ། །

[Block 5162]
བདེ་བར་གཟུང་བའི་དོན་གང་ཡིན་པ་དེ་ནི་བདེ་བར་ཟིན་པའོ། །

[Block 5163]
ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 5164]
ནད་དྲི་བའི་སྐབས་ནས་གླེང་བསླང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུམ་གྱི༌[^3318]དམ་བཅའ་བ༌[^3319]དང་། གཏན་ཚིགས་དང་། དཔེ་སྟེ། གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །

[Block 5165]
མ་སྨད་ཅེས་བྱ་བ་ནི་ཡ་རབས་ཉིད་དུ་སྐྱེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5166]
མིའི་ལུས་སུ་སྐྱེས་པ་ཞེས༌[^3320]བྱ་བ་ནི་མི་ཉིད་དུ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5167]
དེ་བཞིན་དབང་པོ་རྣམས་ཀྱང་མ་ཉམས་རྣོ་དང་ལྡན། །ཞེས་བྱ་བ་ལ་དབང་པོ་ཐམས་ཅད་མ་ཉམས་པ་ནི། མ་ཚང་བ་མེད་པ་དང་། རྣོ་བ་དང་ལྡན་པའོ། །

[Block 5168]
དེས་པར་འཆི་བདག་ཅེས་བྱ་བ་ནི་འཆི་བའི་ཆོས་སོ། །

[Block 5169]
བག་མེད་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་དགེ་བའི་ཆོས་རྣམས་མི་བསྟེན་པའོ། །

[Block 5170]
དགེ་བའི་ཆོས་དེ་ཡང་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པ་སྟེ།[^3321] དེ་དག་ལ་མ་བརྟེན་ཅིང་། མ་བསྒོམས་པས་ནི་བསླུས་པར་གྱུར་པ་ཡིན་ཏེ། དགེ་བའི་ཆོས་མ་བསྒོམས་ན་ནི་ཡང་དེའི་འབྲས་བུ་འཐོབ་པར་མི༌[^3322]འགྱུར་རོ། །

[Block 5171]
དེ་ཡང་ཚེ་སྐད་ཅིག་མ་གཅིག་གིས་ཟད་པ་དང་། ཚེ་ཐུང་བའི་ཕྱིར་དང་། འདས་ནས་ཀྱང་ལྡོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 5172 [VERSE]]
འདི་ནི་རེ་ཞིག་དམ་བཅའ་བའོ། །
ཅིའི་ཕྱིར་སླུ་བ་ཡིན་ཞེ་ན།
དགེ་བ་མི་བྱེད་བས་སོ། །

[Block 5173]
འདི་ནི་གཏན་ཚིགས་སོ། །

[Block 5174]
དེའི་རྒྱུ་རབ་ཏུ་མི་འབྱུང་ཞིང་ཟད་པ༌[^3323]དང་། དེའི་རྒྱུ་འབྱུང་བར་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་གཉིས་སྨོས་ཏེ། རབ་ཏུ་སྦྱིན་དང་ཞེས་བྱ་བ་དང་། རིགས་ལ་སོགས་པ་དམན་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །

[Block 5175]
རིགས་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུའོ། །

[Block 5176]
གཟུགས་དང་། ལང་ཚོའི་ཡོན་ཏན་དང་། སྟོབས་རབ་ཏུ་ཆེ་བ་དང་། ནོར་ལ་སོགས་པ་ནི་སྦྱིན་བའི་འབྲས་བུའོ། །

[Block 5177]
དེ་ཡང་ཁ་དོག་ཕུན་སུམ་ཚོགས་པར་བྱིན་པས་ནི། གཟུགས་བཟང་བའོ། །

[Block 5178]
ཡང་ན་གོས་བྱིན་པས་སོ། །

[Block 5179]
ལང་ཚོའི་ཡོན་ཏན་རྣམས་དང་། སྟོབས་རབ་ཏུ་ཆེ་བ་ནི། ཉམས༌[^3324]བརྟས་པའི་བཟའ་བ༌[^3325]དང་། བཏུང་བ་བྱིན་པའི་འབྲས་བུའོ། །

[Block 5180]
ནོར་གྱིས་ཕྱུག་པར་གྱུར་པ་ནི་ནོར་བྱིན་པའི་འབྲས་བུའོ། །

[Block 5181]
ཕྱི་མ་ལ་ཡང་བདེ་བ་འཐོབ་མི་འགྱུར། །ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་དུ་སྟེ། འཇིག་རྟེན་འདིའི་བདེ་བའི་རྒྱུས་ཏེ། བདེ་བ་ནི་དགེ་བ་ལ་སོགས་པ་ཡིན་པས་སོ། །

[Block 5182]
རབ་ཏུ་སྦྱིན་དང་ཚུལ་ཁྲིམས་ལ་སོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱང་གཟུང༌[^3326]ངོ་། །དགེ་བ་དེ་ནི་ཐམས་ཅད་ཀྱི་རྒྱུ་ཡིན་པའི་ཕྱིར། འདི་ལས་བྱུང་ཞེས་བྱ་བས་བསྟན་པ་ཡིན་ནོ། །

[Block 5183]
ད་ནི་འབྲས་བུ་དེ་མེད་པར་ཡང་སྦྱིན་པ་ལ་སོགས་པ་དང་ལྡན་ན་འབྲས་བུ་སྐྱེ་བའི་དབང་དུ་བྱས་ནས། དེ་མེད་ཀྱང་དེའི་དངོས་པོའི་རྒྱུ་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་སྨྲས་པ། རིགས་ལ་སོགས་པ་དམན་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5184]
སྡིག་པ་ལ་མ་ཆགས་ཤིང་ཞེས་བྱ་བས་ནི། སྡིག་པ་ལས་ལྡོག་པར་སྟོན་ཏེ། མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལས་ལྡོག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5185]
རབ་ཏུ་སྦྱིན་དང་ཚུལ་ཁྲིམས་ལ་སོགས་ཡོན་ཏན་ལྡན། །ཞེས༌[^3327]བྱ་བ་ནི། སྦྱིན་པ༌[^3328]དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ལྡན་པའོ། །
--- END BLOCKS ---
