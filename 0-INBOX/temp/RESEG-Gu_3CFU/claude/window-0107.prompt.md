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
[Block 3746]
འདིར་ལུང་ནི་གང་ཞིག་ལམ་དུ་ཞུགས་པ་ལ་ལུས་དང་འབྲེལ་པའི་ཕྱོགས༌[^2566]ནས་མཚམས༌[^2567]སོ། །

[Block 3747]
འདོམ་བཞི་བཅུ་རྩ་དགུ་ཚུན་ཆད་ཉེན་ཀོར་ཡིན་པར་གསུངས་པ་གང་ཡིན་པ་དང་། མཚམས་གཞན་པ་ལ་ལུས་ཀྱིས་ནོན་པ་ཉི༌[^2568]ཚེ་གནས་ཉིད་ཡིན་པར་གསུངས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 3748]
ཡང་རིགས༌[^2569]པ་ནི་འདིར་ཞུགས་པ་ལ་གནས་ཉིད་ཙམ་དུ་རུང་བ་ཉིད་ཀྱིས༌[^2570]གནས་ཀྱི་ཁོངས་སུ་གཏོགས་པ༌[^2571]ཞེས་བྱ་བ་སྟེ་གཟུགས་ལ༌[^2572]ནི་མ་ཡིན་ཞེས་བྱ་བའོ།

[Block 3749]
[^2573] །དེའི་ཕྱིར་གནས་བསྟན་པར་བྱས་པའོ།[^2574] །

[Block 3750]
ད་ནི་འདི་ལ་ཉེན་ཀོར་བསྟན་པའི་ཕྱིར་ཉེན་ཀོར་ནི་ཁོ་ར་ཁོར་ཡུག་ཏུ་འདོམ་རེ་རེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེན་ཀོར་ནི་རྣམ་པ་གཉིས་ཏེ། བརྩམས་པ་ཉིད་ཀྱི་གནས་ཉིད་ཀྱི་ཁོངས་སུ་གཏོགས་པ་དང་། གནས་ངེས་པ་ལ་ལྷག་པར་གནས་ཤིང་བརྩམས་པའི༌[^2575]སྐབས་ལ་བརྩམས་པ༌[^2576]ཡང་དག་པར་གནས་ཞེས་བྱ་བའོ། །

[Block 3751]
ཉེན་ཀོར་དུ་གྱུར་པ་ཉིད་ཀྱི་དང་པོ་ལ་འདིར་བརྗོད་པ་ཉིད་དོ། །

[Block 3752]
ཁོར་ཡུག༌[^2577]ཏུ་འདོམ་རེ་རེའོ་ཞེས་བྱ་བའོ། །

[Block 3753]
ཕྱི་མ་ནི་དམིགས་ཀྱིས་བསལ་བར༌[^2578]གྱུར་པའོ། །

[Block 3754]
གྲོང་གསུམ་དང་འབྲེལ་པ་གནས་སོ་སོས༌[^2579]བརྩམས་པ་ཙམ༌[^2580]ནི་མ་ཡིན་ནོ། །

[Block 3755]
ལྷག་པར་གནས་པ་བརྩམས་པ་ལ་ཡང་གསུམ་སྟེ། ཉེན་ཀོར་ལ་ཡང་གྲུབ་པ་དང་། ཤིང་རྟ་ལ་སོགས་པ་རྣམས་ལ་འདིར་གཡོག་འཁོར་ཉིད་དོ། །

[Block 3756]
གྲུབ་པ་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། བཤང་བ་དང་གཅི་བ་དང་མི་གཙང་བའོ། །

[Block 3757]
ང་རྒྱལ་ཡང་ར་དང་ལུག་ལ་སོགས་པ་རྣམས་ཀྱི་རླུང་གིས༌[^2581]ངེས་པར་འབབ་པར་འགྱུར་བ་སྟེ། དེ་བས་ན་དེ་རྣམས་ལ་འདི་བརྟེན་པའོ། །

[Block 3758]
རྩིག༌[^2582]པས་བསྐོར་བའི་གྲོང་ལ་ནི་ཇི་ཙམ་དུ་བ་ལང་དྲུག༌[^2583]དང་ལྡན་པའི་ཤིང་རྟ་སྨྱིག་མ་ཅན་གྱིའམ་བྱ་གག་སྤར་ནས་འདུག་པའི་ལམ་གྱིས་ཁྱབ་པའོ་ཞེས་བྱ་བ། བྱ་གག་སྤར་ནས་འདུག་པའི་ཞེས་བྱ་བ་ནི་ལམ་ཇི་ཙམ་ན་འདུག་པ་དེ་ནི་འདིའམ་སྔ་མ་གང་ཡང་རུང་བ་ཉེན་ཀོར་ཡིན་ནོ། །

[Block 3759]
རིབ་མས༌[^2584]བསྐོར་བ་ལ་ནི་ར་ལུག་གི་རྡུལ་གྱི་འམ་མི་རང་བཞིན་གྱིས༌[^2585]ངོ་ཚ་བ་དང་ལྡན་པའི་བཤང་བའི་ལམ་གྱིས་སོ་ཞེས་བྱ་བ་ནི་མི་རང་བཞིན་གྱིས༌[^2586]ངོ་ཚ་བ་དང་ལྡན་པ་གང་ཡིན་པ་དེས་སྤྲོ་བས་འདིར་དེ་ནི་ཉེན་ཀོར་རམ་ཇི་སྲིད་དུ་རྡུལ་གྱིས་ཁྱབ་པ་ལའོ། །

[Block 3760]
འོབས་ཀྱིས་བསྐོར་བ་ལ་ནི་སྐས་གདང་བུ་བཅུ་གཉིས་པའི་འམ་ཕྱག་དར་བོར་བའི་བོང་བ་རགས་པའི་ལམ་གྱིས་སོ་ཞེས་བྱ་བ་ནི་ཕྱག་དར་བོར་བའི་བོང་བ་རགས་པ་ཡན་ལག་ཏུ་གྱུར་པའི་ལམ་གྱིས་ཁྱབ་པ་གང་ཡིན་པ་དེ་ནི་ཉེན་ཀོར་དུ་བརྗོད་དོ། །

[Block 3761]
བརྩམས་པ༌[^2587]ཉིད་ཀྱི་གནས་པ་ལ་ཉེན་ཀོར་ནང༌[^2588]དུ་འབྱུང་ཞིང་ཉེན་ཀོར་དུ་གྱུར་པ་ཉིད་ཀྱིས་གང་ཡིན་པ་དེ་ནི་བརྗོད་པར་བྱ་སྟེ། གནས་དེའི་འཕྲལ༌[^2589]གྱི་བྱ་བ་དང་འགྲོ་བ་དང་འདུག་པ་དང་རྡུལ་དག་གིས་དེར་གཏོགས་པ༌[^2590]ཁྱབ་པའོ་ཞེས་བྱ་བ་ནི་གནས་དེ༌[^2591]དང་འབྲེལ་པ་དེའི་འཕྲལ༌[^2592]གྱི་བྱ་བ་ཉིད་གང་ཡིན་པ་དང་འགྲོ་བ་དང་འདུག་པ་དང་རྡུལ་དེ་དག་གིས་སམ། དེ་ཇི་ཙམ་པ་དེར་གཏོགས་པ་དེའི་གནས་ཀྱི་ས་ཕྱོགས་ལ་ཁྱབ་པའོ། །

[Block 3762]
དེ་ཡང་ཉེ་བར་སྤྱོད་པ་གཞན་ནོ། །

[Block 3763]
དེའི་སྒྲ་ནི་འདིར་གཞན་གནས་པའོ། །

[Block 3764]
འཕྲལ་གྱི་བྱ་བ་ལ་སོགས་པ་ཁྱབ་པར་གྱུར་པ་ལ་གནས་གཞན་པ་ཉེ་བར་སྤྱོད་པ་ཉིད་ཐོབ་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་གང་དུ་ཡང་དེ་རྣམས་འདྲ་བར་བྱེད་པ་དང་། རྔོ༌[^2593]བར་བྱེད་པ་དང་། [^2594]འཐག་པར་བྱེད་པ་དང་། ཁྱིའུ་སུས་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཉེ་བར་སྤྱོད་པ་རིགས་ལ་སོགས་པ་གང་ཡིན་པ་དང་བརྗོད༌[^2595]པ་གང་ཡིན་པ་དེ་ནི༌[^2596]ཁོངས་སུ་གཏོགས་པ་བསྡུ་བའི་དོན་དུ་མདོ་འདི་བྱས་པའོ། །

[Block 3765]
མཚམས་མེད་པའི་ལམ་དུ་ཐ་དད་པ་མ་ཡིན་པར་འགྲོ་བའི་མི་ལ་ནི་འདོམ་བཞི་བཅུ་རྩ་དགུའོ་ཞེས་བྱ་བ་ནི་གང་དུ་བྱིན་གྱིས་རློབ་པར༌[^2597]བྱེད་པ་དེ་མངོན་པར་འགྲོ་བ་དེ་དང་མངོན་པར་ཕྱོགས་པར་འགྲོ་བ་གང་ལ་ཡོད་པ་དེ་ནི་ཐ་དད་པ་མ་ཡིན་པར་འགྲོ་བའོ། །

[Block 3766]
དེ་མཚམས་བཅད་པ་མ་ཡིན་པའི་ལམ་ལ་འཇུག་པར་གྱུར་པ་ལ་ཉེ་བར་སྤྱོད་པ་འདི་བྱས་སོ། །

[Block 3767]
མཚམས་བཅད་པ་དང་བཅས་པ་ལ་མཚམས་བཅད་པ་ཉིད་ཀྱིས་རྣམ་པར་གཞག་པ་རིགས་པ་ཡིན་ཏེ། ཞེང་དུ་ལམ་ཇི་ཙམ་གྱི་འགྲོ་བ་རྣམས་ལ་ལམ་གཅིག་ལ་ལྟུང་བ་ཉིད་སེམས་པར་བྱེད་པ་རྒྱས་པ་དེ་ཙམ་ལ་འདིར་འདི་ལ་ལམ་ཉིད་ཅེས་བྱ་བར༌[^2598]རིག་པར་བྱའོ། །

[Block 3768]
གང་ལ་གནས་དང་གནས་མ་ཡིན་པ་དག་ལ་བསམ་པ་དེ་ལ་འདི་ནི་གནས་ཉེ་བར་བཟུང་བ་ཞེས་བྱ་བ་སྐབས་ཀྱིས༌[^2599]རྟོགས་པའོ། །

[Block 3769]
མི་ལ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ལ་འདི་བཟུང་བའོ། །

[Block 3770]
འདིར་མོའི་མཚན་མ་འམ་སྐྱེས་པའི་མཚན་མ་གཙོ་བོ་མ་ཡིན་པ་དེ་ལ་ནི་འདོམ་བཞི་བཅུ་རྩ་དགུ་ཡན་ཆད་ཞེས༌[^2600]བྱ་བ་ཤིང་རྣམས་ཀྱིས༌[^2601]རྒྱས་པ་བདུན་པའི་ཚད་ཀྱིས་ལམ་གྱི་བར་གྱིས་བར་དུ་ཆོད་པར་བྱས་པ་ལ་ཤིན་ཏུ་རིང་བ་ཉིད་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 3771]
སྦྱར་བར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 3772]
འདི་ནི་དམིགས་ཀྱིས་བསལ་བ་སྟེ། དེ་བས་ན་ལམ་བརྒྱད་ཀྱི་ཐ་མ་ལ་འདིར་འདོམ་བཞི་བཅུ་རྩ་དགུ་ཚུན་ཆད་ལ་གྲངས་ཡིན་ཏེ། དེ་ལས་གཞན་པའི་འདོམ་གང་ཡིན་པ་དེ་ནི་མཐའ་ཚུན་ཆད་ལས་གཞན་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3773]
མཚམས་གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཉེས་པར་སྤྱོད་པ་ཐམས་ཅད་ཀྱི་སྐབས་སུ་གྱུར་པའི་ཉེས་པར་སྤྱོད་པའི་ཆོ་ག་ལ་དམིགས་ཀྱིས་བསལ་བ་འདི་ཡིན་ནོ། །

[Block 3774]
དབུས་ནས་རྒྱང་གྲགས་ཀྱི་མཐའ་ཕན་ཆད་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དབུས་སུ་གྱུར་པའི་ཡན་ལག་དང་པོར་བྱས་ཏེ། གང་ཞིག་རྒྱང་གྲགས་གང་ཡིན་པ་དེའི་མཐའ་མ་ལས་གཞན་པའི་ཐ་དད་པ་ཉིད་གནས་ཀྱི་མཚན་ཉིད་ཀྱིས་ཀྱང་ཞུགས་པ་མ་ཡིན་ན་ཉེ་བར་སྤྱོད་པའི་མཚན་ཉིད་ཀྱིས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3775]
གནས་དང་ཉེ་བར་སྤྱོད་པའི་ཆོ་ག་རྣམ་པ་གཉིས་ཀ་ལ་ཡང་འདི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 3776]
ལུང་ནི་གཞུང་བསྟན་པའི་ཕྱིར་ནགས་ཞེས་བྱ་བ་ནི་ཤིང་ལྗོན་པའི་གནས་སོ། །

[Block 3777]
དེ་ལ་ཇི་སྲིད་དུ་ཡལ་ག་དང་ལོ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་ལ་ཕན་ཚུན་འབྲེལ་པར་གྱུར་པ་དེར་དགེ་སློང་གི་རྒྱང་གྲགས་ཁོ་ར་ཁོར་ཡུག་གར༌[^2602]དགའ་བར་ཆོས་གོས་བཞག་སྟེ་དེར་གར་དགའ་བར་སྐྱ་རེངས༌[^2603]འཆར་བར་བྱའོ་ཞེས་མ་མོ་ལས་གསུངས་པ་ཡིན་ཏེ་གནས་རྣམས་ཐམས་ཅད་ལ་ཆོ་ག་འདིས་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་བར་རྣམ་པར་གཞག་གོ། །

[Block 3778]
འབྲལ་བའི་སྤང་བ་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3779]
དམ་དུམ་དུ་གྱུར་པ་ལ་བྱིན་གྱིས་བརླབ་པ་མེད་པར་མི་འགྱུར་རོ། །

[Block 3780]
སྤང་བ་ལ་ནི་མི་འཆགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྤང་བར་བྱ་བའི་དངོས་པོ་ལ་བྱིན་གྱིས་བརླབ་པ་མི་འཆགས་པར་མི་འགྱུར་བ་སྟེ་རང་ཉིད་དང་མ་བྲལ་བའི་ཕྱིར་རོ། །

[Block 3781]
གཞུང་ཁ་ཅིག་ལས་དགེ་སློང་གིས་ཆོས་གོས་དེ་ཉིད་དགུང་བཅུ༌[^2604]འདས་པ་ཡང་ལགས་ལ་དགུང་གཅིག་བྲལ་བ་ཡང་ལགས་པ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། ཆོས་གོས་ཞག་བཅུ་འདས་པ་ཡང་ཡིན་ལ་དགེ་སློང་གིས་ཀྱང་དེ་བྱིན་གྱིས་བརླབས་ཏེ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སྐྱ་རེངས༌[^2605]འཆར་བར་བྱེད་པའོ་ཞེས་གསུངས་ཏེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3782]
དགེ་སློང་གིས་ཀྱང་དེ་བྱིན་གྱིས་བརླབས་ནས་ཞེས་བྱ་བ་ལ་དེ་བྱིན་གྱིས༌[^2606]བརླབས་ཏེ་ཞེས་བྱ་བའི་ཚིག་ནི་འདིར་འཆད་པ་ཞེས་མཐོང་བ་ཡིན་ནོ། །

[Block 3783]
དགེ་འདུན་གྱི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབས་པ་མི་འཆགས་པ་མ་ཡིན་ནོ། །

[Block 3784]
རང་ཉིད་ཁོ་ནས་དགེ་སློང་ལ་དགེ་འདུན་གྱི་ཉེ་བར་ལོངས་སྤྱོད་པའི་དུས་ན་རྣམ་པར་གཞག་པ་དེ་བཞིན་དུ་མང་པོ་ཡོངས་སུ་ཐོབ་པ་རེ་རེ་ནས་ཉེ་བར་ལོངས་སྤྱོད་པ་ལ་མང་པོ་དང་འབྲེལ་པའི་དོན་ཉིད་ཀྱི་ཕྱིར་དེ་ལས་འབྲལ་བར་འགྱུར་རོ། །

[Block 3785]
དེ་ལས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་བྱིན་གྱིས་བརླབས་པ་དེ་ལས་འདིར་བྱིན་གྱིས་བརླབས་པ་བཟུང་བ་ནི་རྒྱུ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་བཟུང་བ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
