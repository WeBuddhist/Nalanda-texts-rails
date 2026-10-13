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
[Block 141]
ཁྱད་པར་ཅན་གྱི་རྒྱན་མཆོག་ཐམས་ཅད་ཀྱིས། །ཞེས་བྱ་བ་ལ་རྒྱན་མཆོག་ཅེས་བྱ་བ་ནི་མང་པོའི་རྣམ་གྲངས་སོ། །

[Block 142]
ལྷ་དང་མིའི་རྣམ་པ་ཐམས་ཅད་དང་ལྡན་པའི་དམ་པ་རྣམས་ཀྱིས་རྒྱལ་བ་དེ་དག་ཐམས་ཅད་ལ་མཆོད་པར་བགྱིའོ། །

[Block 143 [HEADING]]
#### བླ་ན་མེད་པའི་མཆོད་པ། ^2-2-2-0

[Block 144]
ད་ནི་བླ་ན་མེད་པའི་མཆོད་པ༌[^46]བཤད་པར་བྱ་སྟེ། མཆོད་པ་གང་རྣམས་བླ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། བླ་ན་མེད་པའི་མཆོད་པ་རྒྱ་ཆེ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་གྱི་མཐུ་ལས་སྐྱེས་པ་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་དུ་ཁྱབ་པར་ཆོས་ཀྱི་དབྱིངས་དམ་པས་རྒྱལ་བ་དེ་དག་ཀུན་ལ་བདག་གི་བསམ་པས་སོ།[^47] །

[Block 145]
བཟང་པོ་སྤྱོད༌[^48]ལ་དད་པའི་སྟོབས་དག་གིས། །ཞེས་བྱ་བ་ནི་བཟང་པོ་སྤྱོད་པ་ལ་མོས་པ་དང་། དད་ཅིང་ངེས་པར་ཡིད་ཆེས་པ་དེའི་སྟོབས་ཀྱིས་སོ། །

[Block 146]
བཟང་པོ་སྤྱོད་པ་ནི་མདོ་སྡེ་དུ་མ་ནས་བྱང་ཆུབ་སེམས་དཔའི་མཆོད་པ་རྣམ་པ་སྣ་ཚོགས་འབྱུང་བའོ། །

[Block 147]
ད་ནི་ཇི་ལྟར་བཤད་པའི་ཕྱག་བྱ་བ་དང་། མཆོད་པ་རྣམས་མཇུག་བརྟུལ་བའི་ཕྱིར། རྒྱལ་བ་ཀུན་ལ་ཕྱག་འཚལ་མཆོད་པར་བགྱི། །ཞེས་བྱ་བ་བཤད་དེ། རྒྱལ་བ་ཐམས་ཅད་ལ་ཕྱག་བྱ་ཞིང་མཆོད་པར་བྱའོ། །

[Block 148 [HEADING]]
### སྡིག་པ་བཤགས་པ། ^2-3-0

[Block 149]
རང་བཞིན་དང་རྒྱུ་དང་གནས་ཏེ༌[^49]གསུམ་གྱི༌[^50]སྡིག་པ་བཤགས་པར་བཤད་དེ། འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་དབང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 150 [HEADING]]
#### རང་བཞིན། ^2-3-1-0

[Block 151]
དེ་ལ་རང་བཞིན་ནི། །སྡིག་པ་བདག་གིས་བགྱིས་པ་ཅི་མཆིས་པ། །ཞེས་བྱ་བ་སྟེ། ཚེ་འདི་དང་ཚེ་གཞན་དུ་བྱས་པ་དང་། བྱེད་དུ་བཅུག་པ་དང་། རྗེས་སུ་ཡི་རང་བ་རྣམས་སོ། །

[Block 152 [HEADING]]
#### རྒྱུ། ^2-3-2-0

[Block 153]
རྒྱུ་གང་གིས་ཤེ་ན། འདོད་ཆགས༌[^51]ཞེ་སྡང་གཏི་མུག་དབང་གིས་སོ། །

[Block 154 [HEADING]]
#### གནས། ^2-3-3-0

[Block 155]
གནས་གང་ཞེ་ན། ལུས་དང་ངག་དང་ཡིད་ལ་གནས་ནས་སོ། །

[Block 156]
དེ་ལྟ་བུ་དེ་དག་ཐམས་ཅད་རྒྱལ་བ་ཀུན་དང་དེའི་སྲས་རྣམས་ཀྱི་སྤྱན་སྔར་འདུག་པ་བཞིན་དུ་ཤིན་ཏུ་འགྱོད་པའི་ཡིད་ཀྱིས་སྐད་ཅིག་རེ་རེ་ལ་ཡང་བཤགས་ཤིང་སྨྱུར༌[^52]ཏེ་སྐྱུག༌[^53]པར་བྱའོ། །

[Block 157 [HEADING]]
### བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ། ^2-4-0

[Block 158]
ད་ནི་བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་བཤད་དེ། ཕྱོགས་བཅུའི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 159]
ཕྱོགས་བཅུའི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དང་བསྒོམ་པ༌[^54]ལས་བྱུང་བའི་བསོད་ནམས་དང་། དུས་གསུམ་དུ་གང་སློབ་པའི་གང་ཟག་བདུན་དང་། གང་མི་སློབ་པའི་དགྲ་བཅོམ་པ་དང་། གང་རང་རྒྱལ་བའི་རྣམ་པ་སྟེ།[^55] དེ་ཡང་བསེ་རུ་ལྟ་བུ་དང་། སྡེས་རྒྱུ་བ་དང་རྣམ་པ་གཉིས་ཀྱི༌[^56]འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་དུས་གསུམ་གྱི་བསོད་ནམས་དང་། གང་ཐོག་མར་སེམས་བསྐྱེད་པ་རྣམས་ནས་བཟུང་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་དང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་གང་དུས་གསུམ་དུ་གཤེགས་པ་རྣམས་ཀྱི་དང་། བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པར་རྟོགས་པ༌[^57]ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ས་ལ་སོགས་པ་ལས་སྐྱེས་པ་དང་། དུས་གསུམ་དུ་གཤེགས་པ་འཇིག་རྟེན་གྱི་དང་། འཇིག་རྟེན་ལས་འདས་པ་རེ་རེའི་བསོད་ནམས་ཀྱི་ཚོགས་ཚད་མེད་པ་བསམ་དུ་མེད་པ་དང་། སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་དེ་དག་ཐམས་ཅད་ལ་སྐད་ཅིག་རེ་རེ་ཞིང་ཡང་རྗེས་སུ་ཡི་རང་བར་བྱའོ། །

[Block 160]
འགྲོ་བ་ཞེས་བྱ་བའི་ཚིག་ནི་མ་ལུས་པར་སྙེགས་པས༌[^58]སློབ་པ་ལ་སོགས་པའི་བསོད་ནམས་ཀྱང་འདུས་ན་ཅིའི་ཕྱིར་ཐ་དད་དུ་སྨོས་ཤེ་ན་དེ་ལྟ་མ་ཡིན་ཏེ། འགྲོ་བས་ན་འགྲོ་བ་སྟེ༌[^59]སྲེད་པ་དང་བཅས་པས་འཁོར་བར༌[^60]འཁོར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 161]
དེ་ལ་གང་ཡང་འགྲོ་བ་མེད་ན་ཇི་ལྟར་འགྲོ་བ་ཞེས་བྱ། དེ་བས་ན་སོ་སོར་བསྟན་ཏོ། །

[Block 162 [HEADING]]
### ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་བསྐུལ་བ། ^2-5-0

[Block 163]
ད་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་བསྐུལ་བ༌[^61]བཤད་དེ།

[Block 164 [VERSE]]
གང་རྣམས་ཕྱོགས་བཅུའི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །
གང་རྣམས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་སྒྲོན་མ་དག །

[Block 165]
ཅེས་བྱ་བ་ནི་འགྲོ་བའི་སྒྲོན་མ་སྟེ། །འཇིག་རྟེན་གྱི་ཕྱི་དང་ནང་གི་མུན་པ་མང་པོ་རྣམ་པར་སེལ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་འཇིག་རྟེན་གྱི་སྒྲོན་མའོ། །

[Block 166]
བྱང་ཆུབ་རིམ་པར་སངས་རྒྱས་ཞེས་བྱ་བ་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་སངས་རྒྱས་པའོ། །

[Block 167]
མ་ཆགས་བརྙེས་ཞེས་བྱ་བ་ནི་མངོན་པར་བྱང་ཆུབ་པའི་སྟོབས་ཀྱིས༌[^62]དངོས་པོ་ཐམས་ཅད་ཀྱི་རང་བཞིན་མ་ལུས་པར་ཡོངས་སུ་མཁྱེན་པས་ཆགས་པར་གྱུར་པ་ཐམས་ཅད་ལས་འདས་པའོ། །

[Block 168]
ཆོས་ཟབ་མོ་རྟོགས་པར་བྱ་བ་ལ་གཞན་དག་མི་འདོད་ཅིང་། བརྩོན་འགྲུས་རྩོམ་པས་ཁོང་དུ་ཆུད་པར་བྱ་བར་དཀའ་བས་ན་ཆོས་འཆད་པའི་ཕྱིར་སྤྲོ་བ༌[^63]མི་མཛད་པར་འཇིག་རྟེན་སྣ་ཚོགས་པའི་བྱང་ཆུབ་ཀྱི་ཤིང་དམ་པའི་དྲུང་དུ་བཞུགས་པའི་འཇིག་རྟེན་གྱི་མགོན་པོ་ཐམས་ཅད་ལ་འགྲོ་བ་རྣམས་ཀྱི་མི་ཤེས་པའི་མུན་གནག༌[^64]བསལ་བར་བྱ་ཞིང་བླ་ན་མེད་པའི་ཡེ་ཤེས་ཀྱི༌[^65]སྣང་བར་བྱ་བར་བླ་ན་མེད་པའི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བའི་ཕྱིར་པུས་མོ་གཉིས་ས་ལ་བཙུགས་ནས་ཐལ་མོ་སྦྱར་ཏེ་མདུན་ན་འདུག་པ་བཞིན་དུ་བསྐུལ་བར་བྱའོ། །

[Block 169 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ། ^2-6-0

[Block 170]
ད་ནི་དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ་གདབ་པ་ནི། མྱ་ངན་འདའ༌[^66]སྟོན༌[^67]གང་བཞེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་ཞེས་བྱ་བ་ཁྱད་པར་དུ་མ་བརྗོད་ཀྱང་། གང་རྣམས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་སྒྲོན་མ་དག །ཅེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 171]
ཕྱོགས་བཅུ་ན༌[^68]སངས་རྒྱས་བཅོམ་ལྡན་འདས་བཞུགས་པ་རྣམས་མྱ་ངན་ལས་འདའ༌[^69]ཞིང་མྱ་ངན་ལས་འདའ་བ་སྟོན་པར་བྱེད་པ་གང་དག་ཡིན་པ་དེ་དག་ཐམས་ཅད་ལ་བདག་གིས་ཐལ་མོ་སྦྱར་ཏེ་ཡུན་རིང་དུ་བཞུགས་པར་གསོལ་བ་གདབ་པོ། །ཅིའི་ཕྱིར་ཞེ་ན། མགོན་མེད་པར་གྱུར་པའི་འགྲོ་བ་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བའི་ཕྱིར་ཏེ། དེ་ལ་ཕན་པ་ཞེས་བྱ་བ་ནི་བདེ་བ་དང་ལྡན་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་འཐོབ་པར་བྱེད་པའོ། །

[Block 172]
བདེ་བ་ཞེས་བྱ་བ་ནི་ལྷའི་ལོངས་སྤྱོད་ཐོབ་པར་བྱེད་པའོ། །

[Block 173]
དུས་ཇི་སྲིད་དུ་ཞེ་ན། དུས་གསུམ་དུ་གཤེགས་པའི་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི༌[^70]བསྐལ་པར་བཞུགས་སུ་གསོལ་བའོ། །

[Block 174 [HEADING]]
### དགེ་བའི་རྩ་བ་ཡོངས་སུ་བསྔོ་བ། ^2-7-0

[Block 175]
ད་ནི་ཇི་ལྟར་བཤད་པའི་ཕྱག་བྱ་བ་ལ་སོགས་པ་ཚད་མེད་པ་ལས་བྱུང་བའི་བསོད་ནམས་མ་ལུས་པ་རྣམས་ཡོངས་སུ་བསྔོ་བར་བྱ་སྟེ། ཕྱག་འཚལ་བ་དང་། མཆོད་ཅིང་བཤགས་པ་དང་། བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་བསྐུལ་བ་དང་བདེ་བར་གཤེགས་པ་བཞུགས་པར་གསོལ་བ་རྣམས་ཀྱི་དགེ་བ་ཅུང་ཟད་བདག་གིས་ཅི་བསགས་པ་དེ་དག་ཐམས་ཅད་བདག་གིས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོ་བར་བྱའོ། །

[Block 176 [HEADING]]
### བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་ཡན་ལག་རབ་ཏུ་དབྱེ་བ། ^2-8-0

[Block 177]
ད་ནི་དེའི་རབ་ཏུ་དབྱེ་བ་སྟེ་བརྒྱད་པའོ། །

[Block 178]
དེ་ཡང་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་ཡན་ལག་རབ་ཏུ་དབྱེ་བ་སྟེ། དེ་དག་ནི་རྣམ་པ་བཅུ་དྲུག་གོ། །

[Block 179]
འདི་ལྟ་སྟེ། བསམ་པ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ་དང་། ཆགས་པ་མེད་པར་སྦྱོར་བ་དང་། སེམས་ཅན་ལ་ཕན་གདགས་པ༌[^71]དང་། གོ་ཆ་བགོ་བ་དང་། སྐལ་བ་མཐུན་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟེན་པ་དང་། དགེ་བའི་བཤེས་གཉེན་མགུ་བར་བྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པ་མངོན་སུམ་དུ་བྱ་བ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་བསྡུ་བ་དང་། མི་ཟད་པའི་མཛོད་རྙེད་པ་དང་། འཇུག་པར་བྱ་བ་དང་། སྟོབས་དང་། གཉེན་པོ་དང་། ལས་དང་། རྗེས་སུ་སློབ་ཅིང་བསྔོ་བ་དང་། བསྡུ་བར་བྱ་བ་རྣམས་སོ། །

[Block 180 [HEADING]]
#### བསམ་པ། ^2-8-1-0
--- END BLOCKS ---
