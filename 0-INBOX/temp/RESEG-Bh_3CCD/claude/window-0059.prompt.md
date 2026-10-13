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
[Block 2066]
སྣང་བ་མཐའ་ཡས་ཀྱི་ངོ་བོ་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པ་སྟེ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ཉིད་དུ་སོ་སོར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 2067]
མི་བསྐྱོད་པའི་ངོ་བོ་ནི་མངོན་པར་བྱང་ཆུབ་པ་སྟེ་འོད་གསལ་བ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2068]
དོན་ཡོད་གྲུབ་པའི་ངོ་བོ་ཉིད་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་སྟེ་བྱ་བ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2069]
ཡེ་ཤེས་ལྔ་ནི་འདིར་དེ་བཞིན་གཤེགས་པ་དང་དབྱེར་མེད་པའི་ཕྱིར་མ་བསྟན་ཏོ། །

[Block 2070]
གཏི་མུག་རྣམ་པར་དག་པའི་ངོ་བོ་ནི་རྡོ་རྗེ་བཟླས་པ༌[^1399]སྟེ། སྔགས་ཐམས་ཅད་ལ་མ་རྨོངས་པའི་ཕྱིར་རོ། །

[Block 2071]
ཞེ་སྡང་རྣམ་པར་དག་པ་ནི་སེམས་རྣམ་པར་དག་པ་སྟེ། ཕྱིན་ཅི་མ་ལོག་པའི་རང་བཞིན་དང་སྣང་བ་ཐམས་ཅད་ལ་རྣམ་པར་སྣང་བའི༌[^1400]ཕྱིར་རོ། །

[Block 2072]
ང་རྒྱལ་རྣམ་པར་དག་པ་ནི་བདག༌[^1401]བྱིན་གྱིས་རློབ་པ་སྟེ་ཐ་མལ༌[^1402]པའི་ང་རྒྱལ་ལོག་པས་སོ། །

[Block 2073]
འདོད་ཆགས་རྣམ་པར་དག་པ་ནི་མངོན་པར་བྱང་ཆུབ་པ་སྟེ་འདོད་ཆགས་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2074]
ལྟ་བ་རྣམ་པར་དག་པ་ནི་ཟུང་དུ་འཇུག་པ་སྟེ་ལྟ་བ་ཐམས་ཅད་ཀྱི་དྲི་མ་མེད་པའི་ཕྱིར་རོ། །

[Block 2075]
ངག་རྣམ་པར་དག་པ་ནི་རྡོ་རྗེ་བཟླས་པ་སྟེ་ངག་གི་བརྗོད་པ་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2076]
སེམས་རྣམ་པར་དག་པ་ནི། ཐམས་ཅད་རྣམ་པར་དག་པའི་རིམ་པ་སྟེ། སེམས་དང་སེམས་ལས་བྱུང་བ་ཐམས་ཅད་འགོག་པའི་ཕྱིར་རོ། །

[Block 2077]
ལུས་རྣམ་པར་དག་པ་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པ་སྟེ་ཡིད་ཀྱི་རང་བཞིན་གྱི་སྐུ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2078]
དེས་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྣམ་པར་དག་པ་སྟེ་ཐམས་ཅད་སྒྱུ་མ་ཙམ་དུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2079]
དོན་དམ་པའི་བདེན་པ་རྣམ་པར་དག་པ་ནི་མངོན་པར་བྱང་ཆུབ་པ་སྟེ་འོད་གསལ་བའི་དེ༌[^1403]ཁོ་ན་ཉིད་མངོན་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2080]
བདེན་པ་གཉིས་རོ་གཅིག་པ་ནི་ཟུང་དུ་འཇུག་པ་སྟེ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་ངོ་བོ་ཡིན་པས་སོ། །

[Block 2081]
དེ་བཞིན་དུ་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱང་གཏི་མུག་ལ་སོགས་པར་འདུས་པར་ཤེས་པར་བྱའོ།[^1404] །

[Block 2082]
དེ་རྣམས་ཡང་དག་བསྡུས་པ་ནི་ཞེས་བྱ་བ་ལ། དབྱེ་བ་ཐམས་ཅད་གཅིག་ཏུ་འདུས་པ་དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 2083]
རང་རང་གི་རིགས་ལ་ལྟོས་པ་དང་། ཐ་དད་པའི་རིགས་ལ་ལྟོས་པའོ། །

[Block 2084]
དེ་ལ་ཡང་རང་གི་རིགས་ལ་ལྟོས་པ་ནི་ཇི་ལྟར༌[^1405]རྡོ་རྗེ་བཟླས་པ་རྣམ་པ་བཅུ་མ་ནིང་གི་བཟླས་པ་གཅིག་པུ་ལ་འདུས་སོ། །

[Block 2085]
དེ་བས་ན་དེ་ནི་ལེའུ་བཅུ་གསུམ་པ་ལས་ཐ་མར༌[^1406]བསྟན་ཏོ། །

[Block 2086]
སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་པོ་ནི་འོད་གསལ་བ་ལའོ། །

[Block 2087]
ཆོས་ཀྱི་སྐུ་ལ་སོགས་པ་ཡེ་ཤེས་ཀྱི༌[^1407]སྐུ་ལའོ། །

[Block 2088]
འདོད་ཆགས་དང་འདོད་ཆགས་བྲལ་བ་དང་འདོད་ཆགས་བར་མ་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ལའོ། །

[Block 2089]
རྒྱུ་དང་འབྲས་བུ་དག་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལ་འདུས་པར་འགྱུར་རོ། །

[Block 2090]
རིགས་ཐ་དད་པ་ལ་ལྟོས་པ་ནི་ཇི་ལྟར་རིམ་པ་ཐམས་ཅད་རྒྱུ་དང་འབྲས་བུའི་ངོ་བོར་གནས་ཏེ། དེ་ལ་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་རིམ་པ་བཞི་པོ་ནི་རྒྱུའོ། །

[Block 2091]
ཟུང་དུ་འཇུག་པ་རིམ་པ༌[^1408]འབྲས་བུ་ཡིན་པས་རིམ་པ་བཞི་པོ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་ལྔ་པ་ལ་འདུས་ཏེ། བྱ་བ་བྱས་པ་དང་། དེ་ལས་གཞན་པ་མི་སློབ་པའི་ཕྱིར་རོ། །

[Block 2092]
དེ་ལྟར་རིམ་པ་ལྔ་པོ་དེ་དག་གི་དབྱེ་བ་དང་བསྡུ་བ་གང་གིས་ཤེས་པ་དེས་རྒྱུད་ནི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་རྣམས་རིག་ཅིང་ཤེས་སོ་ཞེས་ཚིག་གི་དོན་ཏོ། །

[Block 2093]
ཚིག་གི་དོན་གཅིག་པུ་ཙམ་བཤད་པ་ལ་མཁས་པས་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 2094]
ད་ནི་རིམ་པ་ལྔའི་བསྡུས་པའི་དོན་ཤེས་པས་མཐའ་དྲུག་གི་འགྲེལ་པ༌[^1409]འདི་ལ་སྣོད་དུ་རུང་བར་འགྱུར་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། སྔགས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། དེ་ལ་སྔགས་དང་སྔགས་ནི་སྔགས་སོ། །

[Block 2095]
གཅིག་ནི་ལྷག་མའི་བསྡུ་བ་བྱས་ནས་སྔགས་ཀྱི་སྒྲ་གཉིས་གཟུང་ངོ་། །དེ་ལ་སྔགས་ཀྱི་སྒྲ་དང་པོས་ནི་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པ་ཏིང་ངེ་འཛིན་གསུམ་གྱིས་རྫོགས་པའི་སྔགས་ཀྱི་སྐུ་བརྗོད་པའོ། །

[Block 2096]
གཉིས་པས་ཀྱང་སྔགས་ཐམས་ཅད་ཀྱི་སྙིང་པོར་གྱུར་པ་ཡི་གེ་གསུམ་པོ་འཇུག་པ་ལ་སོགས་པ་གཙོར་གྱུར་པ་རྗོད་པར་བྱེད་དོ། །

[Block 2097]
དེའི་རྗེས་སུ་ཡེ་ཤེས༌[^1410]དང་རྣམ་ཤེས་དང་རང་བཞིན་ཐམས་ཅད་འགོག་པས་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་རྫོགས་པ༌[^1411]སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་སོ་སོར་བསྟན་པའི་རིམ་པ་ནི་སེམས་སོ། །

[Block 2098]
དེ་ལ་རྣམ་པར་དག་པའི་ཚིག་མི་མངོན་པར་ཤེས་པར་བྱའོ། །

[Block 2099]
དེའི་རྗེས་སུ་གྲིབ་མ་དང་། སྒྱུ་མ་དང་འཇའ་ཚོན་ལ་སོགས་པ་སྒྱུ་མའི་དཔེ༌[^1412]རྣམས་ཀྱིས་མཚོན་པ་ཡེ་ཤེས་ཀྱི་སྐུ་སྟོན་པར་བྱེད་པ་ནི་ལུས་སོ། །

[Block 2100]
སྒྱུ་མའི་ལུས་པོ་དེ་ལ་ཡང་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པ་བསྒོམ་པའི་དབང་གིས་ཉེ་བར་ཞི་བས་འོད་གསལ་བ་ལ་འཇུག་པའི་མཚན་ཉིད་ཀྱི་རིམ་པ་སྟོན་པར་བྱེད་པ་ནི་རྣམ་དག་གོ། །

[Block 2101]
སྔར་བཤད་པའི་ཀུན་རྫོབ་དང་དོན་དམ་པ་ལ་སོགས་པ་གཉིས་སུ་འཛིན་པའི་རྣམ་པར་རྟོག་པ་གསལ་བའི༌[^1413]མཚན་ཉིད་ཀྱི་རིམ་པ་སོ་སོར་བསྟན་པ་ནི་ཟུང་དུ༌[^1414]འཇུག་གོ། །

[Block 2102]
དེ་དག་ལ་བརྟེན༌[^1415]ཏེ་རྐྱེན་དང་ལྡན་པའི་སྒྲ་ཕྱེ་བས༌[^1416]ལས་ཀྱི་དོན་དུ་འམ་རྒྱུ༌[^1417]

[Block 2103]
ལྔ་པ་ལ༌[^1418]བྱའོ། །

[Block 2104]
རིམ་པ་ལྔའི་བསྡུས་པའི་དོན་ནི་དེ་དག་སྐབས༌[^1419]ཀྱི་རིམ་པའི་རིགས་པས་བསྡུས་པའི་དོན་རྣམས་ཤེས་ནས་ནི་རྟོགས་ནས་སོ། །ཅི་བྱ་ཞེ་ན། མཐའ་དྲུག་ལ་འཇུག་གོ་ཞེས་སྨོས་ཏེ་དོན་དྲུག་སོ་སོར་བསྟན་པའི་འགྲེལ་པ་འདི་ལ་འཇུག་པར་བྱ་སྟེ། དེ་མཉན་པའམ་བཤད་པ་ལ་སྣོད་དུ་རུང་བར་འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 2105]
ཇི་ལྟར་མཐའ་དྲུག་གི་འགྲེལ་པའི་རིམ་པ་ལྔ་བརྗོད་པར་བྱ་བ༌[^1420]དེ་བཞིན་དུ་སྔོན་དུ་བཤད་ཟིན་པ་དང་འཆད་པར་ཡང་འགྱུར་རོ། །
--- END BLOCKS ---
