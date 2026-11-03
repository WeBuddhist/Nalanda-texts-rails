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
གཞན་གྱི་དོན་དུ་མེད་ཅེས་བྱ་བ་དང་། བཟློག་པ་དེ༌[^545]མི་ནུས་པའི་ཕྱིར་སྤངས་པར་གྱུར་པ་ཡིན་ཏེ། འདིས་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ནོར་ཡོངས་སུ་བཟུང་བ་བསྟན་ཏོ། །

[Block 982]
མདོག་དང་བསུང་དང་འཇམ་པ་ལ་སོགས་པའི་ཞེས་པ༌[^546]སོགས་པའི་སྒྲས༌[^547]ནི་སྨིན་པའི་ནུས་པ་དང་བཟའ་བའི༌[^548]ཡོན་ཏན་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 983]
རྣམ་པ་སྣ་ཚོགས་ཞེས་བྱ་བ་ནི་དངོས་པོའི་རྣམ་པའོ། །

[Block 984]
ཡང་ན་བཅའ་བ་ལ་སོགས་པ་རེ་རེའི་རྣམ་པ་ཡང་སྣ་ཚོགས་པར་གྱུར་པ་ཡིན་པས་སྣ་ཚོགས་པར་བཤམས་པའོ། །

[Block 985]
བཟའ་བ་དང་བཅའ་བ་ལ་སོགས་པའི་སྒྲས་གཞིབ་པ༌[^549]དང་བལྡག་པ་ལ་སོགས་པ་ཡང་གཟུང༌[^550]ངོ་། །དེའི་བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པར་འཕེལ་བར་འདོད་པ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་འོ། །

[Block 986]
འདིས་སྩོགས་པ་ཡིན་པས་ཚོགས་ཏེ་བསོད་ནམས་ཉིད་ཚོགས་སོ། །

[Block 987]
འདིར་སྦྱིན་པའི་ཉི་ཚེ་ལ་བསམས་པ་ཡིན་གྱི། ཚུལ་ཁྲིམས་དང་བཟོད་པ་རྣམ་པར་འཕེལ་བར་འདོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 988]
ཉོན་མོངས་པ་ཐམས་ཅད་ནི་ཁམས་གསུམ་གྱི་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས༌[^551]སྤང་བར་བྱ་བའོ། །

[Block 989]
ཉོན་མོངས་པ་ཉིད་བུད་ཤིང་ཡིན་པས་ཉོན་མོངས་པའི་བུད་ཤིང་ངོ་། །དེ་ཡང་མི་མཐུན་པའི་ཆོས་སུ་བསྟན་ཏེ། ཇི་ལྟར་མེས་བུད་ཤིང་བསྲེགས་པ་དེ་བཞིན་དུ་ཡེ་ཤེས་ཀྱི་མེས་ཉོན་མོངས་པ་ཐམས་ཅད་ངེས་པར་བསྲེག་པ༌[^552]ཡིན་ནོ། །

[Block 990]
ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེགས་པ༌[^553]གང་ཡིན་པ་དེ་ནི་ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེག་པ༌[^554]ཡིན་ནོ། །

[Block 991]
དོགས་མེད་མི་གཡོ་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་གང་འདུག་པ་དང་། ཇི་ལྟར་འདུག་པ་དང་། ཅིའི་ཕྱིར་འདུག་པ་སྟེ། ཚིག་རྐྱང་པ་འདིའི་དོན་འདི་དག་ནི་ཚིགས་བཅད་ཀྱིས་སྒྲུབ་པའོ། །

[Block 992]
གང་འདུག་པ་ནི་ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེགས་པའོ། །

[Block 993]
ཇི་ལྟར་འདུག་པ་ནི་ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེགས་པར༌[^555]གྱུར་པ་ལས་ཤེས་པ་ཡིན་ཏེ། དེས༌[^556]སྨྲས་པ། དོགས་མེད་མི་གཡོ་བརྟན་ཞིང་ཞི་བའི་ཞེས་བྱ་བ་དེས་བསྟན་པ་སྟེ། དོགས་མེད་ཅེས་སྨོས་པས་ནི་མཐོང་བས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེགས་པར་བསྟན་ཏོ། །

[Block 994]
གང་གི་ཕྱིར་དོགས་པ་དང་མ་བྲལ་བ་ནི་བདག་ཏུ་ལྟ་བ་ཡིན་ཞིང་བདག་ཏུ་ལྟ་བ་ལ་འཇུག་པ་སྐྱེས་པ༌[^557]ཡིན་ཏེ། དེ་མེད་བས་ན་དེ་མེད་པར་རྗེས་སུ་དཔག་པ་ཡིན་ནོ། །

[Block 995]
མི་གཡོ་བ༌[^558]བརྟན་ཞིང་ཞི་བ་ཞེས་པ་དག་གིས་བསྒོམ་པས༌[^559]སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤངས་པར༌[^560]བསྟན་པ་ཡིན་ཏེ། གཏི་མུག་དང་། ཆགས་པ་དང་། ཞེ་སྡང་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་སྦྱར་ཏེ། ཀུན་ཏུ་རྨོངས་པས་ནི་ལྟ་བར་གཡོ་བར་འགྱུར་རོ། །

[Block 996]
ཆགས་པས་ནི་མི་བརྟན་པར་འགྱུར་རོ། །

[Block 997]
ཞེ་སྡང་གིས་ནི་མ་ཞི་བར་འགྱུར་ཏེ།[^561] ཉོན་མོངས་པ་དེ་དག་སྤངས་ཤིང་མེད་པའི་ཕྱིར་རོ། །

[Block 998]
མིག་གིས་ས་ལ་གཉའ་ཤིང་གང་དུ་ལྟ། །ཞེས་བྱ་བ་ནི་ཁྱིམ་དུ་འགྲོར་རུང་བའི་ལྟ་བ་དེས་དབང་པོའི་སྒོ་བསྡམས་པའོ། །

[Block 999]
རབ་ཏུ་ཞི་བར་གྱུར་ཅིང་ཞེས་བྱ་བ་འདིས་ནི་ཀུན་ཏུ་ལྟ་བ་ལ་སོགས་པ་ལ་ཤེས་བཞིན་དུ་ལྡན་པར་བསྟན་ཏོ། །

[Block 1000]
དེ་ན་སྡོད་ཅེས་བྱ་བ་ནི་སྒོ་གང་ན་སློང་བའི་དོན་དུའོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྨྲས་པ། དེའི་ལག་པདྨའི་མཆོག་ནི་ལྷུང་བཟེད་ཐོགས། །ཞེས་བྱ་བ་ནི་འདི་ཡིན་ཏེ། གང་གི་ཕྱིར་ལྷུང་བཟེད་ལག་ན་ཡོད་པ་ནི་སློང་བར་ཤེས་པ་ཡིན་ནོ། །

[Block 1001]
སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པ་དེ་ཞེས་བྱ་བ་ནི་ལེན་པ་དང་གཏོང་བ་པོ་ཕུན་སུམ་ཚོགས་པར་གྱུར་པས་སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ། འདིར་སྦྱིན་པའི་སྒྲ་ནི་རྒྱུད་ལ་སོགས་པ་ལ་ཡང་དག་པར་འཇུག་སྟེ། གང་གིས་སྦྱིན་པ༌[^562]དེ་ནི་སྦྱིན་པ་སྟེ། མཆོད་པ་དང་རྗེས་སུ་བཟུང་བའི་འདོད་པས་ལུས་དང་ངག་གི་ལས་སྤྲོ་བ་དང་བཅས་པའི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1002]
དེ་ལ་བགེགས་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་བར་དུ་གཅོད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1003]
བཟའ་བ་དང་བཅའ་བ་ཉིད་སྨོས་པ་ནི་དེ་ན༌[^563]བཏུང་བ་དང་བལྡག་པ༌[^564]ལས་དགར་བའོ། །

[Block 1004]
དེ་ལ་ཞེས་བྱ་བ་ནི་དམྱལ་བའི་གནས་སྐབས་ཀྱིས་སོ། །

[Block 1005]
དེས་སྨྲས་པ་ནི་དམྱལ་བ་ཞེས་བྱ་བའི་མིང་ཡང་མ་བརྗོད་ཅིང་དངོས་པོ་མ་སྨྲས་པ་ནི་དེས་སྨྲས་པའོ། །

[Block 1006]
ཁང་པའི་ངོས་ཀྱི་རྩིག་པ་ནས་བྱུང་སྟེ་བདག་གི༌[^565]ལུས་ཡ་མཚན་ཆེ་བ་བསྟན་པས་བར་སྣང་ལ་གནས་ཏེ།

[Block 1007 [VERSE]]
དེ་ལ་ཚིག་འདི་བསྟན་པའི་ཕྱིར་རོ། །
ཕོངས་པས་བསྔགས་པའི་ཚིག་གིས་བསླུས་ནས་ནི། །

[Block 1008]
ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་གྲགས་པའི་ཕན་ཡོན་གྱིས་སོ། །

[Block 1009]
ནོར་ཉམས་པའི་རྒྱུས་ནི༌[^566]ཉེས་པ་བསྒྲགས་པའི་ཕྱིར་བཤད་པ་ཡིན་ཏེ། ཇི་ལྟར་ནོར་ཆུད་ཟོས་ཤེ་ན། དེ་དག་ནི་ལོ༌[^567]སྟོང་ཕྲག་དུ་མར་ཡང་། དམྱལ་བ་འདི་ན་གནས་འགྱུར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1010]
དེ་བསྒྲུབ་པའི༌[^568]ཕྱིར། ནོར་ནི་འཁོར་གསུམ་ཁྱད་པར་རྒྱུ་ཡིན་ཏེ། །ཞེས་བྱ་བའི་ཚིགས༌[^569]བཅད་ཡིན་ཏེ། ཇི་ལྟར་ནོར༌[^570]འཁོར་གསུམ་གྱི་ཁྱད་པར་གྱི་རྒྱུ་ཡིན་ཞེ་ན། འདི་ལྟར་ནོར་ནི་ཆོས་དང་དོན་དང་འདོད་པ་རྣམས་ཀྱི་མངོན་སུམ་དང་། བརྒྱུད་པའི་ཚུལ་གྱིས་ཏེ། ཇི་ལྟར་མངོན་སུམ་གྱི་རྒྱུ་ཡིན་ཞེ་ན། མཐོང་བ་ཉིད་ཀྱི་ཆོས་ལ་ཞིང་ལ་ནོར་སྐྱེད་པས་ཆོས་ཀྱི་རྒྱུ་ཡང་ནོར་ཡིན་ནོ། །

[Block 1011]
ནོར་ཡང་ནོར་ཉིད་ཀྱི༌[^571]རྒྱུ་ཡིན་ཏེ།

[Block 1012 [VERSE]]
ནོར་དང་ནོར་ནི་འབྲེལ་པ་སྟེ། །
གླང་པོ་ནགས་ཀྱི་གླང་པོ་བཞིན། །

[Block 1013]
ཞེས་བྱ་བའི༌[^572]ཚིག་གིས་སོ། །

[Block 1014]
འདོད་པའི་ཡང་རྒྱུར་གྱུར་པ་ཉིད་དེ་བརྒྱུད་པའི་ཚུལ་གྱིས་ཀྱང་ནོར་དང་ཆོས་ཀྱི་བྱ་བ་ཡིན་ཏེ། དེ་ཡང་རང་གི་ཆོས་ཀྱིའོ། །

[Block 1015]
རྟག་ཏུ་ཡང་ཆོས་དང་། ནོར་དང་།

[Block 1016 [VERSE]]
འདོད་པ་རྣམས་ཀྱི་རྒྱུར་གྱུར་པ་ཉིད་དོ། །
ཆོས་ཀྱང་འཁོར་གསུམ་གྱི་རྒྱུ་ཡིན་ཏེ།
རྒྱུན་དུ་འཁོར་གསུམ་གྱི་རྒྱུར་གྱུར་པས་སོ། །

[Block 1017]
མཐོང་བའི་ཆོས་ལ་ཡང་རེས་འགའ་དོན་དང་། འདོད་པའི་རྒྱུར་གྱུར་པ་ཡིན་ནོ། །

[Block 1018]
དེའི་ཕྱིར་ན་ཁྱད་པར་གྱི་རྒྱུ་ཞེས་སྨོས་སོ། །

[Block 1019]
དེ་མེད་བྱས་ན་ཞེས་བྱ་བ་ནི་འཁོར་གསུམ་གྱི་ཁྱད་པར་གྱི་རྒྱུ་ནོར་དང་ཆོས་མེད་པར་བྱས་ན་ཉམས་པར་བྱས་པའོ། །ཇི་ལྟར་ཞེ་ན། སྨྲས་པ། ནོར་ཆུད་གསན་པས་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་ལྟར་ནོར་ཉམས་པར་བྱས་ན་དམྱལ་བར་གནས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1020]
དམྱལ་བར་གནས་པར་འགྱུར་བ་དེ་ལྟར་རབ་ཏུ་བསྒྲུབ་པའི༌[^573]ཕྱིར། སྦྱིན་པའི་ཕྱིར་ནི་ཆོས་ཀྱི་རྩར་གྱུར་པའི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །
--- END BLOCKS ---
