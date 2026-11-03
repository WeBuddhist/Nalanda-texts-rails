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
[Block 2591]
ཆོས་གོས་ཀྱི་རིན་བཀུར་བ༌[^1659]ལས་བླང་བའི་ཆོ་ག་གང་ཡིན་པ་དེ་ལས་འདས་ན་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ལ། མ་འདས་ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2592]
ཅི་ཡང་རུང་བ་ལེན་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2593]
གང་ལ་ཅི་ཡང་རུང་བ་ལེན་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཆགས་པར་མ་གྱུར་པས་ཆགས་པར་གྱུར་པ་ལས་ཅི་ཡང་རུང་བ་བདག་གིར་བྱེད་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་དགེ་སློང་མ་ལ་གོ་བར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆགས་པར་མ་གྱུར་པས་ཞེས་བྱ་བ་ནི་འདིར་འདོད་ཆགས་མངོན་སུམ་དུ་མ་གྱུར་པ་ལ་བྱའི་མི་ལྟོས་པ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2594]
དགེ་སློང་མ་ཆགས་པར་མ་གྱུར་པས་སྐྱེས་པ་ཆགས་པར་གྱུར་པ་ལས་ཅི་ཡང་རུང་བ་བདག་གིར་བྱེད་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2595]
དེ་བཞིན་དུ་དགེ་སློང་མ་ལ་གོ་བར་བྱེད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2596]
དེ་ལྟར་ཡང་སྦོམ་དགའ་མོས་གཙུག་དགའ་མོ་ལ་ཀྱེ་ཁྱོད་ཆགས་པར་མ་གྱུར་ན། ཁྱོད་ཆགས་སུ་མེད་པས་ཆགས་པར་གྱུར་པ་ལས་ཅི་ཡང་རུང་བ་བདག་གིར་བྱ་བ་རུང་ངོ་ཞེས་ཉེས་པ་སྦོམ་པོ་ཡང་དག་པར་ལེན་དུ་བཅུག་པ་དེ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་གསུངས་པ་ཡིན་པས། དེའི་ཕྱིར་ཆགས་པར་གྱུར་པ་ལས་བདག་ཏུ་བྱ་བ་ཅི་ཡང་རུང་བ་ལེན་དུ་འཇུག་པ་ལ་ཤིན་ཏུ་ལྕི་བ་ཉིད་ཀྱི་ཕྱིར་ཁ་ན་མ་ཐོ་བ་འདིར་གཏོགས་པར་བྱའོ། །

[Block 2597]
ལྟོས་པ་མེད་པས་གཟུང་བ་ལན༌[^1660]དུ་འཇུག་པ་ལ་བར་དུ་གཅོད་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་ཁ་ན་མ་ཐོ་བའི་ཚིག་ཅན་འདི་ལ༌[^1661]སྦོམ་པོར་རྟོགས་པར་བྱའོ། །

[Block 2598]
ཅི་ཡང་རུང་བ་ལེན་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2599]
འོག་མ་བཞི་པོ་དག་ལ་ནི་དགེ་སློང་མ་མེད་པར་རོ་ཞེས་བྱ་བ་ནི་མཚན་མོ་འབྲལ་བ་ལ་སོགས་པ་རྣམས་ལ་འདིའི་འོག་མ་བསླབ་པའི་གཞི་བཞི་པོ་དག་ལ་དགེ་སློང་མ་མེད་པར་འགྲོ་ན་ཚིག་འདི་རྟོགས་པར༌[^1662]བྱའོ། །

[Block 2600]
དགེ་སློང་མ་ཉིད་ནི་སུམ་ཆ་དང་བྲལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སུམ་ཆ་དང་བྲལ་ཞིང་སུམ་གཉིས་ཡོད་པ་མ༌[^1663]ཡིན་ཏེ། གང་གི་ཕྱིར་དགེ་སློང་མ་སུམ་ཆ་མ་ཡིན་ཏེ། དགེ་སློང་མ་མ་ཡིན་པ་མ་ཡིན་ཏེ་དེ་དགེ་སློབ༌[^1664]མ་ལས་སུམ་ཆ་གཉིས། དགེ་སློང་མ་དང་བྲལ་བས་རྗེས་སུ་བསྒྲུབ་པར་མི་འགྱུར༌[^1665]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2601]
འདིར་སུམ་ཆར་གྱུར་པའི་སུམ་ཆའི་ཚིག་ལ་དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བའི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2602]
དེ་མ་ཐག་པའི་ཚིག་ལ་ཉེས༌[^1666]བྱས་ཕྲ་མོར་འགྱུར་རོ། །

[Block 2603]
གསུམ་པ་ལ་ཤིན་ཏུ་མ་ཆོག་པ་དེ་བས་ན་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 2604]
དགེ་ཚུལ་མ་ནི་སུམ་ཆའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་མ་དེ་ནི་དགེ་སློང་མ་དང་ལྷན་ཅིག་འགྲོགས་པའི་སུམ་ཆ་རྗེས་སུ་བསྒྲུབ་ཅིང་དགེ་སློང་མ་དང་བྲལ་བ་ལ་རྗེས་སུ་བསྒྲུབ་པར་འགྱུར་ཏེ། གཉིས་པོ་ནི་རྗེས་སུ་མ་གྲུབ་པར་འགྱུར་རོ། །

[Block 2605]
དེ་བས་ན་འདིར་སྦོམ་པོ་ཆ་གཅིག་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་ཆུང་བར་འགྱུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2606]
མི་འདོད་བཞིན་དུ་འབྲལ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་ཉེས་པ་མེད་དོ་ཞེས༌[^1667]བྱ་བ་ནི་དེ་ལྟ་བུར་གྱུར་པའི་བྲལ་བ་ལ་ལྟུང་བ་མི་སྐྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2607]
འདིར་གཞུང་ནི། གལ་ཏེ་ཕྱི་བཞིན་དུ་འབྲང་བའི་དགེ་སྦྱོང༌[^1668]མ་བརྡེགས༌[^1669]སམ། ཤིའམ་ཉམས་སམ་ལྟུང་བར་གྱུར་ཏམ། གཞན་གྱི་ཡུལ་འཁོར་རམ་གཞན་གྱི་ཡུལ་དུ་བྲོས་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2608]
མི་འདོད་པ་ལས་སྐྱེས་པ་བྲལ་བ་རྩེ་གཅིག་པ་ཉིད་དུ་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2609]
འདིར་རྒྱུ་མཚན་གཞན་ཡང་འཕྲོག་པ་དང་ཉམས་པ་ལ་སོགས་པ་ཡོད་པ་མ༌[^1670]ཡིན་ཏེ། དེ་བས་ན་དེ་སྐད་ཅེས་སྨོས་སོ། །

[Block 2610]
ཁྱིམ་པའི་དངོས་པོར་གཏོགས་པ་ལ་འདིར་དགེ་སློང་མ་ཉིད་དུ་གཏོགས་པ་ལ་ཉམས་པ་ལ༌[^1671]ཞེས་སྨོས་སོ། །

[Block 2611]
ལྟུང་བ་ཞེས་བྱ་བ་འདིས་ནི་ལྟུང་བ་ཉིད་བསྟན་པ་ཡིན་ཏེ། ལྟུང་བ་ཞེས་བྱ་བ་ནི་ཕམ་པར་འགྱུར་བའོ། །

[Block 2612]
བར་ཆད་བྱུང་བའི་དབང་ཉིད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སྦྱོང་གི་ཚུལ་དང་། ཚངས་པར་སྤྱོད་པའི་བར་ཆད་བྱུང་བའི་དབང་ཉིད་ཀྱིས་ཁྲིམས་ཟླ་དང་བྲལ་བ་ལ་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2613]
དུས་དང་འབྲེལ་པ་ལས་མཐའ་ཉིད་ཀྱི་མདུན་རོལ་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དུས་འགའ་ཞིག་ལ་བརྟེན་པའི་བྱ་བའི་ཁྱད་པར་གང་ཞིག་བརྗོད་པ་ནི་འདི་ལྟ་སྟེ། དཔེར་ན་མཚན་མོ་དང་ཉིན་མོའི་དུས་ཀྱི་མཐའི་སྐད་ཅིག་མ་ལ་བྱ་བ་གང་འབྱུང་བ་དེ་ལ་ནི་དངོས་གཞི་ཉིད་དུ་འགྱུར་རོ། །

[Block 2614]
མདུན་རོལ་དུ་ནི་དེའི་གང་ཞིག་དེ་མ་ཐག་པའི་ཚིག་ཉིད་ཀྱི་དོན་ཏོ།[^1672] །དུས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ལས་གང་ཞིག་མདུན་རོལ་གྱི་དུས་སུ་བྱ་བ་གང་ཡིན་པ་དེ་ལ་ནི་སྦྱར་བ༌[^1673]ཉིད་དོ། །

[Block 2615]
མཐའི་དུས་སུ་གྱུར་པ་ཉིད་ལ་བྱ་བ་གང་ཡིན་པ་དེ་ལ་ནི་དངོས་གཞི་ཉིད་ཡིན་ནོ། །

[Block 2616]
དེ་གང་ལ༌[^1674]ཤེས་ཤེ་ན། དེའི་ཕྱིར་དབྱར་ཁང་དང་བྲལ་བར་གྱུར་ཅིང་གཞན་དུ་མཚན་མོ་སྐྱ་རེངས་འཆར་བར་བྱེད་ནའོ་ཞེས་གསུངས་པ་ལ་སྟེ། དགེ་སློང་མ་གཅིག་པུ་དབྱར་ཁང་གི་ཕྱི་རོལ་གཞན་དུ་མཚན་མོ་སྐྱ་རེངས༌[^1675]འཆར་བར་བྱེད་ན་ཐམས་ཅད་དུ་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ་ཞེས་གསུངས་པ་དེ་གཉིས༌[^1676]ཀྱིས་ནི་འདིར་ཉིན་མོ་འབྲལ་བ་དང་། མཚན་མོ་འབྲལ་བ་གཉིས་བསྟན་ཏོ། །

[Block 2617]
འདིར་མཐར༌[^1677]ཙམ་ལ་དངོས་གཞིར་གསུངས་པས་དེའི་ཕྱིར། མདུན་རོལ་གྱི་དུས་ལ་ནི་སྦྱོར་བ་ཉིད་ཁོ་ནར་སྦྱར་ཏེ། དེ་བས་འདི་ལྟར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 2618]
ཉི་མ་ནུབ་པའི་མཐའ་ནི་ཉིན་མོའི་མཐའ་ཡིན་ནོ༌[^1678]ཞེས་བྱ་བ་ནི། ཉི་མ་ནུབ་ཀར་འཇུག་པའི་མཐའ་ནི་ཉིན་མོའི་མཐའོ། །

[Block 2619]
དེ་ཕན་ཆད་ནི་མཚན་མོར་གཏོགས་པའི་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2620]
འོག་མ་བཞི་པོ་དག་གི་ཐུན༌[^1679]མོང་གི་མཚན་ཉིད་བཤད་ཟིན་ཏོ། །

[Block 2621]
ད་ནི་སོ་སོར་རྟོགས་པ༌[^1680]བརྗོད་པར་བྱ་སྟེ། གང་ལ་མཚན་མོ་འབྲལ་བའི་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ༌[^1681]ཞེ་ན། དེའི་ཕྱིར་མཚན་མོ་དབྱར་ཁང་ལས་ཕྱི་རོལ་དུ་གྱུར་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དབྱར་ཁང་ན་གནས་པ་ནི་གནས་ཉིད་ཀྱི་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ། ཁྱིམ་གྱི་ནང་དུ་ཡང་འདིར་གནས་པ་ཉིད་དུ་བརྟེན་པ་འཕེན་པའོ། །

[Block 2622]
གྲོང་དང་སྐྱེད་མོས་ཚལ་ལ་སོགས་པའི༌[^1682]ཕྱི་རོལ་གྱི་གནས་ལ་བསྙེགས་པའོ། །

[Block 2623]
དགོན་པ་ལ་ཡང་དོན་དང་བཅས་པའི་ས༌[^1683]ཕྱོགས་ཀྱི་ཕྱོགས་གཅིག་ལ་སོགས་པ་ཡང་བསྙེགས་པའོ། །

[Block 2624]
བུད་མེད་འཇུག་པ་ལ་ཡང་འདི་རྣམ་པར་སྦྱོར་བ་གང་ཞིག་དེ་ལ་སོགས་པ་ངེས་པ༌[^1684]བཞི་པོ་རྣམས་སོ། །

[Block 2625]
དེ་བས་ན་འདིར་ཕྱི་རོལ་གྱི་ངོས་ནི་དབྱར་ཁང་གི་མཚམས་སོ། །

[Block 2626]
གལ་ཏེ་འདི་ལ་སྐོར་བ༌[^1685]ཡོད་ན་ནི་དེ་ཉིད་ལའོ། །

[Block 2627]
གལ་ཏེ་མེད་ན་ནི་དེ་ཉིད་ལའོ། །

[Block 2628]
མཚན་མོ་འབྲལ་བའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2629]
གང་ལ་ཉིན་མོ་བྲལ་བའི༌[^1686]དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཉིན་མོའི་ཞེས་བྱ་བ་སྨོས་ཏེ། དབྱར་ཁང་ལ༌[^1687]ཕྱི་རོལ་དུ་གྱུར་ནའོ་ཞེས་བྱ་བར་སྦྱོར༌[^1688]རོ། །

[Block 2630]
གཅིག་པུ་ཉེ་དུའི་ཁྱིམ་དུ་ཟན་གྱི་ཕྱིར་ལོ་ཉེས་བྱུང་བའི་ཕྱིར་ཉེ་དུ་རྣམས་དང་ལྷན་ཅིག་འབྲེལ་པའི་ཉེ་བར་སྤྱོད་པའི་གནང་བ་ཐོབ་ན་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1689]གླེང་གཞི་དག་ལས།
--- END BLOCKS ---
