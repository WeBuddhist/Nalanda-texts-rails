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
## ༄༅། །སྤྱོད་པའི་གླུའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཙཱརྱ་གཱི་ཏི༌[^1]བྲྀཏྟི། བོད་སྐད་དུ། སྤྱོད་པའི་གླུའི་འགྲེལ་པ། འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [VERSE]]
རྣམ་པ་ཀུན་གྱི་མཆོག་ལྡན་པ། །
ཟུང་འཇུག་སྐུ་ལ་ཕྱག་འཚལ་ལོ། །
སྤྱོད་པ་གླུ་ཡི་དོན་དབྱེ་བ། །
གཞན་ལ་ཕན་པའི་བློ་ཡིས་བྲི། །

[Block 5]
འདིར་ཡང་དག་པའི་ལྟ་བ་རྣམ་པ་གཉིས་ཀྱི་དབང་དུ་བྱས་ནས། རྡོ་རྗེའི་གླུས་འོད་གསལ་བ་དང་། འགོག་པའི་དང་དོན་དམ་པའི་བདེན་པ་གཙོར་བསྟན་ནས། སྤྱོད་པའི་གླུས་བདག་བྱིན་གྱིས་བརླབ་པ་དང་། །ལམ་གྱི་བདེན་པ་དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་བསྟན་པའི་ཕྱིར། །གཟུགས་བརྙན་ཅི་འདྲ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་

[Block 6 [HEADING]]
## ཤེས་རབ་ཀྱི་མིག་གིས་བལྟ་བར་བྱ་བའི་ཡུལ། ^1-0

[Block 7]
འདིར་ཤེས་རབ་ཀྱི་མིག་གིས་བལྟ་བར་བྱ་བའི་ཡུལ་ནི་གཉིས་ཏེ། མེད་པ་དང་། ཡོད་པའི་རང་བཞིན་ནོ། །

[Block 8 [HEADING]]
### མེད་པ། ^1-1-0

[Block 9]
མེད་པ་ནི་མ་ཡིན་པ་ལ་དེར་སྣང་བ་སྟེ། དཔེར་ན་རབ་རིབ་ཅན་གྱི་ཤེས་པ་བཞིན་ནོ། །

[Block 10]
གཟུགས་བརྙན་ཅི་འདྲ་ཞེས་པ་ནི་དེ་ལ་གསུམ་སྟེ། མེ་ལོང་གཡའ་མེད་པ་དང་། བཞིན་ཉེ་བར་གནས་པ་དང་། ནམ་མཁའི་སྒྲིབ་གཡོགས་མེད་པ་ལ་གཟུགས་སྣང་ངོ་། །དེ་བཞིན་དུ་སེམས་དང་རླུང་གི་རྣམ་འཕྲུལ་ལས་མ་རིག་པས་ཁྱད་པར་དུ་བྱས་པ་ལ་སྲིད་པ་གསུམ་གྱི་འགྲོ་བ་གསལ་བར་སྣང་སྟེ། དེ་ཡང་སྣང་བ་ཙམ་ལས་དོན་དུ་གྲུབ་པ་གང་ཡང་མེད་དོ། །

[Block 11]
དེའི༌[^2]ཕྱིར། རང་གི་ངོ་བོ་བརྟགས་ན་རང་བཞིན་ཡོད་མ་ཡིན། །ཞེས་བྱ་བའོ། །ཇི་ལྟར་བརྟགས་པས་མེད་པར་ཤེས་ཤེ་ན། བདག་དང་ཁམས་གསུམ་པའི་རང་གི་ངོ་བོ་གཟུགས་བརྙན་ལྟར་སྣང་བ་ཙམ་དུ་ཤེས། མ་སྐྱེས་པར་ཤེས་པའོ། །

[Block 12]
དེ་ཀྭའི་ཞེས་བོས་ནས་གདམས་པའོ། །

[Block 13]
གཟུགས་བརྙན་ལ་འཁྲུལ་བར་མ་བྱེད། གཟུགས་བརྙན་གྱི་རང་བཞིན་མི་ཤེས་པར་མ་བྱེད་ཅེས་པའོ། །

[Block 14]
དེ་ལྟར་མདོར་བསྟན་ནས་དཔེ་དོན་གྱི་མཚན་ཉིད་རྒྱས་པར་བསྟན་པའི་ཕྱིར། དྲི་མེད་མཁའ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། [^3]ནམ་མཁའ་དྲི་མ་མེད་པ་དང་། ནོར་བུ་དང་། མེ་ལོང་དག་པ་དང་། བཞིན་གསུམ་འདུས་པ་ལས་གཟུགས་བརྙན་སྣང་བ་དེ་བཞིན་དུ་སེམས་དང་རླུང་དང་ལས་དང་མ་རིག་པ་ལས་བདག་དང་ཁམས་གསུམ་པའི་གཟུགས་བརྙན་སྣང་སྟེ། དེ་ལ་འཁྲུལ་ཏེ་རྟག་པ་དང་ཡང་དག་པར་ཤེས་པ་ནི་སེང་གེ་རང་གི་གྲིབ་མ་ལ་བརྒལ་བས་རྒྱ་མཚོར་ཤི་བ་དང་འདྲ་སྟེ་བླུན་པའོ། །

[Block 15]
ཡང་བརྡ་མི་ཤེས་པའི་བྱིས་པས་རང་གི་གཟུགས་བརྙན་ལ་འབྲད་པ་དང་འདྲ་སྟེ་བླུན་པའོ། །

[Block 16]
དེ་བཞིན་དུ་བདག་དང་ཁམས་གསུམ་པ་གཟུགས་བརྙན་ལྟར་སྣང་བ་ལ་བདག་དང་གཞན་དུ་ཅིའི་ཕྱིར་འཁྲུལ་ཏེ་འཁྲུལ་པར་མ་བྱེད་ཅེས་བྱ་བའོ། །

[Block 17]
དེ་ཡང་མདོ་ལས།

[Block 18 [VERSE]]
ཇི་ལྟར་མེ་ལོང་ངོས་ལ་ནི། །
སྣང་ཡང༌[^4]དེ་ན་ཡོད་མིན་ལྟར། །
དེ་བཞིན་དངོས་རྣམས་ངོ་བོ་ཉིད། །

[Block 19]
ཅེས་པ་དང་། ཡང་།

[Block 20 [VERSE]]
དོན་ཡོད་མ་ཡིན་སེམས་ཉིད་དེ། །
བག་ཆགས་ཀྱིས་ནི་དཀྲུགས༌[^5]པའི་ཡིད། །
དོན་དུ་སྣང་བ་བྱུང་བ་ཡིན། །

[Block 21]
ཞེས་གསུངས་པས་བདག་དང་ཁམས་གསུམ་པའི་དངོས་པོ་ཚུ་རོལ་མཐོང་བའི་ཤེས་པ་དང་། ཤེས་བྱ་མ་ལུས་པར་ནམ་མཁའི་མེ་ཏོག་ལྟར་ཤེས་པར་བྱའོ། །

[Block 22 [HEADING]]
### ཡོད་པའི་རང་བཞིན་མཐོང་བ། ^1-2-0

[Block 23]
ད་ནི་ཡོད་པའི་རང་བཞིན་མཐོང་བའི་དབང་དུ་བྱས་ནས། དཀྱིལ་འཁོར་འཁོར་ལོ་བསྒོམ་པ་བརྟན་པར་བྱ་བ་སྟེ། ཞེས་བྱ་བ་དེ་ལ་ལྔ་སྟེ་རྟེན་འབྲེལ་ལ་མཐུ་ཡོད་པ་དང་། དེ་ཡིན་པ་དང་། དེར་ཤེས་པ་དང་། དེར་བསྒོམ་པ་དང་། བྱིན་གྱི་རླབས༌[^6]འབྱུང་བའོ། །

[Block 24 [HEADING]]
#### རྟེན་འབྲེལ་ལ་མཐུ་ཡོད་པ། ^1-2-1-0

[Block 25]
དེ་ལྟར་ཡོད་པ་མ་ཡིན་པའི་དོན་བསལ་ནས་སེམས་རླུང་གཉིས་ཟག་མེད་ཀྱི་ཡོན་ཏན་གྱིས་ཁྱད་པར་དུ་བྱས་པའི་ཚེ། རྟེན་དང་བརྟེན་པའི་ལྷའི་འཁོར་ལོར་སྣང་བ་སྟེ་ཉེར་ལེན་གྱི་རྒྱུ་སེམས་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་རླུང་ཟག་མེད་ཀྱི་ཡོན་ཏན་གསུམ་འདུས་པ་ལས་ཡིད་ཀྱི་ལུས་སྒྱུ་མ་ལྟ་བུ་ལ་སོགས་པར་སྣང་ངོ་། །

[Block 26 [HEADING]]
#### དེ་ཡིན་པ། ^1-2-2-0

[Block 27]
དེ་ཡང་རང་བཞིན་གྱིས་ཟག་པ་མེད་པའི་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཡིན་པ་ཤེས་པ་མེད་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 28 [HEADING]]
#### དེར་ཤེས་པ། ^1-2-3-0

[Block 29]
དེ་ཡང་ཤེས་བྱེད་ཡང་དག་པའི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ནས་བདག་བྱིན་གྱིས་བརླབ་པའི་རང་བཞིན་དུ་དཔེ་གསུམ་དང་བཅུ་གཉིས་ཀྱི་སྒོ་ནས་མཚོན་ཅིང་ཤེས་པ་དང་།

[Block 30 [HEADING]]
#### དེར་བསྒོམ་པ། ^1-2-4-0

[Block 31]
དེ་ཡང་དབང་པོ་ལྔས་དབང་བྱས་ནས་བསྒོམ་པ་དང་།

[Block 32 [HEADING]]
#### བྱིན་གྱི་རླབས་འབྱུང་བ། ^1-2-5-0

[Block 33]
དེ་ལས་བྱིན་གྱི་རླབས༌[^7]ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟར་སྣང་བ་ངེས་པའི་ཤེས་པ་སྐྱེའོ། །

[Block 34]
གཞན་ལྷས་སྐྱོང་བ་ལ་སོགས་པ་འཕགས་པའི་ལྷས་བཤད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 35]
དེ་ཉིད་ཤེས་པའི་རྣལ་འབྱོར་པ་ཡིས་དེར་མི་གནས། །ཞེས་བྱ་བ་ནི་སྒྱུ་མར་ཤེས་ཀྱང་སྒྱུ་མས་བྱས་པའི་བུད་མེད་ལ་ཆགས་པ་སྐྱེ་བ་དང་འདྲ་བར་ཞེན་པ་ཡོད་པས་དེ་འོད་གསལ་གྱིས༌[^8]སྦྱངས་པའོ། །

[Block 36]
མཚོན་པར་བྱ་བ་མཆོག་ཏུ་བདེ་ཆེན་ཞེས་པ་སྟེ། །ཞེས་པའི་ཚིག་གཉིས་པོ་གོ་སླའོ། །

[Block 37]
ཁྱེད་ཀྱིས་བརྟགས་ཤིང་བསྐྱེད་པའི་ཚུལ་ནི་གང་ཡིན་པ། །ཞེས་བྱ་བ་ནི་བདེན་པ་གཉིས་ཀྱི་མཚན་ཉིད་དང་མི་ལྡན་པའི་བརྟགས་པའི་རྣལ་འབྱོར་དགག་པ་སྟེ་གོ་སླའོ། །

[Block 38 [VERSE]]
ཇི་སྲིད་དེ་ནི་རང་བཞིན་ཡོངས་སུ་མི་ཤེས་པས། །
དེ་སྲིད་བྱང་ཆུབ་བླ་ན་མེད་པ་ཇི་ལྟར་འགྲུབ། །
ཅེས་བྱ་བ་ནི་འོད་གསལ་དང་ཟུང་འཇུག་གོ། །
རྣམ་རྟོག་སྤྲོས་པ་མ་ལུས་དངོས་པོ་མེད་པ་སྟེ། །

[Block 39]
ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་སེམས་བརྒྱ་དྲུག་ཅུའོ། །

[Block 40]
དེ་དག་མཆོག་ཏུ་བདེ་བ་ཆེན་པོ་འོད་གསལ་གྱི་རང་བཞིན་གྱིས་སྦྱངས་པ་ཡིན་ཞེས་བྱའོ། །
--- END BLOCKS ---
