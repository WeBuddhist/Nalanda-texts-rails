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

[Block 776]
ངལ་བསོ་བའི་གནས་སུ་གཙུག་ལག་གི་ཚིགས་སུ་བཅད་པ་གདོན་ནོ། །

[Block 777]
ཆུ་བཅུས་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གནས་སུ་དྲང་སྲོང་གིས་གསུངས་པའི་ཚིགས་སུ་བཅད་པ་གདོན་པའོ། །སུའི་ཕྱིར་ཞེ་ན། དེའི་ཕྱིར་ཆུ་གང་གི་ཡིན་པ་དེའི་ཕྱིར་རོ། །

[Block 778]
ལྷ་རྣམས་ཀྱི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཆུ་བཅུས་པའི་གནས་སུ་ཡང་དྲང་སྲོང་གིས་གསུངས་པའི་ཚིགས་སུ་བཅད་པ་གཞན༌[^695]གདོན་ནོ་ཞེས་བྱ་བ་ནི་ཆུའི་ལྷ་རྣམས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པའོ། །

[Block 779]
གནས་པར་རྒྱུན་ཆགས་གསུམ༌[^696]པའོ་ཞེས་བྱ་བ་ནི་ཞག་ཏུ་གནས་པའི་གནས་སུ་རྒྱུན་ཆགས་གསུམ་པ༌[^697]གདོན་པར་བྱའོ། །

[Block 780]
དཔྱང་ཐག༌[^698]བཅང་བར་བྱའོ། །

[Block 781]
དེའི་ཚད་ཀྱིའོ་ཞེས་བྱ་བ་ནི་ཁྲོན་པ་དེའི་འོ། །

[Block 782]
ཁྲུ་བརྒྱ་ཡན་ཆད་ནས་བརྒྱ་ལྔ་བཅུ་མན་ཆད་དོ། །

[Block 783]
ཁ་ཅིག་ལས་ནི་ཡུལ་གྱི་རྗེས་སུ་མཐུན་པའོ་ཞེས་སོ་ཞེས་བྱ་བ་ནི་ཁ་ཅིག་ནི་ཚིགས་སུ་བཅད་པ་རྣམས་ལ་འདོད་དོ། །

[Block 784]
དེ་མེད་པར་ཞེས་བྱ་བ་ནི་ཁྲོན་པའི་ཆུ་དེའོ། །

[Block 785]
ཁྲོན་པའི་ཆུ་མ་ཡིན་པ་དཀོན་པའི་ཡུལ་དུ་ཀུན་དུ་རྒྱུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཁྲོན་པའི་ཆུ་མ་ཡིན་པ་ལ་ནི་འབབ་ཆུ་ལ་སོགས་པའི་ཆུ་ཕྱོགས་གང་ན་རྙེད་པར་དཀའ་བ་དེའི་ཁྲོན་པའི་ཆུ་མ་ཡིན་པ་དཀོན་པའི་ཡུལ་ལོ། །

[Block 786]
ལམ་དུ་འགྲོ་བས་ཆོས་གོས་སྤྲུགས་ཤིང་ཁྲུས་བྱས་པའམ། རྐང་ལག་བཀྲུས་ཏེ་ཆུ་ཐོགས་ནས་མཆིལ་ལྷམ་ཕྱིས་ཤིང་ཆོས་གོས་གསུམ་གྱོན་ཏེ་སྤྱོད་ལམ་ཞི་བས་གཙུག་ལག་ཁང་དུ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སིལ་བུ་དག་ལས་འདི་བསྟན་ནོ། །

[Block 787]
རྒན་རིམས་བཞིན་ལ་ཕྱག་བྱས་ནས་ཐ་མལ་པའི་ཕྱོགས་སུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཐ་མལ་པའི་ཕྱོགས་ལྐོག་ཏུ་གྱུར་པ་མ་ཡིན་པ་དགེ་སློང་ཐམས་ཅད་འདུན་པ་གང་ཡིན་པ་དེར་བསྡད་པར་བྱའོ། །

[Block 788]
སྒྲ་བསྐྱུང་བ༌[^699]དང་མཛེས་པ་དང་ཤིན་ཏུ་བསྡམས་པ་དང་སྤྱོད་ལམ་རན་པར་རོ་ཞེས་བྱ་བ་ནི། ཤིན་ཏུ་བསྡམས་པ་དང་སྤྱོད་ལམ་རན་པར་རོ། །

[Block 789]
འདིར་ནི་མ་མོ་དག་ལས།

[Block 790]
ཐ་མལ་པའི་ཕྱོགས་སུ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 791]
མི་ཤེས་ན་ཞེས་བྱ་བ་ནི།

[Block 792]
འདིར་སིལ་བུ་དག་ལས།

[Block 793]
དེ་ལ་སོགས་པ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 794]
རྒྱུས་ཤེས་པ་དང་ལྡན་པས་བསུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་དེའི་རྒྱུས་ཤེས་པ་ནི་དེ་ལ༌[^700]འདི་ནི་ཆེ་གེ་མོ་ཞིག་ནས་འོངས་སོ། །

[Block 795]
ཆེ་གེ་མོ་ཞིག་གི༌[^701]ལྷན་ཅིག་གནས་པ་དང་ཉེ་གནས་ཡིན་ནོ་ཞེས་དེས་བསུ་ཞིང་རང༌[^702]གནས་སུ་ངལ་བསོར་གཞུག་པ་དང་ཆམ་དུ་དབབ་པར་བྱའོ། །

[Block 796]
རྒྱུས་ཀྱི༌[^703]སྒྲས་ནི་དེ་ཤེས་པ་བརྗོད་པ་ཡིན་ཏེ། དེ་གང་ལ་ཡོད་པ་དེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 797]
མི་ཤེས་ན་མུ་གཅིག་པ་ཡིན་ཡང་བསུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་དུ་མུ་གཅིག་པ་དང་བསུ་བར་མི་བྱ་བ་འབའ་ཞིག་ཏུ་མ་ཟད་དོ། །

[Block 798]
སྒོ་ཆོད་ཅིག་ཚོལ་ན་མ་སྦྱིན་ཅིག་ལེན་ན་བཟློག་ཅིག་ཅེས་བཅོལ་བ་ཁས་བླངས་ནས་ཡལ་བར་བོར་རམ། འདི་ཁོ་བོའི་གྲོགས་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་ཡིད་གཅུགས༌[^704]པའི་དངོས་པོ་ཉིད་དུ་བསྒྲུབ་པ༌[^705]ལ་བརླག་པར་གྱུར་ན་གཞལ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཡིད་གཅུགས་པའི་དངོས་པོ་ཉིད་དུ་བསྒྲུབས་པ༌[^706]ལས་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདི་ཁོ་བོའི་གྲོགས་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་ཁས་བླངས་ནས་ཡལ་བར་བོར་ན་རྣམ་པ་འདི་གཉིས་ནི༌[^707]གཉུག་མར་གནས་པ་དང་། གློ་བུར་དུ་འོངས་པ་གཉིས་ཀ་ལ་བྱེ་བྲག་མེད་པ་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཡིད་ཆེས་པ་ལ་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱིས་མི་ཤེས་པའི་བྱེ་བྲག་བརྟག་པ་ནི་ཐབས་ཡིན་ནོ། །

[Block 799]
དབུལ་བར་བྱ་བ་ལྟུང༌[^708]ནའོ་ཞེས་བྱ་བ་ནི་དབུལ་བར་བྱ་བའི་དངོས་པོ་ལེན་པར་བྱེད་པའི་ལག་ཏུ་མ་སོང་བར་འབབ་ཆུ་ལ་སོགས་པའི་ནང་དུ་ལྷུང་ནས་འཛིན་མ་ནུས་ན་ཞེས་བྱ་བ་དོན་གྱིས༌[^709]རིག་པར་བྱའོ། །ཅི་རྣམ་པ་ཐམས་ཅད་དུའམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་མ་བླངས་པར་བཏང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་གང་ལ་དབུལ་བ་དེས་མ་བླངས་པར་འབུལ་བར༌[^710]བྱེད་པས་བཏང་ན་ནི་དེས་ན་དབུལ་བར༌[^711]བྱེད་པ་ཉིད༌[^712]ཡིན་ནོ། །

[Block 800]
དེ་ལ་བག་མེད་པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་དྲི་བར༌[^713]བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་མ་བླངས་པ་དེ་ལའོ། །

[Block 801]
ཁྱོད་ཀྱིས་ཟིན་ཏམ༌[^714]འོན་ཏེ་མ་ཟིན་ཅེས་བྱ་བའི་ཚིག་གིས་ཐ་སྙད་དུ་བྱ་བའོ། །

[Block 802]
དེའི་ཕྱིར་ཟིན་ཏམ༌[^715]མ་ཟིན་ཅེས་བརྗོད་ན་ཟིན་པ་ཉིད་དུ་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 803]
བརྙས་པ་མི་གཙང་བས་མ་རུང་བར༌[^716]འགྱུར་བ་བཀྲུ་བ་ལ་སོགས་པས་སེམས་གཟུང་བར༌[^717]མ་གྲུབ་ན་རིན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་དེ་སོན་པ་ལ་སྨོས༌[^718]ཏེ། གཞན་དུ་ཡང་ཆོ་ག་འདི་སྦྱར་བ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པའོ། །

[Block 804]
ཞར་ལ་བྱུང་བའི་སྐབས༌[^719]སོང་ཟིན་ཏོ།། །།

[Block 805]
རྒྱུས་ཤེས་པ་དང་ལྡན་པས་བསུ་བར་བྱའོ་ཞེས་གང་སྨོས་པ་དེ་ལ་ཇི་ལྟར་བསུ་བར་བྱ་ཞེ་ན་ལྷུང་བཟེད་དང་ཆོས་གོས་བླང་བར་བྱའོ། །

[Block 806]
སྟན་གདིང་བར་བྱའོ། །

[Block 807]
རྐང་པ་བཀྲུ་བར་འགྲོན༌[^720]དུ་གཉེར་བར་བྱའོ། །

[Block 808]
ཆུས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་དོན་དུ་ཆུས་འགྲོན༌[^721]དུ་བསྙེན་པར་བྱའོ་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 809]
ཕྱག་བྱའོ། །

[Block 810]
སྤྱོད་པ་བདེའམ་འདྲིའོ།[^722] །ཅི་ནུས་ཀྱིས་ཡང་དག་པར་དགའ་བར༌[^723]འགྱུར་བར་བྱའོ། །
--- END BLOCKS ---
