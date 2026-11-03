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
ཞེས་བྱ་བ་འདིས་ནི་སེམས་ཅན་གྱི་དོན་བྱ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1892]
མཐུན་པ་དང་གུས་པ་དང་ཡོ་བྱད་ཀྱིས་ཞེས་བྱ་བ་ལ། མཐུན་པ་ཞེས་བྱ་བ་ནི་དེས་པའོ། །

[Block 1893]
ཡང་ན་དམན་པའི་ཚུལ་ཉིད་དོ། །

[Block 1894]
ཡང་ན་བྱས་པ་གཟོ་བ་ཉིད་དོ། །

[Block 1895]
གུས་པ་ནི་དུལ་བའོ། །

[Block 1896]
མཐུན་པ་དང་གུས་པའི་ཡོ་བྱད་ནི་མཐུན་ཞིང་གུས་པའི་ཡོ་བྱད་དོ། །

[Block 1897]
དེ་མཉེན་པར་གྱུར་པ་ནི་མཐུན་པ་དང་གུས་པའི་ཡོ་བྱད་ཀྱིས་མཉེན༌[^1108]པར་གྱུར་པའོ། །

[Block 1898]
གཟེངས་བསྟོད་པ་ལས་བརྩམས་ནས་མངོན་པར་འཕེལ་བའོ། །

[Block 1899]
སྙིང་རྗེའི་སྡུག་བསྔལ་བ་ལ༌[^1109]ཡང་བརྗོད་པར་བྱ་སྟེ། འདི་ལྟར་སྙིང་རྗེའི་དབང་གིས་རང་གི་ཤ་དང་ཁྲག་ཀྱང་ཡོངས་སུ་གཏོང་བར་བྱེད་པས་སོ། །

[Block 1900]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བྱམས་པའི་སྟོབས་ཀྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 1901 [HEADING]]
## ཐམས་ཅད་སྒྲོལ་གྱི་སྐྱེས་པའི་རབས། ^9-0

[Block 1902]
དབང་པོ་ཐུལ་བ་གོམས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི༌[^1110]སོ་སོར་བརྟགས་པས༌[^1111]བྱས་པ་མ༌[^1112]ཡིན་པའི་ཕྱིར་དབང་པོ་སྦས་པ་ལ།[^1113] དབང་པོ་ཐུལ་བ་ལ་གོམས་པར་གྱུར་པ་ཉིད་དོ། །

[Block 1903]
ཅིའི་ཕྱིར་དབང་པོ་ཐུལ་བ་ལ་གོམས་པར་གྱུར་པ་འདིར་ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་རིམ་པ་དང་འགལ་བར་དང་པོར་བརྗོད་ཅེ་ན། ལུགས་ཀྱི་བསྟན་བཅོས་དེ་ནི་གཞོན་ནུའི་རིམ་པ་བསྟན་པ་དང་། རིགས་པ༌[^1114]དང་། རྒན་པ་ལ་བརྟེན་པའི༌[^1115]རིམ་པ་ཡིན་ལ། འདིར་ནི་རྒྱལ་པོ་དང་། རྒྱལ་བུ་རྣམས་ཀྱི་གཙོ་བོར་གྱུར་པའི་ཡོན་ཏན་དབང་པོ་ཐུལ་བ་ཉིད་ཡིན་ཏེ། རིགས་པ༌[^1116]དང་རྒན་པ་ལ་བརྟེན་པ་ལ་སོགས་པའི་འབྲས་བུར་གྱུར་པ་ནི་དབང་པོ་ཐུལ་བ་ཡིན་ཏེ། དེ་བས་ན་འདི་བསྟན་ཏོ། །

[Block 1904]
དཔའ་བ་དང་ཚུལ་ཕུན་སུམ་ཚོགས་པ་ནི་སྤྲོ་བ་དང་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །

[Block 1905]
རྣམ་པར་རྒྱལ་བའི་དབང་ཐོབ་པ། །ཞེས་བྱ་བས༌[^1117]ནི། གཙོ་བོའི་ནུས་པ་བསྟན་ཏོ། །

[Block 1906]
རྣམ་པར་རྒྱལ་བ་ཉིད་ནི༌[^1118]དཔལ་ཡིན་པས་རྣམ་པར་རྒྱལ་བའི་དཔལ་ལོ། །

[Block 1907]
རྣམ་པར་རྒྱལ་བའི་དཔལ་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི། རྣམ་པར་རྒྱལ་བའི་དཔལ་ཐོབ་པའོ། །

[Block 1908]
ཡང་ན་ཕ་རོལ་གནོན་པ་བསྟན་ཏོ། །

[Block 1909]
གང་གི་ཚུལ་དང་དུལ་བ་ཕུན་སུམ་ཚོགས་པས་བསྟན་པ་ནི༌[^1119]རྒྱལ་སྲས་སོ། །

[Block 1910]
རྒན་པ་ལ་བསྙེན་བཀུར་ངེས་པར་བྱས་པས། ཞེས་བྱ་བ་ནི། རིགས་པས༌[^1120]རྒན་པ་ལ་བརྟན་པའི༌[^1121]ཕྱིར་རོ། །

[Block 1911]
རྒན་པ་ལ་བསྙེན་བཀུར་ཉིད་ངེས་པ་ཡིན་ཏེ། དེ་བས་ན་རྒན་པ་ལ་བསྙེན་བཀུར་པར༌[^1122]བྱེད་པ་ངེས་པའོ། །

[Block 1912]
རིག་བྱེད་གསུམ་པ་ཞེས་བྱ་བ།[^1123]

[Block 1913]
གསུམ་པ་ནི་ངེས་བརྗོད་དང་། སྙན་ཚིག་དང་། མཆོད་སྦྱིན་གྱི་རིག་བྱེད་དོ། །

[Block 1914]
[^1124]ཡང་ན་སྲིད་སྲུང་གི་རིག་བྱེད་དང་། ཡང་ན༌[^1125]དེ་ལྟ་བུ་འབྱུང་བ་ཡང་རིག་བྱེད་དོ། །

[Block 1915]
བསྟན་པ༌[^1126]ནི་གྲངས་ཅན་དང་། རྣལ་འབྱོར་པ་དང་། འཇིག་རྟེན་རྒྱང་འཕེན་པ༌[^1127]བརྟག་པའོ། །

[Block 1916]
དོན་གྱི་དེ་ཁོ་ན་ཉིད་ཁོང་དུ་ཆུད་པས༌[^1128]ཞེས་བྱ་བ་ནི་དེའི་གྲུབ་པའི་མཐའ་མངོན་པར་རྟོགས་པའོ། །

[Block 1917]
འདི་ནི་མཆོད་སྦྱིན་ལ་སོགས་པའི་བྱ་བ་མི་བྱེད་པར་བསྟན་ཏོ། །

[Block 1918]
རང་གི་ཆོས་དང་ལས་ལ་འབད་པ་ཞེས་བྱ་བ་ནི་གནས་དང་། ལས་དང་། རིགས་ཀྱིའོ། །

[Block 1919]
ཡང་ན་ཐམས་ཅད་ཀྱི་ལས་ཀྱི་འཚོ་བའོ། །

[Block 1920]
ཆོས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བྱ་པའོ། །

[Block 1921]
ཡིད་མ་བྱུང་ཞིང་བདེ་བར་འཚོ་བ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་མེད་པས་ཡིད་སྐྱོ་བ་མེད་པའོ། །

[Block 1922]
ཡང་ན་སྐྱོ་བ་མེད་པ༌[^1129]ནི་འཚེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1923]
བདེ་བར༌[^1130]འཚོ་བ་ནི་ལོ་ལེགས་པ་ལ་སོགས་པའི༌[^1131]ཡོན་ཏན་དང་ལྡན་པས་སོ། །

[Block 1924]
སྙིང་ཉེ་བ་ནི༌[^1132]རྒྱལ་པོའི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པས་སོ། །

[Block 1925]
བཀའ་ཁྲིམས་ནི་དོན་གྱི་བསྟན་བཅོས༌[^1133]སོ། །

[Block 1926]
འཚོ་ཚིས་ཀྱི་བྱ་བ་ལེགས་པར་འབྱོར་པ་ནི་ཞིང་ལས་དང་། བསྲུང་བ་དང་། ཚོང་ལ་སོགས་པ་འཚོ་ཚིས་ཞེས་བརྗོད་དོ། །

[Block 1927]
དཔའ་བ་ཕུན་སུམ་ཚོགས་པའི་རྣམ་པར་རྒྱལ་བའི་དཔལ་ཐོབ་པ་དང་ཞེས་བྱ་བ་འདིས་ནི༌[^1134]མ་ཐོབ་པ་འཐོབ་པར༌[^1135]བསྟན་ཏོ། །

[Block 1928]
རང་གི་ཆོས་དང་ལས་དང་འབད་པ་དང་ཡིད་མ་བྱུང་ཞིང་བདེ་བར་འཚོ་བ་དང་། འཚོ་ཚིས་བྱས་པ་ལེགས་པར་འབྱོར་པ་ཞེས་བྱ་བ་དག་གིས་ནི་རྣམ་པར་འཕེལ་བ་བསྟན་ཏོ། །

[Block 1929]
ཡོན་ཏན་ལྡན་པས་ཞེས་བྱ་བས་ནི་ཐོབ་པ་རྣམ་པར་སྤེལ་བ་དང་། ཡོངས་སུ་བསྲུང་བ༌[^1136]དབང་དུ་བྱས་པའོ། །

[Block 1930]
ཡོན་ཏན་དང༌[^1137]ལྡན་པས༌[^1138]ཞེས་བྱ་བའི་ཕྱེད་ཀྱིས་ནི༌[^1139]ཡོན་ཏན་དང་ལྡན་པ་དེས་རང་བཞིན་གྱིས་ཉམས་པ་མེད་པ་བསྟན་ཏེ། དེས་ན་ཡང་དེ༌[^1140]བསྲུང་བར་འགྱུར་བ་ཡིན་ཏེ། འདིས༌[^1141]ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
