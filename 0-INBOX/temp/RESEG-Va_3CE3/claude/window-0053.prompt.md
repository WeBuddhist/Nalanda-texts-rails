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
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང༌[^1268]དམིགས་སུ་མ་མཆིས་ཏེ་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1857]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་གཟུགས་ཀྱང་མི་དམིགས་ཞེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 1858]
བཅོམ་ལྡན་འདས་འོ་ན་སུའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་པའོ། །

[Block 1859]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་མ་བགྱིས་པ༌[^1269]སྟེ། མངོན་པར་འདུས་མ་བགྱིས་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1860]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་སྤྱན་ལྔས་ཀྱང་ཞེས་པ༌[^1270]ནི་དགུ་པའོ། །

[Block 1861]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ༌[^1271]དོན་དམ་པ་ལ་བཞུགས་ཏེ་ཞེས་བྱ་བ་ནི་བཅུ་པའོ། །

[Block 1862]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་སྤྲུལ་པ་ལྟ་བུ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅུ་གཅིག་པའོ། །

[Block 1863]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དེ་བཞིན་གཤེགས་པ་མི་བཞུགས༌[^1272]ན་ཞེས་བྱ་བ་ནི་བཅུ་གཉིས་པའོ། །

[Block 1864]
བཅོམ་ལྡན་འདས་གལ་ཏེ་སྤྲུལ་པ་དང་དེ་བཞིན་གཤེགས་པ་ལ་ཁྱད་པར་མ་མཆིས་ན་ཞེས་བྱ་བ་ནི་བཅུ་གསུམ་པའོ། །

[Block 1865]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད་རྣམ་པར་དཀྲུག༌[^1273]པར་མི་བགྱི་བ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅུ་བཞི་པའོ། །

[Block 1866]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཞན་རྣམས་ཁོང་དུ་ཆུད་པར་བགྱི་བའི་སླད་དུ། བཅོམ་ལྡན་འདས་ཀྱིས་མིང་དང་མཚན་མས་ཞེས་བྱ་བ་ནི་བཅྭ་ལྔ་པའོ། །

[Block 1867]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་མིང་དང་མཚན་མ་ཙམ་དུ་བས་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅུ་དྲུག་པའོ། །

[Block 1868]
བཅོམ་ལྡན་འདས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ༌[^1274]རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ༌[^1275]ཉིད་ཅེས་གསུང་ངམ་ཞེས་བྱ་བ་ནི་བཅུ་བདུན་པའོ། །

[Block 1869]
བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ༌[^1276]ཉིད་འདི་གསུམ༌[^1277]ཁྱད་ཅི་ཞིག་མཆིས་ཞེས་བྱ་བ་ནི་བཅོ་བརྒྱད་པའོ། །

[Block 1870]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བགྱི་ཞེས་བྱ་བ་ནི་བཅུ་དགུ་པའོ། །

[Block 1871]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ལ་ནི་ལམ་གྱི་རྣམ་པ༌[^1278]ཤེས་པ་ཉིད་ཅེས་བགྱི་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་པའོ། །

[Block 1872]
ཅིའི་སླད་དུ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ལ་ནི་ཐམས་ཅད་ཤེས་པ་ཉིད་ཅེས་བགྱི་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གཅིག་པའོ། །

[Block 1873]
བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ་ཉིད་འདི་གསུམ་ལས་འདིའི་སྤོང་བ་ནི་ལྷག་མ་དང་བཅས་པའོ། །

[Block 1874]
འདིའི་སྤོང་བ་ནི་ལྷག་མ་མ༌[^1279]མཆིས་པའོ་ཞེས་བགྱི་བར་ཉོན་མོངས་པ་སྤོང་བ་ལ་ཐ་དད་དུ་བགྱི་བ་མ་མཆིས་སམ་ཞེས་བགྱི་བ༌[^1280]ནི་ཉི་ཤུ་གཉིས་པའོ། །

[Block 1875]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དེ་དག་ཐམས་ཅད་ཀྱིས་འདུས་མ་བགྱིས་མ་ཐོབ་པར་ཉོན་མོངས་པ་སྤངས་སམ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གསུམ་པའོ། །

[Block 1876]
བཅོམ་ལྡན་འདས་འདུས་མ་བགྱིས་པ༌[^1281]ལ་བྱེ་བྲག་དམིགས་སུ་མ༌[^1282]མཆིས་སམ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བཞི་པའོ། །

[Block 1877]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དམིགས་སུ་མ་མཆིས་ན་ཅིའི་སླད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ༌[^1283]ཞེས་བྱ་བ་ནི་ཉི་ཤུ་ལྔ་པའོ། །

[Block 1878]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ལམ་ལ་གནས་ཏེ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དྲུག་པའོ། །

[Block 1879]
སྐབས་འདིར་བར་སྐབས་སུ་ཞུས་པ་བཞིའོ། །

[Block 1880]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ལམ་ཡང་དངོས་པོ༌[^1284]མ་མཆིས་ལ་མྱ་ངན་ལས་འདས་པ་ཡང་དངོས་པོ༌[^1285]མ་མཆིས་ན་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བདུན་པའོ། །

[Block 1881]
བཅོམ་ལྡན་འདས་ཅི་ལགས་འདུས་མ་བགྱིས་པ༌[^1286]འདི་ནི་རྒྱུན་དུ་ཞུགས་པའོ་ཞེས་རབ་ཏུ་བྱེད་པ་ལགས་སོ་ཞེས༌[^1287]བྱ་བ་ནི་ཉི་ཤུ་བརྒྱད་པའོ། །

[Block 1882]
བཅོམ་ལྡན་འདས་འཁོར་བའི་ཕྱི་མའི་མཐའ་ཇི༌[^1288]ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དགུ་པའོ། །

[Block 1883]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་ན་ཞེས་བྱ་བ་ནི༌[^1289]སུམ་ཅུ་པའོ། །

[Block 1884]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བགྱི་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གཅིག་པའོ། །

[Block 1885]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དོན་དང་ཚུལ་གྱིས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གཉིས་པའོ། །

[Block 1886]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་དོན་ཀྱང་མི་བགྱིད་དོན་མ་ལགས་པ་ཡང་མི་བགྱིད་ལགས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གསུམ་པའོ། །

[Block 1887]
བཅོམ་ལྡན་འདས་འོ་ན་འདུས་མ་བགྱིས། འཕགས་པ་ཐམས་ཅད་ཀྱི་དོན་མ་ལགས་སམ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བཞི་པའོ། །

[Block 1888]
བཅོམ་ལྡན་འདས་འོ་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་འདུས་མ་བགྱིས་ཀྱི་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་ལྔ་པའོ། །

[Block 1889]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཉིས་སུ་མ་མཆིས་པའི་ཆོས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དྲུག་པའོ། །

[Block 1890]
སྐབས༌[^1290]འདིར་བར་སྐབས་སུ་ཞུས་པ་གསུམ་པའོ། །

[Block 1891]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སེམས་དང་པོ་བསྐྱེད་པ་དང་ལྡན་པ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འཚལ་བ་དེ༌[^1291]བསོད་ནམས་ཇི་ཙམ་ཞིག་བསྐྱེད་པར༌[^1292]འགྱུར་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བདུན་པའོ། །

[Block 1892]
བཅོམ་ལྡན་འདས་སེམས་དང་པོ་བསྐྱེད་པས་ཅི་ཞིག༌[^1293]ཡིད་ལ་བགྱི་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བརྒྱད་པའོ། །

[Block 1893]
བཅོམ་ལྡན་འདས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི༌[^1294]དམིགས་པ་ཇི༌[^1295]ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དགུ་པའོ། །

[Block 1894]
བཅོམ་ལྡན་འདས་ཅི་ལགས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་འབའ་ཞིག་དངོས་པོ་མ་མཆིས་པ་ལགས་སམ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་པའོ། །

[Block 1895]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ངོ་བོ་ཉིད་མ་མཆིས་པ་ལགས་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཅིག་པའོ། །
--- END BLOCKS ---
