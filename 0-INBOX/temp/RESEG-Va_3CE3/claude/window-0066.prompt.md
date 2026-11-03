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
རབ་འབྱོར་ཇི་ལྟར་ཆོས་ཐམས་ཅད་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་པ༌[^1624]ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་གཉི་གར་ཡང་མི་འགྱུར་རོ། །

[Block 2312]
གཅིག་གི་ཚིག་བླ་དགས་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གྲངས་ཤེས་པ་བསྟན་ཏོ། །

[Block 2313]
བུད་མེད་ཀྱི་ཚིག་བླ་དགས་ལ་མཁས་པ༌[^1625]ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རྟགས་ཤེས་པ་བསྟན་ཏོ། །

[Block 2314]
ལམ་གྱི་རྒྱུན་བཅད་པ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་ལམ་ལ་མཁས་པའོ། །

[Block 2315]
ལམ་གྱི་རྒྱུན་མ་བཅད་པ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་ལ་མཁས་པའོ། །

[Block 2316 [HEADING]]
##### སྤྱད་པ་དང་མངོན་པར་བསྒྲུབ་པ་དང་བསྒོམ་པ། ^1-2-7-30-0

[Block 2317]
རབ་འབྱོར་གཟུགས་ཞི་བས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཞི་བ་ལ་སོགས་པ་མཚན་ཉིད་བཟུང་སྟེ་ཤེས་རབ་བསྐྱེད་པར་བྱ་བའོ། །

[Block 2318]
རབ་འབྱོར་ནམ་མཁའ་ལྟར་སྟོང་པ་ཉིད་མངོན་པར་བསྒྲུབ་པས། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མངོན་པར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ༌[^1626]བ་ནི་ནམ་མཁའ་བཞིན་དུ་སྟོང་པ་ཉིད་དུ་རྟོགས་པར་བྱ་བའོ། །

[Block 2319]
ནམ་མཁའ་སྟོང་པ་ཉིད་དུ་བསྒོམ་པས༌[^1627]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་བསྒོམ་པ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་བསྒོམ་པར་བྱ་བའོ། །

[Block 2320]
དེ་ལ་བྱེ་བྲག་ཏུ་བརྗོད་པར་འདོད་པ་ལ།[^1628]

[Block 2321]
དང་པོ་ནི་རྩོལ་བ་དང་བཅས་མཚན་མ་དང་བཅས་པའི་གནས་སྐབས་ཀྱི་སྤྱོད་པའོ། །

[Block 2322]
ས་དང་པོ་ཡན་ཆད་ནི་རྩོལ་བ་དང་བཅས་ལ། མཚན་མ་མེད་པའི་གནས་སྐབས་ཀྱི་མངོན་པར་སྒྲུབ་པའོ། །

[Block 2323]
ས་བརྒྱད་པ་ཡན་ཆད་ནི་ལྷུན་གྱིས་གྲུབ་ཅིང་མཚན་མ་མེད་པའི་གནས་སྐབས་ཀྱི་སྒོམ་པའོ༌[^1629]ཞེས་བསྟན་པའོ། །

[Block 2324]
སེམས་ཀྱི་རྒྱུན་མ་ཆད་ཅིང་མ་བྲལ་བར་རྗེས་སུ་འབྲེལ་པས་ཞེས་བྱ་བ་ནི་སེམས་རྒྱུན་མ་ཆད་པ་དང་། མ་བྲལ་བ་སྟེ། གང་རྗེས་སུ་འབྲེལ་ཞིང་རྒྱུན་ཆགས་པ་དེས་སེམས་བར་ཆད་མེད་ཅིང་སོ་སོར་མ་གྱེས་པ་དང་། རྗེས་སུ་འབྲེལ་བར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2325]
ཅི་ནས་ཀྱང་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་མི་རྒྱུ་བ་དེ་ལྟར་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གྱུར་གྱི༌[^1630]བར་དུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2326]
ཅི་ལགས་བསྒོམས་པས༌[^1631]རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རམ་ཞེས་གསོལ་པ་དང་། རབ་འབྱོར་དེ་ནི་མ་ཡིན་ནོ་ཞེས་བསལ་བ༌[^1632]གསུངས་ཏེ། རྩོལ་བ་དང་བཅས། རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་གནས་སྐབས་ལ་བྱའོ། །

[Block 2327]
མ་བསྒོམས་པས་སམ་ཞེས་གསོལ་ནས། ཅང་མི་གསུང་བར་གྱུར་པ༌[^1633]དང་། མ་ཡིན་ནོ་ཞེས་བསལ་བ༌[^1634]གསུངས་པའོ། །

[Block 2328]
བསྒོམས་ཀྱང་བསྒོམས༌[^1635]ལ་མ་བསྒོམས་ཀྱང༌[^1636]བསྒོམས་པས་སམ་ཞེས་གསོལ་པ་དང་། སྐྱོན་གཉིས་ཀ་བཤད་ཟིན་པས་གསལ་བ་གསུངས་སོ། །

[Block 2329]
བསྒོམས་པ་ཡང་མ་ལགས་མ༌[^1637]བསྒོམས་པ་ཡང་མ་ལགས་པས་སམ་ཞེས་གསོལ་པ་དང་། གལ༌[^1638]གཉིས་སུ་སྨྲ་བའི་གཞུང་གིས་འཁྲུགས་སུ་དོགས་པས་བསལ་བ༌[^1639]གསུངས་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་བརྗོད་དུ་མེད་ཅིང་བསམ་གྱིས་མི་ཁྱབ་པའི་གནས་སྐབས་ཡིན་པར་བསྟན་ཏོ། །

[Block 2330 [HEADING]]
##### ཆོས་ཐམས་ཅད་མི་དམིགས་པའི་གནས། ^1-2-7-31-0

[Block 2331]
རབ་འབྱོར་དེ་བཞིན་ཉིད་ཇི་ལྟ་བ་བཞིན་ཞེས་བྱ་བ་ནི་ཕྱིས་ཆོས་ཐམས་ཅད་མི་དམིགས་པའི་གནས་སུ་བསྟན་པ་སྟེ། བདག་གི༌[^1640]ཁམས་ཇི་ལྟ་བ་བཞིན་ཞེས་བྱ་བ་ལ་སོགས་པའོ།[^1641] །རབ་འབྱོར་གདགས་སུ་མེད་པའོ་ཞེས་བྱ་བ་ནི་བརྗོད་དུ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2332]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས་སེམས་ཅན་དུ་གདགས་པ་དམིགས་སུ་ཡོད་དམ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སེམས་ཅན་དམྱལ་བ་ལ་སོགས་པས༌[^1642]ཀུན་བརྟགས་པའི་ཕྱིར་མེད་པ་ལས་ཀུན་རྫོབ་ཏུ་བཏགས་པ་སྟེ། བྱིས་པ་སོ་སོའི༌[^1643]སྐྱེ་བོ་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པའོ། །

[Block 2333]
དབྲི་བ་མེད་པ་དང་བསྣན་པ་མེད་པར་ཞེས་བྱ་བ་ནི་ཡོད་པ་ལ་སྐུར་པ་འདེབས་པ་ནི་དབྲི་བའོ། །

[Block 2334]
མེད་པ་ལ་སྒྲོ་འདོགས་པ་ནི་བསྣན་པའོ། །

[Block 2335]
སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་ལ༌[^1644]བསླབ་པ་ཞེས་བྱ་བ་སྐྱེ་བ་མེད་པའི་བསླབ་པ༌[^1645]ནི་གང་སྒྲོ་འདོགས་པ་མེད་པའོ། །

[Block 2336]
འགག་པ་མེད་པའི་བསླབ་པ་ནི་ཡོད་པ་ལ༌[^1646]གང་སྐུར་པ་འདེབས་པ་མེད་པའོ། །

[Block 2337]
བསྒོམ་པར་ཡང་མི་བགྱི། རྣམ་པར་གཞིག་པ༌[^1647]ཡང་མི་བགྱི་ཞེས་བྱ་བ་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ལ་སློབ་པ་སྟེ། བསྒོམ་པར་བྱ། བསྐྱེད་པར་བྱ་སྙམ་པའི་མངོན་པར་འདུ་བྱེད་པ་མེད་པས་སྐྱེ་བ་མེད་པའི་བསླབ་པའོ། །

[Block 2338]
རྣམ་པར་གཞིག་པར་བྱ༌[^1648]མེད་པར་བྱ་སྙམ་པའི་མངོན་པར་འདུ་བྱེད་པ་མེད་པས་འགག་པ་མེད་པའི་བསླབ་པའོ། །

[Block 2339]
གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་གཟུགས་ནི་གཟུགས་ཉིད་དུ་མེད་པའོ། །

[Block 2340]
གཟུགས་ཀྱི་མཚན་ཉིད་ཀྱིས་སྟོང་པའི་ཕྱིར་རོ། །

[Block 2341]
སྤྱོད་པ་མེད་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དམིགས་སུ་མེད་པའི་ཕྱིར་གང་ལ་ཡང་མི་སྤྱོད་པ་ཉིད་སྤྱོད་པའོ། །

[Block 2342]
གལ་ཏེ་སྤྱོད་པ་མ་མཆིས་པ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལགས་ན་ལས་དང་པོ་པའི་བྱང་ཆུབ་སེམས་དཔས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཇི་ལྟར་སྤྱད་པར་བགྱི་ཞེས་ཞུས་པ་དང་། ལས་དང་པོ་པའི་བྱང་ཆུབ་སེམས་དཔས་ཞེས་བྱ་བ་ནི༌[^1649]ལ་སོགས་པས་སེམས་དང་པོ་བསྐྱེད་པ་ནས་བཟུང་སྟེ། མི་དམིགས་པའི་ཚུལ་དུ་ཆོས་ཐམས་ཅད་ལ་བསླབ་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། ལས་དང་པོ་པ་ལ་དོན་དམ་པའི་སྤྱོད་པ་མེད་དུ་ཟིན་ཀྱང་དེའི་ཕྱིར་བསླབ་པར་བྱ་སྟེ། བསླབ་པ་ཉིད་སྤྱད་པ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 2343 [HEADING]]
##### དམིགས་པ་དང་མི་དམིགས་པ་མཉམ་པ་ཉིད། ^1-2-7-32-0

[Block 2344]
བཅོམ་ལྡན་འདས་ཅི་དམིགས་སུ༌[^1650]མཆིས་པ་མི་དམིགས་པ་ལགས༌[^1651]སམ་ཞེས་བྱ་བ་ནི་མི་དམིགས་པ་དམིགས་སུ་མཆིས་སམ་ཞེས་ཞུས་པའོ། །

[Block 2345]
དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་དམིགས་སུ་མེད་པས། དམིགས་སོ་ཞེས་བརྗོད་དུ་མི་རུང་བའི་ཕྱིར་དམིགས་སུ་ཡོད་པ་མི་དམིགས་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བས་བསྩལ་བ༌[^1652]གསུངས་ཏེ། དམིགས་སུ་མེད་པའི་མཚན་ཉིད་ཆོས་ཐམས་ཅད་ཀྱི་མཉམ་པ་ཉིད་ཡོད་པའི་ཕྱིར༌[^1653]མི་དམིགས་པ་དམིགས་སུ་མེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2346]
དམིགས་པ་དང་མི་དམིགས་པ་མཉམ་པ་ཉིད་ནི་མི་དམིགས་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དམིགས་སུ་ཡོད་པ༌[^1654]དངོས་པོ༌[^1655]གང་ཡིན་པ་དང་། ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པ་དངོས་པོ་མེད་པ་གང་ཡིན་པ་དེ་གཉི་ག་ཡང་མཚུངས་སོ། །

[Block 2347]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་ཏེ། དམིགས་སུ་ཡོད་པ་ནི་ཀུན་བརྟགས་པ་ཡིན་པས་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 2348]
དམིགས་སུ་མེད་པ་ཡང་དངོས་པོ་མེད་པའི་བདག་ཉིད་ཡིན་པས་ངོ་བོ་ཉིད་མེད་དེ། དེ་བས་ན༌[^1656]གཉི་ག་ཡང་ངོ་བོ་ཉིད་མེད་པར་མཚུངས་ཏེ། དམིགས་སུ་ཡོད་པ་དང་། དམིགས་སུ་མེད་པ་དེ་གཉིས་ཀྱི༌[^1657]མཉམ་པ་ཉིད་ངོ་བོ་ཉིད་མེད་པ། གང་ཡིན་པ་དེ་ནི་དམིགས་སུ་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2349 [HEADING]]
##### ས་ནས་ས་ཡོངས་སུ་རྫོགས་པར་བྱ་བ། ^1-2-7-33-0

[Block 2350]
ཇི་ལྟར་ས་ནས་ས་ཡོངས་སུ་རྫོགས་པར་བགྱི། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཇི་ལྟར་ཐོབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དམིགས་པ་ལ་ཆགས་པར་མ་གྱུར་ན། གོང་ནས་གོང་མའི་ས་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་ཇི་ལྟར་བརྩོན་པར་བྱ་ཞེས་དགོངས་པའོ། །
--- END BLOCKS ---
