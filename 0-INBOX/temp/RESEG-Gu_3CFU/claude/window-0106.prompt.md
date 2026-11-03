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
འདི་ནི་ཆོས་གོས་ཀྱི་གནས་ལ་ཐོབ་པ་མི་སྲིད་པ་ལ་སླར་ཆོ་གའི་རྣམ་པ་སྟེ་ཐབས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3712]
སྣམ་སྦྱར་ལྕི་བ་ཉིད་ཡིན་ན་རྒན་པོ་དང་ནད་པ་དག་ལ་མི་འབྲལ་པའི་གནང་བ་སྦྱིན་ནོ་ཞེས་བྱ་བ་སྟེ་འབྲལ་པའི་སྤང་བའི་ཐབས་སོ། །

[Block 3713]
གང་ལ་གནང་བ༌[^2543]དང་སྤང་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་ཉིད་ཅེ་ན། དེའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ་དང་གནང་བ་མ་ཐོབ་པ་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་ཞེས་བྱ་བ་འདི་ལ་གོས་ཀྱི་དངོས་པོར་ཡོངས་སུ་གྱུར་པ་ལ་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 3714]
དེ་བས་ན་ལྷུང་བཟེད་ལ་སྐབས་མ་ཡིན་ནོ། །

[Block 3715]
བྱིན་གྱིས་བརླབས་པའི་གོས༌[^2544]ལ་གང་ཟག་གནང་བ་མ་ཐོབ་པ་ནི་ལྷུང་བའི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3716]
འདིར་ནི་གནས་སྐབས་ཐམས་ཅད་ལ་གང་ཟག་དེ་བྱེད་པ་པོ་ཉིད༌[^2545]མ་ཡིན་ཏེ། དེ་ལ་བདེན་པ་ལ་འདི་གང་ཡིན་པ་དེར་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེའི་གནས་ཉེན་ཀོར་དང་བཅས་པ་ནས་གཞན་ན་གནས་པ་ལ་སྐྱ་རེངས༌[^2546]ཤར་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་གོས་བྱིན་གྱིས་བརླབས་པ་དེའི་གནས་གང་ཡིན་པ་གནས་པའི་ས་དེ་ཉེ་བར་སྤྱད་པས་ཀྱང་གནས་གཞན་ན་གནས་པ་ལ་སྟེ་གང་ཡང་རུང་བ་གཅིག༌[^2547]གི་དུས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3717]
འོན་ཀྱང་སྐྱ་རེངས༌[^2548]ཤར་བ་ལ་གང་གིས་དེ་བྱིན་གྱིས་བརླབས་པ་དེ་ལ་ཞེས་བྱ་བ་འདི་སྐྱ་རེངས༌[^2549]ཤར་བ་ལ་འབྲེལ་པ་ཅན་གྱི་སྒྲ་ཉིད་ཀྱི་ཕྱིར་ཤེས་པར་བྱའོ། །

[Block 3718]
འདིར་བཟུང་བ་ཙམ་ནི་གནས་མ་ཡིན་ཏེ་དེ་བས་ན་འདི་ལ་མཚམས་བརྗོད་པར་བྱའོ། །

[Block 3719]
མཚམས་བྱས་པ་ལ་མཚམས་གནས༌[^2550]ཀྱི་མཐའོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཡོལ་བ་དང་རྩིག་པ་དང་རིབ་མ་དང་འོབས་ཀྱིས་བསྐོར་བ་ལ་སོགས་པ་དག་ཀྱང་མཚམས་ཉིད་ཡིན་ནོ། །

[Block 3720]
མཚམས་བཅད་པ་འབའ་ཞིག་མཚམས་ཡིན་པར་ནི་མ་ཟད་དེ་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བའི་ཕྱིར་རོ། །

[Block 3721]
ཇི་ལྟར༌[^2551]བདག་པོ་གཅིག་པ་ཉིད་མ་ཡིན་པའི་བར་གྱི་མཚམས་རྣམ་པ༌[^2552]ཐ་དད་པ་ཉིད་ཡིན་པ་དེ་བཞིན་དུ་བདག་པོ་གཅིག་ཉིད་ཀྱི་བར་གྱི་མཚམས་རྣམས་ནི་ཐ་དད་པ་ཉིད་དུ་མི་འགྱུར་བས་དེའི་ཕྱིར་བདག་པོ་གཅིག་ཉིད་མ་ཡིན་པའི་བར་གྱི་མཚམས་རྣམས་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་རབ་ཏུ་འབྱེད་པས་མང་བའི་བདག་པོ་རྣམས་ལ་གཉེན་གཅིག་པའི་རིགས་པས་གནས་པ་དེ་ལ་ཆོ་ག་འདི་མི་འཇུག་པའོ། །

[Block 3722]
མཚམས་གཞན་ལ་ཡང་དེ་ཉིད་ལ་བདག་པོ་ཉིད་དོ། །

[Block 3723]
གནས་སོ་སོར་ནི་བདག་པོ་ཐ་དད་པ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 3724]
གང་ཞིག་སྣ་ཚོགས་པ་ཉེ་བར་སྤྱོད་པའི་རིགས་ལ་ཕྱི་སྒོ་ལ་སོགས་པ་ཐུན་མོང་པའི་དངོས་པོ་བརྗོད་པ་ནི་ཡུལ་གྱི་ཚོམས་དང་། མུ་སྟེགས་ཅན་གྱི་ཁྱིམ་དང་། ཚོང་ཁང་དང་། ཚོང་རྡལ་དང་། གཞག་སྟེགས་དང་། འདུག་སྟེགས་དང་། དགྲ་ཁང་དང་། གཡུལ་དང་། དཀྱིལ་དང་། རྒྱལ་མཚན་གྱི་ཤིང་བསྒྲེང་བ་དང་། ཤིང་རྟ་དང་། ཁ་ལོ་བའི་གནས་ཞེས་བྱ་བ་དང་། གྲུ་ལ་དང་། གྲུ་དོང༌[^2553]དང་། ཀུན་དགའ་ར་བ་ནི་ཁྲོན་པ་ཐུན་མོང་ཡིན་ཏེ། ཐམས་ཅད་ལ་དེ་དང་ཁྱིམ་པ་ལ་སོགས་པར་འཇུག་པ་ལ་ནི་ཞུགས་པའི་བདག་པོ་རྣམས་དེ་ཡོངས་སུ་གཅོད་པ༌[^2554]ཉིད་ཀྱི་སྒོ་བ༌[^2555]ལ་སོགས་པ་རྣམས་ལ་ཞེན་པ་ཞེས་བྱ་བ་འདིས་ཤེས་པའོ། །

[Block 3725]
ནོར་ལས་དང་ལྟ་བ་ལས་ཐ་དད་པས་ཐ་དད་པ་མ་ཡིན་པའི་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ནོར་ལས་ནི་འདི་ལྟ་སྟེ་དཔེར་ན་སྤུན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 3726]
ལྟ་བ་ལས་ནི་མུ་སྟེགས་ཅན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 3727]
མ་བགོས་པ་ནི་ཡོངས་སུ་བཟུང་བ་པོ་རྣམས་སོ། །

[Block 3728]
གཞན་མཚམས་ཀྱང་ཐ་དད་པ་ཉིད་མ་ཡིན་ཏེ། གནས་འགོད་པ་ལ་ཐ༌[^2556]དད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3729]
ཡལ་ག་དང་ཡལ་ག་ཕྲ་མོ་དག་མ་རེག་པ་ནི་གནས་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་མི་རེག་པ་ནི་མ་རེག་པ་སྟེ་ཕན་ཚུན་མ་ཕྲད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3730]
དེ་ཡོད་པ་ལ་གནས་ཐ་དད་པ་ཉིད་དེ་འདི་རྣམས་མ༌[^2557]འདྲེས་པ་ལ་གནས་གཅིག་པ་ཉིད་ཅེས་བྱ་བ་འདི་དང་བྱས་པར་རིག་པར་བྱའོ། །

[Block 3731]
རྩ་བ་ནི་ཐུན་མོང་ངོ་ཞེས་བྱ་བ་ནི་ཡལ་ག་དེ་དག་གི་རྩ་བ་ནི་ཐུན་མོང་བའོ། །

[Block 3732]
རྩ་བའི་རྩ་བ་ལ་སོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱོགས་གང་ལས་ཡལ་ག་དུ༌[^2558]གྱེས་པར་གྱུར་པ་དེའི་མོད༌[^2559]ཁོ་ནའི་འོག་ན་ཡལ་ག་མེད་པའི་ཤིང་ལྗོན་པའི་ལྡོང་པོའི་ཕྱོགས་ལ་བྱ་སྟེ་དེ་ནི་རྩ་བའོ། །

[Block 3733]
དེ་ལ་དེ་ལྟ་བུ་ཉིད་ཀྱི་ཡལ་ག་གཅིག་ཏུ་གྱུར་ཏམ་ཡལ་ག་དུ་མར་གྱུར་པའི་ཆུང་ངུ་འམ་ཆེན་པོ་འམ་ཕྲ་བ་འམ༌[^2560]རགས་པའི་ཤིང་ལྗོན་པ་དང་ལྷན་ཅིག་ཏུ་གང་དུ་གཅིག་པ་ཉིད་དེའི་མཐའ་ཅན་འདིར་རྟེན་ཡལ་ག་མེད་པ་ཤིང་ལྗོན་པའི་སྡོང་པོའི་ཕྱོགས་ལ་བྱ་སྟེ། དེ་ནི་རྩ་བའི་རྩ་བར་རིག་པར་བྱའོ། །

[Block 3734]
སོགས་པའི་སྒྲས་ནི་དེ་མན་ཆད་ནས་ས༌[^2561]གཞི་ལ་ཐུག་པ་ཡན་ཆད་ཀྱི་བར་བཟུང་སྟེ་དེ་རྣམས་ཉེ་བར་སྡུད་པའོ། །

[Block 3735]
གང་གི་གང་རྣམས་ལ་རྩ་བ་ཉིད་དེའི་དེ༌[^2562]རྣམས་ཐུན་མོང་བ་ཉིད་དོ། །

[Block 3736]
འདིར་གཞུང་ནི་འདི་ལྟ་སྟེ་ཤིང་ལྗོན་པ་ཡལ་ག་དང་ལོ་མ་མ་རེག་པ་དེའི་ཉེན་ཀོར་གང་ལགས། སོ་སོ་ཐ་དད་པའོ། །

[Block 3737]
ཇི་ཞིག་ཐུན་མོང་ལགས་རྩ་བའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3738]
ཡལ་ག་དང་ལོ་མ་རེག་པའི་ཤིང་ལྗོན་པ་རྣམས་ནི་གནས་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་ལ་ཡལ་ག་རྒྱས་པར་འགྱུར་བ་ཉིད་དེ་དེ་བས་ན་སོ་སོར་མ་སྨོས་སོ། །

[Block 3739]
ཤིང་ལྗོན་པ་རྣམས་ཞེས་བྱ་བ་ནི་ཤིང་དག་དང་ཤིང་རྣམས་ལའོ། །

[Block 3740]
དེའི་ཆ་འོག་མར་སྦྱངས་པ་ནི་སྟེང་གཡོགས༌[^2563]དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་བླ་གབ་ཀྱི་རིམ་པའི་ཆ་འོག་མ་དེའི་གནས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་དེ་བཞིན་དུ་འདིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3741]
གྲུ་དང་ཤིང་རྟ་དག་གི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆ་འོག་མ་ཡང་སྟེང་གཡོགས་དང་འདྲ་བར་ཁོངས་སུ་གཏོགས་པར་ཤེས་པར་བྱའོ། །

[Block 3742]
ནམ་མཁའ་ནི་མཚམས་སུ་གཏོགས་པ་མ་ཡིན་ནོ། །

[Block 3743]
དེ་བས་ན་དེ་དང་འབྲེལ་པ་སྟེང་གི་ངོས་དང་འབྲེལ་པའི་རྫས་ནི་མདོ་འདི་གཉིས་ཀྱིས༌[^2564]གནས་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3744]
མཚམས་མེད་པ་ལ་ནི་ཡན་ལག་གིས་ཁྱབ་པ་མཐའོ་ཞེས་བྱ་བ་ནི་ལྷག་པར་གནས་པ་འམ་དེའི་རྣམ་པའི་ཤིང་གཅོད་པ་ལ་སོགས་པ་ལ་རྣམ་པར་གཅོད་པ་ནི་འདིར་མཚམས་བཅད་པ་སྟེ། དེ་མེད་པ་ལ་འདི་རྣམས་མཚམས་བཅད་པ་མེད་པ་ཉིད་ཀྱི་ཚིག་གོ། །

[Block 3745]
ཁྱབ་པ་ནི་གནས་ཏེ་དེར་ཡལ་ག༌[^2565]གང་ཡིན་པ་དེའི་མཐར་ཐུག་པ་ནི་གནས་ཀྱི་མཐར་ཐུག་པའོ། །

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
--- END BLOCKS ---
