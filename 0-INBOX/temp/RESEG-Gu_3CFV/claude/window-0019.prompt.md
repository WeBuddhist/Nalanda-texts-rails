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
[Block 666]
ལྕི་སྐམ་མམ་ལྕི་བའམ་ས་གང་ཡང་རུང་བ་ལན་གསུམ་བཀྲུས་པ་ལ་སྣུམ་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 667]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་གིས༌[^389]ལྷུང་བཟེད་ལྕི་སྐམ་མམ་ལྕི་བའམ་སས་ལན་གསུམ་འཁྲུ་བར་བགྱིད་ཅིང་དེ་ཡང་སྣུམ་ཞིང་སྣུམ་བག་ཆགས་པར་གྱུར་ན་ཡོངས་སུ་ལོངས་སྤྱད་པར་བགྱི་འམ། ཉེ་བ་འཁོར་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ཐ་སྙད་དུ་བྱ་བའི་རིན་མི་ཆོག་པའི་ཕྱིར་རོ། །

[Block 668]
འདིར་ལྕི་སྐམ་ལ་སོགས་པ་གསུམ་པོ་འདི་དཔེ་ཙམ་དུ་ཟད་ཀྱི་གཞན་དག་ཀྱང་རུང་བར་རིག་པར་བྱའོ། །

[Block 669]
ལངས་པ་བསལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་དེ་ལྷུང་བཟེད་དག་པར་བྱས་པ་ལ་སྣུམ་བག་གམ་ཚོན་རྩིའི་བག་སྐོ་ལ་སོགས་པ་དག་ཕྲད་པས་ལངས་པར་གྱུར་ན་བསལ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 670]
འདིར་གཞུང་ནི་དགེ་སློང་ཞིག་ལ་ལྷུང་བཟེད་འཕྲེན་ཆེན་ཞིག་ཡོད་ནས། དེས་དེར་ཁུ་བ༌[^390]བྱིན་ལེན་བྱས་པ་ན་སྣུམ་བག་འཐོན་ཅིང་སྟེང་དུ་ཞག་ཉ་མིག་ཆགས༌[^391]ཤིང་འདུག་ནས་དགེ་སློང་དེ༌[^392]འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྟེང་གི་སྣུམ་བསལ་ཏེ་བཏུང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 671]
འབགས་པའི་ཕྱོགས་ཉི་ཚེ་བཀྲུ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ཉི་ཚེ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཀྱི་ཕྱོགས་གང་དུ་འབགས་པར་གྱུར་པའི་ཕྱོགས་དེའོ། །

[Block 672]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ལྷུང་བཟེད་འཕྲེན་ཅན་ཞིག་དེས་འཁྲུ་བར་བྱེད་པ་ན་འཕྲེན་རེར་འབྲས་ཆན་གྱི་དུམ་བུ་སོང་བ་ཞིག་མཐོང་ནས་དེ་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཤིང་བུས་བྲུད་དེ་ཆུས་ལན་གཉིས་སམ་གསུམ་བཤལ་ནས་ཡོངས་སུ་སྤྱད་པར་བྱ་སྟེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 673]
བུམ་པ་ལ་སོགས་པ་སྣུམ་ཅན་དག་སྣུམ་མེད་པར་བྱ་བའི་ཕྱིར་ཆུའི་རྫིང་བུ་ཟབ་མོའི་ནང་དུ་གཞུག་གོ། །

[Block 674]
ཉའམ་རུས་སྦལ་ལམ་སྦལ་པའམ་ཆུ་སྲིན་བྱིས་པ་གསོད་དམ་ཉ་ཁྱི་བ་དག་གིས་མ་ལུས་པར་ལྡོགས་ཀྱི་བར་དུ་གཞག་གོ། །

[Block 675]
བསྲེགས་པས་ཀྱང་སྣུམ་མེད་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་མ་ལུས་པར་ལྡོགས་པ་དང་བསྲེག་པ་དག་གིས་སྣུམ་མེད་པར་འགྱུར་བའི་བུམ་པ་ལ་སོགས་པ་དག་ཇི་ལྟར་དག་ཅིང་གཙང་བ་ཉིད་དུ་བྱ་ཞེ་ན། དེའི་ཕྱིར་སྣུམ་མེད་པར་གྱུར་པ་ནི་བཀྲུས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་དང་འདི་འབྲེལ་ཏེ། གང་གིས༌[^393]བཀྲུ་ཞེ་ན། དེའི་ཕྱིར་ལྕི་སྐམ་མམ་ལྕི་བས་དག་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐོ་རངས་ཀྱི་ཆུ་འམ་ལྕི་བས་དག་པ་སྟེ་སྣུམ་མེད་པར་གྱུར་པ་ནི་དག་པ་ཉིད་དོ། །

[Block 676]
ལན་ཚྭ་ལ་སོགས་པ་ཚྭ་ཆུ་དང་འགྱུར་བྱེད་ཀྱི་ཆུ་དང་རྙོག་ཆུར་གྱུར་པ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལན་ཚྭ་དང་འགྱུར་བྱེད་དང་། རྙོག་པ་དག་ལས་ཚྭ་ཆུར་གྱུར་པ་དང་འགྱུར་བྱེད་ཀྱི་ཆུར་གྱུར་པ་དང་རྙོག་པ་རྙོག་ཆུར་གྱུར་པ་འཐུང་བ་ནི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 677]
དེ་ནི་ཐམས་ཅད་ལ་དུས་མ་ཡིན་པར་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལན་ཚྭ་ལ་སོགས་པར་གྱུར་པ་དེ་ནི་རུང་བ་ཉིད་དེ་ནད་པ་མ་ཡིན་པ་ཐམས་ཅད་ཀྱིས་ཀྱང་ངོ་། །ལན་ཚྭ་དང་འགྱུར་བྱེད་རང་གི་བྱ་བ་མི་བྱེད་པ་དག་ལ་ནི་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ཕྱེད་ཉིད་ཀྱང་མེད་པ་ཉིད་དེ། དེ་ལ་ནི་ལྟུང་བ་མེད་པ་ཁོ་ན་སྟེ། ཉེས་བྱས་ཀྱི་ལྟུང་བ་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 678]
འདིར་ཐམས་ཅད་ལ་ལན་ཚྭ་དང་འགྱུར་བྱེད་ཅེས་སྨོས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་པར་རིག་པར་བྱའི་ཉེ་བར་སྒྲུབ་པ༌[^394]ནི་མ་ཡིན་ནོ། །

[Block 679]
ཉེ་བར་བསྒྲུབས་པ༌[^395]དེ་ལ་འབྱུང་ཁུང་གི་དབང་གིས་འབྱུང་ཁུང་དག་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^396]འདི་ནི་ཆོ་གའོ། །

[Block 680]
གཞན་ལ་ཐ་སྙད་བཏགས་པར༌[^397]འགྱུར་བ་མ་ཡིན་པ་ལ་ཡང་ཉེས་པ་ཡོངས་སུ་རྫོགས་པ་ལ་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 681]
གང་ལ་གནས་པ་ལ་ཡང་དང་བ་འབྱུང་བར་འགྱུར་བའི་དུས་ཀྱིས་བར་དུ་ཆུས་དག་པ་དེའི་ཚེ་ནི༌[^398]ལྷན་ཅིག་སྐྱེས་པ་མ་ཡིན་ཡང་ལྷན་ཅིག་སྐྱེས་པ་ཉིད་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 682]
འདིར་ཕྱེད་ཉིད་ཀྱི་གཞུང་ནི་ཞུ་བ་ལས།

[Block 683]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ཆབ་དབོན་ཚ་ཅན་དུ་བགྱིས་པ་གསོག་འཇོག་བགྱིས་ཏེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ། །

[Block 684]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས༌[^399]ཆབ་དབོན་ཚ་ཅན་དུ་བགྱིས་ནས༌[^400]བྱིན་ལེན་མ་བགྱིས་པ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ། །

[Block 685]
འདིར་ནི་སྔ་རོལ་དུ་ཡང་དབོན་ཚ་ཅན་དུ་བགྱིས་པ་ཞེས་བྱ་བའི་ཚིག་ནི་གང་གིས་ཤེས་བྱེད་ཡིན་སྙམ་དུ་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། ལྷན་ཅིག་སྐྱེས་པ་ལ་ཡང་སྦྱོར་བ་འདི་ཡོད་པའི་ཕྱིར་རོ། །

[Block 686]
གང་གི་ཕྱིར་རང་བཞིན་གྱིས་ཀྱང་དབོན་ཚ་ཅན་གྱི་ཆུ་ནི་དབོན་ཚ་ཞེས་བྱ་བར་སྨྲ་བ་ཡིན་ཏེ། ཉམས་པ་འདི་ལ་ཡང་དབོན་ཚ་ཅན་དུ་བྱས་པ་ཞེས་བྱ་བ་རང་བཞིན་ཡིན་ནོ། །

[Block 687]
འདིར་ཡང་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ཆབ་འགྱུར་བྱེད་ཅན་དུ་བྱས་པ་བྱིན་ལེན་མ་བྱས་པར་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 688]
འགྱུར་བྱེད་ཅན་དུ་བགྱིས་པའི་ཚིག་ཀྱང་དབོན་ཚ་ཅན་དུ་བྱས་པའི་སྤྱོད་པས་བསལ་ཟིན་ཏོ། །

[Block 689]
རྙོག་པ་ཅན་གྱི་གཞུང་ཡང་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ཆབ་རྙོག་པ་ཅན་བྱིན་ལེན་མ་བྱས་པར་འཚལ་ན་ལྟུང་བར༌[^401]ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 690]
ཐ་མ་ལ་ནི་གཟུགས་བརྙན་བྱུང་ནའོ་ཞེས་བྱ་བ་ནི་ལན་ཚྭ་ཅན་དང་འགྱུར་བྱེད་དག་གི༌[^402]ཐ་མ་ནི་རྙོག་མ༌[^403]ཅན་གྱི་ཆུར་གྱུར་པ་ཉིད་ཀྱིས༌[^404]བཞིན་གྱི་གཟུགས་བརྙན་འབྱུང་བ་ཡོད་པ་ལ་མེད་པ་ཉིད་དོ། །

[Block 691]
ཀ་ཏ་ཀའི་འབྲས་བུས་ཆུ་ཤིན་ཏུ་དང་བར་འགྱུར་རོ། །

[Block 692]
འགྱུར་བྱེད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དང་བར་འགྱུར་བའོ། །

[Block 693]
ཟན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རྫས་གཞན་འདིས་དང་བར་འགྱུར་བའོ། །

[Block 694]
དེ་མི་འཇིག༌[^405]པར་བྱ་བའི་ཕྱིར་སྣུམ་གྱིས་བསྐུའོ་ཞེས་བྱ་བ་ནི་གཞུག་པར་བྱ་བའི་ཟན་དེས་ཆུ་ཤིན་ཏུ་དང་བར་འགྱུར་རོ། །

[Block 695]
དེ་ལྟར་མ་ཞུགས་པ་ལ་འབྱུང་ཁུང་དུ་བཏབ་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 696]
དེ་བས་ན་འདི་ལ་ཐ་སྙད་དུ་གྱུར་པ་ཉིད་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ནི་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 697]
འབྱུང་ཁུང་དག་ཏུ་བཏབ་པ་མི་མངོན་པ་ནི་ཡོད་པའི་གྲངས་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མང་པོ་འདུས་པ་དག་ཁྲོན་པ་དག་ཏུ་ལྷུང་བཟེད་དག་འཁྲུ་བར་བྱེད་པ༌[^406]ན། ཀུན་དགའ་ར་བ་པ་དང་དགེ་བསྙེན་དག་གིས་དེ་དག་ཏུ་མར་སར་དང་འབྲུ་མར་དང་ཞོ་དང་སྦྲང་རྩིའི་བུམ་པ་དག་འཁྲུ་བར་བྱེད་པས་སྟེང་དུ་སྣུམ་གྱི་ཉ་མིག་ཆིལ་ཆིལ་པོ་དག་ཆགས་པར༌[^407]གྱུར་ནས། དགེ་སློང་དག་འགྱོད་པ་སྐྱེས་ནས་མི་འཐུང་བའི༌[^408]སྐབས་དེ་དགེ་སློང་དག་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་དག་དེ་དག་གིས་འབགས་པ་དེས་ཟས་ཀྱི་བྱ་བ་བྱར་མི་རུང་གི༌[^409]བསལ་ལ་བཏུང་བར་བྱ་སྟེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 698]
ཕྱོགས་གཅིག་ཏུ་འདྲེས་པར་གྱུར་ན་དེ་ཉིད་ཉི་ཚེ་བསལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་འདི་འདྲེས་པར་གྱུར་པའི་ཕྱོགས་དེ་ཉིད་ལའོ། །

[Block 699]
ཁྭའི་མཆུས༌[^410]རེག་པ་ལ་ནི་ཐན་སྐོར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་རེག་པའི་ཕྱོགས་དེ་ཉིད་དང་དེའི་ཐན་སྐོར་ཡང་བསལ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 700]
འོ་ན་མདོ་སྔ་མ་ཤོས་ཀྱི་དགོངས་པ༌[^411]མེད་དམ་ཞེ་ན་མ་ཡིན་ཏེ། འདིར་ཐམས་ཅད་མི་རུང་བར་འགྱུར་བར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་དེ་ལ་འདི་བསྟན་གྱི་ལྷག་མ་ལ་ནི་མ་ཡིན་ཏེ་བཙོག་པ༌[^412]ཉིད་སྤང་བའི་ཕྱིར་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ། དེ་བས་ན་དོན་འདི་བརྗོད་པའོ། །

[Block 701]
དེ་དང་འབྲེལ་པའི་རྒྱུན་གྱིས་རེག་པ་ནི་དེ་ལ་རེག་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་དང་འབྲེལ་པའི་རྒྱུན་ལ་རེག་པ་དེ་འོ་མ་ལ་སོགས་པ་དེ་ལ་དེར་རེག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 702]
ནོར་བ་དང་བརྗེད་པས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རེག་པ་ལ་རེག་པ་ཉིད་དོ། །

[Block 703]
དེ་གཉིས་ཀྱིས་སྤོས་པ་གཞག་པའི་ཕྱིར་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནོར་བ་དང་བརྗེད་པ་དེ་ཉིད་ཀྱིས་སྤོས་པ་ཕྱིར་གཞག་པར་བྱ་བའི་དོན་དུ་རེག་པ་ཡང་རེག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 704]
གནས་ཀྱི་ཐག་ཤིན་ཏུ་ཉེ་བར་བསྐུར་རོ་ཞེས་བྱ་བ་ནི་གནས་གང་དུ་བར་སྐབས་ཀྱི་ཐག་ཤིན་ཏུ་ཉེ་བ་ཡོད་པ་དེར་སྤོང་བ་ལ་ཉེ་བར་བསྐུར་བར་བྱའོ། །

[Block 705]
གནས་ཀྱི་ཐག་ཤིན་དུ་རིང་བར་ཁྱེར་ན་དེ་ལ་རྗེས་སུ་གནང་བ་ཉིད་ཀྱི་ཕྱིར་རེག་པ་ཉིད་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
