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
[Block 2311]
བཞོན་པ་ང་ལ་ཡོད་ཅེས་པ་ནི་བཞོན་པ་སྦྱིན་པར་ཁས་བླངས་པའོ། །

[Block 2312]
རི་དགས་དང་ར་དང་གླང་ཞེས་པ་ནི་ཕྱི་རོལ་ན་ཡོད་པ་དང་དངོས་བསྟན་པའོ། །

[Block 2313]
འབྲས་བུ་ནི་རྒྱུའི་སྒོ་ནས་བྱུང་། གཞུང་ཉིད་ནི་བསྟན་པ་ལས་ཕྱི་རོལ་བས་ཕྱི་རོལ་ན་ཡོད་ཅེས་སྨྲས་སོ། །

[Block 2314]
བླ་ན་མེད་པའི་གནས༌[^1941]ཁམས་གསུམ་ལས་འདས་པའི་ཕྱིར་ཕྱི་རོལ་ན་ཡོད་ཅེས༌[^1942]བསྟན་ཏོ། །

[Block 2315]
ཁྱེད་ཅག་གི་ཕྱིར་ངས་བྱས་ཞེས་པ་ནི་བཞོན་པའི་དགོས་པ་བསྟན་ཏེ། མྱ་ངན་ལས་འདས་པའི་གནས་དམ་པ་ནི་འདུས་མ་བྱས་པ་ཡིན་མོད་ཀྱི་ཐེག་པ་ཉིད་འདུས་བྱས་ཡིན་པའི་ཕྱིར་བྱས་ཞེས་སྨྲས་སོ། །

[Block 2316 [HEADING]]
###### **གསུང་རབ་ལ་བརྟེན་ནས་ཉོན་མོངས་པའི་ས་ནས་འབྱུང་བའི་དཔེ།** ^4-3-5-4-2-1-1-1-4-0

[Block 2317]
མདོ་ལས།

[Block 2318 [HEADING]]
###### **བུ་རྣམས་སྡུག་བསྔལ་གྱི་ས་ནས་འཐོན་པ།** ^4-3-5-4-2-1-1-1-4-1-0

[Block 2319]
བཞོན་པ་དེ་འདྲ་ཡོད་པར་ཤེས་ནས་སུ། །ཞེས་པ་ནས། སྡུག་བསྔལ་དག་ལས་ཐར་ཏེ་སྟོང་པར་འདུག །ཅེས་པའི་བར་དུ་ནི་གསུང་རབ་ལ་བརྟེན་ནས་སྡུག་བསྔལ་ལས་ཐར་བར་བསྟན་ཏེ། དེ་ཡང་བུ་རྣམས་སྡུག་བསྔལ་གྱི་ས་ནས་འཐོན་པ༌[^1943]དང་ཕ་བདེ་བར་གནས་པ་སྟེ། འདིས་ནི་བུ་རྣམས་སྡུག་བསྔལ་གྱི་ས་ནས་འཐོན་པ་བསྟན་ཏོ། །

[Block 2320]
སྟོང་པར་འདུག་ཅེས་པ་ནི་སྒྲིབ་པ་གསུམ་དང་བྲལ་བའི་གནས་བསླབ་པ་མེད་པའི་ས་དང༌[^1944]པོ་ལ་གནས་པའོ། །

[Block 2321 [HEADING]]
###### **ཕ་བདེ་བར་གནས་པ།** ^4-3-5-4-2-1-1-1-4-2-0

[Block 2322]
མདོ་ལས།

[Block 2323]
མི་དེས་བྱིས་པ་འཐོན་པ་མཐོང་ནས་སུ། །ཞེས་པ་ནས། ཕ་དེ་བདེ་བར་འདུག་པར༌[^1945]རིག་ནས་སུ། །ཞེས་པའི་བར་དུ་ནི་བུ་རྣམས་ཐོན་ནས་ཕ་བདེ་བར་གནས་པ་བསྟན་ཏེ། དཔོང་ས་བཞི་མདོར་ཞེས་པ་ནི། བདེན་པ་བཞིའོ། །

[Block 2324]
སེང་གེའི་ཁྲི་ལ་བཞུགས་ཞེས་པ་ནི་མི་འཇིགས་པའི་ས་ལ་གནས་པ་སྟེ། སྔོན་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་མཛད་པ་ན་སེམས་ཅན་ཐམས་ཅད་སྒྲོལ་བའི་ཐུགས་དམ་དང་བཅས་པས༌[^1946]སེམས་ཅན་འཁོར་བའི་གནས་ནས་ཐོན་པས་དགོངས་པ་གྲུབ་པའི་ཕྱིར་བདེ་བར་བཞུགས་ཞེས་སྨྲས་སོ། །

[Block 2325 [HEADING]]
###### **ངེས་པའི་དོན།** ^4-3-5-4-2-1-1-2-0

[Block 2326]
མདོ་ལས།

[Block 2327]
བུ་རྣམས་དོང་སྟེ་འདི་སྐད་སྨྲས། །ཞེས་པ་ནས། དེ་དག་དུས་དེང་སྩལ་དུ་གསོལ། །ཞེས་པའི་བར་དུ་ནི་དེ་ཡན་ཆད་ནི་དྲང་བའི་དོན་བསྟན་འདི་མན་ཆད་ནི་ངེས་པའི་དོན་བསྟན་ཏེ། བདག་ཅག་སྩོལ་ཞེས་པ་ནི་དབང་པོ་སྨིན་ཞེས་པའི་དོན་ཏོ། །

[Block 2328]
མདོ་ལས།

[Block 2329]
མི་དེ་མཛོད་ཀྱི་མཐུ་ལྡན་པ། །ཞེས་པ་ནས། གང་ལ་རིན་ཆེན་ཤིང་རྟ་བཅས། །ཅེས༌[^1947]པའི་བར་དུ་ནི་མི་དེ་མཛོད་ཀྱི་མཐུ་དང་ལྡན་པ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་མཛོད་དང་ལྡན་པའོ། །

[Block 2330]
ཡུལ་འཁོར་ཐམས་ཅད་ཀྱང༌[^1948]མི་ལ་བྱིན་ན་ཡང་མི་ཟད་པའི་ནོར་དང་ལྡན་པ་ཡིན་ན། བྱིས་པ་རྣམས་ལ་བྱིན་པས་གང་ལ་ཟད་པར་འགྱུར་བ་ནི་ཡོན་ཏན་གྱི་ཆོས་མང་པོ་དང་ལྡན་པའོ། །

[Block 2331]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཟག་པ་མེད་པའི་ཕུང་པོ་ལྔ་དང་ལྡན་པའི་སྐུ་སྟེ། ཤིང་རྟ་ཞེས་པ་ནི་དེ་བཞིན་ཉིད་ཀྱི་ཆོས་ལ་བྱའོ། །

[Block 2332]
རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པའི་ཤིང་རྟ་དེ་ཡང་ཁ་ལོ་སྒྱུར་བ་དང་དྲིལ་བུ་དང་། གཡེར་ཀ་དང་། གདུགས་དང་། ལྷབ་ལྷུབ་དང་། མུ་ཏིག༌[^1949]གི་དྲ་བ་དང་། གསེར་གྱི་ཕྲེང་བ་དང་། གདིང་བ་འཇམ་པོ་ལ་སོགས་པའི་རྒྱུ་ནི་རྣམ་པར་དཀར་བ་སྒྲིབ་པ་གཉིས་དང་བྲལ་བའི་རྐྱེན་སྤྱོད་པ་དམ་པ་དང་ལྡན་པ་འཚོ་བ་རྣམ་པར་དག་པའི་གདན་ལ་བཞུགས་ཞེས་པའི་དོན་ཏོ། །

[Block 2333]
གླང་དཀར་པོ་ཚོ་ལ་བཟང་བ་ནི། གཅིག་ཏུ་དཀར་བ། གཅིག་ཏུ་ཚོ་ཞིང་སྟོབས་དང་ལྡན་པ་གཅིག་ཏུ་འབད་པ། གཅིག་ཏུ་མཛེས་པ་དང་ལྡན་ཞེས་པའི་དོན་ཏོ། །

[Block 2334]
མདོ་ལས།

[Block 2335 [VERSE]]
སྐྱེས་བུ་དུ་མས་རབ་ཁྲིམ༌[^1950]པ། །
སྐྱེས་བུ་དེ་ཡིས་དེ་འདྲ་བྱིན། །

[Block 2336]
ཞེས་པ་ནས། ཕྱོགས་དང་ཕྱོགས་མཚམས་རྩེ་བར་དོང་། །ཞེས་པའི་བར་དུ་ནི། ཕྱོགས་དང་ཕྱོགས་མཚམས་ཞེས་པ་ནི་ཕྱོགས་བཞིར་སྐྱེ་བ་རྣམ་བཞིས་སྐྱེ་བའི་སེམས་ཅན་གྱི་དོན་ལ་རོལ་པའོ། །

[Block 2337]
རྩེ་ཞེས་པ་ནས༌[^1951]རྫུ་འཕྲུལ་གྱིས་རོལ་པའོ། །

[Block 2338 [HEADING]]
###### **དཔེ་དང་དོན་དུ་སྦྱར་བ།** ^4-3-5-4-2-1-2-0

[Block 2339]
མདོ་ལས།

[Block 2340]
དེ་བཞིན་ང་ཡང་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། སྐྱེ་རྒ༌[^1952]ན༌[^1953]བ་དུ་མ་བརྒྱ།[^1954] །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་དྲུག་ཅུ་རྩ་ལྔས་ནི་དཔེ་བསྟན། བཅོ་བརྒྱད་ཀྱིས་ནི་དོན་དང་སྦྱར་བ་བསྟན་ཏེ། དེ་ལ་དང་པོ་ཚིགས་བཅད་བཅུ་གཅིག་གིས་ནི་དྲང་བའི་དོན་བསྟན། ཚིགས་བཅད་བདུན་གྱིས་ནི་ངེས་པའི་དོན་བསྟན། དྲང་བའི་དོན་ལ་ཡང་ཚིགས་བཅད་གསུམ་གྱིས་བསྟན། ཁམས་གསུམ་གྱིས༌[^1955]ནི་ཁམས་གསུམ་ན་སངས་རྒྱས་བཞུགས་པ་དང་སྦྱར། དེའི་འོག་མ་ཚིགས་བཅད་གསུམ་གྱིས་ནི་འགྲོ༌[^1956]བ་རྣམ་ལྔ་གཡང་ཟ་བའི༌[^1957]གནས་སུ་སྦྱར། དེའི་འོག་མ་ཚིགས་བཅད་ལྔས་ནི་དྲང་བའི་དོན་གྱི་དཔེ་བསྟན་ཏོ། །

[Block 2341]
མདོ་ལས།

[Block 2342]
ཁམས་གསུམ་ནས་ནི་ང་ཐར་ཞིང་།[^1958] །ཞེས་པ་ནས། མི་ལྡོག་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་པའི་བར་དུ་ནི་དྲང་བའི་ཐབས་ཀྱི་དཔེ་བསྟན་པ་དང་། སྡུག་བསྔལ་བ་རྣམས་ལ་ཐུགས་རྗེ་སྐྱེ་བ་དང་། དོན་ཆེན་པོ་བསྟན་ཀྱང་མི་དངང་བ་དང་། བདག་ཉིད་ཁམས་གསུམ་གྱི་གནས་ལས་བྱུང་བར་བསྟན་པ་དང་། གནས་དེ་ཉིད་སངས་རྒྱས་ཀྱི་ཡིན་པ༌[^1959]བསྟན་པའོ། །

[Block 2343]
ནགས་ཚལ་དབེན་པའི་གནས་ཞེས་པ་ནི་ཡོན་ཏན་མང་པོའི་ཚལ་དུ་སྦྱར་རོ། །

[Block 2344]
ཕྱིར་མི་ལྡོག་ཞེས༌[^1960]པ་ནི་ས་དང་པོ་ལ་གནས་པ་ཡན་ཆད་དོ། །

[Block 2345]
དྲུག་ཤེས་པ་ནི་དགྲ་བཅོམ་པའོ། །

[Block 2346]
གསུམ་རིག་པ་ནི་སྔོན་གྱི་གནས་དྲན་པ་དང་། ལྷའི་སྤྱན་དང་། ཟག་པ་ཟད་པར་མཁྱེན་པའོ། །

[Block 2347]
མདོ་ལས།

[Block 2348]
མཁས་པ་རྣམས་ལ་དཔེ་མཆོག་འདི།[^1961] །ཞེས་པ་ནས། མི་མཆོག་ཐབས་མཁས༌[^1962]མ་གཏོགས་སོ། །ཞེས་པའི་བར་དུ་ནི། ཐེག་པ་མཆོག་ཡིན་པར་བསྟོད་ཅིང་བསྔགས་པ་སྟེ། ཐེག་པ་དེ་ཡང་ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་ཐེག་པ་དེ་ཡོན་ཏན་བཞི་དང་ལྡན་པར་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་འཕགས་པ་རྣམས་ཀྱི༌[^1963]བསྔགས་པ་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་ལོངས་སྤྱོད་དམ་པ་དང་ལྡན་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་དགའ་བའི་མཆོག་ཡིན་པར་བསྟན་ཏོ། །

[Block 2349]
དེ་ལ་ཡོན་ཏན་བཞི་ནི་དམ་པ་ཁྱད་པར་ཅན་སྒྲིབ་པ་མེད་པས་རྣམ་པར་དག་པ་དང་། མཆོག་དམ་པ་ཡིན་པ་དང་།

[Block 2350 [VERSE]]
བླ་ན་མེད་པ་དང་ཟླ༌[^1964]མེད་པའོ། །
ཡངས་པའི་དངོས་པོ་ཕྱག་གི་གནས། །
--- END BLOCKS ---
