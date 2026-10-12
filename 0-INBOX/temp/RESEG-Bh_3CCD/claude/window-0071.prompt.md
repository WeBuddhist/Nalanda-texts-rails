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
[Block 2486]
གཞན་དུ་མིན༌[^1613]སྒྲ་ཇི་བཞིན་པ་ཙམ་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2487]
ཉེ་བར་སྡུད༌[^1614]པའི་ཕྱིར། དེ་བས༌[^1615]ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྡོ་རྗེ་སློབ་དཔོན་ནི་ཡང་དག་པའི་དབང་བསྐུར་བ་ལ་སོགས་པ་ཡོན་ཏན་གྱི་ཚོགས་དང་ལྡན་པ་ལས་སོ། །

[Block 2488]
བཤད་པའི་རྒྱུད་ལ་མཁས་པ་ལས་ནི་རྡོ་རྗེ་སློབ་དཔོན་གྱི་ཁྱད་པར་རོ། །

[Block 2489]
གླེང་གཞི་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 2490]
རིམ་པ་ནི་རྫོགས་པའི་རིམ་པ་སྟེ། དེ་དག་གི་སྦྱོར་བ་ནི་བཤད་པའི་འབྲེལ་པའོ། །

[Block 2491]
ཡིས་ནི་བྱེད་པའི་གསུམ་པའོ། །

[Block 2492]
དེའི་སྒོ་ནས་བཤད་པའི་རྒྱུད་ལ་མཁས་པའི་རྡོ་རྗེ་སློབ་དཔོན་གང་ཡིན་པ་དེ་ལས་སོ། །

[Block 2493]
འབད་དེ་ནི་ཐོས་པ་ལ་སོགས་པའི་རྩོལ་བས༌[^1616]སོ། །

[Block 2494]
རྣལ་འབྱོར་རྒྱུད་རྣམས་གཟུང་ཞེས་པའི༌[^1617]རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་རྣམས་མཉན་པར་བྱ་བའོ། །

[Block 2495]
དེ་ལྟ་ན་རིམ་པའི་སྒྲས་ནི་བསྐྱེད་པ་དང་རྫོགས་པ་གཉིས་ཀ་བརྗོད་ན། འདིར་རྫོགས་པ༌[^1618]གཅིག་པུ་ཇི་ལྟར་བརྗོད་ཅེ་ན། སྨྲས་པ་གླེང་གཞིའི་སྒྲ་གང་དུ་ཡོད་པས་དེའི་ཕྱིར་གླེང་གཞིའི་སྒྲས་ནི་བསྐྱེད་པའི་རིམ་པ་བརྗོད་དོ་ཞེས་དོན་གྱི་ཤུགས་ཀྱིས༌[^1619]རིམ་པའི་སྒྲས་རྫོགས་པའི་རིམ་པ་རྗོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2496]
གང་གི༌[^1620]ཕྱིར་སྤྱིའི་སྒྲ་རྣམས་ནི་རྒྱུད་རྣམ་པ་བཞིས་ཁྱད་པར་ཅན་དུ་འགྱུར་ཏེ། དོན་དང༌[^1621]རྟགས་དང་རབ་ཏུ་བྱེད་པ་དང་སྒྲ་གཞན་དང་འགྲོགས་པས་སོ། །

[Block 2497]
དེ་ལ་དོན་གྱིས་ནི་དཔེར་ན་བཟའ་བ་པོ་འདི་ཡིན་ནོ་ཞེས་འདིས་ཐམས་ཅད་བཟའ་བ་པོ་ཡིན་པས་བཟའ་བ་པོའི༌[^1622]སྒྲས་དོན་གྱི་ཤུགས་ལས་ཁྱད་པར་སྟོན་ཏེ། དེས་ན་མང་པོ་ཟ་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 2498]
རབ་ཏུ་བྱེད་པས་ནི་དཔེར་ན་སེན་ད་བ་ཁྱེར་ལ་ཤོག་ཅེས༌[^1623]པས་ཚང་བང་ན་གནས་པའི་མིས་ཚྭ་འོང་ངོ་། །གཡུལ་ངོར་གནས་པའི་མིས་སྨྲས་ན་རྟ་འདོད་པ་ཡིན་ནོ། །

[Block 2499]
རྟགས་ཀྱིས་ནི་གོ༌[^1624]ཞེས་འདིས་རྟགས་གཉིས་ཀ་ཅན་ཡིན་ཡང་བུད་མེད་ཀྱི་རྟགས་ཀྱི༌[^1625]རྐྱེན་དང་གཞི་མཐུན་པས་བུད་མེད་ཀྱི་དོན་ལ་འཇུག་གོ། །

[Block 2500]
དཔེར་ན་གོ་ཨི༌[^1626]ཡཾ་ཞེས་པས་མོ་བསྟན་ཏོ། །

[Block 2501]
གོ༌[^1627]ཨ་ཡི་ཞེས་པས་ཕོ་བསྟན་ཏོ། །

[Block 2502]
སྒྲ་གཞན་དང་འགྲོགས་པ་ནི་པ་ཡང་འོངས་པ་དང་གླང་རྣམས་ཀྱང་འོངས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2503]
དེ་བཞིན་དུ་འདིར་ཡང་ཤེས་པར་བྱའོ། །

[Block 2504]
རྒྱན་རྣམ་པ་བདུན་བཤད་པའི་རིགས་པའོ་ཞེས་པ་འདིས་རྒྱན་གྱི་བཤད་པ་རྫོགས་ཞེས་བསྟན་པའོ། །

[Block 2505]
[^1628]

[Block 2506 [HEADING]]
### རྒྱུད་ཀྱི་དོན། ^1-8-0

[Block 2507]
ད་ནི་ལེའུ་བཅུ་བདུན་གྱིས༌[^1629]བསྡུས་པའི་དོན་བཤད་པར་བྱ་ཞེས་བྱ་བ་ལ། དེའི་དགོངས་པ་ནི་རྒྱུད་ཀྱི་དོན་ནི་རྣམ་པ་གསུམ་སྟེ། ཚིག་གི་དོན་དང་། ངག་གི་དོན་དང་། བསྡུས་པའི་དོན་ནོ། །

[Block 2508]
དེ་ལ་ཚིག་གི་དོན་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བཤད་པའོ། །

[Block 2509]
ངག་གི་དོན་ནི་ལེའུ་སོ་སོ་ངག་ཏུ་ཡོད་པའི་ངག་རྣམས་ཀྱིས༌[^1630]བརྗོད་པར་བྱ་བ་སོ་སོར་བསྟན་པའོ། །

[Block 2510]
བསྡུས་པའི་དོན་ནི་ལེའུ་དེ་རྣམས་ཀྱིས་བརྗོད་པར་བྱ་བ་ནི་འདི་ཡིན་ཏེ་ཞེས་བརྟག་པ་ན་བསྡུས་ཏེ་དོན་སོ་སོར་བསྟན་པའོ། །

[Block 2511 [HEADING]]
#### བསྡུས་པའི་དོན། ^1-8-3-0

[Block 2512]
དེ་ལ་བསྡུས་པའི་དོན་ངེས་པ་ལས་ཚིག་གི་དོན་དང་ངག་གི་དོན་དག་ནི་བདེ་བར་རྟོགས་པས་དང་པོ་བསྡུས་པའི་དོན་སྨྲ་བར་བྱ་བའི་ཕྱིར། དེ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1631]སྨོས་སོ། །

[Block 2513]
རྗོད་པ་དང་བརྗོད་པར་བྱ་བའི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོའི༌[^1632]ཞེས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། རྗོད་པ་ནི་རྒྱུད་ཀྱི་ཚིག་རྣམས་སོ། །

[Block 2514]
བརྗོད་པར་བྱ་བ་ནི་རིམ་པ་གཉིས་སོ། །

[Block 2515]
དེ་དག་གི་བདག་ཉིད་ནི་ངོ་བོ་གང་ལ་ཡོད་པ༌[^1633]རྗོད་པ་དང་། བརྗོད་པར་བྱ་བའི་བདག་ཉིད་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟེ། དཔལ་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བསྟན་ཏོ། །

[Block 2516]
གང་གི་ཕྱིར་རྒྱུད་ཀྱི་ཚིག་རྣམས་དང་དེ་ལས་ཉེ་བར་དམིགས་པའི་དོན་གྱི་ཁྱད་པར་བསྒོམས་པ་རྣམས་ཀྱིས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 2517]
སྒྲ་དང་དོན་གྱི་ངོ་བོ་རྡོ་རྗེ་སེམས་དཔའ་ཁོ་ནའོ། །

[Block 2518]
གང་གི་ཕྱིར་ལྟེ་བ་ན་གནས་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོ་འོད་གསལ་བ་ལས།

[Block 2519]
སྲོག་གི་རླུང་ལངས་ཏེ་གནས་བརྒྱད་དང་ཕྲད་པས་ཡི་གེ་རྣམས་འབྱུང་བར་འགྱུར་ཏེ་དེ་དག་གི༌[^1634]ཚིག་རྣམས་སོ། །

[Block 2520]
དེ་དག་གིས་ཀྱང་ངག་བསྐྱེད་ཅིང་དེ་ལས་ཀྱང་རྒྱུད་དང་རབ་ཏུ་བྱེད་པ་ལ་སོགས་པ་སྒྲའི་ཚོགས་ཐམས་ཅད་རྒྱུ་དང་རྗེས་སུ་མཐུན་པ་ཉིད་ཡིན་ནོ། །

[Block 2521]
རྒྱུ་དེ་ཡང་འོད་གསལ་བའི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་དོ། །

[Block 2522]
ཡང་ན་བརྗོད་པ་ནི་རྒྱུད་ཀྱི་མིང་སྟེ་གསང་བ་འདུས་པ་ཞེས་བྱའོ། །

[Block 2523]
དེས་ནི་སྐུ་གསུང་ཐུགས་ཀྱི་ངོ་བོ་ཉིད་སངས་རྒྱས་ཐམས་ཅད་འདུས་པའི་བདག་ཉིད་དེ་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 2524]
བརྗོད་པར་བྱ་བ་ནི་རིམ་པ་གཉིས་ཏེ། དེ་ལས་བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ་གྱི་ངོ་བོ་རྡོ་རྗེ་འཛིན་པའོ། །

[Block 2525]
རྫོགས་པའི་རིམ་པ་ཡང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པའི་མཚན་ཉིད་དོ། །
--- END BLOCKS ---
