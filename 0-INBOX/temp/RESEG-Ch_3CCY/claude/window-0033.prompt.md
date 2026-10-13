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
[Block 1156 [HEADING]]
### ཚིགས་བཅད་ང་གཉིས་པ། ^1-52-0

[Block 1157 [VERSE]]
གལ་ཏེ་མིག་གིས༌[^827]བདག་མཐོང་མིན། །
དེས་གཟུགས་མཐོང་བ༌[^828]ཇི་ལྟར་འགྱུར། །
དེ་ཕྱིར་མིག་དང་གཟུགས་བདག་མེད། །
དེ་བཞིན་སྐྱེ་མཆེད་ལྷག་མ་རྣམས། །

[Block 1158]
གལ་ཏེ་མིག་གིས་བདག་ཉིད་མི་མཐོང་ལ། དེའི་ཚེ་རང་གི༌[^829]བདག་ཉིད་མ་མཐོང་བས་བོང་བ་ལ་སོགས་པ་བཞིན་དུ་གཟུགས་ཀྱང་མི་མཐོང་ལ། དེ་ནི་བོང་བ་ལ་སོགས་པ་བཞིན་པས་མིག་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་སྒྲུབ་པར་བྱེད་ན་དེ། [^830]དེ་ཕྱིར་མིག་བདག་མེད་ཅེས་པ་ལ། གང་གི་ཕྱིར་མིག་གིས་གཟུགས་མི་མཐོང་བ་དེའི་ཕྱིར་རང་བཞིན་མེད་དོ། །

[Block 1159]
མིག་མེད་ན་མིག་དང་དེ་ལ་བརྟེན་པའི་མིག་གི༌[^831]བློ་མེད་པས་གཟུང་བ་མེད་པའི་ཕྱིར། གཟུགས་ནི་ཤིན་ཏུ་ཡང་རང་བཞིན་མེད་དོ། །

[Block 1160]
ཇི་ལྟར་མིག་དང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དག་རང་བཞིན་མེད་པ་ཉིད་ལྟར། དེ་བཞིན་སྐྱེ་མཆེད་ལྷག་མ་རྣམས་ནི། སྐྱེ་མཆེད་ཐམས་ཅད་མིག་དང་གཟུགས་བཞིན་དུ་རང་བཞིན་ཡིན་པར༌[^832]ཁོང་དུ་ཆུད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1161]
འདིར་སྨྲས་པ། རེག་གི་སྐྱེ་མཆེད་ཉེ་བར་བསྟན་པའི་ཕྱིར་མིག་ཡོད་པ་ཉིད་དེ། འདིར་རེག་གི་སྐྱེ་མཆེད་དྲུག༌[^833]པ་འདི་ལྟ་སྟེ། མིག་གི་རེག་པའི་སྐྱེ་མཆེད་ནས། ཇི་སྲིད་ཡིད་ཀྱི་རེག་པའི་སྐྱེ་མཆེད་ཀྱི་བར་དུ་ཞེས་སོ། །

[Block 1162]
དེ་ལ་རེག་པ་ཞེས་བརྗོད་པ་ནི་དབང་པོ་དང་ཡུལ་དང་ཤེས་པ་རྣམ༌[^834]གསུམ་འདུས་པའི་མཚན་ཉིད་ཅན། ཚོར་བའི་རྒྱུ་སེམས་ལས་བྱུང་བའི་ཆོས་ལ། དེ་ལ་རེག་པའི་སྐྱེ་མཆེད་ནི་རེག་པ་སྐྱེ་བའི་སྒོའི་དངོས་པོར་རྣམ་པར་གནས་པས་རེག་པའི་སྐྱེ༌[^835]མཆེད་དེ། མིག་གི་རེག་པའི་སྐྱེ་མཆེད་ནས་ཇི་སྲིད་ཡིད་ཀྱི་རེག་པའི་སྐྱེ་མཆེད་ཀྱི་བར་དུ་རིག་པར་བྱའོ། །

[Block 1163]
གལ་ཏེ་མིག་མེད་ན་དེའི་རེག་པའི་སྐྱེ་མཆེད་ཉེ་བར་མི་སྟོན་ལ། དེ་ཡང་ཉེ་བར་བསྟན་པས༌[^836]དེའི་ཕྱིར་རེག་གི་སྐྱེ་མཆེད་ཉེ་བར་བསྟན་པས་ན་མིག་ཡོད་པ་ཉིད་དོ་ཞེ་ན། སྨྲས་པ། སྐྱེ་མཆེད་རྣམས་ཡོད་ན་རེག་གི་སྐྱེ་མཆེད་ཅེས་བྱ་བར་འགྱུར་ན། དེ་ལྟ་ན་ཡང་སྐྱེ་མཆེད་རྣམས་མ་གྲུབ་སྟེ། ཇི་ལྟར་བྱས་ན་གང་གི་ཕྱིར་ཞེས་གསུངས་པ།

[Block 1164 [HEADING]]
### ཚིགས་བཅད་ང་བཞི་པ། ^1-53-0

[Block 1165 [VERSE]]
གང་ཚེ་གཅིག་དང་རེག་ལྡན་གཅིག །
[^837]དེ་ཚེ་ཅིག་ཤོས་སྟོང་པ་ཉིད། །
སྟོང་པའང་མི་སྟོང་མི་བརྟེན་ལ། །
མི་སྟོང་པ་ཡང་སྟོང་པ་མིན། །

[Block 1166]
སེམས་ཅན་རྣམས་ཀྱི་རྣམ་པར་ཤེས་པ་རྒྱུད་གཅིག་གི་ཕྱིར་རྣམ་པར་ཤེས་པ་གཅིག་གི་རྒྱུད་ཉིད་ལ་ཉེ་བར་འབྱུང་ལ། དེ་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་ཉེ་བ་ན། མིག་གཅིག་ཉིད་རེག་པ་དང་ལྷན་ཅིག་གྱུར་པར་འབྱུང་བས་རེག་ལྡན་གཅིག༌[^838]སྟེ། རེག་དང་འབྲེལ་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1167]
གང་གི་ཚེ་གཅིག་རེག་དང་ལྷན་ཅིག་གནས་པ་ན་དེའི་ཚེ་ཅིག་ཤོས་རྣ་བ་ལ་སོགས་པའི་རེག་གི་སྐྱེ་མཆེད་རྣམས་སྟོང་པ་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1168]
ཡང་འདི་སྙམ་དུ་སེམས་ན། གལ་ཏེ་ཡང་དེའི་གནས་སྐབས་ནས༌[^839]རང་གི་རྣམ་པར་ཤེས་པ༌[^840]སྟོང་པའི༌[^841]རྣ་བ་ལ་སོགས་པ་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་དང་བྲལ་བ་ཡོད་པའི་རྣ་བ་ལ་སོགས་པ་དེ་དག་ཀྱང་རང་གི་རྣམ་ཤེས་མངོན་དུ་གྱུར་པ་ན་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་གྱིས་མི་སྟོང་པར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། སྟོང་པའམ༌[^842]མི་སྟོང་མི་བརྟེན་ལ། །གང་ལས་གང་གི༌[^843]རང་བཞིན་དང་བཅས་པར་མི་རུང་སྟེ། འདི་ལྟ་སྟེ་གང་སྲ་བའི་རང་བཞིན་དང་བྲལ་བ་ནམ་ཡང་སྲ་བའི་རང་བཞིན་དང་ལྡན་པ་མ་ཡིན་ལ། དེ་བཞིན་དུ་རྣ་བ་ལ་སོགས་པ་ཡང་ནམ་ཡང་རེག་གི་སྐྱེ་མཆེད་མི་འབྱུང་ལ། མིག་ཀྱང་རྟག་པ་ཉིད་དུ་རེག་གི་སྐྱེ་མཆེད་ཅན༌[^844]དུ་འགྱུར་ཏེ། གང་གི་ཕྱིར་མི་སྟོང་པ་ཡང་སྟོང་པ་མ་ཡིན་ཏེ། གང་མི་སྟོང་པའི་རང་བཞིན་དེ་ནི་སྟོང་པ་ཉིད་མི་བརྟེན་ལ། ད་ལྟར་བ་མེ་དྲོ་བའི་མཚན་ཉིད་དང་ལྡན་པ་དེ་ཉིད་དེས་སྟོང་པ་མི་བརྟེན་ནོ། །

[Block 1169]
ཡང་ན་རང་བཞིན་གྱིས་མི་འགྱུར་བའི་ཕྱིར་སྟོང་པ་ཡང་མི་སྟོང་པ་མི་བརྟེན་ལ། མི་སྟོང་པ་ཡང་སྟོང་པ་མིན། །དེའི་ཕྱིར་གང་ཞིག་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་ཡིན་ན། དེ་ནི་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་ཉིད་ཐོབ་པའམ། གང་ཞིག་རེག་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་མ་ཡིན་པ་ཉིད་ཐོབ་པ་དེ་ཡང་མི་འཐད་དོ་ཞེས་བྱའོ། །

[Block 1170]
དེའི་ཕྱིར་རེག་གི་སྐྱེ་མཆེད་མེད་དོ། །

[Block 1171]
འདིར་སྨྲས་པ། གལ་ཏེ་རེག་གི་སྐྱེ་མཆེད་མེད་ཀྱང་དེ་ལྟ་ན་ཡང་རེ་ཞིག་རེག་པ་ཡོད་དེ། གསུམ་འདུས་པའི་མཚན་ཉིད་པས། [^845]དེ་ཡོད་ན་རེག་གི་སྐྱེ་མཆེད་ཀྱང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་རེག་པ་ཉིད་ཡོད་ན་རེག་པའི་སྐྱེ་མཆེད་ཡོད་དེ།[^846] དེ་ཡོད་པ་མ་ཡིན་ལ། ཇི་ལྟར་ཡང་མེད་པ་དེ་ལྟར་སྒྲུབ་པར་བྱེད་པ་གསུངས་པ།

[Block 1172 [HEADING]]
### ཚིགས་བཅད་ང་ལྔ་པ། ^1-54-0

[Block 1173 [VERSE]]
ངོ་བོ༌[^847]མི་གནས་ཡོད་མིན་པས། །
གསུམ་འདུས་པ་ཡང་ཡོད་མ་ཡིན། །
དེ་ཡི་བདག་ཉིད་རེག་མེད་པས། །
དེ་ཚེ་ཚོར་བ་ཡོད་མ་ཡིན། །

[Block 1174]
གནས་པའི་རང་བཞིན་ཅན་གྱི༌[^848]དངོས་པོ་རྣམས་ལས་ཕན་ཚུན་འདུས་པ་འབྱུང་སྲིད་ལ། མི་གནས་པའི་རང་བཞིན་ཅན་གྱི་དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་ལ་མ་ཡིན་ཏེ། སྐྱེས་མ་ཐག་ཏུ་འཇིག་པའི་ཕྱིར་མི་གནས་པའི་ངོ་བོ་ལ། མི་གནས་པའི་ངོ་བོའི་ཕྱིར་ཡང་སྐྱེས་མ་ཐག་ཏུ་འཇིག་པ་ཉིད་ཀྱིས་ནི༌[^849]འདུ་བའི་དུས་ཀྱི་བར་དུ་མེད་པའི་ཕྱིར། འདི་དག་ཕྲད་པ༌[^850]ག་ལ་ཞིག །ཅེས་བསྒྲུབས་པས། ངོ་བོས་མི་གནས་པའི་ངོ་བོ་ལ་གསུམ་འདུས་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 1175]
གང་གི་ཚེ་མེད་པ་དེའི་ཚེ་འདུ་བ་མེད་པས། དེའི་བདག་ཉིད་ཀྱི་རེག་པ་མེད་དེ། གསུམ་འདུས་པའི་རང་བཞིན་གྱི༌[^851]རེག་པ་མེད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 1176]
འདིར་སྨྲས་པ། རེག་པ་ཡོད་པ་ཉིད་དེ། དེའི་འབྲས་བུ་ཚོར་བ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1177]
འདིར་རེག་པའི་རྐྱེན་གྱིས་ཚོར་བ་ཉེ་བར་དམིགས་ལ། དེ་ཡོད་པས་དེའི་རྒྱུ་རེག་པ་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་ཚོར་བ་ཉིད་ཡོད་ན་རེག་པ་ཡོད་ལ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ། དེ་ཚེ་ཚོར་བ་ཡོད་མ་ཡིན། །ཞེས་པ་ལ། གལ་ཏེ་རེག་པ་ཡོད་ན་དེའི་ཚེ་རེག་པའི་རྒྱུ་ཅན༌[^852]ཚོར་བ་ཡོད་ལ། གང་གི་ཚེ་རེག་པ་ཉིད་མེད་ན་དེའི་ཚེ་རྒྱུ་མེད་པའི་ཚོར་བ་ག་ལས༌[^853]འབྱུང་། ཚོར་བ་མེད་པའི་ཕྱིར་ཡང་རེག་པ་མེད་དོ་ཞེས་གྲུབ་པོ། །འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་ཁྱོད་ཀྱིས།

[Block 1178 [VERSE]]
དེའི་ཕྱིར༌[^854]མིག་དང་གཟུགས་བདག་མེད། །
དེ་བཞིན་སྐྱེ་མཆེད་ལྷག་མ་རྣམས། །

[Block 1179]
ཤེས་པས་སྐྱེ་མཆེད་དགག་པ་དེ་ལྟར་སྨྲས་ལ། དེ་ལྟ་ན་ཡང་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་མ་བཀག་པའི་ཕྱིར་ཡོད་ལ། དེ་ཡོད་པས་དེའི་རྟེན༌[^855]དང་དམིགས་པའི་སྐྱེ་མཆེད་ཀྱང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་རྣམ་པར་ཤེས་པ་ཉིད་ཡོད་ན་སྐྱེ་མཆེད་རྣམས་ཡོད་ལ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 1180 [HEADING]]
### ཚིགས་བཅད་ང་དྲུག་པ། ^1-55-0

[Block 1181 [VERSE]]
ནང་དང་ཕྱི་ཡི་སྐྱེ་མཆེད་ལ། །
བརྟེན་ནས་རྣམ་པར་ཤེས་པ་འབྱུང་། །
དེ་ཕྱིར་རྣམ་པར་ཤེས་པ་མེད། །
སྨིག་རྒྱུ་སྒྱུ་མ་ལྟ་བུར་སྟོང་། །

[Block 1182]
གལ་ཏེ་རྣམ་པར་ཤེས་པ་རང་བཞིན་གྱིས་ཡོད་ན། དེ་ནི་ནང་དང་ཕྱིའི་སྐྱེ་མཆེད་ལ་བརྟེན་ནས་འབྱུང་བར་མི་འགྱུར་ཏེ། ད་ལྟར༌[^856]བཞིན་དུ་རྣམ་པར་ཤེས་པ་ཡོད་པ་ཉིད་དུ་གནས་པས་བརྟེན༌[^857]ནས་འབྱུང་བར་ཡང་མི་འགྱུར་རོ། །

[Block 1183 [VERSE]]
རྒྱུ་དང་རྐྱེན་ལས་སྐྱེས་པར་འགྱུར་བའི༌[^858]ཕྱིར། །
ངེས་པར་རྣམ་པར་ཤེས་པ་དེ་མེད་དེ། །
རང་བཞིན་གྱིས་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1184]
གལ་ཏེ་དེ་ལྟར་རྣམ་པར་ཤེས་པ་མེད་ན། དེ་བཞིན་དུ་དེ་ལྟ༌[^859]ཡོད་པ་མ་ཡིན་པའི་ཕྱིར། འདི་ནི་དམིགས་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ། སྨིག་རྒྱུ་སྒྱུ་མ་ལྟ་བུར་སྟོང་། །ཞེས་པ་ལ། སྒྱུ་མ་དང་སྨིག་རྒྱུ་བཞིན་དུ་རང་བཞིན་གྱིས་སྟོང་པའི་རྣམ་པར་ཤེས་པ་ཡང་འཇིག་རྟེན་པས་ཉེ་བར་དམིགས་ལ། དེ་ཙམ་ཞིག་ཀྱང་འདིའི་རང་བཞིན་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1185]
འདིར་སྨྲས་པ། ཡུལ་ཡོངས་སུ་གཅོད་པ་ཡོད་པས་རྣམ་པར་ཤེས་པ་ཡོད་པ་ཉིད་དོ། །

[Block 1186]
གལ་ཏེ་རྣམ་པར༌[^860]ཡུལ་ཡོངས་སུ་གཅོད་པ་པོ་ཡོད་ན་དེ་ལྟར་ཡོད་ལ། ཡོད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1187 [HEADING]]
### ཚིགས་བཅད་ང་བདུན་པ། ^1-56-0

[Block 1188 [VERSE]]
རྣམ་ཤེས་ཤེས་བྱ་ལ་བརྟེན་ནས། །
འབྱུང་བ་ཤེས་བྱ་ཡོད་མ་ཡིན། །
ཤེས་བྱ་ཤེས་པ་མེད་པའི་ཕྱིར། །
དེ་ཕྱིར་ཤེས་པ་པོ་ཉིད་མེད། །

[Block 1189]
འདིར་འདིའི་རྣམ་པར་ཤེས་པ་དམིགས་པ་མེད་པར་མི་འབྱུང་བས་ཤེས་བྱ་ལ་ལྟོས་ལ།[^861] གང་གི་ཕྱིར་དེ་ལྟར་རྣམ་པར་ཤེས་པ་དང་། ཤེས་བྱ་དག་ལ༌[^862]བརྟེན་ནས་འབྱུང་བས་ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་པས། དེའི་ཕྱིར་ཤེས་བྱ་མེད་ལ། ཤེས་བྱ་མེད་པར་གྱུར་ན་དམིགས་པ་མེད་པར༌[^863]རྣམ་པར་ཤེས་པ་ག་ལ་འབྱུང་ཞེས་བྱ་སྟེ། རྣམ་པར་ཤེས་པ་མེད་པས་རྣམ་ཤེས་ནི། །སྨིག་རྒྱུ་སྒྱུ་མ་བཞིན་དུ་སྟོང་། །ཞེས་གནས་སོ། །

[Block 1190]
འདིར་སྨྲས་པ། རྣམ་པར་ཤེས་པ་ནི་ཡོད་པ་ཉིད་དེ། ཤེས་བྱ་དང་ཤེས་པ་པོ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1191]
འདིར་རེ་ཞིག་རྣམ་པར་ཤེས་སོ་ཞེས་པས་རྣམ་པར་ཤེས་པ་པོ་ཡོད་དེ། ཕུང་པོ་ལ་བརྟེན་ནས་བརྟགས་པའི་གང་ཟག་བྱེད་པ་པོར་གྱུར་པའོ། །

[Block 1192]
དེ་གང་གིས༌[^864]རྣམ་པར་ཤེས་སོ་ཞེས་དེ་ནི་འདིའི་བྱེད་པ་ཡིན་ལ། གང་ཞིག་རྣམ་པར༌[^865]ཤེས་སོ་ཞེས་དེ་ནི་འདིའི་ལས་སོ། །

[Block 1193]
བྱེད་པ་དང་ལས་མེད་པར་བྱེད་པ་པོ་ཡོད་པར་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེས་ན་བྱེད་པ་པོ་ཡོད་པས་ན། དེ་བཞིན་དུ་ཤེས་བྱ་དང་ཤེས་པ་པོ་ཡོད་དོ་ཞེས་བྱའོ། །

[Block 1194]
སྨྲས་པ། གལ་ཏེ་ཤེས་པ་པོ་ཉིད་ཡོད་ན། རྣམ་པར་ཤེས་པ་དང་ཤེས་བྱ་ཡོད་པར་འགྱུར་ན། གང་ཇི་སྲིད་དུ་རྣམ་པར་ཤེས་པ་དང་ཤེས་བྱ་དག་མེད་པས་ལས་དང་བྱེད་པ་དང་བྲལ་བའི་ཕྱིར། བྱེད་པ་པོ་ཉིད་འགའ་ཡང་ག་ལ་ཞིག་ཅེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1195 [VERSE]]
ཤེས་བྱ་ཤེས་པ་མེད་པའི་ཕྱིར། །
དེ་ཕྱིར་ཤེས་པ་པོ་ཉིད་མེད། །
--- END BLOCKS ---
