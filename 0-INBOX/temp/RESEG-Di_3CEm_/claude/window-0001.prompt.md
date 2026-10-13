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

[Block 41 [HEADING]]
#### གོ་ཆ། ^1-8-5-0

[Block 42]
སེམས་ཅན་གྱི་སྤྱོད་པའི་རྗེས་སུ་འཇུག་པ་དང་། སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་བསྐང་བ་དང་། དམ་པའི་ཆོས་རབ་ཏུ་བསྟན་པས་གོ་ཆ་རྣམ་པ་གསུམ་སྟེ། གང་གསུངས་པ། སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པ༌[^11]དང་མཐུན་པར་འཇུག་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 43 [HEADING]]
#### སྐལ་པ་མཉམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་འགྲོགས་པ། ^1-8-6-0

[Block 44]
ལུས་དང་ངག་དང་སྤྱོད་པ་དང་སྨོན་ལམ་གྱི་སྐལ་བ་མཉམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་འགྲོགས་པ་སྟེ། གང་གསུངས་པ། བདག་གི་སྤྱོད་དང་མཐུན་པར་གང་སྤྱོད་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 45 [HEADING]]
#### དགེ་བའི་བཤེས་གཉེན་དང་འགྲོགས་པ། ^1-8-7-0

[Block 46]
ཕན་པའི་བསམ་པ་བསྟན་པ་དང་ནན་ཏན་གྱིས༌[^12]དགེ་བའི་བཤེས་གཉེན་གྱི་དབང་དུ་མཛད་ནས་གང་གསུངས་པ། བདག་ལ་ཕན་པར་འདོད་པའི་གྲོགས་པོ་དག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 47 [HEADING]]
#### དེ་བཞིན་གཤེགས་པ་མངོན་དུ་འགྱུར་བ། ^1-8-8-0

[Block 48]
དུས་དང་འཁོར་དང་མཆོད་པ་བྱེད་པ་ལ་ཡོངས་སུ་མི་སྐྱོ་བས་དེ་བཞིན་གཤེགས་པ་མངོན་དུ་འགྱུར་བ་སྟེ། གང་གསུངས་པ། མངོན་སུམ་རྟག་ཏུ་བདག་གིས་རྒྱལ་བ་བལྟ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 49 [HEADING]]
#### དམ་པའི་ཆོས་ཡོངས་སུ་གཟུང་བ། ^1-8-9-0

[Block 50]
འཛིན་པ་དང་ཡོངས་སུ་སྦྱོང་བ༌[^13]དང་བཤད་པས་དམ་པའི་ཆོས་ཡོངས་སུ་གཟུང་བར་གསུངས་པ། རྒྱལ་བ་རྣམས་ཀྱི་དམ་པའི་ཆོས་འཛིན་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 51 [HEADING]]
#### མི་ཟད་པའི་མཛོད་རབ་ཏུ་རྙེད་པ། ^1-8-10-0

[Block 52]
བསོད་ནམས་དང་ཡེ་ཤེས་ལ་སོགས་པ་ཚོགས་བསྒྲུབས་པས་མི་ཟད་པའི་མཛོད་རབ་ཏུ་རྙེད་པར་གང་གསུངས་པ། སྲིད་པ་ཐམས་ཅད་དུ་ནི་འཁོར་བ་ན། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 53 [HEADING]]
#### འཇུག་པ། ^1-8-11-0

[Block 54]
འཇུག་པ་ནི་རྣམ་པ་བརྒྱད་དེ། སངས་རྒྱས་དང་དེའི་ཞིང་མཐོང་བ་ལ་འཇུག་པའི༌[^14]ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་བསྟན་ཏེ། གང་གསུངས་པ། རྡུལ་གཅིག་སྟེང་ན་རྡུལ་སྙེད་ཞིང་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 55]
སངས་རྒྱས་ཀྱི་གསུང༌[^15]ལ་འཇུག་པ་ནི་གང་གསུངས་པ། གསུང་གཅིག་ཡན་ལག་རྒྱ་མཚོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 56]
ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་ལ༌[^16]འཇུག་པར་གསུངས་པ་ནི། དེ་དག་གི་ཡང་གསུང༌[^17]དབྱངས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 57]
བསྐལ་པར་རབ་ཏུ་འཇུག་པ་ནི་གང་གསུངས་པ། མ་འོངས་བསྐལ་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 58]
དེ་བཞིན་གཤེགས་པའི་སྤྱོད་ཡུལ་ལ་འཇུག་པ་ནི་གང་གསུངས་པ། དུས་གསུམ་གཤེགས་པ་མིའི་སེང་གེ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 59]
སངས་རྒྱས་ཀྱི་ཞིང་སྒྲུབ་པ་ལ་འཇུག་པར་གང༌[^18]གསུངས་པ། གང་ཡང་དུས་གསུམ་དག་གི་ཞིང་གི་རྒྱན། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 60]
དེ་བཞིན་གཤེགས་པའི་དྲུང་དུ་འགྲོ་བར་འཇུག་པ་བརྒྱད་པ་ནི་གང་གསུངས་པ། གང་ཡང་མ་བྱོན་འཇིག་རྟེན་སྒྲོན་མ་དག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 61 [HEADING]]
#### སྟོབས། ^1-8-12-0

[Block 62]
སྟོབས་ནི་རྣམ་པ་བཅུ་སྟེ། ཚིགས་སུ་བཅད་པ་གཉིས་ལས་རྫུ་འཕྲུལ་ལ་སོགས་པའོ། །

[Block 63]
ཀུན་དུ་མྱུར་བའི་རྫུ་འཕྲུལ་སྟོབས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 64 [HEADING]]
#### གཉེན་པོ། ^1-8-13-0

[Block 65]
གཉེན་པོ་ནི་ལས་དང་ཉོན་མོངས་པ་དང་བདུད་ཀྱི་སྟོབས་མི་མཐུན་པའི་ཕྱོགས་རབ་ཏུ་གཞོམ༌[^19]པའི་ཕྱིར་རྣམ་པ་གསུམ་དུ་གང༌[^20]གསུངས་པ། ལས་ཀྱི་སྟོབས་རྣམས་ཡོངས་སུ་དག་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 66 [HEADING]]
#### ལས། ^1-8-14-0

[Block 67]
སངས་རྒྱས་ཀྱི་ཞིང་རྒྱ་མཚོ་ཡོངས་སུ་སྦྱང་བ༌[^21]ལ་སོགས་པ་ལས་ནི་རྣམ་པ་བརྒྱད་དེ། ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་གསུངས་པ། ཞིང་རྣམས་རྒྱ་མཚོ་རྣམ་པར་དག་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 68 [HEADING]]
#### རྗེས་སུ་སློབ་པར་བསྔོ་བ། ^1-8-15-0

[Block 69]
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་རྗེས་སུ་སློབ་པར་ཡོངས་སུ་བསྔོ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་ལ་དེ་བཞིན་གཤེགས་པའི་རྗེས་སུ་སློབ་པར་བསྔོ་བ་ནི། གང་ཡང་དུས་གསུམ་གཤེགས་པ་རྒྱལ་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 70]
ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྤྱོད་པ་དང༌[^22]ཞིང་དང་སྨོན་ལམ་རྣམ་པར་དག་པས་འཕགས་པ་ཀུན་དུ་བཟང་པོ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རྗེས་སུ་སློབ་པར་བསྔོ་བ་ནི་ཚིགས་སུ་བཅད་པ་གསུམ་གྱིས་གསུངས་པ། རྒྱལ་བ་ཀུན་གྱི་སྲས་ཀྱི་ཐུ་བོ་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 71 [HEADING]]
#### བསྡུ་བ། ^1-8-16-0

[Block 72]
ཚད་དང་སྦྱོར་བ་དང་ཡོན་ཏན་དང་སྤྱོད་པ་དང་གནས་ཀྱི་བྱེ་བྲག་གིས་ཀུན་དུ་བསྡུ་བ་གསུངས་པ། སྤྱོད་པ་དག་ནི་ཚད་ཡོད་མ་གྱུར་ཅིག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 73 [HEADING]]
### སྨོན་ལམ་གྱི་མཐའ། ^1-9-0

[Block 74]
དེ་ལ་སྨོན་ལམ་གྱི་མཐའ་མེད་པའི་དཔེ་ནི་རྣམ་པ་བཞིར་གསུངས་ཏེ། ནམ་མཁའི་མཐར་ཐུག་གྱུར་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 75 [HEADING]]
### སྨོན་ལམ་གྱི་ལེགས་པ། ^1-10-0
--- END BLOCKS ---
