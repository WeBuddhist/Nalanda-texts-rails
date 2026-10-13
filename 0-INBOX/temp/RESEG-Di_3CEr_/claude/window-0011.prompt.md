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
[Block 386]
གྲུབ་སྟེ་འདི་ལྟར་ཀུན་གྱི་རྗེས་ཐོགས་ལས་རླུང་ལ་སོགས་པའི་རང་བཞིན་རྗེས་སུ་དཔག་པར་གྲུབ་པའོ། །

[Block 387]
དེ་སྐད་དུ་ཡང་རེག་བྱ་ནི་མཐོང་བ་རྣམས་ཀྱི་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ཡོད་པར་མ་གྲུབ་པའི་ཕྱིར་དང་། ལྡོག་པ་ཡང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 388]
རླུང་ལ་སོགས་པ་ཡོད་པར་གྲུབ་ན་ནི་མི་ལྡོག་པ་ཡང་སྲིད་དེ། ཡོན་ཏན་གྱི་བྱེ་བྲག་དང་འབྲེལ་པ་ལས་ཡོན་ཏན་གྱི་སྤྱི་བོར་ནས་ཡོན་ཏན་གྱི་བྱེ་བྲག་གིས༌[^318]རྫས་ཀྱི་བྱེ་བྲག་རྗེས་སུ་དཔོག་པར༌[^319]བྱེད་ལ། རེག་ན་ཡོད་པར་ནི་གྲུབ་པ་མེད་དོ།[^320] །

[Block 389]
ས་ལ་སོགས་པ་ལས་ལོག་པ་དང་ཡང་མཚུངས་པར་འགྱུར་ཏེ། ཡོན་ཏན་གྱི་བྱེ་བྲག་མ་མཐོང་ཞིང་མ་མཐོང་བ༌[^321]ཙམ་གྱིས་མཐོང་བ་ལས་ལོག་པར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 390]
དེ་ལྟར་ཡང་རིགས་པ་མ་ཡིན་ཏེ།

[Block 391]
མཐོང་བ་ལུས་ཅན་ཐོགས་པ་དང་བཅས་པ་ཙམ་ལས།

[Block 392]
ཡིད་ཀྱི་ཡོན་ཏན་རྗེས་སུ་དཔོག་པའི་ཕྱིར་རེག་བྱ་ལྡོག་པར་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 393]
གང་གི་ཕྱིར་མཐོང་བ་རྣམས་ལས༌[^322]མཐོང་བའི་ཕྱིར་དང་། མ་མཐོང་བ་རྣམས་ལས་མ༌[^323]མཐོང་བའི་ཕྱིར་རེག་བྱ་ནི་མཐོང་བ་རྣམས་ཁོ་ནའོ། །

[Block 394]
དེ་རྣམས་ནི་དུ་མ་ཡིན་པའི་ཕྱིར་འདི་གང༌[^324]གི་ཡིན་ཞེས་ཐེ་ཚོམ་དུ་ནི་འགྱུར་རོ། །

[Block 395]
དེའི་ཕྱིར་ཐམས་ཅད་བཀག་ནས་རླུང་རྗེས་སུ་དཔོག་པ་ནི་རིགས་པ་མ༌[^325]ཡིན་ནོ། །

[Block 396]
གཞན་ཡང་།

[Block 397]
ཡིད་ཆེས་ཚིག་གི་སྒྲུབ༌[^326]བྱེད་ཀྱིས། །དེ་ལས་གཞན་ལ་འགེགས་པར་བྱེད། །

[Block 398]
འདིས་ཀྱང་སྟེ། གང་འདི་རྫས་ཀྱི་སྤྱི་རྗེས་སུ་དཔག་ནས་དེ་ལ་ཡོད་པར་རྗེས་སུ་དཔོག་པ༌[^327]བོར་ནས། ཡིད་ཆེས་པའི་ཚིག་གི་ཚད་མས་རྫས་གཞན་ལ་ཡོད་པ་བཀག་ནས་རླུང་ལ་ཡོད་པ༌[^328]སྒྲུབ་པར་བྱེད་པས་ན་ཡང་དེ་ཉིད་ཀྱིའོ། །

[Block 399]
དེ་བཞིན་དུ་གཞན་རྣམས་ཀྱི་ཡང་ཡིན་ནོ། །

[Block 400]
དེའི་ཕྱིར་རླུང་ལ་སོགས་པ་ལུང༌[^329]ལས་གྲུབ་པ་ཙམ་དུ་ནི་འགྱུར་རོ། །

[Block 401]
གལ་ཏེ་ཐ་མི་དད་དུ་གྲུབ་ཅེ་ན། འདི་ལྟར་ལུང་དང་རྗེས་སུ་དཔག་པ་དག་གིས༌[^330]ཐ་མི་དད་དུ་གྲུབ་པའི་ཕྱིར༌[^331]རྗེས་སུ་དཔག་པ་རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན། དེ་ནི། མ་ཡིན་ཐ་དད་ཀྱང་སྲིད་ཕྱིར། །རབ་ཏུ་གྲགས་པའི་དབང་གིས༌[^332]དཔེ་ནི་བསྟན་པར་མི་བྱའོ་ཞེས་ཁ་ཅིག་གིས་རྗེས་སུ་དཔག་པ་ལས་སྒྲ་ཐ་དད་དུ་འབྱེད་པར་བྱེད་དོ། །

[Block 402]
དེ་ལྟར་གྲགས་པའི་ཕྱིར་དཔེ་བསྟན་པར་མི༌[^333]བྱ་བ་ཡིན་ན་ནི་དཔེར་ན་དུད་པ་ལས་མེ་རྗེས་སུ་དཔོག་པ་ལྟ་བུ་དེར་དོན་ཡོད་པའི་རྗེས་སུ་དཔོག་པ་ཡང་སྒྲར་ཐལ་བར་འགྱུར་རོ། །

[Block 403]
གཞན་དག་ནི་དོན་གྱི་སྒྲ་ལ་ཐ་མི་དད་ཀྱི། སྒྲས་ཉེ་བར་བརྟགས་པ༌[^334]སྟེ་དོན་དེ་ཉིད་རྗེས་སུ་དཔོག་པ༌[^335]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁྱད་པར་རོ་ཞེས་ཟེར་རོ། །

[Block 404]
དེ་ལྟ་ན་ཡང་སྒྲས་ཐ་མི་དད་དུ་ཉེ་བར་བརྟགས་པ༌[^336]ལས་དོན༌[^337]རྗེས་སུ་དཔོག་གོ་ཞེས་ཇི་ལྟར་བརྗོད་པར་བྱ། ཤིང་གི་སྒྲའི་བརྗོད་བྱའི་དོན་གཞན་མ་ཡིན་པས་རྫས་ཀྱི་སྒྲས་དོན་དེ་ཉིད་གོ་རུ་ཟིན་ཀྱང་ཚུལ་གཞན་གྱི་སྒོ་ནས་རྫས་གཞན་མ་ཡིན་པ་ལས་བཟློག་པ་གོ་བ་ཡིན་ནོ། །

[Block 405]
གལ་ཏེ་ཤིང་གི་སྒྲས་རྫས་མ་ཡིན་པ་ལས་ལོག་པ་གོ་བར་བྱེད་དུ་ཟིན་མོད་ཀྱིས་ཀྱང་དོན་ལས་ཡིན་གྱི་སྒྲ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 406]
དེའི་ཕྱིར་སྐྱོན་མེད་དེ་ཞེ་ན། སྐྱོན་དུ་ནི་མི་འགྱུར་ལ་རག་ལ། ཤིང་ལ་སོགས་པའི་ཚིག་ལས་གཞན་པའི་སྒྲ་ཉིད་ཚད་མར་བརྗོད་པར་བྱ་སྟེ། བྱ་བ༌[^338]བརྗོད་པའི་སྒྲས་ཀྱང་དོན་གྱི་ཚུལ་དེ་ཉིད་གོ་བར་བྱེད་དོ། །

[Block 407]
གང་དག་ངག་ཁོ་ན་སྒྲ་ཡིན་ཏེ། ཚིག་ནི་དེ་རྟོག་པར་བྱེད་པའི་རྒྱུ་མ་ཡིན་ལ། སྒྲ་དེའི་ངོ་བོ་ཙམ་ལས་དོན་རྟོགས་པའི་ཕྱིར་རོ་ཞེས་ཁྱད་པར་ཅན་གཞན་ཙམ་ཉེ་བར་བླངས་ནས་རྗེས་སུ་དཔག་པ་ལས་སྒྲ་ཐ་དད་དུ་བརྗོད་ཅེས་བརྗོད་དོ། །

[Block 408]
དེ་ལ་བསམ་པ་ནི་སྒྲ་དང་བྲལ་བའི་རྟགས་དེ་རྗེས་སུ་དཔག་པར་བརྗོད་པ་ཡིན་ནོ། །

[Block 409]
སྒྲ་ཡང་ཡུལ་ཐུན་མོང་མ་ཡིན་པ་དང་འབྲེལ་བ༌[^339]ཡོད་པ་མ་ཡིན་པས་རྣམ་པ་གཉིས་ཀ་རྗེས་སུ་དཔག་པ༌[^340]བརྟག་པར་བྱ་སྟེ། མཐོང་བའི་དོན་དང༌[^341]མ་མཐོང་བའི་དོན་ནོ། །

[Block 410]
དེ་ལ་མཐོང་བའི་དོན་ལ་ནི་མི་གསལ་བར་བྱེད་པའོ། །

[Block 411]
མ་མཐོང་བའི་དོན་ལ་ནི་རྣམ་པར་རྟོག་པ་ཙམ་འབའ་ཞིག་སྟེ། དོན་གྱི་བྱེ་བྲག་རྟོགས་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 412]
གལ་ཏེ་མཐོ་རིས་ལ་སོགས་པའི་སྒྲས་དོན་ཙམ་བརྗོད་པ་ནི་མ་ཡིན་ན་ཇི་ལྟར་རྗེས་སུ་དཔག་པ་ཉིད་དུ་འགྱུར་ཞེ་ན།

[Block 413 [HEADING]]
#### ཡིད་ཆེས་ཚིག་རྗེས་སུ་དཔག་པ་ཉིད། ^2-1-4-0

[Block 414 [VERSE]]
ཡིད་ཆེས་ཚིག་ཀྱང་མི་སླུ་བར། །
མཚུངས་ཕྱིར་རྗེས་སུ་དཔག་པ་ཉིད། །

[Block 415]
ཡིད་ཆེས་པའི་ཚིག་ཉིད་བཟུང་ནས་ཀྱང་མི་བསླུ་བར༌[^342]མཚུངས་པའི་ཕྱིར་དེ་ཡང་རྗེས་སུ་དཔག་པ་ཉིད་དུ་བརྗོད་དོ། །

[Block 416]
དེ་སྐད་དུ་ཡང་། མིང་གི་ལས་རྣམས་ཀྱི་དོན༌[^343]དུ་མངོན་སུམ་སོང་བའི་ཕྱིར་རོ་ཞེས་འབྱུང་ངོ་། །དེ་དག་གིས་ནི་ཕྱོགས་དང་གཙོ་བོ་ལ་སོགས་པའི་རང་བཞིན་ལ་ཡང་རྗེས་སུ་དཔག་པ་དགག་པར་བྱའོ། །

[Block 417]
དེའི་ཕྱིར་རྗེས་སུ་དཔག་པའི་ཡུལ་ནི་རང་གི་མཚན་ཉིད་མ་ཡིན་ནོ། །

[Block 418 [HEADING]]
#### ཚུལ་གསུམ་པའི་རྟགས། ^2-1-5-0

[Block 419]
ཚུལ་གསུམ་པའི་རྟགས་ཞེས་གང་བརྗོད་པ་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 420 [VERSE]]
རྗེས༌[^344]དཔག་བྱ་དང་དེ་མཐུན་ལ། །
ཡོད་དང་མེད་ཉིད་ལ་མེད་པའོ། །

[Block 421]
རྗེས་སུ་དཔག་པར་བྱ་བ་ནི་ཆོས་ཀྱི༌[^345]ཁྱད་པར་དུ་བྱས་པའི་ཆོས་ཅན་ནོ། །

[Block 422]
དེ་ལ་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པས་མཐོང་གི༌[^346]རྗེས་ལ་དེའི་རིགས་དང་མཐུན་པ་ལ་ཡང་སྤྱིའི་ཚུལ་གྱིས་ཕྱོགས་ཐམས་ཅད་དམ་ཕྱོགས་གཅིག་ལ་ཡོད་པར་གྲུབ་པའོ། །

[Block 423]
[^347]ཅིའི་ཕྱིར་ཞེ་ན། དེ་དང་མཐུན་པ་ཁོ་ན་ལ་ཡོད་ཅེས་ངེས་པར་གཟུང་བའི་ཕྱིར་རོ། །

[Block 424]
དེ་དང་མཐུན་པ་ལ་ཡོད་པ་ཁོ་ནའོ་ཞེས་ནི་བརྗོད་པར་མི་བྱ་བའི་ཕྱིར་རོ། །

[Block 425]
མེད་པ་ཉིད་ལས་མེད་པ་ཞེས་པས་ནི་སླར་ཡང་དེ་ཉིད་ངེས་པར་བྱ་བའི་དོན་དུ་སྟེ། མེད་པ་ཉིད་ལ་མེད་པ་ཉིད་ཡིན་གྱི་གཞན་ལ་ཡང་མ་ཡིན་ལ་འགལ་བ་ལ་ཡང་མ་ཡིན་ནོ་ཞེས་པའི་དོན་ནོ། །
--- END BLOCKS ---
