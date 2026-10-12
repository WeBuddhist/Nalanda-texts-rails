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
[Block 2206]
ལེའུ་དེ་བཞིན་ཆོ་ག་དང་། །ཞེས་པ་ནི་ལེའུ་ལ་སོགས་པ་བཞི་པོ་ནི་གཞུང་རྫོགས་པའི་གནས་ཡིན་ཏེ། གང་གི་ཕྱིར་ཡོངས་སུ་གཅོད་ཅིང་གཞལ་བྱ་གང་དུ༌[^1476]རྫོགས་པར་བྱེད་པ་དེ་ནི་ལེའུ་འོ། །

[Block 2207]
གཞན་དུ་ནི༌[^1477]ལེའུ་བཅོ་བརྒྱད་ཀྱི་བདག་ཉིད་ཀྱི་རྒྱུད་ངེས་པར་མི་འགྱུར་ཏེ། མང་ཉུང་གི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2208]
དེ་བཞིན་དུ་ཆོ་ག་ལ་སོགས་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 2209]
ཇི་སྐད་དུ། ཡོངས་སུ་གཅོད་པས་ལེའུ་སྟེ།

[Block 2210 [VERSE]]
སྟོང་པ་ཉིད་ཀྱི་ཆོ་གར་འགྱུར། །
སྤྲོས་པ་མང་བས་དུམ་བུ་སྟེ། །
སྒྲིབ་པ་མེད་པས་རིམ་པ་ཕྱེ། །

[Block 2211]
ཞེས་འབྱུང་ངོ་། །གཞུང་ཉིད་ཀྱིས་ནི་གྲངས་ཀྱང་ངོ་། །ཞེས་པ་ལ་ཀྱང་གི་སྒྲ་ནི་དོན་གྱིས་ཡིན་ཏེ། གང་དུ་དོན་ཡང༌[^1478]ཡོངས་སུ་རྫོགས་པ་དེ་ཡང་ལེའུ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 2212]
དགོས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། དགོས་པ་ཡང་ནི་ཞེས་བྱ་བ་སྨོས་ཏེ་དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། དགོས་པ་དང་། དགོས་པའི་དགོས་པའོ། །

[Block 2213]
དེ་དག་རང་དང་གཞན་གྱི་དོན་སྒྲུབ་པར་བྱེད་པའི་མཚན་ཉིད་དོ། །

[Block 2214]
སྒྲུབ་པ་བརྒྱད་ནི་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་གཙོར་གྱུར་པའོ། །

[Block 2215]
སངས་རྒྱས་ཉིད་ནི་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 2216]
གྲུབ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའོ། །

[Block 2217]
འཇིག་རྟེན་པ་ནི་ཞི་བ་ལ་སོགས་པའི་ཆོ་གའོ། །

[Block 2218]
འཇིག་རྟེན་ལས་འདས་པ་ནི་ཕྲ་བ་ལ་སོགས་པའོ། །

[Block 2219]
དེ་ལ་ཞི་བ་དང༌[^1479]རྒྱས་པ་དང་དབང་དང་དགུག་པ་དང་རྣམ་པར་སྡང་བ་དང་གསོད་པ་དང་། སྐྲོད་པ༌[^1480]དང་རེངས་པའོ། །

[Block 2220]
ཡང་ན་འཁོར་ལོ་དང་རིན་པོ་ཆེ་དང་པདྨ་དང་རལ་གྲི་དང་རྡོ་རྗེ་དང་རི་ལུ༌[^1481]དང་མིག་སྨན་དང་རྐང་མགྱོགས་ཏེ་བརྒྱད་དོ། །

[Block 2221]
ཕྲ་བ་ལ་སོགས་པ་ནི་གཟུགས་ཕྲ་བ་དང་རེག་པ་ཡང་བ་དང་ཁྱབ་པ་དང་ཡང་དག་པར་ཐོབ་པ་ཉིད་དང་རབ་ཏུ་སྣང་བ་ཉིད་དང་བརྟན་པ་དང་དབང་དུ་གྱུར་པ་དང་འདོད་དགུར་གྱུར་པའོ། །

[Block 2222]
[^1482]

[Block 2223]
ཡང་ན།

[Block 2224 [VERSE]]
སྐུ་ཡི༌[^1483]དབང་ཕྱུག་གསུང་དབང་ཕྱུག །
དེ་བཞིན་ཐུགས་ཀྱི་དབང་ཕྱུག་སྟེ། །
རྫུ་འཕྲུལ་ཡོན་ཏན་ཀུན་དབང་ཕྱུག །
བཟའ་བ་བྱེད་པ་ཡོན་ཏན་བརྒྱད། །

[Block 2225]
དེ་ལྟར་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་གཙོར་གྱུར་པ་ནི་དགོས༌[^1484]པའོ། །

[Block 2226]
གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་གཙོར་གྱུར་པ་ནི་དགོས་པའི་དགོས་པའོ། །

[Block 2227]
དགོས་པའི་ཚིག་གཅིག་གིས་གཉིས་ཀ་གཟུང་བ་སྟེ།

[Block 2228]
རྒྱུད་ཀྱི༌[^1485]རིགས་པ་ལས།

[Block 2229]
ཤིན་ཏུ༌[^1486]དང་བ་དེ་ནི་ཁྱི་དང་དཀར་པོ་འགྲོ་བ་ལ་ཡང་འཇུག་པ་བཞིན་ནོ། །

[Block 2230]
དེས་ན་དགོས་པ་དང་དེའི་ཡང་དགོས་པ་ཡང་དག་པར་བསྡུས་སོ། །

[Block 2231]
གླེང་བསླང་བ་ནི་འདས་ཟིན་ཏེ། ཞེས་བྱ་བ་འདིས་ཉེ་བར་སྡུད་པ༌[^1487]བསྟན་ཏོ། །

[Block 2232 [HEADING]]
#### གཉིས་པ། ^1-7-2-0

[Block 2233]
གཉིས་པ་ཞེས་པ་ལ་སོགས་པ་འདིས་གཉིས་པ་མདོར་བསྟན་པའོ། །

[Block 2234]
རྒྱུད་ཅེས་བྱ་བ་ལ་སོགས་པ་འདིས་རྒྱས་པར་བསྟན་པའོ། །

[Block 2235]
མི་ཡི་སྐྱེ་བར༌[^1488]འཁྲུངས་པ་ནི། ཞེས་བྱ་བ་ལ་སོགས་པས་སོ་སོར༌[^1489]བསྟན་པའོ། །

[Block 2236]
དེ་ལ་མདོ་སྡེ་དང་འདུལ་བ་དང་མངོན་པ་རྣམས་ཀྱི་རིགས་པ་ངེས་པར་བསྟན་ནས་སླར་ཡང་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོའི་སྒོ་ནས་སྟོན་པ་ཡིན་ཏེ། དེ་ལ་རེ་ཞིག་དང་པོ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་མིའི་སྐྱེ་བར་འཁྲུངས་པར་བསྟན་ཏེ། གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་ཤཱཀྱ་སེང་གེས་འགྲོ་བ་གདོན་པར་བྱ་བའི་ཕྱིར་རྗེས་སུ་མཐུན་པའི་མིའི་སྐྱེ་བར་འཁྲུངས་སོ། །

[Block 2237]
རིགས་པ་དེ་ཉིད་འཐད་པ་ཡིན་ཏེ་མི་འགལ་བའི་ཕྱིར་རོ། །

[Block 2238]
གང་གི་ཕྱིར་རིགས་མི་མཐུན་པ་རྣམས་ལ་དེའི་ལུས་ལ་སོགས་པ་དང་མཚུངས་པ་མ་ཡིན་ཏེ། བ་ལང་ལ་སོགས་པ་དང་བྱ་རྣམས་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2239]
དེ་བས་ན་མཚུངས་པ་ནི་རྒྱུད་ཡིན་ཏེ། རྒྱལ་རིགས་ཀྱི་སྐྱེས་བུ་ཆེན་པོའམ་བྲམ་ཟེའི་སྐྱེས་བུ་ཆེན་པོར་འཁྲུངས་པའོ། །

[Block 2240]
དེ་ཙམ་གྱིས༌[^1490]དོན་མི་འགྲུབ་པས་ཆགས་པ་དང་བྲལ་ཞིང་དབེན་པ་ལ་མ་བསྟེན་པའི་བར་དུ་མི་འགྲུབ་པས་བཙུན་མོའི་འཁོར་གྱི་ནང་ནས་ཞེས་སྨོས་ཏེ། བཅོམ་ལྡན་འདས་དེ་ཉིད་ཀྱིས་བཙུན་མོའི་འཁོར་གྱི་ནང་དུ་བཞུགས་པས་མཚན་ཕྱེད་ཀྱི་དུས༌[^1491]བཙུན་མོ་ཐམས་ཅད་གཉིད༌[^1492]ལོག་པས་དུར་ཁྲོད་འདི་ཉིད་ཡིན་ཞེས་མི་སྡུག་པའི་བསྒོམ་པ༌[^1493]མངོན་དུ་བྱས་ཏེ་དེའི་ཚེ་མཁའ་ལ་བྱོན་པའི་སངས་རྒྱས་ཀྱི་ཚོགས་འདོད་ཆགས་དང་བྲལ་བ་དག་རྒྱལ་པོའི་ཕོ་བྲང་གི་ནང་དུ་ཞུགས་པ་ལ་བལྟས་ཏེ། དེ་རྣམས་ཀྱིས༌[^1494]སྐུ་བསྟན་པ་མཐོང་ནས་སྐྱོ་བ་སྐྱེས་པར་གྱུར་པས་དེ་རྣམས་ཀྱི་ཆོས་གོས་ཀྱི་མཐའ་བཟུང་ཞིང་། བཅོམ་ལྡན་འདས་རང་སངས་རྒྱས་གང་གིས་བཞུད་པའི་ལམ་དེ་ཉིད་ནས་ངེས་པར་འབྱུང་བར་གྱུར་ཏོ། །

[Block 2241]
བྱུང་ནས་དགོན་པ་དབེན་པ་ལ་དྲང་སྲོང་དམ་པ་ལས་ཆགས་བྲལ་གྱི་ལམ་བླངས་ཏེ། རལ་གྲིས་དབུ་སྐྲ་བྲེགས་ཏེ་ཆོས་གོས་འཛིན་པར་གྱུར་ཏོ་ཞེས་བཙུན་མོའི་འཁོར་གྱི་ནང་ནས་ནི་ངེས་པར་བྱུང་བ་ནི་གླེང་གཞི་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་བའི་སྔོན་བྱུང་བའི་བཅས་གཞིའོ། །

[Block 2242]
དགོན་པར་གནས་པས་ཀྱང་གལ་ཏེ་འདོད་ཆགས་ལ་སོགས་པ་སྐྱེ་བར་གྱུར་ན། དེའི་ཚེ་ཁྱིམ་ནས་འབྱུང་བ་དོན་མེད་པར་འགྱུར་བས་དེའི་ཕྱིར་གསུམ་པ་ཡིན་ཏེ། འདུལ༌[^1495]ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་འདུལ་བ་ལས་བསྟན་པ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ནས་གསུངས་པའི་བསླབ་པའི་ཚིག་གི་ཚོགས་གང་ཡིན་པ་དེ་བཅོམ་ལྡན་འདས་ཀྱིས་བླངས་སོ། །

[Block 2243]
དེས་ནི་དོན་མཐུན་པ་བསྡུ་བའི་དངོས་པོ་བསྟན་ཏོ། །

[Block 2244]
གཞན་དུ་ན་སྡོམ་པ་མ་བླངས་པས་ཕ་རོལ་པོ་རྣམས་ལ་དེ་བསྟན་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 2245]
དེ་བས་ན་དེ་རིགས་པ་ཡིན་ཏེ། །སེམས་ཅན་གྱི༌[^1496]དོན་གྱི་ཡན་ལག་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
