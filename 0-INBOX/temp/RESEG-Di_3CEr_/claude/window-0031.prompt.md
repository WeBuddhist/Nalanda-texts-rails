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
[Block 1086]
གལ་ཏེ་མི་བྱ་སྟེ། འདི་ལྟར། སྒྲུབ་བྱེད་ཉིད་དུ་མི་སྲིད་པས། །བསྒྲུབ་བྱ་སྒྲུབ་ཅེས་པའི་ངག་ལས་ཤེས་པ་དང་འདོད་པ་ལ་སོགས་པ་མི་སྟོན་པ་དེ་དག་ནི་བསྒྲུབ་བྱ་སྒྲུབ་པ་མ་ཡིན་ནོ་ཞེ་ན། ཡང་ཅི་བསྒྲུབ་བྱ་སྒྲུབ་བྱེད་དུ་དངོས་ལས་འདོད་དམ།

[Block 1087 [VERSE]]
ཡང་ན་བརྒྱུད་པ་ལས་ཀྱང་འདོད། །
དེ་ལས་ཅིར་འགྱུར་ཞེ་ན།
གཉིས་ཀ་གཞན་དུ་འཐོབ་པར་འགྱུར། །

[Block 1088]
གལ་ཏེ་དངོས་ལས་ཡིན་ན་ནི་གང་ཉན་པ་དང་འབྲེལ་བའི་དྲན་པ་དེ་ཁོ་ན་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1089]
གལ་ཏེ་བརྒྱུད་པ་ལས་ཡིན་ན་ཡང་གང་ཆོས་མཐུན་པའི་ཉན་པའི་ཤེས་པ་དེ་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1090]
གལ་ཏེ་ཕན་ཚུན་བརྒྱུད་ནས་བསྒྲུབ་བྱ་སྒྲུབ་པ་དེ་གཏན་ཚིགས་ཡིན་ཡང་ཉན་པའི་ཤེས་པ་ལ་ནི་ཐལ་བར་མི་འགྱུར་ཏེ། འདི་ལྟར། ཆོས་མཐུན་གཏན་ཚིགས་དེ་མ་ཡིན། །ངག་དེ་ནི་ཆོས་མཐུན་པ་ལས་དཔེར༌[^833]བརྗོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་དེ་ལའང་སྐྱོན་གཉིས་ཕྱིར། །ཆོས་མཐུན་པ་ལས་དཔེ་བརྗོད་པ་ལ་ཡང་དངོས་ལས་ཡིན་ནམ་ཡང་ན་བརྒྱུད་ནས་ཡིན་ཞེས་འགྱུར་བ་ཡིན་པས་གཉིས་ཀ་ལྟར་ན་ཡང་སྐྱོན་ཅན་ཡིན་ནོ། །

[Block 1091]
གལ་ཏེ་དངོས་ལས་བརྗོད་པར་འདོད་ན་ནི་ཆོས་དང་མཐུན་པའི་ཤེས་པ་དེ་ཉིད་རྟགས་སུ་འགྱུར་རོ། །

[Block 1092]
དེ་ནི་དངོས་དང་བརྒྱུད་པ་ལས་དེ་བསྒྲུབ་བྱ་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 1093]
ཅི་སྟེ་བརྒྱུད་པ་ལས་ཡིན་ན་ཡང་གང་ཉན་པའི་ཤེས་པ་ལ་སོགས་པ་ལ་ཐལ་བར་འགྱུར་བའི་གནས་སྐབས་དེ་ཉིད་དོ། །

[Block 1094]
དེ་ལྟ་ན་ཡང་སྐབས་སུ་བབ་པའི་ཕྱིར་བསྒྲུབ་བྱ་ཁྱད་པར་ཅན་དུ་བསྟན་པར་མི་བྱའོ་ཞེ་ན། གནས་སྐབས་དེ་གང་ཡིན། གནས་སྐབས་ལ་ཡང་གཞན་མི་སྲིད། །གནས་སྐབས་ཀྱི་ཕྱོགས་ལ་ཡང་གང་ཆོས་མཐུན་པ་ལས་དཔེར་བརྗོད་བསྟན་པ་དེ་ཉིད་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1095]
ཆོས་མཐུན་པའི་དཔེར་བརྗོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་གཞན་ལ་ཡང་སྲིད་དོ། །

[Block 1096]
སྲིད་དུ་ཆུག་ཆོས་མཐུན་པའི་ལྟོས་པའི༌[^834]དཔེར༌[^835]བརྗོད་ཡན་ལག་ཕྱི་མ་བསྟན་པ་རྣམས་ཀྱང་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1097]
གལ་ཏེ་ཉེས་པ་དེ་ནི་མེད་དོ། །

[Block 1098]
དཔེར་བརྗོད་པ་ལ་སོགས་པ་ནི་གཏན་ཚིགས་ཉིད་དུ་མི་འགྱུར་ཏེ། རང་རང་གི་མཚན་ཉིད་བསྟན་པས་གནོད་པས་ནའོ། །

[Block 1099]
རང་རང་མཚན་ཉིད་ཀྱིས་གནོད་ཕྱིར། །རྣམ་པར་རྟོག་པ༌[^836]སྲིད་མ་ཡིན། །

[Block 1100]
ཐོབ་པ་རྣམས་ཀྱིས༌[^837]གཅིག་ལ་གནོད་པ་བཞིན་དུ་རྣམ་རྟོག་བསྡུས་པ་ལ་ཡང་འགྱུར་བའི་ཕྱིར་ཐེ་ཚོམ་དུ་འགྱུར་རོ། །

[Block 1101]
དེ༌[^838]ཕྱིར་དྲུག་པར། ཆོས་མཐུན་པའི་དཔེར་བརྗོད་པ་གཏན་ཚིགས་སུ་ཞེས་དྲུག་པར་འགྱུར་ཏེ། དཔེར་ན་གཞན་ལ་ཆོས་དེའི་གཏན་ཚིགས་སོ་ཞེས་པ་བཞིན་ནོ། །

[Block 1102]
དེ་ལྟ༌[^839]ན་ཡང་། ཐེ་ཚོམ་ཡོངས་སུ་སྤངས་པར་འགྱུར་གྱི་སྐྱོན་མེད་པ་ཉིད་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། དེ་ལ་ཡང་། ཁྱད་པར་དོན་མེད་པར་འགྱུར་རོ། །

[Block 1103]
དྲུག་པར་བྱས་ནས་ཀྱང་བསྒྲུབ་བྱ་སྒྲུབ་པ་སྨོས་པ་ལྷག་པར་འགྱུར་རོ། །

[Block 1104]
གལ་ཏེ་ཁྱད་པར་དུ་བྱས་པའི་དོན་དེ་འགྱུར་གྱི་ཆོས་མཐུན་པའི་ངག་ཐམས་ཅད་ནི་གཏན་ཚིགས་མ་ཡིན་ནོ་ཞེ་ན།

[Block 1105]
ངག་ཀུན་མི་འདོད་ཞེ༌[^840]ན་གང་། །འདོད་དེ་ཁྱད་པར་ཅན་དུ་གྱིས། །

[Block 1106]
གལ་ཏེ་ཆོས་མཐུན་ངག་ཐམས་ཅད་གཏན་ཚིགས་མ་ཡིན་ན་ཡང་གང་ཆོས་མཐུན་པའི༌[^841]ངག་དེ་ཉིད་གཏན་ཚིགས་མ་ཡིན་ནམ། དོན་གང་དག་གི་ཁྱད་པར་གྱིས་དེ་ཁྱད་པར་དུ་མི་བྱེད། གལ་ཏེ་འདི་ལྟར་ཁྱད་པར་གྱི་སྒྲ་ལ་མི་སྲིད་པའི་ཕྱིར་དོན་དུ་རྟོགས་པའི་དོན་ལ་འགྱུར་ཏེ། དམ་བཅའ་བ་དང་གཏན་ཚིགས་སུ་འགལ་བའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལྟར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར།

[Block 1107]
དགོས་པ་མེད་པར་དངོས་ཀྱི་ནི། །སྒྲ་དོན༌[^842]འདས༌[^843]འདོད་མ་ཡིན། །

[Block 1108]
རྒྱུ་མཚན་མེད་པར་དངོས་ཀྱི་སྒྲའི་དོན་ལ་འདས་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1109]
དེའི་ཕྱིར་ཆོས་མཐུན་པ་ཉིད་ཁྱད་པར་དུ་བྱའོ། །

[Block 1110]
དོན་སྒྲ་ཁྱད་པར་དུ་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1111]
དེ་ལྟར་ཁྱད་པར་དུ་མ་བྱས་པ་ནི་ཇི་ལྟ་བ་བཞིན་དུ་མི་སྒྲུབ་པའི་ཕྱིར་ཁྱད་པར་དུ་བྱའོ།[^844] །

[Block 1112]
ཅི་སྟེ་བསྒྲུབ་བྱ་སྒྲུབ་པར་བྱེད་པར་སྨོས་པ་དེ་ཉིད་དེ་ཁྱད་པར་དུ་བྱས་པ་མ་ཡིན་ནོ་ཞེ་ན། དེ་ཁྱད་པར་དུ་བྱས་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་གྲངས་ཙམ་ཡན་ལག་ཐམས་ཅད་བསྒྲུབ་བྱ་སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་འགྱུར་བས་ན་བསྒྲུབ་བྱའི་ཁྱད་པར་དུ་བྱེད་པར་ནི་གོ་བར་མི་བྱའོ། །

[Block 1113]
གལ་ཏེ་འདི་ལྟར་ཆོས་མི་མཐུན་པར་སྒྲུབ་པར་བྱེད་པ་ལས་བཟློག་པ༌[^845]དེ་བཞིན་དུ་བསྒྲུབ་བྱ་སྒྲུབ་པར་བྱེད་པར་བཟུང་ངོ་། །ཡང་སྒྲུབ་པར་མི་བྱེད་པ་འདི་ཇི་ལྟ་བུ་ཞིག་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ཏེ་གང་ཆོས་མཐུན་པ་དེ་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་མ་ཡིན་ཏེ། གཏན་ཚིགས་ཉིད་དོ་ཞེས་བརྗོད་པར་བྱ་བ༌[^846]ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་བུའི་ཁྱད་པར་ཡང་རིགས་པ་མ་ཡིན་ཏེ་སྤྱིར་བཏང་བ་ལ། དམིགས་བསལ་ཡོད་པར་སྲིད་མ་ཡིན། །གང་འཁྲུལ་པ་ལ་སོགས་པའི་ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་ཡིན་གྱི་དེ་གཏན་ཚིགས་ཉིད་དུ་བྲལ་བར་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། དམིགས་ཀྱིས་བསལ་བའི་ཡུལ་ལ་སྤྱིར་བཏང་བའི་གོ་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 1114]
སྔར་དམིགས་ཀྱིས་བསལ་བ་བཀོད་པ་ལ༌[^847]ཕྱིས་སྤྱིར་བཏང་བ་བརྟག་པར་བྱ་བའམ། དམིགས་ཀྱི༌[^848]བསལ་བའི་ཡུལ་ལ་སྤྱིར་བཏང་བ་དགོད་པ༌[^849]ནི་མ་ཡིན་ནོ། །

[Block 1115]
གཞན་ཡང་།

[Block 1116]
དེར་སྣང་གིས་སྟོང་ཆོས་གཞན་དང་། །མཚུངས་ཏེ་གཏན་ཚིགས་ཉིད་དུ་འགྱུར།[^850] །

[Block 1117]
གལ་ཏེ་གཏན་ཚིགས་ལྟར་སྣང་བས་སྟོང་པས་ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་གཏན་ཚིགས་ཡིན་ན་སྒྲ་རྟག་སྟེ། མཉན་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་དེ་དཔེ་དང་ཆོས་མཐུན་པ་དེ་དག་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ལ་མི་སྲིད་དོ།[^851] །

[Block 1118]
དེ་ནི་སླར་སྦྱོར་བའི་བུམ་པ་ལ་སོགས་པའི་ཆོས་མི་མཐུན་པ་དང་ཆོས་གཞན་ཉིད་དུའང་འགྱུར་ཏེ། དེ་བཞིན་དུ་སྒྲ་རྟག་སྟེ། བརྩལ༌[^852]མ་ཐག་ཏུ་བྱུང་བའི་ཕྱིར་གློག༌[^853]ལ་སོགས་པ་བཞིན་ཞེས་པ་ཆོས་མི་མཐུན་པ་ཡང་ངོ་། །ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་དེ་དག་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ལ་མི་སྲིད་དོ། །

[Block 1119]
གཞན་དག་ནི་བསྒྲུབ་བྱར་སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་སྔ་མས་ཁྱད་པར་དུ་བྱེད་དོ། །

[Block 1120]
དེ་སྐད་དུ་བརྗོད་པ་ནི། གང་ཆོས་མཐུན་པ་ལས་དཔེར་བརྗོད་པ་སྟོན་པ་དེ་བསྒྲུབ་བྱ་སྒྲུབ་པའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 1121]
གང་བསྒྲུབ་པར༌[^854]བྱ་བ་དང་ཆོས་མཐུན་པ་ལ་སོགས་པ་དེ་དཔེ་ལ་སོགས་པའོ་ཞེས་ཟེར་རོ། །

[Block 1122]
དེ་དག་གི་ལྟར་ན་ཡང་དྲུག་པ་ཉིད་དུ་རིག་པའི་ཚུལ་ལ་ཐེ་ཚོམ་མེད་པའི་དོན་ཡིན་ཞིང་། གཏན་ཚིགས་ལྟར་སྣང་བས་སྟོང་པ་ཡང་གཏན་ཚིགས་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1123]
གཏན་ཚིགས་ཀྱི་མཚན༌[^855]ཉིད་དུ་མི་རིགས་སོ། །

[Block 1124 [HEADING]]
#### བྱེ་བྲག་པ་རྣམས་ཀྱི་འདོད་པ། ^3-3-3-0

[Block 1125]
བྱེ་བྲག་པ་རྣམས་ཀྱི་དེ་དང་ལྡན་པའི་ཆོས་གཏན་ཚིགས་སོ་ཞེས་རྗོད་པར༌[^856]བྱེད་དོ། །
--- END BLOCKS ---
