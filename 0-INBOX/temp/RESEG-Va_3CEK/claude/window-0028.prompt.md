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
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཏེ།

[Block 982 [VERSE]]
སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུའོ། །
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི༌[^713]བཞི་སྟེ།
རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 983]
ཡང་གོ་རིམས་བཞིན་ཞེས་སྨོས་པ་ནི་དབུས་སུ་ཡང་ཐོག་མ་དང་ཐ་མ་བཞིན་ཤེས་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་ནི་མཐུན་པར་སྦྱོར་བའི༌[^714]ཆོས་ཡིན་ནོ། །

[Block 984 [HEADING]]
### རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་ལ་སོགས་པའི་ལས། ^1-57-0

[Block 985]
ལས་བསྟན་པའི་སྐབས་སུ་འདི་ཡང་ཡོངས་སུ་བྲི་བར༌[^715]བྱ་སྟེ།

[Block 986]
བསྟན་བཅོས་དག་ལས།

[Block 987]
རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་དང་། རིགས་པས་བསྐྱེད་པ་དང་། རིགས་པས་བསྐྱེད་པ་ཡང་མ་ཡིན་རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་ཡང་མ་ཡིན་པའི་ལས་ཞེས་གསུངས་པ་དེའི་མཚན་ཉིད་ཅི་ཞེ་ན།

[Block 988 [VERSE]]
རིགས་མིན་བསྐྱེད་པ་ཉོན་མོངས་ཅན། །
ཁ་ཅིག་ཆོ་ག་ཉམས་པ་ཞེའོ། །

[Block 989]
ཁ་ཅིག་ན་རེ་རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་ནི་ལས་ཉོན་མོངས་པ་ཅན་ཡིན་ཏེ། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད༌[^716]ལས་བྱུང་བ་ལས་བྱེད་པ༌[^717]ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 990]
གཞན་དག་ན་རེ་ཆོ་ག་ཉམས་པ་ཡང་ཡིན་ཏེ། གང་གིས་ཇི་ལྟར་འགྲོ་བར་བྱ་བ་དང་། གནས་པར་བྱ་བ་དང་། བཟའ་བར་བྱ་བ་དང་། བགོ་བར་བྱ་བ་དང་། དེ་ལ་སོགས་པ་དེ་གཞན་དུ་བྱེད་ན་དེ༌[^718]ནི་རིགས་པ་མ་ཡིན་པས་བྱེད་པའི་ཕྱིར་རིགས་པ་མ་ཡིན་པས་སྐྱེས་པ༌[^719]ཞེས་བྱའོ། །

[Block 991]
རིགས་པས་བསྐྱེད་པ་ནི་ལས་དགེ་བ་ཡིན་ནོ། །

[Block 992]
གཞན་དག་ན་རེ་ཆོ་ག་མ་ཉམས་པ་ཡང་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 993]
དེ་གཉིས་ལས་གཞན་པ་ནི་གཉི་ག་མ་ཡིན་པའོ། །

[Block 994 [HEADING]]
### ལས་གཅིག་གིས་སྐྱེ་བ་གཅིག་འཕེན་པ། ^1-58-0

[Block 995]
ཅི་ལས་གཅིག་གིས་སྐྱེ་བ་གཅིག་ཁོ་ན་འཕེན་ཏམ་འོན་ཏེ་དུ་མ་ཡང་འཕེན། དེ་བཞིན་དུ་ལས་དུ་མས་ཀྱང་སྐྱེ་བ་གཅིག་འཕེན་ཏམ། འོན་ཏེ་དུ་མ་ཁོ་ན་ཞིག་འཕེན་ཞེ་ན། འདི་ནི་གྲུབ་པའི་མཐའ་ཡིན་ཏེ། གཅིག་གིས༌[^720]སྐྱེ་བ་གཅིག་འཕེན༌[^721]ཏོ། །

[Block 996]
ལས་གཅིག་ཁོ་ནས་སྐྱེ་བ་གཅིག་ཁོ་ན་འཕེན་གྱི་དུ་མ་ནི་མ་ཡིན་ནོ། །

[Block 997]
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་རིས་མཐུན་པ་ལ་བྱ་སྟེ། དེར་ཕྱིན་ནས་སྐྱེ་བ་ཞེས་བརྗོད་དོ། །

[Block 998]
འོ་ན་གནས་བརྟན་མ་འགགས་པས་བདག་ནི་བསོད་སྙོམས་གཅིག་པོ་དེའི་རྣམ་པར་སྨིན་པས་ལན་བདུན་གྱི་བར་དུ་སུམ་ཅུ་རྩ་གསུམ་པའི་ལྷ་རྣམས་ཀྱི་ནང་དུ་སྐྱེས་པ་ནས་ད་ལྟར་ཤཱཀྱ་ཕྱུག་པོའི་རིགས་སུ་སྐྱེས་པའི་བར་དུ་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་ཇི་ལྟ་བུ་ཞེ་ན། འདི་དེས་འབྱོར་པ་རྙེད་ནས་ཚེ་རབས་དྲན་པ་དང་ཡང་བསོད་ནམས་གཞན་བྱས་པས་དེའི་ཕྱིར༌[^722]སློབ་པ་སྟོན་པར་བྱེད་པ་ཡིན་ཏེ། དཔེར་ན་མི་ཞིག་གིས་དོང་ཙེ་གཅིག་གིས་སྟོང་དུ་བསྒྱུར༌[^723]ཏེ་བདག་ནི་དོང་ཙེ་གཅིག༌[^724]གིས་དབང་ཕྱུག་འདི་ཐོབ་པར་གྱུར་ཏོ་ཞེས་སྨྲ་བ་ལྟ་བུའོ། །

[Block 999]
ཡང་སྨྲས་པ། དེ་བསོད་སྙོམས་དེ༌[^725]ལ་བརྟེན་ཏེ་སེམས་པ་རྣམས་ཀྱི་རྒྱུན་མང་པོ་བྱུང་ནས་འགའ་ཞིག་གི༌[^726]འབྲས་བུ་འགའ་ཡོངས་སུ་གཟུང་བ་ཡིན་ནོ། །

[Block 1000]
རིས་མཐུན་པ་དུམ་བུར་འཕེན་པ༌[^727]འགྱུར་དུ་འོངས་པས༌[^728]དུ་མས་ཀྱང་གཅིག་འཕེན་པ་མ་ཡིན་གྱི་ལས་གཅིག་གིས་འཕངས་པའི་རིས་མཐུན་པ་ལ་ལས་ཡོངས༌[^729]རྫོགས་བྱེད་པ་དུ་མ་ཡིན་པར་འདོད་དེ། དཔེར་ན་རི་མོ་མཁན་གྱི༌[^730]རི་ལུ་གཅིག་གིས་གཟུགས་ཀྱི་ས་བཅད་ནས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་འདྲ་སྟེ། འདི་ལྟར་མིར་མཚུངས་མོད་ཀྱི། ཁ་ཅིག་དབང་པོ་དང་ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་ཚང་བར་འགྱུར་ཞིང་། ཁ་དོག་དང་ཤ་ཚུགས་དང་བོང་ཚོད་དང་ཉམས་སྟོབས་ཕུན་སུམ་ཚོགས་པས་རྣམ་པར༌[^731]མཛེས་པ་ཡིན་ལ། ཁ་ཅིག་ནི་དེ་དག་ལས་ལ་ལ་མ་ཚང་བ་ཡིན་ནོ། །

[Block 1001]
ལས་འབའ་ཞིག་ཚེ་འཕེན་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་གཞན་ཡང་ཡིན་ནོ། །

[Block 1002]
རྣམ་པ་ཐམས་ཅད་དུ། སེམས་མེད་སྙོམས་པར་འཇུག་པ་དང་།[^732] །འཕེན་བྱེད་མ་ཡིན་ཐོབ་པའང་ཡིན། །རྣམ་པར་སྨིན་པ་དང་བཅས་པ་སེམས་མེད་པའི༌[^733]སྙོམས་པར་འཇུག་པ་དག་གིས་ཀྱང་རིས་མཐུན་པ་འཕེན་པར་མི་བྱེད་དེ།

[Block 1003 [VERSE]]
[^734]ལས་དང་ལྷན་ཅིག་མི་འབྱུང་བའི་ཕྱིར་རོ། །
ཐོབ་པ༌[^735]རྣམས་ཀྱིས་ཀྱང་མ་ཡིན་ཏེ།
ལས་དང་འབྲས་བུ་མ་ཡིན༌[^736]པའི་ཕྱིར་རོ། །

[Block 1004 [HEADING]]
### སྒྲིབ་པ་གསུམ། ^1-59-0

[Block 1005]
བཅོམ་ལྡན་འདས་ཀྱིས་ལས་ཀྱི་སྒྲིབ་པ་དང་། ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་། རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་དང་། སྒྲིབ་པ་གསུམ་གསུངས་པ་དེ་དག་གི་རང་བཞིན་ཅི་ཞེ་ན།

[Block 1006 [VERSE]]
མཚམས་མེད་པ་ཡི་ལས་རྣམས་དང་། །
ཉོན་མོངས་ཤས་ཆེན་ངན་འགྲོ་དང་། །
འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དང་། །
སྒྲ་མི་སྙན་སྒྲིབ་གསུམ་དུ་འདོད། །

[Block 1007]
མཚམས་མེད་པའི་ལས་རྣམས་ནི་ལས་ཀྱི་སྒྲིབ་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། མ་གསོད་པ་དང་། ཕ་གསོད་པ་དང་། དགྲ་བཅོམ་པ་གསོད་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པའི་སྐུ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་འབྱིན་པའོ། །

[Block 1008]
ཉོན་མོངས་པ་ཤས་ཆེན་པོ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 1009]
ཉོན་མོངས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཉོན་མོངས་པ་ཤས་ཆེ་བ་དང་རྣོ་བའོ། །

[Block 1010]
དེ་ལ་ཤས་ཆེ་བ་ནི་རྒྱུན་དུ་འབྱུང་བ་གང་ཡིན་པའོ། །

[Block 1011]
རྣོ་བ་ནི་ཆེན་པོ་གང་ཡིན་པའོ། །

[Block 1012]
དེ་ལ་ཤས་ཆེ་བ་གང་ཡིན་པ་དེ་ནི་སྒྲིབ་པ་ཡིན་ཏེ། དཔེར་ན་ཟ་མ་ལ་སོགས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 1013]
ཉོན་མོངས་པ་རེས་འགའ་འབྱུང་བ་ནི་ཤུགས་དྲག་ཀྱང་གཞོམ་པར་ནུས་ཀྱིས༌[^737]རྒྱུན་དུ་འབྱུང་བ་ནི་དཔལ༌[^738]ཡང་མ་ཡིན་ཏེ། ཉོན་མོངས་པ་རྒྱུན་དུ་འབྱུང་བ་ནི་དེ་ངེས་པར་གཞོམ་པའི་ཕྱིར་རྩོལ་བའི་དུས་མི་རྙེད་དོ། །

[Block 1014]
དེ་ནི་ཆུང་ངུ་ལ་བརྟེན་ནས་འབྲིང་སྐྱེའོ། །

[Block 1015]
འབྲིང་ལ་བརྟེན་ནས་ཆེན་པོ་སྐྱེ་སྟེ། དེ་ལྟ་བས་ན་དེ་ཉིད་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 1016]
ངན་འགྲོ་རྣམ་པ་གསུམ་དང་། བདེ་འགྲོའི་ཕྱོགས་བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན༌[^739]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 1017]
འདི་དག་གང་ལ་སྒྲིབ་ཅེ་ན། འཕགས་པའི་ལམ་དང་། འཕགས་པའི་ལམ་ལ་སྦྱོར་བར་བྱེད་པའི་དགེ་བའི་རྩ་བ་རྣམས་ལ་སྒྲིབ་བོ། །

[Block 1018]
ངན་སོང་ལ་སོགས་པར་ངེས་པར་འགྱུར་བ་དང་། སྒོ་ང་ལས་སྐྱེ་བར་འགྱུར་བ་དང་། དྲོད་གཤེར་ལས་སྐྱེ་བར་འགྱུར་བ་དང་། བུད་མེད་ཉིད་དུ་འགྱུར་བ་དང་། སྲིད་པ་བརྒྱད་པར་ངེས་པར་འགྱུར་བའི་ལས་གཞན་དང་གཞན་དག་ཀྱང༌[^740]བརྗོད་པར་བྱ་བར་འགྱུར་རོ་ཞེ་ན། གང་དག་གཞི་དང་། འབྲས་བུ་དང་། འགྲོ་བ་དང་། སྐྱེ་བ་དང་། གང་ཟག་དང་། རྒྱུ་ལྔས་བསྟན་པར་སླ་ཞིང་གདགས་པར་བྱ་བ་དེ་དག་ཁོ་ན་བཤད་ཀྱིས༌[^741]གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 1019]
དེ་དག་ལས་ཉོན་མོངས་པའི་སྒྲིབ་པ་ནི་ཐམས་ཅད་ཀྱི་ཐ་ཤལ་ཡིན་ནོ། །

[Block 1020]
དེའི་འོག་ཏུ་ནི་ལས་ཀྱི་སྒྲིབ་པ་སྟེ། དེ་གཉིས་ཀྱིས་ནི་ཚེ་ཕྱི་མ་ལ་ཡང་གསོར་མི་རུང་བར་འགྱུར་རོ། །
--- END BLOCKS ---
