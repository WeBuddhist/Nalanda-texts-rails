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
[Block 526]
གྲོང་ཁྱེར་དྲུག་ཅེས་བྱ་བ་ཡང་ཇི་ལྟར་མང་པོ་དག་ལ་གཅིག་གི་ཚིག་ཏུ་འགྱུར། གྲོང་ཁྱེར་ཉིད་ཀྱང་ཅུང་ཟད་ཀྱང་མེད་ན། དེ་རྣམས་ལ་སྡུད་པ་ལྟ༌[^370]ག་ལ་ཡོད། ཁང་བཟངས་དང་སྐྱེས་བུ་ལ་སོགས་པ་རིགས་མི་མཐུན་པ་རྣམས་ཀྱིས་མི་རྩོམ་པའི་ཕྱིར། དེ་རྣམས་ཀྱི་སྤྱི་ལྟ་ཞིག་རྫས་གང་ལ༌[^371]ཡིན་ཏེ། ལྡན་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 527]
ལྡན་པ་ནི་མ་ཡིན་ཏེ། ཁང་བཟངས་རང་ཉིད་ལྡན་པའི་བདག་ཉིད་ཡིན་པ་གཞན་དང་མི་ལྡན་པའི་ཡང་ཕྱིར་རོ། །

[Block 528]
དེ་ཉིད་ཀྱི་ཕྱིར་གྲངས་ཀྱང་མེད་དེ། གལ་ཏེ་གྲོང་ཁྱེར་ནི་ལྡན་པ་དེ་དང་སྐྱེས་བུས་ཁྱད་པར་དུ་བྱས་པའི་ཡོད་པ་ཡིན་ནོ་ཞེ་ན། བོགས་དབྱུང་དུ་མེད་པ་འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། ཡོད་པ་ཡང་གཅིག་ཡིན་པའི་ཕྱིར། གྲོང་ཁྱེར་མང་པོ་ཉིད་ལ་ཡང་གྲོང་ཁྱེར་རྣམས་ཞེས་མང་པོའི་ཚིག་ཏུ་མི་འགྱུར་རོ།[^372] ། གལ་ཏེ་གཉིས་ཕན་ཚུན་གྲོགས་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེ་ན། ཕན་པར་བྱ་བ་དང་ཕན་པར་བྱེད་པ་པོ་མ་ཡིན་པ་དག་ལ་གྲོགས་བྱེད་པའི་དངོས་པོ་ཅི་ཞིག་ཡོད། སྐྱེས་བུ་དང་ལྡན་པ་དང་། ཡོད་པ་རྣམས་ཀྱང་མང་བའི་ཕྱིར། ཇི་ལྟར་གྲོང་ཁྱེར་ཞེས་གཅིག་གི་ཚིག་ཏུ་འགྱུར། གལ་ཏེ་དེ་ལྟ་བུ་རྣམས་དོན་འགའ་ཞིག་ལ་ནུས་པ་ཐ་མི་དད་པ་ཡོད་པས་དེ་རྒྱུ་མཚན་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ནུས་པ་ནི་དངོས་པོའི་ངོ་བོ་ལས་ཐ་མི་དད་པའི་ཕྱིར་རོ།། །།

[Block 529]
བམ་པོ་གསུམ་པ། འོན་ཏེ་ཐ་དད་ན་ནི་ཕན་པར་བྱ་བ་མ་ཡིན་པ་ལ་གཞན་གྱི་དབང་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 530]
འོན་ཏེ་ཕན་ན་ནི་ནུས་པ་ལ་ཕན་འདོགས་པའི་ནུས༌[^373]པས་ཐུག་པ་མེད་པའི་ཕྱིར་རྟོགས་པ་མེད་དོ། །

[Block 531]
འོན་ཏེ་དེ་དང་ཐ་མི་དད་ན་ནི་དང་པོ་ལ་ཡང་ཐལ་བར་འགྱུར་བས་ད་ནི་གྱི་ནའོ། །

[Block 532]
ནམ་མཁའི་རང་བཞིན་ནམ་མཁའ་ཉིད་ཅེས་བྱ་བ་ཐ་དད་པའི་རྟེན་གྱི་དྲུག་པར་ཡང་མི་འགྱུར་ཏེ། དེ་ལ་སྤྱི་ནི་མེད་དོ། །

[Block 533]
ཁྱབ་པ་ཉིད་ལ་སོགས་པ་ཡོན་ཏན་རྣམས་ལ་དེ་སྐད་དུ་བརྗོད་པ་ཡང་མ་ཡིན་ཏེ། དོན་གཞན་པ་ནི་དེའི་རང་བཞིན་ཡིན་པ་ཉིད་དུ་མི་རུང་བའི་ཕྱིར་དང་། དེ་དག་ཀྱང་རང་བཞིན་མེད་པ་ཉིད་དུ་ཐལ་བའི་ཕྱིར་རོ། །

[Block 534]
དེ་ཡང་རང་བཞིན་དོན་གཞན་པ་ཅན་ཡིན་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་ན་ཡང་རྟོགས་པ་མེད་དོ། །

[Block 535]
དེ་བཞིན་དུ་དངོས་པོ་དྲུག་གི་ཚོགས་ལ་སོགས༌[^374]པ་ལ་ཡང་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་སྤྱི་དང་གྲངས་དང་ལྡན་པ་ནི་མི་སྲིད་དོ། །

[Block 536]
ད་ནི་ཁྱད་པར་མེད་ན་ཇི་ལྟར༌[^375]ནམ་མཁའི་རང་བཞིན་ཞེས་བྱའི། ནམ་མཁའ་ཞེས་བྱ་བ་ཁོ་ན་ནི་མ་ཡིན་ཞེ་ན། ནམ་མཁའི་དོན་གཞན་དང་ཐུན་མོང་བའི་ངོ་བོ་ལ་མི་ལྟོས་པར་ནམ་མཁའ་ཞེས་བྱ་བའི་སྒྲ་འཇུག་པའི་རྒྱུའི་ངོ་བོ་ལ་དེ་ལྟ་བུར་ཤེས་པར་འདོད་པ་དེ་སྐད་དུ་བརྗོད་དོ། །

[Block 537]
ཐམས་ཅད་ལས་ལོག་པའི་རང་གི་ངོ་བོ་བརྗོད་པར་མི་སྲིད་བ༌[^376]མ་ཡིན་ནམ་ཞེ་ན། ངོ་བོ་ཉིད་དེ་བློ་ལ་འཇོག་པ་ནི་མ་ཡིན་ཏེ། དབང་པོས་མི་སོད་པ༌[^377]ཉིད་མ་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 538]
འདི་ནི་དེ་ལྟ་བུ་ཤེས་པར་བྱའོ་སྙམ་ནས་སྒྲས་ཉན་པ་པོ་ལ་རྣམ་པར་རྟོག་པའི་གཟུགས་བརྙན་དེའི་རང་གི་ངོ་བོ་དང་མ༌[^378]འབྲེལ་པ་གཏོད་པར་བྱེད་པ་འབའ་ཞིག་ཏུ་ཟད་དེ། འདི་ལྟར་དོན་མ་མཐོང་བ་ལ་ནི་དོན་གྱི་རྣམ་པར་རྟོག་པ༌[^379]ཙམ་མོ་ཞེས་བཤད་པ་ལྟ་བུའོ། །

[Block 539]
དེ་ལྟར་ན་རྟོགས་པར་བྱ་བ་དང་། རྟོགས་པར༌[^380]བྱེད་པ་དག་གིས་རང་གི་མཚན་ཉིད་རྟོགས་པ་དང་། བསྟན་པ་ནི་མ་ཡིན་ཏེ། མཐོ་རིས་ལ་སོགས་པ་ཐོས་པ་ལ་ཡང་དེ་ཉམས་སུ་མྱོང་བ་དག་དང་འདྲ་བར་སྣང་བ་ཐ་དད་པ་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 540]
དེའི་ཕྱིར་འདིས་དངོས་པོའི་རང་གི་ངོ་བོ་མ་རྟོགས་སུ་ཟིན་ཀྱང་རྣམ་པར་རྟོག་པའི་གཟུགས་བརྙན་དེ་ལྟ་བུ་ཁོ་ན་ལ་དེར་ལྷག་པར་ཞེན་པས་མགུ་བར་འགྱུར་ཏེ། སྒྲའི་དོན་རྟོགས་པ་ནི་དེ་ལྟ་བུ་ཁོ་ན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 541]
དེས་ན་རང་གི་མཚན་ཉིད་བསྟན་ཏོ་ཞེས་དེ་སྐད་དུ་བརྗོད་ཀྱི། རང་གི་ངོ་བོ་སྣང་བའི་རྣམ་པར་ཤེས་པ་ཁོ་ན་བསྐྱེད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 542]
ད་ནི་འོ་ན་ཇི་ལྟར་གཅིག་ཏུ་ལོག་པའི་ངོ་བོ་ཅན་རྣམས་ལ་སྤྱི་ཞེས་བྱ་སྟེ། དེ་དག་མ་འབྲེལ་བའི་ཕྱིར་དང་། [^381]གཞན་ཡང་མེད་པའི་ཕྱིར་རོ་ཞེ་ན། སྤྱི་ཇི་ལྟ་བུ་ཡིན་པ་ནི་བཤད་ཟིན་ཏེ། མ་འདྲེས་པ་རྣམས་ཀྱི་ཅིག་ཤོས་དང་མ་འབྲེལ་བ་དེ་ནི་དེ་ལས་ལྡོག་པ་ཅན་རྣམས་ཀྱི་འདྲ་བ་ཉིད་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 543]
གཞན་ཡང་།

[Block 544 [VERSE]]
ཐ་དད་དངོས༌[^382]རྣམས་ལ་བརྟེན་ནས། །
དོན་གཅིག་ཏུ་ནི་སྣང་བའི་བློ། །
གང་གི༌[^383]རང་གི་ངོ་བོ་ཡིས། །
གཞན་གྱི་ངོ་བོ་སྒྲིབ་བྱེད་པའི། །

[Block 545 [VERSE]]
ཀུན་རྫོབ་དེས་བདག་ཐ་དད་ཀྱང་། །
ཐ་དད་པ་ཉིད་བསྒྲིབས་པ༌[^384]ཡི། །
དངོས་རྣམས་ངོ་བོ་འགའ་ཞིག་གིས། །
ཐ་དད་མིན་པ་ལྟ་བུར་སྣང་། །

[Block 546 [VERSE]]
དེ་ལ་བསམ་པའི་དབང་གིས་ན། །
སྤྱི་ཡོད་པར་ནི་རབ་ཏུ་བསྒྲགས། །
དེ་ཡིས་ཇི་ལྟར་ཀུན་བརྟགས་པ། །
དེ་ནི་དམ་པའི་དོན་དུ་མེད། །

[Block 547]
རྣམ་པར་རྟོག་པ་ཅན་གྱི༌[^385]བློ་ནི་དེ་དག་ལས་གཞན་པ་ལས་ལྡོག་པ་ཅན་གྱི་དངོས་པོ་རྣམས་ལ་བརྟེན་ནས་སྐྱེ་བ་ན། རང་གི་བག་ཆགས་ཀྱི་རང་བཞིན་བྱེད་ཅིང་དེ་དག་གི་ངོ་བོ་ཐ་དད་པ་མི་སྣང་བར་བྱས་ནས། བདག་ཉིད་ཀྱི་རྣམ་པ་ཐ་དད་པ་མེད་པ་ཞེན་པར་བྱས་ཏེ། དེ་རྣམས་འདྲེས་པར་ཀུན་དུ་སྟོན་ཏོ། །

[Block 548]
བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པ༌[^386]གཅིག་པ་ཅན་ཉིད་ཀྱིས་ན་གཞན་ལས་ཐ་དད་པའི་དངོས་པོ་རྣམས་དང་། རྣམ་པར་རྟོག་པ་དེའི་བག་ཆགས་ཀྱི་རང་བཞིན་ནི༌[^387]དེ་དག་ལས་སྐྱེ་བ་ཅན་འདི་དེ་ལྟ་བུར་སྣང་བ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 549]
ད་ནི་ཀུན་རྫོབ་སྟེ་འདིས་རང་གི་ངོ་བོས་གཞན་གྱི་ངོ་བོ་སྒྲིབ་པའི་ཕྱིར་རོ། །

[Block 550]
དེ་དག་ནི་དེས་ཐ་དད་པ་བསྒྲིབས་པས་བདག་ཉིད་ཀྱིས་ཐ་དད་ཀྱང་ངོ་བོ་འགའ་ཞིག་གིས་ཐ་མི་དད་པ་བཞིན་དུ་སྣང་ངོ་། །དེ་བས་ན་རྗེས་སུ་བྱེད་པ་རྣམས་ཀྱི་བློའི་སྣང་བ་ལ་བློ་ལ་སྣང་བའི་དངོས་པོ་ལ་རྣམ་པའི་ཁྱད་པར་ཡོངས་སུ་འཛིན་པས་ཕྱི་རོལ་ལྟ་བུར་ཀུན་ཏུ་འཕྲོ་བ་དེ་དག་ཁོ་ནའི་སྤྱི་ཡིན་པར་བརྗོད་དོ། །

[Block 551]
ད་ནི་ཇི་ལྟར་གཞན་སེལ་བའི་སྤྱི་ཡིན་ཞེ་ན། དེ་ཉིད་གཞན་སེལ་བ་ཡིན་ཏེ། དེ་ན༌[^388]དེ་ཁོ་ན་འཛིན་པའི༌[^389]རྣམ་པར་རྟོག་པ་རྣམས་ནི་རང་བཞིན་གྱིས་འཁྲུལ་པའི་ཕྱིར་དངོས་པོ་འཛིན་པ་ལྟ་བུར་སྣང་ངོ་། །དེ་ནི་དེ་ལས་གཞན་པ་ལས་ཐ་དད་པའི་དངོས་པོ་རྣམས་ཁོ་ན་ལ་སྐྱེ་བ་ན་ཐ་དད་པའི་ཡུལ་ཅན་ཞེས་བྱ་བར་ཤེས་སོ། །

[Block 552]
ཕྱི་རོལ་པ་རྣམས་ཐ་དད་པ་ཡིན་ན་དེ་དག་ལ་ནི་རྣམ་པར་རྟོག་པ་མི་འཇུག་པ་ཡིན་ནམ། ཇི་ལྟར་དེ་དག་ལ་སྐྱེ་ཞེ་ན། འཆད་པར་བྱེད་པ་རྣམས་དེ་ལྟར་རྣམ་པར་འབྱེད་པར་བྱེད་ཀྱི། ཐ་སྙད་འདོགས་པར་བྱེད་པ་རྣམས་ནི་མ་ཡིན་ཏེ། དེ་དག་ནི་རང་གི་དམིགས་པ་ཁོ་ན་དོན་བྱེད་པར་རུང་བར་སེམས་ཤིང་སྣང་བ་དང་། རྣམ་པར་བརྟག་པར༌[^390]བྱ་བའི་དོན་དག་གཅིག་ཏུ་བྱས་ནས་འཇུག་གོ། །

[Block 553]
དེ་དག་གི་བསམ་པའི་དབང་གིས་དེ་སྐད་ཅེས་བྱ་བ་དང་། དེ་བཞིན་དུ་སྒྲས༌[^391]དེ་བྱེད་པ་ཉིད་ཀྱིས་དེ་བྱེད་པ་མ་ཡིན་པ་དག་ལས་ལོག༌[^392]པ་རྣམས་སྟོན་པར་བྱེད་དོ་ཞེས་བརྗོད་དོ། །

[Block 554]
དེ་ཁོ་ན་ཉིད་སེམས་པར་བྱེད་པ་རྣམས་ནི། སྣང་བ་ཐ་དད་པ་ལ་སོགས་པའི་སྒོ་ནས་ཐ་དད་པ་མེད་པར་མི་སེམས་སོ། །

[Block 555]
གལ་ཏེ་རྟོགས་པ་པའི༌[^393]བསམ་པའི་རྗེས་སུ་བྱེད༌[^394]ན་གཞན་སེལ་བ་ཡང་སྤྱི་ཡིན་པར་འགྱུར་ཏེ། [^395]དེ་ལྟར་རྟོགས་པ་ནི་མེད་དོ་ཞེ་ན། དེ་ལྟར་མི་རྟོགས་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་བསལ་བ༌[^396]ལས་ཐ་དད་པ་དང་ཐ་མི་དད་པ་དང་། གཅིག་པ་དང་ཁྱབ་པ་ཉིད་ལ་སོགས་པའི་རྣམ་པས༌[^397]ཀྱང་མི་རྟོགས་པ་ཉིད་དོ། །

[Block 556]
བློ་རྣམ་པ་ཐ་མི་དད་པ་ཅན་སྐྱེ་བ་དེའི་རྟེན་གང་ཡིན་ཞེ་ན། གཞན་སེལ་བ་ཡིན་ནོ་ཞེས་བརྗོད་པ༌[^398]འབའ་ཞིག་ཏུ་ཟད་དེ། དེ་ནི་དངོས་པོ་རྣམས་ལ་ཡོད་པའི་ཕྱིར་དང་། འགལ་བ༌[^399]མེད་པའི་ཕྱིར་དང་། སྒྲའི་རྟེན༌[^400]ཅན་གྱི་ཐ་སྙད་ཀྱང་དེ་ལྟར་སྣང་བའི་ཕྱིར་རོ། །

[Block 557]
བློ་འདི་ཇི་ལྟར་སྣང་བ་ལྟ་བུར་སྤྱི་ཞེས་བྱ་བ་དངོས་པོར་གྱུར་པ་ནི་ཅུང་ཟད་ཀྱང་མེད་དེ། འདི་ལྟར།

[Block 558 [VERSE]]
བསལ་བ༌[^401]རྣམས་ནི་རྗེས་མི་འགྲོ། །
རྗེས་འགྲོ་གཞན་ནི༌[^402]སྣང་བ་མེད། །

[Block 559]
བསལ་བ༌[^403]འདི་དག་ནི་ཕན་ཚུན་རྗེས་སུ་འགྲོ་བ་མ་ཡིན་ཏེ། ཐ་དད་པ་མེད་པས་སྤྱི་ཉིད་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 560]
དེ་རྣམས་ལས་གཞན་པ་ཐ་དད་པ་ཡང་ཅུང་ཟད་ཀྱང་དེ་ལྟ་བུའི་བློ་ལ་མི་སྣང་སྟེ། མི་སྣང་ན་ཇི་ལྟར་བདག་ཉིད་དུ་གཞན་འཛིན་པའམ་ཐ་སྙད་འདོགས་པར་བྱེད་དེ། དེ་དག་དང་འབྲེལ་པ་གཅིག་ཡོད་པའི་ཕྱིར་ཡང་སྤྱི་ཡིན་པར་མི་འགྱུར་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 561]
གལ་ཏེ་ཐ་མི་དད་པའི་བརྗོད་པ་དང་། བློའི་རྒྱུ་མཚན་དུ་གྱུར་པ་གཅིག༌[^404]སྤྱི་ཡིན་གྱི་ཐམས་ཅད་ནི་མ་ཡིན་ནོ་ཞེ་ན། ཇི་ལྟར་གཞན་གྱི་སྒོ་ནས་གཞན་ལ་ཤེས་པ་འཇུག །དེ་དང་འབྲེལ་པའི་ཕྱིར་རོ་ཞེ་ན། གྲངས་དང་འབྲས་བུའི་རྫས་ལ་སོགས་པ་ཡོད་ན་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 562]
གལ་ཏེ་སྤྱིའི་བདག་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། སྤྱིའི་བདག་ཉིད་འདི༌[^405]གང་ཡིན་ཞེས་དེ་ཉིད་དཔྱོད་པ་མ་ཡིན་ནམ། དེ་ལ་འབྲེལ་པ་ཡོད་ན་ཤེས་པ་འཇུག་སྟེ། དེས་ན་སྤྱི་ཡིན་ནོ་ཞེས་སྨྲས་པ་དེ་ལ་བཤད་པ༌[^406]རྒྱུ་མཚན་སྲིད་པའི་ཕྱིར་རྫས་ལ་སོགས་པ་དུ་མ་དང་འབྲེལ་པ་ཅན་དག་ལས་ཀྱང་ཤེས་པ༌[^407]འཇུག་སྟེ། དེའི་ཕྱིར་སྤྱིའི་བདག་ཉིད་ཡིན་ནོ། །

[Block 563]
དེ་ལྟ་མ་ཡིན་ན་གཞན་ལ་ཡང་མི་འཇུག་སྟེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 564]
དེ་ལྟ་ན་ནི་རྫས་དང་ཡོན་ཏན་དང་སྤྱི་རྣམས་ཀྱི་ངོ་བོ་འཆོལ་བ་ཡིན་ནོ། །

[Block 565]
དེ་ལྟ་ན་འོ་ན་ནི། བློའི་སྣང་བ་ཁོ་ན་ཤེས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ཡོད་པ་ཉིད་པས་སྤྱི་ཡིན་ནོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར། ཤེས་དང་ཐ་དད་མ་ཡིན་པ། ཇི་ལྟར་དོན་གཞན་འབྲང་བར་འགྱུར། །ཤེས་པ་པོའི་ངོ་བོ་ཇི་ལྟར་དོན་གཞན་རྣམས་ཀྱི་སྤྱི་ཡིན་ཏེ། དེ་ནི་དེ་རྣམས་ལ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
