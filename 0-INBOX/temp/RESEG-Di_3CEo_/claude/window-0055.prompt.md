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
སྐད་ཅིག་དང་པོ་ནས། ཕྱིན་ཆད་དུས་ནི་གཉིས་དང་པོ། འདས༌[^744]དང་ད་ལྟར་བ་དང་ཡང་ངོ་། །སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པར་གནས་པ་དག་ཀྱང་གདོན་མི་ཟ་བར་རྟག་ཏུ་དགེ་བ་དང་མི་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་པ་ཁོ་ན་མ་ཡིན་ཏེ། འོན་ཀྱང་སྡོམ་མིན་གནས་པ་དགེ་བ་དང་།

[Block 1927 [VERSE]]
སྡོམ་ལ་གནས་པ་མི་དགེ་བའི། །
རྣམ་རིག་མི་ལྡན་ཇི་སྲིད་དུ། །
རིག༌[^745]དང་ཉོན་མོངས་ཤུགས་ལྡན་པར། །

[Block 1928]
སྡོམ་པ་མ་ཡིན་པ༌[^746]ལ་གནས་པ་ནི་རབ་ཏུ་དང་བའི་ཤུགས་ཀྱིས་མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ན་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་ལ། སྡོམ་པ༌[^747]ལ་གནས་པ་ནི་ཉོན་མོངས་པའི་ཤུགས་གང་གིས་གསོད་པ་དང་འཆིང་བ༌[^748]ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ན་དེ་དག་ཇི་སྲིད་དུ་རྗེས་སུ་འབྲང་བ་དེ་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡང་ངོ་། །རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་སྐབས་བཤད་ཟིན་ཏོ། །

[Block 1929 [VERSE]]
རྣམ་རིག་བྱེད་ནི་ཐམས་ཅད་ལ། །
བྱེད་པ་དག་ལ་ད་ལྟར་ལྡན། །

[Block 1930]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་བར་མ་ལ་གནས་པ་ཐམས་ཅད་ཇི་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་བྱེད་པ་དེ་སྲིད་དུ་ད་ལྟར་གྱི་དང་ལྡན་ནོ། །

[Block 1931 [VERSE]]
མ་བཏང་བར་དུ་སྐད་ཅིག་མ། །
ཕྱིན་ཆད་འདས་ལྡན་མ་འོངས༌[^749]མེད། །

[Block 1932]
མ་འོངས་པའི་རྣམ་པར་རིག་བྱེད་ནི་སུ་དང་ཡང་མི་ལྡན་ནོ། །

[Block 1933 [VERSE]]
བསྒྲིབས་པ་དང་ནི་མ་བསྒྲིབས་པ། །
འདས་པ་དག་དང་ལྡན་པ་འང་མེད། །

[Block 1934]
ཆོས་ཉམ༌[^750]ཆུང་བའི་ཐོབ་པ་ཡང་ཉམ༌[^751]ཆུང་བ་ཡིན་པས་རྗེས་སུ་འབྲེལ་པ་ཅན་མ་ཡིན་ནོ། །

[Block 1935 [VERSE]]
སྡོམ་པའི་རྣམ་གྲངས་སྔར་བཤད་ནས། །
སྡོམ་པ་མ་ཡིན་པ་བརྗོད་དེ། །
སྡོམ་པ་མིན་དང་ཉེས་སྤྱད་དང་། །
འཆལ་བའི་ཚུལ་ཁྲིམས་ལས་དེའི་ལམ། །

[Block 1936]
སྡོམ་པ་མིན་པའི་རྣམ་གྲངས་ནི་སྡོམ་པའི་ལས་བཟློག་སྟེ་ཤེས་པར་བྱའོ། །

[Block 1937]
རྣམ་པར་རིག་བྱེད་དང་ལྡན་པ་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་མི་ལྡན་པ་ཞེས་བྱ་བ་མུ་བཞི་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 1938 [VERSE]]
བར་མ་དོར་གནས་སེམས་ཞན་པས། །
བྱེད་ན་རྣམ་རིག་ཉིད་དང་ལྡན། །

[Block 1939]
འདི་ནི་རེ་ཞིག་མུ་དང་པོ་ཡིན་ནོ། །

[Block 1940 [VERSE]]
རྣམ་རིག་བཏང་དང་མ་སྐྱེས་པའི། །
འཕགས་པའི་གང་ཟག་རྣམ་རིག་མིན། །

[Block 1941]
འཕགས་པའི་གང་ཟག་གང་ཞིག་ཚེ་གཞན་དུ་ཡོངས་སུ་གྱུར་ནས་ད་དུང་རྣམ་པར་རིག་བྱེད་མ་བྱུང་བའམ། རྣམ་པར་རིག་བྱེད་རྣམ་པར་ཉམས་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཁོ་ན་དང་ལྡན་ནོ་ཞེས་བྱ་བ་མུ་གཉིས་པའོ། །

[Block 1942]
གསུམ་པ་དང་བཞི་པ་ནི་གོ་སླའོ། །

[Block 1943 [HEADING]]
#### སྡོམ་པ་ཇི་ལྟར་འཐོབ་པ། ^4-2-4-0

[Block 1944]
ཡང་སྡོམ་པ་འདི་དག་ཇི་ལྟར་འཐོབ་ཅེ་ན། བསམ་གཏན་ལས་སྐྱེས་བསམ་གཏན་གྱི། །ས་ཉིད་ཀྱིས་འཐོབ། གང་གི་ཚེ་བསམ་གཏན་གྱིས༌[^752]སེམས་ཟག་པ་དང་བཅས་པ་དངོས་གཞི་བའམ། [^753]ཉེར་བསྡོགས་པ༌[^754]འཐོབ་པ་དེའི་ཚེ་བསམ་གཏན་གྱི་སྡོམ་པ་ཡང་འཐོབ་སྟེ། ལྷན་ཅིག་འབྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1945]
ཟག་མེད་ནི་འཕགས་དེས། དེ་ལ་བསམ་གཏན་བཞི་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དག་ཟག་པ་མེད་པའི་ས་ཡིན་ཏེ། དེ་ཐོབ་པས་ཟག་པ་མེད་པའི་སྡོམ་པ་འཐོབ་བོ། །

[Block 1946]
སོ་སོར་ཐར་ཅེས་པ། གཞན་གྱི་རྣམ་རིག་བྱེད་སོགས་ཀྱིས། །གལ་ཏེ་འདི་ལ་གཞན་གྱིས་རྣམ་པར་རིག་པར་བྱེད་ལ་འདི་ཡང་གཞན་ལས་ཏེ། དེ་ཡང་དགེ་འདུན་ནམ་གང་ཟག་ལས་འཐོབ་པའོ། །

[Block 1947]
སོགས་པའི་སྒྲས་རང་བྱུང་གིས་ནི་སངས་རྒྱས་རྣམས་ཀྱི༌[^755]ཞེས་བྱ་བ་ལ་སོགས་པ་བསྙེན་པར་རྫོགས་པ་རྣམས་བསྡུའོ། །

[Block 1948]
དེ་ལ་ཡང་།

[Block 1949 [VERSE]]
ཇི་སྲིད་འཚོ་དང་ཉིན་ཞག་ཏུ། །
སྡོམ་པ་ཡང་དག་བླང་བར་བྱ། །

[Block 1950]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་ཉིན་ཞག་ཏུའོ། །

[Block 1951 [VERSE]]
གཞན་ནི་ཇི་སྲིད་འཚོའི་བར་དུའོ། །
ཉིན་ཞག་པ་ཡི་སྡོམ་མིན་མེད། །
དེ་དེ་ལྟར་ནོད་མེད༌[^756]ཅེས་གྲག །

[Block 1952]
ཇི་སྲིད་འཚོའི་བར་དུ་སྡིག་པའི་ཁས་བླངས་པ་ལས་སྡོམ་པ་མ་ཡིན་པ་མི་སྐྱེ་ལ། ཉིན་ཞག་པ་ནི་མེད་དོ། །

[Block 1953]
བསྙེན་གནས་ཉིན་ཞག་ཏུ་མནོད༌[^757]ན་ཇི་ལྟར་དུ་མནོད་པར༌[^758]བྱ་ཞེ་ན།

[Block 1954 [VERSE]]
དམའ་བར་འདུག་སྨྲས་བཟླས་པ་ཡིས། །
མི་བརྒྱན་ནམ་ནི་ནང་པར༌[^759]དུ། །
བསྙེན་གནས་ཡན་ལག་ཚང་བར་ནི། །
ནང་པར་གཞན་ལས་མནོད་པར༌[^760]བྱ། །

[Block 1955]
དམའ་བར་འདུག་སྨྲས་བཟླས་པ་ནི། །བསྙེན་གནས་ཀྱི་སྡོམ་པ་སྐྱེ་བའི་དོན་དུའོ། །

[Block 1956]
འབོགས་པ་པོའི་ཚིག་གི་རྗེས་སུ་བཟླས་པར་བྱའི་སྔ་མའམ། མཉམ་དུ་མ་ཡིན་ནོ། །

[Block 1957]
དེ་ལྟར་ན་འདི་གཞན་ལས་མནོས་པ་ཡིན་ནོ། །

[Block 1958]
མི་བརྒྱན་པ་ནི་རྒྱན་ནར་མ་མ་གཏོགས་སོ། །

[Block 1959]
ནང་པར་མནོད་པར༌[^761]བྱ་སྟེ། ཉིན་ཞག་པའི་སྡོམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1960]
གང་གིས་ཆོས་བརྒྱད་ལ་རྟག་ཏུ་བསྙེན་གནས་ལ་གནས་པར་བྱའོ་ཞེས་སྔོན་ཡང་དག་པར་བླངས་པར་བྱས་པ་དེ༌[^762]ནི་ཟན་ཟོས་ཀྱང་མནོད་པར༌[^763]བྱའོ། །

[Block 1961]
གཞན་ལས་མནོད་པར༌[^764]བྱ་སྟེ། རྐྱེན་ཡོད་ཀྱང་མི་འདའ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1962]
དེ་ལས་གཞན་དུ་མནོས༌[^765]པས་ནི་ལེགས་པར་སྤྱད་པ་ཙམ་དུ་འགྱུར་གྱི།

[Block 1963]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཡན་ལག་བརྒྱད་ནོད་ཅེ་ན། །

[Block 1964 [VERSE]]
ཚུལ་ཁྲིམས་ཡན་ལག་བག་ཡོད་པའི། །
ཡན་ལག་བརྟུལ་ཞུགས་ཡན་ལག་སྟེ། །
བཞི་གཅིག་དེ་བཞིན་གསུམ་རིམ་བཞིན། །
ཡང་བག་ཡོད་པའི་ཡན་ལག་དང་། །

[Block 1965]
བརྟུལ་ཞུགས་ཀྱི་ཡན་ལག་འདི་དག་མནོས་པས་ཅིར་འགྱུར་ཞེ་ན། དེ་ཡིས་དྲན་ཉམས་དྲེགས་པར་འགྱུར། །མྱོས་པས་འགྱུར་བ་འཐུངས་པས་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པའི་དྲན་པ་ཉམས་པ་ཉིད་དུ་འགྱུར་རོ། །
--- END BLOCKS ---
