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
[Block 876]
ལག་པ་དང་ཁའི་ཆུ་མི་བླུགས་སོ། །

[Block 877]
དགེ་ཚུལ་བག་མེད་པའི་ཆོས་ཅན་བྱི་དོར་བྱེད་དུ་མི་གཞུག་གོ། །

[Block 878]
བྱེ་མ་ཅན་དང་ལྕི་བས་མི་བྱའོ། །

[Block 879]
ཧ་ཅང་གཤེར་བཞིན་དུ་ཕྱིར་མི་གཞུག་གོ། །

[Block 880]
ཧ་ཅང་བསྐམ་པར་མི་བྱའོ། །

[Block 881]
རྡོའི་སྟེང་དུ་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་གཞག་པ་འདི་ནི་རེ་ཞིག་གི༌[^631]དུས་ཅན་ནོ། །

[Block 882]
མི་གཙང་བའི་ཕྱོགས་སུ་མི་གཞག་གོ། །

[Block 883]
གར་བབ་བབ་ཏུ་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་ཕྱོགས་ཞེས་པ་དང་མི་གཞག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 884]
དེར་མི་བཞག་གོ་ཞེས་བྱ་བ་ལ། གར་བབ་བབ་ཏུ་འདི་ནི་གཏན་དུ་གཞག་པའི་ཕྱིར་དགག་པ་ཡིན་གྱི་རེ་ཞིག་ཁོ་ན་ནི་མ་ཡིན་ནོ། །

[Block 885]
དེའི་ཆེད་དུ་ངོས་ཁུང་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་གཞག་པའི་དོན་དུའོ། །

[Block 886]
ངོས་ཁུང་ཞེས་བྱ་བ་ནི་ཁུང་བུའི་མིང་ངོ་། །ངོས་ཁུང་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གཙུག་ལག་ཁང་དང་ཁང་ཁྱིམ་དག་རྩིག་པའི་ཚེ་བྱའི་རྩིག་པ་རྐོ་བས་ནི་མ་ཡིན་ནོ། །

[Block 887]
དགོན་པ་པ་རྣམས་ཀྱིས་སྐོན་བུ་ཁ་སྦྱར་བར༌[^632]བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷུང་བཟེད་གཞག་པའི་ཕྱིར་བྱ་བའོ། །

[Block 888]
ནམ་མཁའ་ལ་ངོས་ཁུང་ཞེས་བྱ་བ་འདི་ལ་འདོན་པ་གཞན་ལ་ཐ་སྙད་དོ། །དེ་ཅི་ལས་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྕུག་མ་འམ་སྲད་བུ་ལས་བྱས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲད་བུའི་རང་བཞིན་གྱི་རྣམ་པར་འགྱུར་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 889]
ལྕི་བ་དང་སས་བྱུགས་པས་སོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་རང་བཞིན་གྱི་ཁ་གབ་ལའོ། །

[Block 890]
འདི་ལ་ཁ་གབ་ཀྱང་ལྕུག་མའི་རང་བཞིན་ནམ་སྲད་བུའི་རང་བཞིན་པའི་ལྕི་བ་དང་སས་བྱུག་པ༌[^633]བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 891]
དེར་ནི་གཟར་ཐག་གིས་ཤིང་ལ་དཔྱངས༌[^634]ན་བཟང་ངོ་། །ས་ལ་མི་བཞག་གོ། །

[Block 892]
དེ་གཞན་དུ་མི་བསྐུར༌[^635]རོ་ཞེས་བྱ་བ་ནི་སྐོན་བུའོ། །

[Block 893]
དེ་བསྐུར་བ༌[^636]ནི་ལུང་ཐག་བཏགས་ཏེ་ལྷུང་བཟེད་ལའོ། །

[Block 894]
ལག་པས་ཞེས་བྱ་བ་ནི་མི་བསྐུར༌[^637]བའོ། །

[Block 895]
དེ་མཆན་ཁུང་གིས་སོ་ཞེས་བྱ་བ་ནི༌[^638]ལྷུང་བཟེད་དོ། །

[Block 896]
ཁུར་བ་ན་དཔྱང༌[^639]ཐག་བཏགས་ནས་སོ། །

[Block 897]
ལྷུང་བཟེད་དང་སྨན་དང་བར་བུར་དག་སྣོད་ཐ་དད་པར་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ལྷུང་བཟེད་དང་། གཞན་ལ་སྨན་དང་གཞན་ལ་བར༌[^640]བུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 898]
བར་བུར་ཞེས་བྱ་བ་ཡང་སྨྱུང་བུ་དང་རྒྱུན་ལ་སོགས་པར་བལྟ་བར་བྱའོ། །

[Block 899]
དེ་དག་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལ་སོགས་པའི་སྣོད་རྣམས་སོ། །

[Block 900]
དེ་དག་ལ་དཔྱང༌[^641]བའི་ལུང་ཐག་མཉམ་པར་གདགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱིང་པ་ཉེ་བར་སྦྱར་བའོ། །

[Block 901]
དེ་དག་ལ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལ་སོགས་པའི་སྣོད་རྣམས་ཀྱི་ལུང་ཐག་མཉམ་པར་སྦང་བས་གདགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 902]
དེ་ལྟར་ཡང་གླེང་གཞི་ནི་འཕགས་པ་ཅི་ཞིག་འདི་རྫ་རྔ་འམ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 903]
དེ་བས་ན་མཉམ་པར་གཞག་པའི་དོགས་པ་དགག་པའི་གཙོ་བོ་འདི་ཡིན་ཏེ། སྡུག་བསྔལ་མི་འདོད་པས་ནི་ཞེང་ཆུང་ངུ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དཔྱང༌[^642]ཐག་རྣམས་ལ་ཕྱིང་བུས་སྦྱར་བར་བྱའོ། །

[Block 904]
རྒྱུ་ཅིའི་ཕྱིར་ཞེ་ན། སྡུག་བསྔལ་མི་འདོད་པས་ནི་ཞུམ་པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་འདོད་པ་སྦྱིན་པ་མ་ཡིན་ནོ། །

[Block 905]
འདོད་པ་མི་སྦྱིན་པ་ཕྱོགས་གང་ལས་ཤེ་ན། དེའི་ཕྱིར་དབུས་སུ་ཞེས་བྱ་བ་སྨོས་ཏེ། དཔྱང༌[^643]ཐག་ཅེས་བྱ་བ་སྐབས་ཀྱིས་གོ་བར་བྱའོ། །

[Block 906]
ཐ་དད་པ་ཉིད་འདིའི་དབུས་སུ་སྟེ་རིང་པོ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི༌[^644]དོན་གྱིས་གོ་བར་བྱའོ། །

[Block 907]
དེ་གནས་པར་བྱ་བའི་ཕྱིར་མདོ་མདོར་བྱ་རོག་རྐང་བྱའོ། །

[Block 908]
ལྷུང་བཟེད་མིག་བཞིན་དུ་བསྐྱང་བར་བྱའོ། །

[Block 909]
སྣམ་སྦྱར་པགས་པ་དང་འདྲ་བར་རོ། །

[Block 910]
ཆོས་གོས་ལྷག་མ་ཡང་ངོ་། །བཅོས་ལེགས་བྱ་བ་ཡལ་བར་མི་འདོར༌[^645]རོ་ཞེས་བྱ་བ་ནི་ལྷན་པ་དང་བསྲོ་བ་དང་འཁྲུ་བ་དང་བསྟེན་པ་དང་ཁ་བསྒྱུར་བ་རྣམས་ཏེ། ལྷུང་བཟེད་དང་ཆོས་གོས་གཉིས་ལ་ལྟོས་ནས་ཆོ་ག་འདིའོ། །

[Block 911]
འདིར་ལྷན་པ༌[^646]ནི་དབེན་པའི་ཕྱོགས་སུ་བསྒྲུབ་པར་བྱའོ། །

[Block 912]
སོ་སོར་མ་སྦས་པར་འདི་བྱེད་པར་གྱུར་ན་མ་དད་པ་སྐྱེ་བའི་དངོས་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་བསྟན་པའི་ཕྱིར་མདོ་འདིའོ། །

[Block 913]
དགེ་འདུན་གྱིས་མགར་སྤྱད་དག་བསྲེལ་བར་བྱའོ། །

[Block 914]
བུ་གུ་དེའི་ཞེས་བྱ་བ་ནི་ལྷན་པའོ། །

[Block 915]
བུ་རམ་དང་རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མ༌[^647]དང་སྤྲ་ཚིལ་དང༌[^648]ཞ་ཉེ་དཀར་པོ་དང་ཞ་ཉེ་ནག་པོ་རྣམས་ཀྱིས་མི་བཟང་ངོ་། །འོ་ན་གང་བཟང་ཞེ་ན། དེའི་ཕྱིར་ལྷན་རིངས་དང་ཐམ་ཕྲན༌[^649]དང་ལྷན་པ་དང་ཆུ་སྲིན་གྱི་སོ་ལྟ་བུ་དག་བཟང་ངོ་ཞེས་བྱ་བ་དག་སྨོས་ཏེ། ཕྱེ་མས་ཀྱང་ངོ་། ། ལྕགས་ཀྱི་འམ་རྡོའིའོ། །
--- END BLOCKS ---
