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
[Block 701]
རྒྱུ་ལ༌[^545]ནི་གེགས་བྱེད་པ་ལ་སོགས་པ་ཡང་སྲིད་ལ་འབྲས་བུ་མེད་པར་ཡང་འབྱུང་བའི་ཕྱིར་འཁྲུལ་པས་ན་རྗེས་སུ་དཔག་པ་མ་ཡིན་ནོ། །

[Block 702]
གལ་ཏེ་རྒྱུ་ཉིད༌[^546]རྗེས་སུ་དཔག༌[^547]པར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ༌[^548]ཉེ་བར་བརྟགས་ནས་བརྗོད་པར་བྱའོ་ཞེ་ན།[^549] དེ་ལྟར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་གལ་ཏེ་འཁྲུལ་ན་ནི། དེ་རྟགས་མིན། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལས་ནི་དོན་དེའི་རྟགས་མ་ཡིན་ཏེ། ཐེ་ཚོམ་བསྐྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 703]
དེའི་ཕྱིར་འདིར་རྗེས་སུ་དཔག་པ་ཉེ་བར་གདགས་པ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 704]
རྒྱུ་ལ་འབྲས་བུའི་ཤེས་པ་དེ་འབྱུང་བ་སྲིད་ཀྱང་རྟགས་འཁྲུལ་པར་ངོ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 705]
འཁྲུལ་པར་བརྗོད་དོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དེའི་ཚེ་དེའི་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 706]
གང་གི་ཚེ་དེར་དོན་ཇི་ལྟ་བ་མ་ཡིན་པའི་ཉེས་པ་འབྱུང་བ་དེའི་ཚེ་ནི་དེའི༌[^550]རྗེས་སུ་དཔག་པ་མ་ཡིན་ནོ། །

[Block 707]
གལ་ཏེ་ཡང་རྒྱུ་དང་འབྲས་བུའི་ཤེས་པ་དང་མི་ལྡན་པས་ཡང་འཁྲུལ་པར་བྱེད་པ་ཉིད་མ་ཡིན་ལ། རག་ལས་པ་ཡིན་ན་ནི་དེ་ལྟར་ན། འབྲེལ་པ་གཞན་དག་འོས་པ༌[^551]ཡིན། དེ་ལྟ་ན་ནི་གང་མི་འཁྲུལ་བ་ལ་ལྟོས་པ༌[^552]དེ་ཉིད་མེད་ན་མི་འབྱུང་བ་ཉིད་དེ། [^553]དེ་རྗེས་སུ་དཔག་པའི་རྒྱུ་ཡིན་གྱི་འབྲས་བུ་དང་འབྲེལ་བ་ནི་མ་ཡིན་ནོ། །

[Block 708]
གལ་ཏེ་རྣམ་པར་དཔྱོད་པ་ཅན་གྱི་ལྷག་མ་དང་ལྡན་པ་ཉིད་ནི་རྗེས་སུ་དཔག་པ་སྟེ་གཞན་དུ་གཏན་ཚིགས་ཉིད་ལ་རྗེས་སུ་དཔག་པར༌[^554]ཉེ་བར་བརྟགས་ནས་བརྗོད་དོ་ཞེ་ན། དེ་བཞིན་དུ་དེའི་རྗེས་སུ་དཔག་པ་ཐམས་ཅད་ལ། དཔྱོད་དང་བཅས་པར་བརྗོད་པར་བྱ། །མངོན་སུམ་གྱིས་སྤྱི་ཙམ་བཟུང་ཡང་འདི་ལ་དོན་གྱི་བྱེ་བྲག་མི་ངེས་པའི་ཕྱིར་ཏེ། དེ་ན༌[^555]ལྷག་མ་དང་ལྡན་པ་ཁོ་ན་རྣམ་པར་དཔྱོད་པ་དང་བཅས་པ་ནི་མ་ཡིན་ཏེ། ཡོད་པའང་དཔྱོད་པ་དང་བཅས་ཕྱིར། །རྟགས་ཡོད་པར་གྲུབ་པ་འདི་ལ་ཅི་འདི་ལས་འགྱུར་རམ་འོན་ཏེ་མི་འགྱུར་ཞེས་རྣམ་པར་དཔྱོད་པའི་ཕྱིར་རོ། །

[Block 709]
འདི་ལྟར་ཆུ་ཀླུང་གང་བས༌[^556]ན་མི་འཁྲུལ་བ་ཉིད་ཡིན་ཞིང་རྣམ་པར་དཔྱོད་པ་དང་བཅས་པ་ཡིན་ཡང་བྱ་བ་དང་བྱེད་པ་ལས་ནི་མ་ཡིན་ཏེ། མེད་ན་མི་འབྱུང་བ་ལས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 710]
གལ་ཏེ་དེ་ལྟར་ངེས་པར་བཟུང་བ་བྱས་པས་གང་སྤྱི་མཐོང་བའི་རྗེས་སུ་དཔག་པ་དེ་དག་ནི་ལྷག་མ་དང་ལྡན་པ་དབང་པོའི་ཡུལ་ལས་འདས་པ་རྣམས་ཡང་དག་པར་རྟོགས་པར་བྱེད་དོ་ཞེ་ན། དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། གཞན་པ་ལས་ཀྱང་རབ་ཏུ་གྲུབ། ། གང་གི་ཚེ་རྗེས་སུ་འགྲོ་བ་ལ་སོགས་པ་དེ་ཉིད་ནས༌[^557]ཡང་ནས་ཡང་དུ་གཙོ་བོ་ཡོད་པ་ཉིད་ལ་སོགས་པ༌[^558]རྟོགས་པར་བྱེད་པ་དེའི་ཚེ་བྱེ་བྲག་མཐོང་བ་ལ༌[^559]ཡང་ཁོང་དུ་ཆུད་པར་མཐོང་བའི་ཕྱིར་ངེས་པར་བཟུང་བ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 711]
གཞན་ཡང་། གཙུག་ཕུད་ཅན་དོན་གཅིག་རྟོགས་དེས། །ལྷག་མ་དང་ལྡན་པའི་རྗེས་དཔག་གི་ཡན་ལག་ལས་དེའི་གཙོ་བོ་གཅིག་ཡོད་པ་ཉིད་ཁོང་དུ་ཆུད་པ་ནི༌[^560]འཐད་པ་སྟེ། དེའི་དངོས་པོ་ཉིད་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 712]
གལ་ཏེ་དེའི་ཡང་ཐ་དད་པ་ལས་རྟོགས་པར་མི་རིགས་སོ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་རྗེས་འགྲོ༌[^561]ལ་སོགས་པ་ལས་ཐ་དད་པ་ཉིད་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 713]
ཐ་དད་ཐ་སྙད་ཡོད་མིན་པའམ། །ཅི་སྟེ་ཐ་དད་ལས་གཞན་མ་ཡིན་པའི་རྗེས་སུ་འགྲོ་བ་ལ་སོགས་པ་ལས་གཙོ་བོ་གཅིག་ཉིད་ལ་སོགས་པ་བསྒྲུབ་པའི༌[^562]ཕྱིར་ལྷག་མ་དང་ལྡན་པའི༌[^563]གཏན་ཚིགས་ཀྱིས་ཅི་ཞིག་གོ་བར་བྱེད་ཅེས་བརྗོད་དོ། །

[Block 714]
དེ་ལྟ་ན་ནི་རྣམ་པར་ལྡན་པ་རྣམ་ལྔ་བརྗོད་པར་མི་བྱ་ཞིང་གཙུག་ཕུད་ཅན་གྱི་དོན་བཅུ་ཡང་མ་ཡིན་ནོ། །

[Block 715]
གཞན་ཡང་། སྐྱེས་བུའི་རྣམ་ཀུན་རྟོགས་མི་འགྱུར། སྐྱེས་བུའི་ཡོད་པ་ཉིད་དམ། མང་པོ་ཉིད་དམ། ཐ་དད་པའམ། ཐ་མི་དད་པ་ཡང་རུང་རྣམ་པ་ཐམས་ཅད་དུ་རྗེས་སུ་དཔག་པས་གོ་བར་མི་འགྱུར་ཏེ། སྐྱེས་བུའི་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 716]
དེ་ལྟ་བས་ན་གྲངས་ཅན་པ༌[^564]རྣམས་ཀྱི་རྗེས་དཔག་ནི་རིགས་པ་དང་མི་ལྡན་ནོ། །

[Block 717 [HEADING]]
### དཔྱོད་པ། ^2-6-0

[Block 718]
དཔྱོད་པ༌[^565]རྣམས་ཀྱི་ནི་རྗེས་སུ་དཔག་པ་ལ་སོགས་པ་མངོན་སུམ༌[^566]སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར། དེ་དང་མཚུངས་པ་ཉིད་ཡིན་པས་མདོར་མ་མཚོན་ནོ། །

[Block 719 [HEADING]]
#### འགྲེལ་པ་བྱེད་པ། ^2-6-1-0

[Block 720]
འགྲེལ་པ་བྱེད་པས་ནི་ངག་བྱེད་མཁན་གྱི་བསམ་པ་རྗེས་སུ་བཟླས་ནས་རྣམ་པར་ཕྱེའོ་ཞེས་ཟེར་རོ། །

[Block 721]
དེ་ལ།

[Block 722 [VERSE]]
མངོན་སུམ་སྔོན་འགྲོ་ཅན་ཡིན་ཕྱིར། །
རྗེས་དཔག་ལ་སོགས་མདོར་མ་མཚོན། །
ཞེ་ན་དྲན་འདོད་ཞེ་སྡང་དང་། །
རྩོལ་བ་ལ་སོགས་ཚད་མར་འགྱུར། །

[Block 723]
གལ་ཏེ་མངོན་སུམ་སྔོན་དུ་འགྲོ་བ་ཅན་དེ་ཉིད་ཚད་མ་ཉིད་དུ་ཤེས་ཟིན་པས་ངག་བྱེད་མཁན་གྱི་རྗེས་དཔག་ལ་སོགས་པ་མ༌[^567]བརྗོད་པ་དེ༌[^568]ལྟ་ན་ནི་མངོན་སུམ་སྔོན་དུ་སོང་བ་ཅན་ཡིན་པའི་ཕྱིར་དྲན་པ་ལ་སོགས་པ་ཡང་ཚད་མ་གཞན་ཉིད་དུ་འགྱུར་རོ། །

[Block 724]
འབྲེལ་པ་བྱེད་པས་གཞན་གཞུང་ལས་བཏོན་ཏེ་གཅིག་ཏུ་བསྟུན་ནས་ནི། རྗེས་དཔག་ལ་སོགས་བསྟན་པ་སྟེ།[^569] མངོན་སུམ་སྔོན་འགྲོ་ཅན་མ་ཡིན། །མངོན་སུམ་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་ནི་འབྲེལ་བའམ་ལྡན་པ་ལ་སོགས་པ་ལ༌[^570]མངོན་སུམ་པ༌[^571]ཉིད་དུ་བརྗོད་པར་བྱ་ན་འབྲེལ་པ་ཅན་ནམ་གཉིས་ཀ་ལྟར་ན་ཡང་རིགས་པ་མ་ཡིན་ཏེ།

[Block 725]
ལྡན་སོགས་ཡུལ་ལ་དབང་བློ་མེད། །ཡུལ་ལའང༌[^572]དེ་དག་ཡོད་མ་ཡིན། །

[Block 726]
དབང་པོ་ནི་ཐུན་མོང་མ་ཡིན་པའི་ཡུལ་ཅན་ནོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 727]
འབྲེལ་བ་ནི་དུ་མ་ལ་བརྟེན་པ་ཡིན་ན་དེ་ཇི་ལྟར་རྟོགས་པ༌[^573]མེད་པའི་དབང་པོའི་བློའི་ཡུལ་དུ་འགྱུར།[^574] འབྲེལ་བ་ཅན་ཡང་འབྲེལ་བ་ཅན་ཉིད་དུ་བཟུང་ན་ནི་རྗེས་སུ་དཔག་པ་ལ་སོགས་པ་ཉེ་བར་མཁོ་བར་འགྱུར་ན་མངོན་སུམ་གྱིས་ནི་དེ་ལྟ༌[^575]མ་ཡིན་ནོ། །

[Block 728]
འབྲེལ་པ༌[^576]བྱེད་པས་ནི་ཕལ་ཆེར་བྱེ་བྲག་པའི་རྗེས་སུ་དཔག་པ་ཉིད་རྗོད་པར་བྱེད་པ་སྟེ། མཐོང་བའི་སྤྱི་དང་མ་མཐོང་བའི་ལ་སོགས་པར་བྱེད༌[^577]པའི་ཕྱིར་རོ། །

[Block 729]
དེ་ལ་འདུ་བ་དང་དོན་གཅིག་ལ་འདུ་བ་དང་འགལ་བ་དང་དེ་དང་ལྡན་པ་རྣམས་ནི་མངོན་སུམ་པ་མ་ཡིན་ཏེ། དེས་ནི་ལྡན་པ་དང་བཅས་པའི་འབྲེལ་བ་ཅན་མངོན་སུམ་པར་གྱུར་པ་ཡིན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 730]
དེ་ལྟར་ཁས་ལེན་པ་ལ་བརྗོད་པ། ལྡན་པ་རྗེས་དཔག་གིས༌[^578]རྟགས་མིན། ལྡན་པ་ནི་མེ་དང་དུ་བ་དག་རྗེས་སུ་དཔོག་པ་མ་ཡིན་ཏེ། གཉིས་ཀའི་རྒྱུར་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 731]
རྣམ་པ་ཐམས་ཅད་ནས་གོ་བར་འགྱུར་རོ་ཞེས་བརྗོད་ཟིན་ཏོ། །

[Block 732]
ལྡན་པ་ཅན་ནི་རང་ངོ་བོས། །ཁོང་དུ་ཆུད་པར་བྱེད་མ་ཡིན། །

[Block 733]
འབྲེལ་པ་ཅན་གྱི་རང་གི་ངོ་བོས་ནི་རྗེས་སུ་དཔག་པ་ལ་འགའ་ཞིག་ཏུ་ཡང་ཕན་མི་འདོགས་སོ། །

[Block 734]
གཞན་མིན་མངོན་སུམ་ཡང་མ་ཡིན། །ཇི་ལྟར་རྟོགས་པ་དེས་རྗེས་སུ་དཔག་པ་ལ་ཕན་མི་འདོགས་པ་དེ་བཞིན་དུ་མངོན་སུམ་ལ་ཡང་ངོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 735]
རྗེས་སུ་དཔག་པ་དང་རྗེས་སུ་བསྟན་པ་དང་ཉེ་བར་གཞལ་བ་རྣམས་ལ་ནི་འདིར་དགག་པ་བརྗོད་པར་མི་བྱ་སྟེ། གང་གི་ཕྱིར། གང་དུ་ཕྱིར།

[Block 736]
གང་དུ་རྗེས་དཔག་ལ་སོགས་འདི། །བཀག་པ་དེ་བཞིན་དེ་ཡང་བཀག །

[Block 737]
འདིར་རང་གི་འདོད་པ་རྗེས་སུ་དཔག་པ་ལ་སོགས་པ་ཅུང་ཟད་ཀྱང་བསྒྲུབས་པ་མེད་དོ།[^579] །

[Block 738]
འབྲེལ་བ་གཞན་མ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 739]
འདིར་ཅུང་ཟད་བརྗོད་པ་ནི་བྱེ་བྲག་པའི་འདོད་པ་ཁ་ཅིག་ལས་སོ། །

[Block 740]
དེས་ན་དེ་བཀག་པ་བཞིན༌[^580]དུ་འདི་ཡང༌[^581]བཀག་པར་རིག་པར༌[^582]བྱའོ། །
--- END BLOCKS ---
