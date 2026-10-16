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
[Block 3046]
ཆུ་དེ་ཡོངས་སུ་སྨིན་པའི་ཀུ་ཤ༌[^1931]དང་འདྲ་བའི་ཁ་དོག་ཀྱང་ཡོད་པས་སོ། །

[Block 3047]
སྨྱིག་མའི་མདོག་དང་། བཻ་ཌཱུརྱའི་འོད་ནི་སྨྱིག་མའི་མདོག་དང་བཻ་ཌཱུརྱའི་འོད་དོ། །

[Block 3048]
དེ་དང་འདྲ་བར༌[^1932]ནི་མཐུན་པར་སྣང་བ་སྟེ། སྔོ་བའི་ཆུ་གང་ཡིན་པའོ། །

[Block 3049]
རྒྱ་མཚོ་ཡང་བླ་འོག་བཟློག་པ་འདྲའོ། །

[Block 3050]
ཞིང་ཞེས་བྱ་བ་ནི་ཁས་བུབ་ཏུའོ། །

[Block 3051]
སེར་བ་དྲག་པོ་འབབ་པ་འདྲ་ཞིང་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་འཇིགས་སུ་རུང་བའོ། །

[Block 3052]
སྨྱིག་མའི་ཚལ་མེས་ཚིག་སྟེ་ཏོག་ཡར་གྱིས༌[^1933]འགེངས་པ་དང་འདྲ་བར་ཐོས་ནས་ཀྱང་རབ་ཏུ་སྐྲག་ཅིང་འདར་བའོ། །

[Block 3053]
གཡང་ས་བཞིན་དུ་ཞེས་བྱ་བ་ནི་མྱུར་དུ་ལྟུང་བའི་ཕྱིར་རོ། །

[Block 3054]
གཅོང་རོང་བཞིན་དུ་ཞེས་བྱ་བ་ནི་བསྡུས་ནས་ལྟུང་བའི་ཕྱིར་རོ། །

[Block 3055]
བདག་ཅག་རྣ་བ་གས་ཤིང་ཞེས་བྱ་བའི་ཚིག་རྐང་འདིས་ནི་གང་གོང་དུ་བསྟན་པའི་འཇིགས་པ་བྱེད་པ་ཐོས་པར་གྱུར་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 3056]
ཆུའི་བདག་པོ་ཁྲོས་པ་འདྲ་བའི་ཞེས་བྱ་བའི་ཚིག༌[^1934]རྐང་འདིས་ནི་གང་དེ་སྔར་བསྟན་པའི་མེའི་ཏོག༌[^1935]ཡར་གྱིས་འགེངས་པ་འདྲ་བའི་སྒྲ་ཆེ་ཞིང་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3057]
འཇིགས་སུ་རུང་བ་ནི་དེའི་སྒྲ་ཤིན་ཏུ་ཆེ་བས་འཇིགས་སུ་རུང་བ་ཉིད་དུ་བསྟན་པ་སྟེ། དེ་ཉིད་འདིས་བསྟན་པའི་ཕྱིར། ཆུ་འདི་ཐམས་ཅད་གཅོང་རོང་འཇིགས་པའི་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ནི་གང་དེ་སྔར་བསྟན་པའི་ཆུའི་འཇིང༌[^1936]ཆེན་པོ་སྟེ༌[^1937]གཡང་ས་དང་གཅོང་རོང་གི་ནང་དུ་བབ་པ་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 3058]
མངོན་སོང་ཞེས་བྱ་བ་དེ༌[^1938]ནི་ཉེ་བར་གྱུར་པ་ཡིན་ཏེ། ཉེ་བར་ཕྱོགས་ཤིང་མངོན་དུ་བལྟས་པའམ་མངོན་དུ་ཕྱོགས་པ་ནི་མངོན་སོང་ངོ་། །ལྷ་དབང་གུས་པས་ཕྱག་འཚལ་ཞེས་བྱ་བ་ལ་ཉི་མ་ཞེས་སྨོས་པས་ལྷ་ཐམས་ཅད་གྲུབ་མོད་ཀྱི། སོ་སོར་སྨོས་པ་ནི་ལྷའི་བདག་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3059]
ཕོངས་པར་གྱུར་ལ་འཇིགས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3060]
གཞན་ལ་ཕན་འདོགས་ཡོན་ཏན་བསགས་པའི༌[^1939]ཞེས་བྱ་བ་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3061]
ཡང་ན་ཚིག་རྐང་དང་པོས་ནི་ཡོངས་སུ་སྐྱོབ་པའི་ནུས་པ་བསྟན་ཏོ། །

[Block 3062]
གཉིས་པས་ནི་བྱེད་པར་འདོད་པ་ཉིད་བསྟན་ཏོ། །

[Block 3063]
ཁྱོད་ཀྱི་མཐུ་ཆེན༌[^1940]ཁྱད་པར་ཅན། །ཞེས་བྱ་བ་དེས་ནི་རྣམ་པ་གཉིས་ཏེ། སྦྱོར་བའི༌[^1941]མཚན་ཉིད་ཀྱིས༌[^1942]ནུས་པའམ། བྱེད་པར་འདོད་པའི་མཚན་ཉིད་དོ། །

[Block 3064]
ཉམ་ཐག་པ་ནི༌[^1943]སྡུག་བསྔལ་བ༌[^1944]ཉིད་དོ། །

[Block 3065]
མགོན་མེད་པ་ནི༌[^1945]སྐྱབས་མེད་པར་གྱུར་པའོ། །

[Block 3066]
སྐྱབས་སུ་མཆིས་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་སྐྱབས་པའི་དོན་དུ་སྟེ། རྒྱུ་འདི་གསུམ་གྱིས་ནི་བདག་ཉིད་སྙིང་རྗེའི་གནས་སུ་སྟོན་པ་ཡིན་ནོ། །

[Block 3067]
ད་ནི་བཅོས་པའི་ཆེད་ཉིད་ལས་བརྩམས་ནས། སྐྱེ་བོ་ཆབ་ཀྱི་ནང་དུ་འགུམ་པ་འདི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། དེ་བས་ཞེས་བྱ་བ་ནི་ཁྱོད་ཀྱི་བཀའ་ལས་མི་འདའ་བས་ནའོ། །

[Block 3068]
བསད་པར་བདག་ནི་ཡོངས༌[^1946]མི་དྲན། །ཞེས་བྱ་བ་ནི་དུས་དེ་ཡན་ཆད་དུའོ། །

[Block 3069]
བདག་ནི་ཤེད་བྱེ་ཚུན་ཆད་དུ། །ཞེས་བྱ་བ་ནི་ཤེད་བྱེ་ཞིང་གོ་བ་ནས་བརྩམས་པའོ། །

[Block 3070]
བདག་གི་བསོད་ནམས་མཐུ་དག་གིས། །ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལས་ལྡོག་པའི་རྒྱུ་དེའི་བསོད་ནམས་ཀྱི་སྟོབས་སོ། །

[Block 3071]
ཡང་ན་སྐྱེ་བ་དུ་མ་ནས་བསགས་པའི་བསོད་ནམས་དེའི་མཐུས་སོ། །

[Block 3072]
གང་སྔར་བསྟན་པའི་ཆོས་ལ་གནས་ན་བདེན་པའི་ཚིག་ཙམ་གྱིས་ཀྱང་མ་རུང་བར་འགྱུར་བ་ལས་ཐལ་བར༌[^1947]འགྱུར་ན་དེའི༌[^1948]འབྲས་བུ་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བ་དེ་ཡང་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 3073]
གཞལ་མེད་ཁང་མཛེས་པའི་ཚུལ་དུ་ཞེས་བྱ་བ་ནི་མཐུན་པའི་རླུང་གིས་འགྲོ་བ་དང་ཆོས་མཐུན་པས་སོ། །

[Block 3074]
ཡང་ན་རང་དགར་ཞེས་བྱ་བ་ནི་རླུང་གི་དབང་མ་ཡིན་པར་ཡང༌[^1949]དེའི་བདེན་པའི་བྱིན་གྱི་བསོད་ནམས་ཀྱིས་ཡོངས་སུ་གཟུང་བས༌[^1950]སོ། །

[Block 3075]
ཉི་མ་ནུབ་པའི་ལམ་ཞེས་བྱ་བ་ནི་ནམ་མཁའོ། །

[Block 3076]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ལེགས་པར་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3077 [HEADING]]
## ཉའི་སྐྱེས་པའི་རབས། ^16-0

[Block 3078]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཉར་སྐྱེས་པ་འདི་ཉིད་དུ་དེའི་ཚུལ་ཁྲིམས་གཟུང་བ༌[^1951]ཡིན་ཏེ། ཟས་སུ་གྱུར་པའི་ནི་ནང་གི་ཉ་དག་ལས་སོ། །

[Block 3079]
མིར་གྱུར་པ་གཞན་དག་ལ་ནི༌[^1952]དགེ་བ་དང་མི་དགེ་བའི་ལས་ལ་གོམས་པ་འདི་ལྟ་བུ་མེད་པ་ཡིན་ཏེ། ཚེ་རབས་གཞན་དང་གཞན་དུ་གོམས་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3080]
དེ་ལྟ་བུ་དག་ཅེས་བྱ་བ་ནི་དགེ་བ་དང་མི་དགེ་བའི་ལས་རྣམས་སོ། །

[Block 3081]
མ་བསྒྲིབས་ཀྱང་ཞེས་བྱ་བ་ནི་གོམས་པར་བྱས་པའི་ཕྱིར་ཏེ། རྨི་ལམ་གྱི་ནང་བཞིན་དུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3082]
བྱམས་པ་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3083]
སྦྱིན་པ་དང་། ཚིག་འཇམ་པོ་དང་། དོན་སྤྱོད་པ་ལ་སོགས་པའི་རིམ་པས་རབ་ཏུ་ཕན་འདོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3084]
འདིར་ཇི་ལྟར་བསྡུ༌[^1953]བའི་དངོས་པོ་བཞིས་ཕན་འདོགས་པའི་དོན་ཡིན་ཞེ་ན། མཐུན་པར་བདག་དང་གཞན་ལ་ཕན་འདོགས་པར་འཇུག་པ་ནི་འདི་དག་གི་བསྡུས་པའི་དོན་ཏེ། འདིར་ནི་གཞན་ལ་ཕན་འདོགས་པ༌[^1954]རང་འཇུག་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའོ། །

[Block 3085]
རིམ་པ་ཞེས་སྨོས་པ་ནི་འདུལ་བའི་སྐྱེ་བོ་ལ་སྔོན་དུ་སྦྱིན་པར་བྱ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
