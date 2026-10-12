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
དོན་ཡོད་པ་དང་མེད་པའི་ཐེ་ཚོམ་ནི་དཔེར་ན་རོ་ལངས་བསླང་བ་བཞིན་ནོ། །

[Block 1857]
དེ་ལ་དོན་དང་ལྡན་པ་ནི་འཇུག་པའི་ཡན་ལག་གོ། །

[Block 1858]
དོན་དང་མི་ལྡན་པ་དང་དོན་མེད་པ་དང་། ཡོད་པའི་ཐེ་ཚོམ་དག་ནི་ལྡོག་པའི་ཡན་ལག་གོ། །

[Block 1859]
འདིར་ནི་དང་པོའི་ཚིག་ཚད་མ་མེད་པ་ལས་ཅི་འདིར་བརྗོད་པ་ལ་སོགས་པ་ཡོད་དམ་མེད་ཅེས་ཐེ་ཚོམ་ལ་འཇུག་པར་འགྱུར་ཏེ། དེའི་རྗེས་སུ་རིམ་པ་གཉིས་ཀྱིས་མཚོན་པའི་བརྗོད་པར་བྱ་བ་དང་། དེ་རྗོད་པར་བྱེད་པའི་ཚིག་གི་ཚོགས་དང་དེ་དག་གི་འབྲེལ་པ་ཡང་ཐོས་ནས་བསམ་པ་དང་བསྒོམ་པའི༌[^1278]རིམ་པས་ཐ་མལ་པའི་ལུས་བཟློག་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་རྡོ་རྗེའི་སྐུའི་མཚན་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྲིན་ལས་ཐམས་ཅད་པ་ཐོབ་ནས། དེའི་རྗེས་ཐོགས་སུ་འགྲོ་བ་ཐམས་ཅད་ཀྱང་རྡོ་རྗེ་འཛིན་པར་བྱེད་པ་ནི་དགོས་པའི་དགོས་པ་ཡང་ལ་ལ་ཡོད་པར་འདོད་པས་བསྟན་བཅོས་འདི་ལེགས་ཞེས་མགུ་ཞིང་བྱ་བ་བྱས་པར་འགྱུར་རོ། །

[Block 1860]
དེའི་ཕྱིར་དོན་གྱི་ཐེ་ཚོམ་ལས་འཇུག་པ་ནི་རིགས་པ་ཁོ་ནའོ། །

[Block 1861]
གཞན་དག་གིས་ཀྱང་ཁྱབ་པར་བྱེད་པ་མི་དམིགས་པས་རྒོལ་བར་བྱེད་པ་གང་ཡིན་པ་དེའི་གཏན༌[^1279]ཚིགས་མ་གྲུབ་པ་ཡིན་ཞེས་སྨྲ་བར་བྱ་བའི་ཕྱིར། བརྗོད་པ་ལ་སོགས་པའི་མཚན་ཉིད་འཆད་པར་འགྱུར་རོ། །

[Block 1862]
[^1280]

[Block 1863]
འདིར་འབྲེལ་པ་རྩོམ་པའི་དུས་སུ་སློབ་དཔོན་ཟླ་གྲགས་རང་འདོད་པའི་ལྷ་ལ་ཕྱག་འཚལ་བ༌[^1281]རྩོམ་པ༌[^1282]བྱེད་དེ། དེ་ལ་རྣམ་པ་གསུམ་སྟེ། མཐུན་པ་དང༌[^1283]རྗེས་སུ་མཐུན་པ་དང་གཉི་གའི་རྗེས་སུ་འགྲོ་བའོ། །

[Block 1864]
དེ་ལ་མཐུན་པ་ཞེས་བྱ་བ་ནི་གང་བསྟན་བཅོས་དང་མི་འགལ་བ་ཡིན་གྱི་བསྟན་བཅོས་མཁན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 1865]
འདི་ལྟ་སྟེ། དཔལ་གྱི་ཕུན་སུམ་ཚོགས་པའི་ས༌[^1284]ལས་འདས་ཞེས་བྱ་བ་ལ་སོགས་པ་སོ་སོར་ཐར་པའི་རབ་ཏུ་བྱེད་པའི་དང་པོ་བཅོམ་ལྡན་འདས་འདོད་ཆགས་དང་བྲལ་བ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 1866]
རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་ནི་བསྟན་བཅོས་དང་མི་འགལ་བ་ཡིན་ཏེ། བསྟན་བཅོས་མཁན་གྱི་མངོན་པར་འདོད་པ་ཁོ་ནའོ། །

[Block 1867]
འདི་ལྟ་སྟེ།

[Block 1868 [VERSE]]
ངག་ནི་རྟོགས་པར་བྱེད་པ་མཆོག །
འཇིག་རྟེན་མགོན་པོ་ལ་བཏུད་ནས། །

[Block 1869]
ཞེས་སྣང་བའི་ཕྲེང་བའི་འབྲེལ་པ༌[^1285]

[Block 1870]
དང་པོ་ལ་ཕྱག་འཚལ་བ་བཞིན་ནོ། །

[Block 1871]
དེ་ལ་ནི་བསྟན་བཅོས་ཀྱི་བརྗོད་པར་བྱ་བ་དང་མཐུན་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་འགྲེལ་པ་མཁན་གྱི་ཡི༌[^1286]དམ་ཡིན་པས་རྗེས་སུ་མཐུན་པའོ། །

[Block 1872]
གཉི་གའི་རྗེས་སུ་འགྲོ་བ་ནི་གང་བསྟན་བཅོས༌[^1287]དང་བསྟན་བཅོས་མཁན་པོ་དག་གིས༌[^1288]བརྗོད་པར་བྱ་བ་དང་མངོན་པར་འདོད་པས་གཉི་གའི་རྗེས་སུ་འགྲོ་བའོ། །

[Block 1873]
གཞན་ཡང་འདི་ལྟ་སྟེ། ཁམས་གསུམ་སྤྱོད་པ་ལས་གྲོལ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཕྱག་འཚལ་བའི་ཚིག་ལ་བརྗོད་པར་བྱ་བ་དང་། རང་འདོད་པའི་ལྷ་གཉི་གའི་རྗེས་སུ་འགྲོའོ།[^1289] །

[Block 1874]
དེ་ལྟར་འདིར་ཡང་དཔལ་རྡོ་རྗེ་སེམས་དཔའ་ལ་ཕྱག་འཚལ་བ་ནི་སློབ་དཔོན་ཟླ་བ་གྲགས་པའི་དེ་ཉིད་རང་འདོད་པའི་ལྷ་ཡིན་ཏེ། དཔལ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་ཀྱིས༌[^1290]འདོད་པ་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1875]
སྒྲོན་མ༌[^1291]གསལ་བར་བྱེད་པ་ལས་ཀྱང་། དེ་ཉིད་བརྗོད་པར་བྱ་བ་ཡིན་ཏེ། །ཏིང་ངེ་འཛིན་ཐམས་ཅད་ཀྱི་སྒོ་ནས་དེ་ཉིད་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1876]
རྗོད་པ་དང་བརྗོད་པར་བྱ་བའི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོའི༌[^1292]ཡིན་ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 1877]
དེའི་ཕྱིར༌[^1293]ཕྱག་འཚལ་བ་གཉི་གའི་རྗེས་སུ་འགྲོ་བ་འདི་ཡིན་ནོ། །

[Block 1878]
དེ་ལྟར༌[^1294]ན་ཕྱག་འཚལ་བ་བྱས་པས་ཅིར་འགྱུར། བགེགས་ཉེ་བར་ཞི་བར་འགྱུར་ཞེས་རིགས་པ་གང་ཞིག་ཡོད་ཅེ་ན། ཕྱག་འཚལ་བ་བྱས་པས་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཡོན་ཏན་བརྗོད་པ་ལས་སྐྱེས་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱིས༌[^1295]བསོད་ནམས་མ་ཡིན་པ་ལོག་པར་འགྱུར་རོ། །

[Block 1879]
བསོད་ནམས་མ་ཡིན་པ་ལས་སྐྱེས་པའི་བགེགས་བསོད་ནམས་ཉེ་བར་དམིགས་པས་དེ་དག་མེད་དོ་ཞེས་དགག་པར༌[^1296]བྱ་བའི་རྒྱུ་འགལ་བ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1880]
ཕྱག་འཚལ་བ་དེ་ཡང་ལ་ལས་རྣམ་པ་བཞི་རུ་འདོད་དེ་ལུས་དང་ངག་དང་ཡིད་དང་བླ་ན་མེད་པའི་མཆོད་པས་ཕྱག་འཚལ་བའོ། །

[Block 1881]
དེ་ལ་ལུས་ཀྱིས་ནི༌[^1297]ཡན་ལག་ལྔ་པའི་ཕྱག་གོ། །

[Block 1882]
ངག་གིས་ནི་དེའི་ཡོན་ཏན་གྱི་ཚོགས་བརྗོད་པའི་མཚན་ཉིད་དོ། །

[Block 1883]
ཡིད་ཀྱིས་ནི་དེ་ཉིད་རྗེས་སུ་དྲན་པའོ། །

[Block 1884]
བླ་ན་མེད་པའི་མཆོད་པའི་ཕྱག་འཚལ་བ་ནི་དེའི་བདག་ཉིད་རྗེས་སུ་འཇུག་པའོ། །

[Block 1885]
རབ་ཏུ་བྱེད་པ་ལས།

[Block 1886 [VERSE]]
ཇི་ལྟར་ཆུ་ལ་ཆུ་བཞག་དང་། །
ཇི་ལྟར་མར་ལ་མར་བཞིན་དུ། །
རང་གིས་རང་གི་ཡེ་ཤེས་ནི། །
ལེགས་མཐོང་གང་ཡིན་འདིར་ཕྱག་ཡིན། །

[Block 1887]
ཞེས་དེ་ལྟ་བུའི་ཕྱག་འཚལ་བ་ཡང་འདིར་འདུས་པ་ཁོ་ནའོ། །

[Block 1888]
[^1298]

[Block 1889]
ད་ནི་ཕྱག་འཚལ་བ་བཤད་པར་བྱ་སྟེ། དཔལ་ལྡན་རྒྱུད་རྒྱལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའ་ལ་ཕྱག་འཚལ་ནས། སློབ་དཔོན་ཟླ་བ་གྲགས་པས་འདུས་པ་ནི་གསང་བ་འདུས་པ་ཞེས་བྱ་བའི་རྒྱུད་དོ། །

[Block 1890]
རབ་གསལ་ཞེས་བྱ་བ་ནི་གསལ་བར་བྱེད་པའོ། །

[Block 1891]
འདུས་པ་ཇི་ལྟ་བུ་ཞེ་ན། དཔལ་ལྡན་རྒྱུད་རྒྱལ་དམ་པ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱི་ཁྱད་པར་རོ། །

[Block 1892]
དཔལ་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1893]
དེ་དང་ལྡན་པས་ན་དཔལ་ལྡན་ནོ། །

[Block 1894]
དེ་བཞིན་དུ་ནི་དང་པོ་སྙིང་རྗེ་ཆེན་པོའི་སེམས་བསྐྱེད་ལ་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་གྱིས་སེམས་ཅན་མ་ལུས་པའི་དོན་བྱས་ཏེ་དེའི་རྗེས་ལ་ངག་ལ༌[^1299]སོགས་པ་རྣམ་པར་དག་པར་བྱེད་པ་རིམ་པ་ལྔའི་མཚན་ཉིད་ཡེ་ཤེས་ཀྱི་ཚོགས་མངོན་དུ་བྱའོ། །

[Block 1895]
ཡང་ན་དཔལ་ནི་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་སོགས་པ་བཞིའོ། །
--- END BLOCKS ---
