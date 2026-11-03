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
ཀུན་ཏུ་ཆགས་པར་གྱུར་ན་ཞལ་ཏ་བྱེད་པ་མོས་རྗེས་སུ་བསྟེན་པར༌[^468]བྱའོ། །

[Block 667]
དྲན་པ་ཉེ་བར་ཞོག་ཅིག །ཅི་རྣག་གི་ལུས་འདི་ལ་སྙིང་པོ་ཡོད་དམ་ཞེས་སོ་ཞེས་བྱ་བ་ལ། ཀུན་ཏུ་ཆགས་པར་གྱུར་ན་ཞེས་བྱ་བ་ནི་འབྲེག་མཁན་ལ་དགེ་སློང་མ༌[^469]དེའོ། །

[Block 668]
འབྲེག་མཁན་ལ་ནི་མ་དང་སྲིང་མོ་དང་བུ༌[^470]མོའི་འདུ་ཤེས་ཉེ་བར་ཞོག་ཅིག་ཅེས་སོ་ཞེས་བྱ་བ་ལ། ཀུན་དུ་ཆགས་པར་གྱུར་པ་ལ་ཞལ་ཏ་མོས་མ་ལ་སོགས་པའི་འདུ་ཤེས་ཉེ་བར་ཞོག་ཅིག་ཅེས་བྱ་བ་ལ༌[^471]ཡང་དག་པར་རྗེས་སུ་བསྟན་པར་བྱའོ། །

[Block 669]
དེ་བྱས་ནས་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་དེ་ཞེས་བྱ་བ་ནི་སྐྲ་དང་ཁ་སྤུ་བྲེག་པ་ལའོ། །

[Block 670]
ཡང་ན་ཡན་ལག་ལྔའི་ཁྲུས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ན་ཞེས་བྱ་བའི་སྒྲ་ནི་ཆོ་ག་གཞན་བསྟན་པའི་དོན་ཏོ། །

[Block 671]
ཆུ་ཡོད་པ་ལ་འདི་བརྟག་པ་ཉིད་ཡིན་ཏེ། འདིར་གཞུང་ནི་དགེ་སློང་གིས་སྐྲ་བཟེད་བཅང་བར་བྱ་ཞིང་ཁྲུས་ཀྱང་བྱ་སྟེ། ཐ་ན་རྐང་ལག་དག་ཀྱང་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 672]
སྒྲེན་མོར་ཁྲུས་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ལྟར་འཁོར་གསུམ་གཡོགས་པ་ཉིད་ཡོངས་སུ་རྫོགས་པ་ཉིད་ནི་སྒྲེན་མོ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 673]
ཇི་སྲིད་དུ༌[^472]འཁོར་གསུམ་གཡོགས་པ་ལ་ཡན་ལག་ལས་སྐྱེས་པའི་སྤུ་དག་གཡོགས་པ་ཉིད་ནི་དེ་སྲིད་དུ་གཡོགས་པ་ཉིད་ཀྱིས་ཐམས་ཅད་ལ་སྤང་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་འདི་ནི་འདིར་ཤུགས་ཀྱིས༌[^473]རྟོགས་པར་བྱའོ། །

[Block 674]
དགེ་སློང་མས་སྐྱེས་པའི་ཆུ་ངོགས་སུ་མི་བྱའོ། །

[Block 675]
བུད་མེད་ཀྱི་ཆུ་ངོགས་སུ་ཡང་ཕྱེ་མས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྐྱེས་པ་རྣམས་ཀྱི་ཆུ་ངོགས་སུ་དགེ་སློང་མས་ཁྲུས་བྱས་པ༌[^474]ཉིད་བཀག་པའོ། །

[Block 676]
བུད་མེད་ཀྱི་ཆུ་ངོགས་སུ་ནི་སྲན་ཆུང་གི་ཕྱེ་མ་ལ་སོགས་པས་ཁྲུས་བྱ་བ་བཀག་པར་མཛད་ཀྱི་ཁྲུས་ཉི་ཚེ་ནི་མ་བཀག་གོ། །

[Block 677]
འདིར་གཞུང་ནི་བཅུ་གཉིས་སྡེ་རྣམས་བུད་མེད་ཀྱི་ཆུ་ངོགས་སུ་ཁྲུས་བྱེད་པར་གྱུར༌[^475]ཏེ། ཁྱིམ་བདག་གི་བུད་མེད་ཁྲུས་བྱེད་པ་རྣམས་ལ་ང་རྒྱལ་བྱེད་ཅིང་མོན་སྲན་གྲེའུའི་ཕྱེ་མ་ལ་སོགས་པ་ཡང་འདོར་བར་བྱེད་དེ་ཞེས་བྱ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མ་བུད་མེད་ཀྱི་ཆུ་ངོགས་སུ་ཕྱེ་མས་ཁྲུས་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 678]
མོན་སྲན་གྲེའུ་ལ་སོགས་པའི༌[^476]ཕྱེ་མའི་དྲིས་བསྒོས་པ་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ནི༌[^477]ཐམས་ཅད་དུ་དབང་དུ་བྱེད་པའོ། །

[Block 679]
དེ་ནི་བླང་བར༌[^478]བྱའོ། །

[Block 680]
ནད་པས་ནི་སྨན་གྱི་དགོས་པ༌[^479]ཡང་ངོ་ཞེས་བྱ་བ་ནི་རུང་ངོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་མཐུན་ནོ། །

[Block 681]
དགེ་སློང་མས་བུད་མེད་ལ་ཕྱེ་མས་མི་གཏོར་རོ་ཞེས་བྱ་བ་ནི་ཁྲུས་ཀྱི་དུས་སུ་འམ་དུས་གཞན་ལ་ཡང་ཞེས་བྱ་བ་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བ་སྒྲེན་མོ་ཉིད་བསལ་བ་ཞར་ལ་བསྒྲུབ་པ༌[^480]བརྗོད་པ་ཡིན་ནོ། །

[Block 682]
ཤམ་ཐབས་ཀྱི་མཐའ་མ་ཉིད་ཀྱི་མདུན་དང་རྒྱབ་ཀྱི་མཐའ་མ་མ་མདུད་པར་སྐས་ལ་མི་འཛེག་གོ་ཞེས་བྱ་བ་ནི་ཤམ་ཐབས་ཀྱི་གོས་ཀྱི་མཐའ་མ༌[^481]རྒྱབ་དང་འོག་མ་ནི་འོག་ནས་འབྱུང་བའི་མཐའ་མ་གང་གིས་ན༌[^482]མདུད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 683]
འདི་ནི་སྨད་དཀྲིས་མཐོང་བ་ཡོངས་སུ་སྤང་བའོ། །

[Block 684]
ཤིང་ལ་སོགས་པ་ལ་འཛེག་པ་ཡང་སྨད་དཀྲིས་མཐོང་བ་བསྒྲུབ་པ་ཡིན་ནོ། །

[Block 685]
དེ་བས་ན་སྐབས་ཀྱི་ཚིག་ནི་འདིར་དཔེ་ཙམ་དུ་རྟོགས་པར་བྱའོ། །

[Block 686]
རྒུད་པའི་དུས་སུ་འཛེག་པ་ལ་གསོ་བའི་དོན་དུ་འཛེག་པ་གང་ཞིག་གལ་ཏེ་ཤམ་ཐབས་དེ་ལ་འདི་ལྟར་མདུད་པས་ཉེ་བར་བཀག་པ་མིན་ནས་དེ་ལ་སྲུང་བ༌[^483]ཉིད་དོ། །

[Block 687]
གལ་ཏེ་མ་ཡིན་ན་མ་ཡིན་ཞེས་བྱ་བ་ཤིང་ལ་འཛེག་པ་གནང་བས་རྗེས་སུ་རྟོགས་པར་བྱའོ། །

[Block 688]
གཞན་གྱི་དུས་སུ་དེ་ལྟར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྐས་ལ་འཛེག་པ་ལས་དུས་གཞན་དུ་ཤམ་ཐབས་ཀྱི་མཐའ་མ་ཉིད་ཀྱི་མདུན་དང་རྒྱབ་ཀྱི་མཐའ་མདུད་པས༌[^484]གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 689]
ཁའི་ནང་ཡང་སྨད་དཀྲིས་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་ཀྱི་ཕྱོགས་འདི་ལ་དེ་སྒྲེན་མོ་ཡོངས་སུ་སྤང་བ་བརྗོད་པ་ཡིན་ཏེ། ཁ་མ་བཀག་པར༌[^485]གདངས་པར༌[^486]མི་བྱའོ་ཞེས་བྱ་བ་ལ། གོས་ལ་སོགས་པས་ཁ་མ་བཀབ་པར་གདངས་པ་གང་ཞིག་དེ་ནི་བསྟེན་པར་མི་བྱ་སྟེ། འདིར་གཞུང་ནི་དགེ་སློང་གླལ་བར་གྱུར་པས་ཁ་ལ༌[^487]ལག་པས་དགབ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 690]
འདིར་དཔེ་ནི་ལག་པ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 691]
གླལ་བ་ཡང་འདོད་པ་བཞིན་དུ་བྱ་བ་སྟེ། གང་རྣམ་པར་གསལ་བའི༌[^488]སླད་དུ་དེའི་དབང་དུ་བྱས་ནས་འདི་གསུངས་པ་ཡིན་ཏེ། ནུས་པ་མེད་པ་ལ་གང་ཞིག་ཁ་ཕྱེ་བ་དེ་བསྟེན་པ་ལ་སྐྱོན་མེད་དོ། །

[Block 692]
ཁྲུས་རས་བཅང་བར་བྱའོ། །

[Block 693]
ཉི་རིམ་ལ་ནི་སྲོག་ཆགས་དག་ཀུན་དུ་འཆགས་སོ་ཞེས་བྱ་བ་ལ༌[^489]བརྗོད་པར་བྱ་བ་ལ་ཀུན་དུ་ཞེས་བྱ་བ་ནི་གཞུང་མཛེས་པ་སྒྲུབ་པའི་ཕྱིར་ཉེ་བར་བཟུང་བ་སྟེ་འདི་ནི་རྒྱུ་མཚན་བསྟན་པ་ཡིན་ནོ། །

[Block 694]
གང་གི༌[^490]ཕྱིར༌[^491]ཉི་རིམ་ལ་སྲོག༌[^492]ཆགས་རྣམས་འཆགས་པར༌[^493]གྱུར་པ་དེའི་ཕྱིར་སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་དེ་ལྟ་བུའི་གོས་ཀྱིས་ཁྲུས་མི་བྱའོ་ཞེས་བྱ༌[^494]བའི་དོན་ཏོ། །

[Block 695]
ཆོས་གོས་གསུམ་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཁྲུས་རས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 696]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག༌[^495]སློང་ཆོས་གོས་གསུམ་པས་ཀྱང༌[^496]ཁྲུས་རས་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 697]
ཁ་ཅིག་ནི་བྱིན་གྱིས་མ་བརླབས་པར་ཡང་གཟུང་བར་བྱ་ཞེས་ཟེར་ཏེ། དེ་ནི་མི་རིགས་སོ། །

[Block 698]
བདག་གིས་ཁྲུས་རས་ཞེས་བྱ་བ་ཀུན་དུ་རྟོག་པ༌[^497]མ་སྐྱེས་པ་རང་བཞིན་གྱིས་ལྡང་བའི་ཕྱིར་ངེས་པར་ཀུན་དུ་རྟོག་པ༌[^498]འདི་འདིར་བསྐྱེད་པར་བྱའོ། །

[Block 699]
འདིར་ཡང་བསྐྱེད་པ་ལ་ཡིད་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་འདིར་སྐྱེ་བ་ཡིན་ཏེ། དེ་བས་ན་བྱིན་གྱིས་བརླབ་པ་གཞན་ལ་བྱ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 700]
ངག་གིས་བྱིན་གྱིས་བརླབ་པ་ཤིན་ཏུ་བདེ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 701]
གནང་བ་འདི་ཉིད་ལས་ནི་འདིས་ཡང་དག་པར་བླངས་པ་འདི་ལས་ཉམས་པར་འགྱུར་བ་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར༌[^499]བྱའོ། །

[Block 702]
མེད་ན་མདུན་དང་རྒྱབ་ནས་ལོ་མ་དག་གིས་གླན་ལ་དབེན་པའི་ཕྱོགས་སུ་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་དུ་ཆོས་གོས་གསུམ་པ་ཉིད་ནི་མ་ཡིན་ཏེ། འདིར་གཞུང་ནི། གཞན་རྣམས་ལ་ཁྲུས་རས་ཀྱི་རྙེད་པ་མེད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་རྣམས་ཀྱི་མདུན་དང་རྒྱབ་ནས་ལོ་མ་རྣམས་ཀྱིས༌[^500]གླན་ལ་དབེན་པའི་ས་ཕྱོགས་སུ་ཁྲུས༌[^501]བྱའོ་ཞེས་བྱ་བ་ཁྱད་པར་མེད་པར་གསུངས་པ་ཡིན་ནོ།[^502] །སྲོག་ཆགས་ཆགས་ན་བཤལ་བས་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་རིམ་པ་གཅིག་ལས༌[^503]ཉི་རིམ་ལ་སྲོག༌[^504]ཆགས་ན་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པའོ། །

[Block 703]
ལྷན་པ་ཅན་ཡང་ཉི་རིམ༌[^505]མེད་པ་མ་ཡིན་ནོ། །

[Block 704]
དེ་བས་ན་འདིས་སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་ཁྲུས་མི་བྱའོ་ཞེས་བྱ་བ་འདིར་གནས་པར་རིག་པར༌[^506]བྱའོ། །

[Block 705]
དེ་གཙུག་ལག་ཁང་དུ་ནི་སྟོར་ཁུང་དུའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཙུག་ལག་ཁང་དུ་འདི་ཁྲུས་བྱེད་ན་སྟོར་ཁུང་ཉིད་དུ་བྱ་སྟེ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
