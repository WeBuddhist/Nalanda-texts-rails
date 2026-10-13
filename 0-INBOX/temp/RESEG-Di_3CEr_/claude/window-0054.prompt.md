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
[Block 1891]
གྲུབ་པའི༌[^1505]དུས་ན་ནི་གཏན་ཚིགས་མ་བརྗོད་ན་གཏན་ཚིགས་མ་ཚང་བར་འགྱུར་ན་འདི་ནི་མ་བརྗོད་པ་ལས་སྔར་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 1892]
འདིར་གཏན་ཚིགས་ཀྱི་དོན་མ་ལུས་པ་མེད་པར་བརྩད་པའི་ཕྱིར་དཔེ་བརྗོད་མ་ཚང་བ༌[^1506]ལྟར་སྣང་བ་ཉིད་དུ་ཡང་རིག་པར་བྱའོ། །

[Block 1893 [HEADING]]
### མ་སྐྱེས་པ་མཚུངས་པ། ^6-5-0

[Block 1894]
བརྗོད་པ་ལས་སྔར་རྟགས་མིན་ཕྱིར། །མ་གྲུབ་པ་དང་འགལ་བའི་ངག །

[Block 1895]
མ་སྐྱེས་པ་མཚུངས། དཔེར་ན་སྔར་བཞིན་བྱས་པ་ལ་གལ་ཏེ་འདི་ལྟར་བརྗོད་པ་ལས་སྔར་སྒྲ་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་མ་ཡིན་པས༌[^1507]འགྱུར་རོ། །

[Block 1896]
རྩོལ་བ་ལས་མ་བྱུང་བའི་ཕྱིར་བརྟག་པ༌[^1508]ཡང་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ནི་མ་སྐྱེས་པ་མཚུངས་པའོ། །

[Block 1897]
དེ་ལྟ་ན་ཡང་། རྣམ༌[^1509]གཉིས། གཉིས་སུ་སྒྲོ་བཏགས་པ་ལས་འདོད། །དེ་ལ་བརྗོད་པ་ལས་སྔར་སྒྲུབ་བྱེད་དུ་སྒྲོ་བཏགས་པ་ལས་མ་གྲུབ་པ་ལྟར་སྣང་བའོ། །

[Block 1898]
སྐྱེས་པ་དག་ནི་སྒྲ་ཞིག་པ་ཉིད་ཀྱིས་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་ཡིན་པའི་ཕྱིར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1899]
དེ་དེའི་ཚེ་ཡོད་པ་ཡང་ཡིན་ནོ། །

[Block 1900]
རྩོལ་བ་ལས་མ་བྱུང་བ་ཉིད་ནི། དོན་གྱི་དབང་གིས་མི་རྟག་པ་ཉིད་དུ་ཡང་སྒྲོ་འདོགས་པས་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1901 [HEADING]]
### འབྲས་བུ་མཚུངས་པ། ^6-6-0

[Block 1902]
འབྲས་བུ་གཞན་ཉིད་ཀྱི་ཆ་ནས། བསྒྲུབ་བྱ་མི་འགྲུབ་པར་སྟོན་པ།[^1510] དེ་ནི་འབྲས་མཚུངས། དཔེར་ན་སྒྲ་མི་རྟག་སྟེ། འབྲས་བུ་ཡིན་པའི་ཕྱིར་བུམ་པ་བཞིན་ཞེས་བྱ་བ་ལ། གཞན་བུམ་པའི་འབྲས་བུ་ཉིད་ཀྱིས་བྱས་པ་མི་རྟག་པ་ཡིན་ན་སྒྲ་འདིའིའོ་ཞེས་ཅི་སྟེ་བྱ་ཞེས༌[^1511]བྱ་བ་ནི་འབྲས་བུ་མཚུངས་པའོ། །

[Block 1903]
དེ་ལྟ་བུ། སྨྲ་པོའི་འདོད་པ་རྣམ་པ་གསུམ། །གལ་ཏེ་སྨྲ་བ་པོའི་བུམ་པའི་འབྲས་བུ་ཉིད་སྒྲ་ལ་མེད་དོ་ཞེས་རྩོད་ན་ནི་དེའི་ཚེ་མ་གྲུབ་པ་ལྟར་སྣང་བའོ། །

[Block 1904]
འོན་ཏེ་སྒྲའི་འབྲས་བུ་ཉིད་བུམ་པ་ལ་སོགས་པའི་མི་རྟག་པ་ལ་མེད་དོ་ཞེས་རྩོད་པའི་ལྟ་ན་འགལ་བ་ལྟར་སྣང་བའོ། །

[Block 1905]
དེ་སྟེ་དེ་ཉིད་རྟག་པ་ལ་ཡང་མེད་དོ་ཞེ་ན་ནི་ཐུན་མོང་མ་ཡིན་པ་ཡིན་པའི་ཕྱིར། མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1906]
ཡང་ན་ཆོས་མཐུན་པ༌[^1512]བསྟན་པའི་ཕྱིར། དཔེའི་སྐྱོན་ལྟར་སྣང་བའོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཆོས་ཀྱི་སྤྱི་བཟུང་ནས་རྗེས་སུ་དཔོག་པར་བྱེད་པ་ཡིན་གྱི། དེའི་བྱེ་བྲག་ལས་ནི་མ་ཡིན་ཏེ། དེའི་དོན་སོ་སོར་ངེས་པ་ཉིད་ཀྱི༌[^1513]རྗེས་སུ་དཔག་པ་མེད་པ༌[^1514]ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1907 [HEADING]]
### ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་མཚུངས་པ། ^6-7-0

[Block 1908]
ངེས་བསྟན་མི་མཐུན་ཕྱོགས་དག་ལས། །ཆོས་མཐུན་དཔེ་ཡིས་གཞན་སྒྲུབ༌[^1515]པ། །

[Block 1909]
ཆོས་མཐུན་པར་མཚུངས། གཞན་སྒྲུབ་ཅེས་བྱ་བ་ནི། བཟློག་པ་སྒྲུབ་པ་སྟེ་བྱེད་པ་པོའི་རྒྱུར་བྱས་ནས་སོ། །

[Block 1910]
དཔེར་ན། སྒྲ་མི་རྟག་སྟེ། རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་ཆོས་མི་མཐུན་པའི་དཔེ་ནམ་མཁའ་བཞིན་ནོ་ཞེས་བྱ་བ་ལ། ངེས་པར་བསྟན་པའི་ནམ་མཁའ་དང་ཡང་ལུས་ཅན་མ་ཡིན་པ་ལ་སོགས་པར་ཆོས་མཐུན་པའི་ཕྱིར་མི་རྟག་པའོ་ཞེས་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 1911]
དེ་ལྟར་ན༌[^1516]གཏན་ཚིགས་འདི་དག་ཉིད་དུ། བུམ་པ་ཆོས་མཐུན་པར་བྱས་པ་ལ། དེའི་མི་མཐུན་པའི་ཕྱོགས་ནམ་མཁའ་དང་ཆོས་མཐུན་པར་བརྗོད་པ་དེ་ལྟ་བུ་ནི་ཆོས་མཐུན་པ་མཚུངས་པའོ། །

[Block 1912]
གཞན་དག་ནི། ཆོས་མི་མཐུན་པས། ངེས་པར་བསྟན་པའི་མི་མཐུན་པའི་ཕྱོགས་དག་ལས་གཞན་སྒྲུབ་པར་བྱེད་དོ་ཞེས་བརྗོད་པ་ལ། དཔེ་གཉིས་ཀ་ཡང་སྔར་བཞིན་བུམ་པ་ཆོས་མི་མཐུན་པའི་དཔེར་སྦྱར་བར་བྱའོ། །

[Block 1913]
དེ་ལྟ་བུ་དག་གི །མཚུངས་པ་ཉིད།

[Block 1914 [VERSE]]
གཞན་ལ་མ་གྲུབ་བསྟན་པའི་ཕྱིར། །
ཐུན་མོང་ལྟར་སྣང་རྣམ་པ་གཉིས། །

[Block 1915]
གལ་ཏེ་འདི་ལུས་ཅན་མ་ཡིན་པ་ལ་སོགས་པ་དང་ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པ་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 1916]
གཞན་ལ་མ་གྲུབ་པ་རྩོད་ན་ནི་ཇི་ལྟར་ཁོ་བོའི་ཆོས་མཐུན་པ་དང་། ཆོས་མི་མཐུན་པ་ཙམ་ལས་མ་གྲུབ་པ་བཞིན་དུ་ཁྱོད་ཀྱི་ཡང་ཡིན་ནོ། །

[Block 1917]
དེས་ཐུན་མོང་གི་མ་ངེས་པ་ལྟར་སྣང་པའོ། །

[Block 1918]
ཕྱོགས་སྔ་མ་ལ་ལུས་ཅན་མ་ཡིན་པ་ཉིད་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་ཉིད་མ་ངེས་པ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1919]
དེ་ལྟ་བུ་ཉིད་དག་ནི་གྲུབ་པར་འདོད་པ་མཚུངས་པའི་ཕྱིར་འགལ་བ་མི་འཁྲུལ་བ་ཅན་བཞིན། གལ་ཏེ་བསམ་པ་འདི་ཡིན་ན་ནི་ཇི་ལྟར་ཁྱོད་ཀྱི་ཆོས་མཐུན་པ་ཙམ་ལས་གྲུབ་པ་དེ་བཞིན་ཁོ་བོའི་ཡང་ཡིན་ཏེ། དེས་ན་འགལ་བ་མི་འཁྲུལ་བ་ཅན་ལྟར་སྣང་བའོ། །

[Block 1920]
འདི་ཡང་རྗེས་འགྲོ་མེད་པའི་ཕྱིར། །དཔེ་ལྟར་སྣང་བའི་སྐྱོན་བརྗོད་ཡིན། །

[Block 1921]
རྣམ་པ་གཉིས་ཀ་ཡང་མ་ངེས་པ་ལྟར་སྣང་བ་སྟེ། གཏན་ཚིགས་དང་བསྒྲུབ་བྱའི་རྗེས་སུ་འགྲོ་བ་མ་བསྟན་པའི་ཕྱིར་དང་། བསྒྲུབ་བྱ་མེད་པའི་གཏན་ཚིགས་མེད་པར་མ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1922]
ཕྱོགས་ཕྱི་མ་ལ་ཡང་ཇི་ལྟ་བ་བཞིན་དུ་ཕྱོགས༌[^1517]སྔ་མ་ལ་ཡང་ཡིན་ནོ། །

[Block 1923]
དཔེ་ལྟར་སྣང་བའི་རྩོད་པ་ལ་ཡང་རྗེས་སུ་འགྲོ་བ་མེད་པར་སྦྱར་རོ། །

[Block 1924 [VERSE]]
རྗེས་འགྲོ་ཕྱིན་ཅི་ལོག་ཉིད་ལས། །
དཔེ་དང་བསྒྲུབ་བྱ་འདྲེས་པར་འགྱུར། །

[Block 1925]
ཕལ་ཆེར་ནི་རྟོག་གེ་ངན་པ༌[^1518]ཁོ་ན་དཔེས་ཉེ་བར་འཇལ་བར་བྱེད་དེ། སྒྲ་ནི་བུམ་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1926]
སྒྲ་ནམ་མཁའ་ལྟ་བུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1927]
དེར་དེ་ལྟར་འདྲེས་པ་ལ༌[^1519]ཕྱིན་ཅི་ལོག་ཡིན་ཀྱང་རྗེས་སུ་འགྲོ་བ་སྲིད་དེ། གང་མི་རྟག་པ་དེ་རྩོལ་བ་ལས་བྱུང་ངོ་ཞེས་བྱ་བ་དང་། གང་རྩོལ་བ་ལས་མ་བྱུང་བ་དེ་རྟག་པའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1928]
དེ་ལྟ་བུར་བྱས་པ་ལ་དེ་བཞིན་དུ་ཞེས་པ་དང་། དེ་བཞིན་དུ་མ་ཡིན་ནོ་ཞེས་མཇུག་བསྡུ་བར༌[^1520]བྱའོ། །

[Block 1929]
ཕྱོགས་ཕྱི་མ་ཇི་ལྟ་བ་བཞིན་དུ་ཕྱོགས་སྔ་མ་ཡང་ཡིན་པས་མཚུངས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། དེ་ལྟར་སྣང་བ་ཡང་འཐད་པ་ཡིན་ནོ། །

[Block 1930]
དཔེར༌[^1521]བསྟན་པ་ཙམ་ཉིད་ལ་ཕྱོགས་སྔ་མ་དང་ཕྱི་མ་གཉིས་ཀ་ཡང་རྗེས་སུ་འགྲོ་བ་ཕྱིན་ཅི་ལོག་ཏུ་མཚུངས་སོ། །
--- END BLOCKS ---
