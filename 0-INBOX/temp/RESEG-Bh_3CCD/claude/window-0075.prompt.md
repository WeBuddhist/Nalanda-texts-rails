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
[Block 2626]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པ་ཞེས་པའི༌[^1712]བར་དུ་ནི་བསྟོད་པ་ཙམ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2627]
དཀྱིལ་འཁོར་ལ་སོགས་པ་ཞེས་པའི་སྒྲས་ཤེས་པར་བྱའོ་ཞེས་དགོངས་སོ། །

[Block 2628]
དེ་བཞིན་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་ཞེས་པའི་བར་དུ་ནི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 2629]
དེ་ལྟར༌[^1713]ན་དཀྱིལ་འཁོར་ལ་སོགས་ཞེས་བྱ་བ་འདིས་སྒྲ་ཇི་བཞིན་པར་ཇི་ལྟར་མི་འགྱུར་ཞེ་ན། སྨྲས་པ། [^1714]དཀྱིལ་འཁོར་གྱི་ཚད་ཙམ་དང་དགོད་པ་དེ༌[^1715]དག་ཏུ་སྒྲ་ཇི་བཞིན་པའོ། །

[Block 2630]
འདིར་ནི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན༌[^1716]ཉིད་ཀྱི་སྐབས་ཡིན་པས་དགོངས་པ་མ་ཡིན་པའོ། །

[Block 2631]
དེ་ནས་སྟོན་པ་ཞེས་པ་ནས། སྒྲ་ཇི་བཞིན་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་ཙམ་བརྗོད་བྱ་ཡིན་པས་སོ། །

[Block 2632]
དེ་ནས་ཐུགས་ཞེས་པ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་མཚན་མའི་ཕྱག་རྒྱ་དང་བཅས་པའི་དཀྱིལ་འཁོར་དང་དེ༌[^1717]ཁོ་ན་ཉིད་ཀྱང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2633]
ལེའུ་བཞི་པའི་ཞེས་པ་འདིས་ཉེ་བར་སྡུད༌[^1718]པའོ། །

[Block 2634]
དེ་ནས་ཞེས་བྱ་བ་ནས་སྒྲ་ཇི་བཞིན་ཞེས་བྱ་བའི་བར་དུ་ནི་སྤྱོད་པའི་མཚན་ཉིད་བསྟན་ཏོ།[^1719] །

[Block 2635]
སྤྱོད་པ་ཇི་ལྟ་ཇི་ལྟར་གསུངས། །ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 2636]
རྣམ་པར༌[^1720]མི་རྟོག་པ་ཞེས་བྱ་བ་ནས་དགོངས་པ་མ་ཡིན་པ་ཞེས་བྱ་བའི་བར་དུ་དེ་ཁོ་ན་ཉིད་གསལ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2637]
རིགས་ངན་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པའི་ཞེས་པའི༌[^1721]བར་དུ་ནི་དངོས་གྲུབ་ཀྱི་ཆོ་ག་དགག་པ་སྒྲ་ཇི་བཞིན་པ་ཉིད་དེ། སོགས་པའི་སྒྲ་སྦྱོར་བས་སོ། །

[Block 2638]
སྲོག་གཅོད༌[^1722]པ་ནས་དགོངས་པས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་འཇིག་རྟེན་དང་འགལ་བའི་སྒྲའི་སྒོ་ནས་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2639]
མ་དང་ཞེས་པ་ནས་དྲང་བའི་དོན་དང་ངེས་པའི་དོན་གྱི་ཞེས་བྱ་བའི་བར་དུ་ནི་ལེགས་པར་བསླབས་པའི༌[^1723]དམ་ཚིག་གི་ཕྱག་རྒྱ་དང་ཆོས་དང་ལོངས་སྤྱོད་དང་སྤྲུལ་པའི་སྐུ་བརྗོད་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2640]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་བཞིན་ཞེས་བྱ་བའི་བར་དུ་ནི། སྤྱོད་པ་ཇི་ལྟ་ཇི་ལྟར་གསུངས། །ཞེས་བྱ་བས་དེ་མཚོན་པའི་ཕྱིར་རོ། །

[Block 2641]
དེ་ནས་ཞེས་པ་ནས་དྲང་བ༌[^1724]དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་རྒྱལ་བ་དང་འོད་གསལ་བ་ལ་འཇུག་པས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2642]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལན་བཏབ་པ་དང་འོད་ཟེར་སྤྲོ་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2643]
དེ་ཡང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 2644]
དེ་ནས་ཞེས་པ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་གྱི་བར་དུ་ནི་རང་གི་གདན་ལ་གནས་པ་དང་འོད་གསལ་བ་དང་བདག་ལ་བྱིན་གྱི༌[^1725]རློབ་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2645]
དེ་ནས་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པའི་ཞེས་བྱ་བའི་བར་དུ་ནི་སྤྱོད་པའི་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2646]
ལེའུ་ལྔ་པ་ཞེས་བྱ་བ་འདིས་ཉེ་བར་བསྡུས་པ༌[^1726]བསྟན་ཏོ། །

[Block 2647]
[^1727]དེ་ནས་ཞེས་པ་ནས། དྲང་བའི་དོན་དང༌[^1728]ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་བཀོད་པ་ལ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་འཇུག་པས༌[^1729]སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་བྱིན་གྱིས་རླབ་པ༌[^1730]བསྟན་པའི་ཕྱིར་རོ། །

[Block 2648]
རྫོགས་པའི་རིམ་པ་ལ་དེ་བཞིན་གཤེགས་པ་ལྔའི་བདག་ཉིད་སྐུ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་སྒྱུ་མའི་ལུས་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2649]
དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས། དགོངས་པས༌[^1731]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲ་བརྗོད་པའི་སྒོ་ནས་རིམ་པ་ལྔ་པོ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2650]
དེ་ནས་དཔལ་ཞེས་པ༌[^1732]ནས་ངེས་པའི་དོན་དང་དྲང་བའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་ལོ་བཅུ་དྲུག་པའི་རོལ་བྱེད་མ་དང་སྙོམས་པར་ཞུགས་པ་དང་ཕྱི་དང་ནང་གི་མཆོད་པ་དང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་ཉིད་ཤེས་རབ་དང་རྗེས་སུ་མཐུན་པའི་མཆོད་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2651]
ལེའུ་དྲུག་པ་ཞེས་བྱ་བ་འདིས་ཉེ་བར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 2652]
[^1733]

[Block 2653]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པ་ཞེས་པའི༌[^1734]བར་དུ་ནི་སྤྱོད་པའི་གནས་སྐབས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2654]
སློང་མོ་ཟ་ཞེས་པ་ནས། དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་དམན་པ་ཉིད་ཡོངས་སུ༌[^1735]དགག་པ་དང་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2655]
སངས་རྒྱས་ཞེས་བྱ་བ་ནས། རྣམ་པ་བཞི་ཡི་ཚུལ་གྱིས༌[^1736]བཤད། །ཅེས་བྱ་བའི་བར་དུ་ནི་དེ་ལ་སྤྱིའི་དོན་གྱི་ཕྱོགས་སུ་གཟུགས་ལ་སོགས་པ་རྣམས་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས༌[^1737]པའི་ངོ་བོ་ཉིད༌[^1738]ཡོངས་སུ་ཤེས་པ་ལ་ལོངས་སྤྱོད་པ་སྟེ། དེ་རྣམས་དེའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2656]
སྦས་པའི་ཕྱོགས་སུ་ནི་ཡེ་ཤེས་གསུམ་གྱི་རང་བཞིན་གྱི་གཟུགས་ལ་སོགས་པ་རྣམས་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 2657]
མཐར་ཐུག་པ་ལ་ཡང་འོད་གསལ་བའི་ངོ་བོ་ཉིད་དུ༌[^1739]གཟུགས་ལ་སོགས་པ་སྤྱད༌[^1740]པའོ། །

[Block 2658]
སངས་རྒྱས་རྗེས་དྲན་ཞེས་བྱ་བ་ནས་དགོངས་པས༌[^1741]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བ༌[^1742]བརྗོད་པའི་སྒོ་ནས་རྫོགས་པའི་རིམ་པའི་རྣམ་གྲངས་ཅན་རིམ་པ་ལྔ་པོ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2659]
བུད་མེད་ཅེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་ཕྱག་རྒྱའི་འབྲེལ་པ་དེ་ཁོ་ན་ཉིད་ཉེ་བར་མཚོན་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2660]
སངས་རྒྱས་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་འགལ་བའི་སྒྲའི་སྒོ་ནས་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་དེ་བཞིན་གཤེགས་པ་ལྔའི་སྐུ་སྒོམ་པ༌[^1743]དང་། ཚིམ་པར་བྱེད་པའི་ཆོ་ག་དང་དམ་ཚིག་དང་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱ་དག་ལས་གང་ཡང་རུང་བ་དང་སྙོམས་པར་ཞུགས་པའི་དོན་རབ་ཏུ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2661]
དེ་ལ་སྐུ་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པར་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་སྐུ་ལ་སོགས་པར་བྱིན་གྱིས་རློབ་པར་བྱས་ནས༌[^1744]དེའི་ང་རྒྱལ་ཙམ་དེའི་བརྗོད་པར་བྱ་བ་ཡིན་པས་སོ། །

[Block 2662]
དེ་ཡང་སོགས་པའི་སྒྲ་སྔ་མ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 2663]
དེ་ལ་ཞེས་བྱ་བ་ནས་དགོངས་པས་བཤད་པ༌[^1745]ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲའི་སྦྱོར་བས་སྒོ་ང་ལས་སྐྱེས་པ་ལ་སོགས་པའི་སེམས་ཅན་གྱི་ཁམས་རྣམ་པ་བཞིའི་ངོ་བོ་ཡོངས་སུ་ཤེས་པ་དང་། དམ་ཚིག་གི་དཀྱིལ་འཁོར་ཕྱུང་བ་དང༌[^1746]རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2664]
དེ་ལ་ཤེས་རབ་ཅེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་ཉིད་ཀྱི་འོད་གསལ་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2665]
དེ་ལ་མ་སྐྱེས་པ་ཞེས་པ་ནས༌[^1747]སྒྲ་ཇི་བཞིན་པར་བཤད་པར༌[^1748]བྱ་བའི་བར་དུ་ནི་སྤྱོད་པ་ཉིད་ཀྱི་ཕན་ཡོན་ཙམ་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
