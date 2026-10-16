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
[Block 316]
དེ་ནས་སྡེ་པ་འོང་བ་ཐོས་ནས་ཉེ་སྡེས་འཇིགས་ནས་ཛེ༌[^209]ཏའི་ཚལ་དུ་རབ་ཏུ་བྱུང་ངོ་། །དེས་ཕྱིས་བདག་གི་ཁྱིམ་དུ་ཕྱིན་པ་དང་། སྡེ་པའི་ཆུང་མས་ཁྱོ་ནི་འོང་ཁྱོད་ནི་ཐར་ན་བདག་ཇི་ལྟར་བྱ་ཞེས་དྲིས་པ་དང་། ཉེ་སྡེས་གྲོགས་པོ་སྨན་པ་གཅིག༌[^210]ལ་ཇི་ལྟར་གྱུར་པ་རྒྱས་པར་སྨྲས་ནས། སྨན་པས་བདག་གིས༌[^211]མངལ་འཇིག་པར་འགྱུར་བའི་སྨན་གྱིས་མངལ་ན་ཡོད་པ་དེ་དུམ་བུར་ཞིག་པར་འགྱུར་བ་དེ་སྦྱིན་ནོ་ཞེས་བྱས་ཏེ། སྡེ་པའི་ཆུང་མ་ལ་སྨན་ཕྱེ་མ་བླུད་པས་རུམ་ན་ཡོད་པ་ཡང་མེད་པར་གྱུར་ཏོ། །

[Block 317]
ཉེ་སྡེ་ཡང་སྨན་བྱས་པ་ལ་ཡི་རང་ནས་ཅང་མ་སྨྲས་སོ། །

[Block 318]
དུས་ཕྱི་ཞིག་ན་དེ་ལྟར་གྱུར་པ་སྐྱེ་བོ་ཀུན་གྱིས་ཐོས་ནས་དགེ་སློང་ཞེས་འཛེར་ཏོ། །

[Block 319]
དེ་ལྟར་གྱུར་པ་དེ་དགེ་སློང་རྣམས་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཉེ་སྡེ་ལ་ཁྱོད་ཀྱིས་དེ་ལྟར་བྱས་པ་བདེན་ནམ་ཞེས་སྨྲས་ནས། བཙུན་པ་དེ་ལྟར་ནི་མ་བགྱིས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་ནི་བགྱིས་སོ་ཞེས་གསོལ་པས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉེ་སྡེ་ལ་ནི་ལྟུང་བ་མེད་ཀྱིས་ཕྱིན་ཆད་དེ་ལྟ་བུ་ལ་ཡི་རང་ན་ཉེས་པ་དང་བཅས་པར་འགྱུར་རོ། །

[Block 320]
དགེ་སྦྱོང་གིས་སྐྱེས་པའམ་བུད་མེད་དམ་མ་ནིང་ལ་གསད༌[^212]སེམས་ཀྱིས་ཁ་ཟས་ཀྱི་ནང་དུ་དུག་སྦྱར་མ་བླུགས་པ་དང་། ཁྲུས་ཆུ་དང་། སྐོམ༌[^213]དང་། བདུག་སྤོས་ཀྱི༌[^214]ནང་དུ་དུག་གི་ཕྱེ་མ་བླུགས་ཏེ་འདིས་འཆི་བར་འགྱུར་རོ་སྙམ་ན་ཡང་དེ་ཉིད་ཀྱི་ཚེ་ཤིའམ་དུས་ཕྱིས་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 321]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 322]
དགེ་སྦྱོང་གིས༌[^215]ཆང་ངམ་སྨྱོ་བའི་སྨན་བྱིན་ཏེ་ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེ་ཉིད་ཀྱི་ཚེའམ་ཕྱིས་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 323]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 324]
འཆི་བའི་ཕྱོགས་སུ་བཏང་ངམ༌[^216]ཞེས་བྱ་བ་ལ་དགེ་སྦྱོང་གིས་གསད༌[^217]སེམས་ཀྱིས་གཡང་དུ་ཕུལ་བ་དང་། མེར་ཕུལ་བ་དང་། འཆི་བའི་ཕྱོགས་སུ་བཏང་བ་དང་། སྟག་གཟིག༌[^218]ལ་སོགས་པ་གཅན་གཟན་གདུག༌[^219]པའི་གནས་སུ་བཏང་བ་དང་། སྦྲུལ་དང་སྡིག་པ་ལ་སོགས་པ་སྲོག་ཆགས་གདུག་པའི་གནས་སུ་བཏང་བའམ། གསད་པར༌[^220]འདོད་པས་གྲང་བའི་ཚེ་གྲིབ་མ་ལ་བཞག་ནས་ལྷགས་པ༌[^221]ལ་བོར་བ་དང་། དྲོ་བའི་ཚེ་ཉི་མ་ལ་བཞག་ནས་དྲོ༌[^222]ཁུང་དུ་བཞག་སྟེ་ཐབས་འདིས་ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེའི་ཚེ་ཤིའམ་ཕྱིས་ཤི་ན་ཡང་ཕས་ཕམ་པའོ། །

[Block 325 [VERSE]]
མི་གཞན་ཐབས་རྣམས་སྣ་ཚོགས་ཀྱིས། །
བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར། །

[Block 326]
ཞེས་བྱ་བ་ལ་གཞན་གསད་པའི༌[^223]བསམ་པས་ཐབས་ཀྱིས་འཆི་བས་བསད་པ་འམ་ཤིང་ལ་འཆིང་བས་བསད་པ་དང་། དེ་ལ་དགེ་སྦྱོང༌[^224]གིས་གསད༌[^225]སེམས་ཀྱིས་སྤྱུགས་ནས་སྟག་གཟིག་གམ་འཕར་སྤྱང་ལ་སོགས་པས་ཟོས་སམ། ཐབས་ཅི་ཡང་རུང་བས་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 327]
དགེ་སྦྱོང་གིས་གསད༌[^226]སེམས་ཀྱིས་མི་ཤིང་ལ་འབྲེང་རློན་གྱིས་བཅིངས་ཏེ་བཞག་པ་ལ་སྟག་གཟིག་གམ་འཕར་སྤྱང་ལ་སོགས་པས་ཟོས་སམ་ཅིའི་ཐབས་ཀྱིས་ཤི་ཡང་ཕམ་པའོ། །

[Block 328]
དགེ་སྦྱོང་གིས༌[^227]བུད་མེད་སྦྲུམ་མ་གསད་པར་བསམས་ཏེ་དཀུ་མཉེས་པ་ལས་མ་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 329]
བུ་ཤི༌[^228]ལ་མ་མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 330]
གཉིས་ཀ་མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 331]
བུ་བསད་པར་འདོད་དེ། དཀུ་མཉེས་པ་ལས་བུ་ཤི་ལ་མ་མ་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 332]
བུ་མ་ཤི་ལ་མ་ཤི་ན་ཡང༌[^229]སྦོམ་པོའོ། །

[Block 333]
གཉིས་ཀ་མ་ཤི་ན་ཡང་སྦོམ་པོའོ། །

[Block 334]
དེ་བཞིན་དུ་དགེ་སྦྱོང་གིས་གསད༌[^230]སེམས་ཀྱིས་སྙིང་ཁར༌[^231]འདེབས་པའི་རལ་གྲི་དང་ཆུ་གྲི་བཞག་པ་དང་། གཏོར་མ་བཞག་པ་དང་། ས་མདའ་དང་། རྩང་བཙུགས་པ་ལ་སོགས་པ་བཞག་པ་ལ་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 335]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 336]
འདི་ཡན་ཆད་ཀྱིས་ཕས་ཕམ་པའི་ཟླ་ལ་སྦོམ་པོ་ཡང་བཅད་དེ་བཤད་དོ། །

[Block 337]
ཡན་ལག་བདུན་དང་ལྡན་ན་སྲོག་གཅོད་པའི་མཚན་ཉིད་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 338]
བདུན་གང་ཞེ་ན། མིའི་རྒྱུད་ཡིན། མི་ཡིན། གཞན་མ་ཡིན། མིར་འདུ་ཤེས། སྦྱོར་བ་བྱས། འཚོ་བ་ཉམས། བདག་མ་སྨྱོས་པའོ། །

[Block 339 [HEADING]]
#### སྦོམ་པོའི་གནས། ^5-1-2-0

[Block 340]
བྱོལ་སོང་དང་ནི་སེམས་དམྱལ་དང་། །ཡི་དགས་འོན་ཏེ་ལྷ་ཡང་རུང་།[^232] །བསད་ན་ངན་འགྲོར་ལྷུང་བ་ཡིས།[^233] །

[Block 341 [VERSE]]
སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར། །
བརྟུལ་ཞུགས་ཅན་གྱིས་བསད་སྙམ་སྟེ། །
ལུས་དང་ངག་གི་སྦྱོར་བ་ལས། །
སྐྱེ་བོ་གསོན་ཡང་དེ་ལ་ནི། །

[Block 342]
ཁ་ན་མ་ཐོ་རྣམ་གསུམ་འགྱུར། །ཞེས་བྱ་བས་ཉེས་པ་སྦོམ་པོའི་གནས་བསྟན་ཏེ། བྱོལ་སོང་ནི་རྟ་དང་བ་ལང་དང་ལུག་ལ་སོགས་པ་ལ་བྱ་སྟེ། དགེ་སྦྱོང་གིས་གསད༌[^234]སེམས་ཀྱིས་བྱོལ་སོང་བསད་ན་སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། སེམས་ཅན་དམྱལ་བ་དང་ཞེས་བྱ་བ༌[^235]སེམས་ཅན་དམྱལ་བ་ལ་རྣམ་པ་གཉིས་ཏེ། སེམས་ཅན་དམྱལ་བ་ཆེན་པོ་དང་། ཕྱོགས་གཅིག་པའི་སེམས་ཅན་དམྱལ་བའོ། །

[Block 343]
སེམས་ཅན་དམྱལ་བ་ཆེན་པོ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚ་བའི་སེམས་ཅན་དམྱལ་བ་དང་། གྲང་བའི་སེམས་ཅན་དམྱལ་བའོ། །

[Block 344]
དེ་ལ་ཚ་བའི་སེམས་ཅན་དམྱལ་བ་ནི་མནར་མེད་པ་དང་། རབ་ཏུ་ཚ་བ་དང་། ཚ་བ་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ངུ་འབོད་དང་། བསྡུས་འཇོམས༌[^236]དང་། ཐིག་ནག་དང་། ཡང་སོས་སོ། །

[Block 345]
གྲང་བའི་སེམས་ཅན་དམྱལ་བ་ཆེན་པོ་ལ་ཡང་བརྒྱད་དེ། ཆུ་བུར་དང་། ཆུ་བུར་ཆེན་པོ་དང་། པདྨ་དང་། པདྨ་ཆེན་པོ་དང་། ཨུཏྤ་ལ་དང་། ཨུཏྤ་ལ་ཆེན་པོ་དང་། ཧ་ཧ་ཞེས་ཟེར་བ་དང་། ཧུ་ཧུ་ཞེས་ཟེར་རོ། །

[Block 346]
ཕྱོགས་གཅིག་པའི་སེམས་ཅན་དམྱལ་བ་ཞེས་བྱ་བ་ནི་ལྷའི་ལོངས་སྤྱོད་ཀྱང་ཡོད་ལ་བར་འགའ་ནི་སེམས་ཅན་དམྱལ་བའི་སྡུག་བསྔལ་ཡང་མྱོང་བའོ། །

[Block 347]
དགེ་སྦྱོང་གིས་གསད༌[^237]སེམས་ཀྱིས་སེམས་ཅན་དམྱལ་བ་བསད་ན༌[^238]སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 348]
ཡི་དགས་ཞེས་བྱ་བ་ལ། ཡི་དགས་ཞེས་བྱ་བ་ནི་ཕལ་ཆེར་གཅོང་རོང་དང་མྱ་ངན༌[^239]དག་ན་གནས་སོ། །

[Block 349]
དགེ་སྦྱོང་གིས་གསད༌[^240]སེམས་ཀྱིས་ཡི་དགས་བསད་ན་སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 350]
ལྷ་ཡང་རུང་ཞེས་བྱ་བས་འདོད་ཁམས་ཀྱི་ལྷ་དང་། གཟུགས་ཁམས་ཀྱི་ལྷ་དང་། གནས་རིས་བཅུ་བདུན་ཞེས་བྱ་བ་ན་གནས་པའི་ལྷ་རྣམས་དགེ་སྦྱོང་གིས༌[^241]བསད་ན་སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 351]
སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་གང་ཞེ་ན། སྡིག་པ་སྦོམ་པོའི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། བསད་ན་ངན་སོང༌[^242]ལྟུང་བའི་ཞེས་བྱ་བ་སྨོས་ཏེ། དཔེར་ན་དུག་ཆེན་པོས་ཀྱང་སྐྱེས་བུ་ཆེན་པོ་གསོད་ལ། དུག་ཆུང་ངུས་ཀྱང་སྐྱེས་བུ་ཆེན་པོ་གསོད་པ་དང་། དེ་བཞིན་དུ་མེ་སྟག་ཆེན་པོས་ཀྱང་ཡུལ་ཆེན་པོ་ཚིག༌[^243]ལ་མེ་སྟག་ཆུང་ངུས་ཀྱང་ཡུལ་ཆེན་པོ་སྲེག་པ༌[^244]དང་། ཕས་ཕམ་པ་བྱུང་ན་ངན་སོང་གསུམ་དུ་སྐྱེ་བར༌[^245]འགྱུར་བ་དེ་བཞིན་དུ་ཉེས་པ་སྦོམ་པོ་བྱུང་བ་ལ་ཚུལ་བཞིན་དུ་མ་བཤགས་ན་ངན་སོང་གསུམ་དུ་ལྟུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 352]
བརྟུལ་ཞུགས་ཅན་གྱིས་བསད་སྙམ་སྟེ། །ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་གིས་སྐྱེས་པ་དང་བུད་མེད་དང་། མ་ནིང་སྟེ་མི་རྣམ་པ་གསུམ་ལས་གང་ཡང་རུང་བ་ཅིག་བསད་དོ་སྙམ་དུ་བསམས་ཏེ་ལུས་དང་ངག་གི༌[^246]སྦྱོར་བ་བཤམས་པ་ལས་ཞེས་བྱ་བ་ལ། ལུས་ཀྱིས་བཤམས་ཏེ་ཁུ་ཚུར་དང་ཐལ་མོ་དང་རྡོ་དབྱིག་དང་མཚོན་ཆས་ཀྱང་བཏབ། ངག་གིས་བཤམས་ཏེ་གོང་དུ་བཤད་པ་བཞིན་དུ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། ཚུལ་ཁྲིམས་འཆལ་བ་དང་། ནད་པ་རྣམས་འཆི་བའི་རིགས་སོ་ཞེས་བསྔགས་པ་བརྗོད་པ་ལས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 353 [VERSE]]
སྐྱེ་བོ་གསོན་ཡང་དེ་ལ་ནི། །
ཁ་ན་མ་ཐོ་རྣམ་གསུམ་འགྱུར། །

[Block 354]
ཞེས་བྱ་བ་ལ། གསད་པར༌[^247]ཡང་བསམས་ལུས་དང་ངག་གིས་ཀྱང་བཤམས་པ་ལས་མི་གསུམ་པོ་གསོན་ཏེ་མ་ཤི་ཡང་དགེ་སྦྱོང་དེ་ལ་ཁ་ན་མ་ཐོ་བ་རྣམ་པ་གསུམ་ཐོབ་པར་འགྱུར་ཏེ། ཡིད་ཀྱི་ཉེས་པ་སྦོམ་པོ་དང་། ལུས་ཀྱི་ཉེས་པ་སྦོམ་པོ་དང་། ངག་གི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །

[Block 355]
དེ་ལ་གསད་པར༌[^248]བསམས་པས་ན་ཡིད་ཀྱི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
