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

[Block 41]
མེ་རླུང་ལ་ཐིམ་པར་གྱུར་པ་ལས།

[Block 42]
ནམ་མཁའ་སྣང་བར་གྱུར་པ༌[^18]ལྟ་བུ་སྟེ་གསུམ་པའོ། །

[Block 43]
ཁམས་ཕྲ་བ་ཀུན་དུ་སྣང་བ་གསུམ་དུ་སོང་བ་ལས་མར་མེ་ལྟར་སྣང་བའི་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་ནི་བཞི་པའོ། །

[Block 44]
རང་བཞིན་ཀུན་དུ་སྣང་བ་ལ་ཐིམ་པར་གྱུར་པ་ལས་སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་ཞིང་རྟག་ཏུ་སྣང་བ་འོད་གསལ་བ་ཙམ་དུ་གྱུར་པ་ནི་ལྔ་པའོ། །

[Block 45]
མཚན་མ༌[^19]ལྔ་པོ་དེ་དག་གིས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 46]
དེ་ཡང་ཇི་སྐད་དུ་ལས་ཀྱི་མཐའ་རྣམ་པར་འབྱེད་པ་ལས།

[Block 47 [VERSE]]
དང་པོ་ས་ནི་ཆུ་ལ་ཐིམ། །
ཆུ་ཡང་མེ་ལ་ཐིམ་པར་གྱུར། །
མེ་ནི་རླུང་ལ་ཐིམ་འགྱུར་ཞིང་། །
རླུང་ཡང་རྣམ་པར་ཤེས་ལ་འཇུག །

[Block 48 [VERSE]]
རྣམ་ཤེས་གཟུང་བ་དེ་ཉིད་ནི། །
འོད་གསལ་པར་ཡང་འཇུག་པ་ཡིན། །

[Block 49]
ཞེས་གསུངས་པས་སོ། །

[Block 50]
བརྟན་པར་གྱུར་ཅིང་རྣམ་པར་དག་པར་གྱུར་ནས། རྡོ་རྗེའི་ལམ་ནས་འདའ༌[^20]བར་མི་བྱ་བའི་མཚན་མ་ལྔའི་རིམ་གྱིས༌[^21]འོད་གསལ་བར་འཇུག་པས་ནམ་མཁའི་ཁམས་ཏེ། འཇིག་རྟེན་གྱི་ཁམས་སུ་སྤྲོ་བར་བྱ་ཞིང་ཆོས་ཀྱི་སྐུའི་ཚུལ་གྱིས་ཁྱབ་པར་བྱའོ། །

[Block 51]
དེ་དག་ནི་འཛིན་པའི་ཡན་ལག་ཅེས་བྱ་བ༌[^22]སྟེ་བཞི་པའོ། །

[Block 52 [HEADING]]
## རྗེས་སུ་དྲན་པ། ^5-0

[Block 53]
དེ་ལྟར་བདག་ཉིད་འོད་གསལ་བར་སོང་བར་རྣམ་པར་བསྒོམ་ཞིང་མངོན་སུམ་དུ་བྱས་ནས། གང་སྔོན་རྗེས་སུ་དྲན་པ་སྨིག་རྒྱུ་འདྲ་བ་ལ་སོགས་པའི་རྣམ་པས་ཡང་དག་པའི་མཐའ་ཐོབ་པ་དེ་དང་འདྲ་ཞིང་། དེ་ཉིད་ཀྱི་རིམ་པས༌[^23]སྤྲོ་བར་བྱ་ཞིང་བསྐྱེད་པར་བྱ་སྟེ། བཤད་མ་ཐག་པ་དེ་དག་ནི་རྗེས་སུ་དྲན་པ་ཞེས་བཤད་པ་ཡིན་པར་ཤེས་ཤིང་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 54]
སོ་སོར་སྣང་བ་དེ་ལས༌[^24]སྐྱེ། །ཞེས་བྱ་བ་ལ། སོ་སོར་སྣང་བ་ནི་ཡང་དག་པར་རིག་པ་སྟེ། དེ་ལས༌[^25]རྗེས་སུ་དྲན་པའི་ཡན་ལག་སྐྱེ་བར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 55 [HEADING]]
## ཏིང་ངེ་འཛིན། ^6-0

[Block 56]
ཐབས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་འཇུག་པ་སྟེ། ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པའི་སྦྱོར་བས་དངོས་པོ་ཐམས་ཅད་དེ་རྒྱུ་བ་དང་། མི་རྒྱུ་བ་ལ༌[^26]གནས་པ་གོང་བུའི་ཚུལ་གྱིས་ཏེ། ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་ཀྱིས་གཅིག་ཏུ་བྱས་ནས་རྒྱུ་བ་དང་། མི་རྒྱུ་བ་དེའི་དབུས་སུ་ཟུང་དུ་འཇུག་པའི་བདག་ཉིད་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་རྣམ་པར་བསྒོམ་པར༌[^27]བྱའོ། །

[Block 57]
རིམ་པ་འདི་ཉིད་ཀྱིས༌[^28]ཡུད་ཀྱི༌[^29]ཞེས་པ་སྟེ། སྐད་ཅིག་ཙམ་གྱིས་སོ། །

[Block 58]
ཡེ་ཤེས་རྫོགས་པར་བྱེད་པ་ཞེས་པ་སྟེ། ཡེ་ཤེས་ཀྱི་སྐུ་རྫོགས་པར་བྱེད་པ་ནི་ཏིང་ངེ་འཛིན་ཏེ། ཡན་ལག་དྲུག་པ་ཡིན་པར་བཤད་དོ། །

[Block 59]
དཔལ་སྒྱུ་འཕྲུལ་དྲ་བ་ལས་ཀྱང་ལྷ་བསྐྱེད་པའི་དབྱེ་བ་འདི་ཉིད་གསལ་བར་གསུངས་ཏེ།

[Block 60 [VERSE]]
རྣལ་འབྱོར་རྣམ་གསུམ་ཤེས་བྱ་སྟེ། །
བྱིན་གྱིས་བརླབས་དང་ཡོངས་བརྟག༌[^30]དང་། །
གཟུགས་ཉིད་ཡོངས་སུ་རྫོགས་པ་སྟེ། །
རྣལ་འབྱོར་སངས་རྒྱས་རྣམས་ཀྱི་བསྔགས། །

[Block 61 [VERSE]]
སྔགས་ཀྱིས་བྱིན་བརླབས་ང་རྒྱལ་བསྐྱེད། །
རྣལ་འབྱོར་བྱིན་རླབས༌[^31]ཡིན་པར་གསུངས། །
བྱང་ཆུབ་སེམས་ནི་དག་པ་དང་། །
གསང་སྔགས་ས་བོན་སྐྱེ་བ་ཆེ། །

[Block 62 [VERSE]]
ཕྱག་རྒྱའི་ཚོགས་སུ་བརྟག་པ་ཡིས། །
རིམ་གྱིས་གཟུགས་ནི་རྫོགས་བྱས་པ། །
དེ་ནི་བརྟག་པར༌[^32]བརྗོད་པ་སྟེ། །
རྣལ་འབྱོར་ཆོ་ག་ཡིན་པར་གསུངས། །

[Block 63 [VERSE]]
སྡུད་དང་སྤྲོ་བར་བྱས་པ་ལས། །
རྣམ་པའི་མཆོག་ཀུན་ལྡན་པ་དག །
སྐད་ཅིག་ཡེ་ཤེས་ཀྱིས་རྫོགས་པ། །
རྫོགས་པའི་རྣལ་འབྱོར་ཞེས་བཤད་དོ། །

[Block 64]
ཞེས་བྱ་བ་དང་། རྣམ་པར་སྣང་མཛད་མངོན་པར་བྱང་ཆུབ་པ་ལས་ཀྱང་། ལྷའི་རྣལ་འབྱོར་པ༌[^33]རྣམ་པ་གཉིས་སྟོན་ཏེ། གསང་བའི་བདག་པོ་ལྷའི་གཟུགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་དག་པ་དང་། ཡོངས་སུ་མ་དག་པའོ། །

[Block 65]
དེ་ལ་ཡོངས་སུ་དག་པ་ནི་རྟོག་པའི་ངོ་བོ་སྟེ། མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའོ། །

[Block 66]
ཡོངས་སུ་མ་དག་པ་ནི་མཚན་མ་དང་བཅས་པའི་གཟུགས་ཏེ། ཁ་དོག་དང་དབྱིབས་སོ། །

[Block 67]
དེ་ལ་ལྷའི་གཟུགས་རྣམ་པ་གཉིས་ཀྱིས་བྱ་བ་གཉིས་འགྲུབ་པར་འགྱུར་ཏེ། མཚན་མ་དང་བཅས་པས་ནི་མཚན་མ་དང་བཅས་པའོ། །

[Block 68]
མཚན་མ་མེད་པས་ནི་མཚན་མ་དང་བཅས་པའི་དངོས་གྲུབ་ཀྱང་འབྱུང་བར་འགྱུར་རོ། །

[Block 69 [VERSE]]
མཚན་མར་བཅས་པས་མཚན་བཅས་ཀྱིས། །
དངོས་གྲུབ་རྒྱལ་བ་དམ་པ་བཞེད། །
མཚན་མ་མེད་ལ་གནས་པས་ནི། །
མཚན་མ་ཅན་ཡང་འགྲུབ་ཏུ་རུང་། །

[Block 70 [VERSE]]
དེ་བས་རྣམ་པ་ཐམས་ཅད་དུ། །
མཚན་མ་མེད་པ་བསྟེན་པར་བྱ། །

[Block 71]
ཞེས་བྱ་བ་སྟེ་དགོངས་པས་བཤད་པའོ། །

[Block 72 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 73 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 74]
སྦྱོར་བ་ཡན་ལག་དྲུག་པ་ཞེས་བྱ་བའི་འགྲེལ་པ་སློབ་དཔོན་ཆེན་པོ་ཟླ་བ་གྲགས་པས་མཛད་པ་རྫོགས་སོ།། །།

[Block 75 [HEADING]]
### འགྱུར་བྱང། ^a-2-0
--- END BLOCKS ---
