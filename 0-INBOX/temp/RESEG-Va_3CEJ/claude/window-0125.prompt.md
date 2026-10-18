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
[Block 4376]
ད་ནི་ཅི་རབ་ཏུ་འཇུག་པར་བྱེད་པ༌[^2637]ཇི་ལྟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱང་དེ་དང་འདྲ་འམ། འོན་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་དུ༌[^2638]ཡིན། དེ་ལས་ཅིར་འགྱུར། གལ་ཏེ་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་ཡིན༌[^2639]ནོ་ཞེ་ན་ནི་འཇིག་ཚོགས་དང་། མཐར་འཛིན་པར་ལྟ་བས་རབ་ཏུ་འཇུག་པའི་ཕྱིར་འདི་ནི་ཡང་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར་རིག་བྱེད་ཡོད་པར་འགྱུར་རོ། །

[Block 4377]
ཡང་ན་མཐོང་བས་སྤང་བར་བྱ་བ་ཐམས་ཅད་ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་ཁྱད་པར་དུ༌[^2640]བརྗོད་དགོས་སོ། །

[Block 4378]
གལ་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་ནོ་ཞེ་ན་ནི་སེམས་མི་དགེ་བ་ལུང་དུ་མ་བསྟན་པ་ཅན་གྱི་སོ་སོར་ཐར་པའི་རྣམ་པར་རིག་བྱེད་དགེ་བར་མི་འགྱུར་རོ། །

[Block 4379]
རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱང་དེ་དང་འདྲ་མོད་ཀྱི་བསྒོམ་པས་སྤང་བར་བྱ་བས་བར་དུ་གཅོད་པའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ཇི་ལྟ་བ་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 4380]
གལ་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པའི་དབང་གིས་དགེ་བ་ལ་སོགས་པ་ཉིད་མ་ཡིན་ན། འོ་ན་ནི་མདོ་ལས་རྒྱུའི་ཀུན་ནས་སློང་བ་ལས་དགོངས་ཏེ་གསུངས་ཀྱི་དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་ལས་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་འདི་ནི་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར་རིག་བྱེད་མེད་དོ་ཞེས་བྱ་བ་འདི་བརྗོད་པར་མི་བྱའི་འདི་སྐད་དུ་གཞན་གྱིས་ཆོད་པའི་རྒྱུའི་ཀུན་ནས་སློང་བ་ལས་དགོངས་ནས་གསུངས་སོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4381]
ཞར་ལ་འོངས་པ་རྫོགས་སོ།། །།

[Block 4382 [HEADING]]
##### སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་དེ་དག་ལས་གཞན་པ། ^4-2-2-2-0

[Block 4383]
སྔར་བཤད་པའི། རྣམ་རིག་མིན། དེ་ནི་རྣམ་གསུམ་ཞེས་བྱ། སྡོམ་དང་སྡོམ་པ་མིན་དང་གཞན། །སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་དེ་དག་ལས་གཞན་པ་སྡོམ་པ་ཡང་མ་ཡིན། སྡོམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་སྟེ། འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུ༌[^2641]སྡོམ་ཞིང་འགོགས་པས༌[^2642]ན་སྡོམ་པའོ། །

[Block 4384]
དེ་ལ།

[Block 4385 [HEADING]]
###### སྡོམ་པ། ^4-2-2-2-1-0

[Block 4386 [VERSE]]
སྡོམ་པ་སོ་སོར་ཐར་ཞེས་བྱ། །
དེ་བཞིན་ཟག་མེད་བསམ་གཏན་སྐྱེས། །

[Block 4387]
སྡོམ་པ་རྣམ་པ་གསུམ་སྟེ། སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་འདི་པ་རྣམས་ཀྱི་འདོད་པ་ན་སྤྱོད་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 4388]
བསམ་གཏན་གྱི་སྡོམ་པ་ནི་གཟུགས་ན་སྤྱོད་པ་རྣམས་ཀྱི་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 4389 [HEADING]]
###### **སོ་སོར་ཐར་པའི་སྡོམ་པ།** ^4-2-2-2-1-1-0

[Block 4390]
ཟག་པ་མེད་པའི་སྡོམ་པ་ནི་ཟག་པ་མེད་པའི་ཚུལ་ཁྲིམས་ཡིན་ནོ།[^2643] །དེ་ལ། སོ་སོར་ཐར་ཞེས་བྱ་རྣམ་བརྒྱད། །དགེ་སློང་གི་སྡོམ་པ་དང་། དགེ་སློང་མའི་སྡོམ་པ་དང་།[^2644] དགེ་ཚུལ་གྱི་སྡོམ་པ་དང་། དགེ་ཚུལ་མའི་སྡོམ་པ་དང་། དགེ་བསྙེན་གྱི་སྡོམ་པ་དང་། དགེ་བསྙེན་མའི་སྡོམ་པ་དང་། བསྙེན་གནས་པའི་སྡོམ་པ་སྟེ།[^2645] སྡོམ་པ་རྣམ་པ་དེ་བརྒྱད་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཞེས་བྱ་སྟེ། མིང་དུ་ནི་རྣམ་པ་དེ་བརྒྱད་ཡིན་ནོ། །

[Block 4391]
རྫས་སུ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 4392]
དགེ་སློང་གི་སྡོམ་པ་དང་། དགེ་ཚུལ་གྱི་སྡོམ་པ་དང་། དགེ་བསྙེན་གྱི་སྡོམ་པ་དང་། བསྙེན་གནས་ཀྱི་སྡོམ་པའོ། །

[Block 4393]
དེ་ལྟར་ན་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་མཚན་ཉིད་སོ་སོར་ངེས་པའི་ཕྱིར་རྫས་ཉིད་དུ་རྣམ་པ་དེ་བཞིན་ཡིན་ཏེ། དགེ་སློང་གི་སྡོམ་པ་ལས་ནི་དགེ་སློང་མའི་སྡོམ་པ་གཞན་མ་ཡིན་ནོ། །

[Block 4394]
དགེ་ཚུལ་གྱི་སྡོམ་པ་ལས་ཀྱང་དགེ་སློང་མ་དང་། དགེ་ཚུལ་མའི་སྡོམ་པ་གཞན་མ་ཡིན་ནོ། །

[Block 4395]
དགེ་བསྙེན་གྱི་སྡོམ་པ་ལས་ཀྱང་དགེ་བསྙེན་མའི་སྡོམ་པ་གཞན་མ་ཡིན་ནོ། །ཇི་ལྟར་ཤེས་ཤེ་ན། མཚན་ལས་མིང་ནི་འཕོ་བའི་ཕྱིར། །མཚན་ཞེས་བྱ་བ་ནི་རྟགས་ཞེས་བྱ་བ་སྟེ། གང་གིས་སྐྱེས་པ་དང་བུད་མེད་དག་ཏུ་མཚོན་པར་བྱེད་པའོ། །

[Block 4396]
མཚན་ལས་ནི་དགེ་སློང་དང་དགེ་སློང་མ་ལ་སོགས་པའི་མིང་འཕོ་བར་འགྱུར་ཏེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན། མཚན་གྱུར་ན་དགེ་སློང་ནི་དགེ་སློང་མ་ཞེས་བྱ། དགེ་སློང་མ་ཡང་དགེ་སློང་ཞེས་བྱའོ། །

[Block 4397]
དགེ་ཚུལ་ནི་དགེ་ཚུལ་མ་ཞེས་བྱ་ལ་དགེ་ཚུལ་མ་དང་དགེ་སློང་མ་ཡང་དགེ་ཚུལ་ཞེས་བྱའོ། །

[Block 4398]
དགེ་བསྙེན་ནི་དགེ་བསྙེན་མ་ཞེས་བྱ་ལ་དགེ་བསྙེན་མ་ཡང་དགེ་བསྙེན་ཞེས་བྱ་སྟེ། མཚན་གྱུར་པ་ལས་སྔོན་གྱི་སྡོམ་པ་གཏོང་བའི་རྒྱུ་ཡང་ཡོད་པ་མ་ཡིན་ལ་སྔོན་མེད་པའི་སྡོམ་པ་འཐོབ་པའི་རྒྱུ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4399]
དེ་ལྟ་བས་ན་སྡོམ་པ་བཞི་པོ་དེ་དག་ནི་གསུམ་པོ་ལས་རང་བཞིན་ཐ་མི་དད་དོ། །

[Block 4400]
གང་གི༌[^2646]དགེ་བསྙེན་གྱི་སྡོམ་པ་ལས་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་ལ། དེ་ལས་ཡང་དགེ་སློང་གི་སྡོམ་པ་ཡང་དག་པར་བླངས་ན། ཅི་སྤོང་བའི་འཕེལ་བ་དང་ལྡན་པའི་ཕྱིར་སྡོམ་པ་དེ་དག་ལྔ་དང་བཅུ་དང་ཉི་ཤུ་ཞེས་བྱ་བ་ལྟ་བུ་དང་། དོང་ཙེ་གཅིག་དང་གཉིས་ཞེས་བྱ་བ་བཞིན་དུ་གཞན་དང་གཞན་ཞེས་བྱ་བ་འམ། འོན་ཏེ་དེ་དག་ཐམས་ཅད་ཐ་དད་པ་ཉིད་གཅིག་ཏུ་སྐྱེ་ཞེ་ན། སྨྲས་པ། ཐ་དད། དེ་དག་ནི་མ་འདྲེས་པ་ཉིད་དེ། སྡོམ་པ་གསུམ་དག་ལ་སྲོག་གཅོད་པ་སྤོང་བ་གསུམ་ནས་མྱོས་པར་འགྱུར་བའི་བཏུང་བ་སྤོང་བ་གསུམ་གྱི་བར་དུ་མཚན་ཉིད་ཐ་དད་པར་སྐྱེ་སྟེ། ལྷག་མ་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 4401]
དེ་དག་ལ༌[^2647]ཁྱད་པར་ཅི་ཞིག་ཡོད་ཅེ་ན། གཞིའི་ཁྱད་པར་ལས་ཁྱད་པར་ཡོད་དོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། ཇི་ལྟ་ཇི་ལྟར་བསླབ་པའི་གཞི་ཆེས་མང་པོ་དག་ཡང་དག་པར་ལེན་པར་འདོད་པ་དེ་ལྟ་དེ་ལྟར་རྒྱགས་པ་དང་བག་མེད་པའི་གནས་ཆེས་མང་པོ་དག་ལས་ལྡོག་པ་ན་སྲོག་གཅོད་པ་ལ་སོགས་པའི་གཞི་ཆེས་མང་པོ་དག་ལས་ལྡོག་པར་འགྱུར་ཞིང་སྤོང་བའི༌[^2648]གཞི་རྣམས་ལ་ཡང་འཇུག་པར་འགྱུར་བས་གཞིའི་ཁྱད་པར་ལས་སྤོང་བ་རྣམས་ཁྱད་པར་ཡོད་དོ། །

[Block 4402]
དེ་ལྟ་མ་ཡིན་ན༌[^2649]གཉི་ག་ཡང་དེར་འདུས་པའི་ཕྱིར་དགེ་སློང་གི་སྡོམ་པ་བཏང་བས་སྡོམ་པ་གསུམ་ཆར་ཡང་བཏང་བར་འགྱུར་བ་ཞིག་ན་དེ་ནི་མི་འདོད་དོ། །

[Block 4403]
དེ་ལྟ་བས་ན་སྡོམ་པ་དེ་དག་ནི་ཐ་དད་པ་ཁོ་ནའོ། །

[Block 4404]
དེ་དག་འགལ་བ་མེད། དེ་གསུམ་ཆར་ཡང་ལྷན་ཅིག་པར་འགྱུར་གྱི། སྡོམ་པ་ཕྱི་མ་ཡང་དག་པར་བླངས་པས་སྔ་མ་གཏོང་བ་ནི་མ་ཡིན་ཏེ། དེ་ལྟ་མ་ཡིན་ན་དགེ་སློང་གི་སྡོམ་པ་ཡོངས་སུ་བཏང་བས་དགེ་བསྙེན་ཡང་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་དུ་འོང་ངོ་། །འདི་ཇི་ལྟར་ན་དགེ་བསྙེན་ཡིན། ཇི་ལྟར་ན་བསྙེན་གནས་པ་ནས་དགེ་སློང་གི་བར་དུ་ཡིན་ཞེ་ན།

[Block 4405 [VERSE]]
སྤང་བྱ་ལྔ་བརྒྱད་བཅུ་དང་ནི། །
ཐམས་ཅད་སྤོང་བ་མནོས་པ་ལས། །
དགེ་བསྙེན་དང་ནི་བསྙེན་གནས་དང་། །
དགེ་ཚུལ་ཆེད་དང་དགེ་སློང་ཉིད། །

[Block 4406]
གྲངས་བཞིན་དུ་བསྟན་པར་རིག་པར་བྱ་སྟེ། སྤང་བར་བྱ་བ་ལྔ་པོ་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་དང་། འདོད་པས་ལོག་པར་གཡེམ་པ་དང་། བརྫུན་དུ་སྨྲ་བ་དང་། འབྲུའི་ཆང་དང་སྦྱར་བའི་ཆང་མྱོས་པར་འགྱུར་བའི་བཏུང་བ་སྤོང་བ་ཡང་དག་པར་བླངས་པས་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་གནས་པ་ཡིན་ནོ། །

[Block 4407]
བརྒྱད་པོ་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་དང་། མི་ཚངས་པར་སྤྱོད་པ་དང་། བརྫུན་དུ་སྨྲ་བ་དང་། མྱོས་པར་འགྱུར་བའི་བཏུང་བ་དག་དང་། སྤོས་དང་། མེ་ཏོག་ཕྲེང་དང་། བྱུག་པ་དང་། གར་དང་། གླུ་དང་། རོལ་མོ་དང་། ཁྲི་སྟན་མཐོན་པོ་དང་། ཁྲི་སྟན་ཆེན་པོ་དང་། དུས་མ་ཡིན་པའི་ཟས་སྤོང་བ་ཡང་དག་པར་བླངས་པས་ནི་བསྙེན་གནས་ལ་གནས་པ་ཡིན་ནོ། །

[Block 4408]
དེ་དག་ཉིད་དང་གསེར་དང་དངུལ་འཛིན་པ་དང་བཅུ་སྤོང་བ་ཡང་དག་པར་བླངས་པས་ནི་དགེ་ཚུལ་ཡིན་ཏེ། འདི་གར་དང་། གླུ་དང་རོལ་མོ་དང་། སྤོས་དང་། མེ་ཏོག་ཕྲེང་དང་། བྱུག་པ་གཉིས་སུ་བྱས་ནས་བཅུར་འགྱུར་རོ། །

[Block 4409]
ལུས་དང་ངག་གི་ལས་སྤང་བར་བྱ་བ་ཐམས་ཅད་སྤོང༌[^2650]བ་ཡང་དག་པར་བླངས་པས་ནི་དགེ་སློང་ཡིན་ནོ། །

[Block 4410]
སོ་སོར་ཐར་པའི་སྡོམ་པ་དེ་ནི།

[Block 4411 [VERSE]]
ཚུལ་ཁྲིམས་དང་ནི་ལེགས་སྤྱད་དང་། །
ལས་དང་སྡོམ་པ་ཞེས་བྱའོ། །

[Block 4412]
ལས་མི་མཉམ་པ་ཅན་རྣམས་ཡང་དག་པར་འཇོག་པར་བྱེད་པས་ན༌[^2651]ཚུལ་ཁྲིམས་སོ། །

[Block 4413]
ངེས་པའི་ཚིག་ཏུ་ན་བསིལ་བའི་ཕྱིར་ཏེ།

[Block 4414]
ཚིགས་སུ་བཅད་པ་ལས།

[Block 4415 [VERSE]]
ལུས་ལས་ཡོངས་སུ་གདུང་མེད་པས། །
ཚུལ་ཁྲིམས་ཡང་དག་བླངས་པ་བདེ། །
--- END BLOCKS ---
