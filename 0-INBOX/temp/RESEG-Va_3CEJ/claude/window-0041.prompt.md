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
ཟག་པ་མེད་པའི་ཆོས་རྣམས་དང་སུ་ཞིག་ལྡན་ཞེ་ན། སྨྲས་པ། སེམས་ཅན་ཐམས་ཅད་དོ་ཞེས་འབྱུང་ངོ་ཞེས་གྲག་གོ། །

[Block 1437]
སོ་སོར་བརྟགས་པས་འགོག་པ་དང་ནི་འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་སྐད་ཅིག་མ་དང་པོ་ལ་གནས་པ་མ་གཏོགས་པ་འཕགས་པ་ཐམས་ཅད་དང་། སོ་སོའི་སྐྱེ་བོ་ཁ་ཅིག་ཀྱང་ཡིན་ནོ། །

[Block 1438]
ནམ་མཁའ་དང་ནི་འགའ་ཡང་ལྡན་པ་མེད་དེ། དེ་བས་ན་འདི་ལ་ཐོབ་པ་མེད་དེ། གང་ལ་ཐོབ་པ་མེད་པ་དེ་ལ་ནི་མ་ཐོབ་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་གྲུབ་པའི་མཐའ་ཡིན་ནོ། །

[Block 1439]
ཐོབ་པ་ཞེས་བྱ་བ་རྫས་གཞན་ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་འདི་གང༌[^618]ལས།

[Block 1440]
སྨྲས་པ་མདོ་ལས་ཏེ། མདོ་ལས་དེ་མི་སློབ་པའི་ཆོས་བཅུ་པོ་འདི་དག་བསྐྱེད་ཅིང་སོ་སོར་ཐོབ་པ་ལས༌[^619]ཀུན་ཏུ་ལྡན་པས་ན་ཡན་ལག་ལྔ་རྣམ་པར་སྤངས་པའི་འཕགས་པར་འགྱུར་རོ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 1441]
འོ་ན་ནི་དེས་ནི་སེམས་ཅན་དུ་མི་སྟེན་པ༌[^620]དག་དང་སེམས་ཅན་གཞན་དག་དང་ཡང་ལྡན་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། མདོ་ལས་དགེ་སློང་དག་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་རིན་པོ་ཆེ་སྣ་བདུན་དང་ལྡན་པ་ཞེས་རྒྱས་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1442]
དེར་ནི་དབང་བ་དེ༌[^621]ཉིད་ལ་ལྡན་པའི་སྒྲར་གསུངས་ཏེ། དེ་རིན་པོ་ཆེ་སྣ་བདུན་དག་ལ་དབང་ཉིད་དགའ་དགུར༌[^622]བྱེད་པའི་ཕྱིར་རོ། །

[Block 1443]
ལྡན་པ་དེར་ནི་དབང་བ་ཉིད་ཡིན་ལ། [^623]གཞན་དུ་ནི་རྫས་གཞན་ཡིན་ནོ། །ཞེས་བྱ་བ་འདི་དག༌[^624]ལས།

[Block 1444]
དེ་ལྟ་ན་ཡང་མི་རུང་བ་ཅི་ཞིག་ཡོད། མི་རུང་བ་འདི་དག༌[^625]ཡོད་དེ། གང་གི་ཕྱིར་གཟུགས་དང་སྒྲ་ལ་སོགས་པ་ལྟར་རམ། འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པ་ལྟར་འདིའི་རང་གི་ངོ་བོ་ཡང་མི་སྣང་ལ། མིག་དང་རྣ་བ་ལ་སོགས་པ་ལྟར་བྱ་བ་ཡང་མི་སྣང་བ་དེའི་ཕྱིར་རྫས་ཀྱི་ཆོས་མི་སྲིད་པས་མི་རུང་ངོ་། །[^626]གལ་ཏེ་ཆོས་རྣམས་སྐྱེ་བའི་རྒྱུ་ལ་ཐོབ་པའོ༌[^627]ཞེས་བྱའོ་ཞེ་ན། འདུས་མ་བྱས་ཀྱི་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1445]
ཆོས་གང་དག་མ་ཐོབ་པ་རྣམས་དང་། གང་དག་ས་འཕོས་པ་དང་འདོད་ཆགས་དང་བྲལ་བས་བཏང་སྙོམས་པ༌[^628]དེ་དག་ཀྱང་ཇི་ལྟར་སྐྱེ་བར་འགྱུར་རོ།[^629] །འོན་ཏེ་ལྷན་ཅིག་སྐྱེས་པའི་ཐོབ་པའི་རྒྱུ་རྐྱེན༌[^630]ཡིན་ནོ་ཞེ་ན། དེའི་ཚེ་སྐྱེ་བའམ། སྐྱེ་བའི་སྐྱེ་བ་ཅི་ཞིག་བྱེད་པར་འགྱུར། འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་རྣམས་ཀྱི་ཉོན་མོངས་པ་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་སྐྱེ་བའི་ཁྱད་པར་དུ་ཡང་མི་འགྱུར་ཏེ། ཐོབ་པ་བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 1446]
འོན་ཏེ་དེ་ལས་དེ་དག་གི་བྱེ་བྲག་ཏུ་འགྱུར་ན་ནི་དེ་ཁོ་ན་ལས་དེ་དག་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1447]
དེ་ལྟ་བས་ན་ཐོབ་པ་སྐྱེ་བའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 1448]
ཐོབ་པ་སྐྱེ་བའི་རྒྱུ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་སུ༌[^631]ཟེར། འོ་ན་ཅི་ཞེ་ན། རྣམ་པར་གཞག་པའི་རྒྱུ་ཡིན་ཏེ། ཐོབ་པ་མེད་ན་འཇིག་རྟེན་པའི་ཡིད་དང་ལྡན་པའི་འཕགས་པ་དང་། སོ་སོའི་སྐྱེ་བོ་རྣམས་ལ་འདི་དག་ནི་འཕགས་པའོ། །

[Block 1449]
འདི་དག་ནི་སོ་སོའི༌[^632]སྐྱེ་བོའོ་ཞེས་རྣམ་པར་གཞག་པར་མི་འགྱུར་རོ། །

[Block 1450]
དེ་ནི་ཉོན་མོངས་པ་སྤངས་པ་དང་མ་སྤངས་པ་ཉིད་ཀྱི་བྱེ་བྲག་ལས་འགྱུར་བར་འོས་སོ། །

[Block 1451]
འདི་དག་ནི་ཉོན་མོངས་པ་སྤངས་པའོ། །

[Block 1452]
འདི་དག་ནི་ཉོན་མོངས་པ་མ་སྤངས་པའོ་ཞེས་བྱ་བ་འདི་ཉིད་དུ་ཡང་ཇི་ལྟར་འགྱུར། ཐོབ་པ་ཡོད་ན་ནི་དེ་དང་བྲལ་མ་བྲལ་ལས་འདི་ཡང་འགྲུབ་བོ། །

[Block 1453]
འདི་ནི་རྟེན་གྱི་བྱེ་བྲག་ལས་འགྲུབ་པར་འགྱུར་ཏེ། འཕགས་པ་རྣམས་ཀྱི་གནས་དེ་ནི་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་གྱི་མཐུས་ཇི་ལྟར་དེ་དག་གིས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་རྣམས་ཡང་འབྱུང་བར་མི་ནུས་པ་དེ་ལྟར་གྱུར་པ་ཡིན་ཏེ། དེའི་ཕྱིར་རྟེན་འབྲུ་མེས་ཚིག་པ་བཞིན་དུ་ཉོན་མོངས་པ་རྣམས་ཀྱི་ས་བོན་དུ་མ་གྱུར་པའམ། འཇིག་རྟེན་པའི་ལམ་གྱི་ས་བོན་གྱི་དངོས་པོ་ཉམས་པར་བྱས་ན་ཉོན་མོངས་པ་སྤངས་པ་ཞེས་བྱ་ལ། བཟློག་པ་ནི་མ་སྤངས་པ་མ༌[^633]ཡིན་པས་གང་མ་སྤངས་པ་དེ་དང་མི་ལྡན།[^634] གང་སྤངས་པ་དེ་དང་ནི་མི་ལྡན་ནོ་ཞེས་གདགས་སོ། །

[Block 1454]
དགེ་བའི་ཆོས་རྣམས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། མ་འབད་པར་སྐྱེ་བ་རྣམས་དང་། འབད་དེ་སྐྱེ་བ་རྣམས་ཏེ། གང་དག་སྐྱེ་བས་ཐོབ་པ་དང་། སྦྱོར་བ་ལས་བྱུང་བ་ཞེས་བྱ་བ་དེ་དག་ཡིན་ནོ། །

[Block 1455]
དེ་ལ་མ༌[^635]འབད་པར་སྐྱེ་བ་རྣམས་དང་ནི་རྟེན༌[^636]དེ་དག་གི་ས་བོན་གྱི་དངོས་པོ་ཉམས་པར་མ་བྱས་པའི་ཕྱིར་ལྡན་ལ། ཉམས་པར་བྱས་པའི་ཕྱིར་མི་ལྡན་པ་ཞེས་བྱ་སྟེ། དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པ་ཡིན་ནོ། །

[Block 1456]
དེ་ཡང་ལོག་པར་ལྟ་བས་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1457]
རྒྱུ༌[^637]ལ་དགེ་བའི་ཆོས་རྣམས་ཀྱི་ས་བོན་གྱི༌[^638]དངོས་པོ་གཏན༌[^639]དུ་ཡང་དག་པར་བཅོམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 1458]
གང་དག་འབད༌[^640]དེ་སྐྱེ་བ་ནི་སྐྱེས་པ་དེ་དག་དང་རྒྱུད་ལ་དེ་དག་སྐྱེ་བའི་དབང་ཉིད་ཐོགས་པ་མེད་པའི་ཕྱིར་ལྡན་པ་ཞེས་བྱའོ། །

[Block 1459]
དེའི་ཕྱིར་འདིར་ས་བོན་ཁོ་ན་རྩ་ནས་མ་བཏོན་པ་དང་། ཉམས་པར་མ་བྱས་པ་དང་། དབང་ཉིད་ཀྱི་དུས་ན་རྒྱས་པར་གྱུར་པ་ནི་ལྡན་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་ཀྱི་རྫས་གཞན་ནི་མེད་དོ། །

[Block 1460]
ས་བོན་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཡིན། འབྲས་བུ་བསྐྱེད་པར་བྱ་བ་ལ་རྒྱུད་འགྱུར་བའི་བྱེ་བྲག་གི་མངོན་སུམ་མམ་བརྒྱུད་པས་ནུས་པའི་མིང་དང་གཟུགས་གང་ཡིན་པའོ། །

[Block 1461]
འགྱུར་བ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཡིན། རྒྱུད་གཞན་ཉིད་དུ་འགྱུར་བའོ། །

[Block 1462]
རྒྱུད་ཅེས་བྱ་བ་འདི་ཡང་ཅི་ཞིག༌[^641]ཡིན། འདུ་བྱེད་དུས་གསུམ་པ་རྒྱུ་དང་འབྲས་བུར་གྱུར་པ་རྣམས་སོ། །

[Block 1463]
གང་ལས་ཆགས་པ་དང་ལྡན་པ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་པོ་དག་བསྒོམ་པའི་སྐལ་བ་དང་མི་ལྡན་ནོ་ཞེས་གསུངས་པ་དེར་ནི་ལྡན་པ་ཆགས་པ་དང་དུ་ལེན་བ་འམ་མི་སེལ་བ་ཡིན་ཏེ། ཇི་སྲིད་དུ་དེ་དང་དུ་ལེན་བའམ་མི་སེལ་བ་དེ་སྲིད་དུ་དེ་དག་བསྒོམ་པའི་སྐལ་བ་དང་མི་ལྡན་ནོ། །

[Block 1464]
དེ་ལྟར་ན་ལྡན་པ་འདི་དང་དེ་འགོག་པ་མི་ལྡན་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་བཏགས་པའི་ཆོས་ཡིན་གྱི་རྫས་ཀྱི་ཆོས་ནི་མ་ཡིན་ནོ། །

[Block 1465]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གཉི་ག༌[^642]རྫས་ཁོ་ན་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་ཁོ་བོ་ཅག་གིས་གྲུབ་པའི་མཐའ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1466]
ཐོབ་པ་དེ་ནི། དུས་གསུམ་པའི་རྣམ་པ་གསུམ་ཞེས་གྲག་སྟེ། ཆོས་འདས་པ་རྣམས་ཀྱི་ཐོབ་པ་འདས་པ་ཡང་ཡོད། མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཡང་ཡོད་ལ། དེ་བཞིན་དུ་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་ཡང་སོ་སོར་རྣམ་པ་གསུམ་མོ། །

[Block 1467]
དགེ་ལ་སོགས་ཀྱི་དགེ་ལ་སོགས། །དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་རིམ་པ་བཞིན་དུ་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན༌[^643]ཡིན་ནོ། །

[Block 1468]
དེར་གཏོགས་རྣམས་ཀྱི་རང་ཁམས་པ། ། ཆོས་གང་དག་ཁམས་གང་དུ་གཏོགས་པ་དེ་དག་གི་ཐོབ་པ་ནི་རང་གི་ཁམས་པ་ཡིན་ཏེ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་རིམ༌[^644]པ་བཞིན་དུ་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡིན་ནོ། །

[Block 1469]
མ་གཏོགས་རྣམས་ཀྱི་རྣམ་པ་བཞི། །ཟག་པ་མེད་པའི་ཆོས་རྣམས་ཀྱི་ཐོབ་པ་ནི་མདོར་བསྡུ་ན་རྣམ་པ་བཞི་སྟེ། ཁམས་གསུམ་པ་དང་། ཟག་པ་མེད་པའོ། །

[Block 1470]
དེ་ལ༌[^645]སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པའི་ནི་ཁམས་གསུམ་པ་ཡིན་ནོ། །

[Block 1471]
སོ་སོར་བརྟགས་པས་འགོག་པའི་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་ཡིན་ལ། ཟག་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 1472]
ལམ་གྱི་བདེན་པའི༌[^646]ཟག་པ་མེད་པ་ཉིད་དོ། །

[Block 1473]
དེ་ནི་མདོར་བསྡུས་ཏེ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 1474]
སློབ་པའི་ཆོས་རྣམས་ཀྱི་ཐོབ་པ་ནི་སློབ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1475]
མི་སློབ་པ་རྣམས་ཀྱི་ནི་མི་སློབ་པ་ཁོ་ན་ཡིན་ནོ། །
--- END BLOCKS ---
