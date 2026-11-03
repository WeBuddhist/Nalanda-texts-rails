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
[Block 1296]
ཉེ་འཁོར་གྱི་རྣམ་པ་ཉིད་ཀྱིས་འདི་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ཤེས་པ་ཡིན་ཏེ་ཁྱེར་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1297]
ཁྱེར་གཞན་གྱིས་བར་དུ་ཆོད་པ་ནི། གང་ཞིག་འདི་ལ་བར་དུ་ཆོད་པ་ཉིད་དེ་ལ་ཉེ་འཁོར་གྱི་རྣམ་པ་ཉིད་དོ། །

[Block 1298]
དེ་བས་ན་འདི་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1299]
ཉེ་འཁོར་དང་བཅས་པ་ནས་གནས་ཁང་ཙམ་གྱི་ཕ་རོལ་ན་ཐ་དད་པར་གྱུར་ཅིང་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཉེ་འཁོར་དང་བཅས་པའི་གནས་ལ་ཚད་གང་ཡིན་པ་དེ་ཙམ་གྱི་བར་ནས་གཞན་ཐ་དད་པར་གྱུར་པ་གཅིག་གམ་དུ་མའི་གང་ཟག་གིས་ལྷག་པར་གནས་པ་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ནི་མ་ཡིན་ལ་གནས་ངེས་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1300]
གཡོགས་པ་གཅིག༌[^795]ཆ་ཅན་བཀབ་པ་འདི་ཡིན་ཏེ་ཞེས་བྱ་བ་འདིར་ཧ་ཅང་ཐལ་བས་གནས་གཅིག༌[^796]ཉིད་དུ་རྟོགས་པ་ཡིན་ནོ། །

[Block 1301]
འདིར་ཁུངས་ནི་འགྲོན་པ་ལས་ཕྱི་རོལ་དུ་འབྱུང་བར་མི་བྱ་བར་འདི་འདི༌[^797]ལྟར་འགྲོན་པ་དང་ཁོ་བོ༌[^798]གཉིས་སུ་གཅད༌[^799]དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1302]
གང་གི་ཕྱིར་འདི་ནི་མངོན་པར་སྐྱོབ་པའི་དབང་དུ་བྱས་པ་མ་ཡིན་ཏེ། འདི་ལ་ཉེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1303]
ཐ་དད་པར་གྱུར་པ་བསྙེན་པར་མ་རྫོགས་པ་ལྷག་པར་གནས་པ་ཉིད་ནི་འདིར་གཙོ་བོ་མ་ཡིན་ཏེ། དུ་མ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 1304]
དེ་ལྟ་བས་ན་གཅིག་ལ་ཡང་འདིར་འཕགས་པར་བྱས་པ་ཡིན་ནོ། །

[Block 1305]
ཤིང་ལྗོན་པའི་དྲུང་དང་རྩིག་པའི་བར་དང་ཚང་ཚིང་གི་དྲུང་དག་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1306]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་ཤིང་ལྗོན་པའི་དྲུང་དུ་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་མཆིས་ཤིང་ཉལ་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ། །

[Block 1307]
དེ་བཞིན་དུ་རྩིག་པའི་བར་དང་དེ་བཞིན་དུ་ཤིང་དྲུང་དག་ཏུ་ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་དུ་རིག་པར༌[^800]བྱའོ། །

[Block 1308]
མ་བསྐོར་བ་དང་མ་བཀབ་པ་དང་བསྐོར་བའི་སྣ་མ་ཕྲད་པ་དང་གཅིག་གམ་གཉིས་སམ་བསྐོར་བའི་སྣ་མ་ཕྲད་པ་དང་། བྱ་སྐྱིབས་དང་ཤིང་ལྗོན་པ་ལ་སོགས་པ་དག་ཀྱང་རྣམ་པ་འདི་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 1309]
གང་གི་ཕལ་ཆེར་སྐོར་བ༌[^801]མེད་པ་དེ་ནི་འདིར་བར་དུ་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 1310]
ཐིབས་པོ་དང་བཅས་པ་དག་བུད་མེད་དང་ལྷན་ཅིག་ཉལ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཐིབས་པོ་ཞེས་བྱ་བ་རྩྭའམ༌[^802]ནགས་སམ་འོད་མའམ་ཚེར་མ་ལ་སོགས་པ་དང་བཅས་པ་དག་གི༌[^803]ནང་དུ་བུད་མེད་དང་ལྷན་ཅིག་ཉལ་ཡང་ཉེས་བྱས་ཉིད་དེ་ཤིང་གི་རྩ་བ་གཅིག་པུར་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1311]
ཀུན་ནས་ཡོངས་སུ་བསྐོར་བ་ལ་ཡང་མ་གཡོགས་པ་དང་གསང་བར་གྱུར་པ་གཞན་དག་ཀྱང་འདིར་འཕངས་པར་རིག་པར་བྱའི། ཉེ་འཁོར་དང་བཅས་པ་གནས་པ༌[^804]ཙམ་ལས་གཞན་ཐ་དད་པར་གྱུར་པ་ལྷག་པར་གནས་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1312]
དེ་བུད་མེད་དང་ལྷན་ཅིག་ཉལ་བ་ལ་དམིགས་ཀྱིས་བསལ་བའི་བྱེ་བྲག་གང་ཞིག་བསྟན་པའི་ཕྱིར་འདི་ལ་ནི་བྱ་གག་འཕུར་ནས་བབ་པའི༌[^805]ལམ་གྱིས་བར་དུ༌[^806]ཆོད་པར་གྱུར་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱ་གག་འཕུར་ནས་བབ་པའི༌[^807]བར་གྱི་ལམ་གང་ཡིན་པ་དེ་ལ། འདིར་བུད་མེད་དང་ལྷན་ཅིག་བར་དུ་ཆོད་པར་གྱུར་པ་ཉིད་དོ། །

[Block 1313]
ཉེ་འཁོར་དང་བཅས༌[^808]ནས་གནས་ཁང་ཙམ་གྱི་ཕ་རོལ་ན་ནི་མ་ཡིན་ཏེ། དེ་ཙམ་གྱི་བར་ཆད་ཀྱིས༌[^809]བར་དུ་ཆོད་པ་མེད་པ་དང་བར་དུ་ཆོད་པ་ལ་བར་དུ་མི་རྒྱུ་བའི་དབང་གིས་གནས་གཅིག་པ་ཉིད་དུ་བརྟེན་པ་ཡིན་ནོ། །

[Block 1314]
ཐ་དད་པར་གྱུར་པ་ཉིད་དུ་ལྷག་པར་གནས་པ་ཐ་དད་པར་གནས་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་འདི་ནི་བྱེད་པ་པོའོ། །

[Block 1315]
ནང་དུ་གཅིག་ཏུ་རྒྱུ་ཞིང་བར་ན་གནས་གཞན་མེད་པ་མ་ཡིན་པ་ཉིད་ལ་ནི་གཡོགས་པ་ཐམས་ཅད་གཅིག༌[^810]པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བར་ན་གནས་གཞན་མེད་པ་གཡོགས་པ་གང་ཡིན་པ་དེ་ནི་བར་ན་གནས་གཞན་མེད་པ་ཉིད་དོ། །

[Block 1316]
གནས་མེད་པར་གྱུར་པའི་བར་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1317]
འདིའི༌[^811]གང་སླར་གཡོགས་ཤིང་ཡོངས་སུ་བསྐོར་བའི་མཐར་ཐུག་པ་ཉེ་འཁོར་དུ་གྱུར་པ་མ་ཡིན་པའི་གནས་གཞན་ཐམས་ཅད་ལ་གནས་ཐ་དད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1318]
རྒྱུ་བའི་གོ་སྐབས་གང་འདི་ལ་གནས་པ༌[^812]ཉིད་དུ་བྱེད་པའི་ཉེ༌[^813]འཁོར་དང་ལྡན་པ་ལ་ཕལ་ཆེར་ལ་གཡོགས་པ་ཉིད་ཀྱིས་གནས་གཞན་མ་ཡིན་པ་ཉེ་བར་མེད་པ་ཉིད་དོ། །

[Block 1319]
གནས་མ་ཡིན་པར་གྱུར་པའི་བར་གྱི་དེ་ལ་ནང་དུ་རྒྱུ་བ་འདི་ཡོད་པ་ཡིན་ཏེ། འབྱུང་བ་ཉིད་ཀྱིས་ནི་གོ་སྐབས་དེ་འདིར་འཇུག་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1320]
དེ་དང་ལྷན་ཅིག་ཏུ་གནས་པ་ཉིད་དེ་དང་ལྷན་ཅིག་ཏུ་གང་གི་ཕྱིར་དེ་བརྗོད་པ་ཐམས་ཅད་ལ་གནས་མ་ཡིན་པར་གྱུར་པ་ཉིད་ལ་རྒྱུ་བའི་ལམ་པ༌[^814]ལའོ། །

[Block 1321]
གལ་ཏེ་མ་ཡིན་ན་འདི་ལ་གཡོགས་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1322]
གལ་ཏེ་གཡོགས་པ༌[^815]ཉིད་ཡིན་ན་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 1323]
ཁྱམས་ངོས་བཞི་དང་གསུམ་པ་དག་ལ་ནོར་དག་ལ་བར་ཆོད༌[^816]དང་བཅས་པ་ཉིད་ཀྱིས༌[^817]ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 1324]
རང་གི་ཆར་གཏོགས་པའི་སྒོ་བཅད་པ་ལ་ནི་ཉེ་འཁོར་ཡང་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་འབྱིན་པ་པོའི་ཆར་གཏོགས་པའི་སྒོ་གང་ཡིན་པ་བཅད་པས་བཅད་པ་ཉིད་ཀྱི་སྒོ་དང་ཉེ་འཁོར་ལ་ཡང་འདིར་བུད་མེད་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་ལ་ཐ་དད་པ་ཉིད་དོ། །

[Block 1325]
ཁང་བཟངས་ཀྱི་ཕྱོགས་ཀྱི་གཞན་ལ་གནས་ཁང་གཞན་སྒོ་ཁང་དང་བང་རིམ་པ༌[^818]རྣམས་ལ་གོང་རིམ༌[^819]ཉིད་དུ་སྨོས་དགོས་སོ། །

[Block 1326]
ལྟུང་བ་འབྱིན་པར་བྱེད་པ་དགེ་སློང་གིས་བསྲུངས་པ་ཉིད་ནི་དེ་དང༌[^820]འདྲའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་འབྱིན་པར་བྱེད་པ་དགེ་སློང་གིས་བསྲུངས་པ་ཉིད་དང་། བུད་མེད་ཀྱི་ཚོགས་ཀྱང་བདག་པོས་བསྲུངས་པ་ཉིད་དོ། །

[Block 1327]
འདིར་བུད་མེད་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་གང་ཡིན་པ་དེ་རང་གི་ཆར་གཏོགས་པའི་སྒོ་བཅད་པས་བཅད་པ་ཞེས་བསྟན་པ་གང་ཡིན་པ་དེ་ནི་དེ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 1328]
འདི་ཡང་ཉེ་བར་སྤྱོད་པ་ལ་སོགས་པ་རྣམས་ལ་ཐ་དད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1329]
འདིར་གཞུང་ནི་དགེ་སློང་བང་རིམ་ཁ་ན་རྟག་ཏུ་ཉལ་བར་བྱེད་ཅིང་བུད་མེད་སྒོ་ཁང་ན་ཉལ་ན། དགེ་སློང་དེས་ཕྱི་སྒོ་གཅད་པར་བྱ་བའམ་དགེ་སློང་སྲུང༌[^821]མ་གཞག་པར་བྱའོ། །

[Block 1330]
ཕྱི་སྒོ་གཅོད་པར༌[^822]མི་བྱེད་དམ་དགེ་སློང་སྲུང༌[^823]མ་འཇོག་པར་མི་བྱེད་པར་གློས་ཕབ་སྟེ་གཉིད་ལོག་པར་བྱེད་ན་ཇི་སྲིད་དུ་སྐྱ་རེངས༌[^824]མ་ཤར་གྱི་བར་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 1331]
སྐྱ་རེངས༌[^825]ཤར་ནས་ནི་ལྟུང་བྱེད་དོ། །

[Block 1332]
བདག་པོས་བསྲུངས་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་ཡང་གསུངས་པ་ཡིན་ནོ། །

[Block 1333]
གནས་ཐ་དད་པ་ཉིད་ལ་ནི་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ལྟུང་བ་མེད་པ་ཡིན་ནོ། །

[Block 1334]
གནས་གཅིག་པ་ཉིད་ལ་ནི་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ཡང་སྤྱོད་པ་ལས་བྱུང་བའི་ཆ་དང་། ལྷན་ཅིག་ཏུ་བུད་མེད་ལ་སོགས་པ་དང་འདུག་པའི་གེགས་བྱེད་པའི་བུད་མེད་དང་འབྲེལ་པའི་སྲུང༌[^826]མ་ཉིད་ལ་ཡང་ལྟུང་བ་མེད་པ་ཡིན་པས་དེའི་ཕྱིར་འདིར་བདག་པོས་བསྲུངས་པ་ཉིད་ནི་དེ་བཞིན་དུ་འདིར་ལྟུང་བས་གོ་བར་བྱེད་པའི་བློ་ལ་སྐབས་མེད་དོ། །

[Block 1335]
དེ་བས་ན་འདིར་ཡང་གནས་ཐ་དད་པ་ཉིད་ལ་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ལྟུང་བ་མེད་དོ། །
--- END BLOCKS ---
