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
སྔོན་ལྟུང་བ་བྱུང་བ་དང་དང་པོ་འཁྲུགས་པ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་། དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་། མཐའི་ལྟུང་བ་བྱུང་བ་དང་། ལྷན་ཅིག་འདུག་པས་དེ་དག་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2067]
དེ་བས་གཞན་པའི་དགེ་སྦྱོང་དང་བྲམ་ཟེ་དང་ལྷན་ཅིག་འདུག་པས་དེ་རྣམས་ལ་མ་དྲིས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། བསྙེན་པར་རྫོགས་པ་དང་བཅས་པའི་དབུས་སུ་གནས་པའི་དགེ་སློང་དང་དགེ་སློང་མ་དག་ཅེས་བྱ་བ་འདིས་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 2068]
རྫུ་འཕྲུལ་གྱིས་ནི༌[^1301]ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་གྲོང་དུ་འཇུག་པ་ལ་བྱེ་བྲག་གི་དོན་ཏེ། འདིར་འདི་ནི་མེད་པར་ནི་གོ་བ༌[^1302]མ་ཡིན་ནོ། །

[Block 2069]
གཞུང་གི་སྡེབ་སྦྱོར་བསྒྲུབ་པའི་དོན་འདི་སྦྱར་བ་ཡིན་ནོ། །

[Block 2070]
འདིར་གཞུང་ནི་རྫུ་འཕྲུལ་གྱིས་ནམ་མཁའ་ལ་འཇུག་ན་མ་སྨྲས་ཀྱང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2071]
དུས་མ་ཡིན་པར་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 2072]
གང་ལ་གྲོང་རྒྱུ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དུས་མ་ཡིན་པར་ཁྱིམ་པའི་གཞི་ལ་སོགས་པར་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་འཁོད་པར་མ་སྨྲས་པར་ཞེས་བྱ་བ་འདིས་དམིགས་ཀྱིས་བསལ༌[^1303]བར་གྱུར་པའི་ཆོ་ག་འདི་ཡིན་ནོ། །

[Block 2073]
དགེ་སློང་འཁོད་པ་ལ་སྨྲས་ཀྱང་ཁྱིམ་གཞི་ལ་སོགས་པར་དུས་མ་ཡིན་པར་འགྲོ་བ་གང་ཡིན་པ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་འདིར་དེ་འབའ་ཞིག་ལའམ་ཞེ་ན། དེའི་ཕྱིར་དེའི་ཚིག་གིས་དགེ་འདུན་སྤྱན་དྲངས་པ་ན་སྦྱིན་བདག་ཁོ་བོ་མ་འོངས་པའི་དབང་གིས་བྲིམ་པ་ཡོལ་བར་མ་བྱས་ཤིག་ཅེས་མ་བསྒོ་བར་གསུངས་པ་ལ་སོགས་པར་རྒྱུ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཚིག་གིས་དགེ་འདུན་སྤྱན་དྲངས་པ་ན་འདི་སྐད་ཅེས་ཁོ་བོ་མ་འོངས་པའི་དབང་གིས༌[^1304]ཞེས་བྱ་བ་བྲིམ་པ་ཡོལ་བར་མ་བྱས་ཤིག་ཅེས་བསྒོ་བའོ། །

[Block 2074]
ཟས་དེ་སྦྱིན་པ་པོ་ནི་སྦྱིན་བདག་སྟེ། དེས་གནང་བ་མ་བྱིན་པར་ཁྱིམ་གསུམ་པ་ལ་སོགས་པར་འགྲོ་བ་སྨོས་པ་གང་ཡིན་པ་དེ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2075]
དགེ་སྦྱོང་གི་ཚུལ་དང་སྲོག་ལ་སོགས་པའི་བར་ཆད་ཀྱི་དབང་གིས་དེ་དག་ལ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2076]
ཉི་མ་དེ་ཉིད་དང༌[^1305]གསོ་སྦྱོང་བྱེད་པའི་དུས་དེ་སྲིད་དུ་ཆོས་འདིའི་དབང་དུ་བྱས་པ་ལ་ཐོ་འཚམས༌[^1306]པར་བྱེད་ན་ཞེས་བྱ་བ་གླེང་གཞི་ལས་ཕྱི་ནས་ཁ་ཟས་བགོས་པ་ལ་སོ་སོར་ཉིད་དུ་གནང་བ་སྟེ། ཁ་ཟས་སྔ་མའི་ཆོ་གའི་ལྷག་མ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2077]
འདིར་ཐ་དད་པ་རྩོམ་པ་ནི་མི་མཐུན་པ་སྟེ། བདེན་པ་ཉིད་ཀྱི་ཕྱིར་ཕྱིས་དེར་འགྲོ་བ་ན་ལྟུང་བྱེད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2078]
དེ་བས་ན་བཞི་པ་ལ་སོགས་པ་དང་གསུམ་པ་ལ་སོགས་པ་ཞེས་སྨོས་པ་ཡིན་ཏེ།

[Block 2079]
བཞི་པ་དང་གསུམ་པ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2080]
ཟན་གཅད་པར༌[^1307]བྱ་བའི་བསམ་པས་གང་ཟག་རེ་རེ་ལ་འདིར་ལྟུང་བྱེད་གཞན་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 2081]
གྲོང་དུ་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 2082]
ཤེས་གཙོ་བོ༌[^1308]ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ནམ་མ་ལངས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉིན་མོའི་དང་པོ་ནི་སྐྱ་རེངས༌[^1309]ཤར་བ་ཡིན་པར་གསུངས་ལ་དེའི་མདུན་རོལ་ནི་མཚན་མོའི་མཐའ་ཡིན་པར་རྣམ་པར་གཞག་ན་ཅི་འདིར་ཡང་དེ་བཞིན་དུ་རྣམ་པར་གཞག་གམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་འདིར་ནི་སྐྱ་རེངས་ཐ་མ༌[^1310]མ་ཤར་བ་ཉིད་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དམར་ཞིང་སྐྱ་བ་ནི་ཐ་མའི་སྐྱ་རེངས༌[^1311]ཡིན་ལ་དེ་མ་ཤར་བ་ཉིད་ནི་འདིར་ནམ༌[^1312]མ་ལངས་པ་ཉིད་ཡིན་ལ། ཤར་བ་ཉིད་ནི་ནམ་ལངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2083]
མི་འཕྲོགས་པའི་རིན་པོ་ཆེ་རྣམས་སམ་རིན་པོ་ཆེར་སྨོས་པ་རྣམས་ལ་གང་ཞིག་འདིར་ཆོས་ཙམ་དུ་བརྗོད་པ་དེ་ནི་འོད་མེད་པ་ཉིད་ཀྱི་གནས་སྐབས་སུ་ཕལ་ཆེར་འགའ་ཞིག་འདིར་དམིགས་ཀྱིས་བསལ་བ་བསྐྱེད་པའོ། །

[Block 2084]
གང་ཞིག་འདི་སྤོང་བར་རིགས་པ་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུ་འདི༌[^1313]བསྟན་པ་ཡིན་ནོ། །

[Block 2085]
མི་འཕྲོགས་པ་ཉིད་འདི༌[^1314]ལ་ལྟུང་བ་བསྐྱེད་པའི་ཡན་ལག་ཉིད་མ་ཡིན་ཏེ། དེ་བས་ན་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2086]
གནས་སྐབས་གང་ལ་དེ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཙུན་མོའི་འཁོར་འདུག་པའི་གནས་དང་འབྲེལ་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཙུན་མོའི་འཁོར་འདུག་པའི་གནས་དང་འབྲེལ་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2087]
རང་འཇུག་པའི་དབང་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་འབྱིན་པར་བྱེད་པའི་དུས་སུ་འབྲེལ་པ་ཉིད་ལ་འདིར་མ་སྨྲོས་པའི༌[^1315]ཕྱིར་ལྟུང་བ་འབྱིན་པ་པོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 2088]
ལུས་ཀྱིས་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་འབྲེལ་པའོ། །

[Block 2089]
གང་གི་ཕྱིར་འདིར་དམིགས་པར་བྱེད་པ་པོ་ཉིད་ཀྱིས་སེམས་ཙམ་གྱི་འབྲེལ་པར་འགྱུར་ཏེ། དེ་ལ་ཡང་རེ་ཞིག་སེམས་ལ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ཉིད་ལ༌[^1316]ལྟུང་བ་མི་འཐད་པ་ཉིད་དོ། །

[Block 2090]
ཉོན་མོངས་པ༌[^1317]ཅན་ཉིད་ལ་ཡང་བསྡམ༌[^1318]པར་བྱ་བ་ཉིད་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2091]
དེ་ལྟ་བས་ན་སེམས་ཀྱིས་ནི༌[^1319]མ་ཡིན་ཏེ། འོན་ཀྱང་ལུས་ཀྱིས་ཀྱང་ལྟུང་བ་འབྱིན༌[^1320]པ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2092]
མཚན་མོ་དུས་གཞན་གྱི་ཚེ་ན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི༌[^1321]འདིར་ཤེས་གཙོ་བོ༌[^1322]ནམ་མ་ལངས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་འདིས་གྲུབ་པའོ། །

[Block 2093]
ཅི་ནུབ་མོ་གང་ལ་འབྲེལ་པ་ཉིད་དུ་འགྲོ་བའི་སྐབས་བྱེད་པ་ཉིད་ལ་ཡང་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དེའི་ཚེ་སྐབས་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ནུབ་མོ་དེ་དང་འབྲེལ་པ་ཉིད་ཀྱི་སྐབས་མ་ཡིན་པ་སྟེ། འབྲེལ་པ་ཉིད་འདི༌[^1323]ལ་ཞེས་བྱ་བ་དེའི་ཚེ་སྐབས་མ་ཡིན་པའོ། །

[Block 2094]
འདིར་གཞུང་ནི་གང་གི་ཚེ་འཕགས་པ་ཤཱ་རིའི་བུས་འཇུག་པར་བྱེད་པའི་གཞན་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་རྗེས་སུ་མ་གནང་མོད་ཀྱི་གནས་དེ་ནི་ཡོད་དོ། །

[Block 2095]
གང་ཞིག་ཡིད་ཆེས་པ་འདི་ཉིད༌[^1324]ཀྱི་དབང་དུ་བྱས་ན་རྗེས་སུ་ཡང་སུན་འབྱིན་པ༌[^1325]ཉིད་དུ་གྲགས་པ་དེ་བས་ན་མདོ་འདི་བྱས། མཚན་མོ་དུ་མར་འབྲེལ་པ་ཉིད་ལ་ཐམས་ཅད་ལ་འདུ་ཤེས་གཅིག་ཁོ་ན་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མཚན་མོ་རེ་རེ་ལའོ༌[^1326]ཞེས་བྱ་བ་སྨོས་ཏེ། ཉིན་མཚན་གྱི་དང་པོ་མ་ཡིན་པ་ལ་ཐ་མ་མ་ཡིན་པ་མེད་པ་ཉིད་དོ་ཞེས་སྨོས་པ་དེས་ནི་ཉིན་མཚན་གྱི་ཆོ་ག་འདི་བསྟན་པ་ཡིན་གྱི་མཚན་མོ་འབའ་ཞིག་གི་མཚན་ཉིད་བསྟན་པ་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་འདི༌[^1327]ལས་འཇུག་པ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2096]
མཚན་མོའི་ཆ་གང་ཡང་རུང་བ་ཉིད་ལ་ནི་ལྟུང་བྱེད་དོ། །

[Block 2097]
འོད་དམར་པོ་ཆགས་པ་གང་ཡིན་པ་དེ་འདས་པར་གྱུར་པ་ནི་མཚན་མོའི་དང་པོ་ཡིན་ཏེ། གལ་ཏེ༌[^1328]ནམ་འདས་པ༌[^1329]ཉིད་བསྟན་པའི་རྗེས་སུ་འབྲངས་པ་ལས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2098]
རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་མཚན་གཅིག་ལ་བར་མ་ཆད་པའི་གནས་སྐབས་ལ་ལྟུང་བ་གཅིག་པ་ཉིད་དོ། །

[Block 2099]
བར་དུ་ཆད་པ་ལ་ནི་ལྟུང་བྱེད་གཞན་ཡིན་ཏེ། རྩོམ་པ་གཞན་དུ་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2100]
གང་ནས་བརྩམས་ཏེ་སྒོར་ཞུགས་པ་དང་བཙུན་མོའི་འཁོར་གྱི་ནང་དུ་གནས་པ་རྟོགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེའི་སྒོའི་གཏན་པའི་ཉེན་ཀོར་གཉིས་ནི་དེའི་དང་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཙུན་མོའི་འཁོར་གྱི་གནས་དེའི་སྒོ་གཏན་པ་གང་ཡིན་པ་དེའི་ཉེན་ཀོར་གྱི་མདུན་དུ་ལྟུང་བ་དང་ཕྱིས་ལྟུང་བ་དག་ལ་སྲིད་པར་གྱུར་པའི་ཕྱོགས་དེས་ཇི་སྲིད༌[^1330]དུ་དེའི་ནང་གི་ངོས་ཀྱི་བཙུན་མོའི་འཁོར་གྱི་གནས་དེའི་དང་པོ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2101]
གལ་ཏེ་སྒོ་མ་བཅད་ན་ནི་ཉེ་འཁོར་གྱི་མཐའ་འདིར་དང་པོ༌[^1331]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2102]
སྒོ་བཅད་ན་ནི་དེའི་ཚེ་སྒོ་གཏན༌[^1332]གྱི་མཐའོ། །

[Block 2103]
རྒྱལ་པོའི་ཕོ་བྲང་དང༌[^1333]གྲོང་ཁྱེར་དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བཙུན་མོའི་འཁོར་དུ་འདུག་པའི་གནས་ཀྱི་དང་པོའི་སྒོ་གཏན་པའི༌[^1334]ཉེན་ཀོར་གྱི་མཐའ་གཉིས་ནི་དང་པོ་ཡིན་ནོ། །

[Block 2104]
དེ་བཞིན་དུ་རྒྱལ་པོའི་ཕོ་བྲང་དང་གྲོང་ཁྱེར་དག་གི་དང་པོ་ཡང་སྒོའི་གཏན་པའི༌[^1335]ཉེ་ཀོར་གྱི་མཐའ་གཉིས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2105]
འོབས་ཀྱིས༌[^1336]བསྐོར་བ་ཉིད་ལ་ནི་སྒོའི་དབུས་ཀྱི་རི་མོ་ལ་ནི་སྒོའི་ངོགས་ཀྱི་དབུས་ཉིད་དུ་ངེས་པ་འདི་ནི་ཆོ་ག་དང་པོར་ཁོང་དུ་ཆུད་པར་བྱའོ། །
--- END BLOCKS ---
