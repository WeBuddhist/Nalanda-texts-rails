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
[Block 3116]
དེ་ལྟར་སྤོབས་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟ་བུར་ན་སྤོབས་པ་མཐར་ཕྱིན་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3117]
གཟུགས་སུ་སྣང་བ་ཇི་སྙེད་པ་ཞེས་བྱ་བ་ནི་གཟུགས་སུ་སྣང་བའི་ཆོས་ཇི་སྙེད་པ་རྣམས་མི་རྟག་པ༌[^2700]ལ་སོགས་པར་སུན་འབྱིན་པ་དང་། ཆོས་དེ་དག་གི༌[^2701]མཚན་ཉིད་ཚིགས་སུ་བཅད་དེ་སྦྱར་ཏེ་བསྟན་པར་ནུས་པའི་ཤེས་རབ་ཀྱང་དེ་སྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3118]
དེ་བཞིན་དུ་སྒྲ་ལ་ཡང་སྦྱར་རོ། །

[Block 3119]
དེ་དང་དེར་ཞེས་བྱ་བ་ནི་འཁོར་དེ་དང་དེ་དག་ཏུའོ། །

[Block 3120]
དེའི་ལྷུན་གྱིས་གྲུབ་པ༌[^2702]ཉིད་དུ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་དེའི་སྤོབས་པ་རྩོལ་བ་དང་འབད་པ་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3121]
དད་པ་ནི་དེ་དག་ཇི་ལྟར་འདོད་པའོ། །

[Block 3122]
དབང་པོ་རྣམས་ནི་དབང་པོ་རྣོན་པོ་དང་། འབྲིང་དང་། ཐ་མ་རྣམས་སོ། །

[Block 3123]
ཆོས་སྤོབས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་དད་པ་དང་། དབང་པོ་དང་མཐུན་མཐུན་དུ༌[^2703]ཆོས་སྟོན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3124]
དེ་འདོད་ན་ཚེ་གཞན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི།[^2704] སྤོབས་པ་མི་ཟད་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་གལ་ཏེ་བདག་ཉིད་འདོད་ན་ཚེ་དུ་མ་དང་། བསྐལ་པ་དུ་མ་འདས་ཀྱི་བར་དུ་ཡང་འདུག་པའི་སྤྱོད་ལམ་ལས་མི་ལྡང་ཞིང་བསམ་མི་དགོས་པར་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3125]
དེའི་ཆོས་བསྟན་པ་དེས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེའི་སྤོབས་པས་ཆོས་བསྟན་པ་དེས་ཀྱང་སེམས་ཅན་རྣམས་སྡུག་བསྔལ་ཡང་དག་པར་ཟད་པར་བྱ་བའི་ཕྱིར། ངེས་པར་འབྱུང་བར་འགྱུར་ཏེ་དེ་བཞིན་དུ་སྡུག་བསྔལ་ཡང་དག་པར་ཟད་པར་བྱེད་ནུས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3126]
གཟུངས་དང་སྤོབས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3127 [HEADING]]
## སྟོན་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^10-0

[Block 3128]
སྟོན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་འདུ་བྱེད་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་དང་། ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་དང་། ཞི་པའི་ང་རྒྱལ་མེད་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། བཙུན་པ་ཤ་ར་དྭ༌[^2705]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^2706]ཆོས་ཀྱི་མདོ་བཞི་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་གི་བསྡུས་པའི་དོན་དེ་ཐོབ་པ་རྣམ་པར་གཞག་པ༌[^2707]བསྟན་ཏོ། །

[Block 3129]
ཆོས་ཀྱི་མདོ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་རྣམས་མི་རྟག་པ་ལ་སོགས་པ་འདི་བཞི་མདོར༌[^2708]བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། ཆོས་ཀྱི་མདོ་ཞེས་བྱའོ། །

[Block 3130]
མི་ཟད་པ་ནི་དེས་བསྡུ་བར་བྱ་བའི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཟད་མི་ཤེས་པས་ན་མི་ཟད་པ་ཞེས་བྱའོ། །

[Block 3131]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། བཞི་གང་ཞེ་ན་འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། མི་ཟད་པའི་ཤེས་བ་རབ་ཏུ་འཇུག་པའོ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་བསྟན་པའི་ཚུལ་ལོ། །

[Block 3132]
དེ་མན་ཆད་ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 3133]
འདུ་བྱེད༌[^2709]ཐམས་ཅད་མི་རྟག་པར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་བསྟན་པ་མི་ཟད་པའི་ཤེས་པ་རབ་ཏུ་འཇུག་པ་ཞེས་བྱ་བ་ནི། འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་པའོ་ཞེས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་བསྟན་པའི་ཤེས་པ་འབྱུང་བ་སྟེ། མི་ཟད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3134]
དེ་མི་ཟད་པ་ཡང་འདུ་བྱེད་ཀྱི་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར། དེ་བསྟན་པའམ་ཤེས་པ་ཡང་མི་ཟད་པ་སྟེ། དེ་བཞིན་དུ་སྡུག་བསྔལ་ལ་སོགས་པ་འོག་མ་རྣམས་ལ་ཡང་སྦྱར་རོ། །

[Block 3135 [HEADING]]
### འདུ་བྱེད་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ། ^10-1-0

[Block 3136]
འདུ་བྱེད་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་བསྟན་པའི་དབང་དུ་བྱས་ནས་དེ་ལ་མི་རྟག་པའི་དོན་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3137]
མི་རྟག་པའི་དོན་ཡང་རྣམ་པ༌[^2710]གཉིས་ཏེ། མེད་པའི་དོན་དང་། འཇིག་པའི་དོན་ཏོ། །

[Block 3138]
འདིར་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་ཡིན་པར་དགོངས་པས། མེད་པའི་དོན་ལ་མི་རྟག་པའི་དོན་དུ་དགོངས་ཀྱི༌[^2711]འཇིག་པའི་དོན་དུ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་མེད་པའི་དོན་དང་མི་ཆགས་པའི་དོན་ཏེ།[^2712] དངོས་པོ་རྣམ་པར་འཇིག་པའི་དོན་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3139]
དེ་ལ་མེད་པའི་དོན་ནི། དོན་དམ་པར་གཟུང་བ་དང་འཛིན་པ་ཀུན་བརྟགས༌[^2713]ཀྱི་ཆོས་གང་ཡང་རྟག་ཏུ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་མེད་པ་སྟེ། དེ་ནི་མི་རྟག་པའི་དོན་ཏོ། །

[Block 3140]
མི་ཆགས་པའི་དོན་ནི་བདག་དང་བདག་གི་ཞེས་བྱ་བ་ལ་སོགས་པ་ཆགས་པར་འགྱུར་བའི༌[^2714]དངོས་པོ་གང་ཡང་མེད་པའི་ཕྱིར༌[^2715]མི་ཆགས་པ་སྟེ། དེ་ནི་མི་རྟག་པའི་དོན་ཏོ། །

[Block 3141]
དེ་བས་ན་དངོས་པོ་འཇིག་པའི་དོན་ནི་མ་ཡིན་ནོ་ཞེས་དངོས་སུ་གསུངས་ཏེ། འཇིག་རྟེན་པའི་མི་རྟག་པར༌[^2716]གྲགས་པ་དང་། དངོས་པོ་ཡོད་པ་ལས་ཞིག་སྟེ་མེད་པར་འགྱུར་བ༌[^2717]ལས་མི་རྟག་ཅེས་བྱ་བ་མ་ཡིན་གྱི་ཡེ་ནས་རང་བཞིན་གྱིས་རྟག་པ༌[^2718]མེད་པ་ལ་མི་རྟག་པ་ཞེས་བྱའོ། །

[Block 3142]
དོན་དེ་ཉིད་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར་མི་རྟག་པའི་དོན་ནི་ཆོས་ལ་བདག་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཕུང་པོ་དང་ཁམས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་ངོ་བོ་མེད་པ་ཉིད་མི་རྟག་པའི་དོན་ཏེ༌[^2719]ཆོས་ལ་བདག་མེད་པ་དེ་རྟག་ཏུ་གཟུང་བ༌[^2720]དང་འཛིན་པའི་ངོ་བོ་ཉིད་ཀྱིས་དབེན་པའི་ཕྱིར་སྟོང་པ་དེ་ལ་འཇིག་པ་གང་ཡང་མེད་དེ་གང་འཇིག་པ་མེད་ཅིང་རྟག་ཏུ་སྟོང་པ་དེ་ནི་མི་རྟག་པའི་དོན་ཏོ། །

[Block 3143 [HEADING]]
### ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ། ^10-2-0

[Block 3144]
ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་བསྟན་པའི་དབང་དུ་བྱས་ནས་དེ་ལ་སྡུག་བསྔལ་གྱི་དོན་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3145]
སྡུག་བསྔལ་གྱི་དོན་ཀྱང་རྣམ་པ་ལྔ་སྟེ་དགའ་བ་ལས་བཟློག༌[^2721]པའི་དོན་དང་དགའ་བ་དང་བྲལ་བའི་དོན་དང་། དགའ་བའི་ཡུལ་མ་ཡིན་པའི་དོན་དང་། སྒྲ་ཙམ་དུ་ཟད་པའི་དོན་དང་། རང་བཞིན་གྱིས༌[^2722]སྟོང་པའི་དོན་ཏོ། །

[Block 3146 [HEADING]]
#### དགའ་བ་ལས་བཟློག་པའི་དོན། ^10-2-1-0

[Block 3147]
དེ་ལ་དགའ་བ་མེད་པའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ་ཞེས་བྱ་བས་དགའ་བ་ལས་བཟློག་པའི་དོན་རྣམ་པར་བསྟན་ཏེ། སྡུག་བསྔལ་ནི་དགའ་བ་ལས་བཟློག་པ་སྟེ་གང་དགའ་བའམ་ཆགས་པར་འགྱུར་བའི་དངོས་པོ་མེད་ཅིང་དེ་ལས་བཟློག་པའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ། །

[Block 3148 [HEADING]]
#### དགའ་བ་དང་བྲལ་བའི་དོན། ^10-2-2-0

[Block 3149]
དགའ་བ་ཟད་པའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ་ཞེས་བྱ་བས་དགའ་བ་དང་བྲལ་བའི་དོན་བསྟན་ཏེ། དགའ་བའི་ཡུལ་དང་བྲལ་བ་ནི༌[^2723]སྡུག་བསྔལ་སྐྱེ་བས༌[^2724]དགའ་བ་དང་ཆགས་པ་རྣམས་དང་བྲལ་བའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ། །

[Block 3150 [HEADING]]
#### དགའ་བའི་ཡུལ་མ་ཡིན་པའི་དོན། ^10-2-3-0

[Block 3151]
སྨོན་པ་མེད་པའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ་ཞེས་བྱ་བ་དགའ་བའི་ཡུལ་མ་ཡིན་པའི་དོན་བསྟན་ཏེ། ཟག་པ་དང་བཅས་པའི་ཆོས་ཐམས་ཅད་ནི་སྡུག་བསྔལ་རྣམ་པ་སྣ་ཚོགས་སྐྱེ་བའི་རྒྱུ་དང་གཞི་ཡིན་པས་དེ་ལ་སྨོན་ཅིང་དགའ་བར་བྱ་བའི་ཡུལ་མ་ཡིན་ཏེ་དེ་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ། །

[Block 3152 [HEADING]]
#### སྒྲ་ཙམ་དུ་ཟད་པའི་དོན། ^10-2-4-0

[Block 3153]
སྡུག་བསྔལ་གྱི་སྒྲ་རབ་ཏུ་བསྟན་པ༌[^2725]ཞེས་བྱ་བས་སྒྲ་ཙམ་དུ་ཟད་པའི་དོན་བསྟན༌[^2726]ཏེ། སྡུག་བསྔལ་ཞེའོ་ཞེས་བྱ་བའི་སྒྲས་བརྗོད་པ་ཉིད་སྡུག་བསྔལ་དུ་ཟད་ཀྱི་སྡུག་བསྔལ་གྱི་དངོས་པོ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3154 [HEADING]]
#### རང་བཞིན་གྱིས་སྟོང་པའི་དོན། ^10-2-5-0

[Block 3155]
ནམ་མཁའ་རབ་ཏུ་བརྗོད་པའི་དོན་ནི་ཞེས་བྱ་བས་རང་བཞིན་གྱིས་སྟོང་པའི༌[^2727]དོན་བསྟན་ཏེ། གང་སྟོང་པ་དེ་ཉིད་སྡུག་བསྔལ་བ་སྟེ། ནམ་མཁའ་བཞིན་དུ་སྟོང་པར་བརྗོད་པའི་དོན་ཉིད་སྡུག་བསྔལ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
