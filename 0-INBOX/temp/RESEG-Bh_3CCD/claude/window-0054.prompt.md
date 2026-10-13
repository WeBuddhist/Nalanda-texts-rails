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
འདུས་པ་ཇི་ལྟ་བུ་ཞེ་ན། དཔལ་ལྡན་རྒྱུད་རྒྱལ་དམ་པ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱི་ཁྱད་པར་རོ། །

[Block 1892]
དཔལ་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1893]
དེ་དང་ལྡན་པས་ན་དཔལ་ལྡན་ནོ། །

[Block 1894]
དེ་བཞིན་དུ་ནི་དང་པོ་སྙིང་རྗེ་ཆེན་པོའི་སེམས་བསྐྱེད་ལ་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་གྱིས་སེམས་ཅན་མ་ལུས་པའི་དོན་བྱས་ཏེ་དེའི་རྗེས་ལ་ངག་ལ༌[^1299]སོགས་པ་རྣམ་པར་དག་པར་བྱེད་པ་རིམ་པ་ལྔའི་མཚན་ཉིད་ཡེ་ཤེས་ཀྱི་ཚོགས་མངོན་དུ་བྱའོ། །

[Block 1895]
ཡང་ན་དཔལ་ནི་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་སོགས་པ་བཞིའོ། །

[Block 1896]
དེ་ཉེ་བར་བསྟན་པ་ཡོད་པས་དཔལ་ལྡན་ནོ། །

[Block 1897]
དེ་ལྟར་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་དུས་སུ་རིགས་ངན་གྱི་བུ་མོ་ལ་སོགས་པ་ལས་དང་དམ་ཚིག་གི་ཕྱག་རྒྱ་མེད་པས་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱ་བསམས་ཏེ། བདེ་བ་ཆེན་པོའི་མཚན་ཉིད་ཅན་ཕྱག་རྒྱ་ཆེན་པོ་ཐོབ་པར་འགྱུར་ཞེས་བསྟན་ཏོ། །

[Block 1898]
རྒྱུད་ནི་སྤྱོད་པ་ལ་སོགས་པའི་རྒྱུད་དོ། །

[Block 1899]
དེ་རྣམས་ཀྱི་དམ་པའི་རྒྱལ་པོ་ནི་རྒྱལ་པོ་དམ་པ་སྟེ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་དོ། །

[Block 1900]
རྒྱུད་ཅེས་བྱ་བ་གང་ཞེ་ན། བཅོམ་ལྡན་འདས་ཀྱིས༌[^1300]རྒྱུད་ཕྱི་མ་ལས་གསུངས་ཏེ། རྒྱུད་ནི་རྒྱུན་ཞེས་བྱ་བ་སྟེ།

[Block 1901 [VERSE]]
རྒྱུན་དེ་རྣམ་པ་གསུམ་དུ་འགྱུར། །
གཞི་དང་རང་བཞིན་ཉིད་དང་ནི། །
འགྱུར་བ་མེད་པ་རབ་དབྱེ་བའོ། །
རང་བཞིན་རྣམ་པ་རྒྱུ་ཡིན་ཏེ། །

[Block 1902 [VERSE]]
དེ་བཞིན་འགྱུར་མེད་འབྲས་བུ་ཡིན། །
གཞི་ནི་ཐབས་ཞེས་བཤད་པ་སྟེ། །
གསུམ་གྱིས་རྒྱུད་ཀྱི་དོན་འདུས་སོ། །

[Block 1903]
ཞེས་འབྱུང་ངོ་། །དེའི་དགོངས་པ་ནི་རྒྱུའི་རྒྱུད་དང་འབྲས་བུའི་རྒྱུད་དང་ཐབས་ཀྱི་རྒྱུད་དོ། །

[Block 1904]
དེ་ལ༌[^1301]རྒྱུའི་རྒྱུད་ནི་གང་དུ་ཚངས་པའི་གནས་དང་རྣམ་པར་ཐར་པའི་སྒོ་ལ་སོགས་པའི་སྒོམ་པ་བསྟན་པའོ། །

[Block 1905]
འབྲས་བུའི་རྒྱུད་ནི་གང་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱ་ཆེན་པོ་ངེས་པར་བསྟན་པའོ། །

[Block 1906]
ཐབས་ཀྱི་རྒྱུད་ནི་གང་དུ་ཞི་བ་ལ་སོགས་པའི་ལས་ཀྱི་ཚོགས་ངེས་པར་བསྟན་པའོ། །

[Block 1907]
དོན་སོ་སོར་སྟོན་པར་བྱེད་པའི་རྒྱུད་རྣམས་ཀྱི་རྒྱལ་པོ་དམ་པའོ། །

[Block 1908]
དེ་ནས་ལས་འཛིན་པའི་བསྡུ་བ་བྱའོ། །

[Block 1909]
དེས་ནི་རྒྱུད་ཐམས་ཅད་ཀྱི་དམ་པ་ཉིད་ཉེ་བར་བསྟན་པ་ཡིན་ནོ། །

[Block 1910]
གལ་ཏེ་རྒྱུད་ཐམས་ཅད་ཀྱི་དམ་པ་ཡིན་ན། དེའི༌[^1302]ཚེ་དོན་ཟབ་མོ་དང་ལྡན་པའི་ཕྱིར་ཁྱོད་ཀྱིས་ཇི་ལྟར་བཤད་པར་ནུས་པ་ཞེ༌[^1303]ན། རྣལ་འབྱོར་རྒྱུད་རྣམས་ཀྱི༌[^1304]ལེགས་པར་བཤད་པ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཡན་ལག་དང་བཤད་པའི་རྒྱུད་སྔར་བཤད་པའོ། །

[Block 1911]
དེ་རྣམས་ཀྱི་ལེགས་པར་བཤད་པ་ནི་གསལ་བར༌[^1305]བཤད་ནུས་པའོ། །

[Block 1912]
ཤིན་དུ་གསལ་བར་རྣམ་པར་ཕྱེ་ཞེས་པ་ནི་དེ་རྣམས་ནི་ཁྱད་པར་རོ། །

[Block 1913]
བཤད་པ་ནི་དོན་གསལ་བར་རྟོགས་པའི་རྒྱུས་སོ། །

[Block 1914]
རྩ་བའི་རྒྱུད་ནི་བཤད་པའི་རྒྱུད་ཁོ་ནས་རྟོགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1915]
རྣལ་འབྱོར་གྱི་དོན་གང་ཞེ་ན། རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 1916 [VERSE]]
ཐབས་དང་ཤེས་རབ་མཉམ་སྦྱོར་བས། །
རྣལ་འབྱོར་ཞེས་ནི་མངོན་པར་བརྗོད། །
རང་བཞིན་མེད་པ་ཤེས་རབ་སྟེ། །
ཐབས་ནི་དངོས་པོའི་མཚན་ཉིད་དོ།[^1306] །

[Block 1917]
ཞེས་འབྱུང་ངོ་། །དེའི་དགོངས་པ་ནི་བསྐྱེད་པའི་རིམ་པས་སྙིང་རྗེ་ཆེན་པོ་སྔོན་དུ་འགྲོ་བར་བསྒོམ་པ་ནི་ཐབས་སོ། །

[Block 1918]
རྫོགས་པའི་རིམ་པ་གཉིས་པ་དང་བཞི་པ་དག་གིས་ཆོས་ཐམས་ཅད་རང་བཞིན་མེད་པའི་མཚན་ཉིད་ཅན་སྟོང་པ་ཉིད་སྒོམ་པ་ནི་ཤེས་རབ་བོ། །

[Block 1919]
དེ་དག་སྙོམས་པར་ཞུགས་པ་ནི་རྣལ་འབྱོར་རོ། །

[Block 1920]
ཡང་ན་སྔ་མ་བཞིན་དུ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་ནམ། །ཡང་ན་གང་དུ་ཕྱག་རྒྱའི་མཉམ་པར་སྦྱོར་བ་དགོངས་པ༌[^1307]དེ་ལ་དབང་པོ་གཉིས་ཀྱིས་མཉམ་པར་སྦྱོར་བ། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་འཇུག་པའི་མཚན་ཉིད་རྣལ་འབྱོར་ཞེས་བཤད་དོ། །

[Block 1921]
སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པའི་རིམ་པ་དག་ཏུ་བདེ་བ་ཆེན་པོ་བསྐྱེད་པའི་སླད་དུ་བསྒྲུབ་བྱ་དང་སྒྲུབ་བྱེད་ཀྱི་དབྱེ་བ་ལ་དམིགས་ཏེ། ཐབས་དང་ཤེས་རབ་ཉིད་དུ་འཇོག་པར་བྱས་པ་གཉི་ག་སྙོམས་པར་ཞུགས༌[^1308]པའི་མཚན་ཉིད་ནི་རྣལ་འབྱོར་ཞེས་བྱའོ། །

[Block 1922]
དེ་བཞིན་དུ་ཡང་བཤད་པའི་བྱེ་བྲག་གཞན་རྣམས་ཀྱང་འོག་ནས་སྐབས་སྐབས་སུ་འཆད་པར་འགྱུར་རོ། །

[Block 1923]
གལ་ཏེ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཁོ་ནས་རྩ་བའི་རྒྱུད་བཤད་པ་ཡིན་ན། དེའི་ཚེ་འགྲེལ་པ་བརྩམས་པས་ཅི་ཞིག་བྱ་ཞེ་ན། མཐའ་དྲུག་འཆིང་བ་རྣམས་ཀྱིས་བཅིངས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཐའ་དྲུག་ཅེས་བྱ་བའི་བཤད་པ་ནི། འོག་ནས་འཆད་པར་གྱུར་པ་དེ་ཉིད་འཆིང་བ་ནི་འབྲེལ་པའོ། །

[Block 1924]
དེས་བཅིངས་པ་ནི་བཅིངས་པ་སྟེ་དེའི་ཕྱིར་རྟོགས༌[^1309]པར་དཀའ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1925]
གང་གི་ཕྱིར་བཤད་པའི་རྒྱུད་ཀྱིས་ནི་རྩ་བའི་རྒྱུད་ཀྱི་ཚིག་དང་ངག་གི་དོན་ཙམ་སོ་སོར་བསྟན་པར་ནུས་ཀྱི་མཐའ་དྲུག་གི་བྱེ་བྲག་དང་རབ་ཏུ་དབྱེ་བ་བཤད་པར་མི་ནུས་སོ་ཞེས་འགྲེལ་པ༌[^1310]བྱ་བར་དོན་དང་ལྡན་ནོ། །

[Block 1926]
དེ་ལྟ་ན་འདུས་པའི་རྒྱན་ལ་སོགས་པ་གཞན་ཡོད་པས་འགྲེལ་པ་འདིས་ཅི་ཞིག་བྱ་ཞེ་ན། རྒྱལ་སྲས་ཡུལ་གྱུར་ཞེས་སྨོས་པ་ལ་རྒྱལ་བའི་སྲས་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་བྲལ་བས་ས་བཅུའི་དབང་ཕྱུག་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 1927]
དེ་རྣམས་ཀྱི་ཡུལ་དུ་གྱུར་པ༌[^1311]ནི་བཤད་པའི་སྤྱོད་ཡུལ་འདུས་པ་འདི་ཡིན་ཞེས་འདིས་བདག་ཉིད་མངོན་པར་ཤེས་པ་ཐོབ་པ་ཉིད་ཀྱིས༌[^1312]སྣོད་དུ་རུང་བ་ཉིད་དུ་བསྟན་པས༌[^1313]འགྲེལ་པ་བྱས་པ་སྟེ།[^1314] སྐྱེ་བོ་གཞན་གྱིས་འགྲེལ་པ་བྱེད་མི་ནུས་སོ། །

[Block 1928]
རྒྱུད་ཀྱི་མིང་བསྟན་པར་བྱ་བའི་ཕྱིར། རྒྱལ་བ་རྣམས་ཀྱི་འདུས་པ་གང་ཡིན་པ། །ཞེས་སྨོས༌[^1315]ཏེ། རྒྱལ་བ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པ་ལྔའོ། །

[Block 1929]
དེ་རྣམས་ཀྱི་འདུས་པ་ནི་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 1930]
དགོངས་པ་ནི་འདི་ལྟ་སྟེ། བསྐྱེད་པའི་རིམ་པའི་རིགས་བརྒྱའི་དབྱེ་བ་ཉེ་བར་བསྡུས་ཏེ། ཕུང་པོ་ལྔ་དང་ཉོན་མོངས་པ་དང་དབང་པོ་དང་ཡུལ་དང་། རྣམ་པར་ཤེས་པ་དང་འབྱུང་བ་དང་རླུང་རྣམ་པ་ལྔ་ལ་སོགས་པའི་རྣམ་པར་དག་པའི༌[^1316]བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་སྤྲོས་ཏེ། དེ་དག་གཅིག་ཏུ་གྱུར་པ་དག་གིས་མགྲིན་པ་གཅིག་གིས༌[^1317]
--- END BLOCKS ---
