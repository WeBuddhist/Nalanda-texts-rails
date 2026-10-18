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
[Block 3431]
དེ་བཞིན་དུ་ཆོས་འདི་བྱང་ཆུབ་སེམས་དཔའ་ལ་གཏད་པར་འོས་ཀྱི་ཉན་ཐོས་པ་རྣམས་ལ་མ་ཡིན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ནི་ཐོས་པ་ཙམ་གྱིས་མཐར་ཕྱིན་པར་འགྱུར་བ་དང་བདག་དང་གཞན་གྱི༌[^2901]དོན་འགྲུབ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3432 [HEADING]]
#### ཚིགས་སུ་བཅད་པ། ^4-10-5-0

[Block 3433]
མདོ་ལས།

[Block 3434]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2902]དེའི་ཚེ་ཞེས་པ་ནས་འཛིན་པ་ལ་བཀུར་སྟི་བྱ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་བཅུ་དྲུག་ལ་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། ཚིག་དང་པོ་གཉིས་ཀྱིས་ནི་ཆོས་སྨྲ་བའི་ཡོན་ཏན་དང་མཆོད་པར་འོས་པ་གླེངས། ཚིག་བཅུ་གསུམ་གྱིས་ནི་ཆོས་སྨྲ་བའི་ཡོན་ཏན་ཉིད་གླེངས། ཚིག་གཅིག་གིས་ནི་ཆོས་ཁྱད་པར་ཅན་བསྡུ་བ༌[^2903]བསྟན་ཏོ། །

[Block 3435 [HEADING]]
##### ཆོས་སྨྲ་བའི་ཡོན་ཏན་དང་མཆོད་པར་འོས་པ། ^4-10-5-1-0

[Block 3436]
ཚིག་དང་པོ་དེ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚིགས་བཅད་གཅིག་གིས་ནི་ལྷུན་གྱིས་གྲུབ་པའི་ཡེ་ཤེས་ཐོབ་པ་བསྟན་ཏེ། ཡང་དག་པའི་ཡེ་ཤེས་དང་། སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 3437]
དེའི་འོག་མས་ནི་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་སྟོན༌[^2904]ཏེ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་དང་། ཕྱིས་ཐོབ་པའི་ཡེ་ཤེས་དང་། རྩ་བའི་ཡེ་ཤེས་སོ། །

[Block 3438]
སུ་མདོ་འདི་འཛིན་པ་དང་། མཆོད་པ་དང་། བསྟི་སྟང་དུ༌[^2905]བྱེད་པ༌[^2906]ཡེ་ཤེས་དེ་དག་འཐོབ་པ༌[^2907]ལ་ཐེ་ཚོམ་མེད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 3439 [HEADING]]
##### ཆོས་སྨྲ་བའི་ཡོན་ཏན། ^4-10-5-2-0

[Block 3440]
མདོ་ལས།

[Block 3441 [HEADING]]
###### ཆོས་སྨྲ་བའི་ཁྱད་པར། ^4-10-5-2-1-0

[Block 3442]
འཇིག་རྟེན་མགོན་གྱི་སྐྱེ་བ་སྟེ། །ཞེས་པ་ནས། བླ་ན་མེད་པའི་མདོ་སྡེ་འདི། །ཞེས་པའི་བར་དུ་ནི༌[^2908]ཚིགས་བཅད་བཅུ་གསུམ་གྱིས༌[^2909]ཆོས་སྨྲ་བའི་ཡོན་ཏན་སྟོན་ཏེ། དེ་ལ་ཡང་ཚིགས་བཅད་གསུམ་གྱིས་ནི་ཆོས་སྨྲ་བའི་ཁྱད་པར་བསྟན། ཚིགས་བཅད་བཅུས་ནི་བཙུན་པ་དང་གུས་པར་བྱ་བ་བསྟན། དང་པོའི་ཚིག་གསུམ་གྱིས་ནི་དེ་བཞིན་གཤེགས་པས་བསྔགས་པ་དང་། སྐྱེ་བ་བཟང་པོ་བསྟན་པ་དང་། སྨོན་ལམ་གྱི་དབང་གིས༌[^2910]སྐྱེ་བ་བསྟན་ཏོ། །

[Block 3443 [HEADING]]
###### མཆོད་པ་དང་གུས་པར་བྱ་བ། ^4-10-5-2-2-0

[Block 3444]
མདོ་ལས།

[Block 3445 [HEADING]]
###### **རིམ་གྲོ་བཀུར་སྟི་བྱ་བ།** ^4-10-5-2-2-1-0

[Block 3446]
འཕྲུལ་གྱི་མེ་ཏོག་བཀུར་སྟི་བྱ། །ཞེས་པ་ནས། ཆོས་སྨྲ་དེ་ལ་རིན་ཆེན་འཐོར། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་བཅུས་མཆོད་པ་དང་གུས་པར་བྱ་བ་བསྟན་ཏེ། དེ་ལ་ཡང་ཚིགས་བཅད་བཞིས་ནི་ཆོས་སྨྲ་བ་ལ་རིམ་གྲོ་བཀུར་སྟི་བྱ་བ་བསྟན། ཚིགས་བཅད་ཕྱི་མ་དྲུག་གིས་ནི་བསོད་ནམས་ཀྱི་ཁྱད་པར་བསྟན་ཏེ། གུས་པ་སྐྱེ་བ་བསྟན། དང་པོའི་ཚིགས་བཅད་བཞི་ལ་ཡང་། དང་པོའི་ཚིག་གཅིག་གིས་ནི་ཆོས་སྨྲ་བ་ཉིད་བསྟན། འོག་མ་གསུམ་གྱིས་ནི་འཛིན་པ་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 3447]
ཆོས་སྨྲ་བ་དེ་འབྲས་བུ་དམ་པ་ཐོབ་པའི༌[^2911]ཕྱིར་རོ། །

[Block 3448]
མདོ་ལས།

[Block 3449]
དེ་དག་རྟག་ཏུ་ཐལ་སྦྱར་ཏེ། །ཞེས་པ་ནས། དེ་བཞིན་གཤེགས་ཀྱི་བྱ་བ་བྱེད། །ཅེས་པའི་བར་དུ་ནི་འདིས་འཛིན་པ་བསོད་ནམས་ཆེ་བ་བསྟན་ཏེ། གུས་པ་དང་། མཆོད་པ་དང་། གསུང་མཉན་པ་དང་། འདོན་ཞིང་ཁ་ཏོན༌[^2912]བྱེད་པའོ། །

[Block 3450 [HEADING]]
###### **བསོད་ནམས་ཀྱི་ཁྱད་པར།** ^4-10-5-2-2-2-0

[Block 3451]
མདོ་ལས།

[Block 3452]
མི་རུང་འབྱུང༌[^2913]ན་ངས་དེ་བཏང་། །ཞེས་པ་ནས། སྡིག་པ་ཤིན་ཏུ་དེ་མང་བཤད། །ཅེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་སྡིག་པའི་ཁྱད་པར་བསྟན། ཚིག༌[^2914]བཞིས་ནི་དགེ་བའི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 3453]
མདོ་ལས།

[Block 3454]
མི་གང་ང༌[^2915]ལ་མངོན་བསྟོད་པ། །ཞེས་པ་ནས། དེ་ལ༌[^2916]བསོད་ནམས་ཆོས༌[^2917]མང་རྙེད། །ཞེས་པའི༌[^2918]བར་དུ་ནི་བསོད་ནམས་ཀྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 3455]
མདོ་ལས།

[Block 3456]
དགའ་སྐྱེས་ང་ལ་བསྟོད་པ་ནི། །ཞེས་པ་ནས། ངོ་མཚར་ཆེན་པོ་དེས་ཐོབ་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་ཆོས་ཐོས་པའི་བསོད་ནམས་དང་། ཕྱི་ནང༌[^2919]མཆོད་པ་རྣམ་གཉིས་ཀྱི་ཁྱད་པར་བསྟན་པའོ། །

[Block 3457 [HEADING]]
##### ཆོས་ཁྱད་པར་ཅན་བསྡུ་བ། ^4-10-5-3-0

[Block 3458]
མདོ་ལས།

[Block 3459]
སྨན་གྱི་རྒྱལ་པོ་ཁྱོད་མོས་པར་བྱ་ཞེས་པ་ནས་བཤད་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་འདི་ཁྱད་པར་ཅན་དུ་བསྟན་པའོ། །

[Block 3460 [HEADING]]
#### ཆོས་སྨྲ་བ་ཉིད། ^4-10-6-0

[Block 3461]
མདོ་ལས།

[Block 3462 [HEADING]]
##### ཚིག་རྐྱང་པ། ^4-10-6-1-0

[Block 3463 [HEADING]]
###### ཆོས་ཆུད་པར་དཀའ་བ། ^4-10-6-1-1-0

[Block 3464]
སྨན་གྱི་རྒྱལ་པོ་ཆོས་ཀྱི་གཞུང་འདི་དག །ཅེས་པ་ནས། དད་པར་མི་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་སྨྲ་བ་ཉིད་སྟོན་ཏོ༌[^2920]སྔར་ནི་ཚིག་རྐྱང་པས་བསྟན། འོག་ཏུ༌[^2921]ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ། ཚིག་རྐྱང་པ་ལ༌[^2922]ཆོས་ཆུད་པར་དཀའ་བ་དང་། འདོན་པའི་གནས་ཏེ་མཆོད་རྟེན་དུ་གྱུར་པ་བསྟན་པ་དང་། འཁོར་རྣམས་ཀྱི་ཚུལ་བསྟན་པའོ། །

[Block 3465]
མདོ་ལས།

[Block 3466]
སྨན་གྱི་རྒྱལ་པོ་འདི་ནི་ཞེས་པ་ནས་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཞལ་བཞུགས་པ་ན་ཡང་གསངས་ཏེ། ཀུན་ལ་བསྟན་པ་མ་ཡིན་པའང་ཆུད་དཀའ་བའི་ཕྱིར་མ་འོངས་པའི་དུས་ན་དབང་པོ་མ་རྟོགས་པ་རྣམས་ལ་བསྟན་ན་སྐུར་བ་འདེབས་པའི་ཕྱིར་མ་སྟོན་ཅིག་པར་བསྟན་པའོ། །

[Block 3467]
མདོ་ལས་འདི་ལྟར་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་ཕྱག་གིས་བྱུག་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་འདིའི་མཐུས་འདོན་པའི་གང་ཟག་ཡོན་ཏན་ཅན༌[^2923]དུ་འགྱུར་བ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ན་བཟའ་ནི་བཟོད་པ། ཞི་བ། དུལ་བ། བྱམས་པ་དང་སྙིང་རྗེར་ལྡན་པ། ངོ་ཚ་བ་དང་འཛེམ་པ་སྤངས་པ་སྟེ། ན་བཟའ་དེས་བཀབ་པར་གྱུར་པ་དང་། དབང་པོ་སྨིན་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^2924]དགོངས་ཤིང་སྐྱོབ་པར་འགྱུར་བ་དང་། མོས་པ་ཆེ་བར་འགྱུར་བ་དང་། སྨོན་ལམ་དང་དད་པ་བཙན་པའི༌[^2925]རང་བཞིན་ཅན་དུ་འགྱུར་བ་དང་། དགེ་བའི་རྩ་བ་ཅན་དུ་འགྱུར་བ་དང་། སྟོང་པ་ཉིད་དང་སྙིང་རྗེའི་ཁྱད་པར༌[^2926]བཅོམ་ལྡན་འདས་དང་འདྲ་བར་འཇུག་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཕྱག་གིས་བྱུག་ཅིང་གནས་འཚོབ་པར་ལུང་བསྟན་པ་འཐོབ་པའོ། །

[Block 3468 [HEADING]]
###### འདོན་པའི་གནས་མཆོད་རྟེན་དུ་གྱུར་པ། ^4-10-6-1-2-0

[Block 3469 [HEADING]]
###### **ཆོས་ཀྱི་སྐུ་དང་རིང་བསྲེལ།** ^4-10-6-1-2-1-0

[Block 3470]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་མཆོད་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་སྐུ་དང་། རིང་བསྲེལ་མཆོད་པར་འོས་པ་བསྟན་ཏེ། དེ་ལ་དང་པོ༌[^2927]ཆོས་ཀྱི་སྐུ་དང་། རིང་བསྲེལ་བསྟན་པ་དང་། འདི་ལ་བརྟེན་ཏེ་ཆོས་སྨྲ་བ་ཡོན་ཏན་ཅན་དུ་འགྱུར་བ་བསྟན་ཏོ། །
--- END BLOCKS ---
