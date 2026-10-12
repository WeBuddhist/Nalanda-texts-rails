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
[Block 76]
ཞེས་བྱ་བའོ།

[Block 77]
[^22] །ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ནི་རྣམ་པར་ཤེས་པ་གཞན་དག་གི༌[^23]རྐྱེན་ཡིན་པས་རྐྱེན་གྱི་རྣམ་པར་ཤེས་པའོ། །

[Block 78]
དེ་ལས་བྱུང་བ་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ནི་ཉེ་བར་སྤྱོད་པ་ཅན་ནོ། །

[Block 79]
ཉེ་བར་སྤྱོད་པ་ནི༌[^24]ཚོར་བའོ། །

[Block 80]
ཡོངས་སུ་སྤྱོད་པ་ནི་འདུ་ཤེས་སོ། །

[Block 81]
རྣམ་པར་ཤེས་པ་འཇུག་པར་བྱེད་པ་དག་ནི་འདུ་བྱེད་རྣམས་ཏེ། སེམས་པ་དང་ཡིད་ལ་བྱེད་པ་ལ་སོགས་པའོ། །

[Block 82 [HEADING]]
#### ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད། ^1-1-9-0

[Block 83]
ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་ཀྱང་སྟོན་ཏེ།

[Block 84 [VERSE]]
སྒྲིབ་པའི་ཕྱིར་དང་འདེབས་པའི་ཕྱིར། །
ཁྲིད་པའི་ཕྱིར་དང་ཀུན་འཛིན་ཕྱིར། །
རྫོགས་བྱེད་ཕྱིར་དང་གསུམ་གཅོད་ཕྱིར། །
ཉེ་བར་གཅོད༌[^25]ཕྱིར་སྡུད་པའི་ཕྱིར། །

[Block 85 [VERSE]]
སྦྱོར་བའི་ཕྱིར་དང་མངོན་དུའི་ཕྱིར། །
སྡུག་བསྔལ་ཕྱིར་ནི༌[^26]འགྲོ་ཉོན་མོངས། །
རྣམ་གསུམ་རྣམ་གཉིས་ཀྱང་ཉོན་མོངས། །
རྣམ་བདུན་ཡང་དག་མིན༌[^27]རྟོག་ལས། །

[Block 86]
ཞེས་བྱ་བའོ། །

[Block 87]
དེ་ལ་སྒྲིབ་པའི་ཕྱིར་ནི་མ་རིག་པས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བ་ལ་བགེགས་བྱེད་པའི་ཕྱིར་རོ། །

[Block 88]
འདེབས་པའི་ཕྱིར་ནི་འདུ་བྱེད་རྣམས་ཀྱིས་རྣམ་པར་ཤེས་པ་ལ་ལས་ཀྱི་བག་ཆགས་འཇོག་པའི་ཕྱིར་རོ། །

[Block 89]
ཁྲིད་པའི་ཕྱིར་ནི་རྣམ་པར་ཤེས་པས་སྐྱེ་བའི་གནས་སུ་ཕྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 90]
ཀུན་འཛིན་ཕྱིར་ནི་མིང་དང་གཟུགས་ཀྱི་ལུས་སོ། །

[Block 91]
རྫོགས་བྱེད་ཕྱིར་ནི་སྐྱེ་མཆེད་དྲུག་གིས་སོ། །

[Block 92]
གསུམ་གཅོད་ཕྱིར་ནི་རེག་པས་སོ། །

[Block 93]
ཉེ་བར་སྤྱོད་པའི་ཕྱིར་ནི་ཚོར་བས་སོ། །

[Block 94]
སྡུད་པའི་ཕྱིར་ནི་ལས་ཀྱིས་བཏབ་པའི་ཡང་སྲིད་པ་སྲེད་པས་སོ། །

[Block 95]
སྦྱོར་བའི་ཕྱིར་ནི་ལེན་པ་རྣམས་ཀྱིས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་དང་མཐུན་པར་འདོད་པ་ལ་སོགས་པ་རྣམས་སུའོ། །

[Block 96]
མངོན་དུའི་ཕྱིར་ནི་ལས་བྱས་པའི་རྣམ་པར་སྨིན་པ་སྲིད་པས་ཡང་སྲིད་པར་འབྱིན་པར་མངོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 97]
སྡུག་བསྔལ་ཕྱིར་ནི་སྐྱེ་བ་དང་། རྒ་ཤིས་འགྲོ་བ་རྣམས་ཉོན་མོངས་པར་བྱེད་པའོ། །

[Block 98]
དེ་ཡང་།

[Block 99 [VERSE]]
རྣམ་གསུམ་རྣམ་གཉིས་ཀྱང་ཉོན་མོངས། །
རྣམ་བདུན་ཡང་དག་མིན་རྟོག་ལས། །

[Block 100]
རྣམ་གསུམ་ནི་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། [^28]ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 101]
དེ་ལ་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི་མ་རིག་པ་དང་སྲེད་པ་དང་ལེན་པ་རྣམས་སོ། །

[Block 102]
ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་ནི༌[^29]འདུ་བྱེད་རྣམས་དང་སྲེད་པའོ། །

[Block 103]
སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ཡན་ལག་ལྷག་མ༌[^30]རྣམས་སོ། །

[Block 104]
ཀུན་ནས་ཉོན་མོངས་པ་རྣམ་པ་གཉིས་ནི་རྒྱུའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། འབྲས་བུའི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 105]
དེ་ལ་རྒྱུའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ཉོན་མོངས་པ་དང་། ལས་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་ཡན་ལག་རྣམས་ཀྱིས་སོ། །

[Block 106]
འབྲས་བུའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ཡན་ལག་ལྷག་མ་རྣམས་ཀྱིས་སོ། །

[Block 107]
ཀུན་ནས་ཉོན་མོངས་པ་རྣམ་པ་བདུན་ནི་རྒྱུ་རྣམ་པ་བདུན་ཏེ། མ་རིག་པ་ནི་ཕྱིན་ཅི་ལོག་གི་རྒྱུའོ། །

[Block 108]
འདུ་བྱེད་རྣམས་ནི་འབེབས་པའི༌[^31]རྒྱུའོ། །

[Block 109]
རྣམ་པར་ཤེས་པ་ནི་ཉེ་བར་ཁྲིད་པའི་རྒྱུའོ། །

[Block 110]
མིང་དང་གཟུགས་དང་སྐྱེ་མཆེད་དྲུག་ནི་ཀུན་འཛིན་པའི་རྒྱུའོ། །

[Block 111]
རེག་པ་དང་ཚོར་བ་ནི་ཉེ་བར་སྤྱོད་པའི་རྒྱུའོ། །

[Block 112]
སྲེད་པ་དང་། ལེན་པ་དང་། སྲིད་པ་ནི་སྡུད༌[^32]པའི་རྒྱུའོ། །

[Block 113]
སྐྱེ་བ་དང་། རྒ་ཤི་ནི་སྐྱོ་བའི་རྒྱུའོ། །

[Block 114]
ཀུན་ནས་ཉོན་མོངས་པ་འདི་དག་ཐམས་ཅད་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ལས་འབྱུང་བའོ། །

[Block 115]
ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པའི་དོན་བསྡུས་པ་ནི་ཡོད་པའི་མཚན་ཉིད་དང་། མེད་པའི་མཚན་ཉིད་དང་། རང་གི་མཚན་ཉིད་དང་། བསྡུ་བའི་མཚན་ཉིད་དང་། མེད་པའི་མཚན་ཉིད་ལ་འཇུག་པའི་ཐབས་ཀྱི་མཚན་ཉིད་དང་། རབ་ཏུ་དབྱེ་བའི་མཚན་ཉིད་དང་། རྣམ་གྲངས་ཀྱི་མཚན་ཉིད་དང་། འཇུག་པའི་མཚན་ཉིད་དང་། ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་དེ། མཚན་ཉིད་རྣམ་པ་དགུ་བསྟན་པའོ། །

[Block 116 [HEADING]]
### སྟོང་པ་ཉིད། ^1-2-0

[Block 117]
དེ་ལྟར་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ༌[^33]རྟོག་པ་བརྗོད་ནས། སྟོང་པ་ཉིད་ཇི་ལྟར་ཤེས་པར་བྱ་བ་དེ་སྟོན་ཏེ།

[Block 118 [VERSE]]
སྟོང་པ་ཉིད་ནི་མདོར་བསྡུ་ན། །
མཚན་ཉིད་དང་ནི་རྣམ་གྲངས་དང་། །
དེ་ཡི་དོན་དང་དབྱེ་བ་དང་། །
སྒྲུབ་པ་དག་སྟེ་ཤེས་པར་བྱ། །

[Block 119]
ཞེས་བྱ་བའོ། །

[Block 120 [HEADING]]
#### སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད། ^1-2-1-0

[Block 121]
མཚན་ཉིད་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན།

[Block 122 [VERSE]]
གཉིས་དངོས་མེད་དང༌[^34]དངོས་མེད་པའི། །
དངོས་པོ་སྟོང་པའི་མཚན་ཉིད་དོ། །

[Block 123]
གཉིས་པོ་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོ་མེད་པ་དང་། དངོས་པོ་མེད་པ་དེའི་དངོས་པོ་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དོ། །

[Block 124]
དེ་ལྟར་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དུ་ཡོངས་སུ་བསྟན་པ་ཡིན་ནོ། །

[Block 125]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་ནི། ཡོད་པ་མ་ཡིན་མེད་པའང་མིན། །ཇི་ལྟར་ཡོད་པ་མ་ཡིན་ཞེ་ན། འདི་ལྟར་གཉིས་པོ་དེའི་དངོས་པོ་མེད་པའོ། །ཇི་ལྟར་མེད་པ་ཡང་མ་ཡིན་ཞེ་ན། འདི་ལྟར་གཉིས་པོའི་དངོས་པོ་མེད་པའི་དངོས་པོ་དེ་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དེ།[^35] དེ་བས་ན་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་དང་། ཐ་དད་གཅིག་པའི་མཚན་ཉིད་མིན། །ཐ་དད་པ༌[^36]ཡིན་ན་ནི་ཆོས་ལ་ཆོས་ཉིད་གཞན་མ་ཡིན་པ་མི་རུང་སྟེ། མི་རྟག་པ་ཉིད་དང་། སྡུག་བསྔལ་བ་ཉིད་བཞིན་ནོ། །

[Block 126]
གཅིག་པ་ཡིན་དུ་ཟིན་ན་ནི་རྣམ་པར་དག་པའི་དམིགས་པ་དང་། སྤྱིའི་མཚན་ཉིད་དུ་མི་འགྱུར་ཏེ། དེས་དེ་ཉིད་དང་གཞན་ལས་རྣམ་པར་གྲོལ་བ་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཡོངས་སུ་བསྟན་པ་ཡིན་ནོ། །

[Block 127 [HEADING]]
#### རྣམ་གྲངས། ^1-2-2-0

[Block 128]
རྣམ་གྲངས་ཇི་ལྟར་རིག་པར་བྱ་ཞེ་ན།

[Block 129 [VERSE]]
སྟོང་པ་ཉིད་ནི་མདོར་བསྡུ་ན། །
དེ་བཞིན་ཉིད་དང་ཡང་དག་མཐའ། །

[Block 130]
མཚན་མ་མེད་དང་དོན་དམ་དང་།[^37] །ཆོས་ཀྱི་དབྱིངས་ནི་རྣམ་གྲངས་སོ། །

[Block 131 [HEADING]]
#### རྣམ་གྲངས་ཀྱི་དོན། ^1-2-3-0

[Block 132]
རྣམ་གྲངས་ཀྱི་དོན་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན།

[Block 133 [VERSE]]
གཞན་མིན་ཕྱིན་ཅི་ལོག་མ་ཡིན། །
དེ་འགོག༌[^38]འཕགས་པའི་སྤྱོད་ཡུལ་དང་། །
འཕགས་པའི་ཆོས་ཀྱི་རྒྱུ་ཡི་ཕྱིར། །
རྣམ་གྲངས་དོན་དེ་གོ་རིམས་བཞིན། །

[Block 134]
གཞན་མ་ཡིན་པའི་ཕྱིར་དེ་བཞིན་ཉིད་དེ། རྟག་ཏུ་དེ་བཞིན་པའི་ཕྱིར་རོ། །

[Block 135]
ཕྱིན་ཅི་ལོག་མ་ཡིན་པའི་ཕྱིར་ཡང་དག་པའི་མཐའ་སྟེ། ཕྱིན་ཅི་ལོག་གི་གཞི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 136]
མཚན་མ་འགོག་པའི་ཕྱིར་མཚན་མ་མེད་པ་སྟེ། མཚན་མ་ཐམས་ཅད་མེད་པའི་ཕྱིར་རོ། །

[Block 137]
འཕགས་པའི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་ཡིན་པས་དོན་དམ་པ་སྟེ། ཡེ་ཤེས་དམ་པའི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 138]
འཕགས་པའི་ཆོས་ཀྱི་རྒྱུ་ཡིན་པས་ཆོས་ཀྱི་དབྱིངས་ཏེ། འཕགས་པའི་ཆོས་རྣམས་ནི་དེ་ལ་དམིགས་པས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 139]
འདིར་དབྱིངས་ཀྱི་དོན་ནི་རྒྱུའི་དོན་ཏོ། །

[Block 140 [HEADING]]
#### སྟོང་པ་ཉིད་ཀྱི་རབ་ཏུ་དབྱེ་བ། ^1-2-4-0

[Block 141]
སྟོང་པ་ཉིད་ཀྱི་རབ་ཏུ་དབྱེ་བ་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། ཀུན་ནས་ཉོན་མོངས་རྣམ་པར་དག །ཅེས་བྱ་བ་སྟེ། དེའི་རབ་ཏུ་དབྱེ་བ་སྟེ།[^39] །གང་གི་ཚེ་ཀུན་ནས་ཉོན་མོངས་པ་ལ། གང་གི་ཚེ་རྣམ་པར་དག་ཅེ་ན། དེ་ནི་དྲི་བཅས་དྲི་མ་མེད། །གང་གི་ཚེ་དྲི་མ་དང་བཅས་པར་གྱུར་པ་དེའི་ཚེ་ཀུན་ནས་ཉོན་མོངས་པ་གནས༌[^40]པའོ། །

[Block 142]
གང་གི་ཚེ་དྲི་མ་སྤངས་པ་དེའི་ཚེ་རྣམ་པར་དག་པའོ། །

[Block 143]
གལ་ཏེ་དྲི་མ་དང་བཅས་པར་གྱུར་ལ་དྲི་མ་མེད་པར་ཡང་འགྱུར༌[^41]ན་འགྱུར་བའི་ཆོས་ཅན་ཡིན་པས་ཇི་ལྟར་མི་རྟག་པར་མི་འགྱུར་ཞེ་ན། དེ་ནི་འདི་ལྟར།

[Block 144 [VERSE]]
ཆུ་ཁམས་གསེར་དང་ནམ་མཁའ་རྣམས། །
དག་པ་བཞིན་དུ་དག་པར་འདོད། །

[Block 145]
གློ་བུར་གྱི་དྲི་མ་དང་བྲལ་བ་ལ་བྱའི༌[^42]དེའི་ངོ་བོ་ཉིད་གཞན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 146]
གཞན་ཡང་རབ་ཏུ་དབྱེ་བ་ནི་སྟོང་པ་ཉིད་རྣམ་པ་བཅུ་དྲུག་པོ་འདི་ལྟ་སྟེ། ནང་སྟོང་པ་ཉིད་དང་། ཕྱི་སྟོང་པ་ཉིད་དང་། ཕྱི་ནང་སྟོང་པ་ཉིད་དང་། ཆེན་པོ་སྟོང༌[^43]པ་ཉིད་དང་། [^44]སྟོང་པ་ཉིད༌[^45]སྟོང་པ་ཉིད་དང་། དོན་དམ་པ་སྟོང་པ་ཉིད་དང་། འདུས་བྱས་སྟོང་པ་ཉིད་དང་། འདུས་མ་བྱས་སྟོང་པ་ཉིད་དང་། [^46]མཐའ་ལས་འདས་པ་སྟོང་པ༌[^47]ཉིད་དང་། ཐོག་མ་དང་ཐ་མ་མེད་པ་སྟོང་པ་ཉིད་དང་། དོར་བ་མེད་པ་སྟོང་པ་ཉིད་དང་། རང་བཞིན་སྟོང་པ་ཉིད་དང་། ཆོས་ཐམས་ཅད༌[^48]སྟོང་པ་ཉིད་དང་། རང་གི་མཚན་ཉིད༌[^49]སྟོང་པ་ཉིད་དང་། དངོས་པོ་མེད་པ་སྟོང་པ་ཉིད་དང་། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་དོ།[^50] །དེ་ཡང་མདོར་བསྡུ་ན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 147]
ཟ་བ་བཟའ་དང་དེ་ཡི་ལུས།[^51] །

[Block 148 [VERSE]]
གནས་ཀྱི་གཞི་ཡི་སྟོང་པ་ཉིད། །
དེ་ཡང་གང་གིས་ཇི་ལྟར་མཐོང་། །
གང་ཕྱིར་དེ་ཡང་སྟོང་པ་ཉིད། །
དགེ་གཉིས་ཐོབ་པར་བྱ་བའི་ཕྱིར། །

[Block 149 [VERSE]]
རྟག་ཏུ་སེམས་ཅན་ཕན་བྱའི་ཕྱིར། །
འཁོར་བ་གཏང་བར༌[^52]མི་བྱའི་ཕྱིར། །
དགེ་བ་མི་ཟད་བྱ་བའི་ཕྱིར། །
རིགས་ཀྱང་རྣམ་པར་དག་བྱའི་ཕྱིར། །

[Block 150 [VERSE]]
མཚན་དང་དཔེ་བྱད་ཐོབ་བྱའི་ཕྱིར། །
སངས་རྒྱས་ཆོས་རྣམས་དག་བྱའི་ཕྱིར། །
བྱང་ཆུབ་སེམས་དཔའ་སྒྲུབ་པར་བྱེད། །

[Block 151]
དེ་ལ་ཟ་བ་སྟོང་པ་ཉིད་ནི་ནང་གི་སྐྱེ་མཆེད་རྣམས་ལས༌[^53]བརྩམས་སོ། །

[Block 152]
བཟའ་བ་སྟོང་པ་ཉིད་ནི་ཕྱི་རོལ་གྱི་རྣམས་སོ། །

[Block 153]
དེའི་ལུས་ནི་ཟ་བ་དང་བཟའ་བ་དེ་གཉིས་ཀྱི་གནས་གང་ཡིན་པ་སྟེ་ཁོག་པའོ། །

[Block 154]
དེའི་སྟོང་པ་ཉིད་ནི་ཕྱི་ནང་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །

[Block 155]
གནས་ཀྱི་གཞི་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ཏེ། དེ་རྒྱ་ཆེ་བའི་ཕྱིར་དེའི་སྟོང་པ་ཉིད་ནི་ཆེན་པོ་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །
--- END BLOCKS ---
