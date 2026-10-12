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
[Block 2451]
དེ་ལྟར་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 2452]
[^1585]བདག་གི༌[^1586]དོན་དང་གཞན་གྱི་དོན་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2453]
རིན་པོ་ཆེ་བསྟན་པར་བྱ་བའི་ཕྱིར། །ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྒྱུ་དང་མི་རྒྱུ་རྣམས་ཀྱི་རྟེན་ས་གཞི་བཞིན་དུ་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་གཞི༌[^1587]ནི་ཚུལ་ཁྲིམས་དེ་དང་ལྡན་པའོ། །

[Block 2454]
དག་པ་ནི་གཡོ་སྒྱུ༌[^1588]མེད་པའོ། །

[Block 2455]
མཁས་པ་སྒྲིན༌[^1589]ཞེས་བྱ་བ༌[^1590]ནི་དགེ་བའི་ལས་རྣམས་ལ་བརྩོན་ཞིང་ཡོངས་སུ་ཤེས་པའོ། །ཤེས་རབ་ལྡན་ཞིང་ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ཡོད་པའོ། །

[Block 2456]
རྒྱུད་གཅིག་པ་ནི་ལན་གཅིག༌[^1591]གཞན་གྱིས་བརྗོད་པའི་གཞལ་བྱ་ཐོས་ནས་ཇི་སྲིད་འཚོ་བའི་བར་དུ་འཛིན་ཅིང་དྲན་པའོ། །

[Block 2457]
ཐོས་ནས་ལེགས་པར་སྟོན་པ་ནི། །ཞེས་པ་ལ། ཇི་ལྟར་སློབ་དཔོན་གྱི་ཞལ་ནས་ཐོས་པ་དེ་བཞིན་དུ། བཤད་པའི་རྒྱུད་ལ་སོགས་པ་དང་བཅས་པ་མ་ནོར་བར་སྟོན་པ་དེ་ནི་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་སྟེ་རེ་བ་ཐམས་ཅད་རྫོགས་པར་བྱེད་པ་དང་རིན་ཐང་མེད་པའི་ཕྱིར་རོ། །

[Block 2458]
ཡང་ན༌[^1592]སྔོན་དུ་བཤད་པའི་ཡོན་ཏན་གྱི་ཚོགས་རིན་ཆེ་བའོ།[^1593] །

[Block 2459]
དེ་དང་ལྡན་པའི་ཕྱིར་རིན་པོ་ཆེའོ། །

[Block 2460]
གང་ཟག་དེ་རྣམས་རྣམ་པ་གཉིས་སུ་བསྟན་པར་བྱ་བའི༌[^1594]ཕྱིར་ཨུཏྤ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 2461]
གང་ཟག་བཞི་པ༌[^1595]འདི་དག་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། །བསྐྱེད་པའི་རིམ་པ་གཙོར་གྱུར་པའི་ཚོགས་ཀྱི་བཤད་པའི་སྣོད་དུ་རུང་བ་ཡིན་གྱིས་གཞན་གྱི་ནི་མ་ཡིན་ཞེས་ཚིག་གི་ལྷག་མའོ། །

[Block 2462]
དེ་ལྟ་ན་ཙནྡན་ཞེས་བྱ་བ་བེམས་པའི༌[^1596]རིགས་ཅན་དེ་ཅིའི་ཕྱིར་བཤད་པའི་སྣོད་དུ་རུང་བར་འགྱུར་ཞེ་ན། སྨྲས་པ། རྣམ་པ་ཀུན་ཏུ་ཉན་འདོད་པ། །ཞེས་སྔོན་དུ་བཤད་དེ་ཉན་པ་ལ་འཇུག་པ་ནི་བཏང་སྙོམས་ཀྱི་གནས་མ་ཡིན་པ་དང་། རྗེས་སུ་གཟུང་བར་བྱ་བ་ཡིན་པས་སོ། །

[Block 2463]
གང་གི་ཕྱིར་གསང་བ་འདུས་པ་འདི་ལ་ནི། རིགས་ངན་དང་། སྨྱུག་མ༌[^1597]མཁན་ལ་སོགས་པ་ཡང་སྣོད་དུ་རུང་བར་འགྱུར་ན། ཆོས་ཐོས་པ་ལ་སོགས་པའི་རིམ་གྱིས་འཇུག་པ་ནི་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེའི་ལྟ་བ་ལོག་པ་ཙམ་རིམ་གྱིས་བསལ༌[^1598]བར་ནུས་ཀྱི་དེ་ཉིད་ཀྱི་ཕྱིར་རྫོགས་པའི་རིམ་པའི་སྣོད་མ་ཡིན་ནོ། །

[Block 2464]
གང་གི་ཚེ་སྐས་ཀྱི་རིམ་པའི་རིགས་པས་བསྐྱེད་པའི་རིམ་པ་མཐར་ཕྱིན༌[^1599]ན་དེའི་ཚེ་ཙནྡན་ལྟ་བུ་ཡང་རྫོགས་པའི་རིམ་པའི༌[^1600]སྣོད་དུ་འགྱུར་རོ། །

[Block 2465]
དེས་ན་རྣམ་པ་ཐམས་ཅད་དུ་དེ་ལ་བཏང་སྙོམས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2466]
རྫོགས་པའི་རིམ་པའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འདི་སློབ་མ་ལ་བཤད་པའི་སྣོད་དུ་རུང་བ་གཅིག་པུ་ཁོ་ན་ཞེས་དམ་བཅའ་བའོ།[^1601] །

[Block 2467]
རྟག་ཏུ་སྤྱོད་པས་རྣམ་བརྒྱན་པ་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ཡོན་ཏན་རྣམས་ཀྱིས་བརྒྱན་པ་ཞེས་ཁྱད་པར་གྱི་སྒོ་ནས་གཏན་ཚིགས་སོ། །

[Block 2468]
ད་ནི་སློབ་མ་བརྟགས༌[^1602]པས་བཤད་པའི་དབྱེ་བ་བསྟན་པར་བྱ་བའི་ཕྱིར། གང་ཟག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། གང་ཟག་གང་ཡིན་པ་དང་ཇི་ལྟ་བུའི་ཤེས་པ་དང་ལྡན་པ་ཞེས་ཡོངས་སུ་བརྟགས་ཏེ་སྣོད་དང་སྣོད་མིན་ཞེས་པ་ལ༌[^1603]ཡོན་ཏན་ཅན་དང་ཡོན་ཏན་ཅན་མ་ཡིན་པ་ཤེས་ནས། རྡོ་རྗེ་སློབ་དཔོན་མཁས་པ་ནི། །ཞེས་པ་ལ། དེ་རྣམས་ཀྱི་བསམ་པ་དང་བག་ཆགས་ལ་སོགས་པའི་དབྱེ་བ་ཤེས་པས་སོ། །

[Block 2469]
བཤད་པ་རྣམ་པ་གཉིས་བྱའོ། །ཞེས་པ་ནི༌[^1604]སྔར་བཤད་པའི་བཤད་པ་བྱ་བ་ཡིན་ཏེ། གཞན་དུ་ན་ཐམས་ཅད་དཀྲུགས་པར་འགྱུར་རོ། །

[Block 2470 [HEADING]]
##### བསྡུ་བའི་རྒྱན། ^1-7-3-3-0

[Block 2471]
བསྟན་བཅོས་ཐམས་ཅད་ཁྱབ་པར༌[^1605]བྱེད་པ་བསྡུ་བའི་རྒྱན་བསྟན་པར་བྱ་བའི་ཕྱིར། རྒྱན་ནི་དྲུག་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། གླེང་གཞི་ལ་སོགས་པ་དྲུག་གིས་རྒྱུད་ཀྱི་ལུས་ངེས་པར་བྱས་པས་སོ། །

[Block 2472 [HEADING]]
##### བདེན་གཉིས་རྣམ་པར་ངེས་བྱས་པ། ^1-7-3-4-0

[Block 2473]
བདེན་གཉིས་རྣམ་པར་ངེས་བྱས་པ། །ཞེས་པ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པ་དབྱེར་མེད་པའི་ཏིང་ངེ་འཛིན་སོ་སོར་བསྟན་པའོ། །

[Block 2474]
དེ་ནི་རྒྱན་འགྱུར་བདུན་པ་སྟེ། །ཞེས་པ་ལ། དེ་ལས་གཞན་པའི་རྒྱན་མི་དགོས༌[^1606]ཏེ་བསླབ་པར་བྱ་བ་མེད་པས་སོ། །

[Block 2475]
རྫོགས་པའི་རིམ་པ་སྒྲུབ་པའོ། །ཞེས་པ་ནི་རྡོ་རྗེའི་སྐུ་རྣམ་གྲངས་ཅན་ཆོས་ཀྱི་དབྱིངས་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཇི་ལྟར་གྱུར་པའི་ཚུལ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་བརྗོད་པ་སྟེ་འབྲས་བུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2476]
དེ་ལྟ་ན་ཟུང་དུ་འཇུག་པ་རབ་ཏུ་བསྟན་པ་ནི་མཐར་ཐུག་པའི་རྣམ་པ་གཉིས་པ་འདི་ཡིན་ན། དེ་ཅིའི་ཕྱིར་རྫོགས་པའི་རིམ་པ་སྒྲུབ་པར་བྱེད་པའི་རྒྱན་གཞན༌[^1607]བཤད་ཅེ་ན། དེ་ནི་བདེན་གྱི་རྒྱས་པར་བཤད་པ་དང་མངོན་དུ་བྱེད་པ་དག་གིས་བྱེ་བྲག་ཡོད་དོ། །

[Block 2477]
དགོངས་པ་ནི་མཐར་ཐུག་པས་ནི་ཟུང་དུ་འཇུག་པའི་རྒྱས་པར་བཤད་པ་དང་མཚན་ཉིད་སྟོན་ཏོ། །

[Block 2478]
དེ་བས་ན་ཟུང་དུ་འཇུག་པ་ལ་རྟོགས་པ་ཞེས་བཤད་ཀྱི་ཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2479]
འདིར་ནི་བསྟན་བཅོས་ཀྱི་དོན་མ་ལུས་པ་ཡོངས་སུ་བརྟགས༌[^1608]པས་གཉིས་སུ་མེད་པའི་ཏིང་ངེ་འཛིན༌[^1609]དུ་གྱུར་ཏེ། ཐོས་པ་དང་བསམ་པའི་ཤེས་རབ་དག་ལས་བསྒོམ་པའི་རང་བཞིན་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་པས་མངོན་དུ་བྱེད་པའི་དབང་གིས་རྒྱན་འདི་ཐ་དད་པ་ཁོ་ནའོ། །

[Block 2480]
ད་ནི་གཞུང་གི་ཚད་མ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས༌[^1610]ནས་ཞེས་སྨོས་ཏེ། རྡོ་རྗེ་ཕྲེང་བ་ལ་སོགས་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས་པས་སོ། །

[Block 2481]
སྨྲས་བཤད་ཤིན་ཏུ་རྙེད་པར་དཀའ། །ཞེས་པ་ནི་སྨྲས་པ་དེ་ཉིད་བཤད་པ་ནི་བསྟན་བཅོས་ཀྱི༌[^1611]དོན་མ་ལུས་པ་ཡོངས་སུ་མ་བརྟགས་ན་རྙེད་པར་དཀའ་བའོ། །

[Block 2482]
དེས་ནི་སྒྲ་ཇི་བཞིན་པ་ལ་བརྟེན་ཏེ་བཤད་པ་པོ་གཞན་རྣམས་ལ༌[^1612]སུན་འབྱིན་པའོ། །

[Block 2483]
དེའི་ཕྱིར།

[Block 2484 [VERSE]]
རྣལ་འབྱོར་རྒྱུད་རྣམས་འདི་ཉིད་ཀྱིས། །
དྲངས་ཏེ་བཤད་པ་གཞན་གྱིས་མིན། །

[Block 2485]
ཞེས་པ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོ་ནི་བཤད་པ་འདི་ཉིད་ཀྱིས་བཤད་པར་རིགས་སོ། །

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
--- END BLOCKS ---
