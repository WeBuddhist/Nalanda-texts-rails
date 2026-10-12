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
དེ་ལྟ་ན་འདུས་པའི་རྒྱན་ལ་སོགས་པ་གཞན་ཡོད་པས་འགྲེལ་པ་འདིས་ཅི་ཞིག་བྱ་ཞེ་ན། རྒྱལ་སྲས་ཡུལ་གྱུར་ཞེས་སྨོས་པ་ལ་རྒྱལ་བའི་སྲས་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་བྲལ་བས་ས་བཅུའི་དབང་ཕྱུག་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 1927]
དེ་རྣམས་ཀྱི་ཡུལ་དུ་གྱུར་པ༌[^1311]ནི་བཤད་པའི་སྤྱོད་ཡུལ་འདུས་པ་འདི་ཡིན་ཞེས་འདིས་བདག་ཉིད་མངོན་པར་ཤེས་པ་ཐོབ་པ་ཉིད་ཀྱིས༌[^1312]སྣོད་དུ་རུང་བ་ཉིད་དུ་བསྟན་པས༌[^1313]འགྲེལ་པ་བྱས་པ་སྟེ།[^1314] སྐྱེ་བོ་གཞན་གྱིས་འགྲེལ་པ་བྱེད་མི་ནུས་སོ། །

[Block 1928]
རྒྱུད་ཀྱི་མིང་བསྟན་པར་བྱ་བའི་ཕྱིར། རྒྱལ་བ་རྣམས་ཀྱི་འདུས་པ་གང་ཡིན་པ། །ཞེས་སྨོས༌[^1315]ཏེ། རྒྱལ་བ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པ་ལྔའོ། །

[Block 1929]
དེ་རྣམས་ཀྱི་འདུས་པ་ནི་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 1930]
དགོངས་པ་ནི་འདི་ལྟ་སྟེ། བསྐྱེད་པའི་རིམ་པའི་རིགས་བརྒྱའི་དབྱེ་བ་ཉེ་བར་བསྡུས་ཏེ། ཕུང་པོ་ལྔ་དང་ཉོན་མོངས་པ་དང་དབང་པོ་དང་ཡུལ་དང་། རྣམ་པར་ཤེས་པ་དང་འབྱུང་བ་དང་རླུང་རྣམ་པ་ལྔ་ལ་སོགས་པའི་རྣམ་པར་དག་པའི༌[^1316]བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་སྤྲོས་ཏེ། དེ་དག་གཅིག་ཏུ་གྱུར་པ་དག་གིས་མགྲིན་པ་གཅིག་གིས༌[^1317]

[Block 1931]
དང་པོ་ཞུ་བ་སྔོན་དུ་འགྲོ་བར་གསོལ་བ་གདབ་བོ། །

[Block 1932]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དེ་རྣམས་ལ་སོ་སོར་བསྟན་ཞེས་རྒྱལ་བ་རྣམས་ཀྱི༌[^1318]འདུས་པའོ། །

[Block 1933]
ཡང་ན་དམ་ཚིག་གི་དཀྱིལ་འཁོར་དུ་ཐམས་ཅད་ཕྱུང་བ་ནི་འདུས་པའོ། །

[Block 1934]
ཡང་ན་སྐུ་དང་གསུང་དང༌[^1319]ཐུགས་ཀྱི་ངོ་བོ་ཉིད་ཡི་གེ་གསུམ་པོ་འཇུག་པ་ལ་སོགས་པའི་རིམ་གྱིས་གོམས་པར་གྱུར་པ་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་འཁོར་ལོ་རོ་གཅིག་པར་གྱུར་པ་ནི་འདུས་པའོ། །

[Block 1935]
གཞན་ཡང་ཕྱིར་མི་ལྡོག་པའི་དབང་གིས་དུས་སུ་སློབ་མའི་ཚངས་པའི་སྒོ་ནས་དེ་བཞིན་གཤེགས་པ་འཇུག་པས་གཅིག་ཏུ་གྱུར་པ་ནི་འདུས་པའོ། །

[Block 1936]
རྫོགས་པའི་རིམ་པ་ལ་ཡང་རྩ་སྟོང་ཕྲག་བདུན་ཅུ་རྩ་གཉིས་ཀྱི་བུག་པ་ནས་འཕོ་བའི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་རྡོ་རྗེའི༌[^1320]རྩེ་མོར་འཛིན་པའི་ཡན་ལག་གིས་གཟུང་བ་ནི་འདུས་པའོ། །

[Block 1937]
ཡང་ན་དངོས་པོ་ཐམས་ཅད་ཉེ་བར་བསྡུས་ཤིང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་སྒོམ་པ་ནི་འདུས་པའོ། །

[Block 1938]
དེ་ལྟ་བུའི་རྣམ་པ་དུ་མ་གཞུང་རྒྱས་པའི་འཇིགས་པས་འདིར་མ་བཤད་དོ། །

[Block 1939]
གསང་བ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་ཡིན་ཏེ། གསང་བ་འདུས་པ་ཞེས་བྱའོ། །

[Block 1940]
ཐ་མལ་པའི་ལུས་ངག་ཡིད་འཇིག་རྟེན་ལས་འདས་པར་བྱེད་པ་ནི་གསང་བའོ། །

[Block 1941]
སྐུ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཡི་གེ་གསུམ་གྱི་འཇུག་པ་ལ་སོགས་པའི་སྒོམ་པ་ནི་གསང་བའོ། །

[Block 1942]
ཡང་ན་འདོད་པའི་གདུགས་ལ་སོགས་པ་རྩ་གསུམ་དུ་བདེ་བ་ཆེན་པོ་མྱོང་བ་ནི་གསང་བའོ། །

[Block 1943]
དེ་བཞིན་དུ་གཞན་ཡང་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 1944]
ཇི་སྐད་དུ།

[Block 1945 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་རྣམ་པ་གསུམ། །
གསང་བ་ཞེས་ནི་མངོན་པར་བརྗོད། །
འདུས་པ་བསྡུས་པར་བརྗོད་པ་སྟེ། །
སངས་རྒྱས་ཐམས་ཅད་མིང་ཞེས་བྱའོ། །

[Block 1946]
ཞེས་འབྱུང་ངོ་། །རང་གི༌[^1321]གླེགས་བམ་ལ་བལྟ་བ་བཀག་པ་དང་སློབ་དཔོན་གྱིས༌[^1322]མན་ངག་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་ནི་དཔལ་ལྡན་ཀླུ་སྒྲུབ༌[^1323]ལས་རྙེད་པ། །ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་དཔལ་ཀླུ་སྒྲུབ༌[^1324]ཀྱི་ཞལ་སྔ་ནས་ཀྱི་དངོས་སུ་སློབ་མ་ཉིད༌[^1325]སོ་སོར་བསྟན་གྱི་བརྒྱུད་པས༌[^1326]ནི་མ་ཡིན་ནོ། །

[Block 1947]
དེས་འདུས་པའི་ཚིག་གི༌[^1327]ཁྱད་པར་དང་བཅས་པར་སྨྲ་བ་ན་རྒྱུད་ཀྱི་མིང་བསྟན་ཏོ། །

[Block 1948]
བརྗོད་པར་བྱ་བ་བསྟན་པར་བྱ་བའི་ཕྱིར། རིམ་པ་གཉིས་ཀྱི་གནས་ཞེས་བྱ་བ་སྨོས་པ་ལ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པ་ནི་རིམ་པ༌[^1328]གཉིས་སོ། །

[Block 1949]
དེ་དག་གི་གནས་ནི་འདུས་པའོ། །

[Block 1950]
དེས་དེ༌[^1329]དག་ཁོ་ན་བསྟན་པར་བྱ་བ་ནི་བརྗོད་པར་བྱ་བ་ཡིན་གྱི་གཞན་མ་ཡིན་ནོ། །

[Block 1951]
རིམ་པ་གཉིས་པོ་ནི་དབྱེ་བ་དང་མཚན་ཉིད་དང་བཅས་པར་བཤད་ཟིན་ཏོ། །

[Block 1952]
མཐའ་དྲུག་ཀྱང་བཤད་པའི་རྒྱུད་ལས་ཤེས་པར་བྱས་ལ་རྒྱུད་གོ་བར་གྱུར་པས་འགྲེལ་པས་ཅི་ཞིག་བྱ་ཞེས་དེ་ལ་བསྟན་པར་བྱ་བའི་ཕྱིར། སངས་རྒྱས་ཀུན་གྱིས༌[^1330]རྒྱས་བཏབ་པ། །ཞེས་སྨོས་ཏེ། དཔེར་ན་རྒྱལ་པོ་རྣམས་ཀྱིས་རང་གི་མཛོད་ལ་རྒྱས་བཏབ་པ་བཞིན་དུ་སངས་རྒྱས་ཀུན་གྱི་མན་ངག་གི་གནས་དག་ཏུ་རྡོ་རྗེའི་ཚིག་གིས་རྒྱུད་འདི་ལ་རྒྱས་བཏབ་པའོ། །

[Block 1953]
དེ་བས་ན་འགྲེལ་པའི༌[^1331]ལྡེ་མིག་གིས་ཕྱེ་བར་བྱས་སོ། །

[Block 1954]
རྡོ་རྗེ་སེམས་དཔའ་དེ་ཇི་ལྟ་བུ་ཞེ་ན། ཁྱབ་བདག་ཅེས་སྨོས་ཏེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བདག་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1955]
གང་གི་ཕྱིར་ཡེ་ཤེས་ལྔ་ནི་ཐ་དད་པ་ལྟར་སྣང་བ་ཡིན་ཞེས་ཀུན་རྫོབ་ཀྱི་ཕྱོགས་སོ། །

[Block 1956]
དེ་དག་ནུས་པ་ཐམས་ཅད་ཉེ་བར་བསྡུས་པ་ན་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཀྱི་གནས་སྐབས་སུ་གྱུར་པ་ཐམས་ཅད་སྟོང་པའི་མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་གང་ཡིན་པ་བཅོམ་ལྡན་འདས་ཏེ་ཡེ་ཤེས་དང་ཤེས་བྱ་རོ་གཅིག་པ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁྱབ་བདག་ཅེས་བཤད་དོ། །

[Block 1957 [VERSE]]
དཔལ་གྱི་སྒྲ་ནི་སྔར་བཤད་དོ། །
རྡོ་རྗེ་སེམས་དཔའ་བཤད་པར་བྱ་སྟེ།
སྤོང་བ་ལྔ་དང་ཡེ་ཤེས་ལྔ། །
རྡོ་རྗེ་ཞེས་ནི་མངོན་པར་བརྗོད། །

[Block 1958]
དོན་ནི་འདི་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་ལྔ་པོ་སྤོང་བར་བྱེད་པ༌[^1332]ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་སྟོང་པ་འོད་གསལ་བ་ནི་རྡོ་རྗེར་བཤད་དོ། །

[Block 1959]
དེ་ཉིད་སེམས་དཔའ་སྟེ་ངོ་བོ་ཉིད་གང་ལ་ཡོད་པ་དེ་ནི་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 1960]
ཡང་ན་རྡོ་རྗེ་ནི་ཐབས་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 1961]
སེམས་དཔའ་ནི་ཤེས་རབ་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 1962]
དེ་དག་རོ་གཅིག་པ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 1963]
ཡང་ན་དཔལ་ནི་ཐབས་ཏེ་རྡོ་རྗེ་ཤེས་རབ་བོ། །

[Block 1964]
དེས་ན་སྙིང་རྗེ་དང་སྟོང་པ་ཉིད་དབྱེར་མེད་པ་ཉིད་དཔལ་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 1965]
རྡོ་རྗེ་རྩེ་མོ་ལས་ཀྱང་།
--- END BLOCKS ---
