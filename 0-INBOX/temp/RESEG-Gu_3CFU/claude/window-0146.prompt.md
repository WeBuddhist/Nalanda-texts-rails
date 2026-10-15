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
[Block 5111]
ཐུན་ཚོད་དུ་རུང་བ་ཡང་དེ་མ་ཐག་པའི༌[^3503]མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་ཆུ་གྲང་མོས་སོ། །

[Block 5112]
འདི་ལ་གཞན་གྱི་དུས་མ་ཡིན་པ་ལས་མ༌[^3504]བྱས་པ་ལ༌[^3505]བྱས་པ་ཉིད་དོ། །

[Block 5113]
མར་བསྲུབ་པའི་ཚེ་དང་འབྲི་མར་འཚིར་བའི་ཚེ་ན་ཡང་ཆུ་གྲང་མོས་གདབ་དགོས་མོད་གྱི། འོན་ཀྱང་མར་དང་མར་ནག་པོ་དག་གིས༌[^3506]རུང་བར་བྱས་པ་ཉིད་དོ། །

[Block 5114]
ཀུན་སློང་ལ་འདི་དགོས་པས་འདི་དག་གྲུབ་པ་ལ་རུང་བ་འདི་ལ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་བུ་རམ་ཡང་མེས་བསྐོལ་བ་ན་ཆུ་གྲང་མོས་གདབ་པར༌[^3507]བྱ་བ་ཡིན༌[^3508]མོད་ཀྱི། དེའི་ཚེ་ན་ཆུས༌[^3509]བཏབ་པ་དེས༌[^3510]རུང་བར་བྱས་པ་ཉིད་དུ་མི་ཆུད་དོ། །

[Block 5115]
ཞག་བདུན་པ་ལ་མེས་རུང་བར༌[^3511]བྱ་བ་མི་སྲིད་དེ་འདིར་གཞུང་ནི་དེ་ལ་ཉམས་སུ་

[Block 5116]
མ་གྲུབ་པ་དང་། མངོན་སུམ་མ་ཡིན་པར་ཐོས་པར་འཕྱ་ཡང་རུང་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་སྙེགས༌པའི་ཕྱིར་རོ། །

[Block 5117]
འདིར་གཞུང་ནི་ཚེ་དང་ལྡན་པ་ཉེ་དགའ་དང་ལྷན་ཅིག་ཏུ་འདུ་འཛིའི་གཏམ་གྱི་ཕྱིར་འཁོད་པ་ན་ཚེ་དང་ལྡན་པ་གྱད་བུ་ནོར་ཕྱོགས་དེར་སོང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5118]
གཞོགས་འཕྱས་ཞེས་བྱ་བ་ནི་གང་གི་དོན་དུ་འཕྱ་བ་དེའི་མིང་ནས་འབྱིན་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5119]
ལྟུང་བ་ཇི་ལྟ་བུ་དང་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་ལ་འདིར་འདི་རྣམས་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན་བགྲངས་པ་ལ་ནི་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མངོན་སུམ་དུ་འཕྱ་བ་དང་གཞོགས་འཕྱས་བྱེད་པ་འཕངས་པ་ཉིད་ཀྱིས་གལ་ཏེ་འདི་བགྲང་བར༌[^3512]གྱུར་ཅིག༌[^3513]འཕྱ་བ་དང་གཞོགས༌[^3514]འཕྱས་བྱེད་ན་དེ་ནས་གང་ཟག་འདི་ལ་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 5120]
མ་བགྲངས་པ་ལ་གཞན་དུ་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5121]
ཅུང་ཟད་ཙམ་ཡང་དང་དུ་ལེན་པར་མི་ནུས་པ་ལ་ནི་བརྗོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཅུང་ཟད་ཙམ་ཡང་དང་དུ་ལེན་པར་མི་ནུས་པའི་གང་ཟག་ལ་བསྐུལ་བ་དྲན་པ་བྱ་བ་ལ་སོགས་པས་ཅུང་ཟད་ཙམ་ཡང་བརྗོད་པར་མི་བྱའོ། །

[Block 5122]
གཞན་ལ་འཕྱ་བ་དང་གཞོགས་འཕྱས་བྱེད་པའི་རྣམ་པས་གང་ཞིག་བརྗོད་པ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 5123]
ཞེ་སྡང་བར་གྱུར་པ་དེ་རང་གིས༌[^3515]ལས་སུ་བསྐོ་བར༌[^3516]མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཅུང་ཟད་ཙམ་ཡང་དང་དུ་ལེན་པར་མི་ནུས་པའི་གང་ཟག་གང་ཡིན་པ་དེ་ཞེ་སྡང་བར་གྱུར་ཅིང་མི་དགའ་བར་གྱུར་ན་དེ་དགེ་འདུན་གྱིས་ལས་སུ་བསྐོ་བར་མི་བྱ་སྟེ་བརྒྱུད་པས་ནི་བསྐོ་བར་བྱའོ། །

[Block 5124]
འཕྱ་བའོ། །

[Block 5125]
གླེང་བར་གཏོགས་པའི་བསྒོ་བ༌[^3517]ཚིག་གིས་རྣ༌[^3518]ལ་གཟོན་པ་དང་། ཅང་མི་སྨྲ་བས་རྣ༌[^3519]ལ་གཟོན་པ་དང་། གང་ཟག་བསྟན་པ་རྣམས་ལ་ངོར་འཕྱ་བ་དང་། ཟུར་གྱིས་གཞོགས་འཕྱས་བྱེད་པ་གསོལ་བར༌[^3520]མི་བགྲང་བར་མི་བྱའོ་ཞེས་པ་ནི་གླེང་བར་གཏོགས་པའི་བསྒོ་བའི༌[^3521]ཚིག་གིས་རྣ་ལ་གཟོན་པ་དང་། ཅང་མི་སྨྲ་བས་རྣ་ལ་གཟོན་པ་དང་། གང༌[^3522]ཟག་བསྟན་པ་རྣམས་ལ་ངོར་འཕྱ་བ་དང་ཟུར་གྱིས་གཞོགས༌[^3523]འཕྱས་བྱེད་པ་དང་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 5126]
ཟས་ལ་བསྐོ་བ་ལ་སོགས་པའི་གང་ཟག་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 5127]
ད་ལྟར་བྱུང་བ་ལ་འདི་ནི་ངེས་པར་བྱེད་པ་སྟེ། བགྲང་བར་བྱ་བ༌[^3524]ནི་ངེད་ཀྱིས་ཁྱོད་ཀྱི་སྤྱོད་པ་དམ་པ་མ་ཡིན་པ་འདི་འདྲ་བར་ཤེས་ཏེ། ཁྱོད་གང་ཟག་སྤྱོད་པ་དམ་པ་མ་ཡིན་པ་དང་ལྡན་པ་དེ་ལྟ་བུ་དག་གི་ནང་དུ་བཅུག་གོ་ཞེས་ཁྲེལ་མེད་པ་རྣམ་པ་དེ་ལྟ་བུ་ཉིད་ཀྱི་གྲངས་སུ་དེ་དག་བགྲང་བའོ། །

[Block 5128]
དེ་བས་ན་དེ་དག་བགྲང་བ་ལ་བཏང་སྙོམས་བྱ་བ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 5129]
གླེང་བར་གཏོགས་པ་ནི་ཚིག་ཏུ་གྱུར་པ་གོ་བར་བྱེད་པའོ། །

[Block 5130]
གླེང་བར་གཏོགས་པའི་བསྒོ་བ༌[^3525]གླེང་བ་པོས་བྱ་བའི་དྲི་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5131]
རྣ་ལ་གཟོན་པ་ནི་རྣམ་པ་གཉིས་དག་གིས་ཏེ། ཚིག་གིས་ལེན༌[^3526]འདེབས་པ་ལ་སོགས་པས་གང་ཞིག་བཟློག་པ་དང་ཅང་མི་སྨྲ་བའི་ངོ་བོས་སོ། །

[Block 5132]
དེ་ལ་གླེང་བར་གཏོགས་པའི་གང་ཞིག་གླེང་བ་དང་འབྲེལ་བའི་བསྒོ་བ་རྣ་ལ་གཟོན་པར་བྱེད་པ་དེ་ནི་འདིར་རྣ་ལ་གཟོན་པ་པོར་རིག་པར་བྱའོ། །

[Block 5133]
གང་ཞིག་ཅང་མི་སྨྲ་བའི་ཚུལ་གྱིས་རྣ་ལ་གཟོན་པར་བྱེད་པ་དེ་ནི་ཅང་མི་སྨྲ་བའི་ཚུལ་གྱིས་རྣ་ལ་གཟོན་པའོ། །

[Block 5134]
གང༌[^3527]ཟག་བཅུ་གཉིས་གསུངས་པ་དེ་རྣམས་ལ་གང་ཞིག་མངོན་སུམ་དུ་འཕྱ་བར་བྱེད་པ་དེ་ནི་གང་ཟག་བརྗོད་པ་ལ་མངོན་སུམ་དུ་འཕྱ་བར་བྱེད་པའོ། །

[Block 5135]
འདིར་མངོན་སུམ་གྱི་སྒྲས་ནི་མིང་ནས་འབྱིན་པའོ། །

[Block 5136]
གང་ཟག་འདི་རྣམས་ཉིད་ནི་ཟུར་གྱིས་གཞོགས་འཕྱས་བྱེད་པས་གང་གིས་སྐུལ་བར༌[^3528]བྱེད་པས་དེ་ནི་ཟུར་གྱིས་གཞོགས་འཕྱས་བྱེད་པས་སོ། །

[Block 5137]
གང་ཞིག་གོ་བར་བྱེད་པ༌[^3529]ནི་འདིར་འཕྱ་བའོ། །

[Block 5138]
མིང་ནས་མི་འབྱིན་པ་ཉིད་ཀྱིས་འཕངས་པའོ། །

[Block 5139]
འདི་རྣམས་ནི་གསོལ་བའི་ལས་ཀྱིས་བགྲང་བར་བྱའོ། །

[Block 5140]
བསྒོ་བ་རྣ་ལ་གཟོན་པ་ཉིད་དང་། ཅང་མི་སྨྲ་བས་རྣ་ལ་གཟོན་པ་ཉིད་དང་མངོན་སུམ་དུ་འཕྱ་བར་བྱེད་པ་དང་། ཟུར་གྱིས་གཞོགས་འཕྱས་བྱེད་པ་འཕངས་པ་ཉིད་ཀྱིས་གྲངས་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 5141]
ཅི་ཞིག་བྱས་ན་བསྒོ་བ་རྣ་ལ་གཟོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་བསྒོ་བ་རྣ་ལ་གཟོན་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5142]
བསམ་པ་ཇི་ལྟ་བུས༌[^3530]ཤེ་ན། འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5143]
རྣ་ལ་གཟོན་པར་འདུན་པ་སྟེ་གཞན་དུ་ན༌[^3531]ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 5144]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་གཞན་བརྗོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྒོ་བ་མ་ཡིན་པ་དང་འདྲ་བའི་དོན་གྱི༌[^3532]ཚིག་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5145]
ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བའི་ཕྱིར་འདིར་ཐམས་ཅད་དུ་དགེ་སློང་གིས་བསྒོ་བ་ཐམས་ཅད་དུ་རྣ་ལ་གཟོན་པ་ལ་ཐ་ན་འགྲོ་བ་ཡོངས་སུ་འདྲི་བའི་བདག་ཉིད་ཅན་ལ་དངོས་གཞི་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 5146]
དེ་ལྟར་ཡང་གཞུང་ནི་འདི༌[^3533]རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་གིས་ཇི་ཙམ་དུ་གཞན་འདྲི་བ་ལ་ལན་འདེབས་ན་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5147]
གཞན་འདྲི་བ་ལ་དོན་གཞན་བརྗོད་པ་ནི་གཞན་བརྗོད་པའོ། །

[Block 5148]
རྟོག་པ༌[^3534]ཡོད་པ་ལ་དོན་གཞན་གྱིས་ནི་དངོས་ཏེ།

[Block 5149]
དེ་ལྟར་ཡང་གཞུང་ནི་ཞུ་བ་ལས།

[Block 5150]
དབུས་པའི་ཚིག་གིས་མཐའ་འཁོབ་པ་ལ་འམ། མཐའ་འཁོབ་པའི་ཚིག་གིས་དབུས་པ་ལ་མཐའ་གཞན་དང་གཞན༌[^3535]བརྗོད་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
