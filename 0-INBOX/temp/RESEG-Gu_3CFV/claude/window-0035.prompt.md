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
དུས་བྱིན་གྱིས་མ་བརླབས་པའམ་ན་བའི་དབང་ཉིད་དུ་གནས་པ་མ་ཡིན་པའི་རང་ངམ་བསྒོ་བས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1227]
མེ་སྦར་ཏམ༌[^746]གསོད་དམ༌[^747]མེས་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེས་མ་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེ་དང་བཅས་པའི་བུད་ཤིང་འདྲེན་ཏམ་བསྐུལ་ཏམ། མདག་མ་སྤུངས་སམ༌[^748]འབྲུ་བར་བྱེད་པ་འདི་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1228]
འདིར་གཞུང་ནི་དགེ་སློང་མེ་སྦར་བར་བྱེད་ན་དེས་དུས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1229]
བྱིན་གྱི༌[^749]མ་བརླབས་པར༌[^750]སྦར་བར་བྱེད་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1230]
སྦར་ཏམ༌[^751]གསོད་པ་དག་ལ་ནི་འདི་ཡིན་ཏེ། བུད་ཤིང་མེས་རེག་པ་བསྐུལ་ཏམ། མས༌[^752]མ་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེ་དང་བཅས་ཤིང་འབྲེལ་པའི་བུད་ཤིང་ཕྱིར་དྲངས་སམ། མདག་མ་དག་སྤུངས་སམ་དེ་བཞིན་དུ་མགལ་བར་སྐུལ༌[^753]བར་བྱེད་དམ། མགལ་བ་འདྲེན་པར་བྱེད་དམ། ཤིང་འཛུད་པར་བྱེད་ན་ཐམས་ཅད་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1231]
མེས་མ་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ་ཞེས་བྱ་བ་གཞན་ཀློག་པ་འདི་བུད་ཤིང་བསྐུལ་བར་གྱུར་ན་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་སྨོས་པ་དང་། འདིར་རང་གིས་བསྐུལ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་དང་། འདིར་གཞན་ལ་བསྒོ་བ༌[^754]ཞེས་བྱ་བ་མདོའི་ཚིག་ལས་རྟོགས་པར༌[^755]བྱའོ། །

[Block 1232]
མེ་མ༌[^756]མུར་ནི་ཕྱེད་ཤི་བ་ཉིད་དོ་ཞེས་བྱ་བ་ཉེས་བྱས་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1233]
འདིར་གཞུང་ནི་མེ་མ༌[^757]མུར་ལ་རེག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1234]
མེ་ལྕེ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས༌[^758]ནི་ཕྱེད་ཤི་བ་ཉིད་ཅེས་བྱ་བའི་རྗེས་སྙེགས༌[^759]པའི་ཕྱིར་སྨོས་སོ། །

[Block 1235]
འདིར་གཞུང་ནི་མེ་མ༌[^760]མུར་ལ་རེག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1236]
འདིར་གང་ཞིག་མེ་མ༌[^761]མུར་དང་མེ་ལྕེ་རྣམས་ལ་དེར་བུད་ཤིང་འཛུད་པ༌[^762]དང་འབྱིན་པ་ནི་མེ་གཞན་གྱི་ཉེས་པ་ཁོ་ན་ཡིན་གྱི་དེར་ཅི་ཞིག་འདིར་བྱས་པས་ཉེས་བྱས་སུ་རྟོགས་པར་བྱ་ཞེས་བྱ་བ་འདིར་སྟོན་པ་ནི་དེར་བུད་ཤིང་འཇུག་པ་དང་འབྱིན་པ་ནི་མེ་གཞན་གྱི༌[^763]ཉེས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མེ་གཞན་དུ་འཛུད་པ་ནི་འདི་ཡིན་ཏེ། མེ་མ༌[^764]མུར་དང་མེ་ལྕེའི་འཇུག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1237]
དེ་ལྟ་བས་ན་དེའི་དབང་གིས་འདིར་ལྟུང་བ་འབྱུང་བ་མ་ཡིན་ནོ། །

[Block 1238]
མེ་གཞན་གྱི་དབང་ཁོ་ནར་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1239]
འདིར་འཛུད་པ་ལ་ནི་ལྟུང་བྱེད་དུ་ཤེས་པར་བྱའོ། །

[Block 1240]
སྐྲ་དང་ཁ༌[^765]སྤུ་དང་སེན་མོ་དང་མཆིལ་མ་དང་སྣབས་དང་སྐྱུགས་པ་དང་རླུགས་པ་དང་། མོན་སྲན་སྡེའུ་དང་། མོན་སྲན་གྲེའུ་དང་ཏིལ་དང་འབྲུ་མར་དང་སྦྲང་རྩི་དང་མར་དག་ནི་བུད་ཤིང་གི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་ཤིང་གི་ཕྱེད་དུ་གྱུར་པ་འདི་རྣམས་ལ་ནི་ཉེས་བྱས་ཏེ། འདི་རྣམས་ལ༌[^766]ནི་འཇོག་པ་དང་འདོན་པ༌[^767]དག་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1241]
ཀློག་པ་ཁ་ཅིག་ལས་དགེ་སློང་གིས་མེའི་ནང་དུ་སྐྲ་དང་སྤུ་དང་རུས་པ་དང་སེན་མོ་དག་འཇུག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1242]
གཞན་དུ་ན་ཡང་མེའི་ནང་དུ་མཆིལ་མ་དང་སྣབས་དང་སྐྱུགས་པ་དང་རླུགས་པ་དག་འཛུད་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་དང་། ཞུ་བ་ལས་ཀྱང་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ཏིལ་མར་དང་མོན་སྲན་སྡེའུ་དང་། མོན་སྲན་གྲེའུ་ཞུགས་སུ་གསོལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ། །

[Block 1243]
ཀློག་པ་ཁ་ཅིག་ལས་བཙུན་པ༌[^768]རེ་ཞིག་དགེ་སློང་གིས་མར་དང་འབྲུ་དང་སྦྲང་རྩི་ཞུགས་སུ་སྩོལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས༌[^769]བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1244]
དེ་བཞིན་དུ་རུས་པ་དང་མཆིལ་མ་བསྲེགས༌[^770]ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན༌[^771]ཏེ། དེ་དག་ནི་བསྡུས་ནས་སྨྲས་སོ། །

[Block 1245]
དེ་དག་ཀྱང་དཔེ་ཙམ་དུ་ཟད་དེ་རྩྭ་དང་ཤིང་དང་རས་བལ་དང་བལ་དུ་གྱུར་པ་ཡང་དེ་དང་འདྲ་བར་བཅས་པའི་ཆོས་ཅན་ནོ། །

[Block 1246]
གཞན་གྱི་བྱ་བ་གཞན་ལ་བྱིན་གྱིས་རློབ་པ༌[^772]ནི་ཕྱེད་བྱིན་གྱིས་བརླབས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་ནི་དོན་ཇི་ལྟ་བར་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ན་སྨད་པ་ཡིན་ནོ། །

[Block 1247]
འདིར་གཞུང་ལ་ལ་དག་ལས་ནི་འདི་སྐད་ཅེས་དགེ་སློང་གིས༌[^773]མཁན་པོའི་བྱ་བ་ལ་མེ་ལ་རེག་ཅིང་སློབ་དཔོན་ལ་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 1248]
ཆོས་ཀྱི་བྱ་བས་དགེ་འདུན་ལ་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 1249]
ཐམས་ཅད་ཕྱིན་ཅི་ལོག་ཏུ་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1250]
མེ་ལ་རེག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1251]
ཅི་ཞིག་བྱས་ན་དད་པ་ཕྱིར་བསྒྱུར་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གི་དོན་གྱི་ཆེད་ཀྱི་ལས་བྱས་པ་ལ་དད་པ་ཕུལ་བའི་ཕྱིར་བསྒྱུར་བའི་ཕྱིར་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་སྟེ། དགེ་སློང་དང་འབྲེལ་པའི་དོན་གྱིས་དགོས་པ་གང་ཡིན་པ་དེ་ནི་དགེ་སློང་གི་དོན་ཏོ། །

[Block 1252]
དོན་དེའི་ཕྱིར་ལས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་དགེ་སློང་གི་དོན་ཆེད་དོ། །

[Block 1253]
དོན་གྱི་ཆེད་དེ་ལ་གསོལ་བ་དང་བརྗོད་པ་དང་དགག་དབྱེ་དང་བསྒོ་བའི་བདག་ཉིད་ཀྱིས༌[^774]ལས་བྱས་པ་གང་ཡིན་པ་དེ་དོན་གྱི་ཆེད་ཀྱི༌[^775]ལས་སོ། །

[Block 1254]
ལས་དེ་བྱས་པ་ལ་ཞེས་བྱ་བ་ནི་བྱས་ཟིན་པ་ལའོ། །

[Block 1255]
ལས་བྱས་པ་དེ་ལ་དད་པ་ཕུལ་བ་ཕྱིར་བསྒྱུར་བའི་ཕྱིར་སྨྲས་པ་ནི་དགེ་སློང་དད་པ་སླར་བྱིན་ཅིག །ཁྱོད་ལ་མི་སྦྱིན་ནོ་ཞེས་དེ་སྐད༌[^776]ཟེར་ཞིང་ཕྱིར་འཕྲོག་པ་སྟེ། དེ་བས་ན་དད་པ༌[^777]ཕྱིར་བསྒྱུར་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1256]
ཚོགས་པ་འདི་འཇིག་པ༌[^778]དགེ་འདུན་འབྱེད༌[^779]པ་ཞེས་བྱ་བའི༌[^780]ཁ་ན་མ་ཐོ་བའོ། །

[Block 1257]
དད་པ་ཕྱིར་བསྒྱུར་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1258]
ཟླ་བ་དང་ཉི་མ་མ་གཏོགས་པའི་སྣང་བ་དང་བཅས་པའི་གནས་ཀྱི་ཕྱོགས་སུ་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཟླ་བ་དང་ཉི་མ་དག་མ་གཏོགས་པའི་སྣང་བ་ཟླ་བ་དང་ཉི་མ་དག་ལས་གཞན་པའི་སྣང་བ་ཁྱིམ་གྱི་ཕྱོགས་གང་ན་ཡོད་པ་དེར་རོ། །

[Block 1259]
ཁྱིམ་དེ་ནི་དེར་གང་ཞིག་སླར་བཀབ་པ་དང་ཡོངས་སུ་བསྐོར་བ་ཁྱིམ་གྱི་ཐ་མར་ཞེས་བྱ་བ་འདི་འཇུག་པས་ཁྱིམ་འདིའི་ངོ་བོ་རིག་པར་བྱའོ། །

[Block 1260]
འདི་ཕྱོགས་ཀྱི་ཚིག་ནི་ཕྱོགས་གང་ན་སྣང་བ་མེད་པ་དེར་ཉལ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 1261]
ཕྱོགས་དེ་ལས་གཞན་དུ་ནི་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་འདི་བསྒྲུབ་པའི་དོན་དུའོ། །

[Block 1262]
འོ་ན་འདི་ལྟར་སྣང་བ་དང་བཅས་པ་ཉིད་ལ་ཕྱོགས་གཅིག་ཏུ་སྣང་བ་དང་བྲལ་བའི་ཕྱོགས་ལ་སྣང་དུ་རུང་བ་ཉིད་ཡོད་དོ་ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་འདི་ནི་ལོངས་སྤྱོད་ཅན་གྱི་ཡོ་ལང་སྤང་བའི་ཕྱིར་ཡིན་གྱི། ལྟ་བའི་ཕྱིར་བཀག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
འདིར་གླེང་གཞི་ནི་གཙོ་བོ་མ་ཡིན་ཏེ། ཟླ་བ་དང་ཉི་མ་དག་ལས་སྤང་བ་མ་ཡིན་པ་ཉིད་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1264]
ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པ་ལས་འདའ་བར་བྱ་སྟེ། དེ་ཉལ་ན་མཚན་མོའི་མཐར་ནི་དངོས་གཞིར་འགྱུར་བའི་ཉེས་བྱས་སོ། །

[Block 1265]
མདུན་རོལ་དུ་ནི་སྦྱོར་བར་འགྱུར་བའི་ཞེས་བྱ་བ་འདི་འདིར་རྟོགས་པར་བྱའོ། །ཅི་རྣམ་པ་ཐམས་ཅད་ཉིད་ཀྱིས་དེ་ལྟ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ནད་པ་དང་། ནད་གཡོག་གི་དབང་ཉིད་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནད་པའི་དབང་ཉིད་དང་ནད་གཡོག་གི་དབང་ཉིད་ཀྱིས་དེར་ཉལ་བ་ནི་མ་གཏོགས་སོ། །
--- END BLOCKS ---
