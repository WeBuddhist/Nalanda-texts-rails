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
འདྲེས་པ་ལ་དམིགས་པ་ཞེས་བྱ་བ་ནི་མཁས་པས་དམིགས་པའི་གནས་ལ་དམིགས་པའོ། །

[Block 1087]
འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1088]
དེའི་རྗེས་ལ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གཞག་པ་སྟེ། དེ་ནི་འཇིག་རྟེན་པ་ཞེས་བརྗོད་པར་བྱ་སྟེ། འདི་ལྟར་འཇིག་རྟེན་པ་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1089]
གང་གི་ཕྱིར་འཇིག་རྟེན་ལས་འདས་པ་འབའ་ཞིག་ནི་འཇིག་རྟེན་པ་ལ་རེག་པ༌[^717]མ་ཡིན་པས་སོ། །

[Block 1090]
དེ་བས་ན་གཅིག་ཏུ་ཞུགས་པར་མི་བརྗོད་དོ། །

[Block 1091]
དེ་གནས་གྱུར་ནས་ཞེས་བྱ་བ་ནི་འདྲེས་པ་ལ་དམིགས་པའི་ཡེ་ཤེས་ཀྱི་བྱེ་བྲག་གནས་གྱུར་པའོ། །

[Block 1092]
སངས་རྒྱས་ཀྱི་སྐུ་རྣམ་པ་གསུམ་ཐོབ་པར་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་རྣམ་པ་གསུམ་ཐོབ་པར་འགྱུར་བ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 1093]
མྱ་ངན༌[^718]འདས་པའི་ཁྱད་པར་ནི་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་མི༌[^719]གནས་པའི་མྱ་ངན་ལས་འདས་པ་འཛིན་པར་བྱེད་ཀྱི་ཉན་ཐོས་ནི་མ་ཡིན་ནོ། །

[Block 1094]
ཡོངས་སུ་དག་པའི་ཁྱད་པར་ནི་ཞེས་བྱ་བ་ལ། འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བག་ཆགས་དང་བཅས་པའི་ཉོན་མོངས་པ་རྣམས་སྤོང་བ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་སྦྱོང་བ་ཡིན་གྱི་ཉན་ཐོས་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 1095 [HEADING]]
#### དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པ་ཚིགས་སུ་བཅད་པ། ^3-2-10-0

[Block 1096]
ཇི་ལྟ་བུར་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པ་དེ་ཚིགས་སུ་བཅད་པ།

[Block 1097 [VERSE]]
མིང་དང་དངོས་གཉིས་ཕན་ཚུན་དུ། །
གློ་བུར་ཡིན་པར་ཡོངས་སུ་བཙལ། །

[Block 1098]
ཞེས་བྱ་བ་ལ། མིང་ནི་དོན་ལ་གློ་བུར་བ་ཡིན་ལ། དོན་ནི་མིང་ལ་གློ་བུར་བ་སྟེ། དེའི་བདག་ཉིད་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1099]
ཡོངས་སུ་བཙལ་ཞེས་བྱ་བ་ནི་མཉམ་པར་གཞག་པས་བལྟ་བར་བྱའོ། །

[Block 1100 [VERSE]]
བཏགས་པ༌[^720]རྣམ་པ་གསུམ་པོ༌[^721]ལ། །
དེ་ཙམ་ཉིད་དུ་བཙལ་བར་བྱ། །

[Block 1101]
ཞེས་བྱ་བ་ནི་དོན་གྱི་ངོ་བོ་དང་ཁྱད་པར་མ་ཡིན་པ་བཏགས་པའི༌[^722]དོན་དང་། བཏགས༌[^723]པའི་ཁྱད་པར་དེ་ཙམ་པ་ཉིད་དུ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1102]
ཡང་དག་ཇི་བཞིན་ཡོངས་ཤེས་པས། །ཞེས་བྱ་བ་ནི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་སྟེ། འདི་ལྟར་གང་གི་ཕྱིར་ཚོལ་བ་རྣམ་པ་བཞི་ཞེས་བྱ་བའི་རྒྱུ་ལས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1103]
དོན་མེད་པར་ནི་རྟོག་པ༌[^724]གསུམ་དང་། མཐོང་བ་གསུམ་ལ་ཞེས་བྱ་བ་ལ། དོན་མེད་པར་བརྟགས་པ་རྣམ་པ་གསུམ་མཐོང་བ་སྟེ། མིང་དུ་བརྟགས་པ་དང་། ངོ་བོར་བརྟགས་པ༌[^725]དང་། [^726]ཁྱད་པར་དུ་བརྟགས་པའོ། །

[Block 1104]
དོན་མེད་པ་ནི་དོན་མེད་པ་ཉིད་དོ། །

[Block 1105]
མཐོང་བ་གསུམ་ལ་ཞེས་བྱ་བ་ནི་དོན་མེད་ན་རྟོགས་པ༌[^727]ཡང་མེད་པར་འགྱུར་བ་སྟེ། གང་གི་ཕྱིར་བརྟག་པར༌[^728]བྱ་བ་ཡོད་ན་དེ་ལ་དམིགས་པ༌[^729]ཡོད་དེ། དེའི་ཕྱིར་དོན་མེད་པར་གྱུར་ན་རྟོག་པར་བྱེད་པ་ཡང་མེད་པར་བལྟའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1106]
གསུམ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་གསུམ་ལ་འཇུག་པའོ། །

[Block 1107]
དེ་ལ་མིང་དང་དོན་གཉིས་ཕན་ཚུན་གློ་བུར་བ་ཉིད་དུ་མཐོང་བ་ཉིད་དུ་མཐོང༌[^730]བར་གྱུར་ན་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་ལ་བཞུགས་པ༌[^731]ཡིན་ནོ། །

[Block 1108]
མིང་གི་ངོ་བོ་ཉིད༌[^732]བརྟགས་པ་དང་། ཁྱད་པར་དུ་བརྟགས་པ་ཙམ་དུ་མཐོང་བ་ན་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ལ་ཞུགས་པ་ཡིན་ནོ། །

[Block 1109]
བརྟགས་པ་དེ་ཉིད་མཐོང་བ་ན་ཡོངས་སུ་གྲུབ་པ་ལ་ཞུགས་པ་ཡིན་ཏེ། དེ་ལྟ་བུ་ནི་གསུམ་ལ་འཇུག་པ་ཡིན་ནོ། །

[Block 1110 [HEADING]]
#### དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་དོན་གྱི་མན་ངག། ^3-2-11-0

[Block 1111]
གང་གིས་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་དོན་གྱི་མན་ངག་སྦྱིན་པར་བྱེད་དེ། དེ་ལ་དོན་གྱི་ཚིགས་སུ་བཅད་པ། གཟུགས་བརྙན་ཡིད་དུ་མཐོང་བ་ནི། །ཞེས་བྱ་བ་ལ། ཆོས་དང་དོན་དུ་སྣང་བ་གང་ཡིན་པའི་གཟུགས་བརྙན་དེ་ཡིད༌[^733]ཡིན་ནོ་ཞེས་མཐོང་བའོ། །གང་གིས༌[^734]མཐོང་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔས་སོ། །གང་གི༌[^735]དུས་ན་ཞེ་ན། མཉམ་གཞག་པས་སོ། །

[Block 1112 [VERSE]]
དོན་གྱི་འདུ་ཤེས་བཟློག་ནས་སུ། །
རང་གི་འདུ་ཤེས་ངེས་པར་གཟུང་། །

[Block 1113]
ཞེས་བྱ་བ་ནི་དེའི་དུས་ན་དོན་གྱི་འདུ་ཤེས་བོར་ནས་རང་གི་སེམས་ཉིད་ཆོས་དང་དོན་གྱི་རྣམ་པ་དེ་ཡིན་པར་གཟུང༌[^736]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1114]
དེ་ལྟར་ནང་དུ་སེམས་གནས་སོ། །ཞེས་བྱ་བ་ན༌[^737]གང་གི་སེམས་འདི་ལྟར་གནས་པར་གྱུར་པ་སྟེ། དོན་ནི་མེད་དོ། །

[Block 1115]
དེ་ལྟ་ན་ཡང་སེམས་ལ་སེམས་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1116]
གཟུང་བ་མེད་པར་རྟོགས་པར་བྱོས། །ཞེས་བྱ་བ་ནི། གཟུང་བ་མེད་པར་ཤེས་པར་གྱིས་ཤིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1117]
དེ་ཕྱིར་འཛིན་པ་མེད་རྟོགས་ཀྱིས། །ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་གཟུང་བར་བྱ་བའི་དོན་ཡོད་པ་མ་ཡིན་པས་འཛིན་པར་བྱེད་པའི་སེམས་ཉིད་ཀྱང་རིགས་པ་མ་ཡིན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1118]
དེས་ན་དམིགས་པ་མེད་ལ་རེག །ཅེས་བྱ་བ་ནི། དེའི་ཕྱིར་ན་དེ་ལས་གཞན་པའི་དེ་བཞིན་ཉིད་ལ་རེག་པར་འགྱུར་རོ་ཞེས་སྨྲས་པ་ཡིན་ཏེ། དེ་བཞིན་ཉིད་ནི་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1119 [HEADING]]
#### མངོན་པར་རྟོགས་པའི་ཚིགས་སུ་བཅད་པ། ^3-2-12-0

[Block 1120]
དེ་ལས་གཞན་པ་མངོན་པར་རྟོགས་པའི༌[^738]ཚིགས་སུ་བཅད་པ་ཇི་ལྟར་མདོ་སྡེའི་རྒྱན་ལས་བསྟན་པ་ལས་གང་དེ་ལས་རྟོགས་པར་དཀའ་བ་དེ་བསྟན་པར་བྱས་པ། མཐའ་ཡས་ཕ་རོལ་མེད་ཅེས་བྱ་བ་སྟེ། ཕ་རོལ་རིང་བས་ཇི་ལྟར་ཚིག་ལ་མཐའ་མེད་ཅེས་བྱ་བ་ལྟ་བུ་སྟེ། དེ་ལ་མཐའ་མེད་པ་མ་ཡིན་ན་ཡང་མང་པོ་ཉིད་ལ་མཐའ་མེད་ཅེས་བྱ་བའི་བརྗོད་པ་འཐོབ་སྟེ། འདི་ཡང་དེ་དང་འདྲའོ། །ཅིའི་ཚོགས་རྣམས་ཤེ་ན། བསོད་ནམས་ཡེ་ཤེས་ཀྱིའོ། །

[Block 1121]
དེ་ལ་སྦྱིན་པ་ལ་སོགས་པ་ལ༌[^739]ཕ་རོལ་ཏུ་ཕྱིན་པ་གསུམ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་སོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1122]
བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གཉི་ག་སྟེ། དེའི་དོན་གྱི་ཐབས༌[^740]ཀྱི་བརྩོན་འགྲུས་ནི་ཡེ་ཤེས་སོ། །

[Block 1123]
གང་སེམས་ཅན་གྱི་དོན་གྱི་བརྩོན་འགྲུས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་སོ། །

[Block 1124]
དེ་བཞིན་དུ་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། དེ་ལ་གང་ཡང་ཚད་མེད་པ་རྣམས་ལ་དམིགས་པའི་བསམ་གཏན་གྱི་བསོད་ནམས་སོ། །

[Block 1125]
དེ་ལས་གཞན་པ་དག༌[^741]ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །གང་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་ཉིད་དོ། །
--- END BLOCKS ---
