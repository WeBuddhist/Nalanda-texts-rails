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
[Block 2696 [VERSE]]
བྲམ་ཟེ་ན་ཚོད་ཁྱེར་ཟིན་རྒ་བ་དང་། །
ན་བ་ཡིན་ཏེ་གཤིན་རྗེའི་དྲུང་དུ་ཕྱིན། །
བར་ན་ཁྱོད་ཀྱི་གནས་ཀྱང་ཡོད་མིན་ཞིང་། །
ཁྱོད་ཀྱི་ལམ་བརྒྱགས༌[^1458]ཀྱང་ནི་ཡོད་མ་ཡིན། །

[Block 2697]
ཞེས་གསུངས་པའི་ཚིགས་སུ་བཅད་པ་འདི་ཇི་ལྟར་དྲང་། འདིར་ཡང་དགོངས་པ་ནི་མི་དག་གི་ནང་ན་གནས་སུ་མེད་དོ་སྙམ་པ་ཡིན་ནོ། །

[Block 2698]
ཡང་ན་སྐྱེ་བའི་ཡུལ་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་དང༌[^1459]འགྲོ་བ་ལ་བགེགས་བྱེད༌[^1460]པ་མེད་པའི་ཕྱིར་སྲིད་པ་བར་མ་ན་ཡང་འདི་གནས་པ་མེད་དོ་སྙམ་པ་ཡིན་ནོ། །

[Block 2699]
འདི་ལ་འདི་ནི་དགོངས་པ་ཡིན་གྱི་འདི་ནི་དགོངས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་བརྟགས་པ༌[^1461]འདི་ནི་ཁྱོད་ལ་ཡང་མཚུངས་ཏེ། དེ་ལྟ་བས་ན་གཉི་གའི་ཕྱོགས་ལ་ཡང་ཇི་སྐད་གསུངས་པའི་མདོ་མི་འགལ་བའི་ཕྱིར་འདི་ནི་སྲིད་པ་བར་མ་མེད་པའི་ཁུངས་མ་ཡིན་ནོ། །

[Block 2700]
ཁུངས་ཞེས་བྱ་བ༌[^1462]ནི་ཤེས་པར་བྱེད་པ་གཞན་དུ་ཤེས་པར་མི་བྱེད་པ་ཡིན་ནོ། །

[Block 2701 [HEADING]]
##### སྲིད་པ་བར་མའི་ཤ་ཚུགས། ^3-1-7-2-0

[Block 2702]
ཡང་འགྲོ་བ་གང་དུ་འགྲོ་བར་འགྱུར་བའི་སྲིད་པ་བར་མའི་ཤ་ཚུགས་ཇི་ལྟ་བུ་ཞིག་མངོན་པར་འགྲུབ་ཅེ་ན།

[Block 2703 [VERSE]]
དེ་ནི་འཕེན་པ་གཅིག་པའི་ཕྱིར། །
སྔོན་དུས་སྲིད་འབྱུང་ཤ་ཚུགས་ཅན། །

[Block 2704]
ལས་གང་གིས་འགྲོ་བ་འཕེན་པ་དེ་ཉིད་ཀྱི༌[^1463]དེར་ཕྱིན་པར་བྱ་བའི་ཕྱིར་སྲིད་པ་བར་མ་ཡང་འཕེན་ཏེ། དེའི་ཕྱིར་དེ་ནི་འགྲོ་བ་གང་དུ་འགྲོ་བར་འགྱུར་བའི་འགྲོ་བ་དེ༌[^1464]དུས་སྔ་མའི་སྲིད་པ་འབྱུང་བར་འགྱུར་བ་གང་ཡིན་པ་དེའི་ཤ་ཚུགས་ལྟ་བུར་འགྱུར་རོ། །

[Block 2705]
དེ་ལྟ་ན་འོ་ན་ཁྱི་མོ་ལ་སོགས་པའི་མངལ་གཅིག་ཏུ་འགྲོ་བ་ལྔ་པའི་སྲིད་པ་བར་མ་མངོན་པར་འགྲུབ་པས་དམྱལ་བའི་སྲིད་པ་བར་མས་མའི་མངལ་ཚིག༌[^1465]པར་འགྱུར་རོ་ཞེ་ན། རེ་ཞིག་སྲིད་པ་སྔ་མ་ལ་ཡང་དམྱལ་བ་པ་རྣམས་ལྷག་པ་དག་ན་འཕྱན་པ་ན་རྟག་ཏུ་འབར་བ་མ་ཡིན་ན་སྲིད་པ་བར་མ་པ་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། ཡང་ན་འབར་དུ་ཆུག་ན་ཡང་དེ་ནི་ལུས་ཤིན་ཏུ༌[^1466]དང་བའི་ཕྱིར་ཇི་ལྟ་བ༌[^1467]བལྟར་མི་ནུས་པ་དེ་ལྟར་རེག་པ༌[^1468]ཡང་མི་ནུས་པས་འདི་ནི་ཀླན་ཀར་མི་རུང་ངོ་། །སྲིད་པ་བར་མ་རྣམས་ཀྱང་མངལ་ན་ཕན་ཚུན་མི་རེག་པའི་ཕྱིར་དང་། ལས་ལ་རག་ལུས་པའི་ཕྱིར་མི་ཚིག༌[^1469]གོ། །

[Block 2706]
བོང་ཚོད་ནི། དཔེར་ན་བྱིས་པ་ལོ་ལྔའམ་དྲུག་ལོན་པ་ལྟ་བུ་སྟེ། དེ་ཡང་དབང་པོ་གསལ་བ་ཡིན་ནོ། །

[Block 2707]
བྱང་ཆུབ་སེམས་དཔའ་ནི་དཔེར་ན་གཞོན་ནུ་ཐོར་བུ་ལྟ་བུ༌[^1470]མཚན་དང་དཔེ་བྱད་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2708]
དེ་ཉིད་ཀྱི་ཕྱིར་སྲིད་པ་བར་མ་ལ་གནས་པ་ཡུམ་གྱི་ལྷུམས་སུ་ཞུགས་པས༌[^1471]གླིང་བཞི་པ་བྱེ་བ་ཕྲག་བརྒྱ་སྣང་བར་མཛད་དོ། །

[Block 2709]
འོ་ན་གང་བྱང་ཆུབ་སེམས་དཔའི་ཡུམ་གྱི་རྨི་ལམ་ན་ལྷུམས་སུ་གླང་པོ་ཆེའི༌[^1472]ཕྲུ་གུ་དཀར་པོ་ཞུགས་པར་གཟིགས་པ་ཇི་ལྟ་བུ་ཞེ་ན། དུད་འགྲོའི་སྐྱེ་གནས་བཟློག་ནས་ཡུན་རིང་དུ་ལོན་པའི་ཕྱིར་དེ་ནི་མཚན་མ་ཙམ་དུ་ཟད་དེ། དཔེར་ན་རྒྱལ་པོ་ཀྲྀ་ཀིས་གླང་པོ་དང་། ཁྲོན་པ་དང་། ཕྱེ་དང་། ཙན་དན་དང་། ཚལ་དང་། གླང་པོ་ཆེའི་ཕྲུ་གུ་དང་། སྤྲེའུ་གཉིས་དང་། རས་ཡུག་དང་། འཐབ་མོ་ཞེས་བྱ་བ་རྨི་ལམ་བཅུ་མཐོང་བ་ལྟ་བུའོ། །

[Block 2710]
སྲིད་པ་བར་མ་ནི་ལྟོ་བ་བརྟོལ་ཏེ་འཇུག་པ་མ་ཡིན་གྱི་སྐྱེ་གནས་ཀྱི་སྒོ་ནས་འཇུག་སྟེ། དེ་ཉིད་ཀྱི་ཕྱིར་མཚེ་མ་ལས་གང་ཕྱིས་བྱུང་བ་དེ་ནི་ནུ་བོ༌[^1473]ཞེས་བྱའོ། །

[Block 2711]
གང་སྔར་བྱུང་བ་དེ་ནི་ཕུ་བོ༌[^1474]ཞེས་བྱའོ། །

[Block 2712]
འོ་ན་ཆོས་ལྡན་རབ་འབྱོར་གྱིས། །

[Block 2713 [VERSE]]
གླང་ཆེན་དཀར་པོ་མཆེ་བ་དྲུག༌[^1475]ལྡན་པ། །
རྐང་བཞི་མཛེས་དང་ལྡན་པར་ཞལ་བཞེས་ནས། །
དྲང་སྲོང་གནས་ཞེས་པ་ནི་ཇི་བཞིན་དུ། །
ཡུམ་གྱི་ལྷུམས་ཀྱི་གནས་སུ་ཞུགས་པར་གྱུར། །

[Block 2714]
ཅེས་བཤད་པ་འདི་ཇི་ལྟར་དྲང་ཞེ་ན། འདི་ནི་གདོན་མི་ཟ་བར་དྲང་བར་བྱ་བ་མ་ཡིན་ཏེ། འདི་ནི་མདོ་སྡེ་ཡང་མ་ཡིན། འདུལ་བ་ཡང་མ་ཡིན། ཆོས་མངོན་པ་ཡང་མ་ཡིན་གྱི། འདི་ནི་རང་བཟོ་ཡིན་ཏེ། རང་བཟོ་མཁན་རང་བཟོ་སྦྱོར་བ་རྣམས་ཀྱི་བསམ་པ་ཁ་ཅིག་ནི་སྒྲོ་འདོགས་པར་ཡང་འགྱུར་རོ། །

[Block 2715]
འོན་ཏེ་གདོན་མི་ཟ་བར་དྲང་བར་བྱའོ་ཞེ་ན་ཡང་ཇི་ལྟར་ཡུམ་གྱི་རྨི་ལམ་ན་དེ་ཞུགས་པར་གཟིགས་པ་ལྟར་དེས་ཀྱང་ཚིགས་སུ་བཅད་པ་འདི༌[^1476]ལྟར་བྱས་སོ་ཞེས་དེ་ལྟར་དྲང་བར་བྱའོ། །

[Block 2716]
གཟུགས་ན་སྤྱོད་པའི་སྲིད་པ༌[^1477]བར་མ་ཡང་བོང་ཚོད༌[^1478]རྫོགས་པ་དང་། ངོ་ཚ་ཤེས་པའི་ཤས་ཆེ་བའི་ཕྱིར་གོས་དང་བཅས་པར་འབྱུང་ངོ་། །བྱང་ཆུབ་སེམས་དཔའི་ཡང་གོས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2717]
དགེ་སློང་མ་དཀར་མོའི་ཡང་གོས་དང་བཅས་པ་ཡིན་ཏེ། སྨོན་ལམ་གྱི་དབང་གིས་དེ་ཉིད་ཀྱིས་དཀྲིས་ནས་བསྲེགས་པའི་བར་དུ་ཡིན་ནོ། །

[Block 2718]
འདོད་པའི་ཁམས་ན་ངོ་ཚ་མེད་པའི༌[^1479]ཤས་ཆེ་བའི་ཕྱིར༌[^1480]གཞན་ནི་གཅེར་བུ་ཡིན་ནོ། །

[Block 2719]
ཡང་སྲིད་པ་སྔ་མ་ཞེས་བྱ་བ་འདི་གང་ཡིན་ཞེ་ན།

[Block 2720 [VERSE]]
དེ་ནི་འཆི་བའི་སྔོན་རོལ་ཏེ། །
སྐྱེ་བའི་སྐད་ཅིག་ཕན་ཆད་དོ། །

[Block 2721]
སྲིད་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པར་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་དག་གོ། །

[Block 2722]
ད༌[^1481]ནི་རྣམ་པ་བཞིར་དབྱེ་སྟེ། སྲིད་པ་བར་མ་ནི་ཇི་སྐད་བཤད་པའོ། །

[Block 2723]
སྐྱེ་བའི་སྲིད་པ་ནི་འགྲོ་བ་རྣམས་སུ་ཉིང་མཚམས་སྦྱོར་བའི་སྐད་ཅིག་མའོ། །

[Block 2724]
དེ་ཕན་ཆད་འཆི་བའི་སྐད་ཅིག་མ་མ་གཏོགས་པའི་སྲིད་པ་གཞན་ཐམས་ཅད་ནི་དུས་སྔ་མའི་སྲིད་པ་ཡིན་ནོ། །

[Block 2725]
སྐད་ཅིག་མ་ཐ་མ་ནི་འཆི་བའི་སྲིད་པ་ཡིན་ཏེ། གལ་ཏེ་སེམས་ཅན་གཟུགས་ཅན་དག་གི་ནང་དུ་སྐྱེ་ན་གང་གི་འོག་ཏུ་སྲིད་པ་བར་མ་འབྱུང་བ་ཡིན་ནོ། །

[Block 2726]
སྲིད་པ་བར་མ་དེ་ཡང་། རིས་མཐུན་ལྷ་མིག་དག་པས་མཐོང་། །སྲིད་པ་བར་མ་རིས་མཐུན་པ་དག་གིས་མཐོང་ངོ་། །གང་དག་ལ་ལྷའི་མིག་ཤིན་ཏུ་རྣམ་པར་དག་པ་མངོན་པར་ཤེས་པ་ལས་བྱུང་བ་ཡོད་པ་དེ་དག་གིས་འདི་མཐོང་གི། ཤིན་ཏུ་དང་བའི་ཕྱིར་སྐྱེས་ནས་ཐོབ་པའི་མིག་གིས་ནི་མི་མཐོང་ངོ་། །གཞན་དག་ན་རེ་ལྷའི་སྲིད་པ་བར་མ་པས་ནི་ཐམས་ཅད་མཐོང་ངོ་། །མི་དང་། ཡི་དགས་དང་། དུད་འགྲོ་དང་། དམྱལ་བའི་སྲིད་པ་བར་མ་རྣམས་ཀྱིས་ནི་གོང་མ་མ༌[^1482]གཏོགས་པའོ་ཞེས་ཟེར་རོ། །

[Block 2727 [VERSE]]
ལས་ཀྱི་རྫུ་འཕྲུལ་ཤུགས་དང་ལྡན། །
རྫུ་འཕྲུལ་ནི་ནམ་མཁའ་ལ་འགྲོ་བའོ། །

[Block 2728]
ལས་ཀྱི་རྫུ་འཕྲུལ་བྱེད་པས་ན༌[^1483]ལས་ཀྱི་རྫུ་འཕྲུལ་ལོ། །

[Block 2729]
དེའི་ཤུགས་ནི་ལས་ཀྱི་རྫུ་འཕྲུལ་གྱི་ཤུགས་དེ་མགྱོགས་པ་ཉིད་དོ། །

[Block 2730]
དེ་འདི་ལ་ཡོད་པས་ན་ལས་ཀྱི་རྫུ་འཕྲུལ་གྱི་ཤུགས་དང་ལྡན་པའོ། །

[Block 2731]
དེས་ན་འདི་ནི་སངས་རྒྱས་རྣམས་ཀྱིས་ཀྱང་དགག་པར་མི་སྤྱོད་དེ། ལས་སྟོབས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2732]
དབང་པོ་ཀུན་ཚང་། དབང་པོ་ལྔ་ཆར་ཚང་བའོ། །

[Block 2733]
ཐོགས་མེད་ལྡན། ཐོགས་པ་ནི་རྡུགས་པའོ། །

[Block 2734]
དེ་འདི་ལ་ཡོད་པས་ཐོགས་པ་དང་ལྡན་པའོ། །

[Block 2735]
ཐོགས་པ་མེད་པ་དང་ལྡན་པས་ན་ཐོགས་མེད་ལྡན་ཏེ། རྡོ་རྗེ་ལ་སོགས་པས་ཀྱང་མི་ཟློགས༌[^1484]པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
