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
[Block 2171]
འདི་ཡང་རབ་ཏུ་འགྲོ་བ་ཡོངས་སུ་སྤང་བའི་དོན་དུ་རོ་མ་རྨས་པ་ལས༌[^1509]གོས་བླང་བར་མི་བྱའོ། །

[Block 2172]
རང་གིས་རྨས་པ་དང་རྨས་པར་བྱེད་དུ་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་རོ་ཞེས་བྱ་བ་མཐའ་གཉིས་ཀར་སྦྱར་རོ། །

[Block 2173]
ཐམས་ཅད་དུ་བསྟི་གནས་དང་སོ་ཤིང་དང་ཆུ་དང་འདག་རྫས་དང་ལྕི་བ་དང་ས་ཅི་བདེར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་བྱུག་པ་ལ་སོགས་པའི་དོན་དུ་བ་ལང་གི་ལྕི་བ་བཟུང་བ་ཡིན་ཏེ། འདག་རྫས་སུ་གྱུར་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2174]
འདིར་གཞུང་ནི་དགེ་སློང་གང་དུ་བསྟི་བ་དེར་རྣམ་པ་ལྔ་པོ་ཅི་བདེར་བརྗོད་པར་བྱ་སྟེ། སོ་ཤིང་དང་ཆུ་དང་འདག་རྫས་དང་ལྕི་བ་དང་སའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2175]
དགེ་སློང་དང་དགེ་ཚུལ་མི་འདོད་བཞིན་དུ་འབྲེལ་བས་ཁྲིད་པ་ན་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འབྲེལ་བས་ཞེས་བྱ་བ་ནི་ཕུ་ནུ་དང་བུ་སྲིང་དང་ཆུང་མ་ལ་སོགས་པས་མི་འདོད་བཞིན་དུ་ཁྲིད་པར་གྱུར་ན་དགེ་སློང་གིས་གཟུང་བར་བྱའོ། །

[Block 2176]
འདིར་གཞུང་ནི་དེ་ལ་ལག་པ་གང་ཤོས་ན་ཞེས་དྲིའོ། །

[Block 2177]
གལ་ཏེ་སྔོན་གྱི་ཆུང་མས་བཟུང་བ་ཤོས་ནའོ་ཞེས་ཟེར་ན་ནི་མི་གཏང༌[^1510]ངོ་། ། གལ་ཏེ་ཁྱོད་ཀྱིས་བཟུང་བ་ཤོས་ནའོ་ཞེས་ཟེར་ན་ནི་བསམ་པ་ལས་ཆུང་མ་འདོད་པ་འདྲ་བས་ཐོང་ཤིག༌[^1511]ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2178]
ཐམས་ཅད་དུ་མཚན་མ་ཉམས་པ་དང་ཚངས་པར་སྤྱོད་པ་དང་བཅས་པའི་རབ་ཏུ་བྱུང་བ་ལ་འདིའི་བྱ་བ་ཉིད་རིགས་པ་ཡིན་ཏེ། དེ༌[^1512]བས་ན་དགེ་ཚུལ་གྱི་ཚིག་བཟུང་བའོ། །

[Block 2179]
[^1513]ཕྲན་ཚེགས་ཀྱི་སྐབས་སོ།། །།

[Block 2180]
ཀ་ཀ་ནི་བཞི་ལ་མ༌[^1514]ཤ་ཀའོ་ཞེས་བྱ་བ་ལ། ཀ་ཀ་ནི་ཞེས་བྱ་བ་ནི་བོ་དྷི་ཀ་སྟེ། འགྲོན་བུ་ཉི་ཤུའི་རིན་ཐང་གི་མིང་ཡིན་ནོ། །

[Block 2181]
ཀ་ཀ་ནི་བཞི་ལ་ནི་མ་ཤ་ཀ་སྟེ། ཚིགས༌[^1515]ཉིད་ཉི་ཤུ་སྟེ་ཞེས་བྱ་བ་འཆད་པར་འགྱུར་བའི་ཚིག་དེའི་རང་གི་ངོ་བོ་བསྟན་པའི་ཕྱིར་མདོ་འདིའོ། །

[Block 2182]
གང་གི་ཕྱིར་འདིར་མ་ཤ་ཀ་ནི་ཚིགས་ཏེ་དེ་ཡང་དག་པར་བརྗོད་པ་ནི་ཀཱར་ཥཱ་པ་ཎའི་ཚད་མ་ལུས་པ་ཤེས་པའི་དོན་དུའོ། །

[Block 2183]
དེ་མ་ལུས་པར་ཤེས་པ་ནི་དེའི་བཞི་ཆ་ཅིག༌[^1516]བརྐུས་པའི་མཐའ་མར་འགྱུར་པ་ཉིད་ཀྱིས༌[^1517]ཚད་ཤེས་པར་བྱ་བའི་ཕྱིར། །ལྔ་ཉིད་ནི་ཀཱར་ཥཱ་པ་ཎ་བཞི་ཆའི་དཔེ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་རྣམ་པར་འབྱེད་པའི་མདོ་ལས་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པ་ཞེས་བྱ་བ་གསུངས་པ་དེ་ནི་ཀཱར་ཥཱ་པ་ཎའི་བཞི་ཆ་ཅིག་ནི༌[^1518]དཔེ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2184]
ཀཱར་ཥཱ་པ་ཎ་བཞི་ཆ་ཅིག༌[^1519]ཏུ་རྐུ་ན་ཕམ་པ་ཞེས་བྱ་བ་ཉིད་དོ། །

[Block 2185]
དེའི་ཕྱིར་འདི་གནས་གང་དང་དུས་གང་ལ་བརྟེན་ནས་ཤེས༌[^1520]ཤེ་ན། དེའི་ཕྱིར་གང་ན་དེའི་ཚིགས་ཉིད་ཉི་ཤུ་ཡིན་པ་དེ་ལ་བརྟེན་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་དང་དུས་གང་ན་ཀཱར་ཥཱ་པ་ཎ་དེའི་ཚིགས་ཉིད་མ་ཤ་ཀ་ཉི་ཤུ་ཡིན་པ་དེ་ལ་བརྟེན་ནས་མ་ཤ་ཀ་ལྔ་ཉིད་ནི་འདིའི་དཔེ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2186]
གང་ཞིག་བརྐུ་བའི༌[^1521]གནས་དང་དུས་ཀྱིས་དེའི་བརྩི་བ་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་འཆད་པར་འགྱུར་བ་ལས་དགར་བར་བྱ་བ་དང་དུས་དང་གནས་ཀྱི་དགོངས་པ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 2187]
ལྔ་ཉིད་ཅེས་བྱ་བ་ནི་དཔེ་ཡིན་ཏེ། དེ་བས་ན༌[^1522]ཚིགས་ལ་མ་ཤ་ཀའི་དགོས་པ་ཉིད་དོ། །

[Block 2188]
འོ་ན་ན༌[^1523]ན་ཀ་ཞེས་བྱ་བ་ལ་ཚིགས་འདི་འདོན་པ་ཡིན་ཏེ། ན་ན་ཀ་ཅི་ལྟ་བུ་མ་ཤ་ཀ་ལྔའི་བར་དུ་ལྟུང་བར་མི་འགྱུར་ན་ཐ་མའི་བཞི་ཆའི་ཀ་ཀ་ནིས་མ་ཤ་ཀ་ཚིགས་ཉི་ཤུ་པའི་ན་ན་ཀས་ཞེས་བྱའོ། །

[Block 2189]
འདིར་ཀཱར་ཥཱ་པ་ཎ་ཉིད་ན་ན་ཀའི་སྒྲས་གསུངས་པ་འདི་ལྟ་སྟེ། འདོན་པ་གང་ཞིག་ལ་མ་ཤ་ཀ་ནི་ན་ན་ཀ་ཉིད་ཀྱིས་འདོན་པ་ཡིན་ཏེ། ཀཱར་ཥཱ་པ་ཎ་ནི་ཚིགས་ཉིད་ཀྱིས་སོ། །

[Block 2190]
ན་ན་ཀ་ཇི་ལྟ་བུས་བརྐུས་ཤིང་ཀ་ཀ་ནི་བཞིས་ཉེ་བར་མཚོན་པའི་ཉི་ཤུ་ཉེ་བར༌[^1524]སོང་བའི་ཀཱར་ཥཱ་པ་ཎས་མ་ཤ་ཀ་ལྔ་རྐུ་ཞིང་ཐ་མ་ལ་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 2191]
འདིར་ཁ་ཅིག་རྣམས་ཀྱིས༌[^1525]འདོན་པ་དེ་ཇི་ལྟར་ཡང་མ་ཤ་ཀ་ལྔ་བརྐུས་ན་ལྟུང་བའི་མཐར་འགྱུར་རོ། །

[Block 2192]
མ་ཤ་ཀ་ཉི་ཤུ་པའི་ན་ན་ཀས་སོ། །

[Block 2193]
ཇི་ལྟ་བུས་ཤེ་ན་ཀ་ཀ་ནི་བཞི་ལ་མ་ཤ་ཀའོ། །

[Block 2194]
ཀཱར་ཥཱ་པ་ཎ་ཇི་ལྟ་བུས་ཤེ་ན། ན་ན་ཀའོ། །

[Block 2195]
དེའི་བཞི་ཆ་བརྐུ་བར་བྱས་པ་ཞེས་བྱ་བའོ། །

[Block 2196]
འདིར་མ་ཤ་ཀ་ཞེས་བྱ་བ་ཉིད་ཀྱིས་ཚིགས༌[^1526]བརྗོད་དེ་དེ་བས་ན་ཀཱར་ཥཱ་པ་ཎའི་དགོངས་པ་ཉིད་ན་ན་ཀའི་སྒྲ་ལ་དེའི་ཕྱིར་ལྟུང་བའོ། །

[Block 2197]
འོ་ན་དེ་ལྟར་ཡིན་ན་ཀཱར་ཥཱ་པ་ཎ་ཅི་ལྟ་བུ་ཞེས་བྱ་བའི་དྲི་མ་འདི་མི་ལྡང་ངོ་ཞེ་ན། འདི་ན༌[^1527]ཡོད་པ་མ་ཡིན་ཏེ། ཅི་ཞིག་བྱས་པ་དང་། ཅི་ཞིག་རྣམ་པར་གཞག་པས་ཞེས་བྱ་བ་ཉེ་བར་ཤེས་པ་པོ་མ་ལུས་པ་ཤེས་པའི་དོན་ཉིད་ཀྱི་ཕྱིར་འདི་ལའོ། །

[Block 2198]
དེ་ལྟར་ན་ཡང་བརྐུ་བར་བྱས་པས་ཞེས་བྱ་བས་ཉེ་བར་ཤེས་པ་པོ་ཉིད་ལ་བརྐུས་པ་ལ་རྒྱལ་པོས་བསྟན་པའོ། །

[Block 2199]
གཞུང་འདི་རྣམས་ལ་མ་ཤ་ཀ་ཉི་ཤུ་པ་ཉིད་ཀཱར་ཥཱ་པ་ཎ་གང་ལ་གསུངས་པའོ། །

[Block 2200]
ཀཱར་ཥཱ་པ་ཎ་ཅི་ལྟ་བུས་མ་ཤ་ཀ་ལྔ་བརྐུས་ན་ལྟུང་བ་ཐ་མར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་འདི་ལ་གཙོ་བོ་མ་ཡིན་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 2201]
དེ་བས་ན་འདིར་ལྔ་ཉིད་ནི་དཔེ་ཡིན་ཏེ། ཀཱར་ཥཱ་པ་ཎའི་བཞི་ཆ་ཞེས་བྱ་བ་འདི་རྙེད་པའོ། །

[Block 2202]
དེ་ལྟར་ཡང་གཏམ་གྱི་གཞིའི་སྐབས་ནས་ཤིན་ཏུ་གསལ་བར་འདི་གསུངས་པ་ཡིན་ཏེ། བཙུན་པ་མ་ཤ་ཀ་གསུམ་བརྐུས་ན་ཕམ་པའི་ལྟུང་བར་འགྱུར་བ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དོ།[^1528] །གང་ན་མ་ཤ་ཀ་བཅུ་གཉིས་ལ་ཀཱར་ཥཱ་པ་ཎ་གཅིག་ཏུ་གྱུར་པ་ནའོ། །

[Block 2203]
མ་ཤ་ཀ་ལྔ་ལས་ལྷག་པ༌[^1529]བརྐུས་ན་ཕམ་པའི་ལྟུང་བར་མི་འགྱུར་བ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། གང་ན་མ་ཤ་ཀ་བཞི་བཅུ་ལ་ཀཱར་ཥཱ་པ་ཎ་གཅིག་ཏུ་འགྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེར་ནི་མ་ཤ་ཀ་བཅུ་བརྐུས་ན་ཕམ་པར་འགྱུར་བར་དགོངས་སོ། །

[Block 2204]
དེང་སོང༌[^1530]ནི་འདིར་ཀཱར་ཥཱ་པ་ཎ་གཅིག་ནི་པ་ཎ་བཅུ་དྲུག་གིས་ཏེ། དེང་སོང༌[^1531]ནི་འདིར་པ་ཎ་བཞི་བརྐུས་ན་ཕམ་པར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 2205]
རྐུ་བའི་གནས་དང་དུས་ཀྱིས་དེའི་བརྩི་བ་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི་རྐུ་བའི་གནས་དང་རྐུ་བའི་དུས་ཀྱི་རིན་ཐང་བརྩི་བ་གང་ཡིན་པས་ཀཱར་ཥཱ་པ་ཎ་དེའི་རིན་ཐང་མ་ཤ་ཀ་བཅུ་གཉིས་ལ་ཀཱར་ཥཱ་པ་ཎ་གཅིག་གམ་མ་ཤ་ཀ་བཅུ་དྲུག་གམ་མ་ཤ་ཀ་ཉི་ཤུའམ། མ་ཤ་ཀ་བཞི་བཅུའམ་དེ་ལ་སོགས་པའི་རིན་ཐང་བརྩི་བ་དེས་བརྩིས་པའི་ཀཱར་ཥཱ་པ་ཎའི་བཞི་ཆ་ཅིག༌[^1532]བརྐུས་ན་ཕམ་པར་འགྱུར་བར་ཤེས་པར་བྱའོ།[^1533] །ཡུལ་གཞན་དང་དུས་གཞན་དང་གླིང་གཞན་གྱི་རིན་ཐང་བརྩི་བ་དེས་ཡུལ་དང་དུས་དང་གླིང་གཞན་དུ་བརྩི་བ་ནི་མ་ཡིན་ནོ། །

[Block 2206]
ཆེ་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར༌[^1534]མི་ནུས་པ་ནི་རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་ཕ་ལམ་ལ༌[^1535]སོགས་པ་རིན་པོ་ཆེ་གང་ཆེ་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར་མི་ནུས་པ་དེ་ནི་རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་ཡིན་ཏེ། རྫས་དེ་ལ་རིག་པར་བྱའོ། །

[Block 2207]
མ་ཤ་ཀ་ལྔ༌[^1536]ལ་སོགས་པའི་རིན་ཐང་བཟློག་པར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཕམ་པ་འབྱུང་བར་བྱ་བ༌[^1537]གང་ཞིག་བསམ་པ་དེའི་འདོད་པ་བཟློག་པའི་དོན་དུ་མདོ་འདི་གསུངས་སོ། །

[Block 2208]
ཕམ་པ་ནི་འདི་རྐུ་བ་ཞེས་བྱ་བ་དགུག་པའི་དོན་ཏོ། །

[Block 2209]
ཆུང་བ་ཉིད་ཀྱིས་དེར་མི་ཆོག་པ་ནི་ཁོངས་སུ་མ་གཏོགས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་རིན་ཐང་གདབ་མི་ནུས་པ་ལ་སྟེ། གང་ཞིག་ལ་ཆུང་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར་མི་ཆོག་པ་སྟེ། གང་ཞིག་མི་ཆོག་པ་ཉིད་ནི་དེར་ཁོངས༌[^1538]སུ་མ་བསྡུས་པ་ཉིད་མ་ཡིན་སྟེ། དེར་སྦོམ་པོའི་ལྟུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2210]
དེ་ལ་སངས་རྒྱས་ཀྱི་སྐུ་གདུང་ནི་གཞལ་དུ་མེད་པའི་རིན་པོ་ཆེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གཞལ་དུ་མེད་པ་ནི་མི་ནུས་པ་སྟེ། རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་ཡིན་པའི་ཕྱིར་འདི་ཙམ་ཞེས་བྱ་བ་གང་ཞིག་གཞལ་བར་མི་ནུས་པའི་རིན་པོ་ཆེ་དེ་ནི་གཞལ་དུ་མེད་པ་སྟེ། སངས་རྒྱས་ཀྱི་སྐུ་གདུང་དེ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
