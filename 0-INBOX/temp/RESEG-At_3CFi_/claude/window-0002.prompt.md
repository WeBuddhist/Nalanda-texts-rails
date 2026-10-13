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
དེ་གང་གི་ཡུལ་ཡིན་ཞེ་ན། རྣལ་འབྱོར་ཐུབ་མཆོག་མ་ལུས༌[^17]རྣམ་པར་རོལ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རྣལ་འབྱོར་པ་ཐུབ་པས་སངས་རྒྱས་ཀྱི་སྲས་བླ་མ་དམ་པ་ཉེ་བར་བསྟེན་པ་ཚོགས་བསགས་པ་སྐལ་བ་དང་ལྡན་པ་རྣམས་ཀྱིས་ཤེས་རབ་ཀྱི་མིག་གིས་ཡུལ་དུ་མཐོང་ཞིང་། དབང་པོ་བཞིས་ངེས་པའི་ཚུལ་གྱིས་རོལ་པའོ། །

[Block 72]
དེའི་ཕྱིར་དེ་ནི་བཙུན་མོ་བདག་མེད་མ་ཞེས་བྱའོ། །

[Block 73]
དེ་ལྟ་བུའི་རང་བཞིན་བདག་མེད་མ་དེ༌[^18]དང་རོལ་པས། ལས་དང་ཉོན་མོངས་པའི་སྐྱེ་བ་ལ་སོགས་པ་རྩད་ནས་གཅོད་པ་ཡང་ཡིན་ལ། རང་བཞིན་གྱིས་འགོག་པ་མངོན་དུ་བྱ་རྒྱུ་ཡང་ཡིན་མོད་ཀྱི། འོན་ཀྱང་བྱམས་པ་དང་སྙིང་རྗེས་འཕངས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་རང་གི་རྒྱུད་ལ་ཟག་མེད་ཀྱི་ཡོན་ཏན་མ་ལུས་པ་རྫོགས་པར་མ་བྱས། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་མ་བྱས། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་མ་བྱས་པར་བར་མ་དོར་ཡང་དག་པའི་མཐའ༌[^19]མངོན་དུ་བྱས་ན་ཉན་ཐོས་དང་རང་རྒྱལ་བར་ལྟུང་བས། དེའི་ཕྱིར་བཟོད་པ་དེ་དང་ལྡན་བཞིན་དུ་དགེ་བའི་ཆོས་མཐའ་དག་རྫོགས་པར་བྱ་དགོས་པར་བསྟན་པའི་ཕྱིར།

[Block 74 [VERSE]]
ཆགས་མེད་བྱམས་དང་སྙིང་རྗེ་ལས་བྱུང་བ།[^20] །
བྱང་ཆུབ་སྨོན་པའི་སེམས་ནི་ལེགས་བརྟན་བྱེད། །

[Block 75]
ཅེས་པ་ལ་ཆགས་པ་མེད་པ་ནི་སྒྱུ་མ་མཁན་ལྟར་རང་བཞིན་ཤེས་པས་མ་ཞེན་པའོ། །

[Block 76]
བྱམས་པ་དང༌[^21]སྙིང་རྗེས་འཕངས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ནི་གོ་བར་ཟད་དོ། །

[Block 77]
དེ་ལ་འདིར་རིམ་པ་ནི་འདི་ཡིན་ཏེ། རྣལ་འབྱོར་པས་ཐོག་མར་མལ་ནས་ལངས་ནས། ཐོག་མ་མེད་པ་ནས་ཡིད་ཀྱི་རང་བཞིན་གྱི་ལུས་ལ་བདག་དང་བདག་གིར་མ་གྲུབ་བཞིན་དུ་དེར་བརྟགས༌[^22]པས་རྟོག་པར་བལྟས་པའི་དབང་གིས་རྟོག་པའི་རྒྱུན་ལ་སྡུག་བསྔལ་གྱི་མེ་འབར་བ་རྣམས་ལ་བལྟས་ཏེ། སྐྱེ་བའི་བརྒྱུད་པ་ལ་གྲངས་མེད་པས་སེམས་ཅན་འདི་གཅིག་གིས་ཀྱང་མ་ལྟ་བུ་བྱས་པའི་གྲངས་མི་ཆོད་པས་འཁོར་བ་མཐའ་དག་ན་གནས་པའི་འགྲོ་བ་རྣམས་གདོན་པའི་བསམ་པས་དང་པོར་བྱམས་པ་དང་སྙིང་རྗེ་ཡིད་ལ་བྱ། དེ་ནས་དེ་རྣམས་ཀྱི་ཆེད་དུ་དཔལ་ཧེ་རུ་ཀ་འདོད་པའི་སྨོན་པ་བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པར་བྱ། དེ་ནས་ཆོས་ཐམས་ཅད་སེམས་རླུང་གི་རྣམ་འཕྲུལ་ཡིན་པའི་ཕྱིར། སེམས་ལས་གཞན་པའི་དོན་མེད་པར་བསམས་ལ། རླུང་སེམས་ཙམ་ལ་ལྷའི་སྐུང་བསམ་པ་ནི་བདག་བྱིན་གྱིས་བརླབ་པ་ཀུན་རྫོབ་ཀྱི་བདེན་པའོ། །

[Block 78]
དེ་ནས་སྔར་གྱི་བདེ་བ་དང་དྲན་པའི་ཐབས་ཀྱིས་སེམས་རླུང་རྩ་དབུ་མར་བཅུག་ལ་སྟོང་པ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་བདེ་བ་དང་བཅས་པ་བསྒོམ་པར་བྱའོ། །

[Block 79]
དེ་ནས་སེམས་ཀྱི་རང་བཞིན་ལ་ཞུགས་པར་བསམས༌[^23]ལ་དེའི་ཚེ་དེའི་མཚན་ཉིད་འོད་གསལ་བ་སྣང་བ་མེད་པའོ། །

[Block 80]
ནམ་མཁའི་དཀྱིལ་ལྟ་བུ་ལ་ཤེས་རབ་ཀྱི་མིག་གིས་བལྟ། དྲན་པས་མ་ཡེངས་པར་བལྟ། དད་པས་ཡིད་ཆེས་པར་བྱས་ལ་བལྟ། བརྩོན་འགྲུས་ཀྱིས་འཇིག་རྟེན་པའི་སེམས་མེད་པར་བྱས་ལ་བལྟ། ཏིང་ངེ་འཛིན་གྱིས་རྩེ་གཅིག་པའི་ཚུལ་གྱིས་བལྟས་པས་སེམས་ཀྱི་རང་བཞིན་འོད་གསལ་བ་དེ་སྣང་བ་མེད་པ་གསལ་བ་དང་བ་དག་པར་སྣང་བ་དེ་ལ་བརྟེན་ནས་ངེས་པའི་ཤེས་པ་སྐྱེའོ། །

[Block 81]
དྲན་པས་མ་ཡེངས་པར་བལྟ་བའི་དཔེ་ནི་ཡུངས་ཀར་བརྩེགས་པ་ལག་ཏུ་བསྐུར་བའི་སྐྱེས་བུ་ལྟ་བུའོ། །

[Block 82]
དད་པས་ཡིད་ཆེས་པའི་དཔེ་ནི་གཞོན་ནུ་མས་འདོད་པ་མྱོང་བ་ལྟ་བུའོ། །

[Block 83]
བརྩོན་པའི་དཔེ་ནི་རྒྱལ་པོའི་སྒོ་སྲུང་བ་ལྟ་བུའོ། །

[Block 84]
ཏིང་ངེ་འཛིན་གྱི་དཔེ་ནི་རླུང་མེད་པའི་མར་མེ་དང་འདྲ་བར་བལྟའོ། །ཤེས་རབ་ཀྱི་ངེས་པའི་དཔེ་ནི་སྔར་འདྲིས་པའི་མི་མཐོང་བ་བཞིན་ནོ། །

[Block 85]
དཔེ་འདི་རྣམས་ཀྱི་གཏམ་རྒྱུད་ནི་གཞུང་མངས་པའི་འཇིགས་པས་མ་བྲིས་སོ། །

[Block 86]
དེ་ལྟར་ཇི་ཙམ་སེམས་གནས་པར་ནུས་པ་དེ་སྲིད་དུ་གནས་ལ། དེ་ནས་དེའི་ངང་ལ་སྐད་ཅིག་གིས་སྒྱུ་མ་ལྟ་བུའི་ལྷའི་སྐུར་ལངས་ལ་དངོས་པོ་ཐམས་ཅད་ཆུ་ཟླ་ལྟ་བུར་སྒྲོ་སྐུར་དང་བྲལ་བ་སྣང་བ་ཙམ་གྱི་མཚན་ཉིད་དུ་བསམས་ལ། བྱམས་པ་དང་སྙིང་རྗེ་དང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་འཕངས་པའི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཆུ་ཟླ་ལྟར་སྒྲོ་སྐུར་དང་བྲལ་བའི་ཚུལ་གྱིས་ཡོངས་སུ་རྫོགས་པར་བྱའོ། །

[Block 87]
དེ་ལྟར་ན་ཐབས་ཤེས་རབ་དང་། སྙིང་རྗེ་དང་། ཤེས་རབ་དབྱེར་མེད་པའི་ཚུལ་གྱིས་དགེ་བའི་ཆོས་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱ་སྟེ་དེ་ལྟར་མ་ཡིན་ན་ཉན་ཐོས་ལ་སོགས་པར་ལྟུང་ངོ་། །དེའི་ཕྱིར་མདོ་ལས།

[Block 88]
ཐབས་མེད་ཤེས་རབ་བྲལ་བས་ཉན་ཐོས་ཉིད་དུ་ལྟུང་། །ཞེས་པས་སོ། །

[Block 89]
དེ་ལ་ཐབས་གང་ཞེ་ན། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་འཕངས་ནས་དགེ་བའི་ཆོས་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱེད་པའོ། །ཤེས་རབ་གང་ཞེ་ན་དེའི༌[^24]ཞེན་པ་དང་སྤྲོས་པ་གཅོད་པའོ། །

[Block 90]
དེ་བས་ན་ཐབས་དེ་མེད་ན་ཤེས་རབ་དེ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 91]
དེ་བཞིན་དུ་ཐེག་པ་ཆེན་པོའི་མདོ་གཞན་ལས་ཀྱང་། ཐབས་ཀྱིས༌[^25]དགེ་བའི་ཆོས་ཐམས་ཅད་སྡུད་པ་ཡིན་ལ། ཤེས་རབ་ཀྱིས་འབྱེད་པའོ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 92]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པ་ནི་མཐའ་གཉིས་ལ་མི་གནས་པར་འགྲོ་བས་དེའི་ཕྱིར།

[Block 93 [VERSE]]
རང་བཞིན་གོམས་པའི་ཡིད་ནི་གར་མི་གནས། །
འདི་དེ་ཉིད་ནི་བླ་མེད་བྱང་ཆུབ་ལམ། །

[Block 94]
ཞེས་བྱའོ། །

[Block 95]
ད་ནི་ཤེས་རབ་ཀྱི་མིག་གིས་ལྟ་བའི༌[^26]ཡུལ་གཞན་བསྟན་པའི་ཕྱིར། རབ་རིབ་ཅན་ནི་མཁའ་ལ་སྐྲ་མཐོང་སྨྲ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་

[Block 96 [HEADING]]
## དེས་བལྟ་བའི་ཡུལ། ^4-0

[Block 97]
དེས་བལྟ་བའི་ཡུལ་གཉིས་ཏེ་མེད་པ་དང་ཡོད་པའོ། །

[Block 98 [HEADING]]
### མེད་པ་མཐོང་བ། ^4-1-0

[Block 99]
མེད་པ་མཐོང་བ་ནི་ཚུ་རོལ་མཐོང་བའི་ཤེས་པ་དང་། ཤེས་བྱ་མ་ལུས་པ་སྟེ་མེད་པ་མཐོང་བ་དཔེར་ན༌[^27]རབ་རིབ་ཅན་གྱི་སྐྲ་ལ་སོགས་པ་དང་འདྲ་བར་ཤེས་པའོ། །

[Block 100 [HEADING]]
### ཡོད་པའི་རང་བཞིན་མཐོང་བ། ^4-2-0

[Block 101]
ཡོད་པའི་རང་བཞིན་མཐོང་བ་ལ་གཉིས་ཏེ་རྟེན་འོད་གསལ་དང་། བརྟེན་པ་ཟག་མེད་ཀྱི་ཡོན་ཏན་མཐོང་བའོ། །

[Block 102 [HEADING]]
#### རྟེན་འོད་གསལ། ^4-2-1-0

[Block 103]
འོད་གསལ་ཇི་ལྟར་མཐོང་ཞེ་ན། སྐྱེ་བ་མེད་པ་རྣམ་པ་མེད་པར་མཐོང་བས་དེའི་ཕྱིར། སྐྱེ་མེད་གནས་མེད་འགྲོ་ཀུན་ཡང་དག་པར། །ཞེས་བྱའོ། །

[Block 104 [HEADING]]
#### བརྟེན་པ་ཟག་མེད་ཀྱི་ཡོན་ཏན་མཐོང་བ། ^4-2-2-0

[Block 105]
ཟག་མེད་ཀྱི་ཡོན་ཏན་ཇི་ལྟར་མཐོང་ཞེ་ན། སྒྱུ་མ་དང་རྨི་ལམ་དང་། མིག་འཕྲུལ་དང་། ཆུ་ཟླ་ལྟར་སྒྲོ་སྐུར་དང་བྲལ་བ་སྣང་བ་ཙམ་མྱོང་བ་ཙམ་གྱིས་རང་བཞིན་དུ་མཐོང་བའོ། །

[Block 106]
དེའི་ཕྱིར། མིག་འཕྲུལ༌[^28]ཇི་བཞིན་ངེས་པར་ཡོངས་སུ་སྣང་། །ཞེས་བྱའོ། །

[Block 107]
ད་ནི་ཞར་ལ་འོངས་པའི་བརྟགས༌[^29]པའི་རྣལ་འབྱོར་དགག་པའི་ཕྱིར། བརྟགས་པའི་སྤྲོས་པས་བསྐྱེད་ལ་མ་ཆགས་ཤིག །ཅེས་བྱ་བ་ལ། བརྟགས་པའི་སྤྲོས་པ་ནི་ཐིག་ལེ་དང་ཕྲ་མོ་ལ་སོགས་པའོ། །

[Block 108]
མ་ཆགས་པ་ནི་དེ་ལ་བརྟེན་ནས་སེམས་གནས་པ་ཕྲ་མོ་ཡོད་ཀྱང་ལམ་གྱི་མཚན་ཉིད་མ་ཚང་བས་བྱང་ཆུབ་ཀྱི་ལམ་མ་ཡིན་པས་དགག་པའོ། །

[Block 109]
དེ་ཉིད་འཁོར་བའི་འཁྲུལ་འཁོར་གཅོད་པའི་ལམ་མ་ཡིན་པས་འཁོར་བའི་རྒྱུར་བསྟན་པ་ནི།

[Block 110 [VERSE]]
སྣ་ཚོགས་རྣམ་རྟོག་ལས་གཞན་འཆིང་བ་མེད། །
དེ་ལ་སྐྱེ་འཆི་འཁོར་བ་གཞན་མ་ཡིན། །
--- END BLOCKS ---
