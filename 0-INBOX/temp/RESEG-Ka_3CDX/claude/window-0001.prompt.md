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
[Block 36 [HEADING]]
## བཅོམ་ལྡན་འདས་ཀྱང་བཞེད་པ། ^2-0

[Block 37]
འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱང་བཞེད་པ་ཁོ་ན་ཡིན་ཏེ། ཇི་སྐད་དུ།

[Block 38 [VERSE]]
དགེ་སློང་དག་གམ་མཁས་རྣམས་ཀྱིས། །
བསྲེགས༌[^26]བཅད་བདར་བས་གསེར་བཞིན་དུ། །
ཡོངས་སུ་བརྟགས་ནས་ང་ཡི་བཀའ། །
བླང་བར་བྱ་ཡི་གུས་ཕྱིར་མིན། །

[Block 39]
ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 40]
འདིས་ནི་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པའི་མཚན་ཉིད་རྣམ་པ་གཉིས་ཁོ་ན་ཞལ་གྱིས༌[^27]བཞེས་པ་ཡིན་ཏེ། དཔེ་ལ་སོགས་པས་ཡོངས་སུ་བརྟགས་པར་ཞལ་གྱིས་བཞེས་པའི་ཕྱིར་རོ། །

[Block 41]
མངོན་སུམ་གྱི་དཔེ་ནི་བསྲེགས༌[^28]པ་དང་ཆོས་མཐུན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 42]
རྗེས་སུ་དཔག་པ༌[^29]ནི་བདར་བ་དང་ཆོས་མཐུན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 43]
ཕན་ཚུན་དུ་མི་འགལ་བ་ནི་བཅད་པ༌[^30]དང་ཆོས་མཐུན་པར་ཡོངས་སུ་བརྟགས་པར་གསུངས་ཏེ། དེ་ཡང་རྗེས་སུ་དཔག་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 44]
འདི་ལྟར་དོན་ནི་རྣམ་པ་གསུམ་སྟེ། མངོན་སུམ་དང་། ལྐོག་ཏུ་གྱུར་པ་དང་། ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པའོ། །

[Block 45]
དེ་ལ་བཀའི་དོན་མངོན་སུམ་ལ་ནི་བསྲེགས་པས༌[^31]གསེར་བཞིན་དུ་མངོན་སུམ་གྱིས་བརྟགས་པ་ཡིན་ནོ། །

[Block 46]
དོན་ལྐོག་ཏུ་གྱུར་པ་ལ་ནི༌[^32]བདར་བ་བཞིན་དུ་རྗེས་སུ་དཔག་པས་བརྟགས་པ༌[^33]ཡིན་ནོ། །

[Block 47]
དེ་ཉིད་ཀྱི་དོན་ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་ལ་ནི་བཅད་པས་གསེར་བཞིན་དུ་ཕན་ཚུན་མི་འགལ་བའི་སྒོ་ནས་བརྟགས་པ༌[^34]ཡིན་ཏེ། དེ་ལྟར་ཡོངས་སུ་དག་པའི་ལུས༌[^35]ལ་ནི་ཡུལ་ལྐོག་ཏུ་གྱུར་ཀྱང་། རྟོག་པ་དང་ལྡན་པ་ཚད་མ་ཡིན་པར་ཡིད་ཆེས་པ་རྣམས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 48]
ཆོས་མངོན་པ་ལས་མིག་གི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པས་སྔོན་པོ་ཤེས་ཀྱི་སྔོན་པོའོ་སྙམ་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། དོན་ལ་དོན་དུ་ཤེས་ཀྱི་དོན་ལ་ཆོས་སུ་འདུ་ཤེས་པ་མ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། སྔོན་པོ་ཤེས་པ་དང་དོན༌[^36]དུ་འདུ་ཤེས་ཀྱི་ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་ཡུལ་ཕྱིན་ཅི་མ་ལོག་པར་བསྟན་པའི་ཕྱིར། མ་འཁྲུལ་པ་ཉིད་བཤད་པ་ཡིན་ནོ། །

[Block 49]
སྔོན་པོའོ་སྙམ་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། ཆོས་སུ་འདུ་ཤེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་མིང་དང་འབྲེལ་པའི་དོན་འཛིན་པ་སྤངས་པའི་ཕྱིར་རྟོག་པ་དང་བྲལ་བ་ཉིད་བཤད་པ་ཡིན་ཏེ། དེ་ཉིད་ལས་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་ངེས་པར་རྟོག་པ་དང་། རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པས། རྣམ་པར་མི་རྟོག་པ་ཉིད་དུ་ཡང་བརྗོད་པར༌[^37]མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་གཟུགས་ལ་སོགས་པའི་སྐྱེ་མཆེད་ཀྱི་རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ཡིན་པར་ཡང་བསྟན་ཏོ། །

[Block 50]
མདོ་ལས་ཀྱང་།

[Block 51 [VERSE]]
འདུ་བྱེད་ཐམས་ཅད་སྐད་ཅིག་མ། །
མི་གནས་བྱ་བ་ག་ལ་ཡོད། །
འདི་དག་འབྱུང་བ་དེ་ཉིད་ནི། །
བྱ་བ་དེ་ཉིད་བྱེད་པོར༌[^38]བརྗོད། །

[Block 52]
ཅེས་གསུངས་ཏེ། འདིས་ནི་བྱེད་པ་པོ་དང་ལས་ལ་སོགས་པའི་དངོས་པོ་ཡང་དག་པར༌[^39]བཀག་པས་བྱ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་ཁོངས་སུ་འདུས་པ་སྤངས་པའི་ཕྱིར། བྱ་བའི་མཚན་ཉིད་ཀྱི་འབྲས་བུ་དོན་གཞན་དུ་གྱུར་པ་བཀག་པ་ཡིན་ནོ། །

[Block 53 [HEADING]]
## རྗེས་སུ་དཔག་པ་ལ་ལོག་པར་རྟོགས་པ། ^3-0

[Block 54]
རྗེས་སུ་དཔག་པ་ལ་ཡང་ལོག་པར་རྟོགས་པ་སྣང་སྟེ། འདི་ལྟ་སྟེ། བརྡ་སྤྲོད་པ་རྣམས་ནི་རྗེས་སུ་དཔག་པ་ཚད་མ་མ་ཡིན་ཏེ། འཁྲུལ་པ་སྲིད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 55 [HEADING]]
### ཚུལ་གསུམ་པ། ^3-1-0

[Block 56]
སྣོད་ཀྱི་རྗེས་ན་རེ་ནི་གཞན་དུ་མི་འཐད་པའི་ངོ་བོ་གཅིག་པུ་ཁོ་ན་གཏན་ཚིགས་ཀྱིས༌[^40]རྟོགས་པར་བྱེད་པ་ཉིད་ཀྱི་ཡན་ལག་ཡིན་གྱི། ཕྱོགས་ཀྱི་ཆོས་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱི་ཚུལ་གསུམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 57]
འདི་ལྟར་སྔོ་བསངས་ཡིན་ཏེ་དེའི་བུ་ཡིན་པའི་ཕྱིར། དེའི༌[^41]བུ་སྣང་བ་ཡིན༌[^42]ནོ་ཞེས་བྱ་བའི་གཏན་ཚིགས་འདི་ལ་ཚུལ་གསུམ་པ་ཡོད་ཀྱང་གཞན་དུ་མི་འཐད་པ་ཉིད་ཀྱི་ཡན་ལག་མེད་པའི་ཕྱིར་རྟོགས་པར་བྱེད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 58]
ཚུལ་གསུམ་པ་མེད་ཀྱང་གཞན་དུ་མི་འཐད་པ་དང་ལྡན་པ་ཙམ་ཁོ་ནས་གཏན་ཚིགས་རྟོགས་པར་བྱེད་པ་ཡིན་པ་ཡང་མཐོང་སྟེ། འདི་ལྟ་སྟེ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་ནི་ཇི་ལྟར་ཡང་ཡོད་པའི་བདག་ཉིད་དག་ཡིན། ཇི་ལྟར་ཡང་དམིགས་པའི་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 59]
འདི་ལ་ནི་ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པའི་དཔེ་དག་མེད་དེ། དངོས་པོ་ཐམས་ཅད་ཀྱི་ཚོགས་དངོས་པོ་དང་། དངོས་པོ་མེད་པ་ཕྱོགས་སུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 60]
དེ་དག་ལ་མ་གཏོགས་པ་གཞན་མེད་པའི་ཕྱིར་གང་ཞིག་དཔེ་ཉིད་ཡིན་པར་འགྱུར། ཕྱོགས་ཀྱི་ཆོས་ཀྱང་གཞན་དུ་མི་འཐད་པ་ཉིད་ཁོ་ནའི་ཁོངས་སུ༌[^43]འདུས་པའི་ཕྱིར་རོ། །

[Block 61]
དེ་ལྟར་ན་རྟགས་ནི་ཚུལ་གཅིག་པ་ཁོ་ན་ཡིན་པར་རིགས་ཀྱི་ཚུལ་གསུམ་པ་ཉིད་ནི་མ་ཡིན་པའི་རིགས་སོ་ཞེས་ཟེར་རོ། །

[Block 62]
གཞན་དག་ནི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་དང་། མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་ཉིད་དང་། མི་མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་ཉིད་དང་། གནོད་པ་མེད་པའི་ཡུལ་ཅན་ཉིད་དང་། བརྗོད་པར༌[^44]འདོད་པའི་གྲངས་གཅིག་པ་ཅན་ཉིད་དང་། ཤེས་པ་ཉིད་ཅེས་བྱ་བ་མཚན་ཉིད་དྲུག་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 63]
གྲངས་ཅན་པ་རྣམས་ན་རེ་རྗེས་སུ་དཔག་པ་ནི་འབྲེལ་པ་གཅིག་ལས་ལྷག་མ་གྲུབ་པ་ཡིན་ནོ། །

[Block 64]
ལྷག་མ་གྲུབ་པ་ནི་འདིར་ཉེ་བར་བཏགས་པའི་སྒོ་ནས་རྟགས་ཤེས་པ་ཁོ་ན་ཡིན་ཏེ། རྗེས་སུ་དཔག་པར་འདོད་ཀྱི། རྗེས་སུ་དཔག་པར་བྱ་བ་ཤེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 65]
སློབ་དཔོན་དབྱིག་གཉེན་ཡང་མེད་ན་མི་འབྱུང་བའི་དོན་མཐོང་བའི་དེར༌[^45]རིག་པའི་རྗེས་སུ་དཔག་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདི་ཡང་རྗེས་སུ་དཔག་པ་ནི་རྟགས་ཤེས་པ་ཁོ་ན་ཡིན་ལ། རྗེས་སུ་དཔག་པར་བྱ་བ་ཤེས་པ་ནི་འབྲས་བུ་ཡིན་པར་འདོད་དེ། ཕྱིར་རྒོལ་བ་འདི་ཐམས་ཅད་ནི་འབྲས་བུ་ཚད་མ་ལས་དོན་གཞན་ཁོ་ན་ཡིན་པར་ཡང་འདོད་པ་ཉིད་དོ། །

[Block 66]
བྱེ་བྲག་པ་ལ་སོགས་པ་ནི་ཡང་དག་པར་མ་གྲུབ་པ་ཡང་གཏན་ཚིགས་སུ་ཉེ་བར་རྟོགས་པར་བྱེད་དེ། འདི་ལྟ་སྟེ། བདག་ནི་ཐམས་ཅད་ནི༌[^46]ཡོད་པ་ཡིན་ཏེ། ཐམས་ཅད་ན་ཡོན་ཏན་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 67]
རྒྱལ་དཔོག་པ་ལ་སོགས་པ་ནི་མི་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་ཡང་གཏན་ཚིགས་སུ་ཉེ་བར་བརྟེན་ཏེ། འདི་ལྟ་སྟེ། སྒྲ་ནི་རྟག་པ་སྟེ། གཞལ་བྱ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་བརྗོད་པར༌[^47]འདོད་པའི་སྐྱེས་བུ་འགའ་ཞིག་ཐམས་ཅད་མཁྱེན་པ་མ་ཡིན་ཏེ། གཞལ་བྱ་དང་། ཤེས་བྱ་དང་། དངོས་པོ་དང་། ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 68]
དེ་རྣམ་པར་གཅད་པའི༌[^48]ཕྱིར་ངེས་པར་གཟུང་བ༌[^49]ཡིན་ནོ། །

[Block 69]
གྲངས་ཅན་པ་ལ་སོགས་པ་ནི་གཏན་ཚིགས་འགལ་བར་མཐོང་བཞིན་དུ་ཡང་ཤིན་ཏུ་ངོ་མཚར་ཆེ་བའི་མ་རིག་པས་བློ་གྲོས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པས་མི་འགལ་བ་བཞིན་དུ་རྟོགས་པར་བྱེད་དེ། འདི་ལྟ་སྟེ། མིག་ལ་སོགས་པ་ནི་གཞན་གྱི་དོན་ཡིན་ཏེ། བསགས་པ་ཡིན་པའི་ཕྱིར། མལ་ཆ་དང་སྟན་ལ་སོགས་པའི་ཡན་ལག་བཞིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 70]
དེ་རྣམ་པར་གཅད་པའི༌[^50]ཕྱིར། མི་མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་སྨོས་སོ། །

[Block 71]
གང་དག་རང་གི་ཕྱོགས་གྲུབ་པར་བྱ་བའི་ཕྱིར། མི་མཐུན་པའི་ཕྱོགས་གཅིག་ལ་ཡོད་པ་ལ༌[^51]ཡང་གཏན་ཚིགས་སུ་རྟོགས་པར༌[^52]བྱེད་དེ། འདི་ལྟ་སྟེ། སྒྲ་ནི་རྟག་པ་སྟེ། བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་དེ་རྣམ་པར་གཅད་པའི་ཕྱིར་ངེས་པའི་གཟུང༌[^53]བ་ཡིན་ནོ། །

[Block 72]
གཉི་གར་ཡང་ཁྱད་པར་ཅན་གྱི་གནས་སུ་ངེས་པར་གཟུང་བ་ནི་བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ལ་སོགས་པ་མཐུན་པའི་ཕྱོགས་གཅིག་ལ་ཡོད་པ་ཡང་མི་རྟག་པ་ཉིད་ལ་སོགས་པ༌[^54]སྒྲུབ་པ་ཉིད་དུ་འགལ་བ་མེད་དོ་ཞེས་བྱ་བ༌[^55]རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 73]
ཚུལ་གསུམ་པའི་དངོས་ཀྱི་ཚུལ་དུ་ཡོད་ཀྱང་ཇི་སྲིད་དུ་རྟོགས་པར་མ་གྲུབ་པ༌[^56]དེ་སྲིད་དུ་དེ་ལ༌[^57]བསྒྲུབ་པར་བྱ་བ་རྟོགས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^58]རབ་ཏུ་བསྟན་པའི་ཕྱིར། ངེས་པའི༌[^59]ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་དཔེར་བརྗོད་པ་ཡང་འདི་ཉིད་ལས་སྟོན་པར་འགྱུར་རོ། །

[Block 74]
རྗེས་སུ་དཔག་པར་བྱ་བ་ཆོས་དང་ཆོས་ཅན་གྱི་སྤྱི་ཡིན་པའི་ཕྱིར། དེ་མ་གྲུབ་པ་དེ་ལ་རྟག་པ༌[^60]ཡོད་པ་རྟག་ཏུ་མ་གྲུབ་པ་ཁོ་ནའོ། །

[Block 75]
འོན་ཏེ་སྒྲུབ་ན་ནི་བསྒྲུབ་པར་བྱ་བ་སྔ་ཉིད་ནས་གྲུབ་པའི་ཕྱིར། རྟགས་ཀྱི་རྗེས་སུ་འབྲང་བ་དོན་མེད་དོ་ཞེས་བྱ་བའི་ཀླན་ཀ་ཡོངས་སུ་སྤང་བའི་ཕྱིར། འདི་ལས་རྗེས་སུ་དཔག་པར་བྱ་བ་ནི། འདིར་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་དོ། །
--- END BLOCKS ---
