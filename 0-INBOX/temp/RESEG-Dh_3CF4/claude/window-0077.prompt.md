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
[Block 2696]
རྩོལ་མི་ཕོད་དམ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་རྩོལ་བ་དང་བྲལ་བ་སྟེ། སྙིང་སྟོབས་མེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2697]
ང་རྒུད་པ་ཞེས་བྱ་བ་དེ་ལ་མི་བཟོད་པར་གྱུར་པ་དེ་ནི་ང་རྒུད་མི་བཟོད་པས་སོ། །

[Block 2698]
མི་རྣམས་དཔའ་བོའི་ལམ་ཞེས་བྱ་བ་ནི་དཔའ་བོའི་འདྲོན་པོའོ།[^1712] །སྤྲོ་བ་དང་བྲལ་བ་ནི་སྤྲོ་བ་མེད་ཅིང་ལེ་ལོ་སྟེ་དེས་བླུན་པའོ། །

[Block 2699]
ཡང་ན་འདི་ལ་སྤྲོ་བ་མེད་པའོ། །

[Block 2700]
སྤྲོ་བ་མེད་པ་གང་ཡིན་པ་དེ་ནི་བླུན་པ་ཡིན་པས་སྤྲོ་བ་མེད་ཅིང་བླུན་པའོ། །

[Block 2701]
རབ་བསྒྲགས་ཤིང་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་མང་པོ་ལའོ། །

[Block 2702]
མ་བཅབས་རྒྱ་ཆེར་ཞེས་བྱ་བ་ནི་འདི་མི་མངོན་པ་མ༌[^1713]ཡིན་ཞིང་རྒྱ་ཆེར་རོ། །

[Block 2703]
བསྟན་པ་ནི་ཐམས་ཅད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2704]
ཚིག་དང་ཟུར་ལ་སོགས་ཀྱང་སྟེ། རྒྱུ་འདི་གསུམ་གྱི་སྡུག་བསྔལ་རབ་ཏུ་བསྒྲགས་པ་སྟེ། ཤིན་ཏུ་དཀའ་བར་བསྟན་པ་དེས་ན་ཡང་ཤིན་ཏུ་སྡུག་བསྔལ་ཆེན་པོ་ཉིད་དོ། །

[Block 2705]
བསྒྲིམས་པ་དང་བྲལ་བ་གང་ཡིན་པ་དེ་ནི་མི་སྒྲིམ་པའོ། །

[Block 2706]
མི་སྒྲིམ་པ་གང་ཡིན་པ༌[^1714]བརྟན་པ་ཡང་ཡིན་པས་མི་སྒྲིམ་བརྟན་གྱུར་པའོ། །

[Block 2707]
མི་སྒྲིམ་བརྟན་པར་གྱུར་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་མི་སྒྲིམ་བརྟན་པར་གྱུར་པའོ། །

[Block 2708]
དེ་ལྟར་ཐ་མལ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཅི་ལྟར་སྡུག་བསྔལ་ཐོས་པའི་དུས་དེ་བཞིན་དུ་གདུག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2709]
བྱམས་པ་དང་བྲལ་བ་ནི་འདི་ལྟར་མི་བྱམས་པའོ། །

[Block 2710]
མི་བྱམས་པ་ཡང་ཡིན་ལ་སྲ་བ་ཡང་ཡིན་པས་མི་བྱམས་ཤིང་སྲ་བའོ། །

[Block 2711]
མི་བྱམས་ཤིང་སྲ་བ་གང་ཡིན༌[^1715]པ་དེ་ནི་མི་བྱམས་ཤིང་སྲ་བ་ཉིད་དེ། དེ་ཡོད་པ་དེའི་ཕྱིར་རོ། །

[Block 2712]
དེ་ལྟར་གང་གོང་དུ་བསྟན་པ་དེ་མི་སྒྲིམ་བརྟན་པར་གྱུར་པའི་ཡིད་དང་ཐ་མལ་བཞིན་དུ་གནས་གྱུར་པ། །ཞེས་བྱ་བ་དག་དེ་ལྟ་བུའི་དོན་ཏོ། །

[Block 2713]
མཁན་པོས་བསྟན་པའི་རིམ་ལ༌[^1716]ཞེས་བྱ་བ་ནི། །

[Block 2714 [VERSE]]
གཞན་ནོར༌[^1717]མ་མཐོང་བླང་བར་གྱིས། །
ཞེས་བྱ་བ་ཡིན་ཏེ་དེའི་རིམ་པའོ། །
སྡིག་པའི་ལས་རྣམས་བྱེད་པ་ན། །

[Block 2715]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བདག་གིས༌[^1718]མི་རིག་པ༌[^1719]ལྷའི་མིག་གི་སྤྱོད་ཡུལ་དུ་བསྟན་ཏོ། །

[Block 2716]
བདག་ཉིད་སྦྱངས་པ་ལྷ་ཡི་སྤྱན། །ཞེས་བྱ་བ་འདིས་ནི་མངོན་པར་ཤེས་པའི་རང་བཞིན་གྱི་ལྷའི་མིག་གི་རང་བཞིན་དུ་བསྟན་ཏོ། །

[Block 2717]
ཉེས་བྱས་གཞན་གྱིས་མཐོང་བ་དང་། །གང་ཡང་བདག་གིས་མཐོང་བ་ཞེས་བྱ་བ་ནི་གཉི་གས་མཐོང་བ་ལས་སོ། །

[Block 2718]
ལེགས་པར་མཐོང་བ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་དཔྱད་ན་གང་དེ་བདག་གིས་མཐོང་བ་དེ་ནི་ལེགས་པར་མཐོང་བ་ཡིན་ཏེ། བདག་གིས་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2719]
ལེགས་པར་མཐོང་བ་དེ་ཉིད་བསྒྲུབ་པའི་ཕྱིར། །བདག་གི་དགོས་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་པ་ཡིན་ཏེ། ལེགས་པར་མཐོང་བ་དེ་ནི་མཐོང་བ་ངེས་པར་བསྟན་པས་སོ། །

[Block 2720]
ཆགས་པ་ལ་ཞེན་པ་ནི་ཆགས་པ་ལ་ཞེན་པའོ། །

[Block 2721]
རྩེ་གཅིག་ཏུ་དམིགས་པ་ནི་རྩེ་གཅིག་པའོ། །

[Block 2722]
ཆགས་པས༌[^1720]ཞེན་པ་ཡང་ཡིན་ལ་རྩེ་གཅིག་པ་ཡང་ཡིན་པས་ཆགས་པས་རྩེ་གཅིག་པའོ། །

[Block 2723]
ཆགས་པས་རྩེ་གཅིག་པའི་ཡིད་གང་ལ་ཡོད་པ་དེ་ནི་ཆགས་པས་རྩེ་གཅིག་ཡིད་གྱུར་པ་སྟེ། བདག་གི་དགོས་པ་ལ་ཆགས་པས་རྩེ་གཅིག་པའི་ཡིད་དུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2724]
དེ་ལྟར་ནོར་གྱི་ཕྱིར་ཞུགས་ཞེས་བྱ་བ་ནི་རྐུ་བ་ལ་ཞུགས་པའོ། །

[Block 2725]
སྐྱོན་དང་ཡོན་ཏན་ནི་ཡོན་ཏན་དང་ཡོན་ཏན་མ་ཡིན་པའི་ཁྱད་པར་རོ། །

[Block 2726]
ནོར་ཕྱིར་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་ནོར་ལ་བཙོང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2727]
ལྷའི་དབང་པོར་གྱུར་པའི་ཕྱིར་ནི་ལྷའི་དབང་ཕྱིར་ཏེ། ལྷའི་རྒྱལ་པོར་སྐྱེ་བའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2728]
ཆོས་དང་འགལ་བ་ཞེས་བྱ་བ་ནི་ཆོས་ཉམས་པའོ། །

[Block 2729]
གོས་ངན་པ་གྱོན་པ་ནི་གོས་ངན་པ་འཆང་བའོ། །

[Block 2730]
དགྲ་བོའི་ཁྱིམ་ན་འབྱོར་པ་མཐོང་བ་ཞེས་བྱ་བ་ནི་དེའི་གན་དུ་བསླང་བའི་དོན་དུ་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2731]
བུ་ལེགས་སོ་ལེགས་སོ་བྲམ་ཟེ་ཆེན་པོ་ལེགས་སོ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་རྒྱུ་དགུས་དུལ་བ་ཞེས་བྱ་བ་དང་། རང་གི་ཆོས་ཉིད༌[^1721]གྲགས་པ་ཞེས་བྱ་བ་སྟེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2732]
རབ་ཏུ་ཞི་བས་བརྒྱན་པ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་ལང་ཚོའི་ཚེ་ཡང་ཞི་ཞིང་ཆོས་བཟང་བས་ཞེས་བྱ་བ་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་གོ། །

[Block 2733]
ཁྱོད་ཀྱི་ཤེས་རབ་ཅེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི། ཐོས་པ་ལྡོབ་ཅིང་འཛིན་གསལ་དང་། །ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་གོ། །

[Block 2734]
རང་གི་ཆོས་ཉིད་ལམ་ཡིན་པས་རང་གི་ཆོས་ལམ་སྟེ། རང་གི་ཆོས་ཀྱི༌[^1722]བདེ་འགྲོ་ཐོབ་པར་བྱེད་པ་ནི་ཆོས་ཡིན་ནོ། །

[Block 2735]
དཀའ་ཐུབ་ཅེས་སྨོས་པས་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་གཉིས་གཟུང་ངོ་། །ཐོས་པ་དང་ཤེས་པ་སྨོས་པས་ནི་སེམས་ལས་བྱུང་བ་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་གཟུང་སྟེ། འདི་དག་གིས་ནི་བདག་ལ་ཕན༌[^1723]པའི་ཐབས་བསྟན་ཏོ། །
--- END BLOCKS ---
