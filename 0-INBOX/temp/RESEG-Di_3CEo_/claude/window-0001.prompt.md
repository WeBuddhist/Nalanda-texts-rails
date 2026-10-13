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
[Block 36 [HEADING]]
### ཆོས་ཐམས་ཅད་མདོར་བསྡུས་ཏེ་བསྟན་པ། ^1-5-0

[Block 37]
ཆོས་དེ་དག་ཀྱང་གང་ཞེ་ན། ཟག་བཅས་ཟག་པ་མེད་ཆོས་རྣམས། །ཞེས་བྱ་བ་སྨོས་ཏེ། [^22]འདི་ནི་ཆོས་ཐམས་ཅད་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 38 [HEADING]]
#### ཟག་པ་དང་བཅས་པའི་ཆོས། ^1-5-1-0

[Block 39]
དེ་ལ་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་གང་ཞེ་ན། ལམ་མ་གཏོགས་པའི་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་སྨོས་སོ། །

[Block 40]
ལམ་གྱི་བདེན་པ་མ་གཏོགས་པ་འདུས་བྱས་ཀྱི་ཆོས་གཞན་རྣམས་ནི་ཟག་པ་དང་བཅས་པ་དག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར་དེ་དག་ལ། ཟས༌[^23]རྣམས་ཀུན་དུ་རྒྱས་པར་འགྱུར། །ཞེས་བྱ་སྟེ། འདི་རྣམས་ལ་ཟག་པ་རྣམས་རྒྱས་པར་འགྱུར་ཏེ། འགོག་པ་དང་ལམ་གྱི་བདེན་པ་དག་ལ་དམིགས་པ་ཡིན་དུ་ཟིན་ཀྱང་རྒྱས་པར་ནི་མི་འགྱུར་རོ། །

[Block 41]
ཟག་པ་དང་བཅས་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 42 [HEADING]]
#### ཟག་པ་མེད་པའི་ཆོས། ^1-5-2-0

[Block 43 [VERSE]]
ཟག་མེད་ལམ་གྱི་བདེན་པ་དང་། །
འདུས་མ་བྱས་རྣམ༌[^24]གསུམ་ཡང་སྟེ། །
རྣམ་པ་གསུམ་གང་ཞེ་ན།
ནམ་མཁའ་དང་ནི་འགོག་པ་གཉིས། །

[Block 44]
གཉིས་གང་ཞེ་ན། སོ་སོར་བརྟགས་པས་འགོག་པ་དང་། སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ། དེ་ལྟར་ན་ནམ་མཁའ་ལ་སོགས་པ་འདུས་མ་བྱས་གསུམ་པོ་དེ་དག་དང་ལམ་གྱི་བདེན་པ་ནི་ཐག་པ་མེད་པའི་ཆོས་རྣམས་ཏེ། དེ་དག་ལ་ཟག་པ་རྒྱས་པར་འགྱུར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 45 [HEADING]]
#### འདུས་མ་བྱས་པ་བསྟན་པ། ^1-5-3-0

[Block 46]
འདུས་མ་བྱས་པ་བསྟན་པ།

[Block 47 [VERSE]]
རྣམ་པ་གསུམ་པོ་གང་ཡིན་པ། །
དེ་ལ་ནམ་མཁའ་མི་སྒྲིབ་པ། །

[Block 48]
ནམ་མཁའ་ནི་སྒྲིབ་པ་མེད་པའི་རང་བཞིན་ཏེ། །

[Block 49 [VERSE]]
གང་ན་གཟུགས་ཀྱི་གོ་ཡོད་པའོ། །
སོ་སོར་བརྟགས་པས་འགོག་པ་གང་། །
བྲལ་བའོ་སོ་སོ་སོ་སོ་ཡིན། །

[Block 50]
གང་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་དང་བྲལ་བ་དེ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པའོ། །

[Block 51]
སྡུག་བསྔལ་ལ་སོགས་པ་འཕགས་པའི་བདེན་པ་རྣམས་ལ༌[^25]སོ་སོར་རྟོག་པ༌[^26]ནི་སོ་སོར༌[^27]བརྟགས་པ་སྟེ། དགེ་བའི་བློ་ཡི་བྱེ་བྲག་གོ། །

[Block 52]
དེས་ཐོབ་པར་བྱ་བའི་འགོག་པ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པའོ། །

[Block 53]
དེ་ཡང་འདི་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་སོ་སོ་སོ་སོར་ཏེ།

[Block 54]
ལྡན་པའི་རྫས་རྣམས་ཇི་སྙེད་པ། །བྲལ་བའི་རྫས་ཀྱང་དེ་སྙེད་དོ། །

[Block 55]
འགོག་པ་གཅིག་ཉིད་ཡིན་ན༌[^28]ཉོན་མོངས་པའི་ཕྱོགས་གཅིག་སྤོངས༌[^29]ན་དེ་མངོན་སུམ་དུ་བྱས་པར་འགྱུར་བས་ལྷག་མའི་གཉེན་པོ་བསྒོམ་པ་དོན་མེད་པར་འགྱུར་རོ་ཞེས་སོ་སོར་བརྟགས༌[^30]པས་འགོག་པ་བཤད་ཟིན་ཏོ། །

[Block 56 [VERSE]]
སྐྱེ་ལ་གཏན་དུ་གེགས་བྱེད་པ། །
འགོག་གཞན་སོ་སོར་བརྟགས་མིན་པས། །

[Block 57]
ཆོས་མ་འོངས་པ་རྣམས༌[^31]སྐྱེ་བ་ལ་གཏན་དུ་གེགས་སུ་གྱུར་པ་བྲལ་བ་ལས་གཞན་པའི་འགོག་པ་གང་ཡིན་པ་དེ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ། འདི་སོ་སོར་བརྟགས་པས་ཐོབ་པ་ནི༌[^32]མ་ཡིན་ནོ། །

[Block 58]
འོ་ན་ཅི་ཞེ་ན། རྐྱེན་མ་ཚང་བ་ལས༌[^33]ཐོབ་པའོ། །

[Block 59 [HEADING]]
### འདུས་བྱས་ཆོས་རྣམས། ^1-6-0

[Block 60]
ཡང་། ལམ་མ་གཏོགས་པའི་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་གང་སྨྲས་པའི་ཡུལ་འདུས་བྱས་དེ་དག་གང་ཞེ་ན།

[Block 61 [VERSE]]
འདུས་བྱས་ཆོས་རྣམས་དེ་དག་ཀྱང་། །
གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། །

[Block 62]
གཟུགས་ཀྱི་ཕུང་པོ་དང་། [^34]ཚོར་བའི་ཕུང་པོ་དང་། འདུ་ཤེས་ཀྱི་ཕུང་པོ་དང་། འདུ་བྱེད་ཀྱི་ཕུང་པོ་དང་། རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཞེས་བྱ་བ་དེ་དག་ནི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 63]
རྐྱེན་རྣམས་འདུས་ཤིང་ཕྲད་ནས་བྱས་པ་དག་གི་ཕྱིར་འདུས་བྱས་རྣམས་སོ། །

[Block 64 [VERSE]]
དེ་དག་ཉིད་དུས་གཏམ་གཞི་དང་། །
ངེས་པར་འབྱུང་བཅས་གཞི་དང་བཅས། །

[Block 65]
དེ་ལ་སོང་བ་དང་འགྲོ་བ་དང་འགྲོ་བར་འགྱུར་བའི་ཕྱིར་རམ། མི་རྟག་པ་ཉིད་ཀྱིས་ཟ་བའི་ཕྱིར་དུས་རྣམས་སོ། །

[Block 66]
གཏམ་ནི་ངག་གོ། །

[Block 67]
དེའི་གཞི་ནི་མིང་སྟེ། དོན་དང་བཅས་པའི་གཞི་བཟུང་བས་ན་འདུས་བྱས་ནི་གཏམ་གྱི་གཞི་ཞེས་བྱའོ། །

[Block 68]
ངེས་པར་འབྱུང་བ་ཉིད་ནི་ངེས་པར་འབྱུང་བ་སྟེ། འདུས་བྱས་ཐམས་ཅད་ཀྱི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 69]
དེ་འདི་དག་ལ་ཡོད་པས་ངེས་པར་འབྱུང་བཅས༌[^35]དག་གོ། །

[Block 70]
རྒྱུ་དང་བཅས་པའི་ཕྱིར་གཞི་དང་བཅས་པ་དག་གོ། །

[Block 71]
ཡང་འདུས་བྱས་དེ་དག་ཉིད། གང་དག་ཟག་བཅས་ཉེར་ལེན་པའི། །ཕུང་པོ་འང་དེ་དག །[^36]དེ་དག་ཉེ་བར་ལེན་པ་དག་ནི་ཉོན་མོངས་པ་རྣམས་ཏེ། དཔེར་ན་རྩྭ་དང་སྦུན་པའི་མེ་བཞིན་ནམ། དེ་དག་ལ་རག་ལུས་པའི་ཕྱིར་རྒྱལ་པོའི་མི་བཞིན་ནོ། །

[Block 72]
ཡང་ན་དེ་དག་ལས་ཉེ་བར་ལེན་པ་རྣམས་འབྱུང་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་རྣམས་ཏེ། མེ་ཏོག་དང་འབྲས་བུའི་ཤིང་ལྗོན་པ་བཞིན་ནོ། །

[Block 73]
ཟག་པ་དང་བཅས་པའི་ཆོས་དེ་དག་ཉིད། འཐབ༌[^37]བཅས་ཀྱང་ཞེས་བརྗོད་དོ། །

[Block 74]
འཐད་པ༌[^38]ནི་ཉོན་མོངས་པ་རྣམས་ཏེ། བདག་དང་གཞན་ལ་གནོད་པའི་ཕྱིར་རོ། །

[Block 75]
དེ་དག་གིས་རྒྱས་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་འཐབ་བཅས་དག་སྟེ།
--- END BLOCKS ---
