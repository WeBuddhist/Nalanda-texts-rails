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
[Block 3886]
དེས་མཛེས་པ་གང་ཡིན་པ་དེ་ནི་རྨ་བྱའི་མདོངས་མཛེས་པར་གྱུར་པའོ། །

[Block 3887]
དེ་དག་གི་ཅོང་ཅོང་གི་སྒྲ་འབྱིན་པ་ནི་རྨ་བྱའི་སྒྲ་ཅོང་ཅོང་དུ་འབྱིན་པའོ། །

[Block 3888]
དེས་མགུ་བར་བྱེད་པ་ནི་སྒྲ་བསྒྲགས་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3889]
གར་གྱི་བྱེད་པ་ནི་གར་བྱེད་པ་སྟེ། དེ་དག་བྱེད་པའོ། །

[Block 3890]
ཕྲ་མོ་ཉིད་བྱ་ཡིན་པས་བྲན་ནོ། །

[Block 3891]
ཡང་ན་བྱ་དང་བྲན་མང་པོ་ནི་བྱ་བྲན་མང་པོའོ། །

[Block 3892]
མེ་ཏོག་ཀ་དམ་པ་དང་། སརྫ་དང་། ཨརྫུ་ན་དང་། ཀེ་ཏ་ཀའི་དྲི་ཞིམ་པོས་བསྒོས་པ་གང་ཡིན་པ་དེ་ནི་མེ་ཏོག་ཀ་དམ་པ་དང་། སརྫ་དང་། ཨརྫུ་ན་དང་། ཀེ་ཏ་ཀའི་དྲི་ཞིམ་པོས་བསྒོས་པའོ། །

[Block 3893]
གླེང་ལངས་པ་ནི་བརྩམས་པའོ། །

[Block 3894]
ཡུལ་དང་ཕྱོགས་ནི་ཡུལ་དང་ཕྱོགས་སོ། །

[Block 3895]
དེ་རྣམས་ཀྱི༌[^2514]གཏམ་ནི་ཡུལ་དང་ཡུལ༌[^2515]ཕྱོགས་རྣམས་ཀྱི་གཏམ་མོ། །

[Block 3896]
དེས་ཞེས་བྱ་བ་ནི་ངང་པ་ཁྱོ༌[^2516]ཤུག་གཉིས་ཀྱིས་སོ། །

[Block 3897]
བསྔགས་པ་རྨད་དུ་བྱུང་བར་བཟང་པོའི་མཚོ་གང་ཡིན་པ་དེ་ནི་རྨད་དུ་བྱུང་བར་བཟང་བའི་ཡོན་ཏན་རྣམས་སོ། །

[Block 3898]
ཡོན་ཏན་ཆེ་བ་བརྗོད་པར་མི་ནུས་པ་སྟེ། བརྗོད་ཀྱིས༌[^2517]མི་ལང་བའི་ཡོན་ཏན་གང་ལ་ཡོད་པ་དེ་ནི་ཡོན་ཏན་བརྗོད་ཀྱིས༌[^2518]མི་ལང་བའོ། །

[Block 3899]
འཇིགས་པ་དང་བག་ཚ་བ་ནི་འཇིགས་ཤིང་བག་ཚ་བའོ། །

[Block 3900]
འཇིགས་པ་དང་བག་ཚ་བ་མ་མཆིས་པ་གང་ཡིན་པ་དེ་ནི༌[^2519]འཇིགས་པ་དང་། བག་ཚ་བ་མ་མཆིས་པའོ། །

[Block 3901]
གྲོས་འདྲི་བའི་ཚིག་དང་ཡི་གེ་གསལ་བ་གང་ཡིན་པ་དེ་ནི་གྲོས་འདྲི་བའི་ཚིག་དང་ཡི་གེ་གསལ་བའོ། །

[Block 3902]
ཇི་ལྟར་ཆགས་པའི་གནས་ཡིན་ཞེ་ན་སྨྲས་པ། ཤ་བཟར་རུང་བ་དང་། བལྟ་ན་སྡུག་པའི་ཕྱིར་ཏེ། བལྟ་ན་སྡུག་པ༌[^2520]ནི་ཡིད་དུ་འོང་བའོ། །

[Block 3903]
ཤ་བཟར་རུང་བ་ནི་བཟའ་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3904]
འདི་གཉིས་ཀྱི་རྒྱུས་བདག་ཅག་གཟུང་བ༌[^2521]དང་གསད་པར༌[^2522]འོས་པ་ཉིད་ཡིན་ཏེ། འདིས་ནི་བདག་ཅག་ཉིད་ཀྱི་རང་བཞིན་བསྟན་ཏོ། །

[Block 3905]
འདིས་ནི་ཅིས་ཀྱང་ཕོངས་པ་མ་མཆིས་སོ་ཞེས་བྱ་བ་ནི་ཅི་སྟེ་བདག་ཉིད་ཀྱི་གནས་ཆགས་པར་བྱ་བ་མེད་ན་ནི་གནས་ངན་པའི་ཕྱིར་དེ་ཡོངས་སུ་གཏང་བར་བྱ་བ་ཡིན་ན་དེ་ཡང་མ་ཡིན་ནོ། །

[Block 3906]
གནས་དེར་འགྲོ་བའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར། །ཚིག་འཇམ་པོ་བཅོས་མ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ཏེ། ཕྱི་བཞག་ཅན་དུ་སྨྲ་བ་ནི་ཕྱི་བཞག་ཅན་དུ་སྨྲ༌[^2523]བའོ། །

[Block 3907]
ཚིག་འཇམ་པོ༌[^2524]བཅོས་མ་ཉིད་ཕྱི་བཞག་ཅན་དུ་སྨྲ་བ་ནི་ཚིག་འཇམ་པོ་བཅོས་མ་ཕྱི་བཞག་ཅན་དུ་སྨྲ་བའོ། །

[Block 3908]
རང་བཞིན་ངན་པའི་དངོས་པོ་ཉིད་གནོད་པར་སེམས་པ་ཉིད་ཡིན་པས་གནོད་པར་སེམས་པའི་རང་བཞིན་ངན་པའོ། །

[Block 3909]
ཚིག་འཇམ་པོ༌[^2525]བཅོས་མ་དང༌[^2526]ཕྱི་བཞག་ཅན་དུ་སྨྲ་བ་གཉིས་ཀྱིས་མི་མངོན་པར་བྱས་པའི་གནོད་པར་སེམས་པའི་རང་བཞིན་གང་ཡིན་པ་པ་དེ་ནི་ཚིག་འཇམ་པོ༌[^2527]བཅོས་མ་ཕྱི་བཞག་ཏུ་སྨྲ་ལ༌[^2528]གནོད་པར་སེམས་པའི་རང་བཞིན་མི་མངོན་པར་བྱེད་པའོ། །

[Block 3910]
ཆུང་བ་དང༌[^2529]དམན་པའི་སྙིང་རྗེ་གང་ལ་ཡོད་པ་དེ་ནི་སྙིང་རྗེ་ཆུང་བའོ། །

[Block 3911]
དོན་གྱི་རྗེས་སུ་འགྲོ་བ་ནི་དོན་མཐུན་པར་བྱེད་པའོ། །

[Block 3912]
སྨྲ་བ་དང་སེམས་པ༌[^2530]མཐུན་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་སྨྲ་བ་དང་སེམས་པ་མཐུན་པའོ། །

[Block 3913]
ཕལ་ཆེར་ཞེས་བྱ་བ་ནི་བྱ་དང་རི་དགས་ཐམས་ཅད་ནི་མ་ཡིན་པ་སྟེ། དེ་ཡང་དེ་དག་ལས་མི་རྣམས་ཀྱིས་བསླབས་པ་ཁ་ཅིག་ནི་སྨྲ་བ་དང་། སེམས་པ་མཐུན་པར་བྱེད་པ་མ་ཡིན་པས་སོ། །

[Block 3914]
མིའི་ནང་ན་ཁ་ཅིག་ཅེས་བྱ་བ་ནི་དམ་པ་རྣམས་མ་གཏོགས་པར་ཏེ།[^2531] དེ་ནི་སྨྲ་བ་དང་། སེམས་པ་མཐུན་པར་བྱེད་པ་ཉིད་དོ། །

[Block 3915]
དེ་དག་ལས་བཟློག་པ་ནི་དེ་ལས་བཟློག་པའི་ཚུལ་ཏེ། དེ་ལས་མཁས་པ་དེ་ནི་དེ་ལས་བཟློག་པའི་ཚུལ་ལ་མཁས་པ་སྟེ། སྨྲ་བ་དང་སེམས་པ་མཐུན་པར་བྱེད་པའམ། སྨྲ་བ་དང་སེམས་པ་མི༌[^2532]མཐུན་པ་མེད་པ་ལས་སོ། །

[Block 3916]
དེ་ལས་བཟློག་པ་མཁས་པ་ཉིད་བསྟན་པའི་ཕྱིར། འཇམ་ཞིང་སྙན་པའི་ཚིག་སྨྲ་ཡང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3917]
ད་ལྟར་ནི་སྙན་ལ་མ་འོངས་པ་ན་ནི་དོན་དང་མཐུན་པ་མེད་ཅིང་སྐྱོན་དང་བཅས་པས་གནོད་པ་ཡིན་ཏེ། འདིར་སྙན་པ་སྨྲ་བ་ཡིན་ན་ཡང་སྐྱོན་དང་བཅས་སོ་ཞེས་བྱ་བར་བསྟན་ཏེ། །[^2533]ཅིའི་ཕྱིར་དེ་ལྟར་སྨྲ་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། ཁེ་འཚལ་ཕྱིར་ཞེས་བྱ་བ་ཡིན་ཏེ། སྤོགས༌[^2534]འགྲུབ་པ་དེ་ནི་ཁེ་འདོད་པ་སྟེ། དེ་ནི་ཚོང་པ་རྣམས་ཀྱང་རང་གི་ནོར་འགེད་པར་བྱེད་དེ། ཁེ་འདོད་པའི་ཕྱིར་རོ། །

[Block 3918]
དེ་བས་ལྷན་ཅིག་དེ་ཙམ་ཞེས་བྱ་བ་ནི་ཕྱི་བཞག་ཅན་དུ་སྨྲ་བ་ཙམ་གྱིས་སོ། །

[Block 3919]
ཡང་ན་ཚིག་འཇམ་པོ་ལ་སོགས་པའོ། །

[Block 3920]
དགོས་པ་མཆིས་ཀྱང་ཞེས་བྱ་བ་ནི་དེར་སོང་ཞིང་གནས་པས་ཅི་ཞིག་འགྲུབ་པར་གྱུར་ཀྱང་མི་སྨྲ་ན་ནི།[^2535] དེ་མེད་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། སྐྱོན་དང་བཅས་ཤིང་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3921]
སྐྱོན་དང་བཅས་ཤིང་ཚུལ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་སྐྱོན་དང་བཅས་ཤིང་མི་རིགས་པའོ། །

[Block 3922]
ཟླ་བ་དང་རྒྱུ་སྐར་དང་སྐར་མ་ནི་ཟླ་བ་དང་རྒྱུ་སྐར་དང་སྐར་མ་སྟེ། སྟོན་གྱི་དུས་ལ་བབ་ཅིང་དྲི་མ་མེད་པའི་སྐར་མ་དང་རྒྱུ་སྐར་གྱི་རྒྱན་གང་ལ་ཡོད་པ་ཉིད་དེ་དེ་བས་ནའོ། །

[Block 3923]
ངང་པའི་ཚོགས་མང་པོ་ཞེས་བྱ་བ་ནི་ངང་པའི་ཁྱུ་མང་པོས༌[^2536]མཚོ་དེར་འདོད་པར་བྱ་བའི་གཏམ་བརྗོད་དེ། འདོང་བ་ནི་མཚོ་དེར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 3924]
ཡིད་དུ་འོང་བའི་བཀོད་པ་ཡིན་བས་ཡིད་དུ་འོང་བའི༌[^2537]བཀོད་པའོ། །

[Block 3925]
ཡོན་ཏན་མཉམ་པ་མེད་པ་ནི་ཡོན་ཏན་མཚུངས་པ་མེད་པར་གྱུར་པའོ། །
--- END BLOCKS ---
