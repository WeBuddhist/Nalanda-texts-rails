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
[Block 3361]
མདོ་ལས།

[Block 3362]
བདེ་གཤེགས་བྱེ་བ་བརྒྱད་ཅུ་མཆོད་བྱས་ན།[^2843] །ཞེས་པ་ནས། སངས་རྒྱས་བྱང་ཆུབ་འདི་ལ་རྒྱུ་ཡང་སྐྱེད།[^2844] །ཅེས་པའི་བར་དུ༌[^2845]འབྲས་བུ་ལས་དགོངས་ཏེ་ལུང་བསྟན་པ་ལ་མཚན་དང་། ཞིང་གི་རྒྱན་དང་། ཡུལ་གྱི་མིང་དང་། ཕན་འདོགས་པ་དང་། རྗེས་སུ་བསྔགས་པ་དང་། སྐུ་ཚེའི་ཚད་དང་། སེམས་ཅན་ལ་ཕན་འདོགས་པ་དང་། དེ་བཞིན་གཤེགས་པའི་སྤྱོད་པའི་རྒྱུ་སྒྲུབ་པ་སྟེ། འདི་ནི་ཚིག་དང་པོ་དང་སྦྱར་རོ། །

[Block 3363]
མདོ་ལས་དེ་ནས་འཁོར་དེ་ན་ཞེས་པ་ནས་ཅིའི་རྐྱེན་དུ་འགྱུར་ཞེས་པའི་བར་དུ་ནི་འཁོར་གྱི་ཐེ་ཚོམ་མོ། །

[Block 3364]
མདོ་ལས།

[Block 3365]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་དེ་ཞེས་པའི་བར་དུ༌[^2846]ནི་སྔོན་གྱི༌[^2847]རྒྱུ་བསྟན་པ་དང་། དེའི་འོག་ཏུ་འཕྲལ་གྱི་སྤྱོད་པ་བསྟན་པ་དང་། བསྡུ་སྟེ༌[^2848]ལུང་སྟོན་པ་ལ༌[^2849]འདི་ནི་དང་པོའོ། །

[Block 3366]
མདོ་ལས་དེ་ན་རིགས་ཀྱི་བུ་འདི་ནི་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་པ་ཐོས་ཞེས་པའི་བར་དུ་ནི་སྤྱོད་པ་ཕྱི་མ་བསྟན་པ་དང་། མདོར་བསྡུས་ཏེ་ལུང་བསྟན་པའོ། །

[Block 3367]
མདོ་ལས།

[Block 3368]
བདག་གིས༌[^2850]སངས་རྒྱས་ཀྱི་ཞིང་གི་ཞེས་པ་ནས། སྔོན་གྱི་སྨོན་ལམ་དྲན་ནོ་ཞེས་པའི་བར་དུ་ནི་དགའ་བོས་མངོན་དུ་རྟོགས་པ་བསྟན་ཏོ། །

[Block 3369]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་དགའ་བོས་ཞེས་པ་ནས། དམ་པའི་ཆོས་འཛིན་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱིར་ཞེས་པའི་བར་དུ་ནི་དགའ་བོས་རང་གི་ཡོན་ཏན་བསྒྲགས་པས་གཞན་དེ་འདྲ་བ་བྱེད་དུ་གཞུག་པའོ། །

[Block 3370 [HEADING]]
##### སྒྲ་གཅན་འཛིན་ལུང་བསྟན་པ། ^4-9-4-2-0

[Block 3371]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2851]ཞེས་པ་ནས་འཚང་རྒྱ་བར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འདིས་གཉིས་པ་ལུང་བསྟན་པའོ། །

[Block 3372]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ན་ཞེས་པ་ནས། འགྱུར་བ་བྱང་ཆུབ་ཚོལ་བ་ན༌[^2852]ཞེས་པའི་བར་དུ་ནི། འདི་མན་ཆད་བཞིར་དབྱེ་སྟེ། རྟག་ཏུ་དེ་བཞིན་གཤེགས་པའི་སྲས་སུ་གྱུར་པ་དང་། དེ་བཞིན་གཤེགས་པ་གཞན་གྱི་སྲས་སུ་ཡང་སྟོན་པ་དང་། རྒྱུ་དམ་པ་འཆད་པ་དང་རྣམ་པ་བཞི་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 3373]
མདོ་ལས་མི་ཤེས་སྤྱོད་པ་སྒྲ་གཅན་འདི་ཞེས་པ་ནས། དེ་ལྟར་བྱང་ཆུབ་ཀྱི་ཕྱིར་གནས་སོ་ཞེས་པའི་བར་དུ་ནི་མྱ་ངན་ལས་མ་འདས་ཏེ་འཇིག་རྟེན་འདི་ནི༌[^2853]བཞུགས་པ་བསྟན་པའོ། །

[Block 3374 [HEADING]]
##### དགེ་སློང་ཉིས་སྟོང་ལུང་བསྟན་པ། ^4-9-4-3-0

[Block 3375 [HEADING]]
###### དྲིས་པ། ^4-9-4-3-1-0

[Block 3376]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་གསོལ་བ་མཐོང༌[^2854]ཞེས་པའི་བར་དུ་ནི་སློབ་པ་དང་མི་སློབ་པ་ཉིས་སྟོང་ལུང་བསྟན་པ་སྟེ། དེ་ལ་དྲིས་པ་དང་། ལན་བཏབ་པ་དང་། མངོན་དུ་ལུང་བསྟན་པ་དང་། མངོན་པར་དགའ་བ་དང་།[^2855] བཞིར་དབྱེ་བ་ལ་འདི་ནི་དང་པོའོ། །

[Block 3377]
འཇམ་པ་ཞེས་པ་ནི་སེམས་དུལ་བའོ། །

[Block 3378]
མཉེན་པ་ཞེས་པ་ནི་དབང་པོ་སྨིན་པའོ། །

[Block 3379 [HEADING]]
###### ལན་བཏབ་པ། ^4-9-4-3-2-0

[Block 3380]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་དམ་པའི་ཆོས་ཀྱང་མཉམ་པར་གནས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ལན་བཏབ་པ་དང་། རྒྱུ་དང་འབྲས་བུ་བསྟན་པ་དང་། མཚན་མཐུན་པར༌[^2856]བསྟན་ཏོ། །

[Block 3381 [HEADING]]
###### མངོན་པར་དགའ་བ། ^4-9-4-3-3-0

[Block 3382]
མདོ་ལས་དེ་ནས་སློབ་པ་དང་མི་སློབ་པ་ཞེས་པ་ནས་ལུང་བསྟན་པ་དང་། འདི་ཐོས་པ་ཞེས་པའི་བར་དུ་ནི༌[^2857]འཁོར་རྣམས་ཀྱི་དགའ་བའི་ཚིག་གོ།། །།

[Block 3383 [HEADING]]
### ཆོས་སྨྲ་བའི་ལེའུ། ^4-10-0

[Block 3384]
འདི་མན་ཆད་ཆོས་སྨྲ་བའི་ལེའུ་སྟོན་ཏེ། ལེའུ་འདིའི་གཏན་ཚིགས་དང་། མིང་དང་། དོགས་པ་བསལ་བའོ། །

[Block 3385 [HEADING]]
#### གཏན་ཚིགས། ^4-10-1-0

[Block 3386]
གཏན་ཚིགས་ནི་མདོ་སྡེ་འདི་དང་པོར་ནི་གླེང་གཞིའི་ལེའུ་བསྟན། དེའི་འོག་ཏུ་ལེའུ་བརྒྱད་ཀྱིས་ནི་གཞུང་ཉིད་བསྟན་ཏེ། གཞུང་ནི་ཐེག་པ་གཅིག་པུ་ཐབས་དང་དཔེ་རྣམ་པ་སྣ་ཚོགས་ཀྱིས་སྟོན་ཅིང་ཐེག་པ་རྣམ༌[^2858]གཉིས་དང་རིགས་མ་ངེས་པ་རྣམས་ཀྱི་ཆེད་དུ་བསྟན་པ་དང་། ལུང་སྟོན་པའོ། །

[Block 3387]
དེ་མན་ཆད་ལེའུ་བཅུ་དགུས༌[^2859]ནི་རྗེས་སུ་འཛིན་པ་སྟོན་ཏེ། མདོ་སྡེ་འདི་རྒྱ་ཆེ་ཞིང་ཟབ་ལ་དབང་པོ་ཞན་པ་རྣམས་མོས་པར་དཀའ་བའི་ཕྱིར་མདོ་སྡེ་འདི༌[^2860]གཞན་དང་མི་འདྲ་བ༌[^2861]བསྔགས་པ་དང་། རྗེས་སུ་འཛིན་པའི་ཡོན་ཏན་མང་དུ་བཤད་དོ། །

[Block 3388]
ཡང་རྗེས་སུ་འཛིན་པའི་དོན་སྟོན་པས། སྤྱིར་རྗེས་སུ་འཛིན་པར་གདགས་པ་དང་། མདོ་སྡེ་འདིའི་གཞུང་སྟོན་པའི་ལེའུ་བཅུ་དགུ་ཡོད་པ་ལ་བཅུ་གཉིས་ཀྱིས་ནི་ཐེག་པ་གཅིག་པོའི༌[^2862]སྤྱོད་ཡུལ་སྟོན་ཏེ།[^2863] ལེའུ་སྔ་མ་བརྒྱད་ཀྱིས་ནི་དྲང་བ་དང་ངེས་པའི་དོན་དབྱེ་བ་དང་། དབང་པོ་རྣམ༌[^2864]གསུམ་པོ་རིམ་པར་ལུང་བསྟན་པ་སྟོན། དེའི་འོག་མ་བཞིས་ནི་ཆོས་དང་གང་ཟག་གཉི་གའི་ཡོན་ཏན་སྟོན་པས་འདི་ཡང་རྗེས་སུ་འཛིན་པ་ཉིད་དུ་བསྡུ་བ་དང་། ཡང་མདོ་འདི༌[^2865]འགྲེལ་པ་ལས་དཔེ་རྣམ་པ་བདུན་དང་། མཉམ་པ་གསུམ་དང་། བླ་ན་མེད་པ་བཅུ་སྟོན་པ་ལ། འདིར་བཅུ་པ་སྟེ། སྟོབས་བླ་ན་མེད་པ་ཁྱད་པར་ཅན་སྟོན་ཏོ། །

[Block 3389]
སྟོབས་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཀྱི་སྟོབས་དང་སྤྱོད་པའི་སྟོབས་སོ། །

[Block 3390]
ཆོས་ཀྱི་སྟོབས་ཀྱང་རྣམ་པ་ལྔ་སྟེ། ཆུད་པ་དང་། མོས་པ་དང་། མཚམས་ཆོད་པ་དང་། ཆོས་ཉིད་ཐོབ་པ༌[^2866]དང་། ཀློག་ཅིང་འཛིན་པའོ། །

[Block 3391]
སྤྱོད་པའི་སྟོབས་ཀྱང་རྣམ་པ་བདུན་ཏེ། རྗེས་སུ་འཛིན་པ་དང་། ཆོས་འཆད་པ་དང་། དཀའ་བ་སྤྱོད་པ་དང་། སེམས་ཅན་འདུལ་བ་དང་། སེམས་ཅན་རྣམས་ཀྱི་སྡུག་བསྔལ་བཏོན་པ༌[^2867]དང་། ཡོན་ཏན་ཁྱད་པར་ཅན་དང་། ཆོས་འདོན་པའོ། །

[Block 3392]
འཛིན་པའི་སྟོབས་ལ་ལེའུ་གསུམ་སྡུད་དེ། ཆོས་སྨྲ་བའི་ལེའུ་དང་། བདེ་བ་ལ་གནས་པ་དང་། རྗེས་སུ་འཛིན་པའི་ལེའུའོ། །

[Block 3393]
ལེའུ་འདིའི་ནང་དུ་གཟུང་བ་དང་། འཛིན་པ་དང་། གང་ཟག་དང་ཆོས་གཉི་ག་སྟོན་ཏོ། །

[Block 3394 [HEADING]]
#### མིང། ^4-10-2-0

[Block 3395]
མིང་ནི་ཆོས་སྨྲ་བ་ཞེས་པ་ཆོས་འདོན་པ་དང་ལུང་སྨྲ་བའི་གང་ཟག་དེ་ཆོས་སྨྲ་བ་ཡིན་པས་ཆོས་སྨྲ་བའི་ལེའུའོ། །

[Block 3396 [HEADING]]
#### དོགས་པ་བསལ་བ། ^4-10-3-0

[Block 3397]
དོགས་པ་བསལ་བ་ནི་ཆོས་སྨྲ་བ་ཞེས་པ་འདི་སངས་རྒྱས་འཇིག་རྟེན་དུ༌[^2868]བཞུགས་པ་དང་། མི་བཞུགས་པ་གང་གི་ཚེ་ན་ཆོས་སྨྲ་བ་ཞེས་གདགས། དེ་གཉི་ག་ཡང་ཆོས་སྨྲ་བ་ཡིན་མོད་ཀྱི་སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པའི་ཚེ་ནི་སློབ་པ་ལ་གནས་པས་འཁོར་བརྒྱད་པོ་ཞེས་གདགས་ཀྱི། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་ཆོས་སྟོན་པ་དེ་ཆོས་སྨྲ་བ་ཞེས་གདགས་སོ། །

[Block 3398]
ལེའུ་འདིའི་ནང་ནས་ཀྱང་ལུང༌[^2869]སྟོན་པ་འབྱུང་ན་ལུང་བསྟན་པའི་ལེའུ་ཞེས་ཅིའི་ཕྱིར་མི་གདགས་ཤེ༌[^2870]ན། གཙོ་བོ༌[^2871]ལས་དྲས༌[^2872]པའི་ཕྱིར་མི་གདགས་སོ། །

[Block 3399 [HEADING]]
#### ཚིག་རྐྱང་པ། ^4-10-4-0

[Block 3400]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་ལུང་སྟོན༌[^2873]ཏོ་ཞེས་པའི་བར་དུ་ནི་ལེའུ་འདི་ཡང་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པ་གཉིས་སུ་དབྱེའོ། །
--- END BLOCKS ---
