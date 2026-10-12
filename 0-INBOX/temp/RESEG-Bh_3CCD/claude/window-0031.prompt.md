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
དེའི་ཕྱིར་ན་ཕུང་པོ༌[^754]ལྔ་ལས་དངོས་པོ་གང་ཡང་མེད་དོ། །

[Block 1087]
རང་བཞིན་བེམས་པོ་ཡིན་པས་བྱ་བ་ཇི་ལྟར་བྱེད། བེའུ་འོ་མས༌[^755]སྐྱེད་པ་ཡིན་ཞེས་མི་རིགས་ཏེ། དེ་ལ་གང་གི་ཕྱིར་བའི་སེམས་ཀྱིས་འོ་མ་སྦྱིན་པ་ལ༌[^756]འཇུག་པ་ཡིན་གྱི་འོ་མ་ནི་མ་ཡིན་ནོ། །

[Block 1088]
དཔེར་ན་བ་མི་འདོད་ན་རང་གི་བེའུ་ལ་ཡང་མི་སྟེར་བའི་ཕྱིར་རོ། །

[Block 1089]
དེའི་ཕྱིར་སེམས་དང་ལྡན་པ་ཁོ་ན་ལ་འཇུག་པ་དང་ལྡོག་པའོ། །

[Block 1090]
གང་གི་ཕྱིར་སྐྱེས་བུས་མི་བྱེད་དོ་ཞེས་ཁྱེད་ཅག་འདོད་པས་བྱ་བ་ཐམས་ཅད་གང་ལས་འབྱུང་། དེ་ལྟར་སྐྱེས་བུ༌[^757]མེད་དེ་དམིགས་པའི་མཚན་ཉིད་དང་ལྡན་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1091]
དཔེར་ན་བུམ་པས་དབེན་པའི་ས་ཕྱོགས་བཞིན་ནོ། །

[Block 1092]
མེད་པའི་སྐྱེས་བུ་གང་ཡིན་པ་དེ་ལ་འཆིང་བ་འམ་ཐར་པ་ག་ལས་སྲིད་རི་བོང་རྭ་ལ་སྤོང་བ་དང་ལེན་པ་བཞིན་ནོ། །

[Block 1093]
རང་བཞིན་ཡོད་པས་སྐྱེས་བུ་དང་ལྷན་ཅིག་ཏུ་བྱེ་བྲག་ཡོངས་སུ་ཤེས་པར་རིགས་སོ། །

[Block 1094]
དེ་ཡུལ༌[^758]མེད་པས་སྐྱེས་བུ་དུ་མ་དང་དེ་ཐར་པའི་ཕྱིར་རང་བཞིན་དུ༌[^759]འཇུག་པ་དང་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་མི་རིགས་སོ། །

[Block 1095]
དེ་ལྟར་གྲངས་ཅན་པ་རྣམས་བཀག་གོ། །

[Block 1096 [HEADING]]
###### **རིགས་པ་པ།** ^1-5-3-3-1-2-0

[Block 1097]
རིགས་པ་པ༌[^760]དང་ཁྱད་པར་པ་རྣམས་ནི་རྟག་པ་དང་བེམས་པོ་དག༌[^761]ཏུ་སྨྲ་བ་བདག་གི་ཡོན་ཏན་དགུ་ལོག་པ་ན་ཚིག་གི་དོན་བཅུ་དྲུག་ཡོངས་སུ་ཤེས་པ་ནི།[^762] ཚད་མ་བཞིས་གྲུབ་པའི་བདག་ཤེས་པས་གྲོལ་བའོ། །

[Block 1098]
དེ་ལྟར་ཡོངས་སུ་མི་ཤེས་པས་འཆིང་བའོ། །

[Block 1099]
དེ་རྣམས་ལ་ལན༌[^763]འདི༌[^764]ཡིན་ཏེ། བདག་མེད་དེ་དམིགས་པའི་མཚན་ཉིད་དང་ལྡན་པ་མི་དམིགས་པའི་ཕྱིར་ཏེ། བུམ་པས་དབེན་པའི་ས་ཕྱོགས་བཞིན་ནོ། །

[Block 1100]
གང་ཡོངས་སུ་ཤེས་པས་གྲོལ་བ་ཡོན་ཏན་དགུ་པོ་དེ་གང་ཡིན། གལ་ཏེ་འདི་ལྟར་འདོད་ན་ཁྱེད་ཅག་ཕུང་པོ་ལྔ་ཁོ་ན་བདག་ཡིན་ན། དེ་ནི་མི་རིགས་ཏེ། ཕུང་པོ་མི་རྟག་པས་བདག་ཀྱང་མི་རྟག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1101]
ཡང་ན་མི་རྟག་པ་མ་ཡིན་ཏེ་དེ་དང་གཞི༌[^765]མཐུན་པ་མེད་པས་འོན་ཀྱང་ཕུང་པོ་ལ་བདག་ཡོད་དོ་ཞེས་གཞི་དང་གཞི་ཅན་གྱི་ཐ་སྙད་དུ་གནས་ཞེས༌[^766]འདོད་དོ་ཞེ་ན། དེ་ཡང་མི་རིགས་ཏེ། རྟག་པ་དང་མི་རྟག་པ་དག་གི་གཞི་དང་གཞི་ཅན་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 1102]
ཡང་ན་གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ཡོད་མོད་ཀྱི་འོན་ཀྱང་རྒྱུ་དང་འབྲས་བུའི་འབྲེལ་པ་ཁོ་ན་གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ཡིན་གྱི་གཞན་མ་ཡིན་ནོ། །

[Block 1103]
འདི་ལྟར་རྟེན་གྱིས་བརྟེན་པའི་ལྟུང་བ་འགོག་པར་བྱེད་པའི་མཚན་ཉིད་ཀྱི་གནས་སྐབས་སྐྱེད་པར་བྱེད་པ་ཡིན་ཏེ། ལྟུང་བའི་ཆོས་དང་མི་ལྟུང་བའི་ཆོས་ཅན་ཐ་དད་པ་ཡིན༌[^767]ཕྱིར་རོ། །

[Block 1104]
དངོས་པོའི་གནས་སྐབས་གཞན་སྐྱེད་པར་བྱེད་པ་ནི་བྱ་བ་ཡིན་ཏེ། སྐད་ཅིག་མའི་རང་བཞིན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1105]
དཔེར་ན་སྣོད་ལ་འབྲས་བུ་བཞིན་ནོ། །

[Block 1106]
གཞི་གང་ཡིན་པ་དེ་ཉིད་རྒྱུ་ཡིན་ཞེས་བྱ་བའི་གཞི་ཅན་ཡང་མི་རྟག་པར་འགྱུར་རོ། །

[Block 1107]
དེ་ཡང་མི་རིགས་ཏེ། བདག་རྟག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1108]
བདག་ལ་ཕུང་པོ་ཡོད་ཅེས་ཕྱོགས་ནི་མི་རིགས་ཏེ། སྔ་མ་བཞིན་དུ་སྐྱོན་དུ༌[^768]ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1109]
བྱ་བའི་རབ་ཏུ་སྐྱེད་པས་རྒྱུ་ཉམས་པར་མཐོང་བའི༌[^769]ཤིན་ཏུ་ཡང་བདག་མི་རྟག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1110]
རྒྱུ་དེ༌[^770]རྣམས་ནི་ངེས་པར་འབྲས་བུ་དང་ལྡན་པར་མི་འགྱུར་ཏེ་ཞེས༌[^771]ཁྱོད་ཀྱི་བདག་གི་ཕུང་པོ་རྣམས་མི་སྐྱེད་པར་ཡང་ཡང༌[^772]སྲིད་པའོ། །

[Block 1111]
ཕུང་པོ་ཁོ་ན་བདག་ཡིན་ཞེས་གཞི་མཐུན་པའི་ཕྱོགས་སུ་སྔར་བཤད་པའི་སྐྱོན་ཁོ་ནར་ཐལ་བར་འགྱུར་ཏེ་ཐ་མི་དད་པའི་ཕྱིར་རོ།[^773] །

[Block 1112]
ཕུང་པོ་དང་བདག་ནི་མེ་དང་བུད༌[^774]ཤིང་བཞིན་དུ་ཐ་མི་དད་ཅེ་ན་དེ་ཡང་མེད་དོ། །

[Block 1113]
གལ་ཏེ་དེ་ལྟར་ཡིན་ན་བུད་ཤིང་ཉམས་པ་ལས་མི་སྐྱེ་བ་ནི་མེ་ཡིན་གྱི་གཞན་མ་ཡིན་ནོ། །

[Block 1114]
དེ་བཞིན་དུ་བདག་ཉམས་པ་ལས་ཕུང་པོ་སྐྱེ་བར་འགྱུར་བས༌[^775]བདག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1115]
ཡང་ན་བདག་ཡོངས་སུ་གྱུར་ཞིང་ཕུང་པོ་སྐྱེ་བ་མ་ཡིན་གྱི། འོན་ཀྱང་ཕུང་པོ་ཡོངས་སུ་གྱུར་པ་ལས་བདག་ཏུ་འགྱུར་རོ་ཞེ༌[^776]ན་སྨྲས་པ། ཕུང་པོ་མ་གཏོགས་པའི༌[^777]བདག་མི་དམིགས་པས་མེད་དོ་ཞེས་རྟག་པ་ཉིད་ཀྱང་མེད་དོ། །

[Block 1116]
བེམས་པོ་ཉིད་ཀྱང་མི་རིགས་ཏེ་བྲག་དང་འདྲ་བའི་བེམས་པོ་ལ་འཆིང་བ་དང་གྲོལ་བའི་ཐ་སྙད་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 1117]
དེའི་ཕྱིར་ཡོན་ཏན་དགུ་པོ་མཐོ་རིས་དང་དམྱལ་བ་སྒྲུབ་པར་བྱེད་པ་ཇི་ལྟར་རིགས། །

[Block 1118 [VERSE]]
ཆོས་དང་ཆོས་མིན་བདེ་སྡུག་བསྔལ། །
འདོད་དང་ཞེ་སྡང་དེ་བཞིན་ཏེ། །
རྩོལ་བ་ཤེས་པ་འདུ་བྱེད་རྣམས། །
བདག་ཡོད་པ་ལ་རྟགས༌[^778]རྣམས་སོ། །

[Block 1119]
ཞེས་འབྱུང་བ་དེ་ནི་མི་རིགས་ཏེ། གང་གི་ཕྱིར་རྟགས་ནི་རྟགས་ཅན་མཚོན་པར་བྱེད་པས་དེ་ལས་ཐ་དད་པ་ཡིན་ནམ། ཐ་མི་དད་པ་ཡིན། གལ་ཏེ་ཐ་དད་པ་ཡིན་ན་དངོས་པོ་ཐམས་ཅད་ལ་ཆོས་ལ་སོགས་པ་རྟགས་སུ་འགྱུར་རོ། །

[Block 1120]
ཡང་ན་ཐ་མི་དད་པ་ཡིན་ན་དེའི་ཚེ། རང་རིག༌[^779]པ་ཡིན་ནམ། གཞན་ཡིན། དེ་ལས༌[^780]གཞན་ཡིན་ན། རང་གིས་མི༌[^781]རིག་པའི་ཆོས་ལ་སོགས་པས་དམྱལ་བ་དང་མཐོ་རིས་ལ་སོགས་པའི་འབྲས་བུ་དང་འབྲེལ་པ་མེད་དོ། །

[Block 1121]
རང་རིག༌[^782]པ་ཡིན་ན་བེམས་པོ་ཉིད་དུ་ཇི་ལྟར་འགྱུར་ཞེས་ཕན་ཚུན་འགལ་བའོ། །

[Block 1122]
མེ་དང་དུ་བ་བཞིན་དུ་བདག་དང་རྟགས་དག་གི་འབྲེལ་པ་ཡིན་ན་དེ་ཡང་ཆོས་ལ་སོགས་པའི་བྱ་བ་རྟོགས་པར་བྱེད་པ་འབྱུང་བས་རྟོགས་པར་བྱ་བ་རྒྱུར་འགྱུར་བ་བདག་འགོག་པར་ཐལ་བར་འགྱུར་ཏེ། འབྲས་བུ་འབྱུང་བས་རྒྱུ་རྣམས་ཉམས་པར་འགྱུར་བའི་ཕྱིར་བདག་མེད་བདག༌[^783]ཅེས་རིགས་པ་པ་དང་བྱེ་བྲག་སྨྲ་བ་རྣམས་ལ་ལན་ནོ། །

[Block 1123 [HEADING]]
###### **འཇིག་རྟེན་རྒྱང་པན་པ།** ^1-5-3-3-1-3-0

[Block 1124]
འཇིག་རྟེན་རྒྱང་པན་པས་ནི་མངོན་སུམ་ཁོ་ན་ཚད་མ་ཡིན་གྱི་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1125 [VERSE]]
ལག་པ་རེག་པས་ལོང་བ་ཡིས།[^784] །
དཀའ་བའི་ལམ་དུ་རྒྱུག་པ་ན། །
རྗེས་སུ་དཔག་པ་གཙོར་གྱུར་ལ། །
ལྟུང་བ་དག་ནི་དཀོན་པ་མིན། །
--- END BLOCKS ---
