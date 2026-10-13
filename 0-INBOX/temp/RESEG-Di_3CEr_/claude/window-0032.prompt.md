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

[Block 1126]
འདིར་ཡང་གལ་ཏེ་དེ་ཞེས་པའི་སྒྲས་བསྒྲུབ་བྱ་བརྗོད་པ་དང་མངོན་པར་འབྲེལ་བར་འགྱུར་ཏེ། དེས་བསྒྲུབ་བྱ་ཉིད་ལ་དེ་དང་ལྡན་པའོ་ཞེས་བརྗོད་པར་འགྱུར་རོ། །

[Block 1127]
དེ་ལ་ཡང་གལ་ཏེ་སྤྱིའམ་ཡང་ན་ཆོས་སམ། དེ་སྟེ་ཆོས་ཅན་ཉིད་ལས་འགྱུར་གྲང་། གལ་ཏེ་སྤྱི་ཡིན་ན་དེ་ལྟ་ན། སྤྱི་ཉིད་ཆོས་སུ་ཐལ་བར་འགྱུར། །འདིར་སྒྲ་མི་རྟག་གོ་ཞེས་བྱ་བའི་སྤྱི་ལ་མི་རྟག་པའི་ཆོས་ཉིད་དོ་ཞེས་འདིའི་གཏན་ཚིགས་སུ་བརྗོད་པར་འགྱུར་རོ། །

[Block 1128]
སྤྱིའི་ཆོས་གཞན་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1129]
རྭ་ཅན་ཡིན་པའི་ཕྱིར་རྟ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་ཡང་བསྒྲུབ་པར་བྱ་བ་ལ་སྤྱི་ཉིད་ཀྱི་ཆོས་སོ་ཞེས་བྱས་ན༌[^857]གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1130]
ཅི་སྟེ་ཆོས་ཡིན་ན་ནི་དེའི་བྱས་པ་ཉིད་ལ་སོགས་པ་མི་སྲིད་དོ། །

[Block 1131]
དེ་སྟེ་ཆོས་ཅན་ཡིན་ན་ནི་དེ་ཡང་མི་འཐད་དེ་གྲུབ་པའི༌[^858]ཕྱིར་རོ། །

[Block 1132]
མི་རྟག་པ་ཉིད་བསྒྲུབ་བྱ་ཡིན་ནོ་ཞེ༌[^859]ན་མ་ཡིན་ཏེ། སྤྱི་དོན་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1133]
མི་རྟག་པ་ཉིད་ཀྱི་སྒྲ་ཞེས་སམ། སྒྲ་མི་རྟག་པ་ཉིད་དོ་ཞེས་སམ། སྒྲ་མི་རྟག་གོ་ཞེས་པའི་སྤྱིའི་དོན་དེ་དག་ནི་རྣམ་པར་བཅད་པའི༌[^860]འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1134]
དེ་ལྟ་ན་སྤྱིའི་དོན་ཉིད་བསྒྲུབ་བྱ་ཡིན་པར་འགྱུར་རོ། །

[Block 1135 [VERSE]]
ཆོས་དང་ཆོས་ཅན་བསྒྲུབ་བྱ་མིན། །
དེ་དག་བསྒྲུབ་བྱར་མི་སྲིད་དེ།[^861] །
སྐྱོན་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 1136]
སྤྱི་ཡང་མ་ཡིན་ཏེ་སྔར་བརྗོད་པའི་སྐྱོན་ཉིད་དོ། །

[Block 1137]
དེས་ན་སྒྲའི་ཡོན་ཏན་དུ་གྱུར་པ་ཉིད་ནི་བསྒྲུབ་བྱར་འབྲེལ་བར་འགྱུར་ཏེ། དེ་ལ་སྤྱི་འམ་ཆོས་ཅན་ནམ་གཞན་ལ་ཡང་གང་དེ་དང་ལྡན་པའི་ཆོས་འགྱུར་བ་མེད་པའི་ཆོས་མི་རྟག་པའོ་ཞེས་བསྒྲུབ་བྱས་ཁས་བླང་བར་བྱའོ། །

[Block 1138]
དེ་ནས་སྒྲ་ཉིད་དེ་དང་ལྡན་པའོ་ཞེས་གང་དེའི་ཆོས་དེ་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1139]
དེའི་ཡང་ཐུན་མོང་བའི་དང་ཁྱད་པར་གྱི་བསྒྲུབ་བྱ་དང་ལྡན་པའི་ཆོས་སུ་འགྱུར་ཏེ། [^862]ཁྱད་པར་བསྒྲུབ་བྱ་དང་ལྡན་པའི། །ཆོས་འཐོབ།[^863] བསྒྲུབ་པར་བྱ་བ་དང་ལྡན་པའི་ཆོས་ཉིད་དོ་ཞེས་ངེས་པར་བཟུང་བར་བྱེད་པ་ནི་གང་ཡང་མེད་དོ། །

[Block 1140]
དོན་གྱི༌[^864]ཆོས་ཅན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1141]
དེ་ནི་བསྒྲུབ་བྱ་དང་ལྡན་པ་ཉིད་ཀྱི་ཆོས་སོ་ཞེས་འབྲེལ་བའི་ཕྱིར་དེའི་ཆོས་འཐོབ་པར༌[^865]འགྱུར་རོ། །

[Block 1142]
དེ་ལྟ་ན་ཡང་སྒྲ་རྟག་སྟེ། མཉན་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་པ་ཡང་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1143]
བསྒྲུབ་པར་བྱ་བའི་ཆོས་མཚུངས་པ་ཉིད་དོ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཁྱད་པར་དུ་བྱེད་པ་ལས་གཞན་ལ་གཉིས་སུ་འཇུག་གོ་ཞེས་པ་འདིས་ཐུན་མོང་དུ་གཞན་ལ་འཇུག་པ་མ་ཡིན་པའི་ཕྱིར་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 1144]
མི་རྟག་པ་ཙམ་ཉིད་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་ཡིན་ན༌[^866]སྒྲ་གཞན་གྱིའང་དེ་དང་ལྡན་པ༌[^867]བུམ་པ་ལ༌[^868]སོགས་པའི་ཆོས་གཏན་ཚིགས་སུ་བརྗོད་པར་གྱུར་པའི་ཕྱིར་མིག་གིས་གཟུང་བར༌[^869]བྱ་བ་ཉིད་ཀྱང་གཏན་ཚིགས་སུ་བརྗོད་པར་འགྱུར་རོ། །

[Block 1145]
གཞན་ཡང་མ་ངེས་པ་མ་ངེས་པ་ཞེས་བྱ་བ་ནི་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཏེ། འཁྲུལ་པའི་གཏན་ཚིགས༌[^870]དེ་ཡང་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1146]
དཔེར་ན་རྟག་སྟེ། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ཡང་དེ་དང་ལྡན་པར་རྟོགས་པར་འགྱུར་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་མ་འབྲེལ་བ་ཉིད་དོ། །

[Block 1147]
དེའི་ཕྱིར་ཆོས་མཐུན་པའི་དེ་དང་ལྡན་པ་ནི༌[^871]འཁྲུལ་བའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1148]
དེ་ལྟ་ན་ནི་དེ་དང་ལྡན་པའི་ཆོས་དང་མཐུན་པ་ཆོས་མཐུན་པ་ཡིན་པས་ཆོས་གཞན༌[^872]སྤངས་པར་འགྱུར་ཏེ། མཉན་པར་བྱ་བ་ཉིད་དང་། འཁྲུལ་པ་ཅན་གྱི་ཆོས་ཀྱི་ངག་མ་འཁྲུལ་བར་འགྱུར་རོ་ཞེས་ངེས་པར་བཟུང་བ་སྨྲས་པའི་ཕྱིར་རོ། །

[Block 1149]
སྔ་མ་ལ་ནི་ཇི་སྐད་བརྗོད་པའི་སྐྱོན་ཡོད་པ་ཡིན་ནོ། །

[Block 1150]
མཁའ་སོགས་ཡོད༌[^873]ཉིད་བསྒྲུབ་པ༌[^874]ཡི། །སྦྱོར་བའང་འགོད་པར་མི་བྱེད་འགྱུར། །

[Block 1151]
དེ་ལ་ནི་དམ་བཅས་པ༌[^875]དང་ལྡན་པའམ། བསྒྲུབ་པར་བྱ་བ་དང་ལྡན་པའི་ཆོས་སུ་གྲུབ་པ་ཡོད་པ་མ་ཡིན་ཏེ། ཆོས་ཅན་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1152]
དེའི་ཕྱིར་སྦྱོར་བ་ཡང་མ་འབྲེལ་བར་འགྱུར་བས་ན་གཏན་ཚིགས་སུ་མི་འཐད་པ་ཉིད་དོ། །

[Block 1153 [HEADING]]
#### སེར་སྐྱ་བ་རྣམས་ཀྱི་འདོད་པ། ^3-3-4-0

[Block 1154]
སེར་སྐྱ་བ་རྣམས་ན་རེ་གཞན་ལ་བསྟན་པར་བྱ་བའི་དོན་དུ་རྣམ་པར་ལྡན་པ་དང༌[^876]བསལ་ཏེ་འོངས་པའི་བྱེ་བྲག་གི༌[^877]རྗེས་སུ་དཔག་པ་རྣམ་པ་གཉིས་ཏེ། དེ་ལ༌[^878]རྣམ་པར་ལྡན་པའི་ངག་གི་དངོས་པོའི་ཡུལ་རྣམ་པ་ལྔ་སྟེ། དམ་བཅའ་བ་ལ་སོགས་པའི་དབྱེ་བས་སོ་ཞེས་ཟེར་རོ། །

[Block 1155]
དེ་ཡང་རྣམ་པར་ལྡན་པ་དང་བསལ་ཏེ་འོངས་པའི་སྦྱོར་བ་དག་ལ་གཞན་པར༌[^879]བྱ་བ་དང་འབྲེལ་པ་ཉིད་དུ་སྤྱད་པར༌[^880]བྱའོ། །

[Block 1156 [HEADING]]
##### རྣམ་པར་ལྡན་པ། ^3-3-4-1-0

[Block 1157]
ཡན་ལག་ཐམས་ཅད་ནི་གཏན་ཚིགས་ཉིད་མ་ཡིན་ཏེ། རྣམ་པར་ལྡན་པ་དང་བསལ་ཏེ་འོངས་པའི་ནང་དུ་འདུས་པའི་ཕྱིར་རོ། །

[Block 1158]
དེ་ལ་རེ་ཞིག་གཙོ་བོ་ཡོད་དེ་བསལ་བ་རྣམས་དང་རྗེས་སུ་འགྲོ་བ་མཐོང་བའི་ཕྱིར་ཞེས་པ་ལ། གལ་ཏེ་འདིར་གཙོ་བོའི་ཡོད་པ་ཉིད་བསྒྲུབ་བྱ་ཡིན༌[^881]ཞེ་ན། དེ་མ་ཡིན་ཏེ། ཚད་མའི་ཡུལ་མ་ཤེས་པའི་ཕྱིར་རོ།[^882] །

[Block 1159]
སྤྱིའི་མཚན་ཉིད་མ་ཡིན་པའི་ཡུལ་ལ༌[^883]རྗེས་སུ་དཔག་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1160]
བསྒྲུབ་བྱའི་ཆོས་ཀྱང་སྒྲུབ་བྱེད་འགྱུར། །བསྒྲུབ་བྱར་གྱུར་པའི་ཆོས་སྒྲུབ་བྱེད་དུ་འགྱུར་བའི་རིགས་ཏེ། ཐ་དད་དུ་གྱུར་པ་མེད་པས་སོ། །
--- END BLOCKS ---
