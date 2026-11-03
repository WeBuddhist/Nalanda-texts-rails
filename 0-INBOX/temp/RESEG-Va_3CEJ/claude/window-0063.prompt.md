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
[Block 2206]
མུ་གཉིས་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་དང་པོ་དང་སེམས་དང་བཅས་པའི་གནས་སྐབས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 2207]
མུ་གསུམ་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་དང་པོ་དང་། སེམས་དང་བཅས་པའི་གནས་སྐབས་དག་གོ། །

[Block 2208]
མུ་བཞི་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པ་དང་། ལྡང་བའི་སེམས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 2209]
ཆོས་གང་དག་སེམས་ཀྱི་མཚུངས་པ་དེ་མ་ཐག་པ་ཅན་ཡིན་པ་དེ་དག་སྙོམས་པར་འཇུག་པའི་དེ་མ་ཐག་པ་ཅན༌[^1171]ཡིན་ནམ་ཞེ་ན། མུ་བཞི་སྟེ།

[Block 2210]
གསུམ་པ་དང་བཞི་པ་གང་དག་ཡིན་པ་དེ་དག་ནི་དང་པོ་དང་གཉིས་པ་དག་གོ། །

[Block 2211]
དང་པོ་དང་གཉིས་པ་གང་དག་ཡིན་པ་དེ་དག་ནི་གསུམ་པ་དང་བཞི་པ་གང་དག་ཡིན་པར་བཤད་དོ། །

[Block 2212]
ད་ནི་ཇི་ལྟར་ལྡང་བའི་སེམས་ཡུན་རིང་མོ་ཞིག་ཏུ་ཆད་པ་སྙོམས་པར་འཇུག་པའི་སེམས་ཀྱི་མཚུངས་པ་དེ་མ་ཐག་པ་ཞེས་བྱ་ཞེ་ན། སེམས་གཞན་གྱིས་མཆོད་པའི་ཕྱིར་རོ། །

[Block 2213]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་བཤད་ཟིན་ཏོ། །

[Block 2214 [HEADING]]
##### དམིགས་པའི་རྐྱེན། ^2-5-1-3-0

[Block 2215]
དམིགས་པ་ཆོས་རྣམས་ཐམས་ཅད་དོ། །

[Block 2216]
ཅི་རིགས་པར་མིག་གི་རྣམ་པར་ཤེས་པ་མཚུངས་པར་ལྡན་པ་དང་བཅས་པའི་ནི་གཟུགས་སོ། །

[Block 2217]
རྣ་བའི་རྣམ་པར་ཤེས་པའི་ནི་སྒྲའོ། །

[Block 2218]
སྣའི་རྣམ་པར་ཤེས་པའི་ནི༌[^1172]དྲིའོ། །

[Block 2219]
ལྕེའི་རྣམ་པར་ཤེས་པ༌[^1173]ནི་རོའོ། །

[Block 2220]
ལུས་ཀྱི་རྣམ་པར་ཤེས་པ༌[^1174]ནི་རེག་བྱའོ། །

[Block 2221]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི༌[^1175]ཆོས་ཐམས་ཅད་དོ། །

[Block 2222]
ཆོས་གང་ཞིག་ཆོས་གང་གི་དམིགས་པ་ཡིན་པའི་ཆོས་དེ་ནི་མི་དམིགས་ཀྱང་དེ་ལྟ་བུའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ནམ་ཡང་དམིགས་པ་མ་ཡིན་ཏེ། དཔེར་ན་ཤིང་ལ་སོགས་པ་མི་སྲེག་ཀྱང་དེ་ལྟ་བུའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་བུད་ཤིང་ཞེས་བྱ་བ་བཞིན༌[^1176]ནོ། །

[Block 2223]
སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་སྐྱེ་མཆེད་དང་། རྫས་དང་། སྐད་ཅིག་མ་ངེས་པས་དམིགས་པ་ལ་སྐད་ཅིག་བདག་ཉིད་ཇི་ལྟ་བར་ངེས་པ་འདི་དག་ཅི་རྟེན་ངེས་པས་ཀྱང་ངེས་པ་ཞིག་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་དེ་བཞིན་ཏེ། སྐྱེས་པ་རྣམས་ནི༌[^1177]རྟེན་དང་ལྷན་ཅིག་པ་དག་ཡིན་ནོ། །

[Block 2224]
མ་སྐྱེས་པ་རྣམས་དང་། འདས་པ་རྣམས་ནི་རྟེན་དང་མ་འབྲེལ་པ་དག་ཡིན་ནོ། །

[Block 2225]
གཞན་དག་ན་རེ་འདས་པ་རྣམས་ཀྱང་རྟེན་དང་ལྷན་ཅིག་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2226]
དམིགས་པའི་རྐྱེན་བཤད་ཟིན་ཏོ། །

[Block 2227 [HEADING]]
##### བདག་པོའི་རྐྱེན། ^2-5-1-4-0

[Block 2228]
བྱེད་རྒྱུ་ཞེས་བྱ་བདག་པོར་བཤད། །བྱེད་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ཉིད་བདག་པོའི་རྐྱེན་ཡིན་ནོ། །

[Block 2229]
རྐྱེན་འདི་ནི་ལྷག་པ་ཡིན་པས་བདག་པོའི་རྐྱེན་ཏོ། །

[Block 2230]
དམིགས་པའི་རྐྱེན་ཡང་ཆོས་ཐམས་ཅད་ཡིན་ལ། བདག་པོའི་རྐྱེན་ཡང་ཆོས་ཐམས་ཅད་ཡིན་ན་འདི་ལ་ལྷག་པ་ཅི་ཞིག་ཡོད་ཅེ་ན། ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་ནི་ནམ་ཡང་དམིགས་པ་མ་ཡིན་གྱི་བདག་པོའི་རྐྱེན་ནི་ཡིན་པས་འདི་ལ་ལྷག་པ་ཡོད་པ་ཉིད་དོ། །

[Block 2231]
ཡང་ན་ལྷག་པའི་རྐྱེན་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་རང་གི་ངོ་བོ་མ་གཏོགས་པའི་འདུས་བྱས་ཐམས་ཅད་ཀྱི་ཡིན་ནོ། །

[Block 2232]
རྐྱེན་བཞི་ཆར་གྱིས་ཀྱང་ཆོས་ཀྱི་རྐྱེན་མ་ཡིན་པའི་ཆོས་ལྟ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། རང་གི་ངོ་བོས་རང་གི་ངོ་བོ་ལྟ་བུའོ། །

[Block 2233]
གཞན་གྱི་ངོ་བོ་ཡང་ཡོད་དེ། འདུས་མ་བྱས་ཀྱི་འདུས་བྱས་ལྟ་བུ་དང་། འདུས་མ་བྱས་ཀྱི་འདུས་མ་བྱས་ལྟ་བུའོ། །

[Block 2234 [HEADING]]
#### རྐྱེན་འདི་དག་བྱ་བ་བྱེད་པ། ^2-5-2-0

[Block 2235]
ཡང་རྐྱེན་འདི་དག་བྱ་བ་བྱེད་པ་ན་གནས་སྐབས་གང་གི་ཆོས་ལ་བྱེད་ཅེ་ན།

[Block 2236]
རེ་ཞིག་རྒྱུའི་རྐྱེན་རྣམ་པ་ལྔར་བཤད་པ་དེ་ལས།

[Block 2237]
རྒྱུ་གཉིས་པོ་དག་འགག་པ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2238]
འགག་པ་ཞེས་བྱ་བ་ནི་ད་ལྟར་ཡིན་ཏེ། འགག་པ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 2239]
དེ་ལ་ནི་ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་བྱ་བ་བྱེད་དེ། དེ་གཉིས་ནི་ལྷན་ཅིག་འབྱུང་བའི་འབྲས་བུ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2240]
གསུམ་པོ་ནི་སྐྱེ་བ་ལའོ། །

[Block 2241]
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་མ་འོངས་པ་སྟེ། སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་ཡིན་ནོ། །

[Block 2242]
དེ་ལ་ནི་སྐལ་བ་མཉམ་པ་དང་། ཀུན་ཏུ་འགྲོ་བ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་རྣམས་བྱ་བ་བྱེད་དེ། རེ་ཞིག་རྒྱུའི་རྐྱེན་ནི་དེ་ལྟ་བུ་ཡིན་ནོ།[^1178] །དེ་ལས་གཞན་པའི་རྐྱེན་དག་དེ་ལས་བཟློག་པ་ཡིན། མཚུངས་པ་དེ་མ་ཐག་པ་དང་། དམིགས་པའི་རྐྱེན་དག་ནི་བྱེད་པའི་ཚུལ་གང་གིས་རྒྱུའི་རྐྱེན་རྣམ་པ་གཉིས་སུ་བྱས་ནས་བཤད་པ་དེ་ལས་བཟློག་པར་རིག་པར་བྱ་སྟེ། མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སྐབས་འབྱེད་པའི་ཕྱིར་སྐྱེ་བ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2243]
དམིགས་པའི་རྐྱེན་ནི་ད་ལྟར་གྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱིས་འཛིན་པའི་ཕྱིར་འགག་པ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2244]
བདག་པོའི་རྐྱེན་ནི་གནས་སྐབས་ཐམས་ཅད་དུ་མི་སྒྲིབ་པའི་ངོ་བོར་གནས་པས་འདིའི་བྱ་བ་ནི་འདི་ཉིད་ཡིན་ནོ། །

[Block 2245]
རྐྱེན་རྣམས་བྱེད་པ་དང་བཅས་པར་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
