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
## ༄༅། །སྦྱོར་བ་ཡན་ལག་དྲུག་པ་ཞེས་བྱ་བའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཥཊ་ཨཾ་ག་ཡོ་ག་ནཱ་མ་ཊཱི་ཀ །བོད་སྐད་དུ། སྦྱོར་བ་ཡན་ལག་དྲུག་པ་ཞེས་བྱ་བའི་འགྲེལ་པ། དཔལ་རྡོ་རྗེ་སེམས་དཔའ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## སོ་སོར་སྡུད་པ། ^1-0

[Block 5]
དབང་པོ་རྣམས་དང་དབང་པོ་རྣམས་ཀྱི་ཡུལ་གཉི་གའི་དབང་པོ་སྟེ། དབང་པོ་བཅུ་པོ་ཡུལ་དང་ཡུལ་ཅན་དེ༌[^1]རྣམས་ཀྱི་རང་གི་འཇུག་པ་ནི། ཇི་ལྟར་རང་ཉིད་ཀྱི་གཟུང་བ་དང་། འཛིན་པའི་རང་བཞིན་གྱིས་འཇུག་པ་ནི་རང་གི་འཇུག་པའོ། །

[Block 6]
དེར་གནས་པས་ན༌[^2]རང་གི་འཇུག་པ༌[^3]གནས་སོ། །

[Block 7]
ཐམས་ཅད་དུ་དམན་པ་དང་། བར་མ་དང་།

[Block 8 [VERSE]]
མཆོག་གི་བྱེ་བྲག་གིས་སོ། །
འདོད་པ་སོ་སོར་སྡུད་པས་ན། །

[Block 9]
ཞེས་བྱ་བ་ནི་འདོད་ཅིང་ཆགས་པར་བྱ་བ་ཡིན་པས་ན། འདོད་པ་སྟེ་གཟུགས་ལ་སོགས་པའོ། །

[Block 10]
དེ་རྣམས་ལ་ནི་དབང་པོ་རྣམས་ཀྱིས་གང་སོ་སོར་ཡང་དང་ཡང་དུ་སྡུད་ཅིང་ལེན་པས་ན༌[^4]སྡུད་པ་ཞེས་བྱ་སྟེ། ཡན་ལག་དང་པོའི་བཤད་པའོ། །

[Block 11 [HEADING]]
## བསམ་གཏན། ^2-0

[Block 12]
སོ་སོར་སྡུད་པ་རྣམ་པར་སྦྱང་བར་བྱ་བའི་དོན་དུ་ཡན་ལག་གཉིས་པ་བསྟན་པའི་ཕྱིར་འདོད་པ་ལྔ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདོད་པ་ལྔ་ནི་དབང་པོ་ལྔའི་ཡུལ་དུ་གྱུར་པ་གཟུགས་ལ་སོགས་པ་ནི་མདོར་བསྡུས་ནས་ཏེ། དབང་པོ་རྣམས་དང་གཅིག་ཏུ་གྱུར་ནས་སོ། །

[Block 13]
སངས་རྒྱས་ལྔ་ནི་མིག་ལ་སོགས་པ་སྟེ། དེ་རྣམས་ཀྱི་སྦྱོར་བ་ནི་ཡང་དག་པར་སྦྱོར་བས་སངས་རྒྱས་ལྔ་རུ་སྦྱོར་བ་ཡིན༌[^5]ཏེ། དེ་བས་ན་གཟུགས་ལ་སོགས་པ་རྣམས་ཀྱང་སངས་རྒྱས་ཡིན་ནོ། །

[Block 14]
དེ་ལྟར་གྱུར་པའི་ཡོངས་སུ་དག་པའི་བརྟག་པ་དེ་ཉིད་བསམ་གཏན་ཞེས་བཤད་དོ། །

[Block 15]
དེ་ཡང་རྟོག་པ་ལ་སོགས་པའི་དབྱེ་བས་རྣམ་པ་ལྔར་འགྱུར་ཏེ། རྟོག་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དེའི་དབྱེ་བ་བཤད་པའོ། །

[Block 16]
དབང་པོ་དང་། ཡུལ་དང་། དབང་པོའི་ཤེས་པ་ནི་གསང་བ་གསུམ་སྟེ། དབང་པོ་ལྔ་དང་། དབང་པོའི་ཤེས་པ་དང་། དེའི་ཡུལ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པ་རྣམ་པ་ལྔའི་བདག་ཉིད་ཡིན་ནོ་ཞེས་གང་རྟོག་པ་དེ་ནི་རྟོག་པའོ། །

[Block 17]
དེ་ཉིད་ལ་རྣམ་པར་དཔྱོད་པ་ནི་གནས་པ་ལ་སྤྱོད༌[^6]པའོ། །

[Block 18]
དེ་ལྟར་དཔྱད་ནས་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པ་ལ་མངོན་པར་ཕྱོགས་པས་གང་ཡིད་ལ༌[^7]བདེ་བའི་མཚན་ཉིད་ཅན་དེ་ཉིད༌[^8]དགའ་བ་ལ་རེག་པའོ། །

[Block 19]
དེ་ཁོ་ན་ཉིད་ལ་མངོན་པར་ཞུགས་པས་ལུས་ཤིན་ཏུ་སྦྱངས་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་གྱི་བདེ་བ་གང་ཐོབ་པ་དེ་ནི་བདེ་བས་བསྡུས་པའོ། །

[Block 20]
དེ་ལྟར་སྦྱངས་པ་ལས་རབ་ཀྱི་མཐར་ཐུག་པར་སོན་པའི་ཕྱིར་ཤེས་པ་སྟེ། མིག་ལ་སོགས་པ་དྲུག་གི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་དང་ཤེས་བྱ་སྟེ། གཟུགས་ལ་སོགས་པ་ནས་ཆོས་ཀྱི་ཁམས་ཀྱི་བར་དུ་འབྱུང་བ་ནི་ཤེས་པ་དང་ཤེས༌[^9]བྱ་བྱུང་བའོ། །

[Block 21]
དེའི་ཟད་པ་ནི་སེམས་ཀྱི་གཟུང་བ་དང་འཛིན་པ་སྟོང་པ་ཉིད་དེ། དེ་བས་ན་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་ཅན་གྱི་སེམས་རྩེ་གཅིག་པ་ལ་ནི་རང་སེམས་ཞེས་བྱའོ། །

[Block 22]
དེ་ལྟ་བུའི་སེམས་དེ་ནི་སངས་རྒྱས་ཀུན་དངོས་ཞི་བ་སྟེ། སྣང་བ་ཙམ་དང་ཐམས་ཅད་སྟོང་པར་གཅིག་ཏུ་མཐར་ཐུག་པར་འབྱུང་བར་འགྱུར་ཏེ། ཡན་ལག་གཉིས་པའི་དབྱེ་བ་རྣམ་པ་ལྔའོ། །

[Block 23 [HEADING]]
## སྲོག་དང་རྩོལ་བ། ^3-0

[Block 24]
ཡེ་ཤེས་ལྔའི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཡེ་ཤེས་ལྔའི་རང་བཞིན་གྱིས་དབུགས་ཏེ། ཡང་དེ་ཉིད་ས་ལ་སོགས་པའི་བདག་ཉིད་དུ་རང་གི་རྡོ་རྗེའི༌[^10]བུ་ག་ནས་བྱུང་ནས་པདྨའི་སྣའི་རྩེ་མོར་གོང་བུའི་གཟུགས་ཀྱིས་ཏེ། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེའི་གཟུགས་ཀྱིས་བསྒོམ་པར་བྱའོ། །

[Block 25]
དེ་ཉིད་གྱེན་དུ་འགྲོ་བའི་དབུགས་ནི་ཁ་དོག་སྣ་ལྔ་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་ལྔའི་བདག་ཉིད་ཅན་ནོ། །

[Block 26]
དེ་ཉིད་ཀྱིས་ན་རིན་པོ་ཆེའོ། །

[Block 27]
སྲོག་ནི་འཚོ་བའོ། །

[Block 28]
རྩོལ་ཞིང་རིང་དུ་སྤྲོས་པ་གང་ཡིན་པ་དེ་ནི་སྲོག་དང་རྩོལ་བ་ཞེས་བྱར་བཤད་ཅེས་བྱ༌[^11]བ་སྟེ། དེ་ཉིད་དུ་འཇུག་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཉིན་དང་མཚན་དུ་ཟློས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 29]
རང་སྔགས་སྙིང་གར་བསམས༌[^12]ཏེ། རང་གི་སྙིང་གར་བསམས་ཏེ། རང་གི་སྙིང་གའི་པདྨ་ལ་བསམས་ནས། སྲོག་ནི་ཐིག་ལེར་གྱུར་པར་བཞག །ཅེས་བྱ་བ་མི་ཤིགས་པ༌[^13]གཏོགས་པར་དགོད་པ་སྟེ་ཡན་ལག་གསུམ་པའོ། །

[Block 30 [HEADING]]
## འཛིན་པ། ^4-0

[Block 31]
རང་གི་གཟུགས་ལ་སོགས་པའོ། །

[Block 32]
དབང་པོ་ནི་མིག་ལ་སོགས་པ་སྟེ། དེ་ལ་དབང་པོ་གཉིས་དགག་ཅིང་ངེས་པར་ཐིམ་ནས་དེའི་འོག་ཏུ་ཡུལ་དང་དབང་པོའི་རྟེན་དུ་གྱུར་པའི་རིན་པོ་ཆེ་སྟེ། སེམས་ཀྱི་རིན་པོ་ཆེ་སྲོག་དང་རྩོལ་བ་དང་བཅས་པར་བཀག་ཅིང་ནུབ་པར་གྱུར་པའི་གཟུང་བ་གང་ཡིན་པ་དེ་འཛིན་པ་ཡིན༌[^14]པར་བཤད་དེ། དེ་ཡང་གང་ཞེ་ན། ཡང་དག་པའི་མཐའ་ཞེས་བྱ་བ་སྟེ།

[Block 33 [VERSE]]
སེམས་ནི་འགོག་པའི་རྡོ་རྗེར་འགྱུར། །
མཚན་མ༌[^15]ཉེར་འཛིན་འབྱུང་བར་འགྱུར། །

[Block 34]
ཞེས་བྱ་བ་ལ། འགོག་པའི་རྡོ་རྗེ་ནི་འོད་གསལ་བའོ། །

[Block 35]
དེར་གྱུར་པ་ནི་སེམས་དེར་གྱུར་པའོ། །

[Block 36]
མཚན་མ་རྣམས་ཀྱི་ཉེ་བར་འཛིན་པ་ན༌[^16]མཚན་མར་ཉེར་འཛིན་ཏེ། མཚན་མར་སྣང་བའོ། །

[Block 37]
འབྱུང་བར་གྱུར་པ་ནི་སྐྱེ་བར་གྱུར་པའོ། །

[Block 38 [VERSE]]
མཚན་མའི་ཁམས་ནི་རྣམ་པ་ལྔར། །
བྱང་ཆུབ་རྡོ་རྗེ༌[^17]གསུངས་པ་ཡིན། །

[Block 39]
ཞེས་བྱ་བ་ནི་ས་ཆུ་ལ་ཐིམ་པར་གྱུར་པ་ལས་སྨིག་རྒྱུ་དང་འདྲ་བར་སྣང་བར་གྱུར་པ་ནི་མཚན་མ་དང་པོའོ། །

[Block 40]
དེ་བཞིན་དུ་ཆུ་མེ་ལ་ཐིམ་པར་གྱུར་པ་ལས་དུ་བ་ལྟ་བུ་སྟེ་གཉིས་པའོ། །
--- END BLOCKS ---
