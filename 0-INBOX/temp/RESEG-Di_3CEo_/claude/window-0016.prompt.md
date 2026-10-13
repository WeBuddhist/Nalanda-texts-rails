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
གཟུགས་ཅན་སྲོག་དང་སྡུག་བསྔལ་དག །ཟག་པ་དང་བཅས། དབང་པོ་གཟུགས་ཅན་བདུན་དང་། སྲོག་གི་དབང་པོ་དང་། སྡུག་བསྔལ་དང་ཡིད་མི་བདེ་བའི་དབང་པོ་དག་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 562]
དགུ་རྣམ་གཉིས། ཡིད་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་དག་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་། དབང་པོ་དགུ་པོ་དེ་དག་ནི་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་དག་གོ། །

[Block 563]
རྣམ་པར་སྨིན་པ་ཡིན་པ༌[^221]རྣམས་ནི་དུ། མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ། སྲོག་ནི་རྣམ་སྨིན་བཅུ་གཉིས་གཉིས། །བཅུ་གཉིས་གང་ཞེ་ན། ཐ་མ་བརྒྱད་དང་ཡིད་མི་བདེ། མ་གཏོགས་པ་སྟེ། དད་པ་ལ་སོགས་པ་ཐ་མ་བརྒྱད་དང་། ཡིད་མི་བདེ་བ༌[^222]མ་གཏོགས་པ་སྲོག་གི་དབང་པོ་ལས་གཞན་བཅུ་གཉིས་ནི་རྣམ་པ་གཉིས་ཏེ། རྣམ་པར་སྨིན་པ་དང་། རྣམ་པར་སྨིན་པ་མ་ཡིན་པའོ། །

[Block 564]
དེ་ལ་མིག་ལ་སོགས་པ་བདུན་རྒྱས་པ་ལས་བྱུང་བ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 565]
ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པའོ། །

[Block 566]
ཡིད་དང་སྡུག་བསྔལ་བ་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ནི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་རྣམས་དང་། སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པ་དང་། སྤྲུལ་པ་རྣམས་ནི་ཅི་རིགས་པར་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 567]
ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ཡིན་པའོ། །

[Block 568]
དབང་པོ་རྣམས་ལ་རྣམ་པར་སྨིན་པ་དང༌[^223]བཅས་པ་ནི་དུ། རྣམ་པར་སྨིན་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། གང་འདི་ཡིད་མི་བདེ་བར་བཤད་མ་ཐག་པ། དེ་གཅིག་ནི། རྣམ་པར་སྨིན་བཅས། དེ་གཅིག་པུ་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ༌[^224]ཁོ་ན་ཡིན་ནོ། །

[Block 569]
ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ན་ཞེས་བྱ་བའི་དོན་དང་། རིམ་པ་བཞིན་དུ་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 570]
བཅུ་རྣམ་གཉིས། རྣམ་པར་སྨིན་པ་དང་བཅས་པ་དག་ཀྱང་ཡིན། རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཀྱང་ཡིན་ནོ།[^225] །

[Block 571]
བཅུ་གང་ཞེ་ན། ཡིད་དང་ཚོར་གཞན་དད་ལ་སོགས། །ཚོར་གཞན་ཞེས་སྨོས་པས་ནི་ཡིད་མི་བདེ་བ་ལས་གཞན་པའི་གཟུང་ངོ་། །དེ་ལ་ཡིད་དང་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་མི་དགེ་བ་དང་། དགེ་བ་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་དག་ཡིན་ནོ། །

[Block 572]
ཟག་པ་མེད་པ་རྣམས་དང་ལུང་དུ་མ་བསྟན་པ་རྣམས་ནི༌[^226]རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 573]
སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 574]
ལུང་དུ་མ་བསྟན་པ་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །

[Block 575]
དད་པ་ལ་སོགས་པ་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་དག་ཡིན་ནོ། །

[Block 576]
ཟག་པ་མེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 577]
གཞན་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ཞེས་བྱ་བར་གྲུབ་པོ། །དགེ་བ་ལ་སོགས་པའི་དྲི་བ་ལ། དགེ་བ་བརྒྱད། དད་པ་ལ་སོགས་པ་གཅིག་ཏུ་དགེ་བ་རྣམས་སོ། །

[Block 578]
ཡིད་མི་བདེ་བ། རྣམ་གཉིས། དགེ་བ་ཡང་ཡིན། མི་དགེ་བ་ཡང་ངོ་། །ཡིད་དང་ཚོར་གཞན་ནི། རྣམ་གསུམ། དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 579]
གཞན་ནི་རྣམ་པ་གཅིག །བརྒྱད་པོ་དག་ནི་ལུང་དུ་མ་བསྟན་པ་ཁོ་ནའོ། །

[Block 580]
ཁམས་ཀྱི་དྲི་བ་ལ། དྲི་མེད་མ་གཏོགས་འདོད་པར་གཏོགས། །གཅིག་ཏུ་ཟག་པ་མེད་པ་མ་གཏོགས་པའི་ལྷག་མ་ནི་སྲིད་པས་འདོད་པར་གཏོགས་པའོ། །

[Block 581]
ཕོ་མོའི་དབང་དང་སྡུག་བསྔལ་དག །མ་གཏོགས་གཟུགས་གཏོགས། དྲི་མ་མེད་པ་ཡང་མ་གཏོགས་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྡུག་བསྔལ་དག །ཅེས་བྱ་བ་ནི་སྡུག་བསྔལ་དང་། ཡིད་མི་བདེ་བ་དག་གོ། །

[Block 582]
གཟུགས་ཅན་དང་། བདེ་བའང་མ་གཏོགས་གཟུགས་མེད་གཏོགས། །ཇི་སྐད་བཤད་པ་མ་གཏོགས་པའི་ལྷག་མ་ཅི་ཞེ་ན། ཡིད་དང་། སྲོག་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་དང་། དད་པ་ལ་སོགས་པ་ལྔ་པོ་ཡང་ངོ་། །སྤོང་བའི་དྲི་བ་ལ། ཡིད་དང་ཚོར་བ་གསུམ་རྣམ་གསུམ། །ཚོར་བ་གསུམ་ནི་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་རྣམས་སོ། །

[Block 583]
གཉིས་ཀྱིས་སྤང་བྱ་ཡིད་མི་བདེ། །ཡིད་མི་བདེ་བ་ནི་མཐོང་བ་དང་བསྒོམ་པ་གཉིས་ཀྱིས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 584]
དགུ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་ཞེས་པའི་དབང་དུ་བྱས་ཏེ། མིག་ལ་སོགས་པ་དང་བརྒྱད་པ་སྲོག་དང་སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 585]
ལྔ་པོ་ནི་སྤང་བར་བྱ་བ་ཡིན༌[^227]ཡང་། དད་པ་ལ་སོགས་པ་ལྔ་ནི་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པའི་ཕྱིར་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་མ་ཡིན་པ་ཡང་ངོ་། །གསུམ་མིན་གཞན་གསུམ་ནི་སྤང་བྱ་མ་ཡིན་པ་ཉིད་དེ། ཟག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 586 [HEADING]]
#### རྙེད་པ། ^2-1-3-0

[Block 587]
རྣམ་པའི་བྱེ་བྲག་བཤད་ཟིན་ནས་རྙེད་པ་བརྗོད་པར་བྱ་སྟེ། འདོད་པར་དང་པོ་རྣམ་སྨིན་གཉིས། །རྙེད་དེ། ལུས་ཀྱི་དབང་པོ་དང་། སྲོག་གི་དབང་པོའོ། །

[Block 588]
དེ་དག་ཀྱང་། རྫུས༌[^228]ཏེ་སྐྱེ་བས་མིན། རྫུས༌[^229]ཏེ་སྐྱེ་བ་བཀག་པས་སྒོ་ང་ལས་སྐྱེ་བ་དང་། མངལ་ནས་སྐྱེ་བ་དང་། དྲོད་གཤེར་ལས་སྐྱེས་པ་དག་གིས་རྙེད་པར་རིག་པར་བྱའོ། །

[Block 589]
ཡིད་དང་བཏང་སྙོམས་དག་ཀྱང་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་ཉོན་མོངས་པ་ཅན་ཡིན་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བ་དག་མ་ཡིན་ནོ། །

[Block 590]
ཡང་རྫུས༌[^230]ཏེ་སྐྱེ་བ་དག་གིས་དུ་ཞིག་འཐོབ༌[^231]ཅེ་ན། དེ་ཡིས༌[^232]དྲུག་གམ། གལ་ཏེ་མཚན་མ་མེད་པ་ཞིག་ཡིན་ན་སྟེ། འདི་ལྟར་བསྐལ་པ་དང་པོ་པ་རྣམས་ལྟ་བུའོ། །

[Block 591]
དེ་དག་གིས་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དང་། སྲོག་གི་དབང་པོ་རྣམས་འཐོབ་བོ། །

[Block 592]
བདུན་ནམ༌[^233]ནི། གལ་ཏེ་མཚན་གཅིག་པ་ཞིག་ཡིན་ན་སྟེ། འདི་ལྟར་ལྟ་ལ་སོགས་པ་དག་ནའོ། །

[Block 593]
བརྒྱད་ནི་གལ་ཏེ་མཚན་གཉིས་པ་ཞིག་ཡིན་ནའོ། །

[Block 594]
ཇི་ལྟར་ངན་སོང་དག་ནའོ། །

[Block 595]
རེ་ཞིག་འདོད་པའི་ཁམས་ན་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 596]
གཟུགས་ན་དྲུག་གོ། །

[Block 597]
འདོད་པའི་ཁམས་ན་མཚན་མ་མེད་པ་དག་གིས་རྙེད་པ་གང་དག་ཡིན་པ་ཉིད་དོ། །

[Block 598]
གོང་མར་གཅིག །གཟུགས་མེད་པའི་ཁམས་སུ་དང་པོ་ཉིད་དུ་སྲོག་གི་དབང་པོ་གཅིག་ཁོ་ན་རྣམ་པར་སྨིན་པ་ཐོབ༌[^234]བོ། །

[Block 599 [HEADING]]
#### གཏོང་བ། ^2-1-4-0

[Block 600]
རྙེད་པ་བཤད་ཟིན་ནས་གཏོང་བ་བརྗོད་པ།
--- END BLOCKS ---
