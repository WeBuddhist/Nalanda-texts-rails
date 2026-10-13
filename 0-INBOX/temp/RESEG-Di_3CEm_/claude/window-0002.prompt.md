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

[Block 76]
སྨོན་ལམ་གྱི་ལེགས་པ་ནི་ཡོན་ཏན་རྣམ་པ་གཉིས་ཏེ། ཚེ་འདི་དང་། ཕྱི་མའོ།[^23] །

[Block 77 [HEADING]]
#### ཚེ་འདིའི་ལེགས་པ། ^1-10-1-0

[Block 78]
དེ་ལ་ཚེ་འདིའི་རྣམ་པ་བཞི་ནི་འདི་ལྟ་སྟེ། བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་གཟུང་བ༌[^24]དང་། དེ་བཞིན་གཤེགས་པ་མཐོང་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་སྐལ་བ་མཉམ་པ་རྙེད་པ་དང་། ལས་ཀྱི་སྒྲིབ་པ་ཡོངས་སུ་ཟད་པའོ། །

[Block 79]
དེ་ལ་མང་པོ་དང་། རྒྱ་ཆེ་བ་དང་། སྣ་ཚོགས་པ་དང་། རྗེས་སུ་གཟུང་བ་དང་། དངོས་པོ་དང་། ཞིང་དམ་པའི་བསོད་ནམས་ཀྱི་དཔེ་དང་། བྱང་ཆུབ་འདོད་པ་དང་། སྨོན་ལམ་ལ་མོས་པས་བསོད་ནམས་ཀྱི་མཆོག་དམ་པ་ཡོངས་སུ་འཛིན་པར་གསུངས་པ་སྟེ། གང་ཡང་ཕྱོགས་བཅུའི་ཞིང་རྣམས་མཐའ་ཡས་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 80]
ངན་སོང་དང་ལོག་པའི་གྲོགས་པོ་ཡོངས་སུ་སྤངས་པས་དེ་བཞིན་གཤེགས་པ་མཐོང་བར་འགྱུར་ཏེ། དེས་ནི་ངན་སོང་ཐམས་ཅད་སྤང་བར༌[^25]འགྱུར། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 81]
རབ་ཏུ་བསྔགས་པ་རྙེད་པ་འཚོ་བའི་ཚེ་འཐོབ་པས་བྱང་ཆུབ་སེམས་དཔའ་དང་སྐལ་བ༌[^26]མཉམ་པ་རྙེད་པར་གསུངས་ཏེ། དེ་དག་རྙེད་པ་རབ་རྙེད་བདེ་བར་འཚོ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 82]
ལས་ཀྱི་སྒྲིབ་པ་ཡོངས་སུ་ཟད་པའི་ཡོན་ཏན་ལེགས་པ་བཞི་པ་ནི་གང་གསུངས་པ། མཚམས་མེད་ལྔ་པོ་དག་གི་སྡིག་པ་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 83 [HEADING]]
#### ཕྱི་མའི་ལེགས་པ། ^1-10-2-0

[Block 84]
ཕྱི་མའི་ཡང་རྣམ་པ་གཉིས་ཏེ། རྒྱུས་བསྡུས་པ་དང་། འབྲས་བུས་བསྡུས་པའོ། །

[Block 85]
དེ་ལ་རྒྱུས་བསྡུས་པ་ནི། །ཡེ་ཤེས་དང་མཚན་དང་དཔེ་བྱད་བཟང་པོའི་ལུས་དང་ནད་མེད་པའི་ལུས་ཀྱི་མཚན་ཉིད་དུ་གང་གསུངས་པ། ཡེ་ཤེས་དང་ནི་གཟུགས་དང་མཚན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 86]
འབྲས་བུས་བསྡུས་པ་ནི་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་འགྲོ་བ་དང་། སེང་གེའི་ཁྲི་ལ་འདུག་པར་སྟོན་པ་དང་། བདུད་རྣམས་རབ་ཏུ་ཕམ་པ་དང་། མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ལ་སོགས་པའི་མཚན་ཉིད་དུ་གསུངས་པ། བྱང་ཆུབ་ཤིང་དབང་དྲུང་དུ་དེ་མྱུར་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 87]
མདོར་ན་འཇིག་རྟེན་གྱི་དང་འཇིག་རྟེན་ལས་འདས་པའི་སྦྱོར་བ་ཐོབ་པ་ནི་ལེགས་པའོ། །

[Block 88]
གང་ཡང་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་འདི། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 89 [HEADING]]
### བསྔོ་བ་གསུམ། ^1-11-0

[Block 90]
འདི་མན་ཆད་ཀྱི་བསྔོ་བ་གསུམ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་བཞིན་གཤེགས་པས་གསུངས་པའི་སྒྲིབ་པ་མེད་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མཐུན་པའི་ལུས་འཛིན་ཅིང་སྨོན་ལམ་ཡོངས་སུ་རྫོགས་པས་འཇིག་རྟེན་ན་གནས་ཏེ་སེམས་ཅན་གྱིས༌[^27]དོན་སྒྲུབ་པར་གསུངས་པ། འཇམ་དཔལ་ཇི་ལྟར་མཁྱེན་ཅིང་དཔའ་བ་ཞེས་བྱ་བ་ནས་བཟུང་སྟེ། འཇིག་རྟེན་ཇི་སྲིད་སེམས་ཅན་ཕན་པར་བགྱི། །ཞེས་བྱ་བའི་བར་རྣམས་སོ། །

[Block 91]
ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་གྱི་དོན་ཀུན་བསྡུས་པ་རྫོགས་སོ།། །།

[Block 92 [HEADING]]
## འཕགས་པ་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་རྒྱལ་པོའི་བཤད་པ། ^2-0

[Block 93]
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 94]
བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་བསྡུས་པའི་དོན་ནི་རྣམ་པ་བཅུའོ། །

[Block 95]
འདི་ལྟ་སྟེ། དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ་དང་། དེ་ལ་མཆོད་པ་དང་། སྡིག་པ་བཤགས་པ་དང་། བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་བསྐུལ་བ་དང་། དེ་བཞིན་གཤེགས་པ་བཞུགས་པར་གསོལ་བ་དང་། དགེ་བའི་རྩ་བ་ཡོངས་སུ་བསྔོ་བ་དང་། དེའི་རབ་ཏུ་དབྱེ་བ་དང་། དེའི་མཐའ་དང་། དེ་དག་གི་ལེགས་པ་རྣམས་སོ། །

[Block 96 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ། ^2-1-0

[Block 97]
དེ་ལ་མི་དབྱེ་བའི་སྤྱིས་ནི་ཕྱོགས་བཅུའི་དུས་གསུམ་གྱི་ཞིང་ཐམས་ཅད་ཀྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ལ་ལུས་དང་ངག་དང་ཡིད་ཀྱིས་ཕྱག་བྱ་བའི་ཕྱིར། ཇི་སྙེད་སུ་དག་ཅེས་བྱ་བ་ལ་སོགས་པ་བཤད་དོ། །

[Block 98]
ཇི་སྙེད་ཅེས་བྱ་བ་ནི་གྲངས་ཇི་ཙམ་པའི་ཚད་དེ། དེ་དག་གི་ཚད་ཆད་པར་མ་གྱུར་པས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་སྤྱིར་བསྟན་པའི་ཕྱིར། སུ་དག་ཅེས་བྱ་བ་བཤད་དེ། གྲངས་ཆད་པ་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 99]
ཕྱོགས་བཅུ་ཞེས་བྱ་བ་ནི་ཕྱོགས་བཅུའོ། །

[Block 100]
འཇིག་རྟེན་གྱི༌[^28]ཞེས་བྱ་བ་ནི་འགྲོ་བ་རྣམས་སོ། །

[Block 101]
དུས་གསུམ་གཤེགས་པ་ཞེས་བྱ་བ་ནི་དུས་གསུམ་གྱི༌[^29]ཀུན་ཆུབ་པས་ཏེ། དུས་གསུམ་གྱི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 102]
མི་ཡི་སེང་གེ་ཞེས་བྱ་བ་ལ་སེང་གེ་ནི་ཐམས་ཅད་དུ་བག་བརྐྱང་ཞིང་གར་ཡང་དོགས་པ༌[^30]མེད་ལ། དེ་དང་འདྲ་བ་ལྷར་བཅས་པའི་འཇིག་རྟེན་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སེང་གེ་དང་ཡང་འདྲ་ལ། མི་ཡི་ཚེ་ཡང་སྟོན་པའི་ཕྱིར་མི་ཡང་ཡིན་ལ་སེང་གེ་ཡང་ཡིན་པས་མིའི་སེང་གེའོ། །

[Block 103]
བདག་གི༌[^31]མ་ལུས་དེ་དག་ཐམས་ཅད་ལ། །ཞེས་བྱ་བ་ལ་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཕྱོགས་གཅིག་ཏུ་ཡང་བརྗོད་དུ་རུང་བས་ན་འདིར་ནི་མ་ལུས་ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 104]
ལུས་དང་ངག་ཡིད་དང་བས་ཕྱག་བགྱིའོ། །ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་དང་བ་བསྐྱེད་པ་སྟེ། སེམས་དང་བ་དེས་བསྐྱེད་པས་ན་ལུས་དང་ངག་ཀྱང་དང་བའོ། །

[Block 105]
ད་ནི་ལུས་ལ་སོགས་པས་ཕྱག་བྱ་བ་སོ་སོར་ཕྱེ་སྟེ་བཤད་དོ། །

[Block 106 [HEADING]]
#### ལུས་ཀྱི་ཕྱག་བྱ་བ། ^2-1-1-0

[Block 107]
དེ་ལ་ལུས་ཀྱི་ཕྱག་བྱ་བ་ནི། ཞིང་གི་རྡུལ་སྙེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི་ལུས་ཀྱིས་ཕྱག་བྱ་བའོ། །

[Block 108]
སྙེད་ཅེས་བྱ་བ་ནི་དཔེའི་རྣམ་གྲངས་ཏེ། ཕྱོགས་བཅུ་དུས་གསུམ་དུ་གཤེགས་པའོ༌[^32]སངས་རྒྱས་ཀྱི་ཞིང་ཇི་སྙེད་ཀྱི་ལུས་རབ་ཏུ་བཏུད་པས་ཕྱག་བྱ་བའོ། །

[Block 109]
རྒྱལ་བ་ཀུན་ལ་རབ་ཏུ་ཕྱག་འཚལ་ལོ། །ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་དགྲ་དང་བདུད་ལས་རྒྱལ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་རྒྱལ་བ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ།

[Block 110 [VERSE]]
སྡིག་པའི་ཆོས་རྣམས་ལས་རྒྱལ་བས། །
ཉེར་འགྲོ་ང་ནི་རྒྱལ་བ་ཡིན། །
--- END BLOCKS ---
