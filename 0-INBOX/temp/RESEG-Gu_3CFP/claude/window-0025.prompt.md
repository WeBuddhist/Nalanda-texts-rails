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
[Block 876]
བསམ་པར་བྱ་བ་མ་ཡིན་པ་ནི་མི་བསམ་པ་སྟེ། དེའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ༌[^661]བསམ་པར་མི་ནུས་པ་དང་། བསམ་པར་མི་འོས་པའོ། །

[Block 877]
གནས་གང་ལ་ཡིན་ན་ཆོས་རྣམས་བསམ་པ་ལས་རྩོམ་པར་བྱེད་དེ། རྒྱས་པར་བསམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 878]
རྟག་ཏུ་གུས་པར་བྱེད་པའི་སྦྱོར་བ་སེམས་པས་རྟག་ཏུ་གུས་པར་བྱེད་པའི་སྦྱོར་བའི་མི་མཐུན་པའི་ཕྱོགས་ནི་ལྷོད་ལ། དེའི་གཉེན་པོའི་ཕྱོགས་ནི་ལྷོད་པར་མི་བྱེད་དོ། །

[Block 879]
སྤྱོད༌[^662]པར་བྱེད་ཅིང་ཞེས་བྱ་བ་ནི་འདི་ལྟར་རིགས་ལ་འདི་ལྟར་ནི་མི་རིགས་པའོ་ཞེས་རྗེས་སུ་ཞུགས་ཤིང་དེ་ལྟར་སྦྱོར་བའོ། །

[Block 880]
ནག་པོ་བསྟན་པ་དང་ཆེན་པོ་བསྟན་པ་རྣམས་ཀྱང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནི། གང་མདོ་སྡེ་ལ་འཇུག་ཅིང་འདུལ་བ་ལ་སྣང་ལ། ཆོས་ཉིད་དང་མི་འགལ་བ་དེ་ནི་ཆེན་པོ་བསྟན་པ་ཡིན་ལ། དེ་ལས་བཟློག་པ་ནི་ནག་པོ་བསྟན་པའོ། །

[Block 881]
ཐོག་མ་འཇུག་པ་ནས་ཞེས་བྱ་བ་ནི་སྔོན་མ་ཞུགས་པར་སེམས་པ་ལས༌[^663]འཇུག་པ་ནི་ཐོག་མ་འཇུག་པའོ། །

[Block 882]
རྨོངས་པར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་བསམ་པར་མི་ནུས་པའི༌[^664]སེམས་པའོ། །

[Block 883]
སེམས་གཡེང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་བསམ་པར་མི་འོས་པ་མི་སེམས་པའོ། །

[Block 884]
སྔོན་མ་རྟོགས༌[^665]པའི་དོན་ཁོང་དུ་ཆུད་ཅིང་ཐོབ་པར་འགྱུར་བའམ། ཐོས་པ་སྔོན་དུ་འགྲོ་བས་རྟོགས་པ་ནི་མངོན་པར་ཤེས་པའམ། སྔར་མ་ཐོབ་པ་ཐོབ༌[^666]པས་ན་དེ་དག་གཉི་ག་རྟོགས་ཤིང་ཐོབ་པ་སྟེ། རིམ་པ་བཞིན་དུ་དེས་ཤེས་པ་རབ་ཏུ་ཐོབ་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆུད་ཟ་བར་མི་འགྱུར་ཏེ་བརྗེད་པར༌[^667]མི་འགྱུར་ཞེས་བྱ་བ་དེ་གཉི་ག་ཉིད་ལ་གོ་རིམ་བཞིན་ནོ། །

[Block 885]
གཞན་གྱི་དྲིང་མི་འཇོག་པ་ཞེས་བྱ་བ་ནི་གཞན་ལ་མི་ལྟོས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 886]
མ་སྨས་ཤིང་མི༌[^668]ཉམས་པར་ཏེ། མ་འོངས་པ་དང་མཐོང་བའི་ཆོས་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་འཛིན་པ་ལ་མཁས་པ་ན་ནག་པོ་བསྟན་པ་ལ་མཁས་པ་ཡིན་པ་ཉིད་ཀྱིས་བསྐྱོད་པར་མི་ནུས་ཏེ། མི་མཐུན་པའི་ཕྱོགས་ལ་ཞུགས་པར༌[^669]མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 887]
བསྒུལ་བར་ཡང་མི་ནུས་ཏེ། ཆེན་པོ་བསྟན་པ་ལ་མཁས་པའི་ཕྱིར་རོ། །

[Block 888]
ཕྱོགས་ལས་བཟློག་པར་མི་ནུས་པ་ཉིད་ནི་སུས་ཀྱང་ཞེས་བྱ་བ་སྟེ། ཐོས་པ་མང་པོ་དག་གིས་སམ། འཇིག་རྟེན་ན་ཤེས་རབ་ཆེ་བར་འདོད་པ་དག་གིས་སམ། རྒན་རབས་སོ། །

[Block 889]
ཇི་ལྟར་ཡང་ཞེས་བྱ་བ་ནི་ལུང་དག་གིས་སམ། རིགས་པ་དག་གིས་སོ། །

[Block 890]
བསམ་པ་རྣམ་པ་བརྒྱད་ཀྱི༌[^670]བསྡུས་པའི་དོན་ནི་གང་བསམ་པ་དང་། དེ་ཇི་ལྟར་བསམ་པར་བྱ་བ་དང་། གང་གི་དོན་དུ་བསམ་པ་སྟེ། བསམ་པ་ནི་ཆོས་སོ། །

[Block 891]
ཇི་ལྟར་བསམ་ན་རྒྱས་པ་ལ་སོགས་པ་རྣམ་པ་ལྔས༌[^671]སོ། །གང་གི་དོན་དུ་ཞེ་ན། སེམས་པས་འཇུག་པར་བྱ་བའི་དོན་དང་། བཟོད་པ་ཐོབ་པ༌[^672]དེ་ཉིད་སྙིང་པོར་བྱ་བའི་དོན་དང་བསྒོམ་པ་ལ་ཞུགས་པའི་དོན་ཏོ། །

[Block 892]
མདོར་བསྡུས་པ་ནི་རྣམ་པ་གང་གིས་ཅི་ལ་བརྟེན་ཞིང་གང་ལ་བརྟེན་ནས་ཅི་ཞིག་ཤེས་པའོ། །

[Block 893]
ཅི་ལ་བརྟེན་ནས༌[^673]རིགས་པའམ་ལུང་གིས་ལུས་དང་ངག་དང་ཡིད་ཀྱིས་རྗེས་སུ་ཞུགས་པས། གང་ལས་ལོག་པའི་ངང་ཚུལ་དང་། ཞུགས་པའི་ངང་ཚུལ་གྱིས་རྗེས་སུ་ཞུགས་པ་བརྟེན་པ་དེ་ལ་རབ་ཏུ་གནས་སམ།[^674] བསམ་པ་དང་བསྒོམ་པ་ལ་སྦྱོར་བར་བྱེད་དེ། འདི་ནི་འདིའི་གོ་རིམ་མོམོ། །

[Block 894]
སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་ལ། སྤྲོས་པ་ནི་རྣམ་པར་རྟོག་པ་སྟེ། ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་ལ་སོགས་པའོ། །

[Block 895]
ཡོངས་སུ་གཡེང་བ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གཡེང་བ་ཐམས་ཅད་དང་བྲལ་བའོ། །

[Block 896]
འདུ་ཤེས་ཡིད་ལ་བྱེད་པ་ནི་འདུ་ཤེས་ཡིད་ལ་བྱེད་པ་ནང་གི་ཏིང་ངེ་འཛིན་གྱིས་མཚན་མ་རྣམས་ལ་ཞེས་བྱ་བ་ནས་རྒྱས་པར་སེམས་འཇོག་ཅིང་ཤིན་ཏུ་འཇོག་པ་ནས་རྩེ་གཅིག་ཏུ་བྱེད་ཅིང་མཉམ་པར་འཇོག་པའི་བར་འདི་ནི་ཞི་གནས་ཞེས་བྱ་བའོ། །

[Block 897]
མཚན་མ་ཡིད་ལ་བྱེད་ཅིང་འབྱེད་པ་ནས་ཤེས་རབ་ཀྱིས༌[^675]འཇུག་པ་ཞེས་བྱ་བའི་བར་ལ། དེ་ལ་འབྱེད་པ་ནི་སྡུག་བསྔལ་མ་ལུས་པར་བསྡོམས༌[^676]ནས་སྡུག་བསྔལ་འཕགས་པའི་བདེན་པ་ཞེས་བྱ་བའོ། །

[Block 898]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ཞེས་བྱ་བ་ནི་སོ་སོར་བྱ་བའི་ཆ་འཛིན་པ་སྟེ། དཔེར་ན་སྐྱེ་བ་སྡུག་བསྔལ་རྒ་བ་སྡུག་བསྔལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 899]
ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ནི་དེ་ལ༌[^677]བརྟེན་ནས་མདོ་སྡེ་ལ་སོགས་པའི་ཆོས་རྣམས་རྣམ་པར་འབྱེད་པ་སྟེ། འདི་ལྟར་དེ་ལ་བརྟེན་ནས་སྔ་མ་གཉིས་འབྱེད་པ་སྟེ། དེ་ལ་འབྱེད་པ་ནི་ངེས་པར་གཟུང་བའི་མཚན་ཉིད་དོ། །

[Block 900]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ནི་ཡང་དག་པར་ངེས་པར་གཟུང་བའི་མཚན་ཉིད་དོ། །

[Block 901]
ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ནི་ཉེ་བའི་མཚན་ཉིད་ངེས་པར་བཟུང༌[^678]བའོ། །

[Block 902]
དེ་ལ་སྔ་མས་ནི་ལམ་ཚོལ་བ་ཡིན་ལ་འདི་ནི་ལམ་རྣམ་པར་ངེས་པའོ། །

[Block 903]
རྣམ་གྲངས་གཞན་ཡང་མཚན་ཉིད་ནི་ཤེས་བྱའི་དངོས་པོ་ཡིད་ལ་བྱེད་པ་མ་སྤངས་པའོ། །

[Block 904]
ཡང་དག་པའི་མཚན་ཉིད་ནི་ཀུན་དུ་གཏད་ནས་ཚོལ་བའོ། །

[Block 905]
ཉེ་བའི་མཚན་ཉིད་ནི་བཙལ་བ་རྣམ་པར་ངེས་པར་འབྱེད་པའོ། །

[Block 906]
བསྙེན་པ་ནི་རྣམ་པར་འབྱེད་པའི༌[^679]ལུས་ཀྱི་ཤེས་བྱའི་དངོས་པོ་རབ་ཏུ་རྟོགས་པའོ། །

[Block 907]
རྣམ་གྲངས་གཞན་ཡང་བསྙེན་པ་ནི་རང་གི་མཚན་ཉིད་ཡང་དག་པར་སོ་སོར་རིག་པའོ། །

[Block 908]
རིག་པའི་སྤྱིའི་མཚན་ཉིད་ཀྱིས་ཇི་སྙེད་ཡོད་པ་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་འཛིན་པའོ། །

[Block 909]
སྔོན་དང་ཕྱི་མ་དག་ཏུ་ཡང་དང་ཡང་དུ༌[^680]འཕེལ་ཞིང་རྒྱས་པ་ནི་རྟོགས་པ་སྟེ། སྔོན་དང་ཕྱི་མའི་དོན་མི་བརྗོད་པའོ། །

[Block 910]
བློ་ནི་རབ་ཏུ་རྣམ་པར་འབྱེད་པར་ནུས་པའི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་བོ། །

[Block 911]
མཁས་པ་ནི་ཀུན་དུ་བརྟགས་པའི་ཤེས་རབ་གང་ཡིན་པའོ། །ཤེས་རབ་ཀྱིས༌[^681]འཇུག་པ་ནི་བསྟེན་པ་དང་། བརྗོད་པ་དང་། ཡོངས་སུ་དྲི་བ་དང་། འཕེལ་བའི་གཏམ་གཏན་ལ་དབབ་པ་ལས་ཀུན་དུ་ཤེས་པའི་དོན་ཁྱད་པར་ཅན་དུ་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་ནི་ཤེས་རབ་པོ། །ལུས་ཤིན་ཏུ་སྦྱངས་པ་ནི་ལུས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 912]
སེམས་ཤིན་ཏུ་སྦྱངས་པ་ནི་སེམས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 913]
གནས་ངན་ལེན་བསལ་བར་བྱ་བ༌[^682]ཞེས་བྱ་བ་ལ། གནས་ངན་ལེན་ཞེས་བྱ་བ་ནི་རྟེན་ལ་ཡོད་པའི་ཉོན་མོངས་པའི་ས་བོན་ནོ། །

[Block 914]
ཡེ་ཤེས་ནི་ལྐོག་ཏུ་གྱུར་པ་རྗེས་སུ་འཛིན་པའོ། །

[Block 915]
མཐོང་བ་ནི་མངོན་སུམ་གྱི་རྫས་འཛིན་པའོ། །
--- END BLOCKS ---
