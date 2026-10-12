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
[Block 4306]
དེས༌[^2637]ནི་རིའི་རྩེ་མོ་རྣམ་པ་ཉི་ཤུ་ལས་བྱུང་བའི་འཇིག་ཚོགས་ཀྱི་ལྟ་བ་བཀག་གོ། །

[Block 4307]
གང་གིས་འཁོར་བའི་འཁོར་ལོ་མ་ལུས་པ་འདི་ཉིད་མཚན་དུ་འཁྲུལ་འཁོར་གྱི་རིགས་པས་འཁོར་བ་ཞེས་བདག་ཏུ་སྨྲ་བའི་ཕྱོགས་བཀག་པའོ། །

[Block 4308]
དབང་ཕྱུག་དང་ཐམས་ཅད་བྱེད་པ་དང་ཐམས་ཅད་འཇིག་པར་བྱེད་པ་ནུས་པ་གསུམ་གྱིས་སྤྲུལ་པའི་བདག་ཉིད་ཆེ་བ་རྟག༌[^2638]པ་ཡིན་ནོ་ཞེས་འགལ་བ༌[^2639]སྟེ་གང་གི་ཕྱིར་གལ་ཏེ༌[^2640]ཐམས་ཅད་བྱེད་ཅིང་འཇིག་པར་བྱེད་པ་ན་དེའི་ཚེ་ཅིག་ཅར་དུ་བྱེད་པའམ་འཇིག་པ་ཅིའི་ཕྱིར་མི་བྱེད། དེ་མི་བྱེད་པས་རིམ་གྱིས་བྱེད་པ་མ༌[^2641]ཡིན་ཏེ། དེ་ཉིད་མི་རྟག་པ་ཉིད་དོ། །

[Block 4309]
གང་གི་ཕྱིར་གང་གི༌[^2642]དུས་སུ་བྱེད་ན་དེའི་ཚེ་དེ་ལ་ནུས་པ་ཡོད་དེ། [^2643]དུས་གཞན་དུ་དེ་མེད་དོ་ཞེས་ལྟོས་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 4310]
ལྟོས་པ་དང་བཅས་པའི་ནུས་པ་མེད་པ་སྟེ། ལྷན་ཅིག་བྱེད་པ་ལ་ལྟོས་པའི་ཕྱིར་ཏེ། བུམ་པ་བཞིན་ནོ། །

[Block 4311]
དེ་བས་ན་དབང་ཕྱུག་མེད་དོ། །

[Block 4312 [VERSE]]
སྒྲུབ་དང་བྱེད་པ་ངེས་པ་རང་བཞིན་དང་། །
དུས་དང་གཟའ་དང་དབང་ཕྱུག་ལྷ་ཉིད་དང་། །
རྒལ་བ་བསོད་ནམས་གཤིན་རྗེ་མཐར་བྱེད་ནི། །
མངོན་དུ་བྱས་པའི་མིང་གི་རྣམ་གྲངས་ཡིན། །

[Block 4313]
ཞེས་ལ་ལ་འདོད་དོ། །

[Block 4314]
དེ་ལ་སྒྲུབ་པ་ཞེས་པས་དངོས་པོ་འདི་དག་སྐྱེད་པར་བྱེད་པ་དང་། འཇིག་པར་བྱེད་པ་སྟེ། དེ་ཉིད་གཅིག་པུ་འགྲོ་བའི་རྒྱུ་ཡིན་ཞེ་ན། དེ་ཡང་མི་རིགས་ཏེ། རང་གི་ལས་ཀྱི་བག་ཆགས་ཀྱིས་སྤྲུལ་པའི་ཁམས་གསུམ་པ་ལ་སྤྲུལ་པ་གཞན་ནི་མེད་དེ་དེ་ཉིད་སྔར་བཀག་པའི་ཕྱིར་རོ། །

[Block 4315 [VERSE]]
ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས། །
དགེ་དང་མི་དགེ་རང་གིས་བྱས། །
འཇིག་རྟེན་པ་ཡིས་དེ་འབྲས་སྤྱོད། །
བྱེད་པ་གཞན་ནི་ཁ་ཅིག་མེད། །

[Block 4316]
ཅེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4317]
བྱེད་པ་པོ་ཞེས་བྱ་བ་རྣམ་པར་དཔྱད་ན་མེད་དེ། ཉོན་མོངས་པ་དང་ལས་དང་སྐྱེ་བའི་རྒྱུན་གྱི་ཕུང་པོ་རྣམས་འཁོར་བ་ཉིད་ཁམས་གསུམ་ཞེས་བཤད་དོ། །

[Block 4318]
ཁུར་བུ་ཁུར་བ་ལྟར་ཁ་ཅིག་གང་ཟག་ཡོད་དེ། གང་གིས་ཕུང་པོ་འདི་རྣམས་སྤངས་ཏེ། ཕུང་པོ་གཞན་ལེན་པའོ། །

[Block 4319]
འདིར་གང་ཟག་ནི་ལས་དང་ཉོན་མོངས་པའི་བག་ཆགས་དང་ལྡན་པའི་རྣམ་པར་ཤེས་པ་ཉིད་དོ། །

[Block 4320]
དེ་ཉིད་ཁམས་གསུམ་གྱི༌[^2644]ངོ་བོར་ཡོངས་སུ་འཁོར་བར་འགྱུར་ཏེ། དེ་བས་ན་བྱེད་པ་པོ་གཞན་མེད་དོ། །

[Block 4321]
ངེས་པ་ཞེས་བྱ་བ་ནི་འཆི་བདག་ཅེས་བརྗོད་དེ། [^2645]དེ་ཉིད་ཀྱིས་འགྲོ་བ་བསྐྱེད་ཅིང་འཇིག་པར་བྱེད་དོ་ཞེ་ན། དེ་ཡང་མ་ཡིན་ཏེ། གལ་ཏེ་འཆི་བདག་ཡིན་ན་དེའི་ཚེ་འཇིག་པའི་ནུས་པ་དང་ལྡན་པ་ཡིན་གྱི། སྐྱེ་བའི་ནུས་པ་དང་ལྡན་པར་མི་འགྱུར་རོ། །

[Block 4322]
སྐྱེ་བའི་ནུས་པ་དང་ལྡན་ན་འཆི་བདག་མ་ཡིན་ནོ། །

[Block 4323]
དེ་བས་ན་ངེས་པའི་སྨྲ་བ་འདི་ནི་བརྟགས་པ༌[^2646]པ་ཡིན་ནོ། །

[Block 4324]
རྣམ་པར་ཤེས་པ་དང་དབང་པོ་དང་ཚེ་འགག་པར་འགྱུར་ན། ཤིའོ་ཞེས་བརྗོད་པས་འཆི་བདག་མེད་དོ། །

[Block 4325]
རང་བཞིན་གྱིས་སྨྲ་བའི་ཕྱོགས་སུ་དངོས་པོ་རྣམ་པ༌[^2647]སྣ་ཚོགས་པར་སྐྱེ་བར་མི་འགྱུར་གྱི་ཐམས་ཅད་རང་བཞིན་གཅིག་པར་འགྱུར་རོ། །

[Block 4326]
སྣ་ཚོགས་པ་ཉིད་རང་བཞིན་ཡིན་ཞེ་ན། སྨྲས་པ། དེ་ལྟར་ཡིན་ན་ཅིག་ཅར་དུ་སྐྱེ་བ་དང་འཇིག་པར་ཇི་ལྟར་མི་འགྱུར། དེ་བས་ན་རང་བཞིན་གྱིས་སྨྲ་བའི་ཕྱོགས་ནི་མི་རིགས་སོ། །

[Block 4327]
དུས་སྨྲ་བ་རྣམས་ན་རེ། དུས་ཀྱི་འབྱུང་བ་སྨིན་པར་འགྱུར། །ཞེས་ཟེར་ན། དེ་ཡང་མི་རིགས་ཏེ། གང་གི་ཕྱིར་དུས་དེ་ནི་འདས་པ་དང་མ་འོངས་པའི་དབྱེ་བས་གསུམ་དུ་འགྱུར་ཏེ། འདས་པ་ནི་ཞིག་པའི་ཕྱིར་སྨིན་པར་བྱེད་པའི་ནུས་པ་མེད་དོ། །

[Block 4328]
མ་འོངས་པས་ཀྱང་སྨིན་པའི་ནུས་པ་ཡོད་པ་མ་ཡིན་ཏེ་མ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4329]
ད་ལྟར་བྱུང་བ་ལ་ཡང་ནུས་པ་མེད་དེ་སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4330]
དེ་བས་ན་སྐྱེ་བའམ་འཇིག་པའི་ནུས་པ་མེད་དོ། །

[Block 4331]
གཞན་ཡང་ཉིན་མོ་ལ་སོགས་པའི་མཚན་ཉིད་ཉི་མ་ལ་སོགས་པས་བྱས་པ་ཟླ་བ་ལ་སོགས་པའི་དུས་ཡིན་ནོ་ཞེས་མི་རིགས་ཏེ། རེ་ཞིག་ཟླ་བ་ལ་སོགས་པ་ཉིད་ནི་ཡོད་པ་མ་ཡིན་ཏེ། སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4332]
དེ་རྣམས་ཀྱིས་བྱས་པར་གྱུར་པའི་དུས་ཀྱིས་ཀྱང་འབྱུང་བ་སྐྱེ་བ་ལ་སོགས་པའི་ནུས་པ་ཇི་ལྟར་ཡིན་ཞེས་དུས་ཀྱི་སྨྲ་བའི་ཕྱོགས་མེད་དོ། །

[Block 4333]
ཉི་མ་ལ་སོགས་པ་གཟའ་རྣམས་ཀྱིས་ཀྱང་ཁྱིམ་དང་རྒྱུ་སྐར་ལ་རྒྱུ་བའི་དབང་གིས་འགྲོ་བ་སྐྱེད་པ༌[^2648]དང་འཇིག་པར་བྱེད་དོ་ཞེ་ན། དེ་ཡང་མི་རིགས་ཏེ། གཟའ་རྣམས་ནི་ཤར་བ་དང་། ནུབ་པའི་དབང་གིས་མི་རྟག་པ་ཡིན་ནོ། །

[Block 4334]
གང་ཞིག་རང་ཡོད་པ་མ་ཡིན་པ་དེས་ནི་གཞན་བསྐྱེད་པའི་ནུས་པ་ཇི་ལྟར་ཡོད། སྨིན་དྲུག་ལ་སོགས་པ་གཟུང་བའི་ཆའི་སྦྱོར་བས་དེ་རྣམས་ལ་དགོས་པ་མེད་དོ། །

[Block 4335]
རང་ཉིད་ཀྱིས་ཇི་ལྟར་མི་བྱེད་དེ། ལྟོས་པ་དང་བཅས་པའི་ཕྱིར་དེ་རྣམས་ཀྱང་མི་རྟག་པ་ཞེས་བྱའོ། །

[Block 4336]
སྔར་བཤད་པའི་རིགས་པས་དབང་ཕྱུག་བཀག་པས་དེའི་བྱེད་པ་ཉིད་དང་རྟག་པ་ཉིད༌[^2649]ཀྱང་མི་རིགས་སོ། །

[Block 4337]
ལྷས་ཐམས་ཅད་བྱེད་དོ་ཞེས་ཟེར་ན་བདེ་བའི་རང་བཞིན་ཐམས་ཅད་ཅི་སྟེ་མི་བྱེད་སྡུག་བསྔལ་གྱི་རང་བཞིན་བྱེད་པ་དགོས་པ་མེད་དོ།[^2650] །

[Block 4338]
དེ་ཡང་སྤང་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4339]
དེ་བས་ན།

[Block 4340 [VERSE]]
འདོད་དང་མི་འདོད་འབྲས་བུ་ཅན། །
ལས་རྣམས་ཀྱིས་ནི་ཡོངས་སྨིན་པ། །
རྣམ་པར་ཤེས་པ་སྟོང་པ་འདི། །
དེ་དེ་རྣམ་པ་དོན་ལ་འཇུག །

[Block 4341]
ཅེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ། ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེ། །[^2651]ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4342 [VERSE]]
ང་རྒྱལ་ལས་ནི་རབ་སྐྱེས་པ། །
བདག་གི་བྱེད་པས་འཕེལ་འགྱུར་ཏེ། །
འགྲོ་ལ༌[^2652]ཕན་པ་ངེས༌[^2653]སྨྲས་པས། །
སྐྱེ་དགུ་མ་ལུས་འདི་དག་གསུངས།[^2654] །

[Block 4343]
ཞེས་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་བསྟན་ཏོ། །

[Block 4344]
དེ་བས་ལྷ་གཞན་མེད་དོ། །

[Block 4345]
དེ་བཞིན་དུ་སྐལ་བ༌[^2655]ཞེས་བྱ་བ་ནི་གང་གི༌[^2656]དབང་གིས་འཇིག་རྟེན་པ་བདེ་བ་དང་ལྡན་པར་འགྱུར་བ་དང་དེ་མེད་པས་སྡུག་བསྔལ་དང་ལྡན་པར་འགྱུར་རོ། །
--- END BLOCKS ---
