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
[Block 3501]
མདོ་ལས།

[Block 3502]
སྨན་གྱི་རྒྱལ་པོ་ང་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་པ་ནས་ཁ་ཏོན་བྱེད་པ་ནས་སླར་འཐོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཚིག་དེ་དང་མཐུན་པར་བྱས་ན་དེ་བཞིན་གཤེགས་པ་ཡང་རྗེས་སུ་སྐྱོབ་ཅིང་ཉན་དུ་འཛུད། མཐོང༌[^2942]བར་བྱེད་མི་བརྗེད་པར་བྱེད་དོ། །

[Block 3503]
སྤྲུལ་པས་སྤྲུལ་པ་བསྡུ་ཞིང་ཆོས་སྟོན་པའོ། །

[Block 3504 [HEADING]]
##### ཚིགས་སུ་བཅད་པ། ^4-10-6-2-0

[Block 3505 [HEADING]]
###### མོས་པར་དཀའ་བ། ^4-10-6-2-1-0

[Block 3506]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཞེས་པ་ནས་ཤིན་ཏུ་དད་པ་རྙེད་པར་དཀའ་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་བཅོ་བརྒྱད་ལ་རྣམ་པ་གསུམ་དུ་བགོས་ཏེ། ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་མོས་པར་དཀའ་བ་དང་། ཀུན་ལ་བསྙད༌[^2943]དུ་མི་རུང་བ་བསྟན། ཚིགས་བཅད་བཞིས་ནི་ཆོས་ཀྱི་སྐུ་དང་རིང་བསྲེལ་ལ་མཆོད་པས་བྱང་ཆུབ་ཏུ་ཉེ་བར་བསྟན་པ་དང་། ཚིགས་བཅད་བཅུ་གསུམ་གྱིས་ནི་ཆོས་འཆད་པའི་ཚུལ་བསྟན་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 3507 [HEADING]]
###### ཆོས་ཀྱི་སྐུ་དང་རིང་བསྲེལ་ལ་མཆོད་པས་བྱང་ཆུབ་ཏུ་ཉེ་བ། ^4-10-6-2-2-0

[Block 3508]
མདོ་ལས།

[Block 3509]
ཇི་ལྟར་ལ་ལ་ཆུ་འདོད་པ། །ཞེས་པ་ནས། འདི་ནས་ཆུ་ལའང༌[^2944]རིང་མ་ཡིན། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་འདི་བཞིས་ནི་ཆོས་ཀྱི་སྐུ་རིང་བསྲེལ་དུ་བསྒྱུར་བ་ལ་བསྟི་སྟང་བྱས་པས་བྱང་ཆུབ་ཏུ་ཉེ་བ་བསྟན་པ༌[^2945]སྟེ། དཔེ་དང་དོན་ཅི་ལེགས་པར་སྦྱར་རོ། །

[Block 3510]
མདོ་ལས།

[Block 3511]
དེ་བཞིན་དེ་དག་རྒྱང་རིང་བ། །ཞེས་པ་ནས། ཆུ་དང་མེ་ཞེས་བྱ་བ་བཞིན། །ཞེས་པའི་བར་དུ་ནི་སྦྱར་རོ། །

[Block 3512 [HEADING]]
###### ཆོས་འཆད་པའི་ཚུལ། ^4-10-6-2-3-0

[Block 3513]
[^2946]མདོ་ལས།

[Block 3514]
སེམས་ཅན་རྣམས་ལ་ཞེས་པ་ནས་མཆོད་པ༌[^2947]བྱེད་ཅེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་བཅུ་གསུམ་པོ༌[^2948]འདིས་ཆོས་འཆད་པའི་ཚུལ་བསྟན་ཏེ། དེ་ལ་ཚིགས་བཅད་བཅུ་གཅིག་གིས་ནི་ཚུལ་ཉིད་བསྟན། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཉན་པ་དང་འཆད་པ་བསྟན་ཏོ། །

[Block 3515]
མདོ་ལས་འཁོར་རྣམས་ལ་ཡང་ཞེས་པ་ནས་སངས་རྒྱས་མཐོང་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པས་རྗེས་སུ་གཟུང་བ༌[^2949]བསྟན་ཏེ། ཚིག་གཅིག་གིས་ནི་བཟོད་པ་སྤྱོད་པ་བསྟན། ཚིགས་བཅད་གསུམ་གྱིས་ནི་གཞན་གྱི་སྤྲུལ་པས་མཆོད་པ་དང་འཁོར་བྱེད་པ་བསྟན། ཚིགས་བཅད་གཅིག་གིས་ནི་སྐྱོ་ཞིང་བསྲུང་བ་བསྟན། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ལུས་མངོན་དུ་བསྟན་ཏེ། དམིགས་པ་དྲན་པར་བྱས་པ་བསྟན། ཚིག་གཅིག་གིས་ནི་ཡོན་ཏན་དང་ལྡན་པ་ལ་མངོན་དུ་སྟོན་པ་བསྟན། ཚིག་གཅིག་གིས་ནི་འཁོར་བརྒྱད༌[^2950]རྣམས་ཆོས་ཉན་པ་བསྟན་ཏེ། དེ་དག་ཅི་རིགས་པར་སྦྱར་རོ།། །།

[Block 3516 [HEADING]]
### རིན་པོ་ཆེའི་མཆོད་རྟེན་བསྟན་པའི་ལེའུ། ^4-11-0

[Block 3517]
འདི་མན་ཆད་རིན་པོ་ཆེའི་མཆོད་རྟེན་བསྟན་པའི་ལེའུ་འཆད་དོ། །

[Block 3518]
[^2951]དེ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 3519 [HEADING]]
#### གཏན་ཚིགས། ^4-11-1-0

[Block 3520]
ལེའུ་འདིའི་གཏན་ཚིགས་དང༌[^2952]དེའི་མིང་དང་། དོགས་པ༌[^2953]བསལ་བའོ།[^2954] །གདགས་པའི་གཏན་ཚིགས་ལ༌[^2955]ཡང་རྣམ་པ་བཞི་སྟེ། ཉོན་མོངས་པ་མེད་པའི་གང་ཟག་གིས༌[^2956]ང་རྒྱལ་རྣམ་པ་གསུམ་སྤང་པའི་ཕྱིར་ཏེ། དེ་གསུམ་ནི་ཐེག་པ་ཐམས་ཅད་ཐ་དད་པར་མོས་པ་དང་། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཐ་དད་པར་མོས་པ་དང་། སྐུ་ཐ་དད་པར་མོས་པ༌[^2957]ལ་མཉམ་པ་གསུམ་གྱིས་དེ་སེལ་བར་བྱེད་དེ། མཉམ་པ་ཉིད་གསུམ་ནི་ཐེག་པ་མཉམ་པ་དང་། འཁོར༌[^2958]དང་། མྱ་ངན་ལས་འདས་པ༌[^2959]མཉམ་པས། དེ་བཞིན་གཤེགས་པའི་རིན་པོ་ཆེའི་མཆོད་རྟེན་བསྟན་པ་དང་། སྐུ་ཐ་དད་པར་མོས་པ་རྣམས་རིན་ཆེན་མང་དེ་བཞིན་གཤེགས་པའི་སྐུ་ཉིད་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་ཡང་དེ་ཡིན་ཏེ། བྱེ་བྲག་མེད་པར་བསྟན་པ་དང་། འགྲེལ་པ་ལས་བླ་ན་མེད་པ་བཅུ་བསྟན་པའི་ནང་ནས་ཞིང་རྣམ་པར་དག་པ་བསྟན་པ་བླ་ན་མེད་པ་ནི་དེ་བཞིན་གཤེགས་པ་རིན་ཆེན་མང་དང་མཆོད་རྟེན་བྱུང་བས་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པའི་སྐུ་ཐམས་ཅད་དེར་འདུས་ཤིང་། དེ་ནས་འོད་གཅིག་བཏང་བས་ཕྱོགས་ཐམས་ཅད་དུ་ཁྱབ་པར་མཛད་ཅིང་ཞིང་མ་དག་པ་དང་། དག་པ་བྱེ་བྲག་མེད་པར་དེ་བཞིན་གཤེགས་པའི་ཞིང་དག་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་དང་། དམ་པའི་ཆོས་འདི་སྟོན་ཅིང་བཞུགས་པའི་ས་ཐམས་ཅད་སྔོན༌[^2960]བྱུང་བ་དང་འདྲ་བར་རིན་པོ་ཆེའི་མཆོད་རྟེན་ཉིད་དུ་བསྟན་ཅིང་།[^2961] དམ་པའི་ཆོས་ལ་རིམ་གྲོ་བསྐྱེད་པའི་ཕྱིར་ལེའུ་འདི་བསྟན་ཏོ། །

[Block 3521 [HEADING]]
#### མིང་བཤད་པ། ^4-11-2-0

[Block 3522]
མིང་བཤད་པ་ནི་རིན་པོ་ཆེ་ལས་བྱས་པའི་མཆོད་རྟེན་ཡིན་པས་ན་རིན་པོ་ཆེའི་མཆོད་རྟེན་ནོ། །

[Block 3523]
ཡང་ན་དེ་བཞིན་གཤེགས་པ་རིན་ཆེན་མང་གི༌[^2962]མཆོད་རྟེན་ཡིན་པས་ན་རིན་པོ་ཆེའི་མཆོད་རྟེན་ནོ། །

[Block 3524 [HEADING]]
#### དོགས་པ་བསལ་བ། ^4-11-3-0

[Block 3525]
དོགས་པ་བསལ་བ་ལེའུ་འདིའི་ཕྱོགས་བཅུའི་དེ་བཞིན་གཤེགས་པ་འདུས་ཤིང་རྣམ་པར་དག་པ་བསྟན་པ་ཡིན་ན་ཅིའི་ཕྱིར་མིང་དེར་མི་གདགས། མཆོད་རྟེན་དེ་ནམ་མཁའ་ལ་འཕགས་ཤིང་ངོ་མཚར་དུ་གྱུར་པ༌[^2963]ཞིང་རྣམ་པར་དག་པ་སྟོན་པས་དཔེ་གཙོར་བྱས་ཏེ་མིང་དུ་བཏགས་པས་ཉེས་པ་མེད་དོ། །

[Block 3526 [HEADING]]
#### ཚིག་རྐྱང་པ། ^4-11-4-0

[Block 3527]
མདོ་ལས།

[Block 3528 [HEADING]]
##### མཆོད་རྟེན་བར་སྣང་ལ་འཕགས་ཏེ་བྱུང་བ། ^4-11-4-1-0

[Block 3529]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2964]ཞེས་པ་ནས་བར་སྣང་ལ་འདུག་སྟེ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་རྐྱང་པ་སྟོན་པ་ལ་རྣམ་པ་གཉིས་ཏེ་མཆོད་རྟེན་བར་སྣང་ལ་འཕགས་ཏེ་བྱུང་བ་བསྟན་པས་དམ་པའི་ཆོས་འདི་ཁྱད་པར་ཅན་དུ་བསྟན་ཏོ། །

[Block 3530]
རིན་པོ་ཆེའི་མཆོད་རྟེན་དེ་ཁ་ཕྱེ་སྟེ་བསྟན་པ་ནི་འཁོར་རྣམས་དད་པ་དང་། བསྟི་སྟང་བསྐྱེད་པའི༌[^2965]ཕྱིར་རོ། །

[Block 3531]
སྔར་ནི་རིན་པོ་ཆེའི་མཆོད་རྟེན་བསྟན་པ་ཉིད་ཀྱིས༌[^2966]ཡིད་ཆེས་པར་བསྒྲུབས། དེའི་འོག་ཏུ་སྐུ་གདུང་མངོན་པར་བསྟན་པས་ནི་ལུང་ལ༌[^2967]ཡིད་ཆེས་པ་བསྟན་ཏོ། །

[Block 3532]
རིན་པོ་ཆེའི་མཆོད་རྟེན་དེ་ལས་སིལ་སྙན་སྣ་ཚོགས་བྱུང་བ་ནི་མཆོད་རྟེན་མཐོང་བར་བསྟན་པ་དང་། ཆེ་ཆུང་གི་ཚད་བསྟན་པ་དང་། ནམ་མཁའ་ལ་འཕགས་པ་བསྟན་པ་དང་། དེའི་རྒྱན་བསྟན་པའོ། །

[Block 3533]
དེའི་དང་པོ་ལ་ཡང་ཡོན་ཏན་རྣམ་པ་གསུམ་སྟེ། བླ་ན་མེད་པ་བཅུའི་ནང་ནས་ཞིང་རྣམ་པར་དག་པ་བླ་ན་མེད་པ་བསྟན་ཏོ། །

[Block 3534]
དེ་བཞིན་གཤེགས་པ་རིན་ཆེན་མང་གི་མཆོད་རྟེན་བསྟན་པ་ཡང་དོན་རྣམ་པ་དགུ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཞིང་རྣམ་པར་དག་པ་དང་དེའི་མཆོད་རྟེན་དང་། མཆོད་རྟེན་དེའི་ཚད་དང་། མདོ་བསྟན་པ་དང་། དེ་འཛིན་ཅིང་བརྟེན་པ་དང་། དེ་བཞིན་གཤེགས་པ་གྲངས་མེད་པ་སྟོན་པ་དང་། ཞིང་མ་དག་པ་རྣམ་པར་སྤོང་བ་དང་། རིན་ཆེན་མང་བ་དང་། གདན་གཅིག་ལ་བཞུགས་པ་སྟོན་པ་སྟེ། དེ་དག་ནི་འོག་ནས་འབྱུང་བའི་དཀྱུས་དང་སྦྱར་རོ། །

[Block 3535]
མཆོད་རྟེན་དེའི་ནང་ནས་རིང་བསྲེལ་འབྱུང་བ་བསྟན་པ་ནི་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་སྐུ་མདོ་སྡེ་འདི་ལ་གནས་པ་བསྟན་པའོ། །

[Block 3536]
མཆོད་རྟེན་ནམ་མཁའ་ལ་འཕགས་པ་ཡང་དེ་བཞིན་གཤེགས་པའི་ཞིང་རྣམ་པར་དག་པ་ཡང་འཇིག་རྟེན་པའི་དགེ་བའི་རྩ་བ་ལས་ཁྱད་པར་དུ་བསྟན་པའོ། །

[Block 3537]
ལྔ་བརྒྱ་ལ་ཡང་ནམ་མཁའ་ལ་འཕགས་པ་ནི་དེ་བཞིན་གཤེགས་པ་འཁོར་བ་ཐམས་ཅད་ལས་འདས་ཏེ་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ལ་གནས་པ་བསྟན་ཏོ། །

[Block 3538]
ཡང་ན་ཐེག་པ་གཅིག་པོ་འདིར་ཐེག༌[^2968]པ་གཉིས་པ་ལས་ཁྱད་པར་དུ་འཕགས་པ་བསྟན་ཏོ། །

[Block 3539]
ནམ་མཁའ་བར་སྣང་ཞེས་པ་ནི༌[^2969]ཡང་དག་པ་སྟོང་པ་ཉིད་ལ་གནས་པ་བསྟན་ཏོ། །

[Block 3540]
མདོ་ལས་སྣ་ཚོགས་བལྟ༌[^2970]ན་སྡུག་ཅེས་པ་ནས་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཁྱབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་རྒྱན་གྱི་མཚན་ཉིད་བསྟན་ཏེ། རྒྱན་བརྒྱད་དང་། གདུགས་དང་། བ་དན་ལ་སོགས་པའོ། །
--- END BLOCKS ---
