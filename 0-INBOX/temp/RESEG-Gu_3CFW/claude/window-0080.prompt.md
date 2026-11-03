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
[Block 2801]
ཕྱིར་བཅོས་པའི་གཞི་ཞུ་བ་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 2802]
ཕྱིར་བཅོས་པའི༌[^2643]གཞི་རྫོགས་སོ།། །།

[Block 2803 [HEADING]]
## དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞི། ^7-0

[Block 2804]
འདི་ལ་དགེ་འདུན་ལྷག་མར༌[^2644]མི་ཤེས་པ་ཉིད་དང་། བཅབ་པའི་སེམས་མ་བཞག་པས་བརྗེད་པ་དང་། བྱས་སམ་མ་བྱས་ཅི་ཞིག་ཇི་ལྟ་བུ་ཞིག་ཅེས་དྲན་པར་མི་ནུས་པ་ཉིད་དང་། བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དང་། གནས་ནས་ཕྱུང་བ་ཉིད་ལ་འཆབ་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་འཆབ་པའི་ཉེས་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2805]
གང་གི༌[^2645]ཕྱིར་ཤེས་ཏེ་སྦས་ན་ནི་འཆབ་པར་འགྱུར་རོ། །

[Block 2806]
བཅབ་པའི་སེམས་མ་བཞག་པས་བརྗོད་པ་ཞེས་བྱ་བ་ནི་སྔར་ཤེས་པའི་དོན་དེ་ཉིད་དགོས་པ་མེད་པར་བརྗོད་པ་སྟེ་མི་ཤེས་པའོ།[^2646] །གང་གིས་བསམ་པའི་སེམས་མ་བཞག་པས་ནི་མངོན་པར་བརྟེན་པའོ། །

[Block 2807]
བསམ་པས་ཞུགས་པས་གཞག་པར་བྱ་བ་དེ་ལ༌[^2647]དེ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2808]
འཆབ་པ་དེ་ལ་མི་སྐྱེད་པ༌[^2648]མ་ཡིན་ནོ། །

[Block 2809]
དེ་བས་ན་མ་བཞག་པ་ལ་སོགས་པའི་བྱེ་བྲག་བྱས་པའོ། །

[Block 2810]
མི་སྣང་བ་མ་བརྗེད་པ་ཡོད་པར་གྱུར་ན་དེ་ལྟར་བཅབ་པའི༌[^2649]སེམས་མ་བཞག་པས་བརྗེད་པ་དེ་ལ་ཡང་འཆབ་པ་མི་འབྱུང་ངོ་། །མི་ནུས་པ་ཉིད་ཅེས་བྱ་བ་ནི་དྲན་པའི་ཕྱིར་བར་དུ་ཆོད་པའི་ཆོས་ཅན་སྐྱོན་དང་བཅས་པ༌[^2650]བརྗེད་ངས་པ་དེ་བརྗོད་པའོ། །

[Block 2811]
ཇི་ལྟ་བུའི་སྐྱོན་དང་བཅས་པ་བརྗེད་ངས་པ་མི་སྐྱེད་པ༌[^2651]དེ་བཞིན་དུ་འཆབ་པ་ལའོ། །

[Block 2812]
བྱས་སམ་མ་བྱས་ཞེས་འཇུག་པར་རྟོགས་པ་ནི་སྐྱོན་དང་བཅས་པར་བརྗོད་པའོ། །

[Block 2813]
ཇི་སྲིད་ཅིག་ཅེས་བྱ་བ་ནི་དབྱར་གནས་པ་ཉིད་ཀྱིས་ཡིད་ལ་ཉེ་བར་གནས་པ་ལའོ། །

[Block 2814]
ཇི་ལྟ་བུ་ཞིག་ཅེས་བྱ་བ་ནི་སྤྱིར༌[^2652]ཡིད་ཀྱི་ངོ་བོ་ཀུན་ནས་སློང་བས༌[^2653]བསམས་བཞིན་དུ་གྱུར་པ་ལ་དེ་བཟློག་པར་བྱ་བའི་དོན་དུའོ། །

[Block 2815]
བསྙེན་པར་རྫོགས་པ་ཉིད་ལྟུང་བ་དང་ལྡན་པ་ལ་འཆབ་པ་མི་འབྱུང་བ་ཉིད་དོ། །

[Block 2816]
ཐ་སྙད་དུ་བྱ་བའི་འདུ་ཤེས་ལས་ཉམས་པ་ཉིད་ལ་ནི་ཕམ་པར་འགྱུར་བ་མན་ཆད་ཀྱི་ལྟུང་བ་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་སྨྱོན་པ་དང་སེམས་འཁྲུགས་པ་ལ་སོགས་པའི་ཐ་སྙད་དུ་རུང་བའི་འདུ་ཤེས་ཉམས་པ་ཉིད་ལ་ཕམ་པར་འགྱུར་བ་མན་ཆད་ཀྱི་ལྟུང་བ་ཡང་མི་འབྱུང་བའོ། །

[Block 2817]
མན་ཆད་ཅེས་སྨོས་པས་ནི་ལྟུང་བ་ཐམས་ཅད་ནི་མི་འབྱུང་བར་བསྟན་ཏོ། །

[Block 2818]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་འཆབ་པ༌[^2654]ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བའི་རྗེས་བསྟན་ཏོ། །

[Block 2819]
འདིར་ཕམ་པར་འགྱུར་བ་མན་ཆད་ཀྱི་ཞེས་བྱ་བ་ལ།[^2655] འདིར་མན་ཆད་ཀྱི་སྒྲས་ནི་མངོན་པར་ཁྱབ་པའི་དོན་དུའོ། །

[Block 2820]
ཕམ་པར་འགྱུར་བ་མན་ཆད་ཀྱི་ལྟུང་བ་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་ཐམས་ཅད་མི་འབྱུང་བར་བསྟན་ཏོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2821]
མ་བཅས་པ༌[^2656]ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཕམ་པར་འགྱུར་བ་མན་ཆད་ཀྱི་ལྟུང་བ་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྙེགས་པའི༌[^2657]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི༌[^2658]སྒྲ་སྨོས་སོ། །

[Block 2822]
འདིར་གཞུང་ནི་ལས་དང་པོ་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2823]
མི་ཤེས་པ་ཉིད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^2659]ནི་འདི་ལྟུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་མི་ཤེས་པ་ཉིད་ལ་ནི་ལྟུང་བ་མི་འབྱུང་བ་མ་ཡིན་ཏེ་འབྱུང་བ་ཁོ་ན་ཡིན་པའོ། །

[Block 2824]
འདིར་གཞུང་ནི་ཚེ་དང་ལྡན་པ་དེ་མི་ཤེས་པས་ནི་མི་གྲོལ་ཏེ། དེ་ལྟུང་བ་གང་བྱུང་བ་དེ་ཆོས་བཞིན་དུ་བྱེད༌[^2660]དུ་གཞུག་གི་སྟེང་དུ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2825]
མངོན་པར་ཡིད་མི་ཆེས་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མི་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2826]
འདོན་པ་དང་བརྗོད་པ་དག་ཐོས་པ་དང་འདི་ལྟུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་མངོན་པར་ཡིད་མི་ཆེས་པ་ཉིད་ལ་ཡང་ལྟུང་བ་འབྱུང་བ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2827]
མངོན་པར་མི་ཤེས་པ་ཉིད་དུ་འདུ་ཤེས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མི་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདོན་པར་བྱེད་པ་དང་བརྗོད་པར༌[^2661]བྱེད་པ་ལ༌[^2662]འདི་བྱིས་པ་ཡིན་པས་ཅུང་ཟད་ཀྱང་སྨྲ་བ་མ་ཡིན་ནོ་ཞེས་དེའི་ཚིག་དག་ལ་མི་གུས་ཤིང་མངོན་པར་མི་ཤེས་པ་ཉིད་དུ་འདུ་ཤེས་པས་ལྟུང་བ་ལ་ཡང་མངོན་པར་ཡིད་མི་ཆེད་པ༌[^2663]ཉིད་ལ་ཡང་ལྟུང་བ་ཁོ་ནར་འགྱུར་ཏེ། དེ་དག་ནི་ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2828]
འདིར་གཞུང་ནི་ཀུན་ཤེས་པར༌[^2664]འདོད་པའི་དགེ་སློང་གིས་ཀྱང་བསླབ་པ་འདི་ལ་བསླབ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2829]
ས་གཞན་ན་གནས་པ་ཉིད་ལ་ནི་སྔ་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྔོ་བ་དང་མགུ་བ་དང་བསྡིགས་པ་དང་སྨད་པ་དང་བསྐྲད་པ་དང་ཕྱིར་འགྱེད་པ་དང་། བསླབ་པ་བྱིན་པས་ས་གཞན་ན༌[^2665]གནས་པ་ཉིད་ལ་ནི་སྔ་མ་ཞེས་བྱ་བ་ལྟུང་བ་འབྱུང་བ་ཁོ་ནར་མ་ཟད་སྔ་མ་འཆབ་པ་ཞེས་བྱ་བ་ཡང་མི་འབྱུང་བ་མ་ཡིན་ཏེ་འབྱུང་བ་ཁོ་ན་ཡིན་པའོ། །

[Block 2830]
དེ་ལ་འཆབ་པ་དང་ལྟུང་བ་གཉིས་ཀ་འབྱུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2831]
འཆབ་པ་ལ་དགེ་འདུན་ལྷག་མ་ཉིད་ལ་ཡིད་གཉིས་ཟ་བ་ནི་ཤེས་པ་པོ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཡིད་གཉིས་ནི་འདུ་ཤེས་དང་འདྲའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འཆབ་པའི་ཡུལ་ལ་དགེ་འདུན་ལྷག་མ་ལ་ཡིད་གཉིས་ཟ་བཞིན་དུ་བཅབས་ན་དགེ་འདུན་ལྷག་མ་ཤེས་བཞིན་དུ་བཅབས་པ་དང་འདྲ་སྟེ་བཅབས་པའི་ཉེས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2832]
ས་གང་ལ་འཆབ་པ་མི་འབྱུང་བ་དེ་ལ་སྤྱད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ༌[^2666]རྫོགས་པ་དང་གནས་ནས་ཕྱུང་བ་དང་ཐ་སྙད་དུ་རུང་བའི་འདུ་ཤེས་ཉམས་པ་ཞེས་སྨོས་པ་དེ་དག་ནི་འདིར་ས་ཞེས་བྱ་བའི་སྒྲར་བརྗོད་དོ། །

[Block 2833]
དེ་དག་ཇི་ལྟར་འཆབ་པ་འབྱུང་བའི་ཞིང་མ་ཡིན་པ་དེ་བཞིན་དུ་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་སྤྱད་པའི་ཞིང་མ་ཡིན་པའོ། །

[Block 2834]
དེ་བཞིན་དུ་མ་བཅབས་པ་ལ་ཡང་ཇི་ལྟར་འདིར་འཆབ་པ་མི་འབྱུང་བ་དེ་ལྟར་གནས་ནས་སྤོ་བ་ལ་སོགས་པ་སྤྱོད་པ་ལ་ཡང་དེ་ལྟ་བས་ན་འདི་བསྟན་པའོ། །

[Block 2835]
མ་གུས་པས་སྤྱོད་པ་གཏོང་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བ་སྤྱོད་པ་མ་གུས་པས་གཏོང་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2836]
འཐབ་ཀྲོལ་བྱེད་པ༌[^2667]འོང་བས་འཇིགས་པས་གཏོང་བ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 2837]
དེ་ལ༌[^2668]དེའི་སྡེ་པ་ལྷག་པར་སྤྱོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་སྤོ་མགུ༌[^2669]བྱེད་པ་དེ་ལའོ། །

[Block 2838]
དེའི་སྡེ་པ་ཞེས་བྱ་བ་གང་གི་སྡེ་ཚན་སྤྱོད་པ་དེ་ནི་དེའི་སྡེ་པའོ། །

[Block 2839]
ཡོངས་སུ་གནས་པ་དང་མགུ་བ་སྤྱོད་པའི་གནས་སྐབས་དེ་ལ་དེའི་སྡེ་པ་ཞེས་བྱ་བ་དགེ་འདུན་ལྷག་མའི་སྡེ་ཚན་དུ་གཏོགས་པའི་དངོས་གཞི་འམ་ཉེས་པ་སྦོམ་པོའམ་ཉེས་བྱས་ལྷག་པར་སྤྱོད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2840]
ཡོད་ལ་ཕྱིར་མི་འཆོས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལེན་པར་བྱེད་པ་ཡོད་པ་ལ་སོགས་པས་ཕྱིར་བཅོས་པའི་ཐབས་ཡོད་པ་ལ་སྤོ་བ༌[^2670]དང་ལྟུང་བ་ཕྱིར་མི་འཆོས་ན་སྐྱ་རེངས་རེར༌[^2671]ཞིང་ཉེས་བྱས་རེ་རེར་འགྱུར་བའོ། །
--- END BLOCKS ---
