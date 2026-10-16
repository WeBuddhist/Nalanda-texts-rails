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
[Block 4096]
ཡོན་ཏན་ལ་དགའ་བ་ཉིད་བསྟན་པའི་ཕྱིར། འབངས་ལ་ཕན་ཕྱིར་ཞེས་བྱ་བའི༌[^2642]ཚིགས་བཅད་ཡིན་ཏེ། ཁྱོད་ལྟ་ལགས་ཀྱང་མོད་ཅེས་བྱ་བ་ནི་མགྲོན་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 4097]
རང་བཞིན་དུལ་བ་ཞེས་བྱ་བ་ནི་ངང་གིས་སེམས་སྦྱངས་པ་གང་ཡིན་པ་དེ་ནི་རང་བཞིན་དུལ་བ་སྟེ། མི་བཟོད་པ་སྤངས་པས་རང་བཞིན་དུལ་བར་གྱུར་པའོ། །

[Block 4098]
གལ་ཏེ་མི་བཟོད་པ་སྤངས་སོ་ཞེས་བསྟན་ན་ཅིའི་ཕྱིར་སའི་བདག་པོ་བྱེད་པར་འགྱུར་ཞེ་ན། སྨྲས་པ། འབངས་ལ་ཕན་ཕྱིར་རྒྱལ་པོའི་ཚུལ་འཛིན་པ། །ཞེས་བྱ་བ༌[^2643]སྨོས་ཏེ། འདིས་ནི་བདག་ཉིད་ཀྱི་ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕྱིར་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 4099]
རང་གི་ངང་གིས་ཞེས་བྱ་བ་ནི་འབད་པ་མེད་པར་གོམས་པ་སྟེ། དེ་ལ་ཡོན་ཏན་རྣམས་གནས་པར་སྟོན་ཏོ། །

[Block 4100]
དེ་བས་ཞེས་བྱ་བ་ནི་རྒྱུན་མི་འཆད་པའི་ཚུལ་གྱིས་ཡིན་ཏེ་དེས་ནི་བདག་ཉིད་ཀྱི་ཚུལ་བསྟན་ཏོ། །

[Block 4101]
ཡོན་ཏན་བསྟོད་པར་འོས་པ་ཞེས་བྱ་བ་ལ། འོས་པ་ནི་རིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4102]
[^2644]བདེ་བའི་རྒྱུ་ཡོན་ཏན་དང་ཕན་ཡོན་རྣམ་པ་གཉིས་བསྟན་ཏེ། །འཇིག་རྟེན་འདིར་བསྟོད་པའི༌[^2645]འོས་སུ་གྱུར་པ་དང་། འཇིག་རྟེན་ཕ་རོལ་དུ་བདེ་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4103]
བསྟོད་པར་འོས་པ་ཞེས་བྱ་བ་དང་། འབྱུང་པོ་ཉེས་པའི་གཅོང་རོང་མི་འདོང་ངོ་། །ཞེས་བྱ་བས་ནི་འདི་གཉིས་མེད་པར་སྟོན་ཏོ། །

[Block 4104]
[^2646]འཇིག་རྟེན་འདིར་གྲགས་པ་མ་ཡིན་པ་དང་། ཕ་རོལ་དུ་ཡང་ངན་སོང་དུ་འགྲོ་བའི་སྡུག་བསྔལ་མེད་པ་ཡིན་ཏེ། ཡོན་ཏན་གྱི་ཆོས་ཀྱི་ཕན་ཡོན་རྣམ་པ་གཉིས་བསྟན་ནས་སྐྱོན་གྱི་ཆོས་ཉིད་ནི་དེའི་མི་མཐུན་ཕྱོགས་ཉེས་དམིགས་ཉིད་དུ་བསྟན་ཏེ། དེ་ཡང་།

[Block 4105 [VERSE]]
སེམས་ཡོད་སུ༌[^2647]ཞིག་མི་ཕན་ལམ་ངན་འགྲོ། །
ཞེས་བྱ་བ་ནི་ཉེས་པའི་ལམ་ཡིན་ཏེ།
འབྱུང་པོ༌[^2648]ཉེས་པའི་གཅོང་རོང་མི་འདོང་ངོ་། །

[Block 4106]
ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་པ་ཡིན་ནོ། །

[Block 4107]
ཅིའི་ཕྱིར་འབྱུང་པོའི༌[^2649]གཅོང་རོང་དུ་མི་འདོང་ཞེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། དཔའ་བས་ཡུལ་འཁོར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་ཡིན་ནོ། །

[Block 4108]
ཡུལ་ཞེས་བྱ་བ་ནི་གནས་ཞེས་བྱ་བའི་དོན་ཏེ་ཡུལ་དེར་དཔའ་བས་སོ། །

[Block 4109]
ནོར་གྱི་རྩོལ་ཕོད་པ་ཡིན་པས་ནོར་གྱི་རྩོལ་ཕོད་པ་སྟེ། ནོར་གྱི་མཐུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4110]
འདིས་ནི་བདག་པོའི་ནུས་པ་བསྟན་ཏེ། ནོར་དང་། བཀའ་ཁྲིམས་དང་། སྟོབས་ནི་བདག་པོའི་ནུས་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4111]
ཡང་ན་ནོར་དང་། རྩོལ་ཕོད་པ་ནི་ནོར་རྩོལ་ཕོད་པའོ།[^2650] །རྩོལ་ཕོད་པ་སྨོས་པས་ནི་བཀའ་ཁྲིམས་གཟུང་ངོ་། །ཐབས༌[^2651]ཀྱིས་དེ་མི་འཐོབ་ཅེས་བྱ་བ་ནི་ངེས་པ་མེད་པའོ། །

[Block 4112]
ནོར་བཀོད་པ་དང་འབད་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཡོངས་སུ་ངལ་བ་དང་། ནོར་ཟད་པ་གཉིས་ཏེ། འདིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་བསྟན་ཏེ། །[^2652]རྒྱལ་པོའི་སྲིད་ཐོབ་ཅེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་ཡོན་ཏན་ཉིད་ཀྱིས༌[^2653]ཐོབ་པ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 4113]
ལྷའི་རྒྱལ་པོའི༌[^2654]དཔལ་ཡང་ཞེས་བྱ་བ་ནི་མི་ལས་ཁྱད་པར་དུ་གྱུར་པའི་རྒྱལ་སྲིད་འཐོབ་པའི་དབང་དུ་བྱས་པ་སྟེ། འདི་ཡང་ཕན་ཡོན་ཉིད་དེ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུའོ། །

[Block 4114]
ཡོན་ཏན་ཡོད་ན་རྒྱུད་ཀྱང་རབ་ཏུ་འཕེལ། །ཞེས་བྱ་བ་ཡིན་ཏེ། གཞན་རག་ལུས་པ་ནི་ཕན་ཡོན་ཏེ་ལུས་ཀྱི༌[^2655]འདུད་པའོ། །

[Block 4115]
གྲགས་པ་རྣམས་ཀྱང་ཡོན་ཏན་ཉིད་ལས་འཕྲོ་བ༌[^2656]ཞེས་བྱ་བ་འདིས་ནི་གྲགས་པ་འཕེལ་བ་སྟེ།

[Block 4116 [VERSE]]
གཞན་རག་ལུས་པའི་ཕན་ཡོན་ཡིན་ནོ། །
ཟླ་བའི་འོད་ལས་གསལ་བའི་ཡོན་ཏན་ནི། །

[Block 4117]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་གཞན་ཕ་དང་མ་དང་འབྲེལ་པ་ཉིད་དང་བར་བྱེད་པའི་རྒྱུ་ཡིན་ཏེ།[^2657] ཡིད་ཀྱི་ལས་ཀྱི་དབང་དུ་བྱས་ནས་མི་བཟོད་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་མི་བཟོད་པའོ། །

[Block 4118]
དྲེགས་པ་ཞེས་བྱ་བ་ནི་སྐྱེས་བུའི་སྟོབས་ལ་སོགས་པས་བསྙེམས༌[^2658]པའོ། །

[Block 4119]
མི་བཟོད་པ་དང་དྲེགས་པ་ནི་མི་བཟོད་དྲེགས་པའོ། །

[Block 4120]
དེ་གཉིས་ཀྱི་སྡང་བ་ནི་རྩུབ་པ་སྟེ་མི་བཟོད་དྲེགས་པས་སྡང་བའོ། །

[Block 4121]
འདི་དག་གིས་ནི་སེམས་ལ་ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4122]
ཁྲོ་བའི་མཚན་ཉིད་ནི་གནོད་པར་བྱས་པ་དང་། བརྙས་པ་ལས༌[^2659]སེམས་ཀུན་ནས་མནར་སེམས་པ་ཡིན་ནོ། །

[Block 4123]
འཁོན་རྙིང༌[^2660]གང་ཡིན་པ་དེ་ནི་འཁོན་རྙིང༌[^2661]ཡོད་པ་སྟེ། འཁོན་རྙིང༌[^2662]ཡོད་པ་དེ་གང་ཡིན་པ་དེས་ཕྲག་དོག་ཆེ་བའོ། །

[Block 4124]
འཁོན་རྙིང༌[^2663]ཡོད་པ་དང་ཕྲག་དོག་ཆེ་བ་ནི་འཁོན་རྙིང༌[^2664]ཡོད་ཅིང་ཕྲག་དོག་ཆེ་བའོ། །

[Block 4125]
འདིས་ནི་འཁོན༌[^2665]དུ་འཛིན་པ་བསྟན་ཏེ་འཁོན༌[^2666]དང་རྗེས་སུ་འབྲེལ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4126]
དགྲ་ནི་རྣམ་པ་གཉིས་ཏེ། ལྷན་ཅིག་སྐྱེས་པ་དང་། ཀུན་དུ་བརྟགས་པའོ། །

[Block 4127]
དགྲ་བོ་མི་བཟད་ཅེས་བྱ་བ་འདི་ནི་ཀུན་ཏུ་བརྟགས་པའི༌[^2667]དབང་དུ་བྱས་པའོ། །

[Block 4128]
འཁོན་རྙིང༌[^2668]ཡོད་ཅེས་བྱ་བ་འདི་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 4129]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་དེ་བས་ན༌[^2669]འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པའི་ཕྱིར་རམ། ཡང་ན་བསྟོད་པར་འོས་པའི་ཕྱིར་དང་། བདེ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4130]
ཡོན་ཏན་གྱིས་རྒྱལ་ཕྲན་གྱི༌[^2670]དྲེགས་པ་བཏུལ་བའི་ཕྱིར་ཕ་རོལ་གྱི་ཚོགས་སྦྱོང་བ་ཡིན་ཏེ། དུལ་བ་ལ་སོགས་པའི་ཡོན་ཏན་གྱི་ཚོགས་ཡོངས་སུ་སྦྱོང་བའོ། །

[Block 4131]
དུལ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། སོགས་པ་སྨོས་པས་ནི་ཚུལ་ཁྲིམས་དང་། སྦྱིན་པ་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཏེ་བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་གཟུང༌[^2671]ངོ་། །ཡོན་ཏན་བཟང་ཞིང་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་ལམ་ལ་རྗེས་སུ་དགའ་བ་སྟེ། དེའི་ཡོན་ཏན་ལ་རྗེས་སུ་དགའ་བར་འབངས་ཀྱང་བསླབས༌[^2672]པའོ། །

[Block 4132]
དེས་ན་རྒྱལ་པོ་ཅི་ཞིག་ཏུ་འགྱུར་ཞེ་ན། དེའི་ཕན་ཡོན་འབངས་ལ་ཕན་གདགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4133]
འབངས་ལ་ཕན་གདགས་པ་ནི་རྒྱལ་པོའི་དོན་གྱི་མཆོག་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཚེ་རབས་གཉི་གའི་བདེ་བའི་ཕྱིར་རོ། །

[Block 4134]
འཇིག་རྟེན་འདིར་ནི་གྲགས་པ་ལ་སོགས་པ་འཐོབ་པར་འགྱུར་རོ། །

[Block 4135]
འཇིག་རྟེན་ཕ་རོལ་དུ་ནི་བདེ་འགྲོར༌[^2673]འགྲོ་བས་ཕན་པའོ། །
--- END BLOCKS ---
