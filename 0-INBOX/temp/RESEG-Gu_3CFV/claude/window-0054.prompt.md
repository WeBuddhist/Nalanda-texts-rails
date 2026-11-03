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
དེའི༌[^1200]ཕྱིར་ཉུང་ངུ་གཞན་ཡོད་པའི་རྫས་ཉིད་ལ་ནི་ཕལ་ཆེ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚིག་པ་རྣམས་ལ་ཐམས་ཅད་ཉིད་དོ། །

[Block 1892]
དེའི་ཕྱིར་འདིར་རྐོ་བ་དང་རྐོར་བཅུག་པ་དག་ལ་དངོས་གཞི་ཁོ་ན་སྟེ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1893]
ཚིག་པ་ཉིད་ནི་ཉམས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ས་ཉིད་ཚིག་པ་ཉིད་ནི་ཉམས་པ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1894]
སྨིན་པ་ཉིད་ནི་ས་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 1895]
ཉམས་པ་ཉིད་ལ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1896]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ས་ཚིག་པ་རྐོ་ན་ཉེས་བྱས་སོ། །

[Block 1897]
རྐོར་འཇུག་ན་ཉེས་བྱས་སོ། །

[Block 1898]
རྣམ་པར་ཉམས་པ་ཡང་དེ་བཞིན་ནོ༌[^1201]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1899]
ས་ཞག་དང་ངོགས་དང་རྩིག་པ་དང་དེའི་སྐྱང་ནུལ་གྲུགས་པ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་སྦྱར་རོ། །

[Block 1900]
དུས་གང་གི་ཚེ་སྐྱང་ནུལ་ཞེས་བྱ་བའི་སྒྲ་བརྗོད་པའོ། །

[Block 1901]
རྡོ་ཐལ་རྒྱུ་དང་བྱེ་མ་ལ་སོགས་པ་ཤས་ཆེ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1902]
བདུད་རྩིའི་སྦྱིན་པས་རྫས་ལྷག་མ་དག་ལ་སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་བསྙེགས་སོ། །

[Block 1903]
བྱ་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་ཕྱེད་ཉིད་དོ། །དེ་ཡང་གང་ཞེ་ན། དེའི་ཕྱིར་ཕུར་པ་འབྱིན་པ་དང་རི་མོ་འདྲེན་པ་དང་སའི་ཕྱེ་མ་འདྲེན་པའི་ལྕི་བ་འགོགས་པ་དང་འདམ་བསྐྱོད་པ་དང་། དེ་དང་འབྲེལ་པའི་ཕྲུ་བ་ལ་སོགས་པ་འདེགས་པ་དང་འཇིགས་པའི༌[^1202]བདག་ཉིད་ཀྱི་ཚ་སྒོ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕུར་པ་བཏབ་པ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་ལ་ཞེས་བྱ་བ་འདི་ལ་བཟུང་བས་འདིར་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 1904]
སའི་ཕྱེ་མ་འདྲེན་པའི་ལྕི་བ་འགོགས་པ་དེ་ནི་སའི་ཕྱེ་མ་འདྲེན་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1905]
དེ་དང་འབྲེལ་པའི་ཞེས་བྱ་བ་ནི་འདམ་རྫབ་དང་འབྲེལ་པ་བསྟན་པའོ། །

[Block 1906]
ཅི་བསམ་པ༌[^1203]གང་ཡང་རུང་བས་འདིར་དེ་དག་སྤྱད་ན་དེའི་མཐར་ཐུག་ཁ་ན་མ་ཐོ་བ་རྫོགས་པའམ་ཆུང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འདིར་གཞིག་པའི་བློ་དང་ལྡན་ན་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 1907]
ས་ལ་ཞེས་བྱ་བ་འདི་ལ་ཡང་དེ་འདིར་འཇུག་པ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 1908]
གང་གི་ཕྱིར་སྦ་བའི་བློས་ཕུར་བུ་དབྱུང་བ་ལ་སོགས་པའི་བྱ་བ་རྣམས་ལ་འདི་ནི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 1909]
དེའི་ཕྱིར་བགྲང་བ་དང་ཤོད་དགོད་པ་ལ་སོགས་པའི་བསམ་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། །གང་ལ་རྣམ་པར་སྦེད་པ་འདི་ལྟ་བུའི་འདི་ལྟ་སྟེ་ཕུར་བུ་དབྱུང་བའི་གླགས་མེད་པ་དེར་ཆོ་ག་འདི་ལ་ཞེས་བྱ་བ༌[^1204]རིག་པར་བྱའོ། །

[Block 1910]
ས་རྐོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1911]
ཧ་ཅང་བསླང་བར་མི་བྱའོ། །

[Block 1912]
མགྲོན་དུ་བོས་པའི་ཁྱིམ་དུ་གདུགས་ཚོད་བསྐུལ་བ་དེ་མེད་ན་འགྲོར་རུང་ངོ་ཞེས་བྱ་བ་ལ། རུང་ཞེས་བྱ་བ་ནི་འདིར་སློང་བའི་རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་མི་རུང་བར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། བྱ་བར༌[^1205]གྱུར་པ་དུས་ལས་ཡོལ་བར་ཁས་བླངས་པ་བཅག་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1913]
གང་དུ་བདག་གིས་གདུགས་བསྐུལ་བར་མི་ནུས་ཀྱི༌[^1206]རང་གིས༌[^1207]དུས་ཤེས་ནས་ཤོག་ཤིག༌[^1208]ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1914]
དུས་ལས་ཡོལ་དུ་བྱེད་ན་བྲིམས་ཤིག་ཅེས་བསྒོ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཞུ་བའི་དོན་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རིག་པར་བྱའོ། །

[Block 1915]
དེ་མེད་ན་ཞེས་བྱ་བ་ནི་དུས་ལས་ཡོལ་དུ་དོགས་པ་དེ་མེད་ནའོ། །

[Block 1916]
གདུགས་ཚོད་མ་བསྐུལ་བ་ཞེས་བྱ་བ་ལ། འདིར་གདུགས་ཚོད་བསྐུལ་བའི་ཁྱིམ་དུ་སྟེ། དེར་འགྲོར་རུང་བ་ནི་དུས་ལས་ཡོལ་དུ༌[^1209]བྱེད་པ་ཡོད་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1917]
དུས་ལས་ཡོལ་དུ་བྱེད་ན་བྲིམས་ཤིག་ཅེས་བསྒོ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མགྲོན་དུ་བོས་པའི་ཁྱིམ་དུ་སོན་པ་ན་གདུགས་ཚོད་ཡོལ་དུ་བྱེད་ན། གདུགས་ཚོད༌[^1210]བྲིམས་ཤིག་ཅེས་བསྐུལ་དུ་རུང་བ་ཉིད་ཡིན་པའོ། །

[Block 1918]
ཚིག་འབྲུ་དེ་ཉིད་མ་ཡིན་པ་ལ་གུས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཚིག་གང་རྣམས་ལ་སྔགས་ཉིད་ཀྱིས་བསྡུ་བ་མཛད་པ་དེ་རྣམས་ལ་དེ་ཉིད་ཀྱི་ཕྱིར་བསྡུ་བ་སྔགས་ཀྱིས༌[^1211]ངེས་པའི་སྐབས་ལ་བརྗོད་པས་འདི་ནི་མི་འཇུག་པར་རྟོགས་པར་བྱའོ། །

[Block 1919]
དོན་དེ་གོ་བར་བྱ་བའི་ཕྱིར། [^1212]བཅོམ་ལྡན་འདས་ཀྱིས་ཚིག་འབྲུ་གང་དུ་གསུངས་པ་དེ་ཉིད་མ་གཏོགས་པ་དེ་ལས་གཞན་ལ་གུས་པར་མི་བྱ་སྟེ། ཚིག་འབྲུ་དེ་ཉིད་ཀྱིས་དོན་དེ་ཉིད་བརྗོད་པར་བྱ་བ་མ་ཡིན་ཏེ། ཡོངས་སུ་རྫོགས་པ་དེའི་འདོད་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1920]
འདིར་གཞུང་ནི་སྟན་དག་ཅི་བདེར་གྱིས་ཤིག །ཚེ་དང་ལྡན་པ་ཁྱེད་ཀྱི༌[^1213]ཅི་བདེ་བ་ཞེས་བྱ་བ་ནི་བདག་གིས༌[^1214]མི་ཤེས་ཀྱི༌[^1215]འདི་ལྟར་སྟན་དག་ནི་ཁྱེད་ཁོ་ནའི་ཕྱིར་བཤམས་སོ་ཞེས་ཟེར་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་དེ་སྐད་ཟེར་ན་ཅི་བདེར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1921]
དེ་ལྟ་བུར་གྱུར་པ་ཐམས་ཅད་ལ་འདི་རྣམ་པར་གཞག་པ་དེའི་ཕྱིར་ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ཤེས་པའོ། །

[Block 1922]
སོ་སོར་མགྲོན་དུ་བོས་པ་བདག་གིར་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་མི་རུང་བར་ཤེས་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1923]
དགེ་འདུན་མགྲོན་དུ་བོས་པ་ནི་དེའི་ཁོངས་སུ་གཏོགས་པས་མགྲོན་དུ༌[^1216]བོས་པ་ཉིད་དོ། །

[Block 1924]
སྤྱན་དྲངས་པ་ཡོད་ན་ཁས་བླང་བར༌[^1217]མི་བྱ་སྟེ། དེ་ལྟ་བས་ན་མགྲོན་དུ་བོས་པ་མ་ཡིན་པ་ཉིད་ལ་དགེ་འདུན་གྱིས༌[^1218]སོ་སོར་མགྲོན་དུ་བོས་པ་བདག་གིར་བྱའོ། །

[Block 1925]
ཚུལ་འདི་ལྟ་བུ་བྱ་བར་འདོད་པ་ལ་འབྲེལ་པའི་དོན་དུ་གསུངས་པ་ནི། དགེ་འདུན་དང་བཅས་ཏེ་མགྲོན་དུ་བོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་སྤྱན་དྲངས་པ་ཡོད་ན་གང་ཟག་གིས་ཀྱང་མངོན་པར་མི་བརྟེན་པ་ནི་ཁྱད་པར་རོ། །

[Block 1926]
ཇི་ལྟར་གཙུག་ལག་ཁང་གི་ཁ་ཟས་ནི་གང་ཟག་མགྲོན་དུ་བོས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་འདིས་ཞེས་བྱ་བའི་ཚིག་འདིའོ། །

[Block 1927]
དུས་ཐམས་ཅད་དུ་ཡང༌[^1219]ཞེས་བྱ་བ་ནི་དགེ་འདུན་ནམ་གང་ཟག་ཇི་སྲིད་འཚོའི་བར་དུ་མགྲོན་དུ་བོས་ན་ཡང་བདག་གིར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1928]
ཅི་ཞིག་བྱས་ནས་མགྲོན་དུ་གཉེར་བ་ལས་རིང་དུ་འདུག་པའམ་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཚིག་རྣམ་པར་གཞག་པ་མེད་པར་མགྲོན་དུ་གཉེར་བ་དང་ལྡན་པ་ལ། ཕྱིས་གཞན་ནམ་ཡང་དང་ཡང་དུའམ་དུས་ཀྱི་མགྲོན་དུ་གཉེར་བར་མ་བྱས་པ་ཟླ་བ་བཞི་པ་ཡོངས་སུ་རྫོགས་པའི་འོག་ཏུ་བཤམས་པ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་དུས་འདི་ཙམ་དུ་རྟག་པ་ཉིད་དུ་ངེས་པ་རྣམ་པར་གཞག་ནས་ཁྱད་པར་དུ་དགེ་འདུན་གྱི་སྒོ་ནས་མགྲོན་དུ་གཉེར་བར་བྱེད་པ་རབ་ཏུ་སྦྱར་བའི་མགྲོན་དུ་གཉེར་བར་བྱས་པའམ། ཉེ་བར་སྤྱན་དྲངས་པར་གྱུར་པ་འདི་ལྟ་བུར་གྱུར་པའི་མགྲོན་དུ་བོས་པའི་འོག་ཏུ་དགེ་འདུན་ལ་གཞན་དུ་བྱས་པ་ཉིད་ལ་གང་ཟག་ལ༌[^1220]བྱས་པས་དགེ་འདུན་ལ་བྱས་པ་ཉིད་དོ། །

[Block 1929]
ཡང་དང་ཡང་དུའམ་ཤིན་ཏུ་དོན་ཉིད་ཀྱིས་མགྲོན་དུ་བོས་པ་བྱས་པ་ནི་ཟླ་བ་བཞིའི་མཐར་ཐུག་པའི་འོག་ཏུ་བཤམས་པ་རྣམ་པར་གཞག་པ་བྱས་པ་ནི༌[^1221]མགྲོན་དུ་གཉེར་བར་བྱས་པ་ཁ་ཟས་སུ་བྱས་པ་ཟ་བར་བྱེད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1930]
མགྲོན་དུ་གཉེར་བ་ལས་ལྷག་པར་གནས་པའི་ཁ་ན་མ་ཐོ་བ་འདི་དང་མགྲོན་དུ་མ༌[^1222]བོས་པའི་དོན་དུ༌[^1223]ཁ་ཟས་བསོད་པའི་ཁ་ན་མ་ཐོ་བའི་ཆོ་ག་འདི་གཉིས་ཀྱི་བྱེ་བྲག་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
