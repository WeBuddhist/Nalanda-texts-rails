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
[Block 981]
དོན་གྱིས༌[^715]དེ་རྣམས་ཀྱི་ཆེས་རྒན་པའི་གཞོན་ནུ་དེ་གནས་སོ། །

[Block 982]
ཆེས་རྒན་པ་དེ་ལ་ནི་གཞོན་ནུ་ལ་གནང་བར་འགྱུར་ཏེ། གནས་ལ་མི་གནས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 983]
ཡོད་ན་ཡང་རེ་ཞིག་གི་གནས་དེ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གནས་ལའོ། །

[Block 984]
ཡོད་ན་ཡང་རྟེན་ནི་རྟེན་ལའོ། །

[Block 985]
གཞོན་ནུའི་ཆེས་རྒན་པ་ལ་ཞུ་བར་བྱའོ། །

[Block 986]
འདིར་གཞུང་ནི་འདི་ཡིན་ཏེ། རེ་ཞིག་གི་གནས་ཉིད་ཀྱིས་འདི་ཉིད་མཁན་པོ་མཉམ་པར་འགྱུར་རོ། །

[Block 987]
འདི་ཉིད་ཁྱོད་ཀྱིས་ཞུ་བར་བྱའོ། །

[Block 988]
འདི་ཉིད་ཁྱོད་ལ་སློབ་པར་བྱེད་པར་འགྱུར་བ་དང་། ཀློག་ཀྱང་ཀློག་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་རབ་ཏུ་བྱུང་བའི་གཞི་ལས་སྤྲུལ་པ་ལ༌[^716]གསུངས་པའོ། །

[Block 989]
མ་ཞུས་པར་དེ་ལྟ་བུ་ལ་བདག་གིས་སམ་དེས་ཀྱང་བསྙེན་བཀུར་གྱི་ལས་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་དེ་ལྟ་བུ་ནི་ལུགས་ཐ་དད་པའི་རབ་ཏུ་འབྱུང་བ་ཤེས་པའམ་དོགས་པའོ། །

[Block 990]
གནས་པར་འོས་པ༌[^717]ཡོངས་སུ་ཚོལ་བ༌[^718]ལ་ཞུགས་པ་ནི་མེད་ན་མི་གནས་པར་འདུག་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྐྱོན་མེད་པའོ། །

[Block 991]
མེད་ན་ནི་ཞེས་བྱ་བ་ནི་རྟེན་ནོ། །

[Block 992]
སྐྱོན་མེད་པ་ནི་སུ་ལ་ཞེ་ན། དེའི་ཕྱིར་ཡོངས་སུ་འཚོལ་བ་ལ་ཞུགས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 993]
དུས་ཇི་ཙམ་དུ་ཞེ་ན། དེའི་ཕྱིར་ཞག་ལྔའི་མཐར་ཐུག་པའི་བར་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་སྲིད་དུ་ཞག་ལྔའི་མཐར་ཐུག་པའི་བར་དུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 994]
ཇི་སྲིད་ཞག་ལྔ་ཉིད་དུ་རྙེད་པ་ཡོད་ན་འོས་པ་ཡིན་ནོ། །

[Block 995]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས་མི་གནས་པ་ལ་ཡུལ་ཇི་སྲིད་དུ་རྙེད་པ་འཚལ་བར་བགྱི། ཉེ་བ་འཁོར་ཞག་ལྔ་ཚུན་ཆད་དོ། །

[Block 996]
རྙེད་པ་ཡོད་ན་འོས་པ་ཉིད་དེ༌[^719]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 997]
དེ་ཡང་སྦྱོར་བ་མི་ཐོགས་པ་དང་གནས་ཡོངས་སུ་ཚོལ་བ་ལ་ཞེས་བྱའོ། །

[Block 998]
གློ་བུར་དུ་འོངས་པས་ནི་ངལ་སོས་ནས་ཉི་མ་གཉིས་པའམ་གསུམ་པ་ལ་གནས་བཅའ་བར་བྱའོ། །

[Block 999]
ཉི་མ་གཅིག་ནི་ཆེད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་བཅའ་བར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1000]
གནས་པ་ཉེ་བར་མི་གནས་ན་གནས༌[^720]ལ་ཞུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་པར་བྱེད་པས་ན་གནས་པ་སྟེ། འདི་ལས་ལ་ཀའི་རྐྱེན་ཏེ་གནས་ཉིད་ཀྱིས་བཅའ་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1001]
ལས་སུ་བསྐོས་པར་སོང་བ་ན་དེར་གཞན་བྱུང་བ་ན་མ་ཞུས་ཀྱང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ལས་སུ་བསྐོས་པའི་རྒྱུ་མཚན་དུ་སོང་བ་གཞན་གྱིས༌[^721]ལས་སུ་བསྐོས་པ་ལ་འགྲོ་བ་ལ་སྐྱོན་མེད་དེ་མ་ཞུས་པར་ཞེས་པའི༌[^722]དོན་ཏོ། །

[Block 1002]
འདི་ནི་རྣམ་པར་འབྱེད་པ་ལས་གནས་མལ་གྱི་བསླབ་པའི་གཞི་ལས་འདི་དང་ཉེ་བ་ན་མཐོང་བ་མ་ཡིན་ཏེ། གནས་བཅའ་བར་བྱའོ་ཞེས་བྱ་བ་དང་སྦྱར་བར་བྱའོ། །

[Block 1003]
གང་ཡང་རུང་བ་ལ་མི་བྱའོ། །

[Block 1004]
དྲི་བ་ལ་སོགས་པས་ཚུལ་ཁྲིམས་དང་ཤེས་པ་དང་འཁོར་ལ་ཕན་འདོགས་པ་ཉིད་ངེས་པར་ཤེས་པར་བྱས་ནས་དེ་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དང་ཤེས་རབ་དང་འཁོར་དང་འཛིན་པར་བྱེད་པ་དང་རྗེས་སུ་བརྗོད་པ་ལ་སོགས་པ་ལ་རབ་ཏུ་འཇུག་བཞིན་པ་ཉིད་གང་ཟག་འདིའི་དྲི་བས་སམ་ཡང་དག་པར་སྤྱོད་པ་གཞན་གྱིས་ཤེས་ནས་གནས་བཟུང་བ༌[^723]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1005]
ཆོ་ག་ཇི་ལྟ་བུས་ཤེ་ན། སྡོམ་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་སོགས་པ་བཞིན་དུ་སྔགས་ལ་སོགས་པའི་ཆོ་གས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1006]
སྡོམ་པ་ནི་ཐལ་མོ་སྦྱར་ནས་བླང་བར་བྱ་བ་ཡིན་ཏེ། དེའི་ཕྱིར་འདི་ལ་ནི། ལག་པ་གཉིས་ཀྱིས་རྐང་པའི་མཐིལ་གཉིས་ལ་བཅངས་པས་སོ། །

[Block 1007]
ཡོངས་སུ་བརྟགས་ནས་སྦྱིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྟན་པ་ལ་གཞག་པར་ཡང་ནུས་སམ་ཞེས་བྱ་བའི་བརྟག་པ་འདིའོ། །

[Block 1008]
བུ་དང་ཕའི་འདུ་ཤེས་དག་བསྐྱེད་པར་བྱའོ། །

[Block 1009]
མཁན་པོ་དེ་ཉིད་གནས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། །དེའི་སྒྲ༌[^724]ནི་མཁན་པོ་ཉིད་མཆོག་ཏུ་བཟུང༌[^725]བའོ། །

[Block 1010]
མཁན་པོ་གནས་པ་ལ་མཁན་པོ་དེ༌[^726]ཉིད༌[^727]གནས་པ་ཉིད་ནི། འདིར་ཡང་ལས་ལ་ཀའི་རྐྱེན་ནོ། །

[Block 1011]
གནས་པས་ན་གནས་པ་སྟེ་གནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1012]
དེའི་དངོས་པོ་ནི་གནས་པ་ཉིད་དོ། །

[Block 1013]
དེ་བས་ན་དེར་འདི་མ་བཟུང༌[^728]ངོ་། །དེའི་ཕྱིར་དེ་ལ་དེ་མི་བཅའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་གནས་ལའོ། །

[Block 1014]
དེ་ཞེས་བྱ་བ་ནི་མཁན་པོ་ལའོ། །

[Block 1015]
འདི་སྐད་བསྟན་ཏེ། གང་གི་ཕྱིར་ལྷན་ཅིག་གནས་པའི་མཁན་པོ་དེ་ཉིད་ཁོ་ན་ཡིན་པ་དེའི་ཕྱིར་དེའི་དྲུང་ན་གནས་བཅའ་བར་མི་བྱ་ཞེས་བྱ་བའོ། །

[Block 1016]
གཉིས་ཀ་ལ་མི་ལྟོས་པ་ཉིད་བྱུང་བ་ནི་གནས་བཅས་པ་འཇིག་པའི་རྒྱུ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ།[^729] གཉིས་ཀ་ལ་ཞེས་བྱ་བ་ནི་གནས་དང་གནས་པར་ལྡན་པ་དག་ལའོ། །

[Block 1017]
ཅིག་ཅར་རམ་རིམ་གྱིས་མི་ལྟོས་པ་ཉིད་དུ་བྱུང་བ་ཉིད་དོ། །

[Block 1018]
བཅས་པ་ནི་གནས་བཟུང་བ་ལས་ཉམས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1019]
མི་ལྟོས་པ་ཉིད་དུ་གྱུར་པ་གཅིག་ལ་རེ་ཞིག་རྟེན་ལ་རྗེས་སུ་འཇུག་པ་སྟེ། ཇི་སྲིད་དུ་གཞན་མི་ལྟོས་པ་ཉིད་དུ་གྱུར་པ་ཞེས་བྱ་བའོ། །

[Block 1020]
གང་ཞིག་གནས་དང་གནས་པ་ཉིད་དུ་ཁས་བླངས་པ་འདི་ནི་འཁོར་དང་འབྲེལ་པ་སྟེ། གཅིག་ལ་ལྟོས་པ་དང་བཅས་པ་ཉིད་ལ་འཁོར་དང་འབྲེལ་བ་དང་བྲལ་བ་ཉིད་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་འདི་ནི་འདིར་རྣམ་པར་གཞག་པའོ། །
--- END BLOCKS ---
