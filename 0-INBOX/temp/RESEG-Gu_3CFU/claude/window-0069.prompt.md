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

[Block 2421]
རྐུན་པོ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་དུ་མ་ཉིད་ཡིན་ན་སོ་སོའི་སྐལ་བའི་ཆས་རྐུས་པ་ཐ་དད་དོ་ཞེས་སྦྱར་རོ། །

[Block 2422]
དེར་རྐུ་བ་པོ་གཅིག་ལ་ཆ་ཇི་ཙམ་པ་དེ་ཙམ་གྱི་རིན་ཐང་གིས་དེ་ལ་ལྟུང་བའོ། །

[Block 2423]
གཉིས་པ་ལ་ཇི་ཙམ་པ་དེ་ཙམ་པ་དེ༌[^1664]ལ་ལྟུང་བའོ། །

[Block 2424]
དེ་བཞིན་དུ་གསུམ་པ་ལ་སོགས་པ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2425]
སྦྱར་བར་བྱ་བ་དང་འབྲལ་བ་ཉིད་ལ་དུ་མ་ཡིན་ན་རྐུ་བ་པོ་རྣམས་ལ་ཡང་དུ་མ་ཉིད་ལ་བསྒྲུབ་པ་གཅིག་གོ། །

[Block 2426]
སྦྱར་བར་བྱ་བ་དང་དབྲལ་བ་གཅིག་ལ་ཆ་ཇི་ཙམ་པ་དེའི༌[^1665]རིན་ཐང་གིས་དེ་ལ་ལྟུང་བ་གཅིག་གོ། །

[Block 2427]
སྦྱར་བར་བྱ་བ་དང་དབྲལ་བར་བྱ་བའི་གཉིས་པའི་ཆ་གང་ཡིན་པ་དེའི་རིན་ཐང༌[^1666]

[Block 2428]
གཉིས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྟོགས་པར་བྱའོ། །

[Block 2429]
མདོ་འདི་དག་གི་གཞུང་ནི་ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གིས་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པ་བརྐུས་ན་ལྟུང་བ་མཐར་འགྱུར་རོ་ཞེས་གསུངས་པ་ལ། དགེ་སློང་ཤིན་ཏུ་མང་པོ་དག་གིས་བརྐུས་ན་མཐར་མི་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ། སྐྱེ་བོ་མང་པོ་ལ་བརྐུས་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2430]
དེ་བཞིན་དུ་སྐྱེ་བོ་མང་པོ་རྣམས་དང་ལྷན་ཅིག་ཏུ་རྐུ་ན་ཡང་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2431]
འདིར་སྐྱེ་བོ་མང་པོ་ཞེས་བྱ་བའི་ཚད་ནི་གཅིག་གི༌[^1667]ཆས་དངོས་པོ་ཚང་བར་མི་འགྱུར་བ་དེ་སྙེད་དུ་སྐྱེ་བོ་མང་པོ་དེ་ལ༌[^1668]དགོངས་ནས་ཉེས་པ་སྦོམ་པོའི་ཚིག་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2432]
འདི་ལ་བློ་གྲོས་དུ་མ་ཉིད་ཡིན་ན་ཐོབ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་ལ་རྐུན་པོ་རྣམས་དུ་མ་ཡིན་ན༌[^1669]རྫས་གང་ལ་མ་སྐྱེས་པ་ལ་བློ་གྲོས་གཅིག་པ་ནི་བཏུས་ནས་བྱེད་པ་ཉིད་དོ། །

[Block 2433]
བློ་གྲོས་ཐ་དད་པ་འབྱུང་ཞིང་རྐུན་པོ་མང་པོ་རྣམས་རྣམ་པར་བསྒྲུབ་པ་ཡིན་ཏེ། དེར་རྫས་དེ་ལ་ཐོབ་པ་ནི་བརྐུས་པ་སྟེ་སྤོས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2434]
གང་གི་ཚེ་འབྲེལ་བ་དང་བཅས་པ་ཉིད་ཀྱིས༌[^1670]ཐོབ་པའི་སྔ་རོལ་དུ་བདག་གིར་བྱེད་པ་ལ་འདིར་མི་སྐྱེད༌[^1671]པ་ཉིད་དོ། །

[Block 2435]
འདིར་གཞུང་ནི༌[^1672]བཙུན་པ་མུན་ཁྲོད་དུ་ཆོས་གོས་གཞག་པ་ལ་དགེ་སློང་བཞིས་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། བཀའ་སྩལ་པ། ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2436]
ལན་འགའ་མཐར་འགྱུར་ཏེ། གང་གི་ཚེ་ཆ་བཞིར་བྱས་པ་དེའི་ཆ་རེ་རེས་ཀྱང་དངོས་པོ་ཚང་ན་མཐའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2437]
མ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2438]
དེ་ལྟར་དངོས་པོ་དང་བདག་པོ་དང་རྗེས་སུ་བསྒྲུབ་པ་དང་། མཐར་ཐུག་པའི་སྐབས་དེ་རྣམས་ཀྱིས་མ་བྱིན་པར་ལེན་པའི་སྐབས་དག་གི་ཆོ་ག་རྣམ་པར་རིག་པར་བྱའོ། །

[Block 2439]
ཕམ་པར་འགྱུར་བ་གཉིས་པའི་ཞུ་བའི་སྐབས་སོ།། །།

[Block 2440]
བླང་བའི་སྔ་རོལ་དུ་ཤི་བ་ཉིད་དུ་གྱུར་ན་གཞག་པ་ཉིད་དོ་ཞེས་བྱ་བ་བློང་བར༌[^1673]བྱེད་པ་དེའི་བླང་བ་སྟེ་བཟུང་བའོ། །

[Block 2441]
རྣམ་པར་འབྱེད་པའི་དུས་ལ་སྔར་ཆ་བཟུང་བས་གལ་ཏེ་རབ་ཏུ་བྱུང་བ་ཤི་བ་ཉིད་དུ་གྱུར་ན་གང་ལས་ཆ་སྟེ༌[^1674]བླངས་པ་དེ་ཉིད་ལ་འདིའི་གཞག་པ་ཉིད་དེ། དེ་ཤི་བའི་ཡོ་བྱད་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2442]
བཟློག་པ་ན་ཤི་བའི་ཡོ་བྱད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཅི་སྟེ་ཤི་བ་ལས་སྔ་རོལ་དུ་རྫས་བླངས་པར་གྱུར་ན་དེའི་ཚེ་ཤི་བ་དང་འབྲེལ་པ་ཉིད་དོ། །

[Block 2443]
གང་ལས་གཟུང་བ་དེ་ལ་དེར་སོ་སོར་སྦྱིན་པར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ཏེ། ཤི་བའི་ཡོ་བྱད་ཉིད་ཁོ་ན་འདི་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2444]
དགེ་འདུན་ནི་ཕོ་ནུ་དང་འདྲ་བས་དེའི་ཆེད་དུ་རྐུ་བ་ནི་བདག་གིར་མི་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དཔེར་ན་ཕོ་ནུ་རྣམས་ནོར་གཅིག་པ་རྣམས་ལ་སོ་སོར་ཐམས་ཅད་དུ་ནོར་མ་བགོས་པས་བདག་གིར་བྱ་བའི་བློ་འབྱུང་བ་དེ་བཞིན་དུ་དགེ་སློང་རྣམས་ཀྱང་དགེ་འདུན་གྱིའོ། །

[Block 2445]
དེ་བས་ན༌[^1675]དགེ་འདུན་གྱི་དོན་དུ་རྐུ་བ་གང་ཡིན་པ་འདི་ནི་བདག་གིས༌[^1676]བྱ་བ་མིན་པ༌[^1677]མ་ཡིན་ནོ། །

[Block 2446]
ཕམ་པ་ཉིད་གཅིག་གིས་དགེ་འདུན་གྱི་ཆེད་དུ་མ་ཤ་ཀ་ལྔ་ཙམ་གྱི་དངོས་པོ༌[^1678]བརྐུས་པ་ལ་སོ་སོར་དགེ་སློང་རྣམས་ཀྱི་སྐལ་བ་ཚད་མ་ཡིན་པས་སྦོམ་པོའི་ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2447]
འདིར་གཞུང་ནི་དགེ་སློང་གཉུག་མར་གནས་པ་དགེ་འདུན་གྱི་ཞིང་རྨེད་དུ་འཇུག་པ་དེས་ཉེན་ཀོར་ན་ཁྱིམ་བདག་གི་ཞིང་འདུག་པ་ཡང་རྨེད་དུ་བཅུག་པ་དང་ཁྱིམ་བདག་འོངས་ཏེ་སྨྲས་པ། བཙུན་པ་ཅིའི་ཕྱིར་བདག་གི་ཞིང་རྨེད་དུ་བཅུག །སྨྲས་པ། འདི་ཁྱོད་ཀྱི་མ་ཡིན་གྱི་དགེ་འདུན་གྱི་ཞིང་ཡིན་ནོ། །

[Block 2448]
སྨྲས་པ། བཙུན་པ་ཁོ་བོས་མི་མ་ཡིན་པའི་ཆེ་བཞི༌[^1679]བསྟན་པར་བྱའོ། །

[Block 2449]
ཁྱིམ་བདག་དེ་རྣམས་ལ་ཡུལ་ཆོས་རྙིང་པས་མཚམས་སུ་ཕུར་པ་བཏབ་པ་དེ་བསྐོས༌[^1680]ནས་བསྟན་པ་དང་། དགེ་སློང་གིས་བརྐུས་པ་དང་ཕྲོགས་པ་ན་དེས་ཁྱིམ་བདག་དེ་སོང་བ་དང་ཕུར་པ་དེ་ནང་དུ་བསྣུར་ནས་ཞིང་དེ་རྨོས་པ་དང་ཁྱིམ་བདག་ཡང་འོངས་ཏེ་སྨྲས་པ། བཙུན་པ་ཁྱོད་ནི་ཁར་ཚང༌[^1681]ཕམ་པར་བྱས་ཏེ་ད་དུང་ཡང་ཅིའི་ཕྱིར་རྨེད་པར་བྱེད་དེ་འགྱོད་པ་སྐྱེས་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་དངོས་པོ་ཚང་ན་ཕམ་པའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2450]
འདིར་གལ་ཏེ་དངོས་པོ་ཚང་ན་ཞེས་བྱ་བའི་ཚིག་གིས་འདི་ལ་དེར་སྐལ་བ་གང་ཡིན་པ་དེ་ལས་ལྟུང་བ་འདིར༌[^1682]བསྐྱེད་པར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་ཏེ། མ་ཤ་ཀ་ལྔ་ཉིད་ཀྱི་ཕྱིར་སྦྱིན་པར་གྱུར་པའི་ཞིང་ལ་མི་རིགས་པའི་ཕྱིར་ཞེས་བྱའོ། །

[Block 2451]
ཏིལ་ཙམ་ལ་སོགས་པ་ལ་རིགས་པའི༌[^1683]ཕྱིར་དང་། ཚད་མེད་པ་ཉིད་ཀྱིས་ཀྱང་དགེ་སློང་རྣམས་ལ་ཡོངས་སུ་རྫོགས་པ་ཉིད་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་དངོས་གཞིའི་ཆོ་ག་ལ་རྣམ་པར་མི་འབྱེད་པ་ཉིད༌[^1684]ཀྱི་ཕྱིར་སྐལ་བ་རྣམ་པར་བཅད་པས་གནས་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2452]
བདག་པོ་ཐ་དད་པ་མ་ཡིན་པ་ནི་རང་གི་དང་འདྲའོ༌[^1685]ཞེས་བྱ་བ་ནི་གང་དང་འབྲེལ་བའི་རྫས་དེ་ཉིད་ལ་རྐུ་བ་གང་ཡིན་པ་དཔེར་ན་དགེ་འདུན་གྱི་ཡོ་བྱད་ལ་གནས་ནས་དགེ་འདུན་གྱི་དོན་ཉིད་དུ་སྤོ་བར་བྱེད་ཅིང་ཇི་ལྟར་རང་གི་དོན་འདི་ལྟ་བུ་འདི་རིག་པར་བྱའོ། །

[Block 2453]
དཔེར་ན་རང་གི་རྫས་རྐུ་སེམས་ཀྱིས་བླངས་ན་སྦོམ་པོར་འགྱུར་བ་དེ་བཞིན་དུ་འདིར་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2454]
འདིར་གཞུང་ནི་དགེ་སློང་གཉུག་མར་གནས་པས་ཕྱོགས་བཞིའི་དགེ་འདུན་གྱི་ཡོ་བྱད་རྐུ་སེམས་ཀྱིས་གནས་ནས་གནས་གཞན་དུ་སྤོས་པ་དང་དེ་འགྱོད་པ་སྐྱེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལྟུང་བ་ཕམ་པར་ནི་མི་འགྱུར་རོ། །

[Block 2455]
ཉེས་པ་སྡོམ་པོར༌[^1686]འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
