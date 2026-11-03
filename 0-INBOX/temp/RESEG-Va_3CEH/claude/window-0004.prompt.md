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
[Block 141]
བློ་གྲོས་ཡངས་པ་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནང་གི་སོ་སོ་རང་གི་ལེན་པ་མི་མཐོང་། ལེན་པའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ལ། དེ་ཡང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡིན་པ་དང་། ཀུན་གཞི་ཡང་མི་མཐོང་། ཀུན་གཞིའི༌[^90]རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། བསགས་པ་ཡང་མི་མཐོང་། སེམས་ཀྱང་མི་མཐོང་། མིག་ཀྱང་མི་མཐོང་། གཟུགས་ཀྱང་མི་མཐོང་། མིག་གི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། རྣ་བ༌[^91]ཡང་མི་མཐོང་། སྒྲ་ཡང་མི་མཐོང་། རྣ་བའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། སྣ་ཡང་མི་མཐོང་། དྲི་ཡང་མི་མཐོང་། སྣའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། ལྕེ་ཡང་མི་མཐོང་། རོ་ཡང་མི་མཐོང་། ལྕེའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། ལུས་ཀྱང་མི་མཐོང་། རེག་བྱ་ཡང་མི་མཐོང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ཞིང་། བློ་གྲོས་ཡངས་པ་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནང་གི་སོ་སོ་རང་གི་ཡིད་ཀྱང་མི་མཐོང་། ཆོས་རྣམས་ཀྱང་མི་མཐོང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ལ། དེ་ཡང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡིན་ན། དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པ་ལ་མཁས་པ་ཞེས་བྱ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པ་ལ་མཁས་པ་ནི་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཡིན་པར་འདོགས་སོ། །

[Block 142]
བློ་གྲོས་ཡངས་པ་དེ་ཙམ་གྱིས་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཡིན་ལ། དེ་བཞིན་གཤེགས་པ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པར་འདོགས་ན་ཡང་དེ་ཙམ་གྱིས་འདོགས་སོ་ཞེས་བྱ་བ་དང་། ཡང་དོན་འདི་ཉིད་ཚིགས་སུ་བཅད་པ། ལེན་པའི་རྣམ་པར་ཤེས་པ་ཟབ་ཅིང་ཕྲ།[^92] །ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ་རྟོགས་པར་དཀའ་བའི་ཕྱིར་རོ། །

[Block 143]
ས་བོན་ཐམས་ཅད་ཆུ་བོའི་རྒྱུན་བཞིན་འབབ། །ཅེས་བྱ་བ་ནི་རིམ་གྱིས་འཇུག་པ་ཉིད་ཀྱིས་དེར་ས་བོན་ཐམས་ཅད་ཆུ་བོའི་རྒྱུན་བཞིན་དུ་སྐད་ཅིག་མའི༌[^93]རིམ་གྱིས་འཇུག་པས་སོ། །

[Block 144]
ལེན་པའི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་མིང་གི་རྣམ་གྲངས་དང་། ངེས་པའི་ཚིག་གོ། །

[Block 145]
བདག་ཏུ་རྟོག་པར་གྱུར་ན་མི་རུང་ཞེས་བྱ་བ་ནི་རྣམ་པ་གཅིག་ཏུ་ཞུགས་པ་ཉིད་ལ་བདག་ཏུ་རྟོག་པར་མ་བྱེད་ཅིག་པའོ། །

[Block 146]
དབང་པོ་གཟུགས་ཅན་ཐམས་ཅད་ཀྱི་རྒྱུ་ཡིན་པ་ཞེས་བྱ་བའི་བཤད་པ་ནི་འདི་ལྟར་ཚེ་ཇི་སྲིད་པར་རྗེས་སུ་འཇུག་གི་བར་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་མིག་ལ་སོགས་པའི་དབང་པོ་གཟུགས་ཅན་རྣམས་ཀུན་གཞི་རྣམ་པར་ཤེས་པས་མ་བཟུང་ན་ཤི་བའི་ལུས་བཞིན་དུ་སྔོན་པོ་ལ་སོགས་པའི་གནས་སྐབས་སུ་འགྱུར་བས་གང་ཡང་ཤི་བའི་དུས་ན་དེ་དང་བྲལ་བར་གྱུར་པ་ན་འདི་དག་ཀྱང་སྔོན་པོ་ལ་སོགས་པའི་གནས་སྐབས་སུ་འགྱུར་རོ། །

[Block 147]
དེས་ན་འདི་ལྟར་གཟུང་བར༌[^94]བྱ་སྟེ། ཇི་སྲིད་དེས་བཟུང་བའི་བར་དུ་ཚེ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 148]
ལུས་ཐམས་ཅད་ཉེ་བར་ལེན་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར་ན་ཡང་ལེན་པ་སྟེ། འདིའི༌[^95]བཤད་པ་ནི། ཉིང་མཚམས་སྦྱོར་བ་སྦྲེལ་བ་ན༌[^96]ཡང་དེ་དག་མངོན་པར་འགྲུབ་པར༌[^97]ཉེ་བར་འཛིན་པ་ཞེས་བྱ་བ་འདིས་བཤད་པ་ཡིན་ནོ། །

[Block 149]
གང་གི་ཕྱིར་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་པ་དེས་ན་ཡང་ཉིང་མཚམས་སྦྱོར་ཞིང་སྦྲེལ་བ་མངོན་པར་གྲུབ་པ༌[^98]འཛིན་པར་བྱེད་པས་ལུས་ཐམས་ཅད་ཡོངས་སུ་གཟུང་བ༌[^99]བྱས་པས༌[^100]འགྱུར་ཏེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་ལུས་ཐམས་ཅད་ཀྱི་བག་ཆགས་ཀུན་ཏུ་གནས་པའི་ཕྱིར་རོ། །

[Block 150]
དེ་དག་མངོན་པར་གྲུབ་པ༌[^101]སྟེ། དེའི་མངོན་པར་འགྲུབ་པ་ནི་དེ་མངོན་པར་འགྲུབ་པའོ། །

[Block 151]
ཉེ་བར་འཛིན་པ་ནི་དེ་དག་མངོན་པར་འགྲུབ་པ་ཉེ་བར་ལེན་ཏེ། དེའི་ཉེ་བར་འཛིན་པ་ཡང་བདག་གི་དངོས་པོ་བསྐྱེད་པར༌[^102]འགྱུར་བའོ། །

[Block 152]
དོན་འདིས་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལེན་པའི་རྣམ་པར་ཤེས་པ་ཉིད་དུ་ཡང་བརྗོད་པ་ཡིན་ནོ། །

[Block 153 [HEADING]]
#### སེམས། ^1-3-3-0

[Block 154]
ཡང་དེ་ནི་སེམས་ཞེས་ཀྱང་བྱ་སྟེ། ཞེས་བྱ་བའི་སེམས་ཉིད་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་སྟེ། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དོན་སྣ་ཚོགས་ཉིད་དུ་དམིགས་པ་ལྟར་འདིའི་དོན་ཡང་སྣ་ཚོགས་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་འདིས་བསྟན་ཏོ། །

[Block 155]
དེ་ལ་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་ཤེས་པ་གང་དེ་མ་ཐག་པར་འགགས་པ་ཉིད་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་རྒྱུར་འགྱུར་བས་དེ་ནི་ཡིད་གཅིག་གོ། །

[Block 156]
གཉིས་པ་ནི་ཉོན་མོངས་པ་བཞིས་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དེ། དེ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བ་སྟེ། བདག་ཉིད་དུ་མངོན་པར་ཞེན་པ༌[^103]དང་། གང་གི་དབང་གིས༌[^104]ངའོ་སྙམ་དུ་ང་རྒྱལ་ཏེ། བདག་ཉིད་མཐོའོ་ཞེས་པ་དང་། ཡང་དེ་ལ་མི་བདེན་པའི་བདག་ལ་སྲེད་པའི་བདག་ཉིད༌[^105]ལ་ཆགས་པ་དང་། གསུམ་པོ་དེ་དག་གི་རྒྱུ་མ་རིག་པ་སྟེ། མ་རིག་པ༌[^106]མི་ཤེས་པའོ། །

[Block 157]
གང་གནས་གཅིག་པོས་ནི་བསྐྱེད་པ། [^107]གཉིས་པོས༌[^108]ནི་ཉོན་མོངས་པ་ཅན་དུ་བྱས་པ་སྟེ་ཞེས་བྱ་བ་དེ་ལ་འགགས་མ་ཐག་པའི་རྣམ་པར་ཤེས་པ་ཡིད་ཅེས་བརྗོད་པས་ནི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་འབྱུང་བའི་སྐབས་སྦྱིན་པས་སྐྱེ་བའི་རྟེན་ཡིན་ནོ། །

[Block 158]
གཉིས་པ་ཉོན་མོངས་པ་ཅན་ནི་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་པ་སྟེ། གང༌[^109]ཕྱིར་དགེ་བའི་སེམས་ལ་ཡང་བདག་གོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 159]
ཡུལ་ལ་རྣམ་པར་རིག་པའི་ཕྱིར་རྣམ་པར་ཤེས་པའོ། །

[Block 160]
དེ་མ་ཐག་པའི་རྟེན་བྱེད་པ་དང་། ངར་སེམས་པའི་ཕྱིར་ཡིད་ཀྱི༌[^110]རྣམ་པ་གཉིས་སོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཡུལ་ལ་འཛིན་པའི་དོན་གྱིས་ན་རྣམ་པར་ཤེས་པ་ནི་སྐབས་སྟེར་བའི་དོན་གྱིས་ནི་ཡིད་གཅིག་གོ། །

[Block 161]
བདག་ཏུ་ང་རྒྱལ་ལ་སོགས་པས་ཀུན་ནས་ཉོན་མོངས་པའི་དོན་གྱིས་ན་གཉིས་པ་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དོ། །

[Block 162]
གཞན་ཡང་གང་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དེ་མེད་ན། གང་གི་རྒྱུ་ཅན་ཡིད་དང་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ཡང་འཇུག་པར་མི་འགྱུར་རོ་ཞེས་བལྟ་བར་བྱའོ། །

[Block 163]
རྣམ་པར་ཤེས་པ་སྨོས་པས་ཡིད་ཀྱི༌[^111]

[Block 164]
གཉིས་པ་ཡང་སྨོས་པ་ཉིད་དུ་འགྱུར་ཏེ། རྒྱུ་གང་གིས་ཡིད་གང་འགགས་པ་དེ་ཉིད་ཡིད་ཅེས་བརྗོད་ན༌[^112]ཐོབ་པའི་ཕྱིར་རོ། །

[Block 165]
ཡང་འདིའི་ངེས་པའི་ཚིག་ནི་རྣམ་པ་སྣ་ཚོགས་ཀྱི་ཆོས་ཀྱི༌[^113]བག་ཆགས་ཀྱི་ས་བོན་གྱིས་གང་ཞིང་ཉེ་བར་ལེན་པའི་ཕྱིར་རོ། །

[Block 166]
དེ་ལ་རྣམ་པ་སྣ་ཚོགས་ནི་རྣམ་པ་ཐ་དད་པའོ། །

[Block 167]
ཆོས་ཀྱི་བག་ཆགས་ཀྱི་ས་བོན་ཞེས་བྱ་བ་ནི་རྒྱུ་གང་གིས་ནུས་པའི་ཁྱད་པར་རོ། །

[Block 168]
གང་ཞིང་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་གང་ཞིང་བསགས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཤེས་བྱ་ཕྲ་མོ་ཀུན་ཏུ་བསྡུས་པའི་ཕྱིར་ཏེ་ཞེས་བྱ་བ་ནི་དེ་ཕྲ་མོ་ཡང་ཡིན་ལ་ཤེས་བྱ་ཡང་ཡིན་པས་ཤེས་བྱ་ཕྲ་མོ་སྟེ། ཤེས་བྱ་ཕྲ་མོའི་ཁོངས་སུ་གཏོགས་པའམ། རྟོགས་པར༌[^114]དཀའ་བའི་ཕྱིར་རོ། །

[Block 169]
ཉན་ཐོས་ནི་ཤེས་བྱ་ཐམས་ཅད་ཤེས་པའི་དོན་དུ་སྤྲོ་བ་མེད་ཀྱི། བདག་གི་དོན་འབའ་ཞིག་གི་རྒྱུར་དེ་དག་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རགས་པ་ཉིད་སྡུག་བསྔལ་ལ་སོགས་པ་ཤེས་པས་སྤོང་ངོ་། །བྱང་ཆུབ་སེམས་དཔའ་ནི་བདག་དང་གཞན་རྣམས་ཀྱིའོ། །

[Block 170]
ཡང་དེ་ལྟར་གྲགས་པ་དེ་སྒྲུབ་པ་གང་ཡིན་ཞེ་ན། དེ་མེད་དུ་ཟིན་ན་མ་རིག་པ་མ་འདྲེས་པ་མེད་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 171]
ཡང་མ་འདྲེས་པའི་མ་རིག་པ་གང་ཞེ་ན། གཉེན་པོ་མ་སྐྱེས་པ་ན་དེ་ཁོ་ན་ཉིད་ཤེས་པ་ལ་སྒྲིབ་པར་བྱེད་པ་སྟེ། དེ་ཡང་རྣམ་པར་ཤེས་པ་ལྔ་ལ་ནི་ལྡན་པ་མ་ཡིན་ཏེ། དེ་ལ་གནས་པ་ལ་མི་སྒྲིབ་པའི་ཕྱིར་གང་ན་གཉེན་པོ་འབྱུང་བ་ཡོད་པ་དེ་ནི༌[^115]མི་མཐུན་པའི་ཕྱོགས་ཀྱང་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བས་སོ། །

[Block 172]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་ལ་ཡང་མེད་དེ། ཉོན་མོངས་པ་ཅན་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 173]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་གཞན་དུ་ཉོན་མོངས་པ་དང་། ཀུན་ཏུ་སྤྱོད་པར་མི་འགྲུབ་པོ། །དེ་ལྟ་ན་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཅན་དུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཁས་ལེན་ན་ཤིན་ཏུ་ཉོན་མོངས་པ་ཅན་ཉིད་དུ་ཐལ་བར་འགྱུར་བས་ཇི་ལྟར་སྦྱིན་པ་ལ་སོགས་པ་དགེ་བའི་སེམས་འབྱུང་བར་འགྱུར། དེ་དང་མཚུངས་པར་ལྡན་པ་ལས་ཏེ། ཡང་གང་དགེ་བ་དང་མཚུངས་པར་འཇུག་པའི་ཡིད་ཡོད་པས་དེ་ལ་དེ་མཚུངས་པར་ལྡན་པར་འགྱུར་གྱི་ཡང་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ལ་ནི་གཉེན་པོའི་ཕྱོགས་འདྲེན་པར་མི་རིགས་སོ། །

[Block 174]
ཡང་གང་ལ་ཉོན་མོངས་པ་ཙམ་གྱི་ཡིད་དང་མཚུངས་པར་འཇུག་པ་དགེ་བའི་སེམས་ཡོད་ན། དེ་དང༌[^116]དེས་དྲངས་པའི་གཉེན་པོའི་ཕྱོགས་སྐྱེས་པ་ན་ཅིག་ཤོས་འགག་པ་ཡིན་པས་འདི་ལ་སྐྱོན་མེད་དོ། །

[Block 175]
ལྔ་པོ་དག་དང་ཆོས་མཚུངས་དང་སྟེ། ཇི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ལྔ་པོ་དག་ལ་མིག་ལ་སོགས་པ་ལྔ་པོ་དག་རྟེན་མཚུངས་པར་ཡོད་པ་དེ་བཞིན་དུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ལ་ཡང་དེ་དང་མཚུངས་པར་འགྱུར་བའི་རྟེན་ཡོད་པ་ཡིན་ནོ། །

[Block 176]
སྙོམས་པར་འཇུག་པའི་བྱེ་བྲག་དང་སྟེ། གང་ལ་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཡོད་པ་དེ་ནི་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྟེ་དེ་ཡོད་པས་སོ། །

[Block 177]
གཞན་ལ་ནི་དེ་མེད་དེ། དེ་ནི་ཁྱད་པར་ཡིན་ནོ། །

[Block 178]
གཞན་དུ་ན་གཉི་ག་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཀུན་ཏུ་རྒྱུ་བ་མེད་ན་བྱེ་བྲག་མེད་པར་འགྱུར་རོ། །

[Block 179]
ངེས་ཚིག་མེད་པའི་སྐྱོན་དུ་འགྱུར། གང་འདི་སྐད་དུ་ངར་འཛིན་པས་ན་ཡིད་ཅེས་བྱ་བའི་ངེས་པའི་ཚིག་དེ་སྐད་དུ་བརྗོད་པའི་གཞི་གང་ཡིན། རྣམ་པར་ཤེས་པ་དྲུག་པོ་འགགས་མ་ཐག་པའི་རྣམ་པར་ཤེས་པ་ལ་ནི་འདི་ལྟར་མི་བརྗོད་དེ་འགགས་པའི་ཕྱིར་རོ། །

[Block 180]
འདུ་ཤེས་མེད་པའི་སྐྱེ་བའི་རྒྱུན་ཐོབ་པ་ན་ངར་འཛིན་པ་མེད་པའི་སྐྱོན་དུ་འགྱུར་ཏེ། འདི་ལྟར་དེའི་དུས་སྐབས་ན་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་མེད་ན་ངར་འཛིན་པ་མེད་པར་སྐྱེ་བར༌[^117]འགྱུར་རོ། །
--- END BLOCKS ---
