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
[Block 3711]
སྦྱོར་བ་ནི་གང་དང་གང་ཁྱད་པར་ཅན༌[^2333]གྱི་བུད་ཤིང་སྐམ་པོའི་རྒྱུ༌[^2334]ལས་མེ་ལ་སོགས་པ་དེ་དང་དེ་རྣམས་སྲེག་པ༌[^2335]དང་། འཚོད་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པར་མཐོང་ངོ་།[^2336] །བསམ་པ་བཟང་པོས་ཉེ་བར་སྤྱོད་པའི་འདོད་པའི་ཡོན་ཏན་ལྔ་ཁྱད་པར་ཅན་གྱི་ཐར་པའི་མཚན་ཉིད་ཅན་གྱི་འབྲས་བུ་སྟེར་བར་འགྱུར་ཞེས་མཐུན་པའི་དཔེའོ། །

[Block 3712]
གང་རྒྱུ་ཁྱད་པར་ཅན་ལས་མ་སྐྱེས་པ་མེ་ལ་སོགས་པ་དེ་དག་དོན་གྱི་བྱ་བ་སྒྲུབ་པར་བྱེད་པར་མི་ནུས་ཏེ། ཁྱད་པར་མ་ཡིན་པའི་བསམ་པས་གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་སྤྱད་པར་གྱུར་པ་ན་ཁྱད་པར་ཅན་གྱི་འབྲས་བུ་སྟེར་བར་བྱེད་པར་མི་འགྱུར་ཞེས་མི་མཐུན་པའི་དཔེའོ། །

[Block 3713]
རྒྱུ་ཁྱད་པར་ཅན་གྱི་བསམ་པས་གཟུགས་ལ་སོགས་པ་རང་བཞིན་གྱི་གཏན་ཚིགས་སོ། །

[Block 3714]
དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཐབས་ལ་མཁས་པ་ཉིད་གང་གིས་ཡུལ་རྣམས་སྤྱད་པ་ན་ཡང་དེ་ཞེན་པ་ལས་བྱུང་བའི་སྐྱོན་རྣམས་ཀྱིས་གོས་པར་མི་འགྱུར་ཏེ་པདྨ་བཞིན་ནོ་ཞེས་དཔེའོ། །

[Block 3715]
རིགས་པ༌[^2337]འདིས་དེ་ཉིད་འཇིགས་པར་མཛད་པ་ན་ཞེས་གསུངས་སོ། །

[Block 3716]
དྲང་བའི་དོན་ནི་ཐབས་ལ་མཁས་པ་ཉིད་ཙམ་བསྟན་པས་སོ། །

[Block 3717]
པདྨ་ནི་སྐྱེ་གནས་ཞེས་པ་ལ། ཕྱག་རྒྱའི་ཆོས་འབྱུང་བའོ། །

[Block 3718]
མཐར་ནི་ནང་སྟེ། འདོད་པའི་གདུགས་སོ། །

[Block 3719]
དེར་དབང་པོ་གཉིས་སྙོམས་པར་ཞུགས་པའི་ཐབས་ཀྱིས་ཞེས་པ་ནི་གསང་བའི་རྡོ་རྗེ་དང་ཆུ་སྐྱེས་དང་ཕྲད་པའི་མཚན་ཉིད་ཀྱིས་སོ། །

[Block 3720]
མཆོག་ཏུ་དགའ་བའི་བདེ་བ་ཞེས་པ་ནི་ཐ་མལ་པ་མ་ཡིན་པའི་བདེ་བ་ཆེན་པོ་སྐྱེད་པར༌[^2338]བྱེད་ཅིང་གསལ་བར་མཛད་དོ། །

[Block 3721]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ། པདྨ་མཐར་བྱེད་འོད་དཔག་ཏུ་མེད་པའི་རིགས་ཅན་ཡིན་པས་བྱང་ཆུབ་སེམས་ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 3722]
དེ་ཡོད་པས་མཆོག་ཏུ་དགའ་བ་ཡང་དག་པར་འགྱུར་གྱིས་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 3723]
པདྨ་རྡོ་རྗེའི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་།

[Block 3724 [VERSE]]
དངོས་གྲུབ་ཀུན་གྱི་གཏེར་གྱུར་པའི། །
བྱང་ཆུབ་སེམས་ནི་ལྷུང་གྱུར༌[^2339]ན། །
རྣམ་ཤེས་ཕུང་པོ་བརྒྱལ༌[^2340]འགྱུར་བས། །
བླ་མེད་དངོས་གྲུབ་ག་ལས་འགྱུར། །

[Block 3725]
ཞེས་འབྱུང་བས་སོ། །

[Block 3726]
རྡོ་རྗེ་ཕྲེང་བ་ལས་ཀྱང་།

[Block 3727 [VERSE]]
རིན་ཆེན་རྒྱལ་པོ་དཔག་མེད་གཉིས། །
འཁོར་བ་བསྒྲུབ་པའི༌[^2341]རྩ་བ་ཡིན། །

[Block 3728]
ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་། །

[Block 3729]
དེ་ལྟ༌[^2342]ན་ཡང་སྙོམས་པར་ཞུགས་པའི་ཐབས་ཀྱིས་བདེ་བ་ཆེན་པོ་སྐྱེ་བར་འགྱུར་ཞེས་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནམ་མཁའ་བཞིན་དུ་འདུས་མ་བྱས་པའི་ཕྱིར་རོ། །

[Block 3730]
གང་གི་ཕྱིར་རྒྱུ་གང་གིས་ཀྱང་ནམ་མཁའ་མི་བསྐྱེད༌[^2343]ཅིང་འགོག་པར་ཡང་མི་ནུས་ཏེ། རྟག་པར༌[^2344]ཡིན་པའི་ཕྱིར་རོ། །

[Block 3731]
དེ་བཞིན་དུ་ནི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཆོས་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་ཐབས་གང་གིས་ཀྱང་མི་བསྐྱེད༌[^2345]ཅིང་འགོག་པར་ཡང་མི་ནུས་སོ། །

[Block 3732]
གལ་ཏེ་དེ་ནི་བསྐྱེད་པར་བྱ་བ་ཡིན་ན་ནི་དེའི་ཚེ། འདུས་བྱས་པས་འཇིག༌[^2346]པའི་ཆོས་ཅན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 3733]
འཇིམ་པ་ལ་སོགས་པའི་རྒྱུ་རྣམས་ཀྱིས་བསྐྱེད་པར་འགྱུར་བའི་བུམ་པ་བཞིན་ནོ། །

[Block 3734]
གང་གི་ཕྱིར་ཆོས་ཉིད་ནི་ཆོས་གང་གིས༌[^2347]ཀྱང་འབྲེལ་པར་མི་འགྱུར་ཞིང་བྲལ་བར་ཡང་མི་འགྱུར་རོ། །

[Block 3735]
དེ་དང་ལྡན་པ་ཡིན་ན་ཐ་མལ་པའི་སྐྱེས་བུ་བཞིན་དུ་བྱིས་པ་དང་། ལང་ཚོ་དང་། གནས་སྐབས་བར་པ་དང་། རྒས་པ་དང་། ཤི་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 3736]
འཕགས་པ་བྱམས་པས། །

[Block 3737 [VERSE]]
ཆོས་ཀྱི་དབྱིངས་ནི་དབྱེར་མེད་ཅིང་། །
རིགས་ནི་ཐ་དད་རུང་མ་ཡིན། །
གཞི་ཡི་ཆོས་ཀྱི་དབྱེ་བ་ཡིས། །
དེ་ཡི་དབྱེ་བ་རབ་ཏུ་གྲགས། །

[Block 3738]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ།

[Block 3739 [VERSE]]
ཇི་ལྟར་རློན་པ་ཆུ་ཤིང་སྡོང་བུ་ནི། །
སྙིང་པོ་འདོད་པའི་སྐྱེས་བུས་རྣམ་དཔྱད༌[^2348]ན། །
ཕྱི་དང་ནང་མེད་སྙིང་པོ་ཡོད་མི་སྣང་། །
དེ་ལྟར་ཆོས་རྣམས་ཐམས་ཅད་ཤེས་པར་གྱིས། །

[Block 3740]
ཞེས་འབྱུང་ངོ་། །

[Block 3741 [VERSE]]
རིགས་པ་དྲུག་ཅུ་པ་ལས་ཀྱང་། །
མི་རྟག་བསླུས་པའི་ཆོས་དང་ལྡན། །
ཁོང་སྟོང་སྟོང་པ་བདག་མེད་པ། །
དངོས་དང་དངོས་མེད་ལ་མཁས་པས། །

[Block 3742 [VERSE]]
རྣམ་པར་དབེན་པ་ཞེས་མཐོང་ངོ་། །
རྟོག་པ་མེད་ཅིང་དམིགས་པ་མེད། །
བཀོད་པ་མེད་ཅིང་གནས་མེད་པ། །
མ་རིག་ས་བོན་ལས་བྱུང་བའི། །

[Block 3743 [VERSE]]
ཐོག་མ་ཐ་མ་བར་མ་མེད། །
ཆུ་ཤིང་ནང་ལྟར་སྙིང་པོ་མེད། །
དྲི་ཟའི་གྲོང་ཁྱེར་དང་མཚུངས་པ། །
གཞན་དག་རྨུགས་བྱེད་འཇིགས་པ་སྟེ། །

[Block 3744]
འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ།

[Block 3745 [VERSE]]
བདག་ལས་མ་ཡིན་གཞན་ལས་མིན། །
གཉིས་ཀ་ལས་མིན་རྒྱུ་མེད་མིན། །
དངོས་པོ་གང་དང་གང་དུ་ཡང་། །
སྐྱེ་བ་ནམ་ཡང་འཐད་མ་ཡིན། །

[Block 3746]
ཞེས་འབྱུང་ངོ་། །

[Block 3747 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
འདིར་ནི་ཁ་ཅིག་མི་སྐྱེ་ཞིང་། །
ཁ་ཅིག་ཀྱང་ནི་འཆི་མི་འགྱུར། །
སེམས་ཀྱི་ངོ་བོར་རྣམ་གནས་པའི། །

[Block 3748]
འཁོར་བ་ཉིད་དུ་ཤེས་པར་བྱ། །ཞེས་འབྱུང་ངོ་། །

[Block 3749 [VERSE]]
སྲིད་པ་འཕོ་བའི་མདོ་ལས་ཀྱང་། །
དངོས་པོ་ལས་ཀྱང་དངོས་མི་སྐྱེ། །
དངོས་མེད་ལས་ཀྱང་སྐྱེ་མི་འགྱུར། །
དངོས་པོ་རྟག་ཏུ་སྐྱེ་བ་ནི། །

[Block 3750]
འཁྲུལ་པས་ནམ་མཁའི་མེ་ཏོག་བཞིན། །ཞེས་འབྱུང་ངོ་། །
--- END BLOCKS ---
