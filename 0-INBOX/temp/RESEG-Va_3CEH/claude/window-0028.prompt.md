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
ཤེས་བྱའི་མཚན་ཉིད་ལ་འཇུག་པ་ཞེས་བྱ་བའི་དོན༌[^665]གཞན་ཡང་། མང་དུ་ཐོས་པས་བསྒོས་པའི་གནས། །ཞེས་བྱ་བ་སྟེ། ཐེག་པ་ཆེན་པོ་ཡོངས་སུ་བསྒོམ་པའི༌[^666]བདག་ཉིད་ཀྱི་ངོ་བོའོ།[^667] །ཀུན་གཞི་རྣམ་པར་ཤེས་པས་བསྡུས་པ༌[^668]མ་ཡིན་ལ་ཞེས་བྱ་བ་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལྟར་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པས་བསྡུས་པའི་ས་བོན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་ཀྱི་རྒྱུ་ཡིན་པ་དེ་བཞིན་དུ་དེ་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཀྱི༌[^669]རྒྱུར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ།[^670] །

[Block 982]
ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པས་བསྡུས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལྟ་བ་དང་བཅས་པའི་ཡིད་ཀྱིས་བརྗོད་པ་རྣམས་ཀྱི་ཡང་སྟེ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ལས་ཆོས་དང་དོན་གྱི་རྣམ་པ་འབྱུང་བར་འགྱུར་བའི༌[^671]རྒྱུ་ཡིན་ནོ། །

[Block 983]
ཚུལ་ཅན་བཟུང་བའི༌[^672]དངོས་པོ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གཟུགས་སུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 984]
ལྟ་བ་དང་བཅས་པའི༌[^673]ཞེས་བྱ་བ་ནི་ལྟ་བར་གྱུར་པ་རྣམས་སོ། །

[Block 985]
དེ་དག་ཉིད་ནི་རྒྱུ་མཚན་དང་ལྟ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པར༌[^674]རྣམ་པར་འཇོག་པར་འགྱུར་རོ། །

[Block 986 [HEADING]]
#### སུ་ཞིག་འཇུག་པ། ^3-2-2-0

[Block 987]
དེ་ལྟ་བུའི་རྣམ་པ་ལ་འཇུག་པ་ན་སུ་ཞིག་འཇུག་པ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་ཐེག་པ་ཆེན་པོ་སྨོས་པས་ནི་ཉན་ཐོས་ལ་སོགས་པའི་ཐེག་པ་སྤང་བའི་དོན་ཏོ། །

[Block 988]
སངས་རྒྱས་འབྱུང་བ་ཚད་མེད་པ་མཉེས་པར་བྱ་བ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་གྲངས་ལས་ཤིན་ཏུ་འདས་པའི་སངས་རྒྱས་འབྱུང་བ་མཉེས་པར་བྱ་བ་གང་གིས་ཐོབ་པར་གྱུར་པ་སྟེ། སངས་རྒྱས་མངོན་སུམ་དུ་བྱས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 989]
གཅིག་ཏུ་མོས་པ་ཅན་ཞེས་བྱ་བ་ནི་གང་གི༌[^675]མོས་པ་ཐེག་པ་ཆེན་པོ་ལས་བསྐྱོད་པར་མི་ནུས་པ་སྟེ། འདས་མ་ཐག་པར་བཤད་པའི་དགེ་བའི་རྩ་བ་བསགས་པའི་རྒྱུ་རྣམ་པ་གསུམ་པོ་དང་། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལེགས་པར་བསགས་པ་ནི་མི་དགེ་བའི་གྲོགས་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 990 [HEADING]]
#### འཇུག་པའི་གནས། ^3-2-3-0

[Block 991]
དེ་ལྟ་བུའི་རྣམ་པས་འཇུག་པའི་གནས་བསྟན་པར་བྱ་བའི་ཕྱིར་སྨྲས་པ། ཡིད་ཀྱི་བརྗོད་པ་སྟེ་ཡིད་ཀྱི་རྣམ་པར་རྟོག་པའོ། །

[Block 992]
དེ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་གང་འབྱུང་བའི་རྒྱུར་གྱུར་པའོ། །

[Block 993 [HEADING]]
##### མོས་པས་སྤྱོད་པའི་ས་ལ་འཇུག་པ། ^3-2-3-1-0

[Block 994]
ཡང་དེ་ཉིད་དུ་ཡིད་ཀྱི་བརྗོད་པའི་བྱེ་བྲག་གང༌[^676]གིས་གང་དག་འཇུག་པ་དེ་ནི་མོས་པས་སྤྱོད་པའི་ས་ལ༌[^677]འཇུག་པར་འགྱུར་ཏེ། འདི་ལྟར་དེ་ཆོས་ཐམས་ཅད་རྣམ་པར་རིག་པ་ཙམ་དུ་རྗེས་སུ་སྒྲོགས་པ་ལ་མོས་པ་སྐྱེད་པར་བྱེད་དེ། དེས་ན་དེ་དག༌[^678]ནི་དེར་ཞུགས་པ་ཞེས་བརྗོད་དོ། །

[Block 995 [HEADING]]
##### མཐོང་བའི་ལམ་ལ་འཇུག་པ། ^3-2-3-2-0

[Block 996]
དེ་ཇི་ལྟར་མཐོང་བའི་ལམ་ལ་འཇུག་པ་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ།[^679] །ཇི་ལྟ་བ་བཞིན་དུ་དེ་རབ་ཏུ་རྟོགས་པ་དང་ཞེས་བྱ་བ་སྟེ། ཡིད་ཀྱི་བརྗོད་པ་དེ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་རྟོགས་པའོ། །

[Block 997]
ཇི་ལྟར་ན་དེ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་རྟོགས་ཤེ་ན། ཇི་ལྟར་ཆོས་མེད་པ། དོན་མེད་པ། གཟུང་བ་མེད་པ། འཛིན་པ་མེད་པའོ་ཞེས་ཡིད་ཀྱི་བརྗོད་པ་རྟོགས་པ་གང་ཡིན་པའོ། །

[Block 998 [HEADING]]
##### བསྒོམ་པའི་ལམ་ལ་འཇུག་པ། ^3-2-3-3-0

[Block 999]
བསྒོམ་པའི༌[^680]ལམ་ལ་འཇུག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་གཉེན་པོ་བསྒོམ་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་རྟོགས་པ་དེ་ཉིད་གོམས་པར་བྱེད་པ་ནི་སྒོམ་པར༌[^681]གྱུར་པའོ། །

[Block 1000]
དེ་ལྟ་བས་ན་རྣམ་པར་མི་རྟོག་པ༌[^682]ལ་སོགས་པ་དེ་དག་གིས་གང་རྟོགས་པ་དེ་ཉིད་ཀྱིས་སྒྲིབ་པ་རྣམ་པར་སྦྱོང་བར་བྱེད་པའོ། །

[Block 1001 [HEADING]]
##### མཐར་ཕྱིན་པའི་ལམ་ལ་འཇུག་པ། ^3-2-3-4-0

[Block 1002]
མཐར་ཕྱིན་པའི་ལམ་ལ་འཇུག་པ་དེ་བསྟན་པའི་ཕྱིར་སྒྲིབ་པ་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཡེ་ཤེས་ཀྱི༌[^683]དུས་སྐབས་ན་ཤིན་ཏུ་ཕྲ་བའི་སྒྲིབ་པ་ཡང་མེད་པ་ནི་མཐར་ཕྱིན་པའི་ལམ་ལ་འཇུག་པའོ། །

[Block 1003 [HEADING]]
#### གང་གིས་འཇུག་པ། ^3-2-4-0

[Block 1004 [HEADING]]
##### དགེ་བའི་རྩ་བའི་སྟོབས་སྐྱེད་པ། ^3-2-4-1-0

[Block 1005]
གང་གིས་འཇུག་པ་སྟོན་པར་བྱེད་པ་ནི་དགེ་བའི་རྩ་བའི་སྟོབས་སྐྱེད་པ༌[^684]དང་། རྣམ་པ་གསུམ་གྱིས་སེམས་གཟེངས་བསྟོད་པ་ཞེས་བྱ་བ་སྟེ། དགེ་བའི་རྩ་བའི་སྟོབས་སྐྱེད་པའི༌[^685]བྱང་ཆུབ་སེམས་དཔའ་ནི་དེའི་སྟོབས་ཀྱིས་བསྟན་པའི༌[^686]ཕྱིར་སེམས་འགོང་བར་མི་འགྱུར་ཏེ།

[Block 1006 [HEADING]]
##### རྣམ་པ་གསུམ་གྱིས་སེམས་སྦྱོང་བ། ^3-2-4-2-0

[Block 1007]
རྣམ་པ་གསུམ་གྱིས་སེམས་སྦྱོར་བས་ཀྱང་སེམས་གཟེངས་བསྟོད་པ་ཉིད་དོ། །

[Block 1008]
དེ་ལ་སྦྱོར་བ་གཉིས་པ་གང་ཡིན་པ་ཇི་ལྟར་སྦྱོར་བ་ཡིན་པ་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདི་ལྟ་སྟེ། སེར་སྣ་ལ་སོགས་པའི་སྒྲིབ་པ་སྤངས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྣམ་པར་འཆིང་བ་མེད་པ་ཉིད་ཀྱིས་དེ་རྣམས་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 1009]
དེ་ཡོངས་སུ་རྫོགས་པ་ཡང་སངས་རྒྱས་ཉིད་ཡིན་ཏེ། ཆོས་དང་དོན་ལ་དམིགས་པ་ལ་སོགས་པ་ནས། བག་ཡོད་པ་ཞེས་བྱ་བའི་བར་གྱིས་སོ། །

[Block 1010]
དེ་ལ་རྟག་ཏུ་ཞེས་པ་ནི་རྟག་ཏུ་བྱེད་པ་ཉིད་དོ། །

[Block 1011]
གུས་པར་བྱས་ཏེ་སྦྱོར་བ་ནི་བླ་མར་བྱེད་པ་ཉིད་དོ། །

[Block 1012]
གང་གང༌[^687]དུ་བསྟན་པའི་རྣམ་པ་ཉིད་དེ་དེ༌[^688]ནི་བག་ཡོད་པའོ། །

[Block 1013]
གསུམ་པ་གང་ཡིན་པ་དེ་བསྟན་པར་བྱ་སྟེ་དེ་ལ་དགེ་བ་སྒྲིབ་པ་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་དགེ་བ་སྒྲིབ་པ་དང་བཅས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1014]
དེའི་ཕྱིར་བདག་དགེ་བ་སྒྲིབ་པ་མེད་པ་དང་ཤིན་ཏུ་ལྡན་པ་ནི་སངས་རྒྱས་སུ་མི་འགྱུར་བ་ཉིད་ནི་རིགས་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བའོ། །

[Block 1015]
དེ་དག་གི་དོན་ཚིགས་སུ་བཅད་པས་སྟོན་པ། དེའི་ཕྱིར་ཞུམ་པར་མི་བྱའོ། །ཞེས་བྱ་བ་ནི་སེམས་ཞུམ་པ་ཉིད་དུ་སེམས་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

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
--- END BLOCKS ---
