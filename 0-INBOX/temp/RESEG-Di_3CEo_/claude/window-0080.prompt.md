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
[Block 2801 [VERSE]]
ལུང་མ་བསྟན་པའི་རྩ་བ་གསུམ། །
དེ་ནི་སྲེད་དང་མ་རིག་བློ། །

[Block 2802]
སྲེད་པ་དང་། མ་རིག་པ་དང་། ཤེས་རབ་ཐ་ན་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡང་རུང་སྟེ། གང་ཅུང་ཟད་དེ་ཐམས་ཅད་ནི་ལུང་དུ་མ་བསྟན་པའི་རྩ་བའོ། །

[Block 2803]
རྣམ་གཉིས་མཐར༌[^1115]འཇུག་ཕྱིར་དེ་ལས། །

[Block 2804]
གཞན་མིན། ཐེ་ཚོམ་ནི་རྣམ་པ་གཉིས་ཉིད་དུ་འཇུག་པའི་ཕྱིར་རྩ་བར་འོས་པ་མ་ཡིན་ཏེ། གཡོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2805]
ང་རྒྱལ་ནི་ཁེངས་པའི་མཚན་ཉིད་ཀྱིས་མཐོན་པོར་འཇུག་པའི་ཕྱིར་རྩ་བ་མ་ཡིན་ཏེ། ཆོས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2806]
འཇིག་རྟེན་ན་རྩ་བ་རྣམས་ནི་བརྟན་པ་དང་། འོག་ནས་གནས་པ་དག་ཡིན་པར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2807]
བཞི་ཞེས་ཉི་འོག་པ། །དེ་དག་སྲེད་ལྟ་ང་རྒྱལ་རྨོངས། །ལུང་དུ་མ་བསྟན་པའི་སྲེད་པ་དང་། ལྟ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་ནི་ལུང་དུ་མ་བསྟན་པའི་རྩ་བ་དག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། བསམ་གཏན་པ་གསུམ་མ་རིག་ལས། །

[Block 2808]
འདི་ལྟར༌[^1116]བསམ་གཏན་པ་ནི་གསུམ་སྟེ། སྲེད་པ་དང་། ལྟ་བ་དང་། ང་རྒྱལ་ཤས་ཆེ་བའི་བསམ་གཏན་དག་ཡིན༌[^1117]ལ། དེ་དག༌[^1118]ཀྱང་མ་རིག་པའི་དབང་གིས་འགྱུར་རོ། །

[Block 2809 [HEADING]]
### ལུང་དུ་མ་བསྟན་པའི་དངོས་པོ་བཅུ་བཞི། ^5-8-0

[Block 2810]
མདོ་ལས།

[Block 2811]
ལུང་དུ་མ་བསྟན་པའི་དངོས་པོ་བཅུ་བཞི་གང་གསུངས་པ་དེ་དག་ལུང་དུ་མ་བསྟན་པ་ནི་མ་ཡིན་ཏེ། གཞག་པར་བྱ་བའི་དྲི་བ་ནི༌[^1119]ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 2812]
ཅི་དེ་ཁོ་ན་ལུང་དུ་མ་བསྟན་པ༌[^1120]ཡིན་ནམ་མ་ཡིན་ཏེ། འོན་ཀྱང་རྣམ་པ་བཞི་འདི་ལྟ་སྟེ།

[Block 2813 [VERSE]]
མགོ་གཅིག་པ་དང་རྣམ་ཕྱེ༌[^1121]དང་། །
དྲི་དང་བཞག་པར་ལུང་བསྟན་པ། །
འཆི་དང་སྐྱེས༌[^1122]དང་ཁྱད་པར་འཕགས། །
བདག་གཞན་ལ་སོགས་ལྟ་བུ་ཡིན། །

[Block 2814]
ཅི་སེམས་ཅན་ཐམས་ཅད་འཆི་བར་འགྱུར་རམ་ཞེས་འདྲི་ན་འཆི་བར་འགྱུར་རོ་ཞེས་མགོ་གཅིག་ཏུ་ལུང་བསྟེན༌[^1123]པར་བྱའོ། །

[Block 2815]
ཅི་སེམས་ཅན་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་རམ་ཞེས་འདྲི་ན། ཉོན་མོངས་པ་ཅན་རྣམས་ནི་སྐྱེ་བར་འགྱུར་གྱི་ཉོན་མོངས་པ་མེད་པ་རྣམས་ནི་མ་ཡིན་ནོ་ཞེས་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་བྱའོ། །

[Block 2816]
ཅི་མི་འདི་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནམ་དམན་པ་ཡིན་ཞེས་འདྲི་ན་ལྷའམ་ངན་སོང་གང་ལ་ལྟོས༌[^1124]ཏེ་འདི༌[^1125]ཞེས་དྲིས་ནས་ལུང་བསྟན་པར་བྱའོ། །

[Block 2817]
ཅི་ཕུང་པོ་རྣམས་ལས་སེམས་ཅན་གཞན་ནམ་གཞན་མ་ཡིན་ཞེས་འདྲི་ན། སེམས་ཅན་གྱི་རྫས་མེད་པའི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 2818 [HEADING]]
### དངོས་པོ་དེ་དང་ལྡན་པ། ^5-9-0

[Block 2819]
གང་ཟག་གང་གི་ཕྲ་རྒྱས་གང་ཞིག་དམིགས་པ་གང་ལ་རྒྱས་པར་འགྱུར་བ་དེ་ནི་དེས་ན་དེ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 2820]
འདས་པ་ནི་གང་དང་ལྡན་པ་ཞེས་བྱ་བ་ནས། ད་ལྟར་བ་ནི་གང་དང་ལྡན་པ་ཞེས་བྱ་བའི་བར་འདི་དག་གང་ཞེ་ན། སྨྲས་པ།

[Block 2821 [VERSE]]
འདས་དང་ཉེར་གནས་འདོད་ཆགས་དང་། །
ཁོང་ཁྲོ་ང་རྒྱལ་དག་གིས་ནི། །
གང་ལ་དེ་སྐྱེས་མ་སྤངས་པའི། །
དངོས་པོ་དེ་དང་ལྡན་པ་ཡིན། །

[Block 2822]
དངོས་པོ་གང༌[^1126]ལ་འདས་པ་དང་ད་ལྟར་བྱུང་བའི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། ང་རྒྱལ་རྣམས་སྐྱེས་པ་མ་སྤངས་པ༌[^1127]དེ་དག་གིས་དངོས་པོ་དེ་དང་ལྡན་ཏེ། དེ་དག་ནི་རང་གི་མཚན་ཉིད་པའི་ཉོན་མོངས་པ་ཡིན་པའི་ཕྱིར་གདོན་མི་ཟ་བར་ཐམས་ཅད་ལ་ཐམས་ཅད་དུ་འབྱུང་བ་མ་ཡིན་ནོ། །

[Block 2823]
ཡིད་ཀྱི་དེ་དག་མ་འོངས་པས། ཀུན་དང་། གང་ལ་དེ་སྐྱེས་པ༌[^1128]མ་སྤངས་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཡིད་ཀྱི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་མ་འོངས་པ་དེ་དག་ཉིད་ཀྱིས་དུས་གསུམ་པའི་དངོས་པོ་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 2824]
གཞན་གྱིས་རང་དུས་པ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་གཞན་དག་གིས་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་མ་འོངས་པའི་དངོས་པོ་ཁོ་ན་དང་ལྡན་ནོ། །

[Block 2825]
སྐྱེ་བའི་ཆོས་རྣམས་ཀྱིས་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2826]
དེ་དག་ཉིད། མི་སྐྱེ་རྣམས་ཀྱིས་ཐམས་ཅད་དང་། །མི་སྐྱེ་བའི་ཆོས་རྣམས་ཀྱིས་དུས་གསུམ་པའི་དངོས་པོ་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 2827]
ལྷག་མ་ཀུན་གྱིས་ཀུན་དང་ལྡན། །ལྟ་བ་དང་། ཐེ་ཚོམ་དང་མ་རིག་པ་རྣམས་ཀྱིས་དངོས་པོ་ཐམས་ཅད་དང་ལྡན་ཏེ། ཉོན་མོངས་པ་སྤྱི་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2828 [HEADING]]
#### འདས་པ་དང་མ་འོངས་པའི་དངོས་པོ་རྫས་སུ་ཡོད་པ། ^5-9-1-0

[Block 2829]
ཅི་འདས་པ་དང་མ་འོངས་པའི་དངོས་པོ་རྫས༌[^1129]སུ་ཡོད་དམ། འོན་ཏེ་མེད། གལ་ཏེ་ཡོད་ན་ནི་དུས་ཐམས་ཅད་དུ་ཡོད་པའི་ཕྱིར་རྟག་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2830]
འོན་ཏེ་མེད་ན་ཇི་ལྟར་དེ་དང་ངམ། དེས་ལྡན་པའམ། བྲལ་བ་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པའི་ཕྱིར་འདུས་བྱས་རྣམས་རྟག་པ་ཉིད་དུ་དམ་མི་འཆའི། དུས་རྣམས་ཀུན་དུ་ཡོད་པར་ནི་གསལ་བར་དམ་འཆའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གསུངས་ཕྱིར། བཅོམ་ལྡན་འདས་ཀྱིས་གལ་ཏེ་འདས་པའི་གཟུགས་ཞིག་ཡོད་པར་མ་གྱུར་ན། འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་འདས་པའི་གཟུགས་ལ་མི་ལྟ་བར་ཡང་མི་འགྱུར་བ༌[^1130]ཞིག་ན། གང་གི་ཕྱིར་འདས་པའི་གཟུགས་ཡོད་དོ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 2831]
གཉིས་ཕྱིར། རྣམ་པར་ཤེས་པ་ནི་གཉིས་ལ་བརྟེན་ནས་སྐྱེའོ༌[^1131]ཞེས་གསུངས་པ་གང་ཞེ་ན། མིག༌[^1132]དང་གཟུགས་རྣམས་ནས་ཡིད་དང་ཆོས་ཀྱི་བར་ཡིན་ནོ། །

[Block 2832]
ཡུལ་ཡོད་ཕྱིར། འདས་པ་དང་མ་འོངས་པ་མེད་ན་དེ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་ནི་ཡུལ་མེད་པར་འགྱུར་གྱི་ཡུལ་དང་མི་ལྡན་ནོ། །

[Block 2833]
འབྲས་ཕྱིར། གལ་ཏེ་འདས་པ་ཞིག་མེད་ན་ཚེ་ཕྱི་མ་ལ་འདས་པའི་ལས་ཀྱི་འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 2834]
དེའི་ཕྱིར་འདས་པ་དང་མ་འོངས་པ་ཡོད་དོ། །

[Block 2835]
ཡང་འདི་ལྟར། དེ་ཡོད་སྨྲ་བའི་ཕྱིར་ཐམས་ཅད། །ཡོད་པར་སྨྲ་བར་འདོད། གང་དག་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དེ་དག་ནི༌[^1133]ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་ཡིན་ནོ། །

[Block 2836]
གཞན་ནི་རྣམ་པར་ཕྱེ་སྟེ་སྨྲ་བ་ཡིན་ནོ། །

[Block 2837]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དེ་དག་ཀྱང་དུ་ཞིག་ཅེ་ན། སྨྲས་པ། དེ་དག །

[Block 2838 [VERSE]]
རྣམ་བཞི་དངོས་དང་མཚན་ཉིད་དང་། །
གནས་སྐབས་གཞན་གཞན་འགྱུར་ཞེས་བྱ། །

[Block 2839]
དངོས་པོ་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་ཆོས་སྐྱོབ་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་དངོས་པོ་གཞན་དུ་འགྱུར་གྱི་རྫས་གཞན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་གསེར་གྱི་སྣོད་བཅོམ་ནས་གཞན་དུ་བྱེད་པ་ནི་དབྱིབས་གཞན་དུ་འགྱུར་བ་བཞིན་ནོ། །

[Block 2840]
མཚན་ཉིད་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་དབྱངས་སྒྲོགས་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་འདས་པའི་མཚན་ཉིད་དང་ལྡན་ལ་གཉིས་དང་ནི་མི་ལྡན་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
