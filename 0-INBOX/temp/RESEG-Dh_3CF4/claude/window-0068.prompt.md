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
[Block 2381]
དབང་བསྐུར་ཀྱང་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་དབང་བསྐུར་བར༌[^1505]གྱུར་ཀྱང་ངོ་། །ལྷ་ཡི་བུ་ལོན་བྲལ་བར་མཛད་པའི་རིགས།[^1506] །ཞེས་བྱ་བ་འདིས་ནི་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པའི་དབང་དུ་བྱས་ནས་བརྩམས་པའི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 2382]
ད༌[^1507]ནི་སྐྱེ་དགུ་རྣམས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པའི་དབང་དུ་བྱས་ནས་མཆོད་སྦྱིན་ལེགས་པར་བགྱིས་པས་ཞེས་བྱ་བའི༌[^1508]ཚིགས་བཅད་དོ། །

[Block 2383]
དེ་བས་འབངས་ལ་ཕན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མཆོད་སྦྱིན་ལེགས་པར་བྱས་པས་ལྷ༌[^1509]མཉེས་པར་གྱུར་ཏེ་ཆར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2384]
བདག་ལ་ཕན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དགྲ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 2385]
གྲགས་པར་འགྱུར་བའི་ཞེས་བྱ་བ་ནི་གཉིས་ཀར་གྲགས་པར་འགྱུར་བ་ཉིད་ཀྱི་མཆོད་སྦྱིན་གྱི་ཆོ་གའོ། །

[Block 2386]
གཞན་གྱི་དྲིང་ལ་འཇོག་པ་ནི་གཞན་གྱི་དྲིང་འཇོག་པའོ། །

[Block 2387]
ཡང་ན་གཞན་གྱིས༌[^1510]བཀྲིར་རུང་བ་ནི་གཞན་གྱི་དྲིང་ལ་འཇོག་པ་སྟེ། དད་པ་སྐྱེ་བ་ལ་རག་ལུས་པའོ། །

[Block 2388]
བློ་ཆུང༌[^1511]བའི་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་གཞན་གྱི་དྲིང་ལ་འཇོག་ཅིང་བློ་ཆུང་བའི་འགྲོ་བའོ། །

[Block 2389]
སྤྱོད་མི་ནུས་པ་ནི་རིག་པ༌[^1512]ལ་ཉེ་བར་གནས་པའི་སེམས༌[^1513]མེད་པས་སོ། །

[Block 2390]
ཆོས་ཙམ་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་བསོད་ནམས་འདོད་པའོ། །

[Block 2391]
ཆོས་ནི་འདིར་ཆོས་ཀྱི་འབྲས་བུ་ལ་རིག་པར༌[^1514]བྱའོ། །

[Block 2392]
འཇིག་རྟེན་དག་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ཚད་མར་བྱས་ན་སྐྱེ་བོ་མང་པོ་ལ་ཕན་པ་དང་མི་མཐུན་པ་ཡིན་ཏེ།

[Block 2393 [VERSE]]
ལོང་བས་བསྟན་པའི་ལོང་བའི་སྐྱེ་བོ་བཞིན་ནོ། །
ངན་སོང་མི་བདེ་དོགས་པའི་ནང་ན་འཁོད། །

[Block 2394]
ཅེས་བྱ་བ་ནི་བསོད་པ༌[^1515]ནི་ཆོས་སུ་སྦྱོར་བའི་བྱེད་པ་པོ་དེ་ཉིད་ཀྱང་ངན་སོང་མི་བདེ་བ་དོགས་པའི་ནང་ན་འཁོད་པར་བསྟན་ཏོ། །

[Block 2395]
ད་ནི་དེ་ཉིད་སྒྲུབ་པའི་ཕྱིར། ཕྱུགས་རྣམས་བསད་པས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་ལྔ་སྨོས་ཏེ། དེ་ལས་ཕྱུགས་རྣམས་བསད་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་དམ་བཅས་པའི་ཚིགས་བཅད་དེ་སྒྲུབ་པའི་རྗེས་སུ་བསྟན་པས་སོ། །

[Block 2396]
འདིའི་བསྡུས་པའི་རྒྱུ་དང་འབྲས་བུའི་མཚན་མའི་རྟགས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། ཆོས་ཀྱི་རྒྱུ་ནི་ཕྱུགས་རྣམས་གསོད༌[^1516]པའོ། །

[Block 2397]
དེ་ནི་མི་རིགས་པ་ཁས་ལེན་པ་སྟེ་འདིས་ནི་ལྷའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བའི་འབྲས་བུ་དེ་ཡང་མི་རིགས་པ་ཉིད་དུ་དམ་བཅས་པ་ཡིན་ནོ། །

[Block 2398]
ལྷ་མཉེས་པའི་ཆེད་དུ་ཞེས་བྱ་བ་དེ་ཡང་མི་རིགས་པ་ཉིད་དུ་དམ་བཅའ་བ༌[^1517]ཡིན་ཏེ། ཕྱུགས་རྣམས་བསད་པ༌[^1518]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་ཇི་ལྟར་མཆོད་སྦྱིན༌[^1519]པ་དེ་དག་ཕྱུགས་རྣམས་བསད་པ་ཆོས་ཉིད་དུ་རིགས་པར་སྟོན་པར་བྱེད་དེ། དེ་མི་རིགས་པའི་དབང་དུ་བྱས་ནས་ཕྱུགས་རྣམས་བསད་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨྲས་སོ། །

[Block 2399]
སྔགས་ཀྱི་མཐུས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་མཆོད་སྦྱིན་པ་དེ་དག་ཕྱུགས་བསད་པ་ཉི་ཚེས་ནི་ཆོས་ཉིད་དུ་མི་སྟོན་ཏེ་འོན་ཀྱང་སྔགས་ཀྱི་མཐུ་དང་ལྡན་པས་བསད་ན་ནི་མཐོ་རིས་སུ་འགྲོ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྔགས་ཀྱི་མཐུས་བསད་ན་དེ་ཡང་རྒྱུ་སྦྱོར་བ་དང་མངོན་པར་མཐོ་བ་ལ་སྦྱོར་བའི་བྱེད་པ་པོ་དང་། གསད་པར༌[^1520]བྱ་བ་ཉིད་ཀྱིས༌[^1521]མཐོ་རིས་ཀྱི་རྒྱུ་ཡིན་པས་གཞན་གྱི་ཁ་ན་མ་ཐོ་བ་མེད་ཅིང་བདེ་བ་དང་ཕན་པ་ལ་འཇུག་པའི་ཆོས་ཏེ། ཆོས་དེ་ནི་ལྷའི་འཇིག་རྟེན་དུ་སྐྱེ་བའི་རྒྱུའོ། །

[Block 2400]
སྔགས་ཀྱི་མཐུས་བསད་པའི་ཕྱུགས་མཐོ་རིས་སུ་འགྲོ་བ༌[^1522]ག་ལས་ཤེ་ན། གཞན་གྱིས་བྱས་པའི་ལས་ཀྱིས་གཞན་གྱི་འབྲས་བུར་སྨིན་ཅིང་སྟེར་བ་མི་རིགས་པ་ཡིན་ཏེ། གཞན་གྱི་རྒྱུད་ཀྱི་སེམས་ཀྱིས་བྱས་པ་ནི་བྱེད་པ་པོ་དེ་ཉིད་ལ་དགེ་བ་དང་མི་དགེ་བར་འགྱུར་བ་ཡིན་གྱི། གཞན་ལ་ནི་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། བསད་པ་དང་དེ་ཉིད་དུ་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2401]
བསད་པ་དང༌[^1523]དེ་ཆོས་དང་མཐུན་པ་ཡིན་པ་ལ། བསད་པ་འབྲས་བུ་དང་ལྡན་པར་གྱུར་ན་ཡང་བདག་ཉིད་ཀྱི་ལྷའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་དེ་མེད་པས་དེ༌[^1524]ཡང་མེད་དོ། །

[Block 2402]
དོན་འདི་ཉིད་སྒྲུབ་པའི་ཕྱིར་ལོག་པར་སྤྱོད་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2403]
གཞན་གྱིས་བསད་པའི༌[^1525]ཕྱུགས་མཐོ་རིས་སུ་མི་འགྲོ་སྟེ། བསམ་པ་དང་སྦྱོར་བ་གཉིས་ཀྱིས་དགེ་བ་དང་མི་དགེ་བའི་རྟགས་མེད་པའི་ཕྱིར་རོ། །

[Block 2404]
ལོག་པར་སྤྱོད་པས་ཡིད་ནི་མ་བཟློག༌[^1526]ཅིང་། །ཞེས་བྱ་བ་འདིས་ནི་སྡིག་པ༌[^1527]ལས་ལྡོག་པ་མེད་པ་བསྟན་པ༌[^1528]སྟེ་བསམ་པས་སོ། །

[Block 2405]
དགེ་བའི་ལས་ལ་ངེས་པར་མ་བྱས་པ། །ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་དང་སྦྱོར་བ་གཉིས་ཀྱིས༌[^1529]དགེ་བ་ལ་འཇུག་པ་མེད་པར་བསྟན་ཏོ། །

[Block 2406]
སེམས་པ་ནི་རྣམ་པ་གསུམ་སྟེ། ཀུན་ཏུ་སྦྱོར་བ་དང་། ངེས་པར་སེམས་པ་དང་ཚོལ་བའོ། །

[Block 2407]
ཀུན་ཏུ་སྦྱོར་བ་དང་། ངེས་པར་སེམས་པས་བསྐྱོད་པའི་སེམས་ཀྱིས་ལས་ངེས་པར་བྱེད་པ་ཉིད་ན། འདིས་ནི་དེ་དག་མེད་པས་སྦྱོར་བ་མེད་པར་བསྟན་ཏེ།

[Block 2408 [VERSE]]
དགེ་བའི་མཚམས་སྦྱོར་བ་མེད་པར་བསྟན་པའི་ཚུལ་ལོ། །
ཡང་ན་ཕྱུགས་ནི་མཐོ་རིས་སུ་མི་འགྲོ་སྟེ།
རང་གིས༌[^1530]བྱས་པའི་དགེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2409]
དགེ་བ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལྡོག་པ་དང་། འཇུག་པའི་མཚན་ཉིད་དོ། །

[Block 2410]
མི་དགེ་བ་དག༌[^1531]ལས་ལྡོག་པ་ནི་བསམ་པ་དང་སྦྱོར་བ་གཉིས་ཀྱིས་སོ། །

[Block 2411]
དགེ་བ་དག་ལ་འཇུག་པ་ལ་ཡང་བསམ་པ་དང་སྦྱོར་བ་གཉིས་ཀྱིས་སོ། །

[Block 2412]
ཡིད་ངེས་པ༌[^1532]ཞེས་བྱ་བས་ནི་མི་དགེ་བ་ལས་བསམ་པས༌[^1533]ལོག་པ་མེད་པ་དང་། དགེ་བ་ལ་འཇུག་པའི་བསམ་པ་མེད་པར་བསྟན་ཏོ། །

[Block 2413]
དེ་མེད་བ་ལས༌[^1534]དགེ་བ་ལས་ལྡོག་པའི་སྦྱོར་བ་མེད་པ་དང་། དགེ་བ་ལ་འཇུག་པའི་སྦྱོར་བ་མེད་པར་བསྟན་ཏོ། །

[Block 2414]
བསམ་པ་སྔོན་དུ་འགྲོ་བས་དགེ་བ་དང་མི་དགེ་བ་ལ་འཇུག་པ་དང་ལྡོག་པ་ཡིན་ནོ། །

[Block 2415]
ཕྱུགས་མཐོ་རིས་སུ་འགྲོ་བ་དེ་མི་རིགས་པ་ཉིད་དུ་སྒྲུབ་པའི་ཕྱིར། མཆོད་སྦྱིན་ལ་བསད་ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2416]
ཕྱུགས་སུ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཕྱུགས་དག༌[^1535]མཆོད་སྦྱིན་དུ་བསད་པ་དེ་བཞིན་དུ་ཁྱེད་བདག་ཉིད་གསོད་པར་བྱེད་པའོ། །

[Block 2417]
མཆོད་སྦྱིན་ལ་ནི་ཚུལ་འདི་ཡིན་ཏེ། བདག་ཉིད་གསོད་པའི་ཚུལ་ལོ། །

[Block 2418]
དེ༌[^1536]ཕྱིར་དེ་དག་ཚིག་ནི་སུ་ཞིག་ཉན། །ཞེས་བྱ་བ་ནི་ཇི་སྐད་སྨྲས་པ༌[^1537]དེ་བཞིན་དུ་ནི༌[^1538]མི་བྱེད་ན༌[^1539]ནི་ཚིག་བཙུན་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2419]
དེ་ལྟར་ལྷའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་མི་རིགས་པར་བསྟན་ནས། བསྟན་མ་ཐག་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ལྷ་མཉེས་པར་འགྱུར་བ་ཉིད་དུ་མི་རིགས་པར་བསྟན་པའི་ཕྱིར། མཚུངས་མེད་མཐུ་བསུང༌[^1540]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2420]
བསུང༌[^1541]ཉིད་མཐུ་ཡིན་པས་མཐུ་བསུང༌[^1542]ངོ་། །མཐུ་བསུང༌[^1543]དང་། རོ་དང་། གཟི་ནི༌[^1544]མཚུངས་མེད་མཐུ་བསུང༌[^1545]ལྡན་པའོ། །
--- END BLOCKS ---
