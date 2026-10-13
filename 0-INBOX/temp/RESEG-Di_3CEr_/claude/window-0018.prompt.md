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
[Block 631]
དེ་ལ་འབྲེལ་བ་ནི་རྣམ་པ་བདུན་ཏེ། དེ་རྣམས༌[^487]གང་ཡང་རུང་བའི་མངོན་སུམ་པ་གཅིག་གིས་ལྷག་པའི་དོན་མངོན་སུམ་པ་མ་ཡིན་པ་ངེས་པར་གྲུབ་པའི་གཏན་ཚིགས་དེ་ནི་རྗེས་སུ་དཔག༌[^488]པའོ། །

[Block 632]
རྟགས་ཀྱི་ཤེས་པ་ཅུང་ཟད་མ་ངེས་པར་འགྱུར་ཏེ། དོན་ཇི་ལྟ་བ་ནི་མ་ཡིན་ནོ་ཞེས༌[^489]ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་ཕྱིས༌[^490]ཀྱི་རྩོམ་པ་འཇུག་སྟེ། མངོན་སུམ་གྱི་སྤྱི་ཙམ༌[^491]ལས་ངེས་པར་མ་བཟུང་བའི་དོན་གྱི་བྱེ་བྲག་བསྟན་པ་ལས་བྱེ་བྲག་གི་རྟོགས་པ་བསྐྱེད་པ་ཐམས་ཅད་དོ་ཞེས་སོ། །

[Block 633]
དེ་ལྟ་བུ་འདོད་པ་ལྟར་ན་ཡང་མངོན་སུམ་པ་གཅིག་ལས་ཞེས་པ་ནི༌[^492]རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་མངོན་སུམ་ནི། རང་དོན་ཙམ་ལས༌[^493]ལྟ་བའི་ཕྱིར། །བ་ལང་ལ་སོགས་པའི་སྤྱི་དང་བྱེ་བྲག་གཉིས་ཀ་ལའང་རྣ་བ༌[^494]ལ་སོགས་པ་འཇུག་པ་ནི་མེད་དོ། །

[Block 634]
ཅི་སྟེ་ཡང་འདོད་དོ་ཞེ་ན་མ་ཡིན་ཏེ། རྣ་བ་ལ་སོགས་པའི་འཇུག་པ་ཐམས་ཅད་ནི་མངོན་སུམ་མ་ཡིན་ཏེ། དོན་ཇི་ལྟ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 635]
དེའི་ཕྱིར་དེ་ཉིད་བྱེ་བྲག་ཏུ་བརྗོད་པར་བྱ་སྟེ། གཞན་དུ་ཐ་དད༌[^495]དུ་མི་བྱ་བ་འཁྲུལ་བ༌[^496]མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཇི་སྐད་བརྗོད་པ་བཞིན་ནོ། །

[Block 636]
གལ་ཏེ་མངོན་སུམ་གྱི༌[^497]འབྲས་བུ་ལ་མངོན་སུམ་ཞེས་བརྗོད་པ་སྟེ། འདི་ལྟར་མངོན་སུམ་པ་གཅིག་ལས་ཞེས་འདིར་མངོན་སུམ་གྱི་འབྲས་བུ་ཡིན་གྱི་འཇུག་པ་ལ་མངོན་སུམ་མོ་ཞེས་བརྗོད་པ་ཡིན་པས་ན་དེའི་ཡུལ་ཡང་མངོན་སུམ་པར་འགྱུར་བས་ན་ཉེས་པ་མེད་དོ་ཞེ་ན་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། མངོན་སུམ་ནི་རང་དོན་ལ་ལྟ་བའི་ཕྱིར་གལ་ཏེ་མངོན་སུམ་སྤྱི་དང་བྱེ་བྲག་གཉིས་ཀའི་ཡུལ་ཅན་དུ་འགྱུར་ན་ནི། དེ་ལྟ་ན་ཡིད་ཀྱི་འཇུག་པ་ཡང་དེའི་ཡུལ་ཅན་ཉིད་ཀྱི་མངོན་སུམ་དུ་བརྗོད་པར་བྱ་སྟེ། ཡུལ་གཞན་ལ་ཚད་མ་ལ། །ཡུལ་གཞན་ལ་འབྲས་བུ༌[^498]འགྱུར་བ་ནི་མེད་དོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 637]
ཡུལ་གཞན་ལ་མངོན་སུམ་གྱི་ཐ་སྙད་བྱེད་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 638]
དེ་ནས༌[^499]འདི་སྐད་དུ་འབྲེལ་པ་ཅན་མངོན་སུམ་པ་གཅིག་ཅེས་པ་རྣམ་པ་གང་གི་སྒོ་ནས་ཡིན་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 639]
གལ་ཏེ་ནོར་ཉིད་ལ་སོགས་པའོ་ཞེ་ན་མ་ཡིན་ཏེ། དེ་ཉིད་ནོར་ཅན་དང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 640]
ནོར་ནི་ནོར་བདག་དང་འབྲེལ་བ་ཉིད་ཡོད་པས་སོ། །

[Block 641]
ནོར་ཉིད་ལ་སོགས་པའི་རྗེས་སུ༌[^500]འབྱུང་བའི་དྲན་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 642]
གལ་ཏེ་གཞན་ནོ་ཞེ་ན། དེ་ནི་མ་བརྗོད་དོ། །

[Block 643]
གལ་ཏེ་རྟགས་འཛིན་པར་མཚུངས་སོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ནི་འབྲེལ་བ་ཅན་ཉིད་དུ་མི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 644]
རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་པའི་རྟགས་ལ་དུད་པ༌[^501]ལ་སོགས་པ་ཉིད་དུ་བཟུང་ནས་ཕྱིས་དེ་མེ་ལ་སོགས་པ་མེད༌[^502]ན་མི་འབྱུང་བ་ཉིད་དུ་དྲན་པར་བྱེད་དོ། །

[Block 645]
ཇི་སྐད་དུ་བརྗོད་པའི་ནོར་དང་ནོར་ཅན་ལ་སོགས་པའི་འབྲེལ་བ་གཅིག་ལས་ལྷག་པ་གྲུབ་པ་ནི་རྗེས་སུ་དཔག་པའོ་ཞེས་པ་ནི་མི་རིགས་ཏེ། གང་གི་ཕྱིར་ཞེ་ན། དེ་མ་ཤེས་པར་དེ་རྟོགས་ཕྱིར། །ནོར་དང་ནོར་ཅན་ལ་སོགས་པ་མ་ཤེས་པར་མེད་ན་མི་འབྱུང་བ་ཉིད་དམིགས་པ་ལས་ངེས་པའི་ཕྱིར་རོ། །

[Block 646]
འབྲེལ་བ་འཛིན་པ་ནི་རྗེས་སུ་དཔོག་པའི་རྒྱུ་མ་ཡིན་ཏེ། ཤེས་པ་སྔ་མ་ཉིད་དེའི་ཤེས་པར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 647]
ཐམས་ཅད་དུ་ནོར་དང་ནོར་ཅན་ལ་ངེས་པར་ལྟོས་སོ་ཞེས་པའི་མི་འཁྲུལ་བ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་འབྲེལ་བ་ལས་རྗེས་སུ་དཔོགས་སོ། །

[Block 648]
འབྲེལ་བ་དམིགས་ནས་ཡང་མི་འཁྲུལ་བ་ཉིད་ལ་ལྟོས་ཏེ་རྗེས་སུ་དཔོག་པ་ནི་རིགས་པ་མ་ཡིན་ཏེ། དེ་ཉིད་གསལ་བར་བྱེད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 649]
འབྲེལ་བ་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་རྒྱུ་ཉིད་ཡིན་ན་ནི་དེ་ཙམ་གྱི་རྣམ་པས་རྗེས་སུ་དཔག་པར་བྱ་བ་ཤེས་པར་འགྱུར་ཏེ། དེ་ལྟ་མ་ཡིན་ན་རྟགས་ལ་ཤེས་པར་བྱེད་པའི་ནུས་པ་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 650]
འདིར་ཡང་མེས་དུད་པ་རྗེས་སུ་དཔོག་པར་ཐལ་བར་འགྱུར་ཏེ། འབྲེལ་བ་ཁྱད་པར་མེད་པའི་ཕྱིར། །ཁྱད་པར་མེད་པ་ནི་རྒྱུ་མཚན་ཅན་དུ་འབྲེལ་བར་རོ། །

[Block 651]
མེད་ན་མི་འབྱུང་བ་ཉིད་ཀྱི་མེ་དང་དུད་པ་དག་ལ་ནི་འབྲེལ་བའི་སྐྱོན་དེ་ཡོད་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། དེ་ནི་གཉིས་གནས་མིན་ཕྱིར། དུད་པ་ཉིད་ནི་མེ་མེད་ན་མི་འབྱུང་བ་ཡིན་གྱི། མེ་ནི་དུ་བ་མེད་ན་མི་འབྱུང་བ་མ་ཡིན་པས་ཉེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 652]
དེ་ལྟར་ན་རེ་ཞིག་འབྲེལ་བ་དེ་དག་ནི་ཡོད་དུ་ཆུག་ཀྱང་རྒྱུ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 653 [HEADING]]
##### གནོད་བྱ་གནོད་བྱེད་ཀྱི་དངོས་པོ། ^2-5-1-1-0

[Block 654]
གནོད་བྱ་གནོད་བྱེད་ཀྱི་དངོས་པོ་ནི་མ་འབྲེལ་པ་ཉིད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལ་རྟགས་དང་རྟགས་ཅན་མེད། །གང་གནོད་བྱ་གནོད་བྱེད་ནི་སྦྲུལ་དང་ནེའུ་ལེ་ལྟ་བུ་སྟེ། དེ་དག་ལ་ནི་རྟགས་དང་རྟགས་ཅན་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 655]
འདི་ལྟར་སྦྲུལ་རྒྱལ་བ་དང་ནེའུ་ལེ་ཕམ་པ་དག་ལ་ནི་འགལ་བ་མེད་དོ། །

[Block 656]
དེ་བཞིན་དུ་གཞན༌[^503]ཡང་རིག་པར་བྱའོ། །

[Block 657 [HEADING]]
##### རྒྱུ་དང་རྒྱུ་ཅན། ^2-5-1-2-0

[Block 658]
གང་ཡང་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་རྒྱུའི་འབྲེལ་བ་ནི་དེ་དག་ཉིད་དོ་ཞེས་ངེས་པར་བཟུང་བར་བྱེད་པ་དེ་ལ་གང་གི་ཚེ་ཐ་དད་པ་དང་རྗེས་སུ་འགྲོ་བ་ལ་སོགས༌[^504]པ་རྟོགས་པར་བྱེད་པ་དེའི་ཚེ་འབྲེལ་བ་གང་ལས་ཡིན། རྒྱུ་དང་རྒྱུ་ཅན་ནོ་ཞེ་ན། དཔྱད་པར་བྱ་སྟེ། ཅི་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པས་ཡིན་ནམ། འོན་ཏེ་གསལ་བར་བྱ་བ་དང་གསལ་བར་བྱེད་པས་ཡིན་གྲང་། གལ་ཏེ་སྔ་མ་ལྟར་ན་ནི་འདི་ལྟར་རྗེས་འགྲོ་ཡོད་པ་མ་ཡིན་ཏེ། སོ་སོར་མི་བརྗོད་ཐ་དད་ལས། །

[Block 659]
རྒྱུ་ཅན་ནི་ཐ་དད་པ་ཉིད་ཡིན་ལ། རྒྱུ་ནི་གཙོ་བོ་ཡིན་པས་རྗེས་སུ་འགྲོ་བ་ཐ་དད་པ་ལས་སྟོན་པའི་གཏན་ཚིགས་ཉིད་ཀྱི༌[^505]སོ་སོར་བརྗོད་པར་མི་བྱའོ། །

[Block 660]
ཉེས་པ་དེ་ནི་མེད་དོ། །རྗེས་སུ་འགྲོ་བ་གཞན་མིན་ཕྱིར། །

[Block 661]
རྗེས་སུ་འགྲོ་བ་གཞན་ཐ་དད་པ༌[^506]ལས་ནི་མ་ཡིན་ནོ་ཞེ་ན། གལ་ཏེ་གཞན་མིན་རྣམ་ལྔ་མིན། །གལ་ཏེ་རྗེས་སུ་འགྲོ་བ་གཞན་ཐ་དད་ཉིད་ལས་ལྟོས་པར་མི་བརྗོད་ན། རྣམ་པ་ལྔ་རུ་ཐོབ་པར་མི་འགྱུར་ཏེ།

[Block 662 [VERSE]]
དེ་དག་ཐ་མི་དད་པའི་ཕྱིར་རོ། །
གཙོ་བོའི་ཆ་ནས་བརྒྱ་ལམ་ནའང་། །
སྐྱེད་བྱེད་ཉིད་དུ་འགྱུར༌[^507]མ་ཡིན། །
ཐ་དད་ན་ཡང་སྐྱེ་བྱེད༌[^508]མིན། །

[Block 663]
དེ་ལས་ཀུན་ཏུ་འཐོབ་འགྱུར་མིན། །བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པའི་དངོས་པོའི་འབྲེལ་པ་ནི་གཙོ་བོ་ལ་སོགས་པ་ཉིད་ཀྱི་ཆ་ནས་མ་ཡིན་ནོ། །

[Block 664]
ཐ་དད་ནི་ཡོད་པ་ཙམ་ལ་སོགས་པས་ཀྱང་རྟོགས་པར་འགྱུར་རོ། །

[Block 665 [VERSE]]
གཙོ་བོ་ལ་སོགས་ཀྱི་གཅིག་སོགས། །
ཐ་དད་རྣམས་ཀྱི་རྗེས་འགྲོ་ཉིད། །
ལ་སོགས་གང་ལས༌[^509]ཡོངས་སུ་འཛིན། །
དེ་ཡི་ཕྱིར་འདི་གསལ་བྱེད་མིན། །

[Block 666]
གང་གི་ཕྱིར་ཐ་དད་རྣམས་ཀྱི་རྗེས་སུ་འགྲོ་བ་བོར༌[^510]ཚོད་ལ་སོགས་པས་གཙོ་བོ་དང་སྐྱེས་བུ་རྟོགས་པར་བྱེད་པས་ན༌[^511]དེ་ཉིད་གཙུག་ཕུད་ཅན་གྱི་དོན་བསྒྲུབས་པས་ཏེ།[^512] དེའི་ཕྱིར་གཙོ་བོ་ཡོད་པ་ཉིད་ལ་སོགས་པ་རྟོགས་པར་བྱེད་པའི་གཏན་ཚིགས་ཡིན་གྱི། བསྐྱེད༌[^513]བྱ་སྐྱེད་བྱེད་ཀྱི་དངོས་པོ་ནི་མ་ཡིན་ནོ། །

[Block 667]
འདི་ལྟར་གཙོ་བོ་ཡོད་པ་ཉིད་ལ་སོགས་པ་དང་རྗེས་སུ༌[^514]འགྲོ་བ་ལ་སོགས་པ་དེ་རྗེས་སུ་བསྒྲུབས༌[^515]ན་ནི།

[Block 668 [VERSE]]
དེ་བཞིན་ནོར་དང་ནོར་ཅན་ལ། །
མཚོན་ནས་གསལ་བྱེད་མ་ཡིན་ཉིད། །
འབྲེལ་བ་ལས་ཀྱང་དེ་མཚོན་ཕྱིར། །
འབྲེལ་མེད་ཉིད་དུ་ཡང་དག་བརྗོད། །

[Block 669]
འབྲེལ་བ་ཅིག་ཤོས་ལ་ནི་ཆ་འགའ་ཞིག་ལས་རྟགས་དང་རྟགས་ཅན་དུ་འགྱུར་གྱི་གང་ནོར་དང་ནོར་ཅན་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པ་ཐམས་ཅད་དུ་ཕན་ཚུན་གཟུང་བ་དང་འཛིན་པར་འགྱུར་བས་ནའོ། །

[Block 670]
ནོར་ལ་སོགས་པ་ནི་ཆ་གང་གི་སྒོ་ནས་ཀྱང་གསལ་བྱེད་ཉིད་མ་མཐོང་ངོ་། །དེའི་ཕྱིར་འབྲེལ་པ་གཞན་ཉིད་ལས་དོན་བརྗོད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
