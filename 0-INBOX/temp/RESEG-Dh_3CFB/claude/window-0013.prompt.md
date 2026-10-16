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
[Block 456]
དེ་བས་ན་ངེས་པ་དང་མ་ངེས་པའི་དབང་གིས་མངོན་སུམ་གྱིས་འཛིན་པ་དང་མི་འཛིན་པ་དག་མ་ཡིན་ནོ། །

[Block 457]
ངེས་པ་རྣམས་ཀྱིས་ནི་དེ་ལྟར་མ་ཡིན་ཏེ། འགའ་ཞིག་ངེས་ཀྱང་གཞན་ལ་མ་ངེས་པས་འཇུག་པ༌[^315]ཐ་དད་པས་འཛིན་པ་དང་མི་འཛིན་པ་ཡིན་ནོ། །

[Block 458]
དེའི་ཕྱིར་ངེས་པ་གང་ཡིན་པ་དེ་ཉིད་འདི་འཛིན་པ་ཡིན་ནོ། །

[Block 459]
དེ་ལྟ་མ་ཡིན་ན་རྣམ་པ་གཅིག་ལ་ཡང་དེར་མི་འགྱུར་རོ། །

[Block 460]
ཡང་ཅིའི་ཕྱིར་ཐམས་ཅད་པས༌[^316]ཐ་དད་པའི་དངོས་པོའི་ངོ་བོ་ལ་ཉམས་སུ་མྱོང་བ་སྐྱེས་ཀྱང་དེ་ཁོ་ན་བཞིན་དུ་དྲན་པའི་ངེས་པ་མི་འབྱུང་ཞེ་ན། ལྷན་ཅིག་བྱེད་པ་མ་ཚང་བའི་ཕྱིར་རོ། །

[Block 461]
དེ་བས་ན། །ཁྱད་པར་ཆ་ཤས་རྣམ་སྤངས་པ། །མངོན་སུམ་གྱིས་ནི་གཟུང་བའམ།[^317] །

[Block 462 [VERSE]]
ཁྱད་པར་གང་ལ་རྟོགས་པ་ཡི། །
རྐྱེན་ཡོད་དེ་ནི་རྟོགས་པར་འགྱུར། །

[Block 463]
ཐམས་ཅད་ལས་ཐ་དད་པ་ཆ་ཤས་དང་བྲལ་བའི་ངོ་བོ་ཉིད་ཉམས་སུ་མྱོང་མོད་ཀྱི་འོན་ཀྱང་དེ་ཙམ་གྱིས་ཁྱད་པར་ཐམས་ཅད་ལ་ངེས་པར་མི་འགྱུར་ཏེ། རྒྱུ་གཞན་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 464]
ཉམས་སུ་མྱོང་བའི་རྣམ་པར་རྟོག་པ་ལ་ཇི་ལྟར་གོམས་པ་བཞིན་ངེས་པའི་ཤེས་པ་སྐྱེད་པར་བྱེད་དོ།[^318] །དཔེར་ན་གཟུགས་མཐོང་བ་ལ་ཁྱད་པར་མེད་ཀྱང་། རོ་མྱང་བ༌[^319]དང་། ཉལ་པོ་བྱ་བ་དང་། བཟའ་བར་བྱ་བའི་རྣམ་པར་རྟོག་པ་དག་ལྟ་བུའོ། །

[Block 465]
དེ་ལ་ནི་བློ་གསལ་བ་དང་། འདི་བག་ཆགས་གོམས་པ་དང་། སྐབས་ཤེས་བྱ་བ་ལ་སོགས་པ་ཡང་ཉམས་སུ་མྱོང་བ་ལས་ཁྱད་པར་ངེས་པ་སྐྱེ་བའི་ལྷན་ཅིག་བྱེད་པ་དག་ཡིན་ནོ། །

[Block 466]
དེ་དག་ཁོ་ན་ཤིན་ཏུ་ཉེ༌[^320]བ་དང་། ཆེས་ཤིན་ཏུ་ཉེ་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་སྔ་ཕྱི་ཉིད་དུ་འགྱུར་ཏེ། དཔེར་ན་སྐྱེད་པར་བྱེད་པ་དང་། འདོན་དུ་འཇུག་པར་བྱེད་པ་ཉིད་དུ་ཁྱད་པར་མེད་ཀྱང་ཕ་འོང་བ་མཐོང་ནས་བདག་གི༌[^321]ཕ་འོང་ངོ་སྙམ་གྱི་མཁན་པོ་འོང་ངོ་སྙམ་པ་ནི་མ་ཡིན་པ་ལྟ་བུའོ། །

[Block 467]
ངེས་པ་དེར་ཡང་འགྱུར་བ་ན་འཁྲུལ་པའི་རྒྱུ་མེད་ན་མི༌[^322]འགྱུར་རོ། །

[Block 468]
དེའི་ཕྱིར་ཉམས་སུ་མྱོང་བ་ཁོ་ནས་ནི་རྣམ་པ་ཐམས་ཅད་ཅེས༌[^323]པ་མ་ཡིན་ནོ། །

[Block 469 [VERSE]]
དེ་ལའང་གཞན་ལས་ལྡོག་པ་དང་། །
གཞན་ལས་ལོག་པ༌[^324]ཞེས་བྱ་ཡི། །
སྒྲ་དང་ངེས་པ་ཉིད་དག༌[^325]ནི། །
བརྡ་ཡི་རྗེས་སུ་བྱེད་པ་ཡིན།

[Block 470]
[^326] །གཞན་སེལ་བ་དེ་ལ་ཡང་ལྡོག་པ་ཡང་གཞན་ལོག་པ་ཡང་རྒྱུ༌[^327]གཞན་པ་ཉིད༌[^328]མེད་དེ། དེ་ལས་ལྡོག་པ་ལས་ལོག་པ་ལ༌[^329]དེ་ཡོད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 471]
དེ་ལྟ་ཡིན་ན་ནི་ལྡོག་པ་ཡང་མེད་དོ། །

[Block 472]
དེའི་ཕྱིར་ལྡོག་པ་གང་ཡིན་པ་དེ་ཉིད་ལོག་པ་ཡིན་ནོ། །

[Block 473]
སྒྲ་དང་རྟོགས་པའི༌[^330]ཐ་དད་པ་ནི་བརྡའི་བྱེ་བྲག་གིས་ཡིན་གྱི། བརྗོད་པར་བྱ་བ་ལ་ནི་ཐ་དད་པ་མེད་དོ། །

[Block 474]
བརྗོད་པར་བྱ་བ་ཐ་དད་པ་མེད་པའི་ཕྱིར་བརྡའི་བྱེ་བྲག་ཀྱང་མི་རུང་སྟེ། གཉི་གས་གཅིག་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 475]
དེ་ལྟར་ན་ཐ་དད་པར་འབྱེད་པའི་རྣམ་པ༌[^331]དབྱེ་བ་ཡང་མི་སྦྱར་བར་འགྱུར་ཏེ། དེ་ནི་ཐ་དད་པ་ལ་བརྟེན་པའི་ཕྱིར་རོ་ཞེ་ན།

[Block 476 [VERSE]]
གཉི་གས་གཅིག་ཅིག་བརྗོད་མོད་ཀྱི། །
བརྗོད་བྱའི་ཤན་གྱི་ཁྱད་པར་གྱིས། །
རྣམ་དབྱེ་ཐ་དད་འབྱེད་པ་ཡིས། །
ཐ་དད་དོན་བཞིན་སྒྲུབ་པར་བྱེད། །

[Block 477]
སྒྲ་རྣམས་ཀྱི་འཇུག་པ་ཡུལ་གྱི་རང་གི་ངོ་བོ་ལ་རག་ལས་པ་ནི་འགའ་ཡང་མེད་དེ། འདོད་པས་འཇུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 478]
དེ་དག་ཐ་དད་པའམ་ཐ་དད་པ་མ་ཡིན་པ་ལ་ཇི་ལྟར་སྦྱར་བར་འདོད་པ་དེ་ལྟར་སྦྱར་བ་ནི་དོན་དེ་གེགས་བྱེད་པ༌[^332]མེད་པར་རབ་ཏུ་སྟོན་པར་བྱེད་དོ། །

[Block 479]
དེའི་ཕྱིར་བ་ལང་དང་བ་ལང་ཉིད་ཅེས་བྱ་བས་དོན་གཅིག་བརྗོད་མོད་ཀྱི། ཁྱད་པར་འགའ་ཞིག་ཤེས་པར་བྱ་བའི་ཕྱིར། བརྡས་ཁྱད་པར་བྱས་ན་དོན་གཞན་མ་ཡིན་ཀྱང་ཐ་དད་པའི་དོན་ཅན་གྱི་རྣམ་པར་དབྱེ་བས་དོན་ཐ་དད་པ་ལྟ་བུར་སྟོན་པར་སྣང་སྟེ། དེ་ལྟར་སྦྱོར་བ་མཐོང་བ་ལ་གོམས་པའི་ཕྱིར་རོ། །

[Block 480]
དེ་ཙམ་གྱིས་ཐམས་ཅད་ལ་ཐ་དད་པ་ནི་མ་ཡིན་ཏེ། གཞན་ལ་ཡང་སྐྱེས་བུའི་འདོད་པའི་དབང་གིས་འཇུག་པ་ལ་གགས་བྱེད་པ་མེད་པའི་ཕྱིར། དཔེར་ན་གཅིག་ལ་འགའ་ཞིག་ཏུ་གཅིག་གི་ཚིག་གིས་སྒྲོ་འདོགས་ལ། དེར་ཁྱད་པར་མེད་ཀྱང་གུས་པ་ལ་སོགས་པ་བརྗོད་པའི་ཕྱིར། མང་པོའི་ཚིག་གིས་སྒྲོ་འདོགས་པ་ལྟ་བུའོ། །

[Block 481]
དགོས་པ་མེད་པའི་ཕྱིར་བརྡ་ཐ་དད་པར་མི་འགྱུར་རོ་ཞེ་ན། དེ་ཡང་ཡོད་པ་ཁོ་ན་སྟེ༌[^333]འདི་ལྟར།

[Block 482 [VERSE]]
ཁྱད་པར་གཞན་ནི་སྤོང་བ༌[^334]དང་། །
མི་སྤོང་བ་དག་དེ་གཉིས་ཀྱི། །
བརྡ་ཡི་བྱེ་བྲག་རྟོགས་པ་པོའི། །
འདོད་པའི་རྗེས་སུ་བྱེད་པའི་གཞི། །

[Block 483]
གང་གི་ཚེ་རྟོགས་པར་བྱེད་པ་འདི་དེ་ལས་གཞན༌[^335]རྣམ་པར་བཅད་པ་ཡོད་པ་ལ་མི་ལྟོས་པར་གོང་དུ༌[^336]ཁྱད་པར་ལ་རྟ་རྣམ་པར་བཅད་པ༌[^337]ཙམ་ཤེས་པར་འདོད་པ་ན། དེ་ལྟ་བུ་ཤེས་པར་བྱ་བའི་ཕྱིར་དེ་ལྟར་བརྡར་བྱས་པའི་སྒྲས་འདི་ལ་རྟ་མ་ཡིན་པ་ཉིད་ཡོད་དོ་ཞེས་བྱ་བར་རབ་ཏུ་ཤེས་པར་བྱེད་དོ། །

[Block 484]
གང་གི་ཚེ་རྣམ་པར་བཅད་པ༌[^338]གཞན་གྱིས༌[^339]མི་འདོད་པ་མེད་པར་དེ་ཤེས་པར་འདོད་པ་དེའི་ཚེ་ནི་དེ་ལྟར་རབ་ཏུ་བསྟན་པའི་ཕྱིར། རྣམ་པ་གཞན༌[^340]པ་གཞན་ཡོངས་སུ་མ་སྤངས་པ་ལ་འདི་ནི་རྟ་མ་ཡིན་པ་ཡིན་ནོ། །ཞེས་རབ་ཏུ་སྦྱོར་རོ། །

[Block 485]
དེ་ཉིད་ཀྱི་ཕྱིར་སྔ་མ་ལ་ནི་སྒྲ་འཇུག་པ་ཁྱད་པར་གཞན་སྤངས་པའི་ཕྱིར་གཞི་མཐུན་པ་ཉིད་དམ། ཁྱད་པར་དང་ཁྱད་པར་གྱི་གཞི་དངོས་པོ་མ་ཡིན་ཏེ། འདིའི་བ་ལང་ཉིད་དཀར་པོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 486]
དེ་ཙམ་གྱི་ཁྱད་པར་གྱིས་བློ་དེའི་རྟེན་དུ་གྱུར་པ་གཅིག་པ་ཉིད་དུ་མི་སྣང་བའི་ཕྱིར་དང་། འདོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 487]
གཉིས་པ་ལ་ནི་ཡོད་དེ་དེ་ལྟ་བུའི་བརྡའི་རྗེས་སུ་འབྲང་བའི་ཕྱིར། རྣམ་པར་བཅད་པའི་ཆོས་མཐའ་དག་བསྡུས་པས་རྣམ་པར་དབྱེ་བ་དང་ལྡན་པ་གཅིག་ལྟ་བུར་སྟོན་པར་སྣང་བའི་ཕྱིར་དང་། རྣམ་པར་བཅད་པ་གཞན་འདོད་པ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 488 [VERSE]]
ཀུན་ལ་རྫས་དང་དངོས་བརྗོད་པའི། །
སྒྲ་ཡི་ཁྱད་པར་འདི་ཉིད་དེ། །
དེའི་ཕྱིར་དེ་དག་བརྗོད་བྱ་ལ། །
ཁྱད་པར་འགའ་ཡང་ཡོད་མ་ཡིན། །

[Block 489]
དེ་ལྟ་བས་ན་ཐམས་ཅད་དུ་ཆོས་དང་ཆོས་ཅན་བརྗོད་པའི་སྒྲ་དག་གིས་བརྗོད་པར་བྱ་བའི་དོན་ལ་ངེས་པའི་ཤེས་པའི་ཡུལ་ཉིད་དུ་ཁྱད་པར་འགའ་ཡང་མེད་དེ། གཅིག་གིས་ནི་དེ་ཉིད་ཤེས་པར་བྱེད་པ་ལ་ཁྱད་པར་གཞན་སྤངས་ཏེ་ཤེས་པར་བྱེད་པ་ལ། གཞན་གྱིས་ནི་མ་སྤངས་ཏེ། ཤེས་པར་བྱེད་པས་ཁྱད་པར་ནི་དེ་ཡོད་དོ། །

[Block 490 [VERSE]]
དོན་དེ་ཤེས་པར་བྱེད་འདོད་པས། །
དེ་ལ་ཕན་པའམ་བྱེད་ལྡན་པའམ། །
གལ་ཏེ་གཞན་གྱིས་བརྗོད་ཀྱང་རུང་། །
དེ་ལས་ཁྱད་པར་གཞན་མེད་དོ། །

[Block 491]
ཁྱད་པར་དེ་ཙམ་ཁོ་ན་སྟོན་པར་བྱེད་པ་ན་དེ་ལྟ་བུའི་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ།[^341] །བརྩེད་པ༌[^342]ཉིད་ཅེས་དེ་ལ་ཕན་པས་སྟོན་ཀྱང་རུང་། བརྩེད་པ༌[^343]ཞེས་བྱེད་པ་དང་ལྡན་པས་ཀྱང་རུང་། རང་གིས་བྱས་པའི་གཞུང་ལུགས་གཞན་གྱིས་ཀྱང་རུང་། དེ་སྐད་དུ་བརྗོད་པ་ཙམ་གྱིས་ནི་དེ༌[^344]དོན་གཞན་པ་ཉིད་དུ་འགྱུར་ཏེ། དེ་ལྟ་བུ་ཁོ་ན་ཤེས་པར་བྱ་བའི་ཕྱིར་སྒྲ་བརྡར་བྱས་པའི་ཕྱིར་རོ། །

[Block 492]
བརྩེད་པ༌[^345]ཉིད་ཅེས་བྱ་བ་འབྲེལ་པ་ལ་བྱ་བ་མ༌[^346]ཡིན་ནམ། འཚེད་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེ་ན། ཇི་སྐད༌[^347]དུ་བརྗོད་པ་ལྟ་བུར་འཚེད་པ་དང་། འཚེད་པ་པོ་གཞན་འགའ་ཁོ་ན་ཞིག་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 493]
འདིའི་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་བསྟན་ཟིན་ཏོ། །

[Block 494]
དེ་ཉིད་འཚེད་པས་ཀྱང་བརྗོད་དོ། །

[Block 495]
གཏིང་མི་ཚུགས་པ་ལོག་པའི་རྣམ་པར་རྟོག་པ་དག་གིས་ཆོག་གོ།[^348] །ཇི་ལྟར་བྱ་བ་དོན་གཞན་དུ་གྱུར་པའམ། དེ་དག་གི་འདུ་བ་མ་ཡིན་པ་དེ་ནི་འོག་ནས་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
