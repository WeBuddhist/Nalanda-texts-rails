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
དེ་བཞིན་དུ་སོ་སོ༌[^691]སྐྱེ་བོའི་གནས་ཀྱི་ཚེ། དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར། ཀུན་ནས་ཉོན་མོངས་པ་མེད་ལ། གནས༌[^692]གྱུར་པའི་ཚེ་ཡང་ནམ་མཁའ་བཞིན་དུ་སྔོན་མ་བྱུང་བའི་རྣམ་པར་བྱང་བ་མེད་པའི་ཕྱིར། ཀུན་ནས་ཉོན་མོངས་པར་མ་ཡིན། རྣམ་པར་བྱང་བར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 982 [HEADING]]
###### དེ་ཁོ་ནའི་དོན་འཛིན་པ། ^1-2-2-1-5-0

[Block 983]
དེ་བཞིན་དུ་ཤེས་བྱའི་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་བརྟགས་པའི་ཚེ་དང་།[^693] ཆོས་ཐམས་ཅད་མ་སྐྱེས་པ་དང་། མ་འགགས་པའི་ཕྱིར་ཆོས་ཉིད་ལ་སྐྱེ་བ་དང་། འགག་པ་མ་མཐོང་བས། སྐྱེ་བར་མ་ཡིན་འགག་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 984 [HEADING]]
###### ས་ནས་ས་གཞན་དུ་འཕར་བ། ^1-2-2-1-6-0

[Block 985]
ས་འོག་མ་ནས་ས་གོང་མར་འཕར་བའི་ཚེ་ཡང་དོན་དམ་པར་ས་གོང་མར་རྟོགས་པའི་ཆོས་ཁྱད་པར་དུ་འཕགས་པ་ཡང་མི་འཛིན་ལ། ས་འོག་མར་རྟོགས་པའི་ཆོས་ངན་པ་ཡོངས་སུ་གཏོང་བ་ཡང་མེད་པའི་ཕྱིར། གཟུང་བར་མ་ཡིན་མི་གཟུང་བར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 986 [HEADING]]
###### ས་གཞན། ^1-2-2-1-7-0

[Block 987]
དེ་བཞིན་དུ་ས་གོང་མ་ལ་གནས་པར་བྱ་བའི་རྣམ་པར་རྟོག་པ་མེད་ཅིང་། ས་འོག་མ་ལ་གནས་པར་མི་བྱ་བའི་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར། གནས་པ་དང་མི་གནས་པ་གཉི་ག་ཡང་ཀུན་བརྟགས་པ་ཙམ་དུ་ཟད་པས། དེའི་ཕྱིར་གནས་པར་མ་ཡིན་མི་གནས་པར༌[^694]མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 988 [HEADING]]
###### སྒྲུབ་པ། ^1-2-2-1-8-0

[Block 989]
དེ་བཞིན་དུ་ཞི་གནས་དང་ལྷག་མཐོང་སྒྲུབ་པ་ལ་སྦྱོར་བ་ན་སྒྲུབ་པ་དེ་ལ་འདི་ནི་ཡང་དག་པར་སྒྲུབ་པའོ། །

[Block 990]
འདི་ནི་ཡང་དག་པ་མ་ཡིན་པའི་སྒྲུབ་པའོ་ཞེས་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར། ཡང་དག་པར་མ་ཡིན་ལོག་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 991 [HEADING]]
###### ཡིད་ལ་བྱེད་པ། ^1-2-2-1-9-0

[Block 992]
དེ་བཞིན་དུ་དེ་ཉིད་ལ་ཡང་དག་པའི་ཡིད་ལ་བྱེད་པས་མངོན་པར་བརྩོན་པའི་ཚེ་ཡང་འདི་ནི་རིགས་པས་བསྐྱེད་པའི༌[^695]ཡིད་ལ་བྱེད་པའོ། །

[Block 993]
འདི་ནི་མི་རིགས་པས་བསྐྱེད་པའོ་ཞེས་བྱ་བའི་རྣམ་པར་རྟོག་པ་མི་འབྱུང་བའི་ཕྱིར། རིགས་པར༌[^696]མ་ཡིན། མི་རིགས་པར༌[^697]མ་ཡིན་ནོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 994 [HEADING]]
###### སྤོང་བ། ^1-2-2-1-10-0

[Block 995]
དེ་བཞིན་དུ་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པའི་ཕྱོགས་ཀྱི༌[^698]གནས་ངན་ལེན་རྣམས་སྤོང་བ་ན་ཉོན་མོངས་པའི་རྣམ་པར་རྟོག་པ་ཕྲ་མོ་རིམ་གྱིས་སྤོང་ཡང་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་མི་འབྱུང་བའི་ཕྱིར། བག་ཙམ་མ་ཡིན༌[^699]པར་མ་ཡིན༌[^700]ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 996 [HEADING]]
###### རབ་ཏུ་རྟོགས་པ། ^1-2-2-1-11-0

[Block 997]
དེ་བཞིན་དུ་རབ་ཏུ་རྟོགས་པའི་ཚེ་ཡང་དོན་དམ་པ་དེ་བཞིན་ཉིད་ཀྱི་བདག་ཉིད་ལས༌[^701]སའི་རིམ༌[^702]ཀུན་ཏུ་འགྲོ་བའི་དོན་དང་མཆོག་གི་དོན་དང་རྒྱུ་མཐུན་པའི་དོན་དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་དག་པ་མེད་པའི་དོན་དང་། དམན་པ་མེད་པ་དང་། ལྷག་མ་མེད་པའི་དོན་ཅེས་བྱ་བ་ལ་སོགས་པའི་རིམ་པས་ཆ་ཤས་ཀྱིས་རབ་ཏུ་རྟོགས་པར་བྱེད་པའི་ཚེ་ཡང་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར། ཆ་ཤས་སུ་མ་ཡིན། ཆ་ཤས་མེད་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 998 [HEADING]]
###### ཆོས་ཉིད་མངོན་སུམ་དུ་བྱེད་པ། ^1-2-2-1-12-0

[Block 999]
ཆོས་ཉིད་མངོན་སུམ་དུ་བྱེད་པའི་ཚེ་ཡང་ཆོས་ཉིད་རབ་ཏུ་རྫོགས་པར༌[^703]བྱེད་པ་ན་ཆོས་ཀྱི་རྣམ་པ་དང་ཆོས་མ་ཡིན་པར་རྣམ་པར་བརྟགས་ན༌[^704]གཏན་གྱི་དངོས་པོའི་བདག་ཉིད་དུ་མི་སྣང་བའི་ཕྱིར། ཆོས་སུ་མ་ཡིན། ཆོས་མ་ཡིན་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1000 [HEADING]]
###### དེ་བཞིན་ཉིད་སྒོམ་པ། ^1-2-2-1-13-0

[Block 1001]
དེ་བཞིན་ཉིད་སྒོམ་པའི༌[^705]ཚེ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་འམ་གཞན་ནོ་ཞེས་བྱ་བའི་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར། དེ་བཞིན་ཉིད་དུ་མ་ཡིན་དེ་བཞིན༌[^706]ཉིད་མ་ཡིན་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1002 [HEADING]]
###### མྱ་ངན་ལས་འདས་པ། ^1-2-2-1-14-0

[Block 1003]
མྱ་ངན་ལས་འདས་པའི་ཚེ་ཡང་ཡང༌[^707]དག་པའི་དོན་གྱི་མཐའོ་ཞེས་བྱ་བ་དེ་ལས་བཟློག་པའོ་ཞེས་བྱ་བར་འཛིན་པ་མེད་པའི་ཕྱིར། ཡང་དག་པའི་མཐའ༌[^708]མ་ཡིན་ཡང་དག་པའི་མཐའ་མ་ཡིན་པར་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1004]
འདི་ནི་གཉིས་སུ་མེད་པའི་དོན་ཏོ་ཞེས་བྱ་བ་ལ། དོན་ཅེས་བྱ་བ་འདི་ནི་བརྗོད་པར་བྱ་བའི་རྣམ་གྲངས་དང་། དམིགས་པའི་རྣམ་གྲངས་ཏེ། གཉིས་སུ་མེད་པ་འདི་ནི་བཤད་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བརྗོད་པར་བྱ་བའི་དོན་དང་རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དམིགས་པའི་ཚེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དོན་ནི་དམིགས་པའོ་ཞེས་བཤད་པའོ། །

[Block 1005]
དེའི་འོག་ཏུ་དོན་དང་ལྡན་ལ་ཚིག་འབྲུ་དང་ལྡན་པར༌[^709]ཞེས་བྱ་བའི་འགྲེས་ཀྱིས་ནི་བདག་གིས་བཟུང་བའི༌[^710]བསོད་ནམས་པས་བཤད་པའི་བསོད་ནམས་ཆེ་བར་སྟོན་ཏོ། །

[Block 1006]
དེའི་འོག་ཏུ་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཐམས་ཅད་ལ་བདེ་བའི་ཡོ་བྱད་ཐམས་ཅད་ཀྱིས་མཆོད་པ་བྱས་པའི་བསོད་ནམས་པས༌[^711]འདི་བཤད་པའི་བསོད་ནམས་ཆེ་བའི་འགྲེས་དང་། བསྐལ་པ་ཚད་མེད་གྲངས་མེད་དཔག་ཏུ་མེད་པར་དམིགས་པའི་ཚུལ་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སྤྱད་པ་བས་དམིགས་པ་མེད་པའི་ཚུལ་དུ་བཤད་པ་བསོད་ནམས་ཆེ་བའི༌[^712]འགྲེས་དང་། དམིགས་པ་དང་བཅས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འགྲེས་སོ། །

[Block 1007 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྟར་བཅོས་པའི་འགྲེས། ^1-2-2-2-0

[Block 1008]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྟར་བཅོས་པའི་འགྲེས་བཞི་སྟེ། དམིགས་པ་དང་བཅས་པའི་སྒོམ་པ་བསྟན་པའི་འགྲེས་ནི་དང་པོའོ། །

[Block 1009]
འབྲས་བུ་དང་བཅས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པའི་འགྲེས་ནི་གཉིས་པའོ། །

[Block 1010]
བསོད་ནམས་ཀྱི་ཕུང་པོ་དཔག་ཏུ་མེད་པ་འཐོབ་པའི་འགྲེས་ནི་གསུམ་པའོ། །

[Block 1011]
རྗེས་སུ་ཡི་རང་བ་དང་ཡོངས་སུ་བསྔོ་བ་བསྟན་པའི་འགྲེས་ནི་བཞི་པའོ། །

[Block 1012 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་དག་པ་བསྟན་པའི་འགྲེས། ^1-2-2-3-0

[Block 1013]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་དག་པ་བསྟན་པའི་འགྲེས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། མི་དམིགས་པར་གདམས་པའི་འགྲེས་ནི་དང་པོའོ། །

[Block 1014]
ཆོས་ཐམས་ཅད་ལ་མི་ལྟ་བ་དང་། མཆོག་ཏུ་འཛིན་པ་ལས་ཡང་དག་པར་གནས་པའི་འགྲེས་ནི་གཉིས་པའོ། །

[Block 1015]
དེའི་འོག་ཏུ་འཛམ་བུའི་གླིང་དང་། གླིང་བཞི་པ་དང་། སྟོང་གཅིག་དང་། སྟོང་གཉིས་དང་། སྟོང་གསུམ་དང་། ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་སེམས་ཅན་རྣམས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་བཀོད་པ༌[^713]བསོད་ནམས་པས་གཞན་དག་ལ་བཤད་པའི་བསོད་ནམས་ཆེ་བར་བསྟན་པའི་འགྲེས་དྲུག་དང་། དེ་བཞིན་དུ་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ནས་རང་བྱང་ཆུབ་ཀྱི་བར་ལ་བཀོད་པའི་བསོད་ནམས་པས། གཞན་དག་ལ་བཤད་པའི་བསོད་ནམས་ཆེ་བར་བསྟན་པ་ཡང་འཛམ་བུའི་གླིང་དང་། གླིང་བཞི་པ་ལ་སོགས་པའི་དབང་གིས་འགྲེས་དྲུག་གོ། །

[Block 1016]
དེ་བཞིན་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཡང་དག་པར་འཛིན་དུ་འཇུག་པའི་བསོད་ནམས་པས་བཤད་པའི་བསོད་ནམས་ཆེ་བར་བསྟན་པ་ཡང་འཛམ་བུའི་གླིང་དང་། གླིང་བཞི་པ་ལ་སོགས་པའི་དབང་གིས་འགྲེས་དྲུག་གོ། །

[Block 1017]
དེ་བཞིན་དུ་ཕྱིར་མི་ལྡོག་པའི་ས་ལ་བཀོད་པའི༌[^714]ཡང་འགྲེས་དྲུག་གོ། །

[Block 1018]
དེ་ནས་ཡང་ཕྱིར་མི་ལྡོག་པའི་ས་ལ་བཀོད་པ་དེ་དག་ལ་བཤད་པའི་བསོད་ནམས་པས་ཀྱང་གཅིག་གཅིག༌[^715]ལ་མྱུར་དུ་མངོན་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་བཤད་པའི་བསོད་ནམས་ཆེ་བ་བསྟན་པ་ལ་ཡང་འགྲེས་དྲུག་གོ། །

[Block 1019]
བརྒྱ་བྱིན་གྱིས་བསྟན་པའི་འགྲེས་དང་། གནས་བརྟན་རབ་འབྱོར་རྗེས་སུ་ཡི་རང་བའི་འགྲེས་ཏེ་འདིར་ནི་འགྲེས་དེ་རྣམས་བསྟན་ཏོ། །

[Block 1020]
དེ་ནས་ཡང་བསོད་ནམས་ཆེ་བར་བསྟན་པའི་སྐབས་འདི་ཉིད་དུ་རྗེས་སུ་ཡི་རང་བའི་བསོད་ནམས་ཀྱང་མཆོག་ཏུ་འགྱུར་བར་བསྟན་ནས། དེའི་འོག་ཏུ་བཤད་པའི་སྐབས་དབྱེ་བའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པས། བཙུན་པ་རབ་འབྱོར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ཅན་ཐམས་ཅད་དང་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་པ་རྣམས་ཀྱི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། སྒོམ་པ་ལ་རྗེས་སུ་ཡི་རང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དག་པས་བྱང་ཆུབ་སེམས་དཔའ་མི་དམིགས་པའི་ཡིད་ལ་བྱེད་པ་ལ་ཞུགས་པའི༌[^716]རྗེས་སུ་ཡི་རང་བ་དང་། ཡོངས་སུ་བསྔོ་བའི་བསོད་ནམས་གཅིག་མཆོག༌[^717]ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
