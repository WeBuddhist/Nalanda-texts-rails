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
འབྱུང་པོ་ཀུན་ལ་དགའ་བཞིན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་གཏན་ཚིགས་སོ། །

[Block 107]
འདི་སྐད་ཐོས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ནི་དཔེའོ། །

[Block 108]
སེམས་ཅན་ཞེས་བྱ་བ་ནི་སྐྱེ་དགུའོ། །

[Block 109]
ཐམས་ཅད་ནི་ལུས་པ་མེད་པའོ། །

[Block 110]
རྒྱུ་མེད་པར་ཞེས་བྱ་བ༌[^58]ནི་དགོས་པ་མེད་པར་རོ། །

[Block 111]
རབ་ཏུ་ཞེས་བྱ་བ་ནི། ཡང་དག་པར་རབ་ཏུ་དང་བའོ། །

[Block 112]
བྱམས་པ་ནི་མཉེས་གཤིན༌[^59]པ་དང་ལྡན་པའོ། །

[Block 113]
ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ནི་རང་བཞིན་ནོ། །

[Block 114]
འབྱུང་པོ་ཀུན་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་དོ། །

[Block 115]
བདག་བཞིན་དུ་གྱུར་པ༌[^60]ཞེས་བྱ་བ་ནི་བདག་དང་མཉམ་པས་སོ། །

[Block 116]
སྐུ་ཚེ་སྔ༌[^61]མ་ལ་ཡང་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་དུས་ནའོ། །

[Block 117]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་འཇིག་རྟེན་ལ་དེ་བཞིན་ཉིད་དུ་རབ་ཏུ་སྟོན་པ་ཡིན་པས་ན་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་བཤད་པའོ། །

[Block 118]
བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནི་བདུད་བཞི་བཅོམ་བས་ན་བཅོམ་ལྡན་འདས་སོ།[^62] །དེ་བས་ན་གཙོ་བོ་སྟེ་དམ་པ་དེ་ལ་སེམས་དང་བར་བྱ་བ་ནི་དད་པར་བྱ་བའོ། །

[Block 119]
དེ་ཡང་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་གསུམ་མོ། །

[Block 120]
འདི་སྐད་ཐོས་ཞེས་བྱ་བ་ནི་བཤད་པའོ།[^63] །བདག་ཅག་གི་བླ་མ་དཀོན་མཆོག་གསུམ་བླ་མར་བྱེད་པ་གང་ཡིན་པ་དེ་དག་ནི་བླ་མ་དཀོན་མཆོག་གསུམ་བླ་མར་བྱེད་པའོ། །

[Block 121]
བསྒྲུབ་པའི༌[^64]ཡོན་ཏན་ནི་ཚུལ་ཁྲིམས་ཀྱིས་བསྒྲུབ༌[^65]པའི་ཡོན་ཏན་ཏེ།[^66] སྐྱོན་མེད་ཅིང་འདྲེན་མར་མ་གྱུར་པས་བླ་མ་རྣམས་ཏེ། སློབ་དཔོན་དང་། མཁན་པོ་དང་། འཕགས་པ་དགའ་མགུ་བར་བྱའོ། །

[Block 122]
ཡོན་ཏན་གྱི་ཚོགས་ནི་ཡོན་ཏན་བསགས་པ་སྟེ་དེས་བདག་ཅག༌[^67]གི་བླ་མར་གྱུར་པའོ། །

[Block 123]
མཁན་པོ་དག་གིས་ཡོངས་སུ་བསྒྲགས་པ་ནི་བསྔགས་པར་སྨྲ་བ་དག་བསྟན་པའོ། །

[Block 124]
འདི་ཞེས་བྱ་བ་ནི་སྟོན་པ་ཡིན་ཏེ། ཅི་ཞིག་སྟོན་པ་ཡིན་ཞེ་ན། བཅོམ་ལྡན་འདས་ཀྱི་སྐུ་ཚེ་སྔ་མ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པའིའོ། །

[Block 125]
རྟོགས་པ་བརྗོད་པ་སྤྱོད་པའི་མཚན་མའོ། །

[Block 126]
བྱང་ཆུབ་སེམས་དཔའ་ནི་བྱང་ཆུབ་སེམས་དཔས་ན་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 127]
དམ་བཅས་པས་ཁྱད་པར་ཅན་ཞེས་བྱ་བ་དང་པོ་སེམས་བསྐྱེད་པ༌[^68]དེ་དང་རྗེས་སུ་མཐུན་པ་སྟེ། བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་འདིས་སོ། །

[Block 128]
དམ་བཅས་པ་ཁྱད་པར་ཅན་ནི་དམ་བཅས་པ་དམ་པའོ། །

[Block 129]
དེ་གང་ཡིན་ཞེ་ན། སངས་རྒྱས་ཏེ་དེ་དང་མཐུན་པ་ནི་འདྲ་བའོ། །

[Block 130]
གང་བྱིན་པ་དེ་ནི་སྦྱིན་པའོ། །

[Block 131]
ཚིག་སྙན་པ་ནི་གཏམ་སྙན་པའོ། །

[Block 132]
དོན་སྤྱོད་པ་ནི་ཕན་པ་སྤྱོད་པའོ། །

[Block 133]
སོགས་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲ་ནི་དོན་མཐུན་པ་དང་གཞན་ཡང་ཡོན་ཏན་དག་གོ། །

[Block 134]
དོན་མཐུན་པར་སྤྱོད་པ་ནི་དོན་མཐུན་པ་སྟེ་དགེ་བའི་ཆོས་སོ། །

[Block 135]
གཞན་ཡང་ཡོན་ཏན་གྱི་ཆོས་རྣམས་ཡོངས་སུ་གཟུང༌[^69]ངོ་། །ཤེས་རབ་ཀྱིས་ཡོངས་སུ་ཟིན་པས༌[^70]ཞེས་བྱ་བ་ནི་འདིས་ཡོངས་སུ་བཟུང་བས༌[^71]ན་ཡོངས་སུ་ཟིན་པ་སྟེ། ཤེས་རབ་ཉིད་ཀྱིས་ཡོངས་སུ་གཟུང་བའི་ཕྱིར་ཤེས་རབ་ཀྱིས་ཡོངས་སུ་ཟིན་པའོ། །ཤེས་རབ་ཀྱིས་བཟུང་བས་ན་སྐྱོན་མེད་པ་སྟེ་མ་སྨད་པའོ་སྙིང་རྗེའི་རྒྱུ་མཐུན་པ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་རྒྱུས་སྙིང་རྗེ་དང་རྗེས་སུ་མཐུན་པ་སྟེ། རྒྱུ་མཐུན་པ་ནི་རྒྱུ་དང་འདྲ་བའི་ཚིག་གོ། །

[Block 136]
ཡོངས་སུ་འཛིན་པ་ནི་མགུ་བར་བྱས་པའོ། །

[Block 137]
རང་གི་ཆོས་ཡིན་པས་ན་རང་གི་ཆོས་དེ༌[^72]ལས་རྣམ་པ་དྲུག་གོ། །

[Block 138]
དེ་ཡང་མཆོད་སྦྱིན་དང་། མཆོད་སྦྱིན་བྱེད་དུ་འཇུག་པ་དང་། འདོན་པ་དང་། འདོན་དུ་འཇུག་པ་དང་། སྦྱིན་པ་དང་། ལེན་པའོ། །

[Block 139]
ཆོས་དེ་རྣམས་ལ༌[^73]མངོན་པར་དགའ་བ་ལས་གྱུར་པའི་རིགས་ཀྱི་གཙང་སྦྲ་སྤྱོད་པ་གང་ཡིན་པ་དེ་ནི་རང་གི་ཆོས་ལ་མངོན་པར་དགའ་བ༌[^74]ལས་གྱུར་པའི་གཙང་སྦྲའི་སྤྱོད་པ་སྟེ། དེ་ལ་གཙང་སྦྲ་ནི་དག་པའི་སྤྱོད་པ་སྟེ། དག་པར་སྤྱོད་པའི་ཚུལ་ཀུན་ཏུ་སྤྱོད་པའོ། །

[Block 140]
ཆེན་པོ་ཞེས་བྱ་བ་ནི་རིགས་གཞན་ལ་ལྟོས་པས༌[^75]ཆེན་པོའོ། །

[Block 141]
ཇེ་མཐོ་ཇེ་མཐོར་ཞེས་བྱ་བ་ནི་སྐྱེས་ཤིང་སྐྱེས་པ་ནའོ། །

[Block 142]
ཡང་ན་མཐོ་བའི་རིགས་དེ་ལས་བྱང་ཆུབ་སེམས་དཔའ་མཐོ་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 143]
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་འབྱུང་བར་འགྱུར་བའོ། །

[Block 144]
ཡོངས་སུ་བཟུང་བ་ནི་ཐོབ་པར་བྱས་པའོ། །

[Block 145]
གྲགས་སོ༌[^76]ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་མ་གྱུར་བའི་ཚིག་གོ། །
--- END BLOCKS ---
