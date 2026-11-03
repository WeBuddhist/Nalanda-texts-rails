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
[Block 1856]
འདིར་བྱེད་པ་པོ་རྣམས་ལྷ༌[^1174]འདུ་ཤེས་ཡོངས་སུ་མ་རྫོགས་པ་ཉིད་ཡིན་ཡང་གྲགས་པའོ། །

[Block 1857]
ཇི་ལྟར་ཉི་ཤུ་མ་ལོན་པ་ཞིང་ཉིད་ཡིན་ཡང༌[^1175]ཞེ་ན། འདིར་རྣམ་པ་གཉིས་ཀྱིས༌[^1176]ཞིང་ཉིད་དུ་རྣམ་པར་གཞག་སྟེ་དངོས་པོ་དང་ཡིད་ཀྱིས་སོ། །

[Block 1858]
ཡང་དག་པར་ལན་པར༌[^1177]བྱེད་པའི་ཡིད་ཀྱི་དབང་གིས༌[^1178]ཞིང་ཉིད་ཡིན་ཏེ༌[^1179]འོན་ཏེ། གང་ཞིག་ལོ་ཉི་ཤུ་མ་ལོན་པ་ལ་ལོ་ཉི་ཤུ་ལོན་པར་འདུ་ཤེས་པར་གྱུར་ན་ལོ་ཉི་ཤུ་མ་ལོན་པ་ལ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1859]
ཆོ་ག་འདི་མི་ཤེས་ན་མཁན་པོས་མ་དྲིས་པའམ་དགེ་འདུན་གྱིས་ཀྱང་མ་དྲིས་པར་གྱུར་ན་དུས་དེ་ལ་གཏོགས་པ་ནི་མ་གྲགས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1860]
འོ་ན་འདི་ལ་ཚར་བཅད་པའི་བློས་ཡང་དག་པར་གནས་པ་མ་ཡིན་ནོ་ཞེ་ན། འོན་ཀྱང་བདེན་མོད་ཀྱི་ཚར་བཅད་པའི་བློ་ཡིས་ནི་མ་གྲགས་པ་ཡན་ལག་མ་ཡིན་ཏེ། འོན་ཀྱང་ཞིང་ཉིད་དོ། །

[Block 1861]
དེ་ལ་སྐྱེ་བ་ཡང་ཡོད་པར་འགྱུར་ཏེ། ཡོངས་སུ་རྫོགས་པའི་འདུ་ཤེས་ཉིད་ཡོད་པ་ལ་ཡང་ཞིང་ཉིད་དོ། །

[Block 1862]
འོ་ན་རྐུ་ཐབས་སུ་གནས་པ་བསྒྲུབས་པ༌[^1180]གང་ཡིན་ཞེ་ན། འདི་ནི་བསྙེན་པར་རྫོགས་པ་ཉིད་ལ་བསྐྱེད་པ་ཡིན་ནམ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་རྫོགས་པར་ཁས་བླངས་ཤིང་མ་གྲགས་པར་གཏོགས་པ་ལ་སྐྱེད་པ༌[^1181]ཡིན་ཏེ། །རྐྱེན་གྱི་དབང་ཉིད་མ་ཡིན་པ་ལ་མ་ཡིན་ཞེས་བྱ་བ་ཐམས་ཅད་ཉིད་དུ་ཆོ་ག་མ་བྱས་པ་ལ་རྟོགས་པ༌[^1182]ཉིད་ཀྱིས་འདི་བསྐྱེད་པར་རིག་པར་བྱའོ། །

[Block 1863]
གང་གི་ཕྱིར་གཞན་དུ་ན་བདག་ནི་དགེ་སློང་ངོ་སྙམ་དུ་དགེ་འདུན་གྱི་ནང་དུ་གཏོགས་པ་རྐུ་ཐབས་སུ་གནས་པ་མེད་པའི་ཕྱིར་རོ། །ཤེས་ན་ནི་དེ་ཞིག་གོ་ཞེས་བྱ་བ་ནི་ལོ་ཉི་ཤུ་མ་ལོན་པ་བསྙེན་པར་རྫོགས་པ་ལ་ལོ་ཉི་ཤུ་མ་ལོན་པར་ཤེས་ན་དེ་ལ་སྔར་སྡོམ་པ་འཆགས་པ་དེ་ཞིག་གོ། །ཅི་ཆོ་ག་དེ་ལ་གཅིག༌[^1183]ཏུ་ཟད་དམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་སྐྱེས་པ་ན་མ་ལོན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེས་ཞེས་བྱ་བ་ནི་ཤེས་པའོ། །

[Block 1864]
སྐྱེས་པ་ན་མ་ལོན་པའི་འོ་ཞེས་བྱ་བ་ནི་ཤེས་ན་ནི་ཡོད་པ་ཉིད་ཉམས་པའོ། །

[Block 1865]
ཡོངས་སུ་རྫོགས་པ་ཐོབ་པ་ལ་ནི་ཉམས་པ་ཉིད་དོ། །

[Block 1866]
ཅི་དང་པོ་མངལ་གྱི་སྒོ་ནས་བཙས་པ་དེ་ནས་བརྩམས་ཏེ་ཟླ་བ་ལྷག་པ་མེད་པར་སོ་སོར་བགྲང་བ་ལ་བསྙེན་པར་རྫོགས་པ་ཐོབ་པ་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མངལ་ན་གནས་པ་དང་ཤོལ་གྱི་ཟླ་བ་དག་དང་ཡང་བཅས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྙེན་པར་རྫོགས་པ་ཉིད་ལ་དེ་གཉིས་ཀ་བརྟེན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1867]
ལྟུང་བ་དེ་དང་བརྟེན་པས་བསྙེན་པར་རྫོགས་པར་མ་གྲགས་པས་ཤེས་པར་བྱ་བ་རིག་པར་བྱའོ། །

[Block 1868]
མངལ་ན་གནས་པའི་ཟླ་བ་དག་དང་ཤོལ་གྱི་ཟླ་བ་ལྷག་པ་དང་བཅས་ཏེ། དེའི་ལོ་ཉི་ཤུ་ཉིད་བརྩི་བར་བྱའོ། །

[Block 1869]
ལོ་མ་ལོན་པར་བསྙེན་པར་རྫོགས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1870]
གང་ལས་ས་རྐོ་བའི་ཁ་ན་མ་ཐོ་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྐོ་འམ་རྐོར་བཅུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྐོ་བ་ནི་རང་གིས་སོ། །

[Block 1871]
[^1184]རྐོར་བཅུག་པ༌[^1185]ནི་གཞན་ལའོ། །

[Block 1872]
གང་ཞིག་དེ་ཙམ་ཞིག་གིས་ཐ་དད་པར་བྱ་བ་གང་ཡིན་པ་ལ་འབྲས་བུ་ཉིད་ཀྱིས༌[^1186]རྣམ་པར་གཞག་པའོ། །

[Block 1873]
དེའི་ཕྱིར་འདི་ནི་ལན་རེ་བཏབ་པ་ལ་བྱ་བ་ཐ་དད་པར་རིག་པར་བྱའོ། །

[Block 1874]
འབྱིན་པ་ལ་ནི་སོ་སོར་འགུགས་པའོ། །

[Block 1875]
འབད་པ་གཞན་རབ་ཏུ་བསྒྲུབས་པས་འགུགས་པ་ཐ་དད་པའོ། །

[Block 1876]
གང་ཞིག་རྐོ་འམ་རྐོར་བཅུག་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་སའི་སའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སའི་རང་བཞིན་གྱིས་ས་ཡིན་གྱི་བྱེ་མ་དང་རྡོ་ཐལ་རྒྱུ་དང་རྡོ་ལ་སོགས་པའི་རང་བཞིན་གྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་འདི་དག་ཐམས་ཅད་དུ་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལག་གི་བླས་རྒྱུ་སྐར་གྱི༌[^1187]སྦྱོར་བས་རུང་བར་བྱེད་པ་མེད་ན་ཐུར་མ་སོར་བཞི་ཙམ་བཙུགས་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1877]
སའི་ས་ཇི་ལྟ་བུ་ཞིག་ལ་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ༌[^1188]རང་བཞིན་ཅན་དེ་ཡིན་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྲེལ་བར་གྱུར་པའི་གནས་སྐབས་རིགས་མ་ཡིན་པ་ལ་ཉེས་བྱས་འདི་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1878]
མ་འབྲེལ་པར་གྱུར་པའི་གནས་སྐབས་ལ་ནི་ལྟུང་བ་མེད་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1879]
རང་བཞིན་ཅན་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུ་ཞིག་ཡིན་རང་བཞིན་ཅན་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྔ་མ་ཤོས་ནི་ཟླ་བ་གསུམ་ལོན་པའི་འཐས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཐས་པ་ཞེས་བྱ་བ་ནི་འབྲེལ་པ་ཉམས་པ་རྣམས་ལ་དང་པོ་ཉིད་ཡན་ལག་རྣམས་ལ་འབྲེལ་པ་ཁས་ལེན་པར་འདོད་པ་དེ་ལྟ་བུར༌[^1189]གྱུར་པ་འདོད༌[^1190]པ་རྣམས་ལ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1880]
གང་གི་ཕྱིར་མ་འབྲེལ་པར་གྱུར་པ་ཉིད་ལ་འབྲེལ་པ་ཉིད་ཉམས་པས་ཀྱང༌[^1191]ཅུང་ཟད་ཀྱང་ཉམས་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 1881]
ཅི་སྟེ་གང་ནས་བརྩམས་ནས་འབྲེལ་པར་གྱུར་པ་ཉིད་རྟོགས་པར་བྱའོ། །

[Block 1882]
གང་ནས་བརྩམས་ཏེ་སར་པ་ཉིད་དགོད་པ༌[^1192]དང་ལྷན་ཅིག་ཏུ་སོ་སོར་སྨྲ་བ་སྔོན་གྱི་རང་བཞིན་ཅན་ལ་ཇི་ཙམ་དུ་དེའི༌[^1193]རྣམ་པའི་དུས་ལ་དེ་ཙམ་སོ་སོར་གནས་པ་འདི་རྟོགས་པར༌[^1194]བྱའམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཆར་ཆུ་ཞོད་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1883]
དུས་གཞན་གྱི་ཚེ་ཟླ་བ་དུ་ལོན་ན་རང་བཞིན་ཅན་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཚེ་ན་དྲུག་གོ། །

[Block 1884]
རྩིག་པ་ལ་ནི་ས་ཉིད་མ་ཡིན་པར་ཤེས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདིས་ནི་ཁང་ཐོག་ཀྱང་ས་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1885]
ས་ཕུང་ཡང་འབྲེལ་པ་ལ་འདིར་ས་གཞན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 1886]
འཐས་པར་གྱུར་ན་ནི་སའི་གོང་བུ་ཉིད་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1887]
ས་ཕུང་གལ་ཏེ་སྟེང་གི་ཆ་ནི་འཐས་པ་འོག་གི་ཆའི་ཡན་ལག་མ་འཐས་པར་གྱུར་ན་དེ་ནི་ས་ཉིད་མ་ཡིན་པར༌[^1195]ཤེས་པར་བྱའོ། །

[Block 1888]
སྔ་མ་འཐས་པར་གྱུར་ན་ནི་མཚུངས་པ་རྣམས་ལ་མཚན་ཉིད་རྣམས་ལ་རབ་ཏུ་བྱུང་བ་ཉིད་དོ། །

[Block 1889]
འདུས་པ་དག་ལ་ནི་ཤས་ཆེ་བས་མཚན་ཉིད་དག་རབ་ཏུ་འབྱེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། མཚན་ཉིད་དག་ལ་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་རང་གི་མཚན་ཉིད་རིགས༌[^1196]མི་མཐུན་པའི་རྫས་ཡོད་པར་གྱུར་ཀྱང་རྫས་ཀྱི༌[^1197]མཚན་ཉིད་གང་གི་ཆ་ཤས་ཆེ་བ་ཉིད་ནི་དེ་རྣམས་ཀྱིས༌[^1198]ཚོགས་པ་འདི་གཞག་པ་ཡིན་ཏེ་བསྟེན་པ༌[^1199]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1890]
གང་གི་ཕྱིར་ས་ལ་སོགས་པ་འདུས་པ་དག་ལ་རྫས་ཀྱི་རང་གི་མཚན་ཉིད་རྣམས་ནི་མང་བ་ཉིད་ཀྱིས་རྣམ་པར་གཞག་པའོ། །

[Block 1891]
དེའི༌[^1200]ཕྱིར་ཉུང་ངུ་གཞན་ཡོད་པའི་རྫས་ཉིད་ལ་ནི་ཕལ་ཆེ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚིག་པ་རྣམས་ལ་ཐམས་ཅད་ཉིད་དོ། །

[Block 1892]
དེའི་ཕྱིར་འདིར་རྐོ་བ་དང་རྐོར་བཅུག་པ་དག་ལ་དངོས་གཞི་ཁོ་ན་སྟེ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1893]
ཚིག་པ་ཉིད་ནི་ཉམས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ས་ཉིད་ཚིག་པ་ཉིད་ནི་ཉམས་པ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1894]
སྨིན་པ་ཉིད་ནི་ས་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 1895]
ཉམས་པ་ཉིད་ལ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
