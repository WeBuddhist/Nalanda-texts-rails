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
བརྟན་པ་དང་ལྡན་པ་པ༌[^792]དང་། བརྩོན་འགྲུས་དང་ལྡན་པ་དང་། སྤྲོ་བ་ཅན་དང་། ཕ་རོལ་གནོན་པ་བརྟན་པ་དང་། བླངས་པ་མི་འདོར་ཞིང་ཞེས་གསུངས་པའི་ཚིག་དེ་དག་བརྩོན་འགྲུས་ཀྱི་ལུས་རྣམ་པར་གཞག་པ་གསུམ་དང་སྦྱར་བར་བྱའོ། །

[Block 1227]
དེ་ལ་གོ་ཆའི་བརྩོན་འགྲུས་ནི་བརྟན་པ་དང་ལྡན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1228]
དང་པོར་སྦྱོར་བའི་བརྩོན་འགྲུས་ནི་བརྩོན་འགྲུས་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1229]
སྦྱོར་བའི་དུས་སུ་མི་ཞུམ་པ་དང་། མི་འཁྲུགས་པ་དང་། ཆོག་པར་མི་འཛིན་པ་ཞེས་བྱ་བ་དག་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྤྲོ་བ་ཅན་དང་། ཕ་རོལ་གནོན་པ་བརྟན་པ་དང་། བླངས་པ་མི་འདོར་བ་ཞེས་བྱ་བ་འདི་དག་གིས་བསྟན་པ་ཡིན་ནོ། །

[Block 1230]
གང་གི་ཕྱིར་གང་དག༌[^793]དང་པོར་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་དོན་དུ་བརྟན་པ་དང་ཡང་ལྡན་ལ། སྦྱོར་བའི་དུས་སུ་བརྩོན་འགྲུས་དང་ལྡན་དུ་ཟིན་ཀྱང་སེམས་ཞུམ་པར་གྱུར་ན་མ་ཡིན་པས་དེ་ལྟ་བས་ན་དེའི་གཉེན་པོར་སྤྲོ་བ་ཅན་ཏེ། གང་སེམས་སྤྲོ་བ་དང་ལྡན་པ་དེ་སེམས་ཞུམ་པར་མི་འགྱུར་ཏེ། ཞུམ་པ་ནི་འདིར་སེམས་འགོང་བའི་བདག་ཉིད་དུ་འདོད་དོ། །

[Block 1231]
སེམས་ཞུམ་པ་མེད་དུ་ཟིན་ཀྱང་འཁྲུགས་པར་གྱུར་ན་སངས་རྒྱས་ཉིད་ལས་ལྡོག་པར་འགྱུར་བས་དེས་ན་དེའི་གཉེན་པོར་མི་འཁྲུགས་པའི༌[^794]བརྩོན་འགྲུས་བསྟན་ཏེ། དེ་ཡང་ཕ་རོལ་གནོན་པ་བརྟན་པ༌[^795]ཞེས་བྱ་བས་ཕ་རོལ་གནོན་པ་བརྟན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1232]
འདི་ལྟར་ཕ་རོལ་གནོན་པ་བརྟན་པ་ཉིད་ནི་སྡུག་བསྔལ་གྱིས་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 1233]
སྡུག་བསྔལ་གྱིས་ལྡོག་པར་མི་འགྱུར་དུ་ཟིན་ཀྱང་གང་ཉུང་ཟད་ཀྱིས་ཆོག་པར་འཛིན་ན་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་མི་འགྱུར་བས། དེའི་ཕྱིར་ཆོག་པར་མི་འཛིན་པའི་བརྩོན་འགྲུས་ཞེས་བྱ་བར་ཡང་བསྟན་ཏེ། ཅུང་ཟད་ཀྱིས་ཆོག་པར་མི་གཟུང༌[^796]ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1234]
དེ་ཡང་བླངས་པ་མི་འདོར་བ་ཞེས་བྱ་བ་འདིས་བསྟན་ཏེ། དོན་དེ་དག་ཉིད་ཀྱིས་ནི་བརྩོན་འགྲུས་རྣམ་པ་གསུམ་བཤད་པ་ཡིན་ནོ། །

[Block 1235 [HEADING]]
#### བསམ་གཏན། ^4-6-5-0

[Block 1236]
ཡང་གནས་པའི་བསམ་གཏན་ནི་གང་གིས་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པས་གནས་པའོ། །

[Block 1237]
མངོན་པར་སྒྲུབ་པ་ནི༌[^797]གང་གིས་མངོན་པར་ཤེས་པ་དྲུག་མངོན་པར་བསྒྲུབ༌[^798]པའོ། །

[Block 1238]
བྱ་བ་སྒྲུབ་པའི་བསམ་གཏན་ཞེས་བྱ་བ་ནི་གང་བསམ་གཏན་ལ་བརྟེན་ནས་སེམས་ཅན་གྱི་དོན་བྱེད་པ་སྟེ། དེ་ནི་བྱ་བ་སྒྲུབ་པའི་བསམ་གཏན་ནོ། །

[Block 1239]
བསམ་གཏན་རྣམ་པ་གསུམ་གྱི་དོན་ནི་དེ་དག་ཉིད་དོ། །

[Block 1240 [HEADING]]
#### ཤེས་རབ། ^4-6-6-0

[Block 1241]
ཤེས་རབ་ཀྱི་ལུས་རྣམ་པར་གཞག་པ་གསུམ་གྱི་དོན་ནི་གོ་སླའོ། །

[Block 1242 [HEADING]]
### བསྡུས་པ། ^4-7-0

[Block 1243]
འདི་དག་བསྡུས༌[^799]པར་ཇི་ལྟར་བལྟ་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་དག་གིས་དགེ་བའི་ཆོས་རྣམས་ཇི་ལྟར་བསྡུ་ཞེས་བལྟ་བར་བྱའོ། །

[Block 1244]
གང་གི༌[^800]ཕྱིར་དེ་དག་ཏུ་འདི་དག་བསྡུས་པའི་ཕྱིར་འདི་དག་ཏུ་ཡང་དེ་དག་བསྡུས་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1245]
འདི་དག་གིས་དགེ་བའི་ཆོས་ཐམས་ཅད་བསྡུས་ཞེས་བྱ་བ་ནི་འདིར་དགེ་བའི་ཆོས་ཐམས་ཅད་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་སུ་འདོད་དོ། །

[Block 1246]
དེའི་མཚན་ཉིད་ཅེས་བྱ་བ་ལ། དེའི་མཚན་ཉིད་ནི་ཤེས་རབ་བོ། །

[Block 1247]
དེའི་རྒྱུ་མཐུན་པ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཇི་ལྟར་མངོན་པར་ཤེས་པ་དང་། སྟོབས་བཅུ་ལ་སོགས་པའི་ཡོན་ཏན་གཞན་དག་གི་ཡང་རྒྱུར་མཐུན་པར་གྱུར་པའོ། །

[Block 1248]
དེ་དང་མཐུན་པ་ཞེས་བྱ་བ་ནི་དད་པ་ལ་སོགས་པ་ནི་དེ་དང་མཐུན་པར་བལྟ་བར་བྱ་སྟེ། གང་ཡང་དཀར་པོའི་ཆོས་རྣམས་ཐམས་ཅད་ཡང་དག་པར་བསྡུས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་དེས་བསྟན་ཏོ། །

[Block 1249 [HEADING]]
### མི་མཐུན་པའི་ཕྱོགས། ^4-8-0

[Block 1250]
དེ་དག་གི་མི་མཐུན་པའི་ཕྱོགས་རྣམས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་ཐམས་ཅད་ཇི་ལྟར་བསྡུས་པ་དེ་བསྟན་པར་བྱའོ། །

[Block 1251]
དེ་ལ་དེའི་མཚན་ཉིད་དེ་ཞེས་བྱ་བ་ནི་དེའི་མཚན་ཉིད་འདོད་ཆགས་པ༌[^801]ལ་སོགས་པ་དག་གོ། །

[Block 1252]
དེའི་གཞི་ཞེས་བྱ་བ་ནི་གཞི་སྟེ། ཇི་ལྟར་སེར་སྣའི་གཞི་དང་། མ་དད་པ་ཉིད་དང་། ལྟ་བ་ལོག་པ༌[^802]ལ་སོགས་པའོ། །

[Block 1253]
དེའི་འབྲས་བུ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སེར་སྣ་དང་། འཆལ་བའི་ཚུལ་ཁྲིམས་དང་། ཁྲོ་བ་ལ་སོགས་པའི་འབྲས་བུའོ། །

[Block 1254 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཕན་ཡོན། ^4-9-0

[Block 1255]
ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་དག་གི་ཕན་ཡོན་བསྟན་པར་བྱ་བ་ནི། ཁ་ན་མ་ཐོ་བ་མེད་པར་མངོན་པར་མཐོ་བ་སྟེ། ཇི་ལྟར་ཕྱི་རོལ་པའི་ལྟ་བུ་ནི་མ་ཡིན་ཏེ། དེ་དག་གི་མངོན་པར་མཐོ་བ་ཉིད་ཡིན་ན་ཡང་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པས་དམན་པ་ཉིད་ཡིན་པ་དང་། ཡང་དེ་དག་ནི་མི་རྟག་པ་ཉིད་ཡིན་པས་སོ། །

[Block 1256]
ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་ནི་མི་རྟག་པ་མ་ཡིན་ཏེ། བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་གནས་ཀྱི་བར་དུ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1257]
ཡང་དེ་ནི་བདག་འབའ་ཞིག་གི་དོན་ཡིན་གྱི། གཞན་གྱི་མ་ཡིན་པ་དེ་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་ནི་སེམས་ཅན་གྱི་དོན་བྱ་བར་ཉེ་བར་གནས་པ་ཞེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1258]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱི་འབྲས་བུའི་ཕན་ཡོན་ནི། ཁ་ན་མ་ཐོ་བ་མེད་པ་ལ་སོགས་པ་འདི་དག་ཡིན་ནོ། །

[Block 1259 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པ་གཅིག་བསྟན་པའི་དགོངས་པ། ^4-10-0

[Block 1260]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སུམ་བརྒྱ་པ་ལ་སོགས་པ་ལས་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཅིག་བསྟན་པར་བྱས་པ་དེར་གང་ཐམས་ཅད་བསྟན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེའི་དགོངས་པ་གང་ཡིན་ཞེ་ན། གཅིག་ལ་རབ་ཏུ་སྦྱོར་བ་ན༌[^803]ཐམས་ཅད་ཀྱི་བྱེད་པ་འགྲོ་བར་འགྱུར་རོ་ཞེས་དགོངས་པ་ཡིན་ནོ། །

[Block 1261]
དེ་ལ་སྦྱིན་པ་བྱེད་པ་ནི༌[^804]ལུས་དང་ངག་བསྡམས་ནས་སྦྱིན་པར་བྱེད་པ་ནི་དེའི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བྱེད་པ་ཡིན་ནོ། །

[Block 1262]
སྦྱིན་པའི་རྒྱུ་དང་འབྲས་བུ་ཤེས་པ་ཉིད་ནི་ཤེས་རབ་ཀྱི་བྱེད་པ་སྟེ། ལྷག་མ་རྣམས་ཀྱི་བྱེད་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1263 [HEADING]]
## དེའི་རྒྱུ་དང་འབྲས་བུའི་སྒོམ་པ་རབ་ཏུ་དབྱེ་བ། ^5-0

[Block 1264]
དེའི་རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་ལས་བརྩམས་པ་ནི་ཤེས་བྱ་ཆོས་ཀྱི་དབྱིངས་རྣམ་པ༌[^805]བཅུ་པོ་ཀུན་ཏུ་འགྲོ་བའི་དོན་དང་། གཟུངས་དང་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ལ་དབང་བའི་དོན་གྱི་བར་དུའོ། །

[Block 1265 [HEADING]]
### ཤེས་བྱ་ཆོས་ཀྱི་དབྱིངས་རྣམ་པ་བཅུ། ^5-1-0
--- END BLOCKS ---
