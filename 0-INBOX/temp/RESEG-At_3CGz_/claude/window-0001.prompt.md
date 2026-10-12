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
[Block 36 [VERSE]]
བླ་མ་རྣམས་ཀྱིས་བསྟན་པ་ཡིས། །
ཡང་དག་ཐབས་ནི་བསྟན་པར་བྱ། །

[Block 37]
ཞེས་བྱ་བ་ནི་འདི་ཡིན་ནོ། །

[Block 38]
དེ་ལ་བླ་མ་རྣམས་ནི་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང་པོ་དང་། རྗེ་བཙུན་སུ་ཝརྞྞ་དྭཱི་པ་ལ་སོགས་པའོ། །

[Block 39]
ཡང་དག་ཐབས་ཞེས་བྱ་བ་ནི། གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་རྣམ་པ་གཉིས་དང་། མངོན་པར་ཤེས་པ་བསྐྱེད་ནས་གཞན་དོན་ཁྱད་པར་ཅན་བྱ་བའི་ཐབས་དང་། ཐབས་དང་ཤེས་རབ་ཟུང་དུ་འབྲེལ་བའི་ཚོགས་གཉིས་བསག་པའི༌[^16]ཐབས་དང་། བདག་དང་གཞན་དོན་མྱུར་དུ་རྫོགས་པར་འགྱུར་བའི་ཐེག་པ་ཆེན་པོའི་ཆེན་པོ་གསང་སྔགས་ཀྱི་ལུགས་ཀྱི༌[^17]ཐུན་མོང་མ་ཡིན་པའི་ཚོགས་གཉིས་བསགས་པའི་ཐབས་རྣམས་སོ། །

[Block 40]
དེ་ལྟ་བུའི་ཐབས་དེ་དག་རྒྱས་པར་བཤད་པར་འདོད་ནས། རྫོགས་སངས་བྲིས་སྐུ་ལ་སོགས་དང་། །ཞེས་པ་ནས། དེ་ཉིད་རིག་ལ་ཉེས་པ་མེད་པའི་བར་རོ། །

[Block 41]
གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་ནི་ཐར་པའི་གྲོང་ཁྱེར་ཆེན་པོར་འཇུག་པའི་སྒོ་ལྟ་བུར་གྱུར་པ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་གཞི་ལྟ་བུར་གྱུར་པས་དེ་བསྟན་པར་འདོད་ནས།

[Block 42 [VERSE]]
རྫོགས་སངས་བྲིས་སྐུ་ལ་སོགས་དང་། །
མཆོད་རྟེན་དམ་ཆོས་མངོན་ཕྱོགས་ནས། །

[Block 43]
ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་རྐང་བཅུ་གཉིས་ཀྱིས་བསྟན་ཏེ། མངོན་ཕྱོགས་ནས་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་སྐུ་མངོན་དུ་ཕྱོགས་པར་བྱས་ཤིང་མཐོང་བ་ལས་བྱང་ཆུབ་ཀྱི་སེམས་སྐྱེའོ༌[^18]ཞེས་ཐེག་པ་ཆེན་པོའི་མདོ་རྒྱལ་པོ་ལ་གདམས་པའི་སྔོན་གྱི་རྟོགས་པ་བརྗོད་པ་ལས་ཀྱང་མཐོང་བ་དང་། དགེ་བའི་བཤེས་གཉེན་དག་ཀྱང་གསུང་ངོ་། །ཆོ་ག་རྒྱས་པ་ནི་འོག་ནས་སྟོན་པར་འགྱུར་རོ། །

[Block 44]
འདི་ལྟར་བྱུག་རིས་ཀྱི་དཀྱིལ་འཁོར་ཉི་ཤུ་རྩ་བདུན་དུ་དཀོན་མཆོག་གསུམ་གྱི་གཟུགས་བརྙན་སོ་སོར་བཞུགས་སུ་གསོལ་ལ། ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་ན་བཞུགས་པའི་རྣམ་པར་དག་པའི་དཀོན་མཆོག་གསུམ་ཡང་གནས་སོ་སོ་དེ་དག་ཏུ་སྤྱན་དྲང་བའམ། ཡང་ན་ཞིང་ཁམས་དེ་དག་ཉིད་དུ་བདག་ཉིད་འདུག་པར་མོས་ཏེ་ལུས་ཀྱི་རྣམ་པར་འཕྲུལ་པའི་བཀོད་པས་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རེ་རེའི་མདུན་དུ་བདག་ཉིད་འདུག་པར་བསམ༌[^19]ལ་པུག་པུག་པོར་རམ་སོར་མོ་བསྣོལ་ལ་སྤྱི་བོར་ཐལ་མོ་སྦྱར་ནས་མཆོད་པའི་བྱ་བ་རྫོགས་པ་དང་། ཕུང་པོ་གསུམ་པ་བྱས་ལ་བླ་མ་ལ་ཡོན་ཕུལ་ཏེ་སྐྱབས་སུ་འགྲོ་བ་བྱའོ། །

[Block 45]
དེ་ཡང་དཀོན་མཆོག་གསུམ་ནི་འདི་ལྟ་བུ་ཡིན་ཏེ། དེ་ཁོ་ན་ཉིད་ཀྱི་དཀོན་མཆོག་གསུམ་དང་། མདུན་དུ་བཞུགས་པའི་དཀོན་མཆོག་གསུམ་སྟེ། དེ་ལྟ་བུ་ཤེས་པ་སྔོན་དུ༌[^20]འགྲོ་བར་བྱའོ། །

[Block 46]
མེ་ཏོག་བདུག་སྤོས་དངོས་པོ་དག །ཅེས་པ་ནི་ཟང་ཟིང་གི་མཆོད་པ་མཚོན་པའོ། །

[Block 47]
མཆོད་པ་རྣམ་པ་བདུན་དག་ཀྱང་། །ཞེས་པ་ནི་སྒྲུབ་པའི་མཆོད་པ་མཚོན་པའོ། །

[Block 48]
འདིར་བྱང་ཆུབ་སེམས་དཔའ་ཚོགས་ཀྱི་ལམ་པ་སློབ་དཔོན་དུ་གྱུར་པ་དེས་བསོད་ནམས་ཀྱི་ཚོགས་བསག་པའི༌[^21]ཕྱིར། མཆོད་པ་ལ་མཁས་པར་བྱ་བ་ཡིན་ཏེ། དེ་སྨྲ་བ༌[^22]འདོད་ནས།

[Block 49 [VERSE]]
ཀུན་བཟང་སྤྱོད་ལས་གསུངས་པ་ཡི།[^23] །
མཆོད་པ་རྣམ་པ་བདུན་དག་ཀྱང་། །

[Block 50]
ཞེས་བྱ་བ་འདི་ཡིན་ཏེ། ཀུན་བཟང་སྤྱོད༌[^24]ཅེས་བྱ་བ་ནི་འཕགས་པ་སྡོང་པོ་བཀོད་པ་ལས་འབྱུང་བའི་འཕགས་པ་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་རྒྱལ་པོ་ཡིན་ཏེ། འདི་ནི་ཕྱོགས་བཅུ་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོས་ཆེན་པོ་ལ་བཞུགས་པ་ཀུན་དུ་བཟང་པོའི་སྤྱོད་པ་དང་། སྨོན་ལམ་གྱི་རྒྱ་མཚོ་མི་ཟད་པའི༌[^25]བརྙེས་པ་རྣམས་ཀྱི༌[^26]ཀུན་དུ་བཟང་པོའི་སྤྱོད་པ་དང་། ཀུན་དུ་བཟང་པོའི་སྨོན་ལམ་ཡིན་པས་འདི་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པ་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྡེ་སྣོད༌[^27]ཀྱི་མར་མེ་ལྟ་བུ་ཡིན་ནོ་ཞེས་བླ་མ་དམ་པ་མཁས་པ་ཆེན་པོ་དག་གསུངས་པ༌[^28]ཡིན་ནོ། །

[Block 51]
གསུངས་པའི་མཆོད་པ་རྣམ་པ་བདུན། །ཞེས་བྱ་བ་ནི་བླ་མ་ཁ་ཅིག་གི་ཞལ་ནས་འཕགས་པ་བཟང་པོ༌[^29]སྤྱོད་པའི་སྨོན་ལམ་ལས་མཆོད་པ་བདུན་གསུངས་ཏེ། ཇི་སྙེད་སུ་དག་ཕྱོགས་བཅུའི་ཞེས་པ་ཤློ་ཀས་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱིས༌[^30]ཕྱག་འཚལ་བའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 52]
བཟང་པོར་སྤྱོད་ལ་དད་པའི་ཞེས་པ་ལ་སོགས་པའི་ཤློ་ཀས་ནི་ལུས་དབུལ་བའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 53]
རྡུལ་གཅིག་སྟེང་ན་ཞེས་པའི་ཤློ་ཀས་ནི་དེ་དག་ཡུལ་དུ་བྱས་ཏེ་དང་བའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 54]
དེ་དག་བསྔགས་པ་མི་ཟད་རྒྱ་མཚོ་རྣམས། །ཞེས་པ་ལ་སོགས་པས་ནི་བསྟོད་པའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 55]
མེ་ཏོག་དམ་པ་ཞེས་པ་ལ་སོགས་པས་ནི་བླ་ན་ཡོད་པའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 56]
མཆོད་པ་གང་རྣམས་བླ་མེད་རྒྱ་ཆེ་བ། །ཞེས་པས་ནི་བླ་ན་མེད་པའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 57]
འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་ཅེས་པས་ནི་ཕུང་པོ་གསུམ་པའི་མཆོད་པ་བསྟན་ཏོ། །

[Block 58]
གཞུང་གཞན་གྱིས་མི༌[^31]མཆོད་པ་དེ་དག་གི༌[^32]བསྔོ་བ་བསྟན་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ།[^33] །

[Block 59]
ཡང་བླ་མ་དམ་པ་ཁ་ཅིག་གི་ཞལ་ནས། འཕགས་པ་བཟང་པོ༌[^34]སྤྱོད་པའི་སྨོན་ལམ་ལས་མཆོད་པ་བདུན་གསུངས་ཏེ། འདི་ལྟར་མེ་ཏོག་དམ་པ་དང་། ཕྲེང་བ་དམ་པ་དང་། སིལ་སྙན་དམ་པ་དང་། བྱུག་པ་དམ་པ་དང་། མར་མེ་དམ་པ་དང་། བདུག་སྤོས་དམ་པ་དང་། ན་བཟའ་དམ་པ་རྣམས་སོ། །

[Block 60]
དྲི་མཆོག་དམ་པ་དང་། ཕྱེ་མའི་ཕུར་མ་གཉིས་ནི་བྱུག་པ་དམ་པ་དང་། བདུག་པ་གཉིས་ཀྱི་ནང་དུ་འདུས་པ་ཉིད་ཡིན་ལ་བཀོད་པའི་ཁྱད་པར་ཞེས་པ་ནི་སྔ་མ་དེ་དག་རེ་རེ་ཞིང་ཡང་བརྗོད་དུ་མེད་པའི་བཀོད་པ་བྱའོ་ཞེས་གསུང་ངོ་།[^35] །བླ་མ་མཁས་པ་གཞན་དག་ནི་འཕགས་པ་བཟང་པོ༌[^36]སྤྱོད་པའི་སྨོན་ལམ་ལས་མཆོད་པ་བདུན་དུ་གསུངས་པ་ནི་འདི་ལྟར་ཡན་ལག་བདུན་པར་འདུས་ཏེ། སྒྲུབ་པའི་མཆོད་པ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། དེ་ཉིད་ལས་བདུན་པོ་དེ་དག་རྫོགས་པའི་རྗེས་ལ་འདི་སྐད་དུ།

[Block 61]
འདས་པའི་སངས་རྒྱས་རྣམས་དང་ད་ལྟར་གྱི། །ཕྱོགས་བཅུ་དག་ན་གང་བཞུགས་མཆོད་པར་གྱུར། །ཞེས་མཆོད་པ་ཉིད་ཡིན་པར་གསལ་བར་གསུངས་སོ་ཞེས་གསུང་ངོ་། །དེ་དག་ནི་གར་ཡང་འགལ་བ་མེད་པ་དེ་རང་ཉིད་གང་ལ་མོས་པ་དེ་གཟུང་བར་བྱའོ། །

[Block 62 [HEADING]]
## མཆོད་པ། ^1-0

[Block 63]
འདི་ལྟར་མཆོད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཟང་ཟིང་གི་མཆོད་པ་དང་། སྒྲུབ་པའི་མཆོད་པའོ། །

[Block 64 [HEADING]]
### ཟང་ཟིང་གི་མཆོད་པ། ^1-1-0

[Block 65]
ཟང་ཟིང་གི༌[^37]མཆོད་པ་ནི་གཉིས་ཏེ། མངོན་སུམ་པ་ཉིད་དང་། ཡིད་ཀྱིས་བྱས་པའོ། །

[Block 66 [HEADING]]
#### མངོན་སུམ་པ། ^1-1-1-0

[Block 67 [HEADING]]
##### མེ་ཏོག་ལ་སོགས་པ་བདག་ཉིད་ལ་ཡོད་པ། ^1-1-1-1-0

[Block 68]
མངོན་སུམ་པ་ནི་གཉིས་ཏེ། མེ་ཏོག་ལ་སོགས་པ་དང་། བདུག་པ་ལ་སོགས་པ་དང་། རོལ་མོ་ལ་སོགས་པ་དང་། རྒྱལ་སྲིད་དང་། ནོར་བུ་རིན་པོ་ཆེ་ལ་སོགས་པ་བདག་ཉིད་ལ་ཡོད་པའོ། །

[Block 69 [HEADING]]
##### གཉིས་པ་སེམས་རྟེན་དང་བཅས་པ། ^1-1-1-2-0

[Block 70]
གཉིས་པ་ནི་སེམས་རྟེན་དང་བཅས་པ་དང་། བུ་དང་བུ་མོ་དང་། ཆུང་མ་དང་བྲན་ལ་སོགས་པའོ། །

[Block 71 [HEADING]]
#### ཡིད་ཀྱིས་བྱས་པ། ^1-1-2-0

[Block 72 [HEADING]]
##### དང་པོ་བདག་པོ་མེད་ཅིང་གཞན་གྱིས་ཡོངས་སུ་མ་བཟུང་བའི་རྫས། ^1-1-2-1-0

[Block 73]
ཡིད་ཀྱིས༌[^38]བྱས་པ་ལ་གཉིས་ཏེ། དང་པོ་ནི་ཕྱོགས་བཅུའི་འཇིག་རྟེན་ཁམས་ཀྱི༌[^39]བདག་པོ་མེད་ཅིང་། གཞན་གྱིས༌[^40]ཡོངས་སུ་མ་བཟུང་བའི་རྫས་ཕུལ་དུ་བྱུང་བ་མ་ལུས་པ་སྟེ། ཇི་ལྟར་འཕགས་པ་དཀོན་མཆོག་སྤྲིན་དང་། འཕགས་པ་དགོངས་པ་རྒྱུད་ཀྱི་ཕྲེང་བ་དང་། ཏིང་ངེ་འཛིན་གྱི་འཁོར་ལོའི་མཆོད་པའི་ཕྱག་རྒྱའི་མདོ་དང་། དཀོན་མཆོག་ཏ་ལ་ལའི་མདོ་དང་། སྤྱོད་པ་ལ་འཇུག་པ་ལས་གསུངས་པ་ལྟ་བུའོ། །

[Block 74 [HEADING]]
##### གཉིས་པ་ཡིད་ཀྱི་རྣམ་པར་འཕྲུལ་པ་ལས་བྱུང་བའི་བཀོད་པ། ^1-1-2-2-0

[Block 75]
གཉིས་པ་ནི་ཡིད་ཀྱི༌[^41]རྣམ་པར་འཕྲུལ་པ་ལས་བྱུང་བའི་བཀོད་པ་ནམ་མཁའི་མཛོད་ལས་བྱུང་བ་སྟེ། འདི་ལྟར་འཁོར་ལོས༌[^42]སྒྱུར་བའི་རྒྱལ་སྲིད་རིན་པོ་ཆེ་བདུན་དང་། ནོར་བུ་རིན་པོ་ཆེ་གསེར་དང་། དངུལ་དང་། དུང་དང་། མན་ཤེལ་དང་། ཆུ་ཤེལ་དང་། སྤུག་དང་། རྡོའི་སྙིང་པོ་དང་། མུ་ཏིག་དང་། མུ་ཏིག་དམར་པོ་དང་། མན་ཤེལ་དང་། པདྨ་རཱ་ག་དང་། ཨསྨ་གརྦྷ་དང་། མུ་ས་ལ་གལ༌[^43]པ་དང་། དུན་ལས་དང་། ཨིནྡྲ་ནཱི་ལ་དང་། མར་ཀ་ཏ་དང་། བཻ་ཌཱུརྱ་དང་། ཤཾ་ཀ་ཤི་ལ་དང་། བྱི་རུ༌[^44]དང་། ཀེ་ཀེ་རུ་དང་། ཀེ་ཀེ་རུ་ཆེན་པོ་ལ་སོགས་པའི་ནོར་བུ་དེ་དག་གི་ཆར་པ་འབབ་པ་དང་། དེ་དག་གི་གདུགས་དང་། རྒྱལ་མཚན་དང་། བ་དན་དང་། གཞལ་ཡས་ཁང་དང་། དྲ་བའི་ཚོགས་བརྗོད་དུ་མེད་པ་དག་གཞན་ཡང་དཀོན་མཆོག་ཏ་ལ་ལའི་གཟུངས་ལས་འབྱུང་བ་ལྟ་བུ་སྟེ།
--- END BLOCKS ---
