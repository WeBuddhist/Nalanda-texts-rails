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
ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་ནི་ཉན་ཐོས་པ༌[^265]རྣམས་ཚིག་གི་དོན་རྣམ་པ་བཅུ་དྲུག་ཏུ་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ༌[^266]རྣམས་ཚིག་གི༌[^267]དོན་རྣམ་པ་བཅུ་གསུམ་གྱིས༌[^268]སྟོན་པའོ། །

[Block 177]
སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་ནི་བཅོམ་ལྡན་འདས་འཁོར་རྣམས་ཀྱིས༌[^269]བསྐོར་ཏེ༌[^270]གུས་པ་རི་མོ་བྱེད་པའི་ཚུལ་གྱིས༌[^271]མཛེས་པར་གནས་པ་རྣམས་སོ། །

[Block 178]
དེ་ལ་དགེ་སློང་ཞེས་བྱ་བའི་དོན་རྣམ་པ་གསུམ་སྟེ། བདུད་དང་མུ་སྟེགས་འཇིག་པར་བྱེད་པ་དང་། སློང་བ་དང་ཚུལ་ཁྲིམས་བསྲུང་བས་དགེ་འདུན་གྱི་གྲངས་སུ་འགྲོ་བ་དང་། འཚོ་བ་གཙང་མས༌[^272]འཚོ་ཞིང་སྒོ་གསུམ་དག་པར་གནས་པའོ། །

[Block 179]
དགེ་འདུན་གྱི༌[^273]དགེ་སློང་བཞི་ཡན་ཆད་དེ་མང་བ་མཐུན་པ་རིགས་དང་གཞུང་མ༌[^274]འདྲེས་པའི་དོན་ཏོ། །

[Block 180]
ཆེན་པོ་ནི་ཆོས་དང་གྲངས་ལ་སོགས་པའི་ཆེན་པོ་རྣམས་དང་ལྡན་པ་དང་། སློབ་པ་དང་མི་སློབ་པ་ལས་འཕགས་པའི་ཕྱིར་ཁྱད་པར་ཆེ་བ་དང་། ཤེས་རབ་དང་ཡེ་ཤེས་མཐོང་བའི་ཕྱིར་ཡོན་ཏན་ཆེ་བ་དང་། སྟོང་ཕྲག་བཅུ་གཉིས་སྙེད་བཞུགས་པའི་ཕྱིར་གྲངས་མང་བས་ཆེ་བའོ། །

[Block 181]
ཐབས་ཅིག་ནི་གནས་པ་གཅིག་པའི་ཐ་ཚིག་གོ། །

[Block 182 [HEADING]]
###### ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ། ^4-1-5-5-1-0

[Block 183]
ཐམས་ཅད་ཀྱང་དགྲ་བཅོམ་པ་ཤ་སྟག་གོ་ཞེས་བྱ་བ་ནས། དབང་དུ་གྱུར་པ་ཤ་སྟག་གི་བར་སྨོས་པ་ནི༌[^275]ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་སྟེ། མདོ་སྡེ་ལས་ཚིག་གི་དོན་རྣམ་པ་བཅུ་དྲུག་སྨོས་པའོ། །

[Block 184]
དེ་ཡང་མདོར་རྣམ་པ༌[^276]གསུམ་དུ་བསྡུ་ན། ཚིག་གོང་མ་འོག་མས་བཤད་པའི་མདོ་དང་། སྤྱི་དང་དབྱེ་བའི་མཚན་ཉིད་བསྟན་པ་དང་། དོན་གྱི་མདོ་བསྡུ་བ་དང་གསུམ་མོ། །

[Block 185 [HEADING]]
###### **ཚིག་གོང་མ་འོག་མས་བཤད་པའི་མདོ།** ^4-1-5-5-1-1-0

[Block 186]
ཚིག་གོང་མས་འོག་མ་སྟོན་པ་ནི་ཚིག་གོང་མས་ཚིག་འོག་མ་བསྐྱེད་པ༌[^277]དང་། ཡང་ན་ཚིག་འོག་མ་གོང་མས་བཀྲོལ་བ་ནི་ཟག་པ་ཟད་པ་ཉིད་དགྲ་བཅོམ་པ་ཞེས་བསྟན་པ་དང་། ཉོན་མོངས་པ་ཐམས་ཅད་ཟད་པ་ཉིད་ནི་དགྲ་བཅོམ་པ་ཞེས་བཤད་པ་ལྟ་བུའོ། །

[Block 187]
ཟག་པ་ཟད་པ་ཞེས་པ་ནི་ཉོན་མོངས་པ་མངོན་དུ་རྒྱུ་བས་སྲིད་པ་རྣམས་སུ་ཟག་པར་བྱེད་པའི་ཕྱིར་ཟག་པ་ཞེས་བྱའོ། །

[Block 188]
མངོན་དུ་རྒྱུ་བ་དང་བག་ཆགས་ཀྱི་ཚུལ་དུ་གནས་པ་དེ་གཉི་ག་ཡང་སྤྱིར་ཟག་པ་ཞེས་བྱ་སྟེ། དེ་ཡང་འདོད་པའི་ཟག་པ་དང་། སྲིད་པའི་ཟག་པ་དང་། མ་རིག་པའི་ཟག་པ་དང་གསུམ་མོ། །

[Block 189]
བདེན་པ་བཞི་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་དང་། བག་ལ་ཉལ་བ་རྣམས་ནི་འདོད་པའི་ཟག་པའོ། །

[Block 190]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ན་ཁྲོ་བ་བཏོན་པའི་ཉོན་མོངས་པ་ལྷག་མ་ནི་སྲེད་པའི༌[^278]ཟག་པའོ། །

[Block 191]
ཁམས་གསུམ་གྱི་མ་རིག་པ་བཅོ་ལྔ་ནི་མ་རིག་པའི་ཟག་པའོ། །

[Block 192]
དེ་ལ་འདོད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་ཡང་འདོད་པས་གཞི༌[^279]བྱས་པའི་ཕྱིར་འདོད་པའི་ཟག་པའོ། །

[Block 193]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ན་ཉོན་མོངས་པ་གཞན་གྱིས༌[^280]མི་སྐྱེད་ཀྱི་སྲིད་པར་སྦྱོར་བ་ཉིད་ཉོན་མོངས་པ་ཡིན་པས་སྲིད་པའི་ཟག་པའོ། །

[Block 194]
མ་རིག་པ་ཡང་དངོས་སུ་མ་རིག་པ་ཉིད་ཀྱིས༌[^281]ཟག་པར་བྱེད་པའི་ཕྱིར་མ་རིག་པའི་ཟག་པའོ། །

[Block 195]
ཚིག་བཞི་པས་ཚིག་གཉིས་པ་དགྲོལ་བ་ནི་དབང་དུ་གྱུར་པས་ཟག་པ་ཟད་ཅེས་བྱའོ། །

[Block 196]
ཚིག་གཉིས་པ་དང་གསུམ་པས་བཞི་པ་དགྲོལ་བ་ནི་ཟག་པ་ཟད་པ་དང་ཉོན་མོངས་པ་མེད་པར་གྱུར་པས་དབང་ཡང་དག་པ་ཐོབ་ཅེས་བྱ་བའོ། །

[Block 197]
ཉོན་མོངས་པ་མངོན་དུ་རྒྱུ་དང་བག་ཆགས་སུ་གནས་པ་སྤངས་པས་དབང་ཐོབ་པ་ཞེས་བྱའོ།[^282] །ཚིག་དྲུག་པས་ཚིག་བཞི་པ་དགྲོལ་བ་ནི་ཤེས་རབ་དང་སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བས་དབང་རབ་ཏུ་ཐོབ་པ་སྟེ། ཏིང་ངེ་འཛིན་གྱི་སྒྲིབ་པ་སྤངས་པས༌[^283]སེམས་རྣམ་པར་གྲོལ་བ་དང་། རང་བཞིན་སྒྲིབ་པ་སྤངས་པས་ཤེས་རབ་རྣམ་པར་གྲོལ་བའོ། །

[Block 198]
མ་རིག་པ་དང་སྲེད་པ་ལ་སོགས་པ་སྤངས་པས་ཤེས་རབ་རྣམ་པར་གྲོལ་བ་དང་། དེ་དང་སྦྱོར་བའི་སེམས་གནས༌[^284]འཕོས་པས་སེམས་རྣམ་པར་གྲོལ་བ་དང་། དེ་གཉི་གའི་སྐྱོན་དང་བྲལ་ཏེ་འདུས་མ་བྱས་ཉིད་རྟོགས་པའི་ཕྱིར་དབང་དུ་གྱུར་པ་ཞེས་བྱའོ། །

[Block 199]
དེ་དག་གི་འཆིང་བ་མངོན་དུ་རྒྱུ་དང་བག་ཆགས་ཀྱི་ཚུལ་དུ་གནས་པ་ཡང་སྤངས་པའི་ཕྱིར་ཉོན་མོངས་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 200]
སེམས་དང་ཤེས་རབ་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའི་ཕྱིར་རྟ་ཅང་ཤེས་བཞིན་དུ་ཞི་ཞིང་དུལ་བ་དང་། གླང་པོ་ཆེན་པོ༌[^285]ཞེས་བྱ་བ་ནི་ཇི་ལྟར་མི་བདེ་བའི༌[^286]གནས་ཐམས་ཅད་དུ་སོང་ཡང་ལམ་བདེ་བ། མ་ཉམས་པ་ལ་འགྲོ་བ་བཞིན་གང་བགྲོད་པའི་གནས་སུ་སོན་པ་དང་ཐོགས་པ་མེད་པར་གྱུར་པ་སྟེ། དེའི་ཕྱིར༌[^287]བྱ་བ་བྱས་པ་བྱེད་པ་བྱས་པའོ། །

[Block 201]
བྱ་བ་བྱས་པ་བྱེད་པ་བྱས་པའི་ཕྱིར་ཁུར་བོར་བ་སྟེ། ལམ་དང་འགོག་པའི་བདེན་པ་མངོན་དུ་གྱུར་པས་སྲིད་པ་ཕྱི་མ་མི་ལེན་ཞེས་པའི་དོན་ཏོ། །

[Block 202]
སྲིད་པར་སྦྱོར་བའི་ཁུར་ལྕི་བ་བོར་བས་རང་གི་དོན་ཐོབ་པ་ཡིན་ཏེ་མྱ་ངན་ལས་འདས་པའི་བདེ་བ་ཐོབ་ཅེས་པའི་དོན་ཏོ། །

[Block 203]
རང་གི་དོན་བདེ་བ་ཐོབ་པ་ཡང་ཉོན་མོངས་པའི་རྒྱུ་སྤངས་པས་སྲིད་པར་སྦྱོར་བ་ཐམས་ཅད་ཡང་མི་ལེན་ཏེ། ཁམས་གསུམ་དུ་མི་སྐྱེ་ཞེས་པའི་དོན་ཏོ། །

[Block 204]
ཟག་པ་ཟད་པ་ཉིད་བཀའ་ཡང་དག་པས་སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བ་སྟེ། སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བ་ནི་མཐོང་བས་སྤང་བ་ཡང༌[^288]བསྒོམ་པས་སྤང་བའི་ཉོན་མོངས་པ་ཐམས་ཅད་བསལ་ཏེ་སེམས་ཀྱི་དབང༌[^289]ཐོབ་པ་དང་། ཡོན་ཏན་གྱི་མཐར་ཐུག་པས་རྫུ་འཕྲུལ་དང་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་རྫོགས་པར་གྱུར་པའོ། །

[Block 205 [HEADING]]
###### **སྤྱི་དང་དབྱེ་བའི་མཚན་ཉིད་བསྟན་པ།** ^4-1-5-5-1-2-0

[Block 206]
དབྱེ་བ་གཉིས་པ་སྟེ། སྤྱི་དང་དབྱེ་བ་བསྟན་པའི་སྒོ་སྟེ་ཀུན་ཀྱང་དགྲ་བཅོམ་པ་ཤེ་དག༌[^290]གོ་ཞེས་བྱ་བ་ནི་སྤྱིའི་མཚན་ཉིད་དོ། །

[Block 207]
ཚིག་གི་དོན་བཅོ་ལྔ་པོ་གཞན་ནི་དབྱེ་བའི་མཚན་ཉིད་དོ། །

[Block 208]
དགྲ་བཅོམ་པའི་དོན་ནི་འོས་པའི་དོན་རྣམ་པ་བཅོ་ལྔ་སྟེ། དེ་ལ་ཟག་པ་ཟད་པའི་ཕྱིར་ཞལ་ཟས་དང་ཁྲི་སྟན་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི༌[^291]མཆོད་པར་འོས་པས་མཆོད་པའི་ཞིང་དུ་མཛེས་པའོ། །

[Block 209]
ཉོན་མོངས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་སྟོན་པ་ལ་དབང་དུ་གྱུར་པ་སྟེ། ཁེ་དང་གྲགས་པ་ཚོལ་བ་དང་བྲལ་བའི༌[^292]ཕྱིར་རོ། །

[Block 210]
འཇུག་པར་ཡང་འོས་པ་སྟེ། གྲོང་དང་གྲོང་ཁྱེར་དུ་འཇུག་ན་སེམས་ཀྱི་དབང་དུ་གྱུར་པས་འདོད་པའི་ཡུལ་གྱིས་མི་བསླུ་བའི་ཕྱིར་རོ། །

[Block 211]
བདུད་དང་མུ་སྟེགས་འདུལ་བར་འོས་པ་སྟེ། སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་ཀྱི་སྤོབས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 212]
ཆོས་རྣམས་ལ་ཤེས་རབ་མྱུར་བར་འོས་པ་སྟེ། ཤེས་རབ་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའི་ཕྱིར་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པའོ། །

[Block 213]
ཆོས་འཆད་པ་ལ་ཧ་ཅང་མྱུར་བ་དང་བུལ་བའི་སྐྱོན་དང་བྲལ་བར་འོས་པ་སྟེ། ཆོས་འཆད་པ་ལ་མཁས་པ༌[^293]འབྲེལ་པ་སྐྱོ་བ་དང་བྲལ་བ་ཇི་ལྟར་རྟ་ཅང་ཤེས་བཞིན་སེམས་ཤིན་ཏུ་དུལ་བའི་ཕྱིར་རོ། །

[Block 214]
གཅིག་པུ་དབེན་པར་འོས་པ་སྟེ། ཟས་དང་གོས་ལ་སོགས་པ་ཡོ་བྱད་ཐམས་ཅད་མི་སོག༌[^294]མི་སྡུད་པས་ཆོག་ཤེས་པར་གནས་པ་ནི་ཇི་ལྟར་གླང་པོ་ཆེ་འདུ་འཛི་དང་བྲལ་བ་བཞིན་ནོ། །

[Block 215]
གཅིག་ཏུ་ན་བསམ་གཏན་རྣམས་ལ་མ་ཆགས་པ་སྟེ། བྱ་བ་བྱས་པས་རྟག་ཏུ་བླ་མའི་ས་ལ་བརྩོན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
