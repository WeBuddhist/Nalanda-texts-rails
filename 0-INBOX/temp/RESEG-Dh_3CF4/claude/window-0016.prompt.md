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
[Block 561]
སྦྱིན་པ་དེས་དགའ་བར་འགྱུར༌[^270]ཏེ་ཞེས་བྱ་བ་ནི་རེ་བ་ཇི་ལྟ་བ་བཞིན་དུ་བསྒྲུབ་པ༌[^271]ལ་སོགས་པ་གསུམ་གྱིས་སོ། །

[Block 562]
ཕྱོགས་ཐ་དད་པའི་ཡུལ་ན་གནས་པ་དེ་ནི་ཕྱོགས་ཐ་དད་པའི་ཡུལ་ན་གནས་པའོ།[^272] །ཡང་ན་ཕྱོགས་ཐ་དད་པའི་གནས་པས་མཚོན་པའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་དག་གོ། །

[Block 563]
ཕྱོགས་ཐ་དད་པ་ཞེས་སྨོས་པས་ནི་ཐག་རིང་པོ་ནས་འོང་བར་སྟོན་པ་མངོན་པར་མཚོན་པའོ། །

[Block 564]
ཡུལ་ན་གནས་པ་ཞེས་སྨོས་པས་ནི་ཡུལ་ན་གནས་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ། །

[Block 565]
གཞན་དག་ན་རེ་རེ་བ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་མེད་དམ། ཅིའི་ཕྱིར་ཐག་རིང་པོ་ནས་ལྷགས་ཤིང་འོངས་ཤེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མི་ཡུལ་ཀུན་ཏུ༌[^273]ཡིད་ཀྱིས༌[^274]བརྟགས་ན་ཡང་། །ཞེས་བྱ་བའི་ཚིགས༌[^275]བཅད་འདི་སྨོས་སོ། །

[Block 566]
གཞན་དུ་བསླང་བའི་སྐབས་ནི་མ་རྙེད་པ་ཞེས་བྱ་བ་ནི་སེར་སྣ་ཆེ་བར་གྱུར་པ་སྟེ། སྐྱེ་བོ་རྣམས་སྦྱིན་པ་ལ་འཇུག་པ་མེད་པར་སྟོན་ཏོ། །

[Block 567]
དེ་བས་ན་རིང་པོ་ནས་ལྷགས་པར༌[^276]གྱུར་པ་ཡིན་ནོ། །

[Block 568]
ནགས་ཚལ་གླང་པོ་མཚོ་ཆེན་ངོགས་ལྷགས་བཞིན། །ཞེས་བྱ་བ་འདིས་ནི་ཡུལ་ན་གནས་པའི་སྐྱེ་བོ་དག་སྦྱིན་པ་ལ་འཇུག་ཅིང་རེ་བ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཡོད་ཀྱང་དེ་དག་སྤངས་ཏེ་ལྷགས་པ་ཡིན་ནོ། །

[Block 569]
སྐྱེ་བོ་མཛའ་བཤེས་བྱེས༌[^277]ནས་འོངས་པ་དག །ཅེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་ལུས་ནི་སྦྱོར་བ་དང་། དངོས་དང་། མཇུག་སངས་རྒྱས་ཀྱི་བཀའ་དང༌[^278]མཐུན་པར་སྟོན་པ་ཡིན་ཏེ། དེ་ཡང་མདོའི་དོན་དང་མཐུན་པར་འགྱུར་བ་སྟེ། [^279]སྦྱིན་པའི་སྔ་རོལ་ཏུ་ཡིད་དགའ་བར་འགྱུར་བ་དང་། སྦྱིན་པའི་ཚེ་ན་སེམས་དང་བར་འགྱུར་བ་དང་། བྱིན་ནས་མཐར་ཡང་རྗེས་སུ་དགའ་བར་གྱུར་པ་ཡིན་ཏེ། སྦྱོར་བ་དང་། དངོས་དང་། མཇུག་ཉིད་ཀྱིས་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་བསྟན་ཏེ། གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་སྐྱེ་བོ་མཛའ་བཤེས་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་སྦྱར་རོ། །

[Block 570]
སྦྱིན་པ་ལས་བྱུང་བ་ཞེས་བྱ་བ༌[^280]དང་། ཚིགས་བཅད་འདི་གཉིས་ཀྱིས་ནི་མཐོང་བའི་ཆོས་ཀྱིས་རྟོགས་པ་གཉིས་བསྟན་ཏེ། བདག་ཉིད་ལ་ལྟ་བ་དང་། གཞན་དག་ལ་ཡང་གྲགས་པར་བྱེད་པའོ། །

[Block 571]
སྦྱིན་པའི་བསོད་ནམས་མི་འཕེལ་བར་གྱུར་པས་ཞེས་བྱ་བའི་བློས་ཀུན་ཏུ་བརྟགས་པ་བཞིན་དུ་གཞན་ལ་ནོར་བགེགས་སུ་གྱུར་ཅིང་འཕེལ་བར་གྱུར་པས་སོ། །

[Block 572]
སྦྱིན་པའི་བསོད་ནམས་མི་འཕེལ་བ་དེ་ཉིད་སྨྲས་པ། སློང་བའི་སྐྱེ་བོ་འདུ་བ་ཉུང་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ཉིད་བསྒྲུབ་པའི་ཕྱིར། དེ་ལ་བརྟེན་ནས་ཕོངས་པ༌[^281]ཚིམ་པར་གྱུར།[^282] །ཞེས་བྱ་བ་འདི་ཡིན༌[^283]ཏེ། རྒྱལ་པོ་ནི་སྦྱིན་པའི་བསོད་ནམས་མི་འཕེལ་བར་གྱུར་པས་མགུ་བར་མ་གྱུར་ཏེ། སྦྱིན་ལ་དཔའ་བ་དེ་ནི་སྙིང་མ་ཚིམ། །ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 573]
ཕོངས་པ་རྣམས་ཚིམ་པར་གྱུར་ན་དེ་ཅིའི་ཕྱིར་ཚིམ་པར་མ་གྱུར་ཞེ་ན། སྨྲས་པ། ཕོངས་པ༌[^284]རྣམས་ཀྱིས་སློང་བའི་ཚད་དག་གིས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 574]
བདག་གི་ལུས་ནི་ངེས་པར་སྦྱིན་བྱས་ནས་སམ། འདི་ནི༌[^285]རྒྱལ་པོས་གྱི་ན་ད་རྣམས་བརྟགས་པ་སྟེ། དེ་བརྟག་པའི༌[^286]ཕྱིར་བྲམ་ཟེ་རྒན་པོ་ལོང་བ་ཞིག་གི་གཟུགས་སུ་བསྒྱུར་ནས་ཞེས་བྱ་བ་ལ། གསུམ་སྨོས་པའི་ལོང་བ་སྨོས་པ་ནི་ལམ་དུ་འགྲོ་བར་མི་ནུས་པའོ། །

[Block 575]
རྒན་པོ་སྨོས་པ་ནི་དཀའ་བར་གྱུར་པ་ཡིན་ནོ། །

[Block 576]
བྲམ་ཟེ་སྨོས་པ་ནི་འདི༌[^287]དག་གིས་སྦྱིན་པའི་གནས་སུ་བསྟན་པའོ། །

[Block 577]
སྙིང་རྗེ་དང་བྱམས་པ་བསྒོམ་པ༌[^288]ཞེས་བྱ་བ་འདིར་རིམ་པ་སྨོས་པ་ནི་སྡུག་བསྔལ་བསལ་བར་བྱས་ལ། ཕྱི་ནས་བདེ་བ་ལ་གཞག་པར༌[^289]བྱ་སྟེ། སྡུག་བསྔལ་ལས་ཐར་བར་མ་བྱས་པར་ནི་བདེ་བ་ལ་གཞག་པར༌[^290]མི་ནུས་སོ། །

[Block 578]
ལྟ་བ་བརྟན༌[^291]ཞིང་གསལ་ལ་ཞི་བ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་། གཏི་མུག་དང་། ཞེ་སྡང་གི་ཉོན་མོངས་པ་ལ་མི་གནས་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 579]
གཏི་མུག་བར་དུ་སྨོས་པ་ནི་དེ་གཉི་གའི་ཡང་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 580]
གཏི་མུག་ཆེ་བར་གྱུར་ན་ལྟ་བ་གསལ་བ་མེད་པར་འགྱུར་རོ། །

[Block 581]
བསུ་བ་བཞིན་ཞེས་བྱ་བ་ནི་ཐག་རིང་བ་ན་གནས་པའོ། །

[Block 582]
འཁྱུད་པ༌[^292]བཞིན་ཞེས་བྱ་བ༌[^293]དེ་དང་ཉེ་ན་གནས་པར་གྱུར་པ་སྟེ། ཡང་ན་བསུ་བ་ནི་སྙིང་རྗེ་བསྒོམས་པས་སོ། །

[Block 583]
འཁྱུད་པ༌[^294]བཞིན་དུ་ལྟ་བ་ནི་བྱམས་པ་ཡོངས་སུ་བསྒོམས་པ་སྟེ། སྡུག་བསྔལ་བསལ་བ་དང་བདེ་བ་ལ་ཉེ་བར་སྦྱར་བ་གཉིས་ཀྱིས་བྱ་བ་ཕུན་སུམ་ཚོགས་པའི་བསམ་པ་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 584]
ས་བདག་དམ་པ་ཁྱོད་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་ལུས་ནི་གང་སློང་བ་དང་། ཇི་ལྟ་བུ་སློང་བ་དང་། གོང༌[^295]ནས་འོངས་ཏེ་སློང་བའོ། །

[Block 585]
གནས་སྐབས་ཇི་ལྟ་བུས་ཤེ་ན། གནས་སྐབས་གཉིས་པོའི་ཡོན་ཏན་མེད་པས་ནི་ལམ་དུ་འགྲོ་བའི་ཕུན་སུམ་ཚོགས་པ་མེད་པ་ཡིན་ཏེ། མིག་གི་ཡོན་ཏན་མེད་པ་ནི་མི་མཐོང་བཞིན་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 586]
ནུས་པའི་ཡོན་ཏན་ཡང་མེད་དེ་རྒན་པོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 587]
གང་སློང་བ་དེ་ནི་མིག་གང་ལ་གང་ཡོད་པ་དེ་སྟེ། སྤྱན་འཚལ་ཕྱིར་ཞེས་བྱ་བ་ཡིན་ཏེ། དེའི་མིག་གཅིག༌[^296]སློང་བ་སྟེ། འཇིག་རྟེན་གྱི་བྱ་བ་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 588]
དེ་ལྟར་གང་དང་གང་གི་དོན་དུ་སློང་བ་དེ་ཚིགས་བཅད་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 589]
གང་སློང་བ་ནི་འདོད་པའི་ནོར་སློང་བ་སྟེ། སློང་བའི་དངོས་པོས་དེ་དགའ་བ༌[^297]ཐོབ་པར་གྱུར་པ་ཡིན་ཏེ། སྤྱན་ནི་གཅིག་པུས༌[^298]ཀྱང་འཇིག་རྟེན་བགྱི་བ་འགྲུབ་ཅེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 590]
སུ་ཡིས་བསྟན་ཞེས་བྱ་བ་ནི་ལྷས་ཡིན་ནམ་ཞེས་རྟོགས་པ༌[^299]སྐྱེས་ཏེ་དྲིས་པའོ། །

[Block 591]
གཞན་གྱི་སྤྱོད་ལམ་ནི་མ་ཡིན་པའི་ཕྱིར་བདག་ཉིད་ལ་རྣམ་པར་རྟོག་པ་སྟེ། དེ་བས་ན་སློབ་དཔོན་གྱིས་འདི་སྨྲས་པ་ཡིན་ནོ། །

[Block 592]
རྒྱལ་པོ་དེའི་བསམ་པ་རིག་ནས་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ཀྱིས་བསམས༌[^300]པའོ། །

[Block 593]
ལྷའི་མཐུས་ཞེས་པ་ནི་གལ་ཏེ་ལྷའི་མཐུ་ཡིན་ན་འདིའི་མིག་གི་དབང་པོ་ཡང་ཅིའི་ཕྱིར་ལྷའི་མཐུས་དེ་ལྟར་མི་འགྱུར་ཏེ་འགྱུར་རོ་ཞེས་བྱ་བའི་གནས་སྐབས་སོ། །

[Block 594]
དེས་ན་དེ་ཉིད་སྨྲས་པ། ཆོ་ག་འདིས་མིག་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བདག་གིས་མིག་བྱིན་པ་དང་། ལྷའི་མཐུ་དང་ལྡན་པའི་བྲམ་ཟེའི་མིག་གི་ཕུན་སུམ་ཚོགས་པའི་རྒྱུའོ་ཞེས་སོ། །

[Block 595]
ཡིད་ལ་རེ་བ་གང་གིས་འདིར་འོངས་པ། ། ཞེས་བྱ་བ་ནི་མིག་གཅིག་ཐོབ་པར་འདོད་པ༌[^301]གང་ཡིན་པ་དེ་ཉིད་བྲམ་ཟེ་ཁྱོད་ཀྱི༌[^302]རེ་བ་བསྐང་བར་བྱ་ཞེས་བྱ་བ་ཡིན་ཏེ། མིག་གཅིག་སྦྱིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 596]
རེ་བ་བསྐང་བ་ཉི་ཚེར་མ་ཟད་དེ། གཞན་ཡང་མིག་གཉི་ག་ཡང་ངས་སྦྱིན་གྱིས་ཞེས༌[^303]བྱ་བ་ཡིན་ནོ། །

[Block 597]
ཡང་ན་འདིའི་དོན་ནི་མིག་གཅིག་སྦྱིན་པ་ཉིད་ཇི་ལྟར་རེ་བ་བསྐང་བ་ཡིན་ཏེ། རེ་བ་སྐོང་བ༌[^304]ནི་རེ་ཞིག་ཇི་ལྟར་ཡང་མིག་གཉིས་ཐོབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 598]
འོན་ཀྱང་འདིས་ཡིད་ལ་རེ་བ་བཞིན་དུ་སློང་བར་མི་ནུས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། མི་སྦྱིན་སྙམ་པ་དང་། མིག་གཉིས་བསླངས་ན་རྒྱལ་པོ་ལ་གནོད་པར་འགྱུར་བ་དང་། གཞན་གྱི་སེམས་སྲུང་བར་སྟོན་པ་ཡིན་ཏེ། ཡིད་ལ་རེ་བ་ནི་རེ་ཞིག་མིག་གཉི་ག་ཐོབ་པ་ཉིད་དེ། [^305]དེས་ན་དེ་ཉིད་སྨྲས་པ། ཡིད་ལ་རེ་བ་ཡོངས་སུ་བསྐང་བ་ཞེས་སྨོས་པ་དེ་ཉིད་ནི་མིག་གཉིས་ཀྱང་ནི་ངས་སྦྱིན་གྱིས་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 599]
གཞན་དུ་ཇི་ལྟར་རེ་བ་ཡོངས་སུ་སྐོངས་པར་འགྱུར༌[^306]ཏེ། ངའི་མིག་ནི་ཡ་གཅིག་འདོད་པ་ལ་ཞེས་བྱ་བ་སྟེ། སློང་བ་ལ་གཉིས་སྦྱིན་པའི་དོན་ནི་འདི་ཡིན་ནོ། །

[Block 600]
ཤུགས་ཀྱིས་སྐྲག་པ་ནི་ཤུགས་ཀྱིས་སྐྲག་པ་སྟེ། རྟབས་པ༌[^307]དང་བཅས་པའི་ཤུགས་ཀྱིས་སྐྲག་པའོ། །
--- END BLOCKS ---
