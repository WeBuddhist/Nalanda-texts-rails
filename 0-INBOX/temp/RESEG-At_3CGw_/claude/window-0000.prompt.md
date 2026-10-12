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
## ༄༅། །མདོ་ཀུན་ལས་བཏུས་པའི་དོན་བསྡུས་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། སཱུ་ཏྲ་ས་མུཙྪ་ཡ་སཉྩ་ཡ་ཨརྠཿ། བོད་སྐད་དུ། མདོ་ཀུན་ལས་བཏུས་པའི་དོན་བསྡུས་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## མདོ་ཀུན་ལས་བཏུས་པའི་དོན། ^1-0

[Block 5 [HEADING]]
### རྟེན་དལ་འབྱོར་གྱི་མདོ། ^1-1-0

[Block 6]
སློབ་དཔོན་ནཱ་གཱརྫུ་ནས་མཛད་པའི་རིན་པོ་ཆེའི་གཏམ་བརྗོད་པ་མདོ་ཀུན་ལས་བཏུས་པའི་དོན་ནི། མན་ངག་གི་མདོ་རྣམ་པ་བདུན་གྱིས་སྒྲུབ་པའི་ཐབས་ཁྱད་པར་ཅན་རྟོགས་པར་བྱ་སྟེ། བསྒོམ་ཞིང་ཉམས་སུ་བླང་བ་ནི། འདི་ལྟ་སྟེ། རྟེན་དལ་འབྱོར་གྱི༌[^1]མདོ་དང་། གཞི་དད་པའི་མདོ་དང་། རྩ་བ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་མདོ་དང་། རྐྱེན་བར་ཆད་སེལ་བའི༌[^2]མདོ་དང་། སྒྲུབ་པ་ནན་ཏན་སྙིང་པོར་བྱ་བའི་མདོ་དང་། བློ་ཐེག་པ་གཅིག་ཏུ་སྦྱང་བའི༌[^3]མདོ་དང་། ལམ་ཆེ་བ་ཡོན་ཏན་གྱིས་བགྲོད་པའི་མདོའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྲིད་པ་མས་ཆགས་པ་ཐམས་ཅད་ནི་རླུང་གི་དཀྱིལ་འཁོར་ལ་བརྟེན་ནས་མས་ཆགས་པ་བཞིན་དུ་དཀར་པོའི་ཆོས་ཐམས་ཅད་ནི་རྟེན་དལ་འབྱོར་ཕུན་སུམ་ཚོགས་པ་ལ་བརྟེན་ནས་འབྱུང་བར་འགྱུར་རོ། །

[Block 7 [HEADING]]
### གཞི་དད་པའི་མདོ། ^1-2-0

[Block 8]
དཔེར་ན་རྩི་ཤིང་དང་། མེ་ཏོག་དང་ཤིང་གེལ་པ་དང་། སྨན་ལ་སོགས་པ་ཐམས་ཅད་ནི་ས་གཞི་ལ་བརྟེན་ནས་སྐྱེ་བར༌[^4]འགྱུར་བ་དེ་བཞིན་དུ། ཡོན་ཏན་གྱི་ཆོས་ཐམས་ཅད་བསྲུང་ཞིང་འཕེལ་བར་བྱེད་པའི་གཞི་དད་པ་ལ་བརྟེན་ནས་རྒྱས་པར་འགྱུར་རོ། །

[Block 9 [HEADING]]
### རྩ་བ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་མདོ། ^1-3-0

[Block 10]
དཔེར་ན་རྩ་བའམ། ས་བོན་མ་ནོར་བ་ལས་སྡོང་བུ་དང་། ཡལ་ག་དང་ལོ་མ་དང་། མེ་ཏོག་དང་། འབྲས་བུ་ཐམས་ཅད་རིམ་གྱིས་རྒྱས་ཤིང་སྨིན་པར་འགྱུར་བ་དེ་བཞིན་དུ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་སེམས་བསྐྱེད་པའི་རྩ་བ་ལས་ཐམས་ཅད་མཁྱེན་པའི་འབྲས་བུ་འབྱུང་བར་འགྱུར་གྱི། ཉན་ཐོས་པ་དང་། རང་སངས་རྒྱས་པ་དང་། འཇིག་རྟེན་པ་རྣམས་ཀྱི༌[^5]སེམས་བསྐྱེད་པ་ལས་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 11]
དེ་ལྟ་བས་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དང་། ཐུན་མོང་མ་ཡིན་པའི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་། ཚད་མེད་པ་བཞི་དང་། དགེ་སྦྱོང་གི་འབྲས་བུ་བཞི་དང་། རྩ་བ་དང་། བདག་དང་། བདེ་བ་དང་། རྟག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐོབ་པར་འདོད་པས་ཐམས་ཅད་མཁྱེན་པ་ཉིད་སེམས་བསྐྱེད་པའི་རྩ་བ་བརྟན་པོར་གཟུང་བར་བྱའོ། །

[Block 12 [HEADING]]
### རྐྱེན་བར་ཆད་སེལ་བའི་མདོ། ^1-4-0

[Block 13]
དཔེར་ན་ནས་དང་། གྲོ་དང་སཱ་ལུ་ལ་སོགས་པའི་ས་བོན་ལེགས་པར་བཏབ་ཅིང་རྩ་བ་ལེགས་པར༌[^6]བཙུགས་ཀྱང་། སད་དང་སེར་བ་དང་བཙའ་ལ་སོགས་པས། བར་མ་སྐབས་སུ་བར་ཆད་བྱས་ནས། འབྲུའི་ཚོགས་སྨིན་པར་མི་འགྱུར་ཞིང་། ཁམ་གྱི་ཟས་ཀྱིས༌[^7]འཚོ་བར་བྱེད་པའི་ལུས་ཅན་རྣམས་ལ་ཡང་ཕན་འདོགས་པར་མི་བྱེད་དོ། །

[Block 14]
དེ་བཞིན་དུ་དལ་འབྱོར་ཐོབ་ཅིང་དད་པ་ལ་གནས་པས་བྱང་ཆུབ་སེམས་ཀྱི་ས་བོན་མ་ནོར་བར་བཏབ་སྟེ་རྩ་བ་མ་ནོར་བར་བཙུགས་ཀྱང་། བར་མ་སྐབས་སུ་སེམས་ཅན་བློས་སྤོང་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལ་རྨ་འབྱིན་པ་དང་། བདུད་ཀྱི་ལས་སྣ་ཚོགས་པ་དང་། དམ་པའི་ཆོས་སྤོང་བ་དང་། མི་དགེ་བ་བཅུ་དང་། སྤྲོ་བ་མེད་པ་ལ་སོགས་པ་ཚེ་འདི་དང་། མ་འོངས་པའི་ལུས་ལ་གནོད་པ་རྣམས་ཀྱིས་བར་དུ་གཅད༌[^8]ན། བདག་ཉིད་ཀྱང་ཅི་རིགས་པར་རྟེན་མཆོག་ལས་ཉམས་ནས་མི་ཁོམ་པའི་གནས༌[^9]ལྟུང་བ་དང་། ཐེག་པ་མཆོག་ལས་ཉམས་ནས་ཉི་ཚེ་བའི་ཐེག་པར་ལྟུང་བ་དང་། བརྩོན་འགྲུས་མཆོག་ལས༌[^10]ཉམས་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལས་རིང་དུ་འགྱུར་བའོ།[^11] །

[Block 15]
དེའི་ཕྱིར་བརྒྱུད༌[^12]ནས་གཞན་གྱི་དོན་ལས་ཀྱང་ཉམས་པར་འགྱུར་ཏེ། རང་དང་གཞན་གྱི་དོན་ཐམས་ཅད་ཆུད་ཟོས་པར་འགྱུར་རོ། །

[Block 16 [HEADING]]
### སྒྲུབ་པ་ནན་ཏན་སྙིང་པོར་བྱ་བའི་མདོ། ^1-5-0

[Block 17]
དཔེར་ན་ཡིད་བཞིན་གྱི་ནོར་བུ་རིན་པོ་ཆེ་བཙའ༌[^13]རྫིས་ལེགས་པར་མ་བསྐྱངས་ན་བག་མེད་པས་བརླག་པར་འགྱུར་བའི་ཉེན་མཆིས་སོ། །

[Block 18]
དེ་བཞིན་དུ་ཐོབ་པ་ཆུད་མི་གསན་པ་དང་། དད་པ་བརྟན་པོ་དང་། རྩ་བ་མི་འགྱུར་བ་དང་། གནོད་པའི་བར་ཆད་བསལ་བ་ལ་སྒྲུབ་པ་ནན་ཏན་སྙིང་པོར་མ་བྱས་ན། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ནོར་བུ་རིན་པོ་ཆེ་གཏན་རླག་པའི༌[^14]ཉེན་མཆིས་སོ། །

[Block 19 [HEADING]]
### བློ་ཐེག་པ་གཅིག་ཏུ་སྦྱང་བའི་མདོ། ^1-6-0

[Block 20]
དཔེར་ན་ལམ་ཁ་བྲག་ཕྱིན་པ་གང་དུ་འགྲོ་བའི་ཕྱོགས་ལ་ཡིད་འཁྲུགས་ཤིང་ནེམ་ནུར་ཅན་དུ་འགྱུར་རོ། །

[Block 21]
དེ་བཞིན་དུ་སེམས་ལྟ་བ་སྣ་ཚོགས་ཀྱིས་གཟེངས་པར་གྱུར་ན་ཆོས་ཐམས་ཅད་ཀྱི་དེ་ཁོ་ན༌[^15]ཉིད་རྟོགས་པར་མི་འགྱུར་བས་བློ་གྲོས་ཐེག་པ་སྣ་ཚོགས་སུ་འགྲོ་བའི་ཉེན་མཆིས་སོ། །

[Block 22 [HEADING]]
### ལམ་ཆེ་བ་ཡོན་ཏན་གྱིས་བགྲོད་པའི་མདོ། ^1-7-0

[Block 23]
ཕྱིའི་ལོ་ཏོག་ཕུན་སུམ་ཚོགས་པར་འདོད་པས། དོ་གཅིག་སོ་ནམ་ལ་ནན་ཏན་བྱེད་པ་དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་ཆེ་བའི་ཡོན་ཏན་ཐམས་ཅད་ཐོབ་པར་འདོད་པས་ཀྱང་དེ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་ལམ་མ་བགྲོད་ན་ལས་དང་པོ་པའི་ས་ལས་མི་འཕགས་པར་མཆིའོ། །

[Block 24]
དེའི་ཕྱིར་ན་ཤིང་རྟ་ཆེན་པོས་བསྡུས་པའི་མདོ་ནི་མི་མང་ཞིང་མི་ཉུང་བར་དེ་ཁོ་ནའོ། །

[Block 25]
གོ་རིམས་ཀྱང་འདི་ལྟར་ཤེས་ཏེ།

[Block 26]
དང་པོ་གསུམ་ནི་རྒྱུ་བྱ་བ་བྱེད་པའི་རིགས་པ་ཡིན་ལ་བར་མ་གསུམ་ནི་རྐྱེན་ལྟོས་པའི་རིགས་པ་ཡིན་ཞིང་ཐ་མ་ནི་འབྲས་བུ་ཆོས་ཉིད་ཀྱི༌[^16]རིགས་པ་ཡིན་ཏེ། དཔེ་བདུན་ནི་འཐད་པ་སྒྲུབ་པའི༌[^17]རིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 27]
དེ་ལ། སངས་རྒྱས་འབྱུང་བ་རྙེད་པར་དཀའ། །ཞེས་བྱ་བ་ལ་སོགས་པས་རྐྱེན་གཞན་གྱི་འབྱོར་པ་ལྔ་མཚོན་ལ། མིར་གྱུར་པ་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱུ་བདག་ཉིད་ཀྱི་འབྱོར་བ་ལྔ་མཚོན་ནོ། །

[Block 28]
དལ་འབྱོར་རྙེད་པར་དཀའ་ཞེས་བྱ་བས་རྒྱུ་རྐྱེན་ཚོགས་པའི་དལ་འབྱོར་བཅུ་མཚོན་པ་ཡིན་ནོ། །

[Block 29]
དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་དད་པ་རྙེད་པར་དཀའ་ཞེས་པས་གཞི་དད་པ་བསྟན། བྱང་ཆུབ་ཀྱི་སེམས་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡུལ་སངས་རྒྱས་ལ་དམིགས་པའི་སེམས་བསྐྱེད་པ་བསྟན། སེམས་ཅན་ཐམས་ཅད་ལ་སྙིང་རྗེ་ཆེན་པོ་སྐྱེ་བར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་སེམས་ཅན་ལ་དམིགས་པའི་སེམས་བསྐྱེད་པ་བསྟན། བྱང་ཆུབ་སེམས་དཔའ་ལ་རྨ་འབྱིན་པ་ཞེས་བྱ་བ་ནས་བར་དུ་གཅོད་པའི་ཆོས་སྤོང་བ་རྙེད་པར་དཀའ་ཞེས་བྱ་བའི་བར་གྱིས༌[^18]རྐྱེན་བར་ཆད་བསལ་བའི་མདོ་བསྟན། ཁྱིམ་པར་གྱུར་ཀྱང་ཆོས་རྣམས་ལ་ནན་ཏན་གྱིས་གཅེས་པར་བསྒྲུབ་པ་རྙེད་པར་དཀའ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྒྲུབ་པ༌[^19]ནན་ཏན་སྙིང་པོར་བྱེད་པའི་མདོ་བསྟན། མྱ་ངན་ལས་འདས་པ་ལ་མོས་པའི་སེམས་ཅན་རྙེད་པར་དཀའ་ཞེས་པ་ནས་ཐེག་པ་གཅིག་ལ་མོས་པའི་སེམས་ཅན་རྙེད་དཀའ་ཞེས་བྱ་བའི་བར་གྱིས་བློ་ཐེག་པ་གཅིག་ལ་སྦྱང་བའི་མདོ་བསྟན། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་ཆེ་བ་ཉིད་རྒྱ་ཆེན་པོ་ལ་འཇུག་པའི་སེམས་ཅན་ནི༌[^20]རྙེད་པར་དཀའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ལམ་ཆེ་བའི་ཡོན་ཏན་གྱིས་བགྲོད་པའི་མདོ་བསྟན། དེ་ལྟར་རིགས་པ་བཞིས་མདོར་བསྟན། ལུང་གི་མདོ་བདུན་གྱིས་རྒྱས་པར་བཤད་པའི་དོན་དེ་བློ་ལ་གོ་བར་བྱས་ནས་ཉམས་སུ་བླངས་པས་ན་སེམས་བསྐྱེད་པའི་རིགས་བཞི་སྐྱེ་སྟེ།

[Block 30]
དང་པོ་གཡོ་སྨོན་གྱི་ཚུལ་དང་། འཇུག་ཅིང་བསྟན་པ་དང་གནས་པ་དང་མཐར་ཕྱིན་པའི་རིམ་པའོ། །

[Block 31]
དེ་ཡང་དང་པོ་ས་བོན་དང་ཟླ་གྲངས༌[^21]དང་། ཡོན་ཏན་མཐོང་ཐོས་དང་། བྱིན་རླབས་ཀྱི་སྲུང༌[^22]མ་རྣམས་ཀྱིས་རྩྭ་མེ༌[^23]བཞིན་དུ་སྐྱེ་བོ༌[^24]དེའི་གཞིའི༌[^25]སྟེང་དུ་སྙིང་རྗེ་དང་ལྡན་པ་ལ་གོམས་པས་ཟླ་བ་ཡར་ངོ་བཞིན་དུ་འཕེལ་བའི་ཚེ་དབང་དང་ཡོ་བྱད་ལ་སོགས་པ་འཇུག་ཅིང་བསྟན་པའི་ཡན་ལག་ཏུ་འགྱུར་རོ། །

[Block 32]
དེ་ནས་གནས་པ་གསུམ་གྱི་མཐུ་རྫོགས་པར་བྱེད་པ་ཁ་ཅིག་འཕགས་པ་རྟོགས་པ་ཆེན་པོ་ཡོངས་སུ་རྒྱས་པའི་མདོ་ལས་འགྱོད་ཚངས་ཀྱིས་སྡིག་པ་སྦྱང་སྟེ།[^26] མཆོད་བསྟོད་དང་། སྐྱབས་སུ་གསོལ་བ་དང་། དབང་གཟུགས་པ་དང་། དངོས་པོ་བཤགས་པ་དང་། དམ་བཅའ་ཞིང་སྡོམ་པ་གཟུང་བ་དང་། ཁྲུས་བྱ་བ་དང་། ཚངས་པ་ཐོབ་པ་དང་། རྗེས་སུ་སྤྲོ་བ་དང་། གཟེངས་བསྟོད་པའི་ཚུལ་གྱིས་གདམས་པ་དང་། དམིགས་པ་མེད་ཅིང་ཐེག་པ་གཅིག་ཏུ་བློ་སྦྱང་བ༌[^27]དང་། དག་པའི་མཚན་མ་མཐོང་བ་དང་། མིང་གདགས་པ་དང་། ལམ་རྒྱུད་ལ་བསྐྱེད་པ་དང་། འབྲས་བུ་ཐོབ་པའི་བར་དུ་བྱེད་དོ། །

[Block 33]
ཁ་ཅིག་ནི་དེ་བཞིན་གཤེགས་པའི་ཡི་གེ་བརྒྱ་པ་ལ་སོགས་པ་ཟློས་ཤིང་སྒྲའི་མཐའ་ལས་གྲོལ་བའི་ཏིང་ངེ་འཛིན་གྱི་བར་དུ་སྦྱོར་ཞིང་ཁྲིམས་ཉི་ཤུ་རྩ་ལྔ་བསྲུངས་པས་འབྲས་བུ་འཐོབ་པར༌[^28]བྱེད་དོ། །

[Block 34]
གང་ཞིག་སེམས་དཔའ་གསུམ་གྱི་མཐུ་རྫོགས་པས་ན་ཉི་མ་གྲོལ་བ་ལྟར་དུ་མཐར་ཕྱིན་པའི་སེམས་སུ་གྱུར་པའི་ཚེ་བློ་སྙིང་རྗེའི་དབང་དུ་གྱུར་པས་སྒྱུ་མའི་དཔེ་བདུན་པོ་ལྟར་དངོས་པོ་ཐམས་ཅད་ལ་མ༌[^29]ཆགས་ཤིང་རློམ་པ་མེད་པར་གཞན་གྱི་དོན་ལ་ཉིན་མཚན་དུ་འབད་པ་དང་། ཐུན་མོང་གི་ཡོན་ཏན་བྱང་ཆུབ་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་། ཐུན་མོང་མ་ཡིན་པའི་སྟོབས་བཅུ་དང་། མི་འཇིགས་པ་བཞི་དང་མ་འདྲེས་པ་ལ་སོགས་པ་འགྲུབ་པར་བྱེད་དོ། །

[Block 35 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 36 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 37]
སློབ་དཔོན་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ན་ལ་བོད་ཀྱི་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་གསེར་སྲང་བཅུ་བཞིའི་སྦྲང༌[^30]བུ་མེ་ཏོག་དུ་ཕུལ་ནས་བོད་དུ་བྱོན་པའི༌[^31]ཞུ་བ་ཕུལ་བ་ལས་སྒོམ་སྦྱོང་བ་རྣམས་མཐར་ཕྱིན་པར་བྱ་བའི་དོན་དུ་བླ་མ་ཟླ་བ་བཅུ་དྲུག་ཏུ་ལམ་དུ་མ་ཆུད་དོ། །

[Block 38]
དེ་ནས་བོད་དུ་བྱོན༌[^32]ཁར་སློབ་མ་སེམས་སྦྱོང་བ་རྣམས་ཀྱིས་ཞལ་ཆེམས་གཞག་པར་ཞུས་པས་མདོའི་དོན་མན་ངག་ཏུ་བྱས་པ་འདི་ཞལ་ཆེམས་སུ་གནང་ངོ་། །

[Block 39 [HEADING]]
### འགྱུར་བྱང། ^a-2-0

[Block 40]
དེའི་དུས་སུ་རྒྱ་བརྩོན་སེང་གེས་བསྒྱུར་བར་ཞུས་པས་གནང་སྟེ་གཏན་ལ་ཕབ་པོ། །[^33]
--- END BLOCKS ---
