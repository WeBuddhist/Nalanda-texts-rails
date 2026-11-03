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
[Block 736]
ཕྱོགས་དེར་ཞེས་བྱ་བ་ནི་མཆན་ཁུང་གཡས་པའི་ཕྱོགས་དེར་རོ། །

[Block 737]
དེ་ལ་ཞེས་བྱ་བ་དེ་ནི་སྣམ་སྦྱར་དེ་ལའོ། །

[Block 738]
ཁྲུ་ཕྱེད་དང་དོ་དང་མཐོ་གང་ངོ་ཞེས་བྱ་བ་ནི། དེའི་ཚད་ནི་སྲིད་དུ་ཁྲུ་ཕྱེད་དང་དོ་ཞེང་དུ་མཐོ་གང་ངོ་། །ངོས་གཉིས་ཀར་སྐུད་པའི་ཟུངས་ཀྱིས་སྦྱར་རོ་ཞེས་བྱ་བ་ནི་ངོས་གཉིས་ཀར་མཉམ་པར་གླན་པར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^655]དེའི་དོན་རྟོགས་པར་བྱའོ། །

[Block 739]
གཞན་དུ་ནི་གཉིས་ཀ་ལས།

[Block 740]
ངོས་གཉིས་ཀར་གླན་པར་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 741]
སྐུད་པའི་ཟུངས་ཀྱིས་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་སྟེན༌[^656]པས་ནི་མ་ཡིན་ནོ། །

[Block 742]
དུས་དུས་སུ་དེ་བཀྲུ་བ༌[^657]དང་ཁ་བསྒྱུར་བར་བྱའོ། །

[Block 743]
དེའི་དེ་ནི་བཙག་གིས་སོ་ཞེས་བྱ་བ་ནི། གོས་དེའི་ཁ་བསྒྱུར་བ་དེ་ནི་བཙག་གིས་རིགས་པར་བྱའོ། །

[Block 744]
གདོང་ཕྱིས་བཅང་བར་བྱའོ༌[^658]ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་གནས་བརྟན་གྱིས་དྲིས་པ་རུང་རམ།[^659] ཚེ་དང་ལྡན་པ་རྣམས་བདག་ནི་ནད་པས་ཏེ་མི་རུང་ངོ་། །ཅི་ཁྱོད་སྔོན་གདོང་ཕྱིས་བཅང་བར་བྱས་ན་ད་ལྟར་ཅིའི་ཕྱིར་མི་འཆང་། བཅོམ་ལྡན་འདས་ཀྱིས་མ་གནང་ངོ་། །བར་སྐབས་དེར་གསུངས་པ་དེ་བས་ན་གདོང་ཕྱིས་བཅང་བར་བྱའོ་ཞེས་རྗེས་སུ་གནང་བའོ། །

[Block 745]
འདིར་གདོང་ཕྱིས་ནི་ལག་ཕྱིས་ལ་སོགས་པ་དག་གི་དཔེ་ཡིན་ཏེ། ཤིན་ཏུ་མོད་པ་ཉིད་དང་ཤིན་ཏུ་བཟོད་པ་ཞེས་བྱ་བའོ། །

[Block 746]
འདིར་གདོང་པ་ནི་གཙོ་བོ་ཉིད་དུ་བསྟན་པའོ། །

[Block 747]
ལུས་འཛག་པས་རྣག་གཟན་ནོ་ཞེས་བྱ་བ་ནི་བཅང་བར་བྱའོ༌[^660]ཞེས་བྱ་བར་སྦྱར་བར༌[^661]བྱའོ། །

[Block 748]
གང་གི༌[^662]ལུས་ཁྲག་གམ༌[^663]རྣག་འཛག་པ་དེ་ནི་ལུས་འཛག་པ་ཞེས་བྱ་སྟེ། དེས་རྣག་གཟན་བཅང་བར་བྱའོ། །

[Block 749]
དེ་ཆོས་གོས་ཀྱི་ནང་དུ་བགོའོ༌[^664]ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་ལུས་སྤྲུག་པ༌[^665]དེའོ། །

[Block 750]
དབྱར་བ༌[^666]ནི་སྐ་བའི༌[^667]ཆུའམ་སོ་ཕག་གི་ཕྱེ་མ་སྦྱར་བའི་ཆུས༌[^668]སྦངས་ཏེ་དལ་བུས་ཁད་ཀྱིས་འགོགས༌[^669]པར་བྱའོ་ཞེས་བྱ་བ་ལ། སོ་ཕག་གི་ཕྱེ་མ་སྦྱར་ཞེས་བྱ་བ་ནི་ཆུས་སོ། །

[Block 751]
རྣག་དང་ཁྲག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སྐ་བའི༌[^670]ཆུ་དང་སོ་ཕག་གི་ཕྱེ་མ་དང་སྦྱར་བའི་ཆུས་སྦངས་ཏེ་དལ་བུས་ཁད་ཀྱིས་འགོགས་པར༌[^671]བྱའོ། །

[Block 752]
དུས་དུས་སུ་དེ་བཀྲུ་བ་དང་སྐམ་པ་དང་ཁ་བསྒྱུར་བར་བྱའོ་ཞེས་བྱ་བ་ལ༌[^672]དེ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་རྣག་གཟན་ནོ། །

[Block 753]
དེ་ནི་དེའི་བཙག་གིས་བཟང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་རྣག་གཟན་དེ་ཁ་སྒྱུར་བར༌[^673]བྱེད་པ་ནི༌[^674]བཙག་གི་རྡུལ་བུ་གནས་འཛག་པར་སྤངས་པས་ཏེ། དེ་ལྟར་གྲང་མོ་དེ་མེད་པ་ཞེས་བྱ་བ་དེས་ཤེས་པའོ། །

[Block 754]
འདིའི་དེ་ལ་སའི་སྙིང་པོ་བཟང་ངོ་ཞེས་བྱ་བ་ནི། འཛག་པ་དེའི་སྐམ་པ་དང་། ཤ་བཀྲར་མི་འགྱུར་བ་དེའི་སྨད༌[^675]དུ་ནི་སའི་སྙིང་པོའི་ཕྱེ་མ་བཟང་ངོ་། །ཆོས་གོས་གར་བབ་བབ་ཏུ་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི། སྐབས་འགའ་ཙམ་གཞག་པའི་སྐབས་དགག་པ་ནི་སྔར་བྱས་ཟིན་པས། དེ་ནི་མཛོད་དུ་གྱུར་པའི་གནས་གང་ཡིན་པ་དེའི་དགག་པ་ཡིན་ནོ། །

[Block 755]
དེའི་དོན་དུ་གདང་བུ་བཅའོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་གཞག་པའི་དོན་དུའོ། །

[Block 756]
དེའི་དོན་དུ་སྦུབས༌[^676]ཁུང་བྱའོ་ཞེས་བྱ་བ་ནི་བཅའ་བའོ། །

[Block 757]
དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་ཆོས༌[^677]གོས་ཀྱི་གདང་བཅའ་བ་དེའི་དོན་དུའོ། །གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་གཙུག་ལག་ཁང་རྩིག་པའི་ཚེ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དུས་དེ་ལ་སྦུབས་ཁུང་དེ་གདོད་པར་བྱའི།[^678] །བརྩིགས༌[^679]ཟིན་པའི་འོག་ཏུ་མི་བྱའོ། །

[Block 758]
རྩིག་པའི་སྟེང་ནས་དབུག༌[^680]པར་བྱ་བའམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་བྱས་ཟིན་ན་བུ༌[^681]གུ་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཙུག་ལག་ཁང་ལ་ཞེས་བྱ་བ་ལ། འདི་ལ་གཙུག་ལག་ཁང་བརྩིགས༌[^682]ཟིན་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 759]
གཙུག་ལག་ཁང་ནི་དཔེ་ཙམ་ཡིན་ཏེ། ཁང་ཁྱིམ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་གདང་བུའི་སྦུབས་ཁུང་བཅའ་བའོ།[^683] །དེ་ནི་ཤིང་བུའམ་ཐག་པས་འགྲུབ་པོ་ཞེས་བྱ་བ་ནི།[^684] གདང་བུ་དེ་བྱ་བ་ཉིད་ལ་འབྲས་བུ་མ་ཉམས་པར་གཞག་པ་ལ་དགོན་པ་རྣམས་སུ་དེ་གསུངས་ཏེ། ཡོད་པ་ཙམ་ཉིད་ལས་དེ་རྣམས་ལ་བསྟན་པ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 760]
དེ་རྣམས་ཀྱིས་སམ་གཞན་རྣམས་ཀྱིས་ཀྱང་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་གཙོ་བོ་སྙམ་པ་ལ་དེ་སྐད་ཅེས་སྨོས་སོ། །

[Block 761]
གཏུར་བུར་གོས་དག་བསྐུར་ན་བཟང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དག༌[^685]ཆུད་ཟ་བར་འགྱུར་བ་སྤོང་བ་དང་འབྲེལ་བའི་ཕྱིར་དེ་ཞུགས་པའོ། །

[Block 762]
དེ་བྱའོ་ཞེས་བྱ་བ་ནི་གཏུར་བུ་དེ་ལའོ། །

[Block 763]
ཁྲུ་གསུམ་དང་ཕྱེད་དང་གསུམ་གཉིས་བལྟབ༌[^686]ཏུ་བྱས་ཏེ་བཙེམ་མོ་ཞེས་བྱ་བ་ནི་སྲིད་དུ་ནི་ཁྲུ་གསུམ་མོ། །

[Block 764]
ཞེང་དུ་ནི་ཁྲུ་ཕྱེད་དང་གསུམ་ལས་གང་གི་ཚད་དེ་ཉིས་བལྟབ༌[^687]ཏུ་བྱས་པ་ནི་ཞེང་དུ་ཡིན་གྱི། སྲིད་དུ་མ་ཡིན་པ་ནི་དོན་གྱིས༌[^688]གོ་བར་བྱའོ། །

[Block 765]
དབུས་སུ་ཁ་གདོད་དོ་ཞེས་བྱ་བ་ནི་གཏུར་བུ་དེའིའོ། །

[Block 766]
དེར་ཁ་རན་སྦུ༌[^689]གུ་ཅན་དུ་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཁར་རོ། །

[Block 767]
ཁ་རན་སྦུག་གུ་ཅན་ཅི་ལས་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཐ་གུ༌[^690]ལས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 768]
ཁ་རྒྱུན་གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཐ་གུས་སོ། །

[Block 769]
སྤྱད་པར་བྱ་བ་དག་སྟེང་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གོས་རྣམས་ལའོ། །

[Block 770]
སང་འགྲོ་བར་འགྱུར་བ་ཉིད་ན་བླ་མ་ལ་ཞུས་ཏེ་གནང༌[^691]ན་འགྲོ་བར་བྱའོ། །

[Block 771]
རང་གི་གནས་སུ་ཆག་ཆག་ལ་སོགས་པ་བྱས་ཏེ་ཞེས་བྱ་བ་ནི་གནས་ཁང་ན་གནས་པ་དེ་ནི་འདིར་དེའི་རང་གི་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 772]
དེར་གང་གིས་ཆག་ཆག་ལ་སོགས་པ་བྱས་པ་དེའི༌[^692]ནི་རང་གི་གནས༌[^693]དེར་ཆག་ཆག་ལ་སོགས་པ་བྱས་པའོ། །

[Block 773]
སོགས་པ་ཞེས་སྨོས་པའི་སྒྲས་ནི་ཕྱག་དར་དང་ལྕི་བ༌[^694]འཇམ་པོས་བྱུག་པ་དག་བསྡུའོ། །

[Block 774]
མ་མོ་ལས།

[Block 775 [VERSE]]
འགྲོ་བར་འགྱུར་བ་ཞེས་བྱ་བའི་ཚིག་འདིའོ། །
ལམ་དུ་ཆོས་དང་ལྡན་པའི་གཏམ་གྱིས་སམ།
འཕགས་པའི་མི་སྨྲ་བ་ཉིད་ཀྱིས་འགྲོ་བར་བྱའོ། །
--- END BLOCKS ---
