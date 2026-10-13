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
[Block 491 [VERSE]]
རྟོགས་བྱ་རྟགས་ཅན་གྱི་བྱེ་བྲག །
མ་ཡིན་དེ་ལ་རྟོགས་པ་པོའི། །
རྟོགས་པ་རབ་ཏུ་འཁྲུལ་པའི་ཕྱིར། །

[Block 492]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 493 [HEADING]]
#### རྟགས་དང་རྟགས་ཅན་འབྲེལ་པ། ^2-1-9-0

[Block 494]
ཅི་སྟེ་འབྲེལ་པ་ནི་ཡང་དག་པར་འཕྲོད་པ་བཞིན་དུ་གཉིས་ཀ་དང་འབྲེལ་པ་ཡིན་པའི་ཕྱིར་རྟགས་ཅན་གྱི་ཆོས་རྟགས་ལ་ཡང་འགྱུར་རོ་ཞེ་ན།

[Block 495 [VERSE]]
དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། །
འབྲེལ་པ་གཉིས་ལ༌[^391]གནས་མོད་ཀྱང་། །
རྟགས་དང་རྟགས་ཅན་སྟོབས༌[^392]གཅིག་པ། །
རྟེན་དང་བརྟེན་པ་བཞིན་ཡིན་གྱི། །

[Block 496]
ཡང་དག་འཕྲོད་པ་བཞིན་མ་ཡིན། །འབྲེལ་པ་གཉིས་ལ་གནས་པར་བདེན་མོད་ཀྱིས་ཀྱང་འབྲེལ་པ་ཙམ་གྱིས༌[^393]རྟེན་དང་བརྟེན་པའི་ཆོས་སུ་འགྱུར་བའམ། བརྟེན་པ་རྟེན་ཅན་གྱི་ཆོས་དང་ཐུན་མོང་དུ་འགྱུར་བ་ནི་གང་ན་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 497]
དེ་བཞིན་དུ་རྟགས་རྟགས་ཅན་དུ་འགྱུར་བའམ་མ་ཡིན་ཏེ། གཞན་དུ་རྟགས་དང༌[^394]རྟགས་ཅན༌[^395]འགྱུར་བ་ནི་གང་ན་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 498]
ཡང་དག་པར་འཕྲོད་པ་ན༌[^396]ཇི་ལྟར་གཅིག་དང་འབྲེལ་པ་དེ་ཁོ་ན་ལྟར་གཉིས་པ་དང་ཡང་སྟེ། དེའི་ཕྱིར་དེ་དང་འདི་ནི་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 499]
འདི་ལྟར།

[Block 500 [VERSE]]
རྟགས་དང༌[^397]རྟགས་ཅན་ཡོད་པ་ཉིད། །
ཅིག་ཤོས་རྟགས་ཅན་ཉིད་ལ་ཡོད། །
རྟགས་དང་རྟགས་ཅན་དག་འབྲེལ་པའི། །
རྗེས་དཔག་བཟློག་ནས་གནས་པ་ཡིན། །

[Block 501]
དེའི་ཕྱིར་ན་རྟགས་ཅན་ནི་རྟགས་ལ་ཡོད་པ་ཉིད་དོ་ཞེས་བརྗོད་དོ། །

[Block 502]
གང་མེ་ཁོ་ན་ལ་ཡོད་པའི་དུ་བའི་རྫས་ཉིད་ལ་སོགས་པ་ཡང་གོ་བར་བྱེད་པ་ཡིན་ལ། གསལ་བ༌[^398]དང་རྣོ་བ་ལ་སོགས་པ་ནི་གོ༌[^399]བ་མ་ཡིན་པའི་ཕྱིར་རྟགས་རྟགས་ཅན་ཉིད་དུ༌[^400]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 503]
དེའི་ཕྱིར་གཞན་དུ་ནི་རིགས་པ་མ་ཡིན་པས་གང་དུ་བ་ཉིད་བཞིན་དུ་བའི་སྐྱ་བོ་ལ་སོགས་པ་ཡང་གོ་བར་བྱེད་པ་མིན་ཞིང་རྫས་ཉིད་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 504]
དེ་ལྟར་རྟགས་དང་རྟགས་ཅན་དུ་འབྲེལ་བའི་ངེས་པར་བཟུང་བ་ནི་ཕྱིན་ཅི་ལོག་ཏུ་གནས་པ་ཡིན་ནོ། །

[Block 505 [HEADING]]
#### རྟགས་ཀྱི་ཁྱབ་པ། ^2-1-10-0

[Block 506]
ཅི་སྟེ་ཡང་རྟགས་ཡིན་ཡང་རྟགས་ཅན་དུ་འགྱུར་བ་ནི་དཔེར་ན་བྱས་པ་ཉིད་དང་མི་རྟག་པ་ཉིད་ལྟ་བུ་ཞེ་ན།

[Block 507 [VERSE]]
རྟགས་ཀྱི་ཁྱབ་པའང་འདོད་པ་སྟེ། །
དེ་ཡི་ཆ་ནས་རྟགས་ཅན་ཡིན། །
ཁྱབ་བྱེད་ཆ་ནས་དེ༌[^401]གོ་བྱེད། །
མ་ཡིན་བ་ལང༌[^402]རྭ་ཅན༌[^403]བཞིན། །

[Block 508]
གང་ཅུང་ཟད་ཙམ་ནས༌[^404]རྟགས་རྟགས་ཅན་དུ༌[^405]འགྱུར་བ་ནི་ཡོད་མོད་ཀྱིས་ཀྱང་། དེས་དེ་ལ་ཁྱབ་པའི་ཚུལ་གྱིས་རྟགས་ཀྱི༌[^406]ཡན་ལག་ཏུ་འགྲོ་བ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་རྭ་ཅན་ཉིད་ཀྱིས་བ་ལང་ལ་ཁྱབ་ཀྱང་དེས་བ་ལང་གོ་བར་བྱེད་པ་ནི་མ་ཡིན་གྱི་ཁྱབ་བྱེད་དེ་ཉིད་བ་ལང་གིས་གོ་བར་བྱེད་པ་བཞིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 509 [VERSE]]
སོ་སོར་བཀག་པའི་མི་འཁྲུལ་བ། །
གང་ཕྱིར་འབྲེལ་པ་ལ་ལྟོས་ཡིན། །
དེ༌[^407]ཕྱིར་རྟགས་ཀྱི༌[^408]རྟགས་ཅན་ལ། །
ཁྱད་པ༌[^409]བདེན་ཡང་བྱེད་པོ་མིན། །

[Block 510]
བྱས་པས་མི་རྟག་པ་ལ་ཁྱབ་ཏུ་ཟིན་ཀྱང་རྟག་པ་ཉིད་བཀག་ནས་གོ་བར་བྱེད་པ་དེ་བཞིན་དུ་མི་རྟག་པས་བྱས་པ་ལ་ཁྱབ་པ་ཉིད་ཀྱིས་ཀྱང་མ་བྱས་པ་བཀག་ནས་གོ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 511]
དེའི་ཕྱིར་མི་རྟག་པའི་དོན་ལ་བྱས་པ་ཉིད་ཀྱིས་ཁྱབ་པ་ཉིད་ཀྱིས་མ་བྱས་པའི་གོ་སྐབས་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པས་བྱས་པ་ལ་མ་བྱས་པ་བཀག་ནས་གོ་བར་བྱ་བ་ཉིད་དུ་འགྱུར་གྱི་གོ་བར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 512]
ཡང་བརྗོད་པ།

[Block 513 [VERSE]]
བྱས་པ་ཉིད་ཀྱིས་འཇིག་པ་ལ། །
ཁྱབ་ཀྱིས་མ་བྱས་པ་ཡིས་མིན། །
རྟག་པ་མེད་ལ་ཁྱབ་པའི་ཕྱིར། །
མ་ཁྱབ་པ་ཡིས༌[^410]དོན་གྱིས་སྟོན། །

[Block 514 [VERSE]]
རྭ་ཅན་ཉིད་ཀྱིས་བ་ལང་ལ། །
ཁྱབ་པར་རྭ་ཅན་མིན་པ་བཟློག །
གླང་ལ་རྭ་ཅན་གྱིས་ཁྱབ་བཞིན། །
བ་ལང་གི་དོན་ཟློག༌[^411]བྱེད་མིན། །

[Block 515]
ཞེས་བྱ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 516]
རང་གི་དོན་གྱི་རྗེས་སུ་དཔག་པ་ངེས་པར་བསྟན་ཏོ། །

[Block 517 [HEADING]]
### རྩོད་པ་སྒྲུབ་པ། ^2-2-0

[Block 518]
རྩོད་པ་སྒྲུབ་པ་ནས་ནི་མེད་ན་མི་འབྱུང་བའི་དོན་མཐོང་བ་དེ་རིག་པ༌[^412]རྗེས་སུ་དཔག་པའོ་ཞེས་བརྗོད་དོ། །

[Block 519]
དེ་ལ།

[Block 520 [VERSE]]
མེད་ན་མི་འབྱུང་བ་མཐོང་བའི། །
རང་གི་རྣམ་པ་ཙམ་མཐོང་ན། །
གལ་ཏེ་མེད་ན་མི་འབྱུང་བའི། །

[Block 521]
མེད་ན་མི་འབྱུང་བ་དེ་འབའ་ཞིག་ཙམ་མཐོང་བར་འདོད་པ་ཡིན་ན་ནི་དེ། རིག་ཅེས་མི་བརྗོད། ཅེས་བྱ་བ་ནི་འདིར་ཕྱིས་བཅུག་པའོ། །

[Block 522]
ཅི་སྟེ་ཡང་དེ་རིག་ཅེས་བྱ་བ༌[^413]འདིས། གཞན་ཉིད་དུ། བརྗོད་ན་ནི་ལྟ་བུར་གང་ལ། གལ་ཏེ་མེད་ན་མི་འབྱུང་བའི་དོན་གཞན་དུ་མཐོང་བར་འདོད་པ༌[^414]ལྟ་ན་ནི། འདི་མཐོང་ཞེས་ཇི་ལྟར་བརྗོད་པར་བྱ། གང་ལ་དོན་ནི༌[^415]བསྒྲུབ་བྱ་ལ་ཞེ་ན། ཅི་སྟེ་ཡང་ལྷག་མ་དོན་ཞེས་པས་བསྒྲུབ་བྱའི་སྐབས་སུ་བབ་པས་ན་དོན་གང་བསྒྲུབ་པར་བྱ་བ་ལ་མཐོང་བ་དེ་རྗེས་སུ་དཔག་པ་སྟེ། མེད་པ་མི་འབྱུང་བ་ཉིད་རིག་པའོ་ཞེས་འདོད་པ་ཡིན་ན་ནི་དེ་ལྟ་ན། མེད་ན་མི་འབྱུང་ཞེས་ཅི་དགོས། །འདི་ལྟར་སྔར་མེད་ན་མི་འབྱུང་བ་སྨོས་པས་ཕྱིས་ཀྱང་ཡོད་པ་ཉིད་དེ། མེད་ན་མི་འབྱུང་བ་ཉིད་ནི་དོན་མཐོང་ཞེས་པས་རིག༌[^416]ཅིང་དེ་རྗེས་སུ་དཔག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 523]
དུད་སོགས་མེ་སོགས་ལ་མཐོང་ལས། །

[Block 524]
གཞན་པའི་དཔག་བྱ་དེ་རིག་གང་། རྗེས་སུ་དཔག་པ་ཉིད་དཔེར་བརྗོད་པའི་མེ་ལ་སོགས་པ་ལ་དུ་བ་ལ་སོགས་པ་མཐོང་བ་ལས་གཞན་པའི་དཔག་པར་བྱ་བའི་དོན་གང་མེད་ན་མི་འབྱུང་བས༌[^417]དེ་རིག་ཅེས་ཇི་ལྟར་རྗོད་པར་བྱེད།

[Block 525]
ཆོས་དོན་དུ་མ་ཡོད་པ་ལ། །དེ་རིག་པ་ཞེས་ཇི་ལྟར་བརྗོད། །

[Block 526]
ཆོས་ཀྱི་དོན་དུ་མ་ཡོད་པ་ལ་དུ་བས་གོ་བར་བྱ་བའི་ཆ༌[^418]ནི་གང་ཡིན། དུ་བ་ཡང་གང་གི་ཆ་ནས་གསལ་བར་བྱེད་ཅེས་ནི་མ་བསྟན་ཏོ། །

[Block 527 [HEADING]]
### རིགས་པ་ཅན། ^2-3-0

[Block 528]
རིགས་པ་ཅན་རྣམས་ན་རེ་དེ་སྔོན་དུ་སོང་བ་ཅན་གྱི་རྗེས་སུ་དཔག་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྔ་མ་དང་ལྡན་པ༌[^419]དང་། ལྷག་མ་དང་ལྡན་པ་དང་། སྤྱིར་མཐོང་བ་ཅན་ནོ་ཞེས་ཟེར་རོ། །

[Block 529 [HEADING]]
#### མངོན་སུམ་སྔོན་དུ་འགྲོ་བ། ^2-3-1-0

[Block 530]
དེ་ལ་རེ་ཞིག་མངོན་སུམ་སྔོན་དུ་འགྲོ་བ་ནི་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། འབྲེལ་པ་དབང་པོའི་གཟུང་བྱ་མིན། །རྟགས་དང་རྟགས་ཅན་གྱི་འབྲེལ་པ་ནི་དབང་པོའི་ཤེས་པའི་ཡུལ་ཡང་མ་ཡིན་ལ་རྟགས་དང་རྟགས་ཅན་མངོན་སུམ་པའང་མ་ཡིན་ན་དེ་མངོན༌[^420]དུ་སོང་བ་ཅན་ནི་རྗེས་སུ་དཔག་པའོ་ཞེས་གང་གིས་འགྱུར། ཇི་ལྟར་ན་རྗོད་པར་བྱེད། སྔ་མ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ལ་སྔ་མ་དང་མཚུངས་པས་ན་སྔ་མ་ལྟ་བུའོ་ཞེས་ལྟ་བུའི་སྒྲར་འགྱུར་བའམ། འདི་ལ་སྔ་མའི་ཆོས་ཡོད་པས་ན་དེ་དང་ལྡན་པའོ་ཞེས་ལྡན་པའི་སྒྲར་འགྱུར་གྲང་ན། དེ་ལས་ཅིར་འགྱུར། ཐམས་ཅད་སྲིད་ཕྱིར་ལྟ་བུར་མིན། །ཐམས་ཅད་ཅེས་བྱ་བ་ནི་རྗེས་སུ་དཔག་པས་འབྲེལ་པ་འཛིན་པ་ཉམས་སུ་མྱོང་བ་བཞིན་དུ་ཕྱིས་ཀྱང་རྟགས་ཀྱིས༌[^421]རྗེས་སུ་དཔག་པར་བྱ་བ་འཛིན་པར་བྱེད་དོ། །
--- END BLOCKS ---
