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
[Block 2346]
དེ་བས་འདི་སྒྲའི་རྒྱན་ཡིན་ཏེ། སྒྲ་སྣ་ཚོགས་པ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2347]
སྤྱིའི་དོན་བསྟན་པར་བྱ་བའི་ཕྱིར། མདོ་སོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མདོ་སྡེ་ལ་སོགས་པ་ནི་ཉན་ཐོས་དང་མདོ་སྡེ་པ་དང་རྣལ་འབྱོར་སྤྱོད་པ་དང་། དབུ་མ་པ་རྣམས་སོ། །

[Block 2348]
གང་གི་ཚེ་སྔོན་གྱི་བག་ཆགས་ཀྱི་འབྲེལ་པའམ། དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པས་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་བསྟན་པར་གྱུར་པ་དེའི་ཚེ་རང་གི་སྡོམ་པ་དང་འགལ་བའི་དམ་ཚིག་དང་སྡོམ་པ་ཐོས་ནས་འགྱོད་པར་གྱུར་པས་གསང་སྔགས་ཀྱི་གསུང་ལ་སྐུར་བ༌[^1541]བཏབ་པའི་སྡིག་པ་མེ་ལ་ཕྱེ་མ་ལེབ་བཞིན་དུ་ལྟུང་བར་འགྱུར་རོ། །

[Block 2349]
དེ་རྣམས་ཀྱི་འགྱོད་པ་བཟློག་པར་བྱ་བའི༌[^1542]ཕྱིར་དེ་དང་མཐུན་པར་བཅོམ་ལྡན་འདས་ཀྱི་བསྟན་པ་གསུངས་སོ། །

[Block 2350]
གང་གིས་འདི་ནི་རིགས་པ་ཡིན། །ཞེས་ལམ་དེ་ཉིད་དུ་ཞུགས་ཤིང་སྐུར་བ༌[^1543]མི་འདེབས་སོ། །

[Block 2351]
མདོ་སྡེ་ལ་སོགས་པ་ལ་ཞུགས་པའི་འགྱོད་པ་ཟློག༌[^1544]པར་བྱེད་པའི་མཚན་ཉིད་ནི་སྤྱིའི་དོན་གྱི་ཡན་ལག་དང་པོའོ། །

[Block 2352]
དེ་བཞིན་དུ་ཡང་བསྐྱེད་པའི་རིམ་པ་དང་ལྡན་པས་ན་ཞེས་པ་ནི་ཡན་ལག་གཉིས་པའོ།[^1545] །

[Block 2353]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་གྲགས་པ་དང་བསྟན་བཅོས་པའོ། །

[Block 2354]
དེ་ལ་དང་པོ་སྦྱོར་བ་དང་དཀྱིལ་འཁོར་རྒྱལ་བ་དང་ལས་ཀྱི་རྒྱལ་བའི་ཏིང་ངེ་འཛིན་གསུམ་སྟོན་པར་བྱེད་པ་ནི་ཡོངས་སུ་གྲགས་པའོ། །

[Block 2355]
བྱང་ཆུབ་ཀྱི་སེམས་ཁོ་ན་ལས་ཁམས་གསུམ་ཐམས་ཅད་སྐྱེ་བ་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་དེ་ཡང་དབང་པོ་གཉིས་སྙོམས་པར་ཞུགས་པ་ལས་འབྱུང་ངོ་ཞེས་པ་ནི་བསྟན་བཅོས་པའོ། །

[Block 2356]
གཉི་ག་དེ་དག་ཀྱང་སྤྱིའི་དོན་ཞེས་བཤད་པའི་བྱེ་བྲག་སྟེ་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 2357]
རྫོགས་པའི་རིམ་པ་སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར། །འདོད་ཆགས་ཆོས༌[^1546]ཞེས་བྱ་བ་ལ་སོགས་པ་འདོད་ཆགས་ཀྱི་ཆོས་ནི་འདོད་ཆགས་ཀྱི་ཆོས་ཏེ་དེའི་ཆོས་ཉིད་དོ། །

[Block 2358]
བཟླས་པའི་གནས་སྐབས་སུ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་བཟླས་པས་འདོད་ཆགས་ལ་སོགས༌[^1547]གང་གིས་འདོད་ཆགས་རྣམ་པར་དག་པར་གྱུར་པའོ། །

[Block 2359]
འདི་ནི་ཉེ་བར་མཚོན་པ་སྟེ། ཞེ་སྡང་ལ་སོགས་པའི་རྣམ་པར་དག་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 2360]
དེ་རབ་ཏུ་སྟོན་པ་ནི་སྦས་པའི་དོན་གཅིག་པའོ། །

[Block 2361]
དེ་ཡིས་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་བཤད་དོ། །

[Block 2362]
བཟླས་པའི་གནས་སྐབས་སུ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་བཟླས་པས་འདོད་ཆགས་ལ་སོགས་པ༌[^1548]རྣལ་འབྱོར་པས་དག་པར་བྱེད་དོ། །

[Block 2363]
ཀུན་རྫོབ་བདེན་པ་རྟོགས་པ་དང་། །ཞེས་པ་ནི་མྱུར་བའི་ཏིང་ངེ་འཛིན་ནམ་སྣང་བ༌[^1549]ལ་སོགས་པའི་རྣལ་འབྱོར་གྱིས་སྐྱེད་པའི་ལྷའི་སྐུ་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བཅུ་གཉིས་ཀྱི་སྒོ་ནས་མཐོང་བ་ཞེས་བྱ་བ་འདིས་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་སྦས་པའི་དོན་གཉིས་པའོ། །

[Block 2364]
ཡེ་ཤེས་གསུམ་པོ་རྣམ་དཔྱད་པའི། །ཞེས་པ་ནི་འདིས་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 2365]
དེ་ལྟར་རྡོ་རྗེ་བཟླས་པ་དང་སེམས་རྣམ་པར་དག་པ་དང༌[^1550]རང་བྱིན་གྱིས་བརླབ་པ་སྟེ་རིམ་པ་གསུམ་ནི་སྦས་པའོ། །

[Block 2366]
སྦས་པ་ནི་སྦས་པའི་མཚན་ཉིད་ཅན་རིམ་པ་གསུམ་པོ་གང་ལ་ཡོད་པ་དེ་ནི་སྦས་པའོ། །

[Block 2367]
རིམ་པ་ཐ་མ་གཉིས་པོ་སོ་སོར་སྟོན་པར་བྱེད་པ་ན་མཐར་ཐུག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། འོད་གསལ་བ་ལ་རབ་འཇུག་དང་། །ཞེས་སྨོས་ཏེ། ཕྱག་རྒྱ་དང་། ཏིང་ངེ་འཛིན་གྱི་རིམ་པ་དག་གིས་ཡང་དག་པར་ཐོབ་པར་བྱ་བའི་དེ་ཁོ་ན་ཉིད་བཞི་པ་མངོན་དུ་བྱེད་པའོ། །

[Block 2368]
དེས་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 2369]
དེ་བཞིན་དུ། ཟུང་དུ་འཇུག་པ་རྟོགས་པ་སྟེ། །ཞེས་བྱ་བ་འདིས་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 2370]
མཐའ་ནི་མུར་ཐུག་པ་ཡི༌[^1551]ཚིག །ཅེས་པ་ནི་དེ་ལས་གཞན་པའི་རིམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2371]
དེ་ལྟར་བཤད་པ་རྣམ་པ་བཞིས་རིམ་པ་གཉིས་པོ་ཡོངས་སུ་རྫོགས་པར་བསྟན་ཏོ། །

[Block 2372]
དེ་ལྟར་ཡི་གེའི་དོན་ནི་སྒྲའི་རྒྱན་ནོ། །

[Block 2373]
སྤྱིའི་དོན་དང་སྦས་པ་དང་མཐར་ཐུག༌[^1552]པའི་དོན་ནི་དོན་གྱི་རྒྱན་ནོ། །

[Block 2374]
དེ་རྣམས་ཀྱིས་རིམ་པ་གཉིས་པོ་བརྒྱན་པར་བྱེད་ཅེས་པའི་ཐ་ཚིག་གོ། །

[Block 2375]
གལ་ཏེ་བཤད་པ་རྣམ་པ་བཞི་པོས་རིམ་པ་གཉིས་པོ་བསྟན་པ་ཡིན་ན། དེའི་ཚེ་སྒྲ་དང་དོན་གྱི་དབྱེ་བས་ཅི་ཞིག་བྱ་ཞེ་ན། སྨྲས་པ། ངེས་པ་མེད་པའི་ཕྱིར་མཐའ་དྲུག་ཏུ་གསུངས་ཏེ། བཤད་པ་རྣམ་པ་བཞི་པོ་བཞིན་དུ་མཐའ་དྲུག་གིས་ངེས་པར་རིམ་པ་གཉིས་པ༌[^1553]བཤད་པ་མ་ཡིན་ཏེ། [^1554]དྲང་བའི་དོན་གྱིས་རྫོགས་པའི་རིམ་པ་བཀག་ནས་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཙམ་སྟོན་པར་བྱེད་དེ། དེ་བས་ན་སྤྱིའི་དོན་ལས་ཁྱད་པར་ཡོད་པའོ། །

[Block 2376]
ངེས་པའི་དོན་ནི་རྫོགས་པའི་རིམ་པ་སྟོན་པར་བྱེད་པ་ཡང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་སྟོན་པ་ལ་ངེས་པ་མེད་དེ། སྟོང་པ་ཉིད་ཙམ་མམ་གཞན་གང་ཅི་ཡང་རུང་བ་དེས་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2377]
རེས་འགའ་ཞིག་བསྟན་པས་ཀྱང་དེའི་ཐ་སྙད་མི་རིགས༌[^1555]སོ། །

[Block 2378]
དགོངས་པ་བཤད་པས་ཀྱང་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་སོ་སོར་སྟོན་པར་བྱེད་པ་སྔ་མ་བཞིན་ནོ། །

[Block 2379]
ཁྱད་པར་ནི་འགལ་བའི་སྒྲ་རབ་ཏུ་སྦྱོར་བས་སོ། །

[Block 2380]
དགོངས་པ་མ་ཡིན་པ༌[^1556]དེ་བཞིན་ཡིན་ནོ། །

[Block 2381]
སྒྲ་ཇི་བཞིན་པས་ནི་ཕྱིའི་སྤྲོས་པ་ཙམ་སྟོན་པར་བྱེད་པའི་ནུས་པ་ཡོད་ཀྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 2382]
ཤིན་ཏུ་སྤྲོས་པ་མེད་པའི་སྤྱོད་པ་ནི་རྫོགས་པའི་རིམ་པའི་ཡན་ལག་ཡིན་ཡང་སྒྲ་ཇི་བཞིན་པས་དེ་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་གྱི་འོན་ཀྱང་དེའི་མཚན་ཉིད་ཙམ་རྗོད་པར་བྱེད་པས་སྐྱོན་མེད་དོ། །

[Block 2383]
སྒྲ་ཇི་བཞིན་མ་ཡིན་པ་ནི་འཇིག་རྟེན་དང་བསྟན་བཅོས་ལས་ཕྱིར་གྱུར་པས་བསྐྱེད་པའི་རིམ་པ་ཙམ་ལ་ཡང་སྟོན་པར་བྱེད་པའི་ནུས་པ་མེད་ན་ཡང་། ཡན་ལག་ལྔ་དང་ལྡན་པའི་རྫོགས་པའི་རིམ་པ་ལ་ག་ལས་འགྱུར་ཏེ། བརྡ་ཙམ་སྟོན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2384]
དེའི་ཕྱིར་ན་མཐའ་དྲུག་ལས་བཤད་པ་རྣམ་པ་བཞི་པོ་ཐ་དད་པ་ཁོ་ནའོ། །

[Block 2385 [HEADING]]
##### འཆད་པ་པོའི་རྒྱན། ^1-7-3-1-0
--- END BLOCKS ---
