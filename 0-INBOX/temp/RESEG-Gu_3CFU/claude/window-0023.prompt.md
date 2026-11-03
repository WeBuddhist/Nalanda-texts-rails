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
[Block 806]
འདི་ལ་གསལ་བར༌[^582]བྱེད་པ་ཡིན་པ་ནི། སློབ་དཔོན་དང་མཁན་པོ་མཆོག་ཏུ་ཚུལ་ཁྲིམས་འཆལ་པ་ལ་ཡང་བསྙེན་བཀུར་བྱའོ། །

[Block 807]
ཕ་མ་དང་ནད་པ་དག་ནི་ཁྱིམ་པ་ཡིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་འདི་རྣམས་ལ་ཕན་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བས་ན་འདི་སྔོན་དུ་གནང་ངོ་། །ལེགས་པར་སྦྱར་བའི་ཁྲུས་ཀྱིས་བཀྲུའོ་ཞེས་བྱ་བ་ནི་འདིར་གླེང་གཞི་ལས་འདོད་པ་ཡིན་ཏེ། ནད་པའི་ཚིག་ནི་ཐ་སྙད་དུ་མ་བྱས་པ༌[^583]ཡིན་ཏེ། འདི་ལ་གཞན་དུ་མཐུན་པ་ཉིད་ཀྱང་མ་ཡིན་ཏེ། ཁྱད་པར་ཡོངས་སུ་མི་འཛིན་པའི་ཕྱིར་ཐམས་ཅད་ཀྱི་དབང་དུ་མཛད་ནས་ཉེ་བར་བརྟགས་པའོ། །

[Block 808]
དེའི་རང་གི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར། རླུང་འདྲེན་པའི་རྩ་བ་དང་སྡོང་བུ་དང་ལོ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་བསྐོལ་བས་ཁྲུས་བྱ་བ་ནི་དེའི་མིང་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལེགས་པར་སྦྱར་བའི་ཁྲུས་ཀྱིས་བཀྲུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 809]
བཅུད་ནི་ཁྲུས་ཀྱི་དོན་ཏོ། །

[Block 810]
དེ་བས་ན་འདི་རྣམས་ལ་འདིར་ཡན་ལག་ཉིད་དོ། །

[Block 811]
ཁྲུས་ཇི་ལྟར་བྱ་ཞེ་ན། བསྐུ་མཉེ་བྱས་ནས་ཏེ་མི་རྩུབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲན་ཆུང་གི་ཕྱེ་མས་ཉེ་བར་བསལ་བའི་ཕྱིར་འདི་མི་རྩུབ་པའི་དོན་འདི་ལ་འབྲུ་མར་ལ་སོགས་པས་བསྐུ་མཉེ་བྱས་པས་དེ་དང་དབྲལ་བའི་ཕྱིར་སྲན་ཆུང་གི་ཕྱེས་བསྐུ་མཉེ་བྱས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 812]
དེ་དང་དབྲལ་བའི་ཕྱིར་ཁྲུས་གཅལ་གྱིས་སོ། །

[Block 813]
སྔ་མའི་ཆེད་དུ་ཆུའི་བུམ་པ་ཕྱི་མར་སྣུམ་ཐིགས་པ༌[^584]གཉིས་སམ་གསུམ་བླུགས་སོ་ཞེས་བྱ་བ་ནི།[^585] སྔ་མའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་མི་རྩུབ་པ་ཉིད་ཀྱི་ཆེད་དུ་གཉིས་སམ་གསུམ་སྣུམ་གྱི་ཐིགས་པ་ཆུའི་བུམ་པར་ཕྱེ་མ༌[^586]བླུགས་པར་བྱ༌[^587]བའི་དོན་ཏོ། །

[Block 814]
ལྕགས་ཀྱི་གཞོང་རིགས༌[^588]སུ་ཁྲུས་བྱའོ། །

[Block 815]
དེ་ནི་ནད་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི་གཞོང་པའོ། །

[Block 816]
ནད་པ་མ་ཡིན་པས་ནི་བཅང་བར་མི་རིགས་པ་སྟེ། ལྕགས་ཀྱི་རི་ལུ་ལྟར་དགོས་པ་མེད་དོ་ཞེས་བྱ་བ་འདི་ལ་རྟོགས་པར་བྱའོ། །

[Block 817]
འདི་ལྟ་བུའི་རིགས་ཅན་ལ་དོན་མེད་པར་བྱེད་པ་ལ་ང་རྒྱལ་ཡིན་ཏེ། དེ་ཡང་ཐམས་ཅད་ཉེས་པར༌[^589]བྱས་པ་ཞེས་བྱ་བ་གོ་བཞིན་པ་ཉིད་ཀྱི་ཕྱིར་མདོར་བྱས་པ༌[^590]མ་ཡིན་ནོ། །

[Block 818]
དེའི་སྟེང་དུ་ཁ་གབ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་ཆུ་དྲོན་མོ་ལ་གྲང་བའི་དངོས་པོ་ཡོངས་སུ་བསལ་བའི༌[^591]ཕྱིར་རོ། །

[Block 819]
དེར་གཉའ་བར་སྔས་ནང་ཚངས་ཅན་གཞུག་གོ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 820]
འདིར་ཁྲུས་ནི་ཐོགས་པ་མེད་པར་སྡུག་བསྔལ་མེད་པའི་དོན་དུ་སྟེ་དེ་བས་ན་འདི་བཟུང་བའོ། །

[Block 821]
གར་བབ་བབ་ཏུ་རྐང་པ་མི་བཀྲུའོ་ཞེས་བྱ་བ་ལ།

[Block 822 [VERSE]]
འདི་ནི་གཙུག་ལག་ཁང་གི་དབང་དུ་བྱས་པའོ། །
དེའི་གནས་ནི་ཝ་ཁར༌[^592]རོ་ཞེས་བྱ་བ་ལ།
དེའི་ཞེས་བྱ་བ་ནི་རྐང་པ་བཀྲུ་བའོ། །

[Block 823]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྐང་པ་ཝ་ཁར་བཀྲུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 824]
རྐང་ཁྲུས་ཀྱི་གཞི་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་མེད་པར་ཝའི་ཁ་ལ་སོགས་པ་དོན་གྲུབ་པ་རྣམ་པར་ཉམས་པ་སྟེ། དེའི་ཕྱིར་འདི་ནི་རེས་འགའ་བྱ་བ་དང་རེས་འགའ་མི་བྱ་བ་ཡིན་གྱི་ཞེས་བྱ་བ་ཡང་དག་པར་བསྟན་པའི་དོན་དུ་དང་པོར་བྱ་བའི་ཚིག་སྦྱར་བའོ། །

[Block 825]
དགེ་འདུན་གྱི་རྫས་ནི་འདིའི་གནས་ཡིན་ཏེ། དགེ་འདུན་གྱི་རྫས་ནི་གཅིག་ལ་སྐབས་མེད་དེ་དེ་བས་ན་མང་པོའི་ཚིག་གོ། །

[Block 826]
ཕྱོགས་གང་དུ་ཞེ་ན། དེའི་ཕྱིར་གཙུག་ལག་ཁང་གི་སྟེང་གི་ཤར་ལྷོའི་མཚམས་སུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣམ་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་རུས་སྦལ་གྱི་རྣམ་པ་འདྲ་བ་རྩུབ་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དོན་ནི་དྲི་མ་སེལ་བར་བྱེད་པའོ། །

[Block 827]
ཆོལ་ཟངས་ས་ལས་བྱས་པ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིའི་མིང་ནི་ལྷུང་ཞིང་བཟུང་བ་ལའོ། ། ཅི་ལས་བྱས་པ་ཞེ་ན། ས་ལས་བྱས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་གསེར་དང་དངུལ་དང་བཻ་ཌཱུརྱ་དང་ཤེལ་ལས་བྱས་པའི་ཆོལ་ཟངས་ཉེ་བར་གཞག་པར་མི་བྱ་སྟེ། འོན་ཀྱང་སའི་རང་བཞིན་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 828]
དབྱིབས་ཇི་ལྟ་བུ་ཞེ་ན་དེའི་ཕྱིར་ཞབས་གླང་པོ་ཆེའི་རྨིག་མཐིལ་འདྲ་ལ་སྙིང་པོ་ཅན་ནོ་ཞེས་བྱ་བ༌[^593]སྨོས་ཏེ། འདིར་དོན་ནི་མི༌[^594]རྡིབ་པའོ། །

[Block 829]
སྙིང་པོ་ཅན་ནོ་ཞེས་བྱ་བ་ནི་དག་བཞིན་པའི་རྐང་པ་གཞག་པའི་དོན་དུ་འདི་བྱའོ། །

[Block 830]
སྙིང་པོ་གང་དུ་བྱས་པ། དེ་དང་ལྡན་པར་ཤེས་ཤེ་ན། དབུས་ན་ཡོད་པ་ཞེས༌[^595]སྨོས་ཏེ། རྣམ་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་ཀ་དམ་པའི་མེ་ཏོག་འདྲ་བ་རྩུབ་པ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྐང་པ་མི་འདྲེད་པའི་དོན་དུ་རྩུབ་པ་ཉིད་དོ། །

[Block 831]
བཀྲུས་ནས་ཁ་སྦུབ་ཏུ་གཞག་གོ་ཞེས་བྱ་བ་ལ། ཁྲུས་བྱེད་པ་འདི་ནི་དྲི་མ་མེད་པ་ཉིད་ཀྱི་དོན་དུ་སྟེ། དྲི་མ་མེད་པ་ཉིད་ནི་དྲི་མ་དང་བྲལ་བ་ཉིད་དོ། །

[Block 832]
འདི་ལ་ནི་གང་ཞིག་དེར༌[^596]ཆུ་གཙང་མ་རྣམས༌[^597]གནས་པ་དེ་ལ༌[^598]བསྒྲུབ་པ་སྟེ་དེ་ལས༌[^599]དེ་བས༌[^600]ཆུ་གཞན་དག་གིས་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 833]
འདིར་གཞུང་ནི་རྐང་པ་གཉིས་བཀྲུས་ནས་རྐང་པ་བཀྲུས་པའི་ཆུ་གཙུག་ལག་ཁང་གི་ཕྱི་རོལ་ལམ་ཝ་ཁར་དབོར་བཅུག་སྟེ་སླར་ཡང་འཁྲུར་བཅུག་ནས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་དུ་གཞག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་ནི་ཁང་ཐོག་ཏུའོ། །

[Block 834]
གང་ཟག་གི་ནི་གནས་ཁང་གི་སྒོ་གླེགས་ཀྱི་ཕག་ཏུའོ། །

[Block 835]
གཙུག་ལག་ཁང་གི་ཕྱོགས་གང་དུ་ལྷུང་བཟེད་ཀྱི་བྱི་དོར་ལ་སོགས་པ་བྱས་པ་དེར་ཆུས་བྱུག་གོ། །

[Block 836]
ཡང་ན་བསྐུའོ། །

[Block 837]
དེ་མདུང་རྩེའི་རྣམ་པ་ལྟ་བུའམ། རྫ་རྔའི་རྣམ་པ་ལྟ་བུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣམ་པ་དེ་ལྟ་བུ་ཞེས་བྱ་བ་འཇུག་པ་ཡིན་ནོ། །ཅི་ཞིག་གིས་བསྐུ་ཞེ་ན། བ་གླང༌[^601]གི་ལྕི་བའམ་འཇིམ་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 838]
དཀོན་མཆོག་གི་དོན་ཉིད་དུ་བསྐུ་བ་ལ་ནི་རྣམ་པར༌[^602]ངེས་པ་མེད་དོ། །

[Block 839]
ལྷུང་བཟེད་མེད༌[^603]པ་རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ། །

[Block 840]
ཆུང་ངུ་དང་ཆེན་པོ་དང་སྐྱ་བས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷུང་བཟེད་ནི་གསུམ་ཏེ།[^604] ཆེ་བ་དང་འབྲིང་དང་། ཆུང་བ་ཞེས་བྱ་བའོ། །

[Block 841]
དེ་རྣམས་ཀྱི་ཚད་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར། ཁའི་ཆའི་མཐའ་ཁོ་ན་ནས་མཐེ་བོའི་ལྟོ་གང་གི་ལྷག་མར་འབྲས་ཐུག་པོ་ཆེ་མ་ག་དྷཱའི་བྲེའུ་ཆུང་གང་བཙོས་པ་སྲན་ཚོད་དང་བཅས་པ། ཚོད་མ་དང་བཅས་པ་ལྷག་པ་ནས་དོའི་བར་དེ་ཤོང་བ་དེ་ནི་རིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁའི་ཆ་ནས་ཏེ་འོག་གི་ཚད༌[^605]ལ་ནི་མ་ཡིན་ནོ། །

[Block 842]
མཐའ་ཁོ་ན་ནས་ཏེ་ཕྱོགས་གཞན་གྱི་དེ་མ་ཐག་ཏུ་གང་ཞིག་མཐེ་བོའི་ལྟོ་སྟེ་མཐེ་བོའི་ཚིགས་ཀྱི་ཕྱོགས་ལ་གང་ཞིག་མཐེ་བོང་གི་རྒྱ་ཆེ་བ་ཉིད་ནི་ཚད་དེ་ཉིད་དེ། དེའི་ས་ལྷག་མ་སྨད་ཀྱི་ཆར་མ་ག་དྷཱའི་བྲེའུ་ཆུང་གང་བཙོས་པ་དེའི་ཁའི་ཆ་གཉིས་འགྱུར་ཤོང་བའི་བྲེ་ཇི་སྲིད་དུ༌[^606]རང་དང་རྗེས་སུ་མཐུན་པའི་ཚོད་མ་དང་བཅས་པ་དེའི་ཁར་བྲེ་ཉིས༌[^607]འགྱུར་རམ་གང་ཞིག་འཛིན་པ་དེ་ནི་འདི་དང་མ་བྲལ་བར༌[^608]རིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ།[^609] །འབྲུ་མར་དང་མར་དང་སྦྲང་རྩི་དང་ཆུ༌[^610]ལ་སོགས་པ་རྣམས་ཀྱི་སྲོང༌[^611]སུམ་ཅུ་རྩ་གཉིས་ནི་མ་ག་དྷཱའི་བྲིའོ། །

[Block 843]
གཞན་ཞུ་བ༌[^612]མ་ཡིན་པ་རྣམས་ལས་བཅུ་དྲུག་ཅེས་བྱ་བ་རྫས་ཙམ་བསམ་པར༌[^613]བྱེད་པ་རྣམས་ཀྱིའོ། །

[Block 844]
དེ་བས་ན་འདིར་ཆུ་སྲང་བཅུ་དྲུག་ལ་མ་ག་དྷཱའི་བྲེས་བརྗོད་པ་ཞེས་བྱ་བར༌[^614]རྟོགས་པར་བྱའོ། །

[Block 845]
འདིར་གཞུང་དུ་ནི་གང་དུ་མ་ག་དྷཱའི་འབྲས་བྲེའུ་ཆུང་དོ་བཙོས་པ་སྲན་ཚོད་དང་བཅས་ཚོད་མ་དང་བཅས་པ་ལ་མཐེ་བོང་གི་ལྟོ་བ་བཅུག་པ་ཁའི་ཆ་ལ་རེག་པར་མི་འགྱུར་བ་དེ་ནི་ཆེན་པོའི་ཚད་ཡིན་ནོ། །
--- END BLOCKS ---
