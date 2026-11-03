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
[Block 281]
མ་ནོར་བ་ཞེས་བྱ་བ་ལ་ཡང་མི་རྣམ་པ་གསུམ་བསད་ན་ཕས་ཕམ་པར་འགྱུར་བ་ལས།

[Block 282]
བདག་ཀྱང་མིའི་རྒྱུད་དུ་གཏོགས་པ་ཡིན་ཏེ། བདག་གིས་བདག་བསད་པ་ན་ཕས་ཕམ་པར་མི་འགྱུར་གྱི་བདག་གིས་གཞན་བསད་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 283]
བདག་གིས་གཞན་བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། བདག་ཉིད་ཀྱིས་ལག་དར་ཏེ༌[^175]མི་རྣམ་པ་གསུམ་བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར་ཏེ་ཕས་ཕམ་པ་འབྱུང༌[^176]བས་དགེ་སྦྱོང་དུ་མི་རུང་ཞིང་འཕགས་པའི་བདེན་པ་མཐོང་བ་དང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་སྐལ་བ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 284 [HEADING]]
###### ཟིན་པའི་ལུས་སུ་གཏོགས་པ། ^5-1-1-1-1-0

[Block 285]
དེ་ལ་བདག་གིས་བསད་པ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཟིན་པའི་ལུས་སུ་གཏོགས་པ་དང་། ཕྱི༌[^177]རོལ་གྱིས༌[^178]འཕངས་པ་དང་། གཉིས་ཀ་དང༌[^179]ཡང་ལྡན་པའོ། །ཇི་ལྟར་ཟིན་པའི་ལུས་སུ་གཏོགས་པས་ཤེ་ན། དགེ་སྦྱོང་གིས་གསད༌[^180]སེམས་ཀྱིས་སྐྱེས་པ་དང་། བུད་མེད་དམ༌[^181]མ་ནིང་ཁུ་ཚུར་རམ་རྡོ་འམ་ཐ་ན་སོར་མོ་གཅིག་བསྣུན་ཏེ། ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེ་ཉིད་ཀྱི་ཚེའམ་ཕྱིས་ཤི་བར་གྱུར་ན་ནི་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 286]
མ་ཤི་ན་ཉེས་པ་སྦོམ་པོའོ། །

[Block 287 [HEADING]]
###### ཕྱི་རོལ་གྱིས་འཕངས་པ། ^5-1-1-1-2-0

[Block 288]
ཕྱི་རོལ་གྱིས་འཕངས་པ་གང་ཞེ་ན། དགེ་སྦྱོང་གིས་བསད་སེམས་ཀྱིས༌[^182]མི་ལ་མདའ་འཕངས་པའམ། མདུང་དང་། བེ་ཅོན་དང་། ཐ་ན་རྒྱ་ཤུག་གིས་བསྣུན་ཏེ་དེས་ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེ་ཉིད་ཀྱི་ཚེའམ་དུས་ཕྱིས་ཤི་ན་ཡང་པས་ཕམ་པའོ། །

[Block 289]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 290 [HEADING]]
###### གཉིས་ཀ་དང་ལྡན་པ། ^5-1-1-1-3-0

[Block 291]
གཉིས་ཀ་དང་ལྡན་པ་གང་ཞེ་ན། དགེ་སྦྱོང་གིས་མི་ལ་བསད་སེམས་ཀྱིས་རལ་གྲི་དང་དབྱིག་པ༌[^183]དང་མདུང་ཐུང་གིས་བསྣུན་ཏེ་འདིས་ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེ་ཉིད་ཀྱི་ཚེའམ་ཕྱིས་ཤི་ན་ཡང་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 292]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 293 [HEADING]]
##### གཞན་གསོད་དུ་བཅུག་པ། ^5-1-1-2-0

[Block 294]
གཞན་རྣམས་ཀྱིས་བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར་ཞེས་བྱ་བ་ལ། མི་རྣམ་པ་གསུམ་བསད་པའི་ཕྱིར་བདག་གིས་གཞན་ལ་གསོད་དུ་བཅོལ་བ་ལས་དེས་མི༌[^184]རྣམ་པ་གསུམ་གང་ཡང་རུང་བས་བསད་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 295]
འདིར་རྣམ་པ་གསུམ་བཞག་སྟེ། ཟིན་པའི་ལུས་སུ་གཏོགས་པ་དང་། ཕྱི༌[^185]རོལ་གྱིས༌[^186]འཕངས་པ་དང་། གཉིས་ཀ་དང་ལྡན་པ་བཤད་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 296]
ཚིག་དེ་དག་གིས་ནི་བདག་གིས་བསད་པ་དང་།

[Block 297]
གཞན་གྱིས་བསད་པ་སྟོན་ཏོ། །

[Block 298 [HEADING]]
##### ཐབས་ཀྱིས་བསད་པ། ^5-1-1-3-0

[Block 299 [VERSE]]
ཚུལ་ཁྲིམས་ལྡན་ནམ་ཚུལ་ཁྲིམས་འཆལ། །
དེ་བཞིན་ནད་ཀྱིས་བཏབ་པ་ལ། །
གང་ཐོས་སྡུག་བསྔལ་ཉམ་ཐག་སྟེ། །

[Block 300 [VERSE]]
ངེས་འཆིའི་ཆོས་གཏམ་དེ་མི་བྱ། །
སྨན་དང་སྔགས་དང་རིག་པ་དང་། །
འཆི་བའི་ཕྱོགས་སུ་བཏང་བའམ། །
མི་གཞན་ཐབས་རྣམས༌[^187]སྣ་ཚོགས་ཀྱིས། །

[Block 301]
བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར། །ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཐབས་ཀྱིས་གསོད་པ་བསྟན་ཏེ། ཐབས་ཀྱིས།

[Block 302 [VERSE]]
ཚུལ་ཁྲིམས་ལྡན་ནམ་ཚུལ་ཁྲིམས་འཆལ། །
དེ་བཞིན་ནད་ཀྱིས་བཏབ་པ་ལ། །
གང་ཐོས་སྡུག་བསྔལ་ཉམ་ཐག་སྟེ། །
ངེས་འཆིའི་ཆོས་གཏམ་དེ་མི་བྱ། །

[Block 303]
ཞེས་བྱ་བས་ཚིག་གི་སྒོ་ནས་ཐབས་ཀྱིས་གསོད་པ་རྣམས་ཤིག་བསྟན་ཏེ། དེ་ཡང་རྣམ་པ་གསུམ་ཡོད་དེ། གང་ཞེ་ན། ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། ཚུལ་ཁྲིམས་འཆལ་པ་དང་། ནད་ཀྱིས་བཏབ་པ༌[^188]ལ་ཚུལ་ཁྲིམས་དང་ལྡན་ནམ་ཞེས་བྱ་བ་དང་། གང་ཐོས་ཞེས་བྱ་བ་དང་། ངེས་འཆིའི་ཆོས་གཏམ་དེ་མི་བྱ། །ཞེས་བྱ་བར་སྦྱར་ཏེ། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་འཚོ་བའི་ཡོ་བྱད་འདོད་པའི་ཕྱིར་ཚེ་དང་ལྡན་པ་ཁྱོད་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དགེ་བའི་ཆོས་ཅན་ཡིན་པས་འདི་ནས་ཤི་འཕོས་ནས་ཚེ་རབས་གཞན་དུ་སྐྱེས་ན་ལོ་ལེགས་པ་དང་འདྲ། མཐོ་རིས་ནི་དར་ལས་ཆོད། ཐར་པ་ནི་ཡོལ་བ་ལྟ་བུས་ཆོད་དེ་ལུས་དང་བྲལ་ནས་ལྷར་སྐྱེས་པར་འགྱུར་གྱིས་རང་གིས་རང་སོད༌[^189]ཅིག་ཅེས་བསྒོ་བ་ལས་དེ་ཤི་ན་ནི་ཕས་ཕམ་པའོ། །

[Block 304]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 305]
ཚུལ་ཁྲིམས་འཆལ་ཅེས་བྱ་བ་དང་། གང་ཐོས་ཞེས་བྱ་བ་དང་། ངེས་འཆིའི་ཆོས་གཏམ་དེ་མི་བྱ། །ཞེས་བྱ་བར་སྦྱར་ཏེ། ཚུལ་ཁྲིམས་འཆལ་བ་ཅན་ལ་ཡོ་བྱད་འདོད་པའི་ཕྱིར། འཆིར་གཞུག་གོ་སྙམ་དུ་བསམས་ནས་ཚེ་དང་ལྡན་པ་སྡིག་པའི་ཆོས་ཅན་ལུས་དང་ངག་གིས་ངན༌[^190]པར་སྤྱོད་པ་ཁྱོད་ཇི་ཙམ་དུ་ཡུན་རིང་དུ་གསོན་པ་དེ་ཙམ༌[^191]ངན་སོང་དུ་སྐྱེ་བར་འགྱུར་བའི་སྡིག་འཕེལ་བས་རང་གིས༌[^192]རང་སོད༌[^193]ཅིག་ཅེས་བསྒོ་བ་ལས་ཤི་ན་ཕས་ཕམ་པར་འགྱུར་རོ།[^194] །མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 306 [VERSE]]
དེ་བཞིན་ནད་ཀྱིས་བཏབ་པ་ལ། །
གང་ཐོས་སྡུག་བསྔལ་ཉམ་ཐག༌[^195]སྟེ། །
ངེས་འཆིའི་ཆོས་གཏམ་དེ་མི་བྱ། །

[Block 307]
ཞེས་བྱ་བས་ནད་པ་སྦྱར་ཏེ། ནད་ཀྱིས༌[^196]བཏབ་པའི་ནད་པ་ལ༌[^197]ནད་པའི་ཡོ་བྱད་འདོད་པའི་ཕྱིར། ཚེ་དང་ལྡན་པ་ནད་བུ་ཅན་སྡུག་བསྔལ་གྱིས༌[^198]རྙོངས་པ་ཇི་སྲད་དུ་ཡུན་རིང་དུ་འཚོ་བ་དེ་སྲིད་དུ་སྡུག་བསྔལ་དུ་འགྱུར་གྱིས་རང་གིས་རང་སོད༌[^199]ཅིག་ཅེས་གདོན་མི་ཟ་བར་འཆི་བའི་གཏམ་མི་བྱའོ། །

[Block 308]
གལ་ཏེ་གདོན་མི་ཟ་བར་འཆི་བར་འགྱུར་པའི་གཏམ་བྱས་པ་ལས་ཤི་ན་ཕས་ཕམ་པའོ། །

[Block 309]
མ་ཤི་ན་སྦོམ་པོའོ། །

[Block 310]
གོང་དུ་སྨོས་པ་ལྟར་བསྟན་པ་ལ༌[^200]དགེ་སྦྱོང་གིས་འགྱོད་དེ་ང་ནི་བྱིས་པ་དང་འདྲ་བས་གྱི་ན་ཞིག་སྨྲས་ཀྱི་རང་མ་གསོད་ཅིག་ཅེས་བསྒོ་བ་ལས་ཤི་ཡང་རུང་མ་ཤི་ཡང་རུང༌[^201]ཕྱིས་འགྱོད་དེ་བསྒོ་ན་སྦོམ་པོར་ཟད་དོ། །

[Block 311]
སྨན་དང་ཞེས་བྱ་བ་ལ། སྨན་དེ༌[^202]དུག་གིས་བསད་པའི་གླེང་གཞི་ནི།[^203] བཅོམ་ལྡན་འདས་ཛེ་ཏའི་ཚལ་ན་བཞུགས་སོ། །

[Block 312]
དེ་ན་ཁྱིམ་བདག་སྟོབས་སྡེ་ཞེས་བྱ་བ་ལོངས་སྤྱོད་ཆེ་བ་ཞིག་འདུག་པ་ཆུང་མ་དང་ཡོངས་སུ་སྤྱོད་པ་ལས་ཁྱེའུ་གཉིས་བདོག་སྟེ། ཕུ་བོ༌[^204]ནི་སྡེ་པ། ནུ་བོ་ནི་ཉེ༌[^205]སྡེ་ཞེས་མིང་དུ་བཏགས་སོ། །

[Block 313]
དེ་ནས་དུས་གཞན་ཞིག་ན་སྡེ་པ་གཞན་དུ་ཚོང༌[^206]ལ་ཆས་པས་ནོར་མང་དུ་རྙེད་པས་དེ་ཆགས་ཏེ། ཡུན་རིང་དུ་མ་ལོག་གོ། །

[Block 314]
དེ་ནས་སྡེ་བའི་ཆུང་མ་འདོད་ཆགས་ཀྱིས་ཁོལ་བར་གྱུར་ནས་ཉེ་སྡེ་ལ་ལན་དུ་མ་ཞིག་བསྒུགས་པ༌[^207]ལས།

[Block 315]
ཉེ་སྡེས་ཀྱང༌[^208]ཕྱི་ཞིག་ན་སྤྱད་དེ་བུ་ཆགས་སོ། །

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
--- END BLOCKS ---
