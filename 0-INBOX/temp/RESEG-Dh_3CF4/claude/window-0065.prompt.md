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
[Block 2276]
བྲག་ཅའི་སྒྲའི་ཁྱབ་པའི་སྒྲ་གང་ཡིན་པའི་རྔ་སྒྲ་ཆེན་པོའི་སྒྲ་དེ་ནི་ཁྱབ་པའི་བྲག་ཅ་དང་སྒྲ་བརྙན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2277]
གསལ་བའི་ཚིག་དང་འབྲུ་གང་ཡིན་པའི་ནམ་མཁའ་དེ་ནི་ཚིག་འབྲུ་གསལ་བའི་ནམ་མཁའ་ལའོ། །

[Block 2278]
གཡོ་བ་གང་ལ་ཡོད་པ་དེ་ནི་གཡོ་བ་ཅན་ཏེ་རབ་ཏུ་གཡོ་བ་ཅན་ནོ། །

[Block 2279]
རིའི་ནུ་མ་གཡོ་བ་ཅན་གང་ཡིན་པ་དེ་ནི་རིའི་ནུ་མ་གཡོ་བ་ཅན་ནོ། །

[Block 2280]
ནམ་མཁའ་ནི་མཐོ་རིས་སོ། །

[Block 2281]
གློག་གིས༌[^1435]གསལ་བ་དང་བཅས་པའི༌[^1436]གློག་འགྱུ་བ་ནི༌[^1437]འོད་ཀྱིས་གསལ་བའོ། །

[Block 2282]
དེས་གསལ་བ༌[^1438]དང་བཅས་པ་དེ་ལ་ནི་གློག་འགྱུ་བའི་འོད་ཀྱིས་གསལ་ཞིང་མཐོང་བའོ། །

[Block 2283]
ཡང་ན་བརྩམས་པའོ། །

[Block 2284]
ཡང་ན་འོད་དང་ལྡན་པ་སྟེ། དེས་གསལ་བར་གྱུར་པའོ། །

[Block 2285]
སྩལ་བའི༌[^1439]ཐུགས་ནི་དགྱེས་པར་མཛོད། །ཅེས་བྱ་བ་ནི་འདི་ལྟར་མཇུག༌[^1440]གི་ལས་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 2286]
དེ་ལྟར་སེམས་དད་པའི་ཕན་ཡོན་གང་ཡིན་ཞེ་ན། འཇིག་རྟེན་རྣམས་ལ་བཏུང་ཆུ་བཞིན། །ཞེས་སྨོས་སོ། །ཇི་ལྟར་བཏུང་ཆུ་བཞིན་དུ་གྱུར་པ་ཡིན་ཞེ་ན། སླན་ཆད་ཀྱང་ནི་སྦྱིན་བདག་མཛོད། །ཅེས་སྨོས་ཏེ། ཅི་ནས་ཀྱང་སྦྱིན་པ་ལས་བཏུང་ཆུ་བཞིན་དུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2287]
སྦྱིན་པ་ཉིད་ཆོས་ཡིན་པས་སྦྱིན་པའི་ཆོས་སོ། །

[Block 2288]
ཟད་པ་སྐམས་པའོ།[^1441] །འདོད་ལྷའི་སེམས་ནི་མྱ་ངན་མེ་ཡིས་ཚིག །ཅེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྫོགས་པའི་ཕྱིར་ཏེ། དེ་བས་ན་ཡང་སངས་རྒྱས་ཉིད་ཐོབ་པ་ལ་ནི་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་སྦྱིན་པ་ལས་སྙིང་རྗེ་ཁྱད་པར་དུ་གྱུར་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2289]
འོ་ན་མ༌[^1442]དྲི་སྐྱེས་བུ་གཞན་ལ་བྱིན་པས་འཁྲུགས་པར་མ་གྱུར་ཏམ་ཞེ་ན་མ་ཡིན་ཏེ། ཁྱིམ་ཐབ་དང་བྲལ་བའི་མྱ་ངན་གྱི་ཁུར་གྱིས་ནོན་པར་གྱུར་པའི་ཕྱིར་ཏེ། སློང་བ་ལ་མི་བཟློག་པའི༌[^1443]རང་བཞིན་ཡིན་པས་སོ། །

[Block 2290]
དེ་ལ་མིག་ཚུགས་ལྟ་ཞིང་བྲིས༌[^1444]བཞིན་འདུག །ཅེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་མེད་པའི་སྡུག་བསྔལ་གྱི་ཁུར་གྱིས་ནོན་པའི་ཕྱིར་རོ། །

[Block 2291]
བྲིས༌[^1445]བཞིན་ཞེས་བྱ་བ་ནི་གཡོ་བ་མེད་པ་དང་། མིག་འབྱེད་པ་དང་འཛུམས་པ༌[^1446]མེད་པའི་ཕྱིར་རོ། །

[Block 2292]
ཡ་རབས་མ་རབས་ཆོས་གཉིས༌[^1447]ནི། །ཞེས་བྱ་བ་ལ། དམ་པ་དང་དམ་པ་མ་ཡིན་པ་ནི་ཡ་རབས་དང་མ་རབས་སོ། །

[Block 2293]
དེ་གཉིས་ཀྱི་ཆོས་ནི་ཡ་རབས་མ་རབས་ཀྱི་ཆོས་གཉིས་སོ། །

[Block 2294]
མ་རབས་ཀྱི་ཆོས་ནི་གཞན་གྱི་བུད་མེད་ལ་འགྲོ་བའོ། །

[Block 2295]
འདི་ནི་ཡ་རབས་ཀྱི་ཆོས་ཏེ། རང་གི་ཆུང་མ་གཞན༌[^1448]ལ་སྦྱིན་པའོ། །

[Block 2296]
དམ་པ་དང་དམ་པ་མ་ཡིན་པ་ནི་ཡ་རབས་མ་རབས་ཏེ། །ཇི་ལྟར་ཁྱད་པར་རེ་ཆེ་སྙམ་ན།

[Block 2297 [VERSE]]
བདག་ཉིད་མ་སྦྱངས་པ་རྣམས་ནི། །
སུས་ཀྱང་ཡིད་ཆེས་མི་ནུས་སོ། །

[Block 2298]
ཞེས་སྨོས་ཏེ། འདི་ལྟར་དམ་པ་ཡིན་པས་དེ༌[^1449]ནི་ངེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2299]
དེ་ལྟར་མ༌[^1450]རབས་ཀྱི་ཆོས་ཀྱི་རང་གི་ངོ་བོ་བསྟན་ནས། ཡ་རབས་ཀྱི་ཆོས་ཀྱི་སྨྲ་བ་ལས་བརྩམས་པ། འདོད་ཆགས་བྲལ་བར་མ་གྱུར་པས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། རྒྱུ་གསུམ་གྱིས་ནི་ཉོན་མོངས་པ་སྐྱེ་བར་འགྱུར་ཏེ། །

[Block 2300 [VERSE]]
ཕྲ་རྒྱས་སྤངས་པར་མ་གྱུར་དང་། །
ཡུལ་ནི་ཉེ་བར་གནས་པ་དང་། །
ཚུལ་བཞིན་མ་ཡིན་ཡིད་བྱེད་ལས། །
ཉོན་མོངས་རྒྱུ་ནི་ཚང་བ་ཡིན། །

[Block 2301]
ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2302]
དམ་པ་རྣམས་ནི་སེམས་རྒྱ་ཆེ་བ་ཡིན་པས༌[^1451]ཡུལ་མངོན་དུ་གྱུར་ཀྱང་ཉོན་མོངས་པ་འགོག་ཅིང་ཉོན་མོངས་པ་ཀུན་ཏུ་མི་སྤྱོད་པ་ཡིན་ཏེ། དེ་བས་ན་རྒྱུ་མ་ཚང་བས་ཉོན་མོངས་པ་མི་སྤྱོད་པ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 2303]
འདོད་ཆགས་དང་མ་བྲལ་བ་ནི་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཉོན་མོངས་པ་འགོག་པའོ། །

[Block 2304]
ཅིག་ཤོས་ནི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་སྤངས་པ་ཡིན་ཏེ། ད༌[^1452]བུ་དང་ཆུང་མ་ལ་དགའ་བ་ཉིད་ཀྱང་མེད་དེ། དེ་བས་ན་ཉོན་མོངས་པ་འགོག་པ་མེད་པའང༌[^1453]བསྟན་ཏོ། །

[Block 2305]
འདོད་ཆགས་དང་བྲལ་བར་མ་གྱུར་པ་ཞེས་སྨོས་པ་འདིས་ནི་འདོད་ཆགས་སྐྱེ་བའི་རྒྱུ༌[^1454]བསྟན་ཏོ།[^1455] །བུ་སྨད་རབ་ཏུ་སྡུག་པ་དག །ཅེས་བྱ་བ་འདིས་ནི་རྒྱ་ཆེ་བའི་ཡུལ་དང་ཉེ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2306]
དེ་ལྟར་མ་ཆགས་སྦྱིན་བྱེད་པ། །ཞེས་བྱ་བ་ལ། འདིར་འདོད༌[^1456]ཆགས་པ་ནི་སྲེད་པའི་འདོད་ཆགས་སམ་ཆགས་པའོ། །

[Block 2307]
ཆགས་པ་དང་བྲལ་བ་ནི་གང་གི༌[^1457]ཕྱིར་མ་ཆགས་པའོ། །

[Block 2308]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་འདི་ལྟར་མངོན་སུམ་ཉིད་དུ་བསྒོམ་པ༌[^1458]བསྟན་ཏེ། འདིས་ནི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་མེད་པ་ཉིད་དེ། དེ་ལྟར་ཡ་རབས་དང་མ་རབས༌[^1459]ཀྱི་ཆོས་གཉིས་ཤིན་ཏུ་ཁྱད་པར་ཆེ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2309]
ཉི་མའི་འོད་ཀྱིས་ཞེས་བྱ་བ་ལ་ཉི་མའི་འོད་ནི་ཉི་མའི༌[^1460]གཟི་བརྗིད་དོ། །

[Block 2310]
གཞན་གྱི་འོད་ནི་ཟླ་བ་སོགས་པའི་འོད་དོ། །

[Block 2311]
ཉི་མའི་འོད་ཀྱིས་ཞེས་བྱ་བ་དང་། བསྒྲགས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2312]
ཁྱོད་ཀྱི་ཡོན་ཏན་ཆགས་པའི་གཏམ་དག་གིས། །ཞེས་བྱ་བ་ལ་ཆགས་པའི་གཏམ་གང་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། ཁྱོད་ཀྱི་སྤྱོད་པ་ཞེས་ཚིགས་བཅད་བརྩམས་སོ། །ཇི་ལྟར་ཆགས་པའི་གཏམ་ཡིན་ཞེ་ན། ཆགས་པའི་གཏམ་ཉིད་དུ་ཚིགས་བཅད་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 2313 [VERSE]]
ཁྱོད་ཀྱི་སྤྱོད་པ་མི་ལས༌[^1461]འདས། །
ཞེས་བྱ་བ་གང་ཡིན་ཞེ་ན།
ཚིགས་བཅད་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 2314]
གནོད་སྦྱིན་དྲི་ཟ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1462]གཤོལ་མདའ་འཛིན་ལ་སོགས་པའི་རི་དག་གི་བར་ན་གནས་པའོ། །

[Block 2315]
ལྟོས་འགྲོ་ཞེས་བྱ་བ་སྨོས་པས་ནི་སའི་འོག་ན་གནས་པ་པ་དང་། རྒྱ་མཚོ་ན་གནས་པ་གཟུང་ངོ་། །སུམ་ཅུ་རྩ༌[^1463]
--- END BLOCKS ---
