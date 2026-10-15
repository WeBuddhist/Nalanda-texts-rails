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
[Block 1436]
ཁ་མ་བསྒྱུར་བ་ཞེས་བྱ་བ་ནི་ཚོན་གྱིས༌[^893]སོ། །

[Block 1437]
དེ་བས་ན་གང་ཡང་རུང་བས་ཁ་མ་བསྒྱུར་བའི་རང་གི་གོས་ལ་ཞེས་བྱ་བ་ནི་གཞན་གྱི༌[^894]གོས་ཉེ་བར་ལོངས་སྤྱོད་པ་ལ་ན་སྨད་པ་ཉིད་དེ་ཁ་ན་མ་ཐོ་བ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར། བདག་ཏུ་བྱས་པ་དང་དཀྲིས་པར་མངོན་པར་བརྟེན་པ་ཉིད་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལྟར་ཡང་སོ་སོར་ཁྱིམ་པའི་གོས་བགོ་བ་བཀག་པའི་ཚུལ་གྱིས་ཏེ་གཞན༌[^895]དུ་ནི་མ་ཡིན་ནོ། །

[Block 1439]
དེ་ལྟ་བུའི་ལྟུང་བྱེད་ལ་འབྱུང་བ་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1440]
གོས་སར་པ་སོ་སོར་རྙེད་པས་ཞེས་བྱ་བ་ལ། གང་ཞིག་སོ་སོར་རྙེད་པའི་ཚིག་བྱས་ཞེས་བྱ་བ་འདིའི་རྗེས་ལ་ཡང་རང་གི་ཚིག་སྨོས་པ་དེ་ལས་སོ། །

[Block 1441]
སར་པ་ཞེས་བྱ་བ་ལ་སར་པ་ནི་རྣམ་པ་གཉིས་ཏེ། སར་པ་ལས་ཀྱང་སར་པ་དང་སོར༌[^896]སོར་རྙེད་པ་ལས་ཀྱང་སར་པ་སྟེ། དོན་འདི་ལ་ནི་སོར༌[^897]སོར་རྙེད་པ་ལས་སར་པ་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་འདིར་གཞུང་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1442]
རྙིང་པ་ལ་ཡང་ཁ་མ་བསྒྱུར་བ་ལ་བགོ་བར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1443]
ཡང་གང་ཞིག་ཀློག་པ་ལས་འབྱུང་བ་ཡིན་ཏེ། དོན་འདི་ལ་ནི་སར་པ་ལས་སར་པ་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ༌[^898]འདི་ལས་ཉམས་པ་ཉིད་དོ། །

[Block 1444]
དེ་ལྟ་བས་ན་སོ་སོར་རྙེད་པ་ལས་གང་ཞིག་ཐོག་མ་ཉིད་གང་ཡིན་པ་དེས་ཆོས་གོས་དང་པོ་སོ་སོར་རྙེད་པས་འདི་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 1445]
འདིར་ཐམས་ཅད་དཀྲིས་པ་དང་། དུས་འབྱུང་བ་དང་ཕྱེ་མ་ལ་སོགས་པ་ལ་ཉེས་པར་བགོ་བར༌[^899]བྱ་བའི་གོས་བགོ་བར་བྱེད་པར་ནུས་པ་ཉིད་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་སྨོས་པ་ནི་ཐ་ན་ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས་དང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1446]
འདིར་ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས་ཀྱིས་བསོད་སྙོམས་ཉེ་བར་གཡོགས་པ་བརྗོད་པ་མཐོང་བ་ཡིན་གྱི། གཞན་དུ་ནི་རྗེས་སུ་གནང་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས་ལྷུང་བཟེད་ཀྱི་དྲ་བ་ལ་སོགས་པ་རྐང་པ་བཀྲུ་བའི་སྣོད་དུ་སྦྱར་དུ་རུང་ངམ་ཞེ་ན། རུང་ཞེས་གསུངས་པ༌[^900]ནི་ཆུ་ཚགས་འདིར་རིགས་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་བསྡུས་པ་ཡིན་ཏེ། རྒྱུ་བ་འདི་ཆུ་གཟུང་བ༌[^901]ལ་ཁ་བསྒྱུར་བ་དང་བཅས་པ་ཉིད་དོ། །

[Block 1447]
གཟུང་བ༌[^902]དང་ལྡན་པ་ཉིད་དང་འདི་ལ་བྱིན་ལེན་བྱ་བ་ཉིད་དང་། ཉེ་བར་གནས་པ་ཉིད་དང་དུས་མ་ཡིན་པ་ཉིད་ལ་གཟུང་བར༌[^903]བྱ་བ་དང་ཉེ་བར་གནས་པ་ཉིད་ཡོད་ཀྱང་ལོངས་སྤྱད་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1448]
དོན་འདི་ནི་ཕལ་ཆེར་ཉམས་པ་མ་ཡིན་ནོ། །

[Block 1449]
དེ་ལྟ་བས་ན་ཡོ་བྱད་དང་ཆོས་གོས་སྦྱིན་པ་འདི་དང་འདི་ལ་ཁ་མ༌[^904]བསྒྱུར་བ་ཉིད་དུ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 1450]
བགོ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་སོ་སོར་གཡོགས་པ༌[^905]ཡང་སྟེ། བགོ་བ་དང་གཡོགས་པ་དང་ཉིད་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1451]
འདིར་ཚད་དང་ལྡན་པ་ཉིད་ཀྱང་མ་ཡིན་ཞེས་བྱ་བ་འདི་འཇུག་པའོ། །

[Block 1452]
སྐེ་རགས༌[^906]དག་ལ་ཡང་གལ་ཏེ་ཉེས་པ་ཡོད་ན་ཚད་དང་མི་ལྡན་པའི་གོས་ལ་སོགས་པ་ལ་ཡང་འབྱུང་བའི་ཕྱིར་འོས་པ་མ་ཡིན་ཞེས་གསུངས་སོ། །

[Block 1453]
སྡེ་པ་གཞན་གྱིས༌[^907]ན་རུང་བར་བྱ་མི་དགོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་དང་དགེ་སློང་མ་དང་དགེ་ཚུལ་དང་དགེ་སློབ་མ་དང་དགེ་ཚུལ་མའི་སྡེ་པའི་འཁོར་རྣམས་ནི་དེ་ནི་འདིར་སྡེ་པ་ཞེས་བྱ་བའི་སྒྲར་འགྱུར་རོ། །

[Block 1454]
དེ་ལས་སྡེ་པ་གཞན་གང་ཡང་རུང་བའི་གོས་རང་སྤྱོད་པ་ལ་ནི་ཡང་གཟོད་རུང་བར་བྱ་མི་དགོས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1455]
ཁྱིམ་པས་བརྐུས་པ་ཡང་མ་ཡིན་ནོ༌[^908]ཞེས་བྱ་བ་ནི་གཟོད་རུང་བར་བྱ་མི་དགོས་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 1456]
འདིར་མདོ་དེ་གཉིས་ཀྱི་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་དགེ་སློང་གི་གོས་རུང་བར་བྱས་པ་གང་ཡིན་པ་དེ་ནི་དགེ་སློང་མ་རྣམས་ལ་ཡང་རུང་བར་བྱས་པ་ཉིད་ཡིན་ལ། དེ་བཞིན་དུ་སྡེ་པ་ལྔ་པོ་ཐམས་ཅད་ལ་ཡང་རུང་བར་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 1457]
དགེ་སློང་གིས་རྒྱལ་པོའམ་ཕྱིར་རྒོལ་བ་གཞན་དག་གོས་བརྐུས་པར་གྱུར་པ་ཞིག་གལ་ཏེ་སླད་ཀྱིས་ཐོབ་པར་གྱུར་ན་ཡང་རུང་བར་བགྱི་འཚལ་ལམ་ཉེ་བ་འཁོར་མི་དགོས་ཏེ། སྔ་མ༌[^909]ཉིད་དུ་རུང་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1458]
ཁ་དོག་ཆེན་པོར་ཁ་བསྒྱུར་བའི་གོས་བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིའི་གཞུང་ནི་བཤད་ཟིན་ཏོ། །

[Block 1459]
འདིར་བརྒྱད་ཀྱི་ཚིག་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1460]
དེ་བས་ན་འདིར་ཉེ་བར་མ་བསྡུས་སོ། །

[Block 1461]
ཁྱིམ་པའི་གོས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བགོ་བ༌[^910]བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1462]
འདིར་ཕྲན་ཚེགས་དག་ལས༌[^911]དང་པོའི་གཞུང་ངོ་། །གཙུག་ལག༌[^912]ཁང་གི་ནང་དུ༌[^913]ངུར་སྨྲིག་གིས་གཡོགས་ཏེ་བརྟེན་པར༌[^914]བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གནས་ཁང་གཙུག་ལག་ཁང་ནས་ཕྱིར་མི་འབྱུང་བར་བགོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་གྱི་གནས་ཁང་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1463]
གཞན་མ་ཡིན་པ་ལ་ཡང་གཙུག་ལག་ཁང་ཉིད་མ་ཡིན་ནོ། །

[Block 1464]
དེ་བས་ན་འདི་ལ་སོར༌[^915]སོར་བཟུང་བ་མ་བྱས་སོ། །

[Block 1465]
ཁྱིམ་པའི་གོས་ཇི་ལྟ་བུ་ལ་གཙུག་ལག་ཁང་གི་ནང་དུ་བགོ་བ་བརྟེན་པར༌[^916]བྱ་བ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ངུར་སྨྲིག་གིས་གཡོགས་ཏེ་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མལ་ཆའི་སྟེང་དུ་བརྟེན་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་གཞན་དུ་ནི་བཏགས་པའོ། །

[Block 1466]
ལམ་དུ་གོས་བརྙས་པ་ནི་ཐུན་མོང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བརྙས་པ་གཅིག་གིས་ཐོབ་པ་ཡང་འདི་ནི་ཐུན་མོང་བ་ཉིད་དུ་བསྟན་པའོ། །སུ་དང་ཐུན་མོང་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གྲོགས་དག་དང་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟ་བུ་དག་དང་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དང་དགེ་ཚུལ་དག་དང་ངོ་། །གཅིག་པུ་ཉིད་ཡིན་ན་རྒན་རབས་ནས་བརྩམས་ཏེ་ཇི་སྲིད་སླེབས་པའི་སྟེང་དུ་གཡོགས་སོ༌[^917]ཞེས་བྱ་བ་ནི་གོས་བརྙས་པ་ནི་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1467]
དམིགས་ཀྱིས་མ་བསྔོས་ན་གཞན་ལས་གྱོན་ཏེ་བཙག༌[^918]པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གོས་ཐུན་མོང་བ་བགོས་ནས་ཞེས་བྱ་བ་མི་བརྗོད་པ་དམ་པ་རྣམས་ཀྱིས་རྗེས་སུ་གནང་བ་ལ་དེ་ལ་ཡང་ཁོངས་སུ་བསྡུ་བ་སྒྲུབ་པའི༌[^919]དོན་དུ་གང་ཞིག་ཐུན་མོང་ཉིད་དུ་སྦྱིན་པ་སྟེ། དེ་དང་འདི་ཞེས་བྱ་བ་བྱེ་བྲག་ཏུ་ནི་མ་ཡིན་ཏེ། དེ་ནི་དམིགས་ཀྱིས་མ་བསྔོས་པའོ། །

[Block 1468]
བསོད་ནམས་འདོད་པས་མགྲོན་དུ་བོས་ན་ཁ་ཚར་མ་བཅད་པ་མན་ཆད་སར་པ་ལ་མི་རྟག་པས་ཉེན་པར་གྱུར་པའི་ཡིད་ལ་བྱེད་པས་སྟེང་དུ་བརྫི་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དུས་ནམ་གྱི་ཚེ་ན་བརྫི་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མགྲོན་དུ་བོས་ནས་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐོ་འཚམས༌[^920]པར་བྱེད་པའི་བསམ་པས་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་བསོད་ནམས་འདོད་པས་སོ། །ཅི་ཞིག་བརྫི་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་སར་པ་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1469]
ཁ་ཚར་མ་བཅད་པ་ཞེས་བྱ་བ་ནི་འདིར་ཇི་སྲིད་ཀྱི་སྒྲ་དང་འབྲེལ་པ་སྟེ། ཇི་སྲིད་དུ་ཁ་ཚར་མ་བཅད་པ་མན་ཆད་ཅེས་བྱ་བའི་དོན་ཏོ། །ཅི་གང་ཡང་རུང་བས་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མི་རྟག་པས་ཉེན་པར་གྱུར་པའི་ཡིད་ལ་བྱེད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1470]
ཁ་མ་བསྒྱུར་བའི་གོས་གྱོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1471]
གང་དུ་ཅི་ཞིག་བྱས་ན་ལོངས་པ་བཞིར༌[^921]གཏོགས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ༌[^922]ན། དེའི་ཕྱིར་རིན་པོ་ཆེ་རང་གི་མ་ཡིན་པ་དང་། དེར་སྨོས་པ་ལ་རེག་གམ་རེག་ཏུ་བཅུག་ན་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་རེག་གམ་རེག་ཏུ་བཅུག་ན་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1472]
ཅི་ཞིག་བྱས་ན་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་རིན་པོ་ཆེ་རང་གི་མ་ཡིན་པ་དང་། དེར་སྨོས་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1473]
དེར་ཞེས་བྱ་བའི་སྒྲས་ནི་དེར་སྨོས་པ་ལ་རིན་པོ་ཆེར་བཟུང་སྟེ་རིན་པོ་ཆེ་དང་མཉམ་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1474]
དེར་རང་ལ་རང་བཞིན་གྱིས་དངོས་པོ་ཉིད་ཀྱི་ཕྱིར་རང་གི་རིན་པོ་ཆེའི་རང་བཞིན་གྱི་ཆོ་ག་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་ཆོ་ག་འདིར་རང་བཟུང་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་དག་པའི་ལྟུང་བྱེད་ལ་རང་མ་ཡིན་པའི་ཚིག་ཏུ་བྱས་སོ། །

[Block 1475]
དེར་སྨོས་པ་ལ་ཞེས་བྱ་བ་འདི་ལ་རང་མ་ཡིན་པ་ཞེས་བྱ་བ༌[^923]རྟོགས་པར་བྱ་སྟེ། འདིར་གཉིས་ཀ་ཡང་བྱེད་པ་པོར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
