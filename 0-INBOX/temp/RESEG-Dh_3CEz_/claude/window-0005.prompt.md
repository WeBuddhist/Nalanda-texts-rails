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
[Block 176]
བསྐྱེད་པ་ལ་གཉིས་ཏེ། སོ་སོར་དམིགས་པ་དང་སྤྱིར་དམིགས་པའོ། །

[Block 177 [HEADING]]
###### **སྤྱིར་དམིགས་པ།** ^1-1-5-1-1-2-0

[Block 178]
སྤྱིར་དམིགས་པ་ནི་ལྟ་སྟངས་དང་ཞེས་པ་ནས་རྣམ་མང་བརྗོད་པར་བྱ་བའི་བར་ཏེ་བརྡ་ནི་དམིགས་པ་སྟེ། དབུགས་དང་སྔགས་དང་ལྷའི་རྣལ་འབྱོར་རོ། །རེངས་པ་ལ་སོགས་པ་སྟེ། ལས་རྣམ་བཞིའོ། །འོ་ན་བདེ་ཆེན་ནི་རྫོགས་རིམ་ཡིན་ན། བསྐྱེད་རིམ་དུ་འཆད་པ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ལྷའི་རྣལ་འབྱོར་དང་ལྡན་པས་སོ། །ཇི་ལྟར་རིགས་པ་རྣལ་འབྱོར་མ་འོག་ནས་ལས་དང་སྔགས་དང་རྣལ་འབྱོར་སོ་སོར་འཆད་དོ། །དེ་ཡང་ཅིས་ཐོབ༌[^128]ན། བསྐྱེད་དང་ཞེས་པ་ནི་ཚོགས་བསགས་པའོ། །གནས་དང་ཞེས་པ་ནི་རྟེན་གྱི་དཀྱིལ་འཁོར་རོ། །བྱེད་རྒྱུ་ནི་མངོན་པར་བྱང་ཆུབ་པ་ལྔའོ། །

[Block 179 [HEADING]]
###### **སོ་སོར་དམིགས་པ།** ^1-1-5-1-1-1-0

[Block 180]
སོ་སོར་དམིགས་པ་རེངས་པ་ལ་སོགས་པ་ནི་ཇི་ལྟར་རིགས་པ་རྣལ་འབྱོར་རྣམས་ཀྱིས་སོ། །

[Block 181 [HEADING]]
###### རྫོགས་པའི་རིམ་པའི་དམིགས་པ། ^1-1-5-1-2-0

[Block 182]
རྫོགས་པའི་རིམ་པའི་དམིགས་པ་ནི་གཞན་གྱི་དོན་བྱེད་པ་དང་རྣམ་ཤེས་ཡེ་ཤེས་སུ་གྲུབ་པ་དང་ལུས་ལྷ་རྣམས་སུ་སྣང་བ་རང་ལོག་ཏུ་འགྱུར་བ་སྟེ།

[Block 183]
དེ་སྐད་དུ།

[Block 184 [VERSE]]
མཚོན་བྱ་མཚོན་བྱེད་མཚན་ཉིད་ནི། །
རྣམ་ཤེས་ཀྱིས་ནི་ཡེ་ཤེས་བསམ། །
ཡེ་ཤེས་ཀྱིས་ནི་ཤེས་བྱ་བལྟ། །
ཤེས་བྱས་འགྲོ་བ་བརྟག་པར་བྱ། །

[Block 185]
ཞེས་གསུངས་སོ། །

[Block 186 [HEADING]]
##### ཉམས་སུ་བླང་པའི་ཐབས། ^1-1-5-2-0

[Block 187]
དེ་ཉམས་སུ་བླང་པའི་ཐབས་ནི་ལམ་གཉིས་ལས་གོ་རིམས་ངེས་པའི་རྒྱུ་མཚན་དང་། ཧེ་རུ་ཀ་ནི་ཞེས་ཚིག་རྐང་གཉིས་གསུངས་སོ། །

[Block 188 [HEADING]]
###### བསྐྱེད་པའི་རྒྱུ། ^1-1-5-2-1-0

[Block 189]
བསྐྱེད་པའི་རྒྱུ་ནི་གཉིས་ཏེ་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 190 [HEADING]]
###### **དང་པོ་བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-1-0

[Block 191]
དེ་ལ་དང་པོ་གཅིག་ནི་བསྐྱེད་པའི་རིམ་པ་སྟེ།

[Block 192 [VERSE]]
སེམས་ཅན་ལས་ཀྱི་དང་པོ་ལ། །
ལས་རྣམས་ཐམས་ཅད་བསྒྲུབ་པའི་ཕྱིར། །
ལྷ་ཡི་རྣལ་འབྱོར་རིམ་པ་ཞིག །
རྒྱུད་ལས་དང་པོར་གསུངས་པ་ཡིན། །

[Block 193]
ཞེས་གསུངས་སོ། །

[Block 194]
དེ་ནས་བསྐྱེད་པའི་རིམ་པ་ལ་སྡུད་པ་པོ་ཐེ་ཚོམ་དུ་གྱུར་པ་ཁོང་ནས་དྲང་བ་ཡང་བསྐྱེད་རིམ་དངོས་པོས་མི་གྲོལ་ལོ་ཞེ་ན། དེའི་ལན་ཡོན་ཏན་གྱི་མིང་གིས་བོས་ཏེ། དངོས་པོ་ལ་གྲོལ་བ༌[^129]ཡང་ཡོད་འཆིང་བ་ཡང་ཡོད་དེ་ཤེས་རབ༌[^130]དང་མ་ཤེས་པའི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 195]
འོ་ན་དངོས་པོ་མེད་པས་གྲོལ་ལམ་ཞེ་ན་དེ་ཡང་མ་ཡིན་ཏེ། ཤེས་པ་དང་མ་ཤེས་པའི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །དེས་ན་བསྐྱེད་པའི་རིམ་པ་ལ་ཐབས་དང་ཤེས་རབ་མིང༌[^131]དུ་ཤེས་པ་དང་རྨི་ལམ་དང་སྒྱུ་མ་དང་དྲི་ཟའི་གྲོང་ཁྱེར་ལྟ་བུར་ཤེས་པ་སྟེ། དེ་ལྟར་ཧེ་རུ་ཀ་བསྒོམ་བྱ། །ཞེས་པའོ། །དེ་བཞིན་དུ་དངོས་པོ་མེད་པས་ཀྱང་འཆིང་བར་འགྱུར་ཏེ། གྲོལ་བར་ཡང་འགྱུར་རོ། །དངོས་མེད་ལ་ཞེན་ན་ཆད་པའི་ལྟ་བ་སྟེ།

[Block 196 [VERSE]]
མར་མེ་འབར་བ་གསད༌[^132]རུང་གི། །
ཤི་ནས་ཅི་ཡང་བྱ་རུང་མེད། །

[Block 197]
གསུངས་པ་དང་ཡང་།

[Block 198 [VERSE]]
རྒྱུ་དང་འདྲ་བའི་འབྲས་བུ་ནི། །
ཀུན་དུ་མཐོང་བ་མ་ཡིན་ནམ། །

[Block 199]
ཞེས་བྱ་བ་དང་།

[Block 200 [VERSE]]
ལྟ་བ་རྣམ་པར་ལོག༌[^133]རྣམས་དང་། །
བདག་ཏུ་ལྟ་བ་བཟློག་པའི་ཕྱིར། །
སྟོང་པ་རྒྱལ་བ་རྣམས་ཀྱིས་གསུངས། །

[Block 201]
ཞེས་པས་དངོས་པོ་སྒྱུ་མ་ཙམ་རང་སྣང་གི་སེམས་སུ་བྱ་སྟེ། དེ་ལྟར་ཧེ་རུ་ཀ་བསྒོམ་བྱའོ། །

[Block 202]
སྤྱིར་ཀུན་བརྟགས་ཆོས་ལ་ལམ་དུ་བྱེད་པ་དང་། གཞན་དབང་ལུས་ལ་ལམ་དུ་བྱེད་པ་དང་། ཡོངས་གྲུབ་སེམས་ལ་ལམ་དུ་བྱེད་པའོ། །དེ་ཉིད་དམན་པ་དང་མཆོག་གི་ཤེས་པར་བྱ་སྟེ། ཀུན་བརྟགས་མེད་པ་ལ་ཡོད་པར་བློས་བརྟགས་པ་དང་། གཞན་དབང་དེའི་རྒྱུ་མཚན་རྟོགས་པའི་ཤེས་པ། ཡོངས་སུ་གྲུབ་པ༌[^134]དེ་ཉིད་གཟུང་འཛིན་དང་བྲལ་བ་སྟེ། དམན་པའི་རྣམ་པ་གསུམ་ཞེས་བྱའོ། །

[Block 203]
མཆོག་གི་གསུམ་ནི་སྤྱིར་ལྷའི་འཁོར་ལོ་རུ་བརྟགས་པས༌[^135]ཀུན་བརྟགས། ལུས་རྩ་དང་འཁོར་ལོར་སྣང་བ་དེ་གཞན་དབང་། ཡེ་ཤེས་བདེ་བ་ཆེན་པོ་ཡོངས་སུ་གྲུབ་པའོ། །དེ་ལ་དང་པོ་ལ་གསུམ་སྟེ། ཀུན་བརྟགས་ཀྱི་ཀུན་བརྟགས་ས་བོན་དང་མཚན་མས་བསྐྱེད་པའི་རང་རྒྱུད་དུ་རྟོགས་པ་དང་། གཞན་དབང་ཡེ་ཤེས་ཀྱི་སྣང་བར་བྱས་པ་དང་། ཡོངས་གྲུབ་བདེ་བ་ཆེན་པོས་བྱིན་གྱིས་བརླབས་པའོ། །

[Block 204]
གཞན་དབང་གི་གསུམ་ནི་ཀུན་བརྟགས་ནི་རྩ་ཕལ་པའམ་འཁོར་ལོ་གསུམ་མོ། །རྩ་གསུམ་དང་རྩ་གཅིག་ནི་གཞན་དབང་གི་གཞན༌[^136]དབང་ངོ་། །རྩ་ཨ་ཝ་དྷཱུ་ཏཱིའམ་མཆོག་གི་དབང་པོ་ནི་གཞན་དབང་གི་ཡོངས་གྲུབ་བོ། །ཡང་ན་ཤེས་རབ་ཀྱི་རྩ་ཀུན་བརྟགས། ཐབས་ཀྱི་རྩ༌[^137]གཞན་དབང་། དབྱེར་མེད་ཡོངས་གྲུབ་བོ། །དེ་རྣམས་ཀུན་རྫོབ་རྣམ་པར་གཞག་པའོ། །

[Block 205]
ཡང་བསྐྱེད་རིམ་དང་རྫོགས་རིམ་དང་། ཡོངས་སུ༌[^138]རྫོགས་པའི་རིམ་པའོ། །ཡོངས་གྲུབ་ཀྱི་ཀུན་བརྟགས་ནི་མཚོན་བྱ་ཀུན་རྫོབ། གཞན་དབང་གི་མཚོན་བྱ་དོན་དམ། ཡོངས་གྲུབ་ནི་དབྱེར་མེད་དོ། །ཡང་ན་སྟོང་པ་ཉིད་ཀུན་བརྟགས། རིག་པ་གསལ་བ་གཞན་དབང་། དེ་གཉིས་དབྱེར་མེད་ཡོངས་གྲུབ་བོ། །

[Block 206]
དེ་རྣམས་ཉམས་སུ་བླང་བ་ནི། དེ་ཉིད་ངེས་པར་བྱ་སྟེ། ཆོས་ལ་ལམ་དུ་བྱེད་པ་བསྐྱེད་རིམ་ལྷའི་རྣལ་འབྱོར་སྒྲུབ་ཐབས་བཞིན་དུ༌[^139]ལེའུ་གསུམ་པ་དང་། བརྟག༌[^140]པ་ཕྱི་མའི་ལེའུ་ལྔ་པ་ལྟར་བྱ་བ་དང་ལུས་ལ་ལམ་དུ་བྱེད་པ་དང་། གཞན་ལུས་དང་རང་ལུས་ཏེ། །རྩ་དང་བྱང་ཆུབ་སེམས་གཟུང་བ་ལ་སོགས་པ་དགའ་བ་བཞི་བསྒོམ་པ་སྟེ་ལེའུ་དང་པོ་དང་བརྒྱད་པ་དང་བརྟག་པ་ཕྱི་མའི་ལེའུ་གཉིས་པ་དང་ལྔ་པ་ལས་འབྱུང་བ་བསྒོམ་མོ། །སེམས་ལ་ལམ་དུ་བྱེད་པ་སེམས་ལ་བསླབ་པ་སྟེ། ཐབས་དུ་མས་བསླབ་པའོ། །ལམ་གཉིས་ཏེ་བསྐྱེད་རིམ་མང་བར་བྱ་སྟེ་རྫོགས་རིམ་ཉུང་ལྡན་སྒྲུབ་ཐབས་བཞིན་སྒོམ་པ་དང་རྫོགས་པའི་རིམ་པ་མང་ལྡན་བསྐྱེད་རིམ་ཉུང་ལྡན་ཏེ་མོས་པའི་རྣལ་འབྱོར་ལ་སོགས་པའམ་ཡན་ལག་བཞི་བསྒོམ་པའོ། །

[Block 207 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-0

[Block 208]
རྫོགས་པའི་རིམ་པ་ལ་བཞི་སྟེ། ངོ་བོ་ཡེ་ཤེས་ཆེན་པོ་བསྟན་པ་དང་རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ་དང་། ལྡན་པའི་ཆོས་སྡོམ་པའི་དབྱེ་བ་དང་། ཉམས་སུ་ལེན་པ་རླུང་ལ་བསླབ་པ་དང་གཏུམ་མོ་སྦར་བའོ། །

[Block 209 [HEADING]]
###### **ངོ་བོ་ཡེ་ཤེས་ཆེན་པོ་བསྟན་པ།** ^1-1-5-2-1-2-1-0

[Block 210]
ཡེ་ཤེས་ཆེན་པོའི་རང་བཞིན་ལ་ཤེས་པར་བྱ་བ་དང་། སྒོམ་པ་ཉམས་སུ་ལེན་པའོ། །

[Block 211 [HEADING]]
###### **བསླབ་པ་ཤེས་པར་བྱ་བ།** ^1-1-5-2-1-2-1-1-0

[Block 212]
བསླབ་པ་ཤེས་པར་བྱ་བ་ལ་གཉིས་ཏེ། དེ་ཁོ་ན་ཉིད་བཤད་པ་དང་།

[Block 213 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་བཤད་པ།** ^1-1-5-2-1-2-1-1-1-0

[Block 214 [HEADING]]
###### **ཡེ་ཤེས།** ^1-1-5-2-1-2-1-1-1-1-0

[Block 215]
རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བའོ། །དེ་ཁོ་ན་ཉིད་ལ་གཉིས་ཏེ།ཡེ་ཤེས་དང་ཆོས་ཉིད་དོ། །ཡེ་ཤེས་ལ་ཡང་གཉིས་ཏེ།
--- END BLOCKS ---
