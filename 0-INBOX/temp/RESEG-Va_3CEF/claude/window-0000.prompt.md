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
[Block 1 [HEADING]]
### ༄༅། །དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པའི་འགྲེལ་པ།

[Block 2]
༄༅༅། །རྒྱ་གར་སྐད་དུ། མ་དྷྱཱན་ཏ་བི་བྷ་ག་ཊཱི་ཀ །བོད་སྐད་དུ། དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པའི་འགྲེལ་པ། བམ་པོ་དང་པོ། འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 3 [VERSE]]
བསྟན་བཅོས་འདི་ནི་རབ་མཛད་པ། །
བདེ་གཤེགས་ཉིད་སྐྱེས་བདག་སོགས་ལ། །
འཆད་པ་ལ་ཡང་མངོན་མཆོད་ནས། །
དོན་རྣམས་དབྱེ་ཕྱིར་འབད་པར་བྱ། །

[Block 4]
དེ་ལ་ཐོག་མ་ཁོ་ནར་བསྟན་བཅོས་ཀྱི་ལུས་རྣམ་པར་གཞག༌[^1]སྟེ།

[Block 5 [VERSE]]
མཚན་ཉིད་སྒྲིབ་པ་དེ་ཁོ་ན། །
གཉེན་པོ་དག་ནི་བསྒོམ་པ་དང་། །
དེ་ཡི་གནས་དང་འབྲས་བུ་ཐོབ། །
ཐེག་པ་བླ་ན་མེད་པའོ། །

[Block 6]
ཞེས་བྱ་བ་དོན་བདུན་པོ་འདི་དག་བསྟན་བཅོས་འདི་ལས་འཆད་དོ། །

[Block 7]
འདི་ལྟ་སྟེ། མཚན་ཉིད་དང་། སྒྲིབ་པ་དང་། དེ་ཁོ་ན་དང་། གཉེན་པོ་བསྒོམ་པ་དང་། གཉེན་པོ་བསྒོམ་པ་དེ་ཉིད་ཀྱི་གནས་དང་། འབྲས་བུ་ཐོབ་པ་དང་། ཐེག་པ་བླ་ན་མེད་པ་སྟེ་དོན་བདུན་པའོ། །

[Block 8 [HEADING]]
## མཚན་ཉིད། ^1-0

[Block 9 [HEADING]]
### ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ། ^1-1-0

[Block 10 [HEADING]]
#### ཡོད་པའི་མཚན་ཉིད། ^1-1-1-0

[Block 11 [VERSE]]
དེ་ལ་མཚན་ཉིད་ལས་བརྩམས་ནས། །
ཡང་དག་མ་ཡིན་ཀུན་རྟོག་ཡོད། །
དེ་ལ་གཉིས་པོ་ཡོད་མ་ཡིན། །
སྟོང་པ་ཉིད་ནི་འདི་ལ་ཡོད། །

[Block 12]
དེ་ལ་ཡང་ནི་དེ་ཡོད་དོ། །ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 13]
དེ་ལ་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པའི་ནི་གཟུང་བ་དང་འཛིན་པར་རྣམ་པར་རྟོག་པའོ། །

[Block 14 [HEADING]]
#### མེད་པའི་མཚན་ཉིད། ^1-1-2-0

[Block 15]
གཉིས་པོ་ནི་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོ་དང་བྲལ་བའོ། །

[Block 16]
སྟོང་པ་ཉིད་ནི་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པ་དེ་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོ་དང་བྲལ་བ་ཉིད་དོ། །

[Block 17]
དེ་ལ་ཡང་ནི་དེ་ཡོད་དོ། །ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པའོ། །

[Block 18]
དེ་ལྟར་གང་ན་གང་མེད་པ་དེ་ནི་དེས་སྟོང་པར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངོ་། །འདི་ལ་ལྷག་མ་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་འདིར་ཡོད་པར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ཏེ། དེ་ལྟར་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཕྱིན་ཅི་མ་ལོག་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 19 [VERSE]]
སྟོང་པ་མ་ཡིན་མི་སྟོང་མིན། །
དེ་ལྟ་བས་ན་ཐམས་ཅད་བཤད། །
ཡོད་པས་མེད་པས་ཡོད་པས་ན། །
དེ་ནི་དབུ་མའི་ལམ་ཡིན་ནོ། །

[Block 20]
སྟོང་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་དང་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོགས་པས༌[^2]སོ། །

[Block 21]
མི་སྟོང་མིན་ཞེས་བྱ་བ་ནི། །

[Block 22]
གཉིས་པ་སྟེ། གཟུང་བ་དང་འཛིན་པས་སོ། །

[Block 23]
ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་འདུས་བྱས་དང་སྟོང་པ་ཞེས་བྱ་བ་འདུས་མ་བྱས་སོ། །

[Block 24]
བཤད་ཅེས་བྱ་བ་ནི་བསྟན་པའོ། །

[Block 25]
ཡོད་པས་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པའོ། །

[Block 26]
མེད་པས་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 27]
ཡོད་པས་ན་ཞེས༌[^3]བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་ཀུན་ཏུ་རྟོག་པ་ལ་སྟོང་པ་ཉིད་ཡོད་པ་དང་། དེ་ལ་ཡང་ཡང་དག་པ་མ༌[^4]ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ཡོད་པའོ། །

[Block 28]
དེ་ནི་དབུ་མའི་ལམ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་གཅིག་ཏུ་སྟོང་པ་ཡང་མ་ཡིན་ནོ། །

[Block 29]
གཅིག་ཏུ་མི་སྟོང་པ་ཡང་མ་ཡིན་པ་གང་ཡིན་པའོ། །

[Block 30]
དེ་ལྟར་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ནང་ནས་འདི་ཐམས་ཅད་ནི་སྟོང་པ་ཡང་མ་ཡིན། མི་སྟོང་པ་ཡང་མ་ཡིན་ཞེས་འབྱུང་བ་དང་མཐུན་པར་བྱས་པ་ཡིན་ནོ། །

[Block 31 [HEADING]]
#### རང་གི་མཚན་ཉིད། ^1-1-3-0

[Block 32]
དེ་ལྟར་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ཡོད་པའི་མཚན་ཉིད་དང་མེད་པའི་མཚན་ཉིད་བརྗོད་ནས།

[Block 33 [VERSE]]
ད་ནི་རང་གི་མཚན་ཉིད་བརྗོད་དོ། །
དོན་དང་སེམས་ཅན་བདག་རྣམ་རིག །
སྣང་བའི་རྣམ་པར་ཤེས་པ་ནི། །

[Block 34 [VERSE]]
རབ་ཏུ་སྐྱེའོ༌[^5]དེའི་དོན་མེད། །
དེ་མེད་པས་ན་དེ་ཡང་མེད། །

[Block 35]
དེ་ལ་དོན་དུ་སྣང་བ་ནི་གཟུགས་ལ་སོགས་པའི་དངོས་པོར་སྣང་བ་གང་ཡིན་པའོ། །

[Block 36]
སེམས་ཅན་དུ་སྣང་བ་ནི་དབང་པོ་ལྔར་བདག་དང་གཞན་གྱི༌[^6]རྒྱུད་ལ་སྣང་བ་གང་ཡིན་པའོ། །

[Block 37]
བདག་ཏུ་སྣང་བ་ནི༌[^7]བདག་ཏུ་རྨོངས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད༌[^8]དོ། །

[Block 38]
རྣམ་པར་རིག་པར༌[^9]སྣང་བ་ནི༌[^10]རྣམ་པར་ཤེས་པ་དྲུག་རྣམས་སོ། །

[Block 39]
དེའི་དོན་མེད་ཅེས་བྱ་བ་ནི་དོན་དང་སེམས་ཅན་དུ་སྣང་བ་རྣམས་མེད་པ་དང་། བདག་དང་རྣམ་པར་རིག་པར་སྣང་བ་ནི་ལོག་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 40]
དོན་མེད་པས་འཛིན་པའི་རྣམ་པར་ཤེས་པ་དེ་ཡང་མེད་དོ། །

[Block 41 [VERSE]]
ཡང་དག་མ་ཡིན་ཀུན་རྟོག༌[^11]པ། །
དེ་ནི་དེ་ཕྱིར་གྲུབ་པ་ཡིན། །
དེ་བཞིན་མ་ཡིན་ཡེ་མེད་མིན། །

[Block 42]
འདི་ལྟར་ཇི་ལྟར་སྣང་བ་འབྱུང་བ་དེ་ནི་དེ་བཞིན་དུ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 43]
འཁྲུལ་པ་ཙམ་དུ༌[^12]འབྱུང་བའི་ཕྱིར་ཡེ་མེད་པ་ཡང་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་དེ་ཡེ༌[^13]མེད་པ་ཉིད་དུ་མི་འདོད་ཅེ་ན། འདི་ལྟར། དེ་ཟད་ནས་ནི་གྲོལ་བར་འདོད། །གཞན་དུ་ན༌[^14]བཅིངས་པ་དང་ཐར་པར་མི་འགྲུབ་སྟེ། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་ལ་སྐུར་པ་འདེབས་པའི་ཉེས་པར་འགྱུར་རོ། །

[Block 44 [HEADING]]
#### བསྡུ་བའི་མཚན་ཉིད། ^1-1-4-0

[Block 45]
དེ་ལྟར་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པའི་རང་གི་མཚན་ཉིད་བསྟན་ནས་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ཙམ་དུ་ཟད་ན་ངོ་བོ་ཉིད་གསུམ་དུ་ཇི་ལྟར་བསྡུ་བར་འགྱུར་བའི་བསྡུ་བའི་མཚན་ཉིད་སྟོན་ཏེ།

[Block 46 [VERSE]]
བརྟགས་པ་དང་ནི་གཞན་དབང་དང་། །
ཡོངས་སུ་གྲུབ་པ་ཉིད་ཀྱང་ངོ་། །
དོན་ཕྱིར་ཡང་དག་མིན་རྟོག་ཕྱིར། །
གཉིས་པོ་མེད་པའི་ཕྱིར་བཤད་དོ། །

[Block 47]
ཞེས་བྱ་བའོ། །

[Block 48]
དེ་ལ་དོན་ནི་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 49]
ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་དོ། །

[Block 50]
གཟུང་བ་དང་འཛིན་པ་མེད་པ་ཉིད་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 51 [HEADING]]
#### མེད་པའི་མཚན་ཉིད་ལ་འཇུག་པའི་ཐབས་ཀྱི་མཚན་ཉིད། ^1-1-5-0

[Block 52]
ད་ནི་ཡང༌[^15]དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་དེ་ཉིད་ཀྱི་མེད་པའི་མཚན་ཉིད་ལ་འཇུག་པའི་ཐབས་ཀྱི་མཚན་ཉིད་ཡོངས་སུ་སྟོན་ཏེ།

[Block 53 [VERSE]]
དམིགས་པ་ལ་ནི་བརྟེན༌[^16]ནས་སུ། །
མི་དམིགས་པ་ནི་རབ་ཏུ་སྐྱེ། །
མི་དམིགས་པ་ལ་བརྟེན༌[^17]ནས་སུ། །
མི་དམིགས་པ་ནི་རབ་ཏུ་སྐྱེ། །

[Block 54]
ཞེས་བྱ་བའོ། །

[Block 55]
རྣམ་པར་རིག་པ་ཙམ་དུ་དམིགས་པ་ལ་བརྟེན་ནས་དོན་མི་དམིགས་པ་སྐྱེའོ། །

[Block 56]
དོན་མི་དམིགས་པ་ལ་བརྟེན་ནས༌[^18]རྣམ་པར་རིག་པ་ཙམ་ཡང་མི་དམིགས་པ་སྐྱེ་སྟེ།[^19] དེ་ལྟར་གཟུང་བ་དང་འཛིན་པ་དག་མེད་པའི་མཚན་ཉིད་ལ་འཇུག་གོ། །

[Block 57 [VERSE]]
དེ་ཡི་ཕྱིར་ན་དམིགས་པ་ནི། །
མི་དམིགས་ངོ་བོ་ཉིད་དུ་གྲུབ། །

[Block 58]
དམིགས་པར་བྱ་བའི་དོན་མེད་ན་དམིགས་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 59 [VERSE]]
དེ་ལྟ་བས་ན་དམིགས་པ་དང་། །
མི་དམིགས་མཉམ་པར་ཤེས་པར་བྱ། །

[Block 60]
དམིགས་པ་ནི་དམིགས་པ་ཉིད་དུ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 61]
མི་དམིགས་པའི་ངོ་བོ་ཉིད་ཡིན་ཡང་ཡང་དག་པ་མ་ཡིན་པའི་དོན་དུ་སྣང་བས་དམིགས་པ་ཞེས་བྱའོ། །

[Block 62 [HEADING]]
#### རབ་ཏུ་དབྱེ་བའི་མཚན་ཉིད། ^1-1-6-0

[Block 63]
ད་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པ་ཉིད་ཀྱི་རབ་ཏུ་དབྱེ་བའི་མཚན་ཉིད་སྟོན་ཏེ།

[Block 64 [VERSE]]
ཡང་དག་མ་ཡིན་ཀུན་རྟོག་ནི། །
སེམས་དང་སེམས་བྱུང་ཁམས་གསུམ་པ། །

[Block 65]
ཞེས་བྱ་བའོ། །

[Block 66]
འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཐ་དད་པས་སོ། །

[Block 67 [HEADING]]
#### རྣམ་གྲངས་ཀྱི་མཚན་ཉིད། ^1-1-7-0

[Block 68]
རྣམ་གྲངས་ཀྱི་མཚན་ཉིད་ཀྱང་སྟོན་ཏེ།

[Block 69 [VERSE]]
དེ་ལ་དོན་མཐོང་རྣམ་པར་ཤེས། །
དེ་ཡི་ཁྱད་པར་སེམས་ལས་བྱུང་། །

[Block 70]
ཞེས་བྱ་བའོ། །

[Block 71]
[^20]དོན་ཙམ་མཐོང་བ་ནི་རྣམ་པར་ཤེས་པའོ། །

[Block 72]
དོན་གྱི་ཁྱད་པར་མཐོང་བ་ནི་སེམས་ལས་བྱུང་བ་རྣམས་ཏེ༌[^21]ཚོར་བ་ལ་སོགས་པའོ། །

[Block 73 [HEADING]]
#### འཇུག་པའི་མཚན་ཉིད། ^1-1-8-0

[Block 74]
འཇུག་པའི་མཚན་ཉིད་ཀྱང་སྟོན་ཏེ།

[Block 75 [VERSE]]
གཅིག་ནི་རྐྱེན་གྱི་རྣམ་པར་ཤེས། །
གཉིས་པ་ཉེ་བར་སྤྱོད་པ་ཅན། །
ཉེ་བར་སྤྱོད་དང་ཡོངས་གཅོད་དང་། །
དེ་ཡི་འཇུག་བྱེད་སེམས་ལས་བྱུང་། །

[Block 76]
ཞེས་བྱ་བའོ།

[Block 77]
[^22] །ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ནི་རྣམ་པར་ཤེས་པ་གཞན་དག་གི༌[^23]རྐྱེན་ཡིན་པས་རྐྱེན་གྱི་རྣམ་པར་ཤེས་པའོ། །

[Block 78]
དེ་ལས་བྱུང་བ་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ནི་ཉེ་བར་སྤྱོད་པ་ཅན་ནོ། །

[Block 79]
ཉེ་བར་སྤྱོད་པ་ནི༌[^24]ཚོར་བའོ། །

[Block 80]
ཡོངས་སུ་སྤྱོད་པ་ནི་འདུ་ཤེས་སོ། །
--- END BLOCKS ---
