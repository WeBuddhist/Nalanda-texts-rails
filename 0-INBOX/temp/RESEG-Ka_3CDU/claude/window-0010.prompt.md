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
[Block 351]
སྡིག་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་གང་ཞེ་ན། སྡིག་པ་སྦོམ་པོའི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། བསད་ན་ངན་སོང༌[^242]ལྟུང་བའི་ཞེས་བྱ་བ་སྨོས་ཏེ། དཔེར་ན་དུག་ཆེན་པོས་ཀྱང་སྐྱེས་བུ་ཆེན་པོ་གསོད་ལ། དུག་ཆུང་ངུས་ཀྱང་སྐྱེས་བུ་ཆེན་པོ་གསོད་པ་དང་། དེ་བཞིན་དུ་མེ་སྟག་ཆེན་པོས་ཀྱང་ཡུལ་ཆེན་པོ་ཚིག༌[^243]ལ་མེ་སྟག་ཆུང་ངུས་ཀྱང་ཡུལ་ཆེན་པོ་སྲེག་པ༌[^244]དང་། ཕས་ཕམ་པ་བྱུང་ན་ངན་སོང་གསུམ་དུ་སྐྱེ་བར༌[^245]འགྱུར་བ་དེ་བཞིན་དུ་ཉེས་པ་སྦོམ་པོ་བྱུང་བ་ལ་ཚུལ་བཞིན་དུ་མ་བཤགས་ན་ངན་སོང་གསུམ་དུ་ལྟུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 352]
བརྟུལ་ཞུགས་ཅན་གྱིས་བསད་སྙམ་སྟེ། །ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་གིས་སྐྱེས་པ་དང་བུད་མེད་དང་། མ་ནིང་སྟེ་མི་རྣམ་པ་གསུམ་ལས་གང་ཡང་རུང་བ་ཅིག་བསད་དོ་སྙམ་དུ་བསམས་ཏེ་ལུས་དང་ངག་གི༌[^246]སྦྱོར་བ་བཤམས་པ་ལས་ཞེས་བྱ་བ་ལ། ལུས་ཀྱིས་བཤམས་ཏེ་ཁུ་ཚུར་དང་ཐལ་མོ་དང་རྡོ་དབྱིག་དང་མཚོན་ཆས་ཀྱང་བཏབ། ངག་གིས་བཤམས་ཏེ་གོང་དུ་བཤད་པ་བཞིན་དུ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། ཚུལ་ཁྲིམས་འཆལ་བ་དང་། ནད་པ་རྣམས་འཆི་བའི་རིགས་སོ་ཞེས་བསྔགས་པ་བརྗོད་པ་ལས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 353 [VERSE]]
སྐྱེ་བོ་གསོན་ཡང་དེ་ལ་ནི། །
ཁ་ན་མ་ཐོ་རྣམ་གསུམ་འགྱུར། །

[Block 354]
ཞེས་བྱ་བ་ལ། གསད་པར༌[^247]ཡང་བསམས་ལུས་དང་ངག་གིས་ཀྱང་བཤམས་པ་ལས་མི་གསུམ་པོ་གསོན་ཏེ་མ་ཤི་ཡང་དགེ་སྦྱོང་དེ་ལ་ཁ་ན་མ་ཐོ་བ་རྣམ་པ་གསུམ་ཐོབ་པར་འགྱུར་ཏེ། ཡིད་ཀྱི་ཉེས་པ་སྦོམ་པོ་དང་། ལུས་ཀྱི་ཉེས་པ་སྦོམ་པོ་དང་། ངག་གི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །

[Block 355]
དེ་ལ་གསད་པར༌[^248]བསམས་པས་ན་ཡིད་ཀྱི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །

[Block 356]
ལུས་ཀྱིས་བཤམས་པས་ན་ལུས་ཀྱི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །

[Block 357]
ངག་གིས་བཤམས་པས་ན་ངག་གི་ཉེས་པ་སྦོམ་པོ་ཐོབ་པར་འགྱུར་རོ། །

[Block 358]
དེ་དག་ཚུལ་བཞིན་དུ་མ་བཤགས་ན་ངན་སོང་གསུམ་དུ་ལྟུང་ངོ་ཞེས་སྔར་བཤད་པ་བཞིན་དུ་སྦྱར༌[^249]རོ། །

[Block 359 [HEADING]]
#### ཉེས་བྱས་ཀྱི་གནས། ^5-1-3-0

[Block 360 [VERSE]]
རྡོ་དབྱུག་ཁུ་ཚུར་འཚོག་པ་དང་། །
དེ་ལས་གཞན་པའི་གནོད་པ་དང་། །
བ་ལང་ལ་སོགས་གནོད་མི༌[^250]བྱ། །
རྟ་ལ་སོགས་པ་མི་བཞོན༌[^251]ནོ། །

[Block 361]
ཞེས་བྱ་བས་ཉེས་བྱས་ཀྱི་གནས་བསྟན་ཏེ། དེ་ཞེས་བྱ་བ་ལ་གསད༌[^252]སེམས་ནི་མེད་ཀྱི་དགེ་སྦྱོང་གིས༌[^253]ཁྲོ་སེམས་ཀྱིས་མི་རྣམ་པ་གསུམ་ལ་བཙོགས༌[^254]ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 362]
ཁུ་ཚུར་འཚོག་པ་དང་ཞེས་བྱ་བ་ལ་གསད༌[^255]སེམས་ནི་མེད་ཀྱིས། ཁྲོ་སེམས་ཀྱིས་མི་རྣམ་པ་གསུམ་བཙོགས་ན༌[^256]ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 363]
དེ་ལས་གཞན་པའི་གནོད་པ་དང་ཞེས་བྱ་བ་ནི་གསད༌[^257]སེམས་མེད་པར་ཁྲོ༌[^258]སེམས་ཀྱིས་མི་རྣམས་ལ་ཐལ་མོ་བསྣུན་ནམ།[^259] ལྕག་གིས་གཞུས་སམ། ལྷགས་པའི་ཚེ་གྲང་བ་ལ་བོར་ཏམ། ཚ་བའི་ཚེ་དྲོ་བ་ལ་བོར་ན་ཉེས་བྱས་སུ་འགྱུར་ཏེ་དབྱུག་པ་ལ་སོགས་པའི་གྲངས་སུ༌[^260]ཕག་པ་ཉེས་བྱས་ཀྱི་གྲངས་ཀྱང་དེ་སྙེད་ཅིག་འཐོབ་བོ། །

[Block 364]
བ་ལང་ལ་སོགས་གནོད་མི་བྱ། །ཞེས་བྱ་བ་ནི་གཞན་ཡང་བ་ལང་དང་གླང་པོ་ཆེ་དང་རྟ་དང་ལུག་ལ་སོགས་པ་ལ་ཁལ་དགལ་བ་དང་བརྡེག་པ་ལ་སོགས་པའི་གནོད་པ་མི་བྱ་སྟེ། དེ་ལྟ་བུའི་གནོད་པ་བྱས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 365]
རྟ་ལ་སོགས་པ་མི་བཞོན་ནོ། །ཞེས་བྱ་བ་ནི་དགེ་སྦྱོང་གིས་རྟ་དང་གླང་པོ་ཆེ་ལ་སོགས་པ་བཞོན་པར་མི་བྱ་སྟེ། ཞོན༌[^261]ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 366]
དེ་ལ་གནོད༌[^262]སེམས་མེད་ལ་ཡན་ལག་གཞན་ཡོད་ན་ནི་ཉེས་བྱས་སུ་བཞག་གོ། །

[Block 367]
གནོད༌[^263]སེམས་ཡོད་ལ་ཡན་ལག་གཞན་མི་ལྡན་ན་སྦོམ་པོའོ། །

[Block 368]
ཡན་ལག་ཐམས་ཅད་དང་ལྡན་ན་མི་དེ་ནོར་ཏེ་གཞན་བསད་ན་ཡང་སྦོམ་པོའོ། །

[Block 369]
གསད་པར༌[^264]བསམས་ཏེ་སྦྱོར་བ་བྱས་པ་ལས་མ་ཤི་ན་ཡང་སྦོམ་པོའོ། །

[Block 370]
ཡན་ལག་ཐམས་ཅད་དང་ལྡན་ན་ཕས་ཕམ་པའོ། །

[Block 371]
ཕས་ཕམ་པ་བཞི་ལས་སྲོག་གཅོད་པའི་ཕས་ཕམ་པ༌[^265]རྫོགས་སོ།། །།

[Block 372 [HEADING]]
### མ་བྱིན་པར་ལེན་པའི་ཕས་ཕམ་པ། ^5-2-0

[Block 373]
མ་བྱིན་པར་ལེན་པའི་གླེང་གཞི་ནི་བཅོམ་ལྡན་འདས་ཡུལ་རྒྱལ་པོའི་ཁབ་འོད་མའི་ཚལ་བྱ་ཀ་ལན་ད༌[^266]ཀ་གནས་པ་ན་བཞུགས་སོ། །

[Block 374]
དེའི་ཚེ་སྔོན་རྫ་མཁན་ལས་རབ་ཏུ་བྱུང་བའི་དགེ་སློང་ནོར་ཅན་ཞེས་བྱ་བ་ཞིག་རྒྱལ་པོའི་ཁབ་ཀྱི་དགོན་པ་ན་སྤྱིལ་པོ་བྱས་ནས་གནས་སོ། །

[Block 375]
དེ་ནས་ནོར་ཅན་གང་གི་ཚེ་རྒྱལ་པོའི་ཁབ་ཏུ་བསོད་སྙོམས༌[^267]ལ་ཞུགས་པ་དེའི་ཚེ་རྒྱལ་པོའི་ཁབ་ཀྱི་ཕྱུགས་རྫི་དང་ཤིང་ཐུན་རྣམས་ཀྱིས༌[^268]སྤྱིལ་པོ་བཤིག་དྲལ་ཅིང་རྩྭ༌[^269]དང་ཤིང་རྣམས་སོ་སོར་ཁྱེར་རོ། །

[Block 376]
དེ་ལྟ་བུ་ལན་དུ་མ་ཞིག་བྱས་པ་དང་རྫ་མཁན་ནོར་ཅན་གྱིས་བསམས་པ་འདི་ལྟ་བུ་ཐམས་ཅད་དུ་གཙེས་ཤིང་སྤྱིལ་པོ་བྱེད་པ་ཡང་ཤིན་ཏུ་ཉོན་མོངས༌[^270]ལ་དགེ་བའི་བར་ཆད་དུ་ཡང་འགྱུར་བས་འོ་ན་བདག་གིས་སྔོན་གྱི་གནས་རྗེས་སུ་བསྒྲུབ་པས་སའི་སྤྱིལ་པོ་ཞིག་བྱས་ལ་སོ་བཏང་སྟེ་གནས་སོ་སྙམ་དུ་བསམས་ནས་ཁང་བུའི་རྨང་བཏིང་ཞིང་བརྩིགས་ནས་སོ་བཏང་ནས་ཤིན་ཏུ་མཛེས་པ་མེ་ཏོག་ཛི་བ་ཀ་བཞིན་དུ་དམར་ཞིང༌[^271]འཚེར་བ་ཞིག་བྱས་ཏེ་གནས་སོ། །

[Block 377]
དུས་གཞན་ཞིག་ན་བཅོམ་ལྡན་འདས་འཁོར་དགེ་སློང་རྣམས་དང་གནས་རྒྱུ་ཞིང་གཤེགས་པས་ཁང་བུ་གཟིགས་ནས་སུའི་ཡིན། དེ་ནི་དགེ་སློང་ནོར་ཅན་གྱི་ལགས་སོ་ཞེས་སྨྲས་སོ། །

[Block 378]
འདི་ལྟ་བུའི་ཕྱིར་མུ་སྟེགས་པ་རྣམས་ང་ལ་འཕྱ་བར་འགྱུར༌[^272]གྱིས་ཁང་བུ་ཆོམས་ཤིག༌[^273]ཅེས་བཀའ་སྩལ་ནས། དགེ་སློང་རྣམས་ཀྱིས་ཁང་བུ་བཅོམ་སྟེ་གནས་སོ། །

[Block 379]
དེ་ནས་ཡང་ནོར་ཅན་གྱིས༌[^274]བསམ་པ་རྒྱལ་པོའི་ཁབ་གྱི་ཤིང་སྲུངས་ཀྱི་དཔོན་དང་བདག་མཛའ་བས་ཤིང་གི་ཁང་པ་ཞིག་བྱའོ་སྙམ་དུ་བསམས་ནས། ཤིང་སྲུངས་པ་ལ་ལྷས་ཤིང་བྱིན་པ༌[^275]འོན་ཅིག་ཅེས་སྨྲས་པ་དང་། ཤིང་སྲུངས་ཀྱི་དཔོན་པོས་ཀྱང་ལྷས་ཕུལ་ན་བཙུན་པ་ཅི་བདེར་སྣོམས་ཤིག་ཅེས་སྨྲས་ནས། རྒྱལ་པོའི་ཁབ་ཀྱི་ཞིག་རལ་བཅོས་པའི་རྒྱུ་ཤིང་བཅད་པ་དུ་མ་ཞིག་གཤགས་གཏུབས་ཏེ་ཁྱེར་བ༌[^276]གྲོང་ཁྱེར་སྲུངས་པའི༌[^277]དཔོན་པོས་མཐོང་ནས་རྒྱལ་པོ་མ་སྐྱེས་དགྲ་ལ་སྨྲས་སོ། །

[Block 380]
རྒྱུ་མཚན་ཅན་བཀུག༌[^278]སྟེ། དགེ་སློང་ཁྱོད་ནི་ཤིང་མ་བྱིན་པར་ལེན་པ་དབང་བྱས་པ་དང་། མི་དབང་གིས་བདག་ལ་སྩལ་ཏོ། །

[Block 381]
སྔོན་ཡབ་ཀྱིས་ལྷ་ཁྱོད་རྒྱལ་པོར་དབང་བསྐུར་བའི་ཚེ་ངའི་ཡུལ་དགེ་བར་གྲགས་པས་དགེ་སློང་དང་བྲམ་ཟེ་རྣམས་རྩྭ་དང་ཤིང་དང་ཆུ་མ་བྱིན་པར་མི་སྤྱོད་པ༌[^279]དེ་ཐམས་ཅད་ཅི་བདེར་སྤྱོད་ཅིག་ཅེས་ཁྱུ་མཆོག་གི་སྒྲ་ཆེན་པོ་བསྒྲགས་པ་ནི༌[^280]མི་དགོངས་སམ། རྒྱལ་པོས་སྨྲས་པ། དེ་ནི་ཡོངས་སུ་བཟུང་བ་མེད་པ་ལ་བྱའི་ཡོངས་སུ་བཟུང་བ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་སྨྲས་པ་དང་། ཡོངས་སུ་མ་བཟུང་བ་ལ་ནི་རྒྱལ་པོས་མངའ་བགྱིར་ཅི་མཆིས་ཞེས་གསོལ་པ་དང་། རྒྱལ་པོ་ཤིན་ཏུ་ཁྲོས་ནས་མ་བྱིན་པར་ལེན་པའི་དགེ་སློང་བསད་པར་རིགས་ན་ཁྱོད་ད་སླན་ཆད་དེ་ལྟར་མ་བྱེད་ཅིག་ཅེས་སྤྱོས་ནས་སླར་བཏང་ངོ་། །དེ་ནས་དེ་ལྟར་གྱུར་པ་དགེ་སློང་རྣམས་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་ཏོ། །

[Block 382]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དགའ་བོ་ལ་བཀའ་སྩལ་པ། ཀུན་དགའ་བོ་ཁྱོད་སོང་ལ་རྒྱལ་པོའི་གྲོང་དཔོན་དང་དེད་དཔོན་ལམ་བྱིན་པར་ལེན་པ་ཇི་ཙམ་ཞིག་བླངས་པས་སྲོག་ལ་འབབ་པ་དང་ཡུལ་ནས་དབྱུང་བའི་ཆད་པ་གཅོད་པར་བྱེད་སྨྲོས་ཤིག་ཅེས་བཀའ་སྩལ་པ་དང་། ཀུན་དགའ་བོས་དེ་བཞིན་དུ་སྨྲས་པ་དང་། མ་ཤ༌[^281]ཀ་ལྔའམ་ལྔ་ལས་ལྷག་པ་བླངས་པས་སྲོག་ལ་འབབ་པ་དང་ཡུལ་ནས་འབྱིན་པའི་ཆད་པ་གཅོད༌[^282]དོ་ཞེས་མཆི་བ་བཅོམ་ལྡན་འདས་ལ་དེ་བཞིན་གསོལ་པས། དགེ་སློང་ནོར་ཅན་བཀུག་ནས་རྣམ་གྲངས་དུ་མར་སྨད་ནས་འདུལ་བ་ལ་བསླབ་པའི་གནས་བཅས་སོ། །

[Block 383 [VERSE]]
དགེ་ཚུལ་བདག་གམ་གཞན་རྣམས་ཀྱིས། །
རྐུ་སེམས་མཐུ་དང་འཇབ༌[^283]བུ་ཡིས། །
འཁྲུལ་པ་མེད་པར་མི་གཞན་གྱི། །
གནས་ནས་མ་ཤ་ལྔ་ཙམ་མམ། །

[Block 384]
རང་གི་ཡུལ་ནས་བྱུང་བ་ཡང་། །ཀཱར་ཥཱ་པ་ཎའི་བཞི་ཆ་བརྐུས།[^284] །དེ་བརྐུས་ཚུལ་ཁྲིམས་ཞིག་པར་འགྱུར། །ཞེས་བྱ་བ་ལ་དགེ་ཚུལ་ནི་རབ་ཏུ་བྱུང་བའི་སྡོམ་པ་ལ་གནས་པའོ། །

[Block 385]
བདག་གིས་ཀྱང་རྐུ་སེམས་དང་ལྡན་པས་མཐུ་དང་འཇབ་བུ་ཡིས་བརྐུས་ན་ཚུལ་ཁྲིམས་ཞིག་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་ལྟར་རྐུ་སེམས་དང་ལྡན་པས་མཐུ་དང་འཇབ༌[^285]བུས་ཀཱར་ཥཱ་པཎའི་བཞི་ཆ་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན༌[^286]ཕས་ཕམ་པའོ། །

[Block 386]
རྐུ་སེམས་མེད་ན་བསྡམ་པར་བྱ་བའི་ཉེས་བྱས་གཅིག །གཞན་གྱི༌[^287]མཐུ་དང་འཇབ་བུས་བརྐུས་ན་ཚུལ་ཁྲིམས་ཞིག་པར་འགྱུར་ཏེ། བདག་ཉིད་ཀྱིས་ནི་མ་ཡིན་གྱིས་དགེ་སློང་གྲོགས་པོ་ཞིག་ལ་རྐུར་བཅུག་པ་ལས་དེས་མཐུ་དང་འཇབ་བུས་བརྐུས་ཏེ། ནོར་བདག་ཅག་སོ་སོར་བགོས་རིན་ཐང་ཚང་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 387]
རིན་ཐང་མ་ཚང་ན་ཉེས་བྱས་སྦོམ་པོ་རེ་རེ་བརྐུས་ན་བརྐུས་ཤས་ཀྱི༌[^288]སྐལ་བ་བླངས་ན་ཉེས་པ་སྦོམ་པོ་གཅིག །འཁྲུལ་པ་མེད་པར་མི་གཞན་གྱི་ཞེས་བྱ་བ་ལ་འཁྲུལ་པ་ནི་རྨོངས་པ་དང་མི་དྲན་པ་ཡིན་ལ་དེ་མེད་པ་ནི་སེམས་རང་བཞིན་དུ་གནས་པའོ། །

[Block 388]
ཡང་བརྐུ་བར་བྱ་བའི་རྫས་གང་ཡིན་པ་དེ་ཉིད་མངོན་པར་ཐོབ་པ་ལ་བྱ་སྟེ། བརྐུ་བར་བྱ་བའི་རྫས་ཉིད་ནི་མ་ཐོབ་ཀྱི་བར་དུ་རྫས་གཞན་གྱིས་ཐོབ་པ་ལས་འཁྲུལ་ཞེས་བྱ་སྟེ་དེ་ནི་རིན་ཐང་ཚང་ཡང་ཕས་ཕམ་པར་མི་བྱ་སྟེ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 389]
མི་གཞན་ཞེས་བྱ་བ་ནི་བདག་གི་ནོར་དགར་བའི་ཚིག་སྟེ། མི་གཞན་གྱི་ནོར་བརྐུས་ན་ཕས་ཕམ་པར་འགྱུར་རོ།[^289] །བདག་གི་ནོར་བརྐུས་ན་རིན་ཐང་ཚང་ཡང་སྦོམ་པོར་མི་འགྱུར་རོ། །

[Block 390]
གནས་ནས་མ་ཤ་ལྔ་ཙམ་ཞེས་བྱ་བ་ལ་གནས་ནི་ནོར་རྫས་གནས་ནས་སྤགས་ཏེ་བར་དུ་ཆོད་རིན་ཐང་ཚང་བ་ལས་ཕམ་པའོ། །
--- END BLOCKS ---
