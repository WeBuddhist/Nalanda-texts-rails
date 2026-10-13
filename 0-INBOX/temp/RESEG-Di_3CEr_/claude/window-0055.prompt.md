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
སྒྲ་ནམ་མཁའ་ལྟ་བུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1927]
དེར་དེ་ལྟར་འདྲེས་པ་ལ༌[^1519]ཕྱིན་ཅི་ལོག་ཡིན་ཀྱང་རྗེས་སུ་འགྲོ་བ་སྲིད་དེ། གང་མི་རྟག་པ་དེ་རྩོལ་བ་ལས་བྱུང་ངོ་ཞེས་བྱ་བ་དང་། གང་རྩོལ་བ་ལས་མ་བྱུང་བ་དེ་རྟག་པའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1928]
དེ་ལྟ་བུར་བྱས་པ་ལ་དེ་བཞིན་དུ་ཞེས་པ་དང་། དེ་བཞིན་དུ་མ་ཡིན་ནོ་ཞེས་མཇུག་བསྡུ་བར༌[^1520]བྱའོ། །

[Block 1929]
ཕྱོགས་ཕྱི་མ་ཇི་ལྟ་བ་བཞིན་དུ་ཕྱོགས་སྔ་མ་ཡང་ཡིན་པས་མཚུངས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། དེ་ལྟར་སྣང་བ་ཡང་འཐད་པ་ཡིན་ནོ། །

[Block 1930]
དཔེར༌[^1521]བསྟན་པ་ཙམ་ཉིད་ལ་ཕྱོགས་སྔ་མ་དང་ཕྱི་མ་གཉིས་ཀ་ཡང་རྗེས་སུ་འགྲོ་བ་ཕྱིན་ཅི་ལོག་ཏུ་མཚུངས་སོ། །

[Block 1931]
དེ་ལྟ་ན་ནི་བུམ་པ་ལ་ཆོས་གཉིས་ཀ་ཡང་རིགས་པ་ཡིན་ལ་དེ་བཞིན་དུ་ནམ་མཁའ་ལ་ཡང་ངོ་། །དེ་ལྟ་བུ་ཡང་།

[Block 1932 [VERSE]]
རྟགས་དེའི་བདག་ཉིད་ཀྱིས༌[^1522]དབྱེ་བས། །
འཁྲུལ་པ་ལྟར་སྣང་རྣམ་པ་གཉིས། །
གཏན་ཚིགས་ཕྱོགས་གཅིག་ཏུ་ངེས་པ། །
སྦྱོར་བ་སྔ་མ་ལ་ཡོད་མིན། །

[Block 1933]
དེ་ལྟར་ཁོ་བོ་ཅག་གིས་འཇིག་རྟེན་པའི་སྦྱོར་བའི་རྗེས་སུ་ཞུགས་ནས་ཆོས་མཐུན་པ་དང་། མི་མཐུན་པ་མཚུངས་པར་བསྟན་པ་སྟེ། བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་ཉིད༌[^1523]ནི་ཕྱོགས་གཅིག་ཏུ་ངེས་པ༌[^1524]དངོས་པོའི་གཏན་ཚིགས་སུ་འདོད་པ་ཡིན་ཡང་། ཕྱིན་ཅི་ལོག་གི༌[^1525]ངེས་པ་ལྟར་སྣང་བར་བརྗོད་དོ། །

[Block 1934]
ཕྱོགས་སྔ་མ་ལ་ནི་ཁོ་བོ་ཅག་གིས་སྦྱོར་བ་བཞིན་ཕྱོགས་གཅིག་ཏུ་ངེས་པར་བསྟན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1935]
དེ་བཞིན་དུ་གང་གི་ཕྱིར་ཆོས་མཐུན་པ་མཚུངས་པར་བྱས་པ་ལ༌[^1526]ཡང་འབྲེལ་པ་མེད་པའི་ཕྱིར་གཞན་ཉིད་ཡིན་ནོ། །

[Block 1936 [HEADING]]
### རྣམ་པར་རྟོག་པ་མཚུངས་པ། ^6-8-0

[Block 1937]
བྱེ་བྲག་བརྗོད་པས་ཆོས་མཐུན་པའང་། །རྣམ་རྟོག་མཚུངས་པའོ། །

[Block 1938]
དཔེར་ན་སྔར་བཞིན་དུ་བུམ་པ་དང་ཆོས་མཐུན་པས་མི་རྟག་པར་བྱས་པ་ལས༌[^1527]བརྗོད་པ། དེ་ལ་ཆོས་མཐུན་པ་ཡོད་དུ་ཟིན་ཀྱང་བསྲེག་པར་བྱ་བ་དང་། མིག་གི་གཟུང་བྱ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་བུམ་པ་ཁོ་ན་མི་རྟག་པར་འགྱུར་གྱི༌[^1528]སྒྲ་ནི་མ་ཡིན་ལ། སྒྲ་ཁོ་ན་རྟག་པར་འགྱུར་ཏེ། བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་དང་། མཉན་བྱ་ཉིད་ལ་སོགས་པས་སོ༌[^1529]ཞེས་སོ། །

[Block 1939]
བསྒྲུབ་པར་བྱ་བ་ལས་བཟློག་ནས་རྣམ་པར་རྟོག་པར་བྱེད་པས་ན་རྣམ་པར་རྟོག་པ་མཚུངས་པའམ། དཔེར་བརྗོད་པ་ལས་གཞན་ལ་ཡང་བྱས་པ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་བསྲེག་པར་བྱ་བ་དང༌[^1530]བསྲེག་པར་བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་བཞིན་རྟག་པ་དང་མི་རྟག་པ་རྣམ་པར་རྟོག་པ་བརྗོད་པས་ན། རྣམ་པར་རྟོག༌[^1531]པ་མཚུངས་པའོ་ཞེས་ཟེར་རོ། །

[Block 1940]
འདི་ལ་ནི།

[Block 1941]
འཁྲུལ་པ་ཅན་གྱི་བྱེ་བྲག་གིས། །རྟག་པར་འགྱུར་བ༌[^1532]དེ་ལྟར་སྣང་། །

[Block 1942]
སྤྱི་མིན་གྱིས་ཀྱང་། འདི་ལ་ཡང་འཁྲུལ་པ་ཅན་དང་ཐུན་མོང་མ་ཡིན་པ་དེ༌[^1533]བཞིན་དུ་རྟག་པའམ་སུན་འབྱིན་པར་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 1943]
རང་གི་ཕྱོགས་ལ་མ་གྲུབ་པ་བཞིན་གཞན་ལ་མ་གྲུབ་པ་བསྟན་པའི་ཕྱིར་སྒྲུབ་པར་བྱེད་པར་འགྱུར་རོ། །

[Block 1944]
སུན་འབྱིན་པ་ལ་ནི་ཐུན་མོང་ངམ་ཐུན་མོང་མ་ཡིན་པའི་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1945]
བསྒྲུབ་པ༌[^1534]ལ་ནི་འགལ་བ་མི་འཁྲུལ་བ་ཅན་དུ་རྩོད་པ་ལྟར་སྣང་བའོ། །

[Block 1946]
རྣམ་པ་གཞན་ཡང་སྟེ་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1947]
གལ་ཏེ་བསྲེག་པར་བྱ་བ་དང་བསྡོངས་པའི་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་ཉིད་བརྗོད་ན་ནི་མངོན་སུམ་འབའ་ཞིག་པ་མིག་གི་གཟུང་བྱ་མ་ཡིན་པ་ཉིད་དང་རྫས་ཉིད་ལ་སོགས་པས་མ་ངེས་པ་ཡིན་ནོ། །

[Block 1948]
བསྡོངས་པའི་ངེས་པར་བྱེད་པའི་གཏན་ཚིགས་འདི་ཡང་དེ་བཞིན་དུ་མ་ཡིན་ནོ། །

[Block 1949]
བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་འབའ་ཞིག་པ་ནི་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པ་ཡིན་ཏེ། དེའི་ཕྱིར་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1950 [HEADING]]
### བྱེ་བྲག་མེད་པར་མཚུངས་པ། ^6-9-0

[Block 1951]
གཅིག་ཉིད་དུ། ཐལ་བར་འགྱུར་ཕྱིར་བྱེ་བྲག་མེད། །ཆོས་མཐུན་པ་སྟོན་པའི་སྐབས་ཡིན་པའི་ཕྱིར་དེ་དང་གཅིག་ཏུ་ཐལ་བར་འགྱུར་བས༌[^1535]ནའོ། །

[Block 1952]
ཟླ་བོ་མཉན་བྱ་མ་ཡིན་པའི་ཕྱིར་མེད་བཞིན་དུ་གང་དུ་གང༌[^1536]གིས་ན་བསྒྲུབ་བྱའི་ཞེས་གོ་བར་བྱ། བྱེ་བྲག་མེད་ཅེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པར་ཐལ་བའོ། །

[Block 1953]
གང་ཞིག་གང་དང་བྱེ་བྲག་ཡིན་ཞེ་ན། བྱེ་བྲག་མེད་པར་བྱས་པའི་ཕྱིར་ཐམས་ཅད༌[^1537]དང་སྟེ། དཔེར་ན་ཆོས་མཐུན་པའི་དཔེ་བུམ་པ་བསྟན་པའི་ཕྱིར་གཞན་རྣམས་དང་ཡང་ཁྱད་པར་མེད་པར་བྱེད་པས་བུམ་པ་ལ་ཡོད་པའི་ཆོས་ཐམས་ཅད་སྒྲ་ལ༌[^1538]ཐོབ་པར་འགྱུར་རོ། །

[Block 1954]
དེ་ལྟ་བས་ན་ཐམས་ཅད་ཕན་ཚུན་ཆོས་མཐུན་པའི་ཕྱིར་གཅིག་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1955]
འདི་ལ་ཡང་བྱེ་བྲག་མེད་པར་ཐལ་བར་འགྱུར་བས་ན་བུམ་པ་བཞིན་སྒྲའི་བྱེ་བྲག་ཉིད་རབ་ཏུ་སྟོན་པ་ཡིན་པའི་ཕྱིར་རྣམ་རྟོག་མཚུངས་པ་ལས་ཁྱད་པར་ཆེན་པོ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1956]
དེའི་ཕྱིར་དེ་བཞིན་དུ་མ་ངེས་པ་ལྟར་སྣང་བའོ། །

[Block 1957]
ཕྱོགས་སྔ་མ་ལ་ནི་ཆོས་མཐུན་པ་ཙམ་ལས་མི་རྟག་པར་བརྗོད་པ་དང་། གང་བྱེ་བྲག་མེད་པ་ཙམ་ལས་མི་རྟག་པར་བརྗོད་པ་མེད་དེ། གང་བྱེ་བྲག་མེད་པར་མ་མཐོང་བ་ཙམ་ལས་ལྡོག་པར་བྱེད་དོ། །

[Block 1958 [VERSE]]
དེའི་ཕྱིར་མ་ངེས་པ་ལྟར་སྣང་བའོ། །
བསྒྲུབ་བྱ༌[^1539]རྟོགས་ཁྱད་མེད་ཕྱིར་ཡང་། །
མ་གྲུབ་པ་ལྟར་སྣང་བར་འདོད། །

[Block 1959]
བྱེ་བྲག་མེད་པར་མཚུངས་པ་སྔ་མ་ལས་ཐ་དད་དུ་བྱ་བའི་དོན་དུ་ཡང་གི་སྒྲ་སྨོས་སོ། །

[Block 1960]
དེ་ལ་རྣམ་པར་རྟོག་པ༌[^1540]མཚུངས་པ་དང་བྱེ་བྲག་མེད་པ་ལས་བྱེ་བྲག་མེད་པར་མཚུངས་པ་ནི་གཞན་དུ་བརྗོད་པར་བྱ་སྟེ། བསྒྲུབ་བྱ་དང་གཏན་ཚིགས་ཀྱི་དོན་དག་ལ་བྱེ་བྲག་མེད་པའི༌[^1541]ཕྱིར་རོ། །

[Block 1961]
དཔེར་ན་སྔར་བཞིན༌[^1542]བྱས་པ་ལ་གཏན་ནས་བྱུང་བ་མ་ཡིན་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་ཀྱི་དོན་དག་ལ་བྱེ་བྲག་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་སོ། །

[Block 1962]
དེ་ལ་བརྗོད་པ། དེ་ལྟ་བུ་ཡང་མ་གྲུབ་པ་ལྟར་སྣང་བ་སྟེ། སྔ་ན་མེད་པ་སྐྱེས་པ་ལ་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་སྒྲོ་བཏགས་ནས་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་སུ་བྱེ་བྲག་མེད་པར་མགོ་བསྒྲེ་བའི་ཕྱིར་རོ། །

[Block 1963]
གྲུབ་ན་ནི་སྔར་ནས་ཡོད་པ༌[^1543]ཞིག་ན༌[^1544]མེད་པ་བསྒྲུབ་པར་བྱའོ། །

[Block 1964]
གཞན་ཡང་བྱེ་བྲག་མེད་པར་མཚུངས་པ་བརྗོད་པར་བྱ་སྟེ། བརྩལ༌[^1545]མ་ཐག་ཏུ་བྱུང་བ་ཉིད་ནི་མི་རྟག་པ་བསྒྲུབ་པ༌[^1546]བཞིན་ཆོས་གཞན་ཡང་སྒྲུབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པའོ། །

[Block 1965]
དེ་ལྟ་བུ་ཡང་བསྒྲུབ་པར་བྱ་བ་ལ་གནོད་པ་སྒྲུབ་པར་བྱེད་པ་ཉིད་ཀྱིས་ནི༌[^1547]འགལ་བ་ལྟར་སྣང་བའོ། །
--- END BLOCKS ---
