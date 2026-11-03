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
[Block 1926]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཅིག་པའོ། །

[Block 1927]
བཅོམ་ལྡན་འདས་དངོས་པོ་ཞེས་བགྱི་བ་ནི་ཅི་ལགས་དངོས་པོ་མ་མཆིས་པ་ཞེས་བགྱི་བ་ནི་ཅི་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཉིས་པའོ། །

[Block 1928]
བཅོམ་ལྡན་འདས་གཉིས་ནི་གང་ལགས་གཉིས་སུ་མ་མཆིས་པ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གསུམ་པའོ། །

[Block 1929]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ན་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བཞི་པའོ། །

[Block 1930]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ཀྱི་བསམ་གཏན་བཞི་བསྐྱེད་པར་གྱུར་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་ལྔ་པའོ། །

[Block 1931]
ཇི་ལྟར་ན་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་མཐར་གྱིས་སྤྱོད་པ་དང་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དྲུག་པའོ། །

[Block 1932]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ན་འོ་ན་ནི་གཟུགས་ཀྱང་མ་མཆིས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བདུན་པའོ། །

[Block 1933]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ན། དོན་ཅི་ཞིག་མཐོང་ན༌[^1311]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སེམས་ཅན་རྣམས་ཀྱི་དོན་གྱི་སླད་དུ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བརྒྱད་པའོ། །

[Block 1934]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དམིགས་སུ་མ་མཆིས་པ་ལ་འཐོབ་པ་འམ་མངོན་པར་རྟོགས་པ་འམ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དགུ་པའོ། །

[Block 1935]
བཅོམ་ལྡན་འདས་གལ་ཏེ་མི་དམིགས་པ་ཉིད་འཐོབ་པ་ལགས༌[^1312]མི་དམིགས་པ༌[^1313]མངོན་པར་རྟོགས་པ་ལགས༌[^1314]ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་པའོ། །

[Block 1936]
བཅོམ་ལྡན་འདས་མི་དམིགས་པ་དང་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གཅིག་པའོ། །

[Block 1937]
བཅོམ་ལྡན་འདས་དམིགས་པ་མ་མཆིས་པའི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དང་བཟོད་པ་དང་བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་། ཤེས་རབ་དང་མངོན་པར་ཤེས་པ་རྣམས་ཇི་ལྟར་ཐ་དད་དུ་བགྱི་བར་བསྟན་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གཉིས་པའོ། །

[Block 1938]
ཇི་ལྟར་སེམས་བསྐྱེད་པ་གཅིག་གིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡོངས་སུ་འཛིན་པ་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་གསུམ་པའོ། །

[Block 1939]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་སྦྱིན་པའི༌[^1315]སྦྱིན་པ༌[^1316]ཡང་གཉིས་ཀྱི་འདུ་ཤེས་སུ་མི་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བཞི་པའོ། །

[Block 1940]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་མཚན་མ་མ༌[^1317]མཆིས་པ་དང་མངོན་པར་འདུ་བགྱིད་པ་མ་མཆིས་པ་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་ལྔ་པའོ། །

[Block 1941]
བཅོམ་ལྡན་འདས་དེ་ལྟར་ཆོས་ཐམས་ཅད་དབྱེར་མ་མཆིས་ཤིང་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་དྲུག་པའོ། །

[Block 1942]
བཅོམ་ལྡན་འདས་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཞེས་བགྱི་བ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བདུན་པའོ། །

[Block 1943]
བཅོམ་ལྡན་འདས་ཉན་ཐོས་རྣམས་དང་རང་སངས་རྒྱས་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་བརྒྱད་པའོ། །

[Block 1944]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་མཚན་ཉིད་མ་མཆིས་པའི་ཏིང་ངེ་འཛིན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བགྱིས་ཤིང་ཞེས་བྱ་བ་ནི་བརྒྱད་ཅུ་དགུ་པའོ། །

[Block 1945]
བཅོམ་ལྡན་འདས་སྐྱོན་ནི་གང་ལགས་སྐྱོན་མ་མཆིས་པ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་པའོ། །

[Block 1946]
དམིགས་པ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་གཅིག་པའོ། །

[Block 1947]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་ཇི་ལྟར་ན་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་གཉིས་པའོ། །

[Block 1948]
བཅོམ་ལྡན་འདས་གལ་ཏེ༌[^1318]ཆོས་ཐམས་ཅད་དབྱེར་མ་མཆིས་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་གསུམ་པའོ། །

[Block 1949]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བཞི་པའོ། །

[Block 1950]
བཅོམ་ལྡན་འདས་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལ་མ་མཆིས་པའི་ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ལ་མཆིས༌[^1319]ཞེས་བྱ་བ་ནི་དགུ་བཅུ་ལྔ་པའོ། །

[Block 1951]
རབ་འབྱོར་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་སྦྱིན་པས་སེམས་ཅན་རྣམས་སྡུད་པ་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་དྲུག་པའོ། །

[Block 1952]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རམ་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བདུན་པའོ། །

[Block 1953]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་ན་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་བརྒྱད་པའོ། །

[Block 1954]
བཅོམ་ལྡན་འདས་གལ་ཏེ་མཐའ་ལས་འདས་པ་དང་། ཐོག་མ་དང་ཐ་མ་མེད་པའི་སྟོང་པ་ཉིད་ཉེ་བར་བཟུང་སྟེ་སེམས་ཅན་ཡང་ཤིན་ཏུ་མི་དམིགས་ཞེས་བྱ་བ་ནི་དགུ་བཅུ་དགུ་པའོ། །

[Block 1955]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དེ་ལྟར་ཆོས་ཀྱི་དབྱིངས་ལ་ཡང་འདའ་བ་མ་མཆིས། དེ་བཞིན་ཉིད་དང་ཡང་དག་པའི་མཐའ་ལ་ཡང་འདའ་བ་མ་མཆིས་ན་ཅི་ལགས་འོ་ན་གཟུགས་ཀྱང་གཞན་ལ་ཆོས་ཀྱི་དབྱིངས་ཀྱང་གཞན་ཞེས་བྱ་བ་ནི་བརྒྱ་པའོ། །

[Block 1956 [HEADING]]
##### ཞུ་བ་བརྒྱ་ཕྲག་གསུམ་པ། ^1-2-6-3-0

[Block 1957]
འདི་མན་ཆད་ནི༌[^1320]བརྒྱ་ཕྲག་གསུམ༌[^1321]ལ་བབ་སྟེ། བཅོམ་ལྡན་འདས་ཅི་ལགས་ལམ་བསྒོམས་པས་འབྲས་བུ་འབྱུང་ཞིང་འབྲས་བུ་ཐོབ༌[^1322]པའམ། ཐོབ་པར་འགྱུར་བ་མ་མཆིས་སམ་ཞེས་བྱ་བ་ནི་ཞུ་བ༌[^1323]དང་པོའོ། །

[Block 1958]
བཅོམ་ལྡན་འདས་གལ་ཏེ་འདུས་བྱས་ཀྱི་ཁམས་སམ་འདུས་མ་བྱས་ཀྱི་ཁམས་རིགས་སུ་ཚར༌[^1324]བཅད་ཅིང་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 1959]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཆོས་རྣམས་ཀྱི་ཆོས་ཀྱི་མཚན་ཉིད་རྟོགས་པ་ལགས་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 1960]
བཅོམ་ལྡན་འདས་སྤྲུལ་པས་ལམ་བསྒོམ་པ༌[^1325]ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་བཞི་པའོ། །

[Block 1961]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་དངོས་པོ་མ་མཆིས་པའི་ཆོས་རྣམས་རྟོགས་པ་ལགས་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1962]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཟུགས་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 1963]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུར་འཚལ་ཞིང་ཞེས་བྱ་བ་ནི་བདུན་པའོ། །

[Block 1964]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1965]
བཅོམ་ལྡན་འདས་མིང་ནི་གང་ལགས་མཚན་མ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་དགུ་པའོ། །
--- END BLOCKS ---
