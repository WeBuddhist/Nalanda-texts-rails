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
[Block 596]
འདུ་བ་ཡོད་དུ་ཟིན་ཀྱང་རྟོགས་པ་ནི་མེད་ན་མི་འབྱུང་བ་ཉིད་དམིགས་པ་ཁོ་ན་ལས་ཡིན་པའི་ཕྱིར། དེ་ཁོ་ན་རྒྱུ་ཡིན་ནོ། །

[Block 597 [HEADING]]
#### དོན་གཅིག་ལ་འདུ་བ། ^2-4-3-0

[Block 598]
དོན་གཅིག་ལ་འདུ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། འབྲས་བུ་དང་འབྲས་བུ་གཞན་དང་། རྒྱུ་དང་རྒྱུ་གཞན་ནོ། །

[Block 599]
དེར་ཡང་དཔེར་ན་གཟུགས༌[^466]རེག་བྱ་ལྟ་བུ་དང་ལག་པ་དང་། རྐང་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 600]
འདི་ལ་ཡང་དེ་ཉིད་བརྗོད་པར་བྱའོ། །

[Block 601]
འབྲེལ་པ་ཡོད་དུ་ཟིན་ཀྱང་རྒྱུར་ནི་ཁོང་དུ་ཆུད་མི་འགྱུར། དོན་གཅིག་ལ་འདུ་བ་ནི་གང་དུ་ཡང་མངོན་སུམ་དུ་མ་གྱུར་ཏོ། །

[Block 602]
དོན་གཅིག་ལ་འདུ་བ་གཉིས་ཡོད་དུ་ཟིན་ཀྱང་རྟོགས་པ་ནི་མེད་ན༌[^467]མི་འབྱུང་བ་ཁོ་ན་ལས་མཐོང་བ་ཡིན་ནོ། །

[Block 603]
འདིར༌[^468]ཡང་གཟུགས་ཀྱིས་རེག་བྱ་བཞིན། །རེག་བྱས་ཀྱང་གཟུགས་གསལ་བར་བྱེད་པར་འགྱུར་ཏེ། འབྲེལ་པ་ཁྱད་པར་མེད་པའི་ཕྱིར། དོན་གཅིག་ལ་འདུ་བ་ཉིད་ལ་ནི་ཁྱད་པར་ཡོད་པ་མ་ཡིན་པས་གཅིག་ལས་འཁྲུལ་པར་བརྗོད་པ་བཞིན་དུ་འབྲེལ་པ་ལས་ཀྱང་རྒྱུ་མ་ཡིན་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 604]
གང་དོན་གཅིག་ལ་འདུ་བ་ནི་གཉིས་ཁོ་ནའོ་ཞེས་བརྗོད་པ་དེ་ལ།

[Block 605]
གཞན་ཡང་སྲིད་ཕྱིར་གཉིས་མ་ཡིན། །རྒྱུ་ཡང་རྒྱུ་དང་འབྲས་བུ་ལས། །

[Block 606]
འབྲས་བུའི་དོན་གཅིག་ལ་འདུ་བའི་རྟོགས་པ་ནི་མཐོང་བ་ཉིད་དེ། དཔེར་ན་མ་གྱུར་པ་ཞེས་བྱ་བ་དང་། མ་གྱུར་པ་ལས་ཞེས་བརྗོད་པ་ལྟ་བུའོ། །

[Block 607]
དེའི་ཕྱིར་དོན་གཅིག་ལ་འདུ་བ་ནི་རྣམ་པ་གཉིས་ཉིད་དོ་ཞེས་ངེས་པར་བཟུང་བ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 608 [HEADING]]
#### འགལ་བ། ^2-4-4-0

[Block 609]
འགལ་བ་ནི་རྣམ་པ་བཞི་སྟེ། མངོན་སུམ༌[^469]དུ་གྱུར་པ་ལས་མ་གྱུར་པའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ་ཞེས་པ་འདི༌[^470]ཡང་ཐམས་ཅད་དུ། གང་ཞིག་འགལ་བ་དེ༌[^471]རྟགས་ཡིན།[^472] །སྤྲིན་དང་རླུང་གི་སྦྱོར་བ་དང་ཆར་འབབ་པ་ནི་འགལ་ལ་རག་ན་འདིར་ཆར་འབབ་པ་ནི་གཏན་ཚིགས་མ་ཡིན་གྱི་འོན་ཀྱང་དེ་མེད་པ་ཡིན་ནོ། །

[Block 610]
ཆར་མི་འབབ་པ་དང་སྤྲིན་དང་རླུང་གི་སྦྱོར་བ་ནི་འགལ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 611]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 612]
གལ་ཏེ་རྟགས་ནི་རྟོགས་པ་སྔོན་དུ༌[^473]འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར་མངོན་དུ་མ་གྱུར་པ་ལ་སོགས་པའི་རྟོགས་པ་གཏན་ཚིགས་མ༌[^474]ཡིན་ནོ་ཞེས་བརྗོད་དོ་ཞེ་ན། དེ་ནི་རྟགས་མ་ཡིན་ཏེ། འབྲེལ་པ་མེད་ཕྱིར་རྟགས་བློ་མིན། །རྟགས་ཀྱི་བློ་ལ་ནི་རྟགས་ཅན་དང་འབྲེལ་པ་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 613]
ཧ་ཅང་ཐལ་བར་འགྱུར་བས་ན་འབྲེལ་པའི་དོན་དུ་མདོ་ལས་འདི་ནི་འདིའི་ཞེས་སྨོས་སོ། །

[Block 614]
འདི་ནི་རྟགས་ཉིད་དུ་རིགས་པ་མ་ཡིན་ནོ།[^475] །

[Block 615]
ཅིའི་ཕྱིར་ཞེ་ན། རྟགས་ལས་བྱུང་བའི༌[^476]བསྟན་པའི་ཕྱིར། །དཔག་པར་བྱ་བའི་ཤེས་པ་ཡང་འབྲས་བུར་མི་འགྱུར་ཞིང་རྟགས་བརྗོད་པའི་དྲན་པ་ཙམ་ལས་ཀྱང་ཁོང་དུ་ཆུད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 616]
དེའི་ཕྱིར་ཞེས་བྱ་བ་ལས་བསྟན་པས་ན་དྲན་པ་ལ་ལྟོས་པའི་རྟགས་ཀྱི་ཤེས་པ་ཉིད་ཀྱི་རྟགས་ལས་བྱུང་བའོ་ཞེས་ཡིན་གྱི་དེ་རྟགས་ནི་མ་ཡིན་ནོ། །

[Block 617]
གལ་ཏེ་རྒྱུར་བྱས་ནས་རྟགས་སུ་བརྗོད་པ་སྟེ། འདི་ལྟར་དེའི་རྒྱུའི་བྱེ་བྲག་ལ་རྟགས་ཀྱི་སྒྲ༌[^477]མང་དུ་བྱས་ནས་དེ་ལྟར་བརྗོད་པར་བས་སོ་ཞེ་ན། དེ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདིར། ཐམས་ཅད་རྟགས་སུ་བརྗོད་མ་ཡིན། །འདིར་བྱེད་པ་པོ་དང་ཐམས་ཅད་ནི་རྟགས་མ་ཡིན་ཏེ། འདི་ལྟར་རྗེས་སུ་དཔག་པ་ནི་དེ་བརྗོད་པ་ལས་ཀྱང་འབྱུང་ངོ་། །དེ་ལྟ་མ་ཡིན་ན་འདིར་བདག་དང་ཕྲད་པ་ལ་སོགས་པ་ཡང་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 618]
རྟགས་ཀྱི་ཤེས་པ་རྗེས༌[^478]དཔག་གི་དངོས་ཀྱི་རྒྱུ་ནི་མ་ཡིན་ཏེ་དྲན་པས་བར་དུ་ཆོད་པའི༌[^479]ཕྱིར་རོ། །

[Block 619]
དེས་ན་དངོས་ཀྱི་རྒྱུ་ཉིད་དུ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 620]
གང་ཡང་རྟགས་ནི་རྟོགས་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར་ཞེས་གང་བརྗོད་པ་དེ་ལ་གང་གི་ཕྱིར། དྲན་པ་འབྲེལ་པ་ཅན་དུ་འགྲུབ། །འབྲེལ་པ་ཅན་གྱི་རྟོགས་པས༌[^480]ནི་གྲུབ་པ་མ་ཡིན་ནོ།[^481] །

[Block 621]
དེ་སྐད་དུ་ཡང་གང་གི་ཕྱིར། །མ་གྲུབ་པའི་རྟགས་མ་ཡིན་ནོ་ཞེས༌[^482]བཤད་པར་བྱའོ། །

[Block 622]
གལ་ཏེ་འབྲེལ་པ་གཅིག་ཉིད་ལས་རྗེས་དཔག་གི་རྒྱུར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟར་ནི་བསྟན་བཅོས་ནས་བརྗོད་པ་ཉིད་དེ། འབྲས་བུ་ལ་སོགས་མདོར་མ་མཚོན། །གང་དག༌[^483]བསྟན་བཅོས་སུ་རྒྱུ་ཉིད་དང་། འབྲས་བུ་ཉིད་དང་། རྣམ་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་ཞེས་པ་དང་། དེ་བཞིན་དུ་ཡོད་པ་ལ་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་ཞེས་པ་མི་རྟག་པ་ཉིད་དང་རྟག་པ་ཉིད་ཀྱི་རྟགས་སུ་བརྗོད་ཀྱི། མདོར་མཚོན་པ་ནི་མ་ཡིན་ནོ། །

[Block 623]
དེ་དག་རྣམས་ལས་གང་ཡང་རུང་བ་ཅིག་འབྲས་བུ་ལ་སོགས་པ༌[^484]སྲིད་པ་ནི་མ་ཡིན་ནོ། །

[Block 624]
ཇི་ལྟར་མི་སྲིད་དེ་འདི་གང་གསལ་བར་བྱ་བ་དང་གསལ་བར་བྱེད་པ༌[^485]གྲུབ་པ་དེ་ཉིད་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོའོ་ཞེ་ན། གང་འདི་ལྟར་གསལ་བར་བྱེད་པ་ཙམ་རྒྱུར་འདོད་པ་དེའི་ལྟར་ན་ནི། ཐ་མ་གསལ་བྱེད་དུ་མི་འགྱུར། །རྒྱུ་རྣམས་ཀྱི་ཐ་མ་ལྡན་པ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་གསལ་བྱེད་དུ་མི་འགྱུར་ཏེ། རྒྱུ་ལས་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 625]
གཞན་ཡང་། དོན་མེད་གཞན་ལས་ཀྱང་དེ་གྲུབ། །འབྲེལ་པ་གཞན་གྱིས་ཀྱང་དོན་ཁོང་དུ་ཆུད་པར་བྱེད་དོ། །

[Block 626]
[^486]གང་གི་ཕྱིར་འདི་འདིའི་གསལ་བར་བྱེད་པའོ་ཞེས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་རྟོགས་པར་བྱེད་པ་དེའི་རྗེས་སུ་དཔོག་པའི་རྒྱུ་འདི་དོན་མེད་པ་ཉིད་དོ། །

[Block 627]
དེ་ལྟ་བས་ན་རེ་ཞིག་བྱེ་བྲག་པའི་རྗེས་སུ་དཔག་པ་ནི་སྒྲུབ་པར་དཀའོ། །

[Block 628 [HEADING]]
### གྲངས་ཅན་པ། ^2-5-0

[Block 629]
གྲངས་ཅན་པ་རྣམས་ནི་རེ་ཞིག་འབྲེལ་བ་མངོན་སུམ་པ་གཅིག་ལས་ལྷག་པར་གྲུབ་པ་ནི་རྗེས་སུ་དཔག་པའོ་ཞེས་ཟེར་རོ། །

[Block 630 [HEADING]]
#### འབྲེལ་བ་རྣམ་པ་བདུན། ^2-5-1-0

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
--- END BLOCKS ---
