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
[Block 2731]
ལེའུ་བཅུ་བཞི་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། ཕྲེང་བའི་སྔགས་རྣམས་ནི་ལས་ཀྱི་རབ་འབྱམས་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2732]
ལས་ཀྱི་རབ་འབྱམས་ནི་ཞི་བ་ལ་སོགས་པའོ། །

[Block 2733]
སྒྲ་ཇི་བཞིན་པ་ནི་སོགས་པའི་སྒྲ་དང་རྟོག་པའི་སྒྲ་བརྗོད་པས་སོ། །

[Block 2734]
བར་བར་ན་ཞེས་པ་ནི་སྐབས་སྐབས་སུའོ། །

[Block 2735]
ལ་ལ་ནི་ཞེས་པ་ལ་རིམ་པ་མེད་པར་གནས་པའོ། །

[Block 2736]
དགོངས་པས་བཤད་པ་ཡང་ཡོད་དོ་ཞེས་པ་ནི་གང་དུ་འགལ་བའི་སྒྲས་དེ་ཁོ་ན་ཉིད་བསྟན་པའོ། །

[Block 2737]
དེ་བཞིན་དུ་ལེའུ་བཅོ་ལྔ་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་མཐའ་དྲུག་གི་དོན་ཁོ་ན་བསྟན་ཏོ། །

[Block 2738]
ལུས༌[^1797]ཚད་མ་ཉིད་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་ལྟར་མདོའི་ཚིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 2739]
བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བ་ལས་སོ། །

[Block 2740]
དགོངས་པས་བཤད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 2741]
རྣལ་འབྱོར་གྱི་རྒྱུད་ཅེས་པ་ནི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2742]
དེ་ལྟ་ན་ཡང་རྣལ་འབྱོར་མའི་རྒྱུད་རྣམས་ལས་ཀྱང་མཐའ་དྲུག་མཐོང་ན་རྣལ་འབྱོར་གྱི་རྒྱུད་ཁོ་ན་ལས་ཅིའི་ཕྱིར་བཤད་ཅེ་ན། དེ་ལ༌[^1798]བདེན་ཏེ་རྣལ་འབྱོར་གྱི་རྒྱུད་ནི་ཐུན་མོང་ཡིན་ལ་རྣལ་འབྱོར་མའི་རྒྱུད་ཐུན་མོང་མ་ཡིན་ཞེས་ཁྱད་པར་ཐམས་ཅད་སྤྱིའི་དབང་དུ་སོང་བ་ཡིན་པས་ཁྱད་པར་རྣམས་བསྡུ་བར་བྱའོ། །

[Block 2743]
དེ་ལྟར༌[^1799]ན་རྣལ་འབྱོར་རྒྱུད་ནི་མཐའ་དྲུག་ཅན་ཡིན་ཞེས་པའི་ཚིག་ལས་འགྲེལ་པ་འདི་མཐའ་དྲུག་པ་ཞེས་མི་འཐད་དོ། །

[Block 2744]
རྒྱན་བདུན་པ་ཞེས་རིགས་པ་ཡིན་ཏེ། དེ་དག་ཚང་བའི་ཕྱིར་རོ་ཞེ་ན། སྨྲས་པ་གླེང་གཞི་ཞེས་བྱ་བ་ནི་ཚིག་ཐམས་ཅད་དུ་བཤད་པར་བྱ་བ་ཡིན་ཏེ། གང་གི་ཕྱིར་ངེས་བརྗོད་པ་ལ་སོགས་པ་ལྔ་སྟོན་གྱི་ཚིག་རེ་རེ་ལ་ནི་མི་འཇུག་གོ། །

[Block 2745]
རིགས་པ་ཡང་ཚིག་རེ་རེ་ལ་སྨྲ་བར་བྱ་བ་མ༌[^1800]ཡིན་ཏེ། གླེང་བསླང་བ་བཞིན་དུ་དེ་ཡང་དེའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2746]
འཆད་པ་པོའི་རྒྱན་ཡང་ལོགས་པ༌[^1801]མ་ཡིན་ཏེ་མ་གཏོགས་པར་བཤད་པ༌[^1802]དབྱེ་བ་མ༌[^1803]འགྲུབ་པས་སོ། །

[Block 2747]
ཉན་པ་པོའི་རྒྱན་ཡང་རྟེན་མེད་པ་མ་ཡིན་ཏེ་དེའི་རྟེན་མཐའ་དྲུག་ཡིན༌[^1804]པའི་ཕྱིར་རོ། །

[Block 2748]
མཐའ་དྲུག་གི་དོན་སོ་སོར་བསྟན་པ་ཉིད་ཀྱི་རིམ་པ་གཉིས་སྡུད་པར་བྱེད་པའི་བརྗོད་པར་བྱ་བའི་དོན་མ་ལུས་པ་བསྡུ་བའི་རྒྱན་ཞེས་བྱ་བ་འགྲུབ་པོ་ཞེས་དོན་གྱི་ཤུགས་ཀྱིས་ཚིག་རེ་རེ་ལ་མཐའ་དྲུག་གིས་བཤད་པས་དེའི་མིང་གིས་འགྲེལ་པར༌[^1805]གྲགས་སོ། །

[Block 2749]
དེ་ལྟར༌[^1806]ན་བཤད་པ་རྣམ་པ་བཞི་ཡང་ཚིག་རེ་རེ་ལ་ལྔ་ལྔར༌[^1807]ཡོད་པས་ཞེས་མཐའ་དྲུག་གིས༌[^1808]བཤད་པ་མི་རིགས་ཤེ་ན། སྨྲས་པ་དང་།[^1809] གཞན་གྱི་བརྗོད་པས་ཉེས་པ་མེད་དོ། །

[Block 2750]
དཔེར་ན་མའི་བུ་དང་ཕའི་བུ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 2751]
གང་གི་ཕྱིར་གཉི་ག་ལ་འབྱུང་བ་དེ་ཅིག་ཤོས་ཀྱི་མིང་གིས་ཀྱང་གྲགས་པ་ཡིན་ནོ། །

[Block 2752]
དེ་བས་ན་རིམ་པ་འདི་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 2753]
མཐའ་དྲུག་ཏུ་བཤད་པ་དང་རྣམ་པ་བཞིར་བཤད་པ་ཞེས་པ་ནི་མཐའ་དྲུག་དང་བཤད་པ་རྣམ་པ་བཞིས་བཟུང་བས་རྒྱན་གཞན་རྣམས་དེ་དག་ཏུ་འདུས་པས་སོ། །

[Block 2754]
དཔལ་གསང་བ་འདུས་པའི་དོན་རྒྱས་བཏབ་པ་ཡིན་ལ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་བདག་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོས་དེ་དག་གིས་རྒྱས་བཏབ་པ་ནི་བཅིངས་པའོ། །

[Block 2755]
དེས་ན་རྟོགས་པར་དཀའ་བའི་རྒྱུད་འདི་ཡིན་ཞེས་བསྟན་ཏོ། །

[Block 2756]
དེ་མ་གཏོགས་པ་ཞེས་བྱ་བ་འདིས་ད་ལྟར༌[^1810]བྱུང་བ་རྣམས་ཀྱིས་མི་རྟོགས་ཞེས་བསྟན་ཏོ། །

[Block 2757]
སྒྲ་ཇི་བཞིན་པར་བཤད་པའི་སྒྲའི་དོན་ཙམ་ལ་བརྟེན་ཏེ་ཞེས་པ་ནི་མཐའ་དྲུག་གི་དོན་མི་ཤེས་ནས་སོ། །

[Block 2758]
འགལ་བ་དང་ཤིན་ཏུ་རྨད་དུ་གྱུར་པའི་བྱ་བ་བྱེད་པས་ནི་ལྟ་བ་ལ་སོགས་པའི༌[^1811]དབང་གིས་མ་དང་སྲིང་མོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྒྲ་ཇི་བཞིན་དུ་གཟུང་བས་འགལ་བ་སྤྱོད་པས་སོ། །

[Block 2759]
ལས་ཀྱི་དབང་དུ་འགྱུར་རོ་ཞེས་པ་ནི། སྡིག་པའི་ལས་ཀུན་ཏུ་སྤྱོད་པས་མནར་མེད་པ་ལ་སོགས་པར་སྐྱེ་བར་འགྱུར་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2760]
དེ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2761]
གསང་བའི་བདག་པོ་ཞེས་པ་ནི་བོད་པའི་ཚིག་གོ། །

[Block 2762]
ཚུལ་ཆེན་འདི་ནི་རྙེད་གྱུར་ནས། །ཞེས་པ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2763]
ཟད༌[^1812]མིན་དོན་ནི་སྒྲ་ཇི་བཞིན་པ་ཡིན་ཞེས་ཐ་ཚིག་གོ། །

[Block 2764]
ལམ་ངན་པ་ཞེས་པ་ནི་སོ་སོའི་སྐྱེ་བོའི་ལམ་དུའོ། །

[Block 2765]
མངོན་པའི་ང་རྒྱལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིག་པའི་དབང་ཙམ་ཐོབ་ནས་སྒྲུབ་པའི་ཐབས་ཙམ་ཡོངས་སུ་ཤེས་པས་ང་རྒྱལ་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་ཐ་ཚིག་གོ། །

[Block 2766]
ཆོས་ནི་གཡོ་ཡིས་བྱེད་པར་འགྱུར། །ཞེས་པ་ནི་གཡོ་སྒྱུའི༌[^1813]དབང་གིས་ཆོས་བྱེད་པ་སྟེ་སོ་བྱ་བཞིན་ནོ། །

[Block 2767]
སེམས་ཅན་སླུ་བར་བྱེད་པ་ཞེས་བྱ་བའི༌[^1814]དོན་ཏོ། །

[Block 2768]
དེས་ནི་འདུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དམ་ཚིག་ཉམས་པ་དང་ཡོངས་སུ་མི་ཤེས་པ་དག་བསྟན་ཏོ། །

[Block 2769]
མངོན་སུམ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་སློབ་དཔོན་ལ་སྨོད་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 2770]
སྐད་ཅིག་ཅེས་པ་ནས་བྱམས་པའི་སེམས་མེད་པ་དང་། བགྲོད་མིན་ལ་འགྲོ་བ་དང་། མཚམས་མེད་པ་བྱེད་པ་དང་། མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལ་སྤྱོད་པར་བྱེད་པ་སྟོན་པར་བྱེད་དོ། །
--- END BLOCKS ---
