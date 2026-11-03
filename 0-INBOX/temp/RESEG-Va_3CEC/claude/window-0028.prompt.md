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
དེ་ལྟར་སྙིང་རྗེས་སྐྱེད་པར༌[^860]བྱེད་པས་ན། འདི་ལྟར་བྱ་བ་བྱེད་པའི་ཕྱིར་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 982]
གང་བྱེད་ཅེ་ན། འདི་ལྟར་སྦྱིན་པར་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གཞན་ནི་གོ༌[^861]སླ་བས་མ་བཤད་དོ། །

[Block 983]
གདོན་མི་ཟ་བར་བྱེད་ཅེས་བྱ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པའམ། ཆུད་མི་ཟ་བར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 984]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་བྱ་བ་ཇི་སྙེད་ཡོད་ཅེས་སོ་སོར་ཉེ་བར་གནས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ལས་སུ་བྱ་བ་དང་། ཕན་པ་དང་བདེ་བར་བྱ་བ་ཅི་ཡོད་ཅེས༌[^862]རྟག་ཏུ་རྟོག་པར་བྱེད་པ་གནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 985]
སྙིང་རྗེ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 986 [HEADING]]
### བདེ་བ་ལ་རྗེས་སུ་ཡི་རང་བ། ^2-3-0

[Block 987]
བདེ་བ་ལ་རྗེས་སུ་ཡི་རང་བ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^863]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^864]དགའ་བ་ཆེན་པོ་ཡང་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དགའ་བ་མི་ཟད་པ་ཡང་དམིགས་པའི་ཡུལ་ཆོས་དང་། སེམས་ཅན་མི་ཟད་པས་དེ་ལ་དམིགས་པར་བྱེད་པའི་དགའ་བ་ཡང་མི་ཟད་པ་སྟེ། བྱམས་པ་དང་སྙིང་རྗེ་མི་ཟད་པ་བཞིན་ནོ། །

[Block 988]
ཆེན་པོ་ནི་དེ་དག་གི་དགའ་བ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལ་སོགས་པ་ལས་ཀྱང་ཁྱད༌[^865]ཞུགས་པའི་ཕྱིར་རོ། །

[Block 989 [HEADING]]
#### དགའ་བ་ཆེན་པོ་གང་ཡིན་པ་དང་ཇི་ལྟར་མི་ཟད་པ། ^2-3-1-0

[Block 990]
དགའ་བ་ཆེན་པོ་གང་ཡིན་པ་དང་། ཇི་ལྟར་མི་ཟད་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་དགའ་བ་ཆེན་པོ་གང་ཞེ་ན། སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་དྲན་པ་དང་རྗེས་སུ་དྲན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་ནི་ལུང་གི་ཆོས་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་དང་། རྟོགས་པའི༌[^866]ཆོས་འཕགས་པའི་ལམ་མྱ་ངན་ལས་འདས་པའོ། །

[Block 991]
དེ་དག་གི་ཡོན་ཏན་སེམས་པའི་དུས་ན་མ་བརྗེད་པ་ནི་རན་པའོ། །

[Block 992]
བསྒོམ་པའི་དུས་ན་མ་བརྗེད་པ་ནི་རྗེས་སུ་དྲན་པའོ། །

[Block 993]
ཆོས་དེ་ཡང་དུས་གསུམ་གྱི་དབྱེ་བས་དགའ་བ་རྣམ་པ་གསུམ་དུ་འགྱུར་ཏེ། འདས་པའི་ཆོས་ལ་དམིགས་ནས་དགའ་བར་འགྱུར་བ་དང་། ད་ལྟར་བྱུང་བའི་ཆོས་ལ་དམིགས་ནས་དགའ་བར་འགྱུར་བ་དང་། མ་འོངས་པའི་ཆོས་ལ་དམིགས་ནས་དགའ་བར་འགྱུར་པའོ། །

[Block 994]
དེ་ལ་འདས་པའི་དུས་སུ་ལུང་དང་རྟོགས་པའི་ཆོས་རྟོགས་པ༌[^867]རྣམས་དྲན་ནས་སེམས་ལ་སྤྲོ་བ་སྐྱེ་བ་ནི་དགའ་བ་ཞེས་བྱའོ། །

[Block 995]
ད་ལྟར་གྱི་དུས་སུ་ལུང་དང་རྟོགས་པའི༌[^868]ཆོས་རྣམས་བདག་གིས་རྟོགས་པར་ནུས་སོ་སྙམ་དུ་སེམས་ལ་སྤྲོ་བ་སྐྱེ་བ་ནི་མོས་པའོ། །

[Block 996]
མ་འོངས་པའི་དུས་སུ་ལུང་དང་རྟོགས་པའི་ཆོས་དང་། སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་རྣམས་ཐོབ་པར་འགྱུར་རོ་སྙམ་དུ་སེམས་ལ་དགའ་ཞིང་སྤྲོ་བ་སྐྱེ་བ་ནི་མཆོག་ཏུ་དགའ་བའོ། །

[Block 997]
སེམས་མ༌[^869]གོང་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆུང་ངུའི་ཆོས་ཀྱི་ཡོན་ཏན་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཐེག་པ་ཆུང་ངུར་སེམས་མི་སྐྱེ་བའམ། བདག་གིས་མི་ནུས་སོ་སྙམ་དུ་སེམས་ཞུམ་པ་མེད་པའི་ཕྱིར་མ་གོང་བའོ། །

[Block 998]
མི་བརྫི་བ༌[^870]ནི་དགའ་བའི་མི་མཐུན་པའི་ཕྱོགས་མི་དགའ་བས་ཟིལ་གྱིས༌[^871]མི་ནོན་པའོ། །

[Block 999]
སྲེད་པ་མེད་པ་ནི་སྲེད་པ་ལས་མྱ་ངན་དང་། མི་དགའ་བ་སྐྱེའི་ཆགས་ཤིང་སྲེད་པ་མེད་པ་དང་མི་དགའ་བ་སྐྱེ་བའི་རྒྱུ་མེད་པའི་ཕྱིར་རྟག་ཏུ་དགའ་བ་ཉིད་ལ་གནས་སོ། །

[Block 1000]
འདོད་པའི་དགའ་བ་ཐམས་ཅད་གཏོང་བ་ཞེས་བྱ་བ་ནི་འདོད་པའི་ཡོན་ཏན་ལ་དགའ་བའི་དགའ་བ་ཐམས་ཅད་འདོར་བའོ། །

[Block 1001]
ཆོས་ཀྱི་དགའ་བ་ཐམས་ཅད་ཀྱི་རྟེན་དང་ཞེས་བྱ་བ་ནི་དགའ་བ་མི་ཟད་པ་ཉིད་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཆོས་ཐམས་ཅད་སྤྱད་པར་དགའ་ཞིང་སྤྲོ་བའི་གཞི་དང་རྟེན་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1002]
སེམས་མཆོག་ཏུ་དགའ་བ་དང་ཞེས་བྱ་བ་ནི་དགའ་བ་ཆེན་པོ་ལ་གནས་པའི་རྒྱུས་སེམས་ལས་སུ་རུང་བ་སྐྱེ་བས་ན་སེམས་མཆོག་ཏུ་དགའ་བའོ། །

[Block 1003]
དེ་ཉིད་ཀྱི་རྒྱུས་ལུས་ལས་སུ་རུང་བ་སྐྱེ་བའི་ཕྱིར། ལུས་རབ་ཏུ་སིམ་པའོ། །

[Block 1004]
སངས་རྒྱས་ལ་དགའ་ཞིང་ཡི་རངས་པ༌[^872]དང་ཞེས་བྱ་བ་ལ། སངས་རྒྱས་ལ་མོས་པ་ནི་སངས་རྒྱས་ལ་དགའ་བའོ། །

[Block 1005]
དགའ་བ་དེ་ཉིད་ཆུའི་དབའ༌[^873]བདོ་བ་བཞིན་དུ་ཤས་ཆེར་གྱུར་ཅིང་སེམས་སྤྲོ་བ་གོང་ནས་གོང་དུ་འཕེལ་བར་གྱུར་པ་ནི་ཡི་རངས་པའོ། །

[Block 1006]
དེ་བཞིན་གཤེགས་པའི་སྐུ་ལ་དགའ་ཞིང་མོས་པ༌[^874]ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་སྐུ་གསུམ་ཐོབ་པར་དགའ་ཞིང་མོས་པ༌[^875]ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་བས་ན་མཚན་དང་དཔེ་བྱད་བཟང་པོའི་རྒྱན་ཚོལ་བ་ལ་མཁས་པ་སྟེ། དེ་དག་ཐོབ་པར་བྱ་བའི་ཐབས་ལ་མཁས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1007]
དགེ་བའི་ཆོས་མཉན་པས་མི་སྐྱོ་བ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཉིད་ཐོག་མར་ཡང་དགེ་བར་དུ་ཡང་དགེ་ཐ་མར་ཡང་དགེ་བ་ཡིན་པས་དགེ་བའི་ཆོས་ཏེ། དེ་མཉན་པ་ལ་ཆོག་པ་མེད་ཅིང་མི་སྐྱོ་བ་ཉིད་དགའ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1008]
དེ་ཁོ་ནའི་ཆོས་ལ་རྟེན་པའི༌[^876]ནན་ཏན་དང་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་དེ་ཁོ་ན་རྟོགས་པར༌[^877]བྱ་བའི་ཕྱིར་ལམ་ལ་སོགས་པ་སྒྲུབ་པའི་ནན་ཏན་བྱེད་པ་ལ་སེམས་སྤྲོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1009]
དཀོན་མཆོག་གསུམ་དང་དེའི་ཡོན་ཏན་ལ་དད་པའི་སྒོ་ནས་དགའ་བ་སྐྱེ་བ་ནི་དགའ་བའོ། །

[Block 1010]
དེའི་ཡོན་ཏན་ཕྱིན་ཅི་མ་ལོག་པར་ཁོང་དུ་ཆུད་ནས་སེམས་དང་བར་གྱུར་པ་ནི་དད་པའོ། །

[Block 1011]
ཆོས་ཀྱི་དབྱིངས་ལ་དམིགས་པའི་སྒོ་ནས་དགའ་བའམ་ཚིམ་པར་གྱུར་པ་ནི་མཆོག་ཏུ་དགའ་བའོ། །

[Block 1012]
བདག་གི་ཆོས་ཉིད་རྟོགས་ཤིང་ཆོས་ཉིད་ཁོང་དུ་ཆུད་པའི་ཁྱད་པར་ལས་སྐྱེས་པའི་དགའ་བས་སེམས་གཟེངས༌[^878]མཐོ་བའམ། སྤྲོ་བ་སྐྱེས་པ་ནི་རབ་ཏུ་དགའ་བ་སྟེ། རྣམ་པ་དེ་བཞི་ལྟ་བུས་ཆོས་ལ་དགའ་བ་ནི་མོས་པའོ། །

[Block 1013]
ཁོང་ཁྲོ་བ་མེད་པའི་བློ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་ལ་ཞེ་སྡང་མེད་པའི་སེམས་ཞེས་བྱ་སྟེ། སེམས་ཅན་རྣམས་ལ་རྟག་ཏུ་རྒྱུན་མི་འཆད་པར་དགའ་བར་དམིགས་པའི་སེམས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1014]
སངས་རྒྱས་ཀྱི་ཆོས་ཚོལ་བ་ལ་ཤིན་ཏུ་འདུན་པ༌[^879]དང་ཞེས་བྱ་བ་ལ་སོགས་པས་སངས་རྒྱས་ཀྱི་ཆོས་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ཚོལ་ཞིང་ཐོབ་པར་བྱ་བ་ལ་འདུན་པ་ཡང་དགའ་བ་ཡིན་ལ། དེ་ལྟར་ཡོན་ཏན་གྱི་ཆོས་སྒྲུབ་པའི་ཆོས་ལ་འདུན་པ་དེ་མི་འདོར་བ་ཡང་དགའ་བ་ཡིན་པར་སྟོན་ཏོ། །

[Block 1015]
སངས་རྒྱས་ཀྱི་ཆོས་རྒྱ་ཆེན་པོ་ལ་མོས་ཤིང་རྣམ་པར་གྲོལ་བ་དང་། ཉི་ཚེ་བའི་ཐེག་པ་ལས༌[^880]བསལ་ཏེ་སེམས་བསྐྱེད་པ་དང་ཞེས་བྱ་བ། [^881]སངས་རྒྱས་ཀྱི་ཆོས་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དད་པས་ཐེག་པ་ཆུང་ངུ་ལ་སེམས་མི་སྐྱེ་བར་ཐེག་པ་ཆེན་པོ་ལ་སེམས༌[^882]སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1016]
སེར་སྣ་མེད་པས་མ་ཞུམ་པར་སེམས་བསྐྱེད་པ་དང་ཞེས་བྱ་བ་ལ། སེར་སྣའི་དབང་གིས་དངོས་པོ་གཏོང་བར་མི་ནུས་པའམ། ཅུང་ཟད་གཏོང་གི་ཐམས་ཅད་མི་གཏོང་བ་ནི་ཞུམ་པར་སེམས་བསྐྱེད་པ་སྟེ། དགའ་བ་དང་ལྡན་པ་ལ་སེར་སྣ་མེད་པས༌[^883]དངོས་པོ་ཐམས་ཅད་གཏོང་བའི་ཕྱིར་མ་ཞུམ་པར་སེམས་བསྐྱེད་པའོ། །

[Block 1017]
སློང་བ་ལ་སྦྱིན་པ༌[^884]བྱིན་ནས་ཞེས་བྱ་བ་ལ་དེ་ལྟར་མ་ཞུམ་པའི་སེམས་ཀྱིས༌[^885]སློང་བ་པོའི་གང་ཟག་རྣམས་ལ་ཕྱི་དང་ནང་གི་དངོས་པོའི་སྦྱིན་པ་བྱིན་ནས་བདག་དང་སློང་བ་པོ་དང་། སྦྱིན་པ་གསུམ་ཆར་ཡང་གཏོང་བའི༌[^886]རང་བཞིན་དུ་ལྟ་བ་ནི་འཁོར་གསུམ་ཡོངས་སུ་དག་པར་སྦྱངས་པ་སྟེ། དེ་བས་ན་སྦྱིན་པ་ལ་མཆོག་ཏུ་དགའ་བ༌[^887]ཞེས་བྱའོ། །

[Block 1018]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་རྣམས་ལ་དད་པ་ནི་གང་ཟག་ཚུལ་ཁྲིམས་དང་ལྡན་པ་རྣམས་ལ་སེམས་དང་བའོ། །

[Block 1019]
ཚུལ་ཁྲིམས་འཆལ་བ་རྣམས་ལ་རྗེས་སུ་འཛིན་ཅིང་བྱམས་པ་ཞེས་བྱ་བ་ལ་ཚུལ་ཁྲིམས་ཞིག་པའི་གང་ཟག་རྣམས་ནི་ཚུལ་ཁྲིམས༌[^888]འཆལ་བ་རྣམས་སོ། །

[Block 1020]
དེ་དག་མི་དགེ་བའི་ཆོས་ལ་ཕྱིས་མི་གཏོང་བ་ནི་རྗེས་སུ་འཛིན་པའོ། །
--- END BLOCKS ---
