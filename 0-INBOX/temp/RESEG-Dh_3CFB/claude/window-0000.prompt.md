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
### ༄༅། །ཚད་མ་རྣམ་འགྲེལ་གྱི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། པྲ་མཱ་ཎཱ་བ་ཏཱ་ར་ཏི་ཀ་བྲྀཏྟི། བོད་སྐད་དུ། ཚད་མ་རྣམ་འགྲེལ་གྱི་འགྲེལ་པ། བམ་པོ་དང་པོ།

[Block 4 [VERSE]]
ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །
རྟོག་པའི་དྲ་བ་རྣམ་བསལ་ཞིང་། །
ཟབ་ཅིང་རྒྱ་ཆེའི་སྐུ་མངའ་བ། །
ཀུན་ཏུ་བཟང་པོའི་འོད་ཟེར་དག །
ཀུན་ནས་འཕྲོ་བར༌[^1]ཕྱག་འཚལ་ལོ། །

[Block 5 [VERSE]]
སྐྱེ་བོ་ཕལ་ཆེར་ཕལ་ལ་ཆགས་ཤིང་ཤེས་རབ་རྩལ་མེད་པས་ན་ལེགས་བཤད་རྣམས། །
དོན་དུ་མི་གཉེར་ཁོ་ནར་མ་ཟད་ཕྲག་དོག་དྲི་མ་དག་གིས་སྡང་བར་ཡང་། །
ཡོངས་གྱུར་དེས་ན་བདག་ལ་འདི་ནི་གཞན་ལ་ཕན་པ་ཡིན་ཞེས་བསམ་པའང་མེད། །
སེམས་ནི་ཡུན་རིང་ལེགས་བཤད་གོམས་པས་ལྷུར་ལེན་བསྐྱེད་ཕྱིར་འདི་ལ་དགའ་བ་སྐྱེས། །

[Block 6 [HEADING]]
## ཕྱོགས་ཆོས་དེའི་ཆས་ཁྱབ་པའི་གཏན་ཚིགས། ^1-0

[Block 7]
དོན་དང་དོན་མ་ཡིན་པ་རྣམ་པར་འབྱེད་པ་ནི་རྗེས་སུ་དཔག་པ་ལ་བརྟེན་པ་ཡིན་པའི་ཕྱིར་ལ། དེ་ལ་ལོག་པར་རྟོགས་པས༌[^2]དེ་རྣམ་པར་གཞག་པའི་ཕྱིར་བཤད་པ།

[Block 8 [VERSE]]
ཕྱོགས་ཆོས་དེའི་ཆས་ཁྱབ་པ་ཡི། །
གཏན་ཚིགས་དེ་ནི་རྣམ་གསུམ་སྟེ། །
མེད་ན་མི་འབྱུང་ངེས་ཕྱིར་རོ། །
གཏན་ཚིགས་ལྟར་སྣང་དེ་ལས་གཞན། །

[Block 9]
ཕྱོགས་ནི་ཆོས་ཅན་ནོ། །

[Block 10]
གལ་ཏེ་དགོས་པ་མེད་པའི་ཕྱིར་ཉེ་བར་གདགས་པར་མི་བྱའོ་ཞེ་ན། མ་ཡིན་ཏེ། ཆོས་ཅན་གྱི་ཆོས་ཐམས་ཅད་ཡིན་པ་དགག་པའི་ཕྱིར་ཏེ། དེའི་ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར། དེ་ཉེ་བར་གདགས་སུ་རུང་བའི་ཆོས་ཅན་ཡིན་པར་རྟོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 11]
དེ་ལྟ༌[^3]ཡིན་དང་མིག་གིས་གཟུང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྤངས་པ་ཡིན་ནོ། །

[Block 12]
གལ་ཏེ་ཆོས་ཞེས་བརྗོད་པས་ཀྱང་ཆོས་ཅན་ཡིན་པར་གཞི་ལྟ་གྲུབ་སྟེ། ཆོས་ཅན་ཞེས་སྨོས་པའི་ཤུགས་ཀྱིས་ཉེ་བ༌[^4]ཡིན་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཅན་ཡིན་པར་གྲུབ་པོ་ཞེ་ན། མ་ཡིན་ཏེ། དཔེའི་ཆོས་ཅན་ཡང་ཉེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 13]
དེའི་ཆས༌[^5]ཁྱབ་པ་ཞེས་བྱ་བས་དཔེའི་ཆོས་ཅན་ལ་ཡོད་པ་གྲུབ་པས་ཆོས་ཅན་གྱི་ཆོས་ཞེས་སྨོས་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཅན་ཡིན་པར༌[^6]ཡོངས་སུ་གཟུང་ངོ་ཞེ་ན། གྲུབ་བཞིན་དུ་བསྣན་པའི་ཕྱིར་ཡང་སྨོས་པ་ཡིན་པར་ཡང་དགོས་པར་འགྱུར་ཏེ། མཐུན་པ་ཁོ་ན་ལ་ཡོད་པ་ཞེས་བྱ་བ༌[^7]མི་མཐུན་པ་ལས་ལྡོག་པ་གྲུབ་མོད་ཀྱི། བསྒྲུབ་པར་བྱ་བ་མེད་པ་ལ་མེད་པ་སྨོས་པ་བཞིན་ནོ། །

[Block 14]
ཤུགས་ཀྱིས་དོན་གོ་ན་རྟོགས་པར་དཀའ་བ་ཡོངས་སུ་སྤང་བའི༌[^8]ཕྱིར་ཡང་ཕྱོགས་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 15]
གལ་ཏེ་ཕྱོགས་ཀྱི་ཆོས་ཉིད་ཡིན་ན་དེའི་ཁྱད་པར་ལ་ལྟོས་པ་གཞན་ལ་མི་འཇུག་པའི་ཕྱིར་ཐུན་མོང་མ་ཡིན་པ་ཉིད་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དཔེར་ན་ནག་པ་འཕོང་སྐྱེན་ནོ་ཞེས་བྱ་བ་ལྟ་བུར་མི་ལྡན་པ་རྣམ་པར་བཅད་པས་ཁྱད་པར་དུ་བྱས་པའི་ཕྱིར་ཡིན་གྱི། དཔེར་ན་སྲིད་སྒྲུབ་འཕོང་སྐྱེན་ནོ། །ཞེས་བྱ་བ་ལྟ་བུར༌[^9]གཞན་དང་ལྡན་པ་རྣམ་པར་བཅད་པས་ནི་མ་ཡིན་ནོ།[^10] །བཤད་པར་བྱའོ། །

[Block 16]
དེའི་ཆ་ནི་སྨྲ་བ་པོའི་བསམ་པའི་དབང་གིས་དེའི་ཆོས་ཡིན་གྱི། དེའི་ཕྱོགས་གཅིག་ནི་མ་ཡིན་ཏེ། ཕྱོགས་ཞེས་བྱ་བའི་སྒྲ་སྤྱི་ལ་མི་བྱ་བའི་ཕྱིར་རོ། །

[Block 17]
ཁྱབ་པ་ནི་དེ་ལ་ཁྱབ་པར་བྱེད་པ་ཡོད་པ་ཁོ་ནའམ། ཡང༌[^11]དེ་ཁོ་ན་ལ་ཁྱབ་པར་བྱ་བ་ཡོད་པ་ཡིན་ནོ། །

[Block 18]
འདིས་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་ངེས་པ་དག་ཀྱང་བདག་ཉིད་ཇི་ལྟ་བའི་ཚད་མས་བཤད་ལ། ཕྱོགས་ཀྱི་ཆོས་ཀྱང་བཤད་པ་ཡིན་ནོ། །

[Block 19]
དེ་དག་ནི་འབྲས་བུ་དང་། རང་བཞིན་དང་། མི་དམིགས་པའི་མཚན་ཉིད་ཅན་གྱི་གཏན་ཚིགས་གསུམ་ཡིན་ཏེ། དཔེར་ན་དུ་བ་ལས་ནི་འདི་ན་མེ་ཡོད་དོ། །

[Block 20]
ཤིང་ཤ་པ་ཡིན་པའི་ཕྱིར་འདི་ནི་ཤིང་ཡིན་ནོ། །

[Block 21]
ཕྱོགས་ཀྱི་ཁྱད་པར་འགའ་ཞིག་ན་བུམ་པ་མེད་དེ། [^12]དམིགས་པའི་མཚན་ཉིད་ཀྱིར་གྱུར་པ་མི་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་ནོ། །

[Block 22]
གལ་ཏེ་ཡོད་ན་དམིགས་པར་རུང་བའི་ཡོད་པ་ཅན་ཁོ་ནར་འགྱུར་གྱི། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 23]
དེས་ན་དམིགས་པའི་མཚན་ཉིད་ཀྱིར་འགྱུར་བའི་ཡོད་པ་ཅན་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 24]
དེ་ལས་གཉིས་ནི་དངོས་པོ་སྒྲུབ་པ་ཡིན་ལ། གཅིག་ནི་དགག་པའི་གཏན་ཚིགས་ཡིན་ཏེ། རང་བཞིན་དང་འབྲེལ་པ་ཡོད་པ༌[^13]དོན་གྱིས་དོན་འཁྲུལ་པ་མེད་དེ། དེ་ནི་དེའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 25]
གལ་ཏེ་དེའི་བདག་ཉིད་ཡིན་ན་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པའི་བྱེ་བྲག་མེད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། ཆོས་ཀྱི་བྱེ་བྲག་ཀུན་བརྟགས་པའི་ཕྱིར་རོ། །ཞེས་བཤད་པར་བྱའོ། །

[Block 26]
དེ་སྐད་དུ་རྗེས་སུ་དཔག་པ་དང་། རྗེས་སུ་དཔག་པར་བྱ་བའི་ཐ་སྙད་འདི་ཐམས་ཅད་ནི་བློ་ལ་ཡོད་པའི་ཆོས་དང་ཆོས་ཅན་གྱི་བྱེ་བྲག་ཁོ་ནས་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 27]
ཆོས་དང་ཆོས་ཅན་ཉིད་དུ་ཐ་དད་པ་བློའི་རྣམ་པས་བྱས་ཀྱི་དོན་ཀྱང་ནི་མ་ཡིན་ཏེ། བློའི་བྱེ་བྲག་རང་དགའ་བ་རྣམས་ནི་དོན་གྱི་རྟེན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 28]
དེ་དག་གིས་བརྟགས་པའི་ཡུལ་གྱིས་དོན་གོ་ན་ནི་དོན་མི་འཐོབ་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 29]
འབྲས་བུ་ཡང་རང་བཞིན་དང་འབྲེལ་པ་ཡིན་ཏེ། དེའི་རང་བཞིན་དེ་ལས་བྱུང་བའི༌[^14]ཕྱིར་རོ། །

[Block 30]
རྗེས་སུ་དཔག་པར་བྱ་བ་ཤེས་པ་འདི་གཉིས་ནི་དངོས༌[^15]ལས་མ་སྐྱེས་པའི་ཕྱིར་དེར་སྣང་བ་ཉིད་མ་ཡིན་ཡང་། དེ་ལས་སྐྱེས་པའི་ཕྱིར་དེར་འཁྲུལ་པ་མེད་པ་དག་ཡིན་ཏེ། དེས་ན་མཚན་མ༌[^16]ཡིན་ཏེ་མངོན་སུམ་བཞིན་ནོ། །

[Block 31]
མངོན་སུམ་གྱི་ཚད་མ་ཉིད་ཀྱང་དོན་འཁྲུལ་པ་མེད་པ་ཁོ་ན་ཡིན་ཏེ། དེ་མེད་པར་འབྱུང་བ་ནི་དེར་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 32]
གཞན་གྱི་མི་འཁྲུལ་པ་ཡང་དེ་ལས་སྐྱེས་པ༌[^17]ལས་གཞན་ཅི་ཞིག་ཡོད་དེ། རག་མ་ལས་པའི་ངོ་བོ་རྣམས་ནི་ལྷན་ཅིག་འབྱུང་བར་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 33]
གལ་ཏེ་དེ་ལས་སྐྱེ་བའི་ཕྱིར། འབྲས་བུ་གོ་བར་བྱེད་པ་ཡིན་ན་རྣམ་པ་ཐམས་ཅད་དུ་གོ་བར་བྱ་བ་དང་གོ་བར་བྱེད་པའི་ངོ་བོ་ཡིན་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད༌[^18]པ༌[^19]ཡོད་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་མེད་པར་འབྱུང་བ་ནི་དེ་ལས་སྐྱེ་བ་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 34]
དེ་ལྟ་བས་ན།

[Block 35 [VERSE]]
རྒྱུ་ལ་རང་བཞིན་ཇི་སྙེད་ཅིག །
[^20]མེད་ན་མི་འབྱུང་འབྲས་བུ་ནི། །

[Block 36]
དེ་དག་གི་གཏན་ཚིགས་ཡིན་ཏེ། དེ་དག་གི་འབྲས་བུ་ཉིད་དུ་ངེས་པའི་ཕྱིར་རོ། །

[Block 37]
གང་དག༌[^21]དེ་དག་མེད་ན་མི་འབྱུང་བ་དེ་དག་ཁོ་ནས་ཡིན་ནོ། །

[Block 38]
གལ་ཏེ་ཆ་ཤས་ཀྱིས་བསྐྱེད་པར་བྱ་བ་དང་། སྐྱེད་པ་ཡིན་པར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེས་བསྐྱེད་པར་བྱ་བའི་ཁྱད་པར་དང་། རྟགས་ཀྱི་བྱེ་བྲག་གི་ཁྱད་པར་ཅན་གྱི་སྤྱི་རྣམས་གཟུང་ན་ཡིན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 39]
སྤྱི་ཁྱད་པར་དུ་མ་བྱས་པ་བརྗོད་པར་འདོད་ན་ནི་འཁྲུལ་པའི་ཕྱིར་མི་འདོད་དོ། །

[Block 40]
རང་བཞིན་ཡོད་ཙམ་དང་། འབྲེལ་པ་ཅན་གྱི་ངོ་བོ་ཡང་གཏན་ཚིགས་ཡིན་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཏན་ཚིགས་ཀྱི་དེའི་བདག་ཉིད་ནི་དེ་ཙམ་དང་འབྲེལ་པ་ཅན་ཁོ་ནའི་ཕྱིར་རོ། །
--- END BLOCKS ---
