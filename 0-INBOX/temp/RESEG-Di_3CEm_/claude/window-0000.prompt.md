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
## ༄༅། །ཀུན་ཏུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་གྱི་རྒྱལ་པོའི་བཤད་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ས་མནྟ་བྷ་དྲ་ཙརྱ་པྲ་ཎི་དྷཱ་ནརྠ་སཾ་གྲ་ཧ་ཀྲི་ཏི་ཨཱ་ཙཱརྱ་དིཀ་ནཱ་ག་པཱ་དེ༌[^1]ན། བོད་སྐད་དུ། ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་གྱི་དོན་ཀུན་བསྡུས་ཏེ། སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོའི་ཞབས་ཀྱིས༌[^2]མཛད་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་གྱི་དོན་ཀུན་བསྡུས་པ། ^1-0

[Block 5]
ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་ལ་དོན་རྣམ་པ་བཅུ་ཡོད་དོ།[^3] །

[Block 6]
འདི་ལྟ་སྟེ། དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ་དང་། དེ་ལ་མཆོད་པ་དང་། ཉེས་པ་བཤགས་པ་དང་། བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བར་བསྐུལ་བ་དང་། དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ་དང་། དགེ་བའི་རྩ་བ་རབ་ཏུ་བསགས་པ་ཡོངས་སུ་བསྔོ་བ་དང་། དེའི་རབ་ཏུ་དབྱེ་བ་དང་། དེའི་མཐའ་དང་། དེའི་ལེགས་པའོ། །

[Block 7 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ། ^1-1-0

[Block 8]
དེ་ལ་ཕྱོགས་བཅུའི་ཞིང་དང་དུས་ཐམས་ཅད་དུ་གཤེགས་པའི་སངས་རྒྱས་རྣམས་ལ་ལུས་དང་ངག་དང་ཡིད་ཀྱིས་ཕྱག་བྱ་བ་ལས་བརྩམས་ཏེ་གསུངས་པ། ཇི་སྙེད་སུ་དག་ཕྱོགས་བཅུའི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 9]
ལུས་ཀྱིས་ནི་ཞིང་གི་རྡུལ་སྙེད་ལ་སོགས་པའོ། །

[Block 10]
ཡིད་ཀྱིས༌[^4]ནི་རྡུལ་གཅིག་སྟེང་ན་རྡུལ་སྙེད་ལ་སོགས་པའོ། །

[Block 11]
ངག་གིས་ནི་དེ་དག་བསྔགས་པ་མི་ཟད༌[^5]རྒྱ་མཚོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 12 [HEADING]]
### མཆོད་པ། ^1-2-0

[Block 13]
མཆོད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བླ་ན་ཡོད་པ་དང་། བླ་ན་མེད་པའོ། །

[Block 14 [HEADING]]
#### བླ་ན་ཡོད་པའི་མཆོད་པ། ^1-2-1-0

[Block 15]
བླ་ན་ཡོད་པ་ནི། ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་བསྟན་ཏེ། མེ་ཏོག་དམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 16 [HEADING]]
#### བླ་ན་མེད་པ། ^1-2-2-0

[Block 17]
བླ་ན་མེད་པ་ནི་མཆོད་པ་གང་རྣམས་བླ་ན༌[^6]མེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 18 [HEADING]]
### ཉེས་པ་བཤགས་པ། ^1-3-0

[Block 19]
རང་བཞིན་དང་གཞི་དང་གནས་ཀྱི་ཉེས་པ་བཤགས་པ་ལས་བརྩམས་ཏེ་གསུངས་པ། འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 20 [HEADING]]
### བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ། ^1-4-0

[Block 21]
བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བའི་དབང་དུ་བྱས་ཏེ་གསུངས་པ། ཕྱོགས་བཅུའི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 22 [HEADING]]
### ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བར་བསྐུལ་བ། ^1-5-0

[Block 23]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ལ༌[^7]ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བར་བསྐུལ་བ་ལས་བརྩམས་ཏེ་གསུངས་པ། གང་རྣམས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་སྒྲོན་མ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 24 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ། ^1-6-0

[Block 25]
དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ་ནི། མྱ་ངན་འདས་སྟོན་གང་བཞེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 26 [HEADING]]
### དགེ་བའི་རྩ་བ་རབ་ཏུ་བསགས་པ་ཡོངས་སུ་བསྔོ་བ། ^1-7-0

[Block 27]
དགེ་བའི་རྩ་བ་རབ་ཏུ་བསགས་པ་ཡོངས་སུ་བསྔོ་བ་ནི། ཕྱག་འཚལ་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའོ། །

[Block 28 [HEADING]]
### ཀུན་དུ་བཟང་པོའི་སྨོན་ལམ་རབ་ཏུ་དབྱེ་བ། ^1-8-0

[Block 29]
ཀུན་དུ་བཟང་པོའི་སྨོན་ལམ་རབ་ཏུ་དབྱེ་བ་ནི་རྣམ་པ་བཅུ་དྲུག་གོ། །

[Block 30]
འདི་ལྟ་སྟེ། བསམ་པ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ་དང་། མི་ཆགས་པའི་སྦྱོར་བ་དང་། སེམས་ཅན་ལ་ཕན་གདགས་པ་དང་། གོ་ཆ་དང་། སྐལ་པ་མཉམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་། འགྲོགས་པ་དང་། དག་བའི་བཤེས་གཉེན་དང་འགྲོགས་པ་དང་། དེ་བཞིན་གཤེགས་པ་མངོན་དུ་འགྱུར་བ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་གཟུང་བ་དང་། མི་ཟད་པའི་མཛོད་རབ་ཏུ་རྙེད་པ་དང་། འཇུག་པ་དང་། སྟོབས་དང་། གཉེན་པོ་དང་། ལས་དང་། རྗེས་སུ་སློབ་པར་བསྔོ་བ་དང་། བསྡུ་བའོ། །

[Block 31 [HEADING]]
#### བསམ་པ། ^1-8-1-0

[Block 32]
དེ་ལ་བསམ་པ་ནི་རྣམ་པ་གསུམ་སྟེ། དེ་བཞིན་གཤེགས་པའི་དགོངས་པ་ཡོངས་སུ་བསྐང་བའི་བསམ་པ་ནི་གང་གསུངས་པ། འདས་པའི་སངས་རྒྱས་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 33]
སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་སྦྱང་བའི༌[^8]བསམ་པ་ནི། ཕྱོགས་བཅུ་ག་ལའི་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 34]
སེམས་ཅན་ལ་ཕན་པ་དང་བདེ་བའི་བསམ་པ་ནི་གང་གསུངས་པ། ཕྱོགས་བཅུའི་སེམས་ཅན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 35 [HEADING]]
#### བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ། ^1-8-2-0

[Block 36]
གཉེན་པོ་དང་བཅས་པས་མི་མཐུན་པའི་ཕྱོགས་སྤང་བ་བསྟན་པ༌[^9]ནི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པ་སྟེ། གང་གསུངས༌[^10]པ། བྱང་ཆུབ་སྤྱོད་པ་དག་ནི་བདག་སྤྱོད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 37 [HEADING]]
#### མི་ཆགས་པའི་སྦྱོར་བ། ^1-8-3-0

[Block 38]
གང་ལས་ཅི་ལ་ཇི་ལྟར་མི་ཆགས་པའི་སྦྱོར་བ་དེ་བསྟན་པའི་ཕྱིར་གསུངས་པ། ལས་དང་ཉོན་མོངས་བདུད་ཀྱི་ལས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 39 [HEADING]]
#### སེམས་ཅན་ལ་ཕན་གདགས་པ། ^1-8-4-0

[Block 40]
ཚེ་འདི་དང་གཞན་དུ་སེམས་ཅན་ལ་ཕན་པའི་དབང་དུ་བྱས་ཏེ་གསུངས་པ། ངན་སོང་སྡུག་བསྔལ་རབ་ཏུ་ཞི་བར་བྱེད། །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
