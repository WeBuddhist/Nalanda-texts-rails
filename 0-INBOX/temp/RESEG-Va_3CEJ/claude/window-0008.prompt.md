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
[Block 281]
སྐྱེ་མཆེད་དང་ཁམས་དག་གིས་ནི་ཆོས་ཐམས་ཅད་བསྡུས་སོ། །

[Block 282]
མདོར་བསྡུ་ན་ཕུང་པོ་དང་ནི་སྐྱེ་མཆེད་དང་། ཁམས་གཅིག་གིས་ནི་ཐམས་ཅད་བསྡུས་པར་ཤེས་པར་བྱ་སྟེ། གཟུགས་ཀྱི་ཕུང་པོ་དང་ཡིད་ཀྱི་སྐྱེ་མཆེད་དང་ཆོས་ཀྱི་ཁམས་ཀྱིས་ཆོས་རྣམས༌[^115]ཐམས་ཅད་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 283]
བསྡུ་བ་དེ་ནི་གང་དང་གང་ནས་འབྱུང་ཡང་རུང་། རང་གི་ངོ་བོ་ཉིད་ཀྱིས་ཏེ། གཞན་གྱི་དངོས་པོས་ནི་མ་ཡིན་པར་རིག་པར་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཞན་གྱི་དངོས་དང་མི་ལྡན་ཕྱིར། །ཆོས་ནི་གཞན་གྱི་དངོས་པོ་དང་མི་ལྡན་ནོ། །

[Block 284]
དེ་ལྟ་བས་ན་གང་དང་མི་ལྡན་པ་དེ་ཉིད་ཀྱིས་བསྡུས་པར་ནི་མི་རུང་སྟེ། དཔེར་ན་མིག་གི་དབང་པོ་ནི་གཟུགས་ཀྱི་ཕུང་པོ་དང་། མིག་གི་སྐྱེ་མཆེད་དང་། ཁམས་དག་དང་། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བའི་བདེན་པ་དག་གིས་བསྡུས་ཏེ། དེ་དག་གི༌[^116]ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 285]
དེ་དག་གི༌[^117]ངོ་བོ་དང་མི་ལྡན་པའི་ཕྱིར་ཕུང་པོ་ལ་སོགས་པ་གཞན་དག་གིས་ནི་མ་ཡིན་ནོ། །

[Block 286]
དཔེར་ན་བསྡུ་བའི་དངོས་པོ་བཞི་པོ་དག་གིས་འཁོར་རྣམས་བསྡུས་པ་ལྟ་བུ་གཞན་གྱིས༌[^118]གཞན་བསྡུས་སོ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ནི་རེས་འགའ་བ་ཡིན་པའི་ཕྱིར་བརྡར་བཏགས་པ་ཡིན་པར་བྱའོ། །

[Block 287 [HEADING]]
#### མིག་ལ་སོགས་པ་ཁམས་གཅིག་པ་ཉིད། ^1-1-5-0

[Block 288]
མིག་དང་རྣ་བ་དང་སྣ་དག་གཉིས་གཉིས་ཡོད་པའི་ཕྱིར་ཁམས་ཉི་ཤུ་རྩ་གཅིག་ཏུ་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན་མི་འགྱུར་ཏེ། འདི་ལྟར།

[Block 289 [VERSE]]
མིག་ལ་སོགས་པ་གཉིས་མོད་ཀྱི། །
རིགས་དང་སྤྱོད་ཡུལ་རྣམ་པར་ཤེས། །
འདྲ་བའི་ཕྱིར་ན་ཁམས་གཅིག་ཉིད། །

[Block 290]
དེ་ལ་རིགས་འདྲ་བ་ནི་གཉི་ག་མིག་གི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 291]
སྤྱོད་ཡུལ་འདྲ་བ་ནི་གཉི་གའི་ཡུལ༌[^119]གཟུགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 292]
རྣམ་པར་ཤེས་པ་འདྲ་བ་ནི་གཉི་ག་མིག་གི་རྣམ་པར་ཤེས་པ་གཅིག་གི་རྟེན་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་མིག་གི་ཁམས་ནི་གཅིག་པ་ཉིད་དོ། །

[Block 293]
དེ་བཞིན་དུ་རྣ་བ་དང་། སྣ་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 294]
མཛེས་བྱའི་ཕྱིར་ན་གཉིས་འབྱུང་ངོ་། །མིག་ལ་སོགས་པ་ཁམས་གཅིག་པ་ཉིད་ཡིན་ཡང་རྟེན་མཛེས་པར་བྱ་བའི་ཕྱིར་གཉིས་འབྱུང་ངོ་། ། དེ་ལྟ་མ་ཡིན་ཏེ། མིག་དང་རྣ་བའི་རྟེན་གཅིག་དང་། །སྣའི་བུ་ག་གཅིག་ཏུ་གྱུར་ན་ཤིན་ཏུ་མི་མཛེས་པར་འགྱུར་རོ། །

[Block 295]
ཕུང་པོ་དང་། ཁམས་དང་། སྐྱེ་མཆེད་དག་བཤད་ཟིན་ཏོ། །

[Block 296 [HEADING]]
### ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་དོན། ^1-2-0

[Block 297]
ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་དོན་གང་ཡིན་པ་འདིར་བརྗོད་པར་བྱ་སྟེ།

[Block 298 [VERSE]]
སྤུངས་དང་སྐྱེ་དགུ༌[^120]རིགས་ཀྱི་དོན། །
ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་རྣམས་ཡིན། །

[Block 299 [HEADING]]
#### ཕུང་པོའི་དོན། ^1-2-1-0

[Block 300]
མདོ་ལས།

[Block 301]
གཟུགས་གང་ཡིན་པ་ཅི་ཡང་རུང་འདས་པའམ། མ་འོངས་པའམ། ད་ལྟར་བྱུང་བའམ། ནང་གིའམ། ཕྱིའི་འམ། རགས་པའམ། ཕྲ་བའམ། ངན་པའམ། གྱ་ནོམ་པའམ། ཐག་རིང་བ་ན་ཡོད་པ་གང་ཡིན་པ་འམ། ཉེ་བ་ན་ཡོད་པ་གང་ཡིན་པ༌[^121]དེ་དག་ཐམས་ཅད་གཅིག་ཏུ་བསྡུས་ཏེ་གཟུགས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བའི་གྲངས་སུ་འགྲོའོ་ཞེས་འབྱུང་བའི་ཕྱིར་སྤུངས་པའི་དོན་ནི་ཕུང་པོའི་དོན་ཏོ་ཞེས་བྱ་བར་གྲུབ་པོ། །དེ་ལ་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གཟུགས་འདས་པ་ནི་མི་རྟག་པ་ཉིད་ཀྱིས་འགགས་པའོ། །

[Block 302]
མ་འོངས་པ་ནི་མ་བྱུང་བའོ། །

[Block 303]
ད་ལྟར་བྱུང་བ་ནི་བྱུང་བ༌[^122]ལ་མ་འགགས་པའོ། །

[Block 304]
ནང་གི་ནི་རང་གི་རྒྱུད་ལ་ཡོད་པའོ། །

[Block 305]
གཞན་ནི་ཕྱིའི་འོ། །

[Block 306]
ཡང་སྐྱེ་མཆེད་ཀྱི་སྒོ་ནས་སོ། །

[Block 307]
རགས་པ་ནི་ཐོགས་པ་དང་བཅས་པའོ། །

[Block 308]
ཕྲ་བ་ནི་ཐོགས་པ་མེད་པའོ། །

[Block 309]
ཡང་ན་ལྟོས་པ་པ་ཡིན་ནོ། །

[Block 310]
གལ་ཏེ་ལྟོས་པ་པ་ཡིན་པའི་ཕྱིར་མ་གྲུབ་བོ་ཞེ་ན། མ་ཡིན་ཏེ། ལྟོས་པས༌[^123]ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 311]
གང་ལ་ལྟོས་ཏེ་རགས་པ་ཡིན་པ་ནི་ནམ་དུ་ཡང་དེ་ལ་ལྟོས་ནས་ཕྲ་བ་མ་ཡིན་ཏེ། ཕ་དང་བུ་བཞིན་ནོ། །

[Block 312]
ངན་པ་ནི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 313]
གྱ་ནོམ་པ་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའོ། །

[Block 314 [VERSE]]
རིང་བ་ནི་འདས་པ་དང་མ་འོངས་པའོ། །
ཉེ་བ་ནི་ད་ལྟར་བྱུང་བ་སྟེ།
རྣམ་པར་ཤེས་པའི་བར་དུའང་དེ་དང་འདྲའོ། །

[Block 315]
འདི་ནི་ཁྱད་པར་ཡིན་ཏེ། རགས་པ་ནི་དབང་པོ་ལྔ་ལ་བརྟན་པའོ། །

[Block 316]
ཕྲ་བ་ནི་ཡིད་ལས་བྱུང་བའོ། །

[Block 317]
ཡང་ན་ས་ལས་རིག་པར་བྱའོ་ཞེས་སོ། །

[Block 318]
བཙུན་པ་ན་རེ་ནི་གཟུགས་རགས་པ་ནི་དབང་པོ་ལྔས་གཟུང་བར་བྱ་བའོ། །

[Block 319]
གཞན་ནི་ཕྲ་བའོ། །

[Block 320]
ངན་པ་ནི་ཡིད་དུ་མི་འོང་བའོ། །
--- END BLOCKS ---
