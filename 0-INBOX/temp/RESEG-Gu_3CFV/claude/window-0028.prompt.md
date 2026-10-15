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
དེ་བས་ན་བླ་གབ༌[^593]མེད་པར་ནི་འདི་རྣམས་ལ་ནི་བྱེད་པ་པོ་སྟེ། ནགས་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 982]
ཤིག་རྣམས་ནི་རས་མར་གཞུག་པར་བྱའོ། །

[Block 983]
དེ་ནི་གསེབ་དག་ཏུའོ་ཞེས་བྱ་བ་ནི་རས་མ་དེ་ནི་ཀ་བ་ལ་སོགས་པའི་གསེབ་དག་ཏུ་གཞུག་པར་བྱའོ། །

[Block 984]
འདིར་གཞུང་ནི་རས་མའི་ནང་དུ་དཀྲིས་ཏེ་ཀ་བའི་གསེབ་བམ་རྩིག་པའི་གསེབ་དག་ཏུ་གཞུག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 985]
རྩ༌[^594]ཤིག་རྣམས་ནི་བསིང་མར་རོ། །

[Block 986]
ཡང་ན་ཕྱོགས་བསིལ་བར་རོ་ཞེས་བྱ་བ་ནི་གང་དུ་གནས་པ་བསྒྲུབ་པ་དེ་ཞེས་བྱ་བ་དོན་གྱིས་ཤེས་པའོ། །

[Block 987]
སྔ་མ་གཞུག་པར་བྱ་བའི་ཕྱིར་བསལ་སྣོད༌[^595]བཅང་བར་བྱའོ༌[^596]ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་ལ་ཆུའི་སྲོག་ཆགས་རྣམས་ཀྱི་སྐབས་སྔར་མཛད་པ་དེ་རྣམས་གཞུག༌[^597]པའི་དོན་དུ་དེ་ལྟ་བུ་བཅང་བར་བྱའོ། །

[Block 988]
བུམ་པ་གང་བཞིན་དུ་གཞུག་ཅིང་ཤིན་ཏུ་སྟོང་པར་དབྱུང་དུ་རུང་བ་ཞེས་བྱ་བ༌[^598]ནི་བསལ་བའི་སྣོད་བརྗོད་པ་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་བརྗོད་པར་བྱ་བ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་གང་ཞིག་གང་བར་འཇུག་པ་དེ་ནི་གང་བ་ཁོ་ན་ལྡང་བ་མ་ཡིན་གྱི་དེ་བས་བསལ་སྣོད་དུ་འགྱུར་རོ། །

[Block 989]
ཡང་ན་ཆུ་ཚགས་དེ་ཉིད་ཀྱིས་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་སྲོག་ཆགས་དེ་དག་བཙགས་པར་གྱུར་པའི་ཆུ་ཚགས་དེ་ཉིད་ཀྱིས་འདི་རྣམས་ལ་བུ་ག་རྣམས་ཀྱི༌[^599]ལྟུང་བ་མ་གྲུབ་པའོ། །

[Block 990]
འདིར་དོན་ནི་འདི་ཡིན་ཏེ། དེ་བས་ན་གཞན་བསགས་པར་བྱེད་པས་འདི་མི་བྱ་ཞིང་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 991]
ཆུ་ཚགས་ལ་སྲོག་ཆགས་ཆགས་པ་བསལ་བའི་ཐབས་ནི་བཤལ་བ་ཡིན་ནོ། །

[Block 992]
དྲི་མ་ནི་བཀྲུ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དྲི་མ་ཆགས་པ་བསལ་བའི་ཐབས་སོ། །

[Block 993]
རུལ་པ་ཉིད་དུ་མི་འགྱུར་བ་ནི་སྐམ༌[^600]པའོ་ཞེས་བྱ་བ་ཡང་། ཐབས་ཤེས་རབ་རྣམ་པར་སྦྱར་རོ། །

[Block 994]
རུལ་པའི་དངོས་པོ་ནི་རུལ་པ་ཉིད་དོ། །

[Block 995]
དེ་གཉི༌[^601]ག་ལ་ཡང་དམ་དུ་བཙིར་ན་ཕན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དྲི་མ་བསལ་བ་དང་རུལ་པ་ཉིད་དུ་མི་འགྱུར་བར་བྱ་བ་ལའོ། །

[Block 996]
དགེ་འདུན་དང་གང་ཟག་དང་ཆུ་ཚགས་དང་ཆུ་ཚད་མ་རྙེད་པའི་ཤེས་པས༌[^602]འཇུག་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ཚད་མ་རྙེད་པའི་སྒྲ་ལ་སོ་སོར་ཤེས་པས་ཞེས་བྱ་བ་ནི༌[^603]འདི་དང་སྦྱར་བར་བྱའོ། །

[Block 997]
དེ་ལྟར་ན་དགེ་འདུན་ཚད་མ་རྙེད་པའི་ཤེས་པས་འཇུག་པ་དང་། གང་ཟག་ཆུ༌[^604]ཚད་མ་རྙེད་པའི་ཤེས་པས་འཇུག་པ་དང་ཆུ་ཚགས་ཚད་མ་རྙེད་པའི་ཤེས་པས་འཇུག་པ་དང་ཆུ་ཚད་མ་རྙེད་པའི་ཤེས་པས་འཇུག་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 998]
དེ་ལ་དགེ་འདུན་ཚད་མ་རྙེད་པའི་ཞེས་བྱ་བ་ནི་དགེ་འདུན་འདི་ལ་མ་དག་པ་ཉིད་མེད་པ་དང་ཆུ་ཐ་སྙད་བྱེད་པ་མེད་དོ་ཞེས་བྱ་བ་མ་ལུས་པར་ཤེས་པའོ། །

[Block 999]
གང་ཟག་འདི་ནི་དག་པ་མ་ཡིན་པ་དང་། ཆུ་དེས་ཐ་སྙད་དུ་བྱེད་པ་ཞེས་བྱ་བ་གང་ཟག་ཆུ་ཚགས་འདི་དང༌[^605]བུམ་ཚགས་གཅེའུ་ཅན་ནམ༌[^606]དེ་དག་ཐམས་ཅད་ཀྱིས་ཆུ་དག་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆུ་ཚགས་ཀྱིའོ། །

[Block 1000]
ཆུ་འདི་ལ་ཕྱོགས་འདི་འམ་ཐམས་ཅད་དུ་ནམ་ཡང་སྲོག་ཆགས་དང་བཅས་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1001]
དེ་བས་ན་ཆུ་ཚགས་ལ་ཚད་མ་རྙེད་པ་ཉིད་དོ། །

[Block 1002]
ཐ་སྙད་ཀྱི་དུས་སུ་ཆེགས་པ༌[^607]ཉིད་གང་ཡིན་པ་དེ་ལ་འདིར་ཡན་ལག་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1003]
ཁྱིམ་པ་ལ་ཡང་གང་ཟག་གི་ཚིག་གིས་བཟུང་བ་ཉིད་ལ་སྦྱར་བར་གྱུར་པ་ཉིད་དོ། །

[Block 1004]
འདིར་གཞུང་ནི་ཆུ་རུང་བ་ཉིད་དུ༌[^608]རྣམ་པ་ལྔ་སྟེ། དགེ་འདུན་གྱིས་རུང་བ་དང་གང་ཟག་གིས་རུང་བ་དང་ཆུ་ཚགས་ཀྱིས༌[^609]རུང་བ་དང་། ཁྲོན་པས་རུང་བ་དང་། ཉིན་ཞག་གཅིག་ཏུ་རུང་བའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1005]
དེ་ལ་རུང་བ་དང་པོ་བཞི༌[^610]ནི་མདོ་འདིས་བསྡུས་པ་ཡིན་ཏེ་གོ་རིམས་བཞིན་ནོ། །

[Block 1006]
ལྔ་པ་ཉིན་ཞག་གཅིག་ཏུ་རུང་བའི་བཏུང་བ་བསྟན་པའི་ཕྱིར། བཅུས་པ་དང་ཁྲོན་པ་དག་ནི་ཉི་མ་འཆར་ཀ་ཚུན་ཆད་བརྟགས་པ་དེ་ཉིད་རྗེས་སུ་འཇུག་གོ་ཞེས་བྱ་བ་ལ། འདིར་ཁྲོན་པ་ཞེས་བྱ་བ་ནི་ཆུ་དོང་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1007]
རྐང་ཁྲུས་སྣོད་སྟོང་པར་མཐོང་ན་དགང་བར་བྱའོ། །

[Block 1008]
ཆུ་དང་གཞན་གྱི་སྣོད་ཀྱང་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་རྫ་མ་དང་བུམ་པ་དང་། ཆུའི་སྣོད་ལ་སོགས་པ་རྣམས་སོ། །

[Block 1009]
དགེ་འདུན་གྱིས་དེར་གཏོགས་པ་ནི་སྣོད་སྤྱད་འབྲུབ་པའི༌[^611]ལས་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེར་རྟོགས་པ་ཞེས་བྱ་བ་ནི་ཆུའི་སྣོད་ལ་སོགས་པ་དང་འབྲེལ་པའོ། །

[Block 1010]
འདིར་གཞུང་ནི་གནས་མལ་གྱི་གཞི་ལས་ཡོན་བདག་དག་གཙུག་ལག་ཁང་དུ་ལྷགས་ཏེ། དེ་དག་རྫ་མཁན་གྱིས་བྱས་པའི་སྣོད་དག་རེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བསྐུར་ཅིག་ཅེས་བཀའ་སྩལ་ཏོ། །

[Block 1011]
དེ་དག་སུས་ཀྱང་མ་བསྡུས་པས་དེ་དག་ཆུད་ཟོས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་སྣོད་སྤྱད་འབྲུབ་པ་བསྐོ༌[^612]བར་བྱ་ཞིང་དེས་ཀྱང་འོང་བ་དག་ལ་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1012]
འདིར་སྦྱིན་པ་དང་བླང་བ་དག་ཀྱང་མ་འདུས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་འདིར་ཞེས་བྱ་བ་བཟུང་བ་ལའོ། །

[Block 1013]
སྦྱིན་པ་དང་བླང་བ་ཞེས་བྱ་བ་ནི་འདི་ཡང་སྣོད་སྤྱད་འབྲུབ་པས༌[^613]བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1014]
གནས་མལ་གྱི་གཞི་ལས་གང་ཞིག་འདི་དེ་རྣམས་མ་བསྡུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྦྱིན་པ་དང་བླང་བ་དག་ཀྱང་སྣོད་སྤྱད་འབྲུབ་པས་བྱ་བ་བསྟན་པ༌[^614]འདི་ལ་ནི་འདི་བསྡུས་པ་ཉིད་བསྟན་པའོ། །

[Block 1015]
ཁྱིམ་པ་རྙིང་པ་བརྙན་པ་ཉིད་ལ་དེ་ཡོད་པ་ཉིད་ལ་ནི་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་རྙིང་པ་དེ་ཡོད་པ་ཉིད་ཡིན་ན་གཡར་པོར་སྦྱིན་པར་བྱའོ། །

[Block 1016]
དེས་གཙུག་ལག་ཁང་དུ་ཡོན་བདག་རྣམས་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་ཀྱང་མ་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེས་ཡོན་བདག་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་དེས་གཙུག་ལག་ཁང་དུ་ཡོན་བདག་རྣམས་འོངས་ཏེ་བརྙན་པ་དག་ལ་གཡར་བ༌[^615]སྦྱིན་པར་བྱ་བ་ཉིད་ཀྱང་མ་བསྟན་པ་མ་ཡིན་པ་དེ་ནི་སྔར་གཞུང་ལས།

[Block 1017]
ཡོན་བདག་གཙུག་ལག་ཁང་དུ་ལྷགས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ༌[^616]ཉིད་འདིས་བསྡུས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 1018]
དགེ་སློང་ལ་ནི་སར་པ་ཕྱིས་བླང་བ་མེད་པ་ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་སྣོད་སྤྱད་སར་པ་དགེ་སློང་ལ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད༌[^617]དུ་སྦྱིན་པའོ། །

[Block 1019]
དེ་ཡང་དེ་ཡོད་པ་གཉིས་ལ་སྦྱིན་པ་འདི་ཆ་གཅིག་གིས་བརྟགས་པའོ། །

[Block 1020]
འདིར་གཞུང་ནི་དགེ་སློང་རྣམས་ལ་ནི་སར་པ་དག་སྦྱིན་པར་བྱའོ། །
--- END BLOCKS ---
