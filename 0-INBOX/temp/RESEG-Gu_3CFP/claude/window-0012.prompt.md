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
[Block 421]
དེའི་ངོ་བོ་ནི་དེ་ཁོ་ན་ཉིད་དེ། དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 422]
གང་ཇི་ལྟ་བ་བཞིན་ཡོད༌[^263]པའི་ངང་ཚུལ་ཅན་དེ་ནི་ཇི་ལྟར་ཡོད་པ་སྟེ། ཇི་ལྟ་བ་བཞིན་ཡོད་པས་ཇི་ལྟར་ཡོད་པས་སོ།[^264] །དེའི་ངོ་བོ་ནི་ཇི་ལྟར་ཡོད་པ་ཉིད་དོ། །

[Block 423]
དེ་བཞིན་དུ་ཇི་སྙེད་ཡོད་པ་ལ་ཡང་རིག་པར་བྱ་བའོ།[^265] །དེ་ཁོ་ནའི་དོན་དེ་ཡང་ཞེས་བྱ་བ་ནི། བསྟན་པའི་མཚན་ཉིད་ཅན་གྱི་དེ་ཁོ་ནའི་དོན་རྣམ་པ་གཉིས་སོ། །

[Block 424]
རབ་ཏུ་དབྱེ་ན༌[^266]རྣམ་པ་བཞིར་རིག་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ལ། རྣམ་པ་གཉིས་པོ་དེ་ཉིད་ལས་སོ། །

[Block 425]
འཇིག་རྟེན་གྱི་གྲགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འཇིག་རྟེན་ལ་གྲགས་པ་ནི་འཇིག་རྟེན་གྱི་གྲགས་པའོ། །

[Block 426]
བརྡ་དང་ཀུན་རྫོབ་ལ་འདྲིས་པའི་རྗེས་སུ་འགྲོ་བས་ཞུགས་པའི་བློས་ཞེས་བྱ་བ་ལ། བརྡ་ནི་མིང་ངོ་། །ཀུན་རྫོབ་ནི་ཐ་སྙད་དོ། །

[Block 427]
འདྲིས་པ་ནི་དངོས་པོ་འདིའི་མིང་ནི་འདིའོ་ཞེས་བྱ་བའོ། །

[Block 428]
བརྡ་དང་ཀུན་རྫོབ་ལ༌[^267]འདྲིས་པའི་རྗེས་སུ་འགྲོ་བ་ནི་རྗེས་སུ་འགྲོ་བ་ཞེས་བྱ་བ་སྟེ། བརྡ་དང་ཀུན་རྫོབ་ལ་འདྲིས་པ་གཅིག་ནས་གཅིག་ཏུ་འོངས་པའི་བློས་མཐོང་བ་མཉམ་པ་ཉིད་དོ། །ཇི་ལྟར་དངོས་པོ་གང་ལ་ཞེ་ན། བསྟན་པར་བྱ་བ་ཉིད་དེ། སའི་དངོས་པོ་ལ་ཇི་ལྟར་མཐོང་བ་མཉམ་པ་ཡིན་ན། ས་ལ་འདི་ནི་ས་ཁོ་ན་ཡིན་གྱི་མ༌[^268]མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 429]
དེ་ལྟ་བུ་ལ་སོགས་པ་འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་དང་། ལུས་ཀྱི་ཡོ་བྱད་བཅུ་དང་། ཞིང་ལ་སོགས་པ་ཡོངས་སུ་གཟུང་བའི་དངོས་པོ་དང་། ཚོར་བ་སྟེ་ལུས་ཀྱི་ཡོ་བྱད་བཅུ་པོ་ཞིང་ལ་སོགས་པ་ལ་བརྟེན་ནས་འབྱུང་ལ། དེ་དག་ཀུན་གྱི་རྟེན་དུ་གྱུར་པ་ནི་འབྱུང་བ་ལས་གྱུར་པའོ། །

[Block 430]
དེ་དག་ཀུན་ཀྱང་ཚོར་བའི་དོན་ཏེ། དེ་ལས་རབ་ཏུ་འབྱུང་བའི་ཕྱིར། བཟང་འགྲོ་དང་ངན་འགྲོ་ལ་སོགས་པ་དེ་ལྟ་བུའི་དངོས་པོ་ཁོ་ནར་ཡོངས་སུ་གཟུང་བ་ཉིད་དོ། །

[Block 431]
སོགས་པ་སྨོས་པས༌[^269]ནི། དེ་ལས་གཞན་པ་ཡང་གཟུང་བ་སྟེ། འདི་ལྟར་མདོར་བསྡུས་ན་འདི་ནི༌[^270]ཡིན་གྱི་འདི་ནི༌[^271]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཐོང་བ་མཉམ་པའོ། །

[Block 432]
ངེས་པར་མོས་པའི་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་ནི། དངོས་པོ་ལ༌[^272]ངེས་པར་མོས་པའི་སྤྱོད་ཡུལ་ནི་དངོས་པོ་ལ་ངེས་པའི་སྤྱོད་ཡུལ་ཏེ། མོས་པས་དངོས་པོ་འདིའི་མཚན་ཉིད་ནི་ངེས་པར་འདི་ལྟར་རོ་ཞེས་དེ་ལྟར་ངེས་པར་འཛིན་པའོ། །

[Block 433]
དེ་བསྟན་པར༌[^273]བྱ་བའི་ཕྱིར་གང་འཇིག་རྟེན་གྱི་དངོས་པོ་ཐམས་ཅད་གཅིག་ནས་གཅིག་ཏུ་འོང་བའི༌[^274]མིང་གིས་ཞེས་བྱ་བས་ནི། བརྡའི་རྗེས་སུ་འགྲོ་བ་གོང་དུ་བསྟན་པའི་དོན་བརྗོད་པ་ཡིན་ནོ། །

[Block 434]
གཅིག་ནས་གཅིག་ཏུ་འོངས་པ་ཞེས་བྱ་བ་དང་། རང་གི་རྣམ་པར་རྟོག་པ་ལས་གྲགས་པ་ཞེས་བྱ་བས་ཀུན་རྫོབ་ཀྱི་དོན་བསྟན་པ་ནི་མ་བསམས་མ་དཔྱད་མ་བརྟགས་པར༌[^275]བཟུང་བ་ཞེས་བྱ་བའོ། །

[Block 435]
རིགས་པས་གྲགས་པའི་དེ་ཁོ་ན་བསྟན་པའི་ཕྱིར་རྟོག༌[^276]གེ་པ་དཔྱོད་པ་དང་ལྡན་པ་རྟོག་གེར་གཏོགས་པའི་ས་ལ་གནས་པ་རང་གི་སྤོབས་པ་ལས་བྱུང་བ་སོ་སོའི་སྐྱེ་བོ་པ་དཔྱོད་པའི་རྗེས་སུ་དཔྱོད་པ་ལ་གནས་པ་ཞེས་བྱ་བ་སྟེ། ཚིག་འདི་དག་གི་བསྡུས་པའི་དོན་ནི། རྟོག་གེ་པ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་ཚིག་གོ། །

[Block 436]
དཔྱོད་པ་དང་ལྡན་པ་དང་། རྟོག་གེར་གཏོགས་པའི་ས་ལ་གནས་པ་ཞེས་བྱ་བའི་ཚིག་གཉིས་ནི་བཤད་པའོ། །

[Block 437]
རྣམ་པར་འབྱེད་པ་ཉིད་ནི་དཔྱོད་པ་དང་ལྡན་པར་འགྱུར་ལ། དེའི་སྤྱོད་ཡུལ་ལས་མ་འདས་པ་ཉིད་ནི་རྟོག་གེར་གཏོགས་པའི་ས་ལ་གནས་པ་ཡིན་ནོ། །

[Block 438]
ཡང་རྟོག་གེར་གཏོགས་པའི་ས་གང་ཡིན༌[^277]ཞེ་ན། རང་གི༌[^278]སྤོབས་པ་ལས་བྱུང་བ་སོ་སོའི་སྐྱེ་བོ་དཔྱོད་པའི་རྗེས་སུ་དཔྱོད་པར་ཞུགས་པ་རྣམས་ཀྱི་ས་ཡིན་གྱི། དེ་ཁོ་ན་ཉིད་ཀྱི་རྗེས་སུ་ཞུགས་པའི་ས་པའི་ཡུལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 439]
དེ་ལྟར་ཚིག་གཅིག་ནི༌[^279]བསྟན་པ་ཡིན་ལ། ཚིག་གཉིས་ནི་བཤད་པ་ཡིན་པས། ཚིག་གསུམ་པ་ནི་བསྟན་པ་ཡིན། ཚིག་གསུམ་ནི་བཤད་པ་ཞེས་དེ་ལྟར་རིག་པར་བྱའོ། །

[Block 440]
རྣམ་གྲངས་གཞན་ཡང་།

[Block 441 [VERSE]]
རྟོག་གེ་རྣམ་ལྔར་རིག་བྱ་སྟེ། །
བརྟག་བྱ་རྟོག་དེའི་ངང་ཚུལ་དང་། །
སྔོན་གོམས་མངོན་སུམ་མ་བྱས་ཉིད། །
ལུང་ལ་མི་བརྟེན་པ་ཉིད་དང་། །

[Block 442]
འབད་པས་ཡིད་ལ་བྱེད་པ་དང་། །སྔ་མའི༌[^280]འཕེན་པས་ཡོངས་བཟུང་ནས།[^281] །

[Block 443 [VERSE]]
རྟོག་གེ་ལ་ནི་འདྲིས་པ་སྟེ། །
རྣམ་ལྔས་རྫོགས་པར་འདོད་པའོ། །
དེ་དག་དང་ལྡན་རྟོག་གེ་པ། །

[Block 444]
དེ་དག༌[^282]དང་ལྡན་པ་ནི་རྟོག་གེ་པ་སྟེ་ལུང་དང༌[^283]ལྡན་པ་མ་ཡིན་ནོ། །

[Block 445]
དེ་ལ་ཡིད་ལ་བྱེད་པ་ཞེས་བྱ་བ་ནི། བརྟག་པའི༌[^284]གནས་ཡིད་ལ་བྱེད་པའོ། །

[Block 446]
ཡོངས་སུ་གཟུང་བ༌[^285]ཞེས་བྱ་བ་ནི། རིགས་པའི་ཚད་མ་རྣམ་པ་གསུམ་གྱིས་ཡོངས་སུ་གཟུང་བ་སྟེ། དེ་ནི་སོ་སོའི་སྐྱེ་བོའི་ས་ན་གནས་པའོ། །

[Block 447]
ཟག་པ་མེད་པ་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་ལས་འདས་པའིའོ། །

[Block 448]
ཟག་པ་མེད་པ༌[^286]ཐོབ་པར་བྱེད་པ་ནི་སྦྱོར་བའི་ལམ་གྱི་མཚན་ཉིད་ཅན་གྱིས་སོ། །

[Block 449]
ཟག་པ་མེད་པའི་རྗེས་ལས་ཐོབ་པ་འཇིག་རྟེན་པའི་ཞེས་བྱ་བ་ནི། རྣམ་པ་གཉིས་ཀ་ཡང་འཇིག་རྟེན་པའི་སྟེ། ཟག་པ་མེད་པ་ཐོབ་པར་བྱེད་པ་དང་། ཟག་པ་མེད་པའི་རྗེས་ལས་ཐོབ་པའོ། །

[Block 450]
ཤེས་པས་སྤྱོད་ཡུལ་དུ་བྱ་བ་ཞེས་བྱ་བ་ནི་ཤེས་པ་དེས་གང་ཤེས་པར་བྱ་བའི་ཡུལ་ཏེ། དེའི་སྤྱོད་ཡུལ་ལོ། །

[Block 451]
གང་གི་ཕྱིར་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་ཞེས་བརྗོད་ཅེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། དེ་ལ་དམིགས་པས་ཞེས་བྱ་བ་ནས་བརྩམས་པ་སྟེ། དེ་ལ་དམིགས་པས་ཉོན་མོངས་པའི་སྒྲིབ་པ་ལས་ཤེས་པ་རྣམ་པར་དག་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 452]
གང་ཟག༌[^287]མེད་པའི་ཤེས་པ་དེ་འདིར་ཤེས་པ་ཞེས་བརྗོད་དེ། དེ་ལ་བསྡུ་བ་བྱས་ནས་ཉོན་མོངས་པའི་སྒྲིབ་པ་ལས་རྣམ་པར་དག་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པ་སྟེ། ཡེ་ཤེས་གང་ལ་རྣམ་པར་དག་པ་དེ་ཡོད་པའི་ཡེ་ཤེས་དེ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཡེ་ཤེས་ཏེ། དེའི་སྤྱོད་ཡུལ་ལ༌[^288]གཞན་དག་སྦྱོར་བ་དང་རྗེས་ལས་ཐོབ་པའི་ཤེས་པ་གོང་དུ་བསྟན་པ་དག་གིས༌[^289]བསྡུས་པའི་དོན༌[^290]འདི་ཡིན་ཏེ། ཉོན་མོངས་པའི་སྒྲིབ་པ་ལས་རྣམ་པར་དག་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའོ། །

[Block 453]
དེའི་ཕྱིར་ཤེས་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པ་སྟེ། དེའི་སྤྱོད་ཡུལ་ལོ། །

[Block 454]
འདི་ལྟར་བསྡུ་བར༌[^291]བྱ་སྟེ། སྒྲིབ་པ་མེད་པར་གྱུར་ན་ཕྱིས་ཡང་དག་པར་གནས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བའོ། །

[Block 455]
དེ་བས་ན་ཞེས་བྱ་བ་ནི། རྒྱུ་དེས་ནའོ། །

[Block 456]
གཉིས་དག་གམ་ཤེས་པ་རྣམ་པ་གསུམ་ཡང་རུང་སྟེ། ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་ནི་དེ་ཁོ་ན་ཉིད་ཅེས་བརྗོད་དོ་ཞེས་བྱ་བའོ། །

[Block 457]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ཞེས་བྱ་བ་ནི་ཟག་པ་མེད་པ་ཐོབ་པར༌[^292]བྱེད་པའི་ཤེས་པ༌[^293]གོང་དུ་བསྟན་པ་དེས་སོ། །

[Block 458]
མངོན་པར་རྟོགས་པར་འགྱུར་བ་དང་ཞེས་བྱ་བ་ནི། ཟག་པ་མེད་པའི་ཤེས་པ་སྟེ། གང་མངོན་པར་རྟོགས་པའི་ཤེས་པའོ། །

[Block 459]
མངོན་པར་རྟོགས་པར་འགྱུར་བའི་ཤེས་པ་ཞེས་བྱ་བ་ནི། གང་ཟག་པ༌[^294]མེད་པའི་རྗེས་ལས་ཐོབ་པའི་ཤེས་པའོ། །ཤེས་བྱ་ལ་ཤེས་པའི་གེགས་བྱེད་པ་ཞེས་བྱ་བ་ལ། ཤེས་བྱ་ལ་ཤེས་པའི་གེགས་བྱེད་ཅིང་གང་དང་ལྡན་པས་ཤེས་པར་བྱ་བ་མི་ཤེས་པ་དེ་ནི་ཤེས་བྱའི་སྒྲིབ་པ་ཞེས་བརྗོད་དེ། [^295]བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཆོས་བདག་མེད་པའི་རྗེས་ལ་འཇུག་པ་དང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་བདག་མེད་པ་ལ་རབ་ཏུ་ཞུགས་པའི་ཡེ་ཤེས་ཤིན་ཏུ་རྣམ་པར་དག་པ་སྟེ།[^296] བརྟགས་པ་བརྗོད་པའི་ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་མི་རྟོག་པ་ནི་དེ་ལ་རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 460]
དེ་ལྟར་བརྟགས་པ༌[^297]བརྗོད་པའི་ངོ་བོ་ཉིད་རྣམ་པར་མི་རྟོག་པ་གཉིས་པོ་དེས་ཤེས་བྱ༌[^298]དང་། ཤེས་པ་ནི་མཉམ་པས་མཉམ་པའི་ཡེ་ཤེས་དེའི་སྤྱོད་ཡུལ་ཏེ། ཡེ་ཤེས་དེའི་ཤེས་པར་བྱ་བའི་ཡུལ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
