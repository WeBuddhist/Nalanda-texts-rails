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
[Block 106]
རྗེས་སུ་ཡི་རང་བའི་མཆོད་པ་ཡང་འཕགས་པ་ཟླ་བ་སྒྲོན་མའི་མདོ་ལས་འབྱུང་བ་བཞིན་ཏེ་མཆོད་པ་ཉིད་ཡིན་ནོ། །

[Block 107 [HEADING]]
##### བསྐུལ་བ། ^1-2-1-5-0

[Block 108]
བསྐུལ་བ་དང་།

[Block 109 [HEADING]]
##### གསོལ་བ་གདབ་པའི་མཆོད་པ། ^1-2-1-6-0

[Block 110]
གསོལ་བ་གདབ་པའི་མཆོད་པ་དང་།

[Block 111 [HEADING]]
##### ཡོངས་སུ་བསྔོ་བའི་མཆོད་པ། ^1-2-1-7-0

[Block 112]
ཡོངས་སུ་བསྔོ་བའི་མཆོད་པར་འགྱུར་བའི་ཚུལ་ཡང་མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 113 [HEADING]]
#### བླ་ན་མེད་པའི་མཆོད་པ། ^1-2-2-0

[Block 114]
བླ་ན་མེད་པའི་མཆོད་པ་ལ་གཉིས་ཏེ། དམིགས་པ་དང་བཅས་པ་དང་དམིགས་པ་མེད་པའོ། །

[Block 115 [HEADING]]
##### དམིགས་པ་དང་བཅས་པ། ^1-2-2-1-0

[Block 116]
དེ་ལ་དམིགས་པ་དང་བཅས་པ་ནི་འཕགས་པ་བློ་གྲོས་རྒྱ་མཚོའི་མདོ་ལས།

[Block 117]
བློ་གྲོས་རྒྱ་མཚོ་གསུམ་པོ་འདི་དག་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་དང་རིམ་གྲོ་བྱེད་པ་བླ་ན་མེད་པ་སྟེ། གསུམ་གང་ཞེ་ན། བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་འཛིན་པ་དང་། སེམས་ཅན་རྣམས་ལ་སྙིང་རྗེ་ཆེན་པོ་བསྐྱེད་པའོ་ཞེས་གསུངས་སོ། །

[Block 118]
དེ་བཞིན་དུ་འཕགས་པ་མཐར་གྱིས༌[^54]ཡང་དག་འཕགས་པའི་མདོ་ལས།

[Block 119]
བཟང་པོ་ཕན་ཡོན་བཞི་པོ་འདི་དག་མཐོང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་ཡིན་ཏེ། བཞི་གང་ཞེ་ན། སྦྱིན་གནས་མཆོག་ལ་དད་པར་འགྱུར་བ་དང་། བདག་ལ་བཟླས༌[^55]བལྟས་ཏེ་སེམས་ཅན་གཞན་ཡང་མཆོད་པ་བྱེད་པར་འགྱུར་བ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་ནས་བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པར་འགྱུར་བ་དང་། སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ་རྩ་གཉིས་མཐོང་ནས་དགེ་བའི་རྩ་བ་བསྡུས་པར་འགྱུར་བ་སྟེ་བཞི་པོ་འདི་དག་གོ་ཞེས་གསུངས་སོ། །

[Block 120]
སེམས་ཅན་མགུ་བར་བྱེད་པ་ཡང་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་བླ་ན་མེད་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^56]བ་ཚའི༌[^57]ཆུ་ཀླུང་གི་མདོ་ལས་ཇི་སྐད་གསུངས་པ་དང་། སློབ་དཔོན་ཞི་བ༌[^58]ལྷས་ཀྱང་།

[Block 121 [VERSE]]
གང་དག་བདེ་ན་ཐུབ་དབང་རྣམས་དགྱེས་ཤིང་། །
གང་ལ་གནོད་ན་ཐུབ་དབང་མི་དགྱེས་པ།[^59] །
དེ་དག་མགུ་བས་ཐུབ་དབང་ཐམས་ཅད་དགྱེས། །
དེ་ལ་གནོད་བྱས་ཐུབ་ལ་གནོད་བྱས་འགྱུར། །

[Block 122]
ཞེས་པ་དང་།

[Block 123]
ཡང་དེ་ཉིད་ལས།

[Block 124 [VERSE]]
དེ་བཞིན་གཤེགས་རྣམས་མཉེས་པར་བགྱི་སླད་དུ། །
འཇིག་རྟེན་བྲན་དུ་དེང་ནས་མཆི་བར་བགྱི། །
སྐྱེ་བོའི་ཚོགས་ཀྱིས༌[^60]བདག་མགོ་རྐང་བཅད་དམ། །
གསོད་ཀྱང་རུང་སྟེ་འཇིག་རྟེན་མགོན་དགྱེས་མཛོད། །

[Block 125 [VERSE]]
ཐུགས་རྗེ་ལྡན་པ་དག་གིས༌[^61]འགྲོ་འདི་ཀུན། །
བདག་གིར་མཛད་པ་འདི་ལ་དོགས་མ་མཆིས། །
སེམས་ཅན་གཟུགས་སུ་སྣང་བ་འདི་དག་ཀུན། །
མགོན་པོ་མིན་ནམ༌[^62]ཅི་ན་འདིར་མི་གུས། །

[Block 126]
དེ་བཞིན་གཤེགས་པ་མཉེས་བྱའང་དེ་ཉིད་ཡིན། །ཞེས་པ་དང་།

[Block 127]
ཡང་དེ་ཉིད་ལས།

[Block 128 [VERSE]]
བྱམས་པའི་བསམ་ལྡན་མཆོད་པ་གང་། །
དེ་ནི་སེམས་ཅན་ཆེ་བ་ཉིད། །
སངས་རྒྱས་དད་པའི་བསོད་ནམས་གང་། །
དེ་ནི་སངས་རྒྱས་ཆེ་བ་ཉིད། །

[Block 129]
ཅེས་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ལས་གསུངས་སོ། །

[Block 130]
སྤྱོད་འཇུག་ལས་ཀྱང་།

[Block 131]
སེམས་ཅན་མགུ་བྱ་མ་གཏོགས་པ། །རྒྱལ་བ་མཉེས་པའི་ཐབས་གཞན་མེད། །ཅེས་གསུངས་པ་དང་། ཡང་དེ་ཉིད་ལས་དོན་འདི་རྒྱས་པར་བཤད་དེ་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 132]
གཞན་ཡང་མདོ་ཉིད་ན་རྒྱས་པས་མདོ༌[^63]ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 133 [HEADING]]
##### དམིགས་པ་མེད་པའི་མཆོད་པ། ^1-2-2-2-0

[Block 134]
དེ་ལ་དམིགས་པ་མེད་པའི་མཆོད་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྒོམ་པ་ཡིན་ཏེ། དེ་ལ་ནི་མཆོད་པར་བྱ་བ་དང་། མཆོད་པར་བྱེད་པ་དང་། མཆོད་པའི་རྫས་མེད་དེ།

[Block 135]
དེ་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མདོ་ལས།

[Block 136 [VERSE]]
གང་གིས༌[^64]ང་ལ་གཟུགས་སུ་མཐོང་། །
གང་གིས་ང་ལ་སྒྲར་ཤེས་པ། །
དེ་དག་ལོག་པར་མཐོང་བ་སྟེ། །
སྐྱེ་བོ་འདི་ཡིས༌[^65]ང་མི་མཐོང་། །

[Block 137 [VERSE]]
སངས་རྒྱས་རྣམས་ནི་ཆོས་ཀྱི་སྐུ། །
འདྲེན་པ་རྣམས་ནི་ཆོས་ཉིད་བལྟ། །
ཆོས་ཉིད་མཐོང་བར་བྱ་མིན་པས། །
དེ་ནི་རྣམ་པར་ཤེས་མི་ནུས། །

[Block 138]
ཞེས་གསུངས་སོ། །

[Block 139]
དོན་འདི་ནི་འཕགས་པ་རྟག་ཏུ་ངུའི་ལེའུ་ལས་གསལ་བར་གསུངས་པས་དེར་བལྟ་བར་བྱའོ། །

[Block 140]
དེ་བས་ན་འཕགས་པ་སེང་གེ་སྒྲའི་མདོ་ལས།

[Block 141]
སངས་རྒྱས་སུ་འདུ་ཤེས་པ་ལ་སངས་རྒྱས་མཐོང་བ་མེད་ན། སངས་རྒྱས་ལ་མཆོད་པར་འགྱུར་བ་ལྟ་ཅི་སྨོས་དེ་ནི་གནས་མེད་དོ། །

[Block 142]
དེ་ལ་སངས་རྒྱས་ལ་མཆོད་པ་གང་ཞེ་ན། གང་འདུ་ཤེས་ཀྱི་མཚན་མ་མི་སྐྱེད་པའོ། །

[Block 143]
གང་ལ་སེམས་མེད་པ་དང་། སེམས་ལས་བྱུང་བ་མེད་པ་དང་། སངས་རྒྱས་སུ་འདུ་ཤེས་པ་མེད་པ་དང་། ཆོས་སུ་འདུ་ཤེས་པ་མེད་པ་དང་། དགེ་འདུན་དུ་འདུ་ཤེས་པ་མེད་པ་དང་། གང་ཟག་དང་། བདག་དང་། ཕ་རོལ་པོར་འདུ་ཤེས་པ་མེད་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། འདིའི་དོན་རྒྱས་པར་མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 144]
དེ་བས་ན་འཕགས་པ་ཐོགས་མེད་ཀྱི༌[^66]ཞལ་སྔ་ནས། སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་ནི་སྒྲུབ་པའི་མཆོད་པས་མཉེས་པར་འགྱུར་གྱི། ཟང་ཟིང་གི་མཆོད་པས་ནི་དེ་མཉེས་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡང་ལེགས་པར་དྲངས་པར་འགྱུར་རོ། །

[Block 145]
དེ་བས་ན་སངས་རྒྱས་ནི་ཆོས་ཀྱི་སྐུས་གནས་པ་ཡིན་ཏེ།
--- END BLOCKS ---
