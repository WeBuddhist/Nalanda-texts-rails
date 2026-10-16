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
[Block 2486 [VERSE]]
དེ་གཅིག་དེ་ཉིད་རིགས་གཞན་མིན། །
ཞེས་བྱའི་ཁྱད་པར་གང་གིས་བྱས། །
དེ་བཞིན་སྐྱེས་ཡིན་རྣམ༌[^1698]འགས་ཀྱང་། །
ཁྱོད་ཅི་ཤེས་ཅན་འགའ་མི་འདོད། །

[Block 2487]
རིག་བྱེད་པའི་སྒྲ་དེ་དག་བྲམ་ཟེ་ཁྱོད་ཚུར་ཤོག །ཁོ་བོའི་དོན་འདི་ཟུང་ཤིག །གཞན་ནི་མ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་བརྗོད་པར༌[^1699]མི་བྱེད་དོ། །

[Block 2488]
མངོན་པར་གསལ་བ་མ་ཡིན་པའི་དོན་གྱི་ཁྱད་པར་དང་འདྲེ་བ་ཅན་འགའ་ཞིག་གིས་མཉན་པ་ཉིད་སྐྱེད་པར་བྱེད་དོ། །

[Block 2489]
དེ་ལ་སྐྱེས་བུ་གཅིག་གིས་དོན་ཅུང་ཟད་གཅིག་དང་གཞན་གྱིས་གཞན་བརྟགས་པ་ཡིན་གྱི། སྒྲ་རྣམས་ཀྱི་རང་བཞིན་སོ་སོར་ངེས་པ་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ན། གང་གིས་དོན་གཅིག་གི་རྗེས་སུ་བྱེད་ཅིང་གཞན་མ་ཡིན་ཏེ། འོན་ཀྱང་བརྡའི་དབང་གིས་དེ་དང་དེ་བཟུང་བ་ན་མཐོང་བར་འགྱུར་རོ། །

[Block 2490]
ལྐོག་ཏུ་གྱུར་བ་གོམས་པའི་ཕྱིར་ཉེས་པས་བསླད༌[^1700]ཅིང་མི་མཁས་བ་འགའ་ཞིག་དོན་ངེས་པ་རིགས་པ་མེད་པ་ཅན་དེ་དག་དེ༌[^1701]ཁོ་ན་ཉིད་དུ་འཆད་པར་བྱེད་པ་ཡིན་ལ། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2491]
ཅི་སྟེ་འགའ་ཞིག་ལས་བློ་དང་དབང་པོ་ལ་སོགས་པ་དག་དེ་ཉིད་ཀྱིས་རིགས་པ་ཡིན་གྱི། གཞན་གྱིས་ནི་མ་ཡིན་ནོ།[^1702] ། དེའི་དབང་པོ་ལས་འདས་པའི་ཤེས་པའི་ཁྱད་པར་འདི་གང་ལས་ཡིན། དེ་བཞིན་དུ་ཡུལ་དང་དུས་དང་རང་བཞིན་གྱི་བསྐལ་པའི་དོན་དག་མཐོང་ན་གཞན་དག་ཀྱང་ཅིའི་ཕྱིར་མེད་པ་ཅན་མཐོང་བ་ཡིན། དེ་སྤོང་བར་བྱེད་པའི་སྒྲུབ་པར༌[^1703]བྱེད་པ་གང་ཡིན་པ༌[^1704]འགའ་ཞིག་ཀྱང་དེ་དག་གིས་དམིགས་པ་མ་ཡིན་ནོ། །

[Block 2492]
ཇི་ལྟར་དེའི་སྒྲུབ་པར་བྱེད་པ་ཡོད་ན་ཡང་འདིའི་ཁྱེད་པར་འདི་ཡིན་པ་དེ་ལྟར་གཞན་གྱིས༌[^1705]ཡང་འགྱུར་བ་དེ་ལྟར་ན་མངོན་པར་ཞེན་པ་མེད་པར་རིགས་པ་ཡིན་ནོ། །

[Block 2493 [HEADING]]
### ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་ལ་ཚད་མ། ^7-4-0

[Block 2494 [VERSE]]
གལ་ཏེ་གང་ཚིག་ཚད་མ་ཡིས། །
མི་སླུ་དེ་དོན་རིག་ཡིན་ན། །
ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་ལ། །
ཚད་མ་སྲེད་པ་ཡོད་མ་ཡིན། །

[Block 2495]
དེ་ལྟར་ནི་འགྱུར་ན་ཁོ་བོས་སྐྱེས་བུ་ཚད་མར་གྱུར་པའི༌[^1706]ཕྱིར། འགའ་ཞིག་གི་བཤད་པ་ལ་མངོན་པར་ཞེན་པ་མ་ཡིན་ནོ། །

[Block 2496]
འོ་ན་ཅི་ཡིན་ཞེ་ན། ཚད་མ་གཞན་གྱིས་མི་སླུ་བའི་ཕྱིར་རོ། །

[Block 2497]
འཆད་པ་པོ་མང་པོ་དག་ཡོད་ན་ཡང་མངོན་སུམ་ལ་སོགས་པའི་ཚད་མ་སྟོན་པར་བྱེད་པ༌[^1707]གང་ཡིན་པ་དེ་ཁས་ལེན་ཏོ་ཞེ་ན།[^1708] དེ་ནི་མ་ཡིན་ཏེ། དབང་པོ་ལས་འདས་པ་མ་མཐོང་བ་ལ་སོགས་པ་ཚད་མ་གཞན་མི་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2498]
དེ་འཇུག་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་རྟོགས་པར་བྱ་བའི་ཕྱིར། ལུང་དོན་དུ་གཉེར་བ་ཡིན་ནོ། །

[Block 2499]
དེ་ལྟ་མ་ཡིན་ན་དེ་ཡོད་དུ་ཟིན་ཀྱང་ཚད་མ་གཞན་འཇུག་པ་མེད་པ་ན་དོན་རྟོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2500]
ཡན་གར་བ་དེ་ལས་རྟོགས་པའི་ཕྱིར་ལུང་སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 2501]
གལ་ཏེ་གཞན་ཡན་གར་བ་ལས་ཀྱང་དབང་པོ་ལས་འདས་པ་དག་རྟོགས་པར་མི་འགྱུར་རོ་ཞེ་ན།[^1709] ཇི་ལྟར་དབང་པོ་ལས་འདས་པ་ཞེས་བྱ་བ་དང་། མངོན་སུམ་ལ་སོགས་པའི་ཡུལ་ཡང་ཡིན། གལ་ཏེ་དེ་དག་ཀྱང་རང་གི་ཡུལ་ལ་ཡང་ལུང་ལ་ལྟོས་ནས་སྒྲུབ་པར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། དུ་བ་ལ་སོགས་པ་ལས་མེ་ལ་སོགས་པའི་ཤེས་པ་ལུང་མེད་པ༌[^1710]ཅན་དུ་མི་འགྱུར་རོ། །

[Block 2502]
གལ་ཏེ་ལུང་འཇུག་པ་ལ་ཚད་མ་གཞན་ཚོལ་བ༌[^1711]ནི་མ་ཡིན་ནོ། །

[Block 2503]
འོ་ན་ཅི་ཞེ་ན། ལུང་གི་འཇུག་པ་དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན། རབ་ཏུ་སྒྲུབ་པ༌[^1712]བདག་ཉིད་ནུས་པ་འདི་ལུང་དེ་ཉེ་བས༌[^1713]ཕུལ་དུ་བྱུང་བ་ཅི་ཞིག་གསོ་བར་བྱེད། ནུས་པ་མེད་ན་ནི་ལུང་འཇུག་ཏུ་ཟིན་ཀྱང་སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 2504]
དབང་པོ་ལས་འདས་པའི་དོན་དང་འབྲེལ་པའི་ལུང་གི་འཇུག་པ༌[^1714]དེ་ཡང་དབང་པོ་ལས་འདས་པར་ཇི་ལྟར་གཞན་གྱིས་གྲུབ་པ་ཡིན་ཏེ། གཞན་ཡང་དེ་བཞིན་དུ་ལུང་གི་མཚན་ཉིད་དུ་འགྱུར་རོ། །

[Block 2505]
དེ་ལྟར་ན།

[Block 2506 [VERSE]]
གང་གི་ཚིག་ནི་ཚད་མ་ཡིས། །
མི་སླུ་བ༌[^1715]ཅན་དེ་བྱས་ཚིག །
[^1716]དེ་ལུང་ཞེས་ཐོབ་དེ་ཡི་ཕྱིར། །
སྐྱེས་བུས་བྱས་མིན་དོན་མེད་ཡིན། །

[Block 2507]
ལུང་སྨྲ་བར་མཚུངས་ན་ཡང་ཚད་མའི་སྟོབས་ཀྱིས་ལུང་ནི༌[^1717]ལ་ལར་ལུང་ཉིད་ཡིན་ཏེ། ཚད་མས་མི་སླུ་བའི་ཚིག་དག་ལུང་གི་མཚན་ཉིད་ཡིན་པར་འགྱུར་རོ། །

[Block 2508]
སྐྱེས་བུས་བྱས་པ་ནི་མ་ཡིན་ཏེ། དེ་ནི་ཐམས་ཅད་ལ་མཚུངས་པ་ཡིན་ན་ཡང་རྟོགས་པ་ཚད་མས་གནོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2509]
དེ་ཡོད་ན་ཡང་གཞན་དུ་ཚད་མ་གཞན་གྱིས་སླུ་བ༌[^1718]ལ་མི་འདོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2510]
གཞན་ཡང་།

[Block 2511 [VERSE]]
གལ་ཏེ་ཤིན་ཏུ་ལྐོག་གྱུར་དོན། །
ལུང་མེད་ཤེས་པ་ཡོད་ན་ནི། །
དབང་པོ་ལས་འདས་དོན་རིག་འགའ། །
ཡོད་དོ་ཞེས་ནི་མངོན་འདོད་འགྱུར། །

[Block 2512]
གལ་ཏེ་སྐྱེས་བུ༌[^1719]ལུང་ལ་ལྟོས་པ་མེད་པའི་ཤེས་པ་ཇི་ལྟ་བ་དེ་ལྟ་བུ་ཉིད་ལྐོག་ཏུ་གྱུར་པའི་དོན་ལ་འདོད་ན། དབང་པོ་ལས་འདས་པའི་དོན་མཐོང་བའི་སྐྱེས་བུ་ཡོད་དོ་ཞེས་འདོད་པར་འགྱུར་རོ། །

[Block 2513]
མངོན་སུམ་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཚད་མ་ནི་དེ་མཐོང་བ་མེད་པ་ལ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2514]
མངོན་སུམ་འཇུག་པ་མེད་པའི་ཕྱིར། །དེ་དག་ལ་ཚད་མ་གཞན་མི་སྲིད་པ་ན་དེ་ལ་དམིགས་པ་མ་ཡིན་པ་རྟོགས་པར་བྱ་བ་ལུང་ཚད་མ་ཡིན་ནོ། །

[Block 2515]
ཚད་མ་གཞན་འཇུག་པ་མངོན་སུམ་སྒྲུབ་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར། སྐྱེས་བུའི་ཕུལ་དུ་བྱུང་བ་དག་བཟློག་པར་མི་འགྱུར་རོ། །

[Block 2516]
དེ་བས་ན་དབང་པོ་ལས་འདས་པ་དག་ལ་ཚད་མ་གཞན་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 2517]
དེ་ཉིད་ཀྱི་ཕྱིར་ལུང་དོན་གྱི་ཁྱད་པར་ལ་འཇུག་པ་ཡོངས་སུ་ཤེས་པ་མེད་པའི་ཕྱིར།

[Block 2518 [VERSE]]
རྒྱལ་དཔོག་པའམ༌[^1720]གཞན་འདིས་ནི། །
བདག་ཉིད་འདོད་ཆགས་སོགས་ལྡན་པའམ། །
གཞན་ལས་རིག་བྱེད་དོན་རིག་མིན། །
རིག་བྱེད་རིག་པར་བྱེད་མིན་ནའང་། །
རིག་བྱེད་དོན་ནི་གང་ལས་རྟོགས། །

[Block 2519]
ཉེས་པའི་འཁྲུལ་པ་ལས་མ་འདས་པ་ཅན་གྱི་འཆད་པ་པོའི་སྐྱེས་བུ་ཐམས་ཅད་ཀྱི་དབང་པོ་ལས་འདས་པའི་དོན་གྱི་ཁྱད་པར་སོ་སོར་ངེས་པ་དེ་བདག་ཉིད་ཀྱིས་རིག་པ་མ་ཡིན་ནོ། །

[Block 2520]
དེ་དག་ལ་གཞན་གྱིས་རིག་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ལ་ཡང་ཐལ་བར་གྱུར་པ༌[^1721]མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2521]
ལོང་བས་དྲངས་པར་གྱུར་པའི་ལོང་བས་ལམ་རྟོགས་པར་མི་འགྱུར་བ་ལྟ་བུའོ། །

[Block 2522]
རིག་བྱེད་བདག་ཉིད་ཀྱང་རང་གི་དོན་རྣམ་པར་འགྲེལ་པར་བྱེད་པ་མ་ཡིན་ཏེ། བསྟན་པ་དོན་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2523]
དེ་བས་ན་ཡོངས་སུ་ཤེས་པའི༌[^1722]བྱེད་པའི་དོན་ཅན་མ་ཡིན་པའི་སྒྲའི་ལྷག་མ་འདི་ལྟར་ཟུག་རྔུར་གྱུར་པ། ཡང་དག་པ་མཐོང་བ་མ་ཡིན་པའི་རྩ་བ་རྣམས་ཀྱིས༌[^1723]རྣམ་པར་བཅིངས་པ་འབྱུང་བར་དཀའ་བ་སྡུག་བསྔལ་འཇོག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2524 [VERSE]]
དེས་མཐོ་རིས་འདོད་མེ༌[^1724]ལ་ནི། །
སྦྱིན་སྲེག༌[^1725]སྦྱིན་ཞེས་ཐོས་པ་ལ། །
ཁྱི་ཤ་ཟ་ཞེས་བྱ་བ་དེ། །
དོན་མིན་ཞེས་འདིར་ཚད་མ་གང་། །

[Block 2525]
དོན་ལ་ལ་ཡང་ཉེ་བ་དང་། །བསྐལ་པ་དང་བྲལ་བ་མཐོ་རིས་འདོད་པས་མེ་ལ་སྦྱིན་སྲེག་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་དག་ལ་འབྱུང་བའི་ཁྱད་པར་ལ་ཇི་ལྟར་མངོན་པར་འདོད་པའི་མར་ལ་སོགས་པ་བླུགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཡིན་ལ། ཁྱིའི་ཤ་བཟའ་བར་བྱའོ་ཞེས་བྱ༌[^1726]བའི་ཁྱད་པར་མ་མཐོང་ངོ་། །ལྐོག་ཏུ་གྱུར་པའི་སྟོན་པ་པོའི་ཚིག་གི་བསམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་དོན་ད་ལྟར་བདག་གིས་རྟོགས་པར་འགྱུར་བའམ། འོན་ཏེ་བཟློག་པ་ཞེས་བྱ་བ་འདི་ཐམས་ཅད་དུ་ཐལ་བར་འགྱུར་བ་མཚུངས་པ་མ་ཡིན་ནམ། མ་ཡིན་ཏེ། འཆད་པ་པོ་བདག་ཉིད་ཀྱི་དགོངས་པ་གསལ་བར་བྱེད་པས་ཡང་དག་པའི་མན་ངག་སྲིད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
