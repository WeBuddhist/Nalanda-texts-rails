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
སེམས་ཅན་རྣམས་ཀྱི་ལས་ལས་སྐྱེས་པའི་མཐུའི་བྱེ་བྲག་ཅན་གྱིས་རླུང་གི༌[^2348]ས་བོན་ཡིན་ནོ་ཞེས་མ་བཤད་དམ། ཡང་ན་འཇིག་པའི་རླུང་གི་རྩེ་མོ་ནི་དེའི་ཕྱིར༌[^2349]རྒྱུ་ཡིན་པར་འགྱུར་རོ། །

[Block 4097]
ས་སྟོན་པའི་སྡེའི་མདོ་ལས་ནི་རླུང་གིས་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དག་ནས་ས་བོན་དག་ཁྱེར་ཏེ་འོང་ངོ༌[^2350]ཞེས་འབྱུང་ངོ་། །དེ་ལྟར༌[^2351]ཡིན་ཡང་དེ་དག་ས་བོན་ལ་སོགས་པ་ལས་མྱུ་གུ་ལ་སོགས་པ་སྐྱེ་བར་ནི་མི་འདོད་དོ། །

[Block 4098]
འོ་ན་ཇི༌[^2352]ཞེ་ན། རང་གི་ཡན་ལག་དག་ཁོ་ན་ལས་སྐྱེ་བ༌[^2353]ལ། དེ་དག་ཀྱང་རང་གི་ཁོ་ན་དག་ལས་སྐྱེ་སྟེ། རྡུལ་ཕྲ་རབ་དག་ལས་སྐྱེ་བའི༌[^2354]བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་སོ།

[Block 4099]
[^2355] །ད་ནི་མྱུ་གུ་ལ་སོགས་པ་དག་ལས་ས་བོན་ལ་སོགས་པའི་ནུས་པ་ཅི་ཞིག་ཡོད་ཅེ་ན། དེའི་རྡུལ་ཕྲ་རབ་རྣམས་ཕྲད་པ་ལས་མ་གཏོགས་པར་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 4100]
ཡང་ཅིའི་ཕྱིར་དེ་དག་དེ་ལྟར་འདོད་ཅེ་ན། རིགས་མི་མཐུན་པ་ལས་སྐྱེ་བར་ནི་རིགས་པ་མ་ཡིན་ནོ་སྙམ་མོ། །ཅིའི་ཕྱིར་མི་རིགས་ཤེ་ན། ངེས་པ་མེད་པར་འགྱུར་རོ། །

[Block 4101]
ནུས་པ་མེད་པའི་ཕྱིར་དེ་ལྟར་མི་འགྱུར་ཏེ། སྒྲ་དང་ཆོས་བྱེད་ལས༌[^2356]སྐྱེ་བར་འབྱུང་བ༌[^2357]བཞིན་ནོ། །

[Block 4102]
ཡོན་ཏན་གྱི་ཆོས་ནི་སྣ་ཚོགས་ཡིན་གྱི་རྫས༌[^2358]ཀྱི་ཆོས་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། རིགས་མཐུན་པ་དག་ཁོ་ན་ལས་རིགས་མཐུན་པ་རྣམས་འབྱུང་བ་མཐོང་སྟེ། དཔེར་ན་འཇག་མ་དག་ལས་རེ་ལྡེ་དང་། སྐུད་པ་དག་ལས་རས་ཡུག་འབྱུང་བ་བཞིན་ནོ། །

[Block 4103]
འདི་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4104]
འདི་ལ་མི་རིགས་པ་གང་ཞིག་ཡིན་ཞེ་ན། གང་མ་གྲུབ་པ་བསྒྲུབ་པའི་ཕྱིར་དཔེར༌[^2359]བརྗོད་པ་མ་གྲུབ་པ་ཡིན་ནོ། །ཇི་ལྟར༌[^2360]འདི་ལ་ཅི་ཞིག་མ་གྲུབ་ཅེ་ན། འཇག་མ་དག་ལས་རེ་ལྡེ་གཞན་པ་དང་། སྐུད་པ་དག་ལས་རས་ཡུག་གཞན་ཞེས་བྱ་བ་མ་ཡིན་ཏེ། དེ་དག་དང་དེ་དག་ཁོ་ན་དེ་ལྟར་གནས་པ༌[^2361]ལ་དེ་དང་དེའི་མིང་ཐོབ་སྟེ། གྲོག་མའི་ཕྲེང་བ་བཞིན་ནོ། །ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། སྐུད་པ་གཅིག་དང་ལྡན་ན་རས་ཡུག་མི་དམིགས་པའི་ཕྱིར་ཏེ། དེའི་ཚེ་རས་ཡུག་ཡོད་ན་ནི་དམིགས་པར་བྱ་བ་ལ་སུ་ཞིག་བགེགས༌[^2362]བྱེད། ཟད་པར་ཡོད་པ་མ་ཡིན་ན་ནི་དེ་ལ༌[^2363]རས་ཡུག་གི་ཆ་ཡོད་ཀྱི་རས་ཡུག་ནི་མ་ཡིན་པས་འདུས་པ་ཙམ་རས་ཡུག་ཡིན་ནོ། །

[Block 4105]
སྐུད་པ་དག་ལས་གཞན་ལ༌[^2364]རས་ཡུག་གི་ཆ་ཡང་གང་ཞིག་ཡོད། རྟེན་དུ་མ་ཞིག་དང་ལྡན་པ་ལ་ལྟོས་ན་ནི་ཁ་ཚར་མཐོང་བ་ཙམ་དང་ལྡན་ན་རས་ཡུག་དམིགས་པར་འགྱུར་རོ། །

[Block 4106]
ཡང་ན་ནམ་ཡང་མི་དམིགས་པར་འགྱུར་ཏེ། དབུས་དང་ཕ་རོལ་གྱི་ཆ་རྣམས་དབང་པོ་དང་མ་འབྲེལ༌[^2365]པའི་ཕྱིར་རོ། །

[Block 4107]
མིག་དང་རེག་པ་དག་རིམ་གྱིས་ཡན་ལག་རྣམས་དང་ཕྲད་ན་ཡང་ཡན་ལག་ཅན་ནི་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 4108]
དེ་ལྟ་བས་ན་རིམ་གྱིས༌[^2366]ཡན་ལག་ཅན་ཤེས་པའི་ཕྱིར་ཡན་ལག་དག༌[^2367]ཁོ་ན་ལ་དེའི་བློ་སྐྱེ་བར་ཟད་དེ། མགལ་མེའི་འཁོར་ལོ་བཞིན་ནོ། །

[Block 4109]
གཟུགས་དང་རིགས་དང་བྱ་བ་ཐ་དད་པའི་སྐུད་པ་དག་ལས་རས་ཡུག་གི་གཟུགས་ལ་སོགས་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 4110]
གཟུགས་ལ་སོགས་པ་སྣ་ཚོགས་པ་ཡིན་ན་ནི་རིགས་མི་མཐུན་པ་རྩོམ་པར་ཡང་འགྱུར་རོ། །

[Block 4111]
ངོས་ཅིག་ཤོས་མི་བཀྲ་ན་ཡང་རས་ཡུག་མི་མཐོང་བའམ། ཁྲ་བོའི་ངོ་བོར་མཐོང་བར་འགྱུར་རོ། །

[Block 4112]
བྱ་བ་ཡང་སྣ་ཚོགས་པ་ཡིན་པས་ཤིན་ཏུ་སྣ་ཚོགས་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 4113]
མེའི་འོད་ཀྱི་ཚ་བ་དང་། སྣང་བ་དང་པོ་དང་བར་མ་དང་ཐ་མ་དག་ཏུ་ཐ་དད་པས་དེའི་གཟུགས་དང་རེག་བྱ་དག་ཀྱང་མི་འཐད་དོ། །

[Block 4114]
རྡུལ་ཕྲ་རབ་དབང་པོའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཡང་འདུས་པ་དག་ནི་མངོན་སུམ་ཉིད་ཡིན་ཏེ། དཔེར་ན་དེ་དག་གི་འབྲས་བུ་རྩོམ་པ་དང་། མིག་ལ་སོགས་པ་འབྲས་བུ་རྩོམ་པ་དང་། རབ་རིབ་ཅན་རྣམས་ལ་སྐྲ་གྲམ་པའི་ཚོགས་དམིགས་པ་ལྟ་བུ་སྟེ། སྐྲ་ཉག་མ་གཅིག་ནི་རྡུལ་ཕྲ་རབ་བཞིན་དུ་དེ་དག་གི་དབང་པོའི་སྤྱོད་ཡུལ་དུ་མི་འགྱུར་རོ། །

[Block 4115]
གཟུགས་ལ་སོགས་པ་དག་ཁོ་ན་ལ་རྡུལ་ཕྲ་རབ་ཀྱི་མིང་དུ་འདོགས་པའི་ཕྱིར་དེ་ཞིག༌[^2368]ན་རྡུལ་ཕྲ་རབ་ཀྱང་ཞིག་པར་གྲུབ་པ་ཡིན་ནོ། །

[Block 4116]
རྡུལ་ཕྲ་རབ་ནི་རྫས་ཡིན་ལ་རྫས་ཀྱང་གཟུགས་ལ་སོགས་པ་དག་ལས༌[^2369]གཞན་ཡིན་པས་ཞིག་ན་དེ་དག༌[^2370]ཞིག་པར་མ༌[^2371]འགྲུབ་བོ་ཞེ་ན། འདི་གཞན་པ་ཉིད་ཡིན་པར་ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ལྟ་བུར༌[^2372]སུས་ཀྱང་འདི་དག་ནི་ས་དང་ཆུ་དང་མེ་དང་རླུང་དག་ཡིན་ནོ། །

[Block 4117]
འདི་དག་ནི་དེ་དག་གི་གཟུགས་ལ་སོགས་པ་ཡིན་ནོ་ཞེས་ངེས་པར་མི་ཟིན་ལ། མིག་དང་རེག་པའི་གཟུང་བ་དག་ཡིན་པར་ཡང་དམ་བཅའོ། །

[Block 4118]
བལ་དང་རས་བལ་དང་ལེ་བརྒན་རྩི་དང་གུར་གུམ་ཚིག་པ་དག་ལ་དེ་དག་གི་བློ་མེད་པའི་ཕྱིར་གཟུགས་ལ་སོགས་པ་ཁོ་ན་ལ་དེའི་བློ་འཇུག་པར་ཟད་དོ། །

[Block 4119]
ཆོས་བྱེད་ལས་སྐྱེ་བ་བྱུང་བ་ལ་བུམ་པར་ཡོངས་སུ་ཤེས་པ་ནི་དབྱིབས་འདྲ་བའི་ཕྱིར་ཕྲེང་བ་བཞིན་ཏེ། རྟགས་མ་མཐོང་བར་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 4120]
ཡང་ན་བྱིས་པ་བློ་རྡོལ༌[^2373]བ་ལྟ་བུ་དག་ལས་སུ་ཞིག་གུས་པར་འགྱུར་ཏེ། དེ་དག་དགག་པ་ནི་རེ་ཞིག་བཞག་གོ། །

[Block 4121]
ཡང་འཇིག་པ་དེ་དག་གི་རྩེ་མོ་གང་ཡིན་ཞེ་ན།

[Block 4122 [VERSE]]
བསམ་གཏན་གཉིས་སོགས་གསུམ་པོ་ནི། །
དེ་དག་གི་རྩེ་གོ་རིམས་བཞིན། །

[Block 4123]
འཇིག་པའི་རྩེ་མོ་གསུམ་ལ་མེས་འཇིག་པའི་རྩེ་མོ་ནི་བསམ་གཏན་གཉིས་པ་ཡིན་ཏེ། དེ་མན༌[^2374]ཆད་སྲེག་པར་བྱེད་དོ། །

[Block 4124]
ཆུས་འཇིག་པའི་རྩེ་མོ་ནི་བསམ་གཏན་གསུམ་པ་ཡིན་ཏེ། མན་ཆད་སྲུལ་བར་བྱེད་དོ། །

[Block 4125]
རླུང་གིས་འཇིག་པའི་རྩེ་མོ་ནི་བསམ་གཏན་བཞི་པ་ཡིན་ཏེ། མན་ཆད་འཐོར་བར་བྱེད་དོ། །

[Block 4126]
[^2375]འཇིག་པའི་ལྷག་མ་གང་ཡིན་པ་དེ་ནི། རྩེ་མོ་ཞེས་བྱའོ། །

[Block 4127]
ཡང་དེའི་ཕྱིར༌[^2376]བསམ་གཏན་དང་པོ་དང་གཉིས་པ་དང་བསམ་གཏན༌[^2377]

[Block 4128]
གསུམ་པ་དག་མེ་དང་ཆུ་དང་རླུང་དག་གིས་འཇིག་ཅེ་ན། དེ་ཡི་སྐྱོན་དང་ཆོས་མཐུན་ཕྱིར། །བསམ་གཏན་དང་པོ་ན་ནི་རྟོག་པ་དང་དཔྱོད་པ་དག་སྐྱོན་ཡིན་ཏེ། དེ་དག་ཀྱང་ཡིད་ཡོངས་སུ་གདུང་བར་བྱེད་པ་དག་ཡིན་པའི་ཕྱིར་མེའི་བསྐལ་པ་དག་ཡིན་ནོ། །

[Block 4129]
གཉིས་པ་ན༌[^2378]ནི་དགའ་བ་སྐྱོན་ཡིན་ཏེ། དེ་ཡང་ཤིན་ཏུ་སྦྱངས་པ་དང་ལྡན་པས་ལུས་མཉེན༌[^2379]པར་བྱེད་པ་དག༌[^2380]ཡིན་པའི་ཕྱིར་ཆུའི་བསྐལ་པ་ཡིན་ནོ། །

[Block 4130]
དེ་ཉིད་ཀྱི་ཕྱིར་མདོ་ལས།

[Block 4131]
དེ་ནི་ལུས་ཀྱི་མཁྲང་པོ་ཟད་པར་མེད་པའི་ཕྱིར་སྡུག་བསྔལ་གྱི་དབང་པོ་འགགས་སོ་ཞེས་གསུངས་སོ། །

[Block 4132]
བསམ་གཏན་གསུམ་པ་ལ༌[^2381]ནི་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང༌[^2382]བ་དག་སྟེ། དེ་དག་ཀྱང་རླུང་ཁོ་ན་ཡིན་པས་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གང་ན་ནང་གི་སྐྱོན་ཇི་ལྟ་བར་སྐྱེ་བའི་བསམ་གཏན་དེ་ན༌[^2383]ཕྱི་རོལ་གྱི་ཡང་དེ་ལྟ་བུ་ཡིན་ནོ། །ཅིའི་ཕྱིར་སས་འཇིག་པ་མ་ཡིན་ཞེ་ན། སྣོད་ཅེས་བྱ་བ་ནི་ས་ཁོ་ན་ཡིན་ལ་དེ་ནི་མེ་དང་ཆུ་དང་རླུང་དག་དང་མི་མཐུན་གྱི་ས་དང་ནི་མ་ཡིན་ནོ། །

[Block 4133]
བསམ་གཏན་བཞི་པ་ནི་ཇི་ལྟར་མི་འཇིག་ཅེ་ན།

[Block 4134]
བཞི་པ་ན་མེད་མི་གཡོའི་ཕྱིར། །བཅོམ་ལྡན་འདས་ཀྱིས་བསམ་གཏན་བཞི་པ་ནི་ནང་གི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་མི་གཡོ་བ་ཞེས་གསུངས་ཏེ། དེའི་ཕྱིར་དེའི་ཕྱིའི་སྐྱོན་ཡང་མི་འཇུག་པས་དེ་ན༌[^2384]འཇིག་པ་མེད་དོ། །

[Block 4135]
གཞན་དག་ན་རེ་གནས་གཙང་མའི་མཐུས༌[^2385]ཡིན་ཏེ། དེ་དག་གིས་གཟུགས་མེད་པ་དག་ཏུ་འཇུག་པར་ཡང་མི་ནུས་ལ། གཞན་དུ་ཡང་འགྲོ་བར་མི་ནུས་སོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
