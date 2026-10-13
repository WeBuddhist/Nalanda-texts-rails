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
ཞེས་པ་ནི་གསང་བའི་དུས་སུ་མཐོང་བའི་འདྲི་བ༌[^143]དང་མེ་ཏོག་དོར་བ་དང་། ཡེ་ཤེས་དབབ་པའི་སྦྱོར་བས་སྨྲ་བ་ལ་སོགས་པ་འབྱུང་བར་ཤེས་པར་བྱའོ། །

[Block 282]
འདིའི་དུས་ཀྱི་བརྡའང་གང་ཡིན་ཞེ་ན། སྦོམ་པོས་དབང་མོ་མནན་པ་ནི། ཟླ་བ་ཉི་མའི་སྦྱོར་བའོ། །ཞེས་པ་གང་གིས་སྦོམ་པོས་དབང་མོ་མནན་པ་ནི་གསང་བའི་དབང་གི་བརྡ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 283]
གཞན་མ་གཡས་ཀྱི་སྦྱོར་བས་གཡོན་པ་ལ་བྱེད་པས་ཡང་ལ་ལ་དག་འདོད་དོ། །

[Block 284]
དེའི་དུས་སུའང་བསམ་གཏན་ཇི་ལྟར་བྱ་ཞེ་ན། སློབ་དཔོན་རིག་མ་ལྟར༌[^144]བསྒོམ་དང་། གང་གིས་བདེ་སྟེར་བསམ་གཏན་ཡིན། །ཞེས་པ་གསང་བའི་དབང་བསྐུར་བའི་དུས་ཀྱི་བསམ་གཏན་ཡང་དང་པོར་སློབ་དཔོན་རིག་མ་དང་བཅས་པ་ཐབས་དང་ཤེས་རབ་ཀྱི་སྐུར་གནས་པར་བྱ་སྟེ། དེ་ལས་བྱང་ཆུབ་སེམས་ཀྱི་ཆུས་བཀང་བའི་བུམ་པ་ཐོགས་པ་བསམ་གྱིས་མི་ཁྱབ་པ་བྱུང་ནས་སློབ་མའི་ལྕེ༌[^145]ལ་དབང་བསྐུར་བར་བྱའོ། །

[Block 285]
འོ་ན་དེས་བག་ཆགས་སམ་དྲི་མ་གང་འཁྲུ་བར་བྱེད་ན།

[Block 286 [VERSE]]
ངག་གི་རྟོག་དང་དྲི་མར་བཅས། །
སྦྱོང་བར་བྱེད་པ་ནུས་པའོ། །

[Block 287]
ཞེས་པ་ཚིག་འཁྱལ་པ་ལ་སོགས་པའི་དྲི་མ་ཐམས་ཅད་གང་གིས་འཁྲུ་བར་ནུས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 288]
གསང་བའི་དབང་བསྐུར་བའི་སློབ་མ་དེ་ལའང་གང་གི་མན་ངག་བསྟན་པར་བྱ་ཞེ་ན།

[Block 289 [VERSE]]
སྤྲོས་བཅས་དང་ནི་སྤྲོས་མེད་དང་། །
ཤིན་ཏུ་སྤྲོས་མེད་དེ་ལ་བསྟན། །

[Block 290]
ཞེས་པ་སྦྱིན་པ༌[^146]ལ་སོགས་པ་དང་། གང་གིས༌[^147]བུད་མེད་བསྟེན་པ༌[^148]ལ་སོགས་པ་དུས་དང་བྱ་བ་དང་བསམ་པ་ལ་ལྟོས་པའི༌[^149]སྤྲོས་བཅས་དང་། སྤྲོས་མེད་དང་། ཤིན་ཏུ་སྤྲོས་པ་མེད་པའི་སྤྱོད་པའི་མན་ངག་བསྟན་པར་བྱའོ། །

[Block 291]
དེའང་ཚོགས་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན།

[Block 292 [VERSE]]
གསང་བའི་དབང་ནི་བསྐུར་བྱས་ནས། །
ཟབ་པ༌[^150]ཕྱི་ཡི་ཚོགས་རྣམས་བྱ། །

[Block 293]
ཞེས་པ་གང་གསང་བའི་དབང་ཐོབ་པ་དེ་དག་གིས་ནི་དང་བོར་བསྐྱེད་པའི་རིམ་པ༌[^151]ལ་སོགས་པའི་དུས་ནས་ཟབ་པ་ཕྱིའི་འཁོར་ལོ་བུད་མེད་ཉི་ཤུ་རྩ་ལྔ་ལ་སོགས་པ་ལ་བརྟེན་པར་བྱའོ། །

[Block 294]
འོ་ན་གསང་བའི་དབང་ཡང་དངོས་གྲུབ་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན། འདིར༌[^152]ཡང་།

[Block 295 [VERSE]]
ཐུན་མོང་ས་འོག་ལ་སོགས་པ། །
མྱུར་དུ་འགྲུབ་པར་བྱེད་པ་ཡིན། །

[Block 296]
ཞེས་པ་འདིའི་སྦྱོར་བས་ས་འོག་དང་རི་ལུ༌[^153]དང་བུད་མེད་ཀྱི་སྦྱོར་བ་ལ་བརྟེན་པ་ལས་བྱུང་བའི་བཅུད་ཀྱིས༌[^154]ལེན༌[^155]དང་། མངོན་ཤེས་ལ་སོགས་པ་མྱུར་དུ་འབྱུང་བར་འགྱུར་རོ། །

[Block 297]
འབྲས་བུའང་གང་ཡིན་ཞེ་ན།

[Block 298 [VERSE]]
གང་གིས་དེ་དང་དེ་ལས་གཞན། །
ཐོབ་པར་འགྱུར་བ་འབྲས་བུའོ། །

[Block 299]
ཞེས་པ་གང་གིས༌[^156]གང་ལ་བརྟེན་ནས་ཐུན་མོང་དང་མཆོག་གི་དངོས་གྲུབ་དངོས་སུ་དང་། བརྒྱུད༌[^157]ནས་འགྲུབ་པའམ་ཐོབ་པ་འདི་ནི་འབྲས་བུའོ། །

[Block 300]
ཡང་ན་འབྲས་བུ་ནི་མགྲིན་པར་སྣང་བ་མཐའ་ཡས་སུ་གྱུར་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 301]
འདི་དག་གིས་ནི་གསང་བའི་དབང་བསྐུར་བ་བསྟན་ཏོ། །

[Block 302]
[^158]

[Block 303]
དེ་ནས་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བཤད་པར་བྱ་སྟེ། འདིའི་ཡང༌[^159]ངོ་བོ་ཉིད་གང་ཡིན་ཞེ་ན། བཤད་པ།

[Block 304 [VERSE]]
བྱང་ཆུབ་སེམས་ཀྱི་བདེ་བ་ནི། །
གསུམ་པའི་དབང་གི་ངོ་བོའོ། །

[Block 305]
ཞེས་པ་རང་གི༌[^160]བྱང་ཆུབ་སེམས་ཀྱི་བདེ་བ་ཉམས་སུ་མྱོང་བ་འདི་ནི་ཤེས་རབ་ཡེ་ཤེས༌[^161]ཀྱི་ངོ་བོ་བཤད་དོ། །

[Block 306]
འདི་ལའང་ནུས་པ་ཞེས་པ་མ་སྨྲས་སམ་ཞེ་ན། འདི་ཉིད་ནི་ནུས་པ་ཞེས་བྱ་བ་ཁོ་ན་སྟེ། གོང་བཞིན་ནོ། །

[Block 307]
ཡེ་ཤེས་ཞེས་བྱ་བ་འདི་འང༌[^162]དུ་ཞེ་ན། ཕྱི་ནང་སྦས་པའི་བྱེ་བྲག་གིས། གསུམ་པའི་དབང་གིས་དབྱེ་བ་ཡིན། །ཞེས་པ་རིག་མ་གཏད་པ་ནི་ཕྱིའི་འོ། །

[Block 308]
དེ་ལ་བྱང་ཆུབ་སེམས་བསྐྱོད་པས་འབྱུང་བ་ནི་ནང་གིའོ། །

[Block 309]
དེ་བཟློག་པའི་སྟོབས་ཀྱིས༌[^163]འབྱུང་བ་ནི་སྦས་པའོ། །

[Block 310]
འདི་ལའང་ཅིའི་ཕྱིར་ཤེས་རབ་ཡེ་ཤེས་ཞེས་བྱ་ཞེ་ན།

[Block 311 [VERSE]]
ཤེས་རབ་ལ་བརྟེན་ཡེ་ཤེས་ཏེ། །
ཡེ་ཤེས་ཐོབ་པར་བྱེད༌[^164]ཕྱིར་རོ། །

[Block 312]
ཞེས་པ་ཡེ་ཤེས་བསྐྱེད་པའི་རྒྱུའི་ཕྱིར་དང་། ཡེ་ཤེས་དང་ཉེ་བ་ཉིད༌[^165]འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་ཏེ། གོ་རིམས་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 313]
རྣམ་གྲངས་ཀྱང་གང་དང་གང་ཡིན་ཞེ་ན།

[Block 314 [VERSE]]
ཤེས་རབ་ཡེ་ཤེས་བླ་ན་མེད། །
ཐབས་ཀྱི་དམ་པ་ཉེ་བའི་རྒྱུ། །

[Block 315]
ཞེས་པ་ཤེས་རབ་མ་ལ་བརྟེན་ནས་ཡེ་ཤེས་སྐྱེ་བ་ཉིད་དང་། གོང་ན་གཞན་མེད་པ་ཉིད་དང་། མཆོག་དམ་པ་ཉིད་འགྲུབ་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 316]
འོ་ན་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ཞེས་བྱ་བ་འདི་ཡང་ཆོས་དུ་དང་ལྡན་པ་ཡིན་ཞེ་ན།

[Block 317 [VERSE]]
ཤེས་རབ་ལ་བརྟེན་ཡེ་ཤེས་སྐྱེ། །
ཏིང་ངེ༌[^166]འཛིན་དམིགས་བདག་གིས་འཇུག །
བྱང་ཆུབ་སེམས་སྤྱོད་ཉེ་བའི་རྒྱུ། །

[Block 318]
ཞེས་པ་ཤེས་རབ་དམ་པ་བསྐྱེད་པ་ཉིད་དང་། ཡེ་ཤེས་དམ་པ་དང་། ཏིང་ངེ་འཛིན་དམ་པ་ལ་དམིགས་པ་ཉིད་དང་ཐབས་བདེན་པའི་རྣལ་འབྱོར་པ་བདག་ཉིད་ཀྱི་འཇུག་པ་དང་། ཞུ་བ་བྱང་ཆུབ་སེམས་ལ་སྤྱོད་པ་དང་། [^167]དེའང་ཉེ་བའི་རྒྱུར་འདུག་པ༌[^168]སྟེ། འདི་ལྟར་དྲུག་དང་ལྡན་པ་ཁོ་ན་ཡིན་ནོ་ཞེའོ། །

[Block 319]
འོ་ན་དེ་སྨོས་པས་ཅི་བྱེད་ན།

[Block 320 [VERSE]]
བུམ་པ་དང་ནི་གསང་བ་དང་། །
ཐོབ་བྱ་བཞི་པ་སེལ་བར་བྱེད། །
--- END BLOCKS ---
