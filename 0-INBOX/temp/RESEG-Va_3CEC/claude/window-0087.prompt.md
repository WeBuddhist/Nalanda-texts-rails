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
[Block 3046]
ཡང་དག་འཇོག་ལ་མངོན་པར་དགའ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་བསྒོམ་པ༌[^2655]ལ་མོས་པའོ། །

[Block 3047]
བསམ་གཏན་གྱི་ཡན་ལག་ཡིད་ལ་བྱེད་པ་དང་ཞེས་བྱ་བ་ནི་བསམ་གཏན་ལ་སོགས་པའི་ཡན་ལག་རྟོག་དཔྱོད་དང་བཅས་པ་དང་། རྟོག་དཔྱོད་མེད་པ་ལ་སོགས་པ་བསྒོམ་པ་སྔ་ནས་ཡིད་ལ་བྱེད་ཅིང་རྩོམ་པའོ། །

[Block 3048]
བྱམས་པ་བསྐྱེད་པ༌[^2656]དང་། སྙིང་རྗེ་མངོན་པར་བསྒྲུབ་པ༌[^2657]ཞེས་བྱ་བས་ནི་ཏིང་ངེ་འཛིན་གྱི་རྩ་བར་གྱུར་པ་ཚད་མེད་པ་གཉིས་སྔ་ནས་སྐྱེད་ཅིང་སྒྲུབ་པར༌[^2658]བྱེད་པའོ། །

[Block 3049]
དགའ་བ་ལ་གཞོག་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ཏིང་ངེ་འཛིན་མི་འཁྲུག་པར་བྱེད་པ་དགའ་བ་ཚད་མེད་པ་ལ་སེམས་གཞོག་ཅིང་བཏང་སྙོམས་ཚད་མེད་པ་བསྒོམ༌[^2659]ལ། དེ་གཉིས་ཀྱི་སེམས་དང་རྟག་པར་ལྡན་པར་བྱེད་པའོ། །

[Block 3050 [HEADING]]
##### ཞི་གནས་ཉིད། ^8-8-1-2-0

[Block 3051]
ཞི་གནས་བསྟན༌[^2660]པའི་ཕྱིར། བསམ་གཏན་དང་པོ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། མཐར་གྱིས་སྙོམས་པར་འཇུག་པ་འདི་དག་གི་དོན་ནི༌[^2661]སྔར་བཤད་པར་ཟད་དོ། །

[Block 3052]
ཞི་གནས་ཀྱི་ཚོགས་ནི་ཚད་མེད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ཞི་གནས་བསྒོམ་པའི་རྒྱུའི་ཆོས་ནམ་མཁའ་དང་འདྲ་བར་ཚད་མེད་དེ། ཞི་གནས་ཀྱི་ཚོགས་དེ་དག་ལ་གང་བརྩོན་པ་རྣམས་ཀྱང་ཞི་གནས་ཚད་མེད་པར་སྐྱེ་བར་འགྱུར་བས་ན། ཞི་གནས་མི་ཟད་པ་ཞེས་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 3053 [HEADING]]
#### སྤྲོས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པ། ^8-8-2-0

[Block 3054]
སྤྲོས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི། གང་ལམ་དེ་དག་ཉིད་ན་ལྷག་མཐོང་ལ་རབ་ཏུ་སྦྱོར་བ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^2662]ལྷག་མཐོང་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3055]
གང་ཤེས་རབ་ཀྱི་ཆ་དང་མཐུན་པར་བསྒོམ་པའི༌[^2663]ལམ་ཞེས་བྱ་བ་ལ། ལྷག་མཐོང་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པས། ཤེས་རབ་ཀྱི་ཆ་དང་ཕྱོགས་སུ་གཏོགས་པའི་ཆོས་ལ་གོམས་པར་བྱེད་པ་ཐམས་ཅད་ལྷག་མཐོང་ཞེས་བྱའོ། །

[Block 3056]
ཆོས་རྣམས་ལ་གཡོ་བ་མེད་པར་ཤེས་པ་ནི། ཆོས་ཐམས་ཅད་ལ་བྱེད་པ་པོ་མེད་པར་ཤེས་པ་སྟེ། གོང་དུ་བཤད་པ་རྣམས་ནི་འདིར་མ་བཤད་དོ། །

[Block 3057]
བདེན་པ་རྣམས་ལ་ཤིན་ཏུ་རྟོགས་པར་མཐོང་བའི་ཤེས་པ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་ལམ་གྱི་བདེན་པ་རྣམས་ལ། བདེན་པ་སོ་སོའི་མཚན་ཉིད་གང་ཡིན་པ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་ཤིང་མཐོང་བ་ནི། ཤིན་ཏུ་རྟོགས་པར༌[^2664]མཐོང་བའི་ཤེས་པ་ཞེས་བྱའོ། །

[Block 3058]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བ་ལ། ཆོས་ཐམས་ཅད་རྒྱུ་དང་རྐྱེན་ལས་སྐྱེ་བར་མཐོང་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་མི་འགལ་བར་མཐོང་བའི་ཤེས་པའོ། །

[Block 3059]
ལྟ་བ་ཐམས་ཅད་དང་ཞེས་བྱ་བ་ལ། ཆོས་ཐམས་ཅད་རྟག་པ་དང་། ཆད་པ་དང་། བདག་དང་། སེམས་ཅན་མེད་པར་མཐོང་བ་ནི་ལྟ་བ་ཐམས་ཅད་དང་བྲལ་བར་མཐོང་བའི་ཤེས་པ་ཞེས་བྱའོ། །

[Block 3060]
རྒྱུ་དང་འབྲས་བུ་ཞེས་བྱ་བ་ལ། རྒྱུ་གང་བསྐྲུན་ན་འབྲས་བུ་དེ་བཞིན་དུ་སྐྱེ་བར་འགྱུར་བ་དང་། ལས་གང་བྱས་ན་རྣམ་པར་སྨིན་པ་དེ་བཞིན་དུ་མྱོང་བར་འགྱུར་བ་མཐོང་བ་ནི། རྒྱུ་དང་འབྲས་བུ་དང་རྣམ་པར་སྨིན་པ་ཆུད་མི་ཟ་བར་མཐོང་བའི་ཤེས་པའོ། །

[Block 3061]
འབྲས་བུ་ཐོབ་པ༌[^2665]ཞེས་བྱ་བ་ལ། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའི་འབྲས་བུ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་མངོན་དུ་བྱེད་ཅིང་ཁོང་དུ་ཆུད་དོ་ཞེས་མཐོང་བ་ནི། འབྲས་བུ་ཐོབ་པ༌[^2666]མངོན་སུམ་དུ་བྱ་བ་ལ་རྟོག་པར་མཐོང་བའི་ཤེས་པའོ། །

[Block 3062]
ཡང་དག་པ་ཉིད་ལ་འཇུག་པ་ནི་ཡེ་ཤེས་ཏེ། ཡེ་ཤེས་ཀྱིས་སྟོང་པ་ཉིད་རྟོགས་སོ་ཞེས་མཐོང་བ་ནི། ཡང་དག་པ་ཉིད་ལ་འཇུག་པ་མཐོང་བའི་ཤེས་པ་ཞེས་བྱའོ། །

[Block 3063]
ལྷག་མཐོང་གི་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། ལྷག་མཐོང་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཡང་དག་པར་མཐོང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གང་ཟག་དང་ཆོས་ལ་བདག་མེད་པའི་མཚན་ཉིད་དུ་ཆོས་ཐམས་ཅད་ལ་ཕྱིན་ཅི་མ་ལོག་པར་མཐོང་བ་ནི་ལྷག་མཐོང་ངོ་། །ཆོས་རྣམས་ལ་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ལ། ཀུན་རྫོབ་ཏུ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་དང་། སྨིག༌[^2667]རྒྱུ་ཙམ་དུ་ཇི་ལྟར་སྣང་བ་དེ་བཞིན་དུ་ཡོད་པར་མཐོང་བའོ། །

[Block 3064]
ཆོས་རྣམས་དེ་ཁོ་ན་ཉིད་དུ་མཐོང་ཞེས་བྱ་བ་ནི་ཕུང་པོ་ལ་སོགས་པའི་ཆོས་རྣམས་ནམ་མཁའ་བཞིན་དུ་འགྱུར་བ་མེད་པའི་རང་བཞིན་དུ་མཐོང་བའོ། །

[Block 3065]
ཆོས་རྣམས་གཞན་མ་ཡིན་པ་ཉིད་དུ་མཐོང་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད༌[^2668]འབའ་ཞིག་དེ་ཁོ་ན་ཡིན་གྱི། དེ་ལས་དེ་ཁོ་ན་གཞན་མེད་པར་མཐོང་བའོ། །

[Block 3066]
ཇི་ལྟ་བ་བཞིན་དང་། རྣམ་པར་དག་པ༌[^2669]དང་། དབེན་པར་མཐོང་བ༌[^2670]ཞེས་བྱ་བ་ནི། ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས༌[^2671]འོད་གསལ་བ་ཡིན་པ་དང་། གཟུང་བ་དང་འཛིན་པའི་རྣམ་པས་སྟོང་པ་ཡིན་པར་མཐོང་བའོ། །

[Block 3067]
རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། ལྷག་མཐོང་ཞེས་བྱ་བ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3068]
ཡོད་པའི་རྣམ་པ་ཡང་མི་མཐོང་ཞེས་བྱ་བ་ནི་ཡོད་པའི་རང་བཞིན་དང་ངོ་བོ༌[^2672]ཡང་མི་མཐོང་བའོ། །

[Block 3069]
མེད་པའི་རྣམ་པ༌[^2673]ཡང་མི་མཐོང་ཞེས་བྱ་བ་ནི་མེད་པའི་རང་བཞིན་དང་ངོ་བོར་ཡང་མི་མཐོང་བའོ། །

[Block 3070]
དམིགས་པ་དང་མཚན་མ་ཞེས་བྱ་བ་ལ། གཟུགས་དང་སྒྲ་ལ་སོགས་པའི་དམིགས་པ་དང་། དཀར་པོ་དང་དམར་པོ་ལ་སོགས་པའི་མཚན་མའི་རང་བཞིན་ཡིན་པར་ཡང་མི་མཐོང་བའོ། །

[Block 3071]
དེ་མཐོང་མོད་ཀྱི་ཅི་ཡང་མི་མཐོང་ངོ་ཞེས་བྱ་བ་ནི། ལྷག་མཐོང་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་གོང་དུ་མིང་གིས་སྨོས་པའི་ཆོས་རྣམས་མི་དམིགས་པའི་ཚུལ་དུ་མཐོང་མོད་ཀྱི་དམིགས་པ་དང་། ཡོད་པའི་རྣམ་པ་རྡུལ་ཙམ་ཡང་མི་མཐོང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3072]
གང་གི་ཚེ་མཐོང་བ་མེད་པ་དེའི་ཚེ་མཐོང་སྟེ་ཞེས་བྱ་བ་ནི། དེ་ལྟར་ཅི་ཡང་མི་དམིགས་ཏེ། དོན་དམ་པར་ཅི་ཡང་མ་མཐོང་བ༌[^2674]ནི། ཆོས་ཉིད་མཐོང་ཞིང་རྟོགས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3073]
ལྷག་མཐོང་གིས་ཀྱང་མཐོང་བ་མ་ཡིན། མ་མཐོང་བ་ཡང་མ་ཡིན་པར་མཐོང་ཞེས་བྱ་བ་ནི་ནམ་སྟོང་པར་མཐོང་བའི་དུས་ན་དངོས་པོ་རྡུལ་ཙམ་ཡང་མ་མཐོང་བས་མཐོང་བ་ཡང་མ་ཡིན། དེ་ཁོ་ན་མཐོང་བས་ན་མ་མཐོང་བ་ཡང་མ་ཡིན་པ་འམ། དོན་དམ་པར་དངོས་པོ་གང་ཡང་མ་མཐོང་བས་ན། མཐོང་བ་ཡང་མ་ཡིན་ལ། ཀུན་རྫོབ་ཏུ་བཏགས་པ་ཙམ་དུ་མཐོང་བས་ན།[^2675] མ་མཐོང་བ་ཡང༌[^2676]མ་ཡིན་པའོ། །

[Block 3074]
ཡང་དག་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ཕྱིན་ཅི་མ་ལོག་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3075]
ལྷག་མཐོང་ལ་མཁས་པ་ཐོབ་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པའི་ལྷག་མཐོང་ཐོབ་པར་འགྱུར་རོ། །

[Block 3076]
དེ་ལྟར་མཐོང་ཡང་མངོན་པར་འདུ་མི་བྱེད་པར་མི་ལྟུང་ཞེས་བྱ་བ་ནི། དོན་དམ་པར་གོང་དུ་བཤད་པ་ལྟ་བུར་ཆོས་རྣམས་མི་དམིགས་པར་མཐོང་ཡང་སྟོང་པ་ཉིད་ཀྱི་མཐར་ཡང་མི་ལྟུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3077]
དགེ་བའི་རྩ་བ་མངོན་པར་འདུ་བྱེད་པ་ལས་ཀྱང་མི་ལྡང་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཏུ་ལས་དང་འབྲས་བུ་ཡོད་པར་ལྟ་བས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་མངོན་པར་འདུ་བྱེད་པ་ཡང་མི་གཏོང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3078]
ཞི་གནས་དང་ལྷག་མཐོང་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3079 [HEADING]]
## སོ་སོར་རྟེན་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^9-0

[Block 3080]
སོ་སོར་རྟེན་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2677]ཏིའི་བུ་གཞན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདི་གཉིས་ཀྱི༌[^2678]བསྡུས་པའི་དོན་ལུང་བསྟན་པ་ཐོབ་པར་བསྟན་ཏོ། །

[Block 3081]
གཟུངས་དང་སྤོབས་པ་གཉིས་མི་ཟད་པར་ཡང་གཟུངས་ཀྱིས༌[^2679]དྲན་པར་བྱ་བའི་ཆོས་རྣམས་དང་། སྤོབས་པས༌[^2680]རྟོགས་པར་བྱ་ཞིང་བཤད་པར་བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པས་ན་དྲན་པར་བྱེད་པ་དང་། འཆད་པར་བྱེད་པ་ཡང་མི་ཟད་པའོ། །

[Block 3082]
སོ་སོར་རྟེན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཐོས་པ་མི་བརྗེད་པ་དང་། མ་ཐོས༌[^2681]པ་འདོད་པའོ། །

[Block 3083 [HEADING]]
### ཐོས་པ་མི་བརྗེད་པ། ^9-1-0

[Block 3084]
ཐོས་པ་མི་བརྗེད་པ་གང་ཞེ་ན། གང་གསུངས་པ་སོ་སོར་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་གཟུངས་ནི་མི་བརྗེད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3085]
དེ་ཡང་གང་གིས་མི་བརྗེད་པ་དང་། གང་མི་བརྗེད་པ་དང་། མི་བརྗེད་པ་ཉམས་པ་མེད་པའོ། །
--- END BLOCKS ---
