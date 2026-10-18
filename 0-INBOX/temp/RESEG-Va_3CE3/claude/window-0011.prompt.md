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
[Block 386]
ཡོངས་སུ་ཤེས་པར་བྱ་བ་ལ་སོགས་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་བདེན་པར་རྟོགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 387]
འབྲས་བུ་གང་ཡིན་པ་ནི་རྣམ་པར་སྨིན་པའོ། །

[Block 388]
རྣམ་པར་སྨིན་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་སྨིན་པའི་ཆོས་ཅན་ནོ། །

[Block 389]
རབ་ཏུ་དགའ་བ་ལ་སོགས་པ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་ཀྱི་ངོ་བོ་ཉིད་དུའོ། །

[Block 390]
འཐོབ་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་རྙེད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 391]
དམིགས་སུ་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་དབང་པོའི་སྤྱོད་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 392]
བརྗོད་དུ་ཡོད་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཚིག་གི་ལམ་དུ་མ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 393]
[^259]བརྗོད་དུ་མེད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་ཚིག་གི་ལམ་གྱིས་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 394 [HEADING]]
##### ནམ་མཁའ་སེམས་ཅན་ཚད་མེད་གྲངས་མེད་པའི་གོ་འབྱེད་པ། ^1-1-6-3-0

[Block 395]
དེའི་འོག་ཏུ། རབ་འབྱོར་གང་ཡང་ཁྱོད་ཀྱིས་འདི་སྐད་དུ་ཇི་ལྟར་ནམ་མཁའ་སེམས་ཅན་ཚད་མེད་གྲངས་མེད་པའི་གོ་འབྱེད་དོ་ཞེས་སྨྲས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཚིག༌[^260]གསུམ་བསྟན་ཏེ། རབ་འབྱོར་སེམས་ཅན་མེད་པའི་ཕྱིར་ནམ་མཁའ་མེད་པར་རིག་པར་བྱའོ། །

[Block 396]
ནམ་མཁའ་མེད་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་མེད་པར་རིག་པར་བྱའོ༌[^261]ཞེས་བྱ་བའི༌[^262]དོན་གང་ཡིན་ཞེ་ན། གང་ཟག་ལ་བདག་མེད་པས་ཆོས་ལ་བདག་མེད་པ༌[^263]འཇུག་པར་འགྱུར་བའི་ཕྱིར་སྔར་སེམས་ཅན་མེད་པ་ལ་གནས་ནས་ནམ་མཁའ་མེད་པ་ལ་གནས་པར་འགྱུར་རོ། །

[Block 397]
ནམ་མཁའ་མེད་པས་ཐེག་པ་ཆེན་པོ་མེད་པ་ལ་གནས་པར་འགྱུར་རོ། །

[Block 398]
དེ་དག་མེད་པའི་ཕྱིར་དཔག་ཏུ་མེད་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱང་མེད་པ་ཉིད་དེ་ཆོས་ཐམས་ཅད་ཀྱང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 399]
སེམས་ཅན་མེད་པའི་ཕྱིར་དེ་བཞིན་ཉིད་མེད་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་མེད་པས་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་དང་། སྒྲའི་དེ་བཞིན་ཉིད་ལ་སོགས་པ་མེད་པར་རིག་པར་བྱའོ། །

[Block 400]
དེ་ལྟར་ཆོས་ཐམས་ཅད་མེད་པའི་ཕྱིར་ནམ་མཁའ་དང་མཚུངས་པས་གོ་སྐབས་འབྱེད་དོ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 401]
མེད་པ་ཉིད་ཀྱི་ཕྱིར་དཔག་ཏུ་མེད་པ་ལ་སོགས་པར་འགྱུར་རོ། །

[Block 402]
འགྲེས་འདི་ལ་ཉི་ཤུ་རྩ་དྲུག་སྟེ༌[^264]སེམས་ཅན་མེད་པའི་ཕྱིར་ནམ་མཁའ་མེད་དོ། །

[Block 403]
ནམ་མཁའ་མེད་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་མེད་དོ་ཞེས་བྱ་བ་ནི་འགྲེས་དང་པོའོ། །

[Block 404]
གསུམ་པོ་དེ་དག་ཉིད་དཔག་ཏུ་མེད་པ་དང་སྦྱར་བ་ནི་གཉིས་པའོ། །

[Block 405]
གྲངས་མེད་པ་དང་སྦྱར་བ་ནི་གསུམ་པའོ། །

[Block 406]
ཚད་མེད་པ་དང་སྦྱར་བ་ནི་བཞི་པའོ། །

[Block 407]
ཆོས་ཀྱི་དབྱིངས་དང་སྦྱར་བ་ནི་ལྔ་པའོ། །

[Block 408]
དེ་བཞིན་ཉིད་དང་སྦྱར་བ་ནི་དྲུག་པའོ། །

[Block 409]
སེམས་ཅན་དང་སྲོག་ལ་སོགས་པ་བཅུ་གསུམ་གྱིས་བསྣན༌[^265]ཏེ། ཐ་མ་ཡང་དག་པའི་མཐའ་དང་སྦྱར་བ་ནི་བདུན་པའོ། །

[Block 410]
དེ་ཉིད་ལ་ཡང་དག་པའི་མཐའ་བཀོལ་ཏེ། བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་དང་སྦྱར་བ་ནི་བརྒྱད་པའོ། །

[Block 411]
དེ་དག་ཉིད་གཟུགས་ལ་སོགས་པའི་ཕུང་པོའི་ཆོས་དང་སྦྱར་བ་ནི་དགུ་པའོ། །

[Block 412]
དེ་དག་ཉིད་ནང་གི་སྐྱེ་མཆེད་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་པའོ། །

[Block 413]
ཕྱི་རོལ་གྱི་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་གཅིག་པའོ། །

[Block 414]
རྣམ་པར་ཤེས་པ་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་གཉིས་པའོ། །

[Block 415]
རེག་པ་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་གསུམ་པའོ། །

[Block 416]
ཚོར་བའི་ཚོགས་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་བཞི་པའོ། །

[Block 417]
ཁམས་དྲུག་དང་སྦྱར་བ་ནི་བཅོ་ལྔ་པའོ། །

[Block 418]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་སྦྱར་བ་ནི་བཅུ་དྲུག་པའོ། །

[Block 419]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་སྦྱར་བ་ནི་བཅུ་བདུན་པའོ། །

[Block 420]
སྟོང་པ་ཉིད་ཐམས་ཅད་དང་སྦྱར་བ་ནི་བཅོ་བརྒྱད་པའོ། །

[Block 421]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་སྦྱར་བ་ནི་བཅུ་དགུ་པའོ། །

[Block 422]
འཕགས་པའི་བདེན་པ་ནས་གཟུངས་ཀྱི་སྒོའི་བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་པའོ། །

[Block 423]
སྟོབས་བཅུ་ནས། མ་འདྲེས་པའི་བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གཅིག་པའོ། །

[Block 424]
རིགས་ཀྱི་སའི་ཆོས་ནས་བྱས་པ་རྟོགས་པའི༌[^266]བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གཉིས་པའོ། །

[Block 425]
རྒྱུན་དུ་ཞུགས་པ་ནས་དགྲ་བཅོམ་པའི་བར་གྱི་གང་ཟག་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གསུམ་པའོ། །
--- END BLOCKS ---
