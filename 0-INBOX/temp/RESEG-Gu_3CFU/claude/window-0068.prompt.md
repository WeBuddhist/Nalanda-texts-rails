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
[Block 2381]
ནན་ཁུགས༌[^1639]ཀྱིས་རྐུ་བ་ལ་ནི་དབང་གིས་མནན་ཞིང༌[^1640]ལེན་པ་སྟེ། དེའི་ཕྱིར་དེ་བརྐུས་པ༌[^1641]མ་ཡིན་ནོ་སྙམ་དུ་དོགས་པ་འགའ་ཡང་ཡོད་ལ། གང་ཞིག་དང་ན་འཐེན་གྱིས་རྐུ་བ་ཡང་དེ་ནི་མི་སྟེར་བ་ཙམ་དུ་ཟད་ཀྱིས་བརྐུས་པ་ནི་མ་ཡིན་ནོ་སྙམ་དུ༌[^1642]དོགས་པ་ཡོད་པས་དེ་བས་ན་བརྐུས་པ་ཉིད་དུ༌[^1643]བཏགས་པ་མ་ཡིན་ནོ། །

[Block 2382]
དོགས་པ་དེ་གཉིས་བསལ་བའི་ཕྱིར་མདོ་འདི་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2383]
གནས་དང་བཅས་པ་དང༌[^1644]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྫས་གང་གནས་དང་ལྷན་ཅིག་ཏུ་བརྐུས་པ་དེ་ཡང་མ་བརྐུས་པ་མ་ཡིན་ཏེ༌[^1645]བརྐུས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2384]
རྫས་ཀྱི་གནས་ལས་མི་སེལ་བ་ཉིད་དུ་གང་དུ༌[^1646]གནས་ལ་སེལ་བར་བྱེད་པ་དེ་ནི་འདིར་གནས་དང་བཅས་པ་ལ་རྐུ་བར་རིག་པར་བྱའོ། །

[Block 2385]
འདིར་སྦྱོར་བ་དང་བྲལ་བ་ཉིད་ནི་དེ་གཉིས་ནི་དེ༌[^1647]ཉིད་དེ་གནས་དང༌[^1648]བཅས་པར་ཡང་བརྐུས་པ་ཉིད་ལ་བདག་པོ་ལ་རྫས་དང་སྦྱོར་བ་དྲལ་བ༌[^1649]ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2386]
འདིར་གཞུང་ནི་ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཡོ་བྱད་ལྕི་བ་གནས་ནས་སྤོ་བར་བྱེད་ན་མཐའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་བཀའ་སྩལ་ན། དགེ་སློང་གིས་ཡོ་བྱད་ལྕི་བ་གནས་ལས་མ་སྤོས་པར་བརྐུས་ན་མཐའི་ལྟུང་བར་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་གནས་གང་ན་འདུག་པ་དེ་གནས་དང་བཅས་ཏེ་བརྐུས་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2387]
བསད་པ་ཉིད་ནི་བརྐུས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བས་ན་འདི་ཙམ་གྱིས་བརྐུས་པ་ཉིད་དུ་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2388]
འདིར་གནས་ནས་སྤོས་པ་ཉིད་བསད་པ་དང་ལྷན་ཅིག་ཏུ་འགྱུར་བའམ༌[^1650]ཕྱིས་བརྐུས་པ་ཞེས་བྱ་བར་གྲུབ་པའོ། །

[Block 2389]
ཕྱོགས་གཅིག་ཏུ་གནས་ནས་མ་འཕགས་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་གང་ཞིག་ལ་གནས་ནས་སྤོ་བར་གྱུར་པ་ལ་རྫས་རྒྱུད་གཅིག་ལ་ཕྱོགས་འགའ་ཞིག་གནས་དོར་བར་གྱུར་ཏེ་གཞན་ཅུང་ཟད་ཀྱང་མ་གྲོལ་བ་ནི་མི༌[^1651]འདོར་བ་དེ་ལ་འདི་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2390]
ཐམས་ཅད་ཀྱིས་དོར་བ་ལ་བྱས་པ༌[^1652]ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2391]
ལྟུང་བ་ནི་དེ་ལས་ཁྱེར་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་རྣམས་ལ་དེས་ལྟུང་བས་ཏེ། སྔོན་དུ་འདེགས་པ་ལ་རང་གི་གནས་ནས་ཕྱུང་བ་ལ་ལྟུང་བ་དེ་ཉིད་རྐུ་བའོ། །

[Block 2392]
དེར་འོག་ཏུ་སའམ་གོས་ལ་སོགས་པ་གང་ཡིན་པ་དེ་ནི་མཆོག་གི་བརྩེགས༌[^1653]མ་ཐོབ་པའི་བདག་ཉིད་ཅན་གྱི་ལྟུང་བ་ནི་འདིར་བརྐུས་པར་རིག་པར་བྱའོ། །

[Block 2393]
འདིར་ཡུལ་དུ་ཐོབ་པར་བྱེད་པའི་བློ་ཡང་དག་པར་གནས་ཏེ་བསྡུས་པའི་བློ་ནི་མ་ཡིན་ནོ། །

[Block 2394]
ཇི་ལྟར་བསྡུས་ཏེ་གཞག་པ་ལ་དེ་བས་ན་འདིར་བརྐུས་པ་ཉིད་དུ་ཤེས་པའོ། །

[Block 2395]
འདིར་མངོན་པར་འདོད་པས་ཡུལ་གྱི་རྣམ་པར་གཞག་པའོ། །

[Block 2396]
གང་དུ་རྟེན་པ༌[^1654]ཉིད་ཀྱིས་འགྲོ་བར་བྱ་བ་མ་ཡིན་པའམ། འགྲོ་བར་བྱ་བ་མངོན་པར་འདོད་པ་དེ་འདིར་ཡུལ་ལོ། །

[Block 2397]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་ཤིང་ཐོག་རྣམས་སྤྲུགས་ཏེ་ལྷུང་བར་བྱས་ནས་བརྐུས་ན་ལྟུང་བ་ཅིར་འགྱུར། གལ་ཏེ་སྦྱོར་བ་གཅིག་གིས་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པ་ཚང་ན་མཐར་འགྱུར་རོ། །

[Block 2398]
ཅི་སྟེ་མ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2399]
འཛག་པ་དང་འབྲུལ་བར་བྱེད་པའི་བུ་གུ་ལས་ནི་བྱུང་ནའོ་ཞེས་བྱ་བ་ལ། འཛག་པར་བྱེད་པའི་བུ་གུ་ཞེས་བྱ་བ་ནི་དཔེར་ན་ཆུ་ཀླུང་ལ་སོགས་པའོ། །

[Block 2400]
ལག་པས་བྱས་པ་དང་རྐང་པས་བྱས་པ་ནི་དཔེར་ན་གཞིའི་ཆོས་ཅན་རྫོགས་པའི་བང་མཛོད་ལ་སོགས་པ་ལ་བུ་ག་ནི་དེ་བསལ་བ་མ་ཡིན་པ་ལ་ངེས་པར་བྱུང་ནའོ། །

[Block 2401]
དེ་བས་ན་ཆུ་ཀླུང་དང་བང་མཛོད་ལ་སོགས་པ་ལ་རྐུ་བའོ། །

[Block 2402]
འདིར་ཐ་མ་དེ་ཚུན་ཆད་རྫས་གཅིག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ནི་བྱུང་བ་ཐ་མ་ལས་ཇི་སྲིད་དུ༌[^1655]བུ་ག་ལ༌[^1656]རྫས་ཐམས་ཅད་གཅིག་པ་ཉིད་དེ། དེ་ཐམས་ཅད་ཀྱི་རིན་ཐང་གིས་ལྟུང་བ་ལ༌[^1657]རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2403]
གང་ལ་ལོ་ཐོག་བསྐྱེད་པ་ལ་སོགས་པའི་དགོས་པ་ལ་རྩེ་གཅིག་པ་ཉིད་མ་བརྟེན་པར་ཆུ་རྐུ་བ་ལ་སོགས་པ་དེའི་དོན་དུ་ཆུ་འདི་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 2404]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^1658]འབབ་ཆུ་བཅད་ནས་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཆུའི་ཕུང་པོ་དང་པོ་ནས་བཟུང་སྟེ། ཇི་སྲིད་ཐ་མའི་བར་གྱི་ཆུའི་རིན་ཐང་བརྩི་བར་བྱ་སྟེ། དངོས་པོ་ཚང་ན་ནི་མཐའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2405]
དངོས་པོ་མ་ཚང་ན་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2406]
བཙུན་པ་དགེ་སློང་གིས་བང་བ་བརྟོལ་ཏེ། འབྲུ་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། སྦྱོར་བ་གཅིག་གིས་རྐུ་བ་ཉིད་ཚུན་ཆད་ཀྱི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2407]
འདིར་འབུགས་པ་ཉིད་སྦྱོར་བ་སྟེ། གཞན་མེད་པའི་ཕྱིར་དེས་བུག་པ་བྱས་ལ་ཇི་སྲིད་རང་ཉིད་འབྱུང་བ་དེ་སྲིད་དེར༌[^1659]སྦྱོར་བ་གཅིག་བྱས་པ་བརྗོད་པར་རྣམ་པར་གནས་སོ། །

[Block 2408]
ཕུང་པོ་ལས་རྐུ་ན་ནི་ལེན་རེ་རེ༌[^1660]ཞིང་བླངས་པ་ཐ་དད་དོ་ཞེས་བྱ་བ་ནི་བླངས་པ་རེ་རེ་ཕུང་པོ་ལ་རྐུ་ན་ཐ་དད་པའོ། །

[Block 2409]
བསྡུས་པ་ལས་སེལ་བ་འདི་འདིར་བསྡུས་པ་ལས༌[^1661]ལ་ཡང་དག་པར་གནས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2410]
བཏུས་པ་བཞིན་དུ་ནི་འདིར་རྣམ་པར་གཞག་པ་མ་ཡིན་ནོ། །

[Block 2411]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་འབྲུའི་ཕུང་པོ་ལས་བཅད་དེ་འབྲུ་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། རིན་ཐང་བརྩི་བར་བྱ་སྟེ། གལ་ཏེ་སྦྱོར་བ་གཅིག་གིས་དངོས་པོ་ཚང་ན་ནི་མཐའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2412]
གལ་ཏེ་མ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2413]
དབྲལ་བར་བྱ་བ་དུ་མ་ཉིད་ཡིན་ན་དེའི་ཆ་སོ་སོའི༌[^1662]ཞེས་བྱ་བ་ནི༌[^1663]བརྐུས་པ་ཐ་དད་དོ་ཞེས་སྦྱར་རོ། །

[Block 2414]
དེ་རྣམས་ནི་སྦྱར་བ་དང་རྣམ་པར་དབྲལ་བར་བྱ་སྟེ། གང་རྣམས་ཀྱི་རྫས་རྐུ་བ་དེ་རྣམས་དུ་མ་ཉིད་ལ་རེ་རེའི་ཆ་གང་ཡིན་པ་རེ་རེའོ། །

[Block 2415]
དེའི་དོན་དུ་རྐུ་བ་ཐ་དད་པའོ། །

[Block 2416]
བརྐུ་བར་བྱ་བའི་རྫས་ཀྱི་བདག་པོ་གཅིག་ལ་དེའི་ཆ་གང་ཡིན་པ་དེའི་རིན་ཐང་གང་གིས་ལྟུང་བ་གཅིག་གོ། །

[Block 2417]
གཉིས་པ་ལ་གང་ཞིག་དེའི་རིན་ཐང་གིས་གཞན་ནོ། །

[Block 2418]
གསུམ་པ་ལ་གང་ཞིག་དེའི་རིན་ཐང་གིས་གཞན་ནོ། །

[Block 2419]
དེ་ལྟར་ན་དེ་བཞིན་དུ་བཞི་པ་ལ་སོགས་པ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2420]
སྦྱར་བ་དང་དབྲལ་བར་བྱ་བ་སོ་སོ་ལ་འདི་ལ་རིན་ཐང་ཚང་བ་ནི་གང་གི་ངོ་བོ་གཞན་དང་གཞན་ཞེས་བྱ་བ་འདི་འདིའི་ཤེས་པའོ། །
--- END BLOCKS ---
