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

[Block 2666]
ལེའུ་བདུན་པའི་ཞེས་པ་ནི་ཉེ་བར་བསྡུ་བའོ། །

[Block 2667]
[^1749]

[Block 2668]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་སོགས་པའི་སྒྲས་གསོལ་བ་གདབ་པ་ཙམ་བཤད་པས་སོ། །

[Block 2669]
འདོད་ཆགས་ཞེས་པ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་གྱི་བཤད་པ་ཞེས་པའི༌[^1750]བར་དུ་ནི་དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་དེ་བཞིན་གཤེགས་པ་ལྔའི་ངོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་བསྟོད་པས་སོ། །

[Block 2670]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ཡེ་ཤེས་གསུམ་གྱི་ངོ་བོར་གྱུར་པ་རང་བཞིན་གྱིས་འོད་གསལ་བའི་རྣམ་པ་ལ་བསྟོད་པའི་ཕྱིར་རོ། །

[Block 2671]
དེ་ནས་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 2672]
དེ་བཞིན་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲས་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་གྲུབ་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་བརྙན་བསྟན་པ་དང་། བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2673]
ས་ཕྱོགས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པ༌[^1751]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་གནས་ཀྱི་དབྱེ་བ་དང་དེ་ལེགས་པར་སྦྱངས་པ་དང་། ལྷའི་སྐུ་བསྒོམ་པ༌[^1752]སྔོན་དུ་འགྲོ་བས་མཆོད་པའི་སྤྲིན་སྤྲོ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2674]
མཁས་པ་ཞེས་པ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཕྱིའི་མེ་ཏོག་དང་། སྲོག་ལ་སོགས་པའི་རླུང༌[^1753]རྣམས་བསྟན་པའོ།[^1754] །

[Block 2675]
དཔག་ཚད་ཅེས་པ་ནས་སྒྲ་ཇི་བཞིན་པར་བཤད་པ་ཞེས་བྱ་བའི༌[^1755]བར་དུ་ནི་དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་དང་དེའི་ཚད་དང་དེ་ཉིད་དུ་སློབ་མ་འཇུག་པ་དང་། དེའི་ཕན་ཡོན་གསུངས་པས་སོ། །

[Block 2676]
ལེའུ་བརྒྱད་པའི་ཞེས་པ་འདིས་ཉེ་བར་སྡུད་པའོ། །

[Block 2677]
དེ་ནས་རྒྱལ་པོ་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པར་བཤད་པ་ཞེས་པའི་བར་དུ་དམ་ཚིག་ལྔ་ཙམ་བསྟན་པས་སོ། །

[Block 2678]
དེ་ཡང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 2679]
ནམ་མཁའ་ཞེས་པ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས་པའི་བར་དུ་ནི་དེ་ལ་དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་ལྔའི་སྐུ་ལ་དམིགས་ཏེ་སེར་སྣ་དང་འདོད་ཆགས་དང་དཀོན་མཆོག་གསུམ་ལ་གནོད་པ་དང་ང་རྒྱལ་དང་ཕྲག་དོག་ཅན་རྣམས་ཀྱི་རྫས་འཕྲོག་པ་ལ་སོགས་པ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལྔ་སྤྱོད་པས་བསོད་ནམས་ཆེན་པོ་ཐོབ་པར་འགྱུར་ཞེས་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2680]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ཕུང་པོ་ལ་སོགས་པ་རྣམ་པར་རྟོག་པ༌[^1756]རྣམས་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱིས་རོ་གཅིག་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2681]
དེ་ནས་ཞེས་པ་ནས་དགོངས་པས༌[^1757]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལག་ན་རྡོ་རྗེ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^1758]སྨོད་པའི་སེམས་བཟློག་པར་བྱ་བའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་འགལ་བའི་སྒྲའི་སྒོ་ནས་སྲུབ་ཤིང་དང་སྲུབ་གཏན་ལ་སོགས་པའི་རང་བཞིན་མེད་པའི་དཔེས་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2682]
ལེའུ་དགུ་པའི་ཞེས་པ་འདིས་ཉེ་བར་སྡུད་པ་བསྟན་ཏོ། །

[Block 2683]
[^1759]དེ་ནས་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ༌[^1760]ཞེས་བྱ་བའི་བར་དུ་ནི་ལུས་ལ་སོགས་པ་རྣམས་མཉམ་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་པས༌[^1761]སྟོང་པ་ཉིད་ཡིན་པར་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2684]
དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པར་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་རིམ་པ་སྤོང་བ་དང་དེ་བཞིན་གཤེགས་པའི་ཐུགས་བསྐུལ་བ་མེད་པས་དངོས་གྲུབ་མེད་ཅེས་དངོས་གྲུབ་ཡོངས་སུ་བཀག་པ་ཙམ༌[^1762]རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2685]
དེ་ཡང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 2686]
དེ་ནས་རྒྱལ་པོ་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲའི་སྦྱོར་བས་ཕྱག་རྒྱ་ཆེན་པོའི་མཚན་ཉིད་དེ་ཁོ་ན་ཉིད་ཐོབ་པ་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2687]
ལེའུ་བཅུ་པའི་ཞེས་པས་ཉེ་བར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 2688]
[^1763]

[Block 2689]
དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས། སྒྲ་ཇི་བཞིན་པས་བཤད་ཅེས་པའི་བར་དུ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་དང་དེ་བཞིན་གཤེགས་པ་ལྔའི་བསྐྱེད་པའི༌[^1764]རིམ་པ་བརྗོད་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2690]
ཡེ་ཤེས་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འཇམ་པའི་རྡོ་རྗེ་ལ་སོགས་པ་ཞེས་འགལ་བའི་སྒྲས་བརྗོད་པས་འོད་གསལ༌[^1765]བསྟན་པའི་ཕྱིར་རོ། །

[Block 2691]
འོད་ཟེར་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས༌[^1766]བཤད་ཅེས་པའི་བར་དུ་ནི་ཤིན་ཏུ་རྣལ་འབྱོར་གྱི་ལྷའི་དམིགས་པ་ལ་སོགས་པ་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 2692]
རྣམ་པར་དབེན་པ་ཞེས་པ་ནས་དྲང་བའི་དོན་དང་ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་དེ་ལ་དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་རྣམ་པར་དབེན་པ་དང་རིའི་མཆོག་ལ་སོགས་པའི༌[^1767]གནས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2693]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ནུ་མ་རྒྱས་པ་དང་། ཡན་ལག་མཆོག་ལ་སོགས་པ་དང་ལྡན་པའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་དང་ལྷན་ཅིག་ཏུ་སྤྱོད་པ་བསྟན་པས་སོ། །

[Block 2694]
མི་བསྐྱོད་པ་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^1768]མིག་ལ་སོགས་པ་བྱིན་གྱིས་རློབ་པ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཀྱང་བྱའོ་ཞེས་བསྟན་པས་སོ། །

[Block 2695]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲས་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་རྫོགས་པའི་རིམ་པ་བསྟན་པའི༌[^1769]ལེའུ་བཅུ་གཅིག་པའི་ཞེས་པས་ཉེ་བར་བསྡུས་པའོ། །

[Block 2696]
[^1770]

[Block 2697]
དེ་ནས་སྟོན་པ་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་སྤྲོས་པ་འདི་དག་ཐམས་ཅད་རང་བཞིན་མེད་པར་བསྟན་པས་སོ། །

[Block 2698]
དགོན་པ་ཞེས་པ་ནས་དྲང་བའི་དོན༌[^1771]ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས༌[^1772]བྱ་བའི་བར་དུ༌[^1773]དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་རྣམ་པར་དབེན་པའི་གནས་ཀྱི་ཁྱད་པར་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2699]
ངེས་པའི་དོན་ལ་ཡང་ཆོས་ཀྱི་སྐུ་ལ་སོགས་པའི་ཉེ་བར་དམིགས་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2700]
ལུས་དང་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལྕགས་གསུམ་ལ་སོགས་པའི་སྒྲའི་སྒོ་ནས་ཡེ་ཤེས་གསུམ་རྣམ་པར་དག་པའི་མཚན་ཉིད་འོད་གསལ་བའི་དེ་ཁོ་ཉིད་བསྟན་པས་སོ། །
--- END BLOCKS ---
