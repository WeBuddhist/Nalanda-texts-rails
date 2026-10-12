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
དེ་བས་རྡོ་རྗེ་སློབ་དཔོན་གྱིས། །ཞེས་པ་ནི་གོང་མ་དང་འབྲེལ་ཏོ། །

[Block 562]
གླེང་གཞི་རིམ་པ་སྦྱོར་བར་བཅས། །ཞེས་པ་ནི་གླེང་བསླང་བ་ལ་སོགས་པའོ། །

[Block 563]
རྒྱན་རྣམ་པ་བདུན་བཤད་པའི་རིགས་པའོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུད་ཐམས་ཅད་ནི་རྒྱན་རྣམ་པ་བདུན་གྱི༌[^280]འཆིང་བ༌[^281]བཅིངས་ལ་རྒྱུད་ཤེས་པར་འདོད་པས་ཀྱང་དེ་ལ་བསླབ་པར༌[^282]བྱའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 564]
རྒྱན་རྣམ་པ་བདུན་ཡང་ཡིན་ལ་བཤད་པའི་རིགས་པ་ཡང༌[^283]ཡིན་ན༌[^284]དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 565]
སྒྲོན་མ་གསལ་བ་ཞེས་བྱ་བའི་འགྲེལ་བཤད་ལས་རྒྱན་རྣམ་པ་བདུན་སྤྲོས་པ་དང་བཅས་པའི་བཤད་པའོ།། །།

[Block 566 [HEADING]]
## ལེའུ་བཅུ་བདུན་གྱི་བསྡུས་པའི་དོན། ^2-0

[Block 567]
དེ་ལྟར་རྒྱན་རྣམ་པ་བདུན་གོ་རིམས༌[^285]བཞིན་དུ་བཤད་ནས། ད་ནི་ལེའུ་བཅུ་བདུན་པོ་ཉིད་ཀྱིས་བསྡུས་པའི་དོན་བཤད་པར་འདོད་ནས་ད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་གི་ཚོགས་གསུངས་ཏེ། ད་ནི་ཞེས་བྱ་བ་ནི༌[^286]སྐབས་ལ་བབ་པའི་ཚིག་གོ། །

[Block 568]
ལེའུ་བཅུ་བདུན་གྱི་བསྡུས་པའི་དོན་བཤད་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ལ་ལེའུ་བཅུ་བདུན་ནི་ལེའུ་བཅུ་བདུན་ཏེ་གཞུང་གི་ཚོགས་ཀྱི་རིམ་པར་ཕྱེ་བ་བཅུ་བདུན་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 569]
ལེའུ་བཅུ་བདུན་ཞེས་པ་ནི་བཅུ་བདུན་ཁོ་ན་སྟེ་འདི་དག་གིས་ནི་མང་བའམ་ཉུང་བ་རྣམ་པར་བཀག་པ་བསྟན་ཏོ། །

[Block 570]
ཅིའི་ཕྱིར་ཞེ་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའི་ལམ་འབྲས་བུ་དང་བཅས་པ་ནི་འདི་ཉིད་ཀྱིས་སྟོན་པར་འགྱུར་གྱི་གཞན་གྱིས༌[^287]ནི་མ་ཡིན་ནོ། །

[Block 571]
འོན་ཏེ་མ་ཡིན་ན་ཡང་ལམ་འབྲས་བུ་དང་བཅས་པར་སྟོན་པར་ནམ་ཡང་མི་འགྱུར་རོ། །

[Block 572 [HEADING]]
### ལེའུ་དང་པོ། ^2-1-0

[Block 573]
འོ་ན་ལེའུ་དང་པོ་ལས་ནི་ཅི་ཞིག་གང་གི་ཕྱིར་སྟོན་ཞེ་ན། ལེའུ་དང་པོ་ལས་ནི་ཞེས་པ་ལ་སོགས་པ་སྨོས་ཏེ། ལེའུ་དང་པོ་ནི་ཐོག་མ་ཞེས་པའི་དོན་ཏོ། །

[Block 574]
ཐོག་མའི་རིམ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 575]
དེ་ལས་ཅི་སྟོན་ཞེ་ན་རྗོད་པར་བྱེད་པ་དང་བརྗོད་པར་བྱ་བ་ནི་སྒྲའི་ཚོགས་དང་དོན་གྱི་ཚོགས་སོ། །

[Block 576]
དེའི་བདག་ཉིད་ཀྱང་གང་ཡིན་ཞེ་ན། བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་སྨོས་ཏེ་བརྗོད་པར་བྱ་བའི་བདག་ཉིད་ཀྱང་ཡིན་ལ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ཡང་ཡིན་པས་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 577]
དེའི་སྤྲུལ་པའི་དཀྱིལ་འཁོར་ཡང་གང་ཞིག་ཡིན་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་པའོ། །

[Block 578]
དེར་ཉན་པའི་སྐལ་བ་དང་ལྡན་པ་ནི་ཚོགས་ཀྱི་གང་ཟག་དང་སློབ་མའི་གང་ཟག་གོ། །

[Block 579]
དེ་ལ་ཡང་ཅི་བྱེད་ཅེ་ན། རིག་པའི་དབང་བསྐུར་བ་བྱིན་ནས་ཞེས་སྨོས་ཏེ། རིག་པའི༌[^288]དབང་ནི་རིག་པའི་དབང་སྟེ། སློབ་མའི་རིག་པའི་དབང་ནི་འདི་ལྟར་ཆུ་ལ་སོགས་པའོ། །

[Block 580]
ཡང་ན་རིག་པ་དང་བཅས་པ་ལས་བྱུང་བས་རིག་པའི་དབང་སྟེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་དབང་ངོ་། །ཡང་ན་རིག་པའི་ལྷ་མོ་དང་འབྲེལ་པས་རིག་པའི་དབང་སྟེ་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ངོ་། །ཡང་ན་རིག་པ་ཐོབ་པས་ན་རིག་པའི་དབང་སྟེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་དབང་བཞི་པའོ། །

[Block 581]
དེ་ལ་དང་པོའི་དབང་ནི་ཚོགས་ལ་སྦྱིན་པའོ། །

[Block 582]
ལྷག་མ་གསུམ་ནི་སློབ་མའི་གང་ཟག་ལ་སྦྱིན་པའོ། །

[Block 583]
དབང༌[^289]བྱིན་ནས་ཀྱང་ཅི་བྱེད་ཅེ་ན། དབང་དང་རྗེས་སུ་འབྲེལ་པའི་མན་ངག་སྟོན་པ་སྟེ། དེའི་ཕྱིར་དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དྲང་བའི་དོན་དང་ངེས་པའི་དོན་ལ་བརྟག་པ༌[^290]ནི་གོང་དུ་བསྟན་པ་ཉིད་དོ། །

[Block 584]
བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའི་སྒྲུབ་པའི་ཐབས་སོ་སོར་སྟོན་ཅིང་ཞེས་པ་ནི་དབང་རྣམ་པ་གཉིས་བསྐུར་བའི་གང་ཟག་དེ་དང་དེ་ལ་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའི་སྒྲུབ་པའི་ཐབས་མ་འདྲེས་པར་སྟོན་ཏོ། །

[Block 585]
འདིར་གང་ལ་བུམ་པའི་དབང་བསྐུར་བ་དེ་དང་དེ་ལ་ནི་བསྐྱེད་པའི་རིམ་པ་འབའ་ཞིག་ཉེ་བར་བསྟན༌[^291]ཏོ། །

[Block 586]
གསང་བའི་དབང་བསྐུར་བ་ལ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་སྤྱོད་པ་སྤྲོས་ཏེ་སྟོན་ཏོ། །

[Block 587]
དེ་བཞིན་དུ་རྡོ་རྗེ་བཟླས་པ་དང་སེམས་ལ་དམིགས་པ་འབའ་ཞིག་ཀྱང་ཉེ་བར་བསྟན༌[^292]ཏོ། །

[Block 588]
དེ་བཞིན་དུ་སྒྱུ་མ་ལྟ་བུའི་སྐུ་ཡང་ཉེ་བར་བསྟན༌[^293]ཏོ། །ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བ་ལ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་འོད་གསལ་བ་དང་ཟུང་དུ་འཇུག་པ་འབའ་ཞིག་ཉེ་བར་བསྟན༌[^294]ཏོ། །

[Block 589]
ལེའུ་དང་པོ་ལས་དེ་ཉིད་སྟོན་ནས་གཞན་དག་ལས་ཀྱང་སྟོན་ཞེ་ན། གཞན་དག་ལས་ཀྱང་སྟོན་པ་བསྟན་པའི་ཕྱིར་འོག་ནས་བཤད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འོག་ནས་བཤད་པ་ནི་ལེའུ་གཉིས་པ་ལ་སོགས་པ་སྟེ་གོང་མ་མ་ཡིན་པ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 590]
ལེའུ་བཅུ་དྲུག་པོ་ནི་དང་པོ་ལས་གཞན་པའི་ལེའུ་བཅུ་དྲུག་པོ་ཁོ་ན་ཞེས་པའི་དོན་ཏོ། །

[Block 591]
དེའི་དོན་གཞན་དག་ཀྱང་རྙེད་པ་ནི་རྫོགས་པའི་རིམ་པ་དང་ཕྲ་མོའི་ཏིང་ངེ་འཛིན་ལ་སོགས་པ་ཡང་འདིར་རྙེད་ཅེས་སྦྱར་རོ། །

[Block 592]
དེ་ལ་ཡང་འདི་ལས་གཞན་པ་ཞིག་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར། ལྷའི་རྣལ་འབྱོར་རྣམ་པ་གཉིས་པོ་ཉིད་ལ་འཇུག་ཅིང་ཞེས་པ་སྨོས་ཏེ། ལྷའི་རྣལ་འབྱོར་གཉིས་ནི་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པ་གཉིས་སོ། །

[Block 593]
འདི་ལ་གང་གིས༌[^295]ཏིང་ངེ་འཛིན་གྱི་ཡུལ་དུ་བྱེད་པ་དེ་ནི་རྣལ་འབྱོར་པའོ། །

[Block 594]
རྣལ་འབྱོར་རྣམ་པ་གཉིས་པོ་འདི་ཉིད་ཀྱང་གང་ལ་ཤེས་ཤིང་བཤད་ཅེ་ན། གསང་བ་འདུས་པའི་རྒྱུད་ཕྱི་མ་ལས་གསུངས་སོ་ཞེས་སྦྱར་རོ། །

[Block 595]
གསང་བ་འདུས་པའི་དོན་དེ་ཉིད་གཞན་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར་དོན་འདི་ཉིད་ཅེས་སྨོས་ཏེ། འདི་ཉིད་ཉེ་བར་སྟོན་ཏེ་གཞན་ནི་མ་ཡིན་ཞེས་ཤུགས་ཀྱིས་བསྟན་ཏོ། །ཇི་སྐད་བསྟན་ཞེ་ན། སངས་རྒྱས་རྣམས་ཀྱིས་ཆོས་བསྟན་པ། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པ་རྣམས་ཀྱིས་གསུངས་པའི་གཞུང་གི་ཚོགས་རྣམས་སོ། །

[Block 596]
རིམ་པ་གཉིས་ལ་ཡང་དག་གནས། །ཞེས་པ་ནི་དེ་ཐམས་ཅད་ཀྱང་རིམ་པ་གཉིས་སུ་འདུས་ཞེས་པའི་དོན་ཏོ། །

[Block 597]
རིམ་པ་གཉིས་ཉིད་གང་ཡིན་ཞེ་ན། བསྐྱེད་པ་ཡི་ནི་རིམ་པ་དང་། ཞེས་སྨོས་ཏེ་བསྐྱེད་པའི་རིམ་པ་ནི་བསྐྱེད་པའི་རིམ་པ་སྟེ། གང་གིས༌[^296]བློས་བསྐྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 598]
བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ༌[^297]ནི་དེ་ལས་སྐྱེས་པའི་སྐུའོ། །

[Block 599]
ཡང་ན་བསྐྱེད་པའི་རིམ་པ་ནི་ལྷའི་རྣལ་འབྱོར་འབའ་ཞིག་པའོ། །

[Block 600]
རྫོགས་པའི་རིམ་པ་ནི་ཕྲ་མོའི་རྣལ་འབྱོར་འབའ་ཞིག་པའོ། །
--- END BLOCKS ---
