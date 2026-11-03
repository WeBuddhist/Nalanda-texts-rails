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

[Block 2526]
འདི་ནི་སྟོན་པར་བྱེད་པ་པོ་མེད་པའི་སྒྲ་དག་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2527]
འཇིག་རྟེན་གྱིས་ཤེས་པར་བྱ་བའི་དགོངས་པ་ཅན་གྱིས་གསུངས་པ་ན། འཇིག་རྟེན་གྱི་བརྡ་རབ་ཏུ་གྲགས་པ་རྗེས་སུ་སྐྱོང་བར་མཛད་དོ། །

[Block 2528]
དེ་ལས་ཀྱང་དོན༌[^1727]དེའི་རྟོགས་པར་འགྱུར་རོ། །

[Block 2529]
སྐྱེས་བུས་མ་བྱས་པའི་སྒྲ་དག་ནི་མ་ཡིན་ཏེ། དེ་ལ་འགའ་ཞིག་སྨྲ་བར་འདོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2530]
གཞན་ཡང་མཁས་པ་རིགས་པ་ཉིད་རྗེས་སུ་སྐྱོང་བར༌[^1728]བྱེད་པ་དོར་བར་བྱ་བ་དང་། བླང་བར་བྱ་བ་དེའི་རྟེན་དག༌[^1729]ལ་འཇུག་པར་འགྱུར་གྱི། རབ་ཏུ་བརྗོད་པས་ནི་མ་ཡིན་པའི་ཕྱིར་ཐལ་བར་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 2531]
དེ་ཡང་སྐབས་ཇི་ལྟ་བ་བཞིན་དུ་སྟོན་པར་འགྱུར་རོ། །

[Block 2532]
[^1730]འཇིག་རྟེན་གྱི་གནས་པ་ལ་སོགས་པ་རིགས་པའི་ཡུལ་མ་ཡིན་པའི་དོན་ལ་ཡང་སྐྱེས་བུ་ཡིད་ཆེས་པའི་ཚིག་ལས་རྟོགས་པ་མ་ཡིན་ནམ། མ་ཡིན་ཏེ་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2533]
ལ་ལར་འཁྲུལ་པ་མེད་པའི་ཕྱིར་ཐམས་ཅད་ལ་དེ་ལྟར་འགྱུར་བ་མ་ཡིན་ཏེ། འཁྲུལ་བ་མཐོང་བའི་ཕྱིར་དང་། དེའི་འཇུག་པ་མི་སླུ་བ༌[^1731]དང་ཁྱབ་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2534]
ལུང་གི་མཚན་ཉིད་འདི་ནི་གོ་སྐབས་མེད་པ་ཉིད་དུ་འདོད་པས་དེ་ལས་ངེས་པ་མ་ཡིན་ནོ། །

[Block 2535]
དེ་བས་ན་ལུང་ཚད་མ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2536]
སྐྱེས་བུས་མ་བྱས་པའི་སྒྲ་དག་གི་དོན་ཤེས་པ་ཡང༌[^1732]དག་པའི་མན་ངག་ལས་མ་ཡིན། །རིགས་པ་ལས་མ་ཡིན། འཇིག་རྟེན་ལས་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2537]
དེ་ལ་རྟོགས་པ་མེད་པར་རིགས་པ་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 2538]
དེ་ཡང་གལ་ཏེ། འཇིག་རྟེན་ཚིག་རབ་གྲགས་རྟོགས་པའི། །རྒྱུ་ཡིན་ན།

[Block 2539 [VERSE]]
དེ་ལ་སྣ་ཚོགས་དོན་ཅན་སྒྲའི། །
གང་གིས་དོན་འདི་རྣམ་ཕྱེ་བས། །
དབང་པོ་ལས་འདས་དོན་མཐོང་གང་། །

[Block 2540]
སྐྱེས་བུས་མ་བྱས་པའི་སྒྲ་དང་དོན་འབྲེལ་པ་ལས་འཇིག་རྟེན་གྱི་ཐ་སྙད་འདི་ནི་མ་ཡིན་ནོ། །

[Block 2541]
འོ་ན་ཅི་ཞེ་ན། བརྡ་ལས་ཡིན་ཏེ། བསྟན་བཅོས་བྱེད་པ་རང་ཉིད་ཀྱི༌[^1733]བརྡ་ལས་བསྟན་པ་ལ་ལྟོས་པའི་ཕྱིར། པ་ནི་ནའི༌[^1734]སློབ་མ་ལ་སོགས་པའི་ཐ་སྙད་བཞིན་ནོ། །

[Block 2542]
སྐྱེས་བུས་མ་བྱས་པ་དེ་ལ་ནི་བསྟན་པ༌[^1735]རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་འགའ་ཞིག་གིས་ཀྱང་མི་ཤེས་པའི་ཕྱིར་དང་། དབང་པོ་ལས་འདས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2543]
དབང་པོས་གཟུང་བར་བྱ་བ་ཉིད་ཡིན་ན་ནི་གཟུགས་ལ་སོགས་པ་དང༌[^1736]འདྲ་བར་བདག་ཉིད་རྟོགས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2544]
བསྟན་པ་ཡིན་ན་ཡང་སྐྱེས་བུ་རང་རྒྱུད་པ་དག་གི་དེ་ཁོ་ན་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པས་མི་སླུ་བ་མི་འགྲུབ་པའི་ཕྱིར་ཡིད་བརྟན་དུ་མེད་དོ། །

[Block 2545]
གལ་ཏེ་རིག་བྱེད་དང་འདྲ་བར་རྣམ་པར་བཤད་པ་དང་། སྐྱེས་བུས་མ་བྱས་པ་ཐོག་མ་མེད་པའི་ཡང་དག་པའི་མན་ངག་རྒྱུན་མ་ཆད་པ་ལས་འོངས་པ་དེ་ལས་དོན་གྲུབ་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་སྒྲའི་བདག་ཉིད་ཅན་ཡིན་ན་ནི་ཇི་ལྟར་ན་འདིའི་དོན་རིག་པ་ཡིན་ཞེས་བརྒལ་ཞིང་བརྟག་པ་མཚུངས་སོ།[^1737] །རེ་ཞིག་སྐྱེས་བུ་བདག་ཉིད་ཀྱིས་བརྡར་བྱས་པའི་སྒྲ་རྣམས་ཀྱི་དོན་རྭ་ལས་གཟུང་བས་ཀྱང་མི་རྟོགས་པ་རྟོགས་པར་བྱེད་པ་དེ་ལྟར་ན་སྐྱེས་བུས་བྱས་པའི་དོན་རྟོགས་པའི་ཐབས་ཡོད་པ་ཡིན་ནོ། །

[Block 2546]
སྐྱེས་བུས་མ་བྱས་པའི་སྒྲ་ནི་དེ་ལྟར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2547]
འགའ་ཞིག་གིས་ཀྱང་ལ་ལར་འདིའི་འབྲེལ་པ་ངེས་པ་ཤེས་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 2548]
དེའི་དོན་རྟོགས་པ་ཉིད་མེད་དོ།[^1738] །གཞན་ཡང་རིག་བྱེད་དེའམ་དེའི་རྣམ་པ༌[^1739]བཤད་པ་སྐྱེས་བུས་སྐྱེས་བུ་ལ་བསྟན་པར་གྱུར་པ་ན། ཡང་དག་པའི་མན་ངག་འཇིག་པ་མེད་པ་ཅན་ཉིད་རྗེས་སུ་འཇུག་པ་ཞེས་བྱ་བ་འདི་ལ་ཡང་མནའ་ལ༌[^1740]བརྟེན་པར་བྱ་སྟེ། ལུང་འཇིག་པར་བྱེད་པར་བདག་ཉིད་རློམ༌[^1741]པས་སམ། དེའི་བསྟན་པ་ལ༌[^1742]རྣམ་པར་སྡང་བས་སམ། དེར་ཞུགས་པ་དམའ་དབབ་པའི་ཕྱིར་གཡོན་ཅན་ཟིལ་གྱིས་མནན་པས་སམ། རྒྱུ་གཞན་འགའ་ཞིག་ཀྱང་རྣམ་པ་གཞན་དུ་རྩོམ་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2549]
གཞན་ཡང་འདིར་ཁྱོད་ཀྱིས་སྐྱེས་བུ་འདོད་ཆགས་ལ་སོགས་པ་དག་གིས་བསླད་པ་བརྫུན་པ་ཡང་སྨྲ་བའི་ཕྱིར། འདིའི་ཚིག་ཚད་མ་མ་ཡིན་ནོ་ཞེས་བདག་ཉིད་ཀྱིས་ཁས་བླངས་པ་བརྗོད་པ་ཡིན་ཏེ། རང་གི་ཚིག་ལ་རྗེས་སུ་ཆགས་པའི་ཕྱིར་རོ། །

[Block 2550]
དེ་ནི་འདིར་ཡང་ཡོད་དམ་མེད་ཅེས་ཅིའི་ཕྱིར་དཔྱོད་པར་མི་བྱེད། དེ་ཉིད་རིག་བྱེད་དམ་རིག་བྱེད་ཀྱི་དོན་སྟོན་པ་ན་འཁྲུལ་པའི་ཕྱིར་རྣམ་པ་གཞན་དུ་སྟོན་པར་འགྱུར་རོ། །

[Block 2551]
སྐྱེས་བུ་འགའ་ཞིག་གིས་ནུས་པ་ལས་བྱུང་བའི་ཡལ་ག་གཞན་དག་ཐོས་ཤིང་ད་ལྟར༌[^1743]ཡང་ཉུང་ཟད་འདོན་པར༌[^1744]བྱེད་པ་ཅན་འགའ་ཞིག་ཀྱང་མཐོང་ངོ་། །དེ་བཞིན་དུ་རྒྱ་ཆེར་འདོན་པར་བྱེད་པ་ཅན་འགའ་ཞིག་ཀྱང་དུས་འགའ་ཞིག་གི་ཚེ། ནུས་པ་སྲིད་པའི་ཕྱིར་དང་། ཡང་སྐྱེས་བུ་ཡིད་ཆེས་པའི་ཤེས་པས་རབ་ཏུ་མང་པོ་ཁས་བླངས་པ་ཡོད་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2552]
ཡང་རྒྱ་ཆེར་འདོན་པར༌[^1745]བྱེད་པ་པོའི་སྐྱེས༌[^1746]བུ་འགའ་ཞིག་གི་ཚེ༌[^1747]འདོན་པ་བརྗེད་པ། འདོན་པར་བྱེད་པ་ཅན༌[^1748]དེ་དག་དང་། གཞན་སྲིད་པ༌[^1749]ཉམས་པའི་འཇིག་པ་ལ་སོགས་པས་རྣམ་པ་གཞན་དུ༌[^1750]སྲིད་པའི་ཕྱིར་རོ། །

[Block 2553]
དེ་ཤེས་པ་ལས་ཀྱང་དེ་ལ་དད་པ་དག་དཔྱོད་པ་མེད་པར་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2554]
འདོན་པར་བྱེད་པ་པོ་མང་པོ་དག་ལ་སྐྱེས་བུ་ཡིད་ཆེས་པ་ལས་མང་དུ་རྟོགས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2555]
དེ་ལས་ཀྱང་རྣམ་པ་འགའ་ཞིག་གིས་འཁྲུལ་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2556]
གཞན་ཡང་སྐྱེས་བུ་འཆད་པ་པོའི་ཉུང་ཟད་འཆད་པའི་བརྒྱུད་པ་ཉིད་འདི་ལ་ཁྱེད་ཀྱིས་ཀྱང་མཉན་པར་བྱ་བ་ཡིན་ནོ།[^1751] །དེ་ལ་རྣམ་པར་སྡང་བ་དང་། མི་ཤེས་པ་དང་། སྤྱང་པོ་དག་གི་ནང་ནས་འགའ་ཞིག་གང་ལས་རུང་བར་འགྱུར་བའི་ཕྱིར་ཡིད་བརྟན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2557]
དེ་བས་ན་སྐྱེས་བུས་མ་བྱས་པའི་བཤད་པ་ལས་མ་ཡིན་ཞིང་། བརྡ་ལས་བྱུང་བའི་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལས༌[^1752]ཀྱང་རིག་བྱེད་ཀྱི་དོན་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2558]
བརྡ་ལས་བྱུང་བ་མ་ཡིན་པ་ལ་ཡང་དོན་སྣ་ཚོགས་པ་ཅན་གྱི་སྒྲ་རྣམས་ཀྱི་ཐ་སྙད་མཐོང་བའི་ཕྱིར་མ་གྲུབ་པའི་དོན་ཅན་ནམ། རབ་ཏུ་མ་གྲགས་པའི་འགའ་ཞིག་གི་ཡང་བཤད་པ་མཐོང་བས་ཐམས་ཅད་དུ་དེའི་དོགས་པ་མི་ལྡོག་པའི་ཕྱིར་རོ། །

[Block 2559]
ཐམས་ཅད་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ངེས་པར་སྦྱར་བ་ན་ཡང་རྗེས་སུ་མཐུན་པར་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པ་བསྐྱེད་པའི་ཕྱིར་དང་། འདོད་པ་དང༌[^1753]མི་འདོད་པ་དག་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2560]
དོན་ཐམས་ཅད་ལ་ཁྱད་པར་མེད་པ་དག་ནི་ལྐོག་ཏུ་གྱུར་པ་དང་འབྲེལ་པ་ཅན་གྱི་དོན་གཅིག་ལྐོག་ཏུ་གྱུར་པ་མཐོང་བ་མ་ཡིན་པའི་སྐྱེས་བུ་ཐ་མལ་པ༌[^1754]ལ་སུ་ཞིག་རྣམ་པར་འབྱེད་པར་འགྱུར་ཞིང་། གང་ཞིག་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལས་རྟོགས་པར་འགྱུར། གཞན་ཡང་བདག་ཉིད་ཀྱང་ཐམས་ཅད་དུ་གྲགས་པའི་རྗེས་སུ་འབྲང་བར་མི་བྱེད་དོ། །
--- END BLOCKS ---
