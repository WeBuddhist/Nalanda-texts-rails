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
དེའི་ནང་དུ་ཐིག་ལེ་ཟླུམ་པོ་བྲིས་ཏེ། དེའི་ཡང་ནང་དུ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་དག༌[^519]བལྟ་བར་བྱའོ། །

[Block 772]
དཀྱིལ་འཁོར་གྱི་བདག་པོ་ལ་སོགས་པའི་ཐུགས་ཀར་སེམས་དཔའ་གཉིས་པོ་སྣོད་དང་བཅུད་ཀྱི་ངོ་བོ་ཉིད་མ་ལུས་པར་བལྟ་བར་བྱའོ། །

[Block 773]
དེའི་ཤར་གྱི་ཟུར་གྱི་སྟེང་དུ་བདུད་རྩི་ལྔས་གང་བའི་སྣོད་དང་། ཐབས་དང་ཤེས་རབ་ཀྱི་ངོ་བོ་ཉིད་ཧྲི་ཧཱུཾ་དག་གིས་བྱིན་གྱིས་བརླབས་པ་མྱོས་བྱེད་དང་སྦྱར་བའི་ཆང་གིས་བཀང་བའི་སྣོད་གཉིས་ནི་དབུས་ཀྱི་སྣོད་ཀྱི་ལོགས་གཉིས་སུ་གཞག་པར་བྱས་ལ། ནག་པོ་དང་དམར་པོ་དང་དཀར་པོའི་རས་ཀྱིས་ཁ་བཀབ་ལ་མེ་ཏོག་སྙིམ་པས༌[^520]གཏོར་བར་བྱས་ཏེ། ཐུགས་རྡོ་རྗེ་ལ་སོགས་པའི་སྔགས་ཀྱིས་བྱིན་གྱིས་བརླབ༌[^521]པར་བྱའོ། །

[Block 774]
དེ

[Block 775]
་ནས་ཕྱག་བྱས་ཏེ་དབུས་ཀྱི་སྣོད་ལས་ཐིགས་པ་གསུམ་གསུམ་བླངས་ཏེ། གཡས་གཡོན་གྱི་སྣོད་དག་ཏུ༌[^522]གཏོར་བར་བྱ་ཞིང་མྱོས་བྱེད་ཀྱི་སྣོད་དམ་ཆང་གི་སྣོད་བླངས་ལ་རྣལ་འབྱོར་པ་རྣམས་ལ་ལས་ཀྱི་རྡོ་རྗེས༌[^523]

[Block 776]
དང་པོ་བསྙོད་པར་བྱའོ། །

[Block 777]
དེའི་རྗེས་སུ་དགེ་སློང་དང་། དགེ་ཚུལ་དང་དགེ་བསྙེན་གྱི་ཚོགས་ལའོ། །

[Block 778]
གང་ལས་བཏུང་བ་བརྩམ་པ༌[^524]ཐ་མར་དེ་ཉིད་ལ་བསྙོད་པར༌[^525]བྱའོ། །

[Block 779]
དེ་ནས་རེ་རེའི་མདུན་དུ་ཚོད་མ་སྣ་ཚོགས་པ་དང་། ཤ་སྣ་ཚོགས་པ་དང་རོ་དྲུག་དང་ལྡན་པའི་རྒྱལ་པོའི་སཱ་ལུ་ལ་སོགས་པས་བཀང་བའི་སྣོད་རྣམས་འབུལ་བས༌[^526]ཚིམ་པར་བྱའོ། །

[Block 780]
ཕྱེད་ཟོས་པས་བཟའ་བཅའ་ཐམས་ཅད་སྣོད༌[^527]གཅིག་ཏུ་བསྡུས་ཏེ་ཐམས་ཅད་ཀྱིས་གཅིག་ཏུ་བཟའ་བར་བྱའོ། །

[Block 781]
དེ་ནས་བཏུང་བའི་སྣོད་རྣམས་གཅིག་ཏུ་བསྲེས་ཏེ་བཏུང་བར་བྱའོ། །

[Block 782]
ལས་ཀྱི་རྡོ་རྗེས་ཀྱང་ཅང་ཏེའུ་ལ་ཡི་གེ་གསུམ་གྱིས་མཆོད་པར་བྱ་སྟེ། ལག་པ་གཡས་པས་བླངས་ལ་ཧཱུཾ་ཕཊ་ཅེས་བྱ་བའི་སྒྲ་སྒྲོགས་པར་བྱའོ། །

[Block 783]
རྡོ་རྗེ་རྣལ་འབྱོར་མ་རྣམས་ཀྱིས་རྡོ་རྗེའི་གར་སྣ་ཚོགས་བྱའོ། །

[Block 784]
ཚོགས་ཀྱི༌[^528]བདག་པོས་གར་བྱ་བ་དང་། གཞན་མ་རྣམས་ཀྱིས་གླུ་དང་རོལ་མོ་བྱའོ་ཞེས་ལ་ལ་འདོད་དོ། །

[Block 785]
ཐམས་ཅད་ཀྱིས་ཀྱང་གར་བྱའོ་ཞེས་ལ་ལ་འདོད་དོ། །

[Block 786]
དམ་པར་དགའ་བ་སྐྱེས་པ་ན་གར་བྱ་བ་ཡིན་གྱི། གཞན་དུ་ན་སེམས་རྩེ་གཅིག་པར་གནས་པར་བྱའོ། །

[Block 787]
ཚོགས་ཀྱི་འཁོར་ལོའི་བྱིན་གྱིས་རློབ་པའི་རྟགས་ནི་ངང་པ་དང་བུང་བ་དང་ཁྱུ་མཆོག་དང་འུག་པ་ལ་ཞོན་པའི་མཁའ་འགྲོ་མ་རྣམས་འོང་བར་གྱུར་པ་ན་དེ་རྣམས་ཀྱི་ལུས་ཀྱི་དྲི་སྒོག་སྐྱ་དང་ག་བུར་དང་པདྨ་དང་། ཤའི་དྲི་བྲོ༌[^529]བ་དང་། ངང་པ་ལ་སོགས་པའི་སྒྲ་ཐོས་པས་སོ། །

[Block 788]
དེའི་ཚེ་དེ་རྣམས་ལ་ལྷག་མའི༌[^530]གཏོར་མ་རྒྱས་པར་སྦྱིན་པར་བྱའོ། །

[Block 789]
ཚོགས་ཀྱི་ནང་དུ་རྩོད་པའམ་རྒོད་པའམ་རྟོག་པ༌[^531]གང་གིས་བྱེད་པ་དེ་དེ་མ་ཐག་ཏུ་ཕྱི་རོལ་དུ་དབྱུང་བར་བྱའོ། །

[Block 790]
བཟོད་པར་གསོལ་བ་བྱེད་ན་མཆོད་པའི་ལས་བྱེད་དུ་གཞུག་སོ།། །།

[Block 791]
དེ་ནས་ལག་པ་ལ་སོགས་པ་བཀྲུས༌[^532]ལ་མེ་ཏོག་གི་གཅལ་བཀྲམ་པར་བྱ་སྟེ། སོ་རྩི་ཕུལ་ལ་ཡོན་རྣམ་པ་བཞི་པོས་མཉེས་པར་བྱ་སྟེ། གཤེགས་སུ་གསོལ་བས་ཚིགས་སུ་བཅད་པས་ཚོགས་ཀྱི་འཁོར་ལོ་གཤེགས་སུ་གསོལ་ལོ། །

[Block 792]
ཨོཾ་ཀུ་རུ་ཀུ་རུ༌[^533]བཏྟ་ལེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱིས་ལྷག་མའི་གཏོར་མ་དུར་ཁྲོད་དུ་བསྐྱལ་བར་བྱའོ་ཞེས་ཚོགས་ཀྱི་འཁོར་ལོའི་ཆོ་གའི་རིམ་པའོ། །

[Block 793]
[^534]

[Block 794]
དེ་ལྟ་བུའི་མཆོད་པ་རྡོ་རྗེ་སློབ་དཔོན་ལ་བྱས་པས་མཉེས་པར་གྱུར་པའི་སློབ་དཔོན་གྱིས་ཀྱང་སློབ་མས་ཕུལ་བའི་ཕྱག་རྒྱ་དང་ལྷན་ཅིག་སྙོམས་པར་ཞུགས་ཏེ་ཕྱག་རྒྱ་དེ་ཉིད་དམ། ཕྱག་རྒྱ་གཞན་གྱིས་སློབ་མ་དེ་ལ་ཤེས་རབ་ཀྱི་དབང་བསྐུར་བར་བྱའོ། །

[Block 795]
དེ་ལ་སློབ་མ་རྡོ་རྗེ་སློབ་དཔོན་ལ་འདུད༌[^535]ཅིང་ཚིགས་སུ་བཅད་པ་འདིས་བསྟོད་པར་བྱ་སྟེ།

[Block 796 [VERSE]]
ཁམས་གསུམ་ལས་ནི་ངེས་སྒྲོལ་ཞིང་། །
མཁའ་དང་མཉམ་པ་ཉིད་གྱུར་པ། །
ཁྱོད་ནི་འདོད་པས་མ་གོས་པས། །
མི་དམིགས་ཁྱོད་ལ་ཕྱག་འཚལ་བསྟོད། །

[Block 797 [VERSE]]
ཕུང་པོ་དང་ནི་ཁམས་རྣམས་དང་། །
སྐྱེ་མཆེད་རྣམས་ལ་མི་བརྟེན་པ། །
ཕྱིན་ཅི་ལོག་ལས༌[^536]ངེས་གྲོལ་བ། །
དམིགས་མེད་ཁྱོད་ལ་ཕྱག་འཚལ་བསྟོད། །

[Block 798 [VERSE]]
ཇི་ལྟར་ནམ་མཁའ་གཞི་མེད་ཅིང་། །
སྤྲོས་པ་མེད་ཅིང་སྣང་བ་མེད། །
ཁྱོད་ཀྱི་ཐུགས་ནི་མཁའ་དང་མཚུངས། །
མི་དམིགས་ཁྱོད་ལ་ཕྱག་འཚལ་བསྟོད། །

[Block 799]
དེ་ལྟར་བསྟོད་ནས་སླར་ཡང་མངོན་པར་བྱང་ཆུབ་པ་མཐོང་བར་འདོད་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་འདི་དག་གིས་གསོལ་བ་གདབ་པར་བྱ་སྟེ།

[Block 800 [VERSE]]
མངོན་པར་བྱང་ཆུབ་མཐོང་བ་ནི། །
མགོན་པོ་ཆེན་པོ་བདག་ལ་སྩོལ།[^537] །
ལས་དང་སྐྱེ་བ་ལས་གྲོལ་ཞིང་། །
སྣང་བ་གསུམ་པོ་རྣམ་པར་སྤངས། །

[Block 801 [VERSE]]
རྡོ་རྗེ་ཡེ་ཤེས་བླ་མེད་པ། །
སློབ་དཔོན་ཆེན་པོ་བདག་ལ་སྩོལ།[^538] །
སངས་རྒྱས་ཀུན་གྱི་ཡེ་ཤེས་ཆེ། །
དེ་བཞིན་གཤེགས་པ་ཀུན་གྱི་གནས། །

[Block 802 [VERSE]]
ལུས་ངག་ཡིད་ནི་དག་བྱེད་པ། །
རྡོ་རྗེ་ཆེན་པོ་བདག་ལ་སྩོལ།[^539] །
ཐོག་མ་ཐ་མ་མེད་ཞི་བ། །
ཉོན་མོངས་ཐམས་ཅད་སྦྱོང་བྱེད་པ། །

[Block 803]
ཞེས་ཚིགས་སུ་བཅད་པས་མཉེས་པའི་སློབ་དཔོན་གྱི་རྡོ་རྗེ་དབྱིངས་ཀྱི་དབང་ཕྱུག་མའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱག་རྒྱ་རྡོ་རྗེ་འཆང་གི་རང་བཞིན་སློབ་མ་དེ་ལ་སྦྱིན་པར་བྱའོ། །

[Block 804]
དེ་ནས་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི༌[^540]རང་བཞིན་དམ་ཚིག་གི་ཕྱག་རྒྱ་རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ་སྐྲ་གྲོལ་བ་གཅེར་བུར་གྱུར་ནས་ཁྲིའི་ཐོག་ཏུ་བཞུགས་ཏེ་སློབ་མ་བཀུག་ལ་འདི་ལྟར་དྲི་བར་བྱ་སྟེ།

[Block 805 [VERSE]]
[^541]བཤང་གཅི་ལ་སོགས་བཟའ་བ་ནི། །
རྡོ་རྗེ་ཅན་ཁྱོད་ཅི་ནུས་སམ།
ཁྲག་དང་ཁུ་བ་ཤ་དག་དང་། །
བུད་མེད་རྣམས་ལ་དད་པ་དང་། །

[Block 806 [VERSE]]
བྷ་གའི་འོ་བྱེད་མི་རྟོག་གམ། །
བུ་ཁྱོད་སྨྲོས་ཤིག་རྡོ་རྗེ་ཅན། །
སློབ་མས་ཀྱང་འདི་ལྟར་བརྗོད་དེ། །
ཤུ་ཀྲ༌[^542]ཁྲག་སོགས་བཟའ་བ་ནི། །

[Block 807 [VERSE]]
ལྷ་མོ་ཅི་ཕྱིར་བདག་མི་ནུས། །
རཀྟ་ཤུ་ཀྲ་ཤ་ཆེན་དང་། །
བུད་མེད་རྣམས་ལ་དད་དེ་བཞིན། །
བྷ་གའི་པདྨར་ཙུམ་པ་ན། །

[Block 808]
ཐམས་ཅད་བདག་གི་ནུས་པ་ཉིད། །ཅེས་སློབ་མའི་ཚིག་ཐོས་ནས་ལག་པ་གཉིས་ཀྱིས་པདྨ་ཕྱེ་བར་བྱས་ཏེ། ནང་དུ་གནས་པའི་རྩའི་འཁོར་ལོ་བསྟན་པར་བྱེད་དེ། སྐྱེས༌[^543]བུ་གསང་བའི་པདྨ་འདི་ལ་རེ་ཞིག་བལྟ་བར་གྱིས་ཤིག །གང་གི་ནང་དུ་རྩ་རྣམ་པ་ལྔ་པོ་འདི་དག་ནམ་མཁའ་ལྔའི་ངོ་བོ་ཉིད་དུ་གནས་སོ། །

[Block 809]
དེ་ལ་འདོད་པའི་གདུགས་ཞེས་བྱ་བའི་རྩ་དབུ་མ་འདི་ནི་ཆུ་རྒྱུ་བ་ཐུགས་ཀྱི་རྡོ་རྗེའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 810]
འདི་ནི་གཡོན་པའི་རྩ་སྟེ་རི་བོང་འཛིན་མ་ཞེས་བྱ་བ༌[^544]ཤུ་ཀྲ༌[^545]རྒྱུ་བ་སྟེ་བཅོམ་ལྡན་འདས་འོད་དཔག་ཏུ་མེད་པའི་བདག་ཉིད་དུ་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
