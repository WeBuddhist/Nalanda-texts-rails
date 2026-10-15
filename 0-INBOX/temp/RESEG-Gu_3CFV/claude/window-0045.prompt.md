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
[Block 1576]
དེ་བཞིན་དུ་ཚོན་སྣ༌[^984]ལྔའི་སྔགས་སྐུད་གདགས་པར་མི་བྱའོ། །

[Block 1577]
འདོགས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་བར་དུ༌[^985]གསུངས་པ་ཡིན་ནོ། །

[Block 1578]
རྒྱན་འདོགས་པ་འདི་ལ་རྒྱན་དེ༌[^986]ཐམས་ཅད་ནི༌[^987]དཔེ་ཙམ་ཡིན་གྱི་འདི་ཐམས་ཅད་བཅང་བར་བྱ༌[^988]བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་སྟོན་པར་བྱེད་པའོ། །

[Block 1579]
འདི་ནི་རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་དེ་བསྲུང་བའི་དོན་དུ་སྲུང༌[^989]སྐུད་འདི༌[^990]ཚོན་ལྔའི་རང་བཞིན་ཅན་ནི་མི་བྱ་བར༌[^991]ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1580]
ཕྲན་ཚེགས་དག་ལས་དེ་ལ་སོགས་པ་འདིར་རུང་བ་ཞེས་བྱ་བའི་ཕྱིར་མཐར༌[^992]འདི་དྲངས༌[^993]པའོ། །

[Block 1581]
མ་མོ་ལས་ཀྱང་ཉན་ཐོས་ཀྱིས་ཀྱང་དོར་ན་ཞེས༌[^994]གསུངས་པ་ཡིན་ནོ། །

[Block 1582]
རྒྱན་བཅང༌[^995]བར་བྱའོ་ཞེས་བྱ་བ་ལ། རྒྱན༌[^996]རྣམ་པ་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེ་ཡི་ཕྱིར་གདགས་སུ་མི་རུང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གདགས་པར་མི་འོས་པ་དང་མི་རུང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1583]
རང་བཞིན་གང་ལས་བྱས་ཤེ་ན། དེའི་ཕྱིར་རོ་ཉེའམ་ཟངས་མའམ་ར་གན་ནམ་ཁར་བའམ༌[^997]རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མའམ། ཤིང་ངམ་རྡོ་འམ་ས་འམ་བ་སོའམ་རྭ་དག་རྣམས་ལས་བྱས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིའི༌[^998]གཞུང་ནི་གཞུང་ཁ་ཅིག་ལས་དགེ་སློང་གིས་གསེར་དང་དངུལ་དང་བཻ་ཌཱུརྱ་དང་ཤེལ་གྱི་རང་བཞིན་ལས་བྱས་པའི་རྒྱ༌[^999]རྣམས་བཅང་བར་མི་བྱའོ། །

[Block 1584]
སོར་གདུབ་ཀྱི་རྒྱན་ཡང་བཅང་བར་མི་བྱའོ། །

[Block 1585]
འོན་ཀྱང་འདིར་རྒྱན་ནི་རྣམ་པ་ལྔ་སྟེ། ར་གན་ལས་བྱས་པ་དང་ཟངས་མ་ལས་བྱས་པ་དང་། ཁར་བ༌[^1000]ལས་བྱས་པ་དང་བ་སོ་ལས་བྱས་པ་དང་རྭ་ལས་བྱས་པའོ་ཞེས་གསུངས་ཏེ། གཞན་དུ་ནི་དགེ་སློང་གིས་ཇི་སྲིད་གསེར་ལས་བྱས་པའི་བར་དུ་བཅང་བར་བྱའོ། །

[Block 1586]
འོན་ཀྱང་རྒྱན་རྣམ་པ་བརྒྱད་པོ་རོ་ཉེ་དང་ཟངས་དང་ར་གན་དང་ཁར་བ༌[^1001]དང་རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མ༌[^1002]དང་ཤིང་དང་རྡོ་དང་ས་ལས་བྱས་པ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1587]
དེ་ལ་རིན་པོ་ཆེ་ལས་གཞན་པའི་རྫས་ཀྱི་དཔེ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྡུས་ནས་བྱས་པ་ཡིན་ནོ། །

[Block 1588]
རྟགས་ནི་དགེ་འདུན་གྱི་ལ་ནི་དབུས་སུ་འཁོར་ལོ། །

[Block 1589]
ངོས་གཉིས་སུ་རི་དགས། [^1003]འོག་ཏུ་གཙུག་ལག་ཁང་གི་བདག་པོའི་མིང་བྲིའོ།[^1004] །གང་ཟག་གི་ལ་ནི་རུས་པའི་ཀེང་རུས་སམ་མགོའི་ཐོད་པའོ། །

[Block 1590]
སོ་མངས་ཀྱིས་སྐྲ་བཤད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལོངས་པའི་དངོས་པོ་ཡིན་པའི་ཕྱིར་རྣམ་པ་འདི་འཇུག་པ་དངོས་པོའི༌[^1005]རྣམ་པར་ཡང་འདིར་དངོས་པོ་ཞེས་བྱ་བ་འདི་ཞུགས་པའོ། །

[Block 1591]
དེ་ནི་དཔེའོ་ཞེས་བྱ་བ་ནི་སོ་མངས་ཞེས་བྱ་བ་འདི་ནི་གཞན་སྒྲུབ༌[^1006]པར་བྱེད་པའི་དཔེ་ཡིན་ཏེ། གཞན་གྱིས་ཀྱང་མགོའི་སྐྲ་བཤད་པས་མགོ་བཤད་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1592]
མེ་ལོང་གིས་བཞིན་བལྟ་བར་མི་བྱའོ། །

[Block 1593]
ཆུ་ཡན་ཆད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི༌[^1007]ཐ་ན་ཆུ་ཡན་ཆད་ཀྱིས་ཀྱང་སྟེ། ཆུ་ཡན་ཆད་ནས་ཏིལ་མར་དང༌[^1008]མར་ལ་སོགས་པའི་རྫས་གཞན་གྱི་བར་མན་ཆད་ཀྱིས་ཀྱང་བལྟ་བར་མི་བྱ་ཞེས་བྱ༌[^1009]བའི་དོན་ཏོ། །

[Block 1594]
ཆུ་བརྟག་པའི་ཆེད༌[^1010]ཉིད་དང་རྨ་དང་གཉེར་མ་དང་སྐྲ་དཀར་བལྟ་བ་དང་སྔ་ཕྱིའི་མཚན་མ་བཟུང་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པའི་དོན་གྱི་རྒྱུ་མཚན་ཉིད་གཙོ་བོ་འདི་ཡིན་ཏེ། འདིར་མིག་གི་དྲི་མ་ལ་སོགས་པ་ལ་ཡང་དོན་ཡོད་པར་དགོངས་པས་གནང་དུ་རུང་བ་འཕངས་པའོ། །

[Block 1595]
འཕྲལ་རིས་གསུམ་བསྟེན་པར༌[^1011]མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་ཕྱོགས་དེ་ལ་འདི་ནི་དཔེ་ཙམ་ཡིན་ཏེ། དེ་ལྟར་རིགས་ཅན་གྱི་ཆ་ནི་རང་གིས་བྱས་པའམ་གཞན་གྱིས་བྱས་པ་རྣམ་པར་འབྱེད་པ༌[^1012]བྱ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་གིས་འཕྲལ་རིས་གསུམ་བསྟེན་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1596]
གི་ཝང་གིས་བསྐུ་བ་བསྟེན་པར་མི་བྱའོ། །

[Block 1597]
དྲི་དག་གིས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བ་ཡང་བསྐུ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1598]
གསོ་བའི་ཆེད་དུ་ནི་གི་ཝང་གིས༌[^1013]བསྐུ་བ་བསྟན་པར༌[^1014]བྱའོ། །

[Block 1599]
གང་ཞིག་དྲིས་པས་རྗེས་སུ་གནང་བ་དེ་ལ་གསོ་བའི་ཆེད་ཉིད་མ་གཏོགས་པར་གཞན་ནི་ཁོངས་སུ་བསྡུས་པར༌[^1015]རིག་པར་བྱའོ། །

[Block 1600]
བསོད་ནམས་འདོད་པས་རྐང་པ་གཉིས་ལ༌[^1016]ལུས་བསྐུ་བའི་དྲིས་སྐུད་པ་བསྟེན་པར་བྱའོ། །

[Block 1601]
དེའི་མདུན་དུ་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་བསོད་ནམས་འདོད་པ་དེ་ལ་ཆོ་ག་གང་ཡང་འདི་སྐུད་པ༌[^1017]དང་འབྲེལ་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཉིད་བརྗོད་པར་བྱ་ཏེ།[^1018] དེ་དག་བསྐུས་པ་དགེ་འདུན་གྱི་ནང་དུ་འདུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་དྲི་དག་གིས་སོ། །

[Block 1602]
བསྐུས་པ་ཞེས་བྱ་བ་ནི་བྱུགས་པའོ། །

[Block 1603]
ཁྱིམ་བདག་ལ་ཆོས་བསྟན་པར་མི་བྱའོ། །

[Block 1604]
ཁྱིམ་དག་ཏུ་འགྲོ་བར་མི་བྱའོ། །

[Block 1605]
མཇུག་ཏུ་ཁྲུས༌[^1019]བྱའོ། །

[Block 1606]
དེ་དག་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་དྲི་དེ་དག་གོ། །

[Block 1607]
ཕེང་བ་རྒྱུ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང༌[^1020]བླང་བར་བྱའོ། །

[Block 1608]
མཆོད་རྟེན་ལ་དབུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། དྲི་དང་ཕྲེང་བ་རྒྱུ་བླངས་པ་དེ་དག་གོ། །སུའི་མཆོད་རྟེན་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཉན་ཐོས་ཀྱི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སངས་རྒྱས་ཀྱི་འབའ་ཞིག་ལ་དབུལ་བར་མ་ཟད་ཀྱི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1609]
སྦྱིན་པར་བྱེད་པ་མངོན་པར་མ་དད༌[^1021]ན་མགོ་ལོགས་སམ་རྐང་པ་ལོགས་སུའོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལ་དབུལ་བ་སྦྱིན་པར་བྱེད་པ་མངོན་པར་མ་དད་ན་རང་གི་མགོ་ལོགས་ཀྱི་སྔས༌[^1022]སམ་རྐང་པ་ལོགས་ཀྱི་རྟེན་མར་གཞག་པར་བྱའོ། །

[Block 1610]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་སྒོའི་བྱང༌[^1023]ཏད༌[^1024]མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1611]
འདིར་གཞི་གང་ལ་དབུལ་བ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྩིག་པ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཕྲེང༌[^1025]བའོ། །

[Block 1612]
དེ་ལ་དམིགས་ཀྱིས་བསལ་བར་གྱུར་པའི་ཆོ་ག་གཞན་བརྗོད་པར་བྱ་སྟེ། དེར་ཁབ་བམ་ཚེར་མ་བཙུགས་པ་ལ་ཕྲེང་བ་བརྒྱུས་པ་དག་དཔྱང་བར༌[^1026]བྱའོ་ཞེས་བྱ་བ་དེར་ཞེས་བྱ་བ་ནི་རྩིག་པའི་ངོས་བསྟན་པ་ལ་སྟེ་ཕྱེད་བརྐོས་པ༌[^1027]ལ་འཇུག་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1613]
ཚེར་མ་བཙུགས་པ་ལ་ཞེས་བྱ་བ་ནི་ཕྱེད་བཙུགས་པ་ལའོ། །

[Block 1614]
མིག་ལ་ཕན་པའི་དྲི་ཞིམ་པོ་དུས་དུས་སུ་བསྣམ་པར༌[^1028]བྱའོ་ཞེས་བྱ་བ་ནི་ཆོ་ག་འདི་ནི་གཉིས་ཀ༌[^1029]དང་འབྲེལ་པར་རིག་པར་བྱའོ། །

[Block 1615]
བྲམ་ཟེ་སྲད་བུ་ཐོགས་པ་བསྟེན་པར་མི་བྱའོ། །
--- END BLOCKS ---
