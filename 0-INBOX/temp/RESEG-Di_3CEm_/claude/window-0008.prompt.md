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
བལྟ་བར་བགྱི་ཞེས་བྱ་བ་ནི་འཇུག་པའོ། །

[Block 282]
བྱང་ཆུབ་སེམས་དཔའི་སྨོན་ལམ་མི་སྲིད་པར་བཏབ་ན་དོན་མེད་པར་འགྱུར་རོ། །ཇི་ལྟ༌[^139]ཞེ་ན། འདི་ལྟ་སྟེ། སངས་རྒྱས་ཀྱི་ཞིང་གི་ཕྱོགས་ཆ་གཅིག་ཀྱང་རྡུལ་གཅིག་གི༌[^140]སྟེང་དུ་ཆུད་པར་བསྟན་མི་སྲིད་ན་ཇི་ལྟར་དུས་གསུམ་དུ་གཤེགས་པའི་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི༌[^141]སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཞིང་རེ་རེ་ན་ཡང་གྲངས་མེད་པའི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རེ་རེ༌[^142]ཡང་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་གྱི་དབུས་ན་བཞུགས་པས་ཀུན་དུ་གང་བ་དེ་སྙེད་དུ་རྡུལ་གཅིག་གི་སྟེང་དུ་སོ་སོར་བལྟ་ཞིང་སྨོན་པ༌[^143]ཇི་ལྟར་བྱ་ཞེས་བརྒལ་བ༌[^144]དང་། དེ་ལྟར་མ་ཡིན་ཏེ། འདི་ལྟར་བསམ་གྱིས་མི་ཁྱབ་པའི་ལས་འཇིག་རྟེན་གྱི་ཁམས་སྣ་ཚོགས་པ་བླ་འོག་སྣྲེལ༌[^145]ཞི་ལ་སོགས་པ་སྤྲུལ་པ་བཞིན་ཏེ། དེ་ལྟར་བསམ་དུ་མེད་པའི་ཡེ་ཤེས་ཀྱིས་སྤྲུལ་ན་རྡུལ་གཅིག་གི་སྟེང་དུ་ཅིའི་ཕྱིར་མི་སྲིད་དེ། བསམ་གྱིས་མི་ཁྱབ་པར་ལུང་ལས་ཀྱང་བཤད་པ།

[Block 283 [VERSE]]
མཁས་པ་དག་གིས་ས་འདི་ལ། །
ངོ་མཚར་འགྱུར་བ་ཅུང་ཟད་མེད། །
སྒྱུ་མའི་རྣམ་པར་གྱུར་པ་ལ། །
ཡ་མཚན་དུ་ནི་སུ་ཞིག་འཛིན། །

[Block 284 [VERSE]]
བསམ་གཏན་ལས་དང་ཀླུ་རྣམས་དང་། །
སངས་རྒྱས་རྣམས་ཀྱི་ཆེ་བ་ཉིད། །
འཇིག་རྟེན་མགོན་པོ་འདྲེན་པ་དེས། །
བསམ་གྱིས་མི་ཁྱབ་རྣམ་བཞིར་བཤད། །

[Block 285]
དེ་ལྟ་བས་ན་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་གསུང་རབ་ལ་མི་སྲིད་པར་འཛིན་པ་དེ་དག་ཀྱང་འདིས་ཡིད་ཆེས་པར་གྱིས་ཤིག །འཇིག་རྟེན་ན་ཡང་ཤིན་ཏུ་ཆུང་བའི་སྣོད་དུ་ཆུ་དངས་པས་གང༌[^146]བ་ལ། གཟའ་སྐར་ལ་སོགས་པ་ནམ་མཁའི་རྒྱན་ཐམས་ཅད་སྣང་བ་བཞིན་ནོ། །

[Block 286]
དེ་ལྟར་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ།

[Block 287 [VERSE]]
གཟུགས་བརྙན་བཞིན་པ་ཆོས་རྣམས་ཏེ། །
རབ་རིབ་རྨི་ལམ་མཚན་ཉིད་དེ།[^147] །
སྒྱུ་མ་སྨིག་རྒྱུ་འདྲ་བ་དང་། །
དེ་འདྲར་མ་ལུས་ཐམས་ཅད་དོ། །

[Block 288]
ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཇི་ལྟར་རྡུལ་གཅིག་གི་སྟེང་ན་བཞུགས་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 289]
དེ་ལྟར་མ་ལུས་ཞེས་བྱ་བ་ནི་མ་ལུས་པའི་ཕྱོགས་ཐམས་ཅད་དོ། །

[Block 290]
སྐྲ་ཙམ་ཁྱོན་ཞེས་བྱ་བ་ནི་སྐྲའི་ཚད་ཙམ་སྟེ། དེ་ཡང་བཤད་པར་བྱ་བ་ནི་སྐྲའི་རྩེ་མོ་ཙམ་གྱི་ཁྱོན་ཏོ། །

[Block 291]
དུས་གསུམ་ནི་དུས་གསུམ་དུ་གཤེགས་པ་རྣམས་ཀྱིའོ། །

[Block 292]
སངས་རྒྱས་རྒྱ་མཚོ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་ཞིང་རྒྱ་མཚོར་ཡང་། བསྐལ་པ་རྒྱ་མཚོར་སྤྱོད་ཅིང་རབ་ཏུ་འཇུག །ཅེས་བྱ་བ་ནི་དེ་སྲིད་དུ་བྱང་ཆུབ་ཀྱི་སྤྱད་པ་ན་མཐོང་བར་ཤོག་ཤིག༌[^148]པའོ། །

[Block 293]
སངས་རྒྱས་ཀྱི་གསུང་ལ་འཇུག་པ་དེ་གང་ཞེ་ན། གསུང་གཅིག་ཡན་ལག་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 294]
དེ་བཞིན་གཤེགས་པ་གཅིག་གིས་ཆོས་བཤད་པ་ལ་ཉན་པ་གྲངས་མེད་པ་མོས་པ་ཐ་དད་པ་དག་ལས་དོན་ཐ་དད་པ་དང་ཚིག་དང་ཡི་གེ་འབྲུ་ཐ་དད་པ་ཚད་མེད་པ་རྣམས་སུ༌[^149]གོ་བར་འགྱུར་བས་ན་རྒྱ་མཚོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་རྒྱལ་བ་དུས་གསུམ་དུ་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་དེ་བཞིན་དུ་ཆོས་བཤད་པའི་གསུང་སྒྲ་རྣམ་པར་དག་པས་ཉན་པའི་འཁོར༌[^150]གྲངས་མེད་པའི་འགྲོ་བ་རྣམས་ཇི་ལྟར་འདོད་པ་འགྲོ་བ་ལྟར་སངས་རྒྱས་ཀྱིས༌[^151]གསུང་སྒྲ་སྐྱོན་མེད་པའི་རྣ་བས་དེ་དག་གི་གསུང་སྒྲ་རྒྱ་མཚོ་ཀུན་ལ་རྟག་པར་འཇུག་པར་བྱ་སྟེ་མ་ལུས་པར་ཡིད་ལ་བྱའོ། །

[Block 295]
ལུང་ལས་ཀྱང་འདི་སྐད་དུ་གསུངས་ཏེ།

[Block 296 [VERSE]]
འཁོར་བར་འཁོར་བ་མང་པོ༌[^152]རྣམས། །
དད་པའི་རྣམ་པ་སྣ་ཚོགས་ལ། །
གསུང་གཅིག་ཏུ་ནི་བཤད་མོད་ཀྱི།[^153] །
དུ་མའི་རྣམ་པར་གོ་བར་གྱུར། །

[Block 297 [VERSE]]
བདག་ལ་ཉི་ཚེར་འཆད་དོ་སྙམ། །
འགྲོ་བ་ཀུན་གྱིས་ཇི་ལྟར་གོ། །
ཡ་མཚན་དེ་ལས་ཅི་ཞིག་ཆེ། །

[Block 298]
དེ་ལྟར་ངོ་མཚར་ཅི་ཞིག་ཡོད་པ༌[^154]འདི་ལྟ་སྟེ། །སྡོང་པོས་བརྒྱན་པའི་མདོ་སྡེ་འཕགས་པ་བྱམས་པའི་རྣམ་པར་ཐར་པ་ལས་བཤད་པ།

[Block 299 [VERSE]]
ཕྱོགས་བཅུའི་བདེ་བར་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་སྤྲིན་ལ། །
གནས་གཅིག་འདུག་ནས་རྨོངས་པ་མེད་པར་གྱུར་ཏེ་ཉན། །
བསྐལ་པ་བྱེ་བ་མང་པོར་སེམས་ཀྱིས་ངོམས་པ་མེད། །
བློ་ཆེན་རྒྱ་མཚོ་དང་ནི་མཉམ་པར་སྤྱོད་པར་ཤོག །

[Block 300]
ཚིགས་སུ་བཅད་པ་སྔ་མ་གཉིས་ཀྱིས་ནི་འཆད་པའི་ཆེ་བ་ཉིད་བསྟན་པའོ། །

[Block 301]
ཚིགས་སུ་བཅད་པ་འོག་མས་ནི་ཉན་པའི་ཆེ་བ་ཉིད་བསྟན་ཏོ། །

[Block 302]
ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་འཇུག་པ་སྟེ། །དེ་ཡང་གང་ཞེ་ན། དེ་དག་གི་ཡང་གསུང་དབྱངས་མི་ཟད༌[^155]ལ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 303]
དེ་དག་གི་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དུ་གཤེགས་པ་རྒྱལ་བ་ཐམས་ཅད་ཀྱིའོ། །

[Block 304]
ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར༌[^156]བ་ནི་དེ་ལ་འཇུག་པའོ། །

[Block 305]
མི་ཟད་པ་ནི་བགྲང་བ༌[^157]ལས་འདས་པའི་གསུང་སྒྲའོ། །

[Block 306]
དེ་ལ་བློ་ཡི་སྟོབས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་མཐུ་ཆེན་པོས་སྐད་ཅིག་ཏུ་འཇུག་ཅིང་རྟོགས༌[^158]པའོ། །

[Block 307]
ཚུལ་རྣམས་ཞེས་བྱ་བ་ནི་གང་དང་གང་གིས་ཐབས་ཀྱིས༌[^159]གང་དང་གང་ལ་ཆོས་འཆད་པ་ནི་དུས་གང་དང་ཡུལ་གང་དུ་དད་པ་སྣ་ཚོགས་ཀྱི་སེམས་ཅན་དག་ལ༌[^160]འདུལ་བར་འཇུག་པའོ། །

[Block 308]
བསྐལ་པར་འཇུག་པ་སྟེ་དེ་ཡང་གང་ཞེ་ན། སྐད་ཅིག་གཅིག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སྐད་ཅིག་མའི་ཡེ་ཤེས་གཅིག་གིས་ཕྱོགས་བཅུ་རྣམས་ཀྱིའོ། །

[Block 309]
མ་འོངས་བསྐལ་པ་ཐམས་ཅད་འཇུག་པར་ཡང་། །ཞེས་བྱ་བ་ནི་བསྐལ་པ་གཅིག་ནས་གཅིག་ཏུ་བདག་འཇུག་པའོ། །

[Block 310]
མདོར་ན། གང་ཡང་བསྐལ་པ་དུས་གསུམ་ཚད་དེ་དག །ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དུས་གསུམ་དུ་བགྲང་བ་དེ་དག་ཐམས་ཅད་སྐད་ཅིག་མའི་ཡེ་ཤེས་གཅིག་གི༌[^161]ཆ་ཤས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 311]
དེ་བཞིན་གཤེགས་པ་ལྟ༌[^162]ཞིང་དེའི་སྤྱོད་ཡུལ་ལ༌[^163]འཇུག་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། དུས་གསུམ་གཤེགས་པ་མི་ཡི་སེངྒེ་གང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་ཕྱོགས་བཅུ་དུས་གསུམ་དུ་གཤེགས་པའི་མིའི་སེང་གེ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སོ། །

[Block 312]
དེ་དག་བདག་གིས་སྐད་ཅིག་མའི་ཡེ་ཤེས་གཅིག་གིས་བལྟ་བར་བྱ་བ་ནི་མཐོང་བར་བྱ་བའོ།[^164] །

[Block 313]
དེ་དག་གི་སྤྱོད་ཡུལ་ནི་དེ་དག་གི་སྤྱོད་ཡུལ་ལོ། །

[Block 314]
སྒྱུ་མར་གྱུར་པའི་རྣམ་ཐར་སྟོབས་ཀྱིས་འཇུག །ཅེས་བྱ་བ་ནི་སྒྱུ་མར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རྣམ་པར་ཐར་པ་ཡེ་ཤེས་ཀྱི༌[^165]བདག་ཉིད་དེའི་མཐུས་རྟག་པར་འཇུག་པའོ། །

[Block 315]
སངས་རྒྱས་ཀྱི་ཞིང་མངོན་པར་སྒྲུབ་པར་འཇུག་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། གང་ཡང་དུས་གསུམ་དག་གི་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 316]
གང་ཡང་དུས་གསུམ་དག་གི་ཞིང་གི་རྒྱན་ནི་ཞིང་མང་པོ་སྟེ། དེ་དག་མངོན་པར་བསྒྲུབ་ཅེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་གྱི་སྟོབས་ཀྱིས་རྡུལ་གཅིག་གི་སྟེང་དུ་མངོན་པར་བསྒྲུབ༌[^166]པའོ། །

[Block 317]
དེ་ལྟར་མ་ལུས་ཕྱོགས་རྣམས་ཐམས་ཅད་དུ། །ཞེས་བྱ་བ་ནི་ཇི་ལྟར་མ་ལུས་པའི་ཕྱོགས་ཀྱི་རྡུལ་གྱི་སྟེང་དུ་སྒྲུབ་པ་དེ་བཞིན་དུ་ཡེ་ཤེས་ཀྱི༌[^167]སྐད་ཅིག་མ་གཅིག་གིས་ཞིང་མང་པོ་རྣམས་མངོན་པར་བསྒྲུབས༌[^168]ནས་འཇུག་པའོ། །

[Block 318]
ད་ལྟར་གྱི་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་དང་། ཚད་དང་། ཁ་དོག་དང་། དབྱིབས་དག་སོ་སོར་ཐ་དད་པ་མང་པོ་མ་འདྲེས་པ་རྣམས་ཀྱང་རྡུལ་གཅིག་གི་སྟེང་དུ་བཞག་པར་མི་རུང་ན། སོ་སོར་ཐ་དད་པ་མང་པོ་རྣམས་རྡུལ་གཅིག་གི་སྟེང་དུ་ཕྱོགས་བཅུ་མཚམས་མེད་ཅིང་མ་འདྲེས་པར་ཇི་ལྟར་གཞག་པར་བྱ།[^169] དེ་ལྟ་བས་ན་འདི་ལ་ཇི་ལྟར་ཡིད་ཆེས་པར་བྱ་སྙམ་པ་ལ། དེའི་ལན་དུ་དེ་བས་ན༌[^170]ཆོས་ཐམས་ཅད་ནི་ཡོངས་སུ་མ་རྫོགས་པ་སྟེ། ངོ་བོ་ཉིད་མེད་པ་སྒྱུ་མ་ལྟ་བུ་མ་སྐྱེས་པ། མ་འགགས་པ། སྐྲ་ཤད་འཛིངས་པ་ལྟ་བུར་ཐོག་མ་ནས་ཞི་ཞིང་རང་བཞིན་གྱིས་སེམས་ལས་འདས་པ་ལ་ཇི་ལྟར་མོས་པར༌[^171]བརྟགས་པ་ཙམ་གྱིས་འབྱུང་བ་ནི་རྣམ་པ་སྣ་ཚོགས་དུ་མའི་གཟུགས་སུ་རབ་ཏུ་བསྒོམས་པས་རྣམ་པ་མང་པོའི་ཏིང་ངེ་འཛིན་དང་། རྣམ་པར་གྲོལ་བའི་ཁྱད་པར་གྱིས་བསམ་གྱིས་མི་ཁྱབ་པའི་རྣམ་པ་སྣ་ཚོགས་མྱོང་བས་ན་དངོས་པོ་འདི་དག་བར་དུ་གསལ་བར་སྣང་ངོ་། །འཇིག་རྟེན་ན་ཡང་སྔགས་ཅུང་ཟད་ཙམ་ལས་མཐུ་སྐྱེས་པའི་མིག་འཕྲུལ་གྱིས་རབ་ཏུ་བསྒྲུབས་ན་ངོ་མཚར་དང་ལྡན་པའི་སྒྱུ་མའི་མཛེས་པ༌[^172]ཡང་སྣང་ངོ་། །དེ་ལྟ་བས་ན་འདི་དག་ཐམས་ཅད་ནི་ཇི་ལྟར་སྨྲས་པ་བཞིན་ཡིད་ཆེས་པར་བྱ་སྟེ། [^173]འདི་ལྟར་ཡིད་གཉིས་ནི་ཅུང་ཟད་ཀྱང་མ་བྱེད་ཅིག །

[Block 319]
དེ་བཞིན་གཤེགས་པ་ལ་བསྙེན་བཀུར༌[^174]བྱ་བར་འཇུག་པ་དང་བརྒྱད་དེ། དེ་ཡང་གང་ཞེ་ན། གང་ཡང་མ་བྱོན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་མ་བྱོན་པ་ནི་ཕྱི་མ་མ་འོངས་པའི་མཐར་ཐུག་པ་རྣམས་སོ། །

[Block 320]
འཇིག་རྟེན་སྒྲོན་མ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས༌[^175]ཏེ། ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དང་གཞན་ན་ནམ་མཁའི་མཐའ་ཀླས་པ་ན༌[^176]བཞུགས་པ་བགྲང་བ་ལས་འདས་པའི་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་གྱིས་སྐད་ཅིག་གིས་དུས་མཉམ་པར་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར༌[^177]རྫོགས་པར་སངས་རྒྱས་པ་སྟེ། དེ་ནས་འདི་བཞིན་དུ་དུས་མཉམ་པར་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་འགྱུར་བ་དང་། དེ་བཞིན་དུ་མྱ་ངན་ལས༌[^178]འདས་པ་སྟོན་པར་བཤད་དེ། དེ་དག་མངོན་སུམ་དུ་བྱང་ཆུབ་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
