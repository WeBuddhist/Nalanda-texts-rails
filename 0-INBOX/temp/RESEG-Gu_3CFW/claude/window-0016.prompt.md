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
[Block 561]
འདི་ལ་བསྙེན་པར་མ་རྫོགས་པ་ནི་ཐམས་ཅད་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སོ་སོར༌[^501]སྐལ་བའི་ཆ་འོས་པ་ཉིད་ཡིན་པའོ། །

[Block 562]
འདི་ཡང་འདི་ལ་སུམ་ཆ་འབྲི་བ་ལྟ་བུ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 563]
ནད་པས་སྨྲས་པས་བྱིན་པ་ཕྲི་བ་ཡང་ཇི་སྐད་སྨྲས་པ་བཞིན་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། ནད་པས་སྦྱིན་པ་སྨྲས་པ་ལ་གང་དེ་ལ་སྨྲས་པ་དེ་དེས་ཕྲི་བར་གྱུར་ཀྱང་ཇི་ལྟར་དེས་དེ༌[^502]ལ་སྨྲས་པ་དེ་ལྟར་ཁོ་ན་བཞིན་བྱ་དགོས་པར་རིག་པར་བྱའོ། །

[Block 564]
འདིར་གཞུང་ནི། འདུལ་བྱེད་དག་ལས་སྔར་ནད་པས་སྦྱིན་པ་དེ་བདག་ཉིད་ཤི་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། དེ་ལྟ་བས་ན་འདི་ལ་མི་སྦྱིན་པ་མ་ཡིན་ནོ། །

[Block 565]
ནད་གཡོག་གིས་ཕྱིར་ཕྲི་ཡང་གང་ཞིག་དེས་སྨྲས་པ། གཞན་གྱི་ཕྱིར་ཡང་འདི་ལ་བྱེ་བྲག་མེད་པས་རྣམ་པར་གཞག་པའོ་ཞེས་གསུངས་པ་ཙམ་བསྡུས་པ་ཞེས་བྱ་བའོ། །

[Block 566]
ཤི་བ་ཉིད་ཀྱི་དུས་ན་རྫས་ཉིད་བསྒྲུབ་པ་ལ་ནི་ནོར་བདག་མི་དབང་ངོ་ཞེས་བྱ་བ་ནི་རང་ཤི་བ་ཉིད་ཀྱི༌[^503]དུས་ན་གནས་ལ༌[^504]རང་གི་དངོས་པོ་བསྒྲུབ་པ༌[^505]ལ་གལ་ཏེ་བདག་ཤི་བར་གྱུར་ན་ཆེ་གེ་མོ་ཞིག་ལ་བདག་གི་རྫས་འདི་སྦྱིན་པར་བྱའོ་སྙམ་དུ་འདིར་བུ་ལོན་པ་རབ་ཏུ་བྱུང་བ་མི་དབང་བ་མེད་དོ། །

[Block 567]
རབ་ཏུ་བྱུང་བ་རྣམས་ལ་འདིར་དེ་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 568]
ཁྱིམ་ན་གནས་པ་ནི་དབང་ངོ་ཞེས་བྱ་བ་ནི། བུ་ལོན་པ་ཁྱིམ་ན་དབང་བ་ལ་ཤི་བའི་དུས་ན་རང་ཉིད་བསྒྲུབ་པའི་ཕྱིར་དེ་དབང་བའོ། །

[Block 569]
འདིར་གཞུང་ནི།

[Block 570]
ཕྲན་ཚེགས་དག་ལས།

[Block 571]
ཁྱིམ་བདག་ནི་ལྟོས་པ་དང་བཅས་པས་དུས་བྱེད་ལ། རབ་ཏུ་བྱུང་བ་དག་ནི་ལྟོས་པ་མེད་པར་དུས་བྱེད་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ཁྱིམ་བདག་ནི་ལྟོས་པ་དང་བཅས་པའི་ཕྱིར་དབང་ལ། རབ་ཏུ་བྱུང་བ་ནི་ལྟོས་པ་མེད་པའི་ཕྱིར་མི་དབང་ངོ་ཞེས་གསུངས་པ་དེ་བསྒྲུབ་པོ། །ཁྱིམ་པས་བུ་དང་ཆུང་མ་ཕུལ་ནས་ཤི་ན་ཅི་བདེ༌[^506]བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པས་དགེ་འདུན་ལ་བུ་དང་ཆུང་མ་ཕུལ་ནས་ཁྱིམ་པ་ཉིད་ཤི་ན། དེའི་བུ་དང་ཆུང་མ་དག་ཅི་བདེར་བྱས་ཏེ། བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 572]
གླང་པོ་ཆེ་དང་རྟ་དང་། བོང་བུ་དང་དྲེའུ་དང༌[^507]གོ་ཆ་རྣམས་ནི་རྒྱལ་པོ་ལ་དབུལ་ལོ། །

[Block 573]
དབྱིག་དང་གསེར་དང་གཞན་བྱས་པ་དང་མ་བྱས་པ་རྣམས་ནི་གསུམ་ལའོ་ཞེས་བྱ་བ་ནི་དབུལ་ལོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དབྱིག་དང་གསེར་དང༌[^508]དེ་དག་ལས་གཞན་པ་ནི་ཟངས་ཀྱི༌[^509]རང་བཞིན་ལ་སོགས་པ་བརྡུངས་སུ་བྱས་པ་དང་མ་བྱས་པ་རྣམས་ནི་དཀོན་མཆོག་གསུམ་ལ་དབུལ་ལོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 574]
རིན་པོ་ཆེ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ནོར་བུ་དང་བཻ་ཌཱུརྱ་དང་གཡས་སུ་འཁྱིལ་པ༌[^510]ལ་སོགས་པ་རྣམས་ཀྱང་དཀོན་མཆོག་གསུམ་ལ་དབུལ་ལོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^511]པའི་ཕྱིར་ཡང་གི་སྒྲའོ། །

[Block 575]
མུ་ཏིག་རྣམས་ནི་གཞན་ཡོད་ན་དེའི་སྐལ་བས་སམ་ལྷག་པ་ཡིན་ཡང་རུང་ངོ་། །གལ་ཏེ་མེད་ན་དེ་བཞིན་དུ་སངས་རྒྱས་ལའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མུ་ཏིག་ལས༌[^512]གཞན་པའི་རིན་པོ་ཆེ་ཡོད་ན་དཀོན་མཆོག་དག་ལས་སངས་རྒྱས་དེའི་སྐལ་བས་མུ་ཏིག་རྣམས་བརྗེས༌[^513]ཏེ། སངས་རྒྱས་ལ་དབུལ་བར་བྱའོ། །

[Block 576]
གལ་ཏེ་དཀོན་མཆོག་སུམ༌[^514]ཆར་གྱི་སྐུ་སྐལ་ལས་ལྷག་པ་ཉིད་ཡིན་ན། དེ་ལྟར་ཡང་དེ་དག་ཐམས་ཅད་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་དབུལ་བར་བྱའོ། །

[Block 577]
གལ་ཏེ་མུ་ཏིག་རྣམས་ལས་གཞན་པའི་རིན་པོ་ཆེ་མེད་ན་དེ་བཞིན་དུ་སྐྱིན་པ༌[^515]མེད༌[^516]ཀྱང་བླ་སྟེ། ཇི་སྲིད་དུ་སངས་རྒྱས་ཉག་གཅིག་ལ་དབུལ་བར་བགྱིའོ། །

[Block 578]
ཚོན་རྩི་ཆེན་པོ་རྣམས་ཀྱང་ངོ་ཞེས༌[^517]བྱ་བ་ནི། གང་གུས་དང་མཚལ་དང་མཐིང་ཤུན་དང་ལ་སོགས་པ་ཡང་སངས་རྒྱས་ལ་དབུལ་ལོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^518]པའི་ཕྱིར་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 579]
དེ་དག་ནི་བཏགས་ཏེ་དྲི་གཙང་ཁང་གི་ཞལ་ཞལ་དུ་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཅེས༌[^519]བྱ་བ་ལ་དེ་དག༌[^520]ནི་མུ་ཏིག་རྣམས་སོ། །

[Block 580]
དེ་མ་ཡིན་པ་སངས་རྒྱས་ཀྱི་ནི་སྐུ་གཟུགས་དང་། དྲི་གཙང་ཁང་དང་མཆོད་རྟེན་གྱི་ཡོ་བྱད་དུ་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་མུ་ཏིག་དེ་ལས་གཞན་པ་རྣམས་སོ། །

[Block 581]
ཆོས་ཀྱི་ནི་སངས་རྒྱས་ཀྱི་བཀའ་ཞེས༌[^521]བྲི་བ་དང་སེང་གེའི་ཁྲི་དག་གིའོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་དུའོ༌[^522]ཞེས་བྱ་བར༌[^523]སྦྱར་ཏེ་དབུལ་བའོ། །

[Block 582]
ཐེག་པ་ནི་སྐུ་གཟུགས་ལའོ་ཞེས་བྱ་བ་ནི། རྒྱལ་མཚན་དེའི་སྲོག་ཤིང་དག་ནི་རྒྱལ་མཚན་གྱི་དོན་དུའོ་ཞེས་བྱ་བ་ནི། རྒྱལ་མཚན་གྱི་དོན་དུ་དབུལ་ལོ། །

[Block 583]
དེ༌[^524]རུང་བའི་སྲོག་ཤིང་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། སྐུ་གཟུགས་ལ་དབུལ་ལོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^525]པའི་ཕྱིར། ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 584]
གཞན་དག་དང་མཚོན་ཆ་རྣམས་ནི་དགེ་འདུན་ལའོ་ཞེས་བྱ་བ་ནི་དབུལ་ལོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 585]
གཞན་དག་དང་ཞེས་བྱ་བ་ནི།

[Block 586]
རྒྱལ་མཚན་གྱི་སྲོག་ཤིང་དུ་རུང་བ་ལས།

[Block 587]
འདི་ལྟ་སྟེ་ཐུང་ངུ་དག་ལའོ། །

[Block 588]
དེ་དག་ནི་ཁར་གསིལ༌[^526]གྱི་ཡུ་བ་དང་ཁབ་དང་གྲི་གུར་བྱས་ཏེ་བྲིམ་མོ་ཞེས་བྱ་བ་ལ། དེ་བདག༌[^527]ཅེས་བྱ་བ་ནི་སྲོག་ཤིང་ལ་སོགས་པ་རྣམས་སོ། །

[Block 589]
ཇི་ལྟར་རིགས་པ་དེ་རྣམས་ནི་ཡོ་བྱད་དུ་བྱ་བར་རིག་པར་བྱའོ། །

[Block 590]
སྲོག་ཤིང་གཞན་དེ་དག་ནི་ཁར་གསིལ༌[^528]གྱི་ཡུ་བར་བྱའོ། །

[Block 591]
མཚོན་ཆ་རྣམས་ནི་ཁབ་དང་གྲི་གུར་བྱས་ཏེ་དགེ་འདུན་ལ་བྲིམ་མོ། །

[Block 592]
དགེ་འདུན་གྱི་གཞན་རྣམས་ནི་གཞག་པ་དང་བགོ་བ་དང་བཟའ་བ་དག་ཏུ་ཅི་རིགས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་ནི་ཞེས་བྱ་བ་ནི་སྲོག་ཤིང་ལ་སོགས་པ་སྨོས་པའི་ཡོ་བྱད་ཀྱིས་སོ། །

[Block 593]
ཞིང་དང་ཁང་ཁྱིམ་དང་ཚོང་ཁང་དང་། གནས་མལ་དང་མགར་སྤྱད་དང་། གསེར་མགར་གྱི་ལག་ཆ་དང་། འདྲེག་མཁན་གྱི་ལག་ཆ་དང་། རྫ་མཁན་གྱི་ལག་ཆ་དང་། ཤིང་མཁན་གྱི་ལག་ཆ་དང་། བསིལ་ཡབ་མཁན་གྱི་ལག་ཆ་དང་། བྲན་དང་བྲན་མོ་དང་། ལས་བྱེད་པ་དང་ཞོ་ཤས་འཚོ་བ་དང་། བ་གླང༌[^529]དང་མ་ཧེ་དང་། ར་དང་ལུག་དང་སྨན་དང་། སངས་རྒྱས་ཀྱི་བསྟན་བཅོས་ཀྱི་གླེགས་བམ་དང་། མྱུར་དུ་མི་གྲུབ་པའི་དམ་རྒྱ་དག་ནི། དང་པོར་འོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་མྱུར་དུ་མི་གྲུབ་པའི་ཞེས་བྱ་བ་ནི། བྲི་བར་བྱ་བ་གང་ཡིན་པ་དང་། གང་དུ་བྲི་བར་བྱ་བ་མྱུར་དུ་འགྲུབ་པར་མི་ནུས་པའོ། །

[Block 594]
དང་པོར་འོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཞག་པར་འོས་པ་ཡིན་ནོ། །

[Block 595]
རས་དང་རས་ཡུག་ཆེན་པོ་དང་བེའུ་རས་དང་། མཆིལ་ལྷམ་དང་། ལྷམ་སྒྲོག་གུ་ཅན་དང་། འབྲུ་མར་དང་འབྲུ་མར་གྱི༌[^530]སྣོད་དང་། བྱ་མ་བུམ་དང་རིལ་བ་སྤྱི་བླུགས་དང་། གླེགས་བམ་གཞན་དང་དམ་རྒྱ་གཞན་དང་། ཚོན༌[^531]རྩི་གཞན་དག་ནི་གཉིས་པར་འོས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བྱ་མ་བུམ་ཞེས་བྱ་བ་ནི་རྫ་མཁན་གྱི་སྣོད་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 596]
གཞན་དང་ཞེས་བྱ་བ་ལ། གཞན་གྱི་སྒྲས་ནི་གླེགས་བམ་ལ་སོགས་པ་གསུམ་པོ་རྣམས་དང་འབྲེལ་པའོ། །

[Block 597]
སངས་རྒྱས་ཀྱི་བསྟན་བཅོས་ཀྱི་གླེགས་བམ་མྱུར་བར་འབྲི་བ༌[^532]མ་ཡིན་པ་ཚོན་ཆེན་པོ་རྣམས་ལས་གླེགས་བམ་ལ་སོགས་པ། གཞན་རྣམས་ནི་ཕྱི་རོལ་པའི་བསྟན་བཅོས་ཀྱི་གླེགས་བམ་མོ། །

[Block 598]
མྱུར་བར་བསྒྲུབ་པར༌[^533]བྱ་སྟེ། མྱུར་བར་འབྲི་བར་ཁར༌[^534]གསིལ་གྱི་ཡུ་བ་དང་། བཙག་དང་རམས་ལ་སོགས་པ་ཚོན་ཆེན་པོ་རྣམས༌[^535]ལས་ངེས་པར་གྲོལ་པའི་ཁ་དོག་ཅེས༌[^536]བྱ་བ་ནི་འདི་རྣམས་ཀྱིས་ཁ་དོག་གི་སྒྲ་འདི་བསྡུས་པར་བྱས་ཀྱི།[^537] ཚོན་རྩི་དང་ཁར་གསིལ༌[^538]གྱི་ཡན་ལག་ཏུ་གྱུར་པ་ཁ་དོག་བྱེད་པ་ལ་བསྡུ་བའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 599]
གཉིས་པར་ཞེས་བྱ་བ་ནི་གོ་བར་འོས་པ་ཉིད་དུའོ། །

[Block 600]
འབྲས་དང་ཏིལ་དང་ནས་དང་མོན་སྲན་སྡེའུ་དང་མོན་སྲན་གྲེའུ་དང་། འབྲུ་གཞན་དང་བཟའ་བ་དང་བཏུང་བ་དག་ནི་གསུམ་པར་འོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གསུམ་པར་ཞེས་བྱ་བ་བཟའ་བར་འོས་པ་ཉིད་དོ། །
--- END BLOCKS ---
