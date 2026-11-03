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
[Block 2311]
དེ་ལྟ་མ་ཡིན་ན་ཕྱིས་བདེ་བའི་བློ་ཇེ་མང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། ངལ་བའི་སྤྱོད་ལམ་གྱི་རྣམ་པ་དག་ལ་ཡང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 2312]
གལ་ཏེ་དང་པོ་ནས་རྩོམ་པ་ཞིག་མེད་ན་མཇུག་ཏུ་སྡུག་བསྔལ་གྱི་བློར་ག་ལ་འགྱུར་ཞེ་ན། ལུས་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་ཏེ། ཆང་ལ་སོགས་པ་མངར་བ་ལ༌[^1701]མཇུག་ཏུ་སྐྱུར་པོར་འགྱུར་བ་བཞིན་ནོ། །

[Block 2313]
དེ་ལྟ་བས་ན་བདེ་བའི་ཚོར་བ་ཡོད་པ་ཁོ་ནའོ་ཞེས་བྱ་བ་ཡང་གྲུབ་ལ། སྡུག་བསྔལ་ཉིད་གསུམ་དང་ལྡན་པའི་ཕྱིར་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བ་ཡང་གྲུབ་པ་ཡིན་ནོ། །

[Block 2314 [HEADING]]
##### ཀུན་འབྱུང་གི་བདེན་པ། ^3-1-2-6-0

[Block 2315]
ཀུན་འབྱུང་གི་བདེན་པ་གང་ཡིན་པ་དེ་ཉིད་སྡུག་བསྔལ་གྱི་བདེན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་མདོ་ལས་ཐལ་བ་ཡིན་ཏེ། མདོ་ལས་ནི་སྲེད་པ་ཁོ་ན་ཡིན་པར་བཤད་དོ། །

[Block 2316]
དེ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་མདོ་ལས་བཤད་ཀྱི་གཞན་དག་ཀྱང་ཀུན་འབྱུང་ནི་ཡིན་ནོ། །

[Block 2317]
འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་པར་བྱ་ཞེ་ན། གཞན་ལས་གཞན་ཡང་ཡིན་པར་གསུངས་པའི་ཕྱིར་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 2318 [VERSE]]
ལས་དང་སྲིད་པ༌[^1702]དང་ནི་མ་རིག་པ། །
ཕྱི་མའི་ཚེ་ལ་འདུ་བྱེད་རྣམས་ཀྱི་རྒྱུ། །

[Block 2319]
ཞེས་གསུངས་ལ་ཡང་ས་བོན་གྱི་རྣམ་པ་ལྔ་ཞེས་བྱ་བ། འདི་ནི་ཉེ་བར་ལེན་པ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པའི་ཚིག་བླ་དགས་ཡིན་ནོ། །

[Block 2320]
སའི་ཁམས་ཞེས་བྱ་བ་འདི་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བཞིའི་ཚིག་བླ་དགས་ཡིན་ནོ་ཞེས་ཀྱང་གསུངས་ཏེ། དེ་ལྟ་བས་ན་མདོ་ལས་བསྟན་པ་ནི་དགོངས་པ་ཅན་ཡིན་ལ། ཆོས་མངོན་པ་ལས་བསྟན་པ་ནི་མཚན་ཉིད་པ་ཡིན་ནོ། །

[Block 2321]
གཞན་ཡང་མངོན་པར་འགྲུབ་པའི་རྒྱུ་བཀའ་སྩོལ་པ་ན་ནི་ཀུན་འབྱུང་གི་བདེན་པ་སྲེད་པ་ཁོ་ན་ཡིན་པར་གསུངས་ལ། སྐྱེ་བ་དང་མངོན་པར་འགྲུབ་པའི་རྒྱུ།

[Block 2322]
རྒྱུ་དང་བཅས་པར་བཀའ་སྩོལ་པ་ན་ནི་ཚིགས་སུ་བཅད་པ་ལས།

[Block 2323]
ལས་དང་སྲེད་པ་དང་མ་རིག་པ་ཡིན་པར་གསུངས་ཏེ།

[Block 2324]
མདོ་ལས།

[Block 2325]
ལས་ནི་སྐྱེ་བའི་རྒྱུ་ཡིན་ལ། སྲིད་པ་ནི་མངོན་པར་འགྲུབ་པའི་རྒྱུ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2326]
ཡང་ན་མདོ་ལས་རྒྱུ་དང་བཅས། རྐྱེན་དང་བཅས། གཞི་དང་བཅས་ཞེས་འབྱུང་བའི་རིམ་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 2327]
ས་བོན་དང་ཞིང་གི་དངོས་པོར་སྟོན་པར་མཛད་པས་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ལ༌[^1703]ཡང་གསུངས་སོ། །

[Block 2328]
སྐྱེ་བ་ནི་གང་ཡིན། མངོན་པར་འགྲུབ་པ་ནི་གང་ཡིན་ཞེ་ན། ཁམས་དང་འགྲོ་བ་དང་སྐྱེ་གནས་ལ་སོགས༌[^1704]པའི་བྱེ་བྲག་གིས༌[^1705]ལུས་སྐྱེ་བ་ནི་སྐྱེ་བ་ཡིན་ལ། བྱེ་བྲག་མེད་པར་ཡང་སྲིད་པར་ཉིང་མཚམས་སྦྱོར་བ་ནི་མངོན་པར་འགྲུབ་པ་ཡིན་ནོ། །

[Block 2329]
དེ་གཉིས་ཀྱི་རྒྱུ་ནི་གོ་རིམས་བཞིན་དུ་ལས་དང་སྲེད་པ་ཡིན་ཏེ། དཔེར་ན་ས་བོན་སཱ་ལུ་དང་ནས་ལ་སོགས་པའི་རིགས་ཀྱི་བྱེ་བྲག་གིས་མྱུ་གུ་སྐྱེ་བའི་རྒྱུ་ཡིན་ལ། ཆུ་ནི་བྱེ་བྲག་མེད་པར་མྱུ་གུ་ཐམས་ཅད་སྐྱེ་བ་ཙམ་གྱི་རྒྱུ་ཡིན་པ་ལྟ་བུ་སྟེ་འདི་ནི་དཔེ་ཡིན་ནོ། །

[Block 2330]
མངོན་པར་གྲུབ་པའི༌[^1706]རྒྱུ་སྲེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་རིགས་པ་ཅི་ཞིག་ཡོད་ཅེ་ན། སྲེད་པ་དང་བྲལ་བ་སྐྱེ་བ་མེད་པའི་ཕྱིར་ཏེ། སྲེད་པ་དང་བཅས་པ་དང་སྲེད་པ་དང་བྲལ་བ་གཉི་ག་ཡང་འཆི་བ་ལས་སྲེད་པ༌[^1707]དག་ཁོ་ན་སྐྱེ་བར་སྣང་གི་སྲེད་པ་དང་བྲལ་བ་རྣམས་ནི་མ་ཡིན་པས་སྲེད་པ་མེད་ན་སྐྱེ་བ་མེད་པའི་ཕྱིར་སྲེད་པ༌[^1708]མངོན་པར་འགྲུབ་པར་བྱ་བ་ལ་སྲེད་པ་རྒྱུ་ཡིན་པར་ཤེས་སོ། །

[Block 2331]
རྒྱུད་གཞོལ་བའི་ཡང་ཕྱིར་ཏེ། གང་ལ་སྲེད་པ་དང་བཅས་པ་དེར་སེམས་ཀྱི་རྒྱུད་ཡང་དང་ཡང་དུ་གཞོལ་བར་མཐོང་བས། དེ་ལྟ་བས་ན་ཡང་སྲེད༌[^1709]པ་ལ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བར་ཤེས་སོ། །

[Block 2332]
ཇི་ལྟར་སྲེད་པས་འདག་པའི་ཆ་ལ་སྲན་ཆུང་གི་ཕྱེ་མའི་ལྡེ་གུ་བསྐམས་པས་ལུས་བཟུང་བ་བཞིན་དུ་ལུས། ཀུན་དུ་བཟུང་བ་དེ་ལྟར་ནི་གང་གིས་ཀྱང་ལུས་ཀུན་དུ་མ་བཟུང་སྟེ། རྒྱུ་གཞན་ནི་ཇི་ལྟར་བདག་ལ་ཆགས་པ་དེ་ལྟར་རྗེས་སུ་འབྲེལ་བ་མ་ཡིན་ཏེ། འདི་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 2333 [HEADING]]
##### བདེན་པ་གཉིས། ^3-1-2-7-0

[Block 2334]
བཅོམ་ལྡན་འདས་ཀྱིས་བདེན་པ་བཞི་ཞེས་ཀྱང་གསུངས།

[Block 2335]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་དང་། དོན་དམ་པའི་བདེན་པ་དང་བདེན་པ༌[^1710]གཉིས་ཞེས་ཀྱང་གསུངས་ལ།

[Block 2336 [VERSE]]
[^1711] དེ་གཉིས་ཀྱི་མཚན་ཉིད་ཅི་ཞེ་ན། །
གང་ལ་བཅོམ་དང་བློ་ཡིས་གཞན། །
བསལ་ན་དེ་བློ་མི་འཇུག་པ། །
བུམ་ཆུ་བཞིན་དུ་ཀུན་རྫོབ་ཏུ། །

[Block 2337]
ཡོད་དེ་དོན་དམ་ཡོད་གཞན་ནོ། །

[Block 2338 [HEADING]]
###### ཀུན་རྫོབ་ཀྱི་བདེན་པ། ^3-1-2-7-1-0

[Block 2339]
གང་ལ་ཆ་ཤས་སུ་བཅོམ་ན་དེའི་བློ་མི་འཇུག་པ་དེ་ནི་ཀུན་རྫོབ་ཏུ་ཡོད་པ་སྟེ། དཔེར་ན་བུམ་པ་ལྟ་བུའོ། །

[Block 2340]
དེ་ལ་ནི་གྱོ་མོར་བཅོམ་ན་བུམ་པའི་བློ་མི་འཇུག་གོ། །

[Block 2341]
གང་ལ་བློས་ཆོས་གཞན་བསལ་ན་དེའི་བློ་མི་འཇུག་པ་དེ་ཡང་ཀུན་རྫོབ་ཏུ་ཡོད་པ་ཡིན་པར་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ། དཔེར་ན་ཆུ་ལྟ་བུའོ། །

[Block 2342]
དེ་ལ་ནི་བློས་གཟུགས་ལ་སོགས་པའི་ཆོས་བསལ་ན། ཆུའི་བློ་མི་འཇུག་གོ། །

[Block 2343]
དེ་དག་ཁོ་ན་ལ་ཀུན་རྫོབ་ཏུ་དེའི་མིང་དུ་བཏགས་པ་ཡིན་པས་ཀུན་རྫོབ་ཀྱི་དབང་གིས་བུམ་པ་དང་ཆུ་ཡོད་དོ་ཞེས་བརྗོད་པ་ནི༌[^1712]བདེན་པ་ཁོ་ན་སྨྲས་པ་ཡིན་གྱི། བརྫུན་པ་ནི་མ་ཡིན་པས་དེ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡིན་ནོ། །

[Block 2344 [HEADING]]
###### དོན་དམ་པའི་བདེན་པ། ^3-1-2-7-2-0

[Block 2345]
དེ་ལས་གཞན་པ་ནི་དོན་དམ་པའི་བདེན་པ་སྟེ། གང་ལ་བཅོམ་ཡང་དེའི་བློ་འཇུག་པ་ཁོ་ན་ཡིན་ལ། བློས་ཆོས་གཞན་བསལ་ཡང་དེའི་བློ་འཇུག་པ་དེ་ནི༌[^1713]དོན་དམ་པར་ཡོད་པ་ཡིན་ཏེ། དཔེར་ན་གཟུགས་ལྟ་བུའོ། །

[Block 2346]
དེ་ལ༌[^1714]རྡུལ་ཕྲ་བར་ཏུ་བཅོམ་ཡང་རུང་། བློས་རོ་ལ་སོགས་པའི་ཆོས་བསལ་ཀྱང་རུང་གཟུགས་ཀྱི་རང་བཞིན་གྱི་བློ་འཇུག་པ་ཉིད་དེ། ཚོར་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2347]
དེ་ནི་དོན་དམ་པར་ཡོད་པའི་ཕྱིར་དོན་དམ་པའི་བདེན་པ་ཞེས་བྱའོ། །

[Block 2348]
སྔོན་གྱི་སློབ་དཔོན་རྣམས༌[^1715]ན་རེ། ཇི་ལྟར་འཇིག་རྟེན་ལས་འདས་པའི་ཤེས་པའམ། དེའི་རྗེས་ལ་ཐོབ་པ་འཇིག་རྟེན་པས་འཛིན་པ་དེ་ལྟར་ནི་དོན་དམ་པའི་བདེན་པ་ཡིན་ནོ། །

[Block 2349]
ཇི་ལྟར་གཞན་གྱིས་འཛིན་པ་དེ་ལྟར་ནི༌[^1716]ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2350]
བདེན་པ་རྣམས་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
