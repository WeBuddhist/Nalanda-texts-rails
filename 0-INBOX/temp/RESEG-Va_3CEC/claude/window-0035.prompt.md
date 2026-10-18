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
[Block 1226]
འཁོར་བའི་མཐའི་བར་དུ་ཆོས་བཤད་ཀྱང་སྤོབས་པ་ཟད་པར་མི་འགྱུར་བ་ནི་སྤོབས་པ་ལ་མཁས་པའོ། །

[Block 1227]
རང་དང་སྤྱིའི་མཚན་ཉིད་རྣམ་པར་འབྱེད་པ་ནི་ཤེས་རབ་པོ། ། ཆོས་ཐམས་ཅད་སྟོང་པར༌[^1043]ཁོང་དུ་ཆུད་པ་ནི་ཡེ་ཤེས་སོ། །

[Block 1228]
དགའ་ལྡན་གྱི་ཕོ་བྲང་ནས་འཆི་འཕོ་བ༌[^1044]ལ་སོགས་པ་སྟོན་པ་ནི་ཐབས་ལ་མཁས་པ་ལ་འཇུག་པའོ། །

[Block 1229]
དེ་དག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ལྷའི་མིག་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས། འཇིག་རྟེན་གྱི་ཁམས་གཞན་གྱི་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་དེ་དག་མཐོང་ནས་བདག་ཉིད་ཀྱིས་ཀྱང་དེ་དག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ། །

[Block 1230]
གཟུགས་ཐམས་ཅད་མཐོང་བ་བཤད་ཟིན་ཏོ།། །།

[Block 1231 [HEADING]]
#### མི་མཐུན་པའི་དྲི་མས་མ་གོས་པ། ^3-1-3-0

[Block 1232]
མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་མ་གོས་པར༌[^1045]བསྟན་པའི་ཕྱིར་དེ་དག་གི་མིག་དེ་ནི་གཟུགས་ཐམས་ཅད་མཐོང་བས་ན་སྒྲིབ་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་གི་མིག་ཅེས་བྱ་བ་ནི་ལྷའི་མིག་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་མིག་གོ། །

[Block 1233]
ཅིས་ཀྱང་མ་བསྒྲིབས༌[^1046]མ་ཆོད་པར་ཉེ་བ་དང་རིང་བ་ལ་སོགས་པའི་གཟུགས་ཐམས་ཅད་མཐོང་བས་ན་སྒྲིབ་པ་མེད་པའོ། །

[Block 1234]
གཟུགས་ཐམས་ཅད་ལ་མི་ཆགས་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ཐམས་ཅད་མཐོང་བ་ནི་གཟུགས་མཛེས་པ་རྣམས༌[^1047]འདོད་ཆགས་མི་སྐྱེ་བའོ། །

[Block 1235]
རྣམ་པར་གྲོལ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་བག་ལ་ཉལ་དང་ལྟ་བ་ཐམས་ཅད་ཀྱི་བག་ལ་ཉལ་དང་ཉོན་མོངས་པ་མངོན་སུམ་དུ༌[^1048]འབྱུང་བ་ཐམས་ཅད་སྤངས་པས་སོ།[^1049] །རང་བཞིན་གྱིས༌[^1050]འོད་གསལ་བས་ན་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་དྲི་མ་མེད་ཅིང་གཟུགས་གསལ་བར་མཐོང་བའི་མཚན་ཉིད་ཡིན་པས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1236]
ཡུལ་ཐམས་ཅད་ལ་མི་གནས་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ཐམས་ཅད་ལ་མི་རྟོན༌[^1051]པའོ། །

[Block 1237]
ཉོན་མོངས་པ་དང་བག་ལ་ཉལ་བ༌[^1052]ཐམས་ཅད་ལ་མི་སྐྱེ་བའོ་ཞེས་བྱ་བ་ནི་མིག་གིས༌[^1053]གཟུགས་ཐམས་ཅད་མཐོང་དུ་ཟིན་ཀྱང་གཟུགས་མཐོང་བའི་སྒོ་ནས་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་ཉོན་མོངས་པ་སྐྱེ་བར་ཡང་མི་འགྱུར་ལ་ཉོན་མོངས་པའི་བག་ཆགས་ལ་སོགས་པར་ཡང་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1238]
ཐེ་ཚོམ༌[^1054]མེད་པས་ན༌[^1055]ཞེས་བྱ་བ་ནི་བདེན་པ་དང་དཀོན་མཆོག་ལ་ཡིད་གཉིས་མེད་པས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1239]
སྒྲིབ་པར་གྱུར་པའི་ཆོས་ཐམས་ཅད་ལས་ཀུན་ནས་མ་ལངས་ཞེས་བྱ་བའི་བར་དུ་གཅོད་པའམ། སྒྲིབ་པར་འགྱུར་བའི་ཆོས་འདོད་པ་ལ་འདུན་པ་ལ་སོགས་པའི་རྒྱུ་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1240]
ཆོས་ཐམས་ཅད་སྣང་བ་ལ་གསལ་བ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་མཐོང་བར་བྱ་བ་ལ་གསལ་བར་མཐོང་བ་ཐོབ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1241]
ཡེ་ཤེས་ལ་རྟོན་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ལ་རྟོན་པ་ཡིན་པས་དབང་པོའི་འབྱུང་བ་ཆེན་པོ་ལ་མི་རྟོན་པ་སྟེ། དེ་བས་ན་རྣམ་པར་ཤེས་པའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཞེས་བྱའོ། །

[Block 1242]
ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱིས་མ་ཆགས་མི་སྡང་། མ་རྨོངས་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་གཏི་མུག་གིས་མ་གོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1243]
དེ་དག་གི་མིག་དེ་ནི་འཕགས་པའི་དབང་པོ་རྣམས་ལ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པའི༌[^1056]ཞེས་བྱ་བ་ལས་འཕགས་པའི་དབང་པོ་ནི་དད་པ་དང་དྲན་པ་ལ་སོགས་པའི་དབང་པོ་སྟེ། དབང་པོ་དེ་དག་དང་ལྡན་པའི་མིག་དེས་སྣང་བ་མཆེད་པ༌[^1057]ལ་སོགས་པའི་ཆོས་རྣམས་རྟོག་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1244]
འོད་ཟེར་མཉམ་པར་གཏོང་བས་ན་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་ཆེན་པོས་སེམས་ཅན་ལ༌[^1058]མཉམ་པར་ལྟ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1245]
སེམས་ཀྱིས་མི་དགེ་བའི་ཆོས་དང་བྲལ་བས་ན་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་པ་དང་ཞེ་སྡང་བ་དང༌[^1059]བྲལ་བས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1246]
རང་བཞིན་གྱིས་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པས་ན་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་ཉོན་མོངས་པའི་དྲི་མ་དང་མ་འདྲེས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1247]
དེ་དག་གི་མིག་དེ་ནི་བསམ་པ་མ་བསྟན་པ༌[^1060]ཞེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་བསམ་པ་དང་མ་བྲལ་བས་ན། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་སྤྱན་ཐམས་ཅད་མཁྱེན་པའི་རང་བཞིན་ལས་སྐྱེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1248]
རྗེས་སུ་ཆགས་པ་དང་ཁོང་ཁྲོ་བ་དང་བྲལ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་ཆགས་པ་དང་བྲལ་བས་ན་མ་ཆགས་པའོ། །

[Block 1249]
དེ་དག་གི་མིག་དེ་ནི་དོན་གྱི་སྤྱོད་ཡུལ་བདེན་པས་ཉེ་བར་བསྒྲུབས་ཤིང་ཆོས་རྣམ་པར་དག་པ་ཤེས་པའི་ལམ་ལ་མ་ཆགས་པར་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཕྱིན་ཅི་ལོག་གི་དོན་ལ་དམིགས་པ་ལས་བྱུང་བ་ནི་མ་ཡིན་གྱིས།[^1061] དོན་དམ་པའི་བདེན་པ་ཕྱིན་ཅི་མ་ལོག་པ་ལ་དམིགས་པ་ལས་བྱུང་བས་ན་ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པ་ཤེས་པར་བྱ་བ་ལ་ཐགས༌[^1062]ཐོགས་མེད་པར་སྤྱོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1250]
མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་མ་གོས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1251 [HEADING]]
#### རྒྱུ་རྣམ་པར་དག་པ། ^3-1-4-0

[Block 1252]
རྒྱུ་བསྟན་པའི་ཕྱིར། དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་ལྷའི་མིག་དེ་ཅིའི་ཕྱིར་གོང་དུ་བཤད་པ་ལྟ་བུ་ཡིན་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1253]
སྐྱེས་བུ་དམ་པ་དེ་དག་ནི་སྙིང་རྗེ་ཆེན་པོ་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། སྙིང་རྗེ་ཆེན་པོ་ལ་གནས་པའི་རྒྱུ་ལས་བྱུང་བས་ན་དེ་དག་གི་ལྷའི་མིག་ཀྱང་གོང་དུ་བཤད་པ་ལྟ་བུའི་ཡོན་ཏན་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1254]
ཚིག་ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1255]
ཆོས་རྣམས་རིག་པ་ནི་བཤད་པར་བྱ་བའི་ཆོས་ཐམས་ཅད་རིག་པའོ། །

[Block 1256]
དོན་ཤིན་ཏུ་རྟོགས་པ༌[^1063]ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཁོང་དུ་ཆུད་པའོ། །

[Block 1257]
ཁ་ན་མ་ཐོ་བ་མེད་པ་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་བྱེད་པས་སོ། །

[Block 1258]
ཇི་ལྟར་མཐོང་བ་དང་ཐོས་པ་བཞིན་དུ་ཆོས་སྨྲ་བ་ནི་ཇི་ལྟར་མཐོང་བ་དང་ཐོས་པ་ལས་སྐྱེད་སྐུར་བྱས་ཏེ། སྒྲོ་མི་འདོགས་པ་དང་སྐུར་བ་མི་བྱེད་པས་སོ། །

[Block 1259]
མི་དགེ་བ་མི༌[^1064]བསྙིལ་པ་ནི་མི་དགེ་བའི་སྤྱོད་པ་རྣམ་པ་ཐམས་ཅད་དུ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1260]
བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་མངོན་དུ་ཕྱོགས་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ༌[^1065]ཐོབ་པར་བྱ་བ་ལ་གཅིག་ཏུ་མོས་ཤིང་སྒྲུབ་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 1261]
སེམས་གོང༌[^1066]དུ་ཡང་ཐོགས་པ་མེད་ཅེས་བྱ་བ་ནི་དེའི་སེམས་ཀྱི་དངོས་པོ་ཐམས་ཅད་མ་ལུས་པར་ཤེས་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1262]
བརྩོན་འགྲུས་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ལ་འཇོག་པར་བྱེད་པའོ། །

[Block 1263]
བསམ་གཏན་གྱི་ཡན་ལག་སྟོན་པ་ཞེས་བྱ་བ་ནི་བསམ་གཏན་དང་པོ་དང་གཉིས་པ་ལ་སོགས་པ་སྒོམ་པའི༌[^1067]ཐབས་སྟོན་པའོ། །ཤེས་རབ་ཀྱི་མིག༌[^1068]སྦྱིན་པ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའི༌[^1069]ཤེས་རབ་ཀྱི་མིག་སྦྱིན་པའོ། །

[Block 1264]
ལམ་ངན་པ་ལ་ཞུགས་པ་ནི་མུ་སྟེགས་ཅན་རྣམས་སོ། །

[Block 1265]
ལམ་སྟོན་པ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་སྟོན་པའོ། །
--- END BLOCKS ---
