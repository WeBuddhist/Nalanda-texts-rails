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
གང་དག་སེམས་ཐམས་ཅད་ལ་འབྱུང་བ་དེ་དག་ཀྱང༌[^536]གང་ཞེ་ན།

[Block 1227 [VERSE]]
ཚོར་དང་སེམས་པ་འདུ་ཤེས་དང་། །
འདུན་དང་རེག་དང་བློ་གྲོས་དྲན། །
ཡིད་ལ་བྱེད་དང་མོས་པ་དང་། །
ཏིང་ངེ་འཛིན་སེམས་ཐམས་ཅད་ལ། །

[Block 1228]
ཆོས་བཅུ་པོ་འདི་དག་ནི་སེམས་ཀྱི་སྐད་ཅིག་མ་ཐམས་ཅད་ལ་ཚོགས་པར་འབྱུང་ངོ་ཞེས་གྲག་གོ་ལོ།[^537] །དེ་ལ་ཚོར་བ་ནི་མྱོང་བ་རྣམ་པ་གསུམ་སྟེ། བདེ་བ་དང་། སྡུག་བསྔལ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^538]ཡང་མ་ཡིན་པའོ། །

[Block 1229]
སེམས་པ་ནི་སེམས་མངོན་པར་འདུ་བྱེད་པའོ། །

[Block 1230]
འདུ་ཤེས་ནི་འདུས་ནས་ཤེས་པ་སྟེ། ཡུལ་ལ་མཚན་མར་འཛིན་པའོ། །

[Block 1231]
འདུན་པ་ནི་བྱེད་འདོད་པའོ། །

[Block 1232]
རེག་པ་ནི༌[^539]ཡུལ་དང་དབང་པོ་དང་རྣམ་པར་ཤེས་པ་འདུས་པ་ལས་སྐྱེས་པའི་རེག་པའོ། །

[Block 1233]
བློ་གྲོས་ནི་ཤེས་རབ་སྟེ། ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པའོ། །

[Block 1234]
དྲན་པ་ནི་དམིགས་པ་མི་བརྗེད་པའོ། །

[Block 1235]
ཡིད་ལ་བྱེད་པ་ནི་སེམས་ཀྱི་འཇུག་པའོ། །

[Block 1236]
མོས་པ་ནི་འདོད་པའོ། །

[Block 1237]
ཏིང་ངེ་འཛིན་ནི་སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 1238]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་བྱེ་བྲག་ནི་ཕྲ་བས་དེ་ནི་རེ་ཞིག་རྒྱུན་རྣམས་ལ་ཡང་ཡོངས་སུ་གཅད་པར་དཀའ་ན་སྐད་ཅིག་མ་དག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། རེ་ཞིག་སྨན་ལ་སོགས་པ་གཟུགས་ཅན་རྣམས་ལ་ཡང་རོ་མང་པོ་ཁ་ཅིག་གི་རོའི་ཁྱད་པར་དབང་པོས་གཟུང་བར་བྱ་བ་རྣམས་ངེས་པར་གཟུང་བར་དཀའ་ན། ཆོས་གང་དག་གཟུགས་ཅན་མ་ཡིན་ཞིང་བློས་གཟུང་བར་བྱ་བ་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས།

[Block 1239 [HEADING]]
###### དགེ་བའི་ས་མང་པོ་པ། ^2-2-2-1-2-0

[Block 1240]
འདི་དག་ལ་དགེ་བའི་ས་མང་པོ་ཡོད་པས་འདི་དག་ནི་དགེ་བའི་ས་མང་པོ་པ་དག་ཡིན་ཏེ། གང་དག་དགེ་བའི་སེམས་ལ་རྟག་ཏུ་འབྱུང་བའོ། །

[Block 1241]
དེ་དག་ཀྱང་གང་ཞེ་ན།

[Block 1242 [VERSE]]
དད་དང་བག་ཡོད་ཤིན་ཏུ་སྦྱངས། །
བཏང་སྙོམས་ངོ་ཚ་ཤེས་ཁྲེལ་ཡོད། །
རྩ་བ་གཉིས་རྣམ་མི་འཚེ་དང་། །
བརྩོན་འགྲུས་རྟག་ཏུ་དགེ་ལས་འབྱུང་། །

[Block 1243]
ཆོས་འདི་དག་ནི་དགེ་བའི་སེམས་ལ་རྟག་ཏུ་འབྱུང་ངོ་། །དེ་ལ་དད་པ་ནི་སེམས་དང་བའོ། །

[Block 1244]
གཞན་དག་ན་ནི་བདེན་པ་དང་དཀོན་མཆོག་དང་ལས་དང་འབྲས་བུ་རྣམས་ལ་མངོན་པར་ཡིད་ཆེས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1245]
བག་ཡོད་པ་ནི་དགེ་བའི་ཆོས་རྣམས་བསྒོམ༌[^540]པའོ། །

[Block 1246]
དེ་དག་ལས་གཞན་པ་བསྒོམ་པ་དེ་གང་ཞིག་ཡིན་ཞེ་ན། དེ་དག་ཉིད༌[^541]ལ༌[^542]གཅེས་སུ་འཛིན་པ་ཉིད་གང་ཡིན་པའོ། །

[Block 1247]
སྡེ་བ་གཞན་དག་གི་མདོ་ལས་ནི་སེམས་ཀུན་ཏུ་བསྲུང་བའོ་ཞེས་འདོན་ཏོ། །

[Block 1248]
ཤིན་ཏུ་སྦྱངས་པ་ནི་སེམས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 1249]
མདོ་ལས་ལུས༌[^543]ཤིན་ཏུ་སྦྱངས་པ་ཞེས་ཀྱང་གསུངས་པ་མ་ཡིན་ནམ་ཞེ་ན། མ་གསུངས་པ༌[^544]ནི་མ་ཡིན་མོད་ཀྱི་དེ་ནི་ལུས་ཀྱི་ཚོར་བ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1250]
དེ་ཇི་ལྟར་ན་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ་རུང་བར་འགྱུར་ཞེ་ན། འོ་ན་དེར་ནི་ལུས་ལས་སུ་རུང་བ་ཁོ་ན་ལ༌[^545]ལུས་ཤིན་ཏུ་སྦྱངས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1251]
དེ་ཇི་ལྟར་ན་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱ་ཞེ་ན། བྱང་ཆུབ་ཀྱི་ཡན་ལག་དག་མཐུན་པའི་ཕྱིར་ཏེ། ལུས་ལས་སུ་རུང་བ་དེ་ནི་སེམས་ལས་སུ་རུང་བ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་འདྲེན་པར་བྱེད་དོ། །

[Block 1252]
དེ་ལྟ་བུ་གཞན་ལ་ལར་སྣང་བ་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དེ། དཔེར་ན་བཅོམ་ལྡན་འདས་ཀྱིས་དགའ་བ་དང་དགའ་བའི་གནས་ལྟ་བུའི་ཆོས་རྣམས་དགའ་བ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ་གསུངས་པ་དང་། ཁོང་ཁྲོ་བ་དང་ཁོང་ཁྲོ་བའི་རྒྱུ་མཚན་གནོད་སེམས་ཀྱི་སྒྲིབ་པར་གསུངས་པ་དང་། ཡང་དག་པའི་ལྟ་བ་དང་རྟོག་པ་དང་རྩོལ་བ་རྣམས་ཤེས་རབ་ཀྱི་ཕུང་པོར་གསུངས་པ་དག་ལྟ་བུ་སྟེ། རྟོག་པ་དང་རྩོལ་བ་དག་ཤེས་རབ་ཀྱི་རང་བཞིན་མ་ཡིན་ཡང་དེ་དང་མཐུན་པའི་ཕྱིར་དེའི་སྒྲ་འཐོབ་བོ། །

[Block 1253]
དེ་བཞིན་དུ་ལུས་ཤིན་ཏུ་སྦྱངས་པ་ཡང་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་མཐུན་པའི་ཕྱིར། བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱ་བའི་སྒྲ་འཐོབ་པར༌[^546]འགྱུར་རོ། །

[Block 1254]
བཏང་སྙོམས་ནི་སེམས་མཉམ་པ་ཉིད་དང་། སེམས་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དོ། །

[Block 1255]
ད་ནི་ཇི་ལྟར་ན་སེམས་དེ་ཉིད་ལ་རྩོལ་བའི་བདག་ཉིད་ཡིད་ལ་བྱེད་པ་ཡང་འབྱུང་། རྩོལ་བ་མེད་པའི་བདག་ཉིད་བཏང་སྙོམས་ཀྱང་འབྱུང་ཞེས་བྱ་བ་འདི་རུང་བར་འགྱུར་ཞེ་ན། འདི་དག་གི་བྱེ་བྲག་ནི་ཤེས་པར་དཀའོ་ཞེས་བཤད་པ་མ་ཡིན་ནམ། ཤེས་པར་དཀའ་བ་ཡང་ཤེས་པ་ནི་ཡོད་ཀྱི། གང་འགལ་བཞིན་དུ་ཡང་མི་འགལ་ལོ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ཤེས་པར་དཀའོ། །

[Block 1256]
རྩོལ་བ་ཡང་གཞན་དུ་འབྱུང་ལ། རྩོལ་བ་མེད་པ་ཡང་གཞན་དུ་འབྱུང་ངོ་ཞེས་བྱ་བ་འདི་ལ་འགལ་བ་ཅི་ཡོད་ཅེ་ན། འོ་ན་ནི་མཚུངས་པར་ལྡན་པ་ཐམས་ཅད་དམིགས་པ་གཅིག་ཏུ་མི་འགྱུར་རོ།[^547] །འདི་ལས་འདི་ལྟ་བུའི་རིགས་གཞན་ཡང་འབྱུང་བར་འགྱུར་བས་ངང༌[^548]ཚུལ་གང་ཡིན་པ་དེ་འདི་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 1257]
ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 1258]
རྩ་བ་གཉིས་ནི་དགེ་བའི་རྩ་བ་གཉིས་པོ་ཆགས་པ་མེད་པ་དང་། ཞེ་སྡང་མེད་པ་དག་ཡིན་ནོ། །

[Block 1259]
གཏི་མུག་མེད་པ་ཡང་ཡོད་མོད་ཀྱི་དེ་ནི་ཤེས་རབ་ཀྱི་བདག་ཉིད་ཡིན་ལ། ཤེས་རབ་ནི་ས་མང་པོ་པ་ཡིན་པས་འདི་དགེ་བའི་ས་མང་པོ་པ་ཁོ་ན་ཡིན་པར་ནི་མི་བརྗོད་དོ། །

[Block 1260]
རྣམ་པར་མི་འཚེ་བ་ནི་རྣམ་པར་ཐོ་མི་འཚམས༌[^549]པའོ། །

[Block 1261]
བརྩོན་འགྲུས་ནི་སེམས་མངོན་པར་སྤྲོ་བའོ། །

[Block 1262]
དགེ་བའི་ས་མང་པོ་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 1263]
ས་མང་པོ་ནི་ས་མང་བ་ཡིན་ནོ། །

[Block 1264 [HEADING]]
###### ཉོན་མོངས་པའི་ས་མང་པོ་པ། ^2-2-2-1-3-0

[Block 1265]
འདི་དག་ལ་ཉོན་མོངས་པའི་ས་མང་པོ་ཡོད་པས། འདི་དག་ནི་ཉོན་མོངས་པའི་ས་མང་པོ་པ་དག་ཡིན་ཏེ། ཆོས་གང་དག་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ལ་རྟག་ཏུ་འབྱུང་བ་ཡིན་ནོ། །
--- END BLOCKS ---
