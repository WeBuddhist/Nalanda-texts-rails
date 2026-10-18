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
[Block 1016]
ཇི་ལྟར་བདག་གིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་ནུས་ཞེས་དོན་དེ་ལྟ་བུར་བྱུང་བའོ། །

[Block 1017]
ལེགས་ཡིད་ཀྱིས༌[^689]ཞེས་བྱ་བ་ནི་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་མ་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། འདི་ལྟར་ལུང་དུ་མ་བསྟན་པ་ནི་རྣམ་པར་གཡེང་བའི༌[^690]སེམས་ཁ་ཅིག་གིས་སྦྱིན་པ་ལ་སོགས་པ་བྱེད་པའོ། །

[Block 1018]
དེ་བཞིན་དུ་མུ་སྟེགས་པ་ལ་སོགས་པ་མི་དགེ་བའི་སེམས་ཀྱིས་སྦྱིན་པ་ལ་སོགས་པ་བྱེད་པ༌[^691]མ་ཡིན་ཏེ། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་པས་སོ། །

[Block 1019]
ཡང་ན་དེའི་བསམ་པས་དགེ་བའི་རྩ་བ་མཆོག་ཐོབ་པ་ནི་བསྟན་པ༌[^692]རྣམས་སོ། །

[Block 1020]
སྦྱིན་པ་ལ་སོགས་པ་བྱེད་པའི་ཞེས་བྱ་བ་ལ། དེ་ལ་དེའི་བསམ་པ་ཅི་འདྲ་བ་ཅིག་ཐོབ་ནས་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་གོམས་པར་བྱས་པས་དེའི་མི་མཐུན་པའི་ཕྱོགས་སེར་སྣ་ལ་སོགས༌[^693]སྤངས་པའི་སེམས་ཐོབ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1021 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་བརྟན་རྣམས་ཀྱི། །
སྦྱིན་པ་ལ་སོགས་ཉིད་དུ་བརྗོད། །

[Block 1022]
ཅེས་བྱ་བ་ནི་སྦྱིན་པ་ལ་སོགས་པ་ཁོ་ནར་བརྗོད་པའོ། །

[Block 1023]
སོགས་པ་སྨོས་པས་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ནས། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་གཟུང་ངོ་། །འདོད་བཞིན་ཕུན་སུམ་ཚོགས་ལུས་འཐོབ། །ཅེས་བྱ་བ་ནི་འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་ཀྱི་བར་འཐོབ་པ་སྟེ། འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1024]
སྤངས་པ་ཞེས་བྱ་བ་ནི་སྒྲིབ་པ་སྤངས་པའོ། །

[Block 1025]
ཕུན་སུམ་ཚོགས་དེ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1026 [HEADING]]
##### གནས་བཞི་སྤང་བ། ^3-2-4-3-0

[Block 1027]
གང་གནས་བཞི༌[^694]སྤང་བར་བྱ་བ་དེ་བསྟན་པར་བྱ་སྟེ། ཡིད་ལ་བྱེད་པ་ཡོངས་སུ་སྤོང་བ་ཞེས་པ༌[^695]ནི་ཉན་ཐོས་ལ་སོགས་པའི་ཡིད་ལ་བྱེད་པ་ཡོངས་སུ་སྤོང་བའོ། །

[Block 1028]
ཡིད་གཉིས་དང་སོམ་ཉི་སྤངས་ནས་ཞེས་བྱ་བ་ནི་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་ཐེག་པ་ཆེན་པོ་ལ་ཡིད་གཉིས་དང་སོམ་ཉི་སྤངས་པའོ། །

[Block 1029]
དེ་ལ་ཡིད་གཉིས་ནི་བློ་ངན་པའམ་དེ་བཞིན་དུ་གཡོ་བའོ། །

[Block 1030]
སོམ་ཉི་ནི་ཐེ་ཚོམ་མོ། །

[Block 1031]
ཆོས་ལ་མངོན་པར་ཞེན་པ་སྤངས་པས་ཞེས་བྱ་བ་ནི་ཇི་སྙེད་ཐོས་པ་དང་བསམས་པའི་ཆོས་རྣམས་ལ་བདག་ཏུ་འཛིན་པ་དང་བདག་གིར་འཛིན་པ་ཡོད་ཀྱི་བར་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 1032]
རྣམ་པར་རྟོག་པ་སྤངས་པས་ཞེས་བྱ་བ་ནི་གང་གཟུགས་ལ་སོགས་པ་མདུན་ན་གནས་པ་དང་། གང་ཡང་མཉམ་པར་བཞག་པས་རུས་པའི་ཕུང་པོ་ལ་སོགས་པ་དམིགས་པར་འགྱུར་བའི་མཚན་མ་ཐམས་ཅད་ཡིད་ལ་མི་བྱེད་པས་རྣམ་པར་བརྟག་པར་བྱ་བ་ལ་རྣམ་པར་མི་རྟོག་པའི་ཐབས་ཀྱིས་འཇུག་པར་འགྱུར་གྱི། གཞན་དུ་རྣམ་པར་རྟོག་པར་གྱུར༌[^696]ན་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 1033]
མདུན་བཞག་དང་ཞེས་བྱ་བ་ནི་ཚིགས་སུ་བཅད་པ་སྟེ། སྤང་བར་བྱ་བའི་དོན་ཕྱི་མ་གསལ་བར་བྱེད་པའོ། །

[Block 1034 [HEADING]]
#### གང་གིས་ཇི་ལྟར་འཇུག་པ། ^3-2-5-0

[Block 1035]
གང་གིས་ཇི་ལྟར་འཇུག་པ་དེ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་ཐོས་པའི་བག་ཆགས་ཀྱི་རྒྱུ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཐོས་པའི་བག་ཆགས་ཀྱི་རྗེས་སུ་མཐུན་པའོ། །

[Block 1036]
གང་དུ་འཇུག་པའི་གནས་ནི་སྔར་བསྟན་པ་སྟེ། དེ་ཡང་ཐེག་པ་ཆེན་པོའི་བག་ཆགས་ལས་ཡང་དག་པར་བྱུང་བའི་ཕྱིར་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཀྱིས་བསྡུས་པ་ཉིད་དུ་བལྟ༌[^697]བར་བྱའོ། །

[Block 1037]
ཡང་ཇི་ལྟར་འཇུག་པ་དེ་སྟོན་པར་བྱེད་པ་ནི་ཚོལ་བ་རྣམ་པ་བཞི་སྟེ། དེ་སྟོན་པར་བྱེད་པ་ཡང་མིང་དང་དོན་དང་། ངོ་བོ་ཉིད་ལ་སོགས་པ་ཚིག་བཞི་པོ་དེ་དག་གིས་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་མདོར་སྟོན་ཏེ་མིང་དང་། དོན་དང་། ངོ་བོ་ཉིད་དང་། ཁྱད་པར་དུ་བཏགས་པ་དང་། ངོ་བོ་ཉིད་དང་། ཁྱད་པར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་ཞེས་བྱ་བ་ལ། ངོ་བོ་ཉིད་ཀྱི་ཁྱད་པར་གང་བཏགས་པ་དེ་བཞིན་དུ་བྱས་པའོ། །

[Block 1038]
མིང་ཁྱད་པར་དུ་བཏགས་པ་ནི༌[^698]ཞེས་བྱ་བ་ནི་དེ་མི་དམིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1039]
མི་དམིགས་པ་ནི་མིང་དེའི་ངོ་བོ་ཉིད་དང་ཁྱད་པར་དུ་བཏགས་པ་ཙམ་དཔྱོད་པར་བྱེད་པའོ། །

[Block 1040]
གང་གི་ཕྱིར་དེ་ལྟར་ན་མིང་དེའི་ངོ་བོ་ཉིད་དང་ཁྱད་པར་མེད་པ་དེས་ན་མིང་དེའི་ངོ་བོ་ཉིད་བཏགས་པ་ཙམ་དུ་འཛིན་པའོ། །

[Block 1041]
གང་ཡང་དག་པར་དཔྱོད་པ་ནི་ཡོངས་སུ་ཚོལ་བའོ། །

[Block 1042]
གང་མི་དམིགས་པ་ནི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པའོ། །

[Block 1043 [HEADING]]
#### ཅི་འདྲ་བར་འཇུག་པ། ^3-2-6-0

[Block 1044]
འཇུག་ཅེས་ནི་ཇི་སྐད་བྱ། ཅི་འདྲ་བར་འཇུག་ཅེ་ན་ཞེས་བྱ་བ་ནི་དཔེ་དྲིས༌[^699]པའོ། །

[Block 1045]
དེ་ལ་དེ་ཙམ་ཉིད་ཅེས་བྱ་བ་ནི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དོ། །

[Block 1046]
རྒྱུ་མཚན་དང་ལྟ་བ་དང་བཅས་པ་གཉིས་ཞེས་བྱ་བ་ནི། རྒྱུ་མཚན་དང་ལྟ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ་བསྟན་ཏེ། རྒྱུད༌[^700]རབ་ཏུ་གནས་པ་དང་། རྒྱུ་མཚན་དུ་སྣང་བ་ཞེས་བྱ་བར་གྲགས་པ་དེ་ལྟ་བུའི་རྣམ་པར་ཤེས་པ་གཅིག་ཉིད་རྣམ་པ་སྣ་ཚོགས་སུ་འབྱུང་བ་སྟེ། མྱུར་བ་ཉིད་དུ༌[^701]བརྒྱུད་མར་འབྱུང་བས་སོ། །

[Block 1047]
གསུམ་པོ་འདི་དག་ཉིད་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་འཇུག་གོ། །

[Block 1048]
དེ་ལ་ངོ་བོ་ཉིད་གསུམ་ལ་འཇུག་པ་ནི་དཔེ་བསྟན་ཏེ།[^702] རྣམ་པ་དྲུག་ལ་ཡང་དག་པའི་དོན་གསལ་ཞེས་བྱ་བ་ལ། དོན་གྱི་རྣམ་པ་དྲུག་ལ་ཡང་དག་པའི་དོན་རྣམ་པར་གསལ་བ་ཙམ་ནི་རྣམ་པར་གསལ་བའོ། །

[Block 1049]
ཡིད་ཀྱི་བརྗོད་པར་སྣང་བའི་དོན་གྱི་མཚན་ཉིད་ལ་འཇུག་པས་ཞེས་བྱ་བ་ནི་དོན་གང་ཡིན་པ་དེ་ཀུན་དུ་བརྟགས་པ་ཙམ་ཡིན་ནོ་ཞེས་དེ་ལྟར་ཀུན་དུ་བརྟགས་པ་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 1050]
ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་རིག་པའི་ངོ་བོ་ཙམ་ལ་འཇུག་ཅེས་བྱ་བ་ནི་ཡིད་ཀྱི་བརྗོད་པ་དེ་དག་གིས་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་བཟུང༌[^703]ནས་གཞན་གྱི་དབང་ལ་འཇུག་པར་འགྱུར་རོ།། །།

[Block 1051]
བམ་པོ་ལྔ་པ། དོན་དུ་སྣང་བ་ཐམས་ཅད་འབྱུང་བའི་སྐབས་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རྣམ་པར་རིག་པ་ཙམ་གྱི་རྣམ་པར་ཡང་མི་འབྱུང་ན་དེ་དོན་གྱི་རྣམ་པར་སྣང་བ་འབྱུང་བ་ལྟ་ཅི་སྨོས་ཏེ། དེའི་ཕྱིར་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་བརྟགས་ན་ཡང་དོན་དུ་འགྱུར་བས། དེའི་ཕྱིར་དེ་ལས་གཞན་པ་དེ་བཞིན་ཉིད་མངོན་སུམ་ཉིད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1052]
གནས་སྐབས་དེ་ནི་བརྗོད་པར་ནུས་པ་མ་ཡིན་ཏེ། སོ་སོ་རང་གིས་རིག་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1053]
དེའི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་དེའི་དམིགས་པར་བྱ་བ་དང་དམིགས་པར་བྱེད་པ་མཉམ་པས་མཉམ་པའི་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པ་འབྱུང་སྟེ་ཞེས་བྱ་བ་ལ་དམིགས་པར་བྱེད་པ་ནི་ཡེ་ཤེས་དང་དམིགས་པར་བྱ་བ་དེ་ནི་དེ་བཞིན་ཉིད་དེ། དེ་དག་མཉམ་པ་ཉིད་དུ་གྱུར་པ་ནི་ནམ་མཁའ་ཉིད་དུ་གཟུང་བ༌[^704]དང་། འཛིན་པ་མེད་པར་གནས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། གཟུང་བ་དང་འཛིན་པར་རྣམ་པར་རྟོག་པ་མེད་པ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1054]
དེ་ལྟར་ན་ཡོངས་སུ་གྲུབ་པ་ཉིད་ལ་ཞུགས་པ་ཡིན་ནོ། །

[Block 1055 [HEADING]]
#### མིང་གི་བྱེ་བྲག། ^3-2-7-0
--- END BLOCKS ---
