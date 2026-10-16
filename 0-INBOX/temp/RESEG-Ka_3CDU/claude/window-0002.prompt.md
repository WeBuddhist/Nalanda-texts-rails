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
[Block 71]
སློབ་མ་རྣམས་ལ་འདི་དག་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན། འདི་དག་ནི་སྤང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་སྟོན་པའི་ཆོས་ལ་བསྟན་པ་ཞེས་བྱ་སྟེ། འདུལ་བའི་སྡེ་སྣོད་དང་། མདོ་སྡེའི་སྡེ་སྣོད་དང་། མངོན་པའི་ཆོས་ཀྱི་སྡེ་སྣོད་དོ། །

[Block 72]
དེ་ལས་རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིས་བསླབ་ཚིག༌[^30]རྣམ་པ་གསུམ་སྟེ། ལྷག་པ་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་དང་། སེམས་ཀྱི་བསླབ་པ་དང་། ཤེས་རབ་ཀྱི་བསླབ་པའོ། །

[Block 73]
དེ་འདུལ་བའི་སྡེ་སྣོད་ཀྱི་ནང་ནས་ནི་ལྷག་པ་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་འབྱུང་ངོ་། །མདོ་སྡེའི་སྡེ་སྣོད་ལས་ནི་ལྷག་པ་སེམས་ཀྱི་བསླབ་པ་འབྱུང་ངོ་། །མངོན་པའི་ཆོས་ཀྱི་སྡེ་སྣོད་ནས་ནི་ལྷག་པ་ཤེས་རབ་ཀྱི་བསླབ་པ་འབྱུང་སྟེ། དེ་ལྟར༌[^31]སྡེ་སྣོད་གསུམ་ལ་བསྟན་པ་ཞེས་བྱའོ། །

[Block 74 [HEADING]]
### གང་ཟག་ཕུན་སུམ་ཚོགས་པ། ^2-2-0

[Block 75]
དད་པས་རབ་ཏུ་བྱུང་ནས་ནི། །ཞེས་བྱ་བས་གང་ཟག་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། གང་ཟག་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་གཉིས་ཀྱིས་ཕུན་སུམ་ཚོགས་སོ། །

[Block 76]
གང་ཞེ་ན། བསམ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 77 [HEADING]]
#### བསམ་པ་ཕུན་སུམ་ཚོགས་པ། ^2-2-1-0

[Block 78]
དད་པ་ཞེས་བྱ་བས་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ལས་དང་འབྲས་བུ་ལ་སོགས་པ་ནི་ཡོད་པར་ཡིད་ཆེས་པ་དང་། དཀོན་མཆོག་གསུམ་ལ་ནི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པར་སེམས་པ་དང་། འཕགས་པའི་ལམ་ནི་བསྒྲུབ་པར་འདོད་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འདོད་པའི་སེམས་ལ་ནི་དང་བ་ཞེས་བྱའོ། །

[Block 79]
དད་པས་ཞེས་བྱ་བ་ནི། དད་པའི་སེམས་ཀྱིས་རྒྱུར༌[^32]བྱས་ནས། །ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 80 [HEADING]]
#### སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ། ^2-2-2-0

[Block 81]
རབ་ཏུ་བྱུང་ནས་ནི་ཞེས་བྱ་བས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དཀོན་མཆོག་གསུམ་ལ་སྐྱབས་སུ་སོང་ཞིང་བསླབ་ཚིག༌[^33]བཅུ་མནོས་པ་ལས་རབ་ཏུ་བྱུང་བ་ཞེས་བྱའོ། །

[Block 82]
ཡང་ན། དད་པས་རབ་ཏུ་བྱུང་ནས་ནི། །ཞེས་བྱ་བའི་ཚིག་འདིས་བཅོམ་ལྡན་འདས་ཀྱིས་འདུལ་བ་ལས་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ནས་གོས་ངུར་སྨྲིག་གོས་ཏེ་དད་པས་ཡང་དག་པ་ཁོ་ནར་ཁྱིམ་ནས་ཁྱིམ་མེད་པར་རབ་ཏུ་འབྱུང་ངོ་ཞེས་རབ་ཏུ་བྱུང་བའི་མཚན་ཉིད་གསུངས་པའི་དོན་བསྟན་པ་ཡིན་ཏེ། ཚིག་འདིས་ནི་རབ་ཏུ་བྱུང་བ་རྣམས༌[^34]ཀྱི་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་བཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 83]
རྣམ་པ་བཞི་གང་ཞེ་ན།

[Block 84 [VERSE]]
ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དང་། །
ལས་ཕུན་སུམ་ཚོགས་པ་དང་།
གནས་ཕུན་སུམ་ཚོགས་པ་དང་། །
[^35]བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 85]
དེ་ལ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ནས་གོས་ངུར་སྨྲིག་བགོས་ཏེ་ཞེས་བྱ་བས་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ཚུལ་དེ་ལས་ཉོན་མོངས་པ་སྤོང་བ་དང་མཐུན་པའི་ཚུལ་ཡིན་པས་ཁྱིམ་ན་གནས་པའི་ཚུལ་ལས་འཕགས་པ་ཡིན་ནོ། །

[Block 86]
དད་པས་ཡང་དག་པ་ཁོ་ནར་ཞེས་བྱ་བས་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བུ་ལོན་མ་འཁོར་བ༌[^36]དང་རྒྱལ་པོ་ལ་སོགས་པའི་འཇིགས་པས་རབ་ཏུ་བྱུང་བ་མ་ཡིན་གྱི་དད་པའི་སེམས་ཀྱིས་རབ་ཏུ་བྱུང་བ་ཡིན་ནོ། །

[Block 87]
རབ་ཏུ་བྱུང་ཞེས་བྱ་བས་ནི་ལས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བྱ་བ་མཆོག་ཏུ་གྱུར་པ་ལ་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 88]
ཁྱིམ་ནས་ཁྱིམ་མེད་པར་རབ་ཏུ་བྱུང་ཞེས་བྱ་བས་ནི་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བུ་སྨད་དང་ཉེ་དུ་ལ་སོགས་པའི་འཇིགས་པ་མི་བཟད་པའི་གནས་སྤངས་ནས་ཁྱིམ་མེད་པར་ཤིང་དྲུང་དང་བྲག་ཕུག་ན་གནས་པས་ན། གནས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 89]
རབ་ཏུ་བྱུང་ནས་ནི་ཞེས་བྱ་བས་ནི་རབ་ཏུ་བྱུང་བའི་འོག་ཏུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 90 [HEADING]]
### སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ། ^2-3-0

[Block 91]
བརྟུལ་ཞུགས་བསྟན་པས༌[^37]རབ་བསྒྲིམས་ཏེ། །ཞེས་བྱ་བས་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། བརྟུལ་ཞུགས་ཞེས་བྱ་བས་ནི་རང་བཞིན་གྱི༌[^38]ཁ་ན་མ་ཐོ་བ་དང་། བཅས་པའི་ཁ་ན་མ་ཐོ་བའི་བསླབ་པ་ལ་བྱའོ། །

[Block 92]
དེ་ལ་རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བའི་བསླབ་ཚིགས༌[^39]ནི་ཕས་ཕམ་པ་བཞིའོ། །

[Block 93]
བཅས་པའི་ཁ་ན་མ་ཐོ་བའི་བསླབ་ཚིག༌[^40]ནི་ཆང་མི་བཏུང་བ་ལ་སོགས་པ་རྣམ་པ་དྲུག་གོ། །

[Block 94]
བརྟན་པས་རབ་བསྒྲིམས༌[^41]ཏེ་ཞེས་བྱ་བས་ནི་ལུས་ངག་ཡིད་གསུམ་གྱིས་རབ་ཏུ་བསྒྲིམས་ལ་ཕས་ཕམ་པ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་བསྟན་པ༌[^42]སྟེ། ཉེས་པ་ཕྲན་ཚེགས༌[^43]ཀྱང་མི་འབྱུང་བར་བསྲུང་བའོ། །

[Block 95]
དེ་ཡང་ཤིང་ཆེན་པོ་བསྲུང་ན་དེ་ལ་བསྐོར་བའི་ར་བ་དང་ཤིང་ཐགས་རྣམས་ཅི་ནས་ཀྱང་མི་གཞིག༌[^44]པར་བྱའོ། །

[Block 96]
དེ་དང་འདྲ་བར་ཕས་ཕམ་པ་མི་འབྱུང་བར་བྱ་ན་ར་བ་དང་ཤིང་ཐགས་ལྟ་བུའི་བསླབ་པ་ཕྲན་ཚེགས་རྣམས་མ་ཞིག་པར་བསྲུངས་ན་ཚུལ་ཁྲིམས་བརྟན་པར་བསྲུང་བ་ཡིན་ནོ། །

[Block 97 [HEADING]]
### ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ། ^2-4-0

[Block 98]
བདག་གི་ལུས་བཞིན་བསླབ་པ་བསྲུང་། །ཞེས་བྱ་བས་ཇི་ལྟར་བསྒྲུབ་པར༌[^45]བསྟན་ཏེ། དཔེར་ན་བདག་གི་ལུས་འདི་ལ་དུག་དང་ཚེར་མ་དང་ངམ་གྲོག༌[^46]ལ་སོགས་པས་འཆི་བར་མི་འགྱུར་བར་བསྲུང་བ་དང་། བཟའ་བ་དང་བགོ་བ་དང་སྨན་ལ་སོགས་པས་ཅི་ནས་ཀྱང་མི་བརྙས་པར་བྱ་བའི་ཚུལ་དུ་བསྲུང་བ་དང་འདྲ་བར་ཚུལ་ཁྲིམས་ཀྱང་ཅི་ནས་ཀྱང་མི་ཞིག་པར་བསྲུང་བ་དང་། རྣམ་པར་དག་པའི་ཚུལ་དུ་བསྲུང་བའོ། །

[Block 99]
བསླབ་པ་ཉམས་སུ་བླང་བའི་བཤད་པ་རྫོགས་སོ།། །།

[Block 100 [HEADING]]
## སྔ་དྲོའི་དུས་ན་ལས་གང་བྱ་བ། ^3-0

[Block 101]
སྔ་དྲོའི་དུས་ན་ལས་གང་བྱ་བ་བསྟན་པ་ལ་རྣམ་པ་བརྒྱད་བྱ་བར་བསྟན་ཏེ། ཁ་ཏོན་བྱ་བ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་འཚལ་བ་དང་། མཁན་པོ་དང་སློབ་དཔོན་ལ་སྙུན༌[^47]གསོལ་ནས་ལས་སུ་བྱ་བ་ཞུ་བ་དང་། ཆུ་བརྟག་པ་དང་། མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བྱ་བ་བསྒྲུབ་པ་དང་། ཞུ་བ་དང་། ཟས་བཟའ་བ་དང་།

[Block 102 [HEADING]]
### ཁ་ཏོན་བྱ་བ། ^3-1-0

[Block 103 [VERSE]]
བསོད་ནམས་བསྔོ་བ་དང་བརྒྱད་བྱའོ། །
ནམ་གྱི་ཆ་སྨད་མལ་ནས་ལངས། །
ནམ་ལངས་བར་དུ་ཁ་ཏོན་བྱ། །

[Block 104]
ཞེས་བྱ་བས་ཁ་ཏོན་བྱ་བ་བསྟན་ཏོ། །

[Block 105]
དེ་ནམ་གྱི་ཆ་སྨད་ནི་མཚན་གཅིག་ལ་ཐུན་ལྔར་བགོས་པ་ལས་ཐོ་རངས་ལ་བྱ་སྟེ། ཐོ་རངས་མལ་ནས་ལངས་ནས་ནི་ཙོག་ཙོག་པོར་འདུག་ལ་ལྷ་མ་སྲིན་ལ་ཆོས་ཀྱི་སྦྱིན་པ་བྱའོ་སྙམ་དུ་བསམས་ནས་ལྷ་མ་སྲིན་རྣམས་ལ་ཚིགས་སུ་བཅད་པ་སྟེར་བ་ལ་བོས་ཏེ་ནམ་ལངས་ཀྱི་བར་དུ་ཁ་ཏོན་ཅི་ནུས་སུ་བྱའོ། །

[Block 106]
ཁ་ཏོན་བྱས་པའི་བསོད་ནམས་སེམས་ཅན་ཀུན་གྱི་དོན་དུ་བསྔོ་བའོ།། །།

[Block 107 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་འཚལ་བ། ^3-2-0

[Block 108 [VERSE]]
གདོང་དང་སོ་ཡི་དྲི་བཀྲུས་ནས། །
རྫོགས་སངས་རྒྱས་ལ་གུས་ཕྱག་བྱ། །

[Block 109]
ཞེས་བྱ་བས་དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ་བསྟན་ཏེ། ལངས་ནས་ཆུ་དང་སོ་ཤིང་ལ་སོགས་པས་སོ་དང་གདོང་གི་དྲི་མ་བཀྲུས་ནས་རྫོགས་སངས་རྒྱས་ཏེ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ལ་གུས་པས་ཕྱག་བྱའོ། །

[Block 110]
དེ་ལ་ཆོས་ཐམས་ཅད་ཐུགས་སུ་ཆུད་ཅིང་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་མ་ལུས་པར་བརྙེས་པས༌[^48]ན་རྫོགས་པ་ཞེས་བྱའོ། །
--- END BLOCKS ---
