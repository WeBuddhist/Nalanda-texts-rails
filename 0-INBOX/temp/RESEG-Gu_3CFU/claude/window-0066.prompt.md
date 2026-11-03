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
འདི་གཉིས་ཀ་ཡང་ཐ་མི་དད་པར་བསྐྱིས་པ་ཞིག༌[^1594]བྱ་བ་བརྣོགས་པ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 2312]
འདིས་ནི་འདིར་བརྐུ་བའམ༌[^1595]འོན་ཏེ་མ་ཡིན་སྙམ་དུ་ཡིད་གཉིས་ཟ་བར་གྱུར་པ་དེའི་ཚེ་ན་གང་ཞིག་གནས་ལ་འཕོ་བ་དེར་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2313]
དངོས་པོ་ཡོངས་སུ་རྫོགས་པ་དེ་ལ་ཕམ་པ་མི་བསྐྱེད་ཅེས་བྱ་བ་འདི་ཐལ་བར་རིག་པར་བྱའོ། །

[Block 2314]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་བསྙོན་པར་བྱས་ནས་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། གཡར་ནས་བསྙོན་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2315]
དེ་གཉིས་ལན་འགའ་མཐར་འགྱུར་བ་ཡང༌[^1596]ཡོད་དེ་གང་གི་ཚེ་བརྣོགས་པ་ནའོ། །

[Block 2316]
དགེ་སློང་གི་ཐད་དུ་གཞན་གྱིས་གཏམས་ཏེ་གཞག་པ་དེ་ལེན་པའི་ཚེ་བསྙོན་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2317]
ལན་འགའ་ནི་མཐར་འགྱུར་ཏེ། གང་གི་ཚེ་བརྣོགས་པ་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2318]
གཏམས་པ་སྦས་པ་ལ་གལ་ཏེ་སྤོ་བ་དང་ལྷན་ཅིག་ཏུ་དང་། སྤོས་པའི་འོག་ཏུ་དང་། གལ་ཏེ་སྔར་ན་ནི་སྦྱོར་བ་གཞན་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཏམས་པ་ཡང༌[^1597]བ་གང་ཡིན་པ་གང་ཞིག་གཞག་པ་གནས་གང་དུ་གལ་ཏེ་སྤོ་བས་གནས་པ་དང་། ལྷན་ཅིག་ཏུ་བརྣོགས་ན་ཕྱིར་སྤོ་བའི་འོག་ཏུ་དེ་ལས་བརྣོགས་པ་ཉིད་ནི་བརྐུས་པ་ཉིད་ཡིན་ནོ། །

[Block 2319]
འོན་ཏེ་སྤོ་བ་ལས་སྔ་རོལ་དུ་བརྣོགས་ན་གཞན་དུ་བསྙོན་པ་ནི་སྦྱོར་བ་སྟེ་དངོས་གཞིའི༌[^1598]རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2320]
བསྙོན་པ་ཡོད་ཀྱང་གང༌[^1599]དུ་ཆད་པ་ཉིད་ཀྱིས་བརྣོགས་ན་སྦྱོར་བ་མ་ཡིན་པ་ཉིད་དུ་རྟོགས་པར་མི་བྱའོ། །

[Block 2321]
བརྣོགས་པ་ལ་བརྣོགས་པའི་སྔ་རོལ་དུ་བསྙོན་པ་ལ་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 2322]
དེ་བས་ན་སྦྱོར་བ་ཉིད་དོ། །

[Block 2323]
བརྣོགས༌[^1600]པ་དང་བསྙོན་པའོ། །

[Block 2324]
འདིར་སྦས་པ་ནི་བརྐུས་པའོ། །

[Block 2325]
འདིར་གཞུང་ནི་དགེ་སློང་གི་ཐད་དུ་གཞན་གྱིས་གཏམས༌[^1601]ཏེ་གཞག་པ་དེ་ལེན་པའི་ཚེ་བསྙོན་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2326]
ལན་འགའ་ནི་མཐར་འགྱུར་ཏེ་གང་གི་ཚེ་བརྣོགས་པར་བྱེད་ཅིང་དངོས་པོ་ཚང་ན་ནི་མཐར་འགྱུར་རོ། །

[Block 2327]
གལ་ཏེ་མ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2328]
སྔར་བརྣོགས་པར་བྱེད་ཅིང་ཕྱིས་གནས་ནས་སྤོ་བར་བྱེད་ན་བརྣོགས་པའི་ཚེ་ཉིད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2329]
ཅི་སྟེ་སྔར་གནས་ནས་སྤོ་བར་བྱེད་ཅིང་དངོས༌[^1602]པོ་ཚང་ན་མཐར་འགྱུར་རོ། །

[Block 2330]
དངོས་པོ་མ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2331]
སྒྱིད་པ་གཅོད་པ་དང་གསོད་པ་ནི་ཆུད་གཟོན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གླང་པོ་ཆེ་དང་རྟ་དང་རྔ་མོ་དང་བ་ལང་དང་བསེ་ལ་སོགས་པ་རྣམས་ལ་ཕན་པར༌[^1603]མ་གྱུར་ཅིག་ཅེས་ཚུལ་གཅོད་པ་དང་། གསོད་པ་ནི་སྦེད་པའོ། །

[Block 2332]
ཆུད་གཟན་པ་ཞེས་བྱ་བ་འདི་ལ་ཆུད་གཟན་པའི་ཚིག་གི༌[^1604]ཁོངས་སུ་བསྡུ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2333]
འདིར་སྒྱིད་པ་གཅོད་པ་ནི་དཔེ་ཡིན་ཏེ་རྣམ་པར་འཚེ་བ་གཞན་དག་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 2334]
འདིར་གཞུང་ནི་ཅི་སྟེ་ཕན་པར༌[^1605]མ་གྱུར་ཅིག་ཅེས་གསོད་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2335]
ཅི་སྟེ་ཕན་པར༌[^1606]མ་གྱུར་ཅིག་ཅེས་སྒྱིད་པ་གཅོད་པར་བྱེད་ན་ཡང་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2336]
མཚམས་ཀྱི་ནམ་མཁའ་ལས་ཤོ་གམ་འདྲལ་བར་བྱེད་ན་ཡང་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཚམས་དང་འབྲེལ་བའི་ནམ་མཁའ་གང་ཡིན་པ་དེ་ལ་ཤོ་གམ་འདྲལ་བའི་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 2337]
གང་གིས༌[^1607]མཚམས་ཀྱི་ཁོངས་སུ་བསྡུས་པའི་ས་ལ་གནས་པ་ལུས་ཀྱིས༌[^1608]བརྩལ་བ་མཚོན་ཆ་འཕངས་པ་ལ་སོགས་པས་སམ། ངག་གིས༌[^1609]བརྩལ་བ་གསང་སྔགས་ཀྱི་བཟླས་བརྗོད༌[^1610]ལ་སོགས་པས་སམ། ཡིད་ཀྱིས༌[^1611]བརྩལ་བ་རྫུ་འཕྲུལ་མངོན་པར་འདུ་བྱེད༌[^1612]པ་ལ་སོགས་པ་ཤོ་གམ་གྱི་བྱ་བ་མ་ཆགས་པར་གྱུར་པ་ལུས་དང་འབྲེལ་བའི་ནམ་མཁའ་འགའ་ཞིག་ལ་ཤོ་གམ་གྱིས་འདའ་བར་བྱེད་ན་དེར་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའི་དངོས་པོར་ཚང་བ་ལ་ཡང་ཉེས་པ་སྦོམ་པོ་ཡིན་ནོ། །

[Block 2338]
གང་གི་ཚེ་དགེ་སློང་ནམ་མཁའ་ལ་གནས་པ་དང་ཕྱི་རོལ་གྱི་མཚམས་ཀྱི་ས་ལ་གནས་པ་ལ་ནི་དེར་ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིར་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 2339]
རྒྱལ་པོ་དག་ནི་ས་ལ་དབང་བ་ཡིན་གྱི། ནམ་མཁའ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2340]
དེ་བས་ན་དགོངས་པ༌[^1613]མེད་པ་ལ་ས་ལ་སྐྱོན་མེད་པ་ཉིད་དུ་རྣམ་པར་གཞག་གོ། །

[Block 2341]
རྫུ་འཕྲུལ་གྱིས༌[^1614]ཁྱེར་བ་ལ་ནི་ཉེས་པ་མེད་པ༌[^1615]ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདི་ནི་ཤོ་གམ་དྲལ་བ་ལ་གནས་པ་ཉིད་དེ་གསང་སྔགས་དང་སྨན་གྱིས་བྱས་པ་དང་ཡང་འདིར་ལས་ལས་སྐྱེས་པའི་རྫུ་འཕྲུལ་གྱི་མངོན་པར་ཤེས་པ་ཡང་འདི་ལྟར་མངོན་པར༌[^1616]ཤེས་པ་མེད་པར་ཞིང་ཉིད་མ་ཡིན་པའི་ཕྱིར་ཡིད་མི་ཆེས་པའི་སེམས་དང་ལྡན་པ་ལ་ཐམས་ཅད་དུ་ལྟུང་བ་མེད་དོ། །

[Block 2342]
གསང་སྔགས་དང་སྨན་གྱི་ལས་ཀྱིས༌[^1617]སྐྱེས་པ་གང་ཞིག་ལ། མཚམས་ཀྱི་ཁོངས་སུ་གཏོགས་པའི་ས་ལ་གནས་པའི་ཁྱེར་བ་པོ་ལ་དགོས་པ་མེད་པ་དེ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2343]
མཚམས་ཀྱི་ཁོངས་སུ་གཏོགས་པའི་ས་ལ་གནས་པའི་ཁྱེར་བ་པོ་ལ་སྦོམ་པོ་ཉིད་དོ། །

[Block 2344]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་ནམ་མཁའ་ལས་ཤོ་གམ་འདྲལ་བར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། གལ་ཏེ་རྫུ་འཕྲུལ་གྱིས༌[^1618]འདྲལ་བར་བྱེད་ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2345]
ཅི་སྟེ་རྣམ་པ་གཞན་དག་གིས་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2346]
མཚམས་གཞན་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་པ་ཉིད་དོ། །

[Block 2347]
ཤོ་གམ་དྲལ་བ་ན་ཡང་ཞེས་བྱ་བ་དང་རྗེས་སུ་སྦྱར་རོ། །

[Block 2348]
མཚམས་གཞན་དུ་ཞེས་བྱ་བ༌[^1619]ཤོ་གམ་གྱི་བྱ་བ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2349]
ཤོ་གམ་གྱི་གནས་ནས་ཐོབ་པའི་སྤོང་བའི་བདག་ཉིད་ཅན་དྲལ་བའི༌[^1620]བསམ་པ་མེད་པ་ལ་རྐུ་བའི་སེམས་ཞེས་བྱ་བ་འདི་ལ་འདི་བརྗོད་པའོ། །

[Block 2350]
བསྒོ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཤོ་གམ་དྲལ་ན་ཞེས་བྱ་བར་སྦྱར་ཏེ། ས་གང་ཞིག་ལ་ཤོ་གམ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དེས་མི་འགྲོ་བ་ལ་ཐད་ཀར་དེ་ལས་འདའ་བར་བྱེད་པའམ་སོ་སོར་བཟློག་པ་ལ་ས་མ་ཐོབ་པ་ཉིད་ལ་གཞན་གྱིས་འགྲོ་བའམ་བཟློག་པ་ཞེས་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
