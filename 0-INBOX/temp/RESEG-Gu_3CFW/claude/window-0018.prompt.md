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
ལྕགས་ལས་བྱས་པ་ལས་གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ལྕགས་ཀྱི་རང་བཞིན་ཁོ་ན་ལས་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 632]
དོན་གྱིས༌[^563]འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 633]
ཡུ་བ་རྩི༌[^564]ཅན་དང༌[^565]ཁྲ་བོ་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི། ཡུ་བ་མི་བཅང་ངོ་ཞེས་བྱ་བའི་ཚིག་གི་ལྷག་མའོ། །

[Block 634]
སོར་དྲུག་གི་ཚད་ལས་ལྷག་པ་མི་བཅང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གྲི་གུ་ནི་གསུམ་སྟེ། ཆེན་པོ་དང་འབྲིང་དང་ཆུང་ངུའོ། །

[Block 635]
ཆེན་པོ་ནི་སོར་དྲུག་གོ། །

[Block 636]
ཆུང་ངུ་ནི་སོར་བཞིའོ། །

[Block 637]
དེའི་བར་ནི་འབྲིང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 638]
དེ་ལས་མང་བ་ཉིད་ནི་སྤང་བར་རིག་པ་ཡིན་ཏེ། དེ་ལས་ཆུང་བ་ཉིད་ཀྱིས་ནི་དགོས་པ་མི་འགྲུབ་པར་བརྗོད་པ་ཞེས་བྱ་བ་འདིར་དེའི་བསྡུས་པ་ཉིད་ཤེས་ནས་དེ་ལྟར་སྨོས་སོ། །

[Block 639]
ཁ་ཅིག་ལས་ནི་བརྒྱད་ལས་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི་འདོན་པའི་རྣམ་པར་རྟོག་པ་ལས་འདི་ཉེ་བར་བཏགས་པ་སྟེ། འདིར་གཞུང་ཁ་ཅིག་ལས་ནི། གྲི་གུ་སོར་བརྒྱད་ཀྱི་ཚད་ལས་ལྷག་པ་མི་བཅང་ངོ་ཞེས་འབྱུང་ངོ་། །འདིར་གཞུང་ནི་ཆེན་པོ་ནི་སོར་བརྒྱད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 640]
ཤིང་བུ་ཐུང་བ་ཉིད་ལ་དེ་ཡོད་པར་གྱུར་ནའོ། །

[Block 641]
དེ་ལྟ་བས་ན་མི་རིགས་པར་གྱུར་པ་འདི་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 642]
སོར་བཞི་བས་ཐུང་བ་ནི་དགོས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི། མ་ལུས་པ་མ་ཡིན་པ་དགོས་པ་ལ་དགོངས་ནས་དགོས་པ་མེད་པ་ཉིད་བསྟན་པར་བྱ་སྟེ། དགོས་པ་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 643]
གང་གི་ཕྱིར་དེ་ལས་རྣམ་པ་ཐམས་ཅད་དུ་དགོས་པ་མི་འགྲུབ་པ་ནི་མ་ཡིན་ནོ། ལྕི་བའི་བྱུག་པས་བསྐུས་པར་བཙེམ་མོ་ཞེས་བྱ་བ་ནི༌[^566]དངོས་པོའམ་རྒྱུད་པས༌[^567]བཙེམ་པར་བྱ་བའི་ཆོས་གོས་ལ་གནས་གང་ཡིན་པ་དེ་ལ་རྡུལ་ལྡང་བ་མེད་པར་བྱ་བའི་ཕྱིར་ལྕི་བའི་བྱུག་པས་བསྐུ་བར༌[^568]བྱའོ། །

[Block 644]
ལྕི་བ་མེད་ན་ཆག་ཆག་གདབ་ཅིང་ཕྱགས་པར་རོ། །

[Block 645]
དེ་བཙེམ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་སོ། །

[Block 646]
འདིར་གཞུང༌[^569]ནི། དགེ་སློང་དག་བྱ་གག་གི་གཤོག་ཤིང༌[^570]ངམ། སྨྱིག་མའི་ཚལ་བུ་གང་ཡིན་པས་ཆོས་གོས་དག་འཚེམ་པར༌[^571]བྱའོ་ཞེས་གསུངས་པས་དེའི་ཕྱིར་མདོ་འདི་བྱས་པའོ། །

[Block 647]
ཁབ་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ༌[^572]ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་བྱ་གག་གི་གཤོག་ཤིང༌[^573]དང་སྨྱིག་མའི་ཚལ་བུ་འབའ་ཞིག༌[^574]ཏུ་མ་ཟད་ཀྱི༌[^575]ཁབ་ཀྱིས༌[^576]ཀྱང་བཙེམ་དུ་རུང་བའོ། །

[Block 648]
བྱ་གག་གི་གཤོག་ཤིང༌[^577]ལ་སོགས་པ་ལས་དེ་དང་མཐུན་པ་སྟེ་ཁབ་ཀྱིས་ནི་མ་ཡིན་ཏེ། ཁབ་ཀྱིས་འཚེམ་པའི་རྣམ་པ་སྟེ། འདིས་འཚེམ་པར་བྱེད་པའི་བཤད་པ་ཞེས་ཏེ་ཤེས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 649]
དྲ་བའི་གཞུང་ནི་དགེ་སློང་དག་ལག་པ་དག་གིས་དྲལ་བར༌[^578]བྱེད་པ་ན་མ་རུང་བར་གྱུར་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གྲི་གུས་དྲ་བར་བྱའོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 650]
ཁབ་ཀྱི་གཞུང་ནི་དགེ་སློང་དག་བྱ་གག་གི་གཤོག་ཤིང་དང་། སྨྱིག་མའི་ཚལ་བུས་ཆོས་གོས་དག་འཚེམ་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཁབ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ༌[^579]ཡིན་ནོ། །

[Block 651]
དེ་ལ་དྲ་བ་ཉམས་པའི་སྐྱོན་ལ་བརྟེན་ནས་ངེས་པར་ཤེས་པའོ། །

[Block 652]
ཁབ་ཀྱི་ཉེས་པ་ལ་མངོན་པར་མ་བརྟེན་པས་འཕགས་པ་བ༌[^580]ཀུ་ལ་ལ་གླེང་གཞིའི་རྒྱུ་ལས་མི་ལྡོག་པར་རྗེས་སུ་གནང་ངོ་། །དེ་བཅང༌[^581]བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁབ་དེའོ། །

[Block 653]
ར་གན་དང་ཟངས་དང་ཁར་བ༌[^582]དང་ལྕགས་ལས་བྱས་པ་ལས་གཞན་པ་མི་བཅང་ངོ་། །ཁ་ཅིག་ལས་ཟངས་དང་ལྕགས་རྣོ་བ་དག་ལས༌[^583]བྱས་པའི་ཞེས་སོ་ཞེས་བྱ་བ་ནི། འདིར་མ་མོའི་གཞུང་ཁ་ཅིག་ལས་ཁབ་རྣོ་བཟངས༌[^584]དང་རྣོ་ལྕགས་ལས་བྱས་པ་བཅང་ངོ་ཞེས་འབྱུང་སྟེ། རྣོ་བ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་ཀྱི་རིགས་ཀྱི་བདག་ཉིད༌[^585]གཞན་ཞིག་ཡོད་དེ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 654]
དེའི་ཁབ་རལ་སྤུ༌[^586]གུའམ་ཆང་པ་ལྟ་བུ་བཅང་བར་བྱའོ། །

[Block 655]
དེ་ངོ་ཚ་མེད་པ་དང་དགེ་ཚུལ་དག་ལ༌[^587]རག་ལས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་ཁབ་རལ་དེ་དེའི་ནི་མ་མོ་དག་ལས་སོ། །

[Block 656]
མི༌[^588]ཤེས་པ་དང་མི༌[^589]དྲན་པ་དང་། རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དག་ལ་ཡང་ཞེས་བྱ་བ་ནི། རག་ལས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྗེས་སྙེགས༌[^590]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 657]
ཁབ་དང་གྲི་གུ་དག་བཙས་མི་ཟོས་པར་བྱ་བའི་ཕྱིར་སྤྲ་ཚིལ་གྱིས་བསྐུས་པའི༌[^591]རས་མར་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། དགེ་སློང་རྣམས་ཀྱི་ཁབ་བཙས་ཟོས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རས་མལ་སྤྲ་ཚིལ་གྱིས་བསྐུ་བར་བྱ་ཞིང་དེར་ཁབ་དཀྲིས་ཏེ་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་དང་།

[Block 658]
གཞུང་གཞན་དག་ལས།

[Block 659]
ཁབ་དང་མཚོན་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་འདིར་མཚོན་གྱི་སྒྲ་སྨོས༌[^592]སོ། །

[Block 660]
མི་འབྱིལ་བར་བྱ་བའི་ཕྱིར་ཆོས་གོས་ལ་སྒྲོག་རྟེན་བྱས་ཏེ་སྒྲོག་གཟུངས་གདགས་སོ་ཞེས་བྱ་བ་ནི། མི་འབྱིལ་བར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི། ཆོས་གོས་གྱོན་པ་ལུས་ལས་མི་འབྱིལ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 661]
སྒྲོག་གུ་ཡང༌[^593]ཞེས་བྱ་བ་ནི་མི་འབྱིལ་བར༌[^594]བྱ་བའི་ཕྱིར་ཆོས་གོས་ལ་སྒྲོག་རྟེན་བྱས་པ་ལ་དེ་གདགས་པའོ། །

[Block 662]
གཙོ་བླག༌[^595]མཁན་ལ་གོས་ཁ་བསྒྱུར་བ་དང་ཁ་མ་བསྒྱུར་བ་འཁྲུར་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། དྲུག་སྡེ་དག་བཙོ༌[^596]མཁན་དག་ལ་གོས་དག༌[^597]འཁྲུར་འཇུག་པ་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་གི་གོས་ངུར་སྨྲིག་དག་བཙོ་བླག་མཁན་དག་ལ་འཁྲུར་མི་འཇུག་པར་གཞོང་པ་འཇམ་པོར་རང་གིས་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། དྲུག་སྡེ་དག་གོས་དཀར་པོ་དག་བཙོ་བླག༌[^598]མཁན་དག་ལ་འཁྲུར་འཇུག་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་ལྟ་བས་ན་དགེ་སློང་གིས་ཐམས་ཅད་ནས་ཐམས་ཅད་དུ་བཙོ་བླག་མཁན་ལ་གོས་འཁྲུར་མི་འཇུག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 663]
དེ་དང་འདྲ་པར་རང་གིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བཙོ་བླག་མཁན་དེ་དང་འདྲ་བར་མི་བྱའོ།[^599] །དེའི་ངོགས་སུ༌[^600]མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་བཙོ་བླག་མཁན་དེའོ། །

[Block 664]
ཤིང་གི་ངོས་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གོས་བཀྲུ་བར་མི་བྱའོ། །

[Block 665]
གཞོང་པ་འཇམ་པོར་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གཞོང་པ་འཇམ་པོར་རང་གིས་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 666]
ཆུ་བདེ་བས་སོ་ཞེས་བྱ་བ་ལ། དེ་ནི་དྲི་མ་འདག་པའི་ཐབས་བསྟན་པའོ། །

[Block 667]
དེ་བས་ན་ཐབས་གཞན་གྱི་གནས་སུ་དེ་ལ་ནི་བསིལ༌[^601]བ་ཉིད་ནི་ཧ་ཅང་མི་གྲང་བ༌[^602]ནི་མ་ཡིན་ནོ། །

[Block 668]
ལག་པ་གཉིས་ཀྱིས་མཐར་གྱིས་བསྒྱུར་ཞིང་ངོ་ཞེས་བྱ་བ་ནི་བསྒྱུར་ཞིང་བཀྲུ་བར་བྱའོ། །

[Block 669]
མི་ནུས་ན་རྐང་པ་གཉིས་ཀྱིས་སོ། །

[Block 670]
དེ་ལྟར་ཁྱིམ་པས་བཀྲུར་རུང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རང་གིས་བཀྲུ་བའི་ཆོ་ག་དེ་བསྟན་པ་དེ་ལྟར་རོ། །
--- END BLOCKS ---
