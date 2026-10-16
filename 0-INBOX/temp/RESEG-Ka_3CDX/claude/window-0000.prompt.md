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
## ༄༅། །རིགས་པའི་ཐིགས་པའི་ཕྱོགས་སྔ་མ་མདོར་བསྡུས་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ན་ཡ་བིནྡུ་པཱུརྦ་པཀྵེ་སཾ་ཀྵིཔྟ། བོད་སྐད་དུ། རིགས་པའི་ཐིགས་པའི་ཕྱོགས་སྔ་མ་མདོར་བསྡུས་པ། བཅོམ་ལྡན་འདས་ངག་གི་དབང་ཕྱུག་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## མངོན་སུམ་ལ་ལོག་པར་རྟོགས་པ། ^1-0

[Block 5]
ལོག་པར་རྟོགས་པ༌[^1]ནི་རྣམ་པ་བཞི་སྟེ། གྲངས་ལ་ལོག་པར་རྟོགས་པ༌[^2]དང་། རང་གི་ངོ་བོ་ལ་ལོག་པར་རྟོགས་པ༌[^3]དང་། སྤྱོད་ཡུལ་ལ་ལོག་པར་རྟོགས་པ༌[^4]དང་། འབྲས་བུ་ལ་ལོག་པར་རྟོགས༌[^5]པའོ། །

[Block 6 [HEADING]]
### གྲངས་ལ་ལོག་པར་རྟོགས་པ། ^1-1-0

[Block 7]
དེ་ལ་གྲངས་ལ་ལོག་པར་རྟོགས་པ༌[^6]ནི། འདི་ལྟ་སྟེ། ཕུར་བུ་བ་རྣམས་ནི་མངོན་སུམ་གཅིག་ཏུ་ཁོ་ན་ཚད་མ་ཡིན༌[^7]གཞན་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 8]
གྲངས་ཅན་པ་རྣམས་ནི་མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་དང་། སྒྲ་ལས་བྱུང་བ་དང་ཚད་མ་གསུམ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 9]
རིགས་པ༌[^8]ཅན་རྣམས་ནི་མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་དང་། དཔེ་དང་། སྒྲ་ལས་བྱུང་བ་དང་། ཚད་མ་བཞི་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 10]
རྒྱལ་དཔོག་པ་རྣམས་ནི་མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་དང་། དཔེ་དང་། སྒྲ་ལས་བྱུང་བ་དང་། དོན་གྱིས་གོ་བ་དང་། དངོས་པོ་མེད་པ་ཞེས་བྱ་བ་དང་། ཚད་མ་དྲུག་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 11]
ཙ་ར་ཀ་ལ་སོགས་པ་ནི། རིགས་པ་དང་། མི་དམིགས་པ་དང་། སྲིད་པ་དང་ཞེས་གྲགས་པ་དང་སྙམ་དུ་སེམས་པ་ཞེས་བྱ་བ་ཚད་མ་གཞན་དག་ཀྱང་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 12 [HEADING]]
### རང་གི་ངོ་བོ་ལ་ལོག་པར་རྟོགས་པ། ^1-2-0

[Block 13]
དེ་ལ་རང་གི་ངོ་བོ་ལ་ལོག་པར་རྟོགས་པ༌[^9]ནི། འདི་ལྟ་སྟེ། རིགས་པ་ཅན་རྣམས་ནི་མངོན་སུམ་དུ༌[^10]ཐམས་ཅད་ངེས་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར། རྣམ་པར་རྟོག་པ་དང་བཅས་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 14]
རྒྱལ་དཔོག་པ་རྣམས་ནི་གཏོད་པར་བྱེད་པའི་ཤེས་པ་སྐད་ཅིག་མ་དང་པོ་ཁོ་ན་རྣམ་པར་རྟོག་པ་མེད་པར་སྐྱེ་ལ། དེའི་འོག་རོལ་གྱི་མངོན་སུམ་ཐམས་ཅད་ནི་རྟོག་པ༌[^11]དང་བཅས་པ་ཉིད་དོ་ཞེས་ཟེར་རོ། །

[Block 15]
དེ་བཞིན་དུ་གཞན་དག་ནི་དུང་ལ་སེར་པོར་ཤེས་པ་ལ་སོགས་པར༌[^12]འཁྲུལ་པ་ཡང་ཚད་མ་ཉིད་ཡིན་པར་འདོད་དོ། །

[Block 16]
དེ་བཞིན་དུ་བྱེ་བྲག་པ༌[^13]ལ་སོགས་པ་ནི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་མ་ཡིན་པ་ཉིད་དེ། དབང་པོ་དང་། དོན་འབྲེལ་པ༌[^14]ཡིན་པར་བརྗོད་དོ། །

[Block 17]
ཁ་ཅིག་ནི་བདག་དང་ཡིད་འབྲེལ་པའི་ངོ་བོ་ཡིན་པར་བརྗོད་དོ། །

[Block 18]
གཞན་དག་ནི་མངོན་སུམ་རྣ་བ་ལ་སོགས་པའི་དབང་པོ་འཇུག་པའི་ངོ་བོ་ཡིན་པར་བརྗོད་དོ། །

[Block 19]
དེ་བཞིན་དུ་རྣ་མ་ཕུག་ལ་སོགས་པ་ནི་ཡིད་ཀྱི་ཞེས་བྱ་བའི་མངོན་སུམ་ཚད་མར་རིགས་པ་མ་ཡིན་ཏེ། སྔར་མངོན་སུམ་གྱིས་གཟུང་བ་ལས་ཡུལ་གཞན་མ་ཡིན་ན་དེ་བཟུང་ཟིན་པ་འཛིན་པའི་ཕྱིར་ཚད་མ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 20]
ཡུལ་དོན་གཞན་ཉིད་ཡིན་ན་ནི། འདི་རང་དབང་དུ་འཇུག་པའི་ཕྱིར་དང་། དོན་ཐམས་ཅད་ཡུལ་ཡིན་པའི་ཕྱིར། འགའ་ཡང་ལོང་བ་ལ་སོགས་པའི་དངོས་པོར་མི་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 21]
བྱེ་བྲག་ཏུ་སྨྲ་བ་ལ་སོགས་པ་ནི་རང་རིག་པའི་མངོན་སུམ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། བདག་ཉིད་ལ་བྱེད་པ་འགལ་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 22]
རྒྱལ་དཔོག་པ་རྣམས་ན་རེ་སྐྱེས་བུ་ཐམས་ཅད་ནི་འདོད་ཆགས་ལ་སོགས་པ་དང་མ་རིག་པས་འཁྲུལ་པ་ཡིན་ཏེ། འགྲོ་བ་འདི་ལྟ་བུ་མ་ཡིན་པ་ནི་འགའ་ཡང་མེད་དོ། །

[Block 23]
ཐམས་ཅད་ལ་དབང་པོས༌[^15]མི་སོད་པའི་དོན་མཐོང་བའི་ཐབས་མེད་པའི་ཕྱིར་ལ་མངོན་སུམ་ལ་སོགས་པའི་ཚད་མས་གྲུབ་པའི་རྣལ་འབྱོར་པ་དག་ཀྱང་མེད་དེ། དེའི་ཕྱིར་དབང་པོས་མི་སོད་པའི་དོན་མཐོང་བ་མི་སྲིད་པས་རྣལ་འབྱོར་པའི་ཤེས་པ་མེད་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 24 [HEADING]]
### ཡུལ་ལ་ལོག་པར་རྟོགས་པ། ^1-3-0

[Block 25]
དེ་ལ་ཡུལ་ལ་ལོག་པར་རྟོགས་པས༌[^16]ནི་འདི་ལྟ་སྟེ། རིགས་པ་ཅན་ལ་སོགས་པ་ན་རེ་སྤྱིའི་དངོས་པོར་གྱུར་པ་ཡང་ཡོད༌[^17]པའི་ཕྱིར་ལ། དེ་ཡང་མངོན་སུམ་གྱིས་ཡོངས་སུ་གཅད་པར༌[^18]བྱ་བ་ཡིན་པའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་མངོན་སུམ་ནི་སྤྱིའི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ཡང་ཡིན་ནོ། །

[Block 26]
དེ་བཞིན་དུ་བདག་ལ་སོགས་པར༌[^19]རང་གི་མཚན་ཉིད་ཀྱི་ངོ་བོ་ཡང་རྗེས་སུ་དཔག་པའི་ཚད་མས་ཡོངས་སུ་གཅད་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར། རྗེས་སུ་དཔག་པ་ཡང་དེའི་ཡུལ་ཅན་གྱི་ཚད་མས༌[^20]ཡིན་པར་རིགས་སོ་ཞེས་ཟེར་རོ། །

[Block 27 [HEADING]]
### འབྲས་བུ་ལ་ལོག་པར་རྟོགས་པ། ^1-4-0

[Block 28]
དེ་ལ་འབྲས་བུ་ལ་ལོག་པར་རྟོགས་པ༌[^21]ནི་འདི་ལྟ་སྟེ། རྒྱལ་དཔོག་པ་ལ་སོགས་པ་ན་རེ། འཇིག་རྟེན་ན་བསྒྲུབ་པར་བྱ་བ་དང་སྒྲུབ་པ་དག་ནི་ཕན་ཚུན་ཐ་དད་པའི་བདག་ཉིད་དུ་གྲགས་པའི་ཕྱིར། འབྲས་བུ་ནི་ཚད་མ་ལས་དོན་གཞན་དུ་གྱུར་པ་ཁོ་ན་ཡིན་པར་རིགས་ཏེ། དགྲ་སྟ་ཉིད་ཆད་པ་མ་ཡིན་ནོ། །

[Block 29]
[^22]དེ་ལྟ་བས་ན་དེ་ཁོ་ན་ཉིད་འདི་ནི་རྣམ་པ་བཞིར་ཡོངས་སུ་རྫོགས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འཇལ་བར་བྱེད་པ་དང་གཞལ་བྱ་དང་ཚད་མ་དང༌[^23]རྟོགས་པའོ། །

[Block 30]
འདི་ལ་འཇལ་བར་བྱེད་པ་ནི་སྐྱེས་བུ་ཡིན་ནོ། །

[Block 31]
གཞལ་བྱ་ནི་གཟུགས་ལ་སོགས་པའི་ཡུལ་ཡིན་ནོ། །

[Block 32]
ཚད་མ་ནི་དབང་པོ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 33]
རྟོགས་པ་ནི་དོན་ཡོངས་སུ་ཆོད་པ་ཡིན་ནོ། །

[Block 34]
གང་གི་ཚེ་ཤེས་པ་ཁོ་ན་ཚད་མ་ཡིན་པ་དེའི་ཚེ་ཡང་། ཤེས་པ་ཕྱི་མ་ཕྱི་མ་ནི་འབྲས་བུ་ཡིན་ལ། སྔ་མ་ནི་ཚད་མ་ཡིན་ཏེ། སྤྱི་ལ་སོགས་པའི་ཁྱད་པར་གྱི་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་ཚད་མ་ཡིན་ནོ། །

[Block 35]
རྫས་ལ་སོགས་པའི་ཁྱད་པར་ཅན་གྱི་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། གཞན་དག་དེ་ལྟར་མངོན་སུམ་ལ་ལོག་པར་རྟོགས་པ༌[^24]རྣམ་པ་མང་པོ་ཞིག་ཡོད་པ༌[^25]དེ་དག་དགག་པར་ཚད་མའི་མཚན་ཉིད་ཇི་ལྟ་བ་བཞིན་འདི་བྱས་སོ། །

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
--- END BLOCKS ---
