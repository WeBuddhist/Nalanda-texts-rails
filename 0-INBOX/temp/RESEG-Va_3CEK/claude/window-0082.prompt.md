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
[Block 2871]
གནས་ཐམས་ཅད་དུ་འཆི་འཕོ་བ་ཞེས་བྱ་བ་ནི་གནས་གཞན་ཐམས་ཅད་དུ་འཕོས་ནས་འོག་མིན་དུ་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 2872]
ཕྱིར་མི་འོང་བ་ནི་ནམ་ཡང་སྐྱེ་བའི་སྐྱེ་མཆེད་དེ་ཉིད་དུ་ཚེ་གཉིས་པ་མངོན་པར་འགྲུབ་པར་མི་བྱེད་དེ། ཁྱད་པར་དུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2873]
འདི་ལྟར་ན་འདིའི་ཕྱིར་མི་འོང་བ་ཉིད་ཡོངས་སུ་རྫོགས་པ་ཡིན་ཏེ། གང་དུ་སྐྱེས་པ༌[^1978]དེ་འོག་དང་དེར་གཏན་དུ་མི་འོང་བའི་ཕྱིར་རོ། །

[Block 2874]
རེ་ཞིག་བསམ་གཏན་སྤེལ་ནས༌[^1979]འོག་མིན་དུ་འགྲོ་བ་ནི་དེ་ལྟ་བུ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2875 [HEADING]]
###### **སྲིད་པའི་རྩེ་མོར་འགྲོ་བ།** ^3-2-8-7-1-5-2-0

[Block 2876]
དེ་ལས་གཞན་སྲིད་རྩེ་མོར་འགྲོ། །གོང་དུ་འཕོ་བ་བསམ་གཏན་མ་སྤེལ་བ་ནི་སྲིད་པའི་རྩེ་མོའི་མཐར་ཐུག་པ་ཡིན་ཏེ། དེ་ནི་སྙོམས་པར་འཇུག་པ་གཞན་རྣམས་རོ་མྱོང༌[^1980]བར་བྱེད་ཅིང་གནས་གཞན་ཐམས་ཅད་དུ་སྐྱེ་ལ། གནས་གཙང་མ་རྣམས་སུ་མི་འཇུག་པ་ཁོ་ནར་གཟུགས་མེད་པར་སྐྱེ་བའི་རིམ་གྱིས་སྲིད་པའི་རྩེ་མོར་སོང་སྟེ། ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ། །

[Block 2877]
འདི་ནི་ཞི་གནས་སྤྱད་པ་ཡིན་ནོ། །

[Block 2878]
སྔ་མ་ནི་ལྷག་མཐོང་སྤྱད་པ་ཡིན་ནོ། །

[Block 2879]
གོང་དུ་འཕོ་བ༌[^1981]བར་སྐབས་སུ་ཡང་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་རུང་བར་བལྟའོ། །

[Block 2880]
འོག་མིན་དང༌[^1982]སྲིད་པའི་རྩེ་མོའི་མཐར་ཐུག་པ་ཉིད་ནི་ཕན་ཆད་དུ་འགྲོ་བ་མེད་པའི་ཕྱིར་ཏེ། དཔེར་ན་རྒྱུན་དུ་ཞུགས་པ་མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་ཉིད་བཞིན་ནོ། །

[Block 2881]
རེ་ཞིག་དེ་དག་ནི་གཟུགས་སུ་ཉེ་བར་འགྲོ་བའི་ཕྱིར་མི་འོང་བ་ལྔ༌[^1983]ཡིན་ནོ། །

[Block 2882 [HEADING]]
###### གཟུགས་མེད་པར་ཉེ་བར་འགྲོ་བ། ^3-2-8-7-2-0

[Block 2883]
གཞན་ནི་གཟུགས་མེད་འགྲོ་རྣམ་བཞི། །ཕྱིར་མི་འོང་བ་གཞན་ནི་གཟུགས་མེད་པར་ཉེ་བར་འགྲོ་བ་སྟེ། གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་འདི་ནས་ཤི་འཕོས་ནས་གཟུགས་མེད་པ་དག་གི་ནང་དུ་སྐྱེ་བ་གང་ཡིན་པའོ། །

[Block 2884]
དེ་ཡང་སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་རྣམ་པ་བཞི་སྟེ།[^1984] དེ་དག་ནི་ཕྱིར་མི་འོང་བ་རྣམ་པ༌[^1985]དྲུག་ཡིན་ནོ། །

[Block 2885 [HEADING]]
###### མཐོང་བའི་ཆོས་ལ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ། ^3-2-8-7-3-0

[Block 2886]
གཞན་ནི་འདི་ལ་མྱ་ངན་འདའ། །གཞན་ནི་ཚེ་འདི་ཁོ་ན་ལ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་སྟེ། མཐོང་བའི་ཆོས་ལ༌[^1986]ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དེ་ནི་བདུན་པ་ཡིན་ནོ། །

[Block 2887 [HEADING]]
###### གཟུགས་སུ་ཉེ་བར་འགྲོ་བ་དགུ། ^3-2-8-7-4-0

[Block 2888]
གསུམ་ལ༌[^1987]རྣམ་གསུམ་ཕྱི་ནས་སུ།[^1988] །གཟུགས་སུ་ཉེར་འགྲོ་དགུར་བཤད་དོ། །

[Block 2889]
ཕྱིར་མི་འོང་བ་གསུམ་ལ༌[^1989]ཡང་རྣམ་པ་གསུམ་དུ་ཕྱེ་བས༌[^1990]གཟུགས་སུ་ཉེ་བར་འགྲོ་བའི་ཕྱིར་མི་འོང་བ་དགུ་ཡིན་ནོ། །

[Block 2890]
གསུམ་པོ་གང་དག་ཅེ་ན། བར་མ་དོ་དང་སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དག་དང་། གོང་དུ་འཕོ་བའོ། །

[Block 2891]
རྣམ་པ་གསུམ་དུ་ཕྱེ་བས་ཇི་ལྟ་བུ་ཞེ་ན། རེ་ཞིག་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་དཔེ་གསུམ་གྱིས་མྱུར་བ་དང་། མྱུར་བ་མ་ཡིན་པ་དང་། ཡུན་རིང་མོ༌[^1991]ཞིག་ནས༌[^1992]ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 2892]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་ནས་དང་། མངོན་པར་འདུ་བྱེད་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 2893]
དེ་དག་ཐམས་ཅད་ཀྱང༌[^1993]སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དག་ཡིན་ནོ། །

[Block 2894]
གོང་དུ་འཕོ་བ་ནི་འཕར་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 2895]
ཡང་ན་གསུམ་པོ་ཐམས་ཅད་མྱུར་བ་དང་མྱུར་བ་མ་ཡིན་པ་དང་། ཡུན་རིང་མོ་ཞིག་ནས༌[^1994]ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 2896 [HEADING]]
###### ཕྱིར་མི་འོང་བ་དེ་དག་གི་ཁྱད་པར། ^3-2-8-7-5-0

[Block 2897 [VERSE]]
དེ་དག་གི་ནི་ཁྱད་པར་རྣམས། །
ལས་དབང་ཉོན་མོངས་བྱེ་བྲག་ལས། །

[Block 2898]
ཕྱིར་མི་འོང་བ་གསུམ་དང་དགུ་པོ་དེ་དག་གི་ཁྱད་པར་ནི་ལས་དང་། ཉོན་མོངས་པ་དང་དབང་པོའི་བྱེ་བྲག་ལས་ཏེ། རེ་ཞིག་གསུམ་པོ༌[^1995]ནི་གོ་རིམས་བཞིན་དུ་མངོན་པར་འགྲུབ་པ་དང་། སྐྱེས་པ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་བསགས་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་ཀུན་དུ་སྤྱོད་པ་ཆུང་བ་དང་། འབྲིང་དང་། ཆེན་པོའི་ཕྱིར་དང་། དབང་པོ་ཆེན་པོ་དང་འབྲིང་དང་ཆུང་ངུའི་ཕྱིར་རོ། །

[Block 2899]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་སོ་སོའི་ཁྱད་པར་ཡང་ཅི་རིགས་པར་གསུམ་ཚན་དང་པོ་གཉིས་ནི་གོང་མ་བཞིན་དུ་ཉོན་མོངས་པ་དང་། དབང་པོའི་བྱེ་བྲག་ལས་སོ། །

[Block 2900]
གསུམ་ཚན་ཐ་མ་ནི་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་བྱེ་བྲག་ལས་ཀྱང་ཁྱད་པར་དུ་བལྟ༌[^1996]སྟེ། དེ་དག་ནི་ཉོན་མོངས་པ་དང་དབང་པོའི་རྣམ་པ་དགུའི་ཕྱིར་ཕྱིར་མི་འོང་བ་དགུ་ཡིན་ནོ། །

[Block 2901 [HEADING]]
###### སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན། ^3-2-8-7-6-0

[Block 2902]
འོ་ན་མདོ་ལས་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན་བསྟན་པ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 2903 [VERSE]]
གོང་དུ་འཕོ་བ་མ་ཕྱེ་བར། །
དམ་པའི་འགྲོ་བ་བདུན་དུ་འདོད། །

[Block 2904]
གོང་དུ་འགྲོ་བའི་ཆོས་ནི་གོང་དུ་འགྲོ་བའོ། །

[Block 2905]
མདོ་ལས་ནི་དེ་མ་ཕྱེ་བར་བསྟན་པའི་ཕྱིར་མདོ་ལས་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན་ཞེས་གསུངས་སོ། །

[Block 2906]
ཅིའི་ཕྱིར་འདི་དག་ཁོ་ན་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་ཡིན་ལ། སློབ་པའི་འགྲོ་བ་གཞན་དག་ནི་མ་ཡིན་ཞེ་ན། གང་དག་ལ་འགྲོ་བ་འདི་དག་ཡོད་པ་དེ་དག་ནི་ལས་དམ་པ་དགེ་བ་ཁོ་ན་ལ་འཇུག་ཅིང་དམ་པ་མ་ཡིན་པ་མི༌[^1997]དགེ་བ་ལ་མི་འཇུག་པ་དང་། འགྲོ་བ་འདི་དག་ཏུ་སོན་པ་རྣམས་ལ༌[^1998]ཡང་ཕྱིར་འོང་བ་མེད་པ་ཡིན་ལ་ཇི་སྐད་དུ་བཤད་པ་འདི་དག་གཞན་ལ་ནི་མེད་པས་དེའི་ཕྱིར།

[Block 2907 [VERSE]]
དམ་པ་དམ་མིན་འཇུག་མི་འཇུག །
སོན་པ་ཕྱིར་མི་འོང་ཕྱིར་ཏེ། །

[Block 2908]
སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་དག་ཡིན་གྱི་གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 2909]
འོ་ན་མདོ་ཁོ་ན་ལས་སྐྱེས་བུ་དམ་པ་གང་ཞེ་ན། སློབ་པའི་ཡང་དག་པའི་ལྟ་བ་དང་ལྡན་པའོ་ཞེས་རྒྱས་པར་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། གཞན་དག་ལ་ཡང་སྡིག་པ་རྣམ་པ་ལྔ་གཏན་མི་བྱེད་པའི་སྡོམ་པ་ཐོབ་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་མི་དགེ་བ་ཕལ་ཆེར་སྤངས་པའི་ཕྱིར་རྣམ་གྲངས་པའི་སྐྱེས་བུ་དམ་པ་ཉིད་ཡོད་མོད་ཀྱི། འདིར་ནི་གང་དག་ལ་རྣམ་གྲངས་མེད་པར་ཡོད་པ་དེ་དག་གི་སྐབས་ཡིན་ནོ། །

[Block 2910 [HEADING]]
###### འདོད་པར་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ། ^3-2-8-7-7-0
--- END BLOCKS ---
