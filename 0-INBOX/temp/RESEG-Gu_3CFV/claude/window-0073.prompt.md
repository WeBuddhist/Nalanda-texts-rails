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
[Block 2556]
སྐབས་འདི་དང་འོག་མ་དག་ལས་ཆོས་འདི་ནི་དང་པོས་ལྟུང་བར་འགྱུར་ལ་ཞེས་གསུངས་པའི་ཚིག་དེའི་རྣམ་པར་འབྱེད་པ་ནི་མདོ་ལས་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་དོན་ནི་སྤྱད་པ་ཙམ་གྱིས་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་གྱི། ཡང་དང་ཡང་དུ་ཕྱིར་བཟློག་ཅིང་མི་གཏོང་བ༌[^1636]ལ་ནི་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2557]
འབྱུང་བར་འགྱུར་བས་ཏེ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལྟུང་བ་ལས་འབྱུང་བ་དང་རྗེས་སུ་མཐུན་པ་དེ་ནི་ཕམ་པར་འགྱུར་བ་དག་ལྟར༌[^1637]ཕྱིར་བཅོས་སུ་མི་རུང་བ༌[^1638]མ་ཡིན་ནོ། །

[Block 2558]
དེ་ལྟར་ཡང་དེའི་རྣམ་པར་འབྱེད་པ་ནི་ལྟུང་བ་དང་བཅས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2559]
འདིར་ཅུང་ཟད་དགེ་སློང་མ་ལ༌[^1639]བརྟེན་ཏེ་ཕྲན་ཚེགས་དག་ལས་ཅུང་ཟད་ལྷག་པར་གསུངས་པ་དག་བསྟན་པའི་ཕྱིར་དགེ་སློང་མ་ལ་ཁྱིམ་པ་མོ་ཉིད་ཀྱི་བསྔགས་པ་བརྗོད་ན༌[^1640]སྦོམ་པོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྔགས་པ་བརྗོད་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འབྲེལ་པ་བསྟན་པས་ཡང་དག་པར་འཛིན་དུ་འཇུག་པའོ། །

[Block 2560]
འདི་ཡང་འདོད་པ་ལ་བརྟེན་པ་དང་ཕན་ཡོན་བསྟན་པས་གང་ཡང་རུང་བའི་མངོན་པར་འདོད་པ་གླེང་གཞི་ལས་རྟོགས་པའོ། །

[Block 2561]
རབ་ཏུ་འབྱུང་བ༌[^1641]འདོད་པ་རྣམས་ལ་བརྟེན་པར་མཛོད་ཅིག་ཅེས་བྱ་བ་ཉོན་མོངས་པ་དག་གིས་གནོད་པར་འགྱུར་བ་རྣམས་ཀྱིས་གོ་བར་བྱས་པ་ན་སྦོམ་དགའ་མོས་ཚིག་དེ་སྐད་བརྗོད་པ་ལས།

[Block 2562]
འདི་བཅས་ཏེ་དེ་ནི་སྨྱན་བྱེད་པ་དང་། རིགས་མཐུན་པ་ཉིད་ཡིན་པའི་ཕྱིར་འདི་དང་འབྲེལ་པ་ཉིད་ཀྱིས་འདི་རྣམས་ཤེས་པར་བྱའོ། །

[Block 2563]
དགེ་སློང་མ་སྨད་འཚོང་མར་འགྱུར་བ་སུ་ཞིག་ལ་འགའ་ཞིག་ཏུ་ཉེས་པ་མེད་པ་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་ལ་ཡང་དེའི་རྗེས་སུ་འབྲངས་པས་ཉེས་པ་སྦོམ་པོར་འགྱུར་བར་ཤེས་པར་བྱའོ། །

[Block 2564]
གཞན་སྨད་འཚོང་མ་ཉིད་བྱེད༌[^1642]དུ་འཇུག་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྦོམ་པོ་ཞེས་བྱ་བ་ལ་བསྙེག་པའི༌[^1643]དོན་དུའོ། །

[Block 2565]
བདག་ཉིད་ལ་བུད་མེད་གཞན་སྨད་འཚོང་མ་ཉིད་དུ་བྱེད་དུ་འཇུག་ན་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2566]
སྨད་འཚོང་མ་ཞེས་བྱ་བའི་སྒྲ་ནི་འཇུད་མཐུན་མ་ཞེས་བྱ་བ་སྟེ། འཇུད་པ་ཞེས་བྱ་བ་ནི་ཕོའི་དབང་པོ་ལ་བྱས་ཏེ།[^1644] འཇུད་པར་བྱེད་པ་ཡིན་པས་འཇུད་པ་སྟེ། དེས་འཇུད་པ་གང་ལ་ཡོད་པ་དེ་ནི་འཇུད་མཐུན་མ་ཡིན་ཏེ་སྨད་འཚོང་མའོ། །

[Block 2567]
བྲན་མོ་ཟོང་ཉིད་དུ་གཏོང་བ་ནི་དེ་ལས་ཕྱི་རོལ་དུ་གྱུར་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མས་བྲན་མོ་ཟོང་གི་ཕྱིར་སླར༌[^1645]གཏོང་བ་གང་ཡིན་པ་དེ་ལ་སྨད་འཚོང་མ་ཉིད་དུ་འཇུག་པ་ཞེས་བསྟན་པ་དེ་ལས་ཕྱི་རོལ་དུ་གྱུར་པ་ཉིད་མ་ཡིན་ཏེ། དོན་འདྲ་བས་འདི་ལ་ཡང་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2568]
འདི་ལྟར་ཟོང་འགྲེམས་པའི་ཚུལ་གྱིས་འཇུག་པ་འདི་ནི་གྲགས་པའི་དབང་གིས་འདི་ལྟར་མདོར་བྱས་པའོ། །

[Block 2569]
དགེ་སློང་མ་སྨྱན་བྱེད་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 2570]
གཞི་མེད་པའོ། །

[Block 2571]
བག་ཙམ་མོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ལྷག་མ་དང་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་འདི་དག་ཇི་ལྟར་སྨོས་པ་དེ༌[^1646]དགེ་སློང་མ་རྣམས་ཀྱི་ཡང་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2572]
བུད་མེད་སྐྱེས་པ་ཉིད་དང་བཅས་པ་འདི་ལ་སོགས་པ་ཐམས་ཅད་ལ་བྱེ་བྲག་ནི་འདི་ཡོད་པར་རིག་པར་བྱ་སྟེ། ཕོ་ཉིད་ལ་ནི་མོ་ཉིད་དོ། །

[Block 2573]
དེ་ལ་ཕོ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཕོའི་རྟགས་ཀྱི་གནས་སུ་ནི་མོའི་རྟགས་བལྟ་བར་བྱ་ལ། མོའི་རྟགས་ཀྱི་གནས་སུ་ནི་ཕོའི་རྟགས་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2574]
གཞི་མེད་པ་དང་བག་ཙམ་གྱི་དགེ་འདུན་ལྷག་མ་གཉིས་སོ། །

[Block 2575]
གང་ལ་ཅི་ཡང་རུང་བ༌[^1647]ལེན་པའི་དགེ་འདུན་ལྷག་མར་གྱུར༌[^1648]ཞེ་ན། དེའི་ཕྱིར་ཅི་ཡང་རུང་བ་བདག་གིར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དངོས་པོའི་ཚོགས་གང་ཡིན་པ་དེ་ནི་ཕྱག་དར་ནས་བརྩམས་ཏེ་ཅི་ཡང་རུང་བའོ། །

[Block 2576]
ཀ་ཡིག་ནི་སྨོད་པ་ལའོ། །

[Block 2577]
འཁྲིག་པའི་དངོས་པོ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པ༌[^1649]འདི་ལ་འཁྲིག་པ་ལ་ལྟོས་པའི་དབང་གིས་སྦྱིན་པར་བྱ་བ་ཉིད་ལ་རྣམ་པར་གནས་པ་ཉིད་ལ་འདིར་སྨོས་པ༌[^1650]ཞེས་བྱ་བར་ཤེས་པའོ། །

[Block 2578]
བདག་གིར་བྱེད་པ་ཞེས་བྱ་བ་ནི་རང་ཉིད་ཀྱིས༌[^1651]མངོན་པར་བསྟན་པར༌[^1652]གྱུར་པ་སྟེ་ལེན་པར༌[^1653]བྱེད་པའོ། །

[Block 2579]
དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས་བདག་གིར་བྱེད་པ་ནི་ལེན་པར་བྱེད་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཇི་ལྟ་བུར་གྱུར་པས་ཤེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་ཆགས་པར་གྱུར་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་དང་འོག་མ་དག་ལས་འཁྲིག་པའི་འདོད་ཆགས་ཀྱིས་ཆགས་པར་གྱུར་པས་ཞེས་བྱ་བའི་དོན་རྟོགས་པའོ། །

[Block 2580]
གང་ལས་བདག་གིར་བྱེད་ཅེ་ན་དེའི་ཕྱིར་སྐྱེས་པ་ཆགས་པར་འགྱུར་བ་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^1654]ཇི་ལྟ་བུ་ལས་ཤེ་ན། དེའི་ཕྱིར་ཆགས་པར་མ་གྱུར་པས་ནི་སྦོམ་པོའོ། །

[Block 2581]
ཆགས་པར་མ་གྱུར་པ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་ཆགས་པར་མ་གྱུར་པས། སྐྱེས་པ་ཆགས་པ་ལས་ཅི་ཡང་རུང་བ་དང་དུ་ལེན་པར་བྱེད་པ་ལ་ནི་སྦོམ་པོའོ། །

[Block 2582]
ཆགས་པར་མ་གྱུར་པ་ལས་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་ཚིག་གིས་ཆགས་པ་ལས་ཞེས་བྱ་བ་གོང་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 2583]
ཅུང་ཟད་ཀྱང་མི་ཤེས་པར་གྱུར་པ་ལ་སྐྱེས་པ་ཆགས་པར་གྱུར་པས་བསམ་པ་སྐྱོན་ཅན་དུ་གྱུར་པ་དང་མཐུ་དང་ལྡན་པ་ཉིད་ལ་འདི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2584]
མེད་པ་ལ་མེད་པར་ཤེས་པ་ཉིད་ཀྱིས་དེ་ལ་མངོན་པར་ཆགས་པས་ཀྱང་ལྕི་བ་ཉིད་དོ། །

[Block 2585]
[^1655]བསམ་པའི་ཉེས་པ་ལའོ། །

[Block 2586]
དེ་ལྟ་བས་ན་ཅི་ཡང་རུང་བ་བདག་གིར་བྱེད་པ་དང་། སྐྱེས་པ་ཆགས་པར་གྱུར་པ་འདི་གཉིས་ནི་ཤེས་ཀྱང་རུང་དོགས་ཀྱང་རུང་། ཡོད་ཀྱང་རུང་མེད་ཀྱང་རུང་སྟེ། ཡོད་པ་ཉིད་ལ༌[^1656]བརྟེན་པར་གྱུར་ན། དེ་ལྟ༌[^1657]ན་ཇི་སྐད་བསྟན་པ་ཉིད་དོ། །

[Block 2587]
དེ་ལ་སོགས་པ་བཅུ་གསུམ་ཁ་ཅིག་ཏུ་རྒྱུ་བའི་བཞི་པོ་དག་ལ་ནི། དགེ་སློང་རྣམས་ལ༌[^1658]གཅིག་པུ་འགྲོ་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2588]
ལྷག་མ་ལ་ནི་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2589]
འགའ་ཞིག་ཏུ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 2590]
ཡང་ན་ལྟུང་བ་མེད་པ་ནི་དཔེར་ན་ཤི་བའི་ནོར་ལེན་པ་ལྟ་བུའོ། །

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
--- END BLOCKS ---
