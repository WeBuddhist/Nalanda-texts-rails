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
[Block 3186]
མདོ་ལས་མཚན་མས༌[^2697]ངལ་སོས་པར་ཤེས་ནས་ཞེས་པ་ནས་ཁྱེད་འདོང་ངོ་ཞེས་པའི་བར་དུ་ནི། དཔེ་རྣམ་པ་གཉིས་ལ་འདི་ནི་ངེས་པའི་དོན་བསྟན་ཏེ། སྔར་ནི་སྤྲུལ་པ་བསྟན། ཕྱིས་ནི་ཡང་དག་པ་བསྟན་ཏེ། སྤྲུལ་པའི་གྲོང་ཁྱེར་ཞེས་པ་ནི་ཐེག་པ་རྣམ་པ༌[^2698]གཉིས་ཀྱི་གནས་ཏེ༌[^2699]བསྟི་བའི་གནས་དེ་བསྟི་བའི༌[^2700]གནས་དང་འདྲ་བར་བསྟན་པ༌[^2701]ཡིན་གྱི། ཐེག་པ་ཆེན་པོ་རིན་པོ་ཆེའི་འབྱུང་གནས་དེ་ནས་ཉེ་ཞེས་པར་དཔེ་སྨྲས་པ་ཡིན་ནོ། །

[Block 3187 [HEADING]]
##### དཔེ་དང་དོན་དུ་སྦྱར་བ། ^4-7-10-3-0

[Block 3188]
མདོ་ལས་དེ་བཞིན་དུ་དགེ་སློང་རྣམས་ཞེས་པ་ནས་སྤང་བར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་དོན་ཕྱི་མ་དེང༌[^2702]སྦྱར་བ་སྟེ། སྔར་ནི་དྲང་བ་དང་སྦྱར་ཕྱིས་ནི་ངེས་པ་དང་སྦྱར་ཏེ། འཁོར་བ་དང་སྡུག་བསྔལ་ལས་རྒལ་བ༌[^2703]དང་སྤངས་པའོ། །

[Block 3189]
མདོ་ལས་དེ་ནས་སེམས་ཅན་འདི་དག་ཅེས་པ་ནས་མི་རུང་གི་ཞེས་པའི་བར་དུ་ནི་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའི༌[^2704]སྤྱོད་པ་དཀའ་བ་ལ་སེམས་ཞུམ་པ་བསྟན་པའོ། །

[Block 3190]
མདོ་ལས་དེ་བཞིན་གཤེགས་པས་ཞེས་པ་ནས་ས་གཉིས་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་དང་དོན་དུ་སྦྱར་བ་སྟེ། ས་གཉིས་ཞེས་པ་ནི་དབང་པོ་གཉིས་ཀྱིས་བསླབ་པར་བྱ་བ་དང་། ཡེ་ཤེས་གཉིས་པས་ཆུད་པར་བྱ་བའི་སའོ། །

[Block 3191]
མདོ་ལས་དགེ་སློང་རྣམས་གང་གི༌[^2705]དུས་ན་ཞེས་པ་ནས་ཐབས་མཁས་པའོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་འོག་མས་ངེས་པའི་དོན་དང་སྦྱར་བ་སྟེ། བྱ་བ་མ་བྱས་ཞེས་པ་ནི་སྐྱེ་བའི་ལྷག་མ་ལུས་པའོ། །

[Block 3192]
གང་སྐྱེ་བའི་ལྷག་མ་ལུས་པ་ནི་ཚངས་པར་སྤྱོད་པ་མ་སྤྱད་པས༌[^2706]མཐར་མ་ཕྱིན་པ་དང་སྦྱར་རོ། །

[Block 3193]
ལྟོས་ཤིག༌[^2707]རྟོགས་ཤིག་པ་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་གི་ཡེ་ཤེས་ལ་འཇུག་པའོ། །

[Block 3194 [HEADING]]
#### བསྡུ་བ། ^4-7-11-0

[Block 3195 [HEADING]]
##### སྔོན་གྱི་རྒྱུ། ^4-7-11-1-0

[Block 3196]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་རྒྱལ་བ་དེ་ལ་མཆོད་ཅིང་བཀུར་སྟི་བྱེད་ཅེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་བཞི་བཅུ་རྩ་དགུ་ལས་སུམ་ཅུ་རྩ་ཕྱེད་དང་གཅིག་གིས་ནི་སྔོན་གྱི་རྒྱུ་བསྟན། དེའི་འོག་མ་རྣམས་ཀྱིས་ནི་ད་ལྟར་གྱི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3197]
མདོ་ལས།

[Block 3198]
དེ་ནས་རྒྱལ་བས་སྡུག་བསྔལ་བ། །ཞེས་པ་ནས། ཚངས་པའི༌[^2708]གཞལ་མེད་ཁང་རྣམས་རབ་ཏུ་བསྐྱོད། །ཅེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གསོལ་བ་སྟེ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3199]
མདོ་ལས་ཤར་ཕྱོགས་སུ་བྱེ་བ་སྟོང་ཕྲག་ནི་ཞེས་པ་ནས། མི་ཡི་འཆི་བདག༌[^2709]དེ་ཡང་ཤེས་པར་བྱ། །ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གསོལ་བ་དང་། ཡང་དག་པར་སྟོན་པ་འཆད་པ་དང་། སེམས་ཅན་རྣམས་ཀྱིས་ཕན་པ་ཐོབ་པའོ། །

[Block 3200]
མདོ་ལས།

[Block 3201]
དེ་ཡི་ཆོས་རྣམས་བཤད་མ་ཐག་ཏུ་ནི། །ཞེས་པ་ནས་དེ་དག་མཐར་མི་ཕྱིན་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་གྱི་ཕན་པ་ཐོབ་པ་བསྟན་ཏོ། །

[Block 3202]
མདོ་ལས།

[Block 3203]
རྒྱལ་བུ་བཅུ་དྲུག་དེ་དག་ཀྱང་། །ཞེས་པ་ནས། ཇི་ལྟར་དཔའ་བོ༌[^2710]སྤྱན་གཙང་ཁྱོད་བཞིན་དུ། །ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་སྲས་ཀྱི་རྒྱུད་བསམ་པ༌[^2711]བསྟན་ཏེ། མདོ་ལས་འབྱུང་བ་བཞིན་དུ་གོ་བར་གྱིས་ཤིག

[Block 3204]
།མདོ་ལས།

[Block 3205]
རྒྱལ་བ་དེས་ནི་དེ་དག་བསམ་མཁྱེན་ནས། །ཞེས་པ་ནས། དགེ་སློང་གནས་བརྟན༌[^2712]འཇིགས་པར་མ་བྱེད་ཅིག །ཅེས་པའི་བར་དུ་ནི་ཚིག་ལྷུག་པ༌[^2713]དང་སྦྱར་ཞིང་གོ་བར་གྱིས་ཤིག

[Block 3206 [HEADING]]
##### ད་ལྟར་གྱི་འབྲས་བུ། ^4-7-11-2-0

[Block 3207]
།མདོ་ལས།

[Block 3208]
ཇི་ལྟར་དགོན་པ་མ་རུངས་འཇིགས་པར༌[^2714]འགྱུར།[^2715] །ཞེས་པ་ནས། དགོན་པ་མྱ་ངན་རབ་ཏུ་འཇིགས་པ་ཡི།[^2716] །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བཅུ་དགུས་འབྲས་བུ་ཐོབ་པ༌[^2717]དང་། བཀྲི་བའི་དོན་སྤངས་ཤིང་ངེས་པའི་དོན་ལ༌[^2718]འཇུག་པ་བསྟན་ཏོ། །

[Block 3209]
གཅན་གཟན༌[^2719]འཇིགས་པ་ལས་སྒྲོལ་བ་ནི་ཉོན་མོངས་པའི་ལས་སྣ་ཚོགས་སོ། །

[Block 3210]
ཆུ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་བསྟན་པས་དབུགས་འབྱིན་ཞེས་པའོ། །

[Block 3211]
མདོ་ལས་སྲོག་ཆགས་བྱེ་བ་སྟོང་པོ་དག་སྐྱེའོ་ཞེས་པ་ནས། ལྡོག་པར་དགའ་ཞེས་པའི་བར་དུ་ནི་ལྡོག་པའི་དཔེ་བསྟན་ཏོ། །

[Block 3212]
མདོ་ལས།

[Block 3213]
དེ་ནས༌[^2720]མཁས་ཤིང་རྟོགས་པ༌[^2721]དེ་ཡིན་ཞེས་པ་ནས་ཕྱིར་ཟློག་པ༌[^2722]ཞེས་པའི་བར་དུ་ནི་སྤྲུལ་པའི་གྲོང་ཁྱེར་ཤོམ་པའི་དཔེའོ། །

[Block 3214]
མདོ་ལས།

[Block 3215]
འདི་ལྟར་ང་ཡི་རྫུ་འཕྲུལ་སྟོབས་ཀྱིས་དེང་།[^2723] །ཞེས་པ་ནས། སྐྱེས་པ་བུད་མེད་མཚུངས་མེད་ལྡན། །ཞེས་པའི་བར་དུ་ནི་གྲོང་ཁྱེར་མངོན་པར་སྤྲུལ་པ་ཉིད་བསྟན་ཏེ། གྲོང་ཁྱེར་ཞེས་པ་ནི་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་རོ། །

[Block 3216]
ཁང་པ་ཞེས་པ་ནི་སྟོང་པ་ཉིད་ཀྱི་མཐའ་སྟེ། མདོ་དག་ལས་ཀྱང་དོན་དམ་པའི་སྟོང་པ་ཉིད་ནི་ཁང་པ། བྱང་ཆུབ་ཀྱི་ཡན་ལག་ནི་མེ་ཏོག་གི་རྒྱན། གཟུངས་ནི་སྐྱེད་མོས་ཀྱི༌[^2724]ར་བ། ཆོས་ཆེན་པོ་ནི་ཚལ། བསམ་གཏན་དགུ་ནི་ཆུའོ། །

[Block 3217]
རྣམ་པར་ཐར་པ་བརྒྱད་ནི་རྫིང་བུ། རྣམ་པར་ཐར་པ་གསུམ་ནི་སྒོ་ཁང་། མཐོ་བ་དང་མཛེས་པར་བརྒྱན་པ་ནི་མུ་སྟེགས་ཅན་ལས་འཕགས་པའི་དཔེ་ཡང་དག་པ། བདེན་པའི་ཆོས་ནི་སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས། སྙིང་རྗེ་ཆེན་པོ་ནི་བུ་མོར་བལྟའོ། །

[Block 3218]
མདོ་ལས།

[Block 3219]
སྤྲུལ་པ་བྱས་ནས་དེ་ལ་འདི་སྐད་སྨྲ། །ཞེས་པ་ནས། ཞུགས་ཏེ་དོན་རྣམས་རབ་ཏུ་མྱུར་བར༌[^2725]བྱོས། །ཞེས་པའི་བར་དུ་ནི་འཇུག་པར་གཞོན༌[^2726]གདབ་པའོ། །

[Block 3220]
མདོ་ལས།

[Block 3221]
མྱ་ངན་འདས་ཤིང་སེམས་ནི་དགའ་བར་བྱོས། །ཞེས་པ་ནས། དེ་ནས་དེ་དག་ཐམས་ཅད་མཐར་འགྲོ་བ། །ཞེས་པའི་བར་དུ་ནི་དུབ་པ་བསྟི་བའི་དཔེ་བསྟན་ཏོ། །

[Block 3222]
མདོ་ལས།

[Block 3223]
ཐམས་ཅད་ངལ་སོས་པ་ཡི༌[^2727]ཚུལ་རིག་ནས། །ཞེས་པ་ནས། གླིང་དུ་འགྲོ་བའི་ཕྱིར་ནི་བརྩོན་འགྲུས་བསྐྱེད།[^2728] །ཅེས་པའི་བར་དུ་ནི་ངེས་པའི་དོན་སྟོན་པའི་དཔེའོ། །

[Block 3224]
མདོ་ལས།

[Block 3225]
དགེ་སློང་དེ་བཞིན་ང་ཡང་འདྲེན་པ་སྟེ། ཞེས་པ་ནས་ཁྱེད་ཅག་བྱ་བ་བྱས་ཞེས་པའི་བར་དུ་ནི། འདི་མན་ཆད་དཔེ་དང་དོན་དུ་སྦྱར་བ་དང་། བཀྲི་བའི་དོན་དང་། ངེས་པའི་དོན་སྟོན་ཏེ། འདི་ནི་དང་པོའོ། །
--- END BLOCKS ---
